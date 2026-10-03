# ouyang2026symplectic - reviewer report

**Paper**: Ouyang, Liu, Mallada, "Symplectic Inductive Bias for Data-Driven Target Reachability in Hamiltonian Systems".
**Source**: arXiv:2604.17213v1 [math.OC], 19 Apr 2026, 10 pages, two-column; authors' TeX source used (CDC2026_sample.tex).
**Result**: `verify --strict` exit 0, status `reviewed_with_limitations` (mechanical_ok, 12 applied / 0 stale adjudications).
**Package**: ~/AI_agents/paper2agent/Reachability/skills/ouyang2026symplectic-paper (paper.md 662 lines, 4 assets).
**Scratch**: logs/work/ouyang2026symplectic/ (page01-10.py, make_plan.py, make_adjudications.py, check scripts, verify-strict.out).

## Counts
- Figures 3 (Fig. 1-3, image crops + verbatim captions); tables 0; algorithms 1 (image crop + 20-line transcription).
- Formulas kept as images: 0. Display blocks 85, inline math 401; printed equation numbers (1)-(14), all as `\tag`.
- Theorem-like blocks: Definitions 1-8, Assumptions 1-8, Remarks 1-6, Problem 1, Proposition 1, Lemma 1, Theorems 1-4. References 29.
- Omitted regions: 1 (vertical arXiv stamp, p1). Adjudications: 12 (missing_lines p2-p9; number + second-parser p8, p9).

## What was corrected
- Math: every extractor formula image and glyph-soup item replaced by LaTeX from the TeX source, macros expanded.
- Reading order: p3, p7, p10 (extractor interleaved columns); paragraphs/statements merged across columns (p1, p3 Def. 6, p4, p5, p8, p10 ref [20]); cross-page joins p1-2, p2-3, p6-7, p8-9.
- Headings: small-caps sections to `##`, lettered subsections to `###` (extractor had `#`), `## Abstract`.
- Labels: whole label bold (`**Theorem 2 (Target Reachability).**`); `**Proof.**`; end-of-proof box as `$\square$`.
- Floats: Fig. 1 (p8, printed mid-sentence) moved after the paragraph citing it; Algorithm 1 rebuilt from fragments; Fig. 2/3 (p9) merged from 3 fragments each into one crop.
- References (p10): one item per entry, diacritics restored, entry [11] separated from [10], line-wrap hyphens closed.

## Checks beyond the tool
- texcompare.py: all 486 math snippets string-identical to the TeX source after macro expansion (only 2 brace-only differences + the 4 proof squares).
- prosecompare.py: 446 of 511 prose runs found verbatim in the TeX; the 65 others are labels, headings, resolved refs, captions, algorithm keywords (each inspected).
- wordcheck.py (word multiset vs pdftotext): no prose word lost on any page. symbol_check2.py: 5 differing counters, all explained.
- mathcheck.py: 85 displays + 289 unique inline snippets compile with pdflatex, no errors.
- Number diagnostics: none on p1-p7, p10; p8 = algorithm line numbers only; p9 = Unicode vs ASCII minus only.
- Consistency of main bound: (8) squared times mu_H/4 gives (11), whose reciprocal times (H2-H1) gives the Theorem 3 bound, as printed.

## Limitations and uncertainties
- Italic statement bodies are not reproduced; statement ends follow the TeX environments (listed in page notes).
- p1: two unmarked `\thanks` footnotes placed after the author line (no printed marker, so no "Footnote n:" prefix).
- p8: Figure 1 and Algorithm 1 are not at their printed position; algorithm nesting shown with em-spaces.
- p9: bar heights/error bars of Fig. 2-3 not transcribed (only the values quoted in the prose); run-in headings "1) Spring-Mass:" / "2) Single Pendulum:" written as `###` headings without the colon.
- p10: bibliography exists only in the PDF (biblatex, no .bbl); thin-space thousands separators written as ordinary spaces.
- Multi-line displays with a tag on one line ((8), (10), (11)) are split into one block per printed line.
- Source slips kept as printed, listed in "Conversion notes": p3 calligraphic R in Def. 6; p4 two empty-set glyphs; p6 "Assumptions 4-Assumption 7", duplicated clause, x_i in Step 2, T_eps(x)^star; p7 B_r(x) in (10), H_+^*, undefined eta; p8 "i=0,...N", undefined delta in S_tgt^delta; p1 "jliu376@jh.edu".
- One reviewer only; no independent second verifier. No uncertain symbol remained after the 330 dpi crops.

## Self-check
- Damage search on final paper.md: 0 hits (`<sup>`, replacement char, ` ˆ`, `_ _`, `** **`, `~~`), `$` count even, 19 real headings.
- Assets opened: figure-3.jpg (smallest labels; ticks, legend, sub-captions legible) and algorithm-1.jpg (all 20 lines, both rules).
- Question: "State Theorem 3 with its assumptions, radius and sample-complexity bound."
  Answer (paper.md, section "B. Existence of the Chain Policy", lines 315-325): system (1) under Assumptions 4-7, v_0 in (0, underline v_eps); there is an NCP from a finite K with
  r_i = (v_eps(x_i) - v_0) T*_eps(x_i) / (L_H (1 + e^{L T*_eps(x_i)})) > 0, u_i the optimal control reaching the boundary of H_tgt^eps; then (1) almost every x_0 in S_0 reaches S_tgt in finite time, and
  (2) with H(Supp(K)) = [H_1, H_2]: N <= (H_2 - H_1) * 16 L_H^2 / (mu_H (1 - v_0/underline v_eps)^2) * exp(2L(L_H D_X + eps)/underline v_eps) / eps^2.
  Compared with the 330 dpi crop of PDF page 6: identical.

## New pitfalls for the brief
- With TeX available, a string-identity check of every math snippet against the macro-expanded TeX (texcompare.py) and a prose-run check (prosecompare.py) are cheap and far more decisive than the missing-line list; both are in my scratch.
- symbol_check2.py misses `\leq`/`\geq`, `\gets`, `\varnothing`, and counts only `\varepsilon` (this paper prints `\epsilon`); patched copy in my scratch.
- Writing number lists with a space after the comma (`[-20, 20]`, `(24, 24, 16)`) and plain-text numbers in prose left pages 2-7 with zero number diagnostics.
- A tag printed on a middle line of a display needs one block per line, otherwise the tag attaches to the wrong relation.
- arXiv sources using biblatex ship no .bbl: the reference list can only be checked against the PDF.
- The restart cost me all viewing done before the first page was written: write page N before opening page N+1.
