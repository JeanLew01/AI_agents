# Review report: Andrieu, Doucet, Holenstein (2010), PDF pages 1-9

## Per-page log
- **Page 1** done [v2]. Title, authors, summary, keywords, first-page footer (kept as text, moved before the `## 1. Introduction` heading), intro paragraph (continues on p2). Banner artwork omitted. No maths. check: OK; second parser reports an extra `2010` (parser artefact, adjudicated).
- **Page 2** done [v2]. Prose only; `## 2. Inference in state space models`. First item joins p1 (space). Restored compound hyphens `off-the-shelf`, `Lévy-driven`. Diagnostics: 4 missing lines, all (a) (inline `$\pi$`).
- **Page 3** done [v2]. `### 2.1.`, `### 2.2.`; equations (1)-(5) as LaTeX text with tags. First item joins p2 (space). Ends with display (5). Diagnostics: (a) only (maths lines; `−1` vs `-1`).
- **Page 4** done [v2]. `#### 2.2.1.`; unnumbered identity display, (6) (aligned, two lines, one tag), first line of (7) with tag; SMC pseudocode Step 1/2 as text items per step line. Not joined to p3 (p3 ends with display (5)). Diagnostics: (a) only.
- **Page 5** done [v2]. Continuation of display (7) (no tag; tag is on p4), unnumbered `r(A|W)` display, (8); Figure 1 = `figure-1` + caption, moved up to the paragraph break after "This is illustrated in Fig. 1."; page ends with paragraph continuing on p6. Diagnostics: (a) only.
- **Page 6** done [v2]. (9) plus two unnumbered displays; `#### 2.2.2.`, `### 2.3.`. First item joins p5 (space); last paragraph continues on p7. Diagnostics: (a) only.
- **Page 7** done [v2]. (10); `### 2.4.`. First item joins p6 (space); last paragraph continues on p8. Diagnostics: (a) only.
- **Page 8** done [v2]. Two unnumbered displays, (11); `#### 2.4.1.`; PIMH sampler as text items per step. First item joins p7 (space); last paragraph continues on p9. Diagnostics: (a) only.
- **Page 9** done [v2]. Unnumbered proposal display, (12), (13); `#### 2.4.2.`; PMMH sampler as text items per step. First item joins p8 (space). Ends with a complete paragraph. Diagnostics: (a) only.

## Final state
All nine pages (PDF 1-9, journal pp. 269-277) are `reviewed: true` with `[v2]` notes. Every page was compared with its preview; every page with mathematics (3-9) was transcribed from 220-330 dpi crops (no TeX source exists).

## Assets
- `figure-1` (page 5, Fig. 1, ancestral lineages), with caption item. No tables. No algorithm images (the printed SMC / PIMH / PMMH descriptions are text, one item per printed step line, as the assignment prescribes).
- Page 1 banner artwork: omitted (furniture).

## Equations
| Page | Numbered | Unnumbered displays |
| --- | --- | --- |
| 3 | (1), (2), (3), (4), (5) | - |
| 4 | (6) (two lines, one tag, `aligned`), (7) first line with tag | identity `p_θ(x_{1:2}|y_{1:2}) ∝ ...` |
| 5 | - | continuation of (7) (`= f g / q,` and `W_n^k := ...`), `r(A_{n-1}|W_{n-1})` |
| 6 | (9) | `\hat p_θ(y_n|y_{1:n-1}) = (1/N) Σ w_n`, integral for `p_θ(y_n|y_{1:n-1})` |
| 7 | (10) | - |
| 8 | (11) | IMH acceptance probability, `q_θ(dx|y) = E{\hat p_θ(dx|y)}` |
| 9 | (12), (13) | proposal density `q{(θ*,x*)|(θ,x)}` |

No formula was kept as an image; all symbols were legible in the crops.

## Joins
- Set (all `space`): first text item of pages 2, 3, 6, 7, 8, 9.
- Not set on purpose: page 4 first item ("where $W_n^k$ is ...") follows display (5) at the end of page 3; page 5 first item is the continuation of display (7).
- **Boundary to page 10: no join needed.** Page 9 ends with a complete paragraph ("... converges to equation (12) as $N \to \infty$."); page 10 starts with the heading 2.4.3.
- Display (7) is split by the page break 4/5: tag `(7)` is on the page-4 block; the page-5 block (aligned continuation, no tag) follows immediately in the continuous document. If the coordinator prefers a single block, the two items would have to be merged in one page file (the verifier's page-5 native lines for it are maths-only either way).

## Layout moves
- Page 1: first-page footer (address for correspondence, copyright, ISSN line) kept as text and moved before `## 1. Introduction` so the page ends with the paragraph continuing on page 2.
- Page 5: Fig. 1 + caption moved from the page bottom to the paragraph break after "This is illustrated in Fig. 1."; the extractor's merged paragraph was split at the printed break ("This procedure provides us at time T ...").

## Printed peculiarities kept verbatim (no corrections made)
- p1: "Ocober 14th, 2009".
- p4: step 2(b) prints `q(·|y_n, X_{n-1}^{A_{n-1}^k})` without subscript θ; weights written `{W_{1:n}^k}`; upright capital sigma in `Σ_{k=1}^m p_k = 1`.
- p7: in (10) the first product runs to `n+K`, the second to `n+K-1`.
- p8: "in Section 4.5 we present ... the particle Gibbs (PG) algorithm" (the PG sampler is in Section 2.4.3); lower-case "theorem 3".
- p9: journal braces for function arguments (`q{...}`, `p{θ(i-1)}`); (13) has no trailing punctuation.

## Text repairs of substance
Glued words (p3 "knownasahiddenMarkovmodel", p4 "whichtakeintoaccount...", p6 "howbesttoselect", p8/p9 step lines), `<sup>` damage, star superscript extracted as "Å" (now `^*`), restored compound hyphens "off-the-shelf" and "Lévy-driven" (p2), author names mis-tagged as headings (p1), extractor list dashes before "(a)"/"(b)" (p8, p9), "Step 2" merged into the Step 1 item (p8).

## Remaining diagnostics (all category (a); adjudication notes written for pages 1-9)
- p1: check OK; second parser reports one extra `2010` (parser artefact in the Helvetica header/footer lines).
- p2: 4 missing lines = inline `$\pi$`.
- p3-p9: missing lines are lines containing mathematics now in LaTeX; number differences are exclusively PDF `−1` versus ASCII `-1` (p3: 1, p4: 11, p5: 16, p6: 18, p7: 8, p8: 3, p9: 9); the second parser sometimes detaches the minus and reports a bare `1`.

## Proposals for shared files
- Navigation headings in my range: `## 1. Introduction`, `## 2. Inference in state space models`, `### 2.1.`, `### 2.2.`, `#### 2.2.1.`, `#### 2.2.2.`, `### 2.3.`, `### 2.4.`, `#### 2.4.1.`, `#### 2.4.2.` (page 10 has `#### 2.4.3.`, consistent).
- A plan note could say: "Mathematics was transcribed from the typeset page (no TeX source); the journal's `{}` argument braces and star superscripts are kept as printed."

## Limitations / remarks on the brief
- Italic emphasis of printed run-in step labels ("*Step 1*") and italic terms is kept with single asterisks; star superscripts inside `$...$` are written `^*`, so a Markdown renderer that pairs asterisks across maths could mis-render a line; the raw text is unambiguous.
- The brief says the item before a joined item "must be text or caption"; on pages 2, 3, 6-9 the running-header omit item precedes the joined first item. The builder skips omit items (sibling papers have the same pattern), so this was left as is.
- `check` prints long fontTools warnings to stderr for this PDF; harmless.
