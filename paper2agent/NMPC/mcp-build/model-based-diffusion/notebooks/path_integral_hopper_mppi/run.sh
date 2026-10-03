#!/usr/bin/env bash
# Driver for execution_id path_integral_hopper_mppi (Paper2MCP, CLI route, stage 2).
#
#   run.sh import-check                  -> proves that `import mbd` resolves to the private source copy
#   run.sh <label> <path_integral args>  -> runs the unmodified upstream script once
#
# Documented command (scanner entry), label "run1":
#   cd <copy>/mbd/planners && $PROJECT_PYTHON path_integral.py --env_name hopper --update_method mppi --seed 0
#
# The script only captures: command line, exit status, complete stdout/stderr, wall time, launcher lines
# (start, end, peak memory) and every file upstream wrote inside the copy. It does not touch the algorithm.
set -u
PROJECT_ROOT=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/model-based-diffusion
PROJECT_PYTHON=$PROJECT_ROOT/model-based-diffusion-env/bin/python
HEAVY=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh
EVID=$PROJECT_ROOT/notebooks/path_integral_hopper_mppi
COPY=$EVID/source
TIMEOUT=${TIMEOUT:-1500}

label=${1:?usage: run.sh import-check | run.sh <label> <path_integral.py args...>}
shift
mkdir -p "$EVID/logs" "$EVID/outputs/$label"
log=$EVID/logs/$label.log                 # complete stdout+stderr of the upstream process (+ peak-memory line)
launcher=$EVID/logs/$label.launcher.log   # heavy.sh's own stderr lines (start, end)
meta=$EVID/logs/$label.meta

if [ "$label" = import-check ]; then
  cd "$COPY/mbd/planners" || exit 2
  cmd=("$HEAVY" --timeout 300 --log "$log" -- env "PYTHONPATH=$COPY" "$PROJECT_PYTHON" -c
       "import mbd, jax, brax, mujoco, tyro, sys; from mujoco import mjx; print('mbd', mbd.__file__); print('python', sys.version.split()[0]); print('jax', jax.__version__, 'brax', brax.__version__, 'mujoco', mujoco.__version__, 'tyro', tyro.__version__); print('devices', jax.devices()); print('default_backend', jax.default_backend())")
else
  cd "$COPY/mbd/planners" || exit 2
  cmd=("$HEAVY" --timeout "$TIMEOUT" --log "$log" -- env "PYTHONPATH=$COPY" "$PROJECT_PYTHON" path_integral.py "$@")
fi

before=$(mktemp); after=$(mktemp)
( cd "$COPY" && find . -type f -not -path '*/__pycache__/*' | sort ) > "$before"
start_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ); t0=$(date +%s.%N)
"${cmd[@]}" 2> "$launcher"
rc=$?
t1=$(date +%s.%N); end_utc=$(date -u +%Y-%m-%dT%H:%M:%SZ)
( cd "$COPY" && find . -type f -not -path '*/__pycache__/*' | sort ) > "$after"
new_files=$(comm -13 "$before" "$after")
rm -f "$before" "$after"

{
  echo "label: $label"
  echo "cwd: $PWD"
  printf 'command:'; printf ' %q' "${cmd[@]}"; echo
  echo "start_utc: $start_utc"
  echo "end_utc: $end_utc"
  echo "wall_seconds_including_lock_wait: $(echo "$t1 - $t0" | bc)"
  echo "exit_status: $rc"
  echo "files_written_by_upstream_in_copy:"
  if [ -z "$new_files" ]; then echo "  (none)"; else
    while read -r f; do
      mkdir -p "$EVID/outputs/$label/$(dirname "$f")"
      cp -p "$COPY/$f" "$EVID/outputs/$label/$f"
      echo "  $(sha256sum "$COPY/$f" | cut -d' ' -f1)  $f"
    done <<< "$new_files"
  fi
} > "$meta"
rmdir "$EVID/outputs/$label" 2>/dev/null
cat "$meta"; echo "--- launcher"; cat "$launcher"
exit $rc
