# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | Summary of D-MPC and headline claims |
| 1 Introduction | MPC objective (1), why multi-step diffusion models and a learned action proposal, list of contributions |
| 2 Related work | Factored vs joint vs model-free; single-step vs multi-step; Dyna vs MPC; Table 1; Diffuser, Decision Diffuser, TD-MPC, MBOP, MBD, DyDiff |
| 3 Method | Section overview; parent of 3.1-3.4 |
| 3.1 Model predictive control | Under 3 Method: offline training then alternating plan/act; Algorithm 1 (main MPC loop) |
| 3.2 Model learning | Under 3 Method: offline dataset, diffusion dynamics p_d and action proposal rho, learned objective J (2), why no ensembles or reward model |
| 3.3 Planning | Under 3 Method: sampling-based planner, Algorithm 2 |
| 3.4 Adaptation | Under 3 Method: novel rewards via V_n = kappa J + kappa-tilde J-tilde; fine-tuning the dynamics model on play data |
| 4 Experiments | The four experimental questions; parent of 4.1-4.5 |
| 4.1 For fixed rewards, D-MPC is comparable to other offline RL methods | Under 4 Experiments: D4RL locomotion, Adroit and Kitchen comparison, Table 2 |
| 4.2 Generalization to novel rewards | Under 4 Experiments: height-based novel reward on Walker2d, Figure 1, comparison with Diffuser |
| 4.3 Adaptation to novel dynamics | Under 4 Experiments: simulated foot-torque defect on Walker2d, fine-tuning on play data (Table 3(a) is placed under 4.4.3) |
| 4.4 Ablation studies | Under 4 Experiments: parent of 4.4.1-4.4.4 (the summary Table 3(b) is placed under 4.4.3) |
| 4.4.1 Diffusion action proposals improve performance and simplify the planning algorithm | Under 4.4: MBOP baseline vs single-step diffusion proposal and sampling planner |
| 4.4.2 Multi-step diffusion action proposals contribute to improved performance | Under 4.4: single-step vs multi-step diffusion action proposals |
| 4.4.3 Multi-step diffusion dynamics models contribute to improved performance | Under 4.4: long-horizon prediction error, ART vs multi-step diffusion dynamics in the planning loop; Table 3(a), Table 3(b) and Figure 2 are placed here |
| 4.4.4 Necessity of Expressive Models for Multi-Step Prediction | Under 4.4: multi-step MLPs instead of diffusion models |
| 4.5 D-MPC can be distilled into a fast reactive policy for high-frequency control | Under 4 Experiments: distilling the planner into an MLP policy |
| 5 Conclusions | Summary, stated limitations (replanning cost, low-dimensional states, offline data coverage), future work |
| References | Bibliography (author-year style) |
| A Algorithms for model learning | Appendix: conditional diffusion training, denoising loss, Algorithms 3 (one-step models) and 4 (multi-step models) |
| B The MBOP-TrajOpt Algorithm | Appendix: Algorithm 5, the MBOP trajectory optimiser used as baseline |
| C Detailed ablation study results | Appendix: Table 4, per-domain scores of the ablation variants |
| D Normalizing state coordinates | Appendix: empirical-CDF normalisation of state coordinates to [-1, 1] and its inverse |
| E Model architectures and training details | Appendix: parent of E.1-E.6 |
| E.1 Diffusion models | Under E: DDIM with cosine schedule, transformer denoisers, token sizes, diffusion steps and layers per model |
| E.2 One-step MLP dynamics models | Under E: MLP dynamics architecture, Table 5 |
| E.3 Auto-Regressive Transformer dynamics model (ART) | Under E: ART tokens, loss (3), Table 6 |
| E.4 Model architectures for the objective function | Under E: transformer for J, discount factors, termination penalty |
| E.5 Training setups and hyper-parameters | Under E: optimiser, learning-rate schedule, steps, gradient clipping, EMA |
| E.6 Compute Resources | Under E: A100 GPUs and training time |
| F Hyper-parameters for the sampling-based planner | Appendix: forecast horizon F, number of samples N, history length H |
| G Long-horizon dynamics prediction | Appendix: RMSD metric behind Figure 2 and its limits |
| H Generalization to novel rewards | Appendix: details of the height-based novel reward experiment (Figure 1) |
| I Adaptation to novel dynamics | Appendix: defect simulation, play-data collection, fine-tuning protocol |
| J Timing measurements | Appendix: wall-clock planning time per step, Table 7, speed-up options |

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
