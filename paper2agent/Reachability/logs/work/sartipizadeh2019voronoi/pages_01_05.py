# Pages 1-5 of sartipizadeh2019voronoi (executed by make_pages.py; page() and dd() come from there).

# ---------------------------------------------------------------- page 1
page(1, r"""
Compared with the 150 dpi render of PDF page 1 and with the authors' TeX source
(ACC_2019_Voronoi_arxiv.tex). The PDF is a single-column 11pt article, so reading order is top to
bottom. Vertical arXiv stamp in the left margin ('arXiv:1811.03643v1 [math.OC] 8 Nov 2018') set to
omit; no page number is printed on any page. Title kept as the single level-1 heading exactly as
printed ('... of LTI Systems'). Author line: the extractor's detached cedillas ('Beh¸cet A¸cıkme¸se')
were restored to 'Behçet Açıkmeşe' (also in the footnote); the footnote marker after 'Meeko Oishi' is
written $^{\ast}$. 'Abstract' is a printed centred bold heading, written '## Abstract' (extractor had
level 3 with bold markers). Section heading written '## 1 Introduction' with the printed number.
Abstract and both introduction paragraphs compared word by word with the TeX source and the page;
line-wrap hyphens of the PDF ('stochas-tic', 'pro-vides', 'appro-priately') do not occur because the
text is taken from the TeX source; 'reach-avoid', 'sampling-based', 'partition-based', 'trade-off',
'discrete-time', 'chance-constrained', 'transform-based', 'semi-definite', '40-dimensional',
'real-time' are printed compound hyphens. Authors' wording kept: 'we propose a Voronoi
partition-based to check' (no noun after 'partition-based'). Citation groups checked against the
page: [1–5], [1], [1, 6, 7], [8, 9], [8], [4, 9], [4], [10, 11], [5], [12], [10, 11]. The title
footnote (four printed lines: funding, and three affiliation/e-mail lines) is kept as one text item
starting 'Footnote $\ast$:'; the PDF prints it at the bottom of page 1, between the second and the
third paragraph of the Introduction, and it is placed here directly after the author line that
carries its marker so that it does not interrupt the Introduction; e-mail addresses are printed in typewriter
type and written as code spans; the last address is printed with a trailing period inside the
typewriter text ('behcet@uw.edu.').
""", [
    ("p0001-b000", "omit", ("p0001-b000",), "", {"reason": "Vertical arXiv stamp in the left margin ('arXiv:1811.03643v1 [math.OC] 8 Nov 2018'); page furniture, the version is recorded in the conversion notes."}),
    ("p0001-b001", "heading", ("p0001-b001",), "# Voronoi Partition-based Scenario Reduction for Fast Sampling-based Stochastic Reachability Computation of LTI Systems", {}),
    ("p0001-b002", "text", ("p0001-b002",), r"Hossein Sartipizadeh, Abraham P. Vinod, Behçet Açıkmeşe, and Meeko Oishi $^{\ast}$", {}),
    ("p0001-b008", "text", ("p0001-b008", "p0001-b009", "p0001-b010", "p0001-b011"),
     r"Footnote $\ast$: This material is based upon work supported by the National Science Foundation, the Air Force Office of Scientific Research, and the Office of Naval Research. Hossein Sartipizadeh and Behçet Açıkmeşe were supported by Air Force Research Laboratory grant FA8650-15-C-2546 and the Office of Naval Research (ONR) Grant No. N00014-15-IP-00052. Vinod and Oishi were supported under NSF Grant Number CMMI-1254990, NSF Grant No. IIS-1528047, and AFRL Grant No. FA9453-17-C-0087. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation."
     "\n\n"
     "H. Sartipizadeh (corresponding author) is with University of Texas at Austin, TX, US. Email: `hsartipi@utexas.edu`."
     "\n\n"
     "A. Vinod and M. Oishi are with the Electrical & Computer Engineering, University of New Mexico, Albuquerque, NM, US. Email: `aby.vinod@gmail.com; oishi@unm.edu`."
     "\n\n"
     "B. Açıkmeşe is with the Department of Aeronautics & Astronautics in the University of Washington, Seattle, WA. Email: `behcet@uw.edu.`", {}),
    ("p0001-b003", "heading", ("p0001-b003",), "## Abstract", {}),
    ("p0001-b004", "text", ("p0001-b004",),
     "In this paper, we address the stochastic reach-avoid problem for linear systems with additive stochastic uncertainty. We seek to compute the maximum probability that the states remain in a safe set over a finite time horizon and reach a target set at the final time. We employ sampling-based methods and provide a lower bound on the number of scenarios required to guarantee that our estimate provides an underapproximation. Due to the probabilistic nature of the sampling-based methods, our underapproximation guarantee is probabilistic, and the proposed lower bound can be used to satisfy a prescribed probabilistic confidence level. To decrease the computational complexity, we propose a Voronoi partition-based to check the reach-avoid constraints at representative partitions (cells), instead of the original scenarios. The state constraints arising from the safe and target sets are tightened appropriately so that the solution provides an underapproximation for the original sampling-based method. We propose a systematic approach for selecting these representative cells and provide the flexibility to trade-off the number of cells needed for accuracy with the computational cost.", {}),
    ("p0001-b005", "heading", ("p0001-b005",), "## 1 Introduction", {}),
    ("p0001-b006", "text", ("p0001-b006",),
     "Reach-avoid analysis is an established verification tool for discrete-time stochastic dynamical systems, which provides probabilistic guarantees on the safety and performance [1–5]. This paper focuses on the finite time horizon *terminal* hitting time stochastic reach-avoid problem [1] (referred to here as the *terminal time problem*), that is, computation of the maximum probability of hitting a target set at the terminal time, while avoiding an unsafe set during all the preceding time steps using a controller that satisfies the specified control bounds.", {}),
    ("p0001-b007", "text", ("p0001-b007",),
     "The solution to the terminal time problem relies on dynamic programming [1, 6, 7], hence a variety of approximation methods have been suggested in literature. Researchers have looked for scalable approaches to solve this problem using approximate dynamic programming [8, 9], Gaussian mixtures [8], particle filters [4, 9], convex chance-constrained optimization [4], Fourier transform-based verification [10, 11], Lagrangian approaches [5], and semi-definite programming [12]. Currently, the largest system verified is a 40-dimensional chain of double integrators [10, 11] using Fourier transform-based techniques. Existing methods impose a high computational complexity which makes them unrealistic for real-time applications.", {}),
])

