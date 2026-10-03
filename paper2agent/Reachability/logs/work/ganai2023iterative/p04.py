from pagelib import *
P = 4
items = [
    heading("p0004-b000", B(P, "p0004-b000"), "## 4 Stochastic Hamilton-Jacobi Reachability for Reinforcement Learning"),
    text("p0004-b001", B(P, "p0004-b001"),
         r"Classic HJ reachability considers finding the largest feasible set for deterministic environments. In this section, we apply a similar definition in [45, 46] and define the stochastic reachability problem."),
    heading("p0004-b002", B(P, "p0004-b002"), "### 4.1 Persistent Safety and HJ Reachability for Stochastic Systems"),
    text("p0004-b003", B(P, "p0004-b003"),
         r"The instantaneous safety can be characterized by the safe set $\mathcal{S}_s$, which is the zero level set of the safety loss function $h: \mathcal{S} \mapsto \mathbb{R}^+_0$. The unsafe (i.e. violation) set $\mathcal{S}_v$ is the complement of the safe set."),
    text("p0004-b004", B(P, "p0004-b004"),
         r"**Definition 1.** Safe set and unsafe set: $\mathcal{S}_{s}:= \{ s \in \mathcal{S}: h(s) = 0 \},  \mathcal{S}_{v}:= \{ s \in \mathcal{S}: h(s) > 0 \}$."),
    text("p0004-b005", B(P, "p0004-b005"),
         r"We will write $\mathbb{1}_{s\in \mathcal{S}_v}$ as the *instantaneous violation indicator function*, which is $1$ if the current state is in the violation set and $0$ otherwise. Note that the safety loss function $h$ is different from the instantaneous violation indicator function since $h$ captures the magnitude of the violation at the state."),
    text("p0004-b006", B(P, "p0004-b006"),
         r"It is insufficient to only consider instantaneous safety. When the environment and policy are both deterministic, we easily have a unique trajectory for starting from each state (i.e. the future state is uniquely determined) under Lipschitz environment dynamics. In classic HJ reachability literature [13], for a deterministic MDP’s transition model $P_d$ and deterministic policy $\pi_d$, the set of states that guarantees persistent safety is captured by the zero sub-level set of the following value function:"),
    text("p0004-b007", B(P, "p0004-b007"),
         r"**Definition 2.** Reachability value function $V_h^\pi : \mathcal{S} \mapsto \mathbb{R}^+_0$ is: $V_h^\pi (s) := \max_{s_t\in \tau \sim \pi_d,P_d(s)} h(s_t)$."),
    text("p0004-b008", B(P, "p0004-b008"),
         r"However, when there’s a stochastic environment with transition model $P(\cdot | s,a)$ and policy $\pi(\cdot | s)$, the future states are not uniquely determined. This means for a given initial state and policy, there may exist many possible trajectories starting from this state. In this case, instead of defining a binary function that only indicates the existence of constraint violations, we define the reachability estimation function (REF), which captures the probability of constraint violation:"),
    text("p0004-b009", B(P, "p0004-b009"),
         r"**Definition 3.** The reachability estimation function (REF) $\phi^\pi : \mathcal{S} \mapsto [0,1]$ is defined as:"),
    display("p0004-b010", B(P, "p0004-b010"),
            r"\phi^\pi (s) := \mathbb{E}_{\tau \sim \pi,P(s)} \max _{s_t\in \tau} \mathbb{1}_{(s_t|s_0 = s, \pi)\in \mathcal{S}_v}."),
    text("p0004-b011", B(P, "p0004-b011"),
         r"In a specific trajectory $\tau$, the value $\max _{s_t\in \tau} \mathbb{1}_{(s_t|s_0 = s, \pi)\in \mathcal{S}_v}$ will be 1 if there exist constraint violations and 0 if there exists no violation, which is binary. Taking expectation over this binary value for all the trajectories, we get the desired probability. We define optimal REF based on an optimally safe policy $\pi^{\ast} = \arg\min_\pi V^\pi_c(s)$ (note that this policy may not be unique)."),
    text("p0004-b012", B(P, "p0004-b012"),
         r"**Definition 4.** The optimal reachability estimation function $\phi^{\ast} : \mathcal{S} \mapsto [0,1]$ is: $\phi^{\ast} (s) := \phi^{\pi^{\ast}} (s)$."),
    text("p0004-b013", B(P, "p0004-b013"),
         r"Interestingly, we can utilize the fact the instantaneous violation indicator function produces binary values to learn the REF function in a bellman recursive form. The following will be used later:"),
    text("p0004-b014", B(P, "p0004-b014"),
         r"**Theorem 1.** The REF can be reduced to the following recursive Bellman formulation:"),
    display("p0004-b015", B(P, "p0004-b015"),
            r"\phi^\pi (s) = \max \{ \mathbb{1}_{s\in \mathcal{S}_v} , \mathbb{E}_{s' \sim \pi,P(s)} \phi^\pi(s') \},"),
    text("p0004-b016", B(P, "p0004-b016"),
         r"where $s' \sim \pi,P(s)$ is a sample of the immediate successive state (i.e., $s' \sim P(\cdot| s , a\sim \pi(\cdot | s))$) and the expectation is taken over all possible successive states. The proof can be found in the appendix."),
    text("p0004-b017", B(P, "p0004-b017"),
         r"**Definition 5.** The feasible set of a policy $\pi$ based on $\phi^\pi(s)$ is defined as: $\mathcal{S}_{f}^{\pi} := \{ s \in \mathcal{S}: \phi^\pi (s) = 0  \}$."),
    text("p0004-b018", B(P, "p0004-b018"),
         r"Note, the feasible set for a specific policy is the set of states starting *from* which no violation is reached, and the safe set is the set of states *at* which there is no violation. We will use the phrase likelihood of being feasible to mean the likelihood of not reaching a violation, i.e. $1-\phi^\pi(s)$."),
    heading("p0004-b019", B(P, "p0004-b019"), "### 4.2 Comparison with RCRL"),
    text("p0004-b020", B(P, "p0004-b020"),
         r"The RCRL approach [27] uses reachability to optimize and maintain persistent safety in the feasible set. Note, in below formulation, $\mathcal{S}_f$ is the optimal feasible set, i.e. that of a policy $\arg\min_\pi V^\pi_h(s)$. The RCRL formulation is:"),
    display("p0004-b021", B(P, "p0004-b021"),
            r"\max_\pi \mathbb{E}_{s\sim d_0} [V^{\pi}(s)\cdot \mathbb{1}_{s\in \mathcal{S}_f} - V^{\pi}_h(s)\cdot \mathbb{1}_{s\notin \mathcal{S}_f}],\text{ subject to } V^{\pi}_h (s)\leq 0, \forall s\in \mathcal{S}_I \cap \mathcal{S}_f. \tag{RCRL}"),
    text("p0004-b022", B(P, "p0004-b022"),
         r"The equation RCRL considers two different optimizations. When in the optimal feasible set, the optimization produces a persistently safe policy maximizing rewards. When outside this set, the"),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 4 and with main.tex (Section 4, 4.1, start of 4.2). All inline and display
mathematics rewritten in LaTeX from the TeX source with the authors' macros expanded (\E to \mathbb{E}; the indicator,
typed \mathbbm{1} and printed as a double-struck 1, is written \mathbb{1}) and checked symbol by symbol on the render;
TeX and PDF agree. The three extractor formula images were replaced by $$ blocks: the definition of the REF
(unnumbered, ends with a full stop), the Bellman recursion of Theorem 1 (unnumbered, ends with a comma) and the RCRL
problem with its printed name tag '(RCRL)'. In displays the expectation subscripts are printed underneath the E.
Statement ends taken from the TeX environments: Definition 1 and Definition 2 are single lines; Definition 3 consists
of the lead-in line and the display; Definition 4 is one line; Theorem 1 consists of the lead-in, the display AND the
following sentence 'where $s' \sim \pi,P(s)$ ... The proof can be found in the appendix.' (the where-sentence is inside
the theorem environment); Definition 5 is one line. Definition and theorem bodies are printed upright here. Labels
'Definition n.' / 'Theorem 1.' bold as printed. Definition 2 uses the deterministic policy $\pi_d$ and transition model
$P_d$ under the max ($s_t\in\tau\sim\pi_d,P_d(s)$) while the function is named $V_h^\pi$, as printed. The optimal policy
used for the optimal REF is printed as $\pi^{\ast} = \arg\min_\pi V^\pi_c(s)$ (cost value function $V_c$, not $V_h$),
kept. Asterisks written \ast. Italics kept for 'instantaneous violation indicator function', 'from' and 'at'. '\ref' to the RCRL equation prints the name 'RCRL' ('The
equation RCRL considers ...'). Citations [45, 46], [13], [27] checked. Authors' wording kept: 'a unique trajectory for
starting from each state', 'the fact the instantaneous violation indicator function produces', 'bellman recursive form',
'in below formulation'. The last paragraph breaks across pages in the middle of a sentence ('When outside this set, the |
optimization produces a control ...') and continues on page 5 (join_previous there). Heading levels fixed (4 level 2; 4.1, 4.2 level 3). Omitted: printed page number 4.
""")
