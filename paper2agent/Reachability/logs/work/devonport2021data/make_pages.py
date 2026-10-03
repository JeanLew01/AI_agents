#!/usr/bin/env python3
"""Rebuild the reviewed page JSONs for devonport2021data from the backed-up extractor output.

Idempotent: always reads SCRATCH/orig-pages/page-NNNN.json and rewrites D/pages/page-NNNN.json.
Each page is a list of (id, kind, bbox_spec, markdown, extras). bbox_spec is either a list of four
numbers or a tuple of original item ids whose bboxes are unioned.
"""
import json
import sys
from pathlib import Path

R = Path.home() / "AI_agents/paper2agent/Reachability"
D = R / "paper-review/devonport2021data-paper/documents/s001-devonport2021data"
S = R / "logs/work/devonport2021data"

PAGES = {}
NOTES = {}


def page(n, notes, items):
    PAGES[n] = items
    NOTES[n] = " ".join(notes.split())


# ---------------------------------------------------------------- page 1
page(1, r"""
Compared with the 170 dpi render of PDF page 1 and with the authors' TeX source (cfun-paper.tex).
Vertical arXiv stamp in the left margin set to omit. Title kept as the single level-1 heading (bold
markers removed). Author block rewritten as four printed lines; the e-mail line was damaged by the
extractor ('alex ~~d~~ evonport') and is restored as printed in typewriter type
'{alex_devonport,forestyang,elghaoui,arcak}@berkeley.edu'. The run-in label 'Abstract—' is
represented by a '## Abstract' heading and the abstract's bold face was dropped; 'non-convex' is a
real compound hyphen broken at a line end (confirmed in TeX). 'I. INTRODUCTION' (small caps) written
in title case; the unnumbered italic subsection 'Notation' is a level-3 heading. The paragraph that
runs from the bottom of the left column into the right column ('Others incorporate data-driven
elements | into more traditional ...') was merged. 'plug-in approach' is a real compound hyphen
(extractor had 'plugin'). Inline math ($\mathbb{R}^n$, $a,b$) rewritten in LaTeX from the TeX source
(macro \R expanded). The last sentence of the page is an inline formula split by the page break:
the page prints '[a,b] = {x in R^n | a <= x <=' and page 2 starts with 'b}'. To keep the formula one
LaTeX expression, the two glyphs 'b}' printed at the top of page 2 are transcribed here, and the
page-2 item continues with ', where' using join_previous 'none'. Citation numbers [1]-[15] checked
against the page image.
""", [
    ("p0001-b000", "omit", ("p0001-b000",), "", {"reason": "Vertical arXiv stamp in the left margin ('arXiv:2104.13902v1 [eess.SY] 28 Apr 2021'); page furniture, the version is recorded in the conversion notes."}),
    ("p0001-b001", "heading", ("p0001-b001",), "# Data-Driven Reachability Analysis with Christoffel Functions", {}),
    ("p0001-b002", "text", ("p0001-b002", "p0001-b003", "p0001-b004"),
     "Alex Devonport, Forest Yang, Laurent El Ghaoui, Murat Arcak\n"
     "Electrical Engineering and Computer Sciences\n"
     "University of California, Berkeley\n"
     "`{alex_devonport,forestyang,elghaoui,arcak}@berkeley.edu`", {}),
    ("p0001-abstract-h", "heading", [53.0, 175.0, 120.0, 186.0], "## Abstract", {}),
    ("p0001-b005", "text", ("p0001-b005",),
     "We present an algorithm for data-driven reachability analysis that estimates finite-horizon forward reachable sets for general nonlinear systems using level sets of a certain class of polynomials known as Christoffel functions. The level sets of Christoffel functions are known empirically to provide good approximations to the support of probability distributions: the algorithm uses this property for reachability analysis by solving a probabilistic relaxation of the reachable set computation problem. We also provide a guarantee that the output of the algorithm is an accurate reachable set approximation in a probabilistic sense, provided that a certain sample size is attained. We also investigate three numerical examples to demonstrate the algorithm’s capabilities, such as providing non-convex reachable set approximations and detecting holes in the reachable set.", {}),
    ("p0001-b006", "heading", ("p0001-b006",), "## I. Introduction", {}),
    ("p0001-b007", "text", ("p0001-b007",),
     "A popular and effective way to guarantee the safety of a system in the face of uncertainty is *reachability analysis*, a set-based method that characterizes all possible evolutions of the system by computing reachable sets. Many algorithms in reachability analysis use detailed system information to compute a sound approximation to the reachable set, that is an approximation guaranteed to completely contain (or be contained in) the reachable set. However, in many important applications, such as complex cyber-physical systems that are only accessible through simulations or experiments, this detailed system information is not available, so these algorithms cannot be applied.", {}),
    ("p0001-b008", "text", ("p0001-b008",),
     "Applications such as these motivate *data-driven* reachability analysis, which studies algorithms to estimate reachable sets using the type of data that can be obtained from experiments and simulations. These algorithms have the advantage of being able to estimate the reachable sets of any system whose behavior can be simulated or measured experimentally, without requiring any additional mathematical information about the system. The main disadvantage of data-driven reachability algorithms is that generally they cannot provide the same type of soundness guarantees as traditional reachability analysis algorithms; however, they can still guarantee accuracy of the estimates in a probabilistic sense with high confidence.", {}),
    ("p0001-b009", "text", ("p0001-b009",),
     "Data-driven reachability is a rapidly growing area of research within reachability analysis. Many recent developments focus either on providing probabilistic guarantees of correctness for data-driven methods that estimate the reachable set directly from data, for instance using results from statistical learning theory [1] or scenario optimization [2], [3], [4], [5], [6], [7]. Others incorporate data-driven elements into more traditional reachability approaches, for instance estimating entities such as discrepancy functions [8] or differential inclusions [9]. Finally, other developments include incorporating data-driven reachability into verification tools for cyber-physical systems [8], [10].", {}),
    ("p0001-b011", "text", ("p0001-b011",),
     r"This paper investigates a data-driven reachability algorithm that directly estimates the reachable set from data using the sublevel sets of an empirical inverse Christoffel function, and provides a probabilistic guarantee of accuracy for the method using statistical learning-theoretic methods. Christoffel functions are a class of polynomials defined with respect to measures on $\mathbb{R}^n$: a single measure defines a family of Christoffel function polynomials. When the measure in question is defined by a probability distribution on $\mathbb{R}^n$ the level sets of Christoffel functions are known empirically to provide tight approximations to the support. This support-approximating quality has motivated the use of Christoffel functions in several statistical applications, such as density estimation [11], [12] and outlier detection [13]. Additionally, the level sets have been shown, using the plug-in approach [14], to converge exactly to the support of the distribution (in the sense of Hausdorff measure) when the degree of the polynomial approaches infinity, and when the true probability distribution is available [12]. When the true probability distribution is *not* known, as is typically the case in data analysis, the Christoffel function can be empirically estimated using a point cloud of independent and identically distributed (iid) samples from the distribution: this *empirical Christoffel function* still provides accurate estimates for the support, and some convergence results in this case are also known [15].", {}),
    ("p0001-b012", "text", ("p0001-b012",),
     "The contribution of this paper is twofold. First, we provide an algorithm which uses the level sets of a Christoffel function to estimate a reachable set using a point cloud of iid samples from the reachable set, which can be obtained through simulations by a Monte Carlo sampling scheme. Second, we provide a guarantee of the probabilistic accuracy of the reachable set estimate produced by the algorithm: provided that a certain (finite) sample size is attained, the level set provided by the algorithm is guaranteed to achieve a user-specified level of probabilistic accuracy with high confidence. Unlike the convergence results of [12], [15], this result holds for finite sample sizes and finite degrees.", {}),
    ("p0001-b013", "heading", ("p0001-b013",), "### Notation", {}),
    ("p0001-b014", "text", ("p0001-b014",),
     r"Given vectors $a,b\in\mathbb{R}^n$, a multidimensional interval (“interval” for brevity) is the set $[a,b]=\{x\in\mathbb{R}^n | a \le x \le b\}$", {}),
])

