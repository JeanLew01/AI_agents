# Environment manager results: dial-mpc (CLI route, Python backend)

> **Status after attempt 2 (see the "Attempt 2" section at the end, which supersedes sections 3, 5 and 7
> where they differ):** the attempt-1 environment could not do GPU linear algebra (cuSOLVER/cuBLAS wheel
> mismatch). Seven NVIDIA wheels were changed to the CUDA 12.8.1 set. The fix is applied and passes
> `uv pip check` and a static symbol check, but it is **not yet verified with JAX**, and the `dial-mpc`
> feasibility probe is **still not attempted**, because heavy jobs were disabled workspace-wide.

Date: 2026-10-02. Host: WSL2 Ubuntu 24.04 (kernel 6.6.114.1), 16 threads, 7532 MB RAM, 2048 MB swap,
NVIDIA RTX 4070 Laptop GPU 8188 MiB (driver 581.04, nvidia-smi 580.79, CUDA 13.0 runtime reported).

Outcome in one paragraph: the environment is complete and passes `uv pip check`; the pinned checkout is
installed editable; JAX sees the GPU; `dial-mpc --list-examples` works; FastMCP 4.0.3 is installed in the
same environment without a resolver conflict. **The heavy feasibility probe of `dial-mpc --config` was NOT
run**: the coordinator's amendment requires at least 3000 MB in the `available` column of `free -m`
immediately before starting it, and the machine showed 1135 to 1786 MB at every check. The probe configs,
the driver and the exact command are prepared under `tmp/env-probe/` (section 7). No statement about
feasible `Nsample`, JIT time, wall time or GPU memory of the main command is made in this report.

## 1. Interpreter

| item | value |
|---|---|
| PROJECT_ROOT | `/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/dial-mpc` |
| PROJECT_ENV | `/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/dial-mpc/dial-mpc-env` (uv venv, 5.0 GB, outside `repo/`) |
| PROJECT_PYTHON | `/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/dial-mpc/dial-mpc-env/bin/python` |
| Python | 3.10.21 (uv-managed CPython, base `/home/jixia/.local/share/uv/python/cpython-3.10-linux-x86_64-gnu`) |
| uv | 0.12.22 |

Why 3.10: the README asks for Python >= 3.10 and states the authors' environment was Python 3.10 with
CUDA 12.6. FastMCP 4.0.3 declares `requires_python >=3.10`, so one interpreter serves both. The newest
JAX line that still supports 3.10 is 0.6.x, which is also the line current at the pinned commit date.

## 2. Source identity

