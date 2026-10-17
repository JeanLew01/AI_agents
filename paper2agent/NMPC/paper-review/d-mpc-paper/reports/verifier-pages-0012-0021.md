# Independent verification: D-MPC (arXiv:2410.05364v2), PDF pages 12-21

- PKG: /home/jixia/AI_agents/paper2agent/NMPC/staging/d-mpc-paper-s2
- DOC: /home/jixia/AI_agents/paper2agent/NMPC/paper-review/d-mpc-paper/documents/s001-d-mpc
- Scope: page 12 (end of 5 Conclusions + start of References), References pp. 12-15, Appendices A-J pp. 16-21.
- Ground truth: source.pdf only (page crops made with p2s_tools `crop` at 150-330 dpi, native text from p2s_tools `lines`). I did not use the authors' TeX source or the reviewers' reports.
- Scratch: /home/jixia/AI_agents/paper2agent/NMPC/paper-review/_scratch/d-mpc-v2 (crops p12a ... p21a, native text lines-12.txt ... lines-21.txt)
- Status: COMPLETE

## Result

**0 errors, 0 minors** in pages 12-21. Three observations are listed below. They are not defects in the transcription of pages 12-21, and no repair is needed.

## Coverage (what I actually did)

| Page(s) | Checks performed |
| --- | --- |
| 12 | Last two Conclusions paragraphs (p0012-b001, b002): read against a 200-dpi crop and compared word for word with the native text. `## References` heading checked. |
| 12-15 | References: counted the entries (52 in the PDF, 52 in the package, same order). A script rebuilt each entry from the native text lines, using x-positions for hanging indents, and compared **all 52 entries character by character** with paper.md. I also read **every** entry (not only every third) on 200-dpi crops of pp. 12, 13 (two halves), 14 (two halves) and 15. |
| 16 | Appendix A, all four paragraphs, against a 220-dpi crop, with every inline formula checked symbol by symbol. Opened Algorithm 3 and Algorithm 4 JPEGs and compared them line by line with the transcriptions and with a 150-dpi page crop (completeness, rules, no stray body text). B heading and intro sentence. |
| 17 | Algorithm 5: compared the JPEG line by line, including nesting depth, with the transcription and with a page crop. C text. Table 4: checked every CSV cell by script against the native text (7 data rows, all cells identical, including the uneven '(±x)' spacing). Checked the header against a 230-dpi crop and checked for bold cells at 330 dpi (there are none). Appendix D: both displays and the inline S_k definition against a 230-dpi crop. |
| 18 | End of D (inline inverse relation), E, E.1 (all paragraphs and numbers), E.2, and Table 5 (CSV and the markdown copy cell by cell against the native text and the crop). Start of E.3. |
| 19 | E.3 token list, display (3) with \tag{3}, the paragraph after it, and Table 6 (all 9 rows of the CSV and the markdown copy against the native text and a 220-dpi crop). E.4, E.5, E.6 and F against a 200-dpi crop. |
| 20 | G, H (f_novel formula, σ², κ, κ̃, noise range, h_target values), I (clip ranges, 100 episodes, 30170 transitions, 23.14 (± 2.31), 256 trajectories) and the start of J, all against 200-dpi crops. |
| 21 | End of the J paragraph. Table 7: all 12 CSV cells and the markdown copy against the native text and a 230-dpi crop, plus the caption and the unit. |
| 16-21 | Also checked by script: a word-level diff of all appendix prose, captions and headings in paper.md (maths, algorithms and table bodies removed) against the PDF native text. The only differences were maths tokens, so **no prose word differs**. A diff of the numbers in the prose found only representational differences (`10^6` is extracted as `106`). LaTeX check for lines 294-613: `$` delimiters are balanced, braces are balanced, and `\left`/`\right` are paired. No `<sup>`/`<sub>` debris and no unpaired `**`. Non-ASCII characters are only ± × ç ü – ’, all intended. |
| SKILL.md, index.md, conversion notes | Read once. All 37 headings listed in index.md exist exactly in paper.md (`grep -n '^#'`). Each claim in the notes about pp. 12-21 was checked (see below). |

## Findings

| # | severity | PDF page | item id | package says | PDF shows | suggested fix |
| --- | --- | --- | --- | --- | --- | --- |
| - | - | - | - | No discrepancies found in pages 12-21. | - | - |

Observations (no action required):

