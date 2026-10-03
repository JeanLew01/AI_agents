## Conversion notes

- Source version: arXiv:1811.03643v1 [math.OC], 8 Nov 2018 (15 pages, single-column article layout); authors H. Sartipizadeh, A. P. Vinod, B. Açıkmeşe, M. Oishi. The title printed on this version ends with 'of LTI Systems'; the paper was published at the 2019 American Control Conference (ACC) under the title 'Voronoi Partition-based Scenario Reduction for Fast Sampling-based Stochastic Reachability Computation of Linear Systems'. This package was made from the arXiv v1 PDF, not from the proceedings version, so section, equation and reference numbers are those of the arXiv version.
- Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (ACC_2019_Voronoi_arxiv.tex), with the authors' private macros expanded to standard LaTeX, and every formula was checked against the PDF pages (150 dpi page renders and 220-240 dpi crops); the TeX source and the PDF agree and no formula is kept as an image only. The superscript asterisk is written \ast throughout ($p^{\ast}$, $U^{\ast}_{K}$, ...); it is the same printed glyph.
- Equation numbers are the printed ones, (1)-(26), written with \tag. The sub-numbered groups (6a)-(6c) and (14a)-(14c), and the pair (25), (26), are printed as aligned groups and are written as one display block per number. Displays without a printed number: the MILP of Problem 2, the MILP of Problem 3, $\phi(W):=G_{w}W$ in Problem 3, $\hat{X}(\psi^{(j)})$ in Lemma 3, the final chain of inequalities in the proof of Theorem 1, and $p_{\hat{K}}^{\ast}\leq\hat{p}\leq p_{K}^{\ast}$ in Theorem 3. The optimisation problems are typeset by the authors with the optidef package ('max' with the decision variable below it and 's.t.'); they are written with \max_{...} and an aligned block.
- Theorem-like statements (Problems 1-3, Remarks 1-3, Questions 1-2, Lemmas 1-4, Theorems 1-3) are printed with a bold label and an italic body; here the label is bold and the body upright. Where a statement ends was taken from the end of the italic text / the TeX environment: Problem 1 ends after '... induced from $\mathbb{P}_X^{x_0,U}$.' (it contains (4) and (5)); Problem 2 after '... based on the probability law $\mathbb{P}_W$.'; Lemma 1 after its item 2; Lemma 2 with (12); Theorem 1 with (13); Problem 3 after '... a lower bound on the solution of Problem 2.'; Lemma 3 after '... sampled state trajectory set $\mathcal{X}_{K}^{x_0,U}$.'; Lemma 4 with (18); Theorem 2 after 'Problem 3 provides a lower bound for Problem 2.'; Theorem 3 with the chain $p_{\hat{K}}^{\ast}\leq\hat{p}\leq p_{K}^{\ast}$. Proofs start with the printed run-in 'Proof:' and end with the printed filled square, written $\blacksquare$.
- Floats: Figures 1-5 are image crops with verbatim captions. Algorithm 1 is an image crop (assets/figure/algorithm-1.jpg) followed by a text transcription. Table 1 is given as cells (assets/table/table-1.csv): in the PDF its first body cell stacks 'Algorithm 1' and three parameter settings; it is written as a label row 'Algorithm 1' with empty value cells followed by the three setting rows, which all belong to Algorithm 1; the cells are plain text and 'K̂' in them is $\hat{K}$ (the number of Voronoi cells). Reading order differs from the PDF page order for four floats: Figure 3 (printed at the top of page 9, between Theorem 2 and its proof) follows the sentence 'The buffering concept is illustrated in Figure 3.'; Figure 4 (printed at the top of page 12, in the middle of a sentence) follows the Section 5 paragraph 'We set $K=2000$ ...' that introduces it; Table 1 and Figure 5 (printed on page 13, after the Conclusion) follow the Section 5 paragraphs that cite them. Figures 1 and 2 are where the PDF prints them. The paper has one footnote, the title footnote with funding and affiliations: the PDF prints it at the bottom of page 1 (inside Section 1); here it follows the author line that carries its marker. There is no appendix and no printed page numbers.
- The text and formulas are kept as printed. The following are in the source (TeX and PDF) and are not conversion errors. (a) Theorem 1 states the event as $\{p^\ast(x_0)-p_{K}^{\ast}(x_0)\geq\delta\}$, while Question 1, equation (15), the final chain of the proof, the last sentence of the proof and the paragraph after it all use $\{p_{K}^{\ast}(x_0)-p^\ast(x_0)\geq\delta\}$ (the sampled optimum exceeding the true optimum by $\delta$). (b) In the proof of Theorem 3 the Problem 3 optimum is written $\hat{p}_{\hat{K}}^\ast$ (with a hat on $p$) and $(z^{(j)}=0)$ without a hat, while the theorem writes $p_{\hat{K}}^{\ast}$ and Problem 3 writes $\hat{z}^{(j)}$; the same proof calls $\alpha^{(j)}$ 'the set of original scenarios' and $\mathcal{J}$ 'the subset of $\mathcal{C}^\ast$'. (c) (6c) reads $\mathcal{R}=\{x|FX\leq h\}$ and the text gives $F\in\mathbb{R}^{L\times n_x}$. (d) Definition (9) quantifies '$\forall j,\ell\in\mathbb{N}_{[1,\hat{K}]}$ and $j\neq\ell$'. (e) The time index is $k$ in $w_k$, $x_k$ in Section 2.1 and $t$ in (1). (f) Two different epsilons are printed and kept: $\varepsilon^{(j)}$ is the buffer vector and $\epsilon_{\ell}^{(j)}$ are its components (notation, not a slip). (g) In Section 5: '$3\omega x$' in (23), '$\mathcal{W}_N$' for the sample set, 'exponentially increases exponentially', 'coincides the “knee”'. (h) The abstract says 'we propose a Voronoi partition-based to check' (a word is missing). The paper does not print the values of $\delta$ and $\beta$ used for $K=2000$ in Section 5.

<!-- PDF page 1 -->

# Voronoi Partition-based Scenario Reduction for Fast Sampling-based Stochastic Reachability Computation of LTI Systems

Hossein Sartipizadeh, Abraham P. Vinod, Behçet Açıkmeşe, and Meeko Oishi $^{\ast}$

Footnote $\ast$: This material is based upon work supported by the National Science Foundation, the Air Force Office of Scientific Research, and the Office of Naval Research. Hossein Sartipizadeh and Behçet Açıkmeşe were supported by Air Force Research Laboratory grant FA8650-15-C-2546 and the Office of Naval Research (ONR) Grant No. N00014-15-IP-00052. Vinod and Oishi were supported under NSF Grant Number CMMI-1254990, NSF Grant No. IIS-1528047, and AFRL Grant No. FA9453-17-C-0087. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation.

H. Sartipizadeh (corresponding author) is with University of Texas at Austin, TX, US. Email: `hsartipi@utexas.edu`.

A. Vinod and M. Oishi are with the Electrical & Computer Engineering, University of New Mexico, Albuquerque, NM, US. Email: `aby.vinod@gmail.com; oishi@unm.edu`.

B. Açıkmeşe is with the Department of Aeronautics & Astronautics in the University of Washington, Seattle, WA. Email: `behcet@uw.edu.`

## Abstract

In this paper, we address the stochastic reach-avoid problem for linear systems with additive stochastic uncertainty. We seek to compute the maximum probability that the states remain in a safe set over a finite time horizon and reach a target set at the final time. We employ sampling-based methods and provide a lower bound on the number of scenarios required to guarantee that our estimate provides an underapproximation. Due to the probabilistic nature of the sampling-based methods, our underapproximation guarantee is probabilistic, and the proposed lower bound can be used to satisfy a prescribed probabilistic confidence level. To decrease the computational complexity, we propose a Voronoi partition-based to check the reach-avoid constraints at representative partitions (cells), instead of the original scenarios. The state constraints arising from the safe and target sets are tightened appropriately so that the solution provides an underapproximation for the original sampling-based method. We propose a systematic approach for selecting these representative cells and provide the flexibility to trade-off the number of cells needed for accuracy with the computational cost.

