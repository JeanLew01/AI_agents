# lew2021sampling - reviewer report

**Paper**: Lew, Pavone, "Sampling-based Reachability Analysis: A Random Set Theory Approach with Adversarial Sampling" (CoRL 2020 / PMLR 2021).
**Source**: arXiv:2008.10180v2, 16 pages single column (main pp. 1-8, refs pp. 9-11, appendices A-D pp. 11-16). Authors' TeX used.
**Result**: `verify --strict` exit 0, status `reviewed_with_limitations` (33 applied adjudications, 0 stale, 0 unresolved, 12/12 image crops pixel-match).
**Package**: `~/AI_agents/paper2agent/Reachability/skills/lew2021sampling-paper` (staging s1, s2; final rebuilt once to correct navigation wording).
**Scratch**: `logs/work/lew2021sampling/` (one `pageNN.py` per page, `make_plan.py`, `make_adjudications.py`, `linecheck.py`, `verify-strict.out`).

## Counts
- Figures: 10 (Figures 1-6 in `assets/figure/`; appendix Figures 7-10 in `assets/supp_figs/supplementary-figure-7..10`, labels as printed).
- Algorithms: 2 (Alg. 1 randUP, Alg. 2 robUP!), each image crop + line-by-line LaTeX transcription with printed line numbers.
- Tables: 1 CSV (`figure-5-table`, the table printed inside Figure 5; the paper has no numbered tables).
- Display equations: 29 LaTeX blocks; printed tags (1)-(22) incl. (19a)-(19c). Formulas kept as images: 0.
- Omitted regions: 17 (arXiv stamp and CoRL footer banner on p. 1, page numbers pp. 2-16).
- Adjudications: 33 (13 missing_lines, 10 number_differences, 10 independent_parser_number_differences); pages 1, 9, 10 clean.

## What was corrected
- Math: all inline/display math rewritten from TeX with macros expanded; 23 extractor formula images replaced (pp. 3, 5, 6, 12, 14, 15, 16). All 29 displays compiled with pdflatex and compared with 220-260 dpi crops.
- Theorem blocks: Theorem 1 (p. 5) had been swallowed with Figure 2 into one image; now text with (C1)/(C2) as eqs. (3), (4). Theorem 2 (p. 5, restated p. 11), Definitions 1-2, Proof carry bold labels.
- Algorithms: Alg. 1 (p. 4) was interleaved line by line with the wrapped paragraph; Alg. 2 (p. 6) was a "heading" plus image-only table. Both rebuilt.
- Figures: Figs. 4, 5, 8 merged from panel fragments; Figs. 2, 6, 10 were missing and are cropped; all edges checked at 200 dpi.
- Wrapped paragraphs (pp. 4, 8, 13) rebuilt from TeX and checked word by word; merged paragraphs split (pp. 4, 5, 14, 15); lost line "Volume computation ... in closed form as" restored (p. 15).
- Line-wrap hyphens restored (sampling-based, learning-based, Borel-Cantelli, Olivares-Mendez, Springer-Verlag, non-linear in [25]); accents and broken URLs in refs [1], [19], [25], [32], [47]; all 50 entries read against page and .bbl.
- Cross-page joins pp. 1-2, 2-3, 6-7, 15-16; Footnote 1 moved after the abstract so the p. 1-2 join works.
- Checks: word-multiset per page vs pdftotext (no prose word lost); `linecheck.py`: all 325 tool-missing lines have their words in order (math notation only); symbol counts explained; every number token attributed.

## Limitations and uncertainties
- Figure 5 (p. 7) is L-shaped; the single crop unavoidably includes the printed caption (also transcribed). Its table has columns X_0, X_1, X_2, X_4, X_5 as printed; row labels are plain text in the CSV, LaTeX form in a note.
- Theorem labels are written fully bold incl. title (`**Theorem 1 (...).**`); print has bold number, roman title. Theorem-body italics not reproduced; "infinitely often" in (3), (4) is upright.
- Footnotes 2 and 4 sit at the end of their pages, i.e. under Section 2 and Section 7 although cited in Sections 1 and 6 (stated in index and notes).
- Appendix figure asset names use the printed numbers (7-10), not 1-4: my reading of "supplementary-figure-N".
- Source slips kept, not corrected (listed in conversion notes): calligraphic K in Definition 1 (p. 4); parameter set exponents differ between Section 3/Theorem 2 (U^{k-1}), Alg. 1 prose (U^N, W^{N-1}) and Section 4/proof (U^k) (pp. 4-6, 11); index range in (2) (p. 3); extra ")" after (5) (p. 6); theta_k and overlapping disturbance index ranges (p. 8); Q_nom = h Q h^T, square placement in (14), unmatched parenthesis in c (p. 14); Gamma(n/2+2) in (17) (p. 15); five misspellings.
- One reviewer only; no independent second verifier. Session was interrupted once (out of memory) and resumed from disk.

