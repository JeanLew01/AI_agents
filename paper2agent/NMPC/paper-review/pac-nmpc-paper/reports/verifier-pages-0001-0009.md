# Independent verifier report: PAC-NMPC, PDF pages 1-9

Status: COMPLETE.

- Package: `/home/jixia/AI_agents/paper2agent/NMPC/staging/pac-nmpc-paper-s2`
- Document: `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/pac-nmpc-paper/documents/s001-pac-nmpc`
- Ground truth: `source.pdf` (9 pages). The authors' TeX source and the reviewers' reports were not used.
- Scratch (page renders, crops, diff script and output): `/home/jixia/AI_agents/paper2agent/NMPC/paper-review/_scratch/verify-pac/`
- Nothing in the package or in the page plans was changed.

**Result: 0 errors, 3 minor findings, 4 observations that need no action.**

## Coverage

All nine PDF pages were checked in full; nothing was sampled except where stated.

| Check | What was done |
| --- | --- |
| Prose, all pages | Every page rendered at 200 dpi and read next to `paper.md`. In addition a word-level diff of the PDF's native text (`pdftotext`, line-break hyphens rejoined) against the package prose with maths masked (`diff.py`, `diff.out`): 283 opcodes, each one inspected. Every one is explained by masked maths, a running header, in-figure text, the transposed position of a float/footnote block, a correctly restored line-break hyphen, or a combining diacritic. No word, number or citation differs. |
| Display maths | Equations (1)-(12): each compared symbol by symbol with a 260-320 dpi crop. |
| Inline maths | Every inline expression on PDF pages 3-8 compared with the same crops (not only definitions and bounds). |
| Algorithms 1-6 | Each package JPEG opened; each transcription compared line by line with a 300-340 dpi crop of the PDF. |
| Figures 1-12 | Each package JPEG opened and compared with the page render; captions compared with the PDF. |
| References | All 37 entries: token-identical to the PDF's native text in the diff (case-sensitive); the 14 line-break hyphenations (entries 1, 6, 7, 15, 17, 19, 20, 22, 23, 24, 25, 29, 30, 32: compound hyphens kept in "Perception-aware", "Tube-based", "Robust-rrt", "locally-optimal", the others rejoined), the diacritics in [18], [20], [35], and page ranges/years of entries 1, 3, 4, 7, 9, 10, 13, 14, 16, 19, 22, 23, 25, 28, 31, 34, 35, 37 also read from the page image. |
| LaTeX health | Script check of every maths segment: `$` parity per line, brace balance, `\left`/`\right` and `\begin`/`\end` pairing, `\tag` sequence 1-12. Only imbalance is the parenthesis in Eq. (6), which is as printed. |
| Extraction damage | Searched for `<sup>`, `<sub>`, `(cid:`, U+FFFD, ligature glyphs, split decimals, stray `_`/`****`, duplicated paragraphs: none. |
| SKILL.md, index.md, supplement.md, conversion notes | Read once; all 17 index headings exist verbatim in `paper.md`; each claim in the notes compared with the PDF. |

Tables: the paper has none, so there is no CSV to check.

## Findings

| # | Severity | PDF page | Item id | Package says | PDF shows | Suggested fix |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | minor | 3-4 | `references/index.md`, row "B. PAC Bounds for Stochastic Policy Search" | "... its assumptions and Renyi-divergence term, equations (4)-(7)" | Section III-B contains Eqs. (2)-(9): the bound itself is Eq. (2), the importance-weighted mean Eq. (3), robust estimate (4)-(5), divergence term and cost range (6)-(7), concentration term (8), the optimisation problem (9). A reader told "(4)-(7)" may not look there for the bound (2), for Phi (8) or for the weighted cost/constraint problem (9). | Change to "equations (2)-(9)". (Similarly the row for IV-B could say "equations (10)-(11)", and V-A holds Eq. (12); optional.) |
| 2 | minor | - | `references/index.md` "Assets"; `SKILL.md` | Lists `assets/supp_figs/`, `assets/table/`, `assets/supp_table/`; SKILL.md explains CSV/workbook handling and "supplementary information, figures and tables". | The package has only `assets/figure/` (12 figures and the six `algorithm-N.jpg` images). The paper has no tables and no supplement. Nowhere does the index say that the algorithm images live in `assets/figure/`. | Cosmetic template text. If the builder allows it, drop the three absent directories and add "algorithms (JPEG, `algorithm-N.jpg`)" to the `assets/figure/` line. |
| 3 | minor | 3-8 | `paper.md` conversion notes, last bullet | "Subsection letters A, B, C repeat under Sections III-VI." | Only Section IV has a subsection C. Sections III, V and VI have A and B only. | Reword: "Subsection letters restart in each of Sections III-VI (A-B, A-C, A-B, A-B)". |

