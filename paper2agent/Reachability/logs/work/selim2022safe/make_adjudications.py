#!/usr/bin/env python3
"""Write adjudications.json for selim2022safe from the current review queue. Reasons are keyed by (page, check); the
script refuses to run if the queue holds a diagnostic without a written reason or if the diagnostic payload differs
from what was reviewed (EXPECT_* below)."""
import json
from pathlib import Path

R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/selim2022safe-paper"
D = W / "documents/s001-selim2022safe"
ML, ND, IP = "missing_lines", "number_differences", "independent_parser_number_differences"
WORDS = (" Scripted checks: every prose word (3 or more letters) of each listed line occurs in order in the built page text "
         "(linecheck.py), the per-page word multiset against pdftotext shows no lost prose word (wordcheck.py), and the "
         "per-page counts of relation, operator, accent and Greek symbols in the PDF text layer equal those of the LaTeX "
         "(symcheck.py, 0 differing counters).")

REASONS = {
 (2, ML): "All 13 lines contain inline mathematics or special glyphs now written in LaTeX or Unicode: the epsilon of "
          "'$\\epsilon$-greedy', 'naïvely' (PDF text 'na¨ıvely'), 'A$^{\\ast}$' (PDF 'A∗'), and the notation paragraph "
          "of Section II-A ($\\mathbb{R}^n$, $\\mathbb{N}$, $n{:}m$, $(\\mathbf{A})_{i,j}$, $(\\mathbf{A})_{:,j}$, "
          "$(\\mathbf{a})_i$, $\\mathbf{1}_{n\\times m}$, the shorthand $\\mathbf{A}-\\mathbf{x}$, diag, Minkowski sum, "
          "Cartesian product, $\\mathbf{c}\\in\\mathbb{R}^n$). Each was compared with a 300 dpi crop of the paragraph and "
          "with the authors' TeX source." + WORDS,
 (2, ND): "One glyph-run artefact, read on the 300 dpi crop: the PDF text '11×m' is the bold matrix of ones "
          "$\\mathbf{1}$ followed by its subscript $1\\times m$; the parser reads '11', the LaTeX "
          "'\\mathbf{1}_{1\\times m}' gives two tokens '1'. Hence missing '11' x1 and extra '1' x2. No other number differs.",
 (2, IP): "Same as the first parser: PDF text '11×m' (bold one with subscript $1\\times m$, checked on the 300 dpi "
          "crop) is one token '11' for the parser and two tokens '1' in the LaTeX. No other number differs.",
 (3, ML): "All 50 lines contain mathematics now written in LaTeX from the authors' TeX source: the constrained-zonotope "
          "definition with display (1), the zonotope paragraph (linear map, Minkowski sum, interval zonotope with "
          "center $\\tfrac12(\\underline{\\mathbf{l}}+\\overline{\\mathbf{l}})$), Section II-B with display (2), the "
          "Lipschitz sentence, Assumptions 1 and 2, $X_{\\text{obs}}$, Definition 1 with display (3), and Section II-D "
          "($\\hat{\\mathbf{x}}_k$, $\\rho$, $\\mathbf{p}_k$, $\\pi_\\theta$, $R_j\\cap X_{\\text{obs}}=\\emptyset$); also "
          "'naïvely'. Every formula was compared symbol by symbol with five 300 dpi crops of the page and with a "
          "pdflatex rendering of the transcription." + WORDS,
 (3, ND): "Explained item by item on the 300 dpi crops. Missing '−1' x3 with extra '-1' x3: Unicode minus in the PDF "
          "versus ASCII '-' in LaTeX for '$-Z=-1Z$', '$\\{0,\\dots,k-1\\}$' in Definition 1 and '$j=0,\\cdots,k-1$' in "
          "(3). Missing '7' x2: the PDF text layer encodes the two 'maps to' arrows ($\\rho:(\\hat{\\mathbf{x}}_k,"
          "\\mathbf{u}_k)\\mapsto r_k$ and $\\pi_\\theta:\\hat{\\mathbf{x}}_k\\mapsto\\mathbf{u}_k$) as '7→'; there is no "
          "digit 7 on the page at these places.",
 (3, IP): "Second parser, same three places: it splits two of the three Unicode '−1' into '−' and '1' (missing '1' x2 "
          "and '−1' x1) while the LaTeX has ASCII '-1' x3 ('$-1Z$', 'k-1' in Definition 1, 'k-1' in (3)); read on the "
          "300 dpi crops. This parser does not report the '7→' artefact. No real number differs.",
 (4, ML): "All 28 lines contain mathematics now written in LaTeX from the TeX source: $\\mathbf{p}_k$, "
          "$k^{\\text{th}}$, $\\mathbf{p}_{k-1}$, $\\pi_\\theta$, the plan $(\\mathbf{u}_j)_{j=k}^{n_{\\text{plan}}}$, "
          "$\\hat{R}_j\\supseteq R_j$, the trajectory data sentence ($t_i$, $t_{\\text{total}}=\\sum_i^q t_i$, the two "
          "data sequences), fragments of displays (4a)-(4c), $\\mathbf{X}_-$, $\\mathbf{X}_+$, the covering-radius "
          "sentence, $L^\\star$, $\\delta$, $(L^\\star)_i$, $(\\delta)_i$, $Z_\\epsilon$. Compared with 300 dpi crops of "
          "the right column and the lower left column. Lines inside the Algorithm 1 and Algorithm 2 crops are excluded "
          "by the tool; the transcriptions were checked line by line against 300/330 dpi crops of the boxes." + WORDS,
 (4, ND): "Explained item by item. Missing '−1' x6 with extra '-1' x6: Unicode minus in the PDF versus ASCII '-' for "
          "$\\mathbf{p}_{k-1}$, the upper index $t_i-1$ of the input sequence, and $t_1-1$, $t_q-1$ in each of (4a) and "
          "(4c). All other extra tokens are exactly the number tokens of the two algorithm transcriptions, whose PDF "
          "text lies inside the excluded image crops: Algorithm 1 gives the '1' of its title, its line numbers 1-16, '2' and '3' of "
          "'Alg. 2' / 'Alg. 3', subscript digits ($\\hat{\\mathbf{x}}_1$, $k=1$, $\\mathbf{p}_0$, bold zero) and '+1' x2 "
          "($\\hat{\\mathbf{x}}_{k+1}$); Algorithm 2 gives the '2' and '[42]' of its title, its line numbers 1-7, '(3)', and the "
          "digits of line 1 ($(\\mathbf{L}^\\star)_1(\\delta)_1/2$, '/2'), of $\\hat{R}_0$, bold ones and zeros, and "
          "'+1' of $\\hat{R}_{j+1}$. A scripted subtraction of the transcription tokens from the tool's list leaves no "
          "residual (numcheck.py).",
 (4, IP): "Same payload as the first parser: '−1' x6 (Unicode minus) versus ASCII '-1' x6 in $\\mathbf{p}_{k-1}$, "
          "$t_i-1$, and $t_1-1$, $t_q-1$ of (4a) and (4c); all other extra tokens are the number tokens of the "
          "Algorithm 1 and Algorithm 2 transcriptions (line numbers, 'Alg. 2', 'Alg. 3', '[42]', '(3)', subscript "
          "digits, '+1' x3), whose PDF text is inside the excluded crops. Scripted subtraction leaves no residual.",
 (5, ML): "All 33 lines contain mathematics now written in LaTeX from the TeX source: $\\mathbf{u}_0$ in the Figure 2 "
          "caption, $\\pi_\\theta$, the plan $\\mathbf{p}$, the two constrained zonotopes and their intersection with "
          "display (5), the linear program (6) and the sentence after it, the gradient paragraph ($\\hat{R}_k$, "
          "$\\hat{\\mathbf{c}}_k$, $(\\mathbf{z}^\\star,v^\\star)$, $\\nabla_{\\mathbf{u}_k}v^\\star$), displays (7), "
          "(8a), (8b), the projection formula, and Theorem 1 and its proof ($\\mathbf{p}_k$, $k\\ge 0$, "
          "$\\mathbf{u}_{\\text{brk}}$, $k\\in\\mathbb{N}$). Each display was compared symbol by symbol with 300-330 dpi "
          "crops and with a pdflatex rendering. The one line not matched by the script, 'feasible controls: "
          "projUk(uk) = arg minv∈Uk', is the projection formula, read on the 330 dpi crop. Lines inside the Algorithm 3 "
          "and Figure 2 crops are excluded by the tool; the Algorithm 3 transcription was checked against a 330 dpi "
          "crop." + WORDS,
 (5, ND): "Explained item by item. Missing '−1' x9 with extra '-1' x9: Unicode minus in the PDF versus ASCII '-' for "
          "$\\mathbf{u}_{k-1}$ in the text, $\\hat{\\mathbf{c}}_{k-1}$, the upper limit 'j=k-1' and $\\hat{\\mathbf{c}}_{j-1}$ in (7), two 'k-1' in (8a), two in (8b) "
          "and one in 'where $\\mathbf{M}_{k-1}$ is computed'; counted 9 on the crops (text 1, (7) 3, (8a) 2, (8b) 2, 'where' 1). All "
          "other extra tokens are exactly the number tokens of the Algorithm 3 transcription, whose PDF text is inside "
          "the excluded crop: the '3' of its title, line numbers 1-14, '2' of 'Alg. 2', '(6)', '(7)', '1' of '$v^\\star\\le 1$'. Scripted "
          "subtraction leaves no residual (numcheck.py).",
 (5, IP): "Same payload as the first parser: '−1' x9 (Unicode minus; subscripts k-1 and j-1 in the text, (7), (8a), "
          "(8b)) versus ASCII '-1' x9; all other extra tokens are the number tokens of the Algorithm 3 transcription "
          "(line numbers 1-14, 'Alg. 2', '(6)', '(7)', '$v^\\star\\le 1$'), whose PDF text is inside the excluded crop.",
 (6, ML): "All 15 lines contain mathematics now written in LaTeX: $\\hat{R}_j\\cap X_{\\text{obs}}$, "
          "$n_{\\text{plan}}$, $\\mathbf{u}_{\\text{brk}}$ and $j\\ge k+n_{\\text{plan}}$ at the end of the proof, "
          "$X_{\\text{goal}}$, $X_{\\text{obs}}$, the degree values $180^\\circ$, $50^\\circ$, $360^\\circ$, "
          "$n_{\\text{brk}}=6$, $n_{\\text{plan}}=8$, $n_{\\text{brk}}=10$, $n_{\\text{plan}}=11$, the point-robot state, "
          "the safe set $X_{\\text{safe}}$, the norm condition and the reward fraction. Compared with 300-330 dpi crops "
          "of the three regions; the small inline fraction was taken from the TeX source and confirmed on the 330 dpi "
          "crop." + WORDS,
 (6, ND): "Missing '−0.5' with extra '-0.5': Unicode minus in the PDF versus ASCII '-' in '$[-0.5, 0.5]$ rad/s' (read on "
          "the 300 dpi crop). Extra '3' x1: 'Turtlebot3' in the sub-caption '(a) Turtlebot3 Environment', which is "
          "printed inside the Figure 3 crop (PDF text excluded by the tool) and repeated in the caption item for "
          "searchability.",
 (6, IP): "Same as the first parser: Unicode '−0.5' versus ASCII '-0.5' in the angular-velocity interval; extra '3' is "
          "'Turtlebot3' of the Figure 3 sub-caption (a), printed inside the figure crop and repeated in the caption item.",
 (7, ML): "The single line 'of data for BRSL determines the computation time of Mj' ends with the inline symbol "
          "$\\mathbf{M}_j$, now written in LaTeX; the sentence was compared with the 170 dpi page render and the TeX "
          "source and is complete." + WORDS,
 (7, ND): "Extra '3' x1: 'Turtlebot3' in the sub-caption '(a) Turtlebot3 Reward', which is printed inside the Figure 4 "
          "crop (PDF text excluded by the tool) and repeated in the caption item for searchability. All table numbers "
          "of Tables I and II match the PDF text layer (no other difference reported) and were read on a 330 dpi crop.",
 (7, IP): "Same as the first parser: extra '3' is 'Turtlebot3' of the Figure 4 sub-caption (a), printed inside the "
          "figure crop and repeated in the caption item. No table number differs.",
}
EXPECT_ML = {2: 13, 3: 50, 4: 28, 5: 33, 6: 15, 7: 1}
EXPECT_ND = {
    2: ({"11": 1}, {"1": 2}),
    3: ({"−1": 3, "7": 2}, {"-1": 3}),
    6: ({"−0.5": 1}, {"3": 1, "-0.5": 1}),
    7: ({}, {"3": 1}),
}
v = json.loads((D / "verification.json").read_text(encoding="utf-8"))
for p in v["pages"]:
    n = p["page"]
    assert len(p["missing_lines"]) == EXPECT_ML.get(n, 0), ("missing-line count changed", n, len(p["missing_lines"]))
    nd = p["number_differences"]
    if n in EXPECT_ND:
        assert (nd["missing"], nd["extra"]) == EXPECT_ND[n], ("number payload changed", n, nd)
    if n in (4, 5):
        assert set(nd["missing"]) == {"−1"} and nd["extra"]["-1"] == nd["missing"]["−1"], ("minus pairing", n, nd)
    if n in (1, 8):
        assert not nd["missing"] and not nd["extra"]
q = json.loads((W / "review-aid/review-queue.json").read_text(encoding="utf-8"))
entries = []
for s in q["sources"]:
    for it in s["items"]:
        if it.get("kind") != "unresolved_diagnostic":
            continue
        e = dict(it["adjudication_entry"])
        e["reason"] = REASONS[(e["page"], e["check"])]
        entries.append(e)
assert len(entries) == len(REASONS), (len(entries), len(REASONS))
(D / "adjudications.json").write_text(json.dumps({"schema_version": 1, "entries": entries}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("adjudications written:", len(entries))