# ---------------------------------------------------------------- page 2
page(2, r"""
Compared with the 150 dpi render of PDF page 2 and with the TeX source. The three remaining
introduction paragraphs are complete on this page (page 1 ends with a full paragraph, so no
cross-page join). Section references resolved to the printed numbers (Section 2, 3, 4, 5); citations
checked on the page: [4], [13], [14–17], [4, 13], [18, Rem. 1], [15] twice. Headings: '## 2 Problem
formulation', '### 2.1 System description' (extractor had level 1 and 2 with bold markers). All
inline mathematics rewritten in LaTeX from the TeX source with the authors' macros expanded
(\R -> \mathbb{R}, \N -> \mathbb{N}, \X -> \mathcal{X}, \U -> \mathcal{U}, \W -> \mathcal{W},
\Prob -> \mathbb{P}); the extractor had turned the paragraph after equation (2) into superscript
soup. The two extractor 'formula' images were replaced by $$ blocks with the printed numbers (1)
and (2). Checked on the render: $\mathbb{N}_{[a,b]}$, $x_t\in\mathcal{X}=\mathbb{R}^{n_x}$,
$w_t\in\mathcal{W}\subseteq\mathbb{R}^{n_x}$ (disturbance dimension $n_x$, as printed), the stacked
vectors $X$, $U$, $W$ with indices 1..N, 0..N-1, 0..N-1, and $\mathbb{P}_{X}^{x_0,U}$,
$\mathbb{P}_W$, $(\eta_{w})^N$. TeX and PDF agree. Authors' wording kept: 'a length $n$ vector of
real numbers' for $\mathbb{R}^n$, 'Vector with all elements 1 is denoted', '(i.i.d)' without the
final period, 'a $N$-length horizon', and the index $k$ in $w_k$, $x_k$ where the dynamics use $t$.
""", [
    ("p0002-b000", "text", ("p0002-b000",),
     "In this paper, we reconsider the sampling-based approach, proposed in [4]. Similar sampling-based approach has been used successfully in robotics [13] and in stochastic optimal control [14–17]. In the sampling-based stochastic reach-avoid problem, we sample the stochastic disturbance to produce a finite set of *scenarios*, and then formulate a mixed-integer linear program (MILP) to maximize the number of scenarios that satisfy the reach-avoid constraints [4, 13]. As expected, the approximated probability will converge to the true terminal time probability as the number of scenarios increases. However, the computational complexity of MILP increases exponentially with the number of binary decision variables (the number of scenarios) [18, Rem. 1] making the MILP formulation practically intractable.", {}),
    ("p0002-b001", "text", ("p0002-b001",),
     "The main contributions of this paper are two-fold. We first provide a lower bound on the number of scenarios needed to probabilistically guarantee a user-specified upper bound on the approximation error with a user-specified confidence level using concentration techniques. Using Hoeffding’s inequality, we demonstrate that the number of scenarios that need to be considered is inversely proportional to the square of the desired upper bound on the estimate error. Next, we propose a Voronoi-based undersampling technique that underapproximates the MILP-based solution in a computationally efficient manner. This approach allows us to partially mitigate the exponential computational complexity, and provides flexibility to select the number of partitions based on the allowable online computational complexity. We demonstrate the application of the proposed method in a problem of spacecraft rendezvous and docking.", {}),
    ("p0002-b002", "text", ("p0002-b002",),
     "The organization of the paper is as follows: Problem formulation and preliminary definitions are stated in Section 2. Lower bound on the required number of scenarios for the prescribed confidence level is given in Section 3. Section 4 presents the proposed partition-based method and the approximate solution reconstruction. The performance of the proposed method is investigated on a spacecraft rendezvous maneuvering and docking in Section 5.", {}),
    ("p0002-b003", "heading", ("p0002-b003",), "## 2 Problem formulation", {}),
    ("p0002-b004", "text", ("p0002-b004",),
     r"We presume $\mathbb{R}$ and $\mathbb{N}$ are sets of real and natural numbers, with $\mathbb{R}^{n}$ a length $n$ vector of real numbers, and $\mathbb{N}_{[a,b]}$ the set of natural numbers between $a$ and $b$. For $x\in\mathbb{R}^{n}$, $x^{\top}$ denotes the transpose of $x$. Vector with all elements 1 is denoted $\mathbf{1}$.", {}),
    ("p0002-b005", "heading", ("p0002-b005",), "### 2.1 System description", {}),
    ("p0002-b006", "text", ("p0002-b006",), "Consider a discrete-time stochastic LTI system,", {}),
    ("p0002-b007", "text", ("p0002-b007",), dd(r"x_{t+1}=Ax_t+Bu_t+w_t", "1"), {}),
    ("p0002-b008", "text", ("p0002-b008",),
     r"with state $x_t\in \mathcal{X}=\mathbb{R}^{n_x}$, input $u_{t}\in \mathcal{U}\subseteq\mathbb{R}^{n_u}$, disturbance $w_t\in \mathcal{W}\subseteq\mathbb{R}^{n_x}$ at time instant $t$, and matrices $A,B$ assumed to be of appropriate dimensions. We assume that $w_k$ is an independent and identically distributed (i.i.d) random variable with a PDF $\eta_{w}$. Note that we require $\eta_{w}$ only to be a probability density function from which we can draw samples, and do not require it to be Gaussian. The system (1) over a time horizon with length $N$ can be alternatively written in a “stacked” form,", {}),
    ("p0002-b009", "text", ("p0002-b009",), dd(r"X(x_{0},U,W)=G_{x}x_0+G_{u}U+G_{w}W,", "2"), {}),
    ("p0002-b010", "text", ("p0002-b010",),
     r"with $X=[x_{1}^{\top},\cdots,x_{N}^{\top}]^\top \in \mathcal{X}^N$, $U=[u_{0}^{\top},\cdots,u_{N-1}^{\top}]^\top\in \mathcal{U}^N$, and $W=[w_{0}^{\top},\cdots,w_{N-1}^{\top}]^\top\in \mathcal{W}^N$ the concatenated state, input, and disturbance vectors over a $N$-length horizon [15]. The matrices $G_{x}$, $G_{u}$, and $G_{w}$ may be obtained from the system matrices in (1) (see [15]). Due to the stochastic nature of $w_k$, the state $x_k$ and the concatenated state vector $X$ are random. We define $\mathbb{P}_{X}^{x_0,U}$ as the probability measure associated with the random vector $X$, which is induced from the probability measure of the concatenated disturbance vector $\mathbb{P}_W$ and (2). By the i.i.d. assumption on $w_k$, $\mathbb{P}_W$ is characterized by $(\eta_{w})^N$.", {}),
])

