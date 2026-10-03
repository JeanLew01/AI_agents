#!/usr/bin/env python3
"""Set title/notes in plan.json and title/review/navigation in bundle.json (idempotent)."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/devonport2021data-paper"
D = W / "documents/s001-devonport2021data"
TITLE = "Data-Driven Reachability Analysis with Christoffel Functions"

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
plan["notes"] = [
    "Source version: arXiv:2104.13902v1 [eess.SY], 28 Apr 2021 (7 pages, IEEE two-column conference format); authors A. Devonport, F. Yang, L. El Ghaoui, M. Arcak; the paper appeared at IEEE CDC 2021. This package was made from the arXiv v1 PDF, not from the proceedings version.",
    "Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (cfun-paper.tex), with the authors' private macros expanded to standard LaTeX, and every formula was checked against the PDF pages; the TeX source and the PDF agree and no formula is kept as an image only.",
    r"Only three displayed equations carry a printed number: (1) the sample-size bound in Theorem 1, (2) the Duffing dynamics, (3) the traffic dynamics; they are written with \tag{n}. All other displays are unnumbered in the paper.",
    "Algorithm 1 is given as an image crop (assets/figure/algorithm-1.jpg) followed by a text transcription; its lines are not numbered in the paper. Figures 1-3 are image crops with verbatim captions (printed prefix 'Fig. n.'). Figure 1 is printed as a full-width float at the top of PDF page 5 (inside Section IV-B); here it is placed in Section IV-A, directly after the paragraph that introduces it. The paper has no tables, no footnotes and no appendix.",
    "Theorem 1 and Lemma 2 end where the authors' theorem environments end in the TeX source ('... probability mass of $\\mu$.' and '... $\\ge 1-\\delta$.'); the PDF prints the commentary that follows them without a visible paragraph break. Numbers with thousands separators inside mathematics (156,626; 46,052; 2,009,600; 32,292) are written without LaTeX spacing commands.",
    "The text and formulas are kept as printed. The following are in the source and are not conversion errors: 'the assertion of Proposition 1' in Section IV-A (the paper states only Theorem 1); in Lemma 2, 'a sample of $M$ iid samples' and '$i=1,\\dots,n$' while the sum and the bound use $N$; after Lemma 2, $\\text{Pos}(\\mathbb{R}[x]^n_d)$ and 'the dimension of $\\mathbb{R}[x]^n_d$ is $\\binom{n+2k}{n}$' with index $d$; $M^{-1}$ without a hat in the optimization problem for $\\alpha$ and $z(x)$ without subscript $k$ just before it; $\\Phi(t_1;t_0,x_0,u)$ in Problem 1; $N_{ap}$ and $N_{AP}$ for the same quantity; in equation (3) an extra closing parenthesis in the third equation (the $\\dot{x}_n$ line), an undefined $\\beta$, and 'The input $u$' in the following text where the equation uses $d$.",
]
# Reading order: page order, except that Figure 1 and its caption (printed at the top of page 5)
# follow the page-4 paragraph that introduces the figure.
order = []
for entry in plan["pages"]:
    st = json.loads((D / entry["file"]).read_text(encoding="utf-8"))
    for it in st["items"]:
        if it["kind"] == "omit" or it["id"] in ("p0005-b000", "p0005-b001"):
            continue
        order.append(it["id"])
        if it["id"] == "p0004-b010":
            order += ["p0005-b000", "p0005-b001"]
assert "p0005-b000" in order
plan["reading_order"] = order
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 7 PDF pages (arXiv:2104.13902v1) were compared item by item with 170 dpi page renders and 200-300 dpi crops of "
    "the mathematical regions, and with the authors' TeX source and .bbl. Two-column reading order was repaired (page 3 "
    "had the right column interleaved with Algorithm 1; page 5 starts with a full-width float in the middle of a sentence). "
    "All inline and display mathematics was rewritten in LaTeX from the TeX source with private macros expanded; the 22 "
    "extractor 'formula' image items were replaced by 21 $$ blocks (three of them inside the Algorithm 1 transcription), with \\tag for the three printed equation numbers. "
    "Theorem 1, Lemmas 1-2, Remarks 1-2 and Problem 1 carry their printed labels in bold. Algorithm 1 is an image crop plus "
    "a transcription; Figures 1-3 are image crops (edges checked on wider renders) with verbatim captions. The 22 "
    "references were each compared with the page image. The only omitted region is the vertical arXiv stamp on page 1. "
    "Authors' typos and inconsistencies are kept and listed in the page review notes and in the conversion notes. "
    "Review was done by one agent; no independent second verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "One-paragraph statement of the method and the kind of guarantee"},
    {"file": P, "heading": "I. Introduction", "purpose": "Motivation, related data-driven reachability work [1]-[10], Christoffel-function background [11]-[15], the two contributions"},
    {"file": P, "heading": "Notation", "purpose": "Intervals, sub/superscript conventions, monomial vector $z_k(x)$, polynomial space $\\mathbb{R}[x]^n_d$"},
    {"file": P, "heading": "A. Probabilistic Reachability Analysis", "purpose": "Section II-A: transition function $\\Phi$, forward reachable set, measure $\\mu$, Remark 1, Problem 1, regularization requirement"},
    {"file": P, "heading": "B. Christoffel Functions", "purpose": "Section II-B: Christoffel function, moment matrix $M$, inverse and empirical inverse Christoffel function $C(x)$, invertibility condition on $\\hat{M}$"},
    {"file": P, "heading": "III. Christoffel Function Level Sets as Reachable Set Approximations", "purpose": "Algorithm 1 (image and transcription), Theorem 1 with sample-size bound (1), Lemma 1 (VC dimension), Lemma 2 (PAC bound), proof sketch, compactness and level-parameter optimization problem, Remark 2 (reduced-state variant)"},
    {"file": P, "heading": "IV. Examples", "purpose": "Computing platforms used for all three examples"},
    {"file": P, "heading": "A. Chaotic Nonlinear Oscillator", "purpose": "Section IV-A: Duffing dynamics (2), parameters, sample size, computation times, a posteriori accuracy check; Figure 1"},
    {"file": P, "heading": "B. Planar Quadrotor Model", "purpose": "Section IV-B: quadrotor dynamics, parameter values, initial and input sets, full-state versus reduced-state sample sizes and times; Figure 2"},
    {"file": P, "heading": "C. Monotone Traffic Model", "purpose": "Section IV-C: traffic dynamics (3), parameters, monotonicity and tight interval over-approximation; Figure 3"},
    {"file": P, "heading": "V. Conclusion", "purpose": "Authors' assessment of the bound and the kernel / infinite-dimensional extension left open"},
    {"file": P, "heading": "Acknowledgments", "purpose": "Funding grants"},
    {"file": P, "heading": "References", "purpose": "Bibliography [1]-[22]"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, source slips kept as printed (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated")
