#!/usr/bin/env python3
from pagelib import write_page

NOTES = r"""
Compared with the 170 dpi render and four 250 dpi crops of PDF page 4 and with the TeX source. Reading
order: left column, then right column. All mathematics rewritten in LaTeX from main.tex with macros
expanded (\U, \X, \R, \K, \restr) and checked against the crops; TeX and PDF agree. The extractor's
formula images are now $$ blocks: (7), the concatenation u_[n] (unnumbered), (8), the contradiction
inequality (unnumbered), the lim inf display (unnumbered), (9), the definition of h-hat (unnumbered),
(11) and the two-line definition of delta-bar / delta-underbar (one unnumbered aligned block); display
(10) had been flattened into the preceding text item and is a $$ block with \tag{10}. The extractor
classified the heading 'IV. SAFETY ENFORCEMENT USING RECURRENCE' as a formula image; it is now a '##'
heading. The first four items are the remainder of Theorem 2 (items (i), 'Moreover, if ... then:',
(ii), 'In particular, ...'); the theorem ends with '... the set h_{>=0} is safe.' (TeX environment).
The enumerate labels '(i)', '(ii)' are written as plain text at the start of their paragraphs. Proof of
Theorem 2: label 'Proof.' (italic in the PDF) written in bold; the bold run-in titles '(i) Control
tau-recurrence of h_{>=0}.' and '(ii) Safety under h_{>=0} cap R_tau(X_u) = emptyset.' are bold; the
label and the first title are written as one bold run ('Proof. (i) Control ...') so that no '** **'
sequence appears; the end-of-proof box is written $\square$. Stars are written ^{\ast}. Theorem 3 (label 'Theorem 3
(Validity of Signed Distance Function as RCBF).') ends with the delta-underbar display (TeX
environment); it contains the sentence 'Precisely, for all ...' as a new printed paragraph. Definition
8 (label 'Definition 8 (Sector Containment).') ends with '... we say that h is sector contained.'.
Checked specifically on the crops: the hats on h, D_0, c, gamma, alpha, beta, tau in Theorem 3; the
bound on tau-hat is printed inline as max{log(a_2/a_1)/(alpha-hat - alpha), log(a_2/a_1)/(beta -
beta-hat)} + log(delta-bar/delta-underbar)/min{alpha-hat, beta-hat}; the overline and underline on the
two deltas agree with the TeX source (\overline{\delta}, \underline{\delta}); sup and inf are over x in
D_0. Kept as printed (not conversion errors): in (7) the control inside the arg max is u, not u_0; in
Theorem 3 'there exists u in U^{(0,tau]}' has tau without hat while the max in (11) is over (0,
tau-hat]; 'lim inf' is typeset as \lim\inf with the subscript under inf and an upright d, while the
following text defines d(S,x) in italics; 'sign distance function'; 'The proposed approach reduced';
'which we refer here as a cell'. Citations [9, Lemma 1], [10], [10, Theorem 11] read from the page.
Line-wrap hyphens removed (properties, trajectories); 'non-control' (broken at the line end) is a real
hyphen in the TeX source; 'sub-class' is printed with a hyphen.
"""

SD_DELTA = r"""$$
\begin{aligned}
\overline{\delta} &:= \sup_{x \in D_0} \left(\mathrm{sd}(x,S) - \mathrm{sd}(x,h_{\geq 0})\right),\\
\underline{\delta} &:= \inf_{x \in D_0} \left(\mathrm{sd}(x,S) - \mathrm{sd}(x,h_{\geq 0})\right).
\end{aligned}
$$"""

