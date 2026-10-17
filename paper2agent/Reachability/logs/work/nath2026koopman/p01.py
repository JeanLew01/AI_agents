from pagelib import *
P = 1
TITLE = "Scalable Data-Driven Reachability Analysis and Control via Koopman Operators with Conformal Coverage Guarantees"
items = [
    heading("p0001-b002", B(P, "p0001-b002"), "# " + TITLE),
    text("p0001-a1", [90.0, 142.9, 522.0, 156.7], r"**Devesh Nath** $^{\ast 1}$ dnath7@gatech.edu"),
    text("p0001-a2", [90.0, 156.5, 522.0, 170.3], r"**Haoran Yin** $^{\ast 1}$ hyin95@gatech.edu"),
    text("p0001-a3", [90.0, 170.3, 522.0, 182.5], r"**Glen Chou** $^{2}$ chou@gatech.edu"),
    text("p0001-b005", B(P, "p0001-b005"),
         r"*Georgia Institute of Technology.* $^{1}$ *School of ECE,* $^{2}$ *Schools of Cybersecurity & Privacy & Aerospace Eng.*"),
    text("p0001-b013", B(P, "p0001-b013"), r"© 2026 D. Nath, H. Yin & G. Chou."),
    heading("p0001-b006", B(P, "p0001-b006"), "## Abstract"),
    text("p0001-b007", B(P, "p0001-b007"), O(P, "p0001-b007", ("Results on highdimensional", "Results on high-dimensional"))),
    text("p0001-b008", B(P, "p0001-b008"), r"**Keywords:** safety-critical control, reachability, Koopman operators, conformal prediction"),
    figure("p0001-b009", [88.0, 412.0, 524.0, 578.0], "Figure 1", "figure-1"),
    caption("p0001-b010", B(P, "p0001-b010"),
            r"Figure 1: Executed trajectories / reachable sets for a 28D MuJoCo swimmer (a); 11D hopper (b)."),
    heading("p0001-b011", B(P, "p0001-b011"), "## 1. Introduction"),
    text("p0001-b012", B(P, "p0001-b012"), O(P, "p0001-b012")),
    omit("p0001-b000", B(P, "p0001-b000"),
         "Proceedings banner 'Proceedings of Machine Learning Research vol vvv:1–28, 2026' at the top of the first page (PMLR/jmlr class placeholder, not a real volume); page furniture, the source version is recorded in the conversion notes.",
         "Proceedings of Machine Learning Research vol vvv:1–28, 2026"),
    omit("p0001-b001", [10.9, 221.0, 37.7, 571.0],
         "Vertical arXiv stamp in the left margin ('arXiv:2601.01076v1 [eess.SY] 3 Jan 2026'); page furniture, the version is recorded in the conversion notes.",
         "arXiv:2601.01076v1 [eess.SY] 3 Jan 2026"),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 1, a 220 dpi crop of Figure 1, and with main.tex/abstract.tex/introduction.tex.
Title heading made identical to the bundle title (printed on two lines, bold). Author block as printed: three lines, bold
name with the printed superscript marks (*1, *1, 2; written $^{\ast 1}$ etc.) and the e-mail address set flush right in
small caps (written in lower case as in the TeX source: dnath7@gatech.edu, hyin95@gatech.edu, chou@gatech.edu), then
the italic affiliation line 'Georgia Institute of Technology. 1 School of ECE, 2 Schools of Cybersecurity & Privacy &
Aerospace Eng.' with superscript 1 and 2. No footnote text explains the asterisk on this page or elsewhere; none was
added. The extractor had merged the three names into one item with <sup> tags and the e-mails into another; rewritten
as one item per printed line. The copyright line at the foot of the page, '© 2026 D. Nath, H. Yin & G. Chou.', is kept
as text and placed directly after the author block (like a first-page footnote) so that the last Introduction
paragraph stays the last item of the page and can be joined with its continuation on page 2. 'Abstract' is printed as
a centred bold heading (level 2). Abstract: extractor text checked line by line against the render and abstract.tex;
the line-wrap 'high-/dimensional' is a real compound and was restored ('high-dimensional'; the extractor had
'highdimensional'); other wraps ('verifica-tion', 'in-flate') are ordinary word breaks and are closed up. Keywords line
kept with bold 'Keywords:'. Figure 1 (swimmer snapshots on the checkerboard top left, hopper snapshots bottom left, six
small time plots on the right: Body Rot, Vel X, Vel Y, Height z, Torso Angle, Foot Joint, x-axis 'Time (s)'; legend
'Conformalized Koopman Reachable Set', 'Reference', 'Simulation Ground Truth Rollouts', 'Snapshots'; time stamps
t = 0.00 s ... t = 3.99 s) is one crop 'figure-1' with all labels inside (edges checked on the 220 dpi crop: legend,
tick labels -20/-25, 'Time (s)'). The caption refers to panels '(a)' and '(b)', but no panel letters are printed in
the figure (checked on the 220 dpi crop); from the figure content (a) is the swimmer (top) and (b) the hopper (bottom).
The extractor's scattered picture text was deleted after checking that it lies inside the crop. Caption verbatim.
Introduction, first paragraph: prose verbatim from the extractor, checked on the render; citations as printed
'(Bansal et al., 2017; Althoff, 2015)'. The paragraph ends on this page with '... excessive overapproximation' and
continues on page 2 ('over long horizons ...'): joined there with join_previous 'space'. Omitted: the PMLR banner
line at the top and the vertical arXiv stamp; no page number is printed on page 1.
""")
