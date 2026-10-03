# Independent verification: pages 1-9 (main text)

Package: `staging/diffusion-resampling-paper-s1` (`references/paper.md` lines 1-394, assets `algorithm-1/2.jpg`, `figure-1..6.jpg`, `table-1.csv`, `table-2.csv`); document `s001-diffusion-resampling`; paper arXiv:2512.10401v3 (ICML 2026).

Status: COMPLETE

## Coverage
Every page of the range was checked in full; nothing was sampled.
- **Mathematics:** every display equation was compared with a 220-260 dpi crop of the PDF:
  - numbered equations (1)-(16);
  - the unnumbered displays: the recalled reverse SDE on p5, the transition mean/covariance on p4, both exponential integrators on p5, strong log-concavity, the Assumption 1 Lipschitz bound, the Assumption 2 bound, and the Proposition 1 and Corollary 1 bounds.
  - The inline maths of each paragraph was also checked: symbol definitions, $\alpha_i$, $\mu_N$, $\Sigma_N$, $B_k$ covariance, $\mathsf{W}_l^l$, constants and inequalities, and the LGSSM error definitions.
- **Statements:** Assumptions 1-2, Proposition 1, Corollary 1 (with the "Proof. See Appendix B/C"), and Remarks 1-2 were checked for completeness, order and numbering.
- **Numbers:** every cell of Tables 1 and 2 (CSV and the Markdown table in `paper.md`) was compared with a 260-dpi crop. All numbers quoted in the prose of pages 6-9 were checked: N=10,000; K=128/8; ε=0.3/0.8; K≈6/ε at N=8,192; θ1=0.5, θ2=1; 128 steps; Θ box ±0.1; 100 runs; 32 particles; t∈[0,3]; 256 Milstein steps; 100 predictions; 20 runs; N=64; 32×32; J=256.
- **Structure and prose:** headings, paragraph order, joins across columns and pages, and the footnote were checked. Prose completeness was checked with a script: an n-gram comparison of the PDF text of each column (from `pdftotext`) with `paper.md`. Every hit was explained by maths, figure text or column interleaving, apart from the footnote finding below.
- **Algorithms, figures and captions:**
  - Algorithms 1-2: each transcription was checked line by line against both the PDF crop and the packaged JPEG.
  - Figures 1-6: each JPEG was opened and checked for complete panels, axes and legends, and for any caption or body text inside the crop.
  - The captions of Tables 1-2 and Figures 1-6 were compared with the PDF.
- **Package files and notes:**
  - `SKILL.md`, `references/index.md` and `references/supplement.md` were read.
  - Every "Exact heading" in the index was confirmed to exist verbatim in `paper.md`. The only exception is the supplement pseudo-heading "Document beginning", which is expected.
  - The conversion notes were read and their claims checked against pages 1-9 and the page count (32 pages; Acknowledgements and references start on p10; Appendix A on p14).

## Findings

