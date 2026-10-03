# Verification of Neural Reachable Tubes via Scenario Optimization and Conformal Prediction

**Albert Lin** `albert.k.lin@usc.edu`

**Somil Bansal** `somilban@usc.edu`

*Department of Electrical and Computer Engineering, University of Southern California, CA, USA*

## Abstract

Learning-based approaches for controlling safety-critical autonomous systems are rapidly growing in popularity; thus, it is important to provide rigorous and robust assurances on their performance and safety. Hamilton-Jacobi (HJ) reachability analysis is a popular formal verification tool for providing such guarantees, since it can handle general nonlinear system dynamics, bounded adversarial system disturbances, and state and input constraints. However, it involves solving a Partial Differential Equation (PDE), whose computational and memory complexity scales exponentially with respect to the state dimension, making its direct use on large-scale systems intractable. To overcome this challenge, neural approaches, such as DeepReach, have been used to synthesize reachable tubes and safety controllers for high-dimensional systems. However, verifying these neural reachable tubes remains challenging. In this work, we propose two different verification methods, based on robust scenario optimization and conformal prediction, to provide probabilistic safety guarantees for neural reachable tubes. Our methods allow a direct trade-off between resilience to outlier errors in the neural tube, which are inevitable in a learning-based approach, and the strength of the probabilistic safety guarantee. Furthermore, we show that split conformal prediction, a widely used method in the machine learning community for uncertainty quantification, reduces to a scenario-based approach, making the two methods equivalent not only for verification of neural reachable tubes but also more generally. To our knowledge, our proof is the first in the literature to show a strong relationship between the highly related but disparate fields of conformal prediction and scenario optimization. Finally, we propose an outlier-adjusted verification approach that harnesses information about the error distribution in neural reachable tubes to recover greater safe volumes. We demonstrate the efficacy of the proposed approaches for the high-dimensional problems of multi-vehicle collision avoidance and rocket landing with no-go zones.

**Keywords:** Probabilistic Safety Guarantees, Safety-Critical Learning, Neural Certificates, Hamilton-Jacobi Reachability Analysis, Scenario Optimization, Conformal Prediction

## 1. Introduction

It is important to design provably safe controllers for autonomous systems. Hamilton-Jacobi (HJ) reachability analysis provides a powerful framework to design such controllers for general nonlinear dynamical systems (Lygeros, 2004; Mitchell et al., 2005). In reachability analysis, safety is characterized by the system’s *Backward Reachable Tube (BRT)*. This is the set of states from which trajectories will eventually reach a given target set despite the best control effort. Thus, if the target set represents undesirable states, the BRT represents unsafe states and should be avoided. Along with the BRT, reachability analysis provides a safety controller to keep the system outside the BRT.

Traditionally, the BRT computation in HJ reachability is formulated as an optimal control problem. The BRT can then be obtained as a sub-zero level solution of the corresponding value function. Obtaining the value function requires solving a partial differential equation (PDE) over a state-space grid, resulting in an exponentially scaling computation complexity with the number of states (Bansal et al., 2017). To overcome this challenge, a variety of solutions have been proposed that trade off between the class of dynamics they can handle, the approximation quality of the BRT, and the required computation. These include specialized methods for linear and affine dynamics (Greenstreet and Mitchell, 1998; Frehse et al., 2011; Kurzhanski and Varaiya, 2000, 2002; Maidens et al., 2013; Girard, 2005; Althoff et al., 2010; Bak et al., 2019; Nilsson and Ozay, 2016), polynomial dynamics (Majumdar et al., 2014; Majumdar and Tedrake, 2017; Dreossi et al., 2016; Henrion and Korda, 2014), monotonic dynamics (Coogan and Arcak, 2015), and convex dynamics (Chow et al., 2017) (see Bansal et al. (2017); Bansal and Tomlin (2021) for a survey).

Owing to the success of deep learning, there has also been a surge of interest in approximating high-dimensional BRTs (Rubies-Royo et al., 2019; Fisac et al., 2019; Djeridane and Lygeros, 2006; Niarchos and Lygeros, 2006; Darbon et al., 2020) and optimal controllers (Onken et al., 2022) through deep neural networks (DNNs). Building upon this line of work, Bansal and Tomlin (2021) have proposed DeepReach – a toolbox that leverages recent advances in neural implicit representations and neural PDE solvers to compute a value function and a safety controller for high-dimensional systems. Compared to the aforementioned methods, DeepReach can handle general nonlinear dynamics, the presence of exogenous disturbances, as well as state and input constraints during the BRT computation. Consequently, methods for verifying neural reachable tubes have been proposed. For example, Lin and Bansal (2023) propose an iterative scenario-based method (Campi et al., 2009) to recover probabilistically safe reachable tubes from DeepReach solutions up to a desired confidence level and bound on violation rate. Unfortunately, the method does not allow an after-the-fact risk-return trade-off, and as a result, it is highly sensitive to outlier errors in the learned solutions. This can lead to highly conservative reachable tubes and a severe loss of recovery in the case of stringent safety requirements, as we demonstrate in our case studies.

In this work, we propose two different verification methods, one based on robust scenario optimization and the other based on conformal prediction, to provide probabilistic safety guarantees for neural reachable tubes. Both methods are resilient to the outlier errors in neural reachable tubes and automatically trade-off the strength of the probabilistic safety guarantees based on the outlier rate. The proposed methods can evaluate any candidate tube and are not restricted to a specific class of system dynamics or value functions. We further prove that these seemingly different verification methods naturally reduce to one another, providing a unifying viewpoint for uncertainty quantification (typical use case of conformal prediction) and error optimization (typical use case of scenario optimization) in neural reachable tubes. Based on these insights, we propose an outlier-adjusted verification approach that can recover a greater safe volume from a neural reachable tube by harnessing information about the distribution of error in the learned solution. To summarize, the key contributions of this paper are:

- probabilistic safety verification methods for neural reachable tubes that enable a direct trade-off between resilience and the probabilistic strength of safety,
- a proof that split conformal prediction reduces to a scenario-based approach in general, demonstrating a strong relationship between the two highly related but disparate fields,
- an outlier-adjusted verification approach that recovers greater safe volumes from tubes, and
- a demonstration of the proposed approaches for the high-dimensional problems of multi-vehicle collision avoidance and rocket landing with no-go zones.

## 2. Problem Setup

Consider a dynamical system with state $x \in X \subseteq \mathbb{R}^n$, control $u \in \mathcal{U}$, and dynamics $\dot{x} = f(x, u)$ governing how $x$ evolves over time until a final time $T$. Let $\xi_{x,t}^{u}(\tau)$ denote the state achieved at time $\tau \in [t, T]$ by starting at initial state $x$ and time $t$ and applying control $u(\cdot)$ over $[t,\tau]$. Let $\mathcal{L}$ represent a target set that the agent wants to either reach (e.g. goal states) or avoid (e.g. obstacles).

***Running example: Multi-Vehicle Collision Avoidance.*** Consider a 9D multi-vehicle collision avoidance system with 3 independent Dubins3D cars: $Q_1, Q_2, Q_3$. $Q_i$ has position $(p_{xi}, p_{yi})$, heading $\theta_i$, constant velocity $v$, and steering control $u_i \in [u_{\min}, u_{\max}]$. The dynamics of $Q_i$ are: $\dot{p}_{xi} = v\cos{\theta_i}, \quad \dot{p}_{yi} = v\sin{\theta_i}, \quad \dot{\theta_i} = u_i$. $\mathcal{L}$ is the set of states where any of the vehicle pairs is in collision: $\mathcal{L} = \{x: \min\{d(Q_1, Q_2), d(Q_1, Q_3), d(Q_2, Q_3)\} \le R\}$, where $d(Q_i, Q_j)$ is the distance between $Q_i$ and $Q_j$. We set: $v=0.6, \quad u_{\min}=-1.1, \quad u_{\max}=1.1, \quad R=0.25$.

