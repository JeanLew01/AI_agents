# D-MPC (d-mpc-paper), review of pages 16-21 (Appendices A-J)

Reviewer brief: version 2. DOC = `paper-review/d-mpc-paper/documents/s001-d-mpc`.
TeX source used for the maths: `tex-source/d-mpc/appendix.tex` (macros from `macros.tex`; `\Dsarsa` from `method2.tex`).
Macro expansion used throughout: `\vs`, `\va`, `\vh` (`\bm{.}`) -> `\boldsymbol{.}`; `\vA` -> `\mathbf{A}`; `{\bm R}` -> `\boldsymbol{R}`;
`\Dsarsa` -> `\mathcal{D}'`; `\data` -> `\mathcal{D}`; `\model` -> `\mathcal{M}`; `\dynamics` -> `p_d`; `\proposal` -> `\rho`;
`\future` -> `F`; `\past` -> `H`; `\Nsamples` -> `N`; `\rewardfn` -> `R`; `\valuefn` -> `V`.
Page furniture on every page: running header "Published in Transactions on Machine Learning Research (05/2025)" and the page number, both `omit` with a reason.

## Page log

### Page 16 (Appendix A, start of Appendix B): reviewed [v2]
- Headings: `## A Algorithms for model learning`, `## B The MBOP-TrajOpt Algorithm`.
- Three Appendix A paragraphs: inline maths rewritten in LaTeX from appendix.tex, checked on a 200-dpi crop.
- Algorithm 3 (`algorithm-3`, bbox [60,410,544,517]) and Algorithm 4 (`algorithm-4`, bbox [60,541,544,654]): image crops plus line-numbered LaTeX transcriptions (bold printed title first, plain line numbers 1-6 as in the pac-nmpc transcriptions; the indented continuation of Algorithm 4 line 2 starts with `&emsp;`), checked on 260-dpi crops.
- Printed oddities kept and listed in review_notes: $\sqrt{\alpha_k}x_{t-1}$ in the forward process (probably $x_{k-1}$); Algorithm 4 line 2 $\boldsymbol{s}_{t+1:t+f_F}$; prose $s_{t+1:t+f}$ (lowercase f); "by minimize"; "In Algorithm 3 and Algorithm 4, we present the multi-step and single-step training" (order reversed relative to the algorithms).
- Joins: none needed. Page ends with the complete Appendix B intro sentence; Algorithm 5 starts page 17.
- check: ATTENTION, 8 missing lines + number differences, all category (a) (maths in LaTeX, minus glyph, algorithm transcription line numbers). Adjudication note written.

### Page 17 (Algorithm 5, Appendix C, first part of Appendix D): reviewed [v2]
- Headings: `## C Detailed ablation study results`, `## D Normalizing state coordinates`.
- Algorithm 5 (`algorithm-5`, bbox [58,83,544,315]): image crop + 15-line transcription (plain line numbers, one `&emsp;` per loop level, no `end for` because none is printed), checked on a 240-dpi crop. Printed oddities kept: $\mathbf{A}_{N,H} = 0$ (H, not F), $K$ and $\beta$ not among the Def arguments.
- Table 4 (`table-4`, bbox [73,395,540,478]): 8 x 9 string cells; two-level header flattened as `MS Diff Action Proposal: SS Diff Dynamics` etc. (parent repeated; conversion note); `Average` spans Domain Name + Level in print, stored as `Average` + empty Level cell. Every cell checked at 400 dpi; inconsistent `(±0.17)` / `(± 2.67)` spacing in the D-MPC column kept as printed. Caption separate.
- Appendix D: $\mathcal{D}$ and $\hat{F}_k(t)$ displays converted from formula images to unnumbered `$$...$$` items; $\mathcal{S}_k$ with the double `\bigcup\limits` kept inline as printed. Printed oddities kept: $r^2_{1:T_1}$, $r^m_{1:T_2}$, no comma after `\ldots`; "the the empirical"; "a a high-level summary".
- Page 17/18 break: page 17 ends a paragraph ("... indicator function for event $Y$."); TeX has a blank line before "For the state vector", so no join on page 18.
- check: ATTENTION, 12 missing lines + number differences, all category (a). Adjudication note written.

### Page 18 (end of Appendix D, Appendix E.1-E.3 start): reviewed [v2]
- Headings: `## E Model architectures and training details`, `### E.1 Diffusion models`, `### E.2 One-step MLP dynamics models`, `### E.3 Auto-Regressive Transformer dynamics model (ART)`.
- First paragraph (normalisation $\hat{s}_k = 2 \hat{F}_k(s_k) - 1$ and inverse $s_k = \hat{F}_k^{-1}(\frac{1+\hat{s}_k}{2})$): inline in print, written inline. New paragraph in the TeX, so no join to page 17.
- E.1 hyperparameters (256, 16, 8, 1024, 2048, 5/2, 3/2, 32/5, 10/5) checked against the page. Printed $p(s_t+1 | s_t, a_t)$ kept (typo for $s_{t+1}$, also in TeX).
- Table 5 (`table-5`, bbox [224,572,388,637]): 6 x 2 cells; TeX has commented-out rows (optimizer, steps, LR schedule) that are not printed and are not included.
- Text repair: 'sepa-rate' -> 'separate'. Page ends mid-sentence with "This results in the following tokens: $T =$"; continues on page 19 (join set there).
- check: ATTENTION, 5 missing lines + number differences, all category (a). Adjudication note written.

