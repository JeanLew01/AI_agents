VERDICT: clean

Package: skills/gruenbacher2022gotube-paper (SKILL.md, references/index.md, references/paper.md 584 lines, references/supplement.md, 6 JPEG assets, 3 CSV tables) checked against papers/gruenbacher2022gotube.pdf (13 pages). No A, B or C finding was confirmed. Nothing in the package was edited.

## Findings

None.

## Coverage

Theorem-like blocks (8 of 8, each symbol by symbol on 260-300 dpi crops):
- Definition 1 (Bounding Ball), Definition 2 (Bounding Tube) - p. 4 left column, 260 dpi.
- Definition 3 (Lipschitz Cap), Theorem 1 (Radius of Stochastic Lipschitz Caps), Theorem 2 (Convergence via Lipschitz Caps) with both proof sketches - p. 5, 280 dpi.
- Lemma 1 (Stochastic lower bound F_{L,gamma}), restated Theorem 1 - p. 11, 280 dpi; restated Theorem 2 - p. 12, 300 dpi.
- Numbers, titles, statement ends, quantifiers, inequality directions, hats/bars, calligraphic vs italic B and V, sub/superscripts all agree. The restated Theorem 1 differs from the main-text one only in "Eq. (1) in the main paper (...)" and "as defined in Eq. (S3) of Lemma 1", as the package says.

Displayed equations (46 numbered + 5 unnumbered, all checked, tags on the right lines):
- (1) p. 3 at 260 dpi; (2) p. 4 at 260 dpi; (3)-(6) p. 5 at 280 dpi.
- (S1)-(S16) p. 11 at 280 dpi; (S17)-(S37) p. 12 at 300 dpi; (S38)-(S40) p. 13 at 300 dpi.
- Split displays: (S7)-(S13) seven blocks, all lines and tags present and in order, big parenthesis opens in (S8)/(S10) and closes in (S9)/(S11), overset (S1) on "=" in (S12) and (S6) on "<=" in (S13); (S18)-(S20) three blocks in order; (S25)-(S26) parenthesis opens in (S25), closes in (S26); (S34)-(S36), (S2)-(S3), (S32)-(S33), (S39)-(S40) correct.
- Unnumbered displays present and correct: five-line mean-value display after (S27); first half of the display tagged (S28); the line and the "<=>" before (S30); the r_bound lines before (S37); the conditional-probability display before (S39).
- Trailing punctuation of displays ((1)-(5), (S4), (S6), (S13), (S14)-(S16), (S30), (S36) with comma; others without) agrees.

Algorithm 1: 19 of 19 lines plus the Require line and the title checked on a 280 dpi crop of p. 4 (numbering, nesting levels, loop header, conditions, assignments, comments in parentheses, line 2 surface vs line 14 ball, m-star without j in line 13). Asset algorithm-1.jpg has both rules and white margins on all four edges.

Tables (176 cells, all checked; CSV files are cell-identical to the Markdown tables, verified by script):
- Table 1: 17 rows x 5 columns incl. header, 260 dpi (lower rows read at 170 dpi, unambiguous). Bold as stated in the conversion notes (header row, "GoTube (Ours)", last "yes").
- Table 2: 8 rows x 7 columns incl. header, 330 dpi. Bold list in the conversion note (8 cells) is exactly what is printed bold; rule between the classical benchmarks and the CartPole rows confirmed.
- Table 3: 7 rows x 5 columns incl. the two header rows, 330 dpi. All four GoTube numbers bold, as stated.
- Captions of Tables 1-3 verbatim (incl. the two closing quotes around "No" and typewriter Inf / NaN).

Figures (5 figures + the algorithm image): Figures 1, 2, 3, 4 and S1 opened and compared with the page on all four edges; additionally a pixel scan shows a white margin of 16-44 px between content and every edge of every asset, so nothing is cut and no foreign text is included. Figure 3 bottom edge (closing arc of the magnified inset and the tick labels) checked on an enlarged strip against a 260 dpi page crop. Captions verbatim (Figure 2 and Figure 4 captions at 260 dpi, the others at 170 dpi); label numbers correct; in-figure text reported in the conversion notes (legends, panel titles, "Relative volme", Fraktur B, coordinate axes x_x, x_y, x_z) matches.

