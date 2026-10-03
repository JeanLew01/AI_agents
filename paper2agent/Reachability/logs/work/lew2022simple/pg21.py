from pt import *
items = [
 HDR(),
 T(r"""**Remark:** the assumption $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$ holds if the reachability map $f$ is open, e.g., if it is a submersion (its differential is surjective). If $\partial\mathcal{Y}\nsubseteq f(\partial\mathcal{X})$, then one could modify Theorem 2 by replacing Assumption 3 with "*Given $\epsilon,L>0$, there exists $\Lambda_{\epsilon}^{L}>0$ such that $\mathbb{P}_\mathcal{X}\left(B\left(x,\frac{\epsilon}{2L}\right)\right)\geq \Lambda_{\epsilon}^{L}$ for all $x\in\mathcal{X}$*" (i.e., one should sample over the entire set $\mathcal{X}$ and not only along the boundary) and by defining $\delta_M=D(\mathcal{X},\epsilon/(2L))(1 - \Lambda_{\epsilon}^{L})^M$.""", [90, 93, 523, 159]),
 T(r"""**Proof** As in Lemma 4, define $Y_\epsilon^M = \bigcup_{i=1}^M B(y_i,\epsilon)$, $Y^M=\{y_i\}_{i=1}^M$, and""", [90, 173, 523, 188]),
 T(r"""$$
\pi(\partial\mathcal{Y},Y_\epsilon^M) = \sup_{y\in\partial\mathcal{Y}}\mathbb{P}(\{y\} \cap Y_\epsilon^M = \emptyset) = \sup_{y\in\partial\mathcal{Y}}\mathbb{P}(B(y,\epsilon) \cap Y^M = \emptyset),
$$""", [150, 190, 462, 217]),
 T(r"""which corresponds to the worst probability over $y\in\partial\mathcal{Y}$ of not sampling some $y_i$ that is $\epsilon$-close to $y$. First, we derive a bound for $\pi(\partial\mathcal{Y},Y_\epsilon^M)$. Using the fact that the samples $y_i$ are i.i.d.,""", [90, 222, 523, 249]),
 T(r"""$$
\begin{aligned}
\pi(\partial\mathcal{Y},Y_\epsilon^M) &= \sup_{y\in\partial\mathcal{Y}}\mathbb{P}(B(y,\epsilon) \cap Y^M = \emptyset) \\
&= \sup_{y\in\partial\mathcal{Y}}\mathbb{P}\left(\bigcap_{i=1}^M (y_i\notin B(y,\epsilon))\right) \\
&= \left(1 - \inf_{y\in\partial\mathcal{Y}}\mathbb{P}(y_i\in B(y,\epsilon)) \right)^M \\
&=\left(1 - \inf_{y\in\partial\mathcal{Y}}\mathbb{P}_\mathcal{Y}(B(y,\epsilon)) \right)^M.
\end{aligned}
$$""", [200, 253, 412, 383]),
 T(r"""From Lemma 3, for any $x\in\mathbb{R}^p$, $y=f(x)$, and $\epsilon>0$, $\mathbb{P}_\mathcal{Y}(B(y,\epsilon)) \geq \mathbb{P}_\mathcal{X}(B(x,\epsilon/L))$. Since for all $y\in\partial\mathcal{Y}$, there exists $x\in\partial\mathcal{X}$ such that $y=f(x)$, we combine the two previous results to obtain""", [90, 388, 523, 414]),
 T(r"""$$
\pi(\partial\mathcal{Y},Y_\epsilon^M) \leq \left(1 - \inf_{x\in\partial\mathcal{X}}\mathbb{P}_\mathcal{X}(B(x,\epsilon/L)) \right)^M.
$$""", [198, 420, 412, 455]),
 T(r"""In particular, using Assumption 3,""", [90, 458, 523, 470]),
 T(r"""$$
\pi(\partial\mathcal{Y},Y_{\epsilon/2}^M) \leq \left(1 - \inf_{x\in\partial\mathcal{X}}\mathbb{P}_\mathcal{X}(B(x,\epsilon/(2L))) \right)^M \leq \left(1 - \Lambda_{\epsilon}^{L} \right)^M.
$$""", [158, 474, 452, 510]),
 T(r"""To complete the proof of Theorem 2, we use Lemma 4 which states that""", [90, 512, 523, 525]),
 T(r"""$$
\mathbb{P}(\partial\mathcal{Y}\subseteq Y_\epsilon^M) \geq 1 - D(\partial\mathcal{Y},\epsilon/2) \pi(\partial\mathcal{Y},Y_{\epsilon/2}^M) .
$$""", [200, 530, 410, 549]),
 T(r"""Using Lemma 2, $D(\partial\mathcal{Y},\epsilon/2)\leq D(\partial\mathcal{X},\epsilon/(2L))$.""", [90, 554, 523, 566]),
 T(r"""By Lemma 5, if $\partial\mathcal{Y}\subseteq Y_\epsilon^M$ and $Y^M\subseteq\mathcal{Y}$ $^{8}$, then $d_H( \mathrm{H}(Y^M), \mathrm{H}(\mathcal{Y}) )\leq \epsilon$ .""", [90, 567, 523, 580]),
 T(r"""Therefore, with $\hat{\mathcal{Y}}^M=\mathrm{H}(Y^M)$ and Assumption 3, combining the last inequalities,""", [90, 581, 523, 594]),
 T(r"""$$
\begin{aligned}
\mathbb{P}( d_H( \hat{\mathcal{Y}}^M, \mathrm{H}(\mathcal{Y}) )\leq \epsilon ) &\geq \mathbb{P}\left(\partial\mathcal{Y}\subseteq Y_\epsilon^M\right) \\
&\geq 1 - D(\partial\mathcal{Y},\epsilon/2) \pi(\partial\mathcal{Y},Y_{\epsilon/2}^M) \\
&\geq 1 - D(\partial\mathcal{X},\epsilon/(2L)) \left(1 - \Lambda_{\epsilon}^{L} \right)^M.
\end{aligned}
$$""", [170, 599, 440, 657]),
 T(r"""If $d_H( \hat{\mathcal{Y}}^M, \mathrm{H}(\mathcal{Y}) )\leq \epsilon$, then $\mathcal{Y}\subseteq\mathrm{H}(\mathcal{Y})\subseteq \hat{\mathcal{Y}}^M\oplus B(0,\epsilon)=\hat{\mathcal{Y}}_\epsilon^M$. The conclusion follows. $\blacksquare$""", [90, 663, 523, 678]),
 T(r"""Footnote 8: Since $\mathbb{P}_\mathcal{X}(\mathcal{X})=1$, we have that $\mathbb{P}_\mathcal{Y}(\mathcal{Y})=1$, so that $Y^M\subseteq\mathcal{Y}$ with probability one.""", [95, 693, 523, 706]),
 PNUM(21),
]
page(21, items, r"""Remark on the assumption dY subseteq f(dX) and the proof of Theorem 2. Text and mathematics taken from the authors' TeX (main.tex lines 2095-2237), macros expanded, and compared with the 150-dpi render and three 230-dpi crops covering the whole page. The Remark is printed with a bold 'Remark:' (colon, lower-case continuation) directly after the restated Theorem 2 of page 20; it is not part of the theorem environment. Checked: f open / submersion; the modified Assumption 3 in italics inside double quotes with 'for all x in X' (whole set, not the boundary) and delta_M = D(X, eps/(2L)) (1 - Lambda_eps^L)^M. Proof (bold 'Proof', no period): Y_eps^M = cup_{i=1}^M B(y_i, eps), Y^M = {y_i}_{i=1}^M; pi(dY, Y_eps^M) = sup P({y} cap Y_eps^M = empty) = sup P(B(y,eps) cap Y^M = empty); four-line identity ending (1 - inf_{y in dY} P_Y(B(y,eps)))^M; pi(dY, Y_eps^M) <= (1 - inf_{x in dX} P_X(B(x, eps/L)))^M; pi(dY, Y_{eps/2}^M) <= (1 - inf_{x in dX} P_X(B(x, eps/(2L))))^M <= (1 - Lambda_eps^L)^M; P(dY subseteq Y_eps^M) >= 1 - D(dY, eps/2) pi(dY, Y_{eps/2}^M); D(dY, eps/2) <= D(dX, eps/(2L)); final three-line chain P(d_H(\hat Y^M, H(Y)) <= eps) >= P(dY subseteq Y_eps^M) >= 1 - D(dY, eps/2) pi(dY, Y_{eps/2}^M) >= 1 - D(dX, eps/(2L)) (1 - Lambda_eps^L)^M; last line Y subseteq H(Y) subseteq \hat Y^M (+) B(0,eps) = \hat Y_eps^M. All eight displays were extractor formula images or glyph soup and are now LaTeX; none has a printed number. Roman Y^M / Y_eps^M (sample set and union of balls) are distinct from the calligraphic sets. Footnote mark 8 after 'Y^M subseteq calY' written '$^{8}$'; footnote 8 kept as its own item at the bottom of the page ('Footnote 8:' prefix added). A stray space before the period in '<= eps .' is as printed. End-of-proof square written $\blacksquare$. Running header and page number 21 omitted.""")
