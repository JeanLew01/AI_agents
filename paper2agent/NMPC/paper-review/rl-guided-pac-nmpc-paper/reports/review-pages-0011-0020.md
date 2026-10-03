# Review report: RL-Guided PAC-NMPC, PDF pages 11-20 (brief version 2)

Reviewer range: `pages/page-0011.json` ... `page-0020.json` of `documents/s001-rl-guided-pac-nmpc`.
TeX source used: `NMPC/tex-source/rl-guided-pac-nmpc/main.tex` (private macros expanded, `\cite`/`\ref` resolved to the printed values).
Scratch: `_scratch/rlpac-11-20/v2/` (per-page scripts `pNN.py`, `finNN.py`; helper `lib.py`, `triage.py`).

Status legend: DONE = `reviewed: true`, notes start with `[v2]`, adjudication note written where `check` still reports diagnostics.

## Per-page log

### Page 11 (printed 10) - DONE
- Content: end of the Section VII introduction; `### A. Fixed-wing Dynamics and Depth Camera Sensor`; `### B. Actor Critic Training`.
- Equations as LaTeX text: (24), unnumbered `\dot{x}_t` line, (25) (two-column aligned block, new item `p0011-n001`), unnumbered `\Omega(\omega)` matrix, (26)-(31). No formula images kept.
- Figures: `figure-8` (aircraft photo), `figure-9` (2x3 histograms); captions separate.
- Joins: first item `join_previous: space` (continues page 10, owned by the other reviewer); last item continues on page 12.
- check: 40/87 lines; all 47 unmatched lines are mathematics (category a). Number differences: `J^{-1}`, `-1/2` (category a). Adjudication note written.

### Page 12 (printed 11) - DONE
- Content: end of VII-B; `### C. Sensor Prediction`; `### D. Simulation Experiments`; run-in `**1) Controller Configuration:**`.
- Equations as LaTeX text: (32) (aligned, three lines). No formula images kept.
- Figure: `figure-10` (five panels with sub-captions (a)-(e) inside the crop; sub-caption line repeated in the caption item).
- Table: `table-5` (TABLE V, 7x5, header cells `$\delta_1$` ... `$\delta_3$`); caption with LaTeX.
- Joins: first item `space` (continues page 11); `p0012-b018` `space` (paragraph split by column break around Table V); last item continues on page 13.
- check: 101/116 lines, no number differences; 15 unmatched lines are mathematics (category a). Adjudication note written.

### Page 13 (printed 12) - DONE
- Content: rest of `1) Controller Configuration`; run-ins `**2) Environments:**`, `**3) Baseline Comparison:**`.
- Equations as LaTeX text: (33) (six lines), (34) (five lines), both aligned with `\tag`. No formula images kept.
- Figure: `figure-11`. Table: `table-6` (TABLE VI, 4 columns: header `Approach` repeated over its two columns, multirow label `PAC-NMPC` repeated on its five rows, `RL Actor Network` with empty second cell; bold of 468.1 and 90% not kept in cells).
- Joins: first item `space` (continues page 12); `p0013-b009` `space` (column break around Table VI); last item continues on page 14.
- Source typo kept: "using the the widely adopted".
- check: 88/114 lines, no number differences; 26 unmatched lines are mathematics (category a). Adjudication note written.

### Page 14 (printed 13) - DONE
- Content: end of `3) Baseline Comparison`; run-ins `**4) Ablation Study:**`, `**5) Out of Distribution Experiment:**`; `### E. Hardware Experiments`.
- No display equations. Figure: `figure-12`. Tables: `table-7` (TABLE VII; check marks transcribed as `✓`/empty from the crop), `table-8` (TABLE VIII; same two-column `Approach` convention as `table-6`; bold of 481.8 and both 76% not kept in cells).
- Joins: first item `space` (continues page 13); `p0014-b012` `space` (column break around Table VIII); last item continues on page 15.
- Printed cross-reference "Section VII-B" (for the sensor-prediction study, which is subsection C) kept as printed.
- check: 106/109 lines, no number differences; 3 unmatched lines differ only by `\mathrm{m}` unit markup (category a). Adjudication note written.

