# Common brief for all Paper2MCP agents in this workspace

You work inside a Paper2Agent `paper2mcp` conversion coordinated by another agent. The skill lives at
`SKILL_ROOT=/home/jixia/.claude/skills/paper2agent/paper2mcp`. Your assignment names the role file(s) under
`$SKILL_ROOT/references/` that you must read first and follow; those files are authoritative for your role.

## Machine limits (shared laptop, other sessions are running on it)
- WSL2 Ubuntu 24.04, 16 CPU threads, **about 7.5 GB RAM in total with little free**, 2 GB swap,
  one NVIDIA RTX 4070 Laptop GPU with **8 GB** memory (driver 581.04). No sudo. No conda.
- `uv` is at `/home/jixia/.local/bin/uv` (use it for environments and installs; it can download Python versions).
- Any command that imports JAX (even a one-line import check), runs diffres code, tests or notebooks is a
  "heavy job". **Mandatory:** start every heavy job through the guarded launcher and nothing else:
  `/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/heavy.sh [--limit-mb N] [--timeout SECONDS] [--log FILE] -- <command> [args...]`
  It takes a lock shared with the sibling NMPC workspace (one heavy job at a time on the machine), refuses to start
  with exit status 75 when free memory is too low (needs MemAvailable >= limit + 2500 MB; default limit 1200 MB, maximum 1500 MB),
  runs the command in a memory-limited systemd scope without swap (killed with status 137 if it needs more; the
  machine survives), forces **CPU-only JAX** (`JAX_PLATFORMS=cpu`, `CUDA_VISIBLE_DEVICES=` empty), sets
  `XLA_PYTHON_CLIENT_PREALLOCATE=false` and `MPLBACKEND=Agg`, removes `PYTHONPATH` (ROS 2 leaks into the login
  shell; if your command needs it, set it inside: `env PYTHONPATH=... python ...`), and prints peak memory.
  Background: on 2026-10-02 two GPU JAX jobs in the NMPC workspace froze the whole WSL machine. Do not bypass the
  launcher, do not call `flock`/`systemd-run` yourself, never use the GPU, and do not loop on exit status 75: try
  at most three times a few minutes apart, then report "not attempted". Package installs with `uv` that do not
  import JAX are not heavy jobs.
- Never run the paper's full experiment scripts (`experiments/run_*.sh`: 100 seeds x many configurations,
  CIFAR-10 training). Use the smallest upstream-supported settings (for example `--id_l=0 --id_u=0`, few particles)
  and record exactly what you changed; never change the upstream algorithm or source files.
- Watch memory (`free -m`, `nvidia-smi`). If a job is killed or the GPU runs out of memory, do not just retry
  the same thing: reduce the problem size through parameters the upstream code itself exposes
  (for example number of particles, time steps, number of diffusion steps, number of seeds), record exactly what was
  changed, and never change the upstream algorithm or source files.
- Do not start servers that keep running, do not open ports for the user, do not push anything anywhere,
  do not register MCP servers with any client, and do not touch files outside your project root and the
  ownership stated in your assignment.

## Conventions
- Run commands from the project root with the explicit project interpreter (`PROJECT_PYTHON`), never a bare `python`.
- Reports go exactly where the assignment says. Keep them factual: commands, exit statuses, versions, hashes,
  what passed, what failed, what was not attempted and why. Never invent results, provenance or hashes.
- Leave `reports/agent-runs.json`, `.pipeline/` markers and other agents' files to the coordinator.
- Finish with a short message (5-12 lines): report paths, actual outcome, blockers.

## Incident 2026-10-03 01:47:49Z (21:47:49 EDT)
WSL stopped abruptly (journal ends, no shutdown messages, new boot at 21:54 EDT) right when a verifier started
`verify_mcp_server.py` (stdio server spawned inside a heavy.sh scope, limit 1200 MB). Cause unknown (VM freeze or
external shutdown). Since then: heavy.sh needs MemAvailable >= limit + 2500 MB, limit at most 1500 MB; only ONE agent
that runs heavy jobs is active at a time; check `free -m` before each heavy job and keep test batches small
(one test file per heavy.sh call).
