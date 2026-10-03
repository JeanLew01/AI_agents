## Conversion notes

- Source version: arXiv:2112.05745v3 [eess.SY], 13 Apr 2022 (25 pages, single column, L4DC/JMLR style); authors T. Lew, L. Janson, R. Bonalli, M. Pavone; the paper appeared at L4DC 2022. This package was made from the arXiv v3 PDF, which contains the main text (Sections 1-7), the references and the appendix (Appendices A-E with all proofs), not from the proceedings version.
- Mathematics was transcribed to LaTeX from the authors' arXiv TeX source (main.tex, preamble.tex, main.bbl), with the authors' private macros expanded to standard LaTeX, and every formula was checked against the PDF pages (150 dpi page renders, 230-260 dpi crops for all theorem statements and all appendix proofs). No formula is kept as an image only. Where TeX and PDF differ the PDF was followed: the offset vector written \vec{r} in the source is printed as a bold letter (no arrow) and is transcribed $\boldsymbol{r}$.
- Notation as printed: $\mathrm{H}(\cdot)$ is the convex hull (upright H; inside italic theorem bodies the PDF prints it in italic), $\oplus$ the Minkowski sum, $B(x,r)$ / $\mathring{B}(x,r)$ the closed / open ball, $D(A,d)$ the $d$-covering number, $\hat{\mathcal{Y}}^M$ the convex hull of the $M$ output samples and $\hat{\mathcal{Y}}^M_\epsilon=\hat{\mathcal{Y}}^M\oplus B(0,\epsilon)$ the $\epsilon$-padded estimator. In Appendix B the upright $Y$, $Y^M$, $Y^M_\epsilon$ (a generic compact set, the sample set, the union of $\epsilon$-balls around the samples) are different objects from the calligraphic $\mathcal{Y}$ (the reachable set). The Hausdorff distance is printed $d_\mathrm{H}$ in equations (3) and (5) and $d_H$ elsewhere.
- Printed equation numbers are given with \tag: (1)-(3) and (4a)-(4b) in the main text, (5)-(8) and (C1)-(C2) in the appendix; all other displays are unnumbered in the paper. Theorem-like blocks carry their printed bold labels with the printed punctuation: Assumptions 1-5, Theorem 1 (Asymptotic Convergence), Theorem 2 (Finite-Sample Bound) and Corollary 1 in the main text; Definition 1, Theorem 3 and Lemmas 2-7 in the appendix (this version has no Lemma 1). Each block ends where the authors' TeX environment ends. Assumption 1, Theorem 1, Theorem 2 and Corollary 1 are stated in Sections 4-5 and restated in Appendix B.1-B.3, so each of these labels occurs twice; the appendix restatements of Theorem 2 and Corollary 1 write the conclusion as two separate probability bounds and are followed by a Remark on the assumption $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$.
- Figures 1-6 (main text) are image crops in assets/figure/, Figures 7-8 (appendix; printed numbering continues) are in assets/supp_figs/ as supplementary-figure-7 and supplementary-figure-8; all captions are verbatim text. Wrapped and floating figures are placed at paragraph boundaries next to the text that discusses them: Figures 1-5 and 8 beside the paragraphs they are printed next to, Figure 6 (printed at the top of its page) after the paragraph of Section 6.3 that cites it, Figure 7 (printed at the top of its page) in step (C2) of the proof of Theorem 1 where the TeX source inserts it. The paper has no tables and no algorithm box; the algorithm is described in Section 3 and Figure 1, and the two enumerated procedures of Appendix D and E.1 are transcribed as numbered lists.
- Footnotes 1-8 are kept as separate paragraphs starting with 'Footnote n:'; the marks in the text are written $^{n}$. Footnotes 3-6 and 8 stand where the page prints them (after the last text of their page). Footnotes 1, 2 and 7 are printed below a sentence that continues on the next page and are placed after the paragraph (footnote 1) or at the end of the subsection (footnote 2: end of Section 6.2; footnote 7: end of Appendix B.1) that carries the mark. Two formulas are split by a page break in the PDF ($x_t\in\mathbb{R}^6$ in Section 6.3 and the set $\mathcal{X}_0$ in Appendix E.2); they are written whole.
- Citations are author-year as printed (the bibliography is unnumbered, 50 entries, alphabetical). Small-caps names are written RandUP, ReachLP, ReachSDP and GoTube; e-mail addresses printed in small caps are written in lower case; end-of-proof squares are written $\blacksquare$.
- The text and formulas are kept as printed. The following are in the source and are not conversion errors: 'thrustworthy' (Section 1); 'analyis' and 'guarantees, Our analysis' (Section 2); '$\mathcal{Y}^M_\epsilon$ converges' without a hat (after Theorem 1) and $\{\mathcal{Y}^M\}$, $d_H(\mathcal{Y}^M,\mathcal{Y})$ without hats in the conclusion of Theorem 3; '$d$-packing number' before Theorem 2 for the quantity defined as the $d$-covering number; the bound $(2d\sqrt{n}/\epsilon)^n$ with $n$ in Section 5.3; $d_H(\hat{\mathcal{Y}}^M,\mathcal{Y})$ without $\mathrm{H}$ in Section 6.1 and 'theorical' in the Figure 3 caption; the interval $[-0.015,0.015]$ without square in the definition of $\mathcal{X}_t(\nu)$ (Section 6.3); in the proof of Theorem 1: '$G^1_\partial$ ... for $j=1,2$', '$\bigcap_{N=0}^\infty A_n\subseteq A_0$', 'Since $\epsilon\rightarrow\bar\epsilon$', '$G^1_\delta,G^2_\delta$', '$m\geq 1$', 'a sufficient conditions', 'conludes'; in Appendix B.3 '$x\in\mathbb{R}^n$'; in Appendix C 'in Theorem 2', the constant $c_2$ introduced as a second '$c_1$', and the mixed use of $p$ and $n$ in $V(r,a)$; in Appendix E.1 an unbalanced parenthesis in the formula for $p_0^\alpha$; 'explicitely' (Appendix D).

<!-- PDF page 1 -->

# A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis

**Thomas Lew**$^1$ (thomas.lew@stanford.edu)

**Lucas Janson**$^2$ (ljanson@fas.harvard.edu)

**Riccardo Bonalli**$^3$ (riccardo.bonalli@l2s.centralesupelec.fr)

**Marco Pavone**$^1$ (pavone@stanford.edu)

$^1$ Department of Aeronautics and Astronautics, Stanford University

$^2$ Department of Statistics, Harvard University

$^3$ Laboratory of Signals and Systems, University of Paris-Saclay, CNRS, CentraleSupélec

## Abstract

In this work, we analyze an efficient sampling-based algorithm for general-purpose reachability analysis, which remains a notoriously challenging problem with applications ranging from neural network verification to safety analysis of dynamical systems. By sampling inputs, evaluating their images in the true reachable set, and taking their $\epsilon$-padded convex hull as a set estimator, this algorithm applies to general problem settings and is simple to implement. Our main contribution is the derivation of asymptotic and finite-sample accuracy guarantees using random set theory. This analysis informs algorithmic design to obtain an $\epsilon$-close reachable set approximation with high probability, provides insights into which reachability problems are most challenging, and motivates safety-critical applications of the technique. On a neural network verification task, we show that this approach is more accurate and significantly faster than prior work. Informed by our analysis, we also design a robust model predictive controller that we demonstrate in hardware experiments.

**Keywords:** reachability analysis, random set theory, robust control, neural network verification.

## 1. Introduction

![Figure 1](../assets/s001-lew2022simple/figure-1.png)

Figure 1: $\epsilon$-RandUP consists of three simple steps: 1) sampling $M$ inputs $x_i$ in $\mathcal{X}$, 2) propagating these inputs through the reachability map $f$, and 3) taking the $\epsilon$-padded convex hull $\hat{\mathcal{Y}}_\epsilon^M$ to approximate the reachable set $\mathcal{Y}$.

Forward reachability analysis entails characterizing the reachable set of outputs of a given function corresponding to a set of inputs. This type of analysis underpins a plethora of applications in model predictive control, neural network verification, and safety analysis of dynamical systems. Sampling-based reachability analysis techniques are a particularly simple class of methods to implement; however, conventional wisdom suggests that if insufficient representative samples are considered, these methods may not be robust in that they cannot rule out edge cases missed by the sampling procedure. Alternatively, by leveraging structure in specific problem formulations or computational methods designed for exhaustivity (e.g., branch and bound), a large range of algorithms with deterministic accuracy and performance

<!-- PDF page 2 -->

guarantees have been developed. However, these methods often sacrifice simplicity and generality for their power, motivating the development of algorithms that avoid such restrictions.

In this work, we analyze a simple yet efficient sampling-based algorithm for general-purpose reachability analysis. As depicted in Figure 1, it consists of 1) sampling inputs, 2) propagating these inputs, and 3) taking the padded convex hull of these output samples. We refer to this RANDomized Uncertainty Propagation algorithm as $\epsilon$-RandUP: it is simple to implement, benefits from statistical accuracy guarantees, and applies to a wide range of problems including reachability analysis of uncertain dynamical systems with neural network controllers. Importantly, $\epsilon$-RandUP fulfills key desiderata that a general-purpose reachability analysis algorithm should satisfy:

- it works with any choice of possibly nonlinear reachability maps and non-convex input sets,
- its estimate of the reachable set is conservative with high probability and tighter than prior work,
- it is efficient and does not require precomputations, which is a key advantage for learning-based control applications where uncertainty bounds and models are updated in real-time.

Our main contribution is a thorough analysis of the statistical properties of $\epsilon$-RandUP. Specifically:

1. We prove that the set estimator converges to the $\epsilon$-padded convex hull of the true reachable set as the number of samples increases. Our assumption about the sampling distribution is weaker than in related work and implies that sampling the boundary of the input set is sufficient. This asymptotic result justifies using $\epsilon$-RandUP as a thrustworthy baseline for offline validation whenever the reachability map and the input set are complex and no tractable algorithm exists.
2. We derive a finite-sample bound for the Hausdorff distance between the output of $\epsilon$-RandUP and the convex hull of the true reachable set, assuming that the reachability map is Lipschitz continuous. This result informs algorithmic design (e.g., how to choose the number of samples to obtain an $\epsilon$-accurate approximation with high probability), sheds insights into which problems are most challenging, and motivates using this simple algorithm in safety-critical applications.

We demonstrate $\epsilon$-RandUP on a neural network controller verification task and show that it is highly competitive with prior work. We also embed this algorithm within a robust model predictive controller and present hardware results demonstrating the reliability of the approach.

## 2. Related work

Reachability analysis has found a wide range of applications ranging from model predictive control (Schürmann et al., 2018), robotics (Shao et al., 2021; Lew et al., 2022), neural network verification (Tran et al., 2019; Hu et al., 2020), to orbital mechanics (Wittig et al., 2015). Reachability analysis is particularly relevant in safety-critical applications which require the strict satisfaction of specifications. For instance, a drone transporting a package should never collide with obstacles and respect velocity bounds for any payload mass in a bounded input set. In contrast to stochastic problem formulations which typically consider the inputs as random variables with known probability distributions (Webb et al., 2019; Sinha et al., 2020; Devonport and Arcak, 2020), we consider robust formulations which are of interest whenever minimal information about the inputs is available.

Deterministic algorithms are often tailored to the particular parameterization of the reachability map and to the shape of the input set. For instance, one finds methods that are particularly designed for neural networks (Tran et al., 2019; Ivanov et al., 2019; Hu et al., 2020), nonlinear hybrid systems (Chen et al., 2013; Kong et al., 2015), linear dynamical systems with zonotopic (Girard, 2005) and

<!-- PDF page 3 -->

ellipsoidal (Kurzhanski and Varaiya, 2000) parameter sets, etc. We refer to (Liu et al., 2021) and (Althoff et al., 2021) for recent comprehensive surveys. Such algorithms have deterministic accuracy guarantees but require problem-specific structure that restricts the class of systems they apply to. Given the wide range of applications of reachability analysis, there is a pressing need for the development and analysis of simple algorithms that can be applied to general problem formulations.

On the other hand, sampling-based algorithms reconstruct the reachable set from sampled outputs. The stochasticity is typically controlled by the engineer, who selects the number of samples and their distribution. A key strength of this methodology is the possible use of black-box models with arbitrary input sets, which allows using complex simulators of the system. For instance, kernel-based methods (De Vito et al., 2014; Rudi et al., 2017; Thorpe et al., 2021) have been proposed as a strong approach for data-driven reachability analysis. Kernel-based methods are highly expressive, as selecting a completely separating kernel (De Vito et al., 2014) enables reconstructing any closed set to arbitrary precision given enough samples. Their main drawback is the potentially expensive evaluation of the estimator for a large number of samples. Its implicit representation as a level set is also not particularly convenient for downstream applications.

Sampling-based reachable set estimators with pre-specified shapes have been proposed to simplify computations and downstream applications. Recently, (Lew and Pavone, 2020) proposed to approximate reachable sets with the convex hull of the samples, but this approach is not guaranteed to return a conservative approximation. Ellipsoidal and rectangular sets are computed in (Devonport and Arcak, 2020) using the scenario approach, but this work tackles a different problem formulation with inputs that are random variables with known distribution. To tackle the robust reachability analyis problem setting, (Gruenbacher et al., 2022) use a ball estimator that bounds the samples. The statistical analysis is restricted to ball-parameterized input sets, uniform sampling distributions, and smooth diffeomorphic reachability maps that represent the solution of a neural ordinary differential equation (Chen et al., 2018) from the input set. In practice, using an outer-bounding ball is more conservative than taking the convex hull of the samples, see Section 6.

In this work, we slightly modify RandUP (Lew and Pavone, 2020) with an additional $\epsilon$-padding step to yield finite-sample outer-approximation guarantees, Our analysis leverages random set theory (Matheron, 1975; Molchanov, 2017), which provides a natural mathematical framework to analyze the reachable set estimator. We characterize its accuracy using the Hausdorff distance to the convex hull of the true reachable set, which provides an intuitive error measure that can be directly used for downstream control applications. Our analysis draws inspiration from the vast literature on statistical geometric inference, which proposes different set estimators including union of balls (Devroye and Wise, 1980; Baillo and Cuevas, 2001), convex hulls (Ripley and Rasson, 1977; Schneider, 1988; Dumbgen and Walther, 1996), $r$-convex hulls (Rodriguez-Casal and Saavedra-Nieves, 2016, 2019; Arias-Castro et al., 2019), Delaunay complexes (Boissonnat and Ghosh, 2013; Aamari, 2017; Aamari and Levrard, 2018), and kernel-based estimators (De Vito et al., 2014; Rudi et al., 2017). This research typically makes assumptions about the set to be reconstructed (e.g., it is convex (Dumbgen and Walther, 1996) or has bounded reach (Cuevas, 2009)) and considers points that are directly sampled from this set. In this work, we derive similar results for reachable sets given known properties of the input set, reachability map, and chosen input sampling distribution.

