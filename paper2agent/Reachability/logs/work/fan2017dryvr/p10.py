from pagelib import *

items = [
    text("p0010-b000", [133.0, 126.0, 478.0, 149.0],
         r"**Proposition 3.1.** Let $\epsilon, \delta \in \mathbb{R}_{+}$. If $k \geq \frac{1}{\epsilon}\ln\frac{1}{\delta}$ then, with probability $\geq 1-\delta$, the above algorithm finds $(a,b)$ such that $\mathsf{err}_{\mathcal{D}}(a,b) < \epsilon$."),
    text("p0010-b001", [133.0, 157.0, 478.0, 212.0],
         r"*Proof.* The result follows from the PAC-learnability of concepts with low VC-dimension [43]. However, since the proof is very simple in this case, we reproduce it here for completeness. Let $k$ be as in the statement of the proposition, and suppose the pair $(a,b)$ identified by the algorithm has error $> \epsilon$. We will bound the probability of this happening."),
    text("p0010-b002", [133.0, 213.0, 478.0, 260.0],
         r"Let $B = \{(x,y)\: |\: x > ay+b\}$. We know that $\mathcal{D}(B) > \epsilon$. The algorithm chose $(a,b)$ only because no element from $B$ was sampled in Step 1. The probability that this happens is $\leq (1-\epsilon)^k$. Observing that $(1-s) \leq e^{-s}$ for any $s$, we get $(1-\epsilon)^k \leq e^{-\epsilon k} \leq e^{-\ln \frac{1}{\delta}} = \delta$. This gives us the desired result. $\square$"),
    heading("p0010-b003", [133.0, 274.0, 325.0, 284.0], "#### 3.1.2 Learning discrepancy functions"),
    text("p0010-b004", [133.0, 292.0, 478.0, 336.0],
         r"Discrepancy functions will be computed from simulation data independently for each mode. Let us fix a mode $\ell \in \text{Ł}$, and a domain $[0,T]$ for each trajectory. The discrepancy functions that we will learn from simulation data, will be one of two different forms, and we discuss how these are obtained."),
    text("p0010-b005", [133.0, 340.0, 445.0, 351.0],
         "**Global exponential discrepancy (GED)** is a function of the form"),
    text("p0010-b006", [239.0, 355.0, 372.0, 377.0],
         r"$$\beta(x_1,x_2,t) = |x_1 - x_2| Ke^{\gamma t}.$$"),
    text("p0010-b007", [133.0, 382.0, 478.0, 404.0],
         r"Here $K$ and $\gamma$ are constants. Thus, for any pair of trajectories $\tau_1$ and $\tau_2$ (for mode $\ell$), we have"),
    text("p0010-b008", [183.0, 408.0, 429.0, 430.0],
         r"$$\forall t \in [0,T].\ |\tau_1(t) - \tau_2(t)| \leq |\tau_1.\mathit{fstate} - \tau_2.\mathit{fstate}| Ke^{\gamma t}.$$"),
    text("p0010-b009", [133.0, 436.0, 386.0, 446.0],
         "Taking logs on both sides and rearranging terms, we have"),
    text("p0010-b010", [213.0, 450.0, 398.0, 485.0],
         r"$$\forall t.\ \ln \frac{|\tau_1(t) - \tau_2(t)|}{|\tau_1.\mathit{fstate} - \tau_2.\mathit{fstate}|} \leq \gamma t + \ln K.$$"),
    text("p0010-b011", [133.0, 489.0, 478.0, 604.0],
         r"It is easy to see that a global exponential discrepancy is nothing but a linear separator for the set $\Gamma$ consisting of pairs $(\ln \frac{|\tau_1(t) = \tau_2(t)|}{|\tau_1.\mathit{fstate} - \tau_2.\mathit{fstate}|}, t)$ for all pairs of trajectories $\tau_1,\tau_2$ and time $t$. Using the sampling based algorithm described before, we could construct a GED for a mode $\ell \in \text{Ł}$, where sampling from $\Gamma$ reduces to using the simulator to generate traces from different states in $\mathcal{TL}_{\mathsf{init}, \ell}$. Proposition 3.1 guarantees the correctness, with high probability, for any separator discovered by the algorithm. However, for our reachability algorithm to not be too conservative, we need $K$ and $\gamma$ to be small. Thus, when solving the linear program in Step 2 of the algorithm, we search for a solution minimizing $\gamma T + \ln K$."),
    text("p0010-b012", [133.0, 609.0, 478.0, 676.0],
         r"**Piece-wise exponential discrepancy (PED).** The second form of discrepancy functions we consider, depends upon dividing up the time domain $[0,T]$ into smaller intervals, and finding a global exponential discrepancy for each interval. Let $0 = t_0,t_1,\ldots t_N = T$ be an increasing sequence of time points. Let $K, \gamma_1, \gamma_2, \ldots \gamma_N$ be such that for every pair of trajectories $\tau_1,\tau_2$ (of mode $\ell$), for every $i \in \{1,\ldots, N\}$, and $t \in [t_{i-1},t_i]$, $|\tau_1(t) = \tau_2(t)| \leq |\tau_1(t_{i-1}) - \tau_2(t_{i-1})| Ke^{\gamma_i t}$"),
    pageno(10, [300.0, 696.0, 311.0, 703.0]),
]

