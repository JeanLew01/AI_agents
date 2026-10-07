# Independent verifier report: benavoli-piga-2016-paper, PDF pages 1-20

- Package: `staging/benavoli-piga-2016-paper-s1` (`SKILL.md`, `references/index.md`, `references/paper.md`, `references/supplement.md`, 14 JPEGs in `assets/figure/`)
- Source: `paper-review/benavoli-piga-2016-paper/documents/s001-benavoli-piga-2016/source.pdf` (arXiv:1505.01034v2, 20 pages)
- Scratch: `paper-review/_scratch/verify-benavoli-piga`
- Result: **0 errors, 6 minor findings**. Nothing in the package or the review plans was changed.

## Coverage (what was actually done)

- All 20 pages rendered at 170 dpi and read as four column-quarter crops per page (pages 1-18, 72 crops, each shown at roughly 200 dpi effective); pages 19-20 viewed whole. Extra 300 dpi crops of (26), (36)-(37), the paragraph after Algorithm 1 (page 6) and the Theorem 6 interpretation paragraph (page 13).
- Mathematics: every display in the package (76 `$$` blocks, tags (1)-(56) incl. 2a/2b, 51a/51b and all unnumbered displays) compared symbol by symbol with the page crops. Inline maths compared while reading each paragraph against the crop (definitions, bounds, constants, inequalities).
- Statements: Problem 1, Proposition 1, Theorems 1-7, Corollary 1, Definition 1, Remarks 1-6, Examples 1-5 and all proofs read against the PDF.
- Prose: read page by page for pages 3-16; in addition a mechanical bag-of-words comparison (all words of 4+ letters, pages 1-18, maths stripped) between `pdftotext` output and `paper.md` showed no word present in one and missing in the other apart from hyphenation/ligature artefacts, link labels and the "Footnote" labels. Bracketed citation groups in the body compared mechanically: identical multiset.
- Numbers: all prose numbers in Examples 2, 4, 5 and Section 7 checked individually (see below). There are no tables in the paper and no CSVs in the package.
- Figures/algorithms: all 14 JPEGs opened and compared with the pages; the four algorithm transcriptions compared line by line with their crops.
- References: all 64 entries read against the PDF (not sampled), order checked.
- `SKILL.md`, `index.md`, `supplement.md` and the conversion notes read; index headings checked mechanically against `paper.md` headings; LaTeX brace/`$` balance checked mechanically.
- Not verifiable from the PDF (not counted as findings): the published-version citation in the notes (Automatica 70:158-172, doi) and the file names `ErrorBC.eps`/`ErrorIV.eps` quoted in the notes.

## Findings

