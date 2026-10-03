# Review report: pac-nmpc-value-function, PDF pages 1-9 (brief version 2)

Paper: "Robust Perception-Based Navigation using PAC-NMPC with a Learned Value Function"
(Polevoy, Gonzales, Kobilarov, Moore; arXiv:2309.13171v3; ACC 2025).
TeX source used: `main.tex` includes `introduction_v2`, `related_work`, `background_v2`, `approach`,
`sim_experiments`, `hardware_experiments`, `discussion` (the files `introduction.tex`, `background.tex`
and `appendix.tex` are NOT included by `main.tex` and were not used). Bibliography from `main.bbl`.

Status legend: DONE = reviewed under brief v2, `review_notes` starts with `[v2]`.

## Per-page log

### Page 1 - DONE
- Cover sheet with the IEEE copyright notice only; kept verbatim as one `text` item.
- Rotated arXiv margin stamp (`arXiv:2309.13171v3 [cs.RO] 10 Jun 2025`) omitted with reason; this resolves the
  extractor warning "Review possible header/footer: p0001-b000".
- `check`: OK (4/4 lines). No adjudication note needed.

### Page 2 - DONE
- Title (`# `), authors (`$^{1,2}$` superscripts), two affiliation/e-mail notes, abstract, Figure 1, `## I. INTRODUCTION`, four paragraphs.
- Figure: `figure-1` (Figure 1), bbox [323,155,548,366], panels a)-c) inside; caption separate.
- Affiliation footnotes are placed after the author line (not at the page end) so that the page ends with the prose
  that continues onto page 3.
- Abstract: bold face of the whole abstract dropped, run-in "Abstract—" kept in bold italics; "1/10th" written with a plain "th"
  (printed as superscript ordinal).
- Joins: `p0002-b012` join_previous=space (column break inside a sentence). Page ends mid-sentence; continued on page 3.
- `check`: OK (85/85 lines). No adjudication note needed.

### Page 3 - DONE
- End of Section I (join_previous=space from page 2), `## II. RELATED WORK`, `## III. BACKGROUND`, `### A. PAC-NMPC`.
- No floats, no display equations. Inline maths of three paragraphs converted from HTML sub/sup markup to LaTeX
  (from `background_v2.tex`, macros expanded, checked against 260-dpi crops). No TeX-versus-PDF disagreement.
- Joins: `p0003-b000` space (from page 2), `p0003-b005` space (column break). Page ends mid-sentence
  ("where $\mathcal{J}^+_\alpha(\boldsymbol{\nu})$"); continued on page 4.
- Authors' typos kept: unbalanced "(e.g., [38], and", "Actor Critic Props [44], uses".
- `check`: 110/138 lines; 28 missing lines all category (a) (inline maths); number differences are only U+2212 vs
  ASCII minus in `N_T-1` (category (a)). Adjudication note written.

### Page 4 - DONE
- End of III-A (join from page 3), `### B. Actor Critic Reinforcement Learning`, `## IV. APPROACH`, `### A. Problem Formulation`,
  `### B. Learned Value Function`, `### C. PAC-NMPC with Learned Value Function`.
- Display equations now LaTeX text items (formula images `equation-1` ... `equation-5` of the earlier run removed):
  (1) PAC bound, one `\tag{1}` block for the numbered first line plus an aligned block for the four unnumbered lines, same item;
  (2) trajectory cost; (3) constraints, `\tag{3}` on the first line plus aligned block for g_o, c, C; (4) occupied point; (5) reward.
- All inline maths converted to LaTeX from `background_v2.tex` / `approach.tex`, macros expanded, compiled with pdflatex and
  compared with 250-dpi crops. No TeX-versus-PDF disagreement.
- Printed peculiarities kept: unbalanced parenthesis in `D_2(p(.|nu)||(p(.|nu_i))`; `forall j = 0,...,M` vs sum over j=1..M;
  `arg min` in the optimal-policy definition; "the the"; "constrained violation".
