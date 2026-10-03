#!/usr/bin/env python3
"""Rewrite the reviewed page JSON files for devonport2020estimating.

Reads the untouched extractor output from orig_pages/ (backup made before the first edit),
keeps page-level fields and item bboxes, and replaces the item list with the reviewed items
defined below.  Re-runnable: every run regenerates all ten page files from the backup.
"""
import json
import os

R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
S = f"{R}/logs/work/devonport2020estimating"
D = f"{R}/paper-review/devonport2020estimating-paper/documents/s001-devonport2020estimating"

RH = r"\hat{R}_{[t_0,t_1]}"      # \hat R_{[t0,t1]}
RR = r"R_{[t_0,t_1]}"
NFORM = (r"\left\lceil \frac{1}{\epsilon} \frac{e}{e-1} \left( \log\frac{1}{\delta} "
         r"+ n(n+1)/2 + n \right) \right\rceil")

PAGES = {}
NOTES = {}


def T(i, md, **kw):
    return dict(id=i, kind="text", markdown=md, **kw)


def H(i, md):
    return dict(id=i, kind="heading", markdown=md)


# ----------------------------------------------------------------------------- page 1
PAGES[1] = [
    H("p0001-b000", "# Estimating Reachable Sets with Scenario Optimization"),
    T("p0001-b001",
      "**Alex Devonport** ALEX_DEVONPORT@BERKELEY.EDU  \n"
      "*Department of Electrical Engineering and Computer Sciences*  \n"
      "*University of California, Berkeley*",
      merge=["p0001-b001", "p0001-b002", "p0001-b003"]),
    T("p0001-b004",
      "**Murat Arcak** ARCAK@BERKELEY.EDU  \n"
      "*Department of Electrical Engineering and Computer Sciences*  \n"
      "*University of California, Berkeley*",
      merge=["p0001-b004", "p0001-b005", "p0001-b006"]),
    H("p0001-b007", "## Abstract"),
    T("p0001-b008",
      r"Many practical systems are not amenable to the reachability methods that give guarantees of "
      r"correctness, since they have dynamics that are strongly nonlinear, uncertain, and possibly unknown. "
      r"While reachable sets for these kinds of systems can still be estimated in a *data-driven* way, "
      r"data-driven methods typically do not guarantee the validity of their results. However, certain "
      r"data-driven approaches may be given a *probabilistic* guarantee of correctness, by reframing the "
      r"problem as a chance-constrained optimization problem that is solved with scenario optimization. "
      r"We apply this approach to the problem of approximating a reachable set by a norm ball from data. "
      r"The method requires only $O(n^2)$ sample trajectories and the solution of a convex problem. "
      r"A variant of the method restricted to *axis-aligned* norm balls requires only $O(n)$ samples."),
    T("p0001-b009", "**Keywords:** Reachability analysis; Scenario optimization; Randomized algorithms."),
    H("p0001-b010", "## 1. Introduction"),
    T("p0001-b011",
      "Control systems that manage safety-critical applications must be guaranteed to keep the system safe "
      "in the face of uncertainty. An increasingly popular and effective way to provide such a guarantee is "
      "*reachability analysis*, a set-based method that characterizes all possible evolutions of the system "
      "by computing *reachable sets*. However, reachability analysis poses a significant computational "
      "challenge. Even for simple systems, computing exact reachable sets is known to be an unsolvable "
      "problem (Fijalkow et al. (2019)), meaning that computing exact reachable sets is not a plausible "
      "goal. All practical reachability analysis methods therefore settle for computing approximations to "
      "the true reachable set."),
    T("p0001-b012",
      "Many methods have been developed to compute reachable set approximations. The methods that produce "
      "the most accurate approximations are those based on Hamilton-Jacobi equation (Mitchell et al. (2005)) "
      "or dynamic programming (Bertsekas and Rhodes (1971)), but their accuracy comes at the cost of "
      "scalability. Methods designed for better scalability typically draw approximations from a restricted "
      "family of sets, such as ellipsoids (Kurzhanski and Varaiya (2000)), zonotopes (Althoff (2015)), or "
      "multidimensional intervals (Chen et al. (2013); CAPD (2019); Meyer et al. (2019)). Many methods also "
      "focus on a specific class of system dynamics, such as linear systems or systems with bounded or "
      "sign-stable Jacobians, and use these system properties to speed up computations."),
    T("p0001-b013",
      "However, there are many important cases in which these methods cannot be applied. Some cases arise "
      "when the system of interest is high-dimensional and does not satisfy the system assumptions that "
      "allow the faster methods to be used. Others arise when the system of interest is only available"),
]
NOTES[1] = (
    "Compared every item with the 170-dpi render and a 220-dpi crop of the title block/abstract. Title kept as "
    "the single # heading (bold markers removed). The two author names were mis-typed by the extractor as ### "
    "headings; merged each author with e-mail and affiliation into one text item. The e-mails are printed in "
    "small caps and the text layer lost the underscore: restored ALEX_DEVONPORT@BERKELEY.EDU from the image. "
    "Abstract: O(n^2) and O(n) rewritten as LaTeX (was '_O_ ( _n_<sup>2</sup> )'); line-wrap damage "
    "'datadriven' corrected to 'data-driven' (real compound, cf. the other occurrences in the same paragraph). "
    "Headings set to ## (Abstract, 1. Introduction). Emphasis markers tightened (no space before punctuation). "
    "Last paragraph continues on page 2 (joined there). The page carries no running header, footer, proceedings "
    "banner or page number, so nothing is omitted."
)

