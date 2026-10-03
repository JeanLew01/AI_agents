from pagelib import *
P = 27
items = [
    heading("p0027-b000", B(P, "p0027-b000"), "### D.5 Safety Gym Environments"),
    figure("p0027-fig9", [107.0, 97.0, 504.0, 392.5], "Figure 9", "supplementary-figure-9", asset_category="supp_figs"),
    caption("p0027-b002", [107.0, 394.0, 505.0, 403.5], O(P, "p0027-b002")),
    text("p0027-b003", B(P, "p0027-b003"), tidy(O(P, "p0027-b003", ("_has no access to information_", "*has no access to information*")))),
    text("p0027-b004", B(P, "p0027-b004"), tidy(O(P, "p0027-b004"))),
    text("p0027-b005", B(P, "p0027-b005"), tidy(O(P, "p0027-b005", ("over 3 _×_ the number", r"over $3\times$ the number")))),
    text("p0027-b006", B(P, "p0027-b006"), tidy(O(P, "p0027-b006", ("becoming 9 _×_ that", r"becoming $9\times$ that")))),
    text("p0027-b007", B(P, "p0027-b007"), tidy(O(P, "p0027-b007"))),
    text("p0027-b008", B(P, "p0027-b008"), tidy(O(P, "p0027-b008"))),
    text("p0027-b009", B(P, "p0027-b009"), O(P, "p0027-b009")),
    pageno(P),
]
for i in items:
    md = i["markdown"]
    assert "** :" not in md and "** ." not in md and "** ," not in md and "_" not in md, i["id"]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 27, a 100 dpi crop of Figure 9, and with main.tex (D.5). Figure 9 (appendix):
one crop of the four panels in a 2x2 grid, 'CarGoal Cumulative Rewards', 'CarGoal Cumulative Costs' (top),
'PointButton Cumulative Rewards', 'PointButton Cumulative Costs' (bottom; scale factor x10^2 on the cost panel, '1e6'
on all x axes), legend in the first panel (PPOLag, RCRL, FAC, RESPO (ours), CBF, Vanilla PPO, CRPO, P3O, PCPO); these
are enlarged versions of the Safety Gym panels of Figure 2. Asset name 'supplementary-figure-9', category supp_figs,
printed label 'Figure 9' kept; bbox set from the evidence line extent (114.4-497.6 x 99.3-391.2 pt) with a margin and
ending above the caption (394.5 pt); checked on the crop. Caption verbatim. The seven discussion paragraphs each start
with the bold method name(s) followed by a colon; the colon is not bold except in 'Vanilla PPO:' where the source puts
it inside the bold. Extractor text compared with render and TeX and used with corrections: spaces between bold names
and the following colon/comma/full stop removed; italics restored for 'has no access to information'; '$3\times$' and
'$9\times$' restored as mathematics; the line-wrap hyphen of 'maximizing' is not a real hyphen. '&' in 'CRPO, P3O, &
PCPO' as printed. Authors' wording kept: 'in CarGoal environment', 'that of scalar learnable lagrange multiplier',
'maintaining among the lowest violations'. Heading D.5 level 3. Omitted: printed page number 27.
""")
