"""Independent verification of diffres_simulate_lgssm_data (src/tools/gaussian_filters.py).

Oracles: the executor reference notebooks/lgssm_gradient_demo/data/reference_nsteps16_np8.npz (demos/gradient_variance2.py,
nsteps=16, key = split(PRNGKey(666))[0]) and direct calls of diffres.tools.simulate_lgssm in this process.
The wrapper's output is never used as its own oracle. Fixtures: tests/data/gaussian_filters (make_fixtures.py).
"""
import hashlib
import json
import sys
from pathlib import Path

import jax
import jax.numpy as jnp
import numpy as np
import pytest
from fastmcp import Client
from fastmcp.exceptions import ToolError

from diffres.tools import simulate_lgssm

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
from tools.gaussian_filters import gaussian_filters_mcp  # noqa: E402  (same import path as src/diffres_mcp.py)

jax.config.update("jax_enable_x64", True)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "tests" / "data" / "gaussian_filters"
DEMO_REF = ROOT / "notebooks" / "lgssm_gradient_demo" / "data" / "reference_nsteps16_np8.npz"
DEMO_REF_SHA = "19de5274c7b2ee5f9c569ac4e26e04f3e528ed3c61c3812459e36aa4edfc5681"
TOOL = "diffres_simulate_lgssm_data"
KEYS = ("F", "Q", "H", "R", "m0", "P0")


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def model_arrays(path):
    spec = json.loads(Path(path).read_text())
    return [jnp.asarray(np.asarray(spec[k], dtype=np.float64)) for k in KEYS]


def upstream_sim(path, key, nsteps):
    F, Q, H, R, m0, P0 = model_arrays(path)
    xs, ys = simulate_lgssm(key, F, Q, H, R, m0, P0, nsteps)
    return np.asarray(xs), np.asarray(ys)


async def call(args):
    async with Client(gaussian_filters_mcp) as client:
        return (await client.call_tool(TOOL, args)).data


def load(res):
    p = Path(res["artifacts"][0]["path"])
    assert p.is_absolute() and p.name == "data.npz"
    with np.load(p) as d:
        assert sorted(d.files) == ["xs", "ys"]
        return np.asarray(d["xs"]), np.asarray(d["ys"])


def check_contract(res):
    assert set(res) >= {"message", "reference", "artifacts"}
    assert res["reference"].startswith("https://github.com/zgbkdlm/diffres/blob/767effe3e755067eb8a04422597fbf37eb8ab754/")
    assert len(res["artifacts"]) == 2
    for a in res["artifacts"]:
        assert set(a) == {"description", "path"} and Path(a["path"]).is_absolute() and Path(a["path"]).is_file()


async def test_schema_and_inventory():
    async with Client(gaussian_filters_mcp) as client:
        tools = {t.name: t for t in await client.list_tools()}
    assert set(tools) == {"diffres_run_lgssm_kalman_filter", TOOL}
    schema = tools[TOOL].input_schema
    assert set(schema["required"]) == {"model_path", "nsteps"}
    assert set(schema["properties"]) == {"model_path", "nsteps", "seed", "prng_key", "output_dir"}
    for name, prop in schema["properties"].items():
        assert prop.get("description"), name
    assert schema["properties"]["seed"]["default"] == 0


async def test_demo_reference_bitwise(tmp_path):
    """Executor reference: simulate_lgssm with the demo's split key, nsteps=16, true model."""
    assert sha(DEMO_REF) == DEMO_REF_SHA
    ref = np.load(DEMO_REF)
    key_sim = [int(v) for v in ref["key_simulation"]]
    assert key_sim == [2482698485, 3875352609]
    model = DATA / "demo_model_true.json"
    before = sha(model)
    res = await call({"model_path": str(model), "nsteps": 16, "prng_key": key_sim, "output_dir": str(tmp_path)})
    check_contract(res)
    xs, ys = load(res)
    np.testing.assert_array_equal(xs, ref["xs"])
    np.testing.assert_array_equal(ys, ref["ys"])
    assert xs.dtype == np.float64 and ys.dtype == np.float64
    assert res["prng_key_used"] == key_sim and res["seed"] is None
    assert res["xs_shape"] == [17, 1] and res["ys_shape"] == [17, 1]
    assert (res["nsteps"], res["dx"], res["dy"]) == (16, 1, 1)
    # model.json is a byte-identical copy; the input file is unchanged; outputs are inside output_dir
    copy = Path(res["artifacts"][1]["path"])
    assert copy.name == "model.json" and copy.read_bytes() == model.read_bytes()
    assert sha(model) == before
    assert Path(res["artifacts"][0]["path"]).parent.parent == tmp_path.resolve()
    # And the same key through a fresh direct upstream call
    dxs, dys = upstream_sim(model, jnp.asarray(np.asarray(key_sim, dtype=np.uint32)), 16)
    np.testing.assert_array_equal(xs, dxs)
    np.testing.assert_array_equal(ys, dys)


