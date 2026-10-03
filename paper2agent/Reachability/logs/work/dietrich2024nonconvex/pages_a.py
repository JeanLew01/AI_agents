#!/usr/bin/env python3
"""Reviewed items for PDF pages 1-5 of dietrich2024nonconvex (run to rewrite those page files)."""
from pagelib import T, H, C, O, F, write_pages, RUNHEAD, PAGENO

PAGES, NOTES = {}, {}

# ----------------------------------------------------------------------------- page 1
NOTES[1] = r"""
Compared item by item with the 170 dpi render of PDF page 1 (single column). The proceedings banner at
the top ('Proceedings of Machine Learning Research vol 242:514-527, 2024') is page furniture and is set
to omit; its content is recorded in the conversion notes. Title kept as the single level-1 heading (bold
markers removed). The extractor had turned the author names into two level-3 headings and merged the
three e-mail addresses into one line; the author block is rewritten as text, one author per line with the
e-mail printed on the same line at the right margin. The e-mail addresses are printed in small capitals
(the text layer gives capitals and loses the underscore of 'alex_devonport'); they are written in lower
case. Affiliation: two italic lines as printed. 'Abstract' is a printed centred heading, kept as level 2;
abstract and 'Keywords:' line compared word by word, 'probabilistic' is italic in the print. '1.
Introduction' set to level 2. Three introduction paragraphs compared with the render; line-wrap hyphen
of 'Al-thoff and Frehse' removed; 'Donze' restored with its accent (text layer: 'Donz´e'). The last
paragraph ends in the middle of a citation list ('... Duggirala et al., 2013; Maidens') and continues on
page 2 (join set there). The copyright line at the foot of the page ('(c) 2024 E. Dietrich, R.A.
Devonport & M. Arcak.') is kept as a text item; in the reading order it is placed after the author block
so that it does not interrupt the sentence that runs on to page 2. No mathematics on this page.
"""
PAGES[1] = [
    O("p0001-b000", "Proceedings banner at the top of the first page ('Proceedings of Machine Learning Research "
                    "vol 242:514-527, 2024'); page furniture. The volume, page range and year are recorded in the "
                    "conversion notes."),
    H("p0001-b001", "# Nonconvex Scenario Optimization for Data-Driven Reachability"),
    T("p0001-b002",
      "**Elizabeth Dietrich** eadietri@berkeley.edu  \n"
      "**Rosalyn Alex Devonport** alex_devonport@berkeley.edu  \n"
      "**Murat Arcak** arcak@berkeley.edu  \n"
      "*Department of Electrical Engineering and Computer Sciences*  \n"
      "*University of California, Berkeley*",
      box=("p0001-b002", "p0001-b003", "p0001-b004", "p0001-b005")),
    H("p0001-b006", "## Abstract"),
    T("p0001-b007",
      "Many of the popular reachability analysis methods rely on the existence of system models. When system "
      "dynamics are uncertain or unknown, data-driven techniques must be utilized instead. In this paper, we "
      "propose an approach to data-driven reachability that provides a *probabilistic* guarantee of correctness "
      "for these systems through nonconvex scenario optimization. We pose the problem of finding reachable sets "
      "directly from data as a chance-constrained optimization problem, and present two algorithms for estimating "
      "nonconvex reachable sets: (1) through the union of partition cells and (2) through the sum of radial basis "
      "functions. Additionally, we investigate numerical examples to demonstrate the capability and applicability "
      "of the introduced methods to provide nonconvex reachable set approximations."),
    T("p0001-b008", "**Keywords:** Reachability analysis, scenario optimization, data-driven methods"),
    H("p0001-b009", "## 1. Introduction"),
    T("p0001-b010",
      "To guarantee the safety of dynamical systems, *reachability analysis* is often used to determine the set of "
      "states that a system could possibly visit. However, in practice, computing exact reachable sets is an "
      "undecidable problem. For this reason, approximation methods are often used to reason about these systems and "
      "present guarantees. For example, over-approximated reachable sets guarantee safety when they do not overlap "
      "with unsafe regions of the state space."),
    T("p0001-b011",
      "There are many approaches that have been developed for this type of reachability analysis for systems with "
      "known dynamics. The most common of these include utilization of Hamilton-Jacobi differential equations "
      "(Mitchell et al., 2005; Bansal et al., 2017; Chen and Tomlin, 2018) or barrier certificates (Prajna, 2003; "
      "Prajna and Jadbabaie, 2004). While these techniques handle complex nonlinear dynamics well, their "
      "computational cost increases sharply with state dimensions. Set propagation techniques (Althoff, 2010; "
      "Althoff et al., 2021) iteratively compute a sequence of sets and achieve better scalability with state "
      "dimension. The most commonly used families of sets are ellipsoids (Kurzhanski and Varaiya, 2000; Botchkarev "
      "and Tripakis, 2000), hyperrectangles (Meyer et al., 2021), zonotopes (Girard, 2005), polytopes (Althoff et "
      "al., 2010), and support functions (Althoff and Frehse, 2016)."),
    T("p0001-b012",
      "However, when the exact dynamics of a system are not known or only partially known, none of the techniques "
      "above can be used. Instead, we must estimate reachable sets in a data-driven manner. Several methods attempt "
      "to provide probabilistic guarantees of correctness for reachable sets directly from data. These methods "
      "include results from simulation and trajectory sensitivity analysis (Donzé and Maler, 2007; Girard and "
      "Pappas, 2006; Fan et al., 2017) or Gaussian processes (Devonport and Arcak, 2020a) and utilize "
      "simulation-based data to learn reachable sets. Other simulation-based and data-driven reachability methods "
      "include (Duggirala et al., 2013; Maidens"),
    T("p0001-b013", "© 2024 E. Dietrich, R.A. Devonport & M. Arcak."),
]

