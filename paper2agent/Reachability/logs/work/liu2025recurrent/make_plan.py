#!/usr/bin/env python3
"""Set title/notes in plan.json and title/review/navigation in bundle.json (idempotent).
Notes are printed into paper.md unchecked, so they contain no dollar signs."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/liu2025recurrent-paper"
D = W / "documents/s001-liu2025recurrent"
TITLE = "Recurrent Control Barrier Functions: A Path Towards Nonparametric Safety Verification"

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
plan["notes"] = [
    "Source version: arXiv:2510.02127v1 [eess.SY], 2 Oct 2025 (8 pages, IEEE two-column conference format); authors Jixian Liu and Enrique Mallada; the paper appeared at IEEE CDC 2025. This package was made from the arXiv v1 PDF, not from the proceedings version. This version contains the full proofs of Theorems 4 and 5 and the Appendix with the proof of Lemma 1; the proof of Theorem 3 is omitted by the authors (reference to [10, Theorem 11]).",
    "Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (main.tex), with the authors' private macros expanded to standard LaTeX (calligraphic X, U, K, R; the restriction bar), and every formula was checked against 250-300 dpi crops of the PDF pages; the TeX source and the PDF agree and no formula is kept as an image only. Unprinted author comments in the TeX source are not part of the paper and are not included.",
    "Equation numbers (1)-(20) are the printed ones and are written with `\\tag{n}`, one block per printed number; all other displays are unnumbered in the paper. Unnumbered multi-line derivations are written as one `aligned` block each (alignment only). The superscript star is written `^{\\ast}` and the end-of-proof box `\\square`.",
    "Theorem-like blocks start with the printed label in bold, including the printed name in parentheses (for example 'Assumption 1 (Forward Completeness).', 'Theorem 1 ( [2]).' with the printed space, 'Lemma 1.', 'Theorem 4.'); 'Proof.' is italic in the PDF and bold here. Bodies are italic in the PDF, which is not reproduced, so the end of each statement was taken from the TeX environment: Assumption 2 ends with the displayed Lipschitz inequality; Definition 3 with '... and denote by R(S).'; Definition 5 with '... are first-order Lie derivatives.'; Theorem 1 with '... control invariant.'; Definition 6 with 'We refer to such ... recurrent trajectory.'; Definition 7 with 'where the function gamma: R -> R_{>0}.'; Theorem 2 with '... the set h_{>=0} is safe.' (items (i), (ii) are plain paragraphs); Definition 8 with '... sector contained.'; Theorem 3 with the display defining delta-underbar; Lemma 1 with '... on the x variable.'; Theorem 4 with item (ii) (printed without a final period); Theorem 5 with display (20).",
    "Algorithms 1-4 are given as image crops (assets/figure/algorithm-1.jpg to algorithm-4.jpg), each followed by a text transcription with the printed line numbers; nesting is shown with two em-spaces per level. Figures 1-3 are image crops with verbatim captions (printed prefix 'Fig. n:'); the sub-captions printed inside Figures 2 and 3 ('(a) HJ Reachability', '(b) Recurrent Set Approximation'; '(a) Volume Difference', '(b) Computation Time') are in the crops and are repeated as the first line of the caption. Figure 3 is printed at the top of the right column of PDF page 7, before Section VII; here it follows the Section VI-B paragraph that discusses it.",
    "TABLE I and TABLE II (printed Roman numbering; assets table-1.csv and table-2.csv) are transcribed as cells. The first header cell is printed as a backslash-separated pair 'Methods \\ r_min' / 'Method \\ r_min', where r_min is r with subscript min; each value is followed in parentheses by a ballot x or a check mark (Unicode characters in the cells; the captions do not define the marks); in TABLE II the four times of the 'Recurrent Set' row (0.13, 0.61, 3.19, 19.75) are printed in bold. The captions are printed above the tables.",
    "Layout decisions: the two unnumbered first-page footnotes (affiliation with e-mail addresses; funding) are placed directly after the author line; 'Notation:' is a run-in italic paragraph at the end of Section I, not a heading; the abstract's run-in label 'Abstract—' is a heading here; small-caps section titles are written in title case; the Appendix follows the References as printed.",
    "The text and formulas are kept as printed. The following are in the source and are not conversion errors: 'parellizable' (abstract), 'intial state' (II-D), e-mail domain 'jh.edu'; in (7) the control inside the arg max is u while u_0 is selected; in Theorem 3 'there exists u in U^{(0,tau]}' has tau without hat while (11) maximizes over (0, tau-hat]; in the proof of Theorem 4 (i) the term 'r e^{-Lt}' has a minus sign in the exponent while (13) has r e^{Lt}, and the last display of that proof has an italic 'R_{t*}(X_u)'; Theorem 5 (ii) reads 'assume that for all u ... s.t. the following holds'; (17) and the proof of Theorem 5 use the notation h(y,u,t); the proof of Theorem 5 cites 'the conditions of (17)' and 'the conditions of (19)'; Algorithm 1 line 4 passes (17) and (20) as conditions and Section V says 'conditions (13) and (17), and (14) and 20' (last number without parentheses); the TABLE II caption says alpha = 1 while Section VI-A says beta = alpha = 0.05; V_BRT has an italic subscript in VI-A and an upright one in VI-B; in the Appendix a function g and the form F(x,u) - F(x,v) = g(x)(u-v) are used without definition, the integral term is ||u(s) - u(s)||, a calligraphic S appears in the arg min definitions, and the third line of the Case 3 display ends with an unmatched '|'.",
]
plan.pop("reading_order", None)
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
assert all("$" not in n for n in plan["notes"])

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 8 PDF pages (arXiv:2510.02127v1) were compared item by item with 170 dpi page renders and 250-300 dpi crops "
    "of every mathematical region, algorithm box, table and figure, and with the authors' TeX source (main.tex, edits.tex) "
    "and main.bbl. Two-column reading order was repaired on every page (page 6 had the four algorithm boxes fragmented and "
    "interleaved across columns; page 7 had the columns interleaved around three floats). All inline and display "
    "mathematics was rewritten in LaTeX from the TeX source with private macros expanded; the 45 extractor 'formula' "
    "image items (43 displays, one section heading and one text line that were misclassified) and the displays that had been flattened into text are now text items, the displays as $$ blocks, with \\tag for the 20 printed "
    "equation numbers (1)-(20). Assumptions 1-2, Definitions 1-8, Theorems 1-5, Lemma 1 and all proofs carry their "
    "printed labels in bold; statement ends were taken from the TeX environments. Algorithms 1-4 are image crops plus "
    "line-by-line transcriptions; Figures 1-3 are image crops (edges checked on wider renders) with verbatim captions; "
    "Tables I-II are cell transcriptions checked digit by digit. The 20 references were each compared with the page "
    "image. The only omitted region is the vertical arXiv stamp on page 1. Authors' typos and inconsistencies are kept "
    "and listed in the page review notes and in the conversion notes. Review was done by one agent; no independent "
    "second verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "One-paragraph statement of the RCBF notion, the signed-distance result and the data-driven method"},
    {"file": P, "heading": "I. Introduction", "purpose": "Motivation, related work [1]-[13], contributions, section outline; the run-in 'Notation' paragraph (norm, closed ball, signed distance sd(x,S)) is at its end"},
    {"file": P, "heading": "A. Problem Statement", "purpose": "Section II-A: control system (1), input signal sets, concatenation and restriction of inputs, trajectory phi, Assumption 1 (forward completeness), Assumption 2 (uniform local Lipschitz continuity)"},
    {"file": P, "heading": "B. Safety Assessment", "purpose": "Section II-B: unsafe region, Definition 1 (safe state), Definition 2 (control invariant set)"},
    {"file": P, "heading": "C. Reachability Analysis", "purpose": "Section II-C: Definition 3 (backward reachable tube), HJ value function and variational inequality, T-BRT sublevel set"},
    {"file": P, "heading": "D. Control Barrier Functions", "purpose": "Section II-D: Definition 4 (extended class K), Definition 5 (CBF, condition (2)), Theorem 1 (invariance of the superlevel set), remarks on SOS and neural CBFs"},
    {"file": P, "heading": "III. Recurrent Control Barrier Function", "purpose": "Lead paragraph of Section III (idea of replacing invariance by control recurrence)"},
    {"file": P, "heading": "A. Control Recurrent Sets", "purpose": "Section III-A: Definition 6 (control recurrent and control tau-recurrent sets, (3)-(4)), Figure 1, comparison with invariant sets"},
    {"file": P, "heading": "B. Recurrent Control Barrier Function", "purpose": "Section III-B: Definition 7 (RCBF condition (5)), piecewise gamma (6), Theorem 2 (safety assessment via RCBFs) with its proof ((7)-(8))"},
    {"file": P, "heading": "C. Signed Distance Function: a Valid RCBF", "purpose": "Section III-C: Definition 8 (sector containment (9)), class-K sub-class (10), Theorem 3 (signed distance as RCBF, (11), bound on tau-hat, delta-bar and delta-underbar)"},
    {"file": P, "heading": "IV. Safety Enforcement Using Recurrence", "purpose": "Lead paragraph of Section IV (robust conditions from trajectory samples)"},
    {"file": P, "heading": "A. Verification of a Cell", "purpose": "Section IV-A: Lemma 1 (trajectory deviation bound (12)), Theorem 4 (cell inside/outside the tau-BRT, (13)-(14)) with proof, Theorem 5 (robust RCBF conditions (15)-(20)) with proof"},
    {"file": P, "heading": "V. Numerical Methods", "purpose": "Cell partition and the three-stage procedure; Algorithms 1-4 (VerifyRegion, VerifyCells, SafetyCheck, SplitCell) as images and transcriptions"},
    {"file": P, "heading": "VI. Numerical Simulations", "purpose": "3D evasion dynamics, input range and collision set"},
    {"file": P, "heading": "A. Results Comparison", "purpose": "Section VI-A: simulation parameters, Table I (captured unsafe volume fraction), Table II (computation time), Figure 2 (contours)"},
    {"file": P, "heading": "B. Ablation Study", "purpose": "Section VI-B: sweep over tau and alpha, volume gap and computation time; Figure 3"},
    {"file": P, "heading": "VII. Conclusion and Discussion", "purpose": "Authors' summary, stated limitation and future work"},
    {"file": P, "heading": "References", "purpose": "Bibliography [1]-[20]"},
    {"file": P, "heading": "A. Proof of Lemma 1", "purpose": "Appendix A: Gronwall-type bound on the trajectory distance and the three cases for the signed distance"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, where each theorem-like statement ends, source slips kept as printed (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated")