No finding changes a symbol, a number, a statement or omits content.

### Observations (no action needed)

- Run-in headings "1) Hardware:", "2) Setup:", "3) Results:" (PDF pages 7-8) are printed in italics; the package sets them in bold. Text and numbering are as printed.
- Eq. (12) is printed as three centred lines with one number; the package uses `aligned` with alignment at the relation symbols. Content identical.
- Several lines carry more than one `^*` outside code spans (for example Algorithm 2 line 8, Algorithm 5 lines 4, 10, 13, and the paragraph on PDF page 6 with the 95% statement). A Markdown renderer that does not protect `$...$` could pair the asterisks as emphasis. This is the collection-wide convention and is harmless for text reading and for maths-aware renderers.
- Author affiliation superscripts are written `[^1][^2]` with the notes as "Footnote 1: ..." paragraphs rather than Markdown footnote definitions. This is the convention used by the other packages of the collection (checked in the sibling staging packages), and the page-2 title heading is omitted from the page text as stated in the assignment.

## Checked and found correct

**PDF page 1 (cover sheet).** Copyright notice and DOI 10.1109/LRA.2023.3315209 verbatim; arXiv stamp omitted as the notes say.

**PDF page 2.** Authors and affiliation markers (1,2 / 2 / 1,2); abstract; index terms; Section I both columns, including the paragraph that continues under Fig. 1 ("...[7]; in" + "SNMPC, uncertainty distributions..."); the three contributions; the footnote block (manuscript dates May 7 / August 1 / August 24, 2023; editor Clement Gosselin; funding; both affiliations with the three e-mail addresses; DOI line); Fig. 1 image (four panels a-d, no caption inside) and caption ("costs/constraint" correctly rejoined from the line break); start of Section II.

**PDF page 3.** Section II (citation groups [6],[12],[13]; [14]; [15]; [16],[17]; [7],[18],[19]; [20]; [21],[22]; [23],[24]; [25]; [8],[26]; [27]; [9],[28]; [29]; [30]; [31]; [11]; [10]; [32]; [33]); Section III lead-in; III-A inline maths (state/control dimensions, policy with subscript t then without, joint distribution Eq. (1), trajectory density with product limit T, trajectory sequence ending in x_{N_T+1}, the ISPO objective, the regularised update with alpha D(nu, nu-hat*_i), "alpha > 0 is hand-tuned weight"); Algorithm 1 image and all 8 lines (line 7 without a semicolon, as printed); III-B first paragraphs with the italic "an upper confidence bound"; Eq. (2); the sentence "[10] proves that J^+_alpha(nu) bounds the expected cost J(nu) with a probability of 1 - delta"; Eq. (3) with nu_0 in both the sampling distribution and the denominator.

**PDF page 4.** Likelihood-ratio sentence; Catoni estimate E[X] ~ (1/(alpha M)) sum_{i=0}^{M} psi(alpha X_i) with "for some and alpha > 0"; psi(x) = log(1 + x + x^2/2); L priors nu_0..nu_{L-1}, samples indexed i0..iM; Eq. (4) (prefactor 1/(alpha L M), i = 0..L-1, j = 1..M); Eq. (5) (denominator nu_i); Eq. (6) (prefactor 1/(2L), b_i squared, exponent D_2 with the unbalanced parenthesis exactly as printed); Eq. (7) (0 <= J(tau_ij) <= b_i, j = 0..M); Eq. (8) ((1/(alpha L M)) log(1/delta), with the full stop); "It tightens the bound as the number of samples increases and as the bound confidence, 1 - delta, decreases"; constraint-violation probability C(nu) = P(g(tau) > 0) = E[indicator] and "C^+_alpha(nu) which upper bounds C(nu) with probability 1 - delta"; gamma > 0; Eq. (9) (nu_{i+1} = nu* = argmin_nu min_{alpha>0}); L-BFGS-B [36] and self-normalised importance weights [11]; Section IV lead-in; IV-A (open-loop policy, xi as stacked zeta_t, Gaussian surrogate, nu = [mu^T, diag(Sigma)^T]^T, eta_t, dimensions N_u N_T); Algorithm 2 image and 8 lines (nu_i without hat in line 4, hat in lines 1, 6, 8); Algorithm 3 image and 4 lines; "(Eq. 4) and Renyi divergences (Eq. 7)"; stochastic cost remark; IV-B opening with u_t = K_t(x_t^d - x_t) + u_t^d, kappa, K_t in R^{N_u x N_x}.

