# liu2025recurrent - reviewer report

**Paper:** J. Liu, E. Mallada, "Recurrent Control Barrier Functions: A Path Towards Nonparametric Safety Verification" (CDC 2025).
**Source:** arXiv:2510.02127v1, 8 pages, IEEE two-column; authors' TeX source used (main.tex, edits.tex, main.bbl).
**Status:** `verify --strict` exit 0, status `reviewed_with_limitations` (mechanical_ok, 10 adjudications applied, 0 stale, no issues).
**Package:** ~/AI_agents/paper2agent/Reachability/skills/liu2025recurrent-paper (13 files; paper.md 706 lines).
Builds: staging s1, s2 (diagnostics identical), final rebuilt once after a one-line label fix on page 4.

## Counts
- Figures 3 (Fig. 1-3, crops + verbatim captions). Tables 2 (TABLE I, II as cells/CSV). Algorithms 4 (crop + line-by-line transcription each).
- Displays 47 as `$$` blocks, printed tags (1)-(20); formulas kept as images: 0. Inline math 462.
- Omitted regions 1 (vertical arXiv stamp, p1). Adjudications 10: missing_lines on p1-p8, number_differences and independent_parser_number_differences on p6 only.
- Theorem-like blocks: Assumptions 1-2, Definitions 1-8, Theorems 1-5, Lemma 1, four proofs + Appendix A proof. References [1]-[20], all read.

## What was corrected
- Reading order on every page (p6: four fragmented algorithm boxes interleaved across columns; p7: columns interleaved around three floats).
- All math rewritten from TeX with macros expanded; 45 extractor formula items replaced (43 displays, 1 misclassified heading "IV. ...", 1 text line); flattened displays (4), (10), (12), (16), (19), Def. 3 set restored.
- Headings (## sections, ### subsections), bold labels with printed names, statement ends taken from TeX environments (listed in conversion notes).
- Tables: wrong column split in TABLE II fixed; references: bullets removed, [19] title/URL debris repaired.

## Checks beyond the tool (scripts in logs/work/liu2025recurrent/)
- `linecheck.py`: after mapping LaTeX back to text-layer glyphs, 872 of 876 text-layer lines (incl. algorithm boxes) are substrings of the page text; the 4 others are stacked sub/superscript fragments (p6) and the integral glyph (p8).
- `charcheck.py`: per-page multiset of letters/digits/Greek equal on all pages, except 3 glyph codes ('n' = cases brace p3, 'p' = radical p6, 'Z' = integral p8) and the 74 characters of the repeated sub-captions (p7).
- `symbol_check3.py`: counts of 30+ relation/operator/decoration symbols equal on all pages (3 explained glyph differences).
- `wordcheck.py`: no prose word lost. `mathcheck.py`: 47 displays + 270 unique inline compile; displays compared visually with the PDF.
- Number diagnostics: none on 7 pages; p6 extras equal exactly the algorithm-transcription tokens plus Unicode/ASCII minus in [-1,1].

## Limitations / uncertainties (by page)
- p1: the two unnumbered footnotes (affiliation, funding) sit after the author line; "Notation:" kept as run-in italic text, not a heading; "Abstract—" turned into a heading.
- p2-p5: italic theorem bodies not reproduced; ends of statements documented in the conversion notes. p4: "Proof." and the bold title "(i) Control ..." are one bold run.
- p3-p8: authors' slips kept verbatim and listed in the notes (e.g. `re^{-Lt}` and italic `R_{t*}` in proof of Thm 4, `h(y,u,t)` in (17), tau vs tau-hat in Thm 3, "(14) and 20", alpha = 1 in TABLE II caption, undefined g and unmatched `|` in the Appendix). None is a TeX/PDF disagreement.
- p6: Algorithm 2 line 5 is printed slightly less indented than line 4; transcribed at the same level.
- p7: table header cells are plain text ("Methods \ r_min"); the Markdown table in paper.md shows `\\` (CSV is correct); bold of the Recurrent Set times in TABLE II only described in the notes; meaning of the check/cross marks is not defined by the paper. Figure 3 placed after the VI-B paragraph (same page). Sub-captions repeated in captions.
- p8: [18] page range thin spaces -> ordinary spaces; [19] letter-spaced URL closed up.
- One reviewer only; no independent second verifier. The run was interrupted once (machine restart) before any page was saved; all pages were redone from the saved renders.

## Self-check
- SKILL.md (no draft line), index.md (20 navigation rows), whole paper.md read; no `<sup>`, replacement characters, glyph soup or `** **`; `$` count even.
- Assets opened: figure-3 (smallest labels), figure-2, figure-1, algorithm-1, algorithm-3, both CSVs: complete and legible.
- Question: "State Theorem 3 with all assumptions and the bound on tau-hat." Answer from paper.md, Section "C. Signed Distance Function: a Valid RCBF" (lines 253-274): h a CBF satisfying (2) and sector containment (9) over D_0 := h_{>=-c}, c > 0, a_2 > a_1 > 0, class-K function kappa_{alpha,beta} of (10), alpha, beta > 0; for any closed S with h_{>=0} ⊆ S ⊆ h_{>=-c} and ∂S ∩ h_{=0} = ∅, h-hat = -sd(., S) is an RCBF over D-hat_0 := h-hat_{>=-c-hat} (c-hat >= 0 largest with h-hat_{>=-c-hat} ⊆ h_{>=-c}); (11) holds with gamma-hat = gamma_{alpha-hat,beta-hat}, alpha-hat > alpha, beta-hat < beta, and tau-hat >= max{log(a_2/a_1)/(alpha-hat - alpha), log(a_2/a_1)/(beta - beta-hat)} + log(delta-bar/delta-underbar)/min{alpha-hat, beta-hat}, delta-bar/underbar = sup/inf over x in D_0 of sd(x,S) - sd(x,h_{>=0}). Matches the 250 dpi crops of PDF page 4.

## New pitfalls (not yet in the brief)
- `accept.sh` counts `** **` as damage; two adjacent bold runs such as `**Proof.** **(i) Title.**` trigger it. Write one bold run.
- The text layer encodes large delimiters as letters: cases brace = 'n', radical = 'p', integral = 'Z'; tall restriction bars are absent; "neq" is a combining slash plus '='. These explain single-character residues in character-level checks.
- With TeX available, `charcheck.py` + `linecheck.py` (character multiset and line-substring test after de-LaTeX) reduce ~300 "missing lines" to 4 fragments; more decisive than word checks. `symbol_check2.py` misses `\leq`, `\geq`, `\rightarrow`, `\gets`; `symbol_check3.py` counts them and scans the algorithm transcriptions too.
- Check compile flags in the TeX source: here `\setboolean{arxiv}{false}` selects the branch WITH full proofs and appendix. The source also holds unprinted author comments (`\enrique{}`, `\jixian{}`) that must not be transcribed.
- `verify ... | tail; echo $?` reports tail's status; redirect the output to a file to get the real exit code.
- I ran `logs/accept.sh` once by mistake (piped to `head -0`); it stopped before linking, and no ~/.claude/skills/liu2025recurrent-paper link exists.
