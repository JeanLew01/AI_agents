#!/usr/bin/env bash
# Driver for execution_id = mbd_planner_hopper (CLI source executor, stage 2).
#
#   run.sh <label> [extra mbd_planner.py arguments...]
#
# Runs the documented upstream command
#   (cwd = <copy>/mbd/planners)  $PROJECT_PYTHON mbd_planner.py --env_name hopper <extra arguments>
# through the guarded launcher heavy.sh with PYTHONPATH=<copy>, where <copy> is the private, byte-identical
# export of the pinned commit. It does not touch the algorithm: it only starts the upstream script, records the
# exit status / times / logs, and moves the files upstream wrote (<copy>/results/hopper/) to outputs/<label>/.
#
# Labels used:  run1 (reference)      --seed 0     completed, exit status 0
#               run2 (replay)         --seed 0     cut off by a machine freeze after upstream's last line; this
#                                                  script never reached its bookkeeping (see logs/run2.interruption-note.txt)
# Planned but NOT RUN (heavy jobs were disabled after the freeze):
#               changed-input         --Nsample 512 --Ndiffuse 50 --seed 1
# (Only this comment block was edited after the runs; the commands below are the ones that were executed.)
set -u
PROJECT_ROOT=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/model-based-diffusion
PROJECT_PYTHON=$PROJECT_ROOT/model-based-diffusion-env/bin/python
HEAVY=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh
EVID=$PROJECT_ROOT/notebooks/mbd_planner_hopper
COPY=$EVID/source
TIMEOUT=${TIMEOUT:-1500}

label=${1:?usage: run.sh <label> [extra args]}; shift
out=$EVID/outputs/$label
log=$EVID/logs/$label.log                 # complete stdout+stderr of the upstream command (+ scope peak memory line)
launcher=$EVID/logs/$label.launcher.log   # heavy.sh's own stderr lines (start, end, exit, GPU memory)
meta=$EVID/logs/$label.meta.txt

if [ -e "$out" ]; then echo "run.sh: $out already exists, refusing to overwrite" >&2; exit 3; fi
if [ -e "$COPY/results/hopper" ]; then echo "run.sh: stale $COPY/results/hopper present, refusing" >&2; exit 3; fi

cd "$COPY/mbd/planners" || exit 4
{
  echo "label=$label"
  echo "cwd=$(pwd)"
  echo "command=$HEAVY --timeout $TIMEOUT --log $log -- env PYTHONPATH=$COPY $PROJECT_PYTHON mbd_planner.py --env_name hopper $*"
  echo "invoked_utc=$(date -u +%Y-%m-%dT%H:%M:%S.%NZ)"
} > "$meta"
t0=$(date +%s.%N)
"$HEAVY" --timeout "$TIMEOUT" --log "$log" -- env PYTHONPATH="$COPY" "$PROJECT_PYTHON" mbd_planner.py --env_name hopper "$@" 2> "$launcher"
rc=$?
t1=$(date +%s.%N)
{
  echo "returned_utc=$(date -u +%Y-%m-%dT%H:%M:%S.%NZ)"
  echo "exit_status=$rc"
  echo "elapsed_including_lock_wait_s=$(echo "$t1 - $t0" | bc)"
} >> "$meta"
cat "$launcher" >&2

mkdir -p "$out"
if [ -d "$COPY/results/hopper" ]; then
  mv "$COPY/results/hopper"/* "$out"/ && rmdir "$COPY/results/hopper"
  (cd "$out" && sha256sum * > SHA256SUMS && ls -l --time-style=full-iso >> "$meta")
else
  echo "upstream_wrote_no_results_directory=true" >> "$meta"
fi
echo "run.sh: label=$label exit_status=$rc" >&2
exit $rc
