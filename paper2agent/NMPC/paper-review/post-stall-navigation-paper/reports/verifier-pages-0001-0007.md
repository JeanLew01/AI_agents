# Verifier report: post-stall-navigation-paper, pages 1-7

Status: COMPLETE (2026-10-02). Independent check; the reviewers' report was not read. Nothing in the package or the page plans was changed.

- PKG: /home/jixia/AI_agents/paper2agent/NMPC/staging/post-stall-navigation-paper-s1
- DOC: /home/jixia/AI_agents/paper2agent/NMPC/paper-review/post-stall-navigation-paper/documents/s001-post-stall-navigation
- Reference: `source.pdf` (arXiv:2201.01186v1, 7 pages, letter, IEEE two-column). The authors' TeX source was not used.
- Scratch (crops, native text lines, diff scripts): /home/jixia/AI_agents/paper2agent/NMPC/paper-review/_scratch/verify-poststall/

Result: **0 errors, 4 minor findings.** All four minors are in `index.md` / the conversion notes; none is in the transcribed paper text, mathematics, numbers, captions, figures or references.

## Coverage

All seven pages were checked in full; nothing was sampled.

| Check | What was done |
| --- | --- |
| Prose, pages 1-7 | Every page read as an image (130 dpi render) next to `paper.md`. In addition, the native PDF text lines of all pages (`p2s_tools.py lines`) were joined and compared with the package prose by a word-level diff, once with punctuation stripped and once with punctuation kept (scripts `diff.py`, `diff3.py`, `diff4.py` in scratch). Every remaining difference was inspected by eye: they are only (a) moved floats/captions/footnote, (b) inline maths written as LaTeX, (c) italic markers in the references, (d) the omitted arXiv margin stamp. |
| Line-break hyphens | All 44 line-end hyphens in the PDF text (43 before a lower-case continuation, plus LI-/DAR) listed and compared, and the three page ranges split at an en dash in the references (114–123, 969–1002, 235–250): compounds kept (fixed-wing, Slower-moving, LIDAR-based, real-time, perception-aware, post-stall, point-cloud, deep-stall, Perception-aware), plain wraps joined (LI-DAR -> LIDAR, au-tonomous, Bur-gard, ...). |
| Display equations (1)-(5) | Each compared symbol by symbol with crops at 260 dpi (`eq1-2.png`, `eq3.png`, `eq4-5.png`). Brace, `\left`/`\right`, `\begin`/`\end` balance and `\tag` numbers checked by script. |
| Inline maths | Every inline expression on pages 3, 4 and 6 compared with 260 dpi crops (`inline3.png`, `eq4-5.png`, `noise.png`); `$` parity checked per line. |
| Algorithm 1 | Image opened; transcription compared line by line with a 260 dpi crop (`alg1.png`), including block nesting. |
| Numbers | All numbers in prose are covered by the word diff (digits were kept in the comparison keys); the results paragraphs of IV-B, IV-C, V-B, V-C were also read against the page images. The paper has no tables and the package has no CSV. |
| Figures | All 11 JPEGs opened (Figures 1-10, Algorithm 1) and compared with PDF crops taken with a margin; edges of Figures 6, 7, 8, 10 examined at 300-900 dpi; build bounding boxes compared with the ink extent. All 11 caption texts covered by the word diff. All 11 links resolve. |
| References | All 30 entries compared (not every third): alphanumerics and punctuation by the strict diff, italic span and order by eye on the page image. |
| Structure | Heading list of `paper.md` compared with the printed headings and levels; reading order across columns and pages checked at all six page breaks and all column breaks; search for `<sup>`, `<sub>`, ligature glyphs, replacement characters. |
| SKILL.md, index.md, conversion notes | Read once; index headings matched against `paper.md` by script; each statement of the conversion notes checked. The "Draft" line in SKILL.md was ignored as instructed. |

## Findings

