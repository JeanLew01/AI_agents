# Review report: RL-Guided PAC-NMPC, PDF pages 1-10 (brief version 2)

Document: `rl-guided-pac-nmpc-paper/documents/s001-rl-guided-pac-nmpc`
TeX source used: `NMPC/tex-source/rl-guided-pac-nmpc/main.tex`
Status: **complete**. All ten pages are saved with `reviewed: true` and `review_notes` starting with `[v2]`; `check` was re-run once per page after the last edit (results in the table below). The run was interrupted once by a machine restart; nothing was lost (every page had been written to disk when finished).

## Per-page log

### Page 1 - finished [v2]
- Content: IEEE copyright notice only (kept as text, compared with image and TeX). Rotated arXiv stamp omitted (resolves the extraction warning on `p0001-b000`).
- No figures, tables, equations. check: OK (4/4). No adjudication note needed.

### Page 2 - finished [v2]
- Title (`# `), author line with `$^{1,2}$` markers, `Footnote 1: ...` and `Footnote 2: ...` (affiliations) and the unnumbered `Email: ...` line directly after the author line (author/affiliation footnotes; the page still ends with the paragraph that continues on page 3), `**Abstract—**`, `**Index Terms—**`, `## I. INTRODUCTION`.
- Figure 1 -> `figure-1` (box checked with crop and ink measurement), caption `Fig. 1: ...`.
- v2 changes: `<sup>` author markers -> LaTeX superscripts; abstract/index-terms body bold dropped (run-in label bold kept).
- Joins: column break inside paragraph 2 of the Introduction (`p0002-b012` join space). Last item continues on page 3.
- check: OK (90/90). No adjudication note needed.

### Page 3 - finished [v2]
- Text only (end of Section I with contribution list 1)-4), `## II. RELATED WORK`, `### A. Safe RL`, `### B. Learned NMPC Warm-start`). No mathematics.
- Joins: first item joins page 2 (space); `p0003-b012` join none ("ex-pected" split by the column break). Last item continues on page 4.
- "runtime" (Section II-B, printed "run-/time" at a line break) confirmed by the TeX source.
- check: OK (113/113). No adjudication note needed.

### Page 4 - finished [v2]
- `### C. NMPC with Learned Waypoints`, `### D. NMPC & RL Hybrids`, `### E. Vision-based Agile Fixed-Wing Flight`.
- Table I -> `table-1` (9 x 6 string cells, checked against 200-dpi crop and TeX tabular), table footnote `Footnote *: DiffStack ...`, caption `TABLE I: ...`; float placed after the paragraph citing Table I.
- Joins: first item joins page 3 (space); `p0004-b012` join space (sentence broken by the column change, table in between). Last item continues on page 5.
- 'AC-MPC[46]' (table) versus 'Actor Critic MPC [45]' (prose) is as printed: two different bib keys in the TeX source.
- check: OK (122/122). No adjudication note needed.

### Page 5 - finished [v2]
- `## III. PROBLEM FORMULATION`, `## IV. BACKGROUND`, `### A. PAC-NMPC`. Definitions III.1-III.6, IV.1, IV.2 with bold printed labels.
- Display equations now LaTeX text items: unnumbered inequality of Definition III.6 (`p0005-b016b`), Equation (1) (`p0005-b024`, `\tag{1}`), Equation (2) (`p0005-b027`, `\tag{2}`). Former assets `formula-p0005-1`, `equation-1`, `equation-2` no longer exist.
- All inline maths converted from `<sub>`/Unicode to LaTeX with macros expanded; no TeX/PDF disagreement.
- Joins: first item joins page 4 (space); `p0005-b015` join space (Definition III.5 across the column break; "c :" moved to the later item to keep the formula whole). Last item continues on page 6.
- check: 70/108, category (a) only: 38 maths lines; numbers: `7` x5 (PDF `\mapsto` glyph extracted as "7→"), `−1`/`-1` x3 (Unicode minus vs LaTeX). Adjudication note written.

### Page 6 - finished [v2]
- `### B. Actor-Critic RL`, `## V. ACTOR-CRITIC PAC-NMPC (AC-PAC-NMPC)`; Definitions IV.3, IV.4.
- Equations (3)-(12) are LaTeX text items (`p0006-b002` (3, aligned with the two s.t. lines), `-b005` (4), `-b008` (5), `-b008a` (6), `-b008b` (7), `-b010` (8), `-b010a` (9), `-b013` (10), `-b017` (11), `-b020` (12)). No formula images remain; assets `equation-3` ... `equation-12` no longer exist.
- Printed peculiarities kept: unbalanced "(" in the exponent of Equation (8); `...` in (9).
- Joins: first item joins page 5 (space); `p0006-b015` join space (column break). Page ends with a complete paragraph.
- check: 57/104, category (a) only: 47 maths lines; numbers `−1`/`-1` x7, `7` x2 (`\mapsto`). Adjudication note written.

