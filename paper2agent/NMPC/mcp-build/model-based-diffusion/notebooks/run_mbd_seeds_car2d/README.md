# run_mbd_seeds_car2d: reference execution of the multi-seed evaluation

Execution evidence for the Paper2MCP conversion of model-based-diffusion (CLI route, stage 2).
Report: `reports/executed_notebook_run_mbd_seeds_car2d.json`. Status: **succeeded** (two identical runs).

## What was run

Upstream command, unchanged, from the private source copy (`source/`, commit
`c1eb913783f1713f7a1ebb657b34e0188d52cd8b` of https://github.com/LeCAR-Lab/model-based-diffusion):

```
cd source/mbd/scripts
heavy.sh --timeout 1200 --log outputs/<run>/stdout_stderr.log -- \
  env PYTHONPATH=<absolute path of source/> $PROJECT_PYTHON run_mbd.py --env_name car2d --algo mbd --mode seed
```

The exact command lines are in `outputs/run1/run_meta.txt` and `outputs/run2/run_meta.txt`; the driver is `run.sh`
(`run.sh <label> [env_name] [timeout_seconds]`). Device: `cuda:0` (RTX 4070 Laptop GPU), Python 3.11.17, jax 0.4.30,
brax 0.10.5 (all versions in `logs/runtime_probe.log`).

The script runs the planner eight times in one process (seeds 0 to 7, planner defaults: Nsample 2048, Hsample 50,
Ndiffuse 100, temp_sample 0.1, no rendering) and prints the mean and standard deviation of the final reward and of the
wall time. It writes no file.

## Which code ran

`run_mbd.py` does `import mbd` and calls `mbd.planners.mbd_planner.run_diffusion`; it does not change `sys.path`.
The project environment contains an editable install of `mbd` that points at the pinned checkout, so the copy is put
first with `PYTHONPATH`. Proof: `logs/import_proof.log` and `logs/runtime_probe.log` show `mbd/__init__.py`,
`mbd/planners/mbd_planner.py` and `mbd/envs/car2d.py` resolving inside `source/`.

The copy was made with `git archive <commit> | tar -x`. All 34 files were compared with the commit by git blob id
(`logs/source_commit_blobs.txt` and `logs/source_copy_blobs.txt` are identical). The runs added nothing to the copy
except `__pycache__` directories.

## Results

| Run | Exit | Launcher window (UTC) | Peak memory | `rew:` line | `time:` line (not compared) |
| --- | --- | --- | --- | --- | --- |
| run1 | 0 | 14:54:01 to 14:54:35 | 466 MB | `rew: -0.00 \pm 0.00` | `time: 3.58 \pm 1.35` |
| run2 | 0 | 14:58:58 to 14:59:39 | 449 MB | `rew: -0.00 \pm 0.00` | `time: 4.39 \pm 2.70` |

Reference values: reward mean `-0.00`, reward standard deviation `0.00` (text as printed; as numbers -0.0 and 0.0).

Replay comparison (`outputs/replay_comparison_run1_vs_run2.json`): the parsed mean and standard deviation are exactly
equal in the two runs, as text and as numbers. There is no array output to compare. After removing the intermediate
progress updates and the wall-clock fields, the two logs are identical line by line (27 lines each).

Per-seed information printed by the script: none about the final reward. Per seed it prints
`override temp_sample to 0.1`, `init sigma = 6.30e-01` and one progress bar of 99 steps whose `rew=` field is the mean
reward of the 2048 sampled trajectories at the current diffusion step (not the final reward). That field reads
`0.00e+00` for every seed, at every captured update, in both runs (849 and 853 updates).

## The car2d summary is degenerate

All rewards are zero at the printed precision. The summary bounds each of the eight final rewards to within about
0.02 of zero; the exact per-seed values are not printed, so the log does not show that they are exactly equal. The
car2d reward is non-zero only within 0.2 of the goal, and without the demonstration no sampled trajectory got there.
This reference therefore checks the exit status, the eight-run structure and the output format, but it cannot detect a
change in the planner's numerical behaviour and it does not distinguish seeds.

A supplementary run of the same command with `--env_name hopper` (eight seeds, about 35 minutes) was launched at
15:00:01Z. It was still waiting for the workspace lock when the machine froze at about 15:05Z, and heavy jobs were
then disabled workspace-wide. It never started (`outputs/hopper_run1/launcher_stderr.txt` is empty, there is no log),
it was not retried, and **no hopper value exists**. To produce it later, when heavy jobs are allowed again:
`./run.sh hopper_run1 hopper 3000`, then `parse_logs.py hopper_run1` and `build_report.py --hopper-state done`.

## Files

- `run.sh`: driver (command, exit status, log, wall time, files written by upstream).
- `parse_logs.py`, `compare_runs.py`, `build_report.py`: standard-library helpers that read the logs and assemble the
  report; they do not import JAX and do not compute anything scientific.
- `runtime_probe.py`, `logs/`: import proof, versions, device, source identity lists.
- `outputs/run1/`, `outputs/run2/`: `stdout_stderr.log` (complete output, including the launcher's peak-memory line),
  `launcher_stderr.txt` (start and end lines), `run_meta.txt`, `parsed.json`, file lists before and after.
- `outputs/hopper_run1/`: what is left of the run that never started (command line and invocation time only).
- `source/`: private copy of the pinned commit.

Helper checks used for the statements above:

```
tr '\r' '\n' < outputs/run1/stdout_stderr.log | grep -a -o 'rew=[^]]*' | sort | uniq -c
grep -a -E '^(rew|time):' outputs/run*/stdout_stderr.log
```
