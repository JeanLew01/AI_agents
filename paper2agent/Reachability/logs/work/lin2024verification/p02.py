from pagelib import *

items = [
    header(2),
    text("p0002-b001", [89.0, 94.0, 523.0, 213.0],
         "grid, resulting in an exponentially scaling computation complexity with the number of states (Bansal et al., 2017). To overcome this challenge, a variety of solutions have been proposed that trade off between the class of dynamics they can handle, the approximation quality of the BRT, and the required computation. These include specialized methods for linear and affine dynamics (Greenstreet and Mitchell, 1998; Frehse et al., 2011; Kurzhanski and Varaiya, 2000, 2002; Maidens et al., 2013; Girard, 2005; Althoff et al., 2010; Bak et al., 2019; Nilsson and Ozay, 2016), polynomial dynamics (Majumdar et al., 2014; Majumdar and Tedrake, 2017; Dreossi et al., 2016; Henrion and Korda, 2014), monotonic dynamics (Coogan and Arcak, 2015), and convex dynamics (Chow et al., 2017) (see Bansal et al. (2017); Bansal and Tomlin (2021) for a survey).",
         join_previous="space"),
    text("p0002-b002", [89.0, 216.0, 523.0, 416.0],
         "Owing to the success of deep learning, there has also been a surge of interest in approximating high-dimensional BRTs (Rubies-Royo et al., 2019; Fisac et al., 2019; Djeridane and Lygeros, 2006; Niarchos and Lygeros, 2006; Darbon et al., 2020) and optimal controllers (Onken et al., 2022) through deep neural networks (DNNs). Building upon this line of work, Bansal and Tomlin (2021) have proposed DeepReach – a toolbox that leverages recent advances in neural implicit representations and neural PDE solvers to compute a value function and a safety controller for high-dimensional systems. Compared to the aforementioned methods, DeepReach can handle general nonlinear dynamics, the presence of exogenous disturbances, as well as state and input constraints during the BRT computation. Consequently, methods for verifying neural reachable tubes have been proposed. For example, Lin and Bansal (2023) propose an iterative scenario-based method (Campi et al., 2009) to recover probabilistically safe reachable tubes from DeepReach solutions up to a desired confidence level and bound on violation rate. Unfortunately, the method does not allow an after-the-fact risk-return trade-off, and as a result, it is highly sensitive to outlier errors in the learned solutions. This can lead to highly conservative reachable tubes and a severe loss of recovery in the case of stringent safety requirements, as we demonstrate in our case studies."),
    text("p0002-b003", [89.0, 419.0, 523.0, 579.0],
         "In this work, we propose two different verification methods, one based on robust scenario optimization and the other based on conformal prediction, to provide probabilistic safety guarantees for neural reachable tubes. Both methods are resilient to the outlier errors in neural reachable tubes and automatically trade-off the strength of the probabilistic safety guarantees based on the outlier rate. The proposed methods can evaluate any candidate tube and are not restricted to a specific class of system dynamics or value functions. We further prove that these seemingly different verification methods naturally reduce to one another, providing a unifying viewpoint for uncertainty quantification (typical use case of conformal prediction) and error optimization (typical use case of scenario optimization) in neural reachable tubes. Based on these insights, we propose an outlier-adjusted verification approach that can recover a greater safe volume from a neural reachable tube by harnessing information about the distribution of error in the learned solution. To summarize, the key contributions of this paper are:"),
    text("p0002-b004", [107.0, 589.0, 523.0, 706.0],
         "- probabilistic safety verification methods for neural reachable tubes that enable a direct trade-off between resilience and the probabilistic strength of safety,\n"
         "- a proof that split conformal prediction reduces to a scenario-based approach in general, demonstrating a strong relationship between the two highly related but disparate fields,\n"
         "- an outlier-adjusted verification approach that recovers greater safe volumes from tubes, and\n"
         "- a demonstration of the proposed approaches for the high-dimensional problems of multi-vehicle collision avoidance and rocket landing with no-go zones."),
    pageno(2, "p0002-b008", [303.0, 726.0, 309.0, 733.0]),
]

save(2, items, """
Compared the whole page with the 130 dpi render and with sections/introduction.tex. The first item continues the last
sentence of page 1 (join_previous 'space'). All citations are printed in author-year style; each citation group was
compared with the page image, including the order inside the long group for linear and affine dynamics ('Kurzhanski and
Varaiya, 2000, 2002' is printed in this compressed form) and the textual citations 'Bansal et al. (2017); Bansal and
Tomlin (2021)', 'Bansal and Tomlin (2021)', 'Lin and Bansal (2023)'. The dash in 'DeepReach – a toolbox' is an en dash as
printed. Line-wrap hyphens removed (re-quired, approximat-ing, Tom-lin, op-timization, quantifica-tion, har-nessing); real
compound hyphens that fall at a line end were kept or restored after checking the TeX source ('high-dimensional' in the
second paragraph; 'trade-off' and 'multi-vehicle' in the bullet list, where the extractor had dropped the hyphen). The four bulleted
contributions were four extractor items; they are merged into one list item. The authors' wording 'automatically
trade-off the strength' is kept as printed. This page contains no mathematics. Omitted: running header and page number.
""")
