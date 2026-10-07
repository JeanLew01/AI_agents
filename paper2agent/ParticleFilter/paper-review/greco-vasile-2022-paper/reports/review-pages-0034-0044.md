# Review report: Greco & Vasile 2022, PDF pages 34-44

Document: `paper-review/greco-vasile-2022-paper/documents/s001-greco-vasile-2022`. No TeX source; all mathematics transcribed from 170-260 dpi crops.

## State
All eleven pages (34-44) are `reviewed: true` with `[v2]` notes. Item ids on pages 34-40 were regenerated as `pNNNN-rKKK` (pages rewritten from scratch); pages 41-44 keep the extractor ids. `plan.json` had no `reading_order` referring to these pages.

## Content per page
- 34: Appendix A (end): equations (41), (42), (43a), (43b), (44), (45) as LaTeX with `\tag`; heading `### B. B&B Algorithm`; first paragraph of B (continues on 35).
- 35: continuation paragraph, **Algorithm 5** (`algorithm-5`, image crop [70,67,542,380] + line-by-line transcription), heading `### C. B&B proofs`, proof of Lemma 1 up to equation (46).
- 36: end of Lemma 1 proof, proof of Lemma 2 (two unnumbered displays), start of Lemma 3 proof (one unnumbered display).
- 37: end of Lemma 3 proof (two unnumbered displays), proof of Theorem 1, first part (five unnumbered displays).
- 38: end of Theorem 1 proof (five unnumbered displays), heading `### D. Lower bound computation`, first paragraph.
- 39: equations (47a), (47b), (48) and three unnumbered displays.
- 40: three unnumbered displays, `## Funding Sources`, `## References`, references [1]-[5].
- 41: references [6]-[19]. 42: [20]-[32]. 43: [33]-[46]. 44: [47]-[52] (rest of page blank).
- No figures or tables in this range. No formulas kept as images (all 35 extractor formula images replaced by LaTeX text).

## Joins
- Set: page 34 first item `join_previous: space` (continues page 33's last sentence "... the gradient of the estimator" / "with respect to the epistemic parameters"); page 35 first item `space` (paragraph of page 34 continues after Algorithm 5, which was moved below the paragraph); page 40 first item `space` ("Hence, to" / "find a unique value").
- Needed at the boundary: page 33 must end with the paragraph "Let us assume that we can compute ... The quantity to compute is the gradient of the estimator" as its last non-omitted item (text or caption), with no footnote after it. At the time of writing it did.
- No join at 35/36 (36 starts a new sentence after display (46)), 36/37, 37/38, 38/39 (new paragraphs).

## Printed peculiarities kept (not corrected)
- (43a) left side is the gradient of the unnormalised weight (no hat); (44) reuses k as summation index and time index.
- Algorithm 5: both lower and upper bound lists use `min`; children written S^{*^1}_{k+1}, S^{*^2}_{k+1}.
- Theorem 1 proof mixes K and k ("S*_K ... at the k-th iteration", "K_eps < k", "to obtain S*_k").
- Appendix D: second sphere equation has theta-hat(lambda_1) on the right; (48) uses m_{0n}, c_{0n} with plain n; "n + 1 hyper-cones" versus n_lambda.
- Reference [40] has an empty field ("Space,” , 2021."); "simplical" in [33].

## Text repairs of substance
- [33] DOI: extractor dropped the hyphen at the line break; restored `S0898-1221(02)00205-5`.
- [51] "B- plane" -> "B-plane". [31] `R<sup>n</sup>` -> `$\mathbb{R}^n$`. `1<sup>st</sup>` -> `1st` in [3], [21], [43].
- Extractor list bullets (`- [n]`) removed from all references; italic titles kept as `*...*`.
- End-of-proof squares appended as `$\square$` to the last sentence of each proof; "Proof." (italic in print) given as bold `**Proof.**`.

## Remaining diagnostics (all category (a))
- 34-40: missing lines are all lines with LaTeX mathematics; number differences are PDF-minus versus ASCII minus (`k-1`, `^{-1}`), `n_\lambda - 1` (page 39), and on page 35 the extras from the Algorithm 5 transcription (source lines are inside the figure box).
- 42: one line ([31], `$\mathbb{R}^n$`). 43: `1221` versus `-1221` from the rejoined DOI of [33].
- 41 and 44: OK.
- Additional check done: multiset comparison of all words of four or more letters between native text and my markdown for pages 34-40 shows no difference.
Adjudication notes written for pages 34-40, 42, 43.

## Proposals / notes for the coordinator
- Navigation: appendix subsections B, C, D are `###`; this assumes page 33 carries `### A. Estimator Derivatives` under `## Appendix` (the extractor had `# **A. Estimator Derivatives**` there).
- Brief: nothing wrong; the `check` tool prints many pypdf "fontTools" warnings on stderr (use `2>/dev/null`).
