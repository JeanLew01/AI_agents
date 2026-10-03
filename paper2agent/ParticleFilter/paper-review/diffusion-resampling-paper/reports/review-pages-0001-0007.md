# Review report: Diffusion differentiable resampling, PDF pages 1-7

Reviewer range: pages 1-7 of `documents/s001-diffusion-resampling` (TeX source used: `tex-source/diffusion-resampling/main.tex`, macros from `zmacro.tex` expanded).

## Per-page log

### Page 1 (reviewed, [v2])
- Items: title `#` heading, author line, affiliation/correspondence footnote, ICML Proceedings notice (kept), `## Abstract`, abstract, `## 1. Introduction`, 4 Introduction paragraphs.
- Equations: (1) as `$$...\tag{1}$$` (converted from formula image `formula-p0001-007`, asset name dropped).
- Joins: equation (1) and "for any bounded ..." `space`; right-column "& Papaspiliopoulos, 2020). ..." `space` onto "Resampling is a key component ... (SSMs, Chopin".
- Omitted: rotated arXiv stamp, page number.
- Repairs: Ścibior accent; all inline maths rewritten in LaTeX. Author typos kept: "combing", "reparapemtrisation".
- Remaining diagnostics: 15 missing lines (inline maths, category a); number difference `7` = mapsto glyph (category a). Adjudication note written.

### Page 2 (reviewed, [v2])
- Items: 4 Introduction paragraphs, 3 contribution bullets, "See Table 20 ..." line, `## 2. Diffusion differentiable resampling`, Section 2 opening, footnote 1, last paragraph (continues on page 3).
- Equations: (2), (3), (4) as `$$...\tag{}$$` (formula images removed; extractor split (4) into two formula items, merged).
- Joins: (2)/(3)/(4) and their continuations `space`. Footnote 1 placed before the last paragraph, marker `[^1]` after "reverse-time SDE".
- Repairs: "non-linear", "forward-time" (real compound hyphens at line ends restored).
- Remaining diagnostics: 20 missing lines, all maths (category a); no number differences.

### Page 3 (reviewed, [v2])
- Items: continuation of the page-2 paragraph (`space`), eqs (5)-(8), `**Remark 1.**` (with eq. (7)), `### 2.1. Differentiable sequential Monte Carlo`, Algorithm 1.
- Algorithm 1: figure `algorithm-1` (crop [297,66,546,261], top/bottom rules and line numbers inside) + line-by-line transcription item `p0003-alg1-text`. Placed after "We summarise ... Algorithm 1" paragraph and before Remark 1 (it sits at the top of the right column, where Remark 1 would otherwise be interrupted).
- Joins: first item `space` to page 2; (5)/(6)/(7)/(8) and their "where ..." continuations `space`. Last item ends "Take an SSM with state tran" (line-wrap hyphen removed); page 4 continues with `none`.
- Remaining diagnostics: 37 maths lines; numbers: minus glyph and algorithm-transcription indices (category a).

### Page 4 (reviewed, [v2])
- Items: "sition ..." (`none`, completes "tran-sition" from page 3), Algorithm 2, two paragraphs of 2.1, `### 2.2. Mean-reverting Gaussian reference`, `### 2.3. Exponential integrators`, eqs (9)-(12) and the unnumbered transition display.
- Algorithm 2: figure `algorithm-2` (crop [42,178,294,480]) + transcription `p0004-alg2-text` (lines 1-16). Extractor's caption text + two formula fragments replaced. Typo "Feyman–Kac" (Inputs line) kept.
- New item `p0004-b011a` (prose line "whose forward transition required in Equation (6) is" split out of the (10) formula box).
- Joins: left->right column "where $\mu_N$ ..." -> "and $\Sigma_N$ ..." `space`; every equation and its continuation `space`. Page ends with eq. (12); page 5 joins with `space`.
- Remaining diagnostics: 43 maths lines; numbers = minus glyphs and algorithm-transcription indices (category a).

### Page 5 (reviewed, [v2])
- Items: end of Section 2.3 (two exponential integrators, unnumbered), `## 3. Convergence analysis`, recalled (4) (unnumbered), eq. (13), `**Assumption 1 (Diffusion conditions).**`, `**Assumption 2 (Ensemble score condition).**` (each with its unnumbered display), last paragraph continues on page 6.
- New items `p0005-b016a` (prose split out of a formula box) and `p0005-b019a` (Assumption 2 split from the end of Assumption 1).
- Joins: first item `space` to eq. (12) on page 4; all display continuations `space`; left->right column "... by" -> "$q_t=p_{T-t}$ ..." `space`. Last item "Typically, the Monte" continues on page 6.
- TeX vs PDF: PDF cites "Øksendal (2007, ...)" (TeX key Oksendal2003); PDF kept.
- Remaining diagnostics: 43 maths lines; numbers = minus glyph and mapsto `7` (category a).