| # | Severity | PDF page | Item id | Package says | PDF shows | Suggested fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | minor | 5 | p0005-b005, p0005-b007 (Figures 3, 4) | `index.md`, row `V. HARDWARE EXPERIMENTS`: "Flight hardware, simulated-perception and control experiments, Figures 3-10". Row `IV. REAL-TIME SIMULATION STUDY` names no figures. | Figures 3 and 4 are simulation figures: cited only in IV-B ("Figure 3 shows the NanoMap search depth ..."), printed before the heading V, and placed in section IV in `paper.md` (together with Figure 2). Section V contains Figures 5-10. | Row V: "Figures 5-10". Row IV: add "Figures 2-4". |
| 2 | minor | 4-6 | p0004-b011, p0004-b015, p0004-b017, p0005-b010, p0005-b016, p0006-b005, p0006-b016 | `index.md` lists the subsections of III (A. Mapping, B. RRT Generation, C. Direct Trajectory Optimization) but none of the subsections of IV and V, and has no row for `VII. ACKNOWLEDGEMENT`. | Printed headings present in `paper.md` and absent from the index: `A. Simulation Setup`, `B. Experiment 1: Use of NanoMap History`, `C. Experiment 3: Noise`, `A. Experimental Set-up`, `B. Simulated Perception`, `C. Control Experiment`, `VII. ACKNOWLEDGEMENT`. All quantitative results of the paper are in IV-B, IV-C and V-C. | Add the seven rows (exact strings above), each with "Under IV. ..." / "Under V. ..." as for III. |
| 3 | minor | - | - | `index.md`, supplement table: exact heading "Document beginning"; asset list names `assets/supp_figs/`, `assets/table/`, `assets/supp_table/`. | `supplement.md` consists of the heading `# Supplementary information` and the sentence "No corresponding materials were supplied."; there is no heading "Document beginning". Only `assets/figure/` exists in the package; the paper has no tables and no supplement. | Replace the supplement row by a statement that no supplement exists, and list only `assets/figure/` (10 figures + `algorithm-1.jpg`). The same template wording is in the SKILL.md description ("its supplementary information, figures and tables"). |
| 4 | minor | 1 | conversion notes | "Source: arXiv:2201.01186v1 [cs.RO], 4 Jan 2022 (published at ICRA 2022, pp. 9696-9702)." | The PDF carries only the arXiv stamp "arXiv:2201.01186v1 [cs.RO] 4 Jan 2022". ICRA and the page range are printed nowhere in the document. A web search (IEEE Xplore document 9812099; a second search that did not contain the page numbers returned 9696-9702) is consistent with the claim, so it is not false, but it is not a property of the source PDF. | Mark it as external bibliographic information, e.g. "(external metadata, not printed in the PDF: ICRA 2022, pp. 9696-9702)". |

No finding of severity "error".

Remarks that are not findings (printed that way, and reproduced faithfully):
- Eq. (1): the initial-state bound is printed with `x_N` (`x_i - delta_i <= x_N <= x_i + delta_i`); the package keeps `x_N` and says so in the notes.
- Eq. (3) and (5): the exponent is printed as `(r+s)^{2^{n/2+k}}`; kept.
- Algorithm 1: `IS_FRONTIER_NODE()x_new, map)` and `xgoal.FIND_CLOSEST(f)` are printed slips; kept.
- Heading `C. Experiment 3: Noise` follows `B. Experiment 1` and the text calls it "the second set"; kept as printed.
- Prose slips kept as printed: "amendable", "(e.g.,[5])", "most of approaches", "we show in the importance", "a reduced the computational burden", "the summing a maximum", "For these data", "those of the author".
- Figure 7: the bottom tick label "30" is cut at its lower edge in the PDF itself (900 dpi crop `fig7-30.png`); the JPEG contains the whole embedded image. Figure 10 ends at x = 10 in the PDF as well.
- Algorithm 1 transcription does not reproduce the italic type of the conditions (`PATH_OBST_FREE(...)`, "to"); typography only, the linked image shows it.

## Checked and found correct (by page)

**Page 1.** Title; author line with four `$^{1}$` marks; footnote 1 (affiliation, the brace e-mail group, `@jhuapl.edu`) and the distribution statement; abstract complete ("42-inch", "[1]", "[2]"); heading `I. INTRODUCTION`; four introduction paragraphs, the third continuing across the column break below Figure 1 without a gap; heading `II. RELATED WORK`; Figure 1 JPEG complete (both stacked screenshots, no caption text inside); caption verbatim. The rotated arXiv stamp is omitted and declared in the notes.

**Page 2.** Related work continues from page 1 without break ("online mapping, as well as ..."); all citation groups ([7], [8], [5]; [9], [10], [11]; [4], [23], [24], [25], [26]; [12]-[22], [27], [1]) correct; `III. APPROACH` with two paragraphs ("four major stages", "42-inch wingspan"); `A. Mapping` three paragraphs ("K-nearest"); `B. RRT Generation` first paragraph, "Bézier" correct, continues on page 3.

**Page 3.** Rest of III-B; Algorithm 1 image complete and transcription identical line by line (header arguments, 16 lines, nesting of the three `if` blocks, final `Return`); two paragraphs after the algorithm; `C. Direct Trajectory Optimization`. Eq. (1): objective `sum_{k=0}^{N}[x_k^T Q x_k] + x_{N+1}^T Q_f x_{N+1}`, minimisation variables `x_k, u_k, h`, "for all k in [0,...,N] and", Simpson collocation with `h/6.0` and `4 xdot_{c,k}`, the two box constraints on `x_N`, state and input bounds, `c(x) >= 0`, `h_min <= h <= h_max`, tag (1). Eq. (2): four lines including `/2`, `h(...)/8`, final period, tag (2). Inline: `h_min = 0.001s`, `h_max = 0.2s`, `delta_f`, `delta_i`, `(x_f, x_i)`, `c(x) = d(x) - r`, `K = 10`, `d(x)_i = ||x - a_i||`, mean distance and its gradient (no final period, as printed), `d(x) >= r`, `p(x) <= s`. Eq. (3): six lines, limits `k=0..inf`, `j=1..n`, `j=0..k-1`, `Gamma(n/2+k+1)`, `(2 lambda_j)^{1/2}`, `d_{(k-j)}`, `(2 lambda_j)^{-k}`, `Sigma^{-1/2}(x - a_i)`, tag (3).

