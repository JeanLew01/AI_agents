# Review report: whole-body-mppi-paper, pages 1-7 (brief v2)

Paper: "Real-Time Whole-Body Control of Legged Robots with Model-Predictive Path Integral Control",
Alvarez-Padilla, Zhang, Kwok, Dolan, Manchester, arXiv:2409.10469v1 (16 Sep 2024), 7 pages, IEEE two-column.
DOC = /home/jixia/AI_agents/paper2agent/NMPC/paper-review/whole-body-mppi-paper/documents/s001-whole-body-mppi
Reviewer: single reviewer for all pages (r1). Scratch: /home/jixia/AI_agents/paper2agent/NMPC/paper-review/_scratch/whole-body-mppi-r1

## Progress log (appended page by page)

- Page 1: reviewed, [v2], check OK (106/106). Title, author line ($^{1}$/$^{2}$), Footnote 1, Footnote 2,
  IEEE submission notice (printed once in the PDF, kept once), abstract, I. INTRODUCTION. Figure 1 (`figure-1`,
  bbox [310,155,561,260]) + caption "Fig. 1. ...". Join: p0001-b012 join_previous=space (paragraph "There are several
  key design choices ..." crosses from the left to the right column). arXiv stamp omitted. No maths.
- Page 2: reviewed, [v2], check ATTENTION (72/79; 7 missing lines, all category (a) maths, adjudication note written).
  Figure 2 (`figure-2`, bbox [64,47,549,232], all 17 native diagram labels inside) + caption "Fig. 2. ...". Headings
  `## II. BACKGROUND AND RELATED WORK`, `### A. Locomotion and Manipulation for Legged Robots`,
  `### B. Model-Predictive Path Integral Control`. Equations (1), (2) converted from formula images to `$$ \tag{} $$`
  text items (TeX source, checked against 220-dpi crop). Join: p0002-b007 join_previous=space (left->right column).
  Page ends mid-sentence "A lower value of" -> page 3 first item joins.
- Page 3: reviewed, [v2], check ATTENTION (70/71 + extra numbers from the algorithm transcription; all category (a),
  adjudication note written). Figure 3 (`figure-3`, [52,48,560,143]) + caption. Algorithm 1: new image item p0003-alg1
  (`algorithm-1`, [52,172,301,411]) + transcription p0003-b005 (title, Require/Ensure, lines 1:-14:). New heading item
  p0003-h3 `## III. SAMPLING-BASED MPC FOR LEGGED ROBOTS` (extractor lost it). Joins: p0003-b008 join_previous=space
  (continues page 2), p0003-b002 join_previous=space (left->right column). Page ends mid-sentence "we reduce the size of".
- Page 4: reviewed, [v2], check ATTENTION (87/95; 8 missing lines, all category (a) maths, adjudication note written).
  Figure 4 (`figure-4`, [311,48,560,190]) + caption, placed after the paragraph it interrupted. Equation (3) converted
  to one aligned block with one \tag{3}. Headings `### C. State Estimation`, `## IV. EXPERIMENTS AND RESULTS`,
  `### A.`-`### D.`; the centred URL line demoted from heading to text. Joins: p0004-b000 join_previous=space (continues
  page 3), p0004-b010 join_previous=space (left->right column). Page ends mid-sentence "cost for the position".
- Page 5: reviewed, [v2], check ATTENTION (77/85; 8 missing lines, all category (a) maths, adjudication note written).
  Figure 5 had no item (extractor kept only the caption): new item p0005-fig5 (`figure-5`, [90,59,265,205]).
  Figure 6 (`figure-6`, [320,49,550,254], all 14 native labels incl. "×10^6" inside). Equation (4) converted.
  `### E. Ablation Studies`; run-in titles "**1) Sampling representation:**" ... "**4) Prediction horizon:**" in bold.
  Joins: p0005-b001 join_previous=space (continues page 4), p0005-b010 join_previous=space (left->right column).
  Page ends mid-sentence "especially in the absence".
- Page 6: reviewed, [v2], check ATTENTION (82/84 + one minus-sign number difference; all category (a), adjudication
  note written). Figure 7 (`figure-7`, [59,46,550,187], four panels, all 29 native labels inside) + caption. Table I
  (`table-1`, [74,447,279,507], 4x4 string rows, joined two-line headers, empty first header cell) then caption item
  "TABLE I / COMPARISON OF FEATURES ..." (p0006-b006 merged into p0006-b005 and deleted). Headings `### F.`,
  `## V. CONCLUSIONS AND FUTURE WORK`, `### A. Limitations`, `### B. Future Work`, `## ACKNOWLEDGMENTS`.
  Join: p0006-b002 join_previous=space (continues page 5). Page ends with a complete paragraph.
- Page 7: reviewed, [v2], check ATTENTION only for one date-wrap number token (136/136 lines found; adjudication note
  written). `## REFERENCES`, entries [1]-[32] reordered into printed order ([13]-[19] had been placed after [32]),
  [5]/[6] split (new item p0007-b005b), all 32 entries compared with the native lines by script, URLs rejoined
  ([4], [15], [21]), "human-to-humanoid" restored in [3].

## Final state

| Page | reviewed | `[v2]` | check | Remaining diagnostics (category) | Adjudication note |
| --- | --- | --- | --- | --- | --- |
| 1 | true | yes | OK, 106/106 | none | not needed |
| 2 | true | yes | ATTENTION, 72/79 | 7 missing lines: inline maths + eq. (1), (2) (a) | `adjudication-notes/page-0002.json` |
| 3 | true | yes | ATTENTION, 70/71 | 1 missing line ($\lambda$); extra numbers from the Algorithm 1 transcription (a) | `page-0003.json` |
| 4 | true | yes | ATTENTION, 87/95 | 8 missing lines: eq. (3), $x_{\text{ref}}$, $u_{\text{ref}}$, box size, $\ell_1$ (a) | `page-0004.json` |
| 5 | true | yes | ATTENTION, 77/85 | 8 missing lines: box cost, eq. (4), $\sim$, $\lambda$ (a) | `page-0005.json` |
| 6 | true | yes | ATTENTION, 82/84 | 2 missing lines ($\sim$); "40 −50" minus glyph vs `$40-50$` (a) | `page-0006.json` |
| 7 | true | yes | ATTENTION, 136/136 | one number token: wrapped date "2024-09-" / "12." in ref. [4] rejoined as 2024-09-12 (a-like, not maths; nothing missing) | `page-0007.json` |

No category (b) diagnostic remains. Page 7 (references) cannot reach `OK` without breaking the correct date in [4].

## Assets per page

| Page | Item | Kind | Label | Asset | bbox (pt) |
| --- | --- | --- | --- | --- | --- |
| 1 | p0001-b004 | figure | Figure 1 | `figure-1` | [310,155,561,260] |
| 2 | p0002-b000 | figure | Figure 2 | `figure-2` | [64,47,549,232] |
| 3 | p0003-b000 | figure | Figure 3 | `figure-3` | [52,48,560,143] |
| 3 | p0003-alg1 (new) | figure | Algorithm 1 | `algorithm-1` | [52,172,301,411] |
| 4 | p0004-b008 | figure | Figure 4 | `figure-4` | [311,48,560,190] |
| 5 | p0005-fig5 (new) | figure | Figure 5 | `figure-5` | [90,59,265,205] |
| 5 | p0005-b008 | figure | Figure 6 | `figure-6` | [320,49,550,254] |
| 6 | p0006-b000 | figure | Figure 7 | `figure-7` | [59,46,550,187] |
| 6 | p0006-b004 | table (rows) | Table 1 | `table-1` | [74,447,279,507] |

Every figure box was checked on all four edges with a crop. Fig. 2, 6 and 7 carry native text (diagram labels,
tick labels, axis titles, legends, "×10^6"/"·10^6" multipliers); all of it lies inside the boxes (extents measured
from the native lines). Figures 1, 3, 4, 5 are raster images (their in-figure text is raster).
Algorithm 1 has a text transcription item after the image (p0003-b005). No asset-name clashes (one source).

Equations: (1), (2) page 2; (3) page 4 (two printed lines, one number: one `aligned` block with one `\tag{3}`);
(4) page 5. All four were `formula` image items and are now `$$ ... \tag{n} $$` text items taken from the TeX source
and checked against 220-dpi crops. **No formula is kept as an image.**

## Joins

Within the range: p0001-b012, p0002-b007, p0003-b008 (from page 2), p0003-b002, p0004-b000 (from page 3),
p0004-b010, p0005-b001 (from page 4), p0005-b010, p0006-b002 (from page 5); all `space`, each placed directly after
a text item. Range boundaries: page 1 starts the document; page 7 ends with the bibliography. No `none` joins.

Structural repairs of substance: page 3 (the extractor had interleaved the Fig. 3 caption, Algorithm 1 and
right-column prose in one item and lost the section III heading); page 5 (Figure 5 had no item); page 6 (Table I
caption merged from two items, header row joined); page 7 (references [13]-[19] were placed after [32]; [5]+[6] merged).
Floats were moved so that none interrupts a sentence (Fig. 1 after the 2nd intro paragraph, Fig. 4 after the
hardware paragraph, Fig. 5 after the box-pushing subsection, Fig. 6 after the IV-E intro paragraph, Fig. 7 after the
first paragraph of page 6, Fig. 3 + Algorithm 1 after the first paragraph of page 3).

## TeX versus PDF

No disagreement of substance: abstract, sections, equations (1)-(4), Algorithm 1, Table I and root.bbl match the
PDF. Notes: TeX `\Bar{x}` written as `\bar{x}`; `\href{whole-body-mppi.github.io}{website}` printed as plain
"website" (kept plain, the target has no scheme); TeX `\sim` ablation values and `$\lambda = \sim 0.1$` reproduce
the printed "λ =∼ 0.1".

## Authors' slips kept as printed (each verified on the page)

- p3 "a simple yet effective modification better scale MPPI" (missing "to").
- p3 Algorithm 1 line 6 "Simulate forward for $T$ timesteps using $u_n$" (the loop samples $u_t$); line 2
  "$\mathcal{L}_n$ = 0" with a text-mode equals; lines 10/11 "using Equation 1/2" without parentheses.
- p2 eq. (2) $\mu_t = \sum_{n=1}^{N} \omega_n u_{t}$ has no sample index on $u_t$; eq. (1) reuses $n$ as the
  summation index in its denominator (notation as printed).
- p4 "in Sec. IV-E, we investigate ..." (lower-case sentence start); "Across all hard experiments" (for hardware).
- p5 "$\lambda = \sim 0.1$" (printed "λ =∼ 0.1"); "interactions between the robot body" (second object missing).
- p6 "(Fig 7)" without period; run-in title "5) Number samples:"; "can not see".

## Proposed plan notes (conversion notes) for the coordinator

1. "Source: arXiv:2409.10469v1 [cs.RO], 16 Sep 2024 (identifier taken from the rotated margin stamp on page 1, which
   is omitted as page furniture). The page-1 box 'This work has been submitted to the IEEE for possible publication.
   Copyright may be transferred without notice, after which this version may no longer be accessible.' is kept once."
