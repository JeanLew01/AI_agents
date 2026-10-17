# Environment manager results: gpc (Python route)

**Status: PARTIAL.** The environment is installed and passes `uv pip check`, and every non-heavy check passed.
- The pinned checkout is installed editable from `repo/gpc` at 21a5e069, and hydrax is installed from git at
  cfacc396 (tag v0.0.1).
- FastMCP 4.0.3 (the runtime.md baseline) resolved with no conflict, and an in-memory FastMCP call works.
- The CUDA wheels form one release set (CUDA 12.8.1), and a static ELF symbol check finds 0 missing symbols.

**Nothing that imports jax, jaxlib, flax, optax, evosax, mujoco, mujoco.mjx, hydrax or gpc was run.** Heavy
jobs are disabled in this workspace (`mcp-build/HEAVY_JOBS_DISABLED`; `heavy.sh` exits 75). The JAX device
check, the CUDA-library smoke test, the EGL renderer check (`tests/test_env.py::test_render`) and all
JAX/MuJoCo/gpc import checks are **not attempted: heavy jobs disabled**. The exact commands are in section 8. No
statement in this report says that JAX sees the GPU, that GPU linear algebra works, or that offscreen rendering
works.

Date: 2026-10-12 (install at 17:33:15Z). Host: WSL2 Ubuntu 24.04, kernel 6.6.114.1, 7532 MB RAM (MemAvailable
2485 to 2660 MB during this work), RTX 4070 Laptop GPU 8188 MiB, compute capability 8.9, driver 581.04
(`nvidia-smi` 580.79, CUDA 13.0 reported).

## 1. Interpreter

| item | value |
|---|---|
| PROJECT_ROOT | `/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/gpc` |
| PROJECT_ENV | `/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/gpc/gpc-env` (uv venv, 4.7 GB, outside `repo/`) |
| PROJECT_PYTHON | `/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/gpc/gpc-env/bin/python` |
| Python | 3.12.15, uv-managed CPython at `/home/jixia/.local/share/uv/python/cpython-3.12.15-linux-x86_64-gnu`. Chosen because gpc and hydrax both declare `requires-python >=3.12.0` and upstream `environment.yml` uses `python=3.12`. |
| uv | 0.12.22 |
| packages | 152 (`uv pip list` has 155 lines including the header) |

## 2. Source identity (non-importing checks)

| package | how it is installed | evidence |
|---|---|---|
| gpc 0.0.1 | editable, from `repo/gpc` | `uv pip show gpc`: "Editable project location: .../gpc/repo/gpc". `gpc-0.0.1.dist-info/direct_url.json` = `{"url":"file:///home/jixia/AI_agents/paper2agent/NMPC/mcp-build/gpc/repo/gpc","dir_info":{"editable":true}}`. `__editable__.gpc-0.0.1.pth` loads a setuptools finder whose `MAPPING = {'gpc': '.../gpc/repo/gpc/gpc'}` (no sys.path entry for the repo root). `git -C repo/gpc rev-parse HEAD` = `21a5e069304c09a59f681c9587fa0e73eec8a92d`. |
| hydrax 0.0.1 | from git (regular install, not editable) | `hydrax-0.0.1.dist-info/direct_url.json` = `{"url":"https://github.com/vincekurtz/hydrax","vcs_info":{"vcs":"git","commit_id":"cfacc3964f94d933259d76ec843d1c19e5e1bf8c","requested_revision":"cfacc3964f94d933259d76ec843d1c19e5e1bf8c"}}`. `git ls-remote` gives `refs/tags/v0.0.1` = cfacc396, commit 2025-04-11 15:52:23 -0700 "Loosen deps + introduce `dev` dependency group (#39)". `diff -r -x __pycache__` of the installed `site-packages/hydrax` against a shallow clone of the tag (`tmp/env/hydrax-src-clone/hydrax/hydrax`): exit 0, identical (21 .py files plus the `models/` assets). |

**Repository left unmodified.** `git status --porcelain --ignored --untracked-files=all` was empty before the
install. The editable build (setuptools via uv) created the git-ignored `repo/gpc/gpc.egg-info/` (5 files,
17:33:17Z). It is not on the import path (the finder hook is used instead), so I removed it. Afterwards the
status is empty again at 21a5e069. Nothing in `repo/` was imported, so no `__pycache__` was written there.