@pytest.mark.parametrize("seed", [0, 666, 12345])
async def test_seed_matches_direct_upstream(tmp_path, seed):
    res = await call({"model_path": str(DATA / "demo_model_true.json"), "nsteps": 16, "seed": seed,
                      "output_dir": str(tmp_path)})
    xs, ys = load(res)
    dxs, dys = upstream_sim(DATA / "demo_model_true.json", jax.random.PRNGKey(seed), 16)
    np.testing.assert_array_equal(xs, dxs)
    np.testing.assert_array_equal(ys, dys)
    assert res["prng_key_used"] == [int(v) for v in np.asarray(jax.random.PRNGKey(seed))]
    assert res["seed"] == seed


async def test_seed_default_is_zero(tmp_path):
    res = await call({"model_path": str(DATA / "demo_model_true.json"), "nsteps": 5, "output_dir": str(tmp_path)})
    assert res["prng_key_used"] == [0, 0] and res["seed"] == 0
    xs, ys = load(res)
    dxs, dys = upstream_sim(DATA / "demo_model_true.json", jax.random.PRNGKey(0), 5)
    np.testing.assert_array_equal(xs, dxs)
    np.testing.assert_array_equal(ys, dys)


@pytest.mark.parametrize("nsteps,seed", [(20, 7), (0, 3), (1, 11)])
async def test_multivariate_matches_direct_upstream(tmp_path, nsteps, seed):
    """Non-diagonal dx=3, dy=2 model (not from the tutorial), changed T and seed, including T=0."""
    res = await call({"model_path": str(DATA / "mv_model.json"), "nsteps": nsteps, "seed": seed,
                      "output_dir": str(tmp_path)})
    xs, ys = load(res)
    dxs, dys = upstream_sim(DATA / "mv_model.json", jax.random.PRNGKey(seed), nsteps)
    assert xs.shape == (nsteps + 1, 3) and ys.shape == (nsteps + 1, 2)
    np.testing.assert_array_equal(xs, dxs)
    np.testing.assert_array_equal(ys, dys)
    assert res["xs_shape"] == [nsteps + 1, 3] and res["ys_shape"] == [nsteps + 1, 2]
    assert (res["dx"], res["dy"], res["nsteps"]) == (3, 2, nsteps)


async def test_prng_key_overrides_seed(tmp_path):
    a = await call({"model_path": str(DATA / "mv_model.json"), "nsteps": 4, "seed": 5, "prng_key": [1, 2],
                    "output_dir": str(tmp_path)})
    b = await call({"model_path": str(DATA / "mv_model.json"), "nsteps": 4, "seed": 99, "prng_key": [1, 2],
                    "output_dir": str(tmp_path)})
    xa, ya = load(a)
    xb, yb = load(b)
    np.testing.assert_array_equal(xa, xb)
    np.testing.assert_array_equal(ya, yb)
    dxs, dys = upstream_sim(DATA / "mv_model.json", jnp.asarray(np.array([1, 2], dtype=np.uint32)), 4)
    np.testing.assert_array_equal(xa, dxs)
    np.testing.assert_array_equal(ya, dys)
    assert a["prng_key_used"] == [1, 2] and a["seed"] is None


