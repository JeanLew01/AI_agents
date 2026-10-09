# Paper collections available to the brainstorm

Each paper is a Claude Code skill built by `paper2agent` and linked into `~/.claude/skills/<name>/`. The full text is
`references/paper.md` (equations in LaTeX), navigation is `references/index.md`, figures and tables are under
`assets/`. Scouts read these files directly; they do not need to invoke the skill.

Mechanism cards extracted by scouts are cached in `library/cards/<lens>.md`. Reuse them when they exist and only
add the brief-specific hooks; refresh a card when a later session needs a detail it lacks.

To add a collection: convert the papers with the `paper2agent` skill, link them into `~/.claude/skills/`, and add a
section here. The scout lenses in `skill/research-brainstorm/SKILL.md` refer to these sections.

## NMPC (`~/AI_agents/paper2agent/NMPC`)

| Skill | Paper | Lens |
|---|---|---|
| `dial-mpc-paper` | Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing (DIAL-MPC) | sampling MPC, annealing |
| `model-based-diffusion-paper` | Model-Based Diffusion for Trajectory Optimization (MBD) | diffusion as optimizer, Monte Carlo score |
| `pac-nmpc-paper` | Probably Approximately Correct Nonlinear Model Predictive Control (PAC-NMPC) | PAC-Bayes bounds inside stochastic MPC |
| `pac-nmpc-value-function-paper` | Robust Perception-Based Navigation using PAC-NMPC with a Learned Value Function | PAC-NMPC with terminal value |
| `rl-guided-pac-nmpc-paper` | RL-Guided PAC-NMPC for Probabilistically-Safe Perception-Based Navigation in Unknown Environments | learned proposal for PAC-NMPC |
| `post-stall-navigation-paper` | Post-Stall Navigation with Fixed-Wing UAVs using Onboard Vision | application, hardware |
| `urban-swarm-fixed-wing-paper` | Agile Fixed-Wing UAVs for Urban Swarm Operations | application, hardware |

## Particle filtering and robust inference (`~/AI_agents/paper2agent/ParticleFilter`)

| Skill | Paper | Lens |
|---|---|---|
| `diffusion-resampling-paper` | Diffusion differentiable resampling | resampling by reverse SDE, ensemble score |
| `diffpf-paper` | DiffPF: Differentiable Particle Filtering with Generative Sampling via Conditional Diffusion Models | learned diffusion proposal |
| `andrieu-pmcmc-2010-paper` | Particle Markov chain Monte Carlo methods | pseudo-marginal, unbiased evidence |
| `gning-box-bernoulli-2012-paper` | Bernoulli Particle/Box-Particle Filters ... Triple Measurement Uncertainty | box particles, interval analysis |
| `haj-chhade-box-messages-2014-paper` | Non Parametric Distributed Inference in Sensor Networks Using Box Particles Messages | box particles, message passing |
| `benavoli-piga-2016-paper` | A probabilistic interpretation of set-membership filtering ... polytopic bounding | set-membership as probability |
| `benavoli-lower-previsions-2011-paper` | Robust filtering through coherent lower previsions | imprecise probability filtering |
| `greco-vasile-2022-paper` | Robust Bayesian Particle Filter for Space Object Tracking Under Severe Uncertainty | robust Bayes, collision probability bounds |
| `raices-cruz-robust-is-mcmc-2022-paper` | Iterative importance sampling with MCMC sampling in robust Bayesian analysis | reweighting across a set of priors |

## Reachability (`~/AI_agents/paper2agent/Reachability`)

Statistical and scenario-based (lens `reach-stat`):

| Skill | Paper |
|---|---|
| `devonport2020estimating-paper` | Estimating Reachable Sets with Scenario Optimization |
| `devonport2021data-paper` | Data-Driven Reachability Analysis with Christoffel Functions |
| `devonport2023data-paper` | Data-Driven Reachability Analysis and Support Set Estimation with Christoffel Functions |
| `dietrich2024nonconvex-paper` | Nonconvex Scenario Optimization for Data-Driven Reachability |
| `dietrich2025data-paper` | Data-Driven Reachability with Scenario Optimization and the Holdout Method |
| `hewing2019scenario-paper` | Scenario-based Probabilistic Reachable Sets for Recursively Feasible Stochastic MPC |
| `tebjou2023data-paper` | Data-driven Reachability using Christoffel Functions and Conformal Prediction |
| `hashemi2023data-paper` | Data-Driven Reachability Analysis of Stochastic Dynamical Systems with Conformal Inference |
| `hashemi2025pca-paper` | PCA-DDReach: Statistical Reachability of Stochastic Systems via PCA |
| `lin2024verification-paper` | Verification of Neural Reachable Tubes via Scenario Optimization and Conformal Prediction |
| `sartipizadeh2019voronoi-paper` | Voronoi Partition-based Scenario Reduction for Fast Sampling-based Stochastic Reachability of LTI Systems |

Sampling, set-based, and safe learning (lens `reach-set`):

| Skill | Paper |
|---|---|
| `lew2021sampling-paper` | Sampling-based Reachability Analysis: A Random Set Theory Approach with Adversarial Sampling |
| `lew2022simple-paper` | A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis |
| `liebenwein2018sampling-paper` | Sampling-Based Approximation Algorithms for Reachability Analysis with Provable Guarantees |
| `fan2017dryvr-paper` | DryVR: Data-driven verification and compositional reasoning for automotive systems |
| `gruenbacher2022gotube-paper` | GoTube: Scalable Stochastic Verification of Continuous-Depth Models |
| `ganai2023iterative-paper` | Iterative Reachability Estimation for Safe Reinforcement Learning |
| `selim2022safe-paper` | Safe Reinforcement Learning Using Black-Box Reachability Analysis |
| `liu2025recurrent-paper` | Recurrent Control Barrier Functions: A Path Towards Nonparametric Safety Verification |
| `ouyang2026symplectic-paper` | Symplectic Inductive Bias for Data-Driven Target Reachability in Hamiltonian Systems |
