# D-MPC paper review, pages 1-7 (reviewer d-mpc-r1, brief v2)

Paper: "Diffusion Model Predictive Control" (Zhou et al., TMLR 05/2025, arXiv:2410.05364v2).
DOC: `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/d-mpc-paper/documents/s001-d-mpc`
TeX: `/home/jixia/AI_agents/paper2agent/NMPC/tex-source/d-mpc` (read only, never compiled)

## Conventions used on pages 1-7
- Bold vectors: the TeX defines `\va`, `\vs`, `\vh` as `{\bm{a}}` etc. (macros.tex re-`\def`s them with `\bm`), so they are rendered as
  `\boldsymbol{a}`, `\boldsymbol{s}`, `\boldsymbol{h}` (standard amsmath equivalent of `\bm`). Where the authors wrote plain `a`, `s`
  (e.g. inside $J(a_{t:t+F-1}, s_{t+1:t+F})$) the PDF prints them non-bold and so does the transcription.
- Macros expanded: `\dynamics` -> `p_{d}`, `\joint` -> `p_{j}`, `\proposal` -> `\rho`, `\policy` -> `\pi`, `\objfn` -> `J`,
  `\future` -> `F`, `\past` -> `H`, `\argmax` -> `\operatorname*{arg\,max}`.

## Page log

### Page 1 - reviewed [v2]
- Items: title, 9 author items (merged from split name/affiliation/email pieces), corresponding-author footnote `Footnote ∗` after the
  author block (marker `[^*]`), OpenReview line (kept), `## Abstract`, abstract, `## 1 Introduction`, first paragraph.