| # | Severity | PDF page | Item id | Package says | PDF shows | Suggested fix |
|---|---|---|---|---|---|---|
| 1 | minor | 4-8 | markers in p0004-b002, p0004-b003, p0004-b014, p0005-b010, p0006-b012, p0007-b005, p0008-b010 (after (27)); texts in p0004-b008, p0004-r01, p0004-b009, p0004-b021, p0005-b031, p0006-b018, p0007-b007, p0008-b012 | Footnote markers are written `[^1]` ... `[^8]`, but the footnote texts are ordinary paragraphs "Footnote N: ..."; there is no `[^N]:` definition, so a Markdown renderer prints the literal text `[^1]` etc. | Superscript footnote marks 1-8 with footnotes at the column foot | Either turn the texts into real definitions (`[^1]: To clarify ...`) or replace the markers by a plain form that matches the labels (e.g. "(footnote 1)"). Content of all eight footnotes is correct. |
| 2 | minor | 4-5 | p0004-b008, p0004-r01, p0004-b009, p0004-b021 | The block of Footnotes 1-4 sits between "Summing up what we have obtained so far:" and the list items "(1) the set-membership constraint ..." / "(2) for the inferences ...", so the lead-in sentence is separated from its list by four footnote paragraphs | The sentence ending page 4 continues directly with the list (1), (2) at the top of page 5 | Move the four footnote paragraphs after list item (2) (or before "In order to formulate the set-membership filtering problem ..."). |
| 3 | minor | 5-6, 8-9 | p0005-b031, p0006-b018, p0008-b012 | Footnote 5 is placed inside the proof of Theorem 2 (between the display for P(Y(k)\|x(k)) and "Then, the updating step ..."); Footnote 6 between Remark 1 and Remark 2; Footnote 8 between the first paragraph of 5.1 and Definition 1 | Footnotes at column/page foot; the proof and the remarks run continuously | Cosmetic; move each footnote to the end of the paragraph/block that carries its marker (Footnote 5 after the proof of Theorem 1, Footnote 6 after the proof of Theorem 2, Footnote 8 after the sentence following (27)). |
| 4 | minor | 1 | p0001-b013 | "Footnote ⋆ (attached to the paper title): ..." but the H1 title carries no ⋆ mark | Title ends with a ⋆ footnote mark | Cosmetic; acceptable as is, or add the mark to the title line. |
| 5 | minor | 10 | conversion notes (paper.md line 1074) | "a stray number (37) printed on an empty line after the h_4 line of (36) (given as two blocks)" | (36) is printed on the h_1 line; h_2, h_3, h_4 follow and (37) is printed on its own line below h_4. The package's two blocks (h_1 tagged 36; h_2-h_4 tagged 37) reproduce this correctly | Reword the note, e.g. "(36) labels the h_1 line; (37) is printed on a separate line below h_4 and is used here as the tag of the h_2-h_4 block". The transcription itself needs no change. |
| 6 | minor | 3, 4, 5, 7, 10, 13-14, 16-18 | conversion notes (paper.md lines 1074, 1077) | The "kept as printed" list is accurate for every item it names, but it is not complete: other printed oddities are also kept verbatim and are not mentioned | Also printed (and correctly kept): stray ")" in "all the observations y^k)." (Sec. 4); "Qr" (proof of Thm 1); "zonotops" (p. 3); "we loose" (footnote 3); missing full stop before "Hence, since X(k-1)" (p. 5); unclosed parenthesis "(see, e.g. [50,51]." (p. 10); "can be splitted", "is the given by" (p. 12-13); "is seeked", "at the same not containing" (p. 14); "Algorithms 3 is used" (p. 16); refs: "sistems" [1], "Bratislava (Russia)" [28], "in in Semi-Infinite" [40], "Internation Journal" [63]; "(dark grey region)"/"(light gray region)" in Fig. 1 caption; `\omega^T` (upright T) in remark (1) after (33) | Optional: add "among others" to the note or extend the list, so a reader does not take the unlisted oddities for conversion damage. |

No error-level finding: no symbol, number, statement, reference or figure discrepancy was found.

Remarks on the points the coordinator asked about:
- Doubled backslashes: none outside legitimate LaTeX row breaks (mechanical search for `\\\\` and `\\cmd` patterns: no hit). No tables exist.
- Extraction damage (`<sup>`, `<sub>`, stray `**`, split decimals): none found.
- "Footnotes swallowing paragraphs": no paragraph is swallowed or lost; the only effect is the placement described in findings 2-3.
- Reference list: 64 entries, numeric order [1]-[64] kept, none missing or duplicated despite the two-column layout (page 17 right column holds [15]-[32], page 18 holds [33]-[64]).

## Checked and found correct (by page)

