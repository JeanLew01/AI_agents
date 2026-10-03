# Independent verifier report: pac-nmpc-value-function-paper-s1, PDF pages 1-9

Status: COMPLETE (2026-10-02). Nothing in the package or in the review plans was changed.

- Paper: "Robust Perception-Based Navigation using PAC-NMPC with a Learned Value Function", Polevoy, Gonzales, Kobilarov, Moore (arXiv:2309.13171v3)
- Package (PKG): `/home/jixia/AI_agents/paper2agent/NMPC/staging/pac-nmpc-value-function-paper-s1`
- Document (DOC): `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/pac-nmpc-value-function-paper/documents/s001-pac-nmpc-value-function`
- Ground truth: `DOC/source.pdf` (9 pages). Crops, native figure images and scripts are in
  `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/_scratch/verify-pacvf/`.
- I did not read the reviewers' report (`review-pages-0001-0009.md`) and did not use the TeX source.

## Result in one paragraph

The paper text, all seven numbered equations, all inline mathematics, all ten figures and captions and all 55
references agree with the PDF. I found **no discrepancy in `references/paper.md` body text or in the assets**.
Every bar-chart percentage listed in the conversion notes is correct. The only real defect is in
`references/index.md`, which assigns equation numbers to the wrong sections (1 error), plus a few minor
index/cosmetic points (5 minors).

## Coverage (what was actually done)

All nine pages were checked in full; nothing was sampled except where stated.

| Check | Method | Extent |
| --- | --- | --- |
| Display equations (1)-(7) | 300-330 dpi crops of each equation, compared with the LaTeX symbol by symbol | all 11 display blocks (7 tagged + 4 untagged aligned blocks) |
| Inline mathematics | 300 dpi crops of every maths-bearing column region on pages 3, 4, 5, 7; 130 dpi page view for pages 2, 6, 8 | all 190 inline expressions read against the crops |
| LaTeX well-formedness | script: `$` parity per line, `{}` balance, `\left`/`\right`, `\begin`/`\end`, `\tag` inventory | whole file; no problem found |
| Prose | word-level diff of the PDF native text lines against the package text, case-sensitive, hyphen- and dash-sensitive, maths masked | all pages; zero prose differences |
| Line-end hyphenation | every one of the 56 line-end hyphens in the PDF compared with how the package joined the word | all; all correct |
| Numbers in prose | covered by the word diff, plus the reviewer tool `check` on pages 1-9 | all; only minus-glyph (U+2212 vs `-`) differences inside LaTeX |
| Headings and reading order | printed headings vs. `#` headings; column and page joins read | all 17 headings; all cross-column / cross-page sentences |
| Figures | all 10 package JPEGs opened; compared with PDF crops and with the native embedded images (`pdfimages`) | all |
| Bar-chart percentages (notes) | (a) labels read in the native embedded images (1063-1190 px wide, about 270-300 ppi, the highest resolution that exists in the PDF); (b) independent pixel measurement of every bar segment (row boundaries and segment colour) | every number for Figs. 2, 5, 8, 9, 10 |
| Captions | diffed against the PDF text | all 10 |
| References | automated token diff of all 55 entries (case-sensitive, incl. numbers, page ranges, URLs); italic spans in the PDF (font `ReguItal`) vs. `*...*` in the package; visual 230-260 dpi check of [15]-[17] and [44]-[55] | all 55 entries, 56 italic spans |
| Omissions | the diff lists every PDF line not found in the package | only the arXiv margin stamp (declared `omit`) and the page-2 title (declared `omit`, emitted once at the top) |
| `SKILL.md`, `index.md`, `supplement.md`, conversion notes | read once; index headings matched programmatically against `paper.md`; asset links resolved | whole files |

There are no tables, algorithms, theorems, definitions or footnotes with running text in this paper (the two
affiliation footnotes on page 2 are present).

## Findings

