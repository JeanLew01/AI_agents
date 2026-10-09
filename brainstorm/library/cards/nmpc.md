# Mechanism cards: NMPC collection

Scout pass of 2026-10-06 (session `2026-10-06_tro2027-diffusion-control`). Sources: `~/.claude/skills/<skill>/references/paper.md`.
Citations are `skill §section (eq. n)` or `Alg. n, l. m`. Anything marked "(inferred)" is the scout's derivation, not a
statement of the paper. Verbatim equations are collected at the end of the file.

Skills read: `dial-mpc-paper` (DIAL), `model-based-diffusion-paper` (MBD), `pac-nmpc-paper` (PAC-23),
`pac-nmpc-value-function-paper` (PAC-25), `rl-guided-pac-nmpc-paper` (PAC-26). Skimmed for hardware and application
cues: `post-stall-navigation-paper`, `urban-swarm-fixed-wing-paper`.

---

## DIAL-MPC (Xue, Pan, Yi, Qu, Shi; arXiv 2409.15610, ICRA 2025)

### dial-mpc-paper: MPPI as a single-step diffusion (Proposition 1)

- **Computes:** one MPPI update of the control sequence U = u_{t:t+H}, read as one score-ascent step on the Gaussian-smoothed target p_1 = p_0 * φ, with p_0(U) ∝ exp(−J(U)/λ) and φ = N(0, Σ).
- **How:** §III-A, (1) MPPI update; Prop. 1 (2) U⁺ = U + Σ ∇log p_1(U); proof (3a)–(3f): move the gradient into the convolution, differentiate the Gaussian kernel, flip the sign of W, Monte Carlo approximation with N_W samples. Proposition "adopted from [43]" (= MBD).
- **Guarantee:** none beyond the identity; (3f) is a Monte Carlo approximation, no error bound stated. Footnote 1: (2) "does not have scaling factor or extra noise" compared with diffusion models.
- **Cost:** N_W rollouts of the full model per update (N_W = 2048 in all experiments, §IV-A, App. A).
- **Knobs:** Σ (kernel = sampling covariance = step size), λ (temperature; its value is not reported), N_W.
- **Breaks when:** fixed Σ: "MPPI may either over-explore or over-exploit" (§III-B, Fig. 4); a large det Σ shifts the optimum of p_1 away from U* ("distorted optimum", §III-B).
- **Hooks:** any sampler whose update is a softmax-weighted mean of Gaussian perturbations inherits this reading; the weighted mean is a self-normalized importance-sampling (SNIS) estimate of a Tweedie posterior mean (inferred; see identities below).

### dial-mpc-paper: trajectory-level annealing (outer loop)

- **Computes:** a decreasing sequence of sampling kernels Σ^N, …, Σ^1 for the N update iterations at one control step, so that early iterations ascend a heavily smoothed p_i and later ones a sharper one.
- **How:** generic diffusion schedule (4) det(Σ^i) = exp(−(N−i) d/(βN)); trajectory-level version (5) det(Σ^i_{t:t+H}) ∝ exp(−(N−i) H d_u/(β_1 N)); Alg. 1 l. 3–9 (loop printed as i = 1..N; the text anneals i = N..1, conversion note).
- **Guarantee:** none. Rationale: coverage–convergence trade-off (§III-B, Fig. 3–4).
- **Cost:** N × N_W rollouts per control step. Real-time runs: N_W = 2048, H = 20 (0.4 s), 50 Hz on an RTX 4090 in JAX/Brax (App. A). N and β_1 for the real-time tasks are not reported; the offline crate climb uses 4 annealing steps, 4096 samples, 40-step horizon, 30 s for a 2 s plan (App. B).
- **Knobs:** N, β_1, the final level Σ^1. §IV-C: "By controlling the final noise level, we can achieve a suboptimal but robust solution given a mismatched model" (claim, no analysis).
- **Breaks when:** "requires fast simulation to generate samples, which limits the application of DIAL-MPC in longer planning horizon tasks" (§V). Only Σ is annealed; λ stays fixed (§III-C, Alg. 1).
- **Hooks:** the stage index i is the only schedule input; nothing in the paper ties Σ^i to uncertainty, risk or constraints.

### dial-mpc-paper: action-level annealing and the dual loop

