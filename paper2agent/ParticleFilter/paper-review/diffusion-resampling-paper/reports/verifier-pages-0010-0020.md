# Verifier report: Diffusion differentiable resampling, PDF pages 10-20

Package: `/home/jixia/AI_agents/paper2agent/ParticleFilter/staging/diffusion-resampling-paper-s1`
Review document: `.../documents/s001-diffusion-resampling`
Scratch: `/home/jixia/AI_agents/paper2agent/ParticleFilter/paper-review/_scratch/verify-diffres-10-20`

## Coverage

All pages 10-20 were checked in full. Nothing was sampled.

- **pp. 10-13 (Acknowledgements, Impact statement, References):**
  - I extracted the PDF text layer column by column (`pdftotext -x/-y/-W/-H`, left and right column of each page, in reading order), removed hyphens at line breaks and compared it word by word with `paper.md` lines 395-573 using `difflib`.
  - The only differences are line-break artefacts. The PDF shows `405– 431`, `11 (02n03)`, `http:// github.com` and `22: 730–751` with spaces or line breaks where the package has none. The real hyphens in `infinite-dimensional`, `forward-backward` and `DPM-solver++` are line-final in the PDF. `Ś` in Ścibior is a combining-accent sequence in the PDF and precomposed in the package.
  - So every reference entry (84 in total) is present, in the printed order (column 1 then column 2 on each page), with no column interleaving and no lost or extra text.
  - I checked the `n^2` in Klaas et al. visually with a crop. I read the Acknowledgements and Impact statement against the layout text.
