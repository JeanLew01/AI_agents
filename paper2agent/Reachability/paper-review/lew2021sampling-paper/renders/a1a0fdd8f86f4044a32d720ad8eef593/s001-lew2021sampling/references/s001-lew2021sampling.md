## Conversion notes

- Source version: arXiv:2008.10180v2 [eess.SY], 8 Nov 2020 (16 pages, single column: main text pp. 1-8, acknowledgments and references pp. 9-11, appendices A-D pp. 11-16); authors T. Lew and M. Pavone. The page footer names the venue, 4th Conference on Robot Learning (CoRL 2020), Cambridge MA, USA (proceedings: PMLR, 2021). This package was made from the arXiv v2 PDF, not from the PMLR proceedings file.
- Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (Lew.Pavone.CoRL20.tex, preamble.tex), with the authors' private macros expanded to standard LaTeX (bold symbols as \boldsymbol{...}, \mathcal{X}, \mathbb{W}, \mathbb{P}, ...), and every formula was checked against the PDF pages on 220-260 dpi renders; TeX source and PDF agree and no formula is kept as an image only. Equation numbers (1)-(22), including (19a)-(19c), are the printed ones and are given with \tag; the other displays are unnumbered in the paper.
- Algorithm 1 (randUP, Section 3) and Algorithm 2 (robUP!, Section 4) are each given as an image crop (assets/figure/algorithm-1.jpg, algorithm-2.jpg) followed by a line-by-line transcription with the printed line numbers; the printed titles read 'Alg. 1.' / 'Alg. 2.'. The printed pseudocode has no 'end for': in Algorithm 2, lines 4-7 are the indented body of the for-loop of line 3 and line 8 (return) is outside it.
- Theorem 1, Theorem 2 (stated in Section 3 and restated verbatim in Appendix A), Definition 1, Definition 2 and the proof carry their printed labels in bold; theorem bodies are printed in italics, which is not reproduced. Conditions (C1) and (C2) of Theorem 1 are equations (3) and (4).
- Figures 1-6 are main-text image crops (assets/figure/). Figures 7-10 are printed in Appendix B and are stored as supplementary figures (assets/supp_figs/supplementary-figure-7 ... -10) with their printed labels 'Figure 7' ... 'Figure 10'. Figure 5 is an L-shaped arrangement of three plots, a small table and the caption; it is one crop that therefore also shows the printed caption, and the embedded table is additionally transcribed (assets/table/figure-5-table.csv). The paper has no numbered tables. Floats that are printed inside a paragraph (Figures 1, 6, 8, 10, Algorithm 1) are placed after that paragraph; Footnote 1 (code URL) is placed directly after the abstract that cites it, Footnotes 2-5 at the end of their pages' text.
- The text and formulas are kept as printed. The following are in the source (PDF and TeX) and are not conversion errors: Definition 1 writes the intersection with calligraphic $\mathcal{K}$ but quantifies over 'every compact set $K$'; the sampled tuples live in $\mathcal{X}_0\times\mathcal{U}^{k-1}\times\Theta\times\mathbb{W}^{k-1}$ in Section 3 and Theorem 2, in $\mathcal{X}_0\times\mathcal{U}^{N}\times\Theta\times\mathbb{W}^{N-1}$ in the description of Algorithm 1, and in $\mathcal{Z}=\mathcal{X}_0\times\mathcal{U}^{k}\times\Theta\times\mathbb{W}^{k-1}$ in Section 4 and in the proof; equation (2) lists the index range $i=1,\ldots,k-1$ although $\boldsymbol{u}_0,\boldsymbol{w}_0$ appear; the definition of $\boldsymbol{x}_k(\boldsymbol{z})$ after (5) ends with an extra ')'; the table in Figure 5 has columns $\mathcal{X}_0,\mathcal{X}_1,\mathcal{X}_2,\mathcal{X}_4,\mathcal{X}_5$; in Section 6 the disturbance bounds are given 'for $i=1,\ldots,13$' and 'for $i=4,5,6$' and the discretised dynamics use $\boldsymbol{\theta}_k$; in Appendix C.1, $\boldsymbol{Q}_{\mathrm{nom},k}=\boldsymbol{h}\boldsymbol{Q}_k\boldsymbol{h}^T$, the placement of the square in (14) and the unmatched parenthesis in the definition of $c$; in (17), $\Gamma(n/2+2)$; spellings 'innacuracies', 'anynomous', 'news avenues', 'vizualize', 'conludes'.

<!-- PDF page 1 -->

# Sampling-based Reachability Analysis: A Random Set Theory Approach with Adversarial Sampling

**Thomas Lew, Marco Pavone**

Department of Aeronautics and Astronautics  
Stanford University, United States  
`{thomas.lew,pavone}@stanford.edu`

## Abstract

Reachability analysis is at the core of many applications, from neural network verification, to safe trajectory planning of uncertain systems. However, this problem is notoriously challenging, and current approaches tend to be either too restrictive, too slow, too conservative, or approximate and therefore lack guarantees. In this paper, we propose a simple yet effective sampling-based approach to perform reachability analysis for arbitrary dynamical systems. Our key novel idea consists of using random set theory to give a rigorous interpretation of our method, and prove that it returns sets which are guaranteed to converge to the convex hull of the true reachable sets. Additionally, we leverage recent work on robust deep learning and propose a new adversarial sampling approach to robustify our algorithm and accelerate its convergence. We demonstrate that our method is faster and less conservative than prior work, present results for approximate reachability analysis of neural networks and robust trajectory optimization of high-dimensional uncertain nonlinear systems, and discuss future applications$^1$.

**Keywords:** Reachability analysis, robust planning and control, neural networks

Footnote 1: All code is available at https://github.com/StanfordASL/UP

## 1 Introduction

Reachability analysis is at the core of many applications, from robust trajectory planning of uncertain systems, to neural network verification. Generally, it entails characterizing the set of reachable states for a system at any given time in the future. For instance, planning a trajectory for a quadrotor carrying a payload of uncertain mass in severe wind requires ensuring that no reachable state collides with obstacles. In formal verification of neural networks, reachability analysis can be used to quantify the change in output for various input perturbations, and hence ensure prediction accuracy despite adversarial examples. However, reachability analysis is notoriously challenging, as it requires describing all reachable states from *any* possible initial state and any realization of uncertain parameters of the system. In contrast to approaches which can handle problems with known probability distributions over parameters, e.g., when the state of the system is estimated with Kalman filtering, and parameters are updated through Bayesian inference, sometimes only bounds on unknown parameters are available, which is the case when constructing confidence sets for the parameters of the model [1]. To perform reachability analysis for problems with bounded uncertainty, current methods tend to be encumbered by strong assumptions which are difficult to verify in practice, do not scale well to complex systems, or are too slow to be used within data-driven controllers which use and refine bounds on model parameters in real time. In practice for robotic applications, they often require tuning parameters used to provide theoretical guarantees and yield optimal performance, or using a simplified model of the system, e.g., assuming disturbances affect the system additively. These are reasonable assumptions for many applications, but the general problem remains a challenge.

**Contributions** In this work, we consider the problem of reachability analysis for general systems with bounded state and parameters uncertainty, and bounded external disturbances. Our proposed approach can tackle high-dimensional nonlinear dynamics, and makes minimal assumptions about the properties of the system. It is fast, parallelizable, simple to implement, and provides accurate

<!-- PDF page 2 -->

estimates of reachable sets. Our key novel technical idea consists of leveraging random set theory to provide theoretical convergence guarantees of our algorithm, and paves the way for future applications of this theory to the field of robotics. Specifically, our contributions are as follows:

1. A novel, simple, yet effective sampling-based method to perform reachability analysis for general nonlinear systems and bounded uncertainty. Using the theory of random sets, we prove that our method is guaranteed to asymptotically converge to the convex hull of the reachable sets.

2. We develop a novel adversarial sampling scheme inspired by the literature on robust deep learning to accelerate convergence of our algorithm, and identify its strengths and weaknesses.

3. We demonstrate our method on a neural network, and on the robust planning problem of a 13-dimensional nonlinear uncertain spacecraft. We show that our method outperforms current approaches by yielding tighter reachable sets with faster computation time.

4. We discuss immediate applications of our method, as well as possible future applications of random set theory for robotics and deep learning.

![Figure 1](../assets/s001-lew2021sampling/figure-1.png)

**Figure 1:** (**randUP**) consists of three steps: 1) initial states, controls, disturbances and parameters are sampled, 2) each particle is propagated according to the nonlinear dynamics, and 3) the convex hull at each time $k$ is computed. Since each convex hull depends on randomly sampled parameters, it is itself random, and can be mathematically described using theory of random sets [2]. In Theorem 2, we prove that each convex hull $\mathcal{X}_k^M(\omega)$ is guaranteed to converge to the true convex hull of the reachable set $\mathcal{X}_k$ as $M\rightarrow\infty$. In Section 4, we propose (**robUP!**): an adversarial sampling scheme robustifying (**randUP**) by accelerating its convergence.

**Related work** When probability distributions over uncertain parameters are available, sampling-based methods can propagate uncertainty [3, 4] with asymptotic guarantees. Scenario optimization can also be used for reachability analysis [5], and ensure probabilistic convex constraints satisfaction [6]. Although various methods exist to approximately tackle such problems [7, 8, 9, 10], accurate probability distributions over parameters are required to ensure safe operation of the underlying autonomous systems. Instead, the problem of reachability analysis with bounded uncertainty is of interest whenever no accurate prior is available, and one must rely on confidence sets for the parameters of the model [1]. For such problems, endowing a sampling-based approach for reachability analysis with guarantees is a challenging task; this often requires precise knowledge of certain mathematical properties of the system, e.g., the Lipschitz constant of the reachability function from any state with respect to the Hausdorff distance, the ratio of the surface area of the true reachable set to its volume [11], or smoothness properties of the boundary of the true reachable set [12].

Alternatively, methods which directly leverage smoothness properties of dynamical systems are capable of computing outer-approximations of reachable sets. Such algorithms often leverage precise knowledge of the Lipschitz constant of the system to bound the Lagrange remainder resulting from a finite order Taylor series approximation [13, 14]. Unfortunately, precise Lipschitz constants are rarely available in data-driven control applications, and even with this knowledge these algorithms are often too conservative in practice (see Section 6). Computing tight upper-bounds on Lipschitz constants of neural networks is an active field of research [15, 16], but current methods are computationally expensive, which prevents their use in learning-based control where the model of the system is updated online (e.g., via gradient descent [17], or linear regression over the last layer [18, 19]). Recently, efficient and scalable sampling-based algorithms have been proposed to estimate Lipschitz constants [14, 20], but such methods are not guaranteed to provide upper bounds [15].

Finally, Hamilton-Jacobi (HJ) reachability analysis can compute reachable sets exactly [21, 22]. Unfortunately, handling arbitrary systems (e.g., neural networks) with such approaches is challenging, as they require solving a partial differential equation involving a max/minimization over controls

<!-- PDF page 3 -->

and disturbances. For this reason, these methods typically discretize the state space and thus suffer from the curse of dimensionality [21]. Further, these methods leverage the principle of dynamic programming to compute solutions, and thus cannot handle parameter uncertainty which introduces time correlations along the trajectory (see Section 2). Other approaches include using surrogate models to directly parameterize reachable sets [23, 24], and formal verification tools for dynamical systems [25] and neural networks [26]. As these methods typically perform all computation offline$^2$, they may not be adequate for applications where bounds on model parameters are updated over time.

Unlike prior work, our method treats the general problem of performing real-time multi-steps reachability analysis for arbitrary systems. Specifically, we only assume that the dynamics are continuously differentiable, and that the uncertainty is bounded. To do so, we leverage random set theory to provide asymptotic convergence guarantees to the convex hull of the reachable sets. Our proposed method is suitable to various applications where approximations are sufficient in practice, and stronger guarantees can be derived given further system-specific assumptions (see Section 5).

