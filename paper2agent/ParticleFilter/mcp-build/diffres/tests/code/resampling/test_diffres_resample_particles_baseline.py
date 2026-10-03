"""Verifier tests for diffres_resample_particles_baseline (src/tools/resampling.py).

Oracles: executor-saved upstream outputs (native runs of experiments/gms/{baselines,ot,soft,gumbel}.py at MC id 0,
nsamples=1000; eager replay of demos/gaussian_mixture.ipynb cell 6) and direct diffres.resampling calls made here.
Same jitted path -> bitwise equality; eager notebook path vs jit -> atol 1e-10 (observed ~2e-12 for OT).
"""
import json
from pathlib import Path

import jax
import jax.numpy as jnp
import numpy as np
import numpy.testing as npt
import pytest
from diffres.resampling import (ensemble_ot, gumbel_softmax, multinomial, multinomial_stopped, soft_resampling,
                                stratified, systematic)
from ott.tools.sliced import sliced_wasserstein

from conftest import (DATA, GM_KEY, GMS_KEY, NB, RESULTS, call, call_error, ess, key, load_in, load_out, normalise,
                      sha)

TOOL = "diffres_resample_particles_baseline"
UPSTREAM = {"multinomial": multinomial, "stratified": stratified, "systematic": systematic,
            "multinomial_stopped": multinomial_stopped, "ensemble_ot": ensemble_ot, "soft": soft_resampling,
            "gumbel_softmax": gumbel_softmax}
NATIVE = NB / "gms_baselines_experiment/native_run/gms/results"


def upstream_jit(method, raw_key, lw, x, **kw):
    fn = UPSTREAM[method]

    @jax.jit
    def f(k, l, s):
        return fn(k, l, s, **kw)

    return f(key(raw_key), normalise(lw), jnp.asarray(x))


def record(name, payload):
    (RESULTS / f"{TOOL}__{name}.json").write_text(json.dumps(payload, indent=1, default=float))


async def test_gaussian_mixture_notebook_reference(out_base):
    """demos/gaussian_mixture.ipynb cell 6: ensemble_ot(eps=0.3) and multinomial with the notebook key."""
    ref = np.load(NB / "gaussian_mixture_demo/data/outputs_replay.npz")
    cap = np.load(NB / "gaussian_mixture_demo/data/outputs_capture.npz")
    x, lw_in = load_in("gm_demo_particles.npz")
    p = str(DATA / "gm_demo_particles.npz")
    res = await call(TOOL, {"particles_path": p, "method": "ensemble_ot", "eps": 0.3, "prng_key": GM_KEY,
                            "output_dir": out_base})
    s, lw = load_out(res)
    npt.assert_array_equal(ref["approx_post_samples_ot"], cap["approx_post_samples_ot"])
    npt.assert_allclose(s, ref["approx_post_samples_ot"], rtol=0, atol=1e-10)   # notebook is eager, tool jits
    npt.assert_array_equal(lw, ref["log_ws_ot"])
    up_lw, up_x = upstream_jit("ensemble_ot", GM_KEY, lw_in, x, eps=0.3)
    npt.assert_array_equal(s, np.asarray(up_x))
    assert res["settings"] == {"method": "ensemble_ot", "jit": True, "x64": True, "eps": 0.3, "eps_source": "user"}
    assert res["output_weights_uniform"] is True and res["ess_output"] == pytest.approx(1024.0, rel=1e-12)
    assert res["ess_input"] == pytest.approx(178.113, abs=1e-3)
    record("gm_notebook_ot", {"max_abs_vs_eager": float(np.max(np.abs(s - ref["approx_post_samples_ot"])))})

    res = await call(TOOL, {"particles_path": p, "method": "multinomial", "prng_key": GM_KEY, "output_dir": out_base})
    s, lw = load_out(res)
    npt.assert_array_equal(s, ref["approx_post_samples_multinomial"])
    npt.assert_array_equal(lw, ref["log_ws_multinomial"])


