"""Independent verification of diffres_run_lgssm_kalman_filter (src/tools/gaussian_filters.py).

Oracles (never the wrapper's own output):
- executor lgssm_gradient_demo: notebooks/lgssm_gradient_demo/data/reference_nsteps16_np8.npz (demos/gradient_variance2.py
  at nsteps=16: loss_true, grad_true w.r.t. theta, kf/rts outputs at theta=(0.2,0.2) and at the true parameters,
  matrix-form dF/dH);
- executor filters_tests: notebooks/filters_tests/{data/filters_tests_inputs.npz, outputs/capture_outputs.npz}
  (tests/test_filters.py OU model, closed-form GP regression reference);
- direct calls of diffres.gaussian_filters.kf / rts and jax.grad in this process, plus finite differences.
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

from diffres.gaussian_filters import kf, rts
from diffres.tools import simulate_lgssm

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "src"))
from tools.gaussian_filters import gaussian_filters_mcp  # noqa: E402  (same import path as src/diffres_mcp.py)

jax.config.update("jax_enable_x64", True)

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "tests" / "data" / "gaussian_filters"
DEMO_REF = ROOT / "notebooks" / "lgssm_gradient_demo" / "data" / "reference_nsteps16_np8.npz"
OU_IN = ROOT / "notebooks" / "filters_tests" / "data" / "filters_tests_inputs.npz"
OU_OUT = ROOT / "notebooks" / "filters_tests" / "outputs" / "capture_outputs.npz"
SHAS = {DEMO_REF: "19de5274c7b2ee5f9c569ac4e26e04f3e528ed3c61c3812459e36aa4edfc5681",
        OU_IN: "c01efb288c0d0adc8eb53c7b8461b37e4e086e606c041f1ad2ac4ca0295328d7",
        OU_OUT: "bae460b4aa2aa2a9fef51d5013b8b06c399b2f500d7458211501424865b8e983"}
TOOL = "diffres_run_lgssm_kalman_filter"
KEYS = ("F", "Q", "H", "R", "m0", "P0")
BASE = ["filtering_covariances", "filtering_means", "nll", "predictive_covariances", "predictive_means"]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def model_arrays(path):
    spec = json.loads(Path(path).read_text())
    return [jnp.asarray(np.asarray(spec[k], dtype=np.float64)) for k in KEYS]


def upstream_kf(model_path, ys):
    F, Q, H, R, m0, P0 = model_arrays(model_path)
    return kf(jnp.asarray(ys), m0, P0, F, Q, H, R)


async def call(args):
    async with Client(gaussian_filters_mcp) as client:
        return (await client.call_tool(TOOL, args)).data


def load(res):
    assert len(res["artifacts"]) == 1
    a = res["artifacts"][0]
    p = Path(a["path"])
    assert set(a) == {"description", "path"} and p.is_absolute() and p.name == "kalman_results.npz"
    with np.load(p) as d:
        return {k: np.asarray(d[k]) for k in d.files}


@pytest.fixture(scope="module", autouse=True)
def _references_intact():
    for p, h in SHAS.items():
        assert sha(p) == h, p


async def test_schema():
    async with Client(gaussian_filters_mcp) as client:
        tools = {t.name: t for t in await client.list_tools()}
    schema = tools[TOOL].input_schema
    assert set(schema["required"]) == {"model_path", "observations_path"}
    assert set(schema["properties"]) == {"model_path", "observations_path", "smooth", "compute_gradient", "output_dir"}
    for name, prop in schema["properties"].items():
        assert prop.get("description"), name
    assert schema["properties"]["smooth"]["default"] is False
    assert schema["properties"]["compute_gradient"]["default"] is False


async def test_demo_theta_nll_gradient_kf_rts_bitwise(tmp_path):
    """demos/gradient_variance2.py at theta=(0.2,0.2): nll=loss_true, dF/dH, chain rule to grad_true, kf/rts arrays."""
    ref = np.load(DEMO_REF)
    model, obs = DATA / "demo_model_theta.json", DATA / "demo_ys.npz"
    before = (sha(model), sha(obs))
    res = await call({"model_path": str(model), "observations_path": str(obs), "smooth": True,
                      "compute_gradient": True, "output_dir": str(tmp_path)})
    assert set(res) >= {"message", "reference", "artifacts"}
    assert res["reference"].startswith("https://github.com/zgbkdlm/diffres/blob/767effe3e755067eb8a04422597fbf37eb8ab754/")
    out = load(res)
    assert sorted(out) == sorted(BASE + ["smoothing_means", "smoothing_covariances", "grad_F", "grad_H"])
    assert res["nll"] == float(ref["loss_true"]) == 34.829210096507474
    assert res["log_likelihood"] == -res["nll"]
    assert float(out["nll"]) == res["nll"]
    np.testing.assert_array_equal(out["grad_F"], ref["kf_theta_dF"])
    np.testing.assert_array_equal(out["grad_H"], ref["kf_theta_dH"])
    # chain rule: theta0 scales F = theta0*I, theta1 scales H = theta1*ones
    assert float(np.sum(out["grad_F"] * np.eye(1))) == float(ref["grad_true"][0])
    assert float(np.sum(out["grad_H"] * np.ones((1, 1)))) == float(ref["grad_true"][1])
    for mine, theirs in [("filtering_means", "kf_theta_mfs"), ("filtering_covariances", "kf_theta_vfs"),
                         ("predictive_means", "kf_theta_mps"), ("predictive_covariances", "kf_theta_vps"),
                         ("smoothing_means", "rts_theta_mss"), ("smoothing_covariances", "rts_theta_vss")]:
        np.testing.assert_array_equal(out[mine], ref[theirs], err_msg=mine)
    assert out["filtering_means"].shape == (17, 1) and out["predictive_covariances"].shape == (16, 1, 1)
    np.testing.assert_allclose([res["grad_F_frobenius_norm"], res["grad_H_frobenius_norm"]],
                               np.abs(ref["grad_true"]), rtol=1e-15, atol=0)
    assert (res["num_observations"], res["nsteps"], res["dx"], res["dy"]) == (17, 16, 1, 1)
    assert res["smooth"] is True and res["compute_gradient"] is True
    assert (sha(model), sha(obs)) == before


async def test_demo_scalar_parametrisation_direct(tmp_path):
    """Recompute the demo's own scalar-parameter loss/gradient directly (gradient_variance2.py `kf(params, ys)`),
    independently of the executor capture, and compare with the wrapper's matrix gradient via the chain rule."""
    ref = np.load(DEMO_REF)
    _, Q, _, R, m0, P0 = model_arrays(DATA / "demo_model_true.json")
    ys = jnp.asarray(ref["ys"])

    def loss(params):
        return kf(ys, m0, P0, params[0] * jnp.eye(1), Q, params[1] * jnp.ones((1, 1)), R)[2]

    val, g = jax.value_and_grad(loss)(jnp.array([0.2, 0.2]))
    res = await call({"model_path": str(DATA / "demo_model_theta.json"),
                      "observations_path": str(DATA / "demo_ys.npz"), "compute_gradient": True,
                      "output_dir": str(tmp_path)})
    out = load(res)
    assert res["nll"] == float(val)
    np.testing.assert_allclose([np.trace(out["grad_F"]), out["grad_H"].sum()], np.asarray(g), rtol=1e-12, atol=0)
    assert "smoothing_means" not in out


