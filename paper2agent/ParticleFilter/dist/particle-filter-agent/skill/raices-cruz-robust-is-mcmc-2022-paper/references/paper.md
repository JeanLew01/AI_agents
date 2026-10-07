# Iterative importance sampling with Markov chain Monte Carlo sampling in robust Bayesian analysis

IVETTE RAICES CRUZ$^1$, JOHAN LINDSTRÖM$^2$, MATTHIAS C.M. TROFFAES$^3$, AND ULLRIKA SAHLIN$^1$

$^1$Centre for Environmental and Climate Science, Lund University, Lund, Sweden

$^2$Centre for Mathematical Sciences, Lund University, Lund, Sweden

$^3$Durham University, Department of Mathematical Sciences, UK

*E-mail addresses*: ivette.raices_cruz@cec.lu.se, johan.lindstrom@matstat.lu.se, matthias.troffaes@durham.ac.uk, ullrika.sahlin@cec.lu.se.

*Key words and phrases.* bounds on probability; effective sample size; meta-analysis; random effects model; uncertainty quantification.

**Abstract.** Bayesian inference under a set of priors, called robust Bayesian analysis, allows for estimation of parameters within a model and quantification of epistemic uncertainty in quantities of interest by bounded (or imprecise) probability. Iterative importance sampling can be used to estimate bounds on the quantity of interest by optimizing over the set of priors. A method for iterative importance sampling when the robust Bayesian inference rely on Markov chain Monte Carlo (MCMC) sampling is proposed. To accommodate the MCMC sampling in iterative importance sampling, a new expression for the effective sample size of the importance sampling is derived, which accounts for the correlation in the MCMC samples. To illustrate the proposed method for robust Bayesian analysis, iterative importance sampling with MCMC sampling is applied to estimate the lower bound of the overall effect in a previously published meta-analysis with a random effects model. The performance of the method compared to a grid search method and under different degrees of prior-data conflict is also explored.

## 1. Introduction

Bayesian analysis quantifies uncertainty by precise probability derived from a prior (subjective) distribution for parameters and a likelihood for data given parameters [15]. Whereas statistical Bayesian inference usually uses non-informative priors as default, there are exceptions motivating the use of informative priors to reduce complexity [39]. In a decision context where one wants to use the best possible knowledge, informative priors are useful, or even needed, to integrate data with expert knowledge. Specifying a precise informative prior may be difficult, in particular for a model with many parameters or when experts disagree [35, 23].

Robust Bayesian analysis is a way to consider the impact of the choice of prior on uncertainty in relevant quantities. The impact of different priors in Bayesian inference is important to evaluate for two reasons. First, it is common that more than one prior probability distribution could reasonably be chosen for the problem at hand. Second, when information in data is weak (e.g. for small sample sizes), the choice of prior could matter a lot for the final outcome of an analysis. Robust Bayesian analysis has been used for sensitivity analysis towards the choice of prior [2].

A type of robust Bayesian analysis is to use sets of prior distributions or sets of likelihoods resulting in sets of posterior distributions. This can be seen as an extension of Bayesian inference which quantifies uncertainty by bounded (imprecise) probability instead of precise probability [45]. In robust Bayesian analysis, one is often interested in estimating bounds on expectation. For instance, the lower bound on expectation of a function $f$ with respect to a set of posterior distributions, $\mathcal{M}$, is expressed as

$$
\underline{\mathrm{E}}(f) := \inf_{p \in \mathcal{M}} \int f(x)p(x)dx. \tag{1}
$$

Note that a set of posterior distributions is derived from a set of prior distributions.

Robust Bayesian analysis using sets of priors has been developed in a closed analytic form for conjugate models [3, 34, 46]. In [47], a range of posterior expectations are computed using a Monte Carlo method when considering uncertainty regarding the prior or likelihood.

Importance sampling has also been used to estimate bounds on expectations using independent samples drawn from arbitrary (e.g. not necessarily conjugate) models, as long as the posterior can be analytically evaluated up to a normalization constant [14, 41, 42, 43]. In an iterative version of importance sampling, it has been suggested to iteratively change the sampling (also called proposal) distribution of importance sampling, in order to get an effective sample size (i.e. a measure of efficiency) as close as possible to the actual sample size [41, 42]. A small effective sample size means that the weights of importance sampling are too imbalanced and thus might be unreliable.

In [42], it is also suggested to use the posterior distribution directly as a sampling distribution where possible. The use of the posterior allows, in theory, for the effective sample size to be maximized across iterations. For this reason, the effective sample size of the importance sampling estimator is used as the stopping criterion of iterative importance sampling in [42]. However, the effective sample size can be very poor if the sampling distribution is not carefully chosen, i.e. if the initial choice of posterior is far from the posterior that, say, minimizes the expectation of the quantity of interest. Further, the method can have issues with convergence across iterations as a result. The required number of samples for accurate estimation using importance sampling has also been discussed in [1, 7, 37] by means of the Kullback Leibler divergence.

Markov chain Monte Carlo (MCMC) sampling is a method for Bayesian inference which does not require a closed form of the posterior [6, 15]. MCMC sampling allows for inference of simple as well as complex models. So far, few robust Bayesian analysis have used MCMC sampling (see [44] for an example). This is mainly due to limitations in existing methods, such as requirements on knowing the analytical form of the posteriors. The inability to use MCMC sampling severely restricts the use of robust Bayesian analysis on more complex models.

To use iterative importance sampling with MCMC samples there is a need to modify the effective sample size that is used in the stopping criterion in iterative importance sampling. In this paper, we combine iterative importance sampling with MCMC sampling by extending the method from [41, 42] to a wider range of models, specifically those requiring MCMC sampling. To accomplish this, we derive an expression for the effective sample size which accounts for correlated MCMC samples.

In [26], an efficient importance sampling is proposed for improving a MCMC algorithm. The efficient importance sampling consists of selecting a proposal distribution (given a density kernel) using a least squares problem and then using the proposed distribution in an independent Metropolis Hasting sampling. Moreover, in [29], a layered adaptive importance sampling algorithm is presented which combined MCMC algorithms with importance sampling and different strategies to re-use generated samples. The layered adaptive importance sampling algorithm generates samples using two layers. The upper layer generates samples using a MCMC algorithm which are later used in a multiple importance sampling scheme (lower layer) [29]. A recycling layered adaptive importance sampling scheme is presented which re-uses the samples from the upper layer in the lower layer [29]. This scheme is similar to the method proposed in this paper. However, a key difference between the [26] and [29] papers and this paper is that we re-use the MCMC samples from one run by weighting with a different prior, and that we use an efficient sample size for determining when to re-run the MCMC sampler, which leads to fewer MCMC runs to cover the hyperparameter space.

A robust Bayesian analysis allows for a quantification of uncertainty in quantities of interest which is robust to the choice of prior. It can also be useful for Bayesian inference when priors are given as sets. To demonstrate the proposed method, iterative importance sampling with MCMC sampling is applied to estimate the lower bound of the overall effect of biomanipulation of freshwater lakes in an already published meta-analysis [4].

## 2. Importance sampling

Recall that the expectation of a function $f$ with respect to a *target distribution*, $p$ is given by

$$
\mu := \mathrm{E}_p \Bigl(f(x)\Bigr) = \int f(x)p(x)dx, \tag{2}
$$

which can be approximated by the standard Monte Carlo estimator of $\mathrm{E}_p \Bigl(f(x)\Bigr)$ as

$$
\overline{\mu} := \frac{1}{N}\sum_{i=1}^N f(X_i), \tag{3}
$$

where $X_i \sim p$ are independent and identically distributed (i.i.d) samples.

Sometimes, it is difficult to draw samples directly from $p$ or there is a mismatch between $f(x)$ and $p(x)$ [33]. In this case, importance sampling could be applied to estimate the expectation by weighting samples drawn from a *sampling distribution*, $q$, from which it is easier to generate samples [11]. This technique has been applied in Bayesian inference [15] and in numerical integration [28, 33].

The sampling density function $q$ must be such that $q(x) > 0$ whenever $p(x)f(x) \neq 0$. Sometimes $p$ is only known up to a normalization constant, say only $p_u = cp$ is known, where $c > 0$ is an unknown constant. The expectation of $f$ with respect to $p$ can be written as

$$
\mu := \mathrm{E}_p\Bigl(f (x)\Bigr) = \frac{\displaystyle \int f(x)p_u(x) dx}{\displaystyle \int p_u(x) dx} = \frac{\displaystyle \int f(x) w_p(x) q(x) dx}{\displaystyle \int w_p(x)q(x) dx} = \frac{\mathrm{E}_q\Bigl(f(x)w_p(x)\Bigr)}{\mathrm{E}_q\Bigl(w_p(x)\Bigr)}, \tag{4}
$$