References: 64 of 64 entries read on 260-280 dpi crops of pp. 8-10 (authors, initials, diacritics, titles, venues, italics, volumes, issues, pages, years, publishers), and matched by script against the PDF text layer (all 64 entries found; the list accounts for the whole text of pp. 8-10 except the heading). Diacritics confirmed: Abraham with two acutes, Kuncak with hacek, Donze with acute (twice), d'Alche-Buc (twice, straight apostrophe), Franzle and Muller and Puschel with umlauts; Zgliczynski, Zilinskas, Arandjelovic printed without diacritics. Hyphens at line breaks resolved by eye (Cesa-Bianchi, Non-linear, piece-wise, feed-forward, "Pre-Print - ww2.ii.uj.edu.pl", "ICML - Volume 70", 370-379). The slips listed in the conversion notes ("Reachabililty", "Nueral ... nueral", "PATEL, K. K.", "CAPD:: DynSys", "https://github. com/eth-sri/eran") are printed so.

Completeness and order: word-sequence diff (all alphabetic tokens) and bag comparison of words and of numeric tokens between pdftotext of pp. 1-7, 11-13 and paper.md. The only differences are moved floats, text inside figures, mathematics, and line-break hyphenation; no dropped, duplicated or altered prose, no number or citation year differs. Page and column joins read by eye (p1->2 "symbolically bound | the Lipschitz constant", p2->3, p3->4, p4->5, p5->6, p6->7, p11 column break before (S7), p12->13): no cut sentence. First-page footnote, copyright line and author line present once.

Prose read word for word against the page (pages 1-7 and 11-13 in full at 170 dpi, the dense parts again at 260-300 dpi): 10 of 10 text pages; inline math checked in all of them.

Headings and index: all 14 headings of paper.md are printed headings (plus the added "Conversion notes"), nesting sensible; every "Exact heading" of index.md exists verbatim in paper.md and holds what the index says; supplement.md correctly states that no supplement exists.
- Q1: "What is the radius of a stochastic Lipschitz cap and what does it guarantee?" Index -> Main Results -> Theorem 1: r_x = (-lambda_x + sqrt(lambda_x^2 + 4 Delta-lambda_{x,V} (mu m-bar_{j,V} - d_j(x)))) / (2 Delta-lambda_{x,V}), and Pr(d_j(y) <= mu m-bar_{j,V}) >= 1 - gamma for all y in B(x, r_x)^S. Agrees with PDF p. 5, eqs. (4)-(5).
- Q2: "What tube volume does GoTube reach at the 10 s horizon on the CartPole benchmarks, with which settings, and what do the other tools do?" Index -> "GoTube provides safety bounds up an arbitrary time horizon" -> Table 3: 1.1e-19 (CTRNN) and 8.7e-21 (LTC) with mu = 1.1 and 95% confidence; LRT, CAPD, Flow* and LRT-NG all "Blowup" at 10 s. Agrees with PDF p. 6.

Conversion notes: every "kept as printed" claim checked on the page and found true: Delta-lambda with index V in (3)/(S14), index x,V in (4)/(S15), Algorithm 1, proof sketch and (S25)-(S28), index x on p. 13; "1 - lambda" (p. 5) and "confidence coefficient lambda" (p. 7); "delta_t x = 1" (p. 3); star point with and without j; F_{L,gamma-hat(x)} in (S17)-(S20); italic Pr vs upright Pr; surplus ")" in (S29) and (S30); plain sum of indicators in Lemma 1; Area(B_0) in (S32); upright T in the Require line; the listed wording slips; no end-of-proof marks; no page numbers.

Not checked:
- The statement in the conversion notes about the title of the AAAI proceedings version ("Scalable Statistical Verification ...") is outside the PDF and was not verified.
- Curve and point values inside the plots (not transcribed by the package).
- Agreement with the authors' TeX source was not used as evidence.

Housekeeping: all renders and scripts under logs/verify/work/gruenbacher2022gotube/ were deleted by literal path and the directory removed; one process at a time, one page or crop at a time.
