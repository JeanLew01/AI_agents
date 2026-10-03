VERDICT: clean

KEY = liebenwein2018sampling (Liebenwein, Baykal, Gilitschenski, Karaman, Rus, RSS 2018, 10 pages)
Verifier run: 2026-10-02. Ground truth: papers/liebenwein2018sampling.pdf (no TeX source exists for this key).
Package checked: skills/liebenwein2018sampling-paper (SKILL.md, references/index.md, references/paper.md,
references/supplement.md, assets/figure/*.jpg).

## Findings

None. No A, B or C item was confirmed.

Every mathematical object in paper.md was compared by eye against 300 dpi column crops of the PDF
(600 dpi for the smallest sub/superscripts), and all prose was compared mechanically against
`pdftotext` and then read on the page. I found no wrong symbol, direction, index, constant, exponent,
set relation, label, equation number, caption, heading, order, or dropped/duplicated passage.

Not findings, listed only so the reviewer does not re-open them:

- Line-break hyphens that the PDF cannot decide (word broken at the end of a printed line, package keeps
  the hyphen): Abstract "asymptotically-optimal"; Sec. II last paragraph "provably-optimal" and
  "simple-to-implement"; Sec. I item 1 "under-approximation". The package choice is consistent with how
  the same compounds are printed unbroken elsewhere in the paper ("asymptotically-optimal algorithm" in
  Sec. IV, "provably-accurate" in Sec. I, "under-approximations" in Sec. I/II). Unsure in the strict
  sense, not reportable.
- Oddities of the paper itself that the package reproduces exactly as printed (checked on crops):
  "f(x) ⊆ 2^Y" (Sec. III); "ensure that that the union" (Sec. IV-A); Alg. 1 line 2 "≥ δ" vs "> δ" in
  the proof of Lemma 2; italic H in d_H in Assumption 2 only; "g : R^m → Y onto Y"; "we have also have"
  (proof of Lemma 4); "=" instead of "⊆" in the last step of the proof of Lemma 6; μ(F(S)) rather than
  μ(F(X)) on the right-hand side in Corollary 8 and Theorem 10; "X ∈ R^3" (Sec. VI-A); third row of the
  RSL parametrisation "θ_1/ρ − θ_2/ρ" (600 dpi); Theorem 10 running time without the factor 3 that
  Corollary 9 has.

## Coverage

Renders: one page / one crop at a time, deleted afterwards (work directory removed).
pp. 3-6 fully at 300 dpi in six column crops each; p. 2 right column lower half (Sec. III) at 300 dpi;
p. 9 (refs [1]-[28]) at 260 dpi; 600 dpi zooms on the RSL display, Theorem 7 (sup subscript, exponent
−1/d), the packing definition (min subscript) and Theorem 1's constant C; pp. 1, 2, 7, 8, 10 at 170 dpi
(prose, captions, refs [28]-[36]; no display mathematics on these pages except Sec. III on p. 2, which
was cropped at 300 dpi).

1. Theorem-like blocks checked symbol by symbol: 15 of 15
   (Problem 1; Assumptions 1, 2, 3; Theorem 1; Lemmas 2, 3, 4, 5, 6; Theorem 7; Corollaries 8, 9;
   Theorem 10; Proposition 11), including printed number, parenthetical title, quantifiers, ⊂ vs ⊆ on
   every set relation, half-open intervals (0, Δ(X)], and where the italic statement ends.
   Proofs checked line by line: 4 of 4 printed (Lemmas 2, 4, 5, 6), end-of-proof marks present.
2. Displayed equations: 24 of 24 (the PDF has 24, the package has 24), of which 7 numbered; tags
   (1)-(7) sit on the right equations ((3) on Lemma 4's bound, (4) on the second line of the g(δ′)
   chain, (5)/(6) on the Lemma 5/6 inclusions, (7) on the unicycle dynamics). All 24 displays and all
   409 inline formulas of paper.md compile under pdflatex (amsmath/amssymb) without error.
3. Algorithms: 21 of 21 numbered lines (Alg. 1: 4, Alg. 2: 12, Alg. 3: 5) plus the three Input/Output
   headers, against the 300 dpi crop: numbering, nesting (Alg. 1 line 3; Alg. 2 lines 10-11; Alg. 3
   lines 3-4), the two numbered comment lines 3 and 5 of Alg. 2, line 6
   δ ← d((1−ε)^{−1/d} − 1)/(αKc), Output line of Alg. 2 with μ(F(X)).
4. Tables: none in the PDF, none in the package (0 cells).
5. Figures: 4 of 4 assets (figure-1..4.jpg) plus the 3 algorithm crops (algorithm-1..3.jpg): each is
   the complete float (all panels, legends, axis labels and tick labels, Fig. 1 sub-captions (a)-(d)),
   no foreign text, no cut edge; figure-3 and figure-4 are the right, distinct figures. Captions of
   Fig. 1-4 verbatim; label numbers correct.
6. Completeness and order: word-level diff of `pdftotext` (all 10 pages) against paper.md, once on all
   words of 3+ letters and all numbers, once with package math stripped and all words, once including
   punctuation. Only differences: de-hyphenation at line ends, small-caps headings/algorithm names,
   accented letters split by pdftotext, and the relocation of floats (Fig. 1-4, Alg. 1-3). No dropped,
   duplicated or reordered passage; no sentence cut at a column or page break (checked specifically at
   the p.1 col.1→col.2 break around Fig. 1, p.2→3, p.3→4 around Alg. 3, p.6→7, p.7→8). No footnotes in
   the paper other than the equal-contribution note, which is present. References [1]-[36]: all 36
   entries present once, authors, titles, venues, volume(issue):pages, years and back-reference page
   numbers match.
7. Prose spot check: pages 1-8 read on the render next to the package (all paragraphs of pp. 3-6 at
   300 dpi; pp. 1, 2, 7, 8 at 170 dpi), plus the mechanical diff above for every page; inline math in
   Sec. III, IV-A, V, V-A, V-B, VI-A, VI-B checked on crops.
8. Headings and index: 18 of 18 index entries exist verbatim as headings in paper.md and contain what
   the index says (I-VII, IV.A-C, V.A-B, VI.A-B, Abstract, Acknowledgments, References, Conversion
   notes); numbering and nesting match the PDF. supplement.md correctly states that nothing was
   supplied (the PDF has no appendix).
   Q1: "Which packing precision does Algorithm 2 use for accuracy ε, and how many samples can that
   cost?" Index → "B. Approximately-optimal Algorithm" (Alg. 2 line 6) and "B. Analysis of Algorithms 2
   and 3": δ ← d((1−ε)^{−1/d} − 1)/(αKc) (Theorem 7 allows any δ ≤ that value, with
   α = sup_{X′⊆X} λ(∂F(X′))/μ(F(X′)), K the Lipschitz constant, c the constant of Lemma 3);
   Corollary 9: |S| ≤ (3αKΔ(X)c/ε)^d. Matches PDF p. 3 (Alg. 2) and p. 6.
   Q2: "How were the experiments run (model, terminal time, trials, machine)?" Index → "VI. Results",
   "A. Experimental Setup", "B. Evaluation of Computed Reachable Sets": unicycle model (7), MATLAB,
   2.60 GHz Intel i9-7980XE (single core), 128 GB RAM; T = 1 second; grid construction instead of the
   random δ-covering; four initial sets (unit cube, dumbbell, lollipop, hedgehog); results averaged
   over 10 trials. Matches PDF pp. 6-8.
9. Conversion notes: every "kept as printed" claim was confirmed on a crop (Corollary 8 / Theorem 10
   with μ(F(S)); Alg. 1 "≥ δ" vs proof "> δ"; "f(x) ⊆ 2^Y"; italic H in Assumption 2; "onto Y"; "=" in
   the proof of Lemma 6). Also confirmed: proofs printed only for Lemmas 2, 4, 5, 6; no appendix; float
   positions as described (Alg. 3 printed inside Sec. V on p. 3, Fig. 2-3 at the top of p. 7 above the
   VI-B heading); statement end points as listed; back-reference page numbers in the reference list.

## Not checked

- Plot contents of Fig. 1-4 (curve values, tick positions) beyond "the asset is the complete, correct
  figure"; the package does not transcribe them.
- The claim in the conversion notes about the render resolutions the reviewer used (200-900 dpi)
  cannot be verified from the PDF.
- Pages 1, 7, 8 and 10 were not re-rendered above 170 dpi because they contain no display mathematics
  and nothing on them looked doubtful; had a finding arisen there it would have been re-cropped at
  250+ dpi before reporting.
- SKILL.md body is generic boilerplate (it mentions CSV tables and workbooks that this package does not
  have); not treated as a conversion error.
