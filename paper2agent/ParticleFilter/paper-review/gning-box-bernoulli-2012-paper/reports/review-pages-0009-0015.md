# Review report: Gning, Ristic, Mihaylova (2012), PDF pages 9-15

Document: `documents/s001-gning-box-bernoulli-2012`. No TeX source; all mathematics transcribed from crops (200-560 dpi).
Layout: two columns (IEEE draft style; pages 13-15 partly double-spaced). All seven pages are `reviewed: true` with `[v2]` notes.

## Per page

| Page | Content | Assets / equations | State |
| --- | --- | --- | --- |
| 9 | VI-A, VI-B, VII intro, VII-A | Eqs (39)-(47) as LaTeX text | done; diagnostics category (a) |
| 10 | VII-A (cont.), VII-B, start VII-C | Eq (48); `figure-2` (panels a, b) | done; (a) |
| 11 | VII-C 1), start of 2) | `figure-3` (a, b), `figure-4` | done; (a) |
| 12 | VII-C 2), VIII, APPENDIX a) | `figure-5`, `figure-6` | done; (a) |
| 13 | Appendix eqs, b), Acknowledgements, REFERENCES [1] | Eqs (49), (50), (51); `figure-7`, `figure-8`, `figure-9` | done; (a) |
| 14 | Algorithm 3, refs [2]-[25] | `algorithm-3` (image + line-by-line transcription) | done; (a) |
| 15 | refs [25] cont.-[30] | none | done; check OK |

No tables, no footnotes, no author biographies in this range. No formula kept as image (every symbol was legible after zooming).

## Joins
- Range start: page 9 begins with a subsection heading (page 8 ends with a complete paragraph "... Monte Carlo runs."): no join needed at the 8/9 boundary.
- Page breaks inside my range: p0011-b003 (space), p0012-b004 (space), p0015-b001 (none; after the compound hyphen of "multi-target" in ref [25]).
- Column breaks: p0010-b013, p0011-b008, p0012-b008, p0015-b005 (ref [28]), all space.
- Page 12 ends with "are [10, p.520]:" and page 13 starts with display equations (49), (50) (no join field needed: display items).

## Reading-order decisions
- Floats were moved so that they do not interrupt sentences: Fig. 2 between the two paragraphs of VII-B; Figs 3, 4 after the first (continued) sentence of page 11; Figs 5, 6 after the first (continued) sentence of page 12; Figs 7-9 after appendix paragraph b) and before the Acknowledgements.
- Equations (49)-(50) are printed at the bottom-left of page 13 but logically follow page 12's last line; they are the first items of page 13.
- Algorithm 3 is printed at the top of page 14, i.e. after "REFERENCES [1]" in page order. It is the first item of page 14 (between complete entries [1] and [2]). Proposal for the coordinator: a `reading_order` in `plan.json` could move `p0014-b001` and `p0014-b001t` to directly after `p0013-b009` (appendix paragraph b), before the figures/Acknowledgements) so that the bibliography is contiguous.

## Text repairs of substance
- Extractor merged Figs 3+4 and Figs 5+6 into single pictures and dropped the Fig. 4 caption: split and restored.
- Heading `# REFERENCES (49)` repaired (tag belongs to the equation). Subsection headings set to `###`, sections to `##`.
- Compound hyphens restored: range-rate, Box-PF, multi-Bernoulli, set-theoretic ([7]); "Mušicki" ([19]).
- Reference order on page 15 fixed ([28] was last and split from "Chapman and Hall, 1986.").

## Authors' peculiarities kept as printed (recorded in review_notes)
- (41) uses non-bold $P_{k|k}$; "The sensors provides"; "an a function" (captions of Figs 8, 9); "twice less", "almost hundred time smaller"; "set-theoric" in the Fig. 3 legend.
- (50): the summation index in the numerator is set on the baseline, and the numerator has no integral.
- Algorithm 3: lines 5/6 first denominators lack a square on the last term; unbracketed y^2, x^2; azimuth interval called [β] (θ elsewhere); trailing comma in line 13.

## Remaining diagnostics (all category (a); adjudication notes written for pages 9-14)
- Pages 9-13: missing lines are lines with LaTeX maths / caption maths; number differences are minus-glyph vs ASCII '-' inside LaTeX and second-parser decimal splitting.
- Page 14: one line (caron in "Mušicki"); "extra" numbers are the Algorithm 3 transcription (the native lines lie inside the image bbox).
- Page 15: OK.

## Notes on the brief
- The `check`/`crop` tools print long fontTools warnings on stderr; `2>/dev/null` is needed to keep output readable.
- The brief's caption example ("Fig. 3: ...") differs from this paper's printed style ("Figure 3. ..."); printed style kept.

## Limitations
- Fine structure inside plots (legend entries, tick labels) is preserved only in the images.
- Pages 1-8 were not touched; asset names there (figure-1, algorithm-1, algorithm-2, formula-p0008-*) do not clash with mine.