- Checkout: `repo/dial-mpc`, `git rev-parse HEAD` = `871c84f1cefbe9fa9d83a06b05ab4f0243c1a05c`
  (2025-05-28, https://github.com/LeCAR-Lab/dial-mpc). `git status --short` is empty after all work.
- Installed **editable** from that checkout (`uv pip install -e repo/dial-mpc`), which is the README's
  documented method (`pip3 install -e .`). `uv pip freeze` records
  `-e file:///home/jixia/AI_agents/paper2agent/NMPC/mcp-build/dial-mpc/repo/dial-mpc`;
  `dial_mpc-0.0.2.dist-info/direct_url.json` has `"editable": true`; the editable finder maps
  `dial_mpc` to `repo/dial-mpc/dial_mpc`.
- `dial_mpc.__file__` = `.../repo/dial-mpc/dial_mpc/__init__.py`, i.e. the import **points into the
  checkout**, not into a copy in site-packages. Moving or deleting the checkout breaks the installation.
- A regular (non-editable) wheel would not work for this commit: `setup.py` uses
  `find_packages(include=["dial_mpc"])`, which returns only `['dial_mpc']` (checked; without the filter it
  returns 7 packages), and `package_data` is keyed by `"dial-mpc"` instead of the package name, so the
  subpackages, example YAML files and the 48 MB of models would be left out. Stage 5 must therefore
  document a checkout plus editable install (or `PYTHONPATH`), not a plain `pip install git+...`.
- Side effects inside the checkout, all git-ignored, no tracked file touched: `dial_mpc.egg-info/`
  (written by setuptools during the editable build) and `__pycache__/` directories written on import.
- Console scripts created in `dial-mpc-env/bin/` with the project interpreter in the shebang:
  `dial-mpc`, `dial-mpc-sim`, `dial-mpc-plan`, `dial-mpc-real`, `dial-mpc-sim2sim`, `dial-mpc-sim2real`.
  Only `dial-mpc` was executed. `dial-mpc-sim2real` points to `dial_mpc.core.dial_sim2real`, a module that
  does not exist in the tree. `dial-mpc-sim2sim` (`dial_mpc/core/dial_sim2sim.py`) just runs `dial-mpc-sim`
  and then `dial-mpc-plan` through `subprocess.run` with bare command names, so it depends on `PATH`.
  `dial-mpc-real` imports `unitree_sdk2py` and, depending on the plugin, `rclpy` or `pyvicon_datastream`;
  none of them is installed.

## 3. Version resolution and reasons

`setup.py` leaves everything except `numpy<2.0.0` unpinned. Today's releases are jax 0.11.2
(Python >= 3.12), brax 0.14.2 (Python >= 3.11), mujoco / mujoco-mjx 3.14.0. Instead of guessing, the
scientific stack was resolved **as PyPI stood on the day after the pinned commit**
(`uv pip compile --exclude-newer 2025-05-29T00:00:00Z --python-version 3.10`), which gives the releases
the authors' `pip install -e .` would have fetched at that commit. FastMCP and pytest were then resolved
on top with those versions as constraints.

| package | version | released | reason |
|---|---|---|---|
| jax, jaxlib | 0.6.1 | 2025-05-21 | newest at commit date; supports Python 3.10 |
| jax-cuda12-plugin, jax-cuda12-pjrt | 0.6.1 | | from `jax[cuda12]`, CUDA 12 wheels from pip |
| nvidia-*-cu12 | cublas 12.8.4.1, cudnn 9.10.1.4, cufft 11.4.0.6, cusolver 11.7.4.40, cusparse 12.5.9.5, cuda-runtime 12.9.37, cuda-nvcc 12.9.41, cuda-cupti 12.9.19, nvjitlink 12.9.41, nccl 2.26.5, nvshmem 3.2.5 | | pulled by the plugin's `with-cuda` extra, as of commit date |
| brax | 0.12.3 | 2025-04-11 | newest at commit date; provides `brax.mjx.pipeline._reformat_contact`, `brax.envs.base.PipelineEnv`, `brax.io.html` that the code imports (imports verified) |
| mujoco, mujoco-mjx | 3.3.2 | 2025-04-28 | newest at commit date; the two must have the same version |
| numpy | 1.26.4 | | `numpy<2.0.0` from `setup.py` |
| scipy | 1.15.3 | | as of commit date |
| jax-cosmo | 0.1.0 | 2023-02-05 | only release line; provides `InterpolatedUnivariateSpline` |
| flax 0.10.6, optax 0.2.4, chex 0.1.89, jaxopt 0.8.5, orbax-checkpoint 0.11.13, ml-collections 1.1.0 | | | brax dependencies as of commit date |
| flask 3.1.1, flask-cors 6.0.0, werkzeug 3.1.3, pyyaml 6.0.2 | | | not declared by `setup.py` but imported by `dial_core.py`; they arrive through brax and its dependencies |
| matplotlib 3.10.3, scienceplots 2.1.1, tqdm 4.67.1, art 6.5, emoji 2.14.1 | | | `setup.py` requirements as of commit date |
| setuptools | 80.9.0 | 2025-05-27 | **added by hand** (see below) |
| fastmcp, fastmcp-slim | 4.0.3 | | skill baseline |
| mcp, mcp-types | 2.2.0 | | from fastmcp |
| pydantic / pydantic-core | 2.13.5 / 2.46.5 | | from fastmcp (needs >= 2.12) |
| pytest / pytest-asyncio | 9.1.1 / 1.4.0 | | unpinned request, versions chosen by the resolver for Python 3.10 |

Deviations from the pure commit-date stack, both forced by FastMCP 4.0.3 and both outside the numerical path:

1. `typing-extensions` 4.13.2 -> 4.16.0 (pydantic 2.13 needs >= 4.14.1).
2. `tyro` 0.9.22 -> 1.0.16 (tyro 0.9.22 pins `typing-extensions==4.13.2`); `shtab` dropped with it.
   `tyro` is listed in `setup.py` but is not imported anywhere in the checkout (`grep` finds it only in `setup.py`).

Pinning all 87 commit-date packages as constraints made `fastmcp==4.0.3` unsatisfiable (exit 1) for
exactly that reason; releasing only those two pins resolved (exit 0). No scientific package changed.
The runtime.md conflict procedure (choose another FastMCP version) was therefore not needed.

Undeclared requirement found: `jax_cosmo/__init__.py` does `from pkg_resources import ...`. A uv venv has
no setuptools, so the first import attempt failed with `ModuleNotFoundError: No module named
'pkg_resources'`. `setuptools==80.9.0` (commit-date release, still ships `pkg_resources`) was installed.
It prints a `UserWarning: pkg_resources is deprecated` on stderr at every start of `dial-mpc`; this is
harmless but wrappers must not treat stderr output as failure. Stage 5 must list `setuptools<81`.

Resolver inputs and outputs are kept in `tmp/env-probe/resolution/`:
`core.in`, `core-pins.txt` (commit-date stack, 87 packages), `mcp.in`, `all.in`, `sci-constraints.txt`,
`all-resolved.txt` (the 153 pins that were installed).

## 4. Commands and exit statuses

Run from PROJECT_ROOT; `UV=/home/jixia/.local/bin/uv`, `PY=dial-mpc-env/bin/python`.
Setup attempts used: 2 of 3 (attempt 1 = install; attempt 2 = add setuptools after the import failure).

| # | command | exit |
|---|---|---|
| 1 | `uv pip compile core.in --python-version 3.10 --exclude-newer 2025-05-29T00:00:00Z -o core-pins.txt` | 0 |
| 2 | `uv pip compile all.in -c core-pins.txt --python-version 3.10` (all pins kept) | 1 (tyro 0.9.22 vs fastmcp 4.0.3) |
| 3 | `uv pip compile all.in -c sci-constraints.txt --python-version 3.10 -o all-resolved.txt` | 0 |
| 4 | `uv venv dial-mpc-env --python 3.10` | 0 |
| 5 | `uv pip install --python $PY -c tmp/env-probe/resolution/all-resolved.txt -e repo/dial-mpc 'fastmcp==4.0.3' pytest pytest-asyncio` (1 min 24 s) | 0 |
| 6 | `uv pip check --python $PY` | 0, "Checked 153 packages ... All installed packages are compatible" |
| 7 | import check (numpy, scipy, jax, jaxlib, mujoco, mjx, brax, jax_cosmo, flask, yaml, dial_mpc) | 1, `No module named 'pkg_resources'` |
| 8 | `uv pip install --python $PY --exclude-newer 2025-05-29T00:00:00Z setuptools` | 0, `+ setuptools==80.9.0` |
| 9 | `uv pip check --python $PY` | 0, "Checked 154 packages ... All installed packages are compatible" |
| 10 | import check repeated, under the heavy lock (log: `tmp/env-probe/logs/import_check.log`) | 0 |
| 11 | `dial-mpc-env/bin/dial-mpc --list-examples`, cwd `tmp/env-probe`, under the lock (logs: `tmp/env-probe/logs/list_examples.stdout`, `.stderr`) | 0 |
| 12 | after the interruption: `uv pip check --python $PY` | 0, 154 packages compatible |
| 13 | `uv pip freeze --python $PY > reports/environment-requirements.txt` (154 lines) | 0 |
| 14 | `$PY --version > reports/python-version.txt` (`Python 3.10.21`) | 0 |
| 15 | XLA flag check: import `dial_mpc.core.dial_core` first, then jit a matmul on the GPU (log: `tmp/env-probe/logs/xla_flag_check.log`) | 0 |
| 16 | FastMCP smoke test: in-process `Client(server)`, `list_tools`, `call_tool("add")`, `result.data == 5` (log: `tmp/env-probe/logs/fastmcp_smoke.log`) | 0 |
| 17 | `dial-mpc-env/bin/fastmcp version` (FastMCP 4.0.3, MCP 2.2.0, Python 3.10.21) | 0 |
| 18 | `$PY -m pytest --version` (pytest 9.1.1) | 0 |
| 19 | probe driver with `go2_trot_n4_N2048.yaml` | 3, refused by its own guard: `MemAvailable 1528 MB < 3000 MB`; dial-mpc was not started |

Import check output (command 10):

| module | version | origin |
|---|---|---|
| numpy | 1.26.4 | `dial-mpc-env/lib/python3.10/site-packages/numpy/__init__.py` |
| scipy | 1.15.3 | `.../site-packages/scipy/__init__.py` |
| jax | 0.6.1 | `.../site-packages/jax/__init__.py` |
| jaxlib | 0.6.1 | `.../site-packages/jaxlib/__init__.py` |
| mujoco | 3.3.2 | `.../site-packages/mujoco/__init__.py` |
| mujoco.mjx (mujoco-mjx) | 3.3.2 | `.../site-packages/mujoco/mjx/__init__.py` |
| brax | 0.12.3 | `.../site-packages/brax/__init__.py` |
| jax_cosmo | 0.1.0 | `.../site-packages/jax_cosmo/__init__.py` |
| flask | 3.1.1 | `.../site-packages/flask/__init__.py` |
| yaml (pyyaml) | 6.0.2 | `.../site-packages/yaml/__init__.py` |
| dial_mpc | 0.0.2 (no `__version__` attribute) | `repo/dial-mpc/dial_mpc/__init__.py` |
| dial_mpc.core.dial_core | | `repo/dial-mpc/dial_mpc/core/dial_core.py` |
| fastmcp / pytest / pytest_asyncio | 4.0.3 / 9.1.1 / 1.4.0 | site-packages |

`dial-mpc --list-examples` (command 11) printed the banner and:
`unitree_h1_jog`, `unitree_h1_push_crate`, `unitree_h1_loco`, `unitree_go2_trot`, `unitree_go2_seq_jump`,
`unitree_go2_crate_climb`, `allegro_reorient`. The program has no `--help`-only or `--version` contract
beyond argparse; `--list-examples` is the supported non-computing invocation. Even this invocation
imports JAX, Brax and matplotlib first (the module imports sit above `main`). It was not timed; the
separate import check needed 28.4 s for the imports and the XLA flag check 41.4 s in total on this
loaded machine, so wrappers should allow a start-up time of that order.

## 5. Device configuration

- `jax.devices()` = `[CudaDevice(id=0)]`, `jax.default_backend()` = `gpu`, a test array reports
  `device = cuda:0`. GPU JAX from pip CUDA 12 wheels works on this machine (WSL2, driver 581.04).
- `dial_core.py` appends ` --xla_gpu_triton_gemm_any=True` to `XLA_FLAGS` at import. With jaxlib 0.6.1 the
  flag is accepted: after importing `dial_core` first, a jitted 64x64 matmul ran on `cuda:0` (exit 0).
  XLA printed one autotuning warning (`dot_search_space.cc:200 ... All configs were filtered out`),
  which is a warning, not an error.
- `XLA_PYTHON_CLIENT_PREALLOCATE=false` was exported for every JAX command. Without it JAX reserves
  75 % of the 8 GB GPU, of which about 1.1 to 1.26 GB was already in use by the desktop.
- These device checks only show that JAX can use the GPU. They are not evidence that an MJX rollout
  compiles or fits in memory.

## 6. pytest configuration

`pytest.ini` at the project root:

```ini
[pytest]
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
testpaths = tests/code
```

Run tests with `dial-mpc-env/bin/python -m pytest tests/code/`.

## 7. Feasibility probe: NOT ATTEMPTED

Reason: the coordinator's rule is to run it only with at least 3000 MB `available` in `free -m`
immediately before the start. Values observed (MB available / MB swap free): 951/541 and 802/547 at the
start of the work, 1167/92 and 1071/105 around the import checks, 1135/859 after the interruption,
1585/551, 1528 (driver guard), 1786/688, 1718/423 and 1025/445 at the last check. The largest consumers are other
sessions' processes (a Pylance language server with about 2.6 GB resident, VS Code server processes,
other agent sessions); none of them is mine and none was touched.

