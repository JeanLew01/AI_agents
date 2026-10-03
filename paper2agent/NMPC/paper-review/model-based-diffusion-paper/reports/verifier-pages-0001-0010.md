# Verifier report: Model-Based Diffusion (MBD), PDF pages 1-10

- Package: `/home/jixia/AI_agents/paper2agent/NMPC/staging/model-based-diffusion-paper-s1`
- Document: `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/model-based-diffusion-paper/documents/s001-model-based-diffusion`
- Range: PDF pages 1-10 = `references/paper.md` lines 1-297 (everything before reference [2]), plus `SKILL.md`,
  `references/index.md` (all rows), `references/supplement.md` and the conversion notes (paper.md lines 1145-1152).
- Scratch: `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/_scratch/verify-mbd-1-10/`
- Result: **0 errors, 10 minor findings.** Nothing was changed in the package or the plans.

## Coverage (what was actually done)

Nothing was sampled inside the page range; every item below was checked in full.

| Check | Method | Pages |
| --- | --- | --- |
| Prose, word by word | Token diff of `pdftotext` output of pages 1-10 against paper.md lines 1-297, once case/punctuation-insensitive (`wdiff.py`) and once case- and punctuation-sensitive (`pdiff.py`); every non-math difference read | 1-10 |
| Display equations (1a)-(13), 22 tagged blocks | Each compared symbol by symbol with crops at 220-400 dpi | 3-8 |
| Inline mathematics, 161 spans | Read next to the same crops (all spans, not only definitions) | 1-10 |
| LaTeX well-formedness | Script: `$` parity, braces, `\left`/`\right`, `\begin`/`\end`, tag sequence | 1-10 |
| Tables 1-3 | Table 1 read cell by cell against a 230 dpi crop; Tables 2-3: script comparing every CSV cell, every Markdown-table cell and the PDF native text (`tabcheck.py`), then read once more against 300 dpi crops | 6, 9 |
| Algorithms 1-2 | JPEG versus PDF crop versus transcription, line by line | 7, 8 |
| Figures 1-4 | Each JPEG opened: completeness, no caption/body text inside, legibility; captions via the token diff | 1, 5, 9, 10 |
| Footnotes 1-3 | Marker position and text | 3, 6, 8 |
| Headings | Text and level against the page images; heading font heights measured on page 10 | 1-10 |
| Reference [1] | Character by character | 10 |
| index.md | Script: every row's heading looked up in paper.md; the section that actually contains each `\tag`, figure, table and algorithm compared with what the row promises (all rows, including the appendix rows) | all |
| Conversion notes, SKILL.md, supplement.md | Read once; each verifiable claim checked against the PDF | all |

Not verifiable from the PDF (so neither confirmed nor disputed): the notes' statements that the mathematics was "taken from
the authors' arXiv v1 TeX source where it matches", which passages are camera-ready-only, and that reader highlights were
removed from the user's copy.

## Findings

