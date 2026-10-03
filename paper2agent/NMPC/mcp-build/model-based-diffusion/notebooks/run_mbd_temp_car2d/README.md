# run_mbd_temp_car2d: reference execution

Upstream command, run unmodified from a private copy of the pinned source
(LeCAR-Lab/model-based-diffusion, commit c1eb913783f1713f7a1ebb657b34e0188d52cd8b):

```
cd source/mbd/scripts
heavy.sh --timeout 1500 --log <log> -- env PYTHONPATH=<this dir>/source $PROJECT_PYTHON run_mbd.py --env_name car2d --algo mbd --mode temp
```

Device cuda:0 (RTX 4070 Laptop), Python 3.11.17, jax 0.4.30, brax 0.10.5, numpy 1.26.4, float32.

## Result (2026-10-02)

| | exit | command time | peak memory | rews (8 values) | best_temp |
| --- | --- | --- | --- | --- | --- |
| run 1 | 0 | 50 s | 473 MB | all -1.1920929e-07 | 0.01 |
| run 2 (replay) | 0 | 37 s | 504 MB | all -1.1920929e-07 | 0.01 |

Replay: the eight parsed rewards are bitwise equal (`numpy.array_equal` true, maximum absolute difference 0) and
`best_temp` is identical. Upstream wrote no file (the file list of the copy is unchanged by each run).

## The sweep is degenerate on car2d

All eight rewards are the same number, and that number is the lowest reward the environment returns: the car2d
reward is zero unless the car is within 0.2 of the goal, and the planner without demonstration does not get there
for any temperature. `best_temp: 0.01` is only the first grid value, because `numpy.argmax` returns index 0 on a
tie. `diagnostics/reward_floor_check.py` confirms the floor value with upstream functions only: the reward at the
start state, far from the goal, and the mean reward of a car that never moves are all -1.1920929e-07; at the goal
it is 1.0. A test built on these values checks exit status, count, format and the tie rule, not a dependence on
the temperature.

## Supplementary dense-reward run (ant): not attempted

After the degenerate result the coordinator kept car2d as the fast reference and asked for one supplementary run
of the same command on ant (`run_mbd.py --env_name ant --algo mbd --mode temp`, single run, no replay).
**Not attempted: heavy jobs disabled after a machine freeze on 2026-10-02 about 15:05Z.** No value exists.

The driver invoked the launcher at 15:03:15Z; the launcher never printed its `start` line (`heavy.stderr` is
empty, no `stdout_stderr.log`), so the upstream command was never started and there is no partial log. The
halfcheetah fallback was not tried. Details: `outputs/ant-supplementary/STATUS.txt`.

Consequence: there is no reference that shows a dependence of the result on the temperature or on the
environment. The car2d evidence (both runs, the source copy, the driver) was re-verified against its recorded
SHA-256 hashes after the freeze and is intact.

## Files

- `run.sh`: driver (`run.sh import_check | run1 | run2`); its exit status is the upstream exit status.
- `source/`: private copy from `git archive` (34 files, each SHA-256 equal to the blob of the pinned commit, see
  `logs/source_copy_sha256.txt`). The runs added only `__pycache__` directories.
- `logs/import_check.log`: proof that `import mbd` and the planner resolve to `source/`, versions, device.
  This matters because the environment has an editable install of `mbd` that points at the pinned checkout.
- `outputs/run1/`, `outputs/run2/`: command line, exit status, complete stdout/stderr log, launcher lines
  (`heavy.stderr`), times, file lists before and after, `SHA256SUMS`.
- `compare_runs.py`, `replay_comparison.json`: parsing of the two logs and the comparison.
- `diagnostics/`: reward-floor check on car2d (not a reference run).
- `outputs/ant-supplementary/`: remnants of the launch that never started (`STATUS.txt`, command line, start time,
  empty launcher log). No result.
- Report: `../../reports/executed_notebook_run_mbd_temp_car2d.json`.
