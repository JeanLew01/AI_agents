# Verifier report: andrieu-pmcmc-2010-paper, PDF pages 37-55 (printed 305-323)

Package: `staging/andrieu-pmcmc-2010-paper-s1` (`references/paper.md` lines ~861-1345). Reference: `source.pdf` rendered at 170 dpi (whole pages) and 250-300 dpi crops. Scratch: `paper-review/_scratch/verify-andrieu-37-55`.

## Coverage
- All 19 pages viewed as page images next to the package text.
- Mathematics: every display on pages 37-55, including (44)-(54) and all unnumbered displays, compared with page images; 260 dpi crops for the dense ones (p37 Chen weights, p38 (44), p42 (46)-(51), p43 (52)-(54)). Inline maths read against the 170 dpi pages (not every inline symbol re-cropped).
- Prose: automated word-level diff of the PDF text layer against the package text (words of 4+ letters and years, maths stripped) for the whole range, plus visual reading. No missing, duplicated or reordered prose found.
- Tables: every cell of table-d-p0039, table-d1-p0040 (17 rows x 7) and table-d2-p0041 (22 rows x 6) compared with the native text layer line by line and with 250 dpi crops; CSVs are identical to the Markdown tables.
- Figures: assets figure-d9 ... figure-d16 opened; captions compared with the page.
- Algorithm step lists (Chen (a)-(c); Łatuszyński and Papaspiliopoulos algorithms 1-4) compared line by line.
- Headings: all 20 contribution headings touching the range compared with the print. No reference list falls in this range.
- SKILL.md, index.md and the conversion notes read once; index headings for this range exist verbatim in paper.md.

## Findings

| # | Severity | PDF page | Item id | Package | PDF | Suggested fix |
|---|---|---|---|---|---|---|
| 1 | error | 44 | p0044-b000 (figure-d9-p0044.jpg) | Crop starts at x=90 pt: the upper part of the `mus` trace panel of Fig. 9(a) (panel frame line, the highest peaks of the trace, part of the y-axis tick region) is cut off at the image edge | The `mus` panel frame begins at about x=82 pt; whole panel is printed | Widen the figure bbox to about [76, 50, 367, 628] and re-crop |
| 2 | minor | 46 | p0046 (paragraph "and state space moves derived from ...") | `AR(l)` (letter l) | Printed glyph is also the letter "l" (meaning AR(1)) | The conversion note says such 'l'-for-'1' cases are written as digits (done for "(1999)", "(2001)" on p55); make consistent: `AR(1)`, or keep verbatim and say so |
| 3 | minor | 55 / notes | p0055-b006; Conversion notes last bullet | Note claims digit 1 is stored as 'l' "in the PDF text layer"; text gives "Kendall et al. (1999), Liu and West (2001)" | The printed page itself visibly shows "(l999)" and "(200l)" (300 dpi crop), i.e. it is a print typo, not only a text-layer artefact | Keep the correction but reword the note (printed 'l' silently corrected to '1'), and list AR(l) |
| 4 | minor | 49-51 | p0051-b003 and following items on p51 | "Adaption can be local ...", the two PRC displays, "As presented in Peters et al. ..." and "Cornebise et al. (2008) stated ..." are ordinary top-level paragraphs | On p51 all of this text is set with the hanging indent of list item (b) of p49 (left edge 74 pt vs 48 pt), i.e. it is printed as the continuation of item (b) | Optional: indent as continuation of item (b), or add a note; content is complete |
| 5 | minor | 43-46 | Robert et al. contribution | Figs 9 and 10 (links + captions) are inserted inside the sentence "With parameter moves [Fig. 9][Fig. 10] $$\mu^*\sim...$$ and state space moves ..." | Full-page sideways figures on pp. 44-45 interrupt the sentence in print | Move both figures after the paragraph ending "... within $10^4$ iterations." (the notes say floats sit at paragraph boundaries; this one does not) |
| 6 | minor | 44-54 | figure link labels | Link text is "Fig. 9 (discussion: Robert, Jacob, Chopin and Rue)" / "Fig. 10 (...)" but "Figure 11" ... "Figure 16" for the others | - | Cosmetic: unify link labels |