| # | Severity | PDF page | Item id | Package says | PDF shows | Suggested fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | minor (systematic) | 6 | p0006-b002 (paper.md line 148) | In the Markdown rendering of Table 1 the backslashes are doubled: `$p_0(\\cdot)$`, `$Y^{(0)} \\sim p_0(\\cdot)$`. The CSV (`assets/table/table-1.csv`) and the page plan have the correct single backslash, so the builder adds it. Same pattern in every Markdown table with maths outside my range: lines 436-441 (A.1), 723 (Table 4 header), 768-775 (Table 6). | `p_0(·)` and `Y^(0) ~ p_0(·)` | In the builder, do not escape backslashes inside `$...$` in table cells (keep escaping the pipe only). Renderer-dependent: a strict CommonMark renderer turns `\\` back into `\`, a MathJax/KaTeX renderer shows a line break followed by the word "cdot"/"sim", and a reader of the raw text sees LaTeX that is inconsistent with the rest of the file. |
| 2 | minor | 5 | p0005-b008 (line 127) | Denominator of the inline Gaussian density is `1-\bar{\alpha_i}` (bar over the subscript as well) | `1 - \bar{\alpha}_i`, bar over alpha only, as everywhere else | Replace by `1-\bar{\alpha}_i` |
| 3 | minor | 7-8 | p0008-b000 / p0008-b001, index row "4.2" | index.md promises "Algorithm 2" under 4.2, but in paper.md the Algorithm 2 block (lines 199-209) is under `### 4.3`, after its first paragraph | Algorithm 2 is a float printed at the top of page 8 (inside the 4.3 text) but belongs to 4.2, which cites it ("Line 3 in Algorithm 2") | Either move the block to the end of 4.2 (line 193), or move "Algorithm 2" to the 4.3 row of the index |
| 4 | minor | 9 | p0009-b006 / p0009-b007, index row "5.2" | index.md promises "Figure 4" under 5.2, but paper.md has Figure 4 (lines 271-273) before the `### 5.2` heading, i.e. inside 5.1 | Figure 4 is printed at the bottom of page 9 (inside the 5.1 text) and is cited only in 5.2 (Fig. 4(a), Fig. 4(b)) | Move the Figure 4 block after the first paragraph of 5.2, or list Figure 4 in the 5.1 row |
| 5 | minor | 21-22 (outside my range, found through the index) | index row "A.5.3" | index.md promises "RL settings, Tables 5-6" under A.5.3, but paper.md has Tables 5 and 6 under `#### A.5.4` (lines 749-777) | Both tables are printed on page 22 after the A.5.4 text (Table 6 after the A.6 heading); they are the RL settings that A.5.3 describes | Move both tables to the end of A.5.3, or change the index rows (A.5.3: "RL settings"; A.5.4: "RRT and mocap demonstration data, Tables 5-6") |
| 6 | minor | 3 | p0003-b011 | "Footnote 1: ..." sits between equation (1d) and the continuation "where $x_t \in \mathbb{R}^{n_x}$ ...", interrupting the sentence | Footnote is at the page bottom; "where ..." follows the display directly | Move the Footnote 1 item above the display (after p0003-b005, same page), next to its marker |
| 7 | minor | 1 | p0001-b008 | The page-1 footer "38th Conference on Neural Information Processing Systems (NeurIPS 2024)." is a body paragraph between the Figure 1 caption and the second paragraph of the Introduction | Page footer, not part of the Introduction | Move it below the e-mail line of the front matter (it is already in the conversion notes) |
| 8 | minor | 10 | p0010-b008 | `## Acknowledgments` (same level as the numbered sections) | Unnumbered heading printed at subsection size: 8.96 pt glyph height, identical to "5.2 Data-augmented MBD ..."; "6 Conclusion ..." and "References" are 10.75 pt | Strictly `### Acknowledgments`; keeping `##` is defensible (it is not a part of Section 6) but then say so in the notes |
| 9 | minor | 9 | p0009-b000 | Table 2: no emphasis in CSV or Markdown, and the notes do not mention it | All seven cells of the MBD column are bold (best result per row) | Add a sentence to the conversion notes, or bold the MBD column in the Markdown table |
| 10 | minor | - | index.md, supplement table | Row "Document beginning" for supplement.md | supplement.md contains only `# Supplementary information` and "No corresponding materials were supplied."; there is no such heading | Template row; replace by "Supplementary information" or drop the table when no supplement exists |

Cosmetic observation, not counted: the transcriptions of Algorithms 1-2 are flat (lines 3-6 and 3-7 are not indented under
the `for`); the loop is still unambiguous from "for ... do / end for".

## Checked and found correct

**Page 1.** Title, author line with `*`/`dagger` markers, affiliation, e-mail, abstract (bold-italic "without data" and
"model-based", URL), heading "1 Introduction", first paragraph reconstructed correctly from the text wrapped around
Figure 1, citation list [12, 54, 34, 33, 40, 5]. `figure-1.jpg` complete (model box, forward/backward formulas,
"Trajectory" label, humanoid strip and its in-figure label), caption text exact.

