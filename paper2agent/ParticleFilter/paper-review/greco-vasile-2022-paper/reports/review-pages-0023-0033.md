# Review report: Greco & Vasile 2022, PDF pages 23-33

Document: `paper-review/greco-vasile-2022-paper/documents/s001-greco-vasile-2022`. No TeX source; all mathematics
was transcribed from 190/200-dpi crops (equation (40) additionally at 400 dpi). All 11 pages are `reviewed: true`
with `[v2]` notes and have an `adjudication-notes/page-NNNN.json`.

## Pages

| Page | Content | Assets / equations |
| --- | --- | --- |
| 23 | end of III.A.1 (initial epistemic set), `#### 2. Observation model and errors` | Eq. (36), (37), (38) as LaTeX |
| 24 | likelihood epistemic set, `### B. Wall time analysis`, models a), b) | Eq. (39); `table-3` (was a formula image) |
| 25 | model c), regression results, `### C. Results` | `table-4` |
| 26 | `#### 1. Uncertainty propagation` | `figure-3`; unnumbered display PoC_50m ∈ [0, 4.97·10⁻⁵] |
| 27 | ECDF discussion, `#### 2. Collision instance` | `figure-4` |
| 28 | instance B | `figure-5`; displays [0, 2.15·10⁻⁴], [0, 9.69·10⁻³] |
| 29 | instance B performance, `#### 3. No-collision instance` | `figure-6`; display [0, 2.82·10⁻⁴] |
| 30 | instance C end, `#### 4. Measurements simulation instance` | display [0, 0]; Eq. (40) |
| 31 | instance D | `figure-7`; displays [0, 2.94·10⁻²], [1.20·10⁻⁸, 9.94·10⁻¹] |
| 32 | Table 5, `## IV. Conclusions` | `table-5` |
| 33 | Conclusions end, `### A. Estimator Derivatives` (appendix) | inline gradients only |

## Joins
- Set inside the range: first items of pages 23, 28, 29, 30, 31, 33 (`space`); page 24 `p0024-b003` joins
  `p0024-b000` across the floated Table 3.
- Boundary 22 -> 23: `p0023-b000` ("distribution") has `join_previous: space`; page 22 must end with the paragraph
  "... the importance initial distribution is defined as a normal" (it did when I looked).
- Boundary 33 -> 34: page 33 ends with "... The quantity to compute is the gradient of the estimator"; page 34's
  first item already has `join_previous: space`.
- Pages 24->25 (list a), b) | c)), 25->26, 26->27, 31->32 end with complete paragraphs/list entries; no join.

## Formulas kept as images
None. Every display in the range was legible and is LaTeX. Unnumbered displays (the PoC intervals) have no `\tag`.

## Text repairs of substance
- p27: the extractor had swallowed "which would indicate a near-safe conjunction. The difference between" into a
  superscript; over/underlined PoC_300m bounds restored.
- p30: "PoC50m ∈ [0, 0]." had been made a heading; now a display. Overlined PoC restored.
- p33: bold chi_{0:k} had been a superscript.
- p24: Table 3 was a formula image; now a table, moved after the paragraph ending "[48–50]." so it no longer
  interrupts the sentence "... are simulated | starting from ...".
- Authors' typos/wording kept (listed in each page's notes): "a new observations", "each of this models", "the the
  representation accuracy", "A furthermore element", "The simulations of future observations is useful".
- Printed notation inconsistencies kept: lambda_{0-1} vs lambda_{x_{0-1}} (bold x) vs lambda_{x_{0-1}} (italic x) on
  p23; (39) uses y-bar_k while (40) uses y_k.

## Tables
- `table-5`: the spanning header "Time" is folded into the four column names ("Time: Surrogate [s]" ...); values
  printed once per group D1-D3 / D4-D6 (n_λ, L, Surrogate, Proposal) are repeated in each row. I added one
  non-printed text item `p0032-n001` ("Note on Table 5 (transcription): ...") after the table to tell the reader
  this. If the coordinator prefers no non-source text in the page, delete that item and move its content to
  `plan.json` notes.
- Table cells use Unicode (σ, λ, ε, ², ⁻⁶, ·), no LaTeX.

## Remaining diagnostics (all category (a))
- Missing lines on 23-31, 33: lines containing inline/display maths now in LaTeX, units set in maths (24 h), and
  captions with `$3\sigma$`.
- Number differences: Unicode minus vs ASCII minus in exponents/subscripts; `5^2` read as "52" in the PDF; Table 5
  Unicode exponents and repeated group cells (p32); Table 4 header superscripts (p25); second parser splitting
  decimals (4.97, 2.15, 9.69, 2.82, 2.94, 1.20, 9.94, 92.8%, 97.2%).
- Page 32 has full line coverage (66/66).

## Proposals for shared files / coordinator
- Appendix heading level: the manuscript prints "A. Estimator Derivatives" centred in section style and has no
  "Appendix" heading. Pages 34-44 currently use `### B. B&B Algorithm`, `### C. B&B proofs`,
  `### D. Lower bound computation`, so I used `### A. Estimator Derivatives` to match. As they stand, A-D nest under
  `## IV. Conclusions` in navigation and collide by letter with III.A-C. Suggest promoting all four to `##` (the
  brief's rule for lettered appendix sections, e.g. `## A. Estimator Derivatives`) or noting the appendix in plan
  notes.
- No asset-name clashes found across the 44 pages (checked all `asset_name` values).

## Limitations / brief feedback
- Percent values in prose are written as plain text (`75%`) rather than `$75\%$` to keep the number check quiet.
- `check` prints very long pypdf "fontTools is required" warnings on stderr; use `2>/dev/null`.