@pytest.mark.parametrize("method,kw,native", [
    ("multinomial", {}, NATIVE / "multinomial-0.npz"),
    ("stratified", {}, NATIVE / "stratified-0.npz"),
    ("systematic", {}, NATIVE / "systematic-0.npz"),
    ("ensemble_ot", {"eps": 0.3}, NATIVE / "ot-0.3-0.npz"),
    ("soft", {"alpha": 0.9}, NB / "gms_soft_experiment/run_direct/gms/results/soft-0.9-0.npz"),
    ("gumbel_softmax", {"tau": 0.1}, NB / "gms_gumbel_experiment/run_native/gms/results/gumbel-0.1-0.npz"),
])
async def test_gms_native_script_reference(method, kw, native, out_base):
    """experiments/gms/{baselines,ot,soft,gumbel}.py native outputs (MC id 0, nsamples=1000) reproduced bitwise."""
    res = await call(TOOL, {"particles_path": str(DATA / "gms_particles.npz"), "method": method, "prng_key": GMS_KEY,
                            "output_dir": out_base, **kw})
    s, lw = load_out(res)
    ref = np.load(native)
    npt.assert_array_equal(s, ref["approx_post_samples"])
    npt.assert_array_equal(lw, ref["approx_post_log_ws"])
    cap = np.load(NB / "gms_baselines_experiment/data/capture_baselines_multinomial.npz")
    true_m = np.einsum("c,c...->...", cap["post_vs"], cap["post_ms"])
    approx_m = np.einsum("n,n...->...", np.exp(lw), s)
    npt.assert_allclose(approx_m - true_m, ref["residual"], rtol=0, atol=1e-12)
    assert res["ess_input"] == pytest.approx(129.543, abs=1e-3)
    if method == "soft":
        assert res["output_weights_uniform"] is False
        assert res["ess_output"] == pytest.approx(ess(lw), rel=1e-12)
        assert res["ess_output"] == pytest.approx(935.93, abs=1e-2)
        assert res["settings"]["alpha"] == 0.9
    else:
        assert res["output_weights_uniform"] is True
        npt.assert_allclose(lw, -np.log(1000), rtol=0, atol=0)
    record(f"gms_{method}", {"bitwise_vs_native": True, "ess_output": res["ess_output"]})


async def test_multinomial_stopped_forward_equals_upstream(out_base):
    res = await call(TOOL, {"particles_path": str(DATA / "gms_particles.npz"), "method": "multinomial_stopped",
                            "prng_key": GMS_KEY, "output_dir": out_base})
    s, lw = load_out(res)
    x, lw_in = load_in("gms_particles.npz")
    up_lw, up_x = upstream_jit("multinomial_stopped", GMS_KEY, lw_in, x)
    npt.assert_array_equal(s, np.asarray(up_x))
    npt.assert_array_equal(lw, np.asarray(up_lw))
    native = np.load(NATIVE / "multinomial-0.npz")
    npt.assert_array_equal(s, native["approx_post_samples"])          # same ancestors as multinomial
    npt.assert_allclose(lw, -np.log(1000), rtol=0, atol=1e-15)


@pytest.mark.parametrize("method,expected", [
    ("multinomial", {}), ("ensemble_ot", {"eps": None}), ("soft", {"alpha": 0.5}), ("gumbel_softmax", {"tau": 0.5}),
])
async def test_defaults(method, expected, out_base):
    """Defaults: method multinomial; eps None -> upstream 1/log N; alpha, tau 0.5 (experiments/gms argparse); seed 0."""
    args = {"particles_path": str(DATA / "gms_particles.npz"), "output_dir": out_base}
    if method != "multinomial":
        args["method"] = method
    res = await call(TOOL, args)
    s, lw = load_out(res)
    x, lw_in = load_in("gms_particles.npz")
    up_lw, up_x = upstream_jit(method, [0, 0], lw_in, x, **expected)
    npt.assert_array_equal(s, np.asarray(up_x))
    npt.assert_array_equal(lw, np.asarray(up_lw))
    assert res["prng_key"] == [0, 0] and res["settings"]["method"] == method
    if method == "ensemble_ot":
        assert res["settings"]["eps"] == pytest.approx(1 / np.log(1000), rel=1e-15)
        assert res["settings"]["eps_source"] == "upstream default 1/log(N)"
        _, up_x2 = upstream_jit(method, [0, 0], lw_in, x, eps=float(1 / jnp.log(1000)))
        npt.assert_allclose(s, np.asarray(up_x2), rtol=0, atol=1e-12)
    if method == "soft":
        assert res["settings"]["alpha"] == 0.5
    if method == "gumbel_softmax":
        assert res["settings"]["tau"] == 0.5