Consequently unknown, and to be measured later: whether the main command runs at all with this stack
(the environment creation, the MJX compile and the rollout were never executed), wall time, JIT time,
peak GPU memory, peak host memory, whether `Nsample: 2048` is feasible, and the largest feasible
configuration. Largest configuration actually run successfully: none.

What is prepared (all under `tmp/env-probe/`, nothing in the checkout):

- `configs/go2_trot_n4_N2048.yaml`: `dial_mpc/examples/unitree_go2_trot.yaml`
  (sha256 `5eaae666...c88d40`) with exactly two changed lines, `n_steps: 400 -> 4` and
  `output_dir: unitree_go2_trot -> out_go2_trot_n4_N2048`. `Nsample` stays 2048.
  `n_steps: 4` is the smallest useful value: step 0 compiles the planner with `Ndiffuse_init: 10`,
  step 1 compiles it again with `Ndiffuse: 2` (different scan length), steps 2 and 3 show the
  steady-state rate.
- `configs/go2_trot_n4_N1024.yaml`, `..._N512.yaml`, `..._N128.yaml`: the same plus a reduced `Nsample`
  and matching `output_dir`, for stepping down if 2048 runs out of GPU or host memory.
- `run_probe.py` (standard library only): starts `dial-mpc-env/bin/dial-mpc --config FILE` with cwd
  `tmp/env-probe/run` in its own process group with `oom_score_adj` 800 (so that the kernel would
  sacrifice the probe rather than another session), timestamps every output line into
  `logs/probe_<config>.log`, samples total GPU memory and the process' `VmHWM`, waits until
  `*_states.npy` and `*_predictions.npy` exist in the output directory, waits 3 s, sends SIGTERM to the
  group (SIGKILL after 15 s), checks that nothing listens on port 5000 and writes
  `logs/probe_<config>.json`. It refuses to start below `--min-available-mb` (default 3000) or when
  `XLA_PYTHON_CLIENT_PREALLOCATE` is not `false`, and kills the run after `--timeout` (default 900 s).
  Its refusal path was exercised (command 19); the path that launches dial-mpc has never been run,
  so the driver itself is untested beyond that.