- **Computes:** a covariance that grows along the horizon, so actions far in the future are sampled more widely than the next action.
- **How:** (6) det(Σ^i_{t+h}) ∝ exp(−(H−h) d_u/(β_2 H)), h = 0..H; isotropic realization combining both loops (7) Σ^i_{t+h} = exp(−(N−i)/(β_1 N) − (H−h)/(β_2 H)) I; receding-horizon shift (Alg. 1, l. 10). Under the dual loop each action u_H receives N·H updates with kernels Σ^N_H..Σ^1_H; Σ^N_{H−1}..Σ^1_{H−1}; …; Σ^N_0..Σ^1_0 before it is applied (§III-C).
- **Stated rationale (verbatim):** "The covariance matrix increases with time as h increases, allowing for a larger sampling region for future control actions that have been updated fewer times compared to those at the front of the horizon." The reason is the number of refinements an action has received, not prediction uncertainty or disturbance growth.
- **Guarantee:** none.
- **Cost:** none beyond the trajectory loop.
- **Knobs:** β_2; the spline reparameterization of the controls (mentioned only in App. B, "the spline reparameterization trick used in DIAL-MPC").
- **Breaks when:** (inferred) without re-planning (commit the whole horizon) the late actions never receive the extra refinements the schedule assumes.
- **Hooks:** (inferred) with re-planning every M steps, the action now at slot h has been refined in about (H−h)/M earlier planning cycles; (6) makes the variance a decreasing function of that count. Any per-step quantity that should depend on "how many more times will this step be re-planned" can reuse the same index.

DIAL's treatment of constraints, safety, disturbances and uncertainty: the OCP lists state and control constraints 𝒳, 𝒰 (§III-A), but the method never handles them (no projection, penalty or feasibility test is described); tasks use reward terms such as contact penalties (Tables IV–VI). There is no disturbance model. Uncertainty appears only as model mismatch: 2 kg base mass in simulation (Table III), 7–10 kg payload with the model updated in the planner ("update the model parameters in all sampling-based MPCs accordingly", App. B), and ground-truth state from motion capture (App. A). "Safety" appears only in a reference title.

---

## MBD (Pan, Yi, Shi, Qu; NeurIPS 2024)

### model-based-diffusion-paper: Monte Carlo score ascent with a model-based score

- **Computes:** a deterministic reverse pass Y^(N) → Y^(0) that moves one trajectory toward the high-density region of p_0(Y) ∝ exp(−J(Y)/λ) (unconstrained case, §4.1).
- **How:** backward step (6) Y^(i−1) = (Y^(i) + (1−ᾱ_i) ∇log p_i(Y^(i)))/√α_i; score by Bayes' rule (7a)–(7c); swap parameter and variable in the forward Gaussian to get the proposal φ_i = N(Y^(i)/√ᾱ_i, I/ᾱ_i − I) (8); Monte Carlo estimate with weights p_0 (9a)–(9b); Alg. 1 (l. 3 samples from N(Y^(i)/√ᾱ_{i−1}, (1/ᾱ_{i−1} − 1)I), an index shift relative to (8)). Step size (1−ᾱ_i) justified as 1/L for a (1−ᾱ_i)^{-1}-smooth log p_i at low temperature (§4.1, footnote 2).
- **Equivalence stated by the paper:** N = 1 reduces to the Cross-Entropy Method with Σ_CEM = (1/α_0 − 1)I (§4.1 "Connection with Sampling-based Optimization").
- **Equivalence (inferred):** substituting (9b) into (6) gives Y^(i−1) = √ᾱ_{i−1} Ȳ^(0)(𝒴^(i)): every step is "estimate the clean trajectory by SNIS, rescale it to noise level i−1, add no noise" (DDIM with η = 0 and the predicted-noise term dropped). In Ȳ^(0) coordinates MBD is the MPPI/DIAL mean update with covariance σ_i² I, σ_i² = 1/ᾱ_i − 1.
- **Guarantee:** about the target, not the algorithm: Prop. 2 (J(Y) → J* in probability as λ → 0 if the sub-level volume V_J(t) is sandwiched by polynomials), Prop. 4 (Y → Y* in probability for a unique minimizer with J*_𝔅(δ) strictly increasing), Prop. 5 (Y^(i) → N(√ᾱ_i Y*, √(1−ᾱ_i) I) in distribution; the covariance is printed as √(1−ᾱ_i), probably a typo for 1−ᾱ_i) (App. A.2). No finite-sample or convergence result for the Monte Carlo algorithm; §6 lists "theoretically understanding its convergence" as future work.
- **Cost:** N = 100 diffusion steps × 100–300 samples per step (Table 4); 16–35 s per 50-step trajectory on an RTX 4070 Ti, the same as CEM/MPPI with matched budgets (Table 3).
- **Knobs:** λ (0.1–0.4, Table 4), the β schedule (linear 1e-4 → 1e-2, α_i = 1 − β_i, App. A.5.2), N, sample count (converges "with as few as 128 samples", A.7). With this schedule ᾱ_N ≈ 0.60, so the proposal standard deviation runs from about 0.81 to 0.01 (inferred arithmetic).
- **Breaks when:** the paper states no failure mode for the unconstrained case. (Inferred) weights p_0 ∝ e^{−J/λ} degenerate when the spread of J over a batch is much larger than λ.
- **Hooks:** the weighted mean Ȳ^(0) is the slot where any other weight (constraint, risk, belief, demonstration) enters; the β schedule is a free design object ("optimizing the standard Gaussian forward process using the model information" is listed as future work, §6).