# ---------------------------------------------------------------- page 2
page(2, r"""
Compared with the 170 dpi render and 240-260 dpi crops of PDF page 2 and with the TeX source.
All inline and display mathematics rewritten in LaTeX from the TeX source with the authors' macros
expanded (\R -> \mathbb{R}, \initialset -> \mathcal{X}_0, \distset -> \mathcal{D},
\rs -> R_{[t_0,t_1]}, \ars -> \hat{R}_{[t_0,t_1]}) and checked symbol by symbol against the page;
no difference between TeX and PDF was found. The first item continues the inline formula from page 1
(join_previous 'none'): the glyphs 'b}' printed at the top of this page are transcribed at the end of
page 1. In the monomial example the authors' '~~' spacing was written as \quad (same printed
appearance; '~~' would be read as Markdown strikethrough). The six extractor 'formula' image items
were replaced by $$...$$ text items; none of the displays on this page carries a printed equation
number (the paper numbers only the three displays it refers to), so no \tag was added. Section
headings: 'II. PRELIMINARIES' in title case, subsections A and B as level 3. 'Remark 1:' and
'Problem 1:' start their items with the printed label in bold. The paragraph crossing from the left
to the right column ('... than $B$, in | the sense that ...') was merged. The extractor had scrambled
the last paragraph ('ismatrixcalled M-hat theis positive ...'); it is restored from the page.
Authors' wording kept as printed, including: 'the standard partial order $\mathbb{R}^n$' (no 'on'),
'a set $A\in\mathbb{R}^n$' (printed with the element sign, later $A\subseteq\mathbb{R}^n$),
$\Phi(t_1;t_0,x_0,u)$ with $u$ in Problem 1 (elsewhere $d$), 'several important application',
'samples $x^{(i)}$, $i=1,\dots,N$ samples from $\mu$'.
""", [
    ("p0002-b000", "text", ("p0002-b000",),
     r", where $\le$ is the standard partial order $\mathbb{R}^n$. Given a vector $x$, a subscript $x_i$ denotes the $i^{th}$ element of $x$. Given an ordered multiset of vectors (a collection of points in $\mathbb{R}^n$ for instance), a superscript $x^{(i)}$ denotes the $i^{th}$ member of the multiset. For $x\in\mathbb{R}^n$, the vector $z_k(x)\in\mathbb{R}^{\binom{n+k}{n}}$ denotes the vector of monomials of degree $\le k$, including degree zero, evaluated at $x$: for instance, if $n=2$ and $k=2$, then $z_k(x)=[1 \quad x_1 \quad x_2 \quad x_1x_2 \quad x_1^2 \quad x_2^2]^\top$. The space of polynomials of degree $\le d$ in $n$ variables is denoted $\mathbb{R}[x]^n_d$: note that elements of $z_d$, treated as polynomials, form a basis for $\mathbb{R}[x]^n_d$.",
     {"join_previous": "none"}),
    ("p0002-b001", "heading", ("p0002-b001",), "## II. Preliminaries", {}),
    ("p0002-b002", "heading", ("p0002-b002",), "### A. Probabilistic Reachability Analysis", {}),
    ("p0002-b003", "text", ("p0002-b003",),
     r"Consider a dynamical system with a state transition function $\Phi(t_1;t_0, x_0, d)$ that maps an initial state $x(t_0)=x_0\in\mathbb{R}^n$ at time $t_0$ to a unique final state at time $t_1$, under a disturbance $d:[t_0,t_1]\to\mathbb{R}^{w}$. For instance, when the system state dynamics $\dot{x}(t) = f(t,x(t),d(t))$ are known and have unique solutions on the interval $[t_0,t_1]$, then $\Phi(t_1;t_0, x_0, d)$ is just $x(t_1)$, where $x$ is the solution of the state dynamics with initial condition $x(t_0)=x_0$. In addition to representing exogenous disturbances, the disturbance signal $d$ may account for deviations of an input from a nominal control law.", {}),
    ("p0002-b004", "text", ("p0002-b004",),
     r"For the problem of forward reachability analysis, we are also given an *initial set* $\mathcal{X}_0\subset\mathbb{R}^n$, a set $\mathcal{D}$ of allowed disturbances and a time range $[t_0,t_1]$. The *forward reachable set* is then defined as the set of all states to which the system can transition in the time range $[t_0,t_1]$ with initial states in $\mathcal{X}_0$ and disturbances in $\mathcal{D}$, that is the set", {}),
    ("p0002-b005", "text", ("p0002-b005",),
     "$$\n" r"R_{[t_0,t_1]} = \{\Phi(t_1;t_0,x_0, d) : x_0\in\mathcal{X}_0, d\in\mathcal{D}\}." "\n$$", {}),
    ("p0002-b006", "text", ("p0002-b006",),
     r"To tackle the problem of estimating the forward reachable set by statistical means, we add probabilistic structure to the reachability problem that corresponds to taking random independent samples from the reachable set. Specifically, we take random variables $X_0$ and $D$ that take values on $\mathcal{X}_0$ and $\mathcal{D}$ respectively. These random variables then induce a random variable $\Phi(t_1;t_0, X_0, D)$ over the forward reachable set, whose probability measure we denote as $\mu$.", {}),
    ("p0002-b007", "text", ("p0002-b007",),
     r"**Remark 1:** The random variables $X_0$ and $D$ may have a physical significance, if the initial states, inputs, or disturbances are known to behave randomly in the problem at hand. However, they do not need to: they may be considered as *instrumental distributions* whose purpose is to provide a consistent rule for selecting initial states and disturbances at random.", {}),
    ("p0002-b008", "text", ("p0002-b008",),
     r"The measure $\mu(A)$ of a set $A\in\mathbb{R}^n$ has an intuitive interpretation: if we take samples $x_0$ and $d$ of the random variables $X_0$ and $D$, then the vector $\Phi(t_1;t_0,x_0,d)$ lies in $A$ with probability $\mu(A)$. Additionally, the smallest set of measure 1 is the reachable set. This interpretation motivates $\mu(A)$ as a measure of *probabilistic accuracy*: if a set $A\subseteq\mathbb{R}^n$ has a greater measure $\mu(A)$ than a set $B\subseteq\mathbb{R}^n$, then $A$ is a more accurate approximation of the reachable set than $B$, in the sense that it “misses” less of the probability mass than $B$ does. In the probabilistic version of the forward reachability problem, our goal is to find reachable set approximations $\hat{R}_{[t_0,t_1]}$ such that $\mu(\hat{R}_{[t_0,t_1]})$ is close to 1. Formally, we look to solve the following problem.", {}),
    ("p0002-b010", "text", ("p0002-b010",),
     r"**Problem 1:** Given the state transition function $\Phi(t_1;t_0, x_0, u)$, time range $[t_0,t_1]$, initial set $\mathcal{X}_0$, and disturbance set $\mathcal{D}$, the random variables $X_0$ and $D$, and an *accuracy level* $\epsilon\in(0,1)$, compute a set $\hat{R}_{[t_0,t_1]}$ such that $\mu(\hat{R}_{[t_0,t_1]}) \ge 1-\epsilon$.", {}),
    ("p0002-b011", "text", ("p0002-b011",),
     r"Selecting a set with high measure under $\mu$ is not sufficient to ensure a reasonable estimate, since the trivial solution $\hat{R}_{[t_0,t_1]}=\mathbb{R}^n$ satisfies $\mu(\hat{R}_{[t_0,t_1]})=1$. To avoid this problem we require some regularization, such as requiring that $\hat{R}_{[t_0,t_1]}$ be compact and penalizing estimates with high volume.", {}),
    ("p0002-b012", "heading", ("p0002-b012",), "### B. Christoffel Functions", {}),
    ("p0002-b013", "text", ("p0002-b013",),
     r"Given a finite measure $\mu$ on $\mathbb{R}^n$ and a positive integer $k$, the Christoffel function of order $k$ is defined as the ratio", {}),
    ("p0002-b014", "text", ("p0002-b014",),
     "$$\n" r"\kappa(x) = \frac{1}{z_k(x)^\top M^{-1}z_k(x)}," "\n$$", {}),
    ("p0002-b015", "text", ("p0002-b015",), r"where $M$ is the matrix of moments", {}),
    ("p0002-b016", "text", ("p0002-b016",),
     "$$\n" r"M = \int_{\mathbb{R}^n}z_k(x) z_k(x)^\top d\mu(x)" "\n$$", {}),
    ("p0002-b017", "text", ("p0002-b017",),
     r"and $z_k(x)$ is the vector of monomials of degree $\le k$. We assume throughout that $M$ is positive definite, ensuring that $M^{-1}$ exists. The Christoffel function has several important application in approximation theory, where its asymptotic properties are used to prove the regularity and consistency of Fourier series of orthogonal polynomials. For our purposes, it is more convenient to use the *inverse Christoffel function*", {}),
    ("p0002-b018", "text", ("p0002-b018",),
     "$$\n" r"{\kappa(x)}^{-1} = z_k(x)^\top M^{-1}z_k(x)," "\n$$", {}),
    ("p0002-b019", "text", ("p0002-b019",),
     r"which is a polynomial of degree $2k$. In Problem 1, and more generally in the problem of estimating a probability distribution from samples, $\mu$ is a probability measure which we do not *a priori* know. In this case, we instead use an empirical estimate of $\mu$ constructed from a collection of independently and identically distributed (iid) samples $x^{(i)}$, $i=1,\dots,N$ samples from $\mu$, namely", {}),
    ("p0002-b020", "text", ("p0002-b020",),
     "$$\n" r"\hat{\mu}=\frac{1}{N}\sum_{i=1}^N \delta_{x^{(i)}}," "\n$$", {}),
    ("p0002-b021", "text", ("p0002-b021",),
     r"where $\delta_x$ is the *Dirac measure* satisfying $\int f(y)d\delta_x(y)=f(x)$. The measure $\hat{\mu}$ itself defines a Christoffel function, whose inverse", {}),
    ("p0002-b022", "text", ("p0002-b022",),
     "$$\n" r"\begin{aligned}" "\n"
     r"C(x)&= \hat{\kappa}^{-1}(x)= z_k(x)^\top \hat{M}^{-1}z_k(x)\\" "\n"
     r"&= z_k(x)^\top \left( \frac{1}{N} \sum_{i=1}^N z_k(x^{(i)}) z_k(x^{(i)})^\top \right)^{-1}z_k(x)," "\n"
     r"\end{aligned}" "\n$$", {}),
    ("p0002-b023", "text", ("p0002-b023",),
     r"is called the *empirical inverse Christoffel function*. The matrix $\hat{M}$ is positive definite (and hence $\hat{M}^{-1}$ exists) if $N \ge \binom{n+k}{n}$ and the $x^{(i)}$ do not all belong to the zero set of a single degree $k$ polynomial.", {}),
])

