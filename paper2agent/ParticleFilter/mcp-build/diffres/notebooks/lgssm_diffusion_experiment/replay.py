"""Replay: load the saved inputs (data/inputs.npz), call the same upstream functions again, and compare with
outputs/reference_outputs.npz. Floats: exact equality is reported; pass criterion rtol=1e-12, atol=1e-12
(same key, inputs, x64, CPU). Integers/booleans/keys: exact.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lgssm_setup as S  # noqa: E402
import jax  # noqa: E402
import jax.numpy as jnp  # noqa: E402

inp = np.load(os.path.join(HERE, 'data', 'inputs.npz'))
ref = np.load(os.path.join(HERE, 'outputs', 'reference_outputs.npz'))
args = json.load(open(os.path.join(HERE, 'data', 'inputs_args.json')))['cli_args']
C = S.build(args['nsteps'], args['nparticles'], args['a'], args['T'], args['dsteps'], args['integrator'], args['sde'])

ys = jnp.asarray(inp['ys'])
key_pf = jnp.asarray(inp['key_pf'])
params_true = jnp.asarray(inp['params_true'])
init_params = jnp.asarray(inp['init_params'])
cartesian = jnp.asarray(inp['cartesian'])

checks = {}


def exact(name, x, y):
    checks[name] = dict(kind='exact', passed=bool(np.array_equal(np.asarray(x), np.asarray(y))))


def close(name, x, y):
    x, y = np.asarray(x, dtype=np.float64), np.asarray(y, dtype=np.float64)
    both_nan = np.isnan(x) & np.isnan(y)
    d = np.where(both_nan, 0., np.abs(x - y))
    checks[name] = dict(kind='allclose rtol=1e-12 atol=1e-12', bitwise_equal=bool(np.array_equal(x, y, equal_nan=True)),
                        max_abs_diff=float(np.max(d)) if d.size else 0.,
                        passed=bool(np.allclose(x, y, rtol=1e-12, atol=1e-12, equal_nan=True)))


# Input provenance: keys from rnd_keys.npy row and the data simulation
rnd_keys = np.load(os.path.join(HERE, 'run', 'rnd_keys.npy'))
exact('key_mc == rnd_keys[0]', inp['key_mc'], rnd_keys[0])
ks, kp = jax.random.split(jnp.asarray(inp['key_mc']))
exact('key_simulation', ks, inp['key_simulation'])
exact('key_pf', kp, inp['key_pf'])
xs_r, ys_r = S.simulate_lgssm(jnp.asarray(inp['key_simulation']), S.semigroup, S.trans_cov, S.obs_op, S.obs_cov,
                              S.m0, S.v0, args['nsteps'])
close('xs (simulate_lgssm)', xs_r, inp['xs'])
close('ys (simulate_lgssm)', ys_r, inp['ys'])
close('cartesian grid', C['cartesian'], cartesian)

# Upstream computations from the saved inputs
losses_kf = C['vloss_fn_kf'](cartesian, ys)
losses_pf = C['vloss_fn_pf'](cartesian, ys, key_pf)
close('losses_kf', losses_kf, ref['losses_kf'])
close('losses_pf', losses_pf, ref['losses_pf'])
close('err_loss', jnp.mean((losses_kf - losses_pf) ** 2), ref['err_loss'])

mfs_kf, vfs_kf, nll_kf = C['jitted_kf'](params_true, ys)
sampless, log_wss, nll_path, esss = C['jitted_pf_full'](params_true, ys, key_pf)
mfs_pf, vfs_pf, kls, bs, ekl, eb = S.filtering_errors(mfs_kf, vfs_kf, sampless, log_wss)
for k, v in dict(mfs_kf=mfs_kf, vfs_kf=vfs_kf, nll_kf_true=nll_kf, sampless=sampless, log_wss=log_wss, esss=esss,
                 nll_pf_true_path=nll_path, mfs_pf=mfs_pf, vfs_pf=vfs_pf, kl_per_step=kls, bures_per_step=bs,
                 err_filtering_kl=ekl, err_filtering_bures=eb).items():
    close(k, v, ref[k])

v, g = jax.jit(jax.value_and_grad(C['loss_fn_pf']))(params_true, ys, key_pf)
close('nll_pf_true', v, ref['nll_pf_true']); close('grad_pf_true', g, ref['grad_pf_true'])
v, g = jax.jit(jax.value_and_grad(C['loss_fn_kf']))(params_true, ys)
close('grad_kf_true', g, ref['grad_kf_true'])
v, g = jax.jit(jax.value_and_grad(C['loss_fn_pf']))(init_params, ys, key_pf)
close('nll_pf_init', v, ref['nll_pf_init']); close('grad_pf_init', g, ref['grad_pf_init'])

opt_params, st = C['solver'].run(init_params, ys_=ys, key_=key_pf)
close('opt_params', opt_params, ref['opt_params'])
close('opt_fun_val', st.fun_val, ref['opt_fun_val'])
for k, val in dict(opt_success=st.success, opt_status=st.status, opt_iter_num=st.iter_num,
                   opt_num_fun_eval=st.num_fun_eval, opt_num_jac_eval=st.num_jac_eval).items():
    exact(k, val, ref[k])

result = dict(all_passed=all(c['passed'] for c in checks.values()),
              all_floats_bitwise=all(c.get('bitwise_equal', True) for c in checks.values()),
              n_checks=len(checks), checks=checks)
with open(os.path.join(HERE, 'outputs', 'replay_comparison.json'), 'w') as f:
    json.dump(result, f, indent=1)
print(json.dumps(result, indent=1))
sys.exit(0 if result['all_passed'] else 1)
