"""Capture driver for repo/diffres/experiments/gms/{baselines,ot}.py (diffres @767effe).

Runs the UNMODIFIED upstream script in-process with runpy (cwd = capture_run/, which holds a copy of
experiments/rnd_keys.npy and gms/results/), then saves the script's module globals after its single
Monte Carlo iteration (--id_l=0 --id_u=0): the generated GM model, the weighted prior samples that are
the resampler's input, the resampling key, the resampler outputs, and the script's metrics.
Nothing here re-implements the resampler. The key chain is re-derived with jax.random.split only to
document/verify where each key came from.

Usage: python capture.py <script_path> <tag> [script args...]
"""
import json
import os
import runpy
import sys
import time

import numpy as np

NS = os.path.dirname(os.path.abspath(__file__))
script, tag, script_args = sys.argv[1], sys.argv[2], sys.argv[3:]
os.chdir(os.path.join(NS, 'capture_run'))
sys.argv = [script] + script_args
t0 = time.time()
g = runpy.run_path(script, run_name='__main__')
elapsed = time.time() - t0

import jax  # noqa: E402  (already imported by the script; x64 already enabled by it)
import jax.numpy as jnp  # noqa: E402

assert jax.config.jax_enable_x64
args = g['args']
n = args.nsamples
key_mc = np.asarray(g['keys_mc'][0])

# Re-derive the script's key chain (same split calls, same order) to verify provenance of the captured keys.
k_ms, _ = jax.random.split(key_mc)
k_covs, _ = jax.random.split(k_ms)
k_prior, k_prior_unused = jax.random.split(k_covs)
prior_keys = jax.random.split(k_prior, n)
k_post, _ = jax.random.split(k_prior)
post_keys = jax.random.split(k_post, n)
k_resample, _ = jax.random.split(k_post)
chain_ok = {
    'resampling_key_equals_script_global_key': bool(np.array_equal(np.asarray(k_resample), np.asarray(g['key']))),
    'post_keys_equal_script_global_keys': bool(np.array_equal(np.asarray(post_keys), np.asarray(g['keys']))),
}
# The script passes `_` (a key) as the ignored eigvals/eigvecs arguments of sampling_gm; with covs given they are unused.
prior_regen = g['sampler_gm'](prior_keys, g['vs'], g['ms'], k_prior_unused, k_prior_unused, g['covs'])
chain_ok['prior_samples_regenerated_bitwise'] = bool(np.array_equal(np.asarray(prior_regen), np.asarray(g['prior_samples'])))

out = dict(
    key_mc=key_mc,
    key_ms=np.asarray(k_ms), key_covs=np.asarray(k_covs), key_prior=np.asarray(k_prior),
    prior_keys=np.asarray(prior_keys), key_post=np.asarray(k_post), post_keys=np.asarray(post_keys),
    resampling_key=np.asarray(g['key']),
    vs=np.asarray(g['vs']), ms=np.asarray(g['ms']), covs=np.asarray(g['covs']),
    obs_op=np.asarray(g['obs_op']), obs_cov=np.asarray(g['obs_cov']), y=np.asarray(g['y']),
    post_vs=np.asarray(g['post_vs']), post_ms=np.asarray(g['post_ms']), post_covs=np.asarray(g['post_covs']),
    prior_samples=np.asarray(g['prior_samples']), log_ws=np.asarray(g['log_ws']), ws=np.asarray(g['ws']),
    post_samples=np.asarray(g['post_samples']),
    approx_post_log_ws=np.asarray(g['approx_post_log_ws']),
    approx_post_samples=np.asarray(g['approx_post_samples']),
    err=np.asarray(g['err']), residual=np.asarray(g['residual']),
    approx_m=np.asarray(g['approx_m']), true_m=np.asarray(g['true_m']),
)
np.savez(os.path.join(NS, 'data', f'capture_{tag}.npz'), **out)
meta = dict(tag=tag, script=script, argv=script_args, parsed_args=vars(args),
            runtime_seconds_including_jit=elapsed, jax_version=jax.__version__,
            jax_enable_x64=bool(jax.config.jax_enable_x64), devices=[str(d) for d in jax.devices()],
            dtypes={k: str(v.dtype) for k, v in out.items()}, shapes={k: list(v.shape) for k, v in out.items()},
            key_chain_checks=chain_ok, err=float(out['err']), residual=out['residual'].tolist(),
            eff_sample_size=float(1.0 / np.sum(out['ws'] ** 2)))
with open(os.path.join(NS, 'data', f'capture_{tag}.json'), 'w') as f:
    json.dump(meta, f, indent=1)
print(json.dumps(meta['key_chain_checks']), 'err', repr(meta['err']), 'ESS', meta['eff_sample_size'])
