"""Build the resampling test fixtures in tests/data/resampling (numpy only, deterministic, no JAX).

Reference inputs are copied from the executors' saved upstream inputs (notebooks/<id>/data); synthetic inputs use
numpy with fixed seeds. Run: diffres-env/bin/python tests/code/resampling/resampling_fixtures.py
"""
import hashlib
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
NB = ROOT / "notebooks"
DATA = ROOT / "tests" / "data" / "resampling"


def build() -> dict:
    DATA.mkdir(parents=True, exist_ok=True)
    out = {}

    def save(name, **arrays):
        p = DATA / name
        np.savez(p, **arrays)
        out[name] = hashlib.sha256(p.read_bytes()).hexdigest()

    gm = np.load(NB / "gaussian_mixture_demo/data/inputs_resampling.npz")
    save("gm_demo_particles.npz", samples=gm["prior_samples"], log_weights=gm["log_ws"])
    gms = np.load(NB / "gms_diffusion_experiment/data/inputs_A_jk_ode_T3_K128.npz")
    save("gms_particles.npz", samples=gms["samples"], log_weights=gms["log_ws"])
    save("gms_particles_weights.npz", samples=gms["samples"], weights=np.exp(gms["log_ws"]))

    # Same construction as tests/test_resampling.py (uniform on [-2, 2], log w = log N(0; x, 1)), numpy RNG, N=400,
    # 1-D samples (N,), log weights deliberately left unnormalised (+7.5 offset).
    rng = np.random.default_rng(666)
    x = rng.uniform(-2.0, 2.0, size=400)
    lw = -0.5 * x ** 2 - 0.5 * np.log(2 * np.pi) + 7.5
    save("toy1d_unnormalised.npz", samples=x, log_weights=lw)
    save("toy2d_unnormalised.npz", samples=x.reshape(200, 2), log_weights=lw[:200] - 3.0)

    s300, l300 = gms["samples"][:300], gms["log_ws"][:300].copy()
    l300[::3] = -np.inf
    save("gms300_neginf.npz", samples=s300, log_weights=l300)
    zv = gms["samples"][:200].copy()
    zv[:, 2] = 1.0
    save("gms200_zero_variance_dim.npz", samples=zv, log_weights=gms["log_ws"][:200])
    save("gms50_3d_samples.npz", samples=gms["samples"][:50].reshape(50, 2, 4), log_weights=gms["log_ws"][:50])

    # Invalid inputs
    save("invalid_no_samples.npz", particles=gms["samples"][:10], log_weights=gms["log_ws"][:10])
    save("invalid_both_fields.npz", samples=gms["samples"][:10], log_weights=gms["log_ws"][:10],
         weights=np.exp(gms["log_ws"][:10]))
    save("invalid_no_weights.npz", samples=gms["samples"][:10])
    bad = gms["log_ws"][:10].copy()
    bad[3] = np.nan
    save("invalid_nan_log_weights.npz", samples=gms["samples"][:10], log_weights=bad)
    save("invalid_all_neginf.npz", samples=gms["samples"][:10], log_weights=np.full(10, -np.inf))
    save("invalid_shape_mismatch.npz", samples=gms["samples"][:10], log_weights=gms["log_ws"][:9])
    save("invalid_single_particle.npz", samples=gms["samples"][:1], log_weights=np.zeros(1))
    w = np.exp(gms["log_ws"][:10])
    w[0] = -0.1
    save("invalid_negative_weights.npz", samples=gms["samples"][:10], weights=w)
    sm = gms["samples"][:10].copy()
    sm[1, 1] = np.inf
    save("invalid_nonfinite_samples.npz", samples=sm, log_weights=gms["log_ws"][:10])
    (DATA / "invalid_not_npz.txt").write_text("not an npz file\n")
    out["invalid_not_npz.txt"] = hashlib.sha256((DATA / "invalid_not_npz.txt").read_bytes()).hexdigest()

    meta = {
        "built_by": "tests/code/resampling/resampling_fixtures.py",
        "sources": {
            "gm_demo_particles.npz": "notebooks/gaussian_mixture_demo/data/inputs_resampling.npz (prior_samples, log_ws; "
                                     "resampling key [700162660, 1620510799])",
            "gms_particles.npz": "notebooks/gms_diffusion_experiment/data/inputs_A_jk_ode_T3_K128.npz (samples, log_ws; "
                                 "identical in the baselines/soft/gumbel captures; resampling key [1100985983, 1476939598])",
        },
        "sha256": out,
    }
    (DATA / "fixtures_manifest.json").write_text(json.dumps(meta, indent=1))
    return out


if __name__ == "__main__":
    print(json.dumps(build(), indent=1))