## 1 Introduction

Reach-avoid analysis is an established verification tool for discrete-time stochastic dynamical systems, which provides probabilistic guarantees on the safety and performance [1–5]. This paper focuses on the finite time horizon *terminal* hitting time stochastic reach-avoid problem [1] (referred to here as the *terminal time problem*), that is, computation of the maximum probability of hitting a target set at the terminal time, while avoiding an unsafe set during all the preceding time steps using a controller that satisfies the specified control bounds.

The solution to the terminal time problem relies on dynamic programming [1, 6, 7], hence a variety of approximation methods have been suggested in literature. Researchers have looked for scalable approaches to solve this problem using approximate dynamic programming [8, 9], Gaussian mixtures [8], particle filters [4, 9], convex chance-constrained optimization [4], Fourier transform-based verification [10, 11], Lagrangian approaches [5], and semi-definite programming [12]. Currently, the largest system verified is a 40-dimensional chain of double integrators [10, 11] using Fourier transform-based techniques. Existing methods impose a high computational complexity which makes them unrealistic for real-time applications.

<!-- PDF page 2 -->

In this paper, we reconsider the sampling-based approach, proposed in [4]. Similar sampling-based approach has been used successfully in robotics [13] and in stochastic optimal control [14–17]. In the sampling-based stochastic reach-avoid problem, we sample the stochastic disturbance to produce a finite set of *scenarios*, and then formulate a mixed-integer linear program (MILP) to maximize the number of scenarios that satisfy the reach-avoid constraints [4, 13]. As expected, the approximated probability will converge to the true terminal time probability as the number of scenarios increases. However, the computational complexity of MILP increases exponentially with the number of binary decision variables (the number of scenarios) [18, Rem. 1] making the MILP formulation practically intractable.

The main contributions of this paper are two-fold. We first provide a lower bound on the number of scenarios needed to probabilistically guarantee a user-specified upper bound on the approximation error with a user-specified confidence level using concentration techniques. Using Hoeffding’s inequality, we demonstrate that the number of scenarios that need to be considered is inversely proportional to the square of the desired upper bound on the estimate error. Next, we propose a Voronoi-based undersampling technique that underapproximates the MILP-based solution in a computationally efficient manner. This approach allows us to partially mitigate the exponential computational complexity, and provides flexibility to select the number of partitions based on the allowable online computational complexity. We demonstrate the application of the proposed method in a problem of spacecraft rendezvous and docking.

The organization of the paper is as follows: Problem formulation and preliminary definitions are stated in Section 2. Lower bound on the required number of scenarios for the prescribed confidence level is given in Section 3. Section 4 presents the proposed partition-based method and the approximate solution reconstruction. The performance of the proposed method is investigated on a spacecraft rendezvous maneuvering and docking in Section 5.

## 2 Problem formulation

We presume $\mathbb{R}$ and $\mathbb{N}$ are sets of real and natural numbers, with $\mathbb{R}^{n}$ a length $n$ vector of real numbers, and $\mathbb{N}_{[a,b]}$ the set of natural numbers between $a$ and $b$. For $x\in\mathbb{R}^{n}$, $x^{\top}$ denotes the transpose of $x$. Vector with all elements 1 is denoted $\mathbf{1}$.

### 2.1 System description

Consider a discrete-time stochastic LTI system,

$$
x_{t+1}=Ax_t+Bu_t+w_t \tag{1}
$$

with state $x_t\in \mathcal{X}=\mathbb{R}^{n_x}$, input $u_{t}\in \mathcal{U}\subseteq\mathbb{R}^{n_u}$, disturbance $w_t\in \mathcal{W}\subseteq\mathbb{R}^{n_x}$ at time instant $t$, and matrices $A,B$ assumed to be of appropriate dimensions. We assume that $w_k$ is an independent and identically distributed (i.i.d) random variable with a PDF $\eta_{w}$. Note that we require $\eta_{w}$ only to be a probability density function from which we can draw samples, and do not require it to be Gaussian. The system (1) over a time horizon with length $N$ can be alternatively written in a “stacked” form,

$$
X(x_{0},U,W)=G_{x}x_0+G_{u}U+G_{w}W, \tag{2}
$$

with $X=[x_{1}^{\top},\cdots,x_{N}^{\top}]^\top \in \mathcal{X}^N$, $U=[u_{0}^{\top},\cdots,u_{N-1}^{\top}]^\top\in \mathcal{U}^N$, and $W=[w_{0}^{\top},\cdots,w_{N-1}^{\top}]^\top\in \mathcal{W}^N$ the concatenated state, input, and disturbance vectors over a $N$-length horizon [15]. The matrices $G_{x}$, $G_{u}$, and $G_{w}$ may be obtained from the system matrices in (1) (see [15]). Due to the stochastic nature of $w_k$, the state $x_k$ and the concatenated state vector $X$ are random. We define $\mathbb{P}_{X}^{x_0,U}$ as the probability measure associated with the random vector $X$, which is induced from the probability measure of the concatenated disturbance vector $\mathbb{P}_W$ and (2). By the i.i.d. assumption on $w_k$, $\mathbb{P}_W$ is characterized by $(\eta_{w})^N$.

<!-- PDF page 3 -->

### 2.2 Stochastic reach-avoid problem

We are interested in the terminal time problem [1]. As in [1], we seek open-loop control laws, to assure tractability (at the cost of conservativeness [4, 10, 11]). We define the *terminal time probability*, $r_{x_0}^{U}(\mathcal{S}, \mathcal{T})$, for a given initial state $x_0\in \mathcal{X}$ and an open-loop control $U\in \mathcal{U}^N$, as the probability that the state trajectory remains inside the safety set $\mathcal{S} \subseteq \mathcal{X}$ and reaches the target set $\mathcal{T} \subseteq \mathcal{X}$ at time $N$,

$$
r_{x_0}^{U}(\mathcal{S}, \mathcal{T}) = \mathbb{P}_{X}^{x_0,U}\left\{x_{N}\in \mathcal{T} \wedge x_t\in \mathcal{S},\forall t\in \mathbb{N}_{[0,N-1]}\right\}= \mathbb{P}_{X}^{x_0,U}\left\{ X\in \mathcal{R}\right\} 1_{\mathcal{S}}( x_0). \tag{3}
$$

with $\mathcal{R} = \mathcal{S}^{N-1}\times \mathcal{T}$. The stochastic reach-avoid problem is formulated as:

**Problem 1.** Open-loop terminal time problem:

$$
p^{\ast}( x_{0}) = \max_{U\in \mathcal{U}^{N}} \quad r_{x_0}^{U}(\mathcal{S}, \mathcal{T}) \tag{4}
$$

Problem 1 is equivalent to (see [1, Sec. 4]),

$$
p^{\ast}( x_{0}) = \max_{U\in \mathcal{U}^{N}} \quad 1_{\mathcal{S}}( x_0)\mathbb{E}_z^{x_0,U}\left[ z \right], \tag{5}
$$

where $z=1_{\mathcal{T}}(x_N)\prod_{t=1}^{N-1}1_{\mathcal{S}}(x_t) = 1_{\mathcal{R}}(X)$ is a Bernoulli random variable with a discrete probability measure $\mathbb{P}_z^{x_0,U}$ induced from $\mathbb{P}_X^{x_0,U}$.

**Remark 1.** In Problem 1, $p^\ast(x_0)$ is trivially zero when $x_0\not\in\mathcal{S}$, irrespective of the choice of the controller.

In [4, 13], a mixed-integer linear program (MILP) was formulated as an approximation of Problem 1 when the safe and the target sets are *polytopic*. Note that restriction of the safe and the target sets to polytopes is not severe since convex and compact sets admit tight polytopic underapproximations [19, Ex. 2.25]. We will denote the safe set $\mathcal{S}$, the target set $\mathcal{T}$, and the reach-avoid constraint set $\mathcal{R}$ as

$$
\mathcal{S}=\{x|f_{\mathcal{S}}x\leq h_{\mathcal{S}}\}, \tag{6a}
$$

$$
\mathcal{T}=\{x|f_{\mathcal{T}}x\leq h_{\mathcal{T}}\}, \tag{6b}
$$

