# Review report: Benavoli, Zaffalon, Miranda, "Robust filtering through coherent lower previsions" — PDF pages 9-15

Document: `documents/s001-benavoli-lower-previsions-2011`. No TeX source; all mathematics was typed from 230-dpi column crops, with 380-400-dpi zooms of the dense displays. Scratch (crops and the per-page build scripts `p9.py` ... `p15.py`, `lib.py`): `paper-review/_scratch/benavoli-lp-9-15`.

## State

All seven pages are `reviewed: true` with `[v2]` notes. Every page was rebuilt in reading order (left column, then right column). No formula is kept as an image.

| Page | Content | Equations (as `\tag`) | Assets | `check` |
|---|---|---|---|---|
| 9 | end of Sec. IV, `### A. Decision making and estimation`, `## V. BIASED MEASUREMENT NOISE`, start of Theorem 3 | (25), (26), (27) + 1 unnumbered | - | 73/130 lines, all (a) |
| 10 | Theorem 3 (rest) and its proof, footnote 7 | (28)-(36) + 2 unnumbered | - | 32/119, all (a) |
| 11 | lower/upper mean, erf display, variance; `## VI. LINEAR-VACUOUS MIXTURE MODEL`; footnotes 8, 9 | (37)-(40) + 5 unnumbered | - | 54/115, all (a) |
| 12 | Theorem 4 and proof, operator decomposition | (41)-(49) | - | 34/107, all (a) |
| 13 | LGVM filter, `## VII. NUMERICAL EXAMPLE`, simulation set-up | (50)-(52) + 1 unnumbered | `table-cases-1-4-p0013`, `table-case-5-p0013` | 86/115, all (a) |
| 14 | results, `### Software availability`, `## VIII. CONCLUSIONS`, `## ACKNOWLEDGEMENTS` | - | `figure-1`, `figure-2`, `figure-3`, `figure-4` | 52/59, all (a) |
| 15 | end of acknowledgements, `## REFERENCES` [1]-[32], three author biographies | - | - | OK (158/158) |

Adjudication notes written for pages 9-14 (`adjudication-notes/page-0009.json` ... `page-0014.json`); page 15 needs none.

## Remaining diagnostics (all category (a))

- Missing lines on pages 9-14: every one contains inline/display maths now in LaTeX, is a fragment split at an underline/overline glyph or footnote marker, or (page 13) is a table cell with epsilon/delta stored as Unicode text. Pure-prose lines all match.
- Number differences: U+2212 minus tokens in sub/superscripts or intervals versus ASCII minus in LaTeX (`−1`, `−2`, `−0.5`, `−30`, `−100`), `+1` tokenisation of `k+1`, `2125` (PDF glues the square to 125 in `(1−ε_w)^2 125`). The second parser additionally splits decimal table cells on page 13.

## Joins

- Set inside the range: p9 'With this in mind ...' -> right column; p10 '... (g-mu)] =' -> '0. From Corollary 1 ...'; p12 '... the previous' -> 'equation can be rewritten ...'; first item of each of pages 10-15 has `join_previous: "space"` (Theorem 3 statement p9->p10; paragraphs p10->p11, p11->p12, p12->p13, p13->p14; acknowledgements p14->p15).
- **Boundary join needed at page 8/9:** the first item of page 9 ('converges to 0 for k = 1, ..., t, ...') has `join_previous: "space"`. It continues the right-column paragraph that ends page 8 ('Assuming some regularity conditions [21, Sec. 6.10.4], as the radius δ(y_k) of the neighborhoods ỹ_k = B(y_k, δ(y_k))'). That paragraph must be the last item of page 8 in file order (in the extractor's order it already is; the left-column Corollary 1 text must not come after it).

## Theorem-like blocks

`**Theorem 3.**` (pages 9-10, statement split around displays (27)-(31)), its `**Proof:**` (page 10), `**Theorem 4.**` and `**Proof:**` (page 12). Statements and proofs are italic in print; they are set upright with bold labels. End squares kept as `■`.

## Figures and tables

- Figures 1-4 (page 14): the extractor had merged Fig. 3 and Fig. 4 into one box and garbled the Fig. 3 caption; now four figure items with boxes checked by crop (tick labels, axis labels, legends inside; Fig. 4 has two stacked panels and one legend). Pages 1-8 contain no figure or table items in the extractor output, so `figure-1`..`figure-4` should not clash.
- Two unnumbered in-text tables on page 13 (simulation cases 1-4 and case 5) are `table` items with plain-text cells (`ε_w`, `5δ_7/(1 − ε_w)`, `N(0, 125)`, `[0, 5δ_7/(1 − ε_w)]^T`; no backslashes). The first one sits inside a sentence in print ('... have been simulated' [table] 'where δ_k is 1 when ...'); it is kept in place like a display equation, without a join across it.
- Three author portraits on page 15 are omitted as decorative.

## Printed oddities kept verbatim (candidates for a plan note)

- Theorem 3 and Theorem 4 statements print `\underline{E}_{X_t}[g|y^t]` without tilde, while the equations use `\tilde{y}^t`; Eq. (34) prints `I_{\{y^t\}}` without tilde; joint subscripts are `X^t,Y^t` without tilde except in (35) and the sentence after it.
- Page 9: `x_y, y_k ∈ R` (for `x_k`); `θ_k is the mean of the measurement noise at time t`.
- Page 10: `j = 1,...,k-1,k+1,...,≤ t`; `(35))`; `δ(y_k)` next to `y_t`.
- Page 11: lower mean printed with `max(θ^L, θ^U)` and upper mean with `min(θ^L, θ^U)`; `availabile`; `(1-ε_x)e_k`.
- Page 12: Eq. (49) uses `C'` whereas the surrounding text uses `C^T`; Eq. (48) last factor `N(y_{j-1}; C x_i, R)`; Eq. (47) has no `dx_t`.
- Page 14: `LVGM filter`; there is no figure for case 4 (Fig. 4 shows case 5).

## Proposals for shared files

- `plan.json` notes: (1) no TeX source, mathematics transcribed from the author manuscript image; (2) the manuscript has no appendix, proofs are inline; (3) the notation inconsistencies listed above are the authors'.
- Navigation headings in my range: `### A. Decision making and estimation`, `## V. BIASED MEASUREMENT NOISE`, `## VI. LINEAR-VACUOUS MIXTURE MODEL`, `## VII. NUMERICAL EXAMPLE`, `### Software availability`, `## VIII. CONCLUSIONS`, `## ACKNOWLEDGEMENTS`, `## REFERENCES`. The other reviewer should use `## IV. ...` for the parent of subsection A.

## Limitations and remarks on the brief

- Item ids on my pages were regenerated (`pNNNN-rKKK`; the page-number omit item keeps its original id) because almost every item was split, merged or reordered.
- The assignment hint mentions appendix proofs; this manuscript has none.
- The bibliography on page 15 was compared entry by entry with crops only for [8]-[17] and [27]-[32]; the rest relies on the preview and on the verifier finding all native lines verbatim.
- Emphasis inside prose (italic theorem bodies) was not reproduced; only genuinely emphasised terms (*credibility region*, *linear prevision*, *linear-vacuous mixtures*, *ε-contamination*, *Linear Gaussian-Vacuous Mixture*) keep italics.