# ----------------------------------------------------------------------------- page 2
NOTES[2] = r"""
Compared with the 170 dpi render and a 260 dpi crop of the lower half (Section 2). Running header 'DIETRICH
DEVONPORT ARCAK' and page number 2 omitted. The first item continues the sentence from page 1 (join_previous
= space). Line-wrap hyphens removed in 'optimization' (three times), 'simulation', 'estimators', 'approximations',
'independently'; the compound hyphens of 'data-driven', 'chance-constrained', 'non-probabilistic',
'scenario-based', 'a-priori', 'a-posteriori', 'identically-distributed', 'wait-and-judge' are printed and kept.
Section heading '2. Nonconvex Scenario Optimization' set to level 2 (extractor had level 1). All inline
mathematics transcribed visually to LaTeX from the 260 dpi crop (no TeX source): Delta, sigma-algebra, bold P
(written \mathbf{P}), delta^{(i)}, x in calligraphic X subset-or-equal R^d, calligraphic X with subscript
delta^{(i)}, V(x) = P{delta in Delta : x notin X_delta}, x_N^* , V(x_N^*) <= epsilon. The extractor's formula
image for display (1) is replaced by a $$ block with \tag{1}: 'minimize' with x in X underneath, 'subject to'
x in the intersection over i=1,...,N of X_{delta^{(i)}}. Kept as printed: 'delta^{(1)}, ...delta^{(N)}' with no
comma after the dots, and '(i.i.d)' without a final period. 'scenario' and 'wait-and-judge' are italic in the print.
"""
PAGES[2] = [
    O("p0002-b000", RUNHEAD),
    T("p0002-b001",
      "and Arcak, 2015; Arcak and Maidens, 2018; Lew and Pavone, 2020; Alanwar et al., 2021; Sun and Mitra, 2022; Qi "
      "et al., 2018).", join_previous="space"),
    T("p0002-b002",
      "Another data-driven approach to estimating reachable sets utilizes results from scenario optimization (Yang et "
      "al., 2017; Sartipizadeh et al., 2019; Devonport and Arcak, 2020b). This approach reduces the assumptions "
      "imposed on a system and can be applied to any system which admits simulation. Scenario optimization is an "
      "approach to solving chance-constrained optimization problems by solving a non-probabilistic relaxation of the "
      "original problem (Dembo, 1991). Scenario optimization has been used in solving robust control problems "
      "(Marseglia et al., 2014) and specifically problems related to reachability (Hewing and Zeilinger, 2020; Xue et "
      "al., 2020)."),
    T("p0002-b003",
      "In this paper, we generalize the scenario-based reachability method of (Devonport and Arcak, 2020b). The "
      "scenario formalism therein is restricted to the convex case, which features critically in the construction of "
      "the probabilistic safety guarantees. However, this formalism places certain formal restrictions, such as convex "
      "parameterization, that preclude many popular classes of estimators. We generalize to a nonconvex formalism that "
      "allows for a broader class of sets. In particular, both the parametric representation of the minimal reachable "
      "set estimator and the reachable set itself can be nonconvex. Additionally, the existing work of (Devonport and "
      "Arcak, 2020b) yields a-priori complexity bounds for a desired probability of a problem. Our presented approach "
      "does not require a-priori bounds, as we calculate the probability of the original problem after solving the "
      "relaxed optimization problem. This allows us to solve a problem given any number of samples and significantly "
      "decreases the computational cost in finding reachable sets through scenario optimization."),
    T("p0002-b004",
      "We present two approaches in Section 3, both of which allow nonconvex reachable set approximations. In the "
      "first approach we examine the union of partition cells, and in the second approach we examine the sum of radial "
      "basis functions, and use sublevel sets as reachable set estimates."),
    H("p0002-b005", "## 2. Nonconvex Scenario Optimization"),
    T("p0002-b006",
      r"Take $\Delta$ to be a probability space with a $\sigma$-algebra and a probability measure $\mathbf{P}$, and "
      r"let a *scenario*, $\delta$, be a random outcome from this probability space. Since probability $\mathbf{P}$ "
      r"is not known, it is not possible to directly compute the probability that an unseen scenario will violate a "
      r"given set of constraints. Instead we use these scenarios, $\delta^{(i)}$, to construct a scenario optimization "
      r"problem. Nonconvex scenario optimization (Campi et al., 2018; Garatti and Campi, 2024) is a technique to "
      r"a-posteriori evaluate the robustness level of a scenario solution. Consider any constrained optimization "
      r"problem of the form"),
    T("p0002-b007",
      "$$\n"
      r"\begin{aligned}" "\n"
      r"\underset{x \in \mathcal{X}}{\text{minimize}} \quad & f(x) \\" "\n"
      r"\text{subject to} \quad & x \in \bigcap_{i=1,\ldots,N} \mathcal{X}_{\delta^{(i)}}" "\n"
      r"\end{aligned} \tag{1}" "\n"
      "$$"),
    T("p0002-b008",
      r"where $x \in \mathcal{X} \subseteq \mathbb{R}^d$ is the decision variable, $\mathcal{X}_{\delta^{(i)}}$ are "
      r"constraints, and $\delta^{(1)}, ...\delta^{(N)}$ are $N$ independently and identically-distributed (i.i.d) "
      r"scenarios. There are no other restrictions on $f$ and $\mathcal{X}_\delta$."),
    T("p0002-b009",
      r"In solving (1), we aim to find a solution that is robust against constraint violation. The violation "
      r"probability of a given $x \in \mathcal{X}$ is defined as $V(x) = \mathbf{P}\{\delta \in \Delta : x \notin "
      r"\mathcal{X}_\delta\}$. Let $x_N^*$ be the solution to (1) and define the violation of (1) to be $V(x_N^*)$. "
      r"This is the probability that a new, randomly selected scenario, $\delta$, will violate the constraints of (1). "
      r"If $V(x_N^*) \le \epsilon$, then (1) is robust against constraint violation at level $\epsilon$. If the value "
      r"of $\epsilon$ we achieve in our a-posteriori evaluation is not at the intended level, we iteratively increase "
      r"$N$ and recalculate $\epsilon$. Therefore, this approach takes on a *wait-and-judge* perspective (Campi and "
      r"Garatti, 2018)."),
    O("p0002-b010", PAGENO),
]