## 3. Problem definition

In this section, we introduce our notations and problem formulation. Due to space constraints, we leave measure-theoretic details to Appendix A. We denote $\lambda(\cdot)$ for the Lebesgue measure over $\mathbb{R}^p$,

<!-- PDF page 4 -->

$\Gamma(\cdot)$ for the gamma function, $\mathrm{H}(A)$ for the convex hull of a subset $A\subset\mathbb{R}^n$, $A^{\mathsf{c}}=\mathbb{R}^n\setminus A$ for its complement, $\partial A$ for its boundary, $\oplus$ for the Minkowski sum, $B(x,r):=\{y\in\mathbb{R}^n: \|y-x\|\leq r\}$ for the closed ball of center $x\in\mathbb{R}^n$ and radius $r\geq 0$, and $\mathring{B}(x,r)$ for the open ball. The family of nonempty compact subsets of $\mathbb{R}^n$ is denoted as $\mathcal{K}$. For any $A\in\mathcal{K}$ and $d>0$, $D(A, d):=\min\{n\in\mathbb{N} : \exists \{a_1,\dots,a_n\}\subset\mathbb{R}^n, \ A\subset B(a_1,d)\cup\dots\cup B(a_n,d)\}$ denotes the $d$-covering number of $A$.

Let $\mathcal{X}\subset\mathbb{R}^p$ be a compact nonempty set of inputs and $f:\mathbb{R}^p\rightarrow\mathbb{R}^n$ be a continuous function. In this work, we tackle the general problem of reachability analysis, i.e., characterizing the set of reachable outputs $y=f(x)$ for all possible inputs $x\in\mathcal{X}$. This problem is also often referred to as uncertainty propagation. Mathematically, the objective consists of efficiently computing an accurate approximation of the reachable set $\mathcal{Y}\subset\mathbb{R}^n$, which is defined as

$$
\mathcal{Y} = f(\mathcal{X}) = \{ f(x) \, :\, x\in\mathcal{X} \}. \tag{1}
$$

To tackle this problem, $\epsilon$-RandUP relies on the choice of three parameters: a number of samples $M\in\mathbb{N}$, a padding constant $\epsilon>0$, and a sampling distribution $\mathbb{P}_\mathcal{X}$ on measurable subsets of $\mathbb{R}^{p}$. As depicted in Figure 1, $\epsilon$-RandUP consists of sampling $M$ independent identically-distributed inputs $x_i$ in $\mathcal{X}$ according to $\mathbb{P}_\mathcal{X}$, of evaluating each output $y_i=f(x_i)$, and of computing the $\epsilon$-padded convex hull

$$
\hat{\mathcal{Y}}_\epsilon^M := \mathrm{H}\left(\{y_i\}_{i=1}^M\right)\oplus B(0,\epsilon). \tag{2}
$$

Our analysis hinges on the observation that the reachable set estimator $\hat{\mathcal{Y}}_\epsilon^M$ is a *random compact set*, i.e., $\hat{\mathcal{Y}}_\epsilon^M$ is a random variable taking values in the family of nonempty compact sets $\mathcal{K}$. We refer to Appendix A for rigorous definitions using random set theory. Intuitively, different input samples $x_i$ in $\mathcal{X}$ induce different output samples $y_i$ in $\mathcal{Y}$, resulting in different approximated reachable sets $\hat{\mathcal{Y}}_\epsilon^M$. To characterize the accuracy of the estimator, we use the *Hausdorff metric*, which is defined as

$$
d_\mathrm{H}(A,B) := \max\big( \sup_{x\in B} \inf_{y\in A} \|x-y\|, \ \sup_{x\in A} \inf_{y\in B} \|x-y\| \big) \quad \text{for any } A,B\in\mathcal{K}. \tag{3}
$$

This metric induces a topology and an associated $\sigma$-algebra, which enables rigorously defining random compact sets as random variables and describing their convergence; see Appendix A. Interestingly, the distribution of a random compact set is characterized by the probability that it intersects any given compact set. We use this fact in Sections 4 and 5, where we characterize the probability that the set estimator $\hat{\mathcal{Y}}_\epsilon^M$ intersects well-chosen sets along the boundary of the true reachable set. By analyzing the distribution of $\hat{\mathcal{Y}}_\epsilon^M$, this approach allows bounding the Hausdorff distance between $\hat{\mathcal{Y}}_\epsilon^M$ and the convex hull of the true reachable set $\mathrm{H}(\mathcal{Y})$ with high probability.

## 4. Asymptotic analysis

In this section, we provide an asymptotic analysis under minimal assumptions about the input set and the reachability map (namely, that $\mathcal{X}$ is compact and $f$ is continuous). To enable the reconstruction of the true convex hull $\mathrm{H}(\mathcal{Y})$ using the sampling-based set estimator $\hat{\mathcal{Y}}_\epsilon^M$, we make one assumption about the sampling distribution $\mathbb{P}_\mathcal{X}$ for the inputs $x_i$. Note that by definition, $\mathbb{P}_\mathcal{X}(\mathcal{X})=1$.

**Assumption 1** $\mathbb{P}_\mathcal{X}(\{x\in\mathcal{X}: f(x)\in\mathring{B}(y,r)\})>0$ for all $y\in\partial\mathcal{Y}$ and all $r>0$.

This assumption states that the probability of sampling an output arbitrarily close to any point on the boundary of the true reachable set is strictly positive. In other words, the boundary of the reachable

<!-- PDF page 5 -->

set should be contained in the support of the distribution of the output samples $y_i$. Assumption 1 is weaker than the associated assumption in (Lew and Pavone, 2020, Theorem 2), which can be restated as "*$\mathbb{P}_\mathcal{X}(f^{-1}(A))>0$ for any open set $A\subset\mathbb{R}^n$ such that $\mathcal{Y}\cap A\neq \emptyset$*". Indeed, Assumption 1 only considers open neighborhoods of the boundary $\partial\mathcal{Y}$, as opposed to all open sets intersecting $\mathcal{Y}$. Selecting a sampling distribution $\mathbb{P}_\mathcal{X}$ that satisfies Assumption 1 is easy. For instance, if $\mathcal{X}$ has a smooth boundary (see Assumption 4), then the uniform distribution over $\mathcal{X}$ satisfies Assumption 1.

Assumption 1 is sufficient to prove that the random set estimator $\hat{\mathcal{Y}}_\epsilon^M$ converges to the $\epsilon$-padded convex hull of $\mathcal{Y}$ as the number of samples $M$ increases. Below, we prove a more general result which allows for variations of the padding radius $\epsilon$ as the number of samples increases.

**Theorem 1 (Asymptotic Convergence)** Let $\bar{\epsilon}\geq 0$ and $(\epsilon_M)_{M\in\mathbb{N}}$ be a sequence of padding radii such that $\epsilon_M\geq 0$ for all $M\in\mathbb{N}$ and $\epsilon_M\rightarrow \bar{\epsilon}$ as $M\rightarrow\infty$. For any $\epsilon\geq 0$, define the estimator $\hat{\mathcal{Y}}^M_{\epsilon}=\mathrm{H}\left(\{y_i\}_{i=1}^M\right)\oplus B(0,\epsilon)$. Then, under Assumption 1, almost surely, as $M\rightarrow\infty$,

$$
d_H(\hat{\mathcal{Y}}_{\epsilon_M}^M, \mathrm{H}(\mathcal{Y})\oplus B(0,\bar{\epsilon})) \longrightarrow 0.
$$

**Proof** We refer to Appendix B.1. We leverage (Molchanov, 2017, Proposition 1.7.23) which states sufficient conditions for the convergence of random compact sets and use properties of the convex hull to relax the corresponding assumption in (Lew and Pavone, 2020) with Assumption 1. $\blacksquare$

Practically, Theorem 1 justifies using $\epsilon$-RandUP for general continuous maps $f$ and compact sets $\mathcal{X}$. This consistency result implies that choosing any converging sequence of padding radii (e.g., $\epsilon_M=1/M$) guarantees the convergence of the random set estimator $\hat{\mathcal{Y}}_{\epsilon_M}^M$ to the $\bar{\epsilon}$-padded convex hull of the true reachable set. As a particular case, selecting a constant padding radius $\epsilon$ (which yields $\epsilon$-RandUP) guarantees that $\mathcal{Y}_{\epsilon}^M$ converges to the $\epsilon$-padded convex hull $\mathrm{H}(\mathcal{Y})\oplus B(0,\epsilon)$.

Compared to (Lew and Pavone, 2020, Theorem 2), which only treats the case with constant zero padding radii $\epsilon_M=\bar\epsilon=0$ (i.e., without $\epsilon$-padding the convex hull of the output samples), Theorem 1 allows for variations of the padding radii $\epsilon_M$ and is proved under weaker assumptions. Instead of relying on $\epsilon$-covering arguments (e.g., see Corollary 1 in (Dumbgen and Walther, 1996) which assumes that $\mathcal{Y}$ is convex), we use (Molchanov, 2017, Proposition 1.7.23) to conclude asymptotic convergence. This proof technique allows deriving a general result that does not depend on the exact sampling density along the boundary $\partial\mathcal{Y}$ and uses a sequence of padding radii $\epsilon_M$ converging arbitrarily slowly to some constant $\bar{\epsilon}\geq 0$.

## 5. Finite-sample analysis

Theorem 1 provides asymptotic convergence guarantees that support the application of $\epsilon$-RandUP in general scenarios (e.g., as a baseline for offline validation in complex problem settings), but does not provide finite-sample guarantees which are of practical interest in safety-critical applications. Deriving stronger statistical guarantees requires leveraging more information about the structure of the problem. We derive finite-sample rates under general assumptions in Section 5.1 and analyze a particular case in Section 5.2. We discuss practical implications of our results in Section 5.3.

### 5.1. General finite-sample statistical guarantees

To derive convergence rates and outer-approximation guarantees given a finite number of samples $M$, we first make an assumption about the smoothness of the reachability map $f$.

<!-- PDF page 6 -->

**Assumption 2** The reachability map $f:\mathbb{R}^p\rightarrow\mathbb{R}^n$ is $L$-Lipschitz: for some constant $L\geq 0$, $\|f(x_1)-f(x_2)\| \leq L\,\|x_1-x_2\|$ for all $x_1,x_2\in\mathcal{X}$.

Next, we make an assumption about the sampling distribution $\mathbb{P}_\mathcal{X}$ along the input set boundary $\partial\mathcal{X}$.

**Assumption 3** Given $\epsilon,L>0$, there exists $\Lambda_{\epsilon}^{L}>0$ such that $\mathbb{P}_\mathcal{X}\left(B\left(x,\frac{\epsilon}{2L}\right)\right)\geq \Lambda_{\epsilon}^{L}$ for all $x\in\partial\mathcal{X}$.

Given any boundary input $x\in\partial\mathcal{X}$, the constant $\Lambda_{\epsilon}^{L}$ characterizes the probability of sampling an input $x_i$ that is $\epsilon/(2L)$-close to $x$. Selecting a sampling distribution that satisfies Assumption 3 is simple; we provide examples in Sections 5.2 and 6. As we show next, these two assumptions are sufficient to derive finite-sample convergence rates for $\epsilon$-RandUP. Recall that $D(\partial\mathcal{X}, d)$ denotes the $d$-packing number of $\partial\mathcal{X}$, which is necessarily finite by the compactness of $\mathcal{X}$.

**Theorem 2 (Finite-Sample Bound)** Define the estimator $\hat{\mathcal{Y}}^M=\mathrm{H}\left(\{y_i\}_{i=1}^M\right)$ and the probability threshold $\delta_M= D(\partial\mathcal{X},\epsilon/(2L))(1 - \Lambda_{\epsilon}^{L})^M$. Then, under Assumptions 2 and 3 and assuming that $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$, with probability at least $1-\delta_M$,

$$
d_H(\hat{\mathcal{Y}}^M, \mathrm{H}(\mathcal{Y}))\leq \epsilon \quad\text{and}\quad \mathcal{Y}\subseteq\hat{\mathcal{Y}}_\epsilon^M.
$$

**Proof** We refer to Appendix B.2 for a complete proof. $\blacksquare$

Using a similar analysis, one could derive convergence rates for the $\epsilon$-padded union of balls estimator (Devroye and Wise, 1980; Baillo and Cuevas, 2001) that would depend on the $\epsilon$-covering number of the entire input set $D(\mathcal{X},\epsilon)$. In the general case, $D(\partial\mathcal{X},\epsilon)\leq D(\mathcal{X},\epsilon)$: Theorem 2 indicates that using a convex hull is more sample-efficient than a union of balls (assuming that $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$, see Appendix B.2 for further details). It is better suited if $\mathcal{Y}$ is convex or if an approximation of $\mathrm{H}(\mathcal{Y})$ is sufficient for the downstream application, as is usual in control applications which typically use convex reachable set approximations, see (Lew and Pavone, 2020).

### 5.2. Analysis of a particular setting: smooth input set and continuous distribution

![Figure 2](../assets/s001-lew2022simple/figure-2.png)

Figure 2: **Top**: sets $\mathcal{X}$ satisfying Assumption 4 can be non-convex, have holes, and be disconnected. **Bottom**: if $\mathcal{X}^{\mathsf{c}}$ is not $r$-convex, it is still possible to find a conservative approximation that is $r$-convex.

In many applications, the boundary of the input set is smooth (e.g., $\mathcal{X}$ is a $2$-norm ball). In this setting, we can apply Theorem 2 to derive finite-sample guarantees for general continuous sampling distributions. We state this smoothness assumption below.

**Assumption 4** $\mathcal{X}^{\mathsf{c}}$ is $r$-convex for some $r>0$. Equivalently, for any $x\in\partial\mathcal{X}$, there exists $\tilde{x}\in\mathcal{X}$ such that $x\in B(\tilde{x},r)\subseteq \mathcal{X}$.

