# Mechanism cards: particle filtering and robust inference collection (pf)

Scout pass of 2026-10-06 (session `2026-10-06_tro2027-diffusion-control`). Sources:
`~/.claude/skills/<skill>/references/paper.md`. Citations are `skill §section (eq. n)` or `Alg. n, l. m`. Anything
marked "(inferred)" is the scout's derivation, not a statement of the paper.

Skills read: `diffusion-resampling-paper` (diffres), `diffpf-paper` (DiffPF), `andrieu-pmcmc-2010-paper` (PMCMC; main
text §2, §4, §5 and selected discussion contributions), `gning-box-bernoulli-2012-paper` (Gning), `haj-chhade-box-messages-2014-paper`
(Haj-Chhade), `benavoli-piga-2016-paper` (BP16), `benavoli-lower-previsions-2011-paper` (BZM11),
`greco-vasile-2022-paper` (GV22), `raices-cruz-robust-is-mcmc-2022-paper` (RC22).

---

## Diffusion resampling (Andersson & Zhao, ICML 2026, arXiv 2512.10401)

### diffusion-resampling-paper: diffusion resampling (`diffres`), a training-free reverse SDE with an ensemble score

- **Computes:** an unweighted re-sample {(1/N, X*_i)} of a weighted ensemble {(w_i, X_i)} ≈ π, pathwise differentiable
  in particles and weights (§1 (1), §2).
- **How:** forward Langevin SDE toward a user reference, dX = b²∇log π_ref(X) dt + √2 b dW, X(0) ~ π (3); reverse SDE
  dU = b²[−∇log π_ref(U) + 2∇log p_{T−t}(U)] dt + √2 b dW (4), with the intractable score replaced by the ensemble
  score s_N(x,t) = Σ_i α_i(x,t) ∇log p_{t|0}(x | X_i), α_i ∝ w_i p_{t|0}(x | X_i) (5)–(6). Start U_0 ~ π_ref, K
  Euler–Maruyama steps, output U_T (Alg. 1 l. 2–8). Implementable version with Gaussian reference: Alg. 3 (App. A),
  always in log weights.
- **Guarantee:** Prop. 1: W₂²(q̃_t, q_t) ≤ W₂²(p_T, π_ref) e^{b²(C_ref − 2C_p)t} + 2b² N^{−r} C̄_e(t,T), under
  Assumption 1 (Lipschitz reference score, π_ref and every p_t strongly log-concave, 2C_p < C_ref < 2C_ref⁻ + 2C_p) and
  Assumption 2 (sup_x L² error of s_N ≤ C_e(t)/N^r, "typically r = 1/2"). Cor. 1: with N^{r−c} = C̄_e(t,T) and
  T(t) = t + δ, W₂ → 0. Remark 2: with a Gaussian reference, N need grow only polynomially in T (OT resampling:
  exponentially in 1/ε). Continuous-time analysis only, discretisation not covered (§3). Consistent, **not unbiased**
  (Table 20).
- **Cost:** O(KN) per re-sample, parallel over particles (Table 20); one N-term softmax per score call.
- **Knobs:** b ("how much we rely on π_ref"; b = 0 means samples come from π_ref alone, App. C last paragraph); π_ref
  (moment-matched Gaussian recommended, §2.2); T; K; integrator (Euler–Maruyama, Jentzen–Kloeden, Lord–Rougemont,
  Tweedie; SDE or probability-flow ODE). Experiments use b² = Σ_N "not necessarily optimal" (App. F). App. N: "K ≤ 8 is
  often sufficient for learning", keep K < N.
- **Breaks when:** coarse K with SDE integrators: Gaussian-mixture test (d = 8, N = 10 000), T = 3, K = 8: EM-SDE SWD
  5.60, JK-SDE 8.62, JK-ODE 2.53 vs multinomial 0.82; T = 1, K = 8, JK-ODE 1.64; only K = 128 matches multinomial
  (Table 3, App. G: "ODE ... is better than SDE, especially when K is small"). Non-Gaussian targets need long T
  (App. P). Score explodes as t → 0 (§2.3). Gradients through the solver are numerically sensitive (§6). On the
  linear-Gaussian SSM, T = 1, K = 4 already beats OT and multinomial on all three metrics (Table 2).
- **Hooks:** any resampling step of an SMC; any "refit a Gaussian, then resample" step of a population optimiser
  (CEM/MPPI/DIAL) — see the next two cards.

