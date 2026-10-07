# Independent verifier report: haj-chhade-box-messages-2014-paper-s1, PDF pages 1-24

Package: `staging/haj-chhade-box-messages-2014-paper-s1`. Reference: `source.pdf` (24 pages, native text layer). Nothing in the package or plans was changed. Reviewer reports were not consulted.

## Coverage (what was actually done)

- **Prose, all 24 pages**: word-level diff of `pdftotext` output against `paper.md` with maths stripped (tokens > 2 characters; every difference inspected). All remaining differences were running heads, page numbers, float relocation and maths tokens. Pages 1-3 and the reference list were additionally diffed with all tokens (no length filter).
- **Mathematics, pages 4-18**: every display, numbered (2.1)-(6.6) and unnumbered, compared symbol by symbol against page renders (170 dpi) and, for pages 13-18, 250-300 dpi crops. Inline maths in every paragraph of these pages read against the images.
- **Algorithms 1-3**: transcriptions compared line by line with 250 dpi crops of pages 14-16 and with the three algorithm JPEGs.
- **Tables 1-3**: every cell of the three CSVs and of the inline markdown tables compared with pages 20-21.
- **Figures 1-16**: all 16 JPEGs opened (contact sheets) and compared with the pages; all captions compared.
- **References**: all 31 entries compared token by token (automated full-token diff, not sampled).
- **Structure/rendering**: headings vs printed headings, index headings vs `paper.md`, asset links resolve, `$`/brace/`\left`-`\right`/`\begin`-`\end` balance (scripted), search for `](` inside maths, doubled backslashes, `<sup>`, footnote syntax. Page boundaries 8/9 and 16/17 (and all others) read for continuity.
- `SKILL.md`, `index.md`, `supplement.md` and the conversion notes read once.

## Findings

Errors: **0**. Minors: **3**.

| # | Severity | PDF page | Item id | Package | PDF | Suggested fix |
|---|---|---|---|---|---|---|
| 1 | minor | 9, 10, 11 | p0009-b003, p0010-b019, p0011-b014 | Captions `Fig. 5 ...`, `Fig. 6 ...`, `Fig. 7 ...` are plain text | Label printed bold like all others; the other 13 captions in the package are `**Fig. N** ...` | Write `**Fig. 5** Nonparametric belief propagation`, `**Fig. 6** Inclusion function [10]`, `**Fig. 7** Filtering problem [30]` |
| 2 | minor | 11-12 | p0012-b002, p0012-b005 (and the following display/continuation blocks) | In the Section 5.2 bullet list, the displays and continuation text ("where [f] is an inclusion function...", "where [g] is...", "In the bounded error context...", "where n_x represents...", "The term ... represents the new l-th box particle...") are at column 0, so they render outside their bullets; Fig. 7 sits between bullets 1 and 2 | All of this is printed inside the "Time Update Step" / "Measurement Update Step" bullets | Indent continuation paragraphs and `$$` blocks by two spaces under their list item (cosmetic; text and order are correct) |
| 3 | minor | 9, 10 | p0010-b011 and siblings | Italic titles "Operations on Intervals and Boxes.", "Inclusion Functions.", "Constraints Satisfaction Problem and Contraction." are run into the following paragraph | Each is printed on its own line, the paragraph starting (indented) on the next line | Optional: put each italic title on its own line. The conversion notes already say they are kept as italic text, so nothing is misleading |

No mathematical, numerical, textual or omission discrepancy was found.

## Checked and found correct (by page)

