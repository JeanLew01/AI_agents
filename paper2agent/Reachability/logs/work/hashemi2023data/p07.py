from pagelib import *
P = 7
Z = r"\mathbf{diag}\left([0_{1\times n},\ R^{\ast}]\right)"
items = [
    text("p0007-b000", B(P, "p0007-b000"),
         r"initial state $s_0 \stackrel{\mathcal{W}}{\sim} \mathcal{I}$. Define the inflated surrogate flowpipe,",
         join_previous="space"),
    display("p0007-b001", B(P, "p0007-b001"),
            r"X = \bar{X} \oplus \mathsf{Zonotope}(0, \mathbf{diag}([0_{1\times n},\ R^{\ast}])),\ R^{\ast} = \left[ R^{1\ast},\cdots,R^{{n\mathrm{K}}\ast} \right]."),
    text("p0007-b002", B(P, "p0007-b002"),
         r"Then, it holds that $X$ is a $\Delta$-confident flowpipe with $\Delta = 1-n\mathrm{K}(1-\delta)$ for $\sigma_{s_0}$ from $M$ with initial state $s_0 \stackrel{\mathcal{W}}{\sim} \mathcal{I}$."),
    text("p0007-b003", [71.0, 161.0, 540.0, 183.0],
         r"**Proof.** Based on the definition of the conformity score, we have $\Pr\left[ R^j \leq R^{j\ast} \right] \geq \delta$. Therefore, we have that"),
    display("p0007-b004", [249.0, 184.0, 363.0, 205.0],
            r"\Pr[R^j > R^{j\ast}] < 1-\delta."),
    text("p0007-b005", B(P, "p0007-b005"),
         "By applying the union bound over probabilities, it follows that"),
    display("p0007-b006", B(P, "p0007-b006"),
            r"\Pr\left[ \bigvee_{j=1}^{n\mathrm{K}} \left(R^j > R^{j\ast} \right) \right] < n\mathrm{K}(1-\delta)."),
    text("p0007-b007", B(P, "p0007-b007"),
         "The negation of this statement implies that"),
    display("p0007-b008", B(P, "p0007-b008"),
            r"\Pr\left[ \bigwedge_{j=1}^{n\mathrm{K}} \left(R^j \leq R^{j\ast} \right) \right] \geq 1-n\mathrm{K}(1-\delta). \tag{3}"),
    text("p0007-b009", B(P, "p0007-b009"),
         r"We now denote $\Delta= 1-n\mathrm{K}(1-\delta)$ so that we can rephrase the above statement as,"),
    display("p0007-b010", B(P, "p0007-b010"),
            r"\Pr\left[ \bigwedge_{j=1}^{n\mathrm{K}} \left( \mid e_{j+n}^\top \sigma_{s_0} - \mathsf{F}^j(s_0) \mid \leq R^{j\ast}\right) \right] \geq \Delta."),
    text("p0007-b011", B(P, "p0007-b011"),
         r"Next, we define the interval $C_j(s_0)$ = $\left[ \mathsf{F}^j(s_0) -R^{j\ast}\ ,\ \mathsf{F}^j(s_0) + R^{j\ast} \right]$. Accordingly, we have"),
    display("p0007-b012", B(P, "p0007-b012"),
            r"\Pr\left[ \bigwedge_{j=1}^{n\mathrm{K}} \left( e_{j+n}^\top \sigma_{s_0} \in C_j(s_0) \right) \right] \geq \Delta"),
    text("p0007-b013", B(P, "p0007-b013"),
         "Based on this, we can now see that"),
    display("p0007-b014", B(P, "p0007-b014"),
            r"\Pr\left[ \sigma_{s_0} \in \mathsf{Zonotope}\left(\mathcal{F}(s_0) , " + Z + r"\right) \right]\geq \Delta \tag{4}"),
    text("p0007-b015", B(P, "p0007-b015"),
         r"Since $s_0 \stackrel{\mathcal{W}}{\sim} \mathcal{I}$ and $\bar{X}$ is a surrogate flowpipe for the surrogate model $\mathcal{F}$ on $\mathcal{I}$, i.e., $s_0 \in \mathcal{I}$ implies $\mathcal{F}(s_0) \in \bar{X}$, we can conclude,"),
    display("p0007-b016", B(P, "p0007-b016"),
            r"\mathsf{Zonotope}\left(\mathcal{F}(s_0) , " + Z + r"\right)\ \subset \bar{X} \oplus \mathsf{Zonotope}\left(0 , " + Z + r"\right) = X \tag{5}"),
    text("p0007-b017", B(P, "p0007-b017"),
         r"This fact implies that $\Pr[\sigma_{s_0} \in X ] \geq \Delta$, i.e., $X$ is a $\Delta$-confident flowpipe, which completes the proof. $\square$"),
    text("p0007-b018", B(P, "p0007-b018"),
         r"Theorem 1 tells us how to obtain a $\Delta$-confident flowpipe given the $\mathrm{K}$-step datasets $D_{\text{train}}$ and $D_{\text{test}}$. We can now compute a lower bound on the minimum size of the calibration dataset that we need given a confidence probability $\Delta\in (0,1)$. Specifically, we note that $\Delta= 1-n\mathrm{K}(1-\delta)$ is"),
    pageno(P),
]
save(P, items, r"""
Compared with the 130 dpi render and a 200 dpi crop of PDF page 7, and with sections/verification.tex. The first item
continues the statement of Theorem 1 from page 6 ('... from the stochastic system $M$ with | initial state ...') with
join_previous 'space'. Theorem 1 consists of that sentence, the unnumbered display defining the inflated flowpipe
$X = \bar{X}\oplus\mathsf{Zonotope}(0,\mathbf{diag}([0_{1\times n},\ R^{\ast}]))$ and the sentence 'Then, it holds that
... $\Delta = 1-n\mathrm{K}(1-\delta)$ ... .'; it ends there (end of the theorem environment in the TeX source; the italic
body is not reproduced in italics). All mathematics rewritten in LaTeX from the TeX source with macros expanded
(\zon -> \mathsf{Zonotope}, \overallf -> \mathcal{F}, \horizon -> \mathrm{K}) and checked symbol by symbol against the
crop; TeX and PDF agree. The seven extractor 'formula' image items and the theorem display were written as eight $$ text
items; printed equation numbers (3), (4), (5) are given as \tag, the other five displays are unnumbered. Checked in
particular: strict inequalities '$>$' and '$<$' in the two union-bound displays, '$\ge$' in (3), the disjunction
$\bigvee$ versus the conjunction $\bigwedge$, limits $j=1$ to $n\mathrm{K}$, the subset sign in (5), and that displays
(4), (5) and the two displays ending in '$\ge\Delta$' / '$= X$' have no final full stop while the others have one.
Asterisk superscripts written ^{\ast}. The proof label is printed in italics ('Proof.') and is given in bold; the
end-of-proof square is written $\square$. In the sentence 'Next, we define the interval $C_j(s_0)$ = [...]' the equals
sign is outside math in the TeX source and is kept so. The extractor's replacement characters for the large brackets were
removed. The last paragraph ends in the middle of a sentence ('$\Delta= 1-n\mathrm{K}(1-\delta)$ is'); it continues on
page 8 below Figure 1.
""")
