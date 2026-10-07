# Verifier report: andrieu-pmcmc-2010-paper, PDF pages 1-18 (Sections 1-3)

Package: `staging/andrieu-pmcmc-2010-paper-s1` (paper.md lines 1-369). Reference: `source.pdf` rendered with pdftoppm at 170 dpi (every page read in two half-page images), plus 260-300 dpi crops for dense sub/superscript passages and all sideways captions. Pages 19-20 were also opened to check the 18/19-20 boundary and the Fig. 7 caption.

## Coverage
- Pages 1-18 read in full against the package, word by word for mathematics and step lists, by reading (not character diff) for prose.
- All display equations (1)-(19) and all unnumbered displays checked (none sampled).
- All inline definitions in the SMC, PIMH, PMMH, conditional SMC and PG step lists checked.
- All numbers quoted in prose in Section 3 checked.
- Figure assets 1-6 opened; captions 1-7 compared with the PDF (5, 6, 7 on rotated crops).
- SKILL.md, references/index.md, conversion notes, supplement.md read once; index headings checked programmatically against paper.md (all present); `$$` count balanced; no `<sup>` or replacement characters.
- Not checked: the reference list and anything after page 20 (other verifiers); Fig. 7 asset image itself (page 19) only seen on the page render.

## Findings

Errors: 0. Minors: 3.

| severity | PDF page | item id | package | PDF | suggested fix |
| --- | --- | --- | --- | --- | --- |
| minor | 1 | p0001-b002 | The title appears twice as an H1 (paper.md lines 1 and 5), with the journal line between them. | Title printed once. | Drop one of the two H1 lines (or leave if line 1 is the builder's document title). |
| minor | 11-19 | p0011-b002, p0012-b009, p0013-b002, p0014-b002, p0018-b002, p0019-r03 | Captions start with plain `Fig. N.`; only Fig. 1 (p0005-b007) has `**Fig. 1.**`. | All labels printed bold. | Make the label bold in all captions for consistency. |
| minor | 10-18 | (Sections 2.4.3-3.2) | Conditional bar written as bare `|` inside maths from Section 2.4.3 on, `\mid` before. Legend-mark approximations for the dotted gamma line differ between Fig. 6 (ten dots) and Fig. 7 (seven dots). | Same glyph throughout. | Cosmetic only; no change of meaning. Optional normalisation. |

No discrepancy in a symbol, index, number, limit, tag or sentence was found.

## Checked and found correct
- p1: journal line, authors and affiliations, read-before line (printed 'Ocober' kept), Summary, keywords, footer (address, copyright, 1369-7412/10/72269) placed before Section 1; intro paragraph reads continuously across 1/2.
- p2-3: Sections 1, 2, 2.1; eqs (1)-(4); product limits n=2..T and n=1..T in (3); (5) with W_n^k and delta_{X_{1:n}^k}.
- p4-5: Section 2.2.1; unnumbered identity for p(x_{1:2}|y_{1:2}); bold W_n, F(.|p), Sigma_{k=1}^m p_k = 1; Step 1 (a)-(b), eq (6); Step 2 (a)-(c) incl. printed q(.|y_n, X_{n-1}^{A_{n-1}^k}) without theta; eq (7) first line tagged on p4 and continuation on p5; r(A_{n-1}|W_{n-1}); B_T^k := k, B_n^k := A_n^{B_{n+1}^k}; lineage identity (300 dpi crop); Fig. 1 caption; eq (8).
- p6: eq (9), estimate (1/N) sum w_n, integral display; Section 2.2.2 with all citations and years.
- p7: Section 2.3, eq (10) with printed limits k=n..n+K and k=n..n+K-1; Section 2.4 start, italic phrase.
- p8-9: 'Section 4.5' reference as printed; IMH acceptance ratio; E{p-hat} display; PIMH steps and eq (11); eq (12); PMMH steps 1(a)-(b), 2(a)-(c), eq (13) with theta(i-1) subscripts and braces; closing paragraph. Boundary 9/10 clean (paragraph ends, 2.4.3 heading starts p10).
- p10: Section 2.4.3, conditional SMC steps 1-3 (k != B_1, k != B_n, proportional weights), toy example, PG steps 1, 2(a)-(c), theorem 5 sentence; 2.5 and 2.5.1 headings.
- p11: Fig. 2 moved after the end of 2.5.1; the sentence 'numerous more / sophisticated algorithms' reads continuously, nothing lost or duplicated; list (a)-(b); 2.5.2; '3. Applications' paragraph.
- p12-13: eqs (14), (15); N(0,5); sigma values 10/10 and 10/1; y_{1:100}; 50000 iterations; printed p_theta(x_n|y_n, x_n) kept; Fig. 3 caption incl. the printed '|' mark for T = 10; 0.80 for N = 2000, 0.27 for N = 200; Fig. 4 caption; sentence across Figs 3 and 4 ('we / have an average acceptance rate') continuous.
- p14-15: Fig. 5 caption (rotated crop; printed 'and the (b), (d) the PMMH sampler' kept); IG(a,b), a = b = 0.01, T = 500, N = 5000, 0.15 and 0.08, 50000 / 10000 iterations, at least 2000 particles; Section 3.2 start, SDE display, eq (16), printed 'Ornstein-Unlenbeck'.
- p16: integrated volatility displays, sigma_n^2 display, the (sigma^2(n Delta), z(lambda n Delta)) recursion, eq (17), y_n displays, quotation, TS(kappa, delta, gamma), kappa = 1/2, eq (18) with A_0, eq (19) with A lambda Delta, upper limit N(lambda Delta), r_i and r_i^*.
- p17: A = 2^kappa delta kappa^2 / Gamma(1-kappa); G(1-kappa, 1/B); Poisson mean lambda Delta delta gamma kappa; 100 terms; dimension more than 400; T = 400, Delta = 1, (0.50, 1.41, 2.83, 0.10); priors Be(10,10), G(1, sqrt 50), G(1, sqrt 200), G(1, 0.5); N = 50, 100, 200; S&P dates; Be(4,36); T = 1000, N = 1000; O(T^2).
- p18-20: Fig. 6 and Fig. 7 captions (Fig. 6 prints no p(gamma|y) term; kept as printed); both placed after the paragraph ending 'with little user input.', which reads continuously from p17 to p20; Section 4 heading follows.
- Figure assets 1-6: complete, no caption or body text inside, axis labels, panel letters and tick labels present, legible; Figs 5 and 6 in page (sideways) orientation as the notes state.
- Conversion notes: statements relevant to pages 1-18 are true (eq (7) split, printed oddities, figure placement, sideways figures, footer position).

## Question answered from the package
Q: In the PMMH sampler, with what probability is a proposed theta* accepted, and what is stored on acceptance?
A (paper.md, '2.4.2. Particle marginal Metropolis-Hastings sampler', Step 2(c), eq (13)): with probability 1 ^ [p-hat_{theta*}(y_{1:T}) p(theta*)] / [p-hat_{theta(i-1)}(y_{1:T}) p{theta(i-1)}] x q{theta(i-1)|theta*} / q{theta*|theta(i-1)}; on acceptance set theta(i) = theta*, X_{1:T}(i) = X*_{1:T} and p-hat_{theta(i)}(y_{1:T}) = p-hat_{theta*}(y_{1:T}), otherwise keep the previous values. p-hat is the SMC marginal likelihood estimate of eq (9).
Check against PDF page 9 (printed p. 277): identical.