Assumption 4 guarantees that for any parameter $x$ on the boundary $\partial\mathcal{X}$, one can find a ball of radius $r$ contained in $\mathcal{X}$ that also contains $x$, see Figure 2. This assumption corresponds to a general inwards-curvature condition of the boundary $\partial\mathcal{X}$. It is a common assumption in the literature (Walther, 1997; Rodriguez-Casal and Saavedra-Nieves, 2016, 2019; Arias-Castro et al., 2019) and is related to the notion of reach (Federer, 1959; Cuevas, 2009; Aamari, 2017) that bounds the curvature of the boundary $\partial\mathcal{X}$. To guarantee its satisfaction, one can replace $\mathcal{X}$ with $\mathcal{X}\oplus B(0,r)$ (Walther, 1997) before performing reachability analysis, which would yield a more conservative estimate of $\mathcal{Y}$. Next, we state an assumption about the sampling distribution $\mathbb{P}_\mathcal{X}$.

<!-- PDF page 7 -->

**Assumption 5** $\mathbb{P}_\mathcal{X}(A)\geq p_0\lambda(A)$ for all measurable sets $A\subset\mathcal{X}$ for some constant $p_0>0$.

This assumption states that the sampling distribution admits a lower-bounded continuous density. Specifically, there exists a density function $p_\mathcal{X}:\mathbb{R}^p\rightarrow\mathbb{R}_+$ such that $\mathbb{P}_\mathcal{X}(A) = \int_{A} p_{\mathcal{X}}(x)\mathrm{d}x\geq p_0\int_{A} \mathrm{d}x=p_0\lambda(A)$ for any measurable subset $A\subset\mathcal{X}$. For instance, the uniform distribution over $\mathcal{X}$ satisfies this assumption. Similarly to Assumption 3, this density assumption can be relaxed to neighborhoods of $\partial\mathcal{X}$; we leave this extension for future work. We obtain the following corollary.

**Corollary 1** Define the estimator $\hat{\mathcal{Y}}^M=\mathrm{H}\left(\{y_i\}_{i=1}^M\right)$, the offset vector $\boldsymbol{r}=(r,0,\dots,0)\in\mathbb{R}^p$, the volume $\Lambda_{\epsilon}^{r,L}=\lambda\big( B(0,\epsilon/(2L)) \cap B(\boldsymbol{r},r) \big)$, and the threshold $\delta_M= D(\partial\mathcal{X},\epsilon/(2L))(1 - p_0 \Lambda_{\epsilon}^{r,L})^M$. Then, under Assumptions 2, 4 and 5 and assuming that $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$, with probability at least $1-\delta_M$,

$$
d_H(\hat{\mathcal{Y}}^M, \mathrm{H}(\mathcal{Y}))\leq \epsilon \quad \text{ and }\quad\ \mathcal{Y}\subseteq\hat{\mathcal{Y}}_\epsilon^M.
$$

**Proof** We refer to Appendix B.3. We first prove that Assumptions 4 and 5 imply that Assumption 3 holds with $\Lambda_{\epsilon}^{L}=p_0\Lambda_{\epsilon}^{r,L}$. The finite-sample bound then follows by applying Theorem 2. $\blacksquare$

The constant $\Lambda_{\epsilon}^{r,L}$ corresponds to the $p$-dimensional Lebesgue volume of two hyperspherical caps and can be computed analytically, see (Li, 2011; Petitjean, 2013) and Appendix C.

### 5.3. Insights: the difficulty of reachability analysis and algorithmic design

Theorem 2 reveals which characteristics of the problem make reachability analysis challenging:

- **Assuming the smoothness of $f$ is necessary:** given an input set $\mathcal{X}$ and a sampling distribution $\mathbb{P}_{\mathcal{X}}$, one can construct problems for which sampling-based reachability analysis algorithms require arbitrarily many samples to compute an $\epsilon$-accurate approximation of $\mathcal{Y}$, see Section 6.1. To derive finite-sample rates, assuming that the reachability map $f$ is $L$-Lipschitz (Assumption 2) is necessary if only assumptions on input coverage density (Assumption 3) are available.
- **The smoother the easier**: a smaller Lipschitz constant $L$ and a larger radius parameter $r$ induce tighter bounds in Theorem 2, requiring a smaller number of samples $M$ to obtain a desired accuracy with high probability $1-\delta_M$. Indeed, such conditions guarantee a lower bound on the probability of sampling outputs $y_i=f(x_i)\in\mathcal{Y}$ that are close to the boundary $\partial\mathcal{Y}$, which is necessary to accurately reconstruct the true convex hull of the reachable set from samples.
- **Scalability**: by Theorem 2, the number of required samples to reach a desired $\epsilon$-accuracy with high probability depends on the covering number. This constant characterizes the size of the parameter space in terms of dimensionality (the number of different parameters) and volume (variations of each parameter). Given any $\mathcal{X}\in\mathcal{K}$ and $d=\sup_{x\in\partial\mathcal{X}}\|x\|$, a simple and general bound for the covering number is $D(\partial\mathcal{X},\epsilon) \leq \left( 2d\sqrt{n}/\epsilon \right)^n$ (Shalev-Shwartz and Ben-David, 2009).

## 6. Results and applications

We perform a sensitivity analysis in Section 6.1 to illustrate the insights from Theorem 2. In Section 6.2, we compute the reachable sets of a dynamical system with a simple neural network policy and compare with prior work. Finally, in Section 6.3, we embed $\epsilon$-RandUP in a model predictive control (MPC) framework to reliably control a robotic platform. Our code and hardware results are available at https://github.com/StanfordASL/RandUP and https://youtu.be/sDkblTwPuEg. All computation times are measured on a computer with a 3.70GHz Intel Core i7-8700K CPU.

<!-- PDF page 8 -->

### 6.1. Sensitivity analysis

![Figure 3](../assets/s001-lew2022simple/figure-3.png)

Figure 3: Results for the sensitivity analysis in Section 6.1. Experimental results are shown with continuous lines, theorical upper bounds with dashed lines.

We analyze the sensitivity of $\epsilon$-RandUP to the sampling distribution and the smoothness of the reachability map. We consider a $2$-dimensional input ball $\mathcal{X}=B(0,1)$ and the map $f(x)=(Lx_1,x_2)$ with $L\geq 1$. Clearly, $\mathcal{X}^{\mathsf{c}}$ is $1$-convex and $f$ is $L$-Lipschitz continuous, so Corollary 1 applies for any sampling distribution satisfying Assumption 5. We consider a distribution $\mathbb{P}_\mathcal{X}^\alpha$ that depends on a parameter $\alpha\geq 1$, such that $\mathbb{P}_\mathcal{X}^\alpha$ varies from a uniform distribution over $\mathcal{X}$ for $\alpha=1$ to a uniform distribution over the boundary $\partial\mathcal{X}$ as $\alpha\rightarrow\infty$. Given $\delta_M=10^{-3}$, we determine the minimum padding $\epsilon$ guaranteeing $\mathbb{P}( d_H( \hat{\mathcal{Y}}^M, \mathcal{Y} )\leq \epsilon )\geq 1-\delta_M$ using Corollary 1, see Appendix E.1. We take $M=1000$ samples and present results in Figure 3. We observe better performance than the predicted finite-sample bounds and that distributions with a higher probability of sampling close to the boundary (i.e., larger values of $\alpha$) perform better, corresponding to lower Hausdorff distance errors. Also, $\epsilon$-RandUP performs better on problems with smoother reachability maps, as is visible from our empirical evaluation and theoretical bounds on the Hausdorff distance. This validates the discussion in Section 5.3.

### 6.2. Verification of neural network controllers

![Figure 4](../assets/s001-lew2022simple/figure-4.png)

Figure 4: Reachable sets computed in Section 6.2 for a total prediction horizon $N=9$. Sets from the formal method ReachLP are shown in green, dashed sets correspond to no input splitting, straight-lines correspond to splitting $\mathcal{X}_0$ into $16$ components. We use $M=10^3$ samples for all sampling-based methods and $\epsilon=0.02$.

Next, we consider the verification of a neural network controller $u_t=\pi_{\mathrm{nn}}(x_t)$ for a known linear dynamical system $x_{t+1}=Ax_t+Bu_t$, where $t\in\mathbb{N}$ denotes a time index, and $x_t\in\mathbb{R}^2$ and $u_t\in\mathbb{R}$ denote the state and control input. Given a rectangular set of initial states $\mathcal{X}_0\subset\mathbb{R}^2$, the problem consists of estimating the reachable set at time $t\in\mathbb{N}$ defined as $\mathcal{X}_t=\{(A(\cdot)+B\pi_{\mathrm{nn}}(\cdot))\circ\dots\circ (Ax_0+B\pi_{\mathrm{nn}}(x_0)): x_0\in\mathcal{X}_0\}$. Defining $(\mathcal{X},\mathcal{Y})=(\mathcal{X}_0,\mathcal{X}_t)$ and $f(x)=(A(\cdot)+B\pi_{\mathrm{nn}}(\cdot))\circ\dots\circ (Ax+B\pi_{\mathrm{nn}}(x))$, we see that this problem fits the mathematical form described in Section 1. We use a ReLU network $\pi_{\mathrm{nn}}$ from (Everett et al., 2021) with two layers of $5$ neurons each. We compare $\epsilon$-RandUP with the formal method ReachLP (Everett et al., 2021)$^1$ and with two recently-derived sampling-based approaches: the kernel method proposed in (Thorpe et al., 2021)

Footnote 1: Comparisons with ReachSDP (Hu et al., 2020), which is more conservative than ReachLP, show a similar trend.

<!-- PDF page 9 -->

and GoTube (Gruenbacher et al., 2022). We implement GoTube using the $\epsilon$-RandUP algorithm where we replace the last convex hull bounding step with an outer-bounding ball. As ground-truth, we use the reachable sets from $\epsilon$-RandUP with $\epsilon=0$ and $M=10^6$, which is motivated by the asymptotic results from Theorem 1 and was previously done in (Everett et al., 2021). We refer to Appendix E.2 for details and present results in Figures 4 and 5.

![Figure 5](../assets/s001-lew2022simple/figure-5.png)

Figure 5: Neural network verification analysis in Section 6.2: we report the computation time of each algorithm and their averaged Hausdorff distance error (with $\epsilon=0$ for $\epsilon$-RandUP and GoTube) over $100$ tries when estimating $\mathcal{Y}=\mathcal{X}_4$.

**Formal methods** that explicitly bound the output of each layer of the neural network can guarantee that their reachable set approximations are always conservative. However, obtaining tight approximations with ReachLP requires splitting the input set: a computationally expensive procedure (Fig. 5, bottom). Figures 4 and 5 show that ReachLP is more conservative than $\epsilon$-RandUP even when considering polytopic outputs with eight facets. As shown in Figure 4 (right), the conservatism of these methods increases over time. This shows that even when considering small neural networks, verifying safety specifications over long horizons remains an open challenge.

**Sampling-based** approaches do not suffer from the long-horizon conservatism of formal methods. This comes at the expense of probabilistic guarantees (that rely on knowledge of the Lipschitz constant of the model), as opposed to deterministic conservatism guarantees. $\epsilon$-RandUP and GoTube have comparable computation time$^2$ and are significantly faster than other approaches. $\epsilon$-RandUP is significantly more accurate than prior work, especially for larger values of $M$. Also, the results from Theorem 2 allow for principled hyperparameter selection for $\epsilon$-RandUP: given $\epsilon=0.02$, sampling $1400$ uniformly-distributed inputs on $\partial\mathcal{X}$ is sufficient for the output sets to be conservative with probability at least $1-10^{-4}$ (for $L=1$, see Section E.2).

These experiments show that for short-horizon problems ($5$ steps) with relatively simple network architectures, both ReachLP and $\epsilon$-RandUP return accurate reachable set approximations. For longer-horizon problems ($9$ steps) with networks of moderate dimensions (which allows using existing methods to pre-compute a Lipschitz constant, see (Fazlyab et al., 2019) and Section D), $\epsilon$-RandUP is guaranteed to efficiently return non-overly-conservative reachable set approximations with high probability. Finally, though we do not present such results here, the generality of $\epsilon$-RandUP allows it to tackle complex model architectures (see (Lew et al., 2022) for experiments with longer horizons and more complex networks with uncertain weights) for which no alternative methods exist, albeit without finite-sample accuracy guarantees.

Footnote 2: Plotting the kernel-based level set estimator in (Thorpe et al., 2021) from $M$ samples requires classifying a dense grid of points. To evaluate the computation time of this method, we only account for the time to classify $M$ new samples.

### 6.3. Application to robust model predictive control

Finally, we show that $\epsilon$-RandUP can be embedded in a robust MPC formulation to reliably control a planar spacecraft system actuated by cold-gas thrusters. Its state at time $t\geq 0$ is denoted as $x_t\in\mathbb{R}^6$

<!-- PDF page 10 -->

and its control inputs are given as $u_t\in\mathbb{R}^3$. We use an auxiliary linear feedback controller (Lew et al., 2022) and an uncertain linear model $x_{t+1}=f(x_t,u_t,m,F)$ that depends on an uncertain mass $m\in[10,18]\,\mathrm{kg}$ (depending on the payload transported by the robot and the current weight of the gas tanks) and an unknown force $F=(F_x,F_y)\in[-0.015,0.015]^2\,\mathrm{N}$ that accounts for the tilt of the table. To control the system from an initial state $x_0\in\mathbb{R}^n$ to a goal region $\mathcal{X}_{\mathrm{goal}}\subset\mathbb{R}^n$ while minimizing fuel consumption and remaining in a feasible set $\mathcal{X}_{\mathrm{free}}$ (i.e., avoiding obstacles and respecting velocity bounds), we consider the following MPC formulation:

$$
\min_{(\mu,\nu)} \quad \sum_{t=1}^{N} (\mu_t-x_{\mathrm{goal}})^\top Q(\mu_t-x_{\mathrm{goal}}) + \sum_{t=1}^{N} \nu_t^\top R \nu_t, \quad \mathrm{s.t.} \quad\, \mu_0=x_0, \tag{4a}
$$

$$
\mu_{t+1} = f(\mu_t,\nu_t, \bar{m}, \bar{F}), \ \ \nu_t\in\mathcal{U}, \ \ \mathcal{X}_t(\nu) \subset \mathcal{X}_{\mathrm{free}}, \ \ \mathcal{X}_N(\nu) \subset \mathcal{X}_{\mathrm{goal}}, \ \ \ t=0, \dots,N-1. \tag{4b}
$$

