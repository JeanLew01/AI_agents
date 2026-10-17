# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| I. INTRODUCTION AND RELATED WORK | Motivation; run-ins 1) Generative Policies, 2) Sampling-based Predictive Control (SPC), 3) Our Contribution; Fig. 1 (GPC cycle) |
| II. BACKGROUND | Optimal control problem (1a)-(1c) and compact form (2); parent of II-A and II-B |
| A. Sampling-based Predictive Control | Under II: SPC procedure 1)-4) with (3)-(5), footnote 1; weightings MPPI (6), predictive sampling (7), CEM (8), Tsallis-MPPI (9) |
| B. Generative Modeling | Under II: flow matching objective (10) and loss (11); diffusion, noised density (12), Langevin step (13) |
| III. SPC IS ONLINE GENERATIVE MODELING | Target (14), noised target (15), Proposition 1 (score of the noised target, (16)) with proof (17)-(22), SPC update as score ascent (23), why predictive sampling |
| IV. GENERATIVE PREDICTIVE CONTROL | GPC target (24)-(25), Remark 1 (observation conditioning), vector field (26), GPC loss (27), footnote 2, Algorithm 1, parallelism |
| V. USING A TRAINED GPC POLICY | 1) Warm-Starts (28); 2) Deploying the Policy (GPC vs GPC+); 3) Risk-Aware Domain Randomization (29)-(32) |
| VI. SIMULATION STUDIES | Research questions, Fig. 2 (seven systems), network architectures, hardware; parent of VI-A to VI-D |
| A. Policy Performance | Under VI: evaluation protocol, footnote 3 (PPO tuning), Fig. 3(a) GPC/GPC+ vs PPO/SPC, Fig. 3(b) warm-starts vs action inpainting, inference times, Fig. 4 (double cart-pole with and without warm-start) |
| B. Training Stability | Under VI: cost decrease over iterations (the training curves, Fig. 5, are placed at the start of VI-C) |
| C. Risk-Aware Domain Randomization | Under VI: Fig. 5 (training curves, placed here), crane DR experiment (8 domains, beta = 0.25), Table I |
| D. Scalability | Under VI: 1-29 DoF, humanoid standup limit |
| VII. LIMITATIONS AND FUTURE WORK | Value-function learning, sample efficiency, splines and action spaces, actuation limits, hardware and image-conditioned policies |
| VIII. CONCLUSION | Summary and future work |
| REFERENCES | Bibliography [1]-[46] |
| APPENDIX I COSINE-DISTANCE OBJECTIVE WEIGHTING | Cosine similarity (33), weights (34) with gamma = 2.0, weighted loss (35), rationale |
| APPENDIX II EXAMPLE SYSTEM DETAILS | Zero-order-hold spline knots; task, actuation and observation of each example system (Table II, printed on page 10, is placed under Appendix III) |
| APPENDIX III TRAINING DETAILS | Evaluation rollouts (SPC 128 Gaussian; GPC+ 64 + 64); Table II (task specification parameters) and Table III (training and inference hyperparameters), both printed on page 10 |

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
