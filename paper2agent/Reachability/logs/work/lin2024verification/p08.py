from pagelib import *

items = [
    header(8),
    text("p0008-b001", [89.0, 94.0, 523.0, 159.0],
         r"Even though Theorem 3 provides the distribution of the safety level, when we compute safety assurances in practice, it is often desirable to know a lower-bound on the safety level with at least some desired confidence. This corresponds to choosing a lower-bound whose accumulated probability mass is smaller than some confidence parameter $\beta$ (shaded red in Figure 3). The following lemma formalizes this by using the CDF of the Beta distribution in Theorem 3."),
    text("p0008-b002", [89.0, 172.0, 523.0, 196.0],
         r"**Lemma 5 (Conformal Probabilistic Safety Verification)** Select a safety violation parameter $\epsilon \in (0, 1)$ and a confidence parameter $\beta \in (0, 1)$ such that"),
    text("p0008-b003", [240.0, 204.0, 528.0, 248.0], display(BINOM, 5)),
    text("p0008-b004", [90.0, 255.0, 508.0, 266.0],
         r"where $k$ and $N$ are as defined above. Then, with probability at least $1-\beta$, the following holds:"),
    text("p0008-b005", [251.0, 274.0, 528.0, 301.0],
         display(PS + r" \left( V(x,0) \le 0 \right) \le \epsilon", 6)),
    text("p0008-b006", [90.0, 309.0, 523.0, 347.0],
         "Lemma 5 is, in fact, precisely the same result as obtained by Theorem 2 using robust scenario optimization. This is no coincidence, as one can show that split conform prediction more generally reduces to a robust scenario-optimization problem."),
    text("p0008-b007", [90.0, 359.0, 523.0, 384.0],
         "**Remark 6** In general, a split conformal prediction problem can be reduced to a robust scenario-optimization problem. This is proven in the Appendix of the extended version of this article." + FN),
    text("p0008-b008", [90.0, 397.0, 523.0, 434.0],
         "Due to the equivalence between conformal method and robust scenario-based methods, the analysis in Section 4 holds here as well. More generally, we hope that this insight will lead to future research into further investigating the close relationship between the two methods."),
    heading("p0008-b009", [90.0, 455.0, 411.0, 467.0],
            "## 6. Outlier-Adjusted Probabilistic Safety Verification Approach"),
    text("p0008-b010", [90.0, 472.0, 523.0, 510.0],
         "The verification methods in Sections 4 and 5 are limited by the quality of the neural reachable tube. Although they can account for outliers, the computed safety level can be low if the outlier rate is high. This can lead to significant losses in the safe volume, as demonstrated in Sections 6.2 and 6.3."),
    text("p0008-b011", [90.0, 513.0, 523.0, 619.0],
         r"To address this issue, we propose an outlier-adjusted approach that can recover a larger safe volume for any desired $\epsilon$. Note that in the verification methods, the key quantity which determines $\epsilon$ is the number of safety violations $k$. This corresponds to the number of samples $x_i$ which are marked safe by membership in $\mathcal{S}$, i.e., $" + V + r"(x_i,0) \ge \delta$, but are not guaranteed to be safe, i.e., $" + J + r"\left(x_i,0\right) \le 0$. It is easy to see that the best we can do to simultaneously minimize $k$ and maximize volume is to compute $\mathcal{S}$ as the super-$\delta$ level set of the induced *cost* function $" + J + r"(x,0)$. For example, the largest possible $\mathcal{S}$ that is guaranteed to be violation-free is precisely the super-zero level set of $" + J + r"(x,0)$. Thus, our overall approach will be to refine $" + V + r"(x,0)$ so that it more accurately reflects $" + J + r"(x,0)$."),
    text("p0008-b012", [90.0, 621.0, 523.0, 706.0],
         r"Modeling $" + J + r"(x,0)$ can be formulated as a supervised learning problem, since we can sample a state $x_i$ and compute its cost $" + J + r"(x_i,0)$ in simulation. We learn an approximation $" + JT + r"(x,0)$ by retraining $" + V + r"(x,0)$ on a training dataset $\mathcal{T}$ of $n$ samples, $\mathcal{T} = (x_1, " + J + r"(x_1,0)), ..., (x_n, " + J + r"(x_n,0))$. Specifically, we use the *weighted* MSE loss $\frac{1}{n}\sum_{i=1}^{n}w_{i}(" + V + r"(x_i,0) - " + J + r"(x_i,0))^2$, where $w_{i} = w$ if the error is conservative $\left(" + V + r"(x_i,0) < " + J + r"(x_i,0)\right)$, otherwise $w_i = 1$. We introduce $w$ as a hyperparameter to underweight conservative errors because in the end, we are concerned with recovering"),
    pageno(8, "p0008-b013", [303.0, 726.0, 309.0, 733.0]),
]

save(8, items, r"""
Compared the whole page with the 130 dpi render, with 200-210 dpi crops of Lemma 5 and of the lower half of the page
(Section 6), and with sections/conformal_method.tex and sections/outlier-adjusted_approach.tex. All mathematics was
rewritten in LaTeX from the TeX source (macros expanded: \learnedCostFunction -> \tilde{J}_{\tilde{\pi}}) and checked on
the crops; TeX and PDF agree. The two extractor 'formula' images were replaced by $$ blocks with \tag{5} and \tag{6};
conditions (5) and (6) are printed identically to (2) and (3) of Theorem 2 (the guarantee is again on the true value
function V, 'P_{x in S}(V(x,0) <= 0) <= eps'). 'Lemma 5 (Conformal Probabilistic Safety Verification)' and 'Remark 6'
are printed in bold without punctuation; the lemma body (italic) ends with display (6), the remark is the two sentences
ending '... of this article.' followed by footnote mark 1 (ends taken from the TeX environments). Footnote mark 1 refers
to footnote 1 printed on page 5; the sentence is kept verbatim although this arXiv version contains the appendix. Authors'
typos and wording kept as printed: 'split conform prediction' (for 'conformal'), 'between conformal method and robust
scenario-based methods'. Checked on the crop: '\tilde{V}(x_i,0) >= delta', 'J_{\tilde{\pi}}(x_i,0) <= 0' (printed with
\left( \right), which leaves a small gap after the subscript), the training set T = (x_1, J(x_1,0)), ..., (x_n,
J(x_n,0)) printed without set braces, the weighted MSE loss (1/n) sum_{i=1}^{n} w_i (\tilde{V}(x_i,0) -
J_{\tilde{\pi}}(x_i,0))^2 with w_i = w for conservative errors (\tilde{V} < J) and w_i = 1 otherwise. Heading 6 is level 2.
Line-wrap hyphens removed (proba-bility, hyperpa-rameter); real hyphens kept or restored ('scenario-optimization' is
broken at the line end after 'scenario-' in Remark 6 and the extractor had 'scenariooptimization'; lower-bound,
outlier-adjusted, violation-free, super-zero, scenario-based). The last sentence continues on page 9 ('... we are
concerned with recovering | larger safe volumes.'); the first item of page 9 has join_previous 'space'. Omitted: running
header and page number.
""")
