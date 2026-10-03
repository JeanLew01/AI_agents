"""Build the input fixtures of tests/data/feynman_kac (verifier-owned; not collected by pytest).

Executor-derived fixtures copy the exact float64 inputs saved by the executors (filters_tests,
lgssm_diffusion_experiment, lgssm_gradient_demo). Synthetic multi-dimensional observations are produced by a direct
upstream call to diffres.tools.simulate_lgssm. Run once through heavy.sh:
  heavy.sh --limit-mb 1000 -- diffres-env/bin/python tests/code/feynman_kac/make_fixtures.py
"""
import json
from pathlib import Path

import jax
import jax.numpy as jnp
import numpy as np

from diffres.tools import simulate_lgssm

jax.config.update("jax_enable_x64", True)

ROOT = Path(__file__).resolve().parents[3]
NB = ROOT / "notebooks"
DATA = ROOT / "tests" / "data" / "feynman_kac"
DATA.mkdir(parents=True, exist_ok=True)


def write_model(name, F, Q, H, R, m0, P0):
    spec = {k: np.asarray(v, dtype=np.float64).tolist() for k, v in
            (("F", F), ("Q", Q), ("H", H), ("R", R), ("m0", m0), ("P0", P0))}
    (DATA / f"{name}_model.json").write_text(json.dumps(spec, indent=1))
    back = json.loads((DATA / f"{name}_model.json").read_text())
    for k, v in spec.items():  # JSON float repr round-trips float64 exactly
        assert np.array_equal(np.asarray(back[k]), np.asarray(v)), k


def write_ys(name, ys, **extra):
    np.savez(DATA / f"{name}.npz", ys=np.asarray(ys), **extra)


# 1. tests/test_filters.py model and observations (executor filters_tests).
ft = np.load(NB / "filters_tests/data/filters_tests_inputs.npz")
write_model("filters", ft["semigroup"], ft["trans_cov"], ft["obs_op"], ft["obs_cov"], ft["m0"], ft["v0"])
write_ys("filters_ys_1d", ft["ys"])             # (101,) exactly as the upstream test passes it
write_ys("filters_ys_2d", ft["ys"][:, None])    # (101, 1) shared contract

# 2. experiments/lgssm model at the true parameters (executor lgssm_diffusion_experiment).
ld = np.load(NB / "lgssm_diffusion_experiment/data/inputs.npz")
write_model("lgssm", ld["semigroup"], ld["trans_cov"], ld["obs_op"], ld["obs_cov"], ld["m0"], ld["v0"])
write_ys("lgssm_ys", ld["ys"])

# 3. demos/gradient_variance2.py: PF evaluated at params (0.2, 0.2) -> F = 0.2 I, H = 0.2 ones.
gd = np.load(NB / "lgssm_gradient_demo/data/reference_nsteps16_np8.npz")
p = gd["params"]
write_model("graddemo", p[0] * np.eye(1), gd["trans_cov"], p[1] * np.ones((1, 1)), gd["obs_cov"], gd["m0"], gd["v0"])
write_ys("graddemo_ys", gd["ys"])

# 4. Synthetic 2-D models (not from upstream; observations by a direct upstream simulate_lgssm call).
F2 = np.array([[0.9, 0.1], [-0.2, 0.8]])
full = dict(F=F2, Q=np.array([[0.5, 0.2], [0.2, 0.3]]),
            H=np.array([[1.0, 0.5], [0.0, 1.0], [0.3, -0.4]]),
            R=np.array([[0.4, 0.1, 0.05], [0.1, 0.3, 0.0], [0.05, 0.0, 0.5]]),
            m0=np.array([0.1, -0.2]), P0=np.array([[1.0, 0.3], [0.3, 0.8]]))
write_model("full2d", **full)
xs, ys = simulate_lgssm(jax.random.PRNGKey(2024), *(jnp.asarray(full[k]) for k in ("F", "Q", "H", "R", "m0", "P0")), 12)
write_ys("full2d_ys", ys, xs=np.asarray(xs))

diag = dict(F=F2, Q=np.array([[0.5, 0.2], [0.2, 0.3]]), H=np.array([[1.0, 0.5], [0.0, 1.0]]),
            R=np.diag([0.4, 0.2]), m0=np.array([0.1, -0.2]), P0=np.array([[1.0, 0.3], [0.3, 0.8]]))
write_model("diagR2d", **diag)
xs, ys = simulate_lgssm(jax.random.PRNGKey(7), *(jnp.asarray(diag[k]) for k in ("F", "Q", "H", "R", "m0", "P0")), 12)
write_ys("diagR2d_ys", ys, xs=np.asarray(xs))
# Same model with a negligible off-diagonal entry in R: switches the wrapper to its full-R branch.
tiny = dict(diag, R=np.array([[0.4, 1e-300], [1e-300, 0.2]]))
write_model("diagR2d_tinyoffdiag", **tiny)

# Diagonal Q in 2-D (the upstream test's elementwise trans_cov ** 0.5 equals chol(Q) only here).
diagq = dict(F=F2, Q=np.diag([0.5, 0.3]), H=np.array([[1.0, 0.5]]), R=np.array([[0.4]]),
             m0=np.array([0.1, -0.2]), P0=np.diag([1.0, 0.8]))
write_model("diagQ2d", **diagq)
xs, ys = simulate_lgssm(jax.random.PRNGKey(11), *(jnp.asarray(diagq[k]) for k in ("F", "Q", "H", "R", "m0", "P0")), 12)
write_ys("diagQ2d_ys", ys, xs=np.asarray(xs))

# H = 0: every particle has the same potential, so the PF likelihood is exact (offset property test).
write_model("zeroH", ld["semigroup"], ld["trans_cov"], np.zeros((1, 1)), ld["obs_cov"], ld["m0"], ld["v0"])

# Single observation (T = 0).
write_ys("lgssm_ys_T0", ld["ys"][:1])

# Invalid inputs.
bad = json.loads((DATA / "lgssm_model.json").read_text())
(DATA / "bad_missing_R_model.json").write_text(json.dumps({k: v for k, v in bad.items() if k != "R"}))
(DATA / "bad_R_not_pd_model.json").write_text(json.dumps(dict(bad, R=[[-0.5]])))
(DATA / "bad_Q_asym_model.json").write_text(json.dumps(dict(json.loads((DATA / "full2d_model.json").read_text()),
                                                             Q=[[0.5, 0.2], [0.1, 0.3]])))
(DATA / "bad_H_shape_model.json").write_text(json.dumps(dict(bad, H=[[1.0, 2.0]])))
write_ys("bad_ys_nonfinite", np.where(np.arange(33)[:, None] == 5, np.nan, ld["ys"]))
write_ys("bad_ys_wrong_dy", np.concatenate([ld["ys"], ld["ys"]], axis=1))
np.savez(DATA / "bad_no_ys.npz", observations=ld["ys"])
print(sorted(p.name for p in DATA.iterdir()))
