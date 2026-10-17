#!/usr/bin/env python3
"""Write adjudications.json from the current review queue (nath2026koopman). Reasons are keyed by (page, check);
the script refuses to run if the queue holds a diagnostic without a written reason or if the diagnostics changed."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/nath2026koopman-paper"
D = W / "documents/s001-nath2026koopman"
ML, ND, IP = "missing_lines", "number_differences", "independent_parser_number_differences"
CHK = (" Checked with scripts in the scratch directory: every math snippet of the page is string-identical, after macro "
       "expansion and whitespace removal, to the authors' TeX source (texcompare.py, 471 snippets in the paper, only the "
       "title-block author marks differ); every word of three or more letters of each reported line occurs in order in the "
       "page text apart from math glyph order (linecheck.py: 350 lines, the 13 unmatched ones are subscript/superscript "
       "orderings such as 'KAzref', 'emax', 'xref,(0)' and the \\sin/\\cos/\\tan rows of (14)); the per-page multiset of "
       "prose words equals pdftotext apart from math glyph runs, running headers and figure-internal text (wordcheck.py); "
       "the per-page counts of relation, operator and Greek symbols agree with the PDF layer once \\doteq (printed '.='), "
       "\\rightarrow, \\Vert and figure-internal glyphs are accounted for (symbol_check2.py). The page was also read on a "
       "170 dpi render with higher-resolution crops of the mathematics.")
def minus(what):
    return ("Sign glyph only: the PDF prints a Unicode minus and the LaTeX transcription uses the ASCII hyphen-minus, so the "
            "tool reports the same value as missing (Unicode) and extra (ASCII): " + what + " No other number differs; values "
            "read on the render.")
N5 = minus("the six '-1' are the subscripts 0:T-1 of u in Problem 1, Problem 2, Section 5.1 and Section 5.2 and j-1 of the "
           "check-z recursion and of u (Section 5.1).") + (" In addition, Problem 2 prints 'length-(T + 1)' with spaces, which the "
           "PDF tokenizer reads as a bare '1', while the transcription '$(T+1)$' (as typed in the TeX) gives '+1'; so '1' "
           "missing and '+1' extra are the same quantity.")
N8 = minus("the two '-1' are the upper limits T-1 of the braces in displays (8) and (9).") + (" In addition, the index set "
           "'i in {K^cal + 1, ..., K^cal + M}' is printed with spaces around '+' (PDF token '1') while the transcription "
           "'K^{\\text{cal}}+1' gives '+1'; '1' missing and '+1' extra are the same quantity.")
N10 = ("Sign glyph only: '−3.98', '−11.54' (Pure NNV Reachability paragraph) and '−18.709' (Planar Quadcopter paragraph) are "
       "printed with a Unicode minus and typed in math as '$-3.98$', '$-11.54$', '$-18.709$' (ASCII hyphen-minus), so each value "
       "is reported once missing and once extra. The text-mode values '-23.35' and '-40.66' use a hyphen in both and do not "
       "differ. Table 1 cells are in the CSV with the Unicode minus as printed.")
I10 = (N10 + " The second parser in addition reads the first columns of Table 1 without the column gap and reports the "
       "merged tokens '3100', '6100', '12200', '11225', '28400' (system dimension + time steps of the five rows) as missing; the "
       "CSV cells '3', '6', '12', '11', '28', '100' (twice: Unicycle and 2D Quad time steps), '200', '225', '400' are the same "
       "values and are reported as extra. All Table 1 cells were compared one by one with a 280 dpi crop.")
N11 = ("Superscripts and signs only: the PDF text layer flattens '2×10^6' and '1×10^7' to '106' and '107', while the LaTeX "
       "'$2\\times 10^6$', '$1\\times10^{7}$' gives '10' and '6', '10' and '7' (reported as '10' twice, '6', '7' extra). The "
       "learning rate '1×10^−3' and '−30.32' are printed with a Unicode minus and typed with ASCII hyphen-minus in math "
       "('-3', '-30.32' extra; '−3', '−30.32' missing). Values read on the render.")
I11 = ("Same values as the first parser; the second parser keeps the exponents 10^6, 10^7 separate, so only the sign glyph "
       "remains: '−30.32' (NNV-only baseline log-volume, 3D Quadcopter paragraph) and the exponent '−3' of the swimmer "
       "learning rate 1×10^−3 are printed with a Unicode minus and typed with ASCII hyphen-minus in math.")
A17 = ("Missing '−9.81' / extra '-9.81' is the gravity g = −9.81 m/s^2 of the planar quadcopter (Unicode minus in the PDF, "
       "ASCII in '$g=-9.81\\textrm{m/s}^2$'). All other extras come from the transcription of Algorithm 1, whose PDF text "
       "lies inside the image crop 'algorithm-1' and is therefore excluded on the PDF side: the printed line numbers 1-10, "
       "the subscripts 0:T and 0:T-1 (two '-1'), x_0, \\mathcal{B}_1(0) and the references 'Equation (2)', 'Equation (3)'. "
       "A script comparison shows that the token multiset of the transcription item ('1' x8, '0' x15, '2' x3, '-1' x2, '3' "
       "x3, '4' x2, '5' to '10' once each) equals the reported extras exactly. Each line was read on a 160 dpi crop.")
REASONS = {
 (1, ML): "Two lines of the author block, 'Devesh Nath∗1' and 'Haoran Yin∗1': the superscript marks are written as inline math '$^{\\ast 1}$' after the bold name (the PDF glues '∗1' to the name), so the normalized line does not match; names, marks and e-mail addresses were read on the 170 dpi render and kept as printed.",
 (3, ML): "All 7 lines contain mathematics now written in LaTeX: display (1b) with the dotted equals sign, the five lines of the notation paragraph (timestep set, state/control spaces, feedback law, Int with under/overlined bounds, the a-ball with the infinity norm, the sequence notation, the Minkowski symbols) and the last line of the 'Koopman Operators' paragraph (phi^infinity, K phi^infinity(x) =); the formula split at the page end was completed on this page with 'phi^infinity o f(x)' from page 4." + CHK,
 (4, ML): "All 36 lines contain mathematics now written in LaTeX: the end of the Koopman Operators paragraph (lifting function, K_A, K_B, decoder psi, the slip 'g'), the NNV paragraph (CG G, S, n_i, n_o, under/overlined G), Proposition 1 (interval S, affine bounds, Psi, Phi, alpha, beta), the reachable-set paragraph (exact reachable set with its printed extra brace, RSOA, T-step composition, F(x_0)), the CP paragraph (split CP sets, score R^(i), s: Y x Y -> R>=0, Quantile, prediction set, P(...)) and the Problem Statement start (planner P, x^ref, u^ref, X_0 minus B_eps(0)); the first line starts on page 3 with the formula completed there." + CHK,
 (4, ND): minus("the two '-1' are the superscript T-1 of the exact reachable set and the subscript 0:T-1 of u^ref in the Problem Statement."),
 (4, IP): "Same payload as the first parser. " + minus("the two '-1' are the superscript T-1 of the exact reachable set and the subscript 0:T-1 of u^ref in the Problem Statement."),
 (5, ML): "All 60 lines contain mathematics now written in LaTeX: the end of the Problem Statement (X_0 minus B_eps(0), x_0^ref, B_eps(x_0^ref), the probability of the conjunction), Problems 1 and 2 (dataset D with the printed missing parenthesis, Koopman model tuple, controller map, x^ref, u^ref, X-bar_{0:T}), Section 5.1 (composite loss L, L_1, L_2 with check-z, K_A, K_B; the glyph fragments 'j )−ϕ(ψ(ϕ(x(i)' etc.) and Section 5.2 (x_0^ref, lifted dynamics, z^ref, u^ref and display (2))." + CHK,
 (5, ND): N5,
 (5, IP): "Same payload as the first parser. " + N5,
 (6, ML): "All 43 lines contain mathematics now written in LaTeX: the paragraph after (2) (K_B^dagger, delta z, delta u, the LQR cost with transposes, Q, R, Q_T, G_{0:T-1}), displays (3)-(4) printed side by side, the Section 5.3 paragraph (X-bar_t, phi, psi, Gamma, z^ref, the TKFL map, x-hat), displays (5)-(6) and the 'To summarize' paragraph (z_{0:T} with the printed slip z_2, auto_LiRPA, under/overlined Gamma)." + CHK,
 (6, ND): minus("the five '-1' are the subscripts 0:T-1 of delta u, G and the LQR sum limit T-1 (paragraph after (2)), u^ref_{0:T-1} (Section 5.3) and the upper limit T-1 in display (5)."),
 (6, IP): "Same payload as the first parser. " + minus("the five '-1' are the subscripts 0:T-1 of delta u, G and the LQR sum limit T-1, u^ref_{0:T-1} in Section 5.3 and the upper limit T-1 in display (5)."),
 (7, ML): "All 32 lines contain mathematics now written in LaTeX: the continuation 'reached under (5) ...' with X-hat-bar_{0:T}, display (7) (min/max over x_0 in X_0 of under/overlined Gamma_t with u^ref, z^ref), the KRS paragraph, Lemma 1 (Gamma, X_0, x-hat, z^ref, u^ref, the printed X-hat_t) and the first paragraph of 5.4 (D_C with K^cal, x^{ref,(i)}, B_eps(x_0^ref), z^{ref,(i)}, u^{ref,(i)}). Text inside Figure 2 is excluded by the crop." + CHK,
 (7, ND): minus("the five '-1' are the subscripts 0:T-1 of u^ref in display (7) (twice), in Lemma 1, and of u^{ref,(i)} twice in the 5.4 paragraph."),
 (7, IP): "Same payload as the first parser. " + minus("the five '-1' are the subscripts 0:T-1 of u^ref in display (7) (twice), in Lemma 1 and twice in the 5.4 paragraph."),
 (8, ML): "All 57 lines contain mathematics now written in LaTeX: displays (8)-(9) printed side by side, the normalization paragraph (e_{t,j}^(i), D_E, R^(i) = max, lambda_{t,j}, e^max, M^lambda and the printed index set with M), the quantile paragraph (C = Quantile, p, ceiling, e-bar_{t,j}), the unnumbered CP display, Theorem 1 with display (10), the Offline Calibration paragraph (N^ref, x^{ref,(i)}, B_eps, e_t^(i)) and the runtime paragraph (X-hat-bar, diag(e-bar_t) B_1(0))." + CHK,
 (8, ND): N8,
 (8, IP): "Same payload as the first parser. " + N8,
 (9, ML): "All 10 lines contain mathematics now written in LaTeX: nine lines in the continuation of the runtime paragraph (e-bar_t, R^(i), the data pair (x^{ref,(i)}, x_0^(i)), x^ref ~ P, x_0 ~ B_eps(x_0^ref), the probability of the conjunction >= 1 - delta) and one line of the 'Pure CP based verification.' paragraph with the target delta in math." + CHK,
 (10, ML): "All 6 lines contain inline mathematics now written in LaTeX: two lines of the Figure 3 caption (target 1 - delta, K^cal), the Unicycle paragraph (phi, psi, z in R^10) and the Planar Quadcopter paragraph (T = 100, z in R^24, 59.85 s typed with a thin space and \\mathrm{s}). The prose around them was compared with the render." + CHK,
 (10, ND): N10,
 (10, IP): I10,
 (11, ML): "All 8 lines contain inline mathematics now written in LaTeX in the 3D Quadcopter, MuJoCo: Hopper and MuJoCo: Customized Swimmer paragraphs: 1 m and 2153.45 s typed with \\mathrm and thin spaces, T = 200, phi, psi, z in R^24 / R^38, 2 x 10^6, 1 x 10^7, LR 1 x 10^-3, gamma = 0.9999, batch size 512, -30.32. Figure 4 text is excluded by the crop." + CHK,
 (11, ND): N11,
 (11, IP): I11,
 (12, ML): "One line, the first line of the page (end of the Conclusion): 'set with a specified probability (i.e., at least 1 −δ). Across several benchmarks, including a unicy-'. The quantity 1 - delta is typed in math ('$1-\\delta$') and the word 'unicy-cle' is joined across the line end, which breaks the normalized match; read on the render, the sentence is complete and joined to page 11.",
 (15, ML): "All 36 lines contain mathematics now written in LaTeX: Lemma 1 restated (Gamma, X_0, X-hat-bar, z^ref, u^ref, the printed X-hat_t), the proof (Gamma_t with under/overlines, the unnumbered inequality display, Int(x-hat^L, x-hat^U), the two-line min/max display written as one aligned block), Theorem 1 restated with display (11), the unnumbered probability display with the big conjunction, and the start of its proof." + CHK,
 (15, ND): minus("the four '-1' are the subscripts 0:T-1 of u^ref in the restated Lemma 1, in the proof sentence and twice in the unnumbered inequality display."),
 (15, IP): "Same payload as the first parser. " + minus("the four '-1' are the subscripts 0:T-1 of u^ref in the restated Lemma 1, in the proof sentence and twice in the unnumbered inequality display."),
 (16, ML): "All 34 lines contain mathematics now written in LaTeX: Steps 1-3 of the proof of Theorem 1 (x-hat_{t,j}^(0), the Int display with quantifiers, {R^(i)}_{i=0}^{K^cal}, z^ref, u^ref, G_t, B_eps, the event E, the decomposition x = x-hat + e, the bound display, X-bar^{1-delta}) and the 8.2 paragraph (x^ref, u^ref, e-bar_t, X-bar_{0:T}, X^{1-delta}_{0:T})." + CHK,
 (16, ND): minus("the '-1' is the subscript 0:T-1 of u^ref in Step 2 of the proof."),
 (16, IP): "Same payload as the first parser. " + minus("the '-1' is the subscript 0:T-1 of u^ref in Step 2 of the proof."),
 (17, ML): "All 5 lines contain mathematics now written in LaTeX: the unicycle sentence (x in R^3, u in R^2, dt = 0.1), the planar-quadcopter sentence (x in R^6, u in R^2, m = 0.5 kg, g = -9.81 m/s^2, I_y = 0.01 kg m^2, dt = 0.05 s) and the left-hand sides 'x-dot = f(x, u) =' of displays (12) and (13) (bold x and u). Text inside Algorithm 1 is excluded by the crop." + CHK,
 (17, ND): A17,
 (17, IP): "Same payload as the first parser. " + A17,
 (18, ML): "All 11 lines belong to the 3D-quadcopter sentence (I_{x,y,z} = [0.5, 0.1, 0.3] kg m^2, dt = 0.025 s) and display (14): the left-hand side 'x-dot = f(x, u) =' and nine rows of the 12-row vector, whose functions are written \\sin, \\cos, \\tan and whose fractions u_i/I_* are typed \\frac; every row was compared with a 220 dpi crop, including the printed 'cos phi · sin phi' in row 8." + CHK,
 (18, ND): minus("'-9.81' is the gravity g = −9.81 m/s^2 of the 3D quadcopter."),
 (18, IP): "Same payload as the first parser. " + minus("'-9.81' is the gravity g = −9.81 m/s^2 of the 3D quadcopter."),
 (20, ML): "Two lines with inline mathematics now written in LaTeX: 'angular velocity ($p, q, r$) and angle ($\\phi, \\theta, \\psi$)' (8.3.4 continuation) and 'remain with with probability at least $1-\\delta$' (8.3.5; the doubled 'with' is printed). Prose read on the render; Figure 6 text is excluded by the crop.",
}
EXPECT_ML = {1: 2, 3: 7, 4: 36, 5: 60, 6: 43, 7: 32, 8: 57, 9: 10, 10: 6, 11: 8, 12: 1, 15: 36, 16: 34, 17: 5, 18: 11, 20: 2}
v = json.loads((D / "verification.json").read_text(encoding="utf-8"))
for p in v["pages"]:
    n = p["page"]
    assert len(p["missing_lines"]) == EXPECT_ML.get(n, 0), ("missing-line count changed", n, len(p["missing_lines"]))
    for key in (ND, IP):
        d = p[key]
        assert bool(d["missing"] or d["extra"]) == ((n, key) in REASONS), ("number diagnostics changed", n, key, d)
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
