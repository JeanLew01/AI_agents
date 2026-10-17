# LLaDA page review: pages 10-22 (reviewer r2)

Scope: end of Section 4, Section 5, Acknowledgements, References [1]-[125] (pp. 10-18), Algorithms 1-5 (pp. 19-21),
Appendix A (equations (7)-(16)), A.3, start of Appendix B / B.1 (p. 22).
Scratch: `/home/jixia/AI_agents/paper2agent/Diffusion/paper-review/_scratch/r2`.

## Per-page log

### Page 19 - done ([v2], reviewed)
- Algorithms 1-3: `algorithm-1`, `algorithm-2`, `algorithm-3` (figure crops, rules verified) + line-by-line transcriptions.
- Equations (7), (8) as `$$ \tag{} $$` text (were formula images).
- Order change: heading `## A Formulation of Masked Diffusion Models` moved above the three algorithm floats (printed
  above the heading) so the algorithms sit in Appendix A, not under References. `### A.1 Training` follows them.
- Paragraph split repaired (MDMs [16-20] ... / These models introduce ...).
- Remaining diagnostics: maths-only missing lines and extra digits from the transcriptions/tags (category a).
- Join needed: p. 20 first paragraph continues "At $t = 1$, all" -> `join_previous: "space"` on p. 20.

### Page 20 - done ([v2], reviewed)
- Algorithm 4: `algorithm-4` (figure crop) + transcription (14 lines, nested loops/if).
- Equations (9), (10), (11) as `$$ \tag{} $$` text (were formula images).
- Order change: printed Algorithm 4 float interrupted the sentence from p. 19; continuation paragraph first
  (`join_previous: "space"`), then the algorithm.
- Remaining diagnostics: maths-only missing lines; extra digits from transcription/tags (category a).

### Page 21 - done ([v2], reviewed)
- Algorithm 5: `algorithm-5` (figure crop) + transcription (20 lines).
- Equations (12), (13), (14) as `$$ \tag{} $$` text. (13) keeps the printed subscript `p_{\text{data}(x_0)}` (TeX = PDF).
- Heading `### A.2 Inference` (was `# **A.2 Inference**`). Printed order kept (float at top between paragraphs).
- Remaining diagnostics: maths-only (category a).

### Page 22 - done ([v2], reviewed)
- Equations (15), (16) as `$$ \tag{} $$` text; the n-turn dialogue tuples (B.1) as inline LaTeX, checked at 260 dpi.
- Headings `### A.3 Algorithms`, `## B Experiments`, `### B.1 Data Collection and Preprocessing`.
- Repairs: `fixedlength` -> `fixed-length` (real compound hyphen), `au-toregressively` -> `autoregressively`.
- Remaining diagnostics: maths-only missing lines; number check only `−1` vs `-1` in $p_0^{n-1}$ (category a).
- Page ends with a complete paragraph (p. 23 starts B.2): no join needed.

### Page 10 - done ([v2], reviewed)
- `join_previous: "space"` on the first item (continues p. 9 "such as protein | generation [76, 77]").
- Headings `## 5 Conclusion and Discussion`, `## Acknowledgements`, `## References`. `$10^{23}$`. `[31, 78–87]` repaired.
- References [1]-[5]: one item per entry, `*italic*` venues, compared with main.bbl.
- Remaining diagnostics: number check only `10^{23}` vs `1023` (category a). 46/46 lines found.

### Page 11 - done ([v2], reviewed): references [6]-[23]; check OK (48/48). URL of [11] rejoined; [15] quotes kept as printed.

### Page 12 - done ([v2], reviewed): references [24]-[37]; check OK (52/52). [24] `multihead` -> `multi-head` (real hyphen at wrap).

### Page 13 - done ([v2], reviewed): references [38]-[55]; check OK (49/49). [43] `simplexbased` -> `simplex-based`.

### Page 14 - done ([v2], reviewed): references [56]-[73]; check OK (46/46). [64] `continuoustime` -> `continuous-time`.

### Page 15 - done ([v2], reviewed): references [74]-[90]; check OK (47/47). [89] `Dallatorre` -> `Dalla-torre`.

### Page 16 - done ([v2], reviewed): references [91]-[108]; check OK (50/50). URLs of [93], [94], [99] rejoined; '31th' (sic) kept.

### Page 17 - done ([v2], reviewed): references [109]-[124]; check OK (48/48). [111] `bigbench` -> `big-bench`.

### Page 18 - done ([v2], reviewed): reference [125]; URL rejoined; check OK (6/6).

## Summary