# ---------------------------------------------------------------- page 3
ALG1 = "\n\n".join([
    r"**Algorithm 1:** Data-driven reachable set estimation by a sublevel set of an empirical inverse Christoffel function.",
    r"**Input:** Transition function $\Phi$ of a system with state dimension $n$; random variables $X_0$ and $D$ defined on $\mathcal{X}_0$ and $\mathcal{D}$ respectively; time range $[t_0, t_1]$; probabilistic guarantee parameters $\epsilon$ and $\delta$; Christoffel function order $k$.",
    r"**Output:** Set $\hat{R}_{[t_0,t_1]}$ representing an $\epsilon$-accurate reachable set estimate with confidence $1-\delta$.",
    r"Set number of samples",
    "$$\n" r"N = \left\lceil \frac{5}{\epsilon}\left( \log\frac{4}{\delta} + \binom{n+2k}{n} \log\frac{40}{\epsilon} \right)\right\rceil ." "\n$$",
    r"**forall** $i \in \{1,\dots,N\}$ **do**",
    r"&emsp;Take iid samples $x_0^{(i)}$ and $d^{(i)}$ from $X_0$ and $D$ respectively;",
    r"&emsp;evaluate $x_f^{(i)}=\Phi(t_1; t_0, x_0^{(i)}, d^{(i)})$.",
    r"**end**",
    r"Compute the matrix $\hat{M}^{-1}$ and level parameter $\alpha$, where",
    "$$\n" r"\begin{aligned}" "\n"
    r"\hat{M} &= \frac{1}{N} \sum_{i=1}^N z_k(x_f^{(i)})z_k(x_f^{(i)})^\top, \\" "\n"
    r"\alpha &= \max_{i=1,\dots,N} z_k(x_f^{(i)})^\top \hat{M}^{-1} z_k(x_f^{(i)})." "\n"
    r"\end{aligned}" "\n$$",
    r"Record the set",
    "$$\n" r"\hat{R}_{[t_0,t_1]}=\{x\in\mathbb{R}^n : z_k(x)^\top \hat{M}^{-1} z_k(x) \le \alpha\}" "\n$$",
    r"as the reachable set estimate.",
])

