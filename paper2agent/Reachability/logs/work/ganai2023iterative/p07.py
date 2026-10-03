from pagelib import *
P = 7
E2 = "&emsp;&emsp;"
E4 = E2 + E2
ALG = "\n\n".join([
    r"**Algorithm 1** RESPO Actor Critic",
    r"**Require:** Randomly initialized policy $\pi_\theta$’s parameters $\theta_0$, reward critic $Q$’s parameters $\eta_0$, cost critic $Q_c$’s parameters $\kappa_0$, REF $p$’s parameters $\xi_0$, Lagrange multiplier $\lambda$’s parameters $\omega_0$, horizon $T$",
    r"**Require:** Convex projection operators $\Gamma_\Theta$ and $\Gamma_\Omega$, and reward and cost critic learning rate $\zeta_1(k)$, policy learning rate $\zeta_2(k)$, REF learning rate $\zeta_3(k)$, lagrange multiplier learning rate $\zeta_4(k)$",
    r"1: **for** $k=0,1,2,...$ **do**",
    E2 + r"2: **for** $i=0,1,2,...$ **do**",
    E4 + r"3: Sample trajectories $\tau_i: \{(s_j,a_j,s'_j,r_j,h_j)\} \sim \pi_{\theta}$",
    E4 + r"4: **Rew. Update** $\eta_{k+1}=\eta_{k}-\zeta_1(k)\nabla_\eta Q(s_t,a_t)\cdot [Q(s_t, a_t) - (r(s_t, a_t) + \gamma Q(s_{t+1}, a_{t+1}))]$",
    E4 + r"5: **Cost Update** $\kappa_{k+1}=\kappa_{k}-\zeta_1(k)\nabla_\kappa Q_c(s_t,a_t)\cdot [Q_c(s_t, a_t) - (h(s_t) + \gamma Q_c(s_{t+1}, a_{t+1}))]$",
    E4 + r"6: **Policy Update** $\theta_{k+1}=$",
    E4 + r"7: $\Gamma_\Theta \bigg(\theta_k - \zeta_2(k)\gamma^t \bigg[-Q(s_t,a_t) [1 - p(s_t)] +Q_c(s_t,a_t) [\lambda (1 - p(s_t)) + p(s_t)]\bigg] \nabla_\theta \log\pi_\theta (a_t | s_t)\bigg)$",
    E4 + r"8: **REF Update** $\xi_{k+1}=\xi_{k}-\zeta_3(k)\nabla_\xi p(s_t)\cdot [p(s_t) - \max\{\mathbb{1}_{h(s_t)>0}, \gamma p(s_{t+1})\}]$",
    E4 + r"9: **Lagrange multiplier Update** $\omega_{k+1}=\Gamma_\Omega \big(\omega_k - \zeta_4(k)Q_c(s_t,a_t)(1-p(s_t)) \nabla_\omega \lambda\big)$",
    E2 + r"10: **end for**",
    r"11: **end for**",
])
items = [
    figure("p0007-alg1", [106.0, 70.5, 506.0, 273.5], "Algorithm 1", "algorithm-1"),
    text("p0007-alg1-text", [107.0, 74.0, 506.0, 270.0], ALG),
    heading("p0007-b015", B(P, "p0007-b015"), "### 5.4 Convergence Analysis"),
    text("p0007-b016", [107.0, 390.0, 505.0, 433.0],
         r"We provide convergence analysis of our algorithm for Finite MDPs (finite bounded state and action space sizes, maximum horizon $T$, reward bounded by $R_{\max}$, and cost bounded by $H_{\max}$) under reasonable assumptions. We demonstrate our algorithm almost surely finds a locally optimal policy for our RESPO formulation, based on the following assumptions:"),
    text("p0007-b017", [107.0, 433.2, 506.0, 442.4],
         r"• **A1** *(Step size):* Step sizes follow schedules $\{\zeta_1(k)\}$, $\{\zeta_2(k)\}$, $\{\zeta_3(k)\}$, $\{\zeta_4(k)\}$ where:"),
    display("p0007-b017d", [107.0, 442.5, 506.0, 466.5],
            r"\sum_{k} \zeta_i(k) = \infty \text{ and } \sum_{k} \zeta_i(k)^2 < \infty, \forall i\in \{1,2,3,4\}, \quad\text{ and }\quad \zeta_j(k) = o(\zeta_{j-1}(k)), \forall j\in\{2,3,4\}."),
    text("p0007-b017t", [107.0, 466.6, 506.0, 497.3],
         r"The reward returns and cost returns critic value functions must follow the fastest schedule $\zeta_1(k)$, the policy must follow the second fastest schedule $\zeta_2(k)$, the REF must follow the second slowest schedule $\zeta_3(k)$, and finally, the lagrange multiplier should follow the slowest schedule $\zeta_4(k)$."),
    text("p0007-b018", [107.0, 497.4, 506.0, 509.6],
         r"• **A2** *(Strict Feasibility):* $\exists\pi(\cdot | \cdot; \theta)$ such that $\forall s\in \mathcal{S}_I$ where $\phi^{\ast}(s)=0$, $V^{\pi_\theta}_c(s)\leq 0$."),
    text("p0007-b019", [107.0, 509.7, 506.0, 553.0],
         r"• **A3** *(Differentiability and Lipschitz Continuity):* For all state-action pairs $(s,a)$, we assume value and cost Q functions $Q(s,a;\eta),Q_c(s,a;\kappa)$, policy $\pi(a|s; \theta)$, and REF $p(s,a;\xi)$ are continuously differentiable in $\eta,\kappa,\theta,\xi$ respectively. Furthermore, $\nabla_\omega \lambda_\omega$ and, for all state-action pairs $(s,a)$, $\nabla_\theta \pi(a|s;\theta)$ are Lipschitz continuous functions in $\omega$ and $\theta$ respectively."),
    text("p0007-b020", B(P, "p0007-b020"),
         r"The detailed proof of the following result is provided in the appendix."),
    text("p0007-b021", B(P, "p0007-b021"),
         r"**Theorem 2.** Given Assumptions **A1**-**A3**, the policy updates in Algorithm 1 will almost surely converge to a locally optimal policy for our proposed optimization in Equation RESPO."),
    heading("p0007-b022", B(P, "p0007-b022"), "## 6 Experiments"),
    figure("p0007-fig1", [113.0, 275.5, 497.0, 338.5], "Figure 1", "figure-1"),
    caption("p0007-b014", [107.0, 339.0, 505.0, 359.0],
            r"Figure 1: We compare the performance of our algorithm with other SOTA baselines in Safety Gym (left two figures), Safety PyBullet (middle two figures), and Safety MuJoCo (right two figures)."),
    text("p0007-b023", B(P, "p0007-b023"),
         r"**Baselines.** The baselines we compare are CMDP-based or solve for hard constraints. The CMDP baselines are Lagrangian-based Proximal Policy Optimization (**PPOLag**) based on [7], Constraint-Rectified Policy Optimization (**CRPO**) [35], Penalized Proximal Policy Optimization (**P3O**) [32], and Projection-Based Constrained Policy Optimization (**PCPO**) [3]. The hard constraints baselines are **RCRL** [27], **CBF** with constraint $\dot{h}(s) + \nu\cdot h(s)\leq 0$, and Feasibile Actor-Critic (**FAC**) [9]. We classify **FAC** among the hard constraint approaches because we make its cost threshold $\chi=0$ in order to better compare using NN lagrange multiplier with our REF approach in **RESPO**. We include the unconstrained Vanilla **PPO** [33] baseline for reference."),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 7, a 110 dpi crop of the algorithm box, a 130 dpi crop of Figure 1, and with
main.tex. Algorithm 1 (float at the top of the page, between the two rules): the extractor had fragmented it into list
items with glyph soup and merged lines 4-5 and 6-9; it is now one image crop 'algorithm-1' (both horizontal rules, the
title line and lines 1-11 inside; edges checked on the crop) followed by a line-by-line transcription from the
algorithmic source: bold title line, the two unnumbered 'Require:' lines, the printed line numbers 1-11, one paragraph
per printed line, nesting shown with two em-spaces per level (outer loop over k, inner loop over i). As printed: line 6
'Policy Update $\theta_{k+1}=$' ends with the equals sign and its right-hand side is the separate numbered line 7; the
loops are written '$k=0,1,2,...$' with three plain dots; the updates use $s_t,a_t$ while the sampled tuples in line 3
are indexed by j; the REF update uses the indicator $\mathbb{1}_{h(s_t)>0}$; 'lagrange multiplier learning rate' in
lower case. Figure 1 (six environment pictures, float printed directly under the algorithm) is one crop 'figure-1'
(the extractor had six separate image items); the only text inside it is the label 'Unsafe region' in the last
picture; caption verbatim. In the TeX source the figure is declared at the start of Section 6, so its item is placed
after the heading '6 Experiments' here (same page; printed position is above Section 5.4). Section 5.4: mathematics
rewritten in LaTeX from the TeX source and checked on the render. The assumptions A1-A3 are printed as three lines
starting with a bullet typed as a math symbol (not a list); the label 'A1' is bold and the name in parentheses with the
colon is italic. Assumption A1 consists of the lead-in line, the unnumbered display (step-size conditions; printed
flush with wide spaces around the second 'and', written \quad) and the sentence 'The reward returns ... slowest
schedule $\zeta_4(k)$.'; the extractor had put the display into the text item as glyph soup. A2 and A3 are single
paragraphs. Theorem 2 is one sentence and refers to 'Equation RESPO' (the tag name is printed, no number); body upright.
Section 6: run-in bold title 'Baselines.' and bold method names (PPOLag, CRPO, P3O, PCPO, RCRL, CBF, FAC, RESPO, PPO)
as printed; the CBF constraint is printed with a dot over h, $\dot{h}(s)+\nu\cdot h(s)\leq 0$. Authors' spelling
'Feasibile Actor-Critic' kept. 'Constraint-Rectified' is a real compound broken at the line end. Citations checked:
[7], [35], [32], [3], [27], [9], [33]. Heading levels fixed (5.4 level 3; 6 level 2). Omitted: printed page number 7.
""")
