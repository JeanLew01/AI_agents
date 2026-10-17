# Independent verification: D-MPC paper skill, PDF pages 1-11

- Package: /home/jixia/AI_agents/paper2agent/NMPC/staging/d-mpc-paper-s2
- Document: /home/jixia/AI_agents/paper2agent/NMPC/paper-review/d-mpc-paper/documents/s001-d-mpc
- Verifier: fresh independent verifier (2026-10-12). Status: COMPLETE.
- Result: **0 errors, 3 minors** (two are in the navigation index / conversion notes, one is a Markdown escaping issue in
  the Table 1 header). The text, mathematics, tables, algorithms and figures for pages 1-11 match the PDF.

## Coverage

All checks were done in full; nothing was sampled.

- Pages 1-11, plus the top of page 12 where Section 5 ends: I read every page preview next to `paper.md` lines 1-303 (title
  to the end of "5 Conclusions").
- Prose: I ran a word-level diff of `pdftotext` (pp. 1-12) against `paper.md` lines 1-303, with maths, tables and Markdown
  markup removed. **No word differs.** The only differences left are omitted running headers, page numbers, the arXiv
  stamp, maths tokens and where the floats are placed. All numbers quoted in the prose are covered by this diff.
- Maths: I compared 220-260 dpi crops with the LaTeX for:
  - eq. (1) and the h_t definition (p2);
  - all inline formulas of Section 1 (p2), Section 2 paragraph 2 and the Diffuser paragraph (p3);
  - the dataset definition, eq. (2) and the following paragraph (p5);
  - Algorithms 1 and 2 (p5-6);
  - the V_n / J-tilde / f_novel formulas in Section 3.4 (p6);
  - f_novel, sigma^2, kappa and h_target in Section 4.2 (p8);
  - the ART product formula in Section 4.4.3 (p11).

  A script check found that all 2 display and 101 inline formulas have balanced `$` and braces.
- Tables: I compared every CSV cell of table-1, table-2-locomotion, table-2-adroit, table-2-kitchen, table-3a and table-3b
  with a 240-260 dpi crop and with the native PDF text layer. The check/cross code points are U+2713/U+2717 in both the
  PDF and the CSV. I also checked the Markdown copies of the tables in `paper.md`.
- Bold cells: I compared the full bold lists for Table 2 and Table 3(b) in the conversion notes with the crops.
- Algorithms 1 and 2: I opened both JPEGs and compared them line by line with the PDF and the transcription, including
  the nesting.
- Figures 1 and 2: I opened both JPEGs (complete, legible, no caption text inside) and compared the captions with the
  PDF.
- `SKILL.md`, `references/index.md` and the conversion notes: I checked every claim about pages 1-11. A script confirmed
  that every index heading exists exactly in `paper.md`; the only row it did not find is "Document beginning", which
  belongs to `supplement.md`.

## Findings

| # | severity | PDF page | item id | package says | PDF shows | suggested fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | minor | 6 (also 5, 8) | plan.json `notes` (Conversion notes, bullet 2) | "Section 3.1 and 4.3 call the action proposal \pi (\pi_a) and the dynamics p_{s\|a}, elsewhere \rho and p_{d}." | The dynamics is also printed as p_{s\|a} in Section 3.3 ("we predict the corresponding state sequences using p_{s\|a}", p6, item p0006-b003) and Section 3.4 ("supervised fine tuning of p_{s\|a}", p6, item p0006-b006). The package text keeps both correctly; only the note is incomplete. | Reword: "Sections 3.1, 3.3, 3.4 and 4.3 write the dynamics as p_{s\|a}, and Sections 3.1 and 4.3 call the action proposal \pi (\pi_a); elsewhere \rho and p_{d}." |
| 2 | minor | 4 | p0004-b001 (Markdown rendering of Table 1, `paper.md` line 91) | Header cells `Factored: $p_{d}(s\|a)\\,\\rho(a)$ / ...` and `Model-free: $\\pi(a)$`: the backslashes are doubled. This is the only place in `paper.md` with `\\`; the CSV and all other formulas use single backslashes. | p_d(s\|a) ρ(a), π(a) | Write `$p_{d}(s\|a)\,\rho(a)$` and `$\pi(a)$`, keeping only the `\|` escape for the table pipe. Read as LaTeX, `\\` is a line break, so a math renderer (or a reader of the raw file) sees "p_d(s‖a) [newline] , [newline] rho(a)". |
| 3 | minor | 10 | index.md rows "4.3 Adaptation to novel dynamics" and "4.4 Ablation studies" | The 4.3 row says Table 3(a) is there and the 4.4 row says "Table 3(b) summary" is there. | Table 3 is printed at the top of p10, inside 4.4.3. In `paper.md` both sub-tables, their CSV links and the shared caption are under "#### 4.4.3" (lines 263-276), so a reader sent to 4.3 or 4.4 finds only "See Table 3a/3b" with no link. | In the index, write "Table 3(a) (placed under 4.4.3)" in the 4.3 row and "Table 3(b) (placed under 4.4.3)" in the 4.4 row, and add "Table 3" to the 4.4.3 row. |

