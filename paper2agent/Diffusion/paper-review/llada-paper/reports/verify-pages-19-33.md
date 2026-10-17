# Independent verification: LLaDA paper skill, PDF pages 19-33

- PKG: `/home/jixia/AI_agents/paper2agent/Diffusion/staging/llada-paper`
- DOC: `/home/jixia/AI_agents/paper2agent/Diffusion/paper-review/llada-paper/documents/s001-llada`
- Verifier: independent (v2), 2026-10-14. Status: COMPLETE.
- Scratch: `/home/jixia/AI_agents/paper2agent/Diffusion/paper-review/_scratch/v2` (crops, text-layer dump `lines_19_33.txt`, diff scripts `wdiff.py`, `pdiff.py`)

Result: **1 error, 6 minors**. The text, mathematics, algorithms and table numbers in pp. 19-33 are faithful to the PDF. The findings are about structure and formatting: a lost case boundary in Table 16, flattened line breaks, and two inaccurate sentences in the conversion notes.

## Coverage (what I actually did)

- **Text, all pages 19-33.** I dumped the native PDF text layer for pp. 19-33 and compared it with `paper.md` lines 566-1157 in three ways:
  1. A global word diff.
  2. A per-paragraph best-match diff that is not affected by moved floats.
  3. An exact, punctuation-sensitive check of every non-math fragment of 12 or more characters against the de-hyphenated PDF text.

  I also ran the reverse check: every PDF line (minus math tokens) must occur in the package or the CSVs. Prose differences are limited to inline maths, line-end hyphenation and the moved floats. **No word or number differs.** I also read every page preview (19-33) next to the package.
- **Mathematics.** I compared equations (7)-(16) symbol by symbol against 220-dpi crops (pp. 19-22). I checked all inline maths in A.1-A.2, B.1 (the n-turn split), B.2 (4×10⁻⁴, 4.2×10⁻⁴, 6ND, N, D) and B.3 ({0.5, 1, 1.5, 2}). By script, `$`/`$$` are balanced and braces and `\left`/`\right` match in lines 566-1157. There is no `<sup>`, glyph soup or ligature damage.
- **Algorithms 1-5.** I compared every transcription line by line with the linked JPEG, with my own 260-dpi crop of p. 19 (Alg. 1) and with the PDF text layer (Alg. 5). I checked:
  - indices and nesting/indentation;
  - `U(0,1]` and `U[1,4096]`;
  - `1/(t*L)` and `1/(t*L')`;
  - `L/l` and the reused index `i` in Alg. 3;
  - `for t ← 1 down to 1/N step 1/N`, `s = t − 1/N` and the `s/t` remask probability;
  - greedy argmax and `c^i = p_θ(r_0^i|p_0,r_t)_{r_0^i}`;
  - `n_un = ⌊L(1−s)⌋`, `Lowest − n_un({c^i}_1^L)` and both comments.
- **Tables.**
  - Tables 5-12: every cell of each CSV against the PDF text layer, row by row, plus a visual check of the page images.
  - Tables 18-19: every cell (CSV and inline Markdown) compared by script with the text layer (0 mismatching rows out of 20 + 21), plus a visual check of 200-dpi crops.
  - Inline Markdown tables equal their CSVs for Tables 5-12 and 15-17 (script).
  - Tables 15-17: every text cell against the text layer, plus page renders at 150 dpi.
  - All 17 captions in the range match the PDF exactly (string compare).
- **Chinese text.** I checked character by character against 300-dpi crops:
  - B.9 Examples 1-2 (窈窕淑女…/君子好逑。/不拘一格降人才…/我劝天公重抖擞。);
  - Table 17 Q1/Q2 (User, GPT-4o and LLaDA turns, including the printed slips 山居秋膜 and 无亲 and the unclosed （武陵春);
  - the Table 15 translation 现在被证明的曾经只是想象.
