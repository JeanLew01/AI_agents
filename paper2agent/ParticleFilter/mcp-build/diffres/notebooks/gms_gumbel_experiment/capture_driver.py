"""Capture driver for repo/diffres/experiments/gms/gumbel.py (execution_id gms_gumbel_experiment).

Runs the UNMODIFIED upstream script in-process via runpy.run_path (same argv as the native run, cwd = run_capture/),
then saves the module globals left after its single MC iteration: the generated GM problem, the weighted prior
samples / log weights, the exact PRNG keys, the resampler arguments and outputs, and the script's metrics.
No algorithm is re-implemented here; the script itself computes everything.

Usage (cwd must contain rnd_keys.npy and gms/results/):
    python capture_driver.py <out_npz> <out_json> --id_l=0 --id_u=0 --nsamples=1000 --tau=0.1
"""
import json
import runpy
import sys

import numpy as np

SCRIPT = ('/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/repo/diffres/'
          'experiments/gms/gumbel.py')

out_npz, out_json = sys.argv[1], sys.argv[2]
script_args = sys.argv[3:]
sys.argv = [SCRIPT] + script_args
g = runpy.run_path(SCRIPT, run_name='__main__')

import jax  # noqa: E402  (already imported and configured by the script)

assert jax.config.jax_enable_x64, 'script should have enabled x64'
assert len(g['keys_mc']) == 1, 'capture driver expects a single MC id'

names = ['key_mc', 'key', 'vs', 'ms', 'covs', 'obs_op', 'obs_cov', 'y', 'post_vs', 'post_ms', 'post_covs',
         'prior_samples', 'post_samples', 'log_ws', 'ws', 'approx_post_log_ws', 'approx_post_samples', 'err',
         'residual', 'approx_m', 'true_m']
arrays = {}
for nm in names:
    arrays[nm] = np.asarray(g[nm])
# Rename for clarity: 'key' after the last split is the key passed to gumbel_softmax.
arrays['resampling_key'] = arrays.pop('key')
arrays['tau'] = np.asarray(g['tau'], dtype=np.float64)
arrays['mc_id'] = np.asarray(g['mc_id'])
np.savez(out_npz, **arrays)

meta = {
    'script': SCRIPT,
    'argv': script_args,
    'parsed_args': vars(g['args']),
    'jax_version': jax.__version__,
    'jax_enable_x64': bool(jax.config.jax_enable_x64),
    'backend': jax.default_backend(),
    'devices': [str(d) for d in jax.devices()],
    'arrays': {k: {'dtype': str(v.dtype), 'shape': list(v.shape)} for k, v in arrays.items()},
    'err': float(arrays['err']),
    'residual': arrays['residual'].tolist(),
    'residual_sq_sum': float(np.sum(arrays['residual'] ** 2)),
    'resampling_key': arrays['resampling_key'].tolist(),
    'key_mc': arrays['key_mc'].tolist(),
}
with open(out_json, 'w') as f:
    json.dump(meta, f, indent=1)
print('captured', out_npz, 'err', repr(meta['err']), 'residual_sq_sum', repr(meta['residual_sq_sum']))
