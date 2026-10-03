"""Bootstrap particle filter (SMC) for linear Gaussian state-space models with diffres resamplers.

Upstream sources (diffres @ 767effe):
- diffres/feynman_kac.py: smc_feynman_kac, compute_ess (the SMC itself, called unchanged).
- tests/test_filters.py lines 59-73 and experiments/lgssm/{diffusion,baselines,ot,soft,gumbel}.py lines 59-80:
  bootstrap Feynman-Kac model (m0 sampler, log_g0, m_log_g) and resampler wrappers, extracted here as
  closures over user-supplied matrices.
- experiments/lgssm/diffusion.py lines 115-122: weighted filtering moments of the particles and the comparison with
  the exact Kalman filter (diffres.gaussian_filters.kf, diffres.tools.kl, diffres.tools.bures).
- demos/gradient_variance2.py lines 63-89: jax.value_and_grad of the SMC negative log-likelihood.
"""
import json
import math
import uuid
from pathlib import Path
from typing import Annotated, Literal

import jax
import jax.numpy as jnp
import numpy as np
from fastmcp import FastMCP

from diffres.feynman_kac import smc_feynman_kac
from diffres.gaussian_filters import kf
from diffres.resampling import (diffusion_resampling, ensemble_ot, gumbel_softmax, multinomial,
                                multinomial_stopped, soft_resampling, stratified, systematic)
from diffres.tools import bures, kl, logpdf_mvn_chol

# All upstream tests and experiments run in float64 on CPU.
jax.config.update("jax_enable_x64", True)

REFERENCE = ("https://github.com/zgbkdlm/diffres/blob/767effe3e755067eb8a04422597fbf37eb8ab754/"
             "diffres/feynman_kac.py")
PROJECT_ROOT = Path(__file__).resolve().parents[2]
TOOL_NAME = "diffres_run_lgssm_particle_filter"

feynman_kac_mcp = FastMCP(name="feynman_kac")

_MODEL_KEYS = ("F", "Q", "H", "R", "m0", "P0")


def _load_model(model_path: str) -> dict:
    path = Path(model_path)
    if not path.is_file():
        raise FileNotFoundError(f"model_path does not exist: {model_path}")
    spec = json.loads(path.read_text())
    missing = [k for k in _MODEL_KEYS if k not in spec]
    if missing:
        raise ValueError(f"model JSON is missing keys {missing}; required keys are {list(_MODEL_KEYS)}")
    model = {k: np.asarray(spec[k], dtype=np.float64) for k in _MODEL_KEYS}
    for k, v in model.items():
        if not np.all(np.isfinite(v)):
            raise ValueError(f"model entry {k} contains non-finite values")
    F, Q, H, R, m0, P0 = (model[k] for k in _MODEL_KEYS)
    if F.ndim != 2 or F.shape[0] != F.shape[1]:
        raise ValueError(f"F must be a square (dx, dx) matrix, got shape {F.shape}")
    dx = F.shape[0]
    if H.ndim != 2 or H.shape[1] != dx:
        raise ValueError(f"H must have shape (dy, {dx}), got {H.shape}")
    dy = H.shape[0]
    for name, mat, d in (("Q", Q, dx), ("P0", P0, dx), ("R", R, dy)):
        if mat.shape != (d, d):
            raise ValueError(f"{name} must have shape ({d}, {d}), got {mat.shape}")
        if not np.allclose(mat, mat.T, rtol=1e-10, atol=1e-12):
            raise ValueError(f"{name} must be symmetric (it is a covariance matrix; diffres.gaussian_filters.kf "
                             f"uses it as given, while jnp.linalg.cholesky would silently symmetrise it)")
        try:
            np.linalg.cholesky(mat)
        except np.linalg.LinAlgError:
            raise ValueError(f"{name} must be positive definite") from None
    if m0.shape != (dx,):
        raise ValueError(f"m0 must have shape ({dx},), got {m0.shape}")
    return model


