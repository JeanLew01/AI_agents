from pagelib import *
P = 12
EQ7 = r"""
\left\{ \begin{array}{l}
\dot{x}_1 = \cos(x_8) \cos(x_9)x_4+( \sin(x_7) \sin(x_8) \cos(x_9)- \cos(x_7) \sin(x_9))x_5\\
\quad +( \cos(x_7) \sin(x_8) \cos(x_9)+ \sin(x_7) \sin(x_9))x_6+v_1\\
\dot{x}_2 = \cos(x_8) \sin(x_9)x_4+( \sin(x_7)  \sin(x_8)  \sin(x_9)+ \cos(x_7)  \cos(x_9)) x_5\\
\quad +( \cos(x_7)  \sin(x_8)  \sin(x_9)- \sin(x_7)  \cos(x_9)) x_6+v_2\\
\dot{x}_3 =  \sin(x_8) x_4- \sin(x_7)  \cos(x_8) x_5- \cos(x_7)  \cos(x_8) x_6+v_3\\
\dot{x}_4 = x_{12} x_5-x_{11} x_6-9.81  \sin(x_8)+v_4\\
\dot{x}_5 = x_{10} x_6-x_{12} x_4 + 9.81  \cos(x_8)  \sin(x_7)+v_5\\
\dot{x}_6 = x_{11} x_4-x_{10} x_5 + 9.81  \cos(x_8)  \cos(x_7)-9.81-u_1/1.4+v_6\\
\dot{x}_7 = x_{10}+( \sin(x_7) ( \sin(x_8)/ \cos(x_8))) x_{11}+( \cos(x_7) ( \sin(x_8)/ \cos(x_8))) x_{12}+v_7\\
\dot{x}_8 =  \cos(x_7) x_{11}- \sin(x_7) x_{12}+v_8\\
\dot{x}_9 = ( \sin(x_7)/ \cos(x_8)) x_{11}+( \cos(x_7)/ \cos(x_8)) x_{12}+v_9\\
\dot{x}_{10} = -0.9259 x_{11} x_{12} + 18.5185 u_2+v_{10}\\
\dot{x}_{11} = 0.9259 x_{10} x_{12} + 18.5185 u_3+v_{11}\\
\dot{x}_{12} = v_{12}
\end{array} \right.
\qquad \mathcal{I}= \left\{  s_0\ \middle| \  \begin{bmatrix} -0.2\\-0.2\\-0.2\\-0.2\\-0.2\\-0.2\\0\\0\\0\\0\\0\\0\end{bmatrix} \leq s_0 \leq \begin{bmatrix} 0.2\\0.2\\0.2\\0.2\\0.2\\0.2\\0\\0\\0\\0\\0\\0\end{bmatrix}\right\} \tag{7}
"""
items = [
    display("p0012-b000", B(P, "p0012-b000"), EQ7),
    text("p0012-b001", B(P, "p0012-b001"),
         "of the system from a training dataset. We then used the surrogate model to perform reachability analysis over it using existing tools for deterministic reachability analysis. To quantify the error between the surrogate model and the underlying unknown system, we finally use conformal inference on a test dataset. We illustrated our approach using three case studies.",
         join_previous="space"),
    heading("p0012-b002", B(P, "p0012-b002"), "## Acknowledgments"),
    text("p0012-b003", B(P, "p0012-b003"),
         "This work was supported by the National Science Foundation through the following grants: CAREER award (SHF-2048094), CNS-1932620, FMitF-1837131, CCF-SHF-1932620, the Airbus Institute for Engineering Research, and funding by Toyota R&D and Siemens Corporate Research through the USC Center for Autonomy and AI."),
    heading("p0012-b004", B(P, "p0012-b004"), "## References"),
    text("p0012-b005", B(P, "p0012-b005"),
         "[1] A. P. Vinod and M. M. Oishi, “Stochastic reachability of a target tube: Theory and computation,” *Automatica*, vol. 125, p. 109458, 2021."),
    text("p0012-b006", B(P, "p0012-b006"),
         "[2] A. Abate, M. Prandini, J. Lygeros, and S. Sastry, “Probabilistic reachability and safety for controlled discrete time stochastic hybrid systems,” *Automatica*, vol. 44, no. 11, pp. 2724–2734, 2008."),
    text("p0012-b007", B(P, "p0012-b007"),
         "[3] A. Abate, S. Amin, M. Prandini, J. Lygeros, and S. Sastry, “Computational approaches to reachability analysis of stochastic hybrid systems,” in *International Workshop on Hybrid Systems: Computation and Control*. Springer, 2007, pp. 4–17."),
    text("p0012-b008", B(P, "p0012-b008"),
         "[4] Y. Yang, J. Zhang, K.-q. Cai, and M. Prandini, “A stochastic reachability analysis approach to aircraft conflict detection and resolution,” in *2014 IEEE Conference on Control Applications (CCA)*, 2014, pp. 2089–2094."),
    text("p0012-b009", B(P, "p0012-b009"),
         "[5] C. Huang, J. Fan, W. Li, X. Chen, and Q. Zhu, “Reachnn: Reachability analysis of neural-network controlled systems,” *ACM Transactions on Embedded Computing Systems (TECS)*, vol. 18, no. 5s, pp. 1–22, 2019."),
    pageno(P),
]
save(P, items, r"""
Compared with the 130 dpi render and a 230 dpi crop of PDF page 12, and with sections/experimental_results.tex,
sections/conc.tex, main.tex and main.bbl. Equation (7) (the 12-dimensional Quadcopter model and its initial set) is
printed as an uncaptioned full-width float at the top of this page; the text layer of this region is unusable glyph soup
(private-use bracket glyphs and interleaved rows), so the equation was taken from the TeX source and compared line by
line with the 230 dpi crop: the fourteen printed rows (the equations for $\dot{x}_1$ and $\dot{x}_2$ each wrap onto a
second row beginning with '+('), the constants 9.81 (four times), 1.4, 0.9259 (once with a minus sign, once without),
18.5185 (twice), the noise terms $v_1,\ldots,v_{12}$, the inputs $u_1,u_2,u_3$, and the bounds (-0.2 six times then 0 six
times; 0.2 six times then 0 six times). TeX and PDF agree. The source's two side-by-side arrays are written as one
left-brace array followed by the set $\mathcal{I}$ ('$\mathcal{I}=$' is printed on its own line above the set); the
printed number (7) is given as \tag; spacing commands \hspace of the source were dropped and the wrapped rows are
indented with \quad. Kept as printed: $\dot{x}_{12} = v_{12}$; tangent written as $\sin(x_8)/\cos(x_8)$. In the reading
order equation (7) is moved to the Quadcopter paragraph of Section 4 (pages 9-10), which refers to it. The item 'of the
system from a training dataset ...' continues the Conclusion sentence from page 11 with join_previous 'space'. Headings
'Acknowledgments' and 'References' are unnumbered level-2 headings. Acknowledgment: line-wrap hyphens removed in
'CAREER' and 'Institute'; grant numbers SHF-2048094, CNS-1932620, FMitF-1837131, CCF-SHF-1932620 read on the page.
References [1]-[5]: one item per entry, the extractor's bullet markers removed, italics as printed; every entry compared
with the page image and the .bbl (line-wrap hyphens removed in 'computation', 'Systems', 'neural-network' kept as a
compound).
""")