**Notation** We denote the sets of natural and real numbers by $\mathbb{N}$ and $\mathbb{R}$, respectively, and the Borel $\sigma$-algebra in $\mathbb{R}^n$ by $\mathcal{B}(\mathbb{R}^n)$. We use $\mathcal{F}$, $\mathcal{G}$, and $\mathcal{K}$ to denote the families of closed, open, and compact sets in $\mathbb{R}^n$, respectively. We write $\mathcal{S}^N := \mathcal{S}\times\ldots\times\mathcal{S}$ ($N$ times) for any set $\mathcal{S}$, and $\|\boldsymbol{x}\|^2_{\boldsymbol{Q}} = \boldsymbol{x}^T\boldsymbol{Q}\boldsymbol{x}$ with positive-definite matrix $\boldsymbol{Q}$. The function composition operator is denoted as $\circ$, and the convex hull of a discrete set $\mathcal{X}^M = \{\boldsymbol{x}^j\}_{j=1}^M$ as $\mathrm{Co}(\mathcal{X}^M)$.

## 2 Problem Formulation

We consider general discrete-time dynamical systems of the form

$$\boldsymbol{x}_{k+1} = \boldsymbol{f}(\boldsymbol{x}_k, \boldsymbol{u}_k, \boldsymbol{\theta}, \boldsymbol{w}_k), \tag{1}$$

with state $\boldsymbol{x}_k \in \mathbb{R}^n$, control input $\boldsymbol{u}_k \in \mathcal{U}_k$, uncertain parameters $\boldsymbol{\theta} \in \Theta$, external disturbance $\boldsymbol{w}_k \in \mathbb{W}$, and initial state $\boldsymbol{x}_0 \in \mathcal{X}_0$, where $\mathcal{U}_k \subset \mathbb{R}^m$, $\Theta \subset \mathbb{R}^p$, $\mathbb{W} \subset \mathbb{R}^q$, and $\mathcal{X}_0 \subset \mathbb{R}^n$ are known compact sets. We only assume of the dynamics $\boldsymbol{f}(\cdot)$ to be continuously differentiable, which includes neural network approximators and common systems in robotic applications.

Let $N\in\mathbb{N}$, a finite time horizon. The goal of this paper consists of performing reachability analysis for (1), by computing reachable sets $\mathcal{X}_1,\dots,\mathcal{X}_N$ in which the state trajectory is guaranteed to lie. Formally, the reachable set $\mathcal{X}_k$ at each time $k=1,\dots,N$ can be expressed as

$$\mathcal{X}_k = \bigg\{ \boldsymbol{x}_k = \boldsymbol{f}(\cdot, \boldsymbol{u}_{k-1}, \boldsymbol{\theta}, \boldsymbol{w}_{k-1})\circ\dots\circ\boldsymbol{f}(\boldsymbol{x}_0, \boldsymbol{u}_0, \boldsymbol{\theta}, \boldsymbol{w}_0) \ \bigg| \begin{array}{l} \boldsymbol{x}_0\in\mathcal{X}_0, \, \boldsymbol{u}_i\in\mathcal{U}_i, \, \boldsymbol{w}_i\in\mathbb{W} \\ \boldsymbol{\theta}\in\Theta, \quad \ \ i=1,\ldots,k-1 \end{array} \bigg\}. \tag{2}$$

Specifically, $\mathcal{X}_k$ describes the set of all possible reachable states at time $k$, using control inputs respecting actuator constraints, and for any possible model parameter and external disturbance. This problem formulation also allows the verification of a given feedback controller $\boldsymbol{u} = \boldsymbol{\kappa}(\boldsymbol{x})$, by computing the reachable set of the system $\boldsymbol{f}(\boldsymbol{x}_k, \boldsymbol{\kappa}(\boldsymbol{x}_k), \boldsymbol{\theta}, \boldsymbol{w}_k)$. Also, evaluating the reachable set for a given sequence of open-loop control inputs $(\boldsymbol{u}_0,\ldots,\boldsymbol{u}_{N-1})$ is a specific instance of this problem, with $\mathcal{U}_i = \{\boldsymbol{u}_i\}$. By continuity of $\boldsymbol{f}$ and compactness of $\mathcal{X}_0$, $\mathcal{U}_i$, $\Theta$ and $\mathbb{W}$, all reachable sets are guaranteed to be compact. We note that (2) is different than defining the following recursion [28]

$$\tilde{\mathcal{X}}_{k+1}=\{ \boldsymbol{x}_{k+1} \ | \ \boldsymbol{x}_{k+1} = \boldsymbol{f}(\boldsymbol{x}_k, \boldsymbol{u}_k, \boldsymbol{\theta}, \boldsymbol{w}_k), \ \boldsymbol{x}_k\in\tilde{\mathcal{X}}_k, \ \boldsymbol{u}_k\in\mathcal{U}_k, \ \boldsymbol{\theta}\in\Theta, \ \boldsymbol{w}_k\in\mathbb{W} \}, \ \tilde{\mathcal{X}}_0 =\mathcal{X}_0,$$

which neglects the time dependency of the trajectory on $\boldsymbol{\theta}$. For instance, consider $\boldsymbol{x}_{k+1}=\boldsymbol{\theta}\boldsymbol{x}_k$, with $\boldsymbol{\theta}\in\{1,2\}$, and $\mathcal{X}_0=\{1\}$. Then, $\mathcal{X}_2=\{1,4\}$. However, $\tilde{\mathcal{X}}_2=\{1,2,4\}$, which is artificially more conservative than using (2). This is an issue which many uncertainty propagation methods suffer from [13, 24, 8], as it can cause additional conservatism or innacuracies [29] when considering uncertainty over model parameters.

Before proposing an algorithm designed to perform reachability analysis, we recall the three main difficulties of this problem: a) minimal assumptions are made about the dynamics (1); b) reachable sets should be computed as fast as possible, to enable data-driven applications where model parameters are updated online, and to embed this reachability tool within control feedback loops for robotic applications; c) The method should scale to relatively high dimensions $n,m,p,q$. In the following section, we present a sampling-based methodology which addresses these challenges.

Footnote 2: Although recent work enables warm-starting HJ reachability analysis [27], such methods still require a few seconds for a 3D linear system, and more than an hour for a 10D quadrotor.

<!-- PDF page 4 -->

## 3 Approximate Reachability Analysis using Random Set Theory

Consider computing $\mathcal{X}_k$ exactly. To design an algorithm, we start with the observation that if we could evaluate all possible values of $(\boldsymbol{x}_0,\boldsymbol{u},\boldsymbol{\theta},\boldsymbol{w})\in\mathcal{X}_0\times\mathcal{U}^{k-1}\times\Theta\times\mathbb{W}^{k-1}$, and compute $\boldsymbol{x}_k$ for each tuple by forward propagation through the dynamics, then $\mathcal{X}_k$ would be known exactly. Unfortunately, this is only possible if $\mathcal{X}_0,\mathcal{U},\Theta$, and $\mathbb{W}$ are finite and small, which is generally not the case.

Instead, consider sampling a finite number $M$ of initial states $\boldsymbol{x}_0^j$, control trajectories $\boldsymbol{u}^j$, parameters $\boldsymbol{\theta}^j$, and disturbances $\boldsymbol{w}^j$, resulting in a finite number of states $\boldsymbol{x}_k^j$ which are guaranteed to lie within the true unknown reachable set $\mathcal{X}_k$. From this finite set of states, three questions arise:

- How can we best approximate $\mathcal{X}_k$ from $\{\boldsymbol{x}_k^j\}_{j=1}^M$?

- What theoretical guarantees result from such a sampling-based approach?

- How can we best select samples $\{\boldsymbol{x}_0^j,\boldsymbol{u}^j,\boldsymbol{\theta}^j,\boldsymbol{w}^j\}_{j=1}^M$, for both efficiency and accuracy?

This section treats the first two questions, and the third will be dealt with in Section 4. Before proposing a solution, it is important to correctly characterize the properties of possible set estimators which leverage the samples $\{\boldsymbol{x}_k^j\}_{j=1}^M$. Although different approaches to approximate sets from samples can be found in the literature, they typically assume that samples are drawn uniformly within the set itself, and leverage smoothness properties of the set boundaries to provide convergence guarantees of their estimators [12, 30, 31]. To treat our more general problem formulation, we opt for an alternative mathematical description of the class of estimators computed from a collection of randomly sampled states $\boldsymbol{x}^j$: they are *random sets* [2]. Intuitively, different approximate reachable sets will be computed for different realizations of the samples $(\boldsymbol{x}_0^j,\boldsymbol{u}^j,\boldsymbol{\theta}^j,\boldsymbol{w}^j)$. Mathematically, two random sets share the same distribution if their probabilities to intersect any compact set $K\subset\mathbb{R}^n$ are equal. A random set is formally defined as a map from a probability space to a family of sets [2]:

**Definition 1 (Random Set).** A map $\mathcal{X} : \Omega \rightarrow \mathcal{F}$ from a probability space $(\Omega,\mathcal{A},\mathbb{P})$ to the family of closed sets in $\mathbb{R}^n$ is a random closed set if $\{\omega \mid \mathcal{X}(\omega) \cap \mathcal{K} \neq \emptyset\} \in \mathcal{A}$ for every compact set $K \subset \mathbb{R}^n$.

In this work, we seek convex approximations of the reachable sets, as convex sets are widely used for control applications and neural network verification. Specifically, we consider using the convex hull of the samples $\{\boldsymbol{x}_k^j\}_{j=1}^M$. The interpretation of the convex hull of sampled points as a random set was mentioned in [2], but to the best of our knowledge, no prior work uses the theory of random sets for reachability analysis. We leverage random set theory to enable a clear analysis of the properties of our method, despite very weak assumptions about our system.

We propose the simple sampling-based procedure in Algorithm 1 illustrated in Figure 1 to approximate the reachable sets. It consists of 1) sampling i.i.d. tuples $(\boldsymbol{x}_0^j,\boldsymbol{u}^j,\boldsymbol{\theta}^j,\boldsymbol{w}^j)\in\mathcal{X}_0\times\mathcal{U}^{N}\times\Theta\times\mathbb{W}^{N-1}$ according to arbitrary probability distributions over $\mathcal{X}_0$, $\mathcal{U}$, $\Theta$ and $\mathbb{W}$, 2) propagating each sample through the dynamics (1) to obtain states within the true reachable sets $\mathcal{X}_k$, and 3) taking their convex hull. Outer ellipsoidal sets or zonotopes can also be used as alternatives to facilitate the downstream application (see Section 5). Different domain-specific sampling distributions are possible; e.g., a beta distribution of shape parameters $\alpha = \beta \ll 1$ for additive disturbances may maximize the volume of $\mathcal{X}_k^M$.

![Algorithm 1](../assets/s001-lew2021sampling/algorithm-1.png)

**Alg. 1. UP using Random Sampling (randUP)**

**Parameters**: Number of samples $M$  
**Output**: Convex approximation of reachable sets $\mathcal{X}_k$

1: Sample i.i.d. $(\boldsymbol{x}_0^j,\boldsymbol{u}^j,\boldsymbol{\theta}^j,\boldsymbol{w}^j)$, $\quad j=1,\ldots,M$  
2: $\boldsymbol{x}^j_{1:N}\gets \mathrm{Propagate}(\boldsymbol{x}_0^j,\boldsymbol{u}^j,\boldsymbol{\theta}^j,\boldsymbol{w}^j)$, $\quad j=1,\ldots,M$  
3: $\mathcal{X}_k^M = \mathrm{Co}(\{\boldsymbol{x}_k^j\}_{j=1}^M)$, $\quad k=1,\ldots,N$  
4: **return** $\{\mathcal{X}_k^M\}_{k=1}^N$

The key advantages of (**randUP**) over standard reachability analysis tools are that 1) it is easy to understand and implement, 2) the number of particles is a design choice, which can be chosen to best exploit available computation resources, or meet a precision criteria, 3) it is parallelizable, and 4) it requires minimal assumptions about the system, namely continuity of the dynamics, and boundedness of the parameter space. To clarify, $\boldsymbol{f}\in\mathcal{C}^1$ in (1) is only required for the algorithm introduced in the next section, which will leverage gradient information to further improve robustness.

