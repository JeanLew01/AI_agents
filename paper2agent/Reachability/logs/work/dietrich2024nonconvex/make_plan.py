#!/usr/bin/env python3
"""Set title/notes/reading_order in plan.json and title/review/navigation in bundle.json (idempotent)."""
import json
from pagelib import W, D

TITLE = "Nonconvex Scenario Optimization for Data-Driven Reachability"

NOTES = [
    "Source version: the published proceedings PDF, Proceedings of Machine Learning Research vol 242:514–527, 2024 "
    "(L4DC 2024); 14 PDF pages, single column; authors Elizabeth Dietrich, Rosalyn Alex Devonport, Murat Arcak. The "
    "first-page banner ('Proceedings of Machine Learning Research vol 242:514–527, 2024'), the running headers "
    "('DIETRICH DEVONPORT ARCAK' / 'NONCONVEX SCENARIO REACHABILITY') and the page numbers are omitted from the text. "
    "The paper has no appendix and no footnotes.",

    "Mathematics: the authors' TeX source was not available, so all inline and display mathematics was transcribed "
    "visually to LaTeX from 240-600 dpi renders of the PDF pages and then compiled with pdflatex and compared with "
    "the pages again. No formula is kept as an image. The paper prints fourteen numbered displays, (1)-(14); each is "
    r"written as a display block carrying its printed number as `\tag{n}`. Bold P is written $\mathbf{P}$, the upright 'Vol' $\mathrm{Vol}$, the double-struck "
    r"indicator $\mathbb{1}_{A_i}$. Where the authors typed three periods ('{0, 1, ..., N}', '$A_1, ..., A_m$') the "
    r"periods are kept; spaced dots are written `\ldots`. The e-mail addresses are printed in small capitals and are written "
    "in lower case.",

    "Reading order: floats that the PDF prints in the middle of a sentence were moved so that the prose is "
    "continuous. Figure 1 (top of PDF page 6) is placed in Section 3.2 before the paragraph that introduces it; "
    "Algorithm 2 (top of PDF page 7, inside Section 4) is placed at the end of Section 3.2, after the sentence that "
    "refers to it; Figure 2 (top of PDF page 8) follows the first paragraph of Section 4.1.1; Table 1 (top of PDF "
    "page 9, inside Section 4.2) is placed at the end of Section 4.1.2. The copyright line printed at the foot of "
    "the first page is placed directly after the author block.",

    "Algorithms 1 and 2 are given as image crops (assets/figure/algorithm-1.jpg, algorithm-2.jpg) followed by a text "
    "transcription: one paragraph per printed line with the printed line numbers, nesting shown by '&emsp;&emsp;' "
    "per level as read from the printed indentation. The boxes print no 'end' lines.",

    "Tables 1 and 2 are transcribed as cells (CSV in assets/table/). In both tables the first header cell is empty, "
    "and the row-group label (first column) and the value in the 'Estimate' column are printed once per group of "
    "three rows, on the first row of the group; the other cells of those columns are empty in the print and are left "
    "empty. The header symbol of the fourth column is written as the character ϵ; it is the $\\epsilon$ of the text. "
    "In the header 'Run Time of (1)/(2)' the numbers are printed as hyperlinks and refer to Algorithms 1 and 2.",

    "Theorem 1 is printed in upright type and the PDF shows no visible end of the statement. It is taken to end with "
    "display (3); the sentence that follows ('If we apply this general scenario theory to convex problems ...') and "
    "display (4) are the authors' refinement for the convex case and refer to Theorem 1 from outside.",

    "The text and formulas are kept as printed. The following are in the source and are not conversion errors: "
    "'$\\delta^{(1)}, ...\\delta^{(N)}$' without a comma and '(i.i.d)' in Section 2; 'We know $s_N^* < d$' before "
    "display (4), whose first case is '$s_N^* \\ge d$'; the upright 'd' in 'with d optimization variables'; "
    "$\\mathcal{R}$ used both for the reachable set and for its approximation, and 'from state $\\mathcal{X}_0$' in "
    "Section 3; the subscript $i$ on $\\theta_i$ inside the set of display (6); '$A_i \\cap A_j = \\emptyset\\ "
    "\\forall i$' and $\\mathbb{R}^D$ with capital $D$ in Section 3.1; in display (10) the left-hand side is "
    "$f(x, \\mu, \\sigma)$ while the exponent has $\\mu_i$ and $\\sigma_i$; display (9) ends with a comma and "
    "display (12) has a comma after $N$; in Algorithm 1, $\\Phi$ in line 1 but $\\phi$ in line 8, '$\\theta = 0$' "
    "without index in line 2, and the same index $i$ for sample and cell in line 9; in Algorithm 2, '$\\mu_i, "
    "\\ldots, \\mu_m$' in lines 2 and 23, a single exponential (no sum over the $m$ RBFs) in lines 11 and 18, and "
    "line 21 'If $\\Sigma_i = \\Sigma$, then $S = S + 1$' with an equals sign; 'Equation 4' / 'Equation 2' without "
    "parentheses in the algorithms; 'a Apple M2 Pro'; the Duffing dynamics written as one second-order equation "
    "$\\ddot{x} = -\\alpha y + x - x^3 + \\gamma \\cos(\\omega t)$ with states $x, y$; '$[-5, 5]$ x $[-5, 5]$' and "
    "'20x20' with the letter x; $sin$ and $cos$ in math italic in display (13); the closing quotation marks on both "
    "sides of ”one in a billion”; 'a-posterior' in the captions of Tables 1 and 2; 'positon' in the caption of "
    "Figure 3; 'Systems Control Letters' (no ampersand) and lower-case 'Hamilton-jacobi', 'christoffel', 'gaussian', "
    "'monte carlo' in the references.",

    "Number formats: '46, 052' (printed in math mode with a space after the comma) is written $46,052$; the "
    "percentages 74.91%, 88.82%, 88.75% and 87.47% are printed in math type and are written as plain text; '.01', "
    "'.999966' etc. are printed without a leading zero. In the bibliography, URLs and 'volume(issue):pages' strings "
    "that the PDF breaks across lines are closed up.",

    "Reviewer's check of the transcription (not part of the paper): evaluating the transcribed formulas with $N = "
    "1000$ and $\\beta = 10^{-9}$ gives 0.2509 from (4) with $s_N^* = 67$, $d = 400$ (Section 4.1.1) and 0.1253 from "
    "(2) with $s_N^* = 22$ (Section 4.2.2), as printed. The printed 0.1125 of Section 4.2.1 ($s_N^* = 19$) is "
    "obtained from (4) with $d = 100$, and the printed 0.1182 of Section 4.1.2 is obtained from (2) with $s_N^* = "
    "20$, whereas the text states $s_N^* = 19$ (which gives 0.1146); these values were re-read on the page and are "
    "transcribed as printed.",
]

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
plan["notes"] = NOTES

