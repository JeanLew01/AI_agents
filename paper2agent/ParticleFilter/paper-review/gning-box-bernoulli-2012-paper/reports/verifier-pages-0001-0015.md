# Independent verifier report: gning-box-bernoulli-2012-paper, pages 1-15

Package: `staging/gning-box-bernoulli-2012-paper-s1`. Reference: `documents/s001-gning-box-bernoulli-2012/source.pdf` (15 pages, A4, two-column).
Nothing in the package or the review plans was changed. Reviewer reports were not consulted.

## Coverage

- **Pages 1-15, all.** Every page was rendered at 200 dpi and read as four quadrant crops (two per column) next to `references/paper.md`; equations (11), (49), (50) and Algorithm 3 were re-cropped at 300-500 dpi.
- **Mathematics:** all display equations (1)-(51) and the unnumbered displays (the `\beta_k` sample approximation on p. 5, the weight formulas in Algorithms 1-2) were compared symbol by symbol with the crops: bold/non-bold, interval brackets, `k+1|k` subscripts, sum/integral limits, tags. Inline maths was read in every paragraph.
- **Prose:** an automatic word-level diff of `pdftotext` output against the prose of `paper.md` (maths masked) was run over the whole document; all 97 flagged spans were inspected. They are reading-order moves (footnotes, floats, Algorithm 3, references [2]-[10]) or line-wrap hyphens. No word-level difference in body text was found. The moved blocks (footnotes, captions, algorithms, references) were checked by eye.
- **Algorithms 1-3:** transcription compared line by line with the PDF and with the JPEG crops.
- **Figures 1-9 and algorithm-1..3 JPEGs:** all 12 opened; captions compared with the PDF.
- **References:** all 30 entries read against the page images (not sampled).
- **Tables:** the paper has none; `assets/table` is empty, correctly.
- **Mechanical checks:** `$`/`$$` balance, brace and `\left`/`\right` balance, doubled backslashes, `](` inside maths, HTML residue, index headings versus `paper.md` headings.
- `SKILL.md`, `references/index.md`, `references/supplement.md` and the conversion notes were read once.

## Findings

**Errors: 0. Minors: 4.**

| # | Severity | PDF page | Item id | Package says | PDF shows | Suggested fix |
|---|---|---|---|---|---|---|
| 1 | minor | 4 | p0004-b022 (with b020 / b021) | `Footnote 4:` is placed between equation (16) and "Each density $\beta_k(\mathbf{x}\|[\mathbf{z}])$ in the mixture (16) is constructed..." | "Each density..." follows (16) without indentation, i.e. it continues the same paragraph; the footnote is at the column foot | Move the footnote after the paragraph that ends "...where $\mathbf{x}_{b,k}^j = [\ldots]^{\intercal}$" (or after the paragraph containing the `[^4]` marker). No content is lost as it stands. |
| 2 | minor | 4 | p0004-b004 | The chain (11)-(13) is written as four separate `$$` blocks; lines 2-4 each start with a bare `=` | One aligned display: `g_k([z]\|x) = ∫... = φ(...) − φ(...) (11) = ... (12) = ... (13)` | Optional: one `aligned` block cannot carry three tags in most renderers, so the split is defensible; if kept, prefix the continuation lines with `{}` or `\phantom{g_k([\mathbf{z}]\|\mathbf{x})}` so the leading `=` renders with proper spacing. |
| 3 | minor | 3, 4, 6, 7 | footnote items on these pages | Markers are `[^1]`...`[^6]` but the footnote texts are plain paragraphs "Footnote N: ..." (no `[^N]:` definitions), so the markers render literally as `[^N]` | Superscript footnote marks 1-6 | Cosmetic and apparently a collection convention; no action needed unless the renderer is expected to link footnotes. All six footnote texts are present and correct. |
| 4 | minor | conversion notes | - | "accepted author manuscript (second revision, 28 Dec 2011) ... from Lancaster EPrints 52300 ... IEEE TSP 60(5):2138-2151 (2012), doi:10.1109/TSP.2012.2184538" | The PDF itself only prints "Submitted to IEEE Trans. Signal Processing December 28, 2011"; "second revision", the EPrints number and the journal citation are not on the pages (they agree with `papers/SOURCES.tsv`) | None required; noted only because these statements cannot be verified from the PDF. Nothing in the notes was found to be false. |

Rendering problems looked for and **not** found: doubled backslashes, unbalanced `$`/braces, HTML residue (`<sup>`), glyph soup, split decimals, footnotes swallowing paragraphs, a raw `](` inside maths (all occurrences are written `]{}(`, as intended), duplicated paragraphs, sentences broken at column/page changes.

## Checked and found correct (by page)

