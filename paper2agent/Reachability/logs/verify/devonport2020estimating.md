VERDICT: 1 findings (0 A, 0 B, 1 C)

# Verification of devonport2020estimating-paper against papers/devonport2020estimating.pdf

Independent check of `skills/devonport2020estimating-paper` (SKILL.md, references/index.md,
references/paper.md, references/supplement.md, assets/) against the 10-page PDF. No TeX source
exists for this key, so every formula was compared with page crops. Nothing in the package was
edited.

## Findings

### C1 (cosmetic) - upright `\mathrm{e}` in Theorem 1 where the PDF prints math-italic e

- Location: paper.md, `## 3. Scenario Optimization`, Theorem 1, the line after equation (5):
  `where $\mathrm{e}$ is the Euler number, then a minimizer of (4), ...` (PDF page 4).
- Package: `$\mathrm{e}$` (upright roman e).
- PDF: a slanted math-italic *e*, the same glyph as the `e` in the fraction `e/(e-1)` of
  equation (5) directly above it (and as in Theorem 2, Algorithm 1 and equation (11), which the
  package correctly writes as plain `e`).
- Suggested text: `where $e$ is the Euler number, ...`.
- Confirmed on a 400 dpi crop of Theorem 1 (both glyphs side by side) and a 700 dpi crop of
  the words "where e is the Euler number". No change of meaning; the only effect is that the
  package shows two different-looking symbols for one constant.

No A or B findings.

## Conversion notes checked (all confirmed as printed in the PDF)

- Eq. (7) chance constraint is printed `P_Z(||AZ - b||_p - 1 <= 0) <= 1 - eps,` with a
  less-or-equal sign (260 dpi crop, page 5). Kept-as-printed claim is correct.
- Algorithm 1 Output line prints `{x : ||Ax + b||_p <= 1}` with a plus sign (300 dpi crop,
  page 6), while (6) and (8) print `Ax - b`. Correct.
- Section 3 prints `Theta \in R^{n_theta}` with an element-of sign (260 dpi, page 4). Correct.
- Theorem 1 starts with lower-case `let` (400 dpi, page 4). Correct.
- Norm bars: `||` (two single bars) in the body text and in (6), (7); true double bars in
  Algorithm 1 and (8). Correct as described.
- "No proceedings banner, running head or printed page number": correct for all 10 pages
  (text layer of every page, plus full-page renders of pages 1, 2, 3, 6, 8).
- "PDF produced 2020-05-01": matches the PDF metadata (CreationDate 1 May 2020).
- Not verifiable from the PDF: the bibliographic statement "PMLR vol. 120, pp. 75-84" in the
  first note. The PDF itself prints no venue, volume or page range. Not counted as a finding.

## Coverage

- Theorem-like blocks: 2 of 2 checked symbol by symbol (Theorem 1 at 400 dpi, Theorem 2 at
  260 dpi with the sample-size line at 520 dpi), plus the Proof of Theorem 2 (260 dpi).
  Labels, titles and numbers match, including "(Tempo et al. (2012), Corollary 12.1)".
- Displayed equations: 11 of 11 checked, (1)-(11), at 260-400 dpi. Numbers sit on the right
  equations; order in paper.md is 1-7, 9, 10, 8, 11, which is the PDF's reading order because
  (8) is inside the Algorithm 1 float on page 6. Trailing punctuation of each display matches
  (comma after (1), (3), (4), (5), (7), (11); semicolon after (9); period after (10); none
  after (2), (6), (8)).
- Sample-size bounds: Theorem 2 / Algorithm 1 `N = ceil( (1/eps) (e/(e-1)) (log(1/delta) +
  n(n+1)/2 + n) )` and (11) `N_diag = ceil( (1/eps) (e/(e-1)) (log(1/delta) + 2n) )` match the
  crops. Arithmetic cross-check of the transcribed formulas with n = 6, eps = 0.05,
  delta = 1e-9 gives 1509.94 -> 1510 and 1035.35 -> 1036, the values printed in Section 5.
- Algorithm 1: all 10 printed lines checked at 300 dpi (caption, Input, Output, Set N, forall,
  two loop-body lines, end, Solve + (8), return). The PDF has no line numbers; nesting of the
  two loop-body lines is preserved. The paper's missing comma in "from X_0 U, and D" is kept.
- Table 1: 18 of 18 cells (6 header, 12 body) checked at 300 dpi against both table-1.csv and
  the Markdown table; caption verbatim.
- Figures: 2 assets viewed. figure-1.jpg is the complete Figure 1 (three panels with titles,
  both axis labels on each, the x10^-3 exponent of panel 3, the full four-entry legend), no
  foreign text; caption verbatim. algorithm-1.jpg is the complete Algorithm 1 box.
- Completeness and order: word-level diff of the whole PDF text layer against paper.md
  (after de-hyphenation, math masked). The only differences are math tokens, figure tick
  labels and diacritics the text layer splits. No dropped or duplicated passage, no sentence
  cut at any of the nine page breaks, no footnotes in the PDF, 19 of 19 reference entries
  present in the printed order. All 209 inline math fragments were listed and compared with
  the crops; all displays and inline fragments compile with pdflatex without error.
- Prose spot check: every page. Pages 1 and 2 read in full at 170 dpi; pages 3-7 read in full
  at 260 dpi; page 8 (caption, table, Conclusions, Acknowledgments) at 170/300 dpi; pages 9-10
  (references, including accented names and the Bertsekas URL) at 260 dpi. Emphasis (italic
  terms) matches on all pages.
- Headings and index: 10 headings match the PDF in text, number and nesting (1, 2, 3, 4, 4.1,
  4.2, 5, 6, Acknowledgments, References). All 12 rows of the main-paper index point to
  headings that exist with the stated content; the three asset links in paper.md resolve.
  The supplement row "Document beginning" is not a literal heading of supplement.md, but it
  is the same template row in all 16 packages and supplement.md correctly says that no
  materials were supplied, so it is not counted.
- Question 1: "How many trajectories does the exoskeleton example need for the full and the
  axis-aligned variant, and with which guarantee parameters?" From index -> "5. Example":
  p = 2, eps = 0.05, delta = 1e-9, N = 1510, N_diag = 1036. PDF page 7 prints the same.
- Question 2: "How was the a-priori guarantee validated afterwards, and what were the
  measured values?" From "5. Example" and Table 1: 46,052 additional samples, one-sided
  Chernoff bound, estimate exceeds the true measure by at most .01 with confidence 0.9999;
  measures 0.9971 / 0.9927 / 0.9964 (unconstrained) and 0.9977 / 0.9971 / 0.9961
  (axis-aligned) at t = 0, 1.75, 3.5. PDF pages 7-8 print the same (and
  log(1e4) / (2 * 0.01^2) = 46051.7 is consistent with 46,052).

## Not checked

- The venue, volume and page range quoted in the first conversion note (not in the PDF).
- Individual data points inside the Figure 1 scatter plots (only completeness of the crop).
- Correctness of the cited source of Theorem 1 (Tempo et al., Corollary 12.1); only what
  this PDF prints was compared.