- **Images.** I opened all 9 linked JPEGs of the range (algorithm-1…5, figure-4, figure-5, table-13, table-14). All are complete (rules, axes, legends, panel labels), contain no caption or body text and are legible. The Table 13/14 token transcriptions were compared token by token with the images, and both match.
- **Structure.** All 16 printed headings in the range (A, A.1-A.3, B, B.1-B.10, C) are present with the right text and level. Float placement matches the conversion notes. No float interrupts a sentence: the B.4 "Experimental Setup" paragraph that crosses pp. 24-25 around Tables 9-10 reads continuously. All asset links in lines 566-1157 resolve.
- **SKILL.md, index.md and conversion notes.** I read each once. Every index heading exists exactly in `paper.md`; "Document beginning" refers to `supplement.md` by design. I checked the notes' claims against the PDF; see findings 2-3.
- **References** are not in my range (pp. 10-18 belong to the other verifier).

## Findings

| # | severity | PDF page | item id | package says | PDF shows | suggested fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | error | 32 | p0032-b001 (Table 16) | `table-16.csv` and the inline table give all 12 rows of the first two cases the label `Daily life`. Because Table 16 is *multi-turn*, a new User turn does not mark a new case. The interview dialogue (2 rounds) and the programming dialogue (4 rounds) therefore read as one 6-round dialogue. The conversion notes say same-label cases are "separated only by a new User turn", which does not hold for this table. | Three separate dialogues, each with its own italic label and a horizontal rule: *Daily life* (job interview, 2 rounds), *Daily life* (learning programming, 4 rounds), *Math* (2 rounds). | Make the cases distinguishable, for example `Daily life (1)` / `Daily life (2)` or a `Case no.` column. Do the same in Tables 15 and 17 for consistency, and correct the note. |
| 2 | minor | 29 | p0029-b000 / conversion notes | Notes, float bullet: "Tables 13-17 (case studies, printed after Appendix C)". | Table 13 is printed at the top of p. 29, **before** B.9, B.10 and Appendix C. Only Tables 14-17 (pp. 30-32) come after Appendix C. The notes' own page summary ("Tables 14-19 pp. 30-33") is consistent with the PDF. | Change to "Table 13 (top of p. 29) and Tables 14-17 (after Appendix C)". |
| 3 | minor | 19-21 | conversion notes | "Algorithms 1-5 (printed on pp. 19-21, inside Appendix A.1-A.2)". | Algorithms 1-3 sit at the top of p. 19, **above** the "A Formulation of Masked Diffusion Models" heading. Algorithms 4 and 5 are at the tops of pp. 20 and 21, inside A.1's text. None is inside A.2. | Change to "printed on pp. 19-21 (Algorithms 1-3 before the Appendix A heading, 4-5 within A.1)". |
| 4 | minor | 31 | p0031-b001 (Table 15) | In the movie-recommendation LLaDA turn, the printed line breaks before "1.", "2.", "3." and "All of these films…" are flattened into one line, in both the CSV and the Markdown. The Code turn of the same table keeps its line breaks (`\n` / `<br>`), so the treatment is inconsistent. The printed literal `**The Shawshank Redemption**` (etc.) will also render as bold inside the Markdown table, which hides the literal asterisks that the model output contains. | Four line breaks inside the response, and literal `**…**` asterisks in the model output. | Use `\n` in the CSV and `<br>` in the Markdown before each numbered item and before "All of these…". Optionally escape the asterisks (`\*\*`) in the Markdown cell. |
| 5 | minor | 28, 29 | p0028-b006 (iGSM Solution), p0029-b004, p0029-b004b (B.9 examples) | The printed line structure is held only by single newlines inside one Markdown paragraph (`paper.md` lines 1037-1040, 1061-1063, 1065-1067). A renderer joins the four solution lines, and "Example 1: Prompt: … Answer: …", into single lines. | Separate lines: Define … x = 1. / Define … m = x = 1. / Define … = 2; / so n = …, and Example / Prompt / Answer on separate lines. | Add `<br>` or two trailing spaces, or put each line in its own paragraph. |
| 6 | minor | 19, 20 | p0019-b009 (Alg. 2 line 2), p0020-b001 (Alg. 4 line 4) | These two comments are wrapped in backticks (inline code). All other algorithm comments are plain text after `&emsp;`. | Same typeface for every `#` comment. | Remove the backticks so all comments are formatted alike. |
| 7 | minor | – | `references/index.md` (Assets) | Lists `assets/supp_figs/` and `assets/supp_table/`, which do not exist. Says tables live in `assets/table/` "(CSV, or JPEG …)", but the JPEG-only Tables 3, 13 and 14 are in `assets/figure/` (`table-3.jpg`, `table-13.jpg`, `table-14.jpg`). | – | Drop the two non-existent directories and say that the token-visualisation tables are JPEGs in `assets/figure/`. |

