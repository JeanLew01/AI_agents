# fan2017dryvr - reviewer report

**Paper**: Fan, Qi, Mitra, Viswanathan, "DryVR: Data-driven verification and compositional reasoning for automotive systems" (title as printed on the arXiv version; CAV 2017).
**Source**: arXiv:1702.06902v1 [cs.SY], 22 Feb 2017, 25 pages (text 1-17, references 18-22, Appendix A 23-25). TeX source used (section files, prelude1.tex, main2.bbl).
**Status**: `verify --strict` exit 0, status `reviewed_with_limitations`, 36 adjudications applied, 0 stale. Not rebuilt after the restart; state on disk re-checked.
**Package**: /home/jixia/AI_agents/paper2agent/Reachability/skills/fan2017dryvr-paper (paper.md 515 lines; identical to staging -s2 except the SKILL.md status line).
**Scratch**: /home/jixia/AI_agents/paper2agent/Reachability/logs/work/fan2017dryvr (p01.py-p25.py, pagelib.py, refs.py, make_plan.py, make_adjudications.py, checkers).

## Counts
- Figures: 3 image crops (Figures 1-3; printed sub-captions are inside the crop and repeated in the caption text).
- Tables: 1 (Table 1, CSV, 9 x 7, read on a 330-dpi crop).
- Algorithms: 2 (Algorithm 1 GraphReach, p.12, assets/figure; Algorithm 2 VerifySafety, p.25, assets/supp_figs), each crop + line-by-line transcription.
- Formulas kept as images: 0 (6 extractor formula images replaced by LaTeX displays; only (1) and (2) carry printed numbers).
- Omitted regions: 26 (arXiv margin stamp p.1, page number on each of the 25 pages).
- Adjudications: 36 (20 missing_lines, 8 number_differences, 8 independent_parser_number_differences).
- 762 math snippets; string comparison with the macro-expanded TeX leaves 12 deliberate rewrites. 56 references generated from the .bbl; letters and digits agree with the PDF text layer.

## What was corrected
- Every page rewritten by a generator script: math from the TeX with macros expanded; sub/superscript soup restored (p.7 sum, p.10 Prop. 3.1, p.15 Prop. 4.2, p.16 Prop. 4.3 / Thm. 4.4, p.17 graph chains).
- Headings re-levelled; theorem-like labels in bold as printed (Definitions 2.1, 2.2, 2.4, 2.6, 2.7; Propositions 2.3, 2.5, 2.9, 3.1, 4.1-4.3; Remark 2.8; Theorems 3.2, 4.4; three proofs).
- Real hyphens lost at line ends restored (first-order, one-clock, VC-dimension, i7-6600U, 10-20, URL hyphens of [46], [47]); underscores of mode names restored from strikethrough fragments; accented names in references.
- Floats printed mid-sentence at the top of a page moved within their page: Figure 2 (p.13), Table 1 (p.14), Figure 3 (p.17). PED condition split across pp.10/11 given in one piece.
- Algorithm 2, read by the extractor as a table, replaced by crop + transcription; merged references [46]/[47] separated.

