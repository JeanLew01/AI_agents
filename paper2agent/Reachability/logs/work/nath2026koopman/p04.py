from pagelib import *
P = 4
items = [
    text("p0004-b001", B(P, "p0004-b001"),
         r"according to $\phi^\infty(x_{t+1}) = \mathcal{K} \phi^\infty(x_t)$, where $\circ$ denotes function composition. As infinite-dimensional Koopman operators are intractable to obtain in practice, we define an approximation to $\mathcal{K}$ using a finite-dimensional lifting function $\phi: \mathcal{X} \rightarrow \mathcal{Z} \subseteq \mathbb{R}^{l}$ and matrix $K_{A} \in \mathbb{R}^{l \times l}$, which define lifted dynamics $z_{t+1} = K_{A} z_{t}$, where $z_t = \phi(x_t)$ is the lifted state and $z_{t} \in \mathcal{Z} \subseteq \mathbb{R}^{l}$. Here, $l$ can be arbitrarily selected by the choice of the lifting function $\phi$. For systems with control input (1a), the lifted dynamics can be similarly written as $z_{t+1} = K_{A} z_{t} + K_{B} u_t$, where $K_{B} \in \mathbb{R}^{l \times m}$. In practice, $\phi$, $K_A$, and $K_B$ can be learned from data, with the lifting function $g$ parameterized using polynomials or NNs (Shi et al., 2024). In this work, we utilize an NN-based autoencoder architecture, where the encoder $\phi: \mathcal{X} \rightarrow \mathcal{Z}$ defines the lifting function and the decoder $\psi: \mathcal{Z} \rightarrow \hat{\mathcal{X}}$ defines its learned inverse, i.e., $\psi(\phi(x)) \approx x$; if $\psi$ is a perfect inverse, $\psi(\phi(x)) = x$ and $\hat{\mathcal{X}} = \mathcal{X}$.",
         join_previous="space"),
    text("p0004-b002", B(P, "p0004-b002"),
         r"**Reachability via NN Verification (NNV)** We use NNV to compute reachable sets for closed-loop systems involving NN-based lifting and inverse functions. NNV tools represent an NN as a computational graph (CG) – a directed acyclic graph encoding the sequence of operations applied to an input (Rober and How, 2024). For some CG $G$ with input set $\mathcal{S} \subseteq \mathbb{R}^{n_i}$ and output $G(\mathcal{S}) \subseteq \mathbb{R}^{n_o}$, we can compute a guaranteed overapproximation of its image $G(\mathcal{S})$ using CROWN-based (Zhang et al., 2018) tools like `auto_LiRPA` (Xu et al., 2020). These tools provide guaranteed affine lower and upper bounds, $\underline{G}$ and $\overline{G}$, on the output $G(\mathcal{S})$ for any interval $\mathcal{S}$, formalized in this proposition:"),
    text("p0004-b003", B(P, "p0004-b003"),
         r"**Proposition 1 (CG Robustness (Xu et al., 2020))** For some CG $G$ and interval $\mathcal{S} \doteq \{s \in \mathbb{R}^{n_i} \mid \underline{s} \le s \le \overline{s}\}$, there are affine functions $\underline{G}$, $\overline{G}$ such that $\forall s \in \mathcal{S}$, $\underline{G}(s) \leq G(s) \leq \overline{G}(s)$. The inequalities hold element-wise and $\underline{G}(s) = \Psi s + \alpha$, $\overline{G}(s) = \Phi s + \beta$, with $\Psi, \Phi \in \mathbb{R}^{n_o \times n_i}$ and $\alpha, \beta \in \mathbb{R}^{n_o}$."),
    text("p0004-b004", B(P, "p0004-b004"),
         r"Given controller $\pi$, dynamics (1a), and initial set $\mathcal{X}_0$, the $T$-timestep exact reachable set is denoted as $\mathcal{X}_{0:T} \doteq \{\mathcal{X}_0, f(\mathcal{X}_t, \pi(\mathcal{X}_t,t)) \}_{t=0}^{T-1}\}$. While exact reachability analysis is generally intractable for nonlinear systems (Althoff et al., 2021), it is often feasible to compute a reachable set overapproximation (RSOA) $\overline{\mathcal{X}}_{0:T}$, which satisfies $\mathcal{X}_t \subseteq \overline{\mathcal{X}}_t$ for all $t \in \{0,\ldots,T\}$. To obtain $\overline{\mathcal{X}}_{0:T}$, Prop. 1 can be applied to the CG $F$ of the $T$-step composition ${\tilde f^{T}}(\cdot) \doteq \tilde{f} \circ \dotsb \circ \tilde{f}(\cdot)$ of the closed-loop dynamics $\tilde f$ (1b), i.e., $F(x_0) \doteq \{\tilde f(x_t) \doteq f(x_t, \pi(x_t, t)) \}_{t=0}^{T}$, with `auto_LiRPA` computing the RSOA."),
    text("p0004-b005", B(P, "p0004-b005"),
         r"**Conformal Prediction (CP)** Our RSOA computations also rely on CP. In this work, we adopt split CP, which partitions i.i.d. input-output pairs $(v^{(i)}, y^{(i)}) \in \mathcal{V}\times\mathcal{Y}$ from a dataset $\mathcal{D} \doteq\{(v^{(i)}, y^{(i)})\}_{i=1}^{L+K}$ into a size-$L$ training set $\mathcal{D}_T$ and a size-$K$ calibration set $\mathcal{D}_C$. For a given prediction function $\mu:\mathcal{V}\!\to\!\mathcal{Y}$, we compute a nonconformity score $R^{(i)}\!\doteq s(y^{(i)},\mu(v^{(i)}))$ for each of the $K$ calibration pairs in $\mathcal{D}_C$, where $s: \mathcal{Y}\times \mathcal{Y} \rightarrow \mathbb{R}_{\ge 0}$ is a chosen nonconformity score function. As an example, we can express the $\ell_2$ prediction error of a learned dynamics model $\hat f$ in this framework by defining $v = (x_t, u_t)$, $y = x_{t+1}$, $\mu(v) = \hat f(v)$, and $s(y, \mu(v)) = \Vert y - \mu(v)\Vert_2$. Given a miscoverage level $\delta\in(0,1)$, a threshold $C$ is defined as the ($1-\delta$)-quantile of the calibration scores, $C \doteq \text{Quantile}_{1-\delta}(R^{(1)},\dots,R^{(K)},\infty)$. This threshold defines the prediction set $\mathcal{Y}(v) \doteq \{\,y\in\mathcal{Y} \mid s(y,\mu(v))\le C \,\}$, which satisfies the marginal coverage guarantee $\mathbb{P}(y^{(0)}\in\mathcal{Y}(v^{(0)})) \ge 1-\delta$ for an unseen data-point $(y^{(0)}, v^{(0)})$ that is exchangeable with $\mathcal{D}$ (Lindemann et al., 2024)."),
    heading("p0004-b006", B(P, "p0004-b006"), "## 4. Problem Statement"),
    text("p0004-b007", [89.0, 668.0, 523.0, 716.0],
         r"We are given black-box access to $f$ (1a), i.e., we do not know its analytical form and its output can only be estimated via data. We are a planner $P: \mathcal{X} \rightarrow \mathcal{X}^{T+1} \times \mathcal{U}^T$ that generates open-loop reference trajectories $(x^\textrm{ref}_{0:T}, u^\textrm{ref}_{0:T-1})$ that satisfy (1a), starting from an initial condition $x_0^\textrm{ref} \in \mathcal{X}_0 \ominus \mathcal{B}_\epsilon(0)$"),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 4, a 250 dpi crop of Proposition 1 and the reachable-set paragraph, and with
preliminary.tex/problem_statement.tex (macros expanded: \infKoop = \mathcal{K}, \enc = \phi, \dec = \psi, \ka = K_{A},
\kb = K_{B}, \stateSpace = \mathcal{X}). The extractor text was glyph soup with <sup>, underline and strikethrough
markers; all mathematics rewritten from the TeX source and checked on the render. First item: continuation of the
'Koopman Operators' paragraph of page 3; the formula split by the page break ('... K phi^infinity(x) =' / 'phi^infinity
o f(x)') is kept whole on page 3, so this item starts with 'according to ...' and is joined with join_previous 'space'.
Source slip kept as printed: the lifting function is called '$g$' in 'with the lifting function $g$ parameterized
using polynomials or NNs', while it is $\phi$ everywhere else. 'infinite-/dimensional' and 'closed-/loop' at line ends
are real compounds (restored); 'overapproxi-mation' closed up. Run-in bold titles 'Reachability via NN Verification
(NNV)' and 'Conformal Prediction (CP)' kept inside their text items; the en dash in 'computational graph (CG) – a
directed ...' as printed; 'auto_LiRPA' is printed in typewriter and written as a code span. Proposition 1: bold label
as printed 'Proposition 1 (CG Robustness (Xu et al., 2020))' with no trailing punctuation; the body is printed in
italics (not reproduced) and ends with '... and alpha, beta in R^{n_o}.' (end of the TeX proposition environment).
Source slip kept as printed: the exact reachable set is printed with an unmatched closing brace,
$\mathcal{X}_{0:T} \doteq \{\mathcal{X}_0, f(\mathcal{X}_t, \pi(\mathcal{X}_t,t)) \}_{t=0}^{T-1}\}$ (checked at 250
dpi; identical to the TeX). The CP paragraph: Quantile is upright text, the probability is blackboard P, R_{\ge 0}
blackboard R; citation '(Lindemann et al., 2024)'. Heading '4. Problem Statement' level 2. Source slip kept as
printed: 'We are a planner P : ...' (Section 4). The last sentence continues on page 5 ('... initial condition
x_0^ref in X_0 minus B_eps(0) / that is uniformly distributed ...'); the formula is complete on this page and page 5
continues with join_previous 'space'. Citations checked: (Shi et al., 2024), (Rober and How, 2024), (Zhang et al.,
2018), (Xu et al., 2020), (Althoff et al., 2021), (Lindemann et al., 2024). Omitted: running header 'NATH YIN CHOU'
and page number 4.
""")
