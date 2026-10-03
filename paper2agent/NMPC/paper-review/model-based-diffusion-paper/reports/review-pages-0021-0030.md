# Review report: Model-Based Diffusion for Trajectory Optimization, PDF pages 21-30

Reviewer range: `pages/page-0021.json` ... `page-0030.json` of `documents/s001-model-based-diffusion` (brief version 2).
TeX source used as an aid: `NMPC/tex-source/model-based-diffusion/90appendix.tex` (arXiv v1). It ends with A.5.4, so A.6, A.7, A.8,
Algorithm 3, Table 7, Figures 7-9 and the NeurIPS checklist exist only in the PDF and were transcribed from the page images.
Starting state: all ten pages were raw extraction (`reviewed: false`, no notes).

## Per-page log

### Page 21 (done, `[v2]`)
- Items: end of list item 4 (Halfcheetah) from page 20 (join=space), list items 5-8 (Humanoidrun, Humanoidstandup, PushT, Car2D), `#### A.5.2 MBD Hyperparameters`, paragraph, Table 4 (`table-4`, 8x4 cells) + caption, noise-schedule paragraph, `#### A.5.3 Baseline Algorithms Implementation`, two paragraphs, `#### A.5.4 Demonstration Collections`, two paragraphs, page number omitted.
- Maths: Car2D state/action/dynamics and the noise schedule in LaTeX from `90appendix.tex`, checked on 280/220-dpi crops. TeX and PDF agree on this page.
- Repairs: fraction `v/L` (was `<sup>` debris), `0 _._ 2` -> `0.2`, ` : ` after bold task names.
- Authors' wording kept: "continous", "MBD is very little hyperparameters", "schedulling", "the hyperparameters is ported", "we the same hyperparameters".
- Diagnostics left: 6 missing lines (maths, category (a)); number differences are the minus glyph in `10^{-4}`, `10^{-2}`. Adjudication note written.

### Page 22 (done, `[v2]`)
- Items: Table 5 (`table-5`, 9x5) + caption, Table 6 (`table-6`, 9x5) + caption, `### A.6 MBD for Online Control`, two paragraphs, Table 7 (`table-7`, 7x2) + caption, `### A.7 Sample Number Abalation` (printed spelling), one paragraph, page number omitted.
- Tables 5-6 agree with `90appendix.tex`; A.6, Table 7, A.7 are PDF-only (checked on crops and native lines).
- Table 6 Learning Rate cells in LaTeX (`$3 \times 10^{-4}$`, `$6 \times 10^{-4}$`). Repair: `9 _._ 6%` -> `9.6%`.
- Reading order as printed (top-of-page tables do not interrupt a sentence; page 21 ends with complete paragraphs).
- Diagnostics left: 8 missing lines (the eight Learning Rate cells, category (a)); number differences are the minus glyph of `10^{-4}` only. Adjudication note written.

### Page 23 (done, `[v2]`)
- Items: Algorithm 3 image (`algorithm-3`, bbox [106,70.5,506,160]) + line-by-line transcription, Figure 7 (`figure-7`, bbox [107,168,504,415]) + caption, `### A.8 Objective Function Abalation` (printed spelling), two paragraphs, page number omitted.
- PDF-only page (no TeX): maths transcribed from 260-280-dpi crops: Algorithm 3 subscripts, `$J = \sum_{t=0}^{H_{\text{RL}}} \gamma^t r_t, H = 1000, \gamma < 1$`, `$J = \sum_{t=0}^{H_{\text{MBD}}} r_t, H = 50, \gamma = 1$`.
- Repairs: eight glyph-soup algorithm items merged into image + transcription; split decimals `9.6%`, `74.2%`, `65.3%`, `44.5%`, `805.5%`.
- Reading order as printed (floats sit between complete paragraphs; see the `reading_order` proposal below).
- Diagnostics left: 4 missing lines (A.8 formulas, category (a)); number "extras" all come from the Algorithm 3 transcription. Adjudication note written.

### Page 24 (done, `[v2]`)
- Items: Figure 8 (`figure-8`, bbox [107,70,505,273], 2x4 axes incl. the printed empty eighth axis, legend row) + caption (was typed `text`), `## NeurIPS Paper Checklist`, checklist items 1 (Claims, [Yes]) and 2 (Limitations, [Yes]) as text: number + bold title, Question, Answer, Justification, `Guidelines:`, one list item per bullet.
- Repairs: merged `Question ... Answer` and `Justification ... Guidelines:` items of item 2 split (new ids `p0024-b013b`, `p0024-b014b`).
- Last bullet continues on page 25 (join set there).
- Diagnostics: `OK` (32/32). No adjudication note needed.