hydrax runtime note: only `hydrax/tasks/humanoid_mocap.py` downloads data (`hf_hub_download`, Hugging Face).
The gpc envs import CartPole, Crane, DoubleCartPole, HumanoidStandup, Particle, Pendulum, PushT and Walker,
none of which downloads anything. The selected tools need no network at runtime (static grep only).

## 3. Resolution policy (why the lock is date-bounded)

Every direct pin in `repo/gpc/pyproject.toml` is honoured exactly: jax[cuda12]==0.4.35, flax==0.10.0,
mujoco==3.2.4, mujoco-mjx==3.2.4, evosax==0.1.6, optax==0.2.3, matplotlib==3.9.2, tensorboard==2.18.0,
tensorboardX==2.6.2, cloudpickle==3.1.0, moviepy==1.0.3, imageio==2.27(.0), pytest==8.3.3, ruff==0.7.1,
pre-commit==4.0.1, hydrax@v0.0.1.

The transitive dependencies are not pinned upstream. I first ran a dry-run resolve with no date limit
(`tmp/env/compile-default.txt`, exit 0), and it picked 2026 releases far newer than the late-2024 stack:
- numpy 2.5.4, scipy 1.18.1, ml-dtypes 0.6.0, protobuf 7.36.2.
- setuptools 84.0.0. tensorboard 2.18.0's `tensorboard/default.py` does `import pkg_resources`, so this matters.
- the CUDA 12.9 wheel line with cuDNN 9.27.

None of that has been tested with jax 0.4.35 or jaxlib 0.4.34, and none of it can be tested now. I therefore
resolved the scientific stack **as of the day after upstream last changed its dependencies**. Commit 9902fd8,
2025-04-13, is "Pin hydrax version to v0.0.1"; the earlier pin commits are dated 2024-11-05 to 2025-01-16.
- `--exclude-newer 2025-04-14T00:00:00Z` applies to everything.
- `--exclude-newer-package <pkg>=2026-10-12T00:00:00Z` exempts the 60 packages that only the MCP layer
  (fastmcp 4.0.3 and pytest-asyncio) needs, plus two shared packages the resolver named as conflicts:
  `typing-extensions` (pydantic>=2.12 needs >=4.14.1) and `idna` (httpx2 needs >=3.18). List:
  `tmp/env/exempt-packages.txt`.
- Script: `tmp/env/resolve.sh`. Result: `tmp/env/gpc-env.lock.txt` (sha256
  bfeec4086aaff5cb2958b10aad97ca4def7fbdf5eb7ce77d6521c993a95901ed), installed with `uv pip sync`.
- The full table of the 62 packages that differ from the unbounded resolve is in
  `tmp/env/resolution-diff-latest-vs-locked.txt`.

This is a resolution policy, not a change to any requirement, and it uses the resolver throughout. It is also
what an upstream install on 2025-04-13 would have produced for the scientific packages. It is **not validated
at runtime**.

Key resolved versions:

| group | versions |
|---|---|
| JAX | jax 0.4.35, **jaxlib 0.4.34**, jax-cuda12-plugin 0.4.35, jax-cuda12-pjrt 0.4.35 |
| NN / optim | flax 0.10.0, optax 0.2.3, chex 0.1.89, evosax 0.1.6, orbax-checkpoint 0.11.5, tensorstore 0.1.73 |
| MuJoCo | mujoco 3.2.4, mujoco-mjx 3.2.4, glfw 2.8.0, PyOpenGL 3.1.9, trimesh 4.6.6 |
| numerics | numpy 2.2.4, scipy 1.15.2, ml-dtypes 0.5.1, opt-einsum 3.4.0 |
| logging / IO | tensorboard 2.18.0, tensorboardX 2.6.2 (yanked on PyPI: "protobuf requirement is still needed"; protobuf is installed), protobuf 6.30.2, moviepy 1.0.3, imageio 2.27.0, imageio-ffmpeg 0.6.0 (bundled ffmpeg v7.0.2), pillow 11.2.1, cloudpickle 3.1.0, setuptools 78.1.0 (provides `pkg_resources`) |
| hydrax deps | huggingface-hub 0.30.2 |
| MCP / test | fastmcp 4.0.3 (+ fastmcp-slim 4.0.3), mcp 2.3.0, pydantic 2.14.1, pydantic-core 2.50.1, pytest 8.3.3, pytest-asyncio 1.3.0, anyio 4.15.1, typing-extensions 4.16.0 |
| dev tools (pinned upstream) | ruff 0.7.1, pre-commit 4.0.1 |

