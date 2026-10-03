#!/usr/bin/env python3
from pagelib import write_page

NOTES = r"""
Compared with the 170 dpi render and 260 dpi crops of PDF page 6 (each of the four algorithm boxes,
both text regions of the left column, the lower right column) and with the TeX source. Reading order:
left column (Section V text, Algorithm 1, two paragraphs, Algorithm 2, last paragraph), then right
column (end of that paragraph, Algorithm 3, paragraph, Algorithm 4, Section VI). The extractor had
fragmented the four algorithm boxes into headings and list items and had moved lines across columns;
the page was rebuilt. Each algorithm is kept as an image crop (label 'Algorithm n', asset
algorithm-n; crop edges checked on the 260 dpi crops: both rules, the title line and all numbered lines
are inside) followed by a text transcription taken from the algorithmic environments of main.tex and
checked line by line against the crop: title line in bold, one paragraph per printed line with the
printed line numbers ('1:' ...), nesting shown with two em-spaces per level, keywords (Input, while,
do, for, end for, end while, if, then, else if, else, end if, return) bold as printed. The references
to conditions inside Algorithm 1 are the printed equation numbers (13), (14), (17), (20); the comment
of line 4 is printed after a triangle symbol and wraps onto a second line. Algorithm 2 line 5 is
printed slightly less indented than line 4 (authors' \hspace{-0.9em}); it is transcribed at the same
nesting level as line 4. Kept exactly as printed, although they look like slips of the authors (not
conversion errors): Algorithm 1 line 4 passes (17) and (20) as the safe/unsafe conditions (the
conclusions of Theorem 5) and the following text says 'conditions (13) and (17), and (14) and 20' with
the last number printed without parentheses; Algorithm 2 is titled VerifyCells(G, G_u, tau, C_s, C_u)
with upright subscripts s, u in the title and in line 1 but italic subscripts in line 5, uses '-' for
set difference in line 4 and 'for forall g_i = B_r(x) in G, i in N for some r and x'; Algorithm 3 sets
'X_u = G_u' and 'G_s = emptyset' in lines 2-3 and lists the parameter as tau > 0 while Algorithm 1
calls the first stage with 0; Algorithm 4 uses a single bar '|' in both set-builder expressions and a
bold delta. Mathematics in the running text rewritten in LaTeX from main.tex with macros expanded
(\X, \R) and checked on the crops (the superscript |G| on the cell family and on the union, 'i neq j',
'(cup G_u) cup (cup G_s)'). The paragraph 'The verification process in Algorithm 2 ...' runs from the
bottom of the left column into the top of the right column ('... while ensuring rigorous | safety
guarantees.') and is one item. 'V. NUMERICAL METHODS' (extracted as text) and 'VI. NUMERICAL
SIMULATIONS' are '##' headings. The evasion dynamics is an unnumbered $$ block with two bmatrix
columns. Kept as printed: 'find such a h satisfy the RCBF condition', 'implemented by routines
SafetyCheck', 'when the resolution is met', '[x_1, x_2]^T' with an italic T. Line-wrap hyphens removed
(routine, verification); 'x_3-axis' is a printed hyphen.
"""

ALG1 = r"""**Algorithm 1 VerifyRegion($\mathcal{X}, \tau$, $\alpha$, $\beta$)**

1: **Input:** State Space $\mathcal{X}$, Parameters $\tau$, $\alpha$, and $\beta > 0$.

2: $\mathcal{G}_{s}, \mathcal{G}_{u} = \mathrm{VerifyCells}(\mathcal{X}, \mathcal{X}_{u}, 0, \ (13), \ (14))$

3: $\mathcal{G}_{s}, \mathcal{G}_{u} = \mathrm{VerifyCells}(\mathcal{G}_{s}, \mathcal{G}_{u}, \tau, \ (13), \ (14))$

4: $\mathcal{G}_{s}, \mathcal{G}_{u} = \mathrm{VerifyCells}(\mathcal{G}_{s}, \mathcal{G}_{u}, \tau, \ (17), \ (20))$ $\triangleright$ $\alpha$ and $\beta$ are used in the conditions (17) and (20).

5: **return** $\mathcal{G}_{s}$, $\mathcal{G}_{u}$"""

