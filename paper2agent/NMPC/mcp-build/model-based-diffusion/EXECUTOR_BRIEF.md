# Executor brief: model-based-diffusion (CLI route), stage 2

You are a **CLI source executor** for one execution assignment. Establish trustworthy reference results by
running the real upstream command. You do not write wrappers and you do not change the selection.

Read first, in this order:
1. /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/COMMON_BRIEF.md (machine limits; the guarded launcher `heavy.sh` is mandatory)
2. $SKILL_ROOT/references/agents/cli/tutorial-executor-cli.md and $SKILL_ROOT/references/agents/tutorial-executor.md
3. $SKILL_ROOT/references/routes/cli.md, section "Real execution and reference outputs"
4. Your assignment's entry (matched by `execution_id`) in reports/tutorial-scanner-include-in-tools.json: command, effective
   parameters, native outputs, verification basis, risks.

Bound values
- SKILL_ROOT=/home/jixia/.claude/skills/paper2agent/paper2mcp
- PROJECT_ROOT=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/model-based-diffusion
- PROJECT_PYTHON=$PROJECT_ROOT/model-based-diffusion-env/bin/python (Python 3.11.17, jax 0.4.30 CUDA, brax 0.10.5; see reports/environment-manager_results.md)
- Pinned source: $PROJECT_ROOT/repo/model-based-diffusion at commit c1eb913783f1713f7a1ebb657b34e0188d52cd8b. **Never write into it.**
- Your evidence namespace: $PROJECT_ROOT/notebooks/<execution_id>/ ; your report: $PROJECT_ROOT/reports/executed_notebook_<execution_id>.json
- Feasibility already measured by the coordinator: reports/coordinator-feasibility-probe.md

Private source copy (required, because upstream writes its results into `<package parent>/results/<env>/` and several
assignments use the same environment name):
```bash
cd $PROJECT_ROOT && mkdir -p notebooks/<execution_id>/source
git -C repo/model-based-diffusion archive c1eb913783f1713f7a1ebb657b34e0188d52cd8b | tar -x -C notebooks/<execution_id>/source
```
Record how you confirmed that the copy is byte-identical to the pinned commit's tracked files. Run the documented
command with the working directory inside the copy (same relative directory as documented) and
`PYTHONPATH=<absolute path of the copy>` so that `import mbd` resolves to the copy; prove it once with
`heavy.sh -- env PYTHONPATH=<copy> $PROJECT_PYTHON -c "import mbd; print(mbd.__file__)"`. Upstream then writes its
result files inside your copy (`<copy>/results/<env>/`).

Running
- Every Python command goes through
  `/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh --timeout SECONDS --log FILE -- env PYTHONPATH=<copy> $PROJECT_PYTHON <script> <args>`
  (start it from the documented working directory). Keep the launcher's own stderr lines (start, end, peak memory).
  Other executors share the lock, so your command may wait several minutes before it starts; that is normal.
- Keep a small driver script (`notebooks/<execution_id>/run.sh`) with the exact command, and for each run: the
  command line, exit status, complete stdout/stderr log, wall time, and copies of every file upstream wrote
  (`notebooks/<execution_id>/outputs/run1/`, `run2/`), with SHA-256 hashes.
- Run the command twice with identical arguments (the second run is the replay) and compare: printed values parsed
  from the log, array shapes, `numpy.array_equal`, and if not bitwise equal the maximum absolute difference and a
  justified tolerance. State the device (`cuda:0`).
- If the command fails, keep the full traceback and decide per the scanner entry (`execution_risk`, `size_fallback`,
  `rule_if_it_fails`). A failure of the upstream script is a result to report, not something to repair: do not patch
  upstream, do not substitute another method. At most five attempts.

Report (`reports/executed_notebook_<execution_id>.json`): execution id, source path and commit, source URL, status
(`succeeded` / `failed` / `blocked`), execution mode (`native-command`) and `execution_path` (your run.sh), commands
with exit statuses, runtime (interpreter, package versions, device), seed/data provenance, input and output paths with
hashes, parsed reference values, replay comparison, figures (if any), limitations, attempts. Fields without evidence
are null with an explanation. Never invent values. Also write a short human-readable `notebooks/<execution_id>/README.md`.

Finish with a short message: report path, status, the reference values, replay result, anything the coordinator must decide.