### model-based-diffusion-paper: constrained TO by rollout feasibility and indicator weights

- **Computes:** the same reverse pass for the target (2) p_0 ∝ p_d p_J p_g, with p_d a product of dynamics indicators and p_g ∝ ∏_t 1(g_t(x_t, u_t) ≤ 0).
- **How:** draw samples from φ_i, keep their control part and roll it through the dynamics (shooting) to obtain feasible samples 𝒴_d^(i) (Alg. 2 l. 4); weight by w = p_J p_g (10b)–(10d). Infeasible samples (state constraints violated) get weight 0.
- **Guarantee:** none for constraint satisfaction.
- **Cost:** as above, one rollout per sample.
- **Knobs:** the constraint enters only through the hard indicator; there is no margin or soft penalty in the paper.
- **Breaks when:** "the combinatorial explosion of the constrained space … leading to low constraint satisfaction rates" for long horizons (§4.2). The case where every sample in a batch is infeasible (all weights zero) is not discussed (inferred gap). Footnote 1: deterministic dynamics assumed; "The extension to stochastic dynamics is straightforward" (claim, not shown).
- **Hooks:** a chance constraint would replace the indicator by a probability; a feasibility-first rule would replace the zero weights by a violation-depth weight (neither is in the paper).

### model-based-diffusion-paper: demonstration-augmented target with max-weights

- **Computes:** a score estimate that follows a demonstration while samples are poor and the model once samples are better.
- **How:** demonstration as noisy observation p(Y_demo | Y^(0)) = N(Y^(0), σ²I); instead of the posterior product, a mixture target (11) with η chosen by (12) and per-sample weight (13) w = max{p_d p_J p_g(Y^(0)), p_demo(Y^(0)) p_J(Y_demo) p_g(Y_demo)}. A.4 explains why: the product "will draw samples to both model and demonstration data" and compromise; the max lets the demonstration dominate early and the model later (Fig. 6). Data may be infeasible (RRT on simplified dynamics for Car2D U-maze) or partial-state (mocap torso/thigh/shin for humanoid jogging) (§5.2).
- **Guarantee:** none.
- **Cost:** negligible over plain MBD.
- **Knobs:** σ (demonstration width), the scaling constants p_J(Y_demo), p_g(Y_demo).
- **Breaks when:** not stated.
- **Hooks:** a reference trajectory (previous plan, certainty-equivalent plan, a feasible fallback) can enter through the max-weight as a floor on the weights.

### model-based-diffusion-paper: receding-horizon MBD

- **Computes:** closed-loop control by re-solving with "single-step MBD" from the shifted previous solution (Alg. 3, A.6).
- **How:** Alg. 3 l. 3–6.
- **Guarantee:** none.
- **Cost:** 3.5–10 Hz for 50-step problems on an RTX 4070 Ti (Table 7).
- **Breaks when:** not stated; with 5 % control noise the receding-horizon version still beats RL by 65.3 % (Fig. 7).
- **Hooks:** online use requires the warm start; the paper does not describe how the noise level is reset between steps.

---

## PAC-NMPC family (Polevoy, Kobilarov, Moore et al., JHU APL / JHU ME)

### pac-nmpc-paper: PAC bound on expected cost and violation probability of a policy distribution