ALG2 = r"""**Algorithm 2 VerifyCells($\mathcal{G}, \mathcal{G}_{u}, \tau, \mathcal{C}_{\mathrm{s}},\mathcal{C}_{\mathrm{u}}$)**

1: **Input:** Grid $\mathcal{G}$ and $\mathcal{G}_{u}$, Parameter $\tau \ge 0$, Robust Safe Condition $\mathcal{C}_{\mathrm{s}}$, and Robust Unsafe Condition $\mathcal{C}_{\mathrm{u}}$.

2: **while** $\mathcal{G} \neq \emptyset$ **do**

3: &emsp;&emsp;**for** $\forall g_{i} = \mathcal{B}_{r}(x) \in \mathcal{G}, i \in \mathbb{N}$ for some $r$ and $x$ **do**

4: &emsp;&emsp;&emsp;&emsp;$\mathcal{G} \gets \mathcal{G} - \{g_{i}\}$

5: &emsp;&emsp;&emsp;&emsp;$\mathcal{G}$, $\mathcal{G}_s$, $\mathcal{G}_{u}$ = $\mathrm{SafetyCheck}(g_i, \mathcal{G}, \mathcal{G}_u, \tau, \mathcal{C}_{s}, \mathcal{C}_{u})$

6: &emsp;&emsp;**end for**

7: **end while**

8: **return** $\mathcal{G}_{s}$, $\mathcal{G}_{u}$"""

ALG3 = r"""**Algorithm 3 SafetyCheck($g_i, \mathcal{G}, \mathcal{G}_{u}, \tau, \mathcal{C}_{s}, \mathcal{C}_{u}$)**

1: **Input:** Cell $g_i$ to check; Grids $\mathcal{G}, \mathcal{G}_{s}, \mathcal{G}_{u}$; Parameter $\tau > 0$; Robust Safe Condition $\mathcal{C}_{s}$; Robust Unsafe Condition $\mathcal{C}_{u}$.

2: $\mathcal{X}_{u} = \mathcal{G}_{u}$

3: $\mathcal{G}_{s} = \emptyset$

4: Sample $n_s$ trajectories of length $\tau$ from a representative point in $g_i$

5: **if** all sampled trajectories satisfy $\mathcal{C}_u$ **then**

6: &emsp;&emsp;$\mathcal{G}_u \gets \mathcal{G}_u \cup \{g_i\}$

7: **else if** at least one sampled trajectory satisfies $\mathcal{C}_s$ **then**

8: &emsp;&emsp;$\mathcal{G}_s \gets \mathcal{G}_s \cup \{g_i\}$

9: **else**

10: &emsp;&emsp;$\mathcal{G} \gets \mathcal{G} \cup \mathrm{SplitCell}(g_i)$

11: **end if**

12: **return** $\mathcal{G}, \mathcal{G}_{s}, \mathcal{G}_{u}$"""

ALG4 = r"""**Algorithm 4 SplitCell($g$)**

1: **Input:** Grid cell $g = \mathcal{B}_r(x) \in \mathcal{G}$

2: Let $(x_1, x_2, \dots, x_n) = x$

3: $P := \left\{ x + \frac{2r}{3} \cdot \boldsymbol{\delta} | \boldsymbol{\delta} \in \{-1, 0, 1\}^n \right\}$

4: **return** $\mathcal{G}_{split} := \{ \mathcal{B}_{\frac{r}{3}}(p)|p \in P\}$"""

A1 = [50.0, 258.0, 303.0, 357.0]
A2 = [50.0, 543.0, 303.0, 676.0]
A3 = [309.0, 132.0, 563.0, 340.0]
A4 = [309.0, 452.0, 563.0, 531.0]

