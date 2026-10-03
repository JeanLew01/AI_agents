"""Delivery verifier: changed-input real MCP calls through the EXTRACTED server, compared with direct upstream
diffres calls in the same extracted environment; also dumps the live tool schemas and checks import origins.

Run with the extracted .venv python, cwd = extracted package folder, through heavy.sh.
argv: <extracted dir> <inputs dir> <out json>
"""
import asyncio
import json
import os
import sys
from pathlib import Path

EXTRACTED = Path(sys.argv[1]).resolve()
INPUTS = Path(sys.argv[2]).resolve()
OUT = Path(sys.argv[3])
WORKSPACE = "/home/jixia/AI_agents/paper2agent/ParticleFilter"
OUTROOT = EXTRACTED / "tmp" / "outputs" / "delivery-changed-input"
report = {"python": sys.executable, "python_version": sys.version.split()[0], "cwd": os.getcwd()}

import numpy as np  # noqa: E402

# Changed input 1: a new particle file = first 300 particles of the gms fixture (different N), new key/settings.
src = np.load(INPUTS / "resampling" / "gms_particles.npz")
print("gms fixture keys", src.files, {k: src[k].shape for k in src.files})
wkey = "log_weights" if "log_weights" in src.files else "weights"
NEWN = 300
new_particles = INPUTS / "resampling" / "delivery_gms_first300.npz"
np.savez(new_particles, samples=src["samples"][:NEWN], **{wkey: src[wkey][:NEWN]})
DIFF_ARGS = {"particles_path": str(new_particles), "a": -1.5, "T": 2.0, "nsteps": 16,
             "integrator": "lord_and_rougemont", "ode": True, "seed": 4242,
             "output_dir": str(OUTROOT)}

# Changed input 2: OU model of tests/test_filters.py, observations = fixture filters_ys_1d.npz,
# multinomial, N = 64, new key PRNGKey(2026) given as raw prng_key.
PF_KEY = [0, 2026]  # == jax.random.PRNGKey(2026) raw data (checked below)
PF_ARGS = {"model_path": str(INPUTS / "feynman_kac" / "filters_model.json"),
           "observations_path": str(INPUTS / "feynman_kac" / "filters_ys_1d.npz"),
           "nparticles": 64, "resampling_method": "multinomial", "resampling_threshold": 1.0,
           "prng_key": PF_KEY, "output_dir": str(OUTROOT)}
KF_ARGS = {"model_path": PF_ARGS["model_path"], "observations_path": PF_ARGS["observations_path"],
           "output_dir": str(OUTROOT)}


def find_server_pids():
    pids = []
    for p in Path("/proc").iterdir():
        if not p.name.isdigit():
            continue
        try:
            cmd = (p / "cmdline").read_bytes().split(b"\0")
        except OSError:
            continue
        if any(str(EXTRACTED / "src" / "diffres_mcp.py").encode() == c for c in cmd):
            pids.append(int(p.name))
    return pids


async def mcp_part():
    from fastmcp import Client
    env = {k: v for k, v in os.environ.items() if k not in ("PYTHONPATH", "VIRTUAL_ENV", "PYTHONHOME")}
    config = {"mcpServers": {"diffres": {"command": str(EXTRACTED / ".venv" / "bin" / "python"),
                                         "args": [str(EXTRACTED / "src" / "diffres_mcp.py")],
                                         "cwd": str(EXTRACTED), "env": env}}}
    async with Client(config) as client:
        tools = await client.list_tools()
        report["tool_schemas"] = {t.name: t.inputSchema for t in tools}
        r1 = await client.call_tool("diffres_resample_particles_diffusion", DIFF_ARGS, raise_on_error=False)
        report["diffusion_call"] = {"is_error": r1.is_error, "data": r1.data if not r1.is_error else
                                    [getattr(b, "text", "") for b in r1.content]}
        r1b = await client.call_tool("diffres_resample_particles_diffusion", DIFF_ARGS, raise_on_error=False)
        report["diffusion_call_repeat"] = {"is_error": r1b.is_error, "data": r1b.data if not r1b.is_error else None}
        r2 = await client.call_tool("diffres_run_lgssm_particle_filter", PF_ARGS, raise_on_error=False)
        report["pf_call"] = {"is_error": r2.is_error, "data": r2.data if not r2.is_error else
                             [getattr(b, "text", "") for b in r2.content]}
        r3 = await client.call_tool("diffres_run_lgssm_kalman_filter", KF_ARGS, raise_on_error=False)
        report["kf_call"] = {"is_error": r3.is_error, "data": r3.data if not r3.is_error else
                             [getattr(b, "text", "") for b in r3.content]}
        # server process evidence: interpreter, cwd, mapped shared objects
        pids = find_server_pids()
        srv = []
        for pid in pids:
            try:
                exe = os.readlink(f"/proc/{pid}/exe")
                cwd = os.readlink(f"/proc/{pid}/cwd")
                maps = Path(f"/proc/{pid}/maps").read_text().splitlines()
            except OSError as exc:
                srv.append({"pid": pid, "error": str(exc)})
                continue
            files = sorted({ln.split()[-1] for ln in maps if len(ln.split()) >= 6 and ln.split()[-1].startswith("/")})
            srv.append({"pid": pid, "exe": exe, "cwd": cwd, "n_mapped_files": len(files),
                        "mapped_files_under_workspace": [f for f in files if f.startswith(WORKSPACE)
                                                         and not f.startswith(str(EXTRACTED))],
                        "jaxlib_so_sample": [f for f in files if "jaxlib" in f][:2]})
        report["server_processes"] = srv


