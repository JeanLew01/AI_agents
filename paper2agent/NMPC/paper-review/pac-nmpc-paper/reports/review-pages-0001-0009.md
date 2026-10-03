# Review report: PAC-NMPC (s001-pac-nmpc), PDF pages 1-9

Reviewer range: pages 1-9 (whole document). Brief version 2, plus the two conventions sent later by the coordinator
(footnote markers `[^n]` with `Footnote n:` items before the page's last continuing paragraph; no `join_previous` on an
item that follows a `$$` block). TeX source used: `tex-source/pac-nmpc/` (main.tex inputs introduction, related_work,
notation, ispo, pac, trajgen, feedback, nmpc, trajgen_experiments, nmpc_experiment, hardware, fixedwing, discussion;
bibliography from main.bbl; `old_fixedwing.tex` is not included by main.tex and was not used).

## Final state

| PDF page | Printed page | State | `check` | Adjudication note |
| --- | --- | --- | --- | --- |
| 1 | (cover sheet) | reviewed, `[v2]` | OK 4/4 | not needed |
| 2 | 1 | reviewed, `[v2]` | OK 94/94 | not needed |
| 3 | 2 | reviewed, `[v2]` | ATTENTION, category (a) only | written |
| 4 | 3 | reviewed, `[v2]` | ATTENTION, category (a) only | written |
| 5 | 4 | reviewed, `[v2]` | ATTENTION, category (a) only | written |
| 6 | 5 | reviewed, `[v2]` | ATTENTION, category (a) only | written |
| 7 | 6 | reviewed, `[v2]` | ATTENTION, category (a) only | written |
| 8 | 7 | reviewed, `[v2]` | ATTENTION, category (a) only | written |
| 9 | 8 | reviewed, `[v2]` | OK 151/151 | not needed |

All nine pages were examined from the page image (preview, overlay, 150-250 dpi crops) and against the TeX source. Nothing
of category (b) remains. Pages 5-9 were raw extraction when I started; pages 1-4 had partial version-1 edits.
After the restart the state on disk was re-checked: `check` was run once per page and gives the table above.

## Assets (unique in the document, no clashes)

| Asset | Kind | PDF page | Box (pt) |
| --- | --- | --- | --- |
| `figure-1` | figure | 2 | [329,174,546,360] |
| `algorithm-1` | algorithm image + transcription | 3 | [310,53.5,565,165] |
| `algorithm-2` | algorithm image + transcription | 4 | [310,53.5,565,165.5] |
| `algorithm-3` | algorithm image + transcription | 4 | [310,173,565,241.5] |
| `algorithm-4` | algorithm image + transcription | 5 | [47,53.5,302,189] |
| `algorithm-5` | algorithm image + transcription | 5 | [310,53.5,565,229.5] |
| `algorithm-6` | algorithm image + transcription | 5 | [310,239,565,381] |
| `figure-2` | figure (full width, panels a-h) | 6 | [46,51,566,235] |
| `figure-3` | figure | 6 | [46,268,303,400] |
| `figure-4` | figure | 6 | [311,268,566,418] |
| `figure-5` | figure | 7 | [58,51,292,206] |
| `figure-6` | figure (panels a-d) | 7 | [54,244,296,412] |
| `figure-7` | figure | 7 | [310,53,545,170] |
| `figure-8` | figure | 8 | [58,51,292,219] |
| `figure-9` | figure (panels a-d) | 8 | [54,266,296,424] |
| `figure-10` | figure | 8 | [330,51,545,213] |
| `figure-11` | figure (photo a, plot b) | 8 | [325,232,550,366] |
| `figure-12` | figure | 9 | [48,53,302,168] |

The paper has no tables. Every box was checked by cropping. Each figure/algorithm has its own caption or transcription item
directly after it and is placed after the complete paragraph that first cites it on its page (or, for Figs. 8, 9 and 12,
cited on the previous page, after the paragraph that completes the sentence carried over from that page).

## Equations

