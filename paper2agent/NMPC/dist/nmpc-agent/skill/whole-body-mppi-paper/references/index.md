# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| I. INTRODUCTION | Motivation, Fig. 1 (Go1 box pushing, hardware vs MuJoCo), key design choices, three contributions, paper outline; Fig. 2 (system diagram) is placed at the end of this section |
| II. BACKGROUND AND RELATED WORK | Section overview; parent of II-A and II-B (the system diagram Fig. 2 is placed just before this heading) |
| A. Locomotion and Manipulation for Legged Robots | Under II: gradient-based MPC vs simulation-based RL for legged robots |
| B. Model-Predictive Path Integral Control | Under II: MPPI sampling, weights (1), mean update (2), temperature, Algorithm 1, Fig. 3 (box climb keyframes), related MPPI work |
| III. SAMPLING-BASED MPC FOR LEGGED ROBOTS | Section overview; parent of III-A to III-C |
| A. MuJoCo Physics Engine | Under III: simulator choice, CPU MuJoCo vs MJX/Isaac, 30-50 parallel rollouts |
| B. Representing Controls as a Cubic Spline | Under III: sampling spline control points and cubic interpolation |
| C. State Estimation | Under III: EKF fusing MoCap, IMU and encoders; planning/estimation model mismatch |
| IV. EXPERIMENTS AND RESULTS | Overview and project website; parent of IV-A to IV-F |
| A. Hardware Implementation | Under IV: workstation, ROS, update rate, time step, horizon T = 40, 30 samples, PD at 20 kHz; Fig. 4 |
| B. Walking on Flat Terrain | Under IV: walking cost (3), Raibert-heuristic gait reference, Q and R |
| C. Locomotion Over Challenging Terrains | Under IV: climbing a box up to 0.24 m |
| D. Box Pushing | Under IV: box cost and (4), goal placement, success counts 9/10 and 6/10, Fig. 5 |
| E. Ablation Studies | Under IV: Fig. 6 sampling representation, Fig. 7 control frequency, temperature, prediction horizon, number of samples; Table I is placed at the end of this subsection |
| F. Comparisons to RL and MPC | Under IV: discussion of Table I (feature comparison; the table itself is placed just before this heading) |
| V. CONCLUSIONS AND FUTURE WORK | Summary; parent of V-A and V-B |
| A. Limitations | Under V: myopia beyond the horizon, simulator fidelity |
| B. Future Work | Under V: online contact/friction estimation, better sampling distributions, MJPC integration |
| ACKNOWLEDGMENTS | Thanks |
| REFERENCES | Bibliography [1]-[32] |

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