$$
\mathcal{R}=\{x|FX\leq h\} \tag{6c}
$$

with $l_\mathcal{S},l_\mathcal{T}\in \mathbb{N}, L=(N-1)l_\mathcal{S}+l_\mathcal{T}, f_\mathcal{S}\in \mathbb{R}^{l_\mathcal{S}\times n_x}$, $f_\mathcal{T}\in \mathbb{R}^{l_\mathcal{T}\times n_x}$, and $F\in \mathbb{R}^{L\times n_x}$ is constructed using $f_{\mathcal{S}}$ and $f_{\mathcal{T}}$. Using the “big-M” approach [4, 13, 18], and a sampling-based empirical mean for $r_{x_0}^{U}(\mathcal{S}, \mathcal{T})$ that replaces $\mathcal{W}^{N}$ by a finite set of $K$ random samples,

$$
\mathcal{W}_{K}=\{W^{(1)},\cdots,W^{(K)}\}, \tag{7}
$$

we obtain a MILP approximation to Problem 1.

**Problem 2.** A MILP approximation to Problem 1 is given by

$$
\begin{aligned}
\max_{U\in\mathcal{U}^{N}} \quad & \frac{1}{K}\sum_{i=1}^{K}z^{(i)} \\
\text{s.t.} \quad & X^{(i)} = G_{x}x_{0} + G_{u} U + G_{w}W^{(i)}, \quad i\in \mathbb{N}_{[1,K]}, \\
& FX^{(i)} \leq h + M(1-z^{(i)})\mathbf{1}, \quad i\in \mathbb{N}_{[1,K]}, \\
& z^{(i)} \in\{0,1\}, \quad i\in \mathbb{N}_{[1,K]}
\end{aligned}
$$

with the optimal value denoted by $p_{K}^{\ast}(x_0)$, optimal control input $U^{\ast}_{K}$, $M \in \mathbb{R}$ some large positive number, and $W^{(i)}$ that are concatenated disturbance realizations sampled from $\mathcal{W}^N$, based on the probability law $\mathbb{P}_W$.

<!-- PDF page 4 -->

![Figure 1](../assets/s001-sartipizadeh2019voronoi/figure-1.png)

Figure 1: Sampling-based approach illustration for reach-avoid problem in 2D. Reach-avoid set $\mathcal{R}$ is distinguished with lines. Black dots and red crosses represent the sampled state trajectories corresponding to sampled disturbance $\mathcal{W}_{K}$ for a given $U$ and $x_0$ that succeed and fail to remain in $\mathcal{R}$, respectively. Empirical mean of remaining in reach-avoid set is obtained by dividing the number of samples inside $\mathcal{R}$ to the total number of samples.

As observed in [4, 13, 18], $z^{(i)}$ takes the value 1 if and only if $FX^{(i)}\leq h$ for all $i\in \mathbb{N}_{[1,K]}$. For any sampled trajectory that violates the reach-avoid constraint $X^{(j)}\in \mathcal{R},\ j\in \mathbb{N}_{[1,K]}$, we have $FX^{(j)}> h$ which is encoded by $z^{(j)}=0$ . This concept is illustrated in Figure 1; red crosses indicate the sampled trajectories which fail to remain in $\mathcal{R}$ and, therefore, their corresponding binary variables are zero. From [4], we have,

$$
\lim_{K \rightarrow \infty}p_{K}^{\ast}(x_0) = p^{\ast}(x_0). \tag{8}
$$

However, Problem 2 becomes computationally intractable for large values of $K$ since the worst-case time complexity of MILP problems exponentially increases in the number of binary decision variables [18, Rem. 1].

### 2.3 Problem statements

Based on Problem 2, we define the random vector $Z={[z^{(1)}\ \ldots\ z^{(K)}]}^\top$, the concatenation of an i.i.d process consisting of Bernoulli random variables $\{z^{(i)}\}_{i=1}^K$. By definition, the probability measure associated with $Z$ is $\mathbb{P}_{Z}^{x_0, U}=\prod_{i=1}^K\mathbb{P}_z^{x_0,U}$.

We will address the following questions:

**Question 1.** Given a violation parameter $\delta\in[0,1]$ and a risk of failure $\beta\in[0,1]$, characterize the sufficient number of scenarios $K$ to guarantee $\mathbb{P}_{Z}^{x_0, U^\ast_K}\{ p_{K}^\ast(x_0) - p^{\ast}(x_0) \geq \delta\}\leq \beta$ or equivalently $\mathbb{P}_{Z}^{x_0, U^\ast_K}\{ p^{\ast}(x_0) \geq p_{K}^\ast(x_0)-\delta \}\geq 1-\beta$, for all $x_0\in \mathcal{S}$.

**Question 2.** Given $K$ scenarios as characterized in Question 1 to meet desired specifications, construct an under-approximate MILP with $\hat{K}<K$ scenarios (hence binary decision variables) that results in the terminal time probability estimate $\hat{p}(x_0)$ with $\hat{p}(x_0)\leq p_{K}^{\ast}(x_0)$.

We will address Question 1 using Hoeffding’s inequality. By solving Question 1, we seek sufficient number of scenarios that leads to a desired upper bound on the likelihood that the approximate solution exceeds the true solution by some threshold ($\delta$). Note that a smaller $\delta$ implies less conservatism as well as higher accuracy in estimation, but requires more scenarios for a fixed $\beta$, as claimed in next section. Then we address Question 2 using Voronoi partitions to reduce the number of scenarios while preserving the original specifications $\delta$ and $\beta$.

<!-- PDF page 5 -->

### 2.4 Voronoi partition and data clustering

Here we introduce some preliminaries on Voronoi partition that we will use in the rest of this paper. Given a set of seeds (centres) $\mathcal{C}=\left\{c^{(1)},\cdots,c^{(\hat{K})}\right\}$, $c^{(i)}\in\mathbb{R}^{d}$, a Voronoi partition $\mathcal{V}(\mathcal{C})$ partitions the $\mathbb{R}^d$ space to $\hat{K}$ cells $V^{(1)},\cdots,V^{(\hat{K})}$ such that any point in $V^{(j)}$, $\forall j\in\mathbb{N}_{[1,\hat{K}]}$, is closer to $c^{(j)}$ than the other seeds. Given a set of points $\mathcal{P}=\left\{p^{(1)},\cdots,p^{(K)}\right\}$ in $\mathbb{R}^d$, we use $\mathcal{V}_{\mathcal{P}}(\mathcal{C})$ to show the partition of $\mathcal{P}$ through a Voronoi partition with seeds $\mathcal{C}$. We define each cell (may also be referred to as partition in this paper) of $\mathcal{V}_{\mathcal{P}}(\mathcal{C})$ as

$$
V^{(j)}_{\mathcal{P}}(\mathcal{C})=\{p\in \mathcal{P}|d(p,c^{(j)})\leq d(p,c^{(\ell)}), \forall j,\ell\in\mathbb{N}_{[1,\hat{K}]} \ \ \text{and}\ \ j\neq\ell \}, \tag{9}
$$

where $d(p^{(1)},p^{(2)})$ is the distance of $p^{(1)}\in \mathbb{R}^d$ from $p^{(2)}\in \mathbb{R}^d$ in any valid metric (Euclidean norm is used in this paper). We denote the number of elements in $V^{(j)}$ by $\vert V^{(j)} \vert$.

A given set $\mathcal{P}\in \mathcal{X}^K$ with $K$ points in $\mathbb{R}^d$ can be clustered in $\hat{K}$ clusters by finding a set of seeds $\mathcal{C}\in \mathcal{X}^{\hat{K}}$ that minimizes the *within-cluster sum of squares*, as proposed by $k$-means method/Lloyd’s algorithm [20]. The within-cluster sum of squares, denoted by $\mathrm{WSS}(\hat{K},\mathcal{V}_{\mathcal{P}}(\mathcal{C}))$, simply represents the total sum of squared deviations of points in cells from their seeds, i.e., given a set of points $\mathcal{P}$, a set of seeds $\mathcal{C}$, and a partition set $\mathcal{V}_{\mathcal{P}}(\mathcal{C})=\{V^{(1)},\cdots,V^{(\hat{K})}\}$,

