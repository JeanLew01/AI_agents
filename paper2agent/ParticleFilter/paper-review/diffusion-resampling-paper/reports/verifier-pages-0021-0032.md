# Verifier report: pages 21-32 (diffusion-resampling-paper, s001)

Package: `staging/diffusion-resampling-paper-s1` (paper.md lines 873-1238, assets/table/table-7 ... table-20, assets/figure/figure-7 ... figure-12).
Ground truth: `documents/s001-diffusion-resampling/source.pdf`, pages 21-32 (end of Appendix I through Appendix P).
Scratch: `paper-review/_scratch/verify-diffres-21-32` (native text dumps `linesNN.txt`, comparison script `cmp.py`, crops).

Status: COMPLETE

## Coverage (what was actually done)

- **Tables 7-20 (all cells, not sampled).** Native PDF text lines were extracted for each table region (`p2s_tools.py lines`) and every numeric token, NaN, dash and asterisk marker was compared in order against each CSV (script `cmp.py`). Table 7, 8, 9: 192/192 tokens. Table 10: 62/62. Table 11: 43/43. Table 12 RMSE: 91/91. Table 12 success counts: 54/54. Table 13: 66/66. Table 14: 35/35. Table 15: 66/66. Table 16: 35/35. Table 17: 21/21. Table 18: 63/63. Table 19: 63/63. Table 20: checked by eye, cell by cell. The only differences the script reported came from line ordering (NaN cells, row labels sitting 0.2 pt higher), the ∗ glyph versus `*`, and the page number. I resolved each one by hand, and all are correct. The row labels and the order of the flattened multi-level headers (Euler–Maruyama/Lord–Rougemont/Jentzen–Kloeden/Tweedie × ODE/SDE; SDE before ODE in Tables 13 and 15; SSIM/PSNR pairs) were checked against the PDF header lines. The markdown copy of every table was then compared programmatically with its CSV (see finding E1).
- **NaN and asterisk markers.** Table 10: NaN in the ‖θ−θ̂‖ column for Gumbel, Soft and Multinomial (7 cells). Table 12: NaN at T=1,K=4 LR-ODE and at T=2,K=4 LR-ODE, LR-SDE and JK-SDE, plus T=2,K=8 LR-ODE. Table 13: `*` and `– ` at T=1,K=4 JK-SDE, `**` at T=1,K=8 JK-SDE. Table 15: `*` on four configurations (EM-SDE K=4 and K=8, JK-SDE K=4, Tweedie K=4). Table 16: `*` on OT 0.5 and `**` on OT 1.0 and 1.5. All are in the correct cells.
- **Equations (36), (37) and (38)** were compared symbol by symbol against 220-dpi crops. I also checked the inline maths in Appendix K (Z₀ = [π/4 0], Λ_ζ, σ_ζ², σ_train, κ = 10⁴, β₂, **h**(Z_j), the [**h**(Z_j) ζ_j] ∈ ℝ⁵ update rules, ω₀ = 8.0), Appendix L (d_z, d_θ), Appendix M (z_k ∈ ℝ²⁰⁴⁸, 5.625°, 𝒩(y_k | ℳ_k z_k, σ_y² I), the Sigmoid update, σ_q² = 0.1, 2×10⁻⁴, 10⁻⁵) and Appendix N (K ≤ 8, K < N) against crops or native text.
- **Prose completeness.** Two automatic checks were run. First, every PDF prose line on pages 21-32 has all of its 4-word windows present in paper.md, with no misses. Second, every package prose line in Appendices I-P has its 4-word windows present in the PDF text. The only misses came from removed maths, line hyphenation and page breaks, and I checked each one by hand. I also read all paragraphs, the take-away bullets (page 31) and the captions against the page images.
- **Figures 7-12.** I opened every linked JPEG and compared it with the page renders (pages 23, 27, 28 and 30). All panels, axes, tick labels and legends are complete, and no caption or body text sits inside any crop. Figure 7 looks different from a poppler render, where the text overlaps the arrows. A PyMuPDF crop of the PDF matches the package image exactly, so this is a renderer artefact and not a package problem.
- **Structure.** Headings I-P are at the correct level and use the printed titles. I checked the reading order across page breaks (21→J, 23→24, 24→25, 25→26, 29→30, 30→31). I checked the relocated floats against the conversion notes: Tables 8-10 printed alone on page 22 sit at the end of I; Table 12, printed at the top of page 24, sits at the end of J; Figures 8-11, printed on pages 27-28, sit at the end of K; Table 18, printed above the M heading, sits inside M. Nothing is lost or duplicated: 36 asset links, each target linked once.
- SKILL.md, index.md and the conversion notes were read once. Every heading named in index.md exists exactly in paper.md. The notes' claims about pages 21-32 are true (float positions, the asterisk policy, Table 17 bold not carried over, the 'Lokta–Volterra' and 'Jentzen–Kloden' slips kept).
- **References:** not in my page range (pp. 10-13).