- **p. 1:** title, authors with marks (third author mark `♯` in the byline, `∗` on the footnote, as printed), three affiliation footnotes, abstract, index terms, submission line, Introduction paragraphs 1-3.
- **p. 2:** rest of Introduction; Section II; equation (1); II-A, equation (2) (four cases, trailing comma as printed), the four bullet definitions with `abbr` over `=`; II-B up to equation (3).
- **p. 3:** equation (4), `\mathcal{IZ}`, `\mathcal{F}(\mathcal{IZ})`; Section III paragraph with footnote marks 2 and 3; equations (5)-(9) (two-fraction form of (6); sum subscripts `[z] ∈ Υ_{k+1}`; `λ c([z])` denominators); footnotes 1-3; reading order left column then right column.
- **p. 4:** equation (10); Gaussian cdf definition; equations (11)-(13) (non-bold limits in the integral, bold `\overline{z}`, `\underline{z}` afterwards, as printed); values 45, 60, 4, 1, 0.0001; Figure 1 and caption; equation (14); IV-A, equations (15)-(16); footnote 4 text.
- **p. 5:** unnumbered `\beta_k` display; `N_b = m_k · n_0`; `N' = N + N_b`; equations (17)-(18) (`\tilde{w}^{i*}_{k+1}`, `g(...)` without subscript in (18), as printed); normalisation and resampling sets; Remark; Algorithm 1, all 14 lines (including `g([z]|x^i_{k+1})` in step 8 as printed).
- **p. 6:** equation (19); V-A, interval and box definitions, equations (20)-(21), `S ⊆ [x]' ⊆ [x]`; V-B, equations (22)-(25) (weights printed outside the sums in (24)/(25), kept); footnote 5.
- **p. 7:** Algorithm 2, all 14 lines and both bullets (upper limit `N'(1+m_k)`, step 12 as printed); V-C, equations (26)-(32), footnote 6.
- **p. 8:** equations (33)-(36); the four-line chain (34); `N' × (m_k+1)`; Section VI, conditions 1) and 2); equations (37)-(38).
- **p. 9:** VI-A, equations (39)-(42), `W* = A · N^{-1/(n_x+4)}`, `A = [4/(n_x+2)]^{1/(n_x+4)}`; VI-B, equations (43)-(45) (`α → 1` as printed); VII-A, equations (46)-(47); all scenario numbers (k = 3, 54; 550 m, 300 m; −5, −8.5 m/s; ϖ = 0.05; T = 1 s; 60 s; σ_r = 2.5 m, σ_ṙ = 0.01 m/s, σ_θ = 0.25°; Δr = 50 m, Δṙ = 0.2 m/s, Δθ = 4°).
- **p. 10:** equation (48) (−3/4 Δ, +1/4 Δ); p_D = 0.95, λ = 5, 30 m-700 m, ±15 m/s, ±π/2, τ = 0.5, p_B = 0.01, p_S = 0.98; VII-B; Figure 2 and caption (k = 51; k = 5; N = 5000); Fig. 3 text (N = 32, k = 6).
- **p. 11:** Figures 3, 4 and captions; VII-C run-in headings 1) and 2); lists (i)-(iii) twice; `n_0 ≥ 5000`, `N ≥ 2000`, `N ≥ 32`; the sentence ending in a comma ("...and N = 5000,") is as printed.
- **p. 12:** Figures 5, 6 and captions; `n_0 · m_{k−1}`; 40 s and 19 s; Section VIII; Appendix heading and paragraph a).
- **p. 13:** Figures 7, 8, 9 and captions ("an a function" as printed); equations (49)-(51), including the baseline-set sum index and the absent integral in the numerator of (50), both as printed and declared in the notes; κ(Υ) formula; paragraph b); Acknowledgements.
- **p. 14:** Algorithm 3, 13 lines (unsquared `[\dot{x}]`, `[\dot{y}]` in the first denominators of lines 5-6 and bare `y^2`, `x^2` under the roots, as printed; trailing comma on line 13); references [1]-[25].
- **p. 15:** end of [25], references [26]-[30].
- **Figure and algorithm JPEGs:** all complete (axes, tick labels, legends, sub-panel labels (a)/(b)), no caption or body text inside the crops, legible.
- **index.md:** every heading listed for `paper.md` exists verbatim; equation ranges per section are right. **supplement.md:** correctly says no materials were supplied. **SKILL.md:** consistent with the package.

## Technical question answered from the package only

**Question:** In the Bernoulli box-particle filter, how is the weight of a contracted box particle computed for a given interval measurement, and what value is used for the factor κ in practice?

**Answer from the package** (`paper.md`, section "V. BOX PARTICLE FILTER IMPLEMENTATION", "C. Measurement Update Step", equations (30)-(33), and Algorithm 2 steps 8-9): each predicted box `[x^i_{k+1|k}]` is contracted with the constraint `[z] ∩ (h_{k+1}(x) + [ε_{k+1}]) ≠ ∅` (30) to give `[x̃^i_{k+1}]`; its weight is `w̃^i_{k+1} = (p_D / c([z])) · w^i_{k+1|k} · κ^i_{k+1} · |[x̃^i_{k+1}]| / |[x^i_{k+1|k}]|` (32), where κ is the expectation of the generalized likelihood over the contracted box (33). The integral has no closed form; the authors use the constant `κ^i_{k+1} = 1` for all box particles. A replicated, uncontracted set carries weights `(1 − p_D) w^i_{k+1|k}`.

**Check against the PDF** (pages 7-8): equations (30), (32), (33), the sentence "a constant value for all the box particles, e.g., κ = 1 is a good approximation and we adopt this value for the rest of the paper", and Algorithm 2 step 8 all agree with the answer.