@pytest.mark.parametrize("method,kw", [("multinomial", {}), ("stratified", {}), ("systematic", {}),
                                       ("multinomial_stopped", {}), ("ensemble_ot", {"eps": 0.25}),
                                       ("soft", {"alpha": 0.3}), ("gumbel_softmax", {"tau": 0.7})])
async def test_changed_inputs_one_dimensional_unnormalised(method, kw, out_base):
    """1-D (N,) samples with unnormalised log weights and a seed; ensemble_ot gets (N, 1) upstream (ott point cloud)."""
    res = await call(TOOL, {"particles_path": str(DATA / "toy1d_unnormalised.npz"), "method": method, "seed": 21,
                            "output_dir": out_base, **kw})
    s, lw = load_out(res)
    x, lw_in = load_in("toy1d_unnormalised.npz")
    k = np.asarray(jax.random.PRNGKey(21)).tolist()
    xin = x[:, None] if method == "ensemble_ot" else x
    up_lw, up_x = upstream_jit(method, k, lw_in, xin, **kw)
    assert s.shape == (400,) and res["sample_shape"] == []
    npt.assert_array_equal(s, np.asarray(up_x).reshape(400))
    npt.assert_array_equal(lw, np.asarray(up_lw))
    lse = float(jax.scipy.special.logsumexp(jnp.asarray(lw_in)))
    assert res["input_log_normaliser"] == pytest.approx(lse, abs=1e-12) and lse > 5
    assert res["ess_input"] == pytest.approx(ess(normalise(lw_in)), rel=1e-12)


@pytest.mark.parametrize("method,kw", [("multinomial", {}), ("systematic", {}), ("ensemble_ot", {}),
                                       ("soft", {"alpha": 0.5}), ("soft", {"alpha": 1.0}),
                                       ("gumbel_softmax", {"tau": 0.5})])
async def test_zero_weights_accepted(method, kw, out_base):
    """-inf log weights are valid upstream input: same result as the direct call; zero-weight particles are never
    selected by index-based methods."""
    res = await call(TOOL, {"particles_path": str(DATA / "gms300_neginf.npz"), "method": method, "seed": 8,
                            "output_dir": out_base, **kw})
    s, lw = load_out(res)
    x, lw_in = load_in("gms300_neginf.npz")
    up_lw, up_x = upstream_jit(method, np.asarray(jax.random.PRNGKey(8)).tolist(), lw_in, x, **kw)
    npt.assert_array_equal(s, np.asarray(up_x))
    npt.assert_array_equal(lw, np.asarray(up_lw))
    assert np.all(np.isfinite(s))
    if method in ("multinomial", "systematic") or (method == "soft" and kw["alpha"] == 1.0):
        zero_rows = x[::3]
        assert not any(np.any(np.all(zero_rows == row, axis=1)) for row in s)


async def test_three_dimensional_samples(out_base):
    """Index-based methods accept (N, ...) particles; ensemble_ot (ott point cloud) and gumbel_softmax
    (softmax(...) @ samples) do not work upstream for more than two dimensions, so the tool rejects them clearly."""
    x, lw_in = load_in("gms50_3d_samples.npz")
    for method, kw in [("soft", {"alpha": 0.4}), ("systematic", {})]:
        res = await call(TOOL, {"particles_path": str(DATA / "gms50_3d_samples.npz"), "method": method, "seed": 1,
                                "output_dir": out_base, **kw})
        s, _ = load_out(res)
        _, up_x = upstream_jit(method, np.asarray(jax.random.PRNGKey(1)).tolist(), lw_in, x, **kw)
        assert s.shape == (50, 2, 4) and res["sample_shape"] == [2, 4]
        npt.assert_array_equal(s, np.asarray(up_x))
    with pytest.raises(TypeError):     # direct upstream evidence for the gumbel_softmax restriction
        upstream_jit("gumbel_softmax", [0, 1], lw_in, x, tau=0.2)
    msg = await call_error(TOOL, {"particles_path": str(DATA / "gms50_3d_samples.npz"), "method": "gumbel_softmax",
                                  "output_dir": out_base})
    assert "(N,) or (N, d)" in msg
    msg = await call_error(TOOL, {"particles_path": str(DATA / "gms50_3d_samples.npz"), "method": "ensemble_ot",
                                  "output_dir": out_base})
    assert "point cloud" in msg


