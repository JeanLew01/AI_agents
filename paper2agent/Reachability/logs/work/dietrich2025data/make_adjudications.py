#!/usr/bin/env python3
"""Write adjudications.json from the current review queue. Reasons are keyed by (page, check);
the script refuses to run if the queue contains a diagnostic without a written reason, or if the
diagnostic payload no longer matches what was reviewed (EXPECT_* below)."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/dietrich2025data-paper"
D = W / "documents/s001-dietrich2025data"
ML, ND, IP = "missing_lines", "number_differences", "independent_parser_number_differences"
WORDS = (" The prose words of every listed line were checked against the 220 dpi page render and found, in order, in the page text "
         "(scripted word-sequence check; the lines that fail it do so only on math glyphs fused into pseudo-words or on line-wrap fragments, "
         "and were read individually). Every formula was compared with the authors' TeX after normalisation and the displays were compiled "
         "with pdflatex and compared with the page render.")
REASONS = {
 (1, ML): "All 12 lines are in the two paragraphs of Section II-A and display (1) and contain mathematics now written in LaTeX: $R = \\{\\Phi(t_1; t_0, x_0, d) : x_0 \\in X_0, d \\in D\\}$, $X_0 \\subseteq \\mathbb{R}^{n_x}$, $d : [t_0, t_1] \\rightarrow \\mathbb{R}^{n_d}$, $\\Phi : X_0 \\times D \\rightarrow \\mathbb{R}^{n_x}$, $\\hat{R}$, $\\mu_{X_0}$, $\\mu_D$, $\\Delta$, $\\delta^{(i)} = \\Phi(t_1; t_0, x_{0i}, d_i)$, the two i.i.d. sampling statements (three line fragments) and (1). Lines failing the word check: 'Rnx'/'Rnd' (fused $\\mathbb{R}^{n_x}$, $\\mathbb{R}^{n_d}$) and the wrap fragment 'spectively' of 'respectively'." + WORDS,
 (2, ML): "All 39 lines contain mathematics now written in LaTeX from the TeX source: the end of II-A ($g : \\mathbb{R}^{n_x} \\times \\mathbb{R}^{n_\\theta} \\rightarrow \\mathbb{R}$, $\\theta$); II-B ($\\delta^{(1)}, \\dots, \\delta^{(N)}$, $\\beta$, $\\mathbf{P}\\{V(\\hat{R}(\\theta)) > \\epsilon\\} \\leq \\beta$, $V(\\hat{R}(\\theta))$, $e$, $\\hat{e}$, $\\Delta$, displays (2), (3), (4), (5)); II-C ($\\mathrm{Vol} : \\mathbb{R}^{n_\\theta} \\rightarrow \\mathbb{R}_{\\geq 0}$, $R(\\theta)$, the three lines of program (6), the sample points); II-D ($\\epsilon$, twice); II-E ($\\beta$, $\\hat{e}$, $\\hat{k}$); Definition 1 with (7) and (8) ($\\beta \\in (0, 1]$ and the hats on $k$ read on the render); and the holdout-sample sentence of Section III ($\\delta_s^{(i)}$, $x_{0i}^s$, $d_i^s$, $\\mu_D$, $\\hat{R}(\\theta)$, $\\hat{k}$). The one line failing the word check has 'Rnx' and the wrap fragment 'parameteri-'." + WORDS,
 (3, ML): "All 34 lines contain mathematics now written in LaTeX from the TeX source: the three lines of the Figure 1 caption ($\\hat{R}(\\theta)$, three times); Theorem 1 ($\\beta \\in (0, 1)$, $\\hat{k}$, $\\hat{R}(\\theta)$) and display (9); the remark after it ($\\delta_s^{(1)}, \\dots, \\delta_s^{(M)}$, $\\beta$); the Computation paragraph ($e \\mapsto \\mathrm{Bin}(k, M, e)$, where the text layer shows the arrow as '7→'); the order-wise scaling paragraph ($\\overline{\\text{Bin}}(\\hat{k}, M, \\beta)$, $\\hat{k} = 0$, the bound $\\overline{\\text{Bin}}(0, M, \\beta) \\leq \\log(1/\\beta)/M$, $\\log(1/\\beta)$, $\\hat{k} > 0$) and display (10); $V(\\hat{R}(\\theta))$; the two sample sets $\\{\\delta_s^{(i)}\\}_{i=1}^{M}$, $\\{\\delta^{(i)}\\}_{i=1}^{N}$ and the tower-property display (three fragments); the exponent numerators of (11) and (12); and the volume-proxy sentence ($\\sqrt{\\sum_{i=1}^{m} \\sigma_i^2}$, $\\mu_i$, $k$-means). The one line failing the word check has the wrap fragment 'dence' of 'dependence'. Text inside the Figure 1 crop is excluded by the tool and was read on the crop." + WORDS,
 (3, ND): "Explained item by item on the page render. Missing '7': the text layer renders the arrow of $e \\mapsto \\mathrm{Bin}(k, M, e)$ as '7→'; there is no digit 7 there in print. Missing '−1' (twice) and two of the extra '1': the exponents of (11) and (12) are printed as a minus sign followed by the stacked fraction 1/2 (text layer '−1' above '2'), written '-\\frac{1}{2}' in LaTeX. The other two extra '1' and the extra '0' belong to the transcription of the text inside Figure 1 ('Figure 1' in its lead-in, 'i = 1' under the intersection sign, '\\leq 0'), whose PDF text lies inside the excluded image crop; they were read on the crop.",
 (3, IP): "Same causes as the first parser. Missing '7' is the '7→' rendering of \\mapsto in '$e \\mapsto \\mathrm{Bin}(k, M, e)$'. The extra '1' (twice) and '0' are 'Figure 1', 'i = 1' and '\\leq 0' in the transcription of the text inside Figure 1, whose PDF text is inside the excluded crop. pypdf extracts the exponents of (11) and (12) as '− 1' with a space (seen in its raw text), so they are not reported here.",
 (4, ML): "All 27 lines contain mathematics now written in LaTeX from the TeX source: $\\sigma_i$; $\\gamma = 0.25$; $\\beta = 10^{-9}$ and $\\epsilon$; the Duffing dynamics $\\ddot{x} = -\\alpha y + x - x^3 + \\gamma \\cos(\\omega t)$, its states and parameters, $\\alpha = 0.05, \\gamma = 0.4, \\omega = 1.3$, the initial intervals and $\\mu_{X_0}$; the Table I caption ($\\epsilon$) and the header cell Vol(R-hat(theta)); $\\epsilon = 0.018$, $\\epsilon = 0.035$, Vol = 1.55; the three lines of (13); $\\theta$ and $x, h, \\theta$ in the quadrotor paragraph; the two lines of the initial-state display; the input sentence ($u_2(t) = u_2$, $\\forall t \\in [t_0, t_1]$, $[-1.5 + g/K, 1.5 + g/K]$, $[-\\pi/4, \\pi/4]$, $\\mu_{X_0}$, $\\mu_D$); $\\epsilon = 0.051$, Vol = 27.80; and the Figure 2 caption ($\\epsilon$, $\\hat{e}$). All numeric values in these lines were read on the render and agree with the text and with Table I." + WORDS,
 (4, ND): "Formatting only; every value was read on the page render. Unicode minus in the PDF versus ASCII '-' in LaTeX: −9 ($\\beta = 10^{-9}$), −0.05 ($y(0) \\in [-0.05, 0.05]$), −1.7, −0.8, −1.0 (initial-state display), −1.5 ($u_1$ interval). '0,100' versus '0' and '100': the Duffing time range is printed '[0,100]' without a space, which the tool reads as one token; the text has '$[0, 100]$'.",
 (4, IP): "Same differences as the first parser: Unicode versus ASCII minus for −9, −0.05, −1.7, −0.8, −1.0, −1.5, and the time range '[0,100]' (one token in the PDF text, '[0, 100]' in the text). Values read on the page render; pypdf raw text checked for '[0,100]' and '10 −9'.",
 (5, ML): "All 20 lines contain mathematics now written in LaTeX from the TeX source: $\\epsilon = 0.0263$; the Table II caption ($\\epsilon$) and the header cell Vol(R-hat(theta)); the reachable-tube definition ($\\hat{\\mathcal{R}}(t)$, $\\forall t_i \\in [t_0, t]$, $X_0 \\subseteq \\mathbb{R}^{n_x}$, $d : [t_0, t] \\rightarrow \\mathbb{R}^{n_d}$, $\\Phi : \\mathbb{R} \\times X_0 \\times D \\rightarrow \\mathbb{R}^{n_x}$); five fragments of the unnumbered tube program; the 'where' sentence ($\\mu$, $\\sigma$, $\\lambda$, $\\gamma$, $\\delta$, $\\sigma_{avg}$, $\\sigma_i$); $\\dot{x} = Ax$; $[1, 1.25]$ and $\\mu_{X_0}$; $\\beta = 10^{-9}$; $\\epsilon = 0.144$; $\\lambda$. The three lines failing the word check have 'Rnx'/'Rnd'. All numeric values in these lines were read on the render." + WORDS,
 (5, ND): "Formatting only; every value was read on the page render. Unicode minus in the PDF versus ASCII '-' in LaTeX: −0.7 (twice) and −1.0 in matrix (14), −9 in $\\beta = 10^{-9}$. Missing '−1' and extra '1': the exponent of the tube program is printed as a minus sign followed by the stacked fraction 1/2 (text layer '−1' above '2'), written '-\\frac{1}{2}' in LaTeX.",
 (5, IP): "Unicode minus in the PDF versus ASCII '-' in LaTeX only: −0.7 (twice) and −1.0 in matrix (14), −9 in $\\beta = 10^{-9}$; values read on the page render. pypdf extracts the exponent of the tube program as '− 1' with a space (seen in its raw text), so that difference is not reported here.",
 (6, ML): "All 43 lines contain mathematics now written in LaTeX from the TeX source: Section V-A ($\\theta^{\\ast}$, $\\mathbf{P}\\{ g(\\theta^{\\ast}, x) \\le 0 \\} \\ge 1 - \\epsilon$, $\\gamma \\ge 0$, $g(\\theta^{\\ast}, x) \\le \\gamma$, $h(\\epsilon)$, $\\theta$, $(\\sup_x g(x, \\theta) - g(x, \\theta))$, $\\mathbf{P}\\{ g(\\theta^{\\ast}, x) \\le h(\\epsilon) \\} = 1$, $g$); Section V-B ($h : B_2^d \\mapsto \\mathbb{R}$ with the arrow shown as '7→' in the text layer, $B_2^d(r)$, $B_2^d(1)$, condition (b) display in three fragments, Lemma 1 in four fragments, the proof: $h_\\delta(x) := \\delta - L\\|x\\|_2$, the probability statement, the '=_{a.e.}' display, the volume identity, the two-line volume-ratio display, $\\delta_\\star := L\\varepsilon^{1/d}$ and the final maximum); the implication paragraph ($\\varepsilon$, $1/M$, $(L/\\gamma)^d$, $\\max_{x \\in B_2^d} h(x) \\leq \\gamma$); $(L/\\gamma)^d$ queries and $\\gamma$-sub-optimality; and the three lines of Footnote 1 ($\\ell_\\infty$, $\\ell_2$, $\\ell_p$ and the two Lipschitz inequalities; the footnote mark '1' is written $^{1}$ in the body and 'Footnote 1:' at the footnote). The lines failing the word check have 'supx', 'maxx' or 'rdVol' (fused subscripts/superscripts). Lemma 1, conditions (a)-(b) and every step of the proof were read symbol by symbol on the 220 dpi render." + WORDS,
 (6, ND): "Missing '7' (twice): the text layer renders the arrow \\mapsto as '7→' in '$h : B_2^d \\mapsto \\mathbb{R}$', once in the sentence before condition (b) and once in Lemma 1; no digit 7 is printed there (read on the render). No other number differs.",
 (6, IP): "Same cause as the first parser: pypdf joins the subscript 2 of $B_2^d$ with the '7→' rendering of \\mapsto into '27→' (twice, seen in its raw text: 'h:B d 27→R'), giving two missing '27' and two extra '2' (the subscripts, which are in the text as 'B_2^d'). No digit 7 is printed there.",
 (7, ND): "Line wrap only: the grant number is printed 'CNS-' at the end of one line and '2111688' at the start of the next; the text has 'CNS-2111688', which the tool reads as '-2111688'. Read on the page render and in the TeX source ('CNS-2111688').",
 (7, IP): "Same as the first parser: 'CNS-' / '2111688' across a line break in the PDF versus 'CNS-2111688' in the text (token '-2111688'). Read on the page render; pypdf raw text shows 'CNS-\\n2111688'.",
}
# Diagnostic payload sizes that were reviewed; a change means the page changed and must be re-reviewed.
EXPECT_ML = {1: 12, 2: 39, 3: 34, 4: 27, 5: 20, 6: 43, 7: 0}
EXPECT_ND = {
 3: {'missing': {'7': 1, '−1': 2}, 'extra': {'1': 4, '0': 1}},
 4: {'missing': {'−9': 1, '−0.05': 1, '0,100': 1, '−1.7': 1, '−0.8': 1, '−1.0': 1, '−1.5': 1}, 'extra': {'-9': 1, '0': 1, '-0.05': 1, '100': 1, '-1.7': 1, '-0.8': 1, '-1.0': 1, '-1.5': 1}},
 5: {'missing': {'−1': 1, '−0.7': 2, '−1.0': 1, '−9': 1}, 'extra': {'1': 1, '-0.7': 2, '-1.0': 1, '-9': 1}},
 6: {'missing': {'7': 2}, 'extra': {}},
 7: {'missing': {'2111688': 1}, 'extra': {'-2111688': 1}},
}
EXPECT_IP = {
 3: {'missing': {'7': 1}, 'extra': {'1': 2, '0': 1}},
 4: EXPECT_ND[4],
 5: {'missing': {'−0.7': 2, '−1.0': 1, '−9': 1}, 'extra': {'-0.7': 2, '-1.0': 1, '-9': 1}},
 6: {'missing': {'27': 2}, 'extra': {'2': 2}},
 7: EXPECT_ND[7],
}
EMPTY = {'missing': {}, 'extra': {}}
v = json.loads((D / "verification.json").read_text(encoding="utf-8"))
for p in v["pages"]:
    n = p["page"]
    assert len(p["missing_lines"]) == EXPECT_ML.get(n, 0), ("missing-line count changed", n, len(p["missing_lines"]))
    assert p["number_differences"] == EXPECT_ND.get(n, EMPTY), ("number diagnostics changed", n, p["number_differences"])
    assert p["independent_parser_number_differences"] == EXPECT_IP.get(n, EMPTY), ("independent diagnostics changed", n, p["independent_parser_number_differences"])
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