$$
\mathrm{WSS}(\hat{K},\mathcal{V}_{\mathcal{P}}(\mathcal{C}))=\sum_{j=1}^{\hat{K}}\sum_{i=1}^{K} 1_{V^{(j)}}(p^{(i)})\|p^{(i)}-c^{(j)}\|^2. \tag{10}
$$

where $1_{V^{(j)}}(p^{(i)})$ is an indicator function which is one if $p^{(i)}$ belongs to cell $V^{(j)}$, and zero otherwise. Let

$$
\mathcal{C}^\ast=\underset{\mathcal{C}\in \mathcal{X}^{\hat{K}}}{\operatorname{arg\ min}}\ \mathrm{WSS}(\hat{K},\mathcal{V}_{\mathcal{P}}(\mathcal{C})), \tag{11}
$$

be the set of optimal seeds. Given $\mathcal{C}^\ast$, cells of $\mathcal{V}_{\mathcal{P}}(\mathcal{C}^\ast)$ represent the optimal $\hat{K}$ clusters of $\mathcal{P}$. Although solving (11) is an NP-hard problem [21], efficient algorithms exist to compute a local minima. Starting from an initial guess of $\mathcal{C}$, a successive algorithm with time complexity $\mathcal{O}(ndK\hat{K})$ for $n$ iterations can be used to update each seed by replacing it with the centroid of its cluster elements [22]. This process continues until convergence or $n$ reaches its maximum value. Note that the set of optimal seeds $\mathcal{C}^\ast$ is not necessarily a subset of $\mathcal{P}$. In addition, $\mathrm{WSS}(\hat{K},\mathcal{V}_{\mathcal{P}}(\mathcal{C}))$ is non-increasing in $\hat{K}$, and the number of required clusters can be decided by making a trade-off between $\mathrm{WSS}(\hat{K},\mathcal{V}_{\mathcal{P}}(\mathcal{C}))$ (representing accuracy) and $\hat{K}$ (representing computational complexity).

**Lemma 1.** Seed selection and Voronoi configuration are preserved under translation.

1. Let $\mathcal{C}^\ast=\{c^{(1)},\cdots,c^{(\hat{K})}\}$ be the set of $\hat{K}$ optimal seeds of $\mathcal{P}=\{p^{(1)},\cdots,p^{(K)}\}$, calculated as in (11). For any fixed vector $a$, $\mathcal{C}^{\ast}_{a}=\{a+c^{(1)},\cdots,a+c^{(\hat{K})}\}$ represents the optimal seeds of $\mathcal{P}_{a}=\{a+p^{(1)},\cdots,a+p^{(K)}\}$.
2. For any $p^{(i)}\in\mathcal{P}$, let $p^{(i)}\in V^{(j)}_{\mathcal{P}}(\mathcal{C}^{\ast})$. Then $a+p^{(i)}\in V^{(j)}_{\mathcal{P}_a}(\mathcal{C}_a^{\ast})$.

**Proof:** The proof is straight forward since both $\mathrm{WSS}$ and Voronoi partitions (as given in (10) and (9)) are functions of the relative distance of the points in each cell to their seed. $\blacksquare$

## 3 Scenarios required to meet given failure tolerance

Given i.i.d. $y^{(1)}, y^{(2)},\ldots,y^{(K)}$ for $K>0$ and $y^{(i)}\in[0,1],\ \forall i\in \mathbb{N}_{[1,K]}$ with probability measure $\mathbb{P}_y$, we define the concatenation of these random variables $Y=[y^{(1)}\ y^{(2)}\ \ldots\ y^{(K)}]^\top\in {[0,1]}^K$. The probability measure associated with $Y$ is $\mathbb{P}_Y^K=\prod_{i=1}^K \mathbb{P}_y$. We have the following inequalities from Hoeffding [23, Thm. 1].

<!-- PDF page 6 -->

**Lemma 2. (Hoeffding’s inequality)** Define $\overline{Y}=\frac{\mathbf{1}^\top Y}{K}=\frac{\sum_{i=1}^K y^{(i)}}{K}$, and $\mu_{\overline{Y}}\triangleq\mathbb{E}\left[ \overline{Y} \right]$. For any $\delta>0$,

$$
\mathbb{P}_{Y}^K\left\{ \overline{Y} - \mu_{\overline{Y}} \geq \delta \right\}\leq e^{-2K\delta^2}. \tag{12}
$$

**Theorem 1.** Given a violation parameter $\delta\in[0,1]$, risk of failure $\beta\in[0,1]$, initial state $x_0\in \mathcal{S}$, and the optimal solution $U^\ast_K\in \mathcal{U}^N$ to Problem 2, we have the risk of failure $\mathbb{P}_{Z}^{x_0, U^\ast_K}\{ p^\ast(x_0) - p_{K}^{\ast}(x_0) \geq \delta\}\leq \beta$, if

$$
K\geq \frac{-\ln(\beta)}{2\delta^2}. \tag{13}
$$

**Proof:** Let the optimal solution to Problem 1 be $U^\ast\in \mathcal{U}^N$ (which may not be equal to $U^\ast_K$). For $x_0\in \mathcal{S}$,

$$
p^\ast(x_0)= \mathbb{E}_z^{x_0,U^\ast}\left[ z \right]=\frac{\mathbb{E}_Z^{x_0,U^\ast}\left[ \mathbf{1}^\top Z \right]}{K}, \tag{14a}
$$

$$
p^\ast_K(x_0)=\frac{1}{K}\sum_{i=1}^K z^{(i)}=\frac{\mathbf{1}^\top Z}{K}\text{ under } U^\ast_K, \tag{14b}
$$

$$
\mathbb{E}_z^{x_0,U^\ast}\left[ z \right] \geq \mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right] \tag{14c}
$$

Using (14a) and (14b),

$$
\mathbb{P}_{Z}^{x_0, U^\ast_K}\{ p_{K}^{\ast}(x_0)-p^\ast(x_0) \geq \delta\} =\mathbb{P}_{Z}^{x_0, U^\ast_K}\left\{\left( \frac{1}{K}\sum_{i=1}^K z^{(i)} - \mathbb{E}_z^{x_0,U^\ast}\left[ z \right] \right) \geq \delta\right\}. \tag{15}
$$

Adding and subtracting $\mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right]$, we have

$$
\begin{aligned}
\left( \frac{1}{K}\sum_{i=1}^K z^{(i)} - \mathbb{E}_z^{x_0,U^\ast}\left[ z \right] \right) &\ = \left( \frac{1}{K}\sum_{i=1}^K z^{(i)} - \mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right] \right) +\left( \mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right] - \mathbb{E}_z^{x_0,U^\ast}\left[ z \right] \right) \\
&\ \leq \left( \frac{1}{K}\sum_{i=1}^K z^{(i)} - \mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right] \right)
\end{aligned} \tag{16}
$$

where (16) follows from (14c). Thus, $\left\{ \overline{Z}\in\{0,1\}^K: \left( \frac{\mathbf{1}^\top \overline{Z}}{K} - \mathbb{E}_z^{x_0,U^\ast}\left[ z \right]\right)\geq \delta\right\}$ is a subset of $\left\{\overline{Z}\in\{0,1\}^K: \left( \frac{\mathbf{1}^\top \overline{Z}}{K} - \mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right]\right)\geq \delta\right\}$ by (14b) and (16). Using the fact that $\mathbb{P}\{ \mathcal{S}_1\}\leq \mathbb{P}\{ \mathcal{S}_2\}$ for any two sets $\mathcal{S}_1\subseteq \mathcal{S}_2$, Hoeffding’s inequality (12), $\mathbb{E}_z^{x_0,U^\ast_K}\left[ z \right]=\frac{\mathbb{E}_Z^{x_0,U^\ast_K}\left[ \mathbf{1}^\top Z \right]}{K}$, and (15), we have