Despite the simplicity of our algorithm, it is guaranteed to converge to the convex hulls of the true reachable sets $\mathcal{X}_k$. From a theoretical point of view, this result is important, as it guarantees that by increasing the number $M$ of particles, the true reachable sets $\mathcal{X}_k$ will be contained within the sampled convex hulls. At the core of our proof of this result lie mathematical tools from the theory of random sets. Specifically, we first restate a theorem in [2, Prop. 1.7.23], providing necessary and sufficient conditions of convergence of random sets which are key to derive our main result:

<!-- PDF page 5 -->

**Theorem 1 (Convergence of Random Sets to a Deterministic Limit).** A sequence $\{\mathcal{X}^m\}_{m=1}^\infty$ of random closed sets in $\mathbb{R}^n$ almost surely converges to a deterministic closed set $\mathcal{X}$ if and only if the following conditions hold:

(**C1**) For any $K\in\mathcal{K}$, with $\mathcal{K}$ the family of compact sets in $\mathbb{R}^n$,

$$\mathcal{X}\cap K = \emptyset \implies \mathbb{P}(\mathcal{X}^m\cap K \neq \emptyset \ \ \text{infinitely often}) = 0. \tag{3}$$

(**C2**) For any $G\in\mathcal{G}$, with $\mathcal{G}$ the family of open sets in $\mathbb{R}^n$,

$$\mathcal{X}\cap G \neq \emptyset \implies \mathbb{P}(\mathcal{X}^m\cap G = \emptyset \ \ \text{infinitely often}) = 0. \tag{4}$$

![Figure 2](../assets/s001-lew2021sampling/figure-2.png)

**Figure 2:** Conditions (**C1-2**).

With this theorem, we prove that our method in Algorithm 1 computing approximations of the reachable sets is guaranteed to converge to the convex hull of the true reachable sets.

**Theorem 2 (Convergence of Random Convex Hulls using (randUP)).** Let $\{(\boldsymbol{x}_0^j,\boldsymbol{u}^j,\boldsymbol{\theta}^j,\boldsymbol{w}^j)\}_{j=1}^m$ be i.i.d. sampled parameters in $\mathcal{X}_0\times\mathcal{U}^{k-1}\times\Theta\times\mathbb{W}^{k-1}$. Define $\boldsymbol{x}_k^j$ according to (1), and denote the resulting convex hulls as $\mathcal{X}_k^m = \mathrm{Co}(\{\boldsymbol{x}_k^j\}_{j=1}^m)$. Assume that the sampling distribution of the parameters satisfies $\mathbb{P}(\boldsymbol{x}_k^j \in G_k) > 0$ for any open set $G_k$ s.t. $\mathcal{X}_k \cap G_k \neq \emptyset$.

Then, as $m\rightarrow\infty$, $\mathcal{X}_k^m$ converges to the convex hull of the reachable set $\mathrm{Co}(\mathcal{X}_k)$ almost surely.

We provide a complete proof in the Appendix and outline it here. First, it consists of showing that $\{\mathcal{X}^m\}_{m=1}^\infty$ is a sequence of compact random sets. Then, we leverage Theorem 1 and show that its conditions are fulfilled. The i.i.d. assumption is key to apply the second Borel-Cantelli lemma, and the assumption $\mathbb{P}(\boldsymbol{x}_k^j \in G_k) > 0$ ensures that any point of the true reachable set has a positive probability of being within $\mathcal{X}^m$. By choosing an appropriate sampling distribution over parameters, both assumptions are simple to satisfy in practice. The key advantages of (**randUP**) are its asymptotic convergence guarantees for general continuous dynamical systems, and that it is intuitive, practical, and can be applied immediately for various applications. Nevertheless, its generality comes with limitations which we discuss below, and relate to existing results in the literature.

**Outer-approximation** For non-convex sets $\mathcal{X}_k$, the convex hull $\mathrm{Co}(\mathcal{X}_k)$ is an over-approximation. Instead, one could take the union of $\epsilon$-balls whose radius $\epsilon$ shrinks depending on the number of samples and the smoothness of the boundary [12, 31] or dynamics [11], which comes with the limitations mentioned in Section 1. Taking the convex hull is not an issue (and is sufficient) for many applications, e.g., uncertainty-aware trajectory optimizers typically use convex hulls to compute feasible obstacle-free paths, as they convexify constraints using first [8], or second order information$^3$.

**Inner-approximation** For some classes of reachable sets $\mathcal{X}_k$ (e.g., a ball), our method always returns a subset of $\mathcal{X}_k$. This could be a limitation, especially for safety critical applications. This problem is acknowledged in [30], which proposes to inflate the resulting convex hull by a quantity related to the estimated volume of $\mathcal{X}_k$. Unfortunately, their work focuses on set estimation in two dimensions only, and efficiently computing the volume of an arbitrary convex polytope is challenging [32]. Similar related problems are investigated in [12, Chap. 5.4-6,7.5], which proposes maximum likelihood estimators for Dudley sets, as well as star-shaped sets. Unfortunately, their work requires smoothness properties of the boundaries of the estimated set, which are unknown in our problem setting, or would be related to the Lipschitz constant of $\boldsymbol{f}$ and provide coarse estimations as discussed earlier. Critically, they assume uniform sampling of points directly within $\mathcal{X}_k$. For reachability analysis, parameters are sampled, and analytically computing the distribution for $\boldsymbol{x}_k$ is intractable.

**Rate of convergence** Although Theorem 2 provides asymptotic guarantees of convergence to the convex hull of the reachable sets, it does not provide a convergence rate. Rates of convergence for various set estimators are derived in [12, 31], by leveraging smoothness properties, and uniformly sampling directly within $\mathcal{X}_k$. For our problem setting, uniformly sampling parameters and computing reachable states does not lead to a uniform distribution of samples within $\mathcal{X}_k$, and verifying such smoothness properties is a challenge for reachable sets of general dynamical systems. Nevertheless, we believe that random set theory could be used to analyze convergence rates of similar methods (e.g., using the *variance* of the random sets, as pointed out in [33]), which we leave for future work.

Next, we propose an adversarial sampling scheme capable of accelerating the convergence of (**randUP**), alleviating the last two problem-specific limitations above.

Footnote 3: In the multimodal case, since $\boldsymbol{f}\in\mathcal{C}^1$, multimodal reachable sets occur if and only if the parameter set is disjoint. In this case, it suffices to run (**randUP**) on each disjoint set, and return their union.

<!-- PDF page 6 -->

## 4 Adversarial Sampling for Robust Uncertainty Propagation

The accuracy of the reachable set approximation depends on the realization of the sampled parameters $\boldsymbol{z}^j=(\boldsymbol{x}_0^j,\boldsymbol{u}^j,\boldsymbol{\theta}^j,\boldsymbol{w}^j)$. For instance, a sample $\boldsymbol{z}^{M+1}$ for which $\boldsymbol{x}_k^{M+1}\in\mathcal{X}_k^M$ results in the same convex hull $\mathcal{X}_k^{M+1}=\mathcal{X}_k^M$ and is not informative. This motivates choosing new parameters for which $\boldsymbol{x}_k^{M+1}\notin\mathcal{X}_k^M$. This parallels robust classification and adversarial attacks of neural networks [34, 35, 36]. Indeed, the approximate reachable set $\mathcal{X}_k^M$ can be interpreted as a classifier of the reachable states, and new samples satisfying $\boldsymbol{x}_k^{M+1}\notin\mathcal{X}_k^M$ as adversarial examples. The objective then consists of obtaining a robust classifier of the reachable set. Adversarial examples for deep neural network classifiers are often found by slightly perturbing inputs to cause drastic changes in the associated predictions. For such parametric models, the training loss explicitly depends on the possibly perturbed input. In contrast, our decision boundary is implicitly defined as a polytope around the sampled points $\boldsymbol{x}^j$, instead of as a parametric function of $\boldsymbol{z}^j$. Thus, even if a loss function was available for our problem, computing its gradient at any $\boldsymbol{z}$ to find adversarial examples is challenging. Moreover, defining a loss function is not trivial; the Hausdorff distance between the approximate and the true reachable sets would be difficult to evaluate since no ground truth of the reachable set is available. In computer vision, the Chamfer distance [37] or local signed distance functions [38, 39, 40] are used for 3D set reconstruction, but such methods typically discretize the state space and thus do not scale well to high-dimensional systems.

With these analogies and challenges in mind, we propose an algorithm which consists of incrementally sampling new parameters $\boldsymbol{z}$ for which the resulting states lie outside the convex hull of the previous samples. Specifically, we search for new parameters which maximize the metric

$$\mathcal{L}^M(\boldsymbol{z}) = \frac{1}{N}\sum_{k=1}^N \|\boldsymbol{x}_k(\boldsymbol{z})-\boldsymbol{c}_k^M \|_{\boldsymbol{Q}_k^M}^2, \ \text{with}\ \boldsymbol{Q}_k^M=\Big(\frac{1}{M-1}\sum_{j=1}^M \big(\boldsymbol{x}_k^j-\boldsymbol{c}_k^M\big)\big(\boldsymbol{x}_k^j-\boldsymbol{c}_k^M\big)^T \Big)^{-1}, \tag{5}$$

where $\boldsymbol{c}_k^M$ is the geometric center of $\mathcal{X}_k^M$ computed previously with $\{\boldsymbol{x}_k^j\}_{j=1}^M$, $\boldsymbol{Q}_k^M$ are positive definite matrices, and $\boldsymbol{x}_k(\boldsymbol{z})=\boldsymbol{f}(\cdot, \boldsymbol{u}_{k-1}, \boldsymbol{\theta}, \boldsymbol{w}_{k-1})\circ\dots\circ\boldsymbol{f}(\boldsymbol{x}_0, \boldsymbol{u}_0, \boldsymbol{\theta}, \boldsymbol{w}_0))$. Although we take the mean over multiple time steps, it is also possible to assign different time steps for different samples, but this yields minimal differences in practice. We propose to maximize (5) using Projected Gradient Ascent (PGA), and outline the algorithm in Algorithm 2. As the speed of convergence of PGA depends on the condition number of the Hessian of the objective function [41], we choose $\boldsymbol{Q}_k^M$ as the inverse of the covariance matrix of $\{\boldsymbol{x}_k^j\}_{j=1}^M$, which also provides a simple method to weigh the different dimensions of the state trajectory. The projection step of the parameters onto $\mathcal{Z}=\mathcal{X}_0\times\mathcal{U}^{k}\times\Theta\times\mathbb{W}^{k-1}$ can be efficiently computed for common compact sets used for learning-based control applications (e.g., rectangular and ellipsoidal sets [42]).

![Algorithm 2](../assets/s001-lew2021sampling/algorithm-2.png)

**Alg. 2. Robust UP using Adversarial Sampling (robUP!)**

**Input**: Sampled parameters $\{\boldsymbol{z}^j\}_{j=1}^M=(\boldsymbol{x}_0^j,\boldsymbol{u}^j,\boldsymbol{\theta}^j,\boldsymbol{w}^j)_{j=1}^M$  
**Parameters**: Stepsize $\boldsymbol{\eta}$, nb. iters. $n_{\mathrm{adv}}$  
**Output**: Particles $\mathcal{X}_N^{n_{\mathrm{adv}}}=\{\boldsymbol{x}^j\}_{j=1}^{M\cdot n_{\mathrm{adv}}}$

1: $\boldsymbol{x}^j_{1:N}\gets \mathrm{Propagate}(\boldsymbol{z}^j)$, $\quad j=1,\ldots,M$  
2: $\mathcal{X}_N^0=\{\boldsymbol{x}^j_{1:N}\}_{j=1}^M$  
3: **for** $i=1,\dots,n_{\mathrm{adv}}$ **do**  
4: &emsp;&emsp; $\boldsymbol{z}^j \gets \boldsymbol{z}^j + \boldsymbol{\eta}\, \nabla_{\boldsymbol{z}} \mathcal{L}^M(\boldsymbol{x}^j_{1:N})$, $\quad j=1,\ldots,M$  
5: &emsp;&emsp; $\boldsymbol{z}^j \gets \mathrm{Proj}_{\mathcal{Z}}(\boldsymbol{z}^j)$, $\quad j=1,\ldots,M$  
6: &emsp;&emsp; $\boldsymbol{x}^j_{1:N}\gets \mathrm{Propagate}(\boldsymbol{z}^j)$, $\quad j=1,\ldots,M$  
7: &emsp;&emsp; $\mathcal{X}_N^i\gets\mathcal{X}_N^{i-1}\cup\{\boldsymbol{x}^j_{1:N}\}_{j=1}^M$  
8: **return** $\mathrm{Co}\big(\mathcal{X}_N^{n_{\mathrm{adv}}}\big)$

