"""Replay driver for execution_id lgssm_gradient_demo.

Loads the saved reference (data/reference_nsteps16_np8.npz written by capture_run.py) in a fresh process and
recomputes it from the saved inputs:
  (1) PRNG keys: jax.random.PRNGKey(666), split(key)[0], split(key, num=1000)              -> exact
  (2) diffres.tools.simulate_lgssm(key_simulation, saved F,Q,H,R,m0,P0, nsteps)            -> exact
  (3) diffres.gaussian_filters.kf / rts on the saved ys (theta point and true parameters),
      jax.value_and_grad of the nll w.r.t. theta (script form) and w.r.t. F,H (tool form)   -> tolerance
  (4) PF value_and_grad for all 1000 saved keys with the script's own jitted diffpf_diff / diffpf_stopped,
      obtained by exec-ing the script's source text verbatim up to (excluding) the line 'nmcs = 1000'
      (i.e. without the Monte Carlo loop); the repo file is only read, never modified.     -> tolerance
  (5) numbers printed by the native (attempt 1) run vs the captured full-precision values -> 8-digit print tol
Writes data/replay_comparison.json.
"""
import hashlib
import json
import re
import sys
import time

import numpy as np
import jax
import jax.numpy as jnp

jax.config.update('jax_enable_x64', True)
from diffres.gaussian_filters import kf, rts  # noqa: E402
from diffres.tools import simulate_lgssm  # noqa: E402

NS = '/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/notebooks/lgssm_gradient_demo'
SCRIPT = '/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/repo/diffres/demos/gradient_variance2.py'
ref = np.load(f'{NS}/data/reference_nsteps16_np8.npz')
res = {}


def cmp(name, a, b, rtol=0., atol=0.):
    a, b = np.asarray(a), np.asarray(b)
    same_shape = a.shape == b.shape
    if not same_shape:
        res[name] = dict(pass_=False, reason=f'shape {a.shape} vs {b.shape}')
        return
    bitwise = bool(np.array_equal(a, b))
    if np.issubdtype(a.dtype, np.floating):
        d = np.abs(a.astype(np.float64) - b.astype(np.float64))
        maxabs = float(d.max()) if d.size else 0.
        rel = d / np.maximum(np.abs(b.astype(np.float64)), 1e-300)
        maxrel = float(rel.max()) if rel.size else 0.
        ok = bool(np.allclose(a, b, rtol=rtol, atol=atol))
    else:
        maxabs = maxrel = None
        ok = bitwise
    res[name] = dict(pass_=ok, bitwise_equal=bitwise, max_abs_diff=maxabs, max_rel_diff=maxrel,
                     rtol=rtol, atol=atol, shape=list(a.shape), dtype=str(a.dtype))


t0 = time.time()
# (1) keys
key = jax.random.PRNGKey(666)
cmp('key_PRNGKey666', key, ref['key'])
cmp('key_simulation', jax.random.split(key)[0], ref['key_simulation'])
cmp('keys_1000', jax.random.split(key, num=1000), ref['keys'])

# (2) simulation, direct upstream call with saved inputs
F, Q, H, R = (jnp.asarray(ref[k]) for k in ('semigroup', 'trans_cov', 'obs_op', 'obs_cov'))
m0, v0 = jnp.asarray(ref['m0']), jnp.asarray(ref['v0'])
nsteps = int(ref['nsteps'])
xs, ys = simulate_lgssm(jnp.asarray(ref['key_simulation']), F, Q, H, R, m0, v0, nsteps)
cmp('simulate_lgssm_xs', xs, ref['xs'])
cmp('simulate_lgssm_ys', ys, ref['ys'])

# (3) Kalman filter / RTS, direct upstream calls on the saved ys
ys_ref = jnp.asarray(ref['ys'])
params = jnp.asarray(ref['params'])
dx, dy = int(ref['dx']), int(ref['dy'])
F_t, H_t = params[0] * jnp.eye(dx), params[1] * jnp.ones((dy, dx))
TOL = dict(rtol=1e-12, atol=1e-12)  # same key/inputs/x64 on CPU: expect bitwise or ~1e-12


def loss_theta(p, y):  # the script's loss_kf(params, ys) (lines 40-43, 92-93): F = p0*I, H = p1*ones
    return kf(y, m0, v0, p[0] * jnp.eye(dx), Q, p[1] * jnp.ones((dy, dx)), R)[2]


lt, gt = jax.value_and_grad(loss_theta)(params, ys_ref)
cmp('kf_loss_true', lt, ref['loss_true'], **TOL)
cmp('kf_grad_true', gt, ref['grad_true'], **TOL)
out = kf(ys_ref, m0, v0, F_t, Q, H_t, R)
for nm, v in zip(('mfs', 'vfs', 'nll', 'mps', 'vps'), out):
    cmp(f'kf_theta_{nm}', v, ref[f'kf_theta_{nm}'], **TOL)
mss, vss = rts(out[0], out[1], out[3], out[4], F_t)
cmp('rts_theta_mss', mss, ref['rts_theta_mss'], **TOL)
cmp('rts_theta_vss', vss, ref['rts_theta_vss'], **TOL)
out0 = kf(ys_ref, m0, v0, F, Q, H, R)
for nm, v in zip(('mfs', 'vfs', 'nll', 'mps', 'vps'), out0):
    cmp(f'kf_true_{nm}', v, ref[f'kf_true_{nm}'], **TOL)