page(3, r"""
Compared with the 170 dpi render and 200-240 dpi crops of PDF page 3 and with the TeX source.
Reading order repaired: the extractor had interleaved the right column (Theorem 1 continuation,
Lemma 1) with the lower half of Algorithm 1. Order is now left column (Section III heading, intro
paragraph, Algorithm 1, the paragraph 'Since Algorithm 1 ...', start of Theorem 1) then right column.
Algorithm 1 (ruled algorithm2e box, between two paragraphs, it does not interrupt a sentence) is kept
as an image crop 'algorithm-1' (bbox checked on a 200 dpi render: both rules, title, Input/Output,
the three displays and the last line are inside; no neighbouring prose is inside), followed by a text
transcription taken from the TeX source and checked against the crop. The printed algorithm has no
line numbers; the loop body is marked with an em-space indent; the semicolon after 'respectively' and
the full stop after the sample-size display are as printed. All mathematics rewritten in LaTeX from the
TeX source (macros expanded: \ceil* -> \left\lceil..\right\rceil, \ind -> 1, \Ex -> \mathbb{E},
\ars, \initialset, \distset, \R; \dotsc written as \dots) and checked against the page; TeX and PDF
agree. Only the sample-size bound of Theorem 1 carries a printed number, (1), given as \tag{1}; the
other displays on this page are unnumbered in print (the authors use showonlyrefs). Theorem 1,
Lemma 1 ([16], Theorem 7.2), Lemma 2 ([17], Corollary 4) and Remark 2 start with the printed label
in bold; each statement is split into text and $$ items in printed order. Paragraph splits made
from the TeX source where the PDF prints no visible break: the theorem environment ends after
'... probability mass of $\mu$.' and the sentence 'The probability $1-\delta$ is the confidence ...'
is commentary (printed in the same paragraph); Lemma 2 ends at '$\ge 1-\delta$.' and 'Theorem 1
follows from Lemmas 1 and 2 because ...' is the proof sketch (printed on a new line without indent).
Authors' text kept as printed, including probable slips: in Lemma 2 'a sample of $M$ iid samples'
and '$i=1,\dots,n$' (the sum and the bound use $N$); in the proof sketch
$\text{Pos}(\mathbb{R}[x]^n_d)$ and 'the dimension of $\mathbb{R}[x]^n_d$ is $\binom{n+2k}{n}$'
(index $d$ printed, not $2k$); '$z(x)^\top \hat{M}^{-1} z(x)$' without the subscript $k$; and
$M^{-1}$ without a hat in the constraint of the optimization problem. The optimization problem,
which the extractor had turned into the text 'arg min alpha alpha>0 / subject to ...', is a $$ item.
The extractor's ten 'formula' image items on this page (five of them fragments of Algorithm 1) were
replaced by the algorithm crop and by $$ text items.
Remark 2 continues on page 4.
""", [
    ("p0003-b000", "heading", ("p0003-b000",), "## III. Christoffel Function Level Sets as Reachable Set Approximations", {}),
    ("p0003-b001", "text", ("p0003-b001",),
     r"The ability of level sets of Christoffel functions to estimate the support of probability distributions motivates Algorithm 1 as a data-driven strategy for solving Problem 1. Specifically, Algorithm 1 computes an empirical inverse Christoffel function $C(x)$ and a level parameter $\alpha\in\mathbb{R}$, and returns the sublevel set $\{x\in\mathbb{R}^n : C(x) \le \alpha\}$ as a proposed solution to Problem 1.", {}),
    ("p0003-alg1", "figure", [52.0, 178.0, 301.0, 582.0], "", {"label": "Algorithm 1", "asset_name": "algorithm-1"}),
    ("p0003-alg1-text", "text", [58.0, 183.0, 284.0, 578.0], ALG1, {}),
    ("p0003-b023", "text", ("p0003-b023",),
     r"Since Algorithm 1 is a randomized algorithm, it is possible that a particular run will produce an invalid solution to Problem 1. However, Theorem 1 guarantees that the probability that this occurs is no greater than $\delta$, a parameter that the user can specify in advance.", {}),
    ("p0003-b024", "text", ("p0003-b024",),
     r"**Theorem 1:** Let $C$ denote the empirical inverse Christoffel function for a point cloud $x^{(1)},\dots,x^{(N)}$ of iid samples from $\mu$, i.e.", {}),
    ("p0003-b025", "text", ("p0003-b025",),
     "$$\n" r"C(x)=z_k(x)^\top\left(\frac{1}{N}\sum_{i=1}^N z_k(x^{(i)})z_k(x^{(i)})^\top\right)^{-1}z_k(x)," "\n$$", {}),
    ("p0003-b008", "text", ("p0003-b008",),
     r"and let $\alpha = \max_i C(x^{(i)})$. Let $\mu^N$ denote the joint probability measure corresponding to $N$ iid samples from $\mu$. If", {}),
    ("p0003-b009", "text", ("p0003-b009",),
     "$$\n" r"N \ge \frac{5}{\epsilon}\left( \log\frac{4}{\delta} + \binom{n+2k}{n} \log\frac{40}{\epsilon} \right), \tag{1}" "\n$$", {}),
    ("p0003-b010", "text", ("p0003-b010",), "then", {}),
    ("p0003-b011", "text", ("p0003-b011", "p0003-b012"),
     "$$\n" r"\begin{aligned}" "\n"
     r"\mu^N\bigg(&\{(x^{(1)},\dots,x^{(N)}):\\" "\n"
     r"&\mu\left(\{x\in\mathbb{R}^n : C(x) \le \alpha\}\right) \ge 1-\epsilon\}\bigg) \ge 1-\delta." "\n"
     r"\end{aligned}" "\n$$", {}),
    ("p0003-b013", "text", [313.0, 183.0, 559.0, 205.0],
     r"This means that, with probability $\ge 1-\delta$, the $\alpha$-sublevel set of $C(x)$ contains at least $1-\epsilon$ of the probability mass of $\mu$.", {}),
    ("p0003-b013b", "text", [313.0, 205.0, 559.0, 263.0],
     r"The probability $1-\delta$ is the *confidence* that the solution is valid. For instance, suppose we set $\delta=10^{-9}$: then Theorem 1 gives us the confidence that there is less than a one in a billion chance that Algorithm 1 will fail to solve Problem 1.", {}),
    ("p0003-b014", "text", ("p0003-b014",),
     "The proof of this result is based on the following two results from statistical learning theory.", {}),
    ("p0003-b015", "text", ("p0003-b015",),
     r"**Lemma 1 ([16], Theorem 7.2):** Let $V$ be a vector space of functions $g:\mathbb{R}^n\to\mathbb{R}$ with dimension $m$. Then the class of sets", {}),
    ("p0003-b016", "text", ("p0003-b016",),
     "$$\n" r"\text{Pos}(V) = \left\{\ \{x | g(x)\ge 0\}, g\in V\right\}" "\n$$", {}),
    ("p0003-b017", "text", ("p0003-b017",), r"has Vapnik–Chervonenkis (VC) dimension $m$.", {}),
    ("p0003-b026", "text", ("p0003-b026",),
     r"**Lemma 2 ([17], Corollary 4):** Let $\mathcal{C}$ be a class of sets with VC dimension $m$. For a set $c\in\mathcal{C}$, let $\hat{\ell}(c)=\frac{1}{N}\sum_{i=1}^N 1\{x^{(i)}\notin c\}$ be the empirical error from a sample of $M$ iid samples from $\mu$, and let $\ell(c)=\mathbb{E}_\mu[1\{X\notin c\}]=1-\mu(c)$ be the generalization error. If", {}),
    ("p0003-b027", "text", ("p0003-b027",),
     "$$\n" r"N \ge \frac{5}{\epsilon}\left( \log\frac{4}{\delta} + m \log\frac{40}{\epsilon} \right)," "\n$$", {}),
    ("p0003-b028", "text", [313.0, 452.0, 559.0, 490.0],
     r"and if $\hat{\ell}(c)=0$, that is if all of the points $x^{(i)},\ i=1,\dots,n$ are contained in the concept $c$, then $\mu^N\left(\{x^{(1)},\dots,x^{(N)} : \ell(c) \le \epsilon\}\right) \ge 1-\delta$.", {}),
    ("p0003-b028b", "text", [313.0, 490.0, 559.0, 538.0],
     r"Theorem 1 follows from Lemmas 1 and 2 because the set $c=\{x\in\mathbb{R}^n | C(x) \le \alpha\}$ belongs to the class $\mathcal{C}=\text{Pos}(\mathbb{R}[x]^n_d)$ and satisfies $\hat{\ell}(c)=0$, and because the dimension of $\mathbb{R}[x]^n_d$ is $\binom{n+2k}{n}$.", {}),
    ("p0003-b029", "text", ("p0003-b029",),
     r"In addition to providing a high-confidence solution to Problem 1, Algorithm 1 also achieves the regularization goals mentioned at the end of Section II-A. In particular, the estimate $\hat{R}_{[t_0,t_1]}$ produced by Algorithm 1 is compact, since it is a sublevel set of the sum-of-squares polynomial $z(x)^\top \hat{M}^{-1} z(x)$. Furthermore, the level parameter $\alpha$ can equivalently be defined as the solution to the optimization problem", {}),
    ("p0003-b030", "text", [313.0, 636.0, 559.0, 669.0],
     "$$\n" r"\begin{aligned}" "\n"
     r"&\text{arg }\underset{\alpha > 0}{\text{min}} & & \alpha \\" "\n"
     r"&\text{subject to} & & z_k(x^{(i)})^\top M^{-1} z_k(x^{(i)}) \le \alpha,\ i=1,\dots,N." "\n"
     r"\end{aligned}" "\n$$", {}),
    ("p0003-b031", "text", [313.0, 672.0, 559.0, 710.0],
     r"In this problem, $\alpha$ acts as a penalty term for the volume of the sublevel set, since the volume increases monotonically with increasing $\alpha$.", {}),
    ("p0003-b032", "text", ("p0003-b032",),
     r"**Remark 2:** In some reachability problems, we are only interested in computing a reachable set for a subset of the state", {}),
])