![Figure 3](../assets/s001-lew2021sampling/figure-3.png)

**Figure 3:** By varying $\boldsymbol{x}_0$, $\boldsymbol{u}$, $\boldsymbol{\theta}$, and $\boldsymbol{w}$ along the gradient of $\mathcal{L}(\cdot)$ using projected gradient ascent, (**robUP!**) provides a simple and efficient sampling scheme which robustifies (**randUP**) by finding adversarial parameter samples. This figure shows the effect of a single adversarial step on a uncertain system subject to disturbances.

## 5 Leveraging System-Specific Properties and Applications

Despite minimal assumptions about the system, we derived an asymptotic convergence guarantee for our method in Theorem 2 using random set theory. Stronger guarantees can be derived with additional assumptions. Firstly, if the reachable sets are convex, our method is guaranteed to always provide inner approximations for any finite number of samples, and our tool can be immediately used for falsification [43]. This is the case for any convex dynamical system and uncertainty sets, e.g., for

<!-- PDF page 7 -->

time-varying linear systems with polytopic uncertainty, or certain neural network architectures [44, 45]. Secondly, if smoothness properties of $\boldsymbol{f}$ are available, inflating our approximate convex hulls by a quantity proportional to the Lipschitz constant and the distance between parameter samples suffices to guarantee an over-approximation. Our current approach remains an interesting additional option to efficiently approximate reachable sets whenever it is a challenge to compute tight Lipschitz constants. Thirdly, as discussed in Section 3, we believe that rates of convergence could be derived by leveraging random set theory and smoothness properties of the boundary of the reachable set. Since current methods make specific assumptions on the distribution of the samples within $\mathcal{X}_k$ [12, 31], we leave such extensions for future work. Finally, our method can be used to improve the efficiency of other algorithms. Specifically, we present a direct application of our method to the problem of selecting the correct homotopy class of paths for robust planning in the next section.

## 6 Results and Applications

**Linear system** We first compare our approach with [11], which can guarantee $(1-\epsilon)$ volume coverage of the true reachable set. However, this method requires an oracle performing reachability analysis over $\mathcal{U}$ from any state, cannot handle parameters uncertainty and disturbances, requires knowledge of Lipschitz constants, the surface area, and volume of the reachable sets, and requires taking a union of reachable sets, resulting in a non-convex set which is challenging to compute. For these reasons, we provide comparisons on a system for which these assumptions hold, and consider $\boldsymbol{x}_1 = \boldsymbol{x}_0 + \boldsymbol{u}_0, \ \boldsymbol{x}_1 \in \mathbb{R}^n, \boldsymbol{x}_0 \in [-1,1]^n$, $\boldsymbol{u}_0 \in [-\bar{u},\bar{u}]^n$. We set $\eta = 1$ and $n_{\mathrm{adv}} = 1$, sample uniformly over $\mathcal{X}_0 \times \mathcal{U}_0$, and use a grid to construct a $\delta$-covering of $\mathcal{X}_0$ for [11]. Figure 4 reports comparisons of volume coverage. Whereas (**randUP**) and (**robUP!**) provide consistent volume coverage across all problems, the convergence rate of [11] is heavily dependent on $\bar{u}$. Furthermore, (**robUP!**) significantly outperforms other methods with a single adversarial sampling step only.

![Figure 4](../assets/s001-lew2021sampling/figure-4.png)

**Figure 4:** Comparisons on linear system with $\bar{u} \in \{0.5,1,2\}$, $n \in \{3,4\}$, and $3\sigma$ confidence bounds across 10 experiments each. Blue: (**robUP!**), green: (**randUP**), orange: [11].

**Neural network dynamics** Next, we demonstrate our method on a system with learned dynamics. Specifically, we consider a double integrator with $\boldsymbol{x}_k = (\boldsymbol{p}_k,\boldsymbol{v}_k) \in \mathbb{R}^4$, $\boldsymbol{u}_k \in \mathbb{R}^2$, $\boldsymbol{p}_{k+1} = \boldsymbol{p}_k + \boldsymbol{v}_k$, and $\boldsymbol{v}_{k+1} = \boldsymbol{v}_k + \boldsymbol{u}_k$. We train a fully connected neural network with two hidden layers of sizes $(128,128)$ and $\tanh(\cdot)$ activation functions. We use a quadratic loss and $\mathcal{L}_2$ regularization, and provide further details about our implementation in PyTorch [46] in the Appendix. We randomize initial conditions and control trajectories within compact sets $\mathcal{X}_0 \times \mathcal{U}_k^N$ over a horizon of $N=10$ steps, where $\mathcal{X}_0$ are ellipsoidal sets, and $\mathcal{U}_k = \{\boldsymbol{u}_k\}$ are fixed open-loop control trajectories. Since the true system is linear, and our trained model achieves an error below $10^{-7}$ over the state space, we can compute the volume of the true reachable sets. For each of the 100 initial conditions and fixed control trajectories, we evaluate the volume coverage of both (**randUP**) and (**robUP!**), and report all results in Figure 5. To compute the projection step onto $\mathcal{X}_0$ in (**robUP!**), we use the Self-adaptive Alternating Direction Method of Multipliers (S-ADMM) described in [42].

![Figure 5](../assets/s001-lew2021sampling/figure-5.png)

**Figure 5:** Volume coverage on neural network system for 100 different $\mathcal{X}_0$ and control trajectories. Although volume coverage decreases over time (left, with $\pm 2$ standard dev.), (**robUP!**) consistently out-performs (**randUP**). When only considering positions (e.g., for obstacle avoidance), accuracy is better. Comparisons with [13] (top middle, right) show that it is too conservative for a longer horizon, even when the true Lipschitz constant of the system is given.

Transcription of the table embedded in Figure 5 (top right panel). Rows are methods; columns are the reachable sets exactly as printed ($\mathcal{X}_0$, $\mathcal{X}_1$, $\mathcal{X}_2$, $\mathcal{X}_4$, $\mathcal{X}_5$); entries are "% of True Vol.". The row labels are printed as (**randUP**)$^{M=3\mathrm{k}}$, (**robUP!**)$^{M=2\mathrm{k}}_{n_{\mathrm{adv}}=1}$ and Lipschitz [13].

[Figure 5 embedded table](s001-lew2021sampling/figure-5-table.csv)

<!-- PDF page 8 -->

Methods leveraging the Lipschitz constant of the system are capable of conservatively approximating reachable sets. In this experiment, we provide comparisons with the method in [13]$^4$ (see C.1), which propagates a sequence of ellipsoidal sets that are guaranteed to contain the true system. Results in Figure 5 show that even in situations where the true Lipschitz constant is available, [13] is still too conservative. This is due to the outer-bounding of rectangles with ellipsoids, and to the conservative approximation of the Minkowski sum of ellipsoids, neglecting time correlations of the trajectory on the uncertainty (see Section 2). Although this method works well for short horizons and low-dimensional systems, it is too conservative for longer horizons and high-dimensional nonlinear systems, whereas our approach scales well to more challenging systems, as we show next.

**Robust planning for a spacecraft** Since our methods have asymptotic convergence guarantees (as $M\rightarrow\infty$) to the (conservative) convex hull of the reachable sets, we present an application for the quick selection of feasible homotopy classes for robust planning. Providing feasibility with respect to the convex hull is sufficient, since many optimization-based algorithms linearize constraints to find solutions [8]. Our approach has connections to algorithms boosting the convergence speed of sampling-based motion planning with reachability analysis [43, 47], with the difference that our method can account for uncertainty over parameters and disturbances. Specifically, we consider a spacecraft under uncertainty, whose state and control inputs are $\boldsymbol{x}=[\mathbf{p},\mathbf{v},\mathbf{q},\boldsymbol{\omega}]\in\mathbb{R}^{13}$, $\boldsymbol{u}=[\mathbf{F},\mathbf{M}]\in\mathbb{R}^{6}$, and whose dynamics are $\dot{\mathbf{p}} = \mathbf{v}$, $m\dot{\mathbf{v}} = \mathbf{F}$, $\dot{\mathbf{q}} = \frac{1}{2}\boldsymbol{\Omega}(\boldsymbol{\omega})\mathbf{q}$, and $\mathbf{J}\dot{\boldsymbol{\omega}} = \mathbf{M} - \mathbf{S}(\boldsymbol{\omega})\mathbf{J}\boldsymbol{\omega}$, with $J = \mathrm{diag}([J_x,J_y,J_z])$ [8]. We use a zero-order hold on the controls, an Euler discretization scheme with $\Delta t = 5\mathrm{s}$, and an additive disturbance term $\boldsymbol{w}_k$ such that $\boldsymbol{x}_{k+1} = \boldsymbol{f}(\boldsymbol{x}_k,\boldsymbol{u}_k,\boldsymbol{\theta}_k) + \boldsymbol{w}_k$. We assume the mass and inertia are unknown with known bounds $m \in [7.1,7.3]$, $J_i \in [0.065,0.075]$, $|w_{ki}| \leq 10^{-4}$ for $i=1,\ldots,13$, and $|w_{ki}| \leq 5\times10^{-4}$ for $i=4,5,6$. We perform randomized experiments to choose $M$ and $n_{\mathrm{adv}}$, which effectively trade off computation time and accuracy (see the Appendix). We decide to use (**robUP!**) with $M = 100$ and $n_{\mathrm{adv}} = 1$, as we observe reduced returns over more adversarial steps and samples. We extend the SCP-based planning algorithm from [8] to leverage our uncertainty propagation schemes, and use outer rectangular confidence sets to reformulate all constraints. Planning results for a problem with three cylindrical obstacles are shown in Figure 6. Solving this problem with $N=21$ requires 3 SCP iterations and $875\mathrm{ms}$ on a laptop with an i7-6700 CPU (2.60 GHz) and 8 GB of RAM. If the planner is initialized with a trajectory within the homotopy class on the left, the optimizer does not converge and returns an unfeasible trajectory. This is not the case with a straight-line initialization, in which case convergence is achieved within the correct homotopy class. Although we cannot guarantee that this trajectory is safe for any possible parameters since our guarantees only hold as $M\rightarrow\infty$, our approach can be used to rapidly invalidate an unfeasible homotopy class of paths, and thus avoids spending additional computational resources to compute a robust solution to this problem.

![Figure 6](../assets/s001-lew2021sampling/figure-6.png)

**Figure 6:** (**robUP!**) can be used to quickly invalidate unfeasible homotopy classes (red), and provide robust paths for a 13D nonlinear spacecraft system (blue).

## 7 Conclusion

Current approaches for reachability analysis have limitations which prevent their use for complex systems and learning-based robotic applications. To fill this gap, this paper presented a simple but theoretically justified sampling-based approach to perform real-time uncertainty propagation. It makes minimal assumptions about the system, can handle general types of uncertainty, scales well to high-dimensional systems, and out-performs current approaches. As such, it can be combined with conventional uncertainty-aware planners, and used for model-based reinforcement learning with learned dynamics for which no real-time alternatives exist, e.g., Bayesian neural networks [19].

Our new interpretation with random set theory opens news avenues for research. Firstly, it could motivate new methods to perform robust neural network training and verification, and design neural network models predicting reachable sets. Secondly, existing results for random set-valued martingales could provide further insights for reachability analysis. Thirdly, using concentration bounds and smoothness properties of reachable sets could help provide rates of convergence, probabilistic and robust outer-approximations, as long as these assumptions can be verified in practice. Finally, our approach is amenable to parallelization and thus could be further accelerated using GPUs.

