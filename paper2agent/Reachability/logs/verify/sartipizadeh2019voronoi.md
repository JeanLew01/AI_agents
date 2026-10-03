VERDICT: 2 findings (0 A, 0 B, 2 C)

Package: skills/sartipizadeh2019voronoi-paper, checked against papers/sartipizadeh2019voronoi.pdf
(arXiv:1811.03643v1, 15 pages). No mathematical, factual, label, numbering, caption, order or
figure-crop error was found. The two items below are typographic only.

## Findings

### C1 (cosmetic) - "Proof:" label weight
- Location: all six proofs in paper.md, e.g. Section 2.4 "**Proof:** The proof is straight forward",
  Section 3 "**Proof:** Let the optimal solution to Problem 1 be" (PDF pp. 5, 6, 7, 8, 9).
- Package: the run-in label is bold (`**Proof:**`).
- PDF: the label is italic, not bold ("*Proof:*"), on every proof.
- Confirmed on 260-280 dpi crops of pp. 5-9. The conversion notes describe the theorem labels
  (bold label, upright body) but say nothing about the proof label.

### C2 (cosmetic) - Algorithm 1 block headers
- Location: Section 4.3, transcription lines "**Offline (independent of $x_0$):**" and
  "**Online (depends on $x_0$):**" (PDF p. 10).
- Package: bold upright.
- PDF: bold italic ("***Offline (independent of x0):***", "***Online (depends on x0):***").
- Confirmed on a 280 dpi crop of p. 10 and in assets/figure/algorithm-1.jpg itself.

## Conversion-note claim asked about in the task (Theorem 1 event order): CONFIRMED

