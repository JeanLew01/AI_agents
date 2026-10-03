#!/usr/bin/env python3
from pagelib import write_page

NOTES = r"""
Compared with the 170 dpi render and 250 dpi crops of PDF page 3 (left column upper/lower, right
column middle/lower, figure region at 200 dpi) and with the TeX source. Reading order: left column,
then right column; Figure 1 (top of the right column) and its caption are placed before the paragraph
'As Figure 1 shows ...', as printed. All mathematics rewritten in LaTeX from main.tex with macros
expanded and checked against the crops; TeX and PDF agree. The five extractor 'formula' images are now
$$ blocks with the printed numbers \tag{2}, \tag{3}, \tag{5}, \tag{6}; display (4), which the extractor
had flattened into text together with the last sentence of Definition 6, is a $$ block with \tag{4};
the controller-set display in Theorem 1 is unnumbered. Equation (6) is printed as a one-row cases
construct ('{ alpha, if s >= 0, and beta, if s < 0,') and is transcribed that way. Labels in bold with
the printed punctuation: 'Definition 4 (Extended Class K Function).', 'Definition 5 (Control Barrier
Function [2]).', 'Theorem 1 ( [2]).' (the PDF prints a space after the opening parenthesis; kept),
'Definition 6 (Control Recurrent Sets).', 'Definition 7 (Recurrent Control Barrier Function).',
'Theorem 2 (Safety Assessment via RCBFs).'. Bodies are italic in the PDF (not reproduced); the
bold-italic terms 'control recurrent', 'control tau-recurrent', 'Recurrent Control Barrier Function
(RCBF)' and the bold 'control recurrent sets' in the Section III lead paragraph are bold. Statement
ends from the TeX environments: Definition 5 ends with '... are first-order Lie derivatives.'; Theorem
1 ends with '... control invariant.'; Definition 6 ends with 'We refer to such phi(t,x,u) as a
(tau-)recurrent trajectory.'; Definition 7 ends with 'where the function gamma: R -> R_{>0}.'.
Theorem 2 begins at the bottom of the right column ('Let h be an RCBF as in Definition 7. Then:') and
its items (i), (ii) are on page 4. Figure 1: one crop containing both panels (a), (b) and the legend
('Recurrent set', 'A recurrent trajectory'); bbox edges checked on the 200 dpi crop; the legend and
panel letters exist only inside the raster image. Caption verbatim (printed prefix 'Fig. 1:'). The
paragraph after the figure is one printed paragraph ('... before returning [10]. Compared with the
invariant sets ...'). Extractor items that merged two paragraphs were split ('where alpha and beta ...
Section III-C.' / 'The following theorem describes ...'). Kept as printed: 'intial state' (typo),
'based on the Definition 6', 'infinite times', L_F h(x) written without argument u on the left-hand
side. Citations [2], [10]-[12], [14]-[18] read from the page. Line-wrap hyphens removed (trajectories,
Trajectories, particularly); 'first-order', 'Lipschitz-continuous', 'Sum-of-Squares' are printed hyphens.
"""

