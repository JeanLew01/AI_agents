# Report: hewing2019scenario

## Result

- Paper: L. Hewing, M. N. Zeilinger, "Scenario-based Probabilistic Reachable Sets for Recursively Feasible Stochastic Model Predictive Control" (IEEE Control Systems Letters 4(2), 2020; online 2019).
- Source version: accepted version from the ETH Research Collection, doi:10.3929/ethz-b-000389523. 7 PDF pages: page 1 is the ETH Library cover sheet, pages 2-7 are the paper (IEEE two-column). No authors' TeX source.
- Final status: `reviewed_with_limitations`, `verify --strict` exit code 0 (18 adjudications applied, 0 stale, `mechanical_ok: true`).
- Final package: `/home/jixia/AI_agents/paper2agent/Reachability/skills/hewing2019scenario-paper` (`SKILL.md`, `references/index.md`, `references/paper.md`, `references/supplement.md` (empty boilerplate), `assets/figure/figure-1.jpg`, `assets/figure/figure-2.jpg`, `assets/table/table-1.csv`).
- Review directory: `/home/jixia/AI_agents/paper2agent/Reachability/paper-review/hewing2019scenario-paper`; scratch (scripts, renders, queue copies, `verify-strict.out`): `/home/jixia/AI_agents/paper2agent/Reachability/logs/work/hewing2019scenario/`.
- Staging builds `staging/hewing2019scenario-paper-s1 ... -s4` are left in place; `s4` is byte-identical to the final `paper.md`/`index.md`. `s1` is obsolete (it still used `align` blocks).

## Counts

| Item | Count |
| --- | --- |
| Figures (image crops with verbatim captions) | 2 (Fig. 1 crane sketch, Fig. 2 simulation plots) |
| Tables | 1 (Table I, transcribed as CSV cells, 3 columns x 4 rows incl. header) |
| Algorithms | 0 (the paper has none) |
| Formulas kept as images | 0 |
| Display formulas in LaTeX | 42 `$$` blocks: 34 with printed tags (1)-(17b), 8 unnumbered |
| Omitted regions | 1 (ETH Zürich logo on the cover sheet) |
| Adjudications | 18 (page 1: 2; page 2: 1; pages 3-7: 3 each) |
| Navigation entries | 23 |

## What was corrected

- **Mathematics (pages 2-7).** All 40 extractor `formula` image items and all inline glyph-soup math were replaced by LaTeX transcribed visually from 200 dpi page renders, 300 dpi column crops and 500 dpi zooms ((15a)/(15b), Corollary 3, Table I, appendix equation). Every symbol was legible; nothing had to stay an image. The worst extraction damage was in both proofs on page 5, the conditional density p(W_k) on page 4, the MPC problem (11a)-(11g) on page 4 and the fractions d = (n^2+n)/2 on page 6.
- **Reading order.** Two-column order repaired on every page. Page 6 had the right column interleaved into the left. Paragraphs split by a column break were merged (pages 2, 3, 6). Sentences running over page breaks are joined (2→3, 4→5, 5→6, 6→7).
- **Floats.** Fig. 1 (top of page 6, inside a sentence from page 5) is placed at the end of the Section V introduction. Fig. 2 (bottom of page 6) and Table I (top of page 7) sit inside one sentence of Section V-A; both now follow that paragraph, before "B. Results". Fig. 2 is moved across the page break with `reading_order`.
- **Headings.** Extractor had every subsection as `#` and one body sentence as a heading; now `##` for sections I-VI, Acknowledgments, Appendix, References and `###` for subsections. One `#` title (page 2).
- **Theorem-like blocks.** Bold printed labels for Definitions 1-2, Assumptions 1-4, Theorems 1-3, Corollaries 1-3, Remarks 1-7 and two Proofs. Italic statement bodies are not reproduced; where each statement ends is recorded in the conversion notes.
- **Text damage.** Line-wrap hyphens repaired, real compounds kept (`tube-based`, `closed-loop`, `time-varying`, `run-time`, `Constraint-Tightening`, `Discrete-time`); `Allg¨ower` → `Allgöwer`; `<sup>`/`<u>` tags, replacement characters and stray emphasis removed.
- **References.** All 16 entries read against the render, one item per entry.
- **Cover sheet (page 1).** Kept as plain text under `## Repository cover sheet (ETH Research Collection)`, placed after the title, author line and first-page footnote, before the abstract.

## Checks run

