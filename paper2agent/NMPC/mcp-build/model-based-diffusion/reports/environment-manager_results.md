# Environment manager results: model-based-diffusion (CLI route, Python backend)

Written 2026-10-02. All paths are relative to
`PROJECT_ROOT=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/model-based-diffusion` unless absolute.

## Outcome in brief

| Item | Result |
| --- | --- |
| Environment | created, `uv pip check` exit 0 (177 packages) |
| Research source | checkout at commit `c1eb913783f1713f7a1ebb657b34e0188d52cd8b`, imported from the checkout, checkout untouched |
| FastMCP 4.0.3 + pytest + pytest-asyncio | installed in the same environment; resolver accepted them after relaxing two utility pins (`rich`, `typing-extensions`) |
| GPU | `jax.devices()` = `[cuda(id=0)]`, RTX 4070 Laptop GPU, tiny jit ran on it |
| `--help` of the tyro scripts | exit 0 for `mbd_planner.py`, `path_integral.py`, `run_mbd.py` |
| **Feasibility probe** | **NOT ATTEMPTED** (memory gate, see "Feasibility probe"). No planner run, no timing, no GPU-memory figure exists yet. |
| Blocking findings for later stages | `path_integral.py` cannot run with the Brax version the main planner needs (see "Source/dependency disagreements") |

## Interpreter

- `PROJECT_ENV` = `model-based-diffusion-env/`, `PROJECT_PYTHON` = `model-based-diffusion-env/bin/python`
- `Python 3.11.17` (uv-managed CPython, `/home/jixia/.local/share/uv/python/cpython-3.11.17-linux-x86_64-gnu/bin/python3.11`), uv 0.12.22.
- Why 3.11: the repository states no Python version. The dependency set that matches the code's date
  (jax/jaxlib 0.4.30, mujoco 3.1.6: `>=3.9`/`>=3.8`; scipy 1.14.0 and gymnax 0.0.8: `>=3.10`) and FastMCP 4.0.3
  (`>=3.10`) both support 3.11. 3.10 was rejected because it reaches end of life this month; 3.12 was rejected
  because `gputil` (declared in `setup.py`) imports `distutils`, which 3.12 removed. Only 3.11 was tested.

## Setup attempts (limit three)

1. Attempt 1: `uv pip install -r tmp/env-probe/resolved-full.txt` was interrupted during downloads by the host
   restart; nothing had been installed (`tmp/env-probe/install-attempt1.log`).
2. Attempt 2: same command, exit 0, 176 packages installed (`tmp/env-probe/install-attempt2.log`), followed by the
   checkout install, exit 0 (`tmp/env-probe/install-mbd.log`). This is the environment described here.

No third attempt was needed.

## How versions were chosen

`setup.py` pins nothing and omits packages the scripts import. Versions were resolved in two steps; both inputs
and outputs are kept in `tmp/env-probe/`.

**Step 1, dated snapshot of the scientific stack.**
`uv pip compile science.in --exclude-newer 2024-07-04T00:00:00Z -o science-snapshot-2024-07-04.txt` (exit 0, 111 pins).
The cut-off is the day after commit `d523ca3` (2024-07-03, "update arxiv"). The later commits up to the pinned one
(2025-03-27) only touch `README.md`, `mbd/notebooks/` and `mbd/scripts/vis_manim.py` (`git diff --stat d523ca3 HEAD`),
so the planners and environments are code of June 2024. `science.in` contains:

| Requirement | Source | Reason |
| --- | --- | --- |
| gym, pandas, seaborn, matplotlib, imageio, control, tqdm, tyro, meshcat, sympy, gymnax, distrax, gputil, jaxopt | `setup.py` `install_requires` | declared by the repository (unpinned) |
| `jax[cuda12]==0.4.30`, `jaxlib==0.4.30` | `setup.py` says plain `jax` | newest JAX at the cut-off (PyPI 2024-06-18); the `cuda12` extra gives the pip CUDA 12 wheels |
| `brax==0.10.5` | not in `setup.py`; imported by `mbd/envs`, `mbd/utils.py` | newest Brax at the cut-off (PyPI 2024-06-07). `mbd_planner.py` (changed 2024-06-12) calls `env.sys.tree_replace({"opt.timestep": ...})`, the Brax 0.10 `System` layout |
| `mujoco`, `mujoco-mjx` | not in `setup.py`; required by Brax | resolved to 3.1.6 (PyPI 2024-06-03) |
| `flax`, `etils` | not in `setup.py`; imported by `mbd/envs/*.py` | resolved to flax 0.8.5, etils 1.9.2 |
| `numpy<2` | added by me | NumPy 2.0.0 appeared on 2024-06-16, inside the window; the snapshot's compiled wheels date from the NumPy 1.x period, so I kept 1.26.4. NumPy 2 was not tested. |

**Step 2, add the MCP/test tools.**
`uv pip compile science.in mcp.in -c <snapshot pins>` with `mcp.in` = `fastmcp==4.0.3`, `pytest`, `pytest-asyncio`.

- With all 111 snapshot pins as constraints the resolver failed (exit 1, `compile-full-try1.log`):
  `fastmcp-slim==4.0.3` needs `rich>=13.9.4` (snapshot: 13.7.1), then `mcp-types>=2.0.0` needs
  `typing-extensions>=4.13.0` (snapshot: 4.12.2).
- Removing only those two pins (`constraints-science.txt`, 109 pins) resolved (exit 0, `resolved-full.txt`, 176 pins,
  sha256 `eba3a2b5e7568a63ff716acce6d29ff06b8853bc896dd99ce0f5e5b603757a89`). The other 109 snapshot versions are unchanged.
  `rich` became 15.0.0 and `typing-extensions` 4.16.0. Both are general utilities; `tyro 0.8.5` (which uses rich for
  help output) was checked with the `--help` runs below. FastMCP stayed at the 4.0.3 baseline, so the conflict
  procedure for choosing another FastMCP version was not needed.

Installed versions that matter (full list: `reports/environment-requirements.txt`, 177 lines, sha256 `b788f74c...8f77`):

| Package | Version | Package | Version |
| --- | --- | --- | --- |
| jax / jaxlib | 0.4.30 | brax | 0.10.5 |
| jax-cuda12-plugin / jax-cuda12-pjrt | 0.4.30 | mujoco / mujoco-mjx | 3.1.6 |
| nvidia-cudnn-cu12 | 9.2.0.82 | flax | 0.8.5 |
| nvidia-cublas-cu12 | 12.5.3.2 | optax | 0.2.2 |
| nvidia-cuda-runtime/cupti/nvcc-cu12 | 12.5.82 | chex | 0.1.86 |
| nvidia-cufft-cu12 | 11.2.3.61 | numpy | 1.26.4 |
| nvidia-cusolver-cu12 | 11.6.3.83 | scipy | 1.14.0 |
| nvidia-cusparse-cu12 | 12.5.1.3 | matplotlib | 3.9.0 |
| nvidia-nccl-cu12 | 2.22.3 | tyro | 0.8.5 |
| nvidia-nvjitlink-cu12 | 12.5.82 | tqdm | 4.66.4 |
| fastmcp | 4.0.3 | mcp / mcp-types | 2.2.0 |
| pydantic | 2.13.5 | pytest / pytest-asyncio | 9.1.1 / 1.4.0 |
| gym | 0.26.2 | gymnax 0.0.8, distrax 0.1.5, jaxopt 0.8.3, gputil 1.4.0 | (declared, not imported by the scripts) |

Only this one combination was installed and checked. No other JAX/Brax pair was tried.

## Research package identity and the install method that works

`setup.py` has `find_packages(include="mdb")`. The string is treated as the patterns `m`, `d`, `b`, which match no
package, so the distribution contains **no Python package**. Tested on throwaway copies (`git archive HEAD`) outside
the project, with setuptools 84.0.0:

