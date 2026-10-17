# Independent verification: GPC (arXiv:2502.13406v3), pages 1-10

Verifier: a fresh, independent verifier. I did not use the reviewers' reports or the authors' TeX source; the PDF was the reference throughout.

- PKG (actual location): /home/jixia/AI_agents/paper2agent/NMPC/paper-review/staging/generative-predictive-control-paper-s1. The assignment first named NMPC/staging/generative-predictive-control-paper-s1, which does not exist. The coordinator confirmed the paper-review/staging path.
- DOC: /home/jixia/AI_agents/paper2agent/NMPC/paper-review/generative-predictive-control-paper/documents/s001-generative-predictive-control
- Scratch: /home/jixia/AI_agents/paper2agent/NMPC/paper-review/_scratch/generative-predictive-control-v1 (crops, pdftotext output, stdlib-only diff scripts)

Status: COMPLETE. 0 errors, 5 minors.

## Coverage (what was actually done)
All 10 pages were checked in full. Nothing was sampled except where stated.
- **Text:** I ran a whole-document word-level diff (Python stdlib difflib) of the paper.md prose, with maths stripped, against `pdftotext` of source.pdf. I inspected every non-equal block. Each one was explained by maths, float position or the small-caps heading split; none was a real text difference. A second, punctuation-aware diff (commas, periods, brackets, dashes, quotes) found no prose punctuation differences. A rerun that also counted the article "a" found no missing or extra words.
- **Mathematics:** I compared every display equation (1a)-(35), plus the unnumbered q_U definition, with 200-300 dpi crops (`p2s_tools.py crop`). The checks covered bars and tildes, bold **x**/**y**/**z**, the superscripts (i), (i,j), (j), (i,d), fractions, norms, limits, the cases in (8), the exponent 1/(r−1) in (9), trailing punctuation and tags. Inline maths was checked on the same crops for every paragraph on pages 2-5 and 9, and on page images for pages 6-7.
- **LaTeX health:** paper.md has 38 display blocks and 168 inline spans. Braces, `\left`/`\right` and `\begin`/`\end` are all balanced. Every line has an even number of `$`. The tags run 1a, 1b, 1c, 2 … 35 in order, with none missing or duplicated.
- **Proposition 1, the proof (17)-(22) and Remark 1:** checked word by word against crops.
- **Algorithm 1:** I compared all 20 lines plus Input/Output with 260-dpi crops and with assets/figure/algorithm-1.jpg.
- **Tables:** I checked every cell of table-1/2/3.csv and of the three Markdown tables against `pdftotext -layout`, the page images and a 300-dpi crop of Table I (including its bold cells).
- **Figures:** I opened every JPEG (figure-1, -2, -3a, -3b, -4, -5, algorithm-1) and compared each caption with the native text lines.
- **References [1]-[46]:** all present and in order. I compared **all 46** entries character by character (scripted string comparison of each entry plus manual review of every difference). The only differences were line-end hyphens in genuine compounds, Unicode composition (Stańczyk, Özgün Önol), "π0 :" spacing and a URL rejoined across a line break. All are correct in the package.
- **SKILL.md, index.md, supplement.md, conversion notes:** I checked every index heading against paper.md with exact `#`-line matching (18/18 found; "Document beginning" refers to supplement.md). I checked every claim in the conversion notes; see below.

## Findings
| id | severity | PDF page | item | package says | PDF shows | suggested fix |
|---|---|---|---|---|---|---|
| F1 | minor | - | references/index.md, "Assets" list | lists the folders `assets/supp_figs/` and `assets/supp_table/` | the package has no such folders (there is no supplement); only assets/figure and assets/table exist | drop the two bullets, or mark them "(none in this package)" |
| F2 | minor | 3 | p0003-b026 (end of proof of Prop. 1) | QED mark `∎` (filled) | hollow square `□` | optional: use `□` |
| F3 | minor | 6 | p0006-b010 (Table I, Markdown table in paper.md Sec. VI-C) | 103 and 139 plain | 103 (No model error / Average DR) and 139 (With model error / CVaR DR) printed **bold** | write `**103**` and `**139**` in the Markdown table. The notes correctly say the CSV cannot mark bold, but the Markdown table could. |
| F4 | minor | 7, 10 | references/index.md "Look here for" column | the VI-B row lists "Fig. 5 (training curves)"; the APPENDIX II row lists "Table II" | in paper.md, Fig. 5 sits under `### C. Risk-Aware Domain Randomization` (line 328), and Table II sits under `## APPENDIX III TRAINING DETAILS` (line 492). Both placements follow the printed positions (top of p7; p10). | either name the section that actually holds each float in the index (e.g. "Fig. 5 (placed under VI-C)", "Table II (placed under App. III)"), or move the floats. As it stands, a reader who reads only the VI-B or App. II section will not find them. |
| F5 | minor | 2 | p0002-b017 (Footnote 1) | the paragraph "Footnote 1: Some SPC methods …" sits between display (10) (p0002-b035) and "where $\theta$ are learnable parameters …" (p0002-b036), breaking that sentence in two | the footnote is at the foot of the left column; the sentence "…trained … on (10), where θ are learnable parameters (e.g., network weights) and (11)" runs on without a break | move p0002-b017 after p0002-b037 (eq. 11), or to the end of Sec. II-A procedure item 1). |