$$
\mathbb{P}_{Z}^{x_0, U^\ast_K}\{ p_{K}^{\ast}(x_0)-p^\ast(x_0) \geq \delta\} \leq\mathbb{P}_{Z}^{x_0, U^\ast_K}\left\{\left( \frac{\mathbf{1}^\top Z}{K} - \frac{\mathbb{E}_Z^{x_0,U^\ast_K}\left[ \mathbf{1}^\top Z \right]}{K} \right) \geq \delta\right\}\leq e^{-2K\delta^2}.
$$

To obtain the desired probabilistic guarantee $\mathbb{P}_{Z}^{x_0, U^\ast_K}\{ p_{K}^{\ast}(x_0)-p^\ast(x_0) \geq \delta\} \leq\beta$, we require $e^{-2K\delta^2}\leq \beta$. Solving for $K$, we obtain $K\geq \frac{-\ln(\beta)}{2\delta^2}$. $\blacksquare$

Theorem 1 addresses Question 1. Specifically, choosing at least $K$ scenarios, Theorem 1 guarantees that the probability of the event that the MILP-based estimated terminal time probability (the optimal solution to Problem 2) exceeds the true terminal time probability (the optimal solution to Problem 1) by more than $\delta$ is less than $\beta$ (a small value). Here, both $\delta$ and $\beta$ are provided by the user. Note that although $p^{\ast}$ and $p_{K}^{\ast}$ are functions of the time horizon $N$, $K$ is independent of the choice of $N$. A similar bound is used for the application of aircraft conflict detection in [24].

<!-- PDF page 7 -->

## 4 Partition-based sample reduction

As implied from the concentration probability bounds given in Theorem 1, Problem 2 typically needs a large number of samples to provide a precise approximation for Problem 1 with a small deviation $\delta$ and small risk of failure $\beta$. Therefore, solving Problem 2 can be computationally expensive or even intractable for real-time applications. In this section, we address Question 2 by proposing a *partition-based* method which provides an underapproximation to Problem 2 with flexible computational complexity, as opposed to the sampling-based approach, presented in Problem 2. To this end, we propose the following MILP problem with $\hat{K}$ binary variables, where $\hat{K}$ can be significantly smaller than $K$ and is selected by the user.

**Problem 3.** The partition-based terminal time problem is

$$
\begin{aligned}
\max_{U\in\mathcal{U}^N} \quad & \frac{1}{K}\sum_{j=1}^{\hat{K}}\alpha^{(j)}\hat{z}^{(j)} \\
\text{s.t.} \quad & \hat{X}^{(j)} = G_{x}x_{0} + G_{u} U + \psi^{(j)}, \quad j\in \mathbb{N}_{[1,\hat{K}]}, \\
& F\hat{X}^{(j)} \leq h -\varepsilon^{(j)}+ M(1-\hat{z}^{(j)})\mathbf{1}, \quad j\in \mathbb{N}_{[1,\hat{K}]}, \\
& \hat{z}^{(j)} \in\{0,1\}, \quad j\in \mathbb{N}_{[1,\hat{K}]}
\end{aligned}
$$

with the optimal value denoted by $p_{\hat{K}}^{\ast}(x_0)$. Here, $M \in \mathbb{R}$ is some large positive number, and $\psi^{(j)}$ for $j\in\mathbb{N}_{[1,\hat{K}]}$ are $\hat{K}$ selected representatives (seeds) of uncertainty, computed in a prediction mapping $\phi:\mathcal{W}^{N}\rightarrow \mathcal{X}^{N}$ with

$$
\phi(W):=G_{w}W.
$$

$\alpha^{(j)}$ is the importance rate of the $j^{th}$ seed with $\sum_{j=1}^{\hat{K}}\alpha^{(j)}=K$ and $\alpha^{(j)}\in\mathbb{N}_{[1,K]}$. For $j\in\mathbb{N}_{[1,\hat{K}]}$, $\varepsilon^{(j)}$ is an appropriately designed buffer that guarantees the solution of Problem 3 is a lower bound on the solution of Problem 2.

In Problem 3, the state uncertainty is characterized by $\hat{K}$ seeds where the $j^{th}$ seed represents $\alpha^{(j)}$ scenarios of $\mathcal{W}_{K}$. Then the reach-avoid constraints are only checked at the selected seeds instead of being checked at every scenario, which reduces the number of binary variables and constraints.

### 4.1 Seed Selection and Buffer Computation

Given a sample set $\mathcal{W}_K$, $x_{0}\in\mathcal{S}$, and $U$, we define $\mathcal{X}_{K}^{x_0,U}:=X(x_0,U,\mathcal{W}_K)$ as the set of sampled state trajectories. We desire that the elements $\mathcal{X}_{K}^{x_0,U}$ remain in reach-avoid set $\mathcal{R}$. The set $\mathcal{X}_{K}^{x_0,U}$ can be partitioned into cells, where each cell consists of some of the random state trajectories and is represented by a seed. Figure 2 shows a 2D partition with 11 seeds.

**Lemma 3.** Let $\Psi_{\hat{K}}:=\{\psi^{(1)},\cdots,\psi^{(\hat{K})}\}$ be the set of optimal seeds of $\Phi_{K}:=\phi(\mathcal{W}_{K})$ with $\phi(W):=G_{w}W$ that minimizes $\mathrm{WSS}$. Then $\hat{\mathcal{X}}_{\hat{K}}^{x_0,U}=\hat{X}(\Psi_{\hat{K}})=\{\hat{X}(\psi^{(1)}),\cdots,\hat{X}(\psi^{(\hat{K})})\}$ with

$$
\hat{X}(\psi^{(j)})=G_{x}x_{0}+G_{u}U+\psi^{(j)},
$$

represents the set of optimal seeds for sampled state trajectory set $\mathcal{X}_{K}^{x_0,U}$.

**Proof:** Results directly from Lemma 1. Since there is no uncertainty in $G_x$ and $G_u$, $G_{x}x_0+G_{u}U$ in (2) can be interpreted as a translation term. $\blacksquare$

According to Lemma 3, although the state trajectory is an optimization variable, it can be clustered through the prediction mapping $\phi(W)$ *offline*, independent of the choice of $x_0$ and $U$.

<!-- PDF page 8 -->

![Figure 2](../assets/s001-sartipizadeh2019voronoi/figure-2.png)

Figure 2: Partitioning the state uncertainty region of Figure 1 to $\hat{K}$ cells using a Voronoi partition. Larger dots indicate the selected Voronoi seeds. Samples inside each cell are closer to their own seed than other seeds.

**Lemma 4.** Let a set of points $\Phi_{K}$, a set of selected seeds $\Psi_{\hat{K}}$, as defined in Lemma 3, and their Voronoi partition $\mathcal{V}_{\Phi_{K}}(\Psi_{\hat{K}})$ with cells $V_{\Phi_K}^{(1)}(\Psi_{\hat{K}}),\cdots,V_{\Phi_K}^{(\hat{K})}(\Psi_{\hat{K}})$ be given. Then, for $j\in\mathbb{N}_{[1,\hat{K}]}$, every point $\phi\in V_{\Phi_K}^{(j)}(\Psi_{\hat{K}})$ remains in the original constraint set $FX\leq h$ if $\psi^{(j)}$, the $j^{th}$ seed, remains in the buffered constraint set $F\hat{X}(\psi^{(j)})\leq h-\varepsilon^{(j)}$ with

$$
\varepsilon^{(j)}=\left[{\epsilon_{1}^{(j)}},\cdots,{\epsilon_{L}^{(j)}}\right]^{\top}, \tag{17}
$$

and

$$
\epsilon_{\ell}^{(j)}:=\max_{\phi\in V_{\Phi_K}^{(j)}(\Psi_{\hat{K}})} \left(F_{\ell}\phi-F_{\ell}\psi^{(j)}\right), \qquad \ell\in\mathbb{N}_{[1,L]}. \tag{18}
$$

**Proof:** From (18) we conclude that for all $\ell\in\mathbb{N}_{[1,L]}$, $j\in\mathbb{N}_{[1,\hat{K}]}$,

$$
F_{\ell}\phi\leq F_{\ell}\psi^{(j)}+\epsilon_{\ell}^{(j)} \qquad \forall \phi\in V_{\Phi_K}^{(j)}(\Psi_{\hat{K}}). \tag{19}
$$