- **Computes:** with probability ≥ 1−δ over the sampled data, an upper bound 𝒥⁺_α(ν) on 𝒥(ν) = E_{τ,ξ∼p(·,·|ν)}[J(τ)] and 𝒞⁺_α(ν) on 𝒞(ν) = P(g(τ) > 0) = E[𝕀{g(τ) > 0}]. The expectation is over the joint law (1) p(τ, ξ | ν) = p(τ | ξ) p(ξ | ν): policy parameters ξ drawn from a Gaussian surrogate N(μ, diag Σ) over the nominal control trajectory, and the trajectory drawn from the stochastic dynamics (the disturbance) given that policy (§III-A, §III-B).
- **How:** (2) 𝒥⁺_α = 𝒥̂_α + α d(ν) + Φ_α(δ); Catoni-type robust estimator (4) with ψ(x) = log(1 + x + x²/2) on importance-weighted costs ℓ_ij = J(τ_ij) p(ξ_ij|ν)/p(ξ_ij|ν_i) (5) pooled over L prior distributions × M samples; distance (6) d(ν) = (1/2L) Σ_i b_i² exp(D_2(p(·|ν) ‖ p(·|ν_i))) (Rényi-2), requiring bounded costs 0 ≤ J ≤ b_i (7); concentration term (8) Φ_α(δ) = log(1/δ)/(αLM). Combined objective (9) ν_{i+1} = argmin_ν min_{α>0} (𝒥⁺_α + γ 𝒞⁺_α), solved "using a GPU implementation of L-BFGS-B" with "self-normalized importance weights to compute ℓ_ij … and analytical gradients" (§III-B). Alg. 2 iterates sampling (GPU) and bound minimization.
- **Guarantee:** the bound holds with probability 1−δ for "policies sampled from p(ξ|ν*)" (§V-A: "It is guaranteed that policies sampled from p(ξ|ν*) will have an expected cost of ≤ 𝒥⁺ and an expected constraint (probability of collision) of ≤ 𝒞⁺ with a 95% chance"). Derived in ref. [10] (Kobilarov, sample complexity bounds for ISPO); the papers do not restate whether it holds uniformly over the data-selected ν* and α*, nor how self-normalized weights affect it.
- **Cost:** L = 5, M = 1024 (sim), L = 2 (rally car), L = 1 (fixed-wing); 15.9 ms per iteration open-loop and 18.5 ms with feedback (RTX 2070 laptop, 20-step trajectory, 500 offline iterations).
- **Knobs:** δ, γ (constraint weight, "heuristically selected", 10 in all PAC-23 runs), α (optimized inside the bound), L, M, the bound b_i on costs (costs are normalized "to achieve tighter PAC bounds" in PAC-25/26).
- **Breaks when:** the bound is only as good as the sampled dynamics model: optimizing with nominal dynamics made the Monte Carlo estimates exceed the bounds (Fig. 2a,b; bounds held in 93.9 % of planning intervals with nominal dynamics, 64.7 % without feedback, vs 99.8 % with stochastic dynamics, §V-B). Validation compares against Monte Carlo under the same simulated model, not against realized outcomes ("Monte Carlo estimates refer to sampled trajectories using the simulated stochastic dynamics model", §VI-A-3).
- **Floor (inferred from (2), (6), (8)):** for the indicator constraint (b = 1) the Catoni term is ≥ 0 and e^{D_2} ≥ 1, so min_α gives 𝒞⁺ ≥ √(2 ln(1/δ)/(LM)) whatever the data: 7.6 % (LM = 1024), 5.4 % (2048), 3.4 % (5120) at δ = 0.05. This matches the reported "≤ 5 %" (sim, LM = 5120), "≤ 10 %" (rally car, LM = 2048) and "around 10 %" (fixed-wing, LM = 1024). A one-sided Clopper–Pearson bound for 0 failures in n samples is about ln(1/δ)/n (0.29 % at n = 1024).
- **Hooks:** the decision variables are the mean and the diagonal covariance of a Gaussian over controls, the same object an annealed sampler carries; the certificate is an explicit function of that covariance.

### pac-nmpc-paper: PAC feedback motion planning (certify the closed-loop-over-horizon policy)

- **Computes:** samples of the trajectory under a local feedback policy (10) u_t = K_t(τ^d(ξ, x_0))(x_t^d(ξ, x_0) − x_t) + u_t^d(ξ), with the nominal trajectory from deterministic dynamics (11) and TVLQR gains per sampled nominal.
- **How:** two-stage sampling, Alg. 4: nominal rollout, TVLQR, feedback rollout with stochastic dynamics.
- **Guarantee:** as above, for the feedback policy over the planning horizon N_T.
- **Cost:** +16 % per iteration (18.5 vs 15.9 ms).
- **Knobs:** TVLQR weights; policy parameterized only by the nominal inputs (the gains are not decision variables).
- **Breaks when:** not stated; gives "a tighter distribution in state-space" and lower bounds (Fig. 2e–h, Fig. 3).
- **Hooks:** the certified object is a committed feedback policy over the whole horizon, not the re-planning loop.

### pac-nmpc-paper: receding-horizon PAC-NMPC with warm-started priors

