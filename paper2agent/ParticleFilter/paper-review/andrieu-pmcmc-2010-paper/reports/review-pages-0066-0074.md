# Review report: Andrieu, Doucet, Holenstein (2010), PDF pages 66-74

Range: the end of the authors' written reply (journal pp. 334-339) and "References in the discussion" (pp. 339-342, end of document). No TeX source; all maths transcribed from 230-280 dpi crops.

## Per-page log
- **Page 66** done [v2]. Reply prose. List items (a)/(b) as text; (a) joined (space) to page 65's last sentence. Italic run-in titles "Large state spaces", "General proposals for particle Metropolis–Hastings algorithms", "Smoothing" changed from extractor headings to italic text items. Inline maths only. Authors' typo "Andrieu amd Thoms (2008)" kept. Diagnostics: 7 missing lines, all (a).
- **Page 67** done [v2]. First item joined `none` ("frame" + "work"). One unnumbered display ($\check{\pi}^{KN}(\mathrm{d}x)=\frac1K\sum_k\hat{\pi}_k^N(\mathrm{d}x)$; note check accent on the left, hats on the right). Italic title "Performance and the choice of $N$: from theory to practice" as text. Restored hyphen in "random-walk". Diagnostics: 7 missing lines (a); second parser `1` vs `+1` (a).
- **Page 68** done [v2]. First item joined (space). Three unnumbered displays (extended target $\tilde{\pi}^N(k,x^{1:N})$; empirical distribution $\hat{\pi}^N(\mathrm{d}x)$; unbiasedness identity) converted from formula images to LaTeX text. Gibbs steps (a)/(b) split out into new items `p0068-b005a`, `p0068-b005b`. Italic titles "Unbiasedness versus sampling", "Using sequential Monte Carlo methods with Markov chain Monte Carlo moves" as text. Diagnostics: 26 missing lines (a); `−1` vs `-1` (a).
- **Page 69** done [v2]. First item joined (space). Figure 22 = `figure-d22-p0069` + caption, moved between paragraphs 2 and 3 so the page ends with the paragraph continuing onto page 70. Diagnostics: 9 missing lines (a); number difference `000` vs `1000` (PDF text layer has "l000" with a letter l for the printed 1000; (a)).
- **Page 70** done [v2]. First item joined (space). Figure 23 = `figure-d23-p0070` + caption at the end (last prose paragraph is complete). Diagnostics: 7 missing lines (a); `−1` vs `-1` from $(N-1)T$ (a).
- **Page 71** done [v2]. Italic title "Some past and future work" as text; last reply paragraph; `## References in the discussion`; 24 reference entries, one item each (first two entries split: `p0071-b004`, `p0071-b004b`). Diagnostics: 1 missing line (a, inline maths).
- **Page 72** done [v2]. 31 reference entries, one item each (Del Moral and Guionnet entry merged; `p0072-b008` removed). check: OK.
- **Page 73** done [v2]. 33 reference entries (split `p0073-b032`/`p0073-b032b`; Kendall et al. author list re-spaced; URL rejoined). Diagnostics: 1 missing line (a, `$\alpha$-stable`).
- **Page 74** done [v2]. 24 reference entries; URLs rejoined; Wang (2007) re-spaced. check: OK. End of document.

## Assets
- `figure-d22-p0069` (Fig. 22, five histogram panels (a)-(e)), bbox [72, 333, 419, 606].
- `figure-d23-p0070` (Fig. 23, two panels (a), (b)), bbox [36, 301, 443, 606].
- No tables, no algorithms, no formula images (all symbols legible in crops). No numbered equations in this range; four unnumbered displays (one on p67, three on p68).

## Joins
- Set: p66 first item `space` (onto page 65's "In broad terms PMCMC algorithms are valid"); p67 `none` (frame|work; hyphen removed on p66); p68, p69, p70 `space`.
- Not set on purpose: text following a display (p67 "and use a stratified ...", p68 "which by standard arguments ...", "for $q(k,x^{1:N})=\ldots$"), per assignment.
- **Boundary to page 65 (other reviewer):** page 65 must end with the text item "... In broad terms PMCMC algorithms are valid" as its last non-omitted item (it currently does, `p0065-b012`), since `p0066-b001` joins onto it. No footnote may be placed after it.
- No boundary after page 74 (end of document).

## Conventions used
- Italic run-in titles inside the authors' reply are italic text items (`*Smoothing*`), not headings, per the assignment ("italic run-in titles stay text"). The reviewer of page 65 should do the same for "Valid sequential Monte Carlo implementations" etc. (the extractor emitted them as `#` headings) so the reply is consistent; if the coordinator prefers `####` headings for navigation, change both ranges together.
- References: one text item per entry, printed style, `*journal*`, `**volume**`; no list dashes.
- Thousands printed with thin spaces (300 000, 12 000, 100 000) are written without a space, as in the PDF text layer.

## Text repairs of substance
- p69: "l000 times" (text layer) -> "1000 times" (as printed).
- p68: final ":" after "for $l=1,\ldots,m$" -> "." (as printed); "Łatuszyński" accents on p68/p73; "Tadić" on p71.
- p72: URL tilde U+223C written as ASCII `~`; p74: `PS_cache` underscore restored in the arXiv URL; URLs rejoined across line breaks on p73/p74.
- Printed typos kept: "Andrieu amd Thoms" (p66), "Berthelesen" (p71), "genetic alogrithms", "Bethelehem", "Hamze F." (p72), "probabilites" (p73), "configurational-based" in the reply text versus "Configurational-bias" in the reference (p71/p74), $x_k\sim\pi$, $x_l\sim\pi$ with subscripts on p68 where the surrounding text uses superscripts; Fig. 22/23 captions use $b_1,b_2,b_3$ where the text uses $\beta_1,\beta_2,\beta_3$.

## Remaining diagnostics
All category (a); adjudication notes written for pages 66, 67, 68, 69, 70, 71, 73. Pages 72 and 74 are OK.

## Proposals / limitations
- No plan.json changes needed. Asset names follow the `figure-dN-pPPPP` rule, so no clashes.
- The lower half of page 74 (Storvik ... Zhong) was compared against the 110-dpi preview rather than a high-resolution crop; the text is clean and check is OK.
- Brief feedback: nothing wrong; the stderr warning note was helpful.
