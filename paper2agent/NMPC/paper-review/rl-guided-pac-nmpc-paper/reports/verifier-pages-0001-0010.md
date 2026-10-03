# Independent verifier report: RL-Guided PAC-NMPC, PDF pages 1-10

Status: COMPLETE.

- Package (PKG): `/home/jixia/AI_agents/paper2agent/NMPC/staging/rl-guided-pac-nmpc-paper-s1`
- Source (DOC): `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/rl-guided-pac-nmpc-paper/documents/s001-rl-guided-pac-nmpc/source.pdf` (arXiv:2609.39854v1, 20 pages)
- Range: PDF pages 1-10 = `references/paper.md` lines 1-434 (everything before "A. Fixed-wing Dynamics and Depth Camera Sensor"), plus `SKILL.md`, `references/index.md` (all rows) and the "Conversion notes" at the end of `paper.md`.
- Scratch: `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/_scratch/verify-rl-1-10/` (page renders, crops, diff scripts and their outputs).
- Nothing in the package or the review plans was changed. The reviewers' reports were not read.

Result: 2 errors, 5 minors. All of them are in `index.md`, the conversion notes and the Markdown rendering of three tables. The transcription of pages 1-10 itself (prose, definitions, equations (1)-(23), Algorithm 1, Tables I-IV, Figures 1-7, captions) has no discrepancy that I could find.

## Coverage (what was actually done)

| Check | Pages | Method | Sampled? |
|---|---|---|---|
| Prose, word level | 1-10 | Native PDF text extracted column by column (`pdftotext`), compared with `paper.md` lines 1-434 by a token diff: all words, all bracketed citation numbers, all percentages and numbers in prose (`wdiff2.py`, `wdiff3.py`). Every reported difference was read; all are maths (stripped on the package side), float placement, small-caps headings or Markdown markers. | No, complete |
| Prose, punctuation | 1-10 | Character-level diff with whitespace and hyphens removed (`cdiff.py`); the only small differences are Markdown markers (`##`, `*a priori*`, table pipes). | No, complete |
| Display equations (1)-(23) and the unnumbered display of Def. III.6 | 5-9 | Each compared symbol by symbol with crops at 280-320 dpi. | No, all 24 |
| Inline maths | 5-10 | Every inline formula read against the same crops (pages 2-4 contain no maths). | No, complete |
| Definitions III.1-III.6 and IV.1-IV.4 | 5-6 | Label, title, statement and order against crops. | No, all 10 |
| Algorithm 1 | 7 | PDF crop at 320 dpi vs `assets/figure/algorithm-1.jpg` vs the nine transcribed lines. | No, complete |
| Tables I-IV | 4, 9, 10 | Every CSV cell and every Markdown table cell against crops at 260-330 dpi; bold cells against the list in the conversion notes. | No, all cells |
| Figures 1-7, Algorithm 1 image | 2, 7-10 | Every JPEG opened; completeness, absence of caption or body text, legibility; captions against the PDF. | No, all 8 |
| LaTeX well-formedness | 1-10 | Script: `$` parity, brace balance, `\left`/`\right`, `\begin`/`\end`, sequence of `\tag`. | No, complete |
| Structure | 1-10 | Headings and levels, paragraph breaks, column and page joins, footnotes, extraction damage. | Joins: all 9 page boundaries and all column changes that split a sentence |
| `index.md` | all rows | Every "Exact heading" matched against the headings of `paper.md` by script; every "Look here for" text checked against `paper.md` and the PDF text. | No, all rows |
| Conversion notes, `SKILL.md` | n/a | Each statement checked against the PDF or the package. Statements about pages 11-20 were checked only as far as noted below. | Partly (see below) |
| References | 18-20 | Not in my range. Only the in-text citation numbers of pages 2-10 were verified (by the token diff), plus entries [45], [46] because of the Table I / text citation difference. | Not checked |

## Findings

