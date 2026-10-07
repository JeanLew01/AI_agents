# Independent verification: greco-vasile-2022-paper, pages 1-22

Package: `staging/greco-vasile-2022-paper-s1` (`references/paper.md` lines 1-~612, `assets/table/table-1.csv`, `table-2.csv`, `assets/figure/figure-1.jpg`, `figure-2.jpg`, `algorithm-1..4.jpg`), plus one read of `SKILL.md`, `references/index.md`, `references/supplement.md` and the conversion notes.
Reference: `source.pdf` pages 1-22, rendered at 200 dpi (each page viewed as two half-page images), plus the native text layer.

## Coverage

- Pages 1, 2, 4 (lower half), 5-22: every half-page image read next to the package text. Page 3 and the upper half of page 4 (introduction prose, no mathematics) were checked through the text layer only.
- Mathematics: every display equation (1)-(35b), the unnumbered displays on pages 17 and 19, and Lemma 1-3 / Theorem 1 compared symbol by symbol with the 200 dpi renders (under/overlines, hats, tildes, bold, sub/superscripts, sum/min/max limits, tags). Inline mathematics read against the images for every paragraph on pages 5-22.
- Prose: word-level and punctuation-level automatic diff of the PDF text layer (pages 1-22) against the package prose with mathematics stripped; all residual differences were mathematics tokens, float positions or the drop cap.
- Nomenclature: all 48 entries compared with pages 1-2.
- Algorithms 1-4: transcription compared line by line with the page images; the four JPEG crops opened.
- Figures 1-2: crops opened, captions compared.
- Tables 1-2: every CSV cell and the inline Markdown tables compared with pages 21-22.
- Float move on page 9, page boundaries 8/9/10, 11/12, 22/23, rendering problems (doubled backslashes, `<sup>`, footnotes).
- Fonts: `pdffonts` used to decide the identity of the particle-collection glyph.
- Not in my range: references list, pages 23-44.

## Findings

| # | Severity | PDF page | Item id | Package says | PDF shows | Suggested fix |
|---|---|---|---|---|---|---|
| 1 | error (symbol, low impact) | 15, 16, 17, 20 | p0015-r01, r02, r03, r06, r07, r08, r09, r10; p0016-r00, r02; p0017-r02; p0020-r07 | The particle collection is written `\boldsymbol{\mathcal{X}}` (bold calligraphic X) in Eqs. (19a), (19b), (20), (21), (22), (32), Algorithm 4 and the surrounding prose, including `\mu_{\boldsymbol{\mathcal{X}}}^{1H}`, `\sigma_{\boldsymbol{\mathcal{X}}}^{LH}`. | The same glyph as on pages 2, 8, 9: bold chi. The PDF embeds CMMIB10/CMMIB7 (bold math italic) but no bold calligraphic font on any of these pages, and the Nomenclature lists the symbol between phi and Psi as "collection of particles". The package itself uses `\boldsymbol{\chi}` on pages 2, 8-10 and again in Appendix A (line 802), so one printed symbol appears as two different symbols and `\boldsymbol{\mathcal{X}}`, `\mu_{\mathcal{X}}`, `\sigma_{\mathcal{X}}^{1H}` have no Nomenclature entry. | Replace `\boldsymbol{\mathcal{X}}` by `\boldsymbol{\chi}` everywhere (34 occurrences, all in lines 408-559). |
| 2 | minor | 1 | p0001-r001 | `Cristian Greco[^∗] and Massimiliano Vasile[^†]` with the footnotes given as plain paragraphs "Footnote ∗: ...", "Footnote †: ...". | Superscript markers * and † on the names. | The `[^..]` references have no matching footnote definitions and will render literally. Use plain markers (`Cristian Greco∗`) or real footnote definitions. |
| 3 | minor (documented) | 6 | (4a)-(4c) items | Three separate display blocks. | One system with a shared left brace. | None required; the conversion notes state it. |
| 4 | minor (documented) | 12 | Algorithm 3 item | Adds "(inside the loop over $k$)", "(inside the loop over $j$)", "(loop over $j$)", "(loop over $k$)". | No such words; nesting shown by indentation. | Acceptable as documented; could be replaced by indentation. |
| 5 | minor | index.md | - | "equations (22)", "equations (30)", "equations (31)", "equations (32)", "equations (46)" for single equations; appendix headings "A./B./C." collide with subsection letters. | - | Cosmetic; the collision is explained in the notes. |

Totals: 1 error, 4 minors.

## Checked and found correct