- Joins: `p0004-b000` space (from page 3); `p0004-b009` space (column break). Page ends with a complete paragraph.
- `check`: 39/121 lines; 82 missing lines all category (a); number differences only U+2212 vs ASCII minus (`L-1` x2, `N_T-1`).
  Adjudication note written.

### Page 5 - DONE
- End of IV-C, `## V. SIMULATION EXPERIMENTS` (was a text item), `### A. Experimental Setup` (was `# _..._`).
- Display equations as LaTeX text items: (6) value-function improvement constraint (`\tag{6}` on the first line g_V, then aligned block for
  c_V and C; two extractor formula fragments merged into one item); (7) stochastic bicycle model (aligned block for the two unnumbered
  lines, then `\tag{7}` on the noise line, as printed).
- Figures: `figure-2` (Figure 2, bar chart, bbox [311.5,56,560,179]) and `figure-3` (Figure 3, trajectories, bbox [338,217,532,410]);
  captions separate. Both are placed after the paragraph "When running PAC-NMPC ... 50Hz." so that they do not interrupt the sentence
  that runs from the left column bottom to below the figures.
- TeX-versus-PDF: source `(eq. \ref{eq:constraint_pac_bound})` is printed as "(eq. III-A)" (label inside inline maths); the printed text
  is transcribed.
- Text repairs: glyph-soup maths with prose glued into superscripts rewritten; new item `p0005-b008b` for the separate paragraph
  "We use a quadratic state cost ..."; "PAC-NMPC" hyphen restored in the Fig. 3 caption; `A\*` escaped.
- Joins: `p0005-b015` space (column break, sentence "... shortest path to the | goal."). Page ends mid-sentence ("... in simulation with the");
  continued on page 6.
- `check`: 49/87 lines; 38 missing lines all category (a); number differences are scientific notation written as
  `4\mathrm{e}^{-4}` etc. and U+2212 vs ASCII minus (category (a)); the second parser also splits "0.1". Adjudication note written.

### Page 6 - DONE
- End of V-A (join from page 5), `### B. Cluttered Environments`, `### C. Concave Trap Environments` (both were `# _..._`).
- Figures: `figure-4` (Figure 4, PAC bounds vs Monte Carlo, bbox [64,56.5,289,233]), `figure-5` (Figure 5, bar chart, bbox [312,56,559,175.5]),
  `figure-6` (Figure 6, concave trap trajectories, bbox [338,221,533,414]); captions separate. Floats are emitted where the TeX source
  places them (Fig. 4 after the first paragraph of V-B; Figs. 5-6 directly after the heading C), never inside a sentence.
- Joins: `p0006-b002` space (from page 5); `p0006-b012` none ("com-|putation", hyphen removed from `p0006-b007`). Page ends
  mid-sentence ("We generated 100 random"); continued on page 7.
- Text repairs: "i-9-13900H" (extractor had "i-913900H"), inline maths in LaTeX, `A\*` escaped.
- No display equations.
- `check`: 64/71 lines; 7 missing lines category (a); number difference "13900" vs "-13900" is a tokenizer artifact of the real
  hyphen in "i-9-13900H" (category (a)). Adjudication note written.

### Page 7 - DONE
- End of V-C (join from page 6), `### D. Fixed-wing UAV`, `## VI. HARDWARE EXPERIMENTS` (headings repaired from `# `).
- Figures: `figure-7` (Figure 7, fixed-wing simulation rendering, bbox [82.5,55.5,270.5,188]), `figure-8` (Figure 8, bar chart,
  bbox [311,56,560,190]), `figure-9` (Figure 9, bar chart with additional noise, bbox [311,227.5,560,360.5]); captions separate.
  Floats follow the TeX source order (Fig. 7 after the heading D; Figs. 8-9 at the end of Section V).