| # | Severity | PDF page | Item id | Package says | PDF shows | Suggested fix |
|---|---|---|---|---|---|---|
| 1 | error (wrong pointer) | 11-17 (index rows) | `references/index.md` rows "VII. FIXED-WING UAV ..." and "D. Simulation Experiment" | Row VII: "Parent of the fixed-wing subsections A-E; Tables V-VII". Row "D. Simulation Experiment": "Under VIII: experiment supporting the analysis, Tables VIII-IX". | Tables VIII ("Out Of Distribution Experiment Results") and IX ("Fixed-wing aerial vehicle hardware results") belong to Section VII (VII-D and VII-E). `paper.md` itself has them there (lines 634 and 672). Section VIII-D contains no table; it cites Fig. 17 and Fig. 18. | Row VII: "Tables V-IX". Row "D. Simulation Experiment": replace "Tables VIII-IX" by "Figs. 17-18". Optionally add "Table IX" to the row "E. Hardware Experiments". |
| 2 | error (unsupported statement) | 1 | `plan.json` `notes[0]` (first bullet of "Conversion notes", `paper.md` line 994) | "Preprint under review." | Nothing of the kind is printed anywhere in the PDF. Page 1 carries only "©2026 IEEE. Personal use of this material is permitted. ..." and the arXiv stamp. The statement is therefore unsupported by the source. To my knowledge that notice is the wording IEEE asks for on accepted papers (papers still under review carry a different "submitted to the IEEE for possible publication" notice), so the statement is probably also wrong; I could not confirm the status from the PDF. | Delete "Preprint under review." or replace it by what the PDF shows: "PDF page 1 carries an IEEE copyright notice (©2026 IEEE); the publication venue is not stated." |
| 3 | minor (rendering, search) | 9, 10 | p0009-b015 (Table II), p0010-b003 (Table III), p0010-b010 (Table IV) | The Markdown pipe tables in `paper.md` lines 375, 378, 401, 404, 425, 427 contain doubled backslashes: `$V^{\\boldsymbol{\\phi}\\boldsymbol{\\psi}}$`. | $V^{\boldsymbol{\phi}\boldsymbol{\psi}}$. The CSV files and the `rows` of the page plans have the correct single-backslash form, so the doubling is added by the builder when it writes table cells. | Emit single backslashes inside `$...$` in Markdown table cells. Everywhere else in `paper.md` inline maths uses single backslashes, so the table rows are inconsistent, break in renderers that protect maths, and are missed by `rg -F 'V^{\boldsymbol{\phi}'`. The same defect is at line 525 (Table V header, `$\\delta_1$`), outside my range. |
| 4 | minor (index omission) | 9, 12 | `references/index.md` | No row for "C. Sensor Prediction". The rows for Section VI are A, B, D, E and for Section VII are A, B, E. | The heading "C. Sensor Prediction" is printed in both VI and VII and exists twice in `paper.md` (lines 338 and 511). It holds Equations (20)-(23) and Fig. 4 for the rally car, and the depth-image prediction model with Table V for the fixed-wing. | Add a row like the existing one for "D. Simulation Experiments": "C. Sensor Prediction: heading occurs under VI (geometric LiDAR prediction, Eqs. (20)-(23)) and again under VII (learned depth-image prediction, Table V)". |
| 5 | minor (index wording) | 5 | `references/index.md` row "III. PROBLEM FORMULATION" | "Definitions III.1-III.6: stochastic dynamics, sensing, policy, cost, constraint, and the probabilistic safety problem" | The six definitions are Stochastic Dynamics, Sensor Measurement, Observation, Stage Cost, Stage Constraint, Probabilistic Safety Guarantee. Section III defines no policy. | Replace "policy" by "observation" and "probabilistic safety problem" by "probabilistic safety guarantee". |
| 6 | minor (incomplete list in notes) | 5-6 | `plan.json` `notes[2]` (third bullet of the conversion notes) | "Definitions, lemmas and theorems carry their printed labels in bold (Definition III.1-III.6, Lemma VIII.1-VIII.2, Theorem VIII.1-VIII.2, Definition VIII.1-VIII.2)." | The paper and `paper.md` also contain Definitions IV.1-IV.4 (Trajectory Cost, Trajectory Constraint Violation Indicator, Optimal Value Function, Optimal Policy), with bold labels, on PDF pages 5-6. | Add "Definition IV.1-IV.4" to the list. |
| 7 | minor (boilerplate) | n/a | `references/index.md` "Assets" section | Lists `assets/supp_figs/` and `assets/supp_table/`. | These directories do not exist in the package (no supplement was supplied; `supplement.md` says so). `assets/figure/` also holds `algorithm-1.jpg`, which the list describes as "main figures" only. | Drop the two supplementary directories from the list or mark them "(none for this paper)"; mention the algorithm image. |

