from pagelib import *
P = 3
items = [
    text("p0003-b000", B(P, "p0003-b000"), O(P, "p0003-b000"), join_previous="space"),
    heading("p0003-b001", B(P, "p0003-b001"), "### 2.2 Hamilton-Jacobi Reachability Analysis"),
    text("p0003-b002", B(P, "p0003-b002"), O(P, "p0003-b002")),
    heading("p0003-b003", B(P, "p0003-b003"), "## 3 Preliminaries"),
    heading("p0003-b004", B(P, "p0003-b004"), "### 3.1 Markov Decision Processes"),
    text("p0003-b005", B(P, "p0003-b005"),
         r"Markov Decision Processes (MDP) are defined as $\mathcal{M}:=\langle \mathcal{S}, \mathcal{A}, P, r, h, \gamma\rangle$. $\mathcal{S}$ and $\mathcal{A}$ are the state and action spaces respectively. $P:\mathcal{S}\times\mathcal{A}\times\mathcal{S}\mapsto[0,1]$ is the transition function capturing the environment dynamics. $r:\mathcal{S}\times\mathcal{A} \mapsto \mathbb{R}$ is the reward function associated with each state-action pair, $h:\mathcal{S}\mapsto \mathbb{R}^+_0$ is the safety loss function that maps a state to a non-negative real value, which is called the constraint value, or simply cost. $H_{\min}$ is the minimum *non-zero* value of function $h$; $H_{\max}$ is upper bound on function $h$. $\gamma$ is a discount factor in the range $(0,1)$. $\mathcal{S}_I$ is initial state set, $d_0$ is initial state distribution, and $\pi(a|s)$ is a stochastic policy that is parameterized by the state and returns an action distribution from which an action can be sampled and affects the environment defined by the MDP. In unconstrained RL, the goal is to learn an optimal policy $\pi^{\ast}$ maximizing expected discounted sum of rewards, i.e. $\pi^{\ast}=\arg\max_\pi \mathbb{E}_{s\sim d_0} V^\pi (s)$, where $V^\pi(s):=\mathbb{E}_{\tau \sim \pi,P(s)} [\sum_{s_t\in \tau} \gamma^{t} r(s_t,a_t)]$. Note: $\tau \sim \pi,P(s)$ indicates sampling trajectory $\tau$ for horizon $T$ starting from state $s$ using policy $\pi$ in MDP with transition model $P$, and $s_t\in \tau$ is the $t^{th}$ state in trajectory $\tau$."),
    heading("p0003-b006", B(P, "p0003-b006"), "### 3.2 Constrained Markov Decision Process"),
    text("p0003-b007", B(P, "p0003-b007"),
         r"CMDP attempts to optimize the reward returns $V^\pi(s)$ under the constraint that the cost return is below some manually chosen threshold $\chi$. Specifically:"),
    display("p0003-b008", [102.0, 641.0, 510.0, 664.0],
            r"\max_\pi \mathbb{E}_{s\sim d_0}[V^\pi(s)],\text{ subject to }  \mathbb{E}_{s\sim d_0}[V^\pi_c(s)] \leq \chi, \tag{CMDP}"),
    text("p0003-b008w", [107.0, 664.5, 505.0, 679.0],
         r"where cost return function $V^\pi_c(s)$ is often defined as $V^\pi_c(s):=\mathbb{E}_{\tau \sim \pi,P(s)} [\sum_{s_t \in \tau} \gamma^t h(s_t)]$."),
    text("p0003-b009", [107.0, 683.0, 505.0, 725.0],
         r"While many approaches have been proposed to solve within this framework, CMDPs have several difficulties: $1.$ cost threshold $\chi$ often requires much tuning while using prior knowledge of the environment; and $2.$ CMDP often permits some positive average cost which is incompatible with state-wise hard constraint problems, since $\chi$ is usually chosen to be above 0."),
    pageno(P),
]
save(P, items, r"""
Compared with a 150 dpi render of PDF page 3 and with main.tex (end of Section 2.1, Sections 2.2, 3, 3.1, 3.2). The
first item continues the sentence from page 2 ('... else takes steps to minimize | constraint violations.') with
join_previous 'space'. The two Related Work paragraphs are pure prose; extractor text compared with render and TeX and
used unchanged; citations checked: [30], [33], [7], [10], [36], [37], [38], [39], [40], [23, 24], [27], [41], [27],
[42, 43, 44], [45, 46], [47, 48, 49]. Authors' wording kept: 'lagrangian relaxation' (lower case), 'takes framework into
a deterministic hard-constraint setting', 'There are additionally model-based HJ reachability approach'. Section 3.1 and
3.2: all inline mathematics rewritten in LaTeX from the TeX source (extractor output was glyph soup with <sup> tags) and
checked on the render: the MDP tuple with angle brackets, the maps printed with the 'maps to' arrow (\mapsto) for P, r
and h, $\mathbb{R}^+_0$, $H_{\min}$, $H_{\max}$, $\mathcal{S}_I$, $d_0$, $\pi(a|s)$, the optimal policy
$\pi^{\ast}$ (asterisk written \ast), the definitions of $V^\pi$ and $V^\pi_c$ with square brackets around the sums, and
$t^{th}$. The authors' macro \E (an operator printing a blackboard E, with limits underneath in displays) is written
\mathbb{E} with an ordinary subscript. The extractor formula image covered both the display and the following line; it
was replaced by a $$ block carrying the printed tag '(CMDP)' (the equation is tagged with a name, not a number) and a
separate text line 'where cost return function ...'. In the last paragraph the enumerators '1.' and '2.' are printed in
math italic (typed as math in the source) and are written $1.$ and $2.$; the final '0' is plain text. Heading levels
fixed (2.2, 3.1, 3.2 level 3; '3 Preliminaries' level 2). Italic emphasis 'non-zero' kept. Omitted: printed page number 3.
""")
