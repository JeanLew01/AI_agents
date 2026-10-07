# Review report: Greco & Vasile 2022, PDF pages 12-22

Document: `paper-review/greco-vasile-2022-paper/documents/s001-greco-vasile-2022`. No TeX source; all mathematics
transcribed from 170-dpi page renders plus 250-300-dpi crops of the dense displays. All 11 pages are
`reviewed: true` with `[v2]` notes; an adjudication note exists for every page (all still report diagnostics, all category (a)).
Page-building scripts are in `_scratch/greco-12-22/p12.py` ... `p22.py` (re-running them overwrites the page and the
unpruned adjudication note; the adjudication notes on disk were pruned afterwards to the keys `check` reports).

## Pages
| Page | Content | Assets / equations |
| --- | --- | --- |
| 12 | end of II.B.2 paragraph, Algorithm 3, `#### 3. Algorithmic Complexity` | `algorithm-3` (image + transcription) |
| 13 | complexity of precomputation / pSIS | Eqs. (14), (15) |
| 14 | `#### 4. Polynomial propagator`, `### C. Bound Estimator` | Eqs. (16), (17), (18) |
| 15 | bound estimator, confidence interval | Eqs. (19a), (19b), (20), (21) |
| 16 | Algorithm 4, `### D. Global search` | `algorithm-4` (image + transcription) |
| 17 | `#### 1. Preliminary definitions`, `#### 2. Bounding` | Eqs. (22)-(25), 3 unnumbered displays |
| 18 | Lemma 1, Lemma 2, `#### 3. Branching` | Eqs. (26), (27), (28) |
| 19 | Lemma 3, `#### 4. Convergence`, Theorem 1, `#### 5. Filter complexity with epistemic dimension` | Eqs. (29), (30), 3 unnumbered displays |
| 20 | complexity bound, `#### 6. Lipschitz constant estimation`, `## III. Numerical Experiments` | Eqs. (31), (32) |
| 21 | `### A. Definition of the conjunction scenario` | `table-1` (cells, 3x8) |
| 22 | PoC definition, `#### 1. Initial state uncertainty` | Eqs. (33), (34), (35a), (35b); `table-2` (cells, 2x6) |

No formula was kept as an image; every extractor `formula` item was replaced by a LaTeX display block.

## Joins
- Set: page 12 first item (continues page 11 "... Furthermore," -> "the UKF-based proposal ..."), page 20 first item,
  page 21 first item, page 22 first item (all `space`).
- Needed from neighbours: page 11 must end with the text item "With this approach, ... Furthermore," (it does in the
  current extraction); page 23's first item needs `join_previous: "space"` (page 22 ends "... is defined as a normal").
- Per the collection convention no join is set on text that follows a display.

## Layout decisions
- Page 12: Algorithm 3 is a top-of-page float; the continuing paragraph was moved in front of it. The algorithm
  transcription marks loop membership with reviewer parentheticals "(inside the loop over k/j)" / "(loop over k/j)"
  because the printed indentation cannot be kept in markdown; everything else is as printed.
- Captions of Tables 1 and 2 precede the tables, as printed.
- Lemma/theorem statements are printed in italics; only the bold label is reproduced.

## Authors' oddities kept as printed (candidates for plan notes)
- Eq. (20), second line: "for j = n + 1, ..., 2l" (prose uses l + 1).
- Page 15: weights $\hat{w}_M^{(i)}$ in the estimator, $w_M^{(i)}$ (no hat) in the following line.
- Page 17: "lb : S -> R" with italic R (blackboard R in "2. Bounding"); covering condition "= Omega" without subscript;
  vertex list indexed to n rather than n_lambda; (23)/(24) without brackets around the max argument.
- Page 18: vertices written lambda_{i*}, lambda_{j*} before Eq. (28) and lambda*_i, lambda*_j from (28) on.
- Page 19: Lemma 3 second display minimises over S_k^{(j)} in L_K; "lb(S*) <= lb(S_k^{(j)})" uses blackboard S; U_k defined with min.
- Page 20: Omega_lambda with non-bold lambda in one paragraph; "yield".
- Page 21: "envisage", "that needs to estimated", "Sec.II.B.3".

## Remaining diagnostics (all category (a))
- Missing lines on every page: lines with inline/display maths now in LaTeX (page 21: only the `x_k` line).
- Number differences on 12, 13, 15, 16, 18: sub/superscript digits, U+2212 versus ASCII minus, and (12, 16) the
  algorithm transcription repeating numbers that sit inside the excluded image box.
- Page 22, second parser only: splits "0.1" of the Table 2 caption into "0" and "1".
- Pages 14, 17, 19, 20, 21: no number differences.

## Notes for the coordinator
- Asset names used: `algorithm-3`, `algorithm-4`, `table-1`, `table-2` (printed numbering; Algorithms 1-2 and Figures 1-2
  are on pages 1-11, Tables 3-5, Figures 3-7 and Algorithm 5 on later pages; no clash expected).
- Table 2 header cells use plain text for nested subscripts ("1σ_rU [m]").
- Brief feedback: `check` prints very large pypdf "fontTools" warnings on stderr; `2>/dev/null` is needed to read the output.
  The brief says to set `join_previous` on a split paragraph, while the assignment convention forbids joins onto displays; I followed the latter.
