#!/usr/bin/env python3
from pagelib import write_page

NOTES = r"""
Compared with the 170 dpi render and four 250 dpi crops of PDF page 2 (both columns, upper and lower
halves) and with the TeX source. Reading order: left column top to bottom, then right column. The
first item continues the Notation sentence of page 1 (join_previous 'space'). All inline and display
mathematics rewritten in LaTeX from main.tex with the authors' macros expanded (\X -> \mathcal{X},
\U -> \mathcal{U}, \K -> \mathcal{K}, \R -> \mathcal{R}, \restr{u}{(c,d]} -> \left.u\right|_{(c,d]})
and checked symbol by symbol against the crops; TeX and PDF agree. The six extractor 'formula'
images (signed distance definition, (1), concatenation, Lipschitz inequality, HJI variational
inequality, T-BRT sublevel set) and the T-BRT set definition that the extractor had flattened into
glyph soup are now $$ blocks; only the system equation carries a printed number, written \tag{1}.
'II. PRELIMINARIES AND RELATED WORK' was extracted as plain text and the subsection titles as level-1
headings; they are now '## II. ...' and '### A.'-'### D.'. Theorem-like labels are written in bold with
the printed parenthetical name and period ('Assumption 1 (Forward Completeness).', 'Assumption 2
(Uniform Local Lipschitz Continuity).', 'Definition 1 (Safe State).', 'Definition 2 (Control Invariant
Set).', 'Definition 3 (Backward Reachable Tube).'); the PDF prints the number in bold, the name upright
and the body in italics (italics not reproduced); the words printed bold-italic inside the bodies
('forward complete', 'safe', 'control invariant') are bold. Statement ends taken from the TeX
environments: Assumption 2 ends with the displayed Lipschitz inequality; Definition 3 ends with '...
and denote by R(S).'. Extractor items that mixed a display with the following sentence were split
(Definition 3 display / 'When T = infinity ...'; 'where l(x) ...' / 'Once V(x,T) is computed ...').
Kept as printed (authors' wording, not conversion errors): the value function is written with
l(phi(s,x,u)) and min over s in [-t,0]; the Hamiltonian uses f(x,u) although the system is written
with F; the sublevel-set display reads '{x | V(x,T) <= 0, x in X_u}'; 'computational costly';
'distance to entry X_u'. Citation [3] (twice) read from the page. Line-wrap hyphens removed (system,
Definition, reachability); 'continuous-time', 'Hamilton-Jacobi-Isaacs', 'class-K' are printed hyphens;
'Hamilton–Jacobi' and 'Hamilton–Jacobi–Bellman' are printed with en dashes.
"""