# ----------------------------------------------------------------------------- page 2
PAGES[2] = [
    T("p0002-b000",
      "in a form that is mathematically inaccessible (such as a large SIMULINK model), or is only available "
      "through simulations or experiments. For systems such as these, reachable sets can still be computed "
      "in a *data-driven* manner, in which the reachable set is estimated using a finite collection of sample "
      "trajectories of the system. For example, the samples can be generated by simulating trajectories with "
      "initial conditions selected from a uniform grid, and used to approximate a bound on the reachable set. "
      "Under suitable system assumptions, this *quasi-Monte Carlo* approach can provide a formal guarantee of "
      "correctness (Tempo et al. (2012)). However, the grid-based sampling scheme requires a number of samples "
      "that increases exponentially in $n$, so it does not scale well to high-dimensional systems. To combat "
      "the exponential complexity of the quasi-Monte Carlo method, another common approach is to simply select "
      "a number of initial conditions at random. In practice this *Monte Carlo* approach can be effective, but "
      "it is often applied without any formal guarantee of correctness. Without a guarantee, a reachable set "
      "loses much of its power, as it cannot provide any assurance that controller specifications have been met.",
      join_previous="space"),
    T("p0002-b001",
      "In this paper, we show that a class of Monte Carlo-type data-driven methods for reachability analysis "
      "may be given a probabilistic guarantee of correctness, meaning that the estimated reachable set can be "
      "guaranteed to contain a certain measure of the reachable set with high probability. The probabilistic "
      "guarantee is established by reframing the problem of estimating a reachable set from trajectory data as "
      "a *scenario optimization* problem. Scenario optimization is an approach to solving chance-constrained "
      "optimization problems by solving a convex, non-probabilistic relaxation of the problem (Dembo (1991)). "
      "Solutions of the relaxed problem, if they exist, are guaranteed to satisfy the original problem with "
      "high probability. Furthermore, scenario optimization provides a *sample complexity bound*: for a desired "
      "probability of satisfying the original problem, the size of the relaxed problem is known in advance "
      "(Calafiore and Campi (2006); Campi and Garatti (2008)). These results hold for a wide range of "
      "probabilistic uncertainties, including those that inhabit infinite-dimensional spaces (Esfahani et al. "
      "(2014)). Scenario optimization has been used as a randomized approach to solving robust control "
      "problems. For example, Margellos et al. (2014) uses scenario optimization to construct axis-aligned "
      "hyperrectangles that contain a certain probability mass of a random disturbance. We apply a similar "
      "construction, allowing for more general sets, to the problem of reachability analysis."),
    T("p0002-b002",
      "There is some precedent for using scenario optimization to solve problems related to reachability. "
      "Yang et al. (2016) uses scenario optimization to solve a chance-constrained formulation of a "
      "multi-aircraft collision avoidance problem with ellipsoidal reachable sets, in which the randomness in "
      "the problem arises from unknown wind conditions. Ioli et al. (2017) proposes a benchmark problem for "
      "robust control synthesis in which the controller must minimize the size of the reachable set of energy "
      "fluctuations for a microgrid modeled as a discrete-time linear time-invariant system, and propose a "
      "scenario-based solution to the problem. Sartipizadeh et al. (2019) develops a scenario-based approach "
      "for solving reach-avoid problems on discrete-time linear time-invariant systems with additive "
      "probabilistic uncertainty. Hewing and Zeilinger (2019) investigates a scenario-based approach to "
      "provide prediction error bounds for stochastic model-predictive control of discrete-time, linear "
      "time-invariant systems with additive noise. These works focus on controller synthesis for cases in "
      "which the system dynamics are known to be of a certain type such as linear time-invariant, and where "
      "reachability is used to verify safety of the synthesized controller. They use scenario optimization to "
      "mitigate the difficulty of robust synthesis and reach-avoid analysis. However, scenario optimization "
      "may also be used to mitigate the issue of model uncertainty when computing reachable sets."),
]
NOTES[2] = (
    "Read all three paragraphs against the 170-dpi render. First item continues the last sentence of page 1 "
    "('... is only available' / 'in a form that ...'): join_previous=space. Corrected line-wrap damage "
    "'infinitedimensional' to 'infinite-dimensional' (hyphen is at a line end in the PDF; compound adjective). "
    "Inline math: 'exponentially in $n$'. 'SIMULINK' is printed in small caps; kept as in the text layer. "
    "Emphasis kept for data-driven, quasi-Monte Carlo, Monte Carlo, scenario optimization, sample complexity "
    "bound. Authors' grammar kept as printed ('Ioli et al. (2017) proposes ... and propose'). No page "
    "furniture on this page."
)

# ----------------------------------------------------------------------------- page 3
PAGES[3] = [
    T("p0003-b000",
      "Our contribution is to show that scenario optimization may be used to provide guarantees for a range of "
      "data-driven reachability analysis methods that are applicable to a general class of systems. "
      "Specifically, we investigate a Monte Carlo-type method that provides reachable set estimates in the "
      "form of *norm ball* sets, with the optional restriction that the norm balls be *axis-aligned*. For each "
      "of these classes of norm ball sets, we provide a sample complexity bound derived from the scenario "
      "optimization representation of the problem. The sample complexity turns out to be quadratic with "
      "respect to the state dimension for the general norm ball case, and linear in the axis-aligned case."),
    H("p0003-b001", "## 2. Forward Reachable Sets"),
    T("p0003-b002",
      r"We consider a general dynamical system with a state transition function $\Phi(t_1; t_0, x_0, u, d)$ "
      r"that maps an initial state $x_0 \in \mathbb{R}^n$ at time $t_0$ to a unique final state at time $t_1$, "
      r"under the influence of the system dynamics, an input $u : [t_0, t_1] \to \mathbb{R}^p$, and a "
      r"disturbance $d : [t_0, t_1] \to \mathbb{R}^w$. For instance, when the system state dynamics "
      r"$\dot{x}(t) = f(t, x(t), u(t), d(t))$ are known and has unique solutions on the interval $[t_0, t_1]$, "
      r"then $\Phi(t_1; t_0, x_0, u, d)$ is just the value $\phi(t_1)$, where $\phi$ is the solution satisfying "
      r"$\phi(t_0) = x_0$."),
    T("p0003-b003",
      r"For the problem of forward reachability analysis, we are also given an *initial set* "
      r"$\mathcal{X}_0 \subset \mathbb{R}^n$, a set $\mathcal{U}$ of allowed inputs, and a set $\mathcal{D}$ "
      r"of allowed disturbances. The *forward reachable set* is then defined as"),
    T("p0003-b004",
      "$$\n" + RR + r" = \{\Phi(t_1; t_0, x_0, u, d) : x_0 \in \mathcal{X}_0, u \in \mathcal{U}, "
      r"d \in \mathcal{D}\}, \tag{1}" + "\n$$"),
    T("p0003-b005",
      r"that is the set of all states to which the system can transition at time $t_1$ if it starts in a "
      r"state in $\mathcal{X}_0$ at time $t_0$ and is subject to an input in $\mathcal{U}$ and a disturbance "
      r"in $\mathcal{D}$."),
    T("p0003-b006",
      r"Since the exact reachable set cannot be computed, we must settle for the goal of computing some "
      r"approximation $" + RH + r"$. The approximating set is drawn from a family of sets that is described by "
      r"a vector parameter $\theta$, so that the task of computing the approximation is reduced to finding a "
      r"parameter. For instance, if we choose to approximate the reachable set with an *ellipsoid*, that is a "
      r"set of the form $" + RH + r"(A, b) = \{x : \|Ax - b\|_2 \le 1\}$, then the parameter is "
      r"$\theta = (A, b)$."),
    T("p0003-b007",
      r"Typically, $" + RH + r"$ is designed to be either an overapproximation (so that $" + RR +
      r" \subset " + RH + r"$) or an underapproximation (so that $" + RH + r" \subset " + RR + r"$). These "
      r"approximations are useful for making safety guarantees, but reachable sets that are estimated from "
      r"samples will generally not be either. Since we are focusing on a data-driven approach to reachable set "
      r"computation, we will instead aim to compute an approximation that is similar to the true reachable set "
      r"in a probabilistic sense."),
    T("p0003-b008",
      r"Suppose we have a random variable $Z$ whose support is the reachable set, that is such that its "
      r"probability density function (pdf) $p_Z$ satisfies $p_Z(x) = 0$ for $x$ outside of the reachable set "
      r"and $p_Z(x) > 0$ for $x$ inside it. In that case, $" + RR + r"$ is by definition an event with "
      r"probability one, and any set that is disjoint with $" + RR + r"$ has probability zero. Any set that "
      r"contains part of the reachable set will have some probability in between, with a higher probability "
      r"indicating that it contains more of the reachable set. We therefore want to compute a reachable set "
      r"approximation that is guaranteed to have a high probability under such a distribution. If an "
      r"approximation satisfies $P_Z(" + RH + r") \ge 1 - \epsilon$, where $P_Z$ is the probability measure of "
      r"$Z$, then we say that this is an *$\epsilon$-accurate* approximation with respect to the distribution "
      r"$p_Z$."),
    T("p0003-b009",
      r"A reachable set approximation that is $\epsilon$-accurate may still be quite conservative: in addition "
      r"to the part of the approximation with measure $1 - \epsilon$, it could also contain a large portion of "
      r"the state space outside of the reachable set with measure zero. For most approximation classes this"),
]
NOTES[3] = (
    "Compared with the 170-dpi render and two 260-dpi crops (Section 2 down to eq. (1); rest of the page). "
    "Heading '2. Forward Reachable Sets' set to ##. All inline math rewritten in LaTeX from the image and "
    "cross-checked with the native text layer: Phi(t_1; t_0, x_0, u, d), x_0 in R^n, u:[t_0,t_1]->R^p, "
    "d:[t_0,t_1]->R^w, xdot(t)=f(t,x(t),u(t),d(t)), phi(t_1), phi(t_0)=x_0, calligraphic X_0, U, D, "
    "hat R_{[t_0,t_1]}, theta, the ellipsoid {x : ||Ax-b||_2 <= 1}, p_Z (lower-case density) versus P_Z "
    "(upper-case measure), 1 - epsilon. Equation (1) converted from an extractor formula image to a LaTeX "
    "display with \\tag{1}; every symbol was legible, so no formula image is kept. The norm delimiters are "
    "typeset by the authors as two single bars '||' on this page; written as \\| (same meaning). Authors' "
    "wording kept: 'are known and has unique solutions', 'that is the set of all states'. The lunate epsilon "
    "is \\epsilon throughout. Last paragraph continues on page 4."
)

