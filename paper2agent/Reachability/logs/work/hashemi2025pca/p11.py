from pagelib import *
o = orig(11)
B = lambda k: o[k]["bbox"]

rows = [
    ["Exp #:", "Specification: δ", "Specification: τ", "Training: #", "Training: avg runtime", "Training: |T^trn|",
     "Surrogate Reachability: #", "Surrogate Reachability: avg runtime(method)", "Inflating Hypercube: runtime", "Inflating Hypercube: |R^calib|"],
    ["1", "99.99%", "0", "100", "39.6 sec", "42,000", "100", "1.43 sec (E)", "2.08 sec", "20,000"],
    ["2", "99.99%", "0", "451", "33.65 sec", "20,000", "4501", "0.030 sec (E)", "116.58 sec", "20,000"],
    ["3", "95%", "4%", "400", "40.6 sec", "10,000", "4000", "0.064 sec (A)", "142.02 sec", "10,000"],
]

items = [
    table("p0011-b000", [94.0, 90.0, 531.0, 165.5], "Table 1", "table-1", rows),
    caption("p0011-b001", B("p0011-b001"),
            "Table 1: Shows details of the experiments. The models are trained in parallel with 18 CPU workers. Thus, the average training runtime may vary by selecting different number of workers. The words E, and A represent exact-star and approx-star, respectively."),
    text("p0011-note", [94.0, 90.0, 531.0, 92.0],
         r"""Conversion note on Table 1 (not part of the paper): the table is printed with two header rows. The group headers 'Specification' (columns $\delta$, $\tau$), 'Training' (columns #, avg runtime, $|\mathcal{T}^{\mathsf{trn}}|$), 'Surrogate Reachability' (columns #, avg runtime(method)) and 'Inflating Hypercube' (columns runtime, $|\mathcal{R}^{\mathsf{calib}}|$) are repeated in front of each column name in the CSV; 'T^trn' and 'R^calib' in the column names stand for the training dataset $\mathcal{T}^{\mathsf{trn}}$ and the calibration dataset $\mathcal{R}^{\mathsf{calib}}$, so those two columns give the dataset sizes. The dataset sizes are printed in math mode with a gap after the comma and are written here as plain thousands."""),
    heading("p0011-b002", B("p0011-b002"), "### 4.1 12-Dimensional Quadcopter"),
    text("p0011-b003", B("p0011-b003"), X(
         r"""We consider the 12-dimensional quadcopter system under stochastic conditions for two different case studies. Trajectories are simulated using two ODE models from Hashemi et al. (2024b) and Hashemi et al. (2024a) as our simulators. The state variables include the quadcopter’s position $(x_1, x_2, x_3)$, velocity $(x_4, x_5, x_6)$, Euler angles $(x_7, x_8, x_9)$ representing roll, pitch, and yaw angles, and angular velocities $(x_{10}, x_{11}, x_{12})$. We also include zero mean additive Gaussian process noise $v \sim \gaussian(0_{12\times1}, \Sigma_v)$ to the simulators with covariance $\Sigma_v = \mathbf{diag}\left( [0.05 \times \vec{1}_{1\times6} ,\ 0.01\times \vec{1}_{1\times6]}]^2 \right)$. In both examples, the set of initial states $\statee_0 \in \init$ is taken from the cited papers, with the distribution $\statee_0 \sim \mathcal{W}$ being uniform.""")),
    heading("p0011-b004", B("p0011-b004"), "### 4.2 27-Dimensional Powertrain"),
    text("p0011-b005", B("p0011-b005"), X(
         r"""We use the powertrain system proposed by Althoff and Krogh (2012) as our simulator, which is a hybrid system with three modes. To introduce stochastic conditions, we add zero-mean Gaussian process noise, $v \sim \gaussian(\vec{0}_{27\times1}, \Sigma_v)$, where $\Sigma_v = \mathbf{diag}\left( 10^{-5}\times \vec{1}_{1\times27} \right)$, to their simulator, defining the distribution $\trajsim_{\statee_0}\sim \distzero$. This system is highly sensitive to noise, which is a key reason we addressed it in this paper. For example, Figure 6 shows the angular velocity of the last rotating mass, $x_{27}$, both with and without noise. Following Althoff and Krogh (2012), we simulate trajectories with a sampling time of $\delta t = 0.0005$ over a horizon of $2$ seconds ($\horizon = 4000$), and consider their set of initial states $\init$ $^{6}$. We also define the trajectory division setting as $N=4000$, $T_q=1, q\in[N]$. The ReLU NN models are with structure $[27, 54, 27]$. To reduce the training runtime, we again follow the analytical interpolation strategy we introduced for Experiment 2.""")),
    text("p0011-b008", B("p0011-b008"), X(
         r"""Footnote 6: In this case the set $\init$ proposed in Althoff and Krogh (2012) is a large and high dimensional set, thus the exact star does not scale, and we are restricted to utilized approx star for surrogate reachability.""")),
    heading("p0011-b006", B("p0011-b006"), "## 5 Acknowledgements"),
    text("p0011-b007", B("p0011-b007"),
         "This work was partially supported by the National Science Foundation through the following grants: CAREER award (SHF-2048094), CNS-1932620, CNS-2039087, FMitF-1837131, CCF-SHF-1932620, IIS-SLES-2417075, funding by Toyota R&D and Siemens Corporate Research through the USC Center for Autonomy and AI, an Amazon Faculty Research Award, and the Airbus Institute for Engineering Research. This work does not reflect the views or positions of any organization listed."),
    omit("p0011-b009", B("p0011-b009"), "11",
         "Printed page number 11 centred at the foot of the page; page furniture, checked on the 170 dpi render."),
]