2. "Mathematics is written in LaTeX from the authors' TeX source and checked against the PDF; display equations
   (1)-(4) carry their printed numbers as \tag{n}; equation (3) is one two-line aligned block with one number."
3. "Algorithm 1 (page 3) is kept as an image (algorithm-1) followed by a line-by-line transcription; the authors'
   pseudocode is reproduced as printed, including 'using $u_n$' in line 6."
4. "Figures 2, 6 and 7 are vector graphics whose labels, tick values, legends and the ×10^6 / ·10^6 axis multipliers
   are only in the images; the plotted values of Figs. 6-7 are not tabulated in the paper (the authors' pgfplots .dat
   files exist in the TeX source but were not used)."
5. "Table I (page 6) is printed with its caption below the table; the two-line column headers 'Offline / Training'
   and 'Whole-Body / Contact' are joined with a space in one header cell; the first header cell is empty."
6. "Floats were moved between complete paragraphs; cross-column and cross-page paragraphs are rejoined."
7. "No supplementary material: the paper refers to a project website (whole-body-mppi.github.io) with experiment
   videos, code and the full per-task hyperparameter list, and to a supplementary video; none of these is included."

## Navigation list (exact heading -> what is there)

- `# Real-Time Whole-Body Control of Legged Robots with Model-Predictive Path Integral Control` -> author line,
  Footnote 1/2 (CMU affiliations, e-mails), IEEE submission notice, abstract (`**Abstract—**`).