# ----------------------------------------------------------------------------- page 4
PAGES[4] = [
    T("p0004-b000",
      r"conservatism cannot be eliminated, but it should be avoided. Therefore, our goal is not just to compute "
      r"an $\epsilon$-accurate reachable set, but to compute an $\epsilon$-accurate reachable set with as small "
      r"a volume as possible.", join_previous="space"),
    T("p0004-b001", "This goal can be stated as a chance-constrained optimization problem:"),
    T("p0004-b002",
      "$$\n\\begin{aligned}\n"
      r"\underset{\theta}{\text{minimize}} \quad & \mathrm{Vol}(" + RH + r"(\theta)) \\" + "\n"
      r"\text{subject to} \quad & P_Z(" + RH + r"(\theta)) \ge 1 - \epsilon" + "\n"
      "\\end{aligned} \\tag{2}\n$$"),
    T("p0004-b003",
      "This optimization problem is intractable in general. However, in certain cases we may approximately "
      "solve this problem using *scenario optimization*, arriving at a probabilistically guaranteed Monte "
      "Carlo approach to estimating the reachable set."),
    H("p0004-b004", "## 3. Scenario Optimization"),
    T("p0004-b005", "Scenario optimization is a technique to approximately solve optimization problems of the form"),
    T("p0004-b006",
      "$$\n\\begin{aligned}\n"
      r"\underset{\theta}{\text{minimize}} \quad & J(\theta) \\" + "\n"
      r"\text{subject to} \quad & P_Z(g(\theta, Z) \le 0) \ge 1 - \epsilon \\" + "\n"
      r"& \theta \in \Theta," + "\n"
      "\\end{aligned} \\tag{3}\n$$"),
    T("p0004-b007",
      r"where $J$ and $g$ are convex functions, $\Theta \in \mathbb{R}^{n_\theta}$ is convex and compact, and "
      r"$P_Z$ is a probability measure with respect to a random variable $Z$. Solving (3) directly is an "
      r"intractable problem because the probabilistic constraint is difficult to enforce for general random "
      r"variables, and is not guaranteed to be convex even when $g$ is a convex."),
    T("p0004-b008", "Scenario optimization proceeds by solving a deterministic approximation of the problem:"),
    T("p0004-b009",
      "$$\n\\begin{aligned}\n"
      r"\underset{\theta}{\text{minimize}} \quad & J(\theta) \\" + "\n"
      r"\text{subject to} \quad & g(\theta, z^{(i)}) \le 0, \quad i = 1, \dots, N \\" + "\n"
      r"& \theta \in \Theta," + "\n"
      "\\end{aligned} \\tag{4}\n$$"),
    T("p0004-b010",
      r"where $\{z^{(i)}\}_{i=1}^{N}$ are $N$ independently and identically-distributed (iid) samples from "
      r"$Z$. This problem is a non-probabilistic convex program, and so can be solved efficiently even in the "
      r"general case by a range of standard solvers."),
    T("p0004-b011",
      r"The Scenario optimization approach proposes that the minimizer of (4), which we can easily find, is "
      r"also a feasible solution of (3) with high probability. Furthermore, there is a lower bound on this "
      r"probability with respect to $N$:"),
    T("p0004-b012",
      r"**Theorem 1 (Tempo et al. (2012), Corollary 12.1)** let $\delta \in (0, 1)$. If $N$ is selected "
      r"according to"),
    T("p0004-b013",
      "$$\n"
      r"N \ge \frac{1}{\epsilon} \left( \frac{e}{e-1} \right) \left( \log\frac{1}{\delta} + n_\theta \right), "
      r"\tag{5}" + "\n$$"),
    T("p0004-b014",
      r"where $\mathrm{e}$ is the Euler number, then a minimizer of (4), if it exists, is a feasible solution "
      r"to (3) with probability $\ge 1 - \delta$."),
    T("p0004-b015",
      r"While the convexity requirements on $J$ and $g$ can be restrictive, there is a hidden freedom: the "
      r"random variable $Z$ in the probabilistic constraint may have arbitrary support. In our case, we will "
      r"choose a random variable whose support is $" + RR + r"$."),
]
NOTES[4] = (
    "Compared with the 170-dpi render and two 260-dpi crops (eqs. (2)-(3); eqs. (4)-(5) with Theorem 1). "
    "First item continues the sentence from page 3: join_previous=space. Equations (2), (3), (4), (5) "
    "converted from extractor formula images to LaTeX displays with \\tag; all symbols legible, none kept as "
    "an image. (2): minimize over theta of Vol(hat R(theta)) subject to P_Z(hat R(theta)) >= 1 - epsilon. "
    "(3): P_Z(g(theta,Z) <= 0) >= 1 - epsilon, theta in Theta, trailing comma as printed. (4): "
    "g(theta, z^{(i)}) <= 0, i = 1,...,N, theta in Theta, trailing comma as printed. (5): N >= (1/epsilon) "
    "(e/(e-1)) (log(1/delta) + n_theta), with the two parenthesised factors exactly as printed. The paragraph "
    "after (4) was glyph soup ('_{z_<sup>(</sup>...') and was retyped from the image. Theorem 1 label written "
    "in bold with the printed punctuation, i.e. none after the closing parenthesis ('Theorem 1 (Tempo et al. "
    "(2012), Corollary 12.1) let ...'); the statement is printed in italics (italics not reproduced) and is "
    "split into three items (text, display (5), text); it ends with '>= 1 - delta.', after which upright "
    "prose resumes. "
    "Kept as printed: lower-case 'let' at the start of the statement; 'Theta \\in R^{n_theta}' (the authors "
    "print 'element of', not 'subset of'); 'even when g is a convex'; 'The Scenario optimization approach'. In "
    "the clause after (5) the Euler number is printed as an upright e (written \\mathrm{e}) while (5) prints "
    "italic e. Heading '3. Scenario Optimization' set to ##."
)

