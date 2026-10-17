# Environment manager results: adaptive_linear_path_model_based_diffusion (CLI route, Python backend)

Written 2026-10-12. Paths are relative to
`PROJECT_ROOT=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/adaptive_linear_path_model_based_diffusion` unless absolute.

## Status: PARTIAL

The environment is installed and consistent (`uv pip check` exit 0, 150 packages). Every check that does not import
a heavy package passed. **Heavy jobs are disabled in this workspace** (`mcp-build/HEAVY_JOBS_DISABLED` exists;
`heavy.sh` exits 75), so the assignment forbids importing torch, jax, jaxlib, brax, flax, mujoco and moviepy and running
any repository script, including `--help`. Those checks are **not attempted: heavy jobs disabled**. Nothing below
shows that torch or JAX actually load or run on this machine. The commands to run later are in "Deferred checks".

| Item | Result |
| --- | --- |
| Environment | `adaptive_linear_path_model_based_diffusion-env/` created with uv 0.12.22, Python 3.11.17, 1.7 GB |
| Resolution / install | `uv pip compile` exit 0 (150 pins), `uv pip sync` exit 0 (150 installed), first attempt |
| `uv pip check` | exit 0, "Checked 150 packages ... All installed packages are compatible" |
| Light imports (numpy, matplotlib Agg, yaml, tqdm, pandas, wandb, fastmcp, mcp, pydantic, pytest, pytest_asyncio) | exit 0, all from the env's `site-packages`; no heavy module loaded or attempted |
| FastMCP 4.0.3 smoke test under pytest | 1 passed, with and without the ROS `PYTHONPATH` |
| torch / jax / brax / flax / mujoco / moviepy import, device check, tiny torch.compile, `--help` of the scripts | **not attempted: heavy jobs disabled** |
| Research source | checkout at `6c2b004132718a1c6fd54fb7946c2705baee6c5c`, used in place (not installable), untouched |

## Interpreter

- `PROJECT_ENV` = `PROJECT_ROOT/adaptive_linear_path_model_based_diffusion-env`
- `PROJECT_PYTHON` = `PROJECT_ROOT/adaptive_linear_path_model_based_diffusion-env/bin/python`
- `Python 3.11.17` (uv-managed CPython `/home/jixia/.local/share/uv/python/cpython-3.11.17-linux-x86_64-gnu`),
  `pyvenv.cfg`: `include-system-site-packages = false`. `reports/python-version.txt` = `Python 3.11.17`.
- Why 3.11: coordinator decision (used elsewhere in this workspace) and the paper states Python 3.11 + PyTorch.
  The code needs >= 3.10 (PEP 604 `int | None` in `tutorial/plot_utils.py`, `list[int]` annotations; scanner report).
  jaxlib 0.4.30, mujoco 3.1.6, torch 2.8.0 and FastMCP 4.0.3 all publish cp311 wheels. Only 3.11 was tested.

## How versions were chosen

The repository has no requirements file and pins nothing. Direct dependencies come from
`reports/tutorial-scanner.json` → `tool_review.dependencies` (read-only). Inputs and logs are in `tmp/env/`.

