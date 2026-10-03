from pagelib import *
P = 5
items = [
    text("p0005-b000", B(P, "p0005-b000"),
         r"In this work, we are interested in computing $X$ while our access to $M$ is limited to the datasets $D_{\text{train}}$ and $D_{\text{test}}$. We will show that we can compute $X$ with valid guarantees by employing reachability analysis on the surrogate model trained from $D_{\text{train}}$ and error analysis of this model by applying conformal prediction on $D_{\text{test}}$."),
    heading("p0005-b001", B(P, "p0005-b001"), "### 3.1 Computing Reachsets for Surrogate Models"),
    heading("p0005-b002", B(P, "p0005-b002"), "#### 3.1.1 ReLU Surrogate Model"),
    text("p0005-b003", [71.0, 181.0, 540.0, 234.0],
         r"We start with training a neural network surrogate model $\mathcal{F}: \mathbb{R}^n \to \mathbb{R}^{n(\mathrm{K}+1)}$ over the training dataset $D_{\text{train}}$. The surrogate model is trained to approximate the trajectory $\sigma_{s_{0}} \in \mathbb{R}^{n(\mathrm{K}+1)}$ of the stochastic system $M$ sampled with initial state $s_0 \stackrel{\mathcal{W}}{\sim} \mathcal{I}$. We denote the prediction $\bar{\sigma}_{s_{0}} \in \mathbb{R}^{n(\mathrm{K}+1)}$ of $\sigma_{s_{0}}$ as,"),
    display("p0005-b004", [121.0, 234.0, 491.0, 266.0],
            r"\bar{\sigma}_{s_{0}} = \mathcal{F}(s_{0}) = \left[ s_0^\top ,\ \mathsf{F}^1(s_0) , \ \cdots ,\ \mathsf{F}^n(s_0), \ \cdots , \ \mathsf{F}^{(n-1)\mathrm{K}}(s_0) ,\ \cdots ,\ \mathsf{F}^{n\mathrm{K}}(s_0)\right]^\top"),
    text("p0005-b005", B(P, "p0005-b005"),
         r"where $\mathsf{F}^j(s_0)$ is the $(j+n)$-th component of the vector $\mathcal{F}(s_0)$."),
    text("p0005-b006", B(P, "p0005-b006"),
         "Recent works in the literature have had great success on obtaining accurate bounds for the reachability analysis of ReLU neural networks using polyhedral sets [21, 34, 35]. The accuracy of these techniques motivates us to use ReLU activation functions for training neural networks as the surrogate models. These surrogate models will be used for deterministic reachability analysis which provides surrogate flowpipes which we formally define next."),
    text("p0005-b007", B(P, "p0005-b007"),
         r"**Definition 2 (Surrogate flowpipe).** The surrogate flowpipe $\bar{X}\subset \mathbb{R}^{n(\mathrm{K}+1)}$ contains the image of $\mathcal{F}(\mathcal{I})$. Formally, for all, $s_0\in \mathcal{I}$ it has to hold that $\mathcal{F}(s_0) \in \bar{X}$."),
    text("p0005-b008", B(P, "p0005-b008"),
         r"The reachability analysis methodology for ReLU neural networks in [21] introduces two different approaches known as the exact-star and approx-star techniques. These are used to compute a surrogate flowpipe $\bar{X}$. The exact-star technique proposes exact reachability analysis using star sets, but can be slower due to its inherent computational complexity. On the other hand, the approx-star technique computes over-approximation of the flowpipe and is thus runtime-efficient, although it may make the surrogate model reachable set estimation conservative. The computational complexity of the exact-star technique and the conservatism of the approx-star technique can both be noticeably reduced using the idea of set partitioning [21]. In this approach, we partition the set of initial conditions $\mathcal{I}$ into $N$ different sub-partitions,"),
    display("p0005-b009", B(P, "p0005-b009"),
            r"\mathcal{I}_i \subset \mathcal{I} , \quad \bigcup_{i=1}^N \mathcal{I}_i =\mathcal{I},"),
    text("p0005-b010", B(P, "p0005-b010"),
         r"and perform reachability analysis on every single sub-region with parallel computing. The inclusion of set-partitioning results in noticeable improvement in the computational efficiency and helps us compute more accurate $\Delta$-confident flowpipes."),
    heading("p0005-b011", B(P, "p0005-b011"), r"### 3.2 Computation of a guaranteed $\Delta$-confident flowpipe"),
    text("p0005-b012", B(P, "p0005-b012"),
         r"When we train neural network surrogate models, typically we minimize a loss function defined as the difference between the $\mathrm{K}$-step trajectory predicted by the surrogate model and the actual trajectory. Depending on the dynamics of the underlying stochastic system $M$ and depending on how well the surrogate model is trained, there is potential for error when predicting the trajectory"),
    pageno(P),
]
save(P, items, r"""
Compared with the 130 dpi render and a 190 dpi crop of PDF page 5, and with sections/verification.tex. Inline and display
mathematics rewritten in LaTeX from the TeX source with macros expanded (\overallf -> \mathcal{F}, \traj -> \sigma,
\init -> \mathcal{I}, \horizon -> \mathrm{K}; the macro \relu prints an upright 'ReLU' and is written as the plain word
ReLU) and checked against the crop; TeX and PDF agree. The two extractor 'formula' image items were replaced by $$ text
items; neither display is numbered in the paper. In the display of the predicted trajectory the component functions are
sans-serif $\mathsf{F}^j$ (distinct from the calligraphic surrogate model $\mathcal{F}$), with superscripts 1, n,
(n-1)K and nK as printed. The extractor's text box for the paragraph before that display overlapped the display; the
boxes were separated at y = 234 pt. Headings: '3.1 Computing Reachsets for Surrogate Models' level 3, '3.1.1 ReLU
Surrogate Model' level 4, '3.2 Computation of a guaranteed $\Delta$-confident flowpipe' level 3, with printed numbers.
'Definition 2 (Surrogate flowpipe).' label in bold; the definition ends at '$\mathcal{F}(s_0) \in \bar{X}$.' (end of the
definition environment in the TeX source; italic body not reproduced in italics); 'for all, $s_0\in\mathcal{I}$' with the
comma as printed. Citations [21, 34, 35], [21] (twice) checked on the page. Line-wrap hyphen removed in 'reachability'
('reach-ability'); printed compounds kept: exact-star, approx-star, over-approximation, runtime-efficient,
sub-partitions, sub-region, set-partitioning. The last paragraph ends in the middle of a sentence ('when predicting the
trajectory'); it continues on page 6.
""")