Footnote 4: In [13], uncertainty comes in the form of a Gaussian process representing the dynamics, whereas uncertainty is in the initial state in this experiment. Since computing tight upper bounds on Lipschitz constants of neural networks is a rapidly evolving field of research, we implement [13] using the true constant of the system.

<!-- PDF page 9 -->

**Acknowledgments** The authors were partially supported by the Office of Naval Research, ONR YIP Program, under Contract N00014-17-1-2433. The authors thank the anynomous reviewers for their helpful comments, Spencer Richards for his feedback and suggestions, Robert Dyro for his implementation of (S-ADMM), Riccardo Bonalli for his feedback on theoretical results, James Harrison and Apoorva Sharma for helpful discussions on learning-based control, and Paul-Edouard Sarlin for suggesting related work on shape reconstruction.

## References

[1] Y. Abbasi-Yadkori, D. Pál, and C. Szepesvári. Improved algorithms for linear stochastic bandits. In *Conf. on Neural Information Processing Systems*, 2011.

[2] I. Molchanov. *Theory of Random Sets*. Springer-Verlag, second edition, 2017.

[3] E. Schmerling and M. Pavone. Evaluating trajectory collision probability through adaptive importance sampling for safe motion planning. In *Robotics: Science and Systems*, 2017.

[4] A. Loquercio, M. Segu, and D. Scaramuzza. A general framework for uncertainty estimation in deep learning. *IEEE Robotics and Automation Letters*, 5(2):3153–3160, 2020.

[5] A. Devonport and M. Arcak. Estimating reachable sets with scenario optimization. In *2nd Annual Conference on Learning for Dynamics & Control*, 2020.

[6] M. Esfahani, P. T. Sutter, and J. Lygeros. Performance bounds for the scenario approach and an extension to a class of non-convex programs. *IEEE Transactions on Automatic Control*, 60 (1), 2015.

[7] L. Hewing, J. Kabzan, and M. N. Zeilinger. Cautious model predictive control using Gaussian process regression. *IEEE Transactions on Control Systems Technology*, 2018.

[8] T. Lew, R. Bonalli, and M. Pavone. Chance-constrained sequential convex programming for robust trajectory optimization. In *European Control Conference*, 2020.

[9] M. Castillo-Lopez, S. A. Ludivig, P. Sajadi-Alamdari, J. L. Sanchez-Lopez, M. A. Olivares-Mendez, and H. Voos. A real-time approach for chance-constrained motion planning with dynamic obstacles. *IEEE Robotics and Automation Letters*, 5(2):3620 – 3625, 2019.

[10] B. Berret and F. Jean. Efficient computation of optimal open-loop controls for stochastic systems. *IEEE Robotics and Automation Letters*, 115(1), 2020.

[11] L. Liebenwein, C. Baykal, I. Gilitschenski, S. Karaman, and D. Rus. Sampling-based approximation algorithms for reachability analysis with provable guarantees. In *Robotics: Science and Systems*, 2018.

[12] A. P. Korostelev and A. B. Tsybakov. *Minimax Theory of Image Reconstruction*. Springer-Verlag, 1 edition, 1993.

[13] T. Koller, F. Berkenkamp, M. Turchetta, and A. Krause. Learning-based model predictive control for safe exploration. In *Proc. IEEE Conf. on Decision and Control*, 2018.

[14] S. Dean, N. Matni, B. Recht, and V. Ye. Robust guarantees for perception-based control. In *2nd Annual Conference on Learning for Dynamics & Control*, 2020.

[15] M. Fazlyab, A. Robey, H. Hassani, M. Morari, and G. J. Pappas. Efficient and accurate estimation of lipschitz constants for deep neural networks. In *Conf. on Neural Information Processing Systems*, 2019.

[16] F. Latorre, P. Rolland, and V. Cevher. Lipschitz constant estimation of neural networks via sparse polynomial optimization. In *Int. Conf. on Machine Learning*, 2020.

[17] C. Finn, P. Abbeel, and S. Levine. Model-agnostic meta-learning for fast adaptation of deep networks. In *Int. Conf. on Machine Learning*, 2017.

[18] J. Harrison, A. Sharma, and M. Pavone. Meta-learning priors for efficient online bayesian regression. In *Workshop on Algorithmic Foundations of Robotics*, 2018.

[19] T. Lew, A. Sharma, J. Harrison, and M. Pavone. Safe model-based meta-reinforcement learning: A sequential exploration-exploitation framework, 2020. Available at https://arxiv.org/abs/2008.11700.

[20] T. Weng, P. Zhang, H.and Chen, J. Yi, D. Su, Y. Gao, C. Hsieh, and L. Daniel. Evaluating the robustness of neural networks: an extreme value theory approach. In *Int. Conf. on Learning Representations*, 2018.

[21] S. Bansal, S. L. Chen, M. Herbert, and C. J. Tomlin. Hamilton-Jacobi reachability: A brief overview and recent advances. In *Proc. IEEE Conf. on Decision and Control*, 2017.

<!-- PDF page 10 -->

[22] J. F. Fisac, A. Bajcsy, S. L. Herbert, D. Fridovich-Keil, S. Wang, C. J. Tomlin, and A. D. Dragan. Probabilistically safe robot planning with confidence-based human predictions. In *Robotics: Science and Systems*, 2018.

[23] V. Rubies-Royo, D. Fridovich-Keil, S. L. Herbert, and C. J. Tomlin. A classification-based approach for approximate reachability. In *Proc. IEEE Conf. on Robotics and Automation*, 2019.

[24] D. D. Fan, A. Agha-mohammadi, and E. A. Theodorou. Deep learning tubes for tube MPC. In *Robotics: Science and Systems*, 2020.

[25] X. Chen, E. Ábrahám, and S. Sankaranarayanan. Taylor model flowpipe construction for non-linear hybrid systems. In *Proc. of IEEE Real-Time Systems Symposium*, 2012.

[26] R. Ivanov, J. Weimer, R. Alur, G. J. Pappas, and I. Lee. Verisig: verifying safety properties of hybrid systems with neural network controllers. In *Hybrid Systems: Computation and Control*, 2019.

[27] S. Herbert, S. L. Ghosh, S. Bansal, and C. J. Tomlin. Reachability-based safety guarantees using efficient initializations. In *Proc. IEEE Conf. on Decision and Control*, 2019.

[28] U. Rosolia and F. Borrelli. Sample-based learning model predictive control for linear uncertain systems, 2019. Available at https://arxiv.org/abs/1904.06432.

[29] L. Hewing, E. Arcari, L. P. Frohlich, and M. N. Zeilinger. On simulation and trajectory prediction with Gaussian process dynamics. In *2nd Annual Conference on Learning for Dynamics & Control*, 2020.

[30] B. D. Ripley and J. P. Rasson. Finding the edge of a poisson forest. *Journal of Applied Probability*, 14:483–491, 1977.

[31] A. Rodriguez-Casal and P. Saavedra-Nieves. A fully data-driven method for estimating the shape of a point cloud. *ESAIM: Probability and Statistics*, 20(1):332–348, 2016.

[32] B. Büeler, A. Enge, and K. Fukuda. Exact volume computation for polytopes: A practical study. In *Polytopes - Combinatorics and Computation*, pages 131–154. 2000.

[33] C. Chevalier, J. Bect, D. Ginsbourger, E. Vazquez, V. Picheny, and Y. Richet. Fast parallel kriging-based stepwise uncertainty reduction with application to the identification of an excursion set. *Technometrics*, 56(4):455–465, 2014.

[34] I. J. Goodfellow, J. Shlens, and C. Szegedy. Explaining and harnessing adversarial examples. In *Int. Conf. on Learning Representations*, 2015.

[35] A. Kurakin, I. J. Goodfellow, and S. Bengio. Adversarial examples in the physical world, 2017. Available at https://arxiv.org/abs/1607.02533.

[36] Y. Dong, F. Liao, T. Pang, H. Su, J. Zhu, X. Hu, and J. Li. Boosting adversarial attacks with momentum. In *IEEE Conf. on Computer Vision and Pattern Recognition*, 2018.

[37] H. Fan, H. Su, and L. Guibas. A point set generation network for 3D object reconstruction from a single image, 2020. Available at https://arxiv.org/abs/1612.00603.

[38] H. Hoppe, T. DeRose, T. Duchamp, J. McDonald, and W. Stuetzle. Surface reconstruction from unorganized points. In *ACM Proc. of the Annual Conf. on Computer Graphics and Interactive Techniques*, 1992.

[39] D. Cohen-Or, D. Levin, and A. Solomovici. Three-dimensional distance field metamorphosis. *ACM Transactions on Graphics*, 17(2):116–141, 1998.

[40] R. Chabra, J. E. Lenssen, E. Ilg, T. Schmidt, J. Straub, S. Lovegrove, and R. Newcombe. Deep local shapes: Learning local SDF priors for detailed 3D reconstruction, 2020. Available at https://arxiv.org/abs/2003.10983.

[41] S. Boyd and L. Vandenberghe. *Convex optimization*. Cambridge Univ. Press, 2004.

[42] Z. Jia, X. Cai, and D. Han. Comparison of several fast algorithms for projection onto an ellipsoid. *Journal of Computational and Applied Mathematics*, 319(1):320–337, 2017.

[43] A. Bhatia and E. Frazzoli. Incremental search methods for reachability analysis of continuous and hybrid systems. In *Hybrid Systems: Computation and Control*, pages 142–156, Berlin, Heidelberg, 2004. Springer Berlin Heidelberg.

[44] B. Amos, L. Xu, and Z. Kolter. Input convex neural networks. In *Int. Conf. on Machine Learning*, 2017.

[45] Y. Chen, Y. Shi, and B. Zhang. Optimal control via neural networks: a convex approach. In *Int. Conf. on Learning Representations*, 2019.

<!-- PDF page 11 -->

[46] A. Paszke, D. Gross, S. Chintala, G. Chanan, E. Yang, Z. DeVito, Z. Lin, A. Desmaison, L. Antiga, and A. Lerer. Automatic differentiation in pytorch. In *Conf. on Neural Information Processing Systems*, 2017.

[47] A. Wu, S. Sadraddini, and R. Tedrake. R3T: Rapidly-exploring random reachable set tree for optimal kinodynamic planning of nonlinear hybrid systems, 2019. Available at https://groups.csail.mit.edu/robotics-center/public_papers/Wu20.pdf.

[48] D. P. Kingma and J. L. Ba. Adam: A method for stochastic optimization. In *Int. Conf. on Learning Representations*, 2015.

[49] P. Sun and R. M. Freund. Computation of minimum-volume covering ellipsoids. *Operations Research*, 52(5), 2004.

[50] B. Stellato, G. Banjac, P. Goulart, A. Bemporad, and S. Boyd. OSQP: An operator splitting solver for quadratic programs. 2017. Available at https://arxiv.org/abs/1711.08013.

## A Proof of Theorem 2

For ease of reading, we first restate Theorem 2:

**Theorem 2 (Convergence of Random Convex Hulls using (randUP)).** Let $\{(\boldsymbol{x}_0^j,\boldsymbol{u}^j,\boldsymbol{\theta}^j,\boldsymbol{w}^j)\}_{j=1}^m$ be i.i.d. sampled parameters in $\mathcal{X}_0\times\mathcal{U}^{k-1}\times\Theta\times\mathbb{W}^{k-1}$. Define $\boldsymbol{x}_k^j$ according to (1), and denote the resulting convex hulls as $\mathcal{X}_k^m = \mathrm{Co}(\{\boldsymbol{x}_k^j\}_{j=1}^m)$. Assume that the sampling distribution of the parameters satisfies $\mathbb{P}(\boldsymbol{x}_k^j \in G_k) > 0$ for any open set $G_k$ s.t. $\mathcal{X}_k \cap G_k \neq \emptyset$.

Then, as $m\rightarrow\infty$, $\mathcal{X}_k^m$ converges to the convex hull of the reachable set $\mathrm{Co}(\mathcal{X}_k)$ almost surely.

