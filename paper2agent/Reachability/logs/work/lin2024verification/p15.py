from pagelib import *

AB = "Angelopoulos and Bates (2023)"
Q1 = r"\frac{\lceil(N+1)(1-\alpha)\rceil}{N}"
XT = r"X_{\text{test}}"
YT = r"Y_{\text{test}}"

items = [
    header(15),
    heading("p0015-b001", [90.0, 93.0, 251.0, 105.0], "## Appendix B. Conformal Proofs"),
    heading("p0015-b002", [90.0, 115.0, 205.0, 123.0], "### B.1. Proof of Theorem 3"),
    text("p0015-b003", [90.0, 134.0, 523.0, 268.0],
         r"**Proof**" + "\n\n" +
         r"Theorem 3 is a straightforward application of the split conformal prediction method detailed in " + AB + r", where we set the conformal “input” $x=x$, “output” $y=-" + J + r"(x,0)$, “score function” $s(x,y)=y=-" + J + r"(x,0)$, “size of the calibration set” $n=N$, and “user-chosen error rate” $\alpha=\frac{k+1}{N+1}$. The conformal $\hat{q}$ is then computed as the $" + Q1 + r"$ quantile of the calibration scores $-" + J + r"(x_{1:N},0)$. The quantile is $" + Q1 + r" = \frac{\lceil(N+1)(1-\frac{k+1}{N+1})\rceil}{N} = \frac{\lceil(N+1)(\frac{N-k}{N+1})\rceil}{N} = \frac{N-k}{N}$, where we have defined $k$ in the procedures in Section 4 as the number of scores $-" + J + r"(x_i,0) \ge 0$. Thus, this quantile corresponds precisely to the largest *negative* score, so we know that $\hat{q} < 0$. Theorem 1 in " + AB + r" then yields:"),
    text("p0015-b005", [209.0, 276.0, 528.0, 364.0],
         display(PJ + r" \left( -" + J + r"(x,0) \le \hat{q} \right) \ge 1-\alpha") + "\n\n" +
         display(PJ + r" \left( " + J + r"(x,0) \ge -\hat{q} \right) \ge 1-\frac{k + 1}{N + 1}") + "\n\n" +
         display(PJ + r" \left( " + J + r"(x,0) > 0 \right) \ge \frac{N-k}{N + 1}", 11)),
    text("p0015-b006", [90.0, 371.0, 523.0, 410.0],
         r"where Equation (11) follows from the line preceding it because if $" + J + r"(x,0) \ge -\hat{q}$, then certainly $" + J + r"(x,0) > 0$. This coverage property result is precisely the same as described in Remark 4. Furthermore, Section 3.2 in " + AB + r" yields:"),
    text("p0015-b007", [167.0, 418.0, 528.0, 467.0],
         display(PS + r" \left( " + J + r"(x,0) > 0 \right) \sim \text{Beta}(N + 1 - l, l),\quad l= \lfloor (N + 1)\alpha\rfloor") + "\n\n" +
         display(PS + r" \left( " + J + r"(x,0) > 0 \right) \sim \text{Beta}(N-k, k + 1)", 12)),
    text("p0015-b008", [90.0, 474.0, 523.0, 485.0],
         r"which is precisely the result of Theorem 3. $\blacksquare$"),
    heading("p0015-b009", [90.0, 514.0, 487.0, 525.0],
            "### B.2. Proof that Split Conformal Prediction Reduces to Robust Scenario Optimization"),
    text("p0015-b010", [90.0, 534.0, 523.0, 679.0],
         r"Here, we show that split conformal prediction, in full generality, reduces to a robust scenario optimization problem. We hope that this insight will encourage future research on the close relationship between the highly related but disparate fields of conformal prediction and scenario optimization. In split conformal prediction, we first define a score function $s(x,y) \in \mathbb{R}$ which is meant to reflect the uncertainty for a model input $x$ and corresponding model output $y$. Then, we sample an i.i.d. calibration set $(X_1,Y_1),...,(X_n,Y_n)$ and compute $\hat{q}$ as the $\frac{\lceil(n+1)(1-\alpha)\rceil}{n}$ quantile of the calibration scores $s(X_1,Y_1),...,s(X_n,Y_n)$, where $\alpha \in [0, 1]$ is a user-chosen error rate. For a new i.i.d. sample $" + XT + r"$, we construct a prediction set $C(" + XT + r")=\{y: s(" + XT + r",y) \le \hat{q}\}$. Theorem 1 in " + AB + r" provides the following coverage property: $\mathbb{P} \left( " + YT + r" \in C(" + XT + r") \right) \ge 1-\alpha$. This follows from the more powerful property, first introduced in Vovk (2012), which we prove reduces to a robust scenario-based result after:"),
    text("p0015-b011", [137.0, 689.0, 527.0, 711.0],
         display(r"\mathbb{P} \left( " + YT + r" \in C(" + XT + r") | \{ (X_i, Y_i) \}^n_{i=1} \right) \sim \text{Beta}(n + 1 - l, l), \quad l=\lfloor (n + 1)\alpha \rfloor", 13)),
    pageno(15, "p0015-b012", [301.0, 725.0, 311.0, 733.0]),
]