Command to run later, starting with the full sample count and going down only on failure:

```bash
export XLA_PYTHON_CLIENT_PREALLOCATE=false
P=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/dial-mpc
free -m    # need >= 3000 MB available
flock /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/.heavy.lock \
  $P/dial-mpc-env/bin/python $P/tmp/env-probe/run_probe.py \
  --config $P/tmp/env-probe/configs/go2_trot_n4_N2048.yaml
ss -ltnp | grep ':5000'    # must print nothing afterwards
```

The plain upstream command the driver wraps is
`cd $P/tmp/env-probe/run && $P/dial-mpc-env/bin/dial-mpc --config $P/tmp/env-probe/configs/go2_trot_n4_N2048.yaml`;
run that way it does not return, because it ends in `app.run(port=5000)`.

Port 5000: nothing was listening on it at any check (`ss -ltnp`), and no server was started by me.

Facts about the main command that later stages need, read from `dial_core.py` at the pinned commit
(source reading, not execution):

- Result files are written to `output_dir` relative to the **current working directory**:
  `<timestamp>_brax_visualization.html`, `<timestamp>_states.npy`, `<timestamp>_predictions.npy`
  with `timestamp = time.strftime("%Y%m%d-%H%M%S")`. Two runs finishing within the same second in the
  same directory would overwrite each other.