| # | Severity | PDF page | Item | Package says | PDF shows | Suggested fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | **error** (navigation metadata, three rows) | 4, 5 | `references/index.md`, rows "B. Actor Critic Reinforcement Learning", "B. Learned Value Function", "C. PAC-NMPC with Learned Value Function" (equations are items p0004-b010, -b012, -b014, -b017, p0005-b001, -b007) | III-B holds "equation (2)"; IV-B holds "equations (3)-(5)"; IV-C holds "equations (6)-(7)" | (1) is in III-A PAC-NMPC; (2), (3), (4) are in IV-A Problem Formulation; (5) is in IV-B; (6) is in IV-C; (7) is in V-A Experimental Setup. III-B has no numbered equation. `paper.md` itself has them in the right sections | Rewrite the "Look here for" cells: III-A "equation (1)"; III-B no equation number; IV-A "equations (2)-(4)"; IV-B "equation (5)"; IV-C "equation (6)"; V-A "equation (7)" |
| 2 | minor | 2, 5 | `references/index.md`, rows "I. INTRODUCTION" and "B. Cluttered Environments" | Fig. 1 is under I. INTRODUCTION; Figs. 2-4 are under V-B | In `paper.md` the Fig. 1 link and caption sit before the `## I. INTRODUCTION` heading (lines 13-15), and the Fig. 2 and Fig. 3 links and captions sit under `### A. Experimental Setup` (lines 138-144); only Fig. 4 is under V-B. This placement follows the PDF page layout and is fine; the index is what is off | Index: front matter "Fig. 1"; V-A "Figs. 2-3 (links)"; V-B "discusses Figs. 2-4, link of Fig. 4" |
| 3 | minor | 3, 4, 5, 6 | `references/index.md`, descriptions | V-B "rally-car results"; II "Stochastic NMPC, learned terminal costs/value functions, RL for navigation"; IV-A "sensing and dynamics assumptions"; V-A "vehicles, sensing, baselines, compute" | V-B reports simulation trials with the stochastic bicycle model (the rally car is the hardware of Section VI). II covers learned waypoints for MPC, learned value functions as terminal cost, and safe RL (CMDP, safety critics, CBF, reachability, robust MPC). IV-A has the LiDAR model, cost (2), constraints (3) and occupied points (4), no dynamics assumptions. V-A also holds the PAC-NMPC and MPPI parameters, Monte Carlo dropout and the RL training setup | Reword the four cells accordingly |
| 4 | minor | 5-8 | `references/index.md` | No row points to `## Conversion notes` | The conversion notes hold the only text copy of the main quantitative results (bar-chart percentages of Figs. 2, 5, 8, 9, 10) | Add an index row "Conversion notes: source details, authors' typos, bar-chart values of Figs. 2, 5, 8, 9, 10" |
| 5 | minor (cosmetic) | 2, 7 | p0002-b002 (abstract), p0007-b014 (VI, first paragraph) | "1/10th scale" | "1/10" followed by a superscript "th" | Optional: `1/10$^{\text{th}}$`; the meaning is unchanged |
| 6 | minor (cosmetic) | 5-8 | `assets/figure/figure-2.jpg`, `-5`, `-8`, `-9`, `-10` | 618-623 px wide JPEGs (about 180 dpi) | The embedded images are 1063-1190 px wide. All percentage labels are still legible in the package JPEGs, including the tight overlapping pairs ("3%"/"1%" in Fig. 2, "2%"/"1%" in Fig. 5) | Optional: render the bar charts at 300 dpi |

Not counted as findings (information for the coordinator):

- **Clipping that is in the PDF itself.** Four figures are slightly clipped by the authors' own image trim, and
  the package JPEGs reproduce exactly what the PDF shows, no more and no less: Fig. 4 (right edge of the
  x-tick "50"), Fig. 6 (lower half of the x-axis label "X (m)"), Fig. 8 (left edge of the y-axis label
  "Percent (%)"), Fig. 10 (the final "h" of "Function Mismatch"). No caption or body text is inside any crop.
  A sentence in the conversion notes would prevent a later reader from blaming the conversion.
- **Two statements in the conversion notes cannot be verified from the PDF**: the venue line (ACC 2025,
  pp. 414-421, DOI 10.23919/ACC63710.2025.11107521; the note itself marks it as external metadata) and
  "The arXiv source contains an appendix file that is not part of this PDF". I did not check either against
  an outside source. Nothing in the PDF contradicts them.
