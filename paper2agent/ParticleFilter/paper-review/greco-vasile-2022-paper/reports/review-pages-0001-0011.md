# Review report: Greco & Vasile 2022, PDF pages 1-11

All 11 pages are `reviewed: true` with `[v2]` notes. No TeX source; all mathematics transcribed from 170-300 dpi crops.
Page 1 is **not** a repository cover sheet (it is the manuscript title page), so nothing was omitted there.

## Per page
| Page | Content | Assets / equations | Check state |
| --- | --- | --- | --- |
| 1 | Title, authors, affiliation, author footnotes, abstract, `## Nomenclature` (12 lines) | - | OK |
| 2 | Nomenclature (36 lines), `## I. Introduction`, first lines | - | (a): 6 nomenclature symbol lines, `-1` subscript |
| 3 | Introduction prose | - | OK |
| 4 | Introduction prose | - | OK |
| 5 | `## II. Robust Filtering`, `### A. Imprecise Formulation` | Eqs. (1), (2), (3) | (a) maths only |
| 6 | II.A | Eqs. (4a), (4b), (4c), (5), (6a), (6b) | (a) maths only |
| 7 | `### B. Expectation Estimator`, `#### 1. Precomputed Sequential Importance Sampling` | Eqs. (7), (8) | (a) maths only |
| 8 | II.B.1 | Eqs. (9), (10), (11a), (11b) | (a) maths only |
| 9 | floats | `algorithm-1`, `figure-1`, `algorithm-2` (image + transcription each for the algorithms) | (a); second parser sees hidden tick text in Fig. 1 |
| 10 | II.B.1 end, `#### 2. Proposal selection` | `figure-2` | (a); second parser sees hidden tick text in Fig. 2 |
| 11 | II.B.2 | Eqs. (12), (13) | (a) maths only |

Adjudication notes written for pages 2 and 5-11 (pages 1, 3, 4 are OK).

## Joins
- Set inside the range: first items of pages 3, 4, 6, 8, 9, 10, 11 have `join_previous: "space"`. Pages 5 and 7 start with a heading / new paragraph (pages 4 and 6 end with complete paragraphs). Page 2 starts with the nomenclature continuation (separate lines, no join).
- Boundary 11 -> 12: page 11 ends with "With this approach, ... epistemic set. Furthermore," and continues on page 12 ("the UKF-based proposal concentrates ..."). Page 12's continuing item already carries `join_previous: "space"` in the other reviewer's file, but it must come directly after page 11's last text item in the final reading order (if page 12 places floats before it, a `reading_order` entry is needed).

## Page 9 float layout (proposal for plan.json)
One paragraph runs from page 8 ("Once this precomputation step is complete, ...") over page 9 to page 10 ("... (Line 3)."); page 9 holds only two lines of it, around Algorithm 1, Fig. 1 and Algorithm 2. No paragraph boundary exists on page 9, so I split the page-9 prose at a sentence boundary: `p0009-r000` ("described in Algorithm 2. Its graphical representation is shown in Fig. 2.", joined to page 8) comes before the floats and `p0009-r007` ("The pSIS is evaluated by computing the new weights ...", continues on page 10) after them. No sentence is interrupted, but the output shows a paragraph break that is not in the source. If the coordinator prefers, a `reading_order` in `plan.json` could move the three floats (ids `p0009-r001` ... `p0009-r006`) after `p0010-r000`, and `p0009-r007` could then get `join_previous: "space"`.

## Formulas kept as images
None. All 17 numbered displays on pages 5-11 are LaTeX with printed tags.

## Things transcribed as printed (possible authors' slips, not corrected)
- Eq. (5): integrand printed as p(x_k | y_{1:k}; lambda) (x_k rather than x_{0:k}); same in the prose above it.
- (4a)-(4c) share one large left brace in the PDF; written as three tagged blocks without the brace.
- Algorithm 2, line 3: "updated weights hat-w_k^{(i)}" while the sum uses hat-w_M^{(i)}.
- Page 10: n_eff = 1/sum w_k^{(i)^2} printed with unnormalised w and "in percentage".
- Page 8: pi(x_0) with non-bold x in one place; "need not to be drawn again".
- Page 4 typos: "quantity of interest, The result", "concluding remarks an future developments".
- Page 2: drop cap "S" + small caps "tandard" written as "Standard".

## Text repairs of substance
- Nomenclature (pages 1-2) was scrambled by the extractor; rebuilt as 48 "symbol = meaning" lines.
- Page 2 intro paragraph existed as two garbled duplicates; retyped.
- Page 4 first line was a false heading; pages 9/10 had false headings ("Given:", "end for") and the Fig. 2 caption as text.
- All extractor `formula` items converted to LaTeX text; inline superscript soup on pages 8-11 retyped.

## Remaining diagnostics
All category (a) (LaTeX versus glyph text, `-1` minus-glyph tokens, algorithm transcriptions duplicating image text). Second-parser-only "missing" numbers on pages 9 and 10 (0.6, -0.8, -5 ... 6, 12345) are hidden/clipped text objects inside the embedded figure graphics; they are not visible on the page.

## Notes on the brief
- The `check` tool prints very long pypdf font warnings on stderr; redirecting stderr is needed to see the result.
- The brief's rule "floats between complete paragraphs" cannot be met on a page that has no paragraph boundary (page 9); see above.
