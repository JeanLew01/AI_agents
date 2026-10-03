#!/usr/bin/env python3
"""Copy every unresolved diagnostic's adjudication_entry from the review queue and attach the reason
written after checking that page against the renders. Fails if a diagnostic has no written reason."""
import json
from pathlib import Path

R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/hewing2019scenario-paper"
D = W / "documents/s001-hewing2019scenario"

REASON = {
    (1, "number_differences"):
        "No number of the cover sheet is missing. The five 'extra' tokens (0000, -0002, -2770, -4687, 1.0) all come from the one "
        "explicitly labelled conversion-note item that lists the hyperlink targets of the underlined cover-sheet entries "
        "(https://orcid.org/0000-0002-2770-4687 and http://rightsstatements.org/page/InC-NC/1.0/); these URLs are link annotations of the PDF "
        "(read with PyMuPDF), not printed text. Printed numbers (2020-04, the two DOIs, 4(2)) were compared with the 200 dpi render and match.",
    (1, "independent_parser_number_differences"):
        "Same five extra tokens as in the first parser's check, for the same reason: they are the digits of the ORCID URL and the '1.0' of "
        "the rights-statement URL in the labelled conversion-note item with the link targets taken from the PDF link annotations. Nothing "
        "printed on the cover sheet is missing; all printed numbers were compared with the 200 dpi render.",
    (2, "missing_lines"):
        "All 7 lines are lines of Section II-A that contain mathematics now written in LaTeX: display (1) (x(k+1) = Ax(k) + Bu(k) + "
        "\\bar{w}(k) + w(k)), 'with state x(k) ∈ R^n and input u(k) ∈ R^{n_u}', 'taking values in R^n', '\\bar{w}(k) ∈ \\bar{W}', 'times "
        "\\bar{N}', 'W = [w(0)^T, ..., w(\\bar{N})^T]^T ~ Q' and 'all of R^n'. The prose around the formulas was compared word by word with "
        "the 300 dpi crop of the lower right column and matches; the page has no number difference.",
    (3, "missing_lines"):
        "All 32 lines contain mathematics now written in LaTeX; none is plain prose. They are the displays (2a), (3a), (3b), the displays of "
        "Definitions 1 and 2, the subscripts 'x ∈ X ⊆ R^d' of the min in (4a)/(5a), (4b), (5b), fragments of (6), (7), (8), and text lines "
        "with inline symbols (X^j, U, R^{n_u}, \\bar{N}, \\bar{N} → ∞, N ≪ \\bar{N}, π_tube, R_k, R, X_δ, δ, I_s, δ^{(i)}, |I_s| = N_s − "
        "N_k, X_{δ^{(j)}}, 1 − β, N_s). Two of them are also lines ending in a line-wrap hyphen ('rele-', 'optimiza-'). Every line was "
        "compared with the 300 dpi crops of both columns; the words around the symbols match (a word-multiset comparison of the page against "
        "pdftotext shows no lost word), and a per-page count of relation/operator symbols (≤, ≥, ⊆, ∈, →, ∞, =, +, −, ≪, ∀, *, bars, δ, β, π) "
        "in the PDF text layer equals the count in the LaTeX.",
    (3, "number_differences"):
        "The four 'missing' tokens '−1' (Unicode minus) are the four printed 'd − 1': in the binomial coefficient and in the upper summation "
        "limit of (6), in the exponent of (7), and in '(d − 1) ln(2)' of (8). In the LaTeX they are written 'N_k + d - 1' twice (counted as "
        "the two extra '1') and 'd-1' twice (counted as the two extra '-1' with ASCII minus). All four checked on the 300 dpi crop; no "
        "number is missing or changed.",
    (3, "independent_parser_number_differences"):
        "The second parser reads the two 'd − 1' of (6) and (8) with a space after the minus and the exponent 'd−1' of (7) and the summation "
        "limit 'N_k+d−1' of (6) as '−1' with a Unicode minus; the LaTeX has 'd-1' with ASCII minus for these two (the two extra '-1'). "
        "Same four places as in the first parser's check, all verified on the 300 dpi crop; no number is missing or changed.",
    (4, "missing_lines"):
        "All 42 lines contain mathematics now written in LaTeX; none is plain prose. They are the displays (9a)-(9c), the display of "
        "Assumption 2, (10a), (10b), fragments of the MPC problem (11a)-(11g) (the PDF text layer breaks each of its lines into pieces "
        "such as 'lf(x(l)', 'i+1 = Ae(l)', 'NMPC'), (12), the implication of Assumption 4 and 'and Z_f ⊆ Z_∞, where Z_∞ = ∩_{k=1}^{\\bar{N}} "
        "Z_k' (the big intersection is a 'T' glyph in the text layer), the two pieces of the conditional density p(W_k), and text lines with "
        "inline symbols (1 − β, \\bar{w}_i = \\bar{w}(k+i), W_k = [w_0, ..., w_N], π_tube, R^j_{k+i}, N_s^{MPC}, e_i^{(l)}, Z_f, "
        "\\bar{w} ∈ \\bar{W}, π_f(z) ∈ V ∀z ∈ Z_f, R_k = R, 0 ≤ k ≤ \\bar{N}, k = 0, ..., \\bar{N}); two are also line-wrap-hyphen lines "
        "('input con-', 'invari-/ance'). Every line was compared with the 300 dpi crops of both columns; the surrounding words match (no "
        "lost word in the word-multiset comparison), and the per-page counts of ≤, ⊆, ⊂, ∈, ⇒, ∞, =, +, −, ⊖, ∀, *, bars and π in the PDF "
        "text layer equal the counts in the LaTeX.",
    (4, "number_differences"):
        "The four 'missing' tokens '−1' (Unicode minus) are the upper limits 'N−1' of the two sums (expected cost and (11a)), 'w(k−1)' in "
        "the conditional density p(W_k), and '{0, ..., N −1}' after (11g). The LaTeX writes them 'N-1' (three times) and 'k-1' with ASCII "
        "minus (the four extra '-1'). Checked on the 300 dpi crops; no number is missing or changed.",
    (4, "independent_parser_number_differences"):
        "Identical to the first parser's difference: the four printed '−1' with Unicode minus (two summation limits N−1, w(k−1), "
        "{0, ..., N−1}) are 'N-1' / 'k-1' with ASCII minus in the LaTeX. Checked on the 300 dpi crops; no number is missing or changed.",
    (5, "missing_lines"):
        "All 53 lines contain mathematics now written in LaTeX; none is plain prose. They are the pieces of the two proofs in which the "
        "text layer separates sub/superscripts from their base (v^*_{N-1}, π_f(z^*_N), \\bar{V}, \\bar{Z}, Z_i(k) = Z_{i-1}(k+1), "
        "A z^*_N + Bπ_f(z^*_N) + \\bar{w}(k+N+1) ∈ Z_f, R^j_k, Z_0(k) = ∩_{j=1}^{n_c}(X^j ⊖ R^j_k)), the lines of Section IV with W^{(i)}, "
        "E^{(i)}, e_k^{(i)}, R_k, I_s, 1 − β, the scaling problem and (13b), (14b), and lines with \\tilde{R}, α, α^*, X_δ, h^T e, "
        "H ∈ R^{n_hs × n}, ‖H e_k^{(i)}‖_∞. Several are also line-wrap-hyphen lines ('re-/cursive', 'sys-/tem', 'optimiza-/tion', "
        "'prob-/lem'). Every line was compared with the 300 dpi crops of both columns; the surrounding words match (no lost word in the "
        "word-multiset comparison), and the per-page counts of ≤, ≥, ∈, ∞, ×, =, +, −, >, norm bars, ⊖, ∼, *, tildes, bars, δ, β, α and π in "
        "the PDF text layer equal the counts in the LaTeX.",
    (5, "number_differences"):
        "The four 'missing' tokens '−1' (Unicode minus) are the subscripts in v^*_{N−1} (twice, in V^* and in \\bar{V}), Z_{i−1}(k+1) and "
        "w^{(i)}_{\\bar{N}−1}; the LaTeX writes 'N-1', 'i-1', '\\bar{N}-1' with ASCII minus (the four extra '-1'). The two 'missing' tokens "
        "'1' are 'x(k + 1)' and 'z(k + 1)' in the proof of Theorem 2, which the PDF text layer spaces out; the LaTeX writes 'x(k+1)' and "
        "'z(k+1)' (the two extra '+1'). Checked on the 300 dpi crop; no number is missing or changed.",
    (5, "independent_parser_number_differences"):
        "Identical to the first parser's difference: four '−1' with Unicode minus (v^*_{N−1} twice, Z_{i−1}, w_{\\bar{N}−1}) versus ASCII "
        "'-1' in the LaTeX, and 'x(k + 1)', 'z(k + 1)' with spaces versus 'x(k+1)', 'z(k+1)' in the LaTeX. Checked on the 300 dpi crop; no "
        "number is missing or changed.",
    (6, "missing_lines"):
        "All 28 lines contain mathematics now written in LaTeX; none is plain prose. They are Corollary 2's '1 − β the set {e | He ≤ b^*}', "
        "the pieces of (15b), the three occurrences of d = (n^2+n)/2 (the fraction is split over lines in the text layer), Corollary 3's set "
        "{e | (e − e_c^*)^T P^{*-1} (e − e_c^*) ≤ 1}, 'I_s', 'I_dis', the Section V lines with x = [p, v, θ, r]^T, θ, \\bar{N} = 200, "
        "W ∼ N(0, Σ^w), |u| ≤ u_max = 4, the displays (16), (17a), (17b) and the piecewise reference x_k^{ref}, the cost function line with "
        "x^{ref}_{k+i}, N_s^{MPC}, N = 30 with π_tube, R_k^{|p|,|v|}, and the first line of the Fig. 2 caption (p_ref = 1 for k ≤ 100). "
        "'picted in Figure (1) ...' is additionally the second half of the line-wrapped word 'de-picted'. Every line was compared with the "
        "300 dpi crops (and the 500 dpi zooms of (15a)/(15b) and Corollary 3); the surrounding words match (no lost word in the "
        "word-multiset comparison), and the per-page counts of ≤, ≥, ∈, =, +, −, >, ∼, ≈, ±, *, β, θ, π and % in the PDF text layer equal "
        "the counts in the reviewed text.",
    (6, "number_differences"):
        "Every difference is a notation difference, checked on the 300 dpi crops: '−1' three times (P^{*−1} in Corollary 3, [−1, 0, 0, 0]^T "
        "in the reference, p_ref = −1 in the Fig. 2 caption) is '-1' with ASCII minus in the LaTeX; '−0.08' in (17a) is '-0.08'; '90%' twice "
        "in (17a)/(17b) and '99.6%' are written '90\\%' and '99.6\\%' inside math, which the checker reads without the percent sign; "
        "'10−4' (R = 10^{-4}) gives '−4' versus '-4'; and '1 − 10−7' is read by the parser as '−10' and '−7' but is '1 - 10^{-7}' in the "
        "LaTeX ('10' and '-7'). No number is missing or changed.",
    (6, "independent_parser_number_differences"):
        "Same places as in the first parser's check, verified on the 300 dpi crops: three '−1' versus ASCII '-1' (P^{*−1}, [−1,0,0,0]^T, "
        "p_ref = −1); '90%' twice and '99.6%' versus '90\\%' / '99.6\\%' in math; '−4' versus '-4' in 10^{-4}; '−7' versus '-7' in "
        "10^{-7}. The second parser prints (17a) as '≥− 0.08' with a space, so it counts '0.08' twice where the LaTeX has '-0.08' once "
        "and '0.08' once (missing '0.08', extra '-0.08'). No number is missing or changed.",
    (7, "missing_lines"):
        "All 11 lines contain mathematics now written in LaTeX; none is plain prose: 'remove k = 820 samples to determine R_k^{θ_max}', "
        "'and R_k^{θ_min}', 'p_2 = 90% with β = 10^{-7}', five pieces of the appendix matrix equation (cos θ, M l cos θ, −g sin θ − d_M ..., "
        "(w/M) cos θ, u − d_p \\dot{p} − d_M(\\dot{p} + l \\dot{θ} cos θ) + M l \\dot{θ}^2 sin θ + w), the eigenvalue line "
        "λ = [1, 0.3672, 0.8617 ± 0.2788i]^T, and the two lines of K_{i,j} = 0.02^2 + 0.2^2 exp(−½(i − j)^2/10^2), i, j ∈ {1, ..., \\bar{N}}. "
        "Compared with the 300 dpi crops and the 500 dpi zoom of the appendix; the surrounding words match (no lost word in the "
        "word-multiset comparison). Table I, the 16 references and all remaining prose lines are found by the line check.",
    (7, "number_differences"):
        "Every difference is a notation difference, checked on the 500 dpi zoom of the appendix and the 300 dpi crop: 'p_2 = 90%' is "
        "'90\\%' in math (read without the percent sign: missing '90%', extra '90'); 'β = 10−7' is '10^{-7}' ('−7' with Unicode minus "
        "versus '-7'). The remaining tokens all belong to the covariance kernel of the appendix, which the text layer prints flattened as "
        "'0.022 + 0.22 exp(−1' / '2(i −j)2/102)': the LaTeX has 0.02^2 and 0.2^2 (missing '0.022', '0.22'; extra '0.02', '0.2' and two "
        "'2'), -\\frac{1}{2} (missing '−1', extra '1'), and /10^2 (missing '102'; extra '10' and one '2'). The other '102' of the page "
        "(vol. 102 in reference [8]) is present. No number is missing or changed; the values 820, 3, 20, 10000, 1, 10, 9.81, 0.1, 0.3672, 0.8617, 0.2788 and all "
        "reference numbers are matched.",
    (7, "independent_parser_number_differences"):
        "The second parser splits the kerned decimals of the Table I cells: it prints '99 .98%', '91 .2%' and '94 .33%' (seen in its raw "
        "text), hence missing '99', '98%', '91', '2%', '94', '33%' and extra '99.98%', '91.2%', '94.33%'; the CSV cells 99.98%, 91.2%, "
        "94.33% were checked on the 500 dpi zoom of the table and the first parser matches them. The rest is the same notation difference "
        "as in the first parser's check: 'p_2 = 90%' is '90\\%' in math; '10−7' versus '10^{-7}' ('−7' versus '-7'); '0.022', '0.22' and "
        "'/102' are 0.02^2, 0.2^2 and /10^2 in the covariance kernel (extra '0.02', '0.2', '10' and three '2'). No number is missing or changed.",
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
