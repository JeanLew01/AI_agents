VERDICT: clean

Package: skills/liu2025recurrent-paper (references/paper.md 706 lines, index.md, SKILL.md, 7 JPEG assets, 2 CSV).
Ground truth: papers/liu2025recurrent.pdf (arXiv:2510.02127v1, 8 pages). Verified 2026-10-02.
No A, B or C findings. Every mathematical item was compared against a 260-300 dpi crop (tables at 400 dpi).

## Findings

None.

## Observations (not errors, no fix required)

1. Algorithm 2, line 5 (paper.md "5: ... SafetyCheck(g_i, G, G_u, tau, C_s, C_u)", PDF p.6 left column).
   On the page line 5 starts about 0.4 em right of the "for" keyword of line 3 and about 0.6 em left of
   line 4 (measured on a 300 dpi crop: for at x=207, line 5 at x=232, line 4 at x=270 px). It is printed
   after line 4 and before "6: end for", so it is inside the for body. The transcription puts lines 4 and 5
   at the same level (two levels in), which is the correct nesting. The conversion notes do not mention the
   printed offset; a one-line note would be optional.
   Nesting of the other three algorithms matches the page exactly: Alg. 1 flat (5 lines, comment on line 4);
   Alg. 3 lines 6, 8, 10 one level inside if / else if / else, the rest flat; Alg. 4 flat (4 lines).
2. index.md has no row for the two parent headings "II. Preliminaries and Related Work" and "Appendix".
   Neither has text of its own in the PDF (each is followed directly by its subsection A), and all their
   subsections are indexed, so nothing is unreachable.
3. Conversion notes, first bullet: "the paper appeared at IEEE CDC 2025". The PDF does not state a venue
   (only the arXiv stamp "arXiv:2510.02127v1 [eess.SY] 2 Oct 2025"), so this cannot be confirmed from the
   ground truth. It is metadata, not a "kept as printed" claim.
4. Figure 2 legend colours: at small render sizes the r_min = 0.123 legend line looks grey in a pdftoppm
   render. Pixel sampling at 800 dpi gives blue (0,0,255) for 0.370, deep sky blue (0,191,255) for 0.123,
   cyan (0,255,255) for 0.041, light grey (211,211,211) for HJ Reachability; the asset shows the same.

## Conversion notes ("kept as printed" claims): all confirmed on the page

'parellizable' (abstract); 'intial state' (II-D); e-mail 'jliu376@jh.edu'; (7) has u inside the arg max
while u_0 is selected; Theorem 3 'u in U^{(0,tau]}' without hat while (11) maximises over (0, tau-hat];
proof of Theorem 4 (i) prints 'r e^{-Lt}' and the last display prints italic 'R_{t*}(X_u)';
Theorem 5 (ii) 'assume that forall u ... s.t. the following holds'; (17) and the proof of
Theorem 5 use h(y,u,t); the proof cites 'the conditions of (17)' and 'the conditions of (19)'; Algorithm 1
line 4 passes (17), (20); Section V 'conditions (13) and (17), and (14) and 20' (no parentheses on 20);
TABLE II caption alpha = 1 versus beta = alpha = 0.05 in VI-A; V_BRT italic subscript in VI-A, upright in
VI-B; Appendix: undefined g, F(x,u) - F(x,v) = g(x)(u-v), integrand ||u(s) - u(s)||, calligraphic S in both
arg min, unmatched '|' at the end of the third line of the Case 3 display; Theorem 4 (ii) ends without a
period; 'Theorem 1 ( [2]).' with the printed space; TABLE II Recurrent Set times in bold; Figure 3 at the top
of the right column of p.7 before Section VII. No note describes an error that the PDF prints correctly.

## Coverage

- Theorem-like blocks: 16 of 16 checked symbol by symbol (Assumptions 1-2, Definitions 1-8, Theorems 1-5,
  Lemma 1), including printed number, title, bold terms, quantifiers, interval brackets, hats and bars.
  Theorem 3 at 300 dpi: tau-hat bound = max{log(a2/a1)/(alpha-hat - alpha), log(a2/a1)/(beta - beta-hat)}
  + log(delta-bar/delta-underbar)/min{alpha-hat, beta-hat}; sup / inf over x in D_0 confirmed.