async def test_demo_true_parameters_no_options(tmp_path):
    ref = np.load(DEMO_REF)
    res = await call({"model_path": str(DATA / "demo_model_true.json"),
                      "observations_path": str(DATA / "demo_ys.npz"), "output_dir": str(tmp_path)})
    out = load(res)
    assert sorted(out) == sorted(BASE)
    assert res["nll"] == float(ref["kf_true_nll"]) == 29.828975391167102
    for mine, theirs in [("filtering_means", "kf_true_mfs"), ("filtering_covariances", "kf_true_vfs"),
                         ("predictive_means", "kf_true_mps"), ("predictive_covariances", "kf_true_vps")]:
        np.testing.assert_array_equal(out[mine], ref[theirs], err_msg=mine)
    assert "grad_F_frobenius_norm" not in res and res["smooth"] is False and res["compute_gradient"] is False


@pytest.mark.parametrize("obs", ["ou_ys_1d.npz", "ou_ys_2d.npz"])
async def test_filters_tests_ou_model_and_gp_reference(tmp_path, obs):
    """tests/test_filters.py::test_kf: KF/RTS on the OU LGSSM equal closed-form GP regression (assert_allclose
    default rtol=1e-7); kf/rts outputs bitwise equal to the executor capture. The test passes 1-D ys (dy=1)."""
    cap, inp = np.load(OU_OUT), np.load(OU_IN)
    res = await call({"model_path": str(DATA / "ou_model.json"), "observations_path": str(DATA / obs),
                      "smooth": True, "output_dir": str(tmp_path)})
    out = load(res)
    assert res["nll"] == float(cap["kf/nll"]) == 141.42165070795778
    for mine, theirs in [("filtering_means", "kf/mfs"), ("filtering_covariances", "kf/vfs"),
                         ("predictive_means", "kf/mps"), ("predictive_covariances", "kf/vps"),
                         ("smoothing_means", "kf/mss"), ("smoothing_covariances", "kf/vss")]:
        np.testing.assert_array_equal(out[mine], cap[theirs], err_msg=mine)
    np.testing.assert_allclose(out["smoothing_means"][:, 0], inp["gp_mean"], rtol=1e-7)
    np.testing.assert_allclose(out["smoothing_covariances"][:, 0, 0], inp["gp_var"], rtol=1e-7)
    np.testing.assert_allclose(res["nll"], float(inp["gp_nll"]), rtol=1e-7)
    assert (res["num_observations"], res["dx"], res["dy"]) == (101, 1, 1)


