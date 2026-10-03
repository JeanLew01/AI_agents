from pagelib import *

P = 5
ALG3 = [304.0, 52.0, 568.0, 309.0]

items = furniture(P) + [
    text("p0005-b004", B(P, "b004"),
         r"intersection of the plan’s reachable sets with unsafe sets. Note, our proposed adjustment procedure does not depend on $\pi_\theta$, only on the unsafe sets around the robot. The plan is applied to the environment if all of its actions are safe; otherwise, we search for a safe plan. One strategy for finding a safe plan is to sample randomly in the action space [28], but this can be prohibitively expensive in the large action spaces that arise from choosing control inputs at multiple time steps. Instead, we use gradient descent to adjust our plan such that the reachable sets are not in collision, and such that the plan has a failsafe maneuver.",
         join_previous="space"),
    text("p0005-b005", B(P, "b005"),
         r"We adjust unsafe actions using Algorithm 3. If the algorithm does not complete within the duration of one time step (in other words, we fix the rate of receding-horizon planning), we terminate it and continue our previously-found safe plan. Our method steps through each action in a plan $\mathbf{p}$ and performs the following. First, we compute the reachable set for all remaining time steps with Algorithm 2 (Line 5). Second, we collision check the reachable set (Line 6) as detailed below. Third, if the reachable sets are in a collision, we compute the gradient of the collision check and perform projected gradient descent (Line 8) as in fig 2. Finally, if the algorithm converges to a safe plan, we return it, or else return “unsafe.” Note, the final plan must have a failsafe maneuver (Line 11)."),
    figure("p0005-alg3", ALG3, "Algorithm 3", "algorithm-3"),
    text("p0005-alg3-text", ALG3, alg(r"""
**Algorithm 3:** Adjusting Unsafe Actions
**Input:** plan $\mathbf{p}_k = (\mathbf{u}_j)_{j=k}^{n_{\text{plan}}}$, obstacles $X_{\text{obs}}$, initial reachable set $\hat{R}_k$, step size $\gamma$, time limit $t_{\text{max}}$, time steps required to stop $n_{\text{brk}}$
1 // note $\mathbf{p}_k$ has failsafe $\mathbf{u}_{\text{brk}}$ for all $j > k+n_{\text{plan}}$
2 $\mathbf{p}_{\text{safe}} \leftarrow \mathbf{p}_k$ // initialize with given plan
3 **for** $j = k:(k+n_{\text{plan}} + n_{\text{brk}})$ **do**
> 4 **while** *time limit not exceeded* **do**
>> 5 $(\hat{R}_j)_{j=k}^{k+n_{\text{plan}}} \leftarrow \text{reach}\left(\hat{R}_j,\mathbf{p}_{\text{safe}}\right)$ // use Alg. 2
>> 6 $v^\star \leftarrow$ collision check $\hat{R}_j \cap X_{\text{obs}}$ using (6)
>> 7 **if** $v^\star \leq 1$ *(i.e., in collision)* **then**
>>> 8 $\mathbf{u}_j \leftarrow \text{proj}_{U_j}\left(\mathbf{u}_j + \gamma \nabla_{\mathbf{u}_j} v^\star\right)$ // using (7)
>> 9 **else**
>>> 10 **break** and restart inner while loop
11 **if** *all* $\hat{R}_j \cap X_{\text{obs}} = \emptyset$ *and* $\mathbf{x}_n$ *is stopped* **then**
> 12 **return** $\mathbf{p}_{\text{safe}} = (\mathbf{u}_j)_{j=k}^{n_{\text{plan}}}$ // found new safe plan
13 **else**
> 14 **return** error “unsafe” // failed to find safe plan
""")),
    figure("p0005-fig2", [58.0, 52.0, 292.0, 134.0], "Figure 2", "figure-2"),
    caption("p0005-b003", B(P, "b003"),
            r"Fig. 2: We move zonotope reachable sets out of intersection (see Alg. 3) by using the gradient of a collision check, shown in (a), to adjust $\mathbf{u}_0$ so the reachable sets are out of collision as shown in (b)."),
    text("p0005-b006", B(P, "b006"),
         r"We collision check reachable and unsafe sets, all represented as constrained zonotopes, as follows. Consider two constrained zonotopes, $Z_1 = \mathcal{Z}(\mathbf{c}_1,\mathbf{G}_1,\mathbf{A}_1,\mathbf{b}_1)$ and $Z_2 = \mathcal{Z}(\mathbf{c}_2,\mathbf{G}_2,\mathbf{A}_2,\mathbf{b}_2)$. Applying [43, Prop. 1], their intersection is $Z_\cap = Z_1 \cap Z_2 = \mathcal{Z}(\mathbf{c}_{\cap},\mathbf{G}_{\cap},\mathbf{A}_{\cap},\mathbf{b}_{\cap})$, given by"),
    text("p0005-eq5", B(P, "b007"),
         r"$$Z_\cap = \mathcal{Z}\left(\mathbf{c}_1, [\mathbf{G}_1, \mathbf{0}], \begin{bmatrix} \mathbf{A}_1 & \mathbf{0} \\ \mathbf{0} & \mathbf{A}_2 \\ \mathbf{G}_1 & -\mathbf{G}_2 \end{bmatrix}, \begin{bmatrix} \mathbf{b}_1 \\ \mathbf{b}_2 \\ \mathbf{c}_2 - \mathbf{c}_1 \end{bmatrix}\right). \tag{5}$$"),
    text("p0005-b008", B(P, "b008"),
         r"We check if $Z_1 \cap Z_2$ is empty by solving a linear program, as per [43, Prop. 2]:"),
    text("p0005-eq6", B(P, "b009"),
         r"$$v^\star = \min_{\mathbf{z},v} \left\{v\ |\ \mathbf{A}_{\cap} \mathbf{z} = \mathbf{b}_{\cap} \ \text{and}\ |\mathbf{z}| \leq v\right\}, \tag{6}$$"),
    text("p0005-b010", B(P, "b010"),
         r"with $|\mathbf{z}|$ taken elementwise; $Z_\cap$ is nonempty iff $v \leq 1$. Note, (6) is feasible when $Z_1$ and $Z_2$ have feasible constraints."),
    text("p0005-b011", B(P, "b011"),
         r"We use gradient descent to move our reachable sets $\hat{R}_k$ out of collision. Since we use (6) for collision checking, we differentiate its solution with respect to the problem parameters using [50], [51]. Let $\hat{\mathbf{c}}_k$ denote the center of $\hat{R}_k$. Per Algorithm 2, $\hat{R}_k$ is a function of $\mathbf{u}_0,\cdots,\mathbf{u}_{k-1}$. Let $(\mathbf{z}^\star,v^\star)$ be an optimal solution to (6) when the problem parameters (i.e., the input constrained zonotopes) are $\hat{R}_k$ and an unsafe set. Collision avoidance requires $v^\star > 1$ [43, Prop. 2]. We compute the gradient $\nabla_{\mathbf{u}_k} v^\star$ with respect to the input action (assuming a constant linearization point) using a chain rule recursion with $i = 0,\cdots,n_{\text{plan}}$ given by"),
    text("p0005-eq7", B(P, "b021"),
         r"$$\nabla_{\mathbf{u}_{h}} v^\star = \nabla_{\hat{\mathbf{c}}_k} v^\star \nabla_{\hat{\mathbf{c}}_{k-1}} \hat{\mathbf{c}}_k \left(\prod_{j=h+2}^{j=k-1} \nabla_{\hat{\mathbf{c}}_{j-1}} \hat{\mathbf{c}}_j\right) \nabla_{\mathbf{u}_{h}} \hat{\mathbf{c}}_{h+1}, \tag{7}$$"),
    text("p0005-b022", B(P, "b022"),
         r"with $h = k - i$. The gradients of $\hat{\mathbf{c}}_k$ are given by"),
    text("p0005-eq8", B(P, "b023"),
         r"$$\nabla_{\hat{\mathbf{c}}_{k-1}} \hat{\mathbf{c}}_k = (\mathbf{M}_{k-1})_{(1:1+n),(1:1+n)},\ \text{and} \tag{8a}$$"
         "\n\n"
         r"$$\nabla_{u_{k-1}} \hat{\mathbf{c}}_k = (\mathbf{M}_{k-1})_{:,(n+1:n+1+m)}, \tag{8b}$$"),
    text("p0005-b024", B(P, "b024"),
         r"where $\mathbf{M}_{k-1}$ is computed as in Algorithm 2, Line 2, and $n$ and $m$ are the state and action dimensions. After using $\nabla_{\mathbf{u}_k}v^\star$ for gradient descent on $\mathbf{u}_k$, we project $\mathbf{u}_k$ to the set of feasible controls: $\text{proj}_{U_k}(\mathbf{u}_k) = \arg\min_{\mathbf{v} \in U_k} \left\{\lVert\mathbf{u}_k - \mathbf{v}\rVert_2^2\right\}$. The resulting controls may be unsafe, so we collision-check the final reachable sets at the end of Algorithm 3."),
    heading("p0005-b025", B(P, "b025"), "### C. Analyzing Safety"),
    text("p0005-b026", B(P, "b026"),
         "We conclude this section by formalizing the notion that BRSL enables safe RL."),
    text("p0005-b027", B(P, "b027"),
         r"**Theorem 1.** Suppose the assumptions on the robot and environment from Section II all hold, and, at time $k = 0$, the robot is at safe state. Suppose also that, at each time $k > 0$, the robot rolls out a new $\mathbf{p}_k$, then adjusts the plan using Algorithm 3. Then, the robot is guaranteed to be safe at all times $k \geq 0$."),
    text("p0005-b028", B(P, "b028"),
         r"**Proof.** We prove the claim by induction on $k$. At time $0$, the robot can apply $\mathbf{u}_{\text{brk}}$ to stay safe for all time. Assume a safe plan exists at time $k \in \mathbb{N}$. Then, if the output of Algorithm 3 is unsafe (no new plan found), the robot can continue its previous safe plan; otherwise, if a new plan is found, the plan is safe for three reasons. First, the black-box reachability in Algorithm 2 is guaranteed to contain the true reachable set of the system [42, Theorem 2], because process noise is bounded by a zonotope as in Assumption 2. Second, when adjusting an"),
]

