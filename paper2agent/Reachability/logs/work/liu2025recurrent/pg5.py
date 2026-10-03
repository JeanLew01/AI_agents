#!/usr/bin/env python3
from pagelib import write_page

NOTES = r"""
Compared with the 170 dpi render and four 260 dpi crops of PDF page 5 and with the TeX source (the
proofs of Theorems 4 and 5 are in the branch of \ifthenelse{\boolean{arxiv}} that is compiled, since
edits.tex sets the flag to false). Reading order: left column, then right column; Theorem 5 starts at
the bottom of the left column (up to (16)) and continues at the top of the right column. All
mathematics rewritten in LaTeX from main.tex with macros expanded and checked symbol by symbol on the
crops; TeX and PDF agree. The 17 extractor formula images and the displays it had flattened into text
are now $$ blocks; printed numbers (12)-(20) are \tag{12}...\tag{20}, one block per number; the
unnumbered multi-line derivations in the two proofs are single aligned blocks (alignment only, no
content change). Stars are written ^{\ast}. Labels as printed, in bold: 'Lemma 1.', 'Theorem 4.',
'Theorem 5.' (no names), 'Proof.' (italic in the PDF). Bodies are italic in the PDF (not reproduced).
Statement ends from the TeX environments: Lemma 1 ends with '... on the x variable.'; Theorem 4 ends
with item (ii) '... then B_r(x) subseteq R_tau(X_u)' (no final period printed); Theorem 5 ends with
display (20). Item labels '(i)', '(ii)' are plain text at the start of their paragraphs. End-of-proof
boxes written $\square$ (the one of the proof of Theorem 4 is printed alone on its own line below the
last display and is its own item). Items the extractor had merged were split (display (12) / 'where L
is ...'; 'for some r > 0, then ... = emptyset,' / '(ii) Conversely ...'; proof display / 'for all t ...
Hence,'; 'Theorem 5. ...' / '(i) Let'; 'and assume that ...' / displays (16) and (19)); the line 'for
some r > 0, then B_r(x) subseteq R_tau(X_u)', extracted as a formula image, is text. Kept exactly as
printed, although they look like slips of the authors (not conversion errors): in the proof of Theorem
4 (i) the term is 'r e^{-Lt}' with a minus sign in the exponent while (13) has r e^{Lt}; 't* < tau' in
proof (ii); the last display of that proof has an italic 'R_{t*}(X_u)' (not calligraphic, subscript
t*); Theorem 5 (ii) reads 'assume that forall u ... s.t. the following holds'; in (17) and in the
proof of Theorem 5 the expressions 'h(y,u,t)', 'h(y,u*,t*)' appear although h is a function of the
state only; in (17) the exponent is gamma(h(y,u,t)) t while (20) has gamma(h(phi(t,y,u))) t; in the
first display chain of proof (i) the max is over 'u in U, t in (0,tau]' (U without superscript) and
the third line has u, not u*; 'be the time that maximizes' (for t* and u*); the proof text cites 'the
conditions of (17)' in part (i) and 'the conditions of (19)' in part (ii). Line-wrap hyphen removed
(definition); 'left-hand' is a printed hyphen.
"""

