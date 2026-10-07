# Review report: Andrieu, Doucet, Holenstein (2010), PDF pages 47-56 (printed 315-324, discussion)

All ten pages are `reviewed: true` with `[v2]` notes; every page was compared with its preview and with
250-300 dpi crops of all maths, captions and figure boxes. No TeX source. Adjudication notes written for all
ten pages (`adjudication-notes/page-0047.json` ... `page-0056.json`).

## Per page

| Page | Content | Assets | Displays (all unnumbered) |
| --- | --- | --- | --- |
| 47 | end of Bhadra; Bornn and Tabet starts | `figure-d11-p0047` (Fig. 11, panels a-e) | - |
| 48 | Bornn and Tabet ends; Cappé | `figure-d12-p0048` (Fig. 12) | - (caption maths in LaTeX) |
| 49 | Cappé ends; Cornebise and Peters | `figure-d13-p0049` (Fig. 13) | estimate of p-hat_{theta*}(y_{1:T}) |
| 50 | figure page | `figure-d14-p0050` (Fig. 14, panels a-f) | - |
| 51 | Cornebise and Peters ends | `figure-d15-p0051` (Fig. 15, panels a-c) | PRC kernel q*_theta; r(c_n, x_{n-1}) |
| 52 | Creal and Koopman; Crisan starts | - | - |
| 53 | Crisan ends; Draper; Everitt | - | clique factorization; Z_{theta_{1:M}} |
| 54 | Golightly and Wilkinson | `figure-d16-p0054` (Fig. 16) | SDE; Euler-Maruyama transition; alpha/beta (one aligned block) |
| 55 | Golightly and Wilkinson ends; Ionides; Jacob, Chopin, Robert and Rue | - | Chib identity; estimate of p(theta|y) |
| 56 | Jacob et al. ends; Johannes, Polson and Yae starts | - | state space model (aligned, two lines) |

No tables, no algorithms, no footnotes, no formulas kept as images. All extractor `formula` items were
converted to LaTeX `text` items. Figure labels are "Figure 11" ... "Figure 16".

## Headings (all `###`, as printed)
Luke Bornn and Aline Tabet (p47); Olivier Cappé (p48, split off a run-in text item); J. Cornebise ... and
G. W. Peters ... (p49); Drew D. Creal ... and Siem Jan Koopman ... (p52); Dan Crisan (p52); David Draper (p53);
Richard Everitt (p53); Andrew Golightly and Darren J. Wilkinson (p54); Edward L. Ionides (p55);
Pierre Jacob ..., Nicolas Chopin ..., Christian Robert ... and Håvard Rue ... (p55); Michael Johannes ... and
Nick Polson and Seung M.-Yae ... (p56).

## Joins
- Set inside the range: p48 first item (space), p49 first item (space), p53 first item (space), p55 first item (space).
- p47 first item: none needed. Page 46 ends with a complete paragraph; p47 opens with Fig. 11 and a new paragraph.
- **Boundary join needed on page 57 (next reviewer):** page 56 ends mid-sentence with
  "...whether assumption 4 is satisfied in the"; the continuing prose on page 57 needs `join_previous: "space"`
  and page 57 should start with that prose (Fig. 17 after it).
- Pages 49 -> 50 -> 51: p49 ends with Fig. 13 after the complete list item (b); p50 is Fig. 14 only; p51 starts
  with Fig. 15 and then the indented continuation paragraphs of item (b) (new paragraphs, no join).

## Float moves
- p48: Fig. 12 + caption moved before the last paragraph (which continues on p49).
- p54: Fig. 16 + caption moved before the paragraph "To compare the performance..." so the page ends with the
  paragraph that continues on p55 and the alpha/beta display stays attached to its lead-in sentence.

## Printed peculiarities kept verbatim (noted in review_notes)
- p49 Fig. 13 caption: state transition mixes indices, `x_{n-1} + r[1 - {exp(x_{t-1})/K}^zeta]`.
- p48 Fig. 12 caption: `2.26 = int_{-4}^{4} 8 pi^2(x) dx` (the "8" is printed).
- p50: "mixing of parameters K" (sic). p53: "identially distributed" (sic).
- p55: the page prints letter "l" for digit 1 in "Kendall et al. (l999)" and "Liu and West (200l)"; p56: "l/1000th".
  Kept as printed (verifier-clean); a reader should read 1999, 2001, 1/1000th. Coordinator may prefer to normalise.
- p56 display: coefficient of x_t/(1+x_t^2) printed as beta_1 (probably beta_2). Names "Rubio-Ramerez", "Seung M.-Yae" as printed.
- p54 SDE: bare radical sign before beta(X_t, theta), written `\surd`.
- Thin-space digit grouping written without space (100000, 20000, 500000, 60000, 300000) so numbers match the text layer.
- Caption line-style keys written in Unicode: `———` solid, `- - - - - - -` dashed, `· · · · · · ·` dotted,
  `· - · - · - ·` dot-dash, `○` circle, `|` solid vertical, `¦` dashed vertical (p47).

## Text repairs of substance
- Glued words restored: p48 ("Icongratulatetheauthors..."), p51 (after q*_theta), p53 ("processingunittoexploit...").
- p47 "likelihoodbased" -> "likelihood-based"; p53 "autocorrelations" at a line break written "auto-correlations"
  (the same item prints "auto-correlations" earlier; judgement call).

## Remaining diagnostics (all category (a))
Every page still reports `missing line` entries, all of them lines with LaTeX maths, caption plot-symbol keys or
split decimals; number differences on 48, 49, 51, 52, 54, 55, 56 are sub/superscript digits, U+2212 versus ASCII
minus, and decimals split by the text layer (2:26, 2:69, 0:04, 0:5, 0:0025, 0:3, 1:2). Pages 47, 50, 53 have
missing-line diagnostics only. Nothing of category (b) remains.

## Proposals / notes for the coordinator
- Asset names follow the assignment (`figure-dNN-pPPPP`); no clashes expected.
- Brief feedback: the assignment does not say whether publisher glyph errors (letter l for digit 1) count as
  "authors' typos" (keep) or "extraction damage" (fix); I kept the printed form.
- Limitations: none; no formula was left uncertain.
