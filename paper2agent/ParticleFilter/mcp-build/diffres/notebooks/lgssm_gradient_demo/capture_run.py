"""Capture driver for repo/diffres/demos/gradient_variance2.py (execution_id lgssm_gradient_demo).

Executes the UNMODIFIED upstream script with runpy.run_path (same argv as a native run) and captures its
module globals at full precision (the script itself only prints with numpy's default 8-digit precision and
saves nothing). After the script finishes, it calls the upstream functions the script already bound
(kf_ = diffres.gaussian_filters.kf, diffres.gaussian_filters.rts, diffres.tools.simulate_lgssm) once more to
record the full Kalman/RTS outputs that the script computes internally but discards, plus the gradient of the
KF nll w.r.t. the full matrices F and H (the form the MCP tool will expose). No algorithm is re-implemented.

Usage: python capture_run.py --nsteps 16 --nparticles 8 --out data/reference_nsteps16_np8.npz
"""
import argparse
import hashlib
import json
import runpy
import sys
import time

import numpy as np

SCRIPT = '/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/repo/diffres/demos/gradient_variance2.py'

ap = argparse.ArgumentParser()
ap.add_argument('--nsteps', type=int, required=True)
ap.add_argument('--nparticles', type=int, required=True)
ap.add_argument('--out', required=True)
ap.add_argument('--summary', required=True)
cli = ap.parse_args()

np.set_printoptions(precision=17, threshold=10, linewidth=150)

sys.argv = [SCRIPT, '--nsteps', str(cli.nsteps), '--nparticles', str(cli.nparticles)]
t0 = time.time()
g = runpy.run_path(SCRIPT, run_name='__main__')
t_script = time.time() - t0

import jax  # noqa: E402  (already imported and configured with x64 by the script)
import jax.numpy as jnp  # noqa: E402
from diffres.gaussian_filters import kf as kf_up, rts as rts_up  # noqa: E402
from diffres.tools import simulate_lgssm as sim_up  # noqa: E402

assert jax.config.jax_enable_x64, 'script should have enabled x64'
assert g['kf_'] is kf_up and g['simulate_lgssm'] is sim_up

ys, xs, params = g['ys'], g['xs'], g['params']
m0, v0 = g['m0'], g['v0']
semigroup, trans_cov, obs_op, obs_cov = g['semigroup'], g['trans_cov'], g['obs_op'], g['obs_cov']
dx, dy = g['dx'], g['dy']

# Full KF + RTS outputs at the demo's evaluation point theta = params (F = theta0 * I, H = theta1 * ones)
F_theta = params[0] * jnp.eye(dx)
H_theta = params[1] * jnp.ones((dy, dx))
mfs_t, vfs_t, nll_t, mps_t, vps_t = kf_up(ys, m0, v0, F_theta, trans_cov, H_theta, obs_cov)
mss_t, vss_t = rts_up(mfs_t, vfs_t, mps_t, vps_t, F_theta)

# Full KF + RTS outputs at the data-generating parameters
mfs_0, vfs_0, nll_0, mps_0, vps_0 = kf_up(ys, m0, v0, semigroup, trans_cov, obs_op, obs_cov)
mss_0, vss_0 = rts_up(mfs_0, vfs_0, mps_0, vps_0, semigroup)


# Gradient of the KF nll w.r.t. full matrices F and H at the evaluation point (tool form)
def nll_FH(F, H):
    return kf_up(ys, m0, v0, F, trans_cov, H, obs_cov)[2]


nll_FH_val, (dF, dH) = jax.value_and_grad(nll_FH, argnums=(0, 1))(F_theta, H_theta)

