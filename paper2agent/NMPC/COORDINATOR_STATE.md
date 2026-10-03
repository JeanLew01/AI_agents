# NMPC Paper2Agent conversion: coordinator state

Last updated: 2026-10-02T13:23:13Z (update this file at every phase change)

## Goal
User request (2026-10-02): following the Paper2Agent tutorial (https://github.com/jmiao24/Paper2Agent, skill
installed at ~/.claude/skills/paper2agent, commit 8c2d059), turn seven NMPC papers into agents usable from
~/AI_agents/paper2agent/NMPC. Paper skills for all seven; MCP servers for the two papers with public code.

## Inputs
| id | paper | source | TeX |
| --- | --- | --- | --- |
| dial-mpc-paper | DIAL-MPC (arXiv 2409.15610v1) | user's PDF, reader highlights stripped (original in papers/user-annotated/) | tex-source/dial-mpc |
| model-based-diffusion-paper | MBD, NeurIPS 2024 | user's PDF, highlights stripped | tex-source/model-based-diffusion (arXiv v1) |
| pac-nmpc-paper | PAC-NMPC, RA-L 2023 | arXiv 2210.08092v3 | tex-source/pac-nmpc |
| pac-nmpc-value-function-paper | PAC-NMPC + learned value function, ACC 2025 | arXiv 2309.13171v3 | tex-source/pac-nmpc-value-function |
| post-stall-navigation-paper | Post-stall navigation, ICRA 2022 | arXiv 2201.01186v1 | tex-source/post-stall-navigation |
| rl-guided-pac-nmpc-paper | RL-guided PAC-NMPC, under review | arXiv 2609.39854v1 | tex-source/rl-guided-pac-nmpc |
| urban-swarm-fixed-wing-paper | Agile fixed-wing UAVs for urban swarm ops | Field Robotics 3:725-765 (2023) via Wayback; same article later in IEEE T-FR | none |

Code: LeCAR-Lab/dial-mpc @871c84f, LeCAR-Lab/model-based-diffusion @c1eb913 (both Apache-2.0). No public PAC-NMPC code.

## Layout
- papers/, tex-source/, paper-review/<id>/ (external review dirs), paper-review/_tools/ (REVIEWER_BRIEF.md v2, p2s_tools.py)
- mcp-build/<repo>/ (Paper2MCP project roots; COMMON_BRIEF.md; .heavy.lock serialises JAX jobs)
- staging/ (staging builds), dist/nmpc-agent/{skill,mcp}/ (final delivery)

## Conventions
- Maths as LaTeX text (same as ~/AI_agents/paper2agent/Reachability), so strict verify ends reviewed_with_limitations.
- Reviewers own page ranges, mark finished pages with "[v2]" in review_notes, write DOC/adjudication-notes/page-NNNN.json.
- Coordinator builds, binds adjudication notes to fingerprints, runs a fresh verifier per paper, then final build + verify --strict.
- Background agents die when the host session restarts: check page flags and reports, relaunch with the same prompts.

