"""Tools for linear Gaussian state-space models (LGSSMs) extracted from the diffres repository.

Upstream sources (zgbkdlm/diffres @ 767effe):
- diffres/gaussian_filters.py: `kf` (Kalman filter with exact negative log-likelihood) and `rts` (RTS smoother).
- diffres/tools.py: `simulate_lgssm` (simulation of a latent trajectory and observations).
- demos/gradient_variance2.py: reference workflow (simulate data, exact KF nll and its gradient w.r.t. model
  parameters, used as ground truth for particle-filter gradient estimates).
- tests/test_filters.py::test_kf: KF/RTS equal closed-form GP regression on an Ornstein-Uhlenbeck LGSSM.

LGSSM: x_0 ~ N(m0, P0), x_k = F x_{k-1} + N(0, Q), y_k = H x_k + N(0, R), k = 0..T (y_0 is observed).
"""
import json
import shutil
import uuid
from pathlib import Path
from typing import Annotated

import jax
import jax.numpy as jnp
import numpy as np
from fastmcp import FastMCP

from diffres.gaussian_filters import kf, rts
from diffres.tools import simulate_lgssm

# Upstream tests and experiments run in float64 on CPU.
jax.config.update("jax_enable_x64", True)

COMMIT = "767effe3e755067eb8a04422597fbf37eb8ab754"
REFERENCE = f"https://github.com/zgbkdlm/diffres/blob/{COMMIT}/diffres/gaussian_filters.py#L27-L54"
REFERENCE_SIMULATE = f"https://github.com/zgbkdlm/diffres/blob/{COMMIT}/diffres/tools.py#L363-L385"
DEFAULT_OUTPUT_BASE = Path(__file__).resolve().parents[2] / "tmp" / "outputs"
MODEL_KEYS = ("F", "Q", "H", "R", "m0", "P0")

gaussian_filters_mcp = FastMCP(name="gaussian_filters")


def _load_model(model_path: str) -> dict:
    """Read the LGSSM JSON (F, Q, H, R, m0, P0) and check shapes, finiteness and covariance symmetry."""
    path = Path(model_path)
    if not path.is_file():
        raise ValueError(f"model_path does not exist: {model_path}")
    try:
        spec = json.loads(path.read_text())
    except json.JSONDecodeError as exc:
        raise ValueError(f"model_path is not valid JSON: {exc}") from exc
    if not isinstance(spec, dict):
        raise ValueError("model JSON must be an object with keys F, Q, H, R, m0, P0")
    missing = [k for k in MODEL_KEYS if k not in spec]
    if missing:
        raise ValueError(f"model JSON is missing keys {missing}; required keys are {list(MODEL_KEYS)}")
    model = {}
    for k in MODEL_KEYS:
        try:
            model[k] = np.asarray(spec[k], dtype=np.float64)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"model entry {k} is not a numeric array: {exc}") from exc
        if not np.all(np.isfinite(model[k])):
            raise ValueError(f"model entry {k} contains non-finite values")
    F, Q, H, R, m0, P0 = (model[k] for k in MODEL_KEYS)
    if H.ndim != 2:
        raise ValueError(f"H must be a 2-D (dy, dx) matrix, got shape {H.shape}")
    dy, dx = H.shape
    expected = {"F": (dx, dx), "Q": (dx, dx), "R": (dy, dy), "m0": (dx,), "P0": (dx, dx)}
    for k, shape in expected.items():
        if model[k].shape != shape:
            raise ValueError(f"model entry {k} must have shape {shape} (dx={dx}, dy={dy} from H), "
                             f"got {model[k].shape}")
    for k in ("Q", "R", "P0"):
        if not np.allclose(model[k], model[k].T, rtol=1e-10, atol=1e-12):
            raise ValueError(f"covariance {k} must be symmetric: upstream uses it both directly (e.g. F P F^T + Q "
                             f"in kf) and through jnp.linalg.cholesky, which symmetrises its input, so a "
                             f"non-symmetric matrix would be interpreted inconsistently")
    model["dx"], model["dy"] = dx, dy
    return model


def _resolve_key(seed: int, prng_key: list[int] | None):
    if prng_key is None:
        return jax.random.PRNGKey(seed)
    if len(prng_key) != 2 or any((not isinstance(v, int)) or v < 0 or v >= 2 ** 32 for v in prng_key):
        raise ValueError("prng_key must be exactly two integers in [0, 2**32) (raw jax.random.PRNGKey data)")
    return jnp.asarray(np.asarray(prng_key, dtype=np.uint32))


