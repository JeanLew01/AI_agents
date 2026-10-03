"""Capture driver for repo/diffres/experiments/gms/soft.py (execution_id gms_soft_experiment).

Runs the UNMODIFIED upstream script in-process with runpy (same argv as the direct run) from a scratch working
directory that contains a copy of experiments/rnd_keys.npy and an empty ./gms/results/. After the script finishes,
its module-level variables (the script has no functions/return values; everything lives at module scope inside its
single-iteration MC loop) are read back and saved at full precision. No algorithm is re-implemented here.

Usage (from notebooks/gms_soft_experiment/run_capture):
    python ../capture_soft_gms.py <out_dir>
"""
import json
import runpy
import sys

import numpy as np

SCRIPT = '/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/repo/diffres/experiments/gms/soft.py'
ARGV = [SCRIPT, '--id_l=0', '--id_u=0', '--nsamples=1000', '--alpha=0.9']
out_dir = sys.argv[1]

sys.argv = list(ARGV)
g = runpy.run_path(SCRIPT, run_name='__main__')

import jax  # already imported (and x64 enabled) by the script

args = g['args']
key = g['key']  # key passed to resampling(key, log_ws, prior_samples) == soft_resampling(key, ..., alpha)
key_mc = g['key_mc']
inputs = dict(
    key_mc=np.asarray(key_mc),
    key_resampling=np.asarray(jax.random.key_data(key) if jax.dtypes.issubdtype(key.dtype, jax.dtypes.prng_key)
                              else key),
    log_ws=np.asarray(g['log_ws']),           # normalised log importance weights (n,)
    ws=np.asarray(g['ws']),
    prior_samples=np.asarray(g['prior_samples']),  # (n, d) weighted samples fed to the resampler
    alpha=np.float64(g['alpha']),
    y=np.asarray(g['y']),
    obs_op=np.asarray(g['obs_op']),
    obs_cov=np.asarray(g['obs_cov']),
    vs=np.asarray(g['vs']), ms=np.asarray(g['ms']), covs=np.asarray(g['covs']),
    post_vs=np.asarray(g['post_vs']), post_ms=np.asarray(g['post_ms']), post_covs=np.asarray(g['post_covs']),
    post_samples=np.asarray(g['post_samples']),
)
outputs = dict(
    approx_post_log_ws=np.asarray(g['approx_post_log_ws']),
    approx_post_weights=np.exp(np.asarray(g['approx_post_log_ws'])),
    approx_post_samples=np.asarray(g['approx_post_samples']),
    err=np.asarray(g['err']),
    residual=np.asarray(g['residual']),
    approx_m=np.asarray(g['approx_m']),
    true_m=np.asarray(g['true_m']),
)
np.savez(f'{out_dir}/soft_gms_inputs.npz', **inputs)
np.savez(f'{out_dir}/soft_gms_outputs.npz', **outputs)
meta = dict(
    script=SCRIPT, argv=ARGV[1:], parsed_args=vars(args), mc_id=int(g['mc_id']),
    x64=bool(jax.config.jax_enable_x64), jax_version=jax.__version__, backend=jax.default_backend(),
    key_mc_dtype=str(np.asarray(key_mc).dtype), key_resampling_dtype=str(key.dtype),
    dtypes={k: str(v.dtype) for k, v in {**inputs, **outputs}.items()},
    shapes={k: list(v.shape) for k, v in {**inputs, **outputs}.items()},
    err=float(g['err']), residual=np.asarray(g['residual']).tolist(),
    residual_sq_sum=float(np.sum(np.asarray(g['residual']) ** 2)),
)
with open(f'{out_dir}/soft_gms_capture_meta.json', 'w') as f:
    json.dump(meta, f, indent=1)
print(json.dumps(meta, indent=1))
