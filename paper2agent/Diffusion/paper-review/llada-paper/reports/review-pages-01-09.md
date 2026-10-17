# LLaDA review, pages 1-9 (reviewer r1)

DOC = `llada-paper/documents/s001-llada`, TEX = `tex-source/llada/main.tex`. Scratch: `_scratch/r1` (edit scripts `p01.py` ... and helper `pg.py`).

## Per-page log

### Page 1 — done ([v2])
- Items: stamp omitted; title; author line (affiliations $^{1,2,3}$, footnote markers [^∗][^†][^‡][^§]); affiliations + e-mail (one item); author footnotes (one item `Footnote ∗: ...`) directly after the author block; NeurIPS 2025 venue line kept as text after the footnotes; `## Abstract`; abstract; `## 1 Introduction`; intro paragraph; equations (1), (2) as `$$...\tag{n}$$` with the underbrace labels.
- Text repairs: `finetuning` -> `fine-tuning`, `multiturn` -> `multi-turn` (line-wrap at a real compound hyphen).
- Join at end: page ends with equation (2); p. 2 starts with "where x is a sequence ..." — no `join_previous` (previous item is display maths).
- Remaining diagnostics: 6 missing maths lines, U+2212 minus (category a). Adjudication note written.

### Page 2 — done ([v2])
- Items: continuation paragraph "where $x$ ..." (first, no join: previous item is equation (2)); Figure 1 (`figure-1`, bbox [103,67,509,241], both radar charts + legends + group arcs); caption `Figure 1: ...`; four intro paragraphs; Footnote 5 (marker `[^5]`); "We adopt ... contributions:"; bullet 1 (`$10^{23}$ FLOPs`); page number omitted.
- Footnote 5 placed before the "We adopt ..." paragraph so that this paragraph and its bullet list (continuing on p. 3) are not split by the footnote.
- Remaining diagnostics: `1023` vs `10`,`23` (superscript, category a). Adjudication note written.

### Page 3 — done ([v2])
- Items: bullets 2-4 (continuing list, first on page); Figure 2 (`figure-2`, bbox [105,67,497,182], bottom moved up to exclude the caption's first line); caption `Figure 2: ...`; `## 2 Approach`; paragraph with `[^6]`; `### 2.1 Probabilistic Formulation`; two paragraphs; equation (3); "where ..."; paragraph; equation (4); Footnote 6 (before the last paragraph); last paragraph "Notably, ... as shown in" (continues on p. 4: `join_previous: "space"` set on p. 4's first item).
- Remaining diagnostics: 9 missing lines, all maths (category a). Adjudication note written.

