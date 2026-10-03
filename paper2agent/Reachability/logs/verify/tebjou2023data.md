VERDICT: 3 findings (0 A, 0 B, 3 C)

# Verification of tebjou2023data-paper against papers/tebjou2023data.pdf (PMLR v204, 20 pages)

No mathematical, factual, numbering, caption, order or completeness error was found. The
package text and formulas follow the PMLR PDF. The three findings are cosmetic; two of them
are in the conversion notes, not in the paper text.

Special-risk check (arXiv TeX vs PMLR PDF): I compared the package with the PDF pages
directly (crops, see coverage), and separately ran a word-level diff of
tex-source/tebjou2023data/main.tex against the package. The only place where main.tex and the
PDF differ in content is the display `f : R^n -> R^n` at the start of Section 2 (PDF has it,
main.tex does not); the package has the display, i.e. it follows the PDF. I found no place
where the package follows the TeX against the PDF.

## Findings

### C1 - conversion note mis-describes the arXiv TeX (package body is correct)
- Location: paper.md, "## Conversion notes", second bullet, snippet
  `where the arXiv TeX has it only in running text`.
- Package says: "(i) the PDF prints the transition function as a displayed formula,
  f : R^n -> R^n, at the start of Section 2, where the arXiv TeX has it only in running text".
- What is there: PDF p.3 prints the display `f : \mathbb{R}^n \rightarrow \mathbb{R}^n,`
  between "by a transition function" and "which maps a state x in R^n to its successor
  state." (confirmed, 260 dpi crop). main.tex lines 184-185 read "... by a transition
  function" / "which maps a state $\Vec{x} \in \mathbb{R}^{n}$ to its successor state." with
  no formula for f at all; the only `f : \mathbb{R}^... \rightarrow` in main.tex is
  `f : \mathbb{R}^2 \rightarrow \mathbb{R}^2` at line 284 (Example 1).
- So the PDF half of the note is right and the body of paper.md (Section 2, display
  `f : \mathbb{R}^n \rightarrow \mathbb{R}^n,`) is right; only the TeX half of the sentence
  is wrong: the arXiv TeX omits the formula, it does not have it in running text.
- Unsure: I assumed tex-source/tebjou2023data/main.tex is the arXiv v1 source the note
  refers to.

### C2 - binomials in (14) and in two proof displays are text-size in the PDF
- Location: paper.md "## 4. Robustness to Outliers", three displays with snippet
  `\sum_{i=p+1}^{N-p} \binom{N-p}{i} \epsilon^i (1-\epsilon)^{N-p-i}`: equation `\tag{14}`,
  the second line of the `aligned` display in the proof, and the display after
  "Using Theorem 2, we get :". PDF p.13.
- Package: `\binom{N-p}{i}` inside display math (renders display-size).
- PDF: small text-style binomial next to a display-size sum (confirmed, 260 dpi crops of
  p.13). `\tbinom{N-p}{i}` reproduces the print. Content is identical; typography only.

### C3 - one rounded number in the reviewer's numerical note
- Location: paper.md, "## Conversion notes", last bullet, snippet
  `18.1 / 33.9 / 50.9 / 92.3 for N = 100`.