**PDF page 5.** xi in R^{2(N_x N_u + N_x + N_u) N_T}; "mulitvariate" and "we the compute" kept as printed; Eq. (10); tau^d definition; Eq. (11) with bold f; two-stage sampling paragraph; TVLQR [37] paragraph; Algorithm 4 image and 10 lines (inputs without transposes, loop index k in line 3, sign (x_t - x_t^d) in line 8); IV-C (bold x_0, trim by H/Delta t, Trim(kappa) = {K_{H/Delta t}, ..., K_{N_T}}, maximum likelihood estimate = mu); Algorithm 5 image and 14 lines; warm-start paragraph with eta_min; Algorithm 6 image and 10 lines (subscripts N_T - H/Delta t in lines 2, 4, 7; T - H/Delta t in line 9); Section V-A opening (l = 0.33, Gamma = diag([0.001, 0.001, 0.1, 0.2, 0.001])); Eq. (12).

**PDF page 6.** 20 timesteps, Delta t = 0.1 s; x_I, x_G; limits (-0.4, 0.4) rad, (-1.0, 1.0) rad/sec, (-1.0, 1.0) m/s^2; Q_f = diag([2.0, 2.0, 0.0, 0.0, 0.0]); obstacles (1.0, 0.75) and (2.0, -0.75); L = 5, M = 1024, delta = 0.05, gamma = 10; i9-9880H / RTX 2070; 500 iterations; the guarantee sentence (p(xi | nu*) without hat, bounds at nu-hat*, "95% chance"); line 3 of Alg. 3 / line 9 of Alg. 4 replacement; 15.9 ms / 18.5 ms; Fig. 2a,b, 2e-h, Fig 3; RA-MPPI parameters Sigma_epsilon = 0.01, M = 1024, N = 300, eta = 0, alpha = 0.3, A = 10, B = 1, C_u = 0.5 and 0.05; V-B opening (12 timesteps, 0.1 second, H = 0.2 sec). Figures 2, 3, 4: complete (all panel titles, axis labels, legends, annotations), no caption text inside; captions verbatim (Fig. 2 without a final full stop, as printed).

**PDF page 7.** Q_f = diag([1.0, 1.0, 0.1, 0.1, 0.0]); L = 5, M = 1024, delta = 0.05, gamma = 10; 10 Hz to 50 Hz; 54 iterations, 3.7ms; <= 5%; once out of 482; 99.8%; 95% (Fig 6d); 93.9% (Fig 6b); 64.7% (Fig 6a); VI-A hardware (Traxxas, Jetson Orin, VESC, OptiTrack); setup (cost printed without transpose, Q_f = diag([1.0, 1.0, 0.4, 0.1, 0.0]), L = 2); 3-component GMM from 2500 samples; 10 iterations, 20ms; <=10% (Fig. 9d); Fig. 9c sentence. Figures 5, 6, 7 complete; the right edge of Fig. 7 (panel dxdt[4]) is cut in the PDF itself, the package crop is faithful. Captions verbatim.

