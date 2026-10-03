# dietrich2024nonconvex - reviewer report

**Paper:** Dietrich, Devonport, Arcak, "Nonconvex Scenario Optimization for Data-Driven Reachability" (L4DC 2024).
**Source version:** PMLR v242 proceedings PDF (pp. 514-527), 14 pages, single column. No TeX source: all mathematics transcribed visually.
**Status:** `verify --strict` exit 0, status `reviewed_with_limitations`, 23 adjudications applied, 0 stale, mechanical_ok.
**Package:** `~/AI_agents/paper2agent/Reachability/skills/dietrich2024nonconvex-paper` (staging: `-s1`, `-s2`; scripts and crops in `logs/work/dietrich2024nonconvex/`).

## Counts
- Pages reviewed 14/14; numbered displays (1)-(14), all as LaTeX with `\tag`; formulas kept as images: 0.
- Figures 3 (each merged from two extractor crops); tables 2 (as cells, CSV); algorithms 2 (image crop + line-numbered transcription).
- Omitted regions 27: first-page PMLR banner, 13 running headers, 13 page numbers. Bibliography: 39 entries, all read.
- Adjudications 23: missing_lines on pp. 2-10, 12; number diagnostics on pp. 5-11.

## What was corrected
- Math: 14 extractor formula images replaced by LaTeX; all inline math rewritten (extractor output was `<sup>` soup with glued words).
- Algorithms 1 and 2 (12 and 18 fragmented list items) rebuilt as crop + transcription with printed line numbers and nesting.
- Headings: levels fixed (extractor had `#` for sections and author names as headings); small-caps 4.x.y headings in title case.
- Six cross-page sentences joined; four floats and the copyright line moved via `reading_order` (Figure 1, Algorithm 2, Figure 2, Table 1).
- References: split diacritics, line-wrap hyphens, broken URLs/DOIs and `vol(issue):pages` strings repaired; bullets removed.

## Checks beyond the tool
- pdflatex compile of all 14 displays and 302 inline formulas: no errors; rendering compared with the pages.
- Per-page symbol counts (PDF text layer vs LaTeX, incl. algorithm boxes): equal except the big-intersection glyph of (1) and (6), which the text layer encodes as a backslash.
- Per-page word multisets vs pdftotext: no prose word lost. Algorithm transcriptions vs box text layer: number tokens identical.
- Recomputed the printed epsilon values from the transcribed (2) and (4): 0.2509 (N=1000, s=67, d=400) and 0.1253 (s=22) reproduce.

## Limitations and uncertainties
- p. 3: Theorem 1 is set upright with no visible end; taken to end at display (3) (stated in the conversion notes).
- pp. 2-9: no TeX source, so every formula rests on 240-600 dpi reading plus the checks above; none was left uncertain.
- pp. 9-10: Tables 1-2 print the group label and "Estimate" once per three rows; blank cells left blank. Header symbol is the character ϵ, not LaTeX.
- p. 1: e-mail addresses are printed in small capitals and written in lower case.
- Paper inconsistencies kept as printed and listed in the notes: "s_N^* < d" vs case "s_N^* >= d" in (4) (p. 3); mu_i, sigma_i in (10) with no index on the left (p. 5); Algorithm 2 line 21 "If Sigma_i = Sigma, then S = S + 1" (p. 7); 0.1182 is reported with s_N^* = 19 but formula (2) gives it for s = 20 (p. 8); 0.1125 corresponds to d = 100 in (4), not 10^6 cells (p. 9).
- One reviewer only; no independent second verifier.

## Self-check
- SKILL.md, index.md and all 408 lines of paper.md read; no `<sup>`, replacement characters, strikethrough, glyph soup or unbalanced `$`; 18 real headings.
- Opened figure-1, figure-2, figure-3 (tick labels legible, both panels complete), algorithm-1, algorithm-2, both CSVs.
- Question: "State the guarantee: what probability is bounded, how does epsilon depend on the support count, what sample size is needed?"
  Answer from Section 2 (Theorem 1, displays (1)-(4)) and Sections 3.1/3.2: for scenario program (1) with N i.i.d. scenarios and no
  restriction on f or the constraint sets, V(x) = P{delta : x not in X_delta}; s_N^* is the size of an irreducible set of support
  scenarios. Given beta in (0,1), epsilon(s_N^*) = 1 if s_N^* = N, else 1 - (beta / (N binom(N, s_N^*)))^(1/(N - s_N^*)), and
  P{V(x_N^*) > epsilon(s_N^*)} <= beta. Convex refinement (4) replaces N by d (number of decision variables; d = m cells for the
  tiling) with case s_N^* >= d. No a-priori N: N is increased in batches until epsilon is acceptable (examples: N = 1000, beta = 1e-9).
  Checked against the 300 dpi crop of PDF page 3: matches.

## New pitfalls (not yet in the brief)
- Plan notes are printed into paper.md unchecked: a literal `$$` or an odd `$` in a note unbalances the math of the whole file. Run mathcheck on the staging paper.md (its assertion caught this) and write `\tag{n}` in backticks.
- `join_previous` is resolved in reading order, not page order: with `reading_order` a float at the top of a page that splits a sentence needs no text moved; only the item before it in reading order must be text/caption.
- A stacked exponent "-1/2" gives the token "−1" in the first parser but "− 1" in pypdf, so the two number diagnostics get different fingerprints and need differently worded reasons.
- An underscore drawn as a rule (DOI "...-8_4") is a space in the text layer; the tokenizer strips underscores, giving "-8","4" vs "-84".
- The spacing caron U+02C7 (Kunˇcak) counts as a letter in the line check and produces a missing line; ¨ ´ ˜ ¸ do not.
- symbol_check2.py does not cover big operators; in this PDF the big intersection is a backslash in the text layer.
- Recomputing printed numbers from the transcribed bound is worth doing: here it validated (2) and (4) and exposed two inconsistencies in the paper itself.