### Page 25 (done, `[v2]`)
- Items: continuation of the page-24 bullet (join=space), Figure 9 (`figure-9`, bbox [107,70,504,290]) + caption, five more guideline bullets of item 2, checklist item 3 (Theory Assumptions and Proofs, [Yes]) with Question, Answer, Justification, `Guidelines:` and its first bullet, page number omitted.
- Reading order changed: the top-of-page Figure 9 now follows the bullet continuation it interrupted.
- Caption maths in LaTeX (`$\gamma = 1, H = 50$`, `$\gamma < 1, H = 1000$`); split decimals `44.5%`, `805.5%` repaired.
- Diagnostics left: 2 missing lines (caption maths, category (a)); no number differences. Adjudication note written.

### Page 26 (done, `[v2]`)
- Items: five remaining guideline bullets of item 3, checklist item 4 (Experimental Result Reproducibility, [Yes]) complete, start of item 5 (Open access to data and code: Question, Answer [Yes]); page number omitted. No maths, no floats.
- Repairs: item 4 title was a `#` heading, now text; `Justification ... Guidelines:` split (new id `p0026-b008b`); `crossreferenced` -> `cross-referenced`; the lettered sub-points (a)-(d) merged with their parent bullet into one item as a nested list (former `p0026-b014`...`b017` merged into `p0026-b013`).
- Printed as is: "In general. releasing code and data ..." (template typo).
- Diagnostics: `OK` (53/53). No adjudication note needed.

### Page 27 (done, `[v2]`)
- Items: Justification, `Guidelines:` and eight bullets of item 5; checklist item 6 (Experimental Setting/Details, [Yes]) complete; item 7 (Experiment Statistical Significance, [Yes]) up to its fourth bullet; page number omitted. No maths, no floats.
- Repairs: titles of items 6 and 7 were `#` headings, now text; the two line-broken URLs `https://nips.cc/public/guides/CodeSubmissionPolicy` rejoined (extractor spaces and backticks removed).
- Printed as is: Justification of item 5 ("... results comes with the supplemental material.").
- Diagnostics: `OK` (52/52). No adjudication note needed.

### Page 28 (done, `[v2]`)
- Items: last five bullets of item 7; checklist items 8 (Experiments Compute Resources, [Yes]) and 9 (Code Of Ethics, [Yes]) complete; item 10 (Broader Impacts, [NA]) up to its third bullet; page number omitted. No maths, no floats.
- Repair: URL in the Question of item 9 (`https://neurips.cc/public/EthicsGuidelines?`, extractor backticks and space removed).
- Diagnostics: `OK` (51/51). No adjudication note needed.

### Page 29 (done, `[v2]`)
- Items: last three bullets of item 10; checklist item 11 (Safeguards, [NA]) complete; item 12 (Licenses for existing assets, [Yes]) up to its seventh bullet; page number omitted. No maths, no floats.
- Repairs: title of item 11 was a `#` heading, now text; backticks around `paperswithcode.com/datasets` removed.
- Diagnostics: `OK` (51/51). No adjudication note needed.

### Page 30 (done, `[v2]`)
- Items: last bullet of item 12; checklist items 13 (New Assets, [NA]), 14 (Crowdsourcing and Research with Human Subjects, [NA]) and 15 (Institutional Review Board (IRB) Approvals or Equivalent for Research with Human Subjects, [NA]) complete; page number omitted. Last page of the PDF. No maths, no floats.
- Repairs: `Justification ... Guidelines:` of items 14 and 15 split (new ids `p0030-b013b`, `p0030-b020b`).
- Diagnostics: `OK` (50/50). No adjudication note needed.

## Summary

### State
All ten pages are `reviewed: true` with `review_notes` starting `[v2]`. Every page was compared with its preview; pages with maths, tables or floats (21-25) also with 150-280 dpi crops, and all pages with the native text lines. The work was interrupted once by a machine restart after page 23; pages 24-30 were done after the restart from the on-disk state.