On a 280 dpi crop of PDF p. 6:
- Theorem 1 prints `P_Z^{x0,U*_K}{ p*(x0) - p*_K(x0) >= delta } <= beta, if K >= -ln(beta)/(2 delta^2)` (13).
- Eq. (15), the unnumbered final chain, and the last sentence of the proof ("To obtain the desired
  probabilistic guarantee ...") all print `{ p*_K(x0) - p*(x0) >= delta }`.
- Question 1 (p. 4, 280 dpi) prints `{ p*_K(x0) - p*(x0) >= delta } <= beta or equivalently
  { p*(x0) >= p*_K(x0) - delta } >= 1 - beta`.
The package reproduces each of these exactly as printed; note (a) describes the PDF correctly.
Small remark, not a finding: note (a) lists "the paragraph after it" among the places that "use"
the set {p*_K - p* >= delta}; that paragraph states the event in words ("exceeds the true terminal
time probability ... by more than delta"), not in symbols. The meaning is the same.

Other "kept as printed" claims, each confirmed on the PDF (260-400 dpi):
- (b) proof of Theorem 3 (p. 10): `\hat p^*_{\hat K}` with a hat on p, `(z^{(j)} = 0)` without hat,
  "alpha^(j) is the set of original scenarios", "J ... the subset of C*".
- (c) (6c) prints `R = {x | FX <= h}`; text prints `F in R^{L x n_x}` (p. 3).
- (d) (9) prints `forall j, l in N_[1,K^] and j != l` (p. 5).
- (e) `w_k`, `x_k` in the text of Section 2.1 versus `t` in (1) (p. 2).
- (f) `\varepsilon^{(j)}` for the buffer vector and `\epsilon_l^{(j)}` for components, in (17), (18),
  Problem 3, Remark 2, Theorem 2, Figure 3 caption, Algorithm 1 step 7 (pp. 7-10).
- (g) `3 omega x` in (23), `W_N`, "exponentially increases exponentially", "coincides the "knee"" (p. 11).
- (h) abstract: "we propose a Voronoi partition-based to check" (p. 1).
- Also faithful and not in the notes: p. 4 "violates the reach-avoid constraint X^(j) in R" (printed so).
- Float placement claims (Fig. 3 top of p. 9 between Theorem 2 and its proof; Fig. 4 top of p. 12
  splitting the sentence "... terminal time probability and the | mean value ..."; Table 1 and Fig. 5
  on p. 13 after the Conclusion; footnote at the bottom of p. 1; no page numbers) are all correct.
  The package sentence split by Figure 4 in the PDF is whole and not cut.

## Coverage

- Theorem-like blocks checked symbol by symbol (260-280 dpi crops, one 400 dpi crop): 15 of 15 -
  Problems 1-3 (objective and every constraint, including index ranges and the trailing text),
  Remarks 1-3, Questions 1-2, Lemmas 1-4, Theorems 1-3; plus all 6 proofs. Statement ends agree with
  the italic extent in the PDF.
- Displayed equations: 36 of 36 - the 30 numbered ones (1)-(5), (6a)-(6c), (7)-(13), (14a)-(14c),
  (15)-(26), each tag on the right equation, and the 6 unnumbered ones (Problem 2 MILP, Problem 3 MILP,
  phi(W) := G_w W, X^(psi^(j)) in Lemma 3, final chain in proof of Theorem 1, the chain in Theorem 3).
  Trailing punctuation of the displays also matches. One doubtful spot re-cropped at 400 dpi:
  `sum_{j=1}^{K^} alpha^(j) = K` in Problem 3 - the upper limit is K-hat, as in the package.
- Algorithm 1: 14 of 14 lines (title, Input, Offline header + steps 1-7, Online header + steps 1-2,
  Output) against the 280 dpi crop of p. 10 and against the image asset.
- Table 1: 21 of 21 cells (3 header cells, 6 rows x 3, counting the "Algorithm 1" label row) in both
  the CSV and the Markdown table, against a 260 dpi crop of p. 13; caption verbatim.
- Figures: 6 of 6 assets opened (figure-1 ... figure-5, algorithm-1) and compared with the page on all
  four edges. Figure 1 (453x438): all 7 red crosses, the top dot, the two right-most dots, the R arrow
  and dashed line are inside with margin. Figure 2 (530x373): zoom circle, top / right / bottom polygon
  vertices inside. Figure 3 (443x440): both rotated labels, both hatched walls, the `F_1X = h_1` label
  and the dashed line to the right are inside. Figure 4 (1066x841): panels (a), (b), (c) with their
  panel letters, all tick labels, y labels, legend and the `K^` x label of (c) (panels (a), (b) have no
  x label in the PDF either). Figure 5 (553x445): axes, tick labels, x / y labels, legend. No foreign
  text in any asset. Captions of Figures 1-5 verbatim; numbers correct.
- Completeness and order: all 15 pages read next to the package. Additionally a script compared runs
  of 5 or more plain words from `pdftotext` of each page with the package (300 runs) and the reverse
  (378 runs); every non-match was inspected and is a math token, a pdftotext reading-order artefact or
  a moved float, none is a dropped, added or duplicated passage. Section headings 1-6, 2.1-2.4, 4.1-4.3
  are real and correctly numbered and nested. Footnote present once. References [1]-[26]: all 26
  entries compared at 260 dpi (pp. 14-15), no difference.
- Prose spot check: every page 1-13 (all body paragraphs were read against the package, not only two
  per page); pp. 1, 12 and the top half of p. 2 at 170 dpi / pdftotext (prose only), everything else at
  260-280 dpi.
- Index: all 16 headings listed in references/index.md exist in paper.md with exactly that text, and the
  listed contents are where the index says. Asset links in paper.md resolve to existing files.
- Question 1: "How many scenarios does the sampled MILP need for a violation parameter delta and risk
  beta?" Index -> "3 Scenarios required to meet given failure tolerance" -> Theorem 1, (13):
  K >= -ln(beta) / (2 delta^2), independent of the horizon N. PDF p. 6: same.
- Question 2: "How is the constraint buffer of the reduced MILP defined, and what does 40 cells cost
  and achieve in the example?" Index -> "4.1 Seed Selection and Buffer Computation" -> Lemma 4,
  (17)-(18): epsilon_l^(j) = max over phi in V^(j)_{Phi_K}(Psi_K^) of (F_l phi - F_l psi^(j)),
  l in N_[1,L]; index -> Section 5 -> Table 1: K = 2000, K^ = 40 gives 0.8492 in 0.6 s (Fourier
  transform [10]: 0.862 in 66 s). PDF pp. 8 and 13: same.

## Not checked

- The statement in the conversion notes about the title of the ACC 2019 proceedings version
  ("... of Linear Systems") is not verifiable from this PDF and was not checked.
- The authors' TeX under tex-source/ was not opened; everything above is against the PDF only.
- pdflatex compilation of the package formulas was not run; the LaTeX was read, not compiled.
- supplement.md states that no supplementary material was supplied; the PDF has no appendix, nothing
  further to check there.

Work directory logs/verify/work/sartipizadeh2019voronoi/ is empty (all renders and scripts deleted).
