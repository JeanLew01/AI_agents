from pagelib import *
P = 2
items = [
    text("p0002-b001", B(P, "p0002-b001"), ital(O(P, "p0002-b001")), join_previous="space"),
    text("p0002-b002", B(P, "p0002-b002"), ital(O(P, "p0002-b002",
         ("**ScaRe-Kro** <u>(Scalable Reachability</u> via <u>Koopman</u> Operators)", "**ScaRe-Kro** (Scalable Reachability via Koopman Operators)")))),
    text("p0002-l1", [103.0, 462.0, 523.0, 486.0], r"1. A scalable Koopman-based reachability framework for unknown nonlinear dynamics, using NN lifting functions and NN verification to estimate reachable sets in the original state space."),
    text("p0002-l2", [103.0, 489.0, 523.0, 513.0], r"2. An approach for inflating the resulting Koopman reachable sets using CP, to obtain probabilistic guarantees of overapproximation for the *true* dynamics."),
    text("p0002-b004", B(P, "p0002-b004"), O(P, "p0002-b004")),
    text("p0002-b005", B(P, "p0002-b005"), O(P, "p0002-b005")),
    heading("p0002-b006", B(P, "p0002-b006"), "## 2. Related Work"),
    text("p0002-b007", B(P, "p0002-b007"), O(P, "p0002-b007")),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 2 and with introduction.tex/related_work.tex. First paragraph: continuation
of the Introduction paragraph that starts on page 1 ('over long horizons (Rober and How, 2024). ...'), joined to it
with join_previous 'space'. Second paragraph: method name in bold 'ScaRe-Kro'; in the parenthesis '(Scalable
Reachability via Koopman Operators)' the letters 'Sca', 'Re', 'K', 'r' (in 'Operators'), 'o' (in 'Operators') are
underlined to spell the acronym; the underline cannot be kept in Markdown (no <u>), the words are written plain (the
extractor had broken <u> tags around whole words). Italic phrases as printed: 'safety may not hold for the true
system', 'single', 'linear tracking error dynamics', 'true system trajectories', 'true'. '97.5%' kept as printed.
Contribution list: printed as an enumerated list 1-4; the extractor had merged items 1 and 2 into one item, split into
one item per printed entry. Line-wrap hyphens closed ('reach-able', 'au-tonomous', 'tra-jectories', 'proba-bilistic',
'distribu-tion'); real compounds kept ('data-inefficient', 'closed-loop', 'statistically-valid', 'user-specified',
'Koopman-based', 'CP-based', 'high-dimensional', 'data-driven'). Heading '2. Related Work' set to level 2 (extractor
had level 1). Run-in bold paragraph title 'Reachability via Linear Relaxation' kept inside the text item. Citations
compared with the render: (Rober and How, 2024), (Park et al., 2024; Bak et al., 2025), (Bak et al., 2019), (Shi et
al., 2024), (Bak et al., 2021, 2025), (Althoff et al., 2021), (Zhang et al., 2018), (Zhang et al., 2018; Everett et
al., 2021; Jafarpour et al., 2024), (Nath et al., 2025). The last paragraph continues on page 3 ('Symbolic and one-shot
methods / mitigate this ...'). No mathematics on this page. Omitted: running header 'NATH YIN CHOU' and page number 2.
""")
