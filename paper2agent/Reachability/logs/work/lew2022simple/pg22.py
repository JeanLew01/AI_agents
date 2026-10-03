from pt import *
items = [
 HDR(),
 H(r"### B.3. Proof of Corollary 1", [90, 93, 210, 105]),
 T(r"""We start with the following preliminary result:""", [90, 113, 523, 125]),
 T(r"""**Lemma 6** Assume that $\mathcal{X}^{\mathsf{c}}$ is $r$-convex (Assumption 4). Define $\boldsymbol{r}=(r,0,\dots,0)\in\mathbb{R}^p$. Then, for any $\epsilon\geq 0$,""", [90, 135, 523, 160]),
 T(r"""$$
\inf_{x\in\partial\mathcal{X}}\lambda(\mathcal{X} \cap B(x,\epsilon)) \geq \lambda\big( B(0,\epsilon) \cap B(\boldsymbol{r},r) \big).
$$""", [200, 162, 412, 181]),
 T(r"""**Proof of Lemma 6.** By Assumption 4, $\mathcal{X}^{\mathsf{c}}$ is $r$-convex. Thus, for any $x\in\partial\mathcal{X}$, there exists some $\tilde{x}\in\mathrm{Int}(\mathcal{X})$ and a (closed) ball $B(\tilde{x},r)$ such that $x\in B(\tilde{x},r)$ and $B(\tilde{x},r)\subseteq\mathcal{X}$. Since $x\in\partial\mathcal{X}$ and $B(\tilde{x},r)\subseteq\mathcal{X}$, $\|x-\tilde{x}\|=r$.""", [90, 189, 523, 227]),
 T(r"""Let $\epsilon\geq 0$ and $\boldsymbol{r}=(r,0,\dots,0)\in\mathbb{R}^p$. Then, by translational and rotational invariance of the Lebesgue measure,""", [90, 230, 523, 255]),
 T(r"""$$
\lambda(\mathcal{X} \cap B(x,\epsilon)) \geq \lambda\big( B(\tilde{x},r) \cap B(x,\epsilon) \big) = \lambda\big( B(x-\tilde{x},r) \cap B(0,\epsilon) \big) = \lambda\big( B(\boldsymbol{r},r) \cap B(0,\epsilon) \big)
$$""", [96, 262, 515, 281]),
 T(r"""As this holds for $x\in\partial\mathcal{X}$, we obtain that $\inf_{x\in\partial\mathcal{X}}\lambda(\mathcal{X} \cap B(x,\epsilon)) \geq \lambda\big( B(0,\epsilon) \cap B(\boldsymbol{r},r) \big)$. $\blacksquare$""", [90, 286, 523, 306]),
 T(r"""Then, we restate Corollary 1 and prove it below.""", [106, 315, 523, 327]),
 T(r"""**Corollary 1** Define the estimator $\hat{\mathcal{Y}}^M=\mathrm{H}\left(\{y_i\}_{i=1}^M\right)$, the offset vector $\boldsymbol{r}=(r,0,\dots,0)\in\mathbb{R}^p$, the volume $\Lambda_{\epsilon}^{r,L}=\lambda\big( B(0,\epsilon/(2L)) \cap B(\boldsymbol{r},r) \big)$, and the threshold $\delta_M= D(\partial\mathcal{X},\epsilon/(2L))\big(1 - p_0 \Lambda_{\epsilon}^{r,L} \big)^M$. Then, under Assumptions 2, 4 and 5 and assuming that $\partial\mathcal{Y}\subseteq f(\partial\mathcal{X})$,""", [90, 334, 523, 377]),
 T(r"""$$
\mathbb{P}( d_H( \hat{\mathcal{Y}}^M, \mathrm{H}(\mathcal{Y}) )\leq \epsilon )\geq 1-\delta_M, \qquad \text{ and }\qquad\ \mathbb{P}(\mathcal{Y}\subseteq\hat{\mathcal{Y}}_\epsilon^M)\geq 1-\delta_M.
$$""", [140, 384, 472, 401]),
 T(r"""**Proof of Corollary 1.** We prove that Assumptions 4 and 5 imply Assumption 3 with $\Lambda_{\epsilon}^{L}=p_0\Lambda_{\epsilon}^{r,L}$, where $\Lambda_{\epsilon}^{r,L}=\lambda\big( B(0,\epsilon/(2L)) \cap B(\boldsymbol{r},r) \big)$. The result then follows by applying Theorem 2.""", [90, 422, 523, 448]),
 T(r"""Specifically, we must prove that $\mathbb{P}_\mathcal{X}(B(x,\epsilon/(2L)))\geq \Lambda_{\epsilon}^{L}$ for all $x\in\partial\mathcal{X}$.""", [106, 449, 523, 461]),
 T(r"""From Assumption 5, $\mathbb{P}_\mathcal{X}(A)\geq p_0\lambda(A)$ for all $A\in\mathcal{B}(\mathcal{X})$ for some constant $p_0>0$.""", [106, 463, 523, 475]),
 T(r"""Since $\mathbb{P}_\mathcal{X}(\mathcal{X})=1$ (Assumption 5), $\mathbb{P}_\mathcal{X}(B(x,\epsilon/(2L))) = \mathbb{P}_\mathcal{X}(\mathcal{X}\cap B(x,\epsilon/(2L)))$ for any $x\in\mathbb{R}^n$.""", [90, 476, 523, 501]),
 T(r"""Therefore, for all $x\in\partial\mathcal{X}$, $\mathbb{P}_\mathcal{X}(B(x,\epsilon/(2L))) = \mathbb{P}_\mathcal{X}(\mathcal{X}\cap B(x,\epsilon/(2L))) \geq p_0 \lambda(\mathcal{X}\cap B(x,\epsilon/(2L)))$.""", [106, 503, 540, 515]),
 T(r"""From Assumption 4 and Lemma 6, we obtain $\mathbb{P}_\mathcal{X}(B(x,\epsilon/(2L))) \geq p_0 \lambda\big( B(0,\epsilon/(2L)) \cap B(\boldsymbol{r},r) \big)$ for all $x\in\partial\mathcal{X}$ with $\boldsymbol{r}=(r,0,\dots,0)\in\mathbb{R}^p$. This concludes the proof of Corollary 1. $\blacksquare$""", [90, 517, 526, 542]),
 H(r"## Appendix C. Volume of the intersection of two hyperspheres", [90, 571, 400, 584]),
 T(r"""For completeness, we describe the computation of the constant $\Lambda_{\epsilon}^{r,L}=\lambda\big( B(0,\epsilon/(2L)) \cap B(\boldsymbol{r},r) \big)$ in Theorem 2 based on the results in (Li, 2011; Petitjean, 2013; Matt, 2013). Given $r>0$, $a\in\mathbb{R}$, and the incomplete beta function $I_x(a,b)=\Gamma(a+b)(\Gamma(a)\Gamma(b))^{-1}\int_0^x t^{a-1}(1-t)^{b-1}\mathrm{d}t$, we define""", [90, 592, 523, 632]),
 T(r"""$$
V(r,a)=\begin{cases}
\frac{\pi^{p/2}}{2\Gamma(\frac{p}{2}+1)}r^n I_{1-a^2/r^2}\left(\frac{n+1}{2},\frac{1}{2}\right)\ &\text{if }a\geq 0, \\
\frac{\pi^{p/2}}{2\Gamma(\frac{p}{2}+1)}r^n(2-I_{1-a^2/r^2}\left(\frac{n+1}{2},\frac{1}{2}\right)) \ &\text{otherwise.}
\end{cases}
$$""", [170, 640, 442, 682]),
 T(r"""Let $c_1=\frac{(\epsilon/(2L))^2}{2r}$ and $c_1=\frac{2r^2-(\epsilon/(2L))^2}{2r}$. Then, $\Lambda_{\epsilon}^{r,L} = V(\epsilon/(2L),c_1) + V(r,c_2)$.""", [90, 688, 523, 709]),
 PNUM(22),
]
page(22, items, r"""Appendix B.3 (Lemma 6, its proof, restated Corollary 1 and its proof) and Appendix C. Text and mathematics taken from the authors' TeX (main.tex lines 2241-2576), macros expanded, and compared with the 150-dpi render and three 230-260-dpi crops covering the whole page. TeX/PDF difference resolved in favour of the PDF: the source writes the offset vector as \vec{r}; the PDF prints a bold r without arrow (jmlr class), transcribed \boldsymbol{r} throughout (ten occurrences on this page). Checked symbol by symbol: Lemma 6: inf_{x in dX} lambda(X cap B(x,eps)) >= lambda(B(0,eps) cap B(r,r)) for any eps >= 0, with r = (r,0,...,0) in R^p; proof: \tilde x in Int(X), closed ball B(\tilde x, r), ||x - \tilde x|| = r, chain lambda(X cap B(x,eps)) >= lambda(B(\tilde x,r) cap B(x,eps)) = lambda(B(x - \tilde x, r) cap B(0,eps)) = lambda(B(r,r) cap B(0,eps)) (printed without final punctuation). Restated Corollary 1 (bold label without period, italic body): Lambda_eps^{r,L} = lambda(B(0,eps/(2L)) cap B(r,r)), delta_M = D(dX, eps/(2L)) (1 - p_0 Lambda_eps^{r,L})^M, 'under Assumptions 2, 4 and 5 and assuming that dY subseteq f(dX)', two separate probability bounds >= 1 - delta_M (with a comma after the first, as printed). Proof of Corollary 1: Lambda_eps^L = p_0 Lambda_eps^{r,L}; P_X(A) >= p_0 lambda(A) for all A in B(X); P_X(B(x,eps/(2L))) = P_X(X cap B(x,eps/(2L))) >= p_0 lambda(X cap B(x,eps/(2L))) >= p_0 lambda(B(0,eps/(2L)) cap B(r,r)). Appendix C: incomplete beta function I_x(a,b) = Gamma(a+b) (Gamma(a) Gamma(b))^{-1} int_0^x t^{a-1} (1-t)^{b-1} dt; V(r,a) as a two-case formula with prefactor pi^{p/2} / (2 Gamma(p/2 + 1)) r^n and I_{1-a^2/r^2}((n+1)/2, 1/2), second case r^n (2 - I_{...}(...)); c_1 = (eps/(2L))^2 / (2r); Lambda_eps^{r,L} = V(eps/(2L), c_1) + V(r, c_2). Printed slips kept verbatim (same in TeX): both constants are introduced as 'c_1' ('Let c_1 = ... and c_1 = (2r^2 - (eps/(2L))^2)/(2r)') although the last formula uses c_2; the V(r,a) formula mixes the dimensions p (in pi^{p/2}, Gamma(p/2+1)) and n (in r^n, (n+1)/2); 'x in R^n' in the proof of Corollary 1 although inputs live in R^p; 'in Theorem 2' in Appendix C although the constant appears in Corollary 1. All displays were extractor formula images or glyph soup and are now LaTeX; none has a printed number. Proof labels printed bold with period ('Proof of Lemma 6.', 'Proof of Corollary 1.'); end-of-proof squares written $\blacksquare$. Headings fixed to '### B.3. Proof of Corollary 1' and '## Appendix C. Volume of the intersection of two hyperspheres'. Running header and page number 22 omitted.""")
