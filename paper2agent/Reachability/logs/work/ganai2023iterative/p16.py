from pagelib import *
P = 16
items = [
    text("p0016-b000", B(P, "p0016-b000"),
         r"policy, starting from state $s$, there are no future violations incurred in $\tau$. Thus $V^\pi_c(s)=0$. Since $\pi^{\ast}$ incurs the minimum cumulative violation, $V^{\pi^{\ast}}_c(s)=0$ trivially. Therefore, $s$, the first state of the trajectory, is in the feasible set of $\pi^{\ast}$.",
         join_previous="space"),
    text("p0016-b001", B(P, "p0016-b001"),
         r"**Case 2 $m>1$:** Since policy $\pi^{\ast}$ produces the minimum cumulative discounted cost for a given state $s$, the core of this proof will be demonstrating that the minimum cumulative discounted cost of *entering* the feasible set (call this value $H_E$) is less than the minimum cumulative discounted cost of *not entering* the feasible set (call this value $H_N$), and therefore $\pi^{\ast}$ will choose the route of entering the feasible set."),
    text("p0016-b002", B(P, "p0016-b002"),
         r"The proof will proceed by deriving a sufficient condition for $H_E<H_N$ by establishing bounds on them."),
    text("p0016-b003", B(P, "p0016-b003"),
         r"We place an upper bound on the minimum cumulative discounted cost of entering the feasible set $H_E$. Since $\exists\pi$ that enters the feasible set in $m-1$ steps, entering the feasible set can be at most the highest possible cost that $\pi$ incurs. Since the maximum cost at any state is $H_{\max}$, the upper bound is the discounted sum of $m-1$ steps of violations $H_{\max}$, or"),
    display("p0016-b004", B(P, "p0016-b004"),
            r"H_E < \frac{H_{\max}(1-\gamma^{m-1})}{(1-\gamma)}"),
    text("p0016-b005", [107.0, 291.0, 506.0, 362.0],
         r"We place a lower bound on the minimum cumulative discounted cost of not entering the feasible set $H_N$. In this case, say in the sampled trajectory, the maximum gap between any two non-zero violations is $w$. By definition, the trajectory cannot have an infinite sequence of violation-free states since the trajectory never enters the feasible set. Therefore $w$ is finite. Now recall $H_{\min}$ is the lower bound on the non-zero values of $h$. So the minimum cumulative discounted cost of not entering the feasible set must be at least the cost of the trajectory with a violation of $H_{\min}$ at intervals of $w$ steps. That is:"),
    display("p0016-b006", [265.0, 362.5, 347.0, 395.0],
            r"\frac{H_{\min}(\gamma^{w})}{(1-\gamma^{w})} < H_N"),
    text("p0016-b007", B(P, "p0016-b007"),
         r"Now $H_E < H_N$ will be true if the upper bound of $H_E$ is less than the lower bound of $H_N$. In other words $H_E < H_N$ is true if:"),
    display("p0016-b008", B(P, "p0016-b008"),
            r"\frac{H_{\max}(1-\gamma^{m-1})}{(1-\gamma)} < \frac{H_{\min}(\gamma^{w})}{(1-\gamma^{w})} \tag{5}"),
    text("p0016-b009", [107.0, 467.5, 192.0, 478.0], r"Rearranging, we get:"),
    display("p0016-b010", [234.0, 478.5, 510.0, 509.0],
            r"\frac{H_{\max}}{H_{\min}} < \frac{(1-\gamma)\cdot (\gamma^{w})}{(1-\gamma^{m-1})\cdot(1-\gamma^{w})} \tag{6}"),
    text("p0016-b011", B(P, "p0016-b011"),
         r"Let’s define the RHS of the Inequality 6 as the function $\upsilon(\gamma)$. Consider $\gamma\in(0,1)$. It is not difficult to demonstrate that $\upsilon(\gamma)$ in this domain range is a continuous function and that left directional limit $\lim_{\gamma \to 1^{-}} \upsilon(\gamma)=\infty$. This suggests that there is an open interval of values for $\gamma$ (whose supremum is $1$) for which $H_{\max}/H_{\min} < \upsilon(\gamma)$ and so $H_E < H_N$. So we establish that $\exists \epsilon>0$ such that for $\gamma\in (1-\epsilon,1)$, we satisfy the sufficient condition $H_E < H_N$ so that the optimal policy will enter its feasible set."),
    text("p0016-b012", [107.0, 586.0, 505.0, 634.0],
         r"Thus, we prove that if there is a policy entering its feasible set from state $s$, then there is a range of values for $\gamma$ that are close enough to $1$ ensuring that the optimal policy of Main paper Equation 3 will enter its feasible set in a finite number of steps with minimum discounted sum of costs. $\square$"),
    heading("p0016-b013", B(P, "p0016-b013"), "### C.4 Theorem 2 with Proof"),
    text("p0016-b014", B(P, "p0016-b014"),
         r"**Theorem 4.** Given Assumptions **A1**-**A3** in Main paper, the policy updates in Algorithm 1 will almost surely converge to a locally optimal policy for our proposed optimization in Equation RESPO."),
    text("p0016-b015", B(P, "p0016-b015"),
         r"We first provide an intuitive explanation behind why our REF learns to converge to the safest policy’s REF, then a proof overview, and then the full proof."),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 16 and with main.tex (rest of the proof of the restated Proposition 2,
start of C.4). The first item continues the Case 1 paragraph from page 15 ('... using that | policy, starting from
state $s$ ...') with join_previous 'space'. All mathematics rewritten in LaTeX from the TeX source and checked on the
render; TeX and PDF agree. Four displays replaced the extractor's formula images: the unnumbered upper bound
$H_E<H_{\max}(1-\gamma^{m-1})/(1-\gamma)$, the unnumbered lower bound $H_{\min}(\gamma^{w})/(1-\gamma^{w})<H_N$, and
the two numbered inequalities (5) and (6) (the equation counter continues from (4) of the main text; the appendix
numbers are (5)-(13)). None of the four displays ends with punctuation. 'Inequality 6' as printed. The function is
named with the Greek letter upsilon, $\upsilon(\gamma)$ (not $v$): checked against the source. The left limit is
printed $\lim_{\gamma\to 1^{-}}\upsilon(\gamma)=\infty$. 'Case 2 $m>1$:' bold label and colon as printed; italics kept
for 'entering' and 'not entering'. The end-of-proof box is printed on its own line after the last paragraph and is
written as a square symbol at the end of that paragraph. C.4 restates Theorem 2 of the main text as 'Theorem 4.'
(counter continues; printed number kept) with the added words 'in Main paper'; it refers to 'Algorithm 1' and 'Equation
RESPO'. Heading C.4 level 3. Authors' wording kept: 'in this domain range', 'left directional limit'. Omitted: printed
page number 16.
""")
