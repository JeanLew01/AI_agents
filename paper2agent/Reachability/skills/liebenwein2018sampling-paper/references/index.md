# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | Abstract; author block and affiliation are just above it |
| I. Introduction | Motivation, under-approximation setting, list of contributions, Figure 1 |
| II. Related Work | Prior reachability tools and verification work the paper positions itself against |
| III. Problem Definition | Dynamics, control set, reachability function f, union F, Lebesgue measure mu, and Problem 1 with inequality (1) |
| IV. Method | Section opener for the algorithms |
| A. Overview | Section IV: idea of the delta-packing approach; Algorithm 1 (GreedyPack) image and transcription |
| B. Approximately-optimal Algorithm | Section IV: Algorithm 2 (ApproximateReachability), including the line that sets delta from epsilon |
| C. Anytime, Asymptotically-optimal Algorithm | Section IV: Algorithm 3 (AnytimeApproximateReachability) |
| V. Analysis | Section opener: what is proved, which proofs are omitted, intuition and roadmap of Lemmas 3-6 and Theorems 7, 10 |
| A. Preliminaries | Section V: Hausdorff distance, delta-fattening, Assumptions 1-3, rectifiability, covering/packing numbers, Theorem 1, Lemma 2 (size of the GreedyPack output) with proof |
| B. Analysis of Algorithms 2 and 3 | Section V: Minkowski content (2), Lemmas 3-6, Theorem 7 (packing precision delta vs epsilon), Corollary 8, Corollary 9 (sample size), Theorem 10 (running time), Proposition 11 (anytime variant) |
| VI. Results | Section opener: simulation goal, implementation and hardware |
| A. Experimental Setup | Section VI: unicycle dynamics (7), ground-truth reachable set, RSL curve parametrisation |
| B. Evaluation of Computed Reachable Sets | Section VI: scenarios, comparison with uniform sampling, Figures 2-4, number of trials |
| VII. Conclusion | Summary and future work |
| Acknowledgments | Funding |
| References | Bibliography [1]-[36] |
| Conversion notes | Source version, how the mathematics was transcribed, omitted proofs, list of misprints kept as printed |

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
