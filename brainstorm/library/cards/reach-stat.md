# Mechanism cards — lens `reach-stat` (statistical and scenario-based reachability)

Scout pass of 2026-10-06 (session `2026-10-06_tro2027-diffusion-control`). Eleven skills under
`~/.claude/skills/<name>/references/paper.md`. Citations are `skill §section (eq. n)` or `Alg. n`. Anything the
scout inferred rather than read is marked "(inferred)".

Notation used across cards: ε = violation level (the set misses at most ε of the probability mass), β or δ =
confidence parameter (the statement fails with probability at most β over the samples). Papers disagree on
symbols: Devonport and Tebjou use δ for confidence; Dietrich, Hewing and Lin use β; Hewing writes p = 1 − ε;
Hashemi uses δ and Δ for *coverage* (1 − ε) and gives only marginal guarantees (no confidence layer).

## Sample-count formulas in one place

| Formula | Source | Decision may use the same samples? |
|---|---|---|
| N ≥ (1/ε)(e/(e−1))(ln(1/δ) + n_θ) | devonport2020 §3 (5), Thm 1 (Tempo Cor. 12.1) | yes (convex scenario program) |
| C(N_k+d−1, N_k) Σ_{i=0}^{N_k+d−1} C(N_s,i) ε^i (1−ε)^{N_s−i} ≤ β | hewing2019 §II-C (6), Thm 1 (Campi–Garatti 2011) | yes, plus N_k discarded samples (Assumption 1) |
| N_k ≤ εN_s − d + 1 − sqrt(2εN_s ln((εN_s)^{d−1}/β)) | hewing2019 (7) | sufficient condition for (6) |
| N_s ≥ (2/ε)((d−1) ln 2 − ln β) | hewing2019 (8) | no discarding |
| N ≥ (5/ε)(log(4/δ) + C(n+2k,n) log(40/ε)) | devonport2021 Thm 1 (1); devonport2023 (3.1) | yes (VC bound for consistent sets) |
| ε(s) = 1 − (β/(N C(N,s)))^{1/(N−s)}; convex: β/(d C(N,s)) for s < d | dietrich2024 Thm 1 (2), (4) | yes (a posteriori, by support count s) |
| ε = max{e : Σ_{j≤k} C(M,j) e^j (1−e)^{M−j} ≥ β}; k=0: ε = 1−β^{1/M} ≤ ln(1/β)/M | dietrich2025 Def. 1 (7)–(8), Thm 1 (9); lin2024 (2), (5) | no (fresh holdout, decision fixed) |
| P(μ(C) ≥ δ^{1/N}) ≥ 1−δ, N = calibration size | tebjou2023 Thm 4 (10) | no (split) |
| conf. ≥ Σ_{i=p+1}^{N−p} C(N−p,i) ε^i (1−ε)^{N−p−i} with ≤ p outliers | tebjou2023 Thm 5 (14) | no (split) |
| ℓ = ⌈(L+1)δ⌉ ≤ L (marginal coverage δ); robust: ℓ* = ⌈(L+1)(1+1/L)(δ+τ)⌉ | hashemi2023 §3.2; hashemi2025 (4) | no (split) |
| K ≥ −ln β/(2δ²) (additive accuracy δ of a probability) | sartipizadeh2019 Thm 1 (13) | claimed yes; see card |
| PAC-Bayes: D_ber(r̂_Q‖r_Q) ≤ (KL(W_Q‖W_P) + log((N+1)/δ))/N | devonport2023 Thm 3.5 (3.2) | yes (prior fixed in advance) |

Computed by the scout (scipy) for the orchestrator:

| | ε=1e-2, β=1e-2 | ε=1e-2, β=5e-2 | ε=1e-3, β=1e-2 | ε=1e-3, β=5e-2 |
|---|---|---|---|---|
| Holdout / Clopper–Pearson, 0 violations | 459 | 299 | 4,603 | 2,995 |
| same, 1 / 5 / 10 violations | 662 / 1,307 / 2,010 | 473 / 1,049 / 1,693 | 6,636 / 13,105 / 20,140 | 4,742 / 10,511 / 16,959 |
| Exact scenario (6), N_k=0, d=1 (scalar threshold) | 459 | 299 | 4,603 | 2,995 |
| same, d=2 / d=5 / d=12 / d=27 | 662 / 1,157 / 2,144 / 4,047 | 473 / 913 / 1,818 / 3,603 | 6,636 / 11,601 / 21,485 / 40,528 | 4,742 / 9,151 / 18,204 / 36,072 |
| Tempo bound (5), d=1 / d=27 (6-D ellipsoid) | 887 / 5,000 | 633 / 4,746 | 8,868 / 49,999 | 6,322 / 47,453 |
| Hewing (8), d=1 / d=27 | 922 / 4,526 | 600 / 4,204 | 9,211 / 45,254 | 5,992 / 42,036 |
| VC Christoffel, n=2, k=1 (C=6) / k=2 (C=15) | 27,878 / 65,202 | 27,074 / 64,397 | 347,857 / 824,705 | 339,810 / 816,658 |
| Hoeffding (13), additive accuracy = ε | 23,026 | 14,979 | 2,302,586 | 1,497,867 |
| Clopper–Pearson, 0 violations, Bonferroni over 64 / 1024 candidates | 873 / 1,148 | 712 / 988 | 8,760 / 11,531 | 7,152 / 9,923 |