def _fresh_dir(output_dir: str | None, tool: str) -> Path:
    base = Path(output_dir) if output_dir else DEFAULT_OUTPUT_BASE / tool
    out = base / uuid.uuid4().hex
    out.mkdir(parents=True, exist_ok=False)
    return out.resolve()


@gaussian_filters_mcp.tool()
def diffres_run_lgssm_kalman_filter(
    model_path: Annotated[str, "LGSSM JSON with keys F (dx,dx), Q (dx,dx), H (dy,dx), R (dy,dy), m0 (dx), P0 (dx,dx)"],
    observations_path: Annotated[str, ".npz with ys of shape (T+1, dy), ys[0] observed at time 0; (T+1,) allowed if dy=1"],
    smooth: Annotated[bool, "Also run the Rauch-Tung-Striebel smoother (diffres.gaussian_filters.rts)"] = False,
    compute_gradient: Annotated[bool, "Also compute the gradient of the KF nll w.r.t. the full matrices F and H (jax.grad)"] = False,
    output_dir: Annotated[str | None, "Base output directory; a fresh subdirectory is created per call"] = None,
) -> dict:
    """Run the exact Kalman filter (optionally RTS smoother and nll gradient w.r.t. F, H) on an LGSSM.
    Input is a model JSON and an observations .npz; output is the exact nll and an .npz of filter/smoother moments and gradients.
    """
    model = _load_model(model_path)
    dx, dy = model["dx"], model["dy"]
    obs_path = Path(observations_path)
    if not obs_path.is_file():
        raise ValueError(f"observations_path does not exist: {observations_path}")
    with np.load(obs_path) as data:
        if "ys" not in data.files:
            raise ValueError(f"observations .npz must contain 'ys'; found {data.files}")
        ys = np.asarray(data["ys"], dtype=np.float64)
    if ys.ndim == 1 and dy == 1:
        ys = ys[:, None]
    if ys.ndim != 2 or ys.shape[1] != dy or ys.shape[0] < 1:
        raise ValueError(f"ys must have shape (T+1, dy={dy}), got {ys.shape}")
    if not np.all(np.isfinite(ys)):
        raise ValueError("ys contains non-finite values")

    F, Q, H, R, m0, P0 = (jnp.asarray(model[k]) for k in MODEL_KEYS)
    ys_j = jnp.asarray(ys)

    if compute_gradient:
        # As in demos/gradient_variance2.py (loss_kf + jax.value_and_grad), in the general full-matrix form.
        def nll_fn(F_, H_):
            mfs_, vfs_, nll_, mps_, vps_ = kf(ys_j, m0, P0, F_, Q, H_, R)
            return nll_, (mfs_, vfs_, mps_, vps_)

        (nll, (mfs, vfs, mps, vps)), (grad_F, grad_H) = jax.value_and_grad(
            nll_fn, argnums=(0, 1), has_aux=True)(F, H)
    else:
        mfs, vfs, nll, mps, vps = kf(ys_j, m0, P0, F, Q, H, R)

    nll = float(nll)
    if not np.isfinite(nll):
        raise ValueError("Kalman filter nll is not finite: the innovation covariance H P H^T + R is not positive "
                         "definite (Cholesky failed) or the model is numerically degenerate")

    arrays = {"filtering_means": np.asarray(mfs), "filtering_covariances": np.asarray(vfs),
              "predictive_means": np.asarray(mps), "predictive_covariances": np.asarray(vps),
              "nll": np.asarray(nll)}
    result = {}
    if smooth:
        mss, vss = rts(mfs, vfs, mps, vps, F)
        arrays["smoothing_means"], arrays["smoothing_covariances"] = np.asarray(mss), np.asarray(vss)
        if not (np.all(np.isfinite(arrays["smoothing_means"])) and np.all(np.isfinite(arrays["smoothing_covariances"]))):
            raise ValueError("RTS smoother produced non-finite values: a predictive covariance F P F^T + Q is not "
                             "positive definite (Cholesky failed)")
    if compute_gradient:
        arrays["grad_F"], arrays["grad_H"] = np.asarray(grad_F), np.asarray(grad_H)
        if not (np.all(np.isfinite(arrays["grad_F"])) and np.all(np.isfinite(arrays["grad_H"]))):
            raise ValueError("gradient of the Kalman filter nll w.r.t. F, H is not finite")
        result["grad_F_frobenius_norm"] = float(np.linalg.norm(arrays["grad_F"]))
        result["grad_H_frobenius_norm"] = float(np.linalg.norm(arrays["grad_H"]))

    out_dir = _fresh_dir(output_dir, "diffres_run_lgssm_kalman_filter")
    npz_path = out_dir / "kalman_results.npz"
    np.savez(npz_path, **arrays)

    contents = "filtering_means (T+1,dx), filtering_covariances (T+1,dx,dx), predictive_means (T,dx), " \
               "predictive_covariances (T,dx,dx), nll ()"
    if smooth:
        contents += ", smoothing_means (T+1,dx), smoothing_covariances (T+1,dx,dx)"
    if compute_gradient:
        contents += ", grad_F (dx,dx), grad_H (dy,dx)"
    return {
        "message": f"Kalman filter on {ys.shape[0]} observations (dx={dx}, dy={dy}): nll={nll:.10g}"
                   + ("; RTS smoothing done" if smooth else "") + ("; gradient w.r.t. F, H done" if compute_gradient else ""),
        "reference": REFERENCE,
        "artifacts": [{"description": f"Kalman filter results: {contents}", "path": str(npz_path)}],
        "nll": nll,
        "log_likelihood": -nll,
        "num_observations": int(ys.shape[0]),
        "nsteps": int(ys.shape[0] - 1),
        "dx": int(dx),
        "dy": int(dy),
        "smooth": bool(smooth),
        "compute_gradient": bool(compute_gradient),
        **result,
    }