write_page(4, NOTES, [
    ("p0004-b000", "text", ("p0004-b000",),
     r"(i) The superlevel set $h_{\ge 0}$ is control $\tau$-recurrent, i.e., for any $x \in h_{\ge 0}$ there exists $u \in \mathcal{U}$ such that the trajectory $\phi(t,x,u)$ always returns to $h_{\ge 0}$ within time $\tau$.", {}),
    ("p0004-b001", "text", ("p0004-b001",),
     r"Moreover, if $h_{\ge 0} \cap \mathcal{R}_\tau(\mathcal{X}_u)=\emptyset$, then:", {}),
    ("p0004-b002", "text", ("p0004-b002",),
     r"(ii) For any $x \in h_{\ge 0}$, every $u \in \mathcal{U}$ that renders $\phi(t,x,u)$ $\tau$-recurrent also ensures that $\phi(t,x,u)\notin \mathcal{X}_u$ for all $t\geq0$.", {}),
    ("p0004-b003", "text", ("p0004-b003",),
     r"In particular, under the condition $h_{\ge 0} \cap \mathcal{R}_\tau(\mathcal{X}_u)=\emptyset$, the set $h_{\ge 0}$ is safe.", {}),
    ("p0004-b004", "text", ("p0004-b004",),
     r"**Proof. (i) Control $\tau$-recurrence of $h_{\ge 0}$.** Given $x\in h_{\ge 0}$, fix $x_0:=x$ and $t_0:=0$. By the RCBF condition (5), there exists $u_0\in\mathcal{U}^{(0,\tau]}$ and a time", {}),
    ("p0004-b005", "text", ("p0004-b005",),
     r"""$$
\tau_0 := \max\left\{ \arg\max_{t\in(0,\tau]}\ \ e^{\gamma(h(\phi(t,x_0,u)))\,t}\,h(\phi(t,x_0,u))\right\}, \tag{7}
$$""", {}),
    ("p0004-b006", "text", ("p0004-b006",),
     r"such that $x_1:=\phi(\tau_0,x_0,u_0)\in h_{\ge 0}$ and $t_1:=\tau_0+t_0$. Proceed inductively: given $x_n\in h_{\ge0}$ and $t_n$, use (5) to select $u_n\in\mathcal{U}^{(0,\tau]}$ and $\tau_n\in(0,\tau]$ as in (7), leading to $x_{n+1}:=\phi(\tau_{n},x_{n},u_{n})\in h_{\ge 0}$, and $t_{n+1}=\tau_n+t_n$.", {}),
    ("p0004-b007", "text", ("p0004-b007",),
     r"The desired control $u\in \mathcal{U}$ is thus defined by concatenating the restrictions of $u_n$ to the intervals $(0,\tau_n]$, i.e.,", {}),
    ("p0004-b008", "text", ("p0004-b008",),
     r"""$$
u_{[n]}=\left.u_0\right|_{(0,\tau_0]}\left.u_1\right|_{(0,\tau_1]}\dots\left.u_n\right|_{(0,\tau_n]} \in \mathcal{U}^{(0,t_n]}
$$""", {}),
    ("p0004-b009", "text", ("p0004-b009",),
     r"and letting $u=\lim_{n\to\infty}u_{[n]}\in \mathcal{U}^{(0,t^{\ast}]}$, where $t^{\ast}=\lim_{n\rightarrow\infty} t_n$. An argument similar to [9, Lemma 1] shows that $t^{\ast}=\infty$. Moreover, it follows from the construction that for all $n\ge0$,", {}),
    ("p0004-b010", "text", ("p0004-b010",),
     r"""$$
x_{n+1} =\phi(\tau_n,x_n,\left.u_n\right|_{(0,\tau_n]}) = \phi(t_n,x,u), \tag{8}
$$""", {}),
    ("p0004-b011", "text", ("p0004-b011",),
     r"and therefore $\phi(t_n,x,u)\in h_{\ge0}$. It follows then from the fact that for all $n\geq0$, $x_n\in h_{\ge0}$, $t_{n+1}-t_n\in(0,\tau]$ and $t_n\to \infty$, that the trajectory $\phi(t,x,u)$ is $\tau$-recurrent w.r.t. $h_{\ge0}$. Since $x\in h_{\ge0}$ was chosen arbitrarily, $(i)$ follows.", {}),
    ("p0004-b012", "text", ("p0004-b012",),
     r"**(ii) Safety under $h_{\ge 0}\cap \mathcal{R}_\tau(\mathcal{X}_u)=\emptyset$.** Assume $h_{\ge 0}\cap \mathcal{R}_\tau(\mathcal{X}_u)=\emptyset$. Take any $x\in h_{\ge 0}$ and any control $u\in\mathcal{U}$ that renders $\phi(t,x,u)$ $\tau$-recurrent w.r.t. $h_{\ge0}$. Suppose, towards a contradiction, that the trajectory is unsafe: there exists $t' > 0$ with $\phi(t',x,u)\in\mathcal{X}_u$. Since $h(x)\ge 0$ and $h < 0$ on $\mathcal{X}_u$, by continuity there exists a *last exit time* $t''\in[0,t']$ with $h(\phi(t'',x,u))=0$ and $h(\phi(t,x,u)) < 0$ for all $t\in(t'',t']$. Because $h_{\ge 0}\cap \mathcal{R}_\tau(\mathcal{X}_u)=\emptyset$, the state $\phi(t'',x,u)$ cannot reach $\mathcal{X}_u$ within time $\tau$, hence $t'-t'' > \tau$ and", {}),
    ("p0004-b013", "text", ("p0004-b013",),
     r"""$$
h\big(\phi(t''+t,x,u)\big) < 0\qquad\forall\,t\in(0,\tau],
$$""", {}),
    ("p0004-b014", "text", ("p0004-b014",),
     r"which contradicts with the fact that $u$ renders $\phi(t,x,u)$ $\tau$-recurrent w.r.t. $h_{\ge0}$. $\square$", {}),
    ("p0004-b015", "text", ("p0004-b015",),
     r"Besides ensuring safety, RCBFs also share similar properties like standard CBFs. In particular, it is possible to show that whenever $x\in D_0\backslash h_{\ge0}$, there is always some $u\in\mathcal{U}$ such that", {}),
    ("p0004-b016", "text", ("p0004-b016",),
     r"""$$
\lim\inf_{t\rightarrow\infty} \mathrm{d}(h_{\geq0},\phi(t,x,u))=0,
$$""", {}),
    ("p0004-b017", "text", ("p0004-b017",),
     r"with $d(S,x):=\min_{y\in S}\|y-x\|$, thus ensuring that trajectories come back to $h_{\geq0}$ under simplified condition. We do not make these claims formal here, and refer the reader to [10] for similar arguments.", {}),
    ("p0004-b018", "heading", ("p0004-b018",), "### C. Signed Distance Function: a Valid RCBF", {}),
    ("p0004-b019", "text", ("p0004-b019",),
     r"In this section, we present a striking result. The existence of a CBF $h$ satisfying some regularity conditions is sufficient for synthesizing a simple sign distance function that satisfies our RCBF condition. Firstly, we require $h$ to be sector contained.", {}),
    ("p0004-b020", "text", ("p0004-b020",),
     r"**Definition 8 (Sector Containment).** Let $h: D\subseteq \mathbb{R}^n \rightarrow \mathbb{R}$ be continuous. If $\exists a_1, a_2 > 0$ such that", {}),
    ("p0004-b021", "text", ("p0004-b021",),
     r"""$$
(h(x) - a_{1}\mathrm{sd}(x, h_{\leq 0}))(h(x) - a_{2}\mathrm{sd}(x, h_{\leq 0})) \leq 0 \tag{9}
$$""", {}),
    ("p0004-b022", "text", ("p0004-b022",),
     r"for all $x \in D$, we say that $h$ is sector contained.", {}),
    ("p0004-b023a", "text", [313.0, 205.0, 559.0, 239.0],
     r"The second condition refers to the particular choice of extended class $\mathcal{K}$ function. In particular, we will consider the sub-class:", {}),
    ("p0004-b023b", "text", [313.0, 240.0, 564.0, 253.0],
     r"""$$
\kappa_{\alpha,\beta}(s):= \gamma_{\alpha,\beta}(s)\, s. \tag{10}
$$""", {}),
    ("p0004-b024", "text", ("p0004-b024",),
     r"**Theorem 3 (Validity of Signed Distance Function as RCBF).** Let $h$ be a CBF satisfying (2) and (9) over $D_0:=h_{\geq -c}$ with parameters $c > 0$ and $a_2 > a_1 > 0$, and extended class $\mathcal{K}$ function $\kappa_{\alpha,\beta}$ as in (10), with parameters $\alpha > 0$ and $\beta > 0$. Then, for any closed set $S$ satisfying $h_{\geq 0} \subseteq S \subseteq h_{\geq -c}$, with $\partial S\cap h_{=0}=\emptyset$, the function", {}),
    ("p0004-b025", "text", ("p0004-b025",),
     r"""$$
\hat{h}(\cdot) = - \mathrm{sd}(\cdot, S)
$$""", {}),
    ("p0004-b026", "text", ("p0004-b026", "p0004-b027"),
     r"is an RCBF over $\hat D_0:=\hat h_{\geq -\hat c}$ where $\hat c\geq 0$ is the largest constant satisfying $\hat h_{\geq -\hat c} \subseteq h_{\geq -c}$.", {}),
    ("p0004-b028", "text", ("p0004-b028",),
     r"Precisely, for all $x\in \hat h_{\geq-\hat c}$, there exists $u\in\mathcal{U}^{(0,\tau]}$ s.t.", {}),
    ("p0004-b029", "text", ("p0004-b029",),
     r"""$$
\max\limits_{ t\in (0,\hat\tau]} e^{\hat \gamma( \hat h(\phi(t,x,u)))t} \hat h(\phi(t,x,u)) \geq \hat{h}(x) \tag{11}
$$""", {}),
    ("p0004-b030", "text", ("p0004-b030",),
     r"where $\hat\gamma:=\gamma_{\hat\alpha,\hat\beta}$, with $\hat{\alpha}, \hat{\beta} > 0$ satisfying $\hat{\alpha} > \alpha, \hat{\beta} < \beta$, and $\hat{\tau} \geq \max\{\frac{\mathrm{log}(a_2/a_1)}{\hat{\alpha} - \alpha}, \frac{\mathrm{log}(a_2/a_1)}{\beta - \hat{\beta}}\} + \frac{\log (\overline{\delta}/\underline{\delta})}{\min \{\hat{\alpha}, \hat{\beta}\}}$ where", {}),
    ("p0004-b031", "text", ("p0004-b031", "p0004-b032"), SD_DELTA, {}),
    ("p0004-b033", "text", ("p0004-b033",),
     r"**Proof.** The proof follows closely similar results for the non-control case [10, Theorem 11] and it is omitted due to space constraints. $\square$", {}),
    ("p0004-b034", "heading", ("p0004-b034",), "## IV. Safety Enforcement Using Recurrence", {}),
    ("p0004-b035", "text", ("p0004-b035",),
     "In this section, we aim to develop robust conditions that leverage trajectory samples to certify the satisfaction of the RCBF condition on a neighborhood of the trajectory. The proposed approach reduced the problem of checking the RCBF condition on uncountably many points, to checking it on finitely many states, possibly in parallel.", {}),
    ("p0004-b036", "heading", ("p0004-b036",), "### A. Verification of a Cell", {}),
    ("p0004-b037", "text", ("p0004-b037",),
     r"To proceed, we first analyze how trajectories deviate from one another. This step lays the foundation for constructing a stronger verification criterion that ensures local safety in a neighborhood $\mathcal{B}_{r}(x)$ of each sampled point $x$, which we refer here as a cell.", {}),
])
