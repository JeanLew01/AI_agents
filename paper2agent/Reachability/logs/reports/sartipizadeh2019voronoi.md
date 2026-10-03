# Report: sartipizadeh2019voronoi

**Paper**: Sartipizadeh, Vinod, Açıkmeşe, Oishi, "Voronoi Partition-based Scenario Reduction for Fast Sampling-based Stochastic Reachability Computation of LTI Systems" (printed arXiv title, used as package title; the ACC 2019 title "... of Linear Systems" is given in the conversion notes).
**Source**: arXiv:1811.03643v1 [math.OC], 8 Nov 2018, 15 pages, single column. Authors' TeX source and .bbl used.
**Status**: `verify --strict` exit 0, status `reviewed_with_limitations` (22 applied, 0 stale adjudications, no issues).
**Package**: `~/AI_agents/paper2agent/Reachability/skills/sartipizadeh2019voronoi-paper` (staging builds -s1, -s2, -s3 kept).
**Scripts**: `logs/work/sartipizadeh2019voronoi/` (make_pages.py + pages_NN_NN.py, make_plan.py, make_adjudications.py, symcheck.py, wordcheck.py, mathcheck.py, verify-strict.out, review-queue-s1..s3.json).

## Counts
- Figures 5 (image crops, captions verbatim). Tables 1 (Table 1 as cells/CSV). Algorithms 1 (image crop + transcription).
- Display formulas: 36 `$$` blocks, 30 with printed tags (1)-(26) incl. (6a)-(6c), (14a)-(14c); 0 formulas kept as images.
- Omitted regions: 1 (vertical arXiv stamp, p1). No page numbers or banners are printed.
- Adjudications: 22 (12 missing_lines on pp. 2-13; 5 + 5 number differences on pp. 2, 3, 6, 10, 11).

## What was corrected
- All mathematics rewritten in LaTeX from the TeX source (macros expanded, `^{\ast}` throughout) and checked on 150 dpi renders and 220-240 dpi crops of pp. 3-11; TeX and PDF agree everywhere. All 36 displays were also compiled with pdflatex and compared with the pages.
- 35 extractor formula images replaced; superscript soup in pp. 2-3, 6-10 restored; the three optidef MILPs (Problems 1-3) written as `\max_{...}` / `aligned` with `s.t.`.
- Problems 1-3, Remarks 1-3, Questions 1-2, Lemmas 1-4, Theorems 1-3 labelled in bold; ends taken from the TeX environments (listed in the conversion notes); proofs end with `$\blacksquare$`.
- Headings re-levelled with printed numbers; author diacritics restored; two cross-page sentences joined (pp. 10/11, 11/12); 26 references each compared with the page.
- Diagnostics: every missing line contains math; word-multiset check per page found no lost prose word; symbol counts (relations, hats, both epsilons, asterisks, Greek) agree with the PDF text layer; all number differences are Unicode-minus vs ASCII, Algorithm 1 transcription numbers, or pypdf splits ('(N− 1)', '2 .68'), each confirmed.

## Limitations and things a reader must know (page numbers of the PDF)
- p6, source inconsistency kept as printed: Theorem 1 states the event as `p*(x0) − p*_K(x0) ≥ δ`, while Question 1 (p4), eq. (15), the final chain and the end of the proof use `p*_K(x0) − p*(x0) ≥ δ`. Confirmed on a 230 dpi crop; flagged in page notes and conversion notes.
- p10, proof of Theorem 3: `\hat{p}^*_{\hat K}` (hat on p) and `(z^{(j)}=0)` without hat, vs `p^*_{\hat K}` and `\hat z^{(j)}` in the statements; kept as printed.
- p3: (6c) `R = {x | FX ≤ h}` and `F ∈ R^{L×n_x}`; p5: (9) quantifies over `j, ℓ`; p11: `3ωx` in (23), `W_N`; all kept as printed and listed.
- p1: the title footnote (funding, affiliations) is placed after the author line, not at the page bottom inside Section 1.
- Reading order differs from page order for four floats: Figure 3 (p9) follows the sentence citing it on p8, so Theorem 2 is directly followed by its proof; Figure 4 (p12, printed mid-sentence) follows the paragraph "We set K=2000 ..." (p11); Table 1 and Figure 5 (p13, printed after the Conclusion) follow the Section 5 paragraphs citing them.
- p13, Table 1: the printed first body cell stacks "Algorithm 1" and three settings; written as a label row with empty value cells plus three rows. Cells are plain text with Unicode `K̂` (not LaTeX).
- p11: the paper does not print the δ, β behind K = 2000, so bound (13) could not be cross-checked against a printed number.
- Theorem-like bodies are upright (printed italic). Review by one agent; no independent second verifier.

## Self-check
- Damage scan of final `paper.md` (`<sup>`, `�`, ` ˆ`, `_ _`, `** **`, `^*`, `~~`): none; `$` balanced; 17 real headings; mathcheck: 36 displays, 449 inline, no LaTeX errors.
- Opened `figure-5.jpg` (smallest labels: legend legible), `figure-3.jpg` (rotated labels complete), `algorithm-1.jpg`, `table-1.csv`: complete.
- Question: "State the scenario-count theorem with its assumptions and the bound, and define the Voronoi buffers."
  Answer from the package (Section 3, Theorem 1 and (13); Section 4.1, Lemma 4 with (17)-(18)): for violation parameter δ ∈ [0,1], risk β ∈ [0,1], x0 ∈ S and U*_K optimal for the sampled MILP (Problem 2) with K i.i.d. disturbance scenarios, the risk of failure is ≤ β if K ≥ −ln(β)/(2δ²) (one-sided Hoeffding; K does not depend on the horizon N; the event is printed as p* − p*_K ≥ δ in the theorem and p*_K − p* ≥ δ in Question 1 and the proof). Buffers: ε^(j) = [ϵ_1^(j), ..., ϵ_L^(j)]^T with ϵ_ℓ^(j) := max over φ in cell V^(j)_{Φ_K}(Ψ_K̂) of (F_ℓ φ − F_ℓ ψ^(j)), ℓ ∈ N_[1,L]. Checked against the 230 dpi crops of PDF pp. 6 and 8: identical.

## New pitfalls (not yet in the brief)
- optidef `maxi`/`mini` environments print "lhs = max" with the variable below and "s.t." rows; write `p^{\ast}(x_0) = \max_{U\in\mathcal{U}^N} \quad ...` and an `aligned` block with `\text{s.t.}`; unnumbered starred forms carry no tag.
- A `\left`/`\right` balance check must not count `\rightarrow`/`\leftarrow` (use `\\right(?![A-Za-z])`).
- Fingerprints follow the diagnostic payload, not the page: a cosmetic edit that leaves missing lines and numbers unchanged (here a label's bold markers on p6) keeps the adjudications valid; rebuild only. The queue is then empty, so a `make_adjudications.py` that asserts on the queue cannot be rerun: keep `adjudications.json`.
- The PDF text layer maps Computer Modern `\phi` to U+03C6 and has no ∑/∏ characters, so symbol_check2-style counters report phi/varphi and sum/prod mismatches that are harmless.
- Unicode `K̂` in table cells is reported as a missing line against the PDF's 'ˆK' glyph order: one extra adjudication for the table page.
- `**Lemma 2.** **(Title)**` trips the `** **` damage search; use one bold span `**Lemma 2. (Title)**`.
