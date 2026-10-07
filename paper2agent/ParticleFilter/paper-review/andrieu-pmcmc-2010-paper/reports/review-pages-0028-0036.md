# Review report: Andrieu, Doucet, Holenstein (2010), PDF pages 28-36

All nine pages are `reviewed: true` with `[v2]` notes. No TeX source; all mathematics transcribed from 200-400 dpi crops.
No formula was kept as an image. Adjudication notes written for pages 28-33, 35, 36 (page 34 checks `OK`).

## Pages

| Page | Printed | Content | Check |
| --- | --- | --- | --- |
| 28 | 296 | PG sweep steps (b),(c); Assumption 7; Theorem 5 (unnumbered display); `### 4.6. Reusing all the particles`; Theorem 6 with (38), (39) | ATTENTION, category (a) only |
| 29 | 297 | End of Theorem 6 with (40); `## 5. Discussion and extensions`; `### 5.1. ...` | (a) only |
| 30 | 298 | 5.1 continued (unnumbered acceptance-ratio display); `### 5.2. Extensions` | (a) only |
| 31 | 299 | `## Acknowledgements`; `## Appendix A: ...` (steps (a),(b), three unnumbered displays, multinomial procedure); `## Appendix B: Proofs`; `### B.1. Proof of theorem 2` with (41) | (a) only |
| 32 | 300 | `### B.2`-`### B.5` proofs; unnumbered displays; (42) | (a) only |
| 33 | 301 | End of B.5: (43) and two unnumbered displays; `## References` (16 entries) | (a) only |
| 34 | 302 | References (23 entries); `## Discussion on the paper by Andrieu, Doucet and Holenstein`; `### Paul Fearnhead (Lancaster University)` | OK |
| 35 | 303 | Fig. 8 (`figure-d8-p0035`, label "Figure 8") + caption; Fearnhead continued (3 unnumbered displays) | (a) only |
| 36 | 304 | Fearnhead end; `### Simon Godsill (University of Cambridge)`; "The vote of thanks was passed by acclamation."; `### Nicolas Chopin (Ecole Nationale de la Statistique et de l’Administration Economique, Paris)` | (a) only |

Assets: one figure, `figure-d8-p0035` (page 35, bbox [107, 50, 386, 216], both panels with axis and (a)/(b) labels; checked with a crop). No tables, no algorithm boxes.

## Joins
- Set: page 30 first item (continues p29), page 32 first item (continues p31), page 36 first item (continues p35), all `space`.
- Not joined on purpose: page 28 starts with list steps (b),(c) (step (a) is the last item of page 27); page 29 and page 33 start with text following a display on the previous page; pages 31, 34, 35 start new blocks.
- Range boundaries: none needed. Page 28 begins with a new list step; page 36 ends with a complete paragraph and page 37 begins a new paragraph ("Similarly, Chopin (2007) ...").
  Page 27's owner should make sure step (a) of the PG sweep is a text item so that (a),(b),(c) read consecutively.

## Printed peculiarities kept as printed (recorded in review_notes)
- p28: sum in first line of 4.6 printed with upright capital Sigma; Theorem 6(a) prints X_{1:T}^k(i) (elsewhere 1:P).
- p31: step (a) of Appendix A has a non-bold O_{n-1}; "s(.|w_{n-1}, b_{n-1}^K)" capital K vs lower-case k in the displays.
- p32: "1 - Z/Pi_{n=1}^P C_n" with upright Pi; in B.4 i is in {1..N}^{P-1} then {1..N}^P; display has {K} where text has {k}.
- p33: proposal written q(theta,theta') with a comma; E_pi{f(X_{1:P})} without theta.
- p34: "Ornstein–Unhlenbeck" (sic); "Shephard N. and Pitt M. K." without commas; Kitagawa before Ionides.
- p36: "Kingman (1982)": text layer has letter l ("l982"), image reads 1982; transcribed 1982 (causes the page's number difference).

## Repairs of substance
- Glued words repaired on pp. 28, 29, 30, 32 (e.g. "Standard theory of MCMC algorithms", "generalized and studied theoretically in Andrieu and Roberts (2009). The present work is a simple").
- Extractor superscript damage repaired in inline maths throughout (pp. 28, 30, 32, 33, 35).
- References rebuilt from native lines, one text item per entry (the extractor had merged/split entries); italics/bold of journal names and volumes are not marked. Line-wrap hyphen "Genet-ics" removed.
- Fig. 8 caption: printed line-style samples rendered as dashes plus a bracketed description added by the reviewer ("[thick full line]", "[dark grey broken line]", ...). This is the only non-verbatim addition.
- Multi-line displays (39), (41), (42) and unnumbered ones are single `$$` blocks (`aligned` where needed) carrying the single printed number.

## Remaining diagnostics
All `missing line` entries on pp. 28-33, 35, 36 are lines containing LaTeX maths (category a). Number differences: U+2212 vs ASCII minus in subscripts (pp. 28, 30-33, 35); raised decimal dot "0:1" on p35; "l982" on p36. No category (b) item remains.

## Proposals for shared files
- Navigation: discussion contributions are `###` under `## Discussion on the paper by Andrieu, Doucet and Holenstein` (starts on PDF page 34).
- plan note suggestion: "Reference entries are plain text (journal italics and bold volume numbers not marked)."

## Limitations / brief feedback
- Italic "et al." kept as `_et al._` in running prose (not in references).
- The brief does not say how to render caption legends made of line samples; a collection-wide convention would help.
- `check` prints many pypdf fontTools warnings to stderr; filtering them is needed to read the output.