- Proofs: Theorem 2 (i),(ii); Theorem 3 (omitted, reference [10, Theorem 11]); Theorem 4 (i),(ii);
  Theorem 5 (i),(ii) with both arg max pairs and both inequality chains; Appendix A (Gronwall chain,
  Cases 1-3). All lines, relation signs and which u/t carry a star confirmed.
- Displays: 47 of 47 (20 numbered, tags (1)-(20) each on the right equation and present exactly once;
  27 unnumbered). All math blocks are brace-balanced.
- Algorithms: 29 of 29 numbered lines plus 4 title lines against 300 dpi crops; nesting checked for all four.
- Tables: 30 of 30 cells (TABLE I and II, header row included) at 400 dpi, in paper.md and in both CSV
  files: values, 's' units, cross/check marks (HJ BRT: cross, cross, cross, check; Recurrent Set: four
  checks, in both tables), header 'Methods \ r_min' vs 'Method \ r_min'. Both captions verbatim.
- Figures and assets: 7 of 7 (figure-1..3, algorithm-1..4). All four edges compared with the page: nothing
  cut (legend, axis and tick labels, y-labels, sub-captions, top and bottom rules of the algorithm boxes all
  present), no foreign text. Captions of Fig. 1-3 verbatim, numbers correct.
- Completeness and order: word-level diff of pdftotext against the package (all alphabetic words of four or
  more letters, 2753 vs 2778 tokens) shows only float/footnote reordering, small-caps headings and
  line-break hyphens. 473 of 499 prose runs between formulas occur verbatim, punctuation included, in the
  PDF text; the other 26 are heading, float, link or reference-number boundaries, each confirmed by eye.
  Page 6 (four algorithm boxes) and page 7 (two tables, two figures): surrounding paragraphs complete and
  in reading order; the paragraph split across the p.6 column break ("... while ensuring rigorous | safety
  guarantees. ...") is joined correctly. No sentence cut at a page or column break. Both first-page
  footnotes present once. References [1]-[20] all present, checked entry by entry (authors, titles, venues,
  volumes, pages, years, URL of [19], ISBN of [20]).
- Prose spot check: all 8 pages. Page 1 by full token diff including punctuation (no difference); pages
  2-8 read against the crops paragraph by paragraph, inline math included.
- Headings and index: 23 headings (title and 'Conversion notes' included), all real, correctly numbered and nested; 20 index rows each match
  exactly one heading; all 9 asset links resolve; supplement.md correctly says none supplied.
- Two questions answered from the package only (SKILL.md -> index.md -> paper.md), then checked on the PDF:
  Q1 "What horizon does Theorem 3 need for -sd(., S) to be an RCBF?" Index row 'C. Signed Distance
  Function: a Valid RCBF', paper.md lines 253-274: tau-hat >= max{log(a2/a1)/(alpha-hat - alpha),
  log(a2/a1)/(beta - beta-hat)} + log(delta-bar/delta-underbar)/min{alpha-hat, beta-hat}, with
  alpha-hat > alpha, beta-hat < beta and delta-bar / delta-underbar the sup / inf over D_0 of
  sd(x,S) - sd(x,h_{>=0}). Matches PDF p.4 right column (300 dpi).
  Q2 "What does SafetyCheck do with an undecided cell, and how is it split?" Index row 'V. Numerical
  Methods', paper.md lines 482-520: Algorithm 3 lines 9-10 put SplitCell(g_i) back into G; Algorithm 4:
  P = {x + (2r/3) delta : delta in {-1,0,1}^n}, returning the balls B_{r/3}(p), p in P. Matches PDF p.6
  right column (300 dpi).

## Not checked

- The package LaTeX was not compiled (only brace / environment balance was tested).
- Whether the five line-break hyphens kept in the package ('first-order', 'non-control', 'time-dependent',
  'Hamilton-jacobi' in [3], 'input-constrained') are real hyphens cannot be decided from the PDF alone;
  all five are the natural reading.
- Bibliographic correctness of the references against external sources (only fidelity to the PDF).
- The venue statement in the conversion notes (observation 3).

Work directory logs/verify/work/liu2025recurrent was emptied and removed; nothing outside this file was written.