Display equations (1)-(12), all as `$$ ... \tag{n}$$` text items taken from the TeX source with the authors' macros
expanded and compared symbol by symbol with high-resolution crops: (1)-(3) on page 3, (4)-(9) on page 4, (10)-(12) on
page 5 ((12) is a three-line aligned block with a single printed number). **No formula is kept as an image.**
Macro expansion used: `\bX` -> `\boldsymbol{\tau}`, `\bU` -> `\boldsymbol{\xi}`, `\bnu` -> `\boldsymbol{\nu}`,
`\bx`/`\bu` -> `\mathbf{x}`/`\mathbf{u}`, `\bpi` -> `\boldsymbol{\pi}`, `\bzeta` -> `\boldsymbol{\zeta}`,
`\bbeta` -> `\boldsymbol{\eta}` (the macro is named beta but prints eta), `\bmu`, `\bSigma`, `\bK` -> `\mathbf{K}`,
`\bkappa` -> `\boldsymbol{\kappa}`, `\bff` -> `\mathbf{f}`, `\bQ` -> `\mathbf{Q}`, `\vect{..}` -> `\mathbf{..}`,
`\vectg{..}` -> `\boldsymbol{..}`, `\argmin` -> `\operatorname*{arg\,min}`. The `\!` spacing commands were dropped.

## TeX versus PDF

No disagreement between the TeX source and the PDF was found in text, mathematics or bibliography. Reference numbers,
equation numbers and algorithm numbers were resolved to what is printed ("Eq. 1", "Alg. 3", "(Eq. 7)", "[35]", ...).
One point worth knowing: the page prints "Renyi divergences (Eq. 7)" because the authors' label sits on the second line of
the align; (7) is the cost bound `0 <= J <= b_i`, the divergence term is in (6). Transcribed as printed.

## Authors' errors and oddities kept as printed (recorded in the pages' `review_notes`)

- Page 3: `\prod^T_{t=0}` (upper limit T) while the trajectory sequence runs to N_T; `\pi_t(x_t, \xi)` versus `\pi(x_t, \xi)`;
  "is hand-tuned weight"; Algorithm 1 line 7 has no semicolon.
- Page 4: "for some and $\alpha>0$"; Catoni sum `\sum_{i=0}^M` with factor `1/(\alpha M)`; samples indexed i0..iM and
  Eq. (7) `j = 0,...,M` versus `\sum_{j=1}^{M}` in Eq. (4); unbalanced inner parenthesis in the exponent of Eq. (6)
  (`D_2(p(\cdot|\nu)||(p(\cdot|\nu_i))`); Algorithm 2 line 4 samples from `\nu_i` (no hat/star); "Renyi" without accent.
- Page 5: "mulitvariate"; "we the compute"; Algorithm 4 line 3 loops over k while line 4 is indexed by t; Algorithms 4
  (line 8) and 6 (line 5) use `(x_t - x_t^d)` whereas Eq. (10) and Section IV-B use `(x_t^d - x_t)`; Algorithm 6 line 9 has
  subscript `T - H/\Delta t` (not N_T); `f` in the algorithms versus bold `\mathbf{f}` in Eq. (11).
- Page 6: "polices"; `p(\xi|\nu^*)` without hat in the guarantee sentence; bold subscripts in `\mathbf{x_I}`, `\mathbf{x_G}`,
  `\mathbf{Q_f}`.
- Page 7: the rally-car terminal cost is printed without the transpose.
- Page 8: fixed-wing cost with bold subscripts and a running sum starting at t=1; `\mathbf{q} \in \mathbb{Q}`.

## Joins

Inside the range (all `space` unless stated; none follows a `$$` block; the item before each is `text`):
- p2: p0002-b014 (introduction paragraph across the column break under Fig. 1).
- p2 -> p3: p0003-b002 ("... (SNMPC)." | "RNMPC represents ...", same paragraph).
- p3: p0003-b010 ("a vector of" | "control inputs ...").
- p4: p0004-b022 ("For computational efficiency," | "we assume ...").
- p4 -> p5: p0005-b003 `none` ("tra" | "jectory."; line-wrap hyphen removed on page 4).
- p5: p0005-b013 ("... of the control trajectory" | "represent control signals ...").
- p6: p0006-b007 ("(replace line 3 of Alg. 3 and" | "line 9 of Alg. 4 with ...").
- p6 -> p7: p0007-b006 ("We apply a quadratic cost" | "on the final state ...").
- p7: p0007-b012 ("... in the observance" | "of the PAC Bounds in Figure 6.").
- p7 -> p8: p0008-b005b ("When optimizing the bound" | "with nominal dynamics, ...").
- p8: p0008-b012 ("at a replanning" | "period of $H = 0.2$. ...").
- p8 -> p9: p0009-b004 ("... the algorithm is capable" | "of scaling to more complex systems, ...").

