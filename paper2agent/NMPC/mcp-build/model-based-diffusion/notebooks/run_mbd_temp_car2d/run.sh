#!/usr/bin/env bash
# Driver for execution_id run_mbd_temp_car2d (Paper2MCP, CLI route, stage 2).
# Usage: run.sh <label>      label = import_check | run1 | run2 | ...
#
# Runs the documented upstream command, unmodified, from the private copy of the pinned source:
#   cwd  = <copy>/mbd/scripts
#   argv = $PROJECT_PYTHON run_mbd.py --env_name car2d --algo mbd --mode temp
# through the guarded launcher heavy.sh (workspace lock, memory-limited scope,
# XLA_PYTHON_CLIENT_PREALLOCATE=false, MPLBACKEND=Agg, PYTHONPATH removed and then set to the copy).
# The exit status of this script is the exit status of the upstream command.
set -u
PROJECT_ROOT=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/model-based-diffusion
PROJECT_PYTHON=$PROJECT_ROOT/model-based-diffusion-env/bin/python
HEAVY=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh
EVID=$PROJECT_ROOT/notebooks/run_mbd_temp_car2d
COPY=$EVID/source
TIMEOUT=1500
label="${1:?usage: run.sh <label>}"

if [ "$label" = "import_check" ]; then
  cd "$COPY/mbd/scripts" || exit 2
  "$HEAVY" --timeout 300 --log "$EVID/logs/import_check.log" -- \
    env PYTHONPATH="$COPY" "$PROJECT_PYTHON" -c \
    "import sys, mbd, mbd.planners.mbd_planner as p, mbd.envs.car2d as c, mbd.utils as u, jax, numpy, brax, tyro, platform; print('mbd', mbd.__file__); print('mbd_planner', p.__file__); print('car2d', c.__file__); print('utils', u.__file__); print('python', sys.version.replace(chr(10), ' ')); print('executable', sys.executable); print('jax', jax.__version__, 'numpy', numpy.__version__, 'brax', brax.__version__, 'tyro', tyro.__version__); print('devices', jax.devices()); print('default_backend', jax.default_backend()); print('x64', jax.config.jax_enable_x64); print('platform', platform.platform())" \
    2> "$EVID/logs/import_check.heavy.stderr"
  rc=$?
  echo "$rc" > "$EVID/logs/import_check.exit"
  exit $rc
fi

out="$EVID/outputs/$label"
mkdir -p "$out"
cd "$COPY/mbd/scripts" || exit 2

# what exists in the copy before the run (to detect any file upstream writes)
( cd "$COPY" && find . -type f -not -path '*/__pycache__/*' | sort ) > "$out/copy_files_before.txt"

{
  echo "cwd: $(pwd)"
  echo "command: $HEAVY --timeout $TIMEOUT --log $out/stdout_stderr.log -- env PYTHONPATH=$COPY $PROJECT_PYTHON run_mbd.py --env_name car2d --algo mbd --mode temp"
} > "$out/command.txt"

t0=$(date +%s.%N)
date -u +%Y-%m-%dT%H:%M:%SZ > "$out/started_utc.txt"
"$HEAVY" --timeout "$TIMEOUT" --log "$out/stdout_stderr.log" -- \
  env PYTHONPATH="$COPY" "$PROJECT_PYTHON" run_mbd.py --env_name car2d --algo mbd --mode temp \
  2> "$out/heavy.stderr"
rc=$?
t1=$(date +%s.%N)
date -u +%Y-%m-%dT%H:%M:%SZ > "$out/ended_utc.txt"
echo "$rc" > "$out/exit_status.txt"
# wall time of the launcher call, including any wait for the workspace lock
awk -v a="$t0" -v b="$t1" 'BEGIN{printf "%.2f\n", b-a}' > "$out/wall_seconds_including_lock_wait.txt"

( cd "$COPY" && find . -type f -not -path '*/__pycache__/*' | sort ) > "$out/copy_files_after.txt"
diff "$out/copy_files_before.txt" "$out/copy_files_after.txt" > "$out/copy_files_diff.txt"
echo "$?" > "$out/copy_files_diff.exit"   # 0 = upstream wrote no file into the copy

# copies of everything upstream wrote (expected: nothing in --mode temp, not_render=True)
if [ -d "$COPY/results" ]; then
  mkdir -p "$out/upstream_results"
  cp -a "$COPY/results/." "$out/upstream_results/"
fi

( cd "$out" && find . -type f -not -name SHA256SUMS | sort | xargs sha256sum ) > "$out/SHA256SUMS"
echo "run.sh: label=$label exit=$rc wall=$(cat "$out/wall_seconds_including_lock_wait.txt")s" >&2
exit $rc