- p1: title, authors, affiliation, abstract, conference note and both author footnotes (text complete, e-mail addresses correct); Nomenclature b ... L_k.
- p2: Nomenclature l ... Omega_lambda, including `\underline{\mathbb{E}}, \overline{\mathbb{E}}`, `\widetilde{F}` (printed italic F with tilde), `t_{\alpha,l-1}`, `\hat\theta, \underline{\hat\theta}, \overline{\hat\theta}`, `\underline{\boldsymbol\lambda}`, `\sigma^{1H}`; all 48 entries present, in order.
- p3-4: introduction prose identical word for word (printed typos kept: "interest, The result", "remarks an future"); citations [1]-[21] in place.
- p5: Eqs. (1), (2), (3); R^{n_x}, R^{n_d}, R^{n_y}, t_k < t_{k+1}.
- p6: Eqs. (4a)-(4c), (5) (printed p(x_k | y_{1:k}; lambda) kept), (6a) underline / (6b) overline, min/max over lambda in Omega_lambda.
- p7: Eqs. (7), (8) (three lines, proportional sign then two equalities, lambda_y / lambda_x in the last line).
- p8: Eqs. (9), (10), (11a), (11b); hats on w in (10), (11a) right factor and (11b) left side; initial weight formula; non-bold pi(x_0) kept.
- p9: Algorithms 1 and 2 transcriptions and crops; Fig. 1 crop (three panels, axis labels 0 and k, no caption text inside) and caption.
- p8-10 float move: the paragraph "Once this precomputation step is complete ... (Line 3)." is continuous and complete; Algorithm 1, Fig. 1, Algorithm 2, Fig. 2 follow once each; "The derivatives of such estimator ... Appendix A." follows; nothing lost or duplicated.
- p10: Fig. 2 crop (four panels) and caption; n_eff formula with unnormalised w squared.
- p11: Eqs. (12), (13) (sum over j with upper limit N_pi, no lower "=1", as printed).
- p11/12 boundary: "... Furthermore, | the UKF-based proposal ..." continuous; Algorithm 3 placed after that paragraph; transcription and crop correct.
- p12-13: complexity lists, Eqs. (14), (15), O(MN^2 + MN lambda c_{dp} + MN c_pi), c_{dp} > c_pi.
- p14: Eqs. (16), (17), (18) (sum i=0..N_q, tilde on calligraphic F).
- p15: Eqs. (19a), (19b), (20) (printed "j = n+1" kept), (21) (sqrt(N), 1H / LH superscripts, t_{alpha,l-1}) apart from finding 1.
- p16: Algorithm 4 transcription and crop (underline for min, overline for max); Global-search prose, "Eqs. (42) to (44)".
- p17: Eq. (22), sigma(S) display, lb displays, Eqs. (23), (24), (25); italic R in "lb : S -> R" then blackboard R in the Bounding section, as printed.
- p18: Lemma 1 with (26), Lemma 2 with (27), Eq. (28), (sqrt3/2)^{floor(k/n_lambda)}, list update L_k.
- p19: Lemma 3 with both unnumbered displays and (29) (ceiling, log base 2/sqrt3), L_k / U_k (both with min, as printed), Theorem 1 with (30), blackboard S in lb(S*) as printed.
- p20: Eq. (31) (inner ceiling, big parentheses, square brackets), Eq. (32), N_0 = n_lambda!, citations [32]-[39].
- p21: Table 1 caption and all 16 cells (CSV and inline); rTCA 13-Jan-2021 13:24:25 UTC; NORAD IDs 42063 / 30141.
- p22: Eqs. (33), (34), (35a) underline / (35b) overline; Table 2 caption and all 6 cells; "60 deg", "e < 0.1", "<= 800km".
- p22/23 boundary: "... defined as a normal | distribution" then Eq. (36): continuous.
- Rendering: no doubled backslashes in tables, no `<sup>`, no glyph soup, footnotes do not swallow paragraphs, LaTeX delimiters balanced in the range.
- SKILL.md / index.md / notes: all 34 main-paper index headings exist verbatim in paper.md ("Document beginning" for the empty supplement is a placeholder); the notes' statements that concern pages 1-22 (kept printed oddities, brace of (4), Algorithm 3 remarks, float move) are true.

## Technical question answered from the package only

Question: how many longest-edge-bisection steps guarantee a simplex of diameter at most delta, and what filter complexity bound follows?

Answer (sections "3. Branching" and "5. Filter complexity with epistemic dimension"): with N_0 initial n_lambda-simplexes of largest diameter sigma_0, at most K = N_0 n_lambda ceil(log_{2/sqrt3}(sigma_0/delta)) splittings are needed (Lemma 3, Eq. (29)), because LEB shrinks the diameter by at least (sqrt3/2)^{floor(k/n_lambda)} after k splittings. The first iteration needs at most N_0(n_lambda+1) pSIS evaluations and each branching step one more, so C_RPF(n_lambda) = 2[N_0(n_lambda+1)+K] C_pSIS = 2[N_0 + N_0 n_lambda(1 + ceil(log_{2/sqrt3}(sigma_0/delta)))] C_pSIS (Eq. (31)), linear in n_lambda when N_0 does not depend on n_lambda.

Check against the PDF (pages 18-20): identical to Lemma 3, Eq. (29) and Eq. (31) as printed.
