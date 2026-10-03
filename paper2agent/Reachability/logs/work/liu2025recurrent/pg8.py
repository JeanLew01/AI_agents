#!/usr/bin/env python3
from pagelib import write_page

NOTES = r"""
Compared with the 170 dpi render, a 220 dpi crop of the reference list and three 260 dpi crops of the
appendix (left column bottom, right column upper and lower halves), and with the TeX source and
main.bbl. Reading order: left column (references [8]-[20], 'APPENDIX', 'A. Proof of Lemma 1', start of
the proof with its first display), then right column (rest of the proof). The appendix is present in
this arXiv version (the 'arxiv' flag of edits.tex is false, so the full proofs are compiled).
References: one item per entry, list bullets of the extractor removed, italics kept, every one of the
13 entries read against the 220 dpi crop and the .bbl (authors, title, venue, month/year, pages).
Titles are printed in sentence case with lower-case proper names ('gpu-based', 'lyapunov',
'Barriernet', 'Hamilton-jacobi', 'jax'); kept. In [18] the page range is printed with thin spaces as
'11 532–11 539'; written with ordinary spaces. In [19] the title is printed 'Hj_reachability:' with an
underscore (the extractor produced strikethrough debris) and the URL is printed in typewriter type
with letter-spacing and a line break ('https : / / github . com / StanfordASL/hj_reachability'); it is
written closed up in backticks as https://github.com/StanfordASL/hj_reachability. In [20] 'ISBN' is
printed in small caps and '1.2.' is the edition/version field. Line-wrap hyphens removed (Conference
x2, functions, Computation, control, Transactions, barrier, reachability); real hyphens kept
(data-driven, safety-critical, recurrence-based, gpu-based, non-monotonic, Model-free, semi-algebraic,
input-constrained [broken at a line end; compound in the .bbl], Hamilton-jacobi). 'APPENDIX' is a '##'
heading and 'A. Proof of Lemma 1' a '###' heading. Appendix mathematics rewritten in LaTeX from
main.tex and checked on the 260 dpi crops; TeX and PDF agree. The six displays (none carries a printed
number) are aligned blocks inside $$; the extractor had kept five as images and flattened one line of
the first into text. Stars are written ^{\ast}. 'Proof.' (italic in the PDF) and 'Case 1', 'Case 2',
'Case 3' (bold in the PDF, followed by a colon in normal weight) are bold; the end-of-proof box is
$\square$. Kept exactly as printed, although they look like slips of the authors (not conversion
errors): the proof refers to a function g and to 'F(x,u) - F(x,v) = g(x)(u-v)' (control-affine form)
that the paper does not define; 'L_u = max ||g(phi(t,x,u))|| := max_{||v||=1, t} ||g(phi(t,x,u)) v|| >
0 exists'; the integral term has '||u(s) - u(s)||'; 'sd(phi(t,x,u), S)' with a calligraphic S in the
arg min definitions of x* and y* (italic S elsewhere); the bound variables of those arg min are x* and
y* themselves; in Case 3 the third line of the display ends with an unmatched extra '|'; the Case 2
display ends with a comma and is followed directly by Case 3; 'Gronwall' is printed with an umlaut
(Grönwall). Citation [20] read from the page.
"""

CASE12 = r"""$$
\begin{aligned}
 & |\mathrm{sd}(\phi(t,x,u),S) - \mathrm{sd}(\phi(t,y,u), S)| \\
 = & |\|\phi(t,x,u) - x^{\ast}\| - \|\phi(t,y,u)-y^{\ast}\||\\
\le & |\|\phi(t,x,u) - x^{\ast}\| - \|\phi(t,y,u)-x^{\ast}\||\\
\le & \|\phi(t,x,u) - \phi(t,y,u)\| \\
\le & r e^{Lt},
\end{aligned}
$$"""

