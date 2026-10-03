# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | One-paragraph statement of the algorithm, the type of guarantees and the two applications; keywords |
| 1. Introduction | Motivation, the three steps of $\epsilon$-RandUP (Figure 1), desiderata, list of contributions |
| 2. Related work | Deterministic and sampling-based reachability methods, set-estimation literature the analysis builds on |
| 3. Problem definition | Notation ($\mathrm{H}$, $\oplus$, balls, covering number $D(A,d)$), reachable set (1), estimator $\hat{\mathcal{Y}}^M_\epsilon$ (2), Hausdorff metric (3) |
| 4. Asymptotic analysis | Assumption 1 (sampling distribution near $\partial\mathcal{Y}$), Theorem 1 (Asymptotic Convergence), comparison with Lew and Pavone (2020) |
| 5. Finite-sample analysis | Overview of Section 5 (parent of 5.1-5.3) |
| 5.1. General finite-sample statistical guarantees | Assumption 2 (Lipschitz map), Assumption 3 (boundary coverage constant $\Lambda^L_\epsilon$), Theorem 2 (Finite-Sample Bound) with $\delta_M$ |
| 5.2. Analysis of a particular setting: smooth input set and continuous distribution | Assumption 4 ($r$-convexity of $\mathcal{X}^{\mathsf{c}}$, Figure 2), Assumption 5 (density lower bound $p_0$), Corollary 1 with $\Lambda^{r,L}_\epsilon$ |
| 5.3. Insights: the difficulty of reachability analysis and algorithmic design | Role of smoothness, of $L$ and $r$, scalability and the covering-number bound |
| 6. Results and applications | Overview of experiments, code and video links, computing hardware |
| 6.1. Sensitivity analysis | 2-D ball example with $f(x)=(Lx_1,x_2)$ and distributions $\mathbb{P}^\alpha_\mathcal{X}$; Figure 3 |
| 6.2. Verification of neural network controllers | Closed-loop ReLU controller benchmark, comparison with ReachLP, kernel method and GoTube; Figures 4-5; footnotes 1-2; sample-size choice from Theorem 2 |
| 6.3. Application to robust model predictive control | Free-flyer hardware experiment, MPC problem (4a)-(4b), parameters; Figure 6 |
| 7. Conclusion | Summary and future work |
| Acknowledgments | Thanks and funding |
| References | Bibliography, 50 unnumbered author-year entries |
| Appendix A. Formal definitions and random set theory | Appendix notation (parent of A.1-A.2) |
| A.1. Random set theory | Hausdorff metric (5), myopic topology, Definition 1 (random compact set), capacity functional, Theorem 3 with conditions (C1)-(C2) |
| A.2. Sampling-based reachability analysis | Probability-space formalisation of $\epsilon$-RandUP; footnotes 3-4 |
| Appendix B. Proofs | Parent of B.1-B.3 |
| B.1. Proof of Theorem 1 | Restated Assumption 1 and Theorem 1; proof steps (C1), (C2), (C2.1)-(C2.3); equations (6)-(7); Figure 7; footnotes 5-7 |
| B.2. Proof of Theorem 2 | Lemmas 2-5 with proofs (equation (8)), restated Theorem 2, Remark on $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$, proof of Theorem 2; footnote 8 |
| B.3. Proof of Corollary 1 | Lemma 6 (volume bound under $r$-convexity) with proof, restated Corollary 1 and its proof |
| Appendix C. Volume of the intersection of two hyperspheres | Formula for $\Lambda^{r,L}_\epsilon$ via $V(r,a)$ and the incomplete beta function |
| Appendix D. Computing the Lipschitz constant of a ReLU network from samples | Sampling procedure for $\hat{L}$, Lemma 7 and its proof |
| Appendix E. Experimental details | Parent of E.1-E.2 |
| E.1. Sensitivity analysis | Sampling distribution $\mathbb{P}^\alpha_\mathcal{X}$ (Beta radius), evaluation of the bound of Corollary 1, $p_0^\alpha$; Figure 8 |
| E.2. Verification of neural network controllers | System matrices, initial set, baselines, kernel, and the numerical evaluation of the finite-sample bound ($M\approx 1376$) |
| Conversion notes | Source version, how the mathematics was transcribed, numbering and placement conventions, source slips kept as printed (at the end of the file) |

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
