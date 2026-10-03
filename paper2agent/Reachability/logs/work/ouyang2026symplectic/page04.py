from pt import *
items = [
 H("### A. Target Reachability via Chain Policies", (54, 225), 55, 65),
 T(r"As mentioned above, our strategy for reachability is energy-based. We aim to design control actions that drive the system toward the energy levels associated with the target set. Since $S_{\mathrm{tgt}}$ is compact and connected, its image under the Hamiltonian is an interval,", L, 76, 134),
 T(r"$$H(S_{\mathrm{tgt}}) = [H_{\min}, H_{\max}],$$", L, 140, 156),
 T(r"where $H_{\min}:=\min_{x \in S_{\mathrm{tgt}}} H(x)$ and $H_{\max}:=\max_{x \in S_{\mathrm{tgt}}} H(x).$", L, 161, 173),
 T("Once the trajectory reaches this energy band, the zero-input dynamics preserve energy, and the ergodic structure of each energy layer can be used to reach the target set, provided that the target is not dynamically isolated within the layer. This motivates the following assumption.", L, 175, 233),
 T(r"**Assumption 3 (Ergodic Component Coverage).** For every $E \in [H_{\min}, H_{\max}]$ and every ergodic component $K_\alpha^E \subseteq \Sigma_E$,", L, 243, 267),
 T(r"$$S_{\mathrm{tgt}} \cap K_\alpha^E \neq \varnothing.$$", L, 270, 287),
 T("**Remark 3.** Assumption 3 is done for ease of exposition. Violation of this assumption would require a more sophisticated strategy that in philosophy does not depart from the presented here and is left for the journal version of this paper.", L, 294, 340),
 T("To quantify progress toward the target set, we introduce an energy-based distance that measures how far a state lies from the target energy interval. This quantity will serve as a Barrier-like function that we aim to decrease through control actions.", L, 350, 407),
 T(r"**Definition 8 (Energy Signed Distance to $S_{\mathrm{tgt}}$).** Let $H(S_{\mathrm{tgt}}) = [H_{\min}, H_{\max}]$, and define", L, 417, 440),
 T(r"$$H^\star_+ := \frac{H_{\max}+H_{\min}}{2}, \qquad H^\star_- := \frac{H_{\max}-H_{\min}}{2}.$$", L, 444, 469),
 T("The energy distance to the target set is defined as", L, 473, 483),
 T(r"$$\Delta H(x) := |H(x)-H^\star_+| - H^\star_-.$$", L, 488, 504),
 T(r"In particular, $\Delta H(x) \le 0$ if and only if $H(x) \in H(S_{\mathrm{tgt}})$.", L, 510, 521),
 T("We are therefore interested in finding controls that bring the system toward the set", L, 530, 552),
 T(r"$$H_{\mathrm{tgt}} := \{x \in \mathcal{X} : \Delta H(x) \leq 0\}.$$", L, 558, 573),
 T(r"However, in order to provide guarantees, we will require our demonstrations to reach a slightly smaller set. Thus, for any $0 < \epsilon < H^\star_-$, we define", L, 579, 615),
 T(r"$$H_{\mathrm{tgt}}^\epsilon := \{x \in \mathcal{X} : \Delta H(x)\leq -\epsilon\}.$$", L, 619, 635),
 T("This leads to the following assumption.", L, 641, 651),
 T(r"**Assumption 4 (Reachability of $H_{\mathrm{tgt}}^\epsilon$).** For all $x \in \mathcal{X} \setminus H_{\mathrm{tgt}}^\epsilon$, there exist $T > 0$ and $u \in \mathcal{U}^{(0,T]}$ such that", L, 659, 683),
 T(r"$$\phi(T,x,u) \in H_{\mathrm{tgt}}^\epsilon.$$", L, 688, 704),
 T(r"To quantify how quickly the system can be driven toward the target energy band, we introduce the corresponding first hitting time. For any $x \in \mathcal{X}$ and control signal $u \in \mathcal{U}$, define", L, 712, 734),
 T(r"$$T_\epsilon(x,u) := \inf\{t>0 : \phi(t,x,u)\in H_{\mathrm{tgt}}^\epsilon\}.$$", R, 70, 86),
 T(r"Thus, using the energy distance $\Delta H(x)$, we can compute the average decrease rate as", R, 92, 114),
 T(r"$$v_\epsilon(x,u) := \frac{\Delta H(x)-\Delta H(\phi(T_\epsilon(x,u),x,u))}{T_\epsilon(x,u)}. \tag{3}$$", R, 118, 146),
 T(r"By definition $\phi(T_\epsilon(x,u),x,u)\in \partial H_{\mathrm{tgt}}^\epsilon$, thus", R, 149, 162),
 T(r"$$v_\epsilon(x,u)=\frac{\Delta H(x)+\epsilon}{T_\epsilon(x,u)}.$$", R, 167, 194),
 T(r"Thus the best achievable decrease rate at $x$ is given by", R, 198, 208),
 T(r"$$v_\epsilon(x):=\sup_{u\in\mathcal{U}} v_\epsilon(x,u)=\frac{\Delta H(x)+\epsilon}{T_\epsilon^\star(x)}, \tag{4}$$", R, 213, 241),
 T(r"where $T^\star_\epsilon(x)$ is the optimal hitting time maximized (4), i.e., $T^\star_\epsilon(x):=\inf_{u\in\mathcal U}T_\epsilon(x,u)$. This leads to our final requirement.", R, 244, 279),
 T(r"**Assumption 5 (Uniform Positive Energy Decrease Rate).** There exists $\epsilon>0$ such that", R, 287, 309),
 T(r"$$\underline{v_\epsilon} := \inf_{x\in \mathcal{X}\setminus H_{\mathrm{tgt}}^\epsilon} v_\epsilon(x) > 0.$$", R, 314, 336),
 T("We will use the above assumptions to ensure uniform energy decrease toward the target energy band and repeated opportunities to apply control through recurrence of the zero-input dynamics. Once the trajectory reaches this energy band, the ergodic structure of the Hamiltonian flow ensures eventual arrival to the target set.", R, 342, 412),
 T(r"**Theorem 2 (Target Reachability).** Consider system (1) under Assumptions 1–5. Let $\mathcal{K} = \{(x_i, r_i, u_i)\}_{i=1}^N$ be a finite assignment set. Assume that $\mathcal{K}$ satisfies the following:", R, 419, 453),
 T(r"1) **Local energy decrease:** For each $(x_i,r_i,u_i)\in \mathcal{K}$,", R, 456, 467),
 T(r"$$\Delta H(x_i(\tau_i)) + v_0 \tau_i + L_H r_i e^{L \tau_i} \le \Delta H(x_i) - L_H r_i,$$", R, 470, 487),
 T(r"where $x_i(\tau_i):=\phi(\tau_i,x_i,u_i)$, $\tau_{\min}=\min_i\tau_i,\ \text{and }v_0 > 0$.", R, 493, 505),
 T(r"2) **Energy coverage:** Let $c := \sup_{x\in S_0} \Delta H(x)$. Then", R, 506, 518),
 T(r"$$\Delta H(x)\le c \;\implies\; H(x)\in H(\mathrm{Supp}(\mathcal{K})).$$", R, 521, 536),
 T(r"3) **Ergodic coverage:** For all $E \in H(\mathrm{Supp}(\mathcal{K}))$ and all ergodic components $K_\alpha^E \subseteq \Sigma_E$,", R, 542, 566),
 T(r"$$\mathrm{int}(\mathrm{Supp}(\mathcal{K})) \cap K_\alpha^E \neq \emptyset.$$", R, 570, 586),
 T(r"Then, the chain policy $\pi_{\mathcal{K}}$ ensures that for almost every $x_0 \in S_0$, there exists $t<\infty$ such that", R, 591, 615),
 T(r"$$\phi(t,x_0,\pi_{\mathcal{K}}) \in S_{\mathrm{tgt}}.$$", R, 619, 635),
 T("**Proof.** We first establish three key points: (i) each control segment decreases the energy distance on its associated support ball, (ii) whenever the trajectory leaves the support, the zero-input dynamics return it to the support in finite time for almost every initial condition, and (iii) once the trajectory enters the target energy band, it reaches the target set in finite time for almost every initial condition. We then combine these three arguments to conclude the theorem.", R, 641, 734),
]
notes = r"""
Compared with 230 dpi crops of both columns of PDF page 4, a 330 dpi crop of Theorem 2, and the authors' TeX source; mathematics taken from the TeX source
(macros \tgt, \Supp, \X expanded; the spacing-only commands \! of the source dropped) and checked against the crops; TeX and PDF agree.
The extractor's formula images and its glyph-soup text items for displays were replaced by LaTeX display blocks. Only two displays carry a printed number: (3) the average decrease rate
$v_\epsilon(x,u)$ and (4) the best achievable rate $v_\epsilon(x)$; all other displays on the page are unnumbered. References resolved as printed: 'system (1)', 'maximized (4)', 'Assumptions 1–5', 'Assumption 3'.
Reading order: the paragraph 'To quantify how quickly ... the corresponding first | hitting time. For any $x\in\mathcal{X}$ ... define' runs from the bottom of the left column to the top of the right column; merged into one item.
Labels in bold as on the other pages (name printed upright in parentheses between bold number and bold period; 'Remark 3.' has no name). The label of Definition 8 contains mathematics:
'Definition 8 (Energy Signed Distance to $S_{\mathrm{tgt}}$).'; that of Assumption 4: 'Assumption 4 (Reachability of $H^\epsilon_{\mathrm{tgt}}$).'. 'Proof.' is printed in italics and written in bold.
Statement ends (italic bodies, ends from the TeX environments): Assumption 3 ends with its display; Remark 3 is one paragraph; Definition 8 ends with 'In particular, ... $H(x)\in H(S_{\mathrm{tgt}})$.';
Assumption 4 ends with its display; Assumption 5 ends with its display; Theorem 2 consists of the lead-in, the three numbered conditions '1) Local energy decrease', '2) Energy coverage', '3) Ergodic coverage'
(bold-italic run-in names, printed markers '1)', '2)', '3)' kept) with their displays, and the conclusion 'Then, the chain policy ... $\phi(t,x_0,\pi_{\mathcal{K}})\in S_{\mathrm{tgt}}$.'.
The sentence 'where $x_i(\tau_i):=\ldots$, $\tau_{\min}=\min_i\tau_i$, and $v_0>0$.' belongs to condition 1. The proof of Theorem 2 starts on this page (first paragraph) and continues on page 5.
Kept as printed (authors' wording, not conversion errors): the empty set is printed as $\varnothing$ in Assumption 3 and as $\emptyset$ in condition 3 of Theorem 2 (two different glyphs);
'does not depart from the presented here'; 'the optimal hitting time maximized (4)'; 'Barrier-like function'; $\underline{v_\epsilon}$ is printed with the underline under both $v$ and its subscript;
Assumption 5 reads 'There exists $\epsilon>0$' although $\epsilon$ was restricted to $0<\epsilon<H^\star_-$ above; in the hitting-time sentence the control signal is taken in $\mathcal{U}$ (no time superscript);
the name of Definition 8 says 'Signed Distance' while the text says 'energy distance'; $v_0$ in condition 1 is not quantified beyond '$v_0>0$'.
Line-wrap hyphens removed (sophisti-cated); real compounds kept (energy-based, zero-input, Barrier-like). No figures, tables or page furniture. The page ends with a complete paragraph; no join to page 5.
"""
write(4, items, notes)
