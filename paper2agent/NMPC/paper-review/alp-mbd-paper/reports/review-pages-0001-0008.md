# Review report: alp-mbd-paper, pages 1-8 (reviewer alp-mbd-r1, brief v2)

Paper: "Adaptive Linear Path Model-Based Diffusion" (ALP-MBD), Shimizu and Tomizuka, arXiv:2602.02831v1, 8 pages, IEEE conference layout.
DOC: /home/jixia/AI_agents/paper2agent/NMPC/paper-review/alp-mbd-paper/documents/s001-alp-mbd
TeX aid: /home/jixia/AI_agents/paper2agent/NMPC/tex-source/alp-mbd (main.tex, math_commands.tex, reference.bib; read only, nothing compiled or executed). Macros \gS, \gA, \gR expanded to \mathcal{S}, \mathcal{A}, \mathcal{R}.

## Final state

All 8 pages are finished: `reviewed: true` and `review_notes` starting with `[v2]`. No page is left unmarked.
Adjudication notes are in `DOC/adjudication-notes/page-0002.json` to `page-0008.json`. Page 1 has no diagnostics.

| Page | check | Remaining diagnostics (all category (a)) |
| --- | --- | --- |
| 1 | OK, 102/102 | none |
| 2 | 85/103 | 18 lines with inline/display maths; minus glyph in 10^{−4}, 10^{−2}, T−1 |
| 3 | 81/115 | 34 maths lines ((5)-(16) and inline); 8 'i−1' minus glyphs |
| 4 | 73/99 | 26 maths lines ((17), (19), calligraphic MDP symbols) |
| 5 | 77/93 | 16 maths lines; minus glyph in 10^{−2}, 10^{−4}; extra numbers from the Algorithm 1 transcription (its source lines are inside the excluded image box) |
| 6 | 86/104 | 18 maths lines ((21), (22), inline); second parser glues adjacent Table I cells |
| 7 | 118/121 | 3 maths lines ($T$, $\sigma_{\max}$); second parser glues adjacent Table II cells |
| 8 | 172/172 | number check only: rejoined DOI URL of [21] (10.4 + 8550 -> 10.48550) |

No category (b) diagnostic remains.

## Items per page (assets, equations)

- Page 1: title, author line, affiliation footnote, abstract, `## I. INTRODUCTION`, contributions 1) and 2). arXiv stamp omitted (`p0001-b000`). No page numbers are printed in this paper.
- Page 2: contribution 3); Fig. 1 `figure-1` [51,127,292,187] + caption; `## II. RELATED WORK`; `## III. LINEAR PATH MODEL-BASED DIFFUSION`; `### A. Variance Preserving Model-Based Diffusion`; equations (1a), (1b), (1c) (one block per tag), (2), (3), (4).
- Page 3: equations (5) (aligned, one tag), (6) (aligned, \underbrace{...}_{\text{(importance-weighted average)}}), (7), (8), (9), (10), (11), (12) (aligned, underbrace), (13), (14), (15), (16); `### B. Linear Path Model-Based Diffusion`.
- Page 4: `### C. Differences between VP-MBD and LP-MBD`; `## IV. ADAPTIVE LINEAR PATH MODEL-BASED DIFFUSION`; `### A. Formulation as a Reinforcement Learning Problem`; equations (17) (aligned, one tag), (18), (19); Fig. 2 `figure-2` [313,474,559,615] + caption; `### B. Implementation Details`.
- Page 5: Algorithm 1 `algorithm-1` [52,230,301,429] + text transcription; `## V. EXPERIMENTS`; `### A. Numerical Experiments`; equation (20) (aligned, one tag).
- Page 6: Fig. 3 `figure-3` [49,94,304,288] (3x3 grid, three extractor pictures merged) + caption; Fig. 4 `figure-4` [49,334,304,504] (2x3 grid) + caption; `### B. Evaluation of LP-MBD`; Table I caption item + `table-1` [313,235,561,306]; `### C. Evaluation of ALP-MBD`; equations (21), (22) (aligned, one tag each).
- Page 7: Table II caption item + `table-2` [55,675,299,722]; Fig. 5 `figure-5` [308,45,563,133] + caption; Fig. 6 `figure-6` [308,181,563,275] + caption; `## VI. CONCLUSIONS`; `## REFERENCES`; [1]-[4].
- Page 8: references [5]-[41].

