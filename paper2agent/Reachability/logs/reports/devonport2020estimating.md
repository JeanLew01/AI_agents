# Review report: devonport2020estimating (pilot)

## 1. Result

- Paper: A. Devonport, M. Arcak, "Estimating Reachable Sets with Scenario Optimization", L4DC 2020, PMLR vol. 120, pp. 75-84.
- Source version: the PDF supplied as the PMLR v120 proceedings version, 10 pages, single column (pdfTeX, created 2020-05-01). The PDF itself carries no proceedings banner, running head or page number, so the PMLR provenance could not be confirmed from the file; it is recorded as given in the task.
- No authors' TeX source: all mathematics was transcribed visually.
- Final status: `reviewed_with_limitations`; `verify --strict` exit code 0. The "limitations" are only the 13 adjudicated parser diagnostics; there are no image-only formulas, pages or tables.
- Final package: `/home/jixia/AI_agents/paper2agent/Reachability/skills/devonport2020estimating-paper` (SKILL.md, references/index.md, references/paper.md with 268 lines, references/supplement.md as generated boilerplate, assets/figure/figure-1.jpg, assets/figure/algorithm-1.jpg, assets/table/table-1.csv).
- Review directory: `/home/jixia/AI_agents/paper2agent/Reachability/paper-review/devonport2020estimating-paper`. Scratch (scripts, renders, checks): `/home/jixia/AI_agents/paper2agent/Reachability/logs/work/devonport2020estimating/`. Staging builds s1-s3 were left in `staging/`.

## 2. Counts

| Item | Count |
| --- | --- |
| PDF pages reviewed | 10 of 10 |
| Figures | 1 (Figure 1, three panels in one crop) |
| Tables | 1 (Table 1, as cells, 3 x 6) |
| Algorithms | 1 (Algorithm 1: image crop plus LaTeX transcription) |
| Displayed equations transcribed to LaTeX | 11, tags (1)-(11), all printed |
| Inline math spans | about 210 (94 distinct) |
| Formulas kept as images | 0 |
| Omitted regions | 0 (the PDF has no page furniture) |
| Cross-page joins | 2 (pages 1->2 and 3->4) |
| Adjudications | 13 (page 3: 1; pages 4, 5, 6, 7: 3 each), 0 stale |
| Pages with clean diagnostics | 1, 2, 8, 9, 10 |

## 3. What was corrected

- Headings (all pages): the extractor gave `#` with bold for sections 2, 3, 4, 4.2, 5, 6, Acknowledgments and References, `##` for 4.1, and `###` headings for the two author names. Now one `#` title, `##` sections, `###` for 4.1 and 4.2; authors are text.
- Author block (p. 1): name, e-mail and affiliation merged per author. The underscore lost by the text layer was restored in `ALEX_DEVONPORT@BERKELEY.EDU` (printed in small caps, kept upper case as in the text layer).
- Line-wrap damage: `datadriven` -> `data-driven` (p. 1), `infinitedimensional` -> `infinite-dimensional` (p. 2), `Monte Carlotype` -> `Monte Carlo-type` (p. 8).
- Mathematics (pp. 1-8): every inline expression rewritten in LaTeX. All 11 extractor `formula` images became `$$ ... $$` text items with `\tag`. Four passages that were pure glyph soup were retyped from 260-dpi crops: the sentence after (4), the sample size inside Theorem 2, the `O(1/epsilon)` / `O(log 1/delta)` sentence on p. 6, and the Algorithm 1 body.
- Algorithm 1 (p. 6): the extractor had four text fragments plus a formula image. Now one crop of the whole box (`algorithm-1`) followed by one transcription item. Equation (8) is printed inside the box and lives in the transcription with `\tag{8}`.
- Figure 1 (p. 8): extractor bbox checked on a render with margin and kept; the scattered tick/legend text was dropped after confirming it is visible in the crop.
- Table 1 (p. 8): cells re-entered and compared one by one; header math in LaTeX; the first header cell is empty as printed.
- References (pp. 9-10): all 19 entries read in full. The `- ` bullets were removed. Split diacritics repaired (Ábrahám, Nathanaël, Joël, João, Behçet Açikmeşe). The URL broken after `http:` was rejoined. Three volume/page strings broken across lines were closed up (`7(2):233 – 247`, `60(1):46–58`, `59(8):2258–2263`).
- Theorem labels: bold with the printed punctuation, which is none (`**Theorem 1 (Tempo et al. (2012), Corollary 12.1)**`, `**Theorem 2**`, `**Proof**`). I first added full stops under the old brief wording and changed them after the brief update.

## 4. Limitations and uncertainties

