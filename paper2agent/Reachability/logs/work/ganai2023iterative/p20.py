from pagelib import *
P = 20
items = [
    text("p0020-b000", B(P, "p0020-b000"),
         r"And because we have $||Q(s,a;\eta_k)-Q(s,a;\eta^{\ast})||\rightarrow 0$ and $||Q_c(s,a;\kappa_k)-Q_c(s,a;\kappa^{\ast})||\rightarrow 0$ almost surely, we can therefore say $\delta\theta_\epsilon\rightarrow 0$."),
    text("p0020-b001", [107.0, 101.0, 505.0, 125.0],
         r"**Lemma 3:** Finally, since $\hat{\nabla}_\theta J_\pi (\theta)|_{\theta=\theta_k}$ is a sample of $\nabla_\theta L(\theta, \xi_k, \omega_k)|_{\theta=\theta_k}$ based on the history of sampled trajectories, we conclude that $\mathbb{E}[\delta \theta_{k+1} | \mathcal{F}_{\theta,k}]=0$."),
    text("p0020-b001b", [107.0, 129.0, 505.0, 152.0],
         r"From the $3$ above lemmas, the policy $\theta$ update is a stochastic approximation of a continuous system $\theta(t)$ defined by [10]"),
    display("p0020-b002", B(P, "p0020-b002"),
            r"\dot{\theta} = \Upsilon_\Theta[-\nabla_\theta L(\theta, \xi, \omega)] \tag{7}"),
    text("p0020-b003", B(P, "p0020-b003"), r"in which"),
    display("p0020-b004", B(P, "p0020-b004"),
            r"\Upsilon_\Theta[M(\theta] \overset{\Delta}{=} \lim\limits_{0<\psi \to 0}\frac{\Gamma_\Theta(\theta + \psi M(\theta)) - \Gamma_\Theta(\theta)}{\psi}"),
    text("p0020-b005", B(P, "p0020-b005"),
         r"or in other words the left directional derivative of $\Gamma_\Theta(\theta)$ in the direction of $M(\theta)$. Using the left directional derivative $\Upsilon_\Theta[-\nabla_\theta L(\theta, \xi, \omega)]$ in the gradient descent algorithm for learning the policy $\pi_\theta$ ensures the gradient will point in the descent direction along the boundary of $\Theta$ when the $\theta$ update hits its boundary. Using Step 2 in Appendix A.2 from [8], we have that $dL(\theta,\xi,\omega)/dt=-\nabla_\theta L(\theta,\xi,\omega)^T\cdot\Upsilon_\Theta[-\nabla_\theta L(\theta, \xi, \omega)] \leq 0$ and the value is non-zero if $||\Upsilon_\Theta[-\nabla_\theta L(\theta, \xi, \omega)]|| \neq 0$. Now consider the continuous system $\theta(t)$. For some fixed $\xi$ and $\omega$, define a Lyapunov function"),
    display("p0020-b006", B(P, "p0020-b006"),
            r"\mathcal{L}_{\xi, \omega}(\theta) = L(\theta,\xi,\omega) - L(\theta^{\ast}, \xi, \omega)"),
    text("p0020-b007", B(P, "p0020-b007"),
         r"where $\theta^{\ast}$ is a local minimum point. Then there exists a ball centered at $\theta^{\ast}$ with a radius $\rho$ such that $\forall \theta\in \mathfrak{B}_{\theta^{\ast}}(\rho)=\{\theta | ||\theta - \theta^{\ast}|| \leq \rho  \}$, $\mathcal{L}_{\xi, \omega}(\theta)$ is a locally positive definite function, that is $\mathcal{L}_{\xi, \omega}(\theta) \geq 0$. Using Proposition 1.1.1 from [54], we can show that $\Upsilon_\Theta[-\nabla_\theta L(\theta, \xi, \omega)]|_{\theta=\theta^{\ast}}=0$ meaning $\theta^{\ast}$ is a stationary point. Since $dL(\theta,\xi,\omega)/dt\leq 0$, through Lyapunov theory for asymptotically stable systems presented in Chapter 4 of [55], we can use the above arguments to demonstrate that with any initial conditions of $\theta(0)\in \mathfrak{B}_{\theta^{\ast}}(\rho)$, the continuous state trajectory of $\theta(t)$ converges to $\theta^{\ast}$. Particularly, $L(\theta^{\ast},\xi,\omega) \leq L(\theta(t), \xi, \omega) \leq L(\theta(0), \xi, \omega)$ for all $t>0$."),
    text("p0020-b008", B(P, "p0020-b008"),
         r"Using these aforementioned properties, as well as the facts that 1) $\nabla_\theta L(\theta, \xi, \omega)$ is a Lipschitz function (using Proposition $17$ from [8]), 2) the step-sizes of Assumption on steps sizes, 3) $\delta \theta_{k+1}$ is a square integrable Martingale difference sequence and $\delta\theta_\epsilon$ is a vanishing error almost surely, and 4) $\theta_k \in \Theta, \forall k$ implying that $\sup_k  ||\theta_k||<\infty$ almost surely, we can invoke Theorem $2$ of chapter $6$ in [10] to demonstrate the sequence $\{\theta_k\}, \theta_k\in \Theta$ converges almost surely to the solution of the ODE defined by Equation 7, which additionally converges almost surely to the local minimum $\theta^{\ast}\in \Theta$."),
    text("p0020-b009", B(P, "p0020-b009"),
         r"**Step 3** (convergence of REF $p_\xi$ updates): Since $\omega$ is updated on a slower time scale that $\xi$, we can again treat $\omega$ as a fixed parameter at $\omega_k$ when updating $\xi$. Furthermore, in Time scale $3$, we know that the policy has converged to a local minimum, particularly $||\theta_k-\theta^{\ast}(\xi_k,\omega_k)|| = 0$. Now the bellman operator for REF is defined by"),
    display("p0020-b010a", [210.0, 523.5, 402.0, 548.0],
            r"\mathcal{B}_p[p] (s) = \max\{\mathbb{1}_{s\in S_v}, \gamma \mathbb{E}_{s'\sim \pi, P(s)}[p(s')]\}."),
    text("p0020-b011", [107.0, 554.0, 344.0, 564.5],
         r"We demonstrate this is a $\gamma$ contraction mapping as follows:"),
    display("p0020-b010b", [157.0, 570.0, 455.0, 674.0], r"""\begin{aligned}
&|\mathcal{B}_p[p] (s) - \mathcal{B}_p[\hat{p}] (s) | \\
&= |\max\{\mathbb{1}_{s\in S_v},  \gamma \mathbb{E}_{s'\sim \pi, P(s)}[p(s')]\} - \max\{\mathbb{1}_{s\in S_v},  \gamma \mathbb{E}_{s'\sim \pi, P(s)}[\hat{p}(s')]\}| \\
&\leq |\gamma \mathbb{E}_{s'\sim \pi, P(s)}[p(s')] - \gamma \mathbb{E}_{s'\sim \pi, P(s)}[\hat{p}(s')]| \\
&= \gamma |\mathbb{E}_{s'\sim \pi, P(s)}[p(s') -\hat{p}(s')]| \\
&\leq \gamma \sup_{s}|p(s) -\hat{p}(s)|= \gamma ||p-\hat{p}||_\infty
\end{aligned}"""),
    text("p0020-b012", B(P, "p0020-b012"),
         r"So we can say that $p(s;\xi_k)$ will converge to $p(s;\xi^{\ast})$ as $k\rightarrow\infty$ under the same assumptions of the Finite MDP and function approximator expressiveness in Step 1. Therefore, $\pi_{\theta_k}$ will also converge to $\pi^\diamond = \pi_{\theta^{\ast}(\xi^{\ast},\omega_k)}$ as $k\rightarrow\infty$. And because $\pi_\theta$ is the sampling policy used to compute $p$, $p(s;\xi^{\ast})=p^{\pi_{\theta^{\ast}(\xi^{\ast},\omega_k)}}(s;\xi^{\ast})=p^\diamond (s)$."),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 20 and with main.tex (end of Step 2 and the first half of Step 3 of the
convergence proof; this page contains the Bellman operator of the REF and its contraction argument). All mathematics
rewritten in LaTeX from the TeX source and checked on the render; TeX and PDF agree. Displays: (7) the projected ODE
$\dot\theta=\Upsilon_\Theta[-\nabla_\theta L(\theta,\xi,\omega)]$, the only numbered display of the page; the
unnumbered definition of $\Upsilon_\Theta$ (printed with the triangle-over-equals sign, written
\overset{\Delta}{=}, the limit subscript $0<\psi\to 0$, and an unbalanced bracket 'Upsilon_Theta[M(theta]' exactly as
printed: the closing parenthesis after theta is missing in the source and the PDF); the unnumbered Lyapunov function
$\mathcal{L}_{\xi,\omega}(\theta)$; the unnumbered REF Bellman operator
$\mathcal{B}_p[p](s)=\max\{\mathbb{1}_{s\in S_v},\gamma\mathbb{E}_{s'\sim\pi,P(s)}[p(s')]\}.$ (ends with a full stop);
and the unnumbered five-line contraction chain ending in $\gamma||p-\hat{p}||_\infty$ (no final punctuation). The
extractor had one formula image covering both of the last two displays with the sentence 'We demonstrate this is a
$\gamma$ contraction mapping as follows:' between them; they are separate items in printed order now, with bboxes from
the evidence line positions. The extractor had also merged 'Lemma 3: ...' and 'From the $3$ above lemmas ...' into one
item; they are two paragraphs. As printed (kept): the ball is a Fraktur B, $\mathfrak{B}_{\theta^{\ast}}(\rho)$,
defined with a single bar followed by a double-bar norm; 'left directional derivative' although the limit is taken for
$0<\psi\to 0$; 'a slower time scale that $\xi$' (that for than); 'the step-sizes of Assumption on steps sizes'; the
convergence statements written as equalities ($||\theta_k-\theta^{\ast}(\xi_k,\omega_k)||=0$); 'bellman operator'
in lower case; math-mode numerals in 'From the $3$ above lemmas', 'Proposition $17$', 'Theorem $2$ of chapter $6$',
'Time scale $3$' and plain numerals in 'Step 2 in Appendix A.2 from [8]', 'Proposition 1.1.1 from [54]', 'Chapter 4
of [55]', 'Equation 7', 'Step 1'; the limiting policy and REF are marked with a diamond superscript
($\pi^\diamond$, $p^\diamond$). 'Lemma 3' is printed in italics with an upright colon (bold label here, as for Lemmas
1-2); 'Step 3' bold as printed. Asterisks written \ast. Citations [10], [8], [54], [55] checked. In the REF Bellman operator and the first line of the contraction chain a space was typed between the closing square bracket and the argument, '[p] (s)', only so that the pair is not parsed as a Markdown link; it does not change the formula.
Omitted: printed page
number 20.
""")