## Self-check
Question: "State the convergence result for randUP with its assumptions, and the adversarial update of robUP!."
Answer from the package (Section 3, Theorem 2; Section 4, eq. (5) and Algorithm 2): for i.i.d. tuples (x_0^j, u^j, theta^j, w^j) in X_0 x U^{k-1} x Theta x W^{k-1}, with x_k^j from dynamics (1) and X_k^m = Co({x_k^j}_{j=1}^m), if P(x_k^j in G_k) > 0 for every open G_k with X_k ∩ G_k ≠ ∅, then X_k^m -> Co(X_k) almost surely as m -> infinity. Standing assumptions (Section 2): compact X_0, U_k, Theta, W; f continuous (C^1 only needed for robUP!). No rate is given ("Rate of convergence" paragraph). robUP! maximises L^M(z) = (1/N) sum_k ||x_k(z) - c_k^M||^2_{Q_k^M}, Q_k^M the inverse sample covariance, by projected gradient ascent: for i = 1..n_adv: z^j <- z^j + eta grad_z L^M(x^j_{1:N}); z^j <- Proj_Z(z^j); re-propagate; add the new particles; return Co of all particles.
Checked against 230-260 dpi crops of PDF pp. 5, 6 and 11: identical.

## Brief / tool feedback
- The number tokenizer reads `(128,128)`, `{50,100,200}`, `{83,173,...}` as thousands-grouped numbers; writing them with a space after the comma removes the diagnostic. `n/2+2` gives a `+2` token; `n/2 + 2` does not.
- `symbol_check2.py`: the PDF text of `\implies` is "=⇒" (one extra "="), big-cup is a different glyph from `∪`, `\bigg|` is not "|"; the script needs `\leq/\geq/\neq/\rightarrow/\gets/\epsilon` variants.
- `check_missing.py` flagged 72 false positives here; `linecheck.py` (letters-only substring-in-order after stripping LaTeX, function names kept) flagged 0 of 325 and may be worth sharing.
- The brief should say what to do with L-shaped figures whose caption sits inside the bounding box, and with unnumbered tables inside figures.
- "Footnotes at the end of the page's items" puts a footnote under the next section when a section ends mid-page; the navigation text must then say where it is.
- wrapfigure layouts (text beside an algorithm/figure) are the main extraction failure in this paper; expect to rebuild those paragraphs from TeX.
- Writing one generator script per page made the restart after the memory failure a non-event.

## Post-verification repair
An independent verifier (`logs/verify/lew2021sampling.md`) found no textual or mathematical error and two items, both repaired in the page generator scripts:
- [B] Figure 6 (p. 8) was cut at the bottom: bbox bottom moved from y=306 to y=315 pt (`page08.py`). Measured on the 200 dpi render: axis line at 305.3 pt, x tick labels "0", "2" at 307.8-312.8 pt, caption from 320.8 pt. New `figure-6.jpg` (205 x 351 px) opened from the final package: both x tick labels and the full y label "0" are visible, caption outside. My first edge check was by eye on an overlay and was wrong; all 12 crops were then re-checked numerically (no dark pixel on any crop edge, blank band outside each edge).
- [C] Appendix A, first proof paragraph (p. 11): the composition in the definition of f(z) now uses `\circ\ldots\circ` (baseline dots as printed); eq. (2) and the text after eq. (5) keep centred dots (`page11.py`, page note added).
Rebuild: staging `-s3`, then final package deleted and rebuilt. Diagnostics and fingerprints were unchanged (Figure 6 is a raster image, its tick labels are not in the text layer), so the 33 adjudications apply as before (0 stale, 0 unresolved). `verify --strict`: exit 0, status `reviewed_with_limitations`.