### Page 15 (printed 14) - DONE
- Content: rest of VII-E Hardware Experiments (prose only, no headings on this page).
- Figures: `figure-13` (two photos merged), `figure-14`, `figure-15` (two panels merged), `figure-16`; captions separate, Fig. 15 caption with `$\mathcal{C}^+_{\alpha}$`.
- Table: `table-9` (TABLE IX; was extracted as a picture; same two-column `Approach` convention as `table-6`; bold of 80% and 252.2 not kept in cells).
- Order rebuilt so floats sit between complete paragraphs. Joins: first item `space` (continues page 14); `p0015-b015` `space` (column break); last item continues on page 16.
- check: 60/66 lines, no number differences; 6 unmatched lines are inline maths (category a). Adjudication note written.

### Page 16 (printed 15) - DONE
- Content: end of VII-E; `## VIII. ANALYSIS`; `### A. One-Step Feasible Descent`; `### B. Multi-Step Feasible Descent` (start).
- Theorem-like blocks: `**Lemma VIII.1.**`, `**Lemma VIII.2.**`, `**Theorem VIII.1.**`, three `**Proof.**` blocks ending with `$\square$`.
- Equations as LaTeX text: (35)-(46), one `$$` block per printed number; (38) is a three-line aligned block (number printed on its first line). All 13 extractor formula images replaced; none kept.
- Item list rebuilt in reading order (extractor had interleaved the columns); new items `p0016-n001` ... `p0016-n004`.
- Joins: first item `space` (continues page 15); last item continues on page 17.
- Kept as printed: proof of Theorem VIII.1 ends "... < 0," (comma) before the QED box; upright "k" in "for every k in the sequence".
- check: 39/126 lines; 87 unmatched lines are mathematics (category a); number difference `7` is the `\mapsto` glyph artefact (category a). Adjudication note written.

### Page 17 (printed 16) - DONE
- Content: rest of VIII-B; `### C. Approximate Value Functions`; `### D. Simulation Experiment`; `## IX. CONCLUSION` (start).
- Theorem-like blocks: `**Definition VIII.1 (Multi-Step Feedback Dynamics).**`, `**Definition VIII.2 (Multi-Step Feedback Cost).**` (new item `p0017-n001`), `**Theorem VIII.2.**`, `**Proof.**` ending with `$\square$`.
- Equations as LaTeX text: (47)-(52). All 7 extractor formula images replaced; none kept.
- Joins: first item `space` (continues page 16, previous item is prose); `p0017-b016` `space` (column break inside the first paragraph of VIII-C); last item continues on page 18.
- Kept as printed: unsubscripted `x` in `p(x_{t+N_T} | x, ξ)`; `N` versus `N_T` in (47); "Equation 11"; "definition VIII.2".
- check: 62/110 lines; 48 unmatched lines are mathematics (category a); number differences are Unicode/ASCII minus in `N_T-1` (category a). Adjudication note written.

### Page 18 (printed 17) - DONE
- Content: end of `## IX. CONCLUSION`; `## REFERENCES`, entries [1]-[29] (one text item per entry, `[n] ...`, italics as `*...*`).
- Figures: `figure-17`, `figure-18` (side-by-side float; the fused caption item was split into two captions, new item `p0018-n001`).
- Joins: first item `space` (continues page 17). The last item is reference [29]; page 19 starts with [30] (no join).
- References rebuilt from native lines; line-end hyphens decided against `references.bib` (kept: "Perception-aware" [5], "Constraint-informed" [23]); "real- time" in [18] kept as printed.
- check: 121/122 lines, no number differences; the one unmatched line is the caron of "Klaučo" stored as modifier letter U+02C7 in the PDF text layer (category a). Adjudication note written.

### Page 19 (printed 18) - DONE
- Content: bibliography entries [30]-[76] only (left column [30]-[51], right column [52]-[76]); one text item per entry (`p0019-r030` ... `p0019-r076`), italics as `*...*`.
- Rebuilt from native lines; the extractor had fused several entries per list item. Line-end hyphens decided against `references.bib` (kept: "model-based" [36], "fixed-wing" [54], [62], "Comput.-Assist." [76]).
- No joins. check: OK, 163/163 lines, no number differences. No adjudication note needed.

### Page 20 (printed 19) - DONE
- Content: bibliography entries [77], [78]; rest of the page is blank. No author biographies or photos exist in this PDF.
- No joins. check: OK, 6/6 lines, no number differences. No adjudication note needed.

## Summary