Wait-and-judge ε(s) at β=1e-2 (dietrich2024 (2)): N=1000: s=1 → 0.018, s=5 → 0.041, s=20 → 0.104; N=3000:
s=1 → 0.0069, s=5 → 0.016; N=10000: s=1 → 0.0023, s=20 → 0.015. The factor N·C(N,s) makes it looser than a
holdout of the same size.

---

## devonport2020estimating-paper

### devonport2020: Scenario norm-ball reachable set

- **Computes:** a p-norm ball R̂(A,b) = {x : ‖Ax − b‖_p ≤ 1} at one time t_1 that holds at least 1−ε of the mass
  of Z = Φ(t_1; t_0, X_0, U, D) with confidence 1−δ.
- **How:** minimum-volume scenario program: min −log det A s.t. ‖A z^(i) − b‖_p ≤ 1 for all N samples (Alg. 1,
  (8)); chance-constrained target (7). Axis-aligned variant: diagonal A, n_θ = 2n (11); p = ∞ with diagonal A is the
  elementwise min/max box of the samples (§4.2).
- **Guarantee:** Thm 2 (9)–(10): P_S(P_Z(R̂) ≥ 1−ε) ≥ 1−δ when N = ⌈(1/ε)(e/(e−1))(log(1/δ) + n(n+1)/2 + n)⌉,
  from Thm 1 (5) (Tempo et al. Cor. 12.1). Assumes J and g convex in θ, Θ convex compact, i.i.d. samples, a minimizer
  exists. The set is chosen from the same samples (no split). The guarantee is with respect to the sampling
  distribution of (X_0, U, D), which may be instrumental; it is neither an over- nor an under-approximation (§4.1).
- **Cost:** n=6, ε=0.05, δ=1e-9: N=1510 (full A), 1036 (diagonal); sampling 76/52 min, solve 24/14 s; a posteriori
  check with 46,052 samples gave measures 0.993–0.998 (Table 1).
- **Knobs:** set family (p, structure of A), ε, δ; N scales O(n²) (full) or O(n) (diagonal).
- **Breaks when:** the set must be convex in x and the program convex in θ (§6); samples must be i.i.d., so active
  or adaptive sampling is excluded (§6). One time instant only. Non-convex reachable sets (e.g. a window) are
  covered by their convex hull (inferred).
- **Hooks:** a box or ellipsoid around rollout endpoints at a fixed prediction step; the box (p=∞, diagonal) is the
  per-coordinate min/max of the rollouts, so it costs nothing beyond the rollouts already drawn.

## devonport2021data-paper

### devonport2021: Empirical inverse Christoffel sublevel set (VC bound)

- **Computes:** a compact, possibly non-convex and multiply connected set {x : C(x) ≤ α} containing at least 1−ε of
  the mass of the reachable-state distribution μ at time t_1.
- **How:** C(x) = z_k(x)ᵀ M̂⁻¹ z_k(x), M̂ = (1/N) Σ z_k(x^(i)) z_k(x^(i))ᵀ (monomials of degree ≤ k);
  α = max_i C(x^(i)) (Alg. 1). α is also the solution of min α s.t. C(x^(i)) ≤ α (§III), a one-variable scenario
  program on a fixed score.
- **Guarantee:** Thm 1: if N ≥ (5/ε)(log(4/δ) + C(n+2k, n) log(40/ε)) (1), then μ^N(μ({C ≤ α}) ≥ 1−ε) ≥ 1−δ. Proof:
  the set is in Pos(V) with V the degree-2k polynomials, VC dimension C(n+2k, n) (Lemma 1), and has zero empirical
  error (Lemma 2). Same samples fit C and set α. (Tebjou 2023 relabels this "Conjecture 1" because the samples
  are reused; the scout reads Lemma 2 as the standard consistent-learner bound, which holds for every set in the
  class with zero empirical error and so covers a data-chosen set (inferred).)