# ----------------------------------------------------------------------------- page 3
NOTES[3] = r"""
Compared with the 170 dpi render and with 300 dpi / 280 dpi crops of the Theorem 1 region and of Section 3.
Running header 'NONCONVEX SCENARIO REACHABILITY' and page number 3 omitted. The extractor had scattered the
sub/superscripts of s_N^* over <sup> fragments and glued words ('.To calculate an estimate of'); the first
paragraph is rewritten from the render. Theorem 1 carries its printed bold label '**Theorem 1 ((Campi et al.,
2018), Theorem 1)**' (double parenthesis as printed, no period). The statement is set in upright type and the
PDF shows no visible end of the theorem; it is taken to end with display (3), because the next sentence ('If we
apply this general scenario theory to convex problems ...') speaks about Theorem 1 from outside. The four
extractor formula images are replaced by $$ blocks with the printed numbers: (2) epsilon(s_N^*) := cases {1 if
s_N^* = N; 1 - (N - s_N^*)-th root of beta / (N binom(N, s_N^*)) otherwise}, (3) P{V(x_N^*) > epsilon(s_N^*)}
<= beta., (4) the same cases with 'if s_N^* >= d' and denominator d binom(N, s_N^*), (5) R(theta) = {x in
R^{n_x} : g(x, theta) <= 0}. The root index, the binomial and the denominators N versus d were read on the
300 dpi crop. Kept as printed: 'We know s_N^* < d' (strict inequality, while (4) uses >= d), the upright
'd' in 'with d optimization variables', 'can transition to at time t_1 from state X_0' (calligraphic X_0),
calligraphic R used both for the reachable set and for its approximation, 'i.i.d' above the tilde without a
final period, the sentence fragment 'Given a set of samples ... D.'. Section heading '3. Nonconvex
Scenario-Based Reachability' set to level 2. Typed dots '...' in '{0, 1, ..., N}' are kept as three periods;
spaced dots are written \ldots.
"""
EPS2 = (r"\epsilon(s_N^*) := \begin{cases} 1 & \text{if } s_N^* = N, \\ 1 - \sqrt[N - s_N^*]{\dfrac{\beta}"
        r"{N \binom{N}{s_N^*}}} & \text{otherwise.} \end{cases}")
