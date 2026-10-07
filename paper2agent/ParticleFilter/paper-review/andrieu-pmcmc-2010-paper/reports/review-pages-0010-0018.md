# Review report: Andrieu, Doucet, Holenstein (2010), PDF pages 10-18

All nine pages are `reviewed: true` with `[v2]` notes. No TeX source; all maths transcribed from 220-400 dpi crops.
Scratch (scripts `p10.py` ... `p18.py`, crops): `paper-review/_scratch/andrieu-10-18`.

## ACTION NEEDED BY THE COORDINATOR: plan.json `reading_order` for two full-page rotated figures
Pages 14 (Fig. 5) and 18 (Fig. 6) each consist of one rotated full-page figure placed in the middle of a paragraph
that runs from the page before to the page after. A reviewer cannot fix this inside the page files.
- Paragraph `p0013-b004` ("When θ is unknown ... is the inverse") continues in `p0015-b001` ("gamma distribution ..."),
  which has `join_previous: "space"`. In file order the item before `p0015-b001` is the Fig. 5 caption `p0014-b002`.
  `reading_order` must move `p0014-b001`, `p0014-b002` (suggested: directly before `p0013-b004`, i.e. after the Fig. 4
  caption `p0013-b002`; or after `p0015-b003`, the paragraph that discusses Fig. 5). Without this the paragraph would be
  glued onto the Fig. 5 caption.
- Paragraph `p0017-b005` ("Gander and Stephens (2007) proposed ... the PMCMC methodology") continues on page 20
  (owner: reviewer 19-27), because page 19 is another full-page rotated figure (Fig. 7: `p0019-r02`, `p0019-r03`).
  Page 20's continuing item needs `join_previous: "space"`, and `reading_order` must move `p0018-b001`, `p0018-b002`
  and `p0019-r02`, `p0019-r03` out of the paragraph (suggested: all four directly before `p0017-b005`, after
  `p0017-b004`, the paragraph that cites Fig. 7; Fig. 6 is cited in `p0017-b003`).

## Pages
| Page | State | Content | Assets |
| --- | --- | --- | --- |
| 10 | reviewed | 2.4.3 Particle Gibbs sampler; conditional SMC algorithm (Steps 1-3) and PG sampler (Steps 1-2) as text, one item per step/sub-step; headings 2.5, 2.5.1 | none (the extractor's formula image for Step 3 (a)-(c) was transcribed) |
| 11 | reviewed | rest of 2.5.1, 2.5.2, start of section 3 | `figure-2` |
| 12 | reviewed | 3.1, equations (14), (15) | `figure-3` |
| 13 | reviewed | prose + Fig. 4 | `figure-4` |
| 14 | reviewed | rotated full-page Fig. 5 | `figure-5` |
| 15 | reviewed | rest of 3.1, 3.2, unnumbered SDE, equation (16) | none |
| 16 | reviewed | eight displays incl. (17), (18), (19) | none |
| 17 | reviewed | prose only | none |
| 18 | reviewed | rotated full-page Fig. 6 | `figure-6` |

Headings: `#### 2.4.3. Particle Gibbs sampler`, `### 2.5. Improvements and extensions`,
`#### 2.5.1. Advanced particle filtering and sequential Monte Carlo techniques`, `#### 2.5.2. Using all the particles`,
`## 3. Applications`, `### 3.1. A non-linear state space model`, `### 3.2. Lévy-driven stochastic volatility model`.

## Joins
- Set: `p0011-b003` (space, onto `p0010-b018`), `p0013-b003` (space, onto `p0012-b007`), `p0015-b001` (space, onto
  `p0013-b004` across page 14; see action above).
- Start boundary: page 10 starts with a heading after a complete paragraph on page 9; no join.
- End boundary: the continuing item on page 20 must join (`space`) onto `p0017-b005`, across pages 18 and 19 (see action above).
- No joins onto displays: `p0016-b001` (display completing "We define the integrated volatility") and `p0017-b001`
  ("where A = ..." after display (19)) have none.

## Float moves inside pages
- Page 11: Fig. 2 (printed at the top) now after the paragraph ending "... developed in Section 4.1."
- Page 12: Fig. 3 (printed at the bottom) now before the last paragraph, which continues onto page 13.
- Page 13: Fig. 4 (printed at the top) now between the continued paragraph and the next one.

## Formulas kept as images
None. All displays are LaTeX text items; tags (14)-(19).

## Printed oddities kept as printed (no TeX to compare)
- p10 Step 3(b): `q(·|y_n, X_{n-1}^{A_{n-1}^k})` without θ subscript (Step 2(a) has `q_θ`).
- p12: `p_θ(x_n|y_n, x_n)` (probably `x_{n-1}`); Fig. 3 caption marker for T = 10 printed as `|` (plot uses `+`).
- p14 caption: "and the (b), (d) the PMMH sampler".
- p15: SDE printed `dy*(t) = μ + βσ²(t) dt + σ(t) dB(t)` without braces; "Ornstein–Unlenbeck".
- p16/p17: (19) uses `A` in the denominator with `A = 2^κ δκ²/Γ(1−κ)` (p17), while (18) uses `A_0 = 2^κ δκ/Γ(1−κ)`.
- p18 caption lists p(κ|·), p(δ|·), p(λ|·) only.
- Calligraphic-plus-italic symbols: `\mathcal{I}G`, `\mathcal{T}S`, `\mathcal{B}e`; bare radical `\surd 50`.
- Thin-space thousands (50 000, 10 000) written 50000, 10000.
- Line-style legend marks in the captions of Figs 4, 5, 6 are graphics; approximated with characters and described
  in the page notes.

## Text repairs of substance
Glued words (p11 item (b), p15 "recently introduced in ...", p17 "We assigned the following ..."), decimal points
extracted as colons (p15 0.01; p17 0.50, 1.41, 2.83, 0.10, 0.5), caption glyph damage (Figs 2, 3), merged step items
split (p10), rotated captions separated from figure boxes and missing header omit item added (p14, p18).

## Remaining diagnostics (all category (a); adjudication notes written for pages 10-18)
- Missing lines: lines with inline/display maths now in LaTeX, lines glued in the PDF text layer, rotated captions.
- Number differences (pages 10, 12, 15, 16, 17): ASCII versus U+2212 minus in subscripts, signs glued to numbers in
  (14), decimal-point glyphs split by the parser, `σ²(0)` read as "2.0".
- Pages 11, 13, 14, 18: missing-line entries only.

## Proposals / notes
- Rotated figures 5 and 6 are cropped in page orientation (sideways). If the builder can rotate assets, rotate
  `figure-5` and `figure-6` by 90 degrees clockwise; otherwise add a plan note that they are printed landscape.
- Brief: the rule "the item immediately before a joined item must be text or caption" has no solution inside page
  files when a full-page float sits inside a paragraph; a sentence on what reviewers should do would help.
- Figure captions are written `Fig. N. ...` without bold; check consistency with the other reviewers.
