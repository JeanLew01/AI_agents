"""Replay driver (execution_id = gms_diffusion_experiment).

Loads the inputs captured by capture_driver.py (data/inputs_<cfg>.npz) and calls the upstream
diffres.resampling.diffusion_resampling once more, exactly as experiments/gms/diffusion.py does (x64 enabled,
wrapped in jax.jit, same key/log_ws/samples/a/ts/integrator/ode). It then recomputes the script's two metrics with
the same upstream calls the script makes (ott sliced_wasserstein with PNormP(p=1), n_proj=1000; mean residual
einsum) and compares everything with the native, unmodified script output (work_native/gms/results/*.npz) and the
capture run. As an extra (non-reference) check it also calls diffusion_resampling eagerly (no outer jit).
Nothing is re-implemented. Writes data/replay_comparison.json and data/replay_outputs_<cfg>.npz.
"""
import json
import sys

import numpy as np
import jax
import jax.numpy as jnp

jax.config.update('jax_enable_x64', True)

from diffres.resampling import diffusion_resampling  # noqa: E402
from ott.tools.sliced import sliced_wasserstein  # noqa: E402
from ott.geometry.costs import PNormP  # noqa: E402

N = '/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/notebooks/gms_diffusion_experiment'
NATIVE = {
    'A_jk_ode_T3_K128': f'{N}/work_native/gms/results/diffres--1.0-3.0-128-jentzen_and_kloeden-ode-0.npz',
    'B_euler_sde_T1_K8': f'{N}/work_native/gms/results/diffres--1.0-1.0-8-euler-sde-0.npz',
}
CAPTURE_SCRIPT_NPZ = {
    'A_jk_ode_T3_K128': f'{N}/work_capture/gms/results/diffres--1.0-3.0-128-jentzen_and_kloeden-ode-0.npz',
    'B_euler_sde_T1_K8': f'{N}/work_capture/gms/results/diffres--1.0-1.0-8-euler-sde-0.npz',
}
CFG_T_NSTEPS = {'A_jk_ode_T3_K128': (3., 128), 'B_euler_sde_T1_K8': (1., 8)}


@jax.jit
def swd(samples1, samples2, wx=None, wy=None):
    return sliced_wasserstein(samples1, samples2, wx, wy, cost_fn=PNormP(p=1), n_proj=1000)[0]


def maxabs(x, y):
    x, y = np.asarray(x), np.asarray(y)
    assert x.shape == y.shape, (x.shape, y.shape)
    return float(np.max(np.abs(x - y))) if x.size else 0.0