No errors were found. All maths symbols, numbers, statements, headings, captions, table cells, algorithm lines and references agree with the PDF.

## Conversion-notes claims checked
- "arXiv:2502.13406v3 [cs.RO], 5 Mar 2026, 10 pages, IEEE two-column": true (margin stamp, pdfinfo).
- "byte-identical to the arXiv PDF": **cannot be checked offline**. The input papers/generative-predictive-control.pdf (sha256 5e3d54…, recorded in plan.json and papers/SHA256SUMS) and DOC/source.pdf (sha256 04d6f1…, the "normalized_sha256" in plan.json) differ in bytes but give identical pdftotext output. This is not a finding, but the wording could say "the input file …" rather than claim identity with arXiv.
- "(27) and (34) are single blocks with one tag": true.
- Algorithm 1 slips kept as printed: all five are true and transcribed exactly:
  - line 9 conditions p_θ on Ū^{(j)}_{k−1};
  - line 11 has x^{i,j}_{k−1} without parentheses;
  - line 15 uses u^{(j)}_{k−1}, which is not defined in the algorithm;
  - line 19 gives L_GPC five arguments after θ, while (27) has four;
  - the ranges [1, N_S] and [N_S, N] overlap.
- Other authors' slips: all true and kept as printed:
  - "leverage it train" (p1);
  - Ũ_k in Sec. IV, confirmed with a tilde at 300 dpi (p3);
  - "as well highly dynamic tasks" (p5);
  - footnote 3 wording (p5);
  - L_GPC cited as (10) in App. I;
  - the extra ")" in (34): 3 opening and 4 closing parentheses printed, and the package reproduces exactly that;
  - semicolons in (35);
  - "monte-carlo";
  - "T-length" U with T+1 entries;
  - "et. al.", "NeurIps", [4] without a year, [34] without a venue.
- Table notes: true. The bold cells of Table I are 103 and 139 (300-dpi crop). Tables II/III have an empty first header cell and the two-line "Double Cart-Pole" header. N_E, N_S, N_P and δt are plain text. Learning rates are printed as 10^−3. The rules in Table III split its rows into exactly four blocks (Architecture–Train | Envs–Episode len. | Num. Params.–Epochs | Inference–Ctrl. Freq.).
- Fig. 3 split, footnote convention, joined appendix headings, float placement: true as described. F5 qualifies the footnote placement.
- "Mathematics … from the authors' TeX source": I did not use the TeX source. Independently, every equation in the package matches the PDF.

## Checked and found correct (by page)
- **p1:**
  - Title on one line, authors, abstract (word-identical), and Sec. I with run-ins 1)-3).
  - The right-column continuation "tasks are simply difficult…" joins correctly. The p1→p2 join "In particular, we propose GPC…" is continuous.
  - Fig. 1 caption is word-identical, including the URL.
  - figure-1.jpg is complete (both panels, the arrows "training data"/"samples", and the labels U*, Ū_k, Ū_{k−1}) and has no caption inside.
- **p2:**
  - Equations (1a)-(1c), (2), (3) with Ū and σ², (4), (5), (6), (7) with λ→0 under lim, (8) with cases and the final period, (9) with the exponent 1/(r−1), (10), and (11) with the squared norm and a period.
  - Inline: x_τ∈R^n, u_τ∈R^m, ℓ(·,·), φ(·), U=[u_0,…,u_T], g:R→R^+, λ>0, r→1, p_0(**x**)=N(0,I), t=0, t=1.
  - Footnote 1 text.
  - Headings A./B. and the run-in 1) Flow Matching.
- **p3:**
  - The expectation sentence (t∼U(0,1), x_0∼p_0, x_1∼p_1) and 2) Diffusion.
  - Equations (12) and (13), the Sec. III intro, (14), and (15) with Ũ∼N(U,σ²) and g(Ũ).
  - Proposition 1 statement and (16) with the 1/σ² prefactor.
  - The proof: the unnumbered q_U ≜ N(Ũ; U, σ²), (17)-(21) with 1/η and ∇_U log q_U, the fact (Ũ−U)/σ², "Bringing 1/σ² outside", and (22) with σ² in the denominator.
  - Equation (23), including the subscript Ū_{k−1} on ∇ and the " ." spacing.
  - Citations [5, Algorithm 1] and [25, Appendix A].
  - Sec. IV start, (24), (25).
