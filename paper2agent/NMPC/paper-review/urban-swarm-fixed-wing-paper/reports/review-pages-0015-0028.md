# Review report: "Agile Fixed-Wing UAVs for Urban Swarm Operations", PDF pages 15-28

Reviewer range: `pages/page-0015.json` ... `page-0028.json` (brief version 2, no TeX source available).
Document: `documents/s001-urban-swarm-fixed-wing`. Mathematics transcribed from 220-300 dpi crops.

## Per-page log

### Page 15 (printed 739) - reviewed [v2]
- Headings: `### 5.3. Control Experiments`, `### 5.4. Results`.
- Display maths: unnumbered three-line display for q, r, q_f as one `aligned` block. Inline maths in LaTeX.
- Figure 9 -> `figure-9` (two picture regions merged), caption item follows. Float placed after heading 5.4 and
  before the paragraph that continues onto page 16.
- Omitted: running header (b000), footer (b013).
- Joins: none at page top (page starts with a heading). Last paragraph continues on page 16.
- Check: 5 missing lines, all category (a) (LaTeX notation); no number differences. Note written.
- Authors' typo kept: "corresponded to a a path length".

### Page 16 (printed 740) - reviewed [v2]
- Continuing paragraph tail ("elastic mode operation ...") placed first, `join_previous: space` (joins page 15).
- Figure 10 -> `figure-10` (two regions merged), caption follows.
- Headings: `## 6. Outdoor Experiments with Onboard Processing`, `### 6.1. Onboard Processor Selection`,
  `### 6.2. The ACCIPITER Software Stack`.
- Omitted: header (b000), footer (b011). Last paragraph continues on page 17.
- Check: 1 missing line, category (a) (`$90^\circ$`). Note written.
- Authors' typos kept: "Robot Operating Sysem (ROS) and well as", "preformed on par".

### Page 17 (printed 741) - reviewed [v2]
- Continuing paragraph ("and Reconnaissance (see Figure 28) ...") first, `join_previous: space`.
- Figure 11: left plot -> `figure-11` (image); right-hand typeset table kept as a table item with rows
  (`figure-11-table`, label "Figure 11 (right panel): processor mass table", 7x2 strings, no printed table number).
  Caption follows both.
- Heading: `### 6.3. The ACCIPITER Hardware Stack`.
- Omitted: header (b000), footer (b009). Last paragraph continues on page 18.
- Check: 1 missing line, category (a) (`$90^\circ$` in the caption). Note written.

### Page 18 (printed 742) - reviewed [v2]
- Continuing paragraph ("Kinematic (RTK) GPS unit ...") first, `join_previous: space`.
- Figure 12 -> `figure-12` (two photographs merged), caption follows.
- Headings: `### 6.4. System Identification and Controller Configuration`,
  `### 6.5. At-Altitude Tests in Simulated Urban Environments`.
- Inline maths: gamma_{ar}, gamma_{al}, gamma_r, gamma_e, a_t = -4.905, b_t = 107.9, C_{n_d} = 0.0705.
- Omitted: header (b000), footer (b010). Last paragraph continues on page 19.
- Check: 1 missing line and the minus sign of -4.905 (U+2212 vs ASCII), both category (a). Note written.
- Authors' wording kept: "an collision radius".

### Page 19 (printed 743) - reviewed [v2]
- Continuing paragraph ("random tree (RRT). ...") first, `join_previous: space`.
- Figure 13 -> `figure-13` (three extractor regions covering panels (a)-(d) and the sub-labels merged into one crop), caption follows.
- Omitted: header (b000), footer (b007). Last paragraph continues on page 20.
- Check: OK. No mathematics.
- Authors' typo kept: "Seby CACTF" (caption).

### Page 20 (printed 744) - reviewed [v2]
- First paragraph continues from page 19: `join_previous: space`.
- Headings: `### 6.6. Flight Tests in Physical Urban Environment`, `### 6.7. Wind Compensation`.
- Figure 14 -> `figure-14` (three regions and sub-labels (a)-(c) merged), caption follows; emitted after the
  Section 6.6 paragraph that cites it and before heading 6.7 (printed at the page bottom, below a paragraph
  that continues on page 21).
- Omitted: header (b000), footer (b010).
- Check: 1 missing line, category (a) (`$\approx$ 1 m`). Note written.