Observations I did not count:
- `paper.md` line 1033 writes `"#### \$answer"`. The backslash is a Markdown escape that renders as `$answer`, but it appears in the raw text.
- Algorithm 3 uses `\text{log\_likelihood}`. KaTeX renders this fine; MathJax without `textmacros` may show the backslash.
- Table 7 uses the ASCII `L'` in the converter-added column, where the PDF prints the prime `L′`.

## Checked and found correct (by page)

- **p. 19.**
  - Algorithms 1-3, line by line, including Require lines, comments and the truncated "the SFT dat".
  - Heading A, heading A.1 and the A.1 paragraphs.
  - Eq. (7) (product over i=1..L) and Eq. (8) (cases 1−t / t, conditions x_t^i = x_0^i / x_t^i = M).
- **p. 20.**
  - Algorithm 4: s = t − 1/N; argmax with the greedy comment; the if/else nesting; "with probability s/t, r_0^i is set to M"; r_s = r_0; Return r_0.
  - The A.1 continuation.
  - Eq. (9), and Eq. (10) with all four cases and conditions (1; s/t; (t−s)/t q_{0|t}; 0 otherwise).
  - Eq. (11) with x_t^UM and "∀i such that x_t^i = M".
  - The mask-predictor paragraph.
- **p. 21.**
  - Algorithm 5, all 20 lines.
  - Eq. (12) (≜, 1/t, indicator, sum to L).
  - Eq. (13), with the printed p_{data(x_0)} slip kept.
  - Heading A.2.
  - Eq. (14) (l ∼ {1,…,L}, L/l, x_l).
  - Variance paragraph: "over 1000" vs "128", l/L.
- **p. 22.**
  - AO-ARM paragraph; Eq. (15) (π ∼ U_π, x_0^{π(i)} | x_0^{π(<i)}; π); "π(≥ i)".
  - Eq. (16) (tilde p_θ, exponent 1+w over exponent w, m, r_t).
  - A.3 paragraph.
  - Headings B and B.1.
  - B.1: 11 % / 61 % / 28 %, BERT [22], 1 million + 3.5 million, [103] and [104], |EOS| paragraph, the n-turn split.
- **p. 23.**
  - Table 5: all 40 value cells, the headers and the caption.
  - Table 6: all 12 cells and the caption.
  - B.2: 1.5B, 8B, 7B, [6, 21], [105]-[107], AdamW [29], wd 0.1, WSD [28], 2000 iterations, 4×10⁻⁴ with batch 1280, 4.2×10⁻⁴ with batch 4224, 6ND [108, 109].
  - B.3: six benchmarks, scale set {0.5, 1, 1.5, 2}.
- **p. 24.**
  - Figure 4: image, panel labels and caption.
  - Table 7: all cells, with "Block Difusion" kept.
  - Table 8: all cells, with "Block Difusion LLaDA" kept.
  - B.4: Flexible Sampling Strategies paragraph, [31], and the start of Experimental Setup.
- **p. 25.**
  - Table 9 (header "Length" kept) and Table 10: all cells.
  - Rest of the B.4 setup: 1024; {64, 256, 512}; block length 32; |EOS| confidence set to zero for HumanEval, MBPP, GSM8K, Math, GPQA; 256 for the remasking ablation.
  - Results paragraphs; "77.5 to 78.6".
  - Heading B.5.