- O1 (index.md, Assets section): the section points to `assets/supp_figs/` and `assets/supp_table/`. Both directories exist in PKG but are empty, and supplement.md says that no materials were supplied. This is harmless template text. A reader may look in the empty folders, but they lose nothing.
- O2 (index.md, supplement table): "Document beginning" is listed as an exact heading, but supplement.md has no such heading; its only heading is `# Supplementary information`. This is template wording outside pages 12-21. It is harmless because the file is only 3 lines long.
- O3 (Algorithm 4, line 2): the continuation line of item 2 starts with one `&emsp;`. This matches the printed indentation of the wrapped line. Strictly speaking it is a wrap indent, not a nesting level as the conversion notes describe '&emsp;'. This is cosmetic and faithful to print.

## Checked and found correct

- p12 (p0012-b001, b002): the last two paragraphs of 5 Conclusions are identical to the PDF and start a new paragraph after the p11 text.
- pp12-15 References (p0012-b003 ... p0015-b003): the package and the PDF both have 52 entries in the same order. All 52 entries were compared character by character with the PDF native text by script: exact match. The only differences are two line-break joins, and both were handled correctly (#23 Kumar 'reinforce-/ment' -> 'reinforcement'; #41 Sutton '2(4):/160–163' -> '2(4):160–163'). Hyphens that belong to compounds are kept ('model-augmented', 'Compounding-Error'). I also read every entry visually on 200-dpi crops of pp12-15, including the URLs (sP1fo2K9DFG, bAXmvOLtjA, sFyTZEqmUY, doi 10.1007/s00170-021-07682-3, ojs.aaai.org/.../9590), the 'J . Bagnell' spacing, 'Müller', 'François', and the Zhu et al. entry without a year. Italic venue styling is not carried over (an accepted convention).
- p16 Appendix A: the text is verbatim. Maths checked: q(x_k|x_{k-1}) = N(x_k; √α_k x_{t-1}, (1−α_k)I) with the printed x_{t-1} kept; p_θ(x_{k-1}|x_k) = N(x_{k-1}; μ_θ(x_k,k,y), Σ_k); x_K ~ N(0,I); MSE(ε_k, ε_θ(x_0+ε_k,k,y)); p_θ(x_{k-1}|x_k,y); a_{t:t+F-1}; s_{t+1:t+f} (lowercase f as printed). The typo 'by minimize' is kept.
- p16 Algorithm 3 (assets/figure/algorithm-3.jpg, 2017×447): the image is complete, with caption bar, top and bottom rules and line numbers 1-6, and has no body text in it. Transcription lines 1-6 match the image symbol for symbol, including the order a_j, h_j inside p_1(·) and the bold/upright conventions.
- p16 Algorithm 4 (algorithm-4.jpg, 2017×471): the image is complete. Lines 1-6 match, including the printed s_{t+1:t+f_F} in line 2 and s_{t+1:t+F} in line 3.
- p17 Algorithm 5 (algorithm-5.jpg, 2026×968): the image is complete, with lines 1-15 and the nesting bars. All 15 lines match: R_N=0, A_{N,H}=0 (printed H kept), l = n mod K, a^prev_{min(t,F−1)}, f^l_prop, f^l_states, f^i_reward and f^i_value with the 1/K Σ_{i=1}^K averaging, A_{n,t+1} in the softmax-weighted line 14, ∀t∈[0,F−1]. Nesting depth: lines 5-7 and 13 have one level, lines 8-12 have two levels.
- p17 Table 4 (table-4.csv and the markdown copy): the header, 6 data rows and the Average row are all identical to the PDF, including MBOP 9.70 and 12.40, D-MPC 61.24 (±2.30) and 92.49 (±2.23) without a space, the other cells with '(± x)', and the averages 33.13 / 65.98 / 57.81 / 57.14 / 59.83 / 53.32 / 52.93. The caption is verbatim. There are no bold cells in print.
- p17-18 Appendix D: the dataset display (r^2_{1:T_1} and r^m_{1:T_2} kept as printed), the S_k union with limits m=1..M and i=1..T_m, and the F̂_k display with 1/N Σ_{i=1}^N 1_{s_k^i ≤ t} and s_k^{i=1…N} ∈ S_k, both without \tag as printed. ŝ_k = 2F̂_k(s_k) − 1 and s_k = F̂_k^{-1}((1+ŝ_k)/2) are correct. 'the the' is kept.
- p18 E.1: the four model types are correct. p(a_t|s_t), p(s_t+1|s_t,a_t) as printed, p(a_{t:t+F-1}|s_t) and p(s_{t+1:t+F}|s_t,a_{t:t+F-1}) all match. Token dimension 256, 16 Fourier bases, 8 heads, 1024 qkv dims, 2048 MLP dims, and the diffusion steps / transformer layers 5/2, 3/2, 32/5, 10/5 all match.
- p18 E.2 and Table 5: s_{t+1}=f(s_t,a_t). The values 2 / 512 / ReLU / 256 / Mean square error match.
- p19 E.3: the token list with \texttt names, LayerNorm, O_1, O_2, ⋯. Display (3) is correct (sum over t, O_{2t-1}→a_t, O_{2t}→s_{t+1}, \tag{3}). In Table 6 all 9 rows are verbatim, including the trailing full stops in 'Fourier embedding with 16 basis functions.' and 'Not used.'.
- p19 E.4-F: 10 layers, discount factors 0.99 and 0.997 (Hopper), and the −100 termination penalty match. Adam warm-up 0 → 10^{-4} over 500 steps, cosine decay 10^{-4} → 10^{-5}, 2×10^6 steps, clip norm 5 and EMA 0.99 match ('uses EMA' kept). Compute on A100 at about 2 days matches. F = 32, N = 64 and H = 1 match.
- p20 G, H and I: '≲ 1.0' is correct. f_novel(s_t, A_t) = 5 exp(−(h_t − h_target)²/2σ²), σ² = 5×10^{-4}, κ = 0, κ̃ = 1, start height 1.25, noise [−5×10^{-4}, 5×10^{-4}], and h_target 1.2 / 0.9 / 1.4 all match. 'the the' is kept. The clip range [−0.5, 0.5] vs [−1, 1], 100 episodes, 30170 transitions, 23.14 (± 2.31) and 256 trajectories all match.
- p20-21 J and Table 7: the paragraph is continuous across the page break. The 12 cells match (for example 3.51(±0.06) × 10^-1 … 3.51(±0.07) × 10^2). The caption is verbatim, and the unit is milliseconds per environment step.
- Conversion-note claims for pp12-21, all **true**:
  - x_{t-1} in Appendix A, s_{t+1:t+f_F} in Algorithm 4, \mathbf{A}_{N,H} in Algorithm 5 and p(s_t+1|s_t,a_t) in E.1 are kept as printed.
  - 'the the' (D, H), 'a a high-level summary' (C), 'by minimize' (A) and 'uses EMA' (E.5) are kept.
  - The Zhu et al. reference has no year.
  - r^2/r^m in the Appendix D dataset are kept.
  - The Table 4 header is flattened to 'MS Diff Action Proposal: SS Diff Dynamics' etc.
  - The '(±x)' spacing is non-uniform as printed.
  - The Table 7 exponent convention uses ASCII caret and hyphen and the U+00D7 multiplication sign.
  - Only (3) is numbered in this range, and the Appendix D displays are unnumbered.
  - No 'Appendix' heading is printed: p16 starts directly with 'A Algorithms for model learning', and p15 holds only the last 3 references.
  - Algorithms 3-5 are kept as images followed by line-numbered transcriptions.
- The claim that the maths was checked against the TeX source cannot be verified without the TeX, which I deliberately did not use. All maths in my range agrees with the PDF.
- index.md: all headings A-J, E.1-E.6 and References exist exactly in paper.md, and their "Look here for" descriptions fit the content. The asset links `../assets/figure/algorithm-3/4/5.jpg` and `../assets/table/table-4/5/6/7.csv` resolve.

## Technical question answered from the package

**Question:** How expensive is D-MPC's planner per environment step compared with MBOP, and how many denoising steps and transformer layers does its multi-step diffusion dynamics model use?

**Answer from the package only:**
- Source: paper.md "## J Timing measurements" and Table 7 (assets/table/table-7.csv).
- On a single A100, D-MPC needs 9.37(±0.03)×10^1 ms on Walker2d, 9.24(±0.07)×10^1 ms on HalfCheetah and 9.48(±0.04)×10^1 ms on Hopper per environment step. That is about 93 ms, roughly 20× MBOP (4.77 / 3.93 / 5.07 ms) and about 3.6× faster than ART-MPC (337 / 262 / 351 ms). An MLP policy needs about 0.35 ms.
- Source: "### E.1 Diffusion models". The multi-step diffusion dynamics model uses 10 diffusion timesteps and 5 transformer layers. The transformer layers have 8 heads, 1024 qkv dimensions and 2048 MLP hidden dimensions, and the model uses DDIM with a cosine schedule.

**Check against the PDF:** p21 Table 7 shows exactly these values with the caption "(in milliseconds) per environment step … single A100 GPU". The p18 E.1 paragraph reads "For all of our multi-step diffusion dynamics models, we use 10 diffusion timesteps and 5 transformer layers for the denoiser", and the preceding paragraph gives 8 heads, 1024 and 2048. The answer is correct.