- Package (reviewer's own check, not paper content): 92.3.
- Recomputed with python3 from equation (14) as printed, N = 100, p = 5, epsilon = 0.10:
  92.2496, which rounds to 92.2. Every other number in that bullet reproduces (see below).

## Check of the reviewer note on Table 1 and equation (14)

- Equation (14) in paper.md is the printed one: sum from `i=p+1` to `N-p` of
  (N-p choose i) eps^i (1-eps)^(N-p-i); same in the proof and in the Output line of
  Algorithm 2 (PDF p.13 and p.15, 260 dpi). Not altered.
- Table 1 in table-1.csv and in the Markdown copy is the printed one (PDF p.14, 260 dpi):
  100: 33, 51, 68, 96; 500: 10, 42, 77, 99.99; 1000: 3, 37, 84, 99.99;
  2000: 0.4, 31, 92, 99.99. Not altered.
- The note describes the PDF correctly. Recomputed with p = 0.05 N, in %:
  - sum from i = p+1 (as printed): 18.08 / 33.91 / 50.87 / 92.25 (N=100);
    6.90 / 34.62 / 71.24 / 99.986 (500); 2.29 / 32.12 / 81.17 / 100.00 (1000);
    0.29 / 27.78 / 90.57 / 100.00 (2000). These are not the printed entries.
  - sum from i = p: 33.13 / 51.81 / 68.05 / 96.66; 10.22 / 42.52 / 77.68 / 99.993;
    3.24 / 37.52 / 84.76 / 100.00; 0.405 / 31.35 / 92.16 / 100.00. Truncated, these are the
    16 printed entries, as the note says.
- Other numbers in the note also reproduce: 1 - 0.01^(1/N) = 0.0023 / 0.0228 / 0.0046 for
  N = 2000 / 200 / 1000; Example 4 gives 0.9897 (printed 98.9%); Conjecture 1 sample bounds
  10488 / 10335 / 9938 / 10489 for the four (d, epsilon) pairs of Figure 1.
- The note is placed in the conversion notes and labelled as the reviewer's check; nothing
  in the paper text, the table or the equation is changed by it.

## "Kept as printed" claims in the conversion notes (all confirmed on the PDF)

'Table 4' after the proof of Theorem 5 (p.13); 'Figure 9 illustrates how' in Section 5.1
(pp.16-17); 'For fixed d and n -> infinity' twice and 'in these sense of' twice (p.6);
thresholds `b_1, ..., b_n` twice and event `U_(N) <= b_n` (p.8); `C_D` instead of `C_Dcal`
in the conditional probability before Theorem 2 (p.8) and in step 2(c) of Algorithm 2
(p.15); `U_N` without parentheses in the proofs of Theorems 3 and 4 (pp.8-9); capital Pi
product (p.9); 'Combing (10) and (11)' (p.9); 'The reduces the cost' (p.12); subscripts
inlier / oulier / outlier / inliers and `V_i, ..., V_{N-p}` (p.13); 'otherwise. .' (p.15);
'provides ... and proposed', 'compared that the most relevant approaches' (p.18); italic S
and S-hat in Example 1 and under Table 2; varepsilon in sub-captions, in the captions of
Figures 1 and 9 and once in Example 1; `(0, 1/2)` in Theorem 4; `delta^{1/N}` in
Algorithm 1; 'N = 10 000' in Example 1. Block ends (italic bodies) and the three filled
squares are as the notes say. Float moves listed in the notes match the PDF page positions.

## Coverage

- Theorem-like blocks: 9 of 9 (Conjecture 1; Theorems 2, 3, 4, 5; Examples 1, 2, 3, 4) and
  the 3 proofs, symbol by symbol on 250-260 dpi crops; numbers and titles
  ("Thm. 1 in Devonport et al. (2021)", "Thm. 4 from Bates et al. (2023)", "Four squares")
  correct.
- Displays: 39 of 39 display blocks in paper.md (14 numbered, 25 unnumbered) against
  250-260 dpi crops; tags (1)-(14) each occur once and sit on the right equations.
- Algorithms: 18 lines (Algorithm 1: title, Input, Output, comment line, 1, 1(a), 1(b), 2,
  3, region display; Algorithm 2: title, Input, Output, 1, 2, 2(a), 2(b), 2(c)), 260 dpi.
- Tables: Table 1, 20 body cells + 6 header cells; Table 2, 90 body cells + 6 header cells,
  footnote and both captions, 260 dpi. CSV and Markdown copies agree with each other.
- Figures: 9 figure assets and 2 algorithm images opened; all panels, axes and
  sub-captions present, nothing cut, no foreign text; 9 captions verbatim, numbers correct.
- Prose: whole-document word-level diff of pdftotext against paper.md (math stripped): no
  dropped, duplicated or reworded passage; differences are only running headers, page
  numbers, moved floats, accents, line-break hyphens. No sentence is cut at a page break.
  Read by eye on all 20 pages: pp.4, 5, 6, 8, 9, 13, 15 fully at 250-260 dpi; p.3 at
  170 dpi plus a 260 dpi crop; pp.7, 10, 11, 12, 14, 16, 18 math, theorem, algorithm and
  table parts at 260 dpi and the rest at 130-150 dpi; pp.1, 2, 17, 19, 20 at 130-140 dpi.
- References: 19 of 19 entries present once, in order, text matches (pp.19-20).
- Headings and index: 17 of 17 index headings exist in paper.md with correct numbering and
  nesting; footnote 1 present once; math braces balanced in all 39 display and 362 inline
  formulas (python3 check, not a LaTeX compile).
- Question 1: "With up to p outliers in the calibration set, which threshold defines the
  set and what confidence results for N = 500, 10% outliers, epsilon = 0.15?" Via index ->
  "4. Robustness to Outliers": scores sorted in descending order, threshold `score_{p+1}`,
  region `C_D^{(p+1)/N}` (Algorithm 2, step 2); confidence at least the sum in (14);
  Example 4 gives 98.9%. Agrees with PDF pp.13-15.
- Question 2: "How is the transductive p-value computed without re-inverting the moment
  matrix, and at what cost?" Via index -> "3.2. Avoiding the Calibration Set": update (13)
  with `y^i = M_d^{-1} v_d(x^i)`; precomputation O(N s(d)^2), storage O(N s(d)), one
  p-value O(N s(d) + s(d)^2), against O(s(d)^3) per evaluation otherwise. Agrees with PDF
  pp.11-12.

## Not checked

- The statement in the notes that the paper is cited with volume pagination 194-213: it is
  not printed in the PDF (true), the pagination itself cannot be checked from the PDF.
- No pdflatex compile of the formulas; rendering was not tested.
- Bold-italic versus upright-bold versus plain type was checked in every display and
  theorem-like block, not for every inline symbol in running prose.
- Figure colours and plotted data were compared by eye only; hyperlink targets not checked.

## Housekeeping

The run was interrupted once by a machine restart; pages 14-20, the tables, Algorithm 2,
the assets and the notes were checked after the restart, pages 3-13 before it (their
results were in my context and are included above). All my renders and helper files in
logs/verify/work/tebjou2023data/ are deleted; the empty directory is left. Nothing outside
this file and that directory was written.
