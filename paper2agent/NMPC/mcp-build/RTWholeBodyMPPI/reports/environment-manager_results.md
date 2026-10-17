# Environment manager results: RTWholeBodyMPPI

- Date: 2026-10-12. Role: Python environment manager (route `python`), attempt 1.
- **Status: PARTIAL.** The environment is created, installed, resolver-consistent and checked with
  everything that does not import `mujoco`, `mujoco_viewer` or `whole_body_mppi`. Those imports count as
  heavy jobs, and heavy jobs are disabled (`mcp-build/HEAVY_JOBS_DISABLED`, heavy.sh exits 75), so their checks
  were **not attempted: heavy jobs disabled**. The exact commands to run them later are in section 8.
- A successful import, which has not even been tried yet, would still not be scientific validation.

## 1. Interpreter and environment

| Item | Value |
|---|---|
| `PROJECT_ENV` | `/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/RTWholeBodyMPPI/RTWholeBodyMPPI-env` |
| `PROJECT_PYTHON` | `/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/RTWholeBodyMPPI/RTWholeBodyMPPI-env/bin/python` |
| Python | CPython 3.11.17 (uv-managed, `/home/jixia/.local/share/uv/python/cpython-3.11.17-linux-x86_64-gnu`), `include-system-site-packages = false` |
| Created with | `uv venv --python /home/jixia/.local/share/uv/python/cpython-3.11-linux-x86_64-gnu/bin/python3.11 RTWholeBodyMPPI-env` (uv 0.12.22), exit 0 |
| Size | 398 MB |

Why 3.11: the README asks for Python >= 3.9 (`setup.py`: `python_requires=">=3.8"`), and the authors' notebooks record
Python 3.8.10. FastMCP 4 needs >= 3.10, and mujoco 3.1.6 publishes cp38-cp312 wheels (cp311 manylinux2014 x86_64 used).
3.11 is also the version used elsewhere in this workspace.

**Shell caveat:** the login shell exports a ROS 2 Jazzy `PYTHONPATH`
(`/opt/ros/jazzy/opt/gz_math_vendor/lib/python:/opt/ros/jazzy/lib/python3.12/site-packages`). Every command
below ran with `env -u PYTHONPATH`, and later stages must do the same (heavy.sh removes it itself).

## 2. Package and source identity

- Source: `repo/RTWholeBodyMPPI` at commit `55e6dc35d042ed5f175ad6ae312c886282f32529` (`git rev-parse HEAD`, checked
  after the install). MIT licence. Scope: `legged_mppi/` (distribution `whole_body_mppi` 1.0, top-level package `whole_body_mppi`).
- Install: editable, as in the README (`cd legged_mppi && pip install -e .`), via
  `uv pip install --python $PROJECT_PYTHON -c tmp/env/constraints.txt -e repo/RTWholeBodyMPPI/legged_mppi PyYAML Pillow 'fastmcp==4.0.3' pytest pytest-asyncio`
  (exit 0, 96 packages; log `tmp/env/04_install.log`). Build backend: setuptools (from `pyproject.toml`), PEP 660 editable wheel.
- Origin checks, none of which imports the package:
  - `uv pip show whole-body-mppi` -> `Version: 1.0`,
    `Editable project location: /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/RTWholeBodyMPPI/repo/RTWholeBodyMPPI/legged_mppi`.
  - `whole_body_mppi-1.0.dist-info/direct_url.json` ->
    `{"url":"file:///home/jixia/AI_agents/paper2agent/NMPC/mcp-build/RTWholeBodyMPPI/repo/RTWholeBodyMPPI/legged_mppi","dir_info":{"editable":true}}`.
  - The `.pth` is setuptools' static finder: `__editable__.whole_body_mppi-1.0.pth` runs
    `__editable___whole_body_mppi_1_0_finder.install()`. The finder file (sha256 `b2287c99c1b043ad21ce1b116e96d85245e8d448542b8a0d6e2a07c5fc1cf0ed`)
    contains `MAPPING = {'whole_body_mppi': '<PROJECT_ROOT>/repo/RTWholeBodyMPPI/legged_mppi/whole_body_mppi'}` and `NAMESPACES = {}`.
  - `importlib.util.find_spec('whole_body_mppi')` (top-level spec lookup only; module code is not executed) ->
    origin `<PROJECT_ROOT>/repo/RTWholeBodyMPPI/legged_mppi/whole_body_mppi/__init__.py`, loader `SourceFileLoader`.
    `mujoco` and `mujoco_viewer` resolve to `RTWholeBodyMPPI-env/lib/python3.11/site-packages/{mujoco,mujoco_viewer}/__init__.py`
    (`tmp/env/05_light_imports.json`).
