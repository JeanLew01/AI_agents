# Review report: gning-box-bernoulli-2012, PDF pages 1-8

Paper: Gning, Ristic, Mihaylova, "Bernoulli Particle/Box-Particle Filters for Detection and Tracking in the
Presence of Triple Measurement Uncertainty" (author manuscript, 28 Dec 2011). No TeX source; all mathematics
transcribed from 220-600 dpi crops. Layout: two-column IEEE style.

## State
All eight pages are `reviewed: true` with `[v2]` notes. Adjudication notes written for pages 2-8
(`adjudication-notes/page-0002..0008.json`); page 1 checks `OK`.

**No repository cover sheet**: PDF page 1 is the manuscript's own first page (title, authors, abstract,
Section I), so nothing was omitted except the printed page numbers on each page.

## Per page
| Page | Content | Assets | Equations (printed tags) |
| --- | --- | --- | --- |
| 1 | Title, authors, affiliation footnotes, abstract, index terms, submission note, I. Introduction | - | - |
| 2 | I (end), II, II-A, II-B | - | (1), (2), (3) |
| 3 | II-B (end), III, III-A, start III-B; footnotes 1-3 | - | (4)-(9) |
| 4 | III-B, IV, IV-A; footnote 4 | `figure-1` (Figure 1) | (10)-(16) |
| 5 | IV-A (end), IV-B, Remark, start V | `algorithm-1` (image + transcription) | unnumbered beta_k display, (17), (18) |
| 6 | V, V-A, V-B; footnote 5 | - | (19)-(25) |
| 7 | V-B (end), V-C; footnote 6 | `algorithm-2` (image + transcription) | (26)-(32) |
| 8 | V-C (end), VI | - | (33)-(38) |

Document-wide float numbering seen in the PDF: Figures 1-9, Algorithms 1-3 (Algorithm 3 and Figures 2-9 are in
pages 9-15), no tables. Names used here (`figure-1`, `algorithm-1`, `algorithm-2`) follow printed numbering and
do not clash.

## Joins
- Inside the range: page 2, 3, 4, 5, 6 and 8 first items carry `join_previous: "space"` (page 7 starts a new
  paragraph). Column-break joins set on every page where a paragraph crosses columns.
- Range boundary: page 8 ends with a complete paragraph and page 9 starts with heading "A. Computation of ..."
  -> **no boundary join needed**.
- Page 4 last paragraph ("Each density ... as") continues on page 5 ("follows. Suppose ..."), joined on page 5.
  It follows equation (16) as a new sentence and is deliberately not joined to (16) so that footnote 4 can sit
  before it.

## Formulas kept as images
None. Every displayed formula was legible after zooming and is LaTeX text.

## Text repairs of substance
- Pages 3, 6, 8: extractor order interleaved the columns; rebuilt as left column then right column.
- Page 8: one extractor formula region spanned both columns and contained two equations, (33) and (36); split
  (new id `p0008-b003b`). A merged paragraph was split at the printed paragraph break (new id `p0008-b015b`).
- Pages 5 and 7: algorithm boxes had been shredded into text/heading/formula fragments (fake headings
  "ments", "measurements", "Time Update", "Measurement Update"); replaced by one image item and one
  transcription item each.
- Page 6: a formula region contained a prose sentence plus (24)-(25); now text + two display blocks.
- Extractor equation labels (e.g. "(11)", "(14)", "(24)" on page 3) were wrong throughout; printed tags used.
- Page 1: "Submitted to IEEE Trans. Signal Processing December 28, 2011" demoted from heading to text;
  "Index Terms" is run-in text.

## Authors' oddities kept as printed (also in page notes)
- p1: third affiliation footnote is marked ∗ although the author line marks Mihaylova with ♯.
- p4: integral limits in the first line of the (11)-(13) chain are non-bold; "is the sources of fuzziness".
- p5: (18) and Algorithm 1 step 8 write g(.) without subscript k+1; step 8 uses x^i_{k+1}; w^{i,*} vs w^{i*}.
- p6: (22) writes beta without subscript k; (24)/(25) have the weight w^i outside the sum over i; f_k non-bold
  in the "key issue" sentence.
- p7: Algorithm 2 step 10 cites "(8) and (34)"; step 12 normalises \tilde{w} into itself; step 13 index
  N'(1+m_k).
- p8: normalisation sum runs to N' although there are N' x (m_k+1) weights.
- p5: "Remark:" is printed in regular weight; the bold label was added per the brief's convention.

## Remaining diagnostics (all category (a))
- p1: OK.
- p2, p3, p4: missing lines are maths now in LaTeX; p3 second parser splits "Sec.14.7" into 14 and 7.
- p5, p7: missing lines = LaTeX maths; number extras = the algorithm transcriptions that duplicate the
  image-excluded algorithm text; p5 also the minus glyph of h_k^{-1}.
- p6: missing lines = LaTeX maths; minus glyph of [h_k^{-1}].
- p8: missing lines = LaTeX maths; "m_k+1" vs "$m_k + 1$".

## Proposals for shared files
- plan notes: "Author manuscript (second revision, 28 Dec 2011) of the IEEE TSP 60(5), 2012 paper; equation
  numbering follows the manuscript." No reading_order entry is needed for pages 1-8 (floats were placed between
  complete paragraphs inside each page).

## Limitations
- Bold/non-bold distinctions were read from crops; a few scalar-versus-vector choices (Fig. 1 paragraph and
  caption use non-bold z) follow the print as seen at 230-600 dpi.
- Small subscript sizes such as p_B, p_S, p_D (printed with small-capital subscripts) are written as plain
  subscripts.

## Brief feedback
- The brief asks for footnotes "directly before the last paragraph" when that paragraph continues on the next
  page; when the page ends in a long join chain (text-equation-text-equation, page 7) the footnote ends up
  several items earlier. Worked, but an explicit statement that this is acceptable would help.
- Transcribing algorithms next to their image necessarily produces "extra" number diagnostics; worth stating in
  the brief as an expected category (a).
