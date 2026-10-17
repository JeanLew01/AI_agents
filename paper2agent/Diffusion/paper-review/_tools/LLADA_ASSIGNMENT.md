# llada-paper: paper-specific conventions (all reviewers)

Paper: Nie et al., "Large Language Diffusion Models" (LLaDA), arXiv:2502.09992v3 (18 Oct 2025), NeurIPS 2025,
33 pages, **single column** (NeurIPS style): main text pp. 1-10, references pp. 10-18, Algorithms 1-5 and
Appendix A pp. 19-22, Appendix B pp. 22-29, Appendix C p. 29, Tables 14-19 pp. 30-33.

- `DOC` = `/home/jixia/AI_agents/paper2agent/Diffusion/paper-review/llada-paper/documents/s001-llada`
- `TEX` = `/home/jixia/AI_agents/paper2agent/Diffusion/tex-source/llada` (`main.tex`; macros in `math_commands.tex`,
  bibliography in `main.bbl`). Remember: the PDF wins over TeX.
- Tools: `T=/home/jixia/AI_agents/paper2agent/Diffusion/paper-review/_tools/p2s_tools.py`

## Conventions for this paper
1. Single column: reading order is top to bottom; there is no column reordering. Floats (figures/tables placed by
   LaTeX at the top of a page) still must not interrupt a sentence: put them between complete paragraphs on the
   page (the coordinator may move floats across pages later via `reading_order`; propose such moves in your report).
2. Headings: `# Large Language Diffusion Models` only for the title. `## 1 Introduction`, `### 2.1 Probabilistic
   Formulation`, `## A Formulation of Masked Diffusion Models`, `### A.1 Training`, `## References`,
   `## Acknowledgements`, `## C Impact Statement`. Keep the printed numbering and capitalisation. The abstract
   heading is `## Abstract`. Bold run-in paragraph titles (e.g. **Limitations.**, **Flexible Sampling Strategies.**,
   **Experimental Setup.**, **Results.**, **General ability:**) stay inside the text item in bold.