- Subfolders without `__init__.py` (`control/controllers`, `control/gait_scheduler`): the finder maps only the top-level
  package, so submodules are found through `whole_body_mppi.__path__` in the source tree. These two folders then load
  as implicit namespace packages from the source tree, as in the README's editable install. All four existing `__init__.py`
  files (`whole_body_mppi/`, `control/`, `interface/`, `utils/`) are empty. This is from reading the files only; the import itself is deferred (section 8).
- Data files load relative to `__file__` and are present under the mapped source path: 7 controller configs
  (`control/controllers/configs`), 63 gait TSVs (`control/gait_scheduler/gaits/{SLOW,MED,FAST}`),
  `interface/configs/simulator.yml`, `models/common.xml`, 13 `models/go1/*.xml` files (robot and scene models), and `models/go1/assets`.
- Repository state after the install: `git status --porcelain` is empty (no tracked change). `git status --porcelain --ignored`
  shows only `!! legged_mppi/whole_body_mppi.egg-info/`, which setuptools writes during the editable build (first created by the
  dry run). It is covered by the repo's `.gitignore` (`*.egg-info/`). There are no `__pycache__`/`build/` directories in the repo,
  because nothing from it was imported.

## 3. Dependency resolution

Upstream `legged_mppi/requirements.txt`: `mujoco==3.1.6`, `scipy`, `numpy`, `mujoco-python-viewer==0.1.4`, `matplotlib`,
`tqdm==4.66.5`. PyYAML and Pillow (imported by `base_controller.py`/`mppi_*.py` and `simulator.py` but not listed) were
installed explicitly. They are also transitive: `pyyaml` is required by `mujoco-python-viewer` (and `jsonschema-path`),
and `pillow` by `matplotlib` and `imageio`.

**Explicit constraint `numpy<2`** (`tmp/env/constraints.txt`, sha256 `c1bda44f...`). This is an environment choice, not an upstream requirement.
- Unconstrained, the resolver picks numpy 2.4.6 (`tmp/env/02_dryrun.log`).
- The mujoco 3.1.6 cp311 wheel was uploaded on 2024-06-03 (PyPI sha256 `8bff14511ec5924b457dcae8c4bf403a7fbaa6fcecee0f3d2e92b83af2c2d5c3`;
  not compared with the installed files). That is before numpy 2.0.0 (first upload 2024-06-16). mujoco's metadata says only `numpy`.
- The authors' notebooks record Python 3.8.10, which means numpy <= 1.24.
- The extensions `_functions/_render/_rollout/_structs` contain both `numpy._core` and `numpy.core` strings (pybind11 `internals_v4`),
  which suggests they might also load under numpy 2. That is untested, and it cannot be tested while mujoco imports are disabled.
  So the env stays on numpy 1.26.4, which resolves with everything else (`tmp/env/03_dryrun_numpy1.log`).
- A grep of the in-scope `.py`/`.ipynb` files for numpy-2-removed aliases (`np.float`, `np.product`, `np.in1d`, `np.trapz`, `np.NaN`, `np.core`, ...) found nothing.

Key resolved versions (full snapshot: `reports/environment-requirements.txt`, 96 lines, `uv pip freeze`, sha256 `05fd5270...`):

| Package | Version | Note |
|---|---|---|
| whole_body_mppi | 1.0 | editable, `-e file:///.../repo/RTWholeBodyMPPI/legged_mppi` @ 55e6dc3 |
| mujoco | 3.1.6 | pinned upstream |
| mujoco-python-viewer | 0.1.4 | pinned upstream |
| tqdm | 4.66.5 | pinned upstream |
| numpy | 1.26.4 | constrained `<2` (see above) |
| scipy | 1.17.1 | unpinned upstream |
| matplotlib | 3.11.2 | unpinned upstream; backend `Agg` with `MPLBACKEND=Agg` |
| PyYAML | 6.0.3 | not listed upstream |
| Pillow | 12.3.0 | not listed upstream |
| glfw | 2.10.2 | from mujoco / mujoco-python-viewer; bundles `glfw/x11/libglfw.so` and `glfw/wayland/` |
| PyOpenGL | 3.1.10 | from mujoco |
| imageio | 2.38.1 | from mujoco-python-viewer |
| fastmcp | 4.0.3 | tested baseline from runtime.md; resolved with no conflict (`fastmcp-slim` 4.0.3, `mcp` 2.3.0, `pydantic` 2.14.1) |
| pytest | 9.1.1 | |
| pytest-asyncio | 1.4.0 | |

