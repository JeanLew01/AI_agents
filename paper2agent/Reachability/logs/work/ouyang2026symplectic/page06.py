from pt import *
items = [
 T(r"To establish the existence of the assignment set $\mathcal{K}$, we reduce the problem to a covering argument. In particular, constructing $\mathcal{K}$ requires (i) controlling the complexity of the dynamics within each energy layer, and (ii) relating spatial coverage of $\mathcal{X}$ to coverage of the corresponding energy values. The following two assumptions address these requirements.", L, 55, 136),
 T(r"**Assumption 6 (Ergodicity of Energy Layers).** For every $E \in H(\mathrm{Supp}(\mathcal{K}))$, the energy layer $\Sigma_E$ is ergodic, i.e.,", L, 147, 170),
 T(r"$$\forall E \in H(\mathrm{Supp}(\mathcal{K})),\quad K_\alpha^E = \Sigma_E.$$", L, 173, 191),
 T(r"**Assumption 7 (Strong Convexity of the Hamiltonian).** The Hamiltonian function $H$ is strongly convex on $\mathcal{X}$, i.e., there exists $\mu_H>0$ such that for all $x,y\in\mathcal{X}$,", L, 199, 233),
 T(r"$$H(y)\ge H(x)+\nabla H(x)^\top (y-x)+\frac{\mu_H}{2}\|y-x\|^2.$$", L, 236, 262),
 T("**Remark 5.** Assumption 6 reduces each energy layer to a single dynamically connected region, so that the relevant coverage is effectively one-dimensional and parameterized by energy. This corresponds to a simple setting, which includes, for example, Anosov energy surface and Axiom A systems [25], [26], [27]. In the numerical section, we also consider examples where this assumption is not satisfied. Extending the analysis to more general ergodic decompositions is left for future work.", L, 266, 372),
 T(r"**Remark 6.** Assumption 6 ensures that each energy layer behaves as a single dynamically connected region, eliminating the need to cover multiple ergodic components. Assumption 7 provides a regular relationship between distance in state space and variation in energy, allowing geometric coverings of $\mathcal{X}$ to translate into coverage of the corresponding energy values. Together, these assumptions enable finite coverings that lead to the construction of $\mathcal{K}$.", L, 383, 476),
 T(r"**Theorem 3 (Existence of Chain Policy).** Consider system (1) satisfying Assumptions 4–Assumption 7. Let $v_0 \in (0,\underline{v_\epsilon})$. Then there exists a nonparametric chain policy $\pi_{\mathcal{K}}$, constructed from a finite assignment set $\mathcal{K}=\{(x_i,r_i,u_i)\}_{i=1}^{N}$, where", L, 487, 543),
 T(r"$$r_i=\frac{(v_\epsilon(x_i)-v_0)T_\epsilon^\star(x_i)}{L_H(1+e^{LT_\epsilon^\star(x_i)})}>0,$$", L, 546, 577),
 T(r"with $u_i:(0,T_\epsilon^\star(x_i)]\to U$ being the optimal control for reaching $\partial H_{\mathrm{tgt}}^\epsilon$ from $x_i$, $T_\epsilon^\star(x_i)$ denoting its hitting time, such that the following holds:", L, 580, 615),
 T(r"1) **Reachability:** For almost every $x_0\in S_0$, there exists $t<\infty$ such that $\phi(t,x_0,\pi_{\mathcal{K}})\in S_{\mathrm{tgt}}$.", L, 627, 650),
 T(r"2) **Sample complexity:** Let $H(\mathrm{Supp}(\mathcal{K}))=[H_1,H_2]$. Then", L, 653, 664),
 T(r"$$N\leq (H_2-H_1)\frac{16L_H^2}{\mu_H (1-\frac{v_0}{\underline{v_\epsilon}})^2}\frac{\exp(\frac{2L(L_HD_{\mathcal{X}}+\epsilon)}{\underline{v_\epsilon}})}{\epsilon^2}.$$", L, 667, 706),
 T("**Proof.** We construct a canonical assignment set and then verify the three conditions of Theorem 2.", L, 712, 734),
 T("**Step 1: Canonical local construction.** Let", R, 55, 65),
 T(r"$$\mathcal{X}_c:=\{x\in \mathcal{X}:\Delta H(x)\le c\}\setminus H_{\mathrm{tgt}}^\epsilon.$$", R, 70, 87),
 T(r"For every $x \in \mathcal{X}_c$, by Assumptions 4 and 5, choose an optimal control $u_x:(0,T_\epsilon^\star(x)] \to U$, choose an optimal control $u_x:(0, T_\epsilon^\star(x)] \to U$ such that", R, 92, 126),
 T(r"$$\phi(T_\epsilon^\star(x),x,u_x) \in \partial H_{\mathrm{tgt}}^\epsilon, \, v_\epsilon(x) = \frac{\Delta H(x) + \epsilon}{T_\epsilon^\star(x)}$$", R, 129, 160),
 T("Define the certified radius", R, 162, 172),
 T(r"$$r(x) := \frac{(v_\epsilon(x)-v_0) T_\epsilon^\star(x)}{L_H\bigl(1+e^{LT_\epsilon^\star(x)}\bigr)}.$$", R, 174, 205),
 T(r"Since $v_0<\underline{v}_\epsilon\le v_\epsilon(x)$, we have $r(x)>0$. Moreover,", R, 208, 219),
 T(r"$$\begin{aligned} & \Delta H(\phi(T_\epsilon^\star(x),x,u_x)) +v_0T_\epsilon^\star(x) +L_Hr(x)e^{LT_\epsilon^\star(x)}\\ = & \Delta H(x)-L_Hr(x), \end{aligned}$$", R, 224, 252),
 T(r"so each triple $(x,r(x),u_x)$ satisfies Condition 1 of Theorem 2.", R, 260, 281),
 T(r"**Step 2: Uniform lower bound on the certified radii.** According to Assumption 5: $v_\epsilon(x)\geq \underline{v_\epsilon}>0, v_\epsilon(x)=\frac{\Delta H(x_i)+\epsilon}{T_\epsilon^\star(x)},$ we have $T_\epsilon^\star(x) \leq \frac{\Delta H(x)+\epsilon}{\underline{v_\epsilon}}$. Now recall that $r = \frac{\Delta H(x)+\epsilon-v_0 T_\epsilon^\star(x)}{L_H\bigl(1+e^{LT_\epsilon^\star(x)}\bigr)}$. Then", R, 311, 371),
 T(r"$$\Delta H(x)+\epsilon-v_0 T_\epsilon(x)^\star \geq (\Delta H(x)+\epsilon)\left(1-\frac{v_0}{\underline{v_\epsilon}}\right)> 0,$$", R, 374, 405),
 T(r"because of $0<v_0<\underline{v_\epsilon}$.", R, 408, 418),
 T(r"Therefore, for each fixed $x \in \mathcal{X}_c$, we obtain the lower bound of radius $r(x)$", R, 446, 468),
 T(r"""$$r(x) \geq \frac{ (\Delta H(x)+\epsilon)\left(1-\frac{v_0}{\underline{v_\epsilon}}\right) }{ L_H\left( 1+\exp\!\left(\frac{L(\Delta H(x)+\epsilon)}{\underline{v_\epsilon}}\right) \right) }$$

$$\ge \frac{ \epsilon \left(1-\frac{v_0}{\underline{v_\epsilon}}\right) }{2 L_H \exp(\frac{L(L_H D_{\mathcal{X}} +\epsilon)}{\underline{v_\epsilon}}) }, \tag{8}$$""", R, 471, 556),
 T(r"where equation (8) holds from the fact that $H(x)$ is $L_H$-continuous.", R, 559, 580),
 T(r"**Step 3: Each certified ball covers a nontrivial energy interval.** Fix $x\in\mathcal{X}_c$ and consider the ball $\mathcal{B}_{r(x)}(x)$. By Assumption 7, for any $\|v\|=1$, we have", R, 610, 644),
 T(r"$$H(x+rv)+H(x-rv)\ge2H(x)+ \mu_H r^2,$$", R, 648, 666),
 T(r"so at least one of $x\pm rv$ is larger than the average value, that is to say,", R, 671, 693),
 T(r"$$\max \{H(x+rv),H(x-rv)\}\geq H(x)+\frac{\mu_H }{2}r^2. \tag{9}$$", R, 696, 719),
 T(r"For any $y_1, y_2$ and $y\in \mathcal{B}_{r(x)}(x)$, according to (9) it follows", R, 722, 735),
]
notes = r"""
Compared with 230 dpi crops of both columns of PDF page 6, 330 dpi crops of Theorem 3 and of Step 2 / display (8), and the authors' TeX source; mathematics taken from the TeX source
(macros \X, \Supp, \tgt, \cB expanded) and checked symbol by symbol against the 330 dpi crops; TeX and PDF agree.
The extractor's formula images and glyph-soup text items for displays were replaced by LaTeX display blocks. Printed equation numbers on this page: (8), printed on the second line of the two-line lower bound
for $r(x)$ (written as an untagged first block and a second block with the tag, in one item), and (9). All other displays, including the two displays inside Theorem 3, are unnumbered.
References resolved as printed: 'system (1)', 'Theorem 2', 'Assumptions 4 and 5', 'Condition 1 of Theorem 2', 'Assumption 5', 'Assumption 6', 'Assumption 7', '[25], [26], [27]', 'equation (8)', 'according to (9)'.
Labels in bold as on the other pages; 'Proof.' is printed in italics. Statement ends (italic bodies; ends from the TeX environments): Assumption 6 and Assumption 7 end with their displays;
Remarks 5 and 6 are one paragraph each; Theorem 3 consists of the lead-in with the display for $r_i$, the sentence 'with $u_i$ ... such that the following holds:', and the two numbered items
'1) Reachability' and '2) Sample complexity' (bold-italic run-in names, printed markers kept), ending with the display of the bound on $N$. The proof of Theorem 3 starts on this page (Steps 1-3) and continues on page 7.
Kept exactly as printed (authors' text, not conversion errors): 'Assumptions 4–Assumption 7' in Theorem 3; the repeated clause 'choose an optimal control $u_x$ ..., choose an optimal control $u_x$ ... such that' in Step 1;
no punctuation after the display that follows it; '$\Delta H(x_i)+\epsilon$' with $x_i$ in the numerator of the first inline fraction of Step 2 (the rest of the step uses $x$); 'Now recall that $r=$' without argument;
'$T_\epsilon(x)^\star$' with the star after the argument in the display of Step 2; 'equation (8) holds from the fact that $H(x)$ is $L_H$-continuous'; 'Anosov energy surface and Axiom A systems';
in the bound of Theorem 3 and in (8) the inner fractions are set with small parentheses, 'exp(' followed by a fraction. The lower rate is printed $\underline{v_\epsilon}$ (underline under $v$ and its subscript) everywhere on
this page except in 'Since $v_0<\underline{v}_\epsilon\le v_\epsilon(x)$' (Step 1), where only the $v$ is underlined; both forms are reproduced. The constant $c$ in $\mathcal{X}_c$ is the one defined in Theorem 2 (not redefined here).
Line-wrap hyphens removed (be-haves, Ex-tending, con-structed, Theo-rem); real compounds kept (one-dimensional, $L_H$-continuous). The printed blank bands in the right column (above Step 2, above 'Therefore', above Step 3) are column-balancing space, not missing content.
The last sentence of the page ('For any $y_1,y_2$ and $y\in\mathcal{B}_{r(x)}(x)$, according to (9) it follows') continues on page 7 with the word 'that' (joined there). No figures, tables or page furniture.
"""
write(6, items, notes)