The jaxlib version is upstream's own metadata, not a resolver accident. `jax-0.4.35.dist-info/METADATA`
declares `jaxlib==0.4.34; extra == "cuda12"` and `jax-cuda12-plugin[with_cuda]<=0.4.35,>=0.4.34`. A resolve that
forces `jaxlib==0.4.35` fails ("jax[cuda12]==0.4.35 depends on jaxlib==0.4.34"); jaxlib 0.4.35 is not yanked.
The resolver then takes plugin 0.4.35 (the highest allowed).

Static source facts:
- jax 0.4.35 requires jaxlib >= 0.4.34 (`jax/version.py`, checked in `jax/_src/lib/__init__.py`), which passes.
- The plugin's `jax_plugins/xla_cuda12/version.py` says `_minimum_jaxlib_version = "0.4.35"`, but nothing in the
  installed jax, jaxlib or plugin code references it.

So nothing visible in the installed code rejects the 0.4.34/0.4.35 mix. Whether the 0.4.35 PJRT plugin works with
jaxlib 0.4.34 is a runtime question (section 8).

FastMCP: the tested baseline 4.0.3 resolved together with gpc with no conflict, so no other version was needed.
`fastmcp version` notes that 4.1.0 is available; it was not installed (the baseline is kept).

## 4. CUDA wheel set (the dial-mpc pitfall)

`uv pip list` (jax-cuda12-plugin 0.4.35 `with_cuda` extra; every bound is a lower bound, cuDNN <10):

| wheel | version | CUDA release |
|---|---|---|
| nvidia-cublas-cu12 | 12.8.4.1 | 12.8.1 |
| nvidia-cusolver-cu12 | 11.7.3.90 | 12.8.1 |
| nvidia-cusparse-cu12 | 12.5.8.93 | 12.8.1 |
| nvidia-cufft-cu12 | 11.3.3.83 | 12.8.1 |
| nvidia-nvjitlink-cu12 | 12.8.93 | 12.8.1 |
| nvidia-cuda-runtime-cu12 | 12.8.90 | 12.8.1 |
| nvidia-cuda-cupti-cu12 | 12.8.90 | 12.8.1 |
| nvidia-cuda-nvcc-cu12 | 12.8.93 | 12.8.1 |
| nvidia-cudnn-cu12 | 9.8.0.87 | versioned separately (requires only nvidia-cublas-cu12) |
| nvidia-nccl-cu12 | 2.26.2.post1 | versioned separately |

- **One release.** All eight toolkit wheels come from CUDA 12.8.1. This is the same set that dial-mpc attempt 2
  moved to. dial-mpc's failure was cuSOLVER 11.7.4.40 (12.9.0) next to cuBLAS 12.8.4.1, which lacks
  `cublasSetEnvironmentMode`. Here cuSOLVER is 11.7.3.90, the 12.8.1 build. The unbounded resolve would have
  given an all-12.9.1 set with cuBLAS 12.9.2.10, which would also have satisfied that direction.
- **Static symbol check (no dlopen):** `tmp/env/elf_symcheck.sh` → `tmp/env/elf_symcheck.txt`, exit 0. For every
  `.so` under `site-packages/nvidia`, `jax_plugins` and `jax_cuda12_plugin`, each versioned symbol it imports from
  another NVIDIA library (tag `lib{cublas,cublasLt,cusparse,nvJitLink,cusolver,cufft,cudart,cupti,nvrtc,cudnn*,nccl}.so.N`)
  must be defined by the library with that SONAME. Result: **832 imported symbols, 0 missing**. That covers
  libcusolver (138), libcusolverMg (77), libcublas (75), libnvblas (38), libcusparse (8), libcufftw (5) and the
  six cuDNN sub-libraries (49 to 139 each).
