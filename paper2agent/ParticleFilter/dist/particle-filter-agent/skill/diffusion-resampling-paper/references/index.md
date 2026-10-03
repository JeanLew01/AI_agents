# Paper navigation

Use exact headings to locate current line numbers. Read relevant passages, not both complete documents. This index locates evidence; it does not summarize findings.

## Main paper — [paper.md](paper.md)

| Exact heading | Look here for |
| --- | --- |
| Abstract | One-paragraph summary |
| 1. Introduction | Resampling definition (1), differentiable resampling landscape (REINFORCE, soft, Gumbel, OT (2), kernel/CDF), contributions |
| 2. Diffusion differentiable resampling | Langevin forward SDE (3), reverse SDE (4), training-free ensemble score (5)-(6), Algorithm 1 (diffres, Euler-Maruyama), Remark 1 (Doob h-function view (7)) |
| 2.1. Differentiable sequential Monte Carlo | Feynman-Kac model (8), Algorithm 2 (differentiable SMC with diffres), choice of reference from posterior samples |
| 2.2. Mean-reverting Gaussian reference | Moment-matched Gaussian reference (9), mean-reverting forward SDE (10) and its transition mean/covariance |
| 2.3. Exponential integrators | Semi-linear form (11)-(12), Jentzen-Kloeden and Lord-Rougemont integrators |
| 3. Convergence analysis | Ideal vs approximate reversal (13), Assumptions 1-2, Proposition 1 (W2 bound), Corollary 1 (convergence with N(t), T(t)), Remark 2 (polynomial sample size) |
| 4. Experiments | Goals and baselines (OT, Gumbel-Softmax, Soft); code link |
| 4.1. Gaussian mixture importance resampling | Table 1 (sliced W1, resampling variance), Figure 1 (run time vs N, K, epsilon) |
| 4.2. Linear Gaussian SSM | Model (14), Table 2 (log-likelihood, filtering KL, parameter error), Figure 2 (loss landscapes) |
| 4.3. Prey-predator model | Lotka-Volterra SDE (15) with Poisson observations, neural dynamics, Figures 3-4 |
| 4.4. Vision-based pendulum dynamics tracking | Pendulum SSM (16) with image observations, Figures 5-6 |
| 5. Related work | Gourevitch et al. (categorical reparameterisation), Wan & Zhao DiffPF (trained conditional diffusion) |
| 6. Conclusion | Summary; limitations and future work |
| Acknowledgements | Funding, compute resources, author contributions |
| Impact statement | Broader-impact statement |
| References | Bibliography (author-year) |
| A. Diffusion resampling with Gaussian reference | Algorithm 3: implementable diffres with mean-reverting Gaussian reference |
| B. Proof of Proposition 1 | Synchronous coupling, Itô, Grönwall; (17)-(20) |
| C. Proof of Corollary 1 | Langevin contraction (21)-(22), choice of N and T(t) (23)-(25) |
| D. Elaboration of Remark 1 | Empirical forward-reversal pair, weights gamma_i (26)-(30) |
| E. Error analysis of the resampling mapping | L2 error of the resampling map via chi-square divergence (31)-(33) |
| F. Common experiment settings | JAX/OTT/Flax implementation, b^2 = Sigma_N, integrators tested (EM, Jentzen-Kloeden, Lord-Rougemont, Tweedie; SDE vs ODE), T and K grids; Gumbel-Softmax and Soft resampling definitions |
| G. Gaussian mixture resampling | Model (34) and closed-form posterior, Remark 3, Tables 3-4 |
| H. Time comparison | Timing protocol, Tables 5-6 (resampling error vs N for diffusion K and OT epsilon) |
| I. Linear Gaussian SSM | Model (35), L-BFGS divergence criteria, OTT implicit-differentiation issue, Tables 7-10 |
| J. Prey-predator model | Model (36)-(37), network (Figure 7), Tables 11-12 (RMSE and successful runs) |
| K. Vision-based pendulum dynamics tracking | Two training settings, Tables 13-16, Figures 8-11, latent identifiability, network architectures |
| L. Bayesian neural network training | Partial BNN SSM (38) on CIFAR-10 with ResNet18, Table 17 |
| M. Weather forecast | ERA5/WeatherBench 850 hPa temperature, d = 2048 latent state, Tables 18-19, Figure 12 |
| N. Choosing the hyperparameters | Guidance on b, pi_ref, T, integrator, K |
| O. Additional related work | SVGD, feedback particle filter, ensemble score filter |
| P. Take-away messages | Summary bullets; Table 20 (comparison of resampling schemes: differentiability, consistency, bias, complexity) |

For long sections, search a narrower subsection or prompt. Headings inside fenced quotations are source content, not document section boundaries.

## Supplementary information — [supplement.md](supplement.md)

| Exact heading | Look here for |
| --- | --- |
| Document beginning | Source text or supplied-material notes |

For long sections, search a narrower subsection or prompt. Headings inside fenced quotations are source content, not document section boundaries.

## Assets

Figure and table captions in the documents link to the files below. Open only the needed image; for a table, read its header and relevant rows first.

- `assets/figure/`: main figures (JPEG).
- `assets/supp_figs/`: supplementary and extended-data figures (JPEG).
- `assets/table/`: main tables (CSV, or JPEG when transcription is unreliable).
- `assets/supp_table/`: supplementary tables (CSV, or JPEG fallback).

Asset paths are relative to the skill root. CSVs retain internal blank rows; captions and merged headers may also occupy rows. Consult the document notes before treating every row as data.