### Assets
| Page | Asset | Label | Kind |
| --- | --- | --- | --- |
| 21 | `table-4` | Table 4 | table (8x4 cells) |
| 22 | `table-5` | Table 5 | table (9x5 cells) |
| 22 | `table-6` | Table 6 | table (9x5 cells, Learning Rate in LaTeX) |
| 22 | `table-7` | Table 7 | table (7x2 cells) |
| 23 | `algorithm-3` | Algorithm 3 | image [106,70.5,506,160] + text transcription |
| 23 | `figure-7` | Figure 7 | figure [107,168,504,415] |
| 24 | `figure-8` | Figure 8 | figure [107,70,505,273] |
| 25 | `figure-9` | Figure 9 | figure [107,70,504,290] |

No item id or asset name is duplicated anywhere in the 30 page plans (checked by script after page 30). New item ids created by splitting: `p0024-b013b`, `p0024-b014b`, `p0026-b008b`, `p0030-b013b`, `p0030-b020b`. Items removed by merging: `p0023-b002`...`b007` (into the Algorithm 3 transcription `p0023-b001`), `p0026-b014`...`b017` (into `p0026-b013`).

### Mathematics
- No numbered display equations in this range. Inline maths in LaTeX: Car2D model (p21), noise schedule (p21), Table 4 header and Table 6 learning rates (p21, p22), Algorithm 3 subscripts (p23), the two reward sums of A.8 (p23), Figure 9 caption (p25).
- Formulas kept as images: none (Algorithm 3 is image plus transcription, as for Algorithms 1-2).

### Headings (navigation)
`#### A.5.2 MBD Hyperparameters`, `#### A.5.3 Baseline Algorithms Implementation`, `#### A.5.4 Demonstration Collections` (p21); `### A.6 MBD for Online Control`, `### A.7 Sample Number Abalation` (p22); `### A.8 Objective Function Abalation` (p23); `## NeurIPS Paper Checklist` (p24). The 15 numbered checklist titles are text (`N. **Title**`), not headings; four of them had been typed as `#` headings by the extractor (items 4, 6, 7, 11).

### Checklist answers as printed
1 Claims [Yes]; 2 Limitations [Yes]; 3 Theory Assumptions and Proofs [Yes]; 4 Experimental Result Reproducibility [Yes]; 5 Open access to data and code [Yes]; 6 Experimental Setting/Details [Yes]; 7 Experiment Statistical Significance [Yes]; 8 Experiments Compute Resources [Yes]; 9 Code Of Ethics [Yes]; 10 Broader Impacts [NA]; 11 Safeguards [NA]; 12 Licenses for existing assets [Yes]; 13 New Assets [NA]; 14 Crowdsourcing and Research with Human Subjects [NA]; 15 IRB Approvals [NA]. Every item has its Question, Answer, Justification, `Guidelines:` and all guideline bullets.

### Joins
- Set: page 21 first item `p0021-b000` (`space`; end of list item 4 "Halfcheetah" from page 20), page 25 first item `p0025-b002` (`space`; end of a guideline bullet from page 24).
- Range boundary 20/21: the join needs the last non-omitted item of page 20 to stay the text item `4. **Halfcheetah**: ... agent and control`. Checked at the end of my run: page 20 (owned by the 11-20 reviewer) carries `[v2]` and still ends with that text item, so the join is valid. If an item is later appended after that list item, the join on `p0021-b000` breaks.
- No other page of the range starts in mid-sentence (22, 23, 24 start with floats after complete paragraphs; 26-30 start with a new bullet or a new paragraph). Page 30 is the last page.
- No `join_previous` follows a `$$` block (there are no display equations in the range).

### Float order
- Page 25: Figure 9 moved behind the bullet continuation it interrupted.
- Pages 22, 23, 24: printed order kept (top floats after complete paragraphs).

### TeX (arXiv v1) versus PDF (camera-ready)
- Page 21 and Tables 5-6 of page 22 are in `90appendix.tex` and agree with the PDF (in the arXiv source Tables 5-6 sit inside A.5.3 before the "zeroth order" sentence; in the PDF they float to the top of page 22).
- Only in the PDF: A.6 with Table 7 and Algorithm 3, Figure 7, A.7, Figure 8, A.8, Figure 9, the whole NeurIPS Paper Checklist. All transcribed from the page.

