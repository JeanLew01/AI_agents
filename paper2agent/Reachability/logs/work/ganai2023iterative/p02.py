from pagelib import *
P = 2
items = [
    text("p0002-b000", B(P, "p0002-b000"), O(P, "p0002-b000")),
    text("p0002-b001", B(P, "p0002-b001"), O(P, "p0002-b001",
         ("_limited to learning deterministic policies in deterministic environments_ .", "*limited to learning deterministic policies in deterministic environments*."),
         ("_cannot guarantee entrance into the feasible set when possible_ .", "*cannot guarantee entrance into the feasible set when possible*."))),
    text("p0002-b002", B(P, "p0002-b002"), O(P, "p0002-b002", ("( **RESPO** )", "(**RESPO**)"))),
    text("p0002-b003", B(P, "p0002-b003"), O(P, "p0002-b003", ("_•_ We", "• We"))),
    text("p0002-b004", B(P, "p0002-b004"), O(P, "p0002-b004", ("_•_ We", "• We"))),
    text("p0002-b005", B(P, "p0002-b005"), O(P, "p0002-b005", ("_•_ We", "• We"), ("small or even 0 violations", "small or even $0$ violations"))),
    heading("p0002-b006", B(P, "p0002-b006"), "## 2 Related Work"),
    heading("p0002-b007", B(P, "p0002-b007"), "### 2.1 Constrained Reinforcement Learning"),
    text("p0002-b008", B(P, "p0002-b008"), O(P, "p0002-b008")),
    pageno(P),
]
save(P, items, r"""
Compared with a 150 dpi render of PDF page 2 and with main.tex (Introduction paragraphs 2-4, the three contribution
bullets, Section 2 and the start of Section 2.1). Pure prose page; the extractor text was compared sentence by sentence
with the render and the TeX source. Corrections: stray emphasis markers with a space before the full stop repaired for
the two italic (\emph) phrases 'limited to learning deterministic policies in deterministic environments' and 'cannot
guarantee entrance into the feasible set when possible' (kept as italics, the authors' emphasis); '( **RESPO** )'
closed up to '(**RESPO**)' (bold as printed); the three contribution items are printed with a bullet typed as a math
symbol followed by a space (not a list environment) and are written '• We ...' (the extractor had '_•_'); bold '(i)'
and '(ii)' as printed; the math-mode zero in 'small or even $0$ violations' restored. Heading levels fixed: '2 Related
Work' level 2, '2.1 Constrained Reinforcement Learning' level 3 (the extractor had levels 1 and 2 with bold markers).
Citations checked on the render: [11], [12, 13], [14, 15], [16, 17, 18, 19, 20, 21], [22, 23, 24], [25], [26], [27],
[28, 29], [3, 4, 5, 6], [7, 9, 30, 31], [6], [32], [33], [34], [35]. Authors' wording kept: 'control theoretic
functions', 'the well known', 'There also exist hard-constraint approaches like [26] have theoretical safety
guarantees' (sic), 'for states outside optimal feasible set'. The last paragraph (Section 2.1) breaks in the middle of
the sentence '... else takes steps to minimize | constraint violations.' and continues on page 3 (join_previous there).
Omitted: printed page number 2.
""")
