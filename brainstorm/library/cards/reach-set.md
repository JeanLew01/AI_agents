# Mechanism cards: set-based and sampling-based reachability (lens `reach-set`)

Skills: lew2021sampling-paper, lew2022simple-paper, liebenwein2018sampling-paper, fan2017dryvr-paper,
gruenbacher2022gotube-paper, ganai2023iterative-paper, selim2022safe-paper, liu2025recurrent-paper,
ouyang2026symplectic-paper. Citations are `skill §section (eq. n)` against `references/paper.md`.
"(inferred)" marks statements the scout derived rather than read.

Note on authorship: liu2025recurrent-paper (J. Liu, E. Mallada) and ouyang2026symplectic-paper (Z. Ouyang,
J. Liu, E. Mallada) are from the same JHU group as the TRO 2027 project.

---

### lew2021sampling-paper: randUP (random convex hull of propagated samples)

- **Computes:** an approximation of the convex hull Co(X_k) of the reachable set (2) of
  x_{k+1}=f(x_k,u_k,θ,w_k) over all (x_0,u,θ,w) in compact sets, for each k=1..N.
- **How:** Alg. 1: sample i.i.d. z^j=(x_0^j,u^j,θ^j,w^j), propagate, X_k^M = Co({x_k^j}). Note (2) keeps θ
  fixed along a trajectory (time-correlated), unlike the one-step recursion X̃_{k+1} which is
  over-conservative (§2, example x_{k+1}=θx_k).
- **Guarantee:** Thm 2 (§3): if P(x_k^j ∈ G) > 0 for every open G meeting X_k, then X_k^m → Co(X_k) almost
  surely (random-set convergence, Thm 1 conditions (3),(4); proof App. A via Borel-Cantelli). No rate, no
  finite-sample outer bound; for convex X_k the hull is always an inner approximation (§5); for non-convex
  X_k the limit is an outer approximation (§3 "Outer-approximation").
- **Cost:** M forward propagations, embarrassingly parallel; hull or outer box/ellipsoid afterwards.
- **Knobs:** M; sampling distribution (e.g. Beta(α=β≪1) on additive disturbances to push mass to the
  boundary, §3); set representation (hull, box, ellipsoid, zonotope).
- **Breaks when:** finite M (always an inner approximation of convex sets); disconnected parameter sets need
  one run per component (footnote 3); no rate means no sample budget.
- **Hooks:** any planner that already propagates M i.i.d. (decision, nature) pairs gets this estimate for free.

### lew2021sampling-paper: robUP! (adversarial sampling of the uncertain inputs)

- **Computes:** a larger (more accurate) hull for the same budget by moving samples so their states leave the
  current hull.
- **How:** maximize the dispersion objective (5)
  L^M(z) = (1/N) Σ_k ||x_k(z) − c_k^M||²_{Q_k^M}, Q_k^M = (sample covariance of {x_k^j})^{-1}, c_k^M = centre of
  X_k^M, by projected gradient ascent on z=(x_0,u,θ,w): Alg. 2 l.4-5 z^j ← Proj_Z(z^j + η∇_z L^M), l.6
  re-propagate, l.7 keep the union of all iterates, l.8 return the hull of M·n_adv (plus initial) particles.
  The objective pushes outward in the Mahalanobis metric from the hull centre, averaged over the horizon; it is
  not a failure or cost objective. Q is chosen as inverse covariance for conditioning of the PGA Hessian (§4).
- **Guarantee:** none stated beyond randUP. (inferred) Because the initial M i.i.d. samples are kept and every
  iterate is a reachable state, Co(randUP_M) ⊆ robUP! hull ⊆ Co(X_k), so the a.s. convergence of Thm 2
  carries over as M→∞; the adversarial iterates themselves are not i.i.d.
- **Cost:** n_adv extra propagations + gradients per sample; requires f ∈ C^1 and a cheap projection onto Z
  (box, ellipsoid via S-ADMM). Spacecraft (13-D, N=20): M∈{50,100,200}, n_adv=1 → 83/173/304 ms (App. B,
  Fig. 8).
- **Knobs:** step size η (η=1 in §6 linear test), n_adv (1 chosen; "reduced returns" beyond (M,n_adv)=(100,1),
  App. B), weighting Q_k, per-time vs averaged objective ("minimal differences", §4).
- **Breaks when:** more steps concentrate samples on the boundary but do not necessarily enlarge the hull
  (App. B, Fig. 7); gradients through long horizons; non-differentiable simulators.