### Page 7 - finished [v2]
- Figure 2 -> `figure-2` (box tightened to [47,56,302,238]; caption `Fig. 2: ...` now kind caption).
- Algorithm 1 -> image `algorithm-1` (`p0007-b009`, box [310,53.5,565,185.5]) plus LaTeX transcription (`p0007-b010`), placed at the end of subsection V-A.
- `### A. RL-based Warm Start`, `### B. Uncertainty-Aware RL-Augmented Cost` (were `# _..._`).
- Equations (13), (14) are LaTeX text items (`p0007-b014`, `p0007-b017`). Restored a paragraph that the extractor had hidden inside the formula box of (14): new item `p0007-b017a` ("To model the stochastic value function, ...").
- Text repairs: "PACNMPC" -> "PAC-NMPC", "outof-distribution" -> "out-of-distribution"; all inline maths to LaTeX.
- Joins: `p0007-b011` join space (sentence broken by the column change; algorithm box in between). Last item continues on page 8.
- check: 69/86, category (a) only: 17 maths lines; numbers: only "extra" tokens from the Algorithm 1 transcription (source lines are inside the excluded image box). Adjudication note written.

### Page 8 - finished [v2]
- `### C. Uncertainty-Aware Value Function Improvement Constraint` (was plain text), `## VI. RALLY CAR UGV WITH LIDAR: APPROACH AND EVALUATION`, `### A. Rally Car Dynamics and LiDAR Sensor`, `### B. Actor-Critic`.
- Equations (15)-(19) are LaTeX text items (`p0008-b006`, `-b008`, `-b011` (17, aligned with two s.t. lines), `-b022`, `-b026`).
- Figure 3 -> `figure-3`, Figure 4 -> `figure-4` (two separate side-by-side figures; interleaved caption split into two caption items, new `p0008-b017b`). Both placed after the Section VI opening paragraph.
- Text repairs: "multiheaded" -> "multi-headed", "AC-PACNMPC" -> "AC-PAC-NMPC", "costto-go" -> "cost-to-go", fused words around inline maths rebuilt; LiDAR paragraph split off (`p0008-b023b`).
- Joins: first item joins page 7 (space); `p0008-b018` join space (column change with figures in between). Page ends with a complete paragraph.
- check: 76/109, category (a) only: 33 maths lines; numbers: e-notation exponents (`4e−4` etc. written as typeset `4\mathrm{e}^{-4}`), Unicode minus. Adjudication note written.

### Page 9 - finished [v2]
- `### C. Sensor Prediction`, `### D. Simulation Experiments`; run-in `**1) Cluttered Environments:**` kept inside its paragraph.
- Equations (20)-(23) are LaTeX text items (`p0009-b005`, `-b007`, `-b008`, `-b010`).
- Table II -> `table-2` (6 x 5 strings rebuilt from crop and TeX; merged "Approach" header repeated, multirow "PAC-NMPC" repeated; bold best values listed in the page notes), caption `TABLE II: ...`.
- Figure 5 -> `figure-5` (box tightened to [310,143.5,565,276.5]), caption `Fig. 5: ...`. Both floats placed at the end of the page after the paragraph that cites them.
- Text repairs: "twodimensional" -> "two-dimensional", "i-913900H" -> "i-9-13900H", inline maths to LaTeX.
- Joins: `p0009-b019` join space (stage-cost paragraph across the column change; "Q =" moved to keep the formula whole). Page starts and ends with complete paragraphs.
- check: 77/107, category (a) only: 30 maths lines (two are table cells with LaTeX); numbers: `i-9-13900H` hyphenation, `1e−2` exponents, Unicode minus. Adjudication note written.

### Page 10 - finished [v2]
- Figure 6 -> `figure-6`, Figure 7 -> `figure-7` (boxes tightened to exclude captions); Table III -> `table-3` (6 x 5 strings); Table IV -> `table-4` (was misclassified as a picture; now 5 x 4 strings). Captions verbatim.
- `### E. Hardware experiments`, `## VII. FIXED-WING UAV WITH DEPTH CAMERA: APPROACH AND EVALUATION`; run-in `**2) Concave Trap Environments:**` kept inside its paragraph.
- Floats moved after the paragraphs that cite them; `p0010-b012` join space (paragraph broken by the column change).
- Text repairs: `$\pm\frac{\pi}{2}$ radians. 100 environments` rebuilt, "AC-PACNMPC" -> "AC-PAC-NMPC", "wingspan" -> "wing-span" (TeX), `1/10$^{\text{th}}$`, `$0.5 \mathrm{m}$`.
- Last item continues on page 11 (its first item already has join space).
- check: 85/92, no number differences; 7 missing lines are category (a) (four table cells with LaTeX `V`, three prose lines with inline maths). Adjudication note written.

