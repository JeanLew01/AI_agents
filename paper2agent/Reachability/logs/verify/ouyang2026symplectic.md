VERDICT: 1 findings (0 A, 0 B, 1 C)

Package: skills/ouyang2026symplectic-paper (paper.md 662 lines, index.md, SKILL.md, 4 image assets). Ground truth: papers/ouyang2026symplectic.pdf (arXiv:2604.17213v1, 10 pages). Every page was read next to paper.md on column crops at 260-280 dpi, with 500 dpi crops for the densest formulas. No mathematical, factual, numbering, ordering, caption or figure-crop error was found.

## Findings

### C1 (cosmetic, optional) - statement extent is not recoverable for two blocks
- Location: "### C. Recurrence on Energy Layers", paragraph "Hence, for $\mu_\alpha^E$-almost every initial condition in $K_\alpha^E$, the zero-input trajectory visits every neighborhood ..." (PDF p.3, left column); and "### A. Hamiltonian System", paragraph "$\Sigma_E$ is called an invariant energy layer because, under the zero-input, ..." (PDF p.2, right column).
- Package: both sentences are plain paragraphs that follow the display of the block before them (Proposition 1, Definition 2), with nothing to show whether they belong to the statement.
- PDF: the "Hence, ... infinitely often." sentence is printed in italics, i.e. it is the last sentence of Proposition 1. The "Σ_E is called an invariant energy layer ..." sentence is printed upright, i.e. it is outside Definition 2. The two cases look identical in the package.
- Why only C: no text is wrong or missing, and the conversion notes already say italics are not reproduced. The notes spell out the extent of Theorems 2-4 only; one more sentence there for Proposition 1 (ends with "infinitely often.") and Definition 2 (ends with its display) would close the gap.
- Confirmed on 260 dpi crops of p.2 right column and p.3 left column.

No A or B findings.

A candidate that I withdrew: Definition 1 ends "defined on a compact U." with U as plain text in the package. At 500 dpi the PDF prints this U in the text-italic font of the statement body, not in the math font used for U in "u ∈ U ⊂ R^m" on the line above, so the package is faithful.

## Coverage

- Theorem-like blocks checked symbol by symbol: 29 of 29 - Definitions 1-8, Assumptions 1-8, Remarks 1-6, Problem 1, Proposition 1, Lemma 1, Theorems 1-4 (printed number, title, quantifiers, inequality directions, sub/superscripts, underlines, star vs asterisk, calligraphic vs italic). All four proofs (Theorem 2 Steps 1-3 and Conclusion, Lemma 1, Theorem 3 Steps 1-6, Theorem 4) read in full.
- Display blocks: 85 of 85 compared with the page, in order; my own count of displays on the PDF pages is also 85 (p.2: 5, p.3: 8, p.4: 16, p.5: 14, p.6: 13, p.7: 16, p.8: 11, p.9: 2, counting the split lines as the package does). No line lost.
- Printed tags (1)-(14): each on the right line. (5) and (6) are separate lines of one display; (8) is on the second line of its two-line display; (10) on the middle line of its three-line display; (11) on the second line of its two-line display; (12), (13), (14) on the three successive lines of the chain in the proof of Theorem 4. The untagged displays (three conditions of Theorem 2, r_i and the N bound of Theorem 3, the T_max bound of Theorem 4) are untagged in the PDF.
- Algorithm 1: 20 of 20 lines (numbering, nesting depth, conditions, assignments) against a 280 dpi crop. Nesting: lines 5-6 and 19 one level, 7-9, 11-15, 17-18 two levels, 10 and 16 three levels - as printed.
- Tables: none in the paper; 0 cells.
- Figures and assets: 4 of 4 opened and compared on all four edges with the page - figure-1.jpg (543x253), figure-2.jpg (655x383), figure-3.jpg (660x383), algorithm-1.jpg (626x658). Each is complete: all panels, axis labels, tick labels, legends, the printed sub-captions (a)/(b) for Figures 2-3, top and bottom rules of the algorithm; no foreign text, nothing cut. Captions verbatim ("Fig. 1: Assignment set construction.", "Fig. 2: Spring-mass system results.", "Fig. 3: Single pendulum results.").
- Pages 3, 7 and 10 (interleaved columns in the extraction): paragraphs complete and in reading order. p.3: Theorem 1 -> supports K_alpha^E -> Proposition 1 -> II-D -> Definitions 5-6 -> selection rule -> Definition 7 -> Remark 2 -> Section III opener. p.7: Step 3 displays -> (10) -> (11) -> Step 4 -> Steps 5-6 -> III-C -> Assumption 8 -> Theorem 4 -> start of its proof. p.10: references [1]-[29] in order.
- Prose spot check: pages 1-9, at least two full paragraphs each read word for word on the crops, with their inline math; page 10 is the reference list only, all 29 entries read.
- References: 29 of 29; additionally the reference text is character-identical to the PDF text layer (only composed vs decomposed umlauts differ).
- Completeness, checked mechanically as well as by eye:
  - word-sequence diff of the PDF text layer against paper.md shows only moved blocks (footnotes, column order, Figure 1 and Algorithm 1 placement) and math tokens; no dropped or duplicated passage;
  - 479 of 491 prose fragments between formulas occur character for character in the PDF text; the other 12 straddle a column break, footnote or float and were confirmed on the crops;
  - all 85 displays and 401 inline formulas of paper.md compile with pdflatex (amsmath, amssymb); the glyph string of 379 of 401 inline formulas and 50 of 85 displays is found verbatim in the PDF text layer, the rest differ only in extraction order of fractions, limits and matrices and were confirmed on the crops;
  - hyphenated compounds agree per occurrence once line-break hyphens are accounted for.
