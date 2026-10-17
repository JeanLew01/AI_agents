VERDICT: 1 finding (0 A, 0 B, 1 C)

# Verification of nath2026koopman-paper against papers/nath2026koopman.pdf (arXiv:2601.01076v1, 28 pp.)

Verifier: independent, read-only. All 28 pages rendered one at a time at 170 dpi, with 260-300 dpi crops of every
theorem-like block, every numbered display, Algorithm 1, both tables, and selected figure details. Renders deleted.

## Findings

1. **C** - Conversion notes, last bullet ("Values that exist only inside figures"): "hopper: 11 states over about 4.5 s".
   PDF p. 26 (Figure 11): the time axis of the hopper plots starts at about 1.05 s and ends at about 4.8 s
   (ticks 1.5, 2.0, ..., 4.5 in the large Height z panel; ticks 2, 3, 4 in the small panels). So the plotted span is about
   3.8 s and the axis ends near 4.8 s, not "about 4.5 s". Suggested wording: "hopper: 11 states, x-axis 'Time (s)' from
   about 1 s to about 4.8 s". Confirmed on a 260 dpi crop of the Figure 11 time axis. This only matters if "over about 4.5 s"
   is meant as a duration. If it is meant as "up to about 4.5 s", it is only slightly imprecise.

No A or B findings. Everything else I checked matches the printed pages exactly (details below).

## Specific points from the task
- Lemma 1 (p. 7 and p. 15): both copies match symbol by symbol, including the printed slip "x-hat_t in X-hat_t"
  (\hat{\mathcal{X}}_t without overline), the argument order Gamma(x_0, z^ref_{0:T}, u^ref_{0:T-1}) and the KRS symbol
  \hat{\overline{\mathcal{X}}} (hat above bar).
- Theorem 1 (p. 8 and p. 15): both copies match, including "≡", diag(ē_t) B_1(0), the {·}_{t=0}^T range, the 5.4 form
  "contains the true closed-loop system trajectory ... i.e., P(...)" and the 8.1 form "contains true closed-loop system
  trajectory ... 1 − δ:" followed by a separate display. Tags (10) in 5.4 and (11) in 8.1 are on the right displays. The text
  cites "(11)" on p. 8 ("using (11)"), p. 9 ("as defined in (11)") and p. 9 ("computed via (11)"), all reproduced.
- (3)/(4) (p. 6) and (8)/(9) (p. 8): printed side by side and correctly split into separate tagged blocks. (8) is
  x̂^(i)_{1:T} = {ψ(K_A z_t + K_B(u^ref_t − G_t(z_t − z^ref_t)))}_{t=0}^{T−1}. (9) is printed with the unclosed "f(", as the
  package says.
- (14) (p. 18, 300 dpi): all 12 rows match, including row 4 "q·sin(φ)/cos θ + r·cos φ/cos θ", row 6
  "p + q·sin φ·tan θ + r·cos φ·tan θ", rows 7-8 (row 8 prints "cos φ·sin φ"), row 9 "g + u_1·(cos φ·cos θ)/m" and
  rows 10-12 with u_2/I_x, u_3/I_y, u_4/I_z. The parameters m = 1 kg, g = −9.81 m/s², I = [0.5, 0.1, 0.3] kg·m² and
  dt = 0.025 s match. (12) has the trailing period and (13) none, as printed.
- SNSA (p. 8): λ_{t,j} ≐ 1/(e^max_{t,j} + σ) ∈ R_{>0}, the D_N range {e^(i)}_{i=K^cal+1}^{K^cal+M^λ}, the index set
  {K^cal+1, ..., K^cal+M} (M, as printed), R^(i) = max_{t,j}(λ_{t,j}|e^(i)_{t,j}|), C = Quantile_{1−δ}({R^(i)} ∪ {∞}),
  p ≡ ⌈(K^cal + 1)(1 − δ)⌉, ē_{t,j} = C/λ_{t,j} and ē_{t,j} ∈ R_{≥0}, plus the unnumbered coverage display: all match.
- Table 1 (p. 10, 300 dpi): all 11 header cells and 55 data cells match, including "−4.969", "−1.806", "32.595",
  "42.617", "99.5%" and "10.983s". The caption "SCaRe-Kro" matches the print.
- Table 2 (p. 18, 300 dpi): all 3 header cells and 33 data cells match, with every digit.
- Algorithm 1 (p. 17, 260 dpi): the title, Input and Output, the four blue "//" section comments and lines 1-10 match line
  by line. Line 9 carries the comment "// 4. combine to obtain CKRS, and return" on the same line, as printed.
