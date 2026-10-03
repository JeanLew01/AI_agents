from pt import *
items = [
 HDR(),
 T(r"""some $\epsilon>0$ such that $\mathrm{H}(\mathcal{Y})\cap (G\oplus B(0,\bar{\epsilon}-\epsilon))\neq \emptyset$. $^{6}$""", [90, 93, 523, 105], join_previous="space"),
 T(r"""Since $\epsilon\rightarrow\bar{\epsilon}$ as $M\rightarrow\infty$, there exists some $M_\epsilon\in\mathbb{N}$ such that $\bar{\epsilon}-\epsilon<\epsilon_M<\bar{\epsilon}+\epsilon$ for all $M\geq M_\epsilon$.""", [90, 106, 523, 118]),
 T(r"""Second, we rewrite (C2) as""", [90, 119, 523, 131]),
 T(r"""$$
\mathbb{P}(\hat{\mathcal{Y}}^M_{\epsilon_M}\cap G = \emptyset \ \ i.o.) = \mathbb{P}\bigg(\bigcap_{N=1}^\infty\bigcup_{M=N}^\infty \hat{\mathcal{Y}}^M_{\epsilon_M}\cap G = \emptyset\bigg) = 1 - \mathbb{P}\bigg(\bigcup_{N=1}^\infty\bigcap_{M=N}^\infty \hat{\mathcal{Y}}^M_{\epsilon_M}\cap G \neq \emptyset\bigg).
$$""", [100, 139, 512, 177]),
 T(r"""Next, note that""", [90, 186, 523, 197]),
 T(r"""$$
\mathbb{P}\bigg(\bigcup_{N=1}^\infty\bigcap_{M=N}^\infty \hat{\mathcal{Y}}^M_{\epsilon_M}\cap G \neq \emptyset\bigg) \geq \mathbb{P}\bigg(\bigcup_{N=M_\epsilon}^\infty\bigcap_{M=N}^\infty \hat{\mathcal{Y}}^M_{\epsilon_M}\cap G\neq \emptyset\bigg) \geq \mathbb{P}\bigg( \bigcup_{N=M_\epsilon}^\infty \bigcap_{M=N}^\infty \hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq \emptyset\bigg).
$$""", [88, 205, 531, 243]),
 T(r"""The second inequality holds since $\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\subset \hat{\mathcal{Y}}^M_{\epsilon_M}$ if $M\geq M_\epsilon$.""", [90, 254, 523, 266]),
 T(r"""Next, since $\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\subseteq\hat{\mathcal{Y}}^{M+1}_{\bar{\epsilon}-\epsilon}$ for any $M\in\mathbb{N}$, we have that $\{\omega\in\Omega\, |\, \bigcap_{M=N}^\infty \hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq \emptyset\} = \{\omega\in\Omega \, |\, \hat{\mathcal{Y}}^N_{\bar{\epsilon}-\epsilon}\cap G \neq \emptyset\}$. Thus,""", [90, 267, 523, 296]),
 T(r"""$$
\mathbb{P}\bigg(\bigcup_{N=M_{\epsilon}}^\infty\bigcap_{M=N}^\infty \hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq \emptyset\bigg)=\mathbb{P}\bigg(\bigcup_{M=M_\epsilon}^\infty\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq \emptyset\bigg).
$$""", [165, 307, 445, 345]),
 T(r"""Combining the last three results, we obtain the following sufficient condition for (C2)""", [90, 354, 523, 366]),
 T(r"""$$
\mathbb{P}\bigg(\bigcup_{M=M_\epsilon}^\infty\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G \neq \emptyset\bigg) = 1 \implies \mathbb{P}(\hat{\mathcal{Y}}^M_{\epsilon_M}\cap G = \emptyset \ \ i.o.) = 0 . \tag{7}
$$""", [160, 374, 523, 411]),
 T(r"""(C2.3) Finally, we combine (6) and (7) as follows. For $M\geq 0$, we have that""", [90, 421, 523, 433]),
 T(r"""$$
\begin{aligned}
&\{ \omega\in\Omega: (y_{2M+1}(\omega)\in (G_\partial^1\oplus B(0,\bar{\epsilon}))) \cap (y_{2M+2}(\omega)\in (G_\partial^2\oplus B(0,\bar{\epsilon}))) \} \\
&\qquad\subseteq \{\omega\in\Omega \,|\, (\hat{\mathcal{Y}}^{2M+2}_{\bar{\epsilon}-\epsilon}(\omega)\cap (G_\partial^1\oplus B(0,\bar{\epsilon}))\neq\emptyset) \cap (\hat{\mathcal{Y}}^{2M+2}_{\bar{\epsilon}-\epsilon}(\omega)\cap (G_\partial^2\oplus B(0,\bar{\epsilon}))\neq\emptyset) \}
\end{aligned}
$$""", [100, 444, 515, 477]),
 T(r"""Thus,""", [90, 488, 523, 499]),
 T(r"""$$
\begin{aligned}
&\bigcup_{M=0}^\infty \{\omega\in\Omega: (y_{2M+1}(\omega)\in (G_\partial^1\oplus B(0,\bar{\epsilon})))\cap (y_{2M+2}(\omega)\in (G_\partial^2\oplus B(0,\bar{\epsilon})))\} \\
&\quad\subseteq \bigcup_{M=2}^\infty \{\omega\in\Omega \,|\, (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}(\omega)\cap G_\partial^1\neq\emptyset) \cap (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}(\omega)\cap G_\partial^2\neq\emptyset) \} \\
&\quad\subseteq \bigcup_{M=1}^\infty \{\omega\in\Omega \,|\, (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}(\omega)\cap G_\partial^1\neq\emptyset) \cap (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}(\omega)\cap G_\partial^2\neq\emptyset) \}.
\end{aligned}
$$""", [130, 508, 490, 619]),
 T(r"""From (6), the first event holds with probability one. Therefore, by the above,""", [90, 626, 523, 638]),
 T(r"""$$
\mathbb{P}\left( \bigcup_{M=M_\epsilon}^\infty (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G_\partial^1\neq\emptyset) \cap (\hat{\mathcal{Y}}^M_{\bar{\epsilon}-\epsilon}\cap G_\partial^2\neq\emptyset) \right)=1.
$$""", [185, 645, 430, 686]),
 T(r"""Footnote 6: More generally, given $A\subset\mathcal{K}$ and $B\subset\mathbb{R}^n$ an open set, then $A\cap B \neq\emptyset\implies A\cap(B\ominus B(0,\epsilon))\neq\emptyset$ for some $\epsilon>0$.""", [95, 693, 523, 706]),
 PNUM(18),
]
page(18, items, r"""Proof of Theorem 1, steps (C2.2) and (C2.3). Text and mathematics taken from the authors' TeX (main.tex lines 1639-1757), macros expanded, and compared with the 150-dpi render and three 230-dpi crops covering the whole page. First item completes the sentence begun on page 17 ('...there exists' / 'some eps > 0 such that ...'): join_previous=space; footnote mark 6 is printed after the period. Seven displays were extractor formula images or glyph-soup text and are now LaTeX; only Eq. (7) carries a printed number. Checked symbol by symbol on the crops: (i) P(\hat Y^M_{eps_M} cap G = empty i.o.) = P(cap_{N=1} cup_{M=N} ...) = 1 - P(cup_{N=1} cap_{M=N} ... != empty); (ii) the chain of two '>=' with lower limits N=1, N=M_eps, N=M_eps and subscripts eps_M, eps_M, \bar eps - eps; (iii) cup_{N=M_eps} cap_{M=N} = cup_{M=M_eps}; (iv) Eq. (7) with '==>' and 'i.o.'; (v) the two-line inclusion with superscript 2M+2 and subscript \bar eps - eps; (vi) the three-line chain with unions from M=0, M=2, M=1; (vii) the probability-one display with union from M=M_eps. Printed slips kept verbatim (same in TeX): 'Since eps -> \bar eps as M -> inf' (no subscript M on the first eps), union from M=M_eps in display (vii) although the preceding chain ends with a union from M=1, and in footnote 6 'A subset K' and the Minkowski difference symbol. '(C2.3)' is printed in normal weight. Lines starting 'Since eps ...', 'Second, we rewrite ...', 'Next, since ...' are forced line breaks in print and separate items here. Footnote 6 is kept as its own item at the bottom of the page ('Footnote 6:' prefix added); the next page starts a new sentence. Running header and page number 18 omitted.""")
