from pagelib import *
P = 8
items = [
    text("p0008-b000", B(P, "p0008-b000"), O(P, "p0008-b000", ("_multiple hard and soft constraints_ .", "*multiple hard and soft constraints*."))),
    heading("p0008-b001", B(P, "p0008-b001"), "### 6.1 Main Experiments in Safety Gym, Safety PyBullet, and MuJoCo"),
    text("p0008-b002", B(P, "p0008-b002"), O(P, "p0008-b002", ("(up to 76D observation space)", "(up to $76$D observation space)"))),
    text("p0008-b003", B(P, "p0008-b003"), tidy(O(P, "p0008-b003", ("reasonably low to 0 cost violations", "reasonably low to $0$ cost violations")))),
    figure("p0008-fig2", [107.0, 359.0, 506.0, 507.3], "Figure 2", "figure-2"),
    caption("p0008-b005", [107.0, 508.0, 506.0, 557.0], O(P, "p0008-b005", ("over 3 _×_ violations", r"over $3\times$ violations"))),
    heading("p0008-b006", B(P, "p0008-b006"), "### 6.2 Hard and Soft Constraints"),
    text("p0008-b007", B(P, "p0008-b007"), tidy(O(P, "p0008-b007"))),
    text("p0008-b008", B(P, "p0008-b008"), O(P, "p0008-b008")),
    pageno(P),
]
for i in items:
    assert "** ," not in i["markdown"] and "** ." not in i["markdown"] and "** ’" not in i["markdown"], i["id"]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 8, a 140 dpi crop of Figure 2, and with main.tex (Benchmarks paragraph,
Section 6.1, start of Section 6.2). Prose page: the extractor text was compared sentence by sentence with the render and
the TeX source and used with these corrections: stray spaces between bold method names and following punctuation
removed ('**CRPO**,', '**PPOLag**.', '**RESPO**’s', '**H2**,'); the italic phrase 'multiple hard and soft
constraints' restored as italics with its full stop closed up; math-mode numbers restored ('$76$D', 'low to $0$ cost
violations', '$3\times$ violations' in the caption); the en dash in '**RESPO** – for instance' is printed. Bold kept as
printed for the run-in title 'Benchmarks.', the method names and '(H1)', '(H2)', 'H1', 'H2'. The values 0.5 and 0.8
(distances, no unit in the prose) are plain text as in the source. Figure 2 is one crop of all eight panels (top row:
CarGoal, PointButton, BallRun, DroneCircle Cumulative Rewards; bottom row: the corresponding Cumulative Costs) with the
axis ticks, the scale factors (x10^3, x10^2, 1e6) and the legend that is printed only in the first panel (PPOLag, RCRL,
FAC, RESPO (ours), CBF, Vanilla PPO, CRPO, P3O, PCPO); the extractor's figure box overlapped the caption and carried
the plot labels as hidden picture text, the bbox now ends just above the caption (edges checked on the crop: tick labels
'-10' at the left, '1e6' at the bottom right, panel titles at the top are inside). Caption verbatim. Citations [30],
[50], [51] and references 'Figure 2', 'Figure 3' as printed. Authors' wording kept: 'Safety MuJoCo [51], (namely',
'Drone Circle' (two words here, 'DroneCircle' elsewhere), 'overly precautious'. Line-wrap hyphen removed in
'observation'. The last paragraph is cut by the page break in the middle of a sentence ('... where the higher | Drone
makes way ...') and continues on page 9 after the Figure 3 float (join_previous there). Heading levels fixed (6.1, 6.2
level 3). Omitted: printed page number 8.
""")