No Jupyter kernel, papermill or ipykernel was installed: the scanner's plan runs headless driver scripts that call
`Simulator(viewer=False)` / the extracted push-box loop. The notebooks are verification references only, with recorded outputs.
If the coordinator decides to execute notebooks, add `papermill nbclient ipykernel jupytext` and register a kernel inside the env only:
`$PROJECT_PYTHON -m ipykernel install --prefix $PROJECT_ENV --name RTWholeBodyMPPI --display-name "Python (RTWholeBodyMPPI)"`.

## 4. Checks performed (all run with `env -u PYTHONPATH`, from PROJECT_ROOT)

| # | Check | Command (abridged) | Exit | Result |
|---|---|---|---|---|
| 1 | Resolver consistency | `uv pip check --python $PROJECT_PYTHON` | 0 | "Checked 96 packages ... All installed packages are compatible" |
| 2 | Package origin | `uv pip show whole-body-mppi mujoco mujoco-python-viewer`; read `direct_url.json`, `.pth`, finder `MAPPING` | 0 | resolves to `repo/RTWholeBodyMPPI/legged_mppi` (section 2) |
| 3 | Light imports + spec-only lookups | `MPLBACKEND=Agg $PROJECT_PYTHON tmp/env/check_light_imports.py tmp/env/05_light_imports.json` | 0 | numpy, scipy (+`spatial.transform`, `interpolate`), yaml, PIL(+Image), matplotlib(+pyplot, backend Agg), tqdm, imageio, glfw, fastmcp, mcp, pydantic, pytest, pytest_asyncio, concurrent.futures, threading, argparse: all OK. A meta-path blocker refused mujoco/mujoco_viewer/whole_body_mppi/jax, and `sys.modules` was confirmed free of them |
| 4 | Same, without display | `env -u DISPLAY -u WAYLAND_DISPLAY -u XDG_SESSION_TYPE ... check_light_imports.py tmp/env/06_light_imports_nodisplay.json` | 0 | identical; `import glfw` loads `glfw/x11/libglfw.so` without a display (it does not call `glfwInit`) |
| 5 | FastMCP API surface | `$PROJECT_PYTHON -c 'inspect.signature(...)'` (`tmp/env/07_fastmcp_signatures.log`) | 0 | `FastMCP.mount(server, namespace=None, tool_names=None)`; `FastMCP.tool(..., timeout=None, run_in_thread=True)`; `Client.call_tool(name, arguments, ..., raise_on_error=True)` |
| 6 | pytest + FastMCP round trip | `$PROJECT_PYTHON -m pytest -c pytest.ini --rootdir . -s -q -p no:cacheprovider tmp/env/test_env_smoke.py` (`tmp/env/08_pytest_smoke.log`) | 0 | 2 passed: in-memory `Client(server)`, mounted namespace gives tool names `demo_describe`, `demo_norm`, `result.data` checks, error case `is_error`, no heavy modules loaded |
| 7 | Same, with the leaked ROS `PYTHONPATH` kept | same, without `env -u PYTHONPATH` (`tmp/env/09_pytest_smoke_rospath.log`) | 0 | 2 passed; the `-p no:` flags in pytest.ini block the 7 ROS `pytest11` plugins |
| 8 | pytest config discovery | `$PROJECT_PYTHON -m pytest --co` | 5 | `configfile: pytest.ini`, `testpaths: tests/code`; exit 5 = no tests collected (tests/code is empty for now) |
| 9 | CLI entry point | `RTWholeBodyMPPI-env/bin/fastmcp version` | 0 | FastMCP 4.0.3, MCP 2.3.0, Python 3.11.17. It reports "update available: 4.1.0", which is ignored (baseline stays 4.0.3). `whole_body_mppi` declares no console scripts |
| 10 | mujoco wheel native libraries (file listing + `readelf -d`, no execution) | see below | 0 | listed |
| 11 | Deferred-check script syntax | `$PROJECT_PYTHON -m py_compile tmp/env/check_heavy_imports.py` | 0 | compiles; **not run** |

