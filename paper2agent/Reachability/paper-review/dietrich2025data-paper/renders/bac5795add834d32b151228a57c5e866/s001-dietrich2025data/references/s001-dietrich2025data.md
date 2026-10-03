## Conversion notes

- Source version: arXiv:2504.06541v2 [eess.SY], dated 11 Sep 2025 (7 pages, IEEE two-column conference format; arXiv version of the CDC 2025 paper by E. Dietrich, R. Devonport, S. Tu and M. Arcak; the first page carries a ©2025 IEEE notice).
- Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (root.tex, reachable_fig.tex, root.bbl) and checked against the PDF pages; cross-references, equation numbers and citations are given as printed. No formula is kept as an image. Printed equation numbers are (1)-(14); several displays are unnumbered in print and carry no tag here.
- Notation of the transcription: the indicator printed with a double-struck 1 (TeX \mathds{1}) is written \mathbb{1}; \theta^* is written \theta^{\ast}; the violation level is one printed glyph throughout, written \epsilon in Sections II to V-A and \varepsilon in Section V-B as in the authors' source. Authors' inconsistencies and typos are kept as printed (for example k without a hat in Section II-E and in the Computation paragraph, the subscript of the indicator in (5), R(\theta) without a hat in Section II-C, "futher", "critize", "Alburquerque").
- Reading order: the unnumbered first-page author note and the IEEE copyright notice follow the author line; Figure 1 (printed at the top of page 3) follows Theorem 1 and the paragraph after it; Figures 2 and 3 follow the paragraphs that cite them; Footnote 1 follows the paragraph that carries its mark. The text and formulas printed inside Figure 1 are also transcribed after its caption. Tables I and II are CSV files (11 rows x 5 columns each, cells as printed) with a conversion note on the row-group label.
- Scope of this version: no appendix or supplementary material. Theorem 1 is stated with a citation to [28, Thm. 3.3] and has no proof in the paper; Lemma 1 has a proof. The vertical arXiv stamp on page 1 is omitted as page furniture.

<!-- PDF page 1 -->

# Data-Driven Reachability with Scenario Optimization and the Holdout Method

Elizabeth Dietrich, Rosalyn Devonport, Stephen Tu, and Murat Arcak

E. Dietrich and M. Arcak are with the University of California, Berkeley, USA. Email: `{eadietri, arcak}@berkeley.edu`. R. Devonport is with the University of New Mexico, Alburquerque, USA. Email: `devonport@unm.edu`. S. Tu is with the University of Southern California, USA. Email: `stephen.tu@usc.edu`.

©2025 IEEE. Personal use of this material is permitted. Permission from IEEE must be obtained for all other uses, in any current or future media, including reprinting/republishing this material for advertising or promotional purposes, creating new collective works, for resale or redistribution to servers or lists, or reuse of any copyrighted component of this work in other works.

## Abstract

Reachability analysis is an important method in providing safety guarantees for systems with unknown or uncertain dynamics. Due to the computational intractability of exact reachability analysis for general nonlinear, high-dimensional systems, recent work has focused on the use of probabilistic methods for computing approximate reachable sets. In this work, we advocate for the use of a general purpose, practical, and sharp method for data-driven reachability: *the holdout method*. Despite the simplicity of the holdout method, we show—on several numerical examples including scenario-based reach tubes—that the resulting probabilistic bounds are substantially sharper and require fewer samples than existing methods for data-driven reachability. Furthermore, we complement our work with a discussion on the necessity of probabilistic reachability bounds. We argue that any method that attempts to *de-randomize* the bounds, by converting the guarantees to hold deterministically, requires (a) an exponential in state-dimension amount of samples to achieve non-vacuous guarantees, and (b) extra assumptions on the dynamics.

## I. Introduction

Reachability analysis plays an integral role in analyzing system safety by determining the set of states a system can transition to in a finite time horizon [1]. Many set-based techniques [2]–[5] have been developed to compute under- or over-approximated reachable sets to capture all possible trajectories and present guarantees on state-space safety. However, when there is limited information on a system’s dynamics, through only simulation or experimentation, we must estimate reachable sets and derive probabilistic guarantees of correctness directly from data. To provide probability measures for learned reachable sets, many approaches require a minimum number of samples [6]–[9] or assumptions on the system dynamics [10]–[12], and are often computationally intensive [13], [14]. We advocate for the use of a general purpose method, *the holdout method*, that circumvents these limitations and improves the sample complexity and sharpness of existing probabilistic reachability bounds.

The holdout method, or cross-validation, is one of the simplest and most widely used methods for estimating prediction error and providing statistical guarantees [15]–[18]. While this method has been utilized across disciplines for decades, its biggest limitation is the availability of data. The holdout method requires a validation set that is only used to assess the performance of the prediction model. If data is scarce, this can lead to test-set contamination or a small test-set size. However, in the context of data-driven reachability analysis, especially simulation-based approaches, generating new data sets avoids these issues and can be computationally efficient.

There are numerous works investigating other statistical learning techniques for data-driven reachability analysis, including approaches such as scenario optimization [19]–[21], conformal prediction [22]–[24], and Gaussian processes [11], [25]. While many of these works rely on a-priori sample complexities, [19] calculates a-posteriori probability bounds using a wait-and-judge perspective. Therefore, we compare the a-posteriori bounds we achieve with the holdout method directly to the wait-and-judge perspective to demonstrate the stronger and more computationally-efficient guarantees that we are able to obtain. Further, in contrast to existing approaches, the holdout method provides a general purpose framework, amenable to any reachable set estimator, and it does not require any prior knowledge about system dynamics or sample complexity.

To conclude our work, we include a discussion on the necessity of probabilistic bounds in the context of data-driven reachability analysis. We argue that any attempt to *de-randomize* a probabilistic bound—that is, convert a probabilistic bound into a deterministic bound via enlargement of the reachable set—must not only make extra assumptions on the dynamics (e.g., Lipschitz bounds on the transition function), but also requires an exponential in state-dimension number of scenarios to obtain non-vacuous guarantees.

## II. Problem Statement

