# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | Abstract; the author block (five authors, UC San Diego, e-mail addresses) is just above it |
| 1 Introduction | Motivation (CMDP vs hard-constraint methods, CBF, HJ reachability, RCRL and its limits) and the three contributions |
| 2 Related Work | Section opener only; content in 2.1 and 2.2 |
| 2.1 Constrained Reinforcement Learning | CMDP-based methods: trust-region (CPO, PCPO, P3O, CRPO) and primal-dual (PPO Lagrangian, the penalized-reward method of [7]) |
| 2.2 Hamilton-Jacobi Reachability Analysis | HJ reachability, its scaling remedies, reachability in RL, stochastic reach-avoid literature |
| 3 Preliminaries | Section opener only; content in 3.1 and 3.2 |
| 3.1 Markov Decision Processes | MDP tuple, safety loss function h, H_min, H_max, discount factor, initial set and distribution, value function V^pi, trajectory-sampling notation |
| 3.2 Constrained Markov Decision Process | The (CMDP) problem with threshold chi, cost value function V^pi_c, two difficulties of CMDPs |
| 4 Stochastic Hamilton-Jacobi Reachability for Reinforcement Learning | Section opener; content in 4.1 and 4.2 |
| 4.1 Persistent Safety and HJ Reachability for Stochastic Systems | Definition 1 (safe/unsafe set), indicator function, Definition 2 (reachability value function V_h), Definition 3 (reachability estimation function, REF), Definition 4 (optimal REF), Theorem 1 (Bellman recursion of the REF), Definition 5 (feasible set) |
| 4.2 Comparison with RCRL | The (RCRL) problem and the stated drawbacks of optimizing V_h (weak signal, no re-entrance guarantee, deterministic only) |
| 5 Iterative Reachability Estimation for Safe Reinforcement Learning | Section opener with the roadmap of 5.1-5.4 |
| 5.1 Iterative Reachability Estimation for Deterministic Settings | Infeasible part (1), feasible part (2), Proposition 1 (V_c = 0 iff persistent safety), unified problem (3), Proposition 2 (re-entrance into the feasible set for gamma close to 1) |
| 5.2 Iterative Reachability Estimation for Stochastic Settings | The (RESPO) optimization problem weighted by the optimal REF; list of four benefits |
| 5.3 Overall Algorithm | Lagrangian for the feasible case, the learned REF p(s) and its max/discount update rule, time-scale requirement, full objective (4), Q-function relations, projection operators; Algorithm 1 (image and transcription) follows this section's text |
| 5.4 Convergence Analysis | Finite-MDP setting, assumptions A1 (step sizes, four time scales), A2 (strict feasibility), A3 (differentiability, Lipschitz), Theorem 2 (almost sure convergence to a locally optimal policy) |
| 6 Experiments | Figure 1 (environments), baselines and benchmarks paragraphs |
| 6.1 Main Experiments in Safety Gym, Safety PyBullet, and MuJoCo | Qualitative comparison with baselines; Figure 2 (Safety Gym and PyBullet curves) |
| 6.2 Hard and Soft Constraints | Two-drone tunnel task with hard constraints H1, H2 and a soft constraint; Figure 3 |
| 6.3 Ablation Studies | REF learning-rate ablation (Figure 5) and optimization-framework ablation (Figure 6); Figure 4 (MuJoCo curves) is also placed here |
| 7 Discussion and Conclusion | Summary and open extensions |
| 8 Acknowledgements | Funding (NSF, ONR, Amazon Research Award) |
| References | Bibliography [1]-[60] |
| A Notation | Appendix A: Table 1, list of symbols (with a marked LaTeX note) |
| B Gradient estimates | Appendix B: stochastic gradients for the reward and cost critics, the REF, the policy and the Lagrange multiplier; clipping of lambda to [0, lambda_max] |
| C Proofs | Appendix C opener; proofs are in C.1-C.4 |
| C.1 Theorem 1 with Proof | Restatement of Theorem 1 (printed as 'Theorem 3') and the five-line proof of the REF Bellman recursion |
| C.2 Proposition 1 with Proof | Restatement of Proposition 1 (printed as 'Proposition 3') and its IF / ONLY IF proof |
| C.3 Proposition 2 with Proof | Restatement of Proposition 2 (printed as 'Proposition 4'), explanation, proof by cases with bounds on H_E and H_N and inequalities (5), (6) |
| C.4 Theorem 2 with Proof | Restatement of Theorem 2 (printed as 'Theorem 4'); the proof is in the subsubsections C.4.1-C.4.4 |
| C.4.1 Intuition behind REF convergence | Regions W, X, Y, Z of the initial state space and Figure 7 |
| C.4.2 Proof Overview | The four time scales and the four proof steps |
| C.4.3 Proof Details | Full multi-timescale proof: Step 1 (critics), Step 2 (policy; Lemmas 1-3, ODE (7), Lyapunov function), Step 3 (REF Bellman operator, gamma-contraction, limiting optimization (8)), Step 4 (multiplier; Lemmas 4-5, ODE (9)), saddle-point conclusion |
| C.4.4 Remark on Bounding Lagrange Multiplier | Derivation of a lower bound on lambda_max in terms of R_max, gamma, T, H_Delta, P_min |
| D Complete Experiment Details and Analysis | Appendix D opener; details in D.1-D.10 |
| D.1 Baselines | Descriptions of PPOLag, CRPO, P3O, PCPO (CMDP class) and RCRL, CBF, FAC (hard-constraint class) |
| D.2 Benchmarks | Safety Gym, Safety PyBullet, Safety MuJoCo and multi-drone environments (observation dimensions, constraints, noise) |
| D.3 Hyperparameters/Other Details | Table 2 (hyperparameters, learning-rate schedules), code bases, hardware and training time |
| D.4 Double Integrator | Motivating example with Figure 8 (trajectories of RESPO and RCRL started in the infeasible set); dynamics, action range, constraint, cost |
| D.5 Safety Gym Environments | Figure 9 and per-method discussion for CarGoal and PointButton |
| D.6 Safety PyBullet Environments | Figure 10 and per-method discussion for DroneCircle and BallRun |
| D.7 Safety MuJoCo Environments | Figure 11 and per-method discussion for Reacher and HalfCheetah |
| D.8 Hard and Soft Constraints | Figure 12, the multi-constraint Lagrangians (10) for RESPO and (11) for PPOLag/RCRL/FAC, discussion |
| D.9 Ablation – Learning Rate | Figure 13 and discussion of REF learning rates x0.01 to x100 |
| D.10 Ablation – Optimization | Figure 14 and discussion of RESPO vs RCRL-with-REF vs PPOLag with chi = 0 |
| Conversion notes | Source version, how the mathematics was transcribed, equation and theorem numbering (including the renumbered appendix restatements), asset naming, float placement, text that exists only inside figures, source slips kept as printed |

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
