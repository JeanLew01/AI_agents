# selim2022safe - conversion report

**Paper**: Selim, Alanwar, Kousik, Gao, Pavone, Johansson, "Safe Reinforcement Learning Using Black-Box Reachability Analysis" (IEEE RA-L 7(4), 2022).
**Source**: arXiv:2204.07417v2 [cs.RO], 21 Nov 2022, 8 pages, IEEE two-column preprint; authors' TeX source used for all mathematics.
**Result**: `verify --strict` exit 0, status `reviewed_with_limitations` (18 adjudications applied, 0 stale, mechanical_ok true).
**Package**: `~/AI_agents/paper2agent/Reachability/skills/selim2022safe-paper` (paper.md 458 lines; staging builds s1-s3; scripts in `logs/work/selim2022safe/`).

## Counts
- Figures 4 (Fig. 1-4, one crop each), tables 2 (Tables I, II as CSV + Markdown), algorithms 3 (image crop + line-numbered transcription each).
- Display equations 11 printed numbers: (1), (2), (3), (4a)-(4c), (5), (6), (7), (8a)-(8b); formulas kept as images: 0.
- Omitted regions 17: running header and page number on each of 8 pages, vertical arXiv stamp on p1.
- Adjudications 18 (pages 2-7: missing_lines, number_differences, independent_parser_number_differences); pages 1 and 8 clean.
- References 55, generated from the authors' `.bbl` and matched entry by entry against the PDF text layer.

## What was corrected
- Reading order: every page 1-7 has a float that cuts a sentence (Fig. 1, Alg. 1-3, Fig. 2-4, Tables I-II). Floats were placed after the paragraph that introduces them (in-page reordering only, no `reading_order`); six page-break sentences joined; six column-break paragraphs and one split reference merged.
- Math: all inline and display math rewritten from TeX with macros expanded; 13 extractor formula images replaced. pdflatex compiles all 11 displays and 266 inline formulas; rendered displays compared with the page.
- Headings (the extractor had made subsections level 1 and dropped two small-caps headings), theorem-like labels (Assumption 1-2, Definition 1, Theorem 1, Proof) in bold, compound hyphens at line ends, accents, 3 hyperlinks restored from PDF link annotations.
- Tables I-II had been swallowed into one figure image; now cell tables read from a 330 dpi crop and checked against the text layer and TeX.

## Limitations and things kept as printed
- p4, Algorithm 2: printed line 1 holds both the `Z_eps` assignment and the `for` header, so `M_j` is line 2. Kept as printed; it agrees with the text's "Line 1" / "Line 2" references.
- p4: the linearization point `x*_j` of Algorithm 2 is never defined in the printed paper. A commented-out TeX sentence says it is the centre of the current reachable set; this is given in the conversion notes, labelled as not printed.
- p7: bold (best values) cannot be stored in table cells; bold cells are listed in a note after each table, marked as added in conversion. Two-level headers are flattened ("Turtlebot BRSL", ...).
- p3, p5: italic bodies of assumptions/definition/theorem are not reproduced; block ends follow the TeX environments.
- p1: the five unnumbered first-page footnotes sit directly after the author line; "Abstract—" became a `## Abstract` heading.
- p6: the inline reward fraction is printed very small; taken from TeX and confirmed on a 330 dpi crop.
- Source slips kept (listed in the conversion notes): Lipschitz condition with only the state difference on the right (p3), `X_0 in R^n` in Definition 1 (p3), plan index `n_plan` vs `k + n_plan` (p3-5), non-bold `u_{k-1}` in (8b) (p5), Fig. 4 legend has SECAS but the caption does not (p7).
- No appendix or supplement exists in this version. One reviewer; no independent second verifier.

## Self-check
- No leftover damage in `paper.md` (no `<sup>`, replacement characters, stray hats, `~~`, `^*`; `$` count even; 18 real headings). Final body identical to staging s3.
- Opened `figure-4.jpg` (smallest labels; ticks, legends and sub-captions legible) and `algorithm-2.jpg` (complete, including line numbers and the dagger).
- Own checks: symbol counts (relations, operators, hats, Greek) equal between PDF text layer and LaTeX on all pages, 0 differing counters; word-multiset check shows no lost prose word; all "extra" numbers on p4-5 equal the algorithm transcription tokens with no residual.
- Question: "How is the reachable set computed from data, under which assumptions, and what is guaranteed?"
  Answer from the package: dynamics `x_{k+1} = f(x_k,u_k) + w_k` (2), `f` black-box, twice differentiable, Lipschitz (constant `L*`); Assumption 1 (translation invariance, braking in `n_brk` steps), Assumption 2 (`w_k` uniform on a noise zonotope `W = Z(c_w, G_w)`). Offline data matrices `X_-`, `X_+`, `U_-` (4a)-(4c), covering radius `delta`, `L*` and `delta` estimated per dimension. Algorithm 2: `Z_eps = Z(0, diag((L*)_i (delta)_i / 2))`; per step a least-squares model `M_j = (X_+ - c_w) [1; X_- - x*_j; U_- - u_j]^dagger`; residual bounds `l_low`, `l_up` by column-wise min/max; `Z_L = Z(l_low, l_up) - W`; `R_{j+1} = M_j(1 x (R_j - x*_j) x (U_j - u_j)) + W + Z_L + Z_eps`. Theorem 1: under the Section II assumptions, starting safe and adjusting every plan with Algorithm 3, the robot is safe for all `k >= 0`. The guarantee is deterministic and rests on containment from [42, Theorem 2]; there is no sample-size bound (500 offline steps, "formal analysis ... for future work").
  Found under "B. Robot and Environment", "A. Data-Driven Reachability Analysis", "C. Analyzing Safety", "IV. Evaluation"; checked against 300-330 dpi crops of PDF pages 3-6.

## New pitfalls (not yet in the brief)
- algorithm2e boxes can print two statements under one line number when the source lacks a line break; transcribe the printed numbering, do not renumber.
- Figures exported with LaTeXiT carry hidden `<latexit ...>` base64 text in the PDF text layer (p5: about 800 junk words). Exclude figure bboxes in your own word and symbol checks.
- The shared symbol checkers assume `\le`, `\|`, `\cdot`; with `\leq`, `\lVert`, `\cdots` (three dots each), `\mapsto` and `\neq` (text layer "̸ =") they report false differences. `logs/work/selim2022safe/symcheck.py` handles these and excludes figure crops.
- Spaces inside subscripts change number tokens: `k - 1` gives "1", `k-1` gives "-1". Write `k-1`, `h+2` without spaces so the Unicode-minus pairing is one to one.
- Do not repeat "Fig. N" in the added sub-caption sentence; it creates an extra number token.
- Markdown links `[text](url)` are stripped by the tool's tokenizer, so URLs from PDF link annotations (readable with pypdf from the uv environment) add no number differences.
- `logs/work/selim2022safe/refs.py` builds reference entries from a `.bbl` and compares their alphanumeric skeleton with the PDF text; this restores compound hyphens and accents without retyping.
- Unprinted TeX comments may hold definitions the PDF lacks. I reported one as labelled background in the conversion notes; the brief has no rule for this.