write_page(3, NOTES, [
    ("p0003-b000", "text", ("p0003-b000",),
     r"**Definition 4 (Extended Class $\mathcal{K}$ Function).** A function $\kappa: \mathbb{R} \to \mathbb{R}$ is an extended class $\mathcal{K}$ function if it is continuous, strictly increasing, and satisfies $\kappa(0) = 0$.", {}),
    ("p0003-b001", "text", ("p0003-b001",), "We are now ready to formally introduce CBFs.", {}),
    ("p0003-b002", "text", ("p0003-b002",),
     r"**Definition 5 (Control Barrier Function [2]).** A continuously differentiable function $h(x)$ is a CBF for the system (1) if there exists an extended class $\mathcal{K}$ function $\kappa$ such that,", {}),
    ("p0003-b003", "text", ("p0003-b003",),
     r"""$$
\max_{u \in U} L_{F} h(x) +\kappa(h(x)) \ge 0, \tag{2}
$$""", {}),
    ("p0003-b004", "text", ("p0003-b004",),
     r"for all $x \in \mathcal{X}$, and where $L_{F} h(x) = \frac{\partial h}{\partial x}^\top F(x,u)$, are first-order Lie derivatives.", {}),
    ("p0003-b005", "text", ("p0003-b005",),
     r"**Theorem 1 ( [2]).** An immediate consequence of Definition 5 is that any Lipschitz-continuous controller $k(x)$ satisfying", {}),
    ("p0003-b006", "text", ("p0003-b006",),
     r"""$$
k(x) \in \{ u\in U \mid L_{F}h(x) + \kappa(h(x)) \ge 0 \},
$$""", {}),
    ("p0003-b007", "text", ("p0003-b007",),
     r"renders the set $h_{\ge 0}:=\{x:h(x)\ge0\}$ invariant. Thus, $h_{\ge0}$ is, by definition, control invariant.", {}),
    ("p0003-b008", "text", ("p0003-b008",),
     r"Thus, if such a CBF $h$ exists and $h_{\ge 0} \cap \mathcal{X}_u = \emptyset$, all states in $h_{\ge 0}$ can find a control signal $u \in \mathcal{U}$, whose signal at any moment is in the set of $k(x)$. That is to say for any intial state $x \in h_{\ge 0}$, there exists $u \in \mathcal{U}$ such that $\phi(t,x,u) \in h_{\ge 0}, \forall t > 0,$ which means the states in $h_{\ge 0}$ are safe [2].", {}),
    ("p0003-b009", "text", ("p0003-b009",),
     "Sum-of-Squares (SOS) programming is widely used to synthesize/verify polynomial CBFs, but its cost grows rapidly with system dimension [14], [15], and polynomials may poorly capture complex safety sets. Neural network CBFs improve expressivity [16], [17], [18], yet their validity is harder to certify due to limited interpretability [18].", {}),
    ("p0003-b010", "heading", ("p0003-b010",), "## III. Recurrent Control Barrier Function", {}),
    ("p0003-b011", "text", ("p0003-b011",),
     r"The core idea behind ensuring safety using traditional CBFs is to construct a scalar function that makes $h_{\geq0}$ control invariant. Such sets can be as computationally expensive as a BRT, making CBF synthesis difficult. Leveraging recurrence, we show this explicit invariant set is unnecessary: valid RCBFs can be built from **control recurrent sets**, which relax invariance while keeping safety guarantees.", {}),
    ("p0003-b012", "heading", ("p0003-b012",), "### A. Control Recurrent Sets", {}),
    ("p0003-b013", "text", ("p0003-b013",),
     "In this section, we briefly cover the definition of recurrent sets in a control systems setting, which broadly allow trajectories to leave a set, provided they come back to it. The presentation follows [10], [11], [12], particularly [12].", {}),
    ("p0003-b014", "text", ("p0003-b014",),
     r"**Definition 6 (Control Recurrent Sets).** A compact set $S \subseteq \mathbb{R}^n$ is called **control recurrent** w.r.t. (1) if, for all $x \in S$, $\exists$ $u\in \mathcal{U}$, such that for any $t \geq 0$,", {}),
    ("p0003-b015", "text", ("p0003-b015",),
     r"""$$
\exists t' > t \;\; \mathrm{with} \;\; \phi(t', x, u) \in S. \tag{3}
$$""", {}),
    ("p0003-b016", "text", ("p0003-b016",),
     r"Likewise, a set $S \subseteq \mathbb{R}^n$ is called **control $\tau$-recurrent** ($\tau > 0$) w.r.t. (1) if, for all $x \in S$, $\exists$ $u\in \mathcal{U}$, such that for any $t \ge 0$,", {}),
    ("p0003-b017a", "text", [53.0, 702.0, 304.0, 718.0],
     r"""$$
\exists\, t' > t\,, \;\; \mathrm{with} \;\; t' - t \in (0, \tau]\,, \;\; \mathrm{and} \;\; \phi(t', x, u) \in S\,. \tag{4}
$$""", {}),
    ("p0003-b017b", "text", [53.0, 721.0, 299.0, 735.0],
     r"We refer to such $\phi(t,x,u)$ as a ($\tau$-)recurrent trajectory.", {}),
    ("p0003-b018", "figure", [316.0, 46.0, 556.0, 196.0], "", {"label": "Figure 1", "asset_name": "figure-1"}),
    ("p0003-b019", "caption", ("p0003-b019",), "Fig. 1: Illustration of Recurrent Sets and Recurrent Trajectories", {}),
    ("p0003-b020", "text", ("p0003-b020",),
     r"As Figure 1 shows, although a $\tau$-recurrent set is not necessarily invariant, it ensures that trajectories starting in $S$ will revisit it within at most $\tau$-time units infinite times. Notably, based on the Definition 6, an invariant set is always $\tau$-recurrent for any $\tau > 0$. Additionally, a 0-recurrent set is equivalent to an invariant set. Thus, Definition 6 generalizes invariance by allowing the trajectory $\phi(t, x, u)$ to leave the set $S$ before returning [10]. Compared with the invariant sets, recurrent sets show a more flexible shape; it does not need the region to be connected, and it does not require the system (1) to point inwards (or at least not outwards) on all the boundary $\partial S$.", {}),
    ("p0003-b021", "heading", ("p0003-b021",), "### B. Recurrent Control Barrier Function", {}),
    ("p0003-b022", "text", ("p0003-b022",),
     "We now move towards introducing the proposed Recurrent Control Barrier Functions. In fact, similar to [10], simply requiring trajectories to return to the set within a finite time, infinitely many times can guarantee the safety for the dynamical system.", {}),
    ("p0003-b023", "text", ("p0003-b023",),
     r"**Definition 7 (Recurrent Control Barrier Function).** Consider the control system (1). A continuous function $h: \mathbb{R}^{n} \rightarrow \mathbb{R}$ is a **Recurrent Control Barrier Function (RCBF)** if for all $x\in D_0 := h_{\ge-c}$, with $c > 0$, $\exists\, u \in \mathcal{U}^{(0,\tau]}$ s.t.", {}),
    ("p0003-b024", "text", ("p0003-b024",),
     r"""$$
\max\limits_{t\in (0,\tau]} e^{\gamma(h(\phi(t,x,u)))t} \,h(\phi(t,x,u)) \ge h(x), \tag{5}
$$""", {}),
    ("p0003-b025", "text", ("p0003-b025",),
     r"where the function $\gamma: \mathbb{R} \to \mathbb{R}_{>0}$.", {}),
    ("p0003-b026", "text", ("p0003-b026",),
     r"In (5) we follow the standard convention that when the $\sup$ is not achieved within the set $(0,\tau]$ the $\max$ is $-\infty$. Thus, for the $\max$ to be lower bounded, it implies that it is achieved within $(0,\tau]$. A particular choice of $\gamma$ that will be of use throughout this paper is", {}),
    ("p0003-b027", "text", ("p0003-b027",),
     r"""$$
\gamma_{\alpha,\beta}(s) = \begin{cases}
\alpha, \; \text{ if }s\geq0\,,\quad\text{and}\quad
\beta, \; \text{ if }s < 0\,,
\end{cases} \tag{6}
$$""", {}),
    ("p0003-b028a", "text", [313.0, 658.0, 559.0, 680.0],
     r"where $\alpha$ and $\beta$ are positive parameters. This will be particularly useful in our converse results in Section III-C.", {}),
    ("p0003-b028b", "text", [313.0, 682.0, 559.0, 704.0],
     "The following theorem describes how to use RCBFs to assess safety.", {}),
    ("p0003-b029", "text", ("p0003-b029",),
     r"**Theorem 2 (Safety Assessment via RCBFs).** Let $h$ be an RCBF as in Definition 7. Then:", {}),
])
