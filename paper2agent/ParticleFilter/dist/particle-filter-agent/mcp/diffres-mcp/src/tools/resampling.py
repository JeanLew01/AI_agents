"""Tools extracted from diffres/resampling.py (diffusion and baseline resamplers).

Upstream sources: diffres/resampling.py (diffusion_resampling, multinomial, stratified, systematic,
multinomial_stopped, ensemble_ot, soft_resampling, gumbel_softmax), demos/gaussian_mixture.ipynb (cell 6) and
experiments/gms/{diffusion,baselines,ot,soft,gumbel}.py, which normalise the log weights with logsumexp and call
the resampler under jax.jit with jax_enable_x64. diffres.feynman_kac.compute_ess gives the effective sample size.
"""
import uuid
from pathlib import Path
from typing import Annotated, Literal

import jax
import jax.numpy as jnp
import numpy as np
from fastmcp import FastMCP

from diffres.feynman_kac import compute_ess
from diffres.resampling import (diffusion_resampling, ensemble_ot, gumbel_softmax, multinomial,
                                multinomial_stopped, soft_resampling, stratified, systematic)

# All upstream experiments, tests and the demo notebook run in float64.
jax.config.update("jax_enable_x64", True)

REFERENCE = "https://github.com/zgbkdlm/diffres/blob/767effe3e755067eb8a04422597fbf37eb8ab754/diffres/resampling.py"
PROJECT_ROOT = Path(__file__).resolve().parents[2]

resampling_mcp = FastMCP(name="resampling")

_BASELINES = {
    "multinomial": multinomial,
    "stratified": stratified,
    "systematic": systematic,
    "multinomial_stopped": multinomial_stopped,
    "ensemble_ot": ensemble_ot,
    "soft": soft_resampling,
    "gumbel_softmax": gumbel_softmax,
}


def _resolve_key(seed: int, prng_key: list[int] | None):
    if prng_key is None:
        return jax.random.PRNGKey(seed)
    if len(prng_key) != 2 or any((not isinstance(k, int)) or k < 0 or k > 2 ** 32 - 1 for k in prng_key):
        raise ValueError("prng_key must be exactly two integers in [0, 2**32 - 1] (raw jax.random.PRNGKey data).")
    return jnp.array(prng_key, dtype=jnp.uint32)


def _load_particles(particles_path: str):
    """Read samples and (log) weights; return float64 samples, normalised log weights and the log normaliser."""
    path = Path(particles_path).expanduser()
    if not path.is_file():
        raise FileNotFoundError(f"particles_path not found: {path}")
    with np.load(path, allow_pickle=False) as data:
        keys = set(data.files)
        if "samples" not in keys:
            raise ValueError(f"{path} must contain an array 'samples' (N, d); found {sorted(keys)}.")
        has_lw, has_w = "log_weights" in keys, "weights" in keys
        if has_lw == has_w:
            raise ValueError(f"{path} must contain exactly one of 'log_weights' or 'weights'; found {sorted(keys)}.")
        samples = np.asarray(data["samples"], dtype=np.float64)
        raw = np.asarray(data["log_weights" if has_lw else "weights"], dtype=np.float64)
    if samples.ndim < 1 or samples.shape[0] < 2:
        raise ValueError(f"'samples' must have shape (N, ...) with N >= 2; got {samples.shape}.")
    if raw.shape != (samples.shape[0],):
        raise ValueError(f"weights must have shape ({samples.shape[0]},) to match samples; got {raw.shape}.")
    if not np.all(np.isfinite(samples)):
        raise ValueError("'samples' contains non-finite values.")
    if has_w:
        if np.any(np.isnan(raw)) or np.any(np.isinf(raw)) or np.any(raw < 0):
            raise ValueError("'weights' must be finite and non-negative.")
        with np.errstate(divide="ignore"):
            log_ws = np.log(raw)
    else:
        if np.any(np.isnan(raw)) or np.any(raw == np.inf):
            raise ValueError("'log_weights' must not contain NaN or +inf (-inf marks a zero weight).")
        log_ws = raw
    if not np.any(np.isfinite(log_ws)):
        raise ValueError("All weights are zero (all log weights are -inf).")
    # Every upstream caller normalises the log weights with logsumexp before resampling.
    log_ws = jnp.asarray(log_ws)
    log_normaliser = jax.scipy.special.logsumexp(log_ws)
    return jnp.asarray(samples), log_ws - log_normaliser, float(log_normaliser), "log_weights" if has_lw else "weights"


