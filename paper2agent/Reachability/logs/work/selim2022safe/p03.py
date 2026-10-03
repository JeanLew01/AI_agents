from pagelib import *

P = 3

items = furniture(P) + [
    text("p0003-b002", B(P, "b002"),
         r"$\mathbf{G} \in \mathbb{R}^{n \times n_{\text{g}}}$, constraint matrix $\mathbf{A} \in \mathbb{R}^{n_{\text{c}} \times n_{\text{g}}}$, and constraint vector $\mathbf{b} \in \mathbb{R}^{n_{\text{c}}}$ as",
         join_previous="space"),
    text("p0003-eq1", B(P, "b003"),
         r"$$\mathcal{Z}(\mathbf{c},\mathbf{G},\mathbf{A},\mathbf{b}) = \big\{ \mathbf{c} + \mathbf{G}\mathbf{z}\ |\ \mathbf{A}\mathbf{z} = \mathbf{b},\ \lVert\mathbf{z}\rVert_\infty \leq 1 \big\}. \tag{1}$$"),
    text("p0003-b004", B(P, "b004"),
         "By [43, Thm. 1], every convex, compact polytope is a constrained zonotope and vice-versa. For polytopes represented as an intersection of halfplanes, we convert them to constrained zonotopes by finding a bounding box, then applying the halfspace intersection property in [44]."),
    text("p0003-b005", B(P, "b005"),
         r"A zonotope is a special case of a constrained zonotope without equality constraints (but with $\lVert\mathbf{z}\rVert_\infty \leq 1$), which we denote $\mathcal{Z}(\mathbf{c},\mathbf{G})$. For $Z = \mathcal{Z}(\mathbf{c},\mathbf{G}) \subset \mathbb{R}^n$ and a linear map $L$, we have $LZ = \mathcal{Z}(L\mathbf{c}, L\mathbf{G})$; we denote $-Z = -1Z$. The Minkowski sum of two zonotopes $Z_1 = \mathcal{Z}(\mathbf{c}_1,\mathbf{G}_1)$ and $Z_2 = \mathcal{Z}(\mathbf{c}_2,\mathbf{G}_2)$ is given by $Z_1 + Z_2 = \mathcal{Z}(\mathbf{c}_1+\mathbf{c}_2,[\mathbf{G}_1,\mathbf{G}_2])$ [40]. For an $n$-dimensional interval with lower (resp. upper) bounds $\underline{\mathbf{l}} \in \mathbb{R}^n$ (resp. $\overline{\mathbf{l}}$), we abuse notation to represent it as a zonotope $Z = \mathcal{Z}\left(\underline{\mathbf{l}},\overline{\mathbf{l}}\right) \subset \mathbb{R}^n$, with center $\tfrac{1}{2}(\underline{\mathbf{l}}+\overline{\mathbf{l}})$ and generator matrix $\text{diag}\left(\tfrac{1}{2}(\overline{\mathbf{l}} - \underline{\mathbf{l}})\right)$."),
    heading("p0003-b006", B(P, "b006"), "### B. Robot and Environment"),
    text("p0003-b007", B(P, "b007"),
         r"We assume the robot can be described as a discrete-time, nonlinear control system with state $\mathbf{x}_{k} \in X \subset \mathbb{R}^n$ at time $k \in \mathbb{N}$. We assume the state space $X$ is compact. The input $\mathbf{u}_{k}$ is drawn from a zonotope $U_k \subseteq U$ at each time $k$, where $U \subset \mathbb{R}^m$ is a zonotope of all possible actions. We denote process noise by $\mathbf{w}_{k} \in W \subset \mathbb{R}^n$, where $W$ is specified later in Assumption 2. Finally, we denote the black box (i.e., unknown) dynamics $\mathbf{f}: X\times U\times W \to X$, for which"),
    text("p0003-eq2", B(P, "b008"),
         r"$$\mathbf{x}_{k+1} = \mathbf{f}(\mathbf{x}_{k}, \mathbf{u}_{k}) + \mathbf{w}_{k}. \tag{2}$$"),
    text("p0003-b009", B(P, "b009"),
         r"We further assume that $\mathbf{f}$ is twice differentiable and Lipschitz continuous, meaning there exists a *Lipschitz constant* $L^\star$ such that, if $\forall$ $\mathbf{z}_1, \mathbf{z}_2 \in \mathbb{R}^{n+m}$ with $\mathbf{z}_j= (\mathbf{x}_j,\mathbf{u}_j)$, then $\lVert\mathbf{f}(\mathbf{z}_1) - \mathbf{f}(\mathbf{z}_2)\rVert \leq L^\star \lVert\mathbf{x}_1 - \mathbf{x}_2\rVert$. We denote the initial state of the system as $\mathbf{x}_{0}$, drawn from a compact set $X_{0} \subset \mathbb{R}^n$. Note that this formulation leads to an MDP."),
    text("p0003-b010", B(P, "b010"),
         "To enable safety guarantees, we leverage the notion of failsafe maneuvers from mobile robotics [32], [45]."),
    text("p0003-b011", B(P, "b011"),
         r"**Assumption 1.** We assume the dynamics $\mathbf{f}$ are invariant to translation in position, and the robot can brake to a stop in $n_{\text{brk}} \in \mathbb{N}$ time steps and stay stopped indefinitely. That is, there exists $\mathbf{u}_{\text{brk}} \in U$ such that, if the robot is stopped at state $\mathbf{x}_k$, and if $\mathbf{x}_{k+1} = \mathbf{f}(\mathbf{x}_k,\mathbf{u}_{\text{brk}})$, then $\mathbf{x}_{k+1} = \mathbf{x}_k$."),
    text("p0003-b012", B(P, "b012"),
         "Note, many real robots have a braking safety controller available, similar to the notion of an invariant set [29], [28]. Also, failsafe maneuvers exist even when a robot cannot remain stationary, such loiter circles for aircraft [46], [47]."),
    text("p0003-b013", B(P, "b013"),
         "We require that process noise obeys the following assumption for numerical tractability and robustness guarantees."),
    text("p0003-b014", B(P, "b014"),
         r"**Assumption 2.** Each $\mathbf{w}_{k}$ is drawn uniformly from a *noise zonotope* $W = \mathcal{Z}(\mathbf{c}_{\mathbf{w}},\mathbf{G}_{\mathbf{w}})$ with $n_{\text{g},\mathbf{w}}$ generators."),
    text("p0003-b015", B(P, "b015"),
         r"This formulation does not handle discontinuous changes in noise. However, there exist zonotope-based techniques to identify a change in $W$ [48], after which one can compute the system’s reachable set as in the present work. We leave measurement noise and perception uncertainty to future work. We also note, in the case of Gaussian or unbounded noise, one can overapproximate a confidence level set of a probability distribution using a zonotope [40], [48]."),
    text("p0003-b017", B(P, "b017"),
         r"We denote unsafe regions of state space, or *obstacles*, as $X_{\text{obs}} \subset X$. We assume obstacles are static but different in each episode, as the focus of this work is not on predicting other agents’ motion. Furthermore, reachability-based frameworks exist to handle other agents’ motion [33], [49], so the present work can extend to dynamic environments."),
    text("p0003-b018", B(P, "b018"),
         r"We further assume the robot can instantaneously sense all obstacles (that is, $X_{\text{obs}}$) and represent them as a union of constrained zonotopes. In the case of sensing limits, one can determine a minimum distance within which obstacles must be detected to ensure safety, given a robot’s maximum speed and braking distance [32, Section 5]."),
    heading("p0003-b019", B(P, "b019"), "### C. Reachable Sets"),
    text("p0003-b020", B(P, "b020"),
         "We ensure safety by computing our robot’s forward reachable set (FRS) for a given motion plan, then adjusting the plan so that the FRS lies outside of obstacles. We define the FRS, henceforth called the reachable set, as follows:"),
    text("p0003-def1", [311.0, 312.0, 564.0, 346.0],
         r"**Definition 1.** The reachable set $R_{k}$ at time step $k$, subject to a sequence of inputs $\mathbf{u}_{j} \in U_{j} \subset \mathbb{R}^m$, noise $\mathbf{w}_{j} \in W$ $\forall\ j \in \{ 0, \dots, k-1\}$, and initial set $X_{0} \in \mathbb{R}^n$, is the set"),
    text("p0003-eq3", [311.0, 347.0, 564.0, 384.0],
         r"$$\begin{aligned} R_{k} = \big\{&\mathbf{x}_{k} \in \mathbb{R}^n \ \big|\ \mathbf{x}_{j+1} = \mathbf{f}(\mathbf{x}_{j}, \mathbf{u}_{j}) + \mathbf{w}_{j},\ \mathbf{x}_{0} \in X_{0},\\ &\mathbf{u}_{j} \in U_{j},\ \text{and}\ \mathbf{w}_{j} \in W,\ \forall\ j = 0,\cdots,k-1\big\}. \end{aligned} \tag{3}$$"),
    text("p0003-b022", B(P, "b022"),
         r"Recall that we treat the dynamics $\mathbf{f}$ as a black box (e.g., a simulator), which could be nonlinear and difficult to model, but we still seek to conservatively approximate (that is, overapproximate) the reachable set $R_k$."),
    heading("p0003-b023", B(P, "b023"), "### D. Safe RL Problem Formulation"),
    text("p0003-b024", B(P, "b024"),
         r"We denote the state of the RL agent at time $k$ by $\hat{\mathbf{x}}_{k} \in \mathbb{R}^{n_{\text{RL}}}$, which contains the state $\mathbf{x}_k$ of the robot plus information such as sensor measurements and previous actions. At each time $k$, the RL agent chooses $\mathbf{u}_{k}$. Recall that $X_{\text{obs}} \subset \mathbb{R}^n$ denotes obstacles. For a given task, we construct a reward function $\rho: (\hat{\mathbf{x}}_{k},\mathbf{u}_k) \mapsto r_{k} \in \mathbb{R}$ (examples of $\rho$ are given in Section IV). At time $k$, let $\mathbf{p}_k = (\mathbf{u}_j)_{j=k}^{n_{\text{plan}}}$ denote a *plan*, or sequence of actions, of duration $n_{\text{plan}} \in \mathbb{N}$."),
    text("p0003-b025", B(P, "b025"),
         r"Then, our safe RL problem is as follows. We seek to learn a policy $\pi_\theta: \hat{\mathbf{x}}_{k} \mapsto \mathbf{u}_{k}$, represented by a neural network with parameters $\theta$, that maximizes expected cumulative reward. Note that the policy can be deterministic or stochastic. Since rolling out the policy naïvely may lead to collisions, we also seek to create a safety layer between the policy and the robot (that is, to ensure $R_j \cap X_{\text{obs}} = \emptyset$ for all $j \geq k$)."),
    heading("p0003-b026", B(P, "b026"), "## III. Black-box Reachability-based Safety Layer"),
    text("p0003-b027", B(P, "b027"),
         "We unite three components into our BRSL system for collision-free motion planning without a dynamic model of the robot or its surroundings *a priori*. The first component is an environment model, learned online. To find high reward actions (i.e., motion plans) for this model, the second component is an RL agent. Since the agent may create unsafe plans, our third component is a safety layer that combines data-driven reachability analysis with differentiable collision checking to"),
]