Range boundaries: page 1 is the first page and page 9 the last page of the document; no joins are needed outside the range.
Not joined on purpose: page 3 ends with Eq. (3) and page 4 starts a new sentence ("Because the likelihood ratio ...");
page 5 ends with Eq. (12) and page 6 starts a new paragraph.

## Footnotes and front matter (page 2)

- Author line: affiliation markers written `[^1][^2]`, `[^2]`, `[^1][^2]` (printed as superscripts "1,2", "2", "1,2").
- The IEEE `\thanks` block (five items in printed order: manuscript dates; editor/funding note; `Footnote 1: ...`;
  `Footnote 2: ...`; DOI note) is placed after the contributions list and before the `## II. RELATED WORK` heading, i.e.
  before the page's last continuing paragraph while keeping that paragraph's heading attached to it. The three unnumbered
  notes carry no printed marker and are plain text items. If the coordinator prefers the block directly after the Index
  Terms (front matter), it is a pure reordering of items p0002-b009, -b010, -b011, -b011b, -b012.
- Raised ordinal "th" in "1/10th" (abstract, introduction) written as plain "1/10th"; `$^{\text{th}}$` breaks the
  contiguous-line check and is not mathematics.
- Page 1 (cover sheet) copyright notice kept as text as instructed.

## Text repairs of substance

- Page 5: the whole page was glyph soup (Algorithm 4 as one text item, Algorithms 5/6 and equations as "formula"); rebuilt.
- Page 6: one merged figure box for Figs. 3 and 4, which also swallowed the first caption line of Fig. 3, split into two.
- Page 8: body text glued onto two captions (Fig. 9 + "with nominal dynamics, ..."; Fig. 11 + "period of H = 0.2. ...")
  separated; "PACNMPC" -> "PAC-NMPC", "fixedwing" -> "fixed-wing" (real hyphens lost at line wraps).
- Page 9: bibliography [1]-[37] regenerated from main.bbl and read against the page entry by entry; real hyphens restored
  ("Perception-aware", "Tube-based", "Robust-rrt", "locally-optimal"), umlauts/accents fixed (Bürger, Allgöwer, Köhler,
  Müller, Probabilités), merged entries [32]+[33] and [34]+[35] split, list markers and stray italic markers removed.
- Headings: `# ` only for the title; all section headings were `# ` in the raw pages and are now `## ` / `### `.
- Running headers on pages 5-9 had been left as `text`; now `omit` with specific reasons (with the page numbers).

## Extractor warnings (one per page, all "Review possible header/footer")

p0001-b000: rotated arXiv stamp, omitted. p0002-b000, p0003-b001, p0005-b001, p0007-b001, p0009-b001: running header
"IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. ACCEPTED AUGUST, 2023", omitted. p0004-b000, p0006-b001,
p0008-b000: running header "POLEVOY et al.: PROBABLY APPROXIMATELY CORRECT NONLINEAR MODEL PREDICTIVE CONTROL (PAC-NMPC)",
omitted. Each was confirmed on the page image. The `warnings` fields themselves were left unchanged.

## Remaining diagnostics by page (all category (a))

| Page | Missing lines | Number differences (parser 1) | Second parser |
| --- | --- | --- | --- |
| 3 | 38, all lines with inline/display maths now in LaTeX | extras only: Algorithm 1 line numbers, tags, subscripts | same |
| 4 | 46, maths lines (one also carries the removed "tra-" hyphen) | "−1" x3 (Unicode minus in L−1) versus "-1"; extras from algorithm line numbers, tags, subscripts | same |
| 5 | 31, maths lines | extras only: line numbers of Algorithms 4-6, "// Alg. 2", "// Alg. 6", tags, subscripts | additionally splits "0.33" into "33" |
| 6 | 26, maths lines | Unicode versus ASCII minus in −0.4, −1.0 (x2), −0.75 | additionally splits one "3.0" |
| 7 | 10, maths lines | none | splits one "0.2" |
| 8 | 8, maths lines | none | none |

