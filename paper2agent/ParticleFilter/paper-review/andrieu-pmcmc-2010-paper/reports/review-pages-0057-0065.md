# Review report: Andrieu, Doucet, Holenstein (2010), PDF pages 57-65

All nine pages are reviewed (`reviewed: true`, notes start with `[v2]`). No TeX source; all mathematics transcribed
from 300-450 dpi crops. Build script kept at `_scratch/andrieu-57-65/build.py`.

## Pages
| Page | Content | Assets / equations | check |
| --- | --- | --- | --- |
| 57 | full-page Fig. 17 (Lopes/Johannes/Polson contribution from p. 56) | figure-d17-p0057 | (a) caption maths |
| 58 | end of the p. 56 paragraph; Johansen and Aston; Fig. 18 | figure-d18-p0058 | (a) |
| 59 | Johansen/Aston end; Lee and Holmes; Maskell | eq. (55), unnumbered acceptance ratio | (a) |
| 60 | full-page Fig. 19 (Lee and Holmes) | figure-d19-p0060 | OK |
| 61 | Maskell end; Murray et al.; Peters and Cornebise start | inline maths only | (a) |
| 62 | Peters/Cornebise list (a)-(d); Silva, Kohn, Giordani, Pitt | two unnumbered ABC displays, one integral display | (a) |
| 63 | Silva et al. list (b)-(e); Toivanen and Lampinen; Fig. 20 | figure-d20-p0063 | (a) |
| 64 | Toivanen/Lampinen end; Yun and Chen; Fig. 21 | figure-d21-p0064 | (a) |
| 65 | Yun/Chen end; start of the authors' reply | RMSE display, eq. (56) | (a) |

All remaining diagnostics are category (a) (LaTeX versus text-layer glyphs, U+2212 versus ASCII minus, caption
marker glyphs, the restored digit in 'PIMH-Reuse1'); adjudication notes written for pages 57-59 and 61-65.
No formulas kept as images. No tables or algorithms in this range.

## Joins
- p58 first item: `join_previous: space`, continues p56's last paragraph ("...assumption 4 is satisfied in the").
  **Page 57 holds no prose** (only Fig. 17 and its caption), so the item directly before it in file order is the
  Fig. 17 caption. The coordinator's note asked for the continuation to be emitted before Fig. 17: this needs a
  `plan.json` `reading_order` (shared file, not edited by me) that puts `p0058-b001` before `p0057-b002`,
  `p0057-b003`.
- p61 first item: `join_previous: space`, continues p59's last sentence across full-page Fig. 19 on p60. Same
  problem: `reading_order` must put `p0061-b002` before `p0060-b001`, `p0060-b002` (or after p59's `p0059-b013`).
- p59 first item (space, from p58), p64 first item (space, from p63): in range, fine as is.
- Fig. 18, Fig. 20, Fig. 21 were printed inside a paragraph; each is moved in front of that paragraph within its page.
- p65 starts with a display (RMSE) that completes p64's sentence "...and the estimates:"; no join (display).
- **Boundary to p66:** p65 ends with `p0065-b012` ("In broad terms PMCMC algorithms are valid") as its final item;
  `p0066-b001` ("(a) when unbiasedness...") joins onto it with `space` (set by the reviewer of 66-74).

## Decisions to harmonise
- Authors' reply: `### The authors replied later, in writing, as follows` (p65). The three italic titles on p65
  ("What the users say", "Correctness and sequential Monte Carlo implementations", "Valid sequential Monte Carlo
  implementations") are italic text items (`*...*`), not headings, per the coordinator's note.
- Fig. 20 is printed on p63 inside Toivanen and Lampinen's text but belongs to Yun and Chen (p64-65).
- New item ids: `p0062-x_or`, `p0062-x_abc2` (split of one formula image), `p0065-x_hdr` (missing header omit).

## Text repairs and printed peculiarities
- 'PIMH-Reusel' (letter l in the text layer, twice on p65) written 'PIMH-Reuse1' per the coordinator's digit note.
- Thin-space digit grouping removed (300000, 10000, 50000, 13065, 40000, 1000000).
- Kept as printed: p62 second ABC display has `y_{n-1}` in the denominator proposal (first display `y_n`);
  `y_n^k(S)` with capital S after the displays; p65 eq. (56) has `W_T^{*K}` (capital K) and lower-case
  `\hat z^{N,*}` over a sum of capital `\hat Z^{N,*}`; p59 acceptance ratio `q(θ',θ)` over `q(θ,θ')`;
  p58 `N(y_n|x_n,1)`; p61 'ecosytem'; p63 'test image, Owing'.
- Caption line-style and marker keys are approximated by characters/Unicode symbols.

## Limitations / brief feedback
- Items cannot be moved across pages, so paragraphs that straddle a full-page figure can only be fixed through
  `reading_order`; the brief could say this explicitly.
