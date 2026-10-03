from pagelib import *
o = orig(7)
B = lambda k: o[k]["bbox"]

items = [
    text("p0007-b002", B("p0007-b002"), X(
         r"""$\trajsimseg{q}_{\statee_0},\ q \in [N]$, defined as:"""), join_previous="space"),
    text("p0007-b003", [174.0, 219.0, 529.0, 257.0], X(
         r"""$$\trajsimseg{q}_{\statee_0} := \statee_{t_q+1}, \statee_{t_q+2}, \ldots, \statee_{t_q+T_i}, \quad t_q = \sum_{\ell=1}^{q-1} T_\ell,\ t_1 = 0. \tag{8}$$""")),
    text("p0007-b004", [89.0, 260.0, 524.0, 329.0], X(
         r"""The key idea is to directly link each trajectory segment $\trajsimseg{q}_{\statee_0},\ q \in [N]$ to its initial state $\statee_0 \in \init$. Thus, we can train an independent model $\overallf_q(\statee_0\ ; \theta_q),\ q \in [N]$ for each segment, which predicts $\trajsimseg{q}_{\statee_0}$ directly based on the initial state $\statee_0$. This model is also used to compute surrogate flowpipes for the trajectory segments $\bar{X}_q, q \in [N]$, representing the image of set $\init$ through the model $\overallf_q(\init\ ; \theta_q)$.""")),
    figure("p0007-b000", [170.0, 86.0, 444.0, 166.0], "Figure 1", "figure-1"),
    caption("p0007-b001", B("p0007-b001"), X(
         r"""Figure 1: This figure shows the division of the trajectory into $N$ different segments $\trajsimseg{q}_{\statee_0}, q\in[N]$""")),
    text("p0007-b005", B("p0007-b005"), X(
         r"""Here are the reasons why this new training strategy for the trajectory $\trajsim_{\statee_0}$ resolves all the scalability issues, we listed for Hashemi et al. (2024b), in the Introduction section. First and foremost, since all surrogate models $\overallf_q(\statee_0\ ; \theta_q), q \in [N]$ are directly connected to the initial state, we do not need to iterate them sequentially over the time horizon for prediction of states in $\trajsimseg{q}_{\statee_0}, q\in[N]$, thus eliminating the problem of cumulative errors over the time horizon. Furthermore in this setting, the size of the models $\overallf_q(\statee_0\ ; \theta_q), q \in [N]$ can be small. The small size of the models allows for efficient computation of surrogate flowpipes $\bar{X}_q := \overallf_q(\init\ ; \theta_q)$ for each segment via exact-star reachability analysis $^{4}$. Additionally, the smaller models $\overallf_q(\statee_0\ ; \theta_q), q \in [N]$ enable efficient training of accurate models for each trajectory segment. Furthermore, although we have to train more models using this technique, we can train them in parallel as they are totally independent processes.""")),
    text("p0007-b008", B("p0007-b008"), X(
         r"""Footnote 4: However, if the set of initial states $\init$ is large and the partitioning of $\init$ is not scalable (high dimensional states), we remain limited to using approx star. Nevertheless, even for this case, the small size of the model significantly reduces the conservatism of approx star.""")),
    text("p0007-b005b", [90.0, 480.0, 525.0, 536.0], X(
         r"""Once the surrogate flowpipes $\bar{X}_q = \langle \bar{c}_q, \bar{V}^q, \bar{P}_q \rangle$, for $q \in [N]$, are obtained as star sets, the surrogate flowpipe for the entire trajectory forms another star set, $\bar{X} = \langle \bar{c}, \bar{V}, \bar{P} \rangle$. This global surrogate flowpipe is constructed by concatenating all individual star sets $\bar{X}_q$, for $q \in [N]$, which implies: $\bar{c} = \left[ \bar{c}_1^\top , \ldots , \bar{c}_N^\top \right]^{\top}$, $\bar{V} = \mathbf{diag}\left(\bar{V}^1, \ldots, \bar{V}^N\right)$ and $\bar{P} = \bigwedge_{q=1}^N \bar{P}_q$.""")),
    heading("p0007-b006", B("p0007-b006"), "### 3.2 Accurate Inflating Hypercubes via Principal Component Analysis"),
    text("p0007-b007", B("p0007-b007"), X(
         r"""Principal Component Analysis (PCA) is a mathematical technique used to identify the principal directions of variation in a dataset. Given a dataset of $L$ data points, $x_i \in \mathbb{R}^{n}, i\in[L]$, PCA estimates the covariance matrix, $\Sigma \succeq 0, \Sigma \in \mathbb{R}^{n\times n}$ of data points $x_i, i\in[L]$. The eigenvectors of $\Sigma$, known as **principal components**, define the directions along which the data exhibits the highest variance, while the corresponding eigenvalues quantify the magnitude of variance along each direction. These principal components form an orthonormal basis that aligns with the natural structure of the data, providing key insights into its intrinsic geometric properties.""")),
    omit("p0007-b009", B("p0007-b009"), "7",
         "Printed page number 7 centred at the foot of the page; page furniture, checked on the 170 dpi render."),
]
# the paragraph 'Here are the reasons ...' and 'Once the surrogate flowpipes ...' were one extractor item: split the bbox
items[5]["bbox"] = [90.0, 329.0, 525.0, 480.0]

