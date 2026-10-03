#!/usr/bin/env bash
# heavy.sh [--limit-mb N] [--timeout SECONDS] [--log FILE] -- command [args...]
#
# The only allowed way to start a JAX job in the ParticleFilter workspace (CPU only: JAX_PLATFORMS=cpu, no GPU).
# Shares its lock with ~/AI_agents/paper2agent/NMPC/mcp-build so heavy jobs of both collections never overlap.
#  * one heavy job at a time (workspace lock)
#  * refuses to start (exit 75) unless MemAvailable >= limit + 2500 MB; default limit = min(1200, MemAvailable - 2500); hard cap 1500 MB; also refuses while ParticleFilter/mcp-build/HEAVY_JOBS_DISABLED exists
#  * runs the command in a systemd scope with MemoryMax=limit and no swap, so the job is what gets killed
#    (exit 137) if it needs more, never the machine; oom_score_adj=1000 as a second safeguard
#  * XLA_PYTHON_CLIENT_PREALLOCATE=false, PYTHONPATH unset (ROS leaks into the login shell), MPLBACKEND=Agg
#  * prints the scope's peak memory and the GPU memory in use before and after
set -u
LOCK=/home/jixia/AI_agents/paper2agent/NMPC/mcp-build/.heavy.lock
limit=""; tmo=1800; log=""
while [ $# -gt 0 ]; do
  case "$1" in
    --limit-mb) limit="$2"; shift 2;;
    --timeout) tmo="$2"; shift 2;;
    --log) log="$2"; shift 2;;
    --) shift; break;;
    *) echo "heavy.sh: unknown option $1" >&2; exit 2;;
  esac
done
[ $# -gt 0 ] || { echo "heavy.sh: no command" >&2; exit 2; }
if [ -e /home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/HEAVY_JOBS_DISABLED ]; then
  echo "heavy.sh: NOT STARTED: heavy jobs are disabled by the coordinator (see ParticleFilter/mcp-build/HEAVY_JOBS_DISABLED). Do not retry; report as not attempted." >&2
  exit 75
fi
exec 9>"$LOCK"; flock 9
avail=$(awk '/^MemAvailable:/{print int($2/1024)}' /proc/meminfo)
if [ -z "$limit" ]; then limit=$(( avail - 2500 )); [ "$limit" -gt 1200 ] && limit=1200; fi
if [ "$limit" -lt 500 ] || [ "$limit" -gt 1500 ] || [ "$avail" -lt $(( limit + 2500 )) ]; then
  echo "heavy.sh: NOT STARTED: MemAvailable=${avail} MB, limit=${limit} MB (need 500 <= limit <= 1500 and available >= limit + 2500)" >&2
  exit 75
fi
gpu0=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits 2>/dev/null | head -1)
echo "heavy.sh: start $(date -u +%Y-%m-%dT%H:%M:%SZ) MemAvailable=${avail}MB MemoryMax=${limit}MB timeout=${tmo}s gpu_used_before=${gpu0}MiB" >&2
inner='"$@"; rc=$?; cg=/sys/fs/cgroup$(cut -d: -f3 /proc/self/cgroup); echo "heavy.sh: scope memory.peak=$(( $(cat $cg/memory.peak 2>/dev/null || echo 0) / 1048576 ))MB oom_kills=$(grep -w oom_kill $cg/memory.events 2>/dev/null | cut -d" " -f2)" >&2; exit $rc'
if [ -n "$log" ]; then
  systemd-run --user --scope -q -p MemoryMax=${limit}M -p MemorySwapMax=0 -- choom -n 1000 -- \
    env -u PYTHONPATH JAX_PLATFORMS=cpu CUDA_VISIBLE_DEVICES= XLA_PYTHON_CLIENT_PREALLOCATE=false MPLBACKEND=Agg timeout --signal=TERM --kill-after=20 "$tmo" bash -c "$inner" heavy "$@" >"$log" 2>&1
else
  systemd-run --user --scope -q -p MemoryMax=${limit}M -p MemorySwapMax=0 -- choom -n 1000 -- \
    env -u PYTHONPATH JAX_PLATFORMS=cpu CUDA_VISIBLE_DEVICES= XLA_PYTHON_CLIENT_PREALLOCATE=false MPLBACKEND=Agg timeout --signal=TERM --kill-after=20 "$tmo" bash -c "$inner" heavy "$@"
fi
rc=$?
gpu1=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits 2>/dev/null | head -1)
echo "heavy.sh: end $(date -u +%Y-%m-%dT%H:%M:%SZ) exit=${rc} gpu_used_after=${gpu1}MiB MemAvailable=$(awk '/^MemAvailable:/{print int($2/1024)}' /proc/meminfo)MB" >&2
exit $rc