- Joins: `p0007-b002` space (from page 6); `p0007-b011` space (column break inside the sentence "... Q_r = diag([0.00, 0.00, 0.1]), | Q_omega = ...").
  Page ends mid-sentence ("were blocking the path to"); continued on page 8.
- Inline maths rewritten in LaTeX from `sim_experiments.tex`; all numbers read on crops. No display equations. No TeX-versus-PDF disagreement.
- Printed peculiarities kept: missing full stop after "(Fig. 5)"; symbol `L` used both for the number of prior policies and for a wheelbase.
- `check`: 63/84 lines; 21 missing lines category (a); number differences only U+2212 vs ASCII minus (-0.90, -0.89, -0.16, -10).
  Adjudication note written.

### Page 8 - DONE
- End of Section VI (join from page 7), `## VII. DISCUSSION & CONCLUSION`, `## REFERENCES` with entries [1]-[17].
- Figure: `figure-10` (Figure 10, hardware bar chart, bbox [52.5,56,301,178]); caption separate; emitted after the last paragraph of
  Section VI (TeX source position).
- Extractor warning "Review possible header/footer: p0008-b000" resolved: the item is the real heading "REFERENCES", now `## REFERENCES`.
- References: one item per entry, text regenerated from `main.bbl` and verified against the page (all native lines found; entries read on
  crops). URLs re-joined, underscores restored (`paper_files`, `Paper_12.pdf`); merged item [15]-[17] split (`p0008-b023`, `-b023b`, `-b023c`).
- Joins: `p0008-b003` space (from page 7). Page ends with complete entry [17].
- `check`: OK (154/154 lines). No adjudication note needed.

### Page 9 - DONE
- Remainder of the bibliography, entries [18]-[55]; no heading, floats or maths.
- One item per entry, text regenerated from `main.bbl` and verified against the page (all native lines found; every entry read on
  250-dpi crops). Entry [46] had been swallowed into the item of [45]; now its own item `p0009-b028b`. Accents restored
  (Bektaş, Allgöwer, Gjærum, Håkansson, Araújo), URLs re-joined, underscores restored in the URL of [53].
- Joins: `p0009-b020` space (entry [37] continues from the bottom of the left column to the top of the right column).
- `check`: OK (195/195 lines). No adjudication note needed.

## Summary

### Final state
All nine pages are reviewed under brief version 2 (`reviewed: true`, `review_notes` start with `[v2]`). The run was interrupted
once by a machine restart after page 8; state on disk was re-checked page by page before page 9 was finished.
`check` result: pages 1, 2, 8, 9 `OK`; pages 3-7 show only category (a) diagnostics and each has an adjudication note
(`DOC/adjudication-notes/page-0003.json` ... `page-0007.json`). No category (b) diagnostic remains.

### Assets and equations
| PDF page | Item | Asset name | Content |
| --- | --- | --- | --- |
| 2 | Figure 1 | `figure-1` | a) NMPC with learned value function and LiDAR; b), c) timelapse photos |
| 5 | Figure 2 | `figure-2` | cluttered environments, outcome percentages (bar chart) |
| 5 | Figure 3 | `figure-3` | cluttered test environment with trajectories |
| 6 | Figure 4 | `figure-4` | optimized PAC bounds vs Monte Carlo estimates |
| 6 | Figure 5 | `figure-5` | concave trap environments, outcome percentages (bar chart) |
| 6 | Figure 6 | `figure-6` | concave trap environment with trajectories |
| 7 | Figure 7 | `figure-7` | fixed-wing simulation environment |
| 7 | Figure 8 | `figure-8` | fixed-wing environments, outcome percentages |
| 7 | Figure 9 | `figure-9` | fixed-wing environments with additional noise |
| 8 | Figure 10 | `figure-10` | hardware environments, outcome percentages |

All ten figures are raster images without native text; every box was measured from the ink extent (about 2 pt margin, nothing else
within 6 pt) and viewed as a crop. The paper has no tables and no algorithm boxes.