EPS4 = (r"\epsilon(s_N^*) := \begin{cases} 1 & \text{if } s_N^* \ge d, \\ 1 - \sqrt[N - s_N^*]{\dfrac{\beta}"
        r"{d \binom{N}{s_N^*}}} & \text{otherwise.} \end{cases}")
PAGES[3] = [
    O("p0003-b000", RUNHEAD),
    T("p0003-b001",
      r"We determine $\epsilon$ a-posteriori as a function of *support scenarios*. A scenario, $\delta$, is a "
      r"*support scenario* if its removal changes the solution of (1). We evaluate the number of support scenarios, "
      r"$s_N^*$, by re-solving (1) upon individual removal of each scenario. If removing an individual scenario "
      r"changes the solution to (1), then it is a support scenario. Through this process, we obtain an irreducible "
      r"set of support scenarios with cardinality $s_N^*$. To calculate an estimate of $\epsilon$ based on $s_N^*$, "
      r"$\epsilon(s_N^*)$, we first choose a confidence parameter, $\beta$, then calculate $\epsilon(s_N^*)$ through "
      r"Theorem 1."),
    T("p0003-b002",
      r"**Theorem 1 ((Campi et al., 2018), Theorem 1)** Given $\beta \in (0, 1)$, for any $s_N^* \in \{0, 1, ..., "
      r"N\}$, where $N$ is the number of scenario samples, let"),
    T("p0003-b003", "$$\n" + EPS2 + r" \tag{2}" + "\n$$"),
    T("p0003-b004", "Then, the following probability bound holds:"),
    T("p0003-b005", "$$\n" r"\mathbf{P}\{V(x_N^*) > \epsilon(s_N^*)\} \le \beta. \tag{3}" "\n$$"),
    T("p0003-b006",
      r"If we apply this general scenario theory to convex problems in which we restrict $\mathcal{X}_\delta$ from "
      r"(1) to be a family of convex constraints, we can bound the number of support scenarios. We know $s_N^* < d$ "
      r"where $d$ is the number of optimization variables. It is known that a convex optimization problem with d "
      r"optimization variables will never have more than $d$ support scenarios. Therefore, we refine the definition "
      r"of $\epsilon$ in Theorem 1 as follows:"),
    T("p0003-b007", "$$\n" + EPS4 + r" \tag{4}" + "\n$$"),
    H("p0003-b008", "## 3. Nonconvex Scenario-Based Reachability"),
    T("p0003-b009",
      r"We define a forward reachable set as $\mathcal{R} = \{\Phi(t_1; t_0, x_0, d) : x_0 \in \mathcal{X}_0, d \in "
      r"\mathcal{D}\}$ where $\mathcal{X}_0 \subseteq \mathbb{R}^{n_x}$ is the set of initial states, $\mathcal{D}$ "
      r"is the set of disturbance signals $d : [t_0, t_1] \to \mathbb{R}^{n_d}$, and $\Phi : \mathcal{X}_0 \times "
      r"\mathcal{D} \to \mathbb{R}^{n_x}$ is the state transition function. This is the set of all states to which "
      r"the system can transition to at time $t_1$ from state $\mathcal{X}_0$ at time $t_0$ subject to disturbances "
      r"in $\mathcal{D}$. Since we cannot compute exact reachable sets, we aim to compute an approximation, "
      r"$\mathcal{R}$, that is close to the true reachable set in a probabilistic sense."),
    T("p0003-b010",
      r"Let $X_0 \in \mathcal{X}_0$ and $D \in \mathcal{D}$ be random variables, define $R = \Phi(t_1; t_0, X_0, D)$, "
      r"and take accuracy parameter $\epsilon \in (0, 1)$ and confidence parameter $\beta \in (0, 1)$. Given a set of "
      r"samples $\delta^{(i)} = \Phi(t_1; t_0, x_{0i}, d_i), i = 1, \ldots, N$ where $x_{01}, \ldots, x_{0N} "
      r"\overset{i.i.d}{\sim} X_0$, $d_1, \ldots, d_N \overset{i.i.d}{\sim} D$. We will explore reachable set "
      r"estimates of the form"),
    T("p0003-b011", "$$\n" r"\mathcal{R}(\theta) = \{x \in \mathbb{R}^{n_x} : g(x, \theta) \le 0\} \tag{5}" "\n$$"),
    T("p0003-b012",
      r"where $g : \mathbb{R}^{n_x} \times \mathbb{R}^{n_\theta} \to \mathbb{R}$. In (5), $\theta$ represents a "
      r"parameterization of the class of admissible reachable set estimators: to fix a value of $\theta$ is to choose "
      r"an estimator."),
    O("p0003-b013", PAGENO),
]

