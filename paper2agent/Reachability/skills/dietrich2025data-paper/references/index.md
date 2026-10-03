# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | Summary of the claims: holdout method for data-driven reachability, and the de-randomization discussion |
| I. Introduction | Motivation, related work on data-driven reachability, positioning against wait-and-judge scenario bounds |
| II. Problem Statement | Start of the setup section (subsections A to E below) |
| A. Forward Reachable Sets. | Reachable set definition, sampling distributions on X_0 and D, i.i.d. samples, sublevel-set estimator (1) |
| B. Violation Probability. | Violation probability / true error (2), empirical error (3)-(5), the target guarantee P{V > epsilon} <= beta |
| C. Nonconvex Scenario Reachability Analysis | Scenario program (6) with the volume proxy |
| D. Wait-and-Judge | The a-posteriori support-scenario baseline and its computational cost |
| E. Binomial Tail Inversion. | Definition 1: binomial tail inversion, equations (7)-(8) |
| III. The Holdout Method | Holdout sampling, Theorem 1 (bound (9)) and what the probability is taken over, computation, order-wise scaling in M and beta ((10)), zero-violation remark, marginal bound over training and holdout data, Figure 1 |
| IV. Applications | Start of the numerical section; comparison protocol against wait-and-judge |
| A. Reachable Sets | RBF scenario program (11)-(12), solver, experimental settings (gamma, 3000 samples, beta), runtime accounting |
| 1) Duffing Oscillator: | Duffing example: system, Table I (N, M, volume proxy, epsilon), Figure 2, runtimes |
| 2) Quadrotor: | Quadrotor example: dynamics (13), parameters, Table II, runtimes, and the "Sample Complexity" paragraph |
| B. Reachable Tubes | Reachable tube definition, time-varying RBF program, linear example (14), Figure 3 |
| V. De-randomization | The two layers of probability in PAC bounds and the case against de-randomizing them |
| A. De-randomization Methods | Enlargement-based de-randomization, level-set bound function, Lipschitz assumption, sample-and-cover |
| B. Lower Bounds from Zeroth-Order Optimization | Conditions (a)-(b), Lemma 1 and its proof, the (L/gamma)^d sample and query counts, Footnote 1, the three takeaways |
| VI. Conclusion | Closing summary |
| VII. Acknowledgments | Funding |
| References | Bibliography [1]-[36]; [28] is the source of Theorem 1, [19] the wait-and-judge baseline |
| Conversion notes | Source version, how the mathematics was transcribed, relocated items and limitations |

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