- p1: title, authors, journal line, DOI, dates, open-access line, abstract, keywords, affiliations and e-mails.
- p2-3: Introduction, the numbered list of four advantages, outline paragraph, Section 2 opening; boundary 2/3 and 3/4 continuous.
- p4: (2.1), (2.2), (2.3), Fig. 1 crop and caption formula (psi_235, psi_245, psi_12).
- p5: (2.4) (index set (i,j) in E, i in V_x, j in V_x; second product over i in V_x), (2.5), X = (X_1..X_7), Y = (Y_1, Y_3, Y_5), Fig. 2.
- p6: (3.1), unnumbered factorization, (3.2), (3.3) with i-1, (3.4) with printed superscript i, (3.5) over u in Gamma_t, Fig. 3.
- p7: Fig. 4, text, Section 4 opening.
- p8: (4.1) with hat and delta, (4.2) with K_h, (4.3), (4.4), N^d, {Omega_ts^j, X_ts^j}, x_p^i ~ p(x); boundary 8/9 continuous.
- p9: Fig. 5, Section 5 list, (5.1), (5.2), (5.3) with square-cup and hull brackets.
- p10: (5.4), unnumbered set identity, (5.5) all three rows with under/over-bars, division rule [1/y-bar, 1/y-underbar], (5.6), (5.7), Fig. 6.
- p11: (5.8), (5.9), S subset [x]' subset [x], f_j with j in {1..n} as printed, (5.10), Fig. 7.
- p12: time-update, predicted-measurement, innovation, box-likelihood and likelihood-factor displays (tilde on contracted box, (l), k+1 indices).
- p13: message-product display, mixture-of-uniforms display, (p_0, p_1, ..., p_d) as printed, (5.11), (5.12), (5.13), the omega_ts^k / [x_ts^k] notation display, Z = card(Q).
- p14: Algorithm 1 (all five steps incl. weight formula), (5.14) with M^{i-1} and sum to Z, Algorithm 2 (input, five steps, w notation).
- p15: (5.15) four lines (sums to V as printed, no dx_t on line 2 as printed), the for-all display with [e], (5.16) without [e] as printed, (5.17).
- p16: Algorithm 3 (six steps, three sub-bullets), Notes 1-3, (6.1); boundary 16/17 continuous.
- p17: Fig. 8, (6.2) indicator, (6.3), (6.4), (6.5).
- p18: Fig. 9 and caption, (6.6), the three interval-arithmetic displays, theta in [0, 2pi], theta ~ U([0, 2pi]).
- p19-22: Section 7 text and numbers (100 sensors, R = L/4, 0.005L, L = 100 m, i7-3520M 2.90 GHz-4 MB, 200 particles/600 values, 9 boxes/45 values, range 6-9, L/3), Figs. 10-16 and captions (incl. printed "Results fo box-BP" in Table 2 title), Tables 1-3 all cells.
- p22-24: Conclusion, Open Access statement, References 1-31 (printed typos such as "bdallah", "Valois,F.", "pp. 4-6", "vol. 15." are faithfully kept).
- Rendering: no `](` inside maths other than asset links, no doubled backslashes in tables, no footnote/`<sup>` residue, all `$` and braces balanced, all 22 asset links resolve, every index heading exists verbatim in `paper.md`. Conversion-note claims ((3.4) superscript, V vs Z, (5.16) omitting [e], w vs omega) are all true.

## Question answered from the package only

**Q:** When two box-particle messages are combined, what weight does a resulting box get, and how is the weight later changed before the boxes are propagated to the neighbour?

**A (from `paper.md`, Section 5.3, Algorithm 1 and Algorithm 3):** For each pair with non-empty intersection, the new box is X_ts(k) = M_1(i) ∩ M_2(j) with weight W_ts(k) = W_1(i) × W_2(j) × |M_1(i) ∩ M_2(j)| / (|M_1(i)| . |M_2(j)|); coincident boxes are merged by summing weights, then weights are normalized. In the message update, after optional contraction with the local observation (Algorithm 2), the weights are corrected by W_ts(k) ← W_ts(k)/|X_ts(k)|, the boxes are propagated through x_s = f(x_t, v, e), and the weights are normalized again.

**Check against PDF (pp. 14 and 16, 250 dpi crops):** identical to the printed Algorithm 1 steps 3-5 and Algorithm 3 steps 4-6.
