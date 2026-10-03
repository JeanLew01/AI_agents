# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | One-paragraph statement of the problem, the sampling-based guarantee and the Voronoi reduction (the author line and the title footnote with funding and affiliations are just above this heading) |
| 1 Introduction | Terminal-time stochastic reach-avoid problem, prior approximation methods [1]-[18], the two contributions, paper outline |
| 2 Problem formulation | Notation: $\mathbb{R}$, $\mathbb{N}_{[a,b]}$, transpose, all-ones vector |
| 2.1 System description | LTI dynamics (1), disturbance assumption, stacked form (2), probability measures $\mathbb{P}_X^{x_0,U}$ and $\mathbb{P}_W$ |
| 2.2 Stochastic reach-avoid problem | Terminal time probability (3), Problem 1 with (4)-(5), Remark 1, polytopic sets (6a)-(6c), sample set (7), Problem 2 (sampled MILP with big-M), Figure 1, limit (8) |
| 2.3 Problem statements | Random vector $Z$, Question 1 (number of scenarios for given $\delta$, $\beta$) and Question 2 (under-approximate MILP with $\hat{K}<K$ scenarios) |
| 2.4 Voronoi partition and data clustering | Voronoi cells (9), within-cluster sum of squares (10), optimal seeds (11), k-means complexity, Lemma 1 (translation invariance) and proof |
| 3 Scenarios required to meet given failure tolerance | Lemma 2 (Hoeffding, (12)), Theorem 1 with the scenario bound (13), its proof (14a)-(16), discussion of the bound |
| 4 Partition-based sample reduction | Problem 3: the reduced MILP with seeds $\psi^{(j)}$, importance rates $\alpha^{(j)}$ and buffers $\varepsilon^{(j)}$ |
| 4.1 Seed Selection and Buffer Computation | Lemma 3 (seeds computed offline from $G_wW$), Figure 2, Lemma 4 with buffer definitions (17)-(18) and proof (19)-(21), Figure 3, Remark 2 (cost of buffers), Theorem 2 (Problem 3 lower-bounds Problem 2) and proof, Remark 3 |
| 4.2 Tightening the Voronoi-based terminal time probability estimate | Theorem 3: re-evaluated estimate $\hat{p}$ (22) and the ordering of the three probabilities, with proof |
| 4.3 Implementation | Algorithm 1 (offline and online steps; image and transcription), choice of $\hat{K}$ from the WSS curve |
| 5 Illustrative Example: Spacecraft Rendezvous | CWH dynamics (23)-(24), noise, target and safe sets (25)-(26), experiment settings, Figure 4 (WSS, probability, run time versus $\hat{K}$), Table 1 (comparison with other methods), Figure 5 (trajectories) |
| 6 Conclusion | Authors' summary of the two results and of scalability |
| References | Bibliography [1]-[26] |
| Conversion notes | Source version and ACC title, how the mathematics was transcribed, equation numbering, where theorem-like statements end, moved floats, source slips kept as printed (at the end of the file) |

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
