# DIAL-MPC (arXiv:2409.15610v1) page review, pages 1-9 (brief version 2)

Document: `dial-mpc-paper/documents/s001-dial-mpc`. TeX aid: `NMPC/tex-source/dial-mpc/`.
Scratch: `_scratch/dial-1-9/` (edit scripts `n1.py` ... `n9.py`; untouched extractor output saved by the earlier run in `orig/`).

## Per-page log

### Page 1 (done, `[v2]`, check: OK 84/84)
- Items: title, authors, abstract (run-in "Abstract—" kept as text), `## I. INTRODUCTION`, five paragraphs, Fig. 1 + caption, two first-page footnote items.
- Figure: `figure-1` bbox [311, 155.5, 560, 361] (image box 313.2,157.7,558.0,358.9; checked by crop).
- Join: "Specifically, a large sampling range ..." (`p0001-b011`, right column below Fig. 1) has `join_previous: space` to the paragraph that starts at the foot of the left column; Fig. 1 moved after that paragraph.
- Footnotes: placed before the last paragraph (which continues onto page 2), not at the very end of the page.
- Repairs: `13 . 4` -> `13.4`, glued compounds (real-world, high-dimensional, reduced-order, full-order, DIAL-MPC, dual-loop), `<sup>`/`<u>` removed, `$u_H$` in caption.
- Not reproduced: underlining of the initials D-I-A-L-M-P-C in the acronym expansion (stated in the page notes).

### Page 2 (done, `[v2]`, check: 102/105 lines, 3 missing lines of category (a), no number differences)
- Items: continuation paragraph (`join_previous: space` to page 1), three contribution bullets, `## II. RELATED WORK` with `### A/B/C`, `## III. METHOD`, `### A. Sampling-Based MPC as Single-stage Diffusion`, unnumbered optimal-control problem, MPPI paragraph (continues on page 3).
- Equation: the unnumbered optimal-control problem converted from a formula image to a `$$ aligned $$` text item (from `30algo.tex`, checked against a 200-dpi crop).
- Repairs: heading levels, glued compounds (whole-body, zeroth-order, sample-hungry, diffusion-inspired, III-B), `21– 24` -> `21–24`, all inline maths in LaTeX.
- Remaining diagnostics (a): the three lines contain `\mathcal{X}`, `\mathcal{U}`, `\mathcal{N}`; adjudication note written.

### Page 3 (done, `[v2]`, check: 74/104 lines; 30 missing lines and the number difference are category (a))
- Items: continuation of the page-2 sentence (`join_previous: space`), eq. (1), "MPPI as a single-stage Diffusion." paragraph, **Proposition 1 (Adopted from [43])**, eq. (2), **Proof**, eqs. (3a)-(3f) (one item, six `$$` blocks with `\tag{3a}` ... `\tag{3f}`), proof explanation ending with `$\blacksquare$`, "In other words ..." paragraph, Fig. 2 + caption, `### B. Diffusion-Inspired Annealing`, its paragraphs, Fig. 3 + caption, Footnote 1, last paragraph (continues on page 4).
- Figures: `figure-2` bbox [311, 48, 560, 130]; `figure-3` bbox [475.4, 471.2, 560, 559.8] (new item `p0003-fig3`, caption `p0003-cap3`). The extractor's big "figure" over the wrapped Fig. 3 had swallowed the paragraph "Coverage and convergence trade-off. ..."; that paragraph is text again.
- Equations converted from formula images: (1), (2), (3a)-(3f). TeX and PDF agree.
- Joins: `p0003-b000` -> page 2; `p0003-b015` ("(proposition 1), a natural question arises ...") -> `p0003-b011` across the column break; Fig. 2 moved before the heading of III-B so that it does not interrupt that sentence.
- Extractor items dropped after merging: `p0003-b007` (second half of the (3) image), `p0003-b019` (second half of the "This trade-off ..." paragraph).
- Footnote 1 placed before the last paragraph (which continues on page 4).
- Remaining diagnostics (a): LaTeX notation in display and inline maths; `−1` vs `-1` in the five `\Sigma^{-1}` exponents. Adjudication note written.
- Authors' typos kept: "convolusion", "kernal", "robot need to jump", "optimality(i.e., convergence)".