# ----------------------------------------------------------------------------- page 5
PAGES[5] = [
    H("p0005-b000", "## 4. Scenario-Based Reachability with Norm Balls"),
    T("p0005-b001",
      "The method presented here uses trajectory data to approximate the reachable set with a "
      "*$p$-norm ball*, that is a set of the form"),
    T("p0005-b002", "$$\n" + RH + r"(A, b) = \{x : \|Ax - b\|_p \le 1\} \tag{6}" + "\n$$"),
    T("p0005-b003",
      r"where $x, b \in \mathbb{R}^n$, $A \in \mathbb{R}^{n \times n}$, and $p$ may be either any real "
      r"$\ge 1$ or $\infty$. The class of $p$-norm balls encompasses several types of sets that are popular in "
      r"reachability analysis. For instance, choosing $p = 2$ leads to the class of ellipsoids, and choosing "
      r"$p = \infty$ and restricting $A$ to be diagonal leads to the class of multidimensional intervals."),
    H("p0005-b004", "### 4.1. Unconstrained Norm Balls"),
    T("p0005-b005",
      r"We first consider the general case, where $A$ may be any symmetric matrix. We use $-\log\det A$ as a "
      r"proxy for the volume of $" + RH + r"(A, b)$. The value $-\log\det(A)$ is directly proportional to the "
      r"volume of a 2-norm ball; by the equivalence of norms, it is a suitable proxy for the volume of other "
      r"$p$-norm balls as well. Using this proxy, the minimum-volume $\epsilon$-accurate reachable set problem "
      r"(2) becomes"),
    T("p0005-b006",
      "$$\n\\begin{aligned}\n"
      r"\arg\min_{A,b} \quad & -\log\det A \\" + "\n"
      r"\text{s.t.} \quad & P_Z(\|AZ - b\|_p - 1 \le 0) \le 1 - \epsilon," + "\n"
      "\\end{aligned} \\tag{7}\n$$"),
    T("p0005-b007",
      r"where $Z$ is a random variable whose support is $" + RR + r"$. Since $-\log\det A$ and "
      r"$\|AZ - b\|_p - 1$ are convex in $A$ and $b$, (7) is a convex chance-constrained optimization problem, "
      r"meaning that it can be solved using scenario optimization."),
    T("p0005-b008",
      r"We use the transition function $\Phi$ to construct a suitable $Z$. Specifically, let $X_0$, $U$, and "
      r"$D$ be given random variables whose supports are the initial set, input set, and disturbance set. Then "
      r"the support of the random variable $Z = \Phi(t_1; t_0, X_0, U, D)$ is exactly the reachable set."),
    T("p0005-b009",
      r"The approach is outlined in Algorithm 1. The output is a matrix $A$ and vector $b$ for a norm ball "
      r"reachable set estimate that is $\epsilon$-accurate with high probability with respect to $Z$. This is "
      r"the probabilistic guarantee of correctness, which we formally present with Theorem 2."),
    T("p0005-b010",
      r"**Theorem 2** Let $\epsilon, \delta \in (0, 1)$, and let $X_0$, $U$, and $D$ be random variables over "
      r"$\mathcal{X}_0$, $\mathcal{U}$, and $\mathcal{D}$ respectively, and let "
      r"$Z = \Phi(t_1; t_0, X_0, U, D)$. Denote by $P_S$ the probability measure corresponding to the "
      r"multisample of $N = " + NFORM + r"$ points taken from $X_0$, $U$, and $D$, and by $P_Z$ the "
      r"probability measure corresponding to $Z$. Then the output $(A, b)$ of Algorithm 1 satisfies the "
      r"following probability inequality:"),
    T("p0005-b011",
      "$$\n" + r"P_S(P_Z(" + RH + r"(A, b)) \ge 1 - \epsilon) \ge 1 - \delta; \tag{9}" + "\n$$"),
    T("p0005-b012", "or, in other words,"),
    T("p0005-b013",
      "$$\n" + r"P_S(" + RH + r"(A, b) \text{ is } \epsilon\text{-accurate with respect to } Z) "
      r"\ge 1 - \delta. \tag{10}" + "\n$$"),
    T("p0005-b014",
      r"**Proof** If $(A, b)$ is a feasible solution to (7), then $" + RH + r"(A, b)$ is by construction an "
      r"$\epsilon$-accurate estimate. Algorithm 1 finds a solution to (8), which is the scenario problem "
      r"corresponding to (7). The decision variables of (7) are a symmetric $n \times n$ real matrix and a "
      r"real $n$-vector, so $n_\theta = n(n+1)/2 + n$. The $N$ chosen in Algorithm 1 satisfies the sample "
      r"bound in Theorem 1 for this $n_\theta$. Therefore, the $A$ and $b$ that minimize (8) is a feasible "
      r"solution to (7) with probability $1 - \delta$. $\blacksquare$"),
]
NOTES[5] = (
    "Compared with the 170-dpi render and two 260-dpi crops (top half to eq. (7); Theorem 2 and proof). "
    "Headings: '4. Scenario-Based Reachability with Norm Balls' ##, '4.1. Unconstrained Norm Balls' ###. "
    "Equations (6), (7), (9), (10) converted from extractor formula images to LaTeX displays with \\tag; all "
    "symbols legible, none kept as an image. Equation (8) is not on this page: it is printed inside "
    "Algorithm 1 on page 6, so the numbering here goes (6), (7), (9), (10). AUTHORS' TYPO KEPT AS PRINTED: "
    "the chance constraint of (7) is printed 'P_Z(||AZ - b||_p - 1 <= 0) <= 1 - epsilon' (outer relation "
    "'<='), confirmed in the image and in the native text layer; the intended relation is evidently '>=' "
    "(cf. (2), (3), (9)), but it was not changed. Theorem 2: the sample size inside the statement was glyph "
    "soup in the extraction and was retyped from the 260-dpi crop as N = ceil( (1/eps) (e/(e-1)) "
    "(log(1/delta) + n(n+1)/2 + n) ); checked numerically against page 7 (n = 6, eps = 0.05, delta = 1e-9 "
    "gives 1510). Theorem and proof labels in bold with the printed punctuation, i.e. none ('Theorem 2 Let "
    "...', 'Proof If ...'); the theorem statement is printed in italics (it runs from 'Let' to display (10); "
    "the italics were not reproduced). End-of-proof square written as \\blacksquare. Grammar kept as printed ('the A and b that "
    "minimize (8) is a feasible solution'). Norm delimiters printed as '||' on this page, written \\|. "
    "X_0, U, D (italic) are the random variables and calligraphic X_0, U, D the sets, as printed."
)