### Page 21 (printed 745) - reviewed [v2]
- Continuing paragraph ("the existing wind estimates ...") first, `join_previous: space`.
- Figure 15 -> `figure-15` (plot and trajectory inset in one crop), caption follows.
- Headings: `## 7. Vision-Based Navigation and Feature Detection`, `### 7.1. Mapping`.
- Omitted: header (b000), footer (b010). Page ends with a complete paragraph.
- Check: 3 missing lines, category (a) (`$\approx$`). Note written.

### Page 22 (printed 746) - reviewed [v2]
- Algorithm 1 (RRT with frontier nodes) -> image `algorithm-1` plus transcription item `p0022-alg1-text`
  (no printed line numbers; em-space indentation for the printed nesting bars). Printed at the page top;
  emitted after the Section 7.2 paragraph that introduces it.
- Headings: `### 7.2. Dynamic RRT Generation`, `### 7.3. Collision Constraints for Trajectory Optimization`.
- Omitted: header (b000), footer (b010). No join at the top; last paragraph continues on page 23.
- Check: no missing lines; two extra `1` tokens from the algorithm transcription, category (a). Note written.

### Page 23 (printed 747) - reviewed [v2]
- First paragraph continues from page 22: `join_previous: space`. Its inline maths (distance-to-obstacle constraint
  d(x) >= r, K = 10, averaged distance, gradient) is LaTeX, read from a 300-dpi crop. No display equations.
- Headings: `### 7.4. Experimental Setup`, `### 7.5. Simulated Perception Navigation Experiment`,
  `### 7.6. Vision-based Collision-Free Navigation Experiment`.
- Figure 16 -> `figure-16`, caption follows; emitted after the Section 7.5 paragraph that
  cites it and before heading 7.6 (printed at the page bottom).
- Omitted: header (b000), footer (b011). Page ends with a complete paragraph.
- Check: 5 missing lines, category (a) (inline maths). Note written.

### Page 24 (printed 748) - reviewed [v2]
- Figure 17 -> `figure-17`, Figure 18 -> `figure-18` (each merged from two regions), captions follow; printed
  order kept (floats first; page 23 ends with a complete paragraph, no join).
- Heading: `### 7.7. Feature Detection at High Speeds and Aggressive Attitudes`.
- Omitted: header (b000), footer (b012). Last paragraph continues on page 25.
- Check: OK. No mathematics.

### Page 25 (printed 749) - reviewed [v2]
- Figure 19 -> `figure-19` (two regions merged), Figure 20 -> `figure-20` (two regions merged),
  Figure 21 -> `figure-21`; captions follow each.
- The only prose on the page is one block that continues the last sentence of page 24 and continues on page 26,
  with the three figures printed above it. It is split at a sentence boundary into `p0025-b009`
  (`join_previous: space`, joins page 24) and the new item `p0025-b009b`; the three figures are emitted between
  them. No sentence is interrupted, but the paragraph is divided by the floats (see "Proposals").
- Omitted: header (b000), footer (b010).
- Check: 1 missing line = the native line that spans the split point (both halves present verbatim); structural
  artefact, no text missing. Note written.
- Authors' typos kept: "makers" (three times) for "markers".

### Page 26 (printed 750) - reviewed [v2]
- Paragraph tail ("the approximate positions of the markers ...") first, `join_previous: space` (joins `p0025-b009b`).
- Figure 22 -> `figure-22` (four photographs merged), Figure 23 -> `figure-23` (two plots merged); captions follow.
- Heading: `## 8. Swarm System Integration for Urban Operations` (extractor had `#`).
- Omitted: header (b000), footer (b012). Page ends with a complete paragraph.
- Check: 1 missing line, category (a) (`$\leq$`, `$50^\circ$` in the Figure 23 caption). Note written.

### Page 27 (printed 751) - reviewed [v2]
- **Coordinator edit reverted:** `p0027-b007` is the printed heading "8.1. Automatic Take-Off". It had been set
  to `omit` with the reason "Paper title on PDF page 27 ... duplicates the generated document title" (the
  extractor had tagged it `# `). Restored as `### 8.1. Automatic Take-Off`.
- Figure 24 -> `figure-24` (two photographs merged), Figure 25 -> `figure-25` (rendering + still merged);
  captions follow. Figure 25 is emitted after the first paragraph of Section 8.1 (which cites it) instead of
  before the heading, so that it belongs to its subsection.
