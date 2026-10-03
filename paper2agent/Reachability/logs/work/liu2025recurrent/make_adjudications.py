#!/usr/bin/env python3
"""Write adjudications.json from the current review queue. Reasons are keyed by (page, check); the script
refuses to run if the queue holds a diagnostic without a written reason or if the reviewed payload sizes changed."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/liu2025recurrent-paper"
D = W / "documents/s001-liu2025recurrent"
ML, ND, IP = "missing_lines", "number_differences", "independent_parser_number_differences"
CHK = (" Scripted checks on this page (SCRATCH linecheck.py, charcheck.py, symbol_check3.py, wordcheck.py): after mapping the "
       "LaTeX back to the glyphs of the text layer, {lines}; the multiset of letters, digits and Greek letters of the text "
       "layer equals that of the markdown{chars}; the counts of <=, >=, subset, subseteq, in, notin, =, <, >, arrows, "
       "infinity, +, minus, norm bars, single bars, cup, cap, forall, exists, partial, primes, emptyset, hats, stars and "
       "Greek letters agree{syms}; no prose word is missing.")
ALL = "every text-layer line of the page is a substring of the page text"
REASONS = {
 (1, ML): "All 5 lines are prose lines containing inline math now written in LaTeX: '($\\tau$-) recurrent', '(within $\\tau$ units of time)', 'finite-time ($\\tau$)', '$\\tau$-backward reachable', and the Notation line with $\\|\\cdot\\|$, $\\mathbb{R}^n$, $x \\in \\mathbb{R}^n$. Each was read on the 170 dpi render of PDF page 1 and against main.tex; the surrounding words match."
          + CHK.format(lines=ALL, chars="", syms=""),
 (2, ML): "All 51 lines contain mathematics now written in LaTeX from main.tex: the closed ball and the signed-distance cases display, the definitions of $\\mathcal{X}$, $U$, $\\mathcal{U}^{(a,b]}$, $\\mathcal{U}$, the concatenation display, the restriction $u|_{(c,d]}$, $u_{[n]}$, $u_{[\\infty]}$, $\\phi(t,x,u)$, Assumptions 1-2 with the Lipschitz display, Section II-B, Definitions 1-3 with the $\\mathcal{R}_T(S)$ display, the value function, the HJI display, the Hamiltonian, the $T$-BRT sublevel-set display, $\\mathcal{R}^c_{+\\infty}(\\mathcal{X}_u)$ and the class-$\\mathcal{K}$ sentences. Every formula was compared symbol by symbol with four 250 dpi crops of PDF page 2 and with a pdflatex rendering of the transcription."
          + CHK.format(lines=ALL, chars="", syms=""),
 (3, ML): "All 35 lines contain mathematics now written in LaTeX from main.tex: Definition 4 ($\\kappa$, $\\mathcal{K}$), Definition 5 with display (2) and the Lie-derivative fraction, Theorem 1 with its set display and $h_{\\ge 0}$, the paragraph after it, the Section III lead ($h_{\\geq0}$), Definition 6 with displays (3) and (4), the paragraph after Figure 1 ($\\tau$-recurrent, $\\phi(t,x,u)$, $\\partial S$), Definition 7 with display (5) and $\\gamma:\\mathbb{R}\\to\\mathbb{R}_{>0}$, the sup/max convention sentence and display (6) with its three fragments. Compared with four 250 dpi crops of PDF page 3 and a pdflatex rendering."
          + CHK.format(lines=ALL, chars=" except one 'n', which is the text-layer code of the large left brace of the cases construct in (6) (line at x=371, y=634)", syms=""),
 (4, ML): "All 73 lines contain mathematics now written in LaTeX from main.tex: items (i), (ii) and the closing sentence of Theorem 2; its proof with display (7), the concatenation display $u_{[n]}$ (text layer split into four fragments around the restriction bars), $t^{\\ast}$, display (8), the last-exit-time argument with primes $t'$, $t''$, the contradiction display, the lim inf display and $d(S,x)$; Definition 8 with (9); (10); Theorem 3 with $\\hat h$, $\\hat D_0$, $\\hat c$, (11), the inline bound on $\\hat\\tau$ (three fraction fragments) and the two-line definition of $\\overline{\\delta}$, $\\underline{\\delta}$; and the last line with $\\mathcal{B}_r(x)$. Compared with four 250 dpi crops of PDF page 4 (hats, primes, overline/underline, subscripts) and a pdflatex rendering."
          + CHK.format(lines=ALL, chars="", syms=" (the four tall restriction bars of $u_n|_{(0,\\tau_n]}$ are drawn with an extension-font glyph that is not a '|' character in the text layer; read on the crop)"),
 (5, ML): "All 62 lines contain mathematics now written in LaTeX from main.tex: Lemma 1 with display (12); the paragraph before Theorem 4; Theorem 4 with (13), (14) and its proof (five unnumbered displays incl. the printed 're^{-Lt}' and 'R_{t*}(X_u)'); Theorem 5 with (15)-(20) (the text layer splits each $\\hat h_r^{\\pm}$ into two fragments) and its proof (arg max definitions of $t^{\\ast}$, $u^{\\ast}$ and the two inequality chains). Compared symbol by symbol with four 260 dpi crops of PDF page 5 and a pdflatex rendering."
          + CHK.format(lines=ALL, chars="", syms=""),
 (6, ML): "All 28 lines are prose lines of Sections V and VI that contain inline math now written in LaTeX ($S\\subset\\mathcal{X}$, $h=-\\mathrm{sd}(x,S)$, the cell family $\\mathcal{G}$ with its stacked sub/superscripts, $\\mathcal{G}_s$, $\\mathcal{G}_u$, $\\mathcal{C}_s$, $\\mathcal{C}_u$, $\\mathcal{R}_\\tau(\\cup\\mathcal{G}_u)$, $\\mathrm{SafetyCheck}$, $n_s$, $\\tau$, $[x_1,x_2]^T\\in\\mathbb{R}^2$, $x_3\\in[0,2\\pi]$, $u\\in[-1,1]$, the square root). The lines of the four algorithm boxes are excluded by the tool (image crops) and were compared separately with the 260 dpi crops. Compared with 260 dpi crops of PDF page 6 and a pdflatex rendering."
          + CHK.format(lines="every text-layer line (including those of the algorithm boxes, against the transcriptions) is a substring of the page text except the three fragments of the stacked '}_{i=1}^{|G|}' and 'cup_{i=1}^{|G|}', which the text layer orders superscript-first", chars=" except one 'p', which is the text-layer code of the radical sign (line at x=411, y=687)", syms=" (the text layer writes the two 'neq' as a combining slash plus '=')"),
 (6, ND): "Explained token by token with the tool's tokenizer. The 'extra' tokens are exactly the numbers of the four algorithm transcriptions (items p0006-alg1-text to p0006-alg4-text: printed line numbers 1-5, 1-8, 1-12, 1-4; the equation references (13), (14), (17), (20), each twice in Algorithm 1; the 0 arguments; 2r/3, r/3 and {-1,0,1} in Algorithm 4), whose PDF text lies inside the image crops and is therefore not counted on the PDF side; the computed multiset of those items equals the reported 'extra' multiset minus one '-1'. The remaining extra '-1' and the missing '−1' are the same number: 'u in [−1, 1]' is printed with a Unicode minus and written '$u \\in [-1,1]$' with an ASCII '-'. All values were read on the 260 dpi crops.",
 (6, IP): "Same payload as the first parser (identical fingerprint): the extra tokens are the numbers of the four algorithm transcriptions, whose PDF text is inside the excluded image crops (line numbers, the references (13), (14), (17), (20), the 0 arguments, 2r/3, r/3, {-1,0,1}); the pair extra '-1' / missing '−1' is 'u in [−1, 1]', Unicode minus in the PDF and ASCII '-' in LaTeX. All values were read on the 260 dpi crops.",
 (7, ML): "All 12 lines are prose or caption lines containing inline math now written in LaTeX: '$\\tau = 1$ s', the intersection ratio $(V_{BRT\\cap h'\\leq0}/V_{BRT})$ with '$\\beta=\\alpha=0.05$', the TABLE II caption parameters, '$x_3=\\pi$' in the Fig. 2 caption, '$\\tau\\to0$', the volume gap $(V_\\tau-V_{\\mathrm{BRT}})/V_{\\mathrm{BRT}}$, '$\\tau$–accuracy', the Fig. 3 caption ('$n_{\\mathrm{s}}=3000$, $r_{\\min}=0.370$') and two lines of Section VII with $\\tau$. Read on 260-300 dpi crops of PDF page 7; all numbers match (no number difference is reported for this page)."
          + CHK.format(lines=ALL, chars=" except 74 additional characters in the markdown, which are exactly the four sub-captions '(a) HJ Reachability', '(b) Recurrent Set Approximation', '(a) Volume Difference', '(b) Computation Time' that are inside the figure crops and are repeated in the caption items", syms=""),
 (8, ML): "All 28 lines belong to the Appendix (proof of Lemma 1) and contain mathematics now written in LaTeX from main.tex: the definition of $L_u$ with the two limits under max, the two-line display on $F$ and $g$, the Gronwall display, the arg min definitions of $x^{\\ast}$, $y^{\\ast}$ (with the calligraphic $\\mathcal{S}$), the Case 1-3 sentences and their three displays (incl. the unmatched '|' at the end of the third line of Case 3), $p^{\\ast}$ and the final inequality. Compared with three 260 dpi crops of PDF page 8 and a pdflatex rendering. The reference list on this page produces no diagnostic."
          + CHK.format(lines="every text-layer line of the page is a substring of the page text except 'Z t', the text-layer code of the integral sign with its upper limit", chars=" except one 'z', which is that integral-sign glyph", syms=""),
}
EXPECT_ML = {1: 5, 2: 51, 3: 35, 4: 73, 5: 62, 6: 28, 7: 12, 8: 28}
v = json.loads((D / "verification.json").read_text(encoding="utf-8"))
for p in v["pages"]:
    assert len(p["missing_lines"]) == EXPECT_ML.get(p["page"], 0), ("missing-line count changed", p["page"], len(p["missing_lines"]))
    if p["page"] != 6:
        assert not any(p[ND].values()) and not any(p[IP].values()), ("unexpected number difference", p["page"])
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