**PDF page 8.** "(Fig. 9a,b)"; VI-B hardware (24" Edge 540); setup (17-dimensional state, 4-dimensional control, x = [r, q, delta, v, omega, p], q in blackboard Q, u = [u_a, u_e, u_r, u_p], 3-component GMM from 2000 samples, 12 timesteps, Delta t = 0.1 sec, H = 0.2, cost with terminal term plus sum from t = 1 to N_T, L = 1, M = 1024, delta = 0.05, gamma = 10); Ryzen 7 5800x / RTX 3080; results (22 iterations, 8.5 ms, around 10%, Fig. 12); start of Section VII. Figures 8, 9, 10, 11 complete; captions verbatim.

**PDF page 9.** Rest of Section VII; Fig. 12 image and caption; REFERENCES [1]-[37] all present, in order, token-identical to the PDF.

**Conversion notes: each listed authors' inconsistency confirmed against the PDF as printed and as reproduced in the package.**

| Note | PDF location | Confirmed |
| --- | --- | --- |
| "for some and alpha > 0" | page 4, left column, line 4 | yes |
| Unbalanced parenthesis in the exponent of Eq. (6) | page 4: `D_2(p(.|nu)||(p(.|nu_i))`, four opening and three closing | yes |
| j = 0..M in Eq. (7) and in the sample list versus j = 1..M in Eq. (4) | page 4 | yes |
| Product limit T in the trajectory density | page 3, right column | yes |
| (x_t - x_t^d) in Algorithms 4 and 6 versus (x_t^d - x_t) in Eq. (10) | page 5 (Alg. 4 line 8, Alg. 6 line 5, Eq. (10)); the inline policy on page 4 also uses (x_t^d - x_t) | yes |
| Loop index k in Algorithm 4 line 3 | page 5 | yes |
| Subscript T - H/Delta t in Algorithm 6 line 9 | page 5 | yes |
| "Renyi divergences (Eq. 7)" | page 4, right column | yes |

Other statements in the notes (source, arXiv stamp date, page mapping 1-8 = PDF 2-9, no tables, no appendix, algorithms as images with transcriptions, italics of venue titles not reproduced) are true. The statement that the mathematics was taken from the TeX source is a process claim I cannot test; I found no place where the package's mathematics differs from the PDF.

Further printed oddities that are reproduced correctly but not listed in the notes (no action required): sum over i = 0..M with prefactor 1/(alpha M) in the Catoni estimate; missing transpose in the rally-car cost on page 7; Algorithm 4 inputs without transposes while Algorithm 3 has them; "polices", "mulitvariate", "we the compute".

## Technical question answered from the package only

**Question.** What exactly does PAC-NMPC minimise at each planning interval, with what confidence does the returned bound hold, and what settings were used on the rally car?

**Answer from the package** (`paper.md`, "B. PAC Bounds for Stochastic Policy Search", "C. PAC-NMPC", "A. Rally Car").
It solves nu* = argmin_nu min_{alpha>0} ( J^+_alpha(nu) + gamma C^+_alpha(nu) ) with L-BFGS-B on a GPU (Eq. (9)), where the cost bound is J^+_alpha(nu) = J-hat_alpha(nu) + alpha d(nu) + Phi_alpha(delta) (Eq. (2)), with
- robust estimate J-hat_alpha(nu) = (1/(alpha L M)) sum_{i=0}^{L-1} sum_{j=1}^{M} psi(alpha l_ij), l_ij = J(tau_ij) p(xi_ij | nu) / p(xi_ij | nu_i), psi(x) = log(1 + x + x^2/2) (Eqs. (4)-(5));
- divergence term d(nu) = (1/(2L)) sum_{i=0}^{L-1} b_i^2 exp(D_2(p(.|nu) || p(.|nu_i))), D_2 the Renyi divergence and 0 <= J(tau_ij) <= b_i (Eqs. (6)-(7));
- concentration term Phi_alpha(delta) = (1/(alpha L M)) log(1/delta) (Eq. (8)).

J^+_alpha bounds the expected cost with probability 1 - delta, and C^+_alpha, built the same way from the indicator of g(tau) > 0, bounds the probability of constraint violation with probability 1 - delta. On the rally car: L = 2, M = 1024, delta = 0.05 (95% confidence), gamma = 10, 12 timesteps with Delta t = 0.1 s, replanning period H = 0.2 s, Q_f = diag([1.0, 1.0, 0.4, 0.1, 0.0]); about 10 optimisation iterations per interval at roughly 20 ms each; bounds <= 10% collision probability. With these values Phi_alpha = ln(20)/(2048 alpha) = 1.46e-3/alpha (my arithmetic, not in the paper).

**Check against the PDF.** Eqs. (2), (4)-(9) and the two "probability 1 - delta" sentences: PDF pages 3-4, identical. Rally-car settings and results: PDF page 7, right column, identical (L = 2, M = 1024, delta = 0.05, gamma = 10; "average of 10 iterations ... approximately 20ms per iteration"; "PAC bounds <=10%"). The answer is supported by the PDF.