For every missing line a scripted check (`_scratch/pac-1-9/v2/triage.py`) confirmed that all prose words of the line occur
in the page text; the only strings not found are glyph renderings of symbols (e.g. "RNx", "KNT", "QfxNT"). All printed
numbers in prose were compared with crops. Notes are in `DOC/adjudication-notes/page-0003.json` ... `page-0008.json`.

## Proposals for shared files (coordinator)

`plan.json`
- `title`: "Probably Approximately Correct Nonlinear Model Predictive Control (PAC-NMPC)" (currently "pac-nmpc").
- `notes` (suggested strings):
  1. "Source: A. Polevoy, M. Kobilarov and J. Moore, 'Probably Approximately Correct Nonlinear Model Predictive Control
     (PAC-NMPC)', IEEE Robotics and Automation Letters, preprint version accepted August 2023, DOI
     10.1109/LRA.2023.3315209; arXiv:2210.08092v3 [cs.RO], 13 Sep 2023. The rotated arXiv margin stamp and the running
     headers are omitted from the text."
  2. "PDF page 1 is the IEEE copyright cover sheet; the printed page numbers 1-8 are PDF pages 2-9."
  3. "Mathematics is written in LaTeX taken from the authors' arXiv TeX source with their private macros expanded and was
     checked against the PDF. Symbols: τ trajectory, ξ policy parameters, ν hyper-parameters of the surrogate distribution
     p(ξ|ν), J cost, calligraphic J expected cost, J^+_α and C^+_α the PAC bounds on expected cost and on the probability
     of constraint violation, hats denote estimates."
  4. "Algorithms 1-6 are kept as images, each followed by a line-by-line transcription (indentation shown with em-space
     entities). The paper has no tables and no appendix."
  5. "The authors' inconsistencies are preserved, not corrected: 'for some and α>0'; the unbalanced parenthesis in the
     exponent of Eq. (6); the sample index ranges j = 0..M (Eq. (7), sample list) versus j = 1..M (Eq. (4)); the product
     limit T in the trajectory density; the sign convention (x_t − x_t^d) in Algorithms 4 and 6 versus (x_t^d − x_t) in
     Eq. (10); the loop index k in Algorithm 4 line 3; the subscript T − H/Δt in Algorithm 6 line 9; the reference
     'Renyi divergences (Eq. 7)', which points at the cost bound, the divergence term being in Eq. (6)."
  6. "Venue titles in the reference list are printed in italics; the italics are not reproduced. The ordinal in '1/10th' is
     printed with a raised 'th'."
- `reading_order`: not needed; the float order is handled inside the page files.

Navigation headings (as emitted, in order):
`# Probably Approximately Correct Nonlinear Model Predictive Control (PAC-NMPC)`; `## I. INTRODUCTION`;
`## II. RELATED WORK`; `## III. BACKGROUND` (`### A. Iterative Stochastic Policy Optimization`,
`### B. PAC Bounds for Stochastic Policy Search`); `## IV. APPROACH` (`### A. PAC Stochastic Trajectory Optimization`,
`### B. PAC Feedback Motion Planning`, `### C. PAC-NMPC`); `## V. SIMULATION EXPERIMENTS`
(`### A. Trajectory Optimization Experiments`, `### B. NMPC Experiment`); `## VI. HARDWARE EXPERIMENTS`
(`### A. Rally Car`, `### B. Fixed-Wing UAV`); `## VII. DISCUSSION`; `## REFERENCES`.
- The subsection letters repeat (A/B under III, IV, V, VI); if the navigation needs unique anchors, the builder could
  prefix them with the section number ("III-A", ...). I kept the printed form.
- The run-in titles "1) Hardware:", "2) Setup:", "3) Results:" occur twice (VI-A and VI-B) and are bold run-ins inside the
  paragraphs, not headings.