### A. Forward Reachable Sets.

A forward reachable set is defined as $R = \{\Phi(t_1; t_0, x_0, d) : x_0 \in X_0, d \in D\}$ where $X_0 \subseteq \mathbb{R}^{n_x}$ is the set of initial states, $D$ is the set of disturbance signals $d : [t_0, t_1] \rightarrow \mathbb{R}^{n_d}$, and $\Phi : X_0 \times D \rightarrow \mathbb{R}^{n_x}$ is the state transition function. This is the set of all states to which the system can transition to at time $t_1$ from states $X_0$ at time $t_0$ subject to disturbances in $D$. Since we cannot compute exact reachable sets, we aim to compute an approximation, $\hat{R}$, that is close to the true reachable set in a probabilistic sense.

To compute such an approximation, we first endow both $X_0$ and $D$ with probability distributions $\mu_{X_0}$ and $\mu_D$, respectively. Let $\Delta$ be the resulting probability space from which we draw samples $\delta^{(i)} = \Phi(t_1; t_0, x_{0i}, d_i), i = 1, \dots, N$ where $x_{01}, \dots, x_{0N} \overset{i.i.d}{\sim} \mu_{X_0}$, $d_1, \dots, d_N \overset{i.i.d}{\sim} \mu_D$. We compute a reachable set estimate in the form of a sublevel set of a parameterized function

$$
\hat{R}(\theta) = \{x \in \mathbb{R}^{n_x} : g(x, \theta) \leq 0\} \tag{1}
$$

<!-- PDF page 2 -->

where $g : \mathbb{R}^{n_x} \times \mathbb{R}^{n_\theta} \rightarrow \mathbb{R}$. In (1), $\theta$ represents a parameterization of the class of admissible reachable set estimators: to fix a value of $\theta$ is to choose an estimator.

### B. Violation Probability.

Given the samples $\delta^{(1)}, \dots, \delta^{(N)}$ and a desired confidence parameter $\beta$, we wish to find the minimum-volume reachable set that contains the samples and satisfies the probabilistic guarantee $\mathbf{P}\{V(\hat{R}(\theta)) > \epsilon\} \leq \beta$. The violation probability $V(\hat{R}(\theta))$, or true error $e$, of the reachable set estimate, $\hat{R}(\theta)$, is defined as the probability that an unseen scenario will violate the reachable set:

$$
e \equiv V(\hat{R}(\theta)) \equiv \mathbf{P}_{\delta \sim \Delta}\{ g(\delta, \theta) > 0\} \equiv \mathbf{P}_{\delta \sim \Delta}\{ \delta \notin \hat{R}(\theta) \}. \tag{2}
$$

In other words, if $V(\hat{R}(\theta)) \leq \epsilon$, then our reachable set estimate is robust against constraint violation at level $\epsilon$. Since the true error is not an observable quantity, we utilize the empirical error. Given a new sample set of size $M$ drawn from $\Delta$, the empirical error $\hat{e}$, or test error, is the observed number of scenarios that violate the reachable set estimate:

$$
\hat{e} \equiv \hat{V}(\hat{R}(\theta)) \equiv \mathbf{P}_{\delta_s \sim \Delta}\{ \delta_s \notin \hat{R}(\theta) \} \tag{3}
$$

$$
\equiv \frac{1}{M}\sum_{i=1}^{M} \mathbb{1}_{\hat{R}(\theta)}(\delta_s^{(i)}) \tag{4}
$$

where

