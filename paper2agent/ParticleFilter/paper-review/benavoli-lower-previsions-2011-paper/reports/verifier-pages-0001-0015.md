# Independent verifier report: benavoli-lower-previsions-2011-paper, PDF pages 1-15

Package: `staging/benavoli-lower-previsions-2011-paper-s1` (`SKILL.md`, `references/index.md`, `references/paper.md`, `references/supplement.md`, `assets/figure/figure-1..4.jpg`, `assets/table/*.csv`).
Reference: `documents/s001-benavoli-lower-previsions-2011/source.pdf` (15 pages, A4, two-column).
Scratch: `paper-review/_scratch/verify-benavoli-lp` (60 column crops at 230 dpi: `pNN-{L,R}{t,b}.png`; scripts `wd.py`, `bal.py`).

## Result

**Errors: 0. Minors: 3.** No discrepancy in any display equation, theorem statement, number, table cell, caption or reference entry was found.

## Coverage (what was actually done)

- **All 15 pages**, both columns, were read as 230-dpi crops (four crops per page, top/bottom of each column, with overlap) next to the full text of `paper.md` (780 lines, read completely).
- **Mathematics**: every numbered display (1)-(52) and all 20 unnumbered displays were compared symbol by symbol with the crops, with specific attention to underlines/overlines on E, Q and x, tildes on y/Y/calligraphic Y, conditioning bars, inf/min/sup, subscripts/superscripts, upper/lower case (X vs x), bracket chains and equation tags. Inline mathematics of every paragraph was read against the crops as well (not sampled).
- **Statements**: Definitions 1-6, Theorems 1-4, Lemma 1, Corollary 1, Remark 1, Examples 1-3 and all proofs: presence, order, numbering, end-of-statement squares.
- **Prose**: besides reading, an automatic word-level diff (words of 4+ letters, maths stripped) between `pdftotext` output and `paper.md` was run; every reported difference is a reordering caused by two-column extraction, a hyphenation artefact or a small-caps heading. No inserted, dropped or altered prose word was found, including across all column and page boundaries.
- **Tables**: both CSVs and both Markdown tables compared cell by cell with the page-13 crops.
- **Figures**: all four JPEGs opened; captions compared.
- **References**: all 32 entries read against the crops (not sampled), plus the three biographies.
- **Footnotes**: all 9, text and anchor position.
- **Mechanical checks**: `$` parity, brace/`\left`-`\right`/environment balance for all 72 displays and all inline formulas, tag sequence 1..52, headings list, search for `<sup>` and doubled backslashes.
- `SKILL.md`, `index.md`, `supplement.md` and the conversion notes were read once.

Not verifiable from the PDF: the statement in the conversion notes about the published version (IEEE TAC 56(7):1567-1581, 2011, doi:10.1109/TAC.2010.2090707) and the download origin. The date "28 Oct 2010" agrees with the PDF metadata (CreationDate Thu Oct 28 2010).

## Findings

