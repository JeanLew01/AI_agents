# mbd_planner_hopper: reference execution evidence

Execution of the upstream command `python mbd_planner.py --env_name hopper --seed 0` (working directory
`mbd/planners`) from model-based-diffusion at commit `c1eb913783f1713f7a1ebb657b34e0188d52cd8b`
(https://github.com/LeCAR-Lab/model-based-diffusion.git). Full machine-readable report:
`../../reports/executed_notebook_mbd_planner_hopper.json`.

## Outcome

| Run | Who | Exit status | Wall time | Peak memory | Final reward (printed) | mu_0ts.npy SHA-256 |
| --- | --- | --- | --- | --- | --- | --- |
| run1 (reference) | this executor, private source copy | 0 | 202 s | 1253 MB | `1.56e+00` | `46f8393a...2cda` |
| coordinator probe (replay of record) | coordinator, pinned checkout | 0 | 231 s | 1203 MB | `1.56e+00` | `46f8393a...2cda` |
| run2 (cut off) | this executor, private source copy | not recorded | not recorded | not recorded | `1.56e+00` | `46f8393a...2cda` |

- Effective parameters: Nsample 2048, Hsample 50, Ndiffuse 100, temperature 0.1 (script defaults; the log prints
  `override temp_sample to 0.1`). Device `cuda:0` (RTX 4070 Laptop GPU), float32, Python 3.11.17, jax 0.4.30,
  brax 0.10.5, mujoco 3.1.6, numpy 1.26.4.
- Native outputs of run1: `outputs/run1/mu_0ts.npy` (shape (99, 50, 3), float32, values in [-0.999, 0.998]) and
  `outputs/run1/rollout.html` (13083 bytes, Brax visualizer page); stdout lines `override temp_sample to 0.1`,
  `init sigma = 6.30e-01`, `final reward = 1.56e+00`.
- Replay: `mu_0ts.npy` is **bitwise identical** (maximum absolute difference 0.0, `numpy.array_equal` true) and
  `rollout.html` is byte-identical between run1 and the coordinator's run; the printed final reward and all 99
  printed per-iteration mean rewards are the same. The files of the cut-off run2 are identical as well.

## What did not go to plan

- **The replay is not this executor's own second run.** run2 was started with identical arguments, and upstream
  printed its last line (`final reward = 1.56e+00`) and wrote both files, but the machine froze (about 15:05Z on
  2026-10-02) before the launcher recorded the exit status. Details: `logs/run2.interruption-note.txt`. On the
  coordinator's instruction the comparison of record uses the coordinator's earlier complete run of the same
  command (`tmp/env-probe/coord/hopper-default.log`, `hopper-default.time`, `hopper-default-out/`), which was only read.
- **The changed-input case** (`--Nsample 512 --Ndiffuse 50 --seed 1`) was **not attempted**: heavy jobs were
  disabled after the freeze. There is no `outputs/changed-input/`.
- The final reward is known only to the three significant digits upstream prints.

## Proposed tolerance for the wrapper test

`mu_0ts.npy`: same shape and dtype, maximum absolute difference <= 1e-6 (observed 0.0). Final reward: printed
string `1.56e+00` (numeric |difference| <= 0.005). `rollout.html`: exists, complete HTML; byte equality was observed.
The observed noise is zero, and a real floating-point divergence in a contact rollout would not stay small, so a
looser threshold has no basis. Valid only for the same machine, GPU, interpreter and packages, same arguments,
fresh process per run; CPU against GPU was not compared.

## Files

| Path | Content |
| --- | --- |
| `run.sh` | Driver: starts the upstream command through `heavy.sh` with `PYTHONPATH=<source>`, records status and times, moves upstream's result files to `outputs/<label>/` |
| `source/` | Private export of the pinned commit (byte-identical; proof in `logs/tracked_blob_hashes.txt` = `logs/copy_blob_hashes.txt`, SHA-256 list in `logs/source_copy_sha256.txt`) |
| `outputs/run1/` | Reference outputs and `SHA256SUMS` |
| `outputs/run2-interrupted/` | Files upstream wrote during the cut-off run2 (secondary evidence) |
| `logs/run1.log`, `run1.launcher.log`, `run1.meta.txt` | Complete stdout/stderr, launcher start/end lines, command line and exit status of run1 |
| `logs/run2.*` | Partial evidence of run2 and the interruption note |
| `logs/import_proof.*` | `import mbd` resolves to `source/mbd/__init__.py` |
| `runtime_probe.py`, `logs/runtime_probe.*` | Interpreter, package versions, JAX device |
| `compare.py`, `comparison.json` | NumPy-only parsing of the logs and comparison of the three runs |

Re-running (only when heavy jobs are allowed again): `./run.sh <new label> --seed 0`; the script refuses to
overwrite an existing label or to start while `source/results/hopper/` exists.