def _save(tool: str, output_dir: str | None, log_ws_out, samples_out) -> Path:
    base = Path(output_dir).expanduser() if output_dir else PROJECT_ROOT / "tmp" / "outputs" / tool
    out_dir = (base / uuid.uuid4().hex).resolve()
    out_dir.mkdir(parents=True, exist_ok=False)
    out_path = out_dir / "resampled.npz"
    np.savez(out_path, samples=np.asarray(samples_out), log_weights=np.asarray(log_ws_out))
    return out_path


def _check_finite_output(log_ws_out, samples_out, hint: str):
    if not (bool(jnp.all(jnp.isfinite(samples_out))) and not bool(jnp.any(jnp.isnan(log_ws_out)))):
        raise ValueError(f"The upstream resampler returned non-finite values. {hint}")


@resampling_mcp.tool()
def diffres_resample_particles_diffusion(
    particles_path: Annotated[str, ".npz with 'samples' (N, ...) float and exactly one of 'log_weights' (N,) or 'weights' (N,); weights are normalised before resampling; memory grows as N^2 x (sample size) float64 per integration step, so keep N to a few thousand"],
    a: Annotated[float, "Mean-reverting coefficient of the Ornstein-Uhlenbeck reference process; must be negative (more negative = faster mixing towards the empirical Gaussian reference); default -2 from demos/gaussian_mixture.ipynb (gms experiments use -1)"] = -2.0,
    T: Annotated[float, "Terminal diffusion time T > 0; ts = linspace(0, T, nsteps + 1) as in every upstream caller; default 1.0 from the demo notebook"] = 1.0,
    nsteps: Annotated[int, "Number of integration steps K >= 1; default 32 from the demo notebook"] = 32,
    integrator: Annotated[Literal["euler", "lord_and_rougemont", "jentzen_and_kloeden", "diffrax", "tweedie"], "Integrator of the reverse dynamics; 'diffrax' (diffrax Euler solver) requires ode=True and 'tweedie' requires ode=False; default 'euler' from the upstream signature (the demo notebook uses 'jentzen_and_kloeden')"] = "euler",
    ode: Annotated[bool, "True: probability-flow ODE (deterministic given the initial reference draw); False: reverse SDE; default True from the upstream signature"] = True,
    jitter: Annotated[float, "Non-negative value added to the reference variances for numerical stability (e.g. a dimension with zero weighted variance); upstream default 0"] = 0.0,
    seed: Annotated[int, "Seed for jax.random.PRNGKey(seed); ignored when prng_key is given"] = 0,
    prng_key: Annotated[list[int] | None, "Optional raw PRNG key (two uint32 values) used instead of seed, e.g. to reproduce a run with a split key"] = None,
    output_dir: Annotated[str | None, "Base output directory; a fresh unique subdirectory is created per call (default <project>/tmp/outputs/<tool>)"] = None,
) -> dict:
    """Resample a weighted particle set with diffusion resampling (empirical Gaussian reference, diffres.resampling.diffusion_resampling).
    Input is an .npz of samples and (log) weights; output is an .npz of N equally weighted resampled particles and log weights.
    """
    if not a < 0:
        raise ValueError("a must be negative (upstream: 'The forward noising parameter, must be negative').")
    if not T > 0:
        raise ValueError("T must be positive.")
    if nsteps < 1:
        raise ValueError("nsteps must be >= 1.")
    if jitter < 0:
        raise ValueError("jitter must be non-negative.")
    # Upstream raises NotImplementedError for these combinations; reject them with a clear message up front.
    if integrator == "diffrax" and not ode:
        raise ValueError("integrator='diffrax' is only implemented upstream for ode=True.")
    if integrator == "tweedie" and ode:
        raise ValueError("integrator='tweedie' is only implemented upstream for ode=False (SDE).")

    samples, log_ws, log_normaliser, weight_field = _load_particles(particles_path)
    key = _resolve_key(seed, prng_key)
    ts = jnp.linspace(0., T, nsteps + 1)

    # Called under jax.jit as in experiments/gms/diffusion.py (the demo notebook calls it eagerly; the two agree to ~1e-12).
    @jax.jit
    def resampling(key_, log_ws_, samples_):
        return diffusion_resampling(key_, log_ws_, samples_, a, ts, integrator=integrator, ode=ode, jitter=jitter)

    log_ws_out, samples_out = resampling(key, log_ws, samples)
    _check_finite_output(log_ws_out, samples_out,
                         "A dimension with zero weighted variance makes the reference degenerate; try jitter > 0.")
    out_path = _save("diffres_resample_particles_diffusion", output_dir, log_ws_out, samples_out)
    n = int(samples.shape[0])
    return {
        "message": f"Diffusion-resampled {n} particles ({integrator}, {'ODE' if ode else 'SDE'}, a={a}, T={T}, nsteps={nsteps}).",
        "reference": REFERENCE,
        "artifacts": [{"description": "resampled particles: 'samples' (N, ...) and 'log_weights' (N,) = -log N",
                       "path": str(out_path)}],
        "n_particles": n,
        "sample_shape": [int(s) for s in samples.shape[1:]],
        "input_weight_field": weight_field,
        "input_log_normaliser": log_normaliser,
        "ess_input": float(compute_ess(log_ws)),
        "ess_output": float(compute_ess(log_ws_out)),
        "settings": {"a": float(a), "T": float(T), "nsteps": int(nsteps), "integrator": integrator, "ode": bool(ode),
                     "jitter": float(jitter), "ts": "linspace(0, T, nsteps + 1)", "jit": True, "x64": True},
        "prng_key": [int(k) for k in np.asarray(key)],
    }


