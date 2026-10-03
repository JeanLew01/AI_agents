# Independent verifier report: DIAL-MPC (arXiv:2409.15610v1), pages 1-9

- Package (`PKG`): `/home/jixia/AI_agents/paper2agent/NMPC/staging/dial-mpc-paper-s1`
- Reference (`DOC`): `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/dial-mpc-paper/documents/s001-dial-mpc/source.pdf`
- Scratch (crops, scripts, cached text lines): `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/_scratch/verify-dial/`
- Status: COMPLETE. Nothing in the package or in the review plans was changed.
- The reviewers' report and the adjudication notes were not read.

**Result: 0 errors, 9 minor findings.** No wrong symbol, sign, number, table cell, reference or omitted
passage was found. All minors concern placement of floats/footnotes, lost typography, index wording and
one low-resolution figure crop.

## Coverage (what was actually done)

All nine pages were checked in full; nothing in the text was sampled.

| Check | Method | Extent |
| --- | --- | --- |
| Prose | Native PDF text lines of every page read next to `paper.md`; in addition a mechanical word-level and a punctuation-level diff of the whole PDF text against `paper.md` (scripts `worddiff.py`, `punct.py`) | pages 1-9, complete |
| Display equations | Crops at 220-300 dpi compared symbol by symbol | optimal control problem, (1), (2), (3a)-(3f), (4), (5), (6), (7), (8), (9), (10): all |
| Inline mathematics | Every inline formula of `paper.md` compared with the page crops / native text | pages 2-5, 8, 9 (the only pages with inline maths) |
| Proposition and proof | Statement, numbering, six proof steps, explanatory paragraph, QED mark | complete |
| Algorithm 1 | 280 dpi crop versus `algorithm-1.jpg` and versus the transcription, line by line | 11 lines |
| Tables I-VI | Every CSV cell against a 280-300 dpi crop and against the PDF's native cell text (`tabs.py`); CSV versus the Markdown table in `paper.md` | all cells of all six tables |
| Numbers in prose | Covered by the word-level diff (numbers are tokens) plus reading | complete |
| Figures | All ten JPEGs opened; Figs. 1, 2, 3, 4, 6, 8 compared with high-resolution PDF crops, Figs. 5, 7, 9 (photographs/renders) with the page render | complete; text inside figures is not transcribed in the package, so only crop completeness and legibility were checked |
| Captions | Covered by the diffs and by reading | Figs. 1-9, Tables I-VI, Algorithm 1 |
| References | All 46 entries compared character by character after normalising only line-break hyphens, the spaces printed inside arXiv identifiers and Markdown italics (`refs.py`); entries [32]-[36] also inspected on a crop | complete (not a one-in-three sample) |
| Structure | Heading list against the PDF, duplicate-paragraph and repeated-shingle search, LaTeX delimiter/brace balance, extraction-damage patterns, asset links | complete |
| `SKILL.md`, `index.md`, `supplement.md`, conversion notes | Read once; index headings checked for exact existence in `paper.md` | complete |

Not checked exhaustively: italic/bold typography of running text (spot observations only, see findings 5-7).

## Findings