- Omitted: header (b000), footer (b010). No joins (page 26 and this page end with complete paragraphs).
- Check: 4 missing lines, category (a) (`$\approx$`, degree signs). Note written.
- Authors' typos kept: "Do do this", "we were able achieve".

### Page 28 (printed 752) - reviewed [v2]
- Figure 26 -> `figure-26` (two plots merged), Figure 27 -> `figure-27`; captions follow.
- Headings: `### 8.2. Automatic Landing`, `### 8.3. Multi-UAV Collision Avoidance` (extractor had `#`).
- Emitted order: heading 8.2, paragraph, Figure 26, heading 8.3, Figure 27, paragraph (continues on page 29).
  Printed order has both figures at the top of the page.
- Omitted: header (b000), footer (b010). No join at the top.
- Check: no missing lines; minus signs of `$(-140, 0, -30)$` (U+2212 vs ASCII), category (a). Note written.

## Summary

All 14 pages (15-28) are reviewed, saved with `reviewed: true` and `review_notes` starting with `[v2]`.
Every page was compared with its preview; every figure box was checked on a crop of the box; all mathematics
was read from 200-300 dpi crops (no TeX source exists for this paper).

### Assets (asset names are printed numbers; no page-numbered names were needed)
| Page | Assets |
| --- | --- |
| 15 | `figure-9` |
| 16 | `figure-10` |
| 17 | `figure-11` (plot), `figure-11-table` (table item with rows, right-hand panel of Figure 11) |
| 18 | `figure-12` |
| 19 | `figure-13` |
| 20 | `figure-14` |
| 21 | `figure-15` |
| 22 | `algorithm-1` (image) + transcription `p0022-alg1-text` |
| 23 | `figure-16` |
| 24 | `figure-17`, `figure-18` |
| 25 | `figure-19`, `figure-20`, `figure-21` |
| 26 | `figure-22`, `figure-23` |
| 27 | `figure-24`, `figure-25` |
| 28 | `figure-26`, `figure-27` |

19 figures (9-27), 1 algorithm, 1 table item. The extractor produced 37 picture regions and 1 table region for
these 19 figures (counted in `evidence/`); they are merged into 19 figure items plus the Figure 11 table item.
Algorithm 1 had been extracted as text and is now an image crop plus transcription. No printed "Table N" occurs in this range. Asset names and item ids are unique across the document
(checked over all 41 page files at the time of writing).

### Mathematics
- Display equations: one unnumbered three-line display on page 15 (`aligned` block for q, r, q_f). There are
  no numbered equations in pages 15-28.
- Inline maths converted to LaTeX on pages 15, 16, 17, 18, 20, 21, 23, 26, 27, 28 (see per-page log); the
  densest is the distance-to-obstacle constraint and its gradient on page 23.
- Formulas kept as images: none. No symbol remained uncertain after zooming.
- TeX-versus-PDF disagreements: not applicable (no TeX source).

### Joins
- Set (`join_previous: space`) on the first prose item of pages 16, 17, 18, 19, 20, 21, 23, 25, 26.
- No join on pages 15, 22, 24, 27, 28 (previous page ends with a complete paragraph or caption, or the page
  starts with a heading).
- No `join_previous` follows a `$$` block (the paragraph after the page-15 display is a new, indented paragraph).
- Range boundaries: page 15 starts with heading 5.3 (page 14 ends with the Figure 8 caption): nothing needed.
  Page 28 ends with the Section 8.3 paragraph "... during every planning interval to", which continues on
  page 29; `p0029-b003` already carries `join_previous: space` (verified read-only).

### Extractor warnings
All 25 warnings in this range are "Review possible header/footer" for the running header (b000) and the
journal footer line. Each was confirmed on the page image and set to `omit` with a specific reason. Pages 20,
22 and 28 list only one of the two in `warnings`; the other furniture item on those pages is omitted as well.

### Text repairs of substance
- Page 27: heading "8.1. Automatic Take-Off" restored from a wrong `omit` (see below).
- Pages 26-28: single-`#` headings from the extractor corrected to `##` (8.) and `###` (8.1-8.3).
- Glyph-soup maths and `<sup>` degree signs replaced by LaTeX on pages 15, 18, 23, 26, 27.
- Reading order: continuing paragraph tails moved above the figures on pages 16-21, 23, 25, 26; floats moved
  to the paragraph that cites them on pages 15, 20, 22, 23, 27, 28.