- **Computes:** at each planning interval (period H = 0.2 s, horizon 12 × 0.1 s), an optimized ν̂*, and its bounds; executes the TVLQR policy around the mean μ.
- **How:** Alg. 5: Optimize (Alg. 2), maximum likelihood estimate u^d = μ, nominal rollout, TVLQR, Trim, Execute, InitializePrior (Alg. 6: propagate the trimmed mean through the feedback policy, extend the mean with zeros and the variance with its last value, floor the variance at η_min "to prevent it from starting too small, which would inhibit exploration").
- **Guarantee:** "the minimized bounds themselves provide a statistical guarantee for each planning interval" (§I). The executed policy is the mean, while the bound is for the randomized policy ξ ∼ p(·|ν*) (§IV-C). The interpolation from 10 Hz to 50 Hz is executed "with the assumption that our PAC bounds will still hold" (§V-B).
- **Cost:** sim 54 iterations per 0.2 s interval (≈ 3.7 ms each); rally car 10 iterations × 20 ms on a Jetson Orin; fixed-wing (17 states, 4 inputs, L = 1, finite-difference linearization on the prior mean) 22 iterations × 8.5 ms on an RTX 3080.
- **Results:** bound violated in 1 of 482 intervals (sim); rally car bounds ≤ 10 % held at all intervals; on hardware, optimizing with nominal dynamics collided with virtual obstacles with and without feedback, stochastic without feedback collided twice (§VI-A-3). In the offline trajectory-optimization study (§V-A, Fig. 4), compared with RA-MPPI (CVaR) and KL-regularized empirical optimization, PAC-NMPC reached the lowest estimated cost and collision probability.
- **Knobs:** η_min, H, N_T, L, M.
- **Breaks when:** unmodeled dynamics not captured by the GMM noise model (§VI-A-3).
- **Hooks:** the prior variance floor η_min and the "extend with the last variance" rule are a hand-set re-noising schedule between planning intervals.

### pac-nmpc-value-function-paper: learned value function as terminal cost and constraint, with MC dropout inside the bound

