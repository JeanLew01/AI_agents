# Verifier report: urban-swarm-fixed-wing-paper, PDF pages 29-41

Status: COMPLETE.

- Package: `/home/jixia/AI_agents/paper2agent/NMPC/staging/urban-swarm-fixed-wing-paper-s1`
- Source: `documents/s001-urban-swarm-fixed-wing/source.pdf`, PDF pages 29-41 (printed pages 753-765)
- Package range: `references/paper.md` lines 521-907 (tail of the 8.3 paragraph that ends on page 29, Sections 8.4-8.6, 9, Acknowledgments, Appendices A and B, ORCID, References, "How to cite this article", publisher's note) and lines 909-915 (conversion notes); `SKILL.md`, `references/index.md`, `references/supplement.md` read once.
- Scratch (crops, native text, diff script): `paper-review/_scratch/verify-swarm-29-41/`
- Nothing in the package or the review plans was changed.

Result: **0 errors, 4 minor findings**, plus 3 observations that need no repair.

## Coverage

All 13 pages were checked in full; nothing was sampled except where stated.

| Check | What was done |
| --- | --- |
| Prose (pages 29-41) | Word-level diff (`cmp.py`, `difflib`, exact token equality including punctuation, quotes and dashes) of package lines 521-907 against the native PDF text layer with running headers/footers removed. Every non-equal block was read. The only differences are (i) mathematics (checked separately on crops), (ii) floats moved to paragraph boundaries, (iii) line-break joins. Page previews of 29-33 and 37 were also read next to the package text for paragraph breaks and headings. |
| Display equations (27)-(40) | Each compared symbol by symbol with 300-400 dpi crops of pages 34, 35, 36 (bold/italic, sub/superscripts, signs, fractions, limits, brackets, punctuation, `\tag`). |
| Inline mathematics | Every inline expression of Appendices A and B, of Sections 8.5/8.6 and of the captions of Figures 31 and 35 compared with crops. `$`/brace balance checked by script for lines 521-915. |
| Table 1 | All 8 rows x 5 columns of `assets/table/table-1.csv` and of the Markdown table compared with a 300 dpi crop; caption compared. |
| Figures 28-35 | All eight JPEGs opened and compared with the page images: completeness, no caption/body text inside, legibility. Captions covered by the word diff; captions of 31 and 35 also on crops. The "clipped in the PDF itself" claim was checked on crops that extend beyond the figure boxes (Figures 29, 30(c), 32(c)). |
| References | Entry count and order by script (PDF: 4 + 24 + 26 + 25 + 15 = 94 entries on pages 37-41; package: 94; the first 20 characters of every entry agree in sequence). All 94 entries are covered by the exact word diff against the text layer. In addition all 94 (not only every third) were read on 230 dpi crops for italics, diacritics and anything the text layer could hide. |
| Reading-order move | The paragraph running page 30 -> 31 -> 32 checked specifically (see "Checked and correct"). |
| Omissions | Page plans 29-41: the only `omit` items are the 26 running headers/footers. Nothing else printed on these pages is absent from the package. No footnotes exist on these pages. |
| SKILL.md / index / notes | All 35 "Exact heading" entries of `index.md` exist verbatim as headings in `paper.md`; all asset links in `paper.md` resolve; conversion notes read against the PDF. |

## Findings

| # | Severity | PDF page | Item id | Package says | PDF shows | Suggested fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | minor | 37 | p0037-b004 | ORCID block is six consecutive lines with plain newlines (paper.md lines 708-713), which Markdown renders as one run-on paragraph: "Max Basescu https://... Adam Polevoy https://... ..." | Six separate lines, one author per line | End each of the first five lines with a hard break (two trailing spaces or `\`), or make it a list. Text itself is correct. |
| 2 | minor | 29-32 | `references/index.md`, row "8.5. Swarm System Integration Experiments" | "Field experiments, Figures 28-33" | In `paper.md` only Figure 29 sits under the 8.5 heading. Figure 28 sits before the 8.4 heading (under 8.3, line 523) and Figures 30-33 sit under 8.6 (lines 547-561) after the reading-order move. A reader who follows the index and reads only the 8.5 section finds one of the six figures. | Reword the row, e.g. "Field experiments (Figure 29; Figure 28 precedes 8.4, Figures 30-33 follow the 8.6 paragraph)", and/or mention Figures 30-33 in the 8.6 row. |
| 3 | minor | 30, 31 | p0030-b006, p0031-b008b (and paper.md line 53, outside my range) | `RT-RRT$^*$` (four times in line 545), i.e. the asterisk is set as a mathematics superscript | "RT-RRT*" with an ordinary text asterisk (text layer and crop). The same name in the reference list is written `Rt-rrt\*` in the package. | Cosmetic, renders almost identically. For consistency and literal search (`rg -F 'RT-RRT*'` currently finds none of the body occurrences) write `RT-RRT\*`. |
| 4 | minor | 36 | p0036-b011 | Header cell "Surface Area (m^2)" in `table-1.csv` and in the Markdown table (plain caret) | "Surface Area (m²)" with a superscript 2 | Cosmetic. Use `m$^2$` in the Markdown table (and optionally `m²` in the CSV). |

No discrepancy was found in any symbol, number, sign, limit, equation number, table cell, reference entry, heading or sentence of the range.

### Observations (no repair needed)

- Conversion note on floats: "Figures 19-21 and Figures 30-31 were moved after the end of the paragraph they interrupt". This is true. Figures 32-33 (top of page 32, printed before the last two lines of the same paragraph) and Figures 28, 29 and 34 (each at the top of a page inside a running paragraph) were treated the same way; they are covered by the note's general sentence "Floats sit at paragraph boundaries near their printed position", so the note is not false, only less specific for them.
- Conversion note "External metadata: ... IEEE Transactions on Field Robotics, vol. 1, pp. 394-423, 2024, DOI 10.1109/TFR.2024.3496420": cannot be confirmed or refuted from the PDF (it is labelled as external and "not compared"). I did not check it elsewhere. The other source facts in that note that are printed in the PDF are correct (DOI 10.55417/fr.2023023 and "revised: 21 November 2023; accepted: 7 March 2023" on page 1; "Field Robotics, May, 2023 · 3:725-765" appears only in the footers).
- `table-1.csv` uses CRLF line endings (standard CSV output); harmless.

## Checked and found correct (by page)

- **Page 29**: tail of 8.3 joins the page-28 text continuously ("...during every planning interval to evaluate a minimum distance constraint..."). Figure 28 JPEG complete (all blocks, three aircraft photos, orange labels "Start Tactic", "General Params", "RT-RRT* Path,", dotted and dashed frames, "RGBD camera data" line); no caption inside; caption verbatim. Headings "8.4. Swarm System Integration" and "8.5. Swarm System Integration Experiments" as printed, subsection level. Italic *a priori* kept. 8.4 paragraph verbatim.
- **Page 30**: 8.5 first paragraph reads continuously across the page break ("We tested | launching the vehicles..."), Figure 29 placed after it. Numbers "at least 4 m", "in altitude by 4 m", "≈ 5 m width", "four times", "Field Exercise 6", "Figure 24" correct. Figure 29 JPEG complete; the half-cut "Y (m)" and "X (m)" labels are cut in the PDF itself (white space follows them before the caption), as the notes state. Heading "8.6. Future Steps for Swarm System Integration" correct.
- **Pages 30-32, moved floats**: the 8.6 paragraph now reads "...provided by NMPC algorithm. We could also apply additional constraints to the online trajectory optimizer to restrict all trajectories to be within a prespecified radius of the flight path. Initially, we did not believe that the RT-RRT* approach, which updates at 1 Hz, ... (> 100 m), ... For handling unmapped obstacles or dynamic obstacles in the environment, we could leverage onboard sensing and our vision-based planning algorithm." The three printed fragments (page 30 end, five lines on page 31, two lines on page 32) are joined in order, each word exactly once: nothing lost, nothing duplicated. Printed authors' slips kept ("does the tree rewiring ... lends itself", "by NMPC algorithm").
- **Page 31**: Figure 30 JPEG has panels (a), (b), (c) with their sub-labels, colour bar and axis labels; "X (m)" of panel (c) is cut in the PDF itself. Figure 31 JPEG has both panels with colour bars "Speed (m/s)" and "Angle-of-Attack (degrees)". Captions verbatim ("max 30 mph", "max 60°", "Building 15", "shows the how the wind varied" kept as printed).
- **Page 32**: Figure 32 JPEG complete with (a)-(c); "Y (m)" of panel (c) is cut in the PDF itself. Figure 33 JPEG has both stills. Captions verbatim. Heading "9. Discussion" at section level.
- **Page 33**: Figure 34 JPEG has both screenshots; caption verbatim. First paragraph of Section 9 reads continuously across the page break ("...in indoor environments using | offboard sensing and processing..."). Six paragraph breaks of Section 9 match the printed indents. Numbers "42-inch", "about 1 m", "4 m", "3 m", "2.95 m" correct. "we were also able track", "enough time plan" kept as printed.
- **Page 34**: Discussion end, citations (Manchester and Kuindersma, 2017; Bonzanini et al., 2019; Singh et al., 2019; Garimella et al., 2018) correct. "Acknowledgments", "Appendices", "A. Analysis of Post-Stall Turns" present ("OFFensive Swarm-Enabled Tactics" joined correctly). Equations:
  - (27) `c(θ, v, r, f_t) = R^r_b f^b_a + R^r_b f^b_t + g − a = 0.` Bold θ, R, f, g, a; second argument is `v` (not `v_θ`), as printed.
  - (28) `f^b_t = f_t e_x`, `g = −mg e_Z`, `a = −(m v_θ²/r) e_r,` Capital Z subscript, trailing comma.
  - (29) `f^b_a = ρ S v_θ² sin(α) e_z,`
  - (30) `R^r_b f^b_a = (−ρ S v_θ² / 4) e_θ.` Minus sign inside the numerator, as printed.
  - (31) `R^r_b f^b_a = ρ S v_θ² (C_L n_L + C_D n_D),`
  - Inline: bold `e_{x,y,z}`, `e_{r,θ,Z}`, definitions of `f_t`, `m`, `g`, `v_θ`, `r`, `S`, `ρ`; "flat plat theory" kept as printed.
- **Page 35**: `α ≤ α_crit` (italic subscript as printed), "NACA 2412". Equations:
  - (32) `min_{Θ, v, r, f_t} Σ_k P_k  s.t.  c(θ, v_θ, r, f_t) = 0,` Bold capital Θ under min and bold lower-case θ with `v_θ` in the constraint, as printed (differs from (27); reproduced as printed, as the notes say). "where P is the power for the k^{th} rotor."
  - (33) `P = f_t V_⊥^∞ + κ f_t ( −V_⊥^∞/2 + sqrt( V_⊥^∞/4 + f_t/(2 ρ A_disk) ) ),` No square on `V_⊥^∞/4` in the PDF; package reproduces this.
  - `κ = 1.2`; `α > 15°`; `α < 10°`; citations (Chauhan and Martins, 2020; Chauhan, 2020), (Glauert, 1927), (Huang et al., 2009; Bangura and Mahony, 2017) correct.
  - "B. Energy Analysis" heading. (34) `E_total = E_straight + E_turn,`; inline `E_turn = P_turn r ψ_turn`; (35) `E_straight = E_start + E_stop + E_cruise`; (36) `= P_start d_start + P_stop d_stop + P_cruise d_cruise,` Tags (35) and (36) on separate lines as printed.
- **Page 36**: inline `d_stop and d_start` (this order), `P_cruise`, "(Equation 32)", `r = ∞`. Equations:
  - (37) `v(t) = ∫_{v_i}^{v_f} v̇ dt,` Velocity limits on a time integral, as printed.
  - (38) `v̇ = g/tan θ − c ρ v² S/m,` with `c = 0.5` (quadcopter) and `c = 1` (fixed wing).
  - (39) `θ = ± arcsin( m g / f_{t,max} ),`
  - (40) `f_t − m g / sin θ − ρ v² S cos θ = 0,`
  - Inline `f_t ∈ [0, f_{t,max}]`, `E_r = E_fw / E_quad`, "Equation 33", "90° turn", "20 m straightaways and 2 m turns", "factor of two or more".
  - Table 1 caption verbatim ("model use to compute", as printed). Cells: (a) Mini Edge 540 0.100 / 0.151 / 0.152; Tello 0.100 / 0.022 / 0.0762; (b) EdgeV3 0.450 / 0.369 / 0.279; Mavic Air 0.450 / 0.022 / 0.135; (c) Edge540XL 1.00 / 0.449 / 0.305; Mavic2 1.00 / 0.022 / 0.220; (d) Gamebird 3.00 / 0.670 / 0.406; Matrice 3.00 / 0.022 / 0.330. All 32 data cells and the trailing zeros match; pair labels repeated on both rows as documented.
- **Page 37**: Figure 35 JPEG complete (z label "Energy Ratio E_fw/E_quad", both horizontal axis labels, colour bar, surface labels (a)-(d)). Caption verbatim including `R_max` and `10 (π/2) R_max`. Six ORCID identifiers correct digit by digit. First four reference entries.
- **Pages 37-41, references**: 94 entries, alphabetical order as printed, none merged or split. Authors, years, titles, venues, volumes and pages agree for all entries; italics agree with the print (including the non-italic entries Chung 2021, Herbst 1984, Hoerner and Borst 1985, Lavalle 1998, Murray 2007, Min 2004 - 2019). Diacritics correct (Blösch, Hernández Ramírez, Rajamäki, Hämäläinen, Möller, D’andrea). Printed peculiarities kept: lower-cased titles ("nmpc", "uav", "gps"), "IEEE Robot. Autom. Lett", "pages 4186-4191 vol.5", "Journal of Intelligent and Robotics Systems, 101(24)" next to the 2021 duplicate, "(2004 - 2019)", "URL: www. ardupilot. org, accessed, 2:12", "Unmanned... Unlimited". Line-break hyphens resolved correctly ("computa-tionally" -> "computationally"; "rapidly-exploring", "710-733", "24(4):17-26" and the split binvox URL joined correctly).
- **Page 41**: "How to cite this article" box verbatim (italic *Field Robotics, 3*), publisher's note verbatim.
- **Whole range**: no leftover extraction damage (`<sup>`, glyph soup, split decimals, stray `_`/`**`); all `$` and braces balanced; all linked assets exist.
- **SKILL.md / index.md / supplement.md**: SKILL.md statements are consistent with the package; every index heading exists exactly in `paper.md`; "94 entries in author-year style; followed by 'How to cite this article' and the publisher's note" is correct; equation ranges (27)-(33) for A and (34)-(40) plus Table 1 for B are correct. Conversion notes for this range (three printed oddities in (27)/(32), (33), (37); Table 1 merged labels; clipped axis labels of Figures 29, 30(c), 32(c); headers/footers omitted) are all true.

## Technical question answered from the package only

**Question.** In the energy comparison of the appendix, how is the propulsive power of a rotor computed and with which correction factor, and how do the start/stop (acceleration/deceleration) models of the quadcopter and the fixed wing differ?

**Answer from the package** (`paper.md`, "A. Analysis of Post-Stall Turns" for (33); "B. Energy Analysis" for (34)-(40) and Table 1).
- Rotor power: `P = f_t V_⊥^∞ + κ f_t ( −V_⊥^∞/2 + sqrt( V_⊥^∞/4 + f_t/(2 ρ A_disk) ) )` (33), where `V_⊥^∞` is the freestream velocity component perpendicular to the actuator disk and `A_disk` the disk area, with `κ = 1.2` for unmodelled losses. It follows Chauhan and Martins (2020) / Chauhan (2020) and deliberately not Glauert's modified momentum theory: only the perpendicular free-stream component is assumed to contribute to thrust. (The term `V_⊥^∞/4` carries no square in the paper; the conversion notes flag this as printed.)
- Energy of a path segment: `E_total = E_straight + E_turn`, `E_turn = P_turn r ψ_turn`, `E_straight = P_start d_start + P_stop d_stop + P_cruise d_cruise` (34)-(36). `P_cruise` comes from the minimum-power program (32) with `r = ∞` and low angle-of-attack lift/drag coefficients.
- Start/stop: one-dimensional longitudinal dynamics `v̇ = g/tan θ − c ρ v² S/m` (38) with `c = 0.5` for the quadcopter and `c = 1` for the fixed wing. Quadcopter: maximum throttle, `θ = ± arcsin(m g / f_{t,max})` (39), sign by acceleration direction. Fixed wing: `θ(t)` is the largest value satisfying `f_t − m g / sin θ − ρ v² S cos θ = 0` (40) with `f_t ∈ [0, f_{t,max}]`. `P_start`, `P_stop` then follow from (33) and `d_start`, `d_stop` from integrating `v(t)`.
- Reported outcome: the energy ratio `E_r = E_fw/E_quad` for the four equal-mass pairs of Table 1 (0.100, 0.450, 1.00, 3.00 kg) shows a larger fixed-wing advantage at small scales; fixed wings almost always outperform quadrotors except in persistent hover-like paths made up entirely of tight turns, often by a factor of two or more at urban scales (e.g. Edge540XL, 20 m straightaways, 2 m turns); start/stop energy matters little except at very low turn radii.

**Check against the PDF.** Compared with the crops of pages 35 and 36 (`p35-eq33.png`, `p35-eq34-36.png`, `p36-eq37.png`, `p36-eq38-40.png`, `p36-table1.png`): every formula, `κ = 1.2`, `c = 0.5` / `c = 1`, `r = ∞`, the four masses and the quoted conclusions agree with the printed text. The answer is fully supported by the PDF.
