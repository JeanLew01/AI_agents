#!/usr/bin/env python3
"""Copy every unresolved diagnostic's adjudication_entry from the review queue and attach the reason written after
checking that page. Fails if a diagnostic has no written reason or a reason has no diagnostic."""
import json
from pathlib import Path

R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/hashemi2025pca-paper"
D = W / "documents/s001-hashemi2025pca"

WORDS = (" A word-level test of every missing line (all alphabetic words of 3+ letters must occur in the same order in the page "
         "markdown) and a per-page word-multiset comparison with pdftotext leave only math glyph strings unmatched: ")
SYM = (" The per-page counts of relation/operator symbols and Greek letters in the PDF text layer (<=, >=, subset, element-of, ~, "
       "arrows, x, (+), top/bottom, angle and ceiling brackets, asterisk, +, minus, <, >, =, rho, omega, delta, tau, sigma, ell, alpha, "
       "mu, theta, Sigma) equal those in the LaTeX of the page")
MINUS = "The PDF text layer has the Unicode minus (U+2212) where the LaTeX has ASCII '-'; the counts are equal: "

REASON = {
    (2, "missing_lines"):
        "Both lines are prose lines of the second paragraph of the Introduction that contain inline math now written in LaTeX "
        "('threshold delta in (0,1), the goal is to produce a set ...' and '... with a probability of no less than delta. As "
        "explained in the'). Compared with the 170 dpi render; all words are present." + WORDS + "none.",
    (3, "missing_lines"):
        "All 17 lines contain inline math now written in LaTeX: two lines of the conformal-inference paragraph ('delta-quantile'), "
        "seven lines of the Notation paragraph ({1,2,...,n}, [n], the Minkowski-sum symbol, x ~ X, [n_0,n_1,...n_{l+1}], n_i, i in "
        "[l], e_i in R^n, ceil(x), x in R) and eight lines and line fragments of Section 2.1 (S_0..S_K in S, 0..K, S subset-eq R^n, "
        "s_1..s_K, sigma^real_{s_0}, D^real_{S,K}, S_0, W, I, Pr[s_0 not-in I] = 0). Compared with the 170 dpi render and a 260 dpi "
        "crop of the Notation paragraph and Section 2.1." + WORDS + "'lhidden' (the symbol ell followed by 'hidden') and 'Dreal' "
        "(D^real, written with the subscript before the superscript in LaTeX)." + SYM + " (20 symbols). The page has no number difference.",
    (4, "missing_lines"):
        "All 40 lines and line fragments contain math now written in LaTeX: the first paragraph (s_0 ~ W, sigma^real_{s_0} ~ "
        "D^real_{S,K}, sigma^sim_{s_0} ~ D^sim_{S,K}), the first paragraph of Section 2.2 (F: I x Theta -> S^K, theta in Theta, "
        "K-step, T^trn), the fragments of display (1), the paragraph after it (F^{(k-1)n+l}(s_0), l^th, k^th, e_l in R^n, "
        "s_1,...s_K, j=(k-1)n+l), the fragments of display (2), the residual paragraph (rho: R^{nK} -> R_{>=0}, R^j, j in [nK]), "
        "Definition 1 (four distributions), the total-variation sentence, two lines of the surrogate-flowpipe paragraph (X-bar "
        "subset R^{nK}, F(I;theta), F(s_0;theta) in X-bar) and the two lines of Definition 2 on this page. Compared with the 170 dpi "
        "render and three 260 dpi crops; displays (1) and (2) match symbol by symbol." + WORDS + "'Dreal', 'Dsim' (D^real_{S,K}, "
        "D^sim_{S,K}; in the LaTeX the subscript S,K stands between D and the superscript) and 'lsk' (e_l^T s_k in display (2))."
        + SYM + " (71 symbols).",
    (4, "number_differences"):
        MINUS + "the three '−1' are the exponent/index terms (K−1) in F^{(K-1)n+1} of display (1), (k−1) in F^{(k-1)n+l} and (k−1) "
        "in j = (k-1)n + l of the following paragraph. Each was read on the 260 dpi crop; no number is missing or changed. The "
        "equation tags (1), (2), the footnote mark 3 and the section number 2.2 are matched.",
    (4, "independent_parser_number_differences"):
        "Same three (K−1)/(k−1) terms as in the first parser's check (Unicode minus in the PDF, ASCII minus in the LaTeX). The "
        "second parser (pypdf; its text for this page was inspected) prints 'j = (k− 1)n + l' with a space after the minus, which "
        "gives a missing '1' instead of a third missing '−1'. No number is missing or changed.",
    (5, "missing_lines"):
        "All 35 lines and line fragments contain math now written in LaTeX: the two closing lines of Definition 2 (P: R^m -> {top, "
        "bottom}, d x m, mu_l in R, l = 1..m), a fragment of display (3), the paragraph of Section 2.3 on sorted residuals (rho_1 < "
        "... < rho_L, J^sim_{S,K}, delta in (0,1), rho ~ J^real_{S,K}, rho_i, i in [L]), the conformal/robust-conformal paragraph (l "
        ":= ceil((L+1)delta) <= L, Pr[rho < rho_l] >= delta, TV(J^real, J^sim) <= tau, tau > 0, Pr[rho < rho_{l*}] > delta), display "
        "(4), 'Thus, rho_{l*} serves ...', the 'Inflating Hypercube' paragraph (PE = [R^1, R^2, ..., R^{nK}], alpha_j, j in [nK]), "
        "displays (5), (6) (two fragments), the paragraph after (6) (R*, P*, R^j, -R*/alpha_j <= R^j <= R*/alpha_j) and display (7). "
        "Compared with the 170 dpi render and two 260 dpi crops; (3)-(7) match symbol by symbol, including '<= tau', the strict '>' "
        "of the robust statement and the strict '<' inside (6)." + WORDS + "'lvl' (mu_l v_l in (3)) and 'lserves' (rho_l followed by "
        "'serves')." + SYM + " (133 symbols). After writing '(L + 1)' and '(1 + 1/L)' with spaces the page has no number difference.",
    (6, "missing_lines"):
        "All 47 lines and line fragments contain math now written in LaTeX: 'Since Pr[P* = top] >= delta ...', the paragraph "
        "'delta-Confident Flowpipe & Probabilistic Reachability' (delta in (0, 1), s_0 ~ W, X subset-eq R^{nK}, sigma^real_{s_0} ~ "
        "D^real_{S,K}, Pr[sigma^real_{s_0} in X] >= delta, sigma^sim_{s_0} ~ D^sim_{S,K}, F(s_0;theta), X-bar subset R^{nK}, delta X "
        "subset R^{nK}, R^j, j in [nK]), Lemma 3 (X-bar, F, I, PE := [R^1, R^2, ..., R^{nK}], Pr[PE in delta X] > delta, X = X-bar (+) "
        "delta X), four lines of Section 2.4 (J^real_{S,K}, J^sim_{S,K}, tau > 0), two lines of its second paragraph (F(s_0;theta), "
        "delta X) and four lines of Section 3.1 (F(s_0;theta), sigma^sim_{s_0} := s_1,...,s_K, K, N, T_q, q in [N]). Compared with "
        "the 170 dpi render, a 260 dpi crop of the upper half and a 220 dpi crop of the lower half; all formulas match, in "
        "particular the '>= delta' of the flowpipe definition and the strict '> delta' in Lemma 3." + WORDS + "'Dreal', 'Dsim' "
        "(D^real_{S,K}, D^sim_{S,K}, nine fragments)." + SYM + " (64 symbols). The page has no number difference.",
    (7, "missing_lines"):
        "All 31 lines and line fragments contain math now written in LaTeX: the Figure 1 caption line (N, sigma^{sim,q}_{s_0}), the "
        "continuation 'sigma^{sim,q}_{s_0}, q in [N], defined as:', the fragments of display (8), the paragraph 'The key idea ...' "
        "(F_q(s_0;theta_q), X-bar_q, I, F_q(I;theta_q)), seven lines of the paragraph 'Here are the reasons ...', the paragraph "
        "'Once the surrogate flowpipes ...' (X-bar_q = <c-bar_q, V-bar^q, P-bar_q>, X-bar = <c-bar, V-bar, P-bar>, c-bar = "
        "[c-bar_1^T,...,c-bar_N^T]^T, V-bar = diag(V-bar^1,...,V-bar^N), P-bar = big-wedge_{q=1}^N P-bar_q), three lines of Section "
        "3.2 (x_i in R^n, i in [L], Sigma succeq 0, Sigma in R^{n x n}) and the first line of Footnote 4 (I). Compared with the 170 "
        "dpi render and a 240 dpi crop; (8) matches symbol by symbol including the printed index T_i." + WORDS + "none (the large "
        "wedge of 'P-bar = ...' appears as the letters 'VN' in the text layer)." + SYM + " (58 symbols).",
    (7, "number_differences"):
        MINUS + "the one '−1' is the upper limit q−1 of the sum t_q = sum_{l=1}^{q-1} T_l in display (8), read on the 240 dpi crop. "
        "The tag (8), t_1 = 0, the footnote mark 4 and the section number 3.2 are matched. No number is missing or changed.",
    (7, "independent_parser_number_differences"):
        "Identical to the first parser's difference: the upper limit q−1 of the sum in display (8), Unicode minus in the PDF and "
        "ASCII minus in the LaTeX. No number is missing or changed.",
    (8, "missing_lines"):
        "All 21 lines and line fragments contain math now written in LaTeX: two lines of the Figure 2 caption (K = 2, (R^1,R^2), "
        "delta in (0,1)), three lines of the following two paragraphs (rho, delta X, 'equation (5)'), the paragraph 'To obtain the "
        "principal axes ...' (sigma^sim_{s_{0,i}} in T^trn, i in [|T^trn|], q in [N], sigma^{sim,q}_{s_{0,i}}, F_q(s_{0,i};theta_q)), "
        "the fragments of displays (9) and (10) (the text layer shows the sums as 'P|T trn|'), and the last paragraph (Sigma^q, V^q "
        "in R^{T_q n x T_q n}, PE-bar^q, V^q_l, l in [T_q n]). Compared with the 170 dpi render and a 260 dpi crop of the lower "
        "third; (9) and (10) match symbol by symbol, including the missing index i in the second factor of (10)." + WORDS + "none."
        + SYM + " (37 symbols). The page has no number difference.",
    (9, "missing_lines"):
        "All 57 lines and line fragments contain math now written in LaTeX; the page is almost entirely mathematical: the first "
        "paragraph (s_0 ~ W, s_1..s_K, D^sim_{S,K}, PE^q = [R^{t_q n+1},...,R^{(t_q+T_q)n}]), display (11), the sentence with t_q n "
        "+ 1 <= j <= (t_q+T_q)n, display (12), 'where the scaling factors omega_j ...', display (13), the calibration paragraph "
        "(T^trn, V^q, PE-bar^q, omega_j, D^sim_{S,K}), Definition 4 with display (14) and its closing sentence, the paragraph "
        "'Consider sorting ...' (rho_i ~ J^sim, rho_1 < ... < rho_{|R^calib|}, rho ~ J^real, tau > 0, TV(J^real,J^sim) < tau, l*, "
        "rho*_{delta,tau} := rho_{l*}, Pr[rho < rho*_{delta,tau}] > delta), Proposition 5 with display (15) and its closing line. "
        "Compared with the 170 dpi render and three 280-300 dpi crops covering the whole text area; every display and inline "
        "formula matches symbol by symbol (strict '< tau', strict '> delta', non-strict '<=' inside (15))." + WORDS + "'Dsim' "
        "(D^sim_{S,K}, four fragments)." + SYM + " (121 symbols). After writing 't_q n + 1' with spaces the page has no number "
        "difference.",
    (10, "missing_lines"):
        "All 42 lines and line fragments contain math now written in LaTeX: the proof of Proposition 5 (rho, r^j, j in nK; display "
        "(16); Pr[rho <= rho*_{delta,tau}] >= delta, rho < rho*_{delta,tau} <=> |r^j| < rho*_{delta,tau} omega_j, the probability of "
        "the conjunction >= delta, T_q, q in [N]), the paragraph 'Referring to Def. 2 ...' (P_q(r^{t_q n+1},...,r^{(t_q+T_q)n}), "
        "delta X_q), display (17), the paragraph after it (delta X_q = <PE-bar^q, V^q, P_q(...)>, delta X = <PE-bar, V, P>, V = "
        "diag(V^1,...,V^N), P = big-wedge P_q), 'Finally ...' (delta-confident, X-bar, delta X, X = X-bar (+) delta X), three lines "
        "of Remark 6 (PE-bar^q, X-bar_q, V^q), five lines of Section 4 (sigma^real_{s_0} in D^real_{S,K}, TV(J^sim,J^real), tau, "
        "tau = 0, tau = 4%, K) and Footnote 5 (K = 2, n = 2, N = 2, T_1 = T_2 = 1). Compared with the 170 dpi render and three "
        "240-280 dpi crops covering the whole text area; (16) and (17) match symbol by symbol." + WORDS + "'vnk' (the large wedge "
        "with upper limit nK appears as 'VnK' in the text layer) and 'Dreal'." + SYM + " (87 symbols). After writing 'tau = 4%' with "
        "the percent sign outside the math the page has no number difference.",
    (11, "missing_lines"):
        "All 13 lines and line fragments contain math now written in LaTeX: three lines of Section 4.1 (v ~ N(0_{12x1}, Sigma_v), "
        "Sigma_v = diag([0.05 x 1-vec_{1x6}, 0.01 x 1-vec_{1x6]}]^2), s_0 ~ W), eight lines and fragments of Section 4.2 (v ~ "
        "N(0-vec_{27x1}, Sigma_v), Sigma_v = diag(10^{-5} x 1-vec_{1x27}), sigma^sim_{s_0} ~ D^sim_{S,K}, delta t = 0.0005, K = "
        "4000, I with footnote mark 6, N = 4000, T_q = 1, q in [N]) and the first line of Footnote 6 (I). Compared with the 170 dpi "
        "render, a 260 dpi crop of Sections 4.1-4.2 and a 500 dpi crop of the Sigma_v line (stray ']' in the subscript confirmed)."
        + WORDS + "'Dsim'." + SYM + " (27 symbols).",
    (11, "number_differences"):
        "No number is missing or changed; every difference is a tokenisation effect, checked on the 300 dpi crop of Table 1 and the "
        "260/500 dpi crops of Sections 4.1-4.2. (1) The six dataset sizes of Table 1 are printed in math mode with a gap after the "
        "comma ('42, 000', '20, 000' three times, '10, 000' twice): the PDF gives the tokens 42, 20 x3, 10 x2 and 000 x6, the CSV "
        "has '42,000', '20,000' x3, '10,000' x2. (2) Subscripted vectors: the PDF glyph runs '0 12x1', '0-vec 27x1' and '1-vec 1x6' "
        "(twice), '1-vec 1x27' are tokenised as 012, 027 and 11 x3, while the LaTeX $0_{12\\times1}$, $\\vec{0}_{27\\times1}$, "
        "$\\vec{1}_{1\\times6}$, $\\vec{1}_{1\\times27}$ gives 0, 12 / 0, 27 / 1, 1 (extra 0 x2, 12, 27 and six of the extra 1). (3) "
        + MINUS + "'−5' is the exponent of 10^{-5}. (4) The seventh extra '1' is the 'Table 1' named in the conversion-note item "
        "that follows the caption (not source text). All 30 data cells, 18 CPU workers, 0.05, 0.01, 0.0005, 4000, [27, 54, 27] and "
        "the six grant numbers are matched.",
    (11, "independent_parser_number_differences"):
        "Same causes as in the first parser's check (thousands printed with a gap; subscripted-vector glyph runs 012, 027, 11; "
        "Unicode minus in 10^{-5}; 'Table 1' in the conversion note). In addition the second parser (pypdf; its text for this page "
        "was inspected) splits six kerned table cells before the decimal point: '39 .6', '1 .43', '33 .65', '0 .030', '40 .6', '0 "
        ".064', which gives the missing tokens 39, 6, 43, 33, 65, 030, 40, 6, 064 and the extra tokens 39.6, 1.43, 33.65, 0.030, "
        "40.6, 0.064 (the '1' of '1 .43' cancels one of the extra 1). The six values were read on the 300 dpi crop of Table 1 and "
        "agree with the TeX tabular. No number is missing or changed.",
    (14, "missing_lines"):
        "All four lines contain math now written in LaTeX: two lines of the Figure 3 caption ('delta-confident flowpipes ... with "
        "delta = 99.99%', 'T^trn') and two lines of Section A.1 ('K = 100 time steps', 'delta t = 0.05', 'delta-confident', 'delta = "
        "99.99%'). Compared with the 170 dpi render." + WORDS + "none." + SYM + " (9 symbols). The page has no number difference "
        "(the percent signs are written outside the math).",
    (15, "missing_lines"):
        "All three lines are caption lines that contain math now written in LaTeX: two lines of the Figure 4 caption "
        "('delta-confident flowpipe', 'T^trn') and the first line of the Figure 5 caption ('delta-confident flowpipe on the first "
        "8', where the 8 is in math mode). Compared with the 170 dpi render and the 220 dpi crops of the figures with their "
        "captions." + WORDS + "none." + SYM + " (2 symbols). The page has no number difference; tick labels and legends lie inside "
        "the three figure crops.",
    (16, "missing_lines"):
        "All 14 lines and line fragments contain math now written in LaTeX: the first line of the page (N = 100, T_q = 1, q in "
        "[N]), two lines of Section A.2 (delta = 99.99%, N = 5000, T_q = 1, q in [N]; i in 50, 51, ..., 500, j in [10]), display "
        "(18), the line after it (F_{10i}, [12, 24, 12]) and the paragraph of Section A.3 in nine fragments (sigma^real_{s_0} ~ "
        "D^real_{S,K}, Sigma_v, tau = 0.04, TV(J^sim,J^real), tau, delta-confident, delta = 95%). Compared with the 170 dpi render "
        "and a 240 dpi crop; (18) matches symbol by symbol." + WORDS + "'Dreal'." + SYM + " (25 symbols).",
    (16, "number_differences"):
        MINUS + "the one '−0.1' is the term (1 − 0.1j) of display (18), read on the 240 dpi crop. All other numbers of the page (100, "
        "[12, 24, 12] twice, 1 KHz, 5-second, 5000, 500, 99.99%, 50, 51, 10, 0.1, 20%, 0.04, 95%, 8, tag (18)) are matched. No number "
        "is missing or changed.",
    (16, "independent_parser_number_differences"):
        "Same term as in the first parser's check, (1 − 0.1j) in display (18): the second parser (pypdf; text inspected) prints '(1− "
        "0.1j)' with a space after the minus, so its token is '0.1' where the LaTeX '(1-0.1j)' gives '-0.1'. No number is missing "
        "or changed.",
}

queue = json.loads((W / "review-aid/review-queue.json").read_text(encoding="utf-8"))
entries = []
for item in queue["sources"][0]["items"]:
    e = item.get("adjudication_entry")
    if not e:
        continue
    key = (e["page"], e["check"])
    assert key in REASON, f"no written reason for {key}"
    entries.append({"page": e["page"], "check": e["check"], "fingerprint": e["fingerprint"], "reason": REASON.pop(key)})
assert not REASON, f"reasons without a diagnostic: {list(REASON)}"
(D / "adjudications.json").write_text(json.dumps({"schema_version": 1, "entries": entries}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("wrote", len(entries), "adjudications")