where $w_p(x) := \frac{p_u(x)}{q(x)}$.

This expectation can be estimated by *self-normalized importance sampling*, which is defined as

$$
\widetilde{\mu} := \frac{\sum_{i=1}^N f(X_i)w_p(X_i)}{\sum_{i=1}^N w_p(X_i)} \qquad\text{where }X_i\sim q \text{ (i.i.d)}. \tag{5}
$$

In the following, we shall relax the assumption of independence. At this point, it suffices to point out that eq. (5) is still a valid estimator of $\mathrm{E}_p \Bigl(f(x) \Bigr)$ even if the $X_i$ are dependent.

A measure to assess the quality of the importance sampling estimator is the effective sample size, $\mathrm{ESS}$. It is defined by [24], as the ratio of the variances of $\overline{\mu}$ and $\widetilde{\mu}$ estimators, in eq. (3) and eq. (5), scaled to N:

$$
\mathrm{ESS} := \frac{N\mathrm{Var}_p(\overline{\mu})}{\mathrm{Var}_q(\widetilde{\mu})}. \tag{6}
$$

The effective sample size represents the number of standard Monte Carlo samples that are needed for both estimators to have the same variance.

If the samples $X_i$ from $q$ are i.i.d. then $\mathrm{ESS}$ can be estimated by

$$
\mathrm{ESS_{IS}} := \frac{(\sum_{i=1}^N w_p(X_i))^2}{\sum_{i=1}^N w^2_p(X_i)}, \tag{7}
$$

see [33]. However, this formula is not applicable for correlated samples, as would be the case if the $X_i$ are sampled from $q$ using an MCMC algorithm.

## 3. Effective sample size of importance sampling using MCMC

Here, we want to derive an estimate of the effective sample size as defined in eq. (6) when the $X_i$ are sampled from $q$ through MCMC. First, we derive an approximation of $\mathrm{Var}_q(\widetilde{\mu})$.

Importance sampling with MCMC was introduced by [21] for variance reduction [5]. Hastings [21] suggested the following approximate of the denominator in eq. (6):

$$
\mathrm{Var}_q \left(\widetilde{\mu}\right) = \mathrm{Var}_q\left( \frac{\overline{Y}}{\overline{Z}} \right) \approx \frac{\mathrm{Var}_q(\overline{Y}-\mu\overline{Z})}{\Bigl(\mathrm{E}_q(\overline{Z})\Bigr)^2}, \tag{8}
$$

where

$$
\overline{Y} := \frac{1}{N}\sum_{i=1}^N f(X_i)w_p(X_i), \tag{9}
$$

$$
\overline{Z} := \frac{1}{N}\sum_{i=1}^N w_p(X_i), \tag{10}
$$

and $\mu := \mathrm{E}_p\Bigl(f(x)\Bigr)$ as defined earlier.

First, let us evaluate the denominator in eq. (8). Note that

$$
\mathrm{E}_q\Bigl(w_p(X_i)\Bigr) = \int w_p(x)q(x)dx = \int \frac{c p(x)}{q(x)}q(x)dx = c, \tag{11}
$$

so $\mathrm{E}_q(\overline{Z})=c$, and we can approximate the denominator via

$$
\Bigl(\mathrm{E}_q(\overline{Z})\Bigr)^2 \approx \left(\frac{1}{N}\sum_{i=1}^N w_p(X_i)\right)^2. \tag{12}
$$

The numerator in eq. (8) is more tricky. Let

$$
g(X_i) := (f(X_i)-\mu) w_p(X_i). \tag{13}
$$

With this notation, we get

$$
\mathrm{Var}_q(\overline{Y}-\mu\overline{Z}) = \frac{1}{N^2} \left( \sum_{i = 1}^N \mathrm{Var}_q\Bigl(g(X_i)\Bigr) + 2 \sum_{i < j} \mathrm{Cov}_q \Bigl(g(X_i), g(X_j) \Bigr) \right). \tag{14}
$$

If the variables $X_i$ form a stationary stochastic process, as in a converged MCMC algorithm, then $\mathrm{Var}_q \Bigl(g(X_i)\Bigr)$ and $\mathrm{Cov}_q\Bigl(g(X_i), g(X_{i+k})\Bigr)$ depend only on $k$ and not $i$. Hence, with $X := X_1$,

$$
\mathrm{Var}_q(\overline{Y}-\mu\overline{Z}) = \mathrm{Var}_q\Bigl(g(X)\Bigr) \left( \frac{1 + 2 \sum_{k=1}^{N-k} \rho_{g}(k)}{N} \right), \tag{15}
$$

where $\rho_{g}$ is the autocorrelation function of the stationary process. According to [16], for large $N$, the variance is approximately

$$
\mathrm{Var}_q(\overline{Y}-\mu\overline{Z}) \approx \mathrm{Var}_q\Bigl(g(X)\Bigr) \left( \frac{1 + 2 \sum_{k=1}^\infty \rho_{g}(k)}{N} \right). \tag{16}
$$

If $\sum_{k=1}^\infty \rho_{g}(k)$ converges, then a standard approximation is [16, 17]

$$
\sum_{k=1}^\infty \rho_{g}(k)\approx \sum_{k=1}^\ell \hat{\rho}_{g}(k), \tag{17}
$$

where $\ell$ is the first index for which $\hat{\rho}_{g}(\ell+1)<0$, and where $\hat{\rho}_g$ is the empirical autocorrelation function of the sample $g(X_1)$, $\dots$, $g(X_N)$. Note that evaluating $g$ requires knowledge of $\mu$ which is precisely the quantity we wish to estimate. So, instead we will use

$$
\tilde{g}(X_i) := (f(X_i) - \widetilde{\mu})w_p(X_i), \tag{18}
$$

as an approximation for $g(X_i)$, and therefore use

$$
\sum_{k=1}^\infty \rho_{g}(k)\approx \sum_{k=1}^\ell \hat{\rho}_{\tilde{g}}(k). \tag{19}
$$

We now estimate $\mathrm{Var}_q\Bigl(g(X)\Bigr)$ in eq. (16). Using eq. (13), we also get that

$$
\begin{aligned}
\mathrm{Var}_q\Bigl(g(X)\Bigr) &= \mathrm{Var}_q\Bigl(f(X) w_p(X) \Bigr) - 2 \mu \mathrm{Cov}_q \Bigl(f(X) w_p(X) , w_p(X)\Bigr) \\
&\qquad + \mu^2 \mathrm{Var}_q \Bigl(w_p(X)\Bigr).
\end{aligned} \tag{20}
$$

Now, following the same ideas as in [12][p. 5-6] (see A for details) we get

$$
\mathrm{Var}_q\Bigl(g(X)\Bigr) \approx N \mathrm{Var}_p(\overline{\mu})\left(\frac{1}{N}\sum_{i=1}^N w_p^2(X_i)\right). \tag{21}
$$

Putting everything together, we get

$$
\mathrm{Var}_q(\widetilde{\mu}) \approx N \mathrm{Var}_p(\overline{\mu}) \frac{\frac{1}{N}\sum_{i=1}^N w_p^2(X_i)}{\left(\frac{1}{N}\sum_{i=1}^N w_p(X_i)\right)^2} \left( \frac{1 + 2\sum_{k=1}^\ell \hat{\rho}_{\tilde{g}}(k)}{N} \right), \tag{22}
$$

$$
\phantom{\mathrm{Var}_q(\widetilde{\mu})} = \frac{N^2\mathrm{Var}_p(\overline{\mu})}{\mathrm{ESS_{IS}} \cdot \mathrm{ESS_{MCMC}}}, \tag{23}
$$

where $\mathrm{ESS_{IS}}$ is the standard estimate of the effective sample size for importance sampling with independent samples, eq. (7), and $\mathrm{ESS_{MCMC}}$ is the MCMC effective sample size (for $\tilde{g}$),

$$
\mathrm{ESS_{MCMC}} := \frac{N}{1 + 2\sum_{k=1}^\ell \hat{\rho}_{\tilde{g}}(k)}.
$$

Substituting eq. (23) into eq. (6), we finally obtain the following estimate for the combined $\mathrm{ESS}$

$$
\mathrm{ESS} \approx \frac{\mathrm{ESS_{MCMC}}}{N} \cdot \mathrm{ESS_{IS}}. \tag{24}
$$

