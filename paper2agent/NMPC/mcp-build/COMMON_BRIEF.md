# Common brief for all Paper2MCP agents in this workspace

You work inside a Paper2Agent `paper2mcp` conversion coordinated by another agent. The skill lives at
`SKILL_ROOT=/home/jixia/.claude/skills/paper2agent/paper2mcp`. Your assignment names the role file(s) under
`$SKILL_ROOT/references/` that you must read first and follow; those files are authoritative for your role.

## Machine limits (shared laptop, other sessions are running on it)
- WSL2 Ubuntu 24.04, 16 CPU threads, **about 7.5 GB RAM in total with little free**, 2 GB swap,
  one NVIDIA RTX 4070 Laptop GPU with **8 GB** memory (driver 581.04). No sudo. No conda.
- `uv` is at `/home/jixia/.local/bin/uv` (use it for environments and installs; it can download Python versions).
- Any command that imports JAX/Brax/MuJoCo and compiles or runs a simulation is a "heavy job".
  Run heavy jobs **one at a time across the whole workspace** by prefixing them with
  `flock /home/jixia/AI_agents/paper2agent/NMPC/mcp-build/.heavy.lock`
  and always export `XLA_PYTHON_CLIENT_PREALLOCATE=false` for them. Give long jobs a timeout.
- **Memory rule (mandatory).** On 2026-10-02 a small JAX probe started with under 1 GB of free memory froze the
  whole WSL machine and killed every running session. Since then **every** command that imports JAX/Brax/MuJoCo
  (even a one-line import check) must be started through the guarded launcher and nothing else:
  `/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh [--limit-mb N] [--timeout SECONDS] [--log FILE] -- <command> [args...]`
  It takes the workspace lock (one heavy job at a time, others wait), refuses to start with exit status 75 when
  free memory is too low, runs the command in a memory-limited systemd scope without swap (the job is killed with
  status 137 if it needs more; the machine survives), sets `XLA_PYTHON_CLIENT_PREALLOCATE=false` and
  `MPLBACKEND=Agg`, removes `PYTHONPATH` (ROS 2 leaks into the login shell; if your command needs `PYTHONPATH`, set
  it inside the command with `env PYTHONPATH=... python ...`), and prints the scope's peak memory. Do not bypass it,
  do not call `flock`/`systemd-run` yourself, and do not loop on exit status 75: try at most three times a few
  minutes apart, then report "not attempted". Measured on this machine: MBD car2d with script defaults needs about
  0.6 GB and 20 s; MBD hopper with defaults about 1.2 GB and 4 minutes.
- Watch memory (`free -m`, `nvidia-smi`). If a job is killed or the GPU runs out of memory, do not just retry
  the same thing: reduce the problem size through parameters the upstream code itself exposes
  (for example sample count, horizon, number of steps, number of diffusion steps), record exactly what was
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
