# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | One-paragraph statement of the BRSL method and its three components; index terms |
| I. Introduction | Motivation; Figure 1 (overview of the BRSL loop) |
| A. Related Work | Section I-A: objective-based and exploration-based safe RL, control-theoretic safety layers, safe navigation, references [2]-[38] |
| B. Proposed Method and Contributions | Section I-B: what BRSL does, stated limitations (Lipschitz-constant approximation, discrete time, braking, perfect perception), the two contributions, code link |
| II. Preliminaries and Problem Formulation | One-sentence section overview |
| A. Notation and Set Representations | Section II-A: index and matrix notation, Minkowski sum, constrained zonotope (1), zonotope, linear map and Minkowski sum of zonotopes, interval as zonotope |
| B. Robot and Environment | Section II-B: black-box dynamics (2), Lipschitz assumption, Assumption 1 (braking failsafe), Assumption 2 (noise zonotope), obstacle and sensing assumptions |
| C. Reachable Sets | Section II-C: Definition 1 with the reachable set (3) |
| D. Safe RL Problem Formulation | Section II-D: RL state, reward, plan, policy, the safety requirement on reachable sets |
| III. Black-box Reachability-based Safety Layer | Overview of the three components; Algorithm 1 (safe RL loop with BRSL) as image and transcription, with its walk-through |
| A. Data-Driven Reachability Analysis | Section III-A: Algorithm 2 (data-driven zonotope reachability), offline data matrices (4a)-(4c), Lipschitz constant and covering radius, per-dimension Lipschitz zonotope |
| B. Adjusting Unsafe Actions | Section III-B: Algorithm 3 (projected gradient adjustment), Figure 2, constrained-zonotope intersection (5), collision-check linear program (6), gradient chain rule (7), (8a)-(8b), projection |
| C. Analyzing Safety | Section III-C: Theorem 1 (safety guarantee) and its proof, remark on the role of the offline data |
| IV. Evaluation | Setup (TD3, 500 offline data steps, ensemble model), goal-based and path-following environments with parameters, results discussion; Figures 3-4, Tables I-II |
| V. Conclusion | Summary and stated future work |
| References | Bibliography [1]-[55] |
| Conversion notes | Source version, how the mathematics was transcribed, float placement, table and algorithm conventions, source slips kept as printed (at the end of the file) |

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
