# Independent verifier report: whole-body-mppi-paper, pages 1-7

Paper: "Real-Time Whole-Body Control of Legged Robots with Model-Predictive Path Integral Control", arXiv:2409.10469v1 (7 pages).
Verifier: fresh independent verifier (brief: paper-review/_tools/VERIFIER_BRIEF.md). Status: COMPLETE.

**Path note.** The assignment gave PKG = `NMPC/staging/whole-body-mppi-paper-s1`, which does not exist. The package verified is
`/home/jixia/AI_agents/paper2agent/NMPC/paper-review/staging/whole-body-mppi-paper-s1` (built 2026-10-12 12:01). Ground truth:
`DOC/source.pdf`. Its pdftotext output is identical to that of `papers/whole-body-mppi.pdf` (= `originals/`, sha256 1587588e...). The
review copy is re-saved and has a different hash.

## Summary
- **Errors: 0. Minors: 3** (all in navigation/notes metadata, none in paper text, maths, numbers, tables or references).
- The paper text matches the PDF word for word on all 7 pages (scripted check, below). Equations (1)-(4), Algorithm 1, Table I and all
  32 references are correct. All 8 JPEGs are complete and contain no caption or body text.

## Coverage (all pages 1-7, no sampling)
1. Full text, scripted at word level: I took the native PDF text lines of pages 1-7 (`p2s_tools lines`), removed the arXiv margin
   stamp, joined line-end hyphens and aligned the result with `paper.md` with difflib. Display maths, asset links and markdown markers
   were stripped first. I ran the comparison twice: once with quotes and dashes normalised, once with the raw characters.
2. Line-end hyphens: I listed all 66 joins and checked the form the package uses for each.
3. Display equations (1), (2), (4) and (3) against 260-dpi crops. Inline maths in each paragraph checked against crops of pp. 2, 4, 5 and 6.
4. Algorithm 1 against a 240-dpi crop, line by line, and its JPEG.
5. Table I: every CSV cell, the markdown table and the caption, against a 220-dpi crop.
6. Figures 1-7 and algorithm-1.jpg opened. I compared each with its page preview and with the native text labels the PDF holds for the
   vector figures 2, 6 and 7.
7. References [1]-[32]: text and punctuation of all 32 entries checked by the scripted comparison (raw dashes and quotes too). Italics
   checked visually for all 32 against 230-dpi crops of p. 7.
8. Read SKILL.md, index.md, supplement.md and the conversion notes. I checked each claim in the notes, matched every index heading
   against paper.md exactly, checked LaTeX balance ($ parity, braces, \left/\right) and searched for leftover markup.

## Findings

| id | severity | PDF page | item id | package says | PDF shows | suggested fix |
|---|---|---|---|---|---|---|
| V1 | minor | 2 | navigation meta (`_coord/meta/whole-body-mppi-paper.json`), index row "II. BACKGROUND AND RELATED WORK" | index.md lists "Fig. 2 system diagram (...)" under section II | Fig. 2 is printed at the top of p. 2, before the II heading. paper.md places it correctly at the end of section I (paper.md lines 35-37, before `## II.` on line 39), so a reader who opens section II at its heading does not reach Fig. 2 | Move "Fig. 2 system diagram ..." to the I. INTRODUCTION row, or write "Fig. 2 (placed just before this heading)" |
| V2 | minor | 6 | navigation meta, index row "F. Comparisons to RL and MPC" | index.md: "Table I feature comparison and discussion" under IV-F | Table I is printed in column 1 above the F heading. paper.md places it correctly at the end of IV-E (lines 186-195, before `### F.` on line 197), so the table is not inside the F section | Write "Table I (placed just before this heading) and discussion", or list Table I in the E row as well |
| V3 | minor | 5 | conversion notes (meta `notes`), bullet "Authors' slips are kept as printed" | the note quotes the package form as `'$\lambda =\sim 0.1$'` | paper.md line 176 reads `$\lambda = \sim 0.1$` (with a space). It renders the same and the PDF prints "λ =∼ 0.1", so the claim holds, but a literal `rg -F` for the quoted string finds nothing | Quote it exactly: `'$\lambda = \sim 0.1$'` |

Observation, not counted: the generic "Assets" block of index.md mentions `assets/supp_figs/` and `assets/supp_table/`, which this package
does not contain. The same tool text appears in every delivered NMPC skill (those packages do have the empty folders), so I treat it as
build-tool boilerplate. It does no harm.