Every figure box was checked with `crop` on all four edges (panel titles, axis labels, tick labels, colour bars inside; caption excluded). Formulas kept as images: none; all 26 printed equation numbers ((1a)-(1c), (2)-(22)) are LaTeX text items with visible \tag.

## Joins

- Page 1: `p0001-b008` ('frequently leads to ...', top of right column) join_previous=space.
- Page 3: `p0003-b000` ('as VP-MBD, in order to ...') join_previous=space (continues page 2's last paragraph).
- Page 4: `p0004-b008` ('state space, ...') join_previous=space (sentence 'Here, S denotes the / state space' crosses the column break).
- Page 5: `p0005-b000` ('widespread adoption ...') join_previous=space (continues page 4).
- Page 6: `p0006-b000` ('converges more slowly ...') join_previous=space (continues page 5); `p0006-b005` ('superior performance ...', top of right column) join_previous=space.
- Page 7: `p0007-b000` ('For fair comparison, we set the planning horizon ...') join_previous=space (continues page 6).
- Range boundaries: none (single reviewer, whole paper). References do not cross pages or columns ([4] ends on page 7, [24] ends in the left column of page 8).

## Tables: bold cells (cannot be stored in CSV)

Table I (`table-1`, page 6), row label / column header / value:
- header row: all five header cells bold (Tasks, CEM, MPPI, VP-MBD, LP-MBD)
- Ant / CEM / 3.80 ± 0.43
- Hopper / LP-MBD / 2.74 ± 0.01
- HalfCheetah / LP-MBD / 2.73 ± 0.12
- Walker2D / LP-MBD / 2.36 ± 0.02
- Reacher / VP-MBD / -0.17 ± 0.04
- Reacher / LP-MBD / -0.17 ± 0.04
- Pusher / VP-MBD / -0.53 ± 0.11

Table II (`table-2`, page 7):
- header 'Methods' bold (the other header cells 'Steps $T$', '$\sigma_{\max}$', 'Reward', 'Runtime [ms]' are not bold)
- LP-MBD / Runtime [ms] / 36.9
- ALP-MBD / Reward / -3342 ± 128

Cells are strings exactly as printed: negative values use the printed ASCII hyphen-minus; '±' with one space on each side; the VP-MBD sigma_max cell of Table II is a printed '-'; maths in Table II headers in LaTeX ('Steps $T$', '$\sigma_{\max}$'), as in the sibling papers. Both captions are separate caption items placed before their tables ('TABLE I  \nPER-STEP REWARDS FOR DIFFERENT TASKS.' and 'TABLE II  \nAVERAGE SINGLE EPISODE REWARD'; small caps rendered upper case; Table II's caption has no full stop in print).

## Algorithm 1

Image crop `algorithm-1` plus a text item with the same box: first line `**Algorithm 1** Training ALP-MBD with PPO`, then lines `1:` to `13:` separated by Markdown hard breaks, **for**/**do**/**end for** in bold, one `&emsp;` per nesting level, LaTeX maths. Printed line 5 wraps after 'a_t =' and is one transcribed line. Matches main.tex and the 200-dpi crop.

## TeX versus PDF

No disagreement found: every displayed equation and the inline maths checked against 160-200-dpi crops agree with main.tex (e.g. (5) second line 1/\sqrt{\alpha_i} without a bar, as in TeX). Deliberate deviations from the TeX markup, content unchanged:
- (6), (12): TeX's `\displaystyle \text{ (importance-weighted average)}` written as `\text{(importance-weighted average)}` per the collection convention; `split` written as `aligned`.
- (20): TeX spacing `\hspace{5mm}` / `\hspace{4mm}` written as `\qquad` / `\quad`, because the digits 5 and 4 otherwise enter the number check as spurious extras.
- Reference [39] 'FreiburgimBreisgau' (no spaces) is so in both the bib and the print; kept.

## Text repairs of substance

- Line-wrap compound hyphens restored (print and TeX agree): variance-preserving (p1), finite-horizon, state-of-the-art (p2), Monte-Carlo, trial-and-error (p3), decision-making (p4), VP-MBD x3, AVP-MBD, LP-MBD’s (p5), ALP-MBD, LP-MBD (p6), VP-MBD x2, ALP-MBD x2, LP-MBD, flow-matching–inspired, sampling-based in [2] (p7), Neural-swarm2 [8], actor-critic [29], Thirty-seventh [35] (p8).
- Abstract URL rejoined: https://anonymous.4open.science/r/adaptive_linear_path_model_based_diffusion-C58C (identical to main.tex).
- Reference URLs rejoined: [7], [13], [16], [21], [22], [27], [29] (all identical to reference.bib url fields).
- 'H¨onig' -> 'Hönig' [8], 'M¨uller' -> 'Müller' [14], [17]; footnote '_{_ ... _}_' -> '{purewater0901, tomizuka}@berkeley.edu'.
- Stray '=' in 'the system = dynamics' (p2) removed; extractor 'Algorithm 1' heading merged into the transcription (p5); extractor text item '(importance-weighted average)' under (12) deleted (inside the LaTeX block) (p3).
- Reading order: reference [24] moved from the end of page 8 to after [23].

## Authors' slips kept as printed (all verified on the page)

1. Section V-A (p5): 'VP-MBD with the same parameters as in the first example (β0 = 10^{-2}, β1 = 10^{-4})', whereas III-A (p2) gives β0 = 1.0×10^{-4}, β1 = 1.0×10^{-2} and the Section V intro (p5) gives β0 = 0.0001, β1 = 0.01 (endpoints swapped).
2. III-A / III-C / IV (p3-4): the VP schedule triplet is written (β0, β1, T) with T 'the total number of diffusion steps', while (3)-(4) index diffusion steps by N, and T is the trajectory horizon in (1a)-(1c).
3. Text after (22) (p6): 'ψref and vref denote the desired yaw and velocity', but (22) uses θ_ref.
4. V-C (p7): 'This adaptivity enhances the efficiency of VP-MBD' (the paragraph is about ALP-MBD).
5. V-A (p5): 'ALP-MBD successfully discover' (agreement).
6. Minor wording: Fig. 4 caption 'The top row shows the result of VP-MBD' while the comparison is AVP-MBD vs ALP-MBD (panels titled 'VP: step = ...'); 'score-ascent–type' (en dash, p3 left) vs 'score-ascent-type' (hyphen, p3 right).

## Proposed plan notes (for plan.json `notes`, coordinator's decision)

1. "Source: arXiv:2602.02831v1 (8 pages, IEEE conference two-column layout). No supplementary material. The abstract links the authors' anonymous code repository https://anonymous.4open.science/r/adaptive_linear_path_model_based_diffusion-C58C."
2. "All displayed equations (1a)-(22) and inline maths are LaTeX transcribed from the authors' arXiv TeX source and checked against the PDF; the authors' macros \gS, \gA, \gR are expanded to \mathcal{S}, \mathcal{A}, \mathcal{R}. Multi-line equations (5), (6), (12), (17), (20), (21), (22) are single aligned blocks with one tag; (1a)-(1c) are one block per sub-number."
3. "Algorithm 1 (Training ALP-MBD with PPO) is kept as an image (algorithm-1) followed by a line-by-line text transcription."
4. "Tables I and II are stored as CSV (table-1, table-2). Bold marking of best results is lost in CSV: Table I bold = Ant/CEM 3.80 ± 0.43, Hopper/LP-MBD 2.74 ± 0.01, HalfCheetah/LP-MBD 2.73 ± 0.12, Walker2D/LP-MBD 2.36 ± 0.02, Reacher/VP-MBD and Reacher/LP-MBD -0.17 ± 0.04, Pusher/VP-MBD -0.53 ± 0.11; Table II bold = LP-MBD runtime 36.9 ms, ALP-MBD reward -3342 ± 128."
5. "Figures 1-6 are raster images; values shown only in the plots (Fig. 3-6) are not transcribed."
6. "Authors' inconsistencies kept as printed: Section V-A writes β0 = 10^{-2}, β1 = 10^{-4}, swapped relative to β0 = 1.0×10^{-4}, β1 = 1.0×10^{-2} (Section III-A) and β0 = 0.0001, β1 = 0.01 (Section V); the VP triplet (β0, β1, T) uses T for the number of diffusion steps, which (3)-(4) call N; the text after (22) says ψref where (22) has θref; 'the efficiency of VP-MBD' in V-C refers to ALP-MBD."

## Navigation list (exact heading -> content)

- `# Adaptive Linear Path Model-Based Diffusion` -> title, authors, affiliation footnote, abstract with code URL (p1).
- `## I. INTRODUCTION` -> noise-schedule tuning problem, LP-MBD and ALP-MBD in brief, contributions 1)-3), Fig. 1 (obstacle-free driving vs overtaking scenario) (p1-2).
- `## II. RELATED WORK` -> gradient-based vs sampling-based trajectory optimization, MPPI/CEM/CMA-ES, diffusion and flow matching for planning, RL with sampling-based planners, RL fine-tuning of diffusion models (p2).
- `## III. LINEAR PATH MODEL-BASED DIFFUSION` -> section overview (p2).
- `### A. Variance Preserving Model-Based Diffusion` -> trajectory optimization (1a)-(1c), target density (2), VP forward process (3)-(4), MBD denoising step (5), Monte-Carlo score estimate (6), Gaussian proposal (7), update (8), why (β0, β1, T) are coupled (p2-3).
- `### B. Linear Path Model-Based Diffusion` -> linear probability path (9)-(10), denoising step (11), score (12), proposal (13), update (14), truncation t_max (15), σ_max = t_max/(1 − t_max) (16) (p3).
- `### C. Differences between VP-MBD and LP-MBD` -> three coupled VP parameters vs two decoupled LP parameters (σ_max, T) (p4).
- `## IV. ADAPTIVE LINEAR PATH MODEL-BASED DIFFUSION` -> motivation for online adaptation; why LP-MBD suits RL (p4).
- `### A. Formulation as a Reinforcement Learning Problem` -> MDP, scheduler policy over (T, σ_max) with categorical × Gaussian factorization (17), step-penalized reward (18), RL objective (19), Fig. 2 (architecture) (p4).
- `### B. Implementation Details` -> PPO choice, Algorithm 1 (p4-5).
- `## V. EXPERIMENTS` -> goals (i)-(iii), RTX 4090, default β0 = 0.0001, β1 = 0.01, σ_max = 1.8 (p5).
- `### A. Numerical Experiments` -> 1D examples (Fig. 3), proposal standard deviations for T = 2 (20), T = 5 case (0.16 vs 1.8); 2D constrained Gaussian mixture, REINFORCE, AVP-MBD vs ALP-MBD (Fig. 4; learned β0 = 0.000028, β1 = 0.361, T = 3 vs σ_max = 2.11, T = 3) (p5-6).
- `### B. Evaluation of LP-MBD` -> Brax tasks, Table I (CEM, MPPI, VP-MBD, LP-MBD per-step rewards over 5 seeds), Pusher discussion (p6).
- `### C. Evaluation of ALP-MBD` -> mobile-robot trajectory tracking, kinematic model (21), reward (22), RL state, H = 50 and 100 samples, Python/PyTorch, Table II (steps T, σ_max, reward, runtime), Fig. 5 (S-shaped path), Fig. 6 (oval path, generalization) (p6-7).
- `## VI. CONCLUSIONS` -> summary (p7).
- `## REFERENCES` -> [1]-[41] (p7-8).