| PDF page | State | Figures | Tables | Display equations (LaTeX text) | check | Adjudication note |
| --- | --- | --- | --- | --- | --- | --- |
| 11 | reviewed, `[v2]` | figure-8, figure-9 | - | (24)-(31), two unnumbered | 40/87, maths only | yes (3 keys) |
| 12 | reviewed, `[v2]` | figure-10 | table-5 | (32) | 101/116, maths only | yes (missing_lines) |
| 13 | reviewed, `[v2]` | figure-11 | table-6 | (33), (34) | 88/114, maths only | yes (missing_lines) |
| 14 | reviewed, `[v2]` | figure-12 | table-7, table-8 | - | 106/109, unit markup only | yes (missing_lines) |
| 15 | reviewed, `[v2]` | figure-13 ... figure-16 | table-9 | - | 60/66, maths only | yes (missing_lines) |
| 16 | reviewed, `[v2]` | - | - | (35)-(46) | 39/126, maths only | yes (3 keys) |
| 17 | reviewed, `[v2]` | - | - | (47)-(52) | 62/110, maths only | yes (3 keys) |
| 18 | reviewed, `[v2]` | figure-17, figure-18 | - | - | 121/122, one diacritic artefact | yes (missing_lines) |
| 19 | reviewed, `[v2]` | - | - | - | OK 163/163 | none needed |
| 20 | reviewed, `[v2]` | - | - | - | OK 6/6 | none needed |

All ten pages are finished; nothing is left unmarked. No algorithm boxes occur in this range.

## Joins

- Range start: `p0011-b001` has `join_previous: space` and continues the last item of page 10 (`p0010-b018`, "... learned sensor prediction", owned by the other reviewer). This relies on page 10 ending with that text item, which is its current state.
- Page-to-page joins inside the range (first item of the page, all `space`): 12, 13, 14, 15, 16, 17, 18. In every case the preceding item is prose, never a `$$` block.
- Column-break joins inside pages (`space`): `p0012-b018`, `p0013-b009`, `p0014-b012`, `p0015-b015`, `p0017-b016`.
- No `join_previous` follows a display-equation item. No `none` joins were needed (no word is split across a page or float).
- Range end: page 20 is the last page of the document.

## Mathematics

- Every display equation of the range, (24)-(52) plus the two unnumbered displays on page 11, is a `text` item with a `$$ ... $$` block and `\tag`; multi-line groups with one printed number are `aligned` blocks ((25), (32), (33), (34), (38)); groups with several printed numbers are one block per number ((39)-(41), (43)-(44), (47)-(48)).
- **No formula is kept as an image.** All earlier `equation-NN` / `formula-p00NN-k` assets of the version-1 run and of the extractor are gone.
- Source of the LaTeX: the authors' `main.tex`, with the private macros expanded to standard LaTeX and `\cite`/`\ref` replaced by the printed numbers. Each formula was compared with 200-dpi crops.
- **TeX-versus-PDF disagreements: none found** on pages 11-20.
- Authors' irregularities transcribed as printed (also listed in the page notes): last row of the `\Omega(\omega)` matrix on page 11; mixed `\mathbf{v_b}`/`\mathbf{v}_b` and `||`/`\|` on page 11; "Section VII-B" cross-reference on page 14; proof of Theorem VIII.1 ending with a comma; unsubscripted `x` in Definition VIII.1; `N` versus `N_T` in (47); index ranges `{t, ..., t+N_T}` versus `{t,...,t+N_T-1}` in Theorem VIII.2; "Equation 11" without parentheses; "using the the widely adopted" on page 13; "real- time" in reference [18].

## Text repairs of substance

- Pages 15-18: reading order rebuilt (the extractor interleaved columns and placed floats inside sentences); compound hyphens lost at line breaks restored ("PAC-NMPC", "high-dimensional", "real-time", "long-range", "actor-critic").
- Page 15: Table IX converted from a picture with "picture text" into a real table; Figs. 13 and 15 merged from two picture items each.
- Page 16: heading "VIII. ANALYSIS" was plain text; Lemma VIII.1/VIII.2, Theorem VIII.1 and their proofs rebuilt from garbled sub/superscript runs.
- Page 17: Definitions VIII.1 and VIII.2 separated; Theorem VIII.2 and its proof rebuilt.
- Page 18: fused captions of Fig. 17 and Fig. 18 separated.
- Pages 18-20: bibliography rebuilt entry by entry (78 entries in the paper, [1]-[29] on page 18, [30]-[76] on page 19, [77]-[78] on page 20).
- Tables VI, VIII, IX use the same merged-cell convention as the other reviewer's Tables II and III (header `Approach` repeated, multirow label repeated on each row); the version-1 single-column form `PAC-NMPC: <variant>` was replaced.

## Remaining diagnostics by page