# ---------------------------------------------------------------- page 3
page(3, r"""
Compared with the 150 dpi render and two 230 dpi crops of PDF page 3 and with the TeX source.
Heading '### 2.2 Stochastic reach-avoid problem'. All mathematics rewritten in LaTeX from the TeX
source and checked symbol by symbol on the crops; macros expanded (\Costpi ->
r_{x_0}^{U}(\mathcal{S},\mathcal{T}), \mcS/\mcT/\mcR -> \mathcal{S}/\mathcal{T}/\mathcal{R},
\Exp -> \mathbb{E}); the superscript asterisk is written \ast everywhere (same printed glyph; a
bare * could be read as Markdown emphasis). The eight extractor 'formula' images were replaced by
$$ blocks: (3); (4) and (5) inside Problem 1 (the authors' optidef 'maxi' environments print
'p*(x0) = max' with 'U in U^N' set below 'max'; written \max_{U\in\mathcal{U}^{N}}); (6a), (6b),
(6c) as three $$ blocks in one item so that each keeps its printed number; (7); and the unnumbered MILP of
Problem 2 as an aligned block with the printed 's.t.'. Problem 1, Remark 1 and Problem 2 start with
the printed bold label; their bodies are printed in italics and are written upright. Problem 1 ends
after '... induced from $\mathbb{P}_X^{x_0,U}$.' and Problem 2 after '... based on the probability
law $\mathbb{P}_W$.' (end of the italic text in the PDF = end of the TeX environment). Citations
checked on the page: [1] twice, [4, 10, 11], [1, Sec. 4], [4, 13], [19, Ex. 2.25], [4, 13, 18].
Kept as printed (source slips, not conversion errors): in (3) the event uses
$\forall t\in\mathbb{N}_{[0,N-1]}$ while $z$ uses $\prod_{t=1}^{N-1}$; in (6c)
$\mathcal{R}=\{x|FX\leq h\}$ with lower-case $x$ before the bar; '$F\in\mathbb{R}^{L\times n_x}$';
the text after (3) starts with lower-case 'with' after the period of (3); “big-M” with typographic
quotes (TeX source has a straight closing quote).
""", [
    ("p0003-b000", "heading", ("p0003-b000",), "### 2.2 Stochastic reach-avoid problem", {}),
    ("p0003-b001", "text", ("p0003-b001",),
     r"We are interested in the terminal time problem [1]. As in [1], we seek open-loop control laws, to assure tractability (at the cost of conservativeness [4, 10, 11]). We define the *terminal time probability*, $r_{x_0}^{U}(\mathcal{S}, \mathcal{T})$, for a given initial state $x_0\in \mathcal{X}$ and an open-loop control $U\in \mathcal{U}^N$, as the probability that the state trajectory remains inside the safety set $\mathcal{S} \subseteq \mathcal{X}$ and reaches the target set $\mathcal{T} \subseteq \mathcal{X}$ at time $N$,", {}),
    ("p0003-b002", "text", ("p0003-b002",),
     dd(r"r_{x_0}^{U}(\mathcal{S}, \mathcal{T}) = \mathbb{P}_{X}^{x_0,U}\left\{x_{N}\in \mathcal{T} \wedge x_t\in \mathcal{S},\forall t\in \mathbb{N}_{[0,N-1]}\right\}= \mathbb{P}_{X}^{x_0,U}\left\{ X\in \mathcal{R}\right\} 1_{\mathcal{S}}( x_0).", "3"), {}),
    ("p0003-b003", "text", ("p0003-b003",),
     r"with $\mathcal{R} = \mathcal{S}^{N-1}\times \mathcal{T}$. The stochastic reach-avoid problem is formulated as:", {}),
    ("p0003-b004", "text", ("p0003-b004",), "**Problem 1.** Open-loop terminal time problem:", {}),
    ("p0003-b005", "text", ("p0003-b005",),
     dd(r"p^{\ast}( x_{0}) = \max_{U\in \mathcal{U}^{N}} \quad r_{x_0}^{U}(\mathcal{S}, \mathcal{T})", "4"), {}),
    ("p0003-b006", "text", ("p0003-b006",), "Problem 1 is equivalent to (see [1, Sec. 4]),", {}),
    ("p0003-b007", "text", ("p0003-b007",),
     dd(r"p^{\ast}( x_{0}) = \max_{U\in \mathcal{U}^{N}} \quad 1_{\mathcal{S}}( x_0)\mathbb{E}_z^{x_0,U}\left[ z \right],", "5"), {}),
    ("p0003-b008", "text", ("p0003-b008",),
     r"where $z=1_{\mathcal{T}}(x_N)\prod_{t=1}^{N-1}1_{\mathcal{S}}(x_t) = 1_{\mathcal{R}}(X)$ is a Bernoulli random variable with a discrete probability measure $\mathbb{P}_z^{x_0,U}$ induced from $\mathbb{P}_X^{x_0,U}$.", {}),
    ("p0003-b009", "text", ("p0003-b009",),
     r"**Remark 1.** In Problem 1, $p^\ast(x_0)$ is trivially zero when $x_0\not\in\mathcal{S}$, irrespective of the choice of the controller.", {}),
    ("p0003-b010", "text", ("p0003-b010",),
     r"In [4, 13], a mixed-integer linear program (MILP) was formulated as an approximation of Problem 1 when the safe and the target sets are *polytopic*. Note that restriction of the safe and the target sets to polytopes is not severe since convex and compact sets admit tight polytopic underapproximations [19, Ex. 2.25]. We will denote the safe set $\mathcal{S}$, the target set $\mathcal{T}$, and the reach-avoid constraint set $\mathcal{R}$ as", {}),
    ("p0003-b011", "text", ("p0003-b011", "p0003-b012", "p0003-b013"),
     dd(r"\mathcal{S}=\{x|f_{\mathcal{S}}x\leq h_{\mathcal{S}}\},", "6a") + "\n\n"
     + dd(r"\mathcal{T}=\{x|f_{\mathcal{T}}x\leq h_{\mathcal{T}}\},", "6b") + "\n\n"
     + dd(r"\mathcal{R}=\{x|FX\leq h\}", "6c"), {}),
    ("p0003-b014", "text", ("p0003-b014",),
     r"with $l_\mathcal{S},l_\mathcal{T}\in \mathbb{N}, L=(N-1)l_\mathcal{S}+l_\mathcal{T}, f_\mathcal{S}\in \mathbb{R}^{l_\mathcal{S}\times n_x}$, $f_\mathcal{T}\in \mathbb{R}^{l_\mathcal{T}\times n_x}$, and $F\in \mathbb{R}^{L\times n_x}$ is constructed using $f_{\mathcal{S}}$ and $f_{\mathcal{T}}$. Using the “big-M” approach [4, 13, 18], and a sampling-based empirical mean for $r_{x_0}^{U}(\mathcal{S}, \mathcal{T})$ that replaces $\mathcal{W}^{N}$ by a finite set of $K$ random samples,", {}),
    ("p0003-b015", "text", ("p0003-b015",), dd(r"\mathcal{W}_{K}=\{W^{(1)},\cdots,W^{(K)}\},", "7"), {}),
    ("p0003-b016", "text", ("p0003-b016",), "we obtain a MILP approximation to Problem 1.", {}),
    ("p0003-b017", "text", ("p0003-b017",), "**Problem 2.** A MILP approximation to Problem 1 is given by", {}),
    ("p0003-b018", "text", ("p0003-b018",),
     dd(r"""\begin{aligned}
\max_{U\in\mathcal{U}^{N}} \quad & \frac{1}{K}\sum_{i=1}^{K}z^{(i)} \\
\text{s.t.} \quad & X^{(i)} = G_{x}x_{0} + G_{u} U + G_{w}W^{(i)}, \quad i\in \mathbb{N}_{[1,K]}, \\
& FX^{(i)} \leq h + M(1-z^{(i)})\mathbf{1}, \quad i\in \mathbb{N}_{[1,K]}, \\
& z^{(i)} \in\{0,1\}, \quad i\in \mathbb{N}_{[1,K]}
\end{aligned}"""), {}),
    ("p0003-b019", "text", ("p0003-b019",),
     r"with the optimal value denoted by $p_{K}^{\ast}(x_0)$, optimal control input $U^{\ast}_{K}$, $M \in \mathbb{R}$ some large positive number, and $W^{(i)}$ that are concatenated disturbance realizations sampled from $\mathcal{W}^N$, based on the probability law $\mathbb{P}_W$.", {}),
])

