# hashemi2025pca - conversion report

**Paper**: Hashemi, Lindemann, Deshmukh, "PCA-DDReach: Efficient Statistical Reachability Analysis of Stochastic Dynamical Systems via Principal Component Analysis" (NeuS 2025, PMLR 288:693-707).
**Source version**: arXiv:2505.14935v1, 16 pages; authors' TeX source used for all mathematics. Proceedings version not compared.
**Status**: `reviewed_with_limitations`, `verify --strict` exit 0, 21 adjudications applied, 0 stale, mechanical_ok true.
**Package**: `~/AI_agents/paper2agent/Reachability/skills/hashemi2025pca-paper` (4 staging builds s1-s4; final is byte-identical to s4).

## Counts
- Figures 6 (figure-1 ... figure-6, all image crops, bboxes from ink profiles); tables 1 (table-1.csv); algorithms 0 (paper has none).
- Formulas kept as images: 0. All 18 extractor formula images replaced by `$$` blocks with printed tags (1)-(18); 438 inline formulas; pdflatex compiles all of them.
- Omitted regions 17 (arXiv margin stamp p.1, page numbers pp.1-16). Adjudications 21 (13 missing_lines, 4 number, 4 second-parser number).
- Theorem-like blocks: Definitions 1, 2, 4, Lemma 3, Proposition 5 + Proof, Remark 6 (one shared counter). Footnotes 6. References 28.

## What was corrected
- Every math page rewritten from the TeX with private macros expanded by script (`\dist`, `\distzeroR`, `\eigvecseg`, `\PEsimseg`, ...); glyph soup, `<sup>` tags, a stray strikethrough and a replacement character removed.
- Reading order: Figure 1 (p.7) and Table 1 (p.11) no longer interrupt sentences; `reading_order` moves Footnote 2 after its paragraph (pp.2-3) and Figures 3-6 (pp.14-15) after Sections A.1-A.3; the A.1 paragraph is joined across the float-only page 15.
- Author names were extractor headings (p.1); merged paragraphs split (pp.7, 9); overlapping Figure 5/6 boxes and tick-label text removed (p.15); bibliography regenerated from the .bbl and matched entry by entry to the PDF text layer.

## Limitations and uncertainties
- No uncertain symbol remains; TeX and PDF agree everywhere. Review by one agent, no independent second verifier.
- Theorem bodies are italic in print, written upright; six bold run-in paragraph titles ("Inflating Hypercube", ...) are kept as bold text, not headings (pp.2-6).
- In-figure text exists only inside the crops: segment labels (p.7), panel labels "time step k = 1/2" (p.8), tick labels and legends (pp.14-15; Figure 3 ticks are tiny).
- Table 1 (p.11): two header rows combined into single column names; sizes printed "42, 000" written "42,000"; a marked non-source "Conversion note on Table 1" follows the caption.
- Manual `\!` spacing dropped in displays (6) and (15) (pp.5, 9); percent signs written outside math (pp.10, 14, 16).
- Source defects kept and listed in the conversion notes: (8) index `T_i` (p.7); (10) second covariance factor without index i (p.8); stray `]` in the Section 4.1 covariance (p.11); `V` vs `\mathsf{V}^q` after (17) (p.10).
- Guarantee wording is not uniform in the source (kept, flagged): TV `\le\tau` (p.5) vs `<\tau` (pp.6, 9); `\ge\delta` (flowpipe definition p.6, proof p.10) vs `>\delta` (Lemma 3 p.6, Proposition 5 p.9); Proposition 5 calls `\rho^*_{\delta,\tau}` "the δ-quantile" though it is defined as an upper bound; theory needs τ>0 but Experiments 1-2 use τ=0; the paper never states the probability space of `Pr[.]`.

## Self-check
- SKILL.md, index.md and all 330 lines of paper.md read; no `<sup>`, replacement characters, glyph soup or unbalanced `$`; 22 headings all real.
- Opened figure-2 (smallest labels), figure-3, -4, -5, -6, -1 and table-1.csv: complete and legible.
- Question: "State the main guarantee with its assumptions: what is random, the coverage level, how shift is handled."
  Answer from the package (Section 3.2 Definition 4, Proposition 5, (11)-(15); Section 2.3 (4); Lemma 3): mean `\overline{PE}^q`, eigenvectors `\mathsf{V}^q` and scales `\omega_j` come from the training set; residual `\rho = \max_j |r^j|/\omega_j` with `r = {\mathsf{V}^q}^\top(PE^q - \overline{PE}^q)`. A fresh i.i.d. simulated calibration set gives sorted residuals; with `TV(J^real, J^sim) < \tau`, rank `\ell^* = \lceil (L+1)(1+1/L)(\delta+\tau) \rceil \le L` and `\rho^*_{\delta,\tau} := \rho_{\ell^*}`, Proposition 5 gives `Pr[\bigwedge_j -\omega_j\rho^* \le r^j \le \omega_j\rho^*] > \delta` for a real trajectory with `s_0 ~ W`; by Lemma 3, `X = \bar X \oplus \delta X` satisfies `Pr[\sigma^real \in X] \ge \delta`. δ is the coverage level (99.99 %, 95 %). Checked against 260-300 dpi crops of pp.5, 6, 9: identical.
- Numeric check: formula (4) with Table 1 sizes gives `\ell^* = 20000 = L` (L=20000, δ=0.9999, τ=0) and 9902 (L=10000, δ=0.95, τ=0.04).

## New pitfalls (not in the brief)
- `$\delta = 99.99$%` is tokenised as `99.99`, not `99.99%` (the `$` separates them): write `$\delta =$ 99.99%`.
- Text-size binary operators carry spaces in the PDF layer (`(L + 1)`), script-size ones do not (`t_qn+1`): space the former, not the latter, and `+1` diagnostics vanish.
- `lew2021sampling/linecheck.py` needs page markers that the built `paper.md` no longer has; `work/hashemi2025pca/linecheck.py` reads page text from `pages/*.json` instead.
- Do not read bbox coordinates off a displayed crop (the viewer rescales). `work/hashemi2025pca/inkbox.py` prints the ink bbox and row bands in PDF points; a caption can start under 3 pt below a figure label (p.8).
- Reusable here: `pagelib.py` `X()` (macro expander, also `^*` -> `^{\ast}`), `refs.py` (.bbl -> Markdown entries + comparison with the text layer), `symcheck.py` (skips lines inside figure/table/omit boxes).
- `reading_order` + `join_previous` works across a float-only page (join p.16 to p.14).