In this setting, we are interested in computing the system’s initial-time Backward Reachable Tube, which we denote as BRT. We define BRT as the set of all initial states in $X$ from which the agent will eventually reach $\mathcal{L}$ within the time horizon $[0, T]$, despite best control efforts: $\text{BRT} = \{x: x\in X, \forall u(\cdot), \exists \tau \in [0, T], \xi_{x,0}^{u}(\tau) \in \mathcal{L}\}$. When $\mathcal{L}$ represents unsafe states for the system, as it does in our running example, staying outside of BRT is desirable. When $\mathcal{L}$ instead represents the states that the agent wants to reach, BRT is defined as the set of all initial states in $X$ from which the agent, acting optimally, can eventually reach $\mathcal{L}$ within $[0, T]$. Thus, staying within BRT is desirable.

The above 9D system is intractable for traditional grid-based methods, motivating the use of DeepReach to learn a neural BRT. Our goal in this work is to recover an approximation of the safe set with probabilistic guarantees. Specifically, we want to find $\mathcal{S}$ such that $\underset{x \in \mathcal{S}}{\mathbb{P}} ( x \in \text{BRT} ) \le \epsilon$ for some violation parameter $\epsilon \in (0, 1)$. When $\mathcal{L}$ represents goal states, we want $\underset{x \in \mathcal{S}}{\mathbb{P}} ( x \in \text{BRT}^C ) \le \epsilon$.

## 3. Background: Hamilton-Jacobi Reachability, DeepReach, and Safety Verification

Here, we provide a quick overview of Hamilton-Jacobi reachability analysis, a specific toolbox, DeepReach, to compute high-dimensional neural reachable tubes, and an iterative scenario-based method for recovering probabilistically safe tubes from learning-based methods like DeepReach.

### 3.1. Hamilton-Jacobi (HJ) Reachability

In HJ reachability, computing BRT is formulated as an optimal control problem. We will explain it in the context of $\mathcal{L}$ being a set of undesirable states. In the end, we will comment on when $\mathcal{L}$ is a set of desirable states and refer interested readers to Bansal et al. (2017) for other cases.

We first define a target function $l(x)$ such that the sub-zero level of $l(x)$ yields $\mathcal{L}$: $\mathcal{L} = \{x: l(x) \le 0\}$. $l(x)$ is commonly a signed distance function to $\mathcal{L}$. For example, we can choose $l(x) = \min\{d(Q_1, Q_2), d(Q_1, Q_3), d(Q_2, Q_3)\}-R$ for our running example in Section 2. Next, we define the cost function of a state corresponding to some policy $u(\cdot)$ to be the minimum of $l(x)$ over its trajectory: $J_{u(\cdot)}(x,t) = \min_{\tau \in [t, T]} l(\xi_{x,t}^{u}(\tau))$. Since the system wants to avoid $\mathcal{L}$, our goal is to maximize $J_{u(\cdot)}(x,t)$. Thus, the value function corresponding to this optimal control problem is:

$$
V(x,t) = \sup_{u(\cdot)} J_{u(\cdot)}(x,t) \tag{1}
$$

By defining our optimal control problem in this way, we can recover BRT using the value function. In particular, the value function being sub-zero implies that the target function is sub-zero somewhere along the optimal trajectory, or in other words, that the system has reached $\mathcal{L}$. Thus, BRT is given as the sub-zero level set of the value function at the initial time: $\text{BRT} = \{x: x\in X, V(x,0) \le 0 \}$. The value function in Equation (1) can be computed using dynamic programming, resulting in the following final value Hamilton-Jacobi-Bellman Variational Inequality (HJB-VI): $\min\Big\{D_t V(x,t)+ H(x,t), l(x)-V(x,t)\Big\} = 0$, with the terminal value function $V(x,T) = l(x)$. $D_t$ and $\nabla$ represent the time and spatial gradients of $V$. $H$ is the Hamiltonian that encodes the role of dynamics and the optimal control: $H(x,t) = \max_u \langle \nabla V(x,t), f(x,u)\rangle$. The value function in Equation (1) induces the optimal safety controller: $u^{\ast}(x,t) = \underset{u}{\arg\max} \langle \nabla V(x,t), f(x,u)\rangle$. Intuitively, the safety controller aligns the system dynamics in the direction of the value function’s gradient, thus steering the system towards higher-value states, i.e., away from $\mathcal{L}$.

We have just explained the case where $\mathcal{L}$ represents a set of undesirable states. When the system instead wants to reach $\mathcal{L}$, an infimum is used instead of a supremum in Equation (1). The control wants to reach $\mathcal{L}$, hence there is a minimum instead of a maximum in the Hamiltonian and optimal safety controller equations. See Bansal et al. (2017) for details on other reachability cases.

Traditionally, the value function is computed by solving the HJB-VI over a discretized grid in the state space. Unfortunately, doing so involves computation whose memory and time complexity scales exponentially with respect to the system dimension, making these methods practically intractable for high-dimensional systems, such as those beyond 5D. Fortunately, a deep learning approach, DeepReach, has been proposed to enable HJ reachability for high-dimensional systems.

### 3.2. DeepReach and an Iterative Scenario-Based Probabilistic Safety Verification Method

Instead of solving the HJB-VI over a grid, DeepReach (Bansal and Tomlin, 2021) learns a parameterized approximation of the value function using a sinusoidal deep neural network (DNN). Thus, memory and complexity requirements for training scale with the value function complexity rather than the grid resolution, allowing it to obtain BRTs for high-dimensional systems. DeepReach trains the DNN via self-supervision on the HJB-VI itself. Ultimately, it takes as input a state $x$ and time $t$, and it outputs a learned value function $\tilde{V}(x,t)$. $\tilde{V}(x,t)$ also induces a corresponding safe policy $\tilde{\pi}(x,t)$, as well as a BRT (referred to as the neural reachable tube from hereon).

However, the neural reachable tube will only be as accurate as $\tilde{V}(x,t)$. To obtain a provably safe BRT, Lin and Bansal (2023) propose a uniform value correction bound which is defined, for the avoid case, as the maximum learned value of an unsafe state under the induced policy: $\delta_{\tilde{V},\tilde{\pi}} := \max_{x\in X}\{\tilde{V}(x,0): J_{\tilde{\pi}}(x,0) \le 0\}$. The authors show that the super-$\delta_{\tilde{V},\tilde{\pi}}$ level set of $\tilde{V}(x,0)$ is provably safe under the policy $\tilde{\pi}(x,t)$. They also propose an iterative scenario-based probabilistic verification method for computing an approximation of $\delta_{\tilde{V},\tilde{\pi}}$ from finite random samples that satisfies a desired confidence level and violation rate. However, the method is sensitive to outlier errors in the neural reachable tube and can result in very conservative safe sets. Specifically, it does not provide safety assurances for safe sets with nonzero empirical safety violations.

In this work, we propose probabilistic safety verification methods that allow nonzero empirical safety violations at the cost of the probabilistic strength of safety. This enables a direct trade-off between resilience to outlier errors and the strength of the safety guarantee.

