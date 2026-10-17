# nath2026koopman - reviewer report

## Status
- Paper: Devesh Nath, Haoran Yin, Glen Chou (Georgia Tech), "Scalable Data-Driven Reachability Analysis and Control via Koopman Operators with Conformal Coverage Guarantees".
- Source: arXiv:2601.01076v1 [eess.SY], 3 Jan 2026, 28 pages, PMLR/L4DC 2026 single-column style (l4dc2026.cls on jmlr). Main text p1-12 (Sections 1-7), references p12-14 (40 entries), appendix p15-27 (Section 8), p28 blank apart from the running header and page number. The TeX source was used: main.tex and its inputs, symbols.tex, main.bbl.
- The bib key comes from a separate bibliography, not the CoRL one. This is stated in the conversion notes.
- `verify --strict`: exit 0, status `reviewed_with_limitations`, mechanical_ok, 38 adjudications applied, 0 stale, no issues.
- Final package: ~/AI_agents/paper2agent/Reachability/skills/nath2026koopman-paper (19 files). It is not linked into ~/.claude/skills; that is left to accept.sh.
- Staging builds: staging/nath2026koopman-paper-s1 and -s2.
- Scratch: logs/work/nath2026koopman. It holds p01.py-p28.py with pagelib.py, texprep.py (writes full.tex, the macro-expanded and \input-inlined TeX), make_plan.py, make_adjudications.py, the checkers, review-queue-s1/s2.json, and the build/verify logs.

## Counts
- Figures: 12. All are in assets/figure as figure-1 ... figure-12, numbered continuously. Figures 5-12 are appendix figures; this is stated in the notes.
- Tables: 2, both CSV. Table 1 is 11 columns x 5 rows; Table 2 is 3 columns x 11 rows.
- Algorithms: 1. algorithm-1 is an image crop plus a transcription of lines 1-10, with the "//" comments kept.
- Formulas kept as images: 0. The paper.md has 22 display blocks, all compiled with pdflatex without error.
- Omitted regions: 56.
  - p1: the PMLR banner and the arXiv stamp.
  - p2-28: the running header and the page number on each page.
- Adjudications: 38.
  - 16 missing_lines.
  - 11 number_differences.
  - 11 independent_parser_number_differences.

## What was corrected
- **Mathematics.** Glyph soup with `<sup>` and with `~~` for overlines was rewritten from the macro-expanded TeX. In it, \enc=\phi, \dec=\psi, \ka=K_{A}, \kb=K_{B}, \tnfl=\Gamma, \zref/\uref=z^{\text{ref}}/u^{\text{ref}}, \delfz/\delfu, \lqrmat=G, \ncscore=R, \B=\mathcal{B}.
  - 17 extractor formula images were replaced by displays.
  - Tags are as printed: (1a)/(1b), (2)-(14).
  - The side-by-side pairs (3)/(4) and (8)/(9) are each one item, with one block per tag.
  - (14) is one 12-row bmatrix.
- **Structure.**
  - Problems 1 and 2 were merged in the extractor output and have been split.
  - The contribution list, and the Baselines paragraph with its two run-in paragraphs, were also split.
  - The formula boxes on p7 and p8 had swallowed prose; the prose was restored.
  - Heading levels were fixed. The small-caps appendix headings (8.3.1-8.3.9) are written in the TeX's sentence case, keeping the printed number and final period.
  - The 8.3.4 heading had been classed as a caption; it is now a heading.
- **Figures, tables and the algorithm.**
  - Figure 1 had scattered picture text; Figure 2 had been classed as a table with leaked `<latexit>` base64. Both, and Figures 3-12, are now single crops with every label inside.
  - Algorithm 1 was in four fragments and is now one crop plus a transcription.
  - Table 1 cells are rewritten: the extractor had junk such as '99_._0%' and stray 'i'/'l'. Headers are joined, and minus signs are the Unicode minus.
- **Text.**
  - Real compounds broken at line ends were restored: high-dimensional, closed-loop, infinite-dimensional, value-function-based, hyper-rectangular, Swimmer-v5, offline-calibrated, phase-shifted.
  - The underline/contour duplicates were removed ('UnsafeUnsafeUnsafe ...').
  - In the references, `<u>` tags were removed, 'datadriven', 'samplingbased' and 'Cort´es' were repaired, and all 40 entries were checked.
