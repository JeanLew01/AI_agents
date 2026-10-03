VERDICT: 2 findings (0 A, 0 B, 2 C)

# Verification of hewing2019scenario-paper against papers/hewing2019scenario.pdf

No mathematical, factual, numbering, caption, table or completeness error was found. Every
display, theorem-like block, table cell, caption and reference entry in `references/paper.md`
agrees with the page renders. The two items below are cosmetic.

## Findings

### C1 - "Remark n." and "Proof." labels are bold in the package, italic in the PDF
- Location: all seven remarks and both proofs, e.g. `**Remark 1.** The assumption of finite`
  (II-A, PDF p.3 left), `**Remark 5 (Half-space PRS).**` (IV-A, PDF p.5 right),
  `**Proof.** The proof follows from standard arguments` (III-C, PDF p.5 left).
- Package: label in bold.
- PDF: "*Remark* 1." and "*Proof.*" are italic, not bold (only Definition, Assumption, Theorem
  and Corollary labels are bold). For Remark 5 the parenthesised title "(Half-space PRS)" is
  upright.
- The conversion note ("Theorem, corollary and proof labels are set in bold") covers the proof
  label as a package choice but does not mention the remark labels.
- Confirmed on 260 dpi column crops of pp.3, 4, 5, 6.

### C2 - Conversion note says "only the ETH logo was omitted" from the cover sheet
- Location: `## Conversion notes`, "Layout decisions ... only the ETH logo was omitted."
- PDF p.1 also prints a green ORCID iD icon between "Hewing, Lukas" and "; Zeilinger, Melanie N.",
  which is not represented in the package line `**Author(s):** Hewing, Lukas; Zeilinger, Melanie N.`
  (its link target is recorded in the cover-sheet conversion note, so nothing is lost).
- Confirmed on a 260 dpi crop of p.1.

## Observation (not counted as a finding)

- Order of the front matter: the PDF order is cover sheet (p.1), then title, authors, abstract
  (p.2), with the unnumbered footnote at the foot of the first column. The package order is
  title, authors, footnote, `## Repository cover sheet (ETH Research Collection)`, `## Abstract`,
  so the cover sheet sits between the paper's author line and its abstract. Nothing is dropped or
  duplicated and the placement is documented in the conversion notes; flagged only so the
  reviewer can decide whether that position is wanted.

## Conversion-note claims ("kept as printed") - all confirmed on the PDF

`{1, ... n_c}` in (2a) and `{v_0^*, ... v_{N-1}^*}` without comma; "(see [9]." unclosed;
"for all 1 <= i <= N" for v_i^*; Assumption 4 intersection from k=1 vs Remark 3 "k = 0, ..., N-bar";
`W^{(i)} ~ \mathcal{W}` (Section II: `\mathcal{Q}`), W^{(i)} to index N-bar-1 and E^{(i)} to N-bar;
"Assumption (1)", "Figure (1)"; "discard the k samples" (Remark 5) and "remove k = 820 samples";
"P > 0" in (15a) (plain >, 500 dpi) and "P^{*-1}" in Corollary 3 (500 dpi); `\mathcal{I}_{dis}` in
Remark 7; "the sliders position"; italic `p_{ref}` in the Fig. 2 caption; R_k^{theta_max},
R_k^{theta_min} vs Table I +/-theta_max; d_p in the appendix matrix vs "d_m = 10" in the text
(500 dpi); "PP00P2 157601 / 1"; doubled "https://doi.org/https://doi.org/" on the cover sheet;
title "Scenario-based" on p.2 vs "Scenario-Based" on the cover sheet. No claim mis-describes
the PDF.

## Coverage

- Method: every paper page (2-7) rendered as six 260 dpi column crops (left/right x three
  vertical bands) and read completely against paper.md, i.e. the whole text, not a sample.
  Cover sheet p.1 read at 260 dpi. Extra 500 dpi zooms: Theorem 1 with (6); (7); (15a)/(15b);
  Corollary 3; Assumption 4 with its display and the Z_infinity line; the appendix matrix equation
  and parameter paragraph.
- Theorem-like blocks checked: 19 of 19 (Definitions 1-2, Assumptions 1-4, Theorems 1-3,
  Corollaries 1-3, Remarks 1-7), plus the 2 proofs; numbers, titles ("(k-step PRS)", "(PRS)",
  "([9])", "(Half-space PRS)") and statement boundaries correct.
