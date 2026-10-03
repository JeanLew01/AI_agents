from pagelib import *

items = [
    running_header(9),
    text("p0009-b002", [71.0, 99.0, 441.0, 119.0],
         "due to Seeger. This theorem assumes that the concept class admits a parameterization which can be infinite-dimensional.",
         join_previous="space"),
    text("p0009-b003", [71.0, 127.0, 442.0, 185.0],
         r"**Theorem 3.5 (PAC-Bayes Theorem, adapted from [29, 17]).** Consider a concept class $\mathcal{C}$ admitting a parametrization by $w\in\mathcal{W}$. Let the loss function be zero-one valued, that is $\ell:\mathcal{C}\times\mathcal{X}\to\{0,1\}$. The following bound holds for all measures $P$, $Q$ over the concept class $\mathcal{C}$ defined by measures $W_P$ and $W_Q$ over $\mathcal{W}$ such that $W_Q$ is absolutely continuous with respect to $W_P$:"),
    text("p0009-b004", [66.0, 191.0, 435.0, 232.0],
         r"$$P_X^N\left( \left\{x_1,\dotsc,x_N: D_{ber}(\hat{r}_Q || r_Q) \le \frac{ D_{KL}(W_Q || W_P) + \log\frac{N+1}{\delta} }{N} \right\}\right) \ge 1 - \delta. \tag{3.2}$$"),
    text("p0009-b005", [71.0, 238.0, 442.0, 308.0],
         r"Here, $D_{KL}(W_P||W_Q)$ denotes the Kullback-Leibler (KL) divergence between $W_P$ and $W_Q$, and $D_{ber}(q||p)$ denotes the KL divergence between two Bernoulli distributions with parameters $q$ and $p$, given by the formula $D_{ber}(q||p) = q\log\frac{q}{p} + (1-q)\log\frac{1-q}{1-p}$. For a given set of data $x_1,\dotsc,x_N$, confidence parameter $\delta$, and a prior measure $P$ chosen independently of the data, the inequality (3.2) provides a family of Bayesian PAC bounds, one for each posterior measure $Q$."),
    figure("p0009-alg32", [250.0, 330.0, 435.0, 665.0], "Algorithm 3.2", "algorithm-3-2"),
    text("p0009-alg32-text", [256.0, 338.0, 427.0, 659.0], r"""
**Algorithm 3.2** To estimate a support set by a kernelized empirical inverse Christoffel function satisfying a Bayesian PAC bound.

- inputs: random variable $X$ with support in $\mathcal{X}$; positive definite kernel function $k$; PAC parameters $\epsilon,\delta\in(0,1)$; noise parameter $\sigma_0^2\in\mathbb{R}_{++}$; initial sample size $N_0$; batch size $N_b$; threshold $\eta$.
- $N\gets N_0$
- $D\gets (x_1,\dotsc,x_{N})\overset{\textrm{i.i.d.}}{\sim} X$
- $i\gets0$
- $\epsilon^0\gets 1$
- **while** $\epsilon^i > \epsilon$ **do**
    - $i\gets i + 1$
    - append $(x_{N+1},\dotsc,x_{N+N_b})\overset{\textrm{i.i.d.}}{\sim} X$ to $D$
    - $N\gets N+N_b$
    - $K_{\sigma_0}\gets\sigma_0^2I + K$
    - define $C:\mathcal{X}\to\mathbb{R}_{+}$ to be $C(x)=k(x,x)-k_D(x)K_{\sigma_0}^{-1}k_D(x)$;
    - Evaluate $\overline{r}$ as in (3.8)
    - $\epsilon_i \gets \frac{\bar r + \frac{2}{N}\log (\frac{\pi^2i^2}{6 \delta})}{1-F_1(1)}$, $F_1$ as in (3.7)
- **end while**
- **return** $\mathbb{1}\{C(x)\le\eta\}$
"""),
    text("p0009-b006", [71.0, 310.0, 247.0, 545.0],
         r"We use the PAC-Bayes theorem in the proof of Theorem 3.6, which asserts the validity of Algorithm 3.2. First, we construct prior and posterior stochastic estimators $C_P$ and $C_Q$, corresponding to measures $P$, $Q$ over a concept class, which admit a sublevel set of the empirical inverse Christoffel function as a central concept; namely $\bar{c}_Q=\{x:\kappa^{-1}(x) \le\eta\}$ for a given positive $\eta$. Next, we express a formula to compute the empirical stochastic risk $\hat{r}_Q$ of $C_Q$ from the data. Then, we establish a bound on the true stochastic $r_Q$ in terms of $\hat{r}_Q$ using the PAC-Bayes theorem. Finally, we prove a bound on the true risk $r(\bar{c}_Q)$ of the central concept in terms of $r_Q$. This sequence of bounds combines to yield a bound of the form (2.2) computable in terms of known data."),
    text("p0009-b007", [72.0, 553.0, 247.0, 624.0],
         r"**Theorem 3.6.** Denote $C^i$ as the inverse Christoffel function constructed during the $i$th iteration of Algorithm 3.2. We have the following PAC bound on all the inverse Christoffel functions constructed during the algorithm:"),
    text("p0009-b008", [72.0, 634.0, 247.0, 660.0],
         r"$$\begin{aligned} &\mathbb{P}(\forall i\geq1,\, P_X(\{x:C^i(x) \leq\eta\}) \geq 1-\epsilon^i)\\ &\quad \geq 1-\delta. \end{aligned}$$"),
    text("p0009-b011", [72.0, 673.0, 442.0, 695.0],
         r"Thus, with confidence $\delta$, upon the termination condition of Algorithm 3.2, we are left with a support set estimate of probability mass $\geq 1- \epsilon$."),
]