## Summary

### Pages covered and final state

| PDF page | Printed page | State | check (lines found) | Remaining diagnostics | Adjudication note |
| --- | --- | --- | --- | --- | --- |
| 1 | (copyright page) | finished [v2] | OK 4/4 | none | not needed |
| 2 | 1 | finished [v2] | OK 90/90 | none | not needed |
| 3 | 2 | finished [v2] | OK 113/113 | none | not needed |
| 4 | 3 | finished [v2] | OK 122/122 | none | not needed |
| 5 | 4 | finished [v2] | 70/108 | 38 maths lines; numbers `7` x5 (`\mapsto` glyph), `−1` x3 | written (3 keys) |
| 6 | 5 | finished [v2] | 57/104 | 47 maths lines; numbers `−1` x7, `7` x2 | written (3 keys) |
| 7 | 6 | finished [v2] | 69/86 | 17 maths lines; only "extra" numbers from the Algorithm 1 transcription | written (3 keys) |
| 8 | 7 | finished [v2] | 76/109 | 33 maths lines; numbers: e-notation exponents, Unicode minus | written (3 keys) |
| 9 | 8 | finished [v2] | 77/107 | 30 maths lines; numbers: `i-9-13900H`, `1e−2`, `−1` | written (3 keys) |
| 10 | 9 | finished [v2] | 85/92 | 7 maths lines; no number differences | written (`missing_lines` only) |

Every remaining diagnostic is category (a) (LaTeX notation versus the PDF's glyph text, equation tags, sub/superscript
digits, table cells containing LaTeX, or the algorithm transcription whose source lines lie inside the excluded image box).
No category (b) item remains. Each line listed by `check` was compared with a 190-260 dpi crop and with the TeX source.

### Assets (pages 1-10)

| Asset | Kind | Page / item | Label |
| --- | --- | --- | --- |
| `figure-1` | figure | 2 / `p0002-b010` | Figure 1 |
| `table-1` | table (9 x 6) | 4 / `p0004-b009` | Table I |
| `figure-2` | figure | 7 / `p0007-b001` | Figure 2 |
| `algorithm-1` | figure (algorithm image) + transcription `p0007-b010` | 7 / `p0007-b009` | Algorithm 1 |
| `figure-3`, `figure-4` | figures | 8 / `p0008-b015`, `p0008-b016` | Figure 3, Figure 4 |
| `table-2` | table (6 x 5) | 9 / `p0009-b015` | Table II |
| `figure-5` | figure | 9 / `p0009-b017` | Figure 5 |
| `figure-6`, `figure-7` | figures | 10 / `p0010-b001`, `p0010-b008` | Figure 6, Figure 7 |
| `table-3` | table (6 x 5) | 10 / `p0010-b003` | Table III |
| `table-4` | table (5 x 4) | 10 / `p0010-b010` | Table IV |

No asset name of pages 1-10 clashes with pages 11-20 (checked against all 20 page files: the other range uses
`figure-8` ... `figure-16`, `table-5` ... `table-9`, and page-numbered names). No unnumbered asset was needed in my range.

Display equations as LaTeX text items (24 blocks): the unnumbered inequality of Definition III.6 and Equations (1), (2)
on page 5; (3)-(12) on page 6; (13), (14) on page 7; (15)-(19) on page 8; (20)-(23) on page 9. All 213 maths segments of
pages 1-10 (inline, display, table cells) were compiled with pdflatex (amsmath, amssymb) without error, and the rendered
display equations were compared visually with the page.

**Formulas kept as images: none.**

### Joins

- Inside pages (column breaks): `p0002-b012`, `p0004-b012`, `p0005-b015`, `p0006-b015`, `p0007-b011`, `p0008-b018`,
  `p0009-b019`, `p0010-b012` (all `space`); `p0003-b012` (`none`, word "ex-pected").
- Across pages: first items of pages 3, 4, 5, 6, 8 (`space`). Pages 7, 9 and 10 start with a new paragraph.
- Range boundary: the last item of page 10 (`p0010-b018`, "... learned sensor prediction") continues on page 11; the
  other reviewer's `p0011-b001` already has `join_previous: "space"`. Nothing is needed before page 1.
