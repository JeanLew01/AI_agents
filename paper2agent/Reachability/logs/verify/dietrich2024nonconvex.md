VERDICT: clean

# dietrich2024nonconvex - independent verification

Package: `skills/dietrich2024nonconvex-paper` (SKILL.md, references/index.md, references/paper.md,
references/supplement.md, assets/figure x5, assets/table x2).
Ground truth: `papers/dietrich2024nonconvex.pdf` (14 pages, single column). No TeX source exists
for this key, so every comparison below is package vs. rendered page.

## Findings

None. No A, B or C item was confirmed on a render.

Every symbol, number, label and caption I compared agrees with the PDF. The places where the
package looks wrong at first reading are all printed that way in the PDF (confirmed at 300 dpi
unless noted) and are therefore not findings:

- Sec. 2, "$\delta^{(1)}, ...\delta^{(N)}$" (no comma) and "(i.i.d)" - p.2.
- Before (4), "We know $s_N^* < d$" while the first case of (4) is "$s_N^* \ge d$"; upright "d" in
  "with d optimization variables" - p.3.
- Sec. 3, $\mathcal{R}$ for both the reachable set and its approximation; "from state
  $\mathcal{X}_0$"; italic $R = \Phi(t_1; t_0, X_0, D)$ - p.3.
- (6), subscript $i$ on $\theta_i$ inside the set - p.4.
- Sec. 3.1, "$A_i \cap A_j = \emptyset\ \forall i$", $\mathbb{R}^D$; (9) ends with a comma - p.4.
- (10), left side $f(x,\mu,\sigma)$ with $\mu_i$, $\sigma_i$ in the exponent - p.5.
- (12), constraint "$\ge 0$" (opposite to the "$\le 0$" of (5)), comma after $N$, no final
  punctuation - p.6.
- Algorithm 1: $\Phi$ in line 1 but $\phi$ in line 8; "iff $\theta = 0$"; same index $i$ for
  sample and cell in line 9 - p.5.
- Algorithm 2: "$\mu_i, \ldots, \mu_m$" in lines 2 and 23; single exponential in lines 11 and 18
  (line 11 re-checked at 450 dpi); line 21 "If $\Sigma_i = \Sigma$, then $S = S + 1$" - p.7.
- "a Apple M2 Pro"; "46, 052"; ".01"; Duffing dynamics as one equation in $\ddot{x}$ with states
  $x, y$; "$[-5,5]$ x $[-5,5]$", "20x20" - pp.6-7.
- Italic $sin$, $cos$ in (13); closing quotes on both sides of "one in a billion"; "a-posterior"
  in both table captions; "positon" in the Figure 3 caption - pp.8-10.
- Sec. 4.1.2 prints $s_N^* = 19$ with $\epsilon = 0.1182$; Sec. 4.2.1 prints $s_N^* = 19$ with
  $\epsilon = 0.1125$ - pp.8-9.
- References: "Systems Control Letters", "Hamilton-jacobi" (Bansal), "Hamilton–jacobi" with en
  dash (Chen and Tomlin), "hamilton-jacobi" (Mitchell 2005), "christoffel", "gaussian",
  "monte carlo", "07 – 08 June 2021", "60(1):265 – 270" - pp.11-13 at 250 dpi.

Conversion notes: every "kept as printed" item in the last notes bullets was checked against the
page and is really printed that way. Two further factual claims in the notes were checked
independently and hold:

- "In the header 'Run Time of (1)/(2)' the numbers ... refer to Algorithms 1 and 2": the PDF link
  destinations were extracted from the file; `algorithm.1` / `algorithm.2` are each targeted two
  more times than the in-text "Algorithm n" references account for, and `equation.0.2.1` /
  `equation.0.2.2` are fully accounted for by in-text references, so the table-header links go to
  the algorithms, not to equations (1)/(2).
- Reviewer's numerical check: recomputed with $N = 1000$, $\beta = 10^{-9}$: (4) with
  $s = 67$, $d = 400$ gives 0.25091; (2) with $s = 22$ gives 0.12527; (4) with $s = 19$,
  $d = 100$ gives 0.11249; (2) with $s = 20$ gives 0.11819 and with $s = 19$ gives 0.11457.
  All as the note states.

