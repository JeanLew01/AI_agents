#!/usr/bin/env bash
# Driver for execution_id run_mbd_seeds_car2d (Paper2MCP, CLI route, stage 2).
#
#   run.sh <label> [env_name] [timeout_seconds]
#
# Runs the documented upstream command, unchanged, from the private source copy:
#   cd <copy>/mbd/scripts
#   $PROJECT_PYTHON run_mbd.py --env_name <env_name> --algo mbd --mode seed
# through the mandatory guarded launcher heavy.sh, with PYTHONPATH=<copy> so that `import mbd`
# resolves to the copy and not to the editable install of the pinned checkout.
# It only captures evidence (command line, exit status, log, wall time, files written by upstream).
# It does not touch the algorithm and it does not hide a failure: its exit status is the command's.
set -u

PROJECT_ROOT=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/model-based-diffusion
PROJECT_PYTHON=$PROJECT_ROOT/model-based-diffusion-env/bin/python
HEAVY=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh
EVID=$PROJECT_ROOT/notebooks/run_mbd_seeds_car2d
COPY=$EVID/source

label=${1:?usage: run.sh <label> [env_name] [timeout_seconds]}
env_name=${2:-car2d}
tmo=${3:-1200}

out=$EVID/outputs/$label
mkdir -p "$out"
log=$out/stdout_stderr.log
launcher=$out/launcher_stderr.txt
meta=$out/run_meta.txt

cd "$COPY/mbd/scripts" || exit 2

# state of the copy before the run (everything except byte-code caches)
find "$COPY" -type f -not -path '*/__pycache__/*' | sort > "$out/files_before.txt"

cmd=("$HEAVY" --timeout "$tmo" --log "$log" -- env "PYTHONPATH=$COPY" "$PROJECT_PYTHON" run_mbd.py --env_name "$env_name" --algo mbd --mode seed)

{
  echo "label: $label"
  echo "cwd: $(pwd)"
  printf 'command:'; printf ' %q' "${cmd[@]}"; echo
  echo "invoked_utc: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
} > "$meta"

t0=$(date +%s.%N)
"${cmd[@]}" 2> "$launcher"
rc=$?
t1=$(date +%s.%N)

find "$COPY" -type f -not -path '*/__pycache__/*' | sort > "$out/files_after.txt"
comm -13 "$out/files_before.txt" "$out/files_after.txt" > "$out/files_written_by_upstream.txt"

{
  echo "finished_utc: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo "exit_status: $rc"
  echo "wall_seconds_including_lock_wait: $(awk -v a="$t0" -v b="$t1" 'BEGIN{printf "%.1f", b-a}')"
  echo "new_files_in_copy: $(wc -l < "$out/files_written_by_upstream.txt")"
  echo "results_dir_exists: $([ -d "$COPY/results" ] && echo yes || echo no)"
  echo "log_sha256: $(sha256sum "$log" 2>/dev/null | cut -d' ' -f1)"
} >> "$meta"

cat "$launcher" >&2
cat "$meta"
exit $rc
