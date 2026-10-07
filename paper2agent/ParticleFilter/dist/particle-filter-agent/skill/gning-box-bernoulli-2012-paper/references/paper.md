# Bernoulli Particle/Box-Particle Filters for Detection and Tracking in the Presence of Triple Measurement Uncertainty

Amadou Gning∗, Branko Ristic§, Lyudmila Mihaylova♯

Footnote ∗: School of Computing & Communications, Lancaster University, InfoLab21, Lancaster, United Kingdom, email: e.gning@lancaster.ac.uk

Footnote §: Defence Science and Technology Organization, ISR Division, Bld 94, M2.30, 506 Lorimer Street, Fishermans Bend, VIC 3207, Australia; Tel: (+61 3) 9626 8226; Fax: +61 3 9626 8341; email: branko.ristic@dsto.defence.gov.au

Footnote ∗: School of Computing & Communications, Lancaster University, InfoLab21, Lancaster, United Kingdom, email: mila.mihaylova@lancaster.ac.uk

**Abstract**—This work presents sequential Bayesian detection and estimation methods for nonlinear dynamic stochastic systems using measurements affected by three sources of uncertainty: stochastic, set-theoretic and data association uncertainty. Following Mahler’s framework for information fusion, the paper develops the optimal Bayes filter for this problem in the form of the Bernoulli filter for interval measurements. Two numerical implementations of the optimal filter are developed. The first is the Bernoulli particle filter (PF), which turns out to require a large number of particles in order to achieve a satisfactory performance. For the sake of reduction in the number of particles, the paper also develops an implementation based on box particles, referred to as the Bernoulli Box-PF. A box particle is a random sample that occupies a small and controllable rectangular region of non-zero volume in the target state space. Manipulation of boxes utilizes the methods of interval analysis. The two implementations are compared numerically and found to perform remarkably well: the target is reliably detected and the posterior probability density function of the target state is estimated accurately. The Bernoulli Box-PF, however, when designed carefully, is computationally more efficient.

**Index Terms**—Sequential Bayesian Estimation, Random Sets, Bernoulli Filter, Particle Filters, Box Particle Filters, Interval Measurements.

Submitted to IEEE Trans. Signal Processing December 28, 2011

## I. INTRODUCTION

The problem of study is sequential Bayesian detection and estimation of dynamic stochastic systems using measurements affected by three sources of uncertainty: stochastic, set-theoretic and data association uncertainty. The standard measurements used for nonlinear filtering are points, in the measurement space, affected by additive measurement noise of a known probability density function (pdf) [1]. The traditional measurement noise expresses uncertainty due to randomness, often referred to as statistical or stochastic uncertainty. In many practical applications, however, this standard measurement model is not adequate. In wireless sensor networks, for example, the measurements are quantized to only a few bits in order to reduce the communication bandwidth. Such measurements, although reported as point values, in fact represent intervals. Similarly, complex distributed surveillance systems are often operating under unknown synchronization biases and/or unknown system delays. The resulting measurements are affected by bounded errors of typically unknown distributions and biases, and can be also expressed by intervals. An interval measurement expresses a type of uncertainty which is referred to as the set-theoretic uncertainty [2], [3] or imprecision [4] due to partial knowledge or ignorance. The importance and distinctness of this type of uncertainty have been well recognized in the field of expert systems [5], and to some degree in statistics [6]. The two types of uncertainties, the set-theoretic and stochastic, can be treated in combination using various modern estimation formalisms, such as: the set of densities [7], the robust Bayesian inference and imprecise probabilities [8], [9], random sets [10]. In this paper we adopt the random set formalism for the combined treatment of imprecision and randomness.

Often, in practice, the third source of uncertainty in the measurements is also present. Due to the imperfections of the detection process, sensors typically operate with probability of detection less than one and, in addition, report measurements which are false [11]. This translates into *data association* uncertainty, that is the uncertainty as to which (if any) of the received measurements is due to the target.

Following Mahler’s framework for information fusion [10], the theoretically optimal Bayes filter for the described problem of joint detection and tracking using measurements affected by stochastic, set-theoretic and association uncertainty, is the Bernoulli filter for unambiguously generated ambiguous (UGA) measurements. Interval measurements are a special case of UGA measurements, while the most general instance of an UGA measurement is a mixture of fuzzy membership functions [10, Ch.5]. The aforementioned Bernoulli filter has no analytic solution and therefore needs to be implemented numerically.

Particle filter (PF) methods [12], [13] have recently emerged as a powerful tool for solving numerically complex dynamic estimation problems involving high nonlinearities. The PF approaches approximate the posterior state pdf by a set of random samples. The efficiency and accuracy of PFs depend significantly on the number of particles and on the proposal functions used for the importance sampling. A high level of uncertainty in the available measurements, as considered in this paper, may require a large number of particles, resulting in high computational complexity which induces real-time implementation issues. In an attempt to overcome these issues, it is of interest to consider an implementation based on *box particles*. A box particle occupies a small and controllable rectangular region of non-zero volume in the target state space. A box-particle filter (Box-PF) has a potential to significantly reduce the number of required particles, without a loss in the error performance. The concept of the Box-PF was first proposed in [14], using the interval analysis framework to propagate weighted boxes in a sequential way. Subsequently, the Box-PF was studied and explained through the Bayesian perspective in [15] by interpreting each box particle as a uniform pdf.

In this paper, we develop and compare the performance of two numerical implementations of the Bernoulli filter for detection and tracking using measurements affected by triple uncertainty: the particle filter and the box-particle filter based implementations. The comparison is carried out using statistical criteria for measuring the *inclusion* of the true state and the *volume* of the posterior pdf. The paper shows that both filters perform comparably well when a sufficient number of particles is used: the presence of a target is reliably detected, while the true target state is contained in the support of the spatial density function. The Bernoulli Box-PF, however, appears to be more cost efficient. Preliminary results of this research have been reported in [16] and [17].

The rest of the paper is organized as follows. The formal description of the problem is given in Sec. II. The Bernoulli filter for measurements affected by stochastic, set-theoretic and association uncertainty is formulated in Sec. III. The Bernoulli PF implementation and the Bernoulli Box-PF implementation are presented in Secs. IV and V, respectively. The filter performance assessment criteria are described in Sec. VI, with numerical studies presented in Sec. VII. Finally, the conclusions are drawn in Sec. VIII.

## II. PROBLEM FORMULATION

The state vector of the dynamic system (target) at time $t_k$ (discrete-time index $k$) is denoted by $\mathbf{x}_k$. It takes values from the state space $\mathcal{X} \subseteq \mathbb{R}^{n_x}$. The target, however, may or may not be present in the surveillance region at a particular time $t_k$. We therefore model the object state at discrete-time $k$ by a random finite set (RFS) $\mathbf{X}_k$ which can be either empty or a singleton. Mahler’s *finite set statistics* (FISST) provides practical tools for statistical description and mathematical manipulations of finite-set random variables, including the notion of FISST pdf and its integral [10].

A convenient model of target state at time $k$ is the Bernoulli RFS on $\mathcal{X}$. A Bernoulli RFS has a probability $q$ of being a singleton whose only element is distributed according to the pdf $s(\mathbf{x})$ defined on $\mathcal{X}$ and a probability $1 - q$ of being empty. The FISST probability density of a Bernoulli RFS $\mathbf{X}$ is defined as $$
f(\mathbf{X}) = \begin{cases} 1 - q, & \text{if } \mathbf{X} = \emptyset, \\ q \cdot s(\mathbf{x}), & \text{if } \mathbf{X} = \{\mathbf{x}\}, \\ 0, & \text{otherwise.} \end{cases} \tag{1}
$$ The objective of Bayes filtering is to sequentially estimate $\mathbf{X}_k$ from measurements collected up to time $k$. Assume that the measurement set at time $k$ is denoted by $\boldsymbol{\Upsilon}_k$. Then formally the goal is to estimate sequentially the posterior state pdf $f_{k|k}(\mathbf{X}|\boldsymbol{\Upsilon}_{1:k})$ of a Bernoulli random finite process, where $\boldsymbol{\Upsilon}_{1:k} = (\boldsymbol{\Upsilon}_1, \ldots, \boldsymbol{\Upsilon}_k)$ denotes the sequence of measurement sets up to time $k$. The estimation is based on prior knowledge of two models, the *target dynamic model* and the *measurement model*.

### A. Target Dynamic Model

Target dynamic model is defined by the probability density $\Phi_{k+1|k}(\mathbf{X}|\mathbf{X}')$ associated with target transition from state $\mathbf{X}'$ at time $k$ to $\mathbf{X}$ at time $k+1$. Since both $\mathbf{X}'$ and $\mathbf{X}$ are Bernoulli RFSs, $\Phi_{k+1|k}(\mathbf{X}|\mathbf{X}')$ can be defined as: $$
\Phi_{k+1|k}(\mathbf{X}|\mathbf{X}') = \begin{cases} 1 - p_B, & \text{if } \mathbf{X}' = \emptyset, \mathbf{X} = \emptyset, \\ p_B \cdot b_{k+1|k}(\mathbf{x}), & \text{if } \mathbf{X}' = \emptyset, \mathbf{X} = \{\mathbf{x}\}, \\ 1 - p_S(\mathbf{x}'), & \text{if } \mathbf{X}' = \{\mathbf{x}'\}, \mathbf{X} = \emptyset, \\ p_S(\mathbf{x}') \cdot \pi_{k+1|k}(\mathbf{x}|\mathbf{x}'), & \text{if } \mathbf{X}' = \{\mathbf{x}'\}, \mathbf{X} = \{\mathbf{x}\}, \end{cases} \tag{2}
$$ where

