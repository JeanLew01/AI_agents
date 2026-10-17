# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| I. INTRODUCTION | Noise-schedule tuning problem, LP-MBD and ALP-MBD in brief, contributions 1)-3), Fig. 1 (obstacle-free driving vs overtaking) |
| II. RELATED WORK | Gradient-based vs sampling-based trajectory optimisation, MPPI/CEM/CMA-ES, diffusion and flow matching for planning, RL with sampling-based planners, RL fine-tuning of diffusion models |
| III. LINEAR PATH MODEL-BASED DIFFUSION | Section overview; parent of III-A to III-C |
| A. Variance Preserving Model-Based Diffusion | Under III: trajectory optimisation (1a)-(1c), target density (2), VP forward process (3)-(4), MBD denoising step (5), Monte-Carlo score (6), proposal (7), update (8), why (beta0, beta1, T) are coupled |
| B. Linear Path Model-Based Diffusion | Under III: linear probability path (9)-(10), denoising step (11), score (12), proposal (13), update (14), truncation t_max (15), sigma_max = t_max/(1 - t_max) (16) |
| C. Differences between VP-MBD and LP-MBD | Under III: three coupled VP parameters vs two decoupled LP parameters (sigma_max, T) |
| IV. ADAPTIVE LINEAR PATH MODEL-BASED DIFFUSION | Motivation for online adaptation, why LP-MBD suits RL; parent of IV-A and IV-B |
| A. Formulation as a Reinforcement Learning Problem | Under IV: MDP, scheduler policy over (T, sigma_max) (17), step-penalised reward (18), RL objective (19), Fig. 2 (architecture) |
| B. Implementation Details | Under IV: PPO choice, Algorithm 1 (training ALP-MBD with PPO) |
| V. EXPERIMENTS | Experimental questions (i)-(iii), GPU, default beta0, beta1 and sigma_max; parent of V-A to V-C |
| A. Numerical Experiments | Under V: 1D examples (Fig. 3), proposal standard deviations (20), 2D constrained Gaussian mixture, REINFORCE, AVP-MBD vs ALP-MBD (Fig. 4, learned parameters) |
| B. Evaluation of LP-MBD | Under V: Brax tasks, Table I (CEM, MPPI, VP-MBD, LP-MBD per-step rewards), Pusher discussion |
| C. Evaluation of ALP-MBD | Under V: mobile-robot trajectory tracking, kinematic model (21), reward (22), RL state, horizon and sample count, Table II, Fig. 5 (S-shaped path), Fig. 6 (oval path, generalisation) |
| VI. CONCLUSIONS | Summary |
| REFERENCES | Bibliography [1]-[41] |

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
