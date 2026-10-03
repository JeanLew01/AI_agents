#!/usr/bin/env python3
"""Set title/notes/reading_order in plan.json and title/review/navigation in bundle.json (idempotent)."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/lew2022simple-paper"
D = W / "documents/s001-lew2022simple"
TITLE = "A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis"

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
plan["notes"] = [
    "Source version: arXiv:2112.05745v3 [eess.SY], 13 Apr 2022 (25 pages, single column, L4DC/JMLR style); authors T. Lew, L. Janson, R. Bonalli, M. Pavone; the paper appeared at L4DC 2022. This package was made from the arXiv v3 PDF, which contains the main text (Sections 1-7), the references and the appendix (Appendices A-E with all proofs), not from the proceedings version.",
    r"Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (main.tex, preamble.tex, main.bbl), with the authors' private macros expanded to standard LaTeX, and every formula was checked against the PDF pages (150 dpi page renders, 230-260 dpi crops for all theorem statements and all appendix proofs). No formula is kept as an image only. Where TeX and PDF differ the PDF was followed: the offset vector written \vec{r} in the source is printed as a bold letter (no arrow) and is transcribed $\boldsymbol{r}$.",
    r"Notation as printed: $\mathrm{H}(\cdot)$ is the convex hull (upright H; inside italic theorem bodies the PDF prints it in italic), $\oplus$ the Minkowski sum, $B(x,r)$ / $\mathring{B}(x,r)$ the closed / open ball, $D(A,d)$ the $d$-covering number, $\hat{\mathcal{Y}}^M$ the convex hull of the $M$ output samples and $\hat{\mathcal{Y}}^M_\epsilon=\hat{\mathcal{Y}}^M\oplus B(0,\epsilon)$ the $\epsilon$-padded estimator. In Appendix B the upright $Y$, $Y^M$, $Y^M_\epsilon$ (a generic compact set, the sample set, the union of $\epsilon$-balls around the samples) are different objects from the calligraphic $\mathcal{Y}$ (the reachable set). The Hausdorff distance is printed $d_\mathrm{H}$ in equations (3) and (5) and $d_H$ elsewhere.",
    r"Printed equation numbers are given with \tag: (1)-(3) and (4a)-(4b) in the main text, (5)-(8) and (C1)-(C2) in the appendix; all other displays are unnumbered in the paper. Theorem-like blocks carry their printed bold labels with the printed punctuation: Assumptions 1-5, Theorem 1 (Asymptotic Convergence), Theorem 2 (Finite-Sample Bound) and Corollary 1 in the main text; Definition 1, Theorem 3 and Lemmas 2-7 in the appendix (this version has no Lemma 1). Each block ends where the authors' TeX environment ends. Assumption 1, Theorem 1, Theorem 2 and Corollary 1 are stated in Sections 4-5 and restated in Appendix B.1-B.3, so each of these labels occurs twice; the appendix restatements of Theorem 2 and Corollary 1 write the conclusion as two separate probability bounds and are followed by a Remark on the assumption $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$.",
    "Figures 1-6 (main text) are image crops in assets/figure/, Figures 7-8 (appendix; printed numbering continues) are in assets/supp_figs/ as supplementary-figure-7 and supplementary-figure-8; all captions are verbatim text. Wrapped and floating figures are placed at paragraph boundaries next to the text that discusses them: Figures 1-5 and 8 beside the paragraphs they are printed next to, Figure 6 (printed at the top of its page) after the paragraph of Section 6.3 that cites it, Figure 7 (printed at the top of its page) in step (C2) of the proof of Theorem 1 where the TeX source inserts it. The paper has no tables and no algorithm box; the algorithm is described in Section 3 and Figure 1, and the two enumerated procedures of Appendix D and E.1 are transcribed as numbered lists.",
    r"Footnotes 1-8 are kept as separate paragraphs starting with 'Footnote n:'; the marks in the text are written $^{n}$. Footnotes 5, 6 and 8 stand where the page prints them (after the last text of their page). Footnotes 1, 2 and 7 are printed below a sentence that continues on the next page and are placed after the paragraph (footnote 1) or at the end of the subsection (footnote 2: end of Section 6.2; footnote 7: end of Appendix B.1) that carries the mark. Footnotes 3 and 4 are printed on the page where Appendix B begins and are placed at the end of Section A.2, which carries their marks. Two formulas are split by a page break in the PDF ($x_t\in\mathbb{R}^6$ in Section 6.3 and the set $\mathcal{X}_0$ in Appendix E.2); they are written whole.",
    "Citations are author-year as printed (the bibliography is unnumbered, 50 entries, alphabetical). Small-caps names are written RandUP, ReachLP, ReachSDP and GoTube; e-mail addresses printed in small caps are written in lower case; end-of-proof squares are written $\\blacksquare$.",
    r"The text and formulas are kept as printed. The following are in the source and are not conversion errors: 'thrustworthy' (Section 1); 'analyis' and 'guarantees, Our analysis' (Section 2); '$\mathcal{Y}^M_\epsilon$ converges' without a hat (after Theorem 1) and $\{\mathcal{Y}^M\}$, $d_H(\mathcal{Y}^M,\mathcal{Y})$ without hats in the conclusion of Theorem 3; '$d$-packing number' before Theorem 2 for the quantity defined as the $d$-covering number; the bound $(2d\sqrt{n}/\epsilon)^n$ with $n$ in Section 5.3; $d_H(\hat{\mathcal{Y}}^M,\mathcal{Y})$ without $\mathrm{H}$ in Section 6.1 and 'theorical' in the Figure 3 caption; the interval $[-0.015,0.015]$ without square in the definition of $\mathcal{X}_t(\nu)$ (Section 6.3); in the proof of Theorem 1: '$G^1_\partial$ ... for $j=1,2$', '$\bigcap_{N=0}^\infty A_n\subseteq A_0$', 'Since $\epsilon\rightarrow\bar\epsilon$', '$G^1_\delta,G^2_\delta$', '$m\geq 1$', 'a sufficient conditions', 'conludes'; in Appendix B.3 '$x\in\mathbb{R}^n$'; in Appendix C 'in Theorem 2', the constant $c_2$ introduced as a second '$c_1$', and the mixed use of $p$ and $n$ in $V(r,a)$; in Appendix E.1 an unbalanced parenthesis in the formula for $p_0^\alpha$; 'explicitely' (Appendix D).",
]
# Reading order: page order, except that footnote 1 (printed at the bottom of page 8 below a sentence
# that continues on page 9) follows the completed paragraph on page 9.
FOOT1, AFTER = "p0008-r009", "p0009-r001"
order, seen = [], {}
for entry in plan["pages"]:
    st = json.loads((D / entry["file"]).read_text(encoding="utf-8"))
    for it in st["items"]:
        seen[it["id"]] = it
        if it["kind"] == "omit" or it["id"] == FOOT1:
            continue
        order.append(it["id"])
        if it["id"] == AFTER:
            order.append(FOOT1)
assert seen[FOOT1]["markdown"].startswith("Footnote 1:"), seen[FOOT1]["markdown"][:40]
assert seen[AFTER]["markdown"].startswith("and GoTube") and seen[AFTER].get("join_previous") == "space"
assert order.count(FOOT1) == 1 and len(order) == len(set(order))
plan["reading_order"] = order
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 25 PDF pages (arXiv:2112.05745v3) were compared item by item with 150 dpi page renders, with 230-260 dpi crops of "
    "every theorem-like statement in the main text and of every appendix page with proofs (pages 17-25 completely), and with "
    "the authors' TeX source and .bbl. Every page was rewritten from the TeX source rather than patched: all inline and "
    "display mathematics is LaTeX with private macros expanded; the 40 extractor 'formula' image items and several displays "
    "that the extractor had emitted as glyph-soup text were replaced by $$ blocks, with \\tag for the printed numbers "
    "(1)-(3), (4a), (4b), (5)-(8), (C1), (C2). Assumptions 1-5, Theorems 1-3, Corollary 1, Definition 1, Lemmas 2-7, the "
    "Remark and all proofs carry their printed bold labels. Figures 1-8 are image crops whose edges were checked on wider "
    "renders (the extractor's Figure 2 crop missed the lower half, a first Figure 6 crop cut the x tick labels; both fixed), "
    "captions are verbatim; Figures 7-8 are routed to supp_figs as supplementary-figure-7/-8. The 50 reference entries were "
    "generated from the .bbl and each compared with the page image. Omitted regions: the vertical arXiv stamp on page 1, the "
    "running header on pages 2-25 and the page numbers on pages 2-25. Cross-page sentences are joined; footnote 1 is moved "
    "after its paragraph through reading_order, footnotes 2, 3, 4 and 7 are placed at the end of their subsection. One TeX/PDF "
    "difference (\\vec{r} printed as bold r) was resolved in favour of the PDF. Authors' typos and inconsistencies are kept "
    "and listed in the page review notes and in the conversion notes. The printed sample-size value 1376 of Appendix E.2 "
    "was recomputed from the transcribed formula (1375.6). Review was done by one agent; no independent second verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "One-paragraph statement of the algorithm, the type of guarantees and the two applications; keywords"},
    {"file": P, "heading": "1. Introduction", "purpose": "Motivation, the three steps of $\\epsilon$-RandUP (Figure 1), desiderata, list of contributions"},
    {"file": P, "heading": "2. Related work", "purpose": "Deterministic and sampling-based reachability methods, set-estimation literature the analysis builds on"},
    {"file": P, "heading": "3. Problem definition", "purpose": "Notation ($\\mathrm{H}$, $\\oplus$, balls, covering number $D(A,d)$), reachable set (1), estimator $\\hat{\\mathcal{Y}}^M_\\epsilon$ (2), Hausdorff metric (3)"},
    {"file": P, "heading": "4. Asymptotic analysis", "purpose": "Assumption 1 (sampling distribution near $\\partial\\mathcal{Y}$), Theorem 1 (Asymptotic Convergence), comparison with Lew and Pavone (2020)"},
    {"file": P, "heading": "5. Finite-sample analysis", "purpose": "Overview of Section 5 (parent of 5.1-5.3)"},
    {"file": P, "heading": "5.1. General finite-sample statistical guarantees", "purpose": "Assumption 2 (Lipschitz map), Assumption 3 (boundary coverage constant $\\Lambda^L_\\epsilon$), Theorem 2 (Finite-Sample Bound) with $\\delta_M$"},
    {"file": P, "heading": "5.2. Analysis of a particular setting: smooth input set and continuous distribution", "purpose": "Assumption 4 ($r$-convexity of $\\mathcal{X}^{\\mathsf{c}}$, Figure 2), Assumption 5 (density lower bound $p_0$), Corollary 1 with $\\Lambda^{r,L}_\\epsilon$"},
    {"file": P, "heading": "5.3. Insights: the difficulty of reachability analysis and algorithmic design", "purpose": "Role of smoothness, of $L$ and $r$, scalability and the covering-number bound"},
    {"file": P, "heading": "6. Results and applications", "purpose": "Overview of experiments, code and video links, computing hardware"},
    {"file": P, "heading": "6.1. Sensitivity analysis", "purpose": "2-D ball example with $f(x)=(Lx_1,x_2)$ and distributions $\\mathbb{P}^\\alpha_\\mathcal{X}$; Figure 3"},
    {"file": P, "heading": "6.2. Verification of neural network controllers", "purpose": "Closed-loop ReLU controller benchmark, comparison with ReachLP, kernel method and GoTube; Figures 4-5; footnotes 1-2; sample-size choice from Theorem 2"},
    {"file": P, "heading": "6.3. Application to robust model predictive control", "purpose": "Free-flyer hardware experiment, MPC problem (4a)-(4b), parameters; Figure 6"},
    {"file": P, "heading": "7. Conclusion", "purpose": "Summary and future work"},
    {"file": P, "heading": "Acknowledgments", "purpose": "Thanks and funding"},
    {"file": P, "heading": "References", "purpose": "Bibliography, 50 unnumbered author-year entries"},
    {"file": P, "heading": "Appendix A. Formal definitions and random set theory", "purpose": "Appendix notation (parent of A.1-A.2)"},
    {"file": P, "heading": "A.1. Random set theory", "purpose": "Hausdorff metric (5), myopic topology, Definition 1 (random compact set), capacity functional, Theorem 3 with conditions (C1)-(C2)"},
    {"file": P, "heading": "A.2. Sampling-based reachability analysis", "purpose": "Probability-space formalisation of $\\epsilon$-RandUP; footnotes 3-4"},
    {"file": P, "heading": "Appendix B. Proofs", "purpose": "Parent of B.1-B.3"},
    {"file": P, "heading": "B.1. Proof of Theorem 1", "purpose": "Restated Assumption 1 and Theorem 1; proof steps (C1), (C2), (C2.1)-(C2.3); equations (6)-(7); Figure 7; footnotes 5-7"},
    {"file": P, "heading": "B.2. Proof of Theorem 2", "purpose": "Lemmas 2-5 with proofs (equation (8)), restated Theorem 2, Remark on $\\partial\\mathcal{Y}\\subseteq f(\\partial\\mathcal{X})$, proof of Theorem 2; footnote 8"},
    {"file": P, "heading": "B.3. Proof of Corollary 1", "purpose": "Lemma 6 (volume bound under $r$-convexity) with proof, restated Corollary 1 and its proof"},
    {"file": P, "heading": "Appendix C. Volume of the intersection of two hyperspheres", "purpose": "Formula for $\\Lambda^{r,L}_\\epsilon$ via $V(r,a)$ and the incomplete beta function"},
    {"file": P, "heading": "Appendix D. Computing the Lipschitz constant of a ReLU network from samples", "purpose": "Sampling procedure for $\\hat{L}$, Lemma 7 and its proof"},
    {"file": P, "heading": "Appendix E. Experimental details", "purpose": "Parent of E.1-E.2"},
    {"file": P, "heading": "E.1. Sensitivity analysis", "purpose": "Sampling distribution $\\mathbb{P}^\\alpha_\\mathcal{X}$ (Beta radius), evaluation of the bound of Corollary 1, $p_0^\\alpha$; Figure 8"},
    {"file": P, "heading": "E.2. Verification of neural network controllers", "purpose": "System matrices, initial set, baselines, kernel, and the numerical evaluation of the finite-sample bound ($M\\approx 1376$)"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, numbering and placement conventions, source slips kept as printed (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated; reading_order items:", len(order))
