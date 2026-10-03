# gruenbacher2022gotube - reviewer report

**Status: DONE.** `verify --strict` exit 0, status `reviewed_with_limitations` (mechanical_ok, 26 adjudications applied, 0 stale).
Paper: Gruenbacher, Lechner, Hasani, Rus, Henzinger, Smolka, Grosu, "GoTube: Scalable Stochastic Verification of Continuous-Depth Models" (printed arXiv title, used as package title; AAAI 2022 title "... Statistical Verification ..." is recorded in the conversion notes). Source: arXiv:2107.08467v2, 13 pages (main 1-7, references 8-10, appendix 11-13). TeX source used (GoTube.tex, supplements.tex, GoTube.bbl).
Package: `~/AI_agents/paper2agent/Reachability/skills/gruenbacher2022gotube-paper` (staging s1, s2 kept). Scratch: `logs/work/gruenbacher2022gotube/`.
Note for the coordinator: `prepare` had put the AAAI title into `bundle.json`; I changed it to the printed one, so the skill description now reads "Stochastic".

## Counts
- Figures 5 (Figures 1-4 in `assets/figure`, Figure S1 in `assets/supp_figs`), tables 3 (CSV + Markdown), algorithms 1 (crop + 19-line transcription).
- Formulas kept as images: 0 (41 extractor formula images replaced; 52 display blocks, 46 printed tags: (1)-(6), (S1)-(S40)).
- Omitted regions: 1 (vertical arXiv stamp, p1). Adjudications: 26 (11 missing-lines, 8 + 7 number checks). 64 references, 14 headings.

## What was corrected
- Reading order and joins: sentences crossing pages 1-2, 2-3, 3-4, 4-5, 5-6, 6-7 joined; paragraphs split across columns merged (p2, 3, 6, 7, 11); floats moved within their page so no sentence is interrupted.
- All mathematics rewritten in LaTeX from the TeX source, macros expanded (`\calP` is `\bar{p}`, `\rd` is `\delta`). Script check: all 336 math snippets string-identical to the macro-expanded TeX except the dots between relations, written as printed.
- Labels kept as printed (bold, no period): Definitions 1-3, Theorems 1-2, Lemma 1; statement ends from the TeX environments.
- Tables 1-3 re-entered cell by cell (extractor had split headers; Algorithm 1 had been mis-read as a 21-row table); Figure 3 merged from three fragments.
- References generated from the .bbl; all 64 entries matched to the PDF text layer by script and read on renders; diacritics repaired.
- Headings: levels fixed; run-in bold/italic paragraph titles kept as text, not headings.

## Limitations / things a reader should know
- Theorems 1 and 2 appear twice with the same numbers (main text p5 with proof sketches; appendix p11-12 with full proofs; the appendix resets the counter). Lemma 1 exists only in the appendix (p11).
- Multi-line displays whose every line is numbered are one block per line, so big parentheses open in one block and close in the next: (S7)-(S13) p11; (S18)-(S20), (S25)-(S26) p12.
- Bold "best value" marks of Tables 2-3 (p6) and the bold row of Table 1 (p3) are not in the cells; they are listed in labelled conversion notes. In-figure text of Figures 1-4 and S1 is repeated in labelled "Conversion note ... (not printed text)" items; plot values are not transcribed (p1, 2, 6, 7, 11).
- The indicator in Lemma 1 is written `\mathbb{1}` (source `\mathbbm{1}`); some renderers show a plain 1 (p11).
- Source slips kept as printed and listed in the conversion notes: Delta-lambda indexed V in (3)/(S14) but x,V in (4)/(S15) and Algorithm 1; confidence written 1-lambda / "confidence coefficient lambda" on p5, p7; `\delta_t x = 1` on p3; F with "(x)" inside the subscript in (S17)-(S20); surplus ")" in (S29), (S30); Algorithm 1 line 2 samples the surface, line 14 the ball.
- Only the arXiv v2 PDF was reviewed (proceedings version not compared). One reviewer, no independent second verifier. References were read at 170 dpi (page 10 at 90 dpi), not at higher zoom.

## Self-check
1. Read final SKILL.md, index.md and all of paper.md; damage scan (`<sup>`, `<u>`, replacement chars, ligatures, `~~`, stray emphasis) clean; `$` balanced; all math compiles with pdflatex; headings are the 14 real ones.
2. Opened figure-2.jpg (smallest labels) and algorithm-1.jpg from the final package: complete and legible.
3. Question: "What exactly does GoTube guarantee, under which assumptions, and with how many samples?" Answer from the package:
   - Setting (Setup, display (1)): dx/dt = f(x), x(t_0) in the ball B_0 = B(x_0, delta_0), f Lipschitz-continuous and forward-complete; the maximum of d_j(x) = ||chi(t_j,x) - chi(t_j,x_0)|| is attained on the surface, so samples are drawn uniformly from the surface.
   - Tube (Algorithm 1, lines 16-17): ball at each t_j with centre chi(t_j,x_0) and radius delta_j = mu times the sample maximum, mu > 1.
   - Theorem 1, (3)-(5): cap radius r_x = (-lambda_x + sqrt(lambda_x^2 + 4 Delta-lambda (mu m-bar - d_j(x)))) / (2 Delta-lambda), with lambda_x = ||d chi(t_j,x)/dx|| and Delta-lambda the sqrt(1-gamma)-quantile of the lower bound F_L of Lemma 1 (fitted GEV minus the DKW term sqrt(ln(1/alpha)/(2n)), alpha = min(gamma, 0.5), minus the one-sided KS statistic); then Pr(d_j(y) <= mu m-bar) >= 1-gamma on the cap.
   - Theorem 2, (6): for all gamma in (0,1) there exists N = |V| with Pr(mu m-bar_{j,V} >= m_j^star) >= 1-gamma, stated per time step t_j.
   - The paper gives **no explicit sample-size formula**: only existence of N; the proof gives the coverage bound 1 - (1 - p_{r_bound})^N, (S32)-(S37), and Algorithm 1 adds batches until its probability estimate reaches 1-gamma. The only printed count is "20000 samples, mu = 1.1, 99%, one hour" (Figure 3 caption).
   Checked against the 250 dpi crops of PDF page 5 (Theorems 1-2) and page 12 ((S32)-(S37)): matches.

## New pitfalls (not in the brief)
- Segmenting an unnumbered reference list by vertical gaps: use the line bottoms (`bbox[3]`); lines with accented capitals have a higher top and get glued to the previous entry. `refs.py` here (bbl to Markdown entries, gap segmentation, per-entry match against the text layer) is reusable for natbib author-year lists.
- In a .bbl, `\textquotesingle` prints a straight apostrophe and swallows the following space ("d'Alché-Buc"); a plain `'` prints as a typographic apostrophe.
- `\rightarrow` trips a naive `\left`/`\right` balance count in the page helper; use `\\right(?![a-zA-Z])`.
- `{<}\dots{<}` prints low dots, but `\dots` before a bare `<` renders centred in MathJax/KaTeX: write `\ldots` and normalise it in the TeX comparison.
- Unavoidable number diagnostics: "(mu -1)" has the minus glued to the 1 in the text layer (first parser only); repeated parent headers in a CSV add extra digits when the header contains one ("CartPole-v1"); every labelled conversion note adds "extra" numbers on its page.
- When an appendix restates theorems under reset numbers, say so in the plan notes and in the navigation purposes, otherwise "Theorem 1" is ambiguous in the package.
