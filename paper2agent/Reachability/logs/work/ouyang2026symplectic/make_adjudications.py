#!/usr/bin/env python3
"""Write adjudications.json from the current review queue (ouyang2026symplectic).
Reasons are keyed by (page, check); the script refuses to run if the queue holds a diagnostic
without a written reason or if the reviewed payload (EXPECT) changed."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/ouyang2026symplectic-paper"
D = W / "documents/s001-ouyang2026symplectic"
ML, ND, IP = "missing_lines", "number_differences", "independent_parser_number_differences"
CHK = (" Checked with three scripts in the scratch directory: every math snippet of the page is string-identical, after macro expansion and whitespace removal, to the authors' TeX source "
       "(texcompare.py; in the whole paper the only non-identical snippets are two brace-only differences and the end-of-proof squares); "
       "the per-page multiset of prose words of four or more letters equals that of pdftotext apart from LaTeX command names, glyph-soup tokens of formulas, small-caps heading initials and words hyphenated at line ends (wordcheck.py); "
       "and the per-page counts of relation, operator and Greek symbols agree with the PDF text layer except for explained notation differences (lvert/rvert bars, the two-glyph 'not equal' and 'implies' signs, big norm delimiters, labelled arrows; symbol_check2.py). "
       "The formulas were also read on 230-330 dpi crops of the page.")
ALG = ("Extra numbers only, nothing missing. All extras come from the transcription of Algorithm 1, whose PDF text lies inside the image crop and is therefore excluded from the source count: "
       "the title 'Algorithm 1', the printed line numbers 1-20, 'j=1' in line 1 and 'j = 1,...,M' in line 4 (which gives '1' four times in total), "
       "and the zeros of line 5 's <- 0' and line 8 '(0, T_j - s]' and 'r_i(t) > 0' (which gives '0' three times); 2-20 once each. "
       "Each number was read on the 150 dpi crop of the algorithm box and on the built algorithm-1.jpg.")
MIN = ("Sign glyph only: the PDF prints a Unicode minus in the exponents of '1.2 x 10^-3' and '5 x 10^-4', in the matrix entry '-1' of the two dynamics displays (spring-mass and pendulum), "
       "and in the input bound '[-20, 20]' (twice); the LaTeX uses the ASCII hyphen-minus, so the tool reports -3, -4, -1 (x2), -20 (x2) as missing with Unicode minus and extra with ASCII minus. "
       "Each value was read on the 230 dpi column crops and the 330 dpi crops of the two displays; no other number differs.")
REASONS = {
 (2, ML): "All 45 lines contain inline or displayed mathematics now written in LaTeX: the Notation paragraph (norm, ball B_r(x), diameter D_S, closure, boundary, int(S), d(x,S), ceiling/floor), Definition 1 with display (1) and its 'where' clause, Assumption 1, Assumption 2 with its display, Remark 1 with display (2), Definition 2 with the Sigma_E display, the Section II-B paragraph on admissible controls and the flow, S_0 and S_tgt, Problem 1 with its display, the Section II-C paragraph, Definitions 3 and 4. Two of the lines are the line-end halves 'trajecto-' and 'con-/dition' of words written whole." + CHK,
 (3, ML): "All 54 lines contain inline or displayed mathematics now written in LaTeX: Theorem 1 (mu_E, the family mu_alpha^E, nu_E, the integral formula, whose pieces appear as the fragments 'AE µE' and 'α dνE(α).'), the K_alpha^E display and the supp definition, Proposition 1 with its closure display, the demonstration set D, Definition 5 with the control-alphabet display, Definition 6 with the assignment-set and Supp displays, the paragraph defining rho_K and the index map with its cases display (fragments 'min1≤i≤N', 'ρK(x) ≤1,'), Definition 7 with its display, Remark 2 with its display. Two lines are the line-end halves 'intro-' and 'as-/signment' of words written whole." + CHK,
 (4, ML): "All 44 lines contain inline or displayed mathematics now written in LaTeX: H(S_tgt)=[H_min,H_max] and the definitions of H_min, H_max; Assumption 3 with its display; Definition 8 (label with S_tgt, H^star_+, H^star_-, Delta H); the sets H_tgt and H_tgt^epsilon; Assumption 4 with its display; the hitting time T_epsilon, displays (3) and (4) and the unnumbered rate display (numerators and denominators appear as separate fragments such as 'Tϵ(x, u)' and 'vϵ(x) := sup'); Assumption 5 with its display; Theorem 2 with conditions 1)-3), their three displays and the conclusion display." + CHK,
 (5, ML): "All 57 lines contain inline or displayed mathematics now written in LaTeX: Steps 1-3 and the Conclusion of the proof of Theorem 2 with displays (5), (6), (7) and the unnumbered displays for y', Delta H(y'), c, Sigma_E and phi(T,y',0); the ceiling N_* (fragments 'by at least v0τmin > 0, and thus after at most N∗=' and 'v0τmin'); Remark 4 (S_0, S_tgt, alpha); the first paragraph of Section III-B; Lemma 1 with its display; the four displays of its proof (fragments such as 'f(ϕ(t, x, u), u(t)) dt' and 'Tϵ(x, u) ≥T ⋆'). Line-end halves 'com-/ponent', 'trajec-', 'lution.' and 'ing S0' belong to words written whole (component, trajectory, evolution, connecting)." + CHK,
 (6, ML): "All 49 lines contain inline or displayed mathematics now written in LaTeX: the lead-in paragraph (K, X), Assumption 6 and Assumption 7 with their displays, Remark 6 (X, K), Theorem 3 with the display for r_i, the clause on u_i and T^star_epsilon(x_i), items 1) and 2) and the bound on N (fragments '16L2', 'µH(1 −v0', 'exp( 2L(LHDX +ϵ)'), Step 1 (X_c, u_x, the two unnumbered displays, r(x), the 'Moreover' display), Step 2 (inline fractions, the unnumbered display, display (8)), Step 3 (the unnumbered display and display (9)). The line 'Then there exists a nonparametric chain policy πK, con-' ends with the first half of 'constructed'." + CHK,
 (7, ML): "All 50 lines contain inline or displayed mathematics now written in LaTeX: the two three-line displays at the top of the left column (subscript fragments 'y1,y2∈Br(x)(x)'), the two case sentences with H^star_+, the max display, displays (10) and (11), Step 4 with the definition of [H_1,H_2], the covering sentence, the two-line display, the subcover display and the definition of K, the display [H_1,H_2] in H(Supp(K)), Steps 5 and 6 with the two-line bound on N (fragments '16L2', 'µH(1−v0', '2L(LHDX +ϵ)'), Assumption 8 items 1) and 2), Theorem 4 with its display, and the first paragraph of its proof. The line 'Theorem 4 (Finite-Time Reachability). Let K be an assign-' ends with the first half of 'assignment'." + CHK,
 (8, ML): "All 42 lines contain inline or displayed mathematics now written in LaTeX: the proof of Theorem 4 (the sequences x_i, y_i, the three unnumbered displays, the sum and floor displays whose pieces appear as 'Nτmin ≤', 't2,i ≤∆H(x0)', 'v0τmin', the definition of T-bar, displays (12)-(14), the final T_max display), the Section III-D paragraph (D, S_tgt^delta, anchor time s, x_i, u_{i,t}), the display for r_i(t), the paragraph defining t_i, tau_i, sigma_i, x_{i+1} and K, and the first paragraph of Section IV (x=[q^T,p^T]^T, x^*, S_tgt, epsilon = 0.1). Lines inside the Figure 1 and Algorithm 1 crops are excluded by the tool; the algorithm was checked line by line against its crop." + CHK,
 (8, ND): ALG,
 (8, IP): "Same payload as the first parser. " + ALG,
 (9, ML): "All 11 lines contain mathematics or numbers set in mathematics now written in LaTeX: '1.2 x 10^-3' and '5 x 10^-4', the energy bound H-bar, pieces of the two dynamics displays (', H(x) = p2', 'mℓ2 ˙θ', '2mℓ2 + mgℓ(1 −cos q),'), the parameter sentences with m, ell, g = 9.81 m/s^2, u in [-20, 20], x^* = [0, 0]^T and x^* = [pi, 0]^T, 'M = 2 ... M >= 3' and 'M = 1,...,5'. Every number on the page was read on the 230 dpi column crops and the 330 dpi crops of the two displays." + CHK,
 (9, ND): MIN,
 (9, IP): "Same payload as the first parser. " + MIN,
}
EXPECT_ML = {2: 45, 3: 54, 4: 44, 5: 57, 6: 49, 7: 50, 8: 42, 9: 11}
EMPTY = {"missing": {}, "extra": {}}
E8 = {"missing": {}, "extra": {"0": 3, "1": 4, **{str(k): 1 for k in range(2, 21)}}}
E9 = {"missing": {"−3": 1, "−4": 1, "−1": 2, "−20": 2}, "extra": {"-3": 1, "-4": 1, "-1": 2, "-20": 2}}
EXPECT_ND = {8: E8, 9: E9}
v = json.loads((D / "verification.json").read_text(encoding="utf-8"))
for p in v["pages"]:
    n = p["page"]
    assert len(p["missing_lines"]) == EXPECT_ML.get(n, 0), ("missing-line count changed", n, len(p["missing_lines"]))
    assert p["number_differences"] == EXPECT_ND.get(n, EMPTY), ("number differences changed", n, p["number_differences"])
    assert p["independent_parser_number_differences"] == EXPECT_ND.get(n, EMPTY), ("second-parser differences changed", n)
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