- `## I. INTRODUCTION` -> motivation, Fig. 1 (Go1 box pushing, hardware vs MuJoCo), key design choices (spline
  control points + PD tracking, multi-threaded MuJoCo rollouts, ablations), three contributions, paper outline.
- `## II. BACKGROUND AND RELATED WORK` -> Fig. 2 (system diagram: MPPI 100 Hz, joint targets, Go1 PD 20 kHz, EKF
  500 Hz, MoCap 100 Hz).
- `### A. Locomotion and Manipulation for Legged Robots` -> gradient-based MPC [8]-[11] vs RL [12]-[15]; aim of
  combining both without offline optimisation.
- `### B. Model-Predictive Path Integral Control` -> MPPI sampling, weights eq. (1), mean update eq. (2), role of
  temperature $\lambda$, Fig. 3 (box climb keyframes), Algorithm 1 (MPPI Control Algorithm) with transcription,
  related MPPI work (driving, predictive sampling [25], Carius [26]).
- `## III. SAMPLING-BASED MPC FOR LEGGED ROBOTS` -> section overview.
- `### A. MuJoCo Physics Engine` -> simulator choice (Drake, Dojo, Isaac, MJX vs CPU MuJoCo); 30-50 parallel
  rollouts on a Core-i9 suffice.
