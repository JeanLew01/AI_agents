from pagelib import *
P = 21
items = [
    text("p0021-b003", B(P, "p0021-b003"), O(P, "p0021-b003"), join_previous="space"),
    figure("p0021-b001", [90.0, 88.0, 522.0, 292.0], "Figure 7", "figure-7"),
    caption("p0021-b002", B(P, "p0021-b002"), O(P, "p0021-b002")),
    heading("p0021-b004", B(P, "p0021-b004"), "#### 8.3.7. Additional results on 3D quadrotor system."),
    text("p0021-b005", B(P, "p0021-b005"), O(P, "p0021-b005")),
    heading("p0021-b006", B(P, "p0021-b006"), "#### 8.3.8. Additional results on MuJoCo hopper system."),
    text("p0021-b007", B(P, "p0021-b007"), O(P, "p0021-b007")),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 21 and with appendix.tex. Printed order: Figure 7 with its caption at the
top of the page, then the end of the 8.3.6 paragraph ('the resulting closed-loop trajectories remain within the
computed set. ...'), then 8.3.7 and 8.3.8. The continuation item is listed first on this page and joined to page 20
with join_previous 'space'; Figure 7 (the unicycle figure of 8.3.5, declared after the 8.3.5 paragraph in the TeX) is
moved with plan.json reading_order to directly after the 8.3.5 paragraph on page 20, so that it neither interrupts the
8.3.6 sentence nor sits in the planar-quadcopter subsection (noted in the conversion notes). Figure 7 (appendix
figure, label 'Figure 7', asset 'figure-7', main category): x-y plot with the CKRS tube, obstacle, GT rollouts,
reference; axes 'x' (-0.8 ... 0.8) and 'y' (-0.6 ... 0.0); legend 'CKRS (99.0%)', 'Obstacle', 'GT Rollouts', 'Reference
Trajectory'; one crop [90, 88, 522, 292] with all labels inside (union of the figure's text lines [92.3, 109.6, 501.2,
286.7]); the extractor's scattered picture text was deleted after checking it lies inside the crop. Caption verbatim
('3D unicycle model' as printed). Headings '8.3.7. Additional results on 3D quadrotor system.' and '8.3.8. Additional
results on MuJoCo hopper system.' (small caps, final period) written as level 4 in the TeX's spelling. Paragraphs:
extractor prose checked on the render (curly quotes around 'height z', 'torso angle', 'Velocity Foot' as printed;
'roll-outs' closed up; 'state-space', 'non-smooth', '11-dimensional', 'closed-loop' kept); references 'Sec. 5.4',
'Fig. 9', 'Fig. 10', 'Figure 11', citation '(Todorov et al., 2012)'. The 8.3.8 paragraph ends on this page. Omitted:
running header (short title) and page number 21.
""")
