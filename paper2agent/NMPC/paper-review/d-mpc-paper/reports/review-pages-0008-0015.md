# D-MPC (d-mpc-paper), review of pages 8-15 (brief v2)

Reviewer: page-range agent, 2026-10-12. DOC = `d-mpc-paper/documents/s001-d-mpc`. TeX: `tex-source/d-mpc` (adaptation2, ablations2, distillation, discussions2, main.bbl, macros.tex), used as source only, never compiled.

## Summary

| Page | State | check | Content |
| --- | --- | --- | --- |
| 8 | reviewed [v2] | ATTENTION, all category (a), adjudication note written | end of 4.2, Figure 1, start of 4.3 |
| 9 | reviewed [v2] | OK 45/45 | 4.3 cont., 4.4, 4.4.1-4.4.3 |
| 10 | reviewed [v2] | OK 46/46 | Table 3(a), Table 3(b), Figure 2, 4.4.3 cont. |
| 11 | reviewed [v2] | ATTENTION, all category (a), adjudication note written | 4.4.3 end, 4.4.4, 4.5, 5 Conclusions |
| 12 | reviewed [v2] | OK 45/45 | Conclusions end, References (13 entries) |
| 13 | reviewed [v2] | OK 41/41 | References (20 entries) |
| 14 | reviewed [v2] | OK 46/46 | References (16 entries) |
| 15 | reviewed [v2] | OK 7/7 | References (last 3 entries) |

No category (b) diagnostics remain on any page.

## Conventions used
- Bold vectors: aligned with the pages 1-7 reviewer (pages 2-5 were saved during my run). Lower-case vectors are printed bold italic (TeX `\vs`, `\va` = `\bm{...}`), so I write `\boldsymbol{s}`, `\boldsymbol{a}`. Upper-case `\vA` is printed upright bold (TeX `\mathbf{A}`), so I write `\mathbf{A}`. `\dynamics` is written `p_{d}`, as on pages 2-5. I first wrote `\mathbf{s}` on pages 8 and 11 and converted it once their convention was visible.
- `±` in prose and table cells is Unicode, with the printed spacing kept.
- References: one `text` item per entry in printed author-year style (no `[n]`). The extractor's list bullet, italic markers and code backticks are removed. URLs are plain and contain no spaces.
- Furniture: the running header "Published in Transactions on Machine Learning Research (05/2025)" and the page numbers are `omit` items with specific reasons.

## Figures, tables, equations
- Page 8: `figure-1` ("Figure 1"), bbox [68,251,544,524]. One item holds the whole 3x4 composite: column titles, both y-axis labels, all "timestep" labels, snapshot labels and legends. All four edges were checked with crops. A caption item follows.
- Page 10: `table-3a` ("Table 3(a)", item p0010-b001, bbox [90,80,299,152]) and `table-3b` ("Table 3(b)", new item p0010-b001b, bbox [328,80,528,152]). The extractor had glued both into one 8-column table. One shared caption item follows both, as printed.
  - 3(a) rows: `['', 'Diffuser', 'D-MPC']`, `['Original', '79.60', '76.21 (±2.67)']`, `['Pre-FT w/ defect', '25.85 (±1.08)', '22.74(±1.41)']`, `['Post-FT w/ defect', '6.8(±0.86)', '30.65(±1.89)']`. The inconsistent spacing inside the brackets is as printed.
  - 3(b): the two-level header is flattened to `Action Proposal | Dynamics Model: SS Diff | Dynamics Model: SS MLP | Dynamics Model: ART | Dynamics Model: MS Diff`. The rows are `SS Diff 53.32 52.93 - N/A` and `MS Diff 57.81 57.14 59.83 65.98`.
  - **Bold cells:** only Table 3(b) 65.98 (MS Diff proposal x MS Diff dynamics). Table 3(a) has none.
- Page 10: `figure-2` ("Figure 2"), bbox [69,230,540,507]. It holds the 3x3 log-scale grid, the row labels medium/medium-replay/expert, the column titles Walker2d/Hopper/HalfCheetah, "RMSD pred. err.", "Rollout steps" and the legend box, which ends at about y=501. A caption item follows.
- Inline maths written in LaTeX (no display equations in my range, no formulas kept as images):
  - Page 8: $f_{\mathrm{novel}}(\boldsymbol{s}_t, \mathbf{A}_t) = 5 \exp(-(h_t - h_{\mathrm{target}})^2 / 2\sigma^2)$, $\sigma^2 = 5 \times 10^{-4}$, $\kappa = 0$, $\tilde{\kappa} = 1$, $\tilde{J}$, $V_n$, $p_{s|a}$, $\pi_a$.
  - Page 11: $p_{d}(\boldsymbol{s}_{t+1:t+F} | \boldsymbol{s}_{1:t}, \boldsymbol{a}_{1:t+F-1}) = \prod_{t}^{t+F-1} p_{d}(\boldsymbol{s}_{t+1} | \boldsymbol{s}_{1:t}, \boldsymbol{a}_{1:t-1}, \boldsymbol{a}_t)$.