- Misprints of the paper, kept verbatim and listed in the page notes and in "Conversion notes":
  - p. 5, eq. (7): the chance constraint is printed `P_Z(||AZ - b||_p - 1 <= 0) <= 1 - epsilon`. The outer relation is `<=` in both the image and the text layer; (2), (3) and (9) use `>=`.
  - p. 6, Algorithm 1 Output line: `{x : ||Ax + b||_p <= 1}` with a plus sign, against `Ax - b` in (6) and (8).
  - p. 6, Algorithm 1: `from X_0 U, and D` (missing comma).
  - p. 4: `Theta \in R^{n_theta}` (element-of sign); Theorem 1 starts with lower-case `let`; `even when g is a convex`.
- p. 4: in "where e is the Euler number" the e is printed upright, while (5) prints italic e. Written `$\mathrm{e}$` and `e` respectively; this is a font-style reading only.
- Norm delimiters: the PDF typesets `||` in running text and `\|` in Algorithm 1; written `\|` everywhere.
- Theorem statements are printed in italics; the italics are not reproduced. The notes say where each statement ends.
- pp. 9-10: closing up the three line-broken volume/page strings without a space is an inference from the other entries.
- Figure 1 is a vector figure exported at the default 180 dpi (1106 px wide). All tick labels, axis labels, the `x10^-3` exponent and the legend are legible in the JPEG, but small.
- The built `paper.md` has no PDF page markers, so a reader cannot cite PDF pages from the package.

## 5. Self-check

- `paper.md` was read in full. Searches for `<sup>`, `<sub>`, replacement characters, stray accents, ligatures, `_ _`, `** **` found nothing; `$`, braces and `\left`/`\right` are balanced; 13 headings, all real except the generated "Conversion notes".
- All math compiles: 11 displays and 210 inline spans with pdflatex, no errors. The compiled displays were compared by eye with the PDF crops.
- Assets opened: `figure-1.jpg` (three panels, legend, exponent label complete) and `algorithm-1.jpg` (full box, both rules, tag (8)).
- Question: "State the main theorem with all assumptions and the sample-size bound, and the numbers used in the example."
- Answer, from `paper.md` only:
  - Theorem 2 (section "4.1. Unconstrained Norm Balls"): let epsilon, delta in (0,1); let X_0, U, D be random variables over the initial set, input set and disturbance set; let Z = Phi(t_1; t_0, X_0, U, D). With P_S the measure of the multisample of N = ceil( (1/epsilon) (e/(e-1)) (log(1/delta) + n(n+1)/2 + n) ) points, the output (A, b) of Algorithm 1 satisfies P_S( P_Z(R-hat(A,b)) >= 1 - epsilon ) >= 1 - delta (eq. (9)).
  - Algorithm 1 solves the scenario program (8): arg min over (A, b) of -log det A subject to ||A z^(i) - b||_p - 1 <= 0, i = 1..N, with A symmetric (p >= 1 or infinity).
  - The proof uses Theorem 1 (section "3. Scenario Optimization", Tempo et al. (2012), Corollary 12.1): J and g convex, Theta convex and compact, iid samples, N >= (1/epsilon)(e/(e-1))(log(1/delta) + n_theta), a minimizer exists; here n_theta = n(n+1)/2 + n.
  - Diagonal A (section 4.2, eq. (11)): N_diag = ceil((1/epsilon)(e/(e-1))(log(1/delta) + 2n)).
  - Example (section 5): n = 6, p = 2, epsilon = 0.05, delta = 10^-9, N = 1510, N_diag = 1036.
- Check: compared with the 260-dpi crops of PDF pages 4, 5 and 7; identical. Recomputing from the transcribed formulas gives 1510 and 1036.

## 6. Pilot feedback

### Visual transcription of formulas

- Reliability was high. Nothing was uncertain at 260 dpi, so 0 formulas were kept as images. This paper is easy: single column, 10 pt Computer Modern, no long derivations, the largest display is a three-row optimisation problem.
- The 110-dpi previews are fine for prose but not for subscripts. I rendered every page at 170 dpi and math regions at 260 dpi (crops about 1600 px wide).
- Three mechanical cross-checks backed the visual reading, all with plain `python3` on `evidence/page-NNNN.json`, which holds the native text-layer lines with bboxes:
  - `delatex_check.py` maps the LaTeX back to the text-layer glyph order and re-tests every "missing line". Result: 64 of 64 lines matched, so no prose word or symbol letter is missing on the math pages.
  - `symbol_check.py` compares per-page counts of <=, >=, subset, element-of, arrow, infinity, times, =, +, minus and norm bars between text layer and markdown. Result: identical on all 10 pages. This covers what the tool's line check ignores, and it independently confirmed that the `<=` in (7) and the `+ b` in Algorithm 1 are the paper's own.
  - `number_explain.py` attributes every missing/extra number token to a PDF line or a markdown item using the tool's tokenizer.
- Not covered by any mechanical check, eyes only: italic versus calligraphic (X_0 the random variable versus the set), upright versus italic e, subscript versus superscript placement, grouping of fractions and parentheses. For papers with many primes, tildes or nested subscripts I would expect some formulas to need image fallback.
- The three scripts have this paper's paths hard-coded; they would be worth generalising alongside `check_missing.py`, which tests words only.