- **Library loading:** `xla_cuda_plugin.so` and `jax_cuda12_plugin/*.so` have no `DT_NEEDED` on CUDA libraries.
  They carry `DT_RPATH` entries `$ORIGIN/../../nvidia/{cuda_cupti,cublas,nccl,cuda_runtime,cudnn,cufft,cusolver,cusparse}/lib`,
  so the pip wheels are what gets loaded (`DT_RPATH` comes before `LD_LIBRARY_PATH`). There is no
  `/usr/local/cuda`. The ROS directories in the login `LD_LIBRARY_PATH` contain no libcu*/libnv*/libcudnn*/libEGL/libGL* files.
- **jax version checks** (`jax/_src/xla_bridge.py`) only require installed >= build version (cuSOLVER >= 11.4,
  cuBLAS >= 12.1, cuSPARSE >= 12.1, cuDNN >= 9.1, CUDA runtime >= 12.1); every wheel here is newer.
- **Observation (not a blocker):** `libcudnn_engines_runtime_compiled.so.9` has RUNPATH `$ORIGIN/../../nvrtc/lib`,
  so it can load NVRTC lazily. `nvidia-cuda-nvrtc-cu12` is not installed, because neither cuDNN 9.8.0.87 nor the
  jax plugin declares it. cuDNN's runtime-compiled engines will therefore be unavailable and the precompiled
  engines are used. Upstream installs get the same set.
- **Not verified at runtime**: no CUDA library was loaded and no cuSOLVER handle was created. This rests only on
  static evidence. The JAX probe in section 8 exercises cuBLAS, cuSOLVER, cuDNN and cuFFT.

## 5. Commands and exit statuses (run from PROJECT_ROOT unless noted)

| command | exit | result |
|---|---|---|
| `uv python install 3.12` | 0 | CPython 3.12.15 downloaded (side effect: see section 9) |
| `uv venv gpc-env --python /home/jixia/.local/share/uv/python/cpython-3.12.15-linux-x86_64-gnu/bin/python3.12` | 0 | venv created |
| `uv pip compile tmp/env/requirements.in --python gpc-env/bin/python -o tmp/env/compile-default.txt` | 0 | unbounded dry run (not installed) |
| `uv pip compile` probe `jax[cuda12]==0.4.35` + `jaxlib==0.4.35` | 1 | "No solution": extra pins jaxlib==0.4.34 |
| `tmp/env/resolve.sh tmp/env/compile-combined-D.txt` (rounds 1 and 2 of the exemption loop) | 1, 1 | named typing-extensions, then idna |
| `tmp/env/resolve.sh tmp/env/compile-combined-D.txt` (final) | 0 | lock = `tmp/env/gpc-env.lock.txt` |
| `uv pip sync --python gpc-env/bin/python tmp/env/gpc-env.lock.txt` | 0 | 152 packages, 21.6 s (`tmp/env/install-sync.log`) |
| `rm -r repo/gpc/gpc.egg-info` (build artifact created by the sync) | 0 | repo status empty again |
| `uv pip check --python gpc-env/bin/python` | 0 | "Checked 152 packages ... All installed packages are compatible" |
| `uv pip show gpc hydrax` | 0 | `tmp/env/pip-show-gpc-hydrax.txt` |
| `uv pip list` | 0 | `tmp/env/pip-list.txt` |
| `uv pip freeze > reports/environment-requirements.txt` | 0 | 152 lines; same package set as the lock |
| `gpc-env/bin/python --version > reports/python-version.txt` | 0 | `Python 3.12.15` |
| `tmp/env/elf_symcheck.sh gpc-env/lib/python3.12/site-packages` | 0 | 832 symbols, 0 missing |
| `diff -r -x __pycache__ <installed hydrax> <v0.0.1 clone>` | 0 | identical |
| `env -u PYTHONPATH MPLBACKEND=Agg gpc-env/bin/python -I tmp/env/light_import_check.py tmp/env/light-probe-out` (cwd tmp/env) | 0 | all ok, peak RSS 194 MB, 9.2 s (`tmp/env/light_import_check.json`) |
| `env -u PYTHONPATH gpc-env/bin/fastmcp version` | 0 | FastMCP 4.0.3, MCP 2.3.0, Python 3.12.15 |
| `env -u PYTHONPATH gpc-env/bin/python -I -m pytest --version` | 0 | pytest 8.3.3 |
| `gpc-env/bin/ruff --version`; `gpc-env/bin/pre-commit --version` | 0, 0 | 0.7.1; 4.0.1 |
| `env -u PYTHONPATH gpc-env/bin/python -I -m pytest --co -p no:cacheprovider` | 5 | expected (tests/code is empty): configfile pytest.ini, rootdir PROJECT_ROOT, asyncio mode AUTO |
| `nvidia-smi` | 0 | GPU visible to the driver (does **not** show that JAX sees it) |