By adding $F_{\ell}\left(G_{x}x_0+G_{u}U\right)$ to the right and left sides of (19), we have

$$
F_{\ell}\left(G_{x}x_0+G_{u}U+\phi\right)\leq F_{\ell}\left(G_{x}x_0+G_{u}U+\psi^{(j)}\right)+\epsilon_{\ell}^{(j)}. \tag{20}
$$

Consequently, for all $\phi\in V_{\Phi_K}^{(j)}(\Psi_{\hat{K}})$, the following holds for any initial state and input trajectory,

$$
F_{\ell}X(x_0,U,\phi)\leq F_{\ell}\hat{X}(x_{0},U,\psi^{(j)})+\epsilon_{\ell}^{(j)}. \tag{21}
$$

Denoting $F_{\ell}X(x_0,U,\phi)$ and $F_{\ell}\hat{X}(x_0,U,\psi^{(j)})$ with $F_{\ell}X(\phi)$ and $F_{\ell}\hat{X}(\psi^{(j)})$, when $F_{\ell}\hat{X}(\psi^{(j)})\leq h_{\ell}-\epsilon_{\ell}^{(j)}$, it is concluded from (21) that $F_{\ell}X(\phi)\leq h_{\ell}$, $\forall \phi\in V_{\Phi_K}^{(j)}(\Psi_{\hat{K}})$. Since (21) is valid for all $\ell\in\mathbb{N}_{[1,L]}$ and $j\in\mathbb{N}_{[1,\hat{K}]}$, the proof is completed. $\blacksquare$

The buffering concept is illustrated in Figure 3.

**Remark 2.** Computing $\epsilon_{\ell}^{(j)}$ for $\ell=1,\cdots,L$ and $j\in \mathbb{N}_{[1,\hat{K}]}$ is a sorting problem in 1D and can be executed by worst time complexity of $\mathcal{O}(\sum_{j=1}^{\hat{K}}\alpha^{(j)} \log \alpha^{(j)})$.

**Theorem 2.** Let $\Phi_{K}$ be a set of $K$ disturbance samples mapped through the prediction mapping $\phi(W):=G_{w}W$ and let $\Psi_{\hat{K}}$ be a set of selected seeds. Let $\alpha^{(j)}=\vert V_{\Phi_{K}}^{(j)}(\Psi_{\hat{K}})\vert$, $j\in\mathbb{N}_{[1,\hat{K}]}$, denote the number of elements of $V_{\Phi_{K}}^{(j)}(\Psi_{\hat{K}})$ and define $\varepsilon^{(j)}$ as in Lemma 4. Problem 3 provides a lower bound for Problem 2.

<!-- PDF page 9 -->

![Figure 3](../assets/s001-sartipizadeh2019voronoi/figure-3.png)

Figure 3: Buffering process. Cell $V^{(j)}$ is shown in green. If $X(\psi^{(j)})$, the state trajectory corresponding to the seed of $V^{(j)}$, remains in the buffered constraint $F_{\ell}X^{(j)}\leq h_{\ell}-\epsilon_{\ell}^{(j)}$, the state trajectory of every sample in $V^{(j)}$ will satisfy the original constraint $F_{\ell}X\leq h_{\ell}$.

**Proof:** According to the definition of the buffers, if seed $\hat{X}(\psi^{(j)})$, $\forall j\in\mathbb{N}_{[1,\hat{K}]}$, remains in the buffered constraint set, all $\alpha^{(j)}$ points of cell $V_{\Phi_{K}}^{(j)}(\Psi_{\hat{K}})$ remain in the original constraint set. Otherwise, at most $\alpha^{(j)}$ samples belonging to cell $V_{\Phi_{K}}^{(j)}(\Psi_{\hat{K}})$ may violate the original constraints. Since in Problem 3 the worst case is considered by weighting the $j^{th}$ seed with $\alpha^{(j)}$, $p^{\ast}_{\hat{K}}$ provides a lower bound on $p^{\ast}_{K}$. $\blacksquare$

**Remark 3.** If initial state $x_{0}\in\mathcal{S}$ is uncertain, the proposed method can be applied by defining $\phi(x_0,W):=G_{x} x_{0}+G_{w}W$.

Obviously, having more cells results in a higher accuracy and when number of cells tends to the number of samples, $p^{\ast}_{\hat{K}}$ tends to $p^{\ast}_{K}$. However, this improved accuracy comes at a higher computational cost. We thus have to select $\hat{K}$ by trading off accuracy and computational cost.

### 4.2 Tightening the Voronoi-based terminal time probability estimate

Given $U_{\hat{K}}^{\ast}$ obtained from Problem 3, a tighter underapproximation on $p^{\ast}_{K}$ can be recalculated by simply checking the percentage of the original $K$ sampled trajectories that remain in reach-avoid set $\mathcal{R}$, after applying $U_{\hat{K}}^{\ast}$ to the stochastic system. In contrast to solving a large MILP (as done in Problem 2) whose computational complexity grows exponentially with $K$, this improved estimate (see (22)) is obtained by a policy evaluation that has a computational complexity of $\mathcal{O}(K)$. The following theorem presents the probability underapproximation proposed in this paper.

**Theorem 3.** Let $p_{K}^{\ast}$ and $p_{\hat{K}}^{\ast}$ be the optimal values of Problem 2 and Problem 3, respectively, with corresponding optimal solutions $U_{K}^{\ast}$ and $U_{\hat{K}}^{\ast}$. Define $\hat{p}$ as

$$
\hat{p}=\frac{1}{K}\sum_{i\in\mathbb{N}_{[1,K]}} 1_{\mathcal{R}}\left(X(x_{0},U^{\ast}_{\hat{K}},W^{(i)})\right). \tag{22}
$$

Then

$$
p_{\hat{K}}^{\ast}\leq \hat{p}\leq p_{K}^{\ast}.
$$

**Proof:** i) Since $p^{\ast}_{K}$ is the optimal terminal time probability with $K$ samples and $\hat{p}$ is the evaluation of an open-loop controller $U_{\hat{K}}^\ast$ over these $K$ samples, we conclude that $\hat{p}\leq p_{K}^{\ast}$. Equality holds if $U_{\hat{K}}^{\ast}=U_{K}^{\ast}$.

<!-- PDF page 10 -->

ii) Let $\mathcal{J}=\{j\in\mathbb{N}_{[1,\hat{K}]}|\hat{z}^{(j)}=1\}$, the subset of $\mathcal{C}^\ast$ which were deemed safe by Problem 3. By definition of $\alpha^{(j)}$, $\sum_{\{i\in \mathbb{N}_{[1,K]}: W^{(i)}\in V^{(j)}\}} 1_{\mathcal{R}}\left(X(x_{0},U^{\ast}_{\hat{K}},W^{(i)})\right) = \sum_{\{i\in \mathbb{N}_{[1,K]}: W^{(i)}\in V^{(j)}\}} 1$ for every $j\in \mathcal{J}$. In other words, since $\alpha^{(j)}$ is the set of original scenarios that fall in the $j^\mathrm{th}$ cell, whenever the solution of Problem 3 deems the representative seed safe, all the scenarios within it are safe. Thus, we have $\hat{p}$ at least as big as $\frac{1}{K}\sum_{j\in \mathcal{J}}\alpha^{(j)}=\hat{p}_{\hat{K}}^\ast$ since there might be other cells that were not deemed safe by Problem 3 $(z^{(j)}=0)$ but contains scenarios that might be safe $\left(1_{\mathcal{R}}\left(X(x_{0},U^{\ast}_{\hat{K}},W^{(i)})\right)=1\right)$. Hence, $\hat{p}\geq \hat{p}_{\hat{K}}^\ast$. $\blacksquare$

### 4.3 Implementation

![Algorithm 1](../assets/s001-sartipizadeh2019voronoi/algorithm-1.png)

**Algorithm 1** Proposed Voronoi-based reach-avoid solution

**Input:** LTI system (1), safe set $\mathcal{S}$, target set $\mathcal{T}$, initial state $x_0$.

