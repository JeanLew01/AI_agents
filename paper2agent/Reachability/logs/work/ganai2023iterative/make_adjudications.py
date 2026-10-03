#!/usr/bin/env python3
"""Write adjudications.json from the current review queue (ganai2023iterative). Reasons are keyed by (page, check);
the script refuses to run if the queue holds a diagnostic without a written reason or if the reviewed payload changed."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/ganai2023iterative-paper"
D = W / "documents/s001-ganai2023iterative"
ML, ND, IP = "missing_lines", "number_differences", "independent_parser_number_differences"
CHK = (" Checked with scripts in the scratch directory: every math snippet of the page is string-identical, after macro expansion and whitespace removal, to the authors' TeX source (texcompare.py, 606 snippets, none unmatched); "
       "every word of three or more letters of each reported line occurs in order in the page text (linecheck.py, 463 lines, none unmatched); the per-page multiset of words of four or more letters equals that of pdftotext apart from math glyph runs and figure labels inside crops (wordcheck.py); "
       "and the per-page counts of relation, operator and Greek symbols agree with the PDF text layer (symbol_check.py). The formulas were also read on the 170 dpi page render.")
MAPS = "The PDF text layer encodes the 'maps to' arrow (\\mapsto) as the two glyphs '7' and an arrow, so each \\mapsto of the page gives one spurious '7' in the source count; "
RP = "the set of non-negative reals is printed R with superscript + and subscript 0 and typed '\\mathbb{R}^+_0' as in the TeX source, which the tokenizer reads as '+0' where the PDF layer gives a separate '0'. "
def minus(what): return ("Sign glyph only: the PDF prints a Unicode minus and the LaTeX uses the ASCII hyphen-minus, so the tool reports the same value as missing (Unicode minus) and extra (ASCII minus): " + what + " No other number differs; values read on the page render.")
A7 = ("Missing '-1' (Unicode minus) and extra '-1' (ASCII) are the subscript of zeta_{j-1} in the step-size display of assumption A1. All other extras come from the transcription of Algorithm 1, whose PDF text lies inside the image crop and is therefore excluded from the source count: "
      "the title 'Algorithm 1', the printed line numbers 1-11, the loop ranges '0,1,2,...' (twice), the parameter subscripts theta_0, eta_0, kappa_0, xi_0, omega_0, the learning rates zeta_1 to zeta_4, the subscripts k+1 and t+1 (ten '+1'), '[1 - p(s_t)]' and '(1 - p(s_t))' and the indicator 1 with 'h(s_t)>0'. "
      "A script comparison shows that the token multiset of the transcription item (1 x11, 0 x8, 2 x5, 3 x3, 4 x3, +1 x10, 5-11 once each) equals the reported extras exactly, apart from the '-1' explained above. Each line was read on the 110 dpi crop of the algorithm box and compared with the algorithmic source.")
N14 = ("Nothing is missing. The three extras come from Table 1 and its marked conversion note: the indicator symbol in the table cell is written with the Unicode double-struck digit one (counted as a separate token), the note repeats the row symbols in LaTeX (a second d_0 gives the extra '0'; its \\mathbb{1} matches the PDF's '1' of the indicator row) and the words 'Table 1' in the note give the extra '1'. Table rows were read cell by cell on the render.")
N25 = ("Nothing is missing. All extras come from the marked conversion note under Table 2, which repeats the four learning-rate schedules in LaTeX (1e-3 -> 0, 3e-4 -> 0, 5e-5 -> 0, 1e-4 -> 0: tokens 1, -3, 3, -4, 5, -5, 1, -4 and four zeros), says 'to 0' once more, and contains 'Table 2' and the quoted cell '2-Layer, MLP'. A script comparison shows the token multiset of the note equals the reported extras exactly. The table cells themselves match the PDF (the cells use the printed Unicode minus).")
N30 = ("Nothing is missing. All extras come from the marked conversion note after Equation (10), which lists the colour-coded terms of Equations (10) and (11): '10' and '11' twice each, the subscripts hc2 (seven times) and hc1 (seven times) and two '1' from '(1-p_hc2(s))' and '(1-p_hc1(s))'. A script comparison shows the token multiset of the note equals the reported extras exactly. The two equations themselves were compared with the TeX source and the render.")
REASONS = {
 (3, ML): "All 21 lines belong to Sections 3.1 and 3.2 and contain mathematics now written in LaTeX: the MDP tuple, the maps for P, r and h, H_min, H_max, the discount range (0,1), S_I, d_0, pi(a|s), the definitions of V^pi and V^pi_c, the (CMDP) display (fragments such as 's~d0[V pi(s)], subject to', 'max', 'E', '(CMDP)') and the enumerators '1.' and '2.' printed in math type." + CHK,
 (3, ND): MAPS + "this page has three (P, r, h), which gives the three missing '7'. The missing '0' and extra '+0': " + RP + "Checked on the render.",
 (3, IP): "Same payload as the first parser. " + MAPS + "three on this page. Missing '0' / extra '+0': " + RP,
 (4, ML): "All 27 lines contain mathematics now written in LaTeX: Definitions 1-5 (safe/unsafe set, V_h, the REF and its display, the optimal REF, the feasible set), Theorem 1 with its Bellman display and the where-sentence, the indicator notation, the RCRL paragraph and the (RCRL) display (fragments 'max', 'E', 's~d0', '(RCRL)')." + CHK,
 (4, ND): MAPS + "this page has four (h, V_h^pi, phi^pi, phi^*), which gives the four missing '7'. The two missing '0' and two extra '+0': " + RP + "It occurs twice on this page. Checked on the render.",
 (4, IP): "Same payload as the first parser. " + MAPS + "four on this page. Two missing '0' / two extra '+0': " + RP,
 (5, ML): "All 30 lines contain mathematics now written in LaTeX: the end of Section 4.2 (arg min over V_h, V_h^pi, V_h(s)), Section 5.1 (phi^pi(s), the set {0, 1}, phi^*(s), the indicator of S_f^{pi_s}, pi_s), displays (1), (2), (3) (fragments such as 's~d0[-V pi', '(1)', '(2)', '(3)'), Proposition 1 and Proposition 2 (trajectories tau and tau', m, n, epsilon, gamma in (1-epsilon,1), V_c^{pi^*})." + CHK,
 (6, ML): "All 27 lines contain mathematics now written in LaTeX: phi^*(s) and 1-phi^*(s) in Section 5.2, the (RESPO) display, -V_c^pi(s), max_pi V^pi(s), the Lagrangian display, phi^*, the gamma-contraction remark, p(s), the REF update display, S_v, s', '0 << gamma < 1', display (4), and the last paragraph (Q-function relations, Gamma_Theta, theta in R^n, the arg min with double-bar norm, Gamma_Omega)." + CHK,
 (7, ML): "All 13 lines are in Section 5.4 and the Baselines paragraph and contain mathematics now written in LaTeX: assumption A1 with its step-size display (fragments 'zeta_i(k) = infinity and', 'zeta_i(k)2 < infinity, for all i in {1, 2, 3, 4},', 'zeta_j(k) = o(zeta_{j-1}(k)), ...'), the sentence on the four schedules, A2, A3, the CBF constraint with the dotted h and 'chi = 0'. Lines inside the Algorithm 1 and Figure 1 crops are excluded by the tool; the algorithm was checked line by line against its crop." + CHK,
 (7, ND): A7,
 (7, IP): "Same payload as the first parser. " + A7,
 (8, ML): "One line, the last line of the Figure 2 caption: 'slightly higher rewards, but accumulates over 3x violations than RESPO. Note, Vanilla PPO is unconstrained.' The multiplication sign is typed in math mode ('$3\\times$'), which breaks the normalized match; the caption was read on the render and equals the TeX caption.",
 (9, ML): "All 6 lines are in the last paragraph of the page and contain inline mathematics now written in LaTeX ('chi = 0' twice, V^pi_h three times, V^pi_c twice); the paragraph was rebuilt from the TeX source and read on the render." + CHK,
 (10, ML): "All 4 lines contain inline mathematics now written in LaTeX: three lines of the Figure 6 caption (V^pi_c twice, 'chi = 0') and the line 'the importance of learning our REF and using value function V^pi_c' of the continuing paragraph." + CHK,
 (14, ML): "All 10 lines belong to Appendix B and are mathematics now written in LaTeX: the two critic gradients, the REF gradient, the four fragments of the policy-gradient display, the multiplier gradient and the two lines of the clipping sentence (range [0, lambda_max], projection with arg min and double-bar norm). The rows of Table 1 are covered by the CSV." + CHK,
 (14, ND): N14,
 (14, IP): "Same payload as the first parser. " + N14,
 (15, ML): "All 47 lines contain mathematics now written in LaTeX: the Bellman display and where-sentence of the restated theorem, the five-line proof display (many small fragments such as 'tau~pi,P(s) max', 'st in tau\\{s}', 'E'), the explanatory paragraph, Proposition 3 and its proof with the V_c display, Proposition 4, the 'In other words' paragraph and the first lines of the proof (m = 1, m > 1). The proof display was also read on a 260 dpi crop." + CHK,
 (15, ND): minus("'-1' is the '(m-1)' in 'a finite number (m-1) of steps'."),
 (15, IP): "The second parser splits the same '(m - 1)' into a separate minus glyph and '1', so it reports '1' missing and the ASCII '-1' extra. " + minus("it is the '(m-1)' in 'a finite number (m-1) of steps'."),
 (16, ML): "All 21 lines contain mathematics now written in LaTeX: the Case 1 and Case 2 paragraphs (V_c^pi(s) = 0, pi^*, H_E, H_N), the two bound paragraphs (m-1, H_max, w, H_min), the four displays (numerators and denominators appear as separate fragments), the paragraph on upsilon(gamma) with the left limit and gamma in (1-epsilon,1), and the final paragraph." + CHK,
 (16, ND): minus("the five '-1' are 'm-1 steps' (twice in the prose) and the exponent of gamma^{m-1} in the bound on H_E and in displays (5) and (6)."),
 (16, IP): "The second parser reports three of the five as Unicode '-1' and two as a bare '1' (exponent glyphs split from the minus). " + minus("the five '-1' are 'm-1 steps' (twice) and gamma^{m-1} in the H_E bound and in displays (5) and (6)."),
 (17, ML): "All 12 lines contain calligraphic or other mathematics now written in LaTeX: the two caption lines of Figure 7 (regions X and Y) and ten lines of the C.4.1 paragraph (S_hI, S_pI, S_I, the four region definitions with overlines, W, X, Y, Z, lambda, V_c^{pi_theta}(s), the math-mode numerals 4 and 0)." + CHK,
 (18, ML): "All 32 lines contain mathematics now written in LaTeX: the Step 1 paragraph, the two Bellman operators, the sentence with the limits of Q and Q_c, the Step 2 paragraph, the four-line policy-update display and the two long displays for delta theta_{k+1} and delta theta_epsilon (each printed line gives one or more fragments)." + CHK,
 (19, ML): "All 46 lines contain mathematics now written in LaTeX; the page consists of the Lemma 1 and Lemma 2 lead-ins, five displays (the bound on E[||delta theta_{k+1}||^2 | F], the six bounds, the K_2 bound, the final bound, the six-line Lemma 2 chain) and three short connecting paragraphs. The Lemma 2 display was also read on a 200 dpi crop." + CHK,
 (20, ML): "All 47 lines contain mathematics now written in LaTeX: the end of Lemma 2, Lemma 3, display (7), the definition of Upsilon_Theta, the paragraphs with dL/dt, the Lyapunov function, the ball B_{theta^*}(rho), the four facts, Step 3, the REF Bellman operator B_p, the five-line contraction chain and the paragraph on p(s; xi^*), pi^diamond and p^diamond." + CHK,
 (21, ML): "All 44 lines contain mathematics now written in LaTeX: the optimization displays for pi^diamond (including the two-case display and (8)), the paragraph on pi^triangle, the Step 4 paragraph, the three-line multiplier update, the eleven-line delta omega_{k+1} display, and Lemma 4 with its bound." + CHK,
 (22, ML): "All 38 lines contain mathematics now written in LaTeX: the filtration sentence, Lemma 5, display (9), the paragraph with dL/dt and Upsilon_Omega, the Lyapunov function L(omega), the ball B_{omega^*}(rho'), the four facts, the saddle-point paragraph, and the C.4.4 paragraph with lambda_max, H_Delta, P_min and its two-line display." + CHK,
 (23, ML): "All 14 lines contain mathematics now written in LaTeX: 'So we can find the bound for lambda_max:', eight fragments of the five-line derivation, three lines of the following paragraph (inline fractions, 'phi(s) = 1', 'lambda >'), the CBF constraint line with the dotted h, and the FAC line with 'chi = 0'." + CHK,
 (24, ND): minus("'-3' is the position 'x = -3' in the Safety HalfCheetah sentence."),
 (24, IP): "Same payload as the first parser. " + minus("'-3' is the position 'x = -3' in the Safety HalfCheetah sentence."),
 (25, ML): "One line: 'takes ~4 hours to train.' The tilde relation and the 4 are typed in math mode ('$\\sim4$'), which breaks the normalized match; read on the render and equal to the TeX source.",
 (25, ND): N25,
 (25, IP): "Same payload as the first parser. " + N25,
 (26, ML): "Two lines of the first paragraph of D.4 with mathematics now written in LaTeX: the observation space [x_1, x_2], the action range [-0.5, 0.5], the dynamics with dotted s, and the constraint and cost with the double-bar infinity norm." + CHK,
 (26, ND): minus("'-0.5' is the lower end of the action range a in [-0.5, 0.5]."),
 (26, IP): "Same payload as the first parser. " + minus("'-0.5' is the lower end of the action range a in [-0.5, 0.5]."),
 (27, ML): "Two lines with a multiplication sign typed in math mode: 'has over 3x the number of violations as RESPO.' and 'even becoming 9x that of scalar'; both read on the render and equal to the TeX source ('$3\\times$', '$9\\times$').",
 (30, ML): "All 14 lines contain mathematics now written in LaTeX: fragments of displays (10) and (11), the paragraph defining the subscripts hc1, hc2, sc, V^pi(s) and p_hc1, and the last paragraph with V^pi_sc(s), V^pi_hc1(s), V^pi_hc2(s). Lines inside the Figure 12 crop are excluded by the tool." + CHK,
 (30, ND): N30,
 (30, IP): "Same payload as the first parser. " + N30,
 (31, ML): "Two lines of the D.9 paragraph with mathematics typed in math mode: '(i.e. x10 or x0.1)' and 'with learning rate 0.01 times ... where chi = 0'; read on the render and equal to the TeX source.",
 (33, ML): "Two lines of the D.10 paragraph containing 'chi = 0' typed in math mode ('For CMDP, we make the cost threshold chi = 0.' and 'with chi = 0, both the reward performance ...'); read on the render and equal to the TeX source.",
}
EXPECT_ML = {3: 21, 4: 27, 5: 30, 6: 27, 7: 13, 8: 1, 9: 6, 10: 4, 14: 10, 15: 47, 16: 21, 17: 12, 18: 32, 19: 46, 20: 47, 21: 44, 22: 38, 23: 14, 25: 1, 26: 2, 27: 2, 30: 14, 31: 2, 33: 2}
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