### diffusion-resampling-paper: the ensemble score is SNIS of a Tweedie mean (Doob h-function view)

- **Computes:** the score of the noised weighted empirical measure, and the law the implementable reversal reaches.
- **How:** "the ensemble score ... is exactly a self-normalised importance sampling, where π is the proposal,
  π(x₀ | x_t) ∝ p_{t|0}(x_t | x₀) π(x₀) is the target, and ∇log p_{t|0}(x_t | x₀) is the test function" (§3, after
  Assumption 2). Remark 1 (7): s_N = ∇log Σ_i h_i(x,t), h_i = w_i p_{t|0}(x | X_i), a Doob h-function. App. D (30):
  the reversal started at π_ref ends at Σ_i γ_i(u) δ_{X_i} with γ_i(u_T) = w_i ∫ π_ref(u₀) p_{T|0}(u₀ | u_T)/p_T^N(u₀) du₀,
  "an importance sampling upon π^N" with an informative proposal; if π_ref = p_T^N then γ_i = w_i (exact multinomial
  resampling, reparametrised). App. E (32)–(33): |π*^N(φ) − π^N(φ)|² ≤ π^N(φ²) χ²(π_ref ‖ p_T^N).
- **Guarantee:** exact identities; χ² bound on the resampling map.
- **Cost:** none beyond the score.
- **Knobs:** π_ref, T (they set γ_i).
- **Breaks when:** χ²(π_ref ‖ p_T^N) is large (reference far from the noised empirical law).
- **Hooks:** the same SNIS estimates the Monte Carlo score of MBD/DIAL with the roles of proposal and weight swapped
  (identity in the session file).

### diffusion-resampling-paper: moment-matched mean-reverting reference and exponential integrators

- **Computes:** a closed-form forward kernel p_{t|0}(x | x₀) = N(m_t(x₀), V_t), m_t = x₀ e^{−b²Σ_N⁻¹t} +
  μ_N(1 − e^{−b²Σ_N⁻¹t}), V_t = Σ_N(1 − e^{−2b²Σ_N⁻¹t}) for ∇log π_ref = −Σ_N⁻¹(x − μ_N) (9)–(10), μ_N, Σ_N the weighted
  particle moments; semi-linear reverse SDE (11)–(12) integrated by Jentzen–Kloeden or Lord–Rougemont (§2.3).