| Page | missing lines | number differences | second parser | Category |
| --- | --- | --- | --- | --- |
| 11 | 47 | `−1` x2 versus `-1`, `1` | `−1` versus `-1` | (a) LaTeX maths; Unicode/ASCII minus |
| 12 | 15 | - | - | (a) LaTeX maths |
| 13 | 26 | - | - | (a) LaTeX maths |
| 14 | 3 | - | - | (a) `\mathrm{m}` unit markup |
| 15 | 6 | - | - | (a) LaTeX maths |
| 16 | 87 | `7` | `7`, extra `36` | (a) LaTeX maths; `\mapsto` glyph extracted as `7→`; `[...](36)` read as a Markdown link by the verifier |
| 17 | 48 | `−1` x7, `1` versus `-1` x8 | same | (a) LaTeX maths; Unicode/ASCII minus in `N_T-1` |
| 18 | 1 | - | - | (a) caron of "Klaučo" stored as U+02C7, which the verifier counts as alphanumeric |
| 19, 20 | 0 | - | - | OK |

Nothing of category (b) remains.

## Proposals for shared files (coordinator)

- `plan.json` `title` is still the slug `rl-guided-pac-nmpc`; the full title is "RL-Guided PAC-NMPC for Probabilistically-Safe Perception-Based Navigation in Unknown Environments".
- Suggested `notes` entries: (1) Tables II, III, VI, VIII, IX have a two-column "Approach" header and a multirow label "PAC-NMPC"; in the CSV the header and the label are repeated. (2) Bold marking of best values in Tables VI-IX is not represented in the CSV; it is recorded in the page notes. (3) Table VII's check marks are vector drawings transcribed as "✓". (4) The PDF has no author biographies. (5) The bibliography was rebuilt from the PDF text because the arXiv source has no `.bbl`.
- Navigation headings in this range: `## VIII. ANALYSIS`, `## IX. CONCLUSION`, `## REFERENCES`; subsections `### A.`-`### E.` of Section VII (A, B on page 11; C, D on page 12; E on page 14) and `### A.`-`### D.` of Section VIII (A, B on page 16; C, D on page 17). The subsection letters repeat between Sections VI, VII and VIII, so a navigation index should qualify them with the section.
- Asset names in this range: `figure-8` ... `figure-18`, `table-5` ... `table-9`. No clash with pages 1-10 (`figure-1` ... `figure-7`, `table-1` ... `table-4`, `algorithm-1`) at the time of writing.
- Verifier: `[...](36)`-shaped equation text is dropped by the Markdown stripping on the source side (page 16), and the modifier letter U+02C7 counts as alphanumeric (page 18). Both produce false diagnostics that cannot be removed from the page side without corrupting the text.

## Limitations

- Statements of lemmas, theorems and definitions are italic in print; they are stored as plain text with LaTeX maths and a bold label. The end-of-proof box is written `$\square$`.
- Run-in subsubsection titles ("1) Controller Configuration:" ... "5) Out of Distribution Experiment:") are italic in print and bold in the text items, as the brief prescribes.
- Table header cells with mathematics use LaTeX (`$\delta_1$`), so the CSV contains `$` and backslashes.
- Italics in the bibliography were carried over from the extractor's markup and checked visually against the crops; other typographic detail of the bibliography (small caps, spacing) is not represented.
- "A*" is written with a bare asterisk in prose and table cells; none of the occurrences can open Markdown emphasis (each is followed by a space), but a renderer that treats `*` loosely could misread it.
- Fig. 16's last x tick label is cut to "2" in the printed figure itself.

## Remarks on the brief

- The brief asks for bold run-in titles while the paper prints them in italics; followed the brief.
- "Pure-prose pages should reach OK" is not attainable on page 18 because of the U+02C7 artefact described above.
- The brief does not say how to represent multirow/multicolumn table labels beyond "repeat the parent header"; I aligned with the convention already used on pages 9-10 of this paper.
- A `check` over ten pages and the per-page triage are cheap; the costly part was that a formula image's own text lines stop being excluded once it becomes a `text` item, so a maths-heavy page shows 50-90 "missing line" entries that all have to be read. A closest-match listing per missing line (script `triage.py` in the scratch directory) made this tractable and may be useful to other reviewers.
- The assignment expected author biographies on the last pages; this PDF has none.
- The session was interrupted once (machine restart) between pages 16 and 17; pages 11-16 were already on disk with `[v2]`, page 17 had been written but not marked and was re-checked before marking.