def main():
    results = {'jax_version': jax.__version__, 'backend': jax.default_backend(),
               'x64': bool(jax.config.jax_enable_x64), 'configs': {}}
    for name, native_path in NATIVE.items():
        inp = np.load(f'{N}/data/inputs_{name}.npz')
        nat = np.load(native_path)
        capscript = np.load(CAPTURE_SCRIPT_NPZ[name])
        capout = np.load(f'{N}/data/outputs_capture_{name}.npz')
        key = jnp.asarray(inp['key'])
        log_ws = jnp.asarray(inp['log_ws'])
        samples = jnp.asarray(inp['samples'])
        a = float(inp['a'])
        ts = jnp.asarray(inp['ts'])
        integrator = str(inp['integrator'])
        ode = bool(inp['ode'])
        T, nsteps = CFG_T_NSTEPS[name]
        input_checks = dict(
            ts_equals_linspace_0_T_nsteps_plus_1=bool(np.array_equal(inp['ts'], np.asarray(jnp.linspace(0., T, nsteps + 1)))),
            log_ws_logsumexp=float(jax.scipy.special.logsumexp(log_ws)),
            ess=float(1. / np.sum(np.exp(inp['log_ws']) ** 2)),
            dtypes=dict(key=str(inp['key'].dtype), log_ws=str(inp['log_ws'].dtype), samples=str(inp['samples'].dtype)),
            shapes=dict(samples=list(inp['samples'].shape), ts=list(inp['ts'].shape)),
        )

        @jax.jit
        def resampling(key_, log_ws_, prior_samples_):
            return diffusion_resampling(key_, log_ws_, prior_samples_, a, ts, integrator=integrator, ode=ode)

        r_log_ws, r_samples = resampling(key, log_ws, samples)
        e_log_ws, e_samples = diffusion_resampling(key, log_ws, samples, a, ts, integrator=integrator, ode=ode)

        r_err = swd(jnp.asarray(inp['post_samples']), r_samples)
        approx_m = jnp.einsum('n,n...->...', jnp.exp(r_log_ws), r_samples)
        true_m = jnp.einsum('c,c...->...', jnp.asarray(inp['post_vs']), jnp.asarray(inp['post_ms']))
        r_residual = approx_m - true_m
        weighted_in_mean = np.einsum('n,nd->d', np.exp(inp['log_ws']), inp['samples'])

        np.savez(f'{N}/data/replay_outputs_{name}.npz', approx_post_log_ws=np.asarray(r_log_ws),
                 approx_post_samples=np.asarray(r_samples), err=np.asarray(r_err), residual=np.asarray(r_residual),
                 eager_approx_post_samples=np.asarray(e_samples))

        cmp = dict(
            input_checks=input_checks,
            capture_vs_native=dict(
                samples_bitwise_equal=bool(np.array_equal(capscript['approx_post_samples'], nat['approx_post_samples'])),
                log_ws_bitwise_equal=bool(np.array_equal(capscript['approx_post_log_ws'], nat['approx_post_log_ws'])),
                post_samples_bitwise_equal=bool(np.array_equal(capscript['post_samples'], nat['post_samples'])),
                err_bitwise_equal=bool(np.array_equal(capscript['err'], nat['err'])),
                residual_bitwise_equal=bool(np.array_equal(capscript['residual'], nat['residual'])),
                captured_post_samples_equal_native=bool(np.array_equal(inp['post_samples'], nat['post_samples'])),
                captured_outputs_equal_native=bool(np.array_equal(capout['approx_post_samples'], nat['approx_post_samples'])),
            ),
            replay_jit_vs_native=dict(
                samples_bitwise_equal=bool(np.array_equal(np.asarray(r_samples), nat['approx_post_samples'])),
                samples_max_abs_diff=maxabs(r_samples, nat['approx_post_samples']),
                log_ws_bitwise_equal=bool(np.array_equal(np.asarray(r_log_ws), nat['approx_post_log_ws'])),
                err_native=float(nat['err']), err_replay=float(r_err),
                err_abs_diff=abs(float(nat['err']) - float(r_err)),
                residual_native=nat['residual'].tolist(), residual_replay=np.asarray(r_residual).tolist(),
                residual_max_abs_diff=maxabs(r_residual, nat['residual']),
            ),
            replay_eager_vs_native=dict(
                samples_bitwise_equal=bool(np.array_equal(np.asarray(e_samples), nat['approx_post_samples'])),
                samples_max_abs_diff=maxabs(e_samples, nat['approx_post_samples']),
                log_ws_bitwise_equal=bool(np.array_equal(np.asarray(e_log_ws), nat['approx_post_log_ws'])),
            ),
            summary=dict(
                output_log_ws_unique=np.unique(nat['approx_post_log_ws']).tolist(), minus_log_n=float(-np.log(1000)),
                weighted_input_mean=weighted_in_mean.tolist(),
                output_mean=nat['approx_post_samples'].mean(0).tolist(),
                true_posterior_mean=np.asarray(true_m).tolist(),
                sum_sq_residual=float(np.sum(nat['residual'] ** 2)),
                output_all_finite=bool(np.all(np.isfinite(nat['approx_post_samples']))),
            ),
        )
        results['configs'][name] = cmp
        print(name, json.dumps({k: v for k, v in cmp.items() if k != 'summary'}, indent=1), flush=True)
    with open(f'{N}/data/replay_comparison.json', 'w') as fh:
        json.dump(results, fh, indent=1)


if __name__ == '__main__':
    main()