| Method | `find_spec("mbd")` | Files left in the source tree |
| --- | --- | --- |
| `uv pip install <src>` (normal) | `None`: only `mbd-0.0.1.dist-info`, no code | `build/`, `mbd.egg-info/` |
| `uv pip install -e <src>` (default editable) | `None`: finder installed with empty `MAPPING` | `mbd.egg-info/` |
| `uv pip install -e <src> --config-settings editable_mode=compat` | resolves to `<src>/mbd/__init__.py` (plain `.pth` with the source root) | `mbd.egg-info/` |
| the same with `DIST_EXTRA_CONFIG` pointing `[egg_info] egg_base` elsewhere | resolves to `<src>/mbd/__init__.py` | none |

Method used on the real checkout (exit 0, checkout not edited, nothing written into it):

```bash
# tmp/env-probe/dist-extra.cfg:      [egg_info]  egg_base = <PROJECT_ROOT>/tmp/env-probe/build-egg-base
# tmp/env-probe/build-constraints.txt:  setuptools==84.0.0
DIST_EXTRA_CONFIG="$PROJECT_ROOT/tmp/env-probe/dist-extra.cfg" uv pip install --python "$PROJECT_PYTHON" \
  -c tmp/env-probe/resolved-full.txt --build-constraints tmp/env-probe/build-constraints.txt \
  --config-settings editable_mode=compat -e repo/model-based-diffusion
```

Result:

- `model-based-diffusion-env/lib/python3.11/site-packages/__editable__.mbd-0.0.1.pth` contains the single line
  `<PROJECT_ROOT>/repo/model-based-diffusion`; `mbd-0.0.1.dist-info/direct_url.json` records that directory as editable;
  `WHEEL` says `Generator: setuptools (84.0.0)`.
- `uv pip freeze` lists it as `-e file:///home/jixia/AI_agents/paper2agent/NMPC/mcp-build/model-based-diffusion/repo/model-based-diffusion`.
  This is an absolute local path: it identifies the checkout but is not portable, so stage 5 needs its own
  documented install line (commit `c1eb913783f1713f7a1ebb657b34e0188d52cd8b` plus the `.pth`/compat mechanism).
- Distribution version is `0.0.1` (`setup.py`) while `mbd.__version__` is `0.1.0` (`mbd/__init__.py`); both come from upstream.
- `cd repo/model-based-diffusion && git rev-parse HEAD` = `c1eb913783f1713f7a1ebb657b34e0188d52cd8b`;
  `git status --porcelain --ignored` printed nothing after every step in this report.

Note for anyone repeating this: `editable_mode=compat` is a setuptools transition feature. It worked with 84.0.0;
other setuptools versions were not tested.

## Checks (commands and exit statuses)

Common environment for the Python checks: `XLA_PYTHON_CLIENT_PREALLOCATE=false PYTHONDONTWRITEBYTECODE=1 MPLBACKEND=Agg`,
run under `flock /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/.heavy.lock`. Checks marked CPU also had
`JAX_PLATFORMS=cpu` to keep host memory low. Logs are in `tmp/env-probe/`.

