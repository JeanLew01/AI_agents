# Independent verification: DiffPF (arXiv:2507.15716v2), pages 1-8

- Package: `/home/jixia/AI_agents/paper2agent/ParticleFilter/staging/diffpf-paper-s1`
- Document: `/home/jixia/AI_agents/paper2agent/ParticleFilter/paper-review/diffpf-paper/documents/s001-diffpf`
- Scratch: `/home/jixia/AI_agents/paper2agent/ParticleFilter/paper-review/_scratch/verify-diffpf`
- Verifier: fresh, independent; the reviewers' reports and the TeX source were not used as reference. The PDF was the ground truth.

## Coverage (all 8 pages, no sampling)

| Check | How it was done | Pages |
| --- | --- | --- |
| Prose text | Word-level diff of the PDF text layer (`pdftotext`) against `paper.md` with math removed, done twice: once lowercase with punctuation stripped, once case-sensitive. Every remaining difference was looked at by hand. | 1-8 |
| Display equations (1)-(11) | Each one compared symbol by symbol with 230-300 dpi crops (`eq12.png`, `eq3.png`, `eq45.png`, `eq67.png`, `p4a.png`, `p4b.png`, `p5b.png`). | 3-5 |
| Inline maths | Compared with crops and previews: definitions of x_t, post(x_t), chi_t, chi-hat_t, f_dyn, g_obs, c_t, alpha, alpha-bar, sigma, beta, gamma, epsilon_theta (bold vs plain), x*_{t,k}, v*_t, a*_t, Sigma (bold in (11) text, plain in DiffPF(Sigma)/10Sigma), x in R^10, identity transition x-hat = x (not bold), 1e-4, 32x32 / 24x24 / 50x150, sigma = 20. | 2-7 |
| LaTeX validity | Script check of all 114 math segments: braces, `\{ \}`, `\left`/`\right` and `\begin`/`\end` all balanced; `\tag` on every display. | all |
| Tables I-VII | Every decimal in every CSV compared by script with the PDF native text inside the table bbox (24/5/66/36/10/36/48 decimals: all identical and in the same order). Integer labels (K=, N=) and row labels checked by eye. Markdown tables in `paper.md` are identical to the CSVs, checked cell by cell by script. Captions checked against the native text lines. | 5-7 |
| Prose numbers | Every percentage in the PDF and the package listed and compared (14 values, identical and in the same order). All other numbers were covered by the word diff. I also recomputed every percentage from the tables: all agree with the printed values (e.g. 62.2 = (3.62-1.37)/3.62; 90.3 = mean of 86.8/92.6/91.6; 25%/26% vs dEKF; 48%/43% vs DEnKF/alpha-MDF). | 1, 5-7 |
| Citations in text | Sequence of all 85 bracket citations/ranges in the body: identical. | 1-7 |
| Structure | All headings and their levels compared with the previews. Text that runs across columns or pages joins correctly ("elimi-/nates", "operating with / substantially fewer particles", "insufficient convergence due / to suboptimal training", "ten urban / driving sequences"). Floats sit at paragraph boundaries. No `<sup>`, glyph debris or stray markup. Running headers, page numbers and the arXiv stamp are rightly omitted. Page-1 footnotes are present. | 1-8 |
| Figures | All 7 JPEGs opened: complete (all panel labels (a)-(d), "Time Step 54/55/56", Fig. 2 particle-mean box). No caption text inside the crops. Captions match the PDF word for word. | 1, 3-7 |
| References | All 41 entries compared token by token, case-sensitive with punctuation, against the PDF text layer. The only differences are correct joins of words split at line ends (107–113, 6840–6851, attention-based). Italic venue spans checked by eye against crops of both columns (`r1.png`, `r2.png`). | 8 |
| SKILL.md, index.md, supplement.md, conversion notes | Every heading listed in the index exists exactly in `paper.md` (16/16). Each claim in the notes was checked against the PDF. | - |

## Findings

| Severity | PDF page | Item | Package says | PDF shows | Suggested fix |
| --- | --- | --- | --- | --- | --- |
| - | - | - | No errors found | - | - |
| - | - | - | No minors found | - | - |

Observations that need no repair:
- Conversion notes, first bullet: the claim that the GitHub repository "at commit 493081c contains only the global-localization experiment" cannot be checked from the PDF. It is not wrong as far as the PDF goes. It is a claim about outside material and should be kept only if the converter checked it.
- Fig. 1 uses different diffusion notation from the text (epsilon_theta(x_t^n, n, c_t), "N steps", "M particles" against k, K and N particles in Sec. III). This is how the authors printed it and is correctly left only in the image. A reader who needs the formulas should use (6)-(8).

