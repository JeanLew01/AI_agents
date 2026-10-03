"""Independent verification of diffres_run_lgssm_particle_filter (module feynman_kac).

Oracles: (a) upstream outputs saved by the executors (notebooks/filters_tests, notebooks/lgssm_diffusion_experiment,
notebooks/lgssm_gradient_demo), (b) direct upstream calls to diffres.feynman_kac.smc_feynman_kac made here with
bootstrap closures copied from tests/test_filters.py lines 59-73 / experiments/lgssm/*.py lines 63-80 or, for the
matrix generalisations, written independently (jax.scipy.stats.multivariate_normal for full R).
The tool is always called through fastmcp.Client; the wrapper's output is never used as an oracle.
Run: heavy.sh --limit-mb 1200 -- diffres-env/bin/python -m pytest tests/code/feynman_kac
"""
import gc
import hashlib
import json
import math
import sys
from pathlib import Path

import jax
import jax.numpy as jnp
import numpy as np
import pytest
from fastmcp import Client
from fastmcp.exceptions import ToolError

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from diffres.feynman_kac import smc_feynman_kac  # noqa: E402
from diffres.gaussian_filters import kf  # noqa: E402
from diffres.resampling import (diffusion_resampling, ensemble_ot, gumbel_softmax, multinomial,  # noqa: E402
                                multinomial_stopped, soft_resampling, stratified, systematic)
from diffres.tools import bures, kl, logpdf_mvn_chol, simulate_lgssm  # noqa: E402

from src.tools.feynman_kac import feynman_kac_mcp  # noqa: E402

jax.config.update("jax_enable_x64", True)

TOOL = "diffres_run_lgssm_particle_filter"
DATA = ROOT / "tests" / "data" / "feynman_kac"
RESULTS = ROOT / "tests" / "results" / "feynman_kac"
OUT = ROOT / "tmp" / "outputs" / "verify-feynman_kac"
NB = ROOT / "notebooks"
COMPARISONS = {}


@pytest.fixture(autouse=True)
def _free_jax_memory():
    # each tool call traces fresh closures; drop compiled executables between tests to bound peak memory
    yield
    jax.clear_caches()
    gc.collect()


@pytest.fixture(scope="session", autouse=True)
def _write_comparisons():
    yield
    RESULTS.mkdir(parents=True, exist_ok=True)
    (RESULTS / "comparisons.json").write_text(json.dumps(COMPARISONS, indent=1, sort_keys=True))


def d(name):
    return str(DATA / name)


def record(case, **diffs):
    COMPARISONS.setdefault(case, {}).update({k: float(v) for k, v in diffs.items()})


def maxabs(a, b):
    a, b = np.asarray(a, dtype=float), np.asarray(b, dtype=float)
    assert a.shape == b.shape, (a.shape, b.shape)
    return float(np.max(np.abs(a - b))) if a.size else 0.0


async def call(**kw):
    kw.setdefault("output_dir", str(OUT))
    async with Client(feynman_kac_mcp) as client:
        res = await client.call_tool(TOOL, kw)
    return res.data


async def call_error(**kw):
    kw.setdefault("output_dir", str(OUT))
    async with Client(feynman_kac_mcp) as client:
        with pytest.raises(ToolError) as exc:
            await client.call_tool(TOOL, kw)
    return str(exc.value)


def load_art(res):
    assert len(res["artifacts"]) == 1
    p = Path(res["artifacts"][0]["path"])
    assert p.is_absolute() and p.is_file()
    with np.load(p) as z:
        return {k: z[k] for k in z.files}


def load_model(name):
    spec = json.loads((DATA / name).read_text())
    return {k: jnp.asarray(v, dtype=jnp.float64) for k, v in spec.items()}


def weighted_moments(sampless, log_wss):
    w = np.exp(log_wss)
    m = np.einsum("knd,kn->kd", sampless, w)
    c = sampless - m[:, None, :]
    return m, np.einsum("kni,knj,kn->kij", c, c, w)


# ----------------------------------------------------------------------------------------------------------------
# Direct upstream oracles
# ----------------------------------------------------------------------------------------------------------------
def experiment_pf(params, ys, key, nparticles, resampling, sig=1.0, xi=0.5, v0_=1.0, m0=None, threshold=1.0):
    """experiments/lgssm/diffusion.py lines 63-80 (scalar params[0]=F, params[1]=H), verbatim apart from the
    resampling threshold argument."""
    m0 = jnp.zeros(1) if m0 is None else m0
    dx = 1

    def m0_sampler(key_, _):
        rnds = jax.random.normal(key_, shape=(nparticles, dx))
        return m0 + v0_ ** 0.5 * rnds

    def log_g0(samples, y0):
        return jnp.sum(jax.scipy.stats.norm.logpdf(y0, params[1] * samples, xi ** 0.5), axis=-1)

    def m_log_g(key__, samples, y):
        rnds = jax.random.normal(key__, shape=(nparticles, dx))
        prop_samples = params[0] * samples + sig ** 0.5 * rnds
        log_potentials = jnp.sum(jax.scipy.stats.norm.logpdf(y, params[1] * prop_samples, xi ** 0.5), axis=-1)
        return log_potentials, prop_samples

    return smc_feynman_kac(key, m0_sampler, log_g0, m_log_g, ys, nparticles, ys.shape[0] - 1,
                           resampling=resampling, resampling_threshold=threshold, return_path=True)