- No sentence is cut at a page or column break (checked the breaks p.1/2 "such | as energy variation", p.2/3 "The next | theorem", p.3 columns "is its | effective radius", p.4 columns "first | hitting time", p.5 columns "evo|lution", p.6/7 "it follows | that", p.7/8 (falls between two paragraphs of the proof of Theorem 4), p.8 columns around Figure 1 "Its | certified radius is", p.8/9 "trained | with Adam").
- Headings: 17 section headings (Abstract through References), all real, correctly numbered and nested (I-V; II A-D; III A-D; IV 1)-2) printed as run-in italic headings, as the notes say). index.md: every listed heading exists in paper.md and holds what the index says.
- Conversion notes: every "kept as printed" claim was checked on the page and is what the PDF prints - "Assumptions 4-Assumption 7"; the doubled "choose an optimal control" clause; x_i in the first inline fraction of Step 2 and T_epsilon(x)^star in its display (500 dpi); underline under v only in Step 1 and in the last line of the Step 6 display, under v and its subscript elsewhere (500 dpi on Step 1, Step 2, (8), Theorem 3, Step 6); italic B_r(x) under the max signs of (10) and the asterisk on H_+ in the next sentence (500 dpi); undefined eta in Step 6; calligraphic R in Definition 6; two empty-set glyphs; ceiling in N_* vs floors in the proof of Theorem 4; "i=0,...N" vs "i=0,...,N"; tau_j vs T_j; undefined S_tgt^delta; no final periods in Assumption 8; "jliu376@jh.edu"; "a novel class control policies", "maximized (4)", "we can chose", "Fig 1", "Fig 3a"; thin-space page numbers in [6], [21], [28]. The tag-placement and float-placement statements are also correct. No note describes an error that the PDF does not print.

## Two questions answered from the package only

1. "What certified radius and what bound on the number of triples does Theorem 3 give?" Route: SKILL.md -> index.md row "B. Existence of the Chain Policy" -> Theorem 3. Answer: r_i = (v_eps(x_i) - v_0) T*_eps(x_i) / (L_H (1 + e^{L T*_eps(x_i)})) > 0 with v_0 in (0, underline v_eps), and N <= (H_2 - H_1) * 16 L_H^2 / (mu_H (1 - v_0/underline v_eps)^2) * exp(2L(L_H D_X + eps)/underline v_eps) / eps^2, where H(Supp(K)) = [H_1, H_2]. Matches PDF p.6 left column (500 dpi crop).
2. "What success rates does vanilla BC reach on the single pendulum for M = 1..5, against the chain policy, and what is the simulation horizon?" Route: index.md rows "IV. Numerical Simulation" and "2) Single Pendulum". Answer: BC 0.008, 0.53, 0.418, 0.65, 0.744; chain policy 0.348 (M=1), 0.678 (M=2), 1.0 for M>=3; average reach time 114.71 s at M=1 to 13.16 s at M=5; horizon 150 s, unsuccessful runs counted at the horizon. Matches PDF p.9.

## Not checked

- Bar heights and error bars of Figures 2-3 are not transcribed in the package, so there was nothing to compare beyond the image crops and the numbers quoted in the text.
- Italic/bold emphasis was compared only where the package reproduces it (run-in labels, bold condition names, the two bold-italic defined terms, the italic phrase in the Introduction, italic titles in the references); statement bodies are not italic in the package by design.
- The authors' TeX source was used once, to locate the "compact U" wording; it was not used as evidence.
- Hyperlink targets inside the PDF and the dpi figures quoted in the conversion notes.

Renders and temporary files were deleted; the work folder logs/verify/work/ouyang2026symplectic is removed. Nothing outside this findings file was written.
