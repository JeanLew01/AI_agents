from pt import *
items = [
 T(r"As in the limit of $N\rightarrow \infty$ the probability of Eq. (S37) is 1, it follows that $\forall \gamma\in (0,1)\ \exists N \in\mathbb{N}\colon\Pr(\exists x\in\mathcal{V}\colon B(x,r_x)^S\owns x^\star_j)\ge\sqrt{1-\gamma}$.", L, 56, 89.2),
 T(r"Using a set of sampled points $\mathcal{V}$ with cardinality $N$ and using $\hat{\gamma} = 1-\sqrt{1-\gamma}$ as the error rate for the upper bound $\Delta\lambda_x$ of the confidence interval in Eq. (S14). Using the result of Theorem 1, the resulting probability $\forall y\in B(x,r_x)^S$ is:", L, 89.4, 133),
 T(r"$$\Pr\left(d_j(y) \le \mu\cdot \bar{m}_{j,\mathcal{V}}\right)\ge 1-\hat{\gamma} = \sqrt{1-\gamma} \tag{S38}$$", L, 139, 154),
 T(r"If there is an $x\in\mathcal{V}$ such that $B(x,r_x)^S\owns x_j^\star$, then Eq. (S38) obviously holds also for $x_j^\star$, thus:", L, 158, 184.5),
 T(r"$$\Pr( d_j(x^\star) \le \mu\cdot\bar{m}_{j,\mathcal{V}} |\exists x\in\mathcal{V}\colon B(x,r_x)^S\owns x^\star)\ge \sqrt{1-\gamma}$$", (54, 297), 189, 206),
 T(r"For any sets $A, B$ it holds that $\Pr(A)\ge \Pr(A\cap B) = \Pr(A | B) \cdot \Pr(B)$, and using:", L, 212, 233),
 T(r"$$A = (\mu\cdot\bar{m}_{j,\mathcal{V}}\ge m^\star_j) \tag{S39}$$" + "\n\n" + r"$$B = (\exists x\in\mathcal{V}\colon B(x,r_x)^S\owns x_j^\star) \tag{S40}$$", L, 239, 270),
 T(r"it follows that $\Pr(\mu\cdot\bar{m}_{j,\mathcal{V}}\ge m^\star_j)\ge \Pr(A|B) \cdot \Pr(B) = 1-\gamma$ and therefore Eq. (S31) holds.", L, 275.5, 298.5),
]
notes = r"""
Compared with a 250 dpi crop of the printed part of PDF page 13 (top third of the left column; a 60 dpi render of the whole page confirms that the rest of the page and the right column are blank) and with the
authors' TeX source (supplements.tex); mathematics taken from the TeX source (macro \calV -> \mathcal{V}; the tie in '(0,1)~\exists N' written as a backslash-space; '\colon\,' without the thin space;
\eqref numbers resolved) and checked symbol by symbol against the crop; TeX and PDF agree. This page is the end of the proof of the restated Theorem 2 and the end of the paper.
The first paragraph starts a new sentence after display (S37), which ends page 12, so no join is needed. Displays: (S38) numbered; the conditional-probability display after 'thus:' is unnumbered (align* in the
source) and is slightly wider than the column in print; (S39) and (S40) are two numbered lines of one aligned display (one item, one block per printed number). All three printed numbers are given with \tag.
The extractor's three formula images were replaced. No end-of-proof mark is printed after '... and therefore Eq. (S31) holds.'.
As printed in the source (not conversion errors): the star point is $x^\star_j$ in the first paragraph, (S39)/(S40) and the sentence before the unnumbered display, but $x^\star$ without index inside that display;
'the upper bound $\Delta\lambda_x$' (index $x$ only); the sentence 'Using a set of sampled points ... in Eq. (S14).' has no main clause; the final chain ends with '$= 1-\gamma$' (product of the two
$\sqrt{1-\gamma}$ bounds); plain conditional bars. No line-wrap hyphens on this page. Nothing omitted; no page number or running head.
"""
write(13, items, notes)