def matrix_pf(model, ys, key, nparticles, resampling, density, transition="chol", F=None, H=None, threshold=1.0):
    """Independent matrix-form bootstrap closures (same random-number order as upstream)."""
    F = model["F"] if F is None else F
    H = model["H"] if H is None else H
    m0, P0, Q, R = model["m0"], model["P0"], model["Q"], model["R"]
    dx = F.shape[0]
    LP0 = jnp.linalg.cholesky(P0)
    LQ = jnp.linalg.cholesky(Q) if transition == "chol" else Q ** 0.5  # test_filters.py: (trans_cov ** 0.5)
    LR = jnp.linalg.cholesky(R)

    def logg(y, xs):
        if density == "sum_univariate":   # tests/test_filters.py form
            return jnp.sum(jax.scipy.stats.norm.logpdf(y, xs @ H.T, jnp.diag(R) ** 0.5), axis=-1)
        if density == "scipy_mvn":        # independent of diffres.tools
            return jax.scipy.stats.multivariate_normal.logpdf(xs @ H.T, y, R)
        if density == "mvn_chol":         # diffres.tools.logpdf_mvn_chol
            return jax.vmap(lambda x: logpdf_mvn_chol(y, H @ x, LR))(xs)
        raise ValueError(density)

    def m0_sampler(key_, _):
        return m0 + jax.random.normal(key_, shape=(nparticles, dx)) @ LP0.T

    def log_g0(samples, y0):
        return logg(y0, samples)

    def m_log_g(key_, samples, y):
        rnds = jax.random.normal(key_, shape=(nparticles, dx))
        prop = jnp.einsum("ij,nj->ni", F, samples) + jnp.einsum("ij,nj->ni", LQ, rnds)
        return logg(y, prop), prop

    return smc_feynman_kac(key, m0_sampler, log_g0, m_log_g, ys, nparticles, ys.shape[0] - 1,
                           resampling=resampling, resampling_threshold=threshold, return_path=True)


def ys_of(name):
    with np.load(DATA / name) as z:
        return jnp.asarray(z["ys"])


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


# ----------------------------------------------------------------------------------------------------------------
# 1. tests/test_filters.py (executor filters_tests): N=1000, T=100, key PRNGKey(666), every resampler of the test
# ----------------------------------------------------------------------------------------------------------------
FILTERS_CASES = {
    "multinomial": (dict(resampling_method="multinomial"), 6e-2),
    "multinomial_stopped": (dict(resampling_method="multinomial_stopped"), 6e-2),
    "stratified": (dict(resampling_method="stratified"), 6e-2),
    "systematic": (dict(resampling_method="systematic"), 6e-2),
    **{f"diffusion_{i}": (dict(resampling_method="diffusion", diffusion_a=-0.5, diffusion_T=2.0, diffusion_steps=7,
                               diffusion_integrator=i, diffusion_ode=False), 5e-2)
       for i in ("euler", "lord_and_rougemont", "jentzen_and_kloeden", "tweedie")},
    "ensemble_ot_eps0.1": (dict(resampling_method="ensemble_ot", ot_eps=0.1, ot_implicit_diff=True), 7e-2),
}


@pytest.fixture(scope="module")
def filters_capture():
    with np.load(NB / "filters_tests/outputs/capture_outputs.npz") as z:
        return {k: z[k] for k in z.files}


@pytest.mark.parametrize("name", list(FILTERS_CASES))
async def test_filters_tests_reference(name, filters_capture):
    kwargs, rtol_test = FILTERS_CASES[name]
    ys_file = "filters_ys_1d.npz" if name.startswith(("multinomial", "diffusion_e", "diffusion_t")) else "filters_ys_2d.npz"
    res = await call(model_path=d("filters_model.json"), observations_path=d(ys_file), nparticles=1000,
                     prng_key=[0, 666], save_particle_path=True, compare_to_kalman=True, **kwargs)
    art = load_art(res)
    cap = {k.split("/")[-1]: v for k, v in filters_capture.items() if k.startswith(f"pf/{name}/")}
    assert res["nsteps"] == 100 and res["nparticles"] == 1000 and res["dx"] == 1 and res["dy"] == 1
    assert res["prng_key"] == [0, 666]
    assert art["samples_path"].shape == (101, 1000, 1) and art["log_weights_path"].shape == (101, 1000)
    diffs = dict(nll=abs(res["nll"] - float(cap["nll"])),
                 samples_path=maxabs(art["samples_path"], cap["samples"]),
                 log_weights_path=maxabs(art["log_weights_path"], cap["log_ws"]),
                 ess_rel=maxabs(art["ess"] / cap["ess"], np.ones(101)))
    record(f"filters_tests/{name}", **diffs)
    assert diffs["nll"] <= 1e-12 * abs(float(cap["nll"]))
    assert diffs["samples_path"] <= 1e-12 and diffs["log_weights_path"] <= 1e-12 and diffs["ess_rel"] <= 1e-12
    np.testing.assert_array_equal(art["samples"], art["samples_path"][-1])
    np.testing.assert_array_equal(art["log_weights"], art["log_weights_path"][-1])
    assert float(art["nll"]) == res["nll"]
    # weighted filtering moments of the saved upstream path (experiments/lgssm/diffusion.py lines 118-120)
    m_ref, v_ref = weighted_moments(cap["samples"], cap["log_ws"])
    assert maxabs(art["filtering_means"], m_ref) <= 1e-12 and maxabs(art["filtering_covs"], v_ref) <= 1e-12
    # Kalman filter of the same test
    assert res["kalman_comparison"]["kf_nll"] == float(filters_capture["kf/nll"])
    np.testing.assert_allclose(art["kf_filtering_means"], filters_capture["kf/mfs"], rtol=0, atol=1e-14)
    np.testing.assert_allclose(art["kf_filtering_covs"], filters_capture["kf/vfs"], rtol=0, atol=1e-14)
    kl_ref = np.asarray(jax.vmap(kl)(jnp.asarray(filters_capture["kf/mfs"]), jnp.asarray(filters_capture["kf/vfs"]),
                                     jnp.asarray(m_ref), jnp.asarray(v_ref)))
    assert maxabs(art["kl_per_step"], kl_ref) <= 1e-9
    # the upstream test assertion itself (raw nll vs KF nll)
    np.testing.assert_allclose(res["nll"], float(filters_capture["kf/nll"]), rtol=rtol_test)
    # ESS summary: threshold 1 -> resampling at every step where ESS < N
    assert res["ess"]["resampling_steps"] == int(np.sum(cap["ess"][:-1] < 1000))
    assert res["ess"]["min"] == pytest.approx(float(cap["ess"].min()), rel=1e-12)


