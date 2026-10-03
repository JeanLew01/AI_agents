# Verifier report: urban-swarm-fixed-wing-paper, PDF pages 1-14

Status: COMPLETE.

- Package: `/home/jixia/AI_agents/paper2agent/NMPC/staging/urban-swarm-fixed-wing-paper-s1`
- Source: `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/urban-swarm-fixed-wing-paper/documents/s001-urban-swarm-fixed-wing/source.pdf`
- Range: PDF pages 1-14 = `references/paper.md` lines 1-283 (start to end of "5.2. System Identification"), plus `SKILL.md`, `references/index.md` (all rows) and the conversion notes (paper.md lines 909-915).
- Scratch: `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/_scratch/verify-swarm-1-14/` (crops `p8a..p12c.png`, `p11z.png`, `p3ab.png`, `f1pdf.png`, `f2pdf.png`, word-diff scripts and outputs).
- Result: **0 errors, 8 minor findings.** Nothing in the package or the review plans was changed.

## Coverage (what was actually done)

| Check | Extent |
| --- | --- |
| Prose, pages 1-14 | Full. Automated word-level diff of paper.md lines 1-284 against the native PDF text (`worddiff2.py`, alphanumeric tokens) and a second pass including punctuation tokens (`worddiff.py`). Outside mathematics the only differences are relocated floats/footnotes. Pages 1, 6, 7, 13, 14 additionally read against page renders. |
| Display equations (1)-(26) | Full. Every equation compared symbol by symbol with 220 dpi crops of pages 8-12 (330 dpi for (22)). Tags, punctuation, line breaks with `...`, bold/italic, subscripts and superscripts checked. |
| Inline mathematics | Full for pages 8-12 (all definitions, bounds, constants) from the same crops; pages 3, 6, 7, 14 from native text plus a 300 dpi crop of page 3. |
| LaTeX balance | Programmatic: 26 display blocks and 113 inline spans in lines 1-284; braces, `\left/\right`, `\begin/\end`, `$` parity all balanced; tags 1-26 present once each, in order. |
| Numbers in prose | Full for pages 12-14 (Sections 4, 5, 5.1, 5.2) and Section 3.2. No tables in this range. |
| Structure | All headings of the range compared with the PDF (text, numbering, level); page-crossing paragraphs 1-2, 2-3, 3-4, 4-5, 5-6, 6-7, 12-13, 13-14 read continuously; no duplication of body text; no extraction damage (`<sup>`, ligatures, glyph soup: none). |
| Figures 1-8 | All eight JPEGs opened and compared with the pages; captions compared word for word. |
| First-page metadata | Full: special-issue line, article type, title, authors, affiliation, abstract, keywords, dates, correspondence, licence, copyright, DOI. |
| SKILL.md, index.md | Read in full; every index heading checked programmatically for exact existence in paper.md; "look here for" hints checked against paper.md content. |
| Conversion notes | Each claim touching pages 1-14 checked against the PDF; the external IEEE T-FR metadata claim checked against the Crossref record. Claims about pages 15-41 were not checked (other verifiers). |
| References | Not in this range. Only the index claim "94 entries" was checked (94 in the package, 94 in the PDF, pages 37-41). |

## Findings

| # | Severity | PDF page | Item id | Package says | PDF shows | Suggested fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | minor | 1 | p0001-b003 (and builder title) | `# Agile Fixed-Wing UAVs for Urban Swarm Operations` appears twice as H1 (paper.md lines 1 and 7), with the special-issue line and "Regular Article" between them. | Title printed once. | Keep one H1 (drop the builder title on line 1, or demote the printed title item to bold text). |
| 2 | minor | 5 | p0005-b010, p0005-b009 | Footnote text sits directly under `## 3. Approach`, before the paragraph that cites it, as "Footnote 1: ...". The citing paragraph carries the marker `[^1]`, which has no matching `[^1]:` definition and therefore renders literally. | Footnote 1 at the foot of page 5, cited after "supermaneuverability." | Move the footnote after the citing paragraph and make marker and text agree (either `[^1]: Supermaneuverability ...` or a plain "(Footnote 1)" marker). Text itself is correct. |
| 3 | minor | index | index.md row "3.2.2. Direct trajectory optimization" | "NMPC problem, collocation (Hermite-Simpson versus Euler) and constraints" | Section 3.2.2 gives only the Simpson direct-transcription problem (22)-(23). The Hermite-Simpson versus Euler comparison is in Section 4 (PDF page 12, Figure 5). | Change to "NMPC feasibility problem, Hermite-Simpson collocation constraints (22)-(23), bounds" and add "Hermite-Simpson versus Euler, knot-point study, Figure 5" to the Section 4 row. |
| 4 | minor | index | index.md row "4. Real-time Trajectory Optimization Performance" | "Solver timing and convergence study" | Section 4 reports computation time and trajectory-following cost versus number of knot points; there is no convergence study. | "Computation time and trajectory-following cost versus knot points (Hermite-Simpson versus Euler, warm start), Figure 5". |
| 5 | minor | index | index.md row "1. Introduction" | "Motivation, DARPA OFFSET context, contributions" | Section 1 never mentions DARPA or OFFSET (only the special-issue line above it, Sections 6.6, 6.7, 8.5 and the Acknowledgments do). | "Motivation, ACCIPITER overview, contributions, paper organisation". |
| 6 | minor | index | index.md row "8.5. Swarm System Integration Experiments" | "Field experiments, Figures 28-33" | In paper.md the Figure 28 caption is under 8.3 (cited in 8.4 and 6.2), only Figure 29 lies inside the 8.5 heading range, and the captions of Figures 30-33 lie under the 8.6 heading. | "Field experiments, Figures 29-33 (captions of 30-33 follow the 8.6 heading)"; mention Figure 28 in the 8.4 row. Outside my page range: please confirm with the pages 29-41 verifier. |
| 7 | minor | index | index.md | No row for the heading "Conversion notes", although SKILL.md tells the reader to consult document notes and to state extraction limitations. | n/a | Add a row "Conversion notes: source, printed oddities kept, float moves, asset limitations". |
| 8 | minor | 6 | conversion notes, last bullet; asset figure-1.jpg | Notes list clipped axis labels in the publisher's PDF only for Figures 29, 30(c), 32(c). | The x-axis label "Turn Radius (m)" of Figure 1(b) is also cut at its lower edge in the PDF itself (400 dpi crop `f1pdf.png`); the asset reproduces this faithfully and is not at fault. | Optional: add Figure 1(b) to that list so a reader does not suspect the crop. |

