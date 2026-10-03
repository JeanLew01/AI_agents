#!/usr/bin/env python3
"""Set title/notes/reading_order in plan.json and title/review/navigation in bundle.json (idempotent)."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/sartipizadeh2019voronoi-paper"
D = W / "documents/s001-sartipizadeh2019voronoi"
TITLE = "Voronoi Partition-based Scenario Reduction for Fast Sampling-based Stochastic Reachability Computation of LTI Systems"

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
plan["notes"] = [
    "Source version: arXiv:1811.03643v1 [math.OC], 8 Nov 2018 (15 pages, single-column article layout); authors H. Sartipizadeh, A. P. Vinod, B. Açıkmeşe, M. Oishi. The title printed on this version ends with 'of LTI Systems'; the paper was published at the 2019 American Control Conference (ACC) under the title 'Voronoi Partition-based Scenario Reduction for Fast Sampling-based Stochastic Reachability Computation of Linear Systems'. This package was made from the arXiv v1 PDF, not from the proceedings version, so section, equation and reference numbers are those of the arXiv version.",
    "Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (ACC_2019_Voronoi_arxiv.tex), with the authors' private macros expanded to standard LaTeX, and every formula was checked against the PDF pages (150 dpi page renders and 220-240 dpi crops); the TeX source and the PDF agree and no formula is kept as an image only. The superscript asterisk is written \\ast throughout ($p^{\\ast}$, $U^{\\ast}_{K}$, ...); it is the same printed glyph.",
    "Equation numbers are the printed ones, (1)-(26), written with \\tag. The sub-numbered groups (6a)-(6c) and (14a)-(14c), and the pair (25), (26), are printed as aligned groups and are written as one display block per number. Displays without a printed number: the MILP of Problem 2, the MILP of Problem 3, $\\phi(W):=G_{w}W$ in Problem 3, $\\hat{X}(\\psi^{(j)})$ in Lemma 3, the final chain of inequalities in the proof of Theorem 1, and $p_{\\hat{K}}^{\\ast}\\leq\\hat{p}\\leq p_{K}^{\\ast}$ in Theorem 3. The optimisation problems are typeset by the authors with the optidef package ('max' with the decision variable below it and 's.t.'); they are written with \\max_{...} and an aligned block.",
    "Theorem-like statements (Problems 1-3, Remarks 1-3, Questions 1-2, Lemmas 1-4, Theorems 1-3) are printed with a bold label and an italic body; here the label is bold and the body upright. Where a statement ends was taken from the end of the italic text / the TeX environment: Problem 1 ends after '... induced from $\\mathbb{P}_X^{x_0,U}$.' (it contains (4) and (5)); Problem 2 after '... based on the probability law $\\mathbb{P}_W$.'; Lemma 1 after its item 2; Lemma 2 with (12); Theorem 1 with (13); Problem 3 after '... a lower bound on the solution of Problem 2.'; Lemma 3 after '... sampled state trajectory set $\\mathcal{X}_{K}^{x_0,U}$.'; Lemma 4 with (18); Theorem 2 after 'Problem 3 provides a lower bound for Problem 2.'; Theorem 3 with the chain $p_{\\hat{K}}^{\\ast}\\leq\\hat{p}\\leq p_{K}^{\\ast}$. Proofs start with the printed run-in 'Proof:' and end with the printed filled square, written $\\blacksquare$.",
    "Floats: Figures 1-5 are image crops with verbatim captions. Algorithm 1 is an image crop (assets/figure/algorithm-1.jpg) followed by a text transcription. Table 1 is given as cells (assets/table/table-1.csv): in the PDF its first body cell stacks 'Algorithm 1' and three parameter settings; it is written as a label row 'Algorithm 1' with empty value cells followed by the three setting rows, which all belong to Algorithm 1; the cells are plain text and 'K̂' in them is $\\hat{K}$ (the number of Voronoi cells). Reading order differs from the PDF page order for four floats: Figure 3 (printed at the top of page 9, between Theorem 2 and its proof) follows the sentence 'The buffering concept is illustrated in Figure 3.'; Figure 4 (printed at the top of page 12, in the middle of a sentence) follows the Section 5 paragraph 'We set $K=2000$ ...' that introduces it; Table 1 and Figure 5 (printed on page 13, after the Conclusion) follow the Section 5 paragraphs that cite them. Figures 1 and 2 are where the PDF prints them. The paper has one footnote, the title footnote with funding and affiliations: the PDF prints it at the bottom of page 1 (inside Section 1); here it follows the author line that carries its marker. There is no appendix and no printed page numbers.",
    "The text and formulas are kept as printed. The following are in the source (TeX and PDF) and are not conversion errors. (a) Theorem 1 states the event as $\\{p^\\ast(x_0)-p_{K}^{\\ast}(x_0)\\geq\\delta\\}$, while Question 1, equation (15), the final chain of the proof, the last sentence of the proof and the paragraph after it all use $\\{p_{K}^{\\ast}(x_0)-p^\\ast(x_0)\\geq\\delta\\}$ (the sampled optimum exceeding the true optimum by $\\delta$). (b) In the proof of Theorem 3 the Problem 3 optimum is written $\\hat{p}_{\\hat{K}}^\\ast$ (with a hat on $p$) and $(z^{(j)}=0)$ without a hat, while the theorem writes $p_{\\hat{K}}^{\\ast}$ and Problem 3 writes $\\hat{z}^{(j)}$; the same proof calls $\\alpha^{(j)}$ 'the set of original scenarios' and $\\mathcal{J}$ 'the subset of $\\mathcal{C}^\\ast$'. (c) (6c) reads $\\mathcal{R}=\\{x|FX\\leq h\\}$ and the text gives $F\\in\\mathbb{R}^{L\\times n_x}$. (d) Definition (9) quantifies '$\\forall j,\\ell\\in\\mathbb{N}_{[1,\\hat{K}]}$ and $j\\neq\\ell$'. (e) The time index is $k$ in $w_k$, $x_k$ in Section 2.1 and $t$ in (1). (f) Two different epsilons are printed and kept: $\\varepsilon^{(j)}$ is the buffer vector and $\\epsilon_{\\ell}^{(j)}$ are its components (notation, not a slip). (g) In Section 5: '$3\\omega x$' in (23), '$\\mathcal{W}_N$' for the sample set, 'exponentially increases exponentially', 'coincides the “knee”'. (h) The abstract says 'we propose a Voronoi partition-based to check' (a word is missing). The paper does not print the values of $\\delta$ and $\\beta$ used for $K=2000$ in Section 5.",
]

# Reading order: page order, except for four floats (see the conversion notes).
MOVES = {  # anchor item -> items to place right after it
    "p0008-b012b": ["p0009-b000", "p0009-b001"],   # Figure 3 + caption after 'The buffering concept is illustrated in Figure 3.'
    "p0011-b011": ["p0012-b000", "p0012-b001"],    # Figure 4 + caption after the paragraph 'We set K=2000 ...'
    "p0012-b002": ["p0013-b000", "p0013-b001"],    # Table 1 + caption after the paragraph that cites Table 1
    "p0012-b003": ["p0013-b002", "p0013-b003"],    # Figure 5 + caption after 'Figure 5 shows ...'
}
moved = {i for v in MOVES.values() for i in v}
order, allids = [], []
for entry in plan["pages"]:
    st = json.loads((D / entry["file"]).read_text(encoding="utf-8"))
    for it in st["items"]:
        if it["kind"] == "omit":
            continue
        allids.append(it["id"])
        if it["id"] in moved:
            continue
        order.append(it["id"])
        order += MOVES.get(it["id"], [])
assert sorted(order) == sorted(allids) and len(set(order)) == len(order), "reading_order must list every non-omitted item once"
plan["reading_order"] = order
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 15 PDF pages (arXiv:1811.03643v1, single-column) were compared item by item with 150 dpi page renders, with 220-240 dpi "
    "crops of every mathematical region (pages 3-11), and with the authors' TeX source and .bbl. All inline and display "
    "mathematics was rewritten in LaTeX from the TeX source with private macros expanded; the 35 extractor 'formula' image "
    "items were replaced by 36 $$ blocks, 30 of them with \\tag for the printed equation numbers (1)-(26) including (6a)-(6c) and "
    "(14a)-(14c). Problems 1-3, Remarks 1-3, Questions 1-2, Lemmas 1-4 and Theorems 1-3 carry their printed labels in bold; "
    "their ends were taken from the italic text / TeX environments and proofs end with the printed filled square. "
    "Figures 1-5 are image crops whose edges were set from the ink extent of the renders and checked on wider crops; "
    "Algorithm 1 is an image crop plus a transcription; Table 1 was rebuilt as cells and each value read on the page. "
    "Two cross-page or float-interrupted sentences were repaired (pages 10/11 and 11/12) and four floats were moved in the "
    "reading order (Figure 3, Figure 4, Table 1, Figure 5). The 26 references were each compared with the page image. The "
    "only omitted region is the vertical arXiv stamp on page 1. Authors' slips are kept as printed and listed in the page "
    "review notes and the conversion notes, in particular the reversed difference in the statement of Theorem 1. "
    "Review was done by one agent; no independent second verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "One-paragraph statement of the problem, the sampling-based guarantee and the Voronoi reduction (the author line and the title footnote with funding and affiliations are just above this heading)"},
    {"file": P, "heading": "1 Introduction", "purpose": "Terminal-time stochastic reach-avoid problem, prior approximation methods [1]-[18], the two contributions, paper outline"},
    {"file": P, "heading": "2 Problem formulation", "purpose": "Notation: $\\mathbb{R}$, $\\mathbb{N}_{[a,b]}$, transpose, all-ones vector"},
    {"file": P, "heading": "2.1 System description", "purpose": "LTI dynamics (1), disturbance assumption, stacked form (2), probability measures $\\mathbb{P}_X^{x_0,U}$ and $\\mathbb{P}_W$"},
    {"file": P, "heading": "2.2 Stochastic reach-avoid problem", "purpose": "Terminal time probability (3), Problem 1 with (4)-(5), Remark 1, polytopic sets (6a)-(6c), sample set (7), Problem 2 (sampled MILP with big-M), Figure 1, limit (8)"},
    {"file": P, "heading": "2.3 Problem statements", "purpose": "Random vector $Z$, Question 1 (number of scenarios for given $\\delta$, $\\beta$) and Question 2 (under-approximate MILP with $\\hat{K}<K$ scenarios)"},
    {"file": P, "heading": "2.4 Voronoi partition and data clustering", "purpose": "Voronoi cells (9), within-cluster sum of squares (10), optimal seeds (11), k-means complexity, Lemma 1 (translation invariance) and proof"},
    {"file": P, "heading": "3 Scenarios required to meet given failure tolerance", "purpose": "Lemma 2 (Hoeffding, (12)), Theorem 1 with the scenario bound (13), its proof (14a)-(16), discussion of the bound"},
    {"file": P, "heading": "4 Partition-based sample reduction", "purpose": "Problem 3: the reduced MILP with seeds $\\psi^{(j)}$, importance rates $\\alpha^{(j)}$ and buffers $\\varepsilon^{(j)}$"},
    {"file": P, "heading": "4.1 Seed Selection and Buffer Computation", "purpose": "Lemma 3 (seeds computed offline from $G_wW$), Figure 2, Lemma 4 with buffer definitions (17)-(18) and proof (19)-(21), Figure 3, Remark 2 (cost of buffers), Theorem 2 (Problem 3 lower-bounds Problem 2) and proof, Remark 3"},
    {"file": P, "heading": "4.2 Tightening the Voronoi-based terminal time probability estimate", "purpose": "Theorem 3: re-evaluated estimate $\\hat{p}$ (22) and the ordering of the three probabilities, with proof"},
    {"file": P, "heading": "4.3 Implementation", "purpose": "Algorithm 1 (offline and online steps; image and transcription), choice of $\\hat{K}$ from the WSS curve"},
    {"file": P, "heading": "5 Illustrative Example: Spacecraft Rendezvous", "purpose": "CWH dynamics (23)-(24), noise, target and safe sets (25)-(26), experiment settings, Figure 4 (WSS, probability, run time versus $\\hat{K}$), Table 1 (comparison with other methods), Figure 5 (trajectories)"},
    {"file": P, "heading": "6 Conclusion", "purpose": "Authors' summary of the two results and of scalability"},
    {"file": P, "heading": "References", "purpose": "Bibliography [1]-[26]"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version and ACC title, how the mathematics was transcribed, equation numbering, where theorem-like statements end, moved floats, source slips kept as printed (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated;", len(order), "items in reading order")
