from pagelib import *
P = 24
items = [
    heading("p0024-b000", B(P, "p0024-b000"), "### D.2 Benchmarks"),
    text("p0024-b001", B(P, "p0024-b001"), O(P, "p0024-b001")),
    text("p0024-b002", B(P, "p0024-b002"), lead_italic(O(P, "p0024-b002",
         ("have 72D and 76D observation", "have $72$D and $76$D observation"),
         ("has a 72D observation", "has a $72$D observation"),
         ("has a 76D observation", "has a $76$D observation")))),
    text("p0024-b003", B(P, "p0024-b003"), lead_italic(O(P, "p0024-b003"))),
    text("p0024-b004", B(P, "p0024-b004"), lead_italic(O(P, "p0024-b004", ("left of _x_ = _−_ 3.", "left of $x=-3$.")))),
    text("p0024-b005", B(P, "p0024-b005"), tidy(lead_italic(O(P, "p0024-b005")))),
    pageno(P),
]
for i in items:
    assert "** ," not in i["markdown"], i["id"]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 24 and with main.tex (D.2 Benchmarks). Prose page (the lower half is blank;
the source forces a page break before D.3). Extractor text compared sentence by sentence with the render and the TeX
source and used with these corrections: run-in italic paragraph titles ('Safety Gym.', 'Safety PyBullet.', 'Safety
MuJoCo.', 'Multi-Drone environment.') written as italics; math-mode numbers restored ('$72$D and $76$D', '$72$D',
'$76$D', '$x=-3$' with an ASCII minus in LaTeX for the printed minus sign); the percentage in 'adding a 5% gaussian
noise' is printed in math type and kept as plain text so that it stays searchable; stray space after bold 'H2' before
the comma removed. Bold '(H1)', '(H2)', 'H1', 'H2', 'RESPO' as printed; the values 0.5 and 0.8 are plain text. The en
dash in 'distance constraint – as we will show' is printed at the start of a line. Citations [30], [50] checked.
Authors' wording kept: 'we compare the algorithms in with complex dynamics in MuJoCo', 'gaussian', 'overly
precautious'. The Multi-Drone paragraph repeats the description of Section 6.2 and adds the final clause. Heading D.2
level 3. Omitted: printed page number 24.
""")
