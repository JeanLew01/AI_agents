# Review report: post-stall-navigation-paper, pages 1-7 (brief version 2)

Paper: "Post-Stall Navigation with Fixed-Wing UAVs using Onboard Vision", Polevoy, Basescu, Scheuer, Moore
(arXiv:2201.01186v1, ICRA 2022). Document `documents/s001-post-stall-navigation`, 7 pages, IEEE two-column.
TeX source used: `tex-source/post-stall-navigation/` (`main.tex` inputs `intro`, `approach`, `simulation`,
`experiments`, `discussion`; `results.tex` is commented out and is NOT part of the printed paper; `main.bbl`).

Starting state found: no page was marked reviewed and no `review_notes` existed; pages 1-5 carried partial
structural edits of the interrupted version-1 run (figure boxes, order, some headings), pages 6-7 were raw
extractor output. Every page was re-examined from the page render.

## Per-page log

### Page 1 - done, `[v2]`, check OK
- Items: arXiv stamp (omit), title `#`, authors, footnote 1 (affiliation/e-mails) + distribution statement,
  abstract, `## I. INTRODUCTION`, three paragraphs, Figure 1 + caption, one paragraph, `## II. RELATED WORK`,
  first part of its first paragraph.
- Figure: `figure-1` (both stacked screenshots in one crop, bbox [348.5, 143.5, 522.5, 326.0]).
- Joins: `p0001-b012` (`space`, column break inside "Real-time mapping ..." paragraph). The page ends with an
  unfinished paragraph that continues on page 2.
- Extractor warning (possible header/footer `p0001-b000`): it is the rotated arXiv margin stamp; omitted with reason.
- Footnote placement: the `\thanks` footnote is kept directly after the author line (not at the end of the page
  items) so that the page ends with the prose that continues on page 2.
- No mathematics.

### Page 2 - done, `[v2]`, check OK
- Prose only: rest of Related Work, `## III. APPROACH`, `### A. Mapping`, `### B. RRT Generation`.
- Joins: `p0002-b000` (`space`, continues page 1), `p0002-b004` (`space`, column break). Last item continues on page 3.
- No mathematics, figures or tables. Authors' typos kept ("most of approaches", "we show in the importance of").

### Page 3 - done, `[v2]`, check ATTENTION (notation only, adjudication note written)
- Algorithm 1: image `algorithm-1` (`p0003-b003`, bbox [52, 304, 301, 532]) + transcription (`p0003-b004`);
  no printed line numbers, nesting rendered as nested list. Authors' pseudocode errors preserved
  (`IS_FRONTIER_NODE()x_new, map)`, `xgoal.FIND_CLOSEST(f)`).
- Display equations (1), (2), (3): now `text` items with `$$...$$` and `\tag{1}`..`\tag{3}` taken from
  `approach.tex`, checked against 280-300 dpi crops. No formula kept as image.
- Inline maths of three paragraphs rewritten in LaTeX.
- Joins: `p0003-b000` (`space`, continues page 2), `p0003-b010` (`space`, column break).
- Heading `### C. Direct Trajectory Optimization`.
- Diagnostics: 32 missing lines (all maths / lines with inline maths), number differences from LaTeX notation
  and from the algorithm transcription: category (a).

### Page 4 - done, `[v2]`, check ATTENTION (notation only, adjudication note written)
- Display equations (4), (5): `text` items with `$$...$$`, `\tag{4}`, `\tag{5}` from `approach.tex`, checked
  against a 280 dpi crop. No formula kept as image.
- Inline maths in LaTeX (`$n=3$`, `$\mathbf{\Sigma}^{-\frac{1}{2}}$`, `$\mathcal{N}(diag(0, 0, 0),\,diag(0.1, 0.1, 0.1))$`, ...).
- Headings `## IV. REAL-TIME SIMULATION STUDY`, `### A. Simulation Setup`, `### B. Experiment 1: Use of NanoMap History`,
  `### C. Experiment 3: Noise` (printed numbering "Experiment 3" kept).
- Joins: `p0004-b006` (`space`, column break). `p0004-b000` ("where $n=3$ ...") deliberately NOT joined to the
  display equation (3) that ends page 3 (review queue flagged it as a possible cross-page join).
- Diagnostics: 10 missing lines (maths), number differences from LaTeX notation: category (a).

### Page 5 - done, `[v2]`, check OK
- Figures: `figure-2` (one item for the six panels (a)-(f), bbox [73.5, 53, 538.5, 274]), `figure-3`
  ([101, 333, 252, 424.6]), `figure-4` ([101, 461.5, 252, 553]), `figure-5` ([323.4, 333, 547.8, 435.5]); each with
  its caption item. All boxes checked by crop against the embedded-image rectangles.
