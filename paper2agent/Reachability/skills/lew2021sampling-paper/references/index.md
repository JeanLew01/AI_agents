# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | Summary of the method and claims; keywords; Footnote 1 with the code URL |
| 1 Introduction | Motivation, the four contributions, Figure 1 (randUP overview), related work (sampling-based, Lipschitz-based, Hamilton-Jacobi, surrogate models), Notation paragraph ($\mathcal{F}$, $\mathcal{G}$, $\mathcal{K}$, $\mathrm{Co}$) |
| 2 Problem Formulation | Dynamics (1), compactness and $C^1$ assumptions, reachable set definition (2), why the one-step recursion $\tilde{\mathcal{X}}_k$ differs, the three difficulties; Footnote 2 (cited in Section 1) is printed at the end of this section |
| 3 Approximate Reachability Analysis using Random Set Theory | Definition 1 (random closed set), Algorithm 1 (randUP: image and transcription), Theorem 1 (conditions C1, C2; equations (3), (4)), Figure 2, Theorem 2 (almost-sure convergence to the convex hull) with its sampling assumption and proof outline, limitations: outer-/inner-approximation, rate of convergence |
| 4 Adversarial Sampling for Robust Uncertainty Propagation | Adversarial-example analogy, objective (5) with $\boldsymbol{Q}_k^M$ and $\boldsymbol{c}_k^M$, projected gradient ascent, Algorithm 2 (robUP!: image and transcription), Figure 3 |
| 5 Leveraging System-Specific Properties and Applications | When stronger guarantees hold (convex reachable sets, Lipschitz inflation), remarks on convergence rates |
| 6 Results and Applications | Linear system comparison with [11] (Figure 4), neural-network dynamics and Lipschitz comparison with [13] (Figure 5 and its table), spacecraft robust planning with parameter values and timings (Figure 6); its Footnote 4 is printed under 7 Conclusion |
| 7 Conclusion | Summary and future directions; then Footnote 4 (belongs to the Lipschitz comparison in Section 6) and the Acknowledgments paragraph (funding) |
| References | Bibliography [1]-[50] |
| A Proof of Theorem 2 | Restated Theorem 2 and the full proof: random-set measurability and monotonicity, (C1) via the first Borel-Cantelli lemma, (C2) in three steps via the second Borel-Cantelli lemma; equations (6)-(8) |
| B Further Details and Applications of Adversarial Sampling | Effect of the number of adversarial steps (Figures 7, 9), choice of $M$ and $n_{\mathrm{adv}}$ with timings (Figure 8), sensitivity analysis / falsification (Figure 10) |
| C Additional Experimental Details | Parent heading of C.1 and C.2 |
| C.1 Uncertainty Propagation using Lipschitz Continuity | Lipschitz-based ellipsoidal propagation baseline of [13]: Definition 2 (ellipsoidal set), equations (9)-(16) |
| C.2 Neural network experiment and comparisons | Network architecture and training hyperparameters, randomization ranges, computation times, Lipschitz constants used, ellipsoid volume formula (17) |
| D Robust Trajectory Optimization with Sampling-based Convex Hulls | Nominal trajectory (18), robust optimal control problem (19a)-(19c), reachability-aware problem (20), SCP procedure, constraint reformulations (21), (22), ellipsoidal outer bounds; Footnote 5 |
| Conversion notes | Source version, how the mathematics was transcribed, treatment of algorithms/figures/footnotes, source slips kept as printed (at the end of the file) |

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