## 6. Light (non-heavy) checks: all passed

`tmp/env/light_import_check.py` first installs a `sys.meta_path` blocker that raises ImportError for jax,
jaxlib, jax_plugins, jax_cuda12_*, flax, optax, evosax, mujoco, hydrax, gpc, chex, orbax, tensorflow and torch,
and records every attempt. After the run, none of those modules was in `sys.modules`. The only blocked attempts
were `tensorflow` and `torch`, both optional probes by tensorboard/tensorboardX, and neither package is installed.
- Imports: numpy 2.2.4, scipy 1.15.2, cloudpickle 3.1.0, PIL 11.2.1, imageio 2.27.0, protobuf 6.30.2,
  pydantic 2.14.1, mcp, fastmcp 4.0.3, pytest 8.3.3, pytest_asyncio 1.3.0, tensorboardX 2.6.2, tensorboard 2.18.0,
  yaml, rich.
- matplotlib 3.9.2 with backend Agg: `savefig` wrote a 17290-byte PNG.
- cloudpickle round-trip of a lambda and a numpy array works. gpc's policy pickles themselves need flax/jax and
  are deferred.
- protobuf 6.30.2 with tensorboardX/tensorboard: `SummaryWriter.add_scalar` × 3, then `EventAccumulator`
  read back `[(0,0.0),(1,1.0),(2,2.0)]`.
- `from moviepy.editor import ImageSequenceClip` (the tensorboardX `add_video` path) works and finds the bundled
  ffmpeg. moviepy 1.0.3 prints Python 3.12 `SyntaxWarning`s for invalid escape sequences, which are harmless.
- FastMCP API: `FastMCP(...)`, `@server.tool()`, `async with Client(server)`, `list_tools()` → `['add']`,
  `call_tool('add', {'a': 2, 'b': 3}).data` → `5`. This is in-memory transport only; no port was opened and no
  server was left running.

## 7. Device and offscreen-GL prerequisites (static facts only)

- GPU: `nvidia-smi` shows the NVIDIA GeForce RTX 4070 Laptop GPU, 8188 MiB (about 1.7 GiB in use by other
  processes), compute capability 8.9, driver 581.04. The WSL driver libraries are in `/usr/lib/wsl/lib`
  (libcuda.so.1 and others).
- EGL (needed because every `TrainingEnv` creates a `mujoco.Renderer`):
  - Mesa 25.2.8-0ubuntu0.24.04.2 (`libegl-mesa0`, `libgl1-mesa-dri`).
  - glvnd ICD `/usr/share/glvnd/egl_vendor.d/50_mesa.json` → `libEGL_mesa.so.0`; `libEGL.so.1`, `libGL.so.1`,
    `libOpenGL.so.0` and `libgbm.so.1` are in `ldconfig -p`.
  - DRI drivers `swrast_dri.so`, `kms_swrast_dri.so` and `d3d12_dri.so` are present, and so is `/dev/dxg`.
    **There is no `/dev/dri`.** **OSMesa is absent** (no `libOSMesa` in ldconfig).
  - `DISPLAY=:0` and `WAYLAND_DISPLAY=wayland-0` (WSLg).
- mujoco 3.2.4's backend choice (`mujoco/gl_context.py`) reads `MUJOCO_GL` at import time. `egl` uses
  `mujoco/egl`, which sets `PYOPENGL_PLATFORM=egl` and picks a display through `eglQueryDevicesEXT` +
  `eglGetPlatformDisplayEXT(EGL_PLATFORM_DEVICE_EXT)` (`MUJOCO_EGL_DEVICE_ID` selects one). If `MUJOCO_GL` is
  unset, glfw is used. PyOpenGL 3.1.9 includes `OpenGL/raw/EGL`.