- **Computes:** a PAC-NMPC policy whose cost includes q_f(x_{N_T}) = −V^{ψφ}(x_{N_T}, ℓ̂_{N_T}) (TD3 critic evaluated at the actor's action, with the terminal LiDAR scan predicted geometrically) and whose violation indicator also fires if the value does not improve, c_V = (V(x_{N_T}, ℓ̂_{N_T}) − V(x_0, ℓ_0) < 0) (6).
- **How:** §IV-B, §IV-C; one dropout mask per sampled trajectory for actor and critic, so network uncertainty enters the sampled costs at no extra inference cost (§V-A).
- **Guarantee:** the PAC bounds of PAC-23, now over dynamics noise and dropout masks; "The performance guarantees on the value function assume that this future sensor prediction is accurate" (§IV-C).
- **Cost:** L = 5, M = 1024, 12 steps, replan 0.2 s; TD3 training (fixed-wing: 3 M steps, 4.5 h).
- **Results:** with dropout sampling the expected-cost bound was never violated and the violation bound in 0.34 % of intervals; without dropout 65.49 % and 1.45 % (§V-B). No constraint violations in the cluttered and concave-trap sims; MPPI with the same value function as baseline.
- **Knobs:** γ (2 cluttered, 4 traps), cost normalization, dropout rate.
- **Breaks when:** "assumed the ability to adequately predict future sensor measurements … as well as an accurate stochastic dynamics model"; MC dropout cannot capture aleatoric (sensor) noise; "can be affected by uncalibrated uncertainty estimates" (§VII).
- **Hooks:** the generative model whose samples enter the bound (here dropout networks) is treated exactly like the stochastic dynamics; the guarantee is relative to that model.

### rl-guided-pac-nmpc-paper: RL warm start, final variance shrink, infeasibility fallback

- **Computes:** the initial mean μ of the surrogate from an actor rollout through nominal dynamics with a learned sensor predictor ŷ_{t+k} = h^η(x_t, y_t, x_{t+k}) (predicted directly from the current scan, not recursively); the initial variance is "a prespecified high variance to promote exploration" (§V-A, Alg. 1).
- **How:** Alg. 1; if any step of the actor rollout violates the constraint, warm start from the previous PAC-NMPC policy instead (l. 6–8). Final step: "we can perform a final PAC-NMPC policy optimization iteration in which the variances are reduced to a prespecified small value. This produces PAC guarantees that more accurately reflect the executed policies and are often tighter" (§V-A). The paper does not say whether that last iteration draws fresh samples.
- **Guarantee:** inherits the PAC bounds.
- **Cost:** negligible beyond actor and sensor-model inference.
- **Knobs:** initial and final variances.
- **Breaks when:** "when the warm-start produces a trajectory that is severely infeasible … the PAC-NMPC policy distribution may not sample any feasible trajectories. The lack of feasible trajectories in this case will result in failed optimization" (§V-A). Ablation: without RL warm start 11 % success, without learned sensor prediction 3 %, with both 90 % (Table VII).
- **Hooks:** a two-level variance (explore wide, certify narrow) is an annealing schedule with two stages, set by hand.

### rl-guided-pac-nmpc-paper: hard-constrained PAC bounds with a separate value-improvement certificate

- **Computes:** (17) ν* = argmin_ν min_{α>0}(𝒥⁺_α + γ𝒞⁺_α) s.t. 𝒞⁺_α(ν) ≤ ε_c and 𝒞_𝒱⁺_α(ν) ≤ E[V(x_t, y_t)], where 𝒞_𝒱⁺ bounds E[V(x_{t+N_T}, ŷ_{t+N_T})] (15)–(16). Solved with SNOPT (SQP).
- **Guarantee:** two PAC statements per interval (safety and expected value decrease over the horizon), matching Def. III.6, P(P(x_{t+i} ∈ 𝒮 ∀ i ≤ N_T | x_t) ≥ 1−β_𝒮) ≥ 1−δ_𝒮. Explicit limitation: "These bounds are local to each finite-horizon policy and conditional on current observations. Thus, they provide finite-time guarantees and do not guarantee global safety for closed-loop execution of the controller over the infinite horizon" (§IV-A).
- **Cost:** fixed-wing: 11 steps × 0.1 s, re-planning every step (H = 0.1 s), L = 1, M = 1024, δ = 0.05, γ = 2, ε_c = 0.1 (§VII-D-1); laptop i9-13900H with RTX 4080.
- **Results:** fixed-wing sim 90 % success (Table VI), out of distribution 76 % vs actor 46 % (Table VIII), hardware with depth camera 80 % vs 40 % for actor and for map + A* (Table IX).
- **Knobs:** ε_c, γ, δ.
- **Breaks when:** sensor spikes cause spikes in 𝒞⁺ (Fig. 14–15); value-gap e_V unknown (52).
- **Hooks:** the value-improvement bound is a certified Lyapunov-like decrease over one planning horizon, not across intervals.

### rl-guided-pac-nmpc-paper: feasible-descent analysis (Thm VIII.1, VIII.2)

- **Computes:** an existence argument: for a large enough constraint penalty γ_c in RL training and a nonempty set of feasible low-constraint-cost policies Π_ε^c, there is a feasible input (or feasible feedback-policy parameter ξ_c) near the optimal penalized policy that strictly decreases the value function.
- **How:** Lemma VIII.1 (continuity gives a descent neighborhood), Lemma VIII.2 (penalty drives constraint-to-go below ε), Thm VIII.1 (one step), Thm VIII.2 (multi-step feedback policy, needs Ξ compact and a rich enough parameterization).
- **Guarantee:** existence only, for the optimal value function; §VIII-C notes the learned V has an unknown gap e_V.
- **Hooks:** a justification for searching near a learned prior proposal; a Dubins-car experiment supports it (Fig. 18).

---

## Application papers (hardware cues only)

### post-stall-navigation-paper: uncertainty-aware collision constraints in direct NMPC

- **Computes:** direct-collocation NMPC (Hermite–Simpson) on an RRT seed with a NanoMap point-cloud history; collision constraints as distance, distance with standard-deviation inflation, or probability of collision (max 0.5, radius 1.2 m) (§III, §IV-C).
- **Result:** with injected state-estimation noise (variance 0.1 per axis) and depth noise, constraint breaches fell from 17.2 % (plain distance) to 1 % (σ-inflation or probability constraint) (Fig. 2d–f). Hardware: 42-inch Edge540XL, RealSense D455, 5 Hz replanning, 1 s horizon (§V).
- **Hooks:** uncertainty-aware constraints paid off when the state was estimated with noise and the map was partial.

### urban-swarm-fixed-wing-paper: certainty-equivalent wind compensation

- **Computes:** NMPC (10 knot points, ≈ 0.1 s warm-started SNOPT solve on an Intel NUC) with the ArduPilot EKF wind estimate inserted into the planning model, "we assumed that the wind is constant over the planning horizon (≈ 1 s)" (§6.7, §4, §6.1).
- **Result:** large reduction of roll oscillations in a ≈ 3 m/s headwind (Fig. 15).
- **Hooks:** a field-proven instance of the disturbance-observer and certainty-equivalence design.

---

## Verbatim equations

DIAL (§III-A, III-B, III-C):

$$U^+ = U + \frac{\sum_{i=1}^{N_W} \exp\left(-\frac{J(U + [W]_i)}{\lambda}\right) [W]_i}{\sum_{j=1}^{N_W} \exp\left(-\frac{J(U + [W]_j)}{\lambda}\right)}, \tag{1}$$

**Proposition 1 (Adopted from [43]):** The MPPI update (1) can be viewed as a one-step ascent with the score function $\nabla \log p_1(U)$ with a learning rate $\Sigma$:
$$U^+ = U + \Sigma \cdot \nabla \log p_1(U). \tag{2}$$

$$\nabla \log p_1(U) = \frac{\nabla p_1(U)}{p_1(U)} = \frac{\nabla \left(p_0(U) \ast \phi(U) \right)}{p_1(U)} \tag{3a}$$
$$= \frac{p_0(U) \ast \nabla \phi(U)}{p_1(U)} = -\frac{p_0(U) \ast (\phi(U) \Sigma^{-1}U)}{p_1(U)} \tag{3b}$$
$$= - \Sigma^{-1} \frac{\int p_0(U-W) \phi(W) W dW}{\int p_0(U-W) \phi(W) dW} \tag{3c}$$
$$= - \Sigma^{-1} \frac{\mathbb{E}_{W\sim\phi(\cdot)} \left[ p_0(U-W) W \right]}{\mathbb{E}_{W\sim\phi(\cdot)} \left[ p_0(U-W) \right]} \tag{3d}$$
$$= \Sigma^{-1} \frac{\mathbb{E}_{W\sim\phi(\cdot)} \left[ p_0(U+W) W \right]}{\mathbb{E}_{W\sim\phi(\cdot)} \left[ p_0(U+W) \right]} \tag{3e}$$
$$\approx \Sigma^{-1} \frac{\sum_{i=1}^{N_W} \exp\left(-\frac{J(U + [W]_i)}{\lambda}\right) [W]_i}{\sum_{j=1}^{N_W} \exp\left(-\frac{J(U + [W]_j)}{\lambda}\right)}. \tag{3f}$$

$$\det\left(\Sigma^{i}\right) = \exp\left(-\frac{N-i}{\beta N} d\right),\quad \forall i \in \{N, \ldots, 1\}, \tag{4}$$
$$\det\left(\Sigma^i_{t:t+H}\right) \propto \exp\left(-\frac{N-i}{\beta_1 N} H d_u \right), \quad \forall i \in \{N, \ldots, 1\}, \tag{5}$$
$$\det\left(\Sigma^i_{t+h}\right) \propto \exp\left(-\frac{H-h}{\beta_2 H} d_u \right), \quad \forall h \in \{0, \ldots, H\}, \tag{6}$$
$$\Sigma^i_{t+h} = \exp\left(-\frac{N-i}{\beta_1 N} - \frac{H-h}{\beta_2 H} \right) I. \tag{7}$$

MBD (§3, §4.1–4.3):

$$p_0(Y) \propto p_d(Y) p_J(Y) p_g(Y) \tag{2}$$
$$p_{i|0}(\cdot | Y^{(0)}) \sim \mathcal{N}(\sqrt{\bar{\alpha}_i} Y^{(0)}, (1-\bar{\alpha}_i) I), \quad \bar{\alpha}_i = \prod_{k=1}^{i} \alpha_k. \tag{3}$$
$$Y^{(i-1)} = \frac{1}{\sqrt{\alpha_i}} \left(Y^{(i)} + (1-\bar{\alpha}_i) \nabla_{Y^{(i)}} \log{p_i(Y^{(i)})}\right) \tag{6}$$
$$\phi_i(Y^{(0)}) \propto p_{i \mid 0}(Y^{(i)} \mid Y^{(0)}) \propto \exp(-\frac{1}{2} \frac{\left(Y^{(0)} - \frac{Y^{(i)}}{\sqrt{\bar{\alpha}_i}}\right)^\top \left(Y^{(0)} - \frac{Y^{(i)}}{\sqrt{\bar{\alpha}_i}}\right)}{\frac{1-\bar{\alpha}_i}{\bar{\alpha}_i}}) \propto \mathcal{N}(\frac{Y^{(i)}}{\sqrt{\bar{\alpha}_i}}, \frac{I}{\bar{\alpha}_i} - I) \tag{8}$$
$$\nabla_{Y^{(i)}} \log{p_i(Y^{(i)})} = -\frac{Y^{(i)}}{1-\bar{\alpha}_i} + \frac{\sqrt{\bar{\alpha}_i}}{1-\bar{\alpha}_i} \frac{\int Y^{(0)} \phi_i(Y^{(0)}) p_0(Y^{(0)}) \, dY^{(0)}}{\int \phi_i(Y^{(0)}) p_0(Y^{(0)}) \, dY^{(0)}} \tag{9a}$$
$$\approx -\frac{Y^{(i)}}{1-\bar{\alpha}_i} + \frac{\sqrt{\bar{\alpha}_i}}{1-\bar{\alpha}_i} \underbrace{\frac{\sum_{Y^{(0)} \in \mathcal{Y}^{(i)}} Y^{(0)} p_0(Y^{(0)})}{\sum_{Y^{(0)} \in \mathcal{Y}^{(i)}} p_0(Y^{(0)})}}_{\text{Monte Carlo Approximation}} := -\frac{Y^{(i)}}{1-\bar{\alpha}_i} + \frac{\sqrt{\bar{\alpha}_i}}{1-\bar{\alpha}_i} \bar{Y}^{(0)}(\mathcal{Y}^{(i)}) \tag{9b}$$
$$\bar{Y}^{(0)} = \frac{\sum_{Y^{(0)} \in \mathcal{Y}^{(i)}_d} Y^{(0)} w(Y^{(0)})}{\sum_{Y^{(0)} \in \mathcal{Y}^{(i)}_d} w(Y^{(0)})}, \quad w(Y^{(0)}) = p_J(Y^{(0)}) p_g(Y^{(0)}) \tag{10d}$$
$$p'_0(Y^{(0)}) \propto (1-\eta) p_d(Y^{(0)}) p_J(Y^{(0)}) p_g(Y^{(0)}) + \eta p_{\text{demo}}(Y^{(0)}) p_J(Y_{\text{demo}}) p_g(Y_{\text{demo}}) \tag{11}$$
$$w(Y^{(0)}) = \max{\left\{ p_d(Y^{(0)}) p_J(Y^{(0)}) p_g(Y^{(0)}),\; p_{\text{demo}}(Y^{(0)}) p_J(Y_{\text{demo}}) p_g(Y_{\text{demo}}) \right\}} \tag{13}$$

MBD Table 1 (Comparison of MBD and model-free diffusion, MFD):

| Aspect | MBD | MFD |
| --- | --- | --- |
| Target Distribution | Known (Eq. (2)), but hard to sample | Unknown, but have data |
| Objective | Sample Y^(0) from high-likelihood region of p_0(·) | Sample Y^(0) ∼ p_0(·) |
| Score Approximation | Estimated using the model (Eq. (9a)). Can be augmented with demonstrations (Eqs. (11) and (13)) | Learned from data |
| Backward Process | Perform Monte Carlo score ascent (Eq. (6)) to move samples towards most-likely states | Run reverse SDE to preserve sample diversity |

PAC-NMPC (PAC-23 §III-B; same equations in PAC-25 (1) and PAC-26 (4)–(10)):

$$\mathcal{J}^+_\alpha(\boldsymbol{\nu}) \triangleq \widehat{\mathcal{J}}_\alpha(\boldsymbol{\nu}) + \alpha d(\boldsymbol{\nu}) + \Phi_{\alpha}(\delta) \tag{2}$$
$$\mathcal{J}(\boldsymbol{\nu}) =\mathbb{E}_{\boldsymbol{\tau}, \boldsymbol{\xi} \sim p(\cdot, \cdot|\boldsymbol{\nu}_0)}\bigg[J(\boldsymbol{\tau})\frac{p(\boldsymbol{\xi}|\boldsymbol{\nu})}{p(\boldsymbol{\xi}|\boldsymbol{\nu}_0)}\bigg]. \tag{3}$$
$$\widehat{\mathcal{J}}_\alpha(\boldsymbol{\nu}) \triangleq \frac{1}{\alpha LM} \sum_{i=0}^{L-1} \sum_{j=1}^{M} \psi\left(\alpha \ell_{ij} \right),\qquad \psi(x) = \log\left(1+x+\tfrac{1}{2}x^2\right) \tag{4}$$
$$\ell_{ij} = J(\boldsymbol{\tau}_{ij})\frac{p(\boldsymbol{\xi}_{ij}|\boldsymbol{\nu})}{p(\boldsymbol{\xi}_{ij}|\boldsymbol{\nu}_i)} \tag{5}$$
$$d(\boldsymbol{\nu}) \triangleq \frac{1}{2L}\sum_{i=0}^{L-1}b_i^2e^{D_2\left(p(\cdot | \boldsymbol{\nu})||(p(\cdot | \boldsymbol{\nu}_i)\right)} \tag{6}$$
$$0 \leq J(\boldsymbol{\tau}_{ij}) \leq b_i \; \forall j = 0, ..., M \tag{7}$$
$$\Phi_{\alpha}(\delta) \triangleq \frac{1}{\alpha LM}\log\frac{1}{\delta}. \tag{8}$$
$$\boldsymbol{\nu}_{i+1} = \boldsymbol{\nu}^* = \operatorname*{arg\,min}_{\boldsymbol{\nu}}\min_{\alpha>0} (\mathcal{J}^+_\alpha(\boldsymbol{\nu}) + \gamma \mathcal{C}^+_\alpha(\boldsymbol{\nu})) \tag{9}$$

PAC-25 statement of the guarantee: P(E_{τ,ξ∼p(·,·|ν)}[J(τ)] ≤ 𝒥⁺_α(ν)) ≥ 1−δ and P(E_{τ,ξ∼p(·,·|ν)}[C(τ)] ≤ 𝒞⁺_α(ν)) ≥ 1−δ.