3. Equations are numbered (1)-(16) and printed with `\tag{n}`. Underbrace labels in (1)-(2) ("Generative modeling
   principles", "Autoregressive formulation") must be kept, e.g. `\underbrace{...}_{\text{Generative modeling principles}}`.
   Write the indicator as printed (`\mathbf{1}[x_t^i = \mathrm{M}]`), the mask token as `\mathrm{M}`,
   `p_{\theta}`, `p_{\text{data}}`, `q_{t|0}`, `x_t^{\text{UM}}` etc., following the TeX macros expanded to standard LaTeX.
4. Algorithms 1-5 (pp. 19-21): image crop (`kind: "figure"`, `"label": "Algorithm 1"`, `"asset_name": "algorithm-1"`)
   **plus** one `text` item right after it with a line-by-line transcription, in the collection's established form
   (one paragraph per printed line, separated by blank lines; nesting shown with `&emsp;&emsp;` per level):
   ```
   **Algorithm 1** Pre-training of LLaDA

   **Require:** mask predictor $p_\theta$, data distribution $p_{\text{data}}$

   **1:**&ensp;**repeat**

   **2:**&ensp;&emsp;&emsp; $x_0 \sim p_{\text{data}}$ &emsp; `# with a probability of 1%, the sequence length of x0 follows U[1, 4096]`
   ```
   Keep the `#` comments (as inline code when they contain no maths, otherwise as plain text after `#` with LaTeX).
   Preserve the printed pseudocode exactly, including printed oddities (e.g. the comment truncated to
   "the SFT dat" in Algorithm 2, `t ∗ L`, `Lowest − n_un`). Do not repair the algorithms.
5. Figures: Figure 1 (p. 2, two radar charts), Figure 2 (p. 3, panels (a)(b)(c) with legend), Figure 3 (p. 6, six
   scatter panels), Figure 4 (p. 24, three panels (a)(b)(c); one figure item with all panels and their sub-labels),
   Figure 5 (p. 26, four panels). One figure item each, `figure-1` ... `figure-5`; caption as a separate item
   beginning `Figure 1: ...`. Delete stray tick/legend/axis text items only after confirming they are inside the crop.
6. Data tables (Tables 1, 2, 4-12, 18, 19): `kind: "table"` with every cell as a string, exactly as printed,
   shot counts kept in the cell as printed (`65.9 (5)`), `-` kept as `-`, footnote symbols kept
   (`LLaDA 8B∗`, `Qwen2 7B†`, `Deepseek 7B¶`). Multi-row headers (Tables 1-2: Model / Training tokens /
   Post-training / Alignment pairs rows; group rows "General Tasks", "Mathematics & Science", "Code", "Chinese")
   : keep the header-type rows as ordinary rows and the group rows as rows whose first cell is the group name and
   other cells empty; say so in the page notes. Table 7: the "Block Difusion" / "Block Diffusion LLaDA" group label
   spans the L' rows: use a first column "Strategy" with the group label repeated on every row and a second column
   "L'" (e.g. `L' = 2`); keep the printed spelling "Block Difusion" (typo) where printed. Bold best values are not
   carried into the CSV (note it once).
7. Visualisation tables with token images (Table 3 on p. 8, Table 13 on p. 29, Table 14 on p. 30): keep the
   **whole table** as an image crop (`kind: "figure"`, `"label": "Table 3"`, `"asset_name": "table-3"`, etc.;
   caption as a separate `caption` item `Table 3: ...` placed **before** the image, as printed above it), then add a
   `text` item starting `Transcription of Table 3 (verify against the image above):` with the User / LLaDA turns
   verbatim, and for the token-image rows the token sequence as read from the image (tokens separated by spaces,
   e.g. `In 4 hours , Lily runs 12 * 4 = 48 kilometers . ...`), stating that the colour shading (prediction order)
   is only in the image. Chinese and German text verbatim (UTF-8).
8. Dialogue tables (Tables 15, 16, 17, text only): `kind: "table"` with three columns
   `["Case", "Speaker", "Text"]` (header row added by the converter: say so in the notes), one row per printed
   turn, the italic case label (`Daily life`, `Translation`, `Math`, `Code`, `Question1`, ...) repeated on every row
   of its case, Speaker = `User` / `LLaDA` / `GPT-4o` as printed, Text verbatim with its internal line breaks
   replaced by single spaces except in the Python code of Table 15 (use `\n` inside that cell's string, i.e. keep
   the printed line breaks). Keep `**` asterisks that are printed literally in Table 15 (`**The Shawshank
   Redemption**`) as literal characters.
9. Boxed examples on p. 28 (iGSM question/solution and prompt): `text` items, each starting with the printed bold
   label (`**(Question)**`, `**(Solution)**`, `**(Prompt)**`), verbatim including the printed oddities
   (`so n = 3 * w = 3 * 2 = 1 #### 1`, `¨the number`, `High.Ässume`). Do not "fix" them; note them.
10. Chinese text (poem examples B.9, Tables 3, 17): verbatim UTF-8 characters; check each character against a
    220-dpi crop; if a glyph is unreadable keep the table image and say so.
11. References (pp. 10-18): one entry per line `[n] Authors. Title. Venue, year.` exactly as printed (keep the
    printed `Ashish Vaswani. Attention is all you need.`, `Tom B Brown.` etc.); 125 entries in order.
12. Footnotes: p. 1 (∗ Equal contribution, † Work done during an internship at Ant Group, ‡ Project leaders,
    § Correspondence to Chongxuan Li) follow the author block as one `text` item; footnote 5 (p. 2) and footnote 6
    (p. 3): `Footnote 5: ...` with the marker `[^5]` in the running text. The NeurIPS venue line on p. 1
    ("39th Conference on Neural Information Processing Systems (NeurIPS 2025).") is kept as text, not omitted.
13. Page furniture to omit: page numbers, the rotated arXiv stamp on p. 1.
14. Asset names in use (avoid clashes): figure-1..figure-5, algorithm-1..algorithm-5, table-1..table-19.
