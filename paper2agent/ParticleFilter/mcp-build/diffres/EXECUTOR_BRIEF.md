# Executor brief (diffres Paper2MCP, stage 2)

Read first, completely:
1. `/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/COMMON_BRIEF.md` (machine limits; every JAX command goes through `heavy.sh`)
2. `/home/jixia/.claude/skills/paper2agent/paper2mcp/references/agents/tutorial-executor.md` (your role, authoritative)
3. `/home/jixia/.claude/skills/paper2agent/paper2mcp/references/runtime.md`, section "Stage 2"
4. Your source's entry in `reports/tutorial-scanner.json` (`tool_review`, `proposed_executor_assignments`) and
   `reports/environment-manager_results.md`.

Bound values:
- `PROJECT_ROOT=/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres`
- `PROJECT_PYTHON=$PROJECT_ROOT/diffres-env/bin/python`, notebook kernel `diffres-p2a`
- `HEAVY=/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/heavy.sh`
- Source: `repo/diffres` at commit 767effe3e755067eb8a04422597fbf37eb8ab754. **Never modify anything under `repo/`.**
  Scripts that read `rnd_keys.npy` or write `./results/...` relative to the working directory must run from a
  scratch working directory inside your namespace (copy or symlink `repo/diffres/experiments/rnd_keys.npy` there and
  create the result folders it expects), invoking the script by its absolute path in `repo/`.
- Your evidence namespace: `notebooks/<execution_id>/` (driver/executed notebook, `data/`, outputs, `images/`, logs).
  Your report: `reports/executed_notebook_<execution_id>.json`. You own nothing else.

Rules specific to this project:
- Run everything through `$HEAVY --limit-mb 1500 --timeout 1800 -- ...` (lower limits are fine; never higher).
  Other executors share the machine-wide lock, so your command may wait for the lock; that is normal.
- Use the smallest upstream-supported settings given in your assignment. Record exact commands, the changed
  arguments relative to upstream defaults / `run_*.sh`, exit status, runtime, and the peak memory printed by heavy.sh.
- Save what later lets an independent verifier reproduce results with a *direct upstream call*: the exact inputs
  (keys/seeds, arrays as .npz or .npy with float64 where upstream uses x64), the upstream function arguments, and the
  native outputs with full precision. Where useful, add a small driver that loads the saved inputs and calls the same
  upstream functions once more (replay), and compare (exact for integers/identifiers; justified tolerance otherwise).
  A driver may prepare inputs and capture results; it must not re-implement the algorithm.
- JAX determinism: same key + same inputs + same x64 setting on CPU should replay bitwise or to ~1e-12; report what
  you observe.
- At most five execution attempts. If something cannot run within the memory limits, stop, record it as failed or
  blocked with evidence, and do not work around it with a different method.
- Final message (5-12 lines): report path, status, key reference numbers, peak memory, blockers.