- Headings `## V. HARDWARE EXPERIMENTS` (was mis-classed as caption), `### A. Experimental Set-up`,
  `### B. Simulated Perception`.
- Joins: `p0005-b014` (`space`, column break; Figure 5 placed after the completed paragraph). The last item
  continues on page 6.
- No mathematics, no tables.

### Page 6 - done, `[v2]`, check OK
- Figures: `figure-6` ([86, 49, 259.5, 164.2]), `figure-7` ([70.2, 221.2, 280.8, 343.8]), `figure-8`
  ([345.2, 49, 518.5, 164.2]), `figure-9` ([360, 216, 507.5, 316.2]), `figure-10` ([345.2, 632, 518.5, 714.1]).
  Extractor boxes followed the untrimmed image rectangles; re-boxed to the visible plots (ink measured, crops viewed).
  The old Figure 10 box overlapped the last acknowledgement line.
- Text repair of substance: body text glued to two captions was split off: `p0006-b003b` ("with standard deviation
  inflation ... $T_H=1s$ ... 5Hz.", continuation of page 5) and `p0006-b013b` ("part of the wall after the corner
  ...", continuation of `p0006-b009`).
- Joins: `p0006-b003b` (`space`, continues page 5), `p0006-b013b` (`space`, column break).
- Headings fixed: `### C. Control Experiment`, `## VI. DISCUSSION`, `## VII. ACKNOWLEDGEMENT` (were `#`).
- Figure 10 moved from its printed position (after the acknowledgement) to the paragraph of Section V-C that cites it.
- Inline maths: `$T_H=1s$`.

### Page 7 - done, `[v2]`, check OK
- `## REFERENCES` (was `#`) + 30 text items, one entry per item, order [1]-[30]. The extractor had interleaved the
  columns ([22]-[30] between [9] and [10]) and merged [3]+[4], [15]+[16], [23]+[24]; new ids `p0007-b003b`,
  `p0007-b022b`, `p0007-b010b`.
- Entry text generated from `main.bbl` and compared per entry (punctuation included) with the native PDF lines
  (`_scratch/poststall-1-7/v2/p7.py`); only ligature code points, three line-wrap hyphens and "ö" differ.

## Summary

| Page | State | `check` | Floats / equations (asset names) |
| --- | --- | --- | --- |
| 1 | reviewed `[v2]` | OK | `figure-1` |
| 2 | reviewed `[v2]` | OK | none |
| 3 | reviewed `[v2]` | ATTENTION, category (a) only | `algorithm-1` (+ transcription), equations (1), (2), (3) as LaTeX |
| 4 | reviewed `[v2]` | ATTENTION, category (a) only | equations (4), (5) as LaTeX |
| 5 | reviewed `[v2]` | OK | `figure-2`, `figure-3`, `figure-4`, `figure-5` |
| 6 | reviewed `[v2]` | OK | `figure-6`, `figure-7`, `figure-8`, `figure-9`, `figure-10` |
| 7 | reviewed `[v2]` | OK | none (30 reference entries) |

The paper has no tables. 11 image assets in total (10 figures + 1 algorithm); asset names are unique in the document.
The extractor's 14 picture regions map to the 10 printed figures (Figure 1 = 2 stacked images, Figure 2 = 6 panels).

### Joins
- Within the range: `p0001-b012`, `p0002-b000` (page 1 -> 2), `p0002-b004`, `p0003-b000` (page 2 -> 3), `p0003-b010`,
  `p0004-b006`, `p0005-b014`, `p0006-b003b` (page 5 -> 6), `p0006-b013b`; all `space`.
- Not joined on purpose: `p0004-b000` ("where $n=3$ ...") after display equation (3) at the end of page 3, and the
  "where" item after equation (1) on page 3 (prose following a `$$` block starts a new block).
- Range boundaries: the range is the whole document, so no join is needed from outside.

### Formulas kept as images
None. All five numbered display equations are LaTeX text items with `\tag{1}`-`\tag{5}`; all 83 maths segments of
the seven pages were test-compiled with pdflatex (amsmath) and the rendered equations compared with the PDF.

### TeX versus PDF
- No disagreement in the mathematics.
- `\vect{\lambda}` (= `\mathbf{\lambda}`) prints as a non-bold lambda; written `\lambda`.
- `main.bbl` entry [17] contains a U+2010 hyphen ("High‐speed"); the PDF prints an ordinary hyphen, which is used.
- `results.tex` is commented out in `main.tex` (`%\input{results}`) and is not part of the printed paper; nothing was
  taken from it (it contains controller weights Q, r, Q_f, delta_f that the published PDF does not print).
- Footnote e-mail list: the space after "Luca.Scheuer," falls on a line break in the PDF and was taken from `main.tex`.

### Printed peculiarities kept unchanged (possible author typos; not corrected)
- Eq. (1): initial-state bound printed with `x_N`; sum to `N` with terminal term `x_{N+1}`; bold subscripts in the cost.
- Eqs. (3), (5): exponent printed as `(r+s)^{2^{n/2+k}}`.
- Algorithm 1: `IS_FRONTIER_NODE()x_new, map)` and `xgoal.FIND_CLOSEST(f)`.
- Section IV-C is printed "Experiment 3: Noise" although it is the second experiment.
- Prose: "amendable", "most of approaches", "we show in the importance of", "a reduced the computational burden",
  "the summing a maximum of 75 terms", the sentence with the gradient of d(x) has no full stop.

### Remaining diagnostics
- Page 3: 32 missing lines, number differences, second-parser number differences: all category (a) (LaTeX notation and
  the Algorithm 1 transcription); `adjudication-notes/page-0003.json`.
- Page 4: 10 missing lines, number differences, second-parser number differences: all category (a);
  `adjudication-notes/page-0004.json`.
- Pages 1, 2, 5, 6, 7: `OK`, no note file.

### Proposals for shared files (coordinator)
- `plan.json` `title`: "Post-Stall Navigation with Fixed-Wing UAVs using Onboard Vision" (currently "post-stall-navigation").
- `plan.json` `notes` (suggested):
  - "Source: arXiv:2201.01186v1 [cs.RO], 4 Jan 2022 (ICRA 2022); the rotated arXiv margin stamp on page 1 is omitted from the text."
  - "Display equations (1)-(5) and inline mathematics were transcribed to LaTeX from the authors' arXiv TeX source and checked against the PDF; printed peculiarities (x_N in the initial-state bound of (1), the exponent (r+s)^{2^{n/2+k}} in (3) and (5), the pseudocode slips in Algorithm 1, the heading 'Experiment 3: Noise') are reproduced as printed."
  - "Algorithm 1 is given as an image and as a transcription; block nesting (vertical rules in the PDF) is rendered as nested list items."
  - "Floats were moved to paragraph boundaries; Figure 10, printed after the acknowledgement, is placed with the paragraph of Section V-C that cites it. The author footnote (affiliation, e-mail addresses, distribution statement) follows the author line."
  - "The paper has no tables. The first-page title duplicates the generated title."
- Navigation headings: I. INTRODUCTION, II. RELATED WORK, III. APPROACH (A. Mapping, B. RRT Generation, C. Direct
  Trajectory Optimization), IV. REAL-TIME SIMULATION STUDY (A, B, C), V. HARDWARE EXPERIMENTS (A, B, C),
  VI. DISCUSSION, VII. ACKNOWLEDGEMENT, REFERENCES. No `reading_order` is needed.
- Asset names: no clash inside the document (`figure-1` ... `figure-10`, `algorithm-1`).
- `review-queue.json` items: extractor warning page 1 resolved (omit with reason); cross-page joins 1->2 and 2->3 set,
  3->4 deliberately not set (see above); the unflagged join 5->6 was found and set.

### Limitations
- Figure 10's top edge has only about 0.8 pt of margin because the plot starts 1.8 pt below the last acknowledgement
  line; the crop contains the complete plot and none of the text line.
- Figures 6-8 and 10 are trimmed by the authors in the PDF itself (lower axis ticks cut); nothing more exists to crop.
- Typography not reproduced: bold abstract body, small caps of section headings, italics of the if-conditions in
  Algorithm 1 (the image crop preserves them).
- Rendering of `\tag` inside `$$ ... $$` depends on the Markdown maths renderer; the tags are also visible as plain
  `\tag{n}` text in the source.

### Notes on the brief
- "Footnotes ... at the end of that page's items" conflicts with "the page must end with the prose that continues onto
  the next page" (and with the requirement that the item before a joined item is text/caption of the same paragraph)
  when a page has both a footnote and a paragraph running over the page break (page 1 here). I placed the author
  footnote right after the author line; a rule for this case would help.
- The brief does not say whether prose that continues a sentence after a display equation ("where ...") should carry
  `join_previous`; I did not join across `$$` blocks.
- The brief asks for "numbered lines as printed" in algorithm transcriptions but not how to keep block nesting when
  the algorithm has no line numbers; I used nested Markdown list items.
- `check` only reports letters/digits; a punctuation-preserving per-item diff (`_scratch/poststall-1-7/pdiff.py`,
  left by the earlier run) was useful for hyphens and could be added to the shared tools.