**Remark 1** Although we work with DeepReach solutions in particular for our problem setup, our proposed approaches can verify any general $\tilde{V}(x,t)$ and $\tilde{\pi}(x,t)$, regardless of whether DeepReach, a numerical PDE solver, or some other tool is used to obtain them.

## 4. Robust Scenario-Based Probabilistic Safety Verification Method

Here, we propose a robust scenario-based probabilistic safety verification method for neural reachable tubes. The new method is a straightforward application of a scenario-based sampling-and-discarding approach to chance-constrained optimization problems, which quantifies the trade-off between feasibility and performance of the optimal solution based on finite samples (Campi and Garatti, 2011). First, we explain the method when $\mathcal{L}$ represents undesirable states. In the end, we comment on when $\mathcal{L}$ represents desirable states.

***Procedures:*** Let $\mathcal{S} \subseteq X$ be a neural safe set that is, in the avoid case, the *complement* of the neural reachable tube being verified. In our case, $\mathcal{S}$ is typically a super-$\delta$ level set of the learned value function $\tilde{V}(x,0)$. Ideally, any super-$\delta$ level set of $\tilde{V}(x,0)$ for $\delta > 0$ should be a valid safe set; however, due to learning errors, that might not be true in practice. To provide a probabilistic safety assurance for $\mathcal{S}$, we first sample $N$ independent and identically distributed (i.i.d.) states $x_{1:N}$ from $\mathcal{S}$ according to some probability distribution $\mathbb{P}$ over $\mathcal{S}$. Since $\mathcal{S}$ is defined implicitly by $\tilde{V}(x,0)$, we use rejection sampling. We next compute the costs $J_{\tilde{\pi}}(x_i,0)$ for $i=1, 2, ..., N$ by rolling out the system trajectory from $x_i$ under $\tilde{\pi}(x,t)$. Let $k$ refer to the number of “outliers” - samples that are empirically unsafe, i.e., $J_{\tilde{\pi}}(x_i,0) \le 0$. Then the following theorem provides a probabilistic guarantee on the safety of the neural reachable tube and its complement, the neural safe set $\mathcal{S}$:

**Theorem 2 (Robust Scenario-Based Probabilistic Safety Verification)** Select a safety violation parameter $\epsilon \in (0, 1)$ and a confidence parameter $\beta \in (0, 1)$ such that

$$
\sum^k_{i=0} \binom{N}{i} \epsilon^i (1-\epsilon)^{N-i} \le \beta \tag{2}
$$

where $k$ and $N$ are as defined above. Then, with probability at least $1-\beta$, the following holds:

$$
\underset{x \in \mathcal{S}}{\mathbb{P}} \left( V(x,0) \le 0 \right) \le \epsilon \tag{3}
$$

All proofs can be found in the Appendix of the extended version of this article $^{1}$. Disregarding the confidence parameter $\beta$ for a moment, Theorem 2 states that the fraction of $\mathcal{S}$ that is unsafe is bounded above by the violation parameter $\epsilon$, where $\epsilon$ is computed empirically using Equation (2) based on the outlier rate $k$ encountered within $N$ samples. $\epsilon$ is thus a reflection of the safety quality of $\mathcal{S}$, which degrades with the increase in the number of outliers $k$, as expected. This can also be seen for the running example in Figure 1 (the red curve). Overall, Theorem 2 allows us to compute probabilistic safety guarantees for any neural set $\mathcal{S}$ based on a finite number of samples. Subsequently, this result can be used to find some $\mathcal{S}$ for which $\epsilon$ is smaller than a desired threshold, as we discuss later in this section.

Footnote 1: See `https://sia-lab-git.github.io/Verification_of_Neural_Reachable_Tubes.pdf`

To interpret $\beta$, note that $k$ is a random variable that depends on the randomly sampled $x_{1:N}$. It may be the case that we just happen to draw an unrepresentative sample, in which case the $\epsilon$ bound does not hold. $\beta$ controls the probability of this adverse event happening, which regards the correctness of the probabilistic safety guarantee in Equation (3). Fortunately, $\beta$ goes to $0$ exponentially with $N$, so $\beta$ can be chosen to be an extremely small value, such as $10^{-16}$, when we sample large $N$. $1-\beta$ will then be so close to $1$ that it does not have any practical importance.

We have just explained the robust scenario-based probabilistic safety verification method in the case where $\mathcal{L}$ represents undesirable states. When the system instead wants to reach $\mathcal{L}$, $\mathcal{S}$ will be a sublevel set instead of a superlevel set of the learned value function. The cost inequality should be flipped when computing $k$, and the value inequality should be flipped in Equation (3).

### 4.1. Comparison of Robust and Iterative Scenario-Based Probabilistic Safety Verification

The key difference between the proposed robust scenario-based method and the iterative scenario-based method discussed in Section 3.2 is that the former can handle nonzero empirical safety violations $k$. This enables several crucial advantages that we demonstrate in Figures 1 and 2 for a solution learned by DeepReach on the multi-vehicle collision avoidance running example in Section 2. We have fixed the confidence parameter $\beta = 10^{-16}$ to be so close to $0$ that it has no practical significance ($\beta$ plays the same role in both methods).

[Figure 1](../assets/figure/figure-1.jpg)

Figure 1: (Top) For a fixed simulation budget $N$, the cyan curve shows the number of empirical safety violations $k$ for different learned volumes (different super-levels of $\tilde{V}(x,0)$). The red curve shows the trade-off in safety strength $\epsilon$ (in log scale) for each $k$ using the robust method. The grey point indicates the iterative method baseline. The robust method is able to provide safety assurances even for the volumes that have non-zero outliers. (Dashed black line) By a small decrease in safety level (from 99.999% to 99.974%) caused by outliers, we are able to significantly increase the assured safe volume from 0.56 to 0.81. (Bottom) Correspondingly, the safe set $\mathcal{S}$ increases greatly from the complement of the grey region to the complement of the blue region.

Firstly, for a fixed simulation budget $N$, the robust method allows one to trade off the probabilistic strength of safety (increasing $\epsilon$) for resilience (increasing $k$). In other words, the method can verify any given neural safe set $\mathcal{S}$ in an outlier-robust fashion by automatically attenuating the level of safety assurance based on the number of empirical outliers (i.e., safety violations). The iterative method, in contrast, can only verify a region that is outlier-free. Consequently, the robust method enables one to engage in a trade-off if a large increase in safe set volume can be attained by a tolerable decrease in safety, as illustrated in Figure 1.

[Figure 2](../assets/figure/figure-2.jpg)

Figure 2: (Left) Computing the safety strength $\epsilon$ across different volumes (different super-levels of $\tilde{V}(x,0)$) for different simulation budgets $N$ using the robust method. The grey points indicate the iterative method baselines. (Right) As we increase $N$, the largest volume achieving the desired 99.968% safety using the robust method increases up to a limit.

Secondly, by allowing nonzero safety violations $k$, the robust method provides stronger safety assurances for a *fixed* volume with increment in the simulation budget $N$, as long as the outlier rate does not grow substantially with $N$. Thus, with more simulation effort, significantly larger volumes can be attained *for a desired safety strength $\epsilon$* as shown in Figure 2. Incrementing $N$ in the iterative method, on the other hand, will only correspond to verifying *smaller* volumes at a *stronger* $\epsilon$. It cannot verify larger volumes for a fixed $\epsilon$, because empirical safety violations will be introduced. Figure 2 shows how the robust method (curves) adds a new degree of freedom for computing safety assurances compared to the iterative method (grey points).

## 5. Conformal Probabilistic Safety Verification Method

