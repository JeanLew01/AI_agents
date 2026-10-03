#!/usr/bin/env bash
# Driver for execution_id = mbd_planner_car2d_demo (CLI route, native command).
#
# usage: run.sh LABEL [-- extra upstream arguments replacing the default flag set]
#
#   run.sh run1                      documented command, first run
#   run.sh run2                      documented command, replay (identical arguments)
#   run.sh no-demo-comparison -- --env_name car2d --seed 0
#   run.sh readme-spelling    -- --env_name car2d --seed 0 --enable_demos
#   run.sh import-check       (prints mbd.__file__; no planner run)
#
# The upstream script is executed unmodified from a private copy of the pinned commit
# (notebooks/mbd_planner_car2d_demo/source). Nothing is written to repo/model-based-diffusion.
set -u
PROJECT_ROOT=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/model-based-diffusion
PROJECT_PYTHON=$PROJECT_ROOT/model-based-diffusion-env/bin/python
HEAVY=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh
NS=$PROJECT_ROOT/notebooks/mbd_planner_car2d_demo
COPY=$NS/source
CWD=$COPY/mbd/planners
RESULTS=$COPY/results/car2d          # where upstream writes: f"{mbd.__path__[0]}/../results/{env_name}"

label=${1:?label required}; shift
if [ "${1:-}" = "--" ]; then shift; args=("$@"); else args=(--env_name car2d --seed 0 --enable_demo); fi

mkdir -p "$NS/logs" "$NS/outputs"
log=$NS/logs/$label.log                 # complete stdout+stderr of the command (written by heavy.sh --log)
launcher=$NS/logs/$label.launcher.log   # heavy.sh's own stderr lines (start, end)
meta=$NS/logs/$label.meta.txt

if [ "$label" = "import-check" ]; then
  cd "$CWD" || exit 2
  "$HEAVY" --timeout 300 --log "$log" -- env PYTHONPATH="$COPY" "$PROJECT_PYTHON" -c \
    "import mbd, sys; print(mbd.__file__); print(mbd.__path__[0]); print(sys.version)" 2>"$launcher"
  rc=$?
  { echo "label=$label"; echo "cwd=$CWD"; echo "exit_status=$rc"; } >"$meta"
  cat "$launcher" "$log"; exit $rc
fi

out=$NS/outputs/$label
# results directory inside the private copy is emptied first, so every file found afterwards was written by this run
rm -rf "$RESULTS"; rm -rf "$out"; mkdir -p "$out"

cd "$CWD" || exit 2
t0=$(date +%s.%N)
"$HEAVY" --timeout 900 --log "$log" -- env PYTHONPATH="$COPY" "$PROJECT_PYTHON" mbd_planner.py "${args[@]}" 2>"$launcher"
rc=$?
t1=$(date +%s.%N)

{
  echo "label=$label"
  echo "cwd=$CWD"
  printf 'command=%s' "$HEAVY --timeout 900 --log $log -- env PYTHONPATH=$COPY $PROJECT_PYTHON mbd_planner.py"
  printf ' %s' "${args[@]}"; echo
  echo "exit_status=$rc"
  echo "outer_wall_seconds_including_lock_wait=$(echo "$t1 - $t0" | bc)"
  echo "launcher_start=$(grep -o 'start [0-9T:Z-]*' "$launcher" | cut -d' ' -f2)"
  echo "launcher_end=$(grep -o 'end [0-9T:Z-]*' "$launcher" | cut -d' ' -f2)"
} >"$meta"

if [ -d "$RESULTS" ]; then
  cp -p "$RESULTS"/* "$out"/ 2>/dev/null
  (cd "$out" && sha256sum * >SHA256SUMS 2>/dev/null)
  echo "files_written_by_upstream=$(ls "$RESULTS" | tr '\n' ' ')" >>"$meta"
else
  echo "files_written_by_upstream=NONE (results directory was not created)" >>"$meta"
fi
cat "$meta"; cat "$launcher"
exit $rc
