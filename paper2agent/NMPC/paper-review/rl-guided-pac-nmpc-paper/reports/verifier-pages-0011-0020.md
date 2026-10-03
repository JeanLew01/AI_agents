# Independent verifier report: RL-Guided PAC-NMPC, PDF pages 11-20

- Package: `/home/jixia/AI_agents/paper2agent/NMPC/staging/rl-guided-pac-nmpc-paper-s1`
- Document: `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/rl-guided-pac-nmpc-paper/documents/s001-rl-guided-pac-nmpc`
- Range: PDF pages 11-20 (printed 10-19): Section VII from "A. Fixed-wing Dynamics and Depth Camera Sensor", Section VIII, Section IX, References. `paper.md` lines 433-990 plus the conversion notes (lines 992-1000).
- Scratch (crops, scripts): `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/_scratch/verify-rl-11-20/`
- Date: 2026-10-02. The reviewers' reports were not read. Nothing in the package or the plans was changed.

Result: 1 error, 3 minor findings. The error is in `references/index.md`; the body text, mathematics, tables, figures and bibliography of pages 11-20 in `paper.md` matched the PDF in everything I checked.

## Coverage (what was actually done)

| Check | Extent |
| --- | --- |
| Display equations (24)-(52) and the two unnumbered displays on p. 11 | All 31, each compared symbol by symbol with a 220-300 dpi crop of the PDF. Tags present and in order (script). |
| Section VIII statements and proofs (pp. 16-17) | All: Lemma VIII.1, Lemma VIII.2, Theorem VIII.1, Definition VIII.1, Definition VIII.2, Theorem VIII.2, the four proofs, eqs. (35)-(52), read against 260-280 dpi crops of both columns of both pages. |
| Inline mathematics | Every inline expression on pp. 11-17 read against the crops (symbol definitions, bounds, constants, units). |
| Prose | Full, not sampled: word-level diff and an order-independent 4-gram comparison of `paper.md` lines 431-833 against the PDF text layer of pp. 11-18 (scripts `wdiff.py` and inline n-gram script). All differences were reading-order moves, line-break hyphens, page numbers or removed maths. In addition every column of pp. 11-18 was read as an image. |
| Tables V-IX | Every cell of `table-5.csv` ... `table-9.csv` and of the previews in `paper.md` against 240-300 dpi crops, including the position of the check marks in Table VII. |
| Figures 8-18 | All 11 JPEGs opened and compared with the page; captions compared with the PDF. |
| References [1]-[78] | All 78, not sampled: character-level comparison of every entry with the PDF text layer (`refdiff.py`), every line-break hyphen checked individually, and all three reference pages read as images for italic spans, diacritics and number grouping. |
| LaTeX sanity | Script over lines 431-991: `$` parity per line, brace balance, `\left`/`\right`, `\begin`/`\end` for 31 display and 224 inline expressions: no failure. |
| Headings / structure | All headings of the range against the PDF; run-in titles 1)-5) of VII-D; figure and table placement; sentence continuity across columns and pages. |
| Notes, index, SKILL.md | Read once; index rows for Sections VII-IX and the conversion notes checked against the PDF. |

Not done: no pixel-level comparison of figure crops with the PDF beyond visual inspection; pages 1-10 were not examined (other verifier).

## Findings

| # | Severity | PDF page | Item | Package says | PDF shows | Suggested fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | error | 14-15, 17-18 | `references/index.md`, rows "VII. FIXED-WING UAV ...", "E. Hardware Experiments" and "D. Simulation Experiment" | Row VII: "Tables V-VII". Row "D. Simulation Experiment": "Under VIII: experiment supporting the analysis, Tables VIII-IX". | Table VIII (out-of-distribution results) is in VII-D 5), PDF p. 14; Table IX (hardware results) is in VII-E, PDF p. 15. Section VIII-D (PDF p. 17-18) has no table: its results are Fig. 17 (environment) and Fig. 18 (success and collision rate against constraint penalty). | Row VII: "Tables V-IX, Figs. 8-16". Row "E. Hardware Experiments": add "Table IX, Figs. 13-16". Row "D. Simulation Experiment": "Under VIII: stochastic Dubins car experiment supporting the analysis, Figs. 17-18". Row "D. Simulation Experiments": add "Tables VI-VIII" for the occurrence under VII. |
| 2 | minor | 12 | Table V preview in `paper.md` line 525 (plan item `p0012-b016`) | Header cells `$\\delta_1$`, `$\\delta_2$`, `$\\delta_3$` (doubled backslash). | δ1, δ2, δ3. The CSV `assets/table/table-5.csv` has the correct single backslash `$\delta_1$`. | Emit `$\delta_1$` etc. in the Markdown preview. The same doubling is visible in the previews of Tables II-IV (`$V^{\\boldsymbol{\\phi}\\boldsymbol{\\psi}}$`, lines 386-427, outside my range), so it is a builder escape problem, not a single typo. With a maths renderer that reads the source raw, `\\delta` is a line break followed by the word "delta". |
| 3 | minor | 13-15 | Conversion notes, line 999; tables `p0013-b007`, `p0014-b001`, `p0014-b010`, `p0015-b011` | "Bold marking in Tables VI-IX is not recorded here; see the table images in the PDF." | The bold (best) cells are: Table VI - Cost 468.1 (RL Actor Network), Success 90% (Actor-Critic (ours)). Table VII - Success 90% and Cost 513.3 (row with both check marks). Table VIII - Cost 481.8 (RL Actor Network), Success 76% (Map & A* Unknown) and Success 76% (Actor-Critic (ours)). Table IX - Success 80% and Cost 252.2 (Actor-Critic (ours)). Table V has no bold cell. | Replace the last sentence of that note by the list above, as was done for Tables II-IV. The package contains neither the PDF nor table images, so the present pointer cannot be followed. |
| 4 | minor | 12 | `references/index.md` | No row for "C. Sensor Prediction" (occurs under VI and VII), although the notes mention the duplicate heading. | VII-C (PDF p. 12) holds the learned depth-image prediction model, Table V and Fig. 10, one of the paper's named contributions. | Add a row "C. Sensor Prediction: heading occurs under VI (LiDAR geometric projection) and under VII (learned U-Net depth prediction, Table V, Fig. 10)". |

