# diffres MCP server

MCP tools for **diffusion differentiable resampling** and particle filtering, wrapping the authors' code
[`zgbkdlm/diffres`](https://github.com/zgbkdlm/diffres) at commit `767effe3e755067eb8a04422597fbf37eb8ab754`
(J. R. Andersson and Z. Zhao, "Diffusion differentiable resampling", ICML 2026, arXiv:2512.10401).
All computation is done by the upstream `diffres` package; the tools only read inputs, call it and save results.

## What you can do

| Tool | Use it to |
| --- | --- |
| `diffres_resample_particles_diffusion` | Resample your weighted particles with diffusion resampling (the paper's method) |
| `diffres_resample_particles_baseline` | Resample the same particles with multinomial, stratified, systematic, stopped-gradient multinomial, entropic-OT, soft or Gumbel-softmax resampling, for comparison |
| `diffres_run_lgssm_particle_filter` | Run a bootstrap particle filter on a linear Gaussian state-space model (LGSSM) with any of these resamplers; get the log-likelihood estimate, ESS, filtering moments, optionally its gradient w.r.t. F and H and the error against the exact Kalman filter |
| `diffres_run_lgssm_kalman_filter` | Exact Kalman filter (and RTS smoother) for the same model: exact log-likelihood, moments, gradient |
| `diffres_simulate_lgssm_data` | Simulate states and observations from an LGSSM to feed the two filter tools |

Not included (see "Scope and limits"): nonlinear/non-Gaussian models, parameter optimisation, the paper's
image, Lotka-Volterra, Bayesian-neural-network and weather experiments, and the generic diffusion resampler with a
user-defined reference.

## Requirements

- Linux or macOS with **Python 3.11** (tested: CPython 3.11.17 on Ubuntu 24.04 under WSL2, CPU only).
- Internet access and `git` during installation (PyPI and GitHub; `diffres` is installed from the pinned Git commit).
- No GPU needed. The server forces `JAX_PLATFORMS=cpu` unless you set `JAX_PLATFORMS` yourself.
- Memory: the diffusion, entropic-OT and Gumbel-softmax resamplers build N x N float64 arrays. N = 1000 needs
  well under 1.5 GB; keep N to a few thousand.

## Install

From this folder (the one containing `USAGE.md`):

```bash
python3.11 -m venv .venv            # or: uv venv .venv --python 3.11
.venv/bin/python -m pip install -r requirements.txt   # or: uv pip install --python .venv/bin/python -r requirements.txt
```

## Start the server

The server speaks MCP over stdio:

```bash
.venv/bin/python src/diffres_mcp.py
```

Register it with Claude Code (run from this folder; absolute paths keep it working from any directory):

```bash
claude mcp add diffres -- "$PWD/.venv/bin/python" "$PWD/src/diffres_mcp.py"
```

Other clients: `fastmcp install --help` (from the installed environment) lists generators for Claude Desktop,
Cursor, Gemini CLI, Goose and plain MCP JSON; point them at `src/diffres_mcp.py` and this environment's Python.

Outputs go to a fresh subfolder per call, under `tmp/outputs/<tool>/` in this folder unless you pass `output_dir`.
Every tool returns a JSON summary plus the absolute paths of its result files.

## Input formats

- **Weighted particles** (`particles_path`): `.npz` with `samples` (N, ...) and exactly one of `log_weights` (N,) or
  `weights` (N,). Weights are normalised before resampling (as upstream callers do); zero weights are allowed.
- **LGSSM** (`model_path`): JSON with `F` (dx x dx), `Q` (dx x dx), `H` (dy x dx), `R` (dy x dy), `m0` (dx),
  `P0` (dx x dx), meaning x_k = F x_{k-1} + N(0, Q), y_k = H x_k + N(0, R), x_0 ~ N(m0, P0). Q, R, P0 must be
  symmetric positive definite.
- **Observations** (`observations_path`): `.npz` with `ys` of shape (T+1, dy); `ys[0]` is the time-0 observation.

Randomness: `seed` (integer) or `prng_key` (two uint32 numbers, raw JAX key) for exact reproduction.

## Tools

### `diffres_resample_particles_diffusion`
Required: `particles_path`. Main options: `a` (negative mean-reverting coefficient, default -2), `T` (terminal time,
default 1), `nsteps` (integration steps K, default 32; the time grid is linspace(0, T, K+1)), `integrator`
(`euler` default, `jentzen_and_kloeden`, `lord_and_rougemont`, `tweedie` with `ode=false`, `diffrax` with
`ode=true`), `ode` (probability-flow ODE, default true, or reverse SDE), `jitter`, `seed`/`prng_key`,
`output_dir`. Output: `resampled.npz` (`samples`, `log_weights`), input and output ESS.
The paper's best Gaussian-mixture setting is `integrator=jentzen_and_kloeden`, `ode=true`, T = 3, K = 128.

### `diffres_resample_particles_baseline`
Required: `particles_path`. `method` = `multinomial` (default), `stratified`, `systematic`, `multinomial_stopped`,
`ensemble_ot` (`eps`, default 1/log N), `soft` (`alpha`, default 0.5; returns non-uniform weights),
`gumbel_softmax` (`tau`, default 0.5). A method-specific parameter given for another method is an error.
Output: `resampled.npz`, ESS.

### `diffres_run_lgssm_particle_filter`
Required: `model_path`, `observations_path`. Options: `nparticles` (32), `resampling_method` (`diffusion` default or
any baseline), `resampling_threshold` (1.0 = resample every step), the method's parameters (`diffusion_a` -0.5,
`diffusion_T` 3, `diffusion_steps` 8, `diffusion_integrator`, `diffusion_ode`, `diffusion_jitter`, `ot_eps`,
`ot_implicit_diff`, `soft_alpha`, `gumbel_tau`), `save_particle_path`, `compute_gradient` (gradient of the nll
w.r.t. F and H), `compare_to_kalman`, `seed`/`prng_key`, `output_dir`.
Output: `particle_filter.npz` (final particles `samples`/`log_weights`, which the resampling tools accept directly,
ESS, weighted filtering means/covariances, optional path, gradients, Kalman moments and per-step errors) and a
JSON summary.

Read these two conventions before comparing numbers:
- `nll` is the raw upstream value. It is lower than the exact negative log-likelihood by log N, because upstream
  omits the 1/N factor at time 0; `nll_plus_log_n` adds it back and is the one to compare with the Kalman nll.
  Gradients are unaffected.
- With `compare_to_kalman`, `kl` is the upstream `diffres.tools.kl`, which equals **2 x KL**(Kalman || particle
  Gaussian), and `bures` is the **squared** 2-Wasserstein distance between those Gaussians.

### `diffres_run_lgssm_kalman_filter`
Required: `model_path`, `observations_path`. Options: `smooth` (RTS smoother), `compute_gradient`, `output_dir`.
Output: exact `nll`, `kalman_results.npz` (filtering and predictive means/covariances, smoother outputs,
gradients).

### `diffres_simulate_lgssm_data`
Required: `model_path`, `nsteps` (T). Options: `seed`/`prng_key`, `output_dir`. Output: `data.npz` (`xs` (T+1, dx),
`ys` (T+1, dy)) and a copy `model.json`, ready for the two filter tools.

Typical chain: simulate -> Kalman filter (exact reference) -> particle filter with `resampling_method=diffusion` and
with a baseline -> compare `nll_plus_log_n`, gradients and `kl` per step.

## How it was validated

- Reference runs of the unmodified upstream code (demo notebook, single-seed Gaussian-mixture and LGSSM experiment
  scripts at reduced size, the gradient demo, `tests/test_filters.py`); every run was replayed from saved inputs
  with bitwise identical results.
- Independent verification per tool module against those references and new direct upstream calls:
  223 tests (resampling 99, particle filter 66, Kalman filter/simulation 58), all passing. The tools reproduce the
  upstream outputs bitwise when called with the same key; eager-vs-jitted differences are below 1e-12.
- Real MCP calls over stdio: 47 acceptance cases (23 successful calls covering all 5 tools, repeated calls, 24
  input-error cases) passed in the development environment, in a freshly installed environment, and after
  extracting this package to a new location; returned files were compared with the upstream references.

## Scope and limits

- Results are those of the upstream implementation. Single small runs reproduce upstream outputs; they do not
  reproduce the paper's tables, which average 100 runs at larger N.
- Upstream `tests/test_resampling.py` (N = 10,000) was not run: it needs more than 3 GB of memory on the test
  machine. Its test bodies were run at N = 1000 as property checks only.
- Only linear Gaussian state-space models are supported by the particle-filter tool; models given as Python code,
  parameter estimation (L-BFGS in the paper's LGSSM experiment), loss-landscape grids, CIFAR-10/BNN, Lotka-Volterra,
  pendulum and weather experiments are not exposed.
- Upstream `gumbel_softmax` handles only (N,) or (N, d) samples; `ensemble_ot` likewise.
- Tested only on Linux x86-64 CPU with the pinned versions in `requirements.txt`; other jaxlib builds may differ
  from the references at round-off level.

## License and provenance

`diffres` is licensed under the Mozilla Public License 2.0 (see `LICENSE-diffres`); it is installed from the
pinned commit, not modified. `src/tools/*.py` call it and contain small adapted excerpts of its tests and
experiment scripts (bootstrap model construction, resampler wrappers), marked with their source locations; those
excerpts remain under MPL-2.0.
