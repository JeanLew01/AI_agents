# Environment manager results: diffres

Date: 2026-10-03 (UTC). Role: Python environment manager (stage 1). Route: python, CPU-only JAX.

## Interpreter and environment

| Item | Value |
|---|---|
| PROJECT_ENV | `/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/diffres-env` (uv venv, 1.1 GB) |
| PROJECT_PYTHON | `/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/diffres-env/bin/python` |
| Python | CPython 3.11.17 (uv-managed, `~/.local/share/uv/python/cpython-3.11-linux-x86_64-gnu`) |
| uv | 0.12.22 |
| Why 3.11 | pyproject says `requires-python >=3.10`, but its pins `jax==0.7.2`/`jaxlib==0.7.2` and `numpy==2.3.3` need Python >= 3.11; 3.11 was already available locally. |

## Source identity

- Repository: https://github.com/zgbkdlm/diffres, checkout `repo/diffres`, `git rev-parse HEAD` = `767effe3e755067eb8a04422597fbf37eb8ab754` (matches the pin).
- Installed as an editable install (`uv pip install -e repo/diffres`): distribution `diffres 0.0.1`; `direct_url.json` = `file:///home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres/repo/diffres`, `editable: true`; finder `__editable___diffres_0_0_1_finder.py`.
- Import origin (checked under heavy.sh): `diffres.__file__` = `.../diffres/repo/diffres/diffres/__init__.py`. Every submodule resolves into `repo/diffres/diffres/`.
- The checkout was left unmodified. The setuptools build left an untracked `repo/diffres/diffres.egg-info/`, which I deleted. The first import left a `diffres/__pycache__/`, which I also deleted. Later runs used `PYTHONDONTWRITEBYTECODE=1` and `-p no:cacheprovider`. At the end, `git status --short --ignored` in the checkout shows nothing.

## Resolved key versions (full list: reports/environment-requirements.txt, 172 packages)

Upstream pins are all satisfied exactly: jax 0.7.2, jaxlib 0.7.2 (CPU wheel), numpy 2.3.3, scipy 1.16.2, matplotlib 3.10.6, ott-jax 0.5.2, optax 0.2.6, flax 0.12.0. Unpinned upstream deps resolved to: diffrax 0.7.2, equinox 0.13.8, orbax-checkpoint 0.12.6, jaxopt 0.8.5, pytest 9.1.1.

MCP/test/notebook tooling: fastmcp 4.0.3 (mcp 2.3.0, pydantic 2.13.5; `fastmcp version` OK), pytest-asyncio 1.4.0, papermill 2.7.0, nbclient 0.11.0, ipykernel 7.4.0, jupytext 1.19.5. The tested baseline fastmcp==4.0.3 resolved together with the research pins without any conflict.

Undeclared imports of `diffres/data.py` (`mnists`, `dm_pix`, `datasets`) are installed at the versions given in `repo/diffres/experiments/README.md`: mnists 0.4.1, dm-pix 0.4.4, datasets 4.8.4 (this pulls in pyarrow 25.0.1). Without them `import diffres.data` fails. They are only needed for the CIFAR-10 image experiment, which is out of scope. The README's evaluation-only extras (torch CPU, torchmetrics 1.9.0) were **not** installed. No nvidia/CUDA/torch/tensorflow wheels are present in the install log.

## Commands and exit statuses

| # | Command (from PROJECT_ROOT) | Exit | Log |
|---|---|---|---|
| 1 | `uv venv diffres-env --python 3.11` | 0 | tmp/env-probe/01_venv.log |
| 2 | `uv pip install --python $P -e repo/diffres 'fastmcp==4.0.3' pytest pytest-asyncio papermill nbclient ipykernel jupytext 'mnists==0.4.1' 'datasets==4.8.4' 'dm-pix==0.4.4'` | 0 | tmp/env-probe/02_install.log |
| 3 | `uv pip check --python $P` -> "All installed packages are compatible" (172 packages) | 0 | tmp/env-probe/03_pipcheck.log |
| 4 | `$P -m ipykernel install --prefix $PROJECT_ENV --name diffres-p2a --display-name "Python (diffres-p2a)"` | 0 | tmp/env-probe/04_kernel.log |
| 5 | `heavy.sh --limit-mb 1200 --timeout 900 -- $P tmp/env-probe/probe_imports.py` (JAX devices, import all diffres modules, versions) | 0, peak 387 MB, 25 s | tmp/env-probe/05_imports.log |
| 6 | `uv pip freeze --python $P > reports/environment-requirements.txt`; `$P --version > reports/python-version.txt` | 0 | — |
| 7 | Upstream tests, one file per heavy.sh job (see below) | see table | tmp/env-probe/06_*, 07_*, junit_*.xml |
| 8 | Derived reduced-size smoke check (see below) | 1 | tmp/env-probe/08_resampling_reduced_n1000.log |

`$P` = PROJECT_PYTHON. Every JAX-importing command ran through `/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/heavy.sh`, which sets `JAX_PLATFORMS=cpu`, `CUDA_VISIBLE_DEVICES=` empty, no PYTHONPATH and `MPLBACKEND=Agg`. There was one exception. I ran `pytest --collect-only` once outside heavy.sh by mistake. It crashed during pytest plugin loading (the leaked login-shell PYTHONPATH) before the test module imported JAX, so no JAX job ran outside the launcher. I then repeated it through heavy.sh (exit 0, peak 231 MB, 14 tests collected).

## Device and kernel configuration