# ----------------------------------------------------------------------------- page 4
NOTES[4] = r"""
Compared with the 170 dpi render and with two 280 dpi crops (top half: displays (6), (7); bottom half: Section
3.1 with displays (8), (9)). Running header and page number 4 omitted. The four extractor formula images are
replaced by $$ blocks with the printed numbers: (6) minimize over theta Vol(theta) subject to theta in the
intersection over i=1,...,N of {theta_i : g(delta^{(i)}, theta_i) <= 0}; (7) minimize Vol(theta) subject to
g(delta^{(i)}, theta) <= 0, i = 1, ..., N and theta in R^{n_theta}. (final period printed); (8) g(x, theta) =
sum_{i=1}^m theta_i f_i(x); (9) minimize -sum theta_i subject to sum theta_i 1_{A_i}(delta^{(j)}) <= 0, j = 1,
..., N and theta in [0,1]^m, (final comma printed). 'Vol' is printed upright (\mathrm{Vol}); the indicator is a
double-struck 1 (written \mathbb{1}). Subsection heading '3.1. Tiling with Basis Functions' set to level 3
(extractor had level 1). Line-wrap hyphens removed in 'guarantees' and 'nonconvex'; 'minimum-volume' is a
printed compound. Kept as printed: the subscript i on theta inside the set of (6); the upright 'A' in 'We then
partition A into m cells'; 'A_i cap A_j = emptyset forall i' (quantified over i only); the basis functions are
declared on R^D with capital D while the state space is R^{n_x} elsewhere. 'tiling' is italic twice in the print.
Typed dots '...' in 'f_1(x), ..., f_m(x)' and 'A_1, ..., A_m' kept as three periods.
"""
PAGES[4] = [
    O("p0004-b000", RUNHEAD),
    T("p0004-b001",
      r"We next fix a functional $\mathrm{Vol} : \mathbb{R}^{n_\theta} \to \mathbb{R}$ that represents the volume of "
      r"$\mathcal{R}(\theta)$. This motivates the following scenario program:"),
    T("p0004-b002",
      "$$\n"
      r"\begin{aligned}" "\n"
      r"\underset{\theta}{\text{minimize}} \quad & \mathrm{Vol}(\theta) \\" "\n"
      r"\text{subject to} \quad & \theta \in \bigcap_{i=1,\ldots,N} \{\theta_i : g(\delta^{(i)}, \theta_i) \le 0\}" "\n"
      r"\end{aligned} \tag{6}" "\n"
      "$$"),
    T("p0004-b003",
      r"The violation probability, $V(\mathcal{R}(\theta))$, of (6) may be interpreted as the probability that an "
      r"unseen scenario will violate the bounds of the reachable set estimate. Our goal is to select $\theta$ such "
      r"that the probability of $V(\mathcal{R}(\theta)) > \epsilon$ is less than or equal to $\beta$ while minimizing "
      r"$\mathrm{Vol}(\theta)$."),
    T("p0004-b004", "The proposed problem (6) can be equivalently expressed in the functional form"),
    T("p0004-b005",
      "$$\n"
      r"\begin{aligned}" "\n"
      r"\underset{\theta}{\text{minimize}} \quad & \mathrm{Vol}(\theta) \\" "\n"
      r"\text{subject to} \quad & g(\delta^{(i)}, \theta) \le 0, i = 1, \ldots, N \\" "\n"
      r"& \theta \in \mathbb{R}^{n_\theta}." "\n"
      r"\end{aligned} \tag{7}" "\n"
      "$$"),
    T("p0004-b006",
      r"The solution to (7) is the minimum-volume set that contains sample points $\delta^{(1)}, \ldots, "
      r"\delta^{(N)}$, and guarantees $\mathbf{P}\{V(\mathcal{R}(\theta)) > \epsilon\} \le \beta$. The algorithms we "
      r"present in this section solve (7) given arbitrary values of $\epsilon, \beta \in (0, 1)$ and $N$ samples."),
    H("p0004-b007", "### 3.1. Tiling with Basis Functions"),
    T("p0004-b008",
      r"We first present a method to construct a sublevel set function $g(x, \theta)$ that is convex in $\theta$ but "
      r"nonconvex in $x$, as was done in (Devonport, 2023). While convex scenario optimization methods can be used to "
      r"analyze this approach, they require large sample sizes and are not computationally efficient. We show that by "
      r"utilizing the nonconvex scenario optimization tools introduced in Section 2, we can significantly improve "
      r"upon these limitations. To construct $g(x, \theta)$, select a finite set of basis functions $f_1(x), ..., "
      r"f_m(x) : \mathbb{R}^D \to \mathbb{R}$ and take $g$ to be"),
    T("p0004-b009", "$$\n" r"g(x, \theta) = \sum_{i=1}^{m} \theta_i f_i(x) \tag{8}" "\n$$"),
    T("p0004-b010",
      r"In this section, we will use this approach to construct a *tiling* of the state space and estimate the "
      r"reachable set of a given problem. To create this *tiling*, assume that the reachable set, $\mathcal{R}$, is "
      r"contained in a subset $A \subseteq \mathbb{R}^D$. We then partition A into $m$ cells, creating a collection of "
      r"sets $A_1, ..., A_m$ such that $\cup_{i=1}^{m} A_i = A$ and $A_i \cap A_j = \emptyset\ \forall i$. This "
      r"approach can produce arbitrarily fine estimates of the reachable set, depending on how refined the partition "
      r"is. The accuracy of the partition increases as $m$ increases. Further, we define $\mathbb{1}_{A_i}$ to be the "
      r"zero-one indicator function for the set $A_i$, so that $\mathbb{1}_{A_i}(x) = 1$ if $x \in A_i$ and "
      r"$\mathbb{1}_{A_i}(x) = 0$ otherwise. Therefore, the reachable set estimate is a union of the partitioned "
      r"cells. We write this as a constrained optimization problem:"),
    T("p0004-b011",
      "$$\n"
      r"\begin{aligned}" "\n"
      r"\underset{\theta}{\text{minimize}} \quad & -\sum_{i=1}^{m} \theta_i \\" "\n"
      r"\text{subject to} \quad & \sum_{i=1}^{m} \theta_i \mathbb{1}_{A_i}(\delta^{(j)}) \le 0, \quad j = 1, \ldots, N \\" "\n"
      r"& \theta \in [0, 1]^m," "\n"
      r"\end{aligned} \tag{9}" "\n"
      "$$"),
    O("p0004-b012", PAGENO),
]

