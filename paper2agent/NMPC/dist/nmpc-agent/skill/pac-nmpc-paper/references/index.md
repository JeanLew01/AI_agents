# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| I. INTRODUCTION | Motivation, contributions, Fig. 1 |
| II. RELATED WORK | Stochastic and robust NMPC, sampling-based MPC, PAC and statistical-learning approaches |
| III. BACKGROUND | Parent of the two background subsections |
| A. Iterative Stochastic Policy Optimization | Under III. BACKGROUND: ISPO formulation, surrogate distribution over policy parameters, equation (1), Algorithm 1 |
| B. PAC Bounds for Stochastic Policy Search | Under III. BACKGROUND: the PAC bound (2) on expected cost, its assumptions, Renyi-divergence and concentration terms, bound on constraint violation, optimisation problem; equations (2)-(9) |
| IV. APPROACH | Parent of the method subsections |
| A. PAC Stochastic Trajectory Optimization | Under IV. APPROACH: open-loop trajectory optimisation with PAC bounds, Algorithms 2-3 |
| B. PAC Feedback Motion Planning | Under IV. APPROACH: feedback policy parameterisation and its optimisation, equation (10), Algorithm 4 |
| C. PAC-NMPC | Under IV. APPROACH: receding-horizon algorithm, warm start, Algorithms 5-6 |
| V. SIMULATION EXPERIMENTS | Parent of the simulation subsections |
| A. Trajectory Optimization Experiments | Under V. SIMULATION EXPERIMENTS: bound validation on benchmark systems, figures of cost and collision-probability bounds |
| B. NMPC Experiment | Under V. SIMULATION EXPERIMENTS: closed-loop comparison and timing |
| VI. HARDWARE EXPERIMENTS | Parent of the hardware subsections |
| A. Rally Car | Under VI. HARDWARE EXPERIMENTS: hardware, setup and results on the 1/10th-scale rally car |
| B. Fixed-Wing UAV | Under VI. HARDWARE EXPERIMENTS: hardware, setup and results on the fixed-wing UAV |
| VII. DISCUSSION | Limitations and future work |
| REFERENCES | Bibliography, 37 entries |

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
