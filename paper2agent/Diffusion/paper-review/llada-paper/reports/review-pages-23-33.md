# Review report: llada-paper, PDF pages 23-33 (reviewer r3)

Scope: Appendix B.2-B.10 and C, Tables 5-19, Figures 4-5, iGSM boxes, poem examples.
Boundary: page 22 (other reviewer) ends with a complete paragraph (B.1, "... aligns with the above |EOS| padding strategy."); page 23 starts with floats (Tables 5, 6), so no join is needed at the start of my range.

## Per-page log

### Page 23 - done ([v2])
- Table 5 -> `table-5` (9x6), Table 6 -> `table-6` (3x7); captions (printed above) kept before the tables. Bold removed from Table 6 cells.
- Headings `### B.2 Details about Model Training`, `### B.3 Ablation on Classifier-free Guidance` (were `# **...**`).
- LaTeX: $4 \times 10^{-4}$, $4.2 \times 10^{-4}$ (split decimal repaired), $6ND$, $N$, $D$, $\{0.5, 1, 1.5, 2\}$.
- Remaining check: 2 missing lines + `−4` vs `-4` (category a). Adjudication note written.

### Page 24 - done ([v2])
- Figure 4 -> `figure-4` (three picture items merged; box [105,67,509,155] with all panels and sub-captions). Sub-caption line kept verbatim as a text item between figure and caption; caption starts `Figure 4:`.
- Table 7 -> `table-7` (columns `Strategy`, `L'` added per convention; "Block Difusion" typo kept). Table 8 -> `table-8` ("Block Difusion LLaDA" typo kept; "Block Diffusion" row correct as printed).
- Heading `### B.4 Details and Ablation on Sampling Strategies`.
- Last paragraph continues on p. 25 (join set on p. 25).
- Remaining check: 1 missing line ($\times$, category a); second-parser glued table cells (category a).

### Page 25 - done ([v2]), check OK
- Continuing paragraph "per sampling step. ..." moved before the top floats, `join_previous: space` (continues p. 24).
- Table 9 -> `table-9` (printed header "Length" kept although rows are strategies), Table 10 -> `table-10`.
- |EOS| written as plain `|EOS|` (TeX has `$|\text{EOS}|$`; plain text matches the native line check). Proposal: use the same form on page 22 (B.1) for consistency.
- Heading `### B.5 Ablation on Generated Length`. Only second-parser glued-cell differences remain (category a).

### Page 26 - done ([v2]), check OK
- Figure 5 -> `figure-5` (single picture item already covered all four panels; picture-text dump removed). Legend spells "LlaMA3" inside the figure (as printed).
- Heading `### B.6 Standard Benchmarks and Evaluation Details`. Figure 5 is printed in B.5/B.6 but discussed in B.7 (p. 27); left in printed position (between complete paragraphs). Optional `reading_order` move: after the first B.7 paragraph that cites Fig. 5 on p. 27.

### Page 27 - done ([v2])
- Table 11 -> `table-11` (merged "Input Length" cells 512/1024 repeated on each spanned row; extra 512x2, 1024x2 in the number check, category a).
- Repairs: `lm-evaluationharness` -> `lm-evaluation-harness` (real hyphen at line wrap); `|EOS|`.
- Heading `### B.7 Analysis of Sampling Efficiency`.

### Page 28 - done ([v2]), check OK
- Table 12 -> `table-12`. Heading `### B.8 Evaluation on iGSM Dataset`.
- Boxed examples as text items `**(Question)**`, `**(Solution)**` (four printed lines kept as single newlines), `**(Prompt)**`; oddities kept: `3 * 2 = 1 #### 1`, `¨the number`, `High.Ässume` (TeX `\"the` / `\" Assume` accent artefacts), `’#### x.’`.
- Literal dollar in `"#### $answer"` escaped as `\$answer` (markdown maths safety).

### Page 29 - done ([v2])
- Table 13 -> image `table-13` (kind figure, box [106,114,507,222]); caption before it; transcription item `p0029-b001t` (User turn + 62-token LLaDA sequence).
- B.9 poem examples split into two text items with the printed line breaks; every Chinese character checked at 260 dpi (match TeX).
- Headings `### B.9 Poem Completion Tasks`, `### B.10 More Case Studies`, `## C Impact Statement`.
- Remaining check: extra `13` from the transcription heading (category a).
- Table 13 is printed at the top of p. 29 before B.9 although it belongs to B.10; left in printed position (optional `reading_order` move to after the B.10 paragraph).