## Limitations and uncertainties
- TeX/PDF disagreement, PDF followed (from p.2 on): the mode-set macro `\L` is printed as the letter 'Ł', transcribed `$\text{Ł}$`; the conversion notes say it stands for the authors' calligraphic L. vlab/elab/lmap/sim are printed italic (small caps in the TeX).
- Source typos kept and listed in the conversion notes: '=' inside the norm in the GED pair and the PED condition (p.10), exponent `\gamma_i t` in the PED condition, stray parenthesis in Def. 2.4(a) (p.5), plain `U` in Thm. 3.2 (p.13), 'shown in 2' (p.24), Algorithm 2 calling GraphReach(H) without S (p.25).
- No relative-completeness theorem is printed in this version: only the 'Correctness' paragraph (pp.12-13) pointing to Theorems 19 and 21 of [20]; said explicitly in the conversion notes. The paper gives no numerical instance of the Prop. 3.1 bound and no statement linking k to the number of traces.
- Figure 3(c) (p.17): the package image (MuPDF, the builder's renderer) shows translucent striped bands; the PDF has no transparency settings and poppler renders solid blue/red/gray bands, as the text describes. The asset cannot be changed; the conversion notes now give the solid colours. My earlier claim that the tubes are "drawn with transparency" was wrong.
- Table 1 (p.14): Model cells spanning two printed rows are repeated in both CSV rows; cells are plain Unicode with ASCII minus; a conversion note sits under the table.
- Algorithm 2 is `algorithm-2` in `supp_figs` (appendix); line numbers of both algorithms are written as plain numbers (bold in the PDF).
- The CAV proceedings version was not compared. Single reviewer, no independent verifier.

## Self-check (final package, repeated after the restart)
- Damage scan of paper.md: 0 hits (`<sup>`, replacement char, ` ˆ`, `** **`, `_ _`, `<u>`, `~~`); `$` count even; 6 displays and 807 inline snippets compile with pdflatex.
- Assets opened: figure-3 (smallest labels, legible), figure-2, figure-1, algorithm-1, algorithm-2, table-1.csv: complete.
- Question: "What is the PAC guarantee for the learned discrepancy, with its sample count, and what does soundness assume?" Answer from the package (Sections 3.1.1, 3.1.2, 3.2): draw k points from Γ according to D and find (a,b) with x_i ≤ a y_i + b for all i; Proposition 3.1: if k ≥ (1/ε) ln(1/δ) then, with probability ≥ 1−δ, err_D(a,b) < ε, where err_D(a,b) = D({(x,y) ∈ Γ | x > ay+b}); for GED, Γ is the set of pairs (ln(|τ1(t)−τ2(t)|/|τ1.fstate−τ2.fstate|), t) and the LP minimises γT + ln K. Theorem 3.2: if the β's returned by LearnDiscrepancy are always discrepancy functions, VerifySafety is sound (SAFE implies safe; UNSAFE implies an execution entering U). Checked against crops of p.10 (300-450 dpi) and p.13 (400 dpi): matches.

## New pitfalls for the brief
- A private macro can be silently overridden: here `\L` prints 'Ł' and `{\sc ..}` inside math prints italics. Check the printed glyph of every macro on its first page before bulk transcription.
- `accept.sh` counts `** **` as damage: a bold line number followed by a bold keyword (`**2** **for**`) triggers it. Write algorithm line numbers plain.
- The builder's renderer (MuPDF) and pdftoppm can render the same vector plot differently; look at the built JPEG too, and do not explain a difference without checking the PDF (scan for /CA, /ca, /SMask, /BM).
- `\mbox{... $t$ ...}` inside math must be rewritten as `\text{..} t \text{..}`; a nested `$` breaks mathcheck and Markdown.
- Bibliography: generating entries from the .bbl and comparing letters+digits per entry with the extractor text is fast and decisive (`refs.py`, `refcheck.py` in my scratch).
- The brief does not say where an appendix algorithm box goes; I used `algorithm-2` with `asset_category: supp_figs`.
- Hyphen before digits in printed text ('10-20', 'i7-6600U', '11-18') always gives a '-20'-type number diagnostic; unavoidable, adjudicate.
- A restart cancels a pending tool call with a "user doesn't want to take this action" result; I confirmed the restart with `uptime -s` against file timestamps before retrying the same call.

## Post-verification repair (after logs/verify/fan2017dryvr.md: 0 A, 1 B, 2 C)
- B1: conversion note on Figure 3(c) replaced. Checked first: pdftoppm crop of p.17 at 520 dpi (cruise: solid blue for x in [0, 3.5], solid red for [3.5, 4.5]; em_brake: red 0.1 to -0.5, blue -0.5 to -2, gray -2 to -9, red -9 to -10.1) and a scan of the PDF's 150 inflated streams (ExtGState only /OPM 1; no /CA, /ca, /BM; 2 /SMask). The JPEG itself is unchanged.
- C1: navigation purpose of "4 Reasoning principles for trace containment" now says proofs are printed for Proposition 4.1 and Theorem 4.4 only.
- C2: navigation entry added for "A Appendix" (26 entries).
- Only plan notes and bundle navigation changed (make_plan.py); no page file touched, so the review note of page 17 in the external review directory still has the old transparency wording. Staging -s3 built, final package deleted and rebuilt, `verify --strict` exit 0, `reviewed_with_limitations`, 36 adjudications applied, 0 stale; final identical to -s3.
