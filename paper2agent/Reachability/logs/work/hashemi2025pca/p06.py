from pagelib import *
o = orig(6)
B = lambda k: o[k]["bbox"]

items = [
    text("p0006-b000", B("p0006-b000"), X(
         r"""Since $\Pr[P^* = \top] \geq \delta$, this star set serves as such a bounding region for $\PE$. We refer to this bounding region as inflating hypercube.""")),
    text("p0006-b001", B("p0006-b001"), X(
         r"""**$\delta$-Confident Flowpipe & Probabilistic Reachability**. For a given confidence probability $\delta\in (0,\ 1)$, and $\statee_0 \sim \mathcal{W}$, we say that $X \subseteq \reals^{n\horizon}$ is a $\delta$-confident flowpipe if for any random trajectory $\trajreal_{\statee_0} \sim \dist$, we have $\Pr[\trajreal_{\statee_0} \in X ] \geq \delta$. In this paper, our ultimate goal is to propose a $\delta$-confident flowpipe. To compute such a flowpipe, the authors in Hashemi et al. (2024b) suggest simulating a set of trajectories, $\trajsim_{\statee_0} \sim \distzero, \statee_0 \sim \mathcal{W}$ and training a ReLU NN surrogate model $\overallf(\statee_0 ; \theta)$ on this dataset. This model will be utilized to compute for its surrogate reachset, $\bar{X}\subset \mathbb{R}^{n\horizon}$. They also sample a new set of trajectories $\trajsim_{\statee_0} \sim \distzero, \statee_0 \sim \mathcal{W}$ for error analysis on $\overallf(\statee_0 ; \theta)$ through robust conformal inference to compute for another hypercube $\delta X \subset \mathbb{R}^{n\horizon}$, known as the inflating hypercube, that covers the prediction errors $R^j , j\in[n\horizon]$ for trajectories $\trajreal_{\statee_0} \sim \dist$, with a provable probabilistic guarantee, and finally they propose the following lemma to compute for the $\delta$-confident flowpipe on $\trajreal_{\statee_0} \sim \dist, \statee_0 \sim \mathcal{W}$. See Hashemi et al. (2024b) for the proof.""")),
    text("p0006-b002", B("p0006-b002"), X(
         r"""**Lemma 3.** Let $\bar{X}$ be a surrogate flowpipe of the surrogate model $\overallf$ for the set of initial conditions $\init$. Let $\PEreal:=\left[ \errreal{1} , \errreal{2}, \ldots , \errreal{n\horizon} \right]$ be the sequence of prediction errors for $\trajreal_{\statee_0} \sim \dist$, where $\statee_0 \sim \mathcal{W}$, and let $\delta X$ be the inflating hypercube for $\PEreal$ such that $\Pr[\PEreal \in \delta X] > \delta$. Then the inflated reachset $X = \bar{X} \oplus \delta X$ is a $\delta$-confident flowpipe for $\trajreal_{\statee_0} \sim \dist$ where $\statee_0 \sim \mathcal{W}$.""")),
    heading("p0006-b003", B("p0006-b003"), "### 2.4 Problem Definition"),
    text("p0006-b004", B("p0006-b004"), X(
         r"""We are interested in computing a $\delta$-confident flowpipe $X$ from a set of trajectories $\trajsim_{\statee_0}$ collected from $\distzero$ so that $X$ is also valid for all trajectories $\trajreal_{\statee_0} \sim \dist$ when the total variation between $\distR$ and $\distzeroR$ is less than $\tau>0$. While we are motivated by the results in Hashemi et al. (2024b) which propose a solution to the stated problem, we note that their solution lacks scalability and accuracy that results in sometimes large levels of conservatism, i.e., the set $X$ is unnecessarily large.""")),
    text("p0006-b005", B("p0006-b005"), X(
         r"""The primary sources of conservatism and inaccuracy in the methodology described in Hashemi et al. (2024b) stem from the training process for the surrogate model $\overallf(\statee_0\ ; \theta)$ and the method used to compute the inflating hypercube $\delta X$. In the following sections, we address both issues and propose solutions to improve the accuracy and scalability of this approach for the reachability analysis.""")),
    heading("p0006-b006", B("p0006-b006"), "## 3 Scalable and Accurate Data Driven Reachability Analysis"),
    text("p0006-b007", B("p0006-b007"),
         "In this section, we introduce two key adjustments to the methodology of Hashemi et al. (2024b) to enhance scalability and reduce conservatism."),
    heading("p0006-b008", B("p0006-b008"), "### 3.1 Improved Scalabilty and Accuracy for Training Surrogate Models"),
    text("p0006-b009", B("p0006-b009"), X(
         r"""In this section, we introduce a new training strategy for the model $\overallf(\statee_0\ ;\theta)$ that avoids the scalability issues arising from the surrogate model’s large size when handling long time horizons, as encountered in Hashemi et al. (2024b). Figure 1 illustrates a realization of a trajectory $\trajsim_{\statee_0} := \statee_1, \ldots, \statee_{\horizon}$ over the horizon $\horizon$. In this figure, we divide the time horizon into $N$ segments, each with length $T_q$, where $q \in [N]$. We denote each trajectory segment as""")),
    omit("p0006-b010", B("p0006-b010"), "6",
         "Printed page number 6 centred at the foot of the page; page furniture, checked on the 170 dpi render."),
]

save(6, items, r"""
Compared with the 170 dpi render, a 260 dpi crop of the upper half (down to Lemma 3), a 220 dpi crop of the lower half, and the TeX
source (sections/prelim.tex, sections/DDReach.tex, sections/Training.tex, main file for the section titles). All inline math rewritten
in LaTeX from the TeX source with macros expanded and checked on the crops; TeX and PDF agree. Checked in particular: definition of a
$\delta$-confident flowpipe, $\Pr[\sigma^{\mathsf{real}}_{s_0}\in X]\ge\delta$ (non-strict); Lemma 3 with $\mathsf{PE} := [R^1, R^2,
\ldots, R^{n\mathrm{K}}]$, hypothesis $\Pr[\mathsf{PE}\in\delta X] > \delta$ (strict) and conclusion $X=\bar{X}\oplus\delta X$;
Section 2.4: total variation between $\mathcal{J}^{\mathsf{real}}_{S,\mathrm{K}}$ and $\mathcal{J}^{\mathsf{sim}}_{S,\mathrm{K}}$ 'is
less than $\tau>0$'. 'Lemma 3.' is printed in bold with a full stop; the lemma shares the counter of the definitions (Definition 1,
Definition 2, Lemma 3). Its body is italic in the print, written upright here; it ends at '... where $s_0\sim\mathcal{W}$.' (end of the
TeX environment). The paper gives no proof ('See Hashemi et al. (2024b) for the proof.' precedes the lemma). Headings: '2.4 Problem
Definition' (###), '3 Scalable and Accurate Data Driven Reachability Analysis' (##), '3.1 Improved Scalabilty and Accuracy for Training
Surrogate Models' (###; the misspelling 'Scalabilty' is printed so and kept). The run-in title '$\delta$-Confident Flowpipe &
Probabilistic Reachability' is bold text (the $\delta$ is in math italic), followed by a full stop. Printed wording kept: '$\delta\in
(0,\ 1)$' with a wider gap, 'compute for its surrogate reachset', 'which propose a solution', 'ReLU NN'. The extractor's glyph soup
(including a replacement character in the Lemma 3 bracket and merged superscripts in Section 2.4) was replaced. The last paragraph is
cut by the page break after 'We denote each trajectory segment as'; page 7 continues it (join_previous 'space'). Omitted: page number 6.
""")
