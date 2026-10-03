from pagelib import *

items = [
    running_header(3),
    text("p0003-symbols-head", [90.0, 96.0, 435.0, 113.0],
         "**symbol** — **definition**"),
    text("p0003-symbols-reach", [90.0, 113.0, 435.0, 214.0], r"""
*Reachability Analysis*

- $\Phi(t_1;t_0,x_0,d)$ — State transition function, evolving a state $x_0$ at time $t_0$ under disturbance $d$ to a state at time $t_1$
- $\mathcal{X}_0$ — Set of initial states
- $\mathcal{D}$ — Set of disturbances
- $t_0,t_1$ — Initial and final times
- $R_{[t_0,t_1]}$ — Forward reachable set
- $\hat{R}_{[t_0,t_1]}$ — Approximation of forward reachable set
"""),
    text("p0003-symbols-prob", [90.0, 214.0, 435.0, 531.0], r"""
*Probability, Statistical Learning Theory*

- $\mathbb{E}\left[\cdot\right]$ — Expected value of a random variable
- $\mathbb{P}\left(\cdot\right)$ — Probability of an event defined in terms of random variables
- $D_{KL}(P||Q)$ — Kullback-Leibler (KL) divergence from $P$ to $Q$
- $D_{ber}(p||q)$ — KL divergence between Bernoulli distributions with parameters $p$ and $q$
- $X$ — Random variable whose support we wish to estimate
- $F_1$ — CDF of the chi-square distribution with 1 degree of freedom
- $\mathcal{X}$ — Domain of $X$
- $P_X$ — Probability measure of the distribution of $X$
- $P_X^N$ — Probability measure of $N$ iid samples from $X$
- PAC — Probably Approximately Correct
- iid — Independent and Identically Distributed
- $\epsilon$,$\delta$ — accuracy and confidence parameters in PAC guarantees
- $\mathcal{C}$ — Concept class
- $\bar{c}_Q$ — “central concept” of the posterior measure $Q$
- $P$,$Q$ — Prior and posterior probability measures on $\mathcal{C}$
- $W_P$, $W_Q$ — Parametric representations of $P$ and $Q$
- $C_P$, $C_Q$ — Stochastic estimators: random variables on $\mathcal{C}$ distributed according to $P$, $Q$
- $\ell(c,x)$ — statistical loss function comparing a concept $c$ and a datum $x$
- $r(c)$ — risk: average of $\ell(c,x)$ for $x\sim X$
- $\hat{r}(c)$ — empirical estimate of $r(c)$ from data $x_1,\dotsc,x_N$
- $r_Q$ — stochastic risk: average of $\ell(c,x)$ for $x\sim X$, $c\sim Q$
- $\hat{r}_Q$ — empirical estimate of $r_Q$ from data $x_1,\dotsc,x_N$
"""),
    text("p0003-symbols-cfun", [90.0, 531.0, 435.0, 646.0], r"""
*Christoffel Functions*

- $M_m$, $\hat{M}_m$ — Matrix of moments of degree $\le m$ and its empirical estimate
- $\hat{M}_{m,\sigma_0}$ — Empirical moment matrix with diagonals modified by $\sigma_0$
- $z_m(x)$ — vector of monomials with degree $\le m$ evaluated at point $x$
- $\hat{\kappa}^{-1}(x)$ — Polynomial empirical inverse Christoffel function evaluated at $x$
- $\hat{\kappa}^{-1}(x)$ — kernelized empirical inverse Christoffel function
- $C(x)$ — Christoffel-based support set estimator, output of Algorithms 3.1,3.2, and 3.3
"""),
    text("p0003-symbols-gp", [90.0, 646.0, 435.0, 737.0], r"""
*Gaussian Processes*

- $m$, $k$ — prior mean and covariance functions
- $m_q$, $k_q$ — posterior mean and covariance functions
- $K$ — kernel Gramian matrix, $K_{ij}=k(x_i,x_j)$
- $k_D$ — vector of kernel evaluations on data, $(k_D(x))_i=k(x_i,x)$
- $\mathcal{N}\left(\mu,\Sigma\right)$ — Multivariate normal with mean $\mu$ and covariance $\Sigma$
- $\mathcal{GP}(m,k)$ — Gaussian process with mean and covariance functions $m$, $k$
"""),
]

save(3, items, """
The page is the unnumbered two-column list 'symbol / definition' of Section 1.1 (a ruled tabular without table number or caption), in four groups with italic group titles. It is transcribed as text, one list line per printed row in the form 'symbol — definition' (the dash stands for the column gap and is not printed); the extractor's image-fallback table item was replaced, because LaTeX symbols are not usable in CSV cells and the '||' of the KL-divergence symbols would break a Markdown table. Symbols taken from the authors' TeX with macros expanded and every row compared with the 130-dpi render: 6 + 22 + 6 + 6 = 40 rows, same order as printed. As printed, the polynomial and the kernelized empirical inverse Christoffel function are both listed with the same symbol $\\hat{\\kappa}^{-1}(x)$ (in the body the kernelized one is written $\\kappa^{-1}(x)$, eq. (2.6)), and the last Christoffel row prints 'Algorithms 3.1,3.2, and 3.3' without a space after the first comma. Capitalisation of the definitions is inconsistent in the source and kept. Line-wrap hyphens inside cells removed (un-der, param-eters, Algo-rithms). Omitted: running header (short title and page number 3).
""")