**Proof.** Without loss of generality, we prove this theorem for any arbitrary fixed time index $k$. For conciseness, we drop the index $k$ and denote $(\boldsymbol{x}^j,\mathcal{X}^m,\mathcal{X}) = (\boldsymbol{x}^j_k,\mathcal{X}^m_k,\mathrm{Co}(\mathcal{X}_k))$, the sampled parameters tuple $\boldsymbol{z}=(\boldsymbol{x}_0,\boldsymbol{u},\boldsymbol{\theta},\boldsymbol{w})\in\mathbb{R}^z$, and the compact parameters set $\mathcal{Z}=\mathcal{X}_0\times\mathcal{U}^{k}\times\Theta\times\mathbb{W}^{k-1}$. Also, let $\boldsymbol{f}(\boldsymbol{z})=\boldsymbol{f}(\boldsymbol{\cdot},\boldsymbol{u}_{k-1},\boldsymbol{\theta},\boldsymbol{w}_{k-1})\circ\dots\circ\boldsymbol{f}(\boldsymbol{x}_0,\boldsymbol{u}_0,\boldsymbol{\theta},\boldsymbol{w}_{0})$, which is also continuous in $\boldsymbol{z}$.

Let $(\Omega,\mathcal{A}, \mathbb{P})$ a probability space, and $\mathcal{F}$ the family of closed sets in $\mathbb{R}^n$. Define $\mathcal{X}^m:\Omega\rightarrow\mathcal{F}$, with $\mathcal{X}^m(\omega) = \mathrm{Co}(\{\boldsymbol{x}^j\}_{j=1}^m)$. Then, $\{\mathcal{X}^m(\omega), m\geq 1\}$ is a sequence of compact random sets satisfying $\mathcal{X}^1(\omega)\subseteq \mathcal{X}^2(\omega) \subseteq \dots$ almost surely (a.s.).

Indeed, for all $j=1,\dots,m$, $\{\boldsymbol{x}^j\}$ is a random closed set [2]. Then, applying [2, Theorem 1.3.25, (i), (iv)], we obtain that $\mathcal{X}^m=\mathrm{Co}(\{\boldsymbol{x}^j\}_{j=1}^m)$ is a random closed set. Hence $\{\mathcal{X}^m(\omega), m\geq 1\}$ is a sequence of random closed sets satisfying Def. 1. Further, each $\mathcal{X}^m(\omega)$ is compact since it is the convex hull of bounded $\boldsymbol{x}^j$'s, since $\boldsymbol{f}(\cdot)$ is continuous and $\mathcal{Z}$ is compact. Finally, by definition, $\mathcal{X}^m \subseteq\mathcal{X}^{m+1}$ a.s. for all $m$, hence $\mathcal{X}^1(\omega)\subseteq \mathcal{X}^2(\omega) \subseteq \dots$ a.s.

Now that we proved that our convex hulls are random sets, we proceed with the proof that the sequence $\{\mathcal{X}^m(\omega), m\geq 1\}$ converges to $\mathcal{X}$ by proving that we satisfy (**C1**) and (**C2**) of Theorem 1.

(**C1**): Let $K\in \mathcal{K}$ satisfy $\mathcal{X}\cap K = \emptyset$. Since $\boldsymbol{x}^j(\omega)\in\mathcal{X}$ almost surely for all $j$, $\mathcal{X}^m\subset\mathrm{Co}(\mathcal{X})$ almost surely for all $m$. This implies that $\mathcal{X}^m\cap K=\emptyset$ almost surely for all $m$. Thus, $\mathbb{P}(\mathcal{X}^m\cap K\neq\emptyset)=0$ and $\sum_{m=1}^\infty \mathbb{P}(\mathcal{X}^m\cap K\neq\emptyset)=0$. By the first Borel-Cantelli lemma, $\mathbb{P}(\mathcal{X}^m\cap K \neq \emptyset \ \ i.o.) = 0$.

(**C2**): Let $G\in \mathcal{G}$ satisfy $\mathcal{X}\cap G \neq \emptyset$. To prove that $\mathbb{P}(\mathcal{X}^m\cap G = \emptyset \ \ i.o.) = 0$, we proceed in three steps: (1) we show that sampling points $\boldsymbol{x}^j$ within $G$ occurs infinitely often (i.o.); (2) we use the growth property $\mathcal{X}^m\subseteq\mathcal{X}^{m+1}$ to rewrite (**C2**); (3) we relate the probability of sampling $\boldsymbol{x}^j$ within $G$ with the probability of $\mathcal{X}^m$ to intersect with $G$.

(1) The goal is to show $\mathbb{P} (\boldsymbol{x}^j\in G \ \ i.o.) = 1$.

We first note that $\{\omega \,|\, \boldsymbol{x}^j\in G\} = \{\omega \,|\, \boldsymbol{z}^j \ \text{s.t.} \ \boldsymbol{f}(\boldsymbol{z}^j) \in G\}$. Since the parameters $\boldsymbol{z}^j$ are sampled independently for each $j$, it can be shown that $\{\omega\,|\,\boldsymbol{x}^j\in G\}$ are also independent for $j=1,\ldots,m$.

Then, let $\mathcal{Z}_G\subset\mathbb{R}^z$ such that for all $\boldsymbol{z}\in\mathcal{Z}_G$, we have $\boldsymbol{f}(\boldsymbol{z})\in G$. By continuity of $\boldsymbol{f}(\cdot)$, $\mathcal{Z}_G$ is also an open set. Then, since $\mathcal{X}\cap G \neq \emptyset$ and by assumption on the sampling distribution over parameters, we have $\mathbb{P}(\boldsymbol{x}^j\in G) = \mathbb{P}(\boldsymbol{z}^j\in\mathcal{Z}_G)=\alpha_G >0$, where $\alpha_G$ does not depend on $j$ since the parameters $(\boldsymbol{x}_0,\boldsymbol{u},\boldsymbol{\theta},\boldsymbol{w})$ are sampled i.i.d.. Therefore, we obtain $\sum_{j=1}^\infty\mathbb{P}(\boldsymbol{x}^j\in G)=\infty$.

Next, since the events $\{\omega\,|\,\boldsymbol{x}^j\in G\}$ are independent, and by the above, we apply the second Borel-Cantelli lemma to obtain $\mathbb{P} (\boldsymbol{x}^j\in G \ \ i.o.) = \mathbb{P}\big(\cup_{n=1}^\infty\cap_{m=n}^\infty \boldsymbol{x}^j\in G\big) = 1$.

<!-- PDF page 12 -->

From this result and $\cap_{n=1}^\infty A_n \subseteq A_1$, we obtain that

$$\mathbb{P} (\boldsymbol{x}^j\in G \ \ i.o.) \leq \mathbb{P}\bigg(\bigcup_{m=1}^\infty\boldsymbol{x}^m\in G\bigg) \implies \mathbb{P}\bigg(\bigcup_{m=1}^\infty\boldsymbol{x}^m\in G\bigg) = 1. \tag{6}$$

(2) Second, we rewrite (**C2**) as follows:

$$\mathbb{P}(\mathcal{X}^m\cap G = \emptyset \ \ i.o.) = \mathbb{P}\bigg(\bigcap_{n=1}^\infty\bigcup_{m=n}^\infty \mathcal{X}^m\cap G = \emptyset\bigg) = 1 - \mathbb{P}\bigg(\bigcup_{n=1}^\infty\bigcap_{m=n}^\infty \mathcal{X}^m\cap G \neq \emptyset\bigg).$$

Since $\mathcal{X}^m\subseteq\mathcal{X}^{m+1}, \forall m$, we have that $\{\omega \, |\, \bigcap_{m=n}^\infty \mathcal{X}^m\cap G \neq \emptyset\}=\{\omega \, |\, \mathcal{X}^n\cap G \neq \emptyset\}$, and

$$\mathbb{P}\bigg(\bigcup_{n=1}^\infty\bigcap_{m=n}^\infty \mathcal{X}^m\cap G \neq \emptyset\bigg)=\mathbb{P}\bigg(\bigcup_{n=1}^\infty\mathcal{X}^n\cap G \neq \emptyset\bigg).$$

Therefore,

$$\mathbb{P}(\mathcal{X}^m\cap G = \emptyset \ \ i.o.) = 0 \iff \mathbb{P}\bigg(\bigcup_{n=1}^\infty\mathcal{X}^n\cap G \neq \emptyset\bigg) = 1. \tag{7}$$

(3) Finally, we combine the two results from above. First, we note that since $\boldsymbol{x}^j\in\mathcal{X}^j$, we have $\{\omega \,|\, \boldsymbol{x}^j(\omega) \in G\} \subseteq \{\omega \,|\, \mathcal{X}^j(\omega) \cap G \neq \emptyset\}$. Hence, we obtain

$$\bigcup_{j=1}^\infty\{\omega \,|\, \boldsymbol{x}^j(\omega) \in G\} \subseteq \bigcup_{j=1}^\infty\{\omega \,|\, \mathcal{X}^j(\omega) \cap G \neq \emptyset\}.$$

Combining with (6), we obtain:

$$\mathbb{P}\bigg(\bigcup_{n=1}^\infty\mathcal{X}^n\cap G \neq \emptyset\bigg) = 1. \tag{8}$$

Using (7), (8) is equivalent to $\mathbb{P}(\mathcal{X}^m\cap G = \emptyset \ \ i.o.) = 0$, which conludes the proof of (**C2**).

By Theorem 1, we conclude that the sequence $\{\mathcal{X}^m(\omega),m\geq 1\}$ almost surely converges to the deterministic set $\mathcal{X}$ as $m\rightarrow\infty$. As $\mathcal{X}$ is defined as the convex hull of the true reachable set $\mathrm{Co}(\mathcal{X}_k)$, this concludes our proof of Theorem 2. $\square$

<!-- PDF page 13 -->

## B Further Details and Applications of Adversarial Sampling

We present further results for adversarial sampling for $n_{\mathrm{adv}}\geq 1$ in Figure 7. First, we vizualize the effect of adversarial sampling on a planar version of the 13-dimensional nonlinear spacecraft system under uncertainty presented in Section 6. This result shows that taking more adversarial steps leads to samples concentrated at the boundaries of the reachable sets. However, this does not necessarily correlate with larger sets, since the convex hull over the samples is taken.

![Figure 7](../assets/s001-lew2021sampling/supplementary-figure-7.png)

**Figure 7:** Green: (**randUP**). Red: (**robUP!**). Effect of adversarial sampling for $n_{\mathrm{adv}} \in \{1,\ldots,5\}$ for a planar spacecraft system subject to uncertainty. Projection onto positions given a sequence of open-loop controls.

Next, we justify the choice of $M=100$ and $n_{\mathrm{adv}}=1$ when performing robust trajectory optimization in Section 6. Starting from $\boldsymbol{x}_{0}$, we perform 500 experiments where parameters $\boldsymbol{\theta}$, disturbances $\boldsymbol{w}_k$, and control trajectories within $\mathcal{U}$ are randomized. For different $M$ and $n_{\mathrm{adv}}$, we use (**robUP!**) and compare positional volume coverage, which is crucial to determine whether a given homotopy class of paths is feasible or not, due to obstacle avoidance constraints. Results in Figure 8 show that increasing $(M,n_{\mathrm{adv}})$ beyond $(100,1)$ does not lead to drastic improvements, compared to the volume of the experiment with largest $M$ and $n_{\mathrm{adv}}$. It is thus a reasonable choice of hyperparameters for this application. In Figure 9, we provide a visualization of the effect of adversarial sampling for this system, where all samples are projected onto $x,y$.

![Figure 8](../assets/s001-lew2021sampling/supplementary-figure-8.png)

**Figure 8:** To perform robust trajectory optimization for a spacecraft under uncertainty, we run 500 randomized experiments to choose $M$ and $n_{\mathrm{adv}}$. For an horizon $N = 20$, executing (**robUP!**) with $n_{\mathrm{adv}} = 1$ and $M\in\{50,100,200\}$ requires an average of $\{83,173, 304\}$ms, respectively, on a laptop with an i7-6700 CPU (2.60 GHz) and 8 GB of RAM.

![Figure 9](../assets/s001-lew2021sampling/supplementary-figure-9.png)