## Status log
- 2026-10-02T13:23:13Z wave 1 running: reviewers for dial-mpc 1-9, pac-nmpc 1-9, pac-nmpc-value-function 1-9, post-stall 1-7, MBD 1-10; scanners for both repos resumed.
- Pending wave 2: MBD 11-20, MBD 21-30, rl-guided 1-10, rl-guided 11-20, urban-swarm 1-14, 15-28, 29-41; environment managers (dial-mpc-env partly installed).
- 2026-10-02T13:43:49Z done: post-stall 1-7 reviewed (staging s1 built, adjudications bound, strict verify exit 0, fresh verifier running); MBD 1-10 reviewed; both scanners done; dial-mpc env ready (heavy probe pending, needs >= 3 GB free RAM; run via `flock .heavy.lock choom -n 1000 --`).
- 2026-10-02T13:43:49Z running: reviewers dial-mpc 1-9, pac-nmpc 1-9, pac-nmpc-value-function 1-9, rl-guided 1-10 and 11-20, urban-swarm 1-14, MBD 11-20 and 21-30; MBD env manager; post-stall verifier.
- Pending: urban-swarm 15-28 and 29-41 reviewers; verifiers per paper (brief: paper-review/_tools/VERIFIER_BRIEF.md); coordinator helper paper-review/_coord/coord.py (status / meta / bind); final builds into dist/nmpc-agent/skill/.
- 2026-10-02T14:07:57Z WSL was restarted about 13:49Z-14:05Z. Cause: almost certainly the coordinator's MBD probe (ant, Nsample 256) started with 971 MB free and full swap; the VM froze. New rule in mcp-build/COMMON_BRIEF.md: heavy jobs need >= 3500 MB available and a systemd-run memory-limited scope. No reference execution exists yet for either repo; both environments and both scanner reports are complete.
- 2026-10-02T14:07:57Z review state after restart: dial 9/9 (staging s1 strict OK, verifier interrupted), post-stall 7/7 (staging s1 strict OK, verifier interrupted), pac-nmpc 9/9 (report unfinished?), pac-vf 8/9, MBD 19/30, rl-guided 16/20, urban-swarm 13/41 (29-41 not yet assigned). Resuming all interrupted agents via SendMessage.
- 2026-10-02T14:25:23Z all 125 pages reviewed under brief v2. Final skills delivered in dist/nmpc-agent/skill/: dial-mpc-paper, post-stall-navigation-paper (strict verify exit 0, reviewed_with_limitations, independent verifier 0 errors). Staging builds with strict verify exit 0: pac-nmpc-paper-s2, pac-nmpc-value-function-paper-s1, model-based-diffusion-paper-s1, rl-guided-pac-nmpc-paper-s1, urban-swarm-fixed-wing-paper-s1. Verifiers running for those five (reports/verifier-pages-*.md). After each verifier: fix findings (resume the page's reviewer for text fixes; coordinator for meta), then `paper-review/_coord/final.sh PAPER` builds into dist and verifies.
- Metas: paper-review/_coord/meta/PAPER.json (title, notes, navigation, reading_order). final.sh builds at 300 dpi.
- MCP part: environments + scanners done for both repos; no reference execution yet (memory rule). Next: when >= 3500 MB available, run probes in a memory-limited scope, then executors -> implementer -> verifier -> integration -> ZIP.
- 2026-10-02T14:37:59Z ALL SEVEN PAPER SKILLS DELIVERED in dist/nmpc-agent/skill/ (strict verify exit 0, status reviewed_with_limitations, independent verifiers: no error in paper text/maths/tables/references; index and note findings fixed). Symlinked into ~/.claude/skills/ like the Reachability collection. Remaining: Paper2MCP for dial-mpc and model-based-diffusion (blocked on free memory for JAX jobs), README, final report.
- 2026-10-02T14:48:52Z MCP stage 2 started for model-based-diffusion: guarded launcher mcp-build/heavy.sh (mandatory for JAX jobs), coordinator probe OK (car2d 18 s / 0.5 GB; hopper 3m51 / 1.2 GB, reward 1.56), setup marker written, six executors launched (brief: mcp-build/model-based-diffusion/EXECUTOR_BRIEF.md; agent ids in reports/coordinator-events.jsonl). DIAL-MPC: jax 0.6.1 env fails with cuSolver internal error (mixed CUDA 12.8/12.9 wheels suspected); environment manager resumed as attempt 2.
- Next for MBD: merge executed_notebook_*.json into reports/executed_notebooks.json, record runs + exclusion of mbd_run_baseline_planner if path_integral fails, execution gate, then ONE implementer (src/tools/cli_wrapper.py), then ONE fresh verifier, integration (src/model-based-diffusion_mcp.py), clean-env validation, USAGE.md, ZIP, delivery verifier.
- 2026-10-02T15:11:56Z SECOND WSL FREEZE at about 15:05Z (uptime reset; last heavy job: hopper run2, cap 1.5 GB, started at MemAvailable 2211 MB while seven agents were active). Heavy jobs are now DISABLED (mcp-build/HEAVY_JOBS_DISABLED; heavy.sh exits 75; gate tightened to available >= limit + 1500 MB). Do not re-enable without the user's decision (raise WSL memory via C:\Users\jixia\.wslconfig: [wsl2] memory=12GB swap=8GB, then wsl --shutdown; or explicit risk acceptance). When re-enabled: one heavy job at a time, NO other agents active.
- MBD evidence on disk: mbd_planner_car2d (succeeded, bitwise replay), run_mbd_temp_car2d (succeeded, degenerate sweep), run_mbd_seeds_car2d (report written), mbd_planner_car2d_demo (runs done, report being finalised), mbd_planner_hopper (run1 done; replay = coordinator probe in tmp/env-probe/coord/hopper-default-out), path_integral_hopper_mppi (failed: upstream Brax API defect; exclusions written in reports/exclusions/).
- DIAL-MPC: cuSolver failure diagnosed (libcusolver 11.7.4 needs cublasSetEnvironmentMode; installed cuBLAS 12.8.4.1 lacks it; cuBLAS 12.9.0.13 works in a ctypes test). Fix being applied by the environment manager; JAX verification and the feasibility probe still pending.
- README.md written. Remaining MCP stages for both repos: (finish) execution, implementation, verification, integration, clean-env validation, USAGE.md, ZIP, delivery verification, then stage into dist/nmpc-agent/mcp/.
- 2026-10-02T15:17:50Z MBD: all six execution reports final; reports/executed_notebooks.json merged; agent-runs.json has executor runs + two exclusions; execution gate PASSES; .pipeline/reference_execution_done written. Known weak references: seeds and temperature sweeps are degenerate on car2d (dense-reward supplementary runs not attempted); hopper changed-input case not attempted. NEXT (needs JAX, so needs the user's decision first): one implementer for src/tools/cli_wrapper.py (tools: mbd_optimize_trajectory, mbd_evaluate_seeds, mbd_sweep_temperature; algo fixed to mbd; suggestion: run each call from a private per-call copy of the mbd package so results stay isolated), then one fresh verifier, integration, clean-env validation, USAGE.md, ZIP.
- 2026-10-02T15:17:50Z DIAL-MPC: environment attempt 2 recorded as BLOCKED (fix applied: CUDA 12.8.1 wheel set; not verified with JAX; probe not attempted). Setup gate fails on purpose until a verified attempt 3. Commands for later are in reports/environment-manager_results.md section A2.4. FLASK_RUN_FROM_CLI=true makes Flask's app.run return at once (confirmed for Flask alone).
- Waiting for the user's decision on memory before any further JAX job.
