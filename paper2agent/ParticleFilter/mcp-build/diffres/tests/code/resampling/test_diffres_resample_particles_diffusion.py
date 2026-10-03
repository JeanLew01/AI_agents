"""Verifier tests for diffres_resample_particles_diffusion (src/tools/resampling.py).

Oracles: executor-saved upstream outputs (demos/gaussian_mixture.ipynb eager replay; native runs of
experiments/gms/diffusion.py) and direct diffres.resampling.diffusion_resampling / diffusion_resampling_generic calls.
Same jitted path -> bitwise equality; eager notebook path vs jit -> atol 1e-10 (observed ~2e-13).
"""
import json
from pathlib import Path

import jax
import jax.numpy as jnp
import numpy as np
import numpy.testing as npt
import pytest
from diffres.resampling import diffusion_resampling, diffusion_resampling_generic
from ott.tools.sliced import sliced_wasserstein

from conftest import (DATA, GM_KEY, GMS_KEY, NB, RESULTS, call, call_error, ess, key, load_in, load_out, normalise,
                      sha)

TOOL = "diffres_resample_particles_diffusion"


def upstream_jit(raw_key, lw, x, a, T, nsteps, integrator="euler", ode=True, jitter=0.0):
    ts = jnp.linspace(0., T, nsteps + 1)

    @jax.jit
    def f(k, l, s):
        return diffusion_resampling(k, l, s, a, ts, integrator=integrator, ode=ode, jitter=jitter)

    return f(key(raw_key), normalise(lw), jnp.asarray(x))


def record(name, payload):
    p = RESULTS / f"{TOOL}__{name}.json"
    p.write_text(json.dumps(payload, indent=1, default=float))


async def test_gaussian_mixture_notebook_reference(out_base):
    """demos/gaussian_mixture.ipynb cell 6: a=-2, T=1, 32 steps, jentzen_and_kloeden, ODE, notebook key."""
    res = await call(TOOL, {"particles_path": str(DATA / "gm_demo_particles.npz"), "a": -2.0, "T": 1.0, "nsteps": 32,
                            "integrator": "jentzen_and_kloeden", "ode": True, "prng_key": GM_KEY,
                            "output_dir": out_base})
    samples, lw = load_out(res)
    ref = np.load(NB / "gaussian_mixture_demo/data/outputs_replay.npz")
    cap = np.load(NB / "gaussian_mixture_demo/data/outputs_capture.npz")
    assert samples.shape == (1024, 10)
    npt.assert_array_equal(ref["approx_post_samples"], cap["approx_post_samples"])
    # notebook calls the resampler eagerly; the tool (like experiments/gms/diffusion.py) jits it
    npt.assert_allclose(samples, ref["approx_post_samples"], rtol=0, atol=1e-10)
    npt.assert_array_equal(lw, ref["log_ws_diffusion"])
    npt.assert_allclose(lw, -np.log(1024), rtol=0, atol=0)
    x, lw_in = load_in("gm_demo_particles.npz")
    up_lw, up_x = upstream_jit(GM_KEY, lw_in, x, -2.0, 1.0, 32, "jentzen_and_kloeden", True)
    npt.assert_array_equal(samples, np.asarray(up_x))
    npt.assert_array_equal(lw, np.asarray(up_lw))
    assert res["n_particles"] == 1024 and res["sample_shape"] == [10]
    assert res["prng_key"] == GM_KEY and res["input_weight_field"] == "log_weights"
    assert abs(res["input_log_normaliser"]) < 1e-12
    assert res["ess_input"] == pytest.approx(ess(lw_in), rel=1e-12)
    assert res["ess_input"] == pytest.approx(178.113, abs=1e-3)   # executor reference value
    assert res["ess_output"] == pytest.approx(1024.0, rel=1e-12)
    assert res["settings"] == {"a": -2.0, "T": 1.0, "nsteps": 32, "integrator": "jentzen_and_kloeden", "ode": True,
                               "jitter": 0.0, "ts": "linspace(0, T, nsteps + 1)", "jit": True, "x64": True}
    record("gm_notebook", {"max_abs_vs_eager": float(np.max(np.abs(samples - ref["approx_post_samples"]))),
                           "bitwise_vs_direct_jit": True, "ess_input": res["ess_input"]})


