from pagelib import *

P = 1
GITHUB = "https://github.com/Mahmoud-Selim/Safe-Reinforcement-Learning-for-Black-Box-Systems-Using-Reachability-Analysis"

items = furniture(P) + [
    omit("p0001-arxiv", [14.0, 200.0, 40.0, 566.0], "arXiv:2204.07417v2 [cs.RO] 21 Nov 2022",
         "Vertical arXiv stamp in the left margin ('arXiv:2204.07417v2 [cs.RO] 21 Nov 2022'); page furniture, the "
         "version is recorded in the conversion notes."),
    heading("p0001-b003", B(P, "b003"), "# Safe Reinforcement Learning Using Black-Box Reachability Analysis"),
    text("p0001-b004", B(P, "b004"),
         r"Mahmoud Selim $^{1}$, Amr Alanwar $^{2}$, Shreyas Kousik $^{3}$, Grace Gao $^{3}$, Marco Pavone $^{3}$, and Karl H. Johansson $^{4}$"),
    text("p0001-footnotes", B(P, "b011", "b012", "b013", "b014", "b015", "b016"),
         "Footnote: Manuscript received: Feb 24, 2022; Revised: May 11, 2022; Accepted: June 12, 2022\n\n"
         "Footnote: This paper was recommended for publication by Editor Jens Kober upon evaluation of the Associate Editor and Reviewers’ comments\n\n"
         "Footnote: This work was supported by the Swedish Research Council, and the Knut and Alice Wallenberg Foundation. Toyota Research Institute provided funds to support this work. The NASA University Leadership initiative (grant #80NSSC20M0163) provided funds to assist the authors with their research, but this article solely reflects the opinions and conclusions of its authors and not any NASA entity.\n\n"
         "Footnote: $^{1}$Ain Shams University, Cairo, Egypt. $^{2}$Jacobs University, Bremen, Germany. $^{3}$Stanford University, Stanford, CA, USA. $^{4}$KTH Royal Institute of Technology, Stockholm, Sweden. Corresponding author: `mahmoud.selim@eng.asu.edu.eg`.\n\n"
         "Footnote: Digital Object Identifier (DOI): see top of this page"),
    heading("p0001-abstract-h", [58.0, 177.0, 100.0, 186.0], "## Abstract"),
    text("p0001-b005", B(P, "b005"),
         "Reinforcement learning (RL) is capable of sophisticated motion planning and control for robots in uncertain environments. However, state-of-the-art deep RL approaches typically lack safety guarantees, especially when the robot and environment models are unknown. To justify widespread deployment, robots must respect safety constraints without sacrificing performance. Thus, we propose a Black-box Reachability-based Safety Layer (BRSL) with three main components: (1) data-driven reachability analysis for a black-box robot model, (2) a trajectory rollout planner that predicts future actions and observations using an ensemble of neural networks trained online, and (3) a differentiable polytope collision check between the reachable set and obstacles that enables correcting unsafe actions. In simulation, BRSL outperforms other state-of-the-art safe RL methods on a Turtlebot 3, a quadrotor, a trajectory-tracking point mass, and a hexarotor in wind with an unsafe set adjacent to the area of highest reward."),
    text("p0001-b006", B(P, "b006"),
         "*Index Terms*—Reinforcement Learning, Robot Safety, Task and Motion Planning"),
    heading("p0001-b007", B(P, "b007"), "## I. Introduction"),
    text("p0001-b008", B(P, "b008"),
         "In reinforcement learning (RL), an agent perceives and reacts to consecutive states of its environment to maximize long-term cumulative expected reward [1]. One key challenge to the widespread deployment of RL in safety-critical systems is ensuring that an RL agent’s policies are safe, especially when the system environment or dynamics are a black box and subject to noise [2], [3]. In this work, we consider RL for guaranteed-safe navigation of mobile robots, such as autonomous cars or delivery drones, where safety means collision avoidance. We leverage RL to plan complex action sequences in concert with data-driven reachability analysis to guarantee safety for a black-box system."),
    figure("p0001-fig1", [308.0, 171.0, 567.0, 304.0], "Figure 1", "figure-1"),
    caption("p0001-b018", B(P, "b018"),
            "Fig. 1: Overview of the proposed BRSL method ([link to video](https://youtube.com/playlist?list=PL7bkcpwNaUjz-S1b5KBzpgCZ1SP4DXsoi)). Given data collected offline (in yellow, right), we perform online safe training and deployment of an RL agent. The RL agent creates trajectory plans for a robot in a receding-horizon way as follows. Each planning iteration is one clockwise loop in the green dashed box. First (blue, top left), the agent predicts a possible future trajectory by rolling out its current policy with an ensemble of neural networks trained online to model the black-box environment (grey, bottom left). Second (orange, middle), the candidate plan is *adjusted* to ensure safety using data-driven reachability and a constrained, differentiable method of collision-checking our robot’s reachable sets. We execute a failsafe maneuver if the collision check is infeasible. Finally, the new safe plan is passed to the robot, and a penalty is passed to the RL agent for choosing unsafe action."),
    heading("p0001-b009", B(P, "b009"), "### A. Related Work"),
    text("p0001-b010", B(P, "b010"),
         "Safe RL aims to learn policies that maximize expected reward on a task while respecting safety constraints during both learning and deployment [3]. Existing methods can be roughly classified as *objective-based* or *exploration-based*, depending on how safety is formulated. We first discuss these categories, then the specific case of mobile robot navigation, which we use to evaluate our proposed method."),
    text("p0001-b020", B(P, "b020"),
         "Objective-based methods encourage safety by penalizing constraint violations in the objective. This can be done by relating cumulative reward to the system’s risk, such as the probability of visiting error states [4]. In practice, this results in an RL agent attempting to minimize an empirical risk measure (that is, an approximation of the probability of entering a dangerous or undesired state). Similarly, one can penalize the probability of losing reward (by visiting an unsafe state) for a given action [2], in which case the agent minimizes temporal differences in the reward and thus also minimizes risk. Another approach is to restrict policies to be ergodic with high probability, meaning any state can eventually be reached from any other state [5]. This is a more general problem, which comes at a cost: feasible safe policies do not always exist, and the algorithms are far more complex. While these methods can make an agent prefer safe actions, they cannot guarantee safety during training or deployment. Another group of objective-based algorithms aims to modify the Markov Decision Process (MDP) that the RL agent tries to optimize. Some model safe optimization problems as maximizing an unknown expected reward function [6]. However, they exploit regularity assumptions on the function wherein similar decisions are associated with similar rewards. They also assume the bandit setting, where decisions do not cause state transitions. Others"),
]