- **p. 26.**
  - Figure 5: four complete panels, and the caption (256; 32/64/128/256; 8/4/2/1).
  - B.5 text, with "just one tokens" kept.
  - B.6: benchmark lists with citations [110]-[124] and the protocol paragraphs.
- **p. 27.**
  - Table 11: all 30 cells, with the merged Input Length repeated.
  - B.6: lm-evaluation-harness [125], Yang et al. [25], 1 vs 128 Monte Carlo samples, answer lengths 3/64/256/512.
  - B.7: A100-80GB, batch 1, 256 tokens, 1.5× and 1.8×, prompt lengths 894/680/628/132, "compares of" kept.
- **p. 28.**
  - Table 12: all 6 cells.
  - End of B.7: "inherently depend on ARMs" as printed, [31, 79–87].
  - B.8: "#### $answer", the Question/Solution box (3 * 2 = 1 #### 1), the Prompt box (mod 5, '#### x.', ¨the / High.Ässume artefacts), 100 questions, steps 4-6.
- **p. 29.**
  - Table 13: caption, image and token transcription.
  - B.9 Chinese examples.
  - B.10 paragraph.
  - C Impact Statement: both paragraphs.
- **p. 30.** Table 14: caption, image and both User/LLaDA transcriptions (token by token).
- **p. 31.** Table 15: all turns, including ‘sorted()‘ and "The final result is 1500" (no period). Line breaks: see finding 4.
- **p. 32.**
  - Table 16: all turns' text; case boundary: see finding 1.
  - Table 17: all characters.
- **p. 33.**
  - Table 18: 20 rows × 9 columns, including "-" in GSM8K at 981.47B and 1975.52B, "28.5" and "33.9".
  - Table 19: 21 rows × 9 columns, with the "baelines" caption kept.
- **Conversion notes.** These claims are true: the slip list, float moves, Table 7 / 11 / 15-17 conventions, token-visualisation handling, Figure 4 panel line, and "3 * 2 = 1 is modulo 5". The two wrong statements are findings 2-3; the Table 16 statement is part of finding 1.

## Technical question answered from the package only

**Question.** How does LLaDA's low-confidence remasking sampler decide how many tokens stay unmasked after a step, and how is a position's confidence defined? How does this differ from the random-remasking sampler?

**Answer using only the package** (A.3, Algorithms 4 and 5, `paper.md` lines 704-782; A.1 Eq. (10), line 590):
- Both samplers start from a fully masked response r_1 of length L and loop t = 1 down to 1/N in steps of 1/N, with s = t − 1/N.
- **Random remasking (Algorithm 4).** It predicts all tokens greedily (argmax of p_θ(r_0|p_0, r_t)) and keeps already-unmasked tokens. Each newly predicted masked position is set back to M with probability s/t, which is the s/t case of Eq. (10).
- **Low-confidence remasking (Algorithm 5).** It sets c^i = 1 for already-unmasked positions. For masked positions it takes the argmax token and sets c^i = p_θ(r_0^i|p_0, r_t) evaluated at that token. It then computes n_un = ⌊L(1 − s)⌋, which line 12's comment calls "the number of unmasked tokens … in timestep s". Every position whose c^i is among Lowest − n_un({c^i}_1^L) is set to M; line 15's comment reads "the n_un positions with the least confidence are selected for remasking". Finally r_s = r_0.
- Read literally, the two comments are in tension: remasking the n_un lowest leaves L − n_un unmasked, not n_un. The package reproduces this exactly as printed.

**Check against the PDF** (p. 20, Algorithm 4 crop; p. 21, Algorithm 5 crop and text layer; p. 20, Eq. (10) crop): everything in the answer matches, including:
- the floor brackets, (1 − s), the subscript r_0^i on the confidence, and both comments verbatim;
- the s/t probability and the greedy-sampling comment in Algorithm 4;
- the s/t row of Eq. (10).

The tension between the two comments is in the paper itself; it was not introduced by the conversion.