@pytest.mark.parametrize("cfg", [
    dict(tag="A_jk_ode_T3_K128", a=-1.0, T=3.0, nsteps=128, integrator="jentzen_and_kloeden", ode=True,
         native="diffres--1.0-3.0-128-jentzen_and_kloeden-ode-0.npz"),
    dict(tag="B_euler_sde_T1_K8", a=-1.0, T=1.0, nsteps=8, integrator="euler", ode=False,
         native="diffres--1.0-1.0-8-euler-sde-0.npz"),
])
async def test_gms_native_script_reference(cfg, out_base):
    """experiments/gms/diffusion.py run natively (MC id 0, nsamples=1000): bitwise equal to the script's saved output."""
    res = await call(TOOL, {"particles_path": str(DATA / "gms_particles.npz"), "a": cfg["a"], "T": cfg["T"],
                            "nsteps": cfg["nsteps"], "integrator": cfg["integrator"], "ode": cfg["ode"],
                            "prng_key": GMS_KEY, "output_dir": out_base})
    samples, lw = load_out(res)
    native = np.load(NB / "gms_diffusion_experiment/work_native/gms/results" / cfg["native"])
    npt.assert_array_equal(samples, native["approx_post_samples"])
    npt.assert_array_equal(lw, native["approx_post_log_ws"])
    assert res["ess_input"] == pytest.approx(129.543, abs=1e-3)
    # the script's own residual metric reproduced from the tool output (mean of resamples vs true posterior mean)
    inp = np.load(NB / f"gms_diffusion_experiment/data/inputs_{cfg['tag']}.npz")
    true_m = np.einsum("c,c...->...", inp["post_vs"], inp["post_ms"])
    approx_m = np.einsum("n,n...->...", np.exp(lw), samples)
    npt.assert_allclose(approx_m - true_m, native["residual"], rtol=0, atol=1e-12)
    record(f"gms_{cfg['tag']}", {"bitwise_vs_native": True, "residual": (approx_m - true_m).tolist()})


async def test_defaults_match_documented_upstream_call(out_base):
    """Only particles_path given: a=-2, T=1, nsteps=32 (notebook), euler/ODE/jitter 0 (upstream signature), PRNGKey(0)."""
    res = await call(TOOL, {"particles_path": str(DATA / "gms_particles.npz"), "output_dir": out_base})
    samples, lw = load_out(res)
    x, lw_in = load_in("gms_particles.npz")
    up_lw, up_x = upstream_jit([0, 0], lw_in, x, -2.0, 1.0, 32)
    npt.assert_array_equal(samples, np.asarray(up_x))
    npt.assert_array_equal(lw, np.asarray(up_lw))
    assert res["prng_key"] == [0, 0]
    assert res["settings"]["a"] == -2.0 and res["settings"]["T"] == 1.0 and res["settings"]["nsteps"] == 32
    assert res["settings"]["integrator"] == "euler" and res["settings"]["ode"] is True
    assert res["settings"]["jitter"] == 0.0


@pytest.mark.parametrize("integrator,ode", [("euler", False), ("lord_and_rougemont", True),
                                            ("lord_and_rougemont", False), ("jentzen_and_kloeden", False),
                                            ("diffrax", True), ("tweedie", False)])
async def test_changed_integrators_seed_and_params(integrator, ode, out_base):
    """Every supported integrator/flow combination, a seed instead of a key, other a/T/nsteps, unnormalised 2-D input."""
    res = await call(TOOL, {"particles_path": str(DATA / "toy2d_unnormalised.npz"), "a": -0.5, "T": 1.5, "nsteps": 7,
                            "integrator": integrator, "ode": ode, "seed": 11, "output_dir": out_base})
    samples, lw = load_out(res)
    x, lw_in = load_in("toy2d_unnormalised.npz")
    up_lw, up_x = upstream_jit(np.asarray(jax.random.PRNGKey(11)).tolist(), lw_in, x, -0.5, 1.5, 7, integrator, ode)
    npt.assert_array_equal(samples, np.asarray(up_x))
    npt.assert_array_equal(lw, np.asarray(up_lw))
    assert res["prng_key"] == np.asarray(jax.random.PRNGKey(11)).tolist()
    lse = float(jax.scipy.special.logsumexp(jnp.asarray(lw_in)))
    assert res["input_log_normaliser"] == pytest.approx(lse, abs=1e-12) and abs(lse) > 1.0
    assert res["n_particles"] == 200 and res["sample_shape"] == [2]


async def test_changed_seed_changes_output(out_base):
    args = {"particles_path": str(DATA / "toy2d_unnormalised.npz"), "nsteps": 4, "output_dir": out_base}
    s1, _ = load_out(await call(TOOL, {**args, "seed": 1}))
    s2, _ = load_out(await call(TOOL, {**args, "seed": 2}))
    assert not np.array_equal(s1, s2)