- Displays checked: 42 of 42. 34 tagged lines (1), (2a)-(2b), (3a)-(3b), (4a)-(4b), (5a)-(5b),
  (6), (7), (8), (9a)-(9c), (10a)-(10b), (11a)-(11g), (12), (13a)-(13b), (14a)-(14b),
  (15a)-(15b), (16), (17a)-(17b): each tag sits on the right equation, each appears once, in
  order. 8 untagged displays (Def. 1, Def. 2, Assumption 2, expected cost, Assumption 4,
  IV-A chance-constrained problem, x^ref cases, appendix equation) are untagged in the PDF too.
- Arithmetic cross-check of two transcribed formulas against numbers printed elsewhere:
  (7) with p = 0.9, N_s = 10000, d = 1, beta = 1e-7 gives N_k <= 820.46, matching "k = 820";
  (8) with N_s = 10000, beta = 1e-7 and d = 4 (my reading of the |p|,|v| box as four
  half-spaces) gives p >= 99.636 %, matching "99.6%".
- Algorithms: none in the paper, none in the package (0 lines).
- Table cells: Table I, 12 of 12 (3 header + 9 body) in both `assets/table/table-1.csv` and the
  Markdown table; caption "TABLE I / CLOSED-LOOP CHANCE CONSTRAINT EVALUATION"; the note giving
  the stacked-vector form of the first Constraint cell is correct.
- Figures: 2 of 2. figure-1.jpg is the complete crane sketch (u, p, theta, w, p_0, p_1), no
  foreign text; figure-2.jpg has all four panels w(k), p(k), theta(k), u(k) with tick labels and
  the k axis, no foreign text. Captions "Fig. 1." and "Fig. 2." verbatim, numbers correct.
- Completeness and order: `pdftotext` word sequence (3187 words of 3+ letters) diffed against
  paper.md with math removed (3225 words). All differences are math-layer residue, line-break
  hyphenation, small-caps headings, float placement and the documented front-matter order; no
  dropped or duplicated passage. All ten page/column breaks checked by eye, no cut sentence.
  References [1]-[16]: 16 of 16 entries, each compared field by field.
- Prose read word for word: all paragraphs on pp.2-7 (abstract, I, II-A/B/C, III, III-A/B/C,
  IV, IV-A/B/C, V, V-A, V-B, VI, acknowledgments, appendix), including inline math.
- Headings and index: 23 `##`/`###` headings, all real and correctly numbered/nested (I-VI with
  A-C subsections as printed); the 23 index.md rows each match exactly one heading; index
  descriptions point to the right content; SKILL.md, supplement.md and asset links resolve.
- Cover sheet hyperlinks: the PDF holds 6 link URIs; the 4 targets quoted in the cover-sheet
  conversion note match them exactly (the other 2 are the links whose visible text is the URL).
- Question 1: "How many scenarios were drawn and how many discarded for the load-angle chance
  constraints, at which level and confidence?" Package route: index -> "A. Simulation Setup" ->
  N_s = 10000, k = 820 samples removed via (7) (Corollary 1 with Remark 5), p_2 = 90 %,
  beta = 1e-7. PDF p.6 right / p.7 left: same.
- Question 2: "Which d enters condition (6) for an ellipsoidal PRS, with free and with fixed
  centre, and what set is certified?" Package route: index -> "C. Ellipsoidal PRS" ->
  Corollary 3: d = (n^2+n)/2 + n, set {e | (e - e_c^*)^T P^{*-1} (e - e_c^*) <= 1}; Remark 6:
  d = (n^2+n)/2 for e_c = 0. PDF p.6 left: same.

## Not checked

- Claims in the conversion notes about things outside this PDF (title casing in the IEEE
  record, "published online 2019") and the reviewer's stated render resolutions and pdflatex run.
- I did not compile the LaTeX; only brace and \left/\right balance of the 42 displays was
  checked by script (all balanced).
- Figure colours and curve shapes were compared only at the level of "same picture, complete".
- The lowest ~0.4 in of each page was outside the 260 dpi crops; the text layer has nothing there.
- No TeX source exists for this paper, so none was consulted.
- Renders in logs/verify/work/hewing2019scenario/ were deleted; the empty directory remains.