asyncio.run(mcp_part())

# ---- direct upstream references in the same extracted environment (after the server has exited) ----
import jax  # noqa: E402
import jax.numpy as jnp  # noqa: E402

jax.config.update("jax_enable_x64", True)
import diffres  # noqa: E402
from diffres.resampling import diffusion_resampling, multinomial  # noqa: E402
from diffres.feynman_kac import smc_feynman_kac  # noqa: E402
from diffres.gaussian_filters import kf  # noqa: E402

checks = {}
# 1. diffusion resampling
d = np.load(new_particles)
lw = jnp.log(jnp.asarray(d[wkey], dtype=jnp.float64)) if wkey == "weights" else jnp.asarray(d[wkey], dtype=jnp.float64)
lw = lw - jax.scipy.special.logsumexp(lw)
samples = jnp.asarray(d["samples"], dtype=jnp.float64)
key = jax.random.PRNGKey(4242)
ts = jnp.linspace(0., 2.0, 17)
ref_jit_lw, ref_jit = jax.jit(lambda k, l, s: diffusion_resampling(k, l, s, -1.5, ts, integrator="lord_and_rougemont",
                                                                    ode=True))(key, lw, samples)
ref_eager_lw, ref_eager = diffusion_resampling(key, lw, samples, -1.5, ts, integrator="lord_and_rougemont", ode=True)
c1 = {"tool_args": DIFF_ARGS, "N": NEWN, "fixture_weight_field": wkey}
if not report["diffusion_call"]["is_error"]:
    p = report["diffusion_call"]["data"]["artifacts"][0]["path"]
    o = np.load(p)
    p2 = report["diffusion_call_repeat"]["data"]["artifacts"][0]["path"]
    o2 = np.load(p2)
    c1.update({
        "artifact": p, "artifact_repeat": p2, "distinct_artifact_paths": p != p2,
        "samples_shape": list(o["samples"].shape),
        "bitwise_equal_to_direct_jit": bool(np.array_equal(o["samples"], np.asarray(ref_jit))
                                            and np.array_equal(o["log_weights"], np.asarray(ref_jit_lw))),
        "max_abs_diff_vs_direct_jit": float(np.max(np.abs(o["samples"] - np.asarray(ref_jit)))),
        "max_abs_diff_vs_direct_eager": float(np.max(np.abs(o["samples"] - np.asarray(ref_eager)))),
        "repeat_bitwise_equal": bool(np.array_equal(o["samples"], o2["samples"])),
        "prng_key_returned": report["diffusion_call"]["data"]["prng_key"],
        "ess_output": report["diffusion_call"]["data"]["ess_output"],
    })
    c1["pass"] = bool(c1["max_abs_diff_vs_direct_jit"] <= 1e-12 and c1["repeat_bitwise_equal"]
                      and c1["distinct_artifact_paths"])
else:
    c1["pass"] = False
checks["diffusion_changed_input"] = c1

# 2. particle filter, built exactly as tests/test_filters.py (OU model, scalar roots), new key, N = 64
ell, sigma, dx, dy, xi = 1., 1., 1, 1, 1.
obs_op = jnp.ones((dy, dx))
Tt, nsteps = 2., 100
dt = Tt / nsteps
ys_test = jax.random.normal(jax.random.PRNGKey(666), shape=(nsteps + 1,))
ys_fix = np.load(INPUTS / "feynman_kac" / "filters_ys_1d.npz")["ys"]
m0, v0 = jnp.zeros(dx), sigma ** 2 * jnp.eye(dx)
semigroup = jnp.eye(dx) * jnp.exp(-1 / ell * dt)
trans_cov = sigma ** 2 * (1 - jnp.exp(-2 / ell * dt)) * jnp.eye(dx)
model = json.loads(Path(PF_ARGS["model_path"]).read_text())
nparticles = 64
pf_key = jax.random.PRNGKey(2026)


def m0_sampler(key_, _):
    rnds = jax.random.normal(key_, shape=(nparticles, dx))
    return m0 + rnds @ jnp.linalg.cholesky(v0).T


def log_g0(samples_, y0):
    return jnp.sum(jax.scipy.stats.norm.logpdf(y0, samples_ @ obs_op.T, xi ** 0.5), axis=-1)