## Checked and found correct
- **Full text, pp. 1-7.** Every word of the title, author line, both affiliation footnotes, the IEEE notice, the abstract, the body, all
  figure captions, the Table I caption, the acknowledgments and references [1]-[32] matches the PDF. The only differences are:
  (a) maths markup; (b) floats moved to paragraph boundaries (Fig. 1 after the 2nd paragraph of I, Fig. 2 at the end of I, Fig. 3 and
  Algorithm 1 under II-B, Fig. 4 under IV-A, Fig. 5 at the end of IV-D, Fig. 6 after the IV-E intro, Fig. 7 after ablation 4,
  Table I before F), which is faithful to the printed order; (c) labels inside vector figures, which are in the JPEGs; (d) URLs broken
  across lines, rejoined correctly in refs [4], [15] and [21]; (e) '[19]–[21]', whose dash sits at a line end in the PDF (seen in the
  p. 2 preview). The raw-character pass shows that every en dash, em dash ('0.24 m tall — roughly'), curly quote and apostrophe is the
  printed character. Sentences that cross columns or pages (pp. 1→1, 2→3, 3→4, 4→4 after Fig. 4, 4→5, 5→5 after Fig. 6, 5→6) read
  continuously. Nothing is duplicated, and there are no `<sup>`, glyph soup, NBSP/thin-space or stray `**`/`_` artefacts.
- **Line-end hyphens.** Of the 66 joins, 20 are real compounds and keep their hyphen: real-time ×5, sampling-based ×2,
  general-purpose, full-body, loco-manipulation, task-specific, sim-to-real, whole-body, high-dimensional, per-core, body-velocity,
  cost-to-go, model-based, human-to-humanoid and the date 2024-09-12. The other 46 soft hyphens are removed. All correct.
- **Page 1.** Superscripts ¹/² on the author line, footnote texts and e-mail addresses verbatim ('John M. Dolan' in the author line,
  'John Dolan' in footnote 2, as printed), the abstract, the three contributions and the outline paragraph. Fig. 1: the JPEG is complete,
  with 3 headings, 6 panels and the time stamps t = 0/3/12 s.
- **Page 2.** Eq. (1) ω_n = exp(−(L_n − L_min)/λ) / Σ_{n=1}^{N} exp(−(L_n − L_min)/λ) and eq. (2) μ_t = Σ_{n=1}^{N} ω_n u_t are exact,
  with tags. Inline maths checked: u_t ∼ N(μ_t, Σ_t), μ_t, t, Σ_t, N, L_n, n-th, ω_n, λ. The italics *offline* and *without* are kept.
  Fig. 2: the JPEG is complete. All labels are inside it: MPPI, 100 Hz, u, t, joint targets, Unitree Go1, PD, 20 kHz, τ, encoders,
  500 Hz, IMU, encoders, state, EKF, 500 Hz, position, orientation, MoCap, 100 Hz, user specified goal, cost.
- **Page 3.** Fig. 3: the JPEG is complete, with 6 keyframe pairs and t = 0, 1, 2, 3, 4, 7 s. Algorithm 1: the JPEG is complete (top
  rule to bottom rule) with no body text inside. The transcription matches all 14 lines plus Require/Ensure, including 'L_n = 0' with
  the text '=', 'n = 1, …, N', 't = 0, 1, …', 'using u_n', 'u = μ_t[0]' and 'μ_t ← shifted(μ_t)'. The nesting levels (&emsp;) are
  correct. Section III heading and III-A/III-B text checked, including '30-50 parallel rollouts' and 'Intel Core-i9'.
- **Page 4.** Eq. (3): sum over t = 0..T, [(x_ref − x_t)^T Q (x_ref − x_t) + (u_ref(t) − u_t)^T R (u_ref(t) − u_t)], with one number
  for the two lines. Inline maths checked: x_t, u_t, t, x_ref, u_ref(t), u_ref, Q, R, T = 40. Numbers checked: 100 Hz / 500 Hz (MoCap,
  IMU, encoders, EKF), i9-12900KS, 64 GB, 100 Hz, 0.01 s, 0.4 s, 30 samples, 20 kHz, 0.24 m, 3.5 kg,
  0.36m×0.36m×0.36m, ℓ1-norm. Fig. 4: the JPEG is complete.
- **Page 5.** L_box = Q_box ‖x̄_box − x_box‖_1 and eq. (4) L_box push = L_walk + L_box are exact. Numbers checked: 1m, 1m, 0.75m, 0.3m,
  9 out of 10, 6 out of 10, ∼100 Hz, ∼150 Hz, ∼100 Hz, λ =∼ 0.1. Fig. 5: the JPEG is complete, with both panels, dashed goal circles
  and all trajectories. Fig. 6: the JPEG is complete, with the ×10^6 multiplier, y ticks 0-50, the 'Cost' label, the legend
  (Trotting / Box Climb) and the x categories Direct / Zeroth-Order / Linear / Cubic.
