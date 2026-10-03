from pagelib import *
P = 18
items = [
    heading("p0018-b000", B(P, "p0018-b000"), "#### C.4.3 Proof Details"),
    text("p0018-b001", B(P, "p0018-b001"),
         r"**Proof. Step 1** (convergence of the critics $V_\eta$ and $V_\kappa$ updates): From the multi-time scale assumption, we know that $\eta$ and $\kappa$ will convergence on a faster time scale than the other parameters $\theta$, $\xi$, and $\omega$. Therefore, we can leverage Lemma $1$ of Chapter $6$ of [10] to analyze the convergence properties while updating $\eta_k$ and $\kappa_k$ by treating $\theta$, $\xi$, and $\omega$ as fixed parameters $\theta_k$, $\xi_k$, and $\omega_k$. In other words, the policy, REF, and lagrange multiplier are fixed while computing $Q^{\pi_{\theta_k}}(s,a)$ and $Q_c^{\pi_{\theta_k}}(s,a)$. With the Finite MDP assumption and policy evaluation convergence results of [52], and assuming sufficiently expressive function approximator (i.e. wide enough neural networks) to ensure convergence to global mininum, we can use the fact that the bellman operators $\mathcal{B}$ and $\mathcal{B}_c$ which are defined as"),
    display("p0018-b002", B(P, "p0018-b002"), r"""\begin{aligned}
\mathcal{B}[Q] (s,a) = r(s,a)+\gamma\mathbb{E}_{s',a'\sim \pi,P(s)}[Q(s', a')] \\
\mathcal{B}[Q_c] (s,a) = h(s)+\gamma\mathbb{E}_{s',a'\sim \pi,P(s)}[Q_c(s', a')]
\end{aligned}"""),
    text("p0018-b003", B(P, "p0018-b003"),
         r"are $\gamma$-contraction mappings, and therefore as $k$ approaches $\infty$, we can be sure that $Q(s,a;\eta_k)\rightarrow Q(s,a;\eta^{\ast})=Q^{\pi_{\theta_k}}(s,a)$ and $Q_c(s,a;\kappa_k)\rightarrow Q_c(s,a;\kappa^{\ast})=Q_c^{\pi_{\theta_k}}(s,a)$. So since $\eta_k$ and $\kappa_k$ converge to $\eta^{\ast}$ and $\kappa^{\ast}$, we prove convergence of the critics in Time scale 1."),
    text("p0018-b004", B(P, "p0018-b004"),
         r"**Step 2** (convergence of the policy $\pi_\theta$ update): Because $\xi$ and $\omega$ updated on slower time scales than $\theta$, we can again use Lemma $1$ of Chapter $6$ of [10] and treat these parameters are fixed at $\xi_k$ and $\omega_k$ respectively when updating $\theta_k$. Additionally in Time scale 2, we have $||Q(s,a;\eta_k)-Q(s,a;\eta^{\ast})||\rightarrow 0$ and $||Q_c(s,a;\kappa_k)-Q_c(s,a;\kappa^{\ast})||\rightarrow 0$ almost surely. Now the update of the policy $\theta$ using the gradient from Equation 4 is:"),
    display("p0018-b005", B(P, "p0018-b005"), r"""\begin{aligned}
\theta_{k+1} &=\Gamma_\Theta [ \theta_k - \zeta_2(k)( \nabla_\theta L(\theta, \xi_k, \omega_k)|_{\theta=\theta_k})] \\
&=\Gamma_\Theta [\theta_k - \zeta_2(k)[\gamma^t [-Q_\eta(s_t,a_t) [1 - p_{\xi_k}(s_t)] \\
&+ Q_c(s_t,a_t) [\lambda_\omega (1 - p_{\xi_k}(s_t)) + p_{\xi_k}(s_t)]]\nabla_\theta \log \pi(a_t | s_t; \theta) |_{\theta=\theta_k}]]\\
&=\Gamma_\Theta [ \theta_k - \zeta_2(k) (\nabla_\theta L(\theta, \xi_k, \omega_k)|_{\theta=\theta_k, \eta=\eta^{\ast}, \kappa=\kappa^{\ast}} + \delta\theta_{k+1} + \delta\theta_\epsilon)]
\end{aligned}"""),
    text("p0018-b006", B(P, "p0018-b006"), r"where"),
    display("p0018-b007", B(P, "p0018-b007"), r"""\begin{aligned}
\delta \theta_{k+1} = \sum_{s_i,a_i} \biggl[d_0(s_0)P^{\pi_{\theta_k}}(s_i,a_i|s_0) \gamma^i [-Q_\eta(s_i,a_i) [1 - p_{\xi_k}(s_i)] &\\
+ Q_c(s_i,a_i) [\lambda_\omega (1 - p_{\xi_k}(s_i)) + p_{\xi_k}(s_i)]]\nabla_\theta \log \pi(a_i | s_i; \theta) |_{\theta=\theta_k}\biggr] &\\
- \gamma^t [-Q_\eta(s_t,a_t) [1 - p_{\xi_k}(s_t)] + Q_c(s_t,a_t) [\lambda_\omega (1 - p_{\xi_k}(s_t)) + p_{\xi_k}(s_t)]] &\\
\cdot\nabla_\theta \log \pi(a_t | s_t; \theta) |_{\theta=\theta_k} &
\end{aligned}"""),
    text("p0018-b008", B(P, "p0018-b008"), r"and"),
    display("p0018-b009", B(P, "p0018-b009"), r"""\begin{aligned}
\delta \theta_\epsilon = \sum_{s_i,a_i} d_0(s_0)P^{\pi_{\theta_k}}(s_i,a_i|s_0)\biggl[ &\\
- \gamma^i [-Q(s_i,a_i;\eta_k) [1 - p_{\xi_k}(s_i)] + Q_c(s_i,a_i; \kappa_k) [\lambda_\omega (1 - p_{\xi_k}(s_i)) + p_{\xi_k}(s_i)]] &\\
\cdot\nabla_\theta \log \pi(a_i | s_i; \theta) |_{\theta=\theta_k} &\\
+ \gamma^i [-Q^{\pi_{\theta_k}}(s_i,a_i) [1 - p_{\xi_k}(s_i)] + Q^{\pi_{\theta_k}}_c(s_i,a_i) [\lambda_\omega (1 - p_{\xi_k}(s_i)) + p_{\xi_k}(s_i)]] &\\
\cdot\nabla_\theta \log \pi(a_i | s_i; \theta) |_{\theta=\theta_k} \biggr] &
\end{aligned}"""),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 18 and with main.tex (C.4.3, Step 1 and the first half of Step 2 of the
proof of the convergence theorem). All mathematics rewritten in LaTeX from the TeX source and checked on the render,
line by line for the four displays; TeX and PDF agree. None of the displays is numbered and none ends with
punctuation. Display 1: the two Bellman operators; as printed the second line is $\mathcal{B}[Q_c](s,a)$ (operator
without subscript c, although the sentence before it names $\mathcal{B}$ and $\mathcal{B}_c$). Display 2: the policy
update in four aligned lines (the second equality is broken after the first bracket term). Display 3
($\delta\theta_{k+1}$) and display 4 ($\delta\theta_\epsilon$) are multi-line displays whose lines are printed
right-aligned; they are written as aligned blocks with the alignment mark at the line ends, as in the source (in
display 4 the source has no alignment mark on the first line, which only changes its horizontal position; one was
added). The large brackets are fixed-size delimiters that open on one line and close on a later one, exactly as
printed. As printed (kept): 'will convergence', 'mininum', 'bellman operators', 'treat these parameters are fixed',
'lagrange multiplier'; the heading of Step 1 speaks of critics $V_\eta$ and $V_\kappa$ while the text uses $Q$ and
$Q_c$; the norm is typed with double bars; 'Lemma $1$ of Chapter $6$ of [10]' with math-mode numerals (twice);
'Equation 4' (the full objective of Section 5.3); citations [10], [52]. 'Proof.' is printed in italics and 'Step 1' /
'Step 2' in bold; they are written as one bold run '**Proof. Step 1**' and '**Step 2**'. Asterisks written \ast. The
proof continues on page 19 with 'Lemma 1:'. Heading C.4.3 level 4. In the two-line Bellman-operator display a space was typed between the closing square bracket and the argument, '[Q] (s,a)', only so that the pair is not parsed as a Markdown link; it does not change the formula.
Omitted: printed page number 18.
""")