### Page 4 (done, `[v2]`, check: 66/85 lines; 19 missing lines and the number differences are category (a))
- Items: continuation of page 3 (`join_previous: space`), paragraph, Fig. 4 + caption, "Annealing in diffusion process." paragraph, eq. (4), two paragraphs, `### C. Diffusion-Inspired Annealing for Sampling-Based MPC`, paragraph split across the column break (`p0004-b009` + new `p0004-b013a` with `join_previous: space`), Algorithm 1 (image + transcription), "Dual-loop annealing." paragraph, "Trajectory-level annealing." + eq. (5), "Action-level annealing." + eq. (6), last paragraph (continues on page 5).
- Figure: `figure-4` bbox [52, 159.3, 300.8, 256.5]. Algorithm: `algorithm-1` (kind figure) bbox [311, 48.5, 560, 214] + text transcription `p0004-b011` (lines 1-11).
- Equations converted from formula images: (4), (5), (6). TeX and PDF agree.
- Extractor item dropped: `p0004-b012` (scrambled algorithm lines, replaced by the transcription).
- Authors' inconsistency kept as printed: Algorithm 1 inner loop "for i = 1 to N" while the text and (4), (5) anneal from i = N down to 1.
- Remaining diagnostics (a): LaTeX notation; `−1` vs `-1` in five subscripts; extra numbers from the Algorithm 1 transcription (its printed lines are inside the retained image). Adjudication note written.

### Page 5 (done, `[v2]`, check: 103/106 lines; 3 missing lines of category (a), no number differences)
- Items: continuation of page 4 (`join_previous: space`), paragraph, eq. (7), paragraph, `## IV. EXPERIMENT`, two paragraphs, `### A. Convergence and Coverage`, paragraph split across the column break (`p0005-b010` has `join_previous: space`), Table I + caption, Fig. 5 + caption, Footnote 2, "Convergence of DIAL-MPC." paragraph (continues on page 6).
- Table: `table-1` (7 x 4 strings, bbox [322, 109, 549, 187]); asterisk note stays in the printed caption.
- Figure: `figure-5` bbox [311, 298.5, 560, 487.5], merged from three extractor pictures (`p0005-b014`, `p0005-b015` dropped).
- Equation converted from a formula image: (7).
- TeX vs PDF: footnote 2 is printed "can be found in A." (TeX: "in Appendix \ref{subsec:Hardware}"); PDF wording kept.
- Repairs: split decimals 3.9, 0.2, 0.05, 0.4, 13.4, 107.7%; glued "DIALMPC", "realworld".
- Remaining diagnostics (a): `$\Sigma^i_{t+h}$` on two prose lines and one fragment of (7). Adjudication note written.

### Page 6 (done, `[v2]`, check: OK 90/90)
- Items: continuation of page 5 (`p0006-b005`, `join_previous: space`), Fig. 6 + caption, paragraphs, `### B. Test-Time Generalizability`, paragraphs, "Dynamic-level generalizability." paragraph split across the column break (`p0006-b001` has `join_previous: space`), Table II + caption, Fig. 7 + caption, `### C. Robustness to Model Mismatch`, paragraphs, `## V. CONCLUSION`, paragraph (continues on page 7).
- Figures: `figure-6` bbox [52, 48.1, 301, 177] (extractor box reached into the right column), `figure-7` bbox [311, 262.8, 560, 395.8]. Table: `table-2` (3 x 3 strings).
- Reading order rebuilt (the extractor mixed left and right column items).
- Repairs: split decimals 3.9, 3.5%; glued DIAL-MPC, training-free, test-time.
- Kept as printed: "10kg" (Fig. 6 caption), "DIAL-MPC ’s robustness" (with space), several grammatical slips.

### Page 7 (done, `[v2]`, check: 148/148 lines; number differences of category (a) only)
- Items: continuation of the Conclusion (`p0007-b002`, `join_previous: space` to page 6), Table III + caption, `## REFERENCES`, entries [1]-[38] (one text item each, printed style, list dashes removed).
- Table: `table-3` (6 x 3 strings, bbox [83.5, 48.5, 269.3, 122.2]); caption item changed from text to caption. Table III floats at the top of the left column above the end of the Conclusion; it is placed after the Conclusion paragraph.
- Reference repairs: four arXiv identifiers rejoined (1811.07819, 2401.16337, 1503.03585, 2310.04590), "Hernández-Lobato", "Human-to-Humanoid", "Whole-Body", "$L$1-Adaptive" in [34], emphasis spacing.
- Remaining diagnostics (a): the four rejoined arXiv identifiers count as different number tokens. Adjudication note written.