No finding changes a symbol, number or statement of the paper.

## Checked and found correct (by page)

- **Page 1**: special-issue line; "Regular Article"; title; six authors in order with "and"; affiliation "Johns Hopkins University Applied Physics Lab, Laurel, Maryland 20723, USA"; two abstract paragraphs; keywords (aerial robotics, obstacle avoidance, navigation, robot teaming); "Received: 18 June 2022; revised: 21 November 2023; accepted: 7 March 2023; published: 12 May 2023." exactly as printed (including the impossible revision date); correspondence line and e-mail; Creative Commons Attribution licence sentence; "Copyright © 2023 Basescu, Polevoy, Yeh, Scheuer, Sutton and Moore"; DOI https://doi.org/10.55417/fr.2023023. Running header, page number and the `http://fieldrobotics.net` footer are omitted as intended.
- **Pages 2-5**: Sections 1, 2, 2.1, 2.2, 2.2.1, 2.2.2, 2.3, 2.4: all words and citations identical; printed slips kept ("system system", "a an outer control loop", "dynamically a feasible", "outer-loop a virtual-target-following"); `$\leq 30^\circ$` and `RRT$^*$` match the page 3 crop; heading levels H2/H3/H4 follow the printed numbering.
- **Pages 5-7 (Section 3)**: text complete and continuous across the Figure 1 and Figures 2-3 floats; "(> 6)"; footnote 1 text correct; Figure 1, 2, 3 captions word for word ("90°", "0.6 T/W", "NACA 2412", "10° and 15°", "α < 10°").
- **Page 8**: (1) state vector, 16 components in the printed order; inline definitions of r, θ, δ, δ_al = −δ_ar, δ_t, v, ω, O_{x_r y_r z_r}, O_{xyz}, x = [r, θ, δ, δ_t, v, ω]^T, u_cs = [ω_ar, ω_e, ω_r]^T; (2)-(7) including T_ω^{-1}, R_b^r f/m and J^{-1}(m − ω × Jω); v_b = R_b^r{}^T v; (8) with the bracketed sum, −mg R_b^r{}^T e_z, R_t^b f_t, f_d; f_t = [δ_t 0 0]^T; (9); (10) with γ_i v_bw and (R_{s_i}^b{}^T ω + ω_{s_i}) × r_{s_i}.
- **Page 9**: (11) actuator-disk backwash (‖v_p‖_2^2 + 2δ_t/(ρ S_disk) under the root, minus ‖v_p‖_2, times e_x); (12) C_{n_i} = 2 sin α_{s_i} (no punctuation, as printed); (13); "i^{th}"; (14); l_{s_i} = r_{h_i} + R_{s_i}^b r_{s_i}; "(Equation 5)"; u_t ∈ [0, 1]; (15) with C_{b_d}; heading 3.2; Figure 4 caption.
- **Page 10**: 3.2.1 text; "10% bias"; x = [x_0, x_1, …, x_n]; [W_1, W_2, W_3]; κ_max "(set to 2 m^{-1})"; (16) with bold subscripts, E_c in the order E_3 E_2 E_1 E_0 and "R^{3x4}" as printed; (17) with the printed "…" line break and "s ∈ [0, 1],"; (18).
- **Page 11**: (19) all three cross-product terms and the 3/2 power; (20) "v_max − κ(s) * m, s ∈ [0, s_p],"; (21); T_H; 3.2.2 text ("are are often" kept); (22) every line: min over x_k, u_k, h of 0, "∀k ∈ [0, …, N] and", h/6.0 Simpson defect, final/initial boxes with δ_f, δ_i, state and input bounds, d(x) ≥ r, h_min ≤ h ≤ h_max; (23) four lines including the /8 midpoint correction.
- **Page 12**: h_min = 0.001s, h_max = 0.2s; (x_f, x_i); (24) with K printed without (t); (25) two lines with "…"; A(t) with x_0 lacking (t) and B(t) with x_0(t), as printed; (26); Q_f; Section 4: Euler constraint `x_{k+1} − x_k − h(x_k, u_k) = 0` printed without f and with bold k subscripts, reproduced exactly; "≈ 20 knot points", "almost 2-1", "below 30 knot points", "10 knot points", "24 knot points", "4:1", "(≈0.1s for a warm start)".
- **Page 13**: Figure 5 and 6 captions; Section 5 opening paragraph continuous across the floats; 5.1: "24-inch", "120 g", "13 g 2300 Kv Crack Series", "7x3.5 GWS", "five Vicon markers".
- **Page 14**: "8m x 8m", "10 Vantage V5 cameras", "200 Hz", "Dell Precision 5530", "Intel i7-8850H", "vicon_bridge", "8 MHz Arduino Pro Mini", "Spectrum DX6i"; 5.2: factors 1.7 and 0.75, γ_ar = γ_al = γ_r = 0.1, γ_e = 0.3, C_{b_d} = 0.0, a_t = −4.9167, b_t = 9.6466; Figure 7 and 8 captions.
- **Figures 1-8 (assets)**: all complete and legible, no caption or body text inside the crops. Figure 1 includes both panels and the (a)/(b) labels; Figure 2 includes both axis labels and the colour bar; Figure 3 includes all in-figure formulae and both frames; Figure 4 the whole block diagram including the outer feedback loop; Figure 5 both plots with legends and titles; Figure 6 the photograph; Figures 7 and 8 all three panels with titles and axis labels.
- **index.md**: all 35 main-paper headings exist verbatim in paper.md; sub-sections named in "Parent of" rows exist; "equations (27)-(33)" under A and "(34)-(40), Table 1" under B agree with the tags in paper.md; "Algorithm 1" is under 7.2; "94 entries" confirmed. `assets/supp_figs/` and `assets/supp_table/` exist (empty), consistent with supplement.md ("No corresponding materials were supplied").
- **SKILL.md**: front matter and instructions consistent with the package layout; nothing false.
- **Conversion notes** (claims within my range, all true):
  - first-page dates are printed as "revised: 21 November 2023; accepted: 7 March 2023";
  - Figure 5: the caption calls the lower-plot Hermite-Simpson curve blue and Euler green, the legend shows Hermite-Simpson green (solid) and Euler blue (dashed); the upper-plot colours agree with the caption;
  - Figure 2 colour bar is labelled "Angle-of-Attack (rad)" with a 10-80 scale;
  - A(t) is printed with x_0 without (t);
  - the Euler constraint on page 12 is printed without f;
  - the lower plot of Figure 5 has very small tick labels;
  - equations (1)-(26) are all LaTeX, none kept as an image;
  - floats in this range sit at paragraph boundaries near their printed position;
  - source line (journal, May 2023, vol. 3, pp. 725-765, DOI, 41 pages) agrees with the PDF headers and first page;
  - the external claim (IEEE Transactions on Field Robotics, vol. 1, pp. 394-423, 2024, DOI 10.1109/TFR.2024.3496420) agrees with the Crossref record for that DOI (same title and authors). This is not verifiable from the PDF.

