# Review report: haj-chhade-box-messages-2014, PDF pages 1-8

Reviewer range: pages 1-8 (printed pages 455-462). No TeX source; all mathematics transcribed from 200-dpi crops.
All eight pages are `reviewed: true` with `[v2]` notes. Adjudication notes written for pages 1, 3, 4, 5, 6, 7, 8 (page 2 is `OK`).

## Per page

| Page | Content | Floats / assets | Display equations | Check state |
| --- | --- | --- | --- | --- |
| 1 | Title, authors, journal line, dates/licence, abstract, keywords, affiliations | none | none | 1 missing line (envelope glyph "(B)" written "(✉)"), category (a) |
| 2 | `## 1 Introduction` | none | none | OK |
| 3 | Introduction (cont.), numbered list 1-4, `## 2 Graphical Models` | none | none | 2 missing lines, inline maths (a) |
| 4 | `### 2.1 Markov Random Fields` | Figure 1 -> `figure-1` | (2.1), (2.2), (2.3) | 11 missing lines + second-parser "1"x7, all maths (a) |
| 5 | `### 2.2 Inference in Graphical Models`, `## 3 Belief Propagation Algorithm` | Figure 2 -> `figure-2` | (2.4), (2.5) | 16 missing lines, all maths (a) |
| 6 | Section 3 (cont.) | Figure 3 -> `figure-3` | (3.1), unnumbered proportionality after "Noting that", (3.2), (3.3), (3.4), (3.5) | 19 missing lines, "−1" vs "-1" number differences, all maths (a) |
| 7 | Section 3 (cont.), `## 4 Nonparametric Belief Propagation` | Figure 4 -> `figure-4` | none | 2 missing lines, inline `p(x_t|y)` (a) |
| 8 | Section 4 (cont.) | none (Figure 5 is on page 9) | (4.1), (4.2), (4.3), (4.4) | 23 missing lines + second-parser "1"x1 (1/N), all maths (a) |

## Joins
- Set inside my range: page 3 first item (space), page 4 first item (space), page 5 first item (space), page 8 first item (space).
- Page 5 -> 6, 6 -> 7: paragraphs complete, no join.
- Boundary 8 -> 9: page 8 ends with the complete paragraph "... presented in the next section."; page 9 starts with Figure 5. **No join needed.**

## Float placement
- Page 4: Figure 1 and its caption were moved before the paragraph "Pair-wise MRFs ..." so the page ends with the prose continuing on page 5 (printed position: page bottom).
- Pages 5 and 6 end with a figure after a complete paragraph/equation; page 7 starts with Figure 4 (as printed).
- Figure boxes (tightened from full-page-width extractor boxes; all labels verified in crops): figure-1 [208,473,338,643], figure-2 [182,540,364,653], figure-3 [155,448,390,652], figure-4 [158,53,388,225].

## Formulas kept as images
None. All 13 display equations on pages 4-8 were legible and are LaTeX text items.

## Text repairs of substance
- Glued words un-glued: abstract line 3 (page 1), first line of last paragraph (page 2), "arerepresentedbyacollection" etc. (page 8).
- Control/replacement characters were Greek capitals: Γ (pages 4, 6), Ω (page 8).
- Fig. 1 caption factorisation rebuilt from `<sup>` debris.
- Page 1: first-page journal citation line and journal name kept as text (bibliographic metadata); Birkhäuser logo omitted via a new omit item `p0001-logo`.

## Printed peculiarities kept as printed (not corrected)
- Page 3: "e.g quantized", "The use of this approach involve", "using interval techniques result".
- Page 6: (3.4) has superscript i on the incoming messages m_ut (not i-1 as in (3.2)/(3.3)); (3.1) integrates "dx" over subscript "x \ x_t" with non-bold x.
- Page 7: "belief Propagation". Page 8: "( the observation model", "non Gaussian"; (4.2) has no hat on m; (4.4) has no final punctuation.
- Upright single letters in running text (G, V, E, A, B, D, C, Z, t, s, i, N, f) are left as plain text where printed upright, LaTeX where printed italic.

## Proposals for shared files
- `plan.json` title is the placeholder "haj-chhade-box-messages-2014"; proposed: "Non Parametric Distributed Inference in Sensor Networks Using Box Particles Messages".
- Asset names used: figure-1 .. figure-4 (printed numbering; the PDF has Fig. 1-16, Table 1-3, Algorithm 1-3, so no clash if the other ranges use printed numbers).
- Equation numbering is section-wise ((2.1), (3.2), (5.13) ...); tags are written `\tag{2.1}`.

## Limitations / brief feedback
- The envelope glyph on page 1 leaves one permanent "missing line" diagnostic (adjudicated).
- Brief was clear; nothing costly. `check` output is dominated by a pypdf fontTools warning that has to be filtered out.