**Figure 9:** Effect of adversarial sampling for $M = 200$ and $n_{\mathrm{adv}}\in\{1,2,5\}$ (in red) on the projection onto $x,y$ positions of the sampled reachable sets at time $k=12$ for the spacecraft system under uncertainty. In green, (**randUP**) is shown for reference.

**Adversarial sampling for sensitivity analysis** Since (**robUP!**) actively searches for parameters and disturbances which lie outside the convex hull of the reachable states, it can be used to efficiently find parameters for which the system violates a property: a problem also known as falsification. In particular, further insight can be gained from the solution of the robust path of the robust spacecraft planning problem from Section 6. In Figure 10, the samples and convex hulls at times $k=8,14$ are shown. For each one, the sampled state $\boldsymbol{x}_k^j$ closest to obstacles is shown in red. Their respective sampled parameters $\boldsymbol{\theta}^j$ and disturbances $\boldsymbol{w}_k^j$ are equal to $(m^j,J_i^j) = (7.1,0.075)$ for $k = 8$, and $(7.3,0.065)$ for $k = 14$, with saturated $\boldsymbol{w}_{k}^j$ in opposite directions for the two particles. This indicates that all variables influence the size of the reachable sets. Moreover, a larger inertia does not necessarily correlate with smaller reachable sets, and both large and smaller values have an impact. For future applications, this methodology could be used to analyze the sensitivity of more challenging dynamical systems with respect to different parameters, guide sampling-based reachability analysis to respect a finite set of critical constraints, and design robust online adaptation rules for learning-based controllers.

![Figure 10](../assets/s001-lew2021sampling/supplementary-figure-10.png)

**Figure 10:** (**robUP!**) can be used for sensitivity analysis.

<!-- PDF page 14 -->

## C Additional Experimental Details

### C.1 Uncertainty Propagation using Lipschitz Continuity

In this section, we detail our implementation of the Lipschitz-based uncertainty propagation method which we compare with in Section 6. For these experiments, consider the dynamical system

$$\boldsymbol{x}_{k+1} = \boldsymbol{f}(\boldsymbol{x}_k) = \boldsymbol{h}(\boldsymbol{x}_k) + \boldsymbol{g}(\boldsymbol{x}_k), \quad \boldsymbol{x}_k\in\mathbb{R}^n. \tag{9}$$

Note that we drop the dependence on the control input $\boldsymbol{u}_k$ for conciseness, and since our comparisons concern a sequence of known open-loop controls. For simplicity, we assume $\boldsymbol{h}$ is an affine map, and $\boldsymbol{g}$ is Lipschitz continuous, such that for all $\boldsymbol{x},\boldsymbol{\mu}\in\mathbb{R}^n$,

$$|g_i(\boldsymbol{x})-g_i(\boldsymbol{\mu})| \leq L_{g_i} \|\boldsymbol{x}-\boldsymbol{\mu} \|_2, \quad i=1,\ldots,n. \tag{10}$$

The method presented in [13] consists of propagating ellipsoidal sets:

**Definition 2 (Ellipsoidal Set).** A set $\mathcal{B}(\boldsymbol{\mu}, \boldsymbol{Q})$, $\boldsymbol{\mu}\in\mathbb{R}^n,\boldsymbol{Q}\in\mathbb{R}^{n\times n}, \boldsymbol{Q}\succ 0$, is an ellipsoidal set if

$$\mathcal{B}(\boldsymbol{\mu} , \boldsymbol{Q}) := \left\{ \boldsymbol{x} \mid (\boldsymbol{x}-\boldsymbol{\mu})^T \boldsymbol{Q}^{-1} (\boldsymbol{x}-\boldsymbol{\mu}) \leq 1 \right\}. \tag{11}$$

Assume that $\boldsymbol{x}_k\in\mathcal{B}(\boldsymbol{\mu}_k,\boldsymbol{Q}_k)$. The problem consists of computing $\boldsymbol{\mu}_{k+1}, \boldsymbol{Q}_{k+1}$ such that $\boldsymbol{x}_{k+1}\in\mathcal{B}(\boldsymbol{\mu}_{k+1},\boldsymbol{Q}_{k+1})$. Generally, the reachable set of $\boldsymbol{f}(\boldsymbol{x}_k)$ given that $\boldsymbol{x}_k$ lies in an ellipsoidal set will not be an ellipsoidal set. However, an outer-approximation is sufficient for control applications where constraints satisfaction needs to be guaranteed. First, we compute the center of the ellipsoid as

$$\boldsymbol{\mu}_{k+1} = \boldsymbol{f}(\boldsymbol{\mu}_k). \tag{12}$$

Since $\boldsymbol{h}$ is affine, its Jacobian does not depend on $\boldsymbol{x}$. Thus, we decompose the error to the mean as

$$\begin{aligned} \boldsymbol{x}_{k+1}-\boldsymbol{\mu}_{k+1} &= \boldsymbol{h}(\boldsymbol{x}_k)-\boldsymbol{h}(\boldsymbol{\mu}_k)+\boldsymbol{g}(\boldsymbol{x}_k)-\boldsymbol{g}(\boldsymbol{\mu}_k) \\ &= \nabla \boldsymbol{h} \cdot (\boldsymbol{x}_k-\boldsymbol{\mu}_k)+\boldsymbol{g}(\boldsymbol{x}_k)-\boldsymbol{g}(\boldsymbol{\mu}_k). \end{aligned}$$

First, given $\boldsymbol{x}_k\in\mathcal{B}(\boldsymbol{\mu}_k,\boldsymbol{Q}_k)$, we have $\nabla \boldsymbol{h} \cdot (\boldsymbol{x}_k-\boldsymbol{\mu}_k)\in\mathcal{B}(\mathbf{0},\boldsymbol{Q}_{\mathrm{nom},k})$, with $\boldsymbol{Q}_{\mathrm{nom},k}=\boldsymbol{h}\boldsymbol{Q}_k\boldsymbol{h}^T$.

Second, we use the Lipschitz property of $\boldsymbol{g}$ to bound the approximation error component-wise as

$$|g_i(\boldsymbol{x}_k)-g_i(\boldsymbol{\mu}_k)|\leq L_{g_i} \|\boldsymbol{x}_k-\boldsymbol{\mu}_k\|_2\leq L_{g_i} \lambda_{\max}(\boldsymbol{Q}_k), \tag{13}$$

where $\lambda_{\max}(\boldsymbol{Q}_k)$ denotes the largest eigenvalue of $\boldsymbol{Q}_k$, and since $\boldsymbol{x}_k\in\mathcal{B}(\boldsymbol{\mu}_k,\boldsymbol{Q}_k)$. This defines a rectangular set in which $\boldsymbol{g}(\boldsymbol{x}_k)-\boldsymbol{g}(\boldsymbol{\mu}_k)$ is guaranteed to lie, which can be outer-approximated by an ellipsoid as

$$\boldsymbol{g}(\boldsymbol{x}_k)-\boldsymbol{g}(\boldsymbol{\mu}_k)\in\mathcal{B}(\mathbf{0},\boldsymbol{Q}_{\boldsymbol{g}_k}), \quad \text{where} \ \ \boldsymbol{Q}_{\boldsymbol{g}_k}=n\cdot\mathrm{diag}\big((L_{g_i}\lambda_{\max}(\boldsymbol{Q}_k)^2), \ i=1,\ldots,n \big), \tag{14}$$

where $\mathrm{diag}(\ldots)$ denotes the diagonal matrix with diagonal components $(\ldots)$.

Finally, the two terms can be combined as

$$\boldsymbol{x}_{k+1}-\boldsymbol{\mu}_{k+1} \in \mathcal{B}(\mathbf{0},\boldsymbol{Q}_{\mathrm{nom},k}) \oplus \mathcal{B}(\mathbf{0},\boldsymbol{Q}_{\boldsymbol{g}_k}) \subset \mathcal{B}(\mathbf{0},\boldsymbol{Q}_{k+1}), \tag{15}$$

