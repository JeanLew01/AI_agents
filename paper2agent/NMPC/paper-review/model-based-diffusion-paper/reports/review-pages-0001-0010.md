# Review report: Model-Based Diffusion for Trajectory Optimization, PDF pages 1-10

Reviewer range: `pages/page-0001.json` ... `page-0010.json` of `documents/s001-model-based-diffusion` (brief version 2).
TeX source used as an aid: `NMPC/tex-source/model-based-diffusion/` (arXiv v1). The PDF is the NeurIPS camera-ready and wins on every disagreement.

## Per-page log

### Page 1 (done, `[v2]`)
- Items: title heading, author block, `## Abstract`, abstract, `## 1 Introduction`, first introduction paragraph, Figure 1 (`figure-1`, bbox [229,509,509,689.8]) + caption, NeurIPS conference notice.
- Changes: author superscripts to LaTeX; narrow wrapped paragraph checked against `10intro.tex`.
- Diagnostics left: 1 missing line (author line; category (a), `\dagger` letters). Adjudication note written.
- Joins: none (the paragraph ends on page 1; page 2 starts a new paragraph).

### Page 2 (done, `[v2]`)
- Items: 2 introduction paragraphs, 3 contribution bullets, `## 2 Related Work`, 3 run-in-titled paragraphs, page number omitted. No maths, no floats.
- Diagnostics: `OK` (53/53).
- Joins: last paragraph continues on page 3 (join set on page 3's first item).

### Page 3 (done, `[v2]`)
- Items: end of Trajectory Optimization paragraph (join=space), Diffusion for Planning, Langevin-based MCMC paragraph, `## 3 Problem Statement and Background`, Notations, problem statement, equations (1a)-(1d) as LaTeX text (four `$$` blocks with `\tag`), Footnote 1, 'where ...' paragraph (continues on page 4).
- TeX vs PDF: the Langevin-based MCMC paragraph is only in the PDF (transcribed from the image). Line (1d) is printed as `T - 1.3` (stray `3`; TeX has `T-1.`): kept as printed.
- Diagnostics left: 14 missing lines (all maths, category (a)); number differences are minus-glyph only (`−1` vs `-1`, `−1.3` vs `-1.3`). Adjudication note written.

### Page 4 (done, `[v2]`)
- Items: end of the 'where ...' paragraph (join=space), sampling-problem paragraph, equation (2), long paragraph, equation (3), backward-process paragraph, equations (4) and (5) (two items), MFD paragraph, `## 4 Model-Based Diffusion`, section overview.
- TeX vs PDF: the PDF prints the Gaussian second arguments as `(1-\alpha_i) I` (inline) and `(1-\bar{\alpha}_i) I` (equation (3)); the arXiv TeX has `\sqrt{1-\alpha_i} I` and `\sqrt{1-\bar{\alpha}_i} I`. PDF form used.
- Diagnostics left: 18 missing lines (maths, category (a)); number differences are the minus glyph only (17 x `−1` vs `-1`). Adjudication note written.

### Page 5 (done, `[v2]`)
- Items: `### 4.1 Model-based Diffusion as Multi-stage Optimization`, Figure 2 (`figure-2`, bbox [107,108,505,204.5], three panels + colour bar) + caption, two paragraphs, equation (6), paragraph, equations (7a)-(7c) (one item, three tagged `$$` blocks), paragraph, equation (8).
- All five display equations are LaTeX text now (no formula images).
- Diagnostics left: 26 missing lines (maths, category (a)); number differences are `−1` glyph / `\frac{1}{2}` only. Adjudication note written.
- Notes: authors' "log-likelihood gradient" wording and the legend spelling "MC Score Ascend" (inside the figure image) kept.

### Page 6 (done, `[v2]`)
- Items: intro sentence, equations (9a)-(9b) (one item, two tagged `$$` blocks), Table 1 (`table-1`, 5x3 cells) + caption, 'Comparison between MFD and MBD', Footnote 2, 'How diffusion helps?', 'Connection with Sampling-based Optimization' (continues on page 7).
- Reading fix of substance: the raised `2` after `(Y^{(i)} - \arg\max p_i(\cdot))` is the marker of footnote 2, not a square (the earlier draft had it as an exponent; TeX confirms `\footnote`). Footnote markers are written `[^n]` (pages 3, 6, 8).
- Diagnostics left: 31 missing lines (maths, category (a)); number differences are minus-glyph / spacing only. Adjudication note written.

### Page 7 (done, `[v2]`; was raw extraction)
- Items: end of the page-6 paragraph (join=space), Algorithm 1 image (`algorithm-1`, bbox [106,70.5,506,189]) + line-by-line transcription, `### 4.2 Model-based Diffusion for Trajectory Optimization`, paragraph, equations (10a)-(10d) (one item, four tagged `$$` blocks), paragraph, `### 4.3 Model-based Diffusion with Demonstration`, paragraph (ends with split word `pro|cess`, hyphen removed; page 8 joins with `none`).
- Reading order changed: the top-of-page algorithm float now follows the paragraph it interrupts.
- TeX vs PDF: PDF prints "score estimation" (TeX typo "esitimation").
- Printed as is: Algorithm 1 line 3 uses `\bar{\alpha}_{i-1}` while equation (8) uses `\bar{\alpha}_i`.
- Diagnostics left: 22 missing lines (maths, category (a)); number "extras" all come from the Algorithm 1 transcription (its source lines are inside the image crop). Adjudication note written.

### Page 8 (done, `[v2]`; was raw extraction)
- Items: end of the page-7 paragraph (join=`none`, split word `pro|cess`), Algorithm 2 image (`algorithm-2`, bbox [106,70.5,506,191]) + line-by-line transcription, paragraph, equation (11), paragraph, equation (12), paragraph, equation (13), Footnote 3, `## 5 Experimental Results`, two paragraphs, `### 5.1 MBD for Planning in Contact-rich Tasks`, first lines of its paragraph (continues on page 9).
- TeX vs PDF: the sentence about receding-horizon MBD (Appendix A.6, 9.6%) exists only in the PDF.
- Text repairs: `9 . 6%` -> `9.6%`, `blackbox` -> `black-box`; authors' typo "seperating" kept.
- Diagnostics left: 14 missing lines (maths, category (a)); number "extras" all come from the Algorithm 2 transcription. Adjudication note written.

### Page 9 (done, `[v2]`; was raw extraction)
- Items: end of the page-8 paragraph (join=space), comparison paragraph, Table 2 (`table-2`, 8x6) + caption (with the `*RL ...` remark), Table 3 (`table-3`, 8x6) + caption, Figure 4 (`figure-4`, bbox [107,580,505,669]) + caption.
- Reading order changed: the two top-of-page tables now follow the prose they interrupt.
- Tables: cells verified against the 280-dpi crops and position-wise against the native text lines (script). Negative Table 2 entries keep the printed minus sign U+2212.
- TeX vs PDF: the "Please note RL is only used for performance reference ..." sentences exist only in the PDF (they replace an arXiv sentence); "CMAES" repaired to "CMA-ES".
- Diagnostics: primary check `OK` (116/116, no number differences). Second parser splits 19 Table 2 decimals (`0.65` -> `0`, `65`); adjudication note written.

### Page 10 (done, `[v2]`; was raw extraction)
- Items: Figure 3 (`figure-3`, bbox [106,70,507,231]) + caption, `### 5.2 Data-augmented MBD for Trajectory Optimization`, three paragraphs, `## 6 Conclusion and Future Work`, conclusion, `## Acknowledgments`, funding sentence, `## References`, entry `[1]`.
- Text repairs: `highdimensional` -> `high-dimensional` in the caption; headings de-bolded and levelled.
- TeX vs PDF: citation `[1]` after "CMU Mocap dataset" and the Acknowledgments paragraph exist only in the PDF.
- Diagnostics: `OK` (41/41).

## Summary

### State
All ten pages are `reviewed: true` with `review_notes` starting `[v2]`. Every page was compared with its preview and, where there is maths, a float or a table, with 200-300 dpi crops. Pages 1-6 had been partly edited under brief version 1 (HTML `<sup>/<sub>` maths, formula images); pages 7-10 were raw extraction.

### Assets
| Page | Asset | Label | Kind |
| --- | --- | --- | --- |
| 1 | `figure-1` | Figure 1 | figure |
| 5 | `figure-2` | Figure 2 | figure |
| 6 | `table-1` | Table 1 | table (5x3 cells) |
| 7 | `algorithm-1` | Algorithm 1 | image + text transcription |
| 8 | `algorithm-2` | Algorithm 2 | image + text transcription |
| 9 | `table-2` | Table 2 | table (8x6 cells) |
| 9 | `table-3` | Table 3 | table (8x6 cells) |
| 9 | `figure-4` | Figure 4 | figure |
| 10 | `figure-3` | Figure 3 | figure |

No asset name or item id is duplicated anywhere in the 30 page plans (checked by script at the time of writing). Figure 3 is printed on page 10 and Figure 4 on page 9; both stay on their printed pages.

### Display equations (all LaTeX text, none kept as image)
- Page 3: (1a)-(1d). Page 4: (2), (3), (4), (5). Page 5: (6), (7a)-(7c), (8). Page 6: (9a)-(9b). Page 7: (10a)-(10d). Page 8: (11), (12), (13).
- Grouped equations are one text item with one `$$ ... \tag{..} $$` block per printed number, so every printed number is visible.
- Formulas kept as images: none. The former `formula` items and their asset names (`equation-1a-1d`, `equation-2`, ..., `formula-p0007-005`, `formula-p0008-00x`) no longer exist.

### Joins
- Set: page 3 first item (`space`), page 4 first item (`space`), page 7 first item (`space`), page 8 first item (`none`, word `pro|cess`; hyphen removed on page 7), page 9 first item (`space`).
- Range boundaries: page 1 starts the paper; page 10 ends with the complete reference entry `[1]`, page 11 starts with `[2]`, so no join is needed at the 10/11 boundary.
- Float order: on pages 7, 8, 9 the top-of-page floats (Algorithm 1, Algorithm 2, Tables 2-3) were moved behind the prose that continues from the previous page.

### TeX (arXiv v1) versus PDF (camera-ready): PDF used
- p3: whole paragraph "Langevin-based Markov Chain Monte Carlo for Global Optimization." only in PDF.
- p3: (1d) printed with a stray `3`: `\forall t = 0, 1, \dots, T-1.3` (TeX: `T-1.`). Transcribed as printed.
- p4: forward kernels printed as `\mathcal{N}(\sqrt{\alpha_i} Y^{(i-1)}, (1-\alpha_i) I)` and, in (3), `\mathcal{N}(\sqrt{\bar{\alpha}_i} Y^{(0)}, (1-\bar{\alpha}_i) I)`; TeX has `\sqrt{1-\alpha_i} I`, `\sqrt{1-\bar{\alpha}_i} I`.
- p7: "score estimation" (TeX: "esitimation").
- p8: sentence on receding-horizon MBD (Appendix A.6, 9.6%) only in PDF.
- p9: "Please note RL is only used for performance reference not as there is no existing TO method ... Appendix A.8 and A.6." only in PDF; Table 2 header `RL*` and the caption remark only in PDF.
- p10: `[1]` citation for the CMU Mocap dataset and the Acknowledgments only in PDF.

### Text repairs of substance
- p6: the raised `2` after `(Y^{(i)} - \arg\max p_i(\cdot))` is footnote marker 2, not an exponent (was `<sup>2</sup>` read as a square in the earlier draft).
- p8: `9 . 6%` -> `9.6%`, `blackbox` -> `black-box`. p9: `CMAES` -> `CMA-ES`, split decimals in both tables. p10: `highdimensional` -> `high-dimensional`.
- Authors' errors kept as printed: "seperating" (p8), "tasks includes" (p9), "reference not as there is" (p9), "Its log-likelihood gradient is $\nabla p_{i\mid 0}$" (p5), `\bar{\alpha}_{i-1}` in line 3 of both algorithms versus `\bar{\alpha}_i` in (8), `\alpha_0` in the CEM paragraph (p6), in-figure legend "MC Score Ascend" (p5).

### Remaining diagnostics (all category (a); adjudication notes in `adjudication-notes/page-000N.json`)
| Page | Status | Missing lines | Number differences |
| --- | --- | --- | --- |
| 1 | ATTENTION | 1 (author line, `\dagger`) | none |
| 2 | OK | 0 | none |
| 3 | ATTENTION | 14 (maths) | minus glyph (`−1`/`-1`, `−1.3`/`-1.3`) |
| 4 | ATTENTION | 18 (maths) | minus glyph (17 x) |
| 5 | ATTENTION | 26 (maths) | minus glyph, `\frac{1}{2}` |
| 6 | ATTENTION | 31 (maths) | minus glyph / spacing |
| 7 | ATTENTION | 22 (maths) | extras only: Algorithm 1 transcription |
| 8 | ATTENTION | 14 (maths) | extras only: Algorithm 2 transcription |
| 9 | OK | 0 | second parser only: splits 19 Table 2 decimals |
| 10 | OK | 0 | none |

No category (b) item remains. Pages 2 and 10 have no note file because they have no diagnostics.

### Proposals for shared files (not applied by me)
1. `plan.json` note: "Equation (1d) on PDF page 3 is printed as `T - 1.3`; the trailing 3 is a stray character in the camera-ready (arXiv source: `T-1.`)."
2. `plan.json` note: "Footnote markers in the main text are written `[^n]`; the footnote text is the item starting `Footnote n:` on the same page." (I used `[^n]` instead of `$^{n}$` because marker 2 on page 6 directly follows a formula and would read as a square.) If the other reviewers of this paper use another marker form, please harmonise.
3. Reference style: page 10 has `[1] ...` without a list bullet, as the brief asks; page 11 (v1 state when I looked) still has `- [2] ...` bullets. One form should be used through pages 10-13.
4. Heading level: `## Acknowledgments` (unnumbered, printed in subsection type size) is at section level so that it is not nested under `6 Conclusion and Future Work`.
5. Table 1 cells contain LaTeX (`$Y^{(0)}$`, `$p_0(\cdot)$`), so the CSV holds LaTeX strings.
6. Conversion note candidates: underlined initials of "Model-Based Diffusion" in the abstract and the green "data augmentation" in the Figure 4 caption are not representable.

### Limitations
- LaTeX was checked for balanced `$`, braces and parentheses by script and read against the crops, but was not rendered with a TeX/KaTeX engine.
- Algorithm transcriptions have no indentation for the loop body; the `for ... do` / `end for` lines delimit it, and the image crops show the layout.
- Table 2 marks the best method in bold in print; the styling is dropped in the cells (MBD is best in every row).

### Notes on the brief
- "Footnotes at the end of that page's items" conflicts with "the page ends with the prose that continues onto the next page" (a footnote as last item would also break `join_previous`). On pages 3, 6 and 8 the footnote sits before the continuing item.
- The brief does not say how the in-text footnote marker should be written; a fixed form would help (see proposal 2).
- The number check treats U+2212 and ASCII `-` as different tokens, so every LaTeX `i-1` yields a number difference; normalising the minus sign in the tool would remove most of these entries.
- The transcription that the brief requires after an algorithm image always produces "extra" numbers, because the source lines are inside the image crop.