### Page 6 (reviewed, [v2])
- Items: continuation "Carlo order is ..." (`space`), `**Proposition 1.**` + bound + tail, `**Proof.** See Appendix B. $\square$`, `**Corollary 1.**` + bound + tail, `**Proof.** See Appendix C. $\square$`, `**Remark 2.**`, two paragraphs, `## 4. Experiments`, `### 4.1. Gaussian mixture importance resampling`, last line "Table 1 shows that the diffusion resampling at $K=128$" (continues on page 7).
- Equations: Proposition 1 and Corollary 1 bounds (unnumbered) as `$$` blocks.
- Repairs: "Gumbel-Softmax" hyphen restored; URL as code.
- Remaining diagnostics: 30 maths lines; numbers = minus glyphs, mapsto `7`, "10, 000" maths comma (category a).

### Page 7 (reviewed, [v2])
- Order: "gives the best SWD ..." (`space`, continues page 6), Figure-1 timing paragraph, then floats (Table 1 caption + `table-1`, `figure-1` + caption, Table 2 caption + `table-2`), `### 4.2. Linear Gaussian SSM`, text, eq. (14), three paragraphs; the last ("... The reason is due to the quasi-Newton optimiser") continues on page 8.
- Tables: `table-1` (9x3), `table-2` (10x4), re-typed from crops and checked against main.tex; asset names renamed from `table-p0007-002/004`. Printed bold best values (lost in CSV) are recorded in the page notes.
- Figure 1: `figure-1` (renamed from `figure-p0007-006`), crop [52,245,294,379] with both panels, legends, y label, bottom and top axes.
- Equation (14) as `$$...\tag{14}$$`.
- Remaining diagnostics: 23 maths lines; numbers = minus/plus glyphs, "8, 192" maths comma, norm exponent/subscript (category a); second parser glues bold table cells.

## Summary

- Final state: pages 1-7 all `reviewed: true`, notes start with `[v2]`; `check` reports ATTENTION on every page, and every remaining diagnostic is category (a) (LaTeX maths vs PDF glyphs, minus/mapsto glyphs, algorithm-transcription indices, maths-mode thousands commas). Adjudication notes are in `adjudication-notes/page-0001.json` ... `page-0007.json`.
- Assets: `algorithm-1` (p3), `algorithm-2` (p4), `table-1`, `table-2`, `figure-1` (p7). No formula images are left: every displayed equation on pages 1-7 ((1)-(14) and the unnumbered displays) is LaTeX taken from main.tex and checked against the page.
- Theorem-like labels: **Remark 1.** (p3), **Assumption 1 (Diffusion conditions).** and **Assumption 2 (Ensemble score condition).** (p5), **Proposition 1.**, **Proof.** x2, **Corollary 1.**, **Remark 2.** (p6). Footnote 1 on p2 (`[^1]` marker).
- Headings: `#` title; `##` Abstract, 1., 2., 3., 4.; `###` 2.1, 2.2, 2.3, 4.1, 4.2.

## Range boundaries
- Page 1 has no incoming join (start of the paper).
- **Page 8 (other reviewer):** page 7 ends mid-sentence with "... The reason is due to the quasi-Newton optimiser"; the first non-omitted item on page 8 (`p0008-b007`, "L-BFGS-B which heavily depends ...") needs `"join_previous": "space"`. It was not set when I looked; I did not edit page 8.

## TeX vs PDF disagreements (PDF kept)
- p3: citation printed "Zhao et al., 2025" (TeX key `Zhao2024rsta`); p5: "Øksendal (2007, ...)" (TeX key `Oksendal2003`). These are only bibliography-key/year labels; the printed text was kept.
- No mathematical disagreements found.

## Author typos kept verbatim
"combing Fisher's score", "reparapemtrisation" (p1); "Feyman–Kac model" in the Algorithm 2 Inputs line (p4); eq. (11) is printed "dU(t) = A U(t) + f(U(t), t) dt + ..." (no bracket/dt for the linear drift term) (p4); "Remark 2 show", "not superior than", "the needs for fine discretisation is" (p6/p7).

## Proposals for shared files
- `plan.json` title is the placeholder "diffusion-resampling"; propose "Diffusion differentiable resampling" (the page-1 `#` heading is that text).
- Plan note proposal: "In Tables 1 and 2 the authors set the best value of each column in bold, which the CSV cannot hold: Table 1 SWD 0.80 (Diffusion T=3, K=128), resampling variance 3.41 (OT eps=0.6 and eps=0.9); Table 2 2.55 and 4.26 (Diffusion T=3, K=8), 1.28 (Diffusion T=1, K=4)."
- Plan note proposal: "'Table 20' cited on pages 2 and 7 is the appendix comparison table of differentiable resampling schemes."
- Asset names: the extractor's `table-p0007-002`, `table-p0007-004`, `figure-p0007-006` were renamed to `table-1`, `table-2`, `figure-1`; the later reviewers should use `figure-2` onwards and `table-3` onwards for the main-text floats (checked: no clashes at the moment).

## Limitations / brief feedback
- Theorem-style statements (Remark, Assumption, Proposition, Corollary) are printed in italics; they are transcribed upright with a bold label so that the LaTeX maths stays clean. Italic emphasis words in the prose (*resampling*, *as is*, *computed*, ...) are kept.
- Algorithm transcriptions use `**n**&ensp;` line numbers and `&emsp;` indentation, following the Reachability sibling (sartipizadeh2019voronoi).
- The brief's self-check pattern `** **` flags `**1** **for**`; I used `**1**&ensp;**for**` to avoid it.