# ---------------------------------------------------------------- page 4
page(4, r"""
Compared with the 170 dpi render and a 240 dpi crop of the right column of PDF page 4 and with the
TeX source. First item continues Remark 2 from page 3 (join_previous 'space'; the sentence
'... a subset of the state | variables.' was checked on both pages). All mathematics rewritten in
LaTeX from the TeX source and checked against the page; TeX and PDF agree. The five extractor
'formula' image items were replaced by $$...$$ text items: Duffing dynamics with the printed number
(2) as \tag{2}; the parameter values, quadrotor dynamics, initial-state intervals and input intervals
are unnumbered in print. The authors' 'split' environments are written as 'aligned'. Thousands
separators: the PDF prints '156, 626' (a math-mode comma, twice) and '46,052'; all are written as
plain '156,626' / '46,052' inside $...$ and the authors' \! spacing command was dropped so that the
numbers stay searchable. Headings: 'IV. EXAMPLES' in title case, subsections A and B as level 3.
Typewriter 'c5.24xlarge' kept in backticks. The paragraph crossing the column break ('... of the
empirical inverse | Christoffel function sublevel set ...') was merged. Line-wrap hyphens repaired
('numerical', 'random'); 'reduced-state' is a real compound hyphen broken at a line end (extractor
had 'reducedstate'). Authors' text kept as printed, including: 'The initial is the interval'
(no 'set'), 'the assertion of Proposition 1' (the result is Theorem 1; the paper has no
Proposition), '$N_{ap}$' in lower case followed by '$N_{AP}$', 'within 1% of the true'. All numbers
(0.05, 0.4, 1.3, [0.95,1.05], [-0.05,0.05], [0,100], k=10, 10^{-9}, 156,626, 39 minutes, 41 seconds,
46,052, 99.99%, 2x10^{-5}, 0.99, 0.95, g=9.81, K=0.89/1.4, d_0=70, d_1=17, n_0=55, the six initial
intervals, the two input intervals, [0,5]) were checked against the page image. Figure 1, which
is discussed in the paragraph 'Figure 1 shows ...' on this page, is printed on page 5; plan.json
reading_order places the figure and its caption directly after that paragraph. The last sentence
continues on page 5.
""", [
    ("p0004-b000", "text", ("p0004-b000",),
     r"variables. For example, suppose the state is $(x_1,\dots,x_n)\in\mathbb{R}^n$, and we wish to verify a safety specification involving only the states $x_1,\dots,x_m$, where $m<n$: a reachable set for the states $x_1,\dots,x_m$ would suffice for this problem. In cases like this, Algorithm 1 can be modified to use only the first $m$ elements of the samples $x_f^{(i)}$. The output of the algorithm is then an empirical inverse Christoffel function with domain $\mathbb{R}^m$ whose sublevel set $\hat{R}_{[t_0,t_1]}$ estimates the reachable set for the reduced set of states. In the sequel, we refer to this application of Algorithm 1 as the *reduced-state variant* of Algorithm 1.",
     {"join_previous": "space"}),
    ("p0004-b001", "heading", ("p0004-b001",), "## IV. Examples", {}),
    ("p0004-b002", "text", ("p0004-b002",),
     "This section demonstrates Algorithm 1’s ability to make accurate estimates of forward reachable sets with three numerical examples. We demonstrate how the parallel nature of the algorithm can be leveraged to improve computation times by running all experiments on two computing platforms: (i) a laptop with 4 2.6 GHz cores; and (ii) an instance of the AWS EC2 computing platform `c5.24xlarge`, a virtual machine with 96 3.6 GHz cores.", {}),
    ("p0004-b003", "heading", ("p0004-b003",), "### A. Chaotic Nonlinear Oscillator", {}),
    ("p0004-b004", "text", ("p0004-b004",),
     "The first example is a reachable set estimation problem for the nonlinear, time-varying system with dynamics", {}),
    ("p0004-b005", "text", ("p0004-b005",),
     "$$\n" r"\begin{aligned}" "\n"
     r"\dot{x} &= y \\" "\n"
     r"\dot{y} &= -\alpha y + x - x^3 + \gamma\cos(\omega t)," "\n"
     r"\end{aligned} \tag{2}" "\n$$", {}),
    ("p0004-b006", "text", ("p0004-b006",),
     r"with states $x,y\in\mathbb{R}$ and parameters $\alpha, \gamma, \omega\in\mathbb{R}$. This system is known as the *Duffing oscillator*, a nonlinear oscillator which exhibits chaotic behavior for certain values of $\alpha$, $\gamma$, and $\omega$, for instance", {}),
    ("p0004-b007", "text", ("p0004-b007",),
     "$$\n" r"\begin{aligned}" "\n"
     r"\alpha &= 0.05, & \gamma &= 0.4, & \omega &= 1.3." "\n"
     r"\end{aligned}" "\n$$", {}),
    ("p0004-b008", "text", ("p0004-b008",),
     r"The initial is the interval such that $x(0)\in[0.95, 1.05]$, $y(0)\in[-0.05,0.05]$, and we take $X_0$ to be the uniform random variable over this interval. The time range is $[t_0,t_1]=[0,100]$.", {}),
    ("p0004-b009", "text", ("p0004-b009",),
     r"We use Algorithm 1 to compute a reachable set for (2) using an order $k=10$ empirical inverse Christoffel function with accuracy and confidence parameters $\epsilon=0.05$, $\delta=10^{-9}$. With these parameters, (1) states that $N=156,626$ samples are required to ensure that Theorem 1 holds for the reachable set estimate. Total computation times for this example were 39 minutes on the laptop, and 41 seconds on `c5.24xlarge`.", {}),
    ("p0004-b010", "text", ("p0004-b010",),
     r"Figure 1 shows the reachable set estimate for the Duffing oscillator system with the problem data given above, and the point cloud of $156,626$ samples used to compute the empirical inverse Christoffel function and the level parameter $\alpha$. The reachable set estimate is neither convex nor simply connected, closely following the boundaries of the cloud of points and excluding an empty region within the cloud of points.", {}),
    ("p0004-b011", "text", ("p0004-b011",),
     r"To experimentally verify that the assertion of Proposition 1 holds for the reachable set estimate, we compute an *a posteriori* estimate of the accuracy of the empirical inverse Christoffel function sublevel set. To do this, we first compute a new set of sample points of size $N_{ap}$. Denoting by $N_{out}$ the number of new samples that lie outside of the reachable set estimate, we can compute the empirical accuracy of a reachable set approximation as $1-N_{out}/N_{AP}$. We use $N_{AP}=46,052$ sample points to make the *a posteriori* estimate. This sample size ensures that a one-sided Chernoff bound holds, which guarantees that empirical accuracy is within 1% of the true with 99.99% confidence. The *a posteriori* empirical accuracy computed with this sample is $1-(2\times 10^{-5})$, ensuring that the true accuracy of the reachable set estimate is at least $0.99-2\times10^{-5}$ with 99.99% confidence. This is well in excess of the $0.95$ accuracy guaranteed by Theorem 1.", {}),
    ("p0004-b013", "heading", ("p0004-b013",), "### B. Planar Quadrotor Model", {}),
    ("p0004-b014", "text", ("p0004-b014",),
     "The next example is a reachable set estimation problem for horizontal position and altitude in a nonlinear model of the planar dynamics of a quadrotor used as an example in [18], [19]. The dynamics for this model are", {}),
    ("p0004-b015", "text", ("p0004-b015",),
     "$$\n" r"\begin{aligned}" "\n"
     r"\ddot{x} &= u_1 K\sin(\theta)\\" "\n"
     r"\ddot{h} &= -g + u_1 K\cos(\theta) \\" "\n"
     r"\ddot{\theta} &= -d_0\theta - d_1\dot{\theta} + n_0 u_2," "\n"
     r"\end{aligned}" "\n$$", {}),
    ("p0004-b016", "text", ("p0004-b016",),
     r"where $x$ and $h$ denote the quadrotor’s horizontal position and altitude in meters, respectively, and $\theta$ denotes its angular displacement (so that the quadrotor is level with the ground at $\theta=0$) in radians. The system has 6 states, which we take to be $x$, $h$, $\theta$, and their first derivatives. The two system inputs $u_1$ and $u_2$ (treated as disturbances for this example) represent the motor thrust and the desired angle, respectively. The parameter values used (following [19]) are $g=9.81$, $K=0.89/1.4$, $d_0=70$, $d_1=17$, and $n_0=55$. The set of initial states is the interval such that", {}),
    ("p0004-b017", "text", ("p0004-b017",),
     "$$\n" r"\begin{aligned}" "\n"
     r"x(0)&\in[-1.7, 1.7], & \dot{x}(0)&\in[-0.8, 0.8], \\" "\n"
     r"h(0)&\in[0.3, 2.0], & \dot{h}(0)&\in[-1.0, 1.0], \\" "\n"
     r"\theta(0)&\in[-\pi/12, \pi/12], & \dot{\theta}(0)&\in[-\pi/2, \pi/2]," "\n"
     r"\end{aligned}" "\n$$", {}),
    ("p0004-b018", "text", ("p0004-b018",),
     r"the set of inputs is the set of constant functions $u_1(t)=u_1$, $u_2(t)=u_2$ $\forall t\in[t_0,t_1]$, whose values lie in the interval", {}),
    ("p0004-b019", "text", ("p0004-b019",),
     "$$\n" r"\begin{aligned}" "\n"
     r"u_1&\in[-1.5+ g/K, 1.5 + g/K], & u_2&\in[-\pi/4, \pi/4]," "\n"
     r"\end{aligned}" "\n$$", {}),
    ("p0004-b020", "text", ("p0004-b020",),
     r"and we take $X_0$ and $D$ to be the uniform random variables defined over these intervals. The time range is $[t_0,t_1]=[0,5]$. We take probabilistic parameters $\epsilon=0.05$, $\delta=10^{-9}$. Since the goal of this example is to estimate a reachable set for the horizontal position and altitude only, we are interested in a reachable set for a subset of the state variables, namely $x$ and $h$. As mentioned in Remark 2, Algorithm 1 can be used to estimate a reachable set for $x$ and $h$ in two ways: we can either compute a Christoffel function estimate for the reachable set and take the “shadow projection” of the estimate onto $x$ and $h$, or we could compute a Christoffel function estimate for $x$ and $h$ directly using the reduced-state variant of Algorithm 1 with the $(x,h)$ components of the reachable set data. To compare the relative accuracy", {}),
])

