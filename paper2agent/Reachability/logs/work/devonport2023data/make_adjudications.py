#!/usr/bin/env python3
"""Copy every unresolved diagnostic's adjudication_entry from the review queue and attach the reason
written after checking that page. Fails if a diagnostic has no written reason or a reason has no diagnostic."""
import json
from pathlib import Path

R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/devonport2023data-paper"
D = W / "documents/s001-devonport2023data"

WORDS = (" A word-level test of every missing line (all alphabetic words of 3+ letters must occur in the same order in the page text, "
         "line-wrap fragments allowed at line ends) leaves only math glyph strings unmatched: ")
SYM = " The per-page counts of relation/operator symbols and Greek letters in the PDF text layer equal those in the LaTeX"
MINUS = "The PDF text layer has the Unicode minus (U+2212) where the LaTeX has ASCII '-'; counts are equal: "
SAME = "Identical to the first parser's difference and checked the same way: "

REASON = {
    (2, "missing_lines"):
        "Both lines are prose lines of the second paragraph that contain the inline symbol R^n, now written $\\mathbb{R}^n$ ('...nomials defined with "
        "respect to measures on R^n: a single measure defines a family of' and '...ability distribution on R^n the level sets of Christoffel functions "
        "are known empirically'); both begin with the second half of a word hyphenated at the line end (poly-nomials, prob-ability). All words were "
        "compared with the 130 dpi render and are present; the page has no number difference.",
    (3, "missing_lines"):
        "All 15 lines are rows (or the symbol cell of a row) of the symbol list that contain mathematics now written in LaTeX: the symbol cells "
        "Phi(t1;t0,x0,d), R-hat_[t0,t1], M-hat_{m,sigma0}, kappa-hat^{-1}(x) (twice), and definition cells containing C (calligraphic), l(c,x), x ~ X, "
        "c ~ Q, r(c), r_Q, x_1..x_N, '<= m' (twice), sigma_0, mu and Sigma. Each of the 40 rows was compared with the 130 dpi render of the page; the "
        "definition words of every row are present." + WORDS + "none." + SYM + " (32 symbols).",
    (3, "number_differences"):
        MINUS + "the two '−1' are the exponents of the two rows 'kappa-hat^{-1}(x)' (polynomial and kernelized empirical inverse Christoffel function), "
        "written $\\hat{\\kappa}^{-1}(x)$. No number is missing or changed.",
    (3, "independent_parser_number_differences"):
        SAME + "the two exponents −1 of the two 'kappa-hat^{-1}(x)' rows (Unicode minus in the PDF, ASCII minus in LaTeX).",
    (4, "missing_lines"):
        "All 21 lines contain mathematics now written in LaTeX: 15 prose lines of Section 2.1 with inline symbols (Phi(t1;t0,x0,d), x(t0)=x0 in R^n, "
        "d:[t0,t1] -> R^w, [t0,t1], X_0, D, R_[t0,t1], P_X(A), A, B subsets of R^n, R-hat_[t0,t1], {x: p_X(x) != 0}), display (2.1), the four lines of "
        "Problem 1 (epsilon, delta in (0,1); X subset of R^n; x_1..x_N i.i.d. ~ X; c(epsilon,delta;x_1..x_N)) and display (2.2). Compared with the "
        "130 dpi render and 210 dpi crops of the page; (2.1) and (2.2) match symbol by symbol." + WORDS + "none." + SYM + " (35; the PDF encodes the "
        "'not equal' of p_X(x) != 0 as a slash plus '=').",
    (5, "missing_lines"):
        "All 36 lines contain mathematics now written in LaTeX: the two bullet items (12 lines; P_X(c(...)) >= 1-epsilon, 1-delta, P_X^N, A subset of X^N, "
        "x_1..x_N in A, P_X^N({x_1..x_N : ...}) >= 1-delta), the paragraph 'For brevity ...' (c(epsilon,delta;x_1..x_N), epsilon, delta), 17 lines of "
        "Section 2.2 with inline formulas (kappa(x) = 1/z_m(x)^T M_m^{-1} z_m(x), M_m = integral of z_m z_m^T dP_X, kappa(x)^{-1}, M-hat_m = (1/N) sum, "
        "N >= binom(n+m,n), M-hat_{m,sigma} = sigma^2 I + (1/N) sum, sigma^2 > 0, sigma^2 I), display (2.3) (two fragments) and the three lines on the dyadic sum and Z in R^{binom x N}, "
        "Z = [z_m(x_i) ... z_m(x_N)]. Compared with the 130 dpi render and a 210 dpi crop of Section 2.2; all formulas match the page (including the "
        "printed index i in z_m(x_i))." + WORDS + "'dpx' (dP_X(x))." + SYM + " except three centred dots of the printed ellipsis, written \\cdots.",
    (5, "number_differences"):
        MINUS + "the six '−1' are the exponents in M_m^{-1} (ratio defining kappa), 'M_m^{-1} exists', kappa(x)^{-1}, M_m^{-1} (inverse Christoffel "
        "function), and kappa-hat^{-1} and M-hat_{m,sigma}^{-1} in (2.3). Checked on the 210 dpi crop; no number is missing or changed.",
    (5, "independent_parser_number_differences"):
        SAME + "six exponents −1 in Section 2.2 and (2.3) with Unicode minus in the PDF and ASCII minus in the LaTeX.",
    (6, "missing_lines"):
        "All 21 lines contain mathematics now written in LaTeX: the fragments of displays (2.4), (2.5), (2.6) (the text layer breaks them into pieces "
        "such as 'sigma^2 I + 1', 'N ZZ^T -1 = sigma^-2', '0 I + Z^T Z'), the sentence 'This expression for M-hat_{m sigma} ...', the paragraph after "
        "(2.5) with sigma^2 = sigma_0^2/N, z_m(x_i)^T z_m(x_j), (Z^T Z)_ij, (Z^T z_m(x))_i, k: R^n x R^n -> R and the footnote mark 1, 'where K in "
        "R^{NxN} and k_D(x) in R^N are defined as', and the line 'mators of Support. Algorithms 3.1' (second line of the run-in Section 3 title, now the "
        "heading '3. Christoffel Function Estimators of Support' followed by the paragraph 'Algorithms 3.1 and 3.2 ...'). Compared with the 130 dpi "
        "render and a 210 dpi crop of the upper half; (2.4)-(2.7) match symbol by symbol." + WORDS + "none." + SYM + "; the three left arrows of the "
        "PDF text layer belong to the Algorithm 3.1 box (written \\gets in the transcription).",
    (6, "number_differences"):
        "Nothing is missing. " + MINUS + "six '−1' (two in (2.4), kappa-hat^{-1} and one inverse in (2.5), kappa^{-1} and one inverse in (2.6)) and "
        "three '−2' (sigma^{-2} in (2.4), sigma_0^{-2} twice in (2.5)). All other 'extra' tokens (2 x2, 1 x5, 0 x6, 3.1, 5, 4, +2, 40 and two more "
        "'-1') are exactly the number tokens of the Algorithm 3.1 transcription item, whose printed counterpart lies inside the retained image crop "
        "'algorithm-3-1' and is therefore excluded from the source count (verified by tokenising that item with the verifier's tokenizer: after "
        "subtracting it and the minus pairs nothing remains). The transcription was compared line by line with a 300 dpi crop of the box "
        "(5/epsilon, log 4/delta, binom(n+2m,n), log 40/epsilon).",
    (6, "independent_parser_number_differences"):
        SAME + "Unicode-minus exponents of (2.4)-(2.6) (six '−1', three '−2') and the number tokens of the Algorithm 3.1 transcription, whose "
        "printed text is inside the image crop; after subtracting both, no token remains.",
    (7, "missing_lines"):
        "All 19 lines contain mathematics now written in LaTeX: four lines of Remark 3.1 ((x_1..x_n) in R^n, x_1..x_s, s < n, R^s, R-hat_[t0,t1]), "
        "nine lines of Section 3.1 (c subset of X, C subset of 2^X, x_1..x_N, r(c) = E[l(c,X)], l: C x X -> R_+, P_X, r-hat(c) = (1/N) sum l(c,x_i), "
        "r(c) - r-hat(c)), the two lines of Lemma 3.2's statement, the two pieces of display (3.1) ('log 4' / 'delta + d log 40') and the closing line "
        "of the lemma, in two fragments ('and if r-hat(c) = 0, then P_X^N({x_1..x_N : r(c) <= epsilon}) >= 1 - delta'). Compared with the 130 dpi render and a 210 dpi "
        "crop of the lower half; (3.1) reads N >= (5/epsilon)(log(4/delta) + d log(40/epsilon)) on the crop." + WORDS + "'log' (twice; it is the "
        "LaTeX command \\log in (3.1))." + SYM + " (32). The page has no number difference.",
    (8, "missing_lines"):
        "All 38 lines contain mathematics now written in LaTeX: the two lines of Lemma 3.3 (g: R^n -> R, Pos(V) = {{x: g(x) >= 0}, g in V}), five "
        "lines and fragments of Theorem 3.4 ({x in X: C(x) <= alpha}, C(x) = z_m(x)^T M-hat^{-1}_{m,sigma0} z_m(x), alpha = max_i C(x_i), the PAC bound), 22 lines "
        "and line fragments of its proof (Pos(R[x]^n_{2m}), l(c,x) = 1{x not in c}, binom(n+2m,n) = d, r(c) = E[1{x not in c}] = 1 - P_X(c), "
        "r-hat(c) = sum 1{x_i not in c}, the two occurrences of N >= (5/epsilon)(log(4/delta) + binom log(40/epsilon)), the probability statement), "
        "and nine lines of Section 3.2's first paragraph (P, Q, C, r_Q = E[l(c,X)], r-hat_Q = E[(1/N) sum l(c,x_i)], c ~ Q, C_P, C_Q, c-bar_Q). "
        "Compared with the 130 dpi render and a 210 dpi crop of Lemma 3.3 / Theorem 3.4 / proof; all formulas match, including the printed absence "
        "of 1/N in r-hat(c) and the unbalanced braces of the probability statement." + WORDS + "'maxi' (max_i) and 'log' (four times, \\log)." + SYM + " (90).",
    (8, "number_differences"):
        MINUS + "the single '−1' is the exponent of M-hat^{-1}_{m,sigma0} in Theorem 3.4. The numbers of the sample-size bound in the proof (5, 4, 40, "
        "2 in n+2m; printed twice) are all matched. No number is missing or changed.",
    (8, "independent_parser_number_differences"):
        SAME + "the exponent −1 of M-hat^{-1}_{m,sigma0} in Theorem 3.4 (Unicode minus in the PDF, ASCII minus in LaTeX).",
    (9, "missing_lines"):
        "All 15 lines contain mathematics now written in LaTeX: three lines of Theorem 3.5's statement (C, w in W, l: C x X -> {0,1}, W_P, W_Q), the "
        "main line of display (3.2), three lines of the paragraph after it (D_ber(q||p) = q log(q/p) + (1-q) log((1-q)/(1-p)), x_1..x_N, delta, P, Q), "
        "five lines of the narrow paragraph beside the algorithm (c-bar_Q = {x: kappa^{-1}(x) <= eta}, r-hat_Q, C_Q, r_Q, r(c-bar_Q)), the first line "
        "of the unnumbered display of Theorem 3.6 and its two closing lines ('Thus, with confidence delta, ...', '... probability mass >= 1 - epsilon'). "
        "Compared with the 130 dpi render, a 220 dpi crop of the upper half and a 300 dpi crop of Theorem 3.6: (3.2) and the Theorem 3.6 display match "
        "symbol by symbol; 'with confidence delta' is printed so." + WORDS + "'dber', 'dkl' and 'log' (D_ber, D_KL, \\log)." + SYM + " once \\leq/\\geq "
        "and the eight \\gets of the algorithm transcription are counted.",
    (9, "number_differences"):
        "Nothing is missing. " + MINUS + "the one '−1' is the exponent in c-bar_Q = {x : kappa^{-1}(x) <= eta}. All other 'extra' tokens (0 x9, 1 x9, "
        "+1, 3.2, 2 x5, one more '-1', 3.8, 6, 3.7) are exactly the number tokens of the Algorithm 3.2 transcription item, whose printed counterpart "
        "lies inside the retained image crop 'algorithm-3-2' and is excluded from the source count (verified by tokenising that item with the "
        "verifier's tokenizer: after subtracting it and the minus pair nothing remains). The transcription was compared line by line with a 300 dpi "
        "crop of the box (epsilon_i <- (r-bar + (2/N) log(pi^2 i^2/(6 delta)))/(1 - F_1(1)), references (3.8) and (3.7)).",
    (9, "independent_parser_number_differences"):
        SAME + "one Unicode-minus exponent (kappa^{-1}) and the number tokens of the Algorithm 3.2 transcription, whose printed text is inside the "
        "image crop; after subtracting both, no token remains.",
    (10, "missing_lines"):
        "All 29 lines contain mathematics now written in LaTeX: three fragments of the termination remark (D_KL(N(0,(sigma_0^{-1} I + K^{-1})^{-1}) || "
        "N(0,K)) is o(N)), the two halves of display (3.3), four lines after it (x_1..x_N, y_1 = ... = y_N = 0, sigma_0^2, eta-sublevel, g_p), the "
        "fragments of (3.4) and (3.5), three lines between them (c-bar_Q = {x: E[g_q(x)^2] <= eta}, E[g_q(x)] = m_q(x) = 0, Var_{g_q}(x)), Lemma 3.7's "
        "statement line, fragments of (3.6) and (3.7), 'empirical stochastic risk r-hat_Q.', the two statement lines of Lemma 3.8, three fragments of "
        "(3.8), 'with confidence 1 - delta.' and the last line (r-hat_Q). Compared with the 130 dpi render and two 220 dpi crops (upper and lower "
        "half); (3.3)-(3.8) match symbol by symbol, including sigma_0^{-1} in the remark and sigma^2 I_N (no subscript 0) in (3.4)/(3.5)."
        + WORDS + "'dkl', 'dber', 'vargq' and 'log'." + SYM + " (81).",
    (10, "number_differences"):
        MINUS + "nine '−1' (sigma_0^{-1}, K^{-1} and the outer inverse in the termination remark; the inverse in (3.4); the inverse and kappa^{-1} in "
        "(3.5); kappa^{-1}(x_i) in (3.6); K^{-1} and the outer inverse in (3.8)) and one '−2' (sigma_0^{-2} in (3.8)). Each checked on the 220 dpi "
        "crops; no number is missing or changed.",
    (10, "independent_parser_number_differences"):
        SAME + "nine exponents −1 and one exponent −2 in the termination remark and in (3.4)-(3.8), Unicode minus in the PDF and ASCII minus in LaTeX.",
    (11, "missing_lines"):
        "All 28 lines contain mathematics now written in LaTeX: five lines of the first paragraph (r-bar, the root-finding equation D_ber(r-hat_Q||beta) "
        "- (D_KL(N(0,(K^{-1}+sigma_0^{-2} I)^{-1})||N(0,K)) + log((N+1)/delta))/N = 0, beta in [r-hat_Q, 1)), 'Finally, we relate ... r(c-bar_Q) to "
        "r_Q.', the three lines of Lemma 3.9 (r(c-bar_eta), r_Q, r(c-bar_Q) <= r_Q/(1-F_1(1)) ~ 3.15 r_Q), 13 lines and fragments of the proof of "
        "Theorem 3.6 (epsilon^0 <- 1, C_Q^i, g_Q^i(x) ~ N(0, k(x,x) - k_{D^i}(x)^T(sigma_0^2 I + K^i)k_{D^i}(x)), r_Q^i, the two probability bounds with "
        "6 delta/(pi^2 i^2), the final inequality), the second line of the Section 3.3 title ('the Polynomial Case. With the gen-', now heading + "
        "paragraph), two lines of the Section 3.3 paragraph (z_m(x)^T z_m(y), N x N), the two lines of (3.9) and 'W_Q^T z_m are'. Compared with the "
        "130 dpi render and a 220 dpi crop of the upper half; all formulas match, including the printed '(sigma_0^2 I + K^i)' without inverse and the "
        "constant 3.15." + WORDS + "'dber', 'dkl', 'log', 'kdi' (k_{D^i})." + SYM + " once \\leq/\\geq and the \\gets of the algorithm transcription and "
        "of the proof are counted.",
    (11, "number_differences"):
        "Nothing is missing. " + MINUS + "three '−1' (K^{-1} and the outer inverse in the root-finding equation, M-hat^{-1}_{m,sigma0} in W_Q ~ N(0, "
        "M-hat^{-1})) and two '−2' (sigma_0^{-2} in the root-finding equation and in W_P ~ N(0, sigma_0^{-2} I)). All other 'extra' tokens (0 x7, 1 x9, "
        "2 x4, +1, one more '-1', 6, 3.7, 3.3, 3.11) are exactly the number tokens of the Algorithm 3.3 transcription item, whose printed counterpart "
        "lies inside the retained image crop 'algorithm-3-3' and is excluded from the source count (verified by tokenising that item with the "
        "verifier's tokenizer: after subtracting it and the minus pairs nothing remains). The transcription was compared line by line with a 300 dpi "
        "crop of the box. The printed constants 3.15, 6 delta/(pi^2 i^2) and the lemma numbers 3.7, 3.8, 3.9 of the page are matched.",
    (11, "independent_parser_number_differences"):
        SAME + "three exponents −1 and two exponents −2 with Unicode minus in the PDF, plus the number tokens of the Algorithm 3.3 transcription, "
        "whose printed text is inside the image crop; after subtracting both, no token remains.",
    (12, "missing_lines"):
        "All 26 lines contain mathematics now written in LaTeX: five lines at the top (the fragment 'z_m(x)^T z_m(y), conditioned on the obser-', which "
        "completes the inline formula of page 11 and is transcribed there, 'vations x_1..x_N, y_1 = ... = y_N = 0', sigma_0^2, c-bar_Q, C_Q, "
        "eta-sublevel set), the fragments of (3.10), 'that is the eta-sublevel set ...', the two statement lines of Lemma 3.10, the fragments of "
        "(3.11), five lines of Remark 3.12 (eta, k(x,y) = exp(-||x-y||^2/(2l)^2), eta = binom(n+2m,n)/epsilon, the binom/epsilon-level subset), three "
        "lines of Section 3.4 (kappa^{-1}(x), N x N, O(N^3), rank-r) and the two pieces of (3.12). Compared with the 130 dpi render and a 220 dpi crop "
        "of the upper half; (3.10), (3.11), (3.12) match symbol by symbol; in (3.11) the crop shows (sigma_0^2 I + M-hat_{m,sigma0})^{-1} and "
        "N(0, sigma_0^{-2} I)." + WORDS + "'dber', 'dkl', 'log', 'exp', 'knrk', 'knr' (K_{Nr} K_{rr}^{-1} K_{Nr})." + SYM + " (57).",
    (12, "number_differences"):
        MINUS + "five '−1' (M-hat^{-1}_{m,sigma0} in (3.10); the inverse of (sigma_0^2 I + M-hat) in (3.11); kappa^{-1}(x) twice in Section 3.4; "
        "K_{rr}^{-1} in (3.12)) and one '−2' (sigma_0^{-2} in (3.11)). The positive exponent in 'sigma_0^2 I' of (3.11) was read on the 220 dpi crop. "
        "No number is missing or changed.",
    (12, "independent_parser_number_differences"):
        SAME + "five exponents −1 and one exponent −2 in (3.10)-(3.12) and Section 3.4, Unicode minus in the PDF and ASCII minus in LaTeX.",
    (13, "missing_lines"):
        "All 31 lines contain mathematics now written in LaTeX: three lines at the top (K_{Nr} in R^{Nxr}, K_{rr} in R^{rxr}, k(x_i,x_j), K -> K-tilde "
        "[the mapsto arrow is the glyph pair '7->' in the text layer], kappa^{-1}(x)), the four fragments of (3.13), two lines after it (r x r, N x N), "
        "the line with Z_0 ~ N(mu_0,Sigma_0), Z_1 ~ N(mu_1,Sigma_1), the fragments of (3.14), 'For Sigma_0 = (sigma_0^{-2} I + K^{-1})^{-1}, ...', the "
        "fragment of (3.15), four lines after it (log(1+sigma_0^{-2}x), 1/(1+sigma_0^{-2}x), x >= 0, lambda_1..lambda_N), the fragment of (3.16), three "
        "lines of the next paragraph (N x N, lambda_p, p^th, lambda_i ~ lambda_p, lambda_i < lambda_p) and six lines of Section 4 (epsilon = 0.1, "
        "delta = 10^{-9}, k(x,y), m and l, eta = 0.15, eta = binom(n+2m,n)/epsilon). Compared with the 130 dpi render and 210/220 dpi crops of both "
        "halves; (3.13)-(3.16) match symbol by symbol, including the unclosed '(I -' of (3.13)." + WORDS + "'knr', 'krr', 'knrkd', 'krnknr', 'dkl', "
        "'log', 'det', 'pth', 'lused' (the script l run together with 'used')." + SYM + " (the one extra arrow in the PDF is the mapsto glyph).",
    (13, "number_differences"):
        "No number is missing. (1) " + MINUS + "nine '−1', eight '−2' (exponents in (3.13)-(3.16) and in the text between them) and '−9' (delta = "
        "10^{-9}). (2) The 'missing' 7 is the first glyph of the mapsto arrow in 'K 7-> K-tilde' (written \\mapsto). (3) The thousands printed in math "
        "mode with a gap after the comma, '20, 000', '5, 000', '1, 000', are tokenised in the PDF as 20/000, 5/000, 1/000 (missing 20, 5, 1, 000 x3) "
        "and are written 20,000, 5,000, 1,000 (the three extra tokens). All values checked on the 210 dpi crop of Section 4 (20 CPUs, 2.3 GHz, 128 GB, "
        "0.1, 10^{-9}, 0.15, 20,000, 5,000, 1,000).",
    (13, "independent_parser_number_differences"):
        "Same causes as in the first parser's check (Unicode minus exponents, the thousands '20, 000', '5, 000', '1, 000' printed with a gap). The "
        "second parser (pypdf, text inspected) prints one of the '−1' as '− 1' with a space, which gives 'missing 1' twice instead of once and "
        "'missing −1' eight times instead of nine, and it does not produce the stray 7 of the mapsto glyph. No number is missing or changed.",
    (14, "missing_lines"):
        "All 15 lines contain mathematics now written in LaTeX: two lines of the Table 1 caption (k(x,y) = exp(-||x-y||^2/(2l)^2), m, l, epsilon = "
        "0.1, delta = 10^{-9}), eight lines of the narrow first paragraph of Section 4.1 (z-dot = y, y-dot = -alpha y + z - z^3 + gamma cos(omega t), "
        "x = (z,y) in R^2, alpha, gamma, omega, 0.05, 0.4, 1.3, z(0) in [0.95,1.05], y(0) in [-0.05,0.05], X_0), three lines of the second paragraph "
        "(epsilon = 0.10, delta = 10^{-9}, k(x,y) = exp(||x-y||^2/(2 l^2)) with l = 0.25) and two lines of Section 4.2 (the inline quadrotor dynamics, "
        "p_x, p_h). Compared with the 130 dpi render and a 250 dpi crop of the table and caption; the kernel of the second paragraph is printed "
        "without minus sign and with 2 l^2." + WORDS + "'exp', 'cos', 'sin' (LaTeX commands) and 'las' (script l run together with 'as')." + SYM + " (65).",
    (14, "number_differences"):
        "No number is missing. (1) " + MINUS + "'−9' twice (delta = 10^{-9} in the caption and in Section 4.1) and '−0.05' (y(0) in [-0.05, 0.05]). "
        "(2) '11, 000' is printed in math mode with a gap (PDF tokens 11 and 000) and written 11,000. (3) The extra 3.1, 3.3, 3.2 (three each): the "
        "group headers 'Alg. 3.1', 'Alg. 3.3', 'Alg. 3.2' are printed once each above three columns; in the CSV each is repeated in its three "
        "combined column names (two extra each) and the conversion note in the caption item names them once more (one extra each). All 27 data cells "
        "of Table 1 were read on the 250 dpi crop, and 70307 / 14587 were reproduced from the sample-size formula of Algorithm 3.1.",
    (14, "independent_parser_number_differences"):
        SAME + "Unicode minus in 10^{-9} (twice) and -0.05; '11, 000' printed with a gap; the Table 1 group headers 'Alg. 3.1/3.3/3.2' repeated in "
        "the combined CSV column names and named once in the caption's conversion note.",
    (15, "missing_lines"):
        "All 7 lines contain mathematics now written in LaTeX: six lines of the Section 4.2 paragraph (theta = 0, x, h, theta; p_x(0) in [-1.7,1.7], "
        "p_x-dot(0) in [-0.8,0.8]; p_h(0) in [0.3,2.0], p_h-dot(0) in [-1.0,1.0], theta(0) in [-pi/12,pi/12]; u_1(t) = u_1, u_2(t) = u_2 for all t in "
        "[t0,t1]; u_1 in [-1.5+g/L, 1.5+g/L], u_2 in [-pi/4,pi/4]; [t0,t1] = [0,5]) and one line of Section 4.3 (x_1..x_n). Every interval bound was "
        "compared with the 130 dpi render and a 210 dpi crop of the paragraph." + WORDS + "none." + SYM + " (46).",
    (15, "number_differences"):
        "No number is missing. " + MINUS + "−1.7, −0.8, −1.0, −1.5 (lower bounds of the initial-state and input intervals) and −9 (delta = 10^{-9}). "
        "The caption of Fig. 2 prints 'm = 10, 000' in math mode with a gap (PDF tokens 10 and 000); it is written $m=10,000$ (extra token 10,000). "
        "All checked on the 210 dpi crop and the 130 dpi render.",
    (15, "independent_parser_number_differences"):
        SAME + "four negative interval bounds and 10^{-9} with Unicode minus; 'm = 10, 000' in the Fig. 2 caption printed with a gap.",
    (16, "missing_lines"):
        "All 10 lines contain mathematics now written in LaTeX: the five fragments of display (4.1), four lines of the paragraph after it (x-bar, w, "
        "w = 1/6, x-bar = 320, x_i(0) in [100,200], i = 1..n, d in [40/T,60/T], X_0, D) and 'parameters epsilon = 0.10, delta = 10^{-9}.'. Compared "
        "with the 130 dpi render and a 230 dpi crop of the upper part; (4.1) matches symbol by symbol, including the extra closing parenthesis and "
        "the '/beta' of its last line." + WORDS + "'min' (LaTeX command) and 'vxi', 'vxn' (v x_i, v x_n)." + SYM + " (34).",
    (16, "number_differences"):
        "No number is missing. " + MINUS + "three '−1' (x_{i-1}, 'n - 1' and x_{n-1} in (4.1)) and '−9' (delta = 10^{-9}). The caption of Fig. 3 "
        "prints 'm = 10, 000' in math mode with a gap (PDF tokens 10 and 000); it is written $m=10,000$. Parameters 30, 0.5, 1/6, 320, [100, 200], "
        "40/T, 60/T, 4T, 0.10, 2000 checked on the 230 dpi crop and the 130 dpi render.",
    (16, "independent_parser_number_differences"):
        "Same causes as in the first parser's check (three '−1' of (4.1), 10^{-9}, 'm = 10, 000' printed with a gap). In addition the second parser "
        "(pypdf, text inspected) prints 'epsilon = 0 .10' with a space inside the number, which gives missing 0 and 10 and extra 0.10, and prints "
        "'n − 1' with a space, which gives missing 1 instead of −1. No number is missing or changed.",
    (18, "missing_lines"):
        "All 9 lines are lines of Appendix A that contain inline mathematics now written in LaTeX: (g(x_1),...,g(x_m)), m(x) = E[g(x)], k(x,y) = "
        "E[g(x)g(y)], x,y in X, b_1..b_m: X -> R, sum_{i=1}^m w_i b_i, w = (w_1..w_m) ~ N(0,Sigma), k(x,y) = sum_{i=1}^m b(x)^T Sigma b(y), b(.) = "
        "(b_1(.),...,b_m(.))^T, g(x_i) = h_i + epsilon, sigma^2. Compared with the 130 dpi render and a 210 dpi crop of the appendix; all formulas "
        "match (including the printed summation sign in the covariance)." + WORDS + "'wibi' (w_i b_i)." + SYM + " (18). The page has no number "
        "difference; the 15 reference entries [20]-[34] on this page are fully matched.",
    (19, "missing_lines"):
        "All 32 lines contain mathematics now written in LaTeX: the fragments of (A.1)-(A.4), six lines after them (B in R m x N, B = [b(x_1) ... "
        "b(x_N)], b = z_k, Sigma = sigma_0^{-2} I, sigma = N^{-1/2}, the posterior-variance formula, x_1..x_n), six lines of the proof of Lemma 3.7 "
        "(kappa^{-1}(x), g_p(x) ~ N(0,kappa^{-1}(x)), chi^2_1) and two fragments of (B.1), and in the proof of Lemma 3.10 the fragments of W_Q ~ "
        "N(0,(sigma_0^{-2} I + M-hat)^{-1}), display (B.2), the definition of gamma (four fragments) and seven following lines (D_ber(r-hat_Q||r_Q) <= gamma, "
        "{beta: D_ber(r-hat_Q||beta) <= gamma}, [0,infinity), beta -> 0, beta -> 1, (0,1), r-bar, 1 - delta, r_Q). Compared with the 130 dpi render "
        "and two 220 dpi crops; all displays match symbol by symbol, including sigma^2 BB^T in (A.3), b(x) at the end of (A.4), '1{x in C_Q}' in (B.1) "
        "and the exponents -2 (text) versus +2 (gamma) of sigma_0 in the proof of Lemma 3.10." + WORDS + "'vargq', 'dber', 'dkl', 'log'." + SYM +
        " except three centred dots of the printed ellipsis, written \\cdots.",
    (19, "number_differences"):
        MINUS + "eighteen '−1' (the inverses in (A.1), (A.2): two; Sigma^{-1} and the outer inverse in each of (A.3), (A.4): four; N^{-1/2} and the inverse of "
        "the posterior-variance formula: two; kappa^{-1}(x) in the text of the proof of Lemma 3.7: five, and in (B.1): three; the inverses in W_Q "
        "and in gamma: two) and six '−2' (sigma^{-2} in (A.3) and (A.4), sigma_0^{-2} in "
        "'Sigma = sigma_0^{-2} I', in W_P, in W_Q and in gamma). The chi-square symbol is "
        "written $\\chi_1^2$ so that its digits are tokenised as in the PDF. Each exponent was checked on the 220 dpi crops; no number is missing or changed.",
    (19, "independent_parser_number_differences"):
        SAME + "eighteen exponents −1 and six exponents −2 of Appendix A and of the proofs of Lemmas 3.7 and 3.10, Unicode minus in the PDF and "
        "ASCII minus in LaTeX.",
    (20, "missing_lines"):
        "All 35 lines contain mathematics now written in LaTeX: five lines of the proof of Lemma 3.8 (g_q, x_1..x_N, (g_p(x_1),...,g_p(x_N)), "
        "(g_q(x_1),...,g_q(x_N)), K_p(X,X) = K(X,X)), two fragments of (B.3), four lines of the proof of Lemma 3.9 (x in X, c-bar_eta(x) = E[(g(x)^2] "
        "> eta, W_Q^T z_m(x)), the fragments of (B.4), three lines after it (r_Q = P((g(X)^2 > eta), eta), the fragments of (B.5)-(B.7), the two "
        "fragments of the inline inequality 'We have that ...', the fragments of (B.8)-(B.11) and the last line (r(c-bar_eta) <= r_{Q_eta}/(1-F_1(1))). "
        "Compared with the 130 dpi render and two 220 dpi crops; (B.3)-(B.11) match symbol by symbol, including the unmatched '(' in every '(g(x)^2', "
        "'dP_x(x)' with lower-case subscript and r(c-hat_eta) in (B.11)." + WORDS + "'dpx' (dP_x(x), five lines)." + SYM + " (78).",
    (20, "number_differences"):
        MINUS + "three '−1' (the two inverses of the first line of (B.3) and of K(X,X)^{-1}, and the outer inverse of its second line) and one '−2' "
        "(sigma_0^{-2} in (B.3)). Checked on the 220 dpi crop of the upper half; the equation tags (B.3)-(B.11) and all other numbers are matched.",
    (20, "independent_parser_number_differences"):
        SAME + "three exponents −1 and one exponent −2 in (B.3), Unicode minus in the PDF and ASCII minus in LaTeX.",
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
