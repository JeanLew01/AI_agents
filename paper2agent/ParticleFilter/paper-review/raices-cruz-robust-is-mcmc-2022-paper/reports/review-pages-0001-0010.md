# Review report: Raices Cruz et al. 2022 (arXiv:2206.08728v1), PDF pages 1-10

All ten pages were opened, compared with their previews (plus zoomed crops for figures and dense maths),
rewritten, saved with `reviewed: true` and `[v2]` notes. Maths was taken from the authors' TeX
(`article-arxiv.tex`), macros expanded (`\Var`, `\Cov` -> `\mathrm{Var}`, `\mathrm{Cov}`; `\coloneqq` -> `:=`),
`\cref` resolved to the printed forms ("eq. (5)", "Figure 1", "section 5.1"), and checked against the page.

## Per page
| Page | Content | Assets | Equations (as `\tag`) | Check |
| --- | --- | --- | --- | --- |
| 1 | title (`#`), authors, affiliation/e-mail/keyword footnote block (after author line), abstract, `## 1. Introduction` | - | - | OK |
| 2 | Introduction | - | (1) | OK |
| 3 | end of Introduction, `## 2. Importance sampling` | - | (2)-(6) | missing lines: (a) |
| 4 | `## 3. Effective sample size of importance sampling using MCMC` | - | (7)-(14) | missing lines: (a) |
| 5 | Section 3 derivation | - | (15)-(23), unnumbered ESS_MCMC definition | missing lines, numbers: (a) |
| 6 | `## 4. Importance sampling over a set of probability distributions`, Steps 1-5 | - | (24)-(26) | missing lines: (a) |
| 7 | `## 5. An application`, `### 5.1. ...` | - | (27)-(32) | missing lines: (a) |
| 8 | `### 5.2. Selecting a set of priors.`, list items (1)-(4) | `figure-1` | - | missing lines: (a) |
| 9 | list item (5), `### 5.3. ...` | `figure-2` | unnumbered set M, (33) | missing lines, numbers: (a) |
| 10 | 5.3 continued, `### 5.4. ...` | `figure-3` | (34) | missing lines, numbers: (a) |

No tables and no algorithm floats occur on pages 1-10 (Tables 1-4 are on pages 11-12). The five-step procedure
on page 6 is a printed description list, not a float; it is kept as five text items with the printed bold labels
`**Step n:**`. No formula was kept as an image.

## Joins
- Set inside the range: page 2 first item (space, from page 1 "For instance,"), page 3 first item (space),
  page 7 first item (space).
- Boundary 10 -> 11: page 10 ends "It takes much longer time to run a" and page 11 starts "grid search method, ...".
  Page 11's first prose item needs `join_previous: "space"`; it already has it in the other reviewer's file.
- Pages 3->4, 4->5, 5->6, 7->8, 8->9 need no join (display or complete paragraph at the break). Page 9 ends with
  display (33) and a comma; page 10 starts with the continuing "where $X^{(i)}$ ..." text (no join across a display).

## Float placement
- Page 9: Figure 2 is printed between list items (4) and (5); item (5) is placed first, then Figure 2 + caption.
- Page 10: Figure 3 is printed at the top, inside the sentence running from (33); it is moved after the complete
  paragraph ending "... hyperparameters $\mu_0$ and $\tau_0$." and before "Using eq. (34) ...", which cites it.
- Figure boxes were all widened and verified by crops; the extractor's Figure 3 box would have cut the last
  colour-bar label ("20000" -> "2000").

## Text repairs of substance
- Page 1: title was a "page-header" text item; e-mail `ivette.raices_cruz@cec.lu.se` was damaged by strike-through
  markup; `<sup>` and misplaced umlaut in the author line.
- Page 5: the extractor had put everything from "We now estimate ..." to (23) into one formula image, dropping
  three prose lines; all restored as text.
- Pages 3, 4, 6, 9, 10: inline fractions / sets garbled into `<sup>`/`<u>` soup or replacement characters, rewritten.
- Page 4: one extracted item contained two printed paragraphs; split.

## TeX versus PDF
No disagreement found on pages 1-10. Printed forms worth knowing (kept as printed):
- (15) has upper summation limit $N-k$ (sic). "(see A for details)" and "(see C for the proof ...)" are bare
  appendix letters. "[12][p. 5-6]". "(eq. 30 and eq. 31)" versus "eq. (28)" elsewhere.
- Authors' wording kept: "inference rely", "few robust Bayesian analysis have", "Metropolis Hasting",
  "efficient sample size" (page 3), "yields to the set", "effective samples size", "see (Table 1, 2 and 3)".
- Figure 1 shows nodes $k_\mu$, $k_\tau$ where the text uses $k_l$, $k_u$ (visible in the image only).
- `\coloneqq` is written `:=`; (9)/(10), (27)/(28), (30)-(32) and (22)/(23) are printed as aligned groups and are
  given as one `$$` block per printed number ((23) begins with a `\phantom` left-hand side).
- Thousands are printed with a thin space and kept with a plain space ("10 000"); in maths `$\tau_0 = 1~000$`.

## Remaining diagnostics
All remaining `missing line` entries (pages 3-10) are lines containing inline or display maths now in LaTeX;
number differences on pages 5, 9, 10 are U+2212 versus ASCII minus or LaTeX spacing ("\ell+1", "- 2\mu", "- 0.9").
All category (a); adjudication notes written for pages 3-10. Pages 1 and 2 are OK.

## Proposals / notes for the coordinator
- Numbered run-in subsection titles (5.1-5.4, amsart `\subsection`, printed bold with a trailing period) are
  `### ` headings without the trailing period, the same form as the other reviewer's `### 5.5. ...`.
- Asset names in the document: figure-1, figure-2, figure-3 (mine), table-1..table-4 (pages 11-12); no clash.
- Headings and their run-in paragraph share the same printed line, so heading and following text item have
  overlapping boxes (text items only; no effect on crops).
- Brief: the assignment hint about algorithms does not apply (no algorithm float in this paper).
- Incident: one of my shell commands had a mis-terminated heredoc, so bash tried to run a few lines of note text as
  commands (all failed with "command not found"); I checked the document directory and git status and found no
  stray files.
