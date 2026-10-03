"""Evidence driver for execution_id=filters_tests (Paper2MCP, diffres @ 767effe).

Source: repo/diffres/tests/test_filters.py (unchanged). This driver does NOT re-implement any algorithm.

Modes
-----
capture : import the upstream test module from its path (its module-level code builds key, ys, the OU-LGSSM matrices,
          GP-regression reference and runs kf + rts exactly as the test does), save the inputs (.npz, float64),
          then call the same upstream functions as the tests (kf, rts, smc_feynman_kac with every resampler used in
          the tests, with the tests' arguments) and save the native outputs at full precision.
replay  : in a fresh process, WITHOUT importing the test module, load the saved inputs, rebuild the bootstrap
          model callables (verbatim copies of test_filters.py lines 59-73, parameterised by the loaded arrays) and
          call the same upstream functions again; save the outputs.
compare : compare capture vs replay outputs and evaluate the tests' own assertions on the captured outputs.

Run every mode through heavy.sh (CPU-only JAX):
  heavy.sh --limit-mb 1200 -- diffres-env/bin/python notebooks/filters_tests/filters_tests_driver.py capture
"""
import sys
import json
import time
import hashlib
import importlib.util
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[2]
NS = PROJECT_ROOT / 'notebooks' / 'filters_tests'
TEST_PATH = PROJECT_ROOT / 'repo' / 'diffres' / 'tests' / 'test_filters.py'
INPUTS = NS / 'data' / 'filters_tests_inputs.npz'
OUT = {'capture': NS / 'outputs' / 'capture_outputs.npz', 'replay': NS / 'outputs' / 'replay_outputs.npz'}

# Resampler configurations exactly as in test_filters.py (name -> (upstream function name, kwargs, test rtol))
DIFF_TS = dict(start=0., stop=2., num=8)  # jnp.linspace(0., 2., 8) in test_diffres
CONFIGS = {
    'multinomial': ('multinomial', {}, 6e-2),
    'multinomial_stopped': ('multinomial_stopped', {}, 6e-2),
    'stratified': ('stratified', {}, 6e-2),
    'systematic': ('systematic', {}, 6e-2),
    'diffusion_euler': ('diffusion_resampling', dict(a=-0.5, ts=DIFF_TS, integrator='euler', ode=False), 5e-2),
    'diffusion_lord_and_rougemont': ('diffusion_resampling',
                                     dict(a=-0.5, ts=DIFF_TS, integrator='lord_and_rougemont', ode=False), 5e-2),
    'diffusion_jentzen_and_kloeden': ('diffusion_resampling',
                                      dict(a=-0.5, ts=DIFF_TS, integrator='jentzen_and_kloeden', ode=False), 5e-2),
    'diffusion_tweedie': ('diffusion_resampling', dict(a=-0.5, ts=DIFF_TS, integrator='tweedie', ode=False), 5e-2),
    'ensemble_ot_eps0.1': ('ensemble_ot', dict(eps=0.1), 7e-2),
}


def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def make_resampler(name):
    import jax.numpy as jnp
    import diffres.resampling as R
    fname, kw, _ = CONFIGS[name]
    fn = getattr(R, fname)
    if fname == 'diffusion_resampling':
        ts = jnp.linspace(kw['ts']['start'], kw['ts']['stop'], kw['ts']['num'])

        def r(key_, log_ws, samples):  # as in test_diffres
            return fn(key_, log_ws, samples, kw['a'], ts, integrator=kw['integrator'], ode=kw['ode'])
        return r
    if fname == 'ensemble_ot':
        def r(key_, log_ws, samples):  # as in test_ensemble_ot
            return fn(key_, log_ws, samples, eps=kw['eps'])
        return r
    return fn  # passed directly, as in test_smc


