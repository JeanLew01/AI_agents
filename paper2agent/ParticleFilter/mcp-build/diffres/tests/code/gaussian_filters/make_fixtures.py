"""Write the gaussian_filters test fixtures (numpy only, no JAX) into tests/data/gaussian_filters/.

Sources: the executor references notebooks/lgssm_gradient_demo/data/reference_nsteps16_np8.npz
(demos/gradient_variance2.py at nsteps=16) and notebooks/filters_tests/data/filters_tests_inputs.npz
(tests/test_filters.py module-level OU model). The multivariate model is the verifier's own choice.
Run: diffres-env/bin/python tests/code/gaussian_filters/make_fixtures.py
"""
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "tests" / "data" / "gaussian_filters"
DEMO = ROOT / "notebooks" / "lgssm_gradient_demo" / "data" / "reference_nsteps16_np8.npz"
OU = ROOT / "notebooks" / "filters_tests" / "data" / "filters_tests_inputs.npz"
DEMO_SHA = "19de5274c7b2ee5f9c569ac4e26e04f3e528ed3c61c3812459e36aa4edfc5681"
OU_SHA = "c01efb288c0d0adc8eb53c7b8461b37e4e086e606c041f1ad2ac4ca0295328d7"


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def dump(name, spec):
    (OUT / name).write_text(json.dumps({k: np.asarray(v).tolist() if not isinstance(v, (str, float)) else v
                                        for k, v in spec.items()}, indent=1))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert sha(DEMO) == DEMO_SHA and sha(OU) == OU_SHA
    d = np.load(DEMO)
    true = dict(F=d["semigroup"], Q=d["trans_cov"], H=d["obs_op"], R=d["obs_cov"], m0=d["m0"], P0=d["v0"])
    dump("demo_model_true.json", true)
    # demos/gradient_variance2.py evaluation point theta=(0.2, 0.2): F = 0.2*I, H = 0.2*ones
    theta = dict(true, F=d["params"][0] * np.eye(1), H=d["params"][1] * np.ones((1, 1)))
    dump("demo_model_theta.json", theta)
    np.savez(OUT / "demo_ys.npz", ys=d["ys"], xs=d["xs"])

    o = np.load(OU)
    ou = dict(F=o["semigroup"], Q=o["trans_cov"], H=o["obs_op"], R=o["obs_cov"], m0=o["m0"], P0=o["v0"])
    dump("ou_model.json", ou)
    np.savez(OUT / "ou_ys_1d.npz", ys=o["ys"])
    np.savez(OUT / "ou_ys_2d.npz", ys=o["ys"][:, None])

    # Verifier's own non-diagonal model, dx=3, dy=2 (covariances exactly symmetric and PD)
    F = np.array([[0.9, 0.2, -0.1], [-0.15, 0.8, 0.05], [0.1, 0.0, 0.7]])
    A = np.array([[0.5, 0.1, 0.0], [0.2, 0.4, 0.1], [-0.1, 0.3, 0.6]])
    Q = A @ A.T + 0.05 * np.eye(3)
    Q = 0.5 * (Q + Q.T)
    H = np.array([[1.0, 0.5, 0.0], [0.0, -0.3, 1.2]])
    R = np.array([[0.4, 0.1], [0.1, 0.3]])
    m0 = np.array([0.5, -1.0, 0.2])
    P0 = np.array([[1.0, 0.3, 0.0], [0.3, 0.8, -0.2], [0.0, -0.2, 0.6]])
    mv = dict(F=F, Q=Q, H=H, R=R, m0=m0, P0=P0)
    dump("mv_model.json", mv)
    # Observations for the multivariate model are produced by a direct upstream simulate_lgssm call in the tests.

    # Invalid inputs
    dump("bad_missing_key.json", {k: v for k, v in true.items() if k != "R"})
    dump("bad_shape_Q.json", dict(mv, Q=np.eye(2)))
    asym = Q.copy(); asym[0, 1] += 0.05
    dump("bad_asym_Q.json", dict(mv, Q=asym))
    asym_p0 = P0.copy(); asym_p0[2, 0] = 0.1
    dump("bad_asym_P0.json", dict(mv, P0=asym_p0))
    dump("bad_nonpd_R.json", dict(true, R=-5.0 * np.eye(1)))      # KF innovation not PD; simulation Cholesky fails
    dump("bad_nonpd_Q.json", dict(true, Q=-1.0 * np.eye(1)))      # simulation Cholesky of Q fails
    dump("degenerate_F0_Q0.json", dict(true, F=np.zeros((1, 1)), Q=np.zeros((1, 1))))  # KF fine, RTS cho_factor(0) fails
    (OUT / "bad_nonfinite.json").write_text(json.dumps(
        {k: np.asarray(v).tolist() for k, v in true.items()} | {"F": [[float("nan")]]}))  # NaN literal
    (OUT / "bad_not_json.json").write_text("{F: [[0.5]], this is not JSON")
    np.savez(OUT / "bad_no_ys.npz", y=d["ys"])
    np.savez(OUT / "bad_ys_wrong_dy.npz", ys=np.concatenate([d["ys"], d["ys"]], axis=1))
    ys_nan = d["ys"].copy(); ys_nan[3, 0] = np.nan
    np.savez(OUT / "bad_ys_nonfinite.npz", ys=ys_nan)
    np.savez(OUT / "bad_ys_1d_for_dy2.npz", ys=np.linspace(-1.0, 1.0, 11))
    manifest = {p.name: sha(p) for p in sorted(OUT.iterdir()) if p.name != "MANIFEST.json"}
    (OUT / "MANIFEST.json").write_text(json.dumps(manifest, indent=1))
    print(json.dumps(manifest, indent=1))


if __name__ == "__main__":
    main()