So, what is new in eq. (24) with respect to eq. (7) is the factor $\frac{\mathrm{ESS_{MCMC}}}{N}$ which accounts for a reduction in effective sample size due to the correlation of the MCMC samples (a reduction since it is very unlikely that the correlation will be negative).

## 4. Importance sampling over a set of probability distributions

Let $\mathcal{M} \subset \mathbb{R}^d$ be a compact set and $p_t(\cdot) = \{p(\cdot|t)| t \in \mathcal{M}\}$ be a probability density function parameterized by $t$ (i.e. hyperparameters). The lower expectation of a function $f$ with respect to $p_t$ for all $t \in \mathcal{M}$ is assumed to exist and is estimated by

$$
\underline{\mathrm{E}}(f) := \min_{t \in \mathcal{M}} \int f(x)p_t(x) dx. \tag{25}
$$

In practice, one can search for the minimum using numerical methods. For instance, an iterative version of standard importance sampling has been used to estimate bounds on expectations in robust Bayesian analysis [14, 41, 42, 43].

Using importance sampling, the lower expectation is estimated by

$$
\underline{\widehat{\mathrm{E}}}(f) \approx \min_{t \in \mathcal{M}} \frac{\sum_{i=1}^N f(X_i)w_t(X_i)}{\sum_{i=1}^N w_t(X_i)}, \tag{26}
$$

where $w_t(x) := \frac{c p_t(x)}{q(x)}$.

Iterative importance sampling estimates the lower expectation of a function $f$ by moving the sampling distribution, $q$, towards the optimal distribution [14, 41]. The stopping criterion is that the effective sample size of importance sampling should be close enough to the desired independent sample size (denoted by $\mathrm{ESS_{target}}$) that is fixed in advance. In this paper, we adapt iterative importance sampling introduced in [14, 41, 42]. Our contribution is the effective sample size of importance sampling with correlated MCMC samples which allows us to combine iterative importance sampling with MCMC sampling, thus allowing for robust analysis of more complex models. It is important to highlight that how large the sample size for MCMC samples should be and $\mathrm{ESS_{target}}$ in step 2 and step 4 respectively, are values fixed in advance (i.e. they are inputs to the procedure). The method goes as follows:

**Step 1:** Set $t = t^0$ where $t^0$ is an initial value in the feasible region.

**Step 2:** Generate samples from $q(x) = p_t(x)$ using MCMC sampling until the effective sample size for the MCMC sample is large enough (i.e. exceed a specified threshold).

**Step 3:** Find $t_* = \arg \min_{t \in \mathcal{M}} \frac{\sum_{i=1}^N f(X_i)w_t(X_i)}{\sum_{i=1}^N w_t(X_i)}$ using an optimization algorithm.

**Step 4:** If $\mathrm{ESS} > \mathrm{ESS_{target}}$, or maximum number of iterations reached, then stop.

**Step 5:** Set $t = t_*$ and go to Step 2.

The convergence of the method depends on the distributions and the parameter space. We have set a maximum number of iterations (i.e. in our case, 10 000) to stop the algorithm when it does not converge.

The condition of a large enough sample size is added in Step 2 to ensure that the optimization in Step 3 is based on a reliable sample. For example, in the application below, we first specify the $\mathrm{ESS_{target}}$ and then we require the effective sample size for the MCMC samples to be 20% greater than the $\mathrm{ESS_{target}}$. The stopping criterion in Step 4 uses the effective sample size for importance sampling with correlated samples eq. (24), controlling for both convergence of the MCMC and quality of importance sampling. The reason for this stopping criterion is that MCMC sampling might require different numbers of iteration to produce a reasonable number of efficient samples.

Thinning chains in MCMC has been used in several papers; see for instance [8, 13, 25]. Thinning consists of taking every k-th sample instead of all of them in order to reduce autocorrelation. In [27] it is shown that although thinning chains in MCMC reduces autocorrelation between MCMC samples, it also reduces the precision of the estimates (i.e. the average over a thinned sample set has greater variance than the average over the unthinned sample) [16]. Therefore, thinning is not advisable unless it is needed due to computer memory limitations [27].

## 5. An application

To illustrate the proposed method for robust Bayesian analysis, iterative importance sampling with MCMC sampling is applied on a previously published meta-analysis investigating the effect of biomanipulation (the intervention) on water quality in freshwater lakes [4]. We selected the random effects model (described below) for the meta-analysis of the change in the level of *Chlorophyll a* before and during biomanipulation [4]. Available data are estimated mean differences and estimation errors from 75 studies. The estimated effects range from -24.17 to 332.50 $\mu g/l$ with a sample mean of 28.46 $\mu g/l$. The 5th and 95th percentile of the data are -11.10 and 76.29 $\mu g/l$ respectively. Here, a positive value corresponds to an improvement in water quality by biomanipulation (since we have turned the sign of the data). In addition, we investigate what happens with the performance of the suggested method when the set of priors is changed from a set with low to high prior-data conflict.

### 5.1. A Bayesian Linear Random Effects Model

The overall effect of the intervention $\mu$ is estimated by a linear random effects model (Figure 1) according to

$$
y_i | \delta_i \sim N(\delta_i, \sigma_i^2), \tag{27}
$$

$$
\delta_i | \mu, k, \tau_{\mu} \sim N(\mu, k^2 \, \tau_{\mu}^2), \tag{28}
$$

where $y_i$ is the observed intervention effect in study $i$ ($i = 1, \dots, N$) with known within-study variance $\sigma_i^2$, $\delta_i$ is the specific intervention effect in study $i$, and $k^2 \, \tau_{\mu}^2$ is the between-study variance. This model can be expressed in its marginal form [15, 36] as

$$
y_i | \mu, k, \tau_{\mu} \sim N(\mu, \sigma_i^2 + k^2 \, \tau_{\mu}^2). \tag{29}
$$

To implement this model in a Bayesian framework, we select the following prior distributions for the parameters

$$
\mu | \tau_{\mu} \sim N(\mu_0,\tau_{\mu}^2), \tag{30}
$$

$$
\tau_{\mu} \sim U(\tau_l,\tau_0), \tag{31}
$$

$$
k \sim U(k_l, k_u), \tag{32}
$$

where $\mu_0$ is the mean of the overall intervention effect, $\tau_{\mu}$ is the standard deviation of the overall intervention effect which ranges between $\tau_l$ and $\tau_0$, $k$ is a proportionality constant which ranges between $k_l$ and $k_u$. We let $\tau_l = 1$, $k_l = 1$ and $k_u = 5$.

The linear random effects model is implemented using MCMC sampling in Stan through the *rstan* package, the R interface to Stan [40] (see supplementary material for Stan code).

[Figure 1](../assets/figure/figure-1.jpg)

Figure 1. Linear random effects graphical model. Unknown quantities (parameters) are represented by ellipses, known quantities (priors) by circles and observed data by filled squares. The plate indicates repeated cases.

### 5.2. Selecting a set of priors

To expand the linear random effects model into a robust Bayesian framework, we consider a set of prior distributions for $\mu$ and $\tau_\mu$.

There are several methods to elicit priors from experts [32, 19, 20, 18], but there is no obvious alternative to specify a set of priors. The approach that we use to specify a set of priors for multiple parameters is chosen to illustrate robust Bayesian analysis with IIS and MCMC sampling, and other approaches could have been used as well. The prior distributions for each parameter are assumed to belong to the same family of probability distributions (eq. 30 and eq. 31), but with different hyperparameters. In order to consider interaction between parameters, the specification of priors is made using an approach similar to prior predictive check [9, 38]. A compact set of hyperparameters is selected by comparing the distribution of the intervention effect for a random study conditional on the hyperparameters $\delta^*|\mu,\tau_{\mu}$ to an elicited range $R$.

The selection of a set of priors can be summarized as:

(1) Specify a range $R$ where the effect size of a randomly selected study is expected to fall with a probability of at least h% (i.e. target coverage).

(2) Specify a regular grid of hyperparameters $(\mu_0, \tau_0)$.

(3) For each combination of hyperparameters $(\mu_0, \tau_0)$, generate a random sample $\delta^*_1, \dots, \delta^*_M$ from eq. (28).

(4) Identify hyperparameters where the proportion of generated samples falling inside $R$ exceeds the target coverage $h$.

(5) Find a function that discriminates hyperparameters complying with the target coverage and use the function to select a compact set of hyperparameters.

[Figure 2](../assets/figure/figure-2.jpg)

