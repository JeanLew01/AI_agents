# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | Summary of the two verification methods, their equivalence and the outlier-adjusted approach; keywords |
| 1. Introduction | Motivation, related work on reachability and neural reachable tubes, limits of the earlier iterative scenario method, list of contributions |
| 2. Problem Setup | System, target set, definition of the BRT, the probabilistic goal for the safe set, and the 9D multi-vehicle running example with its parameter values |
| 3. Background: Hamilton-Jacobi Reachability, DeepReach, and Safety Verification | Short introduction to the background section (overview of Sections 3.1 and 3.2) |
| 3.1. Hamilton-Jacobi (HJ) Reachability | Target function, cost function, value function (1), HJB-VI, Hamiltonian and optimal safety controller |
| 3.2. DeepReach and an Iterative Scenario-Based Probabilistic Safety Verification Method | Learned value function and induced policy, uniform value correction bound of the earlier iterative method, Remark 1 |
| 4. Robust Scenario-Based Probabilistic Safety Verification Method | Sampling procedure (what is sampled, definition of N and of the outlier count k), Theorem 2 with condition (2) and guarantee (3), interpretation of epsilon and beta, reach case, footnote 1 |
| 4.1. Comparison of Robust and Iterative Scenario-Based Probabilistic Safety Verification | Trade-off between outlier count and safety level at fixed N and across N; Figures 1 and 2 |
| 5. Conformal Probabilistic Safety Verification Method | Theorem 3 (Beta distribution (4) of the safe fraction), Figure 3, Remark 4 (coverage property), Lemma 5 with (5)-(6), Remark 6 (equivalence with the scenario method) |
| 6. Outlier-Adjusted Probabilistic Safety Verification Approach | Retraining on cost labels with a weighted MSE loss, validation metric, settings used in all case studies (w, beta, target epsilon) |
| 6.1. Multi-Vehicle Collision Avoidance | Case study on the running example; Figure 4 |
| 6.2. Rocket Landing | 6D rocket dynamics, target set, results and discussion of the training-regime limitation; Figure 5 |
| 6.3. Rocket Landing with No-Go Zones | Reach-avoid case study; Figure 6 |
| 7. Discussion and Future Work | Summary and stated future directions |
| Acknowledgments | Funding |
| References | Bibliography, 31 unnumbered entries sorted by author (author-year citations) |
| Appendix A. Robust Scenario-Based Proofs | Lemma 7: 1-D chance-constrained problem (7), sample counterpart with discarded constraints (8), condition (9), guarantee (10), and its proof from the sampling-and-discarding theorem |
| A.1. Proof of Theorem 2 | How the verification procedure is cast as the sample problem of Lemma 7 and how the bound on the induced cost transfers to the value function |
| Appendix B. Conformal Proofs | Start of the conformal-prediction proofs (Sections B.1-B.3) |
| B.1. Proof of Theorem 3 | Choice of score, calibration size and error rate; quantile computation; marginal coverage (11) and Beta distribution (12) |
| B.2. Proof that Split Conformal Prediction Reduces to Robust Scenario Optimization | General split conformal prediction setup, calibration-conditional coverage (13), reduction to Lemma 7 giving (14), equivalence via the incomplete beta function |
| B.3. Proof of Lemma 5 | Lemma 5 as a special case of Section B.2 and Lemma 7 |
| Conversion notes | Source version, how the mathematics was transcribed, numbering conventions, values printed only inside figures, source slips kept as printed (at the end of the file) |

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