async def test_one_dimensional_samples_keep_shape(out_base):
    """(N,) samples are passed unchanged (upstream accepts arbitrary data shape); output keeps (N,)."""
    res = await call(TOOL, {"particles_path": str(DATA / "toy1d_unnormalised.npz"), "a": -0.5, "T": 1.0, "nsteps": 15,
                            "integrator": "lord_and_rougemont", "ode": False, "seed": 3, "output_dir": out_base})
    samples, lw = load_out(res)
    x, lw_in = load_in("toy1d_unnormalised.npz")
    assert x.ndim == 1 and samples.shape == (400,) and res["sample_shape"] == []
    up_lw, up_x = upstream_jit(np.asarray(jax.random.PRNGKey(3)).tolist(), lw_in, x, -0.5, 1.0, 15,
                               "lord_and_rougemont", False)
    npt.assert_array_equal(samples, np.asarray(up_x))
    # same as the explicit (N, 1) layout used by tests/test_resampling.py
    _, up_x2 = upstream_jit(np.asarray(jax.random.PRNGKey(3)).tolist(), lw_in, x[:, None], -0.5, 1.0, 15,
                            "lord_and_rougemont", False)
    npt.assert_allclose(samples, np.asarray(up_x2)[:, 0], rtol=0, atol=1e-12)


async def test_three_dimensional_samples(out_base):
    """Upstream accepts (N, ...) particles; the tool passes them through unchanged."""
    res = await call(TOOL, {"particles_path": str(DATA / "gms50_3d_samples.npz"), "nsteps": 4, "seed": 5,
                            "output_dir": out_base})
    samples, _ = load_out(res)
    x, lw_in = load_in("gms50_3d_samples.npz")
    _, up_x = upstream_jit(np.asarray(jax.random.PRNGKey(5)).tolist(), lw_in, x, -2.0, 1.0, 4)
    assert samples.shape == (50, 2, 4) and res["sample_shape"] == [2, 4]
    npt.assert_array_equal(samples, np.asarray(up_x))


async def test_weights_field_equals_log_weights_field(out_base):
    """'weights' input (exp of the gms log weights) gives the same result as 'log_weights'."""
    common = {"a": -1.0, "T": 1.0, "nsteps": 8, "integrator": "euler", "ode": False, "prng_key": GMS_KEY,
              "output_dir": out_base}
    r1 = await call(TOOL, {"particles_path": str(DATA / "gms_particles_weights.npz"), **common})
    s1, l1 = load_out(r1)
    native = np.load(NB / "gms_diffusion_experiment/work_native/gms/results/diffres--1.0-1.0-8-euler-sde-0.npz")
    assert r1["input_weight_field"] == "weights"
    npt.assert_allclose(s1, native["approx_post_samples"], rtol=0, atol=1e-10)
    npt.assert_array_equal(l1, native["approx_post_log_ws"])


async def test_zero_weights_accepted(out_base):
    """-inf log weights (zero weights) are valid input upstream; result equals the direct call and is finite."""
    res = await call(TOOL, {"particles_path": str(DATA / "gms300_neginf.npz"), "seed": 2, "nsteps": 8,
                            "output_dir": out_base})
    samples, lw = load_out(res)
    x, lw_in = load_in("gms300_neginf.npz")
    _, up_x = upstream_jit(np.asarray(jax.random.PRNGKey(2)).tolist(), lw_in, x, -2.0, 1.0, 8)
    assert np.all(np.isfinite(samples))
    npt.assert_array_equal(samples, np.asarray(up_x))
    assert res["ess_input"] == pytest.approx(ess(normalise(lw_in)), rel=1e-12)


async def test_zero_variance_dimension_needs_jitter(out_base):
    """A constant coordinate gives a degenerate reference: upstream returns NaN; tool raises; jitter fixes it."""
    msg = await call_error(TOOL, {"particles_path": str(DATA / "gms200_zero_variance_dim.npz"), "nsteps": 8,
                                  "output_dir": out_base})
    assert "non-finite" in msg and "jitter" in msg
    res = await call(TOOL, {"particles_path": str(DATA / "gms200_zero_variance_dim.npz"), "nsteps": 8,
                            "jitter": 1e-5, "output_dir": out_base})
    samples, _ = load_out(res)
    x, lw_in = load_in("gms200_zero_variance_dim.npz")
    _, up_x = upstream_jit([0, 0], lw_in, x, -2.0, 1.0, 8, jitter=1e-5)
    npt.assert_array_equal(samples, np.asarray(up_x))
    assert res["settings"]["jitter"] == 1e-5


