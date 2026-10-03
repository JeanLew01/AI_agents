#!/usr/bin/env bash
# Native execution of the unmodified upstream scripts (diffres @767effe) at reduced size.
# Changed relative to experiments/run_gms.sh: --id_u=99 -> 0, --nsamples=10000 -> 1000.
# stratified/systematic are accepted by baselines.py but not used in run_gms.sh.
set -u
ROOT=/home/jixia/AI_agents/paper2agent/ParticleFilter/mcp-build/diffres
P=$ROOT/diffres-env/bin/python
SRC=$ROOT/repo/diffres/experiments/gms
NS=$ROOT/notebooks/gms_baselines_experiment
cd $NS/native_run
export PYTHONDONTWRITEBYTECODE=1
run() {
  name=$1; shift
  t0=$(date +%s.%N)
  "$P" "$@" > $NS/logs/native_${name}.log 2>&1
  rc=$?
  t1=$(date +%s.%N)
  echo "RESULT name=${name} exit=${rc} seconds=$(echo "$t1 - $t0" | bc) cmd=$*"
  cat $NS/logs/native_${name}.log | grep -v '^W0000\|^I0000' | tail -5
}
for m in multinomial stratified systematic; do
  run baselines_$m $SRC/baselines.py --id_l=0 --id_u=0 --nsamples=1000 --method=$m
done
run ot_eps0.3 $SRC/ot.py --id_l=0 --id_u=0 --nsamples=1000 --eps=0.3
ls -la gms/results