| Page | State | Check | Content |
|---|---|---|---|
| 10 | [v2] reviewed | ATTENTION (a) | end of Sec. 4, `## 5 Conclusion and Discussion` (Limitations), `## Acknowledgements`, `## References` [1]-[5] |
| 11-18 | [v2] reviewed | OK | references [6]-[125] (one text item per entry; 125 entries, numbered 1-125 in order, verified) |
| 19 | [v2] reviewed | ATTENTION (a) | Algorithms 1-3, `## A Formulation of Masked Diffusion Models`, `### A.1 Training`, Eq. (7)-(8) |
| 20 | [v2] reviewed | ATTENTION (a) | Algorithm 4, Eq. (9)-(11) |
| 21 | [v2] reviewed | ATTENTION (a) | Algorithm 5, Eq. (12)-(14), `### A.2 Inference` |
| 22 | [v2] reviewed | ATTENTION (a) | Eq. (15)-(16), `### A.3 Algorithms`, `## B Experiments`, `### B.1 Data Collection and Preprocessing` |

All remaining diagnostics are category (a) (LaTeX vs PDF glyphs, transcription digits of the algorithm crops, equation tags,
`10^{23}`, `n−1` minus glyph). Adjudication notes written for pages 10, 19, 20, 21, 22.

### Assets
- `algorithm-1` (p. 19, [106,70,506,196]), `algorithm-2` (p. 19, [106,203,506,330]), `algorithm-3` (p. 19, [106,337,506,462]),
  `algorithm-4` (p. 20, [106,70,506,260]), `algorithm-5` (p. 21, [106,70,507,331]); each crop includes the caption line and both
  rules (rule positions measured from 220-dpi renders). Each is followed by a transcription text item in the convention-4 form.
- No formula images kept: the extractor's 10 formula items (`formula-p0019-029`, `-031`, `formula-p0020-004`, `-006`, `-009`,
  `formula-p0021-003`, `-005`, `-009`, `formula-p0022-001`, `-004`) are now `$$ ... \tag{n} $$` text items, equations (7)-(16).

### Joins
- p. 10 first item `join_previous: "space"` (p. 9 ends "such as protein"; p. 9's last item p0009-b011 is text).
- p. 20 first item `join_previous: "space"` (continues "At $t = 1$, all" from p. 19).
- p. 22 -> p. 23: none needed (p. 22 ends a complete paragraph; p. 23 starts with the Table 5 float).

### Reading-order decisions (within page; no cross-page moves needed)
- p. 19: heading `## A Formulation of Masked Diffusion Models` placed before Algorithms 1-3 (printed after them, at mid-page), so
  the algorithms fall under Appendix A instead of under `## References`. The coordinator may prefer the printed order; then
  Algorithms 1-3 would sit at the end of the References section in navigation.
- p. 20: Algorithm 4 moved after the paragraph that continues the p. 19 sentence (printed at the top of the page).

### TeX versus PDF
- No disagreements found in pages 10-22. Printed oddities kept as in both sources: Alg. 2 comment "the SFT dat", `t * L`,
  Alg. 3 reuses `i` as loop and sum index, "Set $r_1$ is a fully masked sequence", Eq. (13) subscript `p_{\text{data}(x_0)}`,
  "analogous to but distinct from, the noise schedule", "predict all masked tokens", "Despite masking exactly $l$ tokens is
  different", "Nie et al. [27] introduces"; references "31th" ([101], [102]), `Llms trained on" a is b" fail to learn" b is a"` ([15]).
- main.bbl matches the printed bibliography except bbl formatting (natexlab a/b year suffixes are not printed; accents).

### Text repairs of substance
- Real compound hyphens restored at line wraps (extractor had dropped them): `multi-head` [24], `simplex-based` [43],
  `continuous-time` [64], `Dalla-torre` [89], `big-bench` [111], `fixed-length` (p. 22).
- URLs broken at line wraps rejoined: [11], [93], [94], [99], [125].
- `[31, 78– 87]` -> `[31, 78–87]` (p. 10); glued "deterministically l/L.While a theoretical..." (p. 21) repaired.
- Paragraph split restored on p. 19 (MDMs [16–20] ... / These models introduce ...).

### Conventions applied / brief notes
- Algorithm comments: the LLaDA assignment's example shows line 2 of Algorithm 1 with its comment as inline code although the
  comment contains maths (`x0`, `U[1, 4096]`); I followed the stated rule instead (inline code only for maths-free comments,
  otherwise plain text after `#` with LaTeX: `# with a probability of 1%, the sequence length of $x_0$ follows $\text{U}[1, 4096]$`).
  Maths-free comments as inline code: Alg. 2 line 2, Alg. 4 line 4.
- `|EOS|` on p. 22 kept as printed plain text (TeX `$|\text{EOS}|$`); other reviewers of Appendix B may want the same form.
- Italics in references written `*...*` (sibling-collection style).
- Instruction cost: none of the brief's instructions were wrong; the `formula` -> text conversion and per-page check loop were
  straightforward. The bbl cross-check (script `_scratch/r2/refs.py`) made the reference pages fast and caught all 6 dropped
  compound hyphens, which the letter-only line check cannot see.

### Limitations
- Reference punctuation/italics were compared visually on every page preview and programmatically against main.bbl; the
  verifier's letter/digit check cannot confirm punctuation.
