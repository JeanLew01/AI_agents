#!/usr/bin/env python3
"""Set title/notes/reading_order in plan.json and title/review/navigation in bundle.json (idempotent)."""
import json
from pagelib import D, R
W = R / "paper-review/hashemi2023data-paper"
TITLE = "Data-Driven Reachability Analysis of Stochastic Dynamical Systems with Conformal Inference"

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
plan["notes"] = [
    "Source version: arXiv:2309.09187v1 [eess.SY], 17 Sep 2023 (15 pages, single-column article layout, printed date 'September 19, 2023'); authors N. Hashemi, X. Qin, L. Lindemann, J. V. Deshmukh (University of Southern California). The paper appeared at IEEE CDC 2023; this package was made from the arXiv v1 PDF, not from the proceedings version, so section, equation and reference numbers are those of the arXiv version.",
    "Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (main.tex, the files under sections/, main.bbl), with the authors' private macros expanded to standard LaTeX (for example the horizon macro is an upright K, written `\\mathrm{K}`; the surrogate model is calligraphic `\\mathcal{F}` and its scalar output components are sans-serif `\\mathsf{F}^j`), and every formula was checked against the PDF pages. TeX source and PDF agree; no formula is kept as an image. Asterisk superscripts are written `^{\\ast}` and `\\hdots` is written `\\ldots`; these do not change the printed symbols.",
    "Printed equation numbers are given as `\\tag{n}`: (1) problem statement, (2) Definition 1, (3)-(5) in the proof of Theorem 1, (6) adaptive cruise control model, (7) quadcopter model, (8) Laubloomis model. All other displays are unnumbered in the paper.",
    "Theorem-like blocks: Definitions 1-4 and Theorem 1 carry their printed labels in bold; their italic bodies are not reproduced in italics. Each block ends where the authors' environment ends in the TeX source: Definition 1 with display (2); Definition 2 with '... in X-bar.'; Definition 3 with '... base vector of R^{n(K+1)}.'; Definition 4 with the line 'where R^j_i = ... .'; Theorem 1 with '... with initial state s_0 ~ I.' just before the proof. The bold run-in paragraph titles of Section 2 (Stochastic Dynamical System, Trajectory Datasets, Surrogate Model, Conformal Inference, Problem Definition), the title 'Notation.' at the end of Section 1 and the italic run-in titles of Section 4 (Adaptive Cruise Control, Quadcopter, Laubloomis) are not section headings and are kept as bold or italic paragraph openings; search for them as text.",
    "Footnotes: the three footnote marks are written as a superscript number in math mode with a space in front, and each footnote text is placed directly after the paragraph or definition that carries its mark, as 'Footnote n: ...' (in the PDF they are at the foot of pages 2 and 6). In Definition 3 the raised 2 after the surrogate component is the mark of footnote 2, not an exponent.",
    "Floats were moved to the text that discusses them: Figure 1 and Table 1 (printed at the top of PDF pages 8 and 9) follow the Adaptive Cruise Control paragraph; equation (7) (an uncaptioned full-width float at the top of PDF page 12, after the Conclusion has begun), Figure 2 (page 10) and Table 2 (page 11) follow the Quadcopter paragraph; Figure 3 (printed on page 13 inside the reference list) and Table 3 (page 11) follow the last Laubloomis paragraph. Figures 1-3 are image crops with verbatim captions.",
    "Tables 1-3 are printed as two side-by-side blocks of three columns (failure probabilities 0.10 to 0.06 in the left block and 0.05 to 0.01 in the right block); they are transcribed as printed, with six columns and the three header names 'Failure Probability', 'Conformal inference Run-time', 'Reachability Run-time' repeated. In each row, columns 1-3 belong together and columns 4-6 belong together. Cells keep the printed precision and the unit 'sec'.",
    "The text is kept as printed. The following are in the source and are not conversion errors: 'non-parameteric' (Section 1); the trajectory written with a subset sign and exponent (K+1)n in Section 2 and with an element sign and exponent n(K+1) afterwards; the test set written with the index i outside the subscript s_0 in Section 2; the residual declared in R_{>0} in Definition 3; 'e_j is the j-th base vector' in Definition 3 while the formula uses e_{j+n}; the index rule 'i·k+n' in footnote 2; absolute values typed with `\\mid`; the vector of bounds (R with superscript star) with a transpose before Theorem 1 and without it inside Theorem 1; the explicit lower bound on the calibration-set size printed after Theorem 1 as ceil((1+delta)/(1-delta)), although the condition printed just before it, ceil((L+1) delta) <= L, is by itself equivalent to L >= delta/(1-delta); strict inequalities in the first two displays of the proof of Theorem 1; a diagonal matrix d called a standard deviation with the noise written N(0, d^2); no unit for the Laubloomis sampling time (the unit 'sec', seconds, of the other sampling times is typed with the operator `\\sec` in the source and written `\\mathrm{sec}` here); 'Fig.3' without a space.",
    "Scope of this version: the paper has five numbered sections, acknowledgments and 37 references, and no appendix (the authors' TeX archive contains an unused file sections/appendix.tex, 'Training the Model', which is not part of the PDF and is not included here). The guarantee is stated for calibration and test trajectories drawn i.i.d. from the same distribution; this version has no section on distribution shift, and reference [33] ('Conformal prediction under covariate shift') is cited only for its Lemma 1.",
]