write_page(2, NOTES, [
    ("p0002-b000", "text", ("p0002-b000",),
     r"as $\mathcal{B}_r(x) := \{ y \in \mathbb{R}^n \mid \|y - x\| \leq r \}$. Given a set $S \subseteq \mathbb{R}^n$ and a point $x \in \mathbb{R}^n$, the signed distance from $x$ to $S$ is",
     {"join_previous": "space"}),
    ("p0002-b001", "text", ("p0002-b001",),
     r"""$$
\mathrm{sd}(x,S) :=
\begin{cases}
\inf_{y \in \partial S} \|y - x\|, & \text{if } x \notin S, \\
- \inf_{y \in \partial S} \|y - x\|, & \text{if } x \in S.
\end{cases}
$$""", {}),
    ("p0002-b002", "heading", ("p0002-b002",), "## II. Preliminaries and Related Work", {}),
    ("p0002-b003", "heading", ("p0002-b003",), "### A. Problem Statement", {}),
    ("p0002-b004", "text", ("p0002-b004",), "Consider a continuous-time control system:", {}),
    ("p0002-b005", "text", ("p0002-b005",),
     r"""$$
\dot{x} = F(x,u), \tag{1}
$$""", {}),
    ("p0002-b006", "text", ("p0002-b006",),
     r"where $x \in \mathcal{X} \subseteq \mathbb{R}^{n}$ is the system’s state in the state space $\mathcal{X}$, $u \in U \subseteq \mathbb{R}^m$ is the control input. We define $\mathcal{U}^{(a, b]} := \{u: (a,b] \rightarrow U| u \text{ is measurable}\}$, as the set of control signals on the time interval $(a,b]$, and $\mathcal{U} := \mathcal{U}^{(0,+\infty)}$. Given $u_0 \in \mathcal{U}^{(0,a]}$ and $u_1 \in \mathcal{U}^{(0, b]}$, their concatenation $u_0u_1 \in \mathcal{U}^{(0, a+b]}$ is defined as", {}),
    ("p0002-b007", "text", ("p0002-b007",),
     r"""$$
(u_0u_1)(t) = \begin{cases}
u_0(t), & t \in (0,a], \\
u_1(t), & t \in (a,a+b].
\end{cases}
$$""", {}),
    ("p0002-b008", "text", ("p0002-b008",),
     r"Similarly, for $u\in\mathcal{U}^{(a,b]}$ and $(c,d]\subset(a,b]$ we will use $\left.u\right|_{(c,d]}$ to denote the restriction of $u$ to the interval $(c,d]$.", {}),
    ("p0002-b009", "text", ("p0002-b009",),
     r"In a more general setting, consider a sequence of control inputs $u_n \in \mathcal{U}^{(0,\tau_n]}$, where $\tau_n > 0$ for every $n \in \mathbb{N}$. We define $u_{[n]} := u_0 u_1 \cdots u_n$, and $u_{[\infty]} := \lim_{n \to \infty} u_{[n]}$. At times, we adopt a slight abuse of notation by writing $u$ both for instantaneous inputs in $U$ and for signals in $\mathcal{U}^{(a,b]}$; the intended interpretation will always be clear from context.", {}),
    ("p0002-b010", "text", ("p0002-b010",),
     r"Given an initial state $x \in \mathbb{R}^n$ and a control signal $u \in \mathcal{U}^{(0,a]}$, we denote by $\phi(t,x,u)$ the trajectory solving (1) for all $t \in (0,a]$. Throughout, we impose the following regularity assumptions on (1).", {}),
    ("p0002-b011", "text", ("p0002-b011",),
     r"**Assumption 1 (Forward Completeness).** The control system (1) is **forward complete**, that is, for any initial condition $x \in \mathbb{R}^n$ and any input $u \in \mathcal{U}$, the solution $\phi(\cdot,x,u)$ exists and is unique on $[0,\infty)$.", {}),
    ("p0002-b012", "text", ("p0002-b012",),
     r"**Assumption 2 (Uniform Local Lipschitz Continuity).** The vector field $F(x,u)$ in (1) is locally Lipschitz in $x$, uniformly with respect to $u$. More precisely, for every compact set $S \subseteq \mathbb{R}^n$, there exists a constant $L \geq 0$ such that", {}),
    ("p0002-b013", "text", ("p0002-b013",),
     r"""$$
\| F(y,u) - F(x,u) \| \leq L \|y - x\|, \quad \forall x,y \in S, \; \forall u \in U.
$$""", {}),
    ("p0002-b014", "heading", ("p0002-b014",), "### B. Safety Assessment", {}),
    ("p0002-b015", "text", ("p0002-b015",),
     r"Our goal is finding input signals $u(\cdot) \in \mathcal{U}$ such that the solution $\phi(t,x,u)$ to (1) can avoid an unsafe region $\mathcal{X}_u \subset \mathcal{X}$ for all time $t\geq 0$. To that end, we aim to design an algorithm that can quickly find a strict subset of $\mathcal{X} \backslash \mathcal{X}_u$ that achieves this goal. We will therefore say that a state $x$ is considered to be safe if one can find a control $u \in \mathcal{U}$ such that the state trajectory $\phi(t, x, u)$ does not visit the unsafe region for all future time.", {}),
    ("p0002-b016", "text", ("p0002-b016",),
     r"**Definition 1 (Safe State).** A state $x \in \mathcal{X}$ is said to be **safe** w.r.t. the system (1) if there exists a control $u \in \mathcal{U}$ such that the trajectory $\phi(t, x, u)$ never visits the unsafe region $\mathcal{X}_{u}$, i.e., $\exists u \in \mathcal{U}$, s.t. $\forall t \geq 0,$ $\phi(t, x, u) \notin \mathcal{X}_{u}$.", {}),
    ("p0002-b017", "text", ("p0002-b017",),
     r"A common approach to ensure safety according to Definition 1 is to find some set $\mathcal{C}$ that does not intersect with $\mathcal{X}_u$ and has the additional property that trajectories that start in $\mathcal{C}$ can be kept in $\mathcal{C}$. That is, $\mathcal{C}$ is control invariant.", {}),
    ("p0002-b018", "text", ("p0002-b018",),
     r"**Definition 2 (Control Invariant Set).** A set $\mathcal{C} \subseteq \mathcal{X}$ is **control invariant** w.r.t. (1) if for every $x \in \mathcal{C}$, there exists a control $u \in \mathcal{U}$ such that $\phi(t,x,u) \in \mathcal{C}$ for all $t \ge 0$.", {}),
    ("p0002-b019", "heading", ("p0002-b019",), "### C. Reachability Analysis", {}),
    ("p0002-b020", "text", ("p0002-b020",),
     r"As mentioned before, a widely adopted method to verify safety is the Hamilton–Jacobi (HJ) reachability analysis. In this framework, one aims to compute the collection of all initial states from which, no matter what control one chooses, the trajectory will eventually end in the unsafe set $\mathcal{X}_u$. We provide a formal definition next.", {}),
    ("p0002-b021", "text", ("p0002-b021",),
     r"**Definition 3 (Backward Reachable Tube).** For a set $S$, and constant $T > 0$, the $T$-Backward Reachable Tube ($T$-BRT) is defined as:", {}),
    ("p0002-b022a", "text", [313.0, 290.0, 559.0, 310.0],
     r"""$$
\mathcal{R}_{T}(S) := \{ x \mid \forall u \in \mathcal{U}^{(0, T]}, \exists t \in (0,T], \mathrm{s.t.} \,\phi(t,x,u) \in S \}.
$$""", {}),
    ("p0002-b022b", "text", [313.0, 312.0, 559.0, 335.0],
     r"When $T=\infty$, we refer to it simply as the Backward Reachable Tube (BRT) and denote by $\mathcal{R}(S)$.", {}),
    ("p0002-b023", "text", ("p0002-b023",),
     r"To construct the BRT, the HJ reachability procedure casts the safety verification task as an optimal control problem. Here, the controller’s objective is to avoid the unsafe set $\mathcal{X}_{u}$. This is quantitatively expressed through a value function $V(x,t) := \min_{ s \in [-t, 0]} l(\phi(s, x, u))$, which measures the minimum cost or the distance to entry $\mathcal{X}_{u}$. In the absence of disturbances, the evolution of $V(x,t)$ is governed by a Hamilton-Jacobi-Isaacs Variational Inequality that takes the form of a Hamilton–Jacobi–Bellman equation [3]:", {}),
    ("p0002-b024", "text", ("p0002-b024",),
     r"""$$
\min \{ D_t V(x,t) + H(x,t,\nabla V(x,t)), l(x) - V(x,t) \} = 0,
$$""", {}),
    ("p0002-b025a", "text", [313.0, 478.0, 559.0, 500.0],
     r"where $l(x)$ is the terminal condition where $V(x, 0) = l(x)$, and $H(x, t, \nabla V(x, t)) := \max_{u \in U} D_{x} V(x, t) \cdot f(x, u)$.", {}),
    ("p0002-b025b", "text", [313.0, 501.0, 559.0, 523.0],
     r"Once $V(x,T)$ is computed, the $T$-BRT is given by the sublevel set", {}),
    ("p0002-b026", "text", ("p0002-b026",),
     r"""$$
\mathcal{R}_T(\mathcal{X}_u)=\{ x \mid V(x,T) \le 0, x \in \mathcal{X}_{u} \},
$$""", {}),
    ("p0002-b027", "text", ("p0002-b027",),
     r"which implies that any state within this set will eventually lead to $\mathcal{X}_{u}$ under any control $u(\cdot)$ within less than $T$ units of time. HJ reachability gives rigorous safety guarantees when $x \in \mathcal{R}^{c}_{+\infty}(\mathcal{X}_u)$, which is the largest safe control invariant set, but is computational costly in high dimensions. Efficient solvers for the HJ PDE mitigate this [3], improving practicality. Our work tackles safety from a complementary angle.", {}),
    ("p0002-b028", "heading", ("p0002-b028",), "### D. Control Barrier Functions", {}),
    ("p0002-b029", "text", ("p0002-b029",),
     r"CBFs offer another conservative alternative to HJ reachability. By bounding $\dot h$ with an extended class-$\mathcal{K}$ function, they render a chosen set $\mathcal{C}$ control invariant and thus ensure safety. To formally introduce CBFs we are required to introduce the notion of extended class $\mathcal{K}$ functions.", {}),
])