- After writing them it calls Flask `app.run(port=5000)` and blocks; the port is hard-coded and there is
  no flag to disable the server. A wrapper has to terminate the process after the files appear. If
  port 5000 is already taken, the files are still written first and the process then fails at bind.
- The seed is the `seed` key of the YAML file; there is no command-line seed flag.

## 8. Unresolved requirements and risks

1. Feasibility of `dial-mpc --config/--example` on this machine is unmeasured (section 7). Host RAM is
   the likely limit: 7.5 GB in total, 1 to 1.8 GB available during this work, while an MJX compile for a
   legged robot needs several GB on the host independent of `Nsample`. This is an expectation, not a
   measurement.
2. `dial-mpc-sim` opens a MuJoCo viewer window (`mujoco.viewer.launch_passive`); no display check was
   made. `dial-mpc-plan` exchanges data with `dial-mpc-sim` through `multiprocessing.shared_memory`
   blocks, so it is meant to run next to it (README: two terminals). Neither was executed.
3. `dial-mpc-real` needs `unitree_sdk2py` (not installed; the README points to the Unitree GitHub
   repository for it), a Unitree Go2 and a localisation source; `rclpy` / `pyvicon_datastream` are not
   installed.
4. `dial-mpc-sim2real` has no module in the checkout; the entry point cannot work at this commit.
5. The environment depends on the checkout path (editable install) and on `setuptools<81` for
   `pkg_resources`.
6. Python 3.10 is at the end of its upstream support period; it was chosen to match the authors'
   tested version and JAX 0.6.x.
7. `fastmcp version` reports that 4.0.10 is available; 4.0.3 was kept as the skill's baseline.

## 9. Files written by this role

- `dial-mpc-env/` (environment)
- `pytest.ini`
- `reports/environment-manager_results.md`, `reports/environment-requirements.txt`, `reports/python-version.txt`
- `tmp/env-probe/resolution/*`, `tmp/env-probe/configs/*.yaml`, `tmp/env-probe/run_probe.py`,
  `tmp/env-probe/logs/*` (`import_check.log`, `list_examples.stdout`, `list_examples.stderr`,
  `xla_flag_check.log`, `fastmcp_smoke.log`, `probe_go2_trot_n4_N2048.json` from the refused start),
  `tmp/env-probe/run/` (empty)

---

# Attempt 2 (2026-10-02, about 14:50Z to 15:20Z): GPU linear algebra

Setup attempts used: 3 of 3 (this is the third change to the environment).

## A2.1 What was wrong

The attempt-1 environment imported and could run a jitted matmul on the GPU, but any cuSOLVER-backed
operation failed. Section 5 above ("GPU JAX from pip CUDA 12 wheels works on this machine") was too
strong: only device listing and a matmul had been tested, not linear algebra.