We now propose a *conformal* probabilistic safety verification method for neural reachable tubes which is intended to be the direct analogue of the *robust scenario-based* method in Section 4. The method is a straightforward application of split conformal prediction, a widely used method in the machine learning community for uncertainty quantification (Angelopoulos and Bates, 2023).

Using the same procedures as described in Section 4, split conformal prediction can be used instead of robust scenario optimization to provide a probabilistic guarantee on the safety of the neural reachable tube and its complement, the neural safe set $\mathcal{S}$:

**Theorem 3 (Conformal Probabilistic Safety Verification)** Let the number of outliers $k$ and the number of samples $N$ be as defined in the procedures in Section 4, then:

$$
\underset{x \in \mathcal{S}}{\mathbb{P}} \left( J_{\tilde{\pi}}(x,0) > 0 \right) \sim \mathrm{Beta}(N-k, k + 1) \tag{4}
$$

Theorem 3 can be established via a straightforward application of conformal prediction with $-J_{\tilde{\pi}}(x,0)$ as the scoring function. The proof is in the Appendix of the extended version of this article $^{1}$. The above theorem states that the fraction of $\mathcal{S}$ that is safe is distributed according to the Beta distribution with shape parameters $N-k$ and $k + 1$. Intuitively, the mass in the distribution shifts towards $0$ as $k$ increases for a fixed $N$, implying that it is more likely that a smaller fraction of $\mathcal{S}$ is safe, as expected. For a fixed ratio $N:k$, $N$ controls how concentrated the mass is around the mean; i.e., for larger sample sizes $N$, we can more confidently determine the fraction of $\mathcal{S}$ that is safe.

To better understand Theorem 3, we show in Figure 3 the Beta distribution of $\underset{x \in \mathcal{S}}{\mathbb{P}} \left( J_{\tilde{\pi}}(x,0) > 0 \right)$ for a solution learned by DeepReach on the multi-vehicle collision avoidance running example in Section 2, for which $k=731$ outliers are found from $N=3684118$ samples.

[Figure 3](../assets/figure/figure-3.jpg)

Figure 3: The Beta distribution of $\underset{x \in \mathcal{S}}{\mathbb{P}} \left( J_{\tilde{\pi}}(x,0) > 0 \right)$ when $k=731$ outliers are found from $N=3684118$ samples. (Dashed black line) For an example choice of confidence $1-\beta=0.9$ (shaded blue), we can lower-bound the fraction of $\mathcal{S}$ which is safe with at least $1-\epsilon=0.99979$ (99.979%) confidence.

**Remark 4** The mean of the Beta distribution in Equation (4) is given as $\frac{N-k}{N+1}$, which is roughly the fraction of the empirically safe samples. One can immediately derive that the safety probability of $\mathcal{S}$, marginalized over the sampled “calibration” states, is given as: $\underset{ \left( x_{1:N},x \right) \in \mathcal{S} }{\mathbb{P}} \left( J_{\tilde{\pi}}(x,0) > 0 \right) \ge \frac{N-k}{N+1}$, which precisely resembles the most commonly used **coverage property** of split conformal prediction.

Even though Theorem 3 provides the distribution of the safety level, when we compute safety assurances in practice, it is often desirable to know a lower-bound on the safety level with at least some desired confidence. This corresponds to choosing a lower-bound whose accumulated probability mass is smaller than some confidence parameter $\beta$ (shaded red in Figure 3). The following lemma formalizes this by using the CDF of the Beta distribution in Theorem 3.

**Lemma 5 (Conformal Probabilistic Safety Verification)** Select a safety violation parameter $\epsilon \in (0, 1)$ and a confidence parameter $\beta \in (0, 1)$ such that

$$
\sum^k_{i=0} \binom{N}{i} \epsilon^i (1-\epsilon)^{N-i} \le \beta \tag{5}
$$

where $k$ and $N$ are as defined above. Then, with probability at least $1-\beta$, the following holds:

$$
\underset{x \in \mathcal{S}}{\mathbb{P}} \left( V(x,0) \le 0 \right) \le \epsilon \tag{6}
$$

Lemma 5 is, in fact, precisely the same result as obtained by Theorem 2 using robust scenario optimization. This is no coincidence, as one can show that split conform prediction more generally reduces to a robust scenario-optimization problem.

**Remark 6** In general, a split conformal prediction problem can be reduced to a robust scenario-optimization problem. This is proven in the Appendix of the extended version of this article. $^{1}$

Due to the equivalence between conformal method and robust scenario-based methods, the analysis in Section 4 holds here as well. More generally, we hope that this insight will lead to future research into further investigating the close relationship between the two methods.

## 6. Outlier-Adjusted Probabilistic Safety Verification Approach

The verification methods in Sections 4 and 5 are limited by the quality of the neural reachable tube. Although they can account for outliers, the computed safety level can be low if the outlier rate is high. This can lead to significant losses in the safe volume, as demonstrated in Sections 6.2 and 6.3.

To address this issue, we propose an outlier-adjusted approach that can recover a larger safe volume for any desired $\epsilon$. Note that in the verification methods, the key quantity which determines $\epsilon$ is the number of safety violations $k$. This corresponds to the number of samples $x_i$ which are marked safe by membership in $\mathcal{S}$, i.e., $\tilde{V}(x_i,0) \ge \delta$, but are not guaranteed to be safe, i.e., $J_{\tilde{\pi}}\left(x_i,0\right) \le 0$. It is easy to see that the best we can do to simultaneously minimize $k$ and maximize volume is to compute $\mathcal{S}$ as the super-$\delta$ level set of the induced *cost* function $J_{\tilde{\pi}}(x,0)$. For example, the largest possible $\mathcal{S}$ that is guaranteed to be violation-free is precisely the super-zero level set of $J_{\tilde{\pi}}(x,0)$. Thus, our overall approach will be to refine $\tilde{V}(x,0)$ so that it more accurately reflects $J_{\tilde{\pi}}(x,0)$.

Modeling $J_{\tilde{\pi}}(x,0)$ can be formulated as a supervised learning problem, since we can sample a state $x_i$ and compute its cost $J_{\tilde{\pi}}(x_i,0)$ in simulation. We learn an approximation $\tilde{J}_{\tilde{\pi}}(x,0)$ by retraining $\tilde{V}(x,0)$ on a training dataset $\mathcal{T}$ of $n$ samples, $\mathcal{T} = (x_1, J_{\tilde{\pi}}(x_1,0)), ..., (x_n, J_{\tilde{\pi}}(x_n,0))$. Specifically, we use the *weighted* MSE loss $\frac{1}{n}\sum_{i=1}^{n}w_{i}(\tilde{V}(x_i,0) - J_{\tilde{\pi}}(x_i,0))^2$, where $w_{i} = w$ if the error is conservative $\left(\tilde{V}(x_i,0) < J_{\tilde{\pi}}(x_i,0)\right)$, otherwise $w_i = 1$. We introduce $w$ as a hyperparameter to underweight conservative errors because in the end, we are concerned with recovering larger *safe* volumes. Thus, selecting a small $w$ allows us to focus on reducing *optimistic* errors $\left(\tilde{V}(x_i,0) > J_{\tilde{\pi}}(x_i,0)\right)$ which are more safety-critical and correspond to outlier safety violations.