Errors: 1. Minors: 5.

## Checked and found correct
- p37: Chopin continuation (page 36->37 boundary, paragraphs complete); Chen heading; steps (a)-(c); displays for w_n, W_n^k, the weight-spreading product (incl. printed "M_{n-l}|X_{1:n-l-1}" and exponent 1/L), auxiliary-filter alpha; printed oddity "γ_{t-1}(x_t − 1)" kept.
- p38: product display (37->38 continuation), Girolami, Whiteley, eq. (44), printed "π̃^N = (b_n^k| ...)" kept as printed.
- p39: proportionality display; Roberts: π̃^N(θ) display, unnumbered step table (all 6 rows x 4 columns), invariant distribution display, f_θ(x)=h/K display on p40.
- p40-41: Belmonte and Papaspiliopoulos heading; Table 1 (all 119 numeric cells, signs, "−0.0000" entries) and footnote; eq. (45) (incl. printed "η_t, ∼"); parameters μ=0.75, φ=0.95, 0.35; Table 2 (all 126 numeric cells; row labels l(μ_KF), V̂(μ_KF) without hat on μ as printed) and footnote; 41->42 sentence continuity ("When the state has so high persistence").
- p42-43: Łatuszyński and Papaspiliopoulos: algorithms 1-4, all steps; (46)-(53) including the printed missing parenthesis in (47) and U_{n-1} without tilde in (53); filtration display; printed misspellings "congraulate", "Łatuszński" kept. Flury and Shephard. Robert et al. heading, (54), SV model display (printed "exp(xt)" kept).
- p44-45: Fig. 9 and Fig. 10 captions (N=10^2, 10^4, μ0=1, ρ0=0.9, σ0=0.5); figure-d10 complete.
- p46: proposal displays (20^{-2}), URL, items (a)-(b), p̂ product display, "The following contributions were received in writing after the meeting.", Bhadra.
- p47-48: figure-d11 complete, caption (line-style marks approximated by design); Bornn and Tabet; Cappé; figure-d12 complete and caption (2.26^{-T}, integral, 10^{-6}, T=17).
- p49-51: Cappé end; Cornebise and Peters heading, p̂ display, items (a)-(b); figure-d13/14/15 complete, captions (0.01, 0.04, T=100, r<2.69, 100000, N=200, 5000, 103, i=10, i=20000); PRC kernel and r(c_n,x_{n-1}) displays.
- p52-53: Creal and Koopman (T=400, T=1000, equations (16)); Crisan; Draper (a)-(b); Everitt: both displays, inline maths, equation (35).
- p54-55: Golightly and Wilkinson: SDE, Euler-Maruyama display, α and β matrices (all entries and signs), θ=(0.5,0.0025,0.3), U(−7,2), 500000, m=5, 1:8:20:40; figure-d16 complete and caption; Ionides; Jacob et al. heading and both displays up to the end of p55.
- Headings: no contribution missing or merged; names and affiliations as printed. No doubled backslashes, `<sup>`, split decimals or glyph soup in the range. Notes on (47)/(53) are true.

## Technical question answered from the package only
Q: In Belmonte and Papaspiliopoulos's simulation, how do PMMH and PG behave as T grows to 5000-10000 with N=500?
A (from "Miguel A. G. Belmonte ... and Omiros Papaspiliopoulos ...", Table 1): PMMH acceptance probability falls from 0.606 (T=100) to 0.004 (T=5000) and 0.003 (T=10000) and its integrated autocorrelation-time proxy 1/(1−ρ̂) rises from 5.77 to 165.85 and 178.91; PG stays at 1.00-1.02 for all T with relative error of at most about 0.016 in magnitude. Check against PDF p40 (Table 1 crop and text layer): all values confirmed.
