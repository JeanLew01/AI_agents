from pagelib import *
P = 3
items = [
    text("p0003-b001", B(P, "p0003-b001"), O(P, "p0003-b001"), join_previous="space"),
    text("p0003-b002", B(P, "p0003-b002"), ital(O(P, "p0003-b002"))),
    text("p0003-b003", B(P, "p0003-b003"), O(P, "p0003-b003")),
    heading("p0003-b004", B(P, "p0003-b004"), "## 3. Preliminaries"),
    text("p0003-b005", B(P, "p0003-b005"), O(P, "p0003-b005")),
    text("p0003-eq1", [230.0, 552.0, 528.0, 591.0],
         "$$\nx_{t+1} = f(x_t, u_t), \\tag{1a}\n$$\n\n$$\nx_{t+1} = f(x_t, \\pi(x_t, t)) \\doteq \\tilde f(x_t), \\tag{1b}\n$$"),
    text("p0003-b008", B(P, "p0003-b008"),
         r"with timestep $t \in \{0, \dots, T\} \doteq \mathcal{T}$, state $x_t \in \mathcal{X} \subseteq \mathbb{R}^n$, control $u_t \in \mathcal{U} \subseteq \mathbb{R}^m$, and feedback control law $\pi: \mathcal{X} \times \mathcal{T} \rightarrow \mathcal{U}$. The initial state $x_0$ lies in set $\mathcal{X}_0 \subseteq \mathcal{X}$. Denote $\textsf{Int}(\underline{a}, \overline{a}) = \{a \mid \underline{a} \le a \le \overline{a}\}$, as an interval, where $\underline{a}, \overline{a} \in \mathbb{R}^A$ and inequalities hold element-wise, i.e., $\underline{a}_i \le a_i \le \overline{a}_i$, $1 \le i \le A$. Denote the $a$-ball as $\mathcal{B}_a(c) \doteq \{ x \mid \Vert x - c \Vert_\infty \le a\}$ and sequence $q_{1:Q} \doteq \{q_1, q_2, \ldots, q_Q\} = \{q_i\}_{i=1}^Q$. We use $\oplus$ and $\ominus$ to denote the Minkowski sum and difference, respectively."),
    text("p0003-b009", B(P, "p0003-b009"),
         r"**Koopman Operators** As our work relies on Koopman operators, we discuss the basic concepts here. Consider autonomous discrete-time nonlinear dynamics $x_{t+1} = f(x_t)$. A Koopman operator $\mathcal{K}$ is an infinite-dimensional linear operator that evolves the observables $\phi^\infty$ of the state $\mathcal{K} \phi^\infty(x) = \phi^\infty \circ f(x)$"),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 3 and with related_work.tex/preliminary.tex (macros of symbols.tex expanded:
\stateSpace = \mathcal{X}, \ctrlSpace = \mathcal{U}, \stateSpaceDim = \mathbb{R}^n, \ctrlSpaceDim = \mathbb{R}^m,
\B = \mathcal{B}, \infKoop = \mathcal{K}, \enc = \phi). First paragraph: continuation of the 'Reachability via Linear
Relaxation' paragraph from page 2 ('mitigate this but raise ...'), joined with join_previous 'space'. Run-in bold
titles 'Koopman Reachability', 'Data-Driven Reachability', 'Koopman Operators' kept inside their text items. Italic
'true' (twice) as printed. Line-wrap hyphens closed ('cal-ibration', 're-quires', 'ineffi-cient', 'dy-namics',
'meth-ods', 'accu-rately', 'hori-zons', 'con-troller', 'dynam-ics'); real compounds kept ('previously-unseen',
'data-efficient', 'Hamilton-Jacobi', 'high-dimensional', 'Sampling-based', 'Koopman-based', 'Trajectory-tracking',
'tracking-error', 'tracking-based', 'closed-loop', 'Koopman-linearized'). Citations compared with the render (e.g.
(Koopman and Neumann, 1932), (Amini et al., 2021; Bayer and Leine, 2023), (Liu et al., 2021; Forets and Pouly, 2017;
Amini et al., 2021), (Forets and Schilling, 2021; Bak et al., 2021, 2025), (Chou et al., 2021, 2022; Knuth et al.,
2023)). Heading '3. Preliminaries' level 2. Displays (1a) and (1b): the extractor had two formula images; now one
text item with one $$ block per printed tag, \tag{1a} and \tag{1b}, from the TeX subequations (alignment '&' dropped);
the dotted equals sign is \doteq. The paragraph after the displays was glyph soup with <sup> and strikethrough markers
(overlines read as '~~'); rewritten from the TeX and checked on the render: Int is printed in sans serif
(\textsf{Int}), lower/upper interval bounds with underline/overline, the a-ball uses the infinity norm, sequence
notation q_{1:Q}. 'Koopman Operators' paragraph: it continues on page 4 inside a formula; the printed line ends with
'K phi^infinity(x) =' and page 4 starts with 'phi^infinity o f(x) according to ...'. Following the brief, the whole
formula $\mathcal{K} \phi^\infty(x) = \phi^\infty \circ f(x)$ is put on this page and page 4 continues with 'according
to ...' (join_previous 'space'). Omitted: running header (short title) and page number 3.
""")
