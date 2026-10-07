# Review report: Haj Chhadé et al. 2014 (box particle messages), PDF pages 9-16

All eight pages are `reviewed: true` with `[v2]` notes; adjudication notes written for pages 9-16.
No TeX source: all mathematics was transcribed from the previews and 200-dpi crops. No formula was kept as an image.
Rebuild script (for reference only): `_scratch/haj-chhade-9-16/build.py`.

## Per page
| Page | Content | Assets | Numbered equations |
| --- | --- | --- | --- |
| 9 | Fig. 5; `## 5 Belief Propagation Combined with Interval Analysis`; `### 5.1 Interval Analysis` | figure-5 | (5.1)-(5.3) |
| 10 | interval arithmetic, inclusion functions, CSP; Fig. 6 | figure-6 | (5.4)-(5.7), 2 unnumbered displays |
| 11 | CSP/contraction; `### 5.2 The Box Particle Filter`; Fig. 7 | figure-7 | (5.8)-(5.10) |
| 12 | Box-PF bullets; `### 5.3 Belief Propagation in the Bounded Error Context` | none | 5 unnumbered displays |
| 13 | messages product derivation | none | (5.11)-(5.13), 3 unnumbered displays |
| 14 | Algorithm 1, partial belief, Algorithm 2 | algorithm-1, algorithm-2 (image + transcription) | (5.14) |
| 15 | convolution step | none | (5.15)-(5.17), 1 unnumbered display |
| 16 | Algorithm 3, notes, `## 6 Self Localization in Sensor Networks: Problem Formulation` | algorithm-3 (image + transcription) | (6.1) |

## Joins
- Set: p0013-b002 (`space`, continues page 12), p0014-b002 (`space`, continues page 13).
- Page 9 first item: none needed (page 8 ends with a complete paragraph; page 9 starts with Fig. 5).
- Page 16 ends with "According to the assumption above:"; page 17 continues with Fig. 8 and then a display equation.
  The page-17 reviewer should place Fig. 8 + caption so that it does not sit between this sentence and its equation
  (Fig. 8 is referenced on page 16, so putting the equation first on page 17 and the figure after it reads best). No join_previous is possible onto a display.

## Text repairs of substance
- Running headers on every page changed to `omit`.
- Glued words repaired on pages 11, 12, 14, 15; scrambled sub/superscripts everywhere; replacement/control characters for Gamma and the integral sign.
- Items mis-tagged as headings ((5.3), (5.9), "input:", Algorithm 3 title, "Notes About the Algorithm") corrected.
- Italic run-in titles in 5.1 ("Operations on Intervals and Boxes.", "Inclusion Functions.", "Constraints Satisfaction Problem and Contraction.") are printed on their own lines; kept in italics at the start of their paragraphs, not as headings. "Notes About the Algorithm" (page 16) kept as an italic text line.
- Algorithm labels are italic in print ("Algorithm 1."), bold in the transcriptions per the brief.

## Printed peculiarities kept as printed (recorded in review_notes)
- p11: "f_j, j in {1,...,n}" although f has m components; (5.10) uses non-bold symbols.
- p12: box likelihood has subscript k while the boxes in the ratio have k+1.
- p13: index vector "(p_0, p_1, ..., p_d)"; RHS of (5.12)/(5.13) without argument (x_t).
- p14: Algorithm 2 uses w for the weights (text uses omega); "k = 1, ... Z".
- p15: sums in (5.15) run to V (Z in (5.14)); (5.16) omits [e]; f(x_t, e, v_f) versus f(x_t, v, e).

## Remaining diagnostics (all category (a))
- Missing lines on every page: lines with inline/display maths now in LaTeX (see adjudication notes).
- Number differences p11, p13, p15: ASCII minus versus U+2212 in k-1 / i-1 sub/superscripts.
- Number differences p14, p16: extra numbers from the algorithm transcriptions, whose printed text lies inside the image crops.

## Proposals / limitations
- Navigation: section headings in this range are `## 5 ...`, `### 5.1`, `### 5.2`, `### 5.3`, `## 6 ...`; other ranges should use the same levels.
- Algorithm transcriptions use nested Markdown list lines with indentation; the loop lines of Algorithm 1 step 3 are continuation lines (may reflow into one paragraph in a strict Markdown renderer; the image crop precedes each transcription).
- Brief: fine. The `check` tool prints many pypdf "fontTools is required" warnings for this PDF (filter with grep).