Observations that are not package defects (no action needed, listed for the record):
- Fig. 16 (`figure-16.jpg`): the last x tick label ("25") is cut at the right edge. The PDF itself clips it (crop to the page edge, `p15-fig16.png`); the JPEG reproduces the print.
- Printed peculiarities kept faithfully: "the the widely adopted Nav2 framework" (p. 13) and "Nav 2" (p. 15); "RealSense D450"; `p(x_{t+N_T} | x, ξ)` with an unsubscripted x in Definition VIII.1; `g_k` in (47)-(48); `G_N` (not `N_T`) in (49); proof of Theorem VIII.1 ending with a comma before the box; "follow from definition VIII.2" in lower case; reference [18] "real- time"; reference [46] "Actor–critic" with an en dash.
- Figure 10's crop contains the sub-captions (a)-(e); they are part of the figure and are also transcribed in the text.

## Checked and found correct (by page)

- **p. 11**: heading "A. Fixed-wing Dynamics and Depth Camera Sensor"; eq. (24); unnumbered state-derivative display; eq. (25) all six component equations including `0.1(1 - q^T q)q`; unnumbered Ω(ω) matrix, all 16 entries and signs as printed; eqs. (26)-(31) including bold/italic subscripts of v_b, v_p; all symbol definitions; Fig. 8 and Fig. 9 crops and captions; RK2 sentence; 87° × 58°; heading "B. Actor Critic Training"; γ_c = 1500, 256 neurons, 10% dropout, 16 × 12.
- **p. 12**: Fig. 10 crop, sub-captions and caption; 0.2-0.4 m; network-input paragraph; heading "C. Sensor Prediction"; ŷ_t, (x_t, y_t, x_{t+k}), k ∈ [0, ..., N_T]; refs [76], [77], [78]; 4096 neurons, SiLU, 20% dropout, 3 stages, 16 channels; Table V all 4 × 7 cells and caption with max(d̂/d, d/d̂) < 1.25^i; h^η; heading "D. Simulation Experiments"; eq. (32) with the 17-entry diagonal of Q and R = 0.01·diag([1 1 1 1]); stage constraint, 7.0 m/s, r_z ∈ [1.25, 3.25], 0.6 m.
- **p. 13**: Fig. 11 crop and caption; 0.1 sec, N_y = 10, 11 timesteps, Δt = 0.1, H = 0.1, L = 1, M = 1024, δ = 0.05, γ = 2, ε_c = 0.1; environment ranges [10, 30], [20, 30], [4, 5], 0-6 traps, ±π/2, radii 0.2-0.4; Table VI all cells (718.14 as printed); eq. (33) all five lines; v_G = 6 m/s; 0.1 m voxels; 6 m/s and 3 m/s; 1 sec; eq. (34) all lines (Q with 10 10 10, Q_v = diag([1 1 1])).
- **p. 14**: Table VII: check-mark positions (row 1 Learned Prediction only, row 2 Warm-start only, row 3 both), 3% / 1001.2, 11% / 889.7, 90% / 513.3; Fig. 12 crop and caption; cost of 100; 100 environments; 90%; run-ins 4) and 5); [60]; "Section VII-B" as printed; Table VIII all cells; 1.25 m, 3.25 m, 0.6 m, 0.2 m; 46%, 76%; heading "E. Hardware Experiments"; 32-inch, D450, D4 board, Arduino Uno Q, 50Hz, 180Hz, i9-13900H, RTX 4080, Futaba T6K.
- **p. 15**: Figs. 13-16 crops and captions (C^+_α in Fig. 15); Table IX all cells; 80 × 60, 10%, 40 × 30, 16 × 12; 80%, 40%; three discussion paragraphs.
- **p. 16**: heading "VIII. ANALYSIS"; eq. (35); c ≥ 0 assumption; heading "A. One-Step Feasible Descent"; Lemma VIII.1 statement (V: X ↦ R, weak continuity, g ≻ 0, B_δ(u*_t), conclusion); eqs. (36)-(38), β ∈ (0,1), g_β; end of proof with ∃δ > 0; Lemma VIII.2 statement (Π^c_ε, U^c, V^c_π, conclusion); eqs. (39)-(44); "γ_c < ∞"; Theorem VIII.1 both paragraphs (δ_min, U_{δ_min}, c_{δ_min}, ε < c_{δ_min}, u^c_t, ΔV < 0); proof with eqs. (45)-(46); heading "B. Multi-Step Feasible Descent".
- **p. 17**: multi-step policy definition; Definition VIII.1 (product limits i = t ... t+N_T-1, integration variables); Definition VIII.2 with eqs. (47)-(48) and the list L_N, ℓ, C_N, c; Theorem VIII.2 statement (Ξ^c_ε with i ∈ {t, ..., t+N_T}, compactness, continuity, ξ*, ξ_c, both conclusions); proof with eq. (49); closing paragraph; heading "C. Approximate Value Functions"; eqs. (50)-(52); heading "D. Simulation Experiment"; Dubins state, input, dynamics, Δt = 0.1, Σ_f; 7.5 m; 13 networks; 5 million timesteps; 100 trials; "lines 6-8 in Algo. 1"; Theorem VIII.2 reference.
- **p. 18**: heading "IX. CONCLUSION", both paragraphs; Fig. 17 and Fig. 18 crops and captions; heading "REFERENCES"; refs [1]-[29].
- **p. 19**: refs [30]-[76].
- **p. 20**: refs [77]-[78]; nothing else is printed on the page (no biographies), as the notes say.
- **References as a whole**: 78 entries, numbered 1-78 in order; all 78 identical to the PDF text layer after resolving 25 line-break hyphens, each of which the package resolved correctly (e.g. "Perception-aware", "Constraint-informed", "model-based", "fixed-wing", "Comput.-Assist." kept; "computationally", "Salakhutdinov", "Kumar" joined). Diacritics (Köhler, Müller, Allgöwer, Klaučo, Kalúz, Araújo, Ginés) and grouped page numbers (11 216–11 235, 14 265–14 271, 14 777–14 784) correct. Italic spans (venue or book title, "et al." in [66]; none in [10] and [75]) were compared by eye with the page images for all 78 entries and agree; the PDF carries no machine-readable italic flag, so this part is visual only.
- **Conversion notes** (for this range): page-number offset, absence of biographies, duplicate subsection headings, two-column "Approach" header, check marks in Table VII, bibliography rebuilt from the PDF: all true. Only the bold-marking note is incomplete (finding 3).

