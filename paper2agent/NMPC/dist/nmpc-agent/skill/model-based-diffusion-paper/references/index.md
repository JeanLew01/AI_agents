# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | Summary of MBD and headline results |
| 1 Introduction | Motivation, Figure 1, contributions |
| 2 Related Work | Diffusion models, sampling-based optimisation, trajectory optimisation, diffusion for planning, Langevin MCMC for global optimisation |
| 3 Problem Statement and Background | Notation, trajectory optimisation problem (1a)-(1d), target distribution (2), forward and backward diffusion (3)-(5) |
| 4 Model-Based Diffusion | Section overview; parent of 4.1-4.3 |
| 4.1 Model-based Diffusion as Multi-stage Optimization | Monte Carlo score ascent (6), score derivation (7a)-(9b), Table 1 MBD versus model-free diffusion, how diffusion helps, connection with CEM, Algorithm 1 |
| 4.2 Model-based Diffusion for Trajectory Optimization | Constrained case: dynamically feasible samples, score (10a)-(10d); Algorithm 2 (its box is placed in the text of 4.3) |
| 4.3 Model-based Diffusion with Demonstration | Demonstration-augmented target distribution (11)-(13) |
| 5 Experimental Results | Overview of experiments and headline numbers |
| 5.1 MBD for Planning in Contact-rich Tasks | Benchmarks against CMA-ES, CEM, MPPI and RL: Tables 2-3, Figure 3; Figure 4 is also placed here |
| 5.2 Data-augmented MBD for Trajectory Optimization | Car UMaze and humanoid jogging with demonstrations (discusses Figure 4) |
| 6 Conclusion and Future Work | Summary and future directions |
| Acknowledgments | Funding |
| References | Bibliography, 64 entries |
| A Appendix / Supplemental Material | Start of the appendix; parent of A.1-A.8 |
| A.1 Notation Table | Symbols used in the paper |
| A.2 Convergence of Distribution with Small $\lambda$ | Definition 1, Proposition 2 and proof, Definition 3, Proposition 4 and proof, Proposition 5; equations (14a)-(28) |
| A.3 Black-box Optimization with MBD | Ackley and Rastrigin benchmarks, Figure 5, baseline implementation details |
| A.3.1 MBD for DNN Training without Gradient Information | MNIST MLP optimised without gradients |
| A.4 MBD with Demonstration Explaination | Equations (29)-(32), Figure 6, why the max weighting is used (heading printed 'Explaination') |
| A.5 Experiment Details | Parent of A.5.1-A.5.4 |
| A.5.1 Simulator and Environment | Task definitions: Ant, Hopper, Walker2d, Halfcheetah, Humanoid, PushT, Car2D |
| A.5.2 MBD Hyperparameters | Table 4, noise schedule |
| A.5.3 Baseline Algorithms Implementation | RL baseline settings (discusses Tables 5-6) |
| A.5.4 Demonstration Collections | RRT and mocap demonstration data; Tables 5-6 are placed after this subsection |
| A.6 MBD for Online Control | Receding-horizon MBD, Algorithm 3, Table 7, Figure 7 |
| A.7 Sample Number Abalation | Effect of sample count, Figure 8 (heading printed 'Abalation') |
| A.8 Objective Function Abalation | RL versus TO objectives, Figure 9 |
| NeurIPS Paper Checklist | The authors' answers to the 15 NeurIPS checklist items |

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