def _load_observations(observations_path: str, dy: int) -> np.ndarray:
    path = Path(observations_path)
    if not path.is_file():
        raise FileNotFoundError(f"observations_path does not exist: {observations_path}")
    with np.load(path) as data:
        if "ys" not in data:
            raise ValueError(f"observations file must contain an array 'ys'; found {list(data.keys())}")
        ys = np.asarray(data["ys"], dtype=np.float64)
    if ys.ndim == 1 and dy == 1:
        ys = ys[:, None]  # (T+1,) with dy = 1 is read as (T+1, 1); per-step values are unchanged
    if ys.ndim != 2 or ys.shape[1] != dy or ys.shape[0] < 1:
        raise ValueError(f"ys must have shape (T+1, {dy}) with ys[0] the time-0 observation, got {ys.shape}")
    if not np.all(np.isfinite(ys)):
        raise ValueError("ys contains non-finite values (missing observations are not supported upstream)")
    return ys


def _resolve_key(seed: int, prng_key: list[int] | None):
    if prng_key is None:
        return jax.random.PRNGKey(seed)
    if len(prng_key) != 2 or any((not isinstance(v, int)) or v < 0 or v >= 2 ** 32 for v in prng_key):
        raise ValueError("prng_key must be exactly two uint32 integers (raw jax.random.PRNGKey data)")
    return jnp.asarray(prng_key, dtype=jnp.uint32)


def _make_resampling(method, nparticles, diffusion_a, diffusion_T, diffusion_steps, diffusion_integrator,
                     diffusion_ode, diffusion_jitter, ot_eps, ot_implicit_diff, soft_alpha, gumbel_tau):
    """Resampling callable (key, log_ws, samples) -> (log_ws, samples) as wrapped in tests/test_filters.py and
    experiments/lgssm/*.py; returns the callable and the resolved settings."""
    if method in ("multinomial", "stratified", "systematic", "multinomial_stopped"):
        fn = {"multinomial": multinomial, "stratified": stratified, "systematic": systematic,
              "multinomial_stopped": multinomial_stopped}[method]
        return fn, {}
    if method == "diffusion":
        if not diffusion_a < 0:
            raise ValueError("diffusion_a must be negative (diffusion_resampling docstring)")
        if not diffusion_T > 0:
            raise ValueError("diffusion_T must be positive")
        if diffusion_steps < 1:
            raise ValueError("diffusion_steps must be >= 1")
        if diffusion_jitter < 0:
            raise ValueError("diffusion_jitter must be >= 0")
        if diffusion_integrator == "tweedie" and diffusion_ode:
            raise ValueError("upstream diffusion_resampling implements integrator 'tweedie' only with ode=False")
        if diffusion_integrator == "diffrax" and not diffusion_ode:
            raise ValueError("upstream diffusion_resampling implements integrator 'diffrax' only with ode=True")
        ts = jnp.linspace(0., diffusion_T, diffusion_steps + 1)

        def resampling(key_, log_ws_, samples_):
            return diffusion_resampling(key_, log_ws_, samples_, diffusion_a, ts, integrator=diffusion_integrator,
                                        ode=diffusion_ode, jitter=diffusion_jitter)
        return resampling, {"a": diffusion_a, "T": diffusion_T, "steps": diffusion_steps,
                            "ts": f"linspace(0, {diffusion_T}, {diffusion_steps + 1})",
                            "integrator": diffusion_integrator, "ode": diffusion_ode, "jitter": diffusion_jitter}
    if method == "ensemble_ot":
        if ot_eps is not None and not ot_eps > 0:
            raise ValueError("ot_eps must be positive (or null for the upstream default 1/log(N))")
        if ot_eps is None and nparticles < 2:
            raise ValueError("the upstream default ot_eps = 1/log(N) needs nparticles >= 2; pass ot_eps explicitly")

        def resampling(key_, log_ws_, samples_):
            return ensemble_ot(key_, log_ws_, samples_, ot_eps, implicit_diff=ot_implicit_diff)
        eps_used = ot_eps if ot_eps is not None else 1 / math.log(nparticles)
        return resampling, {"eps": eps_used, "eps_from_upstream_default": ot_eps is None,
                            "implicit_diff": ot_implicit_diff}
    if method == "soft":
        if not 0 <= soft_alpha <= 1:
            raise ValueError("soft_alpha must lie in [0, 1]")

        def resampling(key_, log_ws_, samples_):
            return soft_resampling(key_, log_ws_, samples_, soft_alpha)
        return resampling, {"alpha": soft_alpha}
    if method == "gumbel_softmax":
        if not gumbel_tau > 0:
            raise ValueError("gumbel_tau must be positive")

        def resampling(key_, log_ws_, samples_):
            return gumbel_softmax(key_, log_ws_, samples_, gumbel_tau)
        return resampling, {"tau": gumbel_tau}
    raise ValueError(f"unknown resampling method {method}")


