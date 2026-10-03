"""Replay driver for gms_gumbel_experiment.

Loads the inputs captured from the upstream script (data/gumbel_inputs_outputs.npz) and calls the upstream resampler
diffres.resampling.gumbel_softmax(key, log_ws, samples, tau) once more in a fresh process, (a) jitted exactly as the
script does (tau closed over as a Python float) and (b) eagerly. It then recomputes the script's two metrics with the
script's own metric code (ott sliced_wasserstein, p=1, n_proj=1000; weighted mean residual) and compares everything
with the captured outputs and with the native run's saved file run_native/gms/results/gumbel-0.1-0.npz.
"""
import json
import sys

import jax
import jax.numpy as jnp
import numpy as np
from diffres.resampling import gumbel_softmax
from ott.geometry.costs import PNormP
from ott.tools.sliced import sliced_wasserstein

jax.config.update('jax_enable_x64', True)

cap_path, native_path, out_npz, out_json = sys.argv[1:5]
cap = np.load(cap_path)
nat = np.load(native_path)

key = jnp.asarray(cap['resampling_key'])
log_ws = jnp.asarray(cap['log_ws'])
samples = jnp.asarray(cap['prior_samples'])
tau = float(cap['tau'])


@jax.jit
def resampling(key_, log_ws_, prior_samples_):  # same wrapper as the script
    return gumbel_softmax(key_, log_ws_, prior_samples_, tau)


@jax.jit
def swd(samples1, samples2, wx=None, wy=None):  # same metric as the script
    return sliced_wasserstein(samples1, samples2, wx, wy, cost_fn=PNormP(p=1), n_proj=1000)[0]


lw_jit, xs_jit = resampling(key, log_ws, samples)
lw_eager, xs_eager = gumbel_softmax(key, log_ws, samples, tau)
err_replay = swd(jnp.asarray(cap['post_samples']), xs_jit)
approx_m = jnp.einsum('n,n...->...', jnp.exp(lw_jit), xs_jit)
true_m = jnp.einsum('c,c...->...', jnp.asarray(cap['post_vs']), jnp.asarray(cap['post_ms']))
residual_replay = approx_m - true_m

np.savez(out_npz, approx_post_log_ws_jit=np.asarray(lw_jit), approx_post_samples_jit=np.asarray(xs_jit),
         approx_post_log_ws_eager=np.asarray(lw_eager), approx_post_samples_eager=np.asarray(xs_eager),
         err=np.asarray(err_replay), residual=np.asarray(residual_replay))


def cmp(a, b):
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    d = np.abs(a - b)
    return {'shape_a': list(a.shape), 'shape_b': list(b.shape), 'bitwise_equal': bool(np.array_equal(a, b)),
            'max_abs_diff': float(d.max()) if d.size else 0.0,
            'max_rel_diff': float((d / np.maximum(np.abs(b), 1e-300)).max()) if d.size else 0.0}


res = {
    'jax_version': jax.__version__, 'backend': jax.default_backend(), 'x64': bool(jax.config.jax_enable_x64),
    'tau': tau, 'n': int(log_ws.shape[0]),
    'native_vs_capture': {k: cmp(nat[k], cap[k]) for k in
                          ['post_samples', 'approx_post_log_ws', 'approx_post_samples', 'err', 'residual']},
    'replay_jit_vs_capture': {
        'approx_post_log_ws': cmp(lw_jit, cap['approx_post_log_ws']),
        'approx_post_samples': cmp(xs_jit, cap['approx_post_samples']),
        'err': cmp(err_replay, cap['err']),
        'residual': cmp(residual_replay, cap['residual']),
    },
    'replay_eager_vs_capture': {
        'approx_post_log_ws': cmp(lw_eager, cap['approx_post_log_ws']),
        'approx_post_samples': cmp(xs_eager, cap['approx_post_samples']),
    },
    'replay_jit_vs_native': {
        'approx_post_samples': cmp(xs_jit, nat['approx_post_samples']),
        'err': cmp(err_replay, nat['err']),
    },
    'err_capture': float(cap['err']), 'err_native': float(nat['err']), 'err_replay': float(err_replay),
    'residual_sq_sum_native': float(np.sum(nat['residual'] ** 2)),
    'output_log_ws_uniform': bool(np.allclose(np.asarray(lw_jit), -np.log(log_ws.shape[0]), rtol=0, atol=0)),
    'output_finite': bool(np.isfinite(np.asarray(xs_jit)).all()),
}
with open(out_json, 'w') as f:
    json.dump(res, f, indent=1)
print(json.dumps(res, indent=1))