save(P, items, r"""
Compared with the 170 dpi render of PDF page 3, five 300 dpi crops (left column top/middle/bottom, right column
middle/bottom) and the TeX source (Sections/4_pb.tex, start of 5_solu.tex; macros from commands.tex expanded: \R, \N,
\vc, \zono -> \mathcal{Z}(...), \ctr/\Gen/\Acon/\bcon/\coef -> bold c, G, A, b, z, \norm -> \lVert..\rVert, \lb/\ub ->
underlined/overlined bold l, \statespace/\actionspace/\noisespace -> X, U, W, \obs/\brk/\nplan/\nrl -> roman
subscripts, \reachset -> R, \RLstate -> hatted bold x, \rewfunc -> \rho, \policy -> \pi). Running header (odd-page
form 'SELIM et al.: BLACK-BOX REACHABILITY-BASED SAFETY') and page number 3 omitted. The first item continues the
sentence from page 2 ('... generator matrix | G in R^{n x n_g} ...'), join_previous 'space'. The three extractor
'formula' images were replaced by LaTeX displays with the printed numbers (1), (2), (3); each was compared symbol by
symbol with the 300 dpi crops. Equation (3) is printed on two lines with one number and is written as one 'aligned'
block. All inline math rewritten from TeX and checked on the crops (the extractor's glyph soup, e.g. for the interval
zonotope with center (1/2)(l_low + l_up) and generator matrix diag((1/2)(l_up - l_low)), was discarded). Theorem-like
blocks: 'Assumption 1.', 'Assumption 2.' and 'Definition 1.' are printed with bold label and period and italic body;
the italics are not reproduced. Their ends are taken from the TeX environments: Assumption 1 ends at
'... then x_{k+1} = x_k.'; Assumption 2 ends at '... generators.' (inside it 'noise zonotope' is printed upright,
i.e. emphasised, and is written in italics); Definition 1 consists of the label item and display (3) that follows it.
The paragraph 'This formulation does not handle ... future work. | We also note, in the case of Gaussian ...' runs
from the bottom of the left column to the top of the right column; it is one paragraph in the TeX source and was
merged. Headings: 'B. Robot and Environment', 'C. Reachable Sets', 'D. Safe RL Problem Formulation' are level 3
(italic subsections); 'III. BLACK-BOX REACHABILITY-BASED SAFETY LAYER' (small caps, plain text in the extractor
output) is level 2. Kept as printed, not conversion errors: the dynamics are declared as f: X x U x W -> X but used
with two arguments in (2); the Lipschitz condition has only ||x_1 - x_2|| on its right-hand side although z_j =
(x_j, u_j), and the norm carries no subscript; 'such loiter circles' (missing 'as'); citation order '[29], [28]';
'initial set X_0 in R^n' with an element sign in Definition 1 (subset sign elsewhere); the plan p_k = (u_j)_{j=k}^{n_plan}
has upper index n_plan here while Algorithms 1-2 use k + n_plan. The last paragraph ends mid-sentence
('... differentiable collision checking to'); it continues on page 4 below the Algorithm 1 float and is joined there.
""")