**Offline (independent of $x_0$):**

&emsp;&emsp;**1.** Generate $\mathcal{W}_{K}$ by taking $K$ i.i.d. samples from $(\eta_{w})^{N}$.

&emsp;&emsp;**2.** Construct $\Phi_{K}=\phi(\mathcal{W}_{K})$ with $\phi(W):=G_{w}W$.

&emsp;&emsp;**3.** Select $\hat{K}$ based on the required time complexity or from the $\mathrm{WSS}$ vs. $\hat{K}$ curve.

&emsp;&emsp;**4.** Compute $\Psi_{\hat{K}}$, the optimal $\hat{K}$ seeds of $\Phi_{K}$, by a clustering method.

&emsp;&emsp;**5.** Determine $\mathcal{V}_{\Phi_{K}}(\Psi_{\hat{K}})$ with cells $V_{\Phi_{K}}^{(1)}(\Psi_{\hat{K}}),\cdots,V_{\Phi_{K}}^{(\hat{K})}(\Psi_{\hat{K}})$ from (9).

&emsp;&emsp;**6.** Compute importance rate vector $\alpha=\{\alpha^{(1)},\cdots,\alpha^{(\hat{K})}\}$ with $\alpha^{(j)}$ the number of elements of $V_{\Phi_{K}}^{(j)}(\Psi_{\hat{K}})$ for $j\in\mathbb{N}_{[1,\hat{K}]}$.

&emsp;&emsp;**7.** Compute $\varepsilon^{(j)}$ for $j\in\mathbb{N}_{[1,\hat{K}]}$ using Lemma 4.

**Online (depends on $x_0$):**

&emsp;&emsp;**1.** Solve Problem 3 for $U^{\ast}_{\hat{K}}$.

&emsp;&emsp;**2.** Compute $\hat{p}$ from (22).

**Output:** $\hat{p}$.

Algorithm 1 describes the proposed Voronoi-based method to solve the open-loop terminal time problem. Given a sample set $\mathcal{W}_K$ with $K$ random samples directly drawn from $(\eta_{w})^{N}$, one can construct $\phi(\mathcal{W}_K)$ and find its optimal $\hat{K}$ seeds. The $k$-means method can be used to find the seeds of a Voronoi partition as explained in Section 2.4. In addition, in order to determine the number of required seeds, $\mathrm{WSS}$ can be used as a measure of variability of points in a cluster. A smaller $\mathrm{WSS}$ implies more compact clusters which reduces the size of defined buffers $\varepsilon^{(1)},\cdots,\varepsilon^{(\hat{K})}$ and the average number of samples in each cell. Note that by increasing $\hat{K}$, clusters become smaller and the precision of Problem 3 grows. However, eventually, the improvement precision is insignificant compared to the imposed computational complexity. Therefore, we compute WSS as a function of $\hat{K}$, to explore this trade-off. We propose that the “knee” of the curve provides an efficient compromise between precision and computational complexity. It is shown experimentally in the next section that the knee of $\mathrm{WSS}$ vs. $\hat{K}$ curve can be a good representative of the knee on the $\hat{p}$ vs. $\hat{K}$. As a result, $\hat{K}$ can be computed and selected in advance.

After selecting $\hat{K}$ based on the required running time for the real-time process or based on the $\mathrm{WSS}$ vs. $\hat{K}$, one can compute the Voronoi-based partition and the number of elements in each cell, and then

<!-- PDF page 11 -->

compute the buffers from Lemma 4. All these steps are executed offline (independent of $x_0$), while solving Problem 3 and probability reconstruction using (22) is done online (dependent on $x_0$).

## 5 Illustrative Example: Spacecraft Rendezvous

We consider the spacecraft rendezvous example discussed in [4]. In this example, two spacecraft are in the same elliptical orbit. One spacecraft, referred to as the deputy, must approach and dock with another spacecraft, referred to as the chief, while remaining in a line-of-sight cone, in which accurate sensing of the other vehicle is possible. The relative dynamics are described by the Clohessy-Wiltshire-Hill (CWH) equations as given in [25],

$$
\ddot{x} - 3 \omega x - 2 \omega \dot{y} = m_{d}^{-1}F_{x},\qquad\ddot{y} + 2 \omega \dot{x} = m_{d}^{-1}F_{y}. \tag{23}
$$

The position of the deputy is denoted by $x,y \in \mathbb{R}$ when the chief, with the mass $m_d=300$ kg, is located at the origin. For the gravitational constant $\mu$ and the orbital radius of the spacecraft $R_{0}$, $\omega = \sqrt{\mu/R_{0}^{3}}$ represents the orbital frequency. In this example, the spacecraft is in a circular orbit at an altitude of 850 km above the earth.

We define $\zeta = [x,y,\dot{x},\dot{y}] \in \mathbb{R}^{4}$ as the system state and $u = [F_{x},F_{y}] \in \mathcal{U}\subseteq\mathbb{R}^{2}$ as the system input, then discretize the dynamics (23) with a sampling time of 20 s to obtain the discrete-time LTI system,

$$
\zeta_{t+1} = A \zeta_{t} + B u_{t} + w_{t}. \tag{24}
$$

The additive stochastic noise, modeled by the Gaussian i.i.d. disturbance $w_{t} \in \mathbb{R}^{4}$, with $\mathbb{E}[w_{t}] = 0$, and $\mathbb{E}[w_{t}w_{t}^\top] = 10^{-4}\times\text{diag}(1, 1, 5 \times 10^{-4}, 5 \times 10^{-4})$, accounts for disturbances and model uncertainty.

We define the target set and the safe set as in [4],

$$
\mathcal{T} = \left\{ \zeta \in \mathbb{R}^{4}: |\zeta_{1}| \leq 0.1, -0.1 \leq \zeta_{2} \leq 0, |\zeta_{3}| \leq 0.01, |\zeta_{4}| \leq 0.01 \right\}, \tag{25}
$$

$$
\mathcal{S} = \left\{\zeta \in \mathbb{R}^{4}: |\zeta_{1}| \leq \zeta_{2}, -1\leq \zeta_{2}, |\zeta_{3}| \leq 0.05, |\zeta_{4}| \leq 0.05 \right\}, \tag{26}
$$

with a horizon of $N = 5$. We consider the initial position $x=y=-0.75$ km, the initial velocity $\dot{x}=\dot{y}=0$ km/s and $\mathcal{U} = [-0.1, 0.1]\times [-0.1, 0.1]$. The terminal time probability for this problem using existing approaches [4, 10] is known to be 0.86, which we assume to be the best open-loop controller-based reach-avoid probability estimate.

We set $K=2000$ as the number of original samples to estimate the terminal time probability, with guarantees afforded by Theorem 1, and run 100 random experiments in which in each experiment $\mathcal{W}_N$ is generated randomly. Simulations are carried out using CVX [26] on a 2.8 GHz processor Intel Core i5 with 16 GB RAM. Figure 4a shows the $\mathrm{WSS}$ curve (mean value and standard deviation of the results of the 100 experiments) with up to 100 cells. Figure 4b shows the terminal time probability approximation provided by Algorithm 1. As proposed, the “knee” of Figure 4a coincides the “knee” of Figure 4b; improvements in the accuracy of Algorithm 1 are insignificant beyond $\hat{K}=20$. In practice, $\hat{K}$ can be selected from one single experiment in which $WSS$ is calculated for a random disturbance set $\mathcal{W}_K$ for up to 100 (maximum allowable) cells. The computation of $\mathrm{WSS}$ curve shown in Figure 4a, for one experiment using $k$-means method, took only about 2.68 s, hence is reasonable for *offline* computation to select $\hat{K}$. The reported time includes the computation time for solving 100 $k$-means with 1 to 100 cells. This time, which is associated with offline step, can be further reduced by changing the step size of $\hat{K}$ variation (horizontal axis) or calculating $\mathrm{WSS}$ for arbitrary $\hat{K}$s (e.g. finer steps at the beginning and coarser steps at the end). The run time for the online component of Algorithm 1 is shown in Figure 4c. Since Problem 3 is a mixed-integer linear program, the time complexity exponentially increases exponentially with the number of cells [18, Rem. 1].