## Asset names

figure-1, figure-2, figure-3, figure-4, figure-5, figure-6, algorithm-1, table-1, table-2. No clashes (single reviewer, single source).

## Limitations

- Plot contents of Fig. 3-6 (trajectories, colour-coded T and σ_max) exist only as images.
- Bold in Tables I and II is recorded here and in the page notes, not in the CSV.
- The Markdown has not been rendered (no build run, per the hard limits); LaTeX uses only standard commands (aligned, underbrace, substack, mathcal, mathbb, mathbf, tfrac, \!, \;), which KaTeX and MathJax support.

## Notes on the brief and the assignment

- The brief says that page-1 footnotes go at the end of the page or before the last paragraph; the assignment says the affiliation footnote follows the author line. I followed the assignment (the brief also allows this for an author/affiliation footnote).
- `check` counts numbers in an algorithm's text transcription as extras, because the source lines lie inside the excluded image box. Every paper with an algorithm will show these; the coordinator could treat them as category (a) by default.
- Spacing commands with digits (`\hspace{5mm}`) create spurious number extras; a collection rule ("prefer \quad/\qquad over \hspace{..mm}") would avoid this.
- Category (a) does not explicitly name rejoined URLs (number check on page 8); I treated the convention-mandated rejoin as acceptable and explained it in the adjudication note.