## Checked and found correct, by page

- **p.1**: title, authors, three footnotes (dates, funding grant numbers T2EP20123-0037 and T2EP20224-0035, e-mails, DOI line), abstract (90.3%, "nearly 50%", italic *differentiable*/*diffusion*, URL), index terms. Introduction paragraphs 1-4, with the drop-cap "ESTIMATING" repaired. Fig. 1 crop and caption (author typo "particles samples" kept).
- **p.2**: end of the introduction, the 3 contribution bullets, II.A-C in full, the opening of III with post(x_t) := p(x_t | o_{1:t}, a_{1:t}) and chi_t := {x_t^(i)}.
- **p.3**: Fig. 2 crop and caption. (1) x-hat_t^(i) = f_dyn(x_{t-1}^(i), a_t). (2) f_t = g_obs(o_t). (3) c_t = **Fusion**(f_t, {x-hat_t^(i)}). (4) and (5), with the Dirac sum over i = 1..N and 1/N. (6) x_{t,K}^(i) ~ N(0, I). (7): first line has x_{t,k-1}^(i) on the left, 1/sqrt(alpha), x_{t.k}^(i) with a period exactly as printed, (1-alpha)/sqrt(1-alpha-bar), plain epsilon_theta(x_{t,k}^(i), k, c_t), and + sigma z; second line is := beta(x_{t,k}^(i) + gamma epsilon_theta(...)) + sigma z. Single tag (7), as printed.
- **p.4**: (8) x_t = (1/N) sum x_t^(i). (9) has the expectation subscripted x*_{t,0}, k, c_t, bold epsilon, and the squared norm. Experimental setup: 100 vs 10 particles, 3-layer U-Net, 10 diffusion steps, RTX 4080 / i7-14700KF, AdamW 1e-4, cosine schedule, 1000 epochs, 4 warmup epochs, batch sizes 50/100. Fig. 3. Disk-tracking data (500/50 sequences, 50 frames, 128×128, 25 distractors, radius 7). (10) x-hat_t^(i) = x_{t-1}^(i) + v*_t.
- **p.5**: Tables I and II (all cells). Ablation bullets with bold variant names. Comparison paragraph (62.2%, 224.1 MB, 73.8%). Global localization overview. Fig. 4. Data paragraph (900/100 sequences, 100 steps). (11): all three rows, cos/sin signs (+ v sin in row 1, − v cos in row 2), theta_t without (i) in row 3 as printed, + omega_t. Sigma = diag(10^2, 10^2, 0.1^2).
- **p.6**: Tables III-V (all cells, row order PFNet before PFRNN as printed). 86.8/92.6/91.6%, 95.5/96.4/96.3%, 10Sigma. Figs. 5 and 6 with their captions. Particle-number paragraph (N = 10, 40, 80). KITTI overview and data.
- **p.7**: Table VI (all cells, "deg/m)" kept as printed), the KITTI implementation, results, the three baseline groups, 25%/26%, 46.5 Hz, 222.7 MB, 10 Hz. Fig. 7. Table VII (all 24 cells, two-level header flattened, footnote kept). Section D in full: x in R^10, 7 joint angles, identity transition, 48%/43%, "over 50 Hz".
- **p.8**: conclusions; references [1]-[41] complete and in order. Every entry was checked character by character, which covers more than the required one in three.

## Question answered from the package alone

**Question:** In the global-localization experiment, how many particles and diffusion steps does DiffPF use by default, and how fast is inference and how much memory does it use at that particle count, compared with the particle budget of the baselines?

**Answer from the package:** IV. EXPERIMENTS says that all DPF baselines use 100 particles, while DiffPF uses 10 particles and 10 diffusion steps unless stated otherwise. Table V (`assets/table/table-5.csv`, column "N = 10") gives an inference frequency of 52.6 Hz and 194.2 MB of memory at N = 10. Table IV gives the matching RMSE at t = 100: 6.1 ± 0.5 / 7.6 ± 0.2 / 15.3 ± 1.2 for Mazes 1-3.

**Check against the PDF:** p.4 left column, "All DPF-based baselines are evaluated with 100 particles, while DiffPF uses 10 particles unless otherwise specified ... number of diffusion steps is set to 10". p.6, Table V, N = 10 column: 52.6 / 194.2. Table IV, N = 10 row: 6.1 ± 0.5, 7.6 ± 0.2, 15.3 ± 1.2. The answer is correct.

## Result

0 errors, 0 minors. The package matches the PDF on pages 1-8 for text, mathematics, all table cells, prose numbers, figures and all 41 references.
