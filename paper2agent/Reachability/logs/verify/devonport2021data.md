VERDICT: 1 findings (0 A, 0 B, 1 C)

Package: skills/devonport2021data-paper (paper.md 349 lines, index.md, SKILL.md, 4 image assets).
Ground truth: papers/devonport2021data.pdf (arXiv:2104.13902v1, 7 pages). TeX source not consulted.

## Findings

### C1 (cosmetic, wording of a conversion note) - mis-located source slip in eq. (3)
- Location: paper.md, "## Conversion notes", last bullet, snippet:
  `in equation (3) an extra closing parenthesis in the third line`. PDF page 5, right column.
- Package says: the extra closing parenthesis is "in the third line" of equation (3).
- PDF prints: equation (3) is typeset on FOUR lines:
  line 1 `x1' = (1/T)(d - min(c, v x1, w(xbar - x2)))` (balanced);
  line 2 `xi' = (1/T)( min(c, v x_{i-1}, w(xbar - x_i))` (opens the big parenthesis);
  line 3 `- min(c, v x_i, w(xbar - x_{i+1}))), (i = 2,...,n-1)` (balanced, closes the big one);
  line 4 `xn' = (1/T)(min(c, v x_{n-1}, w(xbar - x_n)/beta) - min(c, v x_n))),` (one `)` too many).
  The unbalanced parenthesis is on the x_n line, i.e. the third EQUATION but the fourth printed
  line, and also the fourth row of the package's own `aligned` block. The third printed line
  (and third row of the package block) is balanced, so a reader who follows the note looks at
  the wrong row.
- The transcription of eq. (3) itself is correct (parenthesis count per line identical to the
  PDF, including the extra one on the x_n line); only the note's location word is off.
- Suggested wording: "an extra closing parenthesis in the third equation (the $\dot{x}_n$ line)".
- Confirmed on a 280 dpi crop of p.5 (x 1190, y 980, 1060 x 1030 px).

No A or B findings. Nothing dropped, duplicated, renumbered or cut.

## Coverage

- Theorem-like blocks checked symbol by symbol on 260-280 dpi crops: 6 of 6
  (Remark 1, Problem 1, Theorem 1, Lemma 1 "([16], Theorem 7.2)", Lemma 2 "([17], Corollary 4)",
  Remark 2). Numbers, titles, quantifiers, inequality directions, hats, calligraphic X_0 / D / C,
  sub- and superscripts all match.
- Displayed equations: 21 of 21 (the package has 21, the PDF has 21). The three printed numbers
  are on the right equations: (1) sample-size bound in Theorem 1, (2) Duffing dynamics,
  (3) traffic dynamics. Bound (1) and the ceiling version in Algorithm 1 match: 5/eps, log 4/delta,
  binom(n+2k, n), log 40/eps.
- Algorithm 1: 13 items (caption, Input, Output, "Set number of samples" + N display, forall,
  2 body lines, end, "Compute ..." + M-hat and alpha displays, "Record the set" + display +
  closing words) against 260 dpi crops: all match; lines are unnumbered in the PDF as stated.
- Tables: 0 cells. The paper has no tables; assets/table, assets/supp_table, assets/supp_figs
  are empty, which is correct.
- Figures / image assets: 4 of 4 opened and compared edge by edge with 260 dpi page crops.
  - algorithm-1.jpg (623x1010): top rule, bottom rule, left and right text edges all inside the
    image (ink from col 5 to 616, row 8 to 1000). Complete.
  - figure-1.jpg (1036x391): both panels; left panel y ticks 4..-3, x ticks -3..2, labels y and x;
    right panel y ticks -0.5..-2.5 (top label "-0.5" complete), x ticks -2.2..-1 (right-most
    label "-1" complete), labels y and x. Ink from col 31 to 1002, row 26 to 354. Not cut.
  - figure-2.jpg (578x395): y ticks 30..-30, x ticks -100..100, labels h and x. Not cut.
  - figure-3.jpg (578x393): y ticks 140..90, x ticks 100..180, labels x_6 and x_5. Not cut.
  - No asset contains foreign text (no caption or body text inside the figure crops).
  - Captions Fig. 1, Fig. 2, Fig. 3 verbatim (260 dpi), label numbers correct.
