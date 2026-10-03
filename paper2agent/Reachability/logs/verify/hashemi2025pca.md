VERDICT: 2 findings (0 A, 0 B, 2 C)

Package: skills/hashemi2025pca-paper vs papers/hashemi2025pca.pdf (arXiv:2505.14935v1, 16 pages).
No mathematical, factual, numbering, caption, order or figure-crop error was found. The two
items below are cosmetic only.

## Findings

### C1 - end of Definition 4 and of Proposition 5 is not visible in the package
- Location: paper.md, "3.2 Accurate Inflating Hypercubes via Principal Component Analysis";
  PDF p. 9.
- (a) Snippet "Here, $\sigma^{\mathsf{sim}}_{s_{0,i}}, i \in |\mathcal{R}^{\mathsf{calib}}|$ refers
  to the trajectory starting at the $i^{th}$ initial state ... The parameters $r^j_i$ are also as
  defined in equation (11)." The PDF prints these two sentences in italics directly under
  display (14), i.e. they are the closing part of the body of Definition 4. The package writes
  them as an ordinary upright paragraph after the display, indistinguishable from running text.
- (b) Snippet "and $r^j$ is the mapped version of prediction errors $R^j,\ j\in [n\mathrm{K}]$ on
  principal axes." The PDF prints this line in italics under display (15), i.e. it is the last
  clause of Proposition 5. Same presentation in the package (plain paragraph before "**Proof.**").
- Words and symbols are correct in both; only the block boundary is lost (the conversion notes
  say bodies are written upright and that blocks end "where the TeX environment ends", but
  paper.md itself gives no marker). Confirmed on 300 dpi (Def. 4) and 350 dpi (Prop. 5) crops.

### C2 - "Proof." emphasis
- Location: paper.md, same section, "**Proof.** The proof follows as the residual"; PDF p. 10.
- Package: bold "Proof."; PDF: italic "Proof." (300 dpi crop). Typography only.

## Requested confirmations (all confirmed on the PDF, crops at 260-350 dpi)

- Sec. 2.3 (p. 5): ordinary CI "Pr[rho < rho_l] >= delta"; robust CI "TV(J^real, J^sim) <= tau
  with a threshold tau > 0, we have Pr[rho < rho_{l*}] > delta". As the package says.
- Eq. (4) (p. 5): "l* := ceil((L+1)(1+1/L)(delta+tau)), l* <= L." Matches symbol by symbol.
- Eq. (6) and the line after (7) (p. 5-6): ">= delta" on both sides; "Since Pr[P* = T] >= delta".
- delta-confident flowpipe (p. 6): "Pr[sigma^real_{s0} in X] >= delta". Lemma 3 (p. 6):
  "Pr[PE in deltaX] > delta". As the package says.
- Sec. 2.4 (p. 6): "is less than tau > 0" (strict). Sec. 3.2 (p. 9): "a radius tau > 0 such that
  ... TV(J^real, J^sim) < tau" and "Pr[rho < rho*_{delta,tau}] > delta".
- Proposition 5 (p. 9): "TV(J^real, J^sim) < tau", conclusion "Pr[P(r^1,...,r^{nK}) = T] > delta",
  "Assume rho*_{delta,tau} is the delta-quantile of rho ~ J^real". Proof (p. 10):
  "Pr[rho <= rho*] >= delta", "rho < rho* <=> |r^j| < rho* omega_j", ends ">= delta".
- tau = 0 for Experiments 1-2: Sec. 4 text (p. 10) "a 12-D quadcopter with tau = 0" and Table 1
  (p. 11) tau column "0, 0, 4%". Sec. 2.2 (p. 4) additionally prints "tau >= 0" with
  "tau = TV(J^sim, J^real)"; the notes do not mention this line, which is not an error.
- One shared counter: Definition 1, Definition 2, Lemma 3, Definition 4, Proposition 5, Remark 6.
- All other "kept as printed" slips of the conversion notes are really printed so: T_i in (8);
  second factor of (10) without index i and transpose on the first factor; "i in |T^trn|",
  "i in |R^calib|", "j in nK" without brackets; italic V = diag(V^1,...,V^N) and PE-bar without q
  after (17); stray "]" in the subscript "1x6]" of Sigma_v in Sec. 4.1; TV arguments in both
  orders; realization s_1..s_K vs S_0..S_K; "Scalabilty"; "caligraphic"; "In other word";
  "this results"; "restricted to utilized approx star".
