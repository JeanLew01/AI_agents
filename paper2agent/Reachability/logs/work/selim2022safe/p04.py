from pagelib import *

P = 4
ALG1 = [44.0, 53.0, 305.0, 328.0]
ALG2 = [307.0, 51.0, 568.0, 294.0]

items = furniture(P) + [
    text("p0004-b004", B(P, "b004"),
         "enable safe trajectory optimization. Theorem 1 summarizes safety via BRSL.",
         join_previous="space"),
    text("p0004-b005", B(P, "b005"),
         r"BRSL is summarized in Algorithm 1. It uses a receding-horizon strategy to create a new safe plan $\mathbf{p}_k$ in each $k^{\text{th}}$ receding-horizon motion planning iteration. Consider a single planning iteration (that is, time step $k$) (Lines 4–16). Suppose the RL agent has previously created a safe plan $\mathbf{p}_{k-1}$ (such as staying stopped indefinitely). At the beginning of the iteration, BRSL creates a new plan $\mathbf{p}_k$ by rolling out the RL agent along with an environment model. Next, BRSL chooses a safe action by adjusting the rolled-out action sequence (Lines 9–11) such that the corresponding reachable set (computed with Algorithm 2) is collision-free and ends with a failsafe maneuver. If the adjustment procedure (as in Algorithm 3) fails to find a safe plan, then the robot executes the failsafe maneuver. Finally, BRSL sends the first action in the current safe plan to the robot, gets a reward, and trains the RL agent and environment model (Lines 12–16). To enable training our environment model online, we collect data in a replay buffer $B$ at each time $k$ (Line 15). We note that BRSL can be used during both training and deployment. That is, the safety layer can operate even for an untrained policy. Thus, for training, we initialize $\pi_\theta$ with random weights."),
    figure("p0004-alg1", ALG1, "Algorithm 1", "algorithm-1"),
    text("p0004-alg1-text", ALG1, alg(r"""
**Algorithm 1:** Safe RL with BRSL
1 **initialize** the RL agent with a random policy $\pi_\theta$, environment model $\mu_\phi$, empty replay buffer $B$, max number of time steps $n_{\text{iter}}$, and a safe plan $\mathbf{p}_0$
2 **for** *each episode* **do**
> 3 **initialize** task with reward function $\rho$
> 4 $\hat{\mathbf{x}}_1 \leftarrow$ observe initial environment state
> 5 **for** $k = 1 : n_{\text{iter}}$ **do**
>> 6 $\mathbf{p}_k \leftarrow$ roll out a trajectory
>> 7 $\hat{R}_k \leftarrow \mathcal{Z}(\mathbf{x}_k,\mathbf{0})$ // init. reachable set
>> 8 $\left(\hat{R}_j\right)_{j=k}^{k+n_{\text{plan}}} \leftarrow \text{reach}\left(\hat{R}_k,\mathbf{p}_k\right)$ // use Alg. 2
>> 9 **if** *any* $\hat{R}_j \cap X_{\text{obs}} \neq \emptyset$ **then**
>>> 10 **try** $\mathbf{p}_k \leftarrow \text{adjust}(\mathbf{p}_k,X_{\text{obs}})$ // use Alg. 3
>>> 11 **catch** execute failsafe maneuver; continue
>> 12 $\mathbf{u}_k \leftarrow$ get first (safe) action from $\mathbf{p}_k$
>> 13 $r_k \leftarrow \rho(\hat{\mathbf{x}}_k,\mathbf{u}_k)$ // get reward
>> 14 $\hat{\mathbf{x}}_{k+1} \leftarrow$ observe next environment state
>> 15 **add** $(\hat{\mathbf{x}}_k, \mathbf{u}_k, r_k, \hat{\mathbf{x}}_{k+1})$ to $B$
>> 16 **train** the RL agent $\pi_\theta$ and the environment model $\mu_\phi$ using minibatch from $B$
""")),
    text("p0004-b006", B(P, "b006"),
         "To proceed, we detail our methods for data-driven reachability and adjusting unsafe actions."),
    heading("p0004-b007", B(P, "b007"), "### A. Data-Driven Reachability Analysis"),
    text("p0004-b008", B(P, "b008"),
         r"BRSL performs data-driven reachability analysis of a plan $\mathbf{p}_k = (\mathbf{u}_j)_{j=k}^{n_{\text{plan}}}$ using Algorithm 2, based on [42]. Algorithm 2 overapproximates the reachable set as in (3) by computing a zonotope $\hat{R}_j \supseteq R_j$ for each time step of the current plan."),
    figure("p0004-alg2", ALG2, "Algorithm 2", "algorithm-2"),
    text("p0004-alg2-text", ALG2, alg(r"""
**Algorithm 2:** Black-box System Reachability [42]
**Input:** initial reachable set $\hat{R}_0$, actions $(\mathbf{u}_j)_{j=k}^{k+n_{\text{plan}}}$
**Parameter:** state/action data $(\mathbf{X}_-,\mathbf{X}_+,\mathbf{U}_-)$, noise zonotope $W = \mathcal{Z}(\mathbf{c}_{\mathbf{w}},\mathbf{G}_{\mathbf{w}})$, Lipschitz constant $L^\star$, covering radius $\delta$
1 $Z_\epsilon \leftarrow \mathcal{Z}(\mathbf{0},\text{diag}(\left(\mathbf{L}^\star\right)_{1} \left(\delta\right)_{1}/2,\cdots,\left(\mathbf{L}^\star\right)_{n} \left(\delta\right)_{n}/2))$ **for** $j = k:(k+n_{\text{plan}})$ **do**
> 2 $\mathbf{M}_j \leftarrow \left(\mathbf{X}_+ - \mathbf{c}_{\mathbf{w}}\right) \begin{bmatrix} \mathbf{1}_{1 \times t_{\text{total}}} \\ \mathbf{X}_- - \mathbf{x}^\star_j \\ \mathbf{U}_- - \mathbf{u}_j \end{bmatrix}^\dagger$
> 3 $\underline{\mathbf{l}} \leftarrow \min_j \Bigg( (\mathbf{X}_{+})_{:\,,j} - \mathbf{M}_j \begin{bmatrix} 1 \\ (\mathbf{X}_-)_{:\,,j} - \mathbf{x}^\star_j \\ (\mathbf{U}_-)_{:\,,j} - \mathbf{u}_j \end{bmatrix} \Bigg)$
> 4 $\overline{\mathbf{l}} \leftarrow$ same as $\underline{\mathbf{l}}$, but use max instead of min
> 5 $Z_{L} \leftarrow \mathcal{Z}\left(\underline{\mathbf{l}},\overline{\mathbf{l}}\right) - W$ and $U_j \leftarrow \mathcal{Z}(\mathbf{u}_j,\mathbf{0})$
> 6 $\hat{R}_{j+1} \leftarrow \mathbf{M}_j (\mathbf{1} \times (\hat{R}_j-\mathbf{x}^\star_j) \times (U_j- \mathbf{u}_j)) + W + Z_L + Z_\epsilon$.
7 **return** $(\hat{R}_j)_{j=k}^{k+n_{\text{plan}}}$ // overapproximates (3)
""")),
    text("p0004-b009", B(P, "b009"),
         r"Our reachability analysis uses noisy trajectory data of the black-box system model collected offline; we use data collected online only for training the policy and environment model. We consider $q$ input-state trajectories of lengths $t_i \in \mathbb{N}$, $i = 1,\cdots,q$, with total duration $t_{\text{total}} = \sum_i^{q} t_i$. We denote the data as $(\mathbf{x}^{(i)}_k)_{k=0}^{t_i}$, $(\mathbf{u}^{(i)}_k)_{k=0}^{t_i-1}$, $i=1, \cdots, q$. To ease notation for the various matrix operations needed in Algorithm 2, we collect the data in matrices:"),
    text("p0004-eq4", B(P, "b013", "b014"),
         r"$$\mathbf{X}_- = \left[\mathbf{x}^{(1)}_0,\cdots,\mathbf{x}^{(1)}_{t_1-1}, \mathbf{x}^{(2)}_0, \cdots, \mathbf{x}^{(q)}_0, \cdots,\mathbf{x}^{(q)}_{t_q-1} \right], \tag{4a}$$"
         "\n\n"
         r"$$\mathbf{X}_+ = \left[\mathbf{x}^{(1)}_1,\cdots,\mathbf{x}^{(1)}_{t_1}, \mathbf{x}^{(2)}_1, \cdots, \mathbf{x}^{(q)}_1, \cdots,\mathbf{x}^{(q)}_{t_q} \right], \tag{4b}$$"
         "\n\n"
         r"$$\mathbf{U}_- = \left[\mathbf{u}^{(1)}_0,\cdots,\mathbf{u}^{(1)}_{t_1-1}, \mathbf{u}^{(2)}_0,\cdots,\mathbf{u}^{(q)}_0,\cdots,\mathbf{u}^{(q)}_{t_q-1} \right]. \tag{4c}$$"),
    text("p0004-b015", B(P, "b015"),
         r"Note, the time steps are different in $\mathbf{X}_-$ and $\mathbf{X}_+$ to simplify considering state transitions corresponding to the actions in $\mathbf{U}_-$. Selecting enough data to sufficiently capture system behavior is a challenge that depends on the system, though specific sampling strategies exist for some systems [28]."),
    text("p0004-b016", B(P, "b016"),
         r"We must approximate the Lipschitz constant of the dynamics for our reachability analysis, which we do from the data $(\mathbf{X}_-,\mathbf{X}_+,\mathbf{U}_-)$ with the method in [42, Section 4, Remark 1]. We also require a data covering radius $\delta$ such that, for any data point $\mathbf{z}_1 \in X\times U$, there exists another data point $\mathbf{z}_2 \in X\times U$ for which $\lVert\mathbf{z}_1 - \mathbf{z}_2\rVert_2 \leq \delta$. We assume sufficiently many data points are known *a priori* to upper-bound $L^\star$ and lower-bound $\delta$; and, we assume $L^\star$ and $\delta$ are the same for offline data collection and online operation. Note, prior work assumes similar bounds [41], [42]."),
    text("p0004-b017", B(P, "b017"),
         r"We find that the reachable set becomes conservative (i.e., large) if the same $L^\star$ and $\delta$ are used for every dimension, because the true dynamics are typically scaled differently in each state dimension. To mitigate this source of conservativeness, we approximate a different $(L^\star)_i$ and $(\delta)_i$ for each dimension, which we then use to compute a Lipschitz zonotope $Z_\epsilon$ (see Line 1 of Algorithm 2). Note, this is an improvement over prior work [42]."),
    heading("p0004-b018", B(P, "b018"), "### B. Adjusting Unsafe Actions"),
    text("p0004-b019", B(P, "b019"),
         r"After the RL agent rolls out a plan $\mathbf{p}_k$, the safety layer adjusts it to ensure it is safe. This is done by checking the"),
]