MOVE_AFTER = {                      # anchor id -> ids inserted right after it
    "p0001-b002": ["p0001-b013"],                       # copyright line after the author block
    "p0005-b020": ["p0006-b001", "p0006-b003"],         # Figure 1 + caption before 'Figure 1 demonstrates ...'
    "p0006-b006": ["p0007-alg2", "p0007-alg2-text"],    # Algorithm 2 at the end of Section 3.2
    "p0008-b004": ["p0008-b001", "p0008-b003"],         # Figure 2 + caption after the 4.1.1 paragraph
    "p0008-b006": ["p0009-b001", "p0009-b002"],         # Table 1 + caption at the end of Section 4.1.2
}
moved = {i for v in MOVE_AFTER.values() for i in v}
order, states = [], {}
for entry in plan["pages"]:
    st = json.loads((D / entry["file"]).read_text(encoding="utf-8"))
    for it in st["items"]:
        states[it["id"]] = it
        if it["kind"] == "omit" or it["id"] in moved:
            continue
        order.append(it["id"])
        order += MOVE_AFTER.get(it["id"], [])
allids = [i for i, it in states.items() if it["kind"] != "omit"]
assert sorted(order) == sorted(allids) and len(set(order)) == len(order), "reading_order incomplete"
# every join_previous item must directly follow a text/caption item in the reading order
for k, iid in enumerate(order):
    if states[iid].get("join_previous"):
        prev = states[order[k - 1]]
        assert prev["kind"] in ("text", "caption") and not prev["markdown"].rstrip().endswith("$$"), (iid, prev["id"])
        print(f"join {iid} <- {prev['id']}: ...{prev['markdown'][-40:]!r} + {states[iid]['markdown'][:40]!r}")