def run_upstream(key, m0_sampler, log_g0, m_log_g, ys, nparticles, nsteps, kf_args, semigroup):
    """Call the upstream functions exactly as test_filters.py does; return dict of numpy float64 outputs."""
    import jax
    from diffres.feynman_kac import smc_feynman_kac
    from diffres.gaussian_filters import kf, rts
    out, timing = {}, {}
    mfs, vfs, nll, mps, vps = kf(*kf_args)
    mss, vss = rts(mfs, vfs, mps, vps, semigroup)
    for k, v in dict(mfs=mfs, vfs=vfs, nll=nll, mps=mps, vps=vps, mss=mss, vss=vss).items():
        out[f'kf/{k}'] = np.asarray(v)
    for name in CONFIGS:
        t0 = time.time()
        samples, log_ws, nll_pf, ess = smc_feynman_kac(key, m0_sampler, log_g0, m_log_g, ys, nparticles, nsteps,
                                                       resampling=make_resampler(name), resampling_threshold=1.,
                                                       return_path=True)
        nll_pf = jax.block_until_ready(nll_pf)
        timing[name] = time.time() - t0
        out[f'pf/{name}/nll'] = np.asarray(nll_pf)
        out[f'pf/{name}/samples'] = np.asarray(samples)
        out[f'pf/{name}/log_ws'] = np.asarray(log_ws)
        out[f'pf/{name}/ess'] = np.asarray(ess)
        print(f'{name}: nll_pf={float(nll_pf)!r} ({timing[name]:.2f}s)', flush=True)
    return out, timing


def capture():
    spec = importlib.util.spec_from_file_location('upstream_test_filters', TEST_PATH)
    tm = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(tm)  # runs the test's module-level code (x64 on, key, ys, GP ref, kf, rts)
    import jax
    assert jax.config.jax_enable_x64
    inputs = dict(
        key=np.asarray(tm.key),  # legacy raw uint32 PRNGKey(666)
        ys=np.asarray(tm.ys), ts=np.asarray(tm.ts),
        m0=np.asarray(tm.m0), v0=np.asarray(tm.v0), semigroup=np.asarray(tm.semigroup),
        trans_cov=np.asarray(tm.trans_cov), obs_op=np.asarray(tm.obs_op), obs_cov=np.asarray(tm.obs_cov),
        xi=np.float64(tm.xi), ell=np.float64(tm.ell), sigma=np.float64(tm.sigma), T=np.float64(tm.T),
        dt=np.float64(tm.dt), nparticles=np.int64(tm.nparticles), nsteps=np.int64(tm.nsteps),
        dx=np.int64(tm.dx), dy=np.int64(tm.dy),
        gp_mean=np.asarray(tm.gp_mean), gp_var=np.asarray(np.diag(tm.gp_cov)), gp_nll=np.asarray(tm.gp_nll),
        # test-module KF/RTS results computed at import (the values test_kf asserts on)
        testmod_kf_nll=np.asarray(tm.nll), testmod_mss=np.asarray(tm.mss), testmod_vss=np.asarray(tm.vss),
    )
    for k, v in inputs.items():
        if np.asarray(v).dtype.kind == 'f':
            assert np.asarray(v).dtype == np.float64, k
    np.savez(INPUTS, **inputs)
    out, timing = run_upstream(tm.key, tm.m0_sampler, tm.log_g0, tm.m_log_g, tm.ys, tm.nparticles, tm.nsteps,
                               (tm.ys, tm.m0, tm.v0, tm.semigroup, tm.trans_cov, tm.obs_op, tm.obs_cov),
                               tm.semigroup)
    np.savez_compressed(OUT['capture'], **out)
    (NS / 'outputs' / 'capture_timing.json').write_text(json.dumps(timing, indent=1))


