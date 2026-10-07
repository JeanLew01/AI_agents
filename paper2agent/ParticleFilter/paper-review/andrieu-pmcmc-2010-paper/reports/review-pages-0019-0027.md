# Review report: Andrieu, Doucet, Holenstein (2010), PDF pages 19-27 (printed 287-295)

All nine pages are `reviewed: true` with `[v2]` notes; each has an `adjudication-notes/page-NNNN.json`.
Scratch (crops and the per-page build scripts `p19.py` ... `p27.py`, `pg.py`): `paper-review/_scratch/andrieu-19-27`.
No TeX source: all mathematics transcribed from 220-330 dpi crops; prose from the native text lines, checked against crops.
Item ids were regenerated as `pNNNN-rXX` (unique per page).

## Per page

| PDF page | Content | Assets / numbered equations | Headings |
| --- | --- | --- | --- |
| 19 | Full-page rotated Fig. 7 (Lévy-driven SV model, S&P 500) | `figure-7` (bbox [140,49,323.5,630], panels (a) and (b)); caption item | - |
| 20 | End of Section 3 paragraph; Section 4 intro; 4.1 set-up | none (inline maths only) | `## 4. A generic framework for particle Markov chain Monte Carlo methods`, `### 4.1. A generic sequential Monte Carlo algorithm` |
| 21 | Generic SMC algorithm (Step 1 (a)-(b), Step 2 (a)-(c)) as text items; ancestral lineage notation | 2 unnumbered displays, (20), (21), (22) | - |
| 22 | Supports S_n, Q_n; Assumptions 1-3 | unnumbered S_n/Q_n display, (23), (24), (25) | - |
| 23 | Assumption 4; Theorem 1; 4.2 PIMH update | unnumbered Assumption-4 display, (26), (27), (28), (29) | `### 4.2. The particle independent Metropolis–Hastings update` |
| 24 | Extended proposal/target; Theorem 2; Theorem 3(a) | (30), (31), unnumbered Theorem 3(a) display | - |
| 25 | Theorem 3(b); discussion; 4.3 conditional SMC (Step 1 (a)-(b), Step 2 (a)-(c)) as text items | (32), unnumbered L_*^N display, (33) | `### 4.3. The conditional sequential Monte Carlo update` |
| 26 | Conditional SMC discussion; sub-block update (a)-(c); 4.4 PMMH update | (34), (35) | `### 4.4. The particle marginal Metropolis–Hastings update` |
| 27 | S_n^theta, Q_n^theta; Assumptions 5-6; Theorem 4; 4.5 PG sweep step (a) | unnumbered S/Q display, (36), (37), 2 unnumbered displays | `### 4.5. The particle Gibbs update` |

No tables. No formulas kept as images. Algorithms are text (assignment convention), one item per printed step.

## Joins
- Set: page 20 first item (`p0020-r02`, "is less demanding as we could design ...") `join_previous: "space"`; page 27 first item (`p0027-r02`) `join_previous: "space"` (continues page 26).
- **Boundary problem at the start of my range (needs the coordinator):** the paragraph ending page 17 ("... we believe that the PMCMC methodology") continues on page 20, with the full-page Figs 6 (page 18, other reviewer) and 7 (page 19) in between. In file order the item before `p0020-r02` is the Fig. 7 caption (`p0019-r03`), so the join would glue the sentence onto the caption. Proposal: add a `reading_order` in `plan.json` that places `p0020-r02` directly after the last text item of page 17 and moves the Fig. 6 and Fig. 7 figure+caption items (pages 18, 19: `p0019-r02`, `p0019-r03`) after `p0020-r02` (i.e. before the `## 4.` heading `p0020-r03`). If no reading order is used, remove the join on `p0020-r02`.
- End of range: page 27 ends with PG sweep step "(a) ...," ; page 28 starts with step "(b)" as a separate item. No join needed.
- No joins onto displays; sentences continuing after a display are separate items.

## Printed oddities kept verbatim (not corrected)
- p. 25, conditional SMC Step 1(a): proposal printed as `q_1(\cdot)` (Section 4.1 uses `M_1`).
- p. 27: `\mathcal{S}_n^\theta = \{x_{1:n}\in\mathcal{X}^n\in\mathcal{X}^n : ...\}` (duplicated membership); convention `M_n^\theta(x_1|x_{1:0}) := M_1^\theta(x_1)`; "unormalized"; "defined on some space $\Theta\times\mathcal{X}^P\to\mathbb{R}^+$ as defined in equation (8)".
- p. 24: `\mathcal{L}^N(X_{1:P}(i)\in\cdot)` with parentheses in the prose, braces in Theorem 3.
- p. 26: reference to "equation (41)" (appendix) as printed.
- Lower-case "assumption n", "theorem n" in running text as printed. Inline sums/products printed as upright capital Sigma/Pi are written `\Sigma`, `\Pi`.
- Fig. 7 caption: the printed line-style samples in the legend are approximated with characters (`·······`, `-------`, `———`, `┈┈┈┈`).

## Text repairs of substance
- Extractor formula images replaced by LaTeX everywhere (about 30 displays); the generic SMC steps 2(a)-(b) (p. 21) and the complete conditional SMC algorithm (p. 25), which were hidden inside formula images, are now text.
- Glued words split (p. 21 "operationbywhichoffspring...", p. 22 "first-offspringparticlesareassociated"); `Å` -> `*` superscripts; `<u>`/`<sup>` soup removed; heading 4.3 separated from "The expression".
- Line-wrap hyphens rejoined (listed in each page's review_notes); real compounds kept ("sub-blocks", "first-offspring", "well-known", "resample–move").

## Remaining diagnostics (all category (a))
- Page 19: 2 missing lines = rotated caption lines with inline maths.
- Pages 20-27: missing lines are display formulas, algorithm steps with maths, prose lines containing inline LaTeX (the checker's normalisation also sees LaTeX command letters, e.g. `\mathbf{X}` in an otherwise unchanged prose line) or lines ending in a rejoined hyphen. Number differences on every page are exclusively U+2212 "−1" versus ASCII "-1" (plus one or more "1" tokens in the second parser on pages 20, 21, 26). No prose number is missing.

## Proposals for shared files
- `plan.json` `reading_order` for Figs 6-7 as described above.
- Navigation headings: Section 4 and 4.1-4.5 start in this range.

## Limitations / brief feedback
- Fig. 7 is printed rotated by 90 degrees; the asset is kept in page orientation (rotated). The caption was transcribed from a rotated crop.
- The brief's rule "each page must start/end with continuing prose" cannot be met on full-page figure pages without a plan-level reading order; reviewers cannot edit plan.json.
- `check` flags any prose line that contains a LaTeX command, so "missing line" counts are high even when prose is exact.