# ----------------------------------------------------------------------------------------------------------------
# 2. experiments/lgssm/diffusion.py (executor lgssm_diffusion_experiment): value_and_grad, filtering KL/Bures
# ----------------------------------------------------------------------------------------------------------------
async def test_lgssm_diffusion_experiment_reference():
    inp = np.load(NB / "lgssm_diffusion_experiment/data/inputs.npz")
    ref = np.load(NB / "lgssm_diffusion_experiment/outputs/reference_outputs.npz")
    res = await call(model_path=d("lgssm_model.json"), observations_path=d("lgssm_ys.npz"), nparticles=16,
                     resampling_method="diffusion", diffusion_a=-1.0, diffusion_T=1.0, diffusion_steps=4,
                     diffusion_integrator="jentzen_and_kloeden", diffusion_ode=False,
                     prng_key=[int(v) for v in inp["key_pf"]], save_particle_path=True, compute_gradient=True,
                     compare_to_kalman=True)
    art = load_art(res)
    kc = res["kalman_comparison"]
    diffs = dict(nll_vs_value_and_grad=abs(res["nll"] - float(ref["nll_pf_true"])),
                 nll_vs_plain_path_call=abs(res["nll"] - float(ref["nll_pf_true_path"])),
                 dF=abs(float(art["grad_F"][0, 0]) - float(ref["grad_pf_true"][0])),
                 dH=abs(float(art["grad_H"][0, 0]) - float(ref["grad_pf_true"][1])),
                 samples=maxabs(art["samples_path"], ref["sampless"]),
                 log_ws=maxabs(art["log_weights_path"], ref["log_wss"]),
                 ess=maxabs(art["ess"], ref["esss"]),
                 mfs=maxabs(art["filtering_means"], ref["mfs_pf"]), vfs=maxabs(art["filtering_covs"], ref["vfs_pf"]),
                 kl=maxabs(art["kl_per_step"], ref["kl_per_step"]),
                 bures=maxabs(art["bures_per_step"], ref["bures_per_step"]),
                 mean_kl=abs(kc["mean_kl"] - float(ref["err_filtering_kl"])),
                 mean_bures=abs(kc["mean_bures"] - float(ref["err_filtering_bures"])),
                 kf_nll=abs(kc["kf_nll"] - float(ref["nll_kf_true"])))
    record("lgssm_diffusion_experiment", **diffs)
    assert diffs["nll_vs_value_and_grad"] <= 1e-12 * 52 and diffs["nll_vs_plain_path_call"] <= 1e-12 * 52
    assert diffs["dF"] <= 1e-12 and diffs["dH"] <= 1e-12
    for k in ("samples", "log_ws", "ess", "mfs", "vfs", "kl", "bures", "mean_kl", "mean_bures"):
        assert diffs[k] <= 1e-12, k
    assert diffs["kf_nll"] <= 1e-12
    np.testing.assert_allclose(art["kf_filtering_means"], ref["mfs_kf"], rtol=0, atol=1e-14)
    assert res["gradient"]["all_finite"] is True
    assert res["gradient"]["grad_F_frobenius_norm"] == pytest.approx(abs(float(ref["grad_pf_true"][0])), rel=1e-12)
    assert res["ess"]["min"] == pytest.approx(2.8312970986272425, rel=1e-12)  # executor summary ess_min
    assert res["ess"]["mean"] == pytest.approx(8.518241895642031, rel=1e-12)  # executor summary ess_mean


# ----------------------------------------------------------------------------------------------------------------
# 3. demos/gradient_variance2.py (executor lgssm_gradient_demo): per-key PF loss and gradient at params (0.2, 0.2)
# ----------------------------------------------------------------------------------------------------------------
GRAD_DEMO_DIFFUSION = dict(resampling_method="diffusion", diffusion_a=-1.0, diffusion_T=2.0, diffusion_steps=128,
                           diffusion_integrator="euler", diffusion_ode=True, diffusion_jitter=1e-5)


@pytest.mark.parametrize("i", [0, 1, 2])
@pytest.mark.parametrize("method", ["diffusion", "multinomial_stopped"])
async def test_gradient_demo_reference(i, method):
    ref = np.load(NB / "lgssm_gradient_demo/data/reference_nsteps16_np8.npz")
    kw = GRAD_DEMO_DIFFUSION if method == "diffusion" else dict(resampling_method="multinomial_stopped")
    res = await call(model_path=d("graddemo_model.json"), observations_path=d("graddemo_ys.npz"), nparticles=8,
                     prng_key=[int(v) for v in ref["keys"][i]], compute_gradient=True, **kw)
    art = load_art(res)
    loss_ref = ref["losses_dp" if method == "diffusion" else "losses_rein"][i]
    grad_ref = ref["grads_dp" if method == "diffusion" else "grads_rein"][i]
    diffs = dict(nll=abs(res["nll"] - float(loss_ref)), dF=abs(float(art["grad_F"][0, 0]) - grad_ref[0]),
                 dH=abs(float(art["grad_H"][0, 0]) - grad_ref[1]))
    record(f"gradient_demo/{method}/key{i}", **diffs)
    assert diffs["nll"] <= 1e-12 * abs(float(loss_ref))
    assert diffs["dF"] <= 1e-11 and diffs["dH"] <= 1e-11
    note = res["gradient"]["note"]
    assert "unbiased" not in note
    if method == "multinomial_stopped":
        assert "REINFORCE" in note and "stop-gradient" in note