- `verify --strict`: exit 0, `reviewed_with_limitations`.
- Every missing line and every number difference was traced to a PDF line. All are math-notation differences: Unicode vs ASCII minus, `\%` in math, flattened exponents such as `0.022` for 0.02², and kerned table decimals split by the second parser (`99 .98%`, confirmed in its raw text).
- pdflatex compile of all 42 display and 318 inline formulas of the final `paper.md`: no errors. The compiled displays were compared visually with the PDF.
- `symbol_check.py` (adapted, extended symbol list): per-page counts of ≤, ≥, ⊆, ⊂, ∈, →, ⇒, ∞, ×, =, +, −, >, ≪, ‖, ⊖, ∀, ∼, ≈, ±, *, tildes, bars, δ, β, α, θ, π, % agree between PDF text layer and markdown on pages 2-7. The only flagged item is a counting artefact for the two `\ddot` in the appendix.
- `wordcheck.py` (own script): word multiset of each page against `pdftotext`; no prose word lost.
- Recomputing printed numbers from the transcribed bounds: (7) with p = 0.9, N_s = 10000, d = 1, β = 1e-7 gives N_k ≤ 820.46 (paper: 820). (8) with N_s = 10000, β = 1e-7, d = 4 gives p ≥ 99.636 % (paper: 99.6 %).
- Leftover-damage search (`<sup>`, `�`, ` ˆ`, `_ _`, `** **`, `¯`, `˜`, `∗`, ligatures, `\!`, `~~`): no hits. `$` count is even. Exactly one `#` heading.
- Both figure assets and the table CSV opened; all panels, axis and tick labels are complete and legible.

## Limitations and things kept as printed

Nothing in a formula is uncertain. Items a reader should know:

- **Added, non-printed text** (all labelled): the cover-sheet heading; a `## Abstract` heading; the prefix "Footnote (unnumbered, first page):"; a conversion note listing the four cover-sheet hyperlink targets from the PDF link annotations (page 1); a conversion note under Table I giving the printed LaTeX form of the Constraint column (page 7).
- **Footnote position (page 2).** The unnumbered first-page footnote (funding, affiliation, e-mail) is placed after the author line, not at the end of the page's items, because it would otherwise split the sentence that continues on page 3.
- **Table I cells (page 7)** hold the constraints in plain characters (`[|p|; |v|] ≤ [p_max; v_max]`, `θ ≤ θ_max`, `θ ≥ −θ_max`); the first is printed as two stacked column vectors.
- **Multi-line numbered displays** are written as one `$$` block per printed tag (no vertical alignment), so that each block is valid LaTeX.
- **Authors' slips kept verbatim** and listed in the conversion notes:
  - page 3: `{1, … n_c}` in (2a) without a comma; `(see [9].` unclosed.
  - page 4: Z_∞ is an intersection from k = 1, while Remark 3 says k = 0, …, N̄.
  - page 5: `{v_0^*, … v_{N-1}^*}` without a comma; "v_i^* ∈ V for all 1 ≤ i ≤ N"; W^{(i)} ∼ calligraphic W (Section II uses Q); W^{(i)} runs to N̄−1 but E^{(i)} to N̄; "Assumption (1)"; "discard the k samples".
  - page 6: "Figure (1)"; "the sliders position"; `P > 0` in (15a) (plain greater-than at 500 dpi); `P^{*-1}` in Corollary 3 while (15b) uses P; undefined I_dis in Remark 7; `p_{ref}` in the Fig. 2 caption.
  - page 7: "remove k = 820 samples"; R_k^{θ_min} vs ±θ_max in Table I; d_p in the appendix equation vs "damping d_m = 10" in the text.
  - page 2: grant number printed "PP00P2 157601 / 1". Page 1: permanent link printed with a doubled `https://doi.org/` prefix; funding entry ends with `()`.
- **Title capitalisation.** The paper's own title prints "Scenario-based"; the cover sheet and IEEE record print "Scenario-Based". The `#` heading and the bundle/plan `title` use the page-2 form (I changed the top-level bundle title from "Scenario-Based" accordingly).
- **Single reviewer.** No independent second verifier was used.
- **Process deviations.** I did not back up the extractor page JSON before the first overwrite (that rule arrived later); a text dump of the extractor items of pages 2-7 is in scratch (`extractor-output-dump-pages2-7.txt`), page 1's original is not saved. I used `uv run --with pymupdf` once, before the "no `uv run` for own scripts" rule, to read the link annotations.

## Self-check question

**Question.** How does the paper certify a scenario-built set as a probabilistic reachable set: state the scenario theorem with its assumption, the exact conditions on the number of samples and discarded samples, and the corollaries that turn it into k-step PRS, with the numbers used in the example.

