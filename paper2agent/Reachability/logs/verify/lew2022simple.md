VERDICT: clean

# Verification of lew2022simple-paper against papers/lew2022simple.pdf

Independent check of `skills/lew2022simple-paper` (SKILL.md, references/index.md, references/paper.md,
references/supplement.md, 8 figure assets) against the 25-page PDF (arXiv:2112.05745v3). I read
paper.md completely, in order, next to the PDF pages. No severity A, B or C finding.

## Findings

None.

Every difference I found between a careful reading of the mathematics and the package turned out to be
what the PDF prints (a slip of the paper itself, reproduced faithfully and listed in the conversion
notes), so none of them is a finding. See "Conversion notes" below.

## Coverage

Renders: pp. 4-10 and 15-25 as three overlapping 260 dpi strips per page (full text width), plus a
400 dpi zoom on p. 17 and a 260 dpi margin crop on p. 22 (overfull line); pp. 1-3 at 170 dpi full page;
p. 12 at 150 dpi; Figure 6 region of p. 10 at 150 dpi. All renders deleted; TMP is empty.

**Theorem-like blocks: 21 checked symbol by symbol at 260 dpi, 21 match** (label, number, title,
quantifiers, inequality directions, sub/superscripts, hats/bars/tildes, set relations, constants).
- Main text (8): Assumption 1 (p. 4), Theorem 1 (Asymptotic Convergence) (p. 5), Assumption 2,
  Assumption 3, Theorem 2 (Finite-Sample Bound) (p. 6), Assumption 4 (p. 6), Assumption 5, Corollary 1 (p. 7).
- Appendix (13): Definition 1 (Random compact set), Theorem 3 with (C1), (C2) (pp. 15-16); restated
  Assumption 1 and Theorem 1 ("P-almost surely") (p. 16); Lemmas 2, 3, 4, 5 (p. 19); restated Theorem 2
  (two probability bounds, p. 20); Remark on dY in f(dX) (p. 21); Lemma 6, restated Corollary 1 (p. 22);
  Lemma 7 (p. 23). There is no Lemma 1 in the PDF, as the notes say.
- Points checked specifically because the reader will quote them: Assumption 3 ball radius eps/(2L) and
  "for all x in dX"; Theorem 2 delta_M = D(dX, eps/(2L))(1 - Lambda_eps^L)^M, conclusion
  d_H(Yhat^M, H(Y)) <= eps and Y subseteq Yhat_eps^M; Corollary 1 Lambda_eps^{r,L} =
  lambda(B(0, eps/(2L)) cap B(r, r)), delta_M with (1 - p_0 Lambda_eps^{r,L})^M, Assumptions 2, 4 and 5;
  Lemma 3 "for all eps in [0, delta/L]"; Lemma 4 subscripts Y_{2eps}^M vs Y_eps^M and "subset" (not
  "subseteq"); Lemma 5 "eps >= 0", upright Y vs calligraphic Y; Lemma 6 "for any eps >= 0".

**Proofs: 12 checked line by line, 12 match.** Three short main-text proofs (pp. 5-7); proof of Theorem 1
with steps (C1), (C2), (C2.1)-(C2.3) (pp. 16-19); proofs of Lemmas 2, 3, 4, 5 (p. 20); proof of
Theorem 2 (p. 21); proof of Lemma 6 and of Corollary 1 (p. 22); proof of Lemma 7 (pp. 23-24).
Index ranges of every union/intersection/sum (N=1, N=0, N=M_eps, M=N, M=0, M=2, M=1, M=M_eps, i=0),
the 2M+1 / 2M+2 / 2(i+1) subscripts, and every subset vs subseteq vs nsubseteq were compared.

**Displayed equations: 45 of 45 checked** (all displays in paper.md), including the 11 numbered ones:
(1), (2), (3) on p. 4; (4a), (4b) on p. 10; (5), (C1), (C2) on p. 15; (6) on p. 17; (7) on p. 18;
(8) on p. 19. Each printed number sits on the right equation; no unnumbered display carries a tag.
The Appendix C cases formula V(r,a), c_1/c_1, and Lambda = V(eps/(2L), c_1) + V(r, c_2) match (p. 22).
The Appendix E.2 sample-size computation matches (p. 25): X = [2.5,3] x [-0.25,0.25],
D <= 2(0.5+0.5)/(2 eps/(2L)) + 1 = 2/eps + 1, Lambda_eps^L = (2 (eps/2L))/(4 * 0.5) = eps/2,
M >= (log delta_M - log D)/log(1 - Lambda_eps^L) ~ 1376, probability 1 - 10^-4.
All 45 displays and 823 inline formulas also compile with pdflatex (amsmath, amssymb, mathrsfs); every
paragraph has balanced $ delimiters.

**Algorithms:** the PDF has no algorithm box. The two enumerated procedures were checked line by line:
Appendix D (3 lines, p. 23) and Appendix E.1 (3 lines, p. 24); 6 of 6 match.

**Tables:** the PDF has none; assets/table and assets/supp_table are empty. 0 cells.