- $p_B \overset{\text{abbr}}{=} p_{B,k+1|k}$ is the probability of target *birth* during the time interval from $k$ to $k + 1$;
- $b_{k+1|k}(\mathbf{x})$ is the spatial distribution of target birth during the time interval from $k$ to $k + 1$;
- $p_S(\mathbf{x}') \overset{\text{abbr}}{=} p_{S,k+1|k}(\mathbf{x}')$ is the probability that a target with state $\mathbf{x}'$ at time $k$ will survive until time $k + 1$;
- $\pi_{k+1|k}(\mathbf{x}|\mathbf{x}')$ is the target transition density from time $k$ to $k + 1$.

### B. Measurement Model

In general, target detection is imperfect. A target may not be detected at scan $k$, whereas a set of non-existent objects may be detected and reported (false detections or clutter). Let the measurement space be denoted as $\mathcal{Z} \subseteq \mathbb{R}^{n_z}$. If the target exists, *i.e.* $\mathbf{X}_k = \{\mathbf{x}\}$, and has been detected, the conventional point measurement $\mathbf{z} \in \mathcal{Z}$ is related to the target state *via* a nonlinear equation: $$
\mathbf{z} = h_k(\mathbf{x}) + \mathbf{v}, \tag{3}
$$ where the function $h_k$ is a known deterministic mapping from the state space $\mathcal{X}$ to the measurement space $\mathcal{Z}$, while $\mathbf{v}$ is a measurement noise vector characterized by a pdf $p_{\mathbf{v}}$.

In this paper, we assume that if a target exists and is detected, the sensor does not report the conventional measurement $\mathbf{z} \in \mathcal{Z}$. Instead, it reports a closed interval $[\mathbf{z}] \subset \mathcal{Z}$ which contains the target originated point measurement (3) with some probability. The set of all such closed intervals on $\mathcal{Z}$, denoted by $\mathcal{IZ}$, is the interval measurement space.

Due to the imperfect detection process, $m_k \geq 0$ interval measurements $[\mathbf{z}]_{k,1}, \ldots, [\mathbf{z}]_{k,m_k}$ are collected at time $k$. The measurements can be represented by a finite set: $$
\boldsymbol{\Upsilon}_k = \{[\mathbf{z}]_{k,1}, \ldots, [\mathbf{z}]_{k,m_k}\} \in \mathcal{F}(\mathcal{IZ}), \tag{4}
$$ where $\mathcal{F}(\mathcal{IZ})$ is the space of finite subsets of $\mathcal{IZ}$.

The probability of target detection is assumed to be constant over the state space $\mathcal{X}$, and is denoted by $p_D$. The false detections are also assumed to be independent of the target state[^1]. The number of false detections per scan is modelled by a Poisson distribution with mean $\lambda$. The prior probability of false interval detections is modelled by $c([\mathbf{z}])$.

The measurement set $\boldsymbol{\Upsilon}_k$ is characterized by three sources of uncertainty. The additive noise $\mathbf{v}$ in (3) is the source of stochastic uncertainty. Interval (non-point) presentation of measurements is the source of imprecision. Finally, the existence of false detections and a possible absence of target originated detection is the source of data association uncertainty.

## III. BERNOULLI FILTER

The optimal Bayes filter for the problem described above is the Bernoulli filter [10, Sec.14.7], [18] [^2] for interval measurements. Let $f_{k|k}(\mathbf{X}|\boldsymbol{\Upsilon}_{1:k})$ denote the posterior pdf of Bernoulli RFS $\mathbf{X}$ at time $k$. The propagation of this posterior pdf over time is carried out in two steps, the *prediction or time-update step* and *the measurement-update step*. We have seen that $f_{k|k}(\mathbf{X}|\boldsymbol{\Upsilon}_{1:k})$ is completely defined by two posteriors: $q_{k|k} = Pr\{|\mathbf{X}_k| = 1 \mid \boldsymbol{\Upsilon}_{1:k}\}$ is[^3] the posterior probability of target existence, while $s_{k|k}(\mathbf{x}) = p(\mathbf{x}_k|\boldsymbol{\Upsilon}_{1:k})$ is the posterior spatial pdf of $\mathbf{X}_k = \{\mathbf{x}\}$. For this reason, the Bernoulli filter propagates only these two quantities.

### A. Equations

Assuming that $p_S$ is state independent, the prediction step equations are given by: $$
q_{k+1|k} = p_B \cdot (1 - q_{k|k}) + p_S \cdot q_{k|k} \tag{5}
$$

$$
s_{k+1|k}(\mathbf{x}) = \frac{p_B \cdot (1 - q_{k|k}) b_{k+1|k}(\mathbf{x})}{q_{k+1|k}} + \frac{p_S\, q_{k|k} \int \pi_{k+1|k}(\mathbf{x}|\mathbf{x}') \cdot s_{k|k}(\mathbf{x}')\, d\mathbf{x}'}{q_{k+1|k}}. \tag{6}
$$ The predicted birth density $b_{k+1|k}(\mathbf{x})$ in general is unknown and needs to be adaptively designed using the measurement set $\boldsymbol{\Upsilon}_k$ from the previous scan $k$. This will further be discussed in Sec. IV.

Assuming that $p_D$ is state independent, the update equations of the Bernoulli filter for interval measurements are as follows [10, Sec. 14.7]. The probability of existence is updated using the measurement set $\boldsymbol{\Upsilon}_{k+1}$ as: $$
q_{k+1|k+1} = \frac{1 - \Delta_{k+1}}{1 - \Delta_{k+1} \cdot q_{k+1|k}} \cdot q_{k+1|k}, \tag{7}
$$ where $$
\Delta_{k+1} = p_D \left( 1 - \sum_{[\mathbf{z}] \in \boldsymbol{\Upsilon}_{k+1}} \frac{\int g_{k+1}([\mathbf{z}]|\mathbf{x})\, s_{k+1|k}(\mathbf{x})\, d\mathbf{x}}{\lambda\, c([\mathbf{z}])} \right). \tag{8}
$$ The quantity $\Delta_{k+1}$ can be positive or negative and can be interpreted as $1 - \Lambda_{k+1}$, where $\Lambda_{k+1}$ is the measurement likelihood ratio under the assumptions of target existence and non-existence. Quantity $g_{k+1}([\mathbf{z}]|\mathbf{x})$ in (8) represents the *generalized* likelihood function at time $k + 1$ for a target originated interval measurement. Furthermore $\lambda$ and $c([\mathbf{z}])$ have already been defined as false alarm parameters. The generalized likelihood is further discussed in Sec. III-B.

The target spatial pdf is updated as follows: $$
s_{k+1|k+1}(\mathbf{x}) = \frac{1 - p_D + p_D \sum\limits_{[\mathbf{z}] \in \boldsymbol{\Upsilon}_{k+1}} \frac{g_{k+1}([\mathbf{z}]|\mathbf{x})}{\lambda c([\mathbf{z}])}}{1 - \Delta_{k+1}}\, s_{k+1|k}(\mathbf{x}). \tag{9}
$$ In the special case where the detection process is perfect, i.e. $p_D = 1$ and there are no false detections, the measurement set becomes a singleton $\boldsymbol{\Upsilon}_{k+1} = \{[\mathbf{z}]\}$, containing only the target originated measurement. Then it is easy to verify that $\lambda c([\mathbf{z}])$ terms cancel out in (7) and (9). Furthermore, with $p_B = 0$, $p_S = 1$ and $q_{0|0} = 1$, the Bernoulli filter for interval measurements simplifies to the single-target Bayes filter for interval measurements (its update equation given in [p.159] [10]). For the more general case of $p_D(\mathbf{x})$ and $p_S(\mathbf{x})$, the Bernoulli filter equations can be found in [10, Sec.14.7].

The proposed Bernoulli filter is the optimal Bayes filter for the considered problem. In the general case, however, it has no analytic solution and this paper will develop two numerical implementations.

Footnote 1: The assumptions about state independent $p_D$ and false detections can be easily relaxed, see [10].

Footnote 2: The Bernoulli filter for conventional (point) measurements is referred to as Joint Target Detection and Tracking (JoTT) in [10, Sec. 14.7]. It represents a generalization of the Integrated Probabilistic Data Association filter [19], which was derived under the linear-Gaussian-Poisson assumption.

Footnote 3: $|\mathbf{X}|$ denotes the cardinality of set $\mathbf{X}$.

### B. Generalized Likelihood

The update equations (7) and (9) are different from those in the standard Bernoulli filter in the sense that the standard measurement likelihood function is replaced by the *generalized* likelihood function. If $[\mathbf{z}] \in \boldsymbol{\Upsilon}_k$ and $\mathbf{X}_k = \{\mathbf{x}\}$, the expression of the generalized likelihood defined in [10, Ch.5] and derived in [20], [21] is given by: $$
\begin{aligned}
g_k([\mathbf{z}]|\mathbf{x}) &= Pr\big\{h_k(\mathbf{x}) + \mathbf{v} \in [\mathbf{z}]\big\} \\
&= \int_{[\mathbf{z}]} p_{\mathbf{v}}\big(\mathbf{z} - h_k(\mathbf{x})\big)\, d\mathbf{z}.
\end{aligned} \tag{10}
$$

Let $\mathcal{N}(\mathbf{y}; \boldsymbol{\mu}, \mathbf{P})$ denote a Gaussian pdf with mean $\boldsymbol{\mu}$ and covariance $\mathbf{P}$. Its cumulative distribution function (cdf) is denoted by $\varphi(\mathbf{y}; \boldsymbol{\mu}, \mathbf{P}) = \int_{-\infty}^{\mathbf{y}} \mathcal{N}(\mathbf{u}; \boldsymbol{\mu}, \mathbf{P})\, d\mathbf{u}$. Now suppose that the measurement noise $\mathbf{v}$ is zero mean white Gaussian with covariance matrix $\boldsymbol{\Sigma}$, that is $p_{\mathbf{v}}(\mathbf{v}) = \mathcal{N}(\mathbf{v}; \mathbf{0}, \boldsymbol{\Sigma})$. In addition, let the lower and upper bound of the interval $[\mathbf{z}]$ be denoted by $\underline{\mathbf{z}}$ and $\overline{\mathbf{z}}$, respectively, that is $[\mathbf{z}] = [\underline{\mathbf{z}},\ \overline{\mathbf{z}}]$. Then according to (10) the generalized likelihood can be expressed as: $$
g_k([\mathbf{z}]|\mathbf{x}) = \int_{\underline{z}}^{\overline{z}} \mathcal{N}(\mathbf{z}; h_k(\mathbf{x}), \boldsymbol{\Sigma})\, d\mathbf{z}
$$

$$
= \varphi(\overline{\mathbf{z}}; h_k(\mathbf{x}), \boldsymbol{\Sigma}) - \varphi(\underline{\mathbf{z}}; h_k(\mathbf{x}), \boldsymbol{\Sigma}) \tag{11}
$$

$$
= 1 - \varphi(h_k(\mathbf{x}); \overline{\mathbf{z}}, \boldsymbol{\Sigma}) - (1 - \varphi(h_k(\mathbf{x}); \underline{\mathbf{z}}, \boldsymbol{\Sigma})) \tag{12}
$$

$$
= \varphi(h_k(\mathbf{x}); \underline{\mathbf{z}}, \boldsymbol{\Sigma}) - \varphi(h_k(\mathbf{x}); \overline{\mathbf{z}}, \boldsymbol{\Sigma}). \tag{13}
$$

The step from (11) to (12) is based on the property of the Gaussian cdf: $\varphi(\mathbf{a}; \boldsymbol{\mu}, \mathbf{P}) = 1 - \varphi(\boldsymbol{\mu}; \mathbf{a}, \mathbf{P})$.

Note that the generalized likelihood function is not a pdf and as such does not integrate to 1. A theoretical justification of the generalized likelihood function of an interval measurement from a measure-theoretic point of view is given in [20]; see also [21] and [22].

Fig. 1 illustrates the generalized likelihood (13) for one-dimensional measurement ($n_z = 1$), with $\underline{z} = 45$, $\overline{z} = 60$ and three values of $\Sigma$, that is 4, 1 and 0.0001. When variance $\Sigma \to 0$, the fuzzy membership function (13) approaches the indicator function; hence additive noise $\mathbf{v}$ is the sources of fuzziness in the generalized likelihood. Note that the quantity $c([\mathbf{z}])$, which features in (8), can be interpreted as a generalized likelihood function of false interval detections.

[Figure 1](../assets/figure/figure-1.jpg)

Figure 1. Illustration of the generalized likelihood function (13) for $n_z = 1$: interval measurement $[z] = [45, 60]$ affected by additive zero-mean Gaussian measurement noise with different values of the variance $\Sigma$.

## IV. PARTICLE FILTER IMPLEMENTATION

Particle filters have become a popular class of numerical methods for implementation of Bayes filters [12], [13], both in the context of single and multiple targets [10]. Combining the Bernoulli filter with a particle filter results in a Bernoulli PF that approximates the spatial pdf[^4] $s_{k|k}(\mathbf{x})$ by a set of $N$ weighted random samples or particles $\{w_k^i, \mathbf{x}_k^i\}_{i=1}^N$, where $\mathbf{x}_k^i$ is the $i$-th particle and $w_k^i$ is its corresponding normalized weight, such that $\sum_{i=1}^N w_k^i = 1$. The approximation of $s_{k|k}(\mathbf{x})$ can be written as $$
s_{k|k}(\mathbf{x}) \approx \sum_{i=1}^{N} w_k^i\, \delta_{\mathbf{x}_k^i}(\mathbf{x}), \tag{14}
$$ where $\delta_{\mathbf{a}}(\mathbf{x})$ is the Dirac delta function concentrated at $\mathbf{a}$. For a suitably chosen importance density, the sum in (14) converges to $s_{k|k}(\mathbf{x})$ as $N \to \infty$ [23].

Starting from the posterior Bernoulli density at scan $k$, represented by $q_{k|k}$ and a set of weighted particles $\{w_k^i, \mathbf{x}_k^i\}_{i=1}^N$, a cycle of the Bernoulli PF for interval measurements is summarized in Algorithm 1. The implementation is based on the Sampling Importance Resampling (SIR) PF, meaning that the transitional density $\pi_{k+1|k}(\mathbf{x}|\mathbf{x}')$ acts as the importance density and that resampling is carried out at every cycle [13]. More sophisticated particle filter implementations of the Bernoulli filter (e.g. interacting particle systems [24]) are left for future work. We also point out two key differences between the described implementation and the one presented in [25]: first, the measurements we deal with are intervals; second, we estimate the birth density $b_{k+1|k}(\mathbf{x})$ adaptively using the received measurements (in [25] the birth density is assumed known).

### A. Prediction Step

The implementation of the prediction (or time update) step (6) requires to draw samples from two densities. The predicted birth density $b_{k+1|k}(\mathbf{x})$ is implemented as: $$
b_{k+1|k}(\mathbf{x}) = \int \pi_{k+1|k}(\mathbf{x}|\mathbf{x}')\, b_k(\mathbf{x}')\, d\mathbf{x}', \tag{15}
$$ where $b_k(\mathbf{x})$ is the birth density at the previous time $k$. If the target can appear anywhere in the state space $\mathcal{X}$, an obvious choice for $b_k(\mathbf{x})$ is the uniform density over $\mathcal{X}$. This, however, would be very inefficient as it would require a massive number of particles. Instead we design $b_k(\mathbf{x})$ adaptively, using the measurement set from the previous scan $k$, $\boldsymbol{\Upsilon}_k$, i.e. $$
b_k(\mathbf{x}) \approx \frac{1}{|\boldsymbol{\Upsilon}_k|} \sum_{[\mathbf{z}] \in \boldsymbol{\Upsilon}_k} \beta_k(\mathbf{x}|[\mathbf{z}]). \tag{16}
$$

Each density $\beta_k(\mathbf{x}|[\mathbf{z}])$ in the mixture (16) is constructed to be compatible with the interval measurement $[\mathbf{z}] \in \boldsymbol{\Upsilon}_k$ as

Footnote 4: Strictly speaking particle filters approximate integrals, not densities, [12], [13]. follows. Suppose the target state vector $\mathbf{x}$ consists of directly measured component $\mathbf{p}$ and unmeasured vector component $\mathbf{u}$, that is $\mathbf{x} = [\mathbf{p}^{\intercal}\ \ \mathbf{u}^{\intercal}]^{\intercal}$, where $^{\intercal}$ denotes the matrix transpose. First we draw $n_0$ times from $U_{[\mathbf{z}]}(\mathbf{z})$, where $U_{[\mathbf{a}]}(\mathbf{a})$ denotes the uniform pdf over the box $[\mathbf{a}]$, to obtain a sample $\{\mathbf{z}^j\}_{j=1}^{n_0}$. Then we compute $\mathbf{p}_{b,k}^j = h_k^{-1}(\mathbf{z}^j)$ for $j = 1, \ldots, n_0$. For the unmeasured component we assume that a prior is available. By drawing $n_0$ times from this prior we can form a sample $\{\mathbf{u}_{b,k}^j\}_{j=1}^{n_0}$. Finally $$
\beta_k(\mathbf{x}|[\mathbf{z}]) \approx \frac{1}{n_0} \sum_{j=1}^{n_0} \delta_{\mathbf{x}_{b,k}^j}(\mathbf{x})
$$ where $\mathbf{x}_{b,k}^j = [(\mathbf{p}_{b,k}^j)^{\intercal}\ \ (\mathbf{u}_{b,k}^j)^{\intercal}]^{\intercal}$.

The newborn particles representing $b_k(\mathbf{x})$ of (16) are then formed by the union of newborn particles sets corresponding to individual box-measurements. The total number of particles representing $b_k(\mathbf{x})$ hence is $N_b = m_k \cdot n_0$. Their weights are $w_{b,k}^i = 1/N_b$ for $i = 1, \ldots, N_b$. Newborn particles representing $b_k(\mathbf{x})$ are constructed in the described manner in Step 4 of Algorithm 1.

Weighted particle sets of two types, the “persistent” and the “newborn” particles, approximate the predicted spatial pdf of (6). The summation of the two terms on the right-hand side of (6) is carried out by the union of these two sets of particles (Step 7 in Algorithm 1). The number of predicted particles is then $N' = N + N_b$. Their respective weights are computed according to (6), see Step 6 in Algorithm 1.

### B. Measurement Update Step

The update equations of the Bernoulli PF are implemented by steps 8-13 of Algorithm 1. Using the approximation $s_{k+1|k}(\mathbf{x}) \approx \sum_{i=1}^{N'} w_{k+1|k}^i\, \delta_{\mathbf{x}_{k+1|k}^i}(\mathbf{x})$, factor $\Delta_{k+1}$ from (8) can be written as: $$
\Delta_{k+1} \approx p_D \left( 1 - \sum_{[\mathbf{z}] \in \boldsymbol{\Upsilon}_{k+1}} \frac{\sum\limits_{i=1}^{N'} g_{k+1}([\mathbf{z}]|\mathbf{x}_{k+1|k}^i)\, w_{k+1|k}^i}{\lambda\, c([\mathbf{z}])} \right). \tag{17}
$$ The generalized likelihood function $g_{k+1}([\mathbf{z}]|\mathbf{x}_{k+1|k}^i)$ in (17) is computed according to (10) in the general case and according to (13) if the measurement noise is additive Gaussian. The probability of existence is then updated as in (7), while the weights of the particles are updated following (9) as: $$
\tilde{w}_{k+1}^{i*} = \frac{1 - p_D + p_D \sum\limits_{[\mathbf{z}] \in \boldsymbol{\Upsilon}_{k+1}} \frac{g([\mathbf{z}]|\mathbf{x}_{k+1|k}^i)}{\lambda\, c([\mathbf{z}])}}{1 - \Delta_{k+1}} \cdot w_{k+1|k}^i. \tag{18}
$$

The updated weights are then normalized to obtain $w_{k+1}^{i*} = \tilde{w}_{k+1}^{i*} / \sum_{j=1}^{N'} \tilde{w}_{k+1}^{j*}$. Finally, by resampling $N$ times from $\{w_{k+1}^{i,*}, \mathbf{x}_{k+1|k}^i\}_{i=1}^{N'}$, one obtains a random sample $\{w_{k+1}^i = \frac{1}{N}, \mathbf{x}_{k+1}^i\}_{i=1}^{N}$. In order to prevent sample impoverishment, the resampling step can be followed by regularization [13]. The filter reports the posterior probability of existence $q_{k+1|k+1}$ and the particle approximation of the posterior spatial pdf $s_{k+1|k+1}(\mathbf{x})$. Since the output weights $w_{k+1}^i$ in Step 14 of Algorithm 1 are equal, strictly speaking it is unnecessary to input/output them.

**Remark:** As a consequence of imprecise measurements (which model bounded errors with unknown measurement biases), the conventional point state estimates, such as the expected or the maximum a posteriori estimates, in general are also biased.

[Algorithm 1](../assets/figure/algorithm-1.jpg)

**Algorithm 1** The Bernoulli particle filter for interval measurements

1: **Input**: $q_{k|k}$, $\{w_k^i, \mathbf{x}_k^i\}_{i=1}^{N}$, $\boldsymbol{\Upsilon}_k$, $\boldsymbol{\Upsilon}_{k+1}$;

***Time Update***

2: Compute $q_{k+1|k}$ using (5)

3: Draw *persistent* particles at $k + 1$: $\mathbf{x}_{p,k+1}^i \sim \pi_{k+1|k}(\mathbf{x}|\mathbf{x}_k^i)$ for $i = 1, \ldots, N$

4: Create a weighted set of *newborn* particles $\{w_{b,k}^i, \mathbf{x}_{b,k}^i\}_{i=1}^{N_b}$ at $k$ from birth density $b_k(\mathbf{x})$ defined by (16), with $w_{b,k}^i = 1/N_b$;

5: Draw *newborn* particles at $k + 1$: $\mathbf{x}_{b,k+1}^i \sim \pi_{k+1|k}(\mathbf{x}|\mathbf{x}_{b,k}^i)$ for $i = 1, \ldots, N_b$

6: Compute the weights at $k + 1$:

$$
w_{p,k+1}^i = p_S\, q_{k|k}\, w_k^i / q_{k+1|k}; \quad \text{for } i = 1, \ldots, N
$$

$$
w_{b,k+1}^i = p_B\, (1 - q_{k|k}) w_{b,k}^i / q_{k+1|k}; \quad \text{for } i = 1, \ldots, N_b
$$

7: Union of weighted particles: $\{w_{k+1|k}^i, \mathbf{x}_{k+1|k}^i\}_{i=1}^{N'} = \{w_{b,k+1}^i, \mathbf{x}_{b,k+1}^i\}_{i=1}^{N_b} \cup \{w_{p,k+1}^i, \mathbf{x}_{p,k+1}^i\}_{i=1}^{N}$, where $N' = N + N_b$;

***Measurement Update***

8: For every particle $\mathbf{x}_{k+1|k}^i$, $i = 1, \ldots, N'$ and every measurement $[\mathbf{z}] \in \boldsymbol{\Upsilon}_{k+1}$, compute the generalized likelihood $g([\mathbf{z}]|\mathbf{x}_{k+1}^i)$ according to (10);

9: Compute $\Delta_{k+1}$ according to (17);

10: Compute $q_{k+1|k+1}$ according to (7);

11: Compute unnormalized weights $\tilde{w}_{k+1}^{i*}$ according to (18) for $i = 1, \ldots, N'$;

12: Normalize weights: $w_{k+1}^{i*} = \tilde{w}_{k+1}^{i*} / \sum_{j=1}^{N'} \tilde{w}_{k+1}^{j*}$;

13: Resample $N$ times from $\{w_{k+1}^{i,*}, \mathbf{x}_{k+1|k}^i\}_{i=1}^{N'}$ to obtain equally weighted particles $\{w_{k+1}^i = \frac{1}{N}, \mathbf{x}_{k+1}^i\}_{i=1}^{N}$

14: **Output**: $q_{k+1|k+1}$, $\{w_{k+1}^i, \mathbf{x}_{k+1}^i\}_{i=1}^{N}$

## V. BOX PARTICLE FILTER IMPLEMENTATION

Due to the large uncertainty in the measurements, the posterior pdf could be characterized by an extensive support. Consequently, the number of (point) particles required to cover this significant portion of the state space, can be also very large. One natural solution to reduce the number of particles is to use non-point particles, such as the multidimensional rectangular or box particles [14]. The efficiency of box particles combined with interval analysis tools [26] is demonstrated in [14]. Furthermore, in [15] it has been shown that box particles can be interpreted as being supports of a mixture of uniform pdfs, and in this respect, (14) becomes: $$
s_{k|k}(\mathbf{x}) \approx \sum_{i=1}^{N} w_k^i\, U_{[\mathbf{x}_k^i]}(\mathbf{x}), \tag{19}
$$ where $[\mathbf{x}_k^i]$ is a box-particle.

Starting from the posterior Bernoulli density at scan $k$, represented by $q_{k|k}$ and a set of weighted box particles $\{w_k^i, [\mathbf{x}_k^i]\}_{i=1}^{N}$, a cycle of the Bernoulli Box-PF for interval measurements is summarized in Algorithm 2. Since the algorithm heavily relies on the concepts and tools from interval analysis, a brief overview of interval analysis is given next.

### A. Elements of Interval Analysis

A real interval, $[x] = [\underline{x},\ \overline{x}]$ is defined as a closed and connected subset of the set $\mathbb{R}$ of real numbers. In a vector form, a box $[\mathbf{x}]$ of $\mathbb{R}^{n_x}$ is defined as a Cartesian product of $n_x$ intervals: $[\mathbf{x}] = [x_1] \times [x_2] \cdots \times [x_n] = \times_{i=1}^{n_x} [x_i]$. In this paper, the operator $|[.]|$ denotes the size $|[\mathbf{x}]|$ of a box $[\mathbf{x}]$. The underlying concept of interval analysis is to deal with intervals of real numbers instead of dealing with real numbers. For that purpose, elementary arithmetic operations, e.g., $+, -, *, \div$, etc., as well as operations between sets of $\mathbb{R}^n$, such as $\subset, \supset, \cap, \cup$, etc., have been naturally extended to interval analysis context.

A nonlinear transformation of a box $[\mathbf{x}]$ in general has a non-box shape. In order to remain in the realm of boxes, a lot of research in interval analysis has been devoted to *inclusion functions* [26]. An *inclusion function* $[f]$ of a given (nonlinear) function $f$ is defined such that the image of a box $[\mathbf{x}]$ is a box $[f]{}([\mathbf{x}])$ containing $f([\mathbf{x}])$. The goal of inclusion functions is to work only with intervals, to optimize the interval enclosing the real image set and, then to decrease the pessimism (uncertainty) when intervals are propagated.

Often constraints have to be fulfilled which require to solve the *Constraint Satisfaction Problems* (CSPs). A CSP often denoted $\mathcal{H}$ can be written: $$
\mathcal{H} : (\mathbf{f}(\mathbf{x}) = \mathbf{0}, \mathbf{x} \in [\mathbf{x}]). \tag{20}
$$ Equation (20) can be interpreted as follows: find the optimal box enclosure of the set of vector $\mathbf{x}$ belonging to a given prior domain $[\mathbf{x}] \subset \mathbb{R}^n$ satisfying a set of $m$ constraints $\mathbf{f}$ (with $\mathbf{f}$ a multivalued function, i.e., $\mathbf{f} = (f_1, f_2, \cdots, f_m)^T$, where the $f_i$ are real valued functions). The solution set of $\mathcal{H}$ is defined as: $$
\mathcal{S} = \{\mathbf{x} \in [\mathbf{x}] \mid \mathbf{f}(\mathbf{x}) = \mathbf{0}\}. \tag{21}
$$ *Contracting* $\mathcal{H}$ means replacing $[\mathbf{x}]$ by a smaller domain $[\mathbf{x}]'$ such that $\mathcal{S} \subseteq [\mathbf{x}]' \subseteq [\mathbf{x}]$. A *contractor* for $\mathcal{H}$ is any operator that can be used to contract $\mathcal{H}$. Several methods for building contractors are described in [26, Chapter 4], including Gauss elimination, the Gauss-Seidel algorithm, linear programming, etc. Each of these methods may be more suitable to some types of CSP. Although the approaches presented in this work are not limited to any particular contractor, a general and well known contraction method, the *Constraints Propagation* (CP) technique is used in this paper. The main advantages of the CP method is its efficiency in the presence of high redundancy of data and equations. The CP method is also known to be simple and, most importantly, to be independent of nonlinearities. An example of CP algorithm is presented later in the appendix.

### B. Time Update Step

The implementation of the prediction equation (6) requires to use a box particle approximation for newborn target and persistent target densities. The predicted birth density $b_{k+1|k}(\mathbf{x})$ is implemented as in (15). The birth density $b_k(\mathbf{x})$, which features in (15), is designed adaptively, using the measurement set from the previous scan $k$, $\boldsymbol{\Upsilon}_k$ as in (16). For every $[\mathbf{z}] \in \boldsymbol{\Upsilon}_k$, a density $\beta_k(\mathbf{x}|[\mathbf{z}])$ in (16) is approximated with a mixture of uniform pdfs, compatible with the interval measurement $[\mathbf{z}]$, that is $$
\beta(\mathbf{x}|[\mathbf{z}]) \approx \frac{1}{n_0} \sum_{i=1}^{n_0} U_{[\mathbf{x}_{b,k}^i]}(\mathbf{x}). \tag{22}
$$ Equations (16) and (22) mean that $b_k(.)$ is represented by a set of $N_b = m_k \cdot n_0$ box particles $\{[\mathbf{x}_{b,k}^i]\}_{i=1}^{N_b}$. The box particles approximating density $\beta(\mathbf{x}|[\mathbf{z}])$ are formed in the manner somewhat similar to that explained in Sec. IV-A. For the measured component of the state, we construct the inclusion function $[\mathbf{p}] = [h_k^{-1}]{}([\mathbf{z}])$. For the unmeasured component of the state $\mathbf{u}$ we form the inclusion box which contains the support of its prior, i.e. $[\mathbf{u}] \approx [\text{support}(p_0(\mathbf{u}))]$. Finally, the box $[\mathbf{p}] \times [\mathbf{u}]$ is subdivided into $n_0$ boxes. The weights associated with the newborn box particles are made equal, i.e. $w_{b,k}^i = 1/N_b$ for $i = 1, \ldots, N_b$. Box particles approximating $b_k(\mathbf{x})$ are constructed as described here in Step 4 of Algorithm 2.

It remains to explain how the box particles are propagated from time $k$ to $k + 1$, that is how integrals (15) and $\int \pi_{k+1|k}(\mathbf{x}|\mathbf{x}') \cdot s_{k|k}(\mathbf{x}')\, d\mathbf{x}'$ in (6) are approximated. Suppose the transitional density $\pi_{k+1|k}(\mathbf{x}|\mathbf{x}')$ is known through an evolution model $\mathbf{f}_{k+1}$ (possibly nonlinear) that is $$
\mathbf{x}_{k+1} = \mathbf{f}_{k+1}(\mathbf{x}_k) + \mathbf{w}_k, \tag{23}
$$ Furthermore, if we assume that $\mathbf{w}_k$ is a bounded noise[^5] in a box $[\mathbf{w}_k]$, then according to [15] the following approximations are made:

$$
\int \pi_{k+1|k}(\mathbf{x}|\mathbf{x}')\, b_k(\mathbf{x}')\, d\mathbf{x}' \approx w_{b,k}^i \sum_{i=1}^{N_b} U_{[\mathbf{f}_{k+1}]{}([\mathbf{x}_{b,k}^i]) + [\mathbf{w}_k]}(\mathbf{x}) \tag{24}
$$

$$
\int \pi_{k+1|k}(\mathbf{x}|\mathbf{x}')\, s_{k|k}(\mathbf{x}')\, d\mathbf{x}' \approx w_k^i \sum_{i=1}^{N} U_{[\mathbf{f}_{k+1}]{}([\mathbf{x}_{p,k}^i]) + [\mathbf{w}_k]}(\mathbf{x}) \tag{25}
$$ A key issue here is to note that an image of a box $f_k([\mathbf{x}])$ is not always a box. Therefore we have approximated this arbitrarily-shaped image by the inclusion function (a box) $[f_k]{}([\mathbf{x}])$. This was carried out in Steps 3 and 5 of Algorithm 2.

Footnote 5: Without loss of generality, noise $\mathbf{w}_k$ is restricted to be additive and bounded. In [15], the general case is considered with noise $\mathbf{w}_k$ approximated using a mixture of uniform pdfs.

The weights $\{w_{p,k+1}^i\}_{i=1}^{N}$ and $\{w_{b,k+1}^i\}_{i=1}^{N_b}$ are computed according to (6) in Step 6 of Algorithm 2.

Two sets of predicted weighted box particles, the “persistent” $\{w_{p,k}^i, [\mathbf{x}_{p,k}^i]\}_{i=1}^{N}$ and the “newborn” box particles $\{w_{b,k}^i, [\mathbf{x}_{b,k}^i]\}_{i=1}^{N_b}$, approximate the predicted spatial pdf of (6). The summation of the two terms on the right-hand side of (6) is carried out by the union of these two sets of box particles (Step 7 in Algorithm 2). The number of predicted box particles then is $N' = N + N_b$.

[Algorithm 2](../assets/figure/algorithm-2.jpg)

**Algorithm 2** The Bernoulli box-particle filter for interval measurements

1: **Input**: $q_{k|k}$, $\{w_k^i, [\mathbf{x}_k^i]\}_{i=1}^{N}$, $\boldsymbol{\Upsilon}_k$, $\boldsymbol{\Upsilon}_{k+1}$;

***Time Update***

2: Compute $q_{k+1|k}$ using (5)

3: Propagate *persistent* box particles to $k + 1$: $[\mathbf{x}_{p,k+1}^i] = [\mathbf{f}_{k+1}]{}([\mathbf{x}_k^i]) + [\mathbf{w}_k]$ for $i = 1, \ldots, N$

4: Create a weighted set of *newborn* box particles $\{w_{b,k}^i, [\mathbf{x}_{b,k}^i]\}_{i=1}^{N_b}$ at $k$ from birth density $b_k(\mathbf{x})$ defined by (16) using $\boldsymbol{\Upsilon}_k$, with $w_{b,k}^i = 1/N_b$;

5: Propagate *newborn* box particles to $k + 1$: $[\mathbf{x}_{b,k+1}^i] = [\mathbf{f}_{k+1}]{}([\mathbf{x}_{b,k}^i]) + [\mathbf{w}_k]$ for $i = 1, \ldots, N_b$

6: Compute the box particle prediction weights at $k + 1$:

$$
w_{p,k+1}^i = p_S\, q_{k|k}\, w_k^i / q_{k+1|k}; \quad \text{for } i = 1, \ldots, N
$$

$$
w_{b,k+1}^i = p_B\, (1 - q_{k|k}) w_{b,k}^i / q_{k+1|k}; \quad \text{for } i = 1, \ldots, N_b
$$

7: Union of weighted box particles: $\{w_{k+1|k}^i, [\mathbf{x}_{k+1|k}^i]\}_{i=1}^{N'} = \{w_{b,k+1}^i, [\mathbf{x}_{b,k+1}^i]\}_{i=1}^{N_b} \cup \{w_{p,k+1}^i, [\mathbf{x}_{p,k+1}^i]\}_{i=1}^{N}$, where $N' = N + N_b$;

***Measurement Update***

8: Replicate the box particle $[\mathbf{x}_{k+1|k}^i]$ to obtain $N'$ box particle $[\tilde{\mathbf{x}}_{k+1}^i]$ with weights $\tilde{w}_{k+1}^i = (1 - p_D) w_{k+1|k}^i$

9: For every box particle $[\mathbf{x}_{k+1|k}^i]$, $i = 1, \ldots, N'$ and every measurement $[\mathbf{z}] \in \boldsymbol{\Upsilon}_{k+1}$,

- use a contraction algorithm according to (30) to obtain a new box particle $[\tilde{\mathbf{x}}_{k+1}^i]$;
- compute the weight $\tilde{w}_{k+1}^i$ of $[\tilde{\mathbf{x}}_{k+1}^i]$ according to (32);

10: Compute $\Delta_{k+1}$ according to (8) and (34);

11: Compute $q_{k+1|k+1}$ according to (7);

12: Normalize weights: $\tilde{w}_{k+1}^i = \tilde{w}_{k+1}^i / \sum_{j=1}^{N'(1+m_k)} \tilde{w}_{k+1}^j$;

13: Resample $N$ times from $\{\tilde{w}_{k+1}^i, [\mathbf{x}_{k+1|k}^i]\}_{i=1}^{N'(1+m_k)}$ to obtain $N$ equally weighted box particles $\{w_{k+1}^i = \frac{1}{N}, [\mathbf{x}_{k+1}^i]\}_{i=1}^{N}$

14: **Output**: $q_{k+1|k+1}$, $\{w_{k+1}^i, [\mathbf{x}_{k+1}^i]\}_{i=1}^{N}$

### C. Measurement Update Step

In the update step of the Bernoulli Box-PF, a different expression for the generalized likelihood is used. Assuming that the stochastic uncertainty (due to measurement noise $\mathbf{v}$) is small and can be approximated by a uniform pdf[^6] $$
p_{\mathbf{v}}(\mathbf{v}) \approx U_{[\varepsilon]}(\mathbf{v}), \tag{26}
$$ where $[\varepsilon]$ is the measurement noise support. Substitution of (26) into the definition of the generalized likelihood (10) results in: $$
\begin{aligned}
g_k([\mathbf{z}]|\mathbf{x}) &\approx \int_{[\mathbf{z}]} U_{[\varepsilon]}(\mathbf{z} - h_k(\mathbf{x}))\, d\mathbf{z} = \int_{[\mathbf{z}]} U_{[\varepsilon] + h_k(\mathbf{x})}(\mathbf{z})\, d\mathbf{z} \\
&= \frac{|\, [\mathbf{z}] \cap (h_k(\mathbf{x}) + [\varepsilon])\, |}{|[\varepsilon]|}.
\end{aligned} \tag{27}
$$ Here $|.|$ denotes the Lebesgue measure operator (e.g. the volume for boxes in $\mathbb{R}^{n_z}$). From (27), it follows that $$
g_k([\mathbf{z}]|\mathbf{x}) \approx \begin{cases} 1, & \text{if } (h_k(\mathbf{x}) + [\varepsilon]) \subseteq [\mathbf{z}] \\ 0, & \text{if } (h_k(\mathbf{x}) + [\varepsilon]) \cap [\mathbf{z}] = \emptyset \\ \leq 1, & \text{otherwise} \end{cases}\ . \tag{28}
$$ This expression describes fairly accurately any generalized likelihood function; compare it for example with Fig.1.

The update equations of the Bernoulli Box-PF are implemented by steps 8-13 of Algorithm 2. Using the box particle approximation $s_{k+1|k}(\mathbf{x}) \approx \sum_{i=1}^{N'} w_{k+1|k}^i\, U_{[\mathbf{x}_{k+1|k}^i]}(\mathbf{x})$ and the generalized likelihood (27), the terms $\frac{p_D}{c([\mathbf{z}])} \cdot g_{k+1}([\mathbf{z}]|\mathbf{x}) \cdot s_{k+1|k}(\mathbf{x})$ which feature in (9) can be written as: $$
\begin{aligned}
&\frac{p_D}{c([\mathbf{z}])} \cdot g_{k+1}([\mathbf{z}]|\mathbf{x}) \cdot s_{k+1|k}(\mathbf{x}) = \\
&\frac{p_D}{c([\mathbf{z}])} \cdot \sum_{i=1}^{N'} w_{k+1|k}^i \frac{|\, [\mathbf{z}] \cap (h_{k+1}(\mathbf{x}) + [\varepsilon_{k+1}])\, |}{|[\varepsilon_{k+1}]|} U_{[\mathbf{x}_{k+1|k}^i]}(\mathbf{x}).
\end{aligned} \tag{29}
$$ Similarly to what is theoretically derived in [15] for the case of point measurements, the supports of the terms inside the summation on the right-hand side of (29) can be approximated using contraction operations briefly discussed in Sec. V-A. The exact supports are the set solutions of : $$
\{\mathbf{x} \in [\mathbf{x}_{k+1|k}^i] \,|\, [\mathbf{z}] \cap (h_{k+1}(\mathbf{x}) + [\varepsilon_{k+1}]) \neq \emptyset\}. \tag{30}
$$

Footnote 6: In the general case, $p_{\mathbf{v}}$ can be approximated more precisely by a mixture of uniform pdfs and the generalized likelihood function can be expressed as a weighted sum of generalized likelihoods for each uniform pdf. For simplicity, we consider here one component.

Each term inside the summation on the right-hand side of (29) is approximated by a weighted single uniform pdf $U_{[\tilde{\mathbf{x}}_{k+1}^i]}(\mathbf{x})$ i.e. $$
\frac{p_D}{c([\mathbf{z}])} \cdot g_{k+1}([\mathbf{z}]|\mathbf{x}) \cdot s_{k+1|k}(\mathbf{x}) \simeq \sum_{i=1}^{N'} \tilde{w}_{k+1}^i U_{[\tilde{\mathbf{x}}_{k+1}^i]}(\mathbf{x}), \tag{31}
$$ where $[\tilde{\mathbf{x}}_{k+1}^i]$ is a box enclosure of the support (30) that can be obtained by a contraction algorithm. The new weights $\tilde{w}_{k+1}^i$ are obtained from (29) as follows: $$
\tilde{w}_{k+1}^i = \frac{p_D}{c([\mathbf{z}])} \cdot w_{k+1|k}^i\, \kappa_{k+1}^i\, \frac{|[\tilde{\mathbf{x}}_{k+1}^i]|}{|[\mathbf{x}_{k+1|k}^i]|}, \tag{32}
$$ where $\kappa_{k+1}^i$ is chosen to be the expectation of the generalized likelihood $g_{k+1}([\mathbf{z}]|\mathbf{x})$ over the box particle $[\tilde{\mathbf{x}}_{k+1}^i]$. Factor $\kappa_{k+1}^i$ can be written: $$
\kappa_{k+1}^i = \frac{1}{|[\tilde{\mathbf{x}}_{k+1}^i]|} \int_{[\tilde{\mathbf{x}}_{k+1}^i]} \frac{|[\mathbf{z}] \cap (h_{k+1}(\mathbf{x}) + [\varepsilon_{k+1}])|}{|[\varepsilon_{k+1}]|}\, d\mathbf{x}. \tag{33}
$$ The integral defining (33) is not known in a closed form but can be approximated (for instance by using a partition of the set $[\tilde{\mathbf{x}}_{k+1}^i]$ as it is done in the Riemann integration theory [27]). In practice, we found that a constant value for all the box particles, e.g., $\kappa_{k+1}^i = 1$ is a good approximation and we adopt this value for the rest of the paper.

Bearing in mind eq. (9), the posterior pdf $s_{k+1|k+1}(\mathbf{x})$ is approximated using $m_k + 1$ sets of box particles: one set of $N'$ box particles $[\tilde{\mathbf{x}}_{k+1|k}^i]$ with weights $(1 - p_D) w_{k+1|k}^i$ and $m_k$ sets of $N'$ box particles with weights $\tilde{w}_{k+1|k}^i$ obtained using the $m_k$ measurements according to (31) and (32).

Next, the terms $\int g_{k+1}([\mathbf{z}]|\mathbf{x})\, s_{k+1|k}(\mathbf{x})\, d\mathbf{x}$, which feature in (8), can be written as $$
\begin{aligned}
&\int g_{k+1}([\mathbf{z}]|\mathbf{x})\, s_{k+1|k}(\mathbf{x})\, d\mathbf{x} = \\
&\int \frac{|\, [\mathbf{z}] \cap (h_{k+1}(\mathbf{x}) + [\varepsilon_{k+1}])\, |}{|[\varepsilon_{k+1}]|} \cdot \sum_{i=1}^{N'} w_{k+1|k}^i U_{[\mathbf{x}_{k+1|k}^i]}(\mathbf{x})\, d\mathbf{x} = \\
&\sum_{i=1}^{N'} \frac{w_{k+1|k}^i}{|[\mathbf{x}_{k+1|k}^i]| \cdot |[\varepsilon_{k+1}]|} \int_{[\mathbf{x}_{k+1|k}^i]} |\, [\mathbf{z}] \cap (h_{k+1}(\mathbf{x}) + [\varepsilon_{k+1}])\, |\, d\mathbf{x} \\
&= \sum_{i=1}^{N'} \frac{w_{k+1|k}^i}{|[\varepsilon_{k+1}]|} \frac{|[\tilde{\mathbf{x}}_{k+1}^i]|}{|[\mathbf{x}_{k+1|k}^i]|} \kappa_{k+1}^i.
\end{aligned} \tag{34}
$$ The probability of existence is then updated as in (7). The $N' \times (m_k + 1)$ updated weights are then normalized to obtain $\tilde{w}_{k+1}^i = \tilde{w}_{k+1}^i / \sum_{j=1}^{N'} \tilde{w}_{k+1}^j$.

Finally, we resample $N$ times from $\{\tilde{w}_{k+1}^i, [\tilde{\mathbf{x}}_{k+1|k}^i]\}_{i=1}^{N' \times (m_k+1)}$ to obtain a new set of box particle $\{w_{k+1}^i = \frac{1}{N}, [\mathbf{x}_{k+1}^i]\}_{i=1}^{N}$. As explained in [14], instead of replicating box particles which have been selected more than once in the resampling step, we divide them into smaller box-particles as many times as they were selected. Several strategies of subdivision can be used (e.g. according to the largest box face). In this paper we randomly pick a dimension to be divided for the selected box particle.

The filter reports the posterior probability of existence $q_{k+1|k+1}$ and the box particle approximation of the posterior spatial pdf $s_{k+1|k+1}(\mathbf{x})$. A point estimate from the Bernoulli Box-PF in general is biased. This is typically due to the fact that the correct measurement value $h_k(\mathbf{x})$ is not in the middle of the measurement interval. If required, however, the expected a posteriori estimate can be obtained as the expectation of (19), *i.e.*, $$
\hat{\mathbf{x}}_{k+1|k+1} = \sum_{i=1}^{N} w_{k+1}^i \mathbf{c}_{k+1}^i, \tag{35}
$$ where $\mathbf{c}_{k+1}^i$ is the center of the $i$-th box particle. The covariance of (19) can be similarly derived. Then, for each coordinate $j = 1, \ldots, n_x$ of the state, the variance $\sigma_{k+1}^2(j)$ of the state component $\hat{\mathbf{x}}_{k+1|k+1}(j)$ can be obtained as: $$
\sigma_{k+1}^2(j) = \sum_{i=1}^{N} w_{k+1}^i \left( \mathbf{c}_{k+1}^i(j) - \hat{\mathbf{x}}_{k+1|k+1}(j) \right)^2 + \sum_{i=1}^{N} w_{k+1}^i \frac{|[\mathbf{x}_{k+1}^i]{}(j)|^2}{12}. \tag{36}
$$ The first term on the RHS of (36) represents the spread of the means; the second represents the variance of the mixture of the uniform pdfs (for the $j^{th}$ coordinate of the state).

## VI. PERFORMANCE ASSESSMENT

Since the conventional point state estimates are biased, the standard filter error performance measures, such as the mean-square error, are not appropriate for the described Bayes filters. How then to assess their error performance?

Recall that the optimal filter for the problem described in the paper has to satisfy two conditions:

1) The true value of the target state vector $\mathbf{x}_k$ must be contained in the support of the posterior spatial pdf $s_{k|k}(\mathbf{x})$;

2) The volume of the support of the posterior spatial pdf $s_{k|k}(\mathbf{x})$ is minimal.

Accordingly we propose two assessment criteria: the first is referred to as *inclusion* and verifies condition 1. The second, referred to as *volume*, measures the spread (volume) of $s_{k|k}(\mathbf{x})$. Note that the failure to satisfy condition 1 indicates filter divergence, which is considered as a *catastrophic* event in target tracking. For the proposed Bernoulli PF and Box-PF for interval measurements, which are numerical approximations of the optimal Bernoulli filter, it will be an imperative to satisfy condition 1 and desirable to minimise the volume in condition 2.

In order to define the two criteria, let us introduce a *credible set* [8] $\mathbf{C}_k(\alpha)$ associated with the posterior $s_{k|k}(\mathbf{x}) = p(\mathbf{x}_k|\boldsymbol{\Upsilon}_{1:k})$. This set is defined implicitly as the smallest set $\mathbf{C}_k(\alpha) \subseteq \mathcal{X}$ such that its probability is: $$
P\big(\mathbf{C}_k(\alpha)\big) = \int_{\mathbf{C}_k(\alpha)} s_{k|k}(\mathbf{x})\, d\mathbf{x} = 1 - \alpha, \tag{37}
$$ where $\alpha \ll 1$. A credible set at $\alpha \to 0$ represents the support of the posterior spatial pdf $s_{k|k}(\mathbf{x})$. The *inclusion criterion* $\rho_k$ is defined as: $$
\rho_k = \begin{cases} 1, & \text{if the true state } \mathbf{x}_k \in \mathbf{C}_k(\alpha) \\ 0, & \text{otherwise.} \end{cases} \tag{38}
$$

The *volume* criterion $\nu_k$ measures the volume of the credible set $\mathbf{C}_k(\alpha)$. The two assessment criteria, $\rho_k$ and $\nu_k$, will be computed for all discrete-time indices $k$ characterized by $q_{k|k} > \tau$, where $\tau \in [0, 1]$ is the track reporting threshold. Furthermore, in order to establish the expected performance, $\rho_k$ and $\nu_k$ will be averaged over independent Monte Carlo runs.

### A. Computation of $\rho_k$ and $\nu_k$ for the Bernoulli PF

For the implementation of the inclusion criterion $\rho_k$ in (38), only a random sample approximation of $s_{k|k}(\mathbf{x})$, that is $\{w_k^i = \frac{1}{N}, \mathbf{x}_k^i\}_{i=1}^{N}$, is available. In order to establish the inclusion of the true state vector, i.e. $\mathbf{x}_k \in \mathbf{C}_k(\alpha)$, the kernel density estimation (KDE) method [28] can be applied. The (fixed) KDE method places a kernel function $\phi$ on every particle $\mathbf{x}_k^i$, $i = 1, \dots, N$. The result is an approximation of the posterior density $s_{k|k}(\mathbf{x})$:

$$ s_{k|k}(\mathbf{x}) \approx \tilde{s}(\mathbf{x}) = \frac{1}{N W^{n_x}} \sum_{i=1}^{N} \phi\left(\frac{\mathbf{x} - \mathbf{x}_k^i}{W}\right), \tag{39} $$

where $\phi(\mathbf{x})$ is the kernel which satisfies $\phi(\mathbf{x}) \ge 0$ and $\int_{\mathcal{X}} \phi(\mathbf{x})\, d\mathbf{x} = 1$, and $W$ is the kernel width parameter. For convenience we adopt the Gaussian kernel with zero-mean and covariance matrix $\mathbf{P}$:

$$ \phi(\mathbf{x}) = \frac{1}{(2\pi)^{n_x/2}\sqrt{|\mathbf{P}|}} \exp\left\{ -\frac{1}{2} \mathbf{x}^{\mathsf{T}}\, \mathbf{P}^{-1}\, \mathbf{x} \right\}. \tag{40} $$

The optimal fixed bandwidth (under the assumption that the underlying pdf is Gaussian) for the Gaussian kernel $\phi(\mathbf{x})$ is [28] $W^{*} = A \cdot N^{-\frac{1}{n_x+4}}$, where $A = [4/(n_x + 2)]^{\frac{1}{n_x+4}}$. The covariance $\mathbf{P}$ needs to be estimated from the particles; for a particle set $\{w_k^i = \frac{1}{N}, \mathbf{x}_k^i\}_{i=1}^{N}$ at time $k$ we have:

$$ P_{k|k} = \frac{1}{N-1} \sum_{i=1}^{N} (\mathbf{x}_k^i - \hat{\mathbf{x}}_{k|k})(\mathbf{x}_k^i - \hat{\mathbf{x}}_{k|k})^{\mathsf{T}} \tag{41} $$

where $\hat{\mathbf{x}}_{k|k} = \frac{1}{N}\sum_{i=1}^{N} \mathbf{x}_k^i$ is the mean of particles.

Using the KDE method (39), it is possible to approximate the boundary of the credible set $\mathbf{C}_k(\alpha)$. The computation involved, however, would be prohibitively expensive, and we propose a simpler approximation of $\rho_k$ in (38) as follows:

$$ \rho_k = \begin{cases} 1, & \text{if } \tilde{s}(\mathbf{x}_k) \ge \min\limits_{i=1,\dots,N} \tilde{s}(\mathbf{x}_k^i), \\ 0, & \text{otherwise}, \end{cases} \tag{42} $$

where $\mathbf{x}_k$ is the true target state at the time $k$ and $\tilde{s}$ was defined in (39). The value of $\min\limits_{i=1,\dots,N} \tilde{s}(\mathbf{x}_k^i)$ in (42) effectively defines the boundary of $\mathbf{C}_k$ at some $\alpha \ll 1$ in such a manner that set $\mathbf{C}_k$ includes all particles. The boundary itself, however, does not need to be computed.

The volume criterion $\nu_k$ approximates the volume of $\mathbf{C}_k(\alpha)$ by the spread of particles. In practice $\nu_k$ is approximated by the trace of the covariance $P_{k|k}$ in (41).

### B. Computation of $\rho_k$ and $\nu_k$ for the Bernoulli Box-PF

The Bernoulli Box-PF reports, at the end of each cycle, the set of equally weighted box particles $[\mathbf{x}_k^i]$, $i = 1, \dots, N$. The computation of the credible set $\mathbf{C}_k(\alpha)$ at $\alpha \to 1$ from box-particles is straightforward as it does not require the KDE method. Instead, $\mathbf{C}_k(1)$ is approximated simply by the union of all box particles, that is

$$ \mathbf{C}_k(1) = \bigcup_{i=1}^{N} [\mathbf{x}_k^i]. \tag{43} $$

Inclusion $\rho_k$ follows directly from (38) as

$$ \rho_k = \begin{cases} 1, & \text{if } \mathbf{x}_k \in \bigcup_{i=1}^{N} [\mathbf{x}_k^i], \\ 0, & \text{otherwise}, \end{cases} \tag{44} $$

where $\mathbf{x}_k$ is the true target state at time instant $k$. The volume $\nu_k$ is calculated according to

$$ \nu_k = \sum_{j=1}^{n_x} \sigma_k^2(j), \tag{45} $$

where $\sigma_k^2(j)$ was given in (36).

## VII. NUMERICAL EXAMPLES

This section demonstrates the performance of the two described implementations of the Bernoulli filter. First, the target and measurement characteristics will be defined, followed by a single run of each filter. Finally a Monte Carlo simulation based comparison using the described performance criteria of inclusion and spread will be carried out.

### A. Simulation Setup

Consider the problem of tracking a target in two-dimensional plane using range, range-rate and azimuth measurements. The target state vector is $\mathbf{x} = \begin{bmatrix} x & \dot{x} & y & \dot{y} \end{bmatrix}^{\mathsf{T}}$, where $(x, y)$ and $(\dot{x}, \dot{y})$ are the target position and velocity, respectively, in Cartesian coordinates. The target is moving according to the nearly constant velocity motion model with transitional density $\pi_{k+1|k}(\mathbf{x}|\mathbf{x}') = \mathcal{N}(\mathbf{x}; \mathbf{F}\mathbf{x}', \mathbf{Q})$. Here

$$ \mathbf{F} = \mathbf{I}_2 \otimes \begin{bmatrix} 1 & T \\ 0 & 1 \end{bmatrix}, \qquad \mathbf{Q} = \mathbf{I}_2 \otimes \begin{bmatrix} \frac{T^3}{3} & \frac{T^2}{2} \\ \frac{T^2}{2} & T \end{bmatrix} \cdot \varpi \tag{46} $$

with $\otimes$ being the Kronecker product, $T = t_{k+1} - t_k$ the sampling interval and $\varpi$ the intensity of process noise [29]. The target appears at scan $k = 3$ and disappears at scan $k = 54$. Initially (at $k = 0$) the target is located at $(550\ \text{m}, 300\ \text{m})$ and is moving with velocity $(-5\ \text{m/s}, -8.5\ \text{m/s})$. The sensor is static, located at the origin of the $x - y$ plane. Other values are adopted as $\varpi = 0.05$, $T = 1$ s, with the total observation interval of $60$s.

The measurement function $h_k(\mathbf{x})$ is defined as:

$$ h_k(\mathbf{x}) = \left[ \sqrt{x^2 + y^2},\ \frac{x\dot{x} + y\dot{y}}{\sqrt{x^2 + y^2}},\ \arctan(y/x) \right]^{\mathsf{T}}. \tag{47} $$

The measurement noise $\mathbf{v}$ is zero mean white Gaussian with a covariance $\mathbf{\Sigma} = \mathrm{diag}[\sigma_r^2,\ \sigma_{\dot{r}}^2,\ \sigma_\theta^2]$, where $\sigma_r = 2.5$ m, $\sigma_{\dot{r}} = 0.01$ m/s and $\sigma_\theta = 0.25^{\circ}$. For the Box-PF, we use the 99% interval confidences $3\sigma_r$, $3\sigma_{\dot{r}}$ and $3\sigma_\theta$ to model a uniform noise as in Equation (26). Note that mixture of Uniform pdfs can be used instead (at a computation cost).

The sensors provides interval measurements, with an interval length $\mathbf{\Delta} = [\Delta r,\ \Delta\dot{r},\ \Delta\theta]^{\mathsf{T}}$, where $\Delta r = 50$ m, $\Delta\dot{r} = 0.2$ m/s and $\Delta\theta = 4^{\circ}$ are the lengths of intervals in range, range-rate and azimuth, respectively.

The sensor has a bias (systematic error) in the sense that the vector $h_k(\mathbf{x}) + \mathbf{v}_k$ is not in the middle of the measurement interval. A measurement at $k$ is thus defined as:

$$ [\mathbf{z}]_k = [h_k(\mathbf{x}) + \mathbf{v}_k - \frac{3}{4}\mathbf{\Delta},\ h_k(\mathbf{x}) + \mathbf{v}_k + \frac{1}{4}\mathbf{\Delta}]. \tag{48} $$

The two Bernoulli filters are ignorant of the bias.

The probability of detection is $p_D = 0.95$, the mean number of false detections per scan is $\lambda = 5$. The false alarm probability $c([\mathbf{z}])$ is assumed constant for all volumes of $[\mathbf{z}]$, across the range (mid intervals from 30m to 700m), range-rate (mid intervals from $-15$ m/s to $+15$ m/s) and azimuth (mid intervals from $-\pi/2$ rad to $\pi/2$ rad). The reporting threshold $\tau$ is set to $0.5$. The filtering algorithms have the following prior information: $p_D$, false alarm statistics $\lambda$ and $c([\mathbf{z}])$, measurement function $h_k(\mathbf{x})$, covariance matrix $\mathbf{\Sigma}$ and the transitional density $\pi_{k+1|k}(\mathbf{x}|\mathbf{x}')$. The filters are making an inference at every $k$ using measurements $\boldsymbol{\Upsilon}_{1:k}$, and the following parameters: $p_B = 0.01$, $p_S = 0.98$, $n_0$ and $N$. The number of particles or box particles $N$ will be varied.

The implementation of birth density, discussed in Sec.IV-A, is based on the range and azimuth component of each measurement (i.e. neglecting the range-rate), using $\mathbf{p} = [x \;\; y]^{\mathsf{T}}$ and $\mathbf{u} = [\dot{x} \;\; \dot{y}]^{\mathsf{T}}$. The prior for $\dot{x}$ and $\dot{y}$ is a uniform density from $-15$ m/s to $+15$ m/s.

Parameter $n_0$ (see Sec. IV) which is the number of newborn particles at each time and for each measurement is also varied, but only for the Bernoulli PF. We will see that the choice of $n_0$ influences the Bernoulli PF error performance and its computation time. In contrast, parameter $n_0$ is not critical for the Bernoulli Box-PF performance. In all numerical tests, we set $n_0 = 1$: one box particle is sufficient to cover entirely the region of the state space defined by a measurement and the prior.

The experiment and both Bernoulli filters were implemented in MATLAB.

### B. Single runs

First we illustrate single runs of both Bernoulli filters. Fig. 2.(a) shows the output of a typical run of the Bernoulli PF for the testing scenario at time $k = 51$. The green regions represent the measurements, the red asterisk is the true target location, while the gray dots are the particles (number of particles $N = 5000$). Although the particle mean $\hat{\mathbf{x}}_{k|k}$ is a biased estimate of the target state, the particles populate the volume of the state space $\mathcal{X}$ where the true value resides. Fig. 2.(b) shows the estimate of the probability of target existence $q_{k|k}$ over time. Target presence is established at $k = 5$ with $q_{k|k}$ remaining close to $1.0$ after that. Occasionally, when the target detection is missing in the measurement set $\boldsymbol{\Upsilon}_k$, $q_{k|k}$ drops below the value of $1.0$.

[Figure 2](../assets/figure/figure-2.jpg)

Figure 2. Tracking scenario with results at time $k = 51$

The implementation of the Bernoulli Box-PF is based on the INTLAB [30] toolbox, which contains a number of built-in routines for interval calculations. The constraints propagation algorithm [26], used here to contract each box particle at the update step, is presented in Appendix. The original algorithm performs the contractions until the algorithm converges (i.e. there is no more contraction after a specified threshold). In our experiment we are using a loop of 3 iterations (we observed that more contractions do not lead to a significant improvement).

Fig. 3.(a) shows a global view of the filter performance for one single run with measurements generated from (48) and with $N = 32$ box particles. All measurements for 60 scans are plotted by rectangular regions around the sensor. In addition, the blue “plus” marks represent the true target trajectory, while the black circles represent the estimated trajectory. The persistent box particles positions are also shown with rectangular regions. From this snapshot, we can see that: 1) the update step correctly weights the relevant box particles and 2) the Box-PF is able to correctly estimate the target’s trajectory.

Fig. 3(b) shows the estimate of the probability of target existence $q_{k|k}$ over time. Target presence is established at $k = 6$ with $q_{k|k}$ remaining close to $1.0$ after that. Occasionally, when the target detection is missing in the measurement set $\boldsymbol{\Upsilon}_k$, $q_{k|k}$ drops below the value of $1.0$.

### C. Monte Carlo Runs

The average performance of the proposed Bernoulli PF is evaluated via Monte Carlo simulations using the scenario and parameters described in Sec. VII-A. First, the performance criteria presented in Sec. VI are studied.

[Figure 3](../assets/figure/figure-3.jpg)

Figure 3. (a) Snapshot of one run (60 scans) of the box particles Bernoulli filter with $N = 32$. The persistent box particles over the time are shown along with the estimated trajectory and the true one. (b) Estimates of the probability of target existence are also shown for one run.

[Figure 4](../assets/figure/figure-4.jpg)

Figure 4. Average performance over $M = 100$ Monte Carlo runs for the Bernoulli PF using $n_0 = 500$ and $N \in \{500, 1000, 2000, 5000\}$ particles: on the top the probability of existence $q_{k|k}$; in the middle the inclusion $\rho_k$; at the bottom volume (spread) $\nu_k$.

*1) Performance Evaluation via $\rho_k$ and $\nu_k$:* Figs. 4, 5 and 6 show the performance results of the Bernoulli PF using $n_0 = 500$, $n_0 = 1000$ and $n_0 = 5000$ newborn particles, respectively. On the top of each figure is the average probability of target existence $q_{k|k}$; in the middle is the average *inclusion* criterion $\rho_k$; at the bottom is the average volume (spread) $\nu_k$, versus the scan number $k = 1, \cdots, 60$. Averaging was carried out over $M = 100$ independent Monte Carlo runs. Four cases for the number of particles $N$ are displayed: $N = 500$, $N = 1000$, $N = 2000$ and $N = 5000$,

From Figs. 4, 5 and 6 one can observe:

(i) The probability of existence is reliable for all combination of $N$ and $n_0$.

(ii) The inclusion criterion depends on $n_0$ and $N$. Recall that if the average inclusion is $\rho_k = 1$, this means that the true value of the target state $\mathbf{x}_k$ is consistently contained by the support of the particle representation of $s_{k|k}(\mathbf{x})$. Observe that a high value of $n_0$ ($n_0 \ge 5000$) and a high value of $N$ ($N \ge 2000$) are needed to satisfy the inclusion property.

(iii) The volume (spread of particles) $\nu_k$ for all combination of $N$ and $n_0$ is rapidly converging and stabilizing. We can observe that when $n_0$ is fixed, and $N$ increases, the spread is also increasing but very insignificantly. However, when $n_0$ is increasing, we can observe a more visible spread increase.

Fig. 7 shows the average performance of the Bernoulli Box-PF (averaged over $M = 100$ runs), which can be summarized as follows:

(i) The probability of existence is reliable most of the time for all values of $N$,

(ii) One newborn box particle per measurement, that is $n_0 = 1$ is sufficient to satisfy the average inclusion criterion $\rho_k$ provided that $N \ge 32$. This is a useful advantage of the Box-PF implementation compared to the PF implementation.

(iii) The spread $\nu_k$ of box-particles for all combination of $N$ is rapidly converging and stabilizing. The spread change when $N$ is increasing is very insignificant. Finally, the spread of the Box-PF implementation is slightly higher than that of the PF implementation.

*2) Computational Time:* Fig. 8 shows the computational time for the Bernoulli PF using $n_0 = 500$, $n_0 = 1000$ and $n_0 = 5000$. The influence of $n_0$ on the computational time is very critical. This is to be expected since at time $k$ there are $n_0 \cdot m_{k-1}$ newborn particles to process. Fig. 9 shows the computational time for the Bernoulli Box-PF using $n_0 = 1$.

[Figure 5](../assets/figure/figure-5.jpg)

Figure 5. Average performance over $M = 100$ Monte Carlo runs for the Bernoulli PF using $n_0 = 1000$ and $N \in \{500, 1000, 2000, 5000\}$ particles: on the top the probability of existence $q_{k|k}$; in the middle the inclusion $\rho_k$; at the bottom volume (spread) $\nu_k$.

[Figure 6](../assets/figure/figure-6.jpg)

Figure 6. Average performance over $M = 100$ Monte Carlo runs for the Bernoulli PF using $n_0 = 5000$ and $N \in \{500, 1000, 2000, 5000\}$ particles: on the top the probability of existence $q_{k|k}$; in the middle the inclusion $\rho_k$; at the bottom volume (spread) $\nu_k$.

Recall from Sec. VII-C1 that to satisfy the inclusion criterion, the Bernoulli PF requires in excess of $n_0 = 5000$ and $N = 2000$ particles, corresponds to an average computational time of just over $40s$. The Bernoulli Box-PF satisfies the inclusion using just $N \ge 32$ box-particles (with $n_0 = 1$ newborn box-particles), corresponds to an average computation time of about $19s$. Hence, the Box-PF implementation appears to be twice faster. This is despite the fact that interval function calculations were not implemented using MATLAB built-in functions. Although the processing time per box-particle is significantly higher than the processing time per point particles (involving interval analysis calculations), the noticeable reduction in the number of box-particles is responsible for the overall speed-up of this algorithm.

## VIII. CONCLUSIONS

This paper formulated the optimal Bayesian nonlinear filtering problem in the presence of three types of measurement uncertainties: stochastic, set-theoretic and data association uncertainty. Since the optimal filter for this problem has no analytic solution, the paper then proposed two Monte Carlo based approximations. The first is based on the standard particle filtering framework, and referred to as the Bernoulli particle filter. The second, referred to as the Bernoulli box-particle filter is based on box-particles and relies on interval analysis for computations. Finally, the paper presented a comparative analysis of the two filters in the context of target tracking using interval measurements.

Both filters perform comparably well when a sufficient number of particles is used: the presence of a target is reliably detected, while the true target state is contained in the support of the spatial density function. The Bernoulli Box-PF, however, was demonstrated to be more cost efficient: it required twice less computational time and almost hundred time smaller number of particles (that is box-particles). The reduction in the number of particles can be important in the context of distributed networked systems, because of a smaller communication bandwidth requirement.

Future work will focus on the development of a multi-Bernoulli filter for multi-target tracking in the presence of stochastic, set-theoretic and data association uncertainty. Another attractive direction of work is a development of a Bernoulli Box-PF in a distributed environment to take the full advantage in the reduction of particles.

## APPENDIX

*a) Bernoulli filter update equations.:* The original update equations of the Bernoulli filter for the state independent $p_D$ are [10, p.520]:

$$ q_{k+1|k+1} = \frac{1 - p_D + p_D \sum_{[\mathbf{z}] \in \boldsymbol{\Upsilon}_{k+1}} \int g_{k+1}([\mathbf{z}]|\mathbf{x})\, s_{k+1|k}(\mathbf{x})\, d\mathbf{x}\ \frac{\kappa(\boldsymbol{\Upsilon}_{k+1} \setminus \{[\mathbf{z}]\})}{\kappa(\boldsymbol{\Upsilon}_{k+1})}}{q_{k+1|k}^{-1} - p_D + p_D \sum_{[\mathbf{z}] \in \boldsymbol{\Upsilon}_{k+1}} \int g_{k+1}([\mathbf{z}]|\mathbf{x})\, s_{k+1|k}(\mathbf{x})\, d\mathbf{x}\ \frac{\kappa(\boldsymbol{\Upsilon}_{k+1} \setminus \{[\mathbf{z}]\})}{\kappa(\boldsymbol{\Upsilon}_{k+1})}} \tag{49} $$

$$ s_{k+1|k+1}(\mathbf{x}) = \frac{1 - p_D + p_D \sum [\mathbf{z}] \in \boldsymbol{\Upsilon}_{k+1}\, g_{k+1}([\mathbf{z}]|\mathbf{x}) \frac{\kappa(\boldsymbol{\Upsilon}_{k+1} \setminus \{[\mathbf{z}]\})}{\kappa(\boldsymbol{\Upsilon}_{k+1})}}{1 - p_D + p_D \sum_{[\mathbf{z}] \in \boldsymbol{\Upsilon}_{k+1}} \int g_{k+1}([\mathbf{z}]|\mathbf{x})\, s_{k+1|k}(\mathbf{x})\, d\mathbf{x}\ \frac{\kappa(\boldsymbol{\Upsilon}_{k+1} \setminus \{[\mathbf{z}]\})}{\kappa(\boldsymbol{\Upsilon}_{k+1})}}\, s_{k+1|k}(\mathbf{x}) \tag{50} $$

where $\setminus$ denotes the set-minus operation and $\kappa(\boldsymbol{\Upsilon})$ is the pdf of the false alarm random finite set $\boldsymbol{\Upsilon}$. Under the assumption made in Sec.II the false alarm set is a Poisson RFS, whose multi-object pdf is given by [10, p.366]: $\kappa(\boldsymbol{\Upsilon}) = e^{-\lambda} \prod_{[\mathbf{z}] \in \boldsymbol{\Upsilon}} \lambda\, c([\mathbf{z}])$. Then it follows that

$$ \frac{\kappa(\boldsymbol{\Upsilon}_{k+1} \setminus \{[\mathbf{z}]\})}{\kappa(\boldsymbol{\Upsilon}_{k+1})} = \frac{1}{\lambda\, c([\mathbf{z}])}, \tag{51} $$

which leads to the update equations in the form given by eqs.(7)-(9).

*b) Constraints propagation algorithm.:* The CP algorithm [26] that was used in the numerical example in which the measurements are intervals in the range, range-rate, azimuth space, is presented in Algorithm 3. This algorithm performs the contraction of each box particle at the update step.

[Algorithm 3](../assets/figure/algorithm-3.jpg)

**Algorithm 3** Constraints propagation algorithm

1: **Input**: $[\mathbf{x}] = [x] \times [\dot{x}] \times [y] \times [\dot{y}]$, $[\mathbf{z}] = [r] \times [\dot{r}] \times [\beta]$

***constraint*** $1$

2: $[x] = [x] \cap \sqrt{([r]^2 - [y]^2)}$

3: $[y] = [y] \cap \sqrt{([r]^2 - [x]^2)}$

4: $[r] = [r] \cap \sqrt{([x]^2 + [y]^2)}$

***constraint*** $2$

5: $[x] = [x] \cap \frac{[\dot{x}][\dot{y}][y]}{[\dot{r}]^2-[\dot{x}]} + \sqrt{\frac{([\dot{y}]^2-[\dot{r}]^2)y^2}{[\dot{r}]^2-[\dot{x}]^2} + \frac{[\dot{x}][\dot{y}][y]}{[\dot{r}]^2-[\dot{x}]^2}}$

6: $[y] = [y] \cap \frac{[\dot{y}][\dot{x}][x]}{[\dot{r}]^2-[\dot{y}]} + \sqrt{\frac{([\dot{x}]^2-[\dot{r}]^2)x^2}{[\dot{r}]^2-[\dot{y}]^2} + \frac{[\dot{y}][\dot{x}][x]}{[\dot{r}]^2-[\dot{y}]^2}}$

7: $[\dot{x}] = [\dot{x}] \cap \frac{[\dot{r}].(\sqrt{[x]^2+[y]^2})-[y].[\dot{y}]}{[x]}$

8: $[\dot{y}] = [\dot{y}] \cap \frac{[\dot{r}].(\sqrt{[x]^2+[y]^2})-[x].[\dot{x}]}{[y]}$

9: $[\dot{r}] = [\dot{r}] \cap \frac{[x].[\dot{x}]+[y].[\dot{y}]}{\sqrt{[x]^2+[y]^2}}$

***constraint*** $3$

10: $[x] = [x] \cap \frac{[y]}{[\tan]{}([\beta])}$

11: $[y] = [y] \cap [\tan]{}([\beta]).[x]$

12: $[\beta] = [\beta] \cap [\arctan]{}(\frac{[y]}{[x]})$

13: **Output**: $[\mathbf{x}] = [x] \times [\dot{x}] \times [y] \times [\dot{y}]$,

[Figure 7](../assets/figure/figure-7.jpg)

Figure 7. Average performance over $M = 100$ Monte Carlo runs for the Bernoulli Box-PF using $n_0 = 1$ and $N \in \{8, 16, 20, 32, 44, 52\}$ box particles: on the top the probability of existence $q_{k|k}$, in the middle the inclusion $\rho_k$, at the bottom volume (spread) $\nu_k$.

[Figure 8](../assets/figure/figure-8.jpg)

Figure 8. Computational time averaged over $M = 100$ runs for the Bernoulli PF an a function of the number of particles $N$. We show the results for $n_0 = 500, 1000, 5000$.

[Figure 9](../assets/figure/figure-9.jpg)

Figure 9. Computational time over $M = 100$ runs for the Bernoulli Box-PF an a function of the number of particles $N$ and using $n_0 = 1$.

**Acknowledgements.** A. Gning and L. Mihaylova acknowledge the support of the EPSRC project EP/E027253/1 and all the authors are thankful to the [European Community’s] Seventh Framework Programme [FP7/2007-2013] under grant agreement No 238710 (Monte Carlo based Innovative Management and Processing for an Unrivalled Leap in Sensor Exploitation).

## REFERENCES

[1] A. H. Jazwinski, *Stochastic Processes and Filtering Theory*. Academic Press, 1970.

[2] M. Milanese and A. Vicino, “Optimal estimation theory for dynamic systems with set membership uncertainty: An overview,” *Automatica*, vol. 27, no. 6, pp. 997–1009, 1991.

[3] P. L. Combettes, “Foundations of set theoretic estimation,” *Proc. IEEE*, vol. 81, no. 2, pp. 182–208, 1993.

[4] P. Smets, “Imperfect information: Imprecision and uncertainty,” in *Uncertainty Management in Information Systems*, 1996, pp. 225–254.

[5] G. J. Klir and M. J. Wierman, *Uncertainty-based information: Elements of generalized information theory*, 2nd ed. New York: Physica-Verlag, 1999.

[6] T. O’Hogan, “Dicing with the unknown,” *Significance*, vol. 1, no. 3, pp. 132–133, Sep. 2004.

[7] V. Klumpp, B. Noack, M. Baum, and U. D. Hanebeck, “Combined set-theoretic and stochastic estimation: A comparison of the SSI and CS filter,” in *Proc. 13th Int. Conf. Information Fusion*, Edinburgh, UK, July 2010.

[8] J. O. Berger, *Statistical Decision Theory and Bayesian Analysis*. New York: Springer Series in Statistics, 1985.

[9] A. Benavoli and A. Antonucci, “Aggregating imprecise probabilistic knowledge,” in *Proc. 6th International Symposium on Imprecise Probability*, Durham, UK, 2009.

[10] R. Mahler, *Statistical Multisource Multitarget Information Fusion*. Artech House, 2007.

[11] S. M. Kay, *Fundamentals of Statistical Signal Processing: Detection theory*. Prentice Hall, 1998.

[12] A. Doucet, J. F. G. de Freitas, and N. J. Gordon, Eds., *Sequential Monte Carlo Methods in Practice*. Springer, 2001.

[13] B. Ristic, S. Arulampalam, and N. Gordon, *Beyond the Kalman filter: Particle filters for tracking applications*. Artech House, 2004.

[14] F. Abdallah, A. Gning, and P. Bonnifait, “Box particle filtering for nonlinear state estimation using interval analysis,” *Automatica*, vol. 44, pp. 807–815, 2008.

[15] A. Gning, L. Mihaylova, and F. Abdallah, “Mixture of uniform probability density functions for non linear state estimation using interval analysis,” in *Proc. 13th Intern. Conf. Information Fusion*, Edinburgh, UK, July 2010.

[16] B. Ristic, A. Gning, and L. Mihaylova, “Nonlinear filtering using measurements affected by stochastic, set-theoretic and association uncertainty,” in *Proc. 14th Intern. Conf. Information Fusion*, Chicago, USA, July 2011, pp. 1069–1076.

[17] A. Gning, B. Ristic, and L. Mihaylova, “A box particle filter for stochastic set-theoretic measurements with association uncertainty,” in *Proc. 14th Intern. Conf. Information Fusion*, Chicago, USA, July 2011, pp. 716–723.

[18] B.-T. Vo, “Random finite sets in multi-object filtering,” Ph.D. dissertation, School of EECE, The University of Western Australia, June 2008.

[19] D. Mušicki, R. Evans, and S. Stankovic, “Integrated probabilistic data association,” *IEEE Trans. Automatic Control*, vol. 39, no. 6, pp. 1237–1240, June 1994.

[20] R. Mahler, “General bayes filtering of quantized measurements,” in *Proc. 14th Int. Conf. Information Fusion*, Chicago, USA, July 2011, pp. 346–352.

[21] ——, “Generalized likelihood function and measure theory,” July 2011, unpublished note.

[22] R. Curry, W. Velde, and J. Potter, “Nonlinear estimation with quantized measurements–pcm, predictive quantization, and data compression,” *Information Theory, IEEE Transactions on*, vol. 16, no. 2, pp. 152 – 161, mar 1970.

[23] D. Crisan and A. Doucet, “A survey of convergence results on particle filtering methods for practitioners,” *IEEE Trans. Signal Processing*, vol. 50, no. 3, pp. 736–746, 2002.

[24] F. Caron, P. D. Moral, M. Pace, and B. N. Vo, “On the stability and approximation of branching distribution flows with applications to nonlinear multiple target filtering,” INRIA, Bordeaux- Sud Ouest, France, Tech. Rep. 7376, Sept. 2010.

[25] B. T. Vo, B. N. Vo, and A. Cantoni, “The cardinality balanced multi-target multi-Bernoulli filter and its implementations,” *IEEE Trans. Signal Processing*, vol. 57, no. 2, pp. 409–423, 2009.

[26] L. Jaulin, M. Kieffer, O. Didrit, and E. Walter, *Applied Interval Analysis*. Springer, 2001.

[27] R. E. Edwards, “What is the riemann integral?” Dept. of Pure Mathematics, Dept. of Mathematics, Australian National University, 1974.

[28] B. W. Silverman, *Density estimation for statistical and data analysis*. Chapman and Hall, 1986.

[29] Y. Bar-Shalom, X. R. Li, and T. Kirubarajan, *Estimation with Applications to Tracking and Navigation*. John Wiley & Sons, 2001.

[30] S. Rump, *INTLAB - INTerval LABoratory*, ser. Developments in Reliable Computing, T. Csendes, Ed. Dordrecht: Kluwer Academic Publishers, 1999.

## Conversion notes

- Source: accepted author manuscript (second revision, 28 Dec 2011; 15 pages, two-column) from Lancaster EPrints 52300. Authors: Amadou Gning, Branko Ristic, Lyudmila Mihaylova. Published version: IEEE Transactions on Signal Processing 60(5):2138-2151 (2012), doi:10.1109/TSP.2012.2184538; equation numbering and wording may differ slightly from the published article.
- No TeX source exists: all mathematics, equations (1)-(51) and unnumbered displays, was transcribed to LaTeX from high-resolution page crops, with printed numbers as \tag. The authors' inconsistencies are kept as printed (e.g. third affiliation footnote mark, weights outside the sums in (24)/(25), Algorithm 2 step 12, the baseline sum index and missing integral in (50), unsquared terms in Algorithm 3 lines 5-6, 'an a function' in the captions of Figs. 8-9).
- Algorithms 1-3 are image crops followed by line-by-line transcriptions. Algorithm 3 (printed at the top of page 14, inside the reference list) is placed after the appendix paragraph on the constraints propagation algorithm that it belongs to. 'Remark:' on page 5 is printed in regular weight and is given a bold label here. Footnote markers are written [^n] in the running text; each footnote follows as a paragraph starting 'Footnote n:'.
- Figures 1-9 are image crops; legends and tick labels exist only in the images. Floats sit at paragraph boundaries near their printed position.
