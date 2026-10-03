"""Replay driver for the gms baselines/OT experiment (diffres @767effe).

Loads the inputs captured from the upstream scripts (data/capture_<tag>.npz), calls the SAME upstream
resampler once more in a fresh process (jitted exactly as the script does, and also eagerly), and compares
with (a) the native script outputs native_run/gms/results/*.npz and (b) the in-process capture.
The script's SWD metric is recomputed with the identical ott call. Nothing re-implements a resampler.

Usage: python replay.py
"""
import json
import os

import jax
import jax.numpy as jnp
import numpy as np

jax.config.update('jax_enable_x64', True)
from diffres import resampling as R  # noqa: E402
from ott.tools.sliced import sliced_wasserstein  # noqa: E402
from ott.geometry.costs import PNormP  # noqa: E402
from ott.geometry import pointcloud  # noqa: E402
from ott.problems.linear import linear_problem  # noqa: E402
from ott.solvers.linear import sinkhorn  # noqa: E402

NS = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(NS, 'data')

CONFIGS = {
    'baselines_multinomial': dict(fn='multinomial', kw={}, native='multinomial-0.npz'),
    'baselines_stratified': dict(fn='stratified', kw={}, native='stratified-0.npz'),
    'baselines_systematic': dict(fn='systematic', kw={}, native='systematic-0.npz'),
    'ot_eps0.3': dict(fn='ensemble_ot', kw={}, eps=0.3, native='ot-0.3-0.npz'),
}


@jax.jit
def swd(samples1, samples2, wx=None, wy=None):  # identical to the script's metric
    return sliced_wasserstein(samples1, samples2, wx, wy, cost_fn=PNormP(p=1), n_proj=1000)[0]


def maxabs(a, b):
    a, b = np.asarray(a), np.asarray(b)
    if a.shape != b.shape:
        return f'shape mismatch {a.shape} vs {b.shape}'
    return float(np.max(np.abs(a - b))) if a.size else 0.0