## Findings

Totals: **1 error, 3 minor.**

| # | severity | PDF page | item | package says | PDF shows | suggested fix |
| --- | --- | --- | --- | --- | --- | --- |
| E1 | error (maths rendering) | 32 (Table 20); 22 (Table 10 header) | markdown copies of Table 20 and the Table 10 header in paper.md | The markdown tables double every LaTeX backslash, e.g. `$O(K \\, N)$`, `$N(K) \\to \\infty$`, `$O(N^2 \\log(N)^{-1} \\, \\varepsilon^{-1})$`, `Gumbel $\\tau$`, `Soft $\\alpha$`, and the Table 10 headers `$\\lVert L - \\widehat{L} \\rVert_2$` and `$\\lVert \\theta - \\widehat{\\theta} \\rVert_2$`. In a math renderer `\\` is a line break, so the complexity and consistency entries and the column names come out garbled (e.g. "lVert L" or "to infty" as text). | O(K N), N(K) → ∞, O(N² log(N)⁻¹ ε⁻¹), ‖L − L̂‖₂ and ‖θ − θ̂‖₂ as normal maths. The CSVs `table-10.csv` and `table-20.csv` are correct (single backslashes). | Regenerate these two markdown tables from their CSVs with single backslashes. The same defect also affects the main-text Table 2 markdown in paper.md (lines 288-310: `$\\varepsilon=0.3$`, the `\\lVert` headers). That is outside my range, so I flag it for the pages 1-9 verifier. |
| M1 | minor | 26 | eq. (38), Appendix L | The display `$$\begin{aligned}…\end{aligned}\tag{38}$$` is embedded in the middle of a paragraph ("…construct an SSM $$ … $$ for CIFAR10 classification…"). This contradicts the conversion-notes convention ("A sentence that continues after a display equation starts a new paragraph") and may not render as a display in every Markdown renderer. The maths itself is correct. | Display equation (38) between "construct an SSM" and "for CIFAR10 classification, …". | Put eq. (38) in its own `$$` block and start "for CIFAR10 classification, …" as a new paragraph, as for (35)-(37). |
| M2 | minor | 21-32 | float captions | Caption labels are inconsistent: `*Table 7.*` to `*Table 11.*` and `*Figure 7.*` are italic, but "Table 12." to "Table 20." and "Figure 8." to "Figure 12." are plain. The caption text is correct in all cases. | All caption labels are italic. | Use one style throughout (cosmetic). |
| M3 | minor | (index) | references/index.md | The index omits the printed headings "Acknowledgements" and "Impact statement", which exist in paper.md (lines 395 and 401). It also omits "Conversion notes". | n/a | Optionally add rows to the index. Not a correctness issue; every heading the index lists is exact. |

Note (not a package defect): the main-text Table 2 prints OT (ε = 1.6) L-error as 2.75 ± 2.20, while Appendix Table 10 prints 2.76 ± 2.20. The package reproduces both faithfully. This is the authors' inconsistency.

## Checked and found correct (by page)