## Coverage

- Theorem-like blocks: 1 of 1 (Theorem 1, heading "Theorem 1 ((Campi et al., 2018), Theorem 1)",
  statement through (3)), symbol by symbol at 300 dpi.
- Displayed equations: 14 of 14 numbered displays, (1)-(14), each with its printed number, at
  300 dpi. The paper has no unnumbered displays.
- Algorithms: 34 of 34 lines (Algorithm 1: 11, Algorithm 2: 23) - numbering, nesting level,
  conditions, assignments, bold keywords - at 300 dpi; both image assets are complete boxes.
- Tables: 70 of 70 cells (2 tables x 7 rows x 5 columns, empty cells included), in both the CSV
  files and the Markdown copies in paper.md, at 300 dpi; headers, units ("1.70s" without space in
  Table 1, "6.28 s" with space in Table 2) and both captions.
- Figures: 3 of 3 assets (figure-1/2/3.jpg) show both panels with axes and tick labels, no
  caption or body text inside the crop; captions verbatim; numbers correct.
- Completeness and order: `pdftotext` of all 14 pages was aligned word by word with paper.md
  (math stripped on the package side). The only differences are the omitted banner, running
  headers and page numbers, the lower-cased e-mail addresses, the small-caps sub-subsection
  headings, and the moved floats (Figure 1, Algorithm 2, Figure 2, Table 1) exactly as the
  conversion notes describe. No dropped, duplicated or reordered passage; no sentence cut at any
  of the nine body page breaks. No footnotes and no appendix in the PDF.
- Prose: pages 1-10 read in full, not only two paragraphs each. Pages 2-10 at 300 dpi including
  all inline math; page 1 at 170 dpi plus the word alignment (it has no mathematics).
- References: 39 of 39 entries on pages 11-14 read at 250 dpi (authors, diacritics, titles,
  venues, volume(issue):pages, years, DOIs, URLs).
- Headings and index: 17 headings in paper.md, numbering and nesting as printed (4.1.1-4.2.2 are
  the small-caps sub-subsections); all 17 index.md entries exist with the exact heading text, and
  their "look here for" contents (equation numbers, figures, tables, algorithms) are in the
  sections named. supplement.md states only that no supplementary material was supplied, which
  agrees with the PDF.
- Question 1: "Which $\epsilon$ formula does each method use, and what was obtained for the
  Duffing tiling run with $N = 1000$?" From index -> 3.1, 3.2, 4.1.1, Table 1: tiling uses the
  convex refinement (4) with $d = m$ (Algorithm 1 line 10), RBF uses (2) (Algorithm 2 line 22);
  Duffing tiling on a 20x20 grid, $\beta = 10^{-9}$, 1.70 s, $s_N^* = 67$, $\epsilon = 0.2509$
  (0.251 in Table 1), Chernoff estimate .999966. Agrees with PDF pp.5, 7, 8, 9.
- Question 2: "What are the quadrotor parameters, initial set and horizon, and how long did the
  RBF method take at $N = 3000$?" From index -> 4.2, Table 2: $g = 9.81$, $K = 0.89/1.4$,
  $d_0 = 70$, $d_1 = 17$, $n_0 = 55$; initial intervals of (14); $u_1 \in [-1.5 + g/K, 1.5 + g/K]$,
  $u_2 \in [-\pi/4, \pi/4]$; $[t_0, t_1] = [0, 5]$; RBF at $N = 3000$: 5.5 hr, $\epsilon = 0.051$.
  Agrees with PDF pp.9-10.

## Not checked

- Page 1, the caption of Figure 1 and the first lines of the captions of Figures 2 and 3 were not
  rendered at 250 dpi or more (170 / 150 dpi plus text alignment); they contain no mathematics
  beyond $\gamma$ and $\mathbb{R}^2$.
- Figure assets were compared with the page for completeness and content, not pixel by pixel.
- The reviewer's statement about the render resolutions and the pdflatex compile of the
  transcription is a process claim and was not verified.
- Nothing under `paper-review/` was read. TMP renders are deleted.