# Reading order: page order, with floats moved next to the paragraphs that discuss them.
MOVED = {"p0008-b000", "p0008-b001", "p0009-b000", "p0009-b001", "p0012-b000", "p0010-b000", "p0010-b001",
         "p0011-b000", "p0011-b001", "p0013-b000", "p0013-b001", "p0011-b002", "p0011-b003"}
AFTER = {
    "p0009-b005": ["p0008-b000", "p0008-b001", "p0009-b000", "p0009-b001"],          # ACC: Figure 1, Table 1
    "p0010-b002": ["p0012-b000", "p0010-b000", "p0010-b001", "p0011-b000", "p0011-b001"],  # Quadcopter: Eq. (7), Figure 2, Table 2
    "p0011-b004": ["p0013-b000", "p0013-b001", "p0011-b002", "p0011-b003"],          # Laubloomis: Figure 3, Table 3
}
order, kinds, joins = [], {}, {}
for entry in plan["pages"]:
    st = json.loads((D / entry["file"]).read_text(encoding="utf-8"))
    for it in st["items"]:
        if it["kind"] == "omit":
            continue
        kinds[it["id"]] = it["kind"]
        joins[it["id"]] = it.get("join_previous")
        if it["id"] in MOVED:
            continue
        order.append(it["id"])
        order += AFTER.get(it["id"], [])
assert len(order) == len(set(order)) == len(kinds), (len(order), len(kinds))
for a, b in zip(order, order[1:]):
    if joins[b]:
        assert kinds[a] in ("text", "caption") and kinds[b] in ("text", "caption"), (a, b)
plan["reading_order"] = order
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
for n in plan["notes"]:
    assert "$" not in n

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 15 PDF pages (arXiv:2309.09187v1) were compared item by item with 130 dpi page renders and 190-230 dpi crops of "
    "the mathematical regions (the paper is single-column 11 pt, so these resolutions show subscripts clearly), and with the "
    "authors' TeX source and .bbl. All inline and display mathematics was rewritten in LaTeX from the TeX source with "
    "private macros expanded; the 19 extractor 'formula' image items were replaced by text (18 displays and one text line), "
    "20 display blocks in total, with \\tag for the eight printed equation numbers (1)-(8). Definitions 1-4, Theorem 1 and its "
    "proof carry their printed labels in bold; Theorem 1 is split by the page break 6/7 and joined. Eight sentences that run "
    "across page breaks were joined, four of them across floats. Figures 1-3 are image crops (edges checked) with verbatim "
    "captions; Tables 1-3 are transcribed cell by cell (90 cells checked against the page and the TeX source). Equation (7), "
    "whose PDF text layer is unusable, was taken from the TeX source and checked line by line on a 230 dpi crop. Floats were "
    "moved to the paragraphs that discuss them through reading_order. The three footnotes follow the paragraphs that carry "
    "their marks. The 37 references were each read on the page image and compared by script with the PDF text layer. "
    "Omitted regions: the vertical arXiv stamp on page 1 and the 15 printed page numbers. Authors' slips are kept and listed "
    "in the page review notes and in the conversion notes. Review was done by one agent; no independent second verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "One-paragraph statement of the problem, the three key ideas and the kind of guarantee"},
    {"file": P, "heading": "1 Introduction", "purpose": "Motivation, related data-driven reachability work [14]-[19], the four steps of the approach, conformal inference background [22]-[27], paper layout, and the Notation paragraph (index sets, FFNN layer arrays, Zonotope, Minkowski sum, ceiling)"},
    {"file": P, "heading": "2 Problem statement and Preliminaries", "purpose": "Stochastic system and trajectory distribution, initial-state distribution, train/test trajectory datasets and the i.i.d. remark, surrogate model, conformal inference recap (residuals, quantile index, coverage inequality), problem definition with equation (1)"},
    {"file": P, "heading": "3 Scalable Data-Driven Reachability", "purpose": "Definition 1 (confident flowpipe) with equation (2) and the plan of Section 3"},
    {"file": P, "heading": "3.1 Computing Reachsets for Surrogate Models", "purpose": "Parent heading of 3.1.1 (no text of its own)"},
    {"file": P, "heading": "3.1.1 ReLU Surrogate Model", "purpose": "Surrogate output vector and its components, Definition 2 (surrogate flowpipe), exact-star and approx-star reachability, partitioning of the initial set"},
    {"file": P, "heading": "3.2 Computation of a guaranteed $\\Delta$-confident flowpipe", "purpose": "Definition 3 (residual error) with footnote 2, Definition 4 (calibration dataset), conformal bound on each residual with footnote 3, Theorem 1 (inflated surrogate flowpipe and its confidence level) with proof and equations (3)-(5), minimum calibration-set size, remark on conservatism of the union bound"},
    {"file": P, "heading": "4 Experimental Results", "purpose": "Common setup; Adaptive Cruise Control (equation (6), Figure 1, Table 1); Quadcopter (equation (7), Figure 2, Table 2); Laubloomis (equation (8), Figure 3, Table 3, CORA comparison): models, initial sets, noise, network sizes, dataset sizes, run times"},
    {"file": P, "heading": "5 Conclusion", "purpose": "Authors' summary of the approach"},
    {"file": P, "heading": "Acknowledgments", "purpose": "Funding grants"},
    {"file": P, "heading": "References", "purpose": "Bibliography [1]-[37]"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, moved floats, table layout, source slips kept as printed, scope of this version (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated;", len(order), "items in reading order")
