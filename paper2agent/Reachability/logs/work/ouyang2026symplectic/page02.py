from pt import *
items = [
 T("as energy variation and ergodic structure—rather than the ambient state dimension.", L, 55, 76, join="space"),
 T("The remainder of the paper is organized as follows. Section II introduces the Hamiltonian system model and formulates the target reachability problem. Section III presents the main theoretical results, including reachability guarantees and sample complexity bounds under chain policies. Section IV provides numerical validation on representative systems, and Section V concludes with a discussion of future directions.", L, 79, 173),
 T(r"*Notation:* We denote by $\|\cdot\|$ the Euclidean norm. For $x \in \mathbb{R}^n$ and $r>0$, let $\mathcal{B}_r(x) := \{ w \in \mathbb{R}^n \mid \|x-w\| \le r \}$ be the closed ball of radius $r$ centered at $x$. For a compact set $S\subseteq \mathbb{R}^n$, let $D_S:=\sup_{x,y\in S}\|x-y\|$ denote its diameter, $\overline{S}$ its closure, $\partial S$ its boundary, and $\operatorname{int}(S)$ its interior. For $\forall x\in\mathbb{R}^n$, the distance from $x$ to set $S$ is $\mathrm{d}(x,S):=\inf_{y\in S}\|x-y\|$. $\lceil \cdot \rceil$ and $\lfloor \cdot \rfloor$ denote the ceiling and floor operators, respectively.", L, 178, 274),
 H("## II. Preliminaries and Problem Formulations", (66, 287), 289, 299),
 H("### A. Hamiltonian System", (54, 150), 308, 317),
 T("In this paper, we firstly review mathematical formulation of **Hamiltonian System**.", L, 325, 347),
 T(r"**Definition 1 (Hamiltonian System).** A Hamiltonian system without energy dissipation is a dynamical system of the form", L, 356, 377),
 T(r"$$\dot{x} = f(x,u) = J(x)\nabla H(x) + G(x)u, \tag{1}$$", L, 381, 400),
 T(r"where $x \in \mathcal{X} \subset \mathbb{R}^n$ is the state defined on a compact set $\mathcal{X}$, $H:\mathbb{R}^n \to \mathbb{R}$ is the Hamiltonian function, $J(x)\in\mathbb{R}^{n\times n}$ is skew-symmetric, and $u\in U\subset \mathbb{R}^m$ is the input of the system defined on a compact U.", L, 402, 451),
 T(r"Physically, $H(x)$ describes the energy of system (1), i.e., sum of kinetic and potential energy in mechanical system, while the skew-symmetric matrix $J(x)$ encodes the intrinsic power-conserving structure. In particular, $J(x)$ determines how energy flows between state variables without creating or dissipating energy. We make the following assumptions about system (1).", L, 459, 541),
 T(r"**Assumption 1 (Bounded Hamiltonian Gradient).** The Hamiltonian function $H$ is continuously differentiable on $\mathcal{X}$ and there exists an upper bound $L_H > 0$ such that $\forall x\in\mathcal{X}, \|\nabla H(x)\|\le L_H$.", L, 550, 596),
 T(r"**Assumption 2 (Lipschitz Continuity of the Dynamics).** The dynamics $f(x,u)$ in (1) are Lipschitz continuous w.r.t. $x$ in both the state and the input. Namely, for any $u \in U$, there exist constants $L>0$ such that", L, 604, 650),
 T(r"$$\|f(x_1,u)-f(x_2,u)\| \le L\|x_1-x_2\|, \forall x_1,x_2\in\mathcal{X}.$$", L, 656, 671),
 T(r"**Remark 1 (Bounded Vector Field).** Since $\mathcal{X}$ and $U$ are compact, and $f$ is continuous by Assumption 2, there exists a constant $C_f>0$ such that", L, 677, 713),
 T(r"$$\|f(x,u)\|\le C_f, \forall x\in\mathcal{X},\ \forall u\in U. \tag{2}$$", L, 718, 733),
 T(r"Since the Hamiltonian $H(\cdot)$ is conserved along the zero-input dynamics, it is natural to partition the state space into invariant energy layers.", R, 54, 89),
 T(r"**Definition 2 (Energy Layer).** For each energy value $E \in H(\mathcal{X})$, the corresponding energy layer is defined as", R, 96, 118),
 T(r"$$\Sigma_E := \{x \in \mathcal{X} : H(x)=E\}.$$", R, 124, 140),
 T(r"$\Sigma_E$ is called an invariant energy layer because, under the zero-input, every trajectory starting in $\Sigma_E$ remains in $\Sigma_E$ for all future times.", R, 145, 179),
 H("### B. Target Reachability Problem", (313, 443), 187, 196),
 T("We now formalize the control objective considered in this paper. Given the Hamiltonian structure introduced above, our goal is to design control inputs that steer the system from a set of admissible initial conditions to a desired target set.", R, 202, 247),
 T(r"Let $\mathcal{U}^{(0,t]}$ denote the set of admissible control signals on $(0,t]$, where each $u:(0,t]\to U$ is piecewise continuous (and measurable); we also use $\mathcal{U}:=\mathcal{U}^{(0,\infty)}$. Further, given any initial condition $x\in\mathcal{X}$ and control input $u\in \mathcal{U}^{(0,t]}$, we use $\phi(t,x,u)$ to denote the state of system (1) at time $t$.", R, 247, 307),
 T(r"Let $S_0 \subseteq \mathcal{X}$ be a compact set of admissible initial states, and let $S_{\mathrm{tgt}} \subseteq \mathcal{X}$ be the prescribed target set.", R, 308, 332),
 T(r"**Problem 1 (Target Reachability).** Given system (1), an initial state $x_0 \in S_0$, and a target set $S_{\mathrm{tgt}}$, determine a control signal $u \in \mathcal{U}^{(0,t]}$ and a time $t>0$ such that", R, 338, 372),
 T(r"$$\phi(t,x_0,u) \in S_{\mathrm{tgt}}.$$", R, 378, 394),
 H("### C. Recurrence on Energy Layers", (313, 449), 400, 409),
 T(r"We next recall the recurrence structure of the zero-input dynamics associated with (1). Since the system is lossless, the Hamiltonian is conserved along zero-input trajectories. Hence, for each energy value $E\in H(\mathcal{X})$, the energy layer $\Sigma_E:=\{x\in\mathcal{X}:H(x)=E\}$ is invariant under the zero-input flow $\phi(t,x,0)$. Our interest is in how trajectories repeatedly revisit dynamically relevant regions on each compact invariant energy layer. We first introduce invariant measures, which describe measures preserved by the zero-input flow.", R, 414, 532),
 T(r"**Definition 3 (Invariant Measure).** A probability measure $\mu$ on $M$ is said to be invariant under the flow $\phi$ if for any measurable set $A \subseteq M$ and any $t \ge 0$, $\mu(\phi(t,A)) = \mu(A).$", R, 540, 574),
 T("To further characterize whether trajectories explore the whole invariant set or remain confined to smaller invariant subsets, we next introduce ergodicity.", R, 581, 615),
 T(r"**Definition 4 (Ergodic Measure).** Let $\mu$ be an invariant probability measure on a set $M$. The measure $\mu$ is said to be ergodic if for any measurable set $A \subseteq M$ that is invariant under the flow, i.e., $\phi(t,A,0) \subseteq A$ for all $t \ge 0$, it holds that $\mu(A) \in \{0,1\}$.", R, 623, 681),
 T(r"Intuitively, ergodicity means that trajectories are not confined to smaller invariant subsets, but instead propagate throughout $M$. In particular, for almost every initial condition, trajectories are dense in the support of $\mu$. The next", R, 688, 734),
]
notes = r"""
Compared with 230 dpi crops of both columns of PDF page 2 and with the authors' TeX source; all mathematics taken from the TeX source with the private macros expanded
(\X to \mathcal{X}, \R to \mathbb{R}, \cB to \mathcal{B}, \tgt to \mathrm{tgt}) and checked against the crops; TeX and PDF agree on this page.
First item continues the last sentence of page 1 ('... of the Hamiltonian—such | as energy variation ...'), join_previous=space.
The extractor's six formula images were replaced by LaTeX display blocks; only two displays carry a printed number: (1) in Definition 1 and (2) in Remark 1. The displays of
Assumption 2, Definition 2 and Problem 1 are unnumbered. Section cross-references resolved to the printed numbers (Sections II, III, IV, V); equation references '(1)' as printed.
'II. PRELIMINARIES AND PROBLEM FORMULATIONS' (small caps, extractor had it as plain text) is a level-2 heading in title case; italic subsection headings A, B, C are level-3 headings
(the extractor had them as level 1 with italic markers). '*Notation:*' is a run-in italic paragraph label, not a heading, and is kept as italic text.
Theorem-like blocks: the PDF prints the label as bold 'Definition 1', the name in upright parentheses and a bold period; here the whole label is bold
('**Definition 1 (Hamiltonian System).**'). Bodies are printed in italics, which is not reproduced; ends taken from the TeX environments and visible on the page as the end of the italic text:
Definition 1 ends with '... defined on a compact U.'; Assumption 1 is one sentence; Assumption 2 ends with its unnumbered display; Remark 1 ends with display (2);
Definition 2 ends with its display; Problem 1 ends with its display; Definitions 3 and 4 are one paragraph each.
Kept as printed (authors' wording, not conversion errors): 'firstly review mathematical formulation of Hamiltonian System' with bold 'Hamiltonian System'; 'defined on a compact U' where the last U is set as text,
not mathematics, in the source; 'For $\forall x \in \mathbb{R}^n$'; 'Lipschitz continuous w.r.t. $x$ in both the state and the input' and 'there exist constants $L>0$' in Assumption 2;
'sum of kinetic and potential energy in mechanical system'; 'under the zero-input'; Definitions 3 and 4 use a set $M$ and a flow $\phi(t,A)$ / $\phi(t,A,0)$ (two- and three-argument forms as printed);
$G(x)$ in (1) is not described in the text.
Line-wrap hyphens removed (for-mulates, guaran-tees, Hamil-tonian, trajecto-ries, con-fined, con-dition); 'zero-input' and 'power-conserving' are real compounds
(the extractor had 'zeroinput'). The last paragraph ends mid-sentence ('... of $\mu$. The next') and continues on page 3 (joined there). No figures, tables or page furniture on this page.
"""
write(2, items, notes)