**Figures: 8 of 8 assets opened.** Each is the complete figure (all panels, axes, legends, colour bar),
not cut, with no foreign text: Figure 1 (p. 1), 2 (four sets, p. 6), 3 (with colour bar and L label,
p. 8), 4 (three panels, p. 8), 5 (two stacked panels, p. 9), 6 (photo, two renderings, force plot,
p. 10), 7 (p. 17), 8 (p. 24). All 8 captions verbatim, label numbers correct, links resolve.

**Completeness and order:** word-level diff of the PDF text layer (all 25 pages) against paper.md with
math removed: every non-matching span is a relocated figure caption or footnote, a small-caps name, a
line-break hyphen, or math tokens. No dropped, duplicated or reordered prose; no sentence cut at a page
break (checked the 11 page breaks that fall inside a sentence, statement or formula: pp. 1-2, 2-3,
3-4, 4-5, 8-9, 9-10 with x_t in R^6, 15-16 inside Theorem 3, 17-18, 19-20, 23-24, 24-25 with X_0). Footnotes 1-8: 8 marks and 8 texts, each once, text verbatim.
References: 50 of 50 entries present once, in printed order, character-identical to the text layer
after removing whitespace, hyphens and markup; italics spot-checked on p. 12.

**Prose spot check:** pp. 1-10 and 15-25 read in full against the renders (not only two paragraphs);
pp. 11, 13, 14 through the text layer only (see below).

**Headings and index:** 29 headings below the title in paper.md, all real, correctly numbered and nested (5.1-5.3,
6.1-6.3, A.1-A.2, B.1-B.3, E.1-E.2). All 29 index rows exist as exact headings and their "look here
for" descriptions are accurate (equation numbers, figure numbers, footnote ranges, "50 entries").
supplement.md says no supplementary material was supplied, which is correct.

**Two questions answered from the package only (SKILL.md -> index -> section):**
1. "How many samples does the paper need in the neural-network example for eps = 0.02 and confidence
   1 - 10^-4, and from which constants?" Index row E.2 -> paper.md "E.2. Verification of neural network
   controllers": L = 1, D(dX, eps/(2L)) <= 2/eps + 1, Lambda_eps^L = eps/2, M >= ... ~ 1376 (the main
   text, Section 6.2, rounds to 1400). PDF p. 25 and p. 9 agree; recomputing gives 1375.6.
2. "What is delta_M in Corollary 1 and what must hold?" Index row 5.2 -> paper.md Corollary 1:
   delta_M = D(dX, eps/(2L))(1 - p_0 Lambda_eps^{r,L})^M with Lambda_eps^{r,L} = lambda(B(0, eps/(2L))
   cap B(r, r)), r = (r,0,...,0) in R^p, under Assumptions 2, 4, 5 and dY subseteq f(dX). PDF p. 7 agrees.

## Conversion notes (end of paper.md)

Every "kept as printed" claim was checked on a 260 dpi render (400 dpi for the first one below) and is
really what the PDF prints. 23 of 23 confirmed:
- p. 17: "Since dY cap (G^1_d + B(0, eps-bar)) != empty for j = 1,2" (superscript 1, not j; 400 dpi);
  "cap_{N=0}^inf A_n subseteq A_0"; "a sufficient conditions".
- p. 18: "Since eps -> eps-bar as M -> inf" (no subscript M). p. 19: "G^1_delta, G^2_delta",
  "{..., m >= 1}", "conludes".
- p. 2 "thrustworthy"; p. 3 "analyis", "guarantees, Our analysis"; p. 5 "Y^M_eps converges" without hat;
  p. 16 Theorem 3 conclusion "{Y^M}" and "d_H(Y^M, Y)" without hats; p. 6 "d-packing number";
  p. 7 "(2d sqrt(n)/eps)^n"; p. 8 "d_H(Yhat^M, Y)" without H and "theorical"; p. 10 "[-0.015, 0.015]"
  without square in X_t(nu); p. 22 "for any x in R^n", "in Theorem 2", second "c_1", mixed p and n in
  V(r,a); p. 24 unbalanced parenthesis in p_0^alpha, "explicitely".
- Also confirmed: d_H with upright H only in (3) and (5); italic H inside italic theorem bodies;
  the offset vector printed bold without arrow; footnote and figure placements as the notes describe
  (Figure 7 is inserted in main.tex between "We will select specific sets ..." and "To prove (C2)").

## Not checked

- pp. 11, 13, 14 were not rendered: acknowledgments and references on those pages were compared through
  the PDF text layer only, so italic emphasis in those reference entries was not verified by eye.
- pp. 1-3 were read on 170 dpi full-page renders, not 250+ dpi crops; they contain no theorem-like
  statement or display (only the Figure 1 caption math and the first line of Section 3).
- Figure assets were checked for completeness and content by eye, not pixel-compared; Figure 6 was
  compared with a 150 dpi crop.
- I did not verify the notes' statements about the reviewer's own process (render resolutions used).
