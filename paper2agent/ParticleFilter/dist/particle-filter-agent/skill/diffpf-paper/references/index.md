# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| I. INTRODUCTION | Motivation, limitations of Kalman/particle/differentiable particle filters, DiffPF idea, Fig. 1, contributions |
| II. RELATED WORKS | Parent of A-C |
| A. Particle filter | Under II: bootstrap/SIR particle filters, degeneracy, proposal design |
| B. Differentiable Particle Filters | Under II: learned dynamics/observation models, proposals, normalizing-flow DPF, differentiable resampling (soft, OT) |
| C. Diffusion Models for Probabilistic Modeling | Under II: diffusion models in robotics, DnD filter |
| III. METHOD | Bayesian filtering setup, equally weighted particle set, Fig. 2 pipeline |
| A. Prediction and Perception Modeling | Under III: process model (1), sensor model (2), fusion/conditioning vector c_t (3) |
| B. Update Step | Under III: assumption post(x_t) ≈ p(x_t \| c_t) (4), equal-weight particle posterior (5), DDPM reverse sampling (6)-(7), particle-mean estimate (8) |
| C. End-to-End Training | Under III: DDPM noise-prediction loss (9), joint training of all components |
| IV. EXPERIMENTS | Tasks, baselines, particle counts (DiffPF 10 vs 100), U-Net, 10 diffusion steps, hardware, optimiser and training schedule |
| A. Vision-based Disk Tracking | Under IV: data, process model (10), heatmap fusion, Tables I-II (MSE, ablations, inference frequency), Fig. 3 |
| B. Global Localization | Under IV: DeepMind Lab mazes, process model (11), two-phase training, Tables III-V (RMSE, particle number, speed/memory), Figs. 4-6 incl. collapse under 10Σ prior noise |
| C. KITTI Visual Odometry | Under IV: KITTI-10 protocol, 10-fold CV, Table VI (m/m, deg/m) vs differentiable filters, LSTMs, smoothers |
| D. Robotic Manipulation | Under IV: UR5 tabletop task, identity process model, Table VII (MAE joints/end-effector, real and simulated), Fig. 7 |
| V. CONCLUSIONS | Summary and future work (weighted variants against sample collapse / mode dropping) |
| REFERENCES | Bibliography, 41 entries |

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