save(11, items, r"""
Compared with the 170 dpi render, a 300 dpi crop of Table 1 with its caption, a 260 dpi crop of Sections 4.1-4.2, a 500 dpi crop of
the $\Sigma_v$ line of Section 4.1, and the TeX source (sections/Experiments.tex, main file for Section 5). Table 1 (printed at the top
of the page, directly after the paragraph of page 10 that cites it) is converted to a CSV: all 30 data cells and the two header rows
were read on the 300 dpi crop and agree with the TeX tabular. The two printed header rows are combined ('Specification: δ', ...,
'Inflating Hypercube: |R^calib|'); cells are plain strings with the printed precision and units ('39.6 sec', '0.030 sec (E)',
'99.99%'); the dataset sizes are printed in math mode as '42, 000', '20, 000', '10, 000' with a gap and are written '42,000' etc.
A separate item after the caption, marked 'Conversion note on Table 1 (not part of the paper)', explains the combined headers; it is
not source text (its bbox is a thin strip inside the table area). The table bbox was measured with an ink profile (rules from 92.6 to
162.9 pt, caption from 168.9 pt; the table is wider than the text block and reaches x = 528.6 pt). Caption verbatim ('The words E,
and A represent ...' as printed). Headings: '4.1 12-Dimensional Quadcopter' (the '12' is math, not bold, in the print), '4.2
27-Dimensional Powertrain' (###), '5 Acknowledgements' (##; in this arXiv version the Acknowledgements are a numbered section placed
before the Conclusion). Math from the TeX source, checked on the crops. SOURCE TYPO KEPT: in Section 4.1 the covariance is printed
$\Sigma_v=\mathbf{diag}([0.05\times\vec{1}_{1\times6},\ 0.01\times\vec{1}_{1\times6]}]^2)$ with a stray ']' inside the second
subscript (confirmed at 500 dpi; same in the TeX). \vec prints an arrow in this class (checked on the crop): $\vec{1}$, $\vec{0}$;
the mean of the first noise is printed $0_{12\times1}$ without arrow, that of the second $\vec{0}_{27\times1}$ with arrow. Section 4.2:
$\Sigma_v=\mathbf{diag}(10^{-5}\times\vec{1}_{1\times27})$, $\delta t=0.0005$, horizon of 2 seconds ($\mathrm{K}=4000$), $N=4000$,
$T_q=1$, structure $[27, 54, 27]$ (written with spaces after the commas), 'Figure 6' as printed. 'ReLU' printed upright, written as
plain text. Footnote 6 (mark after 'initial states $\mathcal{I}$', printed at the foot of the page) is placed after the paragraph of
Section 4.2 that carries its mark; 'restricted to utilized approx star' is printed so. Acknowledgements: the six grant numbers were
compared digit by digit with the render; 'CCF-SHF-1932620' is broken after 'CCF-' at a line end (real hyphen). Omitted: page number 11.
""")