- The copyright notice of PDF page 1 precedes the `# ` title of page 2 in the emitted text. If the builder drops a title
  heading that duplicates the plan title only on the first page, the page-2 title may be emitted in addition to the
  generated title; the coordinator may want to check this after the build.

Asset names: `figure-1` ... `figure-12`, `algorithm-1` ... `algorithm-6`; no clash inside the document. Other papers of the
NMPC collection will also have `figure-N`/`algorithm-N` names; they are separate skills, so no clash is expected.

## Limitations

- The LaTeX was not compiled or rendered; it was checked by reading against crops and by a script for balanced `$`,
  braces, `\left`/`\right` and environments (`_scratch/pac-1-9/v2/selfcheck.py`).
- In-figure numbers (plot annotations such as 0.376, 4.57%, 9.4%) are only in the images, not transcribed as text.
- Algorithm transcriptions use Markdown hard line breaks (two trailing spaces) and `&emsp;` for indentation; a renderer
  that ignores either will show the lines run together or unindented, the images remain authoritative.
- The algorithm side comments are printed in blue typewriter face; the colour and face are not reproduced.
- E-mail addresses (typewriter face) and italic venue names are plain text.

## Notes on the brief

- The brief's footnote rule ("at the end of that page's items") conflicted with "the page ends with the prose that
  continues onto the next page" for IEEE first pages; the later convention resolves it. For `\thanks` blocks it would help
  to say explicitly whether unnumbered notes (manuscript dates, DOI note) are also labelled and where the block goes
  relative to a section heading that immediately precedes the last continuing paragraph.
- "Run-in paragraph titles ... in bold": IEEE subsubsection run-ins are printed in italics; I followed the brief (bold).
- No format is prescribed for algorithm transcriptions (line breaks, indentation); a fixed convention would make the
  seven papers uniform.
- Triage of `missing line` entries is the costly part once maths is LaTeX (159 lines on six pages here). A `check`
  option that also reports, per missing line, the prose words not found in the page text (what `triage.py` does) would
  make category (b) cases stand out. Treating the Unicode minus and ASCII hyphen-minus as equal in `number_tokens` would
  remove the remaining number differences on pages 4 and 6.
- "Do not put `<sup>` / use LaTeX" leaves the ordinal "1/10th" case open; plain text was the only form that passes the
  contiguous-line check.

## Page log

### Page 1
IEEE copyright cover sheet: one text item (copyright notice + DOI), verbatim; arXiv stamp omitted. check OK.

### Page 2
Title (`#`), authors with `[^n]` markers, abstract, index terms, `## I. INTRODUCTION`, Figure 1 (`figure-1`) with caption,
contributions list, `\thanks` block (see "Footnotes and front matter"), `## II. RELATED WORK`. check OK.

### Page 3
Related Work (continued), `## III. BACKGROUND`, III-A, III-B; equations (1)-(3); Algorithm 1 (`algorithm-1`) with
transcription after the citing paragraph. 38 missing lines / extra numbers, category (a); note written.

### Page 4
III-B continued, `## IV. APPROACH`, IV-A, IV-B; equations (4)-(9); Algorithms 2, 3 with transcriptions. 46 missing lines,
"−1" versus "-1", category (a); note written.

### Page 5
IV-B continued, `### C. PAC-NMPC`, `## V. SIMULATION EXPERIMENTS`, V-A; equations (10)-(12); Algorithms 4, 5, 6 with
transcriptions. 31 missing lines, extras, category (a); note written.

### Page 6
V-A continued, `### B. NMPC Experiment`; Figures 2, 3, 4 with captions; all experiment parameters compared with crops.
26 missing lines, minus-sign differences, category (a); note written.

### Page 7
V-B continued, `## VI. HARDWARE EXPERIMENTS`, `### A. Rally Car`; Figures 5, 6, 7 with captions. 10 missing lines,
second-parser split of "0.2", category (a); note written.

### Page 8
VI-A end, `### B. Fixed-Wing UAV`, `## VII. DISCUSSION`; Figures 8, 9, 10, 11 with captions. 8 missing lines, category (a);
note written.

### Page 9
Discussion end, Figure 12 with caption, `## REFERENCES` with entries [1]-[37] (one text item each). check OK.
