# Review report: Diffusion differentiable resampling, pages 16-23

Reviewer for pages 16-23 under REVIEWER_BRIEF.md ([v2]). TeX source used for maths
(`tex-source/diffusion-resampling/main.tex`, macros from `zmacro.tex` expanded).
Macro expansions used throughout: `\grad`->`\nabla`, `\diff`->`\mathrm{d}`, `\refmeasure`->`\pi_{\mathrm{ref}}`,
`\cond`->`\mid`, `\coloneqq`->`:=`, `\cu{X}`->`\mathbf{X}`, `\R`->`\mathbb{R}`, `\expec{.}`->`\mathbb{E}[.]`,
`\abs*`/`\absbig`->`\lvert..\rvert` with sizing, `\trans`->`\mathsf{T}`.

## Per-page log

### Page 16
- State: reviewed, `[v2]`.
- Join: first item `p0016-b001` has `join_previous: "space"` (continues page 15's last paragraph, "...remains an open | discussion").
- Headings: `## D. Elaboration of Remark 1`, `## E. Error analysis of the resampling mapping`.
- Equations (26)-(30) as LaTeX display blocks (no formula images kept). (30) is one aligned block with `\tag{30}`.
- Furniture: running header and page number `16` omitted.
- Remaining diagnostics: 47 missing lines, all maths (category a); number check: one '7' (maps-to glyph `7→`), category a.
- TeX vs PDF: no disagreement.

### Page 17
- State: reviewed, `[v2]`. No join needed (page 16 ends with a complete paragraph before heading E; page 17 starts a new paragraph after the E heading on page 16, which ends with a complete sentence).
- Heading: `## F. Common experiment settings`.
- Equations (31)-(33) as LaTeX display blocks.
- Typos transcribed as printed (TeX agrees with PDF): chi^2 definition `\int (p(x)-q(x)/q(x)^2) q(x) dx` (misplaced bracket/square); in (32) the integrand absolute value is not squared; (32) ends with `chi^2(pi_ref || p_T^N)` but (33) has `chi^2(p_T || p_T^N)`; prose `pi^{*,N}` vs equations `pi^{\star,N}`; an inequality is called "identity".
- Remaining diagnostics: 34 missing lines, all maths (a). No number differences.

### Page 18
- State: reviewed, `[v2]`. No join (new paragraph at top).
- Run-in bold titles "Gumbel-Softmax resampling", "Soft resampling" kept as text. Heading `## G. Gaussian mixture resampling`.
- Equations: unnumbered `X_i^* = sum S_{i,j} X_j`; soft-resampling steps 1-4 as list text items; (34) aligned with `\tag{34}`; unnumbered posterior block (G_i, Omega_i, M_i, V_i).
- Typos kept: `g_{i,j} = -log log u_{i,j}` (standard Gumbel is `-log(-log u)`), "The gradient produced by method is thus always biased", "Karkus et al. (2018) view".
- Remaining diagnostics: 31 missing lines, maths (a); numbers: two `−1` exponents (U+2212 vs `-`), (a).

### Page 19
- State: reviewed, `[v2]`. No join at top (new paragraph). Page ends mid-sentence ("...for large sample size" -> page 20, join needed on page 20).
- Floats moved: Tables 3-4 (printed at the top) placed after the paragraph "Tables 3 and 4 show more detailed results...", before `## H. Time comparison`.
- Table 3 = `table-3` (10x8, ODE/SDE header flattened as "Euler–Maruyama ODE", ...). Table 4 = `table-4` (5x9, three sub-tables side by side, header "Method | SWD | Resampling variance" repeated; duplicated "Gumbel 0.2" row label kept as printed - PDF/TeX typo).
- Remark 3 as `**Remark 3 (Resampling variance).**`.
- Heading `## H. Time comparison`.
- Remaining diagnostics: 9 missing lines (maths, a); numbers: minus glyphs (a); second parser glues Table 4 neighbouring cells (a).

### Page 20
- State: reviewed, `[v2]`. Join: `p0020-b005` ("N. Moreover, ...") moved to top with `join_previous: "space"` (continues page 19). Page ends mid-sentence ("...and making OT parameter" -> page 21).
- Tables 5-6 (`table-5`, `table-6`, 5x8 each, header "Number of samples N: 128" ... ": 8192") placed after the continuing paragraph, before `## I. Linear Gaussian SSM`.
- Equation (35) LaTeX aligned with `\tag{35}`.
- Repair: extractor had merged the "The optimiser L-BFGS is implemented using JAXopt ..." paragraph into the previous one; split into new item `p0020-b009a`.
- Remaining diagnostics: 20 missing lines (maths, a); numbers: minus glyphs and ^2_2 adjacency (a); second parser glues row label + first cell (a).

### Page 21
- State: reviewed, `[v2]`. Join: `p0021-b003` ("estimation diverges largely...") moved to top, `join_previous: "space"` (continues page 20).
- Table 7 = `table-7` (13x8, flattened ODE/SDE header) placed after the last section-I paragraph, before `## J. Prey-predator model`. Caption lacks final period as printed.
- Equation (36) LaTeX aligned with `\tag{36}`; page ends with (36) (sentence continues "where we set ..." on page 22 as a new item after the display).
- Typos kept: "In Tables 7 we find", "worst even exploding", "Jentzen–Kloden", "Lokta–Volterra".
- Remaining diagnostics: 7 missing lines (maths, a). No number differences.

### Page 22
- State: reviewed, `[v2]`. Floats only (no prose).
- Tables 8, 9 (`table-8`, `table-9`, 13x8, flattened ODE/SDE headers), Table 10 (`table-10`, 11x4, LaTeX norm headers, NaN kept).
- Reading-order issue: equation (36) at the end of page 21 continues on page 23 ("where we set ..."), with these section-I tables in between. **Proposal**: plan.json `reading_order` placing `p0022-b001`..`p0022-b006` before `p0021-b008` (heading J).
- Remaining diagnostics: 2 missing lines (Table 10 LaTeX header cells, a); numbers: four `10^{−1}` minus glyphs (a).

### Page 23
- State: reviewed, `[v2]`. Page starts with "where we set alpha = gamma = 6 ..." (continuation of the sentence of (36) on page 21; not joined, previous item is a display and page 22 floats intervene). Page ends mid-sentence ("... In particular," -> page 24; `p0024-b003` needs `join_previous: "space"`).
- Split the extractor's combined diagram+table item into Figure 7 (`figure-7`, figure item `p0023-b001`, bbox [91, 63, 268, 270]) and Table 11 (`table-11`, new item `p0023-b001t`, 12x3).
- Floats placed after the "Results are shown in Tables 11 and 12 ..." paragraph and before `## K. Vision-based pendulum dynamics tracking` (section K also starts on page 23, not only D-J).
- Equation (37) LaTeX with `\tag{37}`.
- Repairs: Figure 7 caption "preypredator" -> "prey-predator"; glyph-soup maths rewritten.
- Typos kept: "dicretisation", "three-layers".
- Remaining diagnostics: 10 missing lines (maths, a); numbers: `−5` (a); second parser glues Table 11 cells (a).

## Summary

**Pages covered**: 16-23, all `reviewed: true` with `[v2]` notes; adjudication notes written for all 8 pages
(`DOC/adjudication-notes/page-0016.json` ... `page-0023.json`). All remaining `check` diagnostics are category (a)
(LaTeX vs glyph soup, minus glyph U+2212 vs ASCII, sub/superscript adjacency, second-parser gluing of adjacent table cells).

**Assets**
| Page | Item | Label | asset_name |
| --- | --- | --- | --- |
| 19 | p0019-b002 | Table 3 | table-3 |
| 19 | p0019-b004 | Table 4 | table-4 |
| 20 | p0020-b002 | Table 5 | table-5 |
| 20 | p0020-b004 | Table 6 | table-6 |
| 21 | p0021-b002 | Table 7 | table-7 |
| 22 | p0022-b002 | Table 8 | table-8 |
| 22 | p0022-b004 | Table 9 | table-9 |
| 22 | p0022-b006 | Table 10 | table-10 |
| 23 | p0023-b001 | Figure 7 | figure-7 |
| 23 | p0023-b001t | Table 11 | table-11 |

No formula images kept: equations (26)-(37) are all LaTeX display blocks with `\tag{..}`; plus three unnumbered displays
(page 18: `X_i^*` sum and the Gaussian-mixture posterior block). No algorithms on these pages.

**Headings**: `## D. Elaboration of Remark 1`, `## E. Error analysis of the resampling mapping` (p16),
`## F. Common experiment settings` (p17), `## G. Gaussian mixture resampling` (p18), `## H. Time comparison` (p19),
`## I. Linear Gaussian SSM` (p20), `## J. Prey-predator model` (p21), `## K. Vision-based pendulum dynamics tracking` (p23;
the assignment hint listed D-J, but K also starts on page 23). Theorem-like: `**Remark 3 (Resampling variance).**` (p19).

**Joins**: `p0016-b001` space (from page 15, "...remains an open | discussion"); `p0020-b005` space (from p19);
`p0021-b003` space (from p20). **Needed at the boundary**: page 24's first prose item `p0024-b003` ("we compute the
log-likelihood ...") needs `join_previous: "space"` (page 23 ends "... In particular,").

**Floats moved within pages** (all placed between complete paragraphs, after the paragraph that discusses them):
Tables 3-4 (p19), Tables 5-6 (p20), Table 7 (p21), Figure 7 + Table 11 (p23).

**TeX vs PDF**: no disagreement found on pages 16-23; all maths and table values taken from main.tex and checked against
the page images.

**Author typos kept as printed** (TeX agrees): p17 chi^2 definition `\int (p(x)-q(x)/q(x)^2) q(x) dx` (misplaced
bracket/square), (32) integrand `|...|` not squared while LHS is squared, (32) ends `chi^2(pi_ref || p_T^N)` but (33)
uses `chi^2(p_T || p_T^N)`, prose `pi^{*,N}` vs `pi^{\star,N}` in equations, inequality called "identity";
p18 `g_{i,j} = -log log u_{i,j}` (standard Gumbel is `-log(-log u)`), "gradient produced by method";
p19 Table 4 duplicated "Gumbel 0.2" row label (second presumably 0.1); p21 "In Tables 7", "Jentzen–Kloden",
"Lokta–Volterra", Table 7/8 captions lack final period; p23 "dicretisation", "three-layers".

**Text repairs of substance**: p20 the "The optimiser L-BFGS is implemented using JAXopt ..." paragraph had been merged
into the preceding paragraph by the extractor - split into new item `p0020-b009a`; p23 the extractor's single
"table" item mixing the Figure 7 diagram labels with Table 11 cells was split into a figure and a table item
(`p0023-b001t` is new); p23 Figure 7 caption "preypredator" -> "prey-predator"; p16 "Radon– Nikodym" -> "Radon–Nikodym";
all `<sup>`/glyph-soup maths rewritten.

**Table conventions**: cells are plain strings with "a ± b"; row labels like "T = 1, K = 8", "OT (ε = 0.3)";
two-level headers flattened by repeating the parent ("Euler–Maruyama ODE", ..., "Tweedie SDE";
"Number of samples N: 128", ...). Table 4 is captured as one 5x9 grid with its three sub-tables side by side and the
header "Method | SWD | Resampling variance" repeated. Table 10 header cells use LaTeX for the norms.

## Proposals for shared files
1. **plan.json `reading_order`** (reading-order break across pages 21-23): equation (36) ends page 21 with a comma and
   its sentence continues at the top of page 23 ("where we set alpha = gamma = 6 ..."), but page 22 is entirely
   section-I floats (Tables 8-10). Suggest a `reading_order` that places `p0022-b001` ... `p0022-b006` before
   `p0021-b008` (heading `## J. Prey-predator model`), i.e. right after Table 7 (`p0021-b002`). Then J reads
   heading -> "Recall ..." -> (36) -> "where we set ..." continuously.
2. **Asset names**: table-3 ... table-11 and figure-7 follow printed numbering; the other reviewers should not reuse them
   (Table 12 on page 24 -> table-12).

## Limitations
- Remark 3's body is italic in print; emitted as plain text (only the label is bold).
- Table 4's three side-by-side sub-tables share one CSV with repeated column names (as printed); a consumer must read the
  columns in groups of three.

## Brief feedback
- The brief's hint says sections D-J start on pages 16-23; section K also starts on page 23.
- Shell-quoting review notes that contain backticks is error-prone (a backtick in a note was executed by bash once;
  fixed). Writing notes from a Python script avoids this.