- `jax.devices()` = `[CpuDevice(id=0)]`, `jax.default_backend()` = `cpu`. GPU memory in use stayed at 0 MiB before and after every job. No GPU was used.
- `diffres.data`, `feynman_kac`, `gaussian_filters`, `integators`, `nns`, `resampling`, `tools` and `typings`: all 8 modules import OK.
- Jupyter kernel `diffres-p2a` is installed at `diffres-env/share/jupyter/kernels/diffres-p2a/kernel.json`. Its argv[0] is the PROJECT_PYTHON path above. The name was not used before: the user-level kernels contain only `jax-venv`, and `/usr/share/jupyter` and `/usr/local/share/jupyter` have no kernels. `diffres-env/bin/jupyter kernelspec list` lists `diffres-p2a` under PROJECT_ENV. Run papermill with `$P -m papermill ... --kernel diffres-p2a`. heavy.sh sets `MPLBACKEND=Agg`.

## pytest configuration

`pytest.ini` (new) in PROJECT_ROOT:
```
[pytest]
testpaths = tests/code
asyncio_mode = auto
asyncio_default_fixture_loop_scope = function
```
It was in effect for the upstream runs below; it does not change sync upstream tests.

## Upstream unit tests (repo/diffres/tests @767effe, unchanged)

Invocation: `heavy.sh --limit-mb L --timeout 900 --log ... -- env PYTHONDONTWRITEBYTECODE=1 $P -m pytest -p no:cacheprovider -v --durations=0 --junitxml=... <file or node id>`.

| File | Test | Result | Call time |
|---|---|---|---|
| test_filters.py (L=1200; whole file 56.5 s; **peak 566 MB**) | test_kf | PASSED | 0.15 s |
| | test_smc[multinomial] | PASSED | 3.31 s |
| | test_smc[multinomial_stopped] | PASSED | 1.06 s |
| | test_smc[stratified] | PASSED | 1.10 s |
| | test_smc[systematic] | PASSED | 0.89 s |
| | test_diffres[euler] | PASSED | 6.91 s |
| | test_diffres[lord_and_rougemont] | PASSED | 6.22 s |
| | test_diffres[jentzen_and_kloeden] | PASSED | 7.35 s |
| | test_diffres[tweedie] | PASSED | 6.88 s |
| | test_ensemble_ot | PASSED | 11.33 s |
| test_integrators.py (L=1200; 68.4 s; **peak 744 MB**) | test_integrators | PASSED | 59.87 s |
| test_resampling.py, whole file (L=1200) | first test | **OOM-killed** (exit 143, systemd `oom-kill`) after about 15 s | — |
| test_resampling.py, per node id (L=1900) | test_misc_resamplings[<lambda>0] (soft) | **OOM-killed** at 1900 MB | — |
| | test_misc_resamplings[<lambda>1] (gumbel) | **OOM-killed** at 1900 MB | — |
| | test_diffres_versions | PASSED, 34.7 s, **peak 1877 MB** | — |
| | test_ensemble_ot | **OOM-killed** at 1900 MB | — |
| | test_diffres[True-euler] | **OOM-killed** at 1900 MB | — |
| | test_diffres[False-euler] | **OOM-killed** at 1900 MB | — |
| | test_diffres[True/False-lord_and_rougemont, jentzen_and_kloeden, diffrax, tweedie] (8 ids; 2 of them skip upstream) | **not attempted**: heavy.sh refused (exit 75, MemAvailable about 3810 MB < 1900 + 2000) | — |

Summary: 12/12 tests in test_filters.py and test_integrators.py pass. In test_resampling.py, 1/14 passed, 5 were OOM-killed at the largest limit the launcher allows on this machine, and 8 were not attempted.

Cause: test_resampling.py enables `jax_enable_x64` and hardcodes `nsamples = 10000` at module level. The code builds n x n float64 objects, for example `gumbel_softmax` vmaps a length-n softmax over n keys, and `ensemble_ot` returns `out.matrix` (n x n). One 10000 x 10000 float64 array is 800 MB. These tests need more than 1.9 GB per test, but heavy.sh allows at most `MemAvailable - 2000` MB, about 1.8 to 2.1 GB here. The test exposes no size parameter. I did not change the upstream test, and I did not loop further on exit 75. My per-test runner did issue the 8 refused calls back to back before stopping.

### Derived smoke check (NOT upstream validation)

`tmp/env-probe/test_resampling_reduced_n1000.py` is a copy of the upstream test with one change, `nsamples = 10000 -> 1000`, plus a header comment. It ran with L=1200: **peak 872 MB**, 45.9 s, exit 1, with 2 passed (test_diffres_versions, test_ensemble_ot), 2 skipped (upstream skips) and 10 failed. All 10 failures are `assert_allclose(swd, 0, atol=1e-4 / 1e-3)` with SWD between 0.00099 and 0.0021. That is Monte Carlo error at n=1000, about 1/sqrt(10) larger than at the upstream n=10000. Every resampler and integrator path in that file runs without errors under this environment. Accuracy at the upstream tolerances is **not** established for those tests.

## Unresolved requirements / blockers

1. **Memory:** the upstream `tests/test_resampling.py` cannot run within the machine's guarded memory budget (more than 1.9 GB per test at n=10000, float64). The 13 OOM-killed or not-attempted tests are unverified. To run them, the coordinator would need to allow a heavy.sh limit of about 3 GB or more when that much memory is free. Otherwise later stages should treat the tolerances as calibrated for n=10000 and use smaller sizes only as smoke checks.
2. Torch/torchmetrics (CIFAR-10 evaluation only) were not installed; CIFAR-10 is out of scope. `diffres.data` would download datasets from the Hugging Face hub or the network at run time. That was not exercised.
3. A successful import plus the passing filter/integrator tests is not scientific validation of the paper's results.
4. No notebook was executed at this stage. The kernel is registered but has not been exercised by papermill yet.
