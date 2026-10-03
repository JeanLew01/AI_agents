#!/usr/bin/env bash
# Capture (upstream scripts run unmodified via runpy, one fresh process each) then replay (fresh process).
set -u
ROOT=/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres
P=$ROOT/diffres-env/bin/python
SRC=$ROOT/repo/diffres/experiments/gms
NS=$ROOT/notebooks/gms_baselines_experiment
export PYTHONDONTWRITEBYTECODE=1
run() {
  name=$1; shift
  t0=$(date +%s.%N)
  "$P" "$@" > $NS/logs/$name.log 2>&1
  rc=$?
  t1=$(date +%s.%N)
  echo "RESULT name=${name} exit=${rc} seconds=$(echo "$t1 - $t0" | bc)"
  grep -v '^W0000\|^I0000' $NS/logs/$name.log | tail -6
}
for m in multinomial stratified systematic; do
  run capture_baselines_$m $NS/capture.py $SRC/baselines.py baselines_$m --id_l=0 --id_u=0 --nsamples=1000 --method=$m
done
run capture_ot_eps0.3 $NS/capture.py $SRC/ot.py ot_eps0.3 --id_l=0 --id_u=0 --nsamples=1000 --eps=0.3
run replay $NS/replay.py
