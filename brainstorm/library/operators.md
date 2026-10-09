# Combination operators

Moves for turning several methods into one idea. Generators apply them on purpose and name the ones they used in
each idea card (`operators: [ISO, PSEUDO]`). Critics check the "test" line of each operator used.

An idea that only lists components that each keep their own job ("A estimates, B plans, C certifies") is glue, not
a combination. Glue is allowed as a baseline, not as a contribution.

| Code | Move | What it looks like | Test that it is real |
|---|---|---|---|
| ISO | Same computation, two readings | Two components turn out to be one algorithm (e.g. the Monte Carlo score of model-based diffusion and diffusion resampling are both self-normalized importance sampling of a Tweedie posterior mean, with the roles of proposal and weight swapped). | Write the identity as one equation. If it only holds "in spirit", it is an analogy, not ISO. |
| TARGET | Write the joint target | Define the probability measure (often a Feynman–Kac path measure: reference law times potentials) whose exact sampler is the proposed method. Components become factors or potentials. | Which variables are tilted by which factor? Tilting nature (disturbance, belief) by the controller's cost gives optimistic plans; the target must marginalize nature, not optimize it. |
| PSEUDO | Unbiased estimate in place of an intractable factor | An intractable probability (chance constraint, reach-avoid probability, evidence) enters a sampler through a positive unbiased estimate, and the sampler still targets the exact law (pseudo-marginal MCMC, random-weight importance sampling). | Is the estimate unbiased and nonnegative for the factor actually used (a power P^β needs β independent draws, not one)? What does its relative variance do to the effective sample size? |
| SCHED | Couple schedules | One method's schedule (noise level, temperature, particle or scenario count, safety margin, confidence level) is set by a quantity of another component. | Is there a monotonicity or an invariant that justifies the coupling, or is it a heuristic with a free constant? State it. |
| REUSE | Same samples, two uses | Rollouts drawn by the optimizer are data for a reachability or calibration estimator, or filter particles are scenarios for the planner. | Selection bias: data used to choose an object cannot certify it without a holdout split, a union bound over a fixed finite set, or a compression argument. Say which. |
| INSIDE | Move the guarantee inside the loop | An invariant (safety, coverage, constraint satisfaction with confidence) holds at every iteration or diffusion level, not only after a post-hoc check. | Needs anytime validity: a union bound over levels with a fixed allocation, a sequential test, or e-values. Name it. |
| INVERT | Reverse a direction | Forward reachable ↔ backward reach-avoid; filtering ↔ smoothing; noising ↔ denoising; controller ↔ nature; minimize ↔ maximize. | The inverted object must be computable from what the method has (samples, model, data). |
| SETS | Points to sets, laws to credal sets | Box or zonotope particles; scenarios as sets; a set of priors (imprecise probability) instead of one belief, to get bounds robust to misspecification. | What does the set buy that more points would not? Usually: a deterministic statement inside each set, or robustness to a wrong prior. |
| LIMITS | Known methods as corners | The unified method reduces to each ingredient at a limit (temperature to infinity, noise to zero, one particle, zero margin). | List the corners explicitly. A unification without corners is probably a new heuristic. |
| REGIME | Find where the strong baseline fails | Identify the uncertainty that estimation cannot remove (multimodal belief, partial or noisy observation, hidden discrete regime, rare events, misspecification) and the task in which a point-estimate controller provably or empirically fails. | Without such a regime the idea is not a paper. Check it against the failure ledger of the brief. |
| BUDGET | Spend computation where it matters | Multi-fidelity estimates, sequential tests, rare-event splitting, scenario or particle counts that grow along the annealing. | Quantify the saving at the target accuracy (e.g. samples to certify ε = 10^-3). |
| CONDITION | Condition a learned model on another component | A generative model conditioned on the belief, the level, the certificate slack, or the decision. | Does conditioning remove an inference problem the model otherwise has to solve, or just add inputs? |
| DUAL | Constraint ↔ temperature | Anneal a multiplier, or turn a temperature into a risk budget; barrier and penalty readings of exponential weights. | Does the annealed problem converge to the constrained one, and at what rate? |
| LOOP | Score what is executed | Align the object that is scored or certified with the object that runs (closed loop with re-planning, not a committed open-loop plan). | Name the executed object and show the scored law equals it or bounds it in the right direction. |
| FAIL | Turn a failure into the contribution | A diagnosed failure of an earlier attempt becomes the problem the new method solves (e.g. "risk of the committed plan overstates the loop's spread 3–6×"). | The failure must be reproducible and general, not an artifact of one bad setting. |

## Typical compositions

- ISO + TARGET + LIMITS: a single sampler whose limits are the ingredient methods. Strongest when a theorem transfers
  through the identity.
- PSEUDO + SCHED + BUDGET: intractable safety factor estimated with a count of draws that grows along the annealing.
- REUSE + INSIDE: certificates computed from the samples the optimizer already draws, with the independence that
  makes them valid.
- REGIME + FAIL: the experiment design half of an idea. Every idea needs it.