### Page 4 — done ([v2])
- Items: continuation "Eq. (4), LLaDA is ..." (`join_previous: "space"` onto p. 3's last paragraph); `### 2.2 Pre-training`; five paragraphs; `### 2.3 Supervised Fine-Tuning`; two paragraphs; equation (5); "where $L'$ ..."; last paragraph "Note that ... serves as the" (continues on p. 5, join set there); page number omitted.
- Text repair of substance: the extractor had pushed "term compared to Eq. (3), and lacks a theoretical link" into a `<sup>` around a broken fraction; rebuilt as "misses the $\frac{1}{t}$ term compared to Eq. (3), and lacks a theoretical link to maximum likelihood".
- Remaining diagnostics: 8 maths lines, U+2212 minus in $10^{-4}$/$10^{-5}$ (category a). Adjudication note written.

### Page 5 — done ([v2])
- Items: continuation "masked version $x_t$ ..." (`join_previous: "space"`); two SFT paragraphs; `### 2.4 Inference`; four paragraphs; paragraph before (6); equation (6); "where $L$ ..."; "We present ... Appendix A."; `## 3 Experiments`; intro paragraph; page number omitted.
- Text repairs of substance: two broken inline fractions $\frac{s}{t}$ whose following words had been pushed into `<sup>`. Author typo "remarked" (for "remasked") kept verbatim (PDF and TeX).
- Remaining diagnostics: 12 maths lines, U+2212 minus (category a). Adjudication note written.

### Page 6 — done ([v2])
- Items: Figure 3 (`figure-3`, bbox [103,66,508,254], six scatter panels with legends and FLOPs axes); caption `Figure 3: ...`; `### 3.1 Scalability of LLaDA on Language Tasks`; four paragraphs ($10^{18} \sim 10^{20}$, $10^{20} \sim 10^{23}$); `### 3.2 Benchmark Results`; paragraph; last paragraph "As shown in Tab. 1, ... We conjecture that the" (continues on p. 7, join set there); page number omitted.
- Remaining diagnostics: 1 maths line and powers-of-ten tokens (category a). Adjudication note written.

### Page 7 — done ([v2])
- Items: continuation "strengths stem from ..." (`join_previous: "space"`); Table 1 caption; Table 1 (`table-1`, 22x8); Table 2 caption; Table 2 (`table-2`, 17x8); two paragraphs (last continues on p. 8); page number omitted.
- Tables rebuilt cell by cell (220-dpi crops, identical to the TeX tabulars): group rows "General Tasks" / "Mathematics & Science" / "Code" / "Chinese" as name + empty cells; header-type rows (Model, Training tokens, Post-training, Alignment pairs) as ordinary rows; footnote symbols ∗ † ¶ in the column names; bold not carried.
- check: OK (212/212).

### Page 8 — done ([v2])
- Items: continuation "with reinforcement learning (RL), ..." (`join_previous: "space"`); Table 3 caption (before the image, as printed); Table 3 image (`table-3`, kind figure, bbox [104,113,509,415]); new text item `p0008-t3-transcription` "Transcription of Table 3 (verify against the image above): ..." (both groups, all turns verbatim, token sequence read at 300 dpi, Chinese checked per character, German verbatim, printed mixed quote marks kept); two paragraphs; `### 3.3 Reversal Reasoning and Analyses`; two paragraphs; page number omitted.
- Text repair: `AllenZhu` -> `Allen-Zhu` (real hyphen in the name at a line wrap).
- Remaining diagnostics: 1 maths line ($|\text{EOS}|$) and extra numbers from the transcription of text inside the image (category a). Adjudication note written.

### Page 9 — done ([v2])
- Items: Table 4 caption (new item `p0009-t4-caption`); Table 4 (`table-4`, 4x3, bbox [314,99,508,161]); paragraph "We did not design ..." ; paragraph "We also analyze ..." (new item `p0009-p2`); two paragraphs; `### 3.4 Case Studies`; paragraph; `## 4 Related Work`; five paragraphs, the last ending "such as protein" (continues on p. 10, whose first item already has `join_previous: "space"`); page number omitted.
- Wraptable untangled (extractor had merged the left-hand paragraph lines into a 4-column table and interleaved the caption with prose). Citation ranges repaired across line wraps (`[41–51]`, `[52–56]`).
- Remaining diagnostics: $10^{23}$ superscript; second parser glues adjacent Table 4 cells (category a). Adjudication note written.

## Summary

- **Pages covered:** 1-9, all `reviewed: true` with `review_notes` starting `[v2]`. Adjudication notes in `adjudication-notes/page-0001.json` ... `page-0006.json`, `page-0008.json`, `page-0009.json` (page 7 checks OK, so it has no note).
- **Final check state:** p7 OK; p1-p6, p8, p9 ATTENTION with category (a) only (LaTeX maths, U+2212 vs `-`, superscript powers of ten, numbers in the Table 3 transcription of text inside the image, second-parser glued Table 4 cells). No category (b) left.

### Assets
| Page | Item | Label | Asset | Notes |
| --- | --- | --- | --- | --- |
| 2 | p0002-b000 | Figure 1 | `figure-1` | two radar charts (Base / Instruct), bbox [103,67,509,241] |
| 3 | p0003-b000 | Figure 2 | `figure-2` | panels (a)(b)(c) + legend, bbox [105,67,497,182] |
| 6 | p0006-b000 | Figure 3 | `figure-3` | six scatter panels, bbox [103,66,508,254] |
| 7 | p0007-b001 | Table 1 | `table-1` | 22x8 CSV |
| 7 | p0007-b003 | Table 2 | `table-2` | 17x8 CSV |
| 8 | p0008-b001 | Table 3 | `table-3` | kind figure (token image), + transcription item `p0008-t3-transcription` |
| 9 | p0009-b001 | Table 4 | `table-4` | 4x3 CSV |

Equations (1)-(6) are all LaTeX `$$...\tag{n}$$` text items (p1: (1),(2); p3: (3),(4); p4: (5); p5: (6)), taken from main.tex and checked against the page. **No formula kept as an image.** Footnotes: p1 author footnotes ∗ † ‡ § (one item after the author block), footnote 5 (p2, marker `[^5]`), footnote 6 (p3, marker `[^6]`).

### Joins
- Set by me: p4 `p0004-b000`, p5 `p0005-b000`, p7 `p0007-b004`, p8 `p0008-b002` (all `space`).
- Not set (deliberately): p2's first item "where $x$ is a sequence ..." follows display equation (2) on p1; joining prose onto a `$$` block would put text on the closing `$$` line. Same choice as for every "where ..." after an equation within a page.
- Range boundary: p9 ends with "... in other domains such as protein"; p10's first item already has `join_previous: "space"` (set by the p10 reviewer) and my last item before it is text. Nothing needed from the coordinator.

### TeX versus PDF
No disagreement of substance on pp. 1-9. The TeX uses non-breaking hyphens (U+2011) in "Zero/Few‑Shot" and in Table 4 ("2024‑08‑06", "Qwen2.5‑7B", "LLaDA‑8B"); the PDF text layer has ASCII `-`, which I kept.

### Text repairs of substance
- p1: `finetuning` -> `fine-tuning`, `multiturn` -> `multi-turn` (compound hyphens at line ends).
- p4: words "term compared to Eq. (3), and lacks a theoretical link" had been pushed into `<sup>` around the broken fraction; rebuilt with $\frac{1}{t}$.
- p5: the same damage around both $\frac{s}{t}$ fractions.
- p8: `AllenZhu` -> `Allen-Zhu`.
- p9: wraptable untangled; `[41– 51]` -> `[41–51]`, `[52– 56]` -> `[52–56]`, `Comple-tion` / `perfor-mance` wraps.
- Kept as printed (author wording): "remarked" for "remasked" (p5), "Nie et al. [27] suggests" (p6), "continuousize" (p9), "pretraining" without hyphen (p6), the mixed quote marks “...\" in Table 3.

### Proposals for shared files
- None needed for `reading_order`: every float sits between complete paragraphs on its own page (Figure 1 after p2's first paragraph; Figure 2 after the bullet list on p3; Tables 1-2 after the one-sentence continuation on p7; Table 3 after the continuation on p8; Table 4 first on p9, directly after the p8 paragraph that cites it).
- Optional plan note: "Bold best values in Tables 1, 2 and 4 are not carried into the CSVs; see the page images."

### Limitations
- Table 3's token sequence is a reading of an image (300 dpi); its colour shading (prediction order) exists only in the image.
- Vertical rules in Tables 1-2 (self-evaluated models vs. quoted ones) are not represented in the CSVs; the ∗/†/¶ markers carry the same information.

### Notes on the brief
- Clear and workable. One gap: the brief does not say whether to join prose that continues after a display equation across a page break; I left such items unjoined (see Joins).