### Text repairs of substance
- p21: Car2D dynamics fraction `\frac{v}{L}` (extraction had `<sup>` debris); `0 _._ 2` -> `0.2`.
- p22: `9 _._ 6%` -> `9.6%`; Table 6 `<sup>−4</sup>` cells. p23: Algorithm 3 rebuilt; `9.6%`, `74.2%`, `65.3%`, `44.5%`, `805.5%`. p25: `44.5%`, `805.5%`.
- p26: `crossreferenced` -> `cross-referenced`; nested (a)-(d) list. p27/p28/p29: URLs rejoined, backticks removed.
- Authors' errors kept as printed: "continous", "MBD is very little hyperparameters", "schedulling", "we the same hyperparameters" (p21); "running frequence", "Abalation" in the A.7 and A.8 headings (p22, p23); "leads RL by larger 74.2%" (p23); "the number of samples’s effect" (p24); "For both objective function" (p25); "Section 1 list" (p24); "results comes with" (p27); "on Appendix A.5" (p29); template typo "In general. releasing" (p26).
- Printed inconsistencies worth knowing: `HalfCheetah` in Table 7 and the figures versus `Halfcheetah` in Tables 4-6; Car2D uses $\delta$ as state, action and last component of the dynamics; the sums in A.8 have upper limits $H_{\text{RL}}$, $H_{\text{MBD}}$ while the text gives a bare $H$; Table 4 has no Car2D row; Tables 5-6 have a `Pusher` row that is not one of the eight tasks.

### Remaining diagnostics (all category (a))
| Page | Status | Missing lines | Number differences | Adjudication note |
| --- | --- | --- | --- | --- |
| 21 | ATTENTION | 6 (Car2D maths, `Temperature λ`, noise schedule) | minus glyph in `10^{-4}`, `10^{-2}` (both parsers) | yes (3 keys) |
| 22 | ATTENTION | 8 (Table 6 learning-rate cells) | minus glyph in `10^{-4}` x8 (both parsers) | yes (3 keys) |
| 23 | ATTENTION | 4 (A.8 sums) | extras only: Algorithm 3 transcription (both parsers) | yes (3 keys) |
| 24 | OK | 0 | none | none |
| 25 | ATTENTION | 2 (Figure 9 caption maths) | none | yes (1 key) |
| 26 | OK | 0 | none | none |
| 27 | OK | 0 | none | none |
| 28 | OK | 0 | none | none |
| 29 | OK | 0 | none | none |
| 30 | OK | 0 | none | none |

### Proposals for shared files (coordinator)
1. `plan.json` `reading_order` (optional but useful): with per-page order the appendix floats land in the wrong sections, and Figure 9 lands inside the checklist. Suggested moves, all between complete paragraphs and compatible with the two joins:
   - `p0023-b000`, `p0023-b001` (Algorithm 3 image + transcription) and `p0023-b008`, `p0023-b009` (Figure 7 + caption): directly after `p0022-b008` (Table 7 caption), i.e. before the A.7 heading `p0022-b009`.
   - `p0024-b000`, `p0024-b001` (Figure 8 + caption): directly after `p0022-b010` (A.7 paragraph), before the A.8 heading `p0023-b010`.
   - `p0025-b000`, `p0025-b001` (Figure 9 + caption): directly after `p0023-b012` (last A.8 paragraph), before the checklist heading `p0024-b002`. Then `p0025-b002` directly follows `p0024-b017`, which is what its join expects.
   - Optionally `p0022-b000`...`p0022-b003` (Tables 5-6 + captions): after `p0021-b011` (first A.5.3 paragraph).
2. `plan.json` `notes`: "Appendix A.6-A.8, Algorithm 3, Table 7, Figures 7-9 and the NeurIPS Paper Checklist exist only in the NeurIPS camera-ready PDF, not in the arXiv v1 TeX source; they were transcribed from the PDF." and "Headings A.7 and A.8 are printed 'Abalation'."
3. No asset-name clashes. No changes needed in `adjudications.json` beyond binding the four notes (pages 21, 22, 23, 25).

### Limitations
- Bar heights of Figures 7-9 are available only as images; no numbers were read off the plots.
- Table cells with maths (`Temperature $\lambda$`, `$3 \times 10^{-4}$`) are LaTeX strings in the CSV.
- Checklist URLs are written as plain text (printed in typewriter type).
- The answer colours of the checklist (blue [Yes], grey [NA]) are not represented.

### Notes on the brief
- Items are stripped before they are joined, so a nested list (checklist item 4, sub-points (a)-(d)) only keeps its indentation if parent bullet and sub-points are one item; the brief does not say this.
- The brief does not say whether maths inside table cells should be LaTeX; LaTeX cells cost one "missing line" per cell in `check` (8 on page 22).
- With per-page ownership a float cannot be moved back into its own section across a page boundary; only `reading_order` can do that (Figure 9).
- One `crop` call was killed (exit 137) at the time of the machine restart; repeating it afterwards worked. Nothing was lost because every finished page was already on disk.
