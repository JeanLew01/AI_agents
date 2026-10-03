from pt import *
t2 = [
 ["Benchmark", "LRT-NG", "Flow*", "CAPD", "LRT", "GoTube (90%)", "GoTube (99%)"],
 ["Brusselator", "1.5e-4", "9.8e-5", "3.6e-4", "6.1e-4", "8.6e-5", "8.6e-5"],
 ["Van Der Pol", "4.2e-4", "3.5e-4", "1.5e-3", "3.5e-4", "3.5e-4", "3.5e-4"],
 ["Robotarm", "7.9e-11", "8.7e-10", "1.1e-9", "Fail", "2.5e-10", "2.5e-10"],
 ["Dubins Car", "0.131", "4.5e-2", "0.1181", "385", "2.5e-2", "2.6e-2"],
 ["Cardiac Cell", "3.7e-9", "1.5e-8", "4.4e-8", "3.2e-8", "4.2e-8", "4.3e-8"],
 ["CartPole-v1+LTC", "4.49e-33", "Fail", "Fail", "Fail", "2.6e-37", "4.9e-37"],
 ["CartPole-v1+CTRNN", "3.9e-27", "Fail", "Fail", "Fail", "9.9e-34", "1.2e-33"],
]
t3 = [
 ["Benchmark", "CartPole-v1+CTRNN", "CartPole-v1+CTRNN", "CartPole-v1+LTC", "CartPole-v1+LTC"],
 ["Time horizon", "1s", "10s", "0.35s", "10s"],
 ["LRT", "Blowup", "Blowup", "Blowup", "Blowup"],
 ["CAPD", "Blowup", "Blowup", "Blowup", "Blowup"],
 ["Flow*", "Blowup", "Blowup", "Blowup", "Blowup"],
 ["LRT-NG", "3.9e-27", "Blowup", "4.5e-33", "Blowup"],
 ["GoTube (ours)", "8.8e-34", "1.1e-19", "4.9e-37", "8.7e-21"],
]
items = [
 T("The specific reachtubes and the chaotic nature of hundred executions of Dubin’s car are shown in Figure 3. As one can see, the GoTube reachtube extends to a much longer time horizon, which we fixed at 40s. All other tools blew up before 20s. For the two problems involving neural networks, GoTube produces significantly tighter reachtubes.", L, 503, 568, join="space"),
 C(r"Table 2: Comparison of GoTube (using tightness bound $\mu=1.1$) to existing reachability methods. The first five benchmarks concern classical dynamical systems, whereas the two bottom rows correspond to time-continuous RNN models (LTC= liquid time-constant networks) in a closed feedback loop with an RL environment (Hasani et al. 2021; Vorbach et al. 2021). The numbers show the volume of the constructed tube. Lower is better; best number in bold.", L, 303.5, 390),
 TAB("Table 2", "table-2", [53, 398, 294, 481], t2),
 T(r"*Conversion note on Table 2 (not printed text): the printed header 'GoTube' spans the two columns '(90%)' and '(99%)' and is repeated in the combined column names. Cells printed in bold: Brusselator, GoTube (99%) 8.6e-5; Van Der Pol, Flow\* 3.5e-4 and GoTube (99%) 3.5e-4; Robotarm, LRT-NG 7.9e-11; Dubins Car, GoTube (99%) 2.6e-2; Cardiac Cell, LRT-NG 3.7e-9; CartPole-v1+LTC, GoTube (99%) 4.9e-37; CartPole-v1+CTRNN, GoTube (99%) 1.2e-33. A horizontal rule separates the first five benchmarks from the two CartPole rows.*", L, 481.5, 485),
 FIG("Figure 3", "figure-3", [125, 48, 500, 222]),
 C(r"Figure 3: Visualization of the reachtubes constructed for the Dubin’s car model with various reachability methods. While the tubes computed by existing methods (LRT-NG, Flow\* and CAPD) explode at $t \approx 20s$ (this moment is shown on the right side of the figure) due to the accumulation of over-approximation errors (the infamous wrapping effect), GoTube can keep tight bounds beyond $t > 40s$ for a 99% confidence level (using 20000 samples, $\mu=1.1$ and runtime of one hour). Note also the chaotic nature of 100 executions.", (54, 558), 229, 282.5),
 T(r"*Conversion note on Figure 3 (not printed text): the annotations inside the figure read 'GoTube constructs reachtubes up to an arbitrary time-horizon' (left panel, 3-D plot over $x_1$, $x_2$ and Time (s)) and 'GoTube constructs as-tight-as possible reachtubes' (right, magnified circular inset); the legend entries are LRT-NG, Flow\*, CAPD, GoTube (ours) and Sample traces.*", (54, 558), 283, 286),
 H("### GoTube provides safety bounds up an arbitrary time horizon", (54, 276), 579, 602),
 T(r"In our second experiment, we evaluate for how long GoTube and existing methods can construct a reachtube before exploding due to overapproximation errors. To do so, we extend the benchmark setup by increasing the time horizon for which the tube should be constructed, use tightness bound $\mu=1.1$ and set a 95% confidence level, that is, probability of being conservative.", L, 607, 682.5),
 T("The results in Table 3 demonstrate that GoTube produces significantly longer reachtubes than all considered state-of-the-art approaches, without suffering from severe overapproximation errors. Particularly, Figure 1 visualizes the difference to the existing methods and overapproximation margins for two example dimensions of the CartPole-v1 environment and its CT-RNN controller.", L, 684, 705),
 C("Table 3: Results of the extended benchmark by longer time horizons. The numbers show the volume of the constructed tube, “Blowup” indicates that the method produced `Inf` or `NaN` values due to a blowup. Lower is better; the best method is shown in bold.", R, 303.5, 357),
 TAB("Table 3", "table-3", [320, 367, 555, 450], t3),
 T(r"*Conversion note on Table 3 (not printed text): the table has two header rows; the printed headers 'CartPole-v1+CTRNN' and 'CartPole-v1+LTC' each span two columns and are repeated, and the second row gives the time horizon of each column (1s, 10s, 0.35s, 10s). The four numbers of the last row, GoTube (ours), are printed in bold.*", R, 451, 455),
 H("### GoTube can trade runtime for reachtube tightness", (319.5, 554), 537, 548),
 T(r"In our last experiment, we introduced a new set of benchmark models entirely based on continuous-time recurrent neural networks. The first model is an unstable linear dynamical system of the form $\dot{x} = Ax + Bu$ that is stabilized by a CT-RNN policy via actions $u$. The second model corresponds to the inverted pendulum environment, which is similar to the CartPole environment but differs in that the control actions are applied via a torque vector on the pendulum directly instead of moving a cart. The CT-RNN policies for these two environments were trained using deep RL. Our third new benchmark model concerns the analysis of the learned dynamics of a CT-RNN trained on supervised data. In particular, by using the reachability frameworks, we aim to assess if the learned network expressed oscillatory", R, 552, 705),
]
notes = r"""
Compared with a 170 dpi render of PDF page 6, a 330 dpi crop of Table 2, a 260 dpi crop of Table 3, a 130 dpi crop of Figure 3 with margins, and with the authors' TeX source; TeX and PDF agree.
Layout: Figure 3 spans both columns at the top; below it the left column prints the caption of Table 2, Table 2, the end of the paragraph begun on page 5, the subsection heading 'GoTube provides safety bounds up an
arbitrary time horizon' and two paragraphs; the right column prints the caption of Table 3, Table 3, the end of the left column's last paragraph, the heading 'GoTube can trade runtime for reachtube tightness' and one
paragraph. Item order here: (1) the continuation 'The specific reachtubes ...' of the page-5 paragraph 'The results are shown in Table 2. ...' (same paragraph in the TeX source; join_previous=space);
(2) Table 2 with its caption (printed above the table) and Figure 3 with its caption, both referred to in that paragraph; (3) the second subsection with its two paragraphs, the second of which runs from the left
column into the right column ('state-of- | the-art approaches') and is one item; (4) Table 3 with its caption, referred to in that paragraph; (5) the third subsection.
Table 2: 7 columns, header plus 7 benchmark rows; every value read on the 330 dpi crop and compared with the TeX tabular (identical). The two-row header (GoTube over '(90%)' and '(99%)') is flattened to
'GoTube (90%)' and 'GoTube (99%)'. Bold cells are not marked in the cells and are listed in a labelled conversion note placed after the table (eight bold cells; as printed, in the Dubins Car row and the two CartPole rows the bold GoTube (99%) value is larger than the GoTube (90%) value next to it,
in the Brusselator row the two GoTube values are equal and only the (99%) one is bold, and in the Van Der Pol row 3.5e-4 is printed four times but bold only twice).
Table 3: 5 columns; two header rows kept as the first two rows (parent headers repeated); every cell read on the 260 dpi crop and compared with the TeX tabular (identical); bold cells listed in a conversion note.
The extractor's versions of both tables had split header cells ('GoT'/'ube', 'CartPole-v'/'1'/'+CTRNN') and were rebuilt.
Figure 3 is one crop containing both panels, the legend and the two in-figure annotation lines; the extractor had split it into three figure items. Its bbox edges were checked on the wider 130 dpi crop
(legend at the left, circular inset at the right, tick labels at the bottom). The in-figure annotations are repeated in a labelled conversion note after the caption so that they are searchable.
Captions: math of the Figure 3 caption ($t \approx 20s$, $t > 40s$, $\mu=1.1$) from the TeX source ('s' is inside the math in the source and is printed in italics); 'Inf' and 'NaN' in the Table 3 caption are printed in
typewriter type and written as code spans; curly quotes around Blowup as printed. Percentages as printed ('99%', '95%').
The two subsection headings are real (bold, larger type; TeX \subsection) and are level 3; the extractor had them at level 1.
Kept as printed: 'Dubin’s car' (page 2 has 'Dubins Car'), 'hundred executions', 'safety bounds up an arbitrary time horizon' (heading, no 'to'), 'LTC= liquid time-constant networks', 'Results of the extended
benchmark by longer time horizons', 'the difference to the existing methods', 'expressed oscillatory'.
Line-wrap hyphens removed (be-fore, ex-ploding, ex-tend, overap-proximation, dif-ference, mar-gins, envi-ronment, bench-mark, dy-namical, cor-responds, pen-dulum, poli-cies); real compounds kept (state-of-the-art,
time-continuous, time-constant, over-approximation, CartPole-v1, CT-RNN, continuous-time).
The last paragraph ends mid-sentence ('... expressed oscillatory') and continues on page 7 (joined there). No page number or running head.
"""
write(6, items, notes)
