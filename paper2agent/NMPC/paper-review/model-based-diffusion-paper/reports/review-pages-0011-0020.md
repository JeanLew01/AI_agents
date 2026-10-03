# Review report: Model-Based Diffusion for Trajectory Optimization, PDF pages 11-20

Reviewer range: pages 11-20, brief version 2. Document: `model-based-diffusion-paper/documents/s001-model-based-diffusion`.
TeX aid: `tex-source/model-based-diffusion/90appendix.tex` (appendix), `main.tex` (macros), `main.bbl` (arXiv v1 bibliography). The PDF is the NeurIPS camera-ready and wins.

State: all ten pages are finished, `reviewed: true`, `review_notes` start with `[v2]`. The run was interrupted once by a machine restart (after page 16 was saved); pages 17-20 were finished after the restart. Nothing is left unmarked.

## Per-page state

| Page | Content | check result | Adjudication note |
| --- | --- | --- | --- |
| 11 | References [2]-[19] | OK, 45/45 | none needed |
| 12 | References [20]-[38] | OK, 46/46 | none needed |
| 13 | References [39]-[57] | OK, 43/43 | none needed |
| 14 | References [58]-[64], rest blank | OK, 16/16 | none needed |
| 15 | A, A.1 notation table, A.2: Definition 1, Proposition 2, start of proof | 22 missing lines, no number differences | `missing_lines` |
| 16 | Proof of Proposition 2, equations (14a)-(20c) | 79 missing lines, no number differences | `missing_lines` |
| 17 | End of proof, Definition 3, Proposition 4, start of proof, equations (21a)-(25) | 45 missing lines, no number differences | `missing_lines` |
| 18 | End of proof of Proposition 4, (26)-(28), Proposition 5, A.3, Figure 5 | 12 missing lines, no number differences | `missing_lines` |
| 19 | Rest of A.3, A.3.1, A.4 start, equations (29)-(32), footnotes 4-5 | 6 missing lines, number differences (both parsers) | all three keys |
| 20 | Rest of A.4, Figure 6, A.5, A.5.1 items 1-4 | 15 missing lines, number differences (both parsers) | all three keys |

All remaining diagnostics are category (a): LaTeX versus the PDF glyph layer, Greek letters written as LaTeX commands, equation fragments, and two symbol-font artefacts described below. No category (b) item remains.

## Progress log (one entry per finished page)

- **Page 11** (references [2]-[19]): list bullets removed, one entry per item in printed style `[n] ...`. `$\mathbb{R}^n $` in [16] is printed literally (uncompiled BibTeX maths) and kept.
- **Page 12** (references [20]-[38]): bullets removed. Printed peculiarities kept: `$\mathbb{R}^d $` in [21]; missing symbol in "Large-Scale -Regularized" in [36].
- **Page 13** (references [39]-[57]): bullets removed. [57] is printed without venue and year.
- **Page 14** (references [58]-[64]): bullets removed. End of the reference list.
- **Page 15**: headings `## A Appendix / Supplemental Material`, `### A.1 Notation Table`, `### A.2 Convergence of Distribution with Small $\lambda$`. Notation table as cells with LaTeX symbols. Three unnumbered display equations converted from images to `$$`. `**Definition 1.**`, `**Proposition 2.**`, `**Proof.**`. Last item continues on page 16.
- **Page 16**: seven formula images converted to `$$` blocks with `\tag{14a}` ... `\tag{20c}`. First item has `join_previous: space` (previous item is prose on page 15).
- **Page 17**: eight formula images converted ((21a), (21b), (22), (23), (24), (25) and three unnumbered displays). `**Definition 3.**`, `**Proposition 4.**`, `**Proof.**`. `\Gamma(\alpha_k + 1)` written with the printed spacing, which removed a `1` versus `+1` number difference.
- **Page 18**: (26), (27), (28) and the unnumbered limit of Proposition 5 converted. `**Proposition 5.**`. Heading `### A.3 Black-box Optimization with MBD`. Figure 5 box widened on the left. Last item continues on page 19.
- **Page 19**: (29)-(32) converted to four `$$` blocks in one item. Footnotes as `[^4]`, `[^5]` and `Footnote n: ...` items. Headings `#### A.3.1 MBD for DNN Training without Gradient Information`, `### A.4 MBD with Demonstration Explaination`. First item has `join_previous: space`.
- **Page 20**: inline stacked fractions rewritten in LaTeX; Figure 6 box checked; headings `### A.5 Experiment Details`, `#### A.5.1 Simulator and Environment`; list items 1-4. Last item continues on page 21.

## Figures, tables, equations by page

| Page | Item | Asset name | Box (PDF pt) |
| --- | --- | --- | --- |
| 15 | Notation table (Appendix A.1), cells, 1 header + 9 rows x 2 columns | `table-a1-notation` | [129,124,483,251] |
| 18 | Figure 5 (six panels and legend row) | `figure-5` | [106,479,508,646] |
| 20 | Figure 6 (two panels with legends) | `figure-6` | [106,70,508,196] |

Display equations, all as `$$` text with `\tag`: page 16 (14a)-(14d), (15a)-(15b), (16), (17), (18), (19), (20a)-(20c); page 17 (21a)-(21b), (22), (23), (24), (25); page 18 (26), (27), (28); page 19 (29)-(32). Unnumbered displays: page 15 three (definition of $V_F(t)$, polynomial bounds, limit in Proposition 2), page 17 three (choice of $\epsilon_k$, definition of $J^*_{\mathcal{B}}(\delta)$, limit in Proposition 4), page 18 one (limit in Proposition 5).