# ---------------------------------------------------------------- page 5
page(5, r"""
Compared with the 170 dpi render and 260-300 dpi crops (equation (3), monotonicity paragraph) of PDF
page 5 and with the TeX source. Item order changed so that prose reads continuously: the page prints
the full-width Figure 1 at the top, but the first prose line ('and computational expense of these
methods ...') continues the last sentence of page 4, so that item comes first (join_previous
'space'), then Figure 1 with its caption, Figure 2 with its caption, the paragraph 'Figure 2 shows
...', then the right column (IV-C). In the package, plan.json reading_order additionally moves
Figure 1 and its caption out of Section IV-B to Section IV-A (after the paragraph 'Figure 1 shows
...' of page 4), because the float belongs to the Duffing example and LaTeX placed it at the top of
this page only for layout. Figure 1 (two panels, Duffing oscillator; discussed in Section
IV-A on page 4) and Figure 2 are kept as image crops; bboxes checked on wider 150/200 dpi renders:
all tick labels and the axis labels x, y, h are inside, captions are outside. Captions transcribed
verbatim with the printed prefix 'Fig. 1.' / 'Fig. 2.'. Mathematics rewritten in LaTeX from the TeX
source and checked against the page; TeX and PDF agree. Equation (3) (traffic dynamics) is a $$ item
with \tag{3}; 'split' written as 'aligned'. Its parentheses are kept exactly as printed, including
the unbalanced third line '... - \min(c, vx_{n}))\right),' which prints three closing parentheses
where two would balance, and the symbol $\beta$, which the text never defines. Thousands separators
'2,009,600' and '32,292' written plainly (authors' \! dropped). Real compound hyphens broken at line
ends restored from the TeX source: 'continuous-time', 'order-preserving', 'full-state',
'$n$-dimensional'; line-wrap hyphens repaired ('expensive', 'maximum', 'monotonicity'). Authors'
text kept as printed, including: 'Both reachable estimates', 'Traffic enters segment through $x_1$',
'The input $u$ represents the influx' (the equation uses $d$), 'in the range range',
$\overline{x}$ in (3) versus $\bar{x}$ in the following text, and '$t\in[0,T]$' / '$x^{(1)}(T)$' in
the monotonicity definition. Numbers checked against the page: k=4, n=6, N=2,009,600, n=2,
N=32,292, 77 minutes, 2 minutes, 78 seconds, 2 seconds, T=30, v=0.5, w=1/6, x-bar=320, [100,200],
[40/T,60/T], [0,4T], citations [20], [21], [22]. The last sentence continues on page 6.
""", [
    ("p0005-b002", "text", ("p0005-b002",),
     r"and computational expense of these methods, we compute a reachable set estimate for $(x,h)$ using both methods.",
     {"join_previous": "space"}),
    ("p0005-b000", "figure", ("p0005-b000",), "", {"label": "Figure 1", "asset_name": "figure-1"}),
    ("p0005-b001", "caption", ("p0005-b001",),
     "Fig. 1. *Left*: reachable set estimate for the Duffing oscillator system (blue contour), the cloud of 156,626 samples used to compute the empirical inverse Christoffel function (grey points), and the initial set (black box). *Right*: enlarged version of the region in the left plot enclosed by the red box, showing the region excluded from the reachable set.", {}),
    ("p0005-b003", "figure", ("p0005-b003",), "", {"label": "Figure 2", "asset_name": "figure-2"}),
    ("p0005-b004", "caption", ("p0005-b004",),
     r"Fig. 2. Reachable set estimates for the horizontal position and altitude of the planar quadrotor model, computed by projecting the output of Algorithm 1 onto $(x,h)$ (blue) and using the modification of Algorithm 1 mentioned in Remark 2, where the algorithm is run using only the $(x,h)$ components of the data (orange).", {}),
    ("p0005-b005", "text", ("p0005-b005",),
     r"Figure 2 shows the reachable set estimates computed using both methods using order $k=4$ inverse empirical Christoffel functions. Both reachable estimates turn out to be similar, though the estimate using the modification of Remark 2 is slightly tighter and significantly less computationally expensive. Running Algorithm 1 with the full state dimension $n=6$ and order $k=4$ with the $\epsilon$ and $\delta$ above requires $N=2,009,600$ samples: using the reduced-state variant brings the effective state dimension to $n=2$, and the sample size to $N=32,292$. The computation times in the full-state case were 77 minutes on the laptop and 2 minutes on `c5.24xlarge`; in the reduced-state case, computation times were 78 seconds on the laptop and 2 seconds on `c5.24xlarge`. This shows that Algorithm 1’s ability to work on subsets of the state space can speed up computations in cases where only a subset of state variables are of interest.", {}),
    ("p0005-b006", "heading", ("p0005-b006",), "### C. Monotone Traffic Model", {}),
    ("p0005-b007", "text", ("p0005-b007",),
     r"The final example is a special case of a continuous-time road traffic analysis problem used as a reachability benchmark in [20], [21], [22]. This problem investigates the density of traffic on a single lane over a time range over four periods of duration $T$ using a discretization of the cell transmission model that divides the road into $n$ equal segments. The spatially discretized model is an $n$-dimensional dynamical system with states $x_1,\dots,x_n$, where $x_i$ represents the density of traffic in the $i^{th}$ segment. Traffic enters segment through $x_1$ and flows through each successive segment before leaving through segment $n$. The state dynamics are", {}),
    ("p0005-b008", "text", ("p0005-b008",),
     "$$\n" r"\begin{aligned}" "\n"
     r"\dot{x}_1 &= \frac{1}{T}\left(d-\min(c, vx_{1}, w(\overline{x}-x_{2}))\right)\\" "\n"
     r"\dot{x}_i &= \frac{1}{T}\big( \min(c, vx_{i-1}, w(\overline{x}-x_{i})) \\" "\n"
     r"&- \min(c, vx_{i}, w(\overline{x}-x_{i+1}))\big), \quad(i=2,\dots,n-1)\\" "\n"
     r"\dot{x}_{n} &= \frac{1}{T}\left(\min(c, vx_{n-1}, w(\overline{x}-x_{n})/\beta) - \min(c, vx_{n}))\right)," "\n"
     r"\end{aligned} \tag{3}" "\n$$", {}),
    ("p0005-b009", "text", ("p0005-b009",),
     r"where $v$ represents the free-flow speed of traffic, $c$ the maximum flow between neighboring segments, $\bar{x}$ the maximum occupancy of a segment, and $w$ the congestion wave speed. The input $u$ represents the influx of traffic into the first node. For the reachable set estimation problem, we use a model with $n=6$ states, and take $T=30$, $v=0.5$, $w=1/6$, and $\bar{x}=320$. The initial set is the interval such that $x_i(0)\in[100,200]$, $i=1,\dots,n$, the set of disturbances is the set of constant disturbances with values in the range range $d\in[40/T, 60/T]$, and $X_0$ and $D$ are the uniform random variables over these sets. The time range is $[t_0, t_1]=[0, 4T]$.", {}),
    ("p0005-b010", "text", ("p0005-b010",),
     r"The system dynamics (3) are *monotone*, or order-preserving, meaning that if two initial conditions $x^{(1)}(0)$, $x^{(2)}(0)$ and disturbances $d^{(1)}, d^{(2)}$ satisfy $x^{(1)}(0)\le x^{(2)}(0)$ (where $\le$ is the standard partial order) and $d^{(1)}(t) \le d^{(2)}(t),\ t\in[0,T]$, then $x^{(1)}(T)\le x^{(2)}(T)$. This monotonicity allows for a convenient interval over-approximation of the reachable set. If $\underline{x}$, $\overline{x}$ are the lower and upper bounds of the interval of initial states, and $\underline{d}$, $\overline{d}$ are the lower and", {}),
])