- **Cost:** Duffing n=2, k=10, ε=0.05, δ=1e-9: N=156,626 (39 min laptop, 41 s on 96 cores). Planar quadrotor,
  full n=6, k=4: N=2,009,600; reduced to (x,h) n=2: N=32,292 (78 s vs 77 min). A posteriori accuracy
  1 − 2×10⁻⁵ against the guaranteed 0.95, so the bound is conservative (§IV-A, §V).
- **Knobs:** order k; reduced-state variant, i.e. fit only the coordinates the safety specification needs
  (Remark 2).
- **Breaks when:** C(n+2k, n) grows fast with n and k, so the sample count explodes; the bound is loose by orders of
  magnitude; the kernel extension has no finite-sample proof in this paper (§V).
- **Hooks:** a nonconformity score for rollout clouds in the position plane (n=2).

## devonport2023data-paper

### devonport2023: Regularized polynomial Christoffel estimator with VC bound (Alg. 3.1)

- **Computes:** as devonport2021, with M̂_{m,σ} = σ²I + (1/N) Σ z_m z_mᵀ (2.3).
- **How:** Alg. 3.1; α = max_i C(x_i).
- **Guarantee:** Thm 3.4 (VC; N from (3.1) with d = C(n+2m, n)).
- **Cost:** ε=0.1, δ=1e-9: N=70,307 (Duffing, m=10), 14,587 (quadrotor reduced, m=4) (Table 1).
- **Knobs:** m, σ0².
- **Breaks when:** as devonport2021.
- **Hooks:** baseline (already in F6: Christoffel + LTT 0.770 IoU).

### devonport2023: Kernelized Christoffel = GP posterior variance

- **Computes:** κ⁻¹(x) = k(x,x) − k_D(x)ᵀ(σ0²I + K)⁻¹ k_D(x) (2.6)–(2.7), which is the posterior variance of a GP
  with kernel k conditioned on observations y_i = 0 at the samples with noise σ0² (3.4)–(3.5). The support estimate
  is {κ⁻¹ ≤ η}.
- **How:** matrix inversion lemma (2.4)–(2.5) turns the polynomial Christoffel function into a kernel expression;
  replace the inner product by any positive definite kernel.
