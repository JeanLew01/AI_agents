# tebjou2023data - reviewer report

**Paper**: Tebjou, Frehse, Chamroukhi, "Data-driven Reachability using Christoffel Functions and Conformal Prediction" (COPA 2023).
**Source version**: PMLR v204 proceedings PDF, 20 pages, single column (banner "204:1-20, 2023"; volume pagination 194-213 is not printed).
**Status**: `verify --strict` -> `reviewed_with_limitations`, exit 0; 20/20 pages reviewed, 40 adjudications applied, 0 stale.
**Package**: `~/AI_agents/paper2agent/Reachability/skills/tebjou2023data-paper` (staging builds `-s1`, `-s2`; final rebuilt after the post-verification repair and identical to `-s2`).
The run was interrupted once by the machine restart; pages 1-14 were on disk and were kept, pages 15-20 were done after resuming.

## Counts
- Figures 9 (one crop per figure, sub-captions inside the crop and repeated in the caption), tables 2 (CSV + Markdown), algorithms 2 (crop + transcription).
- Displays 39 in LaTeX, printed numbers (1)-(14) as `\tag`; formulas kept as images: 0 (the extractor's 41 formula images were all replaced).
- Omitted regions 39: proceedings banner (p. 1), 19 running headers, 19 page numbers.
- Adjudications 40: 14 missing_lines, 12 number_differences, 14 independent_parser_number_differences.

## What was corrected
- All math rewritten from the arXiv TeX (jmlr macros expanded) and checked on 230-260 dpi crops; pdflatex compiles all 39 displays and 362 inline formulas.
- Theorem-like labels as printed (bold, no punctuation): Conjecture 1, Theorems 2-5, Examples 1-4, three proofs.
- Sentences split by floats re-joined with `reading_order` (pp. 9-11 Example 2; pp. 15-18 last two paragraphs of Section 5.1); 9 joins across pages or moved floats.
- Extraction damage: garbled proof lines (p. 9, p. 13), fragmented algorithm boxes (pp. 10, 15), split diacritics and broken volume/DOI strings in the references (pp. 19-20), `<u>` tags from underlined emphasis.
- Checks beyond the tool: symbol counts PDF vs LaTeX (0 differences on all 20 pages), word-multiset vs pdftotext (only furniture and math tokens differ), number tokens of transcriptions and sub-captions equal the "extra" sets exactly.

## Limitations and uncertainties
- The TeX source is arXiv v1, not the source of the PMLR PDF. Differences found: p. 3 prints `f : R^n -> R^n,` as a display (running text in the TeX); label style (bold, no colon, italic bodies) and float placement differ. Wording and formulas otherwise agree. PDF followed.
- Reading order is not page order: Figure 1 (p. 7) after Example 1; Algorithm 1 (p. 10) before Example 2; Figures 2-3 after Example 2; Figure 4 (p. 12), Figure 5 (p. 14) after their examples; Algorithm 2 (p. 15) at the end of Section 4; Table 2 and Figure 6 (p. 16), Figures 7-8 (p. 17), Figure 9 (p. 18) moved to where they are discussed. Footnote 1 (p. 4) sits after equation (1); the copyright line (p. 1) after the editor line.
- Not reproduced typographically: italic theorem bodies (block ends are listed in the conversion notes); underlined emphasis is written in italics; slanted fractions are written 1/2 (p. 9) and 1/N (p. 10); "N = 10 000" is written 10000 (p. 6).
- Table 1 (p. 14): merged header "confidence in %" repeated in the column names. Table 2 (p. 16): |D| columns are blank or vertical dots as printed, not forward-filled; calligraphic D written as plain D.
- Authors' slips kept and listed in the notes: "Table 4" for Table 1 (p. 13), "Figure 9" for Figures 7-8 (p. 16), `n -> infinity` for N (p. 6), `b_n` next to `b_N` (p. 8), `U_N` without parentheses (pp. 8-9), "oulier", `V_i` (p. 13), "otherwise. ." (p. 15).
- Source inconsistency found by recomputation (recorded as a reviewer note, nothing changed): Table 1 is not reproduced by (14) as printed (sum from i = p+1 gives 18.1/33.9/50.9/92.2 for N = 100); the printed entries equal the same sum started at i = p, truncated. Example 4's 98.9% does match (14) as printed.
- Tick labels inside the raster plots are very small in the PDF itself (Figures 1-3, 9); they are complete but only just legible in the JPEGs.
- One reviewer, no independent second verifier.

## Self-check
Question: how is the Christoffel threshold calibrated, what coverage is guaranteed under which assumptions, and how does it compare with the bound of Devonport et al.?
Answer from the package (Section 3.1: Algorithm 1, Theorem 4; Section 2.3: Conjecture 1): the M i.i.d. samples are split; the M-N training points give the empirical moment matrix, hence the Christoffel polynomial used as nonconformity score; the threshold is alpha = max over the N calibration points of v_d(x^i)^T M-hat_d^{-1} v_d(x^i), and the returned set is the conformal region of level 1/N. Theorem 4: if r is continuous, for all delta in (0,1), P[mu(C) >= exp(log(delta)/N)] >= 1-delta (10), i.e. coverage error epsilon = 1 - delta^(1/N); if mu is also continuous, P[exp(log(1-delta)/N) >= mu(C)] >= 1-delta (11); both hold with probability >= 1-2 delta for delta in (0,1/2) (12). The bound depends only on delta and N, not on n or d. Devonport et al. need N >= (5/epsilon)(log(4/delta) + binom(n+2d,n) log(40/epsilon)); the authors restate it as "Conjecture 1" because the same points build the polynomial and the threshold. Checked against PDF pp. 5, 9, 10: matches. Numerically, delta = 0.01 gives 0.0023 (N = 2000) against 0.085-0.9 for N = 10000 in Figure 1.

## New pitfalls (not yet in the brief)
- siunitx table columns: pypdf extracts the decimal point as a separate chunk ("99 .99", "0 .2 49 .5"), so a correct table yields dozens of second-parser number differences (50 missing / 25 extra on p. 16) while the first parser shows none.
- With an arXiv TeX for a proceedings PDF, do not take label punctuation or body style from the TeX preamble (here small caps with colon, upright); the proceedings class prints them differently. A symbol count plus word-multiset check establishes quickly that wording and formulas agree.
- An algorithm2e comment marker `#` at the start of a transcription line becomes a Markdown heading; write it as a code span.
- `\emph` printed as underline (ulem) reaches the extractor as `<u>` tags that also split words ("<u>(without</u> outliers"); a search for `<u>` belongs in the damage scan.
- Fingerprints are unchanged between a staging build and the final build when no page file changes, so adjudications can be generated from the saved staging queue and no second staging build is needed.
- Recomputing a printed table from the transcribed bound can expose an inconsistency in the source itself; it should go into the conversion notes as a reviewer note, not be "fixed".

## Post-verification repair
An independent verifier found the paper text, formulas, tables and figures correct and two slips in my conversion notes (`logs/verify/tebjou2023data.md`). Only the notes in `make_plan.py` were changed; no page file, table or formula was touched, so all 40 adjudication fingerprints still apply.
- Note 2: the arXiv TeX does not have the transition function "only in running text"; it has no formula for f at that place. Reworded ("the arXiv TeX has no formula for f at that place"), and "No difference" became "No other difference".
- Note 8: the recomputed value of (14) for N = 100, epsilon = 10% is 92.2496, i.e. 92.2, not 92.3. Corrected (all other values of that note were recomputed and stand).
- Rebuilt: staging `-s2` (differs from `-s1` only in these two notes lines; assets and index identical; pdflatex check clean), final package deleted and rebuilt. `verify --strict`: exit 0, status `reviewed_with_limitations`, 40 adjudications applied, 0 stale, 13 asset checks true.