| # | Severity | PDF page | Item id | Package says | PDF shows | Suggested fix |
|---|---|---|---|---|---|---|
| 1 | minor | 4, 6, 7, 10, 11 | markers in p0004-b001, p0004-b008, p0004-r001, p0004-b011, p0006-b016, p0007-b008, p0010-r001, p0011-r016, p0011-r019; texts in p0004-b007, p0004-b020, p0004-b021, p0004-b022, p0006-b022, p0007-b021, p0010-r026, p0011-r023, p0011-r024 | Footnote anchors are written as Markdown footnote references `[^1]` ... `[^9]`, but the footnote texts are plain paragraphs starting "Footnote n:" and there is no `[^n]:` definition anywhere. In a Markdown renderer the anchors therefore appear as literal `[^1]` text and are not linked. | Superscript footnote numbers 1-9 with the footnotes at the column foot. | Either turn the nine paragraphs into real definitions (`[^1]: ...`) or replace the anchors by a plain marker such as "(footnote 1)". Content and anchor positions are correct. |
| 2 | minor | 14 | p0014-r004 (heading), `references/index.md` | `### Software availability` is a level-3 heading placed between Fig. 1 and Fig. 2, so `index.md` lists "figure-2, figure-3, figure-4" under "Software availability" and only figure-1 under "VII. NUMERICAL EXAMPLE". | "Software availability" is an unnumbered italic heading in the left column of page 14 after Fig. 1; Figures 2-4 belong to the numerical example of Section VII (cases 2, 3 and 5) and have nothing to do with the software paragraph. | Move the three figure blocks (Figs. 2-4) before the `### Software availability` heading, or place the software paragraph after Fig. 4, so that the index lists all four figures under VII. |
| 3 | minor | 7, 8, 10, 12 | proofs of Lemma 1, Theorem 2, Corollary 1, Theorems 3 and 4 | Statement and proof bodies are upright; only the labels are bold. | Bodies are printed in italics, with upright emphasis for defined terms. | None required; the conversion notes state this convention. Listed only for completeness. |

No rendering damage was found: no doubled backslashes in tables or matrices, no `<sup>`, no glyph soup, no split decimals, no footnote swallowing a paragraph (each "Footnote n:" paragraph is its own block and the body text continues correctly after it).

The single display flagged by the bracket counter (the unnumbered display at the start of the proof of Lemma 1: five opening and four closing brackets) is as printed in the PDF, and it uses `\Big[` rather than `\left[`, so it renders.

## Checked and found correct (by page)