No formula is kept as an image. No algorithm on these pages. The old asset names `equation-*` and `formula-p00NN-k` no longer exist in pages 15-19.

## Joins

- Set: page 16 first item (`space`, continues "Consider the" from page 15); page 19 first item (`space`, continues "Firstly, the implementation of a" from page 18).
- Not set on purpose: page 20 first item ("where demonstrate likelihood term ...") follows the `$$` block (32) on page 19, so it has no `join_previous` (coordinator's convention).
- Range boundaries: page 11 starts with a new reference entry, no join to page 10. Page 20's last item (list item 4, "... the agent and control") continues on page 21, whose first item already has `join_previous: space`.

## TeX versus PDF

- Bibliography: `main.bbl` (arXiv v1) is a different list (fewer entries, other order and numbering). The PDF list was transcribed; the TeX was not used for pages 11-14.
- Page 15: the notation table (A.1) exists only in the PDF. The A.2 heading is "Convergence of Distribution with Small λ" in the PDF and "Small Temperature" in the TeX.
- Pages 15-20 body: no other difference found between `90appendix.tex` and the PDF. Section numbers differ only because A.1 was inserted (TeX has no A.1).

## Text repairs of substance

- Reference pages: none beyond bullet removal; hyphen repairs from the earlier pass were re-checked.
- Page 19: footnote markers and footnote items changed to the convention of pages 1-10; the two footnote items sit after the BAxUS paragraph (before the A.3.1 heading), because the page ends with display (32) whose sentence continues on page 20.
- Theorem-like statements are printed in italics; the italic markup is not reproduced (label in bold, statement plain with LaTeX maths).
- End-of-proof boxes (pages 17 and 18) are written as `$\square$` at the end of the last proof sentence.
- Numbers in A.3.1 (page 19) are typeset in maths mode in print and written as plain text (85.5%, 256, 2s, 92.7%, 2, 32, 784, 10, 27,562).

## Printed peculiarities kept (not corrected)

- Page 15: "setp" in the notation table; `$Y_*$` inside the norm next to `$Y^*$`; capital `$P(Y)$` for the density; ", It follows that:".
- Page 16: `exp` set as italic letters in (14c), (14d), (20a)-(20c) and one inline formula, upright `\exp` elsewhere; `$V(\epsilon)$` without subscript in (20a); "becuase"; (15a) has no integral sign before the second right-hand term.
- Page 17: factor `$\lambda^{k+1}$` in (21a)/(21b) and lower limit `$\frac{\epsilon}{\lambda}$` on the left side of (21b); `$\max \epsilon_0, \epsilon_1, \cdots, \epsilon_M$` without braces; "golbal"; "sufficient small".
- Page 18: "$J(Y^*)$. and any sufficient small"; "And From"; "The diffused $Y_i$ converge in density"; second Gaussian argument `$\sqrt{1-\bar{\alpha}_i} I$`.
- Page 19: "eqauls", "demostration", "Explaination"; `$w_{\text{demo}}((Y^{(0)}))$` with doubled brackets in (32).
- Page 20: "aviod", "it will yields", "MC Score Ascend" (panel title inside Figure 6).
- Upright bold `$\mathbf{Y}$` and bold italic `$\boldsymbol{Y}$` alternate in A.2 as printed.

## Remaining diagnostics (all category (a))

- Pages 15-18: missing lines only; every line contains LaTeX maths or a Greek letter. The text layer renders the "p over arrow" as `pÐ→` (pages 17, 18).
- Page 19: 6 equation fragments; `−1` versus `-1` from `$Y^{(i-1)}$`; second parser splits the printed `27, 562` into `27` and `562`.
- Page 20: 13 lines with maths; 2 lines and the number `8` (twice) come from the green star symbol, which the text layer encodes as the digit 8 (output has `★`); `−0.4` versus `0.4` from the binary minus in `$||Y| - 0.4| > 0.3$`.

## Proposals for shared files

- `plan.json` notes: (1) "The bibliography and the notation table (A.1) follow the NeurIPS camera-ready PDF; the arXiv v1 TeX source has a different reference list and no notation table." (2) "Coloured words and symbols in captions (red 'MBD', blue 'Gaussian Process-based Bayesian Optimization', green star and circle in Figure 6) are reproduced without colour; the symbols are written as ★ and ●."
- Navigation headings: the A.2 heading contains inline LaTeX (`$\lambda$`). If the navigation needs plain text, "A.2 Convergence of Distribution with Small λ" is the printed form.
- Asset names: `figure-5`, `figure-6`, `table-a1-notation` are unique in the document at the time of the check (pages 1-30 scanned).
- `plan.json` title is still the file stem "model-based-diffusion"; the printed title is "Model-Based Diffusion for Trajectory Optimization".

## Limitations

- Italic type (theorem statements, journal names are kept, statement italics are not) and text colour are not fully reproduced.
- `$\mathbb{R}^n $` and `$\mathbb{R}^d $` in references [16] and [21] are literal printed text; a Markdown renderer will show them as maths.
- Equation alignment is not reproduced: each numbered line is its own `$$` block and continuation lines start with their relation sign.

## Notes on the brief

- The brief asks for footnotes at the end of the page's items and also for the page to end with the prose that continues onto the next page. On page 19 the page ends with a display equation whose sentence continues on page 20, so the footnotes were placed after the paragraph group that cites them. A rule for this case would help.
- The rule "no `join_previous` after a `$$` block" came from the coordinator's message, not from the brief; it should be added to the brief.
- The check counts Greek letters as letters, so every prose line with a single `λ` or `δ` is reported as missing once it is LaTeX. This makes the missing-line lists long on proof pages (79 on page 16) although nothing is wrong.