| # | severity | PDF page | item id | package says | PDF shows | suggested fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | minor | 6-7 | `p0007-b000`, `p0007-b001` (also `p0006-b006`, `p0006-b009`) | Table III (link, Markdown table, caption) sits under `## V. CONCLUSION`, after the conclusion paragraph (`paper.md` lines 273-283). Fig. 7 sits under `### B. Test-Time Generalizability` (lines 259-261). `index.md` nevertheless lists "Table III, Fig. 7" under `C. Robustness to Model Mismatch`; that section of `paper.md` contains neither. | Table III floats at the top of page 7, Fig. 7 on page 6 above the IV-C heading; both are cited only in IV-C. | Move the Table III block (and Fig. 7) to follow the paragraph of IV-C that cites it, so that a bounded read of IV-C returns the numbers; or correct the index row. |
| 2 | minor | 3, 6, 8 | `p0003-b013/b014`, `p0006-b000/b003`, `p0008-b007/b008`, `p0008-b016/b017` | Same kind of mismatch between index and position: Fig. 2 is under III-A (line 119) but the index lists "Figs. 2-4" under III-B; Fig. 6 is under IV-A (line 234) but the index lists it under IV-B; Table IV (line 395) and Fig. 8 (line 412) are under Appendix A but the index lists "Tables IV-VI ... Figs. 8-9" under Appendix B. | Float positions as printed; Fig. 2 is cited in III-A, Fig. 6 in IV-B, Table IV and Fig. 8 in Appendix B. | Either move Fig. 6, Table IV and Fig. 8 into the citing subsection, or change the index rows to the real location (Fig. 2 belongs to the III-A row in any case). |
| 3 | minor | 1, 3, 5 | `p0003-b012`, `p0005-b009`, `p0001-b007`, `p0001-b008` | Footnote texts are separated from their markers: footnote 1 marker is in III-A (line 117), its text is in III-B after the paragraph "This trade-off becomes more pronounced..." (line 137); footnote 2 marker is in the IV introduction (line 207), its text is in IV-A after the Fig. 5 caption (line 230); the author footnotes follow the fourth introduction paragraph (lines 21-23). Wording of all footnotes is correct. | Footnotes at the foot of the column in which the marker occurs. | Place each footnote directly after the paragraph that carries its marker (the author footnotes after the author line). |
| 4 | minor | 5, 6, 7 | `p0005-b011`, `p0006-b002`, `p0007-b000` | Tables I-III are plain text in CSV and Markdown. | The DIAL-MPC row is printed in bold in Tables I, II and III (proposed method, best values). In Table III a horizontal rule separates the four simulation rows from "DIAL-MPC in real". | Optional: bold the row in the Markdown tables, or add one sentence to the conversion notes (bold row; the last row of Table III is the real-world result, separated by a rule). All values are correct. |
| 5 | minor | 1 | `p0001-b012` | "Diffusion-Inspired Annealing for Legged Model Predictive Control (DIAL-MPC)" without marking. | The letters D, I, A, L, M, P, C are underlined to show how the acronym is formed. | Cosmetic; optionally mention in the conversion notes. |
| 6 | minor | 3 | `p0003-b003`, `p0003-b005` | `**Proposition 1 (Adopted from [43]):**` and `**Proof:**` in bold. | Both labels are printed in italics. | Cosmetic; use `*...*` if the printed style is to be kept. Numbering and text are correct. |
| 7 | minor | 3 | `p0003-fig3` | `assets/figure/figure-3.jpg` is 212 x 222 px (about 180 dpi of an 85 pt wide figure); the legend entry "p_0 ∝ exp(−J/λ)" is small though still readable. Complete, no caption inside. | Vector figure. | Re-crop at 300 dpi or more. (All other figure JPEGs are about 623 px wide and legible.) |
| 8 | minor | - | `index.md` | No row for `III. METHOD` (which has its own roadmap paragraph) or `APPENDIX`, and none for the three subsections of II, although `IV. EXPERIMENT` has a parent row. The assets list names `assets/supp_figs/` and `assets/supp_table/`, which do not exist in this package. The supplement row "Document beginning" is not a heading of `supplement.md`. | - | Add a `III. METHOD` row (and, if wanted, II-A/B/C); drop or qualify the two non-existent asset directories. All thirteen headings that the index does list exist exactly once in `paper.md`. |
| 9 | minor | - | conversion notes | "Subsection letters A, B, C repeat in Sections II, III, IV and the Appendix"; "cross-references are printed in lower case ('fig. 2', 'section III-A', 'table I')". | The Appendix has only A and B. The PDF mixes styles: it also prints "Figure 3", "Figure 5", "Figure 6", "Figure 7", "Figure 8", "Table II", "Table III", "Table V", "Table VI", "Appendix B" (all reproduced correctly in `paper.md`). | Reword: "A, B(, C)" and "some cross-references are printed in lower case". |

Notes that are not findings:

- `SKILL.md` carries the line "Draft: source review or verification remains unresolved." It was ignored as instructed;
  from this verification there is no reason to keep it.
- Two statements in the conversion notes cannot be verified from the PDF: "later published at ICRA 2025" and
  "after removing reader highlights (text unchanged)". Nothing contradicts them (no highlight is visible on any page;
  the PDF modification date is 2026-09-28).
- The other conversion notes are true: the four authors' typos 'horizion' (Fig. 1 caption), 'convolusion' and 'kernal'
  (proof), 'Quadraped' (Appendix A) are printed that way; Algorithm 1 prints `for i = 1 to N` while (4), (5) and the
  text ("Sampling proceeds in reverse order", ∀ i ∈ {N, ..., 1}) run from N down to 1; Table IV has merged parent headers.
- Further printed oddities kept faithfully: "DIAL-MPC ’s" with a space (IV-C), "optimality(i.e., convergence)" without a
  space, "10kg" in the Fig. 6 caption, "±(0.65, 0.65, 0.0)m", "model-base RL", "Mujoco MPC", footnote 2 ending "in A.",
  references [8], [11], [21], [22], [23], [29] ending after the title with no venue.
- CSV files use CRLF line endings and UTF-8 arrows (↓, ↑); no caption rows, no blank rows.

## Checked and found correct (by page)

- **p.1**: title; author line with the two asterisks; abstract (13.4 times, 50%, italics on "without any training" and
  "training-free"); I. INTRODUCTION paragraphs 1-4 including the sentence that crosses the columns under Fig. 1
  ("...suboptimal performance. Specifically, a large sampling range..."); Fig. 1 caption with $u_H$; both footnotes
  (equal contribution; affiliation, e-mail list, website); `figure-1.jpg` complete (four task labels, both annealing
  panels, $u_{2H-1}$).