- **p. 14 (Appendix A, start of Appendix B):**
  - Crops of Algorithm 3 at 250 dpi. I compared the transcription line by line (lines 1-15, both `//` comments, the `return` display, line 12's update with brackets, the `n`/`N` index slip). I also opened `assets/figure/algorithm-3.jpg`: it is complete, with top and bottom rules and no caption or body text inside.
  - Equations (17) and (18), the unnumbered three-line derivation and the expectation bound, all checked at 220 dpi.
- **p. 15:** (19) and (20), the definition of $\overline{C}_e$, (21)-(25), the derivative display, and all the prose including the inline exponent and the $T(t)=t+\delta$ argument.
- **p. 16:** the end of Appendix C, and Appendix D (26)-(30) with the inline $h$-function, $\pi^N$, the $\gamma_i$ definition and the Radon–Nikodym sentence. Start of Appendix E.
- **p. 17:**
  - (31)-(33), the inline $\chi^2$ definition and the $\tilde\phi_N$ inequality.
  - The known author slips are reproduced as printed: the misplaced bracket in $\chi^2$, $\pi^{*,N}$ vs $\pi^{\star,N}$, the unsquared integrand of (32), and $\chi^2(\pi_{\mathrm{ref}}\Vert p_T^N)$ in (32) vs $\chi^2(p_T\Vert p_T^N)$ in (33).
  - Appendix F prose: 1,000 projections, $b^2=\Sigma_N$, $T=1,2,3$, $K=4,8,32$, "at least 72 combinations", and the three bullets.
- **p. 18:**
  - Gumbel-Softmax definition: $g_{i,j}=-\log\log u_{i,j}$ (slip kept), $S_{i,j}$, $\overline{S}_{i,j}=\exp((\log w_j+g_{i,j})/\tau)$, $\mathbf{X}\in\mathbb{R}^{N\times d}$.
  - Soft resampling: $q^{\mathrm D}$, steps 1-4, the $\alpha=0/1$ discussion.
  - Appendix G: (34), and the posterior formulas $G_i,\overline\Omega_i,\Omega_i,\mathcal M_i,\mathcal V_i$.
- **p. 19:**
  - Every cell of Tables 3 and 4, both in the CSVs and in the inline Markdown tables, and their captions.
  - The model-generation paragraph: Uniform$([-5,5]^d)$, Wishart, $\omega_i=1/c$, $H\in\mathbb{R}^{1\times d}$, $\Xi=1$, 100 runs.
  - Remark 3: both formulas.
  - The Tables 3/4 discussion: $\varepsilon=0.8$, $T=3,K=32$.
  - Appendix H prose: 50 runs, A100 80G, EPYC 9354 32-Core, $\Delta=T/(K+1)$, $\Delta=0.1$, $T=\Delta(K+1)$.
- **p. 20:**
  - Every cell of Tables 5 and 6 (CSV and inline) and their captions.
  - The sentence that runs across the tables ("large sample size N. Moreover ...") is joined correctly.
  - Appendix I start: (35), $\theta_1=0.5$, $\theta_2=1$, $j=0,\dots,128$, $N=32$, the $\lVert L-\widehat L\rVert_2^2$ definition, the grid $\Theta$, the KL error $\frac{1}{129}\sum_{j=0}^{128}$, `scipyminimize`, $\theta+1$, $\lVert\theta-\widehat\theta\rVert_2<1.9$, 10 %, 80 %.
  - The paragraph that continues onto p. 21 is complete.
- **Whole package:**
  - Read `SKILL.md`, `index.md` and the conversion notes.
  - Every heading listed for `paper.md` in `index.md` exists exactly. "Document beginning" refers to `supplement.md`, which has no heading by design.
  - The conversion-note claims that concern pp. 10-20 are true: the $n^2$ in Klaas, the Appendix E slips, $-\log\log$, the Algorithm 3 `n`/`N` slip, Gumbel 0.2 printed twice in Table 4, the flattened headers of Tables 3, 5 and 6, and the B "where recall that ..." paragraph split.
  - No `<sup>`, glyph soup or stray markers in lines 575-1000.

## Findings

| severity | PDF page | item id | package says | PDF shows | suggested fix |
| --- | --- | --- | --- | --- | --- |
| minor | 12 | p0012-b012 / p0012-b013 | Luo, Y. et al. (2023a): `In *Proceedings* *of The 26th International Conference ...*` (two adjacent italic spans, because the two items are joined) | one continuous italic venue "Proceedings of The 26th International Conference on Artificial Intelligence and Statistics" | Merge into a single span: `*Proceedings of The 26th International Conference on Artificial Intelligence and Statistics*`. Cosmetic: it renders almost the same. |
| minor | 19 | p0019-b002 (table-4.csv) | The CSV header repeats `Method,SWD,Resampling variance` three times (duplicate column names) | three side-by-side sub-tables (OT / Gumbel / Soft) | Optional: rename to e.g. `Method (OT),SWD (OT),...`. It is faithful to print and documented in the notes, but CSV readers will rename or merge the duplicate columns. |

**Errors: 0. Minors: 2.**

There were no mathematical, numerical, ordering or omission errors on pp. 10-20.

## Checked and correct (by page)

- **p. 10:** Acknowledgements (WASP, KAW, Berzelius, MG2024-0035, author contributions), Impact statement, References Agapiou → Chopin & Papaspiliopoulos.
- **p. 11:** Chopin et al. 2022 → Kidger 2021 (thesis). The order across the two columns is correct.
- **p. 12:** Kidger et al. 2021 → Reich 2013. Klaas $n^2$ verified visually.
- **p. 13:** Rosato → Yuan & Lin (left column), Zhang & Chen → Zhu et al. (right column). The list ends at Zhu et al. 2020.
- **p. 14:** Heading A and its intro paragraph. Algorithm 3: all 15 lines, comments, `diffres` monospace, $\{(\frac1N,X_i^*)\}_{i=1}^n$. Heading B. (17) as one tag over two lines, with $b^2(\int\ldots+2\int\ldots)$. (18). The three-line $|h_t|^2$ derivation (factors $2b^2$, $4b^2$). The $\mathbb E$ bound with $2b^2(C_{\mathrm{ref}}-2C_p)$, $4b^2$, $\mathbb E[|h_\tau|^2]^{1/2}$, $C_e(T-\tau)/N^r$.
- **p. 15:** (19) with $2b^2N^{-r}$ as printed. (20) and the $\overline C_e$ definition. Heading C. (21), (22) with $-2b^2C^-_{\mathrm{ref}}T$. $N^{r-c}=\overline C_e$, $0<c<r$. (23), the derivative display, (24), (25). $T'(t)>0$, $T'(t)\le1$.
- **p. 16:** The end of C. Heading D. (26)-(29) with initial laws $\pi$, $p_T$, $p_T^N$, $\pi_{\mathrm{ref}}$. Transition notation $\widetilde q^N_{t|s}$. (30) on two lines. The $\gamma_i$ definition. The special case $\pi_{\mathrm{ref}}=p_T^N$. Heading E and its intro.
- **p. 17:** E (31)-(33) and prose. Heading F, all paragraphs and bullets.
- **p. 18:** Gumbel-Softmax and Soft resampling definitions, complete. Heading G. (34) and the posterior block.
- **p. 19:** Tables 3 and 4 (63 + 24 value cells, all match). The G prose, Remark 3, the discussion. Heading H, the first three paragraphs and the start of the fourth.
- **p. 20:** Tables 5 and 6 (28 + 28 cells, all match), the end of the H paragraph ($K\propto1/\varepsilon$; $\varepsilon=0.1$, $K=32$). Heading I, (35), the following paragraphs up to "making OT parameter".

## Technical question answered from the package

- **Q:** In the experiments, how is the diffusion coefficient $b$ set, and which diffusion times and step counts were mainly tested?
- **Answer (package, `## F. Common experiment settings`):**
  - $b^2=\Sigma_N$, the weighted sample covariance from Algorithm 3. It is chosen to simplify comparison and is "not necessarily optimal"; Corollary 1 suggests an optimal $b$ exists.
  - Mainly tested were $T=1,2,3$ and $K=4,8,32$, on evenly spaced time grids, with four integrators (EM, Jentzen–Kloeden, Lord–Rougemont, Tweedie) in SDE and ODE forms, giving at least 72 combinations.
- **Check against the PDF (p. 17 crop):** identical wording and values.
- **Caveat:** the PDF's Tables 3-4 (p. 19) actually use $K=8,32,128$ for the Gaussian-mixture experiment. This also appears faithfully in the package's Table 3, so a careful reader of the package would get the same, correct picture.