### Page 30 - done ([v2])
- Table 14 -> image `table-14` (box enlarged from [111,324,503,453], which cut the second turn, to [106,322,506,513]); caption before it; transcription `p0030-b001t` with both User turns and both LLaDA token sequences.
- Remaining check: extra `14` from the transcription heading (category a).

### Page 31 - done ([v2]), check OK
- Table 15 -> `table-15` rebuilt as Case/Speaker/Text (13 x 3, header converter-added), one row per turn; Code LLaDA cell keeps `\n` line breaks; literal `**...**` kept; quirks kept (`immaginiert`, `‘sorted()‘`, `4 x 5`).

### Page 32 - done ([v2])
- Table 16 -> `table-16` (17 x 3, Case/Speaker/Text).
- Table 17: caption had been extracted as a `#` heading -> now a caption item. `table-17` (7 x 3; speakers User/GPT-4o/LLaDA). Chinese checked at 260 dpi; wraps inside Chinese joined without spaces (deviation from "single space" wording of convention 8, since Chinese has no inter-word spaces); GPT-4o's own errors kept (`山居秋膜`, `无亲`, unclosed `（武陵春，春晚`).
- Remaining check: extra 1/2 from repeated Question1/Question2 labels (category a).

### Page 33 - done ([v2]), check OK
- Table 18 -> `table-18` (21 x 9), Table 19 -> `table-19` (22 x 9). All 43 rows x 9 cells compared programmatically with the native PDF cells (0 differences) and with TeX (0 differences); Table 18 also by eye. `-` missing values kept; caption typo "baelines" kept.

## Summary

**Pages covered:** 23-33, all saved with `reviewed: true` and `[v2]` notes. Check status: OK on 25, 26, 28, 31, 33; ATTENTION on 23, 24, 27, 29, 30, 32, all category (a), each with an adjudication note in `DOC/adjudication-notes/page-00NN.json`.

**Assets (17):**
| Page | Item | Asset | Form |
|---|---|---|---|
| 23 | Table 5, Table 6 | `table-5`, `table-6` | CSV |
| 24 | Figure 4 | `figure-4` | image (3 extractor pictures merged) |
| 24 | Table 7, Table 8 | `table-7`, `table-8` | CSV |
| 25 | Table 9, Table 10 | `table-9`, `table-10` | CSV |
| 26 | Figure 5 | `figure-5` | image |
| 27 | Table 11 | `table-11` | CSV |
| 28 | Table 12 | `table-12` | CSV |
| 29 | Table 13 | `table-13` | image (kind figure) + transcription text |
| 30 | Table 14 | `table-14` | image (kind figure) + transcription text |
| 31 | Table 15 | `table-15` | CSV (Case/Speaker/Text) |
| 32 | Table 16, Table 17 | `table-16`, `table-17` | CSV (Case/Speaker/Text) |
| 33 | Table 18, Table 19 | `table-18`, `table-19` | CSV |