where $\boldsymbol{Q}_{k+1}=\frac{c+1}{c}\boldsymbol{Q}_{\mathrm{nom},k} + (1+c)\boldsymbol{Q}_{\boldsymbol{g}_k}$, with $c=\sqrt{\mathrm{Tr}(\boldsymbol{Q}_{\mathrm{nom},k}/\mathrm{Tr}(\boldsymbol{Q}_{\boldsymbol{g}_k})}$, and $\mathrm{Tr}(\cdot)$ denotes the trace operator. Finally, combining the terms above and by linearity,

$$\boldsymbol{x}_{k+1} \in \mathcal{B}(\boldsymbol{\mu}_{k+1},\boldsymbol{Q}_{k+1}). \tag{16}$$

Starting from $\boldsymbol{x}_0\in\mathcal{B}(\boldsymbol{\mu}_0,\boldsymbol{Q}_0)$, and applying this recursion for all $k=0,\ldots, N-1$, this method enables the computation of sequence of sets which outer approximate the true reachable sets of the nonlinear system, given known upper-bounds for the Lipschitz constant of the dynamics.

<!-- PDF page 15 -->

### C.2 Neural network experiment and comparisons

**Neural network training** To simplify training, aid generalization, and simplify comparisons with the Lipschitz-based method (see C), we decompose the dynamics as $\boldsymbol{x}_{k+1}=\boldsymbol{f}(\boldsymbol{x}_k,\boldsymbol{u}_k)=\boldsymbol{h}(\boldsymbol{x}_k)+\boldsymbol{g}(\boldsymbol{x}_k,\boldsymbol{u}_k)$, where $\boldsymbol{h}(\boldsymbol{x}_k)=\boldsymbol{x}_k$ is a known nominal term which captures prior knowledge about the system, and $\boldsymbol{g}$ is unknown and needs to be learned by the neural network. We opt for a feed-forward network architecture with $2$ hidden layers of width $128$ each, with $\tanh(\cdot)$ activation functions. To train the neural network, we re-sample states and controls at each training step as described in the next section, giving rise to the tuples $\{(\boldsymbol{x}_k,\boldsymbol{u}_k,\boldsymbol{x}_{k+1})^b\}_{b=1}^B$. We use a single-step quadratic loss $\sum_{b=1}^B \|\boldsymbol{x}_{k+1}^b-\boldsymbol{g}(\boldsymbol{x}_k^b,\boldsymbol{u}_k^b)\|_2^2$, a batch size $B=20$, and include standard $L_2$-regularization with weight $10^{-6}$. All code is written using PyTorch [46], and the model is trained using *Adam* [48], with an initial learning rate of $0.02$, and a decay factor of $(1-10^{-6})$ every gradient descent step. After 10k training steps, the model achieves a loss of around $10^{-7}$ on the validation dataset. We perform further validation through multi-steps rollouts of the system (over 20 timesteps). By adopting a model architecture which leads to minimal error, we are able to compare the reachable sets of the true linear system with those of the neural network, and evaluate volume coverage.

**Randomization** To provide comparisons of volume coverage, we perform $B = 100$ experiments where we randomize initial states $\boldsymbol{x}_0^b \in \mathcal{X}_0 = \mathcal{B}(\boldsymbol{\mu}_0,\boldsymbol{Q}_0)$ and open-loop control trajectories $\boldsymbol{u}^b = (\boldsymbol{u}_0^b,\ldots,\boldsymbol{u}_{N-1}^b)$, $b = 1,\ldots,B$. We sample $\boldsymbol{\mu}_0^b = (\mathbf{p}_0^b,\mathbf{v}_0^b)$ with $\mathbf{p}_{0,i}^b\sim\mathrm{Unif}(-5,5)$, $\mathbf{v}_{0,i}^b\sim\mathrm{Unif}(-1,1)$, and constant $\boldsymbol{Q}_0^b=10^{-3}\mathrm{diag}([10,10,2,2])$. We sample controls as $\boldsymbol{u}_k^b=\bar{\boldsymbol{u}}^b+\delta\boldsymbol{u}_k^b$ with $\bar{\boldsymbol{u}}^b_i\sim\mathrm{Unif}(-0.4,0.4)$ and $\delta\boldsymbol{u}_{k,i}^b\sim\mathrm{Unif}(-0.02,0.02)$ for neural network training, and with $\bar{\boldsymbol{u}}^b_i\sim\mathrm{Unif}(-0.1,0.1)$ and $\delta\boldsymbol{u}_{k,i}^b\sim\mathrm{Unif}(-0.005,0.005)$ for evaluation in Figure 5.

**Computation time** In average, for this neural network, ( (**randUP**)$^{1\mathrm{k}}$, ($\cdot$)$^{3\mathrm{k}}$, ($\cdot$)$^{10\mathrm{k}}$, (**robUP!**)$^{1\mathrm{k}}_{1}$ ) require (9,28,120,648) ms on a laptop with an i7-6700 CPU (2.60GHz) and 8GB of RAM. We did not optimize our implementation. Performing operations in parallel and using a GPU would further accelerate both methods.

**Lipschitz method** In our experiments, we use $\boldsymbol{h}(\boldsymbol{x})=\boldsymbol{x}$, and train a neural network to represent $\boldsymbol{g}(\boldsymbol{x},\boldsymbol{u})$. To reduce conservatism in our comparisons, we use the Lipschitz constant of the true linear system $\boldsymbol{x}_k = (\boldsymbol{p}_k,\boldsymbol{v}_k) \in \mathbb{R}^4$, $\boldsymbol{u}_k \in \mathbb{R}^2$, $\boldsymbol{p}_{k+1} = \boldsymbol{p}_k + \boldsymbol{v}_k$, and $\boldsymbol{v}_{k+1} = \boldsymbol{v}_k + \boldsymbol{u}_k$, which are given as $L_{g_i}=1$ for $i=1,2$, and $L_{g_i}=0$ for $i=3,4$.

**Volume computation** Finally, the volume of the ellipsoidal sets $\mathcal{B}(\boldsymbol{\mu},\boldsymbol{Q})$ are computed in closed form as

$$\mathrm{Vol}(\mathcal{B}(\boldsymbol{\mu},\boldsymbol{Q})) = \frac{\pi^{n/2}}{\Gamma(n/2+2)}\frac{1}{\sqrt{\mathrm{det}(\boldsymbol{Q}^{-1})}}, \tag{17}$$

where $\Gamma(\cdot)$ is the standard gamma function of calculus [49].

## D Robust Trajectory Optimization with Sampling-based Convex Hulls

**Problem formulation** This section proposes a method to perform (approximately) robust trajectory optimization using sampling-based reachability analysis, and sequential convex programming (SCP). Specifically, we extend the method presented in [8] to leverage sampling-based convex hulls.

In the following, we use the same assumptions and notations outlined in Section 2. The goal consists of computing an open-loop trajectory $(\boldsymbol{x}_{0:N},\boldsymbol{u}_{0:N-1})$ which satisfies all constraints $(\boldsymbol{x}_k\in\mathcal{X}_{\text{free}},\boldsymbol{u}_k\in\mathcal{U})$, for any bounded uncertain parameter $\boldsymbol{\theta}\in\Theta$ and disturbances $\boldsymbol{w}_k\in\mathbb{W}$. The initial state $\boldsymbol{x}_0$ is uncertain and lies within a known initial bounded set $\mathcal{X}_0$, and the final state $\boldsymbol{x}_N$ should lie within the final goal region $\mathcal{X}_{\text{goal}}$. The trajectory should minimize the step and final cost functions $l:\mathcal{X}\times\mathcal{U}\rightarrow\mathbb{R}, \ l_f:\mathcal{X}\rightarrow\mathbb{R}$ (e.g., fuel consumption, and final velocity). To make this problem tractable, given a sequence of control inputs $\boldsymbol{u} = (\boldsymbol{u}_0,\ldots,\boldsymbol{u}_{N-1})$, we define the nominal trajectory $\boldsymbol{\mu} = (\boldsymbol{\mu}_0,\ldots,\boldsymbol{\mu}_N)$, from a fixed $\boldsymbol{\mu}_0 \in \mathcal{X}_0$, as

$$\boldsymbol{\mu}_{k+1}=\boldsymbol{f}(\boldsymbol{\mu}_k,\boldsymbol{u}_k,\bar{\boldsymbol{\theta}},\bar{\boldsymbol{w}}_k), \quad \bar{\boldsymbol{\theta}}\in\Theta, \ \ \bar{\boldsymbol{w}}_k\in\mathbb{W}, \tag{18}$$

where $\bar{\boldsymbol{\theta}}$ and $\bar{\boldsymbol{w}}_k$ are fixed nominal parameters and disturbances. Given this nominal trajectory, we aim to minimize the cost of the nominal trajectory $\sum_{k=0}^{N-1} l(\boldsymbol{\mu}_k, \boldsymbol{u}_k)+l_f(\boldsymbol{\mu}_N)$, subject to all

<!-- PDF page 16 -->

constraints defined above. We define the following robust optimal control problem:

**Robust Optimal Control Problem**

$$\min_{\boldsymbol{u}_{0:N-1}} \qquad \sum_{k=0}^{N-1} l(\boldsymbol{\mu}_k, \boldsymbol{u}_k) + l_f(\boldsymbol{\mu}_N) \tag{19a}$$

$$\text{subject to}\qquad \boldsymbol{x}_{k+1} = \boldsymbol{f}(\boldsymbol{x}_k,\boldsymbol{u}_k,\boldsymbol{\theta},\boldsymbol{w}_k), \quad \boldsymbol{w}_k\in\mathbb{W}, \ \ \boldsymbol{\theta}\in\Theta, \quad k=0, \ldots,N-1, \tag{19b}$$

$$\bigwedge_{k=1}^N\big(\boldsymbol{x}_{k} \in \mathcal{X}_{\text{free}}\big) \ \cap \ \bigwedge_{k=0}^{N-1}\big(\boldsymbol{u}_{k} \in \mathcal{U}\big) \ \cap \ \big(\boldsymbol{x}_{N} \in \mathcal{X}_{\text{goal}}\big) \ \cap \ \big(\boldsymbol{x}_{0} \in \mathcal{X}_0\big). \tag{19c}$$

Using the reachable sets $\{\mathcal{X}_k\}_{k=0}^N$ defined in (2), and the nominal trajectory in (18), it is possible to show that the previous problem is equivalent to the following problem:

**Reachability-Aware Optimal Control Problem**

$$\min_{\boldsymbol{u}_{0:N-1}} \ \ \sum_{k=0}^{N-1} l(\boldsymbol{\mu}_k, \boldsymbol{u}_k)+l_f(\boldsymbol{\mu}_N) \quad \text{s.t.} \ \ \bigwedge_{k=1}^N \mathcal{X}_{k} \subset \mathcal{X}_{\text{free}}, \ \ \ \bigwedge_{k=0}^{N-1}\boldsymbol{u}_{k} \in \mathcal{U}, \ \ \ \mathcal{X}_{N} \subset \mathcal{X}_{\text{goal}}, \tag{20}$$

where $\{\mathcal{X}_k\}_{k=0}^N$ depend on the chosen sequence of controls $\boldsymbol{u}_{0:N-1}$, and are computed from $\mathcal{X}_{0}$. In this work, the reachable sets are approximated using either (**randUP**) or (**robUP!**), which yield convex hulls. However, we show next that computing the convex hull of the samples $\boldsymbol{x}_k^j$ is not always necessary to reformulate common constraints found in robotic applications.

**Sequential convex programming (SCP) and constraints reformulation** In this work, we leverage SCP to solve (20). The SCP technique consists of iteratively formulating convex approximations of (20), and solving each sub-problem using convex optimization. Specifically, at each iteration $(i+1)$, the previous nominal solution $(\boldsymbol{\mu}^i,\boldsymbol{u}^i)$ is used to linearize all constraints, and reformulate (20) as a quadratic program with linear constraints which can be efficiently solved using **OSQP** [50]. The solution of this problem, denoted as $(\boldsymbol{\mu}^{i+1},\boldsymbol{u}^{i+1})$, should approach the solution of (20) at convergence, which can be assessed by evaluating $\|\boldsymbol{\mu}^{i+1}-\boldsymbol{\mu}^i\|+\|\boldsymbol{u}^{i+1}-\boldsymbol{u}^i\|$. In this work, we use the open-source SCP procedure presented in [8]$^5$, which includes trust region constraints and additional parameter adaptation rules to encourage convergence to a locally optimal solution to the original non-convex problem.

Next, we present simple methods to use sampling-based reachable sets to reformulate constraints. First, consider dimension-wise constraints of the form

$$\boldsymbol{x}_{\min,i}\leq\boldsymbol{x}_{k,i}(\boldsymbol{u})\leq\boldsymbol{x}_{\max,i}, \ \ \ \forall (\boldsymbol{x}_0,\boldsymbol{\theta},\boldsymbol{w}_{0:k-1}) \in \mathcal{X}_0\times\Theta\times\mathbb{W}^k, \tag{21}$$

where $i\in\{1,\ldots,n\}$. For instance, such constraints can represent velocity bounds, and are incorporated within $\boldsymbol{x}_k\in\mathcal{X}_{\text{free}}$ in (19c). To reformulate such constraints using the reachable set $\mathcal{X}_k(\boldsymbol{u})$ and the nominal trajectory $\boldsymbol{\mu}$, it suffices to compute its outer-bounding rectangle $\Delta_k(\boldsymbol{u})$, defined as $\Delta_k=\{\boldsymbol{x}_k \,| \, |\boldsymbol{x}_{k,i}-\boldsymbol{\mu}_{k,i}|\leq \delta_{k,i}\}$. Using (**randUP**) or (**robUP!**), the bounds $\delta_{k,i}=\max_{j}|\boldsymbol{x}_{k,i}^j-\boldsymbol{\mu}_{k,i}|$ can be efficiently computed. With these rectangular sets, (21) is conservatively reformulated as

$$\boldsymbol{x}_{\min,i}+\delta_{k,i}(\boldsymbol{u})\leq\boldsymbol{\mu}_{k,i}(\boldsymbol{u})\leq\boldsymbol{x}_{\max,i}-\delta_{k,i}(\boldsymbol{u}). \tag{22}$$

Next, linear constraints $\mathbf{a} \cdot \boldsymbol{x}_{k,1:s} \leq b$ on the $s$ first components of $\boldsymbol{x}_k$, with $\mathbf{a}\in\mathbb{R}^s,b\in\mathbb{R}$ can be reformulated using outer-bounding ellipsoidal sets for the $s$ first components of $\boldsymbol{x}$: $\mathcal{B}^s(\boldsymbol{\mu}_k , \boldsymbol{Q}_k) = \left\{ \boldsymbol{x} \mid (\boldsymbol{x}-\boldsymbol{\mu}_{k,1:s})^T \boldsymbol{Q}_k^{-1} (\boldsymbol{x}-\boldsymbol{\mu}_{k,1:s}) \leq 1 \right\}$. Following derivations in Section C.1, $\boldsymbol{Q}_k$ can be computed as $\boldsymbol{Q}_k = s \cdot \mathrm{diag}(\delta_i^2, \, i = 1,\ldots,s)$, yielding an ellipsoidal set $\mathcal{B}^s$ which outer-approximates the reachable set $\mathcal{X}_k$ (projected onto its $s$ first dimensions). Using this ellipsoidal set, the linear constraint $\mathbf{a} \cdot \boldsymbol{x}_{k,1:s} \leq b$ is conservatively reformulated as $\mathbf{a}^T\boldsymbol{\mu}_{k,1:s}+(\mathbf{a}^T\boldsymbol{Q}_k\mathbf{a})^{1/2} \leq b$, following similar derivations as in [8, 13]. Finally, this constraint is linearized, to yield a convex reformulation of the original constraints (19c), and obtain a convex quadratic program with linear constraints which can be solved using **OSQP**. For the spacecraft planning problem in Section 6, such linear constraints are obtained from non-convex obstacle avoidance constraints, by expressing them using the signed distance function, and linearizing the expression. This procedure is described in [8], where it is shown that it is conservative for general convex obstacles.

Footnote 5: The implementation of [8] is available at github.com/StanfordASL/ccscp.
