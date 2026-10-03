# Report: dietrich2025data

**Paper.** Dietrich, Devonport, Tu, Arcak, "Data-Driven Reachability with Scenario Optimization and the Holdout Method" (CDC 2025).
**Source version.** arXiv:2504.06541v2 [eess.SY], 11 Sep 2025, 7 pages, IEEE two-column. Authors' TeX (root.tex, reachable_fig.tex, root.bbl) used as transcription aid.
**Result.** `verify --strict`: exit 0, status `reviewed_with_limitations` (the only limitations are the 16 adjudicated parser diagnostics). All 7 pages reviewed.
**Final package.** `~/AI_agents/paper2agent/Reachability/skills/dietrich2025data-paper` (9 files; build hashes re-checked after the restart, no mismatch).

## Counts
- Figures: 3 (image crops, checked at 200 dpi). Tables: 2 (CSV, 11 x 5 each). Algorithms: 0.
- Formulas kept as images: 0. Displays in LaTeX: 20, with printed tags (1)-(14); 6 displays are unnumbered in print.
- Omitted regions: 1 (vertical arXiv stamp, page 1). Adjudications: 16 (missing_lines on pages 1-6; both number checks on pages 3-7).

## What was corrected
- Math: every inline and display formula rewritten in LaTeX from the TeX source; all 20 formula images replaced. Checked three ways: 220 dpi renders, a scripted comparison of all 163 formulas with the TeX (7 non-matches, all explained), and a pdflatex compile of every formula compared visually with the pages.
- Reading order and paragraphs: column-break splits merged (pages 1-6); cross-page sentences joined (3->4, 4->5, 5->6, 6->7); bibliography order restored (the extractor had [15] after [36]).
- Lost content restored: the heading "IV. APPLICATIONS" (page 3) was missing from the extraction; Lemma 1 and its proof (page 6) were superscript debris with replacement characters.
- Text damage: line-wrap hyphens, diacritics in references, emphasis debris, `<sup>` tags.
- Tables I and II: cell-by-cell against the render and the TeX tabular; printed precision kept.
- Relocations (stated in the conversion notes): author note and IEEE copyright notice after the author line; Figure 1 after Theorem 1 and its follow-up paragraph; Figures 2-3 after the citing paragraphs; Footnote 1 after the paragraph carrying its mark (the page-end position would have broken a cross-page sentence).
- Added, clearly labelled: a transcription of the text inside Figure 1 (it holds the only explicit `\epsilon := \overline{Bin}(\hat k, M, \beta)`), and a conversion note under each table about the row-group label.

## Limitations and uncertainties
- No symbol is uncertain. `\mathbb{1}` (printed double-struck 1, TeX `\mathds{1}`) renders correctly in MathJax but not in plain pdflatex without bbm.
- Displays (3)-(4) are one aligned display in print; given as two consecutive displays so that each keeps its printed number (page 2).
- Authors' inconsistencies kept and noted: `k` without hat in II-E and in "Computation"; indicator subscript in (5); `R(\theta)` without hat in II-C; `g(\theta^*, x)` argument order in V-A; `\epsilon` (II to V-A) vs `\varepsilon` (V-B), same printed glyph; typos "futher", "critize", "Alburquerque".
- Content caveat for the reader: the paper gives **no a-priori sample-size formula**. The scenario step has no bound of its own here (wait-and-judge `\epsilon` is a-posteriori and deferred to [19]); sample sizes are the experimental N and M only. Theorem 1 is cited from [28, Thm. 3.3] without proof; only Lemma 1 is proved. No appendix.
- "CDC 2025" comes from the task statement; the PDF itself only carries the ©2025 IEEE notice.

## Self-check
- Final `paper.md` read in full (405 lines); damage scan clean (`<sup>`, replacement characters, stray hats, `~~`, unbalanced `$`, braces); 22 real headings; Figure 1 (smallest labels) and Figure 3 opened and legible; table CSVs correct.
- **Question.** State the main guarantee with all assumptions: what is bounded, over which randomness, and how the bound depends on the holdout size.
- **Answer from the package (Sections II-E and III).** Definition 1: for `\hat k` violations among M newly sampled scenarios and `\beta \in (0,1]`, `\overline{Bin}(\hat k, M, \beta) = \max_e \{e : Bin(\hat k, M, e) \ge \beta\}` with `Bin(\hat k, M, e) = \sum_{j=0}^{\hat k} \binom{M}{j} e^j (1-e)^{M-j}` ((7)-(8)). Theorem 1: for any `\beta \in (0,1)`, `P\{V(\hat R(\theta)) > \overline{Bin}(\hat k, M, \beta)\} \le \beta` ((9)), where `V` is the violation probability (2). The probability is over the M i.i.d. holdout samples with `\hat R(\theta)` held fixed; by the tower property the same bound holds over all N+M samples. Any estimator parameterisation is allowed; no assumption on the dynamics. Scaling: `\hat k = 0` gives `\le \log(1/\beta)/M` [28, Cor. 3.4]; in general `\hat k/M + O(\sqrt{\log(1/\beta)/M})` ((10)). Experiments: N+M = 3000, `\beta = 10^{-9}`.
- **Check.** Matches PDF pages 2-3 (220 dpi crops), including the open interval (0,1) in Theorem 1 versus (0,1] in Definition 1.
- **Numeric check.** Recomputing Definition 1 with `\beta = 10^{-9}` reproduces printed values: `\hat k`=138, M=1500 -> 0.1437 (printed 0.144); M=10, `\hat k`=0 -> 0.874 (both tables); M=50, `\hat k`=1 -> 0.384; M=1000, `\hat k`=2 -> 0.0263. The `\hat k` values other than 138 are inferred, not printed.

## Tool pitfalls and brief feedback
- The inline Markdown table doubles backslashes in cells, so LaTeX in a table cell comes out broken in `paper.md` (the CSV is fine). Use plain Unicode in cells and give the LaTeX in a note.
- `$$\begin{align} ... \tag{3} \\ ... \tag{4} \end{align}$$` fails the pdflatex check; split a multi-number display into consecutive displays.
- `\mapsto` is "7→" in the PDF text layer: expect a missing "7" (pypdf: "27" when it follows a subscript 2). A stacked `-\frac{1}{2}` exponent is "−1" for pymupdf and "− 1" for pypdf, so the two number checks differ.
- `\theta^*` twice in one paragraph can pair as Markdown emphasis; write `\theta^{\ast}`.
- pypdf/pymupdf are not in the system python. The tool's cached interpreter (`~/.cache/uv/environments-v2/paper-bundle-*/bin/python`) can be called directly to print raw parser text without `uv run`.
- The footnote rule ("end of that page's items") conflicts with `join_previous` when the page's last sentence continues on the next page; the brief could say "after the paragraph carrying the mark" for that case.
- `check_missing.py` flags lines only because of fused math glyphs ("Rnx", "maxx", "supx") or wrap fragments; 15 such lines here, all read individually.
- Page `warnings` keep the extractor's old item ids after a rewrite (advisory only).
- Left on disk: staging builds `staging/dietrich2025data-paper-s1` to `-s4` (s4 is identical to the final package) and my scripts in `logs/work/dietrich2025data/`.
