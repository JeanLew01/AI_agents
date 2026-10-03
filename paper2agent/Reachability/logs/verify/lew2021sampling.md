VERDICT: 2 findings (0 A, 1 B, 1 C)

Package: skills/lew2021sampling-paper (paper.md 518 lines). Ground truth: papers/lew2021sampling.pdf (16 pp.).
No mathematical or factual conversion error was found. Algorithms 1-2, eq. (5), Theorems 1-2, Definitions 1-2,
the Appendix A proof and eqs. (6)-(22) all agree with the PDF symbol by symbol.

## Findings

### 1. [B] Figure 6 asset is cut at the bottom (x-axis tick labels missing)
- Location: paper.md, heading "6 Results and Applications", link `[Figure 6](../assets/figure/figure-6.jpg)`,
  caption "**Figure 6:** (**robUP!**) can be used to quickly invalidate unfeasible homotopy classes"; PDF p. 8
  (wrapped figure at the right of the "Robust planning for a spacecraft" paragraph).
- Package: `assets/figure/figure-6.jpg` (205 x 328 px) ends at the bottom axis line. The x-axis tick labels are
  absent, and the y-axis tick label "0" is clipped (only its upper half is visible at the lower edge).
- PDF: below the bottom axis the figure prints the x-axis tick labels "0" and "2" under their tick marks, and the
  y tick label "0" is complete.
- Confirmed: PDF crop of p. 8 at 300 dpi (`-x 1740 -y 700 -W 400 -H 680`) against a 4x enlargement of the bottom
  90 px of the asset. The rest of the figure (x_N, x_0, three X_obs discs, y ticks 1-5, both trajectories, top
  edge) is complete. Fix: extend the crop about 25 px (at asset scale) downwards; the caption starts below that.

### 2. [C] Appendix A: dots of the composition are baseline dots in the PDF
- Location: paper.md, heading "A Proof of Theorem 2", first proof paragraph, snippet
  `\boldsymbol{w}_{k-1})\circ\dots\circ\boldsymbol{f}(\boldsymbol{x}_0,\boldsymbol{u}_0,\boldsymbol{\theta},\boldsymbol{w}_{0})$, which is also continuous`; PDF p. 11.
- Package: `\circ\dots\circ` (renders as centred dots between the two binary operators).
- PDF: prints "∘. . .∘" with dots on the baseline (i.e. `\ldots`) in this place only; eq. (2) and the definition
  of x_k(z) after eq. (5) print centred dots, which the package matches.
- Confirmed: 300 dpi crop of p. 11. Purely typographic, no change of meaning.

## Coverage

Method: paper.md read completely next to the PDF; every page rendered (170 dpi full page, then 260-340 dpi crops
for all mathematics, algorithms, theorem-like blocks, the table and captions); a word-level diff of `pdftotext`
(per page) against paper.md for the whole document; a token-exact diff for the reference list.

- Theorem-like blocks checked symbol by symbol at >= 300 dpi: 5 of 5 - Definition 1 (p. 4), Theorem 1 with (C1),
  (C2) (p. 5), Theorem 2 (p. 5), Theorem 2 restated (p. 11), Definition 2 (p. 14) - plus the whole proof of
  Theorem 2 (pp. 11-12: both set-up paragraphs, (C1), (C2) steps (1)-(3), closing paragraph). Numbers, titles,
  quantifiers, set relations (⊂ vs ⊆), sub/superscripts and the sampling assumption P(x_k^j ∈ G_k) > 0 all match.
- Displayed equations checked: 29 of 29 - the 24 numbered ones (1)-(18), (19a)-(19c), (20)-(22), each with its
  printed number on the right equation, and the 5 unnumbered ones (recursion for X~_{k+1} on p. 3; two displays in
  proof step (2) and one in step (3) on p. 12; error decomposition on p. 14). Also the inline formulas that carry
  content: Q_nom,k = h Q_k h^T, Q_{k+1} and c (p. 14), the Z set (pp. 6, 11), delta_{k,i}, Delta_k, B^s, Q_k =
  s diag(...), a^T mu + (a^T Q_k a)^{1/2} <= b (p. 16), the spacecraft dynamics and bounds (p. 8), the C.2
  hyper-parameters, Unif ranges and timings (p. 15).
- Algorithm lines: Alg. 1 (title, Parameters, Output, lines 1-4) and Alg. 2 (title, Input, Parameters, Output,
  lines 1-8) = 12 numbered lines + 7 header lines, at 300/340 dpi; numbering, loop nesting (lines 4-7 inside the
  for of line 3, line 8 outside), arrows vs "=", bold eta, Proj_Z, union in line 7 and Co(.) in line 8 all match.
  Both algorithm image assets are complete.
- Table cells: the one table (embedded in Figure 5), 24 of 24 cells (header row, 3 row labels, 15 values) in both
  the Markdown table and assets/table/figure-5-table.csv, at 320 dpi. Columns X_0, X_1, X_2, X_4, X_5 as printed.
