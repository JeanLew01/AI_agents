# Review report: Haj Chhadé et al. 2014, PDF pages 17-24

All eight pages are `reviewed: true` with `[v2]` notes. No TeX source; maths transcribed from 260 dpi crops.

## Pages

| Page | Content | Assets | check |
| --- | --- | --- | --- |
| 17 | Eqs (6.2)-(6.5), Fig. 8, start of box-BP description | figure-8 | ATTENTION, 11 missing lines, all category (a) |
| 18 | Box-BP/NBP implementation, eq (6.6), 3 unnumbered interval displays, Fig. 9 | figure-9 | ATTENTION, 22 missing lines + `-1` minus-glyph, all category (a) |
| 19 | `## 7 Simulation Results`, `### 7.1 Grid-Like Placement of the Anchors`, Fig. 10 | figure-10 | OK |
| 20 | Fig. 11, Table 1, Fig. 12, `### 7.2 Random Placement of the Anchors` | figure-11, table-1, figure-12 | OK |
| 21 | Fig. 13, Fig. 14, Tables 2 and 3 | figure-13, figure-14, table-2, table-3 | OK |
| 22 | Fig. 15, Fig. 16, `## 8 Conclusion` | figure-15, figure-16 | OK |
| 23 | End of conclusion, Open Access statement, `## References` 1-24 | none | OK |
| 24 | References 25-31 | none | OK |

Adjudication notes written for pages 17 and 18 (`adjudication-notes/page-0017.json`, `page-0018.json`).

## Joins and float placement
- Page 17 starts with display equation (6.2), which completes page 16's last sentence ("According to the assumption above:"). It is a `$$` block, so no `join_previous`. Fig. 8 (printed at the top of page 17) was moved after the paragraph "The undirected graph ..." so it does not sit between that sentence and its equation.
- `join_previous: space` set on the first item of pages 18, 21, 22, 23 (sentences running across 17->18, 20->21, 21->22, 22->23). On pages 21 and 22 the continuing paragraph is printed below the floats and was moved to the top of the page.
- Fig. 9 moved from the top of page 18 to after the last interval display.
- Boundary with the 9-16 reviewer: page 16's last equation (6.1) is still a formula image plus glyph-soup text in that reviewer's file at the time I looked; nothing needed from them for the join, but (6.1) and (6.2) should end up in the same form (LaTeX with \tag).

## Mathematics
- No formulas kept as images. (6.2)-(6.6) carry printed tags; (6.4) is one aligned block with one printed number.
- Kept as printed: norms with `||`; interval bounds separated by a space, not a comma (`[\underline{d} \;\; \overline{d}]`); `[x_t]^i` and non-bold `[x_t]`, `[y_t]` next to bold `[\mathbf{x}_t]^{(i)}`.
- Typographic normalisations only: printed italic "cos"/"sin" written `\cos`/`\sin`; italic "i f" in (6.4) written `\text{if}`.
- Fig. 9 caption: radius is printed as d with an overbar (lost by the extractor), written `$\overline{d}$`.

## Text repairs of substance
- Page 17: the sentence "The joint probability distribution ... can be factorized as follows:" was inside a formula image; restored as text.
- Page 18: all three paragraphs had `<sup>`/underline/strikethrough damage; rewritten from the crops.
- Page 20: Table 1 was a picture with picture-text; now a table with string cells.
- Page 21: table row label "Time(s)" -> "Time (s)" as printed.
- Page 23: reference 16 respaced (all spaces lost); references 23 and 24 split into separate items; "166– 171", "498– 519" closed.
- Authors' typos kept: "Results fo box-BP algorithm" (Table 2 caption), "Box-Bp", "box-PF is about ten times faster", "bdallah" (ref 10), "Institue" (ref 13), "california" (ref 22), "Durrant-White" (ref 19).

## Notes for the coordinator
- References are printed as "1. ..." (no brackets) and kept that way; a Markdown renderer will show them as an ordered list.
- Tables 2 and 3 have no header row of their own; the first row ("No of anchors", 6-9) acts as the header.
- I dropped the extractor's `source_class` key on rewritten items (the builder scripts never read it; `check` passes).
- Asset names in other ranges still use extractor defaults (`figure-p0009-002`, `formula-p00NN-...`) at the time of writing; no clash with figure-8..16 / table-1..3.
- `plan.json` title is still the slug "haj-chhade-box-messages-2014"; proposed: "Non Parametric Distributed Inference in Sensor Networks Using Box Particles Messages".
- Brief: nothing wrong; `check` output is dominated by pypdf fontTools warnings (filter with `grep -v fontTools`).

## Limitations
- Figures 10-16 are raster scatter plots with unlabelled ticks; only the axis end labels (0, L) and, in Fig. 14, anchor numbers 1-9 are in the image. Nothing to transcribe.