mss0, vss0 = rts(out0[0], out0[1], out0[3], out0[4], F)
cmp('rts_true_mss', mss0, ref['rts_true_mss'], **TOL)
cmp('rts_true_vss', vss0, ref['rts_true_vss'], **TOL)
nFH, (dF, dH) = jax.value_and_grad(lambda F_, H_: kf(ys_ref, m0, v0, F_, Q, H_, R)[2], argnums=(0, 1))(F_t, H_t)
cmp('kf_theta_nll_via_FH', nFH, ref['kf_theta_nll_via_FH'], **TOL)
cmp('kf_theta_dF', dF, ref['kf_theta_dF'], **TOL)
cmp('kf_theta_dH', dH, ref['kf_theta_dH'], **TOL)
# chain rule: d nll/d theta0 = sum(dF * I), d nll/d theta1 = sum(dH * ones)
cmp('chain_rule_theta_vs_FH', jnp.array([jnp.sum(dF * jnp.eye(dx)), jnp.sum(dH * jnp.ones((dy, dx)))]),
    ref['grad_true'], rtol=1e-12, atol=1e-12)
t_kf = time.time() - t0

# (4) PF gradients with the script's own code, executed up to (excluding) the MC loop
src = open(SCRIPT).read()
marker = '\nnmcs = 1000\n'
assert src.count(marker) == 1
prefix = src.split(marker)[0]
prefix_sha = hashlib.sha256(prefix.encode()).hexdigest()
sys.argv = [SCRIPT, '--nsteps', str(nsteps), '--nparticles', str(int(ref['nparticles']))]
gs = {'__name__': '__gradient_variance2_prefix__', '__file__': SCRIPT}
t1 = time.time()
exec(compile(prefix, SCRIPT, 'exec'), gs)
cmp('prefix_ys', gs['ys'], ref['ys'])
cmp('prefix_loss_true', gs['loss_true'], ref['loss_true'], **TOL)
cmp('prefix_grad_true', gs['grad_true'], ref['grad_true'], **TOL)
keys = jnp.asarray(ref['keys'])
n = keys.shape[0]
L_dp, G_dp, L_st, G_st = np.zeros(n), np.zeros((n, 2)), np.zeros(n), np.zeros((n, 2))
for i in range(n):
    l, g_ = gs['diffpf_diff'](keys[i], gs['params'], gs['ys'])
    L_dp[i], G_dp[i] = l, g_
    l, g_ = gs['diffpf_stopped'](keys[i], gs['params'], gs['ys'])
    L_st[i], G_st[i] = l, g_
t_pf = time.time() - t1
PF_TOL = dict(rtol=1e-9, atol=1e-9)
cmp('pf_losses_diffusion', L_dp, ref['losses_dp'], **PF_TOL)
cmp('pf_grads_diffusion', G_dp, ref['grads_dp'], **PF_TOL)
cmp('pf_losses_multinomial_stopped', L_st, ref['losses_rein'], **PF_TOL)
cmp('pf_grads_multinomial_stopped', G_st, ref['grads_rein'], **PF_TOL)

# (5) native attempt-1 stdout (numpy default 8-significant-digit print) vs captured values
log = open(f'{NS}/logs/attempt1_native_nsteps16_np8.stdout').read()
tail = log.split('\n999\n', 1)[1]
nums = [float(x) for x in re.findall(r'-?\d+\.\d+(?:e[-+]?\d+)?', tail)]
printed = dict(loss_true=nums[0], grad_true=nums[1:3], mc_loss_dp=nums[3], mc_grad_dp=nums[4:6],
               mc_loss_stopped=nums[6], mc_grad_stopped=nums[7:9], rmse_dp=nums[9:11], rmse_stopped=nums[11:13])
captured = dict(loss_true=float(ref['loss_true']), grad_true=ref['grad_true'].tolist(),
                mc_loss_dp=float(ref['losses_dp'].mean()), mc_grad_dp=ref['grads_dp'].mean(0).tolist(),
                mc_loss_stopped=float(ref['losses_rein'].mean()), mc_grad_stopped=ref['grads_rein'].mean(0).tolist(),
                rmse_dp=(np.mean((ref['grads_dp'] - ref['grad_true']) ** 2, 0) ** 0.5).tolist(),
                rmse_stopped=(np.mean((ref['grads_rein'] - ref['grad_true']) ** 2, 0) ** 0.5).tolist())
for k in printed:
    cmp(f'native_print_{k}', np.asarray(captured[k]), np.asarray(printed[k]), rtol=1e-7, atol=1e-8)

summary = dict(all_pass=all(v['pass_'] for v in res.values()),
               n_checks=len(res), n_bitwise=sum(bool(v.get('bitwise_equal')) for v in res.values()),
               script_prefix_sha256=prefix_sha, script_prefix_lines=prefix.count('\n') + 1,
               runtime_s=dict(keys_sim_kf_rts=t_kf, pf_1000x2_with_compile=t_pf),
               native_printed_values=printed, checks=res)
json.dump(summary, open(f'{NS}/data/replay_comparison.json', 'w'), indent=1)
print('REPLAY all_pass =', summary['all_pass'], 'checks =', summary['n_checks'], 'bitwise =', summary['n_bitwise'])
for k, v in res.items():
    print(f"{k:38s} pass={v['pass_']} bitwise={v.get('bitwise_equal')} maxabs={v.get('max_abs_diff')}")
