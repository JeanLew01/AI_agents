# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| I. INTRODUCTION | Motivation, overview of dual-loop annealing, contributions |
| II. RELATED WORK | Parent of A. Agility in Legged Locomotion, B. Sampling-Based Optimization, C. Parallel Robot Simulation |
| A. Agility in Legged Locomotion | Under II. RELATED WORK: NMPC with reduced-order models, model-free and goal-conditioned RL |
| B. Sampling-Based Optimization | Under II. RELATED WORK: zeroth-order optimisation, MPPI and variants |
| C. Parallel Robot Simulation | Under II. RELATED WORK: Isaac Gym, Brax, MuJoCo |
| III. METHOD | Section overview; parent of the three method subsections |
| A. Sampling-Based MPC as Single-stage Diffusion | Under III. METHOD: optimal control problem, MPPI update (1), Proposition 1 and proof (2), (3a)-(3f) |
| B. Diffusion-Inspired Annealing | Under III. METHOD: coverage versus convergence trade-off, annealing in diffusion, noise schedule (4) |
| C. Diffusion-Inspired Annealing for Sampling-Based MPC | Under III. METHOD: Algorithm 1, dual-loop, trajectory-level and action-level annealing (5)-(7) |
| IV. EXPERIMENT | Tasks, baselines and settings; parent of the three result subsections |
| A. Convergence and Coverage | Under IV. EXPERIMENT: comparison with MPPI, CMA-ES, NMPC and GCRL; convergence and coverage discussion |
| B. Test-Time Generalizability | Under IV. EXPERIMENT: task-level and dynamics-level generalisation, payload results |
| C. Robustness to Model Mismatch | Under IV. EXPERIMENT: mass mismatch in simulation and real-robot results |
| V. CONCLUSION | Summary, stated limitation, future work |
| REFERENCES | Bibliography, 46 entries |
| APPENDIX | Parent of A. Hardware and Software Setup and B. Task Implementation Details |
| A. Hardware and Software Setup | Under APPENDIX: robot, torque command (8), implementation, compute hardware, control rates |
| B. Task Implementation Details | Under APPENDIX: reward specifications, staged contact reward (9)-(10), task parameters for velocity tracking, sequential jumping, crate climbing, humanoid crate pushing |

For long sections, search a narrower subsection or prompt. Headings inside fenced quotations are source content, not document section boundaries.

## Supplementary information — [supplement.md](supplement.md)

| Exact heading | Look here for |
| --- | --- |
| Document beginning | Source text or supplied-material notes |

For long sections, search a narrower subsection or prompt. Headings inside fenced quotations are source content, not document section boundaries.

## Assets

Figure and table captions in the documents link to the files below. Open only the needed image; for a table, read its header and relevant rows first.

- `assets/figure/`: main figures (JPEG).
- `assets/supp_figs/`: supplementary and extended-data figures (JPEG).
- `assets/table/`: main tables (CSV, or JPEG when transcription is unreliable).
- `assets/supp_table/`: supplementary tables (CSV, or JPEG fallback).

Asset paths are relative to the skill root. CSVs retain internal blank rows; captions and merged headers may also occupy rows. Consult the document notes before treating every row as data.