To avoid overfitting, we select the training checkpoint that performs best on a validation dataset $\mathcal{V}$. The validation metric we use is the maximum learned cost of an empirically unsafe state: $\max_{x\in \mathcal{V}}\{\tilde{J}_{\tilde{\pi}}(x,0): J_{\tilde{\pi}}(x,0) \le 0\}$, which one can think of as a proxy for the recoverable safe volume. We demonstrate the efficacy of the proposed outlier-adjusted approach for the high-dimensional systems of multi-vehicle collision avoidance and rocket landing with no-go zones. For all case studies, we set $w=10^{-3}$ during retraining, fix the confidence parameter $\beta = 10^{-16}$ and find a safe volume that satisfies $\epsilon \le 10^{-4}$ (99.990% safety) using the robust method in Section 4.

### 6.1. Multi-Vehicle Collision Avoidance

In Figure 4, we compare our outlier-adjusted approach (blue) to the baseline (grey) for a DeepReach solution trained on the multi-vehicle collision avoidance running example in Section 2. A 2.3% increase in the safe volume is attained, shown by the tightened BRT. Note that the largest visual difference in the BRT is where the third vehicle is between the two others; intuitively, the safety in this region is likely more difficult to model by the baseline approach.

[Figure 4](../assets/figure/figure-4.jpg)

Figure 4: Multi-Vehicle Collision Avoidance: outlier-adjusted (blue) and baseline (grey) results. (Left) Slice of the neural BRTs achieving $\epsilon=10^{-4}$ (99.990% safety). (Right) The outlier-adjusted approach increases the safe volume from 0.782 to 0.8 (2.3% increase).

### 6.2. Rocket Landing

We now apply our approach to a 6D rocket landing system with position $(p_{x}, p_{y})$, heading $\theta$, velocity $(v_{x}, v_{y})$, angular velocity $\omega$, and torque controls $\tau_1, \tau_2\in [-250, 250]$. The dynamics are: $\dot{p_x} = v_x, \ \dot{p_y} = v_y, \ \dot{\theta} = \omega, \ \dot{\omega} = 0.3\tau_1, \ \dot{v_x} = \tau_1 \cos{\theta} - \tau_2 \sin{\theta}, \ \dot{v_y} = \tau_1 \sin{\theta} + \tau_2 \cos{\theta} - g$, where $g = 9.81$ is acceleration due to gravity. The target set is the set of states where the rocket reaches a rectangular landing zone of side length 20m centered at the origin: $\mathcal{L} = \{x: |p_x| < 20.0, p_y < 20.0\}$. Note that we want to *reach* $\mathcal{L}$, so the BRT now represents the safe set. Results are shown in Figure 5. Interestingly, a large 9.58% increase in the volume of the safe set is recovered using the proposed approach, particularly near the lower-left part of the state space. Further investigation reveals that the trajectories starting from these states exit the training regime south. This highlights a general limitation of computing the value function over a constrained state space where information is propagated via dynamic programming, which affects both learning-based methods and traditional grid-based methods. Nevertheless, in this case, the relative order of the value function levels is still preserved, leading to a high quality safe policy and recovery of a larger safe volume.

[Figure 5](../assets/figure/figure-5.jpg)

Figure 5: Rocket Landing: outlier-adjusted (blue) and baseline (grey) results. (Left) Slice of the neural BRTs achieving $\epsilon=10^{-4}$ (99.990% safety). (Right) The outlier-adjusted approach increases the safe volume from 0.334 to 0.366 (9.58% increase).

### 6.3. Rocket Landing with No-Go Zones

We now consider the rocket landing problem in a constrained airspace where we have no-go zones of height 100m and width 10m to the left of the landing zone and where altitude is below the landing zone. Safety in this case takes the form of a reach-avoid set - the rocket needs to reach the landing zone while avoiding the no-go zones. An analogous HJI-VI to the one in Section 3.1 can be derived for this case, whose solution can be computed using DeepReach. However, since reach-avoid problems are more complex than just the reach or avoid problem, the DeepReach solution results in a poor safety volume. In fact, *no* safe volume can be recovered with the desired safety level of $\epsilon \le 10^{-4}$. In contrast, we can recover a sizable safe volume using the outlier-adjusted approach, as shown in Figure 6. These examples highlight the utility of the proposed approach.

[Figure 6](../assets/figure/figure-6.jpg)

Figure 6: Rocket Landing with No-Go Zones: outlier-adjusted (blue) and baseline (grey) results. (Left) Slice of the neural BRTs achieving $\epsilon=10^{-4}$ (99.990% safety). (Right) The outlier-adjusted approach increases the safe volume from 0 to 0.19.

## 7. Discussion and Future Work

In this work, we propose two different verification methods, based on robust scenario optimization and conformal prediction, to provide probabilistic safety guarantees for neural reachable tubes. Our methods allow a direct trade-off between resilience to outlier errors in the neural tube, which are inevitable in a learning-based approach, and the strength of the probabilistic safety guarantee. Furthermore, we show that split conformal prediction, a widely used method in the machine learning community for uncertainty quantification, reduces to a scenario-based approach, making the two methods equivalent not only for verification of neural reachable tubes but also more generally. We hope that our proof will lead to future insights into the close relationship between the highly related but disparate fields of conformal prediction and scenario optimization. Finally, we propose an outlier-adjusted verification approach that harnesses information about the error distribution in neural reachable tubes to recover greater safe volumes. We demonstrate the efficacy of the proposed approaches for the high-dimensional problems of multi-vehicle collision avoidance and rocket landing with no-go zones. Altogether, these are important steps toward using learning-based reachability methods to compute safety assurances for high-dimensional systems in the real world.

In the future, we will explore how the key idea of the outlier-adjusted verification approach, using cost labels as a supervised learning signal, can be used to enhance the accuracy of learning-based reachability methods like DeepReach. Other directions include providing safety assurances in the presence of worst-case disturbances and in real-time for tubes that are generated online.

## Acknowledgments

This work is supported in part by a NASA Space Technology Graduate Research Opportunity, the NVIDIA Academic Hardware Grant Program, the NSF CAREER Program under award 2240163, and the DARPA ANSR program.

## References

Matthias Althoff, Olaf Stursberg, and Martin Buss. Computing reachable sets of hybrid systems using a combination of zonotopes and polytopes. *Nonlinear analysis: hybrid systems*, 4(2):233–249, 2010.

Anastasios N. Angelopoulos and Stephen Bates. Conformal prediction: A gentle introduction. *Foundations and Trends® in Machine Learning*, 16(4):494–591, 2023. ISSN 1935-8237. doi: 10.1561/2200000101. URL http://dx.doi.org/10.1561/2200000101.

Stanley Bak, Hoang-Dung Tran, and Taylor T Johnson. Numerical verification of affine systems with up to a billion dimensions. In *International Conference on Hybrid Systems: Computation and Control*, pages 23–32, 2019.

Somil Bansal and Claire J Tomlin. DeepReach: A deep learning approach to high-dimensional reachability. In *IEEE International Conference on Robotics and Automation (ICRA)*, 2021.

Somil Bansal, Mo Chen, Sylvia Herbert, and Claire J Tomlin. Hamilton-Jacobi Reachability: A brief overview and recent advances. In *IEEE Conference on Decision and Control (CDC)*, 2017.

M. C. Campi and S. Garatti. A sampling-and-discarding approach to chance-constrained optimization: feasibility and optimality. *Journal of Optimization Theory and Applications*, 2011.

M. C. Campi, S. Garatti, and M. Prandini. The scenario approach for systems and control design. *Annual Reviews in Control*, 2009.

Yat Tin Chow, Jérôme Darbon, Stanley Osher, and Wotao Yin. Algorithm for overcoming the curse of dimensionality for time-dependent non-convex hamilton–jacobi equations arising from optimal control and differential games problems. *Journal of Scientific Computing*, 73(2-3):617–643, 2017.