We see in Figure 4b, that partitions with 20 to 40 cells provide a reasonable estimate of the terminal time probability, without significant loss of precision. The computed terminal time probability and the

<!-- PDF page 12 -->

mean value of the online run time for $\hat{K}=20$, 40 and 100 are reported in Table 1. As desired, Algorithm 1 provides a flexible trade-off between the accuracy and computation time by selecting a suitable partition, and can be significantly faster than the existing Fourier transform approach [10] and particle filter [4, 13] (which fails to deal with large $K$s due to the exponential complexity of MILP problem).

Figure 5 shows the position trajectory, associated with $\zeta_1$ and $\zeta_2$, obtained by the Fourier method [10] (blue dots) and the proposed Voronoi partition-based method (green stars) with 40 cells. Green regions show the uncertainty regions of Voronoi method at different time instants obtained by 2000 original scenarios.

![Figure 4](../assets/s001-sartipizadeh2019voronoi/figure-4.png)

Figure 4: Mean and standard deviation of (a) within-cluster sum of squares (used to select $\hat{K}$, offline) (b) terminal time probability (c) online run time with increasing number of cells $\hat{K}$, obtained from 100 experiments with 2000 original scenarios.

## 6 Conclusion

In this paper we presented a novel partition-based method for under-approximating the terminal time probability through sample reduction. By using Hoeffding’s inequality, we provided a bound on the required number of scenarios to achieve a desired probabilistic bound on the approximation error. Furthermore, we proposed a method which clusters the taken scenarios in few cells, each cell represented by a seed, where the number of cells is selected by the user in a systematic manner using the trend of a given curve or based on the desired running time. The proposed method scales easily with dimension since the clustering computational complexity increases linearly with the dimension of data. In addition, the simulation results confirm that the proposed method significantly decrease the running time, and therefore, it can be easily applied to real-time systems.

<!-- PDF page 13 -->

[Table 1](s001-sartipizadeh2019voronoi/table-1.csv)

Table 1: Terminal reach-avoid probability estimate and computation time of existing methods and Algorithm 1

![Figure 5](../assets/s001-sartipizadeh2019voronoi/figure-5.png)

Figure 5: Position trajectory for Fourier algorithm given in [10] and the proposed Voronoi partition-based method with 40 cells.

<!-- PDF page 14 -->

## References

[1] S. Summers and J. Lygeros, “Verification of discrete time stochastic hybrid systems: A stochastic reach-avoid decision problem,” *Automatica*, vol. 46, no. 12, pp. 1951–1961, 2010.

[2] B. HomChaudhuri, A. P. Vinod, and M. Oishi, “Computation of forward stochastic reach sets: Application to stochastic, dynamic obstacle avoidance,” in *American Control Conf.*, Seattle, WA, 2017.

[3] N. Malone, K. Lesser, M. Oishi, and L. Tapia, “Stochastic reachability based motion planning for multiple moving obstacle avoidance,” in *Proc. Hybrid Syst.: Comput. and Ctrl.*, 2014, pp. 51–60.

[4] K. Lesser, M. Oishi, and R. S. Erwin, “Stochastic reachability for control of spacecraft relative motion,” in *Proc. IEEE Conf. Dec. & Ctrl.* IEEE, 2013, pp. 4705–4712.

[5] J. Gleason, A. Vinod, and M. Oishi, “Underapproximation of reach-avoid sets for discrete-time stochastic systems via Lagrangian methods,” in *IEEE Conf. Dec. Ctrl.*, 2017. [Online]. Available: https://arxiv.org/abs/1704.03555.

[6] A. Abate, M. Prandini, J. Lygeros, and S. Sastry, “Probabilistic reachability and safety for controlled discrete time stochastic hybrid systems,” *Automatica*, vol. 44, no. 11, pp. 2724–2734, 2008.

[7] A. Abate, S. Amin, M. Prandini, J. Lygeros, and S. Sastry, “Computational approaches to reachability analysis of stochastic hybrid systems,” in *Proc. Hybrid Syst.: Comput. and Ctrl.*, 2007, pp. 4–17.

[8] N. Kariotoglou, K. Margellos, and J. Lygeros, “On the computational complexity and generalization properties of multi-stage and stage-wise coupled scenario programs,” *Syst. and Ctrl. Lett.*, vol. 94, pp. 63–69, 2016.

[9] G. Manganini, M. Pirotta, M. Restelli, L. Piroddi, and M. Prandini, “Policy search for the optimal control of Markov Decision Processes: A novel particle-based iterative scheme,” *IEEE Trans. Cybern.*, pp. 1–13, 2015.

[10] A. Vinod and M. Oishi, “Scalable Underapproximation for the Stochastic Reach-Avoid Problem for High-Dimensional LTI Systems Using Fourier Transforms,” *IEEE Ctrl. Syst. Letters.*, vol. 1, no. 2, pp. 316–321, 2017.

[11] ——, “Scalable underapproximative verification of stochastic LTI systems using convexity and compactness,” in *Proc. Hybrid Syst.: Comput. and Ctrl.*, 2018, pp. 1–10.

[12] D. Drzajic, N. Kariotoglou, M. Kamgarpour, and J. Lygeros, “A semidefinite programming approach to control synthesis for stochastic reach-avoid problems,” in *Int’l Workshop on Applied Verification for Continuous and Hybrid Syst.*, 2016, pp. 134–143.

[13] L. Blackmore, M. Ono, A. Bektassov, and B. C. Williams, “A probabilistic particle-control approximation of chance-constrained stochastic predictive control,” *IEEE Trans. Robot.*, vol. 26, no. 3, pp. 502–517, 2010.

[14] H. Sartipizadeh and T. L. Vincent, “A new robust mpc using an approximate convex hull,” *Automatica*, 2018.

[15] H. Sartipizadeh and B. Açıkmeşe, “Approximate convex hull based sample truncation for scenario approach to chance constrained trajectory optimization,” in *Proc. American Ctrl. Conf.*, 2018, pp. 4700–4705.

<!-- PDF page 15 -->

[16] G. C. Calafiore and L. Fagiano, “Stochastic model predictive control of LPV systems via scenario optimization,” *Automatica*, vol. 49, no. 6, pp. 1861–1866, 2013.

[17] G. C. Calafiore and M. C. Campi, “The scenario approach to robust control design,” *IEEE Trans. Autom. Ctrl.*, vol. 51, no. 5, pp. 742–753, May 2006.

[18] A. Bemporad and M. Morari, “Control of systems integrating logic, dynamics, and constraints,” *Automatica*, vol. 35, no. 3, pp. 407–427, 1999.

[19] S. Boyd and L. Vandenberghe, *Convex optimization*. Cambridge Univ. Press, 2004.

[20] J. A. Hartigan, *Clustering algorithms*. Wiley, 1975.

[21] D. Aloise, A. Deshpande, P. Hansen, and P. Popat, “NP-hardness of euclidean sum-of-squares clustering,” *Machine Learning*, vol. 75, no. 2, pp. 245–248, May 2009. [Online]. Available: https://doi.org/10.1007/s10994-009-5103-0

[22] J. A. Hartigan and M. A. Wong, “Algorithm as 136: A k-means clustering algorithm,” *J. Royal Statistical Society. Series C (Applied Statistics)*, vol. 28, no. 1, pp. 100–108, 1979.

[23] W. Hoeffding, “Probability Inequalities for Sums of Bounded Random Variables,” *J. Amer. Statistical Asso.*, vol. 58, no. 301, pp. 13–30, 1963.

[24] M. Prandini, J. Hu, J. Lygeros, and S. Sastry, “A probabilistic approach to aircraft conflict detection,” *IEEE Trans. Intelligent Transportation Syst.*, vol. 1, no. 4, pp. 199–220, 2000.

[25] W. E. Weisel, *Spaceflight dynamics*. New York, McGraw-Hill Book Co, 1989, vol. 2.

[26] M. Grant and S. Boyd, “CVX: Matlab software for disciplined convex programming, version 2.1,” http://cvxr.com/cvx, Mar. 2014.
