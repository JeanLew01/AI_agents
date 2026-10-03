from pt import *
items = [
 T(r"**Step 1: Energy decrease on the support.** Let $y \in \mathrm{Supp}(\mathcal{K})$. Then there exists $i$ such that $y \in \mathcal{B}_{r_i}(x_i)$, i.e., $\|y-x_i\|\le r_i$. By Lipschitz continuity of the dynamics and Grönwall’s inequality,", L, 54, 101),
 T(r"$$\|\phi(t,x_i,u_i)-\phi(t,y,u_i)\|\le r_i e^{Lt}.$$", L, 105, 121),
 T(r"Since $\|\nabla H(x)\|\le L_H$, the function $\Delta H$ is Lipschitz with constant $L_H$, and therefore", L, 127, 151),
 T(r"""$$\Delta H(\phi(\tau_i,y,u_i)) \le \Delta H(\phi(\tau_i,x_i,u_i)) + L_H r_i e^{L\tau_i}, \tag{5}$$

$$\Delta H(x_i) \le \Delta H(y) + L_H r_i. \tag{6}$$""", L, 155, 185),
 T("Combining (5)–(6) with Condition 1 yields", L, 192, 202),
 T(r"$$\Delta H(\phi(\tau_i,y,u_i)) + v_0\tau_i \le \Delta H(y). \tag{7}$$", L, 208, 223),
 T(r"Thus, whenever the state lies in $\mathrm{Supp}(\mathcal{K})$, the corresponding control segment strictly decreases the energy distance to the target set.", L, 229, 263),
 T(r"**Step 2: Return to the support.** Suppose that after applying a control segment from some $y\in \mathrm{Supp}(\mathcal{K})$, the state", L, 270, 292),
 T(r"$$y':=\phi(\tau_i,y,u_i)$$", L, 296, 312),
 T(r"lies outside $\mathrm{Supp}(\mathcal{K})$. From (7), we have", L, 319, 330),
 T(r"$$\Delta H(y') \le \Delta H(y).$$", L, 334, 349),
 T(r"Since the trajectory starts from $S_0$ and $\Delta H$ decreases along each controlled execution, it follows that", L, 357, 379),
 T(r"$$\Delta H(y') \le c := \sup_{x\in S_0}\Delta H(x).$$", L, 384, 406),
 T(r"By Condition 2, this implies that $H(y')\in H(\mathrm{Supp}(\mathcal{K}))$. Notably, for a point $y'$ s.t. $H(y')\in H(\mathrm{Supp}(\mathcal{K}))$, the chain policy applies $u\equiv 0$, so the Hamiltonian is preserved and the trajectory remains on the energy layer", L, 410, 458),
 T(r"$$\Sigma_E, \quad E:=H(y').$$", L, 463, 478),
 T(r"By Condition 3, $\mathrm{int}(\mathrm{Supp}(\mathcal{K}))$ intersects every ergodic component $K_\alpha^E\subseteq \Sigma_E$. Hence, by Theorem 1 and Proposition 1, for almost every initial condition $y'\in \Sigma_E$, the zero-input trajectory $\phi(t,y',0)$ is dense in its ergodic component. Therefore, for almost every $y'$ s.t. $H(y')\in H(\mathrm{Supp}(\mathcal{K}))$, there exists a finite time $T>0$ such that", L, 485, 555),
 T(r"$$\phi(T,y',0)\in \mathrm{Supp}(\mathcal{K}).$$", L, 560, 575),
 T(r"**Step 3: Reachability inside the target energy band.** Suppose now that $y\in H_{\mathrm{tgt}}$, i.e., $H(y)\in [H_{\min},H_{\max}]$. By Assumption 3, the target set $S_{\mathrm{tgt}}$ intersects every ergodic component of the energy layer $\Sigma_{H(y)}$. Since the zero-input dynamics preserve the Hamiltonian, the trajectory remains on $\Sigma_{H(y)}$. Therefore, by Theorem 1 and Proposition 1, for almost every initial condition $y\in H_{\mathrm{tgt}}$, the zero-input trajectory is dense in its ergodic component and hence intersects $S_{\mathrm{tgt}}$ in finite time. That is, for almost every $y\in H_{\mathrm{tgt}}$, there exists $T'>0$ such that $\phi(T',y,0)\in S_{\mathrm{tgt}}.$", L, 588, 706),
 T(r"**Conclusion.** Starting from any $x_0 \in S_0$, the chain policy alternates between controlled segments and zero-input evolution. By Step 1, each controlled execution decreases $\Delta H$ by at least $v_0\tau_{\min}>0$, and thus after at most $N_{\ast}=\left\lceil \frac{c}{v_0\tau_{\min}} \right\rceil$ executions the trajectory enters $H_{\mathrm{tgt}}$. By Steps 2 and 3, each excursion outside the support returns in finite time, and once in $H_{\mathrm{tgt}}$ the trajectory reaches $S_{\mathrm{tgt}}$ in finite time for almost every initial condition.", L, 712, 734),
 T(r"Since only finitely many such events occur and the flow maps are continuous, the union of all exceptional null sets remains null after finitely many concatenation of controls. Therefore, for almost every $x_0 \in S_0$, there exists $t<\infty$ such that $\phi(t,x_0,\pi_{\mathcal K}) \in S_{\mathrm{tgt}}.$ $\square$", R, 130, 188),
 T(r"**Remark 4.** Theorem 2 shows that reachability does not require coverage of the full state space. Instead, it is sufficient to cover (i) the one-dimensional energy interval connecting $S_0$ to $S_{\mathrm{tgt}}$, and (ii) the ergodic components within each corresponding energy layer. This reduces the coverage requirement from the full $n$-dimensional state space to a structure parameterized by energy and the ergodic index $\alpha$. In particular, reachability can be achieved by covering a set whose effective dimension is that of $\alpha$ plus one, accounting for energy, without requiring demonstrations throughout the state space.", R, 197, 326),
 H("### B. Existence of the Chain Policy", (313, 448), 336, 346),
 T(r"Theorem 2 provides conditions on the assignment set $\mathcal{K}$ under which the chain policy guarantees target reachability. However, it is not a priori clear whether such conditions can be satisfied using a finite set of control segments. To address this question, we first derive upper and lower bounds on the quantities that govern energy decrease and recurrence, which will allow us to establish existence and sample complexity guarantees for $\mathcal{K}$.", R, 351, 445),
 T(r"**Lemma 1 (Velocity and Hitting-Time Bounds).** Under Assumption 5, the energy decrease rate and the first hitting time to $H_{\mathrm{tgt}}^\epsilon$ satisfy, for all $x \in \mathcal{X}\setminus H_{\mathrm{tgt}}$,", R, 454, 490),
 T(r"$$v_\epsilon(x) \le L_H C_f, \quad\text{ and }\quad T_\epsilon^\star(x) \ge \frac{\epsilon}{L_H C_f}.$$", R, 492, 518),
 T("**Proof.** From (2), we have", R, 523, 532),
 T(r"$$\begin{aligned} &|\Delta H(x) - \Delta H(\phi(T,x,u))| \le L_H \|x - \phi(T,x,u)\| \\ &= L_H \Big\|\int_0^T f(\phi(t,x,u),u(t))\,dt\Big\| \le L_H C_f T. \end{aligned}$$", R, 538, 583),
 T("Combining the above with (3), it follows that", R, 586, 596),
 T(r"$$v_\epsilon(x,u) = \frac{\Delta H(x)-\Delta H(\phi(T_\epsilon(x,u),x,u))}{T_\epsilon(x,u)} \le L_H C_f.$$", R, 600, 628),
 T(r"Hence $v_\epsilon(x)\le L_H C_f$, and", R, 632, 643),
 T(r"$$v_\epsilon(x)=\frac{\Delta H(x)+\epsilon}{T_\epsilon^\star(x)} \le L_H C_f, \;\; \Rightarrow \;\; T_\epsilon^\star(x)\ge \frac{\Delta H(x)+\epsilon}{L_H C_f}.$$", R, 648, 677),
 T(r"Since $\Delta H(x)>0$ for all $x\in \mathcal{X}\setminus H_{\mathrm{tgt}}$, we obtain", R, 680, 691),
 T(r"""$$T_\epsilon(x,u)\ge T_\epsilon^\star(x)\ge \frac{\epsilon}{L_H C_f}, \quad \forall x\in\mathcal{X}\setminus H_{\mathrm{tgt}},\ u\in\mathcal{U}.$$

$\square$""", R, 693, 734),
]
notes = r"""
Compared with 230 dpi crops of both columns of PDF page 5 and with the authors' TeX source; mathematics taken from the TeX source (macros \Supp, \tgt, \X expanded) and checked against the crops; TeX and PDF agree.
This page holds the rest of the proof of Theorem 2 (Steps 1-3 and Conclusion; the bold run-in step titles are kept in bold), Remark 4, the heading of Section III-B, Lemma 1 and its proof.
The extractor's formula images were replaced by LaTeX display blocks. Printed equation numbers on this page: (5) and (6) (two lines of one aligned display, written as two tagged blocks in one item) and (7);
all other displays are unnumbered. References resolved as printed: 'Combining (5)–(6) with Condition 1', 'From (7)', 'Condition 2', 'Condition 3', 'Theorem 1 and Proposition 1', 'Assumption 3',
'Step 1', 'Steps 2 and 3', 'Theorem 2', 'Assumption 5', 'From (2)', 'with (3)'.
Reading order: the 'Conclusion.' paragraph starts at the bottom of the left column ('... zero-input evo-') and continues at the top of the right column ('lution. By Step 1, ...'); merged into one item.
End-of-proof boxes (printed as hollow squares at the right margin after '... $\in S_{\mathrm{tgt}}$.' and below the last display of the proof of Lemma 1) are written as $\square$.
'Proof.' is printed in italics and written in bold. Statement ends from the TeX environments: Remark 4 is one paragraph (italic); Lemma 1 ends with its display (the word 'and' inside the display is printed in italics as part of the statement).
The ceiling in $N_{\ast}=\lceil c/(v_0\tau_{\min})\rceil$ is printed with tall brackets around an inline fraction; the subscript asterisk of $N_*$ is written \ast.
Kept as printed (authors' wording, not conversion errors): 'after finitely many concatenation of controls'; 'for a point $y'$ s.t. $H(y')\in H(\mathrm{Supp}(\mathcal{K}))$, the chain policy applies $u\equiv 0$';
the proof's bound $N_*$ uses $c$ and $\tau_{\min}$ and says the trajectory 'enters $H_{\mathrm{tgt}}$'; Lemma 1 is stated 'for all $x\in\mathcal{X}\setminus H_{\mathrm{tgt}}$' (no $\epsilon$ superscript on the set);
in the last display the quantifier reads '$\forall x\in\mathcal{X}\setminus H_{\mathrm{tgt}},\ u\in\mathcal{U}$'. 'Grönwall’s' is printed with the umlaut.
Line-wrap hyphens removed (corre-sponding, com-ponent, trajec-tory, evo-lution, connect-ing, As-sumption); real compounds kept (zero-input, one-dimensional, $n$-dimensional, Hitting-Time).
No figures, tables or page furniture. The page ends with the end of the proof of Lemma 1; no join to page 6.
"""
write(5, items, notes)