Figure 2. Prior check. Selection of priors, a curve fitted to the area where more than 90% of the generated specific intervention effect fell inside of the elicited range.

Here, we select two sets of priors that represent situations with a low and high prior-data conflict, respectively. In actual applications, priors should be elicited by structured expert judgement [32].

A set of priors that represents a situation with low prior-data conflict is derived using an elicited range of specific intervention effect of $R = [-20,80]$, a target coverage of 90%, and a regular grid of $200 \times 200$ of hyperparameters ($-100 \leq \mu_0 \leq 100$ and $5 \leq \tau_0 \leq 50)$. Following the procedure described above yields to the set

$$
\mathcal{M} = \left\{\begin{array}{c}
-8 \leq \mu_0 \leq 68 \\
5 \leq \tau_0 \leq 16 \\
r(\mu_0,\tau_0) - 0.9 \geq 0
\end{array} \right\},
$$

where $r(\mu_0,\tau_0) = \tau_0 - (-0.01 \mu_0^2 + 0.46 \mu_0 + 9.56)$ is a function used to capture hyperparameters fulfilling the target coverage (Figure 2).

### 5.3. Setting up the iterative importance sampling

The quantity of interest is the expected value of the overall intervention effect ($\mu$) on the linear random effects model given in section 5.1. Iterative importance sampling is applied to estimate the lower bound of the quantity of interest over the compact domain of priors $\mathcal{M}$ (see C for the proof of the existence of the minimum in our example). The lower bound of $\mu$ is

$$
\underline{\widehat{\mathrm{E}}}(\mu|\mathbf{y}, \mu_0, \tau_0) \approx \min_{(\mu_0, \tau_0) \in \mathcal{M}} \frac{\sum_{i = 1}^N \mu^{(i)} w(X^{(i)}; \mu_0, \tau_0)}{\sum_{i = 1}^N w(X^{(i)}; \mu_0, \tau_0)}, \tag{33}
$$

where $X^{(i)} = \left\{ \mu^{(i)}, k^{(i)}, \tau_\mu^{(i)} \right\}$ and $\mu^{(i)}$ are samples drawn from a sampling distribution using MCMC based on hyperparameters $\mu_0^\prime$ and $\tau_0^\prime$. The weights are given by

$$
w(X^{(i)}; \mu_0, \tau_0) = \frac{p(\mu^{(i)}, k^{(i)}, \tau_\mu^{(i)}| \mathbf{y}, \mu_0, \tau_0)}{p(\mu^{(i)}, k^{(i)}, \tau_\mu^{(i)}| \mathbf{y}, \mu_0^\prime, \tau_0^\prime)}, \tag{34}
$$

where $p(\mu, k, \tau_\mu| \mathbf{y}, \mu_0, \tau_0)$ is the posterior distribution of the target distribution corresponding to hyperparameters $\mu_0$ and $\tau_0$.

[Figure 3](../assets/figure/figure-3.jpg)

Figure 3. From left, effective sample sizes $\mathrm{ESS}$, $\mathrm{ESS_{IS}}$ and $\mathrm{ESS_{MCMC}}$ given MCMC samples using hyperparameters $\mu_0 = 5$ and $\tau_0 = 7$ (the dot). Here, $\mathrm{ESS_{target}}$ is 5 000 and if the optimization in Step 3 moves the hyperparameters into a region with a lower $\mathrm{ESS}$ we need to re-run the MCMC in Step 2, using the ‘new’ hyperparameters.

Using eq. (34) as weights in eq. (24) gives the effective sample size of importance sampling with MCMC samples. The search for the lower bound in Step 3 will stop when the optimal prior is close to the prior used in the MCMC (Figure 3). How close is determined by the assigned $\mathrm{ESS_{target}}$ in Step 4, which in our example is set to 5 000 and 10 000 samples. The effective sample size for the MCMC samples in Step 2 is set to exceed $\mathrm{ESS_{target}}$ by at least 20%, i.e. MCMC sampling in Step 2 will be run until an effective sample size of 6 000 and 12 000 samples has been reached.

The optimization in Step 3 is performed by simulated annealing, [10, 22], using the *optim* function from the *optimx* package [31] in R.

### 5.4. The lower bound of the expected overall effect

We illustrate the method using two different $\mathrm{ESS_{target}}$ and two choices of initial values $(\mu_0^\prime = -7$, $\tau_0^\prime = 6)$ and $(\mu_0^\prime = 10$, $\tau_0^\prime = 10)$. The number of iterations of iterative importance sampling ranges between 2 and 3 with an effective sample size between 11 640 and 14 305, see (Table 1, 2 and 3). Note that the effective samples size for the MCMC sample is derived based on the hyperparameters in the previous iteration.

The estimated lower bound on the expected overall effect over $\mathcal{M}$ is 12.1 $\mu g/l$ (Table 1, 2 and 3). We also run the method using different random seeds which gives an estimated lower bound on the expected overall effect between 12.07 and 12.24 $\mu g/l$. The bound is lower than 19.9 which is the estimated effect in a standard Bayesian analysis using a flat prior centered at zero ($\mu_0 = 0$ and $\tau_0 = 1~000$). The lower bound is obtained at the corner of the prior region (i.e. $\mu_0 = -8$ and $\tau_0 = 5$). The bound obtained by iterative importance sampling is compared to one estimated by a grid search method across a regular grid of hyperparameters (which yields a total of 4 773 hyperparameter values). The grid search method gives a lower expected bound of 12.09 $\mu g/l$ which is close to the one found using iterative importance sampling. It takes much longer time to run a grid search method, over 10 hours, compared to the iterative importance sampling taking roughly 15 to 25 minutes (Table 1, 2 and 3).

Moreover, we run the optimization algorithm (simulated annealing) over the set $\mathcal{M}$, but without the resampling step, (e.g. just re-run the MCMC for each parameter that is evaluated). The method gives a lower bound of 12.13 $\mu g/l$ and it takes much longer time to run, over 20 hours.

The iterative importance sampling converges with fewer iterations when the initial values are relative close to the hyperparameters corresponding to the lower bound.

Table 1. Summary of iterative importance sampling (IIS) of the lower expected value over the set $\mathcal{M}$, $\mathrm{ESS_{target}}$ = 5 000 and initial values $(\mu_0; \tau_0) = (-7; 6)$.

[Table 1](../assets/table/table-1.csv)

|  | Iter | Samples | μ0* | τ0* | ESS | ESS_MCMC | ESS_IS | μ̂(μ0*, τ0*) | Time |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Grid Search | – | 20 000 | -8 | 5 | – | – | – | 12.091 | 11.45 h |
| IIS | 0 | – | -7 | 6 | – | – | – | – | – |
| IIS | 1 | 20 000 | -7.706 | 5.051 | 27 | 18 005 | 30 | 10.988 | – |
| IIS | 2 | 20 000 | -7.999 | 5.045 | 11 640 | 12 307 | 18 916 | 12.166 | 11.78 mins |

Table 2. Summary of iterative importance sampling (IIS) of the lower expected value over the set $\mathcal{M}$ and $\mathrm{ESS_{target}}$ = 10 000 and initial values $(\mu_0; \tau_0) = (-7; 6)$.

[Table 2](../assets/table/table-2.csv)

|  | Iter | Samples | μ0* | τ0* | ESS | ESS_MCMC | ESS_IS | μ̂(μ0*, τ0*) | Time |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Grid Search | – | 20 000 | -8 | 5 | – | – | – | 12.091 | 11.45 h |
| IIS | 0 | – | -7 | 6 | – | – | – | – | – |
| IIS | 1 | 40 000 | -7.900 | 5.035 | 59 | 31 579 | 75 | 12.006 | – |
| IIS | 2 | 20 000 | -7.998 | 5.136 | 13 899 | 13 901 | 19 997 | 12.135 | 18.73 mins |

Table 3. Summary of iterative importance sampling (IIS) of the lower expected value over the set $\mathcal{M}$ and $\mathrm{ESS_{target}}$ = 10 000 and initial values $(\mu_0; \tau_0) = (10; 10)$.

[Table 3](../assets/table/table-3.csv)

|  | Iter | Samples | μ0* | τ0* | ESS | ESS_MCMC | ESS_IS | μ̂(μ0*, τ0*) | Time |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Grid Search | – | 20 000 | -8 | 5 | – | – | – | 12.091 | 11.45 h |
| IIS | 0 | – | 10 | 10 | – | – | – | – | – |
| IIS | 1 | 40 000 | -6.734 | 5.148 | 5 | 40 000 | 5 | 12.762 | – |
| IIS | 2 | 20 000 | -7.993 | 5.008 | 3 995 | 13 907 | 5 746 | 12.145 | – |
| IIS | 3 | 20 000 | -7.995 | 5.221 | 14 305 | 14 305 | 20 000 | 12.103 | 23.72 mins |