### Page 8 (done, `[v2]`, check: 122/128 lines; 6 missing lines and the number differences are category (a))
- Items: references [39]-[46] (one item each; [46] moved back into sequence), `## APPENDIX`, `### A. Hardware and Software Setup`, paragraphs, eq. (8), "where ..." sentence, "Algorithm Implementation:" paragraph (new `p0008-b015a`) continued in the right column (`p0008-b018`, `join_previous: space`), Table IV + caption, Fig. 8 + caption, `### B. Task Implementation Details`, "Quadruped Velocity Tracking" paragraph, start of "Quadruped Sequential Jumping" (new `p0008-b020a`, continues on page 9).
- Table: `table-4` (11 x 5 strings, bbox [311.2, 48.5, 564.4, 176]); merged parent headers repeated in combined column names ("Walking and Tracking: DIAL-MPC", ...). Caption item changed from text to caption.
- Figure: `figure-8` bbox [311, 251.2, 560, 368.1].
- Equation converted from a formula image: (8). TeX and PDF agree.
- Reference repairs: arXiv identifiers rejoined (2108.10470, 1707.06347, 2407.01573).
- Remaining diagnostics (a): `\tau_i`, `\omega_i`, `\pm` notation; rejoined arXiv identifiers. Adjudication note written.

### Page 9 (done, `[v2]`, check: 83/101 lines; 18 missing lines and the number difference are category (a))
- Items: continuation of page 8 (`p0009-b000`, `join_previous: space`), paragraph, eq. (9), "where ..." paragraph, paragraph, eq. (10), "where ..." paragraph, paragraph, "Quadruped Crate Climbing" paragraph, paragraph split across the column break (`p0009-b014` has `join_previous: space`), Table V + caption, Table VI + caption, Fig. 9 + caption, bold paragraph title "Humanoid Crate Pushing" (text, not a heading) and its paragraph.
- Tables: `table-5` (6 x 2 strings, bbox [366, 48.5, 505.2, 117]), `table-6` (8 x 2 strings, bbox [348.5, 143.7, 522.7, 230.1]).
- Figure: `figure-9` bbox [311, 314.7, 560, 467.6].
- Equations converted from formula images: (9), (10). TeX and PDF agree.
- Remaining diagnostics (a): LaTeX notation with stacked sub/superscripts; `−1` vs `-1` in the two `(j-1)` superscripts. Adjudication note written.

## Summary

### State
All 9 pages are reviewed under brief version 2 (`reviewed: true`, notes start with `[v2]`). Every page was rebuilt from the untouched extractor output (`_scratch/dial-1-9/orig/`) against the page image; the partial version-1 edits of pages 1-2 were not reused except as a cross-check.

| Page | Check result | Remaining diagnostics | Adjudication note |
| --- | --- | --- | --- |
| 1 | OK 84/84 | none | not needed |
| 2 | 102/105 | 3 missing lines (a) | yes |
| 3 | 74/104 | 30 missing lines (a), `−1`/`-1` x5 (a) | yes |
| 4 | 66/85 | 19 missing lines (a), `−1`/`-1` x5 and Algorithm 1 transcription numbers (a) | yes |
| 5 | 103/106 | 3 missing lines (a) | yes |
| 6 | OK 90/90 | none | not needed |
| 7 | 148/148 | 4 rejoined arXiv identifiers (a) | yes |
| 8 | 122/128 | 6 missing lines (a), 2 (3 for the second parser) rejoined arXiv identifiers (a) | yes |
| 9 | 83/101 | 18 missing lines (a), `−1`/`-1` x2 (a) | yes |

No category (b) item remains. For every flagged line I also ran a script that checks that each plain word of four or more letters on the line occurs in the page text; the only misses are glued symbol names (`wcorrect`, `Rcon`, `jmax`).

### Assets (all names unique in the document)
- Figures: `figure-1` (p1), `figure-2`, `figure-3` (p3), `figure-4` (p4), `figure-5` (p5), `figure-6`, `figure-7` (p6), `figure-8` (p8), `figure-9` (p9).
- Algorithm: `algorithm-1` (p4, image) with a text transcription after it.
- Tables (all as string cells): `table-1` (p5), `table-2` (p6), `table-3` (p7), `table-4` (p8), `table-5`, `table-6` (p9).
- Display equations, all as `$$` text with printed tags: unnumbered optimal-control problem (p2); (1), (2), (3a)-(3f) (p3); (4), (5), (6) (p4); (7) (p5); (8) (p8); (9), (10) (p9).
- Formulas kept as images: none.