- Figures: 10 figure assets + 2 algorithm crops opened; all 10 captions compared with the page. Complete: Figures
  1-5, 7-10. Cut: Figure 6 (finding 1). Figure 5's crop contains its own printed caption (L-shaped float); this is
  stated in the conversion notes and is not foreign text. Label numbers are correct (Figures 7-10 keep their
  printed numbers although stored under supp_figs/).
- Completeness and order: the word-level diff (all alphabetic words, plus a separate pass on 1-2 letter words)
  shows no dropped, duplicated or reordered prose; every difference is either a float/caption/footnote that
  pdftotext interleaves with the text or math debris. The paragraphs wrapped around floats are complete and in
  order: p. 4 ("We propose the simple sampling-based procedure ..." beside Alg. 1), p. 8 ("Robust planning for a
  spacecraft" beside Fig. 6), p. 13 ("Next, we justify the choice of M = 100 ..." beside Fig. 8 and "Adversarial
  sampling for sensitivity analysis" beside Fig. 10), each re-read at 300 dpi. No sentence is cut at the page
  breaks 1/2, 2/3, 6/7, 11/12, 15/16. Footnotes 1-5 present once each; placement as described in the notes.
- References: [1]-[50] present once each; token-exact against pdftotext (authors, titles, venues, volumes, pages,
  years, URLs), pages 9-11 also viewed (150-170 dpi).
- Prose spot check (word for word, at least two paragraphs per page where the page has prose): pp. 1-8 and 11-16;
  p. 9 Acknowledgments + entries [1]-[21]; p. 10 is references only ([22]-[45]).
- Headings and index: all 16 headings of paper.md exist in the PDF with the printed numbering and nesting (C.1 and
  C.2 under C); every "Exact heading" of references/index.md exists in paper.md and its description points to
  content that is really there (equation ranges, figure numbers, footnote locations). All 13 asset links resolve.
- Two questions answered from the package only (SKILL.md -> index.md -> section):
  1. "What does robUP! maximise and what is one adversarial iteration?" Index row "4 Adversarial Sampling ..." ->
     eq. (5): L^M(z) = (1/N) sum_k ||x_k(z) - c_k^M||^2_{Q_k^M}, Q_k^M = inverse of the sample covariance with
     1/(M-1), c_k^M the geometric centre of X_k^M; Alg. 2 lines 4-7: z^j <- z^j + eta grad_z L^M(x^j_{1:N}),
     z^j <- Proj_Z(z^j), re-propagate, X_N^i <- X_N^{i-1} ∪ {x^j_{1:N}}; return Co(X_N^{n_adv}). Matches p. 6.
  2. "How is the next ellipsoid shape matrix obtained in the Lipschitz baseline?" Index row "C.1 ..." -> (13)-(15):
     Q_g_k = n diag((L_{g_i} lambda_max(Q_k)^2)), Q_{k+1} = ((c+1)/c) Q_nom,k + (1+c) Q_g_k,
     c = sqrt(Tr(Q_nom,k/Tr(Q_g_k)) as printed (unmatched parenthesis), Q_nom,k = h Q_k h^T. Matches p. 14.
- Conversion notes: every "kept as printed" claim was checked on a >= 260 dpi crop and is what the PDF prints:
  calligraphic K in the intersection of Definition 1 next to "every compact set K"; U^{k-1} x W^{k-1} (Section 3,
  Theorem 2), U^N x W^{N-1} (Alg. 1 description), Z = X_0 x U^k x Theta x W^{k-1} (Section 4, proof); index range
  i = 1,...,k-1 in (2); the extra ")" after w_0 in the definition of x_k(z); Figure 5 columns X_0, X_1, X_2, X_4,
  X_5; "for i=1,...,13" / "for i=4,5,6" and theta_k in Section 6; h Q_k h^T, the position of the square in (14),
  the unmatched parenthesis in c; Gamma(n/2+2) in (17); spellings "innacuracies" (p. 3), "anynomous" (p. 9), "news
  avenues" (p. 8), "vizualize" (p. 13), "conludes" (p. 12). Source line (arXiv:2008.10180v2 [eess.SY], 8 Nov 2020,
  CoRL 2020 footer, page ranges) is correct.

## Not checked / limits
- Reference entries were not re-read at >= 250 dpi; they rest on the token-exact pdftotext diff plus a 150-170 dpi
  read. Entry [25] prints "non-" at a line end followed by "linear"; whether the hyphen is part of the title cannot
  be decided from the PDF (package writes "non-linear"); not counted as a finding.
- Running prose outside the cropped regions was read at 170 dpi, not at 250 dpi (the word diff covers it).
- Plot contents (curves, tick values inside Figures 4, 5, 7-9) were only checked for completeness of the crop,
  not digitised. The claim in the notes that formulas were checked on 220-260 dpi renders is not verifiable.
- The TeX source under tex-source/ was not used.