mujoco 3.1.6 wheel contents (`site-packages/mujoco`): `libmujoco.so.3.1.6` (4.6 MB; NEEDED only libdl, libm, libc,
libpthread, ld-linux), the pybind extensions `_callbacks _constants _enums _errors _functions _render _rollout _simulate _structs`
(`.cpython-311-x86_64-linux-gnu.so`, NEEDED libmujoco + libc family only), and plugins `plugin/{libactuator,libelasticity,libsdf,libsensor}.so`.
`mujoco.rollout` (used by `base_controller.py`) is shipped (`_rollout`). No GL library is linked: GL is loaded at runtime according to
`MUJOCO_GL`. With `MUJOCO_GL` unset, `import mujoco` imports `gl_context` and selects the glfw backend without initialising it (from reading the source).

## 5. Headless / display findings (code reading; nothing executed)

- `mujoco_viewer/mujoco_viewer.py` 0.1.4 imports `mujoco, glfw, numpy, time, pathlib, yaml` at module level. `callbacks.py` also
  imports `imageio`. Importing it should not need a display. That has to be confirmed in the deferred check (section 8).
- `MujocoViewer.__init__` calls `glfw.init()` and `glfw.get_video_mode(glfw.get_primary_monitor())`. In `mode='offscreen'` it only sets
  `glfw.window_hint(glfw.VISIBLE, 0)` and still calls `glfw.create_window(...)`. This **confirms the scanner's expectation:
  offscreen rendering with mujoco-python-viewer needs a display (X11/Wayland)**. Constructing it also reads
  `~/.config/mujoco_viewer/config.yaml` if present. The tools' headless path (`Simulator(viewer=False)`, viewer-free loops) avoids this.