- **Evidence:** NN double-integrator, % of true volume: randUP M=3k → 79-80 %; robUP! M=2k, n_adv=1 → 94-95 %;
  Lipschitz ellipsoids [13] → 170-6542 % (Fig. 5 table). Falsification use: adversarial samples saturate the
  disturbances and pick extreme mass/inertia (App. B, Fig. 10).
- **Hooks:** a pessimistic move for nature samples (projected ascent on Ω) inside a sampling planner; a
  falsifier for a candidate plan.

### lew2021sampling-paper: reachability-aware trajectory optimization with sampled sets (App. D)

- **Computes:** an open-loop plan whose sampled reachable sets avoid obstacles.
- **How:** nominal trajectory (18) with nominal (θ̄,w̄); problem (20): min nominal cost s.t. X_k ⊂ X_free,
  X_N ⊂ X_goal. Box tightening δ_{k,i} = max_j |x^j_{k,i} − μ_{k,i}| gives (22)
  x_min+δ ≤ μ ≤ x_max−δ; linear constraints via ellipsoid Q_k = s·diag(δ_i²); solved by SCP (OSQP).
- **Guarantee:** only as M→∞ (Thm 2); used to invalidate infeasible homotopy classes quickly (§6, Fig. 6:
  3 SCP iterations, 875 ms, N=21).
- **Knobs:** M, n_adv, set shape (box/ellipsoid). **Breaks when:** finite M under-approximates.
- **Hooks:** sample-based constraint tightening of the nominal plan; margin γ ↔ δ_{k,i}.

### lew2022simple-paper: ε-RandUP (padded hull with finite-sample outer guarantee)

- **Computes:** Ŷ^M_ε = H({f(x_i)}) ⊕ B(0,ε) (2) for Y = f(X), X ⊂ R^p compact, f continuous.
- **How:** i.i.d. x_i ~ P_X, evaluate f, hull, pad by ε.
- **Guarantee:** Thm 1 (§4): under Assumption 1 (P_X puts positive mass on f-preimages of every
  neighbourhood of every point of ∂Y — boundary only), d_H(Ŷ^M_{ε_M}, H(Y)⊕B(0,ε̄)) → 0 a.s. for any ε_M → ε̄.
  Thm 2 (§5.1): if f is L-Lipschitz (A2), P_X(B(x, ε/2L)) ≥ Λ^L_ε for all x ∈ ∂X (A3), and ∂Y ⊆ f(∂X), then
  with probability ≥ 1−δ_M, δ_M = D(∂X, ε/(2L))(1−Λ^L_ε)^M:
  d_H(Ŷ^M, H(Y)) ≤ ε and Y ⊆ Ŷ^M_ε. Corollary 1: r-convex complement (A4) + density ≥ p_0 (A5) give
  Λ = p_0 λ(B(0,ε/2L) ∩ B(r,r)). Remark (App. B.2): ∂Y ⊆ f(∂X) holds if f is open (e.g. a submersion);
  otherwise sample all of X and use D(X, ε/2L).
- **Cost:** M ≥ [log δ − log D(∂X,ε/2L)] / log(1−Λ). Example (App. E.2): 2-D input box, L=1, ε=0.02, uniform on
  ∂X, δ=10^-4 → M ≈ 1376. Covering number grows like (2d√n/ε)^n (§5.3) — exponential in input dimension p.
- **Knobs:** M, ε (or ε_M schedule), P_X (boundary-concentrated better: Fig. 3, α→∞), L (needs an estimate;
  App. D samples L̂ for ReLU nets).
- **Breaks when:** L unknown or large; input dimension p large (D explodes); f not open (must cover all of X);
  only the convex hull is recovered (non-convex Y over-approximated).
- **Evidence:** NN-controller verification: more accurate than ReachLP, kernel method and GoTube at comparable
  time (Figs. 4-5).
- **Hooks:** a calibrated padding ε (= tube margin) as a function of M, L and the sampling density; a test of
  whether a *set* of inputs is safe.

### lew2022simple-paper: ε-RandUP inside robust MPC (§6.3)

- **Computes:** plan (μ,ν) for a free-flyer with uncertain mass m∈[10,18] kg and force F∈[−0.015,0.015]² N.
- **How:** (4a)-(4b): nominal cost s.t. X_t(ν) ⊂ X_free, X_N(ν) ⊂ X_goal, X_t(ν) from ε-RandUP over (m,F) with
  an auxiliary linear feedback; ε=0.03, M=10³, 10 Hz in Python.