- The IEEE copyright paragraph of page 1 sits between the title and the author line in `paper.md`. This is a
  consequence of emitting the title once at the top and is harmless.

## Requested confirmations

### Equations (1)-(7), symbol by symbol

| Eq. | PDF page | Result |
| --- | --- | --- |
| (1) | 4 | Correct. Five printed lines; `\tag{1}` is on the first line (`J^+_alpha(nu) := J-hat_alpha(nu) + alpha d(nu) + Phi_alpha(delta),`), which carries the printed number. The other four lines are in the following aligned block: J-hat with 1/(alpha L M), sums i=0..L-1 and j=1..M, zeta(alpha l_ij); zeta(x) = log(1 + x + x^2/2) and l_ij = J(tau_ij) p(xi_ij|nu)/p(xi_ij|nu_i); d(nu) = 1/(2L) sum_{i=0}^{L-1} b_i^2 e^{D_2(...)} and Phi_alpha(delta) = 1/(alpha L M) log(1/delta); 0 <= J(tau_ij) <= b_i for all j = 0, ..., M. The unbalanced parenthesis in the exponent is reproduced exactly: four opening and three closing parentheses, `D_2(p(.|nu)||(p(.|nu_i))` |
| (2) | 4 | Correct: sum from i=0 to N_T-1 of {q(x_i,u_i)} + q_f(x_{N_T}), trailing comma |
| (3) | 4 | Correct. Four printed lines; `\tag{3}` is on the first line (g_b). g_o = not((dist(x_t, p_{o^j}) > r) for all j); c = g_b or g_o; C(tau) = c(x_0) or c(x_1) or ... or c(x_{N_T}) |
| (4) | 4 | Correct: p_{o^j} = p_t + [cos(theta_t + beta^j)  sin(theta_t + beta^j)]^T l_t^j |
| (5) | 4 | Correct: r(s_t, a_t) = -q(x_t, u_t) - gamma_r c(x_t), trailing comma |
| (6) | 5 | Correct. Three printed lines; `\tag{6}` is on the first line (g_V = V(x_{N_T}, l-hat_{N_T}) - V(x_0, l_0)). c_V = g_V < 0; C(tau) = c(x_0) or c(x_1) ... or c(x_{N_T}) or c_V(x_{N_T}), with the "or" before the dots missing as printed |
| (7) | 5 | Correct. Three printed lines; `\tag{7}` is on the last line (omega ~ N(.|0, Gamma).), which carries the printed number. The first two lines (x_{t+1} ~ p(.|x_t,u_t) := x_t + (f + omega) Delta t; f = [v cos(theta), v sin(theta), v tan(delta_s)/l, v-dot, delta_s-dot]^T) are in the preceding aligned block, so the printed order is kept |

### Bar-chart percentages in the conversion notes

Every value was confirmed twice: by reading the label in the native-resolution image and by measuring the
segment in pixels (in all five charts the 0-100 axis spans rows 408 to 103, i.e. 3.05 px per percent; the colour
of each segment identifies its legend class). All labels are legible; none had to be guessed.

