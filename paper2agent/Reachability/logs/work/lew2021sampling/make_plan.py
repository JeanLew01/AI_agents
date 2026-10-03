#!/usr/bin/env python3
"""Set title/notes in plan.json and title/review/navigation in bundle.json (idempotent)."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/lew2021sampling-paper"
D = W / "documents/s001-lew2021sampling"
TITLE = "Sampling-based Reachability Analysis: A Random Set Theory Approach with Adversarial Sampling"
plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
plan.pop("reading_order", None)
plan["notes"] = [
    "Source version: arXiv:2008.10180v2 [eess.SY], 8 Nov 2020 (16 pages, single column: main text pp. 1-8, acknowledgments and references pp. 9-11, appendices A-D pp. 11-16); authors T. Lew and M. Pavone. The page footer names the venue, 4th Conference on Robot Learning (CoRL 2020), Cambridge MA, USA (proceedings: PMLR, 2021). This package was made from the arXiv v2 PDF, not from the PMLR proceedings file.",
    "Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (Lew.Pavone.CoRL20.tex, preamble.tex), with the authors' private macros expanded to standard LaTeX (bold symbols as \\boldsymbol{...}, \\mathcal{X}, \\mathbb{W}, \\mathbb{P}, ...), and every formula was checked against the PDF pages on 220-260 dpi renders; TeX source and PDF agree and no formula is kept as an image only. Equation numbers (1)-(22), including (19a)-(19c), are the printed ones and are given with \\tag; the other displays are unnumbered in the paper.",
    "Algorithm 1 (randUP, Section 3) and Algorithm 2 (robUP!, Section 4) are each given as an image crop (assets/figure/algorithm-1.jpg, algorithm-2.jpg) followed by a line-by-line transcription with the printed line numbers; the printed titles read 'Alg. 1.' / 'Alg. 2.'. The printed pseudocode has no 'end for': in Algorithm 2, lines 4-7 are the indented body of the for-loop of line 3 and line 8 (return) is outside it.",
    "Theorem 1, Theorem 2 (stated in Section 3 and restated verbatim in Appendix A), Definition 1, Definition 2 and the proof carry their printed labels in bold; theorem bodies are printed in italics, which is not reproduced. Conditions (C1) and (C2) of Theorem 1 are equations (3) and (4).",
    "Figures 1-6 are main-text image crops (assets/figure/). Figures 7-10 are printed in Appendix B and are stored as supplementary figures (assets/supp_figs/supplementary-figure-7 ... -10) with their printed labels 'Figure 7' ... 'Figure 10'. Figure 5 is an L-shaped arrangement of three plots, a small table and the caption; it is one crop that therefore also shows the printed caption, and the embedded table is additionally transcribed (assets/table/figure-5-table.csv). The paper has no numbered tables. Floats that are printed inside a paragraph (Figures 1, 6, 8, 10, Algorithm 1) are placed after that paragraph; Footnote 1 (code URL) is placed directly after the abstract that cites it, Footnotes 2-5 at the end of their pages' text, as printed; consequently Footnote 2 (cited in the related-work part of Section 1) appears at the end of Section 2, and Footnote 4 (cited in the Lipschitz comparison of Section 6) appears after the text of Section 7.",
    "The text and formulas are kept as printed. The following are in the source (PDF and TeX) and are not conversion errors: Definition 1 writes the intersection with calligraphic $\\mathcal{K}$ but quantifies over 'every compact set $K$'; the sampled tuples live in $\\mathcal{X}_0\\times\\mathcal{U}^{k-1}\\times\\Theta\\times\\mathbb{W}^{k-1}$ in Section 3 and Theorem 2, in $\\mathcal{X}_0\\times\\mathcal{U}^{N}\\times\\Theta\\times\\mathbb{W}^{N-1}$ in the description of Algorithm 1, and in $\\mathcal{Z}=\\mathcal{X}_0\\times\\mathcal{U}^{k}\\times\\Theta\\times\\mathbb{W}^{k-1}$ in Section 4 and in the proof; equation (2) lists the index range $i=1,\\ldots,k-1$ although $\\boldsymbol{u}_0,\\boldsymbol{w}_0$ appear; the definition of $\\boldsymbol{x}_k(\\boldsymbol{z})$ after (5) ends with an extra ')'; the table in Figure 5 has columns $\\mathcal{X}_0,\\mathcal{X}_1,\\mathcal{X}_2,\\mathcal{X}_4,\\mathcal{X}_5$; in Section 6 the disturbance bounds are given 'for $i=1,\\ldots,13$' and 'for $i=4,5,6$' and the discretised dynamics use $\\boldsymbol{\\theta}_k$; in Appendix C.1, $\\boldsymbol{Q}_{\\mathrm{nom},k}=\\boldsymbol{h}\\boldsymbol{Q}_k\\boldsymbol{h}^T$, the placement of the square in (14) and the unmatched parenthesis in the definition of $c$; in (17), $\\Gamma(n/2+2)$; spellings 'innacuracies', 'anynomous', 'news avenues', 'vizualize', 'conludes'.",
]
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 16 PDF pages (arXiv:2008.10180v2) were compared item by item with 130 dpi page renders and 220-260 dpi crops of "
    "every region containing mathematics, and with the authors' TeX source and .bbl. All inline and display mathematics was "
    "rewritten in LaTeX from the TeX source with private macros expanded; the 23 extractor 'formula' images were replaced by "
    "LaTeX display items with \\tag for the printed equation numbers (1)-(22). Theorem 1 (which the extractor had swallowed "
    "into one image together with Figure 2), Theorem 2 (main text and Appendix A), Definitions 1-2 and the proof carry bold "
    "printed labels. Algorithms 1 and 2 are image crops plus line-by-line transcriptions (the extractor had interleaved "
    "Algorithm 1 with the wrapped paragraph and classified Algorithm 2 as a heading plus a table). Figures 1-10 are single "
    "crops per figure (Figures 4, 5 and 8 were split into panels by the extractor; Figures 2, 6 and 10 were missing), edges "
    "checked on 200 dpi renders, captions verbatim; appendix Figures 7-10 are routed to supp_figs. The table embedded in "
    "Figure 5 is transcribed as CSV. Wrapped paragraphs around Figure 6, Figure 8, Figure 10 and Algorithm 1 were rebuilt "
    "from TeX and checked word by word. The 50 references were each compared with the page image and the .bbl. Omitted "
    "regions: the vertical arXiv stamp and the CoRL footer banner on page 1 and the page numbers of pages 2-16. Authors' "
    "typos and inconsistencies are kept and listed in the page review notes and the conversion notes. Review was done by "
    "one agent; no independent second verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "Summary of the method and claims; keywords; Footnote 1 with the code URL"},
    {"file": P, "heading": "1 Introduction", "purpose": "Motivation, the four contributions, Figure 1 (randUP overview), related work (sampling-based, Lipschitz-based, Hamilton-Jacobi, surrogate models), Notation paragraph ($\\mathcal{F}$, $\\mathcal{G}$, $\\mathcal{K}$, $\\mathrm{Co}$)"},
    {"file": P, "heading": "2 Problem Formulation", "purpose": "Dynamics (1), compactness and $C^1$ assumptions, reachable set definition (2), why the one-step recursion $\\tilde{\\mathcal{X}}_k$ differs, the three difficulties; Footnote 2 (cited in Section 1) is printed at the end of this section"},
    {"file": P, "heading": "3 Approximate Reachability Analysis using Random Set Theory", "purpose": "Definition 1 (random closed set), Algorithm 1 (randUP: image and transcription), Theorem 1 (conditions C1, C2; equations (3), (4)), Figure 2, Theorem 2 (almost-sure convergence to the convex hull) with its sampling assumption and proof outline, limitations: outer-/inner-approximation, rate of convergence"},
    {"file": P, "heading": "4 Adversarial Sampling for Robust Uncertainty Propagation", "purpose": "Adversarial-example analogy, objective (5) with $\\boldsymbol{Q}_k^M$ and $\\boldsymbol{c}_k^M$, projected gradient ascent, Algorithm 2 (robUP!: image and transcription), Figure 3"},
    {"file": P, "heading": "5 Leveraging System-Specific Properties and Applications", "purpose": "When stronger guarantees hold (convex reachable sets, Lipschitz inflation), remarks on convergence rates"},
    {"file": P, "heading": "6 Results and Applications", "purpose": "Linear system comparison with [11] (Figure 4), neural-network dynamics and Lipschitz comparison with [13] (Figure 5 and its table), spacecraft robust planning with parameter values and timings (Figure 6); its Footnote 4 is printed under 7 Conclusion"},
    {"file": P, "heading": "7 Conclusion", "purpose": "Summary and future directions; then Footnote 4 (belongs to the Lipschitz comparison in Section 6) and the Acknowledgments paragraph (funding)"},
    {"file": P, "heading": "References", "purpose": "Bibliography [1]-[50]"},
    {"file": P, "heading": "A Proof of Theorem 2", "purpose": "Restated Theorem 2 and the full proof: random-set measurability and monotonicity, (C1) via the first Borel-Cantelli lemma, (C2) in three steps via the second Borel-Cantelli lemma; equations (6)-(8)"},
    {"file": P, "heading": "B Further Details and Applications of Adversarial Sampling", "purpose": "Effect of the number of adversarial steps (Figures 7, 9), choice of $M$ and $n_{\\mathrm{adv}}$ with timings (Figure 8), sensitivity analysis / falsification (Figure 10)"},
    {"file": P, "heading": "C Additional Experimental Details", "purpose": "Parent heading of C.1 and C.2"},
    {"file": P, "heading": "C.1 Uncertainty Propagation using Lipschitz Continuity", "purpose": "Lipschitz-based ellipsoidal propagation baseline of [13]: Definition 2 (ellipsoidal set), equations (9)-(16)"},
    {"file": P, "heading": "C.2 Neural network experiment and comparisons", "purpose": "Network architecture and training hyperparameters, randomization ranges, computation times, Lipschitz constants used, ellipsoid volume formula (17)"},
    {"file": P, "heading": "D Robust Trajectory Optimization with Sampling-based Convex Hulls", "purpose": "Nominal trajectory (18), robust optimal control problem (19a)-(19c), reachability-aware problem (20), SCP procedure, constraint reformulations (21), (22), ellipsoidal outer bounds; Footnote 5"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, treatment of algorithms/figures/footnotes, source slips kept as printed (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated")
