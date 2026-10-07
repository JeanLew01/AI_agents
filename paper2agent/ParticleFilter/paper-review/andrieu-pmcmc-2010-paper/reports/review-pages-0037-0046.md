# Review report: Andrieu, Doucet, Holenstein (2010), PDF pages 37-46 (printed 305-314)

All ten pages are `reviewed: true` with `[v2]` notes. No TeX source; all mathematics transcribed from 200-420 dpi crops.
Every page still reports `ATTENTION` from `check` (LaTeX versus glyph text only, category (a)); adjudication notes written for pages 37-46.

## Per page

| Page | Content | Assets / numbered equations | State |
| --- | --- | --- | --- |
| 37 | End of Chopin's contribution; Rong Chen (flexible resampling: steps (a)-(c), 4 unnumbered displays) | none | done |
| 38 | End of Chen (display); Mark Girolami; Nick Whiteley | (44) | done |
| 39 | End of Whiteley; Gareth Roberts (pseudo-marginal) | `table-d-p0039` (unnumbered comparison table, rows) | done |
| 40 | End of Roberts; Belmonte and Papaspiliopoulos | `table-d1-p0040` (Table 1 of the contribution, rows) | done |
| 41 | Belmonte and Papaspiliopoulos | (45); `table-d2-p0041` (Table 2, rows) | done |
| 42 | End of Belmonte/Papaspiliopoulos; Łatuszyński and Papaspiliopoulos (algorithms 1-3 as text steps) | (46)-(51) | done |
| 43 | Algorithm 4; Flury and Shephard; Robert, Jacob, Chopin and Rue | (52), (53), (54) | done |
| 44 | Full-page sideways figure | `figure-d9-p0044` (Fig. 9) + caption | done |
| 45 | Full-page sideways figure | `figure-d10-p0045` (Fig. 10) + caption | done |
| 46 | End of Robert et al.; "The following contributions were received in writing after the meeting."; Anindya Bhadra | none | done |

Headings (all `###`, name and affiliation as printed): Rong Chen; Mark Girolami; Nick Whiteley; Gareth Roberts;
Miguel A. G. Belmonte ... and Omiros Papaspiliopoulos ...; Krzysztof Łatuszyński ... and Omiros Papaspiliopoulos ...;
Thomas Flury and Neil Shephard; Christian P. Robert and Pierre Jacob ..., Nicolas Chopin ... and Håvard Rue ...; Anindya Bhadra.

## Joins
- Set inside the range: p40 first item (`space`, continues p39 "... involves a substantial"); p42 first item (`space`, continues p41 "... (2003). When").
  On both pages the omitted running header was moved to the end of the item list so the joined item directly follows the previous page's text.
- Range start (36 -> 37): none needed; page 37 starts a new indented paragraph ("Similarly, Chopin (2007) ...").
- Range end (46 -> 47): none needed; page 46 ends with a complete paragraph ("... run of length 50000."), page 47 starts with Fig. 11.
- Sentences that run into a display on the next page (no join by convention): p37 "... to" -> p38 display; p40 "... state space model:" -> p41 (45);
  p43 "With parameter moves" -> p46 display (pages 44-45 are figure-only pages in between).

## Float placement
- p40: Table 1 (caption, table, dagger footnote) moved before the paragraph "In this contribution ..." which it interrupts.
- p41: Table 2 (caption, table, dagger footnote) moved before the paragraph "We also consider two different parameterizations ... When" which continues on p42.
- Table footnotes are text items beginning with the printed dagger "†" (they are table notes, not numbered footnotes).

## Tables
- Spanning headers ("Results for the following values of T:", "... signal-to-noise ratios:") merged into column headers ("T = 100", "Signal-to-noise ratio 0.05").
- Block labels (KF, SPF, PMMH, PG, Centred PG, Non-centred PG) are rows with empty cells. Minus signs kept as U+2212; "−0.0000" kept as printed.
- p39 table: stacked fractions written "num / {den}", two-line cells joined with "; ".

## Printed oddities kept verbatim (candidate typos in the source)
- p37: alpha(X^k_{1:n-1}) (k rather than N) in the bold alpha vector; M_n(.|X_{n-1}^{A}) in step (b); "M_{n-l}|X_{1:n-l-1}" without parentheses; "gamma_{t-1}(x_t - 1)"; "methods retains".
- p38: display "tilde pi^N = (b_n^k | ...)" with an equals sign.
- p39: table step-3 ratios in columns 3-4 print tilde pi without superscript N; row 0 Z non-bold.
- p41: (45) "eta_t, ~ NID(0,1)" stray comma; Table 2 labels l(mu_KF), V-hat(mu_KF) without hat on mu; "comptutational".
- p42: (47) missing closing parenthesis; "congraulate"; "Łatuszński".
- p43: (53) last bracket has U_{n-1} without tilde; "exp(xt)".
- p46: "AR(l)" with letter l; "lines of codes".

## Text repairs of substance
- p38 glued line restored ("The capabilities of existing MCMC techniques are being severely stretched, because in part of the increasing").
- p39 stray space before a full stop removed ("sampling . Here").
- p43 "likelihood-based" (line-wrap at a real hyphen), heading split from first paragraph; glued algorithm steps split on p42/p43.
- p44/p45: extractor's figure boxes included running header and caption; now header omitted, figure and caption separate.

## Formulas kept as images
None.

## Remaining diagnostics
All pages: category (a) only (LaTeX maths, U+2212 vs ASCII minus, decimals whose point the PDF encodes as ":", powers such as 10^4 read as "104", merged table headers, Unicode row labels). No category (b) items remain.

## Proposals / notes for the coordinator
- Asset names `table-d1-p0040` / `table-d2-p0041` are the contribution's own "Table 1"/"Table 2" (clash with main-paper numbering avoided); `table-d-p0039` is unnumbered.
- Figures on pp. 44-45 are printed sideways; crops are sideways as in the PDF. A plan note could mention this.
- A plan note could say that tables in the discussion carry dagger notes kept as text items after the table.
- Brief: `check` exits with status 1 when a page has diagnostics, which aborts `&&` chains; worth mentioning.

## Limitations
- Table cell values were compared visually with 200 dpi crops against the extractor's native text, not re-keyed independently.
- Bounding boxes of items split from extractor blocks (individual algorithm steps) are approximate subdivisions of the original box.