# ---------------------------------------------------------------- page 6
page(6, r"""
Compared with the 170 dpi render and a 300 dpi crop (interval formula at the top) of PDF page 6 and
with the TeX source and .bbl. First item continues the sentence from page 5 (join_previous 'space').
The interval $[\Phi(t_1;t_0,\underline{x},\underline{d}),\Phi(t_1;t_0,\overline{x},\overline{d})]$,
which the extractor had damaged (lost under/overlines), is rewritten from the TeX source and
checked on the crop. Figure 3 kept as an image crop (bbox checked on a wider 200 dpi render: tick
labels and the axis labels x_5, x_6 are inside; the caption and the paragraph above are outside);
caption verbatim with the printed prefix 'Fig. 3.'. The Conclusion paragraph that crosses the column
break ('... is conservative, and could | be significantly improved ...') was merged. Headings:
'V. CONCLUSION', 'ACKNOWLEDGMENTS' and 'REFERENCES' in title case as level-2 headings. Real compound
hyphens restored where the extractor dropped them at line ends: 'over-approximation',
'control-theoretic', 'infinite-dimensional', 'On-the-fly'; line-wrap hyphens repaired
('conservative', 'interval', 'proposed', 'demonstrate', 'methods', 'reachable', 'verification').
Authors' text kept as printed: 'because reachable set may only occupy', 'empirical Inverse
Christoffel function method' (capital I), and '$\phi(x)^\top\phi(x)=(1+x^\top x)^k$' without the
subscript $k$ on $\phi$. References [1]-[12]: one text item per entry, the bullet markers added by
the extractor removed, journal/booktitle italics kept; every entry was compared with the page image
and the .bbl ([5] 'Açikmeşe' restored from 'Ac¸ikmes¸e'; [7] and [8], merged by the extractor, are
separate items; [12] keeps the printed '——,' repeated-author dash). Numbers checked: k=10, 0.05,
10^{-9}, 10 minutes, 2 minutes, order 10, grant numbers N00014-18-1-2209, FA9550-18-1-0253,
ECCS-1906164, and volume/page/year fields of [1]-[12].
""", [
    ("p0006-b000", "text", ("p0006-b000",),
     r"upper bounds on the values admitted by the disturbance signal, then $[\Phi(t_1;t_0, \underline{x}, \underline{d}), \Phi(t_1;t_0, \overline{x}, \overline{d})]$ is the smallest interval that contains the entire reachable set. While this over-approximation is easy to compute, and the best possible over-approximation by an interval, it is in general a conservative over-approximation because reachable set may only occupy a small volume of the interval. Since the empirical Inverse Christoffel function method can accurately detect the geometry of the reachable set, we use this method to compare the shape of the reachable set to the best interval over-approximation. In particular, we use the reduced-state variant of Algorithm 1 to compute a reachable set for the traffic densities $x_5$ and $x_6$ at the end of the road, using an order $k=10$ empirical inverse Christoffel function with accuracy and confidence parameters $\epsilon=0.05$, $\delta=10^{-9}$. Computation times for this example were 10 minutes on the laptop and 2 minutes on `c5.24xlarge`.",
     {"join_previous": "space"}),
    ("p0006-b001", "figure", ("p0006-b001",), "", {"label": "Figure 3", "asset_name": "figure-3"}),
    ("p0006-b002", "caption", ("p0006-b002",),
     r"Fig. 3. Reachable set estimate for the monotone traffic model with an order 10 empirical inverse Christoffel function (blue), compared to the tight interval over-approximation (red). The reachable set estimate was computed with Algorithm 1 using samples projected onto states $x_5$ and $x_6$.", {}),
    ("p0006-b003", "text", ("p0006-b003",),
     "Figure 3 compares the reachable set estimate computed with Algorithm 1 to the projection of the tight interval over-approximation computed using the monotonicity property of the traffic system. The figure indicates that the tight interval over-approximation of the reachable set is a somewhat conservative over-approximation, since the reachable set has approximately the shape of a parallelotope whose sides are not axis-aligned.", {}),
    ("p0006-b004", "heading", ("p0006-b004",), "## V. Conclusion", {}),
    ("p0006-b005", "text", ("p0006-b005",),
     "Algorithm 1 demonstrates that Christoffel functions, in addition to being useful in data analysis, can also be used as tools to provide principled, data-driven solutions to control-theoretic problems. While Theorem 1 assures that the proposed algorithm is a sound approach to solving reachability problems with data, and the examples of Section IV demonstrate that the algorithm can provide accurate reachable set approximations, we believe it represents only the first step in applying Christoffel functions to data-driven reachability. For instance, the *a posteriori* analysis of Section IV-A suggests the sample bound of Theorem 1 is conservative, and could be significantly improved by applying some of the special properties of Christoffel functions.", {}),
    ("p0006-b007", "text", ("p0006-b007",),
     r"In addition, this paper did not explore how kernel methods can be used alongside Christoffel functions. Although we have defined the Christoffel function using the standard monomial basis vector $z_k(x)$, the Christoffel function is in fact invariant to changes in polynomial coordinates. For instance, $z_k(x)$ could be replaced with the feature vector $\phi_k(x)$ of the polynomial kernel $(1+x^\top x)^k$, that is the monomial vector $\phi_k(x)$ such that $\phi(x)^\top\phi(x)=(1+x^\top x)^k$. By an application of the kernel trick, this approach can be extended to kernels with infinite-dimensional feature spaces, as in [13]. However, the statistical learning-theoretic proof in this paper covers only the finite-dimensional case: providing finite-sample statistical guarantees for the infinite-dimensional case is a topic for future research.", {}),
    ("p0006-b008", "heading", ("p0006-b008",), "## Acknowledgments", {}),
    ("p0006-b009", "text", ("p0006-b009",),
     "This work was supported in part by the grants ONR N00014-18-1-2209, AFOSR FA9550-18-1-0253, NSF ECCS-1906164.", {}),
    ("p0006-b010", "heading", ("p0006-b010",), "## References", {}),
    ("p0006-b011", "text", ("p0006-b011",),
     "[1] A. Devonport and M. Arcak, “Data-driven reachable set computation using adaptive Gaussian process classification and Monte Carlo methods,” in *2020 American Control Conference (ACC)*. IEEE, 2020, pp. 2629–2634.", {}),
    ("p0006-b012", "text", ("p0006-b012",),
     "[2] G. R. Marseglia, J. Scott, L. Magni, R. D. Braatz, and D. M. Raimondo, “A hybrid stochastic-deterministic approach for active fault diagnosis using scenario optimization,” *IFAC Proceedings Volumes*, vol. 47, no. 3, pp. 1102–1107, 2014.", {}),
    ("p0006-b013", "text", ("p0006-b013",),
     "[3] Y. Yang, J. Zhang, K.-Q. Cai, and M. Prandini, “Multi-aircraft conflict detection and resolution based on probabilistic reach sets,” *IEEE Transactions on Control Systems Technology*, vol. 25, no. 1, pp. 309–316, 2016.", {}),
    ("p0006-b014", "text", ("p0006-b014",),
     "[4] D. Ioli, A. Falsone, H. Marianne, B. Axel, and M. Prandini, “A smart grid energy management problem for data-driven design with probabilistic reachability guarantees,” in *4th International Workshop on Applied Verification of Continuous and Hybrid Systems*, vol. 48, 2017, pp. 2–19.", {}),
    ("p0006-b015", "text", ("p0006-b015",),
     "[5] H. Sartipizadeh, A. P. Vinod, B. Açikmeşe, and M. Oishi, “Voronoi partition-based scenario reduction for fast sampling-based stochastic reachability computation of linear systems,” in *2019 American Control Conference (ACC)*. IEEE, 2019, pp. 37–44.", {}),
    ("p0006-b016", "text", ("p0006-b016",),
     "[6] L. Hewing and M. N. Zeilinger, “Scenario-based probabilistic reachable sets for recursively feasible stochastic model predictive control,” *IEEE Control Systems Letters*, vol. 4, no. 2, pp. 450–455, 2019.", {}),
    ("p0006-b017", "text", [317.0, 546.0, 559.0, 581.0],
     "[7] A. Devonport and M. Arcak, “Estimating reachable sets with scenario optimization,” ser. Proceedings of Machine Learning Research, A. M. Bayen, A. Jadbabaie, G. Pappas, P. A. Parrilo, B. Recht, C. Tomlin, and M. Zeilinger, Eds., vol. 120. PMLR, 10–11 Jun 2020, pp. 75–84.", {}),
    ("p0006-b017b", "text", [317.0, 582.0, 559.0, 617.0],
     "[8] C. Fan, B. Qi, S. Mitra, and M. Viswanathan, “DryVR: data-driven verification and compositional reasoning for automotive systems,” in *International Conference on Computer Aided Verification*. Springer, 2017, pp. 441–461.", {}),
    ("p0006-b018", "text", ("p0006-b018",),
     "[9] F. Djeumou, A. P. Vinod, E. Goubault, S. Putot, and U. Topcu, “On-the-fly control of unknown smooth systems from limited data,” *arXiv preprint arXiv:2009.12733*, 2020.", {}),
    ("p0006-b019", "text", ("p0006-b019",),
     "[10] B. Qi, C. Fan, M. Jiang, and S. Mitra, “DryVR 2.0: a tool for verification and controller synthesis of black-box cyber-physical systems,” in *Proceedings of the 21st International Conference on Hybrid Systems: Computation and Control (part of CPS Week)*, 2018, pp. 269–270.", {}),
    ("p0006-b020", "text", ("p0006-b020",),
     "[11] J. B. Lasserre and E. Pauwels, “The empirical Christoffel function in statistics and machine learning,” *arXiv preprint arXiv:1701.02886*, 2017.", {}),
    ("p0006-b021", "text", ("p0006-b021",),
     "[12] ——, “The empirical Christoffel function with applications in data analysis,” *Advances in Computational Mathematics*, vol. 45, no. 3, pp. 1439–1468, 2019.", {}),
])

