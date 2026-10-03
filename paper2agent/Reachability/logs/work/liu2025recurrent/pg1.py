#!/usr/bin/env python3
from pagelib import write_page

NOTES = r"""
Compared item by item with the 170 dpi render of PDF page 1 and with the authors' TeX source (main.tex).
The vertical arXiv stamp in the left margin is set to omit. The title is the single level-1 heading (bold
markers of the extractor removed) and is identical to the bundle title. Author line kept as printed. The
two unnumbered first-page footnotes (the \thanks notes printed at the bottom of the left column:
affiliation with e-mail addresses, and funding) are kept verbatim as two text items placed directly after
the author line instead of at the end of the page, because the last paragraph of this page (Notation)
continues on page 2 and must stay last for the cross-page join; they carry no printed marker, so no
marker was added. The e-mail addresses are printed in typewriter type as 'jliu376@jh.edu,
mallada@jhu.edu' (first domain 'jh.edu' is what the PDF and the TeX source print; kept). The run-in bold
label 'Abstract—' is represented by a '## Abstract' heading and the bold face of the abstract was
dropped. 'parellizable' in the last sentence of the abstract is the authors' spelling (PDF and TeX) and
is kept. 'I. INTRODUCTION' (small caps) written in title case. Line-wrap hyphens removed
(applications, solving, reachability, computational, stability); real compound hyphens kept
(safety-critical, Hamilton-Jacobi, HJ-reachability, Sum-of-Squares, high-dimensional, data-driven,
learning-based, Koopman-based, control-invariant, finite-time, sampling-based, GPU-friendly,
recurrence-based, Information-theoretically, tau-backward). The second paragraph of the Introduction
runs from the bottom of the left column into the right column ('offering efficiency but | with safety
guarantees ...') and was merged into one item. Citation numbers [1]-[13] and the section numbers II-VII
in the outline paragraph were resolved from the page image. Inline math ($\tau$, $\|\cdot\|$,
$\mathbb{R}^n$, $x$, $r$) written in LaTeX from the TeX source. 'Notation:' is a run-in italic paragraph
head (\paragraph*), not a section heading; it is kept as italic run-in text. Its sentence is split by the
page break ('... centered at x is defined | as B_r(x) := ...'); the page-2 item continues it with
join_previous 'space'.
"""

