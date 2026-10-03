# lin2024verification - conversion report

**Paper**: Lin, Bansal, "Verification of Neural Reachable Tubes via Scenario Optimization and Conformal Prediction" (L4DC 2024, PMLR 242:719-731).
**Source**: arXiv:2312.08604v2 PDF, 16 pages (main 1-10, refs 11-13, Appendices A-B 14-16); authors' TeX source used for all mathematics.
**Result**: `verify --strict` exit 0, status `reviewed_with_limitations` (mechanical_ok, 26 adjudications applied, 0 stale).
**Package**: `~/AI_agents/paper2agent/Reachability/skills/lin2024verification-paper` (paper.md 366 lines, 6 figure assets).
**Scratch**: `logs/work/lin2024verification/` (pagelib.py, p01-p16.py, make_plan.py, make_adjudications.py, checkers, review-queue-s1/s2/s4.json, verify-strict.out).

## Counts
- Figures 6 (figure-1 ... figure-6), tables 0, algorithms 0, formulas kept as images 0.
- Display blocks 17 carrying the 14 printed equation numbers (1)-(14); 339 inline formulas; all compile with pdflatex.
- Theorem-like blocks: Remark 1, Theorem 2, Theorem 3, Remark 4, Lemma 5, Remark 6, Lemma 7; 4 proofs. References: 31 (unnumbered, author-year).
- Omitted regions 33: PMLR banner, arXiv stamp, copyright line (p1), 15 running headers, 15 page numbers.
- Adjudications 26: missing_lines on pp. 3-11, 14-16; number_differences + second parser on pp. 3, 4, 5, 6, 9, 10, 16.

## What was corrected
- Math: all 14 extractor formula images replaced by LaTeX from TeX (macros expanded), each checked on 200-220 dpi crops; TeX and PDF agree everywhere.
- Structure: heading levels fixed (extractor had sections as `#`, authors and "Proof" as headings); keywords split from abstract; theorem labels bold as printed; proofs end with a black square.
- Page breaks: joins on pp. 1/2, 3/4 (inline formula split, completed on p3), 4/5 (inside "sampling-and-discarding"), 6/7, 8/9, 9/10.
- Figures: the two panels of Figure 1 merged into one crop (p6); crop edges checked on wider renders; Figure 5 (top of p10, inside a Section 6.3 sentence) moved after the Section 6.2 paragraph via reading_order.
- Text damage: dropped hyphens restored (scenario-based, trade-off, multi-vehicle, No-Go, classification-based, chance-constrained, ...), split diacritics in references (pp. 11-13), broken page ranges/URLs closed up, merged paragraphs split (pp. 3, 9), split paragraph merged (p7).
- End-to-end check: transcribed condition (2) reproduces the printed values (k=731, N=3684118, beta=1e-16 -> 99.974 %; k=0 -> 99.999 %; 1-beta=0.9 -> 1-eps=0.99979; N~116K, k=0 -> log10 eps = -3.5).

## Limitations / things a reader should know
- pp. 5, 7, 8: the text says three times that proofs are "in the Appendix of the extended version" (footnote 1, URL). Kept verbatim; this arXiv version contains that appendix (pp. 14-16). Footnote 1 sits after the Section 4 paragraph carrying its first mark.
- pp. 6, 7, 9, 10: figures are raster images, so in-figure labels are not searchable; the values printed only inside figures (Figure 2(b) N/k pairs, Figure 1 axis pairing of log10 eps with % safety, Vol. annotations) are listed in the conversion notes.
- p15: displays ending in (11) and (12) are three-/two-line aligned displays with a number on the last line only; written as consecutive `$$` blocks, tag on the last (alignment not kept).
- p1: e-mails printed in small capitals are written lower-case (as in TeX). Italic theorem bodies are not reproduced; statement ends are given in the conversion notes.
- Authors' slips kept and listed in the notes: "split conform prediction" (p8), "HJI-VI" (p10) vs "HJB-VI", `g*_{N,k}` with N and a final sum in n identified with Equation (9) in N (p16), "side length 20m" vs bounds 20.0 (p9).
- Not a conversion issue but relevant to the reader's question: Theorem 2/Lemma 5 are stated for the true V, Theorem 3/Remark 4 for the induced cost J of the learned policy (linked by J <= V in A.1/B.3); the only stated sampling assumption is N i.i.d. states from "some probability distribution P over S"; that k is data-dependent is discussed only informally ("k is a random variable"), and Lemma 7 rests on Campi-Garatti (2011) Theorem 2.1 with d=1.
- Single-agent review; no independent second verifier.

