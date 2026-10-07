# Review report: Raices Cruz et al. 2022 (arXiv:2206.08728v1), PDF pages 11-19

Reviewer range: pages 11-19 (all `reviewed: true`, notes start with `[v2]`). Pages 1-10 untouched.
TeX source used for all mathematics (`article-arxiv.tex`); `\Var` expanded to `\mathrm{Var}`, `\coloneqq` written `:=`.
No TeX-versus-PDF disagreement was found in this range. No formulas kept as images.

## Per page

| Page | Content | Assets / equations | State |
| --- | --- | --- | --- |
| 11 | End of 5.4; Tables 1-3 with captions | `table-1`, `table-2`, `table-3` (10-column string tables) | done |
| 12 | 5.5 (set M' display, unnumbered); Table 4; 6. Conclusions | `table-4` | done |
| 13 | End of Conclusions; Supplementary material, Acknowledgement(s), Disclosure statement, Funding; References [1]-[9] | - | done |
| 14 | References [10]-[26] | - | done |
| 15 | References [27]-[43] | - | done |
| 16 | References [44]-[47]; Appendix A. Calculations | eq. (35), (36)-(39) + 3 unnumbered displays | done |
| 17 | End of App. A; Appendix B. Delta method | (40)-(42), (43), (44), (45), (46) | done |
| 18 | Appendix C. Proof of existence of minimum | (47), unnumbered density, (48), (49), (50)-(52), (53) | done |
| 19 | End of App. C; Appendix D. Lemmas (Lemma D.1, Lemma D.2 with proofs) | (54), (55)-(62) | done |

No figures or algorithms in this range (Figures 1-3 are on pages 8-10, other reviewer; names `figure-1..3` are free of clashes with my `table-1..4`).

## Joins
- Set: p11 first item (`p0011-b002`, continues "It takes much longer time to run a" from page 10) `join_previous: space`; p13 first item (`p0013-b002`, continues page 12) `space`.
- Needed from the other reviewer: none beyond page 10 ending with the continuing paragraph as its last emitted item (no float/footnote after it).
- Pages 16->17, 17->18, 18->19 break between paragraphs/displays; no joins.

## Conventions and decisions worth harmonising (coordinator)
- **Run-in numbered subsection title**: "5.5. The influence of prior data conflict." is printed run-in (amsart) but is a `\subsection`; I split it into a `### 5.5. The influence of prior data conflict` heading. Pages 1-10 have the same pattern (5.1-5.4 and probably earlier); the other reviewer should use the same form or I should be told to revert.
- **Multi-numbered aligned displays** ((36)-(39), (40)-(42), (45)/(46), (48)/(49), (55)/(56), (57)/(58), (59)/(60), (61)/(62)): one `$$` block per printed number; continuation blocks start with `=` or `\approx`. Described in each page's notes.
- **Tables 1-4**: header cells are plain Unicode (`μ0*`, `τ0*`, `ESS_MCMC`, `ESS_IS`, `μ̂(μ0*, τ0*)`) because of the no-backslash rule; an added editorial item "Transcription note (column headers ... as printed): ..." after Table 3 (p11) and Table 4 (p12) gives the LaTeX symbols. Remove those two items (`p0011-n01`, `p0012-n02`) if editorial text is unwanted. Multirow labels: "Grid Search" joined to one cell, "IIS" repeated per row.
- Proofs: printed italic "Proof." written as `**Proof.**`; end-of-proof box as `$\square$`.
- Appendix headings keep printed form: `## Appendix A. Calculations` etc.
- Plan title in `plan.json` is still the slug `raices-cruz-robust-is-mcmc-2022`; proposal: full paper title, and a note that the source is the arXiv v1 preprint of the CSDA 176 (2022) article.

## Text repairs of substance
- p13: URL `https://github.com/Iraices/IIS_MCMC` (underscore had become strike-through markup).
- References: merged entries split ([18]/[19], [28]/[29], [40]/[41]); diacritics recomposed (Gårdmark, Víctor, Bürkner, Ríos, Martín, François, Röver, Håvard, Inés, Sébastien); wrapped identifiers restored (doi 10.1186/s13750-015-0032-9, ISSN 0167-7152, doi 10.1007/978-3-319-41192-7, doi ...65052-4_4, doi ...48056-5_10, ISSN 0165-1684, two URLs in [33], [34]).
- Printed oddities kept: "Andrew M. Stuart Stuart" [1], "Anna Gårdmark A." [4], "doi:doi:" [7], ISSNs without hyphen in [11], [21]; "the minimum exist", "the set of prior".
- p16, p19: prose lines that the extractor had hidden inside formula boxes restored as text.

## Remaining diagnostics (all category (a); adjudication notes written for pages 11-19)
- 11, 12: inline maths lines, table header cell, ASCII minus, digits of the editorial transcription notes.
- 13, 15: number tokenisation of re-hyphenated DOI/ISSN only (13 has full line coverage); 15 one line with "V´ıctor".
- 14: two lines with decomposed accents in the PDF text layer; DOI tokenisation.
- 16-19: display/inline maths in LaTeX; minus-glyph differences.

## Limitations
- Text-item bboxes for newly split items (ids `pNNNN-nXX`, `...x`) are approximate (estimated from the preview), which does not affect output; table bboxes were checked on an overlay.
- Rendering of `\Biggl\{` etc. assumes a MathJax/KaTeX-style renderer.

## Brief feedback
- The brief says headings for lettered appendices look like `## A. ...`; this paper prints "Appendix A. Calculations", which I kept. The run-in numbered subsection case (amsart) is not covered by the brief.
