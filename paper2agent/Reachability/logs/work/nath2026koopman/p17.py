from pagelib import *
P = 17
ALG = "\n\n".join([
    r"**Algorithm 1** Online Conformalized Koopman Reachable Set (CKRS)",
    r"**Input:** Koopman model $(\phi, \psi, K_{A}, K_{B})$; true dynamics $f$ (simulator); reference trajectory $x^{\text{ref}}_{0:T}$; initial set $\mathcal{X}_0 = \mathcal{B}_\epsilon(x_0^{\text{ref}})$; RSOA confidence $1-\delta$; calibration sizes $M^{\lambda}, K^{\text{cal}}$; cost matrices $Q, R$; verification tool `auto_LiRPA`",
    r"**Output:** Conformalized Koopman reachable set $\overline{\mathcal{X}}^{1-\delta}_{0:T}$ (CKRS)",
    r"// 1. Initialization",
    r"1: $z^{\text{ref}}_{0:T} \gets \phi(x^{\text{ref}}_{0:T})$ // encode reference state trajectory",
    r"2: $u^{\text{ref}}_{0:T-1} \gets$ Equation (2) // compute feedforward control sequence",
    r"3: $G_{0:T-1} \gets$ LQR$(K_A, K_B)$ // compute LQR gains",
    r"4: $\pi(\cdot) \gets$ Equation (3) // compute lifted controller using LQR and feedforward inputs",
    r"// 2. Error bounds $\bar e_t$ via CP",
    r"5: $\mathcal{D}_E, \mathcal{D}_N \gets \texttt{GenerateCalibrationData}(M^{\lambda}, K^{\text{cal}})$",
    r"6: $\bar e_t \gets \texttt{SNSA}(\mathcal{D}_N, \mathcal{D}_E)$",
    r"// 3. Nominal KRS $\hat{\overline{\mathcal{X}}}_{0:T}$",
    r"7: $\Gamma(\cdot) \gets \psi(\texttt{PropagateLatent}(\phi(\cdot), z^{\text{ref}}, u^{\text{ref}}, G))$ // define CG",
    r"8: $\hat{\overline{\mathcal{X}}}_{0:T} \gets \texttt{AutoLiRPA}(\Gamma, \mathcal{X}_0)$ // compute KRS via CG",
    r"9: $\overline{\mathcal{X}}^{1-\delta}_{0:T} \gets \hat{\overline{\mathcal{X}}}_{0:T} \oplus \textrm{diag}(\bar e_t) \mathcal{B}_1(0)$ // 4. combine to obtain CKRS, and return",
    r"10: **return** $\overline{\mathcal{X}}^{1-\delta}_{0:T}$",
])
items = [
    figure("p0017-alg1", [88.0, 88.0, 524.0, 358.0], "Algorithm 1", "algorithm-1"),
    text("p0017-alg1-text", [90.0, 93.0, 522.0, 356.0], ALG),
    heading("p0017-b005", B(P, "p0017-b005"), "#### 8.3.1. Dynamics."),
    text("p0017-b006", B(P, "p0017-b006"),
         r"For unicycle experiments ($x \in \mathbb{R}^3$, $u \in \mathbb{R}^2$), we used the dynamics model, time-discretized via forward Euler ($dt =0.1$s)"),
    text("p0017-b007", B(P, "p0017-b007"),
         "$$\n\\dot{\\mathbf{x}}\\;=\\; f(\\mathbf{x},\\mathbf{u})=\n\\begin{bmatrix}\nu_1 \\cos(x_2) \\\\ u_1 \\sin(x_2) \\\\ u_2\n\\end{bmatrix}. \\tag{12}\n$$"),
    text("p0017-b008", B(P, "p0017-b008"),
         r"For planar quadcopter experiments ($x \in \mathbb{R}^6$, $u \in \mathbb{R}^2$), we used the parameters $m=0.5\textrm{kg}$, $g=-9.81\textrm{m/s}^2$, $I_y=0.01\textrm{kg} \cdot \textrm{m}^2$ for the dynamics model, and time-discretized with $dt = 0.05\,\mathrm{s}$:"),
    text("p0017-b009", B(P, "p0017-b009"),
         "$$\n\\dot{\\mathbf{x}}\\;=\\; f(\\mathbf{x},\\mathbf{u})=\\begin{bmatrix}\nx_4 \\\\ x_5 \\\\ x_6 \\\\ -\\frac{u_1}{m} \\sin(x_3)\\\\ g+\\frac{u_1}{m}\\cos(x_3)\\\\ \\frac{u_2}{I_y}\n\\end{bmatrix} \\tag{13}\n$$"),
    run_header(P),
    page_number(P),
]
# the extractor's fragmented algorithm items lie inside the algorithm crop
for k in ("p0017-b001", "p0017-b002", "p0017-b003", "p0017-b004"):
    b = B(P, k)
    assert 88.0 <= b[0] and b[2] <= 524.0 and 88.0 <= b[1] and b[3] <= 358.0, (k, b)
save(P, items, r"""
Compared with a 170 dpi render of PDF page 17, a 160 dpi crop of the algorithm box, and with appendix.tex (algorithmic
environment; symbols.tex renames \Require/\Ensure to 'Input:'/'Output:' and prints \Comment as blue '// ...').
Algorithm 1 (float between two horizontal rules at the top of the page): the extractor had split it into four glyph-
soup text items, all lying inside the box; replaced by one image crop 'algorithm-1' [88, 88, 524, 358] (both rules,
the title line 'Algorithm 1 Online Conformalized Koopman Reachable Set (CKRS)', Input/Output and lines 1-10 inside;
edges checked on the crop) followed by a transcription: bold title line, bold 'Input:' and 'Output:' paragraphs, one
paragraph per printed line with the printed line numbers 1-10. The comments are printed in blue and start with '//'
(kept as '//'; not '#'). The three section comments ('// 1. Initialization', '// 2. Error bounds e-bar_t via CP',
'// 3. Nominal KRS ...') are printed on their own unnumbered lines at the statement indentation; the algorithm has no
loops, so no nesting indentation is needed; line 9 carries the comment '// 4. combine to obtain CKRS, and return'.
Procedure names in typewriter (GenerateCalibrationData, SNSA, PropagateLatent, AutoLiRPA) written with \texttt inside
the math as in the TeX; 'auto_LiRPA' as a code span; 'LQR' and 'Equation (2)', 'Equation (3)' as printed; bold
'return'. Heading '8.3.1. Dynamics.' printed in small caps with the final period: level 4, written in title case with
the printed numbering and period. Unicycle sentence: mathematics from the TeX ('dt =0.1' followed by plain 's' as
typed); display (12) with \tag{12} (bmatrix, period after the bracket as printed). Planar quadcopter sentence: units
typed \textrm{kg}, \textrm{m/s}^2, \textrm{kg} \cdot \textrm{m}^2 as in the TeX, 'g = -9.81 m/s^2' (negative, as
printed); display (13) with \tag{13}. Omitted: running header (short title) and page number 17.
""")
