# Review report: Diffusion differentiable resampling, pages 24-32

Reviewer range: PDF pages 24-32 (appendix J tail, K, L, M, N, O, P). Brief: `_tools/REVIEWER_BRIEF.md` ([v2]).
TeX: `tex-source/diffusion-resampling/main.tex` used for all maths and table cells; PDF checked for each.

## Per-page log

### Page 24 — done ([v2])
- First item `p0024-b003` ("we compute the log-likelihood ...") continues page 23's last paragraph (`p0023-b010`, "... In particular,"): `join_previous: "space"`.
- Table 12 (prey-predator, section J): caption `p0024-b001` once, then `table-12-rmse` (`p0024-b002`) and `table-12-success` (`p0024-b002b`); NaN cells as printed; two-level headers flattened as "Euler–Maruyama ODE" etc. Placed after the completed continuation paragraph.
- Last item `p0024-b007` ends mid-sentence ("we consider end-to-end training"), continues on page 25.
- Remaining diagnostics: missing lines / number differences / second-parser differences — all category (a) (LaTeX maths, minus glyph, second parser glues row label "K = 4" with "20"). Adjudication note written.

### Page 25 — done ([v2])
- First item `p0025-b005` ("*with* resampling, ...") continues page 24: `join_previous: "space"`.
- Table 13 (`table-13`, three-level header flattened, asterisks kept: `0.508* ± –`, `16.7* ± –`, `0.763** ± 0.103`, `19.3** ± 0.84`), Table 14 (`table-14`); captions before tables; both placed after the completed continuation paragraph.
- Run-in bold titles "Identifiability of the latent space", "Network architectures". Last item ends mid-sentence ("which embeds the angle and scales") → page 26.
- Remaining: 6 missing lines, all category (a) (inline maths). Adjudication note written.

### Page 26 — done ([v2])
- First item `p0026-b005` ("the velocity. ...") continues page 25: `join_previous: "space"`.
- Table 15 (`table-15`, three-level header flattened, `*` markers kept), Table 16 (`table-16`, `*`/`**` kept; its caption was mis-kinded as text, fixed). Placed after the completed continuation paragraph.
- Heading `## L. Bayesian neural network training`. Equation (38): extractor formula image replaced by text `$$\begin{aligned}...\end{aligned}\tag{38}$$` from TeX (`\cond` expanded); equation and the following "for CIFAR10 classification, ..." joined with `space` (one sentence).
- Remaining: 11 missing lines and number diffs ('7' = mapsto glyph, '−1' minus in $z_{j-1}$), all category (a). Adjudication note written.

### Page 27 — done ([v2])
- Page 26 ends with a complete sentence; no join. Floats first as printed: `figure-8` [50,62,547,231] + caption, `figure-9` [171,318,425,491] + caption, Table 17 caption + `table-17`; then the pBNN paragraph.
- Table 17: bold on the Diffusion cells (87.81, 87.76) is lost in CSV (noted).
- Remaining: 1 missing line + number differences from thousands separators in $d_z = 1,856$, $d_\theta = 11,172,106$ — category (a). Adjudication note written.

### Page 28 — done ([v2]), check OK
- Figure 10: 21 extractor picture fragments merged into `figure-10` [53,63,545,339] (four 2x4 snapshot grids with labels (a)-(d)); caption kept with the authors' unclosed parenthesis "(mean SSIM/PSNR 0.761/17.0, b) ...".
- `figure-11` [52,419,546,622] + caption. No prose on this page.

### Page 29 — done ([v2])
- Heading `## M. Weather forecast`. Table 18 is printed above the M heading but belongs to M: moved caption + `table-18` after the "Results and evaluation" paragraph (first citation); page ends with "Our results show ... drawn from the" → page 30.
- Cells as printed incl. "(T = 1, K = 4,ODE)". Removed `<sup>` damage that had swallowed prose into superscripts.
- Remaining: 15 missing lines + minus-sign number differences, all category (a). Adjudication note written.

### Page 30 — done ([v2])
- First item `p0030-b003` ("held-out evaluation data. ...") continues page 29: `join_previous: "space"`.
- Table 19 caption + `table-19` after that paragraph; `figure-12` [50,393,547,672] + caption (page ends with the caption; page 31 starts a new paragraph).
- Remaining: 2 missing lines + one minus-sign token, category (a). Adjudication note written.

