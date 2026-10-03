"""Replay driver for gms_soft_experiment.

Loads the inputs captured from repo/diffres/experiments/gms/soft.py (data/soft_gms_inputs.npz) in a fresh process,
calls the upstream resampler diffres.resampling.soft_resampling once more exactly as the script does
(jax.jit wrapper with alpha closed over, x64 enabled, CPU), and recomputes the script's metric with the same upstream
ott call (sliced_wasserstein, PNormP(p=1), n_proj=1000). Also calls soft_resampling without jit. Compares with
(a) the capture-run outputs and (b) the native result file written by the direct, unmodified script run.
Particle indices are recovered post hoc by exact row matching of the resampled particles against the input
particles (identification only, not a re-implementation).

Usage: python replay_soft_gms.py <namespace_dir>
"""
import json
import sys

import jax
import jax.numpy as jnp
import numpy as np

jax.config.update("jax_enable_x64", True)
from diffres.resampling import soft_resampling  # noqa: E402
from ott.tools.sliced import sliced_wasserstein  # noqa: E402
from ott.geometry.costs import PNormP  # noqa: E402

ns = sys.argv[1]
inp = np.load(f'{ns}/data/soft_gms_inputs.npz')
cap = np.load(f'{ns}/data/soft_gms_outputs.npz')
direct = np.load(f'{ns}/run_direct/gms/results/soft-0.9-0.npz')
capture_native = np.load(f'{ns}/run_capture/gms/results/soft-0.9-0.npz')

key = jnp.asarray(inp['key_resampling'])
log_ws = jnp.asarray(inp['log_ws'])
prior_samples = jnp.asarray(inp['prior_samples'])
alpha = float(inp['alpha'])
assert key.dtype == jnp.uint32 and log_ws.dtype == jnp.float64 and prior_samples.dtype == jnp.float64


@jax.jit
def resampling(key_, log_ws_, prior_samples_):  # same wrapper as the script
    return soft_resampling(key_, log_ws_, prior_samples_, alpha)


@jax.jit
def swd(samples1, samples2, wx=None, wy=None):  # same metric call as the script
    return sliced_wasserstein(samples1, samples2, wx, wy, cost_fn=PNormP(p=1), n_proj=1000)[0]


lw_jit, xs_jit = resampling(key, log_ws, prior_samples)
lw_nojit, xs_nojit = soft_resampling(key, log_ws, prior_samples, alpha)
post_samples = jnp.asarray(inp['post_samples'])
err_replay = swd(post_samples, xs_jit, wy=jnp.exp(lw_jit))
approx_m = jnp.einsum('n,n...->...', jnp.exp(lw_jit), xs_jit)
true_m = jnp.einsum('c,c...->...', jnp.asarray(inp['post_vs']), jnp.asarray(inp['post_ms']))
residual_replay = approx_m - true_m

lw_jit, xs_jit, lw_nojit, xs_nojit = map(np.asarray, (lw_jit, xs_jit, lw_nojit, xs_nojit))
err_replay, residual_replay = np.asarray(err_replay), np.asarray(residual_replay)


def cmp(a, b):
    a, b = np.asarray(a), np.asarray(b)
    d = float(np.max(np.abs(a - b))) if a.size else 0.0
    return dict(shape_equal=a.shape == b.shape, bitwise_equal=bool(np.array_equal(a, b)), max_abs_diff=d)


def row_indices(x, pool):
    """Exact row matching of resampled particles to input particles (identification, not resampling)."""
    lut = {r.tobytes(): i for i, r in enumerate(pool)}
    return np.array([lut.get(r.tobytes(), -1) for r in x])


pool = np.asarray(inp['prior_samples'])
assert len({r.tobytes() for r in pool}) == pool.shape[0], 'input particles not unique'
inds_replay = row_indices(xs_jit, pool)
inds_direct = row_indices(direct['approx_post_samples'], pool)
assert (inds_replay >= 0).all() and (inds_direct >= 0).all()
np.savez(f'{ns}/data/soft_gms_replay_outputs.npz', approx_post_log_ws=lw_jit, approx_post_samples=xs_jit,
         approx_post_log_ws_nojit=lw_nojit, approx_post_samples_nojit=xs_nojit, err=err_replay,
         residual=residual_replay, resample_indices=inds_replay)
np.save(f'{ns}/data/soft_gms_resample_indices.npy', inds_direct)

w = np.exp(lw_jit)
res = dict(
    replay_jit_vs_capture=dict(log_ws=cmp(lw_jit, cap['approx_post_log_ws']),
                               samples=cmp(xs_jit, cap['approx_post_samples']),
                               err=cmp(err_replay, cap['err']), residual=cmp(residual_replay, cap['residual'])),
    replay_jit_vs_direct_native=dict(log_ws=cmp(lw_jit, direct['approx_post_log_ws']),
                                     samples=cmp(xs_jit, direct['approx_post_samples']),
                                     err=cmp(err_replay, direct['err']),
                                     residual=cmp(residual_replay, direct['residual'])),
    replay_nojit_vs_jit=dict(log_ws=cmp(lw_nojit, lw_jit), samples=cmp(xs_nojit, xs_jit)),
    capture_native_vs_direct_native={k: cmp(capture_native[k], direct[k]) for k in direct.files},
    capture_inputs_vs_direct_native=dict(post_samples=cmp(inp['post_samples'], direct['post_samples'])),
    indices=dict(replay_equals_direct=bool(np.array_equal(inds_replay, inds_direct)),
                 n_unique=int(np.unique(inds_direct).size), min=int(inds_direct.min()), max=int(inds_direct.max())),
    summary=dict(err_direct=float(direct['err']), err_replay=float(err_replay),
                 residual_sq_sum_direct=float(np.sum(direct['residual'] ** 2)),
                 out_weight_sum=float(w.sum()), out_ess=float(1. / np.sum(w ** 2)),
                 out_weight_min=float(w.min()), out_weight_max=float(w.max()),
                 in_ess=float(1. / np.sum(np.asarray(inp['ws']) ** 2)), alpha=alpha,
                 jax_version=jax.__version__, backend=jax.default_backend(), x64=bool(jax.config.jax_enable_x64)),
)
with open(f'{ns}/data/soft_gms_replay_comparison.json', 'w') as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
