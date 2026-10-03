from pt import *
J = "\n\n".join
s18 = J([
 r"$$Pr(X \le \Delta\lambda_{\mathcal{V}}) \ge \tag{S18}$$",
 r"$$\ge Pr\Big(X\le\Delta\lambda_{\mathcal{V}} | F_{L,\hat{\gamma}(x)} \le F(x)\Big)\cdot \tag{S19}$$",
 r"$$\qquad\cdot Pr\Big(F_{L,\hat{\gamma}(x)} \le F(x)\Big) \tag{S20}$$",
])
s25 = J([
 r"$$Pr\Bigg(\lambda_x + \frac{|\lambda_x - \lambda_y|}{\|x-y\|}\cdot \|x-y\| \le \tag{S25}$$",
 r"$$\qquad\le \lambda_x + \Delta\lambda_{x,\mathcal{V}}\cdot \|x-y\|\Bigg)\ge 1-\gamma \tag{S26}$$",
])
s28 = J([
 r"$$\begin{aligned} &\Pr\big(|d_j(x)-d_j(y)|\le \\ &\quad\le (\lambda_x + \Delta\lambda_{x,\mathcal{V}}\cdot \|x-y\|) \cdot \|x-y\|\big) \ge 1-\gamma \end{aligned}$$",
 r"$$\begin{aligned} &\Pr\big(|d_j(x)-d_j(y)|\le \\ &\quad\le (\lambda_x + \Delta\lambda_{x,\mathcal{V}}\cdot r_x) \cdot r_x\big) \ge 1-\gamma \end{aligned} \tag{S28}$$",
])
s30 = J([
 r"$$\Pr\big(d_j(y) - d_j(x) \le \mu\cdot\bar{m}_{j,\mathcal{V}}-d_j(x))\big) \ge 1-\gamma$$",
 r"$$\Longleftrightarrow$$",
 r"$$\Pr\big(d_j(y) \le \mu\cdot\bar{m}_{j,\mathcal{V}})\big) \ge 1-\gamma, \tag{S30}$$",
])
s34 = J([
 r"$$\mu\cdot \bar{m}_{j,\mathcal{V}} - d_j(x) \tag{S34}$$",
 r"$$\quad\ge \mu\cdot \bar{m}_{j,\mathcal{V}} - \bar{m}_{j,\mathcal{V}} = (\mu - 1)\cdot \bar{m}_{j,\mathcal{V}} \tag{S35}$$",
 r"$$\quad\ge (\mu - 1) \cdot d_j(x_{j,1}), \tag{S36}$$",
])
s37 = J([
 r"$$\begin{aligned} & r_{bound} = \\ &\quad=\frac{-\lambda_x + \sqrt{\lambda_x^2 + 4\cdot\Delta\lambda_{x,\mathcal{V}}\cdot(\mu - 1) \cdot d_j(x_{j,1})}}{2\cdot\Delta\lambda_{x,\mathcal{V}}} \le \\ &\quad\le r_x \quad\forall x\in \mathcal{V} \end{aligned}$$",
 r"$$\begin{aligned} &\Rightarrow \Pr(\exists y\in\mathcal{V}\colon B(y, r_y)^S\owns x_j^\star) \ge \\ &\quad\ge 1 - \left( 1 - p_{r_{bound}} \right)^N \end{aligned} \tag{S37}$$",
])
items = [
 T(r"**Proof.** Let $\{x_1,\dots,x_n\}$ be $n$ independent experiments by sampling from $X = \max_{i=1}^m|\lambda_{a_i} - \lambda_{b_i}|/\|a_i - b_i\|$ as defined in Lemma 1, where each variable is the maximum of $m$ executions. From Eq. (S4) it follows that:", L, 56, 99.5),
 T(r"$$Pr(F_{L,\hat{\gamma}(x)} \le F(x))\ge 1-\hat{\gamma} = \sqrt{1-\gamma} \tag{S17}$$", L, 104, 119),
 T(r"Let us now derive the probability of $X$ being less or equal to $\Delta\lambda_{\mathcal{V}}$ defined by Eq. (S14). For any sets $A, B$ it holds that $\Pr(A)\ge \Pr(A\cap B) = \Pr(A | B) \cdot \Pr(B)$, thus:", L, 124, 156),
 T(s18, L, 161, 215),
 T(r"Let us have a look on Eq. (S19): As $Pr(X\le \Delta\lambda)=F(\Delta\lambda)$ and we are looking for the conditional probability depending on $F_{L,\hat{\gamma}(x)} \le F(x)$, we can use $F_{L,\hat{\gamma}}(\Delta\lambda)$ as a lower bound of Eq. (S19) and thus, using Eq. (S17):", L, 223, 266.5),
 T(r"$$Pr(X\le \Delta\lambda_{\mathcal{V}}) \ge F_{L,\hat{\gamma}}(\Delta\lambda_{\mathcal{V}})\cdot \sqrt{1-\gamma} \tag{S21}$$", L, 271, 286),
 T(r"As Eq. (S14) defines $\Delta\lambda_{\mathcal{V}}$ as the $\sqrt{1-\gamma}$-quantile of $F_{L,\gamma}$, we can further state that", L, 287, 313.5),
 T(r"$$\begin{aligned} \Pr(X \le \Delta\lambda_{\mathcal{V}})\ge 1-\gamma, \\ \quad \textrm{with}\quad X=\max_{i=1}^m\left[\frac{|\lambda_{a_i} - \lambda_{b_i}|}{\|a_i-b_i\|}\right] \end{aligned} \tag{S22}$$", L, 316, 357.5),
 T(r"Let $Y = |\lambda_a-\lambda_b|/\|a-b\|$ be another random variable with $a, b$ being to sample points of the initial ball $\mathcal{B}_0$. From Eq. (S22) it holds that", L, 362, 394.5),
 T(r"$$Pr(Y\le \Delta\lambda_\mathcal{V})\ge Pr(X\le \Delta\lambda_\mathcal{V})\ge 1-\gamma \tag{S23}$$", L, 400, 412),
 T(r"It trivially holds for $x, y \in \mathcal{V}$ that:", L, 417, 427.5),
 T(r"$$\begin{aligned} \lambda_y &= \lambda_x + \frac{\lambda_y - \lambda_x}{\|x-y\|}\cdot \|x-y\| \\ &\le \lambda_x + \frac{|\lambda_x - \lambda_y|}{\|x-y\|}\cdot \|x-y\| \end{aligned} \tag{S24}$$", L, 432, 484),
 T(r"From Eq. (S23) it follows that:", L, 490, 500),
 T(s25, L, 506, 562),
 T(r"and using the monotony of the probability measure:", L, 575.5, 585.5),
 T(r"$$\Pr\big(\lambda_y \le \lambda_x + \Delta\lambda_{x,\mathcal{V}}\cdot \|x-y\|\big) \ge 1-\gamma \tag{S27}$$", L, 590, 603),
 T(r"Using the mean value inequality for vector-valued functions it holds that:", L, 608.5, 629),
 T(r"$$\begin{aligned} & |d_j(x) - d_j(y)|= | \left\lVert \chi(t_j,x) - \chi(t_j,x_0)\right\rVert - \\ &\quad- \left\lVert \chi(t_j,y) - \chi(t_j,x_0)\right\rVert|\quad \textrm{\{triangle inequality\}} \\ &\quad \le \|\chi(t_j,x) - \chi(t_j,y)\|\quad \textrm{\{mean value theorem\}} \\ &\Rightarrow\exists z\in [x,y] \colon |d_j(x) - d_j(y)| \\ &\quad\le \|\partial_x \chi(t_j,z) \| \|x-y\| = \lambda_z \cdot \|x-y\| \end{aligned}$$", L, 635, 702.5),
 T(r"Combining this with Eq. (S27) and thus using $\lambda_x + \Delta\lambda_{x,\mathcal{V}}\cdot \|x-y\|$ as a probabilistic upper bound for $\lambda_z$, we obtain the following results for all $y$ with $\|x-y\| \le r_x$:", R, 56, 89),
 T(s28, R, 92, 153),
 T(r"As $r_x$ defined like in Eq. (S15) is the solution of the quadratic equation $\mu\cdot\bar{m}_{j,\mathcal{V}}-d_j(x)=\lambda_x r_x + \Delta\lambda_{x,\mathcal{V}} r_x^2$, it holds that:", R, 156.5, 188.5),
 T(r"$$\begin{aligned} &\Pr\big(|d_j(x) - d_j(y)| \le \mu\cdot\bar{m}_{j,\mathcal{V}}-d_j(x))\big) \ge \\ &\quad \ge 1-\gamma \quad\forall y\in B(x, r_x)^S \end{aligned} \tag{S29}$$", R, 190, 218.5),
 T(r"We now distinguish between two cases for $y$: (a) $d_j(y)\le d_j(x)$ and (b) $d_j(y) \ge d_j(x)$. In case (a) it is trivial: $d_j(y) \le d_j(x) \le \mu \cdot \bar{m}_{j,\mathcal{V}}$. Having case (b), Eq. (S29) is equivalent to", R, 222.5, 265.8),
 T(s30, R, 268.5, 312),
 T(r"thus Eq. (S16) holds and $B(x,r_x)^S$ is a Lipschitz cap.", R, 314, 328),
 T(r"**Theorem 2 (Convergence via Lipschitz Caps)** Given the tightness factor $\mu > 1$, the set of all sampled points $\mathcal{V}$ and the sample maximum $\bar{m}_{j,\mathcal{V}} = \max_{x\in\mathcal{V}} d_j(x)$. Let the initial ball maximum be defined by $m^\star_j=\max_{x\in\mathcal{B}_0} d_j(x)$. Then:", R, 331.5, 377),
 T(r"$$\forall\gamma\in(0,1),\exists N\in\mathbb{N}\textrm{ s.t. } \Pr(\mu\cdot\bar{m}_{j,\mathcal{V}}\ge m^\star_j) \ge 1-\gamma \tag{S31}$$", R, 378.5, 403),
 T(r"where $N=|\mathcal{V}|$ is the number of sampled points.", R, 407.5, 418),
 T(r"**Proof.** Let $x^\star_j$ be a point such that $d_j(x^\star_j) = m^\star_j$. Given $\gamma\in(0,1)$ and cap radii $r_x$ as defined in Eq. (S15), we know from the definition of a spherical cap that", R, 421, 455.8),
 T(r"$$p_{r_x} = \Pr(B(x, r_x)^S\owns x_j^\star) = \frac{\operatorname{Area}(B(x, r_x)^S)}{\operatorname{Area}(\mathcal{B}_0)} \tag{S32}$$", R, 459, 485),
 T(r"and thus it holds that:", R, 488.5, 498.5),
 T(r"$$\Pr(\exists y\in\mathcal{V}\colon B(y, r_y)^S\owns x_j^\star) = 1 - \prod_{x\in\mathcal{V}} \left( 1 - p_{r_x} \right) \tag{S33}$$", R, 501, 527.5),
 T(r"We derive a lower bound of $r_x$ by using the first sample $x_{j,1}$ and replacing the values in Eq. (S15) as follows:", R, 531, 551.8),
 T(s34, R, 555.5, 595),
 T(r"thus a lower bound of all Lipschitz cap radii is given by", R, 598.5, 608.5),
 T(s37, R, 612.5, 703),
]
notes = r"""
Compared with 250 dpi crops of both columns of PDF page 12 (two halves each, together covering the whole page) and with the authors' TeX source (supplements.tex); all mathematics taken from the TeX source
(macros \calV, \calB -> \mathcal{V}, \mathcal{B}; \area -> \operatorname{Area}; spacing-only '\,{=}\,', '\,{-}\,' written plainly; \eqref numbers resolved to the printed (S..) numbers) and checked symbol by symbol
against the crops; TeX and PDF agree. This page holds the proof of the restated Theorem 1 (left column and top of the right column), the restated Theorem 2 with display (S31), and the first half of its proof.
'Proof.' is printed in italics (written in bold as a label, twice); no end-of-proof mark is printed: the proof of Theorem 1 ends with 'thus Eq. (S16) holds and $B(x,r_x)^S$ is a Lipschitz cap.'.
Theorem 2 (bold label without period, italic body not reproduced) runs from 'Given the tightness factor' through (S31) to 'where $N=|\mathcal{V}|$ is the number of sampled points.' (end of the TeX environment).
Displays and printed numbers (all given with \tag): (S17); (S18)-(S20) three numbered lines, one block per line; (S21); (S22) two lines with one centred number (one aligned block); (S23); (S24) two lines, number on the
second line (one aligned block with the single tag); (S25)-(S26) two numbered lines, one block per line, the big parenthesis opening in (S25) and closing in (S26); (S27); the five-line mean-value display is
unnumbered (one aligned block; its bracketed remarks '{triangle inequality}' and '{mean value theorem}' are printed in upright text with braces); (S28): the display holds two two-line statements, the first
unnumbered and the second carrying (S28), written as two aligned blocks; (S29) two lines with one centred number; (S30): three lines (statement, the equivalence arrow, statement) with the number on the last line,
written as three blocks with the tag on the last; (S31); (S32) and (S33) are two numbered lines of one aligned display with the text line 'and thus it holds that:' between them - written as block, text paragraph,
block; (S34)-(S36) three numbered lines, one block per line; (S37): three unnumbered lines defining $r_{bound}$ and bounding it by $r_x$, then a two-line implication carrying (S37) - two aligned blocks.
The extractor's twenty formula images were replaced.
As printed in the source (not conversion errors): '$F_{L,\hat{\gamma}(x)}$' with the argument inside the subscript in (S17), (S19), (S20) and in the sentence after (S20), but '$F_{L,\hat{\gamma}}(\Delta\lambda)$' later;
an italic 'Pr' (typed as letters) in (S17)-(S21), (S23), (S25) and in '$Pr(X\le\Delta\lambda)$', upright Pr elsewhere; 'the $\sqrt{1-\gamma}$-quantile of $F_{L,\gamma}$' (subscript gamma without hat) after (S21);
plain conditional bars; the surplus closing parenthesis in (S29) and in both statements of (S30) ('$-d_j(x))\big)$', '$\bar{m}_{j,\mathcal{V}})\big)$'); the outer absolute-value bars of the mean-value display set as plain
bars; '$r_{bound}$' with an italic subscript; the denominator $\operatorname{Area}(\mathcal{B}_0)$ (not the surface) in (S32); 'being to sample points'; 'Let us have a look on Eq. (S19)'; 'less or equal to';
'As $r_x$ defined like in Eq. (S15)'; case (b) stated with a non-strict inequality; (S14) defines $\Delta\lambda_{\mathcal{V}}$ while (S26)-(S28) use $\Delta\lambda_{x,\mathcal{V}}$.
Line-wrap hyphen removed (de-fined). No floats, no page number or running head. The page ends with display (S37); the proof of Theorem 2 continues on page 13 with a new sentence.
"""
write(12, items, notes)