### Joins
- Across pages (all `space`): p2 `b000`, p3 `b000`, p4 `b000`, p5 `b000`, p6 `b005`, p7 `b002`, p8 none (page 8 starts with reference [39]), p9 `b000`.
- Across column breaks or floats inside a page (all `space`): p1 `b011`, p3 `b015`, p4 `b013a`, p5 `b010`, p6 `b001`, p8 `b018`, p9 `b014`.
- Range boundaries: the range is the whole document, so no join is needed outside it.
- No item with a join follows a `$$` block (a join would put prose on the closing `$$` line); "where ..." sentences after displays are separate items.

### TeX versus PDF
- Footnote 2 (p5): PDF "can be found in A."; TeX "can be found in Appendix \ref{subsec:Hardware}". PDF kept.
- Reference [34] (p7): title starts with math-italic L and upright 1 (`{$L$}1` in `root.bbl`), written `$L$1-Adaptive`.
- Everything else, including all equations, agrees with the TeX source.

### Text repairs of substance
- Split decimals joined on pages 1, 5, 6, 8, 9; seven arXiv identifiers rejoined in the references (four on page 7, three on page 8).
- Glued line-wrap compounds restored (DIAL-MPC many times; real-world, high-dimensional, reduced-order, full-order, dual-loop, whole-body, zeroth-order, sample-hungry, diffusion-inspired, score-based, sampling-based, trajectory-level, training-free, test-time, walking-tracking, Human-to-Humanoid, Whole-Body).
- Page 3: the paragraph swallowed by the extractor's Fig. 3 "figure" restored as text. Page 4: Algorithm 1 and the "Dual-loop annealing" paragraph rebuilt. Page 9: the "where ..." paragraph after (9) rebuilt.
- Reading order rebuilt on pages 6-9 where floats sit at column tops.

### Things kept as printed that a reader may trip over
- Algorithm 1 inner loop is "for i = 1 to N", while the text and (4), (5) anneal from i = N down to 1.
- Cross-references are printed in lower-case cleveref style: "fig. 2", "section III-A", "table I", "(proposition 1)", "(algorithm 1)".
- Subsection letters repeat: A/B/C under II, A/B/C under III, A/B/C under IV, A/B under APPENDIX.
- Typos: "horizion", "convolusion", "kernal", "Quadraped", "model-base RL", "DIAL-MPC ’s", "10kg".

### Proposals for shared files (coordinator)
- `plan.json` `title`: currently "dial-mpc"; propose "Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing".
- `plan.json` `notes`, suggested entries:
  - "Source: arXiv:2409.15610v1 (9 pages). Mathematics is transcribed to LaTeX from the authors' arXiv TeX source and checked against the PDF; equation numbers are given as \tag{...}."
  - "Algorithm 1 is kept as an image and followed by a text transcription; its inner loop is printed as 'for i = 1 to N' although the text anneals from i = N down to 1."
  - "Subsection letters A, B, C repeat in Sections II, III, IV and the Appendix; cross-references are printed in lower case ('fig. 2', 'section III-A', 'table I')."
  - "Table IV has merged parent headers; they are repeated in the column names ('Walking and Tracking: DIAL-MPC', ...)."
- Navigation: because of the repeated subsection letters, headings such as `### A. Convergence and Coverage` are only unique together with their parent section.
- No asset-name clash inside this document (single reviewer).

### Limitations
- Underlining of the initials in "Diffusion-Inspired Annealing for Legged Model Predictive Control" (p1) and bold styling of table rows/abstract are not reproduced.
- Plain numbers and siunitx quantities printed in math font ("13.4", "50%", "10 cm", "24 N·m") are kept as plain text, not `$...$`; this keeps the number checks clean.
- Text inside figures (axis labels, legends, time stamps in Fig. 7) exists only in the image crops.
- The verifier cannot confirm sentence order or punctuation; order was checked by eye on overlays and previews.

### Notes on the brief
- Footnotes "at the end of that page's items" conflicts with "the page ends with the prose that continues onto the next page" (and with `join_previous`, which would attach the continuation to the footnote). On pages 1, 3 and 5 the footnotes are placed immediately before the last, continuing paragraph. A rule such as "after the paragraph that carries the marker" would be simpler.
- `join_previous` concatenates on the same line, so it should not be used on an item that follows a `$$` block; the brief could say so.
- The helper scripts of the earlier run need `pymupdf`; I ran them with `uv run --offline --with pymupdf==1.28.2` (already cached, nothing installed).
- For references, rejoining identifiers that the PDF breaks or stretches (arXiv numbers) necessarily leaves number differences, so "references should reach OK" is not attainable on pages 7-8 without keeping the damage.
