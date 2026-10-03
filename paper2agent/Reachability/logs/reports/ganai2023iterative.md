# ganai2023iterative - reviewer report

## Status
- Paper: Ganai, Gong, Yu, Herbert, Gao, "Iterative Reachability Estimation for Safe Reinforcement Learning" (NeurIPS 2023).
- Source: arXiv:2309.13528v1, 33 pages (main 1-10, references 11-13, appendix A-D 14-33); TeX source main.tex used (embedded thebibliography, 60 entries).
- `verify --strict`: exit 0, status `reviewed_with_limitations`, 44 adjudications applied, 0 stale, no issues.
- Final package: ~/AI_agents/paper2agent/Reachability/skills/ganai2023iterative-paper (21 files). Staging: staging/ganai2023iterative-paper-s1 (paper.md identical to final).
- Scratch: logs/work/ganai2023iterative (p01.py-p32.py + pagelib.py, checkers, review-queue-s0/s1.json, build/verify logs).

## Counts
- Figures 14 (Figures 1-6 in assets/figure; appendix Figures 7-14 as supplementary-figure-7..14 in supp_figs).
- Tables 2 (both in the appendix: supplementary-table-1 notation, supplementary-table-2 hyperparameters; CSV).
- Algorithms 1 (image + line-by-line transcription). Formulas kept as images: 0 (49 displays in LaTeX).
- Omitted regions 34 (arXiv stamp and NeurIPS footer on p1, page numbers p2-33). Adjudications 44 (24 missing-lines, 10 + 10 number).

## What was corrected
- All inline/display math rewritten from TeX (macros expanded); 43 extractor formula images replaced; tags (CMDP), (RCRL), (RESPO), (1)-(11).
- Extractor damage: glyph-soup math with `<sup>`, merged/split paragraphs, formula boxes that swallowed prose lines (p3, 6, 20, 21), fragmented algorithm box (p7), six separate image items for Figure 1, figure boxes overlapping captions (p8-10, 26-32), flattened Table 1, garbled Table 2 cells, heading levels, stray emphasis markers, lost compound hyphens.
- Sentence joins across pages 2-3, 4-5, 8-9, 9-10, 15-16; references generated from the embedded bibliography.

## Checks (all in scratch)
- texcompare.py: 606/606 math snippets identical to the macro-expanded TeX (2 differ only by colour-group braces).
- prosecompare.py: 871 prose runs, the 35 misses are all \ref-generated words, algorithm lines, "Proof", appendix letters.
- wordcheck.py / linecheck.py: no prose word lost on any page; 463/463 missing lines explained as math notation.
- symbol_check.py: per-page relation/operator/Greek counts agree with the PDF layer (only Ohm-sign Omega and the two-glyph "not equal").
- mathcheck.py: 49 displays + 338 unique inline snippets compile (4 small pdflatex batches). Number differences attributed token by token.

## Limitations and uncertainties (page numbers)
- p7, 9, 10, 17: floats reordered within their page (Figure 1 after heading 6; Figures 3-6 after the paragraphs that discuss them; Figure 7 after the C.4.1 paragraph).
- p8-10, 27-32: training curves are image crops only, values not digitised; p9: colour-bar tick labels of Figure 3 are illegible in the JPEG (tiny in the PDF; larger in Figure 12, p30).
- p14, p25: table cells use Unicode symbols; a paragraph marked "Conversion note ... (not part of the paper)" under each table gives the LaTeX forms; header row "Symbol | Meaning" added to Table 1.
- p30: Equations (10), (11) are colour-coded in the PDF; colours are listed in a marked conversion note, not in the formulas.
- p18, p20: a space typed in `[Q] (s,a)` and `[p] (s)` (Bellman operators) to stop Markdown link parsing; formula unchanged.
- p14-16: appendix restatements keep the printed numbers "Theorem 3", "Proposition 3", "Proposition 4", "Theorem 4" (= Theorem 1, Propositions 1-2, Theorem 2); explained in the conversion notes and index.
- p15, 18-22: "Proof." and the informal "Lemma 1-5" of the convergence proof are printed in italics, written bold; p23: underlined group labels kept as plain paragraphs.
- Source slips kept as printed and listed in "Conversion notes" (e.g. arg min over V_c in the optimal-REF definition, italic vs calligraphic S, `Upsilon_Theta[M(theta]`, "Equation is:" without number on p21, Q_h on p19).
- One reviewer, no independent second verifier. One machine restart during the work; nothing was lost (all pages were on disk).

## Self-check
- Damage search on final paper.md: 0 hits; `$` count even; 46 real headings; SKILL.md, index.md read; whole paper.md skimmed.
- Assets opened: figure-3.jpg (smallest labels: titles/axes legible, colour-bar ticks not), algorithm-1.jpg (both rules, lines 1-11 legible), both CSVs.
- Question: "Define the reachability estimation function, give its Bellman-type update, how it is learned, and the guarantee with assumptions."
  Answer (paper.md Sections 4.1, 5.3, 5.4, C.4.3): Definition 3, phi^pi(s) := E_{tau~pi,P(s)} max_{s_t in tau} 1_{(s_t|s_0=s,pi) in S_v}, the probability of ever reaching a violation; optimal REF phi^* = phi^{pi^*}, pi^* = arg min V_c^pi (Def. 4); feasible set {s: phi^pi(s)=0} (Def. 5).
  Theorem 1: phi^pi(s) = max{1_{s in S_v}, E_{s'~pi,P(s)} phi^pi(s')}. Learned REF p(s) = max{1_{s in S_v}, gamma p(s')}, 0 << gamma < 1; Algorithm 1 line 8 is its TD update; B_p[p](s) = max{1, gamma E[p(s')]} is a gamma-contraction in sup norm (C.4.3 Step 3).
  Theorem 2: for finite MDPs under A1 (sum zeta_i = inf, sum zeta_i^2 < inf, zeta_j = o(zeta_{j-1}); critics, policy, REF, multiplier from fastest to slowest), A2 (strict feasibility), A3 (differentiability/Lipschitz), the policy updates converge almost surely to a locally optimal policy of (RESPO); asymptotic, no finite-sample bound.
  Compared with 150 dpi crops of PDF pages 4 and 20: identical.

## New pitfalls for the brief
- `](` inside math is parsed as a Markdown link and stops the build ("Broken local link ... s,a"): operators like `\mathcal{B}[Q](s,a)` need a space before the parenthesis; grep the page scripts for `](` before building.
- Appendix restatements can be renumbered by running counters (Theorem 3 = Theorem 1): keep the printed number, map it in notes and navigation.
- The Unicode double-struck one in a table cell counts as a number token (Python `\d`); text in conversion notes under tables/equations appears as "extra" numbers, so compare its token multiset with the reported extras.
- Coloured formula terms (`\color`) carry meaning the LaTeX loses; say which terms have which colour in a marked note.
- When the bibliography is embedded in main.tex, generate the reference items from it and script-compare letters/digits with the extractor text (60/60 here) instead of retyping.
- Reusing the extractor text by item id for pure-prose paragraphs (helper `O()` with explicit replacements) avoids retyping errors and keeps page scripts short.