- System GL libraries (ldconfig): `libGL.so.1`, `libGLX.so.0`, `libGLX_mesa.so.0`, `libEGL.so.1` (Mesa), `libX11.so.6`, `libwayland-client.so.0`.
  There is no `libOSMesa`, and `ffmpeg` is not on PATH (so mp4 export is impossible, consistent with the scanner's exclusion).
  This shell has WSLg `DISPLAY=:0`/`WAYLAND_DISPLAY=wayland-0`, but per the assignment it is not relied on.

## 6. Devices

MuJoCo is CPU-only here: 16 CPU threads (`nproc`), and the controllers use thread pools (`n_workers` 5 or 15).
GPU: NVIDIA GeForce RTX 4070 Laptop GPU, 8188 MiB, driver 581.04 (1737 MiB in use at check time). The upstream code does not use it.
RAM at check time: 7532 MB total, about 2550-2690 MB available.

## 7. pytest configuration

`PROJECT_ROOT/pytest.ini` (sha256 `3840a5620b187a91735e89b759e8e46d7c203d34d2220df73a74aa311de85782`) uses `[pytest]`,
`testpaths = tests/code`, `asyncio_mode = auto` and `asyncio_default_fixture_loop_scope = function`. Its `addopts` blocks the ROS
plugins `launch_testing, launch_ros, ament_flake8, ament_copyright, ament_pep257, ament_xmllint, ament_lint`.
This matches the convention of the sibling projects in this workspace. Run tests as `env -u PYTHONPATH $PROJECT_PYTHON -m pytest tests/code/`.
Tests that import mujoco/whole_body_mppi must go through heavy.sh.

## 8. Deferred: not attempted (heavy jobs disabled)

These checks import mujoco / mujoco_viewer / whole_body_mppi and were **not attempted: heavy jobs disabled**. The driver
`tmp/env/check_heavy_imports.py` is ready: it compiles, but it has never been run. It imports mujoco (version, `mj_versionString`, `mujoco.rollout`,
and one `mj_step` of a 1-body model), imports `mujoco_viewer` and `glfw` without a display (it does not construct `MujocoViewer`), and imports
`whole_body_mppi`, the two namespace subpackages and all in-scope modules. It asserts that each `__file__`/`__path__` lies under
`repo/RTWholeBodyMPPI/legged_mppi/whole_body_mppi`, and with `--load-models` it compiles the stairs and push-box scenes. It runs no
controller and no simulation. Run it once heavy jobs are re-enabled, one job at a time:

```bash
cd /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/RTWholeBodyMPPI
/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh --limit-mb 1500 --timeout 300 \
    --log /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/RTWholeBodyMPPI/tmp/env/12_heavy_imports.log -- \
    env -u DISPLAY -u WAYLAND_DISPLAY -u XDG_SESSION_TYPE \
    /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/RTWholeBodyMPPI/RTWholeBodyMPPI-env/bin/python \
    /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/RTWholeBodyMPPI/tmp/env/check_heavy_imports.py \
    /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/RTWholeBodyMPPI/tmp/env/12_heavy_imports.json --load-models
```

The same checks as one-liners, if preferred (each through heavy.sh, no display):
- `heavy.sh -- env -u DISPLAY -u WAYLAND_DISPLAY -u XDG_SESSION_TYPE $PROJECT_PYTHON -c "import mujoco, numpy; from mujoco import rollout; print(mujoco.__version__, mujoco.mj_versionString(), numpy.__version__, mujoco.__file__)"`
- `heavy.sh -- env -u DISPLAY -u WAYLAND_DISPLAY -u XDG_SESSION_TYPE $PROJECT_PYTHON -c "import mujoco_viewer, glfw; print(mujoco_viewer.__file__)"` (headless import check)
- `heavy.sh -- env -u DISPLAY -u WAYLAND_DISPLAY -u XDG_SESSION_TYPE $PROJECT_PYTHON -c "import whole_body_mppi, whole_body_mppi.interface.simulator as s, whole_body_mppi.control.controllers.mppi_locomotion as l, whole_body_mppi.control.controllers.mppi_locomanipulation as p; print(whole_body_mppi.__file__, s.__file__, l.__file__, p.__file__)"`

heavy.sh refuses to start (exit 75) unless MemAvailable >= limit + 1500 MB. With `--limit-mb 1500` that is 3000 MB, and about 2550-2690 MB
was available during this session, so memory must also be freed first. After the check passes, refresh
`reports/environment-requirements.txt` only if packages change.

## 9. Unresolved items / blockers

1. **Blocker (external, unchanged): heavy jobs are disabled.** The mujoco / mujoco_viewer / whole_body_mppi imports, the headless
   `import mujoco_viewer` check and any simulation are unverified in this env. Do not retry until the coordinator removes `HEAVY_JOBS_DISABLED`.
2. numpy 1.26.4 is an explicit environment choice. numpy 2.x with mujoco 3.1.6 is untested and should not be described as validated.
3. The editable install leaves `legged_mppi/whole_body_mppi.egg-info/` (gitignored) in the source tree. This is inherent to `pip install -e` with this
   setuptools project. The tracked tree is unchanged.
4. For later stages (FastMCP 4): tools default to `run_in_thread=True`, and the upstream code `print()`s progress to stdout and shows tqdm on stderr.
   A stdio server must keep upstream stdout away from the protocol stream. `contextlib.redirect_stdout` is process-global, so the
   implementer should choose a thread-safe approach (e.g. redirect at file-descriptor level, or run each simulation in a subprocess).
5. Rendering/animation stays blocked: mujoco-python-viewer needs a display even offscreen, there is no OSMesa, and there is no ffmpeg (section 5).

## 10. Files

- Owned outputs: `reports/environment-manager_results.md` (this file), `reports/environment-requirements.txt`, `reports/python-version.txt`
  (`Python 3.11.17`), `pytest.ini`, `RTWholeBodyMPPI-env/`.
- Scratch evidence (`tmp/env/`): `01_uv_venv.log`, `02_dryrun.log`, `03_dryrun_numpy1.log`, `04_install.log`, `constraints.txt`,
  `check_light_imports.py`, `05_light_imports.{json,log}`, `06_light_imports_nodisplay.{json,log}`, `07_fastmcp_signatures.log`,
  `test_env_smoke.py`, `08_pytest_smoke.log`, `09_pytest_smoke_rospath.log`, `10_pytest_testpaths.log`, `11_fastmcp_version.log`,
  `check_heavy_imports.py` (deferred, not run).