save(P, items, r"""
Compared with the 170 dpi render of PDF page 4, 300-330 dpi crops of Algorithm 1, Algorithm 2, the right column
(equations (4a)-(4c) and the two paragraphs after them) and the bottom of the left column, and the TeX source
(Sections/5_solu.tex, algorithms/alg_BRSL.tex, algorithms/alg_reach.tex). Running header and page number 4 omitted.
Reading order: both algorithm boxes are floats at the top of the page (Algorithm 1 over the left column, Algorithm 2
over the right column) and both interrupt sentences. The first item is the continuation of the last sentence of page 3
('... differentiable collision checking to | enable safe trajectory optimization.'), join_previous 'space'.
Algorithm 1 (image crop plus transcription) is placed after the paragraph that walks through it ('BRSL is summarized
in Algorithm 1 ...'); Algorithm 2 (image crop plus transcription) is placed after the first paragraph of Section
III-A, which introduces it (the TeX source has the float at the start of that subsection). The paragraph 'Our
reachability analysis uses ... policy and environment | model. We consider q input-state trajectories ...' runs from
the bottom of the left column to below the Algorithm 2 float in the right column and was merged. Algorithm
transcriptions: bold title line as printed ('Algorithm 1: Safe RL with BRSL', 'Algorithm 2: Black-box System
Reachability [42]'), one paragraph per numbered line with the printed line numbers (1-16 and 1-7), nesting shown by
'&emsp;&emsp;' per level following the printed vertical rules, math from the TeX source and checked on the crops. In
Algorithm 2 the printed line 1 contains both the assignment of Z_epsilon and 'for j = k:(k + n_plan) do' (no line
break in the authors' source), so the loop header has no line number of its own and M_j is on line 2; this is kept
as printed (the text refers to 'Algorithm 2, Line 2' for M_j and 'Line 1' for Z_epsilon). In line 1 the printed
symbols are bold L with star and non-bold delta, each in parentheses with an index: (L*)_1 (delta)_1 / 2, ...,
(L*)_n (delta)_n / 2; the Parameter line prints a non-bold L*. Line 6 ends with a printed full stop. Algorithm 1
line 7 prints x_k without a hat (lines 4, 13-15 use the hatted RL state). Crop edges of both algorithm images checked
(top and bottom rules, line numbers at the left, the dagger of the pseudo-inverse in line 2). The two extractor
'formula' images of the data matrices were replaced by three LaTeX displays with the printed numbers (4a), (4b), (4c),
one $$ block per number, kept in one item. Inline math from TeX, checked on the crops: k^th (superscript 'th'),
p_{k-1}, the sum 'sum_i^q t_i' (lower limit printed as 'i' only), the data sequences (x_k^{(i)})_{k=0}^{t_i} and
(u_k^{(i)})_{k=0}^{t_i - 1}, the covering-radius condition with a 2-norm, (L*)_i and (delta)_i. Line-end hyphens:
'receding-horizon' is a real compound (extractor had 'recedinghorizon'). Line ranges 'Lines 4–16', '9–11', '12–16'
and 'Line 15' as printed. Headings 'A. Data-Driven Reachability Analysis' and 'B. Adjusting Unsafe Actions' are level
3. The last paragraph ends mid-sentence ('This is done by checking the'); it continues on page 5 below the Figure 2
float and is joined there. Kept as printed: plan upper index n_plan in the text versus k + n_plan in the algorithms;
Algorithm 2 takes 'initial reachable set R_0' as input although its loop starts at j = k; the linearization point
x*_j is not defined inside the algorithm box (the source comments, not printed, say it is the centre of the current
reachable set); the loop index j of line 1 is reused as the column index in min_j on line 3.
""")