# ----------------------------------------------------------------------------- page 6
ALG = "\n\n".join([
    r"**Algorithm 1:** Scenario-based estimate of a reachable set by a $p$-norm ball.",
    r"**Input:** Transition function $\Phi$ of a system with state dimension $n$; random variables $X_0$, $U$ "
    r"and $D$ supported on $\mathcal{X}_0$, $\mathcal{U}$, and $\mathcal{D}$ respectively; time range "
    r"$[t_0, t_1]$; norm index $p$; probabilistic guarantee parameters $\epsilon$ and $\delta$.",
    r"**Output:** Matrix $A$ and vector $b$ representing an $\epsilon$-accurate reachable set estimate $" + RH +
    r"(A, b) = \{x : \|Ax + b\|_p \le 1\}$, with confidence $1 - \delta$.",
    r"Set number of samples $N = " + NFORM + r"$;",
    r"**forall** $i \in \{1, \dots, N\}$ **do**",
    r"&emsp;&emsp;Take samples $x^{(i)}$, $u^{(i)}$, and $d^{(i)}$ from $X_0$ $U$, and $D$;",
    r"&emsp;&emsp;evaluate $z^{(i)} = \Phi(t_1; t_0, x^{(i)}, u^{(i)}, d^{(i)})$;",
    r"**end**",
    r"Solve the convex problem",
    "$$\n\\begin{aligned}\n"
    r"\arg\min_{A,b} \quad & -\log\det A \\" + "\n"
    r"\text{subject to} \quad & \|Az^{(i)} - b\|_p - 1 \le 0, \quad i = 1, \dots, N" + "\n"
    "\\end{aligned} \\tag{8}\n$$",
    r"and return $A$, $b$;",
])
PAGES[6] = [
    dict(id="p0006-algorithm1", kind="figure", bbox=[86.0, 90.0, 527.0, 350.0], markdown="",
         label="Algorithm 1", asset_name="algorithm-1"),
    dict(id="p0006-algorithm1-text", kind="text", bbox=[86.0, 90.0, 527.0, 350.0], markdown=ALG),
    T("p0006-b005",
      "While Theorem 2 does not guarantee that the reachable set approximation provided by Algorithm 1 is an "
      "over- or under-approximation of the true reachable set, it still asserts that the computed reachable "
      "set approximation is accurate in a probabilistic sense with respect to the random variables used to "
      "compute it."),
    T("p0006-b006",
      r"The *sample complexity* of a randomized algorithm is the number of samples needed for the algorithm to "
      r"run such that its output satisfies a guarantee of correctness. For instance, from the sample bound "
      r"(5), the sample complexity of an algorithm based on scenario optimization with respect to the "
      r"probabilistic guarantee parameters is $O(\frac{1}{\epsilon})$ and $O(\log\frac{1}{\delta})$. For "
      r"Algorithm 1, the sample complexity also depends on the state dimension $n$. This dependence can be "
      r"determined from (5), and depends on how $n$ affects the number $n_\theta$ of decision variables. In "
      r"Algorithm 1, the $A$ matrix requires $n(n+1)/2$ decision variables and the $b$ vector requires $n$ "
      r"decision variables. This means that $n_\theta = n(n+1)/2 + n$, so the sample complexity of Algorithm 1 "
      r"is $O(n^2)$. Note that the sample bound of Theorem 2 depends only on the parameters $\epsilon$ and "
      r"$\delta$, and the state dimension $n$. The system may therefore have inputs and disturbances of any "
      r"dimension without affecting the sample complexity."),
    H("p0006-b007", "### 4.2. Axis-aligned Norm Balls"),
    T("p0006-b008",
      r"The quadratic sample complexity of the method in the previous section is not scalable to systems of "
      r"high dimension, or systems for which the transition function takes a long time to evaluate. For these "
      r"systems, we would like a variant of the method with less than quadratic sample complexity. The source "
      r"of the quadratic term in the sample complexity is the number of free variables in the $A$ matrix. If "
      r"we constrain the structure of the $A$ matrix so that it has fewer than $O(n^2)$ free variables, then "
      r"the sample complexity will be lowered."),
]
NOTES[6] = (
    "Compared with the 170-dpi render and two 260-dpi crops (the Algorithm 1 box; the prose and 4.2 heading). "
    "Algorithm 1: the extractor had split the box into four text items plus a formula image; replaced by one "
    "image crop of the whole box (asset algorithm-1, bbox from above the top rule to below the bottom rule, "
    "checked on the render) followed by one text item with a line-by-line LaTeX transcription. The box has no "
    "printed line numbers, so none were added; the two statements of the forall body are indented with "
    "&emsp;. Equation (8) is printed inside the algorithm box and is transcribed inside the algorithm text "
    "item with \\tag{8}. AUTHORS' INCONSISTENCIES KEPT AS PRINTED: the Output line prints the set as "
    "{x : ||Ax + b||_p <= 1} with a PLUS sign, whereas eq. (6) and eq. (8) use 'Ax - b' / 'Az^{(i)} - b' "
    "(confirmed in image and text layer); the sampling line prints 'from X_0 U, and D' with no comma after "
    "X_0. The sample-size line N = ceil((1/eps)(e/(e-1))(log(1/delta) + n(n+1)/2 + n)) was read from the "
    "260-dpi crop (the text layer has it as fragments). Prose: the O(1/epsilon) and O(log(1/delta)) sentence "
    "was glyph soup and was retyped from the image; n_theta, n(n+1)/2, O(n^2) written in LaTeX. Heading "
    "'4.2. Axis-aligned Norm Balls' set to ### (extractor had #). Line-wrap hyphen in 'Algo-rithm' removed; "
    "'over- or under-approximation' kept."
)