save(7, items, r"""
Compared with the 170 dpi render, a 240 dpi crop of the text from the Figure 1 caption to the end of Section 3.1, a 300 dpi crop of
Figure 1 with margins, and the TeX source (sections/Training.tex, sections/PCA.tex). The page prints Figure 1 at the top, before the
continuation of the sentence from page 6; the items are ordered so that the prose reads continuously: first the continuation
'$\sigma^{\mathsf{sim},q}_{s_0},\ q\in[N]$, defined as:' (join_previous 'space'), display (8), the paragraph 'The key idea ...', then
Figure 1 and its caption, then the rest. Figure 1: image crop with all in-figure labels ($s_0$, $T_1,\ldots,T_6$, $T_{N-1}$, $T_N$,
segment labels $\sigma^{\mathsf{sim},1}_{s_0},\ldots,\sigma^{\mathsf{sim},N}_{s_0}$, 'k = 0', 'k = K'); bbox edges checked on the 300
dpi crop (the figure is a raster image, so its labels are not in the text layer). Caption verbatim (it has no final full stop).
Mathematics from the TeX source with macros expanded (\trajsimseg{q} -> \sigma^{\mathsf{sim},q}, \overallf_q -> \mathcal{F}_q) and
checked on the crop. The extractor's formula image was replaced by the LaTeX display (8). SOURCE TYPO KEPT: in (8) the last state of
segment $q$ is printed $s_{t_q+T_i}$ (index $T_i$; the segment length is $T_q$ everywhere else); TeX and PDF agree on this. $t_q =
\sum_{\ell=1}^{q-1}T_\ell$, $t_1=0$. In the last paragraph of Section 3.1, $\mathbf{diag}$ is printed in bold, $\bar{c} =
[\bar{c}_1^\top,\ldots,\bar{c}_N^\top]^\top$, $\bar{V} = \mathbf{diag}(\bar{V}^1,\ldots,\bar{V}^N)$, $\bar{P}=\bigwedge_{q=1}^N\bar{P}_q$
(the final full stop, inside the math in the TeX, is written after it). The extractor had merged the paragraphs 'Here are the reasons
...' and 'Once the surrogate flowpipes ...' into one item; they are two paragraphs in the print and are split. Footnote 4 (mark after
'exact-star reachability analysis', printed at the foot of the page) is placed after the paragraph that carries its mark; mark written
' $^{4}$'. Heading '3.2 Accurate Inflating Hypercubes via Principal Component Analysis' as ###. 'principal components' is bold in the
print and kept bold. Printed wording kept: 'scalability issues, we listed for Hashemi et al. (2024b), in the Introduction section',
'Furthermore in this setting', 'approx star' (no hyphen in the footnote). Omitted: page number 7.
""")