async def test_weights_field_equals_log_weights_field(out_base):
    res = await call(TOOL, {"particles_path": str(DATA / "gms_particles_weights.npz"), "method": "soft", "alpha": 0.9,
                            "prng_key": GMS_KEY, "output_dir": out_base})
    s, lw = load_out(res)
    ref = np.load(NB / "gms_soft_experiment/run_direct/gms/results/soft-0.9-0.npz")
    assert res["input_weight_field"] == "weights"
    npt.assert_array_equal(s, ref["approx_post_samples"])
    npt.assert_allclose(lw, ref["approx_post_log_ws"], rtol=0, atol=1e-12)


@pytest.mark.parametrize("method,kw,bound_at_10k", [
    ("soft", {"alpha": 1 - 1e-3}, None), ("gumbel_softmax", {"tau": 1e-3}, None), ("ensemble_ot", {"eps": 0.1}, 3e-3),
])
async def test_swd_property_reduced_n(method, kw, bound_at_10k, out_base):
    """Property check adapted from tests/test_resampling.py::test_misc_resamplings / ::test_ensemble_ot at N=1000
    instead of 10000 (upstream file excluded for memory). For OT the upstream atol 3e-3 is scaled by sqrt(10000/N)
    (Monte Carlo error ~ N^-1/2). The soft/gumbel atol 1e-4 was not reproducible as an absolute bound at N=1000 (plain
    multinomial already gives ~1e-3), so these near-multinomial limits are checked against multinomial resampling with
    the same key: SWD <= 1.5 * SWD(multinomial)."""
    k = jax.random.PRNGKey(666)
    n = 1000
    xs = jax.random.uniform(k, minval=-2., maxval=2., shape=(n, 1))
    lws = jnp.sum(jax.scipy.stats.norm.logpdf(0., xs, 1.), axis=-1)
    kr, _ = jax.random.split(k)
    p = Path(out_base).parent / "swd_input.npz"
    np.savez(p, samples=np.asarray(xs), log_weights=np.asarray(lws))
    res = await call(TOOL, {"particles_path": str(p), "method": method, "prng_key": np.asarray(kr).tolist(),
                            "output_dir": out_base, **kw})
    s, lw = load_out(res)
    log_ws = normalise(lws)
    swd = jax.jit(lambda s1, s2, a_, b_: sliced_wasserstein(s1, s2, a_, b_, n_proj=1000)[0])
    err = float(swd(jnp.asarray(s), xs, jnp.exp(lw), jnp.exp(log_ws)))
    mlw, mx = multinomial(kr, log_ws, xs)
    err_m = float(swd(mx, xs, jnp.exp(mlw), jnp.exp(log_ws)))
    record(f"swd_property_{method}", {"N": n, "swd": err, "swd_multinomial": err_m, **kw})
    if bound_at_10k is not None:
        assert err <= bound_at_10k * np.sqrt(10000 / n)
    else:
        assert err <= 1.5 * err_m


async def test_repeated_calls_fresh_artifacts_and_input_unchanged(out_base):
    p = DATA / "toy2d_unnormalised.npz"
    before = sha(p)
    args = {"particles_path": str(p), "method": "systematic", "seed": 3, "output_dir": out_base}
    r1, r2 = await call(TOOL, args), await call(TOOL, args)
    p1, p2 = Path(r1["artifacts"][0]["path"]), Path(r2["artifacts"][0]["path"])
    assert p1 != p2 and p1.parent.parent == p2.parent.parent == Path(out_base).resolve()
    s1, l1 = load_out(r1)
    s2, l2 = load_out(r2)
    npt.assert_array_equal(s1, s2)
    npt.assert_array_equal(l1, l2)
    assert sha(p) == before