- Without `/dev/dri`, Mesa probably offers only its software (llvmpipe) EGL device on the device platform. That is
  an expectation, not a measurement. If EGL fails, the fallback to try is `MUJOCO_GL=glfw` through WSLg's X server
  (`DISPLAY=:0` must reach the heavy.sh scope). OSMesa is not an option without a system package.
- `import gpc` side effect (`gpc/__init__.py`, read as text): it sets `XLA_PYTHON_CLIENT_MEM_FRACTION=0.9`
  unconditionally and overwrites `XLA_FLAGS` with `--xla_gpu_triton_gemm_any=true `. Any other XLA setting must
  be applied after `import gpc` and before the first JAX computation. `MUJOCO_GL` must be set before mujoco is
  imported, so it belongs in the process environment.

## 8. Deferred: not attempted, heavy jobs disabled

Run these one at a time, only after `mcp-build/HEAVY_JOBS_DISABLED` has been removed by the coordinator or user,
with no other agents active. `--limit-mb 1800` requires MemAvailable >= 3300 MB (MemAvailable was about 2550 MB
today). The commands use `python -I -B`: `-I` ignores PYTHON* variables and `-B` writes no `.pyc` into
`repo/gpc`. heavy.sh already unsets PYTHONPATH and sets `XLA_PYTHON_CLIENT_PREALLOCATE=false`.

```bash
H=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh
P=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/gpc

# 1. Device + CUDA-library check: jax.devices(), cuBLAS matmul, cuSOLVER cholesky/eigh/svd/qr/solve,
#    cuDNN conv, cuFFT; then import gpc/hydrax/mujoco/flax and record origins + XLA env after `import gpc`.
$H --limit-mb 1800 --timeout 600 --log $P/tmp/env/heavy-device-check.log -- \
  env MUJOCO_GL=egl $P/gpc-env/bin/python -I -B $P/tmp/env/heavy_probe_jax.py

# 2. EGL renderer check = upstream tests/test_env.py::test_render, unchanged (expects frames (10, 3, 240, 320)).
#    Run from a scratch cwd with explicit config so nothing is written into repo/gpc.
mkdir -p $P/tmp/env/render-run && cd $P/tmp/env/render-run && \
$H --limit-mb 1800 --timeout 900 --log $P/tmp/env/heavy-test-render.log -- \
  env MUJOCO_GL=egl $P/gpc-env/bin/python -I -B -m pytest -c $P/pytest.ini --rootdir $P/tmp/env/render-run \
  -p no:cacheprovider -q $P/repo/gpc/tests/test_env.py::test_render
#    If EGL fails: repeat with MUJOCO_GL=glfw (WSLg X server) and record which backend works.

# 3. Optional light smoke test of the remaining env/network tests (same pattern):
#    ... -m pytest ... $P/repo/gpc/tests/test_env.py $P/repo/gpc/tests/test_architectures.py
```

What to do if check 1 fails:
- An "incompatible plugin" or PJRT C-API error points to the jaxlib 0.4.34 / plugin 0.4.35 mix. The fallback
  stays inside upstream's declared range: `jax-cuda12-plugin==0.4.34 jax-cuda12-pjrt==0.4.34`.
- A cuSOLVER/cuBLAS internal error contradicts the static evidence in section 4. In that case, record it and
  compare with dial-mpc's `cusolver_ctypes_check.py` approach.

The probe script `tmp/env/heavy_probe_jax.py` was written but never run.

## 9. Side effects, environment hazards and notes for other workers

- **`~/.local/bin/python3.12` symlink (outside my paths).** `uv python install 3.12` created
  `/home/jixia/.local/bin/python3.12 -> ~/.local/share/uv/python/cpython-3.12-linux-x86_64-gnu/bin/python3.12`.
  `~/.local/bin` comes before `/usr/bin` on PATH, so a bare `python3.12` now runs uv's 3.12.15 instead of Ubuntu's
  3.12.3. My attempt to remove the symlink was denied by the permission system, so it is still there. The user may
  want to delete it. gpc-env does not depend on it: it points at the managed install directly.
- **PYTHONPATH leak is real for this env.** The login shell exports
  `PYTHONPATH=/opt/ros/jazzy/opt/gz_math_vendor/lib/python:/opt/ros/jazzy/lib/python3.12/site-packages`. That is
  the same Python minor version, so ROS packages would be importable from gpc-env. Always use
  `env -u PYTHONPATH` or `python -I` (heavy.sh unsets it).
