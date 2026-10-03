# path_integral_hopper_mppi: source execution evidence

Status: **failed** (upstream script fails before optimisation; nothing patched). Full report:
`reports/executed_notebook_path_integral_hopper_mppi.json`.

## What was run

Unmodified `mbd/planners/path_integral.py` from the pinned commit c1eb913783f1713f7a1ebb657b34e0188d52cd8b,
from a private copy (`source/`, made with `git archive | tar -x`), working directory `source/mbd/planners`,
`PYTHONPATH=<copy>`, project interpreter (Python 3.11.17, jax 0.4.30, brax 0.10.5, mujoco 3.1.6, tyro 0.8.5),
device cuda:0, always through `mcp-build/heavy.sh`. Driver: `run.sh`.

| Label | Arguments | Exit | Process time | Peak memory | Printed |
| --- | --- | --- | --- | --- | --- |
| `run1` (documented command) | `--env_name hopper --update_method mppi --seed 0` | 1 | 20 s | 446 MB | `override temp_sample to 0.1`, then traceback |
| `variant_ant_mppi` | `--env_name ant --update_method mppi --seed 0` | 1 | 37 s | 467 MB | same |
| `variant_hopper_cem` | `--env_name hopper --update_method cem --seed 0` | 1 | 15 s | 385 MB | same |

The failure in all three runs:

```
File ".../source/mbd/planners/path_integral.py", line 101, in run_path_integral
    mbd.utils.render_us, step_env_jit, env.sys.replace(dt=env.dt)
File ".../site-packages/mujoco/mjx/_src/dataclasses.py", line 61, in replace
    return dataclasses.replace(self, **updates)
TypeError: System.__init__() got an unexpected keyword argument 'dt'
```

The stdout/stderr text of the three runs is byte-identical (SHA-256
df4418caf6958a4134287b3789d7901f3581b27dcfd9136d709221ac095852de without the launcher's peak-memory line), so the
failure does not depend on the environment or on the update method among the cases run. No `rew:` line, no tqdm
progress, no file written by upstream.

## Files

- `run.sh`: driver (`run.sh import-check`, `run.sh <label> <path_integral.py args>`).
- `logs/<label>.log`: complete stdout and stderr of the process plus the launcher's peak-memory line.
- `logs/<label>.launcher.log`: launcher start and end lines. `logs/<label>.meta`: command line, times, exit status,
  files written by upstream.
- `logs/import-check.log`: `import mbd` resolves to `source/mbd/__init__.py`; package versions; `jax.devices()`.
- `source_verification_expected.txt` / `source_verification_actual.txt`: git blob ids of the 34 tracked files at the
  commit and of the files in the copy (identical, checked before and after the runs).
- `outputs/`: empty, upstream wrote nothing.

## Not done

- No reference value and no replay comparison: there is no numerical result.
- `--update_method cma-es`, other environments and other Brax versions were not run. The upstream file was not changed.
