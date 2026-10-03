from pt import *
items = [
 HDR(),
 T(r"""Given the right choice of $G_\delta^1,G_\delta^2$, by convexity of $\mathrm{H}(\mathcal{Y})$ $^{7}$ (see also Figure 7), we have that""", [90, 93, 523, 105]),
 T(r"""$$
\mathbb{P}\left(\bigcup_{M=M_\epsilon}^\infty \hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq\emptyset\right)\geq \mathbb{P}\left( \bigcup_{M=M_\epsilon}^\infty (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G_\partial^1\neq\emptyset) \cap (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G_\partial^2\neq\emptyset) \right) =1.
$$""", [118, 113, 495, 152]),
 T(r"""Therefore, $\mathbb{P}\left(\bigcup_{M=M_\epsilon}^\infty \hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq\emptyset\right)=1$. Combining this result with (7), we obtain that $\mathbb{P}(\hat{\mathcal{Y}}^M_{\epsilon_M}\cap G = \emptyset \ i.o.) = 0$. This conludes the proof of (C2).""", [90, 160, 523, 192]),
 T(r"""By Theorem 3, we conclude that almost surely, the sequence $\{\hat{\mathcal{Y}}^M_{\epsilon_M}(\omega),m\geq 1\}$ converges to $\mathrm{H}(\mathcal{Y})\oplus B(0,\bar{\epsilon})$ as $M\rightarrow\infty$. This concludes the proof of Theorem 1. $\blacksquare$""", [90, 201, 523, 226]),
 T(r"""Footnote 7: $\mathrm{H}(\mathcal{Y})\oplus B(0,\bar\epsilon)$ is convex, so that any $y\in G\cap (\mathrm{H}(\mathcal{Y})\oplus B(0,\bar\epsilon))\neq\emptyset$ lies on a line passing through two extreme points $z_1^y,z_2^y$ of $\mathrm{H}(\mathcal{Y})\oplus B(0,\bar\epsilon)$. For some $\tilde\epsilon>0$, let $G_\partial^1=\mathring{B}_\partial^1(z_1^y,\tilde\epsilon)$ and $G_\partial^2=\mathring{B}_\partial^2(z_2^y,\tilde\epsilon)$ (note that $G_\partial^1,G_\partial^2$ intersect $\mathrm{H}(\mathcal{Y})\oplus B(0,\bar\epsilon)$). Then, by choosing $\tilde\epsilon$ small enough, since $\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}$ is convex, the inequality follows since $\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}$ necessarily intersects $G$ if it intersects $G_\partial^1$ and $G_\partial^2$.""", [95, 661, 523, 706]),
 H(r"### B.2. Proof of Theorem 2", [90, 253, 205, 265]),
 T(r"""We start with four intermediate results and then prove Theorem 2. We use the notations introduced in Section A throughout this section.""", [90, 272, 523, 298]),
 T(r"""**Lemma 2** Under Assumption 2 and assuming that $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$,""", [90, 310, 523, 322]),
 T(r"""$$
D(\partial\mathcal{Y},\epsilon)\leq D(\partial\mathcal{X},\epsilon/L).
$$""", [245, 332, 368, 347]),
 T(r"""**Lemma 3** Under Assumption 2, for any $x\in\mathbb{R}^p$, $y=f(x)$, and any $\delta>0$,""", [90, 358, 523, 370]),
 T(r"""$$
\mathbb{P}_\mathcal{Y}\big(B(y,\delta)\big) \geq \mathbb{P}_\mathcal{X}\big(B(x,\epsilon)\big) \quad \text{for all }\ \epsilon\in [0,\delta/L].
$$""", [190, 380, 423, 396]),
 T(r"""**Lemma 4** Let $\epsilon>0$ and define""", [90, 407, 523, 419]),
 T(r"""$$
Y_\epsilon^M = \bigcup_{i=1}^{M} \, B(y_i,\epsilon), \qquad \pi(\partial\mathcal{Y},Y_\epsilon^M) = \sup_{y\in\partial\mathcal{Y}}\mathbb{P}(\{y\} \cap Y_\epsilon^M = \emptyset).
$$""", [160, 429, 452, 466]),
 T(r"""Then,""", [90, 473, 523, 484]),
 T(r"""$$
\mathbb{P}(\partial\mathcal{Y}\subset Y_{2\epsilon}^M) \geq 1 - D(\partial\mathcal{Y},\epsilon) \pi(\partial\mathcal{Y},Y_\epsilon^M).
$$""", [205, 485, 406, 500]),
 T(r"""**Lemma 5** Let $\epsilon\geq 0$ and let $Y\in\mathcal{K}$ be such that $\partial\mathcal{Y}\subseteq Y\oplus B(0,\epsilon)$ and $Y\subseteq \mathcal{Y}$. Then, $d_H( \mathrm{H}(Y), \mathrm{H}(\mathcal{Y}) )\leq \epsilon$.""", [90, 510, 523, 537]),
 T(r"""Lemma 4 is the key to deriving Theorem 2. It is first derived in (Dumbgen and Walther, 1996) in the convex problem setting. Notably, Lemma 4 does not require the convexity of $\mathcal{Y}$.""", [90, 549, 523, 575]),
 T(r"""**Proof of Lemma 2.** First, note that since $\mathcal{X}$ is compact and $\partial\mathcal{X}\subseteq\mathcal{X}$, $\partial\mathcal{X}$ is compact (note that the boundary is always closed). Any compact set has a finite covering number, thus $D(\partial\mathcal{X}, \epsilon)$ is finite for any finite $\epsilon>0$. Second, given any $\delta>0$, any $x\in\mathcal{X}$, and $y=f(x)$,""", [90, 590, 523, 629]),
 T(r"""$$
f(B(x,\epsilon)) \subseteq B(y,\delta) \quad \forall \epsilon\in[0,\delta/L], \tag{8}
$$""", [220, 639, 523, 654]),
 PNUM(19),
]
page(19, items, r"""End of the proof of Theorem 1 (step C2.3), then Appendix B.2 with Lemmas 2-5 and the start of the proof of Lemma 2. Text and mathematics taken from the authors' TeX (main.tex lines 1758-1885), macros expanded, and compared with the 150-dpi render and three 230-250-dpi crops (top block, lemma block, bottom block with footnote 7). The page starts a new sentence ('Given the right choice ...'), no join. Lemma numbering is as printed: Lemma 2, 3, 4, 5 (there is no Lemma 1 in this version; the TeX source uses automatic numbering). Labels are bold without a period ('**Lemma 2**'), bodies italic in print; each lemma ends where its TeX environment ends (Lemma 2 and 3 with their display, Lemma 4 with the second display, Lemma 5 with '<= eps.'). Checked symbol by symbol: Lemma 2: D(dY, eps) <= D(dX, eps/L) under Assumption 2 and dY subseteq f(dX); Lemma 3: P_Y(B(y,delta)) >= P_X(B(x,eps)) for all eps in [0, delta/L], for any x in R^p, y = f(x), delta > 0; Lemma 4: Y_eps^M = cup_{i=1}^M B(y_i, eps), pi(dY, Y_eps^M) = sup_{y in dY} P({y} cap Y_eps^M = empty), then P(dY subset Y_{2eps}^M) >= 1 - D(dY, eps) pi(dY, Y_eps^M); Lemma 5: eps >= 0, Y in K (roman Y, a deterministic compact set, distinct from calligraphic Y), dY subseteq Y (+) B(0,eps) and Y subseteq calligraphic Y imply d_H(H(Y), H(calY)) <= eps. Eq. (8) f(B(x,eps)) subseteq B(y,delta) for all eps in [0, delta/L], printed tag (8), ends with a comma and the sentence continues on page 20 ('where L is ...'). All displays were extractor formula images or glyph soup and are now LaTeX. Printed slips kept verbatim (same in TeX): 'G^1_delta, G^2_delta' with delta subscripts in the first line (elsewhere a partial-derivative subscript), '{..., m >= 1}' with lower-case m, 'conludes'. The proof label is printed 'Proof of Lemma 2.' in bold with a period and is written '**Proof of Lemma 2.**'; the end-of-proof square of Theorem 1's proof is written $\blacksquare$. Footnote 7 (mark after 'H(Y)' in the first line) is printed at the bottom of the page below Eq. (8), whose sentence continues on page 20; to keep that sentence unbroken the footnote item is placed at the end of Section B.1 (after the last line of the proof of Theorem 1, before the B.2 heading). Heading fixed to '### B.2. Proof of Theorem 2'. Running header and page number 19 omitted.""")
