#!/usr/bin/env python3
"""Write adjudications.json from the current review queue. Reasons are keyed by (page, check);
the script refuses to run if the queue contains a diagnostic without a written reason, or if the
diagnostic payload no longer matches what was reviewed (EXPECT_* below)."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/sartipizadeh2019voronoi-paper"
D = W / "documents/s001-sartipizadeh2019voronoi"
ML, ND, IP = "missing_lines", "number_differences", "independent_parser_number_differences"
WORDS = (" Every listed line was read; each contains mathematics or starts/ends inside a formula. A per-page word-multiset "
         "comparison against pdftotext (wordcheck.py) found no prose word of the page missing from the text, a symbol-count "
         "comparison (symcheck.py: relations, hats, epsilons, asterisks, Greek letters) agrees with the PDF text layer, and the "
         "LaTeX compiles and was compared with the page crops.")
REASONS = {
 (2, ML): "All 10 lines contain inline math now written in LaTeX from the authors' TeX source: the notation paragraph ($\\mathbb{R}$, $\\mathbb{N}$, $\\mathbb{R}^{n}$, $\\mathbb{N}_{[a,b]}$, $x^{\\top}$, $\\mathbf{1}$), the paragraph after (1) ($x_t\\in\\mathcal{X}=\\mathbb{R}^{n_x}$, $u_t\\in\\mathcal{U}\\subseteq\\mathbb{R}^{n_u}$, $w_t\\in\\mathcal{W}\\subseteq\\mathbb{R}^{n_x}$, $\\eta_w$), and the paragraph after (2) (the stacked vectors $X$, $U$, $W$, whose sub/superscript fragments 'N]⊤∈X N, U = [u⊤' are three of the lines, $x_k$, $\\mathbb{P}_X^{x_0,U}$, $\\mathbb{P}_W$, $(\\eta_w)^N$). Checked on the 150 dpi render of page 2." + WORDS,
 (2, ND): "Sign glyph only: the PDF has two subscripts 'N−1' with the Unicode minus (in $u_{N-1}^{\\top}$ and $w_{N-1}^{\\top}$); LaTeX writes them 'N-1' with ASCII '-'. Counted 2 on the page render and 2 in the text.",
 (2, IP): "Same as the first parser: the two subscripts 'N−1' of $u_{N-1}^{\\top}$ and $w_{N-1}^{\\top}$ (Unicode minus in the PDF, ASCII '-' in LaTeX). No other number differs.",
 (3, ML): "All 33 lines are mathematics or contain inline math now written in LaTeX from the TeX source: the definition of $r_{x_0}^{U}(\\mathcal{S},\\mathcal{T})$ and display (3), '$\\mathcal{R}=\\mathcal{S}^{N-1}\\times\\mathcal{T}$', displays (4) and (5) of Problem 1 and the definition of $z$, Remark 1 ($x_0\\not\\in\\mathcal{S}$), the sentence introducing $\\mathcal{S}$, $\\mathcal{T}$, $\\mathcal{R}$, displays (6a)-(6c), the dimension sentence ($l_\\mathcal{S}$, $L=(N-1)l_\\mathcal{S}+l_\\mathcal{T}$, $F\\in\\mathbb{R}^{L\\times n_x}$), display (7), the four lines of the MILP of Problem 2 and its closing sentence ($p_K^{\\ast}(x_0)$, $U_K^{\\ast}$, $M\\in\\mathbb{R}$, $W^{(i)}$, $\\mathcal{W}^N$). Each display was checked symbol by symbol on two 230 dpi crops and on a pdflatex rendering of the transcription." + WORDS,
 (3, ND): "Sign glyph only: four '−1' with the Unicode minus in the PDF ($\\mathbb{N}_{[0,N-1]}$ in (3), $\\mathcal{S}^{N-1}$, the upper limit of $\\prod_{t=1}^{N-1}$, and $(N-1)l_\\mathcal{S}$) are written with ASCII '-' in LaTeX. Counted 4 on the 230 dpi crops and 4 in the text.",
 (3, IP): "Same four 'N−1' occurrences as the first parser (Unicode minus versus ASCII '-'); pypdf extracts one of them with a space after the minus ('(N− 1)lS' in its raw text, for '$(N-1)l_\\mathcal{S}$'), so it reports '1' once and '−1' three times as missing against four '-1' in the text. Confirmed in the pypdf raw text and on the 230 dpi crop.",
 (4, ML): "All 21 lines contain inline or display math now written in LaTeX: three lines of the Figure 1 caption ($\\mathcal{R}$, $\\mathcal{W}_K$, $U$, $x_0$), the paragraph 'As observed in ...' ($z^{(i)}$, $FX^{(i)}\\leq h$, $X^{(j)}\\in\\mathcal{R}$, $FX^{(j)}>h$), the right part of limit (8), the definition of $Z$ and of $\\mathbb{P}_Z^{x_0,U}$, Question 1 (both probability statements, compared on the 230 dpi crop: '$p_K^\\ast(x_0)-p^{\\ast}(x_0)\\geq\\delta$' with '$\\leq\\beta$' and '$p^{\\ast}(x_0)\\geq p_K^\\ast(x_0)-\\delta$' with '$\\geq 1-\\beta$'), Question 2 ($\\hat{K}<K$, $\\hat{p}(x_0)\\leq p_K^{\\ast}(x_0)$) and the last paragraph ($\\delta$, $\\beta$)." + WORDS,
 (5, ML): "All 39 lines contain inline or display math now written in LaTeX from the TeX source: the Voronoi paragraph ($\\mathcal{C}$, $c^{(i)}\\in\\mathbb{R}^d$, $\\mathcal{V}(\\mathcal{C})$, $V^{(j)}$, $\\mathcal{P}$, $\\mathcal{V}_{\\mathcal{P}}(\\mathcal{C})$), display (9), the metric sentence and $\\vert V^{(j)}\\vert$, the clustering paragraph ($\\mathcal{X}^{K}$, $\\mathcal{X}^{\\hat{K}}$, $\\mathrm{WSS}(\\hat{K},\\mathcal{V}_{\\mathcal{P}}(\\mathcal{C}))$), displays (10) and (11), the paragraph after (11) ($\\mathcal{C}^\\ast$, $\\mathcal{O}(ndK\\hat{K})$), both items of Lemma 1, its proof line ($\\mathrm{WSS}$), and the first paragraph of Section 3 ($y^{(i)}$, $Y$, $\\mathbb{P}_Y^K$). Displays and Lemma 1 were checked on two 230 dpi crops and on a pdflatex rendering." + WORDS,
 (6, ML): "All 36 lines are fragments of Lemma 2 with (12), Theorem 1 with (13), the displays (14a)-(14c), (15), (16) and the final chain of the proof, the two inline set expressions with $\\overline{Z}$, and the surrounding proof sentences with inline math; all were rewritten in LaTeX from the TeX source and compared symbol by symbol with two 230 dpi crops and a pdflatex rendering. In particular the order printed in Theorem 1, '$p^\\ast(x_0)-p_K^{\\ast}(x_0)\\geq\\delta$', and the order '$p_K^{\\ast}(x_0)-p^\\ast(x_0)\\geq\\delta$' in (15), in the final chain and in the last sentence of the proof were each confirmed on the crop." + WORDS,
 (6, ND): "Sign glyph only: the exponent of $e^{-2K\\delta^2}$ is printed three times (in (12), at the end of the final chain of the proof, and in 'we require $e^{-2K\\delta^2}\\leq\\beta$') with the Unicode minus '−2'; LaTeX has '-2'. Counted 3 on the 230 dpi crops and 3 in the text. The leading minus of '$-\\ln(\\beta)$' is not followed by a digit and does not appear in the number check.",
 (6, IP): "Same as the first parser: three exponents '−2' of $e^{-2K\\delta^2}$ ((12), final chain, 'we require ...') with the Unicode minus in the PDF and ASCII '-' in LaTeX. No other number differs.",
 (7, ML): "All 33 lines contain inline or display math now written in LaTeX from the TeX source: the opening paragraph ($\\delta$, $\\beta$, $\\hat{K}$, $K$), the four lines of the MILP of Problem 3 and its explanatory text ($p_{\\hat{K}}^{\\ast}(x_0)$, $\\psi^{(j)}$, $\\phi:\\mathcal{W}^N\\rightarrow\\mathcal{X}^N$, display $\\phi(W):=G_wW$, $\\alpha^{(j)}$, $\\sum_{j=1}^{\\hat{K}}\\alpha^{(j)}=K$, $\\varepsilon^{(j)}$), the paragraph after Problem 3, the first paragraph of Section 4.1 ($\\mathcal{X}_K^{x_0,U}$), Lemma 3 with its display, and the closing sentence ($\\phi(W)$, $x_0$, $U$). Problem 3 and Lemma 3 were checked on two 230 dpi crops (hats, $\\varepsilon^{(j)}$, the weight $\\frac{1}{K}$) and on a pdflatex rendering." + WORDS,
 (8, ML): "All 40 lines contain inline or display math now written in LaTeX from the TeX source: one line of the Figure 2 caption ($\\hat{K}$), Lemma 4 with (17) and (18), its proof with (19), (20), (21) and the closing sentences, Remark 2, and Theorem 2. Many lines are detached sub/superscript fragments of $V_{\\Phi_K}^{(j)}(\\Psi_{\\hat{K}})$ ('ΦK(Ψ ˆ', 'K) ...'). Checked on two 230 dpi crops and on a pdflatex rendering, including the distinction between $\\varepsilon^{(j)}$ and $\\epsilon_{\\ell}^{(j)}$ (their counts on this page agree with the PDF text layer: 3 and 8) and the row index $\\ell$." + WORDS,
 (9, ML): "All 25 lines contain inline or display math now written in LaTeX from the TeX source: the Figure 3 caption ($V^{(j)}$, $X(\\psi^{(j)})$, $F_{\\ell}X^{(j)}\\leq h_{\\ell}-\\epsilon_{\\ell}^{(j)}$, $F_{\\ell}X\\leq h_{\\ell}$), the proof of Theorem 2, Remark 3, the sentence with $\\hat{K}$, the first paragraph of Section 4.2 ($U_{\\hat{K}}^{\\ast}$, $p_K^{\\ast}$, $\\mathcal{R}$, $\\mathcal{O}(K)$), Theorem 3 with (22) and the chain $p_{\\hat{K}}^{\\ast}\\leq\\hat{p}\\leq p_K^{\\ast}$, and part i) of its proof. Checked on a 220 dpi crop and on a pdflatex rendering. Text inside the Figure 3 crop is excluded by the tool and was checked on the crop." + WORDS,
 (10, ML): "All 20 lines contain inline math now written in LaTeX from the TeX source: ten lines of part ii) of the proof of Theorem 3 ($\\mathcal{J}$, $\\hat{z}^{(j)}$, $\\mathcal{C}^\\ast$, the two sums over $\\{i\\in\\mathbb{N}_{[1,K]}:W^{(i)}\\in V^{(j)}\\}$, $\\alpha^{(j)}$, $\\hat{p}$, $\\hat{p}_{\\hat{K}}^\\ast$; checked on a 240 dpi crop) and ten lines of the two paragraphs after Algorithm 1 ($\\mathcal{W}_K$, $(\\eta_w)^N$, $\\phi(\\mathcal{W}_K)$, $\\hat{K}$, $\\mathrm{WSS}$, $\\varepsilon^{(1)},\\cdots,\\varepsilon^{(\\hat{K})}$, $\\hat{p}$; the first of them starts with the line-wrap fragment 'lem.' of 'problem'). Lines inside the Algorithm 1 crop are excluded by the tool and were compared with the 220 dpi crop separately." + WORDS,
 (10, ND): "No number is missing. All extra numbers are those of the Algorithm 1 transcription, whose PDF text lies inside the image crop and is excluded by the tool; each was read on the 220 dpi crop: '1' x8 ('Algorithm 1', system '(1)', offline step 1, $V_{\\Phi_K}^{(1)}$, $\\alpha^{(1)}$, two '$\\mathbb{N}_{[1,\\hat{K}]}$', online step 1), '0' x3 (three '$x_0$'), '2' x2 (offline and online step 2), '3' x2 (step 3, 'Problem 3'), '4' x2 (step 4, 'Lemma 4'), '5', '6', '7' (steps), '9' ('from (9)'), '22' ('from (22)').",
 (10, IP): "Same payload as the first parser: no missing number; the extra numbers ('1' x8, '0' x3, '2' x2, '3' x2, '4' x2, '5', '6', '7', '9', '22') all belong to the Algorithm 1 transcription, whose PDF text is inside the excluded image crop; each was read on the 220 dpi crop.",
 (11, ML): "All 19 lines contain inline or display math now written in LaTeX from the TeX source: the two halves of (23), the paragraph after it ($x,y\\in\\mathbb{R}$, $m_d=300$, $\\mu$, $R_0$, $\\omega=\\sqrt{\\mu/R_0^3}$), the definition of $\\zeta$ and $u$, (24), the noise sentence with $10^{-4}\\times\\text{diag}(1,1,5\\times10^{-4},5\\times10^{-4})$, the set definitions (25) and (26), the line with $\\mathcal{U}=[-0.1,0.1]\\times[-0.1,0.1]$, and eight lines of the experiment paragraph ($\\mathcal{W}_N$, $\\mathrm{WSS}$, $\\hat{K}=20$, $WSS$, $\\mathcal{W}_K$, $k$-means, $\\hat{K}$). All numbers were read on a 230 dpi crop and the displays compared with a pdflatex rendering." + WORDS,
 (11, ND): "Formatting only; every value was read on the 230 dpi crop. Unicode minus in the PDF versus ASCII '-' in LaTeX: '−1' x3 ($m_d^{-1}$ twice in (23), '$-1\\leq\\zeta_2$' in (26)), '−4' x3 ($10^{-4}$ three times), '−0.1' x3 ('$-0.1\\leq\\zeta_2$' in (25) and twice in $\\mathcal{U}=[-0.1,0.1]\\times[-0.1,0.1]$), '−0.75' ('$x=y=-0.75$ km'). '−3' and '−2' versus '3' and '2': the PDF prints '−3ωx' and '−2ω ẏ' in (23) without a space after the binary minus; the LaTeX is '- 3 \\omega x - 2 \\omega \\dot{y}' as in the TeX source, so the tool reads plain '3' and '2'.",
 (11, IP): "Same differences as the first parser for '−1' x3, '−4' x3, '−0.1' x3, '−0.75' (Unicode versus ASCII minus). pypdf extracts (23) as '¨x− 3ωx− 2ω ˙y' with a space after each binary minus, so its '3' and '2' agree with the text. pypdf artefact, confirmed in its raw text: 'about 2 .68 s' is extracted with a space inside the number, which gives '2' and '68' as missing and '2.68' as extra; the page prints 2.68 s.",
 (12, ML): "All 4 lines contain inline math now written in LaTeX: two lines of the Figure 4 caption ($\\hat{K}$ twice), the first line of the continued paragraph ('for $\\hat{K}=20$, 40 and 100 are reported in Table 1'), and the first line of the 'Figure 5 shows ...' paragraph ($\\zeta_1$, $\\zeta_2$). Text inside the Figure 4 crop (panel labels, tick labels, legend) is excluded by the tool and was checked on a 150 dpi crop." + WORDS,
 (13, ML): "The 3 lines are the first halves of the three Algorithm 1 setting cells of Table 1, printed 'K = 2000, ˆK =' with the hat as a separate glyph before K and the value (20, 40, 100) wrapped to the next line of the cell. The table cells contain 'K = 2000, K̂ = 20', 'K = 2000, K̂ = 40' and 'K = 2000, K̂ = 100' (K with a combining circumflex), so only the hat glyph order differs. All cells and values of Table 1 were read on a 150 dpi crop of the table.",
}
EXPECT_ML = {2: 10, 3: 33, 4: 21, 5: 39, 6: 36, 7: 33, 8: 40, 9: 25, 10: 20, 11: 19, 12: 4, 13: 3}
EXPECT_ND = {
    2: ({"−1": 2}, {"-1": 2}),
    3: ({"−1": 4}, {"-1": 4}),
    6: ({"−2": 3}, {"-2": 3}),
    10: ({}, {"1": 8, "3": 2, "0": 3, "2": 2, "4": 2, "5": 1, "9": 1, "6": 1, "7": 1, "22": 1}),
    11: ({"−3": 1, "−2": 1, "−1": 3, "−4": 3, "−0.1": 3, "−0.75": 1}, {"3": 1, "2": 1, "-1": 3, "-4": 3, "-0.1": 3, "-0.75": 1}),
}
EXPECT_IP = {
    2: ({"−1": 2}, {"-1": 2}),
    3: ({"1": 1, "−1": 3}, {"-1": 4}),
    6: ({"−2": 3}, {"-2": 3}),
    10: EXPECT_ND[10],
    11: ({"2": 1, "−1": 3, "−4": 3, "−0.1": 3, "−0.75": 1, "68": 1}, {"-1": 3, "-4": 3, "-0.1": 3, "-0.75": 1, "2.68": 1}),
}
v = json.loads((D / "verification.json").read_text(encoding="utf-8"))
for p in v["pages"]:
    n = p["page"]
    assert len(p["missing_lines"]) == EXPECT_ML.get(n, 0), ("missing-line count changed", n, len(p["missing_lines"]))
    nd, ip = p["number_differences"], p["independent_parser_number_differences"]
    assert (nd["missing"], nd["extra"]) == EXPECT_ND.get(n, ({}, {})), ("number differences changed", n, nd)
    assert (ip["missing"], ip["extra"]) == EXPECT_IP.get(n, ({}, {})), ("second-parser number differences changed", n, ip)
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
