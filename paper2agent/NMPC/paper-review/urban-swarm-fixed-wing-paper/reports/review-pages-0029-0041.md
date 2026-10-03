# Review report: "Agile Fixed-Wing UAVs for Urban Swarm Operations", PDF pages 29-41

Reviewer range: `pages/page-0029.json` ... `page-0041.json` (brief version 2, no TeX source available).
Document: `documents/s001-urban-swarm-fixed-wing`. Mathematics transcribed from high-resolution crops.

## Per-page log

### Page 29 (printed 753) - reviewed [v2]
- Starts with the paragraph continuing from page 28 (`join_previous: space`), then Figure 28, then the sections.
- Headings: `### 8.4. Swarm System Integration`, `### 8.5. Swarm System Integration Experiments`.
- Figure 28 -> `figure-28` (single crop, bbox checked against ink bounds), caption item follows.
- Omitted: running header (b000), footer (b008). Both extractor warnings resolved.
- No mathematics. Last paragraph continues on page 30.
- Check: OK (30/30 lines, no number differences). No adjudication note needed.

### Page 30 (printed 754) - reviewed [v2]
- Starts with the paragraph continuing from page 29 (`join_previous: space`), then Figure 29, then prose.
- Heading: `### 8.6. Future Steps for Swarm System Integration`.
- Figure 29 -> `figure-29` (single crop). The "Y (m)" axis label is clipped in the source PDF itself.
- Inline maths: `$\approx 5$ m`, `RT-RRT$^*$` (three times).
- Omitted: running header (b000), footer (b007). Both extractor warnings resolved.
- Authors' wording kept: "We were also able track our vehicle", "Not only does the tree rewiring ... lends itself".
- Last paragraph continues on page 31.
- Check: OK (34/34 lines). No adjudication note needed.
- (after adding LaTeX) Check: 1 missing line, category (a) (`≈5` written as `$\approx 5$`). Note written.

### Page 31 (printed 755) - reviewed [v2]
- Figure 30 -> `figure-30` (panels (a), (b), (c) in one crop), Figure 31 -> `figure-31` (two panels); captions follow.
  The "X (m)" label of Figure 30(c) is clipped in the source image itself.