save(10, items, r"""
Compared with a 190-dpi render of the text block, 330-450 dpi crops of Proposition 3.1 with its proof, of the inline fraction in the GED paragraph and of the last two lines, and algo.tex. Proposition 3.1 (the PAC statement): bold label with period, italic body in the PDF (not reproduced as italics), ends at '$\mathsf{err}_{\mathcal{D}}(a,b) < \epsilon$.'; checked on the 330-dpi crop: $\epsilon, \delta \in \mathbb{R}_{+}$, $k \geq \frac{1}{\epsilon}\ln\frac{1}{\delta}$, 'with probability $\geq 1-\delta$', strict '$< \epsilon$'. Proof: '*Proof.*' printed in italics with a period; two paragraphs; ends with the printed end-of-proof box, written $\square$; chain $(1-\epsilon)^k \leq e^{-\epsilon k} \leq e^{-\ln \frac{1}{\delta}} = \delta$ checked on the crop. '3.1.2 Learning discrepancy functions' is a numbered sub-subsection (####). The three extractor 'formula' images were replaced by LaTeX display blocks from the TeX (none carries a printed equation number, so no \tag): the GED form $\beta(x_1,x_2,t) = |x_1 - x_2| Ke^{\gamma t}$, the trajectory bound over $[0,T]$, and the log form $\ln\frac{|\tau_1(t)-\tau_2(t)|}{|\tau_1.fstate-\tau_2.fstate|} \leq \gamma t + \ln K$. 'Global exponential discrepancy (GED)' and 'Piece-wise exponential discrepancy (PED).' are run-in bold paragraph titles (the second printed with a period); the GED title runs directly into its sentence. SOURCE TYPOS KEPT AS PRINTED (confirmed at 450 dpi, identical in the TeX): in the inline pair of the GED paragraph the numerator is printed '$|\tau_1(t) = \tau_2(t)|$' with '=' where the display above has '$-$'; the same '=' is printed in the PED condition '$|\tau_1(t) = \tau_2(t)| \leq \ldots$'. The extractor's fraction soup in that paragraph was replaced by the TeX form. 'Ł' for \L as printed. PAGE BREAK: the PED condition is split by the page break after '$\leq$'; the whole inequality (its right-hand side '$|\tau_1(t_{i-1}) - \tau_2(t_{i-1})| Ke^{\gamma_i t}$' is printed at the top of page 11) is placed in the last item of this page, and page 11 continues with '. Under such circumstances' (join_previous 'none'). Extractor damage fixed: 'VCdimension' -> 'VC-dimension' (real hyphen); line-wrap hyphens removed (sep-arator, dis-crepancy). References as printed: 'Step 1', 'Step 2', 'Proposition 3.1', citation [43]. Omitted: page number 10.
""")