Notes on severity: finding 1 does not alter the paper text but sends a reader who looks for Tables VIII-IX to a section that has none. Finding 2 is a statement about the paper that the source does not make. Finding 3 is cosmetic for a human reader of the raw text but breaks rendering and exact-string search for the symbol in three tables.

## Checked and found correct

**Page 1.** Copyright paragraph identical to the PDF. The rotated arXiv stamp is omitted from the text and reported in the notes with the correct identifier and date (arXiv:2609.39854v1 [cs.RO], 30 Sep 2026).

**Page 2.** Title (emitted once at the top; the page-2 title is intentionally omitted from the page text). Author line with affiliation superscripts 1,2 / 2 / 2 / 2 / 2 / 1,2. Footnotes 1 and 2. E-mail addresses, including the printed `jh.edu` domain of two of them. Abstract and Index Terms word for word. Section I paragraphs 1-4 and the join to page 3. Fig. 1 image complete, caption exact.

**Page 3.** Rest of Section I; the four contributions (item 2 has no final full stop in the PDF and none in the package). II, II-A, II-B headings and text; citation numbers [6]-[22].

**Page 4.** II-B (rest), II-C, II-D, II-E text; citations [23]-[55]. Table I: 8 rows by 6 columns, every tick and cross, "(5×a)*", "(12×2)", "(16, 84×84×9)", "(16×12)", the footnote and the caption. The table prints "AC-MPC[46]" while the text prints "Actor Critic MPC [45]"; the package reproduces both as printed.

**Page 5.** End of II-E. Section III: Definitions III.1-III.6 complete and in order, including $\ell(\mathbf{x}_t,\mathbf{u}_t) \succ 0$, $c:\mathcal{X}\times\mathcal{U}\times\mathcal{Y}^{N_y}\mapsto\mathbb{R}$, $\mathbf{y}_{(t-N_y):t}$, and the unnumbered double-probability display of Definition III.6 with $\beta_{\mathcal{S}}$, $\delta_{\mathcal{S}}$, $N_T$. The printed "represent for the robot's observation" is kept. Section IV, IV-A: trajectory $\boldsymbol{\tau}$, $\mathcal{T}\subset\mathcal{X}^{N_T+1}\times\mathcal{U}^{N_T}$, Definitions IV.1 and IV.2, Equations (1) and (2), TVLQR paragraph with the non-bold $f$ in $\mathbf{x}^d_{t+1}=f(\mathbf{x}^d_t,\mathbf{u}^d_t)$ and $\mathbf{u}_t=\mathbf{K}_t(\mathbf{x}^d_t-\mathbf{x}_t)+\mathbf{u}^d_t$.

**Page 6.** Equation (3) (objective with $\gamma$, both chance constraints with $1-\delta$), (4), (5), (6), (7), (8) with the printed unbalanced parenthesis, (9), (10). IV-B: Definitions IV.3 and IV.4, Equations (11) and (12), $\beta\in(0,1)$, $Q^{\boldsymbol{\psi}}$, $Q^*$, $\boldsymbol{\pi}^{\boldsymbol{\phi}}$, $V^{\boldsymbol{\phi}\boldsymbol{\psi}}(\mathbf{x}_t)=Q^{\boldsymbol{\psi}}(\mathbf{x}_t,\boldsymbol{\pi}^{\boldsymbol{\phi}}(\mathbf{x}_t))$, citations [64]-[67]. Section V introduction, $\hat{\mathbf{y}}_{t+k}=\mathbf{h}^\eta(\mathbf{x}_t,\mathbf{y}_t,\mathbf{x}_{t+k})$, the three-item list.