@resampling_mcp.tool()
def diffres_resample_particles_baseline(
    particles_path: Annotated[str, ".npz with 'samples' (N, ...) float ((N,) or (N, d) for ensemble_ot and gumbel_softmax) and exactly one of 'log_weights' (N,) or 'weights' (N,); weights are normalised before resampling; ensemble_ot and gumbel_softmax build N x N arrays, so keep N to a few thousand"],
    method: Annotated[Literal["multinomial", "stratified", "systematic", "multinomial_stopped", "ensemble_ot", "soft", "gumbel_softmax"], "Baseline resampler from diffres.resampling (soft = soft_resampling)"] = "multinomial",
    eps: Annotated[float | None, "ensemble_ot only: entropic regularisation > 0; None uses the upstream default 1/log(N)"] = None,
    alpha: Annotated[float | None, "soft only: softening parameter in [0, 1] (1 = multinomial); None uses 0.5, the experiments/gms/soft.py default (the paper's Gaussian-mixture table reports alpha = 0.9)"] = None,
    tau: Annotated[float | None, "gumbel_softmax only: temperature > 0 (-> 0 approaches multinomial); None uses 0.5, the experiments/gms/gumbel.py default (the paper's Gaussian-mixture table reports tau = 0.1)"] = None,
    seed: Annotated[int, "Seed for jax.random.PRNGKey(seed); ignored when prng_key is given"] = 0,
    prng_key: Annotated[list[int] | None, "Optional raw PRNG key (two uint32 values) used instead of seed, e.g. to reproduce a run with a split key"] = None,
    output_dir: Annotated[str | None, "Base output directory; a fresh unique subdirectory is created per call (default <project>/tmp/outputs/<tool>)"] = None,
) -> dict:
    """Resample a weighted particle set with one of the repository's baseline resamplers, for comparison with diffusion resampling.
    Input is an .npz of samples and (log) weights; output is an .npz of resampled particles and log weights (non-uniform for 'soft').
    """
    given = {"eps": eps, "alpha": alpha, "tau": tau}
    owner = {"eps": "ensemble_ot", "alpha": "soft", "tau": "gumbel_softmax"}
    wrong = [p for p, v in given.items() if v is not None and owner[p] != method]
    if wrong:
        raise ValueError(f"Parameter(s) {wrong} do not apply to method '{method}' "
                         f"({', '.join(f'{p} is for {owner[p]}' for p in wrong)}).")

    samples, log_ws, log_normaliser, weight_field = _load_particles(particles_path)
    n = int(samples.shape[0])
    key = _resolve_key(seed, prng_key)
    settings = {"method": method, "jit": True, "x64": True}
    fn = _BASELINES[method]
    kwargs = {}
    data = samples
    if method == "ensemble_ot":
        if eps is not None and not eps > 0:
            raise ValueError("eps must be positive.")
        if samples.ndim > 2:
            raise ValueError("ensemble_ot needs a point cloud: samples must have shape (N,) or (N, d).")
        if samples.ndim == 1:
            data = samples[:, None]  # ott PointCloud needs (N, d); reshaped back to (N,) afterwards
        kwargs["eps"] = eps
        settings["eps"] = float(eps) if eps is not None else float(1 / np.log(n))
        settings["eps_source"] = "user" if eps is not None else "upstream default 1/log(N)"
    elif method == "soft":
        alpha = 0.5 if alpha is None else alpha
        if not 0 <= alpha <= 1:
            raise ValueError("alpha must be in [0, 1].")
        kwargs["alpha"] = alpha
        settings["alpha"] = float(alpha)
    elif method == "gumbel_softmax":
        if samples.ndim > 2:
            # upstream computes softmax(...) @ samples, which fails for samples with more than two dimensions
            raise ValueError("gumbel_softmax needs samples of shape (N,) or (N, d).")
        tau = 0.5 if tau is None else tau
        if not tau > 0:
            raise ValueError("tau must be positive.")
        kwargs["tau"] = tau
        settings["tau"] = float(tau)

    # Called under jax.jit as in experiments/gms/{baselines,ot,soft,gumbel}.py.
    @jax.jit
    def resampling(key_, log_ws_, samples_):
        return fn(key_, log_ws_, samples_, **kwargs)

    log_ws_out, samples_out = resampling(key, log_ws, data)
    samples_out = samples_out.reshape(samples.shape)
    _check_finite_output(log_ws_out, samples_out, "Check the method parameters (e.g. eps for ensemble_ot).")
    out_path = _save("diffres_resample_particles_baseline", output_dir, log_ws_out, samples_out)
    uniform = method != "soft"
    return {
        "message": f"Resampled {n} particles with {method}.",
        "reference": REFERENCE,
        "artifacts": [{"description": "resampled particles: 'samples' (N, ...) and 'log_weights' (N,) as returned upstream "
                                      + ("(uniform -log N)" if uniform else "(normalised, non-uniform)"),
                       "path": str(out_path)}],
        "n_particles": n,
        "sample_shape": [int(s) for s in samples.shape[1:]],
        "input_weight_field": weight_field,
        "input_log_normaliser": log_normaliser,
        "ess_input": float(compute_ess(log_ws)),
        "ess_output": float(compute_ess(log_ws_out)),
        "output_weights_uniform": uniform,
        "settings": settings,
        "prng_key": [int(k) for k in np.asarray(key)],
    }