- **p1**: title, authors with affiliation superscripts, addresses block, abstract, index terms, Introduction paragraphs 1-5 (start), the p-box inequality F_l <= F <= F_u.
- **p2**: rest of Introduction; citation lists ([11], [13], [14], [15], [17], [18], [19] and [20]); "[21, Sects. 2.10 and 5.9]".
- **p3**: (1), unnumbered Markov display with product over k=1..t, (2), (3) (both lines, integral subscript x_{t-1}), (4), the inline Kalman filter equations (x-hat_t, P_t, S_t, L_t), headings II and III.
- **p4**: Definition 1; Definition 2 with three bullets and the infimum over Z_O x {z_U}; unnumbered sum display; Definition 3 and (5); Theorem 1 with (SC1)-(SC3) (underlines on every E, >= in SC1 and SC3, = in SC2); footnotes 1-4.
- **p5**: necessity paragraph; conjugacy relation with overline/underline; unnumbered inequality chain; Remark 1 (all three paragraphs, every under/overline, signs of epsilon terms); Example 1 (both infimum displays, including the printed "(f|z_U)" on the left of the first one and K_O^{z_U}); Example 2 (linear-vacuous mixture display, epsilon and 1-epsilon placement, K_O(z_U)).
- **p6**: Definition 4 and (6); the two paragraphs on GBR; Example 3 (both unnumbered displays, (7), printed subscript "O union I" kept); Definition 5 and (8) (domains as printed, U_j recursion); Definition 6; (9) (five lines); heading IV; footnote 5.
- **p7**: (10); discretisation paragraph (B(y_k, delta), tilde-y, footnote 6 anchor); Lemma 1 with (11), (12), (13) (untilded y^t on the left, stray comma after X_t, five closing brackets); proof displays, (14), (15); remark with X_{t-2}; Theorem 2 with arg_mu expression and (16) (underline on the first inner E, overline on the second, lower-case x_{k-1} in the outer conditioning).
- **p8**: (17) (four lines), (18), unnumbered three-line display with the -I term, (19), lower-case x_0 subscripts; Corollary 1 and (20); (21) with X_k / x_k as printed; (22), (23), (24) (all lines and the minus-mu term).
- **p9**: (25); truncation paragraph with underlined Q and the <= sign; subsection A (100(1-alpha), chi, strict ">" in the IP region definition); heading V; "x_y, y_k" as printed; (26); vacuous prevision for Theta_k; unnumbered marginalisation display; Theorem 3 opening and (27) (N(x_k; x_{k-1}, Q), no A, as printed).
- **p10**: (28), (29), irrelevance conditions, (30) (min, bold theta^t, minus sign), (31) (sum i=1..t, product j=i+1..t), (32), (33), (34) (three lines, untilded y^t as printed), (35), (36), approximation display with primes, final unnumbered display; "(35))" typo kept; footnote 7.
- **p11**: lower mean (max) and upper mean (min) displays; erf display and definition; credibility condition "= 1 - alpha"; (37); upper variance display; heading VI; (38), (39), (40) (four lines), unnumbered x_{k+1} display; items 1) and 2); footnotes 8 and 9.
- **p12**: (41); Theorem 4 with (42) (no dx_0, as printed) and (43) (four terms); proof; (44), (45), (46) (blackboard I and M, bracket nesting), (47), (48) (last factor N(y_{j-1}; Cx_i, R) as printed), (49) with C' as printed, W_a and W_b^{-1}.
- **p13**: (50), (51), LGVM definition, heading VII, (52) with matrices A and C, P_0, Q, R display, constraints [-100,100] and [-30,30], 15 time steps, 100 runs; table cases 1-4 (all 20 cells) and table case 5 (5 cells); p_0 = 0.2; 99%; Q_w formula with 125 and "approximately 0.4"; ratios 0.8723, 1.008, 1.0027.
- **p14**: rest of the discussion (t = 8, 30, [-30,30], "LVGM" typo kept); Fig. 1-4 captions (0.95/1, 0.95/0.1, 0.9999/1, "Case 5" 0.9999/1); Software availability paragraph and URL; Conclusions; Acknowledgements (grant numbers 200020-121785/1, 200020-116674/1, 10030, TIN2008-06796-C04-01, MTM2010-17844).
- **p15**: references [1]-[32] (authors, titles, venues, volumes, pages, years, including printed oddities "survery", "M. Inc, and I.L Arlington Heights", "E Miranda"); three biographies (portraits omitted, as the notes say).
- **Figures**: figure-1.jpg, figure-2.jpg, figure-3.jpg (single axes, legend LP/UP/TS/KF/Cred IP/Cred KF, axis labels X and Time, all ticks visible) and figure-4.jpg (two panels, both axis labels, legend box TS/KF/LP/UP overlapping the lower panel exactly as printed) are complete, legible and contain no caption or body text.
- **Index / SKILL.md / notes**: all 13 headings in `index.md` exist verbatim in `paper.md`; equation ranges and statement lists per section are right; `supplement.md` correctly says nothing was supplied; the list of kept author inconsistencies in the conversion notes is accurate.

## Test question answered from the package only

**Question**: In the biased-measurement-noise model, what are the lower and upper posterior means of the state, and does the imprecision vanish as t grows?

**Answer from `paper.md`, section "V. BIASED MEASUREMENT NOISE"** (Theorem 3, (30)-(31) and the displays after the proof): the lower prevision is the minimum over theta_1..theta_t in [theta^L, theta^U] of the Gaussian expectation with mean x-hat_t - M_t[theta^t] and variance P_t, where M_t[theta^t] = sum_{i=1}^t [prod_{j=i+1}^t (1 - L_j C)A] L_i theta_i and x-hat_t, P_t, L_t come from the standard KF. With g(x_t) = x_t the lower mean is x-hat_t - sum_i [prod_j (1 - L_j C)A] L_i max(theta^L, theta^U) and the upper mean is the same expression with min(theta^L, theta^U). The gap is proportional to theta^U - theta^L, does not depend on x-hat_t and does not converge to 0 as t tends to infinity; if {A, C} is observable it converges to a finite value.

**Check against the PDF** (pages 10-11, crops `p10-Lt`, `p11-Lt`): (30), (31), both mean displays (max in the lower mean, min in the upper mean) and the three statements about the gap are exactly as printed. The answer is correct.