Transcription note (column headers of Tables 1, 2 and 3 as printed): Iter, Samples, $\mu_{0_*}$, $\tau_{0_*}$, $\mathrm{ESS}$, $\mathrm{ESS_{MCMC}}$, $\mathrm{ESS_{IS}}$, $\hat{\mu}_{(\mu_{0_*}, \tau_{0_*})}$, Time. The first column holds the row-group labels **Grid Search** and **IIS**.

### 5.5. The influence of prior data conflict

In order to illustrate what happens when the set of prior has a high conflict with data, we specify a new set $\mathcal{M}'$ using the procedure described in subsection 5.2, but with $R = [30, 100]$. This range does not include the median (14.6 $\mu g/l$) of the observed effects in the 75 studies or the posterior mean from a standard Bayesian analysis with a flat prior. This gives the set

$$
\mathcal{M}' = \left\{\begin{array}{c}
42 \leq \mu_0 \leq 88 \\
5 \leq \tau_0 \leq 11 \\
r'(\mu_0,\tau_0) - 0.90 \geq 0
\end{array}\right\},
$$

where $r'(\mu_0,\tau_0) = \tau_0 - (-0.011 \mu_0^2 + 1.427 \mu_0 - 35.104)$.

Shifting the prior region from $\mathcal{M}$ to $\mathcal{M}'$, (i.e. towards higher values of $\mu$), increases the lower bound of the expected overall effect from 12.1 to 26.8 $\mu g/l$, (Table 4). The lower bound is in this case obtained for a less precise prior $\tau_0 = 10.5$.

We also compare the bound obtained by iterative importance sampling to the one estimated by a grid search method across a regular grid of hyperparameters (which yields a total of 1 649 hyperparameter values). The grid search method gives a slightly lower expected bound of 26.7 $\mu g/l$, but takes much longer time, 4 hours, compared to 13 minutes for the iterative importance sampling (Table 4).

Table 4. Summary of iterative importance sampling of the lower expected values over the set $\mathcal{M}'$ and $\mathrm{ESS_{target}}$ = 10 000 and initial values $(\mu_0; \tau_0) = (60; 11)$.

[Table 4](../assets/table/table-4.csv)

|  | Iter | Samples | μ0* | τ0* | ESS | ESS_MCMC | ESS_IS | μ̂(μ0*, τ0*) | Time |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Grid Search | – | 20 000 | 57 | 10.5 | – | – | – | 26.754 | 3.70 h |
| IIS | 0 | – | 60 | 11 | – | – | – | – | – |
| IIS | 1 | 40 000 | 59.064 | 10.859 | 15 371 | 17 533 | 35 067 | 26.811 | 12.5 mins |

Transcription note (column headers of Table 4 as printed): Iter, Samples, $\mu_{0_*}$, $\tau_{0_*}$, $\mathrm{ESS}$, $\mathrm{ESS_{MCMC}}$, $\mathrm{ESS_{IS}}$, $\hat{\mu}_{(\mu_{0_*}, \tau_{0_*})}$, Time. The first column holds the row-group labels **Grid Search** and **IIS**.

## 6. Conclusions

Robust Bayesian analysis (i.e. Bayesian inference under a set of priors) offers a way to quantify epistemic uncertainty by bounded instead of precise probability. This type of analysis is useful for evaluating sensitivity to the choice of prior. It is also a solution for Bayesian inference when prior information is upfront given as a set of distributions.

We have derived an expression for the effective sample size of importance sampling with correlated MCMC samples, which ensures reliable samples from both MCMC and importance sampling procedures when combining them. The combination of iterative importance sampling with MCMC sampling was used for robust Bayesian analysis on an existing meta-analysis based on a random effects model [4]. The estimated lower bound on the expected overall effect of the intervention in the meta-analysis is a conservative estimate compared to what would have been the result from selecting one prior in the set and using a standard Bayesian analysis.

Iterative importance sampling with MCMC sampling allows for robust Bayesian analysis on a wider range of models not limited to conjugate models. The flexibility in the choice of model may allow for more applications of robust Bayesian analysis. The method was demonstrated on a relatively simple model with two different choices of prior sets. It would be useful to evaluate the proposed method on more complex models to further explore the theoretical and practical challenges associated with robust Bayesian analysis; as well as to investigate how other discrepancy measures such as those proposed by [30] and the Kullback-Leibler (KL) divergence measure could be used.

## Supplementary material

The Stan and R codes to run the analysis, except the data, are available through the following link: https://github.com/Iraices/IIS_MCMC.

## Acknowledgement(s)

We thank Claes Bernes for supporting this work with data on the meta-analysis in the evidence synthesis example.

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## Funding

This work was supported by the Swedish research council FORMAS through the project “Scaling up uncertain environmental evidence” (219-2013-1271) and the strategic research areas BECC (Biodiversity and Ecosystem Services in a Changing Climate) and MERGE (Modelling the Regional and Global Climate/Earth system).

## References

[1] Sergios Agapiou, Omiros Papaspiliopoulos, Daniel Sanz-Alonso, and Andrew M. Stuart Stuart. Importance sampling: Intrinsic dimension and computational cost. _Statistical Science_, 32(3):405–431, August 2017. doi:10.1214/17-STS611.

[2] James O. Berger. Robust Bayesian analysis: sensitivity to the prior. _Journal of Statistical Planning and Inference_, 25:303–328, 1990.

[3] Jean-Marc Bernard. An introduction to the imprecise Dirichlet model for Multinomial data. _International Journal of Approximate Reasoning_, 39(2):123–150, 2005. ISSN 0888-613X.

[4] Claes Bernes, Stephen R. Carpenter, Anna Gårdmark A., Per Larsson, Lennart Persson, Christian Skov, James D.M. Speed, and Ellen Van Donk. What is the influence of a reduction of planktivorous and benthivorous fish on water quality in temperate eutrophic lakes? A systematic review. _Environmental Evidence_, 4(1):7, 2015. ISSN 2047-2382. doi:10.1186/s13750-015-0032-9.

[5] Sourabh Bhattacharya. Consistent estimation of the accuracy of importance sampling using regenerative simulation. _Statistics & Probability Letters_, 78(15):2522–2527, 2008. ISSN 0167-7152. doi:10.1016/j.spl.2008.02.030.

[6] Steve Brooks, Andrew Gelman, Galin L. Jones, and Xiao-Li Meng, editors. _Handbook of Markov Chain Monte Carlo_. New York: Chapman and Hall/CRC, 2011. doi:10.1201/b10905.

[7] Sourav Chatterjee and Persi Diaconis. The sample size required in importance sampling. _Annals of Applied Probability_, 28(2):1099–1135, 2018. doi:doi:10.1214/17-AAP1326.

[8] Bryce Croll. Markov chain Monte Carlo methods applied to photometric spot modeling. _Publications of the Astronomical Society of the Pacific_, 118(847):1351–1359, 2006.

[9] Takashi Daimon. Predictive checking for Bayesian interim analyses in clinical trials. _Contemporary Clinical Trials_, 29(5):740–750, 2008. ISSN 1551-7144. doi:10.1016/j.cct.2008.05.005.

[10] Ke-Lin Du and M.N.S. Swamy. _Search and Optimization by Metaheuristics. Techniques and Algorithms Inspired by Nature_. Chapman & Hall/CRC Texts in Statistical Science. Springer International Publishing Switzerland, 2016. ISBN 978-3-319-41191-0. doi:10.1007/978-3-319-41192-7.

[11] Daniel Egloff and Markus Leippold. Quantile estimation with adaptive importance sampling. _The Annals of Statistics_, 38(2):1244–1278, 2010. ISSN 00905364.

[12] Víctor Elvira, Luca Martino, and Christian P. Robert. Rethinking the effective sample size. arXiv:1809.04129 [stat.CO], 2018.

[13] Akira Endo, Edwin van Leeuwen, and Marc Baguelin. Introduction to particle Markov chain Monte Carlo for disease dynamics modellers. _Epidemics_, 29:100363, 2019. ISSN 1755-4365. doi:10.1016/j.epidem.2019.100363.

[14] Thomas Fetz. Efficient computation of upper probabilities of failure. In Christian Bucher, Bruce R. Ellingwood, and Dan M. Frangopol, editors, _12th International Conference on Structural Safety & Reliability_, pages 493–502, 2017.