write_page(8, NOTES, [
    ("p0008-b000", "text", ("p0008-b000",),
     "[8] J. Lee, J. Kim, and A. D. Ames, “A data-driven method for safety-critical control: Designing control barrier functions from state constraints,” in *2024 American Control Conference (ACC)*, IEEE, 2024, pp. 394–401.", {}),
    ("p0008-b001", "text", ("p0008-b001",),
     "[9] R. Siegelmann, Y. Shen, F. Paganini, and E. Mallada, “A recurrence-based direct method for stability analysis and gpu-based verification of non-monotonic lyapunov functions,” in *62nd IEEE Conference on Decision and Control (CDC)*, IEEE, Dec. 2023, pp. 6665–6672.", {}),
    ("p0008-b002", "text", ("p0008-b002",),
     "[10] Y. Shen, H. Sibai, and E. Mallada, “Generalized barrier functions: Integral conditions & recurrent relaxations,” in *60th Allerton Conference on Communication, Control, and Computing*, Sep. 2024, pp. 1–8.", {}),
    ("p0008-b003", "text", ("p0008-b003",),
     "[11] Y. Shen, M. Bichuch, and E. Mallada, “Model-free learning of regions of attraction via recurrent sets,” in *61st IEEE Conference on Decision and Control (CDC)*, Dec. 2022, pp. 4714–4719.", {}),
    ("p0008-b004", "text", ("p0008-b004",),
     "[12] H. Sibai and E. Mallada, “Recurrence of nonlinear control systems: Entropy and bit rates,” in *Proceedings of the 27th ACM International Conference on Hybrid Systems: Computation and Control (HSCC)*, ser. HSCC ’24, New York, NY, USA: Association for Computing Machinery, May 2024, pp. 1–9.", {}),
    ("p0008-b005", "text", ("p0008-b005",),
     "[13] H. Sibai and E. Mallada, “Recurrence of nonlinear control systems: Entropy, bit rates, and finite alphabets,” in *Nonlinear Analysis: Hybrid Systems*, Feb. 2025, pp. 1–16, submitted.", {}),
    ("p0008-b006", "text", ("p0008-b006",),
     "[14] A. Clark, “A semi-algebraic framework for verification and synthesis of control barrier functions,” *IEEE Transactions on Automatic Control*, 2024.", {}),
    ("p0008-b007", "text", ("p0008-b007",),
     "[15] S. Prajna and A. Jadbabaie, “Safety verification of hybrid systems using barrier certificates,” in *International Workshop on Hybrid Systems: Computation and Control*, Springer, 2004, pp. 477–492.", {}),
    ("p0008-b008", "text", ("p0008-b008",),
     "[16] W. Xiao et al., “Barriernet: Differentiable control barrier functions for learning of safe robot control,” *IEEE Transactions on Robotics*, vol. 39, no. 3, pp. 2289–2307, 2023.", {}),
    ("p0008-b009", "text", ("p0008-b009",),
     "[17] S. Liu, C. Liu, and J. Dolan, “Safe control under input limits with neural control barrier functions,” in *Conference on Robot Learning*, PMLR, 2023, pp. 1970–1980.", {}),
    ("p0008-b010", "text", ("p0008-b010",),
     "[18] O. So et al., “How to train your neural control barrier function: Learning safety filters for complex input-constrained systems,” in *2024 IEEE International Conference on Robotics and Automation (ICRA)*, IEEE, 2024, pp. 11 532–11 539.", {}),
    ("p0008-b011", "text", ("p0008-b011",),
     "[19] StanfordASL, *Hj_reachability: Hamilton-jacobi reachability analysis in jax*, `https://github.com/StanfordASL/hj_reachability`, 2024.", {}),
    ("p0008-b012", "text", ("p0008-b012",),
     "[20] F. Bullo, *Contraction Theory for Dynamical Systems*, 1.2. Kindle Direct Publishing, 2024, ISBN: 979-8836646806.", {}),
    ("p0008-b013", "heading", ("p0008-b013",), "## Appendix", {}),
    ("p0008-b014", "heading", ("p0008-b014",), "### A. Proof of Lemma 1", {}),
    ("p0008-b015", "text", ("p0008-b015",),
     r"**Proof.** According to the assumption of system (1), since the system (1) is uniformly continuous in $u$, thus $L_{u} = \max\limits_{t\in (0, \tau]} \|g(\phi(t,x,u))\| := \max\limits_{\|v\| = 1, t\in (0,\tau]}\|g(\phi(t,x,u)) v\| > 0$ exists. And the system (1) is uniformly continuous in $u$, and Lipschitz continuous in $x$ for fixed control $u$, with a little abuse of the notation, for all the states $x'$ and $y'$ in trajectories $\phi(t,x,u)$ and $\phi(t,y,u)$, $\forall t\in (0,\tau]$ we have:", {}),
    ("p0008-b028", "text", ("p0008-b028", "p0008-b029"),
     r"""$$
\begin{aligned}
 & \|F(x, u) - F(y, u)\| \leq L \|x - y\|\\
 & \|F(x, u) - F(x, v)\| = \|g(x)(u-v)\| \leq L_{u}\|u-v\|
\end{aligned}
$$""", {}),
    ("p0008-b016", "text", ("p0008-b016",),
     "Thus, according to Corollary 3.17 and Grönwall Comparison Lemma in [20], we have:", {}),
    ("p0008-b017", "text", ("p0008-b017",),
     r"""$$
\begin{aligned}
 & \|\phi(t,x,u) - \phi(t,y,u)\| \\
 & \leq e^{Lt} \|x - y\| + L_{u} \int_{0}^{t}e^{L(t-s)}\|u(s) - u(s)\|ds\\
 & = e^{Lt}\|x-y\| \\
 & \leq re^{Lt},
\end{aligned}
$$""", {}),
    ("p0008-b018", "text", ("p0008-b018",),
     "where equality is held because two trajectories have the same input trajectory.", {}),
    ("p0008-b019", "text", ("p0008-b019",),
     r"Suppose $x^{\ast}=\arg\min_{x^{\ast} \in \partial S} \mathrm{sd}(\phi(t,x,u), \mathcal{S}), y^{\ast}=\arg\min_{y^{\ast} \in \partial S} \mathrm{sd}(\phi(t,y,u), \mathcal{S})$. The three cases are analyzed as follows:", {}),
    ("p0008-b020", "text", ("p0008-b020",),
     r"**Case 1**: $\phi(t,x,u)$ and $\phi(t,y,u)$ are both in $S$, and then we have", {}),
    ("p0008-b021", "text", ("p0008-b021",), CASE12, {}),
    ("p0008-b022", "text", ("p0008-b022",),
     "where the first equality follows from the definition, and the first inequality follows from the triangle inequality.", {}),
    ("p0008-b023", "text", ("p0008-b023",),
     r"**Case 2**: $\phi(t,x,u)$ and $\phi(t,y,u)$ are both not in $S$, and then with the same reason, similarly, we have", {}),
    ("p0008-b024", "text", ("p0008-b024",), CASE12, {}),
    ("p0008-b025", "text", ("p0008-b025",),
     r"**Case 3**: One of $\phi(t,x,u)$ and $\phi(t,y,u)$ is in $S$ and the other not in $S$. Without loss of generality, we can assume that $\phi(t,x,u)$ is in $S$ and $\phi(t,y,u)$ is not in $S$. Then there at least exists a $\lambda \in [0, 1]$ such that $\lambda \phi(t,x,u) + (1-\lambda)\phi(t,y,u) \in \partial S$ and we denote $p^{\ast} := \lambda\phi(t,x,u) + (1-\lambda)\phi(t,y,u) \in \partial S$, thus, we have", {}),
    ("p0008-b026", "text", ("p0008-b026",),
     r"""$$
\begin{aligned}
 & |\mathrm{sd}(\phi(t,x,u),S) - \mathrm{sd}(\phi(t,y,u), S)|\\
 = & \|\phi(t,y,u)-y^{\ast}\| + \|\phi(t,x,u) - x^{\ast}\|\\
\leq & \|\phi(t,x,u) - p^{\ast}\| + \|\phi(t,y,u)-p^{\ast}\||\\
= & \|\phi(t,x,u) - \phi(t,y,u)\|\\
\leq & re^{Lt},
\end{aligned}
$$""", {}),
    ("p0008-b027", "text", ("p0008-b027",),
     r"where the first equality and the first inequality follow from the definition of the signed distance function, and the second equality follows from the definition of $p^{\ast}$. In all cases, we obtain $|\mathrm{sd}(\phi(t,x,u),S) - \mathrm{sd}(\phi(t,y,u), S)| \leq re^{Lt}$ as required. $\square$", {}),
])