# ---------------------------------------------------------------- page 4
page(4, r"""
Compared with the 150 dpi render and a 230 dpi crop of the lower part of PDF page 4 and with the TeX
source. Figure 1 is a float at the top of the page, between the end of Problem 2 (page 3) and the
paragraph 'As observed in ...' that refers to it; it is kept at that position. Figure crop bbox set
from the ink extent of the 150 dpi render (dots from y=64.5 to the lowest red cross at y=226.8,
x 221.9-388.5) with a margin; the only in-figure label is the calligraphic R near the lower right
corner, and the extractor's picture text ('R') is not kept as text. Caption verbatim with LaTeX math
('2D' written plainly; $2$D in the source). Heading '### 2.3 Problem statements'. The
extractor 'formula' image of the limit was replaced by a $$ block with the printed number (8).
Question 1 and Question 2 start with the printed bold label; bodies printed in italics, written
upright. Mathematics from the TeX source, checked on the crop: $Z={[z^{(1)}\ \ldots\ z^{(K)}]}^\top$,
$\mathbb{P}_{Z}^{x_0,U}=\prod_{i=1}^K\mathbb{P}_z^{x_0,U}$, and in Question 1 the two events
$\{p_{K}^\ast(x_0)-p^{\ast}(x_0)\geq\delta\}$ with bound $\leq\beta$ and
$\{p^{\ast}(x_0)\geq p_{K}^\ast(x_0)-\delta\}$ with bound $\geq 1-\beta$, both under
$\mathbb{P}_{Z}^{x_0,U^\ast_K}$. Citations checked: [4, 13, 18], [4], [18, Rem. 1]. Kept as printed
(source wording): 'that violates the reach-avoid constraint $X^{(j)}\in\mathcal{R}$', 'an i.i.d
process', 'as claimed in next section', the space before the period in '$z^{(j)}=0$ .'.
""", [
    ("p0004-b000", "figure", [215.0, 58.0, 396.0, 233.0], "", {"label": "Figure 1", "asset_name": "figure-1"}),
    ("p0004-b001", "caption", ("p0004-b001",),
     r"Figure 1: Sampling-based approach illustration for reach-avoid problem in 2D. Reach-avoid set $\mathcal{R}$ is distinguished with lines. Black dots and red crosses represent the sampled state trajectories corresponding to sampled disturbance $\mathcal{W}_{K}$ for a given $U$ and $x_0$ that succeed and fail to remain in $\mathcal{R}$, respectively. Empirical mean of remaining in reach-avoid set is obtained by dividing the number of samples inside $\mathcal{R}$ to the total number of samples.", {}),
    ("p0004-b002", "text", ("p0004-b002",),
     r"As observed in [4, 13, 18], $z^{(i)}$ takes the value 1 if and only if $FX^{(i)}\leq h$ for all $i\in \mathbb{N}_{[1,K]}$. For any sampled trajectory that violates the reach-avoid constraint $X^{(j)}\in \mathcal{R},\ j\in \mathbb{N}_{[1,K]}$, we have $FX^{(j)}> h$ which is encoded by $z^{(j)}=0$ . This concept is illustrated in Figure 1; red crosses indicate the sampled trajectories which fail to remain in $\mathcal{R}$ and, therefore, their corresponding binary variables are zero. From [4], we have,", {}),
    ("p0004-b003", "text", ("p0004-b003",), dd(r"\lim_{K \rightarrow \infty}p_{K}^{\ast}(x_0) = p^{\ast}(x_0).", "8"), {}),
    ("p0004-b004", "text", ("p0004-b004",),
     r"However, Problem 2 becomes computationally intractable for large values of $K$ since the worst-case time complexity of MILP problems exponentially increases in the number of binary decision variables [18, Rem. 1].", {}),
    ("p0004-b005", "heading", ("p0004-b005",), "### 2.3 Problem statements", {}),
    ("p0004-b006", "text", ("p0004-b006",),
     r"Based on Problem 2, we define the random vector $Z={[z^{(1)}\ \ldots\ z^{(K)}]}^\top$, the concatenation of an i.i.d process consisting of Bernoulli random variables $\{z^{(i)}\}_{i=1}^K$. By definition, the probability measure associated with $Z$ is $\mathbb{P}_{Z}^{x_0, U}=\prod_{i=1}^K\mathbb{P}_z^{x_0,U}$.", {}),
    ("p0004-b007", "text", ("p0004-b007",), "We will address the following questions:", {}),
    ("p0004-b008", "text", ("p0004-b008",),
     r"**Question 1.** Given a violation parameter $\delta\in[0,1]$ and a risk of failure $\beta\in[0,1]$, characterize the sufficient number of scenarios $K$ to guarantee $\mathbb{P}_{Z}^{x_0, U^\ast_K}\{ p_{K}^\ast(x_0) - p^{\ast}(x_0) \geq \delta\}\leq \beta$ or equivalently $\mathbb{P}_{Z}^{x_0, U^\ast_K}\{ p^{\ast}(x_0) \geq p_{K}^\ast(x_0)-\delta \}\geq 1-\beta$, for all $x_0\in \mathcal{S}$.", {}),
    ("p0004-b009", "text", ("p0004-b009",),
     r"**Question 2.** Given $K$ scenarios as characterized in Question 1 to meet desired specifications, construct an under-approximate MILP with $\hat{K}<K$ scenarios (hence binary decision variables) that results in the terminal time probability estimate $\hat{p}(x_0)$ with $\hat{p}(x_0)\leq p_{K}^{\ast}(x_0)$.", {}),
    ("p0004-b010", "text", ("p0004-b010",),
     r"We will address Question 1 using Hoeffding’s inequality. By solving Question 1, we seek sufficient number of scenarios that leads to a desired upper bound on the likelihood that the approximate solution exceeds the true solution by some threshold ($\delta$). Note that a smaller $\delta$ implies less conservatism as well as higher accuracy in estimation, but requires more scenarios for a fixed $\beta$, as claimed in next section. Then we address Question 2 using Voronoi partitions to reduce the number of scenarios while preserving the original specifications $\delta$ and $\beta$.", {}),
])

