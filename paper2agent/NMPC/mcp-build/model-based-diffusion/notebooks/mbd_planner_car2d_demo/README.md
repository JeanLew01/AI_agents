# mbd_planner_car2d_demo: reference execution

Evidence for the execution assignment `mbd_planner_car2d_demo` (Paper2MCP, CLI route, stage 2).
Full report: `../../reports/executed_notebook_mbd_planner_car2d_demo.json`.

## What was run

The documented command of the upstream README (lines 44-51), with the flag spelled as the dataclass field:

```
cd source/mbd/planners
heavy.sh --timeout 900 --log logs/<label>.log -- env PYTHONPATH=<this folder>/source $PROJECT_PYTHON mbd_planner.py --env_name car2d --seed 0 --enable_demo
```

- Source: `source/`, a `git archive` of commit `c1eb913783f1713f7a1ebb657b34e0188d52cd8b` of
  https://github.com/LeCAR-Lab/model-based-diffusion. All 34 tracked files have the same SHA-256 and git blob id as
  in the commit (`logs/source_copy_verification.txt`, taken after run2; the same check gave 0 mismatches before run1).
- `import mbd` resolves to `source/mbd/__init__.py` (`logs/import-check.log`).
- Runtime: Python 3.11.17, jax 0.4.30 (CUDA 12), brax 0.10.5, numpy 1.26.4, matplotlib 3.9.0, tyro 0.8.5.
  Device `cuda:0` according to the sibling executor's probe with the same interpreter
  (`../mbd_planner_car2d/logs/probe_runtime.log`); my own runs did not print the device.
- Effective parameters (script defaults): Nsample 2048, Hsample 50, Ndiffuse 100, temp_sample 0.1, beta0 1e-4,
  betaT 1e-2, seed 0, enable_demo true.
- Flag spelling used: `--enable_demo`. It was accepted (exit 0, demonstration code path ran).

`run.sh <label>` runs the documented command once; `run.sh <label> -- <arguments>` runs the script with other
arguments. The driver only launches the upstream script and copies the files it wrote from `source/results/car2d/`
to `outputs/<label>/`.

## Demonstration data

`mbd/envs/car2d.py:66` loads `f"{mbd.__path__[0]}/assets/car2d_xref.npy"`, relative to the imported `mbd` package
(here `source/mbd/assets/car2d_xref.npy`, SHA-256 `8b671a26...62bf5187`, same bytes as in the pinned checkout).
The file is read in `Car2d.__init__` for every car2d run; the flag decides whether it enters the sample weights
(`mbd_planner.py:117-125`) and the plot (`mbd_planner.py:166-167`). Content: 50 x 2 float64 positions from the start
(-0.5, 0) to the goal (0.5, 0).

## Result

| | run1 | run2 (replay) |
| --- | --- | --- |
| exit status | 0 | 0 |
| `override temp_sample to` | 0.1 | 0.1 |
| `init sigma =` | 6.30e-01 | 6.30e-01 |
| `final reward =` | 3.43e-01 | 3.43e-01 |
| `mu_0ts.npy` | (99, 50, 2) float32 | (99, 50, 2) float32 |
| SHA-256 `mu_0ts.npy` | cb761b5b...fc82323f | cb761b5b...fc82323f |
| SHA-256 `rollout.png` | d8a5bdf9...8d2a2890 | d8a5bdf9...8d2a2890 |
| job wall time (launcher) | 26 s | 25 s |
| peak memory of the scope | 508 MB | 630 MB |

Replay: `numpy.array_equal` is True, maximum absolute difference 0.0; both files are byte-identical between the runs
(`logs/replay_comparison.txt`). No tolerance was needed on this device.

`rollout.png`: the red car path leaves the U-shaped wall of obstacle circles through its open left side, passes
below the lower arm and ends in a cluster of points at the goal near (0.5, 0), close to the green dashed
"RRT path" reference.

## Difference to the run without the flag

Compared with the sibling executor's reference `../mbd_planner_car2d/outputs/run1/` (same commit, interpreter and
arguments, no flag; read-only):

| | with `--enable_demo` | without |
| --- | --- | --- |
| `final reward =` | 3.43e-01 | -1.19e-07 |
| mean absolute control of the final iterate | 0.568 | 0.036 |
| figure | car reaches the goal, reference drawn | car stays at the start inside the U, no reference |

`mu_0ts.npy` has the same shape but differs in all 99 stored iterates (maximum absolute difference 1.13 overall,
0.97 in the final iterate). The flag is passed through and changes the result.

## Not done

- README spelling `--enable_demos`: **not attempted: heavy jobs disabled after a machine freeze on 2026-10-02 about
  15:05Z.** The driver had been launched for it, but the upstream command never started
  (`logs/readme-spelling.launcher.log` is empty, there is no `logs/readme-spelling.log`). Whether the parser rejects
  this spelling is not established.
- Own no-demo run (`outputs/no-demo-comparison/`): **not attempted**, same reason. The sibling reference was used.

## Files

- `run.sh`: driver.
- `source/`: private source copy (upstream writes `results/` into it; the driver empties `results/car2d` before
  each run, so it is empty now).
- `outputs/run1/`, `outputs/run2/`: `mu_0ts.npy`, `rollout.png` as written by upstream, and `SHA256SUMS`.
- `logs/run{1,2}.log`: complete stdout and stderr (tqdm uses carriage returns; read with `tr '\r' '\n'`), ending with
  the launcher's peak-memory line. `logs/run{1,2}.launcher.log`: launcher start and end lines.
  `logs/run{1,2}.meta.txt`: command, working directory, exit status, times, files written.
- `logs/replay_comparison.txt`: replay and with/without comparison (numpy only).
- `logs/source_copy_verification.txt`, `logs/tracked_files.txt`, `logs/copy_files.txt`: source copy check.

## Notes

- One seed, one environment, defaults only. Printed values have three significant digits.
- `Car2d.eval_xref_logpd` subtracts the 50-row reference from the rollout states, so the demonstration presumably
  requires Hsample = 50 (code reading; other horizons were not run).
