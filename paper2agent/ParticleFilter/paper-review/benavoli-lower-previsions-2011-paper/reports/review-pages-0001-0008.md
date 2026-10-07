# Review report: Benavoli, Zaffalon, Miranda, "Robust filtering through coherent lower previsions" — PDF pages 1-8

Document: `documents/s001-benavoli-lower-previsions-2011`. No TeX source; all mathematics transcribed from crops
(200 dpi half-columns for pages 3-6, 300 dpi quarter-columns for pages 7-8, 300-350 dpi zooms for small indices).
All eight pages are `reviewed: true` with `[v2]` notes. No page was left unfinished.

## Per page

| Page | Content | Numbered equations (all as LaTeX text with `\tag`) | Check result |
| --- | --- | --- | --- |
| 1 | Title, authors, address footnote, abstract, index terms, I. Introduction | none | 1 missing line (inline maths, cat. a) |
| 2 | Introduction (cont.) | none | OK |
| 3 | Introduction (end), II. Bayesian filtering, III. Coherent lower previsions | (1)-(4) + unnumbered Markov display | 13 lines + minus-glyph numbers (cat. a) |
| 4 | III (cont.), A. Main definitions and results; Definitions 1-3, Theorem 1 (SC1)-(SC3); footnotes 1-4 | (5) + unnumbered sum | 45 lines (cat. a) |
| 5 | Remark 1, Examples 1-2 | none numbered; 4 unnumbered displays | 64 lines (cat. a) |
| 6 | Definition 4 (GBR), Example 3, Definition 5 (marginal extension), Definition 6 (epistemic irrelevance), IV. heading; footnote 5 | (6)-(9) + 2 unnumbered | 65 lines + minus-glyph numbers (cat. a) |
| 7 | Lemma 1 and proof, Theorem 2; footnote 6 | (10)-(16) + 2 unnumbered | 80 lines + minus-glyph numbers (cat. a) |
| 8 | Proof of Theorem 2, Corollary 1 and proof | (17)-(24) + 1 unnumbered | 89 lines + minus-glyph numbers (cat. a) |

Figures / tables / algorithms on pages 1-8: none (Fig. 1-4 are on the other reviewer's pages; no asset names used here).
Formulas kept as images: none. Every display was legible after zooming.
Adjudication notes written for pages 1, 3, 4, 5, 6, 7, 8 (page 2 is OK).

## Bars (lower/upper previsions)
Every underline/overline was checked on the crops. Points worth knowing:
- Definition 2 and the paragraphs after it use plain `E_{Z_O}` (linear previsions); Definition 3, (5), Theorem 1 use `\underline{E}_{Z_O}`; inside (5) only the argument of `\mathcal{M}` is barred.
- Pages 7-8: all E carry an underline except `\overline{E}_{\tilde{Y}_k}` in the second line of (16), (18), (19), the third line of (17) and of the unnumbered display on page 8, and Corollary 1's lower = upper = linear chains. (20)-(24) contain only unbarred E.

## Printed peculiarities kept verbatim (not corrected)
- p3: KF update printed with `A_t \hat{x}_{t-1}` although model (4) reads `x_{t+1} = A_t x_t + w_t`.
- p4: "power set of $Z_O$" with italic Z (elsewhere calligraphic).
- p5: Example 1 writes the unconditional vacuous prevision as `\underline{E}_{Z_O}(f|z_U)`; Example 2 mixes `\mathcal{K}_O(z_U)` and `\mathcal{K}_O^{z_U}`.
- p6: Definition 4 "let `\underline{E}_{Z_{O\cup U}}(\cdot|Z_U)`"; Example 3 "`E_{Z_{O\cup I}} \in \mathcal{M}(...)`" (subscript I); "and it is CLP." after (8).
- p7: (13) has a stray comma in "`|X_t,]`"; left side of (13) uses `y^t`, `Y^t` without tildes; the unnumbered display after "can be written as" has unbalanced brackets as printed; Theorem 2 writes `\underline{E}_{X_t}[g|y^t]`.
- p8: `\underline{E}_{x_0}[g_0]` with lowercase x_0 (twice); (21) conditions the second term on lowercase `x_k`; (24) uses `g_t` in line 3 and `g` in line 5.

## Structure decisions
- Theorem-like labels (Definition 1-6, Theorem 1-2, Remark 1, Example 1-3, Lemma 1, Corollary 1, Proof) are bold; the paper prints them in italics. Statement bodies are printed in italics with defined terms upright; here bodies are plain and the defined terms are emphasised. End-of-block squares kept as `$\blacksquare$`.
- Headings: `# ` title; `## II. BAYESIAN FILTERING`, `## III. COHERENT LOWER PREVISIONS`, `## IV. GENERALISATION OF BAYESIAN STATE ESTIMATION` (extractor had `# ` or plain text); `### A. Main definitions and results`.
- Footnotes: authors' addresses after the author line (p1); footnotes 1-4 at end of p4; footnote 5 directly before the last (continuing) paragraph of p6; footnote 6 at end of p7. Markers written `[^n]`.
- Display equations are separate blocks without `join_previous` (as in the sibling collections); `join_previous: space` only for prose split by a column or page break.
- Extractor items removed after merging: p0003-b014 (tag of (3)), p0004-b010 (second bullet, now in the list item), p0008-b005 and p0008-b010 (tags of (17) and (22)). New items use ids `pNNNN-rKKK`.
- Multi-line displays with printed open bracket chains ((13), the display after "can be written as") use fixed-size `\Big` delimiters so the LaTeX is valid without changing the printed bracket count.

## Joins
- Set inside my range: p1 b010; p2 b001 (from p1), b005; p3 b001 (from p2), b012; p4 b001 (from p3); p5 b009; p6 b011; p7 b002 (from p6), b001; p8 r001.
- **Needed at the boundary with page 9 (other reviewer):** the first content item of page 9 ("converges to 0 for k = 1, ..., t, we obtain Bayes' rule ...") continues the last paragraph of page 8 ("... of the neighborhoods $\tilde{y}_k = B(y_k, \delta(y_k))$") and needs `join_previous: "space"`.
- Page 5 starts and page 4 ends with complete paragraphs (no join). Page 8 starts with a new block (Proof).

## Remaining diagnostics
All remaining `missing line` entries were filtered for lines without mathematical symbols: none. They are category (a): LaTeX versus glyph text, or fragments the PDF splits at barred E symbols and tall delimiters. Number differences are exclusively U+2212 `−1`/`−2` versus ASCII `-1`/`-2` in LaTeX sub/superscripts (p7 second parser: one extra `1` from token gluing).

## Proposals for shared files
- plan notes: mention that theorem-like statements are printed in italics and are given in upright text with bold labels, and that the source is the authors' manuscript dated 28 Oct 2010 (two-column IEEE style).
- No asset-name clashes (no assets on pages 1-8).

## Limitations / brief feedback
- LaTeX could not be rendered locally; delimiter/brace/`$` balance was checked by script only.
- The first content item of pages 2, 3, 4, 7 follows the page-number `omit` item while carrying a cross-page join; this assumes the builder skips omitted items when joining (as the brief's cross-page instruction implies).
- The brief does not say whether display equations inside a sentence should carry `join_previous`; I followed the majority practice of the sibling collections (no join).
