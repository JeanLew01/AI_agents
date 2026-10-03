#!/usr/bin/env bash
# Driver for execution_id mbd_planner_car2d (CLI source executor, Paper2MCP stage 2).
# It only launches the unmodified upstream script and collects what upstream wrote; it contains no algorithm.
#
#   run.sh probe        import proof (mbd resolves to the private copy) + runtime identity (versions, device)
#   run.sh run <label>  one execution of the documented command; evidence goes to outputs/<label>/ and logs/<label>.*
#
# Documented command (README lines 33-40, scanner entry mbd_planner_car2d):
#   cwd  <source copy>/mbd/planners
#   argv $PROJECT_PYTHON mbd_planner.py --env_name car2d --seed 0
set -u
PROJECT_ROOT=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/model-based-diffusion
PROJECT_PYTHON=$PROJECT_ROOT/model-based-diffusion-env/bin/python
HEAVY=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/heavy.sh
NS=$PROJECT_ROOT/notebooks/mbd_planner_car2d
COPY=$NS/source                      # git archive of commit c1eb913783f1713f7a1ebb657b34e0188d52cd8b
CWD=$COPY/mbd/planners
RESULTS=$COPY/results/car2d          # where upstream writes (mbd_planner.py:153)
mkdir -p "$NS/logs" "$NS/outputs"

case "${1:-}" in
probe)
  cd "$CWD" || exit 2
  "$HEAVY" --timeout 300 --log "$NS/logs/probe_import.log" -- \
    env PYTHONPATH="$COPY" "$PROJECT_PYTHON" -c "import mbd; print(mbd.__file__)" 2> "$NS/logs/probe_import.launcher.txt"
  rc1=$?
  echo "probe_import exit=$rc1" | tee "$NS/logs/probe_import.exit"
  "$HEAVY" --timeout 300 --log "$NS/logs/probe_runtime.log" -- \
    env PYTHONPATH="$COPY" "$PROJECT_PYTHON" -c "
import sys, platform, importlib.metadata as m
import jax, numpy, matplotlib
print('python', sys.version.replace(chr(10), ' '))
print('executable', sys.executable)
print('platform', platform.platform())
for p in ['jax', 'jaxlib', 'jax-cuda12-plugin', 'jax-cuda12-pjrt', 'brax', 'mujoco', 'mujoco-mjx', 'numpy', 'matplotlib', 'tyro', 'tqdm', 'scipy']:
    try:
        print('pkg', p, m.version(p))
    except Exception as e:
        print('pkg', p, 'NOT FOUND', type(e).__name__)
print('jax.devices', jax.devices())
print('jax.default_backend', jax.default_backend())
x = jax.numpy.zeros(3)
print('array_device', list(x.devices()) if hasattr(x, 'devices') else x.device())
print('jax_enable_x64', jax.config.jax_enable_x64)
print('matplotlib_backend', matplotlib.get_backend())
" 2> "$NS/logs/probe_runtime.launcher.txt"
  rc2=$?
  echo "probe_runtime exit=$rc2" | tee "$NS/logs/probe_runtime.exit"
  [ $rc1 -eq 0 ] && [ $rc2 -eq 0 ]
  exit $?
  ;;
run)
  label=${2:?label}
  out=$NS/outputs/$label
  if [ -e "$out" ]; then echo "run.sh: $out already exists, refusing to overwrite" >&2; exit 2; fi
  if [ -e "$COPY/results" ]; then echo "run.sh: $COPY/results exists before the run, refusing (stale upstream output)" >&2; exit 2; fi
  mkdir -p "$out"
  cd "$CWD" || exit 2
  printf '%s\n' "cwd: $CWD" \
    "command: $HEAVY --timeout 900 --log $NS/logs/$label.log -- env PYTHONPATH=$COPY $PROJECT_PYTHON mbd_planner.py --env_name car2d --seed 0" \
    > "$NS/logs/$label.command.txt"
  t0=$(date +%s.%N); echo "start_utc $(date -u +%Y-%m-%dT%H:%M:%SZ)" > "$NS/logs/$label.time"
  "$HEAVY" --timeout 900 --log "$NS/logs/$label.log" -- \
    env PYTHONPATH="$COPY" "$PROJECT_PYTHON" mbd_planner.py --env_name car2d --seed 0 \
    2> "$NS/logs/$label.launcher.txt"
  rc=$?
  t1=$(date +%s.%N)
  {
    echo "end_utc $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    echo "wall_seconds_including_lock_wait $(awk -v a="$t0" -v b="$t1" 'BEGIN{printf "%.2f", b-a}')"
  } >> "$NS/logs/$label.time"
  echo "$rc" > "$NS/logs/$label.exit"
  cat "$NS/logs/$label.launcher.txt" >&2
  echo "run.sh: $label exit=$rc"
  # collect whatever upstream wrote (moved, so that the next run starts without stale files)
  if [ -d "$COPY/results" ]; then
    (cd "$COPY" && find results -type f | LC_ALL=C sort) > "$NS/logs/$label.files_written.txt"
    if [ -d "$RESULTS" ]; then mv "$RESULTS"/* "$out"/ 2>/dev/null; fi
    rm -rf "$COPY/results"
  else
    : > "$NS/logs/$label.files_written.txt"
  fi
  # hashes are written next to the logs so that the list never contains itself
  # (the first version wrote outputs/<label>/SHA256SUMS and hashed its own empty file; fixed after run1,
  #  before run2; the launch command was not changed)
  (cd "$out" && sha256sum * 2>/dev/null) > "$NS/logs/$label.sha256" || true
  cat "$NS/logs/$label.sha256"
  exit $rc
  ;;
*)
  echo "usage: run.sh probe | run <label>" >&2; exit 2;;
esac