- **Guarantee:** inherits Thm 2 per solve (if L known); recursive feasibility reported empirically in hardware.
- **Breaks when:** as above; the nominal (certainty-equivalent) MPC collided because the parameter uncertainty
  was large and unobserved (Fig. 6).
- **Hooks:** baseline "reachability-constrained sampling MPC"; shows when robustness pays (large unobservable
  parametric uncertainty).

### liebenwein2018sampling-paper: δ-packing reachability with volume guarantee

- **Computes:** a finite set S ⊂ X of initial states whose union of reachable sets F(S) = ∪_{x∈S} f(x)
  under-approximates F(X) in volume: (1−ε)μ(F(X)) ≤ μ(F(S)) ≤ μ(F(X)) (Problem 1, (1)). f(x) = H(x,T) is the
  set reachable from x over all controls (set-valued; needs an oracle EvaluateReachability).
- **How:** Alg. 1 GreedyPack (δ-packing, which at termination is also a δ-cover); Alg. 2 sets
  δ = d((1−ε)^{-1/d} − 1)/(αKc) (l.6) from surface-to-volume ratio α, Hausdorff-Lipschitz constant K
  (Assumption 2: d_H(f(x),f(y)) ≤ K||x−y||) and universal constant c (Lemma 3); Alg. 3 anytime: ε ← ε/2.
  Not importance sampling: a deterministic space-filling (coverage) design; experiments used a grid (§VI-B).
- **Guarantee:** Thm 7 (deterministic, not probabilistic) volume under-approximation; Lemma 6 outer bound
  F(X) ⊆ F(S)_{δK} (δK-fattening); Corollary 9 |S| ≤ (3αKΔ(X)c/ε)^d; Thm 10 runtime; Prop. 11 anytime
  asymptotic optimality.
- **Cost:** exponential in state dimension d; constants α, K, c must be bounded (Alg. 2 l.1-4).
- **Knobs:** ε (→ δ), packing vs grid, anytime halving.
- **Breaks when:** α, K, c unknown; per-point reachable-set oracle unavailable; Assumption 1 (f(x) has positive
  volume) fails for fixed-control (point-valued) maps; high d.
- **Evidence:** unicycle, uniform sampling fails on non-convex/uneven initial sets (dumbbell, lollipop,
  hedgehog), packing holds the bound (Figs. 2-4).
- **Hooks:** space-filling sample design for a low-dimensional input (nature or decision) with a deterministic
  coverage certificate; the halving schedule is a coarse-to-fine refinement.

### fan2017dryvr-paper: PAC-learned discrepancy functions

- **Computes:** β(x_1,x_2,t) bounding |τ_1(t) − τ_2(t)| (1) for trajectories of a black-box deterministic
  simulator in one mode.
- **How:** GED β = |x_1−x_2| K e^{γt}: taking logs, ln(|τ_1(t)−τ_2(t)|/|x_1−x_2|) ≤ γt + ln K is a linear
  separator (2) on pairs (ln-ratio, t); sample k pairs, solve an LP minimizing γT + ln K (§3.1.2). PED:
  piecewise γ_i on [t_{i−1},t_i], breakpoints chosen so γ_i < 2.
- **Guarantee:** Prop. 3.1: k ≥ (1/ε) ln(1/δ) ⇒ with prob ≥ 1−δ the learned separator's violation mass under
  the sampling distribution D is < ε. This is a guarantee on the fraction of (pair, time) points violated, not
  that β is a true discrepancy; Thm 3.2 (soundness of VerifySafety) is conditional on β being a true
  discrepancy. (inferred) The bound (1−ε)^k ≤ δ is the zero-failure one-sided binomial (Clopper–Pearson)
  bound.
- **Cost:** 10-20 training traces sufficed; 96 % (>10 traces) and >99.9 % (>20 traces) of test pairs/time
  points satisfied (1) on 1000 test traces (§3.1.3).
- **Knobs:** GED vs PED, time partition, ε, δ, k.
- **Breaks when:** stochastic simulators (TL must be deterministic, Def. 2.6); exponential growth makes long
  horizons conservative (γ ≥ 2 "very conservative").
- **Hooks:** a data-fitted contraction/expansion rate K e^{γt} for the tube margin growth along the horizon.

### fan2017dryvr-paper: simulate-and-bloat reachtubes with refinement (GraphReach / VerifySafety)

