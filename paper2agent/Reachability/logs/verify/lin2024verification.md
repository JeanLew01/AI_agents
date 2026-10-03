VERDICT: 2 findings (0 A, 0 B, 2 C)

Package: skills/lin2024verification-paper, checked against papers/lin2024verification.pdf (arXiv:2312.08604v2, 16 pages).
No mathematical, factual, numbering, caption, ordering or figure-crop error was found. The two items below are cosmetic.

## Findings

### C1 - Conversion notes: position of the volume markers in Figures 5 and 6 is described slightly wrongly
- Location: paper.md, "## Conversion notes", bullet starting "Figures 1-6 are image crops", snippet:
  "Figures 4-6 mark 'Vol. = 0.782' and 'Vol. = 0.8', 'Vol. = 0.334' and 'Vol. = 0.366', and 'Vol. = 0.19' on the 99.990% safety line". PDF pages 9-10.
- Package says: all five marked volumes lie on the dashed 99.990% safety line (log10(epsilon) = -4).
- PDF prints: true for Figure 4(b) (both dots on the dashed line) and for the grey 0.334 dot in Figure 5(b). The cyan dot labelled
  "Vol. = 0.366" in Figure 5(b) sits slightly below the dashed line (about -4.1 on the left axis), and the cyan dot labelled
  "Vol. = 0.19" in Figure 6(b) sits clearly below it (about -4.25 to -4.3; its label is printed under the line as well).
  The numbers themselves (0.782, 0.8, 0.334, 0.366, 0.19) are correct.
- Confirmed on: 400 dpi crops of Figure 5 and Figure 6 (page 10) and of Figure 4 (page 9); dot centre compared with the dashed line
  and the -4 / -5 tick marks.
- Suggested wording: "... next to the 99.990% safety line (in Figures 5(b) and 6(b) the cyan marker is drawn slightly below the line)".

### C2 - index.md has no row for the Section 3 heading
- Location: references/index.md, table "Main paper"; paper.md heading
  "## 3. Background: Hamilton-Jacobi Reachability, DeepReach, and Safety Verification" (PDF page 3).
- Package says: the index goes from "2. Problem Setup" straight to "3.1. Hamilton-Jacobi (HJ) Reachability"; every other heading of
  paper.md (including the content-free parent "Appendix B. Conformal Proofs") has a row.
- PDF prints: Section 3 has its own heading and a three-line introductory paragraph ("Here, we provide a quick overview ..."), which
  paper.md reproduces correctly. Only the index row is missing.
- Confirmed by: script comparison of all paper.md headings with the index rows; heading and paragraph read on a 260 dpi crop of page 3.

## Coverage

- Theorem-like blocks checked symbol by symbol on 260-280 dpi crops: 7 of 7 (Remark 1 p.4; Theorem 2 p.5; Theorem 3 p.7; Remark 4 p.7;
  Lemma 5 p.8; Remark 6 p.8; Lemma 7 p.14), including printed numbers, titles and where each statement ends. All match.
  Proof blocks: 5 of 5 (proof of Lemma 7, A.1, B.1, B.2, B.3), every inline chain of equalities compared term by term
  (quantile chain in B.1; floor/ceiling chain, incomplete-beta sums and index change in B.2). All match.
- Displayed equations: 14 of 14 numbered ((1)-(14)) plus the 3 unnumbered display lines (two above (11), one above (12)); each tag is
  on the right equation. Inequality directions, binomial sums (2), (5), (9), Beta parameters in (4), (12), (13), floor expressions, the
  conditioning bar in (13)-(14) and all sub/superscripts match.
- Inline mathematics outside theorems: read on 260 dpi crops of pages 3-10 (problem setup; running-example dynamics and constants
  v=0.6, u_min=-1.1, u_max=1.1, R=0.25; HJB-VI, Hamiltonian, controller; correction bound delta; weighted MSE loss and validation
  metric; rocket dynamics, g=9.81, torque bounds +-250, target-set bounds 20.0). All match.
- Numerical values in text and captions: k=731, N=3684118, beta=10^-16, w=10^-3, epsilon<=10^-4 (99.990%), 99.999% -> 99.974%,
  0.56 -> 0.81, 99.968%, 1-beta=0.9, 1-epsilon=0.99979 (99.979%), 0.782 -> 0.8 (2.3%), 0.334 -> 0.366 (9.58%), 0 -> 0.19,
  100m / 10m / 20m, award 2240163. All match.