## Progress log

- Page 1: done, reviewed, `[v2]`. check OK (102/102). Title, authors, affiliation footnote (no marker, after author line), abstract with rejoined URL, I. INTRODUCTION start, contributions 1)-2). Join: right-column 'frequently leads ...' has join_previous=space. Repair: 'variancepreserving' -> 'variance-preserving'. arXiv stamp omitted.
- Page 2: done, reviewed, `[v2]`. Fig. 1 (`figure-1`, two extractor panels merged, bbox [51,127,292,187]) + caption; II. RELATED WORK; III heading; III-A start; equations (1a), (1b), (1c), (2), (3), (4) as LaTeX blocks. Repairs: finite-horizon, state-of-the-art, stray '=' removed. Last paragraph continues on page 3 (join set on page 3). Diagnostics: 18 missing lines + minus-glyph number differences, all category (a); adjudication note written.
- Page 3: done, reviewed, `[v2]`. First item joins page 2 (join_previous=space). Equations (5)-(16) as LaTeX blocks ((5), (6), (12) aligned with one tag; underbrace kept in (6), (12)); '### B. Linear Path Model-Based Diffusion'. Repairs: Monte-Carlo, trial-and-error. Slip noted: (β0, β1, T) with T = number of diffusion steps vs N in (3)-(4). Diagnostics: 34 maths lines + 8 '−1' minus glyphs, category (a); adjudication note written.
- Page 4: done, reviewed, `[v2]`. III-C, IV heading, IV-A, (17)-(19) as LaTeX, Fig. 2 (`figure-2`, bbox [313,474,559,615]) + caption, IV-B start. Joins: right column 'state space, ...' join_previous=space (sentence crosses column). Last paragraph continues on page 5. Repair: decision-making. Diagnostics: 26 maths lines, category (a); adjudication note written.
- Page 5: done, reviewed, `[v2]`. First item joins page 4 (space). Algorithm 1 (`algorithm-1`, bbox [52,230,301,429]) + transcription; V. EXPERIMENTS; V-A; (20) as aligned LaTeX (\hspace{5mm}/\hspace{4mm} -> \qquad/\quad). Repairs: VP-MBD x3, AVP-MBD, LP-MBD’s. Slips kept: β0 = 10^{-2}, β1 = 10^{-4} (swapped), 'successfully discover'. Last paragraph continues on page 6. Diagnostics category (a): 16 maths lines; numbers = minus glyphs + Algorithm 1 transcription numbers; adjudication note written.
- Page 6: done, reviewed, `[v2]`. First item joins page 5 (space). Fig. 3 (`figure-3`, 3 extractor pictures merged, [49,94,304,288]) + caption; Fig. 4 (`figure-4`, [49,334,304,504]) + caption; V-B; right-column 'superior performance ...' join_previous=space; Table I caption (before table) + `table-1`; V-C; (21), (22) LaTeX. Repairs: ALP-MBD, LP-MBD hyphens. Slip kept: ψref vs θ_ref. Last paragraph continues on page 7. Diagnostics (a): 18 maths lines; second-parser glued table cells.
- Page 7: done, reviewed, `[v2]`. First item joins page 6 (space). Table II caption (before table) + `table-2`; Fig. 5 (`figure-5`) + caption; Fig. 6 (`figure-6`) + caption; VI. CONCLUSIONS; REFERENCES heading; [1]-[4] all checked character by character. Repairs: VP-MBD x2, ALP-MBD x2, LP-MBD, flow-matching, sampling-based. Slip kept: 'the efficiency of VP-MBD'. Diagnostics (a): 3 maths lines; second-parser glued Table II cells.
- Page 8: done, reviewed, `[v2]`. References [5]-[41], all 37 checked character by character; [24] moved after [23]; umlauts, hyphens (Neural-swarm2, actor-critic, Thirty-seventh) and seven split URLs repaired. check: 172/172 lines; only number difference is the rejoined DOI of [21] (category (a)); adjudication note written.
- Self-check over all pages: no `<sup>`, `�`, `¨`, `_ _`, `** **`, glyph-soup italics or unbalanced `$`; item ids unique; every join follows a text/caption item; table rows rectangular string arrays.
