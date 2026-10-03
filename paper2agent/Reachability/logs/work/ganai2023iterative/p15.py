from pagelib import *
P = 15
items = [
    display("p0015-b000", B(P, "p0015-b000"),
            r"\phi^\pi (s) = \max \{ \mathbb{1}_{s\in \mathcal{S}_v} , \mathbb{E}_{s' \sim \pi,P(s)} \phi^\pi(s') \},"),
    text("p0015-b001", B(P, "p0015-b001"),
         r"where $s' \sim \pi,P(s)$ is a sample of the immediate successive state (i.e., $s' \sim P(\cdot| s , a\sim \pi(\cdot | s))$) and the expectation is taken over all possible successive states."),
    text("p0015-b002", B(P, "p0015-b002"), r"**Proof.**"),
    display("p0015-b003", B(P, "p0015-b003"), r"""\begin{aligned}
\phi^\pi(s) &:= \mathbb{E}_{\tau \sim \pi ,P(s)} \max_{s_t \in \tau} \mathbb{1}_{s_t^\pi \in S_v} \\
&= \mathbb{E}_{\tau \sim \pi ,P(s)} \max\{\mathbb{1}_{s \in S_v}, \max_{s_t \in  \tau \backslash \{s\}} \mathbb{1}_{s_t^\pi \in S_v} \} \\
&= \max\{\mathbb{1}_{s \in S_v}, \mathbb{E}_{\tau \sim \pi ,P(s)} \max_{s_t \in  \tau \backslash \{s\}} \mathbb{1}_{s_t^\pi \in S_v} \} \\
&= \max\{\mathbb{1}_{s \in S_v}, \mathbb{E}_{s' \sim \pi ,P(s)} \mathbb{E}_{\tau' \sim \pi ,P(s')} \max_{s_t \in  \tau'} \mathbb{1}_{s_t^\pi \in S_v} \} \\
&= \max\{\mathbb{1}_{s \in S_v}, \mathbb{E}_{s' \sim \pi ,P(s)} \phi^\pi(s') \}
\end{aligned}"""),
    text("p0015-b004", [107.0, 264.0, 505.0, 335.0],
         r"Note that we use the notation $\tau\sim \pi,P(s)$ to indicate a trajectory sampled from the MDP with transition probability $P$ under policy $\pi$ starting from state $s$, and use the notation $s'\sim \pi,P(s)$ to indicate the next immediate state from the MDP with transition probability $P$ under policy $\pi$ starting from state $s$. The third line holds because the indicator function is either $0$ or $1$, so if it’s $1$ then $\phi^\pi(s)=\mathbb{E}_{\tau \sim \pi ,P(s)} 1 = 1$ else $\phi^\pi(s)=\mathbb{E}_{\tau \sim \pi ,P(s)} \max_{s_t \in  \tau \backslash \{s\}} \mathbb{1}_{s_t^\pi \in S_v}$. $\square$"),
    heading("p0015-b005", B(P, "p0015-b005"), "### C.2 Proposition 1 with Proof"),
    text("p0015-b006", B(P, "p0015-b006"),
         r"**Proposition 3.** The cost value function $V_c^\pi (s)$ is zero for state $s$ if and only if the persistent safety is guaranteed for that state under the policy $\pi$."),
    text("p0015-b007", B(P, "p0015-b007"),
         r"**Proof.** (IF) Assume for a given policy $\pi$, the persistent safety is guaranteed, i.e. $h(s_t|s_0 = 0, \pi) = 0$ holds for all $s_t \in \tau$ for all possible trajectories $\tau$ sampled from the environment with control policy $\pi$. We then have:"),
    display("p0015-b008", B(P, "p0015-b008"),
            r"V^\pi_c(s):=\mathbb{E}_{\tau \sim \pi,P(s)} [\sum\limits_{s_t\in \tau} \gamma^t h(s_t)] = 0."),
    text("p0015-b009", [107.0, 473.0, 506.0, 517.0],
         r"(ONLY IF) Assume for a given policy $\pi$, $V^\pi_c(s) = 0$. Since the image of the safety loss function $h(s)$ is non-negative real, and $V^\pi_c(s)$ is the expectation of the sum of non-negative real values, the only way $V^\pi_c(s) = 0$ is if $h(s_t|s_0 = 0, \pi) = 0$, $\forall s_t \in \tau$ for all possible trajectories $\tau$ sampled from the environment with control policy $\pi$. $\square$"),
    heading("p0015-b009h", [107.0, 529.0, 300.0, 541.0], "### C.3 Proposition 2 with Proof"),
    text("p0015-b009p", [107.0, 549.0, 506.0, 599.0],
         r"**Proposition 4.** If $\exists\pi$ that produces trajectory $\tau=\{(s_i),i\in\mathbb{N}, s_1=s\}$ in deterministic MDP $\mathcal{M}$ starting from state $s$, and $\exists m\in \mathbb{N}, m<\infty$ such that $s_m\in S^\pi_f$, then $\exists \epsilon>0$ where if discount factor $\gamma\in (1-\epsilon,1)$, then the optimal policy $\pi^{\ast}$ of Main paper Equation 3 will produce a trajectory $\tau'=\{(s'_j),j\in\mathbb{N}, s'_1=s\}$, such that $\exists n\in \mathbb{N}, n<\infty$, $s'_n\in S^{\pi^{\ast}}_f$ and $V^{\pi^{\ast}}_c(s)=\min_{\pi'} V^{\pi'}_c(s)$."),
    text("p0015-b010", B(P, "p0015-b010"),
         r"In other words the proposition is stating for some state $s$, if there is a policy that enters its feasible set in a finite number ($m-1$) of steps, then by ensuring discount factor $\gamma$ is close to $1$ we can guarantee that the optimal policy $\pi^{\ast}$ of Main paper Equation 3 will also enter the feasible set in a finite number of steps with the minimum cumulative discounted sum of the costs. Note that $\pi^{\ast}$ will always produce trajectories with the minimum discounted sum of costs whether the state is in the feasible or infeasible set of the policy by virtue of its optimization which constrains $V^\pi_c$."),
    text("p0015-b011", B(P, "p0015-b011"),
         r"**Proof.** We consider two cases: (Case 1) $m=1$ and (Case 2) $m>1$."),
    text("p0015-b012", B(P, "p0015-b012"),
         r"**Case 1 $m=1$:** In this case, there exists a policy $\pi$ in which the the current state $s$ is in the feasible set of that policy. By definition, that means that in a trajectory $\tau$ sampled in the MDP using that"),
    pageno(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 15, a 260 dpi crop of the five-line proof display, and with main.tex
(appendix C.1 from the display of the restated theorem, C.2, start of C.3). The page starts with the display that
belongs to 'Theorem 3.' (the appendix restatement of Theorem 1, lead-in on page 14); the statement ends with the
sentence 'where ... all possible successive states.' (end of the theorem environment; unlike the main-text version it
has no sentence about the appendix). All mathematics rewritten in LaTeX from the TeX source (macros expanded) and
checked on the render and the crop; TeX and PDF agree. Proof of the Bellman recursion: 'Proof.' is printed in italics on
its own line (written in bold); the derivation is one unnumbered five-line aligned display (definition, split of the
first state, max and expectation exchanged, tower property over $s'$ and $\tau'$, result) written as one aligned
block; the explanatory paragraph follows and the end-of-proof box, printed on its own line at the right margin, is
written as a square symbol at the end of that paragraph. As printed (kept): the indicator subscripts in the proof are
$s_t^\pi\in S_v$ and $s\in S_v$ with an italic $S_v$ (calligraphic in the statement), the set difference is typed with
a backslash, and the last line of the display has no final punctuation. C.2: the restated Proposition 1 is numbered
'Proposition 3.' in the PDF (counter continues) and C.3 restates Proposition 2 as 'Proposition 4.' with 'Main paper
Equation 3' in place of 'Equation 3'; both printed numbers are kept. The extractor had merged the '(ONLY IF)'
paragraph, the heading 'C.3 Proposition 2 with Proof' and Proposition 4 into one text item; they are three items now.
Proof of Proposition 3: '(IF)' and '(ONLY IF)' parts with the unnumbered display $V^\pi_c(s):=\ldots=0.$ between
them; the condition is printed as $h(s_t|s_0 = 0, \pi) = 0$ (with '$s_0=0$', twice), kept. The box ends the '(ONLY IF)'
paragraph. Proof of Proposition 4 starts on this page: 'Proof.' line and 'Case 1 $m=1$:' (bold label and colon as
printed; 'the the' is in the source); the Case 1 paragraph is cut by the page break ('... using that | policy,
starting from state $s$ ...') and continues on page 16 (join_previous there). Headings C.2, C.3 level 3. Omitted:
printed page number 15.
""")