# ----------------------------------------------------------------------------- page 7
PAGES[7] = [
    T("p0007-b000",
      r"One such constraint is to require that the $A$ matrix be diagonal. In this case, the $A$ matrix has "
      r"only $n$ free variables, and the overall sample complexity is reduced from $O(n^2)$ to $O(n)$. "
      r"Specifically, in the case of diagonal $A$, Algorithm 1 can run with the reduced sample size"),
    T("p0007-b001",
      "$$\n" + r"N_{diag} = \left\lceil \frac{1}{\epsilon} \frac{e}{e-1} \left( \log\frac{1}{\delta} + 2n "
      r"\right) \right\rceil, \tag{11}" + "\n$$"),
    T("p0007-b002", r"since the free variables in $A$ and $b$ lead to $n_\theta = 2n$."),
    T("p0007-b003",
      r"However, the constraint on the structure of $A$ also induces a constraint on the types of norm ball "
      r"sets that are available as reachable set estimates. In the $p = 2$ case, the norm balls with diagonal "
      r"$A$ are ellipsoids whose principal axes are parallel to the coordinate axis defined by the standard "
      r"basis for $\mathbb{R}^n$. By analogy with these “axis-aligned” ellipsoids, we call any $p$-norm ball "
      r"with a diagonal $A$ matrix an axis-aligned norm ball."),
    T("p0007-b004",
      r"The class of axis-aligned $p$-norm balls with $p = \infty$ is identical to the set of axis-aligned "
      r"hyperrectangles. In this case, the difficulty of the optimization problem is reduced as well as the "
      r"sample complexity: solving (8) reduces to finding the smallest axis-aligned hyperrectangle containing "
      r"all of the sample points $z^{(i)}$. This is just the hyperrectangle whose largest and smallest points "
      r"(with respect to the standard partial order) are the elementwise maximum and minimum of the "
      r"$z^{(i)}$."),
    H("p0007-b005", "## 5. Example: Safety Verification of a Medical Exoskeleton"),
    T("p0007-b006",
      "We consider a problem posed in Narvaez-Aroche et al. (2018) to evaluate the safety of a control system "
      "in a medical application. The system is an exoskeleton: specifically, a brace for the lower limbs, "
      "which has actuators to assist with movement. The exoskeleton and its user are modeled as a three-link "
      "planar robot, which has six states and 12 parameters that depend on the user’s weight. The controller "
      "is a finite-time LQR controller that follows a trajectory that brings the user from a sitting position "
      "to a standing position over the course of 3.5 seconds. The problem is to verify that the controller "
      "can safely bring the user from sitting to standing over a range of parameters effected by a 5% "
      "variation in body weight. The authors of Narvaez-Aroche et al. (2018) solve the problem by computing "
      "the forward reachable set at three times and ensuring that no unsafe states (such as a fallen "
      "position) are reached."),
    T("p0007-b007",
      r"We perform the same reachability-based safety verification using Algorithm 1, treating the uncertain "
      r"parameters as constant-valued disturbances with values sampled uniformly from the allowed range. We "
      r"take $p = 2$, and for the guarantee we take $\epsilon = 0.05$, $\delta = 10^{-9}$. This guarantees "
      r"that Algorithm 1 will produce an ellipsoid containing at least $0.95$ of the measure of the reachable "
      r"set distribution, with only a “one in a billion” chance of failure. To assert this guarantee, the "
      r"sample bound of Algorithm 1 requires $N = 1510$ samples. Using the axis-aligned variant of Algorithm 1 "
      r"reduces the bound to $N_{diag} = 1036$ samples. Figure 1 shows the reachable sets computed by "
      r"Algorithm 1 in the unconstrained and axis-aligned cases, projected from the six kinematic states onto "
      r"the $x$- and $y$- coordinates of the center of mass."),
    T("p0007-b008",
      r"To verify that the computed reachable sets satisfy the *a priori* guarantee that they are "
      r"$\epsilon$-accurate, we compute an *a posteriori* empirical estimate of their measures with an "
      r"additional $46,052$ samples. With this number of samples, a one-sided Chernoff bound holds, which "
      r"ensures that the *a posteriori* estimate of the measure exceeds the true measure by no more than "
      r"$.01$ with confidence $0.9999$. The results are shown in Table 1, and validate that the sets are "
      r"indeed $\epsilon$-accurate. Table 1 also shows the details of the computation times. All computations "
      r"were done on a 3.6 GHz Intel CPU, running MATLAB on one thread."),
]
NOTES[7] = (
    "Compared with the 170-dpi render and two 260-dpi crops (top to end of Section 4.2; the two paragraphs "
    "with the numerical settings). Equation (11) converted from an extractor formula image to LaTeX with "
    "\\tag{11}: N_diag = ceil((1/eps)(e/(e-1))(log(1/delta) + 2n)), trailing comma as printed; 'diag' is an "
    "italic subscript. All numbers on the page checked digit by digit against the crop: six states, 12 "
    "parameters, 3.5 seconds, 5%, p = 2, epsilon = 0.05, delta = 10^{-9}, 0.95, N = 1510, N_diag = 1036, "
    "46,052 additional samples (printed in math mode as '46, 052'), '.01' (printed without leading zero), "
    "0.9999, 3.6 GHz. The two sample sizes were also recomputed from Theorem 2 / eq. (11) with n = 6 and "
    "agree (1510 and 1036). Heading '5. Example: Safety Verification of a Medical Exoskeleton' set to ## "
    "(extractor had #). Line-wrap hyphens removed in 'Specifi-cally', 'hyper-rectangles' (the paper writes "
    "'hyperrectangle' unhyphenated elsewhere on the page), 'un-certain'. Kept as printed: 'parameters "
    "effected by', 'the coordinate axis', '$x$- and $y$- coordinates' (space after the second hyphen)."
)