where $\mu=(\mu_0,\dots,\mu_N)$ and $\nu=(\nu_0,\dots,\nu_{N-1})$ are optimization variables representing the nominal state and control trajectories, $(\bar{m},\bar{F}_x, \bar{F}_y)=(14,0,0)$ are nominal parameter values, $x_{\mathrm{goal}}\in\mathcal{X}_{\mathrm{goal}}$ is the center of the goal set, and the reachable sets $\mathcal{X}_t(\nu)\subset\mathbb{R}^n$ are defined as $\mathcal{X}_t(\nu) = \{ x_t=f(\cdot,\nu_{t-1},m,F) \circ\dots\circ f(x_0,\nu_0,m,F): \ (m,F)\in[10,18]\times[-0.015,0.015] \}$. The numerical implementation is described in (Lew and Pavone, 2020). With a Python implementation, $\epsilon=0.03$, and $M=10^3$, our MPC controller runs at $10$Hz which is sufficient for this platform and could be improved, e.g., by parallelizing computations on a GPU. We compare with a MPC baseline that does not consider uncertainty over the parameters (i.e., assumes $(m,F)\in\{14\}\times\{(0,0)\}$). As shown in Figure 6 and in the attached video, this baseline is unsafe and collides with an obstacle. In contrast, our reachability-aware controller is recursively feasible, satisfies all constraints, and allows safely reaching the goal. These experiments motivate the development of efficient reachability algorithms that can be embedded in generic control frameworks to account for uncertain parameters.

![Figure 6](../assets/s001-lew2022simple/figure-6.png)

Figure 6: Application of $\epsilon$-RandUP to safely control a free-flyer robot in a cluttered environment (left). Using a model predictive controller that does not account for the uncertain dynamics (middle) leads to unsafe behavior, colliding with an obstacle and causing the optimization problem to be infeasible at run-time (right).

## 7. Conclusion

We derived new asymptotic and finite-sample statistical guarantees for $\epsilon$-RandUP, a simple yet efficient algorithm for reachability analysis of general systems. We demonstrated its efficacy for a neural network verification task and its applicability to robust model predictive control. In future work, we will investigate tighter finite-sample bounds by leveraging further information about the smoothness of the input set boundary $\partial\mathcal{X}$. Of practical interest is investigating which sampling distributions enable better sample efficiency, interfacing $\epsilon$-RandUP with Lipschitz constant computation methods (e.g., (Fazlyab et al., 2019) for neural networks), exploring methods to scale to high-dimensional input spaces, and applying the technique to safety-aware reinforcement learning.

<!-- PDF page 11 -->

## Acknowledgments