### Page 19 (Appendix E.3 end to Appendix F): reviewed [v2]
- First item continues the page-18 sentence ("... following tokens: $T =$" + "$[\texttt{embed}_s(\boldsymbol{s}_1), \ldots]$. These then normalized ..."): `join_previous: space`.
- Equation (3): formula image -> `$$\mathcal{L} = \sum_t \texttt{MSE}(\texttt{pred}_a(O_{2t-1}), \boldsymbol{a}_t) + \texttt{MSE}(\texttt{pred}_s(O_{2t}), \boldsymbol{s}_{t+1}) \tag{3}$$`. Typewriter names use `\texttt{}` throughout pages 18-19 (TeX uses `\mathtt`).
- Table 6 (`table-6`, bbox [178,212,434,309]): 10 x 2 cells, citations inside cells as printed.
- Headings: `### E.4` ... `### E.6`, `## F Hyper-parameters for the sampling-based planner`.
- Numbers checked: 256, 16, 10 layers, 0.99, 0.997, $-100$, $10^{-4}$ -> $10^{-5}$, 500 warm-up steps, $2 \times 10^6$ steps, clip norm 5, EMA 0.99, 2 days, F = 32, N = 64, H = 1.
- Authors' grammar kept: "These then normalized", "and uses EMA", "and separate worker".
- check: ATTENTION, 8 missing lines + number differences, all category (a). Adjudication note written.

### Page 20 (Appendices G, H, I, start of J): reviewed [v2]
- Headings: `## G Long-horizon dynamics prediction`, `## H Generalization to novel rewards`, `## I Adaptation to novel dynamics`, `## J Timing measurements`.
- Inline maths in LaTeX: $\lesssim 1.0$, $f_{\mathrm{novel}}(\boldsymbol{s}_t, \mathbf{A}_t) = 5 \exp(-(h_t - h_{\mathrm{target}})^2/2\sigma^2)$, $\sigma^2 = 5 \times 10^{-4}$, $\kappa = 0$, $\tilde{\kappa} = 1$, $[-5 \times 10^{-4}, 5 \times 10^{-4}]$, $h_{\mathrm{target}} = 1.2/0.9/1.4$, $[-0.5, 0.5]$ vs $[-1, 1]$, ($\pm$ 2.31).
- Numbers checked: 1.25, 5, 100 episodes, 30170 transitions, 23.14 (± 2.31), 256 trajectories.
- Typo kept: "replaced the the trained value model". TeX's commented-out G material (random-action figure) not printed, not included.
- Page ends mid-sentence ("... for each algorithm, in"); join set on page 21.
- check: ATTENTION, 9 missing lines + minus-glyph number differences, all category (a). Adjudication note written.

### Page 21 (end of Appendix J, Table 7): reviewed [v2]
- First item continues the page-20 sentence ("... for each algorithm, in" + "three D4RL locomotion environments."): `join_previous: space`.
- Table 7 (`table-7`, bbox [122,175,489,226]): 4 x 5 cells; cell convention `3.51(±0.06) × 10^-1`, `× 10^0`, `× 10^1`, `× 10^2` (printed superscript exponent, ASCII caret, PDF minus as ASCII hyphen). All 12 cells checked at 400 dpi and against the TeX. Caption separate.
- check: all 29 lines found; number differences only from the exponent notation, category (a). Adjudication note written.

## Summary

### Pages and state
| Page | Content | State | check |
| --- | --- | --- | --- |
| 16 | App. A, Algorithms 3-4, App. B intro | reviewed [v2] | ATTENTION, all (a), note written |
| 17 | Algorithm 5, App. C + Table 4, App. D | reviewed [v2] | ATTENTION, all (a), note written |
| 18 | App. D end, E.1-E.3 + Table 5 | reviewed [v2] | ATTENTION, all (a), note written |
| 19 | E.3 end + eq. (3) + Table 6, E.4-E.6, F | reviewed [v2] | ATTENTION, all (a), note written |
| 20 | G, H, I, J start | reviewed [v2] | ATTENTION, all (a), note written |
| 21 | J end + Table 7 | reviewed [v2] | all lines found; exponent-notation number diffs (a), note written |

No category (b) diagnostic remains. Adjudication notes: `DOC/adjudication-notes/page-0016.json` ... `page-0021.json`.