# ---------------------------------------------------------------- page 5
page(5, r"""
Compared with the 150 dpi render and two 230 dpi crops of PDF page 5 and with the TeX source.
Headings '### 2.4 Voronoi partition and data clustering' and '## 3 Scenarios required to meet given
failure tolerance' (extractor had the wrong levels and bold markers). All mathematics rewritten in
LaTeX from the TeX source (macros \mcC, \mcP, \mcV, \X, \R, \N, \Prob expanded) and checked on the
crops; TeX and PDF agree. The extractor 'formula' images were replaced by $$ blocks with the printed
numbers (9), (10), (11); in (9) the authors' '~~\text{and}~~' spacing is written with '\ \ ' (a
double tilde would be Markdown strikethrough); in (11) 'arg min' is printed with a space and the
constraint set below it (\underset{...}{\operatorname{arg\ min}} as in the source). The extractor
had also made a 'formula' image of item 2 of Lemma 1; Lemma 1 is now one text item: bold label,
statement, and the two printed numbered items as a Markdown list (lemma body printed in italics,
written upright; the lemma ends after item 2, as in the TeX environment). The proof starts with the
printed italic run-in 'Proof:' (written in bold) and ends with the printed filled square, written
$\blacksquare$. Citations checked: [20], [21], [22], [23, Thm. 1]. Kept as printed (source slips, not
conversion errors): in (9) the quantifier '$\forall j,\ell\in\mathbb{N}_{[1,\hat{K}]}$ and
$j\neq\ell$' although $j$ is the cell index; (10) ends with a period and the sentence continues with
'where'; '$\mathcal{P}\in\mathcal{X}^K$ with $K$ points in $\mathbb{R}^d$'; 'a local minima';
'straight forward'; $n$ is the iteration count in $\mathcal{O}(ndK\hat{K})$; '(as given in (10) and
(9))' in that order; 'We have the following inequalities from Hoeffding' (plural) before a single
inequality.
""", [
    ("p0005-b000", "heading", ("p0005-b000",), "### 2.4 Voronoi partition and data clustering", {}),
    ("p0005-b001", "text", ("p0005-b001",),
     r"Here we introduce some preliminaries on Voronoi partition that we will use in the rest of this paper. Given a set of seeds (centres) $\mathcal{C}=\left\{c^{(1)},\cdots,c^{(\hat{K})}\right\}$, $c^{(i)}\in\mathbb{R}^{d}$, a Voronoi partition $\mathcal{V}(\mathcal{C})$ partitions the $\mathbb{R}^d$ space to $\hat{K}$ cells $V^{(1)},\cdots,V^{(\hat{K})}$ such that any point in $V^{(j)}$, $\forall j\in\mathbb{N}_{[1,\hat{K}]}$, is closer to $c^{(j)}$ than the other seeds. Given a set of points $\mathcal{P}=\left\{p^{(1)},\cdots,p^{(K)}\right\}$ in $\mathbb{R}^d$, we use $\mathcal{V}_{\mathcal{P}}(\mathcal{C})$ to show the partition of $\mathcal{P}$ through a Voronoi partition with seeds $\mathcal{C}$. We define each cell (may also be referred to as partition in this paper) of $\mathcal{V}_{\mathcal{P}}(\mathcal{C})$ as", {}),
    ("p0005-b002", "text", ("p0005-b002",),
     dd(r"V^{(j)}_{\mathcal{P}}(\mathcal{C})=\{p\in \mathcal{P}|d(p,c^{(j)})\leq d(p,c^{(\ell)}), \forall j,\ell\in\mathbb{N}_{[1,\hat{K}]} \ \ \text{and}\ \ j\neq\ell \},", "9"), {}),
    ("p0005-b003", "text", ("p0005-b003",),
     r"where $d(p^{(1)},p^{(2)})$ is the distance of $p^{(1)}\in \mathbb{R}^d$ from $p^{(2)}\in \mathbb{R}^d$ in any valid metric (Euclidean norm is used in this paper). We denote the number of elements in $V^{(j)}$ by $\vert V^{(j)} \vert$.", {}),
    ("p0005-b004", "text", ("p0005-b004",),
     r"A given set $\mathcal{P}\in \mathcal{X}^K$ with $K$ points in $\mathbb{R}^d$ can be clustered in $\hat{K}$ clusters by finding a set of seeds $\mathcal{C}\in \mathcal{X}^{\hat{K}}$ that minimizes the *within-cluster sum of squares*, as proposed by $k$-means method/Lloyd’s algorithm [20]. The within-cluster sum of squares, denoted by $\mathrm{WSS}(\hat{K},\mathcal{V}_{\mathcal{P}}(\mathcal{C}))$, simply represents the total sum of squared deviations of points in cells from their seeds, i.e., given a set of points $\mathcal{P}$, a set of seeds $\mathcal{C}$, and a partition set $\mathcal{V}_{\mathcal{P}}(\mathcal{C})=\{V^{(1)},\cdots,V^{(\hat{K})}\}$,", {}),
    ("p0005-b005", "text", ("p0005-b005",),
     dd(r"\mathrm{WSS}(\hat{K},\mathcal{V}_{\mathcal{P}}(\mathcal{C}))=\sum_{j=1}^{\hat{K}}\sum_{i=1}^{K} 1_{V^{(j)}}(p^{(i)})\|p^{(i)}-c^{(j)}\|^2.", "10"), {}),
    ("p0005-b005b", "text", [56.0, 353.0, 556.0, 366.0],
     r"where $1_{V^{(j)}}(p^{(i)})$ is an indicator function which is one if $p^{(i)}$ belongs to cell $V^{(j)}$, and zero otherwise. Let", {}),
    ("p0005-b006", "text", [56.0, 368.0, 556.0, 402.0],
     dd(r"\mathcal{C}^\ast=\underset{\mathcal{C}\in \mathcal{X}^{\hat{K}}}{\operatorname{arg\ min}}\ \mathrm{WSS}(\hat{K},\mathcal{V}_{\mathcal{P}}(\mathcal{C})),", "11"), {}),
    ("p0005-b007", "text", ("p0005-b007",),
     r"be the set of optimal seeds. Given $\mathcal{C}^\ast$, cells of $\mathcal{V}_{\mathcal{P}}(\mathcal{C}^\ast)$ represent the optimal $\hat{K}$ clusters of $\mathcal{P}$. Although solving (11) is an NP-hard problem [21], efficient algorithms exist to compute a local minima. Starting from an initial guess of $\mathcal{C}$, a successive algorithm with time complexity $\mathcal{O}(ndK\hat{K})$ for $n$ iterations can be used to update each seed by replacing it with the centroid of its cluster elements [22]. This process continues until convergence or $n$ reaches its maximum value. Note that the set of optimal seeds $\mathcal{C}^\ast$ is not necessarily a subset of $\mathcal{P}$. In addition, $\mathrm{WSS}(\hat{K},\mathcal{V}_{\mathcal{P}}(\mathcal{C}))$ is non-increasing in $\hat{K}$, and the number of required clusters can be decided by making a trade-off between $\mathrm{WSS}(\hat{K},\mathcal{V}_{\mathcal{P}}(\mathcal{C}))$ (representing accuracy) and $\hat{K}$ (representing computational complexity).", {}),
    ("p0005-b008", "text", ("p0005-b008", "p0005-b009", "p0005-b010"),
     "**Lemma 1.** Seed selection and Voronoi configuration are preserved under translation.\n\n"
     r"1. Let $\mathcal{C}^\ast=\{c^{(1)},\cdots,c^{(\hat{K})}\}$ be the set of $\hat{K}$ optimal seeds of $\mathcal{P}=\{p^{(1)},\cdots,p^{(K)}\}$, calculated as in (11). For any fixed vector $a$, $\mathcal{C}^{\ast}_{a}=\{a+c^{(1)},\cdots,a+c^{(\hat{K})}\}$ represents the optimal seeds of $\mathcal{P}_{a}=\{a+p^{(1)},\cdots,a+p^{(K)}\}$." "\n"
     r"2. For any $p^{(i)}\in\mathcal{P}$, let $p^{(i)}\in V^{(j)}_{\mathcal{P}}(\mathcal{C}^{\ast})$. Then $a+p^{(i)}\in V^{(j)}_{\mathcal{P}_a}(\mathcal{C}_a^{\ast})$.", {}),
    ("p0005-b011", "text", ("p0005-b011",),
     r"**Proof:** The proof is straight forward since both $\mathrm{WSS}$ and Voronoi partitions (as given in (10) and (9)) are functions of the relative distance of the points in each cell to their seed. $\blacksquare$", {}),
    ("p0005-b012", "heading", ("p0005-b012",), "## 3 Scenarios required to meet given failure tolerance", {}),
    ("p0005-b013", "text", ("p0005-b013",),
     r"Given i.i.d. $y^{(1)}, y^{(2)},\ldots,y^{(K)}$ for $K>0$ and $y^{(i)}\in[0,1],\ \forall i\in \mathbb{N}_{[1,K]}$ with probability measure $\mathbb{P}_y$, we define the concatenation of these random variables $Y=[y^{(1)}\ y^{(2)}\ \ldots\ y^{(K)}]^\top\in {[0,1]}^K$. The probability measure associated with $Y$ is $\mathbb{P}_Y^K=\prod_{i=1}^K \mathbb{P}_y$. We have the following inequalities from Hoeffding [23, Thm. 1].", {}),
])