# ----------------------------------------------------------------------------------------------------------------
# 4. Matrix generalisations vs direct upstream calls
# ----------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("method,seed", [("multinomial", 3), ("diffusion", 4)])
async def test_full_R_full_Q_model_vs_direct_upstream(method, seed):
    """Non-diagonal Q, R, P0, dy=3 != dx=2; observations from a direct upstream simulate_lgssm call."""
    model, ys = load_model("full2d_model.json"), ys_of("full2d_ys.npz")
    res = await call(model_path=d("full2d_model.json"), observations_path=d("full2d_ys.npz"), nparticles=64,
                     resampling_method=method, seed=seed, save_particle_path=True, compare_to_kalman=True,
                     compute_gradient=(method == "diffusion"))
    art = load_art(res)
    assert res["observation_density"].startswith("multivariate normal") and (res["dx"], res["dy"]) == (2, 3)
    if method == "multinomial":
        r = multinomial
    else:
        ts = jnp.linspace(0., 3.0, 9)

        def r(k, lw, s):
            return diffusion_resampling(k, lw, s, -0.5, ts, integrator="euler", ode=True, jitter=0.)
    key = jax.random.PRNGKey(seed)
    for density in ("scipy_mvn", "mvn_chol"):
        s, lw, nll, ess = matrix_pf(model, ys, key, 64, r, density)
        diffs = dict(nll=abs(res["nll"] - float(nll)), samples=maxabs(art["samples_path"], s),
                     log_ws=maxabs(art["log_weights_path"], lw), ess=maxabs(art["ess"], ess))
        record(f"full2d/{method}/{density}", **diffs)
        assert diffs["nll"] <= 1e-10 and diffs["samples"] <= 1e-10 and diffs["log_ws"] <= 1e-10, density
    # KF comparison: direct kf call and per-step KL/Bures on the oracle moments
    mfs, vfs, nll_kf, *_ = kf(ys, model["m0"], model["P0"], model["F"], model["Q"], model["H"], model["R"])
    assert res["kalman_comparison"]["kf_nll"] == float(nll_kf)
    m_pf, v_pf = weighted_moments(np.asarray(s), np.asarray(lw))
    kl_ref = np.asarray(jax.vmap(kl)(mfs, vfs, jnp.asarray(m_pf), jnp.asarray(v_pf)))
    bu_ref = np.asarray(jax.vmap(bures)(mfs, vfs, jnp.asarray(m_pf), jnp.asarray(v_pf)))
    assert maxabs(art["kl_per_step"], kl_ref) <= 1e-8 * max(1.0, float(np.max(kl_ref)))
    assert maxabs(art["bures_per_step"], bu_ref) <= 1e-8 * max(1.0, float(np.max(bu_ref)))
    assert res["kalman_comparison"]["mean_kl"] == pytest.approx(float(np.mean(kl_ref)), rel=1e-8)
    if method == "diffusion":
        def loss(F, H):
            return matrix_pf(model, ys, key, 64, r, "scipy_mvn", F=F, H=H)[2]
        g = jax.grad(loss, argnums=(0, 1))(model["F"], model["H"])
        dF, dH = maxabs(art["grad_F"], g[0]), maxabs(art["grad_H"], g[1])
        record("full2d/diffusion/grad", dF=dF, dH=dH)
        assert art["grad_F"].shape == (2, 2) and art["grad_H"].shape == (3, 2)
        assert dF <= 1e-8 * max(1.0, float(np.max(np.abs(g[0])))) and dH <= 1e-8 * max(1.0, float(np.max(np.abs(g[1]))))


async def test_diagonal_R_branch_reduces_to_upstream_and_matches_full_branch():
    model, ys = load_model("diagR2d_model.json"), ys_of("diagR2d_ys.npz")
    key = jax.random.PRNGKey(9)
    res = await call(model_path=d("diagR2d_model.json"), observations_path=d("diagR2d_ys.npz"), nparticles=128,
                     resampling_method="multinomial", seed=9, save_particle_path=True)
    res_tiny = await call(model_path=d("diagR2d_tinyoffdiag_model.json"), observations_path=d("diagR2d_ys.npz"),
                          nparticles=128, resampling_method="multinomial", seed=9, save_particle_path=True)
    assert res["observation_density"].startswith("sum of univariate")
    assert res_tiny["observation_density"].startswith("multivariate normal")
    art, art_tiny = load_art(res), load_art(res_tiny)
    s_u, lw_u, nll_u, _ = matrix_pf(model, ys, key, 128, multinomial, "sum_univariate")
    s_m, lw_m, nll_m, _ = matrix_pf(model, ys, key, 128, multinomial, "mvn_chol")
    diffs = dict(diag_branch_vs_upstream_sum=abs(res["nll"] - float(nll_u)),
                 diag_branch_samples_vs_upstream_sum=maxabs(art["samples_path"], s_u),
                 upstream_sum_vs_mvn_chol_nll=abs(float(nll_u) - float(nll_m)),
                 upstream_sum_vs_mvn_chol_logws=maxabs(lw_u, lw_m),
                 full_branch_vs_mvn_chol=abs(res_tiny["nll"] - float(nll_m)),
                 diag_branch_vs_full_branch_nll=abs(res["nll"] - res_tiny["nll"]),
                 diag_branch_vs_full_branch_samples=maxabs(art["samples_path"], art_tiny["samples_path"]),
                 diag_branch_vs_full_branch_logws=maxabs(art["log_weights_path"], art_tiny["log_weights_path"]))
    record("diagR2d/branch_consistency", **diffs)
    assert diffs["diag_branch_vs_upstream_sum"] <= 1e-12 * abs(float(nll_u))
    assert diffs["diag_branch_samples_vs_upstream_sum"] <= 1e-12
    assert diffs["full_branch_vs_mvn_chol"] <= 1e-12 * abs(float(nll_m))
    # the two density formulas are the same density: the branches agree to rounding
    for k in ("upstream_sum_vs_mvn_chol_nll", "diag_branch_vs_full_branch_nll"):
        assert diffs[k] <= 1e-10, k
    for k in ("upstream_sum_vs_mvn_chol_logws", "diag_branch_vs_full_branch_samples", "diag_branch_vs_full_branch_logws"):
        assert diffs[k] <= 1e-10, k


