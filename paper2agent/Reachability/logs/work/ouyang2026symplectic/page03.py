from pt import *
items = [
 T("theorem [24, Theorem 5.1.3] illustrates how every finite invariant measure admits an ergodic decomposition.", L, 55, 77, join="space"),
 T(r"**Theorem 1 (Ergodic Decomposition on an Energy Layer).** Let $\mu_E$ be an invariant measure on $\Sigma_E$. Then there exists a measurable family of ergodic measures $\{\mu_\alpha^E\}_{\alpha\in\mathcal{A}_E}$ and a probability measure $\nu_E$ on the index set $\mathcal{A}_E$ such that $\mu_E = \int_{\mathcal{A}_E} \mu_\alpha^E\, d\nu_E(\alpha)$.", L, 85, 147),
 T(r"For each $\alpha\in\mathcal{A}_E$, define the corresponding support of the ergodic component by", L, 151, 173),
 T(r"$$K_\alpha^E := \mathrm{supp}(\mu_\alpha^E)\subseteq \Sigma_E,$$", L, 178, 195),
 T(r"where $\mathrm{supp}(\mu):=\{x\in \Sigma_E:\mu(\mathcal{B}_r(x))>0,\ \forall r>0\}$ is the smallest closed subset of $\Sigma_E$ that has full $\mu$-measure. In Theorem 1, each measure $\mu_\alpha^E$ represents an ergodic component of the invariant dynamics on $\Sigma_E$, and $K_\alpha^E$ is the closed region where the corresponding ergodic dynamics take place. On each $K_\alpha^E$, typical trajectories are dense [24, Proposition 4.3.5].", L, 200, 282),
 T(r"**Proposition 1 (Density of Typical Trajectories in an Ergodic Support).** For $\mu_\alpha^E$-almost every $x\in K_\alpha^E$, the forward orbit of $x$ is dense in $K_\alpha^E$, namely", L, 291, 327),
 T(r"$$\overline{\{\phi(t,x,0):t\ge 0\}}=K_\alpha^E.$$", L, 329, 347),
 T(r"Hence, for $\mu_\alpha^E$-almost every initial condition in $K_\alpha^E$, the zero-input trajectory visits every neighborhood of every point in $K_\alpha^E$ infinitely often.", L, 350, 388),
 H("### D. Chain Policies", (54, 128), 398, 408),
 T("Motivated by the nonparametric chain-policy idea in [18], we now specialize the policy construction to the reachability problem for the system (1). The basic idea is to build a finite library of demonstrated control snippets and then select among them according to the current state.", L, 415, 472),
 T(r"Suppose we are given a finite set of expert demonstrations $\mathcal{D}:=\{(x_j,u_j(\cdot),\tau_j)\}_{j=1}^M,$ where each $u_j:(0,\tau_j] \to U$ is a piecewise continuous control signal, and $x_j$ is the corresponding initial states of the expert demonstrations’ trajectories of (1). In addition, let $u_0:(0,\tau_0]\to U$ be a prescribed default control signal, where $\tau_0>0$.", L, 475, 546),
 T(r"**Definition 5 (Control Alphabet).** A ***control alphabet*** is a finite collection of control signals", L, 553, 575),
 T(r"$$\mathcal{A} := \{u_i : (0, \tau_i] \to U\}_{i=0}^{M},$$", L, 580, 597),
 T(r"where each $u_i$ is piecewise continuous and $\tau_i > 0$.", L, 602, 614),
 T("The control alphabet provides a library of candidate control snippets. To determine where each snippet should be applied in the state space, we introduce an assignment set.", L, 621, 655),
 T(r"**Definition 6 (Assignment Set).** An ***assignment set*** is a finite collection of verification triples", L, 663, 685),
 T(r"$$\mathcal{K} := \{(x_i, r_i, u_i)\}_{i=1}^{N} \subseteq \mathbb{R}^n \times \mathcal{R}_{> 0} \times \mathcal{A},$$", L, 688, 706),
 T(r"where $x_i \in \mathbb{R}^n$ is the center state point, $u_i \in \mathcal{A}$ is the control signal assigned to that region, and $r_i > 0$ is its effective radius. The support of $\mathcal{K}$ is", L, 709, 735),
 T(r"$$\mathrm{Supp}(\mathcal{K}) := \bigcup_{i=1}^{N} \mathcal{B}_{r_i}(x_i),$$", R, 68, 104),
 T(r"where $N:=\lvert \mathcal{K} \rvert$ is the size of the assignment set.", R, 108, 119),
 T(r"While an assignment set specifies regions that the control is effective, it does not by itself resolve which control to apply when balls overlap, nor what to do when a state lies outside $\mathrm{Supp}(\mathcal{K})$. Based on assignment set, we introduce a normalized nearest-neighbor selection rule with a default fall-back option. For each $x\in\mathcal{X}$, define $\rho_{\mathcal{K}}(x) := \min_{1\le i\le N}\frac{\|x-x_i\|}{r_i}.$ The associated index map $\iota_{\mathcal{K}}:\mathcal{X} \to \{0,1,\dots,N\}$ is given by", R, 131, 225),
 T(r"$$\iota_{\mathcal{K}}(x):= \begin{cases} \displaystyle \arg\min_{1\le i\le N}\frac{\|x-x_i\|}{r_i}, & \rho_{\mathcal{K}}(x)\le 1,\\ 0, & \text{otherwise}. \end{cases}$$", R, 228, 269),
 T(r"Thus, if $x\in\mathrm{Supp}(\mathcal{K})$, the rule selects the assignment whose normalized distance is minimal; otherwise, it selects the default control $u_0$. In the present analysis, we take $u_0$ to be the zero input, so that when the state lies outside $\mathrm{Supp}(\mathcal{K})$, the system follows the zero-input dynamics until it re-enters the support of the assignment set. Building on this rule, we now formalize the induced nonparametric policy.", R, 275, 357),
 T(r"**Definition 7 (Nonparametric Chain Policy).** Given an assignment set $\mathcal{K}$ and a default control $u_0$, the nonparametric chain policy (NCP) is the map", R, 369, 403),
 T(r"$$\pi_{\mathcal{K}}:\mathcal{X}\to\mathcal{A}$$", R, 409, 425),
 T(r"defined by $\pi_{\mathcal{K}}(x)=u_{\iota_{\mathcal{K}}(x)}.$", R, 430, 443),
 T(r"**Remark 2 (Execution of the Nonparametric Chain Policy).** Given an initial state $x_0=x$, the policy $\pi_{\mathcal{K}}$ induces an infinite-horizon control signal by concatenation. For each $n\ge 0$, define recursively $u_n := \pi_{\mathcal{K}}(x_n), T_n := \tau(u_n), x_{n+1} := \phi(T_n,x_n,u_n)$, where $\tau(u_n)$ denotes the duration of the selected control snippet $u_n$. Let $s_0:=0$ and $s_{n+1}:=s_n+T_n$. Then the induced control signal $u_{\mathcal{K},x}:(0,\infty)\to U$ is defined by", R, 452, 548),
 T(r"$$u_{\mathcal{K},x}(t):=u_n(t-s_n),\qquad t\in[s_n,s_{n+1}).$$", R, 552, 568),
 H("## III. Reachability in Hamiltonian Systems", (333, 538), 578, 588),
 T("We are now ready to present the main results of this paper. We establish target reachability by combining two ingredients: local control actions that reduce an energy-based distance to the target, and recurrence of the zero-input Hamiltonian flow, which returns trajectories to regions where those actions can be reused. Repeating this interplay allows the trajectory to reach the target energy band and, ultimately, the target set. This separation between controlled energy reduction and passive recurrence underlies all results in this section.", R, 617, 734),
]
notes = r"""
Compared with 230 dpi crops of both columns of PDF page 3 and with the authors' TeX source; mathematics taken from the TeX source with the private macros expanded
(\cA to \mathcal{A}, \K to \mathcal{K}, \cD to \mathcal{D}, \cB to \mathcal{B}, \supp to \mathrm{supp}, \Supp to \mathrm{Supp}, \X, \R) and checked against the crops; TeX and PDF agree.
First item continues the last sentence of page 2 ('... The next | theorem [24, Theorem 5.1.3] ...'), join_previous=space.
Reading order repaired: the extractor placed the right-column top ('effective radius. The support of K is', the Supp display, ...) before the lower half of the left column. Definition 6 runs
across the column break ('... and $r_i>0$ is its | effective radius. The support of $\mathcal{K}$ is'); the two halves are merged into one item, followed by the Supp display and 'where N := |K| ...'.
The extractor's nine formula images were replaced by LaTeX display blocks; none of the displays on this page carries a printed equation number. Theorem 1's integral formula is printed inline.
Citations and cross-references resolved to the printed forms: '[24, Theorem 5.1.3]', '[24, Proposition 4.3.5]', '[18]', 'Theorem 1', '(1)'.
Labels: whole label in bold (the PDF prints the name in upright parentheses between a bold 'Theorem 1' and a bold period). Italic bodies are not reproduced; statement ends taken from the TeX
environments and visible as the end of the italic text: Theorem 1 ends with the integral formula; Proposition 1 ends with '... infinitely often.' (it includes the display and the sentence 'Hence, ...');
Definition 5 ends with '... and $\tau_i>0$.'; Definition 6 ends with '... is the size of the assignment set.'; Definition 7 ends with 'defined by $\pi_{\mathcal{K}}(x)=u_{\iota_{\mathcal{K}}(x)}.$';
Remark 2 ends with its display. The terms 'control alphabet' and 'assignment set' are printed in bold italics inside Definitions 5 and 6 and are kept as bold italics.
Kept as printed (authors' wording, not conversion errors): in Definition 6 the set is printed with a calligraphic R, '$\mathbb{R}^n \times \mathcal{R}_{>0} \times \mathcal{A}$'
(the source has \mathcal{R}_{>0}); the control alphabet is indexed $i=0,\dots,M$ while the assignment set has $N$ triples and the index map takes values in $\{0,1,\dots,N\}$;
'$x_j$ is the corresponding initial states'; 'regions that the control is effective'; 'Based on assignment set'; in Remark 2 the three recursive definitions are separated by commas only and the
time interval is half-open on the right, $t\in[s_n,s_{n+1})$, while the signal is declared on $(0,\infty)$; the demonstration durations are written $\tau_j$ here and $T_j$ in Section III-D.
In the cases display the arg min is printed in display style with the limit $1\le i\le N$ below 'min'. 'III. REACHABILITY IN HAMILTONIAN SYSTEMS' (small caps, extractor had plain text) is a
level-2 heading in title case; 'D. Chain Policies' is level 3. Line-wrap hyphens removed (con-trol, intro-duce, as-signment); real compounds kept (chain-policy, nearest-neighbor, fall-back, zero-input,
re-enters, infinite-horizon, energy-based). The page ends with a complete paragraph; no join to page 4. No figures, tables or page furniture.
"""
write(3, items, notes)