Samuel Coogan and Murat Arcak. Efficient finite abstraction of mixed monotone systems. In *Proceedings of the 18th International Conference on Hybrid Systems: Computation and Control*, pages 58–67, 2015.

Jerome Darbon, Gabriel P Langlois, and Tingwei Meng. Overcoming the curse of dimensionality for some hamilton–jacobi partial differential equations via neural network architectures. *Research in the Mathematical Sciences*, 7(3):1–50, 2020.

Badis Djeridane and John Lygeros. Neural approximation of pde solutions: An application to reachability computations. In *Conference on Decision and Control*, pages 3034–3039, 2006.

DLMF. *NIST Digital Library of Mathematical Functions*. https://dlmf.nist.gov/, Release 1.1.11 of 2023-09-15, 2023. URL https://dlmf.nist.gov/. F. W. J. Olver, A. B. Olde Daalhuis, D. W. Lozier, B. I. Schneider, R. F. Boisvert, C. W. Clark, B. R. Miller, B. V. Saunders, H. S. Cohl, and M. A. McClain, eds.

Tommaso Dreossi, Thao Dang, and Carla Piazza. Parallelotope bundles for polynomial reachability. In *International Conference on Hybrid Systems: Computation and Control*, 2016.

Jaime F. Fisac, Neil F. Lugovoy, Vicenç Rubies-Royo, Shromona Ghosh, and Claire J. Tomlin. Bridging Hamilton-Jacobi Safety Analysis and Reinforcement Learning. *International Conference on Robotics and Automation*, 2019.

G. Frehse, C. Le Guernic, A. Donzé, S. Cotton, R. Ray, O. Lebeltel, R. Ripado, A. Girard, T. Dang, and O. Maler. SpaceEx: Scalable verification of hybrid systems. In *International Conference Computer Aided Verification*, 2011.

Antoine Girard. Reachability of uncertain linear systems using zonotopes. In *International Workshop on Hybrid Systems: Computation and Control*, pages 291–305, 2005.

Mark R. Greenstreet and Ian Mitchell. Integrating projections. In Thomas A. Henzinger and Shankar Sastry, editors, *Hybrid Systems: Computation and Control*, pages 159–174, Berlin, Heidelberg, 1998. Springer Berlin Heidelberg. ISBN 978-3-540-69754-1.

D. Henrion and M. Korda. Convex computation of the region of attraction of polynomial control systems. *IEEE Transactions on Automatic Control*, 59(2):297–312, 2014.

Alexander Kurzhanski and Pravin Varaiya. On ellipsoidal techniques for reachability analysis. part ii: Internal approximations box-valued constraints. *Optimization Methods and Software*, 17:207–237, 01 2002. doi: 10.1080/1055678021000012435.

Alexander B Kurzhanski and Pravin Varaiya. Ellipsoidal techniques for reachability analysis: internal approximation. *Systems & Control Letters*, 2000.

Albert Lin and Somil Bansal. Generating formal safety assurances for high-dimensional reachability. In *2023 IEEE International Conference on Robotics and Automation (ICRA)*, pages 10525–10531. IEEE, 2023.

John Lygeros. On reachability and minimum cost optimal control. *Automatica*, 40(6):917–927, 2004.

John N Maidens, Shahab Kaynama, Ian M Mitchell, Meeko MK Oishi, and Guy A Dumont. Lagrangian methods for approximating the viability kernel in high-dimensional systems. *Automatica*, 2013.

A. Majumdar and R. Tedrake. Funnel libraries for real-time robust feedback motion planning. *The International Journal of Robotics Research*, 36(8):947–982, 2017.

Anirudha Majumdar, Ram Vasudevan, Mark M. Tobenkin, and Russ Tedrake. Convex optimization of nonlinear feedback controllers via occupation measures. *The International Journal of Robotics Research*, 33(9):1209–1230, 2014. doi: 10.1177/0278364914528059. URL https://doi.org/10.1177/0278364914528059.

Ian Mitchell, Alex Bayen, and Claire J. Tomlin. A time-dependent Hamilton-Jacobi formulation of reachable sets for continuous dynamic games. *IEEE Transactions on Automatic Control (TAC)*, 50(7):947–957, 2005.

KN Niarchos and John Lygeros. A neural approximation to continuous time reachability computations. In *Conference on Decision and Control*, pages 6313–6318, 2006.

Petter Nilsson and Necmiye Ozay. Synthesis of separable controlled invariant sets for modular local control design. In *American Control Conference*, pages 5656–5663, 2016.

Derek Onken, Levon Nurbekyan, Xingjian Li, Samy Wu Fung, Stanley Osher, and Lars Ruthotto. A neural network approach for high-dimensional optimal control applied to multiagent path finding. *IEEE Transactions on Control Systems Technology*, 2022.

Vicenç Rubies-Royo, David Fridovich-Keil, Sylvia Herbert, and Claire J Tomlin. A classification-based approach for approximate reachability. In *International Conference on Robotics and Automation*, pages 7697–7704. IEEE, 2019.

Vladimir Vovk. Conditional validity of inductive conformal predictors. In Steven C. H. Hoi and Wray Buntine, editors, *Proceedings of the Asian Conference on Machine Learning*, volume 25 of *Proceedings of Machine Learning Research*, pages 475–490, Singapore Management University, Singapore, 04–06 Nov 2012. PMLR. URL https://proceedings.mlr.press/v25/vovk12.html.

## Appendix A. Robust Scenario-Based Proofs

First, we introduce and prove the following lemma regarding a generic 1-dimensional chance-constrained optimization problem (CCP), which will be useful for subsequent proofs.

**Lemma 7 (Solution Feasibility for a 1-D CCP)** Consider the following 1-dimensional CCP:

$$
\begin{aligned}
\text{CCP}_\epsilon: &\min_{g\in \mathbb{R}}{g} \\
&\text{s.t. } \underset{h \in H}{\mathbb{P}} \left( f(h) \le g \right) \ge 1-\epsilon
\end{aligned} \tag{7}
$$

where $g$ is the 1-dimensional optimization variable, $h$ is the uncertain parameter that describes different instances of an uncertain optimization scenario, and $f$ is some function of $h$.

The corresponding sample counterpart (SP) of this CCP is:

$$
\begin{aligned}
\text{SP}^A_{N,k}: &\min_{g \in \mathbb{R}}{g} \\
&\text{s.t. } f(h_i) \le g, \quad i \in \{1, ..., N\}-A\{h_1, ..., h_N\}
\end{aligned} \tag{8}
$$

where $N$ constraints are sampled but $k$ constraints are discarded according to some constraint elimination algorithm $A$. Let $g^{\ast}_{N,k}$ denote the solution to the above SP. Select a violation parameter $\epsilon \in (0, 1)$ and a confidence parameter $\beta \in (0, 1)$ such that

$$
\sum^k_{i=0} \binom{N}{i} \epsilon^i (1-\epsilon)^{N-i} \le \beta \tag{9}
$$

Then, with probability at least $1-\beta$, the following holds:

$$
\underset{h \in H}{\mathbb{P}} \left( f(h) > g^{\ast}_{N,k} \right) \le \epsilon \tag{10}
$$