Coordinator's evidence (not produced by me): `tmp/env-probe/coord-run/n4_N128.log` shows
`dial-mpc --config tmp/env-probe/configs/go2_trot_n4_N128.yaml` exiting 1 at
`state_init = reset_env(rng_reset)` (`dial_core.py:227`) with
`jaxlib._jax.XlaRuntimeError: INTERNAL: cuSolver internal error`, scope peak 1321 MB, 44 s wall.

Cause, established without JAX:

1. `jax-cuda12-plugin` 0.6.1 declares `nvidia-cublas-cu12<12.9,>=12.1.3.1` in its `with-cuda` extra
   (installed `METADATA`). The source at tag `jax-v0.6.1`
   (`jax_plugins/cuda/plugin_setup.py`, line 56) gives the reason as a comment: "cudnn has a bug with
   mxfp8 with multiple GPUs per process and cublas 12.9". The cap exists only in 0.6.1; it is absent at
   tags `jax-v0.6.0` and `jax-v0.6.2`. The other NVIDIA requirements have no upper bound.
2. The resolver therefore took cuBLAS from the CUDA 12.8 line (12.8.4.1) and everything else from the
   CUDA 12.9.0 wheels published on 2025-05-01 (cuSOLVER 11.7.4.40, cuSPARSE 12.5.9.5, nvJitLink 12.9.41,
   cuFFT 11.4.0.6, runtime 12.9.37, cupti 12.9.19, nvcc 12.9.41). So the mix comes from the plugin's cap,
   not from the date limit as such: a resolve of `jax[cuda12]==0.6.1` without any date limit today
   also returns a split set (cuBLAS 12.8.5.5 with cuSOLVER 11.7.5.82; whether that one works was not tested).
3. cuSOLVER 11.7.4.40 needs a symbol that cuBLAS 12.8.4.1 does not export:
   - `tmp/env-probe/attempt2/ctypes_A_env_as_installed.log` (run through `heavy.sh`, exit 1, scope peak
     231 MB): loading the installed `libcusolver.so.11` with `RTLD_NOW` fails with
     `undefined symbol: cublasSetEnvironmentMode, version libcublas.so.12`.
   - `tmp/env-probe/attempt2/symbol_check.txt` (`nm -D`): the symbol is defined 0 times in
     libcublas 12.8.4.1 and once in libcublas 12.9.0.13; libcusolver 11.7.4.40 requires it,
     libcusolver 11.7.3.90 does not.
   - `tmp/env-probe/attempt2/static_symbol_resolution.txt`: of the 139 versioned symbols that
     libcusolver 11.7.4.40 imports from cuBLAS, cuBLASLt, cuSPARSE and nvJitLink, exactly one is
     missing in the attempt-1 set, `cublasSetEnvironmentMode@libcublas.so.12`.
   - `tmp/env-probe/attempt2/ctypes_B_only_cublas_12.9.0.13.log` (through `heavy.sh`, exit 0, scope peak
     432 MB): with only libcublas/libcublasLt replaced by the 12.9.0.13 copies and everything else from
     the environment, `cusolverDnCreate` returns `CUSOLVER_STATUS_SUCCESS`.

   The coordinator's hypothesis (mismatched cuBLAS and cuSOLVER release lines) is confirmed for the
   handle creation. The JAX plugin modules have no `DT_NEEDED` entry for cuSOLVER, so they load it
   lazily; that would explain why the failure appears as "cuSolver internal error" at the first solver
   call instead of at import. That last sentence is an inference from `readelf`, not something I traced.

Two further ctypes runs (only cuSOLVER replaced; the full 12.8.1 trio) were queued behind other agents'
jobs on the workspace lock and were cancelled by me before they started; the machine then froze at about
15:05Z and heavy jobs were disabled. They were never run.

## A2.2 What was changed

Two fixes were possible. The one applied is the CUDA 12.8.1 set, not the cuBLAS upgrade:

| candidate | change | runtime evidence | resolver |
|---|---|---|---|
| cuBLAS 12.8.4.1 -> 12.9.0.13 | 1 package | `cusolverDnCreate` succeeds (log B) | **rejected by a fresh resolve**: `jax[cuda12]==0.6.1` plus `nvidia-cublas-cu12==12.9.0.13` gives "No solution found" (`uv pip compile`, exit 1) because of the plugin's `<12.9` cap |
| CUDA 12.8.1 set (applied) | 7 packages | none yet | accepted (`uv pip compile`, exit 0); stays inside every bound declared by `jax-cuda12-plugin` 0.6.1 |