**Page 7.** Fig. 2 image complete (legend row included), caption exact. V-A text, with bold $\mathbf{f}$ here as printed. Algorithm 1: image identical to the PDF; transcription matches line by line (Input, lines 1-9, the loop range $i=t,\cdots,t+N_T-1$, the test $c(\mathbf{x}_{i+1},\hat{\mathbf{u}}_{i+1},\mathbf{y}_{(t-N_y):t})>0$, the final $\boldsymbol{\mu}=(\hat{\mathbf{u}}_t,\cdots,\hat{\mathbf{u}}_{t+N_T-1})$). V-B: Equations (13) and (14), $l\in\{1,\cdots,L\}$, citations [36], [68], [69].

**Page 8.** End of V-B. V-C: Equations (15), (16), (17) (with $\min_{\alpha>0}$, $\epsilon_c$, the full stop after the first constraint and the comma after the second), the inline $\mathbb{E}[\,\cdot\,]<0$ expression, [6], SNOPT [70]. Section VI heading and introduction. Figs. 3 and 4 complete, captions exact. VI-A: state and input vectors, Equation (18), $l=0.33\,\mathrm{m}$, $\boldsymbol{\Sigma_f}=diag([4\mathrm{e}^{-4},4\mathrm{e}^{-4},1.1\mathrm{e}^{-2},1\mathrm{e}^{-1},5.6\mathrm{e}^{-3}])$, limits $[-1.,1]$ m/s², $[-1,1]$ rad/s, $[-0.4,0.4]$ rad, 64 beams, 360°. VI-B: Equation (19), $\gamma_c=1000$.

**Page 9.** VI-B second paragraph (two hidden layers, 256 neurons, 10% dropout). VI-C: Equations (20)-(23) with the nested subscripts and the printed bracket of (21); "360$^o$". VI-D: both quadratic terminal costs, $\mathbf{Q}_f=diag([1\ 1\ 0\ 0\ 0])$, $v_{max}\cdot N_T\cdot\Delta t$, non-bold $\phi$ in $\boldsymbol{\pi}^{\phi}(\mathbf{x})$, $\mathbf{Q}=diag([1\mathrm{e}^{-2}\ 1\mathrm{e}^{-2}\ 0\ 0\ 0])$, $v\in[-1,3]$ m/s, 0.5 m, 12 timesteps, $\Delta t=0.1$, $H=0.2$, $L=5$, $M=1024$, $\delta=0.05$, $\gamma=2$ and $4$, $\gamma_t=0.35$, $\Sigma_\epsilon=0.01$, 50Hz, i-9-13900H, RTX 4080. Table II: all 15 numeric cells and the labels; Fig. 5 complete (both panels, axes, legend), caption exact.

**Page 10.** Fig. 6 complete, caption exact. Paragraphs with 1024, 5%, 0.34%, 65.49%, 1.45%, $\pm\frac{\pi}{2}$, 100 environments. Table III: all 15 numeric cells. VI-E: 1/10th, 20 environments, 8 obstacles, 8 m by 6 m, 0.5 m wheelbase. Fig. 7 complete, caption exact. Table IV: all 12 numeric cells. Section VII heading and the start of its first paragraph, which continues correctly onto page 11.

**Bold cells listed in the conversion notes (Tables II-IV).** All correct and complete against the crops: Table II 3% / 0% / 97%, 3%, 0%; Table III 2% / 0% / 93%, 0%; Table IV 0% / 95%, 0% / 0% / 0%.