- Omitted: running header, rotated arXiv stamp, page number.
- Maths: inline $J(a_{t:t+F-1}, s_{t+1:t+F})$ (non-bold a, s as printed).
- Boundary: the last paragraph continues on page 2 (join set on page 2's first item).
- check: lines 45/45; only U+2212 vs '-' (category a); adjudication note written.

### Page 2 - reviewed [v2]
- First item joins page 1 (`join_previous: space`): "$F$ from the current timestep $t$".
- Equation (1): formula image item (formula-p0002-002) converted to a `$$ ... \tag{1} $$` text item from intro3.tex; checked at 220 dpi.
- Inline maths: $\boldsymbol{h}_t$, two $p_{d}(\cdot|\cdot)$ forms, $\rho(\boldsymbol{a}_{t:t+F-1}|\boldsymbol{h}_t)$, $\boldsymbol{a}_t$.
- Footnote 1 (`[^1]` in text) placed before the last line "In summary, our key contributions are:" (the list follows on page 3).
- Note: "(Zhu et al.)" printed without a year (kept).
- check: 7 missing lines (all maths, category a), 9 number differences (U+2212 vs '-', category a); adjudication note written.

### Page 3 - reviewed [v2]
- Contribution list 1-4, `## 2 Related work`, four paragraphs, Footnote 2 (`[^2]`) placed before the last paragraph, which ends
  mid-sentence ("In addition, we propose") and continues on page 4 (join set on page 4).
- Text repair of substance: the product of one-step conditionals was destroyed by extraction (replacement character); now
  $p_{d}(\boldsymbol{s}_{t+1:t+F}|\boldsymbol{s}_{1:t}, \boldsymbol{a}_{1:t+F-1}) = \prod_{t}^{t+F-1} p_{d}(\boldsymbol{s}_{t+1}|\boldsymbol{s}_t, \boldsymbol{a}_t, \boldsymbol{h}_t)$.
- Kept as printed (noted): typo "Q-leaning"; product lower limit just $t$; SS dynamics written with $\boldsymbol{a}_{t+1}$; mixed straight/curly quotes.
- check: 10 missing lines (all inline maths, category a), 4 minus-glyph number differences (category a); adjudication note written.

### Page 4 - reviewed [v2]
- Order: continuing paragraph from page 3 first (`join_previous: space`), then Table 1 (`table-1`, 7 x 7 CSV) and its caption, then the
  remaining Related-work paragraphs (end of Section 2).
- Table 1 combined headers: `Factored: $p_{d}(s|a)\,\rho(a)$ / Dyna / (single-step)` etc. (parent headers repeated, joined with ' / ');
  ✓/✗ as printed; two empty cells (Non-expert data, Joint and Model-free columns).
- Caption kept verbatim; bold final "s" of "Diffusion World Models" (marks DWMS) rendered plain. Typos kept: "Diffuson Policy",
  "Imitiating Humans", missing comma before "DBC", space before the final period; "MOReL" (table) vs "MOREL" (caption) as printed.
- check: 2 missing lines (Table 1 maths header cells, category a); no number differences; adjudication note written.

### Page 5 - reviewed [v2]
- `## 3 Method`, `### 3.1 Model predictive control`, `### 3.2 Model learning`.
- Equation (2): formula image converted to `$$ ... \tag{2} $$` from method2.tex, checked at 220 dpi.
- Algorithm 1: image crop `algorithm-1` (bbox [60,517,543,655]) + line-numbered transcription (lines 1-9).
- Text repair of substance: the dataset definition $\mathcal{D}=\{\ldots\}$ had been shredded into `<sup>` fragments; rebuilt from TeX.
- Kept as printed (noted): $r_{1:T_1}^2$, $r_{1:T_2}^m$ superscripts in $\mathcal{D}$; Section 3.1 uses $\pi$ for the action proposal and $p_{s|a}$ for dynamics.
- check: 16 missing lines (maths, category a); number differences = minus glyphs + Algorithm 1 transcription numbers (category a); adjudication note written.

### Page 6 - reviewed [v2]
- `### 3.3 Planning`, `### 3.4 Adaptation`, `## 4 Experiments` + question list 1-4.
- Algorithm 2: image crop `algorithm-2` (bbox [60,616,543,731]) + line-numbered transcription (lines 1-7). Moved within the page from
  the bottom (after the Section 4 question list) to the end of Section 3.3, right after the paragraph that introduces it.
- Text repair of substance: Section 3.4's $V_n = \kappa J(\ldots) + \tilde{\kappa}\tilde{J}(\ldots)$ and
  $\tilde{J}(\boldsymbol{s}_{1:F}, \mathbf{A}_{n,1:F}) = \frac{1}{F}\sum_{t=1}^F f_{\mathrm{novel}}(\boldsymbol{s}_t, \mathbf{A}_{n,t})$ were shredded
  into `<sup>` fragments with U+FFFD; rebuilt from TeX. `\vA` = `\mathbf{A}` (upright bold, as printed).
- check: 4 missing lines (maths, category a); extra numbers = Algorithm 2 transcription (category a); adjudication note written.

### Page 7 - reviewed [v2]
- `### 4.1 ...`, two paragraphs, Table 2 as three table items + one caption, `### 4.2 Generalization to novel rewards`, last paragraph
  (continues on page 8; p0008-b001 already has `join_previous: space`, and p0007-b007 is page 7's last non-omitted item, kind text).
- Table 2 items: `Table 2 (locomotion)` -> `table-2-locomotion` (10 x 8), `Table 2 (Adroit)` -> `table-2-adroit` (8 x 5),
  `Table 2 (Kitchen)` -> `table-2-kitchen` (6 x 4). A script found no mismatch between the CSV rows and offline2.tex; each cell was also checked on 220-260-dpi crops.
  The average rows span Domain+Level in print: the label is in Domain and Level is empty.
- check: OK (155/155 lines, no number differences). No adjudication note needed.

## Summary

| Page | State | check | Adjudication note |
| --- | --- | --- | --- |
| 1 | reviewed [v2] | ATTENTION: minus glyph only (a) | yes |
| 2 | reviewed [v2] | 7 maths lines, 9 minus glyphs (a) | yes |
| 3 | reviewed [v2] | 10 maths lines, 4 minus glyphs (a) | yes |
| 4 | reviewed [v2] | 2 maths header cells of Table 1 (a) | yes |
| 5 | reviewed [v2] | 16 maths lines; minus glyphs + Algorithm 1 transcription numbers (a) | yes |
| 6 | reviewed [v2] | 4 maths lines; Algorithm 2 transcription numbers (a) | yes |
| 7 | reviewed [v2] | OK | not needed |

No category (b) diagnostics remain.

### Assets (pages 1-7)
- `table-1` (p4, CSV 7x7), `algorithm-1` (p5, image, bbox [60,517,543,655]), `algorithm-2` (p6, image, bbox [60,616,543,731]),
  `table-2-locomotion`, `table-2-adroit`, `table-2-kitchen` (p7, CSV). Both algorithms are followed by a line-numbered text transcription.
- Display equations: (1) on p2 and (2) on p5 are `$$ ... \tag{n} $$` text items. **No formula is kept as an image.**

### Joins
- Set: p0002-b001 (space; continues page 1), p0004-b003 (space; continues page 3).
- Range boundary p7 -> p8: p0007-b007 (text) is page 7's last non-omitted item; the page-8 reviewer has `join_previous: space` on p0008-b001. Consistent.

### Table 2 bold cells (for the conversion notes; bold = within 5% of the maximum per task; no markers in CSV)
All 26 bold cells match `\textbf` in offline2.tex and were confirmed on 220-260-dpi crops.
- Table 2 (locomotion): halfcheetah/medium: D-MPC (ours) 46.00, IQL 47.40 | hopper/medium: MOReL 95.40 |
  walker2d/medium: MOReL 77.80, D-MPC (ours) 76.21, Diffuser 79.70, IQL 78.30 | halfcheetah/medium-replay: CQL 45.50, IQL 44.20 |
  hopper/medium-replay: MOReL 93.60, D-MPC (ours) 92.49, Diffuser 96.80, CQL 95.00, IQL 94.70 | walker2d/medium-replay: D-MPC (ours) 78.81 |
  Locomotion Average: MOReL 66.48, D-MPC (ours) 65.98, CQL 65.45, IQL 67.47.
- Table 2 (Adroit): adroit-pen/cloned: IQL 114.05 | adroit-door/cloned: D-MPC (ours) 16.36 | adroit-hammer/cloned: D-MPC (ours) 12.27 |
  Adroit Average: IQL 44.90.
- Table 2 (Kitchen): kitchen/mixed: D-MPC (ours) 67.50 | kitchen/partial: D-MPC (ours) 73.33 | Kitchen Average: D-MPC (ours) 70.42.
- For D-MPC cells with a standard error, only the mean is bold (e.g. **46.00** (±0.17)); this also holds for Adroit IQL **114.05** (±4.78).

### TeX versus PDF
- No disagreements were found on pages 1-7. All maths and table cells taken from the TeX match the page images.

### Author typos / oddities kept as printed (all listed in the page review_notes)
- p2: "(Zhu et al.)" printed without a year.
- p3: "Q-leaning"; the product $\prod_{t}^{t+F-1}$ has lower limit "t" (same t as in the factors); SS dynamics written $p_{d}(\boldsymbol{s}_{t+1}|\boldsymbol{h}_t, \boldsymbol{a}_{t+1})$;
  mixed straight/curly quotes.
- p4 (Table 1 caption): "Diffuson Policy", "Imitiating Humans", missing comma before "DBC", space before the final period; "MOReL" (table) vs "MOREL" (caption);
  "DWM, PolyGRAD PGD" (no comma). The PDF bolds the final "s" of "Diffusion World Models" (to mark DWMS); rendered plain.
- p5: dataset $\mathcal{D}$ with $r_{1:T_1}^2$, $r_{1:T_2}^m$ superscripts and no comma before $\ldots$. Section 3.1 writes the action proposal as $\pi$ and the dynamics as $p_{s|a}$.
- p6: capital upright bold $\mathbf{A}$ for action sequences in Section 3.4 (TeX `\vA` = `\mathbf{A}`).

### Proposals for shared files (coordinator)
- plan.json notes (suggested text):
  1. "Table 1 is stored as CSV. Its three header levels (Factored $p_{d}(s|a)\,\rho(a)$ / Joint $p_{j}(s,a)$ / Model-free $\pi(a)$; Dyna / MPC; single-/multi-step)
     are repeated in combined column names joined with ' / ', because CSV cannot merge cells."
  2. "Table 2 is one float with one caption and three printed sub-tables, stored as table-2-locomotion, table-2-adroit and table-2-kitchen. Their 'Average' rows span the Domain and Level
     columns in print; in the CSV the label is in Domain and Level is empty. Bold (scores within 5% of the per-task maximum) cannot be shown in CSV. The bold cells are: <list above>."
  3. Optional: "Bold vectors $\boldsymbol{s}, \boldsymbol{a}, \boldsymbol{h}$ follow the authors' `\bm` macros; $\mathbf{A}$ (upright) is the authors' `\myvec{A}`."
- reading_order: not needed. On page 6, Algorithm 2 was moved within the page (from after the Section 4 question list to the end of Section 3.3),
  so the page JSON order is enough.
- Navigation: headings on pages 1-7 are `#` title, `## Abstract`, `## 1 Introduction`, `## 2 Related work`, `## 3 Method`, `### 3.1`-`### 3.4`,
  `## 4 Experiments`, `### 4.1`, `### 4.2`, all as printed.
- Asset names: there are no clashes within pages 1-7. `table-2-*` follows the assignment.

### Limitations
- Page 1 author blocks: each author is one item with name, affiliation and email on separate lines. The printed layout (email right-aligned) is not kept.
- The footnote marker for the corresponding author is `[^*]` with a text item `Footnote ∗: ...`. The brief only gives numeric examples.

### Remarks on the brief
- The brief's rule that "the item immediately before must be text or caption" is ambiguous when a page starts with an omitted running header. The builder
  (reading_package.py) skips omit items, so a page-start join after an omitted header is valid. Stating this explicitly would save a lookup.
- For algorithm transcriptions, the brief could say that the transcription's numbers appear as "extra" in the number check (the source lines are
  inside the excluded crop). That is expected category (a).