The authors thank Robin Brown for her helpful feedback and insightful discussions about neural network verification, Edward Schmerling for his helpful comments and suggestions, and Adam Thorpe for helpful discussions about kernel methods. The NASA University Leadership Initiative (grant #80NSSC20M0163) provided funds to assist the authors with their research, but this article solely reflects the opinions and conclusions of its authors and not any NASA entity. NVIDIA provided funds to assist the authors with their research. L.J. was supported by the National Science Foundation via grant CBET-2112085.

## References

E. Aamari. *Rates of Convergence for Geometric Inference*. PhD thesis, Université Paris-Saclay, 2017.

Eddie Aamari and Clément Levrard. Stability and minimax optimality of tangential delaunay complexes for manifold reconstruction. *Discrete & Computational Geometry*, 59(4):923–971, 2018.

M. Althoff, G. Frehse, and A. Girard. Set propagation techniques for reachability analysis. *Annual Review of Control, Robotics, and Autonomous Systems*, 4(1):369–395, 2021.

E. Arias-Castro, B. Pateiro-Lopez, and A. Rodriguez-Casal. Minimax estimation of the volume of a set under the rolling ball condition. *Journal of the American Statistical Association*, 114(527):1162–1173, 2019.

A. Baillo and A. Cuevas. On the estimation of a star-shaped set. *Advances in Applied Probability*, 33(4):717–726, 2001.

J. D. Boissonnat and A. Ghosh. Manifold reconstruction using tangential delaunay complexes. *Discrete & Computational Geometry*, 51(1):221–267, 2013.

R. T. Q. Chen, Y. Rubanova, J. Bettencourt, and D. Duvenaud. Neural ordinary differential equations. In *Conf. on Neural Information Processing Systems*, 2018.

X. Chen, E. Abraham, and S. Sankaranarayanan. Flow\*: An analyzer for non-linear hybrid systems. In *Proc. Int. Conf. Computer Aided Verification*, 2013.

A. Cuevas. Set estimation: Another bridge between statistics and geometry. *Boletin de Estadistica e Investigacion Operativa*, 25(2):71–85, 2009.

E. De Vito, L. Rosasco, and A. Toigo. Learning Sets with Separating Kernels. *Applied and Computational Harmonic Analysis*, 37(2):185–217, 2014.

A. Devonport and M. Arcak. Estimating reachable sets with scenario optimization. In *Proc. of the 2nd Conference on Learning for Dynamics and Control*, 2020.

L. Devroye and G. L. Wise. Detection of abnormal behavior via nonparametric estimation of the support. *SIAM Journal on Applied Mathematics*, 38(3):480–488, 1980.

<!-- PDF page 12 -->

L. Dumbgen and G. Walther. Rates of convergence for random approximations of convex sets. *Advances in Applied Probability*, 28(2):384–393, 1996.

M. Everett, G. Habibi, S. Chuangchuang, and J. P. How. Reachability analysis of neural feedback loops. *IEEE Access*, 2021. Available at https://arxiv.org/abs/2101.01815.

M. Fazlyab, A. Robey, H. Hassani, M. Morari, and G. J. Pappas. Efficient and accurate estimation of lipschitz constants for deep neural networks. In *Conf. on Neural Information Processing Systems*, 2019.

H. Federer. Curvature measures. *Transactions of the American Mathematical Society*, (93):418–491, 1959.

A. Girard. Reachability of uncertain linear systems using zonotopes. In *Hybrid Systems: Computation and Control*, 2005.

S. Gruenbacher, M. Lechner, R. Hasani, D. Rus, T. A. Henzinger, S. Smolka, and R. Grosu. GoTube: Scalable stochastic verification of continuous-depth models. In *Proc. AAAI Conf. on Artificial Intelligence*, 2022.

B. Hanin and D. Rolnick. Deep relu networks have surprisingly few activation patterns. In *Conf. on Neural Information Processing Systems*, 2019.

R. Harman and V Lacko. On decompositional algorithms for uniform sampling from n-spheres and n-balls. *Journal of Multivariate Analysis*, 101(10):2297–2304, 2010.

H. Hu, M. Fazlyab, M. Morari, and G. J. Pappas. Reach-SDP: Reachability analysis of closed-loop systems with neural network controllers. In *Proc. IEEE Conf. on Decision and Control*, 2020.

R. Ivanov, J. Weimer, R. Alur, G. J. Pappas, and I. Lee. Verisig: verifying safety properties of hybrid systems with neural network controllers. In *Hybrid Systems: Computation and Control*, 2019.

S. Kong, S. Gao, W. Chen, and E. Clarke. dreach: $\delta$-reachability analysis for hybrid systems. In *Int. Conf. on Tools and Algorithms for the Construction and Analysis of Systems*, 2015.

A. B. Kurzhanski and P. Varaiya. Ellipsoidal techniques for reachability analysis. In *Hybrid Systems: Computation and Control*, 2000.

T. Lew and M. Pavone. Sampling-based reachability analysis: A random set theory approach with adversarial sampling. In *Conf. on Robot Learning*, 2020.

T. Lew, A. Sharma, J. Harrison, A. Bylard, and M. Pavone. Safe active dynamics learning and control: A sequential exploration-exploitation framework. *IEEE Transactions on Robotics*, 2022. In Press.

S. Li. Concise formulas for the area and volume of a hyperspherical cap. *Asian Journal of Mathematics and Statistics*, 4(1):66–70, 2011.

C. Liu, T. Arnon, C. Lazarus, C. Strong, C. Barrett, and M. J. Kochenderfer. Algorithms for verifying deep neural networks. *Foundations and Trends in Optimization*, 4(3-4):244–404, 2021.

<!-- PDF page 13 -->

G. Matheron. *Random sets and integral geometry*. Wiley Series in Probability and Mathematical Statistics, 1975.

M. Matt. How to compute the volume of intersection between two hyperspheres. Mathematics Stack Exchange, available at https://math.stackexchange.com/q/162873, 2013.

I. Molchanov. *Theory of Random Sets*. Springer-Verlag, second edition, 2017.

G. Montufar, R. Pascanu, K. Cho, and Y. Bengio. On the number of linear regions of deep neural networks. In *Conf. on Neural Information Processing Systems*, 2014.

M. Petitjean. Spheres unions and intersections and some of their applications in molecular modeling. In *Distance Geometry: Theory, Methods, and Applications*, pages 61–83. Springer New York, 2013.

B. D. Ripley and J. P. Rasson. Finding the edge of a poisson forest. *Journal of Applied Probability*, 14:483–491, 1977.

A. Rodriguez-Casal and P. Saavedra-Nieves. A fully data-driven method for estimating the shape of a point cloud. *ESAIM: Probability and Statistics*, 20(1):332–348, 2016.

A. Rodriguez-Casal and P. Saavedra-Nieves. Extent of occurrence reconstruction using a new data-driven support estimator. Available at https://arxiv.org/abs/1907.08627, 2019.

A. Rudi, E. De Vito, A. Verri, and F. Odone. Regularized Kernel Algorithms for Support Estimation. *Frontiers in Applied Mathematics and Statistics*, 3:1–15, 2017.

R. Schneider. Random approximation of convex sets. *Journal of Microscopy*, 151(3):211–227, 1988.

R. Schneider. *Convex Bodies: The Brunn-Minkowski Theory*. Cambridge Univ. Press, second edition, 2014.

B. Schürmann, N. Kochdumper, and M. Althoff. Reachset model predictive control for disturbed nonlinear systems. In *Proc. IEEE Conf. on Decision and Control*, 2018.

T. Serra, C. Tjandraatmadja, and S. Ramalingam. Bounding and counting linear regions of deep neural networks. In *Int. Conf. on Machine Learning*, 2018.

S. Shalev-Shwartz and S. Ben-David. *Understanding Machine Learning*. Cambridge University Press, 2009.

Y. S. Shao, C. Chen, S. Kousik, and R. Vasudevan. Reachability-based trajectory safeguard (RTS): A safe and fast reinforcement learning safety layer for continuous control. *IEEE Robotics and Automation Letters*, 6(2):239–261, 2021.

A. Sinha, M. O'Kelly, T. Tedrake, and J. Duchi. Neural bridge sampling for evaluating safety-critical autonomous systems. In *Conf. on Neural Information Processing Systems*, 2020.

A. J. Thorpe, K. R. Ortiz, and Oishi M. M. K. Learning approximate forward reachable sets using separating kernels. In *Proc. of the 3rd Conference on Learning for Dynamics and Control*, 2021.

<!-- PDF page 14 -->

H.-D. Tran, D. Manzanas Lopez, P. Musau, X. Yang, L. V. Nguyen, W. Xiang, and T. T. Johnson. Star-based reachability analysis of deep neural networks. In *Int. Symp. on Formal Methods*, 2019.

J. A. Vincent and M. Schwager. Reachable polyhedral marching (RPM): A safety verification algorithm for robotic systems with deep neural network components. In *Proc. IEEE Conf. on Robotics and Automation*, 2021.

G. Walther. Granulometric smoothing. *The Annals of Statistics*, 25(6):2273 – 2299, 1997.

S. Webb, T. Rainforth, Y.W. Teh, and M. P. Kumar. A statistical approach to assessing neural network robustness. In *Int. Conf. on Learning Representations*, 2019.

A. Wittig, P. Di Lizia, R. Armellin, K. Makino, Bernelli-Zazzera F., and M. Berz. Propagation of large uncertainty sets in orbital dynamics by automatic domain splitting. *Celestial Mechanics and Dynamical Astronomy*, 122:239–261, 2015.

<!-- PDF page 15 -->

## Appendix A. Formal definitions and random set theory

As a complement to Section 3, this section provides a formal description of $\epsilon$-RandUP using random set theory. Since the set estimator $\hat{\mathcal{Y}}^M_{\epsilon}$ in (2) is a random variable, describing its measurability properties is important to formally analyze its convergence properties (in an appropriate topology, which we define using the Hausdorff distance). In particular, random set theory provides a rigorous framework to characterize the probability distribution of $\hat{\mathcal{Y}}^M_{\epsilon}$ in Theorems 1 and 2.

We denote $\mathcal{K}$ for the family of nonempty compact subsets of $\mathbb{R}^n$, $\mathcal{B}(\mathbb{R}^n)$ for the Borel $\sigma$-algebra for the Euclidean topology on $\mathbb{R}^n$ associated to the usual Euclidean norm $\|\cdot\|$, $\lambda(\cdot)$ for the Lebesgue measure over $\mathbb{R}^p$, $\mathrm{H}(A)$ for the convex hull of a subset $A\subset\mathbb{R}^n$, $\oplus$ for the Minkowski sum, $B(x,r)=\{y\in\mathbb{R}^n: \|y-x\|\leq r\}$ for the closed ball of center $x\in\mathbb{R}^n$ and radius $r\geq 0$, $\mathring{B}(x,r)$ for the open ball, and $\partial A$ for the boundary of any $A\subset\mathbb{R}^n$.

### A.1. Random set theory

Our analysis hinges on the observation that the set estimator $\hat{\mathcal{Y}}_\epsilon^M$ is a random compact set, i.e., $\hat{\mathcal{Y}}_\epsilon^M$ is a random variable taking values in the family of nonempty compact sets $\mathcal{K}$. To characterize the accuracy of our estimator, we use the *Hausdorff metric*, which is defined for any $A,B\in\mathcal{K}$ in (3) as

$$
d_\mathrm{H}(A,B) = \max\big( \sup_{x\in B} \inf_{y\in A} \|x-y\|, \ \sup_{x\in A} \inf_{y\in B} \|x-y\| \big). \tag{5}
$$

This metric induces the *myopic topology* on $\mathcal{K}$ (Molchanov, 2017) with its associated generated Borel $\sigma$-algebra $\mathcal{B}(\mathcal{K})$. $(\mathcal{K},\mathcal{B}(\mathcal{K}))$ is a measurable space, which motivates the following definition:

**Definition 1 (Random compact set)** Let $(\Omega,\mathcal{G},\mathbb{P})$ be a probability space. A map $\hat{\mathcal{Y}}:\Omega\rightarrow\mathcal{K}$ is a random compact set if $\{\omega\in\Omega : \hat{\mathcal{Y}}(\omega)\in\mathscr{Y}\}\in\mathcal{G}$ for any $\mathscr{Y}\in\mathcal{B}(\mathcal{K})$.

Since a random compact set $\hat{\mathcal{Y}}$ is a random variable with values in $\mathcal{K}$, its distribution is characterized by the probability $\mathbb{P}(\hat{\mathcal{Y}}\in\mathscr{Y})$ that it takes values in a measurable subset of compact sets $\mathscr{Y}\in\mathcal{B}(\mathcal{K})$. Equivalently (Molchanov, 2017), the law of $\hat{\mathcal{Y}}$ is characterized by the capacity functional $T_{\hat{\mathcal{Y}}}:\mathcal{K}\rightarrow[0,1]$, defined for any $K\in\mathcal{K}$ as $T_{\hat{\mathcal{Y}}}(K)= \mathbb{P}(\hat{\mathcal{Y}} \cap K\neq \emptyset)$. This functional describes the probability that $\hat{\mathcal{Y}}$ intersects any compact set $K$. We will analyze this functional to prove the convergence of our set estimator in Theorems 1 and 2.

Our asymptotic convergence result in Theorem 1 relies on (Molchanov, 2017, Proposition 1.7.23), which provides sufficient conditions for the convergence of random closed sets. We restate this result in the particular case of a sequence of random compact sets.

**Theorem 3 (Convergence of Random Sets to a Deterministic Limit (Molchanov, 2017))** Let $\mathcal{Y}\in\mathcal{K}$ and let $\{\hat{\mathcal{Y}}^M\}_{M=1}^\infty$ be a sequence of random compact sets. Assume that

- For any $K\in\mathcal{K}$ such that $\mathcal{Y}\cap K=\emptyset$,

$$
\mathbb{P}(\hat{\mathcal{Y}}^M\cap K \neq \emptyset \ \text{infinitely often}) = \mathbb{P}\left(\bigcap_{N=1}^\infty\bigcup_{M=N}^\infty \{\hat{\mathcal{Y}}^M\cap K \neq \emptyset\}\right) = 0. \tag{C1}
$$

- For any open subset $G\subset\mathbb{R}^n$ such that $\mathcal{Y}\cap G \neq \emptyset$,

$$
\mathbb{P}(\hat{\mathcal{Y}}^M\cap G = \emptyset \ \text{infinitely often}) = \mathbb{P}\left(\bigcap_{N=1}^\infty\bigcup_{M=N}^\infty \{\hat{\mathcal{Y}}^M\cap G = \emptyset\}\right) = 0. \tag{C2}
$$

<!-- PDF page 16 -->

Then, the sequence of random compact sets $\{\mathcal{Y}^M\}_{M=1}^\infty$ almost surely converges to $\mathcal{Y}$ (in the myopic topology), i.e., almost surely, $d_H(\mathcal{Y}^M,\mathcal{Y})\rightarrow 0$ as $M\rightarrow\infty$.

### A.2. Sampling-based reachability analysis

As discussed in Section 3, $\epsilon$-RandUP relies on the choice of three parameters:

- a number of samples $M\in\mathbb{N}$,
- a padding constant $\epsilon>0$,
- a probability measure $\mathbb{P}_\mathcal{X}$ on $(\mathbb{R}^{p},\mathcal{B}(\mathbb{R}^{p}))$ such that $\mathbb{P}_\mathcal{X}(\mathcal{X})=1$.

This algorithm consists of sampling $M$ independent identically-distributed inputs $x_i$ according to $\mathbb{P}_\mathcal{X}$, of evaluating each output sample $y_i=f(x_i)$, and of computing the reachable set estimator $\hat{\mathcal{Y}}_\epsilon^M=\mathrm{H}\left(\{y_i\}_{i=1}^M\right)\oplus B(0,\epsilon)$ as in (2).

Formally, let $(\Omega,\mathcal{G},\mathbb{P})$ be a probability space such that the $x_i$'s are $\mathcal{G}$-measurable independent random variables which laws $\mathbb{P}_\mathcal{X}$ satisfy $\mathbb{P}_\mathcal{X}(A)=\mathbb{P}(x_i\in A)$ for any $A\in\mathcal{B}(\mathbb{R}^p)$ $^{3}$. Then, the $y_i$'s are independent random variables which laws $\mathbb{P}_{\mathcal{Y}}$ satisfy $\mathbb{P}_{\mathcal{Y}}(B)=\mathbb{P}(y_i\in B)=\mathbb{P}_\mathcal{X}(f^{-1}(B))$ for any $B\in\mathcal{B}(\mathbb{R}^n)$. It follows that $\hat{\mathcal{Y}}_\epsilon^M:\Omega\rightarrow\mathcal{K}$ is a random compact set satisfying Definition 1 $^{4}$. Intuitively, different input samples $x_i(\omega)$ induce different output samples $y_i(\omega)$, resulting in different approximated compact reachable sets $\hat{\mathcal{Y}}_\epsilon^M(\omega)\in\mathcal{K}$, where $\omega\in\Omega$.

## Appendix B. Proofs

### B.1. Proof of Theorem 1

We first restate Assumption 1 and Theorem 1 from Section 4.

**Assumption 1** $\mathbb{P}_\mathcal{X}(\{x\in\mathcal{X}: f(x)\in\mathring{B}(y,r)\})>0$ for all $y\in\partial\mathcal{Y}$ and all $r>0$.

**Theorem 1** Let $\bar{\epsilon}\geq 0$ and $(\epsilon_M)_{M\in\mathbb{N}}$ be a sequence of padding radii such that $\epsilon_M\geq 0$ for all $M\in\mathbb{N}$ and $\epsilon_M\rightarrow \bar{\epsilon}$ as $M\rightarrow\infty$. For any $\epsilon\geq 0$, define the estimator $\hat{\mathcal{Y}}^M_{\epsilon}=\mathrm{H}\left(\{y_i\}_{i=1}^M\right)\oplus B(0,\epsilon)$. Then, under Assumption 1, $\mathbb{P}$-almost surely, as $M\rightarrow\infty$,

$$
d_H(\hat{\mathcal{Y}}_{\epsilon_M}^M, \mathrm{H}(\mathcal{Y})\oplus B(0,\bar{\epsilon})) \longrightarrow 0.
$$

**Proof** Denote $\hat{\mathcal{Y}}^M=\mathrm{H}(\{y_i\}_{i=1}^M)$, so that $\hat{\mathcal{Y}}^M_{\epsilon_M}=\mathrm{H}(\{y_i\}_{i=1}^M)\oplus B(0,\epsilon_M)$.

To prove that almost surely, the sequence of random compact sets $\{\hat{\mathcal{Y}}^M_{\epsilon_M}(\omega), M\geq 1\}$ converges to $\mathrm{H}(\mathcal{Y})\oplus B(0,\bar{\epsilon})$ as $M\rightarrow\infty$, we verify the conditions (C1) and (C2) of Theorem 3.

(C1): Let $K\in \mathcal{K}$ satisfy $(\mathrm{H}(\mathcal{Y})\oplus B(0,\bar{\epsilon}))\cap K = \emptyset$. Then, since $K$ and $\mathrm{H}(\mathcal{Y})\oplus B(0,\bar{\epsilon})$ are both closed, there exists some $\epsilon>0$ such that $(\mathrm{H}(\mathcal{Y})\oplus B(0,\bar{\epsilon}+\epsilon))\cap K = \emptyset$ $^{5}$.

Next, since $\epsilon_M\rightarrow\bar{\epsilon}$ as $M\rightarrow\infty$, we have that $\bar{\epsilon}-\epsilon<\epsilon_M<\bar{\epsilon}+\epsilon$ for all $M\geq M_{\epsilon}$.

Since $y_i(\omega)\in\mathcal{Y}$ almost surely for all $i$, $\hat{\mathcal{Y}}^M\subseteq\mathrm{H}(\mathcal{Y})$ almost surely for all $M\geq M_{\epsilon}$. Thus, for any $M\geq M_{\epsilon}$, $(\hat{\mathcal{Y}}^M\oplus B(0,\epsilon_M)) \subseteq (\mathrm{H}(\mathcal{Y})\oplus B(0,\epsilon_M)) \subset (\mathrm{H}(\mathcal{Y})\oplus B(0,\bar{\epsilon}+\epsilon))$.

Footnote 3: For a canonical construction, let $\Omega=\mathbb{R}^p\times\dots\times\mathbb{R}^p$ ($M$ times), $\mathcal{G}=\mathcal{B}(\mathbb{R}^p)\otimes\dots\otimes\mathcal{B}(\mathbb{R}^p)$, $\mathbb{P}=\mathbb{P}_\mathcal{X}\otimes\dots\otimes\mathbb{P}_\mathcal{X}$ the product measure, and $x=(x_1,\dots,x_M): \Omega\rightarrow\Omega: \omega\mapsto\omega$. Then, the $x_i$ are independent and have the law $\mathbb{P}_\mathcal{X}$.

Footnote 4: Compactness of $\mathcal{X}$ and continuity of $f$ guarantee that both $\mathcal{Y}$ and $\hat{\mathcal{Y}}_\epsilon^M(\omega)$ are compact for any $\omega\in\Omega$. We refer to (Molchanov, 2017) and (Lew and Pavone, 2020) for a proof of measurability of $\hat{\mathcal{Y}}_\epsilon^M$.

Footnote 5: More generally, given $A,B\in\mathcal{K}$, then $A\cap B=\emptyset$ implies that $A\cap(B\oplus B(0,\epsilon))=\emptyset$ for some $\epsilon>0$.

<!-- PDF page 17 -->

Combined with $(\mathrm{H}(\mathcal{Y})\oplus B(0,\bar{\epsilon}+\epsilon))\cap K = \emptyset$, this implies that $(\hat{\mathcal{Y}}^M\oplus B(0,\epsilon_M))\cap K=\emptyset$ almost surely for all $M\geq M_{\epsilon}$.

Thus, $\mathbb{P}(\hat{\mathcal{Y}}^M\oplus B(0,\epsilon_M)\cap K\neq\emptyset)=0$ for all $M\geq M_{\epsilon}$.

Therefore, $\sum_{M=1}^\infty \mathbb{P}(\hat{\mathcal{Y}}^M\oplus B(0,\epsilon_M)\cap K\neq\emptyset)<\infty$. By the first Borel-Cantelli lemma, we obtain that $\mathbb{P}(\hat{\mathcal{Y}}^M\oplus B(0,\epsilon_M)\cap K \neq \emptyset \ \ i.o.) = 0$. This concludes (C1).

(C2): Let $G\subset\mathbb{R}^n$ be an open set satisfying $(\mathrm{H}(\mathcal{Y})\oplus B(0,\bar{\epsilon}))\cap G \neq \emptyset$. Equivalently, let $G\subset\mathbb{R}^n$ satisfy $\mathrm{H}(\mathcal{Y})\cap (G \oplus B(0,\bar{\epsilon}))\neq \emptyset$. We wish to prove that $\mathbb{P}(\hat{\mathcal{Y}}^M_{\epsilon_M}\cap G = \emptyset \ i.o.) = 0$.

Let $G_\partial^1,G_\partial^2\subset\mathbb{R}^n$ be two arbitrary boundary-intersecting open sets such that $\partial\mathcal{Y}\cap (G_\partial^1\oplus B(0,\bar{\epsilon})) \neq \emptyset$ and $\partial\mathcal{Y}\cap (G_\partial^2\oplus B(0,\bar{\epsilon})) \neq \emptyset$. We will select specific sets $G_\partial^j$ as a function of $G$ later in the proof.

![Figure 7](../assets/s001-lew2022simple/supplementary-figure-7.png)

Figure 7: Particular case with $\bar\epsilon=0$: for any set $G\subset\mathbb{R}^n$ that intersects $\mathrm{H}(\mathcal{Y})$ (i.e., $\mathrm{H}(\mathcal{Y})\cap G \neq \emptyset$), there exists two boundary-intersecting sets $G_\partial^1,G_\partial^2\subset\mathbb{R}^n$ (i.e. $\partial\mathrm{H}(\mathcal{Y})\cap G_\partial^j \neq \emptyset$) such that the convex hull of two points $y_1\in G_\partial^1$ and $y_2\in G_\partial^2$ intersects $G$ (i.e., $\mathrm{H}(\{y_1,y_2\})\cap G\neq \emptyset$). With this fact, we quantify the probability that $\hat{\mathcal{Y}}^M$ has at least one vertex in $G_\partial^1$ and one in $G_\partial^2$, which guarantees that $\hat{\mathcal{Y}}^M$ intersects $G$.

To prove (C2), we proceed in three steps: (C2.1) we show that sampling outputs $y_i$ within the boundary sets $G_\partial^j$ occurs infinitely often (i.o.); (C2.2) we derive a sufficient conditions for (C2) using the growth property $\hat{\mathcal{Y}}^M_\epsilon\subseteq\hat{\mathcal{Y}}^{M+1}_\epsilon$ for any fixed $\epsilon\geq 0$; (C2.3) we relate the probability of sampling $y_i$ within two well-chosen boundary-intersecting sets $G_\partial^1,G_\partial^2\subset\mathbb{R}^n$ with the probability of $\hat{\mathcal{Y}}^M_{\epsilon_M}$ to intersect $G\oplus B(0,\bar{\epsilon})$.

**(C2.1)** Consider the events $A_{2i}=\{\omega\in\Omega\,|\, y_{2i+1}\in (G_\partial^1\oplus B(0,\bar{\epsilon})), y_{2(i+1)}\in (G_\partial^2\oplus B(0,\bar{\epsilon}))\}$, where $i\in\mathbb{N}$.

Since the inputs $x_i$ are sampled independently, the outputs $y_i$ are independent. Thus, the events $\{A_{2i}\}_{i=0}^\infty$ are independent and $\mathbb{P}(A_{2i})= \mathbb{P}(y_{2i+1}\in (G_\partial^1\oplus B(0,\bar{\epsilon}))) \mathbb{P}(y_{2i+2}\in (G_\partial^2\oplus B(0,\bar{\epsilon})))$. Since $\partial\mathcal{Y}\cap (G_\partial^1\oplus B(0,\bar{\epsilon})) \neq \emptyset$ for $j=1,2$, we use Assumption 1 to obtain that $\mathbb{P}(A_{2i}) \geq \delta$ for some $\delta>0$ that depends on the choice of $\mathbb{P}_\mathcal{X}$, $G_\partial^j$, and $\bar\epsilon$. Thus, $\sum_{i=0}^\infty\mathbb{P}(A_{2i})=\infty$. Therefore, we apply the second Borel-Cantelli lemma and obtain that $\mathbb{P}\big(\bigcup_{N=0}^\infty\bigcap_{M=N}^\infty A_{2M}\big) = 1$.

Next, since $\bigcap_{N=0}^\infty A_n \subseteq A_0$ for any events $A_i$, $\mathbb{P}\big(\bigcup_{N=0}^\infty\bigcap_{M=N}^\infty A_{2M}\big) \leq \mathbb{P}\big(\bigcup_{M=0}^\infty A_{2M}\big)$. Combining the last two results,

$$
\mathbb{P} \bigg( \bigcup_{M=0}^\infty (y_{2M+1}\in (G_\partial^1\oplus B(0,\bar{\epsilon}))) \cap (y_{2M+2}\in (G_\partial^2\oplus B(0,\bar{\epsilon}))) \bigg) = 1. \tag{6}
$$

(C2.2) To proceed with this step, we first observe the following.

$G$ satisfies $\mathrm{H}(\mathcal{Y})\cap (G\oplus B(0,\bar{\epsilon}))\neq \emptyset$. Therefore, since $\mathrm{H}(\mathcal{Y})$ is compact and $G$ is open, there exists

<!-- PDF page 18 -->

some $\epsilon>0$ such that $\mathrm{H}(\mathcal{Y})\cap (G\oplus B(0,\bar{\epsilon}-\epsilon))\neq \emptyset$. $^{6}$

Since $\epsilon\rightarrow\bar{\epsilon}$ as $M\rightarrow\infty$, there exists some $M_\epsilon\in\mathbb{N}$ such that $\bar{\epsilon}-\epsilon<\epsilon_M<\bar{\epsilon}+\epsilon$ for all $M\geq M_\epsilon$.

Second, we rewrite (C2) as

$$
\mathbb{P}(\hat{\mathcal{Y}}^M_{\epsilon_M}\cap G = \emptyset \ \ i.o.) = \mathbb{P}\bigg(\bigcap_{N=1}^\infty\bigcup_{M=N}^\infty \hat{\mathcal{Y}}^M_{\epsilon_M}\cap G = \emptyset\bigg) = 1 - \mathbb{P}\bigg(\bigcup_{N=1}^\infty\bigcap_{M=N}^\infty \hat{\mathcal{Y}}^M_{\epsilon_M}\cap G \neq \emptyset\bigg).
$$

Next, note that

$$
\mathbb{P}\bigg(\bigcup_{N=1}^\infty\bigcap_{M=N}^\infty \hat{\mathcal{Y}}^M_{\epsilon_M}\cap G \neq \emptyset\bigg) \geq \mathbb{P}\bigg(\bigcup_{N=M_\epsilon}^\infty\bigcap_{M=N}^\infty \hat{\mathcal{Y}}^M_{\epsilon_M}\cap G\neq \emptyset\bigg) \geq \mathbb{P}\bigg( \bigcup_{N=M_\epsilon}^\infty \bigcap_{M=N}^\infty \hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq \emptyset\bigg).
$$

The second inequality holds since $\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\subset \hat{\mathcal{Y}}^M_{\epsilon_M}$ if $M\geq M_\epsilon$.

Next, since $\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\subseteq\hat{\mathcal{Y}}^{M+1}_{\bar{\epsilon}-\epsilon}$ for any $M\in\mathbb{N}$, we have that $\{\omega\in\Omega\, |\, \bigcap_{M=N}^\infty \hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq \emptyset\} = \{\omega\in\Omega \, |\, \hat{\mathcal{Y}}^N_{\bar{\epsilon}-\epsilon}\cap G \neq \emptyset\}$. Thus,

$$
\mathbb{P}\bigg(\bigcup_{N=M_{\epsilon}}^\infty\bigcap_{M=N}^\infty \hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq \emptyset\bigg)=\mathbb{P}\bigg(\bigcup_{M=M_\epsilon}^\infty\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq \emptyset\bigg).
$$

Combining the last three results, we obtain the following sufficient condition for (C2)

$$
\mathbb{P}\bigg(\bigcup_{M=M_\epsilon}^\infty\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq \emptyset\bigg) = 1 \implies \mathbb{P}(\hat{\mathcal{Y}}^M_{\epsilon_M}\cap G = \emptyset \ \ i.o.) = 0 . \tag{7}
$$

(C2.3) Finally, we combine (6) and (7) as follows. For $M\geq 0$, we have that

$$
\begin{aligned}
&\{ \omega\in\Omega: (y_{2M+1}(\omega)\in (G_\partial^1\oplus B(0,\bar{\epsilon}))) \cap (y_{2M+2}(\omega)\in (G_\partial^2\oplus B(0,\bar{\epsilon}))) \} \\
&\qquad\subseteq \{\omega\in\Omega \,|\, (\hat{\mathcal{Y}}^{2M+2}_{\bar{\epsilon}-\epsilon}(\omega)\cap (G_\partial^1\oplus B(0,\bar{\epsilon}))\neq\emptyset) \cap (\hat{\mathcal{Y}}^{2M+2}_{\bar{\epsilon}-\epsilon}(\omega)\cap (G_\partial^2\oplus B(0,\bar{\epsilon}))\neq\emptyset) \}
\end{aligned}
$$

Thus,

$$
\begin{aligned}
&\bigcup_{M=0}^\infty \{\omega\in\Omega: (y_{2M+1}(\omega)\in (G_\partial^1\oplus B(0,\bar{\epsilon})))\cap (y_{2M+2}(\omega)\in (G_\partial^2\oplus B(0,\bar{\epsilon})))\} \\
&\quad\subseteq \bigcup_{M=2}^\infty \{\omega\in\Omega \,|\, (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}(\omega)\cap G_\partial^1\neq\emptyset) \cap (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}(\omega)\cap G_\partial^2\neq\emptyset) \} \\
&\quad\subseteq \bigcup_{M=1}^\infty \{\omega\in\Omega \,|\, (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}(\omega)\cap G_\partial^1\neq\emptyset) \cap (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}(\omega)\cap G_\partial^2\neq\emptyset) \}.
\end{aligned}
$$

