# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | One-paragraph statement of the method and its claims; keywords |
| 1. Introduction | Motivation, related work on data-driven reach sets and SOS/Christoffel approaches, list of contributions, structure of the paper |
| 2. Data-driven Reach Set Approximation with Christoffel Functions | Problem setting: transition function f, initial set, reachable set S as the support of a measure |
| 2.1. Preliminaries | Notation: monomials, polynomial space, number of monomials s(d), monomial vector v_d(x) |
| 2.2. Christoffel Functions | Moment matrix, Christoffel function (1), variational form, empirical measure, empirical moment matrix (2), empirical Christoffel polynomial (3), invertibility condition; footnote 1 |
| 2.3. Set Approximation with Christoffel Functions | Sublevel-set estimate (4)-(6), the PAC bound of Devonport et al. restated as Conjecture 1 and the authors' objection to it, convergence remarks, Example 1 (four squares) and Figure 1 |
| 3. Reach Set Approximation with Conformal Prediction | Nonconformity function, p-value, conformal region, marginal coverage statement (7) and why a guarantee conditional on the data set is needed |
| 3.1. Statistical Guarantees | Split into training and calibration sets; Theorem 2 (from Bates et al.), Theorem 3 with proof, Theorem 4 (coverage bounds (10)-(12)) with proof, Algorithm 1 (image and transcription), Example 2, Figures 2 and 3 |
| 3.2. Avoiding the Calibration Set | Transductive variant: nonconformity function with the test point added, Sherman-Morrison update (13), computational cost, Example 3, Figure 4 |
| 4. Robustness to Outliers | Theorem 5 (bound (14) with at most p outliers in the calibration set) with proof, Table 1, Example 4, Figure 5, Algorithm 2 (image and transcription) |
| 5. Experiments | One-sentence lead-in to the experimental section |
| 5.1. Empirical False Positive Rate | Comparison with one-class SVM, Isolation Forest and LOF as nonconformity functions: Table 2, Figure 6; outliers in the training set: Figures 7 and 8 |
| 5.2. Duffing oscillator | Duffing dynamics, parameter values, initial set, Figure 9 |
| 6. Conclusion | Authors' summary, scope of the results, numerical issues left for future work |
| Acknowledgments | Funding programme |
| References | Bibliography, 19 unnumbered author-year entries in alphabetical order |
| Conversion notes | Source version, how the mathematics was transcribed, differences between the arXiv TeX and the PMLR PDF, where theorem-like blocks end, moved floats, table conventions, source slips kept as printed, reviewer's numerical checks (at the end of the file) |

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