- **p.2**: continuation "online method, ..."; three contribution bullets ("50 Hz"); II. RELATED WORK and A, B, C with
  every citation group ([1, 6, 19, 20], [2, 3, 5, 14], [11, 13, 21–24], [25, 26], [27, 28], [29], [30], [31, 32], [33],
  [15], [16–18], [34–36], [37], [38], [39]-[42]); III. METHOD roadmap; III-A; optimal control problem (sum from h=0 to H,
  terminal cost at $x_{t+H+1}$, dynamics constraint ∀ h ∈ {0, ..., H}, set constraints, unnumbered as printed);
  MPPI description ($N_W$, $[W]_i \sim \mathcal{N}(0, \Sigma_{t:t+H})$, $[W]_{1:N_W}$, $U = u_{t:t+H}$).
- **p.3**: (1) including the minus sign in both exponents, the index i in the numerator and j in the denominator and
  the trailing comma; $p_0(U) \propto \exp(-J(U)/\lambda)$, λ → 0, $U^*$; $p_1(\cdot) \propto (p_0 \ast \phi)(\cdot)$;
  Proposition 1 "(Adopted from [43])"; (2); proof: (3a) two equalities, (3b) with the sign change and
  $\phi(U)\Sigma^{-1}U$, (3c) $-\Sigma^{-1}$ and both integrals with $U-W$, (3d) expectations under $W \sim \phi(\cdot)$,
  (3e) positive sign and $U+W$, (3f) "≈" and Monte Carlo sums, final period; the explanatory paragraph referring to
  (3a)-(3f); QED mark; "fixed" in italics; footnote marker 1 and footnote text; Fig. 2 caption and crop (three panels,
  axis ticks); III-B first two paragraphs ($p_1$ to $p_4$, $p_i$, $p_3$ and $p_4$, bold "advantage"/"disadvantage");
  "Coverage and convergence trade-off" paragraph wrapped around Fig. 3 (four occurrences of det Σ); Fig. 3 caption
  and crop.
- **p.4**: end of the III-B paragraph; "Fortunately, ..." paragraph; Fig. 4 caption and crop (three panels and the
  complete two-row legend); "Annealing in diffusion process" ($p_1(\cdot), \ldots, p_{N-1}(\cdot), p_N(\cdot)$,
  $\phi_i(\cdot) \sim \mathcal{N}(0, \Sigma^i)$, $\Sigma^N$); (4) with βN in the denominator, factor d, ∀ i ∈ {N, ..., 1};
  III-C introduction, read continuously across the columns; Algorithm 1 image and transcription (11 lines, bold
  keywords, $\Sigma^i_{t:t+H}$, $u^{(i)}_{t:t+H}$, `shift`, references to (7), (3), (2)); dual-loop paragraph (all
  kernel lists including the printed missing commas "$\Sigma^N_H \dots, \Sigma^1_H$", "$NH$ updates", $u_{1:H+1}$);
  (5) with $\beta_1 N$, $H d_u$; (6) with $\beta_2 H$, $d_u$, ∀ h ∈ {0, ..., H}.
- **p.5**: end of the action-level paragraph; (7) with both fractions and the factor I; IV. EXPERIMENT introduction
  (3.9 times); task list with footnote marker 2 (10 cm, 60 cm, Appendix B); IV-A (kernel sizes 0.2 and 0.05,
  $N_W = 2048$, $H = 20$ (0.4 s), 500 million steps, 31 minutes, two additional reward terms, six reward terms);
  Table I all 18 cells (16 values and the two dashes of the NMPC row), column arrows, "GCRL*"; Table I caption (10 trials, 0.125 to 0.6 m,
  asterisk note); Fig. 5 caption (19, 30 kg, 15 kg) and crop (three rows); footnote 2; "Convergence of DIAL-MPC"
  (13.4 times, 107.7%, 3 times).
- **p.6**: Fig. 6 caption ("10kg") and crop (both axes, full legend); remaining IV-A text; IV-B (3.9 times, 3.5%,
  10 kg payload, "outperform GCRL with a larger margin"); Table II four values; Table II caption; Fig. 7 caption (7 kg)
  and crop; IV-C (2 kg, 92%, 126%); V. CONCLUSION first part.
- **p.7**: Table III ten values and caption; rest of the conclusion read continuously across the page break;
  references [1]-[38].