From (6), the first event holds with probability one. Therefore, by the above,

$$
\mathbb{P}\left( \bigcup_{M=M_\epsilon}^\infty (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G_\partial^1\neq\emptyset) \cap (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G_\partial^2\neq\emptyset) \right)=1.
$$

Footnote 6: More generally, given $A\subset\mathcal{K}$ and $B\subset\mathbb{R}^n$ an open set, then $A\cap B \neq\emptyset\implies A\cap(B\ominus B(0,\epsilon))\neq\emptyset$ for some $\epsilon>0$.

<!-- PDF page 19 -->

Given the right choice of $G_\delta^1,G_\delta^2$, by convexity of $\mathrm{H}(\mathcal{Y})$ $^{7}$ (see also Figure 7), we have that

$$
\mathbb{P}\left(\bigcup_{M=M_\epsilon}^\infty \hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq\emptyset\right)\geq \mathbb{P}\left( \bigcup_{M=M_\epsilon}^\infty (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G_\partial^1\neq\emptyset) \cap (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G_\partial^2\neq\emptyset) \right) =1.
$$

Therefore, $\mathbb{P}\left(\bigcup_{M=M_\epsilon}^\infty \hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq\emptyset\right)=1$. Combining this result with (7), we obtain that $\mathbb{P}(\hat{\mathcal{Y}}^M_{\epsilon_M}\cap G = \emptyset \ i.o.) = 0$. This conludes the proof of (C2).

By Theorem 3, we conclude that almost surely, the sequence $\{\hat{\mathcal{Y}}^M_{\epsilon_M}(\omega),m\geq 1\}$ converges to $\mathrm{H}(\mathcal{Y})\oplus B(0,\bar{\epsilon})$ as $M\rightarrow\infty$. This concludes the proof of Theorem 1. $\blacksquare$

Footnote 7: $\mathrm{H}(\mathcal{Y})\oplus B(0,\bar\epsilon)$ is convex, so that any $y\in G\cap (\mathrm{H}(\mathcal{Y})\oplus B(0,\bar\epsilon))\neq\emptyset$ lies on a line passing through two extreme points $z_1^y,z_2^y$ of $\mathrm{H}(\mathcal{Y})\oplus B(0,\bar\epsilon)$. For some $\tilde\epsilon>0$, let $G_\partial^1=\mathring{B}_\partial^1(z_1^y,\tilde\epsilon)$ and $G_\partial^2=\mathring{B}_\partial^2(z_2^y,\tilde\epsilon)$ (note that $G_\partial^1,G_\partial^2$ intersect $\mathrm{H}(\mathcal{Y})\oplus B(0,\bar\epsilon)$). Then, by choosing $\tilde\epsilon$ small enough, since $\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}$ is convex, the inequality follows since $\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}$ necessarily intersects $G$ if it intersects $G_\partial^1$ and $G_\partial^2$.

### B.2. Proof of Theorem 2

We start with four intermediate results and then prove Theorem 2. We use the notations introduced in Section A throughout this section.

**Lemma 2** Under Assumption 2 and assuming that $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$,

$$
D(\partial\mathcal{Y},\epsilon)\leq D(\partial\mathcal{X},\epsilon/L).
$$

**Lemma 3** Under Assumption 2, for any $x\in\mathbb{R}^p$, $y=f(x)$, and any $\delta>0$,

$$
\mathbb{P}_\mathcal{Y}\big(B(y,\delta)\big) \geq \mathbb{P}_\mathcal{X}\big(B(x,\epsilon)\big) \quad \text{for all }\ \epsilon\in [0,\delta/L].
$$

**Lemma 4** Let $\epsilon>0$ and define

$$
Y_\epsilon^M = \bigcup_{i=1}^{M} \, B(y_i,\epsilon), \qquad \pi(\partial\mathcal{Y},Y_\epsilon^M) = \sup_{y\in\partial\mathcal{Y}}\mathbb{P}(\{y\} \cap Y_\epsilon^M = \emptyset).
$$

Then,

$$
\mathbb{P}(\partial\mathcal{Y}\subset Y_{2\epsilon}^M) \geq 1 - D(\partial\mathcal{Y},\epsilon) \pi(\partial\mathcal{Y},Y_\epsilon^M).
$$

**Lemma 5** Let $\epsilon\geq 0$ and let $Y\in\mathcal{K}$ be such that $\partial\mathcal{Y}\subseteq Y\oplus B(0,\epsilon)$ and $Y\subseteq \mathcal{Y}$. Then, $d_H( \mathrm{H}(Y), \mathrm{H}(\mathcal{Y}) )\leq \epsilon$.

Lemma 4 is the key to deriving Theorem 2. It is first derived in (Dumbgen and Walther, 1996) in the convex problem setting. Notably, Lemma 4 does not require the convexity of $\mathcal{Y}$.

**Proof of Lemma 2.** First, note that since $\mathcal{X}$ is compact and $\partial\mathcal{X}\subseteq\mathcal{X}$, $\partial\mathcal{X}$ is compact (note that the boundary is always closed). Any compact set has a finite covering number, thus $D(\partial\mathcal{X}, \epsilon)$ is finite for any finite $\epsilon>0$. Second, given any $\delta>0$, any $x\in\mathcal{X}$, and $y=f(x)$,

$$
f(B(x,\epsilon)) \subseteq B(y,\delta) \quad \forall \epsilon\in[0,\delta/L], \tag{8}
$$

<!-- PDF page 20 -->

where $L$ is the Lipschitz constant in Assumption 2. Indeed, let $\tilde{x}\in B(x,\epsilon)$, so that $\|\tilde{x}-x\|\leq\epsilon$. Then, $\|f(\tilde{x})-y\| \leq L\,\|\tilde{x}-x\|\leq L\epsilon\leq\delta$ where the last inequality holds given that $\epsilon \leq \delta/L$.

Next, let $F_{\partial\mathcal{X}}=\{x_i\}_{i=1}^{|F_{\partial\mathcal{X}}|}\subseteq\partial\mathcal{X}$ be a minimum $(\epsilon/L)$-covering for $\partial\mathcal{X}$, so that $|F_{\partial\mathcal{X}}|=D(\partial\mathcal{X},\epsilon/L)$ and for any $x\in\partial\mathcal{X}$, there exists $x_i\in F_{\partial\mathcal{X}}$ such that $\|x-x_i\|\leq \epsilon/L$. Then, $F_{\partial\mathcal{Y}}=\{f(x_i)\, |\,x_i\in F_{\partial\mathcal{X}} \}$ is an $\epsilon$-covering for $\partial\mathcal{Y}$. Indeed, for any $y\in\partial\mathcal{Y}$, there exists some $x\in\partial\mathcal{X}$ such that $y=f(x)$, and there exists some $x_i\in F_{\partial\mathcal{X}}$ such that $\|x-x_i\|\leq \epsilon/L$. Therefore,

$$
\sup_{y_i\in F_{\partial\mathcal{Y}}} \|y-y_i\| = \sup_{x_i\in F_{\partial\mathcal{X}}} \|f(x)-f(x_i)\| \leq \sup_{x_i\in F_{\partial\mathcal{X}}} L\|x-x_i\| \leq \epsilon.
$$

Therefore, since $F_{\partial\mathcal{Y}}$ is an $\epsilon$-covering for $\partial\mathcal{Y}$ and $|F_{\partial\mathcal{Y}}|=|F_{\partial\mathcal{X}}|=D(\partial\mathcal{X},\epsilon/L)$, we obtain that $D(\partial\mathcal{Y},\epsilon)\leq |F_{\partial\mathcal{Y}}| = D(\partial\mathcal{X},\epsilon/L)$ which concludes this proof. $\blacksquare$

**Proof of Lemma 3.** From (8), given any $\delta>0$, $x\in\mathbb{R}^p$, and $y=f(x)$, $f(B(x,\epsilon)) \subset B(y,\delta)$ for any $\epsilon\in[0,\delta/L]$. Thus,

$$
\mathbb{P}_{\mathcal{Y}}(B(y,\delta)) = \mathbb{P}_\mathcal{X}\Big(f^{-1}(B(y,\delta))\Big) \geq \mathbb{P}_\mathcal{X}\left( B(x,\epsilon) \right) \quad \forall \epsilon\in[0,\delta/L],
$$

