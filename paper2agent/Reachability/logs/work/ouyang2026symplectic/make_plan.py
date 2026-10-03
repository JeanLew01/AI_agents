#!/usr/bin/env python3
"""Set title/notes in plan.json and title/review/navigation in bundle.json (idempotent)."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/ouyang2026symplectic-paper"
D = W / "documents/s001-ouyang2026symplectic"
TITLE = "Symplectic Inductive Bias for Data-Driven Target Reachability in Hamiltonian Systems"

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
plan["notes"] = [
    "Source version: arXiv:2604.17213v1 [math.OC], 19 Apr 2026 (10 pages, IEEE two-column conference format); authors Zhuo Ouyang, Jixian Liu and Enrique Mallada. This package was made from the arXiv v1 PDF; it is a preprint and no proceedings version was used.",
    "Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (CDC2026_sample.tex), with the authors' private macros expanded to standard LaTeX and the spacing-only commands dropped, and every formula was checked against the PDF pages (230 dpi column crops, 330 dpi crops for Theorems 2-4, Assumption 8, displays (8), (10), (11), the Step 6 bound and the two example systems). The TeX source and the PDF agree; no formula is kept as an image only.",
    "Printed equation numbers are (1)-(14) and are given as `\\tag{n}`: (1) Hamiltonian system, (2) bound C_f on the vector field, (3) average decrease rate, (4) best achievable rate, (5)-(7) proof of Theorem 2, (8)-(11) proof of Theorem 3, (12)-(14) proof of Theorem 4. All other displays are unnumbered in the paper, including the three conditions of Theorem 2, the radius and the sample-complexity bound of Theorem 3 and the bound of Theorem 4. Where a number is printed on one line of a multi-line display, that line is a separate display block carrying the tag: (8) and (11) are on the second line of two-line displays, (10) on the middle line of a three-line display.",
    "Theorem-like statements keep the printed numbering: Definitions 1-8, Assumptions 1-8, Remarks 1-6, Problem 1, Proposition 1, Lemma 1, Theorems 1-4. The PDF prints each label with the kind and number in bold ('Theorem 2'), the name in upright parentheses and a bold period; here the whole label is bold, e.g. '**Theorem 2 (Target Reachability).**'. Statement bodies are printed in italics, which is not reproduced; each statement ends where its environment ends in the TeX source (recorded page by page in the external review notes). In particular Theorem 2 runs from 'Consider system (1) under Assumptions 1–5' through the three numbered conditions to the conclusion display, Theorem 3 from 'Consider system (1) satisfying ...' through items 1) Reachability and 2) Sample complexity to the bound on N, and Theorem 4 ends with the display of the bound on T_max. 'Proof.' is printed in italics and written in bold; the end-of-proof box is written as a square symbol.",
    "Algorithm 1 (Assignment-Set Construction) is given as an image crop (assets/figure/algorithm-1.jpg) followed by a transcription with the printed line numbers 1-20, one paragraph per printed line and two em-spaces per nesting level. Figures 1-3 are image crops with verbatim captions (printed prefix 'Fig. n:'); the bar heights and error bars of Figures 2 and 3 are not transcribed, and their printed sub-captions '(a) Success rate' and '(b) Average reach time' are inside the crops and repeated as text. The paper has no tables and no appendix.",
    "Placement: Figure 1 is printed at the top of the right column of PDF page 8, in the middle of a sentence of Section III-D; here it follows the paragraph that refers to it, and Algorithm 1 follows it. The two unnumbered first-page footnotes (affiliations and e-mail addresses; funding) are placed directly after the author line. The subsubsections of Section IV are printed as run-in italic headings '1) Spring-Mass:' and '2) Single Pendulum:' and are written as level-3 headings. The only omitted region is the vertical arXiv stamp on page 1.",
    "The text and formulas are kept as printed. The following are in the source and are not conversion errors: 'Assumptions 4–Assumption 7' in Theorem 3; the repeated clause 'choose an optimal control ..., choose an optimal control ...' in Step 1 of the proof of Theorem 3; x_i instead of x in the first inline fraction of Step 2 and the star placed after the argument, T_epsilon(x)^star, in the display of Step 2; the lower rate printed with the underline under v and its subscript almost everywhere but under v only in Step 1 and in the last line of the Step 6 display; a plain italic B_r(x) under the max signs of display (10) and an asterisk instead of a five-pointed star as the superscript of H_+ in the sentence just after it; the symbol eta in Step 6 ('has length at least eta'), which is not defined; a calligraphic R in the product set of Definition 6; the empty set printed with two different glyphs (Assumption 3 and condition 3 of Theorem 2); a ceiling in the execution count (N with a subscript asterisk) of the proof of Theorem 2 but floors in the proof of Theorem 4; index sets written 'i=0,...N' and 'i=0,...,N'; demonstration durations called tau_j in Section II-D and T_j in Section III-D; the set S_tgt^delta, whose delta is not defined; items 1) and 2) of Assumption 8 without final periods; the e-mail address 'jliu376@jh.edu'; and wording such as 'a novel class control policies', 'the optimal hitting time maximized (4)', 'we can chose', 'Fig 1' and 'Fig 3a' without a period.",
    "In the reference list, page and article numbers that the PDF prints with a thin space as thousands separator are written with an ordinary space ('16 989–17 002', '101 649', '111 671'); lower-case words such as 'lti', 'deepc', 'gpu-based', 'lyapunov' and 'axiom a' are as printed.",
]
plan.pop("reading_order", None)
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
for n in plan["notes"]:
    assert "$" not in n, n[:60]

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 10 PDF pages (arXiv:2604.17213v1) were compared item by item with a 170 dpi render of page 1 and 230 dpi crops of both columns of pages 2-10, "
    "with 300-330 dpi crops of the first-page footnotes, Theorems 2, 3 and 4, Assumption 8, displays (8), (10), (11), the Step 6 bound, the labelled-arrow sentence on page 8 "
    "and the two example systems on page 9, and with the authors' TeX source (CDC2026_sample.tex). Two-column reading order was repaired on pages 3, 7, 8 and 10 and paragraphs running across "
    "columns or pages were merged or joined (pages 1-2, 2-3, 6-7, 8-9). All inline and display mathematics was rewritten in LaTeX from the TeX source with private macros expanded; "
    "all extractor 'formula' images were replaced by display blocks, with \\tag for the fourteen printed equation numbers (1)-(14). "
    "Definitions 1-8, Assumptions 1-8, Remarks 1-6, Problem 1, Proposition 1, Lemma 1 and Theorems 1-4 carry their printed labels in bold; statement ends were taken from the TeX environments. "
    "Algorithm 1 is an image crop plus a line-by-line transcription; Figures 1-3 are image crops (edges checked on wider renders) with verbatim captions. "
    "The 29 references were each compared with the page image; the bibliography exists only in the PDF (biblatex, no .bbl in the source bundle). "
    "The only omitted region is the vertical arXiv stamp on page 1. Authors' typos and inconsistencies are kept and listed in the page review notes and in the conversion notes. "
    "Review was done by one agent; no independent second verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "Abstract; the author line, affiliations, e-mail addresses and funding note are just above it"},
    {"file": P, "heading": "I. Introduction", "purpose": "Motivation (inductive bias, sample complexity of linear vs nonlinear data-driven control), chain policies and recurrence, outline of the paper, Notation paragraph (norm, ball, diameter, closure, boundary, interior, distance to a set, ceiling/floor)"},
    {"file": P, "heading": "II. Preliminaries and Problem Formulations", "purpose": "Section opener only; content is in subsections A-D"},
    {"file": P, "heading": "A. Hamiltonian System", "purpose": "Section II-A: Definition 1 with system (1), Assumption 1 (bounded gradient, L_H), Assumption 2 (Lipschitz dynamics, L), Remark 1 with bound (2) (C_f), Definition 2 (energy layer)"},
    {"file": P, "heading": "B. Target Reachability Problem", "purpose": "Section II-B: admissible control signals, flow notation, sets S_0 and S_tgt, Problem 1"},
    {"file": P, "heading": "C. Recurrence on Energy Layers", "purpose": "Section II-C: Definition 3 (invariant measure), Definition 4 (ergodic measure), Theorem 1 (ergodic decomposition), supports K_alpha^E, Proposition 1 (density of typical trajectories)"},
    {"file": P, "heading": "D. Chain Policies", "purpose": "Section II-D: demonstrations, Definition 5 (control alphabet), Definition 6 (assignment set, Supp), index map and selection rule, Definition 7 (nonparametric chain policy), Remark 2 (execution)"},
    {"file": P, "heading": "III. Reachability in Hamiltonian Systems", "purpose": "Section opener: overview of the two ingredients (energy decrease and recurrence)"},
    {"file": P, "heading": "A. Target Reachability via Chain Policies", "purpose": "Section III-A: H_min/H_max, Assumption 3, Remark 3, Definition 8 (energy distance Delta H), sets H_tgt and H_tgt^epsilon, Assumption 4, hitting time and rates (3)-(4), Assumption 5, Theorem 2 with its three conditions, proof (Steps 1-3, (5)-(7)), Remark 4"},
    {"file": P, "heading": "B. Existence of the Chain Policy", "purpose": "Section III-B: Lemma 1 with proof, Assumption 6 (ergodic layers), Assumption 7 (strong convexity, mu_H), Remarks 5-6, Theorem 3 (radius r_i and sample-complexity bound on N), proof Steps 1-6 with (8)-(11)"},
    {"file": P, "heading": "C. Finite Time Reachability", "purpose": "Section III-C: Assumption 8 (return time T_1, reaching time T_2), Theorem 4 (bound on T_max), proof with (12)-(14)"},
    {"file": P, "heading": "D. From Expert Demonstrations to NCPs", "purpose": "Section III-D: construction of the assignment set from demonstrations, certified radius r_i(t), Figure 1, Algorithm 1 (image and transcription)"},
    {"file": P, "heading": "IV. Numerical Simulation", "purpose": "Experimental setup: baseline (behavior cloning) and its hyperparameters, expert generation, test protocol, horizons, hardware"},
    {"file": P, "heading": "1) Spring-Mass", "purpose": "Section IV: spring-mass dynamics and parameters, Figure 2, reported success rates and reach times"},
    {"file": P, "heading": "2) Single Pendulum", "purpose": "Section IV: pendulum dynamics and parameters, Figure 3, reported success rates and reach times"},
    {"file": P, "heading": "V. Conclusions and Future Work", "purpose": "Summary and directions left open"},
    {"file": P, "heading": "References", "purpose": "Bibliography [1]-[29]"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, list of printed equation numbers, placement of floats and footnotes, source slips kept as printed (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated")