- **p.8**: references [39]-[46] (including [41] as printed with the URL); APPENDIX and A heading; "Quadraped
  Configurations" (18 DoF, 12 actuated joints, 24 N·m, 45 N·m, gains 30 and 0.65); (8) with the hat on τ and the comma;
  $d = 0.65$; "Algorithm Implementation:" (JAX [46], Brax [40], RTX 4090, i9-13900KF, 32 GB, 50 Hz, 200 Hz, 2048,
  20-step, 0.4 s), read continuously across the columns; Table IV all 40 cells (signs, dashes, 3.0, 10.0, 0.001) and
  caption; Fig. 8 caption (1 s) and crop (legend complete); B heading; "Quadruped Velocity Tracking" (1 kg, 20%,
  0.6 and 1.0, ±(1.5, 0.5, 0.0) m/s, ±1.5 rad/s, 500 million steps, 31 minutes).
- **p.9**: "Quadruped Sequential Jumping", read continuously across the page break (10 cm, 1 s, ±(0.65, 0.65, 0.0)m,
  0.5 rad); (9) with the superscripts (j) and (j−1) and the bracketed difference; its explanation; (10) with
  $j_{\text{max}}$, the half-open interval $[T_{\text{min}}(j), T_{\text{max}}(j))$ and the minimum; "10 jumping stages
  in 8 s"; 5 trials, $\bar{R}_{\text{con}}$, 10 kg; "Quadruped Crate Climbing" (1/15, 0.6 m, [9], 20 hours; 4096 samples,
  40-step (1 s) horizon, 4 annealing steps, 30 seconds, 2-second), read continuously across the columns; Table V five
  values; Table VI seven values; both captions; Fig. 9 caption and crop; "Humanoid Crate Pushing" (Unitree H1,
  0.8 m/s, 30 kg and 15 kg, seven reward weights, 25 and 18 degrees of freedom).
- **Whole document**: headings and levels equal the printed ones (I-V, REFERENCES, APPENDIX; A-C under II, III, IV;
  A-B under APPENDIX), none invented or missing; no duplicated paragraph; all 34 line-break hyphens of real compounds
  kept (for example "real-world", "dual-loop", "III-B", "Human-to-Humanoid") and all other line-break hyphens removed;
  no `<sup>`, glyph soup, split decimals or stray markup; `$` delimiters, braces and `\left`/`\right` balanced; tags
  (1), (2), (3a)-(3f), (4)-(10) present once each; all 16 asset links resolve.

## One technical question answered from the package only

**Question.** Which covariance does DIAL-MPC use for the perturbation of the control at horizon index h in annealing
iteration i, where is the noise largest and smallest, and which solver settings were used for the real-time tasks and
for crate climbing?

**Answer from the package** (`paper.md`, "C. Diffusion-Inspired Annealing for Sampling-Based MPC", equations (5)-(7);
"A. Convergence and Coverage"; APPENDIX "A. Hardware and Software Setup" and "B. Task Implementation Details",
paragraph "Quadruped Crate Climbing"):

- The kernel is isotropic, $\Sigma^i_{t+h} = \exp\left(-\frac{N-i}{\beta_1 N} - \frac{H-h}{\beta_2 H}\right) I$ (7).
  It realises the trajectory-level schedule $\det(\Sigma^i_{t:t+H}) \propto \exp(-\frac{N-i}{\beta_1 N} H d_u)$ (5) and
  the action-level schedule $\det(\Sigma^i_{t+h}) \propto \exp(-\frac{H-h}{\beta_2 H} d_u)$ (6).
- The noise is largest for i = N and h = H (the kernel equals I: first annealing stage, last control of the horizon)
  and smallest for i = 1 and h = 0, where it equals $\exp(-\frac{N-1}{\beta_1 N} - \frac{1}{\beta_2}) I$. Controls far
  in the horizon get more noise because they have been updated fewer times. The text anneals from i = N down to 1,
  whereas Algorithm 1 prints `for i = 1 to N` (stated in the conversion notes).
- Real-time tasks: $N_W = 2048$ samples, H = 20 steps (0.4 s), control at 50 Hz with a 200 Hz low-level loop.
  Crate climbing (not real time): 4096 samples, 40-step (1 s) horizon, 4 annealing steps, all contacts on base and
  thighs enabled, 30 seconds to produce a 2-second plan.
- The paper gives no numerical values for $\beta_1$, $\beta_2$, and no value of N for the real-time tasks.

**Check against the PDF.** Equation (7): crop of page 5, left column, identical. Equations (5), (6): crop of page 4,
right column, identical. "NW = 2048 ... H = 20 (0.4 s)": page 5, IV-A. "50 Hz", "200 Hz", "2048 parallel environments
and a 20-step horizon (0.4 s)": page 8, Appendix A. "4096 parallel samples, 40-step (1 s) horizon, and 4 annealing
steps", "30 seconds", "2-second": page 9. The PDF text contains no numerical value for β, β1 or β2 and no N for the
real-time tasks. The answer is correct and complete with respect to the PDF.