def _mv_observations(tmp_path, seed=7, nsteps=20):
    """Observations for the dx=3, dy=2 model from a direct upstream simulate_lgssm call (not the wrapper)."""
    F, Q, H, R, m0, P0 = model_arrays(DATA / "mv_model.json")
    _, ys = simulate_lgssm(jax.random.PRNGKey(seed), F, Q, H, R, m0, P0, nsteps)
    p = tmp_path / f"mv_ys_seed{seed}_T{nsteps}.npz"
    np.savez(p, ys=np.asarray(ys))
    return p, np.asarray(ys)


@pytest.mark.parametrize("seed,nsteps", [(7, 20), (1, 0), (2, 1)])
async def test_multivariate_all_outputs_vs_direct_upstream(tmp_path, seed, nsteps):
    obs, ys = _mv_observations(tmp_path, seed, nsteps)
    res = await call({"model_path": str(DATA / "mv_model.json"), "observations_path": str(obs), "smooth": True,
                      "compute_gradient": True, "output_dir": str(tmp_path / "out")})
    out = load(res)
    F, Q, H, R, m0, P0 = model_arrays(DATA / "mv_model.json")
    mfs, vfs, nll, mps, vps = kf(jnp.asarray(ys), m0, P0, F, Q, H, R)
    mss, vss = rts(mfs, vfs, mps, vps, F)
    gF, gH = jax.grad(lambda F_, H_: kf(jnp.asarray(ys), m0, P0, F_, Q, H_, R)[2], argnums=(0, 1))(F, H)
    expected = {"filtering_means": mfs, "filtering_covariances": vfs, "predictive_means": mps,
                "predictive_covariances": vps, "smoothing_means": mss, "smoothing_covariances": vss,
                "grad_F": gF, "grad_H": gH}
    for k, v in expected.items():
        np.testing.assert_allclose(out[k], np.asarray(v), rtol=1e-12, atol=1e-13, err_msg=k)
    np.testing.assert_allclose(res["nll"], float(nll), rtol=1e-13, atol=0)
    assert out["grad_F"].shape == (3, 3) and out["grad_H"].shape == (2, 3)
    assert out["filtering_means"].shape == (nsteps + 1, 3) and out["predictive_means"].shape == (nsteps, 3)
    np.testing.assert_allclose(res["grad_F_frobenius_norm"], np.linalg.norm(np.asarray(gF)), rtol=1e-12)
    np.testing.assert_allclose(res["grad_H_frobenius_norm"], np.linalg.norm(np.asarray(gH)), rtol=1e-12)
    assert (res["dx"], res["dy"], res["nsteps"]) == (3, 2, nsteps)


async def test_options_do_not_change_forward_outputs(tmp_path):
    """Gradient path (value_and_grad with aux) must leave the filter outputs unchanged (bitwise)."""
    obs, ys = _mv_observations(tmp_path)
    base = load(await call({"model_path": str(DATA / "mv_model.json"), "observations_path": str(obs),
                            "output_dir": str(tmp_path / "a")}))
    full = load(await call({"model_path": str(DATA / "mv_model.json"), "observations_path": str(obs),
                            "smooth": True, "compute_gradient": True, "output_dir": str(tmp_path / "b")}))
    for k in BASE:
        np.testing.assert_array_equal(base[k], full[k], err_msg=k)
    mfs, vfs, nll, mps, vps = upstream_kf(DATA / "mv_model.json", ys)
    assert float(base["nll"]) == float(nll)
    np.testing.assert_array_equal(base["filtering_covariances"], np.asarray(vfs))


