"""Input preparation for experiments/lgssm/diffusion.py (diffres @ 767effe3), replicated verbatim.

The upstream script runs argparse and its MC loop at import time, so it cannot be imported. This module copies
its model constants and the closures it builds (script lines 25-93 and 96-102) unchanged, parameterised by the
same CLI arguments. Nothing here implements an algorithm: all computation goes to the upstream functions
diffres.feynman_kac.smc_feynman_kac, diffres.resampling.diffusion_resampling, diffres.gaussian_filters.kf,
diffres.tools.simulate_lgssm, diffres.tools.kl and diffres.tools.bures.

Only addition: `pf_full`, the same smc_feynman_kac call as the script's `pf` but without the `[:3]` slice, so the
ESS array (4th native output) is also captured.
"""
import jax
import jax.numpy as jnp
import numpy as np
import jaxopt
from diffres.resampling import diffusion_resampling
from diffres.feynman_kac import smc_feynman_kac
from diffres.gaussian_filters import kf as kf_
from diffres.tools import simulate_lgssm, bures, kl

jax.config.update("jax_enable_x64", True)  # script line 25

# Script lines 28-39
dx = 1
dy = 1
p1, p2, sig, xi, v0_ = 0.5, 1., 1., 0.5, 1.
semigroup = p1 * jnp.eye(dx)
trans_cov = sig * jnp.eye(dx)
obs_op = p2 * jnp.ones((dy, dx))
obs_cov = xi * jnp.eye(dy)
m0, v0 = jnp.zeros(dx), v0_ * jnp.eye(dx)


def build(nsteps, nparticles, a, T, dsteps, integrator, sde):
    """Return the closures of the upstream script for the given CLI arguments (script lines 43-102)."""
    ts = jnp.linspace(0., T, dsteps + 1)
    ode = not sde

    def kf(params, ys_):
        semigroup_ = params[0] * jnp.eye(dx)
        obs_op_ = params[1] * jnp.ones((dy, dx))
        return kf_(ys_, m0, v0, semigroup_, trans_cov, obs_op_, obs_cov)[:3]

    def resampling(key_, log_ws_, samples_):
        return diffusion_resampling(key_, log_ws_, samples_, a, ts, integrator=integrator, ode=ode)

    def m0_sampler(key_, _):
        rnds = jax.random.normal(key_, shape=(nparticles, dx))
        return m0 + v0_ ** 0.5 * rnds

    def _model(params):
        def log_g0(samples, y0):
            return jnp.sum(jax.scipy.stats.norm.logpdf(y0, params[1] * samples, xi ** 0.5), axis=-1)

        def m_log_g(key__, samples, y):
            rnds = jax.random.normal(key__, shape=(nparticles, dx))
            prop_samples = params[0] * samples + sig ** 0.5 * rnds
            log_potentials = jnp.sum(jax.scipy.stats.norm.logpdf(y, params[1] * prop_samples, xi ** 0.5), axis=-1)
            return log_potentials, prop_samples
        return log_g0, m_log_g

    def pf(params, ys_, key_, return_path=True):
        log_g0, m_log_g = _model(params)
        return smc_feynman_kac(key_, m0_sampler, log_g0, m_log_g, ys_, nparticles, nsteps,
                               resampling=resampling, resampling_threshold=1.,
                               return_path=return_path)[:3]

    def pf_full(params, ys_, key_, return_path=True):
        log_g0, m_log_g = _model(params)
        return smc_feynman_kac(key_, m0_sampler, log_g0, m_log_g, ys_, nparticles, nsteps,
                               resampling=resampling, resampling_threshold=1.,
                               return_path=return_path)

    def loss_fn_kf(params, ys_):
        return kf(params, ys_)[-1]

    def loss_fn_pf(params, ys_, key_):
        return pf(params, ys_, key_, return_path=False)[-1]

    vloss_fn_kf = jax.jit(jax.vmap(jax.vmap(loss_fn_kf, in_axes=[0, None]), in_axes=[0, None]))
    vloss_fn_pf = jax.jit(jax.vmap(jax.vmap(loss_fn_pf, in_axes=[0, None, None]), in_axes=[0, None, None]))
    solver = jaxopt.ScipyMinimize(method='L-BFGS-B', fun=loss_fn_pf, jit=True)

    ngrids1, ngrids2 = 128, 128
    grids_p1 = jnp.linspace(p1 - 0.1, p1 + 0.1, ngrids1)
    grids_p2 = jnp.linspace(p2 - 0.1, p2 + 0.1, ngrids2)
    mgrids = jnp.meshgrid(grids_p1, grids_p2)
    cartesian = jnp.dstack(mgrids)  # (ngrids2, ngrids1, 2)

    return dict(ts=ts, ode=ode, kf=kf, pf=pf, pf_full=pf_full, loss_fn_kf=loss_fn_kf, loss_fn_pf=loss_fn_pf,
                vloss_fn_kf=vloss_fn_kf, vloss_fn_pf=vloss_fn_pf, solver=solver, cartesian=cartesian,
                jitted_kf=jax.jit(kf), jitted_pf=jax.jit(pf), jitted_pf_full=jax.jit(pf_full))


def filtering_errors(mfs_kf, vfs_kf, sampless, log_wss):
    """Script lines 118-122 verbatim, also returning the per-time arrays before the mean."""
    mfs_pf = jnp.einsum('knd,kn->kd', sampless, jnp.exp(log_wss))
    vfs_pf = jnp.einsum('kni,knj,kn->kij', (sampless - mfs_pf[:, None, :]), (sampless - mfs_pf[:, None, :]),
                        jnp.exp(log_wss))
    kls = jax.vmap(kl, in_axes=[0, 0, 0, 0])(mfs_kf, vfs_kf, mfs_pf, vfs_pf)
    bs = jax.vmap(bures, in_axes=[0, 0, 0, 0])(mfs_kf, vfs_kf, mfs_pf, vfs_pf)
    return mfs_pf, vfs_pf, kls, bs, jnp.mean(kls), jnp.mean(bs)