async def test_repeated_calls_isolated(tmp_path):
    args = {"model_path": str(DATA / "demo_model_true.json"), "nsteps": 8, "seed": 1, "output_dir": str(tmp_path)}
    r1, r2 = await call(args), await call(args)
    p1 = {a["path"] for a in r1["artifacts"]}
    p2 = {a["path"] for a in r2["artifacts"]}
    assert not p1 & p2
    assert Path(r1["artifacts"][0]["path"]).parent != Path(r2["artifacts"][0]["path"]).parent
    x1, y1 = load(r1)
    x2, y2 = load(r2)
    np.testing.assert_array_equal(x1, x2)
    np.testing.assert_array_equal(y1, y2)
    r3 = await call(dict(args, seed=2))
    x3, _ = load(r3)
    assert not np.array_equal(x1, x3)
    # first call's files untouched by later calls
    assert all(Path(p).is_file() for p in p1)


async def test_default_output_dir_under_project_tmp():
    res = await call({"model_path": str(DATA / "demo_model_true.json"), "nsteps": 2})
    p = Path(res["artifacts"][0]["path"])
    assert p.parent.parent == (ROOT / "tmp" / "outputs" / TOOL).resolve()


def test_upstream_cholesky_symmetrises_rationale():
    """Rationale for the wrapper's symmetry check (not a wrapper call): jnp.linalg.cholesky symmetrises its input,
    so simulate_lgssm with an asymmetric Q behaves exactly as with (Q + Q^T)/2, whereas kf uses Q unsymmetrised in
    F P F^T + Q. An asymmetric 'covariance' would therefore be interpreted inconsistently by the two upstream
    functions; rejecting it is a justified input check (the reason is not 'only the lower triangle is read')."""
    F, Q, H, R, m0, P0 = model_arrays(DATA / "mv_model.json")
    Qa = Q.at[0, 1].add(0.05)
    key = jax.random.PRNGKey(4)
    xa, ya = simulate_lgssm(key, F, Qa, H, R, m0, P0, 6)
    xs, ys = simulate_lgssm(key, F, 0.5 * (Qa + Qa.T), H, R, m0, P0, 6)
    xl, yl = simulate_lgssm(key, F, jnp.tril(Qa) + jnp.tril(Qa, -1).T, H, R, m0, P0, 6)
    np.testing.assert_allclose(np.asarray(xa), np.asarray(xs), rtol=0, atol=1e-14)
    assert not np.allclose(np.asarray(xa), np.asarray(xl), rtol=0, atol=1e-6)


@pytest.mark.parametrize("model,nsteps,extra,fragment", [
    ("bad_missing_key.json", 4, {}, "missing keys"),
    ("bad_shape_Q.json", 4, {}, "must have shape"),
    ("bad_asym_Q.json", 4, {}, "must be symmetric"),
    ("bad_asym_P0.json", 4, {}, "must be symmetric"),
    ("bad_nonfinite.json", 4, {}, "non-finite"),
    ("bad_not_json.json", 4, {}, "not valid JSON"),
    ("does_not_exist.json", 4, {}, "does not exist"),
    ("bad_nonpd_Q.json", 4, {}, "positive definite"),
    ("bad_nonpd_R.json", 4, {}, "positive definite"),
    ("demo_model_true.json", -1, {}, "non-negative integer"),
    ("demo_model_true.json", 4, {"prng_key": [1, 2, 3]}, "prng_key"),
    ("demo_model_true.json", 4, {"prng_key": [1, 2 ** 32]}, "prng_key"),
    ("demo_model_true.json", 4, {"prng_key": [-1, 2]}, "prng_key"),
])
async def test_invalid_inputs_are_tool_errors(tmp_path, model, nsteps, extra, fragment):
    out = tmp_path / "out"
    with pytest.raises(ToolError, match=fragment):
        await call({"model_path": str(DATA / model), "nsteps": nsteps, "output_dir": str(out), **extra})
    assert not out.exists() or not any(out.iterdir())  # no partial artifacts


def test_nonpd_simulation_is_nan_upstream():
    """Justifies the post-call non-finite check: upstream returns NaN silently for non-PD Q."""
    F, Q, H, R, m0, P0 = model_arrays(DATA / "bad_nonpd_Q.json")
    xs, _ = simulate_lgssm(jax.random.PRNGKey(0), F, Q, H, R, m0, P0, 4)
    assert not np.all(np.isfinite(np.asarray(xs)))