async def test_matches_generic_implementation_reduced_n(out_base):
    """Property check adapted from tests/test_resampling.py::test_diffres_versions (N=400 instead of 10000, 1-D as
    (N, 1)): tool output (euler SDE, a=-1, ts=linspace(0,1,16)) equals diffusion_resampling_generic with the empirical
    Gaussian reference written out as in that test."""
    x, lw_in = load_in("toy1d_unnormalised.npz")
    xs = jnp.asarray(x)[:, None]
    p = Path(out_base).parent / "toy1d_col.npz"
    np.savez(p, samples=np.asarray(xs), log_weights=lw_in)
    res = await call(TOOL, {"particles_path": str(p), "a": -1.0, "T": 1.0, "nsteps": 15, "integrator": "euler",
                            "ode": False, "prng_key": [0, 666], "output_dir": out_base})
    samples, lw = load_out(res)
    a, n = -1.0, xs.shape[0]
    log_ws = normalise(lw_in)
    ws = jnp.exp(log_ws)
    mu = jnp.einsum("i,i...->...", ws, xs)
    stat_vars = jnp.einsum("i,i...->...", ws, (xs - mu) ** 2)
    b2 = -a * stat_vars

    def ref_sampler(key_):
        return mu + jax.random.normal(key_, shape=(n, 1)) * stat_vars ** 0.5

    def score_ref(x_):
        return -(x_ - mu) / stat_vars

    def logpdf_trans(xt, xs_, t, s):
        delta = t - s
        semigroup = jnp.exp(a * delta)
        sigts = stat_vars * (1 - jnp.exp(2 * a * delta))
        return jnp.sum(jax.scipy.stats.norm.logpdf(xt, xs_ * semigroup + mu * (1 - semigroup), sigts ** 0.5), axis=-1)

    lw2, x2 = diffusion_resampling_generic(key([0, 666]), log_ws, xs, ref_sampler, logpdf_trans, score_ref,
                                           b2 ** 0.5, jnp.linspace(0., 1., 16), ode=False)
    npt.assert_allclose(lw, np.asarray(lw2))
    npt.assert_allclose(samples, np.asarray(x2), rtol=1e-7, atol=1e-10)


@pytest.mark.parametrize("integrator,ode", [("euler", True), ("euler", False), ("lord_and_rougemont", True),
                                            ("jentzen_and_kloeden", False), ("diffrax", True), ("tweedie", False)])
async def test_swd_property_reduced_n(integrator, ode, out_base):
    """Property check adapted from tests/test_resampling.py::test_diffres at N=1000 instead of 10000 (upstream file
    excluded for memory). Sliced-Wasserstein distance (n_proj=1000) between resamples and the weighted input; the
    upstream atol 1e-3 is calibrated at N=10000 and Monte Carlo error scales as N^-1/2, so the bound here is
    1e-3 * sqrt(10000 / 1000). Multinomial SWD at the same N is recorded for context (~1e-3)."""
    from diffres.resampling import multinomial
    k = jax.random.PRNGKey(666)
    n = 1000
    xs = jax.random.uniform(k, minval=-2., maxval=2., shape=(n, 1))
    lws = jnp.sum(jax.scipy.stats.norm.logpdf(0., xs, 1.), axis=-1)
    kr, _ = jax.random.split(k)
    p = Path(out_base).parent / "swd_input.npz"
    np.savez(p, samples=np.asarray(xs), log_weights=np.asarray(lws))   # unnormalised, as before the test's own step
    res = await call(TOOL, {"particles_path": str(p), "a": -0.5, "T": 1.0, "nsteps": 15, "integrator": integrator,
                            "ode": ode, "prng_key": np.asarray(kr).tolist(), "output_dir": out_base})
    samples, lw = load_out(res)
    log_ws = normalise(lws)
    swd = jax.jit(lambda s1, s2, a_, b_: sliced_wasserstein(s1, s2, a_, b_, n_proj=1000)[0])
    err = float(swd(jnp.asarray(samples), xs, jnp.exp(lw), jnp.exp(log_ws)))
    mlw, mx = multinomial(kr, log_ws, xs)
    err_m = float(swd(mx, xs, jnp.exp(mlw), jnp.exp(log_ws)))
    record(f"swd_property_{integrator}_{'ode' if ode else 'sde'}", {"N": n, "swd": err, "swd_multinomial": err_m})
    assert err <= 1e-3 * np.sqrt(10000 / n)