- Completeness and order: token-level diff of `pdftotext` against paper.md (3362 vs 3348 words of
  3+ letters outside math): the only differences are the arXiv stamp, small-caps headings, math,
  and float positions. No dropped or duplicated passage; no sentence cut at a page or column
  break (checked the joins p1->p2, p2->p3, p3->p4, p4->p5, p5->p6 by eye). Figure 1 is moved from
  the top of p.5 to Section IV-A after the paragraph that introduces it (documented in the
  notes); Figures 2 and 3 sit where the PDF has them. No footnotes or appendix in the PDF.
- Prose: all 7 pages read in full, not only two paragraphs each. p.1 on a 170 dpi full-page
  render; p.2-7 on contiguous 260-300 dpi crops covering every column.
- References: 22 of 22 entries on 300 dpi crops (authors, titles, venues, volumes, pages, years,
  URL of [19], "Acikmese" diacritics in [5], the long dash in [12]): all match.
- Headings and index: 16 headings in paper.md, all real and correctly numbered and nested
  ("Notation" is an unnumbered italic subheading inside Section I in the PDF). All 14 index
  entries exist as exact headings and describe their content correctly. All 4 asset links resolve.
  supplement.md states that no supplementary material was supplied, which is correct.
- Math syntax: all 21 displays and 309 inline formulas of paper.md compile with pdflatex
  (amsmath, amssymb) without errors.
- Conversion notes: every "kept as printed" claim confirmed on >=260 dpi crops: "Proposition 1"
  in IV-A; "M iid samples" and "i = 1,...,n" in Lemma 2; Pos(R[x]^n_d) and "dimension of R[x]^n_d
  is binom(n+2k,n)"; M^{-1} without hat in the optimization problem and z(x) without subscript
  just before it; Phi(t1; t0, x0, u) in Problem 1; N_ap and N_AP; undefined beta and "The input u"
  around eq. (3). Only the location word in the parenthesis claim is imprecise (C1).

### Two questions answered from the package only
1. "How many samples does Algorithm 1 need for the quadrotor example with the full state and with
   the reduced state?" Index -> "B. Planar Quadrotor Model" -> paragraph after Fig. 2: n = 6,
   k = 4, eps = 0.05, delta = 1e-9 gives N = 2,009,600; the reduced-state variant (n = 2) gives
   N = 32,292. PDF p.5 left column prints the same. Recomputing bound (1) from the package's
   formula gives 2,009,600 and 32,292 (and 156,626 for the Duffing example, n = 2, k = 10), so
   the transcribed formula and the printed numbers are consistent.
2. "What accuracy was measured a posteriori for the Duffing example, with how many samples?"
   Index -> "A. Chaotic Nonlinear Oscillator" -> last paragraph: N_AP = 46,052 new samples;
   empirical accuracy 1 - (2 x 10^-5); true accuracy at least 0.99 - 2 x 10^-5 with 99.99%
   confidence, against 0.95 guaranteed by Theorem 1. PDF p.4 right column prints the same.

### Observations that are not findings
- The PDF prints "156, 626" with a thin space (math mode, twice in IV-A) but "46,052",
  "2,009,600", "32,292" tight; the package writes all four the same way inside `$...$`. No
  effect on content; the notes already mention the separators.
- index.md has no row for the heading "II. Preliminaries" (it has no text of its own; its two
  subsections are listed).

### Not checked
- p.1 was read only at 170 dpi (it has no theorem-like block and no display; inline math is
  R^n and the first half of the interval definition, whose second half was checked at 260 dpi).
- The claim "the paper appeared at IEEE CDC 2021" in the notes cannot be checked from this PDF.
- The authors' TeX source under tex-source/ was not opened.

Work directory logs/verify/work/devonport2021data was emptied and removed.
