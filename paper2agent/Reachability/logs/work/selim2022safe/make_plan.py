#!/usr/bin/env python3
"""Set title/notes in plan.json and title/review/navigation in bundle.json for selim2022safe (idempotent)."""
import json
from pathlib import Path

R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/selim2022safe-paper"
D = W / "documents/s001-selim2022safe"
TITLE = "Safe Reinforcement Learning Using Black-Box Reachability Analysis"

plan = json.loads((D / "plan.json").read_text(encoding="utf-8"))
plan["title"] = TITLE
plan["notes"] = [
    "Source version: arXiv:2204.07417v2 [cs.RO], 21 Nov 2022 (8 pages, IEEE two-column; the running header reads 'IEEE Robotics and Automation Letters. Preprint Version. Accepted June, 2022'). Authors: M. Selim, A. Alanwar, S. Kousik, G. Gao, M. Pavone, K. H. Johansson. The paper was published in IEEE Robotics and Automation Letters 7(4), 2022. This package was made from the arXiv v2 preprint PDF, not from the published journal version; page furniture (running headers, page numbers, the vertical arXiv stamp) is omitted.",
    "Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (`main.tex`, the files under `Sections/`, `commands.tex`), with the authors' private macros expanded to standard LaTeX (bold symbols for vectors and matrices, calligraphic Z for zonotopes and constrained zonotopes, roman subscripts such as obs, brk, plan, safe, total), and every formula was checked against the PDF pages on 300 dpi crops. The TeX source and the PDF agree; no formula is kept as an image only. Numbers that the authors typeset in math mode in running text (for example 500, 0.5, 0.01) are written as plain text.",
    "Printed equation numbers are (1), (2), (3), (4a)-(4c), (5), (6), (7), (8a)-(8b); each is written with `\\tag{n}`. Equation (3) is a two-line display with one number. The sub-numbered displays (4a)-(4c) and (8a)-(8b) are written as one display block per printed number.",
    "Algorithms 1-3 are given as image crops (assets/figure/algorithm-1.jpg, algorithm-2.jpg, algorithm-3.jpg), each followed by a text transcription with the printed line numbers; nesting is shown by indentation. In the printed Algorithm 2, line 1 contains both the assignment of the Lipschitz zonotope and the loop header `for j = k:(k + n_plan) do`, so the loop header has no line number of its own and the least-squares model `M_j` is on line 2; the transcription keeps this, and the text's references ('Line 1 of Algorithm 2', 'Algorithm 2, Line 2') agree with it. In the PDF the algorithm boxes and Figures 1-4 are floats at the tops of columns or pages and interrupt sentences; here each float is placed after the paragraph that introduces it: Figure 1 after the first paragraph of Section I, Algorithm 1 after the paragraph 'BRSL is summarized in Algorithm 1 ...', Algorithm 2 after the first paragraph of Section III-A, Algorithm 3 and Figure 2 after the paragraph 'We adjust unsafe actions using Algorithm 3 ...', Figure 3 after the first paragraph of Section IV, and Figure 4, Table I and Table II after the 'Results and Discussion' paragraph. Sub-captions printed inside Figures 3 and 4 are repeated in the caption text.",
    "Tables I and II are transcribed as cell tables (assets/table/table-1.csv, table-2.csv). Their printed two-level headers (robot or environment above method) are combined into single column names such as 'Turtlebot BRSL'. Bold face, which the paper uses to mark best values, cannot be stored in the cells; the bold cells are listed in a note after each table that is marked as added in conversion.",
    "Theorem-like blocks are printed with a bold label and an italic body; the italics are not reproduced. Their ends follow the authors' TeX environments: Assumption 1 ends with the equality of the stopped state, `x_{k+1} = x_k`; Assumption 2 ends with '... generators.'; Definition 1 consists of its sentence and display (3); Theorem 1 ends with '... at all times `k >= 0`.'; the proof ends with the box symbol. The unnumbered first-page footnotes (manuscript dates, editor, funding, affiliations, DOI line) are placed after the author line, each starting with 'Footnote:'.",
    "The text and formulas are kept as printed. The following are in the source and are not conversion errors: the dynamics are declared as `f: X x U x W -> X` but used with two arguments in (2); the Lipschitz condition in Section II-B has only the state difference on its right-hand side and a norm without subscript; Definition 1 writes the initial set with an element sign (`X_0 in R^n`); the plan is written with upper index `n_plan` in the text and in the Input and return lines of Algorithm 3, but with `k + n_plan` in Algorithms 1 and 2 and in line 5 of Algorithm 3; Algorithm 2 names its input 'initial reachable set' with index 0 although its loop starts at `j = k`, does not define the linearization point (the starred state `x_j` with superscript star), and reuses `j` as the column index of the minimum on line 3; Algorithm 1 line 7 uses `x_k` without a hat; in Algorithm 3 the loop of line 3 runs to `k + n_plan + n_brk`, line 11 tests whether `x_n` is stopped, and line 8 is printed with a plus sign before the gradient step although the text speaks of gradient descent; in (8b) the gradient subscript `u_{k-1}` is not bold; the product in (7) is printed with `j =` in both limits; 'nonempty iff `v <= 1`' is printed without the star after (6); the Figure 4 legends include SECAS, which the caption does not name; wording slips such as 'such loiter circles', 'at safe state', 'manuever', 'as in fig 2', 'conservativeness is by placing', 'a low-dimensional parameterized plans'; '[3] J. Garcıa' without accent in the bibliography.",
    "Not printed in the PDF, reported here only as background from the authors' TeX source: a commented-out sentence in `Sections/5_solu.tex` states that the least-squares model of Algorithm 2 is computed at a linearization point (a starred state and a starred action with index `j`) whose state component is the center of the current reachable set zonotope, following references [40] and [42]; and the source tree contains an appendix file (`Sections/A_implementation_details.tex`) whose inclusion is commented out, so this version of the paper has no appendix and no supplementary material.",
]
assert not any("$" in n for n in plan["notes"])
plan.pop("reading_order", None)
(D / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

b = json.loads((W / "bundle.json").read_text(encoding="utf-8"))
b["title"] = TITLE
src = b["sources"][0]
src["title"] = TITLE
src["reviewed"] = True
src["review_notes"] = (
    "All 8 PDF pages (arXiv:2204.07417v2) were compared item by item with 170 dpi page renders, with 300-330 dpi crops of "
    "every mathematical region, algorithm box, figure and table, and with the authors' TeX source and .bbl. Two-column "
    "reading order was repaired: every page from 1 to 7 has a float (Figure 1, Algorithms 1-3, Figures 2-4, Tables I-II) "
    "that interrupts a sentence; floats were moved next to the paragraph that introduces them and the six sentences split "
    "by page breaks were rejoined. All inline and display mathematics was rewritten in LaTeX from the TeX source with "
    "private macros expanded; the 13 extractor 'formula' images were replaced by 8 display items (11 printed equation "
    "numbers) and by the transcriptions of Algorithms 2 and 3. Assumptions 1-2, Definition 1, Theorem 1 and its proof carry "
    "their printed labels in bold. Algorithms 1-3 are image crops plus line-numbered transcriptions; Figures 1-4 are image "
    "crops (edges checked on renders) with verbatim captions; Tables I-II are cell tables read from a 330 dpi crop, checked "
    "against the PDF text layer and the TeX source, with the bold cells listed in notes. The 55 references were generated "
    "from the authors' .bbl and compared entry by entry with the PDF text layer and the page images. Omitted regions: "
    "running header and page number on each page (16 regions) and the vertical arXiv stamp on page 1. Authors' typos and "
    "inconsistencies are kept and listed in the page review notes and in the conversion notes. Review was done by one "
    "agent; no independent second verifier was used."
)
P = "references/paper.md"
b["navigation"] = [
    {"file": P, "heading": "Abstract", "purpose": "One-paragraph statement of the BRSL method and its three components; index terms"},
    {"file": P, "heading": "I. Introduction", "purpose": "Motivation; Figure 1 (overview of the BRSL loop)"},
    {"file": P, "heading": "A. Related Work", "purpose": "Section I-A: objective-based and exploration-based safe RL, control-theoretic safety layers, safe navigation, references [2]-[38]"},
    {"file": P, "heading": "B. Proposed Method and Contributions", "purpose": "Section I-B: what BRSL does, stated limitations (Lipschitz-constant approximation, discrete time, braking, perfect perception), the two contributions, code link"},
    {"file": P, "heading": "II. Preliminaries and Problem Formulation", "purpose": "One-sentence section overview"},
    {"file": P, "heading": "A. Notation and Set Representations", "purpose": "Section II-A: index and matrix notation, Minkowski sum, constrained zonotope (1), zonotope, linear map and Minkowski sum of zonotopes, interval as zonotope"},
    {"file": P, "heading": "B. Robot and Environment", "purpose": "Section II-B: black-box dynamics (2), Lipschitz assumption, Assumption 1 (braking failsafe), Assumption 2 (noise zonotope), obstacle and sensing assumptions"},
    {"file": P, "heading": "C. Reachable Sets", "purpose": "Section II-C: Definition 1 with the reachable set (3)"},
    {"file": P, "heading": "D. Safe RL Problem Formulation", "purpose": "Section II-D: RL state, reward, plan, policy, the safety requirement on reachable sets"},
    {"file": P, "heading": "III. Black-box Reachability-based Safety Layer", "purpose": "Overview of the three components; Algorithm 1 (safe RL loop with BRSL) as image and transcription, with its walk-through"},
    {"file": P, "heading": "A. Data-Driven Reachability Analysis", "purpose": "Section III-A: Algorithm 2 (data-driven zonotope reachability), offline data matrices (4a)-(4c), Lipschitz constant and covering radius, per-dimension Lipschitz zonotope"},
    {"file": P, "heading": "B. Adjusting Unsafe Actions", "purpose": "Section III-B: Algorithm 3 (projected gradient adjustment), Figure 2, constrained-zonotope intersection (5), collision-check linear program (6), gradient chain rule (7), (8a)-(8b), projection"},
    {"file": P, "heading": "C. Analyzing Safety", "purpose": "Section III-C: Theorem 1 (safety guarantee) and its proof, remark on the role of the offline data"},
    {"file": P, "heading": "IV. Evaluation", "purpose": "Setup (TD3, 500 offline data steps, ensemble model), goal-based and path-following environments with parameters, results discussion; Figures 3-4, Tables I-II"},
    {"file": P, "heading": "V. Conclusion", "purpose": "Summary and stated future work"},
    {"file": P, "heading": "References", "purpose": "Bibliography [1]-[55]"},
    {"file": P, "heading": "Conversion notes", "purpose": "Source version, how the mathematics was transcribed, float placement, table and algorithm conventions, source slips kept as printed (at the end of the file)"},
]
(W / "bundle.json").write_text(json.dumps(b, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("plan.json and bundle.json updated")