async def test_diagonal_Q_cholesky_equals_upstream_elementwise_root():
    model, ys = load_model("diagQ2d_model.json"), ys_of("diagQ2d_ys.npz")
    np.testing.assert_array_equal(np.asarray(jnp.linalg.cholesky(model["Q"])), np.asarray(model["Q"] ** 0.5))
    res = await call(model_path=d("diagQ2d_model.json"), observations_path=d("diagQ2d_ys.npz"), nparticles=64,
                     resampling_method="stratified", seed=21, save_particle_path=True)
    art = load_art(res)
    s, lw, nll, _ = matrix_pf(model, ys, jax.random.PRNGKey(21), 64, stratified, "sum_univariate",
                              transition="elementwise_sqrt")
    diffs = dict(nll=abs(res["nll"] - float(nll)), samples=maxabs(art["samples_path"], s))
    record("diagQ2d/elementwise_root", **diffs)
    assert diffs["nll"] <= 1e-12 * abs(float(nll)) and diffs["samples"] <= 1e-12


# ----------------------------------------------------------------------------------------------------------------
# 5. Other resamplers, thresholds and parameters vs direct upstream calls (experiments/lgssm closures)
# ----------------------------------------------------------------------------------------------------------------
TS4 = jnp.linspace(0., 1.5, 5)
OTHER_CASES = {
    "soft_alpha0.3": (dict(resampling_method="soft", soft_alpha=0.3),
                      lambda k, lw, s: soft_resampling(k, lw, s, 0.3), 1.0, True),
    "gumbel_tau0.3": (dict(resampling_method="gumbel_softmax", gumbel_tau=0.3),
                      lambda k, lw, s: gumbel_softmax(k, lw, s, 0.3), 1.0, False),
    "ensemble_ot_default_eps_unrolled": (dict(resampling_method="ensemble_ot"),
                                         lambda k, lw, s: ensemble_ot(k, lw, s, None, implicit_diff=False), 1.0, True),
    "ensemble_ot_eps0.5_implicit": (dict(resampling_method="ensemble_ot", ot_eps=0.5, ot_implicit_diff=True),
                                    lambda k, lw, s: ensemble_ot(k, lw, s, 0.5, implicit_diff=True), 1.0, False),
    "systematic_threshold0.5": (dict(resampling_method="systematic", resampling_threshold=0.5), systematic, 0.5, True),
    "stratified_threshold0": (dict(resampling_method="stratified", resampling_threshold=0.0), stratified, 0.0, False),
    "multinomial_threshold0.7": (dict(resampling_method="multinomial", resampling_threshold=0.7), multinomial, 0.7,
                                 True),
    "diffusion_lord_and_rougemont_ode": (
        dict(resampling_method="diffusion", diffusion_a=-1.0, diffusion_T=1.5, diffusion_steps=4,
             diffusion_integrator="lord_and_rougemont", diffusion_ode=True),
        lambda k, lw, s: diffusion_resampling(k, lw, s, -1.0, TS4, integrator="lord_and_rougemont", ode=True), 1.0,
        False),
    "diffusion_diffrax_ode": (
        dict(resampling_method="diffusion", diffusion_a=-1.0, diffusion_T=1.5, diffusion_steps=4,
             diffusion_integrator="diffrax", diffusion_ode=True),
        lambda k, lw, s: diffusion_resampling(k, lw, s, -1.0, TS4, integrator="diffrax", ode=True), 1.0, False),
    "diffusion_tweedie_sde_jitter": (
        dict(resampling_method="diffusion", diffusion_a=-1.0, diffusion_T=1.5, diffusion_steps=4,
             diffusion_integrator="tweedie", diffusion_ode=False, diffusion_jitter=1e-3),
        lambda k, lw, s: diffusion_resampling(k, lw, s, -1.0, TS4, integrator="tweedie", ode=False, jitter=1e-3),
        1.0, True),
}


@pytest.mark.parametrize("name", list(OTHER_CASES))
async def test_other_resamplers_vs_direct_upstream(name):
    kw, r, thr, grad = OTHER_CASES[name]
    seed = 100 + list(OTHER_CASES).index(name)
    ys = ys_of("lgssm_ys.npz")
    res = await call(model_path=d("lgssm_model.json"), observations_path=d("lgssm_ys.npz"), nparticles=32, seed=seed,
                     save_particle_path=True, compute_gradient=grad, **kw)
    art = load_art(res)
    key = jax.random.PRNGKey(seed)
    s, lw, nll, ess = experiment_pf(jnp.array([0.5, 1.0]), ys, key, 32, r, threshold=thr)
    diffs = dict(nll=abs(res["nll"] - float(nll)), samples=maxabs(art["samples_path"], s),
                 log_ws=maxabs(art["log_weights_path"], lw), ess=maxabs(art["ess"], ess))
    assert diffs["nll"] <= 1e-11 * abs(float(nll))
    assert diffs["samples"] <= 1e-11 and diffs["log_ws"] <= 1e-11 and diffs["ess"] <= 1e-10
    assert res["ess"]["resampling_steps"] == int(np.sum(np.asarray(ess)[:-1] < thr * 32))
    if name == "stratified_threshold0":
        assert res["ess"]["resampling_steps"] == 0
    if name.startswith("ensemble_ot_default"):
        assert res["resampling_settings"]["eps"] == pytest.approx(1 / math.log(32), rel=1e-15)
        assert res["resampling_settings"]["eps_from_upstream_default"] is True
    if name.startswith("soft"):  # soft returns non-uniform normalised log weights
        assert abs(float(jax.scipy.special.logsumexp(jnp.asarray(art["log_weights"])))) <= 1e-12
    if grad:
        g = jax.grad(lambda p: experiment_pf(p, ys, key, 32, r, threshold=thr)[2])(jnp.array([0.5, 1.0]))
        diffs.update(dF=abs(float(art["grad_F"][0, 0]) - float(g[0])), dH=abs(float(art["grad_H"][0, 0]) - float(g[1])))
        assert diffs["dF"] <= 1e-9 * max(1.0, abs(float(g[0]))) and diffs["dH"] <= 1e-9 * max(1.0, abs(float(g[1])))
        assert "unbiased" not in res["gradient"]["note"]
    record(f"lgssm_other/{name}", **diffs)