### Assets (all unique in the document; no clash with pages 1-15, whose tables/algorithms are numbered 1-3 / 1-2)
- Algorithms (figure crop + text transcription): `algorithm-3`, `algorithm-4` (p16), `algorithm-5` (p17).
- Tables (CSV rows): `table-4` (p17, 8x9), `table-5` (p18, 6x2), `table-6` (p19, 10x2), `table-7` (p21, 4x5).
- Equations: equation (3) on p19 as `$$...\tag{3}$$`; unnumbered displays $\mathcal{D}$ and $\hat{F}_k(t)$ on p17 as `$$...$$`. No formula kept as an image; no figure in this range.

### Joins
- p19 first item (`p0019-b001`, token list `$[\texttt{embed}_s(\boldsymbol{s}_1), \ldots]$`): `join_previous: space` (continues "This results in the following tokens: $T =$" on p18).
- p21 first item (`p0021-b001`): `join_previous: space` (continues "... for each algorithm, in" on p20).
- Not joined, by decision: p17 -> p18 (a new paragraph per the TeX); p16 -> p17 (Algorithm 5 is a float at the top of p17 after a complete sentence).
- Range boundary with page 15 (another reviewer): page 15 ends the references; page 16 starts `## A ...`, so no join is needed.

### TeX versus PDF
- No disagreement in printed content. The TeX contains commented-out material that is not printed and was not included: three rows of Table 5 (Optimizer, Training steps, Learning-rate schedule) and a paragraph plus a figure on random-action prediction errors in Appendix G.
- Typewriter names: the TeX uses `\mathtt`; I wrote `\texttt` (as the assignment asked; same rendering).

### Authors' typos and oddities kept as printed (listed in each page's review_notes)
- p16: $\sqrt{\alpha_k}x_{t-1}$ in the forward process (probably $x_{k-1}$); "by minimize"; prose $s_{t+1:t+f}$ (lowercase f); Algorithm 4 line 2 $\boldsymbol{s}_{t+1:t+f_F}$; "In Algorithm 3 and Algorithm 4, we present the multi-step and single-step training" (Algorithm 3 is actually one-step and Algorithm 4 multi-step).
- p17: Algorithm 5 $\mathbf{A}_{N,H} = 0$; $K$ and $\beta$ not among the Def arguments; $\mathcal{D}$ lists $r^2_{1:T_1}$, $r^m_{1:T_2}$, no comma after $\ldots$; "a a high-level summary"; "the the empirical".
- p18: $p(s_t+1 | s_t, a_t)$ (for $s_{t+1}$).
- p19: "These then normalized", "and uses EMA", "and separate worker".
- p20: "replaced the the trained value model".

### Text repairs of substance
- All glyph-soup maths rebuilt from the TeX (macros expanded) and checked on 200-400 dpi crops; split decimals (`1 _._ 2`), `<sup>`/`<u>` debris and backtick fragments removed.
- p18: line-wrap hyphen "sepa-rate" -> "separate".
- Heading levels fixed (extractor used `#` for appendix sections and `##` for subsections).

### Proposals for shared files (coordinator)
- plan.json notes (conversion notes for tables in this range):
  - "Table 4: the two-level header is flattened by repeating the parent header ('MS Diff Action Proposal: SS Diff Dynamics', ...); the 'Average' label spans the Domain Name and Level columns in print and is stored with an empty Level cell. Spacing inside '(±x)' is kept as printed and is inconsistent in the D-MPC column."
  - "Table 7: cells are written as printed with the superscript exponent as '× 10^-1', '× 10^0', '× 10^1', '× 10^2' (ASCII caret; minus as ASCII hyphen). Units: milliseconds per environment step."
  - "Algorithm transcriptions follow the algorithm2e layout: plain line numbers, one '&emsp;' per nesting level, no 'end' lines unless printed."
- Navigation: appendix sections A-J are `##`, E.1-E.6 are `###`; no printed "Appendix" heading exists, so none was added. The page-1-7 and 8-15 reviewers should use `##` for the numbered sections (e.g. `## 4 Experiments`), `###` for 4.1 etc. and `####` for 4.4.1 etc. so the appendix levels line up.
- reading_order: not needed for pages 16-21 (every float sits between complete paragraphs).

### Limitations
- Algorithm transcriptions use `&emsp;` HTML entities for nesting (as in pac-nmpc); an agent reading the raw Markdown sees the entity text.
- Prose after a `$$` display is a separate item without a join (sibling convention), so "let $\mathcal{S}_k$ ..." and "where $\mathbf{1}_Y$ ..." on p17 appear as their own paragraphs although they belong to one TeX paragraph.

### Brief issues
- The brief does not say where a merged-header conversion note should go if the caption must stay verbatim and plan.json is off-limits; I followed the page-10 reviewer (note in review_notes, proposed plan note above).
- The brief does not say whether typewriter names in maths use `\texttt` or `\mathtt`; the assignment chose `\texttt`. Worth fixing collection-wide.
