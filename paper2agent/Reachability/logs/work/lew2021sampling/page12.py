from pg import *
items=[
T('p0012-b000',[108,74,313,85],r'''From this result and $\cap_{n=1}^\infty A_n \subseteq A_1$, we obtain that'''),
T('p0012-b001',[163,88,510,126],r'''$$\mathbb{P} (\boldsymbol{x}^j\in G \ \ i.o.) \leq \mathbb{P}\bigg(\bigcup_{m=1}^\infty\boldsymbol{x}^m\in G\bigg) \implies \mathbb{P}\bigg(\bigcup_{m=1}^\infty\boldsymbol{x}^m\in G\bigg) = 1. \tag{6}$$'''),
T('p0012-b002',[108,134,266,144],'(2) Second, we rewrite (**C2**) as follows:'),
T('p0012-b003',[122,147,490,185],r'''$$\mathbb{P}(\mathcal{X}^m\cap G = \emptyset \ \ i.o.) = \mathbb{P}\bigg(\bigcap_{n=1}^\infty\bigcup_{m=n}^\infty \mathcal{X}^m\cap G = \emptyset\bigg) = 1 - \mathbb{P}\bigg(\bigcup_{n=1}^\infty\bigcap_{m=n}^\infty \mathcal{X}^m\cap G \neq \emptyset\bigg).$$'''),
T('p0012-b004',[108,188,478,200],r'''Since $\mathcal{X}^m\subseteq\mathcal{X}^{m+1}, \forall m$, we have that $\{\omega \, |\, \bigcap_{m=n}^\infty \mathcal{X}^m\cap G \neq \emptyset\}=\{\omega \, |\, \mathcal{X}^n\cap G \neq \emptyset\}$, and'''),
T('p0012-b005',[190,203,430,240],r'''$$\mathbb{P}\bigg(\bigcup_{n=1}^\infty\bigcap_{m=n}^\infty \mathcal{X}^m\cap G \neq \emptyset\bigg)=\mathbb{P}\bigg(\bigcup_{n=1}^\infty\mathcal{X}^n\cap G \neq \emptyset\bigg).$$'''),
T('p0012-n01',[108,250,160,262],'Therefore,'),
T('p0012-n02',[190,241,510,272],r'''$$\mathbb{P}(\mathcal{X}^m\cap G = \emptyset \ \ i.o.) = 0 \iff \mathbb{P}\bigg(\bigcup_{n=1}^\infty\mathcal{X}^n\cap G \neq \emptyset\bigg) = 1. \tag{7}$$'''),
T('p0012-b006',[108,272,504,295],r'''(3) Finally, we combine the two results from above. First, we note that since $\boldsymbol{x}^j\in\mathcal{X}^j$, we have $\{\omega \,|\, \boldsymbol{x}^j(\omega) \in G\} \subseteq \{\omega \,|\, \mathcal{X}^j(\omega) \cap G \neq \emptyset\}$. Hence, we obtain'''),
T('p0012-b007',[201,296,430,328],r'''$$\bigcup_{j=1}^\infty\{\omega \,|\, \boldsymbol{x}^j(\omega) \in G\} \subseteq \bigcup_{j=1}^\infty\{\omega \,|\, \mathcal{X}^j(\omega) \cap G \neq \emptyset\}.$$'''),
T('p0012-b008',[108,334,234,344],'Combining with (6), we obtain:'),
T('p0012-n03',[250,328,510,358],r'''$$\mathbb{P}\bigg(\bigcup_{n=1}^\infty\mathcal{X}^n\cap G \neq \emptyset\bigg) = 1. \tag{8}$$'''),
T('p0012-b009',[108,361,473,372],r'''Using (7), (8) is equivalent to $\mathbb{P}(\mathcal{X}^m\cap G = \emptyset \ \ i.o.) = 0$, which conludes the proof of (**C2**).'''),
T('p0012-b010',[108,378,504,410],r'''By Theorem 1, we conclude that the sequence $\{\mathcal{X}^m(\omega),m\geq 1\}$ almost surely converges to the deterministic set $\mathcal{X}$ as $m\rightarrow\infty$. As $\mathcal{X}$ is defined as the convex hull of the true reachable set $\mathrm{Co}(\mathcal{X}_k)$, this concludes our proof of Theorem 2. $\square$'''),
O('p0012-b011',[296,740,316,753],'Page number "12" in the footer.'),
]
save(12, items, 'Compared with a 130 dpi render, a 240 dpi zoom of the whole text block and the TeX source. The four extractor formula images are replaced by six LaTeX display items: equation (6), the unnumbered rewriting of (C2), the unnumbered identity after "and", equation (7), the unnumbered inclusion of unions, and equation (8); only the printed tags (6), (7), (8) are used. Each display was checked on the zoom for the order of big cup/cap, their limits (n=1, m=n, m=1, j=1), = versus the not-equal sign next to the empty set, and the final periods. "Therefore," is printed on the same line as equation (7) and "Combining with (6), we obtain:" on the same line as equation (8); they are given as short text items immediately before the respective display. The end-of-proof box is written as $\\square$. Authors\' spelling "conludes" kept. The rest of the page is blank.')