where the last inequality holds since $B(x,\epsilon) \subseteq f^{-1}(B(y,\delta))$, which concludes this proof. $\blacksquare$

**Proof of Lemma 4.** Let $F_{\partial\mathcal{Y}}=\{y_i\}_{i=1}^{|F_{\partial\mathcal{Y}}|}\subseteq\partial\mathcal{Y}$ be a minimum $\epsilon$-covering for $\partial\mathcal{Y}$, so that $|F_{\partial\mathcal{Y}}|=D(\partial\mathcal{Y},\epsilon)$ and for any $y\in\partial\mathcal{Y}$, there exists $y_i\in F_{\partial\mathcal{Y}}$ such that $\|y-y_i\|\leq \epsilon$. Let $B(F_{\partial\mathcal{Y}},\epsilon)=\bigcup_{y_i\in F_{\partial\mathcal{Y}}} B(y_i,\epsilon)$.

By construction, $\partial\mathcal{Y}\subset B(F_{\partial\mathcal{Y}},\epsilon)$, so that $\partial\mathcal{Y}\nsubseteq Y_{2\epsilon}^M\implies B(F_{\partial\mathcal{Y}},\epsilon)\nsubseteq Y_{2\epsilon}^M$. Thus,

$$
\begin{aligned}
\mathbb{P}(\partial\mathcal{Y}\nsubseteq Y_{2\epsilon}^M) &\leq \mathbb{P}(B(F_{\partial\mathcal{Y}},\epsilon)\nsubseteq Y_{2\epsilon}^M) = \mathbb{P}(F_{\partial\mathcal{Y}}\nsubseteq Y_\epsilon^M) \\
&= \mathbb{P}\bigg(\bigcup_{y_i\in F_{\partial\mathcal{Y}}} y_i\notin Y_\epsilon^M\bigg) \\
&\leq \sum_{y_i\in F_{\partial\mathcal{Y}}}\mathbb{P}(y_i\notin Y_\epsilon^M) = \sum_{y_i\in F_{\partial\mathcal{Y}}} \mathbb{P}(\{y_i\}\cap Y_\epsilon^M = \emptyset) \\
&\leq |F_{\partial\mathcal{Y}}| \cdot \sup_{y\in\partial\mathcal{Y}}\mathbb{P}(\{y\}\cap Y_{\epsilon}^M = \emptyset) \\
&\leq D(\partial\mathcal{Y},\epsilon)\pi(\partial\mathcal{Y},Y_{\epsilon}^M).
\end{aligned}
$$

The conclusion follows. $\blacksquare$

**Proof of Lemma 5.** $\partial\mathcal{Y}\subseteq Y\oplus B(0,\epsilon)$ implies that $\mathrm{H}(\mathcal{Y})=\mathrm{H}(\partial\mathcal{Y})\subseteq \mathrm{H}(Y\oplus B(0,\epsilon))=\mathrm{H}(Y)\oplus B(0,\epsilon)$.

$Y\subseteq \mathcal{Y}$ implies that $\mathrm{H}(Y)\subseteq \mathrm{H}(\mathcal{Y})\subset\mathrm{H}(\mathcal{Y})\oplus B(0,\epsilon)$.

Together, $\mathrm{H}(\mathcal{Y})\subset\mathrm{H}(Y)\oplus B(0,\epsilon)$ and $\mathrm{H}(Y)\subset\mathrm{H}(\mathcal{Y})\oplus B(0,\epsilon)$ imply that $d_H( \mathrm{H}(Y), \mathrm{H}(\mathcal{Y}) )\leq \epsilon$, see (Schneider, 2014). $\blacksquare$

With these results, we prove Theorem 2 below. We first restate it for better readability.

**Theorem 2** Define the probability threshold $\delta_M= D(\partial\mathcal{X},\epsilon/(2L))\left(1 - \Lambda_{\epsilon}^{L} \right)^M$ and the estimator $\hat{\mathcal{Y}}^M=\mathrm{H}\left(\{y_i\}_{i=1}^M\right)$. Then, under Assumptions 2 and 3 and assuming that $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$,

$$
\mathbb{P}( d_H( \hat{\mathcal{Y}}^M, \mathrm{H}(\mathcal{Y}) )\leq \epsilon )\geq 1-\delta_M \qquad\text{and}\qquad \mathbb{P}(\mathcal{Y}\subseteq\hat{\mathcal{Y}}_\epsilon^M)\geq 1-\delta_M.
$$

<!-- PDF page 21 -->

**Remark:** the assumption $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$ holds if the reachability map $f$ is open, e.g., if it is a submersion (its differential is surjective). If $\partial\mathcal{Y}\nsubseteq f(\partial\mathcal{X})$, then one could modify Theorem 2 by replacing Assumption 3 with "*Given $\epsilon,L>0$, there exists $\Lambda_{\epsilon}^{L}>0$ such that $\mathbb{P}_\mathcal{X}\left(B\left(x,\frac{\epsilon}{2L}\right)\right)\geq \Lambda_{\epsilon}^{L}$ for all $x\in\mathcal{X}$*" (i.e., one should sample over the entire set $\mathcal{X}$ and not only along the boundary) and by defining $\delta_M=D(\mathcal{X},\epsilon/(2L))(1 - \Lambda_{\epsilon}^{L})^M$.

**Proof** As in Lemma 4, define $Y_\epsilon^M = \bigcup_{i=1}^M B(y_i,\epsilon)$, $Y^M=\{y_i\}_{i=1}^M$, and

$$
\pi(\partial\mathcal{Y},Y_\epsilon^M) = \sup_{y\in\partial\mathcal{Y}}\mathbb{P}(\{y\} \cap Y_\epsilon^M = \emptyset) = \sup_{y\in\partial\mathcal{Y}}\mathbb{P}(B(y,\epsilon) \cap Y^M = \emptyset),
$$

which corresponds to the worst probability over $y\in\partial\mathcal{Y}$ of not sampling some $y_i$ that is $\epsilon$-close to $y$. First, we derive a bound for $\pi(\partial\mathcal{Y},Y_\epsilon^M)$. Using the fact that the samples $y_i$ are i.i.d.,

$$
\begin{aligned}
\pi(\partial\mathcal{Y},Y_\epsilon^M) &= \sup_{y\in\partial\mathcal{Y}}\mathbb{P}(B(y,\epsilon) \cap Y^M = \emptyset) \\
&= \sup_{y\in\partial\mathcal{Y}}\mathbb{P}\left(\bigcap_{i=1}^M (y_i\notin B(y,\epsilon))\right) \\
&= \left(1 - \inf_{y\in\partial\mathcal{Y}}\mathbb{P}(y_i\in B(y,\epsilon)) \right)^M \\
&=\left(1 - \inf_{y\in\partial\mathcal{Y}}\mathbb{P}_\mathcal{Y}(B(y,\epsilon)) \right)^M.
\end{aligned}
$$

From Lemma 3, for any $x\in\mathbb{R}^p$, $y=f(x)$, and $\epsilon>0$, $\mathbb{P}_\mathcal{Y}(B(y,\epsilon)) \geq \mathbb{P}_\mathcal{X}(B(x,\epsilon/L))$. Since for all $y\in\partial\mathcal{Y}$, there exists $x\in\partial\mathcal{X}$ such that $y=f(x)$, we combine the two previous results to obtain

$$
\pi(\partial\mathcal{Y},Y_\epsilon^M) \leq \left(1 - \inf_{x\in\partial\mathcal{X}}\mathbb{P}_\mathcal{X}(B(x,\epsilon/L)) \right)^M.
$$

In particular, using Assumption 3,

$$
\pi(\partial\mathcal{Y},Y_{\epsilon/2}^M) \leq \left(1 - \inf_{x\in\partial\mathcal{X}}\mathbb{P}_\mathcal{X}(B(x,\epsilon/(2L))) \right)^M \leq \left(1 - \Lambda_{\epsilon}^{L} \right)^M.
$$

To complete the proof of Theorem 2, we use Lemma 4 which states that

$$
\mathbb{P}(\partial\mathcal{Y}\subseteq Y_\epsilon^M) \geq 1 - D(\partial\mathcal{Y},\epsilon/2) \pi(\partial\mathcal{Y},Y_{\epsilon/2}^M) .
$$

Using Lemma 2, $D(\partial\mathcal{Y},\epsilon/2)\leq D(\partial\mathcal{X},\epsilon/(2L))$.

By Lemma 5, if $\partial\mathcal{Y}\subseteq Y_\epsilon^M$ and $Y^M\subseteq\mathcal{Y}$ $^{8}$, then $d_H( \mathrm{H}(Y^M), \mathrm{H}(\mathcal{Y}) )\leq \epsilon$ .

Therefore, with $\hat{\mathcal{Y}}^M=\mathrm{H}(Y^M)$ and Assumption 3, combining the last inequalities,

$$
\begin{aligned}
\mathbb{P}( d_H( \hat{\mathcal{Y}}^M, \mathrm{H}(\mathcal{Y}) )\leq \epsilon ) &\geq \mathbb{P}\left(\partial\mathcal{Y}\subseteq Y_\epsilon^M\right) \\
&\geq 1 - D(\partial\mathcal{Y},\epsilon/2) \pi(\partial\mathcal{Y},Y_{\epsilon/2}^M) \\
&\geq 1 - D(\partial\mathcal{X},\epsilon/(2L)) \left(1 - \Lambda_{\epsilon}^{L} \right)^M.
\end{aligned}
$$

If $d_H( \hat{\mathcal{Y}}^M, \mathrm{H}(\mathcal{Y}) )\leq \epsilon$, then $\mathcal{Y}\subseteq\mathrm{H}(\mathcal{Y})\subseteq \hat{\mathcal{Y}}^M\oplus B(0,\epsilon)=\hat{\mathcal{Y}}_\epsilon^M$. The conclusion follows. $\blacksquare$

Footnote 8: Since $\mathbb{P}_\mathcal{X}(\mathcal{X})=1$, we have that $\mathbb{P}_\mathcal{Y}(\mathcal{Y})=1$, so that $Y^M\subseteq\mathcal{Y}$ with probability one.

<!-- PDF page 22 -->

### B.3. Proof of Corollary 1

We start with the following preliminary result:

**Lemma 6** Assume that $\mathcal{X}^{\mathsf{c}}$ is $r$-convex (Assumption 4). Define $\boldsymbol{r}=(r,0,\dots,0)\in\mathbb{R}^p$. Then, for any $\epsilon\geq 0$,

$$
\inf_{x\in\partial\mathcal{X}}\lambda(\mathcal{X} \cap B(x,\epsilon)) \geq \lambda\big( B(0,\epsilon) \cap B(\boldsymbol{r},r) \big).
$$

**Proof of Lemma 6.** By Assumption 4, $\mathcal{X}^{\mathsf{c}}$ is $r$-convex. Thus, for any $x\in\partial\mathcal{X}$, there exists some $\tilde{x}\in\mathrm{Int}(\mathcal{X})$ and a (closed) ball $B(\tilde{x},r)$ such that $x\in B(\tilde{x},r)$ and $B(\tilde{x},r)\subseteq\mathcal{X}$. Since $x\in\partial\mathcal{X}$ and $B(\tilde{x},r)\subseteq\mathcal{X}$, $\|x-\tilde{x}\|=r$.

Let $\epsilon\geq 0$ and $\boldsymbol{r}=(r,0,\dots,0)\in\mathbb{R}^p$. Then, by translational and rotational invariance of the Lebesgue measure,

$$
\lambda(\mathcal{X} \cap B(x,\epsilon)) \geq \lambda\big( B(\tilde{x},r) \cap B(x,\epsilon) \big) = \lambda\big( B(x-\tilde{x},r) \cap B(0,\epsilon) \big) = \lambda\big( B(\boldsymbol{r},r) \cap B(0,\epsilon) \big)
$$

As this holds for $x\in\partial\mathcal{X}$, we obtain that $\inf_{x\in\partial\mathcal{X}}\lambda(\mathcal{X} \cap B(x,\epsilon)) \geq \lambda\big( B(0,\epsilon) \cap B(\boldsymbol{r},r) \big)$. $\blacksquare$

Then, we restate Corollary 1 and prove it below.

**Corollary 1** Define the estimator $\hat{\mathcal{Y}}^M=\mathrm{H}\left(\{y_i\}_{i=1}^M\right)$, the offset vector $\boldsymbol{r}=(r,0,\dots,0)\in\mathbb{R}^p$, the volume $\Lambda_{\epsilon}^{r,L}=\lambda\big( B(0,\epsilon/(2L)) \cap B(\boldsymbol{r},r) \big)$, and the threshold $\delta_M= D(\partial\mathcal{X},\epsilon/(2L))\big(1 - p_0 \Lambda_{\epsilon}^{r,L} \big)^M$. Then, under Assumptions 2, 4 and 5 and assuming that $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$,

$$
\mathbb{P}( d_H( \hat{\mathcal{Y}}^M, \mathrm{H}(\mathcal{Y}) )\leq \epsilon )\geq 1-\delta_M, \qquad \text{ and }\qquad\ \mathbb{P}(\mathcal{Y}\subseteq\hat{\mathcal{Y}}_\epsilon^M)\geq 1-\delta_M.
$$

**Proof of Corollary 1.** We prove that Assumptions 4 and 5 imply Assumption 3 with $\Lambda_{\epsilon}^{L}=p_0\Lambda_{\epsilon}^{r,L}$, where $\Lambda_{\epsilon}^{r,L}=\lambda\big( B(0,\epsilon/(2L)) \cap B(\boldsymbol{r},r) \big)$. The result then follows by applying Theorem 2.

Specifically, we must prove that $\mathbb{P}_\mathcal{X}(B(x,\epsilon/(2L)))\geq \Lambda_{\epsilon}^{L}$ for all $x\in\partial\mathcal{X}$.

From Assumption 5, $\mathbb{P}_\mathcal{X}(A)\geq p_0\lambda(A)$ for all $A\in\mathcal{B}(\mathcal{X})$ for some constant $p_0>0$.

Since $\mathbb{P}_\mathcal{X}(\mathcal{X})=1$ (Assumption 5), $\mathbb{P}_\mathcal{X}(B(x,\epsilon/(2L))) = \mathbb{P}_\mathcal{X}(\mathcal{X}\cap B(x,\epsilon/(2L)))$ for any $x\in\mathbb{R}^n$.