| Figure | Bar | Notes say | Label read | Segment measured (px rows -> %) | Verdict |
| --- | --- | --- | --- | --- | --- |
| 2 | PAC-NMPC quadratic | 76 reached / 24 did not reach | 76 / 24 | blue 76.1, orange 23.9 | correct |
| 2 | PAC-NMPC naive A* | 89 / 4 did not reach / 7 obstacle | 89 / 4 / 7 | blue 89.2, orange 3.9, red 6.9 | correct |
| 2 | Actor policy | 90 / 3 did not reach / 1 velocity / 6 obstacle | 90 / 3 / 1 / 6 | blue 90.2, cyan 1.0, orange 3.0, red 5.9 | correct |
| 2 | MPPI learned VF | 70 / 7 did not reach / 23 obstacle | 70 / 7 / 23 | blue 70.2, orange 6.9, red 23.0 | correct |
| 2 | PAC-NMPC learned VF | 97 / 3 did not reach | 97 / 3 | blue 97.0, orange 3.0 | correct |
| 5 | PAC-NMPC quadratic | 47 / 53 did not reach | 47 / 53 | blue 47.2, orange 52.8 | correct |
| 5 | PAC-NMPC naive A* | 91 / 4 did not reach / 5 obstacle | 91 / 4 / 5 | blue 91.1, orange 3.9, red 4.9 | correct |
| 5 | Actor policy | 82 / 2 did not reach / 1 velocity / 15 obstacle | 82 / 2 / 1 / 15 | blue 82.0, cyan 1.3, orange 2.0, red 14.8 | correct |
| 5 | MPPI learned VF | 55 / 9 did not reach / 36 obstacle | 55 / 9 / 36 | blue 55.1, orange 8.9, red 36.1 | correct |
| 5 | PAC-NMPC learned VF | 93 / 7 did not reach | 93 / 7 | blue 93.1, orange 6.9 | correct |
| 8 | PAC-NMPC quadratic | 72 / 9 altitude / 19 obstacle | 72 / 9 / 19 | blue 72.1, orange 8.9, red 19.0 | correct |
| 8 | Actor policy | 92 / 3 altitude / 5 obstacle | 92 / 3 / 5 | blue 92.1, orange 3.0, red 4.9 | correct |
| 8 | PAC-NMPC learned VF | 96 / 4 obstacle | 96 / 4 | blue 96.1, red 3.9 | correct |
| 8 | PAC-NMPC learned bicycle VF | 98 / 2 obstacle | 98 / 2 | blue 98.0, red 2.0 | correct |
| 9 | PAC-NMPC quadratic | 54 / 20 altitude / 26 obstacle | 54 / 20 / 26 | blue 54.1, orange 20.0, red 25.9 | correct |
| 9 | Actor policy | 80 / 6 altitude / 14 obstacle | 80 / 6 / 14 | blue 80.0, orange 6.2, red 13.8 | correct |
| 9 | PAC-NMPC learned VF | 89 / 11 obstacle | 89 / 11 | blue 89.2, red 10.8 | correct |
| 9 | PAC-NMPC learned bicycle VF | 93 / 7 obstacle | 93 / 7 | blue 93.1, red 6.9 | correct |
| 10 | Actor policy | 85 / 15 obstacle | 85 / 15 | blue 85.2, red 14.8 | correct |
| 10 | PAC-NMPC learned VF | 95 / 5 did not reach | 95 / 5 | blue 95.1, orange 4.9 | correct |
| 10 | Actor policy mismatch | 70 / 30 obstacle | 70 / 30 | blue 70.2, red 29.8 | correct |
| 10 | PAC-NMPC learned VF mismatch | 80 / 20 did not reach | 80 / 20 | blue 80.0, orange 20.0 | correct |

The legend classes are also right: Figs. 2, 5 and 10 use "Reached Goal / Did Not Reach Goal / Velocity
Constraint Violation / Obstacle Constraint Violation"; Figs. 8 and 9 use "Reached Goal / Altitude Constraint
Violation / Obstacle Constraint Violation". The thin cyan (velocity) segment of the actor-policy bar exists in
Figs. 2 and 5 only.

### Authors' typos and the broken cross-reference

All of the following are printed in the PDF exactly as the package has them:

| Item | PDF page | Confirmed |
| --- | --- | --- |
| "(eq. III-A)" at the end of Section IV-C (a section number where an equation number should be) | 5 | yes, printed literally "(eq. III-A)" |
| Extra opening parenthesis in the Renyi-divergence exponent of (1) | 4 | yes |
| "for all j = 0, ..., M" in the last line of (1) although the sum runs over j = 1..M | 4 | yes |
| "arg min" in the definition of the optimal policy pi* (Section III-B) | 4 | yes |
| L used for the number of prior policies (III-A, V-A "L = 5", V-D "L = 1") and for a wheelbase (V-D "atan(L/v theta-dot)", VI "L = 0.5"), while V-A writes the wheelbase as "l = 0.33m" | 4, 5, 7 | yes |
| Subsection letters A, B, C repeated under Sections III, IV and V (V also has D) | 3-7 | yes |