def same(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return bool(a.shape == b.shape and a.dtype == b.dtype and np.array_equal(a, b))


report = {'jax_version': jax.__version__, 'x64': bool(jax.config.jax_enable_x64),
          'devices': [str(d) for d in jax.devices()], 'configs': {}}
for tag, cfg in CONFIGS.items():
    cap = dict(np.load(os.path.join(D, f'capture_{tag}.npz')))
    nat = dict(np.load(os.path.join(NS, 'native_run', 'gms', 'results', cfg['native'])))
    key, log_ws, xs = jnp.asarray(cap['resampling_key']), jnp.asarray(cap['log_ws']), jnp.asarray(cap['prior_samples'])
    n = xs.shape[0]
    fn = getattr(R, cfg['fn'])
    if cfg['fn'] == 'ensemble_ot':
        eps = cfg['eps']
        call = lambda k, l, x: fn(k, l, x, eps)  # noqa: E731  (script: ensemble_ot(key_, log_ws_, prior_samples_, eps))
    else:
        call = fn
    lw_jit, x_jit = jax.jit(call)(key, log_ws, xs)
    lw_eag, x_eag = call(key, log_ws, xs)
    err_replay = swd(jnp.asarray(nat['post_samples']), x_jit)
    approx_m = jnp.einsum('n,n...->...', jnp.exp(lw_jit), x_jit)
    residual_replay = approx_m - jnp.asarray(cap['true_m'])

    r = {'upstream_call': f"diffres.resampling.{cfg['fn']}(key, log_ws, prior_samples" +
                          (f", {cfg['eps']})" if 'eps' in cfg else ')') + ' under jax.jit',
         'n': int(n), 'dx': int(xs.shape[1]),
         'native_vs_capture_bitwise': {k: same(nat[k], cap[k]) for k in nat},
         'replay_jit_vs_native': {
             'approx_post_samples_bitwise': same(x_jit, nat['approx_post_samples']),
             'approx_post_samples_maxabs': maxabs(x_jit, nat['approx_post_samples']),
             'approx_post_log_ws_bitwise': same(lw_jit, nat['approx_post_log_ws']),
             'approx_post_log_ws_maxabs': maxabs(lw_jit, nat['approx_post_log_ws']),
             'err_bitwise': same(err_replay, nat['err']),
             'err_absdiff': maxabs(err_replay, nat['err']),
             'residual_maxabs': maxabs(residual_replay, nat['residual']),
         },
         'replay_eager_vs_jit': {
             'approx_post_samples_bitwise': same(x_eag, x_jit),
             'approx_post_samples_maxabs': maxabs(x_eag, x_jit),
             'approx_post_log_ws_maxabs': maxabs(lw_eag, lw_jit),
         },
         'native_err': float(nat['err']), 'native_residual': nat['residual'].tolist(),
         'native_residual_norm': float(np.linalg.norm(nat['residual'])),
         'output_log_ws_equal_minus_log_n_atol_1e-14': bool(np.allclose(nat['approx_post_log_ws'], -np.log(n), rtol=0, atol=1e-14)),
         'weighted_input_mean_minus_true_m_norm': float(np.linalg.norm(np.exp(cap['log_ws']) @ cap['prior_samples'] - cap['true_m'])),
         'input_ess': float(1.0 / np.sum(np.exp(2 * cap['log_ws']))),
         'input_log_ws_logsumexp': float(jax.scipy.special.logsumexp(jnp.asarray(cap['log_ws']))),
         }
    save = dict(resampling_key=np.asarray(key), replay_jit_log_ws=np.asarray(lw_jit), replay_jit_samples=np.asarray(x_jit),
                replay_eager_log_ws=np.asarray(lw_eag), replay_eager_samples=np.asarray(x_eag),
                replay_err=np.asarray(err_replay), replay_residual=np.asarray(residual_replay))

    if cfg['fn'] != 'ensemble_ot':
        # Recover ancestor indices: each output row must equal exactly one input row (exact float equality).
        P = np.asarray(cap['prior_samples'])
        eq = np.all(np.asarray(nat['approx_post_samples'])[:, None, :] == P[None, :, :], axis=-1)
        nmatch = eq.sum(1)
        anc = eq.argmax(1)
        save['ancestor_indices'] = anc.astype(np.int64)
        counts = np.bincount(anc, minlength=n)
        r['ancestors'] = {
            'every_output_row_matches_exactly_one_input_row': bool(np.all(nmatch == 1)),
            'input_rows_distinct': bool(len(np.unique(P, axis=0)) == n),
            'n_unique_ancestors': int(len(np.unique(anc))),
            'indices_nondecreasing': bool(np.all(np.diff(anc) >= 0)),
            'max_offspring': int(counts.max()),
            'corr_offspring_vs_n_times_weight': float(np.corrcoef(counts, n * np.exp(cap['log_ws']))[0, 1]),
            'max_abs_offspring_minus_n_times_weight': float(np.max(np.abs(counts - n * np.exp(cap['log_ws'])))),
        }
        if cfg['fn'] == 'multinomial':
            # Contract note from the scanner: multinomial_stopped has the same forward output given the same key.
            lw_s, x_s = jax.jit(R.multinomial_stopped)(key, log_ws, xs)
            r['multinomial_stopped_forward_equals_multinomial'] = {
                'samples_bitwise': same(x_s, x_jit), 'log_ws_maxabs': maxabs(lw_s, lw_jit)}
    else:
        # Diagnostic only (not a reference value): the same Sinkhorn problem ensemble_ot builds, to report
        # convergence and marginals of the coupling that produced the output.
        eps = cfg['eps']
        geom = pointcloud.PointCloud(xs, xs, epsilon=eps)
        prob = linear_problem.LinearProblem(geom, a=jnp.full((n,), 1 / n), b=jnp.exp(log_ws))
        out = jax.jit(lambda p: sinkhorn.Sinkhorn()(p))(prob)
        Pm = np.asarray(out.matrix)
        r['sinkhorn_diagnostic'] = {
            'converged': bool(out.converged), 'n_iters': int(out.n_iters),
            'ott_default_threshold': 1e-3,
            'row_marginal_maxabs_vs_1_over_n': float(np.max(np.abs(Pm.sum(1) - 1 / n))),
            'col_marginal_maxabs_vs_weights': float(np.max(np.abs(Pm.sum(0) - np.exp(cap['log_ws'])))),
            'n_P_X_maxabs_vs_native_output': maxabs(n * Pm @ np.asarray(xs), nat['approx_post_samples']),
            'output_mean_minus_weighted_input_mean_norm': float(np.linalg.norm(
                nat['approx_post_samples'].mean(0) - np.exp(cap['log_ws']) @ cap['prior_samples'])),
        }
    np.savez(os.path.join(D, f'replay_{tag}.npz'), **save)
    report['configs'][tag] = r
    print(tag, json.dumps(r['replay_jit_vs_native']), 'native_vs_capture_all_bitwise',
          all(r['native_vs_capture_bitwise'].values()))

with open(os.path.join(D, 'replay_comparison.json'), 'w') as f:
    json.dump(report, f, indent=1)