- The login `LD_LIBRARY_PATH` holds ROS directories, and heavy.sh keeps it. A scan found no GL/EGL/CUDA library
  names in them.
- `__pycache__` directories are git-ignored in `repo/gpc`. Use `-B` or `PYTHONDONTWRITEBYTECODE=1`, without `-I`,
  to keep the checkout byte-for-byte clean.
- Stage 5 `src/requirements.txt` must pin the CUDA wheels, numpy, protobuf and setuptools (or reuse the lock).
  A fresh unbounded resolve recreates the untested 2026 set (CUDA 12.9 / cuDNN 9.27 / numpy 2.5.4 / protobuf
  7.36 / setuptools 84).
- Reproduce the environment from PROJECT_ROOT:
  `uv venv gpc-env --python <cpython-3.12.15>` then `uv pip sync --python gpc-env/bin/python tmp/env/gpc-env.lock.txt`.
  The lock has `-e ./repo/gpc`, which is relative to the cwd.

## 10. pytest configuration

`PROJECT_ROOT/pytest.ini` (`[pytest]` section) sets:
- `testpaths = tests/code`
- `norecursedirs = repo gpc-env tmp notebooks src dist .pipeline .git __pycache__`
- `asyncio_mode = auto`, `asyncio_default_fixture_loop_scope = function`

It was verified with `pytest --co` (configfile pytest.ini, asyncio mode AUTO, no config warnings). Upstream tests
under `repo/gpc/tests` would otherwise pick up `repo/gpc/pyproject.toml` `[tool.pytest.ini_options]` as their
rootdir config and write `.pytest_cache` into the repo. Run them with `-c $P/pytest.ini --rootdir <scratch>
-p no:cacheprovider`, as in section 8.

That invocation pattern was checked with a dummy test at `tmp/env/pytest-probe/repo/x/test_dummy.py`. Its path
contains `repo` and `tmp`, both listed in `norecursedirs`. With `-c pytest.ini --rootdir <scratch> -p
no:cacheprovider -I -B` it was collected and passed (exit 0), and it wrote no `__pycache__` or `.pytest_cache`.

No notebook kernel was registered, because the selected tutorials are scripts and tests.

## 11. Unresolved requirements and blockers

1. **Heavy jobs disabled (external, blocking for completion).** Checks 1 and 2 in section 8 are not attempted.
   GPU visibility to JAX, GPU linear algebra and offscreen rendering are unknown.
2. **Memory.** MemAvailable was about 2.5 GB today. heavy.sh with `--limit-mb 1800` needs about 3.3 GB available.
3. Runtime risks to settle with check 1: jaxlib 0.4.34 with plugin 0.4.35 (upstream metadata); NVRTC absent
   (cuDNN runtime-compiled engines unavailable).
4. Runtime risk to settle with check 2: EGL device enumeration without `/dev/dri`; OSMesa is not available.

Setup attempts used: 1 of 3 (one install; the resolve iterations were dry runs).

## Files

- `gpc-env/` (environment); `pytest.ini`
- `reports/environment-requirements.txt` (uv pip freeze, sha256 4f94c573d5bd0c677f725b128ba39673aa1ae11e201fb8677c628f5e316958cd)
- `reports/python-version.txt` (`Python 3.12.15`)
- `tmp/env/`:
  - `requirements.in`, `resolve.sh`, `exempt-packages.txt`, `gpc-env.lock.txt`
  - `compile-default.txt`, `compile-gpc-only-D.txt`, `compile-mcp-only.txt`, `compile-combined-D.txt`, `resolution-diff-latest-vs-locked.txt`
  - `install-sync.log`, `pip-check.log`, `pip-list.txt`, `pip-show-gpc-hydrax.txt`
  - `elf_symcheck.sh`, `elf_symcheck.txt`, `hydrax-installed-vs-tag.diff` (empty), `hydrax-src-clone/` (read-only reference clone of v0.0.1)
  - `light_import_check.py`, `light_import_check.json`, `light-probe-out/`
  - `heavy_probe_jax.py` (not run), `repo-git-status-before.txt` (empty), `pytest-probe/` (dummy-test collection check)