| # | Command (from the project root unless stated) | Exit | Log |
| --- | --- | --- | --- |
| 1 | `uv pip check --python "$PROJECT_PYTHON"` → "Checked 177 packages ... All installed packages are compatible" | 0 | `pip-check.log` |
| 2 | `uv pip freeze --python "$PROJECT_PYTHON" > reports/environment-requirements.txt` | 0 | the file |
| 3 | `"$PROJECT_PYTHON" --version > reports/python-version.txt` → `Python 3.11.17` | 0 | the file |
| 4 | `cd / && "$PROJECT_PYTHON" tmp/env-probe/check_imports.py` (CPU) | 0 | `check_imports.log` |
| 5 | `"$PROJECT_PYTHON" repo/model-based-diffusion/mbd/planners/mbd_planner.py --help` (CPU) | 0 | `help-mbd_planner.log` |
| 6 | `"$PROJECT_PYTHON" repo/model-based-diffusion/mbd/planners/path_integral.py --help` (CPU) | 0 | `help-path_integral.log` |
| 7 | `"$PROJECT_PYTHON" repo/model-based-diffusion/mbd/scripts/run_mbd.py --help` (CPU) | 0 | `help-run_mbd.log` |
| 8 | `"$PROJECT_PYTHON" tmp/env-probe/check_flags.py` (CPU; parses argument spellings with the scripts' own `Args`, runs no planner) | 0 | `check_flags.log` |
| 9 | `"$PROJECT_PYTHON" tmp/env-probe/check_device.py` (GPU) | 0 | `check_device.log` |
| 10 | `"$PROJECT_PYTHON" tmp/env-probe/check_env_api.py` (CPU; builds each environment object, no rollout) | 0 | `check_env_api.log` |
| 11 | `"$PROJECT_PYTHON" tmp/env-probe/check_foreign_modules.py` (CPU) | 0 | `check_foreign_modules.log` |
| 12 | `"$PROJECT_PYTHON" -m pytest -c pytest.ini --rootdir . -p no:cacheprovider tmp/env-probe/test_fastmcp_smoke.py -v` → 1 passed, in the login shell and with `env -u PYTHONPATH` | 0 / 0 | `pytest-smoke-rosenv.log`, `pytest-smoke-clean.log` |

`mbd/blackbox/mbd_opt.py --help` was **not run**: the file imports tyro but never calls it and has no argument
parsing. By reading the source, any invocation executes the whole experiment (module-level constants `dim = 800`,
`Nexp = 6`, `Nsample = 64`, `Ndiffuse = 100`) and then calls `jnp.save` into
`<checkout>/results/bbo/Rastrigin-800d_MBD.npy` without creating that directory. That behaviour is read from the
code, not observed.

Import origins (check 4): jax 0.4.30, jaxlib 0.4.30, brax 0.10.5, mujoco 3.1.6, mujoco.mjx 3.1.6, flax 0.8.5,
optax 0.2.2, numpy 1.26.4, scipy 1.14.0, tyro 0.8.5, matplotlib 3.9.0, etils 1.9.2, tqdm 4.66.4, fastmcp 4.0.3,
pytest 9.1.1, pytest_asyncio 1.4.0 all load from `model-based-diffusion-env/lib/python3.11/site-packages/`.
`mbd`, `mbd.envs`, `mbd.planners`, `mbd.planners.mbd_planner`, `mbd.planners.path_integral` load from
`repo/model-based-diffusion/mbd/...`; `mbd.assets` (a data directory without `__init__.py`) resolves as a namespace
package at `repo/model-based-diffusion/mbd/assets` and contains `car2d_xref.npy`, `cartpole.xml`, `humanoidrun.xml`,
`humanoidstandup.xml`, `humanoidtrack.xml`, `jog_xref.pkl`, `pushT.xml`, `walk_xref.pkl`.

## Device configuration

- `nvidia-smi`: NVIDIA GeForce RTX 4070 Laptop GPU, 8188 MiB, driver 581.04 (WSL2). The Windows desktop already
  holds about 1.0 to 1.5 GiB of it (readings between 1032 and 1480 MiB during this session).
- Check 9 output: `jax.devices(): [cuda(id=0)]`, `jax.default_backend(): gpu`, device kind
  `NVIDIA GeForce RTX 4070 Laptop GPU`; a jitted `sqrt(...).sum()` over 1e6 floats ran on `cuda(id=0)`;
  backend start plus that jit took 15.0 s; GPU memory in use went from 1280 to 1385 MiB; host peak RSS 391 MiB.
- So GPU JAX from the pip CUDA 12 wheels works here. This says nothing yet about the planner at real sizes.
- CPU fallback (`JAX_PLATFORMS=cpu`) imports and builds all environments (checks 4, 10).

## Machine-specific finding: ROS 2 leaks into the shell

The login shell sources ROS 2 Jazzy and exports
`PYTHONPATH=/opt/ros/jazzy/opt/gz_math_vendor/lib/python:/opt/ros/jazzy/lib/python3.12/site-packages` (plus an
`LD_LIBRARY_PATH` with ROS libraries).

- Effect observed: a plain `"$PROJECT_PYTHON" -m pytest ...` crashed at start-up (exit 1, `pytest-smoke.log`) because
  pytest auto-loaded the ROS `launch_testing` plugin from that path (`ModuleNotFoundError: No module named 'lark'`).
- No scientific import was affected: with that `PYTHONPATH` present, 1646 modules were loaded by
  `import mbd` plus the planners and none came from outside the environment, the standard library or the checkout (check 11).
- Handling: `pytest.ini` blocks the seven ROS pytest plugins by name, so the documented test command works in this
  shell. For child processes started by the wrapper I recommend removing `PYTHONPATH` from the child environment
  (`run_probe.sh` does this with `unset PYTHONPATH`).

## pytest configuration

`pytest.ini` (project root, `[pytest]` section) was needed and written:

```ini
[pytest]
testpaths = tests/code
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
addopts = -p no:launch_testing -p no:launch_ros -p no:ament_flake8 -p no:ament_copyright -p no:ament_pep257 -p no:ament_xmllint -p no:ament_lint
```

Reasons: the ROS plugin crash above, and pytest-asyncio 1.4.0 defaults to strict mode, where unmarked
`async def test_...` functions are not run. Verified with a throwaway in-memory FastMCP test
(`tmp/env-probe/test_fastmcp_smoke.py`: `FastMCP`, `@mcp.tool()`, `Client(server)`, `await client.call_tool`,
`result.data == 5`), 1 passed. That test checks the tooling only; it is not scientific evidence and is not in `tests/code`.

## CLI contract observed (tyro 0.8.5)

- Help shows hyphenated flags (`--env-name`, `--not-render`, `--disable-recommended-params`, `--enable-demo`,
  `--temp-sample`) and keeps the capitals of `--Nsample`, `--Hsample`, `--Ndiffuse`, `--beta0`, `--betaT`.
  Booleans are flag pairs (`--not-render` / `--no-not-render`).
- The README's underscore spellings are accepted: `--env_name car2d --not_render --disable_recommended_params
  --Nsample 64 --Ndiffuse 5` parsed to the expected `Args` (check 8).
- README spellings that this commit **rejects** (tyro exit 2):
  - `mbd_planner.py --enable_demos`: the field is `enable_demo` ("Unrecognized options: --enable-demos").
  - `path_integral.py --mode MODE`: the field is `update_method` ("Unrecognized options: --mode").
- `mbd_planner.py` environment names accepted by `mbd.envs.get_env`: `ant`, `halfcheetah`, `hopper`, `walker2d`,
  `humanoidrun`, `humanoidstandup`, `humanoidtrack`, `pushT`, `car2d`, `cartpole`.
- Recommended overrides applied unless `--disable_recommended_params` (from the source): `temp_sample` per
  environment; `Ndiffuse` 200 for `pushT` and 300 for `humanoidrun`; `Nsample` 8192 for `humanoidrun`;
  `Hsample` 40 for `pushT`. They overwrite values given on the command line for those environments.

## Where the scripts write

`mbd_planner.py` builds `path = f"{mbd.__path__[0]}/../results/{env_name}"`, which with this install is
`repo/model-based-diffusion/results/<env_name>/`, **inside the checkout**, and there is no output-directory argument.
Unless `--not_render` is given it creates the directory and writes `mu_0ts.npy`, plus `rollout.png` for `car2d` or
`rollout.html` for every other environment. With `--not_render` it writes nothing and only prints
`final reward = ...`. The directory does not exist at present. `results/` is listed in the checkout's `.gitignore`, so
`git status --porcelain` would stay empty even if files appear; use `git status --porcelain --ignored` to see them.
The same `results/` location is used by `mbd/scripts/vis_diffusion.py`, `mbd/rl/train_brax.py`,
`mbd/blackbox/mbd_opt.py` and `mbd/envs/pushT.py` (read from source). All of this is from reading the code; no
output file has been produced yet.

Python would also write `__pycache__/` directories into the checkout on import (git-ignored). Every command in
this report set `PYTHONDONTWRITEBYTECODE=1`, and the checkout contains none.

## Source/dependency disagreements found (check 10, Brax 0.10.5)

| Environment | Built | `env.sys.tree_replace({"opt.timestep": env.dt})` (`mbd_planner.py` line 174, render path) | `env.sys.replace(dt=env.dt)` (`path_integral.py` lines 100-101) |
| --- | --- | --- | --- |
| ant, halfcheetah, hopper, walker2d, humanoidrun, humanoidstandup, humanoidtrack, pushT | yes | ok | `TypeError: System.__init__() got an unexpected keyword argument 'dt'` |
| car2d | yes | not applicable (`Car2d` has no `sys`; the planner has a separate car2d branch) | `AttributeError: 'Car2d' object has no attribute 'sys'` |
| cartpole (not in the README list) | **no**: `TypeError ... unexpected keyword argument 'dt'` in `mbd/envs/cartpole.py` line 18 | | |

Consequences, stated with their evidence level:

- `path_integral.py` evaluates `env.sys.replace(dt=env.dt)` unconditionally before optimisation starts, so with
  Brax 0.10.5 I expect it to fail for every environment. I reproduced the failing call in isolation; I did not run
  `path_integral.py` itself beyond `--help`.
- A static look at the Brax 0.9.4 wheel (downloaded and unzipped outside the project, not installed) shows `System`
  with a `dt` field and no `opt`, so `path_integral.py` and `cartpole.py` appear to be written for the older Brax
  layout and `mbd_planner.py`'s render call for the newer one. No single Brax release was found that satisfies both;
  Brax 0.9.x was not installed or run.
- I did not change the source. The coordinator should treat `path_integral.py` (and `run_mbd.py --algo path_integral`)
  as blocked in this environment unless a second environment with an older Brax is wanted.

## Feasibility probe: NOT ATTEMPTED

The coordinator's rule was to run the probe only if `free -m` shows at least 3000 MB "available" immediately
before. It never did. Readings during this session (MB available): 942, 601, 1211, 1180, 1909, 1694, 1561, 1327,
1280, 1784, 1467, 1227, 866, 1188, 1259; swap was between 1.2 and 2.0 GiB used of 2.0 GiB. The memory is held by other
processes on the laptop (VS Code server and Pylance about 4.4 GiB RSS, other agent sessions).

Therefore there is **no measurement** of wall time, JIT time, GPU memory or reward for any planner run, and no
statement can be made yet about whether Nsample 2048 / Ndiffuse 100, or `humanoidrun` with Nsample 8192 /
Ndiffuse 300, are feasible on this machine. The only host-memory figures available are from the light checks:
391 MiB peak RSS for GPU start plus a tiny jit, 799 MiB peak RSS for building all ten environments on CPU.

Prepared runner: `tmp/env-probe/run_probe.sh LABEL TIMEOUT_SECONDS [mbd_planner.py arguments]` (with helper
`tmp/env-probe/stamp_stderr.py`). It runs the unmodified script from `repo/model-based-diffusion/mbd/planners`
as the README does, takes the heavy lock, sets `XLA_PYTHON_CLIENT_PREALLOCATE=false`, refuses to start below
`MIN_AVAIL_MB` (default 3000, checked after the lock is acquired; exit 75 when skipped), and writes
`tmp/env-probe/probe-LABEL/meta.txt` with exit status, wall seconds, peak host RSS, minimum host available memory,
whole-GPU memory baseline/peak (sampled every 0.5 s; WSL2 gives no per-process figure), seconds to the first finished
diffusion step (imports + environment build + JIT + one step) and steady seconds per diffusion step. It lists every
file that appears in the checkout and, with `CLEAN=1`, removes exactly those files and the then-empty directories it
created.

What has and has not been tested of the runner: its mechanics were exercised with `--help` only (exit 0, no file
created in the checkout, `tmp/env-probe/probe-mechanics-help/`), the memory gate was exercised (exit 75 at 1213 MB),
and the step-timing helper was checked against synthetic tqdm loops with known step times (0.3 s, 0.02 s, 0.004 s
recovered). It has never run a real planner job, so its parsing of the real script's progress output is unconfirmed.

Suggested order, smallest first; stop and reduce `--Nsample`/`--Ndiffuse` if any step is killed or the GPU runs out:

```bash
cd /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/model-based-diffusion
# 1. tiny, with rendering: confirms the output files (expected: results/car2d/mu_0ts.npy and rollout.png)
CLEAN=1 tmp/env-probe/run_probe.sh car2d-small 900 --env_name car2d --Nsample 256 --Ndiffuse 20
# 2. small Brax case, no files written
tmp/env-probe/run_probe.sh ant-small 1200 --env_name ant --Nsample 256 --Ndiffuse 10 --not_render
# 3. small Brax case with rendering: confirms rollout.html and the tree_replace render path end to end
CLEAN=1 tmp/env-probe/run_probe.sh ant-small-render 1200 --env_name ant --Nsample 256 --Ndiffuse 10
# 4. script defaults for ant (Nsample 2048, Ndiffuse 100)
tmp/env-probe/run_probe.sh ant-default 1800 --env_name ant --not_render
# 5. humanoidrun at its recommended sample count but only 4 diffusion steps, to read memory and time per step
tmp/env-probe/run_probe.sh humanoidrun-8192x4 1800 --env_name humanoidrun --disable_recommended_params --Nsample 8192 --Ndiffuse 4 --temp_sample 0.1 --not_render
```

The equivalent bare command for case 2, without the runner:

```bash
cd /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/model-based-diffusion/repo/model-based-diffusion/mbd/planners && \
XLA_PYTHON_CLIENT_PREALLOCATE=false PYTHONDONTWRITEBYTECODE=1 MPLBACKEND=Agg env -u PYTHONPATH \
flock /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/.heavy.lock timeout 1200 \
/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/model-based-diffusion/model-based-diffusion-env/bin/python \
mbd_planner.py --env_name ant --Nsample 256 --Ndiffuse 10 --not_render
```

Things to keep in mind when reading probe results (from the source, not measured):

- The loop runs `Ndiffuse - 1` reverse steps; each step rolls out `Nsample` trajectories of `Hsample` (default 50)
  environment steps and keeps every pipeline state, so GPU memory grows with `Nsample x Hsample`.
- After the loop the script compiles a second, non-vmapped rollout to print the final reward, and with rendering it
  steps the environment `Hsample` times through a third jitted function.
- `--Ndiffuse` below 2 gives an empty loop.

## Unresolved requirements and limits

1. Feasibility probe not run (memory gate). Stage 2 problem sizes are undecided.
2. `path_integral.py`, `run_mbd.py --algo path_integral` and the `cartpole` environment are incompatible with
   Brax 0.10.5 as described above. Not fixed, source untouched.
3. README flag names `--enable_demos` and `--mode` do not exist at this commit (`--enable_demo`, `--update_method`).
4. Outputs go into the checkout (`repo/model-based-diffusion/results/`); the wrapper has to collect and remove
   them per call, or always pass `--not_render` and return only the printed reward.
5. The editable install records an absolute local path; stage 5 needs a portable install description.
6. `gym`, `pandas`, `seaborn`, `control`, `meshcat`, `sympy`, `gymnax`, `distrax`, `gputil`, `jaxopt` are installed
   because `setup.py` declares them; no script in the checkout imports them, and they were not import-tested.
   `mbd/scripts/vis_manim.py` needs `manim` and `mbd/notebooks/01_1d_demo.py` needs `scienceplots`; neither is
   declared by `setup.py` and neither was installed.
7. `mbd/blackbox/mbd_mnist.py` downloads MNIST with `urllib` (read from source); not run.
8. Only Python 3.11.17 with the versions listed here was tested. NumPy 2, newer JAX/Brax and other Python versions
   are untested.

## Files written by this role

- `model-based-diffusion-env/` (3.7 GB)
- `pytest.ini`
- `reports/environment-manager_results.md`, `reports/environment-requirements.txt`, `reports/python-version.txt`
- `tmp/env-probe/`: resolver inputs/outputs (`science.in`, `mcp.in`, `science-snapshot-2024-07-04.txt`,
  `constraints-science.txt`, `resolved-full.txt`, `compile-*.log`), install logs, `dist-extra.cfg`,
  `build-constraints.txt`, `build-egg-base/mbd.egg-info/`, check scripts and logs, `run_probe.sh`,
  `stamp_stderr.py`, `test_fastmcp_smoke.py`, `probe-mechanics-help/`

Nothing was written inside `repo/model-based-diffusion`.
