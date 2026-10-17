from pagelib import *
P = 18
EQ14 = "\n".join([
    r"$$",
    r"\dot{\mathbf{x}} \;=\; f(\mathbf{x},\mathbf{u})=",
    r"\begin{bmatrix}",
    r"\dot{x} \\",
    r"\dot{y} \\",
    r"\dot{z} \\",
    r"q \cdot \sin(\phi)/\cos{\theta}+r\cdot \cos{\phi}/\cos{\theta} \\",
    r"q \cdot \cos{\phi} - r\cdot \sin{\phi} \\",
    r"p + q \cdot \sin{\phi}\cdot \tan{\theta} +r\cdot \cos{\phi} \cdot \tan{\theta} \\",
    r"\frac{u_1}{m} \cdot (\sin{\phi} \cdot \sin{\psi} + \cos{\phi} \cdot \cos{\psi} \cdot \sin{\theta}) \\",
    r"\frac{u_1}{m} \cdot (\cos{\phi} \cdot \sin{\phi} - \cos{\phi} \cdot \sin{\psi} \cdot \sin{\theta}) \\",
    r"g + u_1 \cdot (\cos{\phi} \cdot \cos{\theta}) / m\\",
    r"((I_y - I_z) / I_x) \cdot q\cdot r + \frac{u_2}{I_x} \\",
    r"((I_z - I_x) / I_y) \cdot p\cdot r + \frac{u_3}{I_y} \\",
    r"((I_x - I_y) / I_z) \cdot p\cdot q + \frac{u_4}{I_z}",
    r"\end{bmatrix} \tag{14}",
    r"$$",
])
orig_rows = [r for r in [[c.replace("**", "") for c in row] for row in
             [i for i in json.loads((S / "orig_pages/page-0018.json").read_text())["items"] if i["id"] == "p0018-b005"][0]["rows"]]]
items = [
    text("p0018-b001", B(P, "p0018-b001"),
         r"For 3D quadcopter experiments, we used the parameters $m=1$kg, $g=-9.81$ m/s$^2$, $I_{x,y,z}=[0.5, 0.1, 0.3]$ kg·m$^2$ for the dynamics, with a time-discretization of $dt = 0.025\,\mathrm{s}$:"),
    text("p0018-b002", B(P, "p0018-b002"), EQ14),
    heading("p0018-b003", B(P, "p0018-b003"), "#### 8.3.2. Comparison between neural Koopman liftings and polynomial liftings"),
    text("p0018-b004", B(P, "p0018-b004"), O(P, "p0018-b004", ("using auto ~~L~~ iRPA.", "using `auto_LiRPA`."))),
    table("p0018-b005", [186.0, 488.0, 426.0, 658.0], "Table 2", "table-2", orig_rows),
    caption("p0018-b006", B(P, "p0018-b006"), O(P, "p0018-b006")),
    run_header(P),
    page_number(P),
]
assert orig_rows[0] == ["State", "Polynomial Lifting", "Ours"] and len(orig_rows) == 12, orig_rows[0]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 18, a 220 dpi crop of display (14), a 240 dpi crop of Table 2, and with
appendix.tex. 3D quadcopter sentence: mathematics from the TeX (units partly outside math as typed: '$m=1$kg', '$g=-9.81$
m/s$^2$', 'kg·m$^2$' with a middle dot); the inertia vector is written $I_{x,y,z}=[0.5, 0.1, 0.3]$ (a space after the
commas, which does not change the rendering, so the numbers are not read as thousands). Display (14): the 12-row
right-hand side vector in one $$ block with \tag{14} (bmatrix; the trailing \\ before \end{bmatrix} of the TeX dropped,
layout only); every row compared with the 220 dpi crop. Source slip kept as printed: row 8 reads
'(u_1/m) * (cos phi * sin phi - cos phi * sin psi * sin theta)', with the product 'cos phi * sin phi' (probably a
typo in the model; transcribed as printed and as in the TeX, not corrected); row 4 prints 'sin(phi)' with parentheses and the other entries without, as in the TeX.
Heading '8.3.2. Comparison between neural Koopman liftings and polynomial liftings' is printed in small caps without a
final period; level 4, written in the TeX's sentence case. Paragraph: extractor prose checked on the render
('polyno-mial', 'un-stable' closed up; 'polynomial-lifted', 'degree-3', 'open-loop', 'longer-horizon', 'contact-rich',
'reachable-set' kept); 'auto_LiRPA' (typewriter) as a code span; citation (Pan et al., 2024). Table 2: 3 columns x 11
rows plus header; cells as printed, all digits compared one by one with the 240 dpi crop and with the TeX tabular
(e.g. 135554800.971296, 0.259034); bold header markers removed. Table caption printed below the table, placed after
it, verbatim. Omitted: running header 'NATH YIN CHOU' and page number 18.
""")
