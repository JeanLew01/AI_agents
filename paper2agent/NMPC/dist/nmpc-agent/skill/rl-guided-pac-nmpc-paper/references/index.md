# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| I. INTRODUCTION | Motivation and contributions; Fig. 1 |
| II. RELATED WORK | Parent of A. Safe RL, B. Learned NMPC Warm-start, C. NMPC with Learned Waypoints, D. NMPC & RL Hybrids (Table I is placed there), E. Vision-based Agile Fixed-Wing Flight |
| III. PROBLEM FORMULATION | Definitions III.1-III.6: stochastic dynamics, sensor measurement, observation, stage cost, stage constraint, probabilistic safety guarantee |
| IV. BACKGROUND | Parent of A. PAC-NMPC and B. Actor-Critic RL |
| A. PAC-NMPC | Under IV. BACKGROUND: Definitions IV.1-IV.2 and the PAC-NMPC bounds and optimisation, equations (1)-(10) |
| B. Actor-Critic RL | Under IV. BACKGROUND: Definitions IV.3-IV.4, equations (11)-(12) |
| V. ACTOR-CRITIC PAC-NMPC (AC-PAC-NMPC) | Method overview with Fig. 2; parent of the three method subsections |
| A. RL-based Warm Start | Under V: warm start from the actor; Algorithm 1 |
| B. Uncertainty-Aware RL-Augmented Cost | Under V: equations (13)-(14) |
| C. Uncertainty-Aware Value Function Improvement Constraint | Under V: equations (15)-(17) |
| VI. RALLY CAR UGV WITH LIDAR: APPROACH AND EVALUATION | Parent of the rally-car subsections A-E; Figs. 3-4 are placed here |
| A. Rally Car Dynamics and LiDAR Sensor | Under VI: equation (18) |
| B. Actor-Critic | Under VI: equation (19) |
| C. Sensor Prediction | Heading occurs twice: under VI (rally car, equations (20)-(23)) and under VII (fixed-wing, Table V) |
| D. Simulation Experiments | Heading occurs twice: under VI (rally car: Tables II-III, Figs. 5-6) and under VII (fixed-wing: equations (32)-(34), Figs. 11-12, Tables VI-VIII) |
| E. Hardware experiments | Under VI: rally-car hardware trials; Fig. 7, Table IV |
| VII. FIXED-WING UAV WITH DEPTH CAMERA: APPROACH AND EVALUATION | Parent of the fixed-wing subsections A-E |
| A. Fixed-wing Dynamics and Depth Camera Sensor | Under VII: equations (24)-(31); Figs. 8-9 |
| B. Actor Critic Training | Under VII: Fig. 10 |
| E. Hardware Experiments | Under VII: fixed-wing flight experiments; Figs. 13-16, Table IX |
| VIII. ANALYSIS | Equation (35); parent of the analysis subsections A-D |
| A. One-Step Feasible Descent | Under VIII: Lemma VIII.1, Lemma VIII.2, Theorem VIII.1; equations (36)-(46) |
| B. Multi-Step Feasible Descent | Under VIII: Definitions VIII.1-VIII.2, Theorem VIII.2; equations (47)-(49) |
| C. Approximate Value Functions | Under VIII: equations (50)-(52) |
| D. Simulation Experiment | Under VIII: Dubins-car simulation supporting the analysis; Figs. 17-18 |
| IX. CONCLUSION | Conclusion and future work |
| REFERENCES | Bibliography, 78 entries |
| Conversion notes | Source details, table conventions, bold cells of Tables II-IV, printed peculiarities |

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
