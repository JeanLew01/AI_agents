#!/usr/bin/env python3
"""Set title/notes/reading_order in plan.json and title/review/navigation in bundle.json (idempotent)."""
import json
from pathlib import Path

R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/hewing2019scenario-paper"
D = W / "documents/s001-hewing2019scenario"
TITLE = "Scenario-based Probabilistic Reachable Sets for Recursively Feasible Stochastic Model Predictive Control"

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
plan["notes"] = [
    "Source version: accepted version from the ETH Research Collection, doi:10.3929/ethz-b-000389523 (7 PDF pages: page 1 is an ETH Library "
    "cover sheet, the paper itself is the remaining 6 pages in IEEE two-column format). Authors: Lukas Hewing, Melanie N. Zeilinger. Originally "
    "published in IEEE Control Systems Letters 4(2), 2020, doi:10.1109/lcsys.2019.2949194 (published online 2019). This package was made from the "
    "accepted version, not from the IEEE-typeset article; the accepted version carries no page numbers or running headers. The paper's own title "
    "page prints 'Scenario-based' (lower-case b); the cover sheet and the IEEE record print 'Scenario-Based'.",
    "No TeX source of the authors was available. All mathematics (inline and displayed) was transcribed visually to LaTeX from 200 dpi page "
    "renders, 300 dpi column crops and 500 dpi zooms of the densest formulas, and every transcribed formula was compiled with pdflatex as a "
    "syntax check. Every symbol was legible; no formula is kept as an image. Equation tags (1)-(17b) are the printed numbers; displays without a "
    "\\tag are unnumbered in the paper. The sans-serif transpose mark of the paper is written $\\mathsf{T}$.",
    "Layout decisions. The ETH cover sheet (PDF page 1) is reproduced as plain text under the added heading 'Repository cover sheet (ETH Research "
    "Collection)', placed after the title, the author line and the first-page footnote and before the abstract; only the ETH logo was omitted. "
    "The unnumbered first-page footnote (funding, affiliation, e-mail) is printed at the foot of the first column and is placed directly after "
    "the author line. Figure 1 is printed at the top of the page that carries Sections IV-C and V and is placed at the end of the Section V "
    "introduction; Figure 2 and Table I are printed inside the last paragraph of Section V-A and are placed directly after that paragraph, before "
    "'B. Results'. Theorem, corollary and proof labels are set in bold; the paper prints theorem and corollary statements in italics, which is "
    "not reproduced. Where the statements end: the statement of Theorem 1 consists of the sentence 'Let $N_s$ and $N_k$ satisfy', display (6), and "
    "the sentence 'The optimal solution $x^*$ of (5) is a feasible solution for optimization problem (4) with probability $1-\\beta$.'; Theorems 2 "
    "and 3 and Corollaries 1, 2 and 3 each end with the paragraph in which they start; Definitions 1 and 2 and Assumption 2 end with their "
    "display formula; Assumption 4 ends with the sentence 'and $\\mathcal{Z}_f \\subseteq \\mathcal{Z}_\\infty$, where ...' after its display; "
    "Assumptions 1 and 3 and Remarks 1-7 are single paragraphs.",
    "Table I is given as CSV/Markdown cells; its Constraint column contains small formulas that are stored in plain characters, with the printed "
    "LaTeX forms in a labelled conversion note below the table. The paper has no algorithm boxes and no numbered footnotes. The appendix (crane "
    "model and disturbance covariance) is part of this version and is included.",
    "The text and formulas are kept as printed. The following are in the source and are not conversion errors: in (2a) the index set "
    "'$\\{1, \\ldots n_c\\}$' and in the proof of Theorem 2 '$\\{v_0^*, \\ldots v_{N-1}^*\\}$' without a comma after the dots; '(see [9].' with an "
    "unclosed parenthesis before (8); in the proof of Theorem 2 '$v_i^* \\in \\mathcal{V}$ for all $1 \\le i \\le N$'; Assumption 4 defines "
    "$\\mathcal{Z}_\\infty$ as an intersection from $k=1$ while Remark 3 speaks of $k = 0, \\ldots, \\bar{N}$; in Section IV the sampled sequences "
    "are written $W^{(i)} \\sim \\mathcal{W}$ although Section II writes $W \\sim \\mathcal{Q}$, and $W^{(i)}$ runs to index $\\bar{N}-1$ while "
    "$E^{(i)}$ runs to $\\bar{N}$; 'Assumption (1)' and 'Figure (1)' with parentheses; Remark 5 says 'discard the $k$ samples' and Section V-A 'remove "
    "$k = 820$ samples', whereas elsewhere the number of discarded samples is written $N_k$ and $k$ is the time index; (15a) writes '$P > 0$' and Corollary 3 writes '$P^{*-1}$' although (15b) "
    "uses $P$; Remark 7 uses an index set $\\mathcal{I}_{\\text{dis}}$ that is not defined elsewhere; 'the sliders position'; the Fig. 2 caption "
    "writes $p_{ref}$; Section V-A names the sets $\\mathcal{R}_k^{\\theta_{\\max}}$ and $\\mathcal{R}_k^{\\theta_{\\min}}$ while Table I uses "
    "$\\pm\\theta_{\\max}$; the appendix equation uses $d_p$ for the slider damping while the text below it defines $d_m = 10$; the grant number in "
    "the first-page footnote is printed 'PP00P2 157601 / 1'; the cover sheet prints the permanent link with a doubled 'https://doi.org/' prefix.",
]

