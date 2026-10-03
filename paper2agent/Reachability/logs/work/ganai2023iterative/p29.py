from pagelib import *
P = 29
items = [
    heading("p0029-b000", B(P, "p0029-b000"), "### D.7 Safety MuJoCo Environments"),
    figure("p0029-fig11", [107.0, 97.0, 504.0, 391.3], "Figure 11", "supplementary-figure-11", asset_category="supp_figs"),
    caption("p0029-b002", [107.0, 392.3, 505.0, 401.5], O(P, "p0029-b002")),
    text("p0029-b003", B(P, "p0029-b003"), tidy(O(P, "p0029-b003"))),
    text("p0029-b004", B(P, "p0029-b004"), tidy(O(P, "p0029-b004", ("also has 0 constraint", "also has $0$ constraint")))),
    text("p0029-b005", B(P, "p0029-b005"), tidy(O(P, "p0029-b005"))),
    text("p0029-b006", B(P, "p0029-b006"), tidy(O(P, "p0029-b006"))),
    text("p0029-b007", B(P, "p0029-b007"), tidy(O(P, "p0029-b007"))),
    text("p0029-b008", B(P, "p0029-b008"), tidy(O(P, "p0029-b008"))),
    text("p0029-b009", B(P, "p0029-b009"), tidy(O(P, "p0029-b009"))),
    text("p0029-b010", B(P, "p0029-b010"), O(P, "p0029-b010")),
    pageno(P),
]
for i in items:
    md = i["markdown"]
    assert "** :" not in md and "** ." not in md and "** ," not in md and "_" not in md, i["id"]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 29, a 100 dpi crop of Figure 11, and with main.tex (D.7). Figure 11
(appendix): one crop of the four panels in a 2x2 grid, 'Reacher Cumulative Rewards' (y axis -1.5 to -1.2), 'Reacher
Cumulative Costs' (top), 'HalfCheetah Cumulative Rewards' (scale x10^3), 'HalfCheetah Cumulative Costs' (x10^2)
(bottom), '1e6' on all x axes, legend in the first panel (PPOLag, RCRL, FAC, RESPO (ours), CBF, Vanilla PPO, CRPO,
P3O, PCPO); enlarged versions of the panels of Figure 4. Asset name 'supplementary-figure-11', category supp_figs,
printed label 'Figure 11' kept; bbox from the evidence line extent with a margin (the minus signs of the left tick
labels start at about 114 pt), ending above the caption (392.7 pt); checked on the crop. Caption verbatim. Eight
discussion paragraphs ('Note on HalfCheetah' plus the seven method paragraphs), each starting with a bold label and a
colon (colon bold only in 'Vanilla PPO:'): extractor text compared with render and TeX and used with the spaces between
bold labels and following punctuation removed and the math-mode '$0$' restored in 'also has $0$ constraint
violations'. Authors' typos kept: 'rewrad', 'interesting PPOLag learns', 'has high reward follow by very high
constraint violations', 'since its an order of magnitude', 'similar as in'. Heading D.7 level 3. Omitted: printed page
number 29.
""")