Therefore, for all $x\in\partial\mathcal{X}$, $\mathbb{P}_\mathcal{X}(B(x,\epsilon/(2L))) = \mathbb{P}_\mathcal{X}(\mathcal{X}\cap B(x,\epsilon/(2L))) \geq p_0 \lambda(\mathcal{X}\cap B(x,\epsilon/(2L)))$.

From Assumption 4 and Lemma 6, we obtain $\mathbb{P}_\mathcal{X}(B(x,\epsilon/(2L))) \geq p_0 \lambda\big( B(0,\epsilon/(2L)) \cap B(\boldsymbol{r},r) \big)$ for all $x\in\partial\mathcal{X}$ with $\boldsymbol{r}=(r,0,\dots,0)\in\mathbb{R}^p$. This concludes the proof of Corollary 1. $\blacksquare$

## Appendix C. Volume of the intersection of two hyperspheres

For completeness, we describe the computation of the constant $\Lambda_{\epsilon}^{r,L}=\lambda\big( B(0,\epsilon/(2L)) \cap B(\boldsymbol{r},r) \big)$ in Theorem 2 based on the results in (Li, 2011; Petitjean, 2013; Matt, 2013). Given $r>0$, $a\in\mathbb{R}$, and the incomplete beta function $I_x(a,b)=\Gamma(a+b)(\Gamma(a)\Gamma(b))^{-1}\int_0^x t^{a-1}(1-t)^{b-1}\mathrm{d}t$, we define

$$
V(r,a)=\begin{cases}
\frac{\pi^{p/2}}{2\Gamma(\frac{p}{2}+1)}r^n I_{1-a^2/r^2}\left(\frac{n+1}{2},\frac{1}{2}\right)\ &\text{if }a\geq 0, \\
\frac{\pi^{p/2}}{2\Gamma(\frac{p}{2}+1)}r^n(2-I_{1-a^2/r^2}\left(\frac{n+1}{2},\frac{1}{2}\right)) \ &\text{otherwise.}
\end{cases}
$$

Let $c_1=\frac{(\epsilon/(2L))^2}{2r}$ and $c_1=\frac{2r^2-(\epsilon/(2L))^2}{2r}$. Then, $\Lambda_{\epsilon}^{r,L} = V(\epsilon/(2L),c_1) + V(r,c_2)$.

<!-- PDF page 23 -->

## Appendix D. Computing the Lipschitz constant of a ReLU network from samples

In this section, we show that sampling gradients enables obtaining the Lipschitz constant of a neural network with ReLU activation functions with high probability. Consider a feed-forward ReLU neural network $f:\mathbb{R}^n\rightarrow\mathbb{R}^n$ with $\ell\in\mathbb{N}$ layers, given as

$$
f(x) = W^\ell x^\ell + b^\ell, \quad x^{k+1}=\phi^k(W^kx^k+b^k), \ k=0,\dots,\ell-1, \quad x^0 = x,
$$

where $(W^k,b^k)_{k=0}^\ell$ are the network weights and biases, and each $\phi^k:\mathbb{R}^{n_k}\rightarrow\mathbb{R}^{n_{k+1}}$ is defined as $\phi^k(x)=(\varphi(x_1),\dots,\varphi(x_{n_k}))$ with $\varphi(z)=\max(0,z)$. Note that $f$ is piecewise-affine.

Let $\mathcal{X}\subset\mathbb{R}^n$ be a non-empty compact set. Let $\mathcal{A}=\{A_1,\dots,A_N\}$ be the set of all polytopes $A_i\subseteq\mathcal{X}$ where $f|_{A_i}$ is affine, which we call the activation regions of $f$. Let $\Lambda_N=\frac{\min_{i=1,\dots,N} \lambda(A_i)}{\lambda(\mathcal{X})}$ be the smallest (normalized Lebesgue) volume of all activation regions. Note that $f$ is Lipschitz continuous over $\mathcal{X}$, since it is continuous and restricted to a compact subset. Thus, for some $L\geq 0$,

$$
\|f(x_1)-f(x_2)\|\leq L\|x_1-x_2\|\quad \forall x_1,x_2\in\mathcal{X}.
$$

Further, since $f$ is piecewise-affine, $f$ is $L$-Lipschitz continuous with

$$
L=\max_{i=1,\dots,N} \{\|\nabla f(x_i)\|\ \text{for some }x_i\in A_i\}.
$$

We propose the following sampling-based method to recover the Lipschitz constant $L$:

1. Draw $M$ random samples $x_i$ in $\mathcal{X}$ according to the uniform probability measure over $\mathcal{X}$.
2. Evaluate $L_i=\|\nabla f(x_i)\|$ for all $i=1,\dots,M$.
3. Set $\hat{L}=\max_{i=1,\dots,M} L_i$.

In general, with this approach, providing statistical guarantees on whether $\hat{L}$ is a valid Lipschitz constant for $f$ is challenging; the analysis would rely on the Hessian of $f$ which is a-priori unknown. In this specific setting, $f$ is piecewise-affine, which we leverage in the analysis below.

**Lemma 7** With the previous notations, define $\delta_M=N(1-\Lambda_N)^M$. Then,

$$
\mathbb{P}(f\text{ is $\hat{L}$-Lipschitz continuous over $\mathcal{X}$})\geq 1-\delta_M.
$$

**Proof** Since $L=\max_{i=1,\dots,N} \{\|\nabla f(x_i)\|\ \text{for some }x_i\in A_i\}$, a sufficient condition for $f$ to be $\hat{L}$-Lipschitz continuous is that at least one point $x_j$ was sampled in each region $A_i$. Thus,

$$
\begin{aligned}
\mathbb{P}\left( \bigcap_{i=1}^N\left\{ \bigcup_{j=1}^M \{x_j\}\cap A_i\neq\emptyset \right\} \right) &= 1- \mathbb{P}\left( \bigcup_{i=1}^N\left\{ \bigcup_{j=1}^M \{x_j\}\cap A_i\neq\emptyset \right\}^{\mathsf{c}} \right) \\
&\geq 1- \sum_{i=1}^N \mathbb{P}\left( \bigcap_{j=1}^M x_j\notin A_i \right) \quad\text{(Boole's inequality)} \\
&= 1- \sum_{i=1}^N \mathbb{P}\left( x_j\notin A_i \right)^M \qquad\quad\text{(independent samples)} \\
&\geq 1-N(1-\Lambda_N)^M,
\end{aligned}
$$

<!-- PDF page 24 -->

where the last step follows from $\mathbb{P}\left( x_j\notin A_i \right)=1-\mathbb{P}\left( x_j\in A_i \right)\leq 1-\Lambda_N$. $\blacksquare$

Upper bounds for the number of activation regions $N$, as a function of the number of neurons and layers of the neural network $f$, are available in the literature (Montufar et al., 2014; Serra et al., 2018; Hanin and Rolnick, 2019). The regions $A_i$ and their number $N$ could be explicitely computed using formal methods (Serra et al., 2018; Vincent and Schwager, 2021).

## Appendix E. Experimental details

### E.1. Sensitivity analysis

We provide more details into the sensitivity analysis in Section 6.1.

**Sampling distribution**: uniformly sampling over a $p$-dimensional ball $\mathcal{X}=B(0,1)$ can be done with the following algorithm (see, e.g., (Harman and Lacko, 2010)):

1. Sample $u\sim\mathrm{Unif}(0,1)$ and set the radius $r\gets u^{1/p}$.
2. Sample $z\sim \mathcal{N}(\mathbf{0},\mathrm{I}_{p})$ with $\mathrm{I}_p\in\mathbb{R}^{p\times p}$ the identity matrix.
3. Set the input sample to $x \gets (r\cdot z)/\|z\|_2$.

Our sampling distribution $\mathbb{P}_\mathcal{X}^\alpha$ is a simple modification to this algorithm to yield increasingly larger probabilities of sampling inputs $x$ close to the boundary $\partial\mathcal{X}$. Specifically, we replace the first step above with sampling from a $\beta$-distribution $u\sim\mathrm{Beta}(\alpha,\beta)$, where $\beta=1$ is fixed and $\alpha\geq 1$ is a varying parameter. Setting $\alpha=1$ yields a uniform distribution (i.e., $\mathrm{Beta}(1,1)=\mathrm{Unif}(0,1)$) whereas larger values of $\alpha$ yield larger probabilities of sampling close to the boundary $\partial\mathcal{X}$, see Figure 8.

![Figure 8](../assets/s001-lew2022simple/supplementary-figure-8.png)

Figure 8: $M=1000$ samples $x_i$ distributed according to $\mathbb{P}_\mathcal{X}^\alpha$ for two values of the parameter $\alpha$.

**Finite-sample bound**: given a desired $\epsilon$-accuracy, evaluating the theoretical coverage probability $1-\delta_M$ from Corollary 1 requires evaluating the threshold $\delta_M= D(\partial\mathcal{X},\epsilon/(2L))\big(1 - p_0 \Lambda_{\epsilon}^{r,L} \big)^M$. Since $\mathcal{X}$ is a $2$-dimensional unit-radius ball, the covering term is bounded by $D(\partial\mathcal{X},\bar\epsilon)\leq (2\pi) / (2\bar\epsilon) + 1$. The volume term $\Lambda_{\epsilon}^{r,L}=\lambda\big( B(0,\epsilon/(2L)) \cap B(\boldsymbol{r},r) \big)$ is computed as described in Section C. The constant $p_0^\alpha>0$ that satisfies $\mathbb{P}_\mathcal{X}^\alpha(B_x)\geq p_0^\alpha\lambda(B_x)$ for all $B_x=B(x,\bar\epsilon)\cap\mathcal{X}$ with $x\in\partial\mathcal{X}$ (see Assumption 5) can be computed as $p_0^\alpha=(1-\mathrm{CDF}_{\mathrm{Beta}(\alpha,\beta)}((1-\bar\epsilon)^p)))/(1-\mathrm{CDF}_{\mathrm{Unif}(0,1)}((1-\bar\epsilon)^p))$. Finally, given the fixed threshold $\delta_M=10^{-3}$, we compute the corresponding guaranteed accuracy value $\epsilon>0$ that satisfies $\delta_M= D(\partial\mathcal{X},\epsilon/(2L))(1 - p_0 \Lambda_{\epsilon}^{r,L})^M$ using a bisection method.

### E.2. Verification of neural network controllers

We provide further details about the neural network controller experiment in Section 6.2. In this experiment, we consider the verification of a neural network controller $u_t=\pi_{\mathrm{nn}}(x_t)$ for a known linear dynamical system $x_{t+1}=Ax_t+Bu_t$, where $t\in\mathbb{N}$ denotes a time index, and $x_t\in\mathbb{R}^n$ and $u_t\in\mathbb{R}^m$ denote the state and control input. Given a set of initial states $\mathcal{X}_0\subset\mathbb{R}^n$, the problem consists of estimating the reachable set at time $t\in\mathbb{N}$ defined as $\mathcal{X}_t=\{(A(\cdot)+B\pi_{\mathrm{nn}}(\cdot))\circ\dots\circ (Ax_0+B\pi_{\mathrm{nn}}(x_0)): x_0\in\mathcal{X}_0\}$. Defining $(\mathcal{X},\mathcal{Y})=(\mathcal{X}_0,\mathcal{X}_t)$ and $f(x)=(A(\cdot)+B\pi_{\mathrm{nn}}(\cdot))\circ\dots\circ (Ax+B\pi_{\mathrm{nn}}(x))$, we see that this problem fits the mathematical form described in Section 1. In the experiments, we consider $A=\begin{bmatrix} 1&1\\0&1 \end{bmatrix}$, $B=\begin{bmatrix} 0.5\\1 \end{bmatrix}$, $\mathcal{X}_0=\{(x^1,x^2)\in\mathbb{R}^2: 5\leq 2x^1\leq 6, -1\leq 4x^2\leq 1 \}$

<!-- PDF page 25 -->

, and a ReLU network $\pi_{\mathrm{nn}}$ from (Everett et al., 2021) with two layers of $5$ neurons each. We compare $\epsilon$-RandUP with the formal verification technique ReachLP (Everett et al., 2021) and the sampling-based approaches presented in (Thorpe et al., 2021) and (Gruenbacher et al., 2022). We use the Abel kernel $K(x_1,x_2)=\exp(-\|x_1-x_2\|/0.05)$ for the kernel method (Thorpe et al., 2021) due to its separating property (De Vito et al., 2014). To implement GoTube (Gruenbacher et al., 2022), we use the $\epsilon$-RandUP algorithm where we replace the last convex hull bounding step with an outer-bounding ball. We use a uniform sampling distribution for all methods. As ground-truth, we use the reachable sets from $\epsilon$-RandUP with $\epsilon=0$ and $M=10^6$, which is motivated by the asymptotic results from Theorem 1 and was previously done in (Everett et al., 2021).

Next, we provide further details into the evaluation of the finite sample bound: given $\epsilon=0.02$, sampling $M=1400$ inputs that are uniformly-distributed on the boundary $\partial\mathcal{X}$ is sufficient to ensure that the approximated reachable sets from $\epsilon$-RandUP are conservative with probability greater than $1-10^{-4}$. This result relies on the Lipschitz constant of the closed-loop system, which we set to $L=1$ to evaluate this bound since the neural network controller leads to closed-loop stability. Alternatively, one could use a formal method to compute a bound on this constant (in contrast to using a formal method for reachability analysis, computing this Lipschitz constant only needs to be done once and can be done offline) or sampling-based methods with a large number of samples (see Section D for an analysis). Since the input set is given as $\mathcal{X}=[2.5,3]\times[-0.25,0.25]$, we have $D(\partial\mathcal{X}, \epsilon/(2L))\leq 2\cdot(0.5+0.5)/(2\epsilon/(2L)) + 1=2/\epsilon+1$. Finally, since we sample according to a uniform distribution on the boundary and the input set is rectangular, the coverage constant $\Lambda_\epsilon^L$ in Assumption 3 can be set to $\Lambda_\epsilon^L=(2\cdot(\epsilon/2L)) / (4\cdot0.5)=\epsilon/2$. Thus, with $\epsilon=0.02$, (which leads to more accurate reachable set approximations than alternative approaches, see Figure 5), from Theorem 2, choosing $M\geq \frac{\log(\delta_M)-\log(D(\partial\mathcal{X},\epsilon/(2L)))}{\log(1-\Lambda_\epsilon^L)}\approx 1376$ is sufficient to be conservative with probability at least $1-10^{-4}$.