| Package | Version installed | Reason |
| --- | --- | --- |
| torch | **2.8.0+cpu** from `https://download.pytorch.org/whl/cpu` | Coordinator: CPU-only build (the code falls back to CPU by design; a CUDA build costs RAM and GB this machine cannot spare). 2.8.0 is the newest PyTorch release before the pinned commit date 2025-09-15 (PyPI upload 2025-08-06; 2.9.0 came 2025-10-15). Installed with `--torch-backend cpu`, which takes only PyTorch-ecosystem packages from the PyTorch index; every other package came from PyPI (index annotations in `tmp/env/resolved-full.txt`). |
| jax / jaxlib | 0.4.30 / 0.4.30 (plain CPU jaxlib, no `jax-cuda12-*` plugin) | Coordinator: same versions as the tested MBD environment; CPU build (see brax check below; no code path needs a GPU) |
| brax, flax, optax, mujoco, mujoco-mjx | 0.10.5, 0.8.5, 0.2.2, 3.1.6, 3.1.6 | Same as the MBD environment |
| other shared scientific pins (numpy 1.26.4, scipy 1.14.0, matplotlib 3.9.0, pandas 2.2.2, tqdm 4.66.4, pyyaml 6.0.1, chex 0.1.86, orbax-checkpoint 0.5.20, ml-dtypes 0.4.0, protobuf 5.27.2, pillow 10.4.0, imageio 2.34.2, ...) | as listed | Constraints taken from the MBD project's `tmp/env-probe/constraints-science.txt` (sha256 `f7618ac1...5c91`, read-only), with the CUDA pins (`jax-cuda12-*`, `nvidia-*`) and `sympy==1.12.1` removed (torch 2.8.0 requires `sympy>=1.13.3`; sympy resolved to 1.14.0). Result: `tmp/env/constraints-jax-stack.txt` (96 pins). |
| moviepy | 2.2.1 (+ imageio-ffmpeg 0.6.0, proglog 0.1.12) | Imported at module level by `vehicle_control/envs/pathtracking.py`; newest release (2025-05-21), before the pinned commit. The import path `moviepy.video.io.ImageSequenceClip.ImageSequenceClip` and `VideoClip.write_gif(filename, fps=..., loop=0, logger="bar")` exist in the installed files. |
| wandb | 0.21.4 | Module-level import in `run_rl_fine_tuning.py` and `brax_evaluation/main.py`; newest release before the pinned commit (2025-09-11). Runs are to use `--disable_wandb` / `WANDB_MODE=disabled`. |
| fastmcp | 4.0.3 (mcp / mcp-types 2.3.0, pydantic 2.14.1) | Tested baseline from `runtime.md`; resolved together with the stack above without relaxing any scientific pin |
| pytest, pytest-asyncio | 9.1.1, 1.4.0 | verification tooling |

Result versus the MBD environment (`model-based-diffusion/reports/environment-requirements.txt`): of 135 common
packages, the whole JAX/Brax/MuJoCo/NumPy/SciPy stack is identical; the 17 that differ are MCP/utility packages released
since 2026-10-02 (e.g. mcp 2.2.0→2.3.0, pydantic 2.13.5→2.14.1, rich unchanged) and sympy (1.12.1→1.14.0, needed by torch).
Added here: torch, moviepy, imageio-ffmpeg, proglog, wandb and their utilities (filelock, networkx, gitpython, sentry-sdk,
requests, ...). No `nvidia-*`, `triton` or `jax-cuda12-*` package is installed.

Only this one combination was installed and checked.

### Consequence of the CPU-only PyTorch build (recorded as requested)

- `torch/version.py` of the installed wheel: `__version__ = '2.8.0+cpu'`, `cuda = None`; `torch/lib` has
  `libtorch_cpu.so` and no CUDA library.
- **CUDA is unavailable to every PyTorch script.** `--device cuda` cannot select a GPU. By reading the code, it does not
  fail either: `vehicle_control/run_experiment.py:113` (and `run_rl_evaluation.py:191`, `run_rl_fine_tuning.py:200`) do
  `torch.device(args.device if torch.cuda.is_available() else "cpu")`, so `--device cuda` (the default) silently becomes
  CPU; `tutorial/avp_mbd.py:128`, `rl_finetuner/ppo_tuner.py:22`, `utils/path_utils.py:58` pick `cuda` only if available.
  Any GPU timing in the paper cannot be reproduced with this environment. Not yet observed at runtime (deferred).
- JAX is the CPU build as well; `brax_evaluation/main.py` has no device-specific code. With the script defaults
  (`--sample_size 2000 --horizon 50 --total_diffusion_steps 50`, hard-coded 50 env steps x 5 seeds) a CPU run will be
  slow; nothing is measured. Smaller runs must use only the script's own options (`--sample_size`, `--horizon`,
  `--total_diffusion_steps`).