$$
\mathbb{1}_{\hat{R}}(\theta)(\delta_s^{(i)}) = \Bigg\{ \begin{array}{ll}
1 & \text{if } \delta_s^{(i)} \notin \hat{R}(\theta) \\
0 & \text{else}.
\end{array} \tag{5}
$$

Given $\hat{e}$ and $\beta$, we will obtain an appropriate $\epsilon$ to satisfy the bound $\mathbf{P}\{V(\hat{R}(\theta)) > \epsilon\} \leq \beta$ in Section III.

### C. Nonconvex Scenario Reachability Analysis

To calculate reachable set estimates of the form (1), we utilize scenario optimization. Scenario optimization is an approach to solving chance-constrained optimization problems by solving a non-probabilistic relaxation of the original problem [26]. We fix a functional $\mathrm{Vol} : \mathbb{R}^{n_\theta} \rightarrow \mathbb{R}_{\geq 0}$ that acts as a proxy for the volume of $R(\theta)$. This motivates the following scenario program:

$$
\begin{aligned}
& \underset{\theta}{\text{minimize}} & & \mathrm{Vol}(\theta) \\
& \text{subject to} & & g(\delta^{(i)}, \theta) \leq 0, i = 1, \dots, N \\
& & & \theta \in \mathbb{R}^{n_\theta}.
\end{aligned} \tag{6}
$$

The solution to (6) is the minimum-volume set that contains sample points $\delta^{(1)}, \dots, \delta^{(N)}$. In [19], we present two methods for estimating these nonconvex reachable sets, including the sum of radial basis functions, as demonstrated in Section IV.

### D. Wait-and-Judge

Given a scenario program of the form (6), one approach for computing probabilistic bounds is *wait-and-judge* [19]. The wait-and-judge perspective, combined with nonconvex scenario optimization [27], determines $\epsilon$ a-posteriori as a function of support scenarios. A support scenario is any scenario whose removal changes the solution to (6). This approach requires re-solving the scenario program upon removal of each individual scenario. Therefore, this approach can be computationally intensive for systems with high dimensionality or complexity. We refer readers to [19] for more details on computing $\epsilon$. Since we calculate the probability measure of our reachable set after solving the optimization problem, the nonconvex scenario approach is amenable to alternative statistical analysis techniques, such as the holdout method, as discussed in Section III.

### E. Binomial Tail Inversion.

To calculate probabilistic bounds for (6), we employ the holdout method given a sample set of size $M$. We would like to calculate the probability of observing at most $k$ reachable set violations out of $M$ samples. From a statistical perspective, this can be viewed as computing a tail bound for a binomial distribution. We use a binomial tail inversion to obtain the largest true error $e$ such that the probability of $k$ or more samples violating the reachable set is at least $\beta$ [28]. This calculates the bound on the true error given the empirical error $\hat{e}$, or the empirical count of boundary violations $\hat{k}$, and confidence $\beta$.

**Definition 1.** (Binomial Tail Inversion) For $\hat{k}$ violations out of $M$ newly sampled scenarios and all $\beta \in (0, 1]$:

$$
\overline{\text{Bin}}(\hat{k}, M, \beta) = \max_{e}\Bigl\{ e : \text{Bin}\Bigl(\hat{k}, M, e \Bigr) \geq \beta \Bigr\}, \,\,\text{where} \tag{7}
$$

$$
\text{Bin}\Bigl(\hat{k}, M, e \Bigr) = \sum_{j=0}^{\hat{k}} \binom{M}{j} e^j (1-e)^{M-j}. \tag{8}
$$

## III. The Holdout Method

We present a technique that utilizes the *holdout method* to a-posteriori evaluate the robustness level of the scenario solution to (6) by obtaining an empirical estimate of the accuracy of a given reachable set approximation. This well-known method offers a modular technique for computing probabilistic bounds. In particular, we demonstrate the use of the holdout method in nonconvex scenario reachability analysis; we tighten the probabilistic bounds that were first introduced in [19], as shown in Fig. 1. However, it is important to mention that the holdout method works for *any* parameterization of a reachable set estimator, including those that arise from neural networks.

The holdout method is a foundational paradigm of data-driven methodologies. It employs a test set of $M$ fresh scenarios to provide a good risk estimate for a given model [29]. Therefore, we draw a *new* set of samples $\delta^{(i)}_s = \Phi(t_1; t_0, x_{0i}^s, d_i^s), i = 1, \dots, M$ where $x_{01}^s, \dots, x_{0M}^s \overset{i.i.d}{\sim} \mu_{X_0}$, $d_1^s, \dots, d_M^s \overset{i.i.d}{\sim} \mu_D$, and test the accuracy of our estimate $\hat{R}(\theta)$ on $\delta_s^{(1)}, \dots, \delta_s^{(M)}$. Given $\hat{k}$ reachable set violations out of $M$ samples, or the empirical error (4), we are able to use a binomial tail bound, as introduced in Section II-E, to calculate a bound on the true error (2) of the reachable set. We formulate this in the following theorem:

<!-- PDF page 3 -->

**Theorem 1.** (Adapted from [28, Thm. 3.3]) Given any $\beta \in (0, 1)$, empirical count of boundary violations $\hat{k}$, and size of test set $M$, the following probability bound holds for the reachable set estimate $\hat{R}(\theta)$:

$$
\mathbf{P} \{ V(\hat{R}(\theta)) > \overline{\text{Bin}}(\hat{k}, M, \beta) \} \leq \beta. \tag{9}
$$

It is important to note that the probability above is taken with respect to the $M$ holdout samples $\delta_s^{(1)}, \dots, \delta_s^{(M)}$, with the estimated reachable set $\hat{R}(\theta)$ held fixed. This bound is, virtually, perfectly tight; the bound on the true error of our reachable set is violated exactly a $\beta$ portion of the time [28]. In Section IV, we will demonstrate the efficiency of this method when collecting samples is computationally cheap.

![Figure 1](../assets/s001-dietrich2025data/figure-1.png)

Fig. 1. Using nonconvex scenario reachability analysis, we calculate reachable set estimates, $\hat{R}(\theta)$, in the form of a constrained optimization problem. Specifically, we construct $\hat{R}(\theta)$ from a finite set of radial basis functions. We illustrate the output of this method through reach sets of a single time instance and reach tubes. Finally, we utilize the holdout method, and a binomial tail inversion, to calculate probabilistic bounds for $\hat{R}(\theta)$.

Text inside Figure 1 (transcribed from the figure image; three boxes connected left to right by arrows). Left box, titled "Nonconvex Scenario Reachability": $\underset{\theta}{\text{minimize}} \;\; \text{Vol}(\theta)$ subject to $\theta \in \underset{i = 1, ..., N}{\bigcap} \{\theta_i : g(\delta^{(i)}, \theta_i) \leq 0\}$. Middle box, titled "Reachable Set Estimate": two small plots labelled "Time Instance:" and "Tube:". Right box, titled "Holdout Method": $\mathbf{P} \{ V(\hat{R}(\theta)) > \epsilon\} \leq \beta$ and $\epsilon := \overline{\text{Bin}}(\hat{k}, M, \beta)$, above a small plot of a bell-shaped curve with its left tail shaded.

**Computation.** To calculate the binomial tail inversion (cf. Definition 1), we use the SciPy Python library to solve an optimization problem with the sequence’s cumulative distribution function (CDF) as a constraint, as seen in (7). Since the binomial tail inversion reduces to inverting a one-dimensional function, it can be computed efficiently using standard optimization routines, such as Quasi-Newton methods. Additionally, one can exploit the monotonically decreasing property of the function $e \mapsto \mathrm{Bin}(k, M, e)$ on the interval $[0, 1]$ and utilize a simple bisection method.

**Order-wise scaling of binomial tail inversion.** In general, $\overline{\text{Bin}}(\hat{k}, M, \beta)$ does not have a closed-form solution. However, we can obtain an order-wise scaling to illustrate the dependence on $\hat{k}$, $M$, and $\beta$. First, suppose that no violations were observed on our holdout dataset ($\hat{k} = 0$). Then, we have the following bound $\overline{\text{Bin}}(0, M, \beta) \leq \frac{\log(1/\beta)}{M}$ [28, Corollary 3.4]. This illustrates a $1/M$ dependence (known as a “fast-rate” in statistics) in the number of holdout samples $M$, in addition to a logarithmic dependence, $\log(\frac{1}{\beta})$, on the failure probability $\beta$. In the general case, when $\hat{k} > 0$, we have the looser scaling

$$
\overline{\text{Bin}}(\hat{k}, M, \beta) \leq \frac{\hat{k}}{M} + O\Bigl(\sqrt{\frac{\log(\frac{1}{\beta})}{M}}\Bigr), \tag{10}
$$

which is the typical scaling in $M$ predicted by the Central Limit Theorem.

**Zero violation reachable sets.** The holdout method, compared to approaches, such as wait-and-judge (which do not require a separate holdout dataset), is not able to guarantee zero violations on the complete dataset. However, we show in Section IV, that while the wait-and-judge method computes a reachable set estimate with zero dataset violations, the final violation probability, $V(\hat{R}(\theta))$, is substantially more conservative than the holdout method.

**Marginal probability over training and holdout data.** Theorem 1 provides a bound over the probability of the $M$ holdout samples $\{\delta_s^{(i)}\}_{i=1}^{M}$. On the other hand, the reachable set $\hat{R}(\theta)$ is calculated as a function of the $N$ training samples $\{\delta^{(i)}\}_{i=1}^{N}$. It is also possible to obtain a bound which holds over the probability of all $N+M$ data points, which is more comparable to the guarantees provided by scenario optimization. In fact, the same bound from Theorem 1 holds by the tower property:

$$
\mathbf{P}_{(\{\delta^{(i)}\}_{i=1}^{N},\{\delta_s^{(i)}\}_{i=1}^{M})}\{ V(\hat{R}(\theta)) > \overline{\text{Bin}}(\hat{k}, M, \beta) \} \leq \beta.
$$

## IV. Applications

We present numerical examples to demonstrate that the probabilistic bounds that arise from the holdout method are substantially sharper and require fewer samples than existing methods for data-driven reachability. Specifically, we compare the proposed method to the *wait-and-judge* technique presented in [19] to illustrate this improvement. Further, we extend scenario-based reachable sets to reachable tubes, an application now amenable to scenario techniques given our improved computational complexity.

### A. Reachable Sets

We calculate reachable sets, using the sum of radial basis functions, posed as a constrained optimization problem [19]:

$$
\begin{aligned}
& \underset{\mu, \sigma}{\text{minimize}} & & \sum_{i=1}^{m} \sigma_i^2 \\
& \text{subject to} & & \sum_{i=1}^{m} e^{-\frac{1}{2}\frac{(\delta^{(j)} - \mu_i)^2}{\sigma_i^2}} - \gamma \geq 0, \quad j = 1, \dots, N, \\
& & & \sigma \in [0, \infty)^m
\end{aligned} \tag{11}
$$

Observe that (11) corresponds to the program (6), where

$$
g(x, \theta) = \sum_{i=1}^{m} e^{-\frac{1}{2}\frac{(x - \mu_i)^2}{\sigma_i^2}} - \gamma \tag{12}
$$

Further, we let $\mathrm{Vol}(\hat{R}(\theta)) = \sqrt{\sum_{i=1}^{m} \sigma_i^2}$ be a proxy for the volume of $\hat{R}(\theta)$. To solve (11), we first set the initial centers, $\mu_i$, of the RBFs to be close to optimal using a $k$-means

<!-- PDF page 4 -->

clustering algorithm and choose the initial widths, $\sigma_i$, of our RBFs arbitrarily. We then use the SciPy Python library to solve this optimization problem using Sequential Least Squares Programming.

We take $\gamma = 0.25$ as the threshold of our RBF and consider 3000 samples. To apply the holdout method, we partition our data set into a training and test set, $N + M = 3000$, and take $\beta = 10^{-9}$. We compute reachable set estimates and $\epsilon$ a-posteriori for various combinations of $N$ and $M$, as seen in Tables I and II. Additionally, we investigate the difference in volume proxy of our reachable set estimates, to gauge the effect of training set sample complexity. For a comparative baseline, we examine the wait-and-judge technique over $N = 3000$ scenarios. When presenting the runtime of the holdout method, this measure includes the calculation of the reachable set over $N$ training samples, test-set generation of $M$ samples, and a-posteriori bound computation. In contrast, runtimes of the wait-and-judge method account for calculation of the reachable set over $N = 3000$ samples and a-posteriori bound computation using support scenarios.

#### 1) Duffing Oscillator:

The first example is a reachable set estimation problem for the nonlinear, time-varying system with dynamics: $\ddot{x} = -\alpha y + x - x^3 + \gamma \cos(\omega t)$, with states $x, y \in \mathbb{R}$ and parameters $\alpha, \gamma, \omega \in \mathbb{R}$. This system is known as the Duffing oscillator, a nonlinear oscillator which exhibits chaotic behavior for certain values of $\alpha, \gamma$ and $\omega$, for instance $\alpha = 0.05, \gamma = 0.4, \omega = 1.3$. The set of initial states is the interval such that $x(0) \in [0.95, 1.05]$, $y(0) \in [-0.05, 0.05]$, and we take $\mu_{X_0}$ to be the uniform random variable over this interval. The time range is $[t_0, t_1] = [0, 100]$.

TABLE I. Duffing Oscillator: Calculation of $\epsilon$ for the Holdout Method using a Binomial Tail Inversion.

[Table I](s001-dietrich2025data/table-1.csv)

*Conversion note on Table I: the cells are copied as printed. The first header cell, "Holdout Method:", is the row-group label of the nine rows below it, whose first cells are blank in print; the last row, "Wait and Judge:", is the wait-and-judge baseline, for which no testing set size is printed.*

We calculate a reachable set estimate, using two radial basis functions, such that $m = 2$. We apply the holdout method, for combinations of $N$ and $M$, all of which exhibited a runtime of approximately 10-15 sec. When varying the size of the training set, we encounter a significant decrease in volume of our reachable set estimates when the training set has 1000 or less samples. Further, extreme values of $N$, such as $N = 10$ or $N = 2990$, provide similarly poor probability measures. As seen in Fig. 2, it is best to balance the size of $N$ and $M$. We observe that $N = 1500$, $M = 1500$ provides the smallest epsilon, $\epsilon = 0.018$. In contrast, the wait-and-judge approach exhibited a runtime of approximately 22 min and resulted in $\epsilon = 0.035$, with a volume proxy of $\mathrm{Vol}(\hat{R}(\theta)) = 1.55$.

![Figure 2](../assets/s001-dietrich2025data/figure-2.png)

Fig. 2. Duffing Oscillator: $\epsilon$ and $\hat{e}$ for various sizes of the holdout dataset.

#### 2) Quadrotor:

The next example is for a nonlinear model of a quadrotor used as an example in [14], [30], [31]. The dynamics for this system are

$$
\begin{aligned}
\ddot{x} &= u_1 K \sin(\theta), \\
\ddot{h} &= -g + u_1 K \cos(\theta), \\
\ddot{\theta} &= -d_0 \theta - d_1 \dot{\theta} + n_0 u_2
\end{aligned} \tag{13}
$$

where $x$ and $h$ denote the quadrotor’s horizontal position and altitude in meters, respectively, and $\theta$ denotes its angular displacement. The system has 6 states, which we take to be $x, h, \theta$, and their first derivatives. The two system inputs $u_1$ and $u_2$ represent the motor thrust and the desired angle, respectively. The parameter values used (following [31]) are $g = 9.81, K = 0.89/1.4, d_0 = 70, d_1 = 17, n_0 = 55$. The set of initial states is the interval such that

$$
\begin{aligned}
& x(0) \in [-1.7, 1.7], h(0) \in [0.3, 2.0], \theta(0) \in [-\pi/12, \pi/12], \\
& \dot{x}(0) \in [-0.8, 0.8], \dot{h}(0) \in [-1.0, 1.0], \dot{\theta}(0) \in [-\pi/2, \pi/2],
\end{aligned}
$$

the set of inputs is the set of constant functions $u_1(t) = u_1$, $u_2(t) = u_2$ $\forall t \in [t_0, t_1]$, whose values lie in the interval $u_1 \in [-1.5 + g/K, 1.5 + g/K], u_2 \in [-\pi/4, \pi/4]$, and we take $\mu_{X_0}$ and $\mu_D$ to be the uniform random variables defined over these intervals. The time range is $[t_0, t_1] = [0, 5]$.

We calculate a reachable set estimate using three radial basis functions, such that $m = 3$. We apply the holdout method, for combinations of $N$ and $M$, all of which exhibited a runtime of approximately 35-50 sec. When varying training set size, we observed very similar behavior as that depicted in Fig. 2 for the duffing oscillator. Extreme values of $N$ provide poor probability measures and less than 1000 training samples results in decreased volume of the reachable set estimate. In contrast, the wait-and-judge approach exhibited a runtime of approximately 5.5 hrs and resulted in $\epsilon = 0.051$, with a volume proxy of $\mathrm{Vol}(\hat{R}(\theta)) = 27.80$.

**Sample Complexity.** In the section above, we utilize equal size datasets to compare the wait-and-judge and holdout method, highlighting the improved accuracy and computational cost of the holdout method. To demonstrate futher

<!-- PDF page 5 -->

improvements in sample complexity, let us examine the duffing oscillator example with sample size $N + M = 2000$ where $N = 1000$ and $M = 1000$. We apply the holdout method and calculate $\epsilon = 0.0263$, achieving a 1% increase in accuracy with 1000 fewer samples when compared to the wait-and-judge approach on 3000 samples.

TABLE II. Quadrotor: Calculation of $\epsilon$ for the Holdout Method using a Binomial Tail Inversion.

[Table II](s001-dietrich2025data/table-2.csv)

*Conversion note on Table II: the cells are copied as printed. The first header cell, "Holdout Method:", is the row-group label of the nine rows below it, whose first cells are blank in print; the last row, "Wait and Judge:", is the wait-and-judge baseline, for which no testing set size is printed.*

### B. Reachable Tubes

We define a forward estimated reachable tube as $\hat{\mathcal{R}}(t) = \{\Phi(t_i; t_0, x_0, d) : \forall t_i \in [t_0, t], x_0 \in X_0, d \in D\}$ where $[t_0, t]$ is a finite time interval, $X_0 \subseteq \mathbb{R}^{n_x}$ is the set of initial states, $D$ is the set of disturbance signals $d : [t_0, t] \rightarrow \mathbb{R}^{n_d}$, and $\Phi : \mathbb{R} \times X_0 \times D \rightarrow \mathbb{R}^{n_x}$ is the state transition function. $\hat{\mathcal{R}}(t)$ is the set of all states to which the system can transition within a duration of time $[t_0, t]$ for finite time steps $t_i$ from $X_0$ subject to disturbances in $D$. The reachable tube accounts for all time steps in interval $[t_0, t]$, while the reachable sets presented in Section II only consider one specific time instant. We generalize the nonconvex scenario reachability method presented above and pose the problem of finding a reachable tube directly from data as a chance-constrained optimization problem with regularization over time. In particular, we propose an approach in which we construct a smoothed, finite set of time-varying RBFs:

$$
\begin{aligned}
& \underset{\mu, \sigma}{\text{minimize}} & & \sum_{\tau=0}^{t} \sum_{i=1}^{m} \sigma_i(\tau)^2 + \lambda \| \sigma_{avg} - \sigma_i(\tau) \|^2 \\
& \text{subject to} & & \sum_{\tau=0}^{t} \sum_{i=1}^{m} e^{-\frac{1}{2}\frac{(\delta^{(j)}(\tau) - \mu_i(\tau))^2}{\sigma_i(\tau)^2}} - \gamma \geq 0, j = 1, \dots, N, \\
& & & \sigma(\tau) \in [0, \infty)^m.
\end{aligned}
$$

where $\mu$ is the center of an RBF, $\sigma$ is the width of an RBF, $\lambda$ and $\gamma$ are user-specified parameters, $\delta$ is a scenario, and $\sigma_{avg}$ is the average width over all $\sigma_i$.

To illustrate scenario-based reachable tubes, we investigate a simple linear system: $\dot{x} = Ax$ with

$$
A = \begin{bmatrix}
-0.7 & -1.0 \\
1.0 & -0.7
\end{bmatrix}. \tag{14}
$$

The set of initial states is the interval such that $x_1(0), x_2(0) \in [1, 1.25]$, and we take $\mu_{X_0}$ to be the uniform random variable over this interval. The time range is $[t_0, t] = [0, 10]$. We calculate the reachable tube estimate using one radial basis function for every time instant. To apply the holdout method, we partition our data set of trajectories into a training and test set, as was done in the previous section, and take $\beta = 10^{-9}$. We consider a boundary violation to be any trajectory that falls outside the reachable tube at any time instant. We present one example, as can be seen in Fig. 3, given $N = 1500$ and $M = 1500$. We observed 138 boundary violations, resulting in $\epsilon = 0.144$ and a runtime of 4.92 min. Note that by adjusting $\lambda$, we could influence the widths of our RBFs, e.g. increase the size, thereby decreasing the number of violations at later time instances. Further, we do not provide comparisons with the wait-and-judge approach due to its computational cost, as it requires recalculation of the reachable tube upon removal of every individual trajectory.

![Figure 3](../assets/s001-dietrich2025data/figure-3.png)

Fig. 3. Reachable tube of linear system: The progression of time can be seen as the color of the reachable sets gets darker. The small blue dots indicate the 138 boundary violations that arose from the holdout method.

## V. De-randomization

In this work, we have advocated for the use of a general purpose, practical, and sharp method for data-driven reachability: the holdout method. Data-driven reachability offers probabilistic guarantees that are comprised of two “layers” of probability (cf. Theorem 1): the bound on the violation probability, and the bound in probability, with respect to the probability law of the sample generation (in other words, the confidence that the samples have yielded enough information to construct a reachable set estimate for which the violation probability holds). These types of Probably Approximately Correct (PAC) bounds [32] are ubiquitous in statistical learning theory and data-driven approaches to probabilistic verification. They are generally recognized as the strongest type of guarantee that can be made while placing minimal assumptions on the random variable verified. Nevertheless, it is reasonable to critize two layers of probability on the grounds of interpretability and soundness, compared to conventional control-theoretic guarantees, which provide 100% certainty given accurate modeling information. To that end, several works have made attempts to “de-randomize” data-driven

<!-- PDF page 6 -->

methods, augmenting them with additional information to remove one, or both, of the probabilistic layers [33]–[35].

In this section we argue that, while de-randomization aligns with control theory’s pursuit of certainty, it is not practical for the type of data-driven method explored in this paper and similar approaches. Data-driven verification has two primary advantages: mild requirements on side information, often requiring none at all, and computational efficiency compared to deterministic, sampling-based methods. We have found that de-randomized data-driven methods often relinquish both advantages.

### A. De-randomization Methods

The removal of either layer of probability (or both) is carried out by selecting, according to some side information, a suitable enlargement of the data-driven estimator. For simplicity, we first focus on de-randomizing the inner probability layer, and return to the outer layer later. Specifically, suppose we have found a feasible point $\theta^{\ast}$ satisfying the chance constraint $\mathbf{P}\{ g(\theta^{\ast}, x) \le 0 \} \ge 1 - \epsilon$. To de-randomize such a bound is to establish some $\gamma \ge 0$, as a function of information not available to the original data-driven algorithm, such that $g(\theta^{\ast}, x) \le \gamma$ holds almost surely.

A general scheme for how to perform a de-randomization of this type is laid out in [34]. The central idea of the scheme is computing a uniform level-set bound function $h(\epsilon)$ that acts as a uniform upper bound (over $\theta$) on the quantile function of the random variable $(\sup_x g(x, \theta) - g(x, \theta))$. As a consequence, it follows that if $\mathbf{P}\{ g(\theta^{\ast}, x) \le 0 \} \ge 1 - \epsilon$, then $\mathbf{P}\{ g(\theta^{\ast}, x) \le h(\epsilon) \} = 1$. In our case, the function $g$ contains information about the dynamical system specified in the reachability problem, so de-randomization requires some amount of new side information.

A standard assumption is to presume knowledge of a global Lipschitz bound on the dynamics and to take the estimator sets to be $p$-norm balls, or ellipsoids. In this case, the magnitude of the enlargement factor from existing work scales exponentially with state dimension [34, cf. Remark 3.9], [33, cf. Theorem 1]. Interestingly, a less conservative estimate of the reachable set with the same number of queries—and moreover with a non-stochastic guarantee—is possible with a “sample and cover” approach. This approach spreads query points uniformly over the initial set and uses a contraction-based approximation to completely cover a region around each query point. Given this context, it is natural to wonder if the situation can be improved with a sharper analysis, or if there is a fundamental limitation with this type of de-randomization in general.

### B. Lower Bounds from Zeroth-Order Optimization

The exponential scaling mentioned previously is inherent to all de-randomization approaches — ensuring zero violation probability using only samples and a Lipschitz condition. To demonstrate this, suppose we are given an $h : B_2^d \mapsto \mathbb{R}$, where $B_2^d(r) := \{ x \in \mathbb{R}^d \mid \|x\|_2 \leq r\}$ and $B_2^d := B_2^d(1)$, and we are assured that (a) $h$ is $L$-Lipschitz and (b) the following probabilistic guarantee holds:

$$
\mathbf{P}_{x \sim \mu(B_2^d)}\{ h(x) > 0 \} \leq \varepsilon, \quad \mu(B_2^d) := \mathrm{Unif}(B_2^d).
$$

**Lemma 1.** There exists an $h : B_2^d \mapsto \mathbb{R}$ satisfying conditions (a) and (b) above, such that $\max_{x \in B_2^d} h(x) = L \varepsilon^{1/d}$.

**Proof.** The construction is reminiscent of the Lipschitz bump construction used to prove lower bounds for zeroth-order optimization [36, cf. Theorem 1.1.2]. Consider a family of functions $h_\delta(x) := \delta - L \| x \|_2$ for $\delta > 0$. We now tune $\delta$ so that we ensure $\mathbf{P}_{x \sim \mu(B_2^d)}\{ h_\delta(x) > 0 \} = \varepsilon$. Observing that

$$
\{ x \mid h_\delta(x) > 0 \} = \{ x \mid \delta/L > \| x \|_2 \} =_{\mathrm{a.e.}} \{ x \mid x \in B_2^d(\delta/L) \},
$$

and using $\mathrm{Vol}(B_2^d(r)) = r^d \mathrm{Vol}(B_2^d(1))$, we have

$$
\begin{aligned}
\mathbf{P}_{x \sim \mu(B_2^d)}\{ h_\delta(x) > 0 \} &= \mathbf{P}_{x \sim \mu(B_2^d)}\{ x \in B_2^d(\delta/L) \} \\
&= \frac{\mathrm{Vol}(B_2^d(\delta/L))}{\mathrm{Vol}(B_2^d(1))} = (\delta/L)^d.
\end{aligned}
$$

Setting $(\delta/L)^d = \varepsilon$ yields $\delta = \delta_\star := L \varepsilon^{1/d}$, and hence $\max_{x \in B_2^d} h_{\delta_\star}(x) = h_{\delta_\star}(0) = L \varepsilon^{1/d}$. $\blacksquare$

The implication of Lemma 1 is as follows. Suppose that the $\varepsilon$ from Lemma 1 decreases at a rate of $1/M$, where $M$ is the number of holdout examples, one needs at least $(L/\gamma)^d$ samples to ensure a bound $\max_{x \in B_2^d} h(x) \leq \gamma$ in this setting.

Furthermore, from the simple “sample and cover” procedure described in Section V-A, we see that the same conditions on side information that yield a one-level de-randomization also suffices to de-randomize *both* levels. The basic approach is to remove the possibility of an uninformative sample by selecting the query points non-stochastically, and setting the enlargement factor according to the given Lipschitz bound and the largest distance between any of the query points. This is equivalent to the well-studied problem of *zeroth-order optimization*, for which well-known lower bounds [36, e.g., Theorem 1.1.2] state that $(L/\gamma)^d$ queries are needed for any algorithm to obtain the desired $\gamma$-sub-optimality guarantee.$^{1}$ Note that this bound precisely matches the minimum sample complexity prescribed by Lemma 1.

Footnote 1: Nesterov’s bound in the original form holds for $\ell_\infty$-Lipschitz (i.e. $| h(x) - h(y) | \leq L \| x - y \|_\infty$) instead of $\ell_2$-Lipschitz (i.e., $| h(x) - h(y) | \leq L \| x - y \|_2$), but the proof can be modified for any $\ell_p$-Lipschitz assumption.

The foregoing demonstrations yield three key takeaways: (a) De-randomization under standard Lipschitz assumptions necessarily calls for an amount of data that scales *exponentially* with respect to the dimension of the state. (b) The degree of side information required to de-randomize a bound (e.g., Lipschitz constants) is often rich enough to obtain conventional, non-stochastic reachable set over-approximations. (c) There is little room for a “middle ground” in de-randomization: the query complexity and side information required to remove one level of probability is essentially the same as required to remove both.

In contrast, data-driven methods that yield PAC bounds require almost no side information and are quite sample efficient, as demonstrated in this work. Since the costs incurred

<!-- PDF page 7 -->

by de-randomization are large relative to this baseline, we argue that whenever a sampling-based approach is deemed acceptable, the circumstances where de-randomization is worth the price are rare.

## VI. Conclusion

In this paper, we demonstrate that the holdout method can significantly decrease the sample complexity in finding probabilistically tight reachable sets; this method is highly efficient when collecting scenarios is computationally cheap. Furthermore, we complement our work with a discussion on the necessity of probabilistic reachability bounds within the context of data-driven analysis.

## VII. Acknowledgments

This paper is supported in part by the NSF project CNS-2111688. The first author was also supported by an NSF Graduate Research Fellowship.

## References

[1] M. Althoff, “Reachability analysis and its application to the safety assessment of autonomous cars,” Ph.D. dissertation, Technische Universität München, 2010.

[2] S. Prajna and A. Jadbabaie, “Safety verification of hybrid systems using barrier certificates,” in *Hybrid Systems: Computation and Control*. Berlin, Heidelberg: Springer Berlin Heidelberg, 2004, pp. 477–492.

[3] M. Chen and C. J. Tomlin, “Hamilton–Jacobi reachability: Some recent theoretical advances and applications in unmanned airspace management,” *Annual Review of Control, Robotics, and Autonomous Systems*, vol. 1, no. 1, pp. 333–358, 2018.

[4] M. Althoff, G. Frehse, and A. Girard, “Set propagation techniques for reachability analysis,” *Annual Review of Control, Robotics, and Autonomous Systems*, vol. 4, no. 1, pp. 369–395, 2021.

[5] A. Girard, “Reachability of uncertain linear systems using zonotopes,” in *Hybrid Systems: Computation and Control*. Berlin, Heidelberg: Springer Berlin Heidelberg, 2005, pp. 291–305.

[6] A. Devonport and M. Arcak, “Estimating reachable sets with scenario optimization,” in *Proceedings of the 2nd Conference on Learning for Dynamics and Control*, ser. Proceedings of Machine Learning Research, vol. 120. PMLR, 10–11 Jun 2020, pp. 75–84.

[7] ——, “Data-driven reachable set computation using adaptive gaussian process classification and monte carlo methods,” in *2020 American Control Conference (ACC)*, 2020, pp. 2629–2634.

[8] H. Sartipizadeh, A. P. Vinod, B. Açikmeşe, and M. Oishi, “Voronoi partition-based scenario reduction for fast sampling-based stochastic reachability computation of linear systems,” in *2019 American Control Conference (ACC)*, 2019, pp. 37–44.

[9] A. Devonport, F. Yang, L. E. Ghaoui, and M. Arcak, “Data-driven reachability and support estimation with Christoffel functions,” *IEEE Transactions on Automatic Control*, vol. 68, no. 9, pp. 5216–5229, 2023.

[10] T. Lew and M. Pavone, “Sampling-based reachability analysis: A random set theory approach with adversarial sampling,” *ArXiv*, 2020.

[11] P. Griffioen and M. Arcak, “Data-driven reachability analysis for Gaussian process state space models,” in *2023 62nd IEEE Conference on Decision and Control (CDC)*, 2023, pp. 4100–4105.

[12] A. Alanwar, A. Koch, F. Allgöwer, and K. H. Johansson, “Data-driven reachability analysis from noisy data,” *IEEE Transactions on Automatic Control*, vol. 68, no. 5, pp. 3054–3069, 2023.

[13] D. Sun and S. Mitra, “Neureach: Learning reachability functions from simulations,” in *Tools and Algorithms for the Construction and Analysis of Systems*, 2022, pp. 322–337.

[14] A. Devonport, F. Yang, L. El Ghaoui, and M. Arcak, “Data-driven reachability analysis with Christoffel functions,” in *2021 60th IEEE Conference on Decision and Control (CDC)*. IEEE Press, 2021, p. 5067–5072.

[15] M. Stone, “Cross-validatory choice and assessment of statistical predictions,” *Journal of the Royal Statistical Society. Series B (Methodological)*, vol. 36, no. 2, pp. 111–147, 1974.

[16] R. Kohavi, “A study of cross-validation and bootstrap for accuracy estimation and model selection,” in *Proceedings of the 14th International Joint Conference on Artificial Intelligence (IJCAI)*, 1995, pp. 1137–1143.

[17] T. Hastie, R. Tibshirani, and J. Friedman, *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*, 2nd ed., ser. Springer Series in Statistics. Springer, 2009.

[18] R. Tempo, G. Calafiore, and F. Dabbene, *Randomized Algorithms for Analysis and Control of Uncertain Systems: With Applications*, 2nd ed. Springer Publishing Company, Incorporated, 2012.

[19] E. Dietrich, A. Devonport, and M. Arcak, “Nonconvex scenario optimization for data-driven reachability,” in *Proceedings of the 6th Annual Learning for Dynamics & Control Conference*, ser. Proceedings of Machine Learning Research, vol. 242. PMLR, 15–17 Jul 2024, pp. 514–527.

[20] A. Lin and S. Bansal, “Verification of neural reachable tubes via scenario optimization and conformal prediction,” in *Proceedings of the 6th Annual Learning for Dynamics & Control Conference*, ser. Proceedings of Machine Learning Research, vol. 242. PMLR, 15–17 Jul 2024, pp. 719–731.

[21] L. Hewing and M. N. Zeilinger, “Scenario-based probabilistic reachable sets for recursively feasible stochastic model predictive control,” *IEEE Control Systems Letters*, vol. 4, no. 2, pp. 450–455, 2020.

[22] N. Hashemi, X. Qin, L. Lindemann, and J. V. Deshmukh, “Data-driven reachability analysis of stochastic dynamical systems with conformal inference,” in *2023 62nd IEEE Conference on Decision and Control (CDC)*, 2023, pp. 3102–3109.

[23] A. Tebjou, G. Frehse, and F. Chamroukhi, “Data-driven reachability using Christoffel functions and conformal prediction,” in *Proceedings of the Twelfth Symposium on Conformal and Probabilistic Prediction with Applications*, vol. 204. PMLR, Sep 2023, pp. 194–213.

[24] A. Muthali, H. Shen, S. Deglurkar, M. H. Lim, R. Roelofs, A. Faust, and C. Tomlin, “Multi-agent reachability calibration with conformal prediction,” in *2023 62nd IEEE Conference on Decision and Control (CDC)*, 2023, pp. 6596–6603.

[25] A. K. Akametalu, J. F. Fisac, J. H. Gillula, S. Kaynama, M. N. Zeilinger, and C. J. Tomlin, “Reachability-based safe learning with Gaussian processes,” in *53rd IEEE Conference on Decision and Control*, 2014, pp. 1424–1431.

[26] R. S. Dembo, “Scenario optimization,” *Annals of Operations Research*, vol. 30, pp. 63–80, 1991.

[27] M. C. Campi, S. Garatti, and F. A. Ramponi, “A general scenario theory for nonconvex optimization and decision making,” *IEEE Transactions on Automatic Control*, vol. 63, no. 12, pp. 4067–4078, 2018.

[28] J. Langford, “Tutorial on practical prediction theory for classification,” *Journal of Machine Learning Research*, vol. 6, pp. 273–306, 2005.

[29] M. Hardt and B. Recht, *Patterns, predictions, and actions: Foundations of machine learning*. Princeton University Press, 2022.

[30] I. M. Mitchell, J. Budzis, and A. Bolyachevets, “Invariant, viability and discriminating kernel under-approximation via zonotope scaling: Poster abstract,” in *Proceedings of the 22nd ACM International Conference on Hybrid Systems: Computation and Control*. HSCC, 2019, p. 268–269.

[31] P. Bouffard, “On-board model predictive control of a quadrotor helicopter: Design, implementation, and experiments,” Master’s thesis, EECS Department, University of California, Berkeley, Dec 2012.

[32] L. G. Valiant, “A theory of the learnable,” *Commun. ACM*, vol. 27, no. 11, p. 1134–1142, Nov. 1984.

[33] A. Lecchini-Visintini, J. Lygeros, and J. M. Maciejowski, “Stochastic optimization on continuous domains with finite-time guarantees by markov chain monte carlo methods,” *IEEE Transactions on Automatic Control*, vol. 55, no. 12, pp. 2858–2863, 2010.

[34] P. M. Esfahani, T. Sutter, and J. Lygeros, “Performance bounds for the scenario approach and an extension to a class of non-convex programs,” *IEEE Transactions on Automatic Control*, vol. 60, no. 1, pp. 46–58, 2014.

[35] N. Boffi, S. Tu, N. Matni, J.-J. Slotine, and V. Sindhwani, “Learning stability certificates from data,” in *Proceedings of the 2020 Conference on Robot Learning*, ser. Proceedings of Machine Learning Research, vol. 155. PMLR, 16–18 Nov 2021, pp. 1341–1350.

[36] Y. Nesterov *et al.*, *Lectures on convex optimization*. Springer, 2018, vol. 137.
