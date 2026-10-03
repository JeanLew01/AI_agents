# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | One-paragraph statement of the problem, the three key ideas and the kind of guarantee |
| 1 Introduction | Motivation, related data-driven reachability work [14]-[19], the four steps of the approach, conformal inference background [22]-[27], paper layout, and the Notation paragraph (index sets, FFNN layer arrays, Zonotope, Minkowski sum, ceiling) |
| 2 Problem statement and Preliminaries | Stochastic system and trajectory distribution, initial-state distribution, train/test trajectory datasets and the i.i.d. remark, surrogate model, conformal inference recap (residuals, quantile index, coverage inequality), problem definition with equation (1) |
| 3 Scalable Data-Driven Reachability | Definition 1 (confident flowpipe) with equation (2) and the plan of Section 3 |
| 3.1 Computing Reachsets for Surrogate Models | Parent heading of 3.1.1 (no text of its own) |
| 3.1.1 ReLU Surrogate Model | Surrogate output vector and its components, Definition 2 (surrogate flowpipe), exact-star and approx-star reachability, partitioning of the initial set |
| 3.2 Computation of a guaranteed $\Delta$-confident flowpipe | Definition 3 (residual error) with footnote 2, Definition 4 (calibration dataset), conformal bound on each residual with footnote 3, Theorem 1 (inflated surrogate flowpipe and its confidence level) with proof and equations (3)-(5), minimum calibration-set size, remark on conservatism of the union bound |
| 4 Experimental Results | Common setup; Adaptive Cruise Control (equation (6), Figure 1, Table 1); Quadcopter (equation (7), Figure 2, Table 2); Laubloomis (equation (8), Figure 3, Table 3, CORA comparison): models, initial sets, noise, network sizes, dataset sizes, run times |
| 5 Conclusion | Authors' summary of the approach |
| Acknowledgments | Funding grants |
| References | Bibliography [1]-[37] |
| Conversion notes | Source version, how the mathematics was transcribed, moved floats, table layout, source slips kept as printed, scope of this version (at the end of the file) |

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