## Research source identity

- `repo/adaptive_linear_path_model_based_diffusion`, `git rev-parse HEAD` =
  `6c2b004132718a1c6fd54fb7946c2705baee6c5c` (commit date 2025-09-15). No licence file, no requirements file, no
  `setup.py`/`pyproject.toml`: **nothing was installed from the repository**. The scripts are run as
  `"$PROJECT_PYTHON" <script>.py` from their own folders; sibling modules (`controller/`, `envs/`, `controllers/`, ...)
  are found through the script directory on `sys.path`.
- `git status --porcelain --ignored` printed nothing at the start and at the end of this work.
- Recommendation for executors: set `PYTHONDONTWRITEBYTECODE=1` so that importing the sibling modules does not write
  `__pycache__/` into the checkout.

## Checks (commands and exit statuses)

Run from `PROJECT_ROOT`; logs in `tmp/env/`. `PY=$PROJECT_PYTHON`, `UV=/home/jixia/.local/bin/uv`.

| # | Command | Exit | Log / output |
| --- | --- | --- | --- |
| 1 | `$UV venv adaptive_linear_path_model_based_diffusion-env --python cpython-3.11.17-linux-x86_64-gnu --managed-python` | 0 | `venv.log` |
| 2 | `env -u PYTHONPATH $UV pip compile tmp/env/science.in tmp/env/mcp.in -c tmp/env/constraints-jax-stack.txt --torch-backend cpu --python $PY --emit-index-annotation -o tmp/env/resolved-full.txt` → 150 packages | 0 | `compile-full.log`, `resolved-full.txt` (sha256 `60499572...0269`) |
| 3 | `env -u PYTHONPATH $UV pip sync tmp/env/resolved-full.txt --torch-backend cpu --python $PY` → 150 installed | 0 | `install-attempt1.log` |
| 4 | `env -u PYTHONPATH $UV pip check --python $PY` | 0 | `pip-check.log` |
| 5 | `env -u PYTHONPATH $UV pip freeze --python $PY > reports/environment-requirements.txt` (150 lines, identical to `resolved-full.txt` pins) | 0 | sha256 `d8c3e40ccfd317fbc91fc9d2e15c8d21b032eefd4690081801601bd79965b6bd` |
| 6 | `$PY --version > reports/python-version.txt` → `Python 3.11.17` | 0 | the file |
| 7 | `cd tmp/env && env -u PYTHONPATH MPLBACKEND=Agg WANDB_MODE=disabled WANDB_DIR=... $PY tmp/env/check_light_imports.py repo/.../vehicle_control/config` | 0 | `check_light_imports.log` |
| 8 | `env -u PYTHONPATH $PY -I tmp/env/inspect_checkpoint_pickle.py repo/.../vehicle_control/data/fine_tuner_checkpoints/lp_mbd_fine_tuner.pth` (pickletools only, nothing unpickled) | 0 | `inspect_checkpoint_pickle.log` |
| 9 | `$PY -m pytest -c tmp/env/pytest-noblock.ini --rootdir . -p no:cacheprovider tmp/env/test_fastmcp_smoke.py` (login shell, ROS `PYTHONPATH`, no plugin block) | 1 | `pytest-smoke-rosenv-noblock.log`: ROS `launch_testing` plugin → `ModuleNotFoundError: No module named 'lark'` |
| 10 | `$PY -m pytest -c pytest.ini --rootdir . -p no:cacheprovider tmp/env/test_fastmcp_smoke.py -v` (ROS `PYTHONPATH`) → 1 passed | 0 | `pytest-smoke-rosenv.log` |
| 11 | same with `env -u PYTHONPATH` → 1 passed | 0 | `pytest-smoke-clean.log` |
| 12 | `$PY -m pytest -p no:cacheprovider --co -q` (uses `pytest.ini`, `tests/code` still empty) → "no tests collected" | 5 | `pytest-collect-default.log` (expected until tests exist) |