- **Guarantee:** none beyond Prop. 1; Cor. 1 favours π_ref close to π.
- **Cost:** Σ_N⁻¹ (diagonal or precision-matrix estimate suggested, §2.2).
- **Knobs:** reference may be any Gaussian filter output (UKF etc.) (§2.2).
- **Breaks when:** multimodal targets (Gaussian-mixture reference needs an approximate semigroup, §2.2).
- **Hooks:** with b² = Σ_N and a := e^{−t}: p_{t|0}(· | X_i) = N(aX_i + (1−a)μ_N, (1−a²)Σ_N), the Liu–West shrinkage
  kernel (inferred from (10); the brief's pilot confirms numerically, F11).

### diffusion-resampling-paper: differentiable SMC with diffres (Alg. 2)

- **Computes:** a particle approximation of a parametrised Feynman–Kac model Q^θ_{0:J} ∝ Π_j M_j^θ G_j^θ (8) and the
  marginal-likelihood estimate L(θ) = Π_j L_j(θ), L_j = Σ_i w_{j−1,i} G_j (Alg. 2 l. 12–16), differentiable in θ.
- **How:** bootstrap SMC; diffres at the resampling step, reference built from the current posterior particles rather
  than the predictive ones (§2.1).
- **Guarantee:** none stated for L(θ). Because diffres does not satisfy the unbiased-offspring condition of PMCMC
  (23), L(θ) is not the unbiased SMC estimator (inferred).
- **Cost:** 32 particles suffice on the linear-Gaussian SSM (§4.2).
- **Numbers:** Table 2: log-likelihood error 2.55–2.61 (diffusion) vs 2.80 multinomial, 2.64–2.75 OT; parameter
  error 1.28 vs NaN (multinomial, Gumbel, soft divergent under L-BFGS).
- **Hooks:** gradient-based tuning of anything upstream of a filter (planner parameters, model parameters).

---

## DiffPF (Wan & Zhao, IEEE RA-L 2026)

### diffpf-paper: conditional-diffusion measurement update (learned posterior sampler, equal weights)

- **Computes:** N equally weighted particles from p(x_t | c_t), taken as post(x_t) (4)–(5); c_t = Fusion(g_obs(o_t),
  predicted particles) (3).
- **How:** propagate through f_dyn (1); DDPM reverse from N(0, I) with ε_θ(x, k, c_t) (6)–(7); estimate = particle
  mean (8); everything trained end-to-end with the DDPM loss (9) on ground-truth states.
- **Guarantee:** none; (4) is an approximation. diffres §5: a trained conditional diffusion "introduces bias, breaks
  consistency guarantees, and adds substantial computational cost".
- **Cost:** 10 particles, 10 diffusion steps, 3-layer U-Net; 52.6 Hz at N = 10 and 14.3 Hz at N = 80 on an RTX 4080
  (Table V); 1000 training epochs.
- **Knobs:** N, steps, fusion design, prior noise.
- **Breaks when:** the prior (predicted particles) is badly wrong: RMSE 106.4/61.7/67.2 at 10Σ vs 6.1/7.6/15.3 nominal,
  collapse onto wrong trajectories (Table III, Fig. 6); without the prior 137.0/213.0/414.6. Conclusions propose
  weighted variants against collapse and mode dropping.
- **Hooks:** a learned sampler of nature's state conditioned on a summary — the same design as a belief-conditioned
  PREDICT.

---

## Particle MCMC (Andrieu, Doucet & Holenstein, JRSS-B 2010, with discussion)

### andrieu-pmcmc-2010-paper: the SMC normalising-constant estimator (unbiased evidence)

- **Computes:** Ẑ^N = Π_{n=1}^P (1/N) Σ_k w_n(X^k_{1:n}) for a sequence of unnormalised targets γ_n, π_n = γ_n/Z_n
  (§4.1 (20)–(21)); SSM case p̂_θ(y_{1:T}) = Π_n p̂_θ(y_n | y_{1:n−1}), p̂_θ(y_n | y_{1:n−1}) = (1/N)Σ_k w_n (9).
- **How:** generic SMC on any bridging sequence {π_n}, "models which do not have such a structure and for which the user
  induces such a structure (e.g. Chopin (2002) and Del Moral et al. (2006))" (§4 intro) — i.e. tempering ladders are
  in scope.
- **Guarantee:** unbiased, E Ẑ^N = Z, if resampling satisfies E(O^k_n | W_n) = N W^k_n (23) (multinomial, residual,
  stratified) and the support condition (Assumption 1/5) holds — Del Moral (2004) Prop. 7.4.1, cited in §5.1.
  Thm 1: V(Ẑ^N/Z) ≤ C(P)/N under bounded weights (Assumption 3), and C(P) = CP if weights are also bounded below and
  the kernels mix (Assumption 4, "forgetting"); otherwise C(P) "typically exponential" in P. log Ẑ is biased
  (inferred, Jensen).
- **Cost:** N particles × P steps.
- **Knobs:** N, proposals M_n, resampling scheme, the bridging sequence.
- **Breaks when:** no forgetting (static parameters, quasi-deterministic states): authors' reply expects N superlinear
  in T; a few outlier weights dominate Ẑ (reply, citing Murray et al.). Indicator potentials violate the lower bound
  w̲ > 0 of Assumption 4, so the linear-in-P variance bound does not apply to them (inferred).
- **Hooks:** filter evidence as a surprise signal; the probability of a path event written as a Feynman–Kac
  normalising constant with indicator potentials (inferred, see session identities).

### andrieu-pmcmc-2010-paper: particle independent Metropolis–Hastings (PIMH)

- **Computes:** a Markov chain on x_{1:P} using whole SMC runs as independent proposals; accept with 1 ∧ Ẑ*/Ẑ (11), (29).
- **Guarantee:** Thm 2: an exact IMH on the extended space with target (31) for any N ≥ 1 (Assumption 2 only); Thm 3:
  ergodic; geometric with rate ρ_P if sup Ẑ/Z < ∞ (Assumption 3) — "ρ_P is ... independent of N".
- **Cost:** T = 100, σ_V² = σ_W² = 10: acceptance 0.80 at N = 2000 vs 0.27 at N = 200; authors prefer N = 200 and more
  iterations (§3.1, Fig. 3).
- **Knobs:** N.
- **Breaks when:** informative observations with prior proposals (lower acceptance, Fig. 3b).
- **Hooks:** accept/reject of whole candidate populations by their evidence ratio.

### andrieu-pmcmc-2010-paper: particle marginal Metropolis–Hastings (PMMH) and the pseudo-marginal principle

- **Computes:** samples of π(θ, x_{1:P}) ∝ γ(θ, x_{1:P}) by MH on θ with γ(θ) replaced by its SMC estimate (13), (35).
- **How:** propose θ* ~ q(· | θ), run a fresh SMC for θ*, accept with 1 ∧ [γ̂^N(θ*) q(θ | θ*)]/[γ̂^N(θ) q(θ* | θ)];
  on rejection keep the stored γ̂ of the current state (§2.4.2 Step 2(c)).
- **Guarantee:** Thm 4: for any N ≥ 1, an exact MH on the extended space with target (36) whose marginal is
  π(θ, x_{1:P}); convergent under Assumptions 5 (support) and 6 (the ideal MH is irreducible, aperiodic). The
  two-line proof (§5.1, after Andrieu et al. 2007): let U ~ ψ^θ be all auxiliary variables of the SMC and
  γ̂^N(θ) = γ̂^N(θ, U) "an unbiased positive estimate of an unnormalized version of a target density"; the extended
  target π̃(θ, u) ∝ γ̂^N(θ, u) ψ^θ(u) has π(θ) as θ-marginal, and MH with proposal q(θ*|θ) ψ^{θ*}(u*) gives exactly (35).
  Requirements read off the proof: γ̂ ≥ 0; E_{U~ψ^θ} γ̂(θ, U) = γ(θ) for every θ, for the *unnormalised* target
  (constant factors free); U* drawn afresh from ψ^{θ*}, independent of the current (θ, U); the current estimate
  recycled, never recomputed. Authors' reply: the "pseudosampling" (extended-target) view goes beyond unbiasedness and
  is what also yields x_{1:P} and the particle Gibbs sampler.
- **Cost:** one full SMC per MH iteration; N ~ linear in P for ergodic models (reply); §3.1 uses N = 5000 for T = 500,
  with ACFs no better beyond N = 5000 and poor below 2000 (Fig. 5).
- **Knobs:** N, q(θ* | θ).
- **Breaks when:** the estimator's relative variance is large (sticky chain: a lucky overestimate is rarely left);
  non-ergodic models.
- **Hooks:** any MCMC/annealing over a variable whose target contains an intractable expectation that enters
  *linearly* (session file, Q1).

### andrieu-pmcmc-2010-paper: conditional SMC and the particle Gibbs sampler

- **Computes:** a Gibbs sampler for π(θ, x_{1:P}): θ ~ π(θ | x_{1:P}), then a conditional SMC sweep in which a
  prespecified path with lineage B_{1:P} survives every resampling while N − 1 particles are drawn as usual, then pick
  a path ∝ W_P (§2.4.3, §4.3, §4.5; efficient implementation App. A).
- **Guarantee:** Thm 5: invariant density π̃^N (36) for any N ≥ 1; converges for N ≥ 2 under Assumptions 5–7. The
  naive "sample x from the SMC approximation" Gibbs step is *not* invariant (§2.4.3).
- **Cost:** one SMC sweep per iteration; Fig. 5 ACFs improve up to N = 5000.
- **Knobs:** N, the reference path.
- **Breaks when:** early-time degeneracy leaves no particle in the support of p(x_1 | y_{1:T}) (Chopin's discussion).
- **Hooks:** keeping the previous solution (warm start) as the conditioned reference path is a valid MCMC move for the
  new target (inferred).

### andrieu-pmcmc-2010-paper: reuse of all particles, including rejected populations

- **Computes:** Rao–Blackwellised estimates of E_π f from all weighted particles of every iteration (38), and for PMMH
  also from rejected proposals weighted by the acceptance probability α (39)–(40).
- **Guarantee:** Thm 6: a.s. convergence as the number of iterations L → ∞ (Assumptions 2–5, ergodic chain).
- **Hooks:** do not discard evaluated candidate populations.

### andrieu-pmcmc-2010-paper (discussion, Łatuszyński & Papaspiliopoulos): unbiased estimates simulate events exactly

- **Computes:** a Bernoulli(s) draw from an unbiased estimator Ŝ ∈ [0,1] of s: G₀ ~ U(0,1), output 1{G₀ ≤ Ŝ}
  (algorithm 1); with monotone lower/upper sequences l_n ↗ s, u_n ↘ s, stop as soon as G₀ ≤ l_n or G₀ > u_n
  (algorithm 2); with unbiased estimators L_n ≤ U_n in [0,1] satisfying (46)–(49), or reverse-time super/submartingale
  conditions (50)–(51), algorithm 4 ((52)–(53)) still outputs exactly Bernoulli(s).
- **Guarantee:** exactness under the stated conditions (proofs in Łatuszyński et al. 2009).
- **Hooks:** accept a candidate with exactly its safe probability; use cheap lower/upper bounds (e.g. set enclosures)
  to stop sampling early (inferred).

---

## Box particles (Gning, Ristic & Mihaylova 2012; Haj Chhadé et al. 2014)

### gning-box-bernoulli-2012-paper: box-particle filter (inclusion propagation, contraction, volume-ratio weights, resampling by subdivision)

- **Computes:** the (spatial) posterior as a mixture of uniform pdfs on boxes, s_{k|k}(x) ≈ Σ_i w_k^i U_{[x_k^i]}(x)
  (19) — the uniform reading is taken from their ref. [15].
- **How:** time update [x_{k+1}^i] = [f_{k+1}]([x_k^i]) + [w_k] with an inclusion function and bounded process noise
  (24)–(25), Alg. 2 l. 3, 5. Measurement update: contract each predicted box against each interval measurement to a box
  enclosure of {x ∈ [x] : [z] ∩ (h(x) + [ε]) ≠ ∅} (30) by constraint propagation (Alg. 3, forward–backward on primitive
  constraints); weight w̃ = (p_D/c([z])) w κ |[x̃]|/|[x]| (32), κ = mean generalised likelihood over the contracted box
  (33), "in practice ... κ = 1"; normalise, resample N times, and divide a box selected n times into n smaller boxes
  along a randomly chosen dimension (§V-C, end). Evidence-type integral (34). Estimate = weighted box centres (35),
  covariance adds |[x](j)|²/12 (36).
- **Guarantee:** set-level only: inclusion functions satisfy f([x]) ⊆ [f]([x]) and contraction keeps S ⊆ [x]' ⊆ [x]
  (§V-A), so each contracted box encloses its consistent subset if the noise is truly bounded. No probabilistic
  guarantee; the "inclusion" of the true state in ∪ boxes (38), (44) is checked empirically over 100 Monte Carlo runs.
  Point estimates are biased (§V-C). Resampling drops unselected boxes, so ∪ boxes after resampling need not enclose
  the consistent set (inferred).
- **Cost:** inclusion criterion met with N ≥ 32 box particles and n₀ = 1 newborn box per measurement (~19 s per
  60-scan run, MATLAB) vs point Bernoulli PF n₀ ≥ 5000, N ≥ 2000 (~40 s); "almost hundred time smaller number of
  particles", twice faster despite more work per box (§VII-C, §VIII).
- **Knobs:** N, subdivision rule, noise box [ε] (3σ, i.e. 99 %, used for Gaussian noise), κ, contractor.
- **Breaks when:** the inclusion function is pessimistic (wrapping; grows with nonlinearity and horizon, inferred);
  spread ν_k slightly larger than the point PF (§VII-C); κ = 1 ignores the likelihood shape inside the box.
- **Hooks:** a handful of weighted boxes enclosing a reachable/consistent set; volume ratios as weights.

### gning-box-bernoulli-2012-paper: generalised likelihood of a set-valued (interval) measurement

- **Computes:** g([z] | x) = Pr{h(x) + v ∈ [z]} = ∫_{[z]} p_v(z − h(x)) dz (10); Gaussian noise: a difference of CDFs
  (11)–(13); uniform noise: |[z] ∩ (h(x) + [ε])| / |[ε]| ∈ {1 inside, 0 disjoint, ≤ 1 otherwise} (27)–(28). Not a pdf in
  x; tends to an indicator as Σ → 0 (Fig. 1).
- **Hooks:** soft indicator potentials for set-membership events (probability that a noisy point lies in a set)
  (inferred).

### haj-chhade-box-messages-2014-paper: box-particle belief propagation

- **Computes:** BP messages and beliefs on a graphical model as weighted box mixtures, read as mixtures of uniforms
  (§5.3, "a set of boxes constitute a direct approximation of the pdf").
- **How:** product of incoming messages: every tuple of boxes gives the intersection box with weight
  Π ω · |∩ boxes| / Π |box| (5.11)–(5.13), Alg. 1 (exact for products of uniforms); contraction by the local
  observation and re-weighting by the volume ratio (Alg. 2; Box-PF likelihood L = Π_j |[x̃(j)]|/|[x(j)]|, §5.2);
  propagation through a pairwise potential x_s = f(x_t, e, v) with an inclusion function, support approximated by
  [f]([x], [v], [e]) (5.16)–(5.17); weights divided by box volume, then normalised (Alg. 3 l. 4–6).
- **Guarantee:** support containment (5.16) under bounded noise; none probabilistic.
- **Cost:** up to N^d product terms (5.13), far fewer in practice. Sensor-network calibration (100 nodes): 9 boxes (45
  floats) vs NBP 200 particles (600 floats); 14.54 s vs 159.4 s; RMSE 2.11 % vs 2.08 % of L (Table 1); random anchors
  2.06–2.53 % vs NBP 6.89–12.23 % (Tables 2–3).
- **Breaks when:** many neighbours (combinatorial products); dynamic models not treated (§8).
- **Hooks:** the product of two box beliefs is the intersection of their supports with a computable weight — the way
  to combine a belief with a set constraint (e.g. a safe set) (inferred).

---

## Set-membership and imprecise-probability filtering

### benavoli-piga-2016-paper: set-membership filtering is filtering of the credal set of all measures supported on the set

- **Computes:** the state uncertainty set 𝒳_k (Problem 1) as the support of 𝒫_{𝒳_k} = {P : ∫_{𝒳_k} dP = 1} (6),
  equivalent for inferences to Co{δ_x : x ∈ 𝒳_k} (8).
- **How:** Prop. 1: sup_{P ∈ 𝒫_𝒳} E_P g = sup_{x∈𝒳} g(x), attained by a Dirac. Thm 1 (prediction): Chapman–Kolmogorov
  applied pointwise to Diracs gives 𝒳̂_k = {a_d(x) + w : x ∈ 𝒳_{k−1}, w ∈ 𝒲_{k−1}} (9)–(11). Thm 2 (update): Bayes'
  rule applied to the measures with positive denominator (Walley's regular extension, footnote 6) gives
  𝒳_k = 𝒳̂_k ∩ 𝒴_k (13)–(15). Alg. 1.
- **Guarantee:** exact equivalence with set-membership estimation. Statement (§1): set-membership "cannot be
  interpreted in the Bayesian framework, but only in the framework of set of probability measures"; imposing a uniform
  distribution on the set (as in Fernandez-Canti et al. and in the box-particle papers [33, 34]) is "different from
  set-membership estimation" (footnote 3: "we loose the full equivalence"). Remark 3: valid for any compact sets and
  non-polynomial systems; polynomiality is only for computation.
- **Cost:** see next card.
- **Breaks when:** any event the set neither contains nor excludes has lower probability 0 and upper probability 1
  (consequence of Prop. 1, inferred).
- **Hooks:** Remark 2: the probabilistic reading allows hybrid filters mixing bounded and stochastic noise, credible
  regions, and decisions minimising expected loss ("important ... in control design") — announced, not done.

### benavoli-piga-2016-paper: convex outer bounds as sets of means; SOS duality; minimum-volume polytope

- **Computes:** polytopic outer approximations of 𝒳_k.
- **How:** Thm 3: the minimum-volume convex Ω with P(Ω) = 1 for all P ∈ 𝒫 equals 𝓜 = {∫ x dP : P ∈ 𝒫} = conv(𝒳_k)
  (21)–(22). Thm 4: the tightest box from lower/upper means of each coordinate (26). Thm 5: the tightest half-space
  ω^T x ≤ ν*, ν* = max_P ∫ ω^T x dP (28), dual (29): ν − ω^T x ≥ 0 on 𝒳, relaxed by sum-of-squares (§5.1); greedy
  half-space selection and refinement (§6, Alg. 2–3).
- **Guarantee:** outer approximation (SOS relaxation is conservative, inferred standard).
- **Cost:** 28 s per polytope (2-D Lotka–Volterra, ≤ 8 half-spaces, SOS degree 4, SeDuMi) (§7); polynomial dynamics
  and semialgebraic sets required.
- **Breaks when:** real-time use (authors' future work); growth of SOS size with dimension (inferred). Boxes propagated
  instead of polytopes are visibly more conservative (Figs. 6–8).
- **Hooks:** polytopic enclosures of consistent/reachable sets with an expectation reading.

### benavoli-lower-previsions-2011-paper: robust filtering with coherent lower previsions

- **Computes:** lower/upper posterior expectations E̲[g(x_t) | ỹ^t], Ē = −E̲[−g], over closed convex sets of priors,
  transitions and likelihoods.
- **How:** generalised Bayes rule (6): E̲[g | y] is the μ solving E̲_joint[I_y (g − μ)] = 0, equal to the infimum over
  posteriors (7) when the lower probability of y is positive (measurements discretised to neighbourhoods). The joint
  comes from marginal extension under epistemic irrelevance (Lemma 1, (11)–(13)). Thm 2: backward recursion
  g_{k−1} = E̲_{X_k}[ g_k (I_{g_k≥0} E̲[I_{ỹ_k} | X_k] + I_{g_k<0} Ē[I_{ỹ_k} | X_k]) | x_{k−1} ] from k = t to 1 (16),
  then solve E̲_{X_0}[g_0] = 0 for μ. Cor. 1 recovers Bayes (20), (25).
- **Guarantee:** exact lower envelope, jointly coherent with all assessments.
- **Cost:** no forward recursion in the imprecise case: at every time the functional is propagated back to x_0 and μ
  root-found ("each step can be heavy", §IV); suggested cure: truncate after N past steps with a conservative prior.
  Vertex-based alternatives grow exponentially with time (§I).
- **Knobs:** the credal sets; truncation depth.
- **Breaks when:** general credal sets (only special classes are tractable, §V–VI).
- **Hooks:** IP credibility region: minimum-volume χ with E̲(I_{x∈χ}) > 1 − α (§IV-A); robust (lower/upper)
  probabilities of events.

### benavoli-lower-previsions-2011-paper: interval-mean Gaussian (unknown bounded bias) → Kalman filter with a linear shift

- **Computes:** E̲[g | ỹ^t] = min_{θ_{1:t} ∈ [θ^L, θ^U]^t} ∫ g(x) N(x; x̂_t − M_t[θ^t], P_t) dx (30), with
  M_t[θ^t] = Σ_i [Π_{j>i}(1 − L_j C)A] L_i θ_i (31) linear in the biases and x̂_t, P_t, L_t from the standard KF
  (Thm 3).
- **Hooks:** a bounded unknown mean (e.g. mean wind) gives a set of Gaussian posteriors whose means form the linear
  image of a box (a zonotope) (inferred).

### benavoli-lower-previsions-2011-paper: linear-vacuous mixture (ε-contamination) filter (LGVM)

- **Computes:** E̲(g) = ε ∫ g N + (1 − ε) inf g for prior and transition (38)–(40); Thm 4 (42)–(43): the recursion of
  Thm 2 with Kalman-type integrals ("I" operators) and infimum terms ("M" operators), expanded in (44)–(48); the number
  of terms grows with t (inferred from (46)).
- **Numbers:** 15-step tracks, 100 Monte Carlo runs; with an unmodelled 5-unit jump at t = 7 the KF's 99 % interval
  misses the state while the LGVM interval widens to include it; for an unobservable component the upper mean becomes
  vacuous (hits the state bound 30) (§VII, Figs. 1–4).
- **Hooks:** one number that mixes a probabilistic nominal and a set-valued worst case: for an event A,
  Ē(1_A) = ε P_nom(A) + (1 − ε) sup 1_A (inferred from (38) with g = 1_A).

### greco-vasile-2022-paper: precomputed sequential importance sampling — re-weight once-propagated particles across an epistemic set

- **Computes:** θ̂(χ_{0:M}; λ) = Σ_i ŵ_M^i(λ) φ(x^i_{0:M}) for any epistemic parameter λ ∈ Ω_λ of prior, transition and
  likelihood (4)–(5), (10)–(11), from one propagated particle set; robust bounds (6a)–(6b) = min/max over λ.
- **How:** draw and propagate particles once from a λ-independent proposal π, store particles, proposal densities and
  φ values (Alg. 1); for each λ only recompute w_k^i(λ) = ŵ_{k−1}^i p(y_k | x_k^i; λ_y) p(x_k^i | x_{k−1}^i; λ_x)/π_k^i
  and self-normalise (Alg. 2).
- **Guarantee:** per-λ SNIS consistency; "asymptotically unbiased, but for a small sample size the bias could be
  significant"; resampling is impossible inside the precomputed estimator (§II.B.2).
- **Cost:** precomputation O(N + MN) including MN propagations (14); per λ O(N + M + MN) density evaluations and no
  propagation (15); wall time linear with an MN interaction (Table 4, R² = 0.972).
- **Knobs:** proposal, N (50 000 used; < 1 % change beyond).
- **Breaks when:** the λ-posteriors move away from the proposal (ESS collapse); no resampling.
- **Hooks:** evaluate a probability of an event for many model parameters from the same rollouts.

### greco-vasile-2022-paper: a proposal that covers the epistemic set (mixture of UKF posteriors)

- **Computes:** π(x_k | x^i_{k−1}, y_{1:k}) = Σ_j b_j N(μ_k^{(i,j)}, Σ_k^{(i,j)}) (13): one UKF update per sampled
  epistemic likelihood (low-discrepancy sequence, Gaussianised (12)), initial proposal a mixture over the epistemic
  prior set (Alg. 3); polynomial surrogate of the flow for cheap propagation (16)–(18).
- **Numbers:** ESS > 75 % at the last step (instance B, §III.C.2).
- **Hooks:** proposal design for re-weighting across a parameter set.

### greco-vasile-2022-paper: Lipschitz simplex branch-and-bound for lower/upper expectations

- **Computes:** min/max_λ θ̂(χ; λ) (19) to a tolerance ε.
- **How:** simplex partition of Ω_λ; lower bound lb(S) = min_{λ∈S} max_j θ̂(λ_j) − L‖λ − λ_j‖ (23)–(24), upper bound =
  best vertex (25); longest-edge bisection (28); Lipschitz constant from analytic gradients at vertices (32), a lower
  approximation that "could lead to over-pruning".
- **Guarantee:** Thm 1: finite convergence to within ε of the global minimum of the *estimator* θ̂ (not of the true
  bound); K ≤ N₀ n_λ ⌈log_{2/√3}(σ₀/δ)⌉ splits (29); complexity (31) ≈ 2[N₀(n_λ + 1) + K] C_pSIS. A confidence
  interval for the bound estimator from 2l replicate particle sets (20)–(21), assuming small bias.
- **Cost (Table 5, MATLAB, dual-core i7, N = 50 000):** n_λ = 2: 1023 pSIS calls, 80 s optimisation, 2.6 min total;
  n_λ = 4: 903–2774 calls, 4.9–7.7 min; n_λ = 8: 4140–7376 calls, 16–28 min; n_λ = 10: 9752–13 043 calls, 29–35 min.
  Surrogate construction 76–160 s.
- **Numbers:** PoC (50 m) intervals: no measurements [0, 4.97·10⁻⁵]; collision case [0, 2.15·10⁻⁴] at 24 h → [0, 9.69·10⁻³]
  at 9 h; no-collision case [0, 2.82·10⁻⁴] → [0, 0]; simulated future measurements up to [1.20·10⁻⁸, 0.994].
  "lower and upper distributions are not lower and upper envelopes for the ECDFs" — bounds are per quantity of
  interest (§III.C.1).
- **Breaks when:** epistemic dimension grows (initial triangulation n_λ! simplices; time rises "sharply").
- **Hooks:** upper collision probability over a parameter set by weight tuning.

### raices-cruz-robust-is-mcmc-2022-paper: iterative importance sampling over a set of priors, with MCMC samples

- **Computes:** E̲(f) = min_{t∈𝓜} ∫ f p_t (25), estimated by min_t of SNIS with w_t = p_t/q (26), q the posterior at
  the current hyperparameter t′ sampled by MCMC (33)–(34).
- **How:** Steps 1–5 (§4): MCMC at t until ESS_MCMC exceeds the target by 20 %; optimise t* on the re-weighted sample
  (simulated annealing); stop if ESS > ESS_target, else rerun MCMC at t*. ESS with correlated samples
  ESS ≈ (ESS_MCMC/N) · ESS_IS (24), from a delta-method variance (8)–(23).
- **Guarantee:** none on the bound beyond SNIS consistency; existence of the minimum shown for the example (App. C).
- **Cost:** 2–3 iterations, 12–24 min, bound 12.1 vs grid search 12.09 in 11.45 h (4 773 grid points) vs simulated
  annealing with an MCMC rerun per evaluation 12.13 in > 20 h (Tables 1–3); prior–data conflict case 13 min vs 3.7 h
  (Table 4).
- **Knobs:** ESS_target, MCMC length.
- **Breaks when:** the optimum is far from t′: first-iteration ESS 27 of 20 000 and 5 of 40 000 (Tables 1, 3);
  convergence not guaranteed (cap 10 000 iterations); demonstrated on a 2-D hyperparameter set only.
- **Hooks:** re-centre the proposal when re-weighting degenerates; the ESS formula (24) for correlated (MCMC or
  annealing-chain) samples.
