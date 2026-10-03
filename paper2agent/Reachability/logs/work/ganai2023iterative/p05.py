from pagelib import *
P = 5
items = [
    text("p0005-b000", B(P, "p0005-b000"),
         r"optimization produces a control minimizing the maximum future violation, i.e. $\arg\min_\pi V^{\pi}_h(s)$. *However, this does not ensure (re)entrance into the feasible set even if such a control exists.*",
         join_previous="space"),
    text("p0005-b001", B(P, "p0005-b001"),
         r"RCRL performs constraint optimization on $V^\pi_h$ with a neural network (NN) lagrange multiplier with state input [9]. When learning to optimize a Lagrangian dual function, the NN lagrange multiplier should converge to small values for states in the optimal feasible set and converge to large values for other states. Nonetheless, learning $V_h$ provides a weak signal during training: if there is an improvement in safety along the trajectory not affecting the maximum violation, $V^\pi_h$ remains the same for all states before the maximum violation in the trajectory. These improvements in costs can be crucial in guiding the optimization toward a safer policy. And optimizing with $V_h(s)$ can result in accumulating an unlimited number of violations smaller than the maximum violation. Also, a major issue with this approach is that *it’s limited to deterministic MDPs and policies* because its reachability value function in the Bellman formulation does not directly apply to the stochastic setting. However, in general *stochastic* settings, estimating feasibility cannot be binary since for a large portion of the state space, even under the optimal policy, the agent may enter the unsafe set with a non-zero probability, rendering such definition too conservative and impractical."),
    heading("p0005-b002", B(P, "p0005-b002"), "## 5 Iterative Reachability Estimation for Safe Reinforcement Learning"),
    text("p0005-b003", B(P, "p0005-b003"),
         r"In this paper, we formulate a general optimization framework for safety-constrained RL and propose a new algorithm to solve our constraint optimization by using our novel reachability estimation function. We present the deterministic case in Section 5.1 and build our way to the stochastic case in Section 5.2. We present our novel algorithm to solve these optimizations, involving our new reachability estimation function, in Section 5.3. We introduce convergence analysis in Section 5.4."),
    heading("p0005-b004", B(P, "p0005-b004"), "### 5.1 Iterative Reachability Estimation for Deterministic Settings"),
    text("p0005-b005", B(P, "p0005-b005"),
         r"All state transitions and policies happen with likelihood $0$ or $1$ for the deterministic environment. Therefore, the probability of constraint violation for policy $\pi$ from state $s$, i.e., $\phi^\pi(s)$, is in the set $\{0, 1\}$. According to Definition 4, if there exists some policy $\pi$ such that $\phi^\pi(s)=0$, we have $\phi^{\ast}(s)=0$. Otherwise, $\phi^{\ast}(s)=1$. Notice that this captures definitive membership in the optimal feasible set $\phi^{\ast}(s)=\mathbb{1}_{s\in S^{\pi_s}_f}$, which is the feasible set of some safest policy $\pi_s=\arg\min_\pi V^\pi_c (s)$. Now, we divide our optimization in two parts: the infeasible part and the feasible part."),
    text("p0005-b006", B(P, "p0005-b006"),
         r"For the infeasible part, we want the agent to incur the least cumulative damage (discounted sum of costs) and, if possible, (re)enter the feasible set. Different from previous Reachability-based RL optimizations, by using the discounted sum of costs $V^\pi_c(s)$ we consider both magnitude and frequency of violations, thereby improving learning signal. The infeasible portion takes the form:"),
    display("p0005-b007", B(P, "p0005-b007"),
            r"\max_\pi \mathbb{E}_{s\sim d_0}[-V^\pi_c(s)]. \tag{1}"),
    text("p0005-b008", B(P, "p0005-b008"),
         r"For the feasible part, we want the policy to ensure the agent stays in the feasible set and maximize reward returns. This produces a constraint optimization where the cost value function is constrained:"),
    display("p0005-b009", B(P, "p0005-b009"),
            r"\max_\pi \mathbb{E}_{s\sim d_0}\bigl[V^\pi(s)\bigr],\text{ subject to } V^{\pi}_c (s) = 0, \forall s\in \mathcal{S}_I. \tag{2}"),
    text("p0005-b010", [107.0, 550.0, 505.0, 563.5],
         r"The following propositions justify using $V^\pi_c$ as the constraint. Both proofs are in the appendix."),
    text("p0005-b010p", [107.0, 564.0, 505.0, 586.0],
         r"**Proposition 1.** The cost value function $V_c^\pi (s)$ is zero for state $s$ if and only if the persistent safety is guaranteed for that state under the policy $\pi$."),
    text("p0005-b011", B(P, "p0005-b011"),
         r"We define here $\mathcal{S}_f:=\mathcal{S}^{\pi_s}_f$, the feasibilty set of some safest policy. Now, the above two optimizations can be unified with the use of the feasibility function $\phi^{\ast}(s)$:"),
    display("p0005-b012", [125.0, 616.0, 510.0, 636.5],
            r"\max_\pi \mathbb{E}_{s\sim d_0}\bigl[V^\pi(s)\cdot(1-\phi^{\ast}(s)) - V^\pi_c(s)\cdot\phi^{\ast}(s) \bigr], \text{ subject to } V^{\pi}_c (s) = 0, \forall s\in \mathcal{S}_I \cap \mathcal{S}_f. \tag{3}"),
    text("p0005-b013", [107.0, 637.5, 506.0, 670.0],
         r"Unlike other reachability based optimizations like RCRL, one particular advantage in Equation 3 is, with some assumptions, the guaranteed entrance back into feasible set with minimum cumulative discounted violations whenever a possible control exists. More formally, assuming infinite horizon:"),
    text("p0005-b013p", [107.0, 672.5, 506.0, 722.5],
         r"**Proposition 2.** If $\exists\pi$ that produces trajectory $\tau=\{(s_i),i\in\mathbb{N}, s_1=s\}$ in deterministic MDP $\mathcal{M}$ starting from state $s$, and $\exists m\in \mathbb{N}, m<\infty$ such that $s_m\in S^\pi_f$, then $\exists \epsilon>0$ where if discount factor $\gamma\in (1-\epsilon,1)$, then the optimal policy $\pi^{\ast}$ of Equation 3 will produce a trajectory $\tau'=\{(s'_j),j\in\mathbb{N}, s'_1=s\}$, such that $\exists n\in \mathbb{N}, n<\infty$, $s'_n\in S^{\pi^{\ast}}_f$ and $V^{\pi^{\ast}}_c(s)=\min_{\pi'} V^{\pi'}_c(s)$."),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 5 and with main.tex (end of Section 4.2, Section 5 opener, Section 5.1). The
first item continues the sentence from page 4 ('When outside this set, the | optimization produces a control ...') with
join_previous 'space'. All inline and display mathematics rewritten in LaTeX from the TeX source (macros expanded: \E to
\mathbb{E}, \mathbbm{1} and \mathbbm{N} to \mathbb{1} and \mathbb{N}) and checked on the render; TeX and PDF agree. The
extractor formula images for (1) and (2) and the glyph-soup text item for (3) were replaced by $$ blocks with the
printed numbers as \tag: (1) infeasible part $\max_\pi \mathbb{E}[-V^\pi_c(s)]$, (2) feasible part with constraint
$V^\pi_c(s)=0\ \forall s\in\mathcal{S}_I$, (3) unified deterministic problem with constraint on
$\mathcal{S}_I\cap\mathcal{S}_f$. The extractor had merged 'The following propositions ...' with Proposition 1 and 'Unlike
other ...' with Proposition 2; they are separate items now. Proposition 1 is one sentence; Proposition 2 runs from 'If
$\exists\pi$' to '$=\min_{\pi'}V^{\pi'}_c(s)$.' (ends of the prop environments in the TeX source); bodies are printed
upright. Cross-references as printed: 'Section 5.1', 'Section 5.2', 'Section 5.3', 'Section 5.4', 'Definition 4',
'Equation 3' (twice), '[9]'. The paragraph that starts 'RCRL performs ...' begins with a reference to the RCRL equation
that prints as the name 'RCRL'. As printed (kept): the feasible set is written with an italic $S$ in
$\mathbb{1}_{s\in S^{\pi_s}_f}$, $s_m\in S^\pi_f$ and $s'_n\in S^{\pi^{\ast}}_f$ but calligraphic in
$\mathcal{S}_f:=\mathcal{S}^{\pi_s}_f$; the typo 'feasibilty set'; 'lagrange multiplier' in lower case; 'Reachability-based'
capitalised. Italics kept for 'it’s limited to deterministic MDPs and policies', 'stochastic' and the sentence
'However, this does not ensure (re)entrance ...'. Asterisks written \ast. Heading levels fixed (5 level 2; 5.1 level 3).
Omitted: printed page number 5.
""")