Check 7 details: numpy 1.26.4, matplotlib 3.9.0, yaml 6.0.1, tqdm 4.66.4, pandas 2.2.2, wandb 0.21.4, fastmcp 4.0.3,
mcp, pydantic 2.14.1, pytest 9.1.1, pytest_asyncio 1.4.0 all load from the env's `site-packages`; `PYTHONPATH` unset.
The script installs a meta-path blocker for torch/jax/jaxlib/brax/flax/mujoco/moviepy/triton: none was imported and no
import was attempted (so importing wandb/fastmcp does not pull them in). Also checked: matplotlib backend `Agg`; an Agg
figure's `canvas.tostring_argb()` reshaped with `canvas.get_width_height()[::-1] + (4,)` (the frame-grab code of
`envs/pathtracking.py:339-340`) works with matplotlib 3.9.0; `yaml.safe_load` reads all five `vehicle_control/config/*.yaml`
(data files only, no repository code run); `wandb.init(mode="disabled", config=argparse.Namespace(...))`, `wandb.log`,
`wandb.finish` work and wrote no files (`tmp/env/wandb-dirs` stayed empty). Peak RSS 181 MB.
Harmless warnings: pydantic 2.14.1 prints two `UnsupportedFieldAttributeWarning`s while wandb 0.21.4 builds its settings.

Check 8: shipped checkpoint sha256 `3681e9cfc0ff5ba03e3eb9bd027104370fa5706e62e6e96616a3d7feea7e9ed8`, 34 archive entries;
its pickle references only `collections.OrderedDict`, `torch.FloatStorage`, `torch.LongStorage`,
`torch._utils._rebuild_tensor_v2`. These are allowed by torch's weights-only unpickler, so the `torch.load(...)` call in
`rl_finetuner/ppo_tuner.py:248/251` (no `weights_only` argument; default `True` in torch 2.8, see
`torch/serialization.py:_default_to_weights_only`) is expected to load it. Expected, not yet observed (deferred check T1).

### File-level checks of installed heavy wheels (read files only, nothing imported)

- `jax/version.py` and `jaxlib/version.py`: `_version = "0.4.30"`; `jaxlib/xla_extension.so` present; no `jax_cuda12_*`
  or `jax_plugins` directory.
- Brax 0.10.5 against `brax_evaluation/` (read both sides):
  - `brax/envs/__init__.py` registers all eight `--env_name` choices (`ant`, `hopper`, `halfcheetah`, `walker2d`,
    `reacher`, `pusher`, `inverted_double_pendulum`, `inverted_pendulum`); `get_environment(env_name, **kwargs)` passes
    `backend=` to the env class.
  - `brax/envs/base.py`: `PipelineEnv` maps `'positional'` to `brax.positional.pipeline`, stores `self.sys`, has
    `observation_size`/`action_size`; `State` has `pipeline_state` and `reward`. `brax/base.py` `Actuator.ctrl_range`
    is `(num_actuators, 2)`. The env files with backend-specific settings (`ant`, `half_cheetah`, `reacher`, `pusher`,
    the two pendulums) all handle `'positional'`.
  - Controllers use only `jax.jit`, `functools.partial(jax.jit, static_argnums=(0,))`, `jax.vmap`, `jax.lax.scan`,
    `jax.random.PRNGKey/split/normal`, `jax.nn.softmax`, `jnp.einsum/clip/argsort/cumprod/roll/.at[].set`: all present
    in jax 0.4.30. Conclusion: compatible **by reading**; not executed.
- PyTorch: see "Consequence of the CPU-only build". torch 2.8.0 metadata requires filelock, typing-extensions>=4.10,
  sympy>=1.13.3, networkx, jinja2, fsspec (all installed). `torch/lib/libgomp.so.1` is bundled.