# What jax.grad differentiates for each resampler (diffres/resampling.py) and what the paper says about it
# (references: Section 1 and Appendix F/Table 20 of the paper).
_INDEX_NOTE = ("index resampling has no pathwise gradient (paper Table 20); jax.grad treats the resampled ancestor "
               "indices as constants, so the dependence of the resampling step on F and H is dropped")
_GRADIENT_NOTES = {
    "multinomial": _INDEX_NOTE,
    "stratified": _INDEX_NOTE,
    "systematic": _INDEX_NOTE,
    "multinomial_stopped": ("stop-gradient multinomial resampling (Scibior & Wood, 2021): same forward pass as "
                            "multinomial, the weights' gradient enters through a stop-gradient correction; the paper "
                            "classes it as REINFORCE-based, which often has high variance"),
    "diffusion": "pathwise gradient through diffusion resampling (the paper's method)",
    "ensemble_ot": "pathwise gradient through entropic OT resampling (implicit or unrolled Sinkhorn per ot_implicit_diff)",
    "soft": ("gradient flows only through the soft-resampling importance weights, not the sampled indices "
             "(partially differentiable and biased, paper Appendix F)"),
    "gumbel_softmax": "pathwise gradient through the Gumbel-softmax relaxation (biased for tau > 0, paper Appendix F)",
}


