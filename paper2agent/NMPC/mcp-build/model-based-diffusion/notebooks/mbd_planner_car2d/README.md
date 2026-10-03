# mbd_planner_car2d: reference execution

Evidence for the execution assignment `mbd_planner_car2d` (Paper2MCP, CLI route, stage 2).
Full report: `../../reports/executed_notebook_mbd_planner_car2d.json`.

## What was run

The documented command of the upstream README (lines 33-40), unchanged:

```
cd source/mbd/planners
heavy.sh --timeout 900 --log logs/<label>.log -- env PYTHONPATH=<this folder>/source $PROJECT_PYTHON mbd_planner.py --env_name car2d --seed 0
```

- Source: `source/`, a `git archive` of commit `c1eb913783f1713f7a1ebb657b34e0188d52cd8b` of
  https://github.com/LeCAR-Lab/model-based-diffusion. All 34 tracked files have the same git blob id as in the
  commit, before the first run and after the second (`logs/source_copy_verification.txt`).
- `import mbd` resolves to `source/mbd/__init__.py` (`logs/probe_import.log`).
- Runtime: Python 3.11.17, jax 0.4.30 (CUDA 12), brax 0.10.5, numpy 1.26.4, matplotlib 3.9.0; device `cuda:0`
  (`logs/probe_runtime.log`).
- Effective parameters (script defaults): Nsample 2048, Hsample 50, Ndiffuse 100, temp_sample 0.1, beta0 1e-4,
  betaT 1e-2, seed 0, no demonstration.

`run.sh probe` reproduces the two probes, `run.sh run <label>` one execution. The driver only launches the upstream
script and moves the files it wrote from `source/results/car2d/` to `outputs/<label>/`.

## Result

| | run1 | run2 (replay) |
| --- | --- | --- |
| exit status | 0 | 0 |
| `override temp_sample to` | 0.1 | 0.1 |
| `init sigma =` | 6.30e-01 | 6.30e-01 |
| `final reward =` | -1.19e-07 | -1.19e-07 |
| `mu_0ts.npy` | (99, 50, 2) float32 | (99, 50, 2) float32 |
| SHA-256 `mu_0ts.npy` | f8777df1...edf0f75bc | f8777df1...edf0f75bc |
| SHA-256 `rollout.png` | 043b2f8a...512f2e93c | 043b2f8a...512f2e93c |
| job wall time (launcher) | 31 s | 17 s |
| peak memory of the scope | 600 MB | 500 MB |

Replay: `numpy.array_equal` is True, maximum absolute difference 0.0; both files are byte-identical between the runs
(`logs/replay_comparison.txt`). No tolerance was needed on this device.

The plan earns zero reward. The progress bar shows `rew=0.00e+00` at every refresh, and `rollout.png` shows the car
path as a small cluster of points at the start position (about x = -0.5, y = 0) inside the U-shaped obstacle; the
car neither leaves the U nor approaches the goal at (0.5, 0). The printed -1.19e-07 is zero up to float32 rounding
(reading of the reward formula in `mbd/envs/car2d.py:89-93`, not a separate measurement).

## Files

- `run.sh`: driver.
- `source/`: private source copy (upstream writes `results/` into it; the driver empties that after each run).
- `outputs/run1/`, `outputs/run2/`: `mu_0ts.npy`, `rollout.png` as written by upstream.
- `logs/run{1,2}.log`: complete stdout and stderr (tqdm uses carriage returns; read with `tr '\r' '\n'`), ending with
  the launcher's peak-memory line. `logs/run{1,2}.launcher.txt`: launcher start and end lines.
  `logs/run{1,2}.{exit,time,command.txt,files_written.txt,sha256}`: exit status, times, command, file list, hashes.
- `logs/input_hashes.sha256`: hashes of the script, the environment and the bundled asset.

## Notes

- After run1 the driver's hash list was moved from `outputs/<label>/SHA256SUMS` to `logs/<label>.sha256` (the first
  version had hashed its own empty file). The launch command did not change.
- One seed, one environment, defaults only. The final reward is available only with three significant digits.