write_page(6, NOTES, [
    ("p0006-b000", "heading", ("p0006-b000",), "## V. Numerical Methods", {}),
    ("p0006-b001", "text", ("p0006-b001",),
     r"Building on Theorem 4 and Theorem 5, we propose a safety verification algorithm aimed at finding a set $S\subset \mathcal{X}$ such that $h=-\mathrm{sd}(x,S)$ satisfies all the necessary properties for safety assessment described in Theorem 2. The proposed method adaptively partitions $\mathcal{X}$ into cells $\mathcal{G}:=\{g_i:=\mathcal{B}_{r_i}(x_i)\}_{i=1}^{|\mathcal{G}|}$, such that $g_i\cap g_j=\emptyset, i \neq j$ and $\cup\mathcal{G}:=\cup_{i=1}^{|\mathcal{G}|} g_i=\mathcal{X}$, when running our algorithms, two disjoint lists, $\mathcal{G}_s$ (tentative safe cells) and $\mathcal{G}_u$ (verified unsafe cells) are maintained and refined, and progressively, cells from $\mathcal{G}_s$ are assigned to $\mathcal{G}_u$ (while keeping $\mathcal{X} = (\cup \mathcal{G}_u) \cup (\cup\mathcal{G}_s)$) until one is able to guarantee that the safe set $S=\cup \mathcal{G}_s$ and RCBF $h=-\mathrm{sd}(x,S)$ satisfy the robust conditions of Theorem 2.", {}),
    ("p0006-b002", "text", ("p0006-b002",),
     r"This verification process is carried out in three stages, as illustrated in Algorithm 1, where lines $2, 3,$ and $4$ represent stages $1, 2,$ and $3$, respectively.", {}),
    ("p0006-alg1", "figure", A1, "", {"label": "Algorithm 1", "asset_name": "algorithm-1"}),
    ("p0006-alg1-text", "text", A1, ALG1, {}),
    ("p0006-b015", "text", ("p0006-b015",),
     r"Each stage aims to sequentially get a better approximation of a region $S \subseteq \mathcal{X}$ for $h=-\mathrm{sd}(x,S)$ to be a valid RCBF. Stage 1 first finds a sufficiently fine outer approximation of $\mathcal{X}_u$. Stage 2 finds an outer approximation of $\mathcal{R}_\tau(\cup \mathcal{G}_u)$, with $\mathcal{G}_u$ being the output of Stage 1. Finally, Stage 3 further uses $S = \cup \mathcal{G}_s$ in order to find such a $h$ satisfy the RCBF condition.", {}),
    ("p0006-b016", "text", ("p0006-b016",),
     r"All stages are implemented by calling a VerifyCells routine, Algorithm 2, with the current estimates of $\mathcal{G}_s$ and $\mathcal{G}_u$ and the assignment conditions $\mathcal{C}_s$ and $\mathcal{C}_u$, corresponding to conditions (13) and (17), and (14) and 20, respectively. Note that we initially start with one cell (the full set $\mathcal{X}$), and each pass progressively finds finer and more accurate approximations for $\mathcal{G}_s$ and $\mathcal{G}_u$.", {}),
    ("p0006-alg2", "figure", A2, "", {"label": "Algorithm 2", "asset_name": "algorithm-2"}),
    ("p0006-alg2-text", "text", A2, ALG2, {}),
    ("p0006-b019", "text", ("p0006-b019", "p0006-b008"),
     r"The verification process in Algorithm 2 can be done in parallel for all cells in the input $\mathcal{G}$ and ends when this set is empty. This framework facilitates high parallelism through concurrent cell verification while ensuring rigorous safety guarantees. That is to say, each cell in Algorithm 2 is eventually verified to be safe or declared to be unsafe by employing the safe and unsafe assignment conditions, $\mathcal{C}_{s}$ and $\mathcal{C}_{u}$, corresponding to each stage. The specific verification of each cell is implemented by routines $\mathrm{SafetyCheck}$ (Algorithm 3).", {}),
    ("p0006-alg3", "figure", A3, "", {"label": "Algorithm 3", "asset_name": "algorithm-3"}),
    ("p0006-alg3-text", "text", A3, ALG3, {}),
    ("p0006-b020", "text", ("p0006-b020",),
     r"Notably, to verify stages 2 and 3, each cell is required to sample $n_s$ trajectories of length $\tau$ and check whether all satisfy an unsafe condition or at least one satisfies the safe condition. Finally, in cases where neither safe nor unsafe conditions can be verified, one is required to either increase the resolution via the SplitCell routine (Algorithm 4) or eventually declare the cell to be unsafe when the resolution is met.", {}),
    ("p0006-alg4", "figure", A4, "", {"label": "Algorithm 4", "asset_name": "algorithm-4"}),
    ("p0006-alg4-text", "text", A4, ALG4, {}),
    ("p0006-b024", "heading", ("p0006-b024",), "## VI. Numerical Simulations", {}),
    ("p0006-b025", "text", ("p0006-b025",),
     "In this section, we validate the performance and the safety of our algorithm using a 3D evasion problem:", {}),
    ("p0006-b026", "text", ("p0006-b026",),
     r"""$$
\dot{x} = \frac{d}{dt}
\begin{bmatrix}
x_1 \\ x_2 \\ x_3
\end{bmatrix}
=
\begin{bmatrix}
-v + v \cos x_3 + ux_2 \\
v \sin x_3 - ux_1 \\
- u
\end{bmatrix},
$$""", {}),
    ("p0006-b027", "text", ("p0006-b027",),
     r"with $[x_1, x_2]^T \in \mathbb{R}^2$ representing the relative planar location and $x_3 \in [0, 2\pi]$ the relative direction. $v \geq 0$ is the aircraft velocity and $u \in [-1,1]$ is the evader’s angular velocity. A collision occurs if $\sqrt{x_1^2 + x_2^2} \leq 1$, which defines a cylindrical collision set of radius 1 along the $x_3$-axis. Our goal is to determine the set of initial states that inevitably lead to a collision, regardless of the evader’s actions.", {}),
])