- The only prose on the page is one paragraph that continues from page 30 and onto page 32. It is split at a
  sentence boundary: `p0031-b008` ("also apply ... radius of the flight path.", `join_previous: space`) opens the
  page, then both figures with captions, then new item `p0031-b008b` ("Initially, we did not believe ... For
  handling") closes the page. No sentence is interrupted, wording unchanged.
- Inline maths: `RT-RRT$^*$`, `($> 100$ m)`, `(max $60^\circ$)`.
- Omitted: running header (b000), footer (b009). Both extractor warnings resolved.
- Check: 2 missing lines, both category (a) (degree sign in LaTeX; the line that spans the split). Note written.

### Page 32 (printed 756) - reviewed [v2]
- Starts with the end of the paragraph from page 31 (`join_previous: space` added), then Figure 32, Figure 33,
  then `## 9. Discussion` and its first paragraph (continues on page 33).
- Figure 32 -> `figure-32` (panels (a), (b), (c) in one crop), Figure 33 -> `figure-33` (two photographs).
- Omitted: running header (b000, extractor warning) and footer (b011).
- No mathematics. Check: OK (12/12 lines). No adjudication note needed.

### Page 33 (printed 757) - reviewed [v2]
- Starts with the paragraph continuing from page 32 (`join_previous: space`), then Figure 34, then five paragraphs.
- Figure 34 -> `figure-34` (I3 view and STOMP GUI screenshot in one crop), caption follows.
- Omitted: running header (b000), footer (b010). Both extractor warnings resolved.
- No mathematics. Authors' wording kept: "does not have enough time plan a new path".
- Last paragraph continues on page 34.
- Check: OK (42/42 lines). No adjudication note needed.

### Page 34 (printed 758) - reviewed [v2]
- Starts with the paragraph continuing from page 33 (`join_previous: space`).
- Headings: `## Acknowledgments`, `## Appendices`, `### A. Analysis of Post-Stall Turns`.
- Display equations (27), (28), (29), (30), (31): all converted to `$$` blocks with `\tag{..}` (no image kept;
  every symbol legible at 280 dpi). (28) is three side-by-side equalities under one tag.
- Inline maths rewritten in LaTeX (extractor had `<sub>`/`<sup>` and emphasis markers).
- Omitted: running header (b000, extractor warning) and footer (b017).
- Authors' typo kept: "flat plat theory". Page ends with equation (31); the sentence continues on page 35.
- Check: 17 missing lines, all category (a) (display-equation fragments and inline symbols); no number
  differences. Note written.

### Page 35 (printed 759) - reviewed [v2]
- First item continues the sentence after equation (31) on page 34 (no join: it follows a `$$` block).
- Heading: `### B. Energy Analysis`.
- Display equations (32), (33), (34), (35), (36): all converted to `$$` blocks (no image kept). (32) is a two-line
  aligned block with one tag; (35) and (36) are one `$$` block per printed number inside one item.
- Printed as is: (32) minimises over a bold capital Theta and uses `c(theta, v_theta, r, f_t)` while (27) has
  `c(theta, v, r, f_t)`; in (33) the term under the root is `V_perp^infty / 4` (no square).
- Inline maths rewritten in LaTeX. Authors' wording kept: "We would like determine", "The solid red region are".
- Omitted: running header (b000, extractor warning) and footer (b017).
- Page ends with equation (36); the sentence continues on page 36.
- Check: 15 missing lines, all category (a); no number differences. Note written.

### Page 36 (printed 760) - reviewed [v2]
- Untouched by the interrupted run; header (b000, extractor warning) and footer (b012) now omitted.
- First item continues the sentence after equation (36) on page 35 (no join: it follows a `$$` block).
- Display equations (37), (38), (39), (40): all converted to `$$` blocks (no image kept).
- Inline maths rewritten in LaTeX; repaired split decimal `0 . 5`.
- Table 1 -> `table-1`, captured as cells (9 x 5). Pair labels (a)-(d) span two printed rows each and are repeated
  on both rows; the first header cell is blank in print; "m^2" stands for the printed superscript. The extractor's
  labels ("b", "()", "d") were wrong and are fixed. Caption item precedes the table as printed.
- Check: 11 missing lines, all category (a); no number differences. Note written.

### Page 37 (printed 761) - reviewed [v2]
- Untouched by the interrupted run; header (b000) and footer (b010) now omitted (both extractor warnings).
- Figure 35 -> `figure-35` (was `figure-p0037-001`); bbox tightened to exclude the running header; caption
  maths in LaTeX (`$E_r$`, `$R_{\text{max}}$`, `$10\frac{\pi}{2}R_{\text{max}}$`).
- Headings: `## ORCID`, `## References`. ORCID block: six lines, one author per line.
- References: 4 entries (Altug 2002 ... Bachrach 2011), one item per entry, printed author-year style.
- Check: 3 missing lines, all category (a) (caption maths). Note written.

### Page 38 (printed 762) - reviewed [v2]
- References, 24 entries (Bangura and Mahony 2017 ... Garimella et al. 2018), rebuilt as one item per entry
  (`p0038-ref01` ... `p0038-ref24`); the extractor had merged several entries per item.
- Omitted: running header (b000) and footer (b015) (they were still text items; no extractor warning listed).
- Line-wrap repairs: `36(4):710–733.`, `24(4):17–26.`, "takeoff trajectory" (space lost after a ligature in the
  PDF text layer).
- Check: OK (74/74 lines). No adjudication note needed.

### Page 39 (printed 763) - reviewed [v2]
- References, 26 entries (Gill et al. 2005 ... Mathisen et al. 2020), one item per entry
  (`p0039-ref01` ... `p0039-ref26`); the extractor had merged some entries and split others at line ends.
- Omitted: running header (b000), footer (b023). Both extractor warnings resolved.
- Authors' wording kept: "An survey and prototypes overview".
- Check: OK. No adjudication note needed.

### Page 40 (printed 764) - reviewed [v2]
- References, 25 entries (Mathisen et al. 2021 ... Shen et al. 2011), one item per entry
  (`p0040-ref01` ... `p0040-ref25`).
- Omitted: running header (b000, extractor warning) and footer (b025).
- Line-wrap repairs: "computationally" (hyphen removed), URL `https://www.google.com/search?q=binvox` joined,
  "takeoff and landing", "take-off and landing" (space lost after a ligature in the PDF text layer).
- Literal asterisk in "Rt-rrt\* a real-time ..." escaped.
- Check: OK (76/76 lines). No adjudication note needed.

### Page 41 (printed 765) - reviewed [v2]
- References, 15 entries (Singh et al. 2019 ... Zhou et al. 2021), one item per entry
  (`p0041-ref01` ... `p0041-ref15`). The extractor had duplicated "Tabib, W. and Michael, N. (2021)." in two
  items, split Team (2022b) over two items, merged Yang 2008/2010 and lost the hyphen in "rapidly-exploring".
- "How to cite this article" box (b017) and "Publisher's Note" box (b018) kept as text with bold run-in labels.
- Omitted: running header (b000), footer (b019). Both extractor warnings resolved.
- Check: OK (49/49 lines). No adjudication note needed.

## Summary

### Final state
All 13 pages (29-41) are `reviewed: true` with `review_notes` starting `[v2]`. Every extractor warning on these
pages (running headers and footers) is resolved by an `omit` item with a reason; pages 32, 34, 35, 36, 38 and 40
had a footer (and 36/38 a header) that the extractor had not flagged, also omitted.

### Assets
| Page | Asset | Label | Notes |
| --- | --- | --- | --- |
| 29 | `figure-28` | Figure 28 | block diagram, single crop |
| 30 | `figure-29` | Figure 29 | "Y (m)" axis label clipped in the source image |
| 31 | `figure-30` | Figure 30 | panels (a)-(c); "X (m)" of panel (c) clipped in the source image |
| 31 | `figure-31` | Figure 31 | two panels |
| 32 | `figure-32` | Figure 32 | panels (a)-(c) |
| 32 | `figure-33` | Figure 33 | two photographs |
| 33 | `figure-34` | Figure 34 | I3 view and STOMP GUI screenshot |
| 36 | `table-1` | Table 1 | 9 x 5 cells; pair labels repeated for merged cells |
| 37 | `figure-35` | Figure 35 | renamed from `figure-p0037-001`, bbox tightened |

No unnumbered assets were needed, so no page-numbered asset names are used.

### Equations (all as LaTeX `$$` blocks, none kept as an image)
(27)-(31) on page 34, (32)-(36) on page 35, (37)-(40) on page 36. There is no TeX source; every equation was read
from 250-600 dpi crops and no symbol remained uncertain. Things printed in a way a reader may question, kept as
printed and recorded in the page notes:
- (27) has `c(theta, v, r, f_t)`, (32) has `c(theta, v_theta, r, f_t)` and minimises over a bold capital Theta.
- (33): the term under the square root is `V_perp^infty / 4` (no square).
- (37): `v(t) = \int_{v_i}^{v_f} \dot v dt` (limits are velocities).

### Joins
- Set (`join_previous: space`): first prose item of pages 29, 30, 31, 32, 33, 34.
- Range boundary: `p0029-b003` joins the last paragraph of page 28 (`p0028-b009`, "...during every planning
  interval to"). Page 28's footer (`p0028-b010`) is omitted by its owner (checked at the end of my review), so
  the item before the join is that text item.
- Not set on purpose: the first items of pages 35 and 36 continue a sentence after a display equation on the
  previous page (they follow a `$$` block).
- Page 31: the single paragraph of that page continues from page 30 and onto page 32, with Figures 30 and 31
  printed above it. It is split at a sentence boundary (`p0031-b008` / new `p0031-b008b`) with the two figures in
  between, so no sentence is interrupted, but the paragraph appears as two paragraphs in the output.

### Text repairs of substance
- Page 36: split decimal `0 . 5`, garbled Table 1 pair labels, emphasis/`<sup>` debris in inline maths.
- Page 37: caption bound `$10\frac{\pi}{2}R_{\text{max}}$` (extractor had `10<sup><u>π</u></sup> 2<sup>Rmax.</sup>`).
- Pages 38-41: reference list rebuilt entry by entry from the native text lines (the extractor merged, split and
  once duplicated entries). Line-wrap repairs: `36(4):710–733`, `24(4):17–26`, "computationally",
  "rapidly-exploring", the binvox search URL; spaces restored after `ff` ligatures ("takeoff trajectory",
  "takeoff and landing", "take-off and landing").
- Authors' typos kept and noted per page (e.g. "flat plat theory", "We would like determine", "An survey").

### Remaining diagnostics
| Page | Missing lines | Number differences | Category |
| --- | --- | --- | --- |
| 30 | 1 | none | (a) `≈5` written `$\approx 5$` |
| 31 | 2 | none | (a) degree sign in LaTeX; one line spans the sentence split around the figures |
| 34 | 17 | none | (a) equations (27)-(31) and inline symbols |
| 35 | 15 | none | (a) equations (32)-(36) and inline symbols |
| 36 | 11 | none | (a) equations (37)-(40) and inline symbols |
| 37 | 3 | none | (a) Figure 35 caption maths |
Pages 29, 32, 33, 38, 39, 40, 41: `OK`. Adjudication notes written for pages 30, 31, 34, 35, 36, 37
(`missing_lines` only; no number differences and no second-parser differences were reported on any page).

### Proposals for shared files (coordinator)
- `plan.json` `title`: "Agile Fixed-Wing UAVs for Urban Swarm Operations" (currently the file stem).
- `plan.json` `notes` candidates: (1) Table 1 has merged pair-label cells that are repeated on both rows in the
  CSV; (2) axis labels of Figures 29, 30(c) and 32(c) are clipped in the publisher's PDF itself; (3) the paragraph
  on PDF page 31 is split around Figures 30 and 31.
- Optional `reading_order`: if the coordinator prefers the page-31 paragraph in one piece, move `p0031-b001`,
  `p0031-b004`, `p0031-b005`, `p0031-b007` after `p0032-b008` and add `join_previous: space` to `p0031-b008b`
  (it would then directly follow `p0031-b008`).
- Navigation: unnumbered headings in this range are `## Acknowledgments`, `## Appendices` (with `### A.` and
  `### B.` below it), `## ORCID`, `## References`.
- No asset-name clashes found when scanning all 41 page files at the end of the review.

### Limitations
- No TeX source: bold/italic distinctions in the maths (bold upright R, f, e, n, g, a; bold-italic theta) were
  read from the glyph shapes at high zoom.
- The STOMP GUI screenshot in Figure 34 contains tiny text that is illegible in the source PDF.
- Italics in the reference list were taken from the extractor's font information and compared with page crops
  for every entry on pages 37-41; punctuation inside entries is from the PDF text layer.

### Notes on the brief
- "Put each float between complete paragraphs" cannot be met when a page's only prose is one paragraph that
  runs in from the previous page and out to the next (page 31); a rule for that case would help.
- For author-year reference lists the example `[12] ...` does not apply; I used one text item per entry without
  list markers.
- `check` reports a line as missing whenever an inline symbol is rewritten, even `≈`; this makes otherwise clean
  prose pages need a note.