Display equations, all as LaTeX `text` items (none kept as image): (1)-(5) on page 4, (6)-(7) on page 5.
Where the printed number belongs to one line of a multi-line group ((1), (3), (6): first line; (7): last line), that line is its own
`$$...$$` block with `\tag{n}` and the unnumbered lines are an `aligned` block in the same item, so every printed number is visible
on the line that carries it in the PDF. In the authors' usage the number labels the whole group.
All LaTeX on pages 3-7 was test-compiled with `pdflatex` (amsmath, amssymb) and the rendering compared with the page.

### Joins
Inside the range: `p0002-b012`, `p0003-b005`, `p0004-b009`, `p0005-b015`, `p0007-b011`, `p0009-b020` (space, column breaks);
`p0006-b012` (none, "com-|putation").
Across pages (first item of the later page, space): `p0003-b000`, `p0004-b000`, `p0006-b002`, `p0007-b002`, `p0008-b003`.
Pages 5, 8 and 9 start with a new paragraph or entry. No join is needed at the range boundaries (the range is the whole document).
No `join_previous` item follows a `$$` block (checked by script, per the coordinator's added convention).

### Formulas kept as images
None.

### TeX-versus-PDF disagreements
- Page 5: source `(eq. \ref{eq:constraint_pac_bound})`; the label is inside inline maths in Section III-A, so the PDF prints
  "(eq. III-A)". Transcribed as printed. The intended target is the unnumbered guarantee
  P(E[C(tau)] <= C^+_alpha(nu)) >= 1 - delta in Section III-A (PDF page 4).
- No other disagreement. `introduction.tex`, `background.tex` and `appendix.tex` are in the arXiv source but are not included by
  `main.tex` and are not part of the PDF; nothing from them was used.

### Printed peculiarities kept verbatim (authors' text, also present in the TeX)
- Page 3: unbalanced parenthesis "Lyapunov functions (e.g., [38], and backwards reachable sets"; "Actor Critic Props [44], uses".
- Page 4, eq. (1): exponent `D_2(p(.|nu)||(p(.|nu_i))` with an extra opening parenthesis; `forall j = 0, ..., M` while the sum runs
  over j = 1..M; "Renyi"; `arg min` over a_t in the definition of the optimal policy; "the the"; "constrained violation".
- Page 5: acceleration limit "[-1., 1] m/s"; `N_t` (lower-case t) in `v_max . N_t . Delta t`.
- Page 7: no full stop after "(Fig. 5)"; `L` denotes the number of prior policies ("We set L = 1") and also a wheelbase
  (`atan((L/v) theta-dot)`, "L = 0.5"); the wheelbase is `l = 0.33 m` on page 5.

### Text repairs of substance
- Pages 3-7: all inline maths rewritten in LaTeX from the TeX source (macros expanded, `\ref`/`\cite` resolved to the printed
  values); on pages 5-7 the extractor had glued prose into superscripts ("andaPACboundontheprobability", "radians.Anexample").
- Page 5: equation (6) merged from two formula fragments; paragraph "We use a quadratic state cost ..." split off (`p0005-b008b`).
- Page 6: "Intel Core i-9-13900H" (extractor: "i-913900H").
- Pages 5-8: headings repaired (`# _A. ..._` -> `###`, text item "V. SIMULATION EXPERIMENTS" -> `##`, page-header "REFERENCES" -> `##`).
- Pages 8-9: bibliography regenerated from `main.bbl` and verified line by line; [46] recovered as its own entry; [15]-[17] split;
  accents, URLs and underscores restored.
- Floats moved out of sentences on pages 5-8 (positions follow the TeX source order).

### Remaining diagnostics (all category (a))
| Page | Missing lines | Number differences | Cause |
| --- | --- | --- | --- |
| 3 | 28 | `−1` x3 vs `-1` x3 | inline maths in LaTeX; U+2212 vs ASCII minus in `N_T-1` |
| 4 | 82 | `−1` x3 vs `-1` x3 | inline maths and equations (1)-(5); minus sign in `L-1` (x2), `N_T-1` |
| 5 | 38 | sci. notation tokens, `−1` x3, `−0.4` | equations (6), (7), inline maths; `4\mathrm{e}^{-4}` etc. tokenised as mantissa + exponent; second parser also splits "0.1" |
| 6 | 7 | `13900` vs `-13900` | inline maths; real hyphen in "i-9-13900H" joined across the line break |
| 7 | 21 | `−0.90`, `−0.89`, `−0.16`, `−10` | inline maths; U+2212 vs ASCII minus |
For every missing line the prose words were additionally checked by script against the markdown with maths removed
(`_scratch/pacvf-1-9/prose.py`); only formula glyph tokens were flagged.

### Proposals for shared files (coordinator)
- `plan.json` `title`: "Robust Perception-Based Navigation using PAC-NMPC with a Learned Value Function" (currently the source id
  "pac-nmpc-value-function"). `name` can stay `pac-nmpc-value-function-paper`.
- `plan.json` `notes`, suggested entries:
  1. "Source: arXiv:2309.13171v3 [cs.RO], 10 Jun 2025 (rotated margin stamp on PDF page 1, omitted from the page text). Authors:
     A. Polevoy, M. Gonzales, M. Kobilarov, J. Moore. ©2025 IEEE; IEEE conference two-column layout."
  2. "PDF page 1 is a cover sheet with the IEEE copyright notice only; the paper starts on PDF page 2. The pages carry no printed
     page numbers."
  3. "Display equations (1)-(7) and all inline maths are LaTeX taken from the authors' TeX source with their macros expanded
     (bold xi = policy parameters, bold tau = trajectory, bold nu = hyper-parameters) and checked against the PDF. For the
     multi-line groups (1), (3), (6), (7) the `\tag` sits on the line that carries the printed number; the unnumbered lines of the
     same group are in the adjacent `aligned` block."
  4. "'(eq. III-A)' in Section IV-C is a broken cross-reference in the original; it points to the guarantee
     P(E[C(tau)] <= C^+_alpha(nu)) >= 1 - delta stated in Section III-A."
  5. "Authors' typos and notation are kept as printed, e.g. the extra parenthesis in the Renyi-divergence exponent of (1),
     'forall j = 0, ..., M', 'arg min' in the optimal-policy definition, and L used for both the number of prior policies and a wheelbase."
  6. "Figures 1-10 are raster images; the percentages in the bar charts (Figs. 2, 5, 8, 9, 10) are only in the images.
     The arXiv source contains an appendix file that is not part of this PDF."
- Optional note with the bar-chart values, read from 250-900-dpi crops by the reviewer (not printed as text anywhere in the paper;
  include only if the coordinator wants figure readings in the notes):
  - Fig. 2 (cluttered): PAC-NMPC quadratic terminal cost 76% reached / 24% did not reach; PAC-NMPC naive A* 89% / 4% did not reach /
    7% obstacle violation; actor policy 90% / 3% did not reach / 1% velocity violation / 6% obstacle violation; MPPI learned value
    function 70% / 7% did not reach / 23% obstacle violation; PAC-NMPC learned value function 97% / 3% did not reach.
  - Fig. 5 (concave traps): quadratic 47% / 53% did not reach; naive A* 91% / 4% did not reach / 5% obstacle violation; actor policy
    82% / 2% did not reach / 1% velocity violation / 15% obstacle violation; MPPI learned value function 55% / 9% did not reach /
    36% obstacle violation; PAC-NMPC learned value function 93% / 7% did not reach.
  - Fig. 8 (fixed-wing): quadratic 72% / 9% altitude violation / 19% obstacle violation; actor policy 92% / 3% altitude / 5% obstacle;
    PAC-NMPC learned value function 96% / 4% obstacle; PAC-NMPC learned bicycle value function 98% / 2% obstacle.
  - Fig. 9 (fixed-wing, additional noise): quadratic 54% / 20% altitude / 26% obstacle; actor policy 80% / 6% altitude / 14% obstacle;
    learned value function 89% / 11% obstacle; learned bicycle value function 93% / 7% obstacle.
  - Fig. 10 (hardware): actor policy 85% reached / 15% obstacle violation; PAC-NMPC learned value function 95% / 5% did not reach;
    actor policy mismatch 70% / 30% obstacle violation; PAC-NMPC learned value function mismatch 80% / 20% did not reach.
- Navigation headings (as emitted): `# Robust Perception-Based Navigation using PAC-NMPC with a Learned Value Function`;
  `## I. INTRODUCTION`; `## II. RELATED WORK`; `## III. BACKGROUND` (`### A. PAC-NMPC`, `### B. Actor Critic Reinforcement Learning`);
  `## IV. APPROACH` (`### A. Problem Formulation`, `### B. Learned Value Function`, `### C. PAC-NMPC with Learned Value Function`);
  `## V. SIMULATION EXPERIMENTS` (`### A. Experimental Setup`, `### B. Cluttered Environments`, `### C. Concave Trap Environments`,
  `### D. Fixed-wing UAV`); `## VI. HARDWARE EXPERIMENTS`; `## VII. DISCUSSION & CONCLUSION`; `## REFERENCES`.
  The subsection letters repeat (A, B, C under III, IV and V); if navigation needs unique anchors, the parent section number has to be
  added by the builder (I did not change the printed headings). The compact builder will drop the page-2 title as a duplicate of the
  generated title once the plan title is set. The copyright notice (page 1) precedes the title in the output.
- Asset names: `figure-1` ... `figure-10`, unique in the document; no clash possible (single reviewer). No `reading_order` entry in
  `plan.json` is needed: floats were ordered inside each page file.
- Affiliation notes on page 2: the author line carries `$^{1,2}$`-style superscripts and the two `\thanks` affiliation/e-mail
  notes follow it as text items starting with `$^{1}$` / `$^{2}$`. I did not convert these to the `[^n]` / `Footnote n:` convention
  added later, because they are author-affiliation marks ("1,2" combined), not footnotes in running text; the paper has no
  running-text footnotes. If the coordinator prefers the footnote form, only `p0002-b001`, `p0002-b008` and `p0002-b011` change.

### Limitations
- Text inside the ten figures (legends, axis labels, percentages) is not searchable; it exists only in the image crops.
- Line coverage cannot be reported as `OK` for pages 3-7 because the mathematics is LaTeX; these pages rely on the visual
  comparison with crops, the pdflatex rendering comparison and the adjudication notes.
- Italic emphasis of venue names in the references is written with `*...*`; punctuation and spacing of the references come from
  `main.bbl` (the verifier checks letters and digits only).
- "1/10th" (pages 2 and 7) is written with a plain "th" where the PDF has a superscript ordinal.

### Notes on the brief
- The footnote rule ("at the end of that page's items") conflicts with "the page ends with the prose that continues onto the next
  page"; the coordinator's later convention (before the last continuing paragraph) resolves it.
- For multi-line equation groups with a single printed number the brief leaves the form open; I used "tag on the printed line plus
  adjacent aligned block". A single convention across reviewers would help.
- `check` reports U+2212 versus ASCII minus as a number difference on every page with negative numbers or `N-1` subscripts in LaTeX;
  normalising the minus sign in `number_tokens` would remove most of the remaining noise.
- An ink-extent helper for figure boxes and a pdflatex syntax check of the page maths were worth having
  (`_scratch/pacvf-1-9/ink2.py`, `texchk.py`); a rendered crop viewed at reduced size can look clipped when it is not.