# ----------------------------------------------------------------------------- page 5
NOTES[5] = r"""
Compared with the 170 dpi render, 280-300 dpi crops of the three regions (text above Algorithm 1, the
algorithm box, Section 3.2) and a 600 dpi crop of display (10). Running header and page number 5 omitted. The
first paragraph follows display (9) of page 4 without indentation; it starts a new sentence, so no join is
needed. The extractor had fragmented Algorithm 1 into twelve list items; they are replaced by one image crop
(figure item, asset algorithm-1, both rules of the box inside the crop) followed by a text transcription: bold
printed title line, then one paragraph per printed line with the printed line numbers 1-11 and nesting shown by
'&emsp;&emsp;' per level (lines 5, 6, 10 at level 1 inside the while loop; lines 7-9 at level 2 inside the for
loop). Kept as printed in the algorithm: capital Phi in the input line but lower-case phi in line 8; 'A_j in
R(theta) iff theta = 0' (theta without subscript); 'Initialize theta_j = 1'; 'while epsilon is large do' with
no numeric threshold; line 9 uses the index i both for the sample delta^{(i)} and for the cell A_i; 'using
Equation 4' printed without parentheses; no 'end' lines. The two extractor formula images are replaced by $$
blocks: (10) f(x, mu, sigma) = exp(-(1/2)(x - mu_i)^2 / sigma_i^2) - the subscripts i on mu and sigma in the
exponent are printed although the left-hand side has none (read at 600 dpi); (11) g(x, theta) = sum_{i=1}^m
f(x, mu_i, sigma_i) - gamma. Subsection heading '3.2. Radial Basis Functions (RBFs)' set to level 3. The last
paragraph ('Figure 1 demonstrates ... If m is larger than') continues on page 6 after the Figure 1 float.
Typed dots in '{1, ..., N}', 'A_1, ..., A_m', 'theta_1, ..., theta_m' kept as three periods; spaced dots are \ldots.
"""
ALG1 = "\n\n".join([
    r"**Algorithm 1** : Scenario reachability through tiling",
    r"1: **Input**: Black-box transition function model $\Phi(t_1; t_0, x_0, d)$; Random variables $X_0$ and $D$; "
    r"Partition dimension $m$; Batch size $B$; Confidence parameter $\beta \in (0, 1)$.",
    r"2: **Output**: $\theta_1, ..., \theta_m$ corresponding to union of cells $A_j$ such that $A_j \in "
    r"\mathcal{R}(\theta)$ iff $\theta = 0$; Robustness against constraint violation $\epsilon$.",
    r"3: **Initialize** $\theta_j = 1$",
    r"4: **while** $\epsilon$ is large **do**",
    r"5: &emsp;&emsp;$N = (B \cdot \text{number of iterations})$",
    r"6: &emsp;&emsp;**for all** $i \in \{1, ..., N\}$ **do**",
    r"7: &emsp;&emsp;&emsp;&emsp;Take samples $x_{0i} \sim X_0, d_i \sim D$",
    r"8: &emsp;&emsp;&emsp;&emsp;Evaluate $\delta^{(i)} = \phi(t_1; t_0, x_{0i}, d_i)$",
    r"9: &emsp;&emsp;&emsp;&emsp;If $\delta^{(i)} \in A_i$, then set $\theta_i = 0$",
    r"10: &emsp;&emsp;**calculate** $\epsilon$ using Equation 4 where $s_N^* = |\mathcal{R}(\theta)|$ and $d = m$.",
    r"11: **return** $\theta_1, \ldots, \theta_m$; $\epsilon$",
])
ALG1_BOX = [86, 247, 526, 451]
PAGES[5] = [
    O("p0005-b000", RUNHEAD),
    T("p0005-b001",
      r"To satisfy the scenario constraints, we set $\theta_i = 0\ \forall i$ such that scenario $\delta^{(j)} \in "
      r"A_i$ for at least one $j \in \{1, ..., N\}$. To minimize the objective while respecting $\theta \in [0, 1]^m$ "
      r"we set $\theta_i = 1$ for all other $A_i$. Therefore, $\mathcal{R}(\theta)$ is the solution to (9), the union "
      r"of cells $A_i$ that contain one or more scenarios $\delta^{(j)}$. This is the minimum volume union of cells "
      r"that contains all scenarios, $\delta^{(1)}, \ldots, \delta^{(N)}$."),
    T("p0005-b002",
      r"We define a support scenario to be the first scenario, $\delta^{(j)}$, in any cell $A_i$. While this set of "
      r"support scenarios is not unique, it is irreducible. These scenarios represent the smallest set of reachable "
      r"states that is possible without changing the solution to (9). This satisfies the conditions needed to obtain "
      r"the number of support scenarios, $s_N^*$. We calculate $\epsilon$ a-posteriori using (4) with $s_N^*$ and the "
      r"number of optimization variables, $d$ (the number of cells in our partition). If the obtained $\epsilon$ does "
      r"not satisfy the necessary bounds, we iteratively increase the number of samples, $N$, and repeat the process. "
      r"This reachability algorithm based on partition $A_1, ..., A_m$ is described in Algorithm 1."),
    F("p0005-alg1", "Algorithm 1", "algorithm-1", ALG1_BOX),
    T("p0005-alg1-text", ALG1, bbox=ALG1_BOX),
    H("p0005-b015", "### 3.2. Radial Basis Functions (RBFs)"),
    T("p0005-b016",
      r"We now turn to a method that allows nonconvexity in both parameters, $\theta$ and $x$. Unlike the method "
      r"proposed in Section 3.1, this method is not amenable to existing approaches, such as those presented in "
      r"(Devonport and Arcak, 2020b; Devonport, 2023). In this approach, we construct $g(x, \theta)$ from a finite set "
      r"of RBFs. We define a RBF, $f(x, \mu, \sigma)$, to be a Gaussian function of $x, \mu, \sigma,$ such that"),
    T("p0005-b017",
      "$$\n" r"f(x, \mu, \sigma) = e^{-\frac{1}{2} \frac{(x - \mu_i)^2}{\sigma_i^2}} \tag{10}" "\n$$"),
    T("p0005-b018", r"where $\mu$ is the center of a RBF and $\sigma$ is the width of a RBF. We take $g$ to be"),
    T("p0005-b019", "$$\n" r"g(x, \theta) = \sum_{i=1}^{m} f(x, \mu_i, \sigma_i) - \gamma \tag{11}" "\n$$"),
    T("p0005-b020", r"Therefore, $\theta = (\mu_1, \ldots, \mu_m; \sigma_1, \ldots, \sigma_m; \gamma)$."),
    T("p0005-b021",
      r"Figure 1 demonstrates that RBFs are particularly well-suited for constructing reachable sets due to the tail "
      r"interactions that allow multiple RBFs to connect into shapes more complicated than unions of ellipsoids. This "
      r"approach allows the number of RBFs, $m$, to be arbitrarily set. If $m$ is larger than"),
    O("p0005-b022", PAGENO),
]

if __name__ == "__main__":
    write_pages(PAGES, NOTES)
