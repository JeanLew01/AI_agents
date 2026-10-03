#!/usr/bin/env python3
"""Write adjudications.json from the current review queue. Reasons are keyed by (page, check);
the script refuses to run if the queue contains a diagnostic without a written reason, or if the
diagnostic payload no longer matches what was reviewed (EXPECT below)."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/lin2024verification-paper"
D = W / "documents/s001-lin2024verification"
ML, ND, IP = "missing_lines", "number_differences", "independent_parser_number_differences"
WORDS = (" Every listed line was read; the prose words of each line were found, in order, in the page text (linecheck.py) "
         "and a per-page word-multiset comparison with pdftotext (wordcheck.py) shows no prose word lost; the mathematics "
         "was compared with 200-220 dpi crops of the page and with the authors' TeX source.")
MINUS = "Sign glyph only: the PDF text layer uses the Unicode minus (U+2212) and the LaTeX transcription the ASCII hyphen-minus. "
REASONS = {
 (3, ML): "All 28 lines contain inline or display mathematics now written in LaTeX: the system definition ($x \\in X \\subseteq \\mathbb{R}^n$, $\\xi_{x,t}^{u}(\\tau)$, $[t, T]$, $\\mathcal{L}$), the Dubins-car running example (the three dynamics equations, the collision set with $\\min\\{d(Q_1,Q_2),\\dots\\} \\le R$), the set definition of BRT, the goal $\\underset{x\\in\\mathcal{S}}{\\mathbb{P}}(x \\in \\text{BRT}) \\le \\epsilon$ and its reach variant with $\\text{BRT}^C$, the target function $l(x)$, the cost $J_{u(\\cdot)}(x,t)$, the fragment 'Ju(·)(x, t)' of display (1), and the last line 'BRT = {x : x ∈', whose formula is completed here with the glyphs printed at the top of page 4." + WORDS,
 (3, ND): MINUS + "Missing '−1.1' / extra '-1.1' is $u_{\\min}=-1.1$ in the running example. The two extra '0' are the end of the split inline formula $\\text{BRT} = \\{x: x\\in X, V(x,0) \\le 0\\}$: 'X, V(x, 0) ≤ 0}' is printed at the top of page 4 and was transcribed on this page to keep one LaTeX expression (page 4 reports the same two '0' as missing). All values read on the 200 dpi crop.",
 (3, IP): MINUS + "Same payload as the first parser: '−1.1' in $u_{\\min}=-1.1$; the two extra '0' belong to 'X, V(x, 0) ≤ 0}', printed at the top of page 4 and transcribed here to complete the split formula. Read on the 200 dpi crop.",
 (4, ML): "All 15 lines contain inline mathematics now written in LaTeX. The first line starts with 'X, V (x, 0) ≤ 0}', the end of the formula begun on page 3, which is transcribed on page 3; the others contain $D_t$, $\\nabla$, the Hamiltonian $H(x,t) = \\max_u \\langle \\nabla V(x,t), f(x,u)\\rangle$, the controller $u^{\\ast}(x,t) = \\arg\\max_u\\langle\\cdot\\rangle$, $\\mathcal{L}$, $\\tilde{V}(x,t)$, $\\tilde{\\pi}(x,t)$ and the definition $\\delta_{\\tilde{V},\\tilde{\\pi}} := \\max_{x\\in X}\\{\\tilde{V}(x,0): J_{\\tilde{\\pi}}(x,0) \\le 0\\}$ (three occurrences of the symbol)." + WORDS,
 (4, ND): "The two missing '0' are 'X, V (x, 0) ≤ 0}' at the top of this page: the end of the inline formula BRT = {x : x ∈ X, V(x,0) ≤ 0} that starts on page 3. It is transcribed on page 3 (which reports two extra '0'), and this page's first item starts after it. Read on the 200 dpi crop; no other number differs.",
 (4, IP): "Same as the first parser: the two missing '0' are in 'X, V (x, 0) ≤ 0}' at the top of the page, transcribed at the end of page 3 to keep the split formula in one piece. No other number differs.",
 (5, ML): "All 28 lines contain mathematics now written in LaTeX: $\\mathcal{L}$, $\\mathcal{S} \\subseteq X$, super-$\\delta$ level sets of $\\tilde{V}(x,0)$, $\\delta > 0$, $x_{1:N}$, $\\mathbb{P}$, $J_{\\tilde{\\pi}}(x_i,0)$, $i=1, 2, ..., N$, the statement of Theorem 2 with fragments of displays (2) ('ϵi(1 −ϵ)N−i ≤β') and (3) ('x∈S (V (x, 0) ≤0) ≤ϵ'), and the discussion of $\\epsilon$, $\\beta$, $k$, $N$, $10^{-16}$ and $1-\\beta$. Displays (2) and (3) were checked symbol by symbol on a 200 dpi crop and compiled with pdflatex." + WORDS,
 (5, ND): MINUS + "The only difference is the exponent of $10^{-16}$ ('such as 10−16'); read on the 200 dpi crop.",
 (5, IP): MINUS + "Same as the first parser: the exponent of $10^{-16}$; read on the 200 dpi crop.",
 (6, ML): "All 9 lines contain inline mathematics now written in LaTeX: $\\beta = 10^{-16}$ and $\\beta$ in the first paragraph; $\\tilde{V}(x,0)$, $\\epsilon$, $k$ and $\\mathcal{S}$ in the Figure 1 caption; $\\epsilon$, $k$ and $\\mathcal{S}$ in the 'Firstly' paragraph; $\\epsilon$, $\\tilde{V}(x,0)$ and $N$ in the Figure 2 caption." + WORDS,
 (6, ND): MINUS + "The only difference is the exponent of $\\beta = 10^{-16}$ in the first paragraph; read on the page render.",
 (6, IP): MINUS + "Same as the first parser: the exponent of $\\beta = 10^{-16}$.",
 (7, ML): "All 18 lines contain mathematics now written in LaTeX: $\\epsilon$ and $N$ in the first paragraph, $\\mathcal{S}$, display (4) ('x∈S (J˜π(x, 0) > 0) ∼Beta(N −k, k + 1)'), $-J_{\\tilde{\\pi}}(x,0)$, the probability $\\underset{x\\in\\mathcal{S}}{\\mathbb{P}}(J_{\\tilde{\\pi}}(x,0) > 0)$ in the text and in the Figure 3 caption, $k=731$, $1-\\beta=0.9$, $1-\\epsilon=0.99979$, and Remark 4 with the two fractions $\\frac{N-k}{N+1}$ and the probability over $(x_{1:N},x)\\in\\mathcal{S}$. Display (4) and Remark 4 were checked on 200-210 dpi crops." + WORDS,
 (8, ML): "All 17 lines contain mathematics now written in LaTeX: $\\beta$, Lemma 5 with fragments of displays (5) and (6) (identical in print to (2) and (3)), $\\epsilon$, $\\tilde{V}(x_i,0) \\ge \\delta$, $J_{\\tilde{\\pi}}(x_i,0) \\le 0$, $J_{\\tilde{\\pi}}(x,0)$, $\\tilde{J}_{\\tilde{\\pi}}(x,0)$, the training set $\\mathcal{T}$, the weighted MSE loss $\\frac{1}{n}\\sum_{i=1}^{n} w_i(\\cdot)^2$ and the conservative-error condition in large parentheses. Checked on 200-210 dpi crops." + WORDS,
 (9, ML): "All 12 lines contain mathematics now written in LaTeX: the optimistic-error condition in large parentheses, the validation metric $\\max_{x\\in\\mathcal{V}}\\{\\tilde{J}_{\\tilde{\\pi}}(x,0): J_{\\tilde{\\pi}}(x,0) \\le 0\\}$, $w=10^{-3}$, $\\beta=10^{-16}$, $\\epsilon \\le 10^{-4}$, $\\epsilon=10^{-4}$ in the Figure 4 caption, and the rocket model of Section 6.2 (state symbols, $\\tau_1,\\tau_2\\in[-250, 250]$, the six dynamics equations, the target set with $|p_x| < 20.0, p_y < 20.0$). Checked on 210 dpi crops." + WORDS,
 (9, ND): MINUS + "The five differences are the exponents of $w=10^{-3}$, $\\beta=10^{-16}$, $\\epsilon \\le 10^{-4}$ (text) and $\\epsilon=10^{-4}$ (Figure 4 caption), and the lower torque bound in $[-250, 250]$; each read on the 210 dpi crops.",
 (9, IP): MINUS + "Same payload as the first parser: exponents −3, −16, −4 (twice: text and Figure 4 caption) and the bound −250 of the torque interval.",
 (10, ML): "The 3 lines contain inline mathematics now written in LaTeX: $\\epsilon = 10^{-4}$ in the Figure 5 caption ('BRTs achieving ϵ = 10−4 (99.990%'), $\\epsilon \\le 10^{-4}$ in the Section 6.3 text, and $\\epsilon = 10^{-4}$ in the Figure 6 caption ('of the neural BRTs achieving ϵ =')." + WORDS,
 (10, ND): MINUS + "The three differences are the exponent of $10^{-4}$ in the Figure 5 caption, in the Section 6.3 text and in the Figure 6 caption; read on the page render.",
 (10, IP): MINUS + "Same as the first parser: the exponent −4 three times (Figure 5 caption, Section 6.3 text, Figure 6 caption).",
 (11, ML): "The single line is the first line of the Chow et al. reference, 'Yat Tin Chow, J´erˆome Darbon, Stanley Osher, and Wotao Yin.': the PDF text layer stores the accents of 'Jérôme' as separate spacing characters, and the modifier circumflex counts as a letter in the tool's normalisation. The name is printed 'Jérôme' on the page (read on the render, same in the authors' .bbl) and is written with precomposed letters; no word is missing.",
 (14, ML): "All 19 lines contain mathematics now written in LaTeX: fragments of displays (7)-(10) of Lemma 7 ('CCPϵ : min', 'h∈H (f(h) ≤g) ≥1 −ϵ', 's.t. f(hi) ≤g,', 'i ∈{1, ..., N} −A{h1, ..., hN}', the binomial-tail line), the lemma text with $\\epsilon, \\beta \\in (0, 1)$ and $1-\\beta$, the proof of Lemma 7 ($\\mathbb{R}$, $\\{g: f(h) \\le g\\}$, the identification $d=1$, $c=1$, $x=g$, ...), and the proof of Theorem 2 ($f(h)=f(x)=-J_{\\tilde{\\pi}}(x,0)$, $g^{\\ast}_{N,k}$, the two probability inequalities and the implication, $J_{\\tilde{\\pi}}(x,t) \\le V(x,t)$). Checked symbol by symbol on 200-210 dpi crops and compiled with pdflatex." + WORDS,
 (15, ML): "All 24 lines contain mathematics now written in LaTeX: the conformal settings of the proof of Theorem 3 (score $-J_{\\tilde{\\pi}}(x,0)$, $n=N$, $\\alpha=\\frac{k+1}{N+1}$), the quantile chain with ceiling brackets (lines such as '⌈(N+1)(1−k+1' are numerators of stacked fractions), the three-line display ending in (11), the two-line display ending in (12), and Section B.2 ($s(x,y)\\in\\mathbb{R}$, the calibration set, the quantile, $C(X_{\\text{test}})$, the coverage property, display (13) with its line fragments 'P (Ytest ∈C(Xtest)|{(Xi, Yi)}n', 'i=1) ∼Beta(n + 1 −l, l),', 'l = ⌊(n + 1)α⌋'). Checked symbol by symbol on 210 dpi crops and compiled with pdflatex." + WORDS,
 (16, ML): "All 22 lines contain mathematics now written in LaTeX: $h=(x,y)$, $f(h)=f((x,y))=s(x,y)$, $k=\\lfloor (n+1)\\alpha-1 \\rfloor$, the quantile chain (the four lines starting with '=' are numerators of stacked fractions), $g^{\\ast}_{N,k}=\\hat{q}$, display (14) and its inline repetition, the incomplete beta function ratio $I_x(n-k, k+1)$ with its three sums (the text layer shows the summation sign as 'P'), $\\beta \\ge I_{1-\\epsilon}(n-k, k+1)$, and $J_{\\tilde{\\pi}}(x,t) \\le V(x,t)$ in the proof of Lemma 5. Checked symbol by symbol on a 210 dpi crop and compiled with pdflatex." + WORDS,
 (16, ND): MINUS + "The three differences are the '−1' in '(n+1)α−1', which occurs three times: in $k=\\lfloor (n+1)\\alpha-1 \\rfloor$ and in the numerators of the second and third fractions of the quantile chain; read on the 210 dpi crop.",
 (16, IP): MINUS + "Same three '(n+1)α−1' as the first parser; pypdf extracts the first one as 'α− 1⌋' with a space after the minus (confirmed in its raw text), so it reports one plain '1' and two '−1' as missing against the three ASCII '-1' of the LaTeX.",
}
# Diagnostic payload sizes that were reviewed; a change means the page changed and must be re-reviewed.
EXPECT_ML = {3: 28, 4: 15, 5: 28, 6: 9, 7: 18, 8: 17, 9: 12, 10: 3, 11: 1, 14: 19, 15: 24, 16: 22}
EXPECT_ND = {3: 4, 4: 2, 5: 2, 6: 2, 9: 10, 10: 6, 16: 6}
v = json.loads((D / "verification.json").read_text(encoding="utf-8"))
for p in v["pages"]:
    n = p["page"]
    assert len(p["missing_lines"]) == EXPECT_ML.get(n, 0), ("missing-line count changed", n, len(p["missing_lines"]))
    for key in (ND, IP):
        tot = sum(p[key]["missing"].values()) + sum(p[key]["extra"].values())
        assert tot == EXPECT_ND.get(n, 0), ("number payload changed", n, key, tot)
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