[15] Andrew Gelman, John B. Carlin, Hal S. Stern, David B. Dunson, Aki Vehtari, and Donald B. Rubin. _Bayesian Data Analysis, Third Edition_. Chapman & Hall/CRC Texts in Statistical Science. Taylor & Francis, 2013. ISBN 9781439840955.

[16] Charles J. Geyer. Practical Markov chain Monte Carlo. _Statistical Science_, 7(4):473–483, 1992.

[17] Geof H. Givens and Jennifer A. Hoeting. _Computational Statistics, Second edition_. John Wiley & Sons, 2012.

[18] John Paul Gosling. _SHELF: The Sheffield Elicitation Framework_, volume 261 of _International Series in Operations Research & Management Science_, pages 61–93. Springer International Publishing, 2018. doi:10.1007/978-3-319-65052-4_4.

[19] Anca M. Hanea, Victoria Hemming, and Gabriela F. Nane. Uncertainty quantification with experts: Present status and research needs. _Risk Analysis_, 2021. doi:10.1111/risa.13718.

[20] Marcelo Hartmann, Georgi Agiashvili, Paul Bürkner, and Arto Klami. Flexible prior elicitation via the prior predictive distribution. In Jonas Peters and David Sontag, editors, _Proceedings of the 36th Conference on Uncertainty in Artificial Intelligence (UAI)_, volume 124 of _Proceedings of Machine Learning Research_, pages 1129–1138. PMLR, August 2020.

[21] W.K. Hastings. Monte Carlo sampling methods using Markov chains and their applications. _Biometrika_, 57(1):97–109, 1970. ISSN 00063444.

[22] Darrall Henderson, Sheldon H. Jacobson, and Alan W. Johnson. _Handbook of Metaheuristics. The Theory and Practice of Simulated Annealing_. Springer US, 2003. ISBN 978-0-306-48056-0. doi:10.1007/0-306-48056-5_10.

[23] David Ríos Insua, Fabrizio Ruggeri, and Jacinto Martín. Bayesian sensitivity analysis. In A. Saltelli, K. Chan, and E. M. Scott, editors, _Sensitivity Analysis_, pages 225–244. Wiley, 2000. ISBN 0-471-99892-3.

[24] Augustine Kong. A note on importance sampling using standardized weights. Technical Report 348, University of Chicago, Dept. of Statistics, 1992.

[25] Leonid Kopylev, John Fox, and Chao Chen. Combining risks from several tumors using Markov chain Monte Carlo. In _Uncertainty Modeling in Dose Response: Bench Testing Environmental Toxicity_, pages 197–205. John Wiley & Sons, 2009.

[26] Roman Liesenfeld and Jean-François Richard. Improving MCMC, using efficient importance sampling. _Computational Statistics & Data Analysis_, 53(2):272–288, 2008. ISSN 0167-9473. doi:10.1016/j.csda.2008.07.028.

[27] William A. Link and Mitchell J. Eaton. On thinning of chains in MCMC. _Methods in Ecology and Evolution_, 3:112–115, 2012. doi:10.1111/j.2041-210X.2011.00131.x.

[28] Jun S. Liu. _Monte Carlo Strategies in Scientific Computing_. Springer, New York, 2008.

[29] F. Llorente, E. Curbelo, L. Martino, V. Elvira, and D. Delgado. MCMC-driven importance samplers, 2021.

[30] Luca Martino, Víctor Elvira, and Francisco Louzada. Effective sample size for importance sampling based on discrepancy measures. _Signal Processing_, 131:386–401, 2017. ISSN 0165-1684. doi:10.1016/j.sigpro.2016.08.025.

[31] John C. Nash and Ravi Varadhan. Unifying optimization algorithms to aid software system users: optimx for R. _Journal of Statistical Software_, 43(9):1–14, 2011.

[32] Anthony O’Hagan, Caitlin E. Buck, Alireza Daneshkhah, J. Richard Eiser, Paul H. Garthwaite, David J. Jenkinson, Jeremy E. Oakley, and Tim Rakow. _Uncertain Judgements: Eliciting Experts’ Probabilities_. Chichester: Wiley, 2006.

[33] Art B. Owen. Monte Carlo theory, methods and examples, 2013. URL http://statweb.stanford.edu/~owen/mc/.

[34] Erik Quaeghebeur and Gert de Cooman. Imprecise probability models for inference in exponential families. In Fabio G. Cozman, Robert Nau, and Teddy Seidenfeld, editors, _ISIPTA’05: Proceedings of the Fourth International Symposium on Imprecise Probabilities and Their Applications_, pages 287–296, Pittsburgh, USA, July 2005. URL http://www.sipta.org/isipta05/proceedings/019.html.

[35] Simon L. Rinderknecht, Mark E. Borsuk, and Peter Reichert. Bridging uncertain and ambiguous knowledge with imprecise probabilities. _Environmental Modelling & Software_, 36:122–130, 2012. ISSN 1364-8152. doi:10.1016/j.envsoft.2011.07.022.

[36] Christian Röver. Bayesian random-effects meta-analysis using the bayesmeta R package. arXiv:1711.08683 [stat.CO], 2017.

[37] Daniel Sanz-Alonso. Importance sampling and necessary sample size: An information theory approach. _SIAM/ASA Journal of Uncertainty Quantification_, 6(2):867–879, 2018. doi:10.1137/16M1093549.

[38] Daniel J. Schad, Michael Betancourt, and Shravan Vasishth. Toward a principled Bayesian workflow in cognitive science. arXiv:1904.12765 [stat.ME], 2019.

[39] Daniel P. Simpson, Håvard Rue, Thiago G. Martins, Andrea Riebler, and Sigrunn H. Sørbye. Penalising model component complexity: A principled, practical approach to constructing priors. _Statistical Science_, 32(1):1–28, 2017.

[40] Stan Development Team. RStan: the R interface to Stan, 2018. R package version 2.17.4.

[41] Matthias C. M. Troffaes. A note on imprecise Monte Carlo over credal sets via importance sampling. In Alessandro Antonucci, Giorgio Corani, Inés Couso, and Sébastien Destercke, editors, _Proceedings of the Tenth International Symposium on Imprecise Probability: Theories and Applications_, volume 62 of _Proceedings of Machine Learning Research_, pages 325–332. PMLR, July 2017.

[42] Matthias C. M. Troffaes. Imprecise Monte Carlo simulation and iterative importance sampling for the estimation of lower previsions. _International Journal of Approximate Reasoning_, 101:31–48, October 2018. doi:10.1016/j.ijar.2018.06.009.

[43] Matthias C. M. Troffaes, Thomas Fetz, and Michael Oberguggenberger. Iterative importance sampling for estimating expectation bounds under partial probability specifications. In _The 8th International Workshop on Reliable Engineering Computing (REC2018)_, July 2018.

[44] Ian Vernon and John Paul Gosling. A Bayesian computer model analysis of robust Bayesian analyses, 2017.

[45] Peter Walley. _Statistical Reasoning with Imprecise Probabilities_. Chapman & Hall, London, 1991.

[46] Peter Walley, Lyle Gurrin, and Paul Burton. Analysis of clinical data using imprecise prior probabilities. _Journal of the Royal Statistical Society_, 45(4):457–485, 1996.

[47] Wei Wei and Wenxin Jiang. On Monte Carlo computation of posterior expectations with uncertainty. _Journal of Statistical Computation and Simulation_, 87(10):2038–2049, 2017. doi:10.1080/00949655.2017.1311895.

## Appendix A. Calculations

Explicit calculations for eq. (20) are given here. Recall eq. (20)

$$
\mathrm{Var}_q \Bigl(g(X)\Bigr) = \mathrm{Var}_q\Bigl( (f(X)-\mu) w_p(X) \Bigr)
$$

We will use that, for any random variable $h(X)$,

$$
\begin{aligned}
\mathrm{E}_q\Bigl(h(X)w_p(X)\Bigr)
&=\int h(x)w_p(x)q(x)dx
=\int h(x)\frac{c p(x)}{q(x)} q(x)dx \\
&=c\int h(x)p(x)dx
=c\mathrm{E}_p\Bigl(h(X)\Bigr),
\end{aligned}
$$

which gives

$$
\mathrm{Var}_q \Bigl(h(X)w_p(X) \Bigr)
= c \mathrm{E}_p \Bigl( h^2(X) w_p(X) \Bigr)
- c^2 \mathrm{E}_p\Bigl( h(X) \Bigr)^2
\tag{35}
$$