- **Computes:** an over-approximate reach tube for a hybrid system with a white-box transition graph and
  black-box mode simulators; decides bounded safety.
- **How:** Alg. 1 l.7-8: LearnDiscrepancy then ReachComp, which "generates finite simulation traces from S_init
  and then bloats the traces ... using β" (described in words only, pointer to [22]). (inferred, standard form
  of [22]) with S_init covered by balls B(x,d) around simulated starts, the tube at time t is
  ∪_x B(τ_x(t), d·K e^{γt}). Alg. 2 (App. A.3): SAFE if the tube misses U, UNSAFE if part of the tube is inside U
  (counterexample), else refine by partitioning S_init or splitting edge time labels. Random executions are
  tried first as falsification (§3.3).
- **Guarantee:** Thm 3.2 soundness and relative completeness given correct β.
- **Cost:** 21-217 s per benchmark, 0-5 refinements (Table 1).
- **Knobs:** partition strategy, GED/PED.
- **Breaks when:** as above; cost grows with refinements.
- **Hooks:** adaptive refinement of an input cover only where the safety verdict is undecided.

### gruenbacher2022gotube-paper: statistical bounding tube with stochastic Lipschitz caps

- **Computes:** bounding balls B_j = B(χ(t_j,x_0), δ_j) of the reach set of a deterministic, Lipschitz,
  forward-complete ODE (1) from an initial ball B_0 = B(x_0,δ_0), at each t_j.
- **How:** because the flow map is a homeomorphism, max_{x∈B_0} ||χ(t_j,x) − χ(t_j,x_0)|| (2) is attained on the
  surface of B_0, so samples are drawn uniformly on the surface only (§Setup). Alg. 1: add batches until the
  achieved confidence p̄ ≥ 1−γ (l.5-14); δ_j = μ·m̄_{j,V} (l.16), μ>1 a tightness factor. Confidence from
  Lipschitz caps (Def. 3): cap radius r_x (4) solves μm̄ − d_j(x) = λ_x r + Δλ r², where λ_x = ||∂_xχ(t_j,x)||
  (variational equation) and Δλ is a quantile (3) of a stochastic lower bound of the distribution of
  difference quotients, built by fitting a generalized extreme-value distribution and correcting with
  DKW + one-sided KS (Lemma 1, (S1)-(S4)). No gradient ascent: the paper replaced SLR's local gradient search
  with more samples (Introduction).
- **Guarantee:** Thm 1: each cap is a γ,t_j-Lipschitz cap (5); Thm 2 (6): ∀γ ∃N with
  P(μ·m̄_{j,V} ≥ m*_j) ≥ 1−γ — per time step t_j; existence of N, not an explicit count.
- **Cost:** sample count grows as γ, μ−1 shrink and with dimension ("Sample blow up", §Discussions).
- **Knobs:** γ, μ, batch size b, time grid.
- **Breaks when:** stochastic dynamics (not for neural SDEs, §Limitations); small μ; balls are loose for
  anisotropic sets; short horizons/small tasks (Table 2).
- **Hooks:** boundary-only sampling of an input ball; anytime stopping rule for the sample count; a
  multiplicative margin μ.

### ganai2023iterative-paper: reachability estimation function (REF)

- **Computes:** φ^π(s) = E_{τ∼π,P(s)} max_t 1{s_t ∈ S_v} — the probability of ever entering the violation set
  (Def. 3); feasible set S_f^π = {φ^π = 0} (Def. 5).
