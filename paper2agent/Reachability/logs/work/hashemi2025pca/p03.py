from pagelib import *
o = orig(3)
B = lambda k: o[k]["bbox"]

items = [
    text("p0003-b000", B("p0003-b000"),
         "the dataset to perform statistical reachability analysis. Similarly, the work presented in Fan et al. (2017) uses the dataset to learn an exponential discrepancy function that estimates trajectory’s sensitivity to uncertainty, enabling the computation of probabilistic reachable sets. Of our particular interest is the method proposed by Hashemi et al. (2024b), which suggests learning a system model on this dataset via ReLU neural networks and then conduct statistical reachability analysis via conformal inference. By leveraging the ability of neural networks to model complex, high-dimensional relationships alongside the data efficiency of conformal inference, this approach establishes an efficient and structured framework for statistical reachability analysis. Additionally, the probabilistic guarantees proposed by Hashemi et al. (2024b) remain valid even when there is a distribution shift between the training and deployment environments. This is the main reason we focus on extending this work instead of building on other existing methodologies.",
         join_previous="space"),
    text("p0003-b001", B("p0003-b001"),
         r"""Conformal inference (CI) is a data-efficient method for formally providing guarantees on the $\delta$-quantile of distributions. This method involves sampling an i.i.d. scalar dataset, sorting the samples in ascending order, and demonstrating that one of the sorted samples represents the $\delta$-quantile. The integration of CI with formal verification techniques has recently received noticeable interest, that is primarily due to its accuracy and level of scalability. For instance, Bortolussi et al. (2019) merges CI with neural state classifiers to develop a stochastic runtime verification algorithm. Lindemann et al. (2023); Zecchin et al. (2024) employ CI to guarantee safety in MPC control using a trained model. Tonkens et al. (2023) applies CI for planning with probabilistic safety guarantees, and Hashemi et al. (2024b) integrates CI with existing neural network reachability techniques and provides a scalable reachability analysis on stochastic systems, see Lindemann et al. (2024) for a recent survey article."""),
    text("p0003-b002", B("p0003-b002"),
         r"""**Notation**. We use bold letters to represent vectors and vector-valued functions, while caligraphic letters denote sets and distributions. The set $\{1,2,\ldots, n\}$ is denoted as $[n]$. The Minkowski sum is indicated by $\oplus$. We use $x \sim \mathcal{X}$ to denote that the random variable $x$ is drawn from the distribution $\mathcal{X}$. We present the structure of a feedforward neural network (FFNN) with $\ell$ hidden layers as an array $[n_0,n_1,\ldots n_{\ell+1}]$, where $n_0$ denotes the number of inputs, $n_{\ell+1}$ is the number of outputs, and $n_i , i\in [\ell]$ denotes the width of the $i$-th hidden layer. We denote $e_i\in\mathbb{R}^n$ as the $i$-th base vector of $\mathbb{R}^n$. We also denote $\lceil x \rceil$ as the smallest integer greater than $x \in \mathbb{R}$."""),
    heading("p0003-b003", B("p0003-b003"), "## 2 Preliminaries"),
    heading("p0003-b004", B("p0003-b004"), "### 2.1 Stochastic Dynamical Systems"),
    text("p0003-b005", B("p0003-b005"),
         r"""Consider a set of random vectors $S_0, \ldots, S_\mathrm{K} \in \mathcal{S}$ indexed at times $0, \ldots, \mathrm{K}$ and with state space $\mathcal{S}\subseteq\mathbb{R}^n$. A realization of this stochastic process is a sequence of values $s_1, \ldots, s_\mathrm{K}$, denoted as system trajectory $\sigma^{\mathsf{real}}_{s_0}$. The joint distribution over $S_1, \ldots, S_\mathrm{K}$ is the trajectory distribution $\mathcal{D}_{S,\mathrm{K}}^{\mathsf{real}}$, while the marginal distribution of $S_0$ is known as the initial state distribution $\mathcal{W}$. It is assumed that $\mathcal{W}$ has support over a compact set of initial states $\mathcal{I}$, implying $\Pr[s_0 \notin \mathcal{I}] = 0$."""),
    text("p0003-b006", B("p0003-b006"),
         "**Training and Deployment Environments**. In the training environment, we pre-record or simulate datasets to conduct reachability analysis. Conversely, the deployment environment refers to the real world where we apply our reachable sets. There is typically a difference between the distribution of trajectories in the training and deployment environments. We"),
    omit("p0003-b007", B("p0003-b007"), "3",
         "Printed page number 3 centred at the foot of the page; page furniture, checked on the 170 dpi render."),
]

save(3, items, r"""
Compared with the 170 dpi render, a 260 dpi crop of the Notation paragraph and Section 2.1, and the TeX source (sections/intro.tex,
sections/prelim.tex). First item continues the 'Related Work' paragraph from page 2 (join_previous 'space'); Footnote 2 of page 2 is
placed after this item by plan.json 'reading_order'. All inline math rewritten in LaTeX from the TeX source with the authors' macros
expanded (\Statee -> S, \statee -> s, \horizon -> \mathrm{K} (upright K as printed), \states -> \mathcal{S}, \trajreal ->
\sigma^{\mathsf{real}}, \dist -> \mathcal{D}_{S,\mathrm{K}}^{\mathsf{real}}, \distinit -> \mathcal{W}, \init -> \mathcal{I}) and checked
on the crop: $\{1,2,\ldots,n\}$, $[n]$, $\oplus$, $x\sim\mathcal{X}$, $[n_0,n_1,\ldots n_{\ell+1}]$ (no comma after the dots, as
printed), $e_i\in\mathbb{R}^n$, $\lceil x\rceil$, $S_0,\ldots,S_\mathrm{K}\in\mathcal{S}$, $\sigma^{\mathsf{real}}_{s_0}$,
$\mathcal{D}^{\mathsf{real}}_{S,\mathrm{K}}$, $\Pr[s_0\notin\mathcal{I}]=0$. The extractor's glyph soup in Section 2.1 (superscripts
run into the prose, '<sup>' tags, 'Pr[ s 0 ∈I/ ]') was replaced. Headings: '2 Preliminaries' (##) and '2.1 Stochastic Dynamical
Systems' (###) with the printed numbering; the extractor had them as '#'/'##' with bold markers. 'Notation' and 'Training and
Deployment Environments' are bold run-in paragraph titles (\mypara), kept as bold text followed by a full stop. Printed wording kept:
'caligraphic' (authors' spelling), 'then conduct', 'trajectory’s sensitivity', 'ReLU' (upright, written as plain text), the definition of
$\lceil x\rceil$ as 'the smallest integer greater than $x$'. Note for readers: the realization is written $s_1,\ldots,s_\mathrm{K}$ and the
joint distribution is over $S_1,\ldots,S_\mathrm{K}$ (index starts at 1), while the random vectors are $S_0,\ldots,S_\mathrm{K}$; this is as
printed. Line-wrap hyphen of 'distribu-tion' removed. The last paragraph is cut by the page break after 'environments. We'; page 4
continues it (join_previous 'space'). Omitted: page number 3.
""")
