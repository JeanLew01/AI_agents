from pagelib import *

items = [
    omit("p0001-b000", [18.0, 213.0, 36.0, 560.0], "arXiv:1702.06902v1 [cs.SY] 22 Feb 2017",
         "Vertical arXiv identifier stamp in the left margin ('arXiv:1702.06902v1 [cs.SY] 22 Feb 2017'); page furniture, not part of the paper. The version it states is recorded in the conversion notes."),
    heading("p0001-b001", [140.0, 163.0, 471.0, 200.0],
            "# DryVR: Data-driven verification and compositional reasoning for automotive systems"),
    text("p0001-b002", [188.0, 224.0, 424.0, 258.0],
         "Chuchu Fan, Bolun Qi, Sayan Mitra, Mahesh Viswanathan"),
    text("p0001-b004", [194.0, 267.0, 417.0, 278.0],
         "University of Illinois at Urbana-Champaign"),
    heading("p0001-b005", [285.0, 306.0, 326.0, 314.0], "## Abstract"),
    text("p0001-b006", [158.0, 321.0, 453.0, 454.0],
         "We present the DryVR framework for verifying hybrid control systems that are described by a combination of a black-box simulator for trajectories and a white-box transition graph specifying mode switches. The framework includes (a) a probabilistic algorithm for learning sensitivity of the continuous trajectories from simulation data, (b) a bounded reachability analysis algorithm that uses the learned sensitivity, and (c) reasoning techniques based on simulation relations and sequential composition, that enable verification of complex systems under long switching sequences, from the reachability analysis of a simpler system under shorter sequences. We demonstrate the utility of the framework by verifying a suite of automotive benchmarks that include powertrain control, automatic transmission, and several autonomous and ADAS features like automatic emergency braking, lane-merge, and auto-passing controllers."),
    heading("p0001-b007", [133.0, 473.0, 247.0, 484.0], "## 1 Introduction"),
    text("p0001-b008", [133.0, 497.0, 478.0, 620.0],
         "The starting point of existing hybrid system verification approaches is the availability of nice mathematical models describing the transitions and trajectories. This central conceit severely restricts the applicability of the resulting approaches. Real world control system “models” are typically a heterogeneous mix of simulation code, differential equations, block diagrams, and hand-crafted look-up tables. Extracting clean mathematical models from these descriptions is usually infeasible. At the same time, rapid developments in Advanced Driving Assist Systems (ADAS), autonomous vehicles, robotics, and drones now make the need for effective and sound verification algorithms stronger than ever before. The DryVR framework presented in this paper aims to narrow the gap between sound and practical verification for control systems."),
    text("p0001-b009", [133.0, 625.0, 478.0, 668.0],
         "**Model assumptions** Consider an ADAS feature like automatic emergency braking system (AEB). The high-level logic deciding the timing of when and for how long the brakes are engaged after an obstacle is detected by sensors is implemented in a relatively clean piece of code and this logical module can be"),
    pageno(1, [303.0, 696.0, 309.0, 703.0]),
]

save(1, items, r"""
Compared with a 190-dpi render of the text block and with intro.tex / main2.tex. Title as printed on this arXiv version (sentence case; 'DryVR' is set in small caps in the PDF, written 'DryVR' here and everywhere in the text); it is the single # heading and equals the bundle title. Author block: the four names are printed on two centred lines without separators (three names, then 'Mahesh Viswanathan'); written on one line with commas added as separators; the affiliation line follows. No emails, footnotes or acknowledgements are printed on this page. 'Abstract' is printed as a centred bold word: kept as ## heading; abstract text compared word by word with main2.tex (line-wrap hyphens removed: sys-tems, sensi-tivity, com-position, switch-ing, veri-fying). '1 Introduction' is a numbered section: ## heading with the printed number. First paragraph compared with intro.tex (line-wrap hyphens removed: avail-ability, trajecto-ries, be-fore; 'hand-crafted' and 'look-up' are real hyphens). 'Model assumptions' is a run-in bold paragraph title (\paragraph in the TeX): kept as bold run-in text, as are all such paragraph titles in this paper. The last sentence continues on page 2 (join there). Omitted: the vertical arXiv stamp in the left margin and the page number 1.
""")
