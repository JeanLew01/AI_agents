from pt import *
items = [
 HDR(),
 H(r"## Appendix D. Computing the Lipschitz constant of a ReLU network from samples", [90, 93, 510, 105]),
 T(r"""In this section, we show that sampling gradients enables obtaining the Lipschitz constant of a neural network with ReLU activation functions with high probability. Consider a feed-forward ReLU neural network $f:\mathbb{R}^n\rightarrow\mathbb{R}^n$ with $\ell\in\mathbb{N}$ layers, given as""", [90, 114, 523, 152]),
 T(r"""$$
f(x) = W^\ell x^\ell + b^\ell, \quad x^{k+1}=\phi^k(W^kx^k+b^k), \ k=0,\dots,\ell-1, \quad x^0 = x,
$$""", [135, 162, 478, 178]),
 T(r"""where $(W^k,b^k)_{k=0}^\ell$ are the network weights and biases, and each $\phi^k:\mathbb{R}^{n_k}\rightarrow\mathbb{R}^{n_{k+1}}$ is defined as $\phi^k(x)=(\varphi(x_1),\dots,\varphi(x_{n_k}))$ with $\varphi(z)=\max(0,z)$. Note that $f$ is piecewise-affine.""", [90, 186, 523, 212]),
 T(r"""Let $\mathcal{X}\subset\mathbb{R}^n$ be a non-empty compact set. Let $\mathcal{A}=\{A_1,\dots,A_N\}$ be the set of all polytopes $A_i\subseteq\mathcal{X}$ where $f|_{A_i}$ is affine, which we call the activation regions of $f$. Let $\Lambda_N=\frac{\min_{i=1,\dots,N} \lambda(A_i)}{\lambda(\mathcal{X})}$ be the smallest (normalized Lebesgue) volume of all activation regions. Note that $f$ is Lipschitz continuous over $\mathcal{X}$, since it is continuous and restricted to a compact subset. Thus, for some $L\geq 0$,""", [90, 213, 523, 266]),
 T(r"""$$
\|f(x_1)-f(x_2)\|\leq L\|x_1-x_2\|\quad \forall x_1,x_2\in\mathcal{X}.
$$""", [197, 277, 415, 292]),
 T(r"""Further, since $f$ is piecewise-affine, $f$ is $L$-Lipschitz continuous with""", [90, 301, 523, 313]),
 T(r"""$$
L=\max_{i=1,\dots,N} \{\|\nabla f(x_i)\|\ \text{for some }x_i\in A_i\}.
$$""", [208, 321, 405, 343]),
 T(r"""We propose the following sampling-based method to recover the Lipschitz constant $L$:""", [90, 352, 523, 364]),
 T(r"""1. Draw $M$ random samples $x_i$ in $\mathcal{X}$ according to the uniform probability measure over $\mathcal{X}$.
2. Evaluate $L_i=\|\nabla f(x_i)\|$ for all $i=1,\dots,M$.
3. Set $\hat{L}=\max_{i=1,\dots,M} L_i$.""", [104, 372, 523, 423]),
 T(r"""In general, with this approach, providing statistical guarantees on whether $\hat{L}$ is a valid Lipschitz constant for $f$ is challenging; the analysis would rely on the Hessian of $f$ which is a-priori unknown. In this specific setting, $f$ is piecewise-affine, which we leverage in the analysis below.""", [90, 432, 523, 471]),
 T(r"""**Lemma 7** With the previous notations, define $\delta_M=N(1-\Lambda_N)^M$. Then,""", [90, 481, 523, 494]),
 T(r"""$$
\mathbb{P}(f\text{ is $\hat{L}$-Lipschitz continuous over $\mathcal{X}$})\geq 1-\delta_M.
$$""", [195, 502, 417, 518]),
 T(r"""**Proof** Since $L=\max_{i=1,\dots,N} \{\|\nabla f(x_i)\|\ \text{for some }x_i\in A_i\}$, a sufficient condition for $f$ to be $\hat{L}$-Lipschitz continuous is that at least one point $x_j$ was sampled in each region $A_i$. Thus,""", [90, 526, 523, 553]),
 T(r"""$$
\begin{aligned}
\mathbb{P}\left( \bigcap_{i=1}^N\left\{ \bigcup_{j=1}^M \{x_j\}\cap A_i\neq\emptyset \right\} \right) &= 1- \mathbb{P}\left( \bigcup_{i=1}^N\left\{ \bigcup_{j=1}^M \{x_j\}\cap A_i\neq\emptyset \right\}^{\mathsf{c}} \right) \\
&\geq 1- \sum_{i=1}^N \mathbb{P}\left( \bigcap_{j=1}^M x_j\notin A_i \right) \quad\text{(Boole's inequality)} \\
&= 1- \sum_{i=1}^N \mathbb{P}\left( x_j\notin A_i \right)^M \qquad\quad\text{(independent samples)} \\
&\geq 1-N(1-\Lambda_N)^M,
\end{aligned}
$$""", [108, 561, 504, 705]),
 PNUM(23),
]
page(23, items, r"""Appendix D (sampling-based Lipschitz constant of a ReLU network, Lemma 7 and the first part of its proof). Text and mathematics taken from the authors' TeX (main.tex lines 2581-2660), macros expanded (\A -> \mathcal{A}, \comp -> \mathsf{c}), and compared with the 150-dpi render and three 230-dpi crops covering the whole page. Checked symbol by symbol: network f: R^n -> R^n with ell layers, f(x) = W^ell x^ell + b^ell, x^{k+1} = phi^k(W^k x^k + b^k), k = 0,...,ell-1, x^0 = x; phi^k: R^{n_k} -> R^{n_{k+1}}, varphi(z) = max(0,z); Lambda_N = min_{i=1,...,N} lambda(A_i) / lambda(X); ||f(x_1)-f(x_2)|| <= L ||x_1-x_2|| for all x_1,x_2 in X; L = max_{i=1,...,N} {||grad f(x_i)|| for some x_i in A_i}; the three-step procedure (one numbered list item, numbering as printed); Lemma 7: delta_M = N (1 - Lambda_N)^M and P(f is \hat L-Lipschitz continuous over X) >= 1 - delta_M; proof chain: P(cap_{i=1}^N {cup_{j=1}^M {x_j} cap A_i != empty}) = 1 - P(cup_{i=1}^N {...}^c) >= 1 - sum_{i=1}^N P(cap_{j=1}^M x_j not-in A_i) (Boole's inequality) = 1 - sum_{i=1}^N P(x_j not-in A_i)^M (independent samples) >= 1 - N (1 - Lambda_N)^M, ending with a comma; the sentence continues on page 24 ('where the last step follows from ...'). All five displays were extractor formula images or glyph soup and are now LaTeX; none has a printed number. Labels as printed: '**Lemma 7**' (bold, no period, italic body ending with the display) and '**Proof**'. Heading fixed to '## Appendix D. Computing the Lipschitz constant of a ReLU network from samples'. Running header and page number 23 omitted.""")