# Reading order = page order with three changes:
#  1. the paper's title, author line and first-page footnote (PDF page 2) come first, then the cover sheet (PDF page 1);
#  2. Figure 2 + caption (bottom of PDF page 6, inside a sentence that continues on page 7) follow the paragraph
#     that ends on page 7 (item p0007-b003).
FRONT = ["p0002-b000", "p0002-b001", "p0002-b007", "p0002-b008"]
FIG2 = ["p0006-b024", "p0006-b025"]
states = [json.loads((D / e["file"]).read_text(encoding="utf-8")) for e in plan["pages"]]
ids = {st["page"]: [it["id"] for it in st["items"] if it["kind"] != "omit"] for st in states}
for x in FRONT:
    assert x in ids[2], x
for x in FIG2:
    assert x in ids[6], x
order = list(FRONT) + ids[1] + [i for i in ids[2] if i not in FRONT]
for p in (3, 4, 5):
    order += ids[p]
order += [i for i in ids[6] if i not in FIG2]
assert ids[7][0] == "p0007-b003"
order += [ids[7][0]] + FIG2 + ids[7][1:]
allids = [i for p in sorted(ids) for i in ids[p]]
assert sorted(order) == sorted(allids) and len(set(order)) == len(order)
plan["reading_order"] = order
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 7 PDF pages (ETH Research Collection accepted version, doi:10.3929/ethz-b-000389523) were compared item by item with 200 dpi page "
    "renders; pages 2-7 additionally with 300 dpi column crops and 500 dpi zooms of (15a)/(15b), Corollary 3, Table I and the appendix "
    "equation. No TeX source exists for this paper, so all inline and display mathematics was transcribed visually to LaTeX; the 40 extractor "
    "'formula' image items were replaced by LaTeX $$ blocks (one $$ block per printed equation number (1)-(17b); the lines of a multi-line display stay together in one item); "
    "all transcribed formulas compile with pdflatex and none is kept as an image. Two-column reading order was repaired on every page (page 6 "
    "had the right column interleaved into the left one; column breaks inside paragraphs on pages 2, 3 and 6 were merged; sentences running "
    "over page breaks are joined). Definitions 1-2, Assumptions 1-4, Theorems 1-3, Corollaries 1-3, Remarks 1-7 and the two proofs carry "
    "their printed labels in bold. Figures 1-2 are image crops (edges checked on the built assets) with verbatim captions; Table I is "
    "transcribed as cells and checked on a 500 dpi zoom. The 16 references were each compared with the page image. The cover sheet (page 1) "
    "is kept as plain text under an added heading; the only omitted region is the ETH logo. Authors' slips and inconsistencies are kept and "
    "listed in the page review notes and in the conversion notes. Review was done by one agent; no independent second verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Repository cover sheet (ETH Research Collection)", "purpose": "Bibliographic record of this accepted version: authors, publication date, permanent link (DOI), rights/licence, journal reference and publisher DOI, funding entry"},
    {"file": P, "heading": "Abstract", "purpose": "Abstract and index terms"},
    {"file": P, "heading": "I. Introduction", "purpose": "Analytic-approximation versus randomized stochastic MPC, related work [1]-[14], what the paper contributes, outline"},
    {"file": P, "heading": "II. Preliminaries", "purpose": "Start of the preliminaries (subsections A-C follow)"},
    {"file": P, "heading": "A. Problem Formulation", "purpose": "Section II-A: system (1), disturbance model $W \\sim \\mathcal{Q}$, chance and input constraints (2a)/(2b), Remark 1, nominal/error split (3a)/(3b)"},
    {"file": P, "heading": "B. Probabilistic Reachable Sets", "purpose": "Section II-B: Definition 1 ($k$-step PRS), Definition 2 (PRS), what the probability level does and does not cover"},
    {"file": P, "heading": "C. Scenario Optimization", "purpose": "Section II-C: chance-constrained program (4), sampled program with discarded samples (5), Assumption 1, Theorem 1 with the binomial condition (6), sufficient condition (7) for the number of discarded samples $N_k$, sample-size bound (8) for $N_k = 0$"},
    {"file": P, "heading": "III. Stochastic MPC using Probabilistic Reachable Sets", "purpose": "Predictive dynamics (9a)-(9c), conditional predictive disturbance sequence $W_k$"},
    {"file": P, "heading": "A. Constraint Tightening", "purpose": "Section III-A: Assumption 2 (bounded tube controller), tightened constraints (10a)/(10b), Assumption 3 (tightening sets are PRS)"},
    {"file": P, "heading": "B. Stochastic MPC with Indirect Feedback", "purpose": "Section III-B: expected cost, sampled MPC problem (11a)-(11g), control law (12), Remark 2"},
    {"file": P, "heading": "C. Recursive Feasibility and Constraint Satisfaction", "purpose": "Section III-C: Assumption 4 (terminal set), Remark 3, Theorem 2 (recursive feasibility) with proof, Theorem 3 (closed-loop constraint satisfaction) with proof"},
    {"file": P, "heading": "IV. Probabilistic Reachable Sets using Scenario Optimization", "purpose": "How disturbance scenarios and simulated error trajectories are used to build PRS; Remark 4 (confidence level $1-\\beta$ and the MPC guarantees)"},
    {"file": P, "heading": "A. Scaling of Convex Set", "purpose": "Section IV-A: scaling problem (13a)/(13b), Corollary 1 ($d = 1$), Remark 5 (half-space PRS)"},
    {"file": P, "heading": "B. Polytopic PRS", "purpose": "Section IV-B: polytope level problem (14a)/(14b), greedy sample removal, Corollary 2 ($d = n_{hs}$)"},
    {"file": P, "heading": "C. Ellipsoidal PRS", "purpose": "Section IV-C: minimum-volume ellipsoid problem (15a)/(15b), Corollary 3 and Remark 6 (values of $d$), Remark 7"},
    {"file": P, "heading": "V. Simulation Example: Overhead Crane", "purpose": "Crane example: states, disturbance, constraints (16), (17a)/(17b), reference; Figure 1"},
    {"file": P, "heading": "A. Simulation Setup", "purpose": "Section V-A: cost weights, horizons, tube controller, number of scenarios, number of discarded samples, resulting probability/confidence levels, computation times; Figure 2 and Table I follow this paragraph"},
    {"file": P, "heading": "B. Results", "purpose": "Section V-B: closed-loop simulation outcome and empirical constraint satisfaction rates"},
    {"file": P, "heading": "VI. Conclusion", "purpose": "Closing summary"},
    {"file": P, "heading": "Acknowledgments", "purpose": "Thanks"},
    {"file": P, "heading": "Appendix", "purpose": "Crane (damped cart-pole) equations of motion, parameter values, sampling time, eigenvalues, disturbance covariance kernel"},
    {"file": P, "heading": "References", "purpose": "Bibliography [1]-[16]"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, layout decisions, source slips kept as printed (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated;", len(order), "items in reading_order")