**Proof** Lemma 7 is a straightforward application of a scenario-based sampling-and-discarding approach to a CCP as detailed in Campi and Garatti (2011). CCP (7) satisfies the assumptions of Campi and Garatti (2011), since both the domain of optimization $\mathbb{R}$ and the constraint sets parameterized by $h$, $\{g: f(h) \le g\}$, are convex and closed in $g$. Thus, Lemma 7 follows as a special case of Theorem 2.1 in Campi and Garatti (2011), where $d=1$, $c=1$, $x=g$, $X=G=\mathbb{R}$, $\delta=h$, $\Delta=H$, and $X_\delta=G_h=\{g: f(h) \le g\}$. $\blacksquare$

### A.1. Proof of Theorem 2

**Proof** Consider the chance-constrained optimization problem (CCP) (7) in Lemma 7 directly above, where $h=x$, $H=\mathcal{S}$, and $f(h)=f(x)=-J_{\tilde{\pi}}(x,0)$. The proposed robust scenario-based probabilistic safety verification method deals with the corresponding sample counterpart (SP) (8) in Lemma 7 where the constraint elimination algorithm $A$ is to remove all $k$ constraints $f(h_i) \le g$ where $f(h_i)=-J_{\tilde{\pi}}(x_i,0) \ge 0$. Thus, the only constraints remaining are $f(h_i) \le g$ where $f(h_i) < 0$. Since we are minimizing $g$, the solution $g^{\ast}_{N,k}$ to the SP must be $< 0$; i.e., $0 < -g^{\ast}_{N,k}$. Therefore, $\underset{x \in \mathcal{S}}{\mathbb{P}} ( J_{\tilde{\pi}}(x,0) \le 0 ) \le \underset{x \in \mathcal{S}}{\mathbb{P}} ( J_{\tilde{\pi}}(x,0) < -g^{\ast}_{N,k} )$. Equation (10) of Lemma 7 then yields: $\underset{x \in \mathcal{S}}{\mathbb{P}} ( J_{\tilde{\pi}}(x,0) < -g^{\ast}_{N,k} ) \le \epsilon \implies \underset{x \in \mathcal{S}}{\mathbb{P}} ( J_{\tilde{\pi}}(x,0) \le 0 ) \le \epsilon$, where $\forall (x,t), J_{\tilde{\pi}}(x,t) \le V(x, t)$ from Equation (1), so Equation (3) of Theorem 2 directly follows. $\blacksquare$

## Appendix B. Conformal Proofs

### B.1. Proof of Theorem 3

**Proof**

Theorem 3 is a straightforward application of the split conformal prediction method detailed in Angelopoulos and Bates (2023), where we set the conformal “input” $x=x$, “output” $y=-J_{\tilde{\pi}}(x,0)$, “score function” $s(x,y)=y=-J_{\tilde{\pi}}(x,0)$, “size of the calibration set” $n=N$, and “user-chosen error rate” $\alpha=\frac{k+1}{N+1}$. The conformal $\hat{q}$ is then computed as the $\frac{\lceil(N+1)(1-\alpha)\rceil}{N}$ quantile of the calibration scores $-J_{\tilde{\pi}}(x_{1:N},0)$. The quantile is $\frac{\lceil(N+1)(1-\alpha)\rceil}{N} = \frac{\lceil(N+1)(1-\frac{k+1}{N+1})\rceil}{N} = \frac{\lceil(N+1)(\frac{N-k}{N+1})\rceil}{N} = \frac{N-k}{N}$, where we have defined $k$ in the procedures in Section 4 as the number of scores $-J_{\tilde{\pi}}(x_i,0) \ge 0$. Thus, this quantile corresponds precisely to the largest *negative* score, so we know that $\hat{q} < 0$. Theorem 1 in Angelopoulos and Bates (2023) then yields:

$$
\underset{ \left( x_{1:N},x \right) \in \mathcal{S} }{\mathbb{P}} \left( -J_{\tilde{\pi}}(x,0) \le \hat{q} \right) \ge 1-\alpha
$$

$$
\underset{ \left( x_{1:N},x \right) \in \mathcal{S} }{\mathbb{P}} \left( J_{\tilde{\pi}}(x,0) \ge -\hat{q} \right) \ge 1-\frac{k + 1}{N + 1}
$$

$$
\underset{ \left( x_{1:N},x \right) \in \mathcal{S} }{\mathbb{P}} \left( J_{\tilde{\pi}}(x,0) > 0 \right) \ge \frac{N-k}{N + 1} \tag{11}
$$

where Equation (11) follows from the line preceding it because if $J_{\tilde{\pi}}(x,0) \ge -\hat{q}$, then certainly $J_{\tilde{\pi}}(x,0) > 0$. This coverage property result is precisely the same as described in Remark 4. Furthermore, Section 3.2 in Angelopoulos and Bates (2023) yields:

$$
\underset{x \in \mathcal{S}}{\mathbb{P}} \left( J_{\tilde{\pi}}(x,0) > 0 \right) \sim \text{Beta}(N + 1 - l, l),\quad l= \lfloor (N + 1)\alpha\rfloor
$$

$$
\underset{x \in \mathcal{S}}{\mathbb{P}} \left( J_{\tilde{\pi}}(x,0) > 0 \right) \sim \text{Beta}(N-k, k + 1) \tag{12}
$$

which is precisely the result of Theorem 3. $\blacksquare$

### B.2. Proof that Split Conformal Prediction Reduces to Robust Scenario Optimization

Here, we show that split conformal prediction, in full generality, reduces to a robust scenario optimization problem. We hope that this insight will encourage future research on the close relationship between the highly related but disparate fields of conformal prediction and scenario optimization. In split conformal prediction, we first define a score function $s(x,y) \in \mathbb{R}$ which is meant to reflect the uncertainty for a model input $x$ and corresponding model output $y$. Then, we sample an i.i.d. calibration set $(X_1,Y_1),...,(X_n,Y_n)$ and compute $\hat{q}$ as the $\frac{\lceil(n+1)(1-\alpha)\rceil}{n}$ quantile of the calibration scores $s(X_1,Y_1),...,s(X_n,Y_n)$, where $\alpha \in [0, 1]$ is a user-chosen error rate. For a new i.i.d. sample $X_{\text{test}}$, we construct a prediction set $C(X_{\text{test}})=\{y: s(X_{\text{test}},y) \le \hat{q}\}$. Theorem 1 in Angelopoulos and Bates (2023) provides the following coverage property: $\mathbb{P} \left( Y_{\text{test}} \in C(X_{\text{test}}) \right) \ge 1-\alpha$. This follows from the more powerful property, first introduced in Vovk (2012), which we prove reduces to a robust scenario-based result after:

$$
\mathbb{P} \left( Y_{\text{test}} \in C(X_{\text{test}}) | \{ (X_i, Y_i) \}^n_{i=1} \right) \sim \text{Beta}(n + 1 - l, l), \quad l=\lfloor (n + 1)\alpha \rfloor \tag{13}
$$

**Proof**

To show that split conformal prediction reduces to a scenario-based approach, consider the CCP (7) in Lemma 7 in Appendix A, where $h=(x,y)$ and $f(h)=f\left((x,y)\right)=s(x,y)$. That is, we want to find a probabilistic upper-bound on samples of the score function. Then, consider the corresponding SP (8) in Lemma 7 where the $n$ sampled calibration scores $s(X_1, Y_1), ..., s(X_n, Y_n)$ forms our set of constraints. Remove the $k=\lfloor (n + 1)\alpha-1 \rfloor$ largest scores, where $\alpha$ is the user-chosen error rate in split conformal prediction. The largest remaining score will be the $\frac{n-k}{n}$ quantile. $\frac{n-k}{n}=\frac{n-\lfloor (n+1)\alpha-1 \rfloor}{n}=\frac{n+\lceil -((n+1)\alpha-1) \rceil}{n}=\frac{\lceil n -(n+1)\alpha+1 \rceil}{n}=\frac{\lceil (n+1)(1-\alpha) \rceil}{n}$, which is precisely the same quantile as $\hat{q}$ in split conformal prediction. Thus, the solution to the SP is $g^{\ast}_{N,k}=\hat{q}$. Lemma 7 tells us that for a violation parameter $\epsilon \in (0, 1)$ and a confidence parameter $\beta \in (0, 1)$ that satisfies the relationship in Equation (9), with probability at least $1-\beta$, the following holds:

$$
\mathbb{P}\left( Y_{\text{test}} \in C(X_{\text{test}}) | \{ (X_i, Y_i) \}^n_{i=1} \right) \ge 1-\epsilon \tag{14}
$$

This is equivalent to Equation (13). To see why, note that the cumulative distribution function of the Beta distribution in Equation (13) is given in terms of $k$ by the incomplete beta function ratio $I_x(n-k, k + 1)=\sum^n_{j=n-k}\binom{n}{j}x^j(1-x)^{n-j}$ from DLMF, (8.17.5). Changing the index $i=n-j$ yields $I_x(n-k, k+1)=\sum^k_{i=0}\binom{n}{n-i}x^{n-i}(1-x)^{n-(n-i)}=\sum^k_{i=0}\binom{n}{i}x^{n-i}(1-x)^{i}$. Thus, Equation (13) is equivalent to the claim that for any violation parameter $\epsilon \in (0, 1)$ and confidence parameter $\beta \in (0, 1)$, $\mathbb{P}\left( Y_{\text{test}} \in C(X_{\text{test}}) | \{ (X_i, Y_i) \}^n_{i=1} \right) \ge 1-\epsilon$ (Equation (14)) holds with probability at least $1-\beta$ as long as $\beta \ge I_{1-\epsilon}(n-k, k + 1)=\sum^k_{i=0}\binom{n}{i}\epsilon^{i}(1-\epsilon)^{n-i}$ (Equation (9)). $\blacksquare$

### B.3. Proof of Lemma 5

**Proof** The conformal probabilistic safety verification method in Section 5 is nothing more than a specific formulation of the general split conformal prediction method in Appendix B.2, which we have proven provides a result that is equivalent to the robust scenario optimization result in Lemma 7. The result in Lemma 7, when formulated in the context of the conformal probabilistic safety verification method in Section 5 and noting that $\forall (x,t), J_{\tilde{\pi}}(x,t) \le V(x, t)$ from Equation (1), is precisely Lemma 5. $\blacksquare$

## Conversion notes

- Source version: arXiv:2312.08604v2 [cs.RO], 10 Apr 2024 (16 pages, single column, PMLR/L4DC style: main text on pages 1-10, acknowledgments and references on pages 11-13, Appendices A and B on pages 14-16); authors Albert Lin and Somil Bansal. The paper was published at L4DC 2024 (Proceedings of Machine Learning Research vol. 242, pp. 719-731). This package was made from the arXiv v2 PDF, not from the proceedings PDF. The first page of the arXiv PDF prints the banner 'Proceedings of Machine Learning Research vol vvv:1–16, 2024' (with the template placeholder 'vvv') and the foot line '© 2024 A. Lin & S. Bansal.'; these, the arXiv stamp, the running headers and the page numbers are page furniture and are not part of the text below.
- Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (root.tex, notation.tex, sections/*.tex), with the authors' private macros expanded to standard LaTeX, and every formula was checked against the PDF pages; the TeX source and the PDF agree and no formula is kept as an image only. Notational choices that do not change the printed symbols: the mathtools definition symbol (coloneqq, printed ':=') is written ':=', a superscript star is written with `^{\ast}`, the authors' macro for the reachable tube prints the upright word BRT and is written as plain text in prose, and percentages and plain decimal numbers in prose and captions (99.974%, 0.56, ...) are plain text.
- Numbering. The 14 printed equation numbers (1)-(14) are written with `\tag{n}`. Numbers (11) and (12) belong to the last line of a three-line and of a two-line display in Appendix B.1; these displays are written as consecutive display blocks with the tag on the last one. Theorem-like statements share one counter: Remark 1, Theorem 2, Theorem 3, Remark 4, Lemma 5, Remark 6, and Lemma 7 (in Appendix A). Their labels are printed in bold without punctuation and their bodies in italics (not reproduced). Statement ends, taken from the TeX environments: Theorem 2 ends with display (3), Theorem 3 with display (4), Lemma 5 with display (6), Lemma 7 with display (10); Remarks 1, 4 and 6 are one paragraph each. Proofs start with a bold 'Proof' and end with a filled square, written as a black square symbol.
- The main text says three times that the proofs are 'in the Appendix of the extended version of this article' with footnote mark 1 (the footnote, printed once, gives a URL). This arXiv version already contains that appendix (Appendix A: Lemma 7 and the proof of Theorem 2; Appendix B: proofs of Theorem 3, of the reduction of split conformal prediction to robust scenario optimization, and of Lemma 5). The sentences are kept verbatim; footnote 1 is placed after the Section 4 paragraph that first carries its mark.
- Figures 1-6 are image crops (assets/figure/figure-1.jpg to figure-6.jpg) with verbatim captions; Figure 1 consists of two stacked panels printed at the left of its caption and is one crop. Figure 5 is printed at the top of PDF page 10, inside a sentence of Section 6.3; here it follows the Section 6.2 paragraph that discusses it. The figures are raster images, so their labels are not searchable; values printed only inside figures: Figure 1(a) is titled with a fixed N of about 3.7M, marks 'Vol. = 0.56' (grey point) and 'Vol. = 0.81' (dashed line), and its right axis pairs log10(epsilon) with safety as -3.5 (99.968%), -4.0 (99.990%), -4.5 (99.997%), -5.0 (99.999%); Figure 2(b) labels its four points with N about 116K and k = 0, N about 368K and k = 36, N about 1.2M and k = 193, N about 3.7M and k = 731; Figure 3 is titled with N about 3.7M and k = 731 and annotated '1-epsilon = about 0.99979' and '1-beta = 0.9'; Figures 4(b), 5(b) and 6(b) mark 'Vol. = 0.782' and 'Vol. = 0.8', 'Vol. = 0.334' and 'Vol. = 0.366', and 'Vol. = 0.19' next to the dashed 99.990% safety line (in Figure 4(b) both markers and in Figure 5(b) the grey 0.334 marker lie on the line; the cyan 0.366 marker of Figure 5(b) is drawn slightly below it and the cyan 0.19 marker of Figure 6(b) clearly below it) (the figures write 'about' as a tilde, e.g. '~3.7M'; the text gives the exact N = 3684118 for the k = 731 run). The paper has no tables and no algorithm boxes.
- The text and formulas are kept as printed. The following are in the source and are not conversion errors: 'split conform prediction' (Section 5, after Lemma 5); 'HJI-VI' in Section 6.3 where Section 3.1 defines 'HJB-VI'; 'side length 20m' next to target-set bounds of 20.0 in Section 6.2; in Appendix B.2 the solution of the sample problem is written with subscript N,k although the calibration set there has size n, and the final binomial sum uses n while the Equation (9) it is identified with uses N. The bibliography is unnumbered (author-year citations, 31 entries). Reading hint: Theorem 2 and Lemma 5 state the guarantee for the true value function V (probability that V(x,0) is at most 0), whereas Theorem 3, Remark 4 and the appendix proofs work with the induced cost of the learned policy; the proofs link the two through the inequality that this cost is at most V.
