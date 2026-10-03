from pagelib import *

G = r"g^{\ast}_{N,k}"

items = [
    header(14),
    heading("p0014-b001", [89.0, 93.0, 315.0, 105.0], "## Appendix A. Robust Scenario-Based Proofs"),
    text("p0014-b002", [89.0, 115.0, 523.0, 139.0],
         "First, we introduce and prove the following lemma regarding a generic 1-dimensional chance-constrained optimization problem (CCP), which will be useful for subsequent proofs."),
    text("p0014-b003", [89.0, 148.0, 504.0, 159.0],
         "**Lemma 7 (Solution Feasibility for a 1-D CCP)** Consider the following 1-dimensional CCP:"),
    text("p0014-b004", [223.0, 163.0, 528.0, 213.0],
         display(r"""\begin{aligned}
\text{CCP}_\epsilon: &\min_{g\in \mathbb{R}}{g} \\
&\text{s.t. } \underset{h \in H}{\mathbb{P}} \left( f(h) \le g \right) \ge 1-\epsilon
\end{aligned}""", 7)),
    text("p0014-b005", [90.0, 216.0, 522.0, 241.0],
         r"where $g$ is the 1-dimensional optimization variable, $h$ is the uncertain parameter that describes different instances of an uncertain optimization scenario, and $f$ is some function of $h$."),
    text("p0014-b006", [106.0, 244.0, 367.0, 254.0],
         "The corresponding sample counterpart (SP) of this CCP is:"),
    text("p0014-b007", [176.0, 257.0, 528.0, 304.0],
         display(r"""\begin{aligned}
\text{SP}^A_{N,k}: &\min_{g \in \mathbb{R}}{g} \\
&\text{s.t. } f(h_i) \le g, \quad i \in \{1, ..., N\}-A\{h_1, ..., h_N\}
\end{aligned}""", 8)),
    text("p0014-b008", [90.0, 308.0, 522.0, 346.0],
         r"where $N$ constraints are sampled but $k$ constraints are discarded according to some constraint elimination algorithm $A$. Let $" + G + r"$ denote the solution to the above SP. Select a violation parameter $\epsilon \in (0, 1)$ and a confidence parameter $\beta \in (0, 1)$ such that"),
    text("p0014-b009", [240.0, 350.0, 528.0, 393.0], display(BINOM, 9)),
    text("p0014-b010", [90.0, 397.0, 343.0, 408.0],
         r"Then, with probability at least $1-\beta$, the following holds:"),
    text("p0014-b011", [248.0, 410.0, 528.0, 438.0],
         display(r"\underset{h \in H}{\mathbb{P}} \left( f(h) > " + G + r" \right) \le \epsilon", 10)),
    text("p0014-b012", [90.0, 442.0, 523.0, 521.0],
         r"**Proof** Lemma 7 is a straightforward application of a scenario-based sampling-and-discarding approach to a CCP as detailed in Campi and Garatti (2011). CCP (7) satisfies the assumptions of Campi and Garatti (2011), since both the domain of optimization $\mathbb{R}$ and the constraint sets parameterized by $h$, $\{g: f(h) \le g\}$, are convex and closed in $g$. Thus, Lemma 7 follows as a special case of Theorem 2.1 in Campi and Garatti (2011), where $d=1$, $c=1$, $x=g$, $X=G=\mathbb{R}$, $\delta=h$, $\Delta=H$, and $X_\delta=G_h=\{g: f(h) \le g\}$. $\blacksquare$"),
    heading("p0014-b013", [90.0, 547.0, 206.0, 556.0], "### A.1. Proof of Theorem 2"),
    text("p0014-b014", [89.0, 566.0, 523.0, 694.0],
         r"**Proof** Consider the chance-constrained optimization problem (CCP) (7) in Lemma 7 directly above, where $h=x$, $H=\mathcal{S}$, and $f(h)=f(x)=-" + J + r"(x,0)$. The proposed robust scenario-based probabilistic safety verification method deals with the corresponding sample counterpart (SP) (8) in Lemma 7 where the constraint elimination algorithm $A$ is to remove all $k$ constraints $f(h_i) \le g$ where $f(h_i)=-" + J + r"(x_i,0) \ge 0$. Thus, the only constraints remaining are $f(h_i) \le g$ where $f(h_i) < 0$. Since we are minimizing $g$, the solution $" + G + r"$ to the SP must be $< 0$; i.e., $0 < -" + G + r"$. Therefore, $" + PS + r" ( " + J + r"(x,0) \le 0 ) \le " + PS + r" ( " + J + r"(x,0) < -" + G + r" )$. Equation (10) of Lemma 7 then yields: $" + PS + r" ( " + J + r"(x,0) < -" + G + r" ) \le \epsilon \implies " + PS + r" ( " + J + r"(x,0) \le 0 ) \le \epsilon$, where $\forall (x,t), " + J + r"(x,t) \le V(x, t)$ from Equation (1), so Equation (3) of Theorem 2 directly follows. $\blacksquare$"),
    pageno(14, "p0014-b015", [301.0, 726.0, 311.0, 733.0]),
]

