from pt import *
BND = r"\frac{\mu_{H} (1-\frac{v_0}{\underline{v_\epsilon}})^2}{16L_H^2}\frac{\epsilon^2}{\exp(\frac{2L(L_HD_{\mathcal{X}}+\epsilon)}{\underline{v_\epsilon}})}"
items = [
 T("that", (54, 69), 55, 64, join="space"),
 T(r"$$\begin{aligned} & \max_{y_1,y_2\in \mathcal{B}_{r(x)}(x)} \bigl(H(y_1)-H(y_2)\bigr)\\ & \ge \max_{y\in \mathcal{B}_{r(x)}(x)} \bigl(H(y)-H(x)\bigr)\\ & \ge \frac{\mu_{H}}{2}r(x)^2. \end{aligned}$$", L, 68, 136),
 T(r"If $H_+^\star\notin H(\mathcal{B}_{r(x)}(x))$, we have:", L, 139, 153),
 T(r"$$\begin{aligned} &\max_{y_1,y_2\in \mathcal{B}_{r(x)}(x)} |\Delta H(y_1)-\Delta H(y_2)|\\ &=\max_{y_1,y_2\in \mathcal{B}_{r(x)}(x)} |H(y_1)-H(y_2)|\\ &\geq \frac{\mu_{H}}{2}r(x)^2. \end{aligned}$$", L, 157, 222),
 T(r"And if $H_+^\star\in H(\mathcal{B}_{r(x)}(x))$, since (9) holds, there exists at least one $y^\star \in \mathcal{B}_{r(x)}(x)$ such that $H(x)+\frac{\mu_{H}}{2}r(x)^2 \le H(y^\star) \le \max H(\mathcal{B}_{r(x)}(x))$. Thus $[H(x),H(x)+\frac{\mu_{H}}{2}r(x)^2]\subseteq H(\mathcal{B}_{r(x)}(x))$, and therefore we have:", L, 225, 276),
 T(r"$$\max\{|H(x)-H_+^\star|,|H(x)+\frac{\mu_{H}}{2}r(x)^2-H_+^\star|\}\geq \frac{\mu_{H}}{4}r(x)^2.$$", L, 278, 301),
 T(r"Consequently, for any $y_1, y_2 \in \mathcal{B}_{r(x)}(x)$, we have", L, 304, 316),
 T(r"""$$\max_{y_1,y_2\in B_r(x)} |\Delta H(y_1)-\Delta H(y_2)|$$

$$\ge \max_{y_1\in B_r(x)}|H(y_1)-H_+^\star| \tag{10}$$

$$\geq \frac{\mu_{H}}{4}r(x)^2,$$""", L, 320, 386),
 T(r"where inequality (10) holds since we can chose $y_2 \in \mathcal{B}_{r(x)}(x)$ such that $H(y_2) = H_+^{\ast}$.", L, 388, 412),
 T(r"Above all, we know that $\forall x \in \mathcal{X}_c$, we have", L, 417, 428),
 T(r"""$$\max_{y_1,y_2\in \mathcal{B}_{r(x)}(x)} |\Delta H(y_1)- \Delta H(y_2)| \ge \frac{\mu_{H}}{4}r(x)^2$$

$$\ge """ + BND + r""" \tag{11}$$""", L, 430, 492),
 T("**Step 4: Finite covering of the relevant energy interval.** Let", L, 501, 523),
 T(r"$$[H_1,H_2]:=H(\mathcal{X}_c)\cup H(H_{\mathrm{tgt}}^\epsilon).$$", L, 523, 538),
 T(r"For every $E\in[H_1,H_2]$, choose any $x\in\mathcal{X}_c$ with $H(x)=E$. Then $E\in H(\mathcal{B}_{r(x)}(x))$, so the family $\{H(\mathcal{B}_{r(x)}(x))\}_{x\in\mathcal{X}_c}$ covers $[H_1,H_2]$. Since $[H_1,H_2]$ is compact and", L, 543, 579),
 T(r"$$\begin{aligned} & \max_{y_1,y_2\in \mathcal{B}_{r(x)}(x)} |H(y_1)-H(y_2)| \geq \frac{\mu_{H}}{4}r(x)^2\\ \ge & """ + BND + r""" \end{aligned}$$""", L, 581, 645),
 T("there exists a finite subcover", L, 648, 658),
 T(r"$$[H_1,H_2]\subseteq \bigcup_{i=1}^N \mathcal{B}_{r_i}(x_i).$$", L, 661, 696),
 T(r"For each selected center $x_i$, define $r_i:=r(x_i), u_i:=u_{x_i},$ and let", L, 700, 722),
 T(r"$$\mathcal{K}:=\{(x_i,r_i,u_i)\}_{i=1}^N,$$", L, 722, 736),
 T("where this finite selection implies", R, 55, 65),
 T(r"$$[H_1,H_2]\subseteq H(\mathrm{Supp}(\mathcal{K})),$$", R, 70, 87),
 T("which verifies Condition 2 of Theorem 2.", R, 92, 102),
 T(r"**Step 5: Ergodic Coverage.** Moreover, under Assumption 6, each energy layer in the relevant range is itself a unique ergodic component. Since $\mathrm{Supp}(\mathcal{K})$ intersects every energy level in $[H_1,H_2]$, Condition 3 of Theorem 2 also holds.", R, 104, 151),
 T(r"Therefore all three conditions of Theorem 2 are satisfied, and the resulting chain policy $\pi_{\mathcal{K}}$ guarantees that for almost every $x_0\in S_0$, there exists $t<\infty$ such that", R, 153, 188),
 T(r"$$\phi(t,x_0,\pi_{\mathcal{K}})\in S_{\mathrm{tgt}}.$$", R, 192, 209),
 T(r"**Step 6: Sample complexity bound.** By (11), every selected interval $\mathcal{B}_{r_i}(x_i)$ has length at least $\eta$. Hence a greedy interval-covering argument on $[H_1,H_2]$ gives", R, 215, 249),
 T(r"$$\begin{aligned} & N \le \frac{H_2-H_1}{" + BND + r"}\\ & = (H_2-H_1)\, \frac{16L_H^2} {\mu_H\left(1-\frac{v_0}{\underline{v}_\epsilon}\right)^2} \frac{ \exp\!\left( \frac{2L(L_HD_{\mathcal{X}}+\epsilon)}{\underline{v}_\epsilon} \right)} {\epsilon^2}. \end{aligned}$$", R, 252, 337),
 T(r"This completes the proof. $\square$", R, 341, 352),
 H("### C. Finite Time Reachability", (313, 428), 364, 374),
 T("The previous subsection establishes a general reachability theorem and the existence of a chain policy that realizes it. We now refine this qualitative result into a finite-time guarantee by deriving a uniform upper bound on the time required for the chain policy to drive the system to the target set. The key additional assumption is the uniform bounds on the uncontrolled hitting times:", R, 381, 463),
 T("**Assumption 8 (Upper Bound of Hitting Time).** Assume that there are upper bounds of the return time:", R, 471, 493),
 T(r"1) Return time to the support set $\mathrm{Supp}(\mathcal{K})$: $\forall x$ satisfies $H(x)\in [H_{1},H_{2}]$, there exists a finite time $T_1 > 0, \mathrm{s.t.}$ $\min_{t\in(0,T_1]}\mathrm{d}(\phi(t,x,0),\mathrm{Supp}(\mathcal{K}))=0$", R, 498, 534),
 T(r"2) Reaching time to the target set $S_{\mathrm{tgt}}$: $\forall x$ satisfies $H(x) \in [H_{\min},H_{\max}]$, there exists a finite $T_2 > 0, \mathrm{s.t.}$ $\min_{t\in(0,T_2]}\mathrm{d}(\phi(t,x,0),S_{\mathrm{tgt}})=0$", R, 535, 570),
 T("Under this assumption, the maximal time needed to reach the target set can be bounded explicitly.", R, 577, 599),
 T(r"**Theorem 4 (Finite-Time Reachability).** Let $\mathcal{K}$ be an assignment set satisfying the conditions of Theorem 2, and define $\tau_{\min}:=\min_i \tau_i$. Under Assumption 8, the time required to reach the target set from any initial state $x\in S_0$ is uniformly bounded by", R, 608, 665),
 T(r"$$T_{\max} \le \frac{L_H D_{\mathcal X}}{v_0}\Bigl(1+\frac{T_1}{\tau_{\min}}\Bigr) + T_2.$$", R, 668, 697),
 T(r"**Proof.** For any initial state $x_0 \in S_0$, Theorem 2 ensures that each time the trajectory leaves the support set $\mathrm{Supp}(\mathcal{K})$, it returns to the support within time at most $T_1$.", R, 700, 734),
]
notes = r"""
Compared with 230 dpi crops of both columns of PDF page 7, 330 dpi crops of the region around displays (10)-(11), of Step 6 and of Assumption 8 / Theorem 4, and the authors' TeX source; mathematics taken from the
TeX source (macros \cB, \X, \K, \Supp, \tgt expanded) and checked symbol by symbol against the 330 dpi crops; TeX and PDF agree.
First item: the single word 'that' at the top of the left column ends the sentence begun on page 6 ('... according to (9) it follows | that'), join_previous=space; the extractor flagged it as possible header/footer, which it is not.
Reading order repaired: the extractor placed the right-column top ('where this finite selection implies') directly after 'that'; here the left column is read to its end
('... and let $\mathcal{K}:=\{(x_i,r_i,u_i)\}_{i=1}^N,$') before the right column.
This page holds the rest of the proof of Theorem 3 (end of Step 3, Steps 4-6), the heading of Section III-C, Assumption 8, Theorem 4 and the first paragraph of its proof.
The extractor's formula images were replaced by LaTeX display blocks. Printed equation numbers on this page: (10), printed on the middle line of a three-line display (written as three blocks in one item, the tag on
the second), and (11), printed on the second line of a two-line display (two blocks, tag on the second). All other displays are unnumbered, including the bound of Theorem 4 and the two-line display of Step 6.
References resolved as printed: 'since (9) holds', 'inequality (10)', 'By (11)', 'Condition 2 of Theorem 2', 'Condition 3 of Theorem 2', 'Assumption 6', 'Theorem 2', 'Assumption 8'.
The end-of-proof box after 'This completes the proof.' is written $\square$. Statement ends (italic bodies; ends from the TeX environments): Assumption 8 consists of the lead-in sentence and the two numbered items
'1) Return time ...' and '2) Reaching time ...' (printed markers kept; neither item has a final period); Theorem 4 ends with its display.
Kept exactly as printed (authors' text, not conversion errors): in display (10) the max subscripts are '$y_1,y_2\in B_r(x)$' and '$y_1\in B_r(x)$' with an italic $B$ and subscript $r$ only, whereas all other displays
use $\mathcal{B}_{r(x)}(x)$; in 'such that $H(y_2)=H_+^*$' the superscript is an asterisk whereas elsewhere it is a five-pointed star ($H_+^\star$); 'we can chose'; 'Above all, we know that $\forall x$';
no punctuation after display (11) and after the display that follows 'Since $[H_1,H_2]$ is compact and'; the subcover display reads '$[H_1,H_2]\subseteq\bigcup_{i=1}^N\mathcal{B}_{r_i}(x_i)$' (balls, not their images under $H$);
'$[H_1,H_2]:=H(\mathcal{X}_c)\cup H(H^\epsilon_{\mathrm{tgt}})$'; 'has length at least $\eta$' although $\eta$ is not defined anywhere ('every selected interval $\mathcal{B}_{r_i}(x_i)$');
'Step 5: Ergodic Coverage.' with capital C; in Assumption 8 '$\forall x$ satisfies', '$T_1>0,\mathrm{s.t.}$' and 'there exists a finite $T_2>0$' (no word 'time' in item 2); 'The key additional assumption is the uniform bounds'.
In the first line of the Step 6 display the lower rate is printed $\underline{v_\epsilon}$ (underline under $v$ and subscript) and in its second line $\underline{v}_\epsilon$ (underline under $v$ only); both reproduced.
Line-wrap hyphens removed (assign-ment); real compounds kept (interval-covering, finite-time, Finite-Time). The proof of Theorem 4 continues on page 8 with a new paragraph ('Accordingly, ...'); no join. No figures, tables or page furniture.
"""
write(7, items, notes)