Reason for the choice: stage 5 has to rebuild the environment with a plain
`uv pip install -r src/requirements.txt`, and `dial-mpc`'s own `setup.py` requires `jax[cuda12]`, which
drags in the `<12.9` cap. A cuBLAS 12.9 pin could only be reproduced with resolver overrides. The CUDA
12.8.1 set is also exactly what `jax-cuda12-plugin[with-cuda]==0.6.0` resolved to on 2025-04-30
(`uv pip compile --exclude-newer 2025-04-30T00:00:00Z`), i.e. the wheels JAX 0.6.x was released against
before the 12.9 wheels appeared. The price is that this choice rests on static evidence only.

Command (exit 0):
`uv pip install --python dial-mpc-env/bin/python -r tmp/env-probe/resolution/attempt2-cuda-12.8.1-pins.txt`

| package | attempt 1 | attempt 2 | reason |
|---|---|---|---|
| nvidia-cusolver-cu12 | 11.7.4.40 | 11.7.3.90 | the 12.9-line build needs `cublasSetEnvironmentMode`, absent from cuBLAS 12.8; this is the change that matters |
| nvidia-cusparse-cu12 | 12.5.9.5 | 12.5.8.93 | same CUDA release as cuBLAS and cuSOLVER (12.8.1) |
| nvidia-nvjitlink-cu12 | 12.9.41 | 12.8.93 | same release |
| nvidia-cufft-cu12 | 11.4.0.6 | 11.3.3.83 | same release |
| nvidia-cuda-runtime-cu12 | 12.9.37 | 12.8.90 | same release |
| nvidia-cuda-cupti-cu12 | 12.9.19 | 12.8.90 | same release |
| nvidia-cuda-nvcc-cu12 | 12.9.41 | 12.8.93 | same release (plugin needs >= 12.6.85) |
| nvidia-cublas-cu12 | 12.8.4.1 | unchanged | already the 12.8.1 build, inside the plugin's cap |
| nvidia-cudnn-cu12 9.10.1.4, nvidia-nccl-cu12 2.26.5, nvidia-nvshmem-cu12 3.2.5 | | unchanged | versioned independently of the CUDA minor release; inside the plugin's bounds |

Only `nvidia-cusolver-cu12` is shown by the evidence to need changing. The other six were moved so that
all CUDA toolkit libraries come from one release; that is a consistency choice, not a demonstrated
necessity. jax/jaxlib/jax-cuda12-plugin 0.6.1, brax 0.12.3, mujoco and mujoco-mjx 3.3.2, numpy 1.26.4 and
every non-NVIDIA package are unchanged.

Checks after the change (none of them loads JAX or touches the GPU):

| command | exit | result |
|---|---|---|
| `uv pip check --python dial-mpc-env/bin/python` | 0 | "Checked 154 packages ... All installed packages are compatible" |
| `uv pip freeze --python dial-mpc-env/bin/python > reports/environment-requirements.txt` | 0 | 154 lines; differs from attempt 1 in exactly the 7 lines above (`diff` against `tmp/env-probe/resolution/attempt1-freeze.txt`) |
| `tmp/env-probe/attempt2/symcheck.sh` on the libraries now in the environment | 0 | libcusolver: 138 imported versioned symbols, 0 missing; libcusparse: 8, 0 missing (appended to `static_symbol_resolution.txt`) |
| `uv pip compile tmp/env-probe/resolution/all.in -c <freeze without the -e line>` | 0 | a fresh resolve reproduces the installed set exactly (152 packages; `setuptools` is the hand-added extra); saved as `tmp/env-probe/resolution/all-resolved-attempt2.txt` |
| `git status --short` in `repo/dial-mpc` | 0 | empty, HEAD still 871c84f |

`reports/python-version.txt` is unchanged (`Python 3.10.21`). The alternative wheels that were unpacked
for the comparison lived in the session scratch directory, outside the environment and the project; they
are deleted and are not part of the environment or of `reports/environment-requirements.txt`.

Stage 5 consequence: `src/requirements.txt` must pin the eight NVIDIA toolkit wheels of
`attempt2-cuda-12.8.1-pins.txt` explicitly. Leaving them to the resolver recreates a split set.

## A2.3 Not verified

- **The fix has not been run with JAX.** No `jnp.linalg.cholesky`, no `jnp.linalg.solve`, no import of
  JAX at all after the change; even `cusolverDnCreate` was not called with the new set. What supports
  it is static: no unresolved symbols, a resolver-valid single-release set. It is possible that the
  12.8.1 set fails for another reason; if so, the fallback with runtime evidence is
  `nvidia-cublas-cu12==12.9.0.13` together with the attempt-1 12.9.0 wheels (`attempt1-freeze.txt`),
  at the cost of the resolver problem described above.