async def test_defaults_match_experiment_cli_defaults():
    res = await call(model_path=d("lgssm_model.json"), observations_path=d("lgssm_ys.npz"))
    assert res["nparticles"] == 32 and res["resampling_method"] == "diffusion" and res["resampling_threshold"] == 1.0
    st = res["resampling_settings"]
    assert (st["a"], st["T"], st["steps"], st["integrator"], st["ode"], st["jitter"]) == (-0.5, 3.0, 8, "euler",
                                                                                        True, 0.0)
    assert res["prng_key"] == [0, 0]
    ts = jnp.linspace(0., 3., 9)
    _, _, nll, _ = experiment_pf(jnp.array([0.5, 1.0]), ys_of("lgssm_ys.npz"), jax.random.PRNGKey(0), 32,
                                 lambda k, lw, s: diffusion_resampling(k, lw, s, -0.5, ts, integrator="euler", ode=True))
    record("defaults", nll=abs(res["nll"] - float(nll)))
    assert abs(res["nll"] - float(nll)) <= 1e-12 * abs(float(nll))
    assert "gradient" not in res and "kalman_comparison" not in res
    art = load_art(res)
    assert set(art) == {"samples", "log_weights", "ess", "filtering_means", "filtering_covs", "nll", "nll_plus_log_n",
                        "prng_key"}


async def test_single_observation_T0():
    ys = ys_of("lgssm_ys_T0.npz")
    res = await call(model_path=d("lgssm_model.json"), observations_path=d("lgssm_ys_T0.npz"), nparticles=16,
                     resampling_method="multinomial", seed=5)
    _, _, nll, ess = experiment_pf(jnp.array([0.5, 1.0]), ys, jax.random.PRNGKey(5), 16, multinomial)
    assert res["nsteps"] == 0 and res["ess"]["resampling_steps"] == 0
    assert res["nll"] == pytest.approx(float(nll), rel=1e-13)
    assert load_art(res)["ess"].shape == (1,)


# ----------------------------------------------------------------------------------------------------------------
# 6. nll offset (-log N) and KL / Bures conventions
# ----------------------------------------------------------------------------------------------------------------
@pytest.mark.parametrize("n", [16, 100])
async def test_nll_offset_is_minus_log_n(n):
    """With H = 0 all particles carry the same potential, so the PF likelihood estimate is exact:
    nll + log N equals the Kalman nll and the raw upstream nll is exactly log N lower."""
    res = await call(model_path=d("zeroH_model.json"), observations_path=d("lgssm_ys.npz"), nparticles=n,
                     resampling_method="multinomial", seed=1, compare_to_kalman=True)
    m = load_model("zeroH_model.json")
    ys = ys_of("lgssm_ys.npz")
    nll_kf = float(kf(ys, m["m0"], m["P0"], m["F"], m["Q"], m["H"], m["R"])[2])
    # closed form with H = 0: sum_k -log N(y_k; 0, R)
    nll_exact = float(-np.sum(jax.scipy.stats.norm.logpdf(np.asarray(ys)[:, 0], 0., 0.5 ** 0.5)))
    assert nll_kf == pytest.approx(nll_exact, rel=1e-13)
    assert res["nll_plus_log_n"] == pytest.approx(nll_exact, rel=1e-12)
    assert res["nll"] == pytest.approx(nll_exact - math.log(n), rel=1e-12)
    assert res["nll_plus_log_n"] - res["nll"] == pytest.approx(math.log(n), rel=1e-12)
    assert res["kalman_comparison"]["nll_plus_log_n_minus_kf_nll"] == pytest.approx(0.0, abs=1e-10)
    art = load_art(res)
    assert float(art["nll_plus_log_n"]) - float(art["nll"]) == pytest.approx(math.log(n), rel=1e-12)


def test_symmetry_check_rationale():
    """jnp.linalg.cholesky (jax 0.7.2) symmetrises its input, but diffres.gaussian_filters.kf uses Q as given:
    an asymmetric Q would give a symmetrised PF transition but an asymmetric KF covariance."""
    Q = jnp.array([[0.5, 0.2], [0.1, 0.3]])
    np.testing.assert_array_equal(np.asarray(jnp.linalg.cholesky(Q)), np.asarray(jnp.linalg.cholesky((Q + Q.T) / 2)))
    m = load_model("full2d_model.json")
    vfs = kf(ys_of("full2d_ys.npz"), m["m0"], m["P0"], m["F"], Q, m["H"], m["R"])[1]
    assert not np.allclose(np.asarray(vfs[1]), np.asarray(vfs[1]).T)


