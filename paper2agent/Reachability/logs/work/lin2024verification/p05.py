from pagelib import *

items = [
    header(5),
    text("p0005-b001", [89.0, 94.0, 523.0, 145.0],
         r"discarding approach to chance-constrained optimization problems, which quantifies the trade-off between feasibility and performance of the optimal solution based on finite samples (Campi and Garatti, 2011). First, we explain the method when $\mathcal{L}$ represents undesirable states. In the end, we comment on when $\mathcal{L}$ represents desirable states.",
         join_previous="none"),
    text("p0005-b002", [89.0, 148.0, 523.0, 281.0],
         r"***Procedures:*** Let $\mathcal{S} \subseteq X$ be a neural safe set that is, in the avoid case, the *complement* of the neural reachable tube being verified. In our case, $\mathcal{S}$ is typically a super-$\delta$ level set of the learned value function $" + V + r"(x,0)$. Ideally, any super-$\delta$ level set of $" + V + r"(x,0)$ for $\delta > 0$ should be a valid safe set; however, due to learning errors, that might not be true in practice. To provide a probabilistic safety assurance for $\mathcal{S}$, we first sample $N$ independent and identically distributed (i.i.d.) states $x_{1:N}$ from $\mathcal{S}$ according to some probability distribution $\mathbb{P}$ over $\mathcal{S}$. Since $\mathcal{S}$ is defined implicitly by $" + V + r"(x,0)$, we use rejection sampling. We next compute the costs $" + J + r"(x_i,0)$ for $i=1, 2, ..., N$ by rolling out the system trajectory from $x_i$ under $" + PI + r"(x,t)$. Let $k$ refer to the number of “outliers” - samples that are empirically unsafe, i.e., $" + J + r"(x_i,0) \le 0$. Then the following theorem provides a probabilistic guarantee on the safety of the neural reachable tube and its complement, the neural safe set $\mathcal{S}$:"),
    text("p0005-b003", [90.0, 290.0, 522.0, 315.0],
         r"**Theorem 2 (Robust Scenario-Based Probabilistic Safety Verification)** Select a safety violation parameter $\epsilon \in (0, 1)$ and a confidence parameter $\beta \in (0, 1)$ such that"),
    text("p0005-b004", [240.0, 318.0, 528.0, 362.0], display(BINOM, 2)),
    text("p0005-b005", [90.0, 370.0, 508.0, 381.0],
         r"where $k$ and $N$ are as defined above. Then, with probability at least $1-\beta$, the following holds:"),
    text("p0005-b006", [251.0, 390.0, 528.0, 417.0],
         display(PS + r" \left( V(x,0) \le 0 \right) \le \epsilon", 3)),
    text("p0005-b007", [90.0, 426.0, 523.0, 545.0],
         r"All proofs can be found in the Appendix of the extended version of this article" + FN + r". Disregarding the confidence parameter $\beta$ for a moment, Theorem 2 states that the fraction of $\mathcal{S}$ that is unsafe is bounded above by the violation parameter $\epsilon$, where $\epsilon$ is computed empirically using Equation (2) based on the outlier rate $k$ encountered within $N$ samples. $\epsilon$ is thus a reflection of the safety quality of $\mathcal{S}$, which degrades with the increase in the number of outliers $k$, as expected. This can also be seen for the running example in Figure 1 (the red curve). Overall, Theorem 2 allows us to compute probabilistic safety guarantees for any neural set $\mathcal{S}$ based on a finite number of samples. Subsequently, this result can be used to find some $\mathcal{S}$ for which $\epsilon$ is smaller than a desired threshold, as we discuss later in this section."),
    text("p0005-b010", [95.0, 696.0, 509.0, 705.0],
         "Footnote 1: See `https://sia-lab-git.github.io/Verification_of_Neural_Reachable_Tubes.pdf`"),
    text("p0005-b008", [90.0, 550.0, 523.0, 629.0],
         r"To interpret $\beta$, note that $k$ is a random variable that depends on the randomly sampled $x_{1:N}$. It may be the case that we just happen to draw an unrepresentative sample, in which case the $\epsilon$ bound does not hold. $\beta$ controls the probability of this adverse event happening, which regards the correctness of the probabilistic safety guarantee in Equation (3). Fortunately, $\beta$ goes to $0$ exponentially with $N$, so $\beta$ can be chosen to be an extremely small value, such as $10^{-16}$, when we sample large $N$. $1-\beta$ will then be so close to $1$ that it does not have any practical importance."),
    text("p0005-b009", [90.0, 632.0, 523.0, 684.0],
         r"We have just explained the robust scenario-based probabilistic safety verification method in the case where $\mathcal{L}$ represents undesirable states. When the system instead wants to reach $\mathcal{L}$, $\mathcal{S}$ will be a sublevel set instead of a superlevel set of the learned value function. The cost inequality should be flipped when computing $k$, and the value inequality should be flipped in Equation (3)."),
    pageno(5, "p0005-b011", [303.0, 725.0, 309.0, 733.0]),
]

save(5, items, r"""
Compared the whole page with the 130 dpi render, with two 200 dpi crops covering the Procedures paragraph, Theorem 2 and
the text below it, and with sections/scenario-based_method.tex. The first item continues the hyphenated word
'sampling-and-discarding' from page 4 (join_previous 'none'). All mathematics was rewritten in LaTeX from the TeX source
(macros expanded) and checked symbol by symbol on the crops; TeX and PDF agree. The two extractor 'formula' images were
replaced by $$ blocks with the printed numbers \tag{2} (binomial-tail condition: sum from i=0 to k of binom(N,i)
eps^i (1-eps)^(N-i) <= beta) and \tag{3} (the guarantee P_{x in S}(V(x,0) <= 0) <= eps, with the true value function V
without tilde). 'Theorem 2 (Robust Scenario-Based Probabilistic Safety Verification)' is printed in bold without
punctuation after the label; the theorem body is printed in italics and ends with display (3) (end of the theorem
environment in the TeX source). 'Procedures:' is a run-in bold-italic label. Details checked on the crop: 'x_{1:N}',
'i = 1, 2, ..., N' (three plain dots), the quotation marks and the single hyphen in '“outliers” - samples', the outlier
condition J(x_i,0) <= 0, delta > 0, 10^{-16}. The sentence 'All proofs can be found in the Appendix of the extended
version of this article' with footnote mark 1 is printed as such although this arXiv version contains the appendix
(Appendices A and B); kept verbatim. The footnote mark is written as a separate ' $^{1}$'; footnote 1 is printed at the
foot of the page and was placed directly after the paragraph that carries the mark; its URL is set in code font to protect
the underscores. Cross-references (Theorem 2, Equation (2), Equation (3), Figure 1) are the printed numbers. Line-wrap
hyphens removed (cor-rectness); real hyphens kept (chance-constrained, trade-off, super-δ). Omitted: running header and
page number.
""")