### Observations (not package errors)

- Diffuser's original Walker2D score is 72.91 (± 3.47) in the Section 4.3 text (p9) but 79.60 in Table 3(a) (p10).
  This inconsistency is in the PDF itself, and the package keeps both values faithfully. It could be added to the
  "slips kept as printed" note so that a user does not take it for a transcription error.
- In Table 2, walker2d/medium-replay CQL 77.20 is within 5% of the maximum (78.81) but is not bold in print. The notes
  list correctly follows the print.
- The conversion note says "the bold final 's' marking 'DWMS'". In print, the bold 's' is the last letter of "Diffusion
  World Model**s**", the expansion of DWMS, not the acronym itself. The wording is acceptable.
- algorithm-1.jpg and algorithm-2.jpg include the algorithm's title rule ("Algorithm 1: Main MPC loop."). This is part
  of the boxed float and is also transcribed, so I treat it as acceptable.

## Checked and found correct

- **p1** (p0001-b002...b031): title; 9 author blocks (names including "Lázaro-Gredilla", affiliation, e-mails); corresponding-author
  footnote; OpenReview line and URL; abstract word for word (including "MBOP(Argenson" with no space); start of the
  Introduction with non-bold `J(a_{t:t+F-1}, s_{t+1:t+F})`. The running header, arXiv stamp and page number are correctly
  omitted.
- **p2**: eq. (1) symbol by symbol: bold arguments of argmax and E, non-bold J arguments, \Big brackets, trailing comma,
  \tag{1}. h_t ≡ {s_{1:t-1}, a_{1:t-1}}; p_d(s_{t+1:t+F}|s_{1:t}, a_{1:t+F-1}); p_d(...|s_t, a_{t:t+F-1}, h_t);
  ρ(a_{t:t+F-1}|h_t); "(Zhu et al.)" with no year. Footnote 1 is complete, with marker [^1] after "fixed reward function.".
- **p3**: contributions list 1-4. Section 2 paragraphs, including "Q-leaning", the mixed straight/curly quotes as in the
  text layer, p_j(s,a) and p_d(s|a)ρ(a) non-bold, the SS/MS formulas, \prod_t^{t+F-1} as printed, the MS dynamics and
  proposal formulas, the Diffuser paragraph with p_j(s_{1:T}, a_{1:T}), p_d(s_{1:T}|a_{1:T}), ρ(a_{1:T}). Footnote 2 is
  complete.
- **p4**: Table 1, all 6×7 cells including the empty Non-expert cells for the Joint and Model-free columns, and the
  header flattening. The caption, including "Diffuson Policy", "Imitiating Humans" and the final " .", matches. The
  remaining Related-work paragraphs (Decision Diffuser, TD-MPC, MBOP, MBD/DyDiff, summary) match.
- **p5**:
  - Section 3 intro and 3.1 (p_{s|a}, π).
  - The dataset definition, with r^2_{1:T_1}, r^m_{1:T_2} and "\ldots" without a comma as printed.
  - The p_d and ρ conditionals.
  - Eq. (2): sum limits k=t to t+F-1, γ^{k-t}, γ^F V(s_{t+F}) with non-bold s, \tag{2}.
  - The "Here γ ..." paragraph and the MBOP-ensembles paragraph.
  - Algorithm 1, lines 1-9 and nesting.
- **p6**:
  - Sections 3.3 and 3.4: V_n = κJ(s_{1:F}, **A**_{n,1:F}) + κ̃J̃(...) and J̃ = (1/F)Σ_{t=1}^F f_novel(s_t, **A**_{n,t}), with upright bold A as printed.
  - Section 4 intro and questions 1-4.
  - Algorithm 2, lines 1-7: hat n, argmax_n, a_{n̂,1}.
