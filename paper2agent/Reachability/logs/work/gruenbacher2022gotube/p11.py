from pt import *
chain = "\n\n".join([
 r"$$Pr\big(\sup_x\big(G_n(x)-F(x)\big)>\epsilon_{n,\gamma} + D_n^-\big) = \tag{S7}$$",
 r"$$= Pr\Big(\sup_x\big(G_n(x)-\hat{F}_n(x)+ \tag{S8}$$",
 r"$$\qquad + \hat{F}_n(x)-F(x)\big)>\epsilon_{n,\gamma} + D_n^-\Big) \tag{S9}$$",
 r"$$\le Pr\Big(\sup_x\big(G_n(x)-\hat{F}_n(x)\big) + \tag{S10}$$",
 r"$$\qquad +\sup_x\big(\hat{F}_n(x)-F(x)\big)>\epsilon_{n,\gamma} + D_n^-\Big) \tag{S11}$$",
 r"$$\overset{\text{(S1)}}{=} Pr\big(\sup_x\big(\hat{F}_n(x)-F(x)\big)>\epsilon_{n,\gamma}\big) \tag{S12}$$",
 r"$$\overset{\text{(S6)}}{\le} \gamma, \tag{S13}$$",
])
items = [
 H("## Appendix", (148, 198.5), 55, 67),
 H("### Proofs of the Theorems", (119, 228), 70, 80.5),
 T(r"**Lemma 1 (Stochastic lower bound $F_{L,\gamma}$)** Consider the experiment of randomly sampling two times $m$ points of the initial ball $\mathcal{B}_0$: $(a_1,\dots,a_m)$ and $(b_1,\dots,b_m)$. Let $g : \mathbb{R}^n \rightarrow \mathbb{R}$ be a real-valued function and $X = \max_{i=1}^m|g(a_i) - g(b_i)|/\|a_i - b_i\|$ be a random variable with the unknown cumulative distribution function $F$. Let $(x_1, \dots, x_n)\sim X$ be independent, identically distributed samples with the empirical distribution function $\hat{F}_n(x) = \sum_{i=1}^n\mathbb{1}_{x_i\le x}$. Let $G_n$ be a generalized extreme value distribution fitted to the empirical distribution function $\hat{F}_n$ and let $D_n^-$ describe the goodness of fit, being the one-sided Kolmogorov–Smirnov statistic:", L, 90, 224),
 T(r"$$D_n^- = \sup_x (G_n(x) - \hat{F}_n(x)) \tag{S1}$$", L, 230, 258),
 T(r"Given the confidence level $\gamma$ and $\alpha = \min(\gamma, 0.5)$, then let us define $\epsilon_{n,\gamma}$ and $F_{L,\gamma}$ as follows:", L, 265, 288.5),
 T(r"$$\epsilon_{n,\gamma} = \sqrt{\frac{\ln{\frac{1}{\alpha}}}{2n}} \tag{S2}$$" + "\n\n" + r"$$F_{L,\gamma}(x) = G_n(x) - \epsilon_{n,\gamma} - D_n^- \tag{S3}$$", L, 294, 350),
 T(r"Then it holds that:", L, 356, 366),
 T(r"$$Pr(\sup_x(F_{L,\gamma}(x)-F(x))\le 0)\ge 1-\gamma, \tag{S4}$$", L, 372, 399),
 T(r"which intuitively means that $F_{L,\gamma}$ is a lower bound of $F$ with confidence $\gamma$.", L, 405.5, 427),
 T(r"**Proof.** The Fisher-Tippett-Gnedenko theorem states that the distribution of a normalized maximum converges to the generalized extreme value distribution, if the distribution of the normalized maximum does converge. So intuitively that theorem is similar to the central limit theorem for the averages, but for the normalized maxima. Consequently, we start by fitting the empirical distribution function $\hat{F}_n$ by a generalized extreme value distribution $G_n$ and compute Eq. (S1).", L, 437.5, 527.5),
 T(r"The Dvoretzky-Kiefer-Wolfowitz inequality (Dvoretzky, Kiefer, and Wolfowitz 1956) with a tight constant determined by (Massart 1990), states that for all $\epsilon \ge \sqrt{\frac{1}{2n}\ln 2}$, it holds that:", L, 529, 579),
 T(r"$$Pr(\sup_x(\hat{F}_n(x)-F(x))>\epsilon)\le e^{-2n\epsilon^2} \tag{S5}$$", L, 582, 612),
 T(r"Solving $\gamma = e^{-2n\epsilon^2}$ for $\epsilon$ and considering Massarts lower bound for $\epsilon$, yields:", L, 614, 643),
 T(r"$$Pr(\sup_x(\hat{F}_n(x)-F(x))>\epsilon_{n,\gamma}) \le \gamma, \tag{S6}$$", L, 648, 677),
 T(r"with $\epsilon_{n,\gamma}$ as defined in Eq. (S2). We use the triangular inequality for supremum and the monotony of the probability measure as follows:", L, 683.5, 705),
 T(chain, R, 67, 229),
 T("from which it follows directly, that Eq. (S4) hold.", R, 230.5, 241.5),
 FIG("Figure S1", "supplementary-figure-1", [326, 262, 548, 430], cat="supp_figs"),
 C(r"Figure S1: Visualisation of the stochastic lower bound $F_{L,\gamma}$ of Lemma 1.", R, 442, 463.5),
 T("*Conversion note on Figure S1 (not printed text): the legend inside the figure reads 'fitted G(x)' (solid line), 'lower bound F_L(x)' (dashed line) and 'empirical cdf F_n(x)' (shaded bars); the axes carry tick labels only.*", R, 464, 468),
 T(r"**Theorem 1 (Radius of Stochastic Lipschitz Caps)** Given a continuous-depth model $f$ from Eq. (1) in the main paper ($\partial_t x = f(x)$ with $x(t_0) \in B(x_0, \delta_0)$), $\gamma \in (0,1)$, $\mu > 1$, target time $t_j$, the set of all sampled points $\mathcal{V}$, the number of sampled points $N = |\mathcal{V}|$, the sample maximum $\bar{m}_{j,\mathcal{V}} = \max_{x\in\mathcal{V}} d_j(x)$, the IVP solutions $\chi(t_j,x)$, and the corresponding stretching factors $\lambda_x = \|\partial_x\chi(t_j,x)\|$ for all $x \in \mathcal{V}$. Let us define $\hat{\gamma} = 1-\sqrt{1-\gamma}$. Let $\Delta\lambda_{\mathcal{V}}$ be the $\sqrt{1-\gamma}$-quantile of a stochastic lower bound $F_{L,\hat{\gamma}}$ as defined in Eq. (S3) of Lemma 1:", R, 477.5, 586.5),
 T(r"$$\Delta\lambda_{\mathcal{V}}(\gamma) = F_{L,\hat{\gamma}}^{-1}(\sqrt{1-\gamma}), \tag{S14}$$", R, 588, 604),
 T(r"Let $r_x$ be defined as:", R, 606, 617.5),
 T(r"$$r_{x} = \frac{\left(-\lambda_x + \sqrt{\lambda_x^2 + 4\cdot\Delta\lambda_{x,\mathcal{V}}\cdot(\mu\cdot\bar{m}_{j,\mathcal{V}}-d_j(x))}\right)}{2\cdot\Delta\lambda_{x,\mathcal{V}}}, \tag{S15}$$", R, 618.5, 662),
 T(r"then it holds that:", R, 666, 675.5),
 T(r"$$\Pr\left(d_j(y) \le \mu\cdot \bar{m}_{j,\mathcal{V}}\right)\ge 1-\gamma\quad \forall y\in B(x,r_x)^S, \tag{S16}$$", R, 677, 690.5),
 T(r"and thus that $B(x, r_x)^S$ is a $\gamma, t_j$-Lipschitz cap.", R, 691.2, 705),
]
notes = r"""
Compared with 250 dpi crops of PDF page 11 that together cover the whole page (left column in two halves, top and bottom of the right column), a 200 dpi crop of Figure S1 with its caption, and with the authors' TeX
source (supplements.tex); all mathematics taken from the TeX source (macros \calB, \calV -> \mathcal{B}, \mathcal{V}; \R -> \mathbb{R}; \rd -> \delta; spacing-only '\,{=}\,', '\,{-}\,' etc. written plainly;
'\frac1{\alpha}' and '\frac1{2n}\ln2' written with braces; \eqref numbers resolved) and checked symbol by symbol against the crops; TeX and PDF agree.
Heading: the appendix title is printed as two centred bold lines, 'Appendix' in section size and 'Proofs of the Theorems' in a smaller size (one \section title with a line break in the TeX source);
written as a level-2 heading 'Appendix' followed by a level-3 heading 'Proofs of the Theorems' (the extractor had one level-1 heading). The appendix numbers its equations (S1), (S2), ... and its figure S1;
the theorem counter is reset, so the appendix restates Theorem 1 (and Theorem 2 on page 13) under the same numbers as the main text; Lemma 1 exists only in the appendix.
Lemma 1: label printed in bold with the math symbol inside the parentheses and no period ('Lemma 1 (Stochastic lower bound F_{L,gamma})'); the italic body is not reproduced in italics; the statement runs from
'Consider the experiment' through displays (S1), (S2)-(S3), (S4) to '... a lower bound of $F$ with confidence $\gamma$.' (end of the TeX environment; seven items). 'Proof.' is printed in italics (written in bold as a
label); no end-of-proof mark is printed. The restated Theorem 1 runs from 'Given a continuous-depth model' through (S14), (S15), (S16) to 'and thus that ... Lipschitz cap.' (seven items); it differs from the
main-text Theorem 1 only in 'Eq. (1) in the main paper ($\partial_t x = f(x)$ with $x(t_0) \in B(x_0,\delta_0)$)' and 'as defined in Eq. (S3) of Lemma 1'.
Displays: all 16 printed numbers (S1)-(S16) of this page are given with \tag. (S2) and (S3) are two lines of one aligned display (one item, two blocks). The seven-line chain (S7)-(S13) carries a number on every
line; it is one item with one display block per printed line, so each relation keeps its tag (line breaks inside the big parentheses as printed: \Big( opens in (S8) and (S10) and closes in (S9) and (S11));
the stacked references over the relation signs in (S12) and (S13) are '(S1)' and '(S6)'. The extractor's twelve formula images were replaced.
As printed in the source (not conversion errors): the probability operator is an italic 'Pr' in (S4)-(S13) (typed as letters) but an upright operator in (S16); the empirical distribution function is printed as
the plain sum of indicators without a factor 1/n; the indicator is a double-struck 1 (\mathbbm{1} in the source, written \mathbb{1}); the letter $n$ is the dimension in $\mathbb{R}^n$ and also the number of samples
$x_1,\dots,x_n$, and $x$ denotes both those samples and the argument of the distribution functions; 'confidence level $\gamma$' with 'lower bound ... with confidence $\gamma$' although (S4) has $1-\gamma$;
(S1) and (S5) end without punctuation; 'Massarts lower bound'; 'the triangular inequality for supremum and the monotony of the probability measure'; 'that Eq. (S4) hold'; 'Fisher-Tippett-Gnedenko' and
'Dvoretzky-Kiefer-Wolfowitz' with hyphens in the prose, 'Kolmogorov–Smirnov' with an en dash; (S14) defines $\Delta\lambda_{\mathcal{V}}$ while (S15) uses $\Delta\lambda_{x,\mathcal{V}}$.
The sentence 'with $\epsilon_{n,\gamma}$ as defined in Eq. (S2). We use ... the probability | measure as follows:' runs from the left column into the right column and is one item.
Figure S1 is printed in the right column between the end of the proof of Lemma 1 and the restated Theorem 1 and is kept there: one image crop (asset supplementary-figure-1, category supp_figs; plot frame, tick
labels and legend inside the crop, edges checked on the 200 dpi crop), the verbatim caption, and a labelled conversion note repeating the legend text. The extractor's scattered tick labels were dropped.
Line-wrap hyphens removed (vari-able, func-tion, gen-eralized, the-orem, general-ized, deter-mined, in-equality); real compounds kept (real-valued, one-sided, continuous-depth, $\sqrt{1-\gamma}$-quantile).
The page ends with the complete last line of Theorem 1; the proof starts on page 12. No page number or running head.
"""
write(11, items, notes)