- `torch.compile` prerequisites (used as decorators in `vehicle_control/controller/{lp,vp}_mbd_controller.py` and
  `envs/pathtracking.py`): `/usr/bin/gcc` and `g++` 13.3.0; `Python.h` present in the uv CPython
  `include/python3.11/`. Whether Inductor compiles on this machine is deferred (check T1).
- moviepy 2.2.1: `ImageSequenceClip` exists at the imported path; ffmpeg binary
  `imageio_ffmpeg/binaries/ffmpeg-linux-x86_64-v7.0.2` bundled.
- matplotlib 3.9.0 `backends/backend_agg.py` keeps `FigureCanvasAgg.tostring_argb` (only `tostring_rgb` is deprecated
  since 3.8).

## Device configuration

- `nvidia-smi`: NVIDIA GeForce RTX 4070 Laptop GPU, 8188 MiB, 1726 MiB in use, driver 581.04. Not usable by this
  environment by design (CPU builds of torch and jaxlib).
- Expected at runtime: `torch.cuda.is_available() == False`; `jax.devices() == [CpuDevice(id=0)]` (JAX may print that a
  GPU exists but no CUDA jaxlib is installed). **Not attempted: heavy jobs disabled** (checks T1, T2).
- No Jupyter kernel was registered: the CLI route does not require notebooks, and no notebook packages were requested.
  If a stage needs notebook evidence later, install papermill/nbclient/ipykernel/jupytext and register a project kernel.

## Machine-specific finding: ROS 2 leaks into the shell

The login shell exports `PYTHONPATH=/opt/ros/jazzy/opt/gz_math_vendor/lib/python:/opt/ros/jazzy/lib/python3.12/site-packages`
and a ROS `LD_LIBRARY_PATH`. Without a guard, pytest auto-loads the ROS `launch_testing` plugin and crashes (check 9).
`pytest.ini` blocks the seven ROS pytest plugins by name (checks 10-11 pass in both shells). For child processes started
by the wrapper, remove `PYTHONPATH` from the child environment (heavy.sh does this itself).

## pytest configuration

`pytest.ini` (project root, `[pytest]` section, sha256 `57d49ebf...2827`):

```ini
[pytest]
testpaths = tests/code
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
addopts = -p no:launch_testing -p no:launch_ros -p no:ament_flake8 -p no:ament_copyright -p no:ament_pep257 -p no:ament_xmllint -p no:ament_lint
```

`asyncio_mode = auto` because pytest-asyncio 1.4.0 defaults to strict mode, where unmarked `async def test_...` are not
run. The smoke test (`tmp/env/test_fastmcp_smoke.py`: `FastMCP`, `@mcp.tool()`, `Client(server)`, `await
client.call_tool`, `result.data == 5`) checks tooling only; it is not scientific evidence and is not in `tests/code`.

## Deferred checks (not attempted: heavy jobs disabled)

All of the following are written and syntax-checked but **not run**. Run them only after the coordinator removes
`mcp-build/HEAVY_JOBS_DISABLED`, one at a time, with no other agents active. The script
`tmp/env/run_deferred_heavy_checks.sh` contains exactly these commands. heavy.sh needs MemAvailable >= limit + 1500 MB
(2700 MB for the limit below; 2544 MB were available at the time of writing). Commands (from `PROJECT_ROOT`):

