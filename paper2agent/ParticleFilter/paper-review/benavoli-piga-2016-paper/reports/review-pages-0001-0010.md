# Review report: Benavoli & Piga 2016, pages 1-10

Document: `documents/s001-benavoli-piga-2016` (arXiv:1505.01034v2). Reviewer range: pages 1-10.
All ten pages are `reviewed: true` with `[v2]` notes. Adjudication notes exist for pages 1-10.
The mathematics was taken from the authors' TeX (`FilteringSM_v15.tex`), macros expanded, and compared with the page previews (zoomed crops for Algorithm 1, the refinement box, Figure 1 and the "(6)" references on page 6).

## Pages

| Page | Content | Equations (printed tags) | Assets |
| --- | --- | --- | --- |
| 1 | Title, authors, affiliations, title footnote, e-mails, preprint footer, Abstract, start of 1 Introduction | none | none |
| 2 | Introduction (contributions) | none | none |
| 3 | End of Introduction, 2 Problem Description, Example 1, Problem 1, start of 3 | (1), (2a), (2b), (3), (4), (5) | none |
| 4 | Section 3, 3.1, Proposition 1, footnotes 1-4 | (6), (7), (8) | none |
| 5 | 3.2, Theorem 1 (Prediction) and proof, Theorem 2 (Updating), footnote 5 | (9)-(15) | none |
| 6 | Proof of Theorem 2, Algorithm 1, Remark 1, start of Remark 2, footnote 6 | (16)-(19) | `algorithm-1` (image + transcription) |
| 7 | End of Remark 2, Section 4, Theorem 3 and proof, footnote 7 | (20)-(25) | none |
| 8 | Refinement of Algorithm 1, Theorem 4 (Box approximation), Section 5, Theorem 5 and proof, Remark 3, 5.1, footnote 8 | (26)-(29) | `algorithm-1-refinement` (image + transcription) |
| 9 | Definition 1, SOS relaxation, remarks (1)-(4), Corollary 1, start of Example 2 | (30)-(35) | none |
| 10 | End of Example 2, Figure 1, Section 6, 6.1 | (36), (37), (38) | `figure-1` + caption |

No tables in this range. No formula was kept as an image.

## Joins

- Within pages: column-break continuations on pages 1, 2, 4, 6, 8, 9 (`space`); page 6 "The" + "steps A1.2.1 ..." around the Algorithm 1 float.
- Across my pages: 1->2 `none` ("correspond|ing"), 2->3 `none` ("pro|cedure"), 3->4 `space`, 5->6 `space`, 6->7 `space`, 9->10 `space`. No join 4->5 (list follows a complete sentence), 7->8, 8->9.
- Range boundary: page 10 ends with `p0010-b020` ("... uniformly distributed in $\mathcal{B}$,") as its last emitted item; page 11's first item already has `join_previous: space`. Nothing further needed.
- Paragraphs resuming after a display equation ("where ...", "with") are separate items without `join_previous`, so each `$$` block stays on its own lines.

## TeX versus PDF

- Page 6: the PDF prints "(6)" twice ("or equivalently by (6)", "defined in (6)") where the TeX references the unnumbered set definition of Problem 1. Kept "(6)" as printed; equation (6) on page 4 is a different formula. A reader may be misled; a plan note could say so.
- Page 10: the h_1..h_4 display carries (36) on the h_1 line and a stray (37) on an empty line after h_4 (trailing line break in the authors' align). Written as two blocks, `\tag{36}` for h_1 and `\tag{37}` for h_2-h_4.
- Page 9, Corollary 1: PDF breaks "half-|space", TeX has "halfspace"; written "halfspace".
- Page 10 caption: PDF breaks "half-s-|pace"; written "half-space".

## Authors' errors kept as printed (listed in each page's review_notes)

- p2: italic $M$ instead of $\mathcal{M}$ once. p3: $\mathbf{C}_{k-1}$ in Example 1; "zonotops".
- p5: missing full stop before "Hence"; "Qr". p6: "steps A1.2.1 and A1.2.1" (second should be A1.2.2).
- p7: stray ")" in $\mathbf{y}^k)$; bold subscript $\delta_{\mathbf{\hat{x}(k)}}$.
- p8: refinement steps are named A1.1.3/A1.1.4. p9: "less then or equal"; $\boldsymbol{\omega}^T$.
- p10: both squared terms of h_2 start with $x_1(1)$; unbalanced parenthesis in "(see, e.g. [50,51]. ...)".