@feynman_kac_mcp.tool()
def diffres_run_lgssm_particle_filter(
    model_path: Annotated[str, "JSON file with LGSSM matrices F (dx,dx), Q (dx,dx), H (dy,dx), R (dy,dy), m0 (dx), "
                               "P0 (dx,dx): x_k = F x_{k-1} + N(0,Q), y_k = H x_k + N(0,R), x_0 ~ N(m0,P0)"],
    observations_path: Annotated[str, ".npz file with 'ys' of shape (T+1, dy); ys[0] is the time-0 observation "
                                      "((T+1,) is accepted when dy = 1)"],
    nparticles: Annotated[int, "Number of particles N (upstream LGSSM experiments use 32, tests 1000)"] = 32,
    resampling_method: Annotated[Literal["diffusion", "multinomial", "stratified", "systematic",
                                         "multinomial_stopped", "ensemble_ot", "soft", "gumbel_softmax"],
                                 "Resampler used inside the SMC"] = "diffusion",
    resampling_threshold: Annotated[float, "Resample when ESS < threshold * N; 1.0 (upstream default) resamples at "
                                           "every step, 0 never resamples"] = 1.0,
    diffusion_a: Annotated[float, "diffusion: negative forward noising coefficient a"] = -0.5,
    diffusion_T: Annotated[float, "diffusion: terminal time T (default 3 as experiments/lgssm; "
                                  "tests/test_filters.py uses 2)"] = 3.0,
    diffusion_steps: Annotated[int, "diffusion: number of integration steps K, ts = linspace(0, T, K+1) (default 8 "
                                    "as experiments/lgssm; tests/test_filters.py uses 7)"] = 8,
    diffusion_integrator: Annotated[Literal["euler", "lord_and_rougemont", "jentzen_and_kloeden", "tweedie",
                                            "diffrax"],
                                    "diffusion: integrator ('tweedie' needs ode=false, 'diffrax' needs ode=true)"]
    = "euler",
    diffusion_ode: Annotated[bool, "diffusion: true = probability-flow ODE, false = reverse SDE"] = True,
    diffusion_jitter: Annotated[float, "diffusion: jitter added to the reference variance (gradient demo uses 1e-5)"]
    = 0.0,
    ot_eps: Annotated[float | None, "ensemble_ot: entropic regulariser; null uses the upstream default 1/log(N)"]
    = None,
    ot_implicit_diff: Annotated[bool, "ensemble_ot: implicit differentiation of Sinkhorn; default false (unrolled) "
                                      "as experiments/lgssm/ot.py, whereas the upstream function default and "
                                      "tests/test_filters.py use true; forward values are the same"] = False,
    soft_alpha: Annotated[float, "soft: softening parameter alpha in [0, 1] (1 = no softening)"] = 0.5,
    gumbel_tau: Annotated[float, "gumbel_softmax: positive temperature tau"] = 0.5,
    seed: Annotated[int, "Seed for jax.random.PRNGKey(seed)"] = 0,
    prng_key: Annotated[list[int] | None, "Optional raw PRNGKey data (two uint32 values) used instead of seed"]
    = None,
    save_particle_path: Annotated[bool, "Also save particles and log-weights of all T+1 steps (else final step "
                                        "only)"] = False,
    compute_gradient: Annotated[bool, "Also compute the gradient of nll w.r.t. F and H by jax.value_and_grad"]
    = False,
    compare_to_kalman: Annotated[bool, "Also run the exact Kalman filter and compute per-step KL and Bures "
                                       "errors of the particle filtering moments"] = False,
    output_dir: Annotated[str | None, "Base output directory; a fresh subdirectory is created per call"] = None,
) -> dict:
    """Run a bootstrap particle filter on a linear Gaussian state-space model with a diffres resampler.
    LGSSM JSON + observations .npz -> negative log-likelihood, ESS, filtering moments (.npz), optional gradient and KF comparison.
    """
    model = _load_model(model_path)
    F, Q, H, R, m0, P0 = (model[k] for k in _MODEL_KEYS)
    dx, dy = F.shape[0], H.shape[0]
    ys_np = _load_observations(observations_path, dy)
    nsteps = ys_np.shape[0] - 1
    if nparticles < 1:
        raise ValueError("nparticles must be >= 1")
    if not 0 <= resampling_threshold <= 1:
        raise ValueError("resampling_threshold must lie in [0, 1]")
    key = _resolve_key(seed, prng_key)
    resampling, method_settings = _make_resampling(
        resampling_method, nparticles, diffusion_a, diffusion_T, diffusion_steps, diffusion_integrator,
        diffusion_ode, diffusion_jitter, ot_eps, ot_implicit_diff, soft_alpha, gumbel_tau)

    ys = jnp.asarray(ys_np)
    m0_j, F_j, H_j = jnp.asarray(m0), jnp.asarray(F), jnp.asarray(H)
    chol_P0 = jnp.linalg.cholesky(jnp.asarray(P0))
    chol_Q = jnp.linalg.cholesky(jnp.asarray(Q))
    R_j = jnp.asarray(R)
    r_diagonal = bool(np.count_nonzero(R - np.diag(np.diag(R))) == 0)
    r_std = jnp.sqrt(jnp.diag(R_j))
    chol_R = jnp.linalg.cholesky(R_j)

    # Bootstrap Feynman-Kac model of tests/test_filters.py lines 59-73 (experiments/lgssm/*.py lines 63-80),
    # with matrix noise factors (Cholesky, as diffres.tools.simulate_lgssm) in place of the 1-D scalar roots.
    def m0_sampler(key_, _):
        rnds = jax.random.normal(key_, shape=(nparticles, dx))
        return m0_j + rnds @ chol_P0.T

    def log_obs_density(y, xs, obs_op):
        if r_diagonal:  # sum of univariate normal log-densities, as upstream
            return jnp.sum(jax.scipy.stats.norm.logpdf(y, xs @ obs_op.T, r_std), axis=-1)
        # full R: multivariate normal log-density with diffres.tools.logpdf_mvn_chol (as in gaussian_filters.kf)
        return jax.vmap(lambda x: logpdf_mvn_chol(y, obs_op @ x, chol_R))(xs)

    def run_smc(semigroup, obs_op):
        def log_g0(samples, y0):
            return log_obs_density(y0, samples, obs_op)

        def m_log_g(key_, samples, y):
            rnds = jax.random.normal(key_, shape=(nparticles, dx))
            prop_samples = samples @ semigroup.T + rnds @ chol_Q.T
            return log_obs_density(y, prop_samples, obs_op), prop_samples

        sampless, log_wss, nll, esss = smc_feynman_kac(key, m0_sampler, log_g0, m_log_g, ys, nparticles, nsteps,
                                                       resampling=resampling,
                                                       resampling_threshold=resampling_threshold,
                                                       return_path=True)
        return nll, (sampless, log_wss, esss)

    grads = None
    if compute_gradient:
        (nll, (sampless, log_wss, esss)), grads = jax.value_and_grad(run_smc, argnums=(0, 1), has_aux=True)(F_j, H_j)
    else:
        nll, (sampless, log_wss, esss) = run_smc(F_j, H_j)

    # Weighted filtering moments, experiments/lgssm/diffusion.py lines 118-120.
    mfs_pf = jnp.einsum('knd,kn->kd', sampless, jnp.exp(log_wss))
    vfs_pf = jnp.einsum('kni,knj,kn->kij', (sampless - mfs_pf[:, None, :]), (sampless - mfs_pf[:, None, :]),
                        jnp.exp(log_wss))

    nll_f = float(nll)
    esss_np = np.asarray(esss)
    arrays = {
        "samples": np.asarray(sampless[-1]), "log_weights": np.asarray(log_wss[-1]),
        "ess": esss_np, "filtering_means": np.asarray(mfs_pf), "filtering_covs": np.asarray(vfs_pf),
        "nll": np.asarray(nll_f), "nll_plus_log_n": np.asarray(nll_f + math.log(nparticles)),
        "prng_key": np.asarray(key, dtype=np.uint32),
    }
    if save_particle_path:
        arrays["samples_path"] = np.asarray(sampless)
        arrays["log_weights_path"] = np.asarray(log_wss)

    result = {}
    if grads is not None:
        dF, dH = (np.asarray(g) for g in grads)
        arrays["grad_F"], arrays["grad_H"] = dF, dH
        result["gradient"] = {"grad_F_frobenius_norm": float(np.linalg.norm(dF)),
                              "grad_H_frobenius_norm": float(np.linalg.norm(dH)),
                              "all_finite": bool(np.all(np.isfinite(dF)) and np.all(np.isfinite(dH))),
                              "note": _GRADIENT_NOTES[resampling_method]}

    if compare_to_kalman:
        # experiments/lgssm/diffusion.py lines 116-122: KL and Bures between KF and PF filtering Gaussians.
        mfs_kf, vfs_kf, nll_kf, *_ = kf(ys, m0_j, jnp.asarray(P0), F_j, jnp.asarray(Q), H_j, R_j)
        kl_steps = np.asarray(jax.vmap(kl, in_axes=[0, 0, 0, 0])(mfs_kf, vfs_kf, mfs_pf, vfs_pf))
        bures_steps = np.asarray(jax.vmap(bures, in_axes=[0, 0, 0, 0])(mfs_kf, vfs_kf, mfs_pf, vfs_pf))
        arrays.update({"kf_filtering_means": np.asarray(mfs_kf), "kf_filtering_covs": np.asarray(vfs_kf),
                       "kf_nll": np.asarray(float(nll_kf)), "kl_per_step": kl_steps, "bures_per_step": bures_steps})
        result["kalman_comparison"] = {
            "kf_nll": float(nll_kf),
            "nll_plus_log_n_minus_kf_nll": nll_f + math.log(nparticles) - float(nll_kf),
            "mean_kl": float(np.mean(kl_steps)), "max_kl": float(np.max(kl_steps)),
            "mean_bures": float(np.mean(bures_steps)), "max_bures": float(np.max(bures_steps)),
            "kl_definition": "diffres.tools.kl(m_KF, P_KF, m_PF, P_PF) per step = 2 * KL(N_KF || N_PF) "
                             "(upstream omits the factor 1/2); mean over all T+1 steps as in experiments/lgssm",
            "bures_definition": "diffres.tools.bures = squared 2-Wasserstein distance between the two Gaussians",
            "kl_all_finite": bool(np.all(np.isfinite(kl_steps))),
        }

    base = Path(output_dir) if output_dir else PROJECT_ROOT / "tmp" / "outputs" / TOOL_NAME
    out_dir = (base / uuid.uuid4().hex).resolve()
    out_dir.mkdir(parents=True, exist_ok=False)
    npz_path = out_dir / "particle_filter.npz"
    np.savez(npz_path, **arrays)

    n_resampled = int(np.sum(esss_np[:-1] < resampling_threshold * nparticles))
    return {
        "message": (f"Bootstrap PF with {resampling_method} resampling: N={nparticles}, T={nsteps}, "
                    f"nll={nll_f:.6g} (nll + log N = {nll_f + math.log(nparticles):.6g})."),
        "reference": REFERENCE,
        "artifacts": [{"description": "particle filter results (.npz): final-step 'samples' (N, dx) and "
                                      "normalised 'log_weights' (N,) [usable as particles_path of the resampling "
                                      "tools], 'ess' (T+1,), weighted 'filtering_means' (T+1, dx) and "
                                      "'filtering_covs' (T+1, dx, dx), nll, nll_plus_log_n, prng_key"
                                      + ("; 'samples_path' (T+1, N, dx), 'log_weights_path' (T+1, N)"
                                         if save_particle_path else "")
                                      + ("; 'grad_F', 'grad_H'" if grads is not None else "")
                                      + ("; 'kf_filtering_means', 'kf_filtering_covs', 'kf_nll', 'kl_per_step', "
                                         "'bures_per_step'" if compare_to_kalman else ""),
                       "path": str(npz_path)}],
        "nll": nll_f,
        "nll_plus_log_n": nll_f + math.log(nparticles),
        "nll_note": ("nll is the raw upstream smc_feynman_kac value; it omits +log(N) in the time-0 term "
                     "(feynman_kac.py lines 82-85), so nll_plus_log_n = nll + log(N) estimates the exact "
                     "negative log-likelihood (comparable to the Kalman filter nll)"),
        "ess": {"final": float(esss_np[-1]), "min": float(esss_np.min()), "mean": float(esss_np.mean()),
                "resampling_steps": n_resampled, "nsteps": nsteps},
        "final_filtering_mean": [float(v) for v in np.asarray(mfs_pf[-1])],
        "nparticles": nparticles, "nsteps": nsteps, "dx": dx, "dy": dy,
        "observation_density": "sum of univariate normals (diagonal R)" if r_diagonal
        else "multivariate normal via diffres.tools.logpdf_mvn_chol (full R)",
        "resampling_method": resampling_method,
        "resampling_settings": method_settings,
        "resampling_threshold": resampling_threshold,
        "prng_key": [int(v) for v in np.asarray(key, dtype=np.uint32)],
        **result,
    }
