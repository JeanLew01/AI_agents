from pagelib import *
P = 1
TITLE = "Iterative Reachability Estimation for Safe Reinforcement Learning"
items = [
    heading("p0001-b001", B(P, "p0001-b001"), "# " + TITLE),
    text("p0001-a1", [145.0, 181.0, 230.0, 213.0], r"**Milan Ganai** UC San Diego `mganai@ucsd.edu`"),
    text("p0001-a2", [262.0, 181.0, 350.0, 213.0], r"**Zheng Gong** UC San Diego `zhgong@ucsd.edu`"),
    text("p0001-a3", B(P, "p0001-b003"), r"**Chenning Yu** UC San Diego `chy010@ucsd.edu`"),
    text("p0001-a4", B(P, "p0001-b004"), r"**Sylvia Herbert** UC San Diego `sherbert@ucsd.edu`"),
    text("p0001-a5", B(P, "p0001-b005"), r"**Sicun Gao** UC San Diego `sicung@ucsd.edu`"),
    heading("p0001-b006", B(P, "p0001-b006"), "## Abstract"),
    text("p0001-b007", B(P, "p0001-b007"), O(P, "p0001-b007")),
    heading("p0001-b008", B(P, "p0001-b008"), "## 1 Introduction"),
    text("p0001-b009", B(P, "p0001-b009"), O(P, "p0001-b009")),
    omit("p0001-b010", B(P, "p0001-b010"), "First-page conference footer '37th Conference on Neural Information Processing Systems (NeurIPS 2023).'; page furniture of the NeurIPS style, the venue is recorded in the conversion notes.", "37th Conference on Neural Information Processing Systems (NeurIPS 2023)."),
    omit("p0001-b000", B(P, "p0001-b000"), "Vertical arXiv stamp in the left margin ('arXiv:2309.13528v1 [cs.LG] 24 Sep 2023'); page furniture, the version is recorded in the conversion notes.", "arXiv:2309.13528v1 [cs.LG] 24 Sep 2023"),
]
save(P, items, r"""
Compared with a 150 dpi render of PDF page 1 and with main.tex (title, author block, abstract, first paragraph of
Section 1). Title heading made identical to the bundle title (printed on two lines between the NeurIPS rules). The author
block is printed as five centred blocks (name in bold, 'UC San Diego', e-mail in typewriter); the extractor had merged
the first two authors into one item with interleaved lines, so the block was rewritten as five items in printed order
(Ganai, Gong, Yu / Herbert, Gao); all five e-mail addresses read on the render and equal to the TeX author block.
'Abstract' is printed as a centred bold heading and is kept as a level-2 heading; '1 Introduction' is level 2. Abstract
and the first Introduction paragraph are pure prose: the extractor text was compared sentence by sentence with the
render and the TeX source and is used unchanged (line-wrap hyphens already removed in 'satisfaction', 'maintaining',
'algorithms', 'performance' (twice); real compounds kept: 'state-wise', 'violation-free', 'safety-constrained',
'state-of-the-art', 'Safety-Constrained', 'real-world', 'safety-critical', 'Trust-region', 'primal-dual',
'multi-timescale', 'minimal-violation'). Citations as printed: [1, 2], [3, 4, 5], [6], [2], [7, 8, 9], [10]. No
mathematics on this page. Omitted: the vertical arXiv stamp in the left margin and the NeurIPS first-page footer line;
there is no printed page number on page 1. The paragraph ends on this page ('... policies when possible.'); the next
paragraph starts on page 2.
""")
