# hashemi2023data - conversion report

**Paper:** Hashemi, Qin, Lindemann, Deshmukh, "Data-Driven Reachability Analysis of Stochastic Dynamical Systems with Conformal Inference" (CDC 2023).
**Source:** arXiv:2309.09187v1, 15 pages, single column. Authors' TeX source used for all mathematics.
**Status:** `reviewed_with_limitations`, `verify --strict` exit 0, 28 adjudications applied, 0 stale, no mechanical issues.
**Package:** `~/AI_agents/paper2agent/Reachability/skills/hashemi2023data-paper` (after three staging builds, s1-s3).

## Counts
- Figures 3 (image crops, verbatim captions); tables 3 (CSV, 90 cells checked); algorithms 0.
- Formulas kept as images: 0. Display blocks: 20, with `\tag` for the eight printed numbers (1)-(8). Extractor produced 19 formula images; all replaced by LaTeX.
- Omitted regions: 16 (arXiv margin stamp on p1, 15 page numbers). Footnotes 3. References 37.
- Adjudications 28: 12 missing-lines, 7 number, 9 second-parser number.

## What was corrected
- Math: every inline and display formula rewritten in LaTeX from the TeX source, macros expanded, checked on 190-230 dpi crops and on a pdflatex rendering. TeX and PDF agree everywhere.
- Structure: Definitions 1-4, Theorem 1 and Proof carry bold labels; ends taken from the TeX environments. Theorem 1 is split by the page break 6/7 and joined.
- Reading order: 8 sentences joined across page breaks (4 of them across floats). Figures 1-3, Tables 1-3 and equation (7) moved next to the paragraphs that discuss them via `reading_order`.
- Extraction damage: merged paragraphs split (p3, p6, p10), glyph soup rewritten (p8 fractions, p12 equation (7)), line-wrap hyphens, sup tags, bullet markers in the bibliography.
- Footnotes placed after the paragraph or definition carrying the mark (p2, p6).

## Limitations and uncertainties
- **Distribution shift is not in this paper.** The guarantee assumes calibration and test trajectories i.i.d. from the same distribution; [33] (covariate shift) is cited only for its Lemma 1 (p4). Recorded in the conversion notes so a reader does not look for it.
- p8: the explicit calibration-size bound is printed as ceil((1+delta)/(1-delta)); the stated condition ceil((L+1)delta) <= L only needs L >= delta/(1-delta). Kept as printed, noted in the conversion notes.
  By my arithmetic (not in the package): for eps = 0.01 the condition needs L >= 29999 (ACC, L = 40000, fine), 59999 (Quadcopter, nK = 600, but L = 40000) and 139999 (Laubloomis, L = 160000, fine). Not verified beyond this arithmetic.
- p6: the raised 2 after F^j(s_0) in Definition 3 is the footnote mark, not an exponent (confirmed in TeX).
- p12: equation (7) is an uncaptioned float whose first-parser text layer is unusable; taken from TeX, checked on a 230 dpi crop and character by character against the second parser's text (identical).
- p9-p11: tables are printed as two side-by-side three-column blocks; transcribed with six columns and repeated header names (explained in the notes).
- p9, p11: the unit typed `\sec` in the source is written `\mathrm{sec}`. `\hdots` is written `\ldots`, `^*` is written `^{\ast}`.
- Run-in titles (Notation, the five of Section 2, the three case studies of Section 4) are bold or italic paragraph openings, not headings; they are found by text search, not through the index.
- Authors' slips kept as printed and listed in the conversion notes (subset sign for the trajectory on p3, `e_j` versus `e_{j+n}` and `R_{>0}` on p6, strict inequalities in the proof on p7, and others).
- The TeX archive has an unused `sections/appendix.tex` ("Training the Model"); it is not in the PDF and not in the package.
- One reviewer only; no independent second verifier.

## Self-check
- `SKILL.md`, `index.md` read; `paper.md` read in full (s2 copy; the final differs only in two conversion-note lines). No `<sup>`, replacement characters, `^*`, `~~` or stray `$`; 13 real headings; all math compiles.
- Figure 2 (smallest labels), Figure 3 and the Table 1 and 3 CSVs opened: complete and legible.
- Question: "State the main guarantee, what must hold, the coverage level, and how the flowpipe is inflated."
  Answer from Section 3.2 (Definitions 2-4, Theorem 1): take a surrogate flowpipe X-bar containing F(I); for each output component j in [nK] sort the L calibration residuals R^j_i = |e_{j+n}^T sigma - F^j(s_0)| and let R^{j*} be the ceil((L+1)delta)-th smallest; set X = X-bar (+) Zonotope(0, diag([0_{1xn}, R*])). Then Pr[sigma_{s_0} in X] >= Delta = 1 - nK(1-delta), for a new trajectory with s_0 drawn from the same distribution W on I, given i.i.d. test trajectories. For a target 1-eps, delta = 1 - eps/(nK). The union bound over nK components is the source of conservatism. Checked against PDF pages 6-8: matches.

## New pitfalls (not yet in the brief)
- Build and verify stdout for this PDF is flooded with multi-kilobyte pypdf "fontTools is required" lines; redirect to a file and `grep -v fontTools`.
- A brace-balance assert in a page generator must ignore `\{` and `\}`: a `\left\{ ... \right.` display otherwise fails it.
- When the first parser's text of a display is glyph soup, pypdf may still extract it cleanly; a de-LaTeXed string comparison against pypdf (`logs/work/hashemi2023data/eq7check.py`) is a strong check.
- `symbol_check2.py` counts `\middle|` as two bars (prefix `\mid`) and does not count an `=` typed outside math; `wordcheck.py` and `symbol_check2.py` end with a FileNotFoundError on papers shorter than their hard-coded page range (results above the traceback are valid).
- `refcheck.py` in the same folder compares every math-free item with the text layer inside its bbox including punctuation and dashes; it settled the whole bibliography in one run.
- The arXiv stamp arrives as a `text` item with empty markdown, not as an `omit` suggestion.