plan["reading_order"] = order
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 14 PDF pages of the PMLR v242 proceedings PDF were compared item by item with 170 dpi page renders and with "
    "240-600 dpi crops of every mathematical region, both algorithm boxes, both tables and all three figures. No TeX "
    "source was available: all inline and display mathematics was transcribed visually to LaTeX; the 14 extractor "
    "'formula' image items were replaced by 14 $$ blocks carrying the printed equation numbers (1)-(14), and no "
    "formula is kept as an image. Theorem 1 carries its printed bold label. Algorithms 1 and 2 (fragmented by the "
    "extractor into 12 and 18 list items) are image crops plus line-by-line transcriptions with the printed line "
    "numbers. Figures 1-3 (each split in two by the extractor) are single crops covering both panels, edges checked "
    "on wider renders, with verbatim captions. Tables 1 and 2 are transcribed as cells and every cell was compared "
    "with a 260 dpi crop. All 39 bibliography entries were read against the page images (split diacritics, line-wrap "
    "hyphens and broken URLs repaired). Omitted regions: the first-page proceedings banner, 13 running headers and "
    "13 page numbers. Four floats and the first-page copyright line are moved in the reading order so that no "
    "sentence is interrupted. The transcription of formulas (2) and (4) was checked by recomputing the epsilon values "
    "printed in Section 4. Authors' misprints and inconsistencies are kept and listed in the page review notes and "
    "in the conversion notes. Review was done by one agent; no independent second verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "One-paragraph statement of the approach and of the two estimators; keywords"},
    {"file": P, "heading": "1. Introduction", "purpose": "Related model-based and data-driven reachability work, prior convex scenario approach of Devonport and Arcak (2020b), what is generalized here"},
    {"file": P, "heading": "2. Nonconvex Scenario Optimization", "purpose": "Scenario program (1), violation probability $V(x)$, support scenarios and $s_N^*$, Theorem 1 (Campi et al., 2018) with $\\epsilon(s_N^*)$ in (2) and the probability bound (3), convex refinement (4)"},
    {"file": P, "heading": "3. Nonconvex Scenario-Based Reachability", "purpose": "Forward reachable set, sampling model, sublevel-set estimate $\\mathcal{R}(\\theta)$ (5), minimum-volume scenario programs (6)-(7) and the guarantee they aim at"},
    {"file": P, "heading": "3.1. Tiling with Basis Functions", "purpose": "Basis-function form (8), partition cells and indicator functions, program (9), support scenarios for the tiling, use of (4); Algorithm 1 (image and transcription)"},
    {"file": P, "heading": "3.2. Radial Basis Functions (RBFs)", "purpose": "Gaussian RBF (10), sublevel function (11), parameter vector $\\theta$, Figure 1, program (12), support scenarios for RBFs, use of (2); Algorithm 2 (image and transcription)"},
    {"file": P, "heading": "4. Examples", "purpose": "Hardware, threads, and the a-posteriori Chernoff-bound validation with its sample count and confidence"},
    {"file": P, "heading": "4.1. Duffing Oscillator", "purpose": "Dynamics, parameter values, initial set and time range of the first example"},
    {"file": P, "heading": "4.1.1. Tiling with Basis Functions", "purpose": "Duffing, Algorithm 1: grid, $N$, $\\beta$, run time, support-scenario count, $\\epsilon$, 100-trial statistics; Figure 2"},
    {"file": P, "heading": "4.1.2. Radial Basis Functions", "purpose": "Duffing, Algorithm 2: number of RBFs, threshold, $N$, $\\beta$, run time, support-scenario count, $\\epsilon$; Table 1"},
    {"file": P, "heading": "4.2. Quadrotor Model", "purpose": "Dynamics (13), parameter values, initial intervals (14), input set and time range; Figure 3"},
    {"file": P, "heading": "4.2.1. Tiling with Basis Functions", "purpose": "Quadrotor, Algorithm 1: grid, $N$, $\\beta$, run time, support-scenario count, $\\epsilon$; Table 2"},
    {"file": P, "heading": "4.2.2. Radial Basis Functions", "purpose": "Quadrotor, Algorithm 2: number of RBFs, threshold, $N$, $\\beta$, run time, support-scenario count, $\\epsilon$"},
    {"file": P, "heading": "5. Conclusion", "purpose": "Authors' summary of the two estimators"},
    {"file": P, "heading": "Acknowledgments", "purpose": "Funding grants"},
    {"file": P, "heading": "References", "purpose": "Complete bibliography, 39 entries, author-year style without numbers"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, moved floats, table and algorithm conventions, misprints of the paper kept as printed, reviewer's numerical check of (2) and (4) (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated;", len(order), "items in reading order")
