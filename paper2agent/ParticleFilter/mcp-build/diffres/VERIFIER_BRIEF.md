# Independent verifier brief (diffres Paper2MCP, stage 3b)

You are a fresh agent: you did not implement any of these tools. Read first, completely:
1. `/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/COMMON_BRIEF.md` (machine limits; JAX only via `heavy.sh`)
2. `/home/jixia/.claude/skills/paper2agent/paper2mcp/references/agents/test-verifier-improver.md` (your role, authoritative)
3. "Independent verifier" section of `/home/jixia/.claude/skills/paper2agent/paper2mcp/references/tool-selection-and-wrapping.md`
4. `/home/jixia/.claude/skills/paper2agent/paper2mcp/references/runtime-verification.md`
5. "Python tool format" in `/home/jixia/.claude/skills/paper2agent/paper2mcp/references/agents/tutorial-tool-extractor-implementor.md`
6. `IMPLEMENTER_BRIEF.md` (shared I/O contracts), your module's `reports/implementation-<module>.json`, the scanner's
   `reports/tutorial-scanner.json`, and the execution evidence named in your assignment.

Bound values: `PROJECT_ROOT=/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres`,
`PROJECT_PYTHON=$PROJECT_ROOT/diffres-env/bin/python`, `HEAVY=/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/heavy.sh`.
Upstream `diffres` @ 767effe (editable install of `repo/diffres`; never modify `repo/`). The paper is available as a
skill package at `/home/jixia/AI_agents/paper2agent/ParticleFilter/dist/particle-filter-agent/skill/diffusion-resampling-paper/`
(`references/paper.md`) if you need to check a scientific statement made in a docstring.

Work rules:
- Tests: one file per exposed tool in `tests/code/<module>/test_<tool>.py`, fixtures in `tests/data/<module>/`,
  results/logs in `tests/results/<module>/` and `tests/logs/<module>/`. Call tools through
  `fastmcp.Client(<module>_mcp)` and `result.data`; expected failures must surface as MCP tool errors.
- Expected values come from the executors' saved upstream outputs and from your own **direct upstream calls**
  (import `diffres` yourself; never use the wrapper's output as the oracle). Use bitwise equality where both sides
  run the same jitted/unjitted path, otherwise a justified tolerance (eager vs jit differences up to ~1e-12 were
  observed). Include changed inputs (other N, d, seeds/keys, parameters), invalid inputs, repeated-call artifact
  isolation, and, for tools that consume another module's artifacts, a composition test that builds its input with
  a direct upstream call (do not import another module's wrapper as a dependency of your verdict; you may add one
  composition test calling the other tool through its own Client, clearly labelled).
- Review the wrapper for faithful reuse: trace every computation to upstream; flag invented maths, unjustified
  input restrictions or generalisations (and check each against upstream code), duplicated algorithms, ignored or
  altered parameters/defaults, and scientific claims in docstrings/notes that the code or paper does not support.
- Keep test runs small and run pytest through `$HEAVY --limit-mb 1500 --timeout 1800 -- $PROJECT_PYTHON -m pytest ...`
  (lower limits fine). Avoid N above ~2000 for diffusion/OT/gumbel (N x N arrays).
- Repairs: you own `src/tools/<module>.py` during verification and may repair it within the bounded policy
  (at most six attempts per tool), rerunning affected tests. Record every change.
- Handoff files: `reports/verification-<module>.json` (with `implementation_run_id`, tested-file sha256 after your
  last change, commands/exits, test totals, repairs, limitations) and `reports/mcp-acceptance-<module>.json`
  (runtime-acceptance schema; use absolute paths under `$PROJECT_ROOT/tests/data/...` for inputs and
  `$PROJECT_ROOT/tmp/outputs/acceptance` as `artifact_root`/`output_dir`; at least one successful case per tool with
  stable `expected_subset` fields, error cases, a repeated call for file-producing tools).
- Final message 5-12 lines: report paths, test totals, repairs, open problems.
