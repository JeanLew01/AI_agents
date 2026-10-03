from pagelib import *
o = orig(1)
B = lambda k: o[k]["bbox"]

TITLE = "PCA-DDReach: Efficient Statistical Reachability Analysis of Stochastic Dynamical Systems via Principal Component Analysis"

items = [
    omit("p0001-b000", B("p0001-b000"), "arXiv:2505.14935v1 [cs.RO] 20 May 2025",
         "Vertical arXiv stamp in the left margin ('arXiv:2505.14935v1 [cs.RO] 20 May 2025'); page furniture. The version and date are recorded in the conversion notes."),
    heading("p0001-b001", B("p0001-b001"), "# " + TITLE),
    text("p0001-b002", [88.0, 170.0, 524.0, 195.0],
         "**Navid Hashemi** navidhas@usc.edu\n\n*University of Southern California, Los Angeles, California, United States*"),
    text("p0001-b005", [88.0, 212.0, 524.0, 237.0],
         "**Lars Lindemann** llindema@usc.edu\n\n*University of Southern California, Los Angeles, California, United States*"),
    text("p0001-b008", [88.0, 255.0, 524.0, 282.0],
         "**Jyotirmoy Deshmukh** jdeshmuk@usc.edu\n\n*University of Southern California, Los Angeles, California, United States*"),
    heading("p0001-b011", B("p0001-b011"), "## Abstract"),
    text("p0001-b012", B("p0001-b012"),
         "This study presents a scalable data-driven algorithm designed to efficiently address the challenging problem of reachability analysis. Analysis of cyber-physical systems (CPS) relies typically on parametric physical models of dynamical systems. However, identifying parametric physical models for complex CPS is challenging due to their complexity, uncertainty, and variability, often rendering them as black-box oracles. As an alternative, one can treat these complex systems as black-box models and use trajectory data sampled from the system (e.g., from high-fidelity simulators or the real system) along with machine learning techniques to learn models that approximate the underlying dynamics. However, these machine learning models can be inaccurate, highlighting the need for statistical tools to quantify errors. Recent advancements in the field include the incorporation of statistical uncertainty quantification tools such as conformal inference (CI) that can provide probabilistic reachable sets with provable guarantees. Recent work has even highlighted the ability of these tools to address the case where the distribution of trajectories sampled during training time are different from the distribution of trajectories encountered during deployment time. However, accounting for such distribution shifts typically results in more conservative guarantees. This is undesirable in practice and motivates us to present techniques that can reduce conservatism. Here, we propose a new approach that reduces conservatism and improves scalability by combining conformal inference with Principal Component Analysis (PCA). We show the effectiveness of our technique on various case studies, including a 12-dimensional quadcopter and a 27-dimensional hybrid system known as the powertrain."),
    text("p0001-b013", B("p0001-b013"),
         "**Keywords:** Reachable set estimation, Conformal Inference, Principal Component Analysis"),
    heading("p0001-b014", B("p0001-b014"), "## 1 Introduction"),
    text("p0001-b015", B("p0001-b015"),
         "System verification tools are crucial for ensuring correctness prior to testing, implementation, or deployment, particularly in expensive, high-risk, or safety-critical systems Zhang et al. (2023); Schilling et al. (2022); Komendera et al. (2012). In real-world implementations, we"),
    omit("p0001-b016", B("p0001-b016"), "1",
         "Printed page number 1 centred at the foot of the page; page furniture, checked on the 170 dpi render."),
]

save(1, items, r"""
Compared with the 170 dpi render. Title heading set identical to the bundle title (three printed lines joined). The extractor had turned
the three author names into '###' headings and split names, e-mail addresses and affiliations into separate items; they are now three
text items (bold name + e-mail on the first line, italic affiliation on the second), no headings. E-mail addresses are printed in small
caps (NAVIDHAS@USC.EDU etc.) and written in lower case as in the TeX source. Bold markers removed from the 'Abstract' and '1 Introduction'
headings (printed numbering '1 Introduction' kept, no dot after the number). Abstract compared sentence by sentence with the TeX source
and the render: identical; the line-wrap hyphen of 'identify-ing' is removed, the compound hyphens of data-driven, cyber-physical,
black-box, high-fidelity, 12-dimensional, 27-dimensional are kept. Keywords line kept with its printed bold label. Citations are printed
in natbib author-year form without parentheses around the group ('Zhang et al. (2023); Schilling et al. (2022); Komendera et al. (2012)')
and are kept exactly so. The last paragraph is cut by the page break after 'In real-world implementations, we'; the first item of page 2
continues it with join_previous 'space'. Omitted: the vertical arXiv stamp in the left margin and the page number 1. No mathematics on
this page.
""")