- Algorithms: none in the paper (0 lines). Tables: none in the paper (0 cells); assets/table and the supp_* directories are empty.
- Figures: 6 of 6 assets opened and compared with 300-400 dpi page crops. All four edges of every asset are intact (titles, axis
  labels, tick labels, legends, panel letters (a)/(b) present; no caption or body text included; a pixel scan found no ink touching any
  border). Captions verbatim, label numbers correct. In-figure values listed in the conversion notes all confirmed: Fig. 1(a) title
  "Fixed N = ~3.7M", "Vol. = 0.56", "Vol. = 0.81", right-axis pairs -3.5 (99.968%), -4.0 (99.990%), -4.5 (99.997%), -5.0 (99.999%);
  Fig. 2(b) points ~116K/k=0, ~368K/k=36, ~1.2M/k=193, ~3.7M/k=731; Fig. 3 title "N = ~3.7M, k = 731", "1-eps = ~0.99979",
  "1-beta = 0.9"; Figs. 4-6 "Vol. = 0.782", "0.8", "0.334", "0.366", "0.19" (C1 is the only imprecision).
  For information, not an error: the notes do not list the slice values printed only inside figures (Fig. 1(b) and 4(a): theta_1 = -1.57,
  with labels "99.974% Safety" / "99.999% Safety" in 1(b); Fig. 5(a): v_y = -200, v_x = 150; Fig. 6(a): v_y = -200, v_x = 50) nor the
  Figure 2 super-title "Achieving a Desired log10(eps) = -3.5 (99.968% Safety) with Different Simulation Budgets N". Asset resolution
  is modest (figure-1.jpg 361x530, figure-3.jpg 276x263) but every label is still readable.
- Completeness and order: whole-document word-level diff of pdftotext against paper.md, run twice (lower-cased words and numbers;
  then case- and punctuation-sensitive). The only differences are page furniture (banner, arXiv stamp, running heads, page numbers,
  copyright line), line-break hyphenation, mathematics layout, the footnote position and the documented move of Figure 5. No dropped,
  duplicated or reordered passage; no sentence cut at a page break. Footnote 1 present once. References: 31 of 31 entries present and
  in order, read against pages 11-13 (11 + 14 + 6).
- Prose spot check: all 16 pages by the automated diff; in addition read by eye on crops of 260 dpi or more: pages 3-10 and 14-16 in
  full; pages 1, 2, 11, 12, 13 (no mathematics) read on 150-170 dpi full-page renders.
- Headings and index: 23 section headings real, correctly numbered and nested; the six figure links resolve; every index row points to
  an existing heading (C2 is the one missing row). SKILL.md and supplement.md ("No corresponding materials were supplied") consistent.
- Conversion notes, "kept as printed" claims, each confirmed on a 260-280 dpi crop: "split conform prediction" (p.8, after Lemma 5);
  "HJI-VI" in Section 6.3 vs "HJB-VI" in Section 3.1 (pp.10, 4); "side length 20m" next to bounds 20.0 (p.9); subscript N,k on the
  sample-problem solution in Appendix B.2 and n in the final binomial sum identified with Equation (9) (p.16); banner "Proceedings of
  Machine Learning Research vol vvv:1-16, 2024" and "(c) 2024 A. Lin & S. Bansal." (p.1); the phrase "in the Appendix of the extended
  version of this article" with footnote mark 1 occurs three times (pp.5, 7, 8); Figure 5 printed at the top of page 10 inside a
  Section 6.3 sentence; (11) and (12) on the last line of a three-line and a two-line display (p.15). All true.

## Two questions answered from the package only

1. "For the running example, what lower bound on the safe fraction of S does the conformal method give at confidence 0.9, and from
   which distribution?" Route: SKILL.md -> index row "5. Conformal Probabilistic Safety Verification Method" -> Theorem 3 / Eq. (4)
   and the Figure 3 caption. Answer: the safe fraction is distributed Beta(N-k, k+1) with k=731, N=3684118; for 1-beta=0.9 the lower
   bound is 1-epsilon = 0.99979 (99.979%). PDF page 7 agrees (a normal approximation of the Beta 10% quantile also gives 0.99979).
2. "What condition links epsilon, beta, k and N in Theorem 2, and how does the proof pass from the induced cost to the true value
   function?" Route: index rows "4. Robust Scenario-Based ..." and "A.1. Proof of Theorem 2". Answer: sum_{i=0}^{k} C(N,i) eps^i
   (1-eps)^(N-i) <= beta (Eq. (2)) gives, with probability at least 1-beta, P_{x in S}(V(x,0) <= 0) <= eps (Eq. (3)); the proof applies
   Lemma 7 with h=x, H=S, f=-J, discards the k constraints with -J(x_i,0) >= 0 so that g* < 0, obtains P(J <= 0) <= P(J < -g*) <= eps
   from Eq. (10), and uses J(x,t) <= V(x,t) from Eq. (1). PDF pages 5 and 14 agree.

## Not checked

- The statement in the conversion notes that the paper appeared in PMLR vol. 242, pp. 719-731 is external to the PDF; not verified.
- The authors' TeX source was not used. Curve shapes in the raster figures were compared by eye only (text labels were read at 300-400 dpi).
- Read-only rule kept: nothing in the package or review directory was modified. All renders were deleted as I went and the work
  directory logs/verify/work/lin2024verification/ was removed at the end.
