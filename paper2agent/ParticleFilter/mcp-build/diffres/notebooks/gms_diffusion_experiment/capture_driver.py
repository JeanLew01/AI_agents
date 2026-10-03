"""Capture driver for experiments/gms/diffusion.py (execution_id = gms_diffusion_experiment).

Runs the UNMODIFIED upstream script (repo/diffres/experiments/gms/diffusion.py) with runpy, once per
configuration, from the scratch working directory work_capture/ (which holds a copy of rnd_keys.npy and the
./gms/results/ folder the script writes to). It does not re-implement anything. To record the exact inputs of
the diffusion_resampling call without changing the compiled computation it:
  * wraps `jax.jit` so that the script's jitted functions named `resampling` and `swd` record their concrete call
    arguments and outputs (the real jax.jit object is created with the same function and kwargs, so the XLA
    program is identical);
  * wraps `diffres.resampling.diffusion_resampling` at trace time only to record its static arguments
    (a, ts, integrator, ode, jitter, einsum) and then calls the original function unchanged;
  * wraps `diffres.tools.gm_lin_posterior` (called eagerly) to record its inputs/outputs (needed to replay the
    script's residual metric).
Everything captured is written as float64/uint32 .npz plus a JSON with the arguments.

Usage (from work_capture/, through heavy.sh):
    python capture_driver.py <out_data_dir>
"""
import functools
import json
import os
import runpy
import sys

import numpy as np
import jax

ROOT = '/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres'
SCRIPT = f'{ROOT}/repo/diffres/experiments/gms/diffusion.py'

CONFIGS = {
    'A_jk_ode_T3_K128': ['--id_l=0', '--id_u=0', '--nsamples=1000', '--a=-1.', '--T=3.', '--nsteps=128',
                         '--integrator=jentzen_and_kloeden'],
    'B_euler_sde_T1_K8': ['--id_l=0', '--id_u=0', '--nsamples=1000', '--a=-1.', '--T=1.', '--nsteps=8',
                          '--integrator=euler', '--sde'],
}

CAP = {}

_real_jit = jax.jit


def recording_jit(fun=None, **kw):
    if fun is None:
        return lambda f: recording_jit(f, **kw)
    jf = _real_jit(fun, **kw)
    name = getattr(fun, '__name__', '')
    if name not in ('resampling', 'swd'):
        return jf

    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        out = jf(*args, **kwargs)
        CAP.setdefault(name, []).append((args, kwargs, out))
        return out

    return wrapper


import diffres.resampling as dres  # noqa: E402
import diffres.tools as dtools  # noqa: E402

_orig_dr = dres.diffusion_resampling
_orig_post = dtools.gm_lin_posterior


def recording_diffusion_resampling(key, log_ws, samples, a, ts, integrator='euler', ode=True, jitter=0.,
                                   einsum=False):
    static = dict(a=a, integrator=integrator, ode=ode, jitter=jitter, einsum=einsum)
    static['ts_is_tracer'] = isinstance(ts, jax.core.Tracer)
    if not static['ts_is_tracer']:
        static['ts'] = np.asarray(ts)
    static['a_is_tracer'] = isinstance(a, jax.core.Tracer)
    CAP.setdefault('diffusion_resampling_static', []).append(static)
    return _orig_dr(key, log_ws, samples, a, ts, integrator=integrator, ode=ode, jitter=jitter, einsum=einsum)


def recording_gm_lin_posterior(y, obs_op, obs_cov, ws, ms, covs):
    out = _orig_post(y, obs_op, obs_cov, ws, ms, covs)
    CAP.setdefault('gm_lin_posterior', []).append(((y, obs_op, obs_cov, ws, ms, covs), out))
    return out


def main(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    jax.jit = recording_jit
    dres.diffusion_resampling = recording_diffusion_resampling
    dtools.gm_lin_posterior = recording_gm_lin_posterior
    summary = {}
    for name, argv in CONFIGS.items():
        CAP.clear()
        sys.argv = [SCRIPT] + argv
        runpy.run_path(SCRIPT, run_name='__main__')
        jax.effects_barrier()
        assert len(CAP['resampling']) == 1 and len(CAP['swd']) == 1 and len(CAP['gm_lin_posterior']) == 1
        assert len(CAP['diffusion_resampling_static']) == 1, CAP['diffusion_resampling_static']
        (key, log_ws, prior_samples), _, (out_log_ws, out_samples) = CAP['resampling'][0]
        static = CAP['diffusion_resampling_static'][0]
        (post_samples, approx_samples_swd), swd_kwargs, err = CAP['swd'][0]
        (y, obs_op, obs_cov, vs, ms, covs), (post_vs, post_ms, post_covs) = CAP['gm_lin_posterior'][0]
        assert not static['ts_is_tracer'] and not static['a_is_tracer']
        assert np.array_equal(np.asarray(approx_samples_swd), np.asarray(out_samples))
        key_mc = np.load('rnd_keys.npy')[0]
        np.savez(f'{out_dir}/inputs_{name}.npz',
                 key=np.asarray(key), log_ws=np.asarray(log_ws), samples=np.asarray(prior_samples),
                 ts=static['ts'], a=np.float64(static['a']), integrator=np.str_(static['integrator']),
                 ode=np.bool_(static['ode']), jitter=np.float64(static['jitter']), einsum=np.bool_(static['einsum']),
                 key_mc=key_mc, y=np.asarray(y), obs_op=np.asarray(obs_op), obs_cov=np.asarray(obs_cov),
                 vs=np.asarray(vs), ms=np.asarray(ms), covs=np.asarray(covs),
                 post_vs=np.asarray(post_vs), post_ms=np.asarray(post_ms), post_covs=np.asarray(post_covs),
                 post_samples=np.asarray(post_samples))
        np.savez(f'{out_dir}/outputs_capture_{name}.npz',
                 approx_post_log_ws=np.asarray(out_log_ws), approx_post_samples=np.asarray(out_samples),
                 err=np.asarray(err))
        args = dict(script=SCRIPT, argv=argv, diffusion_resampling_call=dict(
            a=float(static['a']), ts_linspace=dict(start=float(static['ts'][0]), stop=float(static['ts'][-1]),
                                                   num=int(static['ts'].shape[0])),
            integrator=static['integrator'], ode=bool(static['ode']), jitter=float(static['jitter']),
            einsum=bool(static['einsum']), wrapped_in_jax_jit=True),
            swd_kwargs_passed=sorted(swd_kwargs), jax_enable_x64=bool(jax.config.jax_enable_x64),
            key_dtype=str(np.asarray(key).dtype), key=np.asarray(key).tolist(), key_mc=key_mc.tolist(),
            log_ws_dtype=str(np.asarray(log_ws).dtype), samples_dtype=str(np.asarray(prior_samples).dtype),
            samples_shape=list(np.asarray(prior_samples).shape))
        with open(f'{out_dir}/args_{name}.json', 'w') as fh:
            json.dump(args, fh, indent=1)
        summary[name] = dict(err=float(err), err_repr=repr(float(err)))
        print(name, summary[name], flush=True)
    print(json.dumps(summary, indent=1))


if __name__ == '__main__':
    main(sys.argv[1])
