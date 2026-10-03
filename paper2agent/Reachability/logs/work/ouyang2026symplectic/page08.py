from pt import *
E1 = "&emsp;&emsp;"
ALG = "\n\n".join([
 r"**Algorithm 1** Assignment-Set Construction",
 r"1: **Input:** $\mathcal{D}=\{(x_j,u_j(\cdot),T_{j})\}_{j=1}^M$",
 r"2: **Output:** $\mathcal{K}$",
 r"3: $\mathcal{K}\gets\emptyset$",
 r"4: **for** $j=1,\dots,M$ **do**",
 r"5: " + E1 + r"$s\gets 0$",
 r"6: " + E1 + r"**while** $s<T_{j}$ and $\phi(s,x_j,u_j)\notin S_{\mathrm{tgt}}$ **do**",
 r"7: " + E1*2 + r"$x_i\gets \phi(s,x_j,u_j)$",
 r"8: " + E1*2 + r"choose $t_i\in\arg\max_{t\in(0,T_{j}-s],\,r_i(t)>0} r_i(t)$",
 r"9: " + E1*2 + r"**if** no such $t_i$ exists **then**",
 r"10: " + E1*3 + r"**break**",
 r"11: " + E1*2 + r"**end if**",
 r"12: " + E1*2 + r"$\tau_i\gets t_i$, $u_i\gets u_{i,t_i}$, $r_i\gets r_i(t_i)$",
 r"13: " + E1*2 + r"$\mathcal{K}\gets\mathcal{K}\cup\{(x_i,r_i,u_i)\}$",
 r"14: " + E1*2 + r"$\sigma_i\gets \inf\{\delta:\|\phi(s+\delta,x_j,u_j)-x_i\|=r_i\}$",
 r"15: " + E1*2 + r"**if** the set is empty **then**",
 r"16: " + E1*3 + r"$\sigma_i\gets \tau_i$",
 r"17: " + E1*2 + r"**end if**",
 r"18: " + E1*2 + r"$s\gets s+\sigma_i$",
 r"19: " + E1 + r"**end while**",
 r"20: **end for**",
])
items = [
 T(r"Accordingly, we construct two sequences of states $\{x_i\}_{i=0,\dots N}$ and $\{y_i\}_{i=0,\dots, N}$ as follows. Starting from $x_i$, there exists a time $0 \le t_{1,i} \le T_1$ such that", L, 55, 90),
 T(r"$$y_i = \phi(t_{1,i}, x_i, 0) \in \mathrm{Supp}(\mathcal{K}).$$", L, 95, 110),
 T(r"From $y_i$, applying the control $u_i\in \mathcal{U}^{(0,\tau_i]}$ for time $t_{2,i}:=\tau_i$ yields", L, 112, 138),
 T(r"$$x_{i+1} = \phi(t_{2,i}, y_i, u_i),$$", L, 139, 153),
 T("with the energy decrease condition", L, 159, 169),
 T(r"$$\Delta H(x_{i+1}) + v_0 t_{2,i} \le \Delta H(y_i),$$", L, 175, 190),
 T(r"for all $i = 0,\dots,N$.", L, 196, 206),
 T(r"Thus the policy, iteratively induces the sequence $x_i\xrightarrow {t_{1,i}} y_i\xrightarrow {t_{2,i}} x_{i+1}$.", L, 206, 235),
 T(r"Now, let $N$ be the smallest index such that $x_N \in H_{\mathrm{tgt}}^\epsilon$. Then", L, 236, 259),
 T(r"$$N\tau_{\min}\leq \sum_{i=1}^N t_{2,i}\leq \frac{\Delta H(x_0)}{v_{0}},$$", L, 262, 296),
 T("which implies", L, 300, 310),
 T(r"$$N\leq \left\lfloor \frac{\Delta H(x_0)}{v_{0}\tau_{\min}}\right\rfloor.$$", L, 310, 336),
 T(r"Since $t_{1,i}\leq T_1$, the total time to reach $H_{\mathrm{tgt}}$, i.e. $\overline T$ s.t.", L, 342, 354),
 T(r"$$\forall x_0\in S_0,\ \exists\, T\leq \overline{T}\ \mathrm{s.t.}\ \phi(T,x_0,\pi_{\mathcal{K}})\in H_{\mathrm{tgt}},$$", L, 359, 374),
 T("satisfies", L, 380, 390),
 T(r"""$$\overline{T} \leq \sum_{i=1}^N t_{2,i}+NT_1 \tag{12}$$

$$\leq \frac{\Delta H(x_0)}{v_{0}} + \left\lfloor \frac{\Delta H(x_0)}{v_{0}\tau_{\min}}\right\rfloor T_1 \tag{13}$$

$$\leq \frac{L_{H}D_{\mathcal{X}}}{v_{0}}\Bigl(1+\frac{T_1}{\tau_{\min}}\Bigr). \tag{14}$$""", L, 393, 479),
 T(r"Finally, by Assumption 8, the maximum time $T_{\max}$ to reach $S_{\mathrm{tgt}}$ from $S_0$ satisfies", L, 483, 506),
 T(r"""$$T_{\max}\leq \overline{T}+T_2 \leq \frac{L_{H}D_{\mathcal{X}}}{v_{0}}\Bigl(1+\frac{T_1}{\tau_{\min}}\Bigr)+T_2.$$

$\square$""", L, 509, 550),
 H("### D. From Expert Demonstrations to NCPs", (54, 225), 563, 573),
 T("This subsection explains how the assignment set is constructed from expert demonstrations and how it induces the nonparametric chain policy introduced in Section II-D.", L, 580, 614),
 T(r"Consider a data set $\mathcal{D}=\{(x_j,u_j(\cdot),T_{j})\}_{j=1}^M$ consisting of $M$ expert trajectories, where for each tuple $(x_j,u_j(\cdot),T_{j})\in\mathcal{D}$, the trajectory $\phi(t,x_j,u_j)$, $t\in(0,T_{j}]$ satisfies, $x_{j} \in S_0$ and $\phi(T_{j},x_j,u_j) \in S_{\mathrm{tgt}}^\delta, \forall j = 1,\dots,M$, where $S_{\mathrm{tgt}}^\delta \subseteq H_{\mathrm{tgt}}^\epsilon\cap S_{\mathrm{tgt}}$. The assignment set is obtained by extracting local control snippets and their certified radii along this trajectory. As Algorithm 1 shows, starting from an anchor time $s\in[0,T_{j})$, define $x_i:=\phi(s,x_j,u_j).$ Given a small $v_0$, for each candidate duration $t\in(0,T_{j}-s]$, let $u_{i,t}$ be the restriction of $u_j$ to $(s,s+t]$, so that $\phi(t,x_i,u_{i,t})=\phi(s+t,x_j,u_j)$. Its certified radius is", L, 615, 735),
 T(r"$$r_i(t)= \frac{\Delta H(x_i)-\Delta H(\phi(t,x_i,u_{i,t}))-v_0t} {L_H+L_H e^{Lt}}.$$", R, 194, 223),
 T(r"If $r_i(t)>0$, then $u_{i,t}$ is valid on $\mathcal{B}_{r_i(t)}(x_i)$. We choose $t_i\in\arg\max_{t\in(0,T_{j}-s],\,r_i(t)>0} r_i(t)$, set $\tau_i:=t_i$, $u_i:=u_{i,t_i}$, and $r_i:=r_i(t_i)$, and add $(x_i,r_i,u_i)$ to $\mathcal{K}$. Then let $\sigma_i:=\inf\{\delta\in(0,\tau_i]\mid \phi(s+\delta,x_j,u_j)\in\partial\mathcal{B}_{r_i}(x_i)\},$ with $\sigma_i:=\tau_i$ if the set is empty. The next anchor is $x_{i+1}:=\phi(s+\sigma_i,x_j,u_j),$ which is displayed in Fig 1. Repeating this procedure until the trajectory reaches $S_{\mathrm{tgt}}$, and then over all demonstrations in $\mathcal{D}$, yields $\mathcal{K}=\{(x_i,r_i,u_i)\}_{i=1}^N.$ After the assignment set is constructed, the NCP follows Remark 2 for $\forall x \in \mathcal{X}$.", R, 225, 332),
 FIG("Figure 1", "figure-1", [318, 44, 535, 145]),
 C("Fig. 1: Assignment set construction.", (361, 510), 146, 157),
 FIG("Algorithm 1", "algorithm-1", [311, 340, 561, 603]),
 T(ALG, (313, 559), 603.5, 612),
 H("## IV. Numerical Simulation", (371, 500), 624, 635),
 T(r"We evaluate the proposed NCP on two systems: a spring-mass system and a pendulum, and compare them with a vanilla Behavior Cloning (BC) baseline. The state is written as $x=[q^\top,p^\top]^\top$, where $q$ and $p$ denote the generalized coordinates and momenta. The goal is to drive the state to a small neighborhood of a target state $x^{\ast}$, namely $S_{\mathrm{tgt}}=\{x:\|x-x^{\ast}\|\le \varepsilon\}$, where $\varepsilon = 0.1$. The BC policy is a three-layer multilayer perceptron with hidden sizes $(24, 24, 16)$, trained", R, 641, 735),
]
notes = r"""
Compared with 230 dpi crops of both columns of PDF page 8, a 330 dpi crop of the sentence with the labelled arrows, 150 dpi wide crops around Figure 1 and Algorithm 1, and the authors' TeX source;
mathematics taken from the TeX source (macros \Supp, \tgt, \cD, \K, \cB, \X expanded) and checked against the crops; TeX and PDF agree.
This page holds the rest of the proof of Theorem 4, Section III-D with Figure 1 and Algorithm 1, and the heading and first paragraph of Section IV.
The extractor's formula images were replaced by LaTeX display blocks. Printed equation numbers on this page: (12), (13), (14), the three lines of one aligned display (three tagged blocks in one item; lines (13) and (14)
start with the relation sign as printed). All other displays are unnumbered. The end-of-proof box below the last display of the proof of Theorem 4 is written $\square$.
References resolved as printed: 'Assumption 8', 'Section II-D', 'Algorithm 1', 'Fig 1' (printed without a period), 'Remark 2'.
Reading order and floats: Figure 1 is printed at the top of the right column, in the middle of the sentence '... Its | certified radius is'. The sentence is merged ('... Its certified radius is'), followed by the
display for $r_i(t)$ and the paragraph 'If $r_i(t)>0$ ...' that refers to Fig 1; Figure 1 (image crop, bbox edges checked on the wide crop: all circles, labels $r_0,\dots,r_n$, $x_0,\dots,x_n$, $S_0$, $S_{\mathrm{tgt}}$,
$S^\delta_{\mathrm{tgt}}$ and 'Expert Trajectory' inside, caption outside) and its caption are placed after that paragraph, then Algorithm 1. The caption is verbatim ('Fig. 1: Assignment set construction.').
Algorithm 1 is kept as an image crop (ruled box with title and the 20 numbered lines, edges checked) and is followed by a line-by-line transcription taken from the algorithmic source and checked against the crop:
title in bold as first line, the printed line numbers '1:' to '20:', one paragraph per printed line, nesting shown with two em-spaces per level (levels as printed: lines 5, 6, 19 at level 1; 7-9, 11-15, 17, 18 at level 2; 10 and 16 at level 3).
The extractor had fragmented the box into formula images and text items; those were replaced. The bbox of the transcription item is a thin strip just below the box (the box itself belongs to the image item).
Kept exactly as printed (authors' text, not conversion errors): '$\{x_i\}_{i=0,\dots N}$' (no comma before $N$) next to '$\{y_i\}_{i=0,\dots,N}$'; 'Thus the policy, iteratively induces'; 'for all $i=0,\dots,N$';
the sum in the proof runs over $i=1,\dots,N$; the floor brackets in the bound on $N$ and in (13), whereas the proof of Theorem 2 uses a ceiling; 'i.e. $\overline{T}$ s.t.'; 'the total time to reach $H_{\mathrm{tgt}}$';
'the trajectory ... satisfies, $x_j\in S_0$ and ...'; '$S^\delta_{\mathrm{tgt}}\subseteq H^\epsilon_{\mathrm{tgt}}\cap S_{\mathrm{tgt}}$' ($\delta$ is not otherwise defined); 'follows Remark 2 for $\forall x\in\mathcal{X}$';
the demonstration durations are $T_j$ here ($\tau_j$ in Section II-D); the paragraph defines $\sigma_i$ with $\delta\in(0,\tau_i]$ and $\partial\mathcal{B}_{r_i}(x_i)$ whereas line 14 of Algorithm 1 prints
'$\inf\{\delta:\|\phi(s+\delta,x_j,u_j)-x_i\|=r_i\}$' without a range for $\delta$; in Algorithm 1 the while-condition tests $S_{\mathrm{tgt}}$ and the index $i$ is never incremented explicitly.
The target-state superscript $x^*$ is written with \ast. 'IV. NUMERICAL SIMULATION' (small caps) is a level-2 heading in title case; 'D. From Expert Demonstrations to NCPs' is level 3.
Line-wrap hyphens removed (con-structed); real compounds kept (spring-mass, three-layer, Assignment-Set). The last paragraph ends mid-sentence ('... hidden sizes $(24,24,16)$, trained') and continues on page 9 (joined there).
"""
write(8, items, notes)