```bash
H=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh
PY=$PWD/adaptive_linear_path_model_based_diffusion-env/bin/python
R=$PWD/repo/adaptive_linear_path_model_based_diffusion
# T1 torch import/origin, CUDA availability, numpy interop, checkpoint torch.load default, tiny torch.compile, moviepy import
$H --limit-mb 1200 --timeout 600 --log tmp/env/check_heavy_torch.log -- env PYTHONDONTWRITEBYTECODE=1 TORCHINDUCTOR_COMPILE_THREADS=1 "$PY" tmp/env/check_heavy_torch.py "$R/vehicle_control/data/fine_tuner_checkpoints/lp_mbd_fine_tuner.pth"
# T2 jax/jaxlib/brax/flax/optax/mujoco/mjx import/origin, jax.devices(), tiny jit, the 8 Brax envs with backend="positional" (objects only)
$H --limit-mb 1200 --timeout 600 --log tmp/env/check_heavy_jax.log -- env PYTHONDONTWRITEBYTECODE=1 JAX_PLATFORMS=cpu "$PY" tmp/env/check_heavy_jax.py
# H1-H6 --help of the documented scripts that define argparse options, each from its own folder
$H --limit-mb 1200 --timeout 600 --log tmp/env/help-tutorial-run_1d_example.log -- env -C "$R/tutorial" PYTHONDONTWRITEBYTECODE=1 "$PY" run_1d_example.py --help
$H --limit-mb 1200 --timeout 600 --log tmp/env/help-tutorial-run_2d_example.log -- env -C "$R/tutorial" PYTHONDONTWRITEBYTECODE=1 "$PY" run_2d_example.py --help
$H --limit-mb 1200 --timeout 600 --log tmp/env/help-vehicle_control-run_experiment.log -- env -C "$R/vehicle_control" PYTHONDONTWRITEBYTECODE=1 "$PY" run_experiment.py --help
$H --limit-mb 1200 --timeout 600 --log tmp/env/help-vehicle_control-run_rl_evaluation.log -- env -C "$R/vehicle_control" PYTHONDONTWRITEBYTECODE=1 "$PY" run_rl_evaluation.py --help
$H --limit-mb 1200 --timeout 600 --log tmp/env/help-vehicle_control-run_rl_fine_tuning.log -- env -C "$R/vehicle_control" PYTHONDONTWRITEBYTECODE=1 WANDB_MODE=disabled "$PY" run_rl_fine_tuning.py --help
$H --limit-mb 1200 --timeout 600 --log tmp/env/help-brax_evaluation-main.log -- env -C "$R/brax_evaluation" PYTHONDONTWRITEBYTECODE=1 JAX_PLATFORMS=cpu WANDB_MODE=disabled "$PY" main.py --help
git -C "$R" status --porcelain --ignored   # must print nothing
```

`tutorial/run_alp_mbd.py` and `tutorial/run_avp_mbd.py` have **no argument parsing** (no argparse, no `sys.argv`):
they support no `--help`, and any invocation runs the whole experiment. Do not run them as a help check.
`TORCHINDUCTOR_COMPILE_THREADS=1` keeps Inductor from starting a pool of compile workers on this 16-thread, low-memory
machine; executors running `vehicle_control/` should consider the same setting (it does not change results).

## Source observations for later stages (read from the code, not executed)

- `--save_mode` is declared `type=bool` in `run_experiment.py:110`, `run_rl_evaluation.py:188`,
  `run_rl_fine_tuning.py:197`: argparse calls `bool("False")`, so any non-empty value, including `False`, enables saving.
  Omit the flag to keep the default `False`.
- `envs/pathtracking.py` stores ARGB frames (`tostring_argb`); moviepy 2.2.1 `ImageSequenceClip` takes channels
  `[:, :, :3]` of a numpy frame and, with the default `with_mask=True`, channel 3 as the mask. For ARGB frames those are
  A, R, G and B respectively, so GIF colours may differ from the figure. This is upstream behaviour; compare with the
  shipped `vehicle_control/video/seed_0_mbd_controller.gif` when the GIF path is executed.

## Unresolved requirements and blockers

1. **Blocker (workspace policy): heavy jobs disabled.** torch/JAX/Brax/MuJoCo/moviepy imports, device checks, the tiny
   torch.compile, and the six `--help` checks are not attempted; no repository script has been run. Stage 2 cannot use
   this environment until they pass.
2. CUDA is unavailable by design (CPU-only torch and jaxlib; coordinator decision). GPU results cannot be reproduced.
3. No licence file in the repository (recorded; not an environment issue).
4. No missing data or credentials were found for the environment itself: wandb runs disabled; the reference paths,
   configs and the fine-tuner checkpoint are in the checkout.

Setup attempts used: 1 of 3.