- **Joins and placement.**
  - 10 joins across page breaks (p1-2, 2-3, 3-4, 4-5, 6-7, 8-9, 9-10, 11-12, 19-20, 20-21).
  - The formula split at the p3/p4 break was completed on p3.
  - The copyright line was placed after the author block so that the p1 join works.
  - Within-page reordering on p7 (Figure 2), p10 (Figure 3, Table 1) and p21.
  - reading_order moves Figure 7 into 8.3.5, Figure 8 into 8.3.6, Figures 9-10 into 8.3.7, Figure 11 into 8.3.8, Figure 12 into 8.3.9, and Algorithm 1 back into 8.2. Algorithm 1 is printed on p17 under the heading 8.3.

## Checks (all scripts are in scratch)
- texcompare.py: 471 math snippets checked. All are identical to full.tex except the author marks: TeX `$^{*1}$`, written `$^{\ast 1}$`.
- prosecompare.py: every prose run that does not match is explained by the following:
  - natbib citations;
  - \paragraph/\looseness boundaries;
  - theorem optional arguments, which the regex removes;
  - \underline{Sca}lable;
  - \Comment lines in the algorithm;
  - bibliography entries, which are not in the TeX.
- linecheck.py: 350 missing lines in total. The 13 unmatched ones are subscript glyph orders ('KAzref', 'emax', 'xref,(0)') and the \sin/\cos/\tan rows of (14).
- wordcheck.py: no prose word lost. The differences are running headers, figure-internal text (including the latexit base64 on p7), contour duplicates, and math glyph runs.
- symbol_check2.py: every difference is explained by \doteq (printed '.='), \rightarrow vs \to, \Vert, \cdots, the phi^infty formula moved from p4 to p3, and figure-internal glyphs.
- mathcheck.py: 22 displays and 288 unique inline snippets compile with no errors.
- Number diagnostics are explained token by token:
  - Unicode minus vs ASCII hyphen.
  - '(T + 1)' and 'K^cal + 1' spacing.
  - 10^6/10^7 printed flat.
  - The Table 1 columns merged by pypdf: 3100, 6100, 12200, 11225, 28400.
  - The algorithm transcription's tokens equal the p17 extras exactly.

## Limitations and uncertainties (page numbers)
- **Typography not reproduced** (stated in the notes):
  - p9-10: the underlined italic run-ins are written in italics only.
  - p2: the underlined letters spelling ScaRe-Kro are written plain.
  - p12-14: the underlined venue names are written plain.
  - p1: the small-caps e-mails are written in lower case.
- **p1 Figure 1.** The caption refers to (a)/(b), but no letters are printed. From the content, (a) is the swimmer (top) and (b) the hopper (bottom); this is stated in the notes.
- **p27 Figure 12.** The tick labels are about 3 pt and only marginally legible in the JPEG; the panel names are legible. Curve values in Figures 3-12 were not digitised. The decisive in-figure values of Figure 3 and the 'CKRS (99.0%)' legends are copied into the notes.
- **p8, p15 equation numbers.** The CKRS display is (10) in 5.4 and (11) in the 8.1 restatement, and the text cites "(11)" three times. All are kept as printed; the cause is a duplicate TeX label.
- **Source slips kept as printed** (in the notes and the page notes):
  - p4: "We are a planner P"; the lifting function called "g"; the extra closing brace in the exact reachable set.
  - p5: the missing ")" in Problem 1's dataset; "space.The".
  - p6: "a CG the describes"; "costs that increases"; z_{0:T} = {z_0, z_2, ..., z_T}.
  - p7: Lemma 1's X-hat_t without overline (also on p15).
  - p8: the unclosed "f(" in (9); "K^cal + M" for M^λ; "(8) and (9), respectively" with the order swapped; "via (7))".
  - p10: "SCaRe-Kro".
  - p12: "13-link MuJoCo swimmer".
  - p16: 8.2 writes the KRS without hat and the CKRS without overline; "the the".
  - p18: row 8 of (14), "cos ϕ · sin ϕ".
  - p19: "Figure 6 illustrate".
  - p20: "with with".
  - p24: Figure 9's caption says "a different reference trajectory", singular.