- Converter's arithmetic in the last note re-computed: l* = 20000 for L = 20000, delta = 0.9999,
  tau = 0 ((L+1)^2/L * 0.9999 = 19999.99985); l* = 9902 for L = 10000, delta + tau = 0.99;
  451 = |{50..500}|, 4501 = |{500..5000}|. Correct.

## Coverage

- Theorem-like blocks checked symbol by symbol: 6 of 6 (Def. 1, Def. 2, Lemma 3, Def. 4,
  Prop. 5, Remark 6) plus the proof of Prop. 5; numbers and titles correct.
- Displays checked: 18 of 18 numbered, (1)-(18), each on a 260-350 dpi crop including end
  punctuation and the printed number; the PDF has no unnumbered display. "=" vs ":=" in (6) and
  (15) as printed. All 18 displays and 438 inline formulas compile with pdflatex (amsmath/amssymb).
- Algorithms: none in the paper (0 lines).
- Table 1: 30 data cells + 10 column names + 4 group headers, CSV and Markdown table, all equal
  to the print (300 dpi); group-to-column assignment checked by header position; caption verbatim.
- Figures: 6 of 6 assets opened and compared with the page on all four edges (page crops at
  260-300 dpi; asset edge strips of Figures 1, 3, 5, 6 enlarged 3-4x). All panels, tick labels,
  axis labels, legend (Fig. 6), "k = 0"/"k = K" (Fig. 1) and "time step k = 1/2" (Fig. 2) are
  inside; nothing cut; no foreign text (Figure 5 does not include Figure 6's tick labels, which
  sit 0.18 in to its right). Captions 1-6 verbatim, numbers correct. Note only: Figure 1 asset is
  685x200 px and Figure 6 is 238x230 px; small labels are legible but soft.
- Completeness and order: word-level diff of pdftotext (all 16 pages) against paper.md, plus a
  token diff with numbers and punctuation; no dropped, duplicated or altered prose, nothing cut at
  the page breaks p.1/2, 2/3, 3/4, 4/5 (Definition 2), 5/6, 6/7 (sentence around Figure 1 and
  (8)), 14/16 (Section A.1 around the float page 15). Six footnotes present once each, text
  verbatim, marks at the printed words. References: 28 of 28 entries, token-identical to the PDF
  (authors, titles, volumes, pages, years); italics spot-checked on 7 entries (p. 13).
- Prose read on crops (>= 250 dpi) in addition to the diff: p. 2 (two paragraphs), p. 3
  (Notation, 2.1), p. 4-11 (every math-bearing passage and at least two paragraphs per page;
  the few purely verbal paragraphs there by pdftotext and diff only), p. 14 and 16 (all appendix
  text); p. 1 at 110 dpi plus diff, p. 12 by diff, p. 13 by diff and one 260 dpi crop; p. 15 is
  a float page (captions checked).
- Headings and index: 21 index rows all resolve to existing headings in paper.md; numbering and
  nesting as printed (5 Acknowledgements before 6 Conclusion; Appendix A after References).
- Question 1: "Which calibration rank is used under distribution shift and what does it
  guarantee?" Index -> "2.3 Conformal Inference & Probabilistic Reachability": rank (4)
  l* = ceil((L+1)(1+1/L)(delta+tau)), l* <= L, giving Pr[rho < rho_{l*}] > delta when
  TV(J^real, J^sim) <= tau, tau > 0. Agrees with PDF p. 5.
- Question 2: "What is the setup of Experiment 3?" Index -> "4 Numerical Evaluation" (Table 1),
  "4.2", "A.3": 27-D powertrain, delta = 95%, tau = 4% (noise covariance 20% larger), K = 4000,
  delta t = 0.0005, N = 4000, T_q = 1, ReLU nets [27, 54, 27], 400 trained models (40.6 sec avg),
  |T^trn| = 10,000, 4000 reach computations at 0.064 sec with approx-star, hypercube 142.02 sec,
  |R^calib| = 10,000. Agrees with PDF p. 11 and 16.

## Not checked

- The statement in the conversion notes that the paper appeared in NeuS 2025, PMLR vol. 288,
  pp. 693-707: the PDF carries only the arXiv stamp, so this cannot be confirmed from it.
- Italic/upright emphasis of the reference entries on p. 12 and 14 (text is token-identical).
- Curve shapes inside the plots were compared only visually between asset and page, not by pixel.
- Process claims of the notes (which resolutions the converter used, the external review notes).
- supplement.md says no supplementary material was supplied; none is attached to the PDF.