## Text repairs of substance

- p3: closing line of Problem 1 ("for each $k=1,2,\ldots,T_{\mathrm{o}}$." with end mark) was missing from the extraction; added. "Problem 1 [Set-membership filtering]" was a heading; now a bold label.
- p5, p6, p9: column interleaving repaired. p8: line "where $\boldsymbol{\omega}\in\mathbb{R}^n$, ... [^8]" after (27) was missing; added.
- p9: Definition 1's second sentence was scrambled by the extractor; restored.
- p8: the refinement box body had been turned into a heading; now image plus transcription.
- New items created by splitting: `p0002-r01`, `p0004-r01` (footnote 2), `p0006-r01`, `p0008-r01` (transcriptions), `p0008-r02`.

## Conventions used

- Headings: `#` title, `## Abstract`, `## N Title` for sections, `### N.M Title` for subsections (matches pages 11-20).
- Theorem-like labels bold (`**Theorem 1 (Prediction)**`, `**Proof:**`, `**Remark 1**`, `**Example 1**`, `**Problem 1 [Set-membership filtering]**`, `**Definition 1**`, `**Corollary 1**`, `**Proposition 1**`). Statements printed in italics are written upright.
- Footnotes: `[^n]` markers, `Footnote n:` items. The title footnote is written `Footnote ⋆ (attached to the paper title): ...`; the star is not in the heading, so that the builder's duplicate-title detection still works.
- "Preprint submitted to Automatica" and "6 November 2018" (page-1 footer) are kept as text after the author block; the rotated arXiv stamp and page numbers are omitted.
- Enumerations printed "(1)", "(2)" are written that way, not as Markdown lists.

## Remaining diagnostics (all category a)

| Page | Missing lines | Number differences | Cause |
| --- | --- | --- | --- |
| 1 | 3 | none | author superscripts, $\mathcal{P}$ |
| 2 | 13 | none | calligraphic symbols |
| 3 | 37 | yes | LaTeX maths; U+2212 vs ASCII minus |
| 4 | 42 | second parser only | LaTeX maths; footnote markers |
| 5 | 46 | yes | LaTeX maths; minus glyph |
| 6 | 53 | yes | LaTeX maths; Algorithm 1 transcription numbers (text inside the image) |
| 7 | 40 | none | LaTeX maths |
| 8 | 48 | extras only | LaTeX maths; refinement-box transcription numbers |
| 9 | 64 | yes | LaTeX maths; minus glyph |
| 10 | 47 | yes | LaTeX maths; $-0.2^2$, $-0.4^2$, under-brace labels |

## Proposals for shared files

- `plan.json` note: "References to '(6)' on PDF page 6 point, in the authors' source, to the unnumbered definition of $\mathcal{X}_k$ in Problem 1 (page 3), not to equation (6)."
- `plan.json` note: "Equation number (37) is a stray tag printed after the constraint list h_1..h_4 of Example 2; (36) labels h_1."
- Asset names in this range: `figure-1`, `algorithm-1`, `algorithm-1-refinement` (no clash with algorithm-2, algorithm-3, figure-2..8).

## Limitations

- Text-item bounding boxes were inherited from the extractor (unions when merging, estimated splits for new items); only the three asset boxes were checked with crops.
- The mathematics was compared with previews at preview resolution, plus zoomed crops where symbols were small; not every display was zoomed.
- No build was run (coordinator's task), so rendering of `\tag` inside `aligned`/`array` blocks and of text joined directly after footnote-free paragraphs is untested.

## Notes on the brief

- The brief does not say whether a paragraph resuming after a `$$` display should use `join_previous`; sibling collections do both. I left them unjoined.
- Running a page script twice against an already edited page fails when items were merged; I kept originals of pages 5-10 in the scratch directory (`orig/`). Pages 1-4 scripts are not re-runnable.
