"""Reference driver for experiments/lgssm/diffusion.py, MC id 0, smallest settings.

Run from notebooks/lgssm_diffusion_experiment/run (contains a copy of rnd_keys.npy). Uses the script's own input
preparation (lgssm_setup.py, verbatim copy) and calls the upstream functions exactly as the script does. Saves the
inputs (data/inputs.npz) and the native outputs at float64 (outputs/reference_outputs.npz), and compares the scalar
metrics with the npz written by the unmodified upstream script run (run/lgssm/results/...).
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import lgssm_setup as S  # noqa: E402  (enables x64)
import jax  # noqa: E402
import jax.numpy as jnp  # noqa: E402

ARGS = dict(id_l=0, id_u=0, nsteps=32, nparticles=16, a=-1., T=1., dsteps=4, integrator='jentzen_and_kloeden',
            sde=True)
t_start = time.time()
C = S.build(ARGS['nsteps'], ARGS['nparticles'], ARGS['a'], ARGS['T'], ARGS['dsteps'], ARGS['integrator'],
            ARGS['sde'])

# Script lines 26 and 104-107
keys_mc = np.load(os.path.join(HERE, 'run', 'rnd_keys.npy'))[ARGS['id_l']:ARGS['id_u'] + 1]
mc_id, key_mc = 0, keys_mc[0]
key_simulation, key_pf = jax.random.split(key_mc)
xs, ys = S.simulate_lgssm(key_simulation, S.semigroup, S.trans_cov, S.obs_op, S.obs_cov, S.m0, S.v0, ARGS['nsteps'])

params_true = jnp.array([S.p1, S.p2])
init_params = jnp.array([S.p1 + 1, S.p2 + 1])

# Script lines 109-113: loss grid
losses_kf = C['vloss_fn_kf'](C['cartesian'], ys)
losses_pf = C['vloss_fn_pf'](C['cartesian'], ys, key_pf)
err_loss = jnp.mean((losses_kf - losses_pf) ** 2)

# Script lines 116-122: filtering error at the true parameters
mfs_kf, vfs_kf, nll_kf_true = C['jitted_kf'](params_true, ys)
sampless, log_wss, nll_pf_true_path = C['jitted_pf'](params_true, ys, key_pf)
sampless_f, log_wss_f, nll_f, esss = C['jitted_pf_full'](params_true, ys, key_pf)
mfs_pf, vfs_pf, kls, bs, err_filtering_kl, err_filtering_bures = S.filtering_errors(mfs_kf, vfs_kf, sampless, log_wss)

# Loss + gradient at the true parameters (the objective the script hands to L-BFGS: loss_fn_pf, return_path=False)
nll_pf_true, grad_pf_true = jax.jit(jax.value_and_grad(C['loss_fn_pf']))(params_true, ys, key_pf)
nll_kf_true2, grad_kf_true = jax.jit(jax.value_and_grad(C['loss_fn_kf']))(params_true, ys)
# Same at the L-BFGS initial point (diagnoses the optimiser outcome)
nll_pf_init, grad_pf_init = jax.jit(jax.value_and_grad(C['loss_fn_pf']))(init_params, ys, key_pf)

# Script lines 125-126: optimisation
opt_params, opt_state = C['solver'].run(init_params, ys_=ys, key_=key_pf)
runtime = time.time() - t_start

os.makedirs(os.path.join(HERE, 'data'), exist_ok=True)
os.makedirs(os.path.join(HERE, 'outputs'), exist_ok=True)
np.savez(os.path.join(HERE, 'data', 'inputs.npz'),
         key_mc=np.asarray(key_mc), key_simulation=np.asarray(key_simulation), key_pf=np.asarray(key_pf),
         xs=np.asarray(xs), ys=np.asarray(ys), params_true=np.asarray(params_true),
         init_params=np.asarray(init_params), cartesian=np.asarray(C['cartesian']), ts=np.asarray(C['ts']),
         semigroup=np.asarray(S.semigroup), trans_cov=np.asarray(S.trans_cov), obs_op=np.asarray(S.obs_op),
         obs_cov=np.asarray(S.obs_cov), m0=np.asarray(S.m0), v0=np.asarray(S.v0))
with open(os.path.join(HERE, 'data', 'inputs_args.json'), 'w') as f:
    json.dump(dict(cli_args=ARGS, mc_id=mc_id, rnd_keys_row=int(mc_id),
                   key_derivation='key_simulation, key_pf = jax.random.split(rnd_keys[mc_id])',
                   model=dict(p1=S.p1, p2=S.p2, sig=S.sig, xi=S.xi, v0_=S.v0_, dx=S.dx, dy=S.dy),
                   resampling=dict(fn='diffres.resampling.diffusion_resampling', a=ARGS['a'],
                                   ts='linspace(0, T, dsteps+1)', integrator=ARGS['integrator'],
                                   ode=not ARGS['sde'], jitter=0., einsum=False),
                   smc=dict(fn='diffres.feynman_kac.smc_feynman_kac', resampling_threshold=1.,
                            nparticles=ARGS['nparticles'], nsteps=ARGS['nsteps'])), f, indent=1)

out = dict(losses_kf=losses_kf, losses_pf=losses_pf, err_loss=err_loss,
           mfs_kf=mfs_kf, vfs_kf=vfs_kf, nll_kf_true=nll_kf_true, grad_kf_true=grad_kf_true,
           sampless=sampless, log_wss=log_wss, esss=esss, nll_pf_true_path=nll_pf_true_path,
           nll_pf_true=nll_pf_true, grad_pf_true=grad_pf_true, nll_pf_init=nll_pf_init, grad_pf_init=grad_pf_init,
           mfs_pf=mfs_pf, vfs_pf=vfs_pf, kl_per_step=kls, bures_per_step=bs,
           err_filtering_kl=err_filtering_kl, err_filtering_bures=err_filtering_bures,
           opt_params=opt_params, opt_success=opt_state.success, opt_status=opt_state.status,
           opt_iter_num=opt_state.iter_num, opt_fun_val=opt_state.fun_val,
           opt_num_fun_eval=opt_state.num_fun_eval, opt_num_jac_eval=opt_state.num_jac_eval)
out = {k: np.asarray(v) for k, v in out.items()}
np.savez(os.path.join(HERE, 'outputs', 'reference_outputs.npz'), **out)

# Internal consistency of the two PF calls (same upstream call, with / without the [:3] slice)
consistency = dict(
    pf_full_vs_pf_samples_maxabs=float(np.max(np.abs(np.asarray(sampless_f) - np.asarray(sampless)))),
    pf_full_vs_pf_logws_maxabs=float(np.max(np.abs(np.asarray(log_wss_f) - np.asarray(log_wss)))),
    pf_full_vs_pf_nll_absdiff=float(abs(nll_f - nll_pf_true_path)),
    nll_path_vs_nopath_absdiff=float(abs(nll_pf_true_path - nll_pf_true)),
    kf_nll_jit_vs_grad_absdiff=float(abs(nll_kf_true - nll_kf_true2)))

# Compare with the unmodified script's own output file
a, T, d, integ = ARGS['a'], ARGS['T'], ARGS['dsteps'], ARGS['integrator']
script_npz = os.path.join(HERE, 'run', 'lgssm', 'results',
                          f'diffres-{a}-{T}-{d}-{integ}-{"sde" if ARGS["sde"] else "ode"}-{ARGS["nparticles"]}-0.npz')
cmp = {}
if os.path.exists(script_npz):
    sc = np.load(script_npz)
    for k in ['err_loss', 'err_filtering_kl', 'err_filtering_bures', 'opt_params', 'opt_success', 'opt_iter_num']:
        x, y = np.asarray(sc[k]), out[k]
        cmp[k] = dict(script=sc[k].tolist(), driver=y.tolist(),
                      max_abs_diff=float(np.max(np.abs(x.astype(np.float64) - y.astype(np.float64)))),
                      equal=bool(np.array_equal(x, y)))

summary = dict(runtime_s=runtime, jax_version=jax.__version__, x64=bool(jax.config.jax_enable_x64),
               devices=[str(dv) for dv in jax.devices()],
               scalars={k: out[k].tolist() for k in ['err_loss', 'err_filtering_kl', 'err_filtering_bures',
                                                     'nll_kf_true', 'grad_kf_true', 'nll_pf_true', 'grad_pf_true',
                                                     'nll_pf_init', 'grad_pf_init', 'opt_params', 'opt_success',
                                                     'opt_status', 'opt_iter_num', 'opt_fun_val',
                                                     'opt_num_fun_eval', 'opt_num_jac_eval']},
               ess_min=float(out['esss'].min()), ess_mean=float(out['esss'].mean()),
               shapes={k: list(v.shape) for k, v in out.items()},
               nan_counts={k: int(np.isnan(v).sum()) for k, v in out.items() if v.dtype.kind == 'f'},
               consistency=consistency, script_vs_driver=cmp, script_npz=script_npz)
with open(os.path.join(HERE, 'outputs', 'reference_summary.json'), 'w') as f:
    json.dump(summary, f, indent=1)
np.set_printoptions(precision=17)
print(json.dumps(summary, indent=1))