- **The `dial-mpc` feasibility probe is still not attempted.** Wall time per control step, JIT time, peak
  scope memory, peak GPU memory, feasibility of `Nsample: 2048`: all unmeasured. Largest configuration
  run successfully: none. The only execution of the main command so far is the coordinator's failed
  attempt-1 run quoted in A2.1.
- `FLASK_RUN_FROM_CLI=true`: confirmed for Flask alone, not yet end to end. Flask 3.1.1 `app.py`
  lines 611 to 621 return from `Flask.run` at once when the variable equals `true`. A Flask-only script
  with the same call as `dial_core.py` (`app.run(port=5000)`, no JAX imported) returned after 0.016 s
  with exit 0, printed the "Ignoring a call to 'app.run()'" notice and left nothing listening on port
  5000 (`tmp/env-probe/attempt2/flask_run_from_cli_check.py`, `.log`). That `dial-mpc` as a whole then
  exits by itself with status 0 is expected from this, but the coordinator's run died before reaching
  that line, so it remains to be observed.

## A2.4 Commands to run later, in this order, each through `heavy.sh`

`tmp/env-probe/run_probe.py` and the plain `flock` command of section 7 are **superseded** by the
memory rule in `COMMON_BRIEF.md`; do not use them.

```bash
H=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh
P=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/dial-mpc

# 1. JAX linear algebra check: Cholesky, solve, cho_solve, eigh and a vmapped solve on a 6x6 float32
#    matrix, after importing dial_core so that XLA_FLAGS is set as in the real command.
#    Prints "RESULT: PASS" and exits 0, or exits 1.
cd $P/tmp/env-probe/attempt2
$H --timeout 300 --log $P/tmp/env-probe/attempt2/jax_linalg_check.log -- \
  $P/dial-mpc-env/bin/python $P/tmp/env-probe/jax_linalg_check.py

# 1b. optional, no JAX: cusolverDnCreate with the libraries now installed
$H --timeout 180 --log $P/tmp/env-probe/attempt2/ctypes_E_env_after_fix.log -- \
  $P/dial-mpc-env/bin/python $P/tmp/env-probe/cusolver_ctypes_check.py --label "E: env after attempt-2 fix"

# 2. probe, small sample count (output_dir is relative to the working directory)
mkdir -p $P/tmp/env-probe/run && cd $P/tmp/env-probe/run
FLASK_RUN_FROM_CLI=true $H --timeout 900 --log $P/tmp/env-probe/attempt2/probe_n4_N128.log -- \
  $P/dial-mpc-env/bin/dial-mpc --config $P/tmp/env-probe/configs/go2_trot_n4_N128.yaml

# 3. only if 2 exits 0: the example's own sample count, 4 steps
FLASK_RUN_FROM_CLI=true $H --timeout 1500 --log $P/tmp/env-probe/attempt2/probe_n4_N2048.log -- \
  $P/dial-mpc-env/bin/dial-mpc --config $P/tmp/env-probe/configs/go2_trot_n4_N2048.yaml

ss -ltnp | grep ':5000'     # must print nothing
```

`jax_linalg_check.py` and `cusolver_ctypes_check.py` were written before the freeze; the first has never
been executed, so a failure in it may also be a bug in the script.

What to read from the probe logs: `heavy.sh` prints the scope's `memory.peak` and the GPU memory in use
before and after (not the peak; sample `nvidia-smi` during the run for that). The tqdm line
`Rollout: ... k/4 [..., s/it, rew=..., freq=...]` gives the time per control step; step 1 of 4 includes
the first compilation (`Ndiffuse_init: 10`), step 2 a second compilation (`Ndiffuse: 2`), steps 3 and 4
are steady state. Success means exit 0, the three files `*_brax_visualization.html`, `*_states.npy`
(4 rows) and `*_predictions.npy` in `tmp/env-probe/run/out_go2_trot_n4_N<N>/`, and no listener on 5000.

## A2.5 Files added or changed in attempt 2

- `dial-mpc-env/` (7 NVIDIA wheels replaced), `reports/environment-requirements.txt` (refreshed),
  this report.
- `tmp/env-probe/attempt2/`: `ctypes_A_env_as_installed.log`, `ctypes_B_only_cublas_12.9.0.13.log`,
  `symbol_check.txt`, `static_symbol_resolution.txt`, `symcheck.sh`, `flask_run_from_cli_check.py`,
  `flask_run_from_cli_check.log`.
- `tmp/env-probe/cusolver_ctypes_check.py`, `tmp/env-probe/jax_linalg_check.py`.
- `tmp/env-probe/resolution/`: `attempt1-freeze.txt`, `attempt2-cuda-12.8.1-pins.txt`,
  `all-resolved-attempt2.txt`.