save(9, items, r"""
Compared with the 130-dpi render, a 220-dpi crop of the upper half, and 300-dpi crops of the Algorithm 3.2 box and of Theorem 3.6. First item continues the sentence from page 8 (join_previous 'space'). Theorem 3.5 and Theorem 3.6 are printed in italics with small-caps labels; written with bold labels ('**Theorem 3.5 (PAC-Bayes Theorem, adapted from [29, 17]).**', '**Theorem 3.6.**'), statements verbatim, displays as separate items. (3.2) taken from the authors' TeX and checked on the crop: $D_{ber}(\hat r_Q||r_Q) \le (D_{KL}(W_Q||W_P)+\log\frac{N+1}{\delta})/N$, outer '$\ge 1-\delta$'. Source inconsistency kept: the sentence after (3.2) prints $D_{KL}(W_P||W_Q)$ while (3.2) has $D_{KL}(W_Q||W_P)$. The display of Theorem 3.6 has NO printed equation number (it is broken over two lines in the narrow wrapped column, 'P(forall i>=1, P_X({x: C^i(x) <= eta}) >= 1 - eps^i)' / '>= 1 - delta.'); no \tag was added. (Corollary 3.11 on page 12 later refers to this bound as '(3.6)'; see the note there.) Theorem 3.6 prints 'with confidence $\delta$' (not $1-\delta$) and refers to 'Algorithm 3.2' in plain text; kept. Algorithm 3.2 is a wrapped float in the right half of the column: kept as image crop 'algorithm-3-2' (edges checked on the 300-dpi crop: top rule, caption, inputs, 14 statement lines, bottom rule; no body text inside) plus a transcription from the TeX source checked line by line against the crop, placed before the paragraph 'We use the PAC-Bayes theorem ...' so that paragraph and Theorem 3.6 read continuously. The box has no printed line numbers; the transcription has one paragraph per statement and the while-loop body is marked with '&emsp;&emsp;' (one nesting level); the long input list wraps over six printed lines and is one paragraph; 'append' and the sample tuple, and 'define C ... to be C(x) =' and its formula, are each printed on two lines and joined. Source peculiarities of the box kept as printed: the loop test uses a superscript ($\epsilon^i$, $\epsilon^0$) but the update line assigns $\epsilon_i$ with a subscript; $C(x)=k(x,x)-k_D(x)K_{\sigma_0}^{-1}k_D(x)$ has no transpose on the first $k_D(x)$; 'Evaluate' is capitalised; update line checked on the crop: $\epsilon_i \gets (\bar r + \frac{2}{N}\log(\frac{\pi^2 i^2}{6\delta}))/(1-F_1(1))$. References resolved to printed values: [29, 17], (3.2), Theorem 3.6, Algorithm 3.2, (2.2), (3.8), (3.7). Line-wrap hyphens of the narrow column removed (empir-ical, cen-tral, ex-press, us-ing, in-verse, con-structed, sup-port, in-verse). Omitted: running header (short title and page number 9).
""")
