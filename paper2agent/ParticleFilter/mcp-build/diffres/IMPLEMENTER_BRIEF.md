# Implementer brief (diffres Paper2MCP, stage 3a)

Read first, completely:
1. `/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/COMMON_BRIEF.md` (machine limits; JAX only via `heavy.sh`)
2. `/home/jixia/.claude/skills/paper2agent/paper2mcp/references/agents/tutorial-tool-extractor-implementor.md` (role; its "Python tool format" is mandatory)
3. The "Implementer" section of `/home/jixia/.claude/skills/paper2agent/paper2mcp/references/tool-selection-and-wrapping.md`
4. `/home/jixia/.claude/skills/paper2agent/paper2mcp/references/runtime.md`, "Stage 3"
5. `reports/tutorial-scanner.json` (`tool_review` for your tools) and the execution reports named in your assignment
   (`reports/executed_notebook_<id>.json` + `notebooks/<id>/`), which hold the reference inputs/outputs.

Bound values: `PROJECT_ROOT=/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres`,
`PROJECT_PYTHON=$PROJECT_ROOT/diffres-env/bin/python`, `HEAVY=/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/heavy.sh`,
upstream package `diffres` (editable install of `repo/diffres` @ 767effe; never modify `repo/`).
`REFERENCE` URLs use `https://github.com/zgbkdlm/diffres/blob/767effe3e755067eb8a04422597fbf37eb8ab754/<path>`.

## Shared contracts (all three modules must follow them so the tools compose)
- FastMCP 4.0.3. File `src/tools/<module>.py`, instance `<module>_mcp = FastMCP(name="<module>")`.
  Module docstring names the upstream sources. No shared helper module: each module is self-contained.
- Precision: upstream experiments/tests run with `jax.config.update("jax_enable_x64", True)`; do the same at import
  time in every module (CPU float64). Never select a GPU.
- Randomness: parameter `seed: int` (default 0) -> `jax.random.PRNGKey(seed)`; plus optional
  `prng_key: list[int] | None` (exactly two uint32 values = raw `PRNGKey` data) that, if given, is used instead, so a
  verifier can reproduce reference runs that used a split key. Return the key actually used.
- Weighted particle input (resampling, possibly PF output): `particles_path` = `.npz` with `samples` (N, d) float
  and either `log_weights` (N,) or `weights` (N,) (exactly one). 1-D `samples` is (N,) -> treat as (N, 1) only if the
  upstream code needs 2-D; say what you do. Upstream resamplers assume normalised log weights; every upstream
  caller normalises first (`log_ws - logsumexp(log_ws)`), so the wrapper normalises the same way and reports the
  input's log normaliser; reject non-finite values and all -inf weights with a clear error.
- Resampling output: `.npz` with `samples`, `log_weights` (as returned by upstream) in a fresh per-call directory
  under `output_dir` (default: `$PROJECT_ROOT/tmp/outputs/<tool>/<uuid>`; make the base configurable by the
  `output_dir` parameter, create a fresh unique subdirectory per call). Return ESS of input and output, N, d,
  resolved settings, artifact paths. Never return full arrays.
- LGSSM specification: `model_path` = JSON file with keys `F` (dx x dx), `Q` (dx x dx), `H` (dy x dx), `R` (dy x dy),
  `m0` (dx), `P0` (dx x dx) -- the upstream names are semigroup, trans_cov, obs_op, obs_cov, m0, v0.
  Observations: `observations_path` = `.npz` with `ys` of shape (T+1, dy); `ys[0]` is the observation at time 0
  (upstream `kf` and `smc_feynman_kac` condition on y_0, and `simulate_lgssm` returns T+1 states/observations).
  The simulate tool writes `data.npz` with `xs` (T+1, dx) and `ys` (T+1, dy), plus a copy `model.json`.
- Gradients (optional flags): gradient of the returned negative log-likelihood with respect to the full matrices
  F and H via `jax.grad`, as in demos/gradient_variance2.py / experiments/lgssm (they parametrise scalars; the matrix
  form is the general case and the executor `lgssm_gradient_demo` saved it as dF/dH). Save gradients to the artifact
  and return their Frobenius norms only.
- Known upstream property to document, not "fix": `smc_feynman_kac` returns a negative log-likelihood that is
  offset by -log(N) relative to the exact one (time-0 term `-logsumexp(log_g0)` without `+log N`, feynman_kac.py
  lines 82-85; see executor reports filters_tests and lgssm_gradient_demo). Return the raw upstream value as `nll`;
  you may additionally return `nll_plus_log_n = nll + log(N)` labelled as a convenience, documented in the docstring/report.
- Tests and smoke checks: run any Python that imports JAX through `$HEAVY --limit-mb 1200 --timeout 1200 -- ...`.
  Keep smoke checks small. Do not write tests under `tests/code/` (the verifier owns them); your smoke scripts go to
  `tmp/impl-<module>/`.

## Handoff
`reports/implementation-<module>.json` as the role specifies (tool -> upstream call map, parameter/default
choices, I/O adaptations, smoke outcomes, sha256 of each production file). Final message 5-12 lines.