- **Guarantee:** VC is unavailable (infinite VC dimension for some kernels); see the PAC-Bayes card.
- **Cost:** O(N³) for K; Nyström rank r (3.12)–(3.13) and a top-eigenvalue upper bound on the KL (3.16) reduce cost.
- **Knobs:** kernel and length scale ℓ, σ0², threshold η (chosen in advance; η=0.15 for the SE kernel,
  η = C(n+2m,n)/ε for polynomials by Markov's inequality, Remark 3.12).
- **Breaks when:** N is large (cubic); η must be fixed before the data.
- **Hooks:** an alternative to a KDE score on generated samples: GP posterior variance given the generated states.

### devonport2023: Anytime PAC-Bayes certificate (Alg. 3.2 / 3.3)

- **Computes:** a data-dependent bound ε^i on the missed mass of {κ⁻¹ ≤ η}, valid simultaneously for all batches i.
- **How:** prior C_P = {g_p² ≤ η}, posterior C_Q = {g_q² ≤ η} with g a GP (3.3), or W_P ~ N(0, σ0⁻²I),
  W_Q ~ N(0, M̂⁻¹) in the polynomial case (3.9). Empirical stochastic risk r̂_Q = (1/N) Σ (1 − F_1(η/κ⁻¹(x_i)))
  (3.6), F_1 the χ²₁ CDF (3.7). Upper bound r̄ by inverting the Bernoulli KL (3.8)/(3.11). Central concept risk
  ≤ r_Q/(1 − F_1(1)) ≈ 3.15 r_Q (Lemma 3.9). Batches are added until ε^i ≤ ε, with confidence split
  6δ/(π²i²) across iterations (proof of Thm 3.6).
- **Guarantee:** Thm 3.6: P(∀i ≥ 1: P_X({C^i ≤ η}) ≥ 1 − ε^i) ≥ 1 − δ; Cor. 3.11 for the polynomial case. Can stop
  at any time. Termination requires the KL to grow as o(N), which is not proven.
- **Cost:** ε=0.1, δ=1e-9: Alg. 3.3 needs 11,000 (Duffing), 6,000 (quadrotor), 10,000 (traffic) samples against
  70,307 / 14,587 / 70,307 for the VC version; Alg. 3.2 needs 30,000–35,000 with 325–506 s (Table 1).
- **Knobs:** initial sample size N_0, batch size N_b, η, kernel.
- **Breaks when:** the KL term grows linearly (no termination); the factor 3.15 of Lemma 3.9 is a fixed loss.
- **Hooks:** an anytime stopping rule for "how many samples to draw", with the union over stopping times already
  paid for.

## dietrich2024nonconvex-paper

### dietrich2024: Wait-and-judge (nonconvex scenario) certificate

- **Computes:** an a-posteriori violation level ε(s*_N) of the solution of any scenario program (1), convex or not,
  from the number s*_N of support scenarios.
- **How:** find support scenarios by re-solving with each scenario removed (§2); a scenario is support if its
  removal changes the solution. ε from (2); the convex refinement (4) uses d and s < d.
- **Guarantee:** Thm 1 (Campi et al. 2018): P{V(x*_N) > ε(s*_N)} ≤ β, for any s* ∈ {0..N}. No a-priori N; one may
  increase N and recompute. The paper relies on an "irreducible set of support scenarios". Single-removal testing
  identifies such a set only if the solution can be rebuilt from it (inferred caution for nonconvex programs).
- **Cost:** support detection costs N re-solves: RBF Duffing 7 min (N=1000) to 22 min (N=3000); quadrotor RBF
  30 min (N=1000) to 5.5 h (N=3000) (Tables 1–2).
- **Knobs:** set family; N; β.
- **Breaks when:** many support scenarios (ε grows with s); the support count is expensive to compute; the N·C(N,s)
  factor loosens the bound compared with a holdout (dietrich2025).
- **Hooks:** certifies a decision chosen by any rule *if* that rule is determined by a small subset of samples
  (a compression). A softmax-weighted average of all samples is not such a rule (inferred).

### dietrich2024: Tiling (union of grid cells)

- **Computes:** the union of the partition cells that contain at least one sample (9); support scenarios = first
  sample in each occupied cell; ε from (4) with d = number of cells (Alg. 1).
- **Guarantee:** as above; Duffing 20×20 grid, N=1000: s*=67, ε=0.251 at β=1e-9; quadrotor 10⁶-cell grid: s*=19,
  ε=0.113 (§4).
- **Cost:** seconds (1.7–8.4 s).
- **Knobs:** grid; N.
- **Breaks when:** fine grids in high dimension (many occupied cells, so s* grows).
- **Hooks:** an occupancy grid of rollout endpoints in the (p_x, h) plane, certified by its occupied-cell count.

### dietrich2024: Sum-of-RBF sublevel set

- **Computes:** {x : Σ_i exp(−(x − μ_i)²/(2σ_i²)) ≥ γ} with k-means centres and minimal widths (12), Alg. 2.
- **Guarantee:** wait-and-judge (2); Duffing m=2: s*=19, ε=0.118; quadrotor m=3: s*=22, ε=0.125 (β=1e-9).
- **Cost:** minutes to hours (support detection).
- **Knobs:** m, γ.
- **Breaks when:** support detection cost; local optima of the nonconvex program (inferred).
- **Hooks:** as tiling.

## dietrich2025data-paper

### dietrich2025: Holdout certificate by binomial tail inversion

- **Computes:** an upper bound on the true violation e = V(R̂) of *any* fixed set (or any estimator, including a
  neural one) from k̂ violations among M fresh samples.
- **How:** Bin‾(k̂, M, β) = max{e : Σ_{j≤k̂} C(M,j) e^j (1−e)^{M−j} ≥ β} (7)–(8); bisection (§III).
- **Guarantee:** Thm 1 (9): P{V(R̂) > Bin‾(k̂, M, β)} ≤ β, probability over the M holdout samples with R̂ fixed;
  by the tower property also over training ∪ holdout. With k̂=0: Bin‾ ≤ log(1/β)/M; in general k̂/M +
  O(sqrt(log(1/β)/M)) (10). The paper calls it "virtually perfectly tight". This is the one-sided Clopper–Pearson
  bound.
- **Cost:** Duffing RBF, N+M=3000: best split N=M=1500 gives ε=0.018 vs wait-and-judge 0.035 with all 3000;
  runtime 10–15 s vs 22 min. Quadrotor: N=1000, M=2000 gives ε=0.019 vs 0.051 (35–50 s vs 5.5 h) (Tables I–II).
  Extreme splits are poor (N=10: ε=0.78; M=10: ε=0.87).
- **Knobs:** the split N/M; β.
- **Breaks when:** the holdout is reused for selection; data are scarce; it cannot certify "zero violations on the
  data" by construction (§III).
- **Hooks:** the cheapest certificate for anything a planner proposes, as long as the certifying rollouts are not
  used to choose it.

### dietrich2025: Scenario reach tube with time-varying RBFs

- **Computes:** a tube {R̂(τ)} over a time grid. A trajectory violates it if it leaves the tube at *any* instant
  (§IV-B), so the guarantee is pathwise (joint over time).
- **How:** smoothed time-varying RBF program with penalty λ‖σ_avg − σ_i(τ)‖² (unnumbered display, §IV-B).
  Certified by holdout.
- **Guarantee:** holdout Thm 1. Linear 2-D example, N=M=1500: 138 violations, ε=0.144 at β=1e-9, 4.92 min.
- **Cost:** minutes; wait-and-judge was not attempted (one re-solve per trajectory).
- **Knobs:** λ, γ, m.
- **Breaks when:** the pathwise event makes rare excursions at any time count as violations (inferred; same failure
  mode as F5).
- **Hooks:** pathwise tube certificate on held-out rollouts.

### dietrich2025: De-randomization lower bound

- **Computes:** Lemma 1: an L-Lipschitz h on the unit ball with P{h>0} ≤ ε can have max h = L ε^{1/d}. Making a
  PAC set deterministic needs (L/γ)^d samples (§V-B).
- **Guarantee:** a lower bound, matched by zeroth-order optimization; removing one probability layer costs as much
  as removing both.
- **Hooks:** an argument for keeping a probabilistic certificate rather than inflating it to a worst-case one.

## hewing2019scenario-paper

### hewing2019: Scenario-based k-step probabilistic reachable sets (PRS) of an error system

- **Computes:** time-varying sets R^j_k with Pr(e(k) ∈ R^j_k | e(0)=0) ≥ p_j for the closed-loop error
  e(k+1) = A e + B π_tube(e) + w (3b) (Def. 1). A PRS (Def. 2) holds at every k *individually*, and the paper
  stresses that it is not a joint statement over all k.
- **How:** offline, sample N_s disturbance sequences W^(i) over the whole run time N̄ (non-i.i.d., unbounded,
  correlated allowed), simulate (3b) from e(0)=0, and for each k solve a scenario program with N_k discarded
  samples: scaling of a fixed convex shape (13) (d=1); half-space (Remark 5: discard the N_k largest hᵀe, take the
  max), so the PRS is aligned with the constraint; polytope with fixed H (14) (d = n_hs); ellipsoid (15)
  (d = n(n+1)/2 + n). Discarding by greedy removal of active samples satisfies Assumption 1.
- **Guarantee:** Thm 1 (Campi & Garatti): if (6) holds, the solution is feasible for the chance constraint with
  probability 1−β; Cor. 1–3. Sufficient conditions (7) and (8). Assumes convex closed X_δ and Assumption 1.
- **Cost:** crane example: N_s=10,000. Boxes with no discarding give p=99.6% at β≈1e-7 by (8); θ half-spaces
  discard 820 samples by (7) for p=90%, β=1e-7. Offline "a few seconds" (§V-A).
- **Knobs:** set shape (half-space, box, polytope H, ellipsoid), N_s, N_k, β; the tube controller π_tube, which
  may be nonlinear or saturated (Assumption 2).
- **Breaks when:** the shape is not aligned with the constraint (more tightening); ellipsoids need more samples
  (larger d).
- **Hooks:** the tightening margin per prediction step, computed from rollouts of whatever feedback the loop
  actually runs.

### hewing2019: Stochastic MPC with indirect feedback and PRS tightening

- **Computes:** a closed-loop policy for LTI x(k+1) = Ax + Bu + w̄ + w (1) with chance constraints
  Pr(x(k) ∈ X^j | x(0)) ≥ p_j (2a) and hard input constraints u ∈ U (2b), under unbounded, correlated w.
- **How:** split x = z + e, u = v + π_tube(e) (3). Tightened nominal constraints z_i ∈ Z_i = ∩_j (X^j ⊖ R^j_{k+i})
  and v_i ∈ V = U ⊖ E_u (10). The PRS is indexed by absolute time k+i (Assumption 3). Online QP (11): the nominal
  z_0 = z(k) is *not* reset to the measured state. The cost averages N_s^MPC samples of the *conditional*
  disturbance W_k given past disturbances, with error samples starting at the measured e(k) and precomputed
  (11d, 11g). Apply u(k) = v_0* + π_tube(e(k)) (12). Remark 2: because z is not reset, the closed-loop error evolves
  autonomously by (3b); feedback from x(k) to z enters only through the cost. Terminal set Z_f is robustly
  invariant w.r.t. w̄ under π_f and lies inside Z_∞ = ∩_k Z_k (Assumption 4).
- **Guarantee:** Thm 2: if (11) is feasible at k=0 it is feasible for all 0 ≤ k ≤ N̄ − N (shifted candidate; uses
  Z_i(k) = Z_{i−1}(k+1)). Thm 3: u(k) ∈ U surely, and Pr(x(k) ∈ X^j | x(0)) ≥ p_j for every k. The statement is per
  time step and marginal from x(0): not conditional on x(k−1), not joint over the episode. Remark 4: everything holds
  with confidence 1−β over the offline scenarios. The predictive (conditional) samples serve the cost only;
  constraint satisfaction is proven for the *closed-loop* error and the unconditional W (§III).
- **Cost:** offline seconds; online QP ≈ 20 ms (N=30, N_s^MPC=10). Crane, 10,000 closed-loop runs: guaranteed
  99.6/90/90 %, empirical 99.98/91.2/94.33 % (Table I).
- **Knobs:** π_tube (gain, saturation level ±0.4 in the example), PRS shape per constraint, p_j, β, horizon N,
  N_s^MPC.
- **Breaks when:** dynamics are nonlinear, or the nominal is reset to the measured state. Either way the error is no
  longer autonomous and the offline PRS is not the law of the loop (inferred from Remark 2 and the proof of Thm 3).
  Finite run time N̄ is needed for unstable systems (Remark 1). Per-step marginal guarantees say nothing about the
  probability of any violation in an episode.
- **Hooks:** the template for making the scored set equal to the loop's set: tighten a nominal (CE) plan by a PRS
  of the closed-loop error, computed offline; no online risk estimate is needed for the constraints.

## tebjou2023data-paper

### tebjou2023: Split-conformal Christoffel reach set

- **Computes:** Ŝ = {x : v_d(x)ᵀ M̂_d⁻¹ v_d(x) ≤ α}, with M̂_d fitted on the training set and α = max of the
  scores over a separate calibration set of size N (Alg. 1).
- **How:** split conformal with the Christoffel polynomial as nonconformity function; threshold at the largest
  calibration score (conformal region C^{1/N}).
- **Guarantee:** Thm 4 (training-conditional PAC, from Bates et al. Thm 4 = Thm 2 here):
  P[μ(C^{1/N}) ≥ exp(log δ / N)] ≥ 1−δ (10). With continuous μ and score there is also an upper bound (11), giving
  a two-sided band (12). Independent of n and d. Example: N=2000 cal → ε ≤ 0.002 at 99 %; N=200 → 0.02; 6 of 1000
  repeats exceeded 0.02 (§3.1). Marginal coverage ≥ 1 − (i+1)/(N+1) (7) holds only on average over D.
- **Cost:** fit O(s(d)³); ε depends only on N and δ.
- **Knobs:** split sizes, degree d (tightness only).
- **Breaks when:** the calibration set is small; the score is fitted on the calibration data.
- **Hooks:** any score computed from generated samples (e.g. PREDICT's KDE) can replace the Christoffel polynomial,
  as long as calibration rollouts come from the true law and are not used to fit the score.

### tebjou2023: Transductive Christoffel conformal (no split)

- **Computes:** p-values with the test point added to the moment matrix, via Sherman–Morrison updates (13), cost
  O(N s(d) + s(d)²) per evaluation.
- **Guarantee:** the paper asserts that Thm 4 holds with D_cal := D (§3.2) but gives no separate proof (the scout
  notes the claim; validity of training-conditional bounds for full conformal is not shown here). Example: N=1000,
  ε ≤ 0.45 % at 99 %.
- **Hooks:** none beyond the split version for this brief.

### tebjou2023: Outlier-robust conformal region

- **Computes:** a threshold at the (p+1)-th largest calibration score when at most p calibration points are outliers
  (Alg. 2).
- **Guarantee:** Thm 5 (14): P(μ(C^{(p+1)/N}) ≥ 1−ε) ≥ Σ_{i=p+1}^{N−p} C(N−p,i) ε^i (1−ε)^{N−p−i}. Confidence collapses
  when ε is below the outlier fraction (Table 1).
- **Hooks:** calibration data contaminated by model error, e.g. PREDICT samples mixed with simulator rollouts
  (inferred).

## hashemi2023data-paper

### hashemi2023: Surrogate flowpipe plus component-wise conformal inflation

- **Computes:** a Δ-confident flowpipe X ⊂ R^{n(K+1)}, i.e. a set of whole K-step trajectories with
  Pr[σ_{s0} ∈ X] ≥ Δ (Def. 1, (2)). It is a tube: the trajectory is in X jointly at all times.
- **How:** train a ReLU surrogate F: s_0 ↦ predicted trajectory on D_train. Compute the star-set image of the
  initial set I (exact/approx star, NNV). Residuals R^j = |e_{j+n}ᵀσ − F^j(s_0)| per state component and time
  (Def. 3) on D_test. Per component, take the ℓ-th smallest with ℓ = ⌈(L+1)δ⌉. Inflate: X = X̄ ⊕ Zonotope(0,
  diag([0, R*])) (Thm 1).
- **Guarantee:** Thm 1: Δ = 1 − nK(1−δ) by a union bound over nK components (3). Marginal (over calibration and
  test), no confidence layer. Trajectories are treated as i.i.d. vectors in R^{n(K+1)}.
- **Cost:** L=40,000 calibration trajectories (ACC, quadcopter), 160,000 (Laub–Loomis); 2–2.5 h surrogate
  training; 3–90 s CI (Tables 1–3).
- **Knobs:** surrogate architecture; partitioning of I.
- **Breaks when:** nK is large, because the union bound forces δ → 1 (conservative). The worst case over the
  initial set I is mixed with a statistical inflation.
- **Hooks:** "nominal prediction ⊕ calibrated residual box"; the nominal can be any deterministic predictor of the
  trajectory.

## hashemi2025pca-paper

### hashemi2025: PCA-shaped max-residual conformal tube

- **Computes:** a δ-confident flowpipe with inflating hypercube δX = ⟨mean PE, V, P⟩ oriented along principal axes
  of the training residuals and centred at their mean (Prop. 5, (15), (17)).
- **How:** split the horizon into segments, each with its own surrogate F_q(s_0) predicting from s_0 directly, so
  that errors do not accumulate (8). On training residuals PE^q: mean and covariance (10), eigenvectors V^q.
  Whitened residual r = V^{qᵀ}(PE^q − mean) (11). Scalar score ρ = max_j |r^j|/ω_j with ω_j = max over training
  (12)–(13). Conformal quantile on a *fresh* calibration set (Def. 4): the paper states that reusing the training
  set "violates CI rules".
- **Guarantee:** Pr[all |r^j| ≤ ω_j ρ*] > δ (Prop. 5), joint over the whole trajectory with no union bound,
  marginal. Robust CI: under TV(J^real, J^sim) < τ, use rank ℓ* = ⌈(L+1)(1+1/L)(δ+τ)⌉ (4).
- **Cost:** quadcopter K=100, δ=99.99 %, |T^trn|=42,000, |R^calib|=20,000; K=5000 (1 kHz, 5 s) with 451 trained
  models plus interpolation (18); powertrain 27-D, K=4000, τ=4 %, δ=95 % (Table 1).
- **Knobs:** segment lengths T_q (all experiments use T_q=1, so PCA acts within one time step); τ; normalizers ω_j.
- **Breaks when:** τ must be known; with T_q=1 the cross-time correlation is not exploited (inferred). The max score
  is still set by the worst normalized component.
- **Hooks:** shaping a tube by whitening the residual between realized and predicted trajectories; the max-score
  trick turns a joint-over-time event into one scalar quantile.

## lin2024verification-paper

### lin2024: Robust-scenario verification of a learned safe set

- **Computes:** an upper bound ε on the fraction of a candidate safe set S (super-δ level set of a learned value
  Ṽ(x,0)) whose states are actually unsafe under the induced policy π̃.
- **How:** sample N i.i.d. states from S (rejection sampling), roll out π̃, count k states with J_π̃(x_i,0) ≤ 0
  (§4). ε from (2).
- **Guarantee:** Thm 2: if Σ_{i=0}^k C(N,i) ε^i (1−ε)^{N−i} ≤ β, then w.p. ≥ 1−β, P_{x∈S}(V(x,0) ≤ 0) ≤ ε (3).
  Proof: Lemma 7, a 1-D sampling-and-discarding scenario program (d=1) with the k violators discarded (App. A).
  S and the policy are fixed; the samples are drawn from S. Dynamics are deterministic in this paper. Whether the
  level δ may be chosen with the same samples is not discussed (Figs. 1–2 sweep levels at a fixed budget).
- **Cost:** β=1e-16; multi-vehicle: N=3,684,118, k=731 (Fig. 3).
- **Knobs:** level δ (volume vs ε trade-off), N, β.
- **Breaks when:** the outlier rate is high (ε cannot go below it); a reach-avoid DeepReach solution gave zero
  certifiable volume at ε ≤ 1e-4 (§6.3).
- **Hooks:** certifies a sublevel set of *any* learned safety value against rollouts of the actual policy.

### lin2024: Conformal = robust scenario identity

- **Computes:** Thm 3: P_{x∈S}(J_π̃(x,0) > 0) ~ Beta(N−k, k+1) (4); mean (N−k)/(N+1) (Remark 4). Lemma 5 gives
  exactly the bound (2).
- **How:** App. B.2: split conformal with error rate α keeps the ⌈(n+1)(1−α)⌉-th order statistic. This is the
  scenario program min g s.t. s_i ≤ g with the k = ⌊(n+1)α − 1⌋ largest scores discarded. Its guarantee (9)
  equals the Beta law (13) via the incomplete beta identity.
- **Guarantee:** an identity; holds for any score function fixed before calibration.
- **Hooks:** lets the brief state CP, conformal and scalar scenario certificates as one result.

### lin2024: Outlier-adjusted retraining

- **Computes:** a refined value J̃ ≈ J_π̃ trained on rollout labels with weighted MSE: weight w=1e-3 on conservative
  errors (Ṽ < J) and 1 on optimistic ones (§6); checkpoint chosen on a validation set by
  max{J̃(x): J(x) ≤ 0}.
- **Guarantee:** none by itself; certified afterwards with Thm 2 (ε ≤ 1e-4, β=1e-16). Safe volume +2.3 % (vehicles),
  +9.58 % (rocket), 0 → 0.19 (no-go zones).
- **Hooks:** train the planner's safety predictor on outcomes of the closed loop, with asymmetric loss.

## sartipizadeh2019voronoi-paper

### sartipizadeh2019: Sampled reach-avoid MILP with a Hoeffding count

- **Computes:** p*_K, the maximal fraction of K sampled disturbance sequences for which an open-loop input U keeps
  the LTI trajectory in the safe set and ends in the target (Problem 2, big-M MILP).
- **How:** a binary variable per scenario.
- **Guarantee:** Thm 1: with K ≥ −ln β/(2δ²) (13), P{p*_K − p* ≥ δ} ≤ β, i.e. the optimized empirical value
  overestimates the optimum by more than δ with probability ≤ β. (The theorem statement prints the event with the
  sides swapped; conversion note (a).) The proof applies Hoeffding to the empirical mean under U*_K, which is chosen
  from the same samples, as if U*_K were fixed. A valid version would need a bound uniform over U (e.g. a union
  bound over a finite candidate set) (inferred; scout's assessment).
- **Cost:** exponential in K (MILP).
- **Hooks:** the planner's hit count is this estimator; the winner's-curse correction is a union bound over
  candidates (inferred).

### sartipizadeh2019: Voronoi seeds with buffered constraints

- **Computes:** an under-approximation of p*_K from K̂ ≪ K cluster seeds ψ^(j) of the disturbance-propagated
  samples G_w W, each weighted by its cell count α^(j) and checked against constraints tightened by
  ε_ℓ^(j) = max over the cell of F_ℓ(φ − ψ^(j)) (Problem 3, Lemma 4 (17)–(18)).
- **How:** offline k-means on G_w W (valid for any x_0, U by translation invariance, Lemmas 1, 3); online MILP with K̂
  binaries; then re-evaluate U*_{K̂} on all K samples (22).
- **Guarantee:** deterministic ordering p*_{K̂} ≤ p̂ ≤ p*_K (Thms 2–3), relative to the K samples. p̂ in (22) is
  evaluated on the samples that also built the seeds, with no further statistical claim.
- **Cost:** spacecraft, K=2000: K̂=20 → 0.83 in 0.2 s; K̂=40 → 0.849 in 0.6 s; K̂=100 → 0.860 in 2.7 s; Fourier 0.862
  in 66 s (Table 1).
- **Knobs:** K̂ (WSS knee), metric.
- **Breaks when:** dynamics are nonlinear or the noise enters non-additively. Then the translation invariance
  (Lemma 3) fails and clusters depend on (x_0, U) (inferred). The method is open-loop only.
- **Hooks:** compressing a rollout cloud into a few representatives with conservative buffers, so constraint
  checks on candidates are cheap.