out = dict(
    script_sha256=hashlib.sha256(open(SCRIPT, 'rb').read()).hexdigest(),
    nsteps=g['nsteps'], nparticles=g['nparticles'], dx=dx, dy=dy,
    p1=g['p1'], p2=g['p2'], sig=g['sig'], xi=g['xi'], v0_scalar=g['v0_'],
    a=g['a'], T=g['T'], dsteps=g['dsteps'], ts=np.asarray(g['ts']), integrator=g['integrator'], ode=g['ode'],
    jitter=1e-5, nmcs=g['nmcs'],
    key=np.asarray(g['key']), key_simulation=np.asarray(g['key_simulation']), keys=np.asarray(g['keys']),
    semigroup=np.asarray(semigroup), trans_cov=np.asarray(trans_cov), obs_op=np.asarray(obs_op),
    obs_cov=np.asarray(obs_cov), m0=np.asarray(m0), v0=np.asarray(v0),
    xs=np.asarray(xs), ys=np.asarray(ys), params=np.asarray(params),
    loss_true=np.asarray(g['loss_true']), grad_true=np.asarray(g['grad_true']),
    losses_dp=g['losses_dp'], grads_dp=g['grads_dp'], losses_rein=g['losses_rein'], grads_rein=g['grads_rein'],
    kf_theta_mfs=np.asarray(mfs_t), kf_theta_vfs=np.asarray(vfs_t), kf_theta_nll=np.asarray(nll_t),
    kf_theta_mps=np.asarray(mps_t), kf_theta_vps=np.asarray(vps_t),
    rts_theta_mss=np.asarray(mss_t), rts_theta_vss=np.asarray(vss_t),
    kf_true_mfs=np.asarray(mfs_0), kf_true_vfs=np.asarray(vfs_0), kf_true_nll=np.asarray(nll_0),
    kf_true_mps=np.asarray(mps_0), kf_true_vps=np.asarray(vps_0),
    rts_true_mss=np.asarray(mss_0), rts_true_vss=np.asarray(vss_0),
    kf_theta_nll_via_FH=np.asarray(nll_FH_val), kf_theta_dF=np.asarray(dF), kf_theta_dH=np.asarray(dH),
)
np.savez(cli.out, **out)

summary = dict(
    script_runtime_s=t_script,
    nsteps=int(g['nsteps']), nparticles=int(g['nparticles']), nmcs=int(g['nmcs']),
    dtypes=dict(ys=str(np.asarray(ys).dtype), grads_dp=str(g['grads_dp'].dtype), keys=str(np.asarray(g['keys']).dtype)),
    key=np.asarray(g['key']).tolist(), key_simulation=np.asarray(g['key_simulation']).tolist(),
    keys_first3=np.asarray(g['keys'])[:3].tolist(),
    params=np.asarray(params).tolist(),
    loss_true=repr(float(g['loss_true'])), grad_true=[repr(float(v)) for v in np.asarray(g['grad_true'])],
    kf_theta_nll=repr(float(nll_t)), kf_true_nll=repr(float(nll_0)),
    kf_theta_dF=repr(np.asarray(dF).tolist()), kf_theta_dH=repr(np.asarray(dH).tolist()),
    chain_rule_check=dict(sum_dF_times_I=repr(float(jnp.sum(dF * jnp.eye(dx)))),
                          sum_dH_times_ones=repr(float(jnp.sum(dH * jnp.ones((dy, dx)))))),
    mc_mean_loss_dp=repr(float(np.mean(g['losses_dp']))), mc_mean_grad_dp=[repr(float(v)) for v in np.mean(g['grads_dp'], 0)],
    mc_mean_loss_stopped=repr(float(np.mean(g['losses_rein']))),
    mc_mean_grad_stopped=[repr(float(v)) for v in np.mean(g['grads_rein'], 0)],
    grad_rmse_dp=[repr(float(v)) for v in np.mean((g['grads_dp'] - np.asarray(g['grad_true'])) ** 2, 0) ** 0.5],
    grad_rmse_stopped=[repr(float(v)) for v in np.mean((g['grads_rein'] - np.asarray(g['grad_true'])) ** 2, 0) ** 0.5],
    first_mc=dict(loss_dp=repr(float(g['losses_dp'][0])), grad_dp=[repr(float(v)) for v in g['grads_dp'][0]],
                  loss_stopped=repr(float(g['losses_rein'][0])), grad_stopped=[repr(float(v)) for v in g['grads_rein'][0]]),
    xs=[repr(float(v)) for v in np.asarray(xs).ravel()], ys=[repr(float(v)) for v in np.asarray(ys).ravel()],
    nonfinite=dict(grads_dp=int((~np.isfinite(g['grads_dp'])).sum()), grads_rein=int((~np.isfinite(g['grads_rein'])).sum())),
)
json.dump(summary, open(cli.summary, 'w'), indent=1)
print('CAPTURE_DONE', json.dumps({k: summary[k] for k in ('loss_true', 'grad_true', 'kf_theta_nll', 'chain_rule_check')}))