- `### B. Representing Controls as a Cubic Spline` -> sampling spline control points, cubic interpolation.
- `### C. State Estimation` -> EKF at 500 Hz fusing MoCap (100 Hz), IMU (500 Hz), encoders (500 Hz); model mismatch.
- `## IV. EXPERIMENTS AND RESULTS` -> overview, project URL.
- `### A. Hardware Implementation` -> i9-12900KS, 64 GB, ROS/Ethernet; 100 Hz, dt 0.01 s, 0.4 s horizon ($T = 40$),
  30 samples; PD at 20 kHz; Fig. 4 (hexagon walking).
- `### B. Walking on Flat Terrain` -> walking cost eq. (3), Raibert-heuristic gait reference, $Q$, $R$.
- `### C. Locomotion Over Challenging Terrains` -> box climb up to 0.24 m (Fig. 3).
- `### D. Box Pushing` -> 3.5 kg box, $\ell_1$ box cost, eq. (4), success 9/10 (forward) and 6/10 (front-right),
  Fig. 5 (box trajectories).
- `### E. Ablation Studies` -> Fig. 6 (sampling representation: Direct / Zeroth-Order / Linear / Cubic), Fig. 7
  (control frequency, temperature, horizon, number of samples; MuJoCo vs Gazebo); run-in items **1) Sampling
  representation:**, **2) Control frequency:**, **3) Temperature:**, **4) Prediction horizon:**, **5) Number samples:**.
- `### F. Comparisons to RL and MPC` -> Table I (offline training / whole-body contact / gradient-free) and discussion.
- `## V. CONCLUSIONS AND FUTURE WORK` -> summary.
- `### A. Limitations` -> myopia beyond the horizon, simulator fidelity (fluids, soft materials, contact).
- `### B. Future Work` -> online contact/friction estimation, better sampling distributions, MJPC integration.
- `## ACKNOWLEDGMENTS` -> thanks.
- `## REFERENCES` -> [1]-[32].

Note for the navigation: subsection letters restart in every section, so `### A.` and `### B.` each occur four
times (II, III, IV, V) and `### C.` twice (III, IV); the parent `##` heading disambiguates them.

## Limitations

- The checker cannot verify LaTeX maths against the glyph text; every equation and inline symbol was compared
  visually with 220-dpi crops.
- Figure contents (plot values, diagram labels) are only available as images.
- Page 7 stays at ATTENTION because of the wrapped access date in [4] (see the adjudication note).

## Notes on the brief

- The assignment's own conventions (abstract as `**Abstract—**` with non-bold body, upper-case section headings,
  Table I caption after the table) were clear and differed slightly from older siblings (e.g. `***Abstract***—` on
  post-stall-navigation); the coordinator may want to align earlier papers.
- The brief says references pages "should reach OK"; a correctly rejoined date or URL split across a line break
  can make that impossible (page 7 here), so an adjudication note is needed even for pure prose.
- A page script that adds items is not idempotent if re-run on its own output; keeping a copy of the original page
  JSON in scratch (as done here) avoided damage.