- p1: title, authors, affiliations a/b, abstract, key words, title footnote text, e-mail addresses, "Preprint submitted to Automatica", "6 November 2018", Section 1 start and the two bullets.
- p2: Introduction paragraphs, all citation groups ([1,2,3,4,5,6], [7,8], [9,10], [11,12,13,14], [15,16], [17], [18,19], [20, Ch. 2], [21,22,23], [24], [25,26,27], [28], [29,30], [29], [31], [32], [33,34], [35,36,37], [38]); italic "M" in "includes $M$" kept as printed.
- p3: (1), (2a), (2b), (3), Example 1 (system, q_d, A_{k-1}, C_{k-1}, n=2, m=1, d=2, s(d)=6), (4), (5), Problem 1 set definition and end mark.
- p4: unnumbered Pr(X in X)=1 display, (6), (7), Proposition 1, E[g] display, (8), footnotes 1-4 text.
- p5: list (1)-(2), Theorem 1 with (9), (10), (11); proof displays; (12) all four lines; "Qr"; Theorem 2 with (13), (14), (15); footnote 5.
- p6: Bayes-rule display (both fractions), Pr(y|x) display, denominator display, (16), intersection display, five-line dP display, (17), "(6)" cited twice, "A1.2.1 and A1.2.1", Algorithm 1 (A1.1, A1.2, A1.2.1, A1.2.2), hats on P and X in the paragraph after Algorithm 1 (300 dpi crop), Remark 1 with (18), (19), footnote 6.
- p7: Remark 2 (both paragraphs), (20), (21) incl. "Omega conv." subscript, (22), proof displays, (23), (24), (25), two bullets, footnote 7.
- p8: Refinement of Algorithm 1 (A1.1.3, A1.1.4), Theorem 4 with (26) (under+overline on x_i^*, 300 dpi), (27), footnote 8, Theorem 5 with (28) ("max"), proof display ("sup"), (29), feasibility display, Remark 3.
- p9: Definition 1 with (30), (31), (32), (33), remarks (1)-(4), Corollary 1 with (34) and proof, Example 2 with (35) and all bounds (0.2, 0.4, 0.5, omega = [-1 -0.5]).
- p10: Fig. 1 and caption (0.45), (36), (37) incl. underbrace labels and x_1(1) in both squared terms (300 dpi), 2d=4, 2.40-GHz, 3 GB, 2.1 seconds, Section 6 opening, H_j display, list (1)-(2), (38), challenge list (1)-(2) with citations [50,51], [52], [53,54,55,56], [57], [58], [59,60,61].
- p11: (39), (40), Remark 4 with expectation display and (41), (42), Algorithm 2 (input, A2.1-A2.5, (43), output), paragraph after Algorithm 2 incl. "problem (50)", Example 3 (80 points).
- p12: Fig. 2 (panels a-d) and caption, (44), "R(x_i)" before (45), (45), Fig. 3 and caption, (46), Theorem 6, proof incl. (47), (48).
- p13: (49), end of proof, interpretation paragraph (no tilde on H_1^*, 300 dpi), 6.4 heading, (50), (51a), (51b) incl. missing transpose as printed, Remark 5 (O(mn^{2d}), fraction, ceil(d/2)+1, 4 state variables, degree 6).
- p14: Remark 6 with (52), (53), Example 4 (2d=4, two black points, k=2, 9 linear inequalities), Fig. 4 and caption, 6.5 text and two bullets, Theorem 7 and start of proof.
- p15: Algorithm 3 (input, A3.1, A3.2, A3.2.1 with (54), A3.2.2, output), rest of proof of Theorem 7, Example 5 (54, 830, 80, 108, 54 x 2, 750), Fig. 5 and caption ("Exampe 1"), (55), parameters r=0.25, b=0.95, c=1.1, d=0.55, (56), 0.05, box [0.28 0.32] x [0.78 0.82], 0.001, x_1(0)=0.8, x_2(0)=0.3, [-0.05 0.05].
- p16: k=1..40, N=20, 8 half-spaces, 4 iterations, 28 seconds; Figs. 6, 7, 8 and captions; Conclusions.
- p17-18: end of Conclusions; references [1]-[64] each read against the PDF; the three "PDF drops a character" cases named in the notes ([11] "identificationbounded", [42] "no. 12", [64] URL with blank) are as printed.
- p19-20: each page holds one uncaptioned plot (y_o - y-hat vs Sample, 1-200); crops complete, described correctly in the notes.
- Assets: algorithm-1, algorithm-1-refinement, algorithm-2, algorithm-3, figure-1 ... figure-8, uncaptioned-figure-p0019/p0020: complete (axes, tick labels, panel letters), no caption or body text inside the crops, legible.
- index.md: all 19 listed headings exist verbatim in paper.md; theorem/equation/asset assignments per section are right. SKILL.md and supplement.md contain no false statement (supplement correctly says nothing was supplied).
- Conversion notes: the listed oddities ((6) cited twice; "problem (50)"; R(x_i); missing transpose in (50)/(51); "A1.2.1 and A1.2.1"; x_1(1) twice in h_2; "Exampe 1"; X_0 box vs initial conditions) all checked against the PDF and are true.

## Question answered from the package only

Question: For the SOS-relaxed problems (51), how does the number of optimization variables scale, what SOS degree do the authors recommend, and what problem sizes do they consider tractable?

Answer from `paper.md`, section "6.4 Handling the constraint M ⊆ H_j", Remark 5: for fixed SOS degree 2**d**, the number of optimization variables grows polynomially with the state dimension n and linearly with the number m of constraints h_s; it is O(m n^{2**d**}), because each matrix Q_s (s = 0..m) has C(2n+**d**, **d**)(1 + C(2n+**d**, **d**))/2 = O(n^{2**d**}) free variables. For fixed n the size of Q_s grows exponentially with 2**d**. The authors suggest **d** >= ceil(d/2) + 1, with d the degree of the polynomial system (1). With general-purpose SDP solvers such as SeDuMi on commercial workstations, systems with 4 state variables and degree d up to 6 are solvable; more states are possible for smaller d and vice versa.

Check against the PDF (page 13, right column, Remark 5): identical in every formula and number.