**Other statements of the conversion notes.** Correct: page offset of one; no author biographies in the PDF text; equation numbers run to (52) in both PDF and package; the peculiarities of Equations (8) and (21) are reproduced; subsection letters and the duplicated headings; the run-in titles; the repeated "Approach" header and "PAC-NMPC" label in the CSVs of Tables II, III, VI, VIII, IX; Algorithm 1 as image plus transcription; subscripts in Fig. 2 ($\mathbf{h}_\eta$, $\boldsymbol{\pi}_\phi$, $Q_\psi$). Not checked: the statement about the missing `.bbl`.

**`index.md`.** All 26 main-paper headings exist exactly in `paper.md` ("D. Simulation Experiments" twice, as the row says). "REFERENCES, 78 entries" agrees with 78 numbered entries. Apart from findings 1, 4, 5 and 7 the descriptions are accurate.

**`SKILL.md`.** Front matter name and title correct; the instructions are generic and contain nothing false about this paper.

**Structure.** Heading levels consistent (`##` sections, `###` subsections); no invented or missing heading in the range; no duplicated text; all page and column joins read continuously; no extraction damage (`<sup>`, glyph remnants, split decimals, unbalanced `**`); all 24 display blocks are balanced; 23 carry `\tag{1}` to `\tag{23}` in order and one (Definition III.6) is unnumbered, as printed.

## Observations outside my range (not verified, for the other verifier)

- `paper.md` lines 824-830 place Figs. 17 and 18 between the two paragraphs of "IX. CONCLUSION", although they are cited in VIII-D.
- The conversion notes record bold cells for Tables II-IV and say that Tables VI-IX are not recorded; Table V is not mentioned either way.

## Technical question answered from the package only

**Question.** Which optimisation problem does AC-PAC-NMPC solve at each replanning step, how does the value-function improvement enter it, and with which settings was it run in the rally-car simulations?

**Answer (from `paper.md`, "C. Uncertainty-Aware Value Function Improvement Constraint" and "D. Simulation Experiments" under VI).** The method introduces a third PAC bound ${\mathcal{C}_{\mathcal{V}}}^+_\alpha(\boldsymbol{\nu})$ on the learned value function at the terminal state, with $\mathbb{P}(\mathbb{E}[V^{\boldsymbol{\phi}\boldsymbol{\psi}}(\mathbf{x}_{t+N_T},\hat{\mathbf{y}}_{t+N_T})]\le{\mathcal{C}_{\mathcal{V}}}^+_\alpha(\boldsymbol{\nu}))\ge 1-\delta$ (Eq. 15). The problem solved is $\boldsymbol{\nu}^*=\arg\min_{\boldsymbol{\nu}}\min_{\alpha>0}(\mathcal{J}^+_\alpha(\boldsymbol{\nu})+\gamma\,\mathcal{C}^+_\alpha(\boldsymbol{\nu}))$ subject to $\mathcal{C}^+_\alpha(\boldsymbol{\nu})\le\epsilon_c$ and ${\mathcal{C}_{\mathcal{V}}}^+_\alpha(\boldsymbol{\nu})\le\mathbb{E}[V^{\boldsymbol{\phi}\boldsymbol{\psi}}(\mathbf{x}_t,\mathbf{y}_t)]$ (Eq. 17). Both bounds are hard constraints; the constraint-violation bound also stays in the objective as a penalty so that it can be pushed below $\epsilon_c$. The problem is solved with SNOPT. In the rally-car simulations: 12-timestep trajectories, $\Delta t=0.1$ s, replanning period $H=0.2$ s, $L=5$ prior policies, $M=1024$ samples per prior, $\delta=0.05$, $\gamma=2$ (cluttered) and $\gamma=4$ (concave traps), policies interpolated to 50 Hz, RL warm start not used. With sampled dropout masks the expected-cost bound was never violated and the constraint-violation bound was violated in 0.34% of planning intervals; without them the figures are 65.49% and 1.45%.

**Check against the PDF.** Equations (15)-(17) and the surrounding text agree with the crop of PDF page 8 (left column); the settings agree with PDF page 9 (right column); the violation percentages agree with PDF page 10 (left column). The answer is correct.