def replay():
    import jax
    jax.config.update('jax_enable_x64', True)
    import jax.numpy as jnp
    d = np.load(INPUTS)
    key = jnp.asarray(d['key'], dtype=jnp.uint32)
    ys, m0, v0 = jnp.asarray(d['ys']), jnp.asarray(d['m0']), jnp.asarray(d['v0'])
    semigroup, trans_cov = jnp.asarray(d['semigroup']), jnp.asarray(d['trans_cov'])
    obs_op, obs_cov = jnp.asarray(d['obs_op']), jnp.asarray(d['obs_cov'])
    xi, nparticles, nsteps, dx = float(d['xi']), int(d['nparticles']), int(d['nsteps']), int(d['dx'])

    # --- verbatim copy of test_filters.py lines 59-73 (bootstrap model), bound to the loaded arrays ---
    def m0_sampler(key_, _):
        rnds = jax.random.normal(key_, shape=(nparticles, dx))
        return m0 + rnds @ jnp.linalg.cholesky(v0).T

    def log_g0(samples, y0):
        return jnp.sum(jax.scipy.stats.norm.logpdf(y0, samples @ obs_op.T, xi ** 0.5), axis=-1)

    def m_log_g(key_, samples, pytree):
        y = pytree
        rnds = jax.random.normal(key_, shape=(nparticles, dx))
        prop_samples = samples @ semigroup.T + rnds @ (trans_cov ** 0.5).T
        log_potentials = jnp.sum(jax.scipy.stats.norm.logpdf(y, prop_samples @ obs_op.T, xi ** 0.5), axis=-1)
        return log_potentials, prop_samples
    # ---------------------------------------------------------------------------------------------------

    out, timing = run_upstream(key, m0_sampler, log_g0, m_log_g, ys, nparticles, nsteps,
                               (ys, m0, v0, semigroup, trans_cov, obs_op, obs_cov), semigroup)
    np.savez_compressed(OUT['replay'], **out)
    (NS / 'outputs' / 'replay_timing.json').write_text(json.dumps(timing, indent=1))


def compare():
    d = np.load(INPUTS)
    c, r = np.load(OUT['capture']), np.load(OUT['replay'])
    assert sorted(c.files) == sorted(r.files)
    res = {'replay_vs_capture': {}, 'test_assertions_on_capture': {}, 'reference_numbers': {}}
    for k in sorted(c.files):
        a, b = c[k], r[k]
        diff = float(np.max(np.abs(a - b))) if a.size else 0.0
        res['replay_vs_capture'][k] = dict(shape=list(a.shape), dtype=str(a.dtype), bitwise_equal=bool(np.array_equal(a, b)),
                                           max_abs_diff=diff, allclose_1e12=bool(np.allclose(a, b, rtol=1e-12, atol=1e-12)))
    kf_nll = float(c['kf/nll'])
    # test_kf assertions (npt.assert_allclose default rtol=1e-7)
    for name, (a, b) in dict(mss_vs_gp_mean=(c['kf/mss'][:, 0], d['gp_mean']),
                             vss_vs_gp_var=(c['kf/vss'][:, 0, 0], d['gp_var']),
                             nll_vs_gp_nll=(c['kf/nll'], d['gp_nll'])).items():
        rel = float(np.max(np.abs(a - b) / np.abs(b)))
        res['test_assertions_on_capture'][f'test_kf/{name}'] = dict(max_rel_err=rel, rtol=1e-7, passed=rel <= 1e-7)
    res['test_assertions_on_capture']['kf_nll_equals_test_module_nll'] = bool(np.array_equal(c['kf/nll'], d['testmod_kf_nll']))
    for name, (_, _, rtol) in CONFIGS.items():
        nll_pf = float(c[f'pf/{name}/nll'])
        rel = abs(nll_pf - kf_nll) / abs(kf_nll)
        res['test_assertions_on_capture'][f'pf/{name}'] = dict(nll_pf=nll_pf, kf_nll=kf_nll, rel_err=rel, rtol=rtol,
                                                               passed=rel <= rtol)
    res['reference_numbers'] = dict(kf_nll=kf_nll, gp_nll=float(d['gp_nll']),
                                    pf_nll={n: float(c[f'pf/{n}/nll']) for n in CONFIGS},
                                    pf_final_ess={n: float(c[f'pf/{n}/ess'][-1]) for n in CONFIGS})
    res['all_bitwise_equal'] = all(v['bitwise_equal'] for v in res['replay_vs_capture'].values())
    res['all_test_assertions_pass'] = all(v['passed'] if isinstance(v, dict) else v
                                          for v in res['test_assertions_on_capture'].values())
    res['hashes'] = {str(p.relative_to(PROJECT_ROOT)): sha256(p) for p in [INPUTS, OUT['capture'], OUT['replay'], TEST_PATH]}
    (NS / 'outputs' / 'comparison.json').write_text(json.dumps(res, indent=1))
    print(json.dumps({k: res[k] for k in ['reference_numbers', 'all_bitwise_equal', 'all_test_assertions_pass']}, indent=1))


if __name__ == '__main__':
    {'capture': capture, 'replay': replay, 'compare': compare}[sys.argv[1]]()