- Authors' typos are kept verbatim and listed in the page notes ("a a path length", "Sysem", "and well as",
  "preformed", "an collision radius", "Seby CACTF", "shows the how", "makers", "Do do this",
  "we were able achieve", "with regards landing").

### Remaining diagnostics (all explained in `adjudication-notes/page-NNNN.json`)
| Page | Missing lines | Number differences | Category |
| --- | --- | --- | --- |
| 15 | 5 | - | (a) LaTeX notation |
| 16 | 1 | - | (a) degree sign |
| 17 | 1 | - | (a) degree sign in caption |
| 18 | 1 | -4.905 minus glyph (both parsers) | (a) |
| 19 | 0 | - | OK |
| 20 | 1 | - | (a) approx sign |
| 21 | 3 | - | (a) approx signs |
| 22 | 0 | two extra `1` (both parsers) | (a) text of the algorithm transcription |
| 23 | 5 | - | (a) inline maths |
| 24 | 0 | - | OK |
| 25 | 1 | - | structural: native line spans the split between `p0025-b009` and `p0025-b009b`; both halves present verbatim |
| 26 | 1 | - | (a) `\leq`, degree sign in caption |
| 27 | 4 | - | (a) approx and degree signs |
| 28 | 0 | -140, -30 minus glyphs (both parsers) | (a) |

Nothing of category (b) remains.

## Proposals for shared files / notes for the coordinator
1. **Title-dedup script mis-fired on page 27.** `p0027-b007` ("8.1. Automatic Take-Off") had been set to `omit`
   as "Paper title on PDF page 27 (page 1 is the IEEE copyright cover sheet) ...". That reason belongs to a
   different paper; here it removed a real subsection heading. I restored it as `### 8.1. Automatic Take-Off`.
   Please make sure the script is not re-applied to this document (it seems to key on any `# ` heading that is
   not on page 1; pages 26 and 28 also had extractor `# ` headings, now `##`/`###`). At the time of writing the
   only remaining `# ` heading in the document is the real title on page 1.
2. **Page 25 float placement.** The page has three figures above a single prose block that continues both from
   page 24 and onto page 26. I split the block at a sentence boundary (`p0025-b009` | Figures 19-21 |
   `p0025-b009b`). If you prefer an unbroken paragraph, add a `reading_order` in `plan.json` that moves
   `p0025-b001, b003, b004, b006, b007, b008` after `p0026-b009` (the end of that paragraph), and tell me or set
   `"join_previous": "space"` on `p0025-b009b` at the same time.
3. **Figure 11** is half plot, half typeset table. The table half is a `table` item with rows
   (`figure-11-table`, label "Figure 11 (right panel): processor mass table"), so it will be written to the
   table asset directory although it is not a numbered table. If you want strict "one figure item per figure",
   change the figure bbox to `[126, 67.5, 475, 225]` and delete the table item; the masses would then exist only
   in the image.
4. Navigation headings in this range: `## 6.`, `### 6.1.`-`6.7.`, `## 7.`, `### 7.1.`-`7.7.`, `## 8.`,
   `### 8.1.`-`8.3.`, plus `### 5.3.` and `### 5.4.` on page 15. No `####` level occurs in this range.
5. No plan note is needed for these pages.

## Limitations
- Plot-internal text (tick labels, legends, the small axis labels of Figure 13(d) and the component labels in
  the right photograph of Figure 12) exists only inside the image crops; it is legible at the source resolution
  but not searchable.
- Algorithm 1 has no printed line numbers; the transcription shows nesting by indentation (`&emsp;`), which is a
  rendering choice. The image crop is the authority.
- Italic emphasis that is not mathematics (the Latin "a priori" on page 21) is kept as Markdown emphasis.

## Notes on the brief
- The rule "start with the prose continuing from the previous page, end with the prose continuing onto the next
  page, floats between complete paragraphs" has no solution when a page's only prose block does both (page 25);
  an explicit rule for that case (split at a sentence boundary, or coordinator `reading_order`) would help.
- The brief does not say how to treat a figure whose panel is a typeset table (Figure 11).
- `check` reports a native line as missing when a paragraph is split inside that line; this is a third category
  besides (a) and (b) and could be named in the brief.