# ----------------------------------------------------------------------------- page 8
PAGES[8] = [
    dict(id="p0008-b000", kind="figure", markdown="", label="Figure 1", asset_name="figure-1"),
    dict(id="p0008-b001", kind="caption",
         markdown=r"Figure 1: Reachable set estimates for the exoskeleton computed using Algorithm 1, projected "
                  r"from six kinematic states to the $x$- and $y$-positions of the center of mass. The sample "
                  r"points used to compute each ellipsoid are also shown."),
    dict(id="p0008-b002", kind="table", markdown="", label="Table 1", asset_name="table-1",
         rows=[["", "Sampling $z^{(i)}$", "solving (8)", "$t = 0$ measure", "$t = 1.75$ measure",
                "$t = 3.5$ measure"],
               ["Unconstrained", "1 hr 16 min", "23.6 s", "0.9971", "0.9927", "0.9964"],
               ["Axis-aligned", "52 min", "14.1 s", "0.9977", "0.9971", "0.9961"]]),
    dict(id="p0008-b003", kind="caption",
         markdown="Table 1: Computation times and empirical measures for the reachable sets shown in Fig. 1."),
    H("p0008-b004", "## 6. Conclusions"),
    T("p0008-b005",
      "The method of scenario optimization offers a partial solution to the lack of correctness guarantees for "
      "data-driven approaches to reachability analysis. We have found that several simple Monte Carlo-type "
      "approaches to approximating reachable sets can be put on a solid foundation and supplied with "
      "probabilistic guarantees of correctness by framing them as scenario optimization problems. In this "
      "paper we have focused on two variants of the case of approximation by norm balls, which lead to "
      "scalable sample complexities and efficiently-solvable optimization problems."),
    T("p0008-b006",
      "However, the scenario optimization approach has two limitations. First, the reachable set "
      "approximations must be convex sets, since the scenario optimization guarantee will not hold otherwise. "
      "Second, the requirement that the scenario optimization problem be constructed from iid samples "
      "precludes this approach from providing guarantees for active learning-based approaches, in which case "
      "the sample distribution would have correlations."),
    H("p0008-b007", "## Acknowledgments"),
    T("p0008-b008",
      "This work was supported in part by the grants ONR N00014-18-1-2209, AFOSR FA9550-18-1-0253, NSF "
      "ECCS-1906164."),
]
NOTES[8] = (
    "Compared with the 170-dpi render, a 200-dpi crop of the figure region with margin, and a 220-dpi crop of "
    "caption and table. Figure 1: one crop holding the three panels (titles 'Reachable Set at t = 0 [s]', "
    "'t = 1.75 [s]', 't = 3.5 [s]'), all axis tick labels, the axis labels x_CoM(t) [m] / y_CoM(t) [m], the "
    "'x10^-3' exponent of the third panel and the four-entry legend; the extractor bbox was checked on the "
    "crop and already contains everything with a white margin and no caption text, so it is unchanged. The "
    "tick-label/legend text the extractor had stored in the figure item was dropped (it is visible in the "
    "crop). Table 1 captured as cells and compared cell by cell with the crop: 3 rows x 6 columns, values "
    "1 hr 16 min, 23.6 s, 0.9971, 0.9927, 0.9964 / 52 min, 14.1 s, 0.9977, 0.9971, 0.9961. The first header "
    "cell is empty as printed; header math written in LaTeX (extractor had 'Sampling_z_<sup>...' and "
    "'_t_= 1_._75measure'). The table caption is printed below the table and is kept there. Corrected "
    "line-wrap damage 'Monte Carlotype' to 'Monte Carlo-type' (compound, as on pages 2 and 3). Headings "
    "'6. Conclusions' and 'Acknowledgments' set to ##. Grant numbers checked against the render."
)