- **p21:** Table 7: all 84 cells, its caption (no final period, as printed) and its header. The I-section paragraphs ("estimation diverges largely…", "The results are detailed in Tables 7 to 10…", "Let us focus…", "Table 8 shows…", "Figure 2 shows…"), including 2.72, N = 32, Gumbel 0.2 / soft 0.1, T = 2, K = 4, ε = 0.3, and 'Jentzen–Kloden' kept. The J heading. Eq. (36): dC, dR, the Poisson line, the drift terms (α − βR) and (ζC − γ), σ C dW₁ and σ R dW₂.
- **p22:** Tables 8, 9 and 10: every cell including NaN, and the captions (scaled by 10⁻¹; "Tables 7, 8, and 9.").
- **p23:** Figure 7 (crop complete; caption correct). Table 11: all rows, including Gumbel (0.5) and Stopped. "where we set α = γ = 6, β = 2, ζ = 4, σ = 0.15" and λ: ℝ×ℝ → ℝ²_{>0}. Eq. (37): 5 / (1 + exp([−5c; −cr] + 4)). Milstein, t ∈ [0,3], 256 steps, 1,000 iterations, lr 0.005, 100 predictions, 64 particles, 20 repeats. The K heading. Experiment settings (g = 9.81, l = 0.4, σ_obs = 0.01, t ∈ [0,4], j = 0,…,256, Z₀).
- **p24:** Table 12: both sub-tables, every cell, and the caption. The first and second settings (all hyperparameters). "Results and evaluation" (5 and 9 runs). The paragraph citing Tables 13-16 and Figures 8, 9 and 5.
- **p25:** Tables 13 and 14. The paragraphs "with resampling…", "As we have seen…", "Identifiability of the latent space" (R² ≈ 0.98 and 0.92) and the start of "Network architectures".
- **p26:** Tables 15 and 16 with their captions ("only 3 (**) and 4(*)" as printed). The update rules; SIREN 3×256 with ω₀ = 8.0; the decoder (16 and 256 units, 4×4×16, 3×3 stride 2, 32/16/1 channels, 32×32). The L heading and pBNN text; eq. (38) symbols (N(z_j; ρ z_{j−1}, 1 − ρ²), Softmax(f_{θ,z_j}; D_j)); ρ = 0.99.
- **p27:** Figures 8 and 9 (both panels and legends complete; captions correct). Table 17: 10 cells. ResNet18 paragraph: d_z = 1,856, d_θ = 11,172,106, 8 particles, threshold 0.5, 200 epochs, T = 1, K = 4, JK SDE.
- **p28:** Figure 10: panels a-d complete. Its caption keeps the authors' unclosed parenthesis "(mean SSIM/PSNR 0.761/17.0, b)". Figure 11: all four sub-axes complete; caption correct (T = 1, K = 4; "Figure 10a").
- **p29:** Table 18, including the labels "K = 4,ODE" without a space, as printed. M: experiment settings, training details, and the results paragraph (all numbers).
- **p30:** Table 19. The "worst results … Gumbel (τ = 0.1)" paragraph. The Figure 12 paragraph. Figure 12: both panels, the k = 0…32 labels and the gt/y/pred rows; caption correct.
- **p31:** The M limitations paragraph (d = 2048). N (all hyperparameter guidance). O (Liu 2017, Yang et al. 2013, Kang et al. 2025, Bao et al. 2024, Equations (13) and (30)). P intro and all four take-away bullets verbatim, including π_ref = π and {(w_i, X_i)}_{i=1}^N.
- **p32:** Table 20: every cell (Yes/No entries, "Yes, but not τ → 0", "No, except at τ → 0", Multinomial unbiased "Yes, as N → ∞" as printed, complexities) and its caption. In the CSV everything is correct; for the markdown see E1.

## Technical question answered from the package only

**Question.** In the prey-predator experiment, how did Lord–Rougemont behave with the ODE solver at T = 2, and how does the best diffusion configuration compare with the best baseline in RMSE?

**Answer from the package.** Source: Appendix J, Table 12 (both sub-tables) and Table 11.
- With T = 2 and the Lord–Rougemont ODE solver, K = 4 and K = 8 gave 0 successful runs out of 20, so the RMSE cell is NaN. K = 16 gave 3 out of 20 successful runs, with RMSE 9.52 ± 1.97.
- The lowest diffusion RMSE is Euler–Maruyama SDE at T = 2, K = 16: 1.01 ± 0.47, with 18 of 20 runs successful.
- The best baseline in Table 11 is Soft (0.9): 1.89 ± 0.64, with 16 of 20 runs successful.

**Check against the PDF.** Page 24 Table 12 shows LR-ODE T = 2 as NaN/NaN/9.52 ± 1.97 with success counts 0/0/3, and EM-SDE T = 2, K = 16 as 1.01 ± 0.47 with 18 successes. Page 23 Table 11 shows Soft (0.9) as 1.89 ± 0.64 with 16 successes. The answer is correct.