save(P, items, r"""
Compared with the 170 dpi render of PDF page 5, 300-330 dpi crops of Figure 2, Algorithm 3, the lower left column
(equations (5), (6)), the right column (equations (7), (8a), (8b)) and Theorem 1 with its proof, and the TeX source
(Sections/5_solu.tex, algorithms/alg_adjust.tex). Running header (odd-page form) and page number 5 omitted. Reading
order: Figure 2 (top of the left column) and Algorithm 3 (top of the right column) are floats that interrupt
sentences. The first item continues the last sentence of page 4 ('This is done by checking the | intersection of the
plan's reachable sets ...'), join_previous 'space'. Algorithm 3 (image crop plus transcription) and Figure 2 with its
caption are placed after the paragraph 'We adjust unsafe actions using Algorithm 3 ...', which walks through the
algorithm and refers to the figure ('as in fig 2', printed in lower case without a period). The paragraph 'We use
gradient descent ... (assuming a | constant linearization point) using a chain rule recursion ...' runs from the
bottom of the left column to below the Algorithm 3 float in the right column and was merged. Algorithm 3
transcription: bold title, 'Input:' block, one paragraph per printed numbered line 1-14 (line 1 is a comment line),
nesting by '&emsp;&emsp;' following the printed vertical rules; italic conditions kept in italics; the update on
line 8 is printed with a plus sign, u_j <- proj_{U_j}(u_j + gamma grad_{u_j} v*). The extractor's fragments of the
box (three text items and three 'formula' images) were replaced. Figure 2 crop checked on a 300 dpi render: both
panels with labels R_0, R_1, u_0, X_obs, 'collision check gradient' and the sub-labels (a), (b); caption excluded
(the hidden '</latexit>' junk string in the PDF text layer of panel (b) lies inside the crop). The five extractor
'formula' images were replaced by LaTeX displays with the printed numbers (5), (6), (7), (8a), (8b); (8a) and (8b)
are two $$ blocks in one item; all checked symbol by symbol on the crops. Inline math from TeX, checked on the
crops. Theorem 1: bold label with period, italic body (italics not reproduced); it ends at '... at all times k >=
0.' (end of the TeX theorem environment). The proof is printed with an italic run-in label 'Proof.', written in bold
here; it continues on page 6 and is joined there. Heading 'C. Analyzing Safety' is level 3. Kept as printed, not
conversion errors: in (8b) the subscript of the gradient is an italic (non-bold) u_{k-1}, while (7) uses bold u_h;
the product in (7) has limits 'j = h+2' and 'j = k-1' (both printed with 'j ='); the text introduces the gradient
with respect to u_k while (7) is written for u_h with h = k - i; index ranges (1:1+n) and (n+1:n+1+m) in (8a)/(8b);
'v <= 1' without star in 'Z_cap is nonempty iff v <= 1'; in Algorithm 3 the plan and the returned plan have upper
index n_plan while line 5 uses k + n_plan, the loop of line 3 runs to k + n_plan + n_brk, line 5 passes R_j (the
Input names R_k), line 10 reads 'break and restart inner while loop', and line 11 tests 'x_n is stopped'; 'at safe
state' in Theorem 1; 'previously-found'.
""")