### Page 31 — done ([v2])
- No join (new paragraph after page 30's figure caption). Headings `## N. Choosing the hyperparameters`, `## O. Additional related work`, `## P. Take-away messages`. Four take-away bullets kept as `- ` text items.
- `\refmeasure` expanded to `\pi_{\mathrm{ref}}`. Fixed line-wrap "Euler– Maruyama".
- Remaining: 6 missing lines, category (a) (inline maths). Adjudication note written.

### Page 32 — done ([v2])
- Only Table 20: caption + `table-20` [74,376,519,455], 6x5 cells with LaTeX maths inside cells.
- Remaining: 7 missing lines + minus-sign tokens, category (a). Adjudication note written.

## Summary

All 9 pages (24-32) are `reviewed: true` with `[v2]` notes; adjudication notes written for pages 24-27 and 29-32 (page 28 checks OK). Every remaining diagnostic is category (a): LaTeX maths vs PDF glyph text, U+2212 minus vs ASCII hyphen, the mapsto glyph read as '7' (p26), math-mode thousands separators (p27), and the second parser gluing a row label digit to the first cell in Table 12 (p24). No category (b) items remain.

### Assets (asset name — item id — page)
- `table-12-rmse` (p0024-b002), `table-12-success` (p0024-b002b) — p24, caption `p0024-b001` once, before both
- `table-13` (p0025-b002), `table-14` (p0025-b004) — p25
- `table-15` (p0026-b002), `table-16` (p0026-b004) — p26
- `figure-8` (p0027-b001), `figure-9` (p0027-b003), `table-17` (p0027-b006) — p27
- `figure-10` (p0028-b001; merged from 21 fragments), `figure-11` (p0028-b023) — p28
- `table-18` (p0029-b002) — p29
- `table-19` (p0030-b002), `figure-12` (p0030-b005) — p30
- `table-20` (p0032-b002) — p32
- Equation (38): text `$$\begin{aligned}...\end{aligned}\tag{38}$$` (p0026-b009). No formula kept as an image.
- No asset-name clashes found across the whole document (checked all page files).

### Joins
- p0024-b003 `space` → previous item must be page 23's last item `p0023-b010` (text, "... In particular,"). **Boundary dependency:** the reviewer of pages 16-23 must keep that paragraph as the last non-omit item of page 23 (no float after it).
- p0025-b005 `space`, p0026-b005 `space`, p0026-b009 (eq. 38) `space`, p0026-b010 `space`, p0029→p0030: p0030-b003 `space`.
- No join at p27, p28, p31, p32 (new paragraphs / floats only).

### Float placement (within-page reorders, no plan.json `reading_order` needed)
- p24/25/26/30: page starts with the continuation prose; the top-of-page tables follow that paragraph.
- p29: Table 18 is printed above the `## M. Weather forecast` heading but belongs to M; placed after the "Results and evaluation" paragraph. If the coordinator prefers strict printed order, it would have to sit before the heading (then section L would end with Table 18).

### Headings
`## K.` is on page 23 (other reviewer). Mine: `## L. Bayesian neural network training` (p26), `## M. Weather forecast` (p29), `## N. Choosing the hyperparameters`, `## O. Additional related work`, `## P. Take-away messages` (p31). Run-in bold titles kept in text: Experiment settings / Results and evaluation / Identifiability of the latent space / Network architectures (K); Experiment settings / Training details / Results and evaluation (M).

### TeX vs PDF
No disagreements found in pages 24-32 (all table cells and maths matched). Macros expanded: `\cond` → `\;|\;`, `\R` → `\mathbb{R}`, `\diag{0,1}` → `\operatorname{diag}(0,1)`, `\refmeasure` (defined in main.tex line 124) → `\pi_{\mathrm{ref}}`.

### Notable authors' text kept as printed
"indicate" (p24), "a Markovian dynamics", "a batch data" (p26), "be stochastic"/"score is shown" (p27), Figure 10 caption's unclosed parenthesis "(mean SSIM/PSNR 0.761/17.0, b) ...", Figure 11 "and correspond" (p28), "Tables 18 and Table 19" (p29), "a complete information", "targets at" (p31), "(T = 1, K = 4,ODE)" missing space in Tables 18/19.

### Limitations
- CSV cannot hold bold: Table 17's best values (Diffusion 87.81, 87.76) lose their bold.
- Table cells use plain Unicode ("T = 1, K = 4", "ε", "±") except Table 20, whose cells contain enough maths that LaTeX `$...$` was used inside cells.
- Running header omitted with reason "Running header (paper title ...) repeated on every page" — the coordinator may want the same wording on other ranges.

### Brief feedback
- The brief's join rule ("first item of your first page, look at the previous page") depends on another reviewer's ordering of page 23; a note in the brief that boundary pages must keep continuing prose last would help.
- `check` does not accept LaTeX `$80$%` as "80%" — writing percentages outside maths avoids a spurious number diff; worth a line in the brief.