**Page 4.** "where n = 3 ..."; Eq. (4) with tag; Eq. (5): five lines, brackets, signs (`-1/2 k (2 lambda)^{-k}{}^T Sigma^{-1/2} b_i`), tag (5); "75 terms"; headings `IV. REAL-TIME SIMULATION STUDY`, `A. Simulation Setup`, `B. Experiment 1: Use of NanoMap History`, `C. Experiment 3: Noise`. Numbers: 100 trials; 30Hz; 128x85; 87x58 degrees; 20 meter; two 90 degree turns; 1.2 meters; history of 50 point clouds; 91 trials / 15.4% (Fig. 2a); 58 / 57.4% (Fig. 2c); 80 / 22.5% (Fig. 2b); `N(diag(0,0,0), diag(0.1,0.1,0.1))`; `N(0, 0.316)`; max probability 0.5; radius 1.2 meters; 99 / 17.2% (2d); 95 / 1% (2e); 100 / 1% (2f).

**Page 5.** Figure 2 JPEG: six panels with labels (a)-(f), axes and tick labels complete, no caption text; caption verbatim including the (a)-(f) descriptions. Figures 3 and 4 complete with axis labels; captions verbatim. `V. HARDWARE EXPERIMENTS`, `A. Experimental Set-up`: component names (EPP Edge 540 XL, Twisted Hobbys, mRobotics Control Zero F7, Ardupilot, uBlox ZED-F9P, MS5525, RFD900u, Intel NUC 10 i7, Realsense D455) correct; the paragraph that crosses the column break under Figure 5 reads continuously. Figure 5 JPEG complete with all seven labels legible; caption verbatim. `B. Simulated Perception` start.

**Page 6.** V-B continues across the page break ("... distance to obstacles | with standard deviation inflation with a 3 meter radius, a time horizon `T_H = 1s` and a replanning frequency of 5Hz"); `C. Control Experiment`: "factor of 10", "six hardware trials, four", Figures 7/8/9/10 cited; last paragraph crosses the column break correctly. Figures 6-10 JPEGs complete (axis titles, all tick labels, markers), no body or caption text inside (Figure 10 sits directly under the acknowledgement text: top edge checked, clean). Captions 6-10 verbatim. `VI. DISCUSSION` and `VII. ACKNOWLEDGEMENT` complete.

**Page 7.** `REFERENCES`: 30 entries, in order, all compared in full: authors, titles, venues, volume/number/pages/years; en dashes in page ranges and in "Range–robust"; "Blösch"; "AIAA Unmanned... Unlimited Conference"; "p. 025013"; "vol. 101, no. 24, 2020"; both arXiv numbers (2001.11478, 2012.12142). Italic spans agree with the print.

**SKILL.md / index.md / notes.** The ten main-paper headings named in the index exist verbatim in `paper.md` and each is unique as a full string. Notes checked: margin stamp omitted (true); printed peculiarities reproduced (true, see above); Algorithm 1 as image plus transcription (true); floats moved to paragraph boundaries and Figure 10 placed with the citing paragraph of V-C (true); footnote after the author line (true); no tables (true). The statement that the mathematics was taken from the arXiv TeX source is a process statement; the result agrees with the PDF.

## Technical question answered from the package only

**Question.** In the noise study, which noise was injected, which three collision constraints were compared, and how did they perform? How is the probability-of-collision constraint aggregated over the nearest neighbours?

**Answer from the package** (`paper.md`, sections `C. Experiment 3: Noise` and `C. Direct Trajectory Optimization`, Figure 2 caption):
- Noise: positional noise `N(diag(0,0,0), diag(0.1,0.1,0.1))` on the fixed-wing state and `N(0, 0.316)` on the depth images; a global path to the goal replaces the RRT planner so that only trajectory generation is affected. Each experiment has 100 trials.
- Constraints: (i) distance to obstacles, `c(x) = d(x) - r` with `d(x)` the mean distance to the `K = 10` nearest neighbours; (ii) the same with the collision radius inflated by the standard deviations; (iii) probability of collision `p(x) <= s` with maximum probability 0.5 and robot radius 1.2 m.
- Results: (i) 99 successful trials, 17.2% of them broke the obstacle constraint (Fig. 2d); (ii) 95 successful, 1% (Fig. 2e); (iii) 100 successful, 1% (Fig. 2f).
- Aggregation: Eq. (4), `p(x) = 1 - prod_{i=1}^{K} [1 - p_i]`, with each `p_i` from the series of Eq. (3) (formulation of [29], `n = 3`, `Sigma` the summed covariance of query point and neighbour, at most 75 terms summed, diagonal covariance assumed).

**Check against the PDF** (page 4 right column, crop `noise.png`; page 3 right column; page 4 left column, crop `eq4-5.png`; page 5 caption of Fig. 2): every number, symbol and figure-panel assignment agrees with the print.
