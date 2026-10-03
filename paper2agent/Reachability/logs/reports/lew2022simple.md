# Report: lew2022simple

**Paper**: Lew, Janson, Bonalli, Pavone, "A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis" (L4DC 2022).
**Source**: arXiv:2112.05745v3 [eess.SY], 13 Apr 2022; 25 pages, single column (main text p. 1-10, references p. 11-14, Appendices A-E with all proofs p. 15-25). Authors' TeX used.
**Result**: `verify --strict` exit 0, status `reviewed_with_limitations` (the only "limitations" are the 42 adjudicated parser diagnostics).
**Package**: `~/AI_agents/paper2agent/Reachability/skills/lew2022simple-paper` (staging builds s1-s3 kept in `staging/`).

## Counts
- Figures: 8 image crops. Figures 1-6 in `assets/figure/`; appendix Figures 7-8 in `assets/supp_figs/` as `supplementary-figure-7`/`-8` (printed numbers kept in label and file name).
- Tables: 0. Algorithm boxes: 0 (the paper has none; the two enumerated procedures of App. D and E.1 are numbered lists).
- Formulas kept as images: 0. 45 `$$` displays; 11 printed tags: (1)-(3), (4a), (4b), (5)-(8), (C1), (C2).
- Omitted regions: 49 (arXiv stamp p. 1; running header and page number on p. 2-25).
- Adjudications: 42 (22 missing_lines, 10 number_differences, 10 independent-parser), all applied, none stale.

## What was corrected
- All 25 pages rewritten from the TeX with macros expanded, then checked against 150 dpi renders; every theorem-like statement in the main text and every proof page (p. 15-25) also on 220-260 dpi crops. The 40 extractor formula images and several glyph-soup displays became LaTeX.
- Theorem-like blocks with printed bold labels and printed punctuation: Assumptions 1-5, Theorem 1 (Asymptotic Convergence), Theorem 2 (Finite-Sample Bound), Corollary 1 (p. 4-7); Definition 1, Theorem 3, Lemmas 2-7, Remark, all proofs (p. 15-24). The paper has no Lemma 1. Assumption 1, Theorems 1-2 and Corollary 1 appear twice (Sections 4-5 and restated in App. B); the App. B restatements of Theorem 2 and Corollary 1 give two separate probability bounds.
- TeX/PDF differences, PDF followed: `\vec{r}` is printed as bold r (jmlr class), written `\boldsymbol{r}` (p. 7, 22, 24); step labels "(C1):", "(C2):" are printed in normal weight although the source wraps them in `\textbf` (p. 16-17).
- Figures: extractor crop of Figure 2 covered only the upper half (p. 6); my first Figure 6 crop cut the x tick labels (p. 10); both fixed. All eight crops checked on padded renders. Wrapped/top floats moved to paragraph boundaries (listed in the conversion notes).
- Cross-page joins on p. 2, 3, 4, 5, 9, 10, 18, 25. Two formulas split by a page break are written whole on the earlier page ($x_t\in\mathbb{R}^6$ p. 9/10; the set $\mathcal{X}_0$ p. 24/25).
- References: 50 unnumbered author-year entries generated from the .bbl, each compared with the page image (p. 11-14).
- Heading levels, author block, line-wrap hyphens, accents, small-caps names (RandUP, ReachLP, ReachSDP, GoTube).

## Limitations and deviations
- Footnotes: 5, 6, 8 stand at the bottom of their page. Footnote 1 (p. 8) is moved after its completed paragraph with `reading_order` (the later "Lessons" rule would put it before that paragraph). Footnotes 2 (p. 9) and 7 (p. 19) sit at the end of their subsection because the page's last sentence continues. Footnotes 3-4 (p. 16) are placed at the end of Section A.2, which carries their marks, not inside the proof of Theorem 1 where the page prints them. Marks are written `$^{n}$`.
- Full pages were rendered at 150 dpi, not the 170 dpi the brief asks for; all math regions were read on 220-260 dpi crops.
- 23 printed slips are kept verbatim and listed in the conversion notes and page notes, e.g. "$d$-packing number" before Theorem 2, missing hats after Theorem 1 and in Theorem 3's conclusion, "$c_1$" used twice and mixed $p$/$n$ in App. C, an unbalanced parenthesis in $p_0^\alpha$ (App. E.1).
- One reviewer, no independent second verifier. No symbol remained uncertain after zooming.

## Checks beyond the tool
- `symcheck.py` (adapted symbol_check2): per-page counts of relations, operators, hats, bars and Greek letters agree between PDF text layer and LaTeX on all pages, apart from glyph-encoding effects (each one traced).
- `wordcheck.py`: no prose word lost on any page. `mathcheck.py`: all 45 displays and 431 distinct inline formulas compile with pdflatex.
- Every number difference traced to its cause (Unicode minus, flattened superscripts, the two page-split formulas, "Definition 1" + footnote mark 4 read as "14", maps-to arrow read as "7").
- Printed sample size recomputed from the transcribed App. E.2 formula: 1375.6, printed 1376.

## Self-check
- `paper.md` (781 lines) searched for `<sup>`, replacement characters, stray accents, ligatures, `~~`, glyph soup, unbalanced `$`: none. Headings are the title, the 28 real section headings and "Conversion notes".
- Opened `figure-5.jpg` (smallest labels) and `figure-2.jpg`: complete and legible.
- Question: "State the finite-sample theorem with its assumptions and probability bound." Answer from `paper.md`, Section 5.1: Assumption 2 ($f$ is $L$-Lipschitz on $\mathcal{X}$); Assumption 3 (for given $\epsilon,L>0$ there is $\Lambda^L_\epsilon>0$ with $\mathbb{P}_\mathcal{X}(B(x,\epsilon/(2L)))\geq\Lambda^L_\epsilon$ for all $x\in\partial\mathcal{X}$); additionally $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$. With $\hat{\mathcal{Y}}^M=\mathrm{H}(\{y_i\}_{i=1}^M)$ and $\delta_M=D(\partial\mathcal{X},\epsilon/(2L))(1-\Lambda^L_\epsilon)^M$: with probability at least $1-\delta_M$, $d_H(\hat{\mathcal{Y}}^M,\mathrm{H}(\mathcal{Y}))\leq\epsilon$ and $\mathcal{Y}\subseteq\hat{\mathcal{Y}}^M_\epsilon$. Matches a 230 dpi crop of PDF page 6.

## Tool pitfalls / brief feedback
- `uv run ... verify --strict | tail; echo $?` reports the exit code of `tail`; redirect to a file instead.
- A footnote mark directly after inline math (`$...$$^3$`) creates a `$$`; put a space before the mark.
- "Footnote where the page prints it" puts a footnote into the wrong section when a new section starts above it on the same page; "end of the paragraph or subsection that carries the mark" would be a better rule.
- Class files can change what a macro prints (`\vec` bold in jmlr; `\eqref` ignores `\textbf`); the TeX alone is not enough for accents and weights.
- For symbol_check2, extend the regexes to `\leq`, `\geq`, `\neq`, `\rightarrow`, `\gets`, `\implies`, and exclude text-layer lines inside figure boxes.
- The session was killed once by the out-of-memory restart; writing one script per page made the resume immediate.