Every box was checked with a crop and with an automatic 4-pt margin test (no dark pixels outside any box except neighbouring caption text). Equations: none displayed in this range; inline maths only on pp. 23-24 ($4 \times 10^{-4}$, $4.2 \times 10^{-4}$, $6ND$, $N$, $D$, $\{0.5, 1, 1.5, 2\}$, $\times$, $L'$). **Formulas kept as images:** none.

**Joins:** p. 25 `p0025-b004` `join_previous: space` (continues the p. 24 "Experimental Setup" paragraph; the continuing text was moved in front of the p. 25 top floats). Range start: p. 22 ends with a complete paragraph, p. 23 starts with floats -> no join needed. Range end: p. 29 ends the Impact Statement; pp. 30-33 are float pages.

**Headings set:** `### B.2` ... `### B.10` (B.2 Details about Model Training, B.3 Ablation on Classifier-free Guidance, B.4 Details and Ablation on Sampling Strategies, B.5 Ablation on Generated Length, B.6 Standard Benchmarks and Evaluation Details, B.7 Analysis of Sampling Efficiency, B.8 Evaluation on iGSM Dataset, B.9 Poem Completion Tasks, B.10 More Case Studies), `## C Impact Statement`. The extractor's `# Table 17: ...` heading (p. 32) was turned into a caption.

**TeX versus PDF:** no disagreement found. The iGSM prompt's `¨the` / `High.Ässume` come from the TeX `\"the` / `\" Assume` (accent commands instead of quotes) and are printed that way; kept per convention 9.

**Text repairs of substance:** `lm-evaluationharness` -> `lm-evaluation-harness` (p. 27); `4 _._ 2` -> `$4.2 \times 10^{-4}$` (p. 23); `_|_ EOS _|_` -> `|EOS|` (pp. 25, 27); Table 14 box enlarged (the extractor's box cut off the second dialogue turn); Tables 15-17 rebuilt from glued two-column extractions; poem examples (p. 29) split into two items and freed from backtick code spans; `"#### $answer"` -> `"#### \$answer"` (escaped dollar, p. 28).

**Printed oddities kept (not fixed):** "Block Difusion" (Tables 7, 8), Table 9 header "Length", "just one tokens are transferred" (p. 26), "Tab. 11 compares of memory consumption" (p. 27), "are inherently depend on ARMs" (p. 28), "applies the origin reverse process" (p. 24), "We employ random remasking strategy" (Table 14 caption), "baelines" (Table 19 caption), "LlaMA3" (Figure 5 legend, inside the image), `immaginiert`, `‘sorted()‘`, literal `**...**` (Table 15), `山居秋膜`, `无亲`, unclosed `（武陵春，春晚` (GPT-4o outputs, Table 17).

**Remaining diagnostics (all category a):**
- p. 23: 2 missing lines + `−4`/`-4` (LaTeX exponents); second parser glues Table 6 cells.
- p. 24: 1 missing line (`\times` in Figure 4 caption); second parser glues Table 7/8 cells.
- p. 25: second parser glues Table 9/10 cells only (main check OK).
- p. 27: extra 512 x2, 1024 x2 (merged Input Length cells of Table 11 repeated per row).
- p. 29 / p. 30: extra 13 / 14 (number in the converter-added "Transcription of Table N" line).
- p. 32: extra 1 x2, 2 x2 (Question1/Question2 case labels repeated per row of Table 17).

**Proposals for shared files / other reviewers:**
1. Page 22 (other reviewer, re-read at the end, read-only): it now has `## B Experiments` / `### B.1 Data Collection and Preprocessing` and plain `|EOS|`, consistent with my `### B.2`-`### B.10` and my `|EOS|` form; its last paragraph is complete, so the boundary needs no join.
2. Sub-captions: for Figure 4 I kept the printed sub-caption line `(a) Autoregressive. (b) Block Diffusion. (c) Block Diffusion LLaDA.` as a separate text item between the figure and the `Figure 4:` caption (the convention asks for captions that start with `Figure N:`; the sibling collections instead put the sub-captions as the first line of the caption item). The Markdown output is the same. The coordinator may want Figure 2 (p. 3) handled the same way.
3. Optional `reading_order` moves (not required, all floats already sit between complete paragraphs): Figure 5 (p. 26) to after the first B.7 paragraph citing Fig. 5 on p. 27; Table 12 (p. 28 top) to after the B.8 paragraph that cites it; Table 13 (p. 29 top) to after the B.10 paragraph; Table 10 (p. 25 top) to after the B.5 text on p. 26.
4. Asset names `table-13` and `table-14` are `figure`-kind items (convention 7), so they land in the figure asset folder under a `table-` name; no clash with other names.

**Limitations:** Tables 13 and 14 are images; their token transcriptions were read from 220-230-dpi crops and the prediction-order shading is only in the image. Bold best-value marking in Tables 6-12 is not carried into the CSVs. The case boundaries between consecutive cases with the same label (two "Daily life" and two "Translation" cases in Table 15, two "Daily life" in Table 16) are visible only from the speaker sequence (each new case starts with a User turn).

**Brief notes:** (a) convention 8 says "line breaks replaced by single spaces", which would insert spaces inside Chinese text in Table 17; I joined Chinese wraps without spaces. (b) Convention 9's `**(Question)**` differs slightly from the print `(**Question**)`; I followed the convention. (c) Captions of tables in this paper are printed above the tables; the brief says "caption right after the figure" for figures, so for tables I kept the printed order (caption before table), consistent with convention 7 for Tables 13-14.
