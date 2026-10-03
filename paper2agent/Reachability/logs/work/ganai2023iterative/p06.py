from pagelib import *
P = 6
items = [
    heading("p0006-b000", B(P, "p0006-b000"), "### 5.2 Iterative Reachability Estimation for Stochastic Settings"),
    text("p0006-b001", B(P, "p0006-b001"),
         r"In stochastic environments, for each state, there is some likelihood of entering into the unsafe states under any policy. Thus, we adopt the probabilistic reachability Definitions 3 and 4. Rather than using the binary indicator in the optimal feasible set to demarcate the feasibility and infeasibility optimization scenarios, we use the likelihood of infeasibility of the safest policy. In particular, for any state $s$, the optimal likelihood that the policy will enter the infeasible set is $\phi^{\ast}(s)$ from Definition 4."),
    text("p0006-b002", B(P, "p0006-b002"),
         r"We again divide the full optimization problem in stochastic settings into infeasible and feasible ones similar to Equations 1 and 2. However, we consider the infeasible formulation with likelihood the current state is in a safest policy’s infeasible state, or $\phi^{\ast}(s)$. Similarly, we account for the feasible optimization formulation with likelihood the current state is in a safest policy’s feasible set, $1-\phi^{\ast}(s)$. The complete Reachability Estimation for Safe Policy Optimization (RESPO) can be rewritten as:"),
    display("p0006-b003", B(P, "p0006-b003"),
            r"\max_\pi \mathbb{E}_{s\sim d_0} [V^{\pi}(s)\cdot (1-\phi^{\ast}(s)) - V^{\pi}_c(s)\cdot \phi^{\ast}(s)] \text{, s.t., }V^{\pi}_c (s) = 0, \text{ w.p. } 1-\phi^{\ast}(s), \forall s\in S_I. \tag{RESPO}"),
    text("p0006-b004", B(P, "p0006-b004"),
         r"In sum, the RESPO framework provides several benefits when compared with other constrained Reinforcement Learning and reachability-based approaches. Notably, 1) it maintains persistent safety when in the feasible set unlike CMDP-based approaches, 2) compared with other reachability-based approaches, RESPO considers performance optimization in addition to maintaining safety, 3) it maintains the behavior of a safest policy in the infeasible set and even reenters the feasible set when possible, 4) RESPO employs rigorously defined reachability definitions even in stochastic settings."),
    heading("p0006-b005", B(P, "p0006-b005"), "### 5.3 Overall Algorithm"),
    text("p0006-b006", B(P, "p0006-b006"),
         r"We describe our algorithms by breaking down the novel components. Our algorithm predicts reachability membership to guide the training toward optimizing the right portion of the optimization equation (i.e., feasibility case or infeasibility case). Furthermore, it exclusively uses the discounted sum of costs as the safety value function – we can avoid having to learn the reachability value function while having the benefit of exploiting the improved signal in the cost value function."),
    text("p0006-b007", B(P, "p0006-b007"),
         r"**Optimization in infeasible set versus feasible set.** If the agent is in the infeasible set, this is the simplest case. We want to find the optimal policy that maximizes $-V^\pi_c(s)$. This would be the only term that needs to be considered in optimization."),
    text("p0006-b008t", [107.0, 456.0, 505.0, 479.5],
         r"On the other hand, if the agent is in the feasible set, we must solve the constraint optimization $\max_\pi V^\pi(s)$ subject to $V^\pi_c(s) = 0$. This could be solved via a Lagrangian-based method:"),
    display("p0006-b008", [180.0, 476.5, 432.0, 500.3],
            r"\min_\pi \max_\lambda L(\pi, \lambda) = \min_\pi \max_\lambda\bigg(\mathbb{E}_{s\sim d_0} [-V^\pi(s) + \lambda V^\pi_c(s)]\bigg)."),
    text("p0006-b009", [107.0, 500.5, 505.0, 555.0],
         r"Now what remains is obtaining the reachability estimation function $\phi^{\ast}$. First, we address the problem of acquiring optimal likelihood of being feasible. It is nearly impossible to accurately know before training if a state is in a safest policy’s infeasible set. We propose learning a function guaranteed to converge to this REF (with some discount factor for $\gamma$-contraction mapping) by using the recursive Bellman formulation proved in Theorem 1."),
    text("p0006-b010", [107.0, 559.0, 498.0, 571.0],
         r"We learn a function $p(s)$ to capture the probability $\phi^{\ast}(s)$. It is trained like a reachability function:"),
    display("p0006-b010d", [238.0, 571.2, 374.0, 584.0],
            r"p(s) = \max\{ \mathbb{1}_{s\in S_v}, \gamma \cdot p(s')\},"),
    text("p0006-b011", [107.0, 584.2, 505.0, 617.0],
         r"where $S_v$ is the violation set, $s'$ is the next sampled state, and $\gamma$ is a discount parameter $0\ll\gamma<1$ to ensure convergence of $p(s)$. Furthermore, and crucially, we ensure the learning rate of this REF is on a slower time scale than the policy and its critics but faster than the lagrange multiplier."),
    text("p0006-b012", B(P, "p0006-b012"),
         r"Bringing the concepts covered above, we present our full optimization equation:"),
    display("p0006-b013", [110.0, 635.0, 510.0, 664.0],
            r"\min_\pi \max_\lambda L(\pi, \lambda) = \min_\pi \max_\lambda\bigg(\mathbb{E}_{s\sim d_0}\biggl[ [-V^\pi(s) + \lambda\cdot V^\pi_c(s)]\cdot (1-p(s)) + V^\pi_c(s)\cdot p(s)\biggr]\bigg). \tag{4}"),
    text("p0006-b014", [107.0, 665.5, 506.0, 724.0],
         r"We show the design of our algorithm **RESPO** in an actor-critic framework in Algorithm 1. Note that the $V$ and $V_c$ have corresponding $Q$ functions: $V^\pi(s)=\mathbb{E}_{a\sim\pi(\cdot | s)}Q(s,a)$ and $V^\pi_c(s)=\mathbb{E}_{a\sim\pi(\cdot | s)}Q_c(s,a)$. The gradients’ definitions are found in the appendix. We use operator $\Gamma_\Theta$ to indicate the projection of vector $\theta\in \mathbb{R}^n$ to the closest point in compact and convex set $\Theta\subseteq\mathbb{R}^n$. Specifically, $\Gamma_\Theta=\arg\min_{\hat{\theta}\in \Theta}|| \hat{\theta} - \theta||^2$. $\Gamma_\Omega$ is similarly defined."),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 6 and with main.tex (Sections 5.2 and 5.3). All inline and display
mathematics rewritten in LaTeX from the TeX source (macros expanded) and checked on the render; TeX and PDF agree. Four
displays: the RESPO problem with its printed name tag '(RESPO)' (the tag is printed on its own line under the formula
because the formula fills the line); the unnumbered Lagrangian $\min_\pi\max_\lambda L(\pi,\lambda)$ for the feasible
case; the unnumbered REF target $p(s)=\max\{\mathbb{1}_{s\in S_v},\gamma\cdot p(s')\}$ (the extractor had it inline in a
text item); and the full objective with printed number (4). The extractor's formula image for the Lagrangian also
contained the paragraph 'On the other hand, ...'; it is a separate text item now, and the bboxes of the neighbouring
items were set from the evidence line positions. As printed (kept): the RESPO constraint is written 's.t., ... w.p.
$1-\phi^{\ast}(s)$, $\forall s\in S_I$' with an italic $S_I$ (calligraphic elsewhere), the violation set is an italic
$S_v$ in the REF update and the sentence after it, the norm is typed with double bars '||', and the projection is
written $\Gamma_\Theta=\arg\min_{\hat\theta\in\Theta}||\hat\theta-\theta||^2$ without an argument. 'RESPO' bold as
printed in the last paragraph; 'Optimization in infeasible set versus feasible set.' is a run-in bold paragraph title
(\paragraph), kept as bold text, not a heading. The dash in 'safety value function – we can avoid' is an en dash.
Cross-references as printed: 'Definitions 3 and 4', 'Definition 4', 'Equations 1 and 2', 'Theorem 1', 'Algorithm 1'.
Enumerators '1)', '2)', '3)', '4)' are plain text. Heading levels fixed (5.2, 5.3 level 3). Algorithm 1 itself is on
page 7. Omitted: printed page number 6.
""")