Taking $h(X) = f(X)-\mu$ and noting that $\mathrm{E}_p \Bigl(h(X)\Bigr)=0$, the expression in eq. (20) expands as follows

$$
\mathrm{Var}_q\Bigl(g(X)\Bigr) = \mathrm{Var}_q\Bigl( (f(X)-\mu) w_p(X) \Bigr) =
c \mathrm{E}_p\Bigl( \left(f(X)-\mu\right)^2 w_p(X) \Bigr)
$$

Applying a second order delta method to the last expectation at $\mathrm{E}_p\Bigl(w_p(X)\Bigr)$ and $\mathrm{E}_p \Bigl(h(X) \Bigr)$, gives (see appendix B for details)

$$
\begin{aligned}
\mathrm{Var}_q\Bigl(g(X)\Bigr) & \approx c \Bigl(\mathrm{E}_p\Bigl(h(X)\Bigr)^2 \mathrm{E}_p \Bigl(w_p(X)\Bigr) + \mathrm{E}_p\Bigl(h(X)\Bigr) \mathrm{Cov}_p \Bigl(w_p(X),h(X)\Bigr) \\
& \quad + \mathrm{E}_p \Bigl(w_p(X)\Bigr) \mathrm{Var}_p\Bigl(h(X)\Bigr)\Bigr)
\end{aligned}
\tag{36}
$$

$$
= c \mathrm{E}_p \Bigl(w_p(X)\Bigr) \mathrm{E}_p \Bigl(h^2(X)\Bigr)
\tag{37}
$$

$$
= c \mathrm{E}_p\Bigl( \left(f(X)-\mu\right)^2 \Bigr) \mathrm{E}_p\Bigl( w_p(X) \Bigr)
\tag{38}
$$

$$
= c \mathrm{Var}_p\Bigl( f(X) \Bigr) \mathrm{E}_p\Bigl( w_p(X) \Bigr).
\tag{39}
$$

Using eq. (39) and the equality $\mathrm{Var}_p(f(X))=N \mathrm{Var}_p(\overline{\mu})$ we obtain

$$
\mathrm{Var}_q(g(X)) \approx N \mathrm{Var}_p(\overline{\mu}) c \mathrm{E}_p\Bigl( w_p(X) \Bigr)
\tag{40}
$$

$$
= N \mathrm{Var}_p(\overline{\mu}) \mathrm{E}_q\Bigl( w^2_p(X) \Bigr)
\tag{41}
$$

$$
= N \mathrm{Var}_p(\overline{\mu}) \left(\frac{1}{N}\sum_{i=1}^N w_p^2(X_i)\right).
\tag{42}
$$

Here we have used that eq. (35) with $h(X)=w_p(X)$ gives the equality $c \mathrm{E}_p( w_p(X) ) = \mathrm{E}_q( w_p^2(X) )$.

## Appendix B. Delta method

Let $g(u,v)$ be a function twice differentiable at $(u,v) = (a_1,a_2)$. Then, the second order Taylor polynomial for $g(u,v)$ near the point $(u,v) = (a_1,a_2)$ is:

$$
\begin{aligned}
g(u,v)_{(a_1,a_2)} & = g(a_1,a_2) + \frac{\partial g}{\partial u}(a_1,a_2)(u - a_1) + \frac{\partial g}{\partial v}(a_1,a_2)(v - a_2) \\
& + \frac{1}{2} \frac{\partial^2 g}{\partial u^2}(a_1,a_2)(u - a_1)^2 + \frac{1}{2} \frac{\partial^2 g}{\partial u \partial v}(a_1,a_2)(u - a_1) (v - a_2) \\
& + \frac{1}{2} \frac{\partial^2 g}{\partial v^2}(a_1,a_2)(v - a_2)^2.
\end{aligned}
\tag{43}
$$

Now, we can use the second order Taylor polynomial approximation to estimate the mean (this is also known as second order delta method).

Let $U$ and $V$ be random variables with mean $\theta_1 = \mathrm{E}_p(U)$ and $\theta_2 = \mathrm{E}_p(V)$ respectively.

$$
\begin{aligned}
\mathrm{E}_p\Bigl(g(U,V)\Bigr)_{(\theta_1,\theta_2)} & \approx g(\theta_1,\theta_2) + \frac{\partial g}{\partial u}(\theta_1,\theta_2) \mathrm{E}_p(U - \theta_1) + \frac{\partial g}{\partial v}(\theta_1,\theta_2) \mathrm{E}_p(V - \theta_2) \\
& + \frac{1}{2} \frac{\partial^2 g}{\partial u^2}(\theta_1,\theta_2)\mathrm{E}_p\Bigl( (U - \theta_1)^2\Bigr) \\
& + \frac{1}{2} \frac{\partial^2 g}{\partial u \partial v}(\theta_1,\theta_2)\mathrm{E}_p \Bigl( (U - \theta_1) (V - \theta_2) \Bigr) \\
& + \frac{1}{2} \frac{\partial^2 g}{\partial v^2}(\theta_1,\theta_2)\mathrm{E}_p \Bigl( (V - \theta_2)^2 \Bigr).
\end{aligned}
\tag{44}
$$

Note that $\mathrm{E}_p(U - \theta_1) = 0$ and $\mathrm{E}_p(V - \theta_2) = 0$. Taking $g(u,v) := v^2 u$ where $V = h(X)$ and $U = w_p(X)$ (to match notation in eq. (36))

$$
\begin{aligned}
\mathrm{E}_p\Bigl(g(U,V)\Bigr)_{(\theta_1,\theta_2)} & \approx g(\theta_1,\theta_2) + \theta_2 \mathrm{Cov}_p(U,V) + \theta_1 \mathrm{Var}_p(V) \\
& \approx \Bigl(\mathrm{E}_p(V)\Bigr)^2 \mathrm{E}_p(U) + \mathrm{E}_p(V) \mathrm{Cov}_p(U,V) + \mathrm{E}_p(U) \mathrm{Var}_p(V)
\end{aligned}
\tag{45}
$$

$$
\begin{aligned}
& \approx \Bigl(\mathrm{E}_p\Bigl(h(X)\Bigr)\Bigr)^2 \mathrm{E}_p\Bigl(w_p(X)\Bigr) + \mathrm{E}_p\Bigl(h(X)\Bigr) \mathrm{Cov}_p\Bigl(w_p(X),h(X)\Bigr) \\
& + \mathrm{E}_p(w_p(X)) \mathrm{Var}_p\Bigl(h(X)\Bigr).
\end{aligned}
\tag{46}
$$

## Appendix C. Proof of existence of minimum

To guarantee the minimum exist in our example, it is enough to prove that the expectation is continuous as a function of $(\mu_0, \tau_0)$ on $[-8,68] \times [5,16]$.

By Fubini’s theorem in our example, we have

$$
\mathrm{E}_{(\mu_0, \tau_0)}(\mu) := \int_{1}^{\tau_0} \int_1^5 \int_{- \infty}^{+\infty} \mu \cdot p_{(\mu_0, \tau_0)}(\mu,\tau_\mu,k) \,d\mu \,dk \,d\tau_\mu,
\tag{47}
$$

where

$$
\begin{aligned}
p_{(\mu_0, \tau_0)}(\mu,\tau_\mu,k) &= \frac{1}{c(\mu_0,\tau_0)} \cdot \Biggl(\prod_{i=1}^N \frac{1}{\sqrt{\sigma^2_i + k^2\tau_\mu^2}}\Biggr)
\exp \Biggl\{ -\frac{1}{2} \sum_{i = 1}^N \frac{(y_i - \mu)^2}{\sigma^2_i + k^2\tau_\mu^2} \Biggr\} \cdot \\
& \cdot \frac{1}{ \tau_\mu} \exp \Bigl\{ -\frac{1}{2}\frac{(\mu - \mu_0)^2}{\tau_\mu^2} \Bigr\}
\end{aligned}
$$

is the posterior probability distribution. The proportionality constant $c(\mu_0,\tau_0)$ is given by

$$
\begin{aligned}
c(\mu_0,\tau_0) & = \int_{1}^{\tau_0} \int_1^5
\Biggl( \prod_{i=1}^N \frac{1}{\sqrt{\sigma^2_i + k^2\tau_\mu^2}}\Biggr)
\frac{1}{\tau_\mu} \\
& \Biggl[ \int_{- \infty}^{+\infty}
\exp \Bigl\{-\frac{1}{2} \sum_{i = 1}^N \frac{(y_i - \mu)^2}{\sigma^2_i + k^2\tau_\mu^2} \Bigr\} \cdot
\exp \Bigl\{ -\frac{1}{2}\frac{(\mu - \mu_0)^2}{\tau_\mu^2} \Bigr\}
\,d\mu \Biggr ] \,dk \,d\tau_\mu
\end{aligned}
\tag{48}
$$