async def test_composition_with_diffusion_tool_output(out_base):
    """Composition within the module: the diffusion tool's artifact (samples + log_weights) is a valid input."""
    r = await call("diffres_resample_particles_diffusion", {"particles_path": str(DATA / "toy2d_unnormalised.npz"),
                                                            "nsteps": 4, "output_dir": out_base})
    res = await call(TOOL, {"particles_path": r["artifacts"][0]["path"], "method": "stratified", "seed": 2,
                            "output_dir": out_base})
    s, _ = load_out(res)
    with np.load(r["artifacts"][0]["path"]) as d:
        _, up_x = upstream_jit("stratified", np.asarray(jax.random.PRNGKey(2)).tolist(), d["log_weights"],
                               d["samples"])
    npt.assert_array_equal(s, np.asarray(up_x))
    assert res["ess_input"] == pytest.approx(200.0, rel=1e-12)


async def test_composition_with_feynman_kac_tool_labelled(out_base, tmp_path):
    """LABELLED composition (other module's tool through its own Client; not part of this module's verdict):
    the particle-filter artifact (samples, log_weights + extra keys) is accepted and matches a direct upstream call."""
    from fastmcp import Client
    from tools.feynman_kac import feynman_kac_mcp
    model = {"F": [[0.9]], "Q": [[0.1]], "H": [[1.0]], "R": [[0.5]], "m0": [0.0], "P0": [[1.0]]}
    mp = tmp_path / "model.json"
    mp.write_text(json.dumps(model))
    op = tmp_path / "obs.npz"
    np.savez(op, ys=np.random.default_rng(0).normal(size=(11, 1)))
    async with Client(feynman_kac_mcp) as client:
        pf = (await client.call_tool("diffres_run_lgssm_particle_filter",
                                     {"model_path": str(mp), "observations_path": str(op), "nparticles": 64,
                                      "resampling_method": "multinomial", "output_dir": str(tmp_path / "pf")})).data
    pf_path = pf["artifacts"][0]["path"]
    res = await call(TOOL, {"particles_path": pf_path, "method": "systematic", "seed": 5, "output_dir": out_base})
    s, _ = load_out(res)
    with np.load(pf_path) as d:
        _, up_x = upstream_jit("systematic", np.asarray(jax.random.PRNGKey(5)).tolist(), d["log_weights"],
                               d["samples"])
    npt.assert_array_equal(s, np.asarray(up_x))


@pytest.mark.parametrize("args,fragment", [
    ({"method": "multinomial", "eps": 0.3}, "do not apply"),
    ({"method": "soft", "tau": 0.3}, "do not apply"),
    ({"method": "gumbel_softmax", "alpha": 0.3}, "do not apply"),
    ({"method": "ensemble_ot", "eps": 0.0}, "eps must be positive"),
    ({"method": "ensemble_ot", "eps": -1.0}, "eps must be positive"),
    ({"method": "soft", "alpha": 1.5}, "alpha must be in [0, 1]"),
    ({"method": "soft", "alpha": -0.1}, "alpha must be in [0, 1]"),
    ({"method": "gumbel_softmax", "tau": 0.0}, "tau must be positive"),
    ({"method": "multinomial", "prng_key": [1]}, "prng_key"),
])
async def test_invalid_parameters(args, fragment, out_base):
    msg = await call_error(TOOL, {"particles_path": str(DATA / "toy2d_unnormalised.npz"), "output_dir": out_base,
                                  **args})
    assert fragment in msg


async def test_unknown_method_rejected_by_schema(out_base):
    msg = await call_error(TOOL, {"particles_path": str(DATA / "toy2d_unnormalised.npz"), "method": "residual",
                                  "output_dir": out_base})
    assert "method" in msg


@pytest.mark.parametrize("name,fragment", [
    ("does_not_exist.npz", "not found"),
    ("invalid_no_samples.npz", "samples"),
    ("invalid_both_fields.npz", "exactly one of"),
    ("invalid_nan_log_weights.npz", "NaN"),
    ("invalid_all_neginf.npz", "All weights are zero"),
    ("invalid_shape_mismatch.npz", "shape"),
    ("invalid_single_particle.npz", "N >= 2"),
    ("invalid_negative_weights.npz", "non-negative"),
    ("invalid_nonfinite_samples.npz", "non-finite"),
])
async def test_invalid_particle_files(name, fragment, out_base):
    msg = await call_error(TOOL, {"particles_path": str(DATA / name), "output_dir": out_base})
    assert fragment in msg