# ---------------------------------------------------------------- page 7
page(7, r"""
Compared with the 170 dpi render of PDF page 7 and with the .bbl. The page contains only references
[13]-[22] in the left column; the rest of the page is blank. One text item per entry, the bullet
markers added by the extractor removed, italics kept. Every entry was compared with the page image
(authors, titles, venues, volume/number/pages, years). In [19] the URL is broken across two lines
after 'TechRpts/'; it is written without the line-break space as
http://www.eecs.berkeley.edu/Pubs/TechRpts/2012/EECS-2012-241.html. No word is hyphenated at
a line end on this page; 'Kernel-based', 'plug-in', 'under-approximation', 'On-board' and
'high-dimensional' are printed compound hyphens. There is no appendix in this version of the paper.
""", [
    ("p0007-b000", "text", ("p0007-b000",),
     "[13] A. Askari, F. Yang, and L. E. Ghaoui, “Kernel-based outlier detection using the inverse Christoffel function,” *arXiv preprint arXiv:1806.06775*, 2018.", {}),
    ("p0007-b001", "text", ("p0007-b001",),
     "[14] A. Cuevas and R. Fraiman, “A plug-in approach to support estimation,” *The Annals of Statistics*, vol. 25, no. 6, pp. 2300–2312, 1997.", {}),
    ("p0007-b002", "text", ("p0007-b002",),
     "[15] E. Pauwels, M. Putinar, and J.-B. Lasserre, “Data analysis from empirical moments and the Christoffel function,” *Foundations of Computational Mathematics*, pp. 1–31, 2020.", {}),
    ("p0007-b003", "text", ("p0007-b003",),
     "[16] R. M. Dudley, “Central limit theorems for empirical measures,” *The Annals of Probability*, pp. 899–929, 1978.", {}),
    ("p0007-b004", "text", ("p0007-b004",),
     "[17] T. Alamo, R. Tempo, and E. F. Camacho, “Randomized strategies for probabilistic solutions of uncertain feasibility and optimization problems,” *IEEE Transactions on Automatic Control*, vol. 54, no. 11, pp. 2545–2559, 2009.", {}),
    ("p0007-b005", "text", ("p0007-b005",),
     "[18] I. M. Mitchell, J. Budzis, and A. Bolyachevets, “Invariant, viability and discriminating kernel under-approximation via zonotope scaling,” in *Proceedings of the 22nd ACM International Conference on Hybrid Systems: Computation and Control*, 2019, pp. 268–269.", {}),
    ("p0007-b006", "text", ("p0007-b006",),
     "[19] P. Bouffard, “On-board model predictive control of a quadrotor helicopter: Design, implementation, and experiments,” 2012. [Online]. Available: http://www.eecs.berkeley.edu/Pubs/TechRpts/2012/EECS-2012-241.html", {}),
    ("p0007-b007", "text", ("p0007-b007",),
     "[20] S. Coogan and M. Arcak, “A benchmark problem in transportation networks,” *arXiv preprint arXiv:1803.00367*, 2018.", {}),
    ("p0007-b008", "text", ("p0007-b008",),
     "[21] P.-J. Meyer, A. Devonport, and M. Arcak, “Tira: toolbox for interval reachability analysis,” in *Proceedings of the 22nd ACM International Conference on Hybrid Systems: Computation and Control*. ACM, 2019, pp. 224–229.", {}),
    ("p0007-b009", "text", ("p0007-b009",),
     "[22] A. Devonport, M. Khaled, M. Arcak, and M. Zamani, “PIRK: scalable interval reachability analysis for high-dimensional nonlinear systems,” in *Computer Aided Verification*, S. K. Lahiri and C. Wang, Eds. Cham: Springer International Publishing, 2020, pp. 556–568.", {}),
])


def main():
    seen = set()
    for n, items in sorted(PAGES.items()):
        orig = json.loads((S / f"orig-pages/page-{n:04d}.json").read_text(encoding="utf-8"))
        boxes = {i["id"]: i["bbox"] for i in orig["items"]}
        out_items = []
        for iid, kind, spec, md, extra in items:
            assert iid not in seen, iid
            seen.add(iid)
            if isinstance(spec, tuple):
                bs = [boxes[k] for k in spec]
                bbox = [min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs)]
            else:
                bbox = spec
            assert bbox[0] < bbox[2] and bbox[1] < bbox[3] and bbox[0] >= 0 and bbox[1] >= 0 \
                and bbox[2] <= orig["width"] and bbox[3] <= orig["height"], (iid, bbox)
            if kind not in ("figure", "omit"):
                assert md.count("$") % 2 == 0, ("odd number of $", iid)
                assert md.count("{") == md.count("}"), ("brace imbalance", iid)
            item = {"id": iid, "kind": kind, "bbox": bbox, "markdown": md}
            item.update(extra)
            out_items.append(item)
        state = {k: orig[k] for k in ("page", "width", "height", "mode", "preview")}
        state["reviewed"] = True
        state["review_notes"] = NOTES[n]
        state["warnings"] = orig.get("warnings", [])
        state["items"] = out_items
        (D / f"pages/page-{n:04d}.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"page {n}: {len(out_items)} items written")


if __name__ == "__main__":
    main()