- **Second check.** No independent second verifier was used; this was one reviewer.

## Self-check
- SKILL.md and index.md were read. Navigation has 27 rows, including level-4 headings and "Conversion notes"; all resolved.
- The damage scan of the final paper.md found no `<sup>`, `<u>`, `~~`, `^*` or replacement characters. The `$` count is balanced. The only underscores outside math are inside words in the notes.
- figure-12.jpg (smallest labels) and algorithm-1.jpg were opened: both complete and legible. Both CSVs were read.
- **Question:** "State Theorem 1 with its hypotheses and explain how the bounds ē_{t,j} are built."
- **Answer** (paper.md 5.4 and 8.1):
  - **Calibration data.** K^cal pairs: the true closed-loop rollout (9) and the decoded Koopman rollout (8). The errors are e_{t,j}^(i) = x_{t,j}^(i) − x̂_{t,j}^(i).
  - **Score.** R^(i) = max_{t,j} λ_{t,j}|e_{t,j}^(i)|, with λ_{t,j} ≐ 1/(e^max_{t,j} + σ). e^max comes from a separate normalisation set D_N of M^λ trajectories.
  - **Quantile.** C = Quantile_{1−δ}({R^(i)} ∪ {∞}), the p-th smallest score with p ≡ ⌈(K^cal + 1)(1 − δ)⌉.
  - **Bounds.** ē_{t,j} = C/λ_{t,j}, so that P(|e_{t,j}^(0)| ≤ ē_{t,j} ∀t,j) ≥ 1 − δ.
  - **Theorem 1.** With the KRS from (7), CKRS = {X̂̄_t ⊕ diag(ē_t) B_1(0)}_{t=0}^T (10). For a new reference drawn from the same distribution, P(∧_t x_t^(0) ∈ X̄_t^{1−δ}) ≥ 1 − δ.
  - **Proof (8.1), three steps:**
    1. Lemma 1: deterministic containment via the auto_LiRPA bounds of Proposition 1.
    2. Exchangeability, argued for calibration and test trajectories that share the same reference and gains G_t, with x_0^(i) i.i.d. from B_ε(x_0^ref).
    3. Interval arithmetic.
  - **Offline calibration.** The case of a random reference is argued in the Offline Calibration paragraph: the pairs (x^{ref,(i)}, x_0^(i)) are i.i.d.
  - **Check.** Compared with the 230 dpi crop of PDF page 8 (quantile paragraph and Theorem 1), the 250 dpi crop of the normalisation paragraph, the 220 dpi crop of page 15 and the 170 dpi render of page 16: identical.

## Tool pitfalls / brief improvements
- **Multi-file TeX.** For sources split over \input files, inline them and expand the macros once into one file (texprep.py → full.tex). texcompare/prosecompare then run on that file unchanged.
- **Placing floats.** A float printed under the next heading (Algorithm 1 under 8.3) is not flagged by any join diagnostic; I found it only by reading paper.md. After the first staging build, check each float's section against its \begin{figure}/\begin{algorithm} position in the TeX.
- **Author-year citations.** With natbib author-year citations, prosecompare needs the markdown citations stripped, e.g. `\((...)\d{4}\)` and "Name et al. (2020)". Its `\begin{env}[...]` regex also removes theorem labels; both produce expected misses.
- **contour/ulem underlines.** These draw each run-in title 16 times in the text layer, and the extractor repeats the words three times. This is harmless for the checks, but the extractor text cannot be reused for those items.
- **PDF figures with LaTeX labels.** These leak `<latexit>` base64 into the extractor item and into pdftotext. The extractor may also class such a figure as a table.
- **Duplicate theorem restatements.** A restatement that shares the original's \label shifts every \eqref to the restated tag. Keep the citations as printed, and say so in the notes and in the navigation purpose.
- **Escapes in non-raw strings.** In page scripts, `"\;"` inside non-raw Python strings gives SyntaxWarnings (harmless). Use raw strings for displays as well.