write_page(1, NOTES, [
    ("p0001-b000", "omit", ("p0001-b000",), "", {"reason": "Vertical arXiv stamp in the left margin ('arXiv:2510.02127v1 [eess.SY] 2 Oct 2025'); page furniture, the source version is recorded in the conversion notes."}),
    ("p0001-b001", "heading", ("p0001-b001",), "# Recurrent Control Barrier Functions: A Path Towards Nonparametric Safety Verification", {}),
    ("p0001-b002", "text", ("p0001-b002",), "Jixian Liu and Enrique Mallada", {}),
    ("p0001-b007", "text", ("p0001-b007",),
     "J. Liu and E. Mallada are with the Department of Electrical and Computer Engineering, Johns Hopkins University, MD 21218, U.S.A. `jliu376@jh.edu, mallada@jhu.edu`.", {}),
    ("p0001-b008", "text", ("p0001-b008",),
     "This work was supported by NSF through grant Global Center 2330450, and Johns Hopkins University Institute for Assured Autonomy.", {}),
    ("p0001-abstract-h", "heading", [53.0, 163.0, 110.0, 172.0], "## Abstract", {}),
    ("p0001-b003", "text", ("p0001-b003",),
     "Ensuring the safety of complex dynamical systems often relies on Hamilton-Jacobi (HJ) Reachability Analysis or Control Barrier Functions (CBFs). Both methods require computing a function that characterizes a safe set that can be made (control) invariant. However, the computational burden of solving high-dimensional partial differential equations (for HJ Reachability) or large-scale semidefinite programs (for CBFs) makes finding such functions challenging. In this paper, we introduce the notion of Recurrent Control Barrier Functions (RCBFs), a novel class of CBFs that leverages a recurrent property of the trajectories, i.e., coming back to a safe set, for safety verification. Under mild assumptions, we show that the RCBF condition holds for the signed-distance function, turning function design into set identification. Notably, the resulting set need not be invariant to certify safety. We further propose a data-driven nonparametric method to compute safe sets that is massively parellizable, and trades off conservativeness against computational cost.", {}),
    ("p0001-b004", "heading", ("p0001-b004",), "## I. Introduction", {}),
    ("p0001-b005", "text", ("p0001-b005",),
     "Safety is a fundamental requirement in the control of dynamical systems, particularly in safety-critical applications such as robotics, autonomous vehicles, etc. Safety of the system is typically enforced via Hamilton-Jacobi (HJ) reachability analysis [1] or Control Barrier Functions (CBFs) [2], both of which build a function whose superlevel set is a control invariant safe set. Unfortunately, despite the popularity of these methods, their application relies on the computation of the value function or CBF, which presents significant challenges. HJ-reachability analysis requires solving partial differential equations, which suffers from the curse of dimensionality [3]. The synthesis of valid CBFs often requires solving a Sum-of-Squares (SOS) optimization problem, which is also computationally demanding when applied to high-dimensional systems [4], [5].", {}),
    ("p0001-b006", "text", ("p0001-b006", "p0001-b009"),
     "To reduce the computational burden, some data-driven methods have been proposed. DeepReach greatly improves computational efficiency for high-dimensional HJ reachability by using neural PDE solvers, but its learning-based approximation limits interpretability despite strong empirical performance [6]. [7] accelerates the synthesis of CBF by utilizing Koopman-based matrix multiplications, though at the expense of losing strict guarantees due to operator approximation. [8] constructs control-invariant safe sets from hard constraints via data-driven CBFs, offering efficiency but with safety guarantees limited by uneven or sparse sampling quality.", {}),
    ("p0001-b010", "text", ("p0001-b010",),
     r"In this paper, we build a framework to trade off the computational complexity of finding safe control sets with the level of conservativeness of the solution, which has theoretical safety guarantees. A key insight of the proposed approach is to substitute the invariance property that Reachability and CBF methods aim to guarantee with a more flexible notion called recurrence [9], [10]. A set is ($\tau$-) recurrent if every trajectory that leaves the set comes back to it (within $\tau$ units of time) infinitely many times. Recurrence has emerged as a practical surrogate for invariance in analysis and verification—e.g., for regions of attraction [11], stability [9], and safety verification [10]. Information-theoretically, enforcing (control) recurrence demands lower data rates than invariance [12] and can often be achieved from finite trajectories [13].", {}),
    ("p0001-b011", "text", ("p0001-b011",),
     r"Building on this literature, we extend the notion of Recurrent Barrier Functions proposed in [10] to account for the addition of controls, thus introducing Recurrent Control Barrier Functions (RCBFs). RCBFs relax strict invariance by requiring a finite-time ($\tau$) return to a safe set—conditions met by signed distance functions of given sets—while preserving safety as long as the set excludes the $\tau$-backward reachable tube of the unsafe region. We devise a nonparametric, sampling-based procedure to synthesize RCBFs and verify safety quickly and at scale. To do so, we introduce a robust RCBF condition that uses trajectory data to certify a neighborhood of the initial state; an adaptive sampling method and data-driven exploration remove the need for large optimization programs. The method is GPU-friendly and lets practitioners trade conservativeness for computation without compromising safety.", {}),
    ("p0001-b012", "text", ("p0001-b012",),
     "The remainder of this paper is organized as follows. Section II reviews preliminaries on HJ reachability analysis and CBFs. Section III introduces the definition of RCBFs, extending classical CBFs through recurrence-based safety conditions. Section IV develops the robust conditions that allow for data-driven verification of the RCBF property on a neighborhood of trajectory samples. Section V integrates the robust conditions into a sampling-based method for nonparametric safety verification that actively chooses where to sample based on prior outcomes. Section VI provides numerical validations demonstrating the effectiveness of the proposed approach. Section VII concludes the paper and outlines directions for future work.", {}),
    ("p0001-b013", "text", ("p0001-b013",),
     r"*Notation:* $\|\cdot\|$ is an arbitrary norm on $\mathbb{R}^n$. For $x \in \mathbb{R}^n$ and $r > 0$, the closed ball of radius $r$ centered at $x$ is defined", {}),
])