- **p7**: Section 4.1 text. Table 2: all 7×10 locomotion, 4×8 Adroit and 3×6 Kitchen cells, including "-0.08" and the
  "(±x)" spacing. The 'Average' rows are stored as the notes describe. The bold list in the notes matches the print
  exactly: halfcheetah-m D-MPC/IQL; hopper-m MOReL; walker2d-m MOReL/D-MPC/Diffuser/IQL; halfcheetah-mr CQL/IQL;
  hopper-mr MOReL/D-MPC/Diffuser/CQL/IQL; walker2d-mr D-MPC; Locomotion Avg MOReL/D-MPC/CQL/IQL; pen IQL; door D-MPC;
  hammer D-MPC; Adroit Avg IQL; Kitchen mixed/partial/Avg D-MPC. Only the means are bold. The Table 2 caption matches.
- **p8**: Section 4.2, including f_novel(s_t, **A**_t) = 5 exp(-(h_t - h_target)^2/2σ^2), σ^2 = 5×10^-4, κ = 0, κ̃ = 1 and
  h_target 0.9/1.2/1.4. figure-1.jpg is complete: 4 columns × 3 rows, axis labels, legends, snapshot labels. The Figure 1
  caption matches. Section 4.3 paragraph 1 has p_{s|a}, π_a and "adaptions".
- **p9**: the 4.3 numbers 76.21 (±2.67), 22.74 (±1.41), 72.91 (± 3.47), 25.85 (±1.08), 100 episodes, 30.65 (±1.89) and
  6.8 (±0.86). Sections 4.4 and 4.4.1-4.4.3 text with 33.13, 52.93, 53.32, 57.14, 57.81.
- **p10**: Table 3(a), all 9 cells with the uneven "(±" spacing as printed. Table 3(b), all 10 cells including "-" and
  "N/A", and the bold 65.98. The Table 3 caption matches. figure-2.jpg is complete: 3×3 panels, row and column labels,
  y-label, x-label, legend. The Figure 2 caption matches. The text continues correctly across the float (join).
- **p11**: the ART product formula `\prod_{t}^{t+F-1} p_d(s_{t+1}|s_{1:t}, a_{1:t-1}, a_t)`, the "a-causal" quotes as
  printed, Sections 4.4.4 (4096 hidden units, 65.98, 50.01) and 4.5 (1M steps, 65.08, 65.98, 41.92), and Section 5
  paragraphs 1-2.
- **p12 (top)**: Section 5 paragraphs 3-4 are complete.
- **Headings**: all printed headings in the range are present at the right level and with the exact wording
  (#, ## Abstract, ## 1-5, ### 3.1-3.4 / 4.1-4.5, #### 4.4.1-4.4.4). None is invented.
- **Conversion-note claims for pp. 1-11 that are true**: equations (1) and (2) are numbered with \tag; the
  typos/slips kept as printed in this range ('Q-leaning', 'Diffuson Policy', 'Imitiating Humans', r^2/r^m,
  \prod_t^{t+F-1} in Sections 2 and 4.4.3, 'adaptions', Zhu et al. without a year); the Table 1 header flattening and
  symbols; the Table 2 split into three CSVs and the Average-row handling; the Table 3(b) header flattening; the
  "(±x)" spacing; the full bold list; the footnote convention; the omitted typography. The remaining slips in the list
  ('the the', 'a a high-level summary', 'by minimize', 'uses EMA') are in the appendices, outside my range; 'a a
  high-level summary' is present in Appendix C.

## Technical question answered from the package

**Question:** In the novel-dynamics experiment, what defect was simulated, how was the fine-tuning data collected, and
how did D-MPC and Diffuser perform before and after fine-tuning?

**Answer from the package** (Section 4.3 and Table 3(a), `table-3a.csv`):
- The defect is on Walker2D: the torque executed on a foot joint (action dimension 2) is restricted.
- D-MPC is trained on the medium dataset. It scores 76.21 (±2.67) without the defect and 22.74 (±1.41) with the defect.
- The play data is 100 episodes on the defective hardware, collected by deploying the original D-MPC trained on
  medium-replay. Only the multi-step diffusion dynamics model is fine-tuned on it; the action proposal and the value
  model stay fixed.
- After fine-tuning, D-MPC scores 30.65 (±1.89).
- Diffuser models states and actions jointly, so its full model has to be fine-tuned. With the defect it scores
  25.85 (±1.08); after fine-tuning it drops to 6.8 (±0.86).
- Diffuser's no-defect score is 72.91 (± 3.47) in the text but 79.60 in Table 3(a).

**Check against the PDF:** p9 lines 84-243 (native text layer) and the p10 Table 3(a) crop give exactly these values and
wording, including the inconsistency between 72.91 and 79.60. The answer is correct.