write_page(5, NOTES, [
    ("p0005-b000", "text", ("p0005-b000",),
     r"**Lemma 1.** Suppose that two trajectories $\phi(t, x, u)$, $\phi(t,y, u)$ starts from $x$ and $y$ respectively and share the same control input $u$ all the times, where $\|x - y\| \leq r$. Then we have:", {}),
    ("p0005-b001a", "text", [53.0, 93.0, 304.0, 110.0],
     r"""$$
|\mathrm{sd}(\phi(t, y, u), S) - \mathrm{sd}(\phi(t, x, u), S) | \leq re^{Lt}, \forall t\geq0, \tag{12}
$$""", {}),
    ("p0005-b001b", "text", [53.0, 112.0, 299.0, 136.0],
     r"where $L$ is a uniform bound on the Lipschitz constant of (1) on the $x$ variable.", {}),
    ("p0005-b002", "text", ("p0005-b002",), r"**Proof.** See Appendix A. $\square$", {}),
    ("p0005-b003", "text", ("p0005-b003",),
     r"We leverage Lemma 1 to verify different properties of a given cell $\mathcal{B}_r(\cdot)$. In particular, Theorem 4 below gives us a condition that verifies whether a cell $\mathcal{B}_{r}(x)$ is completely inside $\mathcal{R}_{\tau}(\mathcal{X}_{u})$, completely outside $\mathcal{R}_{\tau}(\mathcal{X}_{u})$, or partially inside $\mathcal{R}_{\tau}(\mathcal{X}_{u})$. This will be critical to over approximate $\mathcal{R}_\tau(\mathcal{X}_u)$.", {}),
    ("p0005-b004", "text", ("p0005-b004",),
     r"**Theorem 4.** Consider a state $x \in \mathcal{X}$, and let $\mathcal{B}_{r}(x) :=\{y | \|y-x\| \leq r\}$ be a neighborhood of $x$. Then, we have:", {}),
    ("p0005-b005", "text", ("p0005-b005",),
     r"(i) Given $x\in \mathcal{X}$, if there exists $u\in \mathcal{U}^{(0,\tau]}$ s.t.", {}),
    ("p0005-b006", "text", ("p0005-b006",),
     r"""$$
\forall t \in [0,\tau],\;\mathrm{sd}(\phi(t, x, u), \mathcal{X}_{u}) > re^{Lt}, \tag{13}
$$""", {}),
    ("p0005-b007a", "text", [56.0, 301.0, 264.0, 311.5],
     r"for some $r > 0$, then $\mathcal{B}_{r}(x) \cap \mathcal{R}_{\tau}(\mathcal{X}_{u}) = \emptyset$,", {}),
    ("p0005-b007b", "text", [56.0, 312.0, 264.0, 323.0],
     r"(ii) Conversely, given $x\in\mathcal{X}$, if for all $u \in \mathcal{U}^{(0,\tau]}$,", {}),
    ("p0005-b008", "text", ("p0005-b008",),
     r"""$$
\exists t\in (0,\tau], \text{ s.t. } \mathrm{sd}(\phi(t, x, u), \mathcal{X}_{u}) < -r e^{Lt}, \tag{14}
$$""", {}),
    ("p0005-b009", "text", ("p0005-b009",),
     r"for some $r > 0$, then $\mathcal{B}_{r}(x) \subseteq \mathcal{R}_{\tau}(\mathcal{X}_{u})$", {}),
    ("p0005-b010", "text", ("p0005-b010",),
     "**Proof.** *(i)* If the initial states satisfy the condition (13), then by Lemma 1, we have:", {}),
    ("p0005-b011a", "text", [53.0, 397.0, 299.0, 412.0],
     r"""$$
\mathrm{sd}(\phi(t, y, u), \mathcal{X}_{u}) \geq \mathrm{sd}(\phi(t, x, u), \mathcal{X}_{u})-re^{-Lt} > 0,
$$""", {}),
    ("p0005-b011b", "text", [53.0, 414.0, 299.0, 428.0],
     r"for all $t \in [0,\tau]$ and all $y \in \mathcal{B}_{r}(x)$. Hence,", {}),
    ("p0005-b012", "text", ("p0005-b012",),
     r"""$$
\mathcal{B}_{r}(x) \cap \mathcal{R}_{\tau}(\mathcal{X}_{u}) = \emptyset.
$$""", {}),
    ("p0005-b013", "text", ("p0005-b013",),
     r"*(ii)* If instead the initial states satisfy the condition (14), let $t^{\ast} < \tau$ be the time at which", {}),
    ("p0005-b014", "text", ("p0005-b014",),
     r"""$$
\mathrm{sd}(\phi(t^{\ast}, x, u), \mathcal{X}_{u}) < -re^{Lt^{\ast}}.
$$""", {}),
    ("p0005-b015", "text", ("p0005-b015",), "Again, by Lemma 1, we have:", {}),
    ("p0005-b016", "text", ("p0005-b016",),
     r"""$$
\mathrm{sd}(\phi(t^{\ast}, y, u), \mathcal{X}_{u}) \le \mathrm{sd}(\phi(t^{\ast}, x, u), \mathcal{X}_{u})+re^{Lt^{\ast}} < 0,
$$""", {}),
    ("p0005-b017", "text", ("p0005-b017",),
     r"for all $y \in \mathcal{B}_{r}(x)$. Consequently,", {}),
    ("p0005-b018", "text", ("p0005-b018",),
     r"""$$
\mathcal{B}_{r}(x) \subseteq R_{t^{\ast}}(\mathcal{X}_{u}).
$$""", {}),
    ("p0005-qed4", "text", [287.0, 571.0, 300.0, 586.0], r"$\square$", {}),
    ("p0005-b019", "text", ("p0005-b019",),
     "The following theorem verifies whether the states of a cell all satisfy the RCBF condition (5) or all such states are guaranteed not to satisfy such a condition.", {}),
    ("p0005-b020a", "text", [54.0, 633.0, 299.0, 656.0],
     r"**Theorem 5.** Given a closed set $S$, a candidate RCBF $h(\cdot) := - \mathrm{sd}(\cdot, S)$, and function $\gamma:=\gamma_{\alpha,\beta}$, with $\alpha,\beta > 0$.", {}),
    ("p0005-b020b", "text", [54.0, 657.0, 299.0, 668.0], "(i) Let", {}),
    ("p0005-b021", "text", ("p0005-b021",),
     r"""$$
\hat{h}_{r}^{-}(x,u,t) := h(\phi(t, x, u)) - re^{Lt} \tag{15}
$$""", {}),
    ("p0005-b022a", "text", [68.0, 689.0, 299.0, 703.0],
     r"and assume that $\exists u\in\mathcal{U}^{(0,\tau]}$ s.t. the following holds", {}),
    ("p0005-b022b", "text", [68.0, 704.0, 304.0, 736.0],
     r"""$$
\max\limits_{ t \in (0,\tau]} e^{\gamma(\hat h_r^-(x,u,t)) t}\, \hat{h}_{r}^{-}(x, u, t)\geq h(x) + r, \tag{16}
$$""", {}),
    ("p0005-b023", "text", ("p0005-b023",),
     r"for some $r > 0$. Then for all $y \in \mathcal{B}_{r}(x)$, the RCBF condition is satisfied, i.e.,", {}),
    ("p0005-b024", "text", ("p0005-b024",),
     r"""$$
\max\limits_{t \in (0,\tau]} e^{\gamma(h(y, u, t)) t} h(\phi(t, y, u)) \geq h(y), \tag{17}
$$""", {}),
    ("p0005-b025", "text", ("p0005-b025",), "(ii) Let", {}),
    ("p0005-b026", "text", ("p0005-b026",),
     r"""$$
\hat{h}_{r}^{+}(x,u,t) := h(\phi(t, x, u)) + re^{Lt} \tag{18}
$$""", {}),
    ("p0005-b027a", "text", [328.0, 137.0, 559.0, 152.0],
     r"and assume that $\forall u\in\mathcal{U}^{(0,\tau]}$ s.t. the following holds", {}),
    ("p0005-b027b", "text", [328.0, 153.0, 564.0, 184.0],
     r"""$$
\max\limits_{ t \in (0,\tau]} e^{\gamma(\hat h_r^+(x,u,t)) t}\, \hat{h}_{r}^{+}(x, u, t) < h(x) - r \tag{19}
$$""", {}),
    ("p0005-b028", "text", ("p0005-b028",),
     r"for some $r > 0$. Then, for all $y \in \mathcal{B}_{r}(x)$, the RCBF condition is not satisfied, i.e.,", {}),
    ("p0005-b029", "text", ("p0005-b029",),
     r"""$$
\max_{t \in (0, \tau]} e^{\gamma(h(\phi(t,y,u))) t} h(\phi(t, y, u)) < h(y). \tag{20}
$$""", {}),
    ("p0005-b030", "text", ("p0005-b030",),
     r"**Proof.** (i) Let $t^{\ast}$ and $u^{\ast}$ be the time that maximizes the left-hand side of (16), i.e.", {}),
    ("p0005-b031", "text", ("p0005-b031",),
     r"""$$
\begin{aligned}
t^{\ast} &= \arg\max_{t\in(0,\tau]} \max\limits_{u \in \mathcal{U}^{(0,\tau]}} e^{\gamma(\hat h_r^-(x,u,t)) t}\, \hat{h}_{r}^{-}(x, u, t),\\
u^{\ast} &= \arg\max_{u\in \mathcal{U}^{(0,\tau]}} \max\limits_{t \in (0,\tau]} e^{\gamma(\hat h_r^-(x,u,t)) t}\, \hat{h}_{r}^{-}(x, u, t).
\end{aligned}
$$""", {}),
    ("p0005-b032", "text", ("p0005-b032",),
     r"At this maximizing time $t^{\ast} \in (0,\tau]$, it follows that", {}),
    ("p0005-b033", "text", ("p0005-b033",),
     r"""$$
\begin{aligned}
& \max\limits_{u \in \mathcal{U}, t \in (0,\tau]} e^{\gamma(h(y, u, t)) t} h(\phi(t, y, u))\\
\geq& e^{\gamma(h(y,u^{\ast},t^{\ast})) t^{\ast}}\, h(y, u^{\ast}, t^{\ast}) \\
\geq & e^{\gamma(\hat h_r^-(x,u,t^{\ast})) t^{\ast}}\, \hat h_{r}^{-}(x, u, t^{\ast}) \\
\geq & h(x)+r \\
\geq & h(y),
\end{aligned}
$$""", {}),
    ("p0005-b034", "text", ("p0005-b034",),
     "where the first inequality follows from the definition of maximum, the second and fourth inequalities are derived from Lemma 1 and the third inequality is derived from the conditions of (17).", {}),
    ("p0005-b035", "text", ("p0005-b035",),
     r"(ii) Let $t^{\ast}$ and $u^{\ast}$ be the time and control signal that maximize the left-hand side of (20), i.e.", {}),
    ("p0005-b036", "text", ("p0005-b036",),
     r"""$$
\begin{aligned}
t^{\ast} &= \arg\max_{t\in(0,\tau]}\max_{u \in \mathcal{U}^{(0,\tau]}} e^{\gamma(h(y,u,t)) t}\,h(y, u, t),\\
u^{\ast} &= \arg\max_{u\in\mathcal{U}^{(0,\tau]}}\max_{t \in (0,\tau]}e^{\gamma(h(y,u,t)) t}\,h(y, u, t).
\end{aligned}
$$""", {}),
    ("p0005-b037", "text", ("p0005-b037",),
     r"Again, at this maximizing time $t^{\ast} \in (0,\tau]$, we get", {}),
    ("p0005-b038", "text", ("p0005-b038",),
     r"""$$
\begin{aligned}
& \max_{u \in \mathcal{U}^{(0,\tau]}, t \in (0, \tau]} e^{\gamma(h(y, u, t)) t} h(y, u, t)\\
\le & e^{\gamma(\hat h_r^+(x, u^{\ast}, t^{\ast})) t^{\ast}} \hat h_r^+(x, u^{\ast}, t^{\ast}) \\
\leq & \max\limits_{u \in \mathcal{U}^{(0,\tau]}, t \in (0,\tau]} e^{\gamma(\hat h_r^+(x,u,t)) t}\, \hat{h}_{r}^{+}(x, u, t)\\
< & h(x)-r\\
< & h(y),
\end{aligned}
$$""", {}),
    ("p0005-b039", "text", ("p0005-b039",),
     r"where the second inequality is derived from the definition of the maximum, the first and fourth inequalities are derived from Lemma 1, and the third inequality is derived from the conditions of (19). $\square$", {}),
])
