#!/usr/bin/env python3
"""Write adjudications.json from the current review queue. Reasons are keyed by (page, check);
the script refuses to run if the queue contains a diagnostic without a written reason, or if the
diagnostic payload no longer matches what was reviewed (EXPECT below)."""
import json
from pathlib import Path
R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/devonport2021data-paper"
D = W / "documents/s001-devonport2021data"
ML, ND, IP = "missing_lines", "number_differences", "independent_parser_number_differences"
WORDS = (" The prose words of every listed line were compared with the 170 dpi page render and found, in order, in the "
         "page text (scripted word-sequence check; the only tokens not matched are line-wrap fragments and glyph-soup math).")
REASONS = {
 (1, ML): "All 4 lines contain inline math now written in LaTeX: $\\mathbb{R}^n$ (twice, PDF text 'Rn'), $a,b\\in\\mathbb{R}^n$ and the interval definition $[a,b]=\\{x\\in\\mathbb{R}^n | a \\le x \\le b\\}$, whose last two glyphs 'b}' are printed on page 2 and were transcribed here to keep one formula." + WORDS,
 (2, ML): "All 43 lines are inline or display mathematics now written in LaTeX from the authors' TeX source: the notation paragraph ($z_k(x)$, $\\mathbb{R}^{\\binom{n+k}{n}}$, $\\mathbb{R}[x]^n_d$), $\\Phi(t_1;t_0,x_0,d)$, $\\mathcal{X}_0$, $\\mathcal{D}$, $\\mu(A)$, $\\hat{R}_{[t_0,t_1]}$, Problem 1, and the six displays (reachable set, $\\kappa(x)$, $M$, $\\kappa(x)^{-1}$, $\\hat{\\mu}$, $C(x)$), each checked symbol by symbol on a 240-260 dpi crop and on a pdflatex rendering of the transcription. The first line starts with 'b}', which is transcribed at the end of page 1." + WORDS,
 (2, ND): "Sign glyph only: the PDF has eight exponents '−1' with the Unicode minus (in $1/(z_k^\\top M^{-1} z_k)$, '$M^{-1}$ exists', $\\kappa(x)^{-1}=z_k^\\top M^{-1}z_k$, $\\hat{\\kappa}^{-1}=z_k^\\top\\hat{M}^{-1}z_k$, $(\\cdot)^{-1}$, '$\\hat{M}^{-1}$ exists'); LaTeX writes them '^{-1}' with ASCII '-'. Counted 8 on the page image and 8 in the text.",
 (2, IP): "Same as the first parser: eight '−1' exponents (Unicode minus in the PDF) are written '^{-1}' (ASCII minus) in LaTeX; 8 on the page image, 8 in the text. No other number differs.",
 (3, ML): "All 33 lines contain mathematics now written in LaTeX from the TeX source: Theorem 1 (definition of $C(x)$, bound (1) whose fraction fragments are the lines 'log 4' / 'log 40', the $\\mu^N(\\cdot)\\ge 1-\\delta$ display), the confidence sentence with $\\delta=10^{-9}$, Lemma 1 with $\\text{Pos}(V)$, Lemma 2 with $\\hat{\\ell}(c)$, $\\mathbb{E}_\\mu$ and its bound, the proof sketch with $\\text{Pos}(\\mathbb{R}[x]^n_d)$, and the arg-min problem. Each display was checked on 240 dpi crops and on a pdflatex rendering. Lines inside the Algorithm 1 crop are excluded by the tool and were checked separately against the crop." + WORDS,
 (3, ND): "Explained item by item. Extra '1'x10, '0'x9, '5', '4', '40', one '+2' and three '-1' are the numbers of the Algorithm 1 transcription (subscripts of $X_0$, $\\mathcal{X}_0$, $t_0$, $t_1$, $x_0^{(i)}$, 'Algorithm 1', $1-\\delta$, $\\{1,\\dots,N\\}$, $\\frac{1}{N}$, $i=1$ twice, $\\frac{5}{\\epsilon}$, $\\log\\frac{4}{\\delta}$, $\\binom{n+2k}{n}$, $\\log\\frac{40}{\\epsilon}$, $\\hat{M}^{-1}$ three times); the PDF text of the algorithm lies inside the image crop and is excluded, and every one of these was read on the crop. Missing '2' / second extra '+2': the PDF prints 'n + 2k' with spaces in bound (1), LaTeX has '\\binom{n+2k}{n}'. Missing '−1'x3 and '−9' are the Unicode-minus exponents of $(\\cdot)^{-1}$ in Theorem 1, $z(x)^\\top\\hat{M}^{-1}z(x)$, $M^{-1}$ in the arg-min constraint and $10^{-9}$, written with ASCII '-' in LaTeX (the other three extra '-1' and the '-9').",
 (3, IP): "Same payload as the first parser. Extra numbers ('1'x10, '0'x9, '5', '4', '40', one '+2', three '-1') come from the Algorithm 1 transcription, whose PDF text is inside the excluded image crop; each was read on the crop. 'n + 2k' in bound (1) is '2' in the PDF text and '+2' in '\\binom{n+2k}{n}'. The three '−1' exponents and '−9' of $10^{-9}$ use the Unicode minus in the PDF and ASCII '-' in LaTeX.",
 (4, ML): "All 33 lines contain mathematics now written in LaTeX from the TeX source: the end of Remark 2 ($x_1,\\dots,x_m$, $x_f^{(i)}$, $\\mathbb{R}^m$, $\\hat{R}_{[t_0,t_1]}$), Duffing dynamics (2) and its parameters, the initial intervals, $\\epsilon$, $\\delta$, the a posteriori accuracy $1-(2\\times10^{-5})$ and $0.99-2\\times10^{-5}$, the quadrotor dynamics, the six initial-state intervals and the two input intervals. The displays were checked on a 240 dpi crop of the right column, the left column on the 170 dpi render, and all on a pdflatex rendering." + WORDS,
 (4, ND): "Formatting only; every value was read on the page image. Unicode minus in the PDF versus ASCII '-' in LaTeX: −0.05, −9 (twice, $10^{-9}$), −5 (twice, $10^{-5}$), −2 (in $0.99-2\\times10^{-5}$), −1.7, −0.8, −1.0, −1.5. '0' and '100' versus '0,100': the time range is printed '[0, 100]' and written '$[0,100]$' as in the TeX source; the tool reads '0,100' as one token. '156' and '626' (twice) versus '156,626' (twice): the PDF prints '156, 626' with a math-mode space after the comma; the text has 156,626.",
 (4, IP): "Same differences as the first parser (Unicode versus ASCII minus for −0.05, −9 x2, −5 x2, −2, −1.7, −0.8, −1.0, −1.5; '[0, 100]' versus '[0,100]'; '156, 626' versus '156,626', twice), plus '46' and '052' versus '46,052': pypdf extracts the kerned number as '46 ,052' (confirmed in its raw text); the page prints $N_{AP}=46,052$.",
 (5, ML): "All 16 lines contain mathematics now written in LaTeX from the TeX source: $n=6$, $k=4$, $\\epsilon$, $\\delta$ in the Figure 2 paragraph; $x_1,\\dots,x_n$; the four lines of the traffic dynamics (3); $\\bar{x}$, $w=1/6$, $x_i(0)\\in[100,200]$, $d\\in[40/T,60/T]$; and the monotonicity definition with $x^{(1)}$, $x^{(2)}$, $d^{(1)}$, $d^{(2)}$, $\\underline{x}$, $\\overline{x}$, $\\underline{d}$, $\\overline{d}$. Equation (3) and the monotonicity paragraph were checked on 260-300 dpi crops, including the three closing parentheses of the last line of (3), and on a pdflatex rendering." + WORDS,
 (5, ND): "Formatting only. '−1' x3 (Unicode minus) are the subscripts $x_{i-1}$, $x_{n-1}$ and '$n-1$' of equation (3), written with ASCII '-' in LaTeX. '100' and '200' versus '100,200': the page prints '[100, 200]', the text has '$[100,200]$' as in the TeX source, which the tool reads as one token. All read on the 300 dpi crop / page render.",
 (5, IP): "Same as the first parser ('−1' x3 in equation (3) versus ASCII '-1'; '[100, 200]' versus '[100,200]'), with two pypdf artefacts confirmed in its raw text: 'N = 2 ,009,600' is split into '2' and '009,600' (the page prints $N=2,009,600$), and '(i = 2,...,n − 1)' is extracted with a space, giving '1' instead of a third '−1'.",
 (6, ML): "All 4 lines contain inline math now written in LaTeX: the interval $[\\Phi(t_1;t_0,\\underline{x},\\underline{d}),\\Phi(t_1;t_0,\\overline{x},\\overline{d})]$ (under/overlines are not in the PDF text layer; checked on a 300 dpi crop), $\\epsilon=0.05$, $\\delta=10^{-9}$, and the kernel expressions $\\phi_k(x)$, $(1+x^\\top x)^k$, $\\phi(x)^\\top\\phi(x)=(1+x^\\top x)^k$." + WORDS,
 (6, ND): "Sign glyph only: the exponent of $\\delta=10^{-9}$ is '−9' with the Unicode minus in the PDF and '^{-9}' with ASCII '-' in LaTeX; read on the page render.",
 (6, IP): "Same as the first parser: '−9' in $\\delta=10^{-9}$ (Unicode minus) versus ASCII '-9' in LaTeX; read on the page render.",
}
# Diagnostic payload sizes that were reviewed; a change means the page changed and must be re-reviewed.
EXPECT_ML = {1: 4, 2: 43, 3: 33, 4: 33, 5: 16, 6: 4}
v = json.loads((D / "verification.json").read_text(encoding="utf-8"))
for p in v["pages"]:
    assert len(p["missing_lines"]) == EXPECT_ML.get(p["page"], 0), ("missing-line count changed", p["page"], len(p["missing_lines"]))
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