| # | severity | PDF page | item | package says | PDF shows | suggested fix |
|---|---|---|---|---|---|---|
| 1 | error | 2 (cont. 3) | p0002-b017, p0002-b016 (join into p0003-b001) | `paper.md` l.63 has one paragraph that starts "Footnote 1: To simplify later analysis we assume that the Brownian motions in Equations (3) and (4) are the same. At time $T$, the marginal distribution $q_T$ ..." and runs on through "... according to $$(5)". The page plan puts the footnote item b017 *before* b016. b016 has `join_previous: space`, so it attaches to the footnote and not to eq. (4). Main-text sentences (the time-reversal argument, the intractable score, the lead-in to eq. (5)) therefore read as part of footnote 1. Eq. (4) is left without its continuation. The `[^1]` marker after "reverse-time SDE" has no `[^1]:` definition, so it renders as literal text. | The body continues straight after eq. (4): "At time T, the marginal distribution q_T of U(T) equals π by construction, since X(T − t) and U(t) solve the same / [p3] Kolmogorov forward equation. ...". Footnote 1 ("To simplify later analysis we assume that the Brownian motions in Equations (3) and (4) are the same.") sits alone at the foot of the right column. | Move b016 directly after b014, keeping `join_previous: space`, so that eq. (4) continues into "At time $T$ ...". Then move the footnote after the end of that paragraph, after eq. (6)'s paragraph or at the end of Section 2 preamble. Write it as `[^1]: To simplify ...` to match the `[^1]` marker, or keep "Footnote 1:" and drop `[^1]` in favour of a plain superscript. Either way the footnote must be its own paragraph and must not absorb body text. |
| 2 | minor | 7 | p0007-b002, p0007-b004 (Markdown tables in `paper.md` l.288-290, 303, 308-310) | LaTeX in the Markdown table rows is written with doubled backslashes, e.g. `OT ($\\varepsilon=0.3$)` and `$\\lVert L - \\widehat{L} \\rVert_2$`. MathJax/KaTeX reads `\\` as a line break followed by plain letters. The CSVs (`table-1.csv`, `table-2.csv`) and the prose use single backslashes. The same pattern recurs outside this range: `paper.md` l.959 (Table 9 header) and l.1225-1229 (Table 20). | ε and the norm symbols. | Replace `\\` with `\` inside `$...$` in the Markdown table rows, matching the CSVs. |
| 3 | minor | 7 | p0007-b001, p0007-b003, p0007-b007 | Labels are inconsistent. Table 1, Table 2 and Figure 1 captions start with plain "Table 1." / "Figure 1.". Figures 2-6 use italic "*Figure 2.*". | All caption labels are italic. | Use one style, e.g. italic labels, for all captions. |
| 4 | minor | — | Conversion notes, bullet 6 | "A sentence that continues after a display equation starts a new paragraph (e.g. Appendix B ...)." This is stated as a general rule. | In the main text the continuation is joined to the display in the same paragraph (eqs. (1)-(14), e.g. `$$ for any bounded ...`, `$$ where $P^\varepsilon$ ...`). The rule holds only for (15)-(16) and the appendices. | Reword to "In some sections (e.g. 4.3, 4.4, Appendix B) ...", or make the joins consistent. |

No other discrepancies were found.

## Checked and found correct
- **p1:**
  - Title, authors, affiliation and correspondence footnote (incl. 趙正 and e-mail), proceedings notice; the arXiv stamp is correctly omitted. Abstract matches word for word.
  - Eq. (1): both lines, "s.t.", $\mathbb{E}[\frac1N\sum\psi(X_i^*)]=\mathbb{E}[\psi(X)]$, single tag.
  - Inline maths: $I_i\sim\mathrm{Categorical}(w_1,\ldots,w_N)$, $X_i^*\coloneqq X_{I_i}$, $\partial X_i^{\theta,*}/\partial\theta$, $\partial\mathbb{E}[X_i^{\theta,*}]/\partial\theta$.
  - Paragraphs that cross columns are joined correctly. Authors' typos ("combing", "reparapemtrisation") are kept.
- **p2:**
  - Eq. (2) ($N\sum_j P^\varepsilon_{i,j}X_j$, $i=1,\ldots,N$), eq. (3) and eq. (4) (including $2\nabla\log p_{T-t}$ and $U(0)\sim p_T$).
  - $P^\varepsilon\in\mathbb{R}^{N\times N}$, $1/\varepsilon$; the three contribution bullets; "See Table 20"; Section 2 heading.
  - Only the footnote placement is wrong (finding 1).
- **p3:**
  - Eq. (5): both lines and the normalising integral. Eq. (6) and the definition of $\alpha_i$. Eq. (7) and $h_i$. Eq. (8) (product from $j=0$ to $J$, $M_j^\theta(z_j\mid z_{j-1})G_j^\theta(z_j,z_{j-1})$).
  - $O(N)$ cost and the logarithmic parallel cost; the JKO sentence; Remark 1 (with $\gamma_i=w_i$ and $p_T(x)=\sum h_i(x,T)$).
  - Algorithm 1: Inputs, Outputs and lines 1-9, including $\xi_k^i\sim\mathrm N(0,2b^2\Delta_kI_d)$ and the line 6 update with $s_N(U_{i,t_{k-1}},T-t_{k-1})$. The JPEG is complete and clean.
- **p4:**
  - Bootstrap $M_j^\theta$/$G_j^\theta$.
  - Algorithm 2: caption, Inputs ("Feyman–Kac" as printed) and lines 1-16. Lines 6, 12 and 16 match exactly. The JPEG is complete.
  - Reference-choice paragraph with $(w_{j-1,i},Z_{j,i})$ vs $(w_{j,i},Z_{j,i})$.
  - $\mu_N$, $\Sigma_N$ (with transpose); eqs. (9) and (10).
  - Transition $m_t(x_0)$ and $V_t=\Sigma_N(1-\mathrm e^{-2b^2\Sigma_N^{-1}t})$.
  - Eq. (11): the missing bracket is printed this way and is noted in the conversion notes. Eq. (12): $A=b^2\Sigma_N^{-1}$, $f=b^2(2\nabla\log p_{T-t}(u)-\Sigma_N^{-1}\mu_N)$.
- **p5:**
  - Jentzen–Kloeden integrator: $A^{-1}(\mathrm e^{A\Delta_k}-I_d)f(U_{t_{k-1}})$, the $B_k$ Wiener integral, and $B_k\sim\mathrm N(0,\Sigma_N(\mathrm e^{2A\Delta_k}-I_d))$.
  - Lord–Rougemont integrator: $\Delta_k\mathrm e^{A\Delta_k}f(U_{t_{k-1}},t_{k-1})$ and $B_k\sim\mathrm N(0,2b^2\mathrm e^{2A\Delta_k}\Delta_k)$.
  - Recalled eq. (4) and eq. (13) with $\widetilde U(0)\sim\pi_{\mathrm{ref}}$.
  - $q_t=p_{T-t}$; $p_{t|\tau}$ for $0\le\tau<t\le T$; $\mathsf W_l^l$ definition; strong log-concavity display; $\nu\preceq z$.
  - Assumption 1 ($2C_p<C_{\mathrm{ref}}<2C_{\mathrm{ref}}^-+2C_p$, Lipschitz display, $\pi_{\mathrm{ref}}\preceq C^-_{\mathrm{ref}}$, $p_t\preceq C_p$, $t\ge0$).
  - Assumption 2 (sup over $x$, exponent 1/2, $C_e(t)/N^r$, $t>0$).
  - SNIS paragraph.
- **p6:**
  - $r=1/2$.
  - Proposition 1 bound: $\mathsf W_2^2(p_T,\pi_{\mathrm{ref}})\mathrm e^{b^2(C_{\mathrm{ref}}-2C_p)t}+2b^2N^{-r}\overline C_e(t,T)$, for $t\in[0,T)$.
  - Corollary 1 ($N^{r-c}=\overline C_e(t,T)$, $0<c<r$; bound $2b^2N^{-c}+\mathrm e^{b^2(C_{\mathrm{ref}}-2C_p)t-2b^2C^-_{\mathrm{ref}}T}\mathsf W_2^2(\pi,\pi_{\mathrm{ref}})$; $\lim\mathsf W_2=0$).
  - Remark 2 and the following prose; Gibbs chain $(p_{T|0},q_{T|0})$; $\widetilde q_{T|0}$.
  - Section 4 intro, code URL, Section 4.1 model.
- **p7:**
  - Table 1: all 8×2 cells. Table 2: all 9×3 cells, including the NaN entries. Both captions are correct (scalings $10^{-1}$/$10^{-2}$; $10^{-1}$/$10^{-1}$).
  - Figure 1 JPEG: both panels, the legend and both x-axes (bottom and top) are complete; the caption is correct.
  - Eq. (14) and the LGSSM error definitions.
- **p8:**
  - Figures 2-4 JPEGs are complete: 6 panels with colourbars, 11 box plots with labels, and the legend and axes. Captions are correct.
  - Eq. (15) and eq. (16), including $\sigma^2_{\text{obs}}I_{32\times32}$; $Z_j$ bmatrix; $\zeta_j\sim\mathcal N(0,\Delta_j\Lambda_\zeta)$.
- **p9:**
  - Figures 5 and 6: the JPEGs are complete (both y-axes in Fig. 5; 8 tiles in Fig. 6) and the captions are correct.
  - Pendulum paragraphs; Sections 5 and 6, with "Limitations and future work" in bold as printed.
  - The section ends at "... diffusion resampling." (Acknowledgements are on p10, outside this range).

## Technical question answered from the package
**Question:** With the moment-matched Gaussian reference, what are the forward transition mean and covariance used in the ensemble score? How is the Wiener increment of the Jentzen–Kloeden integrator distributed?

**Answer from `paper.md` §2.2 and §2.3:**
- $p_{t|0}(x_t\mid x_0)=\mathrm N(x_t; m_t(x_0),V_t)$, where
  - $m_t(x_0)=x_0\,\mathrm e^{-b^2\Sigma_N^{-1}t}+\mu_N(1-\mathrm e^{-b^2\Sigma_N^{-1}t})$, and
  - $V_t=\Sigma_N(1-\mathrm e^{-2b^2\Sigma_N^{-1}t})$.
- $\mu_N$ and $\Sigma_N$ are the weighted empirical mean and covariance, computed from $\{(w_{j-1,i},Z_{j-1,i})\}$ inside SMC.
- With $A=b^2\Sigma_N^{-1}$, the Jentzen–Kloeden step adds $B_k\sim\mathrm N(0,\Sigma_N(\mathrm e^{2A\Delta_k}-I_d))$.

**Check against the PDF:** p4 right column and p5 left column (crops `p4-eq9-10.png`, `p5-L1.png`) show exactly these expressions. The answer is correct.
