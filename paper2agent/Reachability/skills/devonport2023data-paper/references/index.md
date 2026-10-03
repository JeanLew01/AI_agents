# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | One-paragraph statement of the method and of the two kinds of PAC guarantee; key words |
| 1. Introduction | Motivation, related data-driven reachability work, Christoffel-function background, relation to the conference paper [10], contributions |
| 1.1. List of Acronyms and Symbols | Symbol list in four groups: reachability, probability / statistical learning, Christoffel functions, Gaussian processes |
| 2.1. Probabilistic Reachability and Estimation of Support | Section 2: reachable set (2.1), probabilistic relaxation, Problem 1 and the PAC bound (2.2), meaning of accuracy and confidence |
| 2.2. Christoffel Functions | Christoffel function, moment matrix, empirical inverse Christoffel function (2.3), matrix-inversion form (2.4)-(2.5), kernelized version (2.6)-(2.7), Footnote 1 |
| 3. Christoffel Function Estimators of Support | Algorithm 3.1 (polynomial estimator, classical PAC; image and transcription), overview of the two analyses, Remark 3.1 (reduced-state variation) |
| 3.1. Classical PAC Analysis | Empirical risk minimization, Lemma 3.2 with sample-size bound (3.1), Lemma 3.3 (VC dimension), Theorem 3.4 and its proof |
| 3.2. Bayesian PAC Analysis | Stochastic estimators and central concept, Theorem 3.5 (PAC-Bayes, (3.2)), Algorithm 3.2 (kernelized estimator), Theorem 3.6, constructions (3.3)-(3.5), Lemmas 3.7-3.9 with (3.6)-(3.8), proof of Theorem 3.6 |
| 3.3. Bayesian PAC Analysis: the Polynomial Case | Algorithm 3.3 (polynomial estimator with Bayesian PAC bound; image and transcription), (3.9)-(3.10), Lemma 3.10 with bound (3.11), Corollary 3.11, Remark 3.12 (choice of threshold $\eta$) |
| 3.4. Numerical Considerations for Large Datasets | Nyström approximation (3.12)-(3.13), KL divergence formulas (3.14)-(3.16) and eigenvalue upper bound |
| 4. Examples | Computing platform, common parameters ($\epsilon$, $\delta$, kernel, thresholds, initial and batch sizes), Table 1 (orders, times, sample sizes) |
| 4.1. Chaotic Nonlinear Oscillator | Duffing oscillator: dynamics, parameters, initial set, results; Figure 1 |
| 4.2. Planar Quadrotor | Quadrotor dynamics, parameter values, initial and input sets, reduced-state variation; Figure 2 |
| 4.3. Monotone Traffic | Cell transmission traffic model (4.1), parameters, comparison with interval over-approximation; Figure 3 |
| 5. Conclusion | Authors' summary and possible improvements (derandomized PAC-Bayes bounds, prior design) |
| References | Bibliography [1]-[34] |
| Appendix A. Background on Gaussian Process Models | Gaussian processes, GP regression posterior (A.1)-(A.4), link between posterior variance and the polynomial empirical inverse Christoffel function |
| Appendix B. Proofs of Some Results in Section 3.2 | Proofs of Lemma 3.7, Lemma 3.10, Lemma 3.8 and Lemma 3.9 (in this printed order), equations (B.1)-(B.11) |
| Conversion notes | Source version, numbering of this version, how mathematics/algorithms/tables were transcribed, source errors kept as printed (at the end of the file) |

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