async def test_gradient_finite_differences_and_chain_rule(tmp_path):
    """Independent property checks of the full-matrix gradient on the non-diagonal model:
    central finite differences of the direct upstream nll, and the chain rule for scalar scalings of F and H
    (the demo's parametrisation generalised: d/dtheta0 nll(theta0*F, H) = sum(grad_F * F))."""
    obs, ys = _mv_observations(tmp_path)
    out = load(await call({"model_path": str(DATA / "mv_model.json"), "observations_path": str(obs),
                           "compute_gradient": True, "output_dir": str(tmp_path / "o")}))
    F, Q, H, R, m0, P0 = model_arrays(DATA / "mv_model.json")
    yj = jnp.asarray(ys)

    def nll(F_, H_):
        return float(kf(yj, m0, P0, F_, Q, H_, R)[2])

    h = 1e-6
    fdF = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            E = jnp.zeros((3, 3)).at[i, j].set(h)
            fdF[i, j] = (nll(F + E, H) - nll(F - E, H)) / (2 * h)
    fdH = np.zeros((2, 3))
    for i in range(2):
        for j in range(3):
            E = jnp.zeros((2, 3)).at[i, j].set(h)
            fdH[i, j] = (nll(F, H + E) - nll(F, H - E)) / (2 * h)
    np.testing.assert_allclose(out["grad_F"], fdF, rtol=1e-5, atol=1e-6)
    np.testing.assert_allclose(out["grad_H"], fdH, rtol=1e-5, atol=1e-6)

    g = jax.grad(lambda th: kf(yj, m0, P0, th[0] * F, Q, th[1] * H, R)[2])(jnp.array([1.0, 1.0]))
    np.testing.assert_allclose([np.sum(out["grad_F"] * np.asarray(F)), np.sum(out["grad_H"] * np.asarray(H))],
                               np.asarray(g), rtol=1e-10)


async def test_composition_direct_upstream_simulation(tmp_path):
    """Composition with inputs built by a direct upstream simulate_lgssm call (demo key, true model)."""
    ref = np.load(DEMO_REF)
    F, Q, H, R, m0, P0 = model_arrays(DATA / "demo_model_true.json")
    _, ys = simulate_lgssm(jnp.asarray(ref["key_simulation"]), F, Q, H, R, m0, P0, 16)
    p = tmp_path / "direct.npz"
    np.savez(p, ys=np.asarray(ys))
    res = await call({"model_path": str(DATA / "demo_model_true.json"), "observations_path": str(p),
                      "output_dir": str(tmp_path / "o")})
    assert res["nll"] == float(ref["kf_true_nll"])


async def test_composition_via_simulate_tool_labelled(tmp_path):
    """LABELLED cross-tool composition: diffres_simulate_lgssm_data (through its own Client) -> this tool,
    using the simulate tool's data.npz and model.json copy. Expected from direct upstream calls."""
    async with Client(gaussian_filters_mcp) as client:
        sim = (await client.call_tool("diffres_simulate_lgssm_data",
                                      {"model_path": str(DATA / "mv_model.json"), "nsteps": 12, "seed": 21,
                                       "output_dir": str(tmp_path / "sim")})).data
        data_npz, model_json = (a["path"] for a in sim["artifacts"])
        res = (await client.call_tool(TOOL, {"model_path": model_json, "observations_path": data_npz,
                                             "smooth": True, "output_dir": str(tmp_path / "kf")})).data
    F, Q, H, R, m0, P0 = model_arrays(DATA / "mv_model.json")
    _, ys = simulate_lgssm(jax.random.PRNGKey(21), F, Q, H, R, m0, P0, 12)
    mfs, vfs, nll, mps, vps = kf(ys, m0, P0, F, Q, H, R)
    mss, _ = rts(mfs, vfs, mps, vps, F)
    out = load(res)
    assert res["nll"] == float(nll)
    np.testing.assert_array_equal(out["smoothing_means"], np.asarray(mss))


async def test_repeated_calls_isolated(tmp_path):
    args = {"model_path": str(DATA / "demo_model_theta.json"), "observations_path": str(DATA / "demo_ys.npz"),
            "compute_gradient": True, "output_dir": str(tmp_path)}
    r1, r2 = await call(args), await call(args)
    p1, p2 = Path(r1["artifacts"][0]["path"]), Path(r2["artifacts"][0]["path"])
    assert p1 != p2 and p1.parent != p2.parent and p1.parent.parent == p2.parent.parent == tmp_path.resolve()
    a, b = load(r1), load(r2)
    for k in a:
        np.testing.assert_array_equal(a[k], b[k])
    assert r1["nll"] == r2["nll"] and p1.is_file()


async def test_default_output_dir_under_project_tmp():
    res = await call({"model_path": str(DATA / "demo_model_true.json"),
                      "observations_path": str(DATA / "demo_ys.npz")})
    assert Path(res["artifacts"][0]["path"]).parent.parent == (ROOT / "tmp" / "outputs" / TOOL).resolve()