def test_kl_and_bures_conventions_of_upstream_tools():
    rng = np.random.default_rng(0)
    for _ in range(3):
        A, B = rng.normal(size=(2, 2)), rng.normal(size=(2, 2))
        c0, c1 = A @ A.T + 0.5 * np.eye(2), B @ B.T + 0.5 * np.eye(2)
        m0, m1 = rng.normal(size=2), rng.normal(size=2)
        ic1 = np.linalg.inv(c1)
        kl_true = 0.5 * (np.trace(ic1 @ c0) - 2 + (m1 - m0) @ ic1 @ (m1 - m0)
                         + np.log(np.linalg.det(c1) / np.linalg.det(c0)))  # KL(N0 || N1)
        assert float(kl(*map(jnp.asarray, (m0, c0, m1, c1)))) == pytest.approx(2 * kl_true, rel=1e-10)
    # Bures: squared 2-Wasserstein distance; closed form for commuting (diagonal) covariances
    m0, m1 = np.array([0.3, -1.0]), np.array([1.0, 0.5])
    s0, s1 = np.array([0.5, 2.0]), np.array([1.5, 0.7])
    w2sq = np.sum((m0 - m1) ** 2) + np.sum((np.sqrt(s0) - np.sqrt(s1)) ** 2)
    assert float(bures(jnp.asarray(m0), jnp.diag(jnp.asarray(s0)), jnp.asarray(m1), jnp.diag(jnp.asarray(s1)))) \
        == pytest.approx(w2sq, rel=1e-12)


async def test_kalman_comparison_labels():
    res = await call(model_path=d("lgssm_model.json"), observations_path=d("lgssm_ys.npz"), nparticles=16,
                     resampling_method="multinomial", compare_to_kalman=True)
    kc = res["kalman_comparison"]
    assert "2 * KL(N_KF || N_PF)" in kc["kl_definition"] and "squared 2-Wasserstein" in kc["bures_definition"]
    assert kc["nll_plus_log_n_minus_kf_nll"] == pytest.approx(res["nll_plus_log_n"] - kc["kf_nll"], abs=1e-12)
    assert kc["kl_all_finite"] is True


# ----------------------------------------------------------------------------------------------------------------
# 7. Seeds, repeated calls, input isolation, 1-D observations
# ----------------------------------------------------------------------------------------------------------------
async def test_seed_key_and_repeated_call_isolation():
    files = [DATA / "lgssm_model.json", DATA / "lgssm_ys.npz"]
    before = [sha(f) for f in files]
    kw = dict(model_path=d("lgssm_model.json"), observations_path=d("lgssm_ys.npz"), nparticles=16,
              resampling_method="multinomial")
    r1 = await call(seed=0, **kw)
    r2 = await call(seed=0, **kw)
    r3 = await call(prng_key=[0, 0], seed=99, **kw)
    r4 = await call(seed=1, **kw)
    assert r1["nll"] == r2["nll"] == r3["nll"] and r4["nll"] != r1["nll"]
    assert r3["prng_key"] == [0, 0] and r4["prng_key"] == [0, 1]
    paths = {r["artifacts"][0]["path"] for r in (r1, r2, r3, r4)}
    assert len(paths) == 4 and all(Path(p).parent.parent == OUT.resolve() for p in paths)
    np.testing.assert_array_equal(load_art(r1)["samples"], load_art(r2)["samples"])
    assert [sha(f) for f in files] == before


async def test_one_dimensional_ys_equals_two_dimensional():
    kw = dict(model_path=d("filters_model.json"), nparticles=200, resampling_method="systematic", seed=4,
              save_particle_path=True)
    r1 = await call(observations_path=d("filters_ys_1d.npz"), **kw)
    r2 = await call(observations_path=d("filters_ys_2d.npz"), **kw)
    assert r1["nll"] == r2["nll"]
    np.testing.assert_array_equal(load_art(r1)["samples_path"], load_art(r2)["samples_path"])


# ----------------------------------------------------------------------------------------------------------------
# 8. Composition
# ----------------------------------------------------------------------------------------------------------------
async def test_composition_direct_simulate_and_resample(tmp_path):
    """Observations from a direct upstream simulate_lgssm call are accepted; the PF artifact holds the resampling
    contract (samples (N, dx), normalised log_weights (N,)) and feeds a direct upstream resampler."""
    m = load_model("full2d_model.json")
    xs, ys = simulate_lgssm(jax.random.PRNGKey(31), m["F"], m["Q"], m["H"], m["R"], m["m0"], m["P0"], 6)
    obs = tmp_path / "data.npz"
    np.savez(obs, xs=np.asarray(xs), ys=np.asarray(ys))
    res = await call(model_path=d("full2d_model.json"), observations_path=str(obs), nparticles=50,
                     resampling_method="systematic", seed=2)
    _, _, nll, _ = matrix_pf(m, ys, jax.random.PRNGKey(2), 50, systematic, "scipy_mvn")
    assert res["nll"] == pytest.approx(float(nll), rel=1e-10) and res["nsteps"] == 6
    art = load_art(res)
    assert art["samples"].shape == (50, 2) and art["log_weights"].shape == (50,)
    assert abs(float(jax.scipy.special.logsumexp(jnp.asarray(art["log_weights"])))) <= 1e-12
    lw_out, s_out = diffusion_resampling(jax.random.PRNGKey(0), jnp.asarray(art["log_weights"]),
                                         jnp.asarray(art["samples"]), -1.0, jnp.linspace(0., 1., 9))
    assert s_out.shape == (50, 2) and bool(jnp.all(jnp.isfinite(s_out)))