def m_log_g(key_, samples_, pytree):
    y = pytree
    rnds = jax.random.normal(key_, shape=(nparticles, dx))
    prop_samples = samples_ @ semigroup.T + rnds @ (trans_cov ** 0.5).T
    log_potentials = jnp.sum(jax.scipy.stats.norm.logpdf(y, prop_samples @ obs_op.T, xi ** 0.5), axis=-1)
    return log_potentials, prop_samples


ys_used = jnp.asarray(ys_fix).reshape(-1)
sampless, log_wss, nll_ref, esss = smc_feynman_kac(pf_key, m0_sampler, log_g0, m_log_g, ys_used, nparticles, nsteps,
                                                   resampling=multinomial, resampling_threshold=1.,
                                                   return_path=True)
_, _, kf_nll_ref, *_ = kf(ys_used[:, None], m0, v0, semigroup, trans_cov, obs_op, jnp.eye(dy) * xi)
c2 = {"tool_args": PF_ARGS, "N": nparticles,
      "prng_key_matches_PRNGKey2026": [int(v) for v in np.asarray(pf_key)] == PF_KEY,
      "fixture_ys_equal_test_ys_bitwise": bool(np.array_equal(np.asarray(ys_fix).reshape(-1), np.asarray(ys_test))),
      "fixture_F_minus_test_semigroup": float(model["F"][0][0] - float(semigroup[0, 0])),
      "fixture_Q_minus_test_trans_cov": float(model["Q"][0][0] - float(trans_cov[0, 0])),
      "direct_upstream_nll": float(nll_ref), "direct_upstream_nll_plus_log_n": float(nll_ref) + float(np.log(nparticles)),
      "direct_upstream_kf_nll": float(kf_nll_ref)}
if not report["pf_call"]["is_error"]:
    data = report["pf_call"]["data"]
    o = np.load(data["artifacts"][0]["path"])
    c2.update({
        "artifact": data["artifacts"][0]["path"],
        "tool_nll": data["nll"], "tool_nll_plus_log_n": data["nll_plus_log_n"],
        "abs_diff_nll": abs(data["nll"] - float(nll_ref)),
        "max_abs_diff_final_samples": float(np.max(np.abs(o["samples"] - np.asarray(sampless[-1])))),
        "max_abs_diff_final_log_weights": float(np.max(np.abs(o["log_weights"] - np.asarray(log_wss[-1])))),
        "max_abs_diff_ess": float(np.max(np.abs(o["ess"] - np.asarray(esss)))),
        "bitwise_nll": data["nll"] == float(nll_ref),
    })
    c2["pass"] = bool(c2["abs_diff_nll"] <= 1e-12 * max(1., abs(float(nll_ref)))
                      and c2["max_abs_diff_final_samples"] <= 1e-12 and c2["max_abs_diff_ess"] <= 1e-9)
else:
    c2["pass"] = False
if not report["kf_call"]["is_error"]:
    c2["tool_kf_nll"] = report["kf_call"]["data"].get("nll")
    c2["abs_diff_kf_nll_tool_vs_direct"] = abs(c2["tool_kf_nll"] - float(kf_nll_ref))
    c2["pf_nll_plus_log_n_minus_kf_nll"] = c2.get("tool_nll_plus_log_n", float("nan")) - c2["tool_kf_nll"]
checks["particle_filter_changed_input"] = c2
report["checks"] = checks

# ---- import origins: import the extracted server module (without running it) and list module files ----
sys.path.insert(0, str(EXTRACTED / "src"))
import importlib  # noqa: E402

srvmod = importlib.import_module("diffres_mcp")
mods = {n: getattr(m, "__file__", None) for n, m in list(sys.modules.items())}
files = [f for f in mods.values() if f]
report["origins"] = {
    "diffres_file": diffres.__file__,
    "fastmcp_file": sys.modules["fastmcp"].__file__,
    "jax_file": jax.__file__,
    "server_module_file": srvmod.__file__,
    "tools_modules": {n: mods[n] for n in mods if n.startswith("tools.")},
    "n_loaded_module_files": len(files),
    "module_files_in_workspace_outside_extracted": sorted(f for f in files if f.startswith(WORKSPACE)
                                                          and not f.startswith(str(EXTRACTED))),
    "module_files_outside_extracted_and_uv_python": sorted(
        f for f in files if not f.startswith(str(EXTRACTED)) and not f.startswith("/home/jixia/.local/share/uv/python")),
    "sys_path": sys.path,
}
report["success"] = bool(c1["pass"] and c2["pass"]
                         and not report["origins"]["module_files_in_workspace_outside_extracted"]
                         and all(not s.get("mapped_files_under_workspace") for s in report["server_processes"]))
OUT.write_text(json.dumps(report, indent=1, default=str))
print(json.dumps({k: v for k, v in report.items() if k not in ("tool_schemas", "origins")}, indent=1, default=str)[:6000])
print("origins:", json.dumps({k: v for k, v in report["origins"].items() if k != "sys_path"}, indent=1)[:3000])
print("SUCCESS" if report["success"] else "FAILURE")