- No item with `join_previous` follows a `$$` block; "where ..." clauses after display equations are separate items.
- Two printed column splits fell inside a formula ("given as c :" / domain on page 5; "where Q =" / "diag(...)" on
  page 9). In both cases the one or two symbols before the break were moved to the later item so that the formula is a
  single `$...$`; this is recorded in the page notes.

### TeX-versus-PDF disagreements

None in content. The TeX source helped to resolve line-end hyphens ("runtime", "multi-headed", "out-of-distribution",
"wing-span", "i-9-13900H", "AC-PAC-NMPC"). Spacing hacks (`\!`, `\hspace`) were dropped and private macros expanded.
`\mathcal{C_V}^+_\alpha` is written `{\mathcal{C}_{\mathcal{V}}}^+_\alpha` (same glyphs, robust in MathJax/KaTeX).

### Peculiarities of the source kept as printed (not corrected)

- Equation (8): unbalanced extra "(" in the exponent, `D_2(p(\cdot|\nu)||(p(\cdot|\nu_i))`.
- Equation (21): bracket opens before `\mathbf{o}^j`, unlike Equation (22).
- Equations (16), (17): "s.t." printed inside the display; (17) has a period after the first constraint and a comma after the second.
- Equation (3) minimises over `\alpha` without the condition `\alpha>0` that Equation (17) has.
- Page 5: nominal dynamics `f` is not bold in the TVLQR paragraph (bold `\mathbf{f}` later).
- Page 8: acceleration limit printed `[-1., 1]`; covariance and weights printed in e-notation with a superscript exponent
  (`4\mathrm{e}^{-4}`, `1\mathrm{e}^{-2}`); `diag` italic; "larger states spaces".
- Page 9: `360$^o$` with a letter o (page 8 has a degree sign); `\boldsymbol{\pi}^{\phi}(\mathbf{x})` with a non-bold phi.
- Page 4: table cites "AC-MPC[46]", prose cites "Actor Critic MPC [45]" (two different bibliography keys in the TeX source).
- Page 10: the trap-environment paragraph ends "An example environment is shown in Figure 5." (as printed).
- Algorithm 1 tests the constraint on the measured history `\mathbf{y}_{(t-N_y):t}`, not on the predicted measurement.

### Text repairs of substance

- Page 7: a whole paragraph ("To model the stochastic value function, we implement ... Monte Carlo (MC) dropout:") was
  hidden inside the extractor's formula box for Equation (14); restored as `p0007-b017a`.
- Page 8: interleaved captions of Figures 3 and 4 separated; fused words around inline maths rebuilt; LiDAR paragraph split off.
- Page 10: Table IV was a picture with scattered text, now a table; "± π/2 radians. 100 environments" rebuilt.
- Pages 9, 10: Tables II and III had split header/row labels ("Ap|proach", "RL Ac|tor Network"); rebuilt.
- Pages 7-10: headings were `# _..._` or plain text; now `## ` / `### ` with printed numbering.
- Lost compound hyphens restored (list in the per-page log).

## Proposals for shared files (coordinator)

1. `plan.json` `title` is currently the file stem `rl-guided-pac-nmpc`. Proposed: "RL-Guided PAC-NMPC for
   Probabilistically-Safe Perception-Based Navigation in Unknown Environments".
2. `plan.json` `notes`, proposed entries:
   - "Source: arXiv:2609.39854v1 [cs.RO], 30 Sep 2026 (identifier taken from the rotated margin stamp on PDF page 1, which is omitted from the text). Authors: Adam Polevoy, Dillon Capalongo, Katherine Tang, Mark Gonzales, Marin Kobilarov, Joseph Moore."
   - "PDF page 1 is an IEEE copyright page; the paper's printed page numbers are the PDF page numbers minus one."
   - "Mathematics was transcribed to LaTeX from the authors' TeX source and checked against the PDF; the authors' macros were expanded. Printed peculiarities (for example the unbalanced parenthesis in Equation (8)) are reproduced, not corrected."
   - "Tables II, III and IV print the best value of each column in bold; CSV cells cannot carry bold. Bold cells: Table II - Stuck 3% (RL Actor Network), Violation 0% (PAC-NMPC, Quad. Term. Cost), Success 97%, Stuck 3%, Violation 0% (PAC-NMPC, Learned V). Table III - Stuck 2% (RL Actor Network), Violation 0% (PAC-NMPC, Quad. Term. Cost), Success 93% and Violation 0% (PAC-NMPC, Learned V). Table IV - Stuck 0% (Actor Policy), Success 95% and Violation 0% (PAC-NMPC w/ Learned V), Stuck 0% (Actor Policy w/ Mismatch), Violation 0% (PAC-NMPC w/ Learned V w/ Mismatch)."
   - "In Tables II and III the header 'Approach' spans two columns (repeated in both header cells) and the label 'PAC-NMPC' spans three rows (repeated on each)."
   - "Algorithm 1 is kept as an image (figure asset algorithm-1) followed by a line-by-line transcription."
   - "Figure 2 writes the learned models with subscripts (h_eta, pi_phi, Q_psi); the text uses superscripts (h^eta, pi^phi, Q^psi). This is the authors' notation in both places."