- **How:** Thm 1 Bellman form φ^π(s) = max{1_{s∈S_v}, E_{s'} φ^π(s')}; learned with a discounted target
  p(s) = max{1_{S_v}(s), γ p(s')} (§5.3; Alg. 1 l.8). (inferred) Because the indicator is binary,
  max{1_v, E p(s')} = 1_v + (1−1_v) E p(s'), which is linear in p(s'), so the single-sample TD target is
  unbiased.
- **Guarantee:** convergence via γ-contraction; intended target is φ* of a safest policy, reached only with
  the time-scale ordering of A1 (below).
- **Cost:** one extra critic.
- **Knobs:** discount γ, learning rate ζ_3.
- **Breaks when:** REF learned too fast converges to φ^π of the current policy (suboptimal feasible set,
  conservative); too slow lets the multiplier blow up (§6.3, Fig. 5).
- **Hooks:** a learned closed-loop hit probability from the loop's own data (contrast: Monte Carlo hit
  probability of a committed open-loop plan).

### ganai2023iterative-paper: RESPO feasibility-switched Lagrangian

- **Computes:** a policy that maximizes reward with persistent safety where feasible and minimizes cumulative
  discounted violation V_c elsewhere, with guaranteed (re)entry to the feasible set when possible (Prop. 2,
  deterministic MDP, γ near 1).
- **How:** (4) min_π max_λ E[(−V^π + λV_c^π)(1−p(s)) + V_c^π p(s)]; Alg. 1: critics, policy, REF, multiplier
  updated on four time scales ζ_1 ≫ ζ_2 ≫ ζ_3 ≫ ζ_4 (A1). Uses V_c (sum of costs) rather than the max-violation
  value V_h because V_h gives a weak signal and allows many sub-maximal violations (§4.2).
- **Guarantee:** Thm 2: under A1 (step sizes), A2 (strict feasibility), A3 (smoothness), a.s. convergence to a
  locally optimal policy of RESPO (finite MDPs).
- **Breaks when:** time-scale ordering violated (ablation Fig. 5); multiplier unbounded (App. C.4.4).
- **Hooks:** principled form of "feasibility-first fallback": rank by violation magnitude when infeasible,
  by cost under a hard constraint when feasible, blended by an estimated infeasibility probability.

### selim2022safe-paper: data-driven zonotope reachability for a black-box plant

- **Computes:** zonotopes R̂_j ⊇ R_j (3) for a given action plan of x_{k+1} = f(x_k,u_k) + w_k, w_k uniform in a
  noise zonotope W (Assumption 2).
- **How:** Alg. 2 (from Alanwar et al. [42]): least-squares local linear model M_j fitted to offline data
  (X_−, X_+, U_−) (4a-c) around a linearization point; residual interval zonotope Z_L (l.3-5); Lipschitz
  remainder Z_ε = diag(L_i δ_i/2) from per-dimension Lipschitz constants L_i and data covering radii δ_i (l.1);
  R̂_{j+1} = M_j(1 × (R̂_j − x*) × (U_j − u_j)) + W + Z_L + Z_ε (l.6).
- **Guarantee:** containment via [42, Thm 2] given bounded zonotopic noise and correct L*, δ (which are
  estimated from data, Limitations).
- **Cost:** 500 offline steps sufficed empirically; 30-72 ms per planning step including repair (Tables I-II).
- **Breaks when:** L*, δ mis-estimated; offline data not representative at run time; dimension (curse of
  dimensionality in data for L*, §I-B Limitations).
- **Hooks:** a reachability estimator whose centre chain is differentiable in the actions.

### selim2022safe-paper: safety layer = differentiable collision check + gradient plan repair + failsafe induction

- **Computes:** a modified action plan whose reachable zonotopes miss obstacles and that ends in a braking
  failsafe.
- **How:** Alg. 1: roll out the RL policy with a learned ensemble model to get a plan; if any R̂_j meets X_obs,
  Alg. 3 repairs it: collision depth v* = LP (6) on the constrained-zonotope intersection (5) (empty iff
  v* > 1); u_j ← proj_{U_j}(u_j + γ∇_{u_j}v*) (l.8; an ascent step on v*) with ∇ via the chain (7)-(8) through
  the zonotope centres only (constant linearization). The plan must stop after n_plan steps (Assumption 1:
  brake to a standstill and stay there). If repair fails within one step's time budget, continue the previous
  safe plan.
- **Guarantee:** Thm 1: safe for all k by induction (previous plan + failsafe always available), given the
  modelling assumptions; the learned environment model does not affect safety.
- **Breaks when:** no invariant failsafe (a quadrotor under wind cannot "stop and stay"); repair is local
  gradient ascent and can fail; the gradient ignores generator changes.
- **Evidence:** 0 % collisions on Turtlebot, quadrotor, point mass, hexarotor in wind, higher reward than RTS,
  SAILR, SECAS (Tables I-II).
- **Hooks:** a guidance gradient on decision samples; recursive feasibility by keeping the last certified plan.

### liu2025recurrent-paper: recurrent control barrier functions (RCBF) and τ-recurrent sets

- **Computes:** a safety certificate that needs return to a set within τ instead of invariance.
- **How:** Def. 6: S is control τ-recurrent if ∀x∈S ∃u with returns to S at intervals ≤ τ (4). Def. 7 (5):
  h is an RCBF if ∀x ∈ h_{≥−c} ∃u ∈ U^{(0,τ]}: max_{t∈(0,τ]} e^{γ(h(φ(t,x,u)))t} h(φ(t,x,u)) ≥ h(x), with
  piecewise γ_{α,β} (6).
- **Guarantee:** Thm 2: h_{≥0} is control τ-recurrent; if h_{≥0} ∩ R_τ(X_u) = ∅ (no state of h_{≥0} can reach the
  unsafe set within τ), every recurrent control keeps the trajectory out of X_u forever (last-exit-time
  argument). Thm 3: for a sector-contained CBF h and any closed S between h_{≥0} and h_{≥−c}, the signed
  distance −sd(·,S) is an RCBF, with an explicit lower bound on τ̂ — "function design becomes set
  identification".
- **Breaks when:** deterministic dynamics assumed (forward completeness, uniform local Lipschitz,
  Assumptions 1-2); no disturbance.
- **Hooks:** a receding-horizon certificate that asks only for a return to a certified set within τ ≤ H,
  witnessed by one control signal.

### liu2025recurrent-paper: nonparametric cell verification from sampled controls

- **Computes:** an outer approximation of the τ-backward reachable tube R_τ(X_u) and a safe set S = ∪G_s for
  which h = −sd(·,S) satisfies the robust RCBF conditions.
- **How:** Lemma 1 (12): same control, |sd(φ(t,y,u),S) − sd(φ(t,x,u),S)| ≤ r e^{Lt} for ||x−y|| ≤ r. Thm 4: cell
  B_r(x) misses R_τ(X_u) if ∃u with sd(φ(t,x,u),X_u) > r e^{Lt} ∀t ∈ [0,τ] (13); is inside it if ∀u ∃t:
  sd < −r e^{Lt} (14). Thm 5: robust RCBF condition (16) with ĥ^−_r = h(φ) − r e^{Lt} (15) certifies all y in
  B_r(x); (19) certifies failure. Alg. 1-4: three stages (outer-approximate X_u, then R_τ, then RCBF), each
  cell samples n_s control signals from its centre (Alg. 3 l.4): unsafe if all samples meet C_u, safe if at
  least one meets C_s, else split into 3^n cells of radius r/3 (Alg. 4).
- **Guarantee:** safe cells are sound: the existential condition is witnessed exactly by the sampled control.
  (inferred) The "∀u" unsafe test is only checked on n_s samples, so G_u may contain safe cells — conservative
  in the safe direction. Approximation gap vs n_s not quantified (§VII).
- **Cost:** 3-D evasion, n_s = 3000, τ = 1 s: 0.13-19.75 s vs HJ 0.02-83.73 s; HJ under-captures unsafe volume
  at coarse grids (0.51-0.95) while the method captures 1.0 at every precision (Tables I-II). Smaller τ → tighter
  but cost grows roughly exponentially (Fig. 3).
- **Knobs:** τ, α, β, n_s, r_min.
- **Breaks when:** large L or τ (e^{Lτ} bloat); state dimension (3^n splits); disturbances.
- **Hooks:** a sampled control certifies a whole ball of states; the planner's own samples could serve as
  witnesses.

### ouyang2026symplectic-paper: nonparametric chain policy with certified snippet radii

- **Computes:** a policy that reaches S_tgt by concatenating demonstrated control snippets, each valid on a
  certified ball, for lossless Hamiltonian systems.
- **How:** assignment set K = {(x_i, r_i, u_i)} (Def. 6), normalized nearest-neighbour selection with default
  zero input (Def. 7, Remark 2). Radius from a demonstration snippet (§III-D):
  r_i(t) = [ΔH(x_i) − ΔH(φ(t,x_i,u_{i,t})) − v_0 t] / (L_H + L_H e^{Lt}) (Grönwall + Lipschitz energy distance,
  (5)-(7)); Alg. 1 extracts snippets along each demonstration.
- **Guarantee:** Thm 2: local energy decrease + energy coverage + ergodic coverage ⇒ a.e. x_0 ∈ S_0 reaches
  S_tgt; Thm 4: finite-time bound T_max ≤ (L_H D_X / v_0)(1 + T_1/τ_min) + T_2 under return-time bounds
  (Assumption 8). Data requirement scales with the energy interval and ergodic index, not with state dimension
  (Remark 4).
- **Breaks when:** dissipative or forced systems (no energy-layer recurrence); Assumption 3 (target meets every
  ergodic component) — deferred to a journal version.
- **Hooks:** certify a library of decision snippets once (offline) and reuse them online; recurrence as a
  substitute for coverage.