**Answer (from the package only).**

- Section II-C considers min_{x ∈ X ⊆ R^d} c^T x s.t. Pr(x ∈ X_δ) ≥ p (4), with X_δ convex and closed for each realization of δ and d the dimension of x. It is replaced by the sampled program (5) over an index set I_s with |I_s| = N_s − N_k, i.e. N_k of N_s samples discarded.
- Assumption 1 ([9]): constraints are discarded such that the optimal solution x* of (5) violates all discarded constraints.
- Theorem 1 ([9]): if binom(N_k+d−1, N_k) · Σ_{i=0}^{N_k+d−1} binom(N_s, i) (1−p)^i p^{N_s−i} ≤ β (6), then x* of (5) is feasible for (4) with probability 1 − β.
- Sufficient condition for (6): N_k ≤ (1−p)N_s − d + 1 − sqrt(2(1−p)N_s ln(((1−p)N_s)^{d−1}/β)) (7).
- Without discarding (N_k = 0): N_s ≥ (2/(1−p)) ((d−1) ln 2 − ln β) (8).
- PRS (Section IV): with N_s, N_k satisfying (6), with probability 1 − β the set is a k-step PRS of probability p for the error system (3b) initialized at e(0) = 0, where
  - Corollary 1: α*·R̃ from the scaling problem (13), d = 1;
  - Corollary 2: {e | He ≤ b*} from (14), d = n_hs;
  - Corollary 3: the ellipsoid from (15), d = (n²+n)/2 + n (Remark 6: d = (n²+n)/2 with fixed centre).
- Remark 4: Assumption 3 and Theorem 3 then hold with probability 1 − β.
- Example (Section V-A): N_s = 10000; boxes with no sample removed give p_1 = 99.6 % with 1 − β ≈ 1 − 10^{-7} by (8); half-spaces with k = 820 samples removed give p_2 = 90 % with β = 10^{-7} by (7).

**Where it came from.** `references/paper.md`, headings "C. Scenario Optimization", "IV. Probabilistic Reachable Sets using Scenario Optimization" with its subsections A-C, and "A. Simulation Setup". Checked against the 300 dpi crops of PDF pages 3, 5, 6 and 7; the statements match, and (7) and (8) reproduce 820 and 99.6 %.

## Tool pitfalls and brief feedback

- **`align` inside `$$`.** `$$\begin{align} … \tag{2a} \\ … \tag{2b} \end{align}$$` fails the coordinator's `mathcheck.py` (amsmath "Erroneous nesting", because the script wraps displays in `\[ … \]`). The brief should say how to write multi-line displays with several printed tags. I used one `$$ … \tag{n}$$` block per printed number, kept together in one item.
- **Backslashes in table cells.** The builder's `table_markdown` doubles every backslash, so `$\theta$` in a cell appears as `$\\theta$` in `paper.md` (the CSV is fine). The brief's new line "Table cells may contain `$...$` math" should mention this.
- **Cover-sheet PDFs.** The rule "first non-omitted item of page 1 is exactly `# <title>`" cannot hold when page 1 is a repository cover sheet. What works: `reading_order` puts the page-2 title first; the builder then finds the `#` heading at the start of the text. The title comparison is on casefolded alphanumerics, so capitalisation differences do not duplicate the title. Automatic title omission only looks at page-1 headings whose top is ≤ 130 pt.
- **`join_previous` with `reading_order`.** It is applied in reading order, not page order. So "the continuing item must be the first non-omitted item of its page" is only the rule without `reading_order`; with it, a float at the bottom of the previous page can simply be listed after the joined paragraph.
- **Footnote rule vs. cross-page sentences.** "Footnotes at the end of that page's items" breaks a sentence that continues on the next page. The brief should say where such a footnote goes.
- **`check_missing.py`** reports many false positives on math-heavy pages (glyph words like `rnu`, `xref`, and halves of hyphenated words). A plain word-multiset comparison against `pdftotext` (`wordcheck.py` in my scratch) was more decisive.
- **Percent signs.** `90\%` inside math is read as `90` by the number check. Standalone percentages in prose are better written as plain text so they stay searchable.
- **Second-parser raw text.** `pypdf` is not in the system Python. Running the cached tool interpreter directly (`~/.cache/uv/environments-v2/paper-bundle-*/bin/python`) gives its raw text without building a new environment.
- **Link annotations.** Repository cover sheets carry link targets (ORCID, rights statement) that are not visible text; the brief does not say whether to keep them. I kept them in a labelled note, which costs two extra adjudications on page 1.
