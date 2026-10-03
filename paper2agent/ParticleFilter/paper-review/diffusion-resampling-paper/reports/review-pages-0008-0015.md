# Review report: Diffusion differentiable resampling, pages 8-15

Reviewer range: PDF pages 8-15 of `s001-diffusion-resampling` (main text end, references, appendix A-C start).
TeX source used: `tex-source/diffusion-resampling/main.tex` (+ `zmacro.tex` macros expanded: `\diff`->`\mathrm{d}`, `\cond`->`\mid`, `\R`->`\mathbb{R}`, `\expec`->`\mathbb{E}[...]`, `\norm`->`\lVert ... \rVert`, `\kl`->`\mathrm{KL}(\cdot \, \Vert \, \cdot)`, `\refmeasure`->`\pi_{\mathrm{ref}}`, etc.).

## Per-page log

### Page 8 — reviewed [v2]
- Starts mid-sentence: `p0008-b007` has `join_previous: "space"` (continues page 7's last item `p0007-b014`, "...quasi-Newton optimiser").
- Floats: `figure-2` [53,62,541,152] (six panels + colourbars), `figure-3` [52,199,291,362], `figure-4` [315,199,534,367], each with verbatim caption; placed after the first complete paragraph.
- Headings: `### 4.3. Prey-predator model`, `### 4.4. Vision-based pendulum dynamics tracking`.
- Equations (15), (16): LaTeX from TeX (formula items converted to text).
- Repairs: "preypredator" -> "prey-predator" (Figure 4 caption), "Ścibior" accent restored. Author spelling "Lokta–Voltera" kept.
- Ends mid-sentence ("...observations $Y_{0:J}$"); page 9's first item needs `join_previous: "space"` (in my range).
- Remaining diagnostics: maths/minus glyphs only (category a); adjudication note written.

### Page 9 — reviewed [v2]
- `p0009-b003` joins page 8 (`space`); `p0009-b016` joins the column-split Related-work paragraph (`space`).
- Floats: `figure-5` [62,62,283,213]; `figure-6` [316,64,533,179] (eight extractor tiles merged into one, 7 duplicate items deleted). Captions verbatim.
- Headings: `## 5. Related work`, `## 6. Conclusion`; run-in "**Limitations and future work**." kept bold in text.
- Page ends with a complete paragraph.
- Remaining diagnostics: maths only (category a); adjudication note written.

### Pages 10-13 — reviewed [v2] (check: OK on all four)
- Page 10: headings `## Acknowledgements`, `## Impact statement`, `## References`; acknowledgements/funding and authors' contributions kept.
- References: 18 + 25 + 24 + 18 = 85 entries, one `text` item each, printed author-year style (extractor "- " bullets removed, `_x_` -> `*x*`).
- Page 12: Luo, Xie & Huo (2023a) split across columns -> `join_previous: "space"` on `p0012-b013`.
- Page 13: extractor had put the right column between the two halves of the left column; reordered.
- Repairs of substance: wrapped page ranges/volume(number) spacing joined; real hyphens restored ("infinite-dimensional", "forward-backward", "DPM-solver++"); "Ścibior"; Klaas et al. "$n^2$ Monte Carlo" (refs.bib has `$N^2$`, PDF prints lowercase `n` — PDF followed); "http://github.com/google/flax".

### Page 14 — reviewed [v2]
- Headings `## A. Diffusion resampling with Gaussian reference`, `## B. Proof of Proposition 1`.
- `algorithm-3` [44,119,549,411] image + `p0014-alg3text` transcription (15 numbered lines, comments, `Equation (4)`). Authors use `n` in Inputs/Outputs and `N` in the body; kept as printed.
- Equations (17), (18) + two unnumbered displays in LaTeX; formula boxes that swallowed prose were split (new ids `p0014-eq18`, `p0014-therefore`, `p0014-ebound`); missing page-number omit added (`p0014-pagenum`).
- Page ends with an unnumbered display equation whose sentence continues on page 15 ("where recall that ..."); no join set across the display (same as within pages).
- Remaining diagnostics: maths and transcription numbers (category a); adjudication note written.

### Page 15 — reviewed [v2]
- Starts with "where recall that ..." (sentence continuing after page 14's unnumbered display; no join across display).
- Heading `## C. Proof of Corollary 1`. Equations (19)-(25) + one unnumbered display in LaTeX; truncated extractor paragraphs (b013, b019, b020) restored in full from TeX/PDF.
- Ends mid-sentence ("... score approximation remains an open"): **page 16's first item needs `join_previous: "space"`** (next reviewer).
- Remaining diagnostics: maths only (minus glyphs, `7→` = \mapsto glyph) (category a); adjudication note written.

## Summary

| Page | State | check | Assets | Equations |
| --- | --- | --- | --- | --- |
| 8 | reviewed [v2] | ATTENTION (maths only, adjudicated) | figure-2, figure-3, figure-4 | (15), (16) |
| 9 | reviewed [v2] | ATTENTION (maths only, adjudicated) | figure-5, figure-6 | — |
| 10 | reviewed [v2] | OK | — | — |
| 11 | reviewed [v2] | OK | — | — |
| 12 | reviewed [v2] | OK | — | — |
| 13 | reviewed [v2] | OK | — | — |
| 14 | reviewed [v2] | ATTENTION (maths + algorithm transcription, adjudicated) | algorithm-3 (+ text transcription) | (17), (18), 2 unnumbered |
| 15 | reviewed [v2] | ATTENTION (maths only, adjudicated) | — | (19)-(25), 1 unnumbered |

Adjudication notes: `adjudication-notes/page-0008.json`, `-0009`, `-0014`, `-0015` (pages 10-13 are OK, no note).

### Joins
- Set: `p0008-b007` (from page 7, `space`), `p0009-b003` (from page 8), `p0009-b016` (column split), `p0012-b013` (reference split across columns).
- Needed at my boundaries: page 7's last item must be prose ending "...quasi-Newton optimiser" (it is: `p0007-b014`). **Page 16's first item needs `join_previous: "space"`** (page 15 ends "...score approximation remains an open").
- Not joined: page 14 -> 15 boundary falls after an unnumbered display equation; page 15 starts "where recall that ...". Treated like display equations inside pages (no join). Coordinator may decide otherwise.

### Formulas kept as images
None. All displayed equations on pages 8, 14, 15 are LaTeX taken from main.tex and checked against the page.

### TeX versus PDF
- Klaas et al. (2005) reference: refs.bib `$N^2$`, PDF prints `$n^2$` (bst lowercasing); PDF followed.
- No disagreements in the maths on my pages.
- Authors' quirks kept as printed: "Lokta–Voltera" (p. 8); Algorithm 3 Inputs/Outputs index `n` while body uses `N`; "Feynman-Kac" with hyphen in Del Moral title; "arxiv:2601.00781" lowercase; $\mathsf{W}_1$ in prose vs $\mathsf{W}_2^2$ bounds around (22)-(23).

### Proposals for shared files
- None needed for plan.json. Asset names used: figure-2..figure-6, algorithm-3 (printed numbering; no page suffix needed unless another reviewer uses the same names for appendix floats — appendix figures should continue at Figure 7+).
- Heading levels: `### 4.3`, `### 4.4` assume page 7 uses `## 4. Experiments`.

### Notes on the brief
- The brief does not say whether to keep the extractor's "- " list bullets in author-year bibliographies; I removed them (printed list has no bullets). Coordinator may want to align with other reviewers.
- The join rule ("item before must be text") does not say what to do when a page ends with a display equation whose sentence continues; I did not join across it.
