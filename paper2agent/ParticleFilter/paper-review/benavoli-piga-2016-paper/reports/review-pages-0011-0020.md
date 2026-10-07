# Review report: Benavoli & Piga 2016, PDF pages 11-20

Document: `documents/s001-benavoli-piga-2016`. All ten pages are `reviewed: true` with `[v2]` notes.
TeX source used: `tex-source/benavoli-piga-2016/FilteringSM_v15.tex` and `.bbl` (macros expanded:
`\xhyp` -> `\rho`, `\xaug` -> `\tilde{\mathbf{x}}`, `\relorder` -> `\mathbf{d}`, `\DP{..}` -> content).

## Pages

| Page | State | Content | Assets | Check |
| --- | --- | --- | --- | --- |
| 11 | done | end of 6.1: (39)-(42), Remark 4; 6.2; Algorithm 2 with (43); Example 3 (start) | `algorithm-2` (image + transcription) | ATTENTION, category (a) only |
| 12 | done | Example 3 (end), Fig. 2, 6.3, (44)-(48), Fig. 3, Theorem 6, Proof (start) | `figure-2`, `figure-3` | (a) only |
| 13 | done | Proof end with (49); 6.4; (50), (51a), (51b); Remark 5 | none | (a) only |
| 14 | done | Remark 6 with (52), (53); Example 4; Fig. 4; 6.5; Theorem 7, Proof (start) | `figure-4` | (a) only |
| 15 | done | Proof end; Algorithm 3 with (54); Example 5; Fig. 5; section 7 with (55), (56) | `algorithm-3` (image + transcription), `figure-5` | (a) only |
| 16 | done | section 7 end; Figs. 6-8; section 8 (start) | `figure-6`, `figure-7`, `figure-8` | (a) only |
| 17 | done | section 8 end; References [1]-[32] | none | OK |
| 18 | done | References [33]-[64] | none | OK |
| 19 | done | stray uncaptioned plot only | `uncaptioned-figure-p0019` | OK |
| 20 | done | stray uncaptioned plot only | `uncaptioned-figure-p0020` | OK |

No formula is kept as an image; every display equation (39)-(56) is LaTeX text with its printed `\tag`.
No tables in this range. Adjudication notes written for pages 11-16.

## Joins
- Page 11 first item (`p0011-b000`, "the integral ... can be approximated as:") has `join_previous: "space"`;
  it continues the last paragraph of page 10 (`p0010-b020`, ends "... uniformly distributed in $\mathcal{B}$,").
  The page-10 reviewer must keep that paragraph as the last emitted item of page 10 (no footnote or float after it).
- Inside my range: 11->12 (Example 3, space), 12->13 (proof of Theorem 6, space), 14->15 (proof of Theorem 7, space),
  15->16 (section 7 paragraph, space), 16->17 ("opti-/mization", none; hyphen removed on page 16).
- Within pages: 11 (paragraph around the Algorithm 2 float), 13 (column break), 15 (Example 5 around Fig. 5).

## Float placement (differs from the printed position, by the brief's rule)
- Algorithm 2 (top of right column, p. 11) is emitted before the paragraph "Algorithm 2 generates ..." that it interrupts.
- Fig. 3 (top right, p. 12) follows the sentence citing it; Fig. 4 (top right, p. 14) follows Example 4.
- Algorithm 3 (top left, p. 15) is emitted after the end of the proof of Theorem 7.
- Figs. 6-8 (p. 16) follow the first, continued paragraph.

## TeX versus PDF
- No mathematical disagreement found. Example numbers are taken from the PDF (Example 3, 4, 5; "Example 2" for `\ref{ex:1}`).
- References: the PDF does not render some Unicode dashes of the .bbl: [11] "identificationbounded noise case",
  [42] "no. 12" (.bbl: "no. 1–2"). [64]: the URL is printed with a space where the source has `~`
  (`http://cse.lab.imtlucca.it/ bemporad/hybrid/toolbox`). All kept as printed and recorded in the page notes.

## Authors' errors kept as printed (see page notes)
- p. 11: "problem (50)" cited in the paragraph after Algorithm 2; "referred to as [62]".
- p. 12: "$R_{\{\mathcal{H}_j\}}(x_i)$" before (45); Fig. 3 caption "$I_{\mathcal{H}_j}$" without braces.
- p. 13: constraint in (50)/(51) printed as $\nu_j - \boldsymbol{\omega}_j\mathbf{x}$ (no transpose), "+" then "−" over the line break;
  integral subscript without the last $\cap$.
- p. 15: Fig. 5 caption "Exampe 1" (text says Example 2); min subscript of (54) uses non-bold $\omega$;
  $\mathcal{X}_0 = [0.28\ 0.32]\times[0.78\ 0.82]$ versus initial conditions $x_1(0)=0.8$, $x_2(0)=0.3$ (order apparently swapped in print).
- p. 16: "Algorithms 3 is used".

## Proposals for shared files
- `plan.json` note: "PDF pages 19 and 20 each contain one uncaptioned plot ($y_o-\hat{y}$ versus Sample). They are the files
  ErrorBC.eps and ErrorIV.eps of the arXiv source, which the paper never includes or cites; arXiv appended them. They are kept
  as images `uncaptioned-figure-p0019/-p0020` and are not part of the article."
- Heading levels used here: `##` for "7 Numerical examples", "8 Conclusions", "References"; `###` for 6.2-6.5. The pages 1-10
  reviewer should use the same (`### 6.1 ...`, and `## 6 ...` for the section).
- Asset names in my range follow printed numbering (figure-2..8, algorithm-2, algorithm-3); page 10's figure should become
  `figure-1` and Algorithm 1 / its refinement need names that do not collide (`algorithm-1`, e.g. `algorithm-1-refinement`).
- Theorem-like labels are written without a trailing period, as printed ("**Remark 4** ...", "**Theorem 6** ...", "**Proof:** ...").

## Limitations
- Italic body text of remarks, examples and theorem statements is emitted upright (bold labels kept); italics in the
  reference list were dropped.
- [36] uses the precomposed character "ḿ" (U+1E3F) for the printed accented m.
- Brief feedback: the `check` output is flooded by pypdf "fontTools is required" warnings on stderr; filtering stderr was needed.