Further authors' slips that are also reproduced as printed (the notes say "e.g.", so they are not required to
list them): "(e.g., [38], and backwards reachable sets" with the parenthesis never closed (page 3); "constrained
violation" (page 4); "we assign the the estimated" (page 4); the missing "or" before the dots in the last line of
(6) (page 5); "[-1., 1] m/s" for an acceleration (page 5); "N_t" instead of "N_T" in "v_max . N_t . Delta t"
(page 5); "Intel Core i-9-13900H" (page 6); "(Fig. 5)" without a full stop at the end of V-C (page 7);
"S. Michra" in reference [44] (page 9).

## Checked and found correct, by page

- **Page 1**: IEEE copyright notice complete; arXiv margin stamp omitted with a reason and quoted in the notes.
- **Page 2**: title (once, at the top); author line with affiliation superscripts 1,2 / 1,2 / 2 / 1,2; both
  affiliation footnotes with e-mail addresses; abstract complete; Fig. 1 JPEG complete (panels a, b, c) and
  caption; Introduction paragraphs 1-4 including the column break ("...true system dynamics, | which can be...")
  and the page break into page 3; citations [1]-[16].
- **Page 3**: end of Introduction; II. RELATED WORK (three paragraphs + closing sentence, citations [17]-[46]);
  III. BACKGROUND and A. PAC-NMPC; inline maths: p(x_{t+1}|x_t,u_t), x_t in R^{N_x}, u_t in R^{N_u},
  u_t = pi(x_t, xi), p(xi|nu), the TVLQR feedback policy, tau^d, the nominal dynamics, K_t in R^{N_u x N_x},
  xi = [u_0^{dT} u_1^{dT} ... u_{N_T-1}^{dT}]^T, N(xi|mu, Sigma), nu := [mu^T diag(Sigma)^T]^T,
  tau = {x_0,u_0,x_1,u_1...,u_{N_T-1},x_{N_T}}, J(tau) >= 0, C(tau) in {0,1}, the arg min / min objective.
- **Page 4**: equation (1) and its explanation; both PAC guarantees P(E[.] <= bound) >= 1 - delta; delta = 0.05
  and 95%; III-B (R_t^{gamma_d}, gamma_d in [0,1), Q^pi, V^pi, pi^phi, Q^psi, pi*, Bellman relation); IV. APPROACH,
  A. Problem Formulation (LiDAR ranges l_t and bearings beta with upper index N_l, l_max); equations (2)-(4);
  B. Learned Value Function with (5), citations [48]-[52], V^{psi phi}; C. first paragraph (l-hat, beta-hat,
  atan2, arg min over k).
- **Page 5**: q_f = -V^{psi phi}; equation (6); the guarantee paragraph with "(eq. III-A)"; V. A. Experimental
  Setup; equation (7); state and control vectors, l = 0.33m, Gamma = diag([4e-4, 4e-4, 1.1e-2, 1e-1, 5.6e-3]),
  limits [-1., 1] m/s, [-1, 1] rad/s, [-0.4, 0.4] rad; Q = diag([1e-2 1e-2 0 0 0]), v in [-1, 3] m/s;
  Q_f = diag([1 1 0 0 0]); four baselines; 12 time steps, Delta t = 0.1 s, H = 0.2 s, 50 Hz, L = 5, M = 1024,
  delta = 0.05, gamma = 2 / 4, gamma_t = 0.35, Sigma_epsilon = 0.01; Fig. 2 and Fig. 3 JPEGs and captions.
- **Page 6**: 64 beam 360 degree LiDAR, gamma_r = 1000, CPU/GPU names; B. Cluttered Environments (100
  environments, 1024 trajectories, 5%, 0.34%, 65.49%, 1.45%); cross-column join "com|putation";
  C. Concave Trap Environments (0 to 20 obstacles, 2.5 to 5.0 m, +/- pi/2); Figs. 4, 5, 6 JPEGs and captions.
