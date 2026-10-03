# Coordinator feasibility probe (stage 1 reconciliation), model-based-diffusion

Recorded 2026-10-02T14:47:01Z by the coordinator, because the environment manager could not run the probe (memory gate).
All runs used `mcp-build/heavy.sh` (memory-limited scope), the project interpreter, the unmodified checkout at
c1eb913783f1713f7a1ebb657b34e0188d52cd8b, cwd `repo/model-based-diffusion/mbd/planners`, device cuda:0 (RTX 4070 Laptop, 8 GB).

| Command | Exit | Wall time | Scope peak memory | Printed result | Files written by upstream |
| --- | --- | --- | --- | --- | --- |
| `python mbd_planner.py --env_name car2d --seed 0` (defaults: Nsample 2048, Hsample 50, Ndiffuse 100) | 0 | 18 s | 531 MB | final reward = -1.19e-07 | results/car2d/mu_0ts.npy, results/car2d/rollout.png |
| `python mbd_planner.py --env_name hopper --seed 0` (defaults) | 0 | 3 min 51 s (99 steps at about 1.06 s) | 1203 MB | final reward = 1.56e+00 | results/hopper/mu_0ts.npy, results/hopper/rollout.html |

Logs: tmp/env-probe/coord/*.log and *.time; the files upstream wrote into the checkout were moved to
tmp/env-probe/coord/<case>-out/ so that `git status --porcelain --ignored` shows only `__pycache__` directories.
The car2d result without demonstration stays inside the U-shaped obstacle, which is what the paper reports for the
data-free case (its Figure 4(b)); the hopper reward is in the range of the paper's Table 2 (1.53 +/- 0.03).
These probe runs are feasibility evidence only; reference results come from the executors.

Reconciliation of the scanner's selection with feasibility: all six execution assignments are feasible in size on
this machine (car2d and hopper at script defaults). `path_integral_hopper_mppi` is expected to fail at
`env.sys.replace(dt=env.dt)` with the resolved Brax version; its executor decides by running it.
An earlier coordinator probe (ant, Nsample 256) was started without the memory guard at 13:47Z and coincided with a
freeze of the WSL machine; its partial logs are in tmp/env-probe/probe-ant-small-interrupted/ and are not evidence.