## Technical question answered from the package alone

**Question.** Which collocation constraint does the direct NMPC enforce between knot points, how is the time step bounded, and how many knot points did the authors settle on and why?

**Answer from the package** (Sections "3.2.2. Direct trajectory optimization" and "4. Real-time Trajectory Optimization Performance"). The planner solves a feasibility problem (objective 0) over x_k, u_k and a common step h with SNOPT. The dynamics are imposed by the Hermite-Simpson defect x_k − x_{k+1} + (h/6.0)(ẋ_k + 4ẋ_{c,k} + ẋ_{k+1}) = 0, with u_{c,k} = (u_k + u_{k+1})/2, x_{c,k} = (x_k + x_{k+1})/2 + h(ẋ_k − ẋ_{k+1})/8 and ẋ_{c,k} = f(t, x_{c,k}, u_{c,k}) (equations (22)-(23)). Further constraints: box tolerances δ_f and δ_i on the final and initial states, state and input bounds, the obstacle clearance d(x) ≥ r from a distance map, and h_min ≤ h ≤ h_max with h_min = 0.001 s and h_max = 0.2 s. In Section 4 the authors compare this with an Euler constraint: Euler only became feasible at about 20 knot points and needed 24 for comparable tracking, while Hermite-Simpson tracked well at 10 and was almost twice as fast below 30 knot points; warm starting gave about 4:1 over a naive seed. They chose Hermite-Simpson with 10 knot points (about 0.1 s for a warm start).

**Check against the PDF.** Pages 11-12 (crops `p11c.png`, `p11z.png`, `p12a.png`, `p12c.png`): every formula, bound and number above matches the print.