async def test_composition_cross_tool_clients():
    """LABELLED cross-tool composition (not an oracle): gaussian_filters.diffres_simulate_lgssm_data output feeds this
    tool, and this tool's artifact feeds resampling.diffres_resample_particles_diffusion, each through its own Client."""
    from src.tools.gaussian_filters import gaussian_filters_mcp
    from src.tools.resampling import resampling_mcp
    async with Client(gaussian_filters_mcp) as c:
        sim = (await c.call_tool("diffres_simulate_lgssm_data", {
            "model_path": d("full2d_model.json"), "nsteps": 5, "seed": 3, "output_dir": str(OUT)})).data
    data_path = next(a["path"] for a in sim["artifacts"] if a["path"].endswith("data.npz"))
    model_copy = next(a["path"] for a in sim["artifacts"] if a["path"].endswith("model.json"))
    res = await call(model_path=model_copy, observations_path=data_path, nparticles=40,
                     resampling_method="multinomial", seed=1)
    m = load_model("full2d_model.json")
    with np.load(data_path) as z:
        ys = jnp.asarray(z["ys"])
    _, _, nll, _ = matrix_pf(m, ys, jax.random.PRNGKey(1), 40, multinomial, "scipy_mvn")
    assert res["nll"] == pytest.approx(float(nll), rel=1e-10)
    async with Client(resampling_mcp) as c:
        rs = (await c.call_tool("diffres_resample_particles_diffusion", {
            "particles_path": res["artifacts"][0]["path"], "seed": 0, "output_dir": str(OUT)})).data
    assert rs["n_particles"] == 40 and rs["sample_shape"] == [2]
    assert abs(rs["input_log_normaliser"]) <= 1e-12


# ----------------------------------------------------------------------------------------------------------------
# 9. Invalid inputs surface as MCP tool errors
# ----------------------------------------------------------------------------------------------------------------
ERRORS = [
    (dict(model_path=d("does_not_exist.json")), "model_path does not exist"),
    (dict(model_path=d("bad_missing_R_model.json")), "missing keys ['R']"),
    (dict(model_path=d("bad_R_not_pd_model.json")), "R must be positive definite"),
    (dict(model_path=d("bad_Q_asym_model.json"), observations_path=d("full2d_ys.npz")),
     "Q must be symmetric (it is a covariance matrix"),
    (dict(model_path=d("bad_H_shape_model.json")), "H must have shape"),
    (dict(observations_path=d("bad_ys_nonfinite.npz")), "non-finite"),
    (dict(observations_path=d("bad_ys_wrong_dy.npz")), "ys must have shape (T+1, 1)"),
    (dict(observations_path=d("bad_no_ys.npz")), "must contain an array 'ys'"),
    (dict(observations_path=d("missing.npz")), "observations_path does not exist"),
    (dict(nparticles=0), "nparticles must be >= 1"),
    (dict(resampling_threshold=1.5), "resampling_threshold must lie in [0, 1]"),
    (dict(diffusion_a=0.5), "diffusion_a must be negative"),
    (dict(diffusion_T=0.0), "diffusion_T must be positive"),
    (dict(diffusion_steps=0), "diffusion_steps must be >= 1"),
    (dict(diffusion_jitter=-1.0), "diffusion_jitter must be >= 0"),
    (dict(diffusion_integrator="tweedie", diffusion_ode=True), "'tweedie' only with ode=False"),
    (dict(diffusion_integrator="diffrax", diffusion_ode=False), "'diffrax' only with ode=True"),
    (dict(resampling_method="ensemble_ot", ot_eps=-1.0), "ot_eps must be positive"),
    (dict(resampling_method="ensemble_ot", nparticles=1), "needs nparticles >= 2"),
    (dict(resampling_method="soft", soft_alpha=1.5), "soft_alpha must lie in [0, 1]"),
    (dict(resampling_method="gumbel_softmax", gumbel_tau=0.0), "gumbel_tau must be positive"),
    (dict(prng_key=[1, 2, 3]), "prng_key must be exactly two uint32"),
    (dict(prng_key=[-1, 2]), "prng_key must be exactly two uint32"),
    (dict(resampling_method="residual"), "resampling_method"),
]


@pytest.mark.parametrize("kw,fragment", ERRORS, ids=[e[1][:30] for e in ERRORS])
async def test_invalid_inputs(kw, fragment):
    args = dict(model_path=d("lgssm_model.json"), observations_path=d("lgssm_ys.npz"), nparticles=8)
    args.update(kw)
    msg = await call_error(**args)
    assert fragment in msg, msg


# ----------------------------------------------------------------------------------------------------------------
# 10. Tool format
# ----------------------------------------------------------------------------------------------------------------
async def test_tool_schema_and_format():
    async with Client(feynman_kac_mcp) as client:
        tools = await client.list_tools()
    assert [t.name for t in tools] == [TOOL]
    t = tools[0]
    schema = t.inputSchema
    assert set(schema.get("required", [])) == {"model_path", "observations_path"}
    for name, prop in schema["properties"].items():
        assert prop.get("description"), name
    assert set(schema["properties"]["resampling_method"]["enum"]) == {
        "diffusion", "multinomial", "stratified", "systematic", "multinomial_stopped", "ensemble_ot", "soft",
        "gumbel_softmax"}
    assert set(schema["properties"]["diffusion_integrator"]["enum"]) == {
        "euler", "lord_and_rougemont", "jentzen_and_kloeden", "tweedie", "diffrax"}
    doc_lines = [ln for ln in (t.description or "").strip().splitlines() if ln.strip()]
    assert len(doc_lines) == 2
    res = await call(model_path=d("lgssm_model.json"), observations_path=d("lgssm_ys.npz"), nparticles=8,
                     resampling_method="multinomial")
    assert {"message", "reference", "artifacts"} <= set(res)
    assert res["reference"].startswith("https://github.com/zgbkdlm/diffres/blob/767effe3e755067eb8a04422597fbf37eb8ab754/")
    json.dumps(res)