- TeX versus PDF: no disagreements. The printed novel-reward formula equals the TeX exactly.

## Joins
- p0008-b001 `join_previous: "space"`: page 8 continues the Section 4.2 paragraph begun on page 7 (same TeX paragraph). This needs page 7's last emitted item p0007-b007 ("...on the Walker2d medium-replay dataset.") to stay a `text` item. **Page 7 is still unreviewed; its reviewer should keep that item last and as text.**
- p0010-b005 `join_previous: "space"` joins onto page 9's last paragraph ("...on the non-velocity" / "coordinates with increasing trajectory length").
- p0011-b001 `join_previous: "space"` joins onto page 10's last paragraph ("...due to the fact that" / "the transformer dynamics model").
- Range end: page 15 ends the bibliography and page 16 starts `## A Algorithms for model learning`, so no join is needed. No reference entry crosses a page break in my range.
- Page 10 was reordered so that it starts with the continuing prose. Table 3 and Figure 2 now sit between complete paragraphs, so no `reading_order` entry is needed.

## Text repairs of substance
- Page 9: `( _±_ 2.67)`-style emphasis damage became `(±2.67)`. Every prose number was verified against crops: 76.21 (±2.67), 22.74 (±1.41), 72.91 (± 3.47) (space as printed), 25.85 (±1.08), "100 episodes", 30.65 (±1.89), 6.8 (±0.86), 33.13, 52.93, 53.32, 57.14, 57.81.
- Page 10:
  - "nonvelocity" became "non-velocity". The line-break hyphen is a real compound; the TeX has "non-velocity".
  - "33 _._ 13" became "33.13".
  - "_±_" became "±".
- Page 11: numbers verified: 4096, 65.98, 50.01, 6, 1M, 65.08, 65.98, 41.92.
- Page 14:
  - "Diffusion modelaugmented" became "Diffusion model-augmented".
  - "CompoundingError" became "Compounding-Error". Both hyphens are real and were lost at line ends; main.bbl confirms them.
  - "2(4): 160–163" became "2(4):160–163".
- URLs broken across lines were repaired:
  - Page 12: openreview sP1fo2K9DFG, arxiv 2008.05556, 2303.04137, 2210.10047.
  - Page 14: arxiv 1911.08265, doi 10.1007/s00170-021-07682-3, ojs.aaai.org/.../view/9590.
- Headings set exactly as printed:
  - `### 4.3 Adaptation to novel dynamics`, `### 4.4 Ablation studies`, `### 4.5 D-MPC can be distilled into a fast reactive policy for high-frequency control`.
  - `#### 4.4.1` to `#### 4.4.4`.
  - `## 5 Conclusions`, `## References`.
- Authors' typos and quirks kept as printed:
  - "adaptions" (p8).
  - Mixed "finetune"/"fine-tune" and lower-case "diffuser" (p9).
  - Straight double quotes around "a-causal" (p11).
  - Product lower limit printed as a bare `t` that is also the factor index (p11; the same quirk occurs on page 3).
  - "J . Bagnell" (p14, bib quirk `J~.~Bagnell`).
  - Zhu, Huang and Russell entry without a year (p15).
  - Lower-case "Td-mpc2", "Morel", "Corl", "Mopo", "Combo", "Em distillation", "D4rl", "atari".

## Reference checking
All 52 entries on pages 12-15 were checked character by character against 180-200 dpi crops, with main.bbl used to locate each entry: 13 + 20 + 16 + 3. This is every entry, beyond the "every third" minimum.

## Remaining diagnostics (all category (a))
- Page 8: 9 missing lines are LaTeX versus PDF glyph order in the inline maths. The number difference is the `10^{-4}` exponent (U+2212 versus `-`); the second parser reports the same.
- Page 11: 2 missing lines are the product formula. The number differences are three `−1` versus `-1` inside the formula; the second parser reports the same.
- Adjudication notes: `DOC/adjudication-notes/page-0008.json`, `page-0011.json`.

## Proposals for shared files (coordinator)
- plan.json `notes`: add "Table 3(b): the CSV flattens the two-level header (Action Proposal; Dynamics Model over SS Diff / SS MLP / ART / MS Diff) into 'Dynamics Model: ...' column names; the bold best cell 65.98 is not marked in CSV."
- Navigation: the heading levels above are consistent with `## 4 Experiments` on page 6. Nothing else to add.
- reading_order: not needed for pages 8-15.
- Asset names: `figure-1`, `figure-2`, `table-3a`, `table-3b` are unique in the document (checked against all page files). Page 7's Table 2 still carries the extractor name `table-p0007-004`; its reviewer should rename it to `table-2`.

## Limitations and notes on the brief
- Unicode `±` is used instead of `$\pm$`. The brief does not say which; it matches the table cells.
- The brief's example reference style is `[12] ...`. For this author-year paper the assignment's plain style was used instead.
- The bold-vector convention was not fixed in advance. Reviewers working in parallel can diverge (I had to convert pages 8 and 11), so a per-paper convention line in the assignment would save a pass.