### Brief: wrong, ambiguous or costly

- Original brief said notes are printed at the top; they go to the end under "## Conversion notes" (now fixed in the brief).
- Label punctuation: the old examples (`**Theorem 1.**`) led me to add full stops the PDF does not print. The updated rule fixes that, but its examples all carry punctuation; add a case with none (`**Theorem 2** Let ...`), which is what jmlr/PMLR style prints.
- Italic theorem bodies: the brief does not say whether to reproduce them. I did not (italics around inline math are fragile) and recorded where each statement ends. A stated convention would help.
- Algorithms without printed line numbers: "numbered lines as printed" does not cover this, nor how to show nesting. I used one paragraph per printed line and `&emsp;&emsp;` for the loop body. Please fix a convention.
- A numbered equation inside an algorithm box: I put it in the algorithm transcription with `\tag{8}` and added a conversion note, because the tags then appear in the order 7, 9, 10, 8, 11.
- Table header cells with math: the brief says "copied exactly", `review-plan.md` says to remove Markdown styling. I used `$...$` in the cells; the line check still passes. Say whether that is wanted.
- References "check a sample": at this length, reading every entry cost about a minute and found three entries with split diacritics. I would say "read every entry" for lists under about 40 entries.
- Line-broken `volume(issue):pages` strings in bibliographies: tell reviewers to close them up without a space and note it.
- "Source version" for PMLR papers: say that such PDFs may have no banner or page numbers, so reviewers do not look for furniture to omit.
- "No `uv run` for your own scripts" arrived after I had run one helper (`pypdf_peek.py`) once with `uv run --offline`. It installed 14 packages from the local cache into a new environment, with no download. It was only needed to see pypdf's text for the second-parser adjudications; the first parser's lines are already in `evidence/*.json`.
- The Build section still says "copy each remaining diagnostic's `adjudication_entry` from the review queue". Once adjudications exist the queue no longer lists those diagnostics, so a script that regenerates `adjudications.json` from the queue produces nothing on a second run. Save a copy of the queue after the first staging build; `review-aid` wipes its directory each run.

### Tool behaviour that surprised me

- Fingerprints depend only on the diagnostic payload: alphanumeric line content and number tokens. Changing punctuation, bold markers, `review_notes`, `plan.json` notes or navigation does not make adjudications stale; a rebuild is still needed because `verify` hashes the review inputs.
- After LaTeX transcription, only lines containing a LaTeX command name go "missing" (`\epsilon`, `\hat`, `\mathbb`, `\frac`, ...). Lines whose math is only letters, digits and sub/superscripts (`$t_0$`, `$z^{(i)}$`, `$O(n^2)$`, `$N = 1510$`) still match, because the check keeps alphanumerics only. Here: 20/41, 12/38, 19/43, 6/24 and 7/43 lines on pages 3-7.
- Number diagnostics here were exactly the harmless patterns: U+2212 versus ASCII minus (`e-1`, `10^{-9}`), `n(n+1)` tokenised as `+1` where the PDF's spaced `n + 1` gives `1`, `$46,052$` versus the PDF's `46, 052`, and the algorithm transcription counted as "extra". The second parser splits `e− 1` differently, so its diff differs from the first.
- A text item may hold several paragraphs and a `$$` block; it is emitted verbatim. That is how the algorithm transcription is one item.
- A new item with no extractor counterpart still needs a `bbox`; I reused the float's box. Text bboxes play no role in exclusion; only figure, formula, omit and image-table boxes hide source lines.
- Assets are JPEG at 180 dpi by default. For vector figures with small labels `--dpi 300` would help; the brief's command uses the default, so I kept it. Worth a coordinator decision.
- I had to delete and rebuild my own final directory twice (a note wording fix, then the label rule). Do the note and wording polish before the final build.

### Timing

- About 25 minutes of work in total, excluding the session restart: reading the contract and the builder source about 5 min, viewing pages and crops about 6 min, writing the page script about 6 min, builds/diagnostics/adjudication/self-check about 8 min.
- `build` takes about 10 s, `review-aid` and `verify` about 3 s each, rendering all pages at 170 dpi about 2 s.

### Tips for editing page JSON

- Do not patch JSON with Edit calls: every LaTeX backslash must be doubled in JSON. Generate the page files from a Python script with raw strings (`write_pages.py`), reading bboxes by item id from a backup of the extractor output made before the first edit. It is re-runnable, survives interruptions, and a wording change is one line plus a re-run.
- Define the recurring symbols once as Python constants (here `\hat{R}_{[t_0,t_1]}` and the ceiling formula for N).
- Keep `review_notes`, plan notes and adjudication reasons in scripts too (`write_plan.py`, `write_adjudications.py`); the adjudication script fails if the queue has a diagnostic without a prepared reason.
- A crop helper taking PDF points (`crop.sh name page x0 y0 x1 y1 dpi`) lets you render exactly the bbox you are about to commit for a figure or algorithm.
