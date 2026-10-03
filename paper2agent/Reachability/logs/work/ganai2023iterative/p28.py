from pagelib import *
P = 28
items = [
    heading("p0028-b000", B(P, "p0028-b000"), "### D.6 Safety PyBullet Environments"),
    figure("p0028-fig10", [107.0, 97.0, 504.0, 391.3], "Figure 10", "supplementary-figure-10", asset_category="supp_figs"),
    caption("p0028-b002", [107.0, 392.3, 505.0, 401.5], O(P, "p0028-b002")),
    text("p0028-b003", B(P, "p0028-b003"), tidy(O(P, "p0028-b003", ("to almost 0 constraint violations", "to almost $0$ constraint violations")))),
    text("p0028-b004", B(P, "p0028-b004"), tidy(O(P, "p0028-b004"))),
    text("p0028-b005", B(P, "p0028-b005"), tidy(O(P, "p0028-b005"))),
    text("p0028-b006", B(P, "p0028-b006"), tidy(O(P, "p0028-b006"))),
    text("p0028-b007", B(P, "p0028-b007"), tidy(O(P, "p0028-b007"))),
    text("p0028-b008", B(P, "p0028-b008"), tidy(O(P, "p0028-b008"))),
    text("p0028-b009", B(P, "p0028-b009"), O(P, "p0028-b009")),
    pageno(P),
]
for i in items:
    md = i["markdown"]
    assert "** :" not in md and "** ." not in md and "** ," not in md and "_" not in md, i["id"]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 28, a 100 dpi crop of Figure 10, and with main.tex (D.6). Figure 10
(appendix): one crop of the four panels in a 2x2 grid, 'DroneCircle Cumulative Rewards' (scale x10^3), 'DroneCircle
Cumulative Costs' (top), 'BallRun Cumulative Rewards' (x10^3), 'BallRun Cumulative Costs' (x10^2) (bottom), '1e6' on
all x axes, legend in the first panel (PPOLag, RCRL, FAC, RESPO (ours), CBF, Vanilla PPO, CRPO, P3O, PCPO); enlarged
versions of the PyBullet panels of Figure 2. Asset name 'supplementary-figure-10', category supp_figs, printed label
'Figure 10' kept; bbox from the evidence line extent (114.4-497.6 x 99.3-389.4 pt) with a margin, ending above the
caption (392.7 pt); checked on the crop. Caption verbatim. Seven discussion paragraphs, each starting with the bold
method name(s) and a colon (colon bold only in 'Vanilla PPO:'): extractor text compared with render and TeX and used
with the spaces between bold names and following punctuation removed and the math-mode '$0$' restored in 'almost $0$
constraint violations'; the en dash in 'behavior with extremes – it has' is printed. Authors' wording kept: 'In the
both BallRun and DroneCircle', 'its costs violations', 'Drone Circle' (two words in the RCRL paragraph), 'PPOLag' not
bold at its third occurrence in the PPOLag paragraph. Heading D.6 level 3. Omitted: printed page number 28.
""")
