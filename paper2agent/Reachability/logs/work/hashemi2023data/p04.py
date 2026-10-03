from pagelib import *
P = 4
items = [
    text("p0004-b000", B(P, "p0004-b000"),
         r"predictive model can be difficult, especially when the dynamics are nonlinear. Hence, in practice, we train models that take as input trajectory fragments to predict future trajectory fragments and then sequentially compose such models to obtain a longer predicted trajectory. We remark that this does not affect the probabilistic reasoning that we perform later in the paper as the entire predictive model can still be treated as a deterministic map that takes as input the initial state $s_0$ and outputs a $\mathrm{K}$-step predicted trajectory.",
         join_previous="space"),
    text("p0004-b001", B(P, "p0004-b001"),
         r"**Conformal Inference.** Conformal inference [22, 23, 29] is a statistical tool for uncertainty quantification that has recently been used for analysing the uncertainty in the predictions performed by complex machine learning models [30–32]. Conformal inference/prediction performs error quantification without making any assumption on the underlying data-generating distribution or the machine learning model. Consider a regression model $\mu$ and the random variables $z_1,z_2,...,z_{m+1}$ where $z_i=(x_i,y_i) \in \mathbb{R}^n \times \mathbb{R}$ with $i\in [m + 1]$ which are all independently sampled from the same distribution. Given a miscoverage level $\alpha \in (0, 1)$, conformal inference enables us to compute a prediction interval $C(x_{m+1})=[\mu(x_{m+1})-R^{\ast},\ \mu(x_{m+1})+R^{\ast}] \subset \mathbb{R}$ from $z_1,z_2,...,z_{m}$ such that,"),
    display("p0004-b002", B(P, "p0004-b002"),
            r"\Pr[ y_{m+1} \in C(x_{m+1})] \geq 1- \alpha."),
    text("p0004-b003", B(P, "p0004-b003"),
         r"More formally, define the residual $R_i=\mid y_i-\mu(x_i) \mid$ for all $z_i$ with $i\in [m + 1]$. Since the random variables $z_1,z_2,...,z_{m+1}$ are independent and identically distributed, the same applies to the residual $R_1,\ldots, R_{m+1}$. Under the assumption that $m$ satisfies $\ell=\lceil (m+1)(1-\alpha)\rceil\le m$, it holds that $R^{\ast}$ can be chosen to be the $\ell$-th smallest residual [33, Lemma 1]. Without loss of generality, if $R_1,\ldots, R_{m}$ are sorted in non-decreasing order, then $R^{\ast}=R_\ell$ and it holds that $\Pr[ R_{m+1} \leq R^{\ast}] \geq (1-\alpha)$. By the choice of the residual, it hence holds that"),
    display("p0004-b004", B(P, "p0004-b004"),
            r"\Pr\Big[ y_{m+1} \in [\mu(x_{m+1})-R^{\ast},\ \mu(x_{m+1})+R^{\ast}] \Big] \geq 1-\alpha."),
    text("p0004-b005", B(P, "p0004-b005"),
         r"We also refer to $\delta = 1-\alpha$ as the confidence probability."),
    text("p0004-b006", B(P, "p0004-b006"),
         r"**Problem Definition.** Our probabilistic reachability analysis can be formally stated as follows. Given the stochastic dynamical system $M$ with initial state $s_0 \stackrel{\mathcal{W}}{\sim} \mathcal{I}$ and trajectory distribution $\mathcal{S}$, training and test datasets $D_{\text{train}}$ and $D_{\text{test}}$ consisting of $\mathrm{K}$-step trajectories independently sampled from $M$, and a user provided failure probability threshold $\varepsilon \in (0,1)$, compute a probabilistic reach set (also called flowpipe) $X$ such that:"),
    display("p0004-b007", B(P, "p0004-b007"),
            r"\Pr\left[ \sigma_{s_0} \in X \right] \geq 1-\varepsilon \tag{1}"),
    heading("p0004-b008", B(P, "p0004-b008"), "## 3 Scalable Data-Driven Reachability"),
    text("p0004-b009", B(P, "p0004-b009"),
         r"In the setting described in the previous section, we now show how to compute a reach set or a flowpipe $X\subset \mathbb{R}^{n(\mathrm{K}+1)}$ using reachability analysis and conformal inference. This flowpipe will contain the trajectory $\sigma_{s_0}$ of $M$ sampled with initial state $s_0 \stackrel{\mathcal{W}}{\sim} \mathcal{I}$ with the confidence level of $\Delta = 1-\varepsilon$. We hence denote this flowpipe as $\Delta$-confident flowpipe and define it as follows."),
    text("p0004-b010", B(P, "p0004-b010"),
         r"**Definition 1 ($\Delta$-confident flowpipe).** For a given confidence probability $\Delta\in (0,\ 1)$ and a random trajectory $\sigma_{s_0} \sim \mathcal{S}$ with initial state $s_{0} \stackrel{\mathcal{W}}{\sim} \mathcal{I}$, we say that $X \subset \mathbb{R}^{n(\mathrm{K}+1)}$ is a $\Delta$-confident flowpipe if"),
    display("p0004-b011", B(P, "p0004-b011"),
            r"\Pr[\sigma_{s_0} \in X ] \geq \Delta \tag{2}"),
    pageno(P),
]
save(P, items, r"""
Compared with the 130 dpi render and a 190 dpi crop of PDF page 4, and with sections/PSandprelim.tex and
sections/verification.tex. The first item continues the sentence from page 3 ('Training such a K-step | predictive model
...') with join_previous 'space'. All inline and display mathematics rewritten in LaTeX from the TeX source with macros
expanded and checked symbol by symbol against the crop; TeX and PDF agree. The four extractor 'formula' image items were
replaced by $$ text items; only the two displays with printed numbers carry \tag: (1) the problem statement
$\Pr[\sigma_{s_0}\in X]\ge 1-\varepsilon$ and (2) the definition of a $\Delta$-confident flowpipe; the two conformal
inference displays are unnumbered. Changes of notation that do not change the printed symbols: \hdots written \ldots,
$R^*$ written $R^{\ast}$ (two asterisks in one paragraph would pair as Markdown emphasis). The authors type absolute
values with \mid ('$R_i=\mid y_i-\mu(x_i)\mid$'), which is kept. Run-in bold paragraph titles 'Conformal Inference.' and
'Problem Definition.' start their paragraphs in bold (not section headings). 'Definition 1 ($\Delta$-confident
flowpipe).' is printed with bold 'Definition 1', an upright parenthesis and a bold full stop; the whole label is given in
bold. Definition 1 ends with display (2), which has no final full stop (end of the definition environment in the TeX
source); its italic body is not reproduced in italics. Citations checked on the page: [22, 23, 29], [30–32],
[33, Lemma 1]. Line-wrap hyphens removed in 'quantification' (twice); 'data-generating', 'non-decreasing', '$\ell$-th'
are printed compounds. 'a user provided failure probability threshold' has no hyphen in the source. Section heading
'3 Scalable Data-Driven Reachability' is level 2.
""")
