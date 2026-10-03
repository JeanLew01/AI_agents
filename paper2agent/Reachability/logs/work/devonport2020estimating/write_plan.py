#!/usr/bin/env python3
"""Set title/notes in plan.json and title/review flags/navigation in bundle.json (devonport2020estimating)."""
import json, os
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
W = f"{R}/paper-review/devonport2020estimating-paper"
D = f"{W}/documents/s001-devonport2020estimating"
TITLE = "Estimating Reachable Sets with Scenario Optimization"

plan = json.load(open(f"{D}/plan.json"))
plan["title"] = TITLE
plan["notes"] = [
    "Source: A. Devonport and M. Arcak, \"Estimating Reachable Sets with Scenario Optimization\", L4DC 2020, "
    "Proceedings of Machine Learning Research vol. 120, pp. 75-84; converted from the PDF supplied as the PMLR "
    "v120 proceedings version (10 pages, single column, PDF produced 2020-05-01). The PDF pages carry no "
    "proceedings banner, running head or printed page number; page numbers mentioned in these notes are PDF "
    "pages 1-10.",
    "The authors' TeX source was not available. All mathematics (inline and displayed, equations (1)-(11), "
    "Theorems 1-2, Algorithm 1) was transcribed visually to LaTeX from 170-260 dpi renders of the PDF and "
    "cross-checked against the PDF's native text layer. Every formula was fully legible; no formula is kept as "
    "an image.",
    "Algorithm 1 is provided both as an image crop (assets/figure/algorithm-1.jpg) and as a LaTeX transcription; "
    "equation (8) is printed inside the Algorithm 1 box (PDF page 6), i.e. after equations (9)-(10) in reading "
    "order.",
    "The paper's own misprints are reproduced verbatim, not corrected: the chance constraint of equation (7) is "
    "printed with '\\le 1 - \\epsilon' (equations (2), (3) and (9) use '\\ge 1 - \\epsilon'); the Output line of "
    "Algorithm 1 prints '\\|Ax + b\\|_p \\le 1' whereas equations (6) and (8) use 'Ax - b'; Section 3 prints "
    "'\\Theta \\in \\mathbb{R}^{n_\\theta}' (element-of sign, where a subset relation would be expected); Theorem 1 "
    "starts with a lower-case 'let'.",
    "Theorem and proof labels are bold with the printed punctuation, which is none ('**Theorem 1 (Tempo et al. "
    "(2012), Corollary 12.1)**', '**Theorem 2**', '**Proof**'). The PDF prints theorem statements in italics; "
    "the italics are not reproduced: Theorem 1 runs from 'let' to 'with probability $\\ge 1 - \\delta$.' and "
    "Theorem 2 from 'Let' to equation (10). The norm delimiters are written \\| throughout (the PDF typesets "
    "them as '||' in the running text and as \\| in Algorithm 1).",
    "Table 1 is transcribed as cells (CSV); its first header cell is empty in the PDF. The paper has no appendix "
    "or supplementary material.",
]
json.dump(plan, open(f"{D}/plan.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

b = json.load(open(f"{W}/bundle.json"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 10 PDF pages were inspected against 170-dpi full-page renders plus 200-260 dpi crops of every region "
    "containing mathematics, the algorithm box, the figure, the table and the reference list. Prose is verbatim "
    "with extraction damage repaired (line-wrap hyphens, glued/split words, split diacritics in author names, "
    "author block mis-typed as headings). All inline and displayed mathematics, equations (1)-(11), Theorems 1-2 "
    "and Algorithm 1 were transcribed visually to LaTeX (no TeX source available) and cross-checked against the "
    "native text layer; no formula had to be kept as an image. Assets: Figure 1 (three-panel crop), Algorithm 1 "
    "(image crop plus transcription), Table 1 (cells). The complete reference list (19 entries) was read entry by "
    "entry. Printed misprints of the paper (relation sign in (7), '+ b' in the Algorithm 1 output line) are kept "
    "and recorded in the page notes and conversion notes. The PDF has no page furniture, so nothing is omitted."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "Problem, approach and the O(n^2) / O(n) sample-count claims in brief"},
    {"file": P, "heading": "1. Introduction", "purpose": "Motivation, related scenario-optimization and reachability work, statement of contribution (PDF pages 1-3)"},
    {"file": P, "heading": "2. Forward Reachable Sets", "purpose": "System model and transition function, definition of the reachable set (1), epsilon-accurate approximation, chance-constrained problem (2)"},
    {"file": P, "heading": "3. Scenario Optimization", "purpose": "Chance-constrained program (3), scenario program (4), Theorem 1 with the sample bound (5) and its assumptions"},
    {"file": P, "heading": "4. Scenario-Based Reachability with Norm Balls", "purpose": "Definition of the p-norm ball estimate (6)"},
    {"file": P, "heading": "4.1. Unconstrained Norm Balls", "purpose": "Problem (7), construction of Z, Theorem 2 with proof (9)-(10), Algorithm 1 with scenario program (8), sample-complexity discussion"},
    {"file": P, "heading": "4.2. Axis-aligned Norm Balls", "purpose": "Diagonal-A variant, reduced sample size N_diag (11), hyperrectangle case"},
    {"file": P, "heading": "5. Example: Safety Verification of a Medical Exoskeleton", "purpose": "Experimental setup and parameter values, sample sizes used, a posteriori check, Figure 1 and Table 1"},
    {"file": P, "heading": "6. Conclusions", "purpose": "Summary and the stated limitations of the approach"},
    {"file": P, "heading": "Acknowledgments", "purpose": "Funding grants"},
    {"file": P, "heading": "References", "purpose": "Complete bibliography (author-year, unnumbered)"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, misprints of the paper kept verbatim, asset notes"},
]
json.dump(b, open(f"{W}/bundle.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("plan and bundle written")