save(14, items, r"""
Compared the whole page with the 130 dpi render, with 200-210 dpi crops of Lemma 7 and of the two proofs, and with
sections/scenario-based_appendix.tex. All mathematics was rewritten in LaTeX from the TeX source and checked symbol by
symbol on the crops; TeX and PDF agree. The four extractor 'formula' images were replaced by $$ blocks with the printed
numbers \tag{7} (CCP_eps: min over g in R of g, subject to P_{h in H}(f(h) <= g) >= 1 - eps), \tag{8} (SP^A_{N,k}: min
over g in R of g, subject to f(h_i) <= g for i in {1, ..., N} - A{h_1, ..., h_N}), \tag{9} (the binomial-tail condition,
identical to (2) and (5)) and \tag{10} (P_{h in H}(f(h) > g*_{N,k}) <= eps). (7) and (8) are two-line displays with one
printed number each and are written with an aligned environment inside one $$ block; the labels 'CCP' and 'SP' and
's.t.' are printed in italics because the lemma body is italic, and are written with \text{}. The star of g^*_{N,k} is
written g^{\ast}_{N,k} (a bare '^*' can pair up as Markdown emphasis); same printed symbol. 'Lemma 7 (Solution Feasibility
for a 1-D CCP)' is printed in bold without punctuation; the lemma body (italic) runs from 'Consider the following ...' to
display (10) (end of the lemma environment in the TeX source) and contains the indented sentence 'The corresponding sample
counterpart (SP) of this CCP is:' as its own paragraph. Both proofs start with a bold 'Proof' without punctuation and end
with a filled end-of-proof square, written as $\blacksquare$. Checked on the crop of the proof of Theorem 2: f(h) = f(x) =
-J_{\tilde{\pi}}(x,0); discarded constraints are those with f(h_i) = -J_{\tilde{\pi}}(x_i,0) >= 0; remaining ones have
f(h_i) < 0; 'must be < 0; i.e., 0 < -g*_{N,k}'; the two probability inequalities with '<= 0' and '< -g*_{N,k}'; the
implication arrow (\implies); and 'for all (x,t), J_{\tilde{\pi}}(x,t) <= V(x,t)'. Printed cross-references: Lemma 7,
CCP (7), SP (8), Equation (10), Equation (1), Equation (3), Theorem 2, 'Theorem 2.1 in Campi and Garatti (2011)'.
Headings: 'Appendix A.' is level 2, 'A.1.' is level 3 (the extractor had levels 1 and 2). Line-wrap hyphens removed
(ap-proach, parame-terized); real hyphens kept or restored ('chance-constrained' is broken at the line end after 'chance-'
and the extractor had 'chanceconstrained'; 1-dimensional, 1-D, scenario-based, sampling-and-discarding). Omitted: running
header and page number.
""")