def test_rationale_upstream_silent_failures():
    """Why the wrapper's post-call checks exist: upstream returns NaN silently (no exception) for a non-PD
    innovation covariance (kf) and for a singular predictive covariance (rts); and 1-D ys with dy>1 would be
    silently broadcast by kf_update (y - H m is (dy,)), so 1-D ys is only meaningful for dy=1."""
    F, Q, H, R, m0, P0 = model_arrays(DATA / "bad_nonpd_R.json")
    ys = np.load(DATA / "demo_ys.npz")["ys"]
    assert not np.isfinite(float(kf(jnp.asarray(ys), m0, P0, F, Q, H, R)[2]))
    F, Q, H, R, m0, P0 = model_arrays(DATA / "degenerate_F0_Q0.json")
    mfs, vfs, nll, mps, vps = kf(jnp.asarray(ys), m0, P0, F, Q, H, R)
    assert np.isfinite(float(nll))
    mss, vss = rts(mfs, vfs, mps, vps, F)
    assert not np.all(np.isfinite(np.asarray(mss)))
    F, Q, H, R, m0, P0 = model_arrays(DATA / "mv_model.json")
    y1 = jnp.asarray(np.load(DATA / "bad_ys_1d_for_dy2.npz")["ys"])
    out = kf(y1, m0, P0, F, Q, H, R)  # runs without error: the scalar is broadcast to both components
    assert np.isfinite(float(out[2]))


async def test_degenerate_model_kf_ok_but_smoother_error(tmp_path):
    """F=0, Q=0: the filter is well defined (wrapper must succeed without smoothing, matching upstream),
    the RTS smoother's cho_factor(0) fails -> MCP tool error with smooth=True."""
    model, obs = DATA / "degenerate_F0_Q0.json", DATA / "demo_ys.npz"
    res = await call({"model_path": str(model), "observations_path": str(obs), "output_dir": str(tmp_path / "a")})
    assert res["nll"] == float(upstream_kf(model, np.load(obs)["ys"])[2])
    with pytest.raises(ToolError, match="RTS smoother produced non-finite"):
        await call({"model_path": str(model), "observations_path": str(obs), "smooth": True,
                    "output_dir": str(tmp_path / "b")})


async def test_singular_P0_is_accepted(tmp_path):
    """No positive-definiteness check is imposed on P0 for the KF (upstream kf handles P0=0 when R is PD)."""
    spec = json.loads((DATA / "demo_model_true.json").read_text())
    spec["P0"] = [[0.0]]
    p = tmp_path / "p0zero.json"
    p.write_text(json.dumps(spec))
    ys = np.load(DATA / "demo_ys.npz")["ys"]
    res = await call({"model_path": str(p), "observations_path": str(DATA / "demo_ys.npz"),
                      "output_dir": str(tmp_path / "o")})
    assert res["nll"] == float(upstream_kf(p, ys)[2])


@pytest.mark.parametrize("model,obs,fragment", [
    ("demo_model_true.json", "bad_no_ys.npz", "must contain 'ys'"),
    ("demo_model_true.json", "bad_ys_wrong_dy.npz", "ys must have shape"),
    ("demo_model_true.json", "bad_ys_nonfinite.npz", "non-finite"),
    ("mv_model.json", "bad_ys_1d_for_dy2.npz", "ys must have shape"),
    ("demo_model_true.json", "missing.npz", "does not exist"),
    ("missing.json", "demo_ys.npz", "does not exist"),
    ("bad_missing_key.json", "demo_ys.npz", "missing keys"),
    ("bad_shape_Q.json", "demo_ys.npz", "must have shape"),
    ("bad_asym_Q.json", "demo_ys.npz", "must be symmetric: upstream uses it both directly"),
    ("bad_asym_P0.json", "demo_ys.npz", "must be symmetric"),
    ("bad_nonfinite.json", "demo_ys.npz", "non-finite"),
    ("bad_not_json.json", "demo_ys.npz", "not valid JSON"),
    ("bad_nonpd_R.json", "demo_ys.npz", "nll is not finite"),
])
async def test_invalid_inputs_are_tool_errors(tmp_path, model, obs, fragment):
    out = tmp_path / "out"
    with pytest.raises(ToolError, match=fragment):
        await call({"model_path": str(DATA / model), "observations_path": str(DATA / obs),
                    "smooth": True, "compute_gradient": True, "output_dir": str(out)})
    assert not out.exists() or not any(out.iterdir())