async def test_repeated_calls_fresh_artifacts_and_input_unchanged(out_base):
    p = DATA / "toy2d_unnormalised.npz"
    before = sha(p)
    args = {"particles_path": str(p), "nsteps": 4, "seed": 9, "output_dir": out_base}
    r1, r2 = await call(TOOL, args), await call(TOOL, args)
    p1, p2 = Path(r1["artifacts"][0]["path"]), Path(r2["artifacts"][0]["path"])
    assert p1 != p2 and p1.parent != p2.parent
    assert p1.parent.parent == p2.parent.parent == Path(out_base).resolve()
    s1, l1 = load_out(r1)
    s2, l2 = load_out(r2)
    npt.assert_array_equal(s1, s2)
    npt.assert_array_equal(l1, l2)
    assert sha(p) == before
    assert r1["reference"].startswith("https://github.com/zgbkdlm/diffres/blob/767effe")


async def test_composition_with_direct_upstream_particle_filter(out_base):
    """Composition: final-step particles of a direct upstream smc_feynman_kac run (tests/test_filters.py model, 200
    particles) saved in the feynman_kac artifact layout (extra keys allowed) and resampled by the tool."""
    from diffres.feynman_kac import smc_feynman_kac
    from diffres.resampling import multinomial
    k = jax.random.PRNGKey(666)
    nsteps, n, dt = 20, 200, 0.02
    ys = jax.random.normal(k, shape=(nsteps + 1,))
    sg, tc = jnp.exp(-dt), 1 - jnp.exp(-2 * dt)

    def m0_sampler(key_, _):
        return jax.random.normal(key_, shape=(n, 1))

    def log_g0(samples, y0):
        return jnp.sum(jax.scipy.stats.norm.logpdf(y0, samples, 1.), axis=-1)

    def m_log_g(key_, samples, y):
        prop = samples * sg + jax.random.normal(key_, shape=(n, 1)) * tc ** 0.5
        return jnp.sum(jax.scipy.stats.norm.logpdf(y, prop, 1.), axis=-1), prop

    sampless, log_wss, nll, _ = smc_feynman_kac(k, m0_sampler, log_g0, m_log_g, ys, n, nsteps, resampling=multinomial,
                                                resampling_threshold=0.5, return_path=True)
    p = Path(out_base).parent / "pf_final.npz"
    np.savez(p, samples=np.asarray(sampless[-1]), log_weights=np.asarray(log_wss[-1]), nll=np.asarray(nll))
    res = await call(TOOL, {"particles_path": str(p), "a": -1.0, "T": 1.0, "nsteps": 8, "seed": 4,
                            "output_dir": out_base})
    samples, lw = load_out(res)
    _, up_x = upstream_jit(np.asarray(jax.random.PRNGKey(4)).tolist(), np.asarray(log_wss[-1]),
                           np.asarray(sampless[-1]), -1.0, 1.0, 8)
    npt.assert_array_equal(samples, np.asarray(up_x))
    assert res["ess_input"] == pytest.approx(ess(normalise(log_wss[-1])), rel=1e-10)
    assert samples.shape == (200, 1)


@pytest.mark.parametrize("args,fragment", [
    ({"a": 0.0}, "a must be negative"),
    ({"a": 1.0}, "a must be negative"),
    ({"T": 0.0}, "T must be positive"),
    ({"nsteps": 0}, "nsteps must be >= 1"),
    ({"jitter": -1e-3}, "jitter must be non-negative"),
    ({"integrator": "diffrax", "ode": False}, "diffrax"),
    ({"integrator": "tweedie", "ode": True}, "tweedie"),
    ({"prng_key": [1, 2, 3]}, "prng_key"),
    ({"prng_key": [1, -2]}, "prng_key"),
])
async def test_invalid_parameters(args, fragment, out_base):
    msg = await call_error(TOOL, {"particles_path": str(DATA / "toy2d_unnormalised.npz"), "output_dir": out_base,
                                  **args})
    assert fragment in msg


async def test_unknown_integrator_rejected_by_schema(out_base):
    msg = await call_error(TOOL, {"particles_path": str(DATA / "toy2d_unnormalised.npz"), "integrator": "tme",
                                  "output_dir": out_base})
    assert "integrator" in msg


async def test_missing_required_input():
    await call_error(TOOL, {})


@pytest.mark.parametrize("name,fragment", [
    ("does_not_exist.npz", "not found"),
    ("invalid_not_npz.txt", ""),
    ("invalid_no_samples.npz", "samples"),
    ("invalid_no_weights.npz", "exactly one of"),
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
    assert not Path(out_base).exists() or not any(Path(out_base).rglob("*.npz"))