## Question answered from the package only

Question: Under what condition on ε does Theorem VIII.1 guarantee a feasible input that still descends the value function, how are the quantities in that condition defined, and what is the corresponding empirical evidence?

Answer from `paper.md`, section "VIII. ANALYSIS" > "A. One-Step Feasible Descent" (Theorem VIII.1 and proof) and "D. Simulation Experiment":
- Let δ_min = min over π ∈ Π^c_ε of δ_π > 0, where δ_π is the neighbourhood radius of Lemma VIII.1 for V_π. On the compact set U_{δ_min} = {u_t ∈ U | dist(u_t, U^c) ≥ δ_min} (inputs at least δ_min away from the feasible set U^c(x_t) = {u_t | c(x_t, u_t) = 0}) the Extreme Value Theorem gives c_{δ_min} = min over U_{δ_min} of c(x_t, u_t) > 0.
- Condition: under the assumptions of Lemmas VIII.1 and VIII.2, if Π^c_ε ≠ ∅ with ε < c_{δ_min}, then there is a feasible input u^c_t ∈ U^c(x_t) in the neighbourhood of u*_t = π*_{γ_c}(x_t) with ΔV(x_t, u^c_t) < 0.
- Argument: Lemma VIII.2 gives γ_c large enough that V^c_{π*_{γ_c}}(x_t) < ε < c_{δ_min}; if the optimal input stayed at distance ≥ δ_min from U^c along γ^k_c → ∞ (45), then V^c ≥ c(x_t, π*(x_t)) ≥ c_{δ_min} (46), a contradiction; so the optimal input is within δ_min of U^c and Lemma VIII.1 supplies the descent.
- Evidence: a stochastic Dubins car (Euler integration, Δt = 0.1 sec, Σ_f = [0.01 0.01 0.01]^T), goal surrounded by a hexagonal lattice of obstacles, start 7.5 m from the goal, 13 actor-critic networks with increasing γ_c each trained for 5 million timesteps, 100 trials per γ_c; AC-PAC-NMPC navigates successfully at smaller γ_c than the actor alone (Fig. 18), and the actor infeasibility check (lines 6-8 of Algorithm 1) markedly improves safety.

Check against the PDF: p. 16 right column (Theorem VIII.1, proof, eqs. (45)-(46)) and p. 17 right column (VIII-D) agree with every element of the answer; Fig. 18 on p. 18 shows the green AC-PAC-NMPC collision curve at about zero for all penalties and the success curves rising at smaller penalties than the actor's. Correct.