**Page 2.** Two paragraphs and three contribution bullets word for word ("59%"), heading "2 Related Work", the three run-in
paragraphs with their citation numbers. The sentence crossing pages 2-3 ("... commonly used to solve TO / problems, where
...") reads continuously.

**Page 3.** Rest of Related Work including the Langevin paragraph: `p ∝ exp(-J/λ)`, `O(1/ε² log(1/ε))`, `O(1/ε)`.
"Notations" paragraph. Equations (1a)-(1d): min subscript `x_{1:T}, u_{1:T}`, sum from `t=0` to `T-1`, "s.t." on (1b),
trailing comma on (1c); **(1d) reproduced with the printed stray "3" (`T-1.3`), as the notes state**. Footnote 1 text
exact, marker `[^1]` with the printed spaces. Domains of `f_t`, `g_t`, `l_t` (`n_x`, `n_u`, `n_g`).

**Page 4.** Sentence crossing pages 3-4 ("... are the stage / costs.") continuous. `Y = [x_{1:T}; u_{1:T}]`; `p_d`, `p_J`,
`p_g` definitions (products from `t=1` to `T`, indicator bold 1, `f_{t-1}(x_{t-1}, u_{t-1})`). Equation (2) without
punctuation. Forward kernel `N(sqrt(α_i) Y^(i-1), (1-α_i) I)` without bars. Equation (3): bars on both alphas, product
`k=1..i`, final period. Equations (4) (trailing comma) and (5) (product from `i=N` to `1`, `dY^(1:N)`). Heading
"4 Model-Based Diffusion" and its paragraph.

**Page 5.** Heading 4.1 (level 3), `figure-2.jpg` complete (three panels, tick labels, legend, colour bar), caption exact.
Equation (6): `1/sqrt(α_i)` without bar, `(1-\bar α_i)` with bar. (7a) both fractions, (7b) numerator
`-(Y^(i) - sqrt(\bar α_i) Y^(0))/(1-\bar α_i)`, (7c). Inline density and its gradient (apart from finding 2).
Equation (8): inner fractions `Y^(i)/sqrt(\bar α_i)`, denominator `(1-\bar α_i)/\bar α_i`, covariance `I/\bar α_i - I`.

**Page 6.** (9a); (9b) with the underbrace "Monte Carlo Approximation", `:=`, `\bar Y^(0)(𝒴^(i))` and sums over
`Y^(0) ∈ 𝒴^(i)`. Table 1: header and all 4 rows x 3 columns, including "(Eq. (9a))", "(Eqs. (11) and (13))",
"(Eq. (6))"; caption exact. Comparison paragraph: reverse-SDE formula (`(1-α_i)/2`, `sqrt(1-α_i) z_i`, bold z),
`∇ log p_i ≈ -1/(1-\bar α_i) (Y^(i) - arg max p_i(·))`, marker `[^2]`, "[64]". Footnote 2 exact (no final period, as
printed). "How diffusion helps?": `p_N ~ N(0, I)`, `\bar α_N → 0`, `Σ_{φ_i} = (1/\bar α_i - 1) I`, `\bar α_i → 1`.
CEM paragraph checked at 400 dpi: `\bar α_1/α_1`, `α_0` without bar in `N(Y^(1)/α_0, (1/α_0 - 1) I)` and in `Σ_CEM`,
all as printed.

**Page 7.** `algorithm-1.jpg` complete; transcription lines 1-7 identical to the image (line 3 uses `\bar α_{i-1}` under
the square root and in the covariance, line 5 `≈`, line 6 `←`). End of the CEM paragraph (`p_20, p_100`, `p_1`).
Heading 4.2; (10a) factor order `p_d p_g p_J`, (10b) sums over `𝒴_d^(i)` with `p_J p_g`, (10c) trailing comma, (10d)
"where" and `w = p_J p_g`. Following paragraph (`U = u_{1:T}`, `Y_d^(0)`, Line 3/4/5, Eq. (1c), [29]). Heading 4.3 and
the first half of its paragraph.

**Page 8.** Sentence crossing pages 7-8 ("sampling pro-/cess") continuous. `algorithm-2.jpg` complete; transcription lines
1-8 identical to the image. `p_demo(Y^(0)) ∝ p(Y_demo | Y^(0)) ∝ N(Y^(0) | Y_demo, σ² I)`. Marker `[^3]`; printed typo
"seperating" kept. (11) prime on `p'_0`, `(1-η)` and `η`; (12) `<` and `≥` cases, final period; (13) max over the two
stacked terms, comma and final period. Footnote 3 exact. Section 5: 59%, 10%, 23%, 800d, [23, 18, 56, 42, 41, 44], 28K,
86%, 2s, [2], 93%, 9.6%, italic "gradient-free". Heading 5.1.

**Page 9.** Sentence crossing pages 8-9 continuous. Table 2: 7 rows x 6 columns, all values and uncertainties, the two
negative entries (−0.13, −0.63), header "RL*", caption with the asterisk note. Table 3: 7 x 6, all durations including
"17 m 45.63 s", "4 m 29 s", "67 m 25.6 s". CSV = Markdown table = PDF for every cell. Paragraph of 5.1: [7], [11], [59],
[47], [22], [20], "RTX 4070 Ti", "50 steps repeated for 8 seeds", the printed garbled sentence "not as there is no
existing TO method" kept as printed. `figure-4.jpg` complete (both panels, legends, axis ticks), caption exact.

**Page 10.** `figure-3.jpg` complete (panels a-c, arrow, "i = 0", "i = N", "Model-based Diffusion"), caption exact. Heading
5.2 and its three paragraphs ([38], Fig. 4(b), [26, 45], [1], Fig. 4(a)). "6 Conclusion and Future Work".
Acknowledgments: "NSF Grant 2154171, NSF CAREER 2339112 and CMU CyLab Seed Funding." Heading "References"; entry [1]
character by character.

**LaTeX.** 22 display blocks, 161 inline spans: `$` parity, braces, `\left`/`\right`, `\begin`/`\end` all balanced; tags
run (1a), (1b), (1c), (1d), (2)-(6), (7a)-(7c), (8), (9a), (9b), (10a)-(10d), (11)-(13) without gap or duplicate. No
`<sup>`, glyph soup, stray `_`/`**` or split decimals in the range.

**index.md.** All 29 paper rows name a heading that exists exactly once in paper.md; the only paper.md headings not
indexed are the title and "Conversion notes". Equation ranges promised per row match the tags found in those sections
((1a)-(5) in 3; (6)-(9b) in 4.1; (10a)-(10d) in 4.2; (11)-(13) in 4.3; (14a)-(28) in A.2; (29)-(32) in A.4). "64 entries"
and "15 checklist items" confirmed by count. The three float-location mismatches are findings 3-5.

**Conversion notes.** Page ranges confirmed (references end with [64] on page 14, appendix starts on page 15, checklist
heading on page 24, Figure 9 on page 25). Stray "3" in (1d), headings "Abalation" (A.7, A.8) and "Explaination" (A.4),
`[^n]` convention, algorithms as image plus transcription, LaTeX in the Table 1 CSV, uncoloured "data augmentation" in
the Figure 4 caption, underlined initials in the abstract not represented: all true. Nothing false found.

**SKILL.md / supplement.md.** Name and description match the paper; supplement.md states that no materials were supplied.

Printed peculiarities that the package reproduces faithfully (not package errors): Algorithm 1/2 line 3 samples with
`\bar α_{i-1}` while equation (8) defines the proposal with `\bar α_i`; the CEM paragraph uses `α_0` and `\bar α_1/α_1`.

## Technical question answered from the package only

**Question.** In MBD for trajectory optimisation, how is the sample for diffusion step i-1 computed from Y^(i), and how
does a demonstration change the computation? For Push T, how do MBD and RL compare in reward and time?

**Answer from the package** (paper.md, "4.2 Model-based Diffusion for Trajectory Optimization", the Algorithm 2 block and
equations (11)-(13) in "4.3 Model-based Diffusion with Demonstration", Tables 2-3 in "5.1"):
1. Sample a batch `𝒴^(i) ~ N(Y^(i)/sqrt(\bar α_{i-1}), (1/\bar α_{i-1} - 1) I)` (Algorithm 2, line 3).
2. Roll the control part `U = u_{1:T}` through the dynamics (1c) to obtain dynamically feasible samples `𝒴_d^(i)` (line 4).
3. `\bar Y^(0) = Σ Y^(0) w(Y^(0)) / Σ w(Y^(0))` over `𝒴_d^(i)`, with `w = p_J(Y^(0)) p_g(Y^(0))` in the model-only case
   (10d), or `w = max{ p_d(Y^(0)) p_J(Y^(0)) p_g(Y^(0)), p_demo(Y^(0)) p_J(Y_demo) p_g(Y_demo) }` with a demonstration
   (13), where `p_demo(Y^(0)) ∝ N(Y^(0) | Y_demo, σ² I)`; this corresponds to η = 1 when the demonstration term is larger
   and η = 0 otherwise (12).
4. Score `≈ -Y^(i)/(1-\bar α_i) + sqrt(\bar α_i)/(1-\bar α_i) \bar Y^(0)` (10c), then
   `Y^(i-1) = (1/sqrt(α_i)) (Y^(i) + (1-\bar α_i) score)` (6).
5. Push T: reward 0.67 ± 0.10 for MBD against −0.63 ± 0.16 for RL; time 10 m 32.8 s against 67 m 25.6 s.

**Check against the PDF.** Pages 7-9 (Algorithm 2, equations (6), (10c), (10d), (12), (13), Tables 2-3): every formula
and number above is as printed. The answer is complete only because the reader continues from 4.2 into 4.3 to find
Algorithm 2 (finding 3).