- **p4:**
  - Remark 1 word by word, including y=h(x), p_θ(U | x) and h(x).
  - Data (Ū_k, x_k), (26), U_t∼N(0,I), (27) as one block with a comma, and footnote marker 2.
  - The bold sentence "directly training … not particularly effective".
  - The paragraph covering x_0^(j), 𝒳_0, N_E, N_S, line refs 8/9/19, x_k^(j), U_k^(j) (no bar, as printed), t∈U(0,1), U_0∼N(0,I), j=1,…,N_E, k=1,…,K.
  - "GPC benefits from parallelism" (lines 11/2/19, [36], [19]).
  - Sec. V 1) Warm-Starts: (28), α∈[0,1], α=1, α=0, Ū_{k−1}. Then 2) Deploying the Policy, with bold-italic GPC/GPC+, and the p4→p5 join.
  - Footnote 2 (Ū_k−Ū_{k−1}, Ū_{k−1}).
  - Algorithm 1: all lines identical, as listed above.
  - algorithm-1.jpg is complete (top and bottom rules, line numbers 1-20) with no surrounding text.
- **p5:**
  - Fig. 2 caption. figure-2.jpg is complete (7 panels) with no caption inside.
  - 3) Risk-Aware DR with [37], [38]; (29)-(32), including inf_{z∈R}, E_d, max(J^(i,d)−z,0)/(1−β) and β∈[0,1).
  - `hydrax` [24].
  - Sec. VI questions 1)-4), the summary paragraph, and the systems paragraph (bold-italic names, URL).
  - The MLP/CNN/FiLM [41] and hardware paragraph (RTX 4070, 12 GB, 64-bit/32-bit).
  - VI-A: the video URL (character-exact "mjL7CF877Ow"), 100 simulations, N = 128, the bold result sentence, [27, Eq. 2-4], 1 and 10 ms, 100-1000 Hz.
  - Footnote 3 and the p5→p6 join.
- **p6:**
  - Fig. 3 (a), (b) and the main caption; Fig. 4 caption (compared with native lines).
  - figure-3a.jpg and figure-3b.jpg each have 7 panels with titles, the y-label "Cost Per Step", tick labels and rotated x labels. figure-4.jpg has 4 panels with titles "No Warm Start"/"With Warm Start", Control/Tip Height and Time (s). None has caption text inside.
  - Table I: 6 cells, row and column labels, and the caption.
  - The push-T/20 min/hour paragraph and the warm-start paragraph (α = 0, α = 1, 1 and 2 seconds).
  - VI-B text with the bold sentence.
- **p7:**
  - Fig. 5 caption with J and L_GPC. figure-5.jpg is complete (21 panels; row labels Cost/Best %/Loss; x-label Iteration).
  - VI-C continuation (β = 0.25, 8 domains), 50 targets, 15 cm, 10 seconds, and the model-error paragraph.
  - VI-D (1 to 29 DoF, bold sentence).
  - VII: T in Problem 1, v_θ, ∇ log p(U | x), (2), N, *all*, [17], [42]–[44], [45], [46].
  - VIII and the p7→p8 join.
- **p8:** references [1]-[46], all present, in order, and character-checked.
- **p9:**
  - App. I: (33), [−1, 1], L_GPC (10), U*, Ū_k−Ū_{k−1}, Ū_k−U_0, U_0, (34) (single block, extra parenthesis as printed), γ > 0, γ = 2.0, w = 1, w → 0, and (35).
  - App. II: intro and the seven system paragraphs (1.5 m/s, Unitree G1, y = h(x)).
  - App. III: 128 rollouts, 64 + 64.
- **p10:** Table II (35 cells) and Table III (98 cells) in both the CSV and the Markdown table, and both captions. The CSVs use CRLF line ends, which is standard CSV.
- **SKILL.md / index.md / supplement.md:** the name and description match the printed title. Every index heading exists exactly once in paper.md. The equation and section pointers in the index are correct, apart from F1 and F4. supplement.md correctly states that no materials were supplied.

## Technical question answered from the package only
**Q:** For the luffing-crane domain-randomization study, how many parallel environments, Gaussian SPC samples and policy samples does GPC training use, and what CVaR level and number of domains were used? Which DR policy is fastest with and without model error?

**Answer (package):**
- Table 3 (`assets/table/table-3.csv`, Crane column): Envs. N_E = 512, SPC samp. N_S = 4, Policy samp. N_P = 2. Also 10 iterations, batch size 1024, 20 epochs and a 30 Hz control frequency.
- Sec. VI-C ("C. Risk-Aware Domain Randomization"): CVaR (32) with β = 0.25 over 8 randomized domains (joint damping, payload mass, payload inertia, actuator gains).
- Table 1: without model error, Average DR is fastest (103 s, vs 106 for No DR and 133 for CVaR DR). With model error, CVaR DR is fastest (139 s, vs 165 and 184).

**Check against the PDF:**
- Table III on p10, Crane column: 512 / 4 / 2 / 10 / 1024 / 20 / 30. Matches.
- p7 left column: "(β = 0.25). We use 8 randomized domains …". Matches.
- Table I on p6: 106 / 103 / 133 and 165 / 184 / 139, with 103 and 139 bold. Matches. The package's prose would not show the bold emphasis (F3), but the numbers are right.