## Self-check
- SKILL.md, index.md and all of paper.md read; no `<sup>`, replacement characters, stray accents, `~~`, `^*`, odd `$`; 24 headings, all real. Opened figure-1 and figure-3 (smallest labels) and figure-5: complete and legible.
- Question: "State the scenario-optimization guarantee: what is sampled, what is random, the bound, how outliers enter; and the conformal counterpart."
- Answer (Section 4 "Procedures" + Theorem 2; Section 5; Appendix A): S is the candidate safe set (super-delta level set of the learned value). Draw N i.i.d. states x_{1:N} from S under a distribution P over S (rejection sampling), roll out the learned policy, and let k = number of samples with cost J(x_i,0) <= 0 (outliers; they are not removed from S, they weaken eps). For eps, beta in (0,1) with sum_{i=0}^{k} C(N,i) eps^i (1-eps)^{N-i} <= beta (2), with probability >= 1-beta over the sample, P_{x in S}(V(x,0) <= 0) <= eps (3). Proof: Lemma 7 (1-D chance-constrained program, sampling-and-discarding, discard the k constraints with -J >= 0) plus J <= V. Conformal: P_{x in S}(J(x,0) > 0) ~ Beta(N-k, k+1) (4), marginal coverage >= (N-k)/(N+1) (Remark 4), and Lemma 5 = same condition (5) and guarantee (6); B.2 shows the Beta CDF equals the binomial tail. Checked against PDF pages 5, 7, 8, 14 crops: identical.

## New pitfalls (not yet in the brief)
- A float printed at the top of the next page inside a running sentence: `join_previous` silently attaches the continuing text to the float's *caption* (caption counts as prose), with no error. Always move such a float with reading_order and re-read the join in paper.md.
- Text-layer spacing depends on math size: "k + 1" (text/display) tokenises as `1`, "N+1" inside script-size fractions as `+1`. Typing the LaTeX spaces accordingly removed 12 number differences on pp. 7, 15, 16 without touching the math.
- `\implies` is "=⇒" in the text layer, so symbol_check2 shows one extra "=" per arrow.
- Split diacritics: the modifier circumflex "ˆ" (U+02C6) counts as a letter in the tool's normalisation, so "J´erˆome" gives a missing line on a reference page although the entry is right; acute and cedilla do not.
- Raster figures give no number diagnostics at all, which also means nothing flags values that exist only in a figure; copy the decisive ones into the plan notes.

## Post-verification repair
- Independent verifier (logs/verify/lin2024verification.md): no A/B findings; two cosmetic C findings in the package metadata, both fixed. Page files were not touched.
- C1, conversion notes (figures bullet): the marked volumes of Figures 4(b)-6(b) are now described as "next to the dashed 99.990% safety line", with the detail that both markers of 4(b) and the grey 0.334 marker of 5(b) lie on the line, the cyan 0.366 marker of 5(b) slightly below it and the cyan 0.19 marker of 6(b) clearly below it (re-checked on the figure-5 and figure-6 assets).
- C2, navigation: added an index row for "3. Background: Hamilton-Jacobi Reachability, DeepReach, and Safety Verification" (index now has 23 rows for the 23 headings below the title).
- Rebuilt staging (`-s5`), deleted and rebuilt the final package; `verify --strict` exit 0, status `reviewed_with_limitations`, 26 adjudications applied, 0 stale; notes have no `$`, paper.md math compiles (17 displays, 339 inline).