save(15, items, r"""
Compared the whole page with the 130 dpi render, with two 210 dpi crops (proof of Theorem 3; Section B.2 with display
(13)) and with sections/conformal_appendix.tex. All mathematics was rewritten in LaTeX from the TeX source and checked
symbol by symbol on the crops; TeX and PDF agree. Section B.1: the bold word 'Proof' is printed on a line of its own (the
extractor had made it a heading); it is kept as a bold paragraph label followed by the proof text in the same item.
Checked on the crop: the conformal settings (input x = x, output y = -J_{\tilde{\pi}}(x,0), score s(x,y) = y, n = N,
alpha = (k+1)/(N+1)); the quantile chain ceil((N+1)(1-alpha))/N = ceil((N+1)(1-(k+1)/(N+1)))/N =
ceil((N+1)((N-k)/(N+1)))/N = (N-k)/N with ceiling brackets in every numerator except the last; 'number of scores
-J_{\tilde{\pi}}(x_i,0) >= 0'; '\hat{q} < 0'. The first extractor 'formula' image was a three-line aligned display of
which only the third line carries a printed number, (11); it is written as three consecutive $$ blocks in one item, the
third with \tag{11} (the text refers to 'the line preceding it', so the lines must stay distinguishable): P(-J <= \hat{q})
>= 1 - alpha; P(J >= -\hat{q}) >= 1 - (k+1)/(N+1); P(J > 0) >= (N-k)/(N+1), all three with the probability over
'(x_{1:N}, x) in S'. The second image was a two-line display whose second line carries (12); it is written as two $$
blocks, the second with \tag{12}: Beta(N+1-l, l) with l = floor((N+1) alpha), then Beta(N-k, k+1), both with the
probability over 'x in S'. The proof ends with a filled square at the right of the line 'which is precisely the result of
Theorem 3.', written as $\blacksquare$. Section B.2: one paragraph and display (13), replaced by a $$ block with \tag{13};
the conditional bar in P(Y_test in C(X_test) | {(X_i, Y_i)}_{i=1}^n) is a plain '|' as in the TeX source, the subscript
'test' is upright (\text{test}), alpha is in the closed interval [0, 1], and l = floor((n+1) alpha) uses lower-case n.
Citations 'Angelopoulos and Bates (2023)' (four times, with 'Theorem 1' twice and 'Section 3.2') and 'Vovk (2012)' are as
printed. Headings: 'Appendix B.' is level 2, B.1 and B.2 are level 3. Line-wrap hyphens removed (quan-tile, Fur-thermore,
opti-mization); real hyphens kept (user-chosen, scenario-based). The page ends with display (13); the proof that follows
starts on page 16. Omitted: running header and page number. LaTeX source spacing only: sums such as 'k + 1' and 'N + 1' are typed with spaces where the PDF text layer has spaces (text and display size) and without spaces inside small inline fractions, so that the tool's number tokens agree; this does not change the formulas.
""")