save(P, items, r"""
Compared item by item with the 170 dpi render of PDF page 1, 300 dpi crops of the author line, the footnote block and
Figure 1, and the authors' TeX source (main.tex, Sections/1_abs.tex, 2_intro.tex, 3_related.tex). Omitted as page
furniture: the running header 'IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. ACCEPTED JUNE, 2022', the page
number 1, and the vertical arXiv stamp 'arXiv:2204.07417v2 [cs.RO] 21 Nov 2022' (the extractor had an empty text item
there). Title kept as the single level-1 heading. Author line: the extractor's sup tags were replaced by LaTeX
superscripts (affiliation marks 1, 2, 3, 3, 3, 4 checked on the 300 dpi crop). The five unnumbered first-page footnotes
(IEEE \thanks block: manuscript dates, editor note, funding, affiliations with corresponding e-mail, DOI note) are
printed at the bottom of the left column; they are placed directly after the author block, each starting with
'Footnote:', so that the last sentence of the page can join page 2. The extractor had split 'Accepted: June | 12, 2022'
and made '12, 2022' a heading; rejoined. The e-mail is printed in typewriter type and is written in backticks. The
run-in label 'Abstract—' (bold italic) is represented by a '## Abstract' heading and the bold face of the abstract was
dropped; 'data-driven' is a real compound hyphen broken at a line end (TeX confirms; extractor had 'datadriven').
'Index Terms—' line kept as a text item, not a heading (the extractor had made it a level-3 heading). 'I. INTRODUCTION'
(small caps) written in title case; 'A. Related Work' (italic subsection) is a level-3 heading. Figure 1 is printed at
the top of the right column and interrupts the first sentence of Section I-A ('... safety constraints during | both
learning and deployment [3]'); the figure and its caption are placed after the first paragraph of Section I (where
the TeX source has the float) and the Related-Work sentence was merged across the columns. Figure 1 crop checked on
a 300 dpi render: it contains the whole green dashed box, the 'Offline Data Collection' box on the right and the
label 'Online Training + Testing'; the caption is not in the crop. In the caption, 'link to video' is a hyperlink
whose target (read from the PDF link annotation and identical to the TeX \href) is given as a Markdown link;
'collision-checking' is a compound hyphen at a line end (extractor had 'collisionchecking'). 'objective-based' at the
line end in the last paragraph likewise restored (extractor had 'objectivebased'). The last paragraph ends in the
middle of a sentence ('... Others'); it continues on page 2 ('utilize constrained MDPs ...'), joined there with
join_previous 'space'. Citation numbers [1]-[6] checked against the page image. No mathematics on this page.
""")