@gaussian_filters_mcp.tool()
def diffres_simulate_lgssm_data(
    model_path: Annotated[str, "LGSSM JSON with keys F (dx,dx), Q (dx,dx), H (dy,dx), R (dy,dy), m0 (dx), P0 (dx,dx)"],
    nsteps: Annotated[int, "Number of transitions T; T+1 states and observations (times 0..T) are returned"],
    seed: Annotated[int, "Seed for jax.random.PRNGKey(seed); ignored if prng_key is given"] = 0,
    prng_key: Annotated[list[int] | None, "Optional raw PRNGKey data (two uint32 values) used instead of seed"] = None,
    output_dir: Annotated[str | None, "Base output directory; a fresh subdirectory is created per call"] = None,
) -> dict:
    """Simulate a latent trajectory and observations from an LGSSM with diffres.tools.simulate_lgssm.
    Input is a model JSON, T and a seed/key; output is data.npz (xs (T+1,dx), ys (T+1,dy)) plus a model.json copy.
    """
    if isinstance(nsteps, bool) or not isinstance(nsteps, int) or nsteps < 0:
        raise ValueError(f"nsteps must be a non-negative integer, got {nsteps!r}")
    model = _load_model(model_path)
    key = _resolve_key(seed, prng_key)
    F, Q, H, R, m0, P0 = (jnp.asarray(model[k]) for k in MODEL_KEYS)

    xs, ys = simulate_lgssm(key, F, Q, H, R, m0, P0, nsteps)
    xs, ys = np.asarray(xs), np.asarray(ys)
    if not (np.all(np.isfinite(xs)) and np.all(np.isfinite(ys))):
        raise ValueError("simulation produced non-finite values: Q, R and P0 must be positive definite "
                         "(upstream uses their Cholesky factors)")

    out_dir = _fresh_dir(output_dir, "diffres_simulate_lgssm_data")
    data_path = out_dir / "data.npz"
    np.savez(data_path, xs=xs, ys=ys)
    model_copy = out_dir / "model.json"
    shutil.copyfile(model_path, model_copy)
    key_used = [int(v) for v in np.asarray(key, dtype=np.uint32).ravel()]
    return {
        "message": f"Simulated {nsteps} LGSSM steps (dx={model['dx']}, dy={model['dy']}) with PRNG key {key_used}",
        "reference": REFERENCE_SIMULATE,
        "artifacts": [{"description": "simulated latent states xs (T+1,dx) and observations ys (T+1,dy)",
                       "path": str(data_path)},
                      {"description": "copy of the LGSSM model JSON used for the simulation", "path": str(model_copy)}],
        "nsteps": int(nsteps),
        "dx": int(model["dx"]),
        "dy": int(model["dy"]),
        "xs_shape": list(xs.shape),
        "ys_shape": list(ys.shape),
        "prng_key_used": key_used,
        "seed": None if prng_key is not None else int(seed),
    }