- **Page 7**: D. Fixed-wing UAV: state x = [r, q, delta, v, omega, p] with q in blackboard Q, u = [u_a,u_e,u_r,u_p];
  noise means [0.10, -0.90, -0.89] m/s^2 and [1.18, -0.16, 1.71] rad/s^2, variances diag([1.71, 1.63, 1.41]) and
  diag([10.05, 5.57, 15.23]); cost weights diag([0.01,0.01,0.01]), diag([0.1,0.1,0.1]); altitude [0,5] m, speed
  <= 8 m/s, roll rate [-10,10] rad/s; L = 1, gamma = 3, 20 obstacles, 3 million steps, 4.5 hours;
  q_f = 10.0 . q; v_min = 2, v_max = 8; delta = atan(L/v theta-dot); diag([0.00,0.00,0.1]), diag([0.1,0.1,0.1]),
  diag([1,1,1]); shifted means [3.10, 2.10, 2.11] and [4.18, 2.84, 4.71]; VI. first two paragraphs (L = 0.5,
  20 environments, 8 obstacles, 8 m by 6 m); Figs. 7, 8, 9 JPEGs and captions.
- **Page 8**: rest of VI; Fig. 10 JPEG and caption; VII. DISCUSSION & CONCLUSION (two paragraphs);
  REFERENCES [1]-[17].
- **Page 9**: REFERENCES [18]-[55], including the entry [37] that continues across the column break; accented
  names (Bektaş, Allgöwer, Gjærum, Håkansson, Araújo); URLs with underscores ([16], [17], [53]).
- **Package files**: all 17 index headings exist exactly once in `paper.md`; all 10 figure links resolve;
  `supplement.md` correctly states that no supplementary material was supplied; the conversion notes contain no
  statement that the PDF contradicts.

## Technical question answered from the package only

**Question.** How does the method turn the learned value function into a terminal cost and a constraint for
PAC-NMPC, what do the returned bounds guarantee, and with which settings was PAC-NMPC run in the bicycle
simulations?

**Answer from the package** (`paper.md`, "C. PAC-NMPC with Learned Value Function" and "A. Experimental Setup"
under V; bar values from "Conversion notes"):

- The future LiDAR scan at the terminal state is predicted from the current scan: the range and bearing from
  the terminal position to each observed occupied point are computed and assigned to the closest sensor bearing.
- Terminal cost: q_f(x_{N_T}) = -V^{psi phi}(x_{N_T}, l-hat_{N_T}), with V^{psi phi}(x_t, l_t) = Q^psi(s_t, pi^phi(s_t))
  reconstructed from the TD3 critic and actor.
- Extra constraint, equation (6): g_V(x_{N_T}) = V(x_{N_T}, l-hat_{N_T}) - V(x_0, l_0), c_V = (g_V < 0), and
  C(tau) is the logical or of the state/obstacle constraints c(x_0) ... c(x_{N_T}) and c_V(x_{N_T}); a trajectory
  therefore counts as violating if the value function does not improve from the current to the terminal state.
- Guarantee: PAC-NMPC returns nu*, J^+_alpha(nu*) and C^+_alpha(nu*); the probability of violating the obstacle
  constraint or worsening the learned value function, given the current LiDAR measurement, is less than
  C^+_alpha(nu) with probability 1 - delta.
- Settings: 12-step horizon, Delta t = 0.1 s, replanning period H = 0.2 s, feedback policies interpolated to
  50 Hz, L = 5, M = 1024, delta = 0.05, trajectory costs normalised, gamma = 2 (cluttered) and gamma = 4 (concave
  traps); dropout masks of actor and critic are sampled with every trajectory.
- Outcome in the cluttered environments (Fig. 2, values from the notes): 97% reached the goal, 3% did not, no
  constraint violation.

**Check against the PDF.** Page 4 right column (IV-C first paragraph), page 5 left column (q_f, equation (6),
guarantee paragraph) and page 5 right column (settings paragraph) say exactly this; Fig. 2 shows 97% / 3% for
"PAC-NMPC Learned Value Function". The answer is correct and complete. Note that the index would have sent a
reader looking for "equation (7)" or "equations (3)-(4)" to the wrong section (finding 1); the text search
recommended in `SKILL.md` finds them regardless.