$$
\begin{aligned}
&= \int_{1}^{\tau_0} \int_1^5
\Biggl( \prod_{i=1}^N \frac{1}{\sqrt{\sigma^2_i + k^2\tau_\mu^2}}\Biggr)
\frac{1}{ \tau_\mu} \\
& \Biggl[ \int_{- \infty}^{+\infty}
\exp \Biggl\{-\frac{1}{2} \Biggl( a(\tau_\mu, k, \mu_0)\mu^2 -2b(\tau_\mu, k, \mu_0) \mu + c(\tau_\mu, k, \mu_0)\Biggr) \Biggr\}
\,d\mu \Biggr ] \,dk \,d\tau_\mu
\end{aligned}
\tag{49}
$$

where

$$
a(\tau_\mu, k, \mu_0) = \sum_{i =1}^N \frac{1}{\sigma_i^2 + k^2\tau_\mu^2} + \frac{1}{\tau_\mu^2},
\tag{50}
$$

$$
b(\tau_\mu, k, \mu_0) = \sum_{i =1}^N \frac{y_i}{\sigma_i^2 + k^2\tau_\mu^2} + \frac{\mu_0}{\tau_\mu^2},
\tag{51}
$$

$$
c(\tau_\mu, k, \mu_0) = \sum_{i =1}^N \frac{y_i^2}{\sigma_i^2 + k^2\tau_\mu^2} + \frac{\mu_0^2}{\tau_\mu^2}.
\tag{52}
$$

Since $a(\tau_\mu, k, \mu_0) > 0$, then by Lemma D.1 in (48), we get that the integral with respect to $\mu$ is

$$
\sqrt{2\pi}\cdot a(\tau_\mu, k, \mu_0)^{\frac{-1}{2}} \cdot \exp \Biggl\{-\frac{1}{2} \Biggl(c(\tau_\mu, k, \mu_0) - \frac{b(\tau_\mu, k, \mu_0)^2}{a(\tau_\mu, k, \mu_0)}\Biggr)\Biggr\}.
\tag{53}
$$

Note that $a(\tau_\mu, k, \mu_0)$, $b(\tau_\mu, k, \mu_0)$ and $c(\tau_\mu, k, \mu_0)$ are continuously differentiable and $\tau_\mu \in [1, \tau_0]$ and $k \in [1,\, 5]$. Thus, by Leibniz integral rule it follows that $c(\mu_0,\tau_0)$ is continuously differentiable on $[-8,68] \times [5,16]$.

Analogously, applying Lemma D.2 to eq. (47), we get that the integral with respect to $\mu$ is

$$
\sqrt{2\pi}\cdot a(\tau_\mu, k, \mu_0)^{\frac{-3}{2}} \cdot b(\tau_\mu, k, \mu_0) \cdot \exp \Biggl\{-\frac{1}{2} \Biggl (c(\tau_\mu, k, \mu_0) - \frac{b(\tau_\mu, k, \mu_0)^2}{a(\tau_\mu, k, \mu_0)} \Biggr) \Biggr\}.
\tag{54}
$$

Furthermore, by Leibniz integral rule it yields that $\mathrm{E}_{(\mu_0, \tau_0)}(\mu)$ is continuously differentiable on $[-8,68] \times [5,16]$.

## Appendix D. Lemmas

**Lemma D.1.** *Let $a > 0, b \in \mathbb{R}$ and $c \in \mathbb{R}$. It holds that:*

$$
\int_{-\infty}^{+\infty} \exp \Biggl\{-\frac{1}{2}(ax^2 -2bx + c)\Biggr\} \,dx
\tag{55}
$$

$$
= \sqrt{2\pi} \cdot a^{-\frac{1}{2}} \cdot \exp \Biggl \{ -\frac{1}{2} \Biggl(c - \frac{b^2}{a} \Biggr) \Biggr \}.
\tag{56}
$$

**Proof.** By completing the square, we obtain

$$
\int_{-\infty}^{+\infty} \exp \Biggl\{-\frac{1}{2}\Biggl(\frac{x - \frac{b}{a}} {a^{-\frac{1}{2}}}\Biggr) ^2 \Biggr\}
\cdot \exp \Biggl\{-\frac{1}{2}\Biggl(c - \frac{b^2}{a}\Biggr) \Biggr \} \,dx
\tag{57}
$$

$$
= \sqrt{2 \pi} \cdot a^{-\frac{1}{2}} \cdot \exp \Biggl\{-\frac{1}{2} \Biggl(c - \frac{b^2}{a}\Biggr)\Biggr\} \cdot
\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi} \cdot a^{-\frac{1}{2}}}
\exp \Biggl\{-\frac{1}{2} \Biggl(\frac{x - \frac{b}{a}} {a^{-\frac{1}{2}}}\Biggr) ^2 \Biggr\} \,dx.
\tag{58}
$$

Note that the integrand is the probability density function of a normally distributed random variable with mean $\frac{b}{a}$ and variance $\frac{1}{a}$, (i.e. $N \Bigl (\frac{b}{a}, \frac{1}{a}\Bigr)$). Thus, the desired result immediately follows. $\square$

**Lemma D.2.** *Let $a > 0, b \in \mathbb{R}$ and $c \in \mathbb{R}$. It holds that:*

$$
\int_{-\infty}^{+\infty} x \exp \Biggl\{-\frac{1}{2}(ax^2 -2bx + c)\Biggr\} \,dx
\tag{59}
$$

$$
= \sqrt{2\pi} \cdot a^{-\frac{3}{2}}\cdot b \cdot \exp \Biggl \{ -\frac{1}{2}\Biggl(c - \frac{b^2}{a} \Biggr) \Biggr \}.
\tag{60}
$$

**Proof.** By completing the square, we obtain

$$
\int_{-\infty}^{+\infty} x \cdot \exp \Biggl\{-\frac{1}{2}\Biggl(\frac{x - \frac{b}{a}} {a^{-\frac{1}{2}}}\Biggr) ^2 \Biggr\}
\cdot \exp \Biggl\{-\frac{1}{2} \Biggl(c - \frac{b^2}{a} \Biggr) \Biggr \} \,dx
\tag{61}
$$

$$
= \sqrt{2 \pi} \cdot a^{-\frac{1}{2}} \cdot \exp \Biggl\{-\frac{1}{2} \Biggl(c - \frac{b^2}{a} \Biggr)\Biggr\} \cdot
\int_{-\infty}^{+\infty} \frac{1}{\sqrt{2 \pi} \cdot a^{-\frac{1}{2}}}
x \exp \Biggl\{-\frac{1}{2} \Biggl(\frac{x - \frac{b}{a}} {a^{-\frac{1}{2}}}\Biggr) ^2 \Biggr\} \,dx.
\tag{62}
$$

Note that the previous integral is the expected value of a normally distributed random variable with mean $\frac{b}{a}$ and variance $\frac{1}{a}$, (i.e. $N \Bigl (\frac{b}{a}, \frac{1}{a}\Bigr)$). Thus, the desired result immediately follows. $\square$

## Conversion notes

- Source: arXiv:2206.08728v1 (17 Jun 2022 preprint, 19 pages). Authors: Ivette Raices Cruz, Johan Lindström, Matthias C. M. Troffaes, Ullrika Sahlin. Published version: Computational Statistics & Data Analysis 176 (2022) 107558, doi:10.1016/j.csda.2022.107558 (open access; numbering and wording may differ from this preprint). Authors' code (R/Stan): https://github.com/Iraices/IIS_MCMC.
- Mathematics is taken from the authors' arXiv TeX source (macros expanded) and checked against the PDF; printed equation numbers are \tag{1}-\tag{62}; aligned displays with several printed numbers are split into one block per number; \coloneqq is written ':='. The authors' typos and oddities are kept as printed (e.g. upper limit N-k in (15), bare appendix references 'see A', 'see C').
- Run-in subsection titles (e.g. '5.5. The influence of prior data conflict') are headings. Steps 1-5 of the iterative algorithm (Section 4) are a printed list kept as text with bold 'Step n:' labels.
- Tables 1-4 are transcribed as cells with plain-Unicode headers; a 'Transcription note' after a table gives its header symbols in LaTeX. Figures are image crops; values inside plots are not transcribed. Floats sit at paragraph boundaries near their printed position.