- Figure crops: all 12 figures and algorithm-1.jpg are complete on all four edges, with tick labels, axis labels and
  legends, and no caption text inside. Figure 12's tiny tick labels are present at about 170-dpi-equivalent resolution;
  they are legible in outline only, but nothing is cut. At 170 dpi, some thin legend line colours look different between
  the page render and the assets (Figure 10 legend). A 260 dpi crop shows the asset is right (green and orange lines).
- reading_order: Figure 2 sits after the end of 5.3. Figure 3 follows the "Pure CP" paragraph and Table 1 follows
  "Pure NNV". Figures 7, 8, 9, 10, 11 and 12 sit at the ends of 8.3.5, 8.3.6, 8.3.7 (both), 8.3.8 and 8.3.9, and
  Algorithm 1 at the end of 8.2. No sentence is broken by a float. In particular, the 8.3.6 paragraph, which the PDF
  interrupts with Figure 7 on p. 21, is continuous in the package. Every page and column break is joined correctly.
- Conversion-notes slips: I checked each listed slip against the page and every one is printed as stated: "We are a
  planner P"; "lifting function g"; the extra "}" in X_{0:T}; the missing ")" in Problem 1; "space.The"; "a CG the
  describes"; "costs that increases"; "{z_0, z_2, ..., z_T}"; Lemma 1 X-hat_t; the unclosed f( in (9); "+ M"; "(8) and
  (9), respectively"; "via (7))"; "SCaRe-Kro"; "13-link"; 8.2 without hat or overline; "cos φ·sin φ"; "the the";
  "Figure 6 illustrate"; "with with"; and the Figure 9 caption with four panels. I also confirmed: the underlined letters
  Sca/Re/K/r/o (p. 2, 260 dpi); the degree signs in the text layer of pp. 23-24 (15 and 38 lines); no panel letters in
  Figure 1; "(a)-(d)" in Figures 8 and 9; no footnote for the asterisk; page 28 blank apart from the header.

## Coverage
- Theorem-like blocks: 7 statements (Proposition 1, Problems 1-2, Lemma 1 ×2, Theorem 1 ×2) plus 2 proofs, each checked
  symbol by symbol on 260 dpi crops. Run-in titles and numbers are correct.
- Displays: 22 (15 numbered: (1a), (1b), (2)-(14); 7 unnumbered: the CP coverage bound, the two Lemma-proof displays,
  the Theorem 1 probability bound in 8.1, and the Step 1, event-E and Step 3 displays). All are at 260-300 dpi, and every
  tag is on the right equation.
- Algorithm: 10 numbered lines, 4 comment lines and the Input/Output blocks.
- Table cells: 102 (Table 1: 66; Table 2: 36).
- Figures: 12, plus the Algorithm 1 image. All captions are verbatim with correct numbers.
- Completeness: a word-sequence diff of pdftotext against paper.md (math stripped) shows no dropped or duplicated prose.
  Every difference is page furniture, figure-internal text, hyphenation or math. A number-sequence diff found nothing in
  prose. The references were checked by word diff and number diff: 40 entries, all numbers identical.
- Prose read word for word against the render: pp. 1-12 and 15-22 (at least two full paragraphs per page, inline math
  checked). Pp. 13-14 (references) were checked by script plus a visual look at p. 12. Pp. 23-27 are float pages and
  p. 28 is blank.
- Headings and index: all 27 index headings exist exactly once in paper.md, and "Document beginning" belongs to
  supplement.md. Numbering and nesting (##/###/####) match the PDF. The index descriptions are accurate.
- Q1 "How are λ_{t,j} and the final bound ē_{t,j} computed?" Path: SKILL.md, then index, then 5.4. Answer: λ = 1/(e^max + σ)
  from D_N; C is the p-th smallest score with p = ⌈(K^cal+1)(1−δ)⌉; ē = C/λ. This matches PDF p. 8.
- Q2 "3D quadcopter online runtime and log volume vs the NNV-only baseline?" Path: index, then Table 1 and "3D Quadcopter".
  Answer: 0.675 s total and −42.954 online log volume, against 2153.45 s and −30.32 for the baseline. This matches
  PDF pp. 10-11.
- Not checked: claims I cannot test from the PDF (byte-identity with the arXiv download, the "471 math snippets" script
  check, the class name, the bib-key provenance). Figure values beyond the notes' summary were not digitised.
