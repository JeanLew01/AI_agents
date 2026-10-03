# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | One-paragraph statement of the RCBF notion, the signed-distance result and the data-driven method |
| I. Introduction | Motivation, related work [1]-[13], contributions, section outline; the run-in 'Notation' paragraph (norm, closed ball, signed distance sd(x,S)) is at its end |
| A. Problem Statement | Section II-A: control system (1), input signal sets, concatenation and restriction of inputs, trajectory phi, Assumption 1 (forward completeness), Assumption 2 (uniform local Lipschitz continuity) |
| B. Safety Assessment | Section II-B: unsafe region, Definition 1 (safe state), Definition 2 (control invariant set) |
| C. Reachability Analysis | Section II-C: Definition 3 (backward reachable tube), HJ value function and variational inequality, T-BRT sublevel set |
| D. Control Barrier Functions | Section II-D: Definition 4 (extended class K), Definition 5 (CBF, condition (2)), Theorem 1 (invariance of the superlevel set), remarks on SOS and neural CBFs |
| III. Recurrent Control Barrier Function | Lead paragraph of Section III (idea of replacing invariance by control recurrence) |
| A. Control Recurrent Sets | Section III-A: Definition 6 (control recurrent and control tau-recurrent sets, (3)-(4)), Figure 1, comparison with invariant sets |
| B. Recurrent Control Barrier Function | Section III-B: Definition 7 (RCBF condition (5)), piecewise gamma (6), Theorem 2 (safety assessment via RCBFs) with its proof ((7)-(8)) |
| C. Signed Distance Function: a Valid RCBF | Section III-C: Definition 8 (sector containment (9)), class-K sub-class (10), Theorem 3 (signed distance as RCBF, (11), bound on tau-hat, delta-bar and delta-underbar) |
| IV. Safety Enforcement Using Recurrence | Lead paragraph of Section IV (robust conditions from trajectory samples) |
| A. Verification of a Cell | Section IV-A: Lemma 1 (trajectory deviation bound (12)), Theorem 4 (cell inside/outside the tau-BRT, (13)-(14)) with proof, Theorem 5 (robust RCBF conditions (15)-(20)) with proof |
| V. Numerical Methods | Cell partition and the three-stage procedure; Algorithms 1-4 (VerifyRegion, VerifyCells, SafetyCheck, SplitCell) as images and transcriptions |
| VI. Numerical Simulations | 3D evasion dynamics, input range and collision set |
| A. Results Comparison | Section VI-A: simulation parameters, Table I (captured unsafe volume fraction), Table II (computation time), Figure 2 (contours) |
| B. Ablation Study | Section VI-B: sweep over tau and alpha, volume gap and computation time; Figure 3 |
| VII. Conclusion and Discussion | Authors' summary, stated limitation and future work |
| References | Bibliography [1]-[20] |
| A. Proof of Lemma 1 | Appendix A: Gronwall-type bound on the trajectory distance and the three cases for the signed distance |
| Conversion notes | Source version, how the mathematics was transcribed, where each theorem-like statement ends, source slips kept as printed (at the end of the file) |

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