3. Navigation headings for pages 1-10 (all present as heading items, printed numbering kept):
   `# RL-Guided PAC-NMPC ...` (p2); `## I. INTRODUCTION` (p2); `## II. RELATED WORK` (p3) with `### A. Safe RL`,
   `### B. Learned NMPC Warm-start` (p3), `### C. NMPC with Learned Waypoints`, `### D. NMPC & RL Hybrids`,
   `### E. Vision-based Agile Fixed-Wing Flight` (p4); `## III. PROBLEM FORMULATION` (p5); `## IV. BACKGROUND` (p5) with
   `### A. PAC-NMPC` (p5), `### B. Actor-Critic RL` (p6); `## V. ACTOR-CRITIC PAC-NMPC (AC-PAC-NMPC)` (p6) with
   `### A. RL-based Warm Start`, `### B. Uncertainty-Aware RL-Augmented Cost` (p7),
   `### C. Uncertainty-Aware Value Function Improvement Constraint` (p8);
   `## VI. RALLY CAR UGV WITH LIDAR: APPROACH AND EVALUATION` (p8) with `### A. Rally Car Dynamics and LiDAR Sensor`,
   `### B. Actor-Critic` (p8), `### C. Sensor Prediction`, `### D. Simulation Experiments` (p9),
   `### E. Hardware experiments` (p10); `## VII. FIXED-WING UAV WITH DEPTH CAMERA: APPROACH AND EVALUATION` (p10).
   Subsection letters restart in every section (A, B, ... occur in II, IV, V, VI, VII), so a navigation index should
   qualify them with the section number (for example "VI-B Actor-Critic" versus "IV-B Actor-Critic RL").
   The two IEEE run-in subsubsection titles "1) Cluttered Environments:" (p9) and "2) Concave Trap Environments:" (p10)
   are `\subsubsection`s in the TeX source but printed run-in; following the brief they are bold run-ins inside their
   paragraphs, not `#### ` headings (the pages 11-20 reviewer did the same for 1)-5) in Section VII). If the coordinator
   wants them in the navigation, they can be promoted to `#### ` in one step for both ranges.
4. Asset names: no clash. Old asset names from the interrupted version-1 pass (`equation-1` ... `equation-12`,
   `formula-p0005-1`, `figure-p0007-001`, `formula-p0007-014`, ..., `table-p0009-015`, `figure-p0010-010`) no longer
   exist in pages 1-10; any stale files of that kind in a previous build can be discarded.
5. The definition labels are written `**Definition III.1 (Stochastic Dynamics).**` (number and name inside the bold
   label), the same form the pages 11-20 reviewer uses for Definitions VIII.1/VIII.2.

## Limitations

- Bold type in Tables II-IV is not represented in the CSV cells (listed above and in the page notes).
- Body italics of definitions and the bold face of the abstract were dropped; wording is verbatim.
- Figure-internal text (Figure 2 block labels, Figure 5 legend and axis labels, Figure 6 axes/legend) is available
  only inside the images; it was read from 250-260 dpi crops and described in the page notes, not transcribed as text.
- Reference entries are outside my range (pages 1-10 contain no bibliography).

## Notes on the brief

- "Run one tool command at a time" and the `check DOC PAGE [PAGE ...]` syntax: I ran `check` for several pages in one
  call early on and once per page at the end; both give the same per-page result.
- Table footnotes: the brief says "Caption and footnotes are separate items" but not how to mark them. For Table I,
  I used the page-footnote form with the printed marker (`Footnote *: ...`), placed directly under the table.
- The number check tokenises `x_{i+1}` as "+1" and e-notation with superscripts as separate tokens, so pages with an
  algorithm transcription or typeset e-notation always show number differences; this cannot be avoided without
  changing the mathematics.
- The PDF's `\mapsto` glyph is extracted as "7→" by both parsers, which produces a spurious missing digit 7 on pages 5 and 6.
- For compound hyphens at line ends the TeX source was the only reliable arbiter; without it "runtime", "wing-span" and
  "i-9-13900H" would have stayed ambiguous.

