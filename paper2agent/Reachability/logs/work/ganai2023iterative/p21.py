from pagelib import *
P = 21
SUM = r"-\sum_{s_i,a_i} d_0(s_0)P^{\pi_{\theta_k}}(s_i,a_i|s_0)[Q^{\pi_{\theta^{\ast}}}_c(s_i,a_i)[1-p_{\xi^{\ast}}(s_i)]\nabla_\omega \lambda_\omega |_{\omega=\omega_k} ]"
items = [
    text("p0021-b000", B(P, "p0021-b000"),
         r"Notice that $\pi^\diamond$ is a locally minimum optimal policy for the following optimization (recall $\lambda_\omega$ is treated as constant in this timescale):"),
    display("p0021-b001a", [134.0, 97.0, 478.0, 124.5],
            r"\min_{\pi} \mathbb{E}_{s\sim d_0} \mathbb{E}_{a\sim \pi(\cdot | s)}\bigg[-Q^{\pi}(s,a)\cdot [1 - p^{\diamond}(s)] + Q^{\pi}_c(s,a)\cdot [(1 - p^{\diamond}(s))\lambda_\omega + p^{\diamond}(s)]\bigg]"),
    text("p0021-b002", [107.0, 127.5, 381.0, 138.5],
         r"and therefore also locally minimum optimal policy for optimization:"),
    display("p0021-b001b", [134.0, 140.0, 478.0, 197.0], r"""\begin{aligned}
\min_{\pi}\mathbb{E}_{s\sim d_0}\mathbb{E}_{a\sim \pi(\cdot | s)}\bigg[-Q^{\pi}(s,a) + Q^{\pi}_c(s,a)\cdot [\lambda_\omega + \frac{p^{\diamond}(s)}{(1 - p^{\diamond}(s))}]\bigg] \text{, if } p^{\diamond}(s) > 0\\
\mathbb{E}_{s\sim d_0}\min_{\pi}\mathbb{E}_{a\sim \pi(\cdot | s)}\bigg[Q^{\pi}_c(s,a)\bigg] \text{, if } p^{\diamond}(s) = 0
\end{aligned}"""),
    text("p0021-b003", [107.0, 203.0, 505.0, 242.5],
         r"Since $\frac{p^{\diamond}(s)}{(1 - p^{\diamond}(s))} \geq 0$, and the $Q$ functions are always nonnegative, we can know that $\pi^\diamond$ is at least as safe as (i.e., its expected cumulative cost is at most that of) a locally optimal policy for the optimization:"),
    display("p0021-b004", [207.0, 243.5, 510.0, 275.0],
            r"\min_{\pi} \mathbb{E}_{s\sim d_0}\mathbb{E}_{a\sim \pi(\cdot | s)}\bigg[ -Q^{\pi}(s,a) + Q^{\pi}_c(s,a)\lambda_\omega\bigg] \tag{8}"),
    text("p0021-b005", [107.0, 275.5, 505.0, 323.0],
         r"As $\lambda_\omega$ approaches $\lambda_{\max}$, which in turn approaches $\infty$, the local minimum optimal policies of Equation 8 approach those of the optimization $\pi^\bigtriangleup = \arg\min_\pi \mathbb{E}_{s\sim d_0}\mathbb{E}_{a\sim \pi(\cdot | s)} Q^{\pi}_c(s,a)\lambda_\omega=\arg\min_\pi \mathbb{E}_{s\sim d_0}\mathbb{E}_{a\sim \pi(\cdot | s)} Q^{\pi}_c(s,a)$. Therefore, the feasible set of the REF $p^{\diamond}$ will approach that of the REF $p^{\pi^\bigtriangleup}$."),
    text("p0021-b006", B(P, "p0021-b006"),
         r"**Step 4** (convergence of lagrange multiplier $\lambda_\omega$ update): Since $\lambda_\omega$ is on the slowest time scale, we have that $||\theta_k - \theta^{\ast}(\omega)||=0$, $||\xi_k - \xi^{\ast}(\omega)||=0$, and $||Q_c(s,a;\kappa_k) - Q^{\pi_{\theta_k}}_c(s,a)||=0$ almost surely. Furthermore, due to the continuity of $\nabla_\omega L(\theta, \xi, \omega)$, we have that $||\nabla_\omega L(\theta, \xi, \omega)|_{\theta=\theta_k, \xi=\xi_k, \omega=\omega_k} - \nabla_\omega L(\theta, \xi, \omega)|_{\theta=\theta^{\ast}(\omega_k), \xi=\xi^{\ast}(\omega_k), \omega=\omega_k}||=0$ almost surely. The update of the multiplier using the gradient for Equation is:"),
    display("p0021-b007", [154.0, 387.5, 458.0, 431.0], r"""\begin{aligned}
\omega_{k+1} &=\Gamma_\Omega [ \omega_k + \zeta_4(k)( \nabla_\omega L(\theta, \xi, \omega)|_{\theta=\theta_k, \xi=\xi_k, \omega=\omega_k})] \\
&=\Gamma_\Omega [ \omega_k + \zeta_4(k)( Q_c(s_t, a_t; \kappa_k)[1-p(s_t; \xi_k)]\nabla_\omega \lambda_\omega |_{\omega=\omega_k})] \\
&=\Gamma_\Omega [ \omega_k + \zeta_4(k)( \nabla_\omega L(\theta, \xi, \omega)|_{\theta=\theta^{\ast}(\omega_k), \xi=\xi^{\ast}(\omega_k), \omega=\omega_k} + \delta \omega_{k+1})]
\end{aligned}"""),
    text("p0021-b008", [107.0, 432.0, 132.0, 442.0], r"where"),
    display("p0021-b009", [114.0, 444.0, 497.0, 660.0], r"""\begin{aligned}
\delta \omega_{k+1} &= -\nabla_\omega L(\theta, \xi, \omega)|_{\theta=\theta^{\ast}(\omega_k), \xi=\xi^{\ast}(\omega_k), \omega=\omega_k} + Q_c(s_t, a_t; \kappa_k)[1-p(s_t; \xi_k)]\nabla_\omega \lambda_\omega |_{\omega=\omega_k} \\
&= """ + SUM + r""" \\
&+ Q_c(s_t, a_t; \kappa_k)[1-p(s_t; \xi_k)]\nabla_\omega \lambda_\omega |_{\omega=\omega_k} \\
&=""" + SUM + r""" \\
&+ [Q_c(s_t, a_t; \kappa_k)[1-p(s_t; \xi_k)] -  Q^{\pi_{\theta_k}}_c(s_t, a_t)[1-p(s_t; \xi_k)] +\\
&Q^{\pi_{\theta_k}}_c(s_t, a_t)[1-p(s_t; \xi_k)] - Q^{\pi_{\theta_k}}_c(s_t, a_t)[1-p^\diamond(s_t)] + \\
&Q^{\pi_{\theta_k}}_c(s_t, a_t)[1-p^\diamond(s_t)] ]\nabla_\omega \lambda_\omega |_{\omega=\omega_k} \\
&=""" + SUM + r""" \\
&+ [(Q_c(s_t, a_t; \kappa_k)-Q^{\pi_{\theta_k}}_c(s_t, a_t))[1-p(s_t; \xi_k)]  +\\
&Q^{\pi_{\theta_k}}_c(s_t, a_t)[p^\diamond(s_t)-p(s_t; \xi_k)] + \\
&Q^{\pi_{\theta_k}}_c(s_t, a_t)[1-p^\diamond(s_t)]] \nabla_\omega \lambda_\omega |_{\omega=\omega_k}]
\end{aligned}"""),
    text("p0021-b010", B(P, "p0021-b010"),
         r"Now, just as in the $\theta$ update convergence, we can demonstrate the following lemmas:"),
    text("p0021-b011", B(P, "p0021-b011"),
         r"**Lemma 4:** $\delta \omega_{k+1}$ is square integrable since"),
    display("p0021-b012", [181.0, 695.0, 431.0, 726.0],
            r"\mathbb{E}[||\delta\omega_{k+1}||^2| \mathcal{F}_{\omega,k}] \leq 2\cdot \frac{H_{\max}}{1-\gamma}\cdot 1 \cdot K_3(1 + ||\omega_k||^2_\infty) < \infty"),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 21 and with main.tex (end of Step 3 and first part of Step 4 of the
convergence proof). All mathematics rewritten in LaTeX from the TeX source and checked line by line on the render; TeX
and PDF agree. Displays: (i) the unnumbered optimization that $\pi^\diamond$ solves; (ii) the unnumbered two-line
display with the cases ', if $p^{\diamond}(s)>0$' and ', if $p^{\diamond}(s)=0$' (two right-aligned lines in the PDF,
written as one aligned block); (iii) the numbered optimization (8); (iv) the three-line multiplier update
$\omega_{k+1}=\Gamma_\Omega[\ldots]$; (v) the eleven-line decomposition of $\delta\omega_{k+1}$; (vi) the bound of
Lemma 4, whose sentence continues on page 22 ('for some large Lipschitz constant $K_3$'). The extractor had one
formula image over displays (i) and (ii) with the sentence 'and therefore also locally minimum optimal policy for
optimization:' printed between them, and the paragraph 'Since ...' began with underlined glyph debris of the inline
fraction; items were rebuilt in printed order with bboxes from the evidence line positions. As printed (kept): 'The
update of the multiplier using the gradient for Equation is:' with no equation number after 'Equation' (the source has
none either); 'Equation 8'; the multiplier update is written with a plus sign, $\omega_k+\zeta_4(k)(\ldots)$; in
display (v) the brackets are ordinary square brackets, three continuation lines start directly with
$Q^{\pi_{\theta_k}}_c$ after a trailing plus sign on the previous line, and the last line ends with one more closing
bracket than is opened; the sum is over $s_i,a_i$ with $Q^{\pi_{\theta^{\ast}}}_c$ and $p_{\xi^{\ast}}$ while the
sampled terms use $s_t,a_t$; convergence statements written as equalities ('$=0$ almost surely'); the limiting policy
is written with a triangle superscript, $\pi^\bigtriangleup$, and $p^{\pi^\bigtriangleup}$; 'lagrange multiplier' in
lower case. 'Step 4' bold as printed; 'Lemma 4' printed in italics with an upright colon (bold label here). Asterisks
written \ast. No citations on this page. Omitted: printed page number 21.
""")