- **Page 6.** '40 − 50' is printed and the package has $40-50$; '(Fig 7)', ∼40 and ∼100 Hz checked. Fig. 7: the JPEG is complete, with
  all 4 panels, the ·10^6 multipliers, y ticks 1 and 1.5, the 'Cost' label, the MuJoCo/Gazebo legend, all x ticks and the four x-axis
  titles. Table I: the CSV header ',Offline Training,Whole-Body Contact,Gradient-Free' and the 9 cells (MPC No/No/No, RL Yes/Yes/Yes,
  MPPI (ours) No/Yes/Yes) are correct; the markdown table is identical; the caption 'COMPARISON OF FEATURES ACROSS MPC [8]–[11], [17],
  [18], RL [12]–[15], [19], [22], [23], AND MPPI' is correct. V, V-A, V-B and the acknowledgments checked.
- **Page 7.** References [1]-[32]: all present and in order. Authors, titles, venues, volumes, numbers, pages (including '13 285–13 292',
  '11 443–11 450', '11 272–11 279'), years, URLs and access dates match. Italics checked for every entry: [1] *Science*, [2] book title,
  [3]/[25]/[28] *arXiv preprint …*, [5]/[7]/[8]/[11]/[14]/[17]/[23]/[24]/[30]/[32] proceedings titles, [6], [9], [10], [12], [13],
  [15], [16], [18], [19], [22], [26], [31]; [4], [20], [21], [27] and [29] carry no italics, as printed.
- **Conversion notes, checked claim by claim.** arXiv id, [cs.RO], date 16 Sep 2024 and 7 pages are confirmed by the margin stamp and
  pdfinfo. 'Byte-identical to the arXiv PDF' and the code-repository remark are external and not verified. The IEEE notice is kept once
  (true). Equations (1)-(4) carry \tag and (3) is one two-line aligned block with one number (true). Algorithm 1 is kept as an image
  plus transcription with &emsp; (true). The listed authors' slips are each present in the PDF and kept in paper.md: 'modification
  better scale MPPI'; line 6 'using u_n'; eq. (2) has no sample index; eq. (1) reuses n; 'in Sec. IV-E' starts a sentence in lower
  case; 'hard experiments'; λ =∼ 0.1 (see V3 for the quoting); 'between the robot body'; '(Fig 7)'; '5) Number samples:'; 'can not
  see'. The note on Figs. 2/6/7 is true: their labels, ticks, legends and ×10^6 / ·10^6 multipliers are vector text found only in the
  crops, and Fig. 2 also embeds raster pictures. The Table I note is true: caption below the table, two-line headers joined with a
  space, empty first cell. The note on float placement and restarting subsection letters is true.
- **SKILL.md / index.md.** The front-matter name and description are correct. All 20 'Exact heading' entries of the paper table exist
  verbatim as headings in paper.md. 'Document beginning' is the supplement placeholder; supplement.md says that no materials were
  supplied, which is correct for this paper. All 9 linked assets exist, and the relative links `../assets/...` resolve from
  `references/`.

## Technical question answered from the package only
**Q:** What MPPI settings run on the Go1 hardware (update rate, time step, horizon, number of samples, low-level control), and how is the
box-pushing cost made up?

**Answer from the package** (paper.md §IV-A "Hardware Implementation" and §IV-D "Box Pushing"):
- The MPPI policy is updated at 100 Hz on an i9-12900KS workstation (64 GB, connected over Ethernet/ROS).
- The dynamics are discretised at 0.01 s and the planning horizon is 0.4 s (T = 40 timesteps); 30 samples are rolled out.
- MuJoCo uses its default contact parameters with the linearised friction cone.
- The joint targets are tracked by the Go1's onboard PD controller at 20 kHz.
- The box-pushing cost is L_box push = L_walk + L_box (eq. 4), with L_box = Q_box‖x̄_box − x_box‖_1 (an ℓ1 cost on box position only,
  orientation not penalised). L_walk is the quadratic state/control tracking cost of eq. (3).

**Check against the PDF:** p. 4 (column 1, lines 'We run MPPI ...' and 'we update the MPPI policy at 100 Hz, discretize the dynamics at
0.01 s, plan over a 0.4 s horizon (T = 40 timesteps), and roll out 30 samples') and p. 4 col. 2 ('... onboard low-level PD controller at
20 kHz'). Page 5, col. 1, eq. (4) and the L_box definition, and 'we do not penalize the orientation'. All of it is confirmed. The
default sample count also matches the dotted line at 30 in the 'Number of samples' panel of Fig. 7.