# ----------------------------------------------------------------------------- page 9
REFS9 = [
    ("p0009-b001", "Matthias Althoff. An introduction to CORA 2015. In *Proc. of the Workshop on Applied "
                   "Verification for Continuous and Hybrid Systems*, 2015."),
    ("p0009-b002", "D.P. Bertsekas and I.B. Rhodes. On the minimax reachability of target sets and target "
                   "tubes. *Automatica*, 7(2):233 – 247, 1971. ISSN 0005-1098. doi: "
                   "https://doi.org/10.1016/0005-1098(71)90066-5. URL "
                   "http://www.sciencedirect.com/science/article/pii/0005109871900665."),
    ("p0009-b003", "Giuseppe C Calafiore and Marco C Campi. The scenario approach to robust control design. "
                   "*IEEE Transactions on Automatic Control*, 51(5):742–753, 2006."),
    ("p0009-b004", "Marco C Campi and Simone Garatti. The exact feasibility of randomized solutions of "
                   "uncertain convex programs. *SIAM Journal on Optimization*, 19(3):1211–1230, 2008."),
    ("p0009-b005", "CAPD. Computer assisted proofs in dynamics group, a c++ package for rigorous numerics, "
                   "2019. URL http://capd.ii.uj.edu.pl/."),
    ("p0009-b006", "Xin Chen, Erika Ábrahám, and Sriram Sankaranarayanan. Flow\\*: An analyzer for non-linear "
                   "hybrid systems. In *International Conference on Computer Aided Verification*, pages "
                   "258–263. Springer, 2013."),
    ("p0009-b007", "Ron S Dembo. Scenario optimization. *Annals of Operations Research*, 30(1):63–80, 1991."),
    ("p0009-b008", "Peyman Mohajerin Esfahani, Tobias Sutter, and John Lygeros. Performance bounds for the "
                   "scenario approach and an extension to a class of non-convex programs. *IEEE Transactions "
                   "on Automatic Control*, 60(1):46–58, 2014."),
    ("p0009-b009", "Nathanaël Fijalkow, Joël Ouaknine, Amaury Pouly, João Sousa-Pinto, and James Worrell. On "
                   "the decidability of reachability in linear time-invariant systems. In *Proceedings of the "
                   "22nd ACM International Conference on Hybrid Systems: Computation and Control*, pages "
                   "77–86. ACM, 2019."),
    ("p0009-b010", "Lukas Hewing and Melanie N Zeilinger. Scenario-based probabilistic reachable sets for "
                   "recursively feasible stochastic model predictive control. *IEEE Control Systems Letters*, "
                   "4(2):450–455, 2019."),
    ("p0009-b011", "Daniele Ioli, Alessandro Falsone, Hartung Marianne, Busboom Axel, and Maria Prandini. A "
                   "smart grid energy management problem for data-driven design with probabilistic "
                   "reachability guarantees. In *4th International Workshop on Applied Verification of "
                   "Continuous and Hybrid Systems*, volume 48, pages 2–19, 2017."),
    ("p0009-b012", "Alexander B Kurzhanski and Pravin Varaiya. Ellipsoidal techniques for reachability "
                   "analysis. In *International Workshop on Hybrid Systems: Computation and Control*, pages "
                   "202–214. Springer, 2000."),
    ("p0009-b013", "Kostas Margellos, Paul Goulart, and John Lygeros. On the road between robust optimization "
                   "and the scenario approach for chance constrained optimization problems. *IEEE "
                   "Transactions on Automatic Control*, 59(8):2258–2263, 2014."),
    ("p0009-b014", "Pierre-Jean Meyer, Alex Devonport, and Murat Arcak. Tira: toolbox for interval "
                   "reachability analysis. In *Proceedings of the 22nd ACM International Conference on Hybrid "
                   "Systems: Computation and Control*, pages 224–229. ACM, 2019."),
    ("p0009-b015", "Ian M Mitchell, Alexandre M Bayen, and Claire J Tomlin. A time-dependent hamilton-jacobi "
                   "formulation of reachable sets for continuous dynamic games. *IEEE Transactions on "
                   "automatic control*, 50(7):947–957, 2005."),
]
PAGES[9] = [H("p0009-b000", "## References")] + [T(i, m) for i, m in REFS9]
NOTES[9] = (
    "All 15 entries on this page read against three 220-dpi crops covering the whole page (not a sample): "
    "author names, titles, venues, volume(issue):pages and years match. The list is unnumbered author-year "
    "style; each entry is its own paragraph and the extractor's '- ' bullets were removed (not printed). "
    "Repaired diacritics that the extractor had split into separate accent glyphs: 'Erika Ábrahám' (was "
    "'Abrah´am' with a stray '<sup>´</sup>'), 'Nathanaël Fijalkow', 'Joël Ouaknine', 'João Sousa-Pinto'. "
    "Bertsekas entry: the URL is broken across two lines after 'http:' in the PDF and was rejoined without a "
    "space; 'Automatica, 7' / '(2):233 – 247' is broken across lines and written '7(2):233 – 247' (no space, "
    "as in the other entries; the spaced en dash is as printed). Esfahani entry: page range broken across "
    "lines, written '46–58'. Margellos entry: line break after '59(8):', written '59(8):2258–2263'. 'Flow*' "
    "written with an escaped asterisk. Lower-case as printed: 'c++', 'hamilton-jacobi', 'IEEE Transactions on "
    "automatic control', 'Tira'. Author order 'Hartung Marianne, Busboom Axel' kept as printed. Heading "
    "'References' set to ##."
)

# ----------------------------------------------------------------------------- page 10
REFS10 = [
    ("p0010-b000", "Octavio Narvaez-Aroche, Pierre-Jean Meyer, Murat Arcak, and Andrew Packard. Reachability "
                   "analysis for robustness evaluation of the sit-to-stand movement for powered lower limb "
                   "orthoses. In *ASME 2018 Dynamic Systems and Control Conference*, Atlanta, GA, USA, October "
                   "2018."),
    ("p0010-b001", "Hossein Sartipizadeh, Abraham P Vinod, Behçet Açikmeşe, and Meeko Oishi. Voronoi "
                   "partition-based scenario reduction for fast sampling-based stochastic reachability "
                   "computation of linear systems. In *2019 American Control Conference (ACC)*, pages 37–44. "
                   "IEEE, 2019."),
    ("p0010-b002", "Roberto Tempo, Giuseppe Calafiore, and Fabrizio Dabbene. *Randomized algorithms for "
                   "analysis and control of uncertain systems: with applications*. Springer Science & Business "
                   "Media, 2012."),
    ("p0010-b003", "Yang Yang, Jun Zhang, Kai-Quan Cai, and Maria Prandini. Multi-aircraft conflict detection "
                   "and resolution based on probabilistic reach sets. *IEEE Transactions on Control Systems "
                   "Technology*, 25(1):309–316, 2016."),
]
PAGES[10] = [T(i, m) for i, m in REFS10]
NOTES[10] = (
    "The four remaining reference entries read in full against a 220-dpi crop; the rest of the page is blank "
    "(no appendix, no page number). Repaired diacritics split by the extractor: 'Behçet Açikmeşe' (was "
    "'Behc¸et Ac¸ikmes¸e'; printed with c-cedilla, dotted i and s-cedilla). Line-wrap hyphen in 'sce-nario' "
    "removed. '- ' bullets removed (not printed). These entries continue the reference list of page 9 and are "
    "separate entries, so no cross-page join is set."
)


def union(boxes):
    return [min(b[0] for b in boxes), min(b[1] for b in boxes), max(b[2] for b in boxes), max(b[3] for b in boxes)]


def main():
    for pn, items in PAGES.items():
        orig = json.load(open(f"{S}/orig_pages/page-{pn:04d}.json"))
        by_id = {it["id"]: it for it in orig["items"]}
        out_items = []
        for spec in items:
            spec = dict(spec)
            merge = spec.pop("merge", None)
            item = {"id": spec["id"], "kind": spec["kind"]}
            if "bbox" in spec:
                item["bbox"] = spec["bbox"]
            elif merge:
                item["bbox"] = union([by_id[m]["bbox"] for m in merge])
            else:
                item["bbox"] = by_id[spec["id"]]["bbox"]
            item["markdown"] = spec["markdown"]
            for key in ("label", "asset_name", "rows", "join_previous", "asset_category"):
                if key in spec:
                    item[key] = spec[key]
            if spec["id"] in by_id and "source_class" in by_id[spec["id"]]:
                item["source_class"] = by_id[spec["id"]]["source_class"]
            out_items.append(item)
        page = {k: v for k, v in orig.items() if k != "items"}
        page["reviewed"] = True
        page["review_notes"] = NOTES[pn]
        page["items"] = out_items
        with open(f"{D}/pages/page-{pn:04d}.json", "w", encoding="utf-8") as f:
            json.dump(page, f, ensure_ascii=False, indent=2)
            f.write("\n")
        dropped = [i for i in by_id if i not in {s["id"] for s in items} and
                   not any(i in (s.get("merge") or []) for s in items)]
        print(f"page {pn}: {len(out_items)} items written; extractor items replaced/dropped: {dropped}")


if __name__ == "__main__":
    main()
