from pagelib import *

items = [
    header(4),
    text("p0004-b001", [89.0, 93.0, 523.0, 209.0],
         r". The value function in Equation (1) can be computed using dynamic programming, resulting in the following final value Hamilton-Jacobi-Bellman Variational Inequality (HJB-VI): $\min\Big\{D_t V(x,t)+ H(x,t), l(x)-V(x,t)\Big\} = 0$, with the terminal value function $V(x,T) = l(x)$. $D_t$ and $\nabla$ represent the time and spatial gradients of $V$. $H$ is the Hamiltonian that encodes the role of dynamics and the optimal control: $H(x,t) = \max_u \langle \nabla V(x,t), f(x,u)\rangle$. The value function in Equation (1) induces the optimal safety controller: $u^{\ast}(x,t) = \underset{u}{\arg\max} \langle \nabla V(x,t), f(x,u)\rangle$. Intuitively, the safety controller aligns the system dynamics in the direction of the value function’s gradient, thus steering the system towards higher-value states, i.e., away from $\mathcal{L}$.",
         join_previous="none"),
    text("p0004-b002", [90.0, 211.0, 523.0, 263.0],
         r"We have just explained the case where $\mathcal{L}$ represents a set of undesirable states. When the system instead wants to reach $\mathcal{L}$, an infimum is used instead of a supremum in Equation (1). The control wants to reach $\mathcal{L}$, hence there is a minimum instead of a maximum in the Hamiltonian and optimal safety controller equations. See Bansal et al. (2017) for details on other reachability cases."),
    text("p0004-b003", [90.0, 265.0, 523.0, 330.0],
         "Traditionally, the value function is computed by solving the HJB-VI over a discretized grid in the state space. Unfortunately, doing so involves computation whose memory and time complexity scales exponentially with respect to the system dimension, making these methods practically intractable for high-dimensional systems, such as those beyond 5D. Fortunately, a deep learning approach, DeepReach, has been proposed to enable HJ reachability for high-dimensional systems."),
    heading("p0004-b004", [90.0, 336.0, 507.0, 347.0],
            "### 3.2. DeepReach and an Iterative Scenario-Based Probabilistic Safety Verification Method"),
    text("p0004-b005", [90.0, 350.0, 523.0, 443.0],
         r"Instead of solving the HJB-VI over a grid, DeepReach (Bansal and Tomlin, 2021) learns a parameterized approximation of the value function using a sinusoidal deep neural network (DNN). Thus, memory and complexity requirements for training scale with the value function complexity rather than the grid resolution, allowing it to obtain BRTs for high-dimensional systems. DeepReach trains the DNN via self-supervision on the HJB-VI itself. Ultimately, it takes as input a state $x$ and time $t$, and it outputs a learned value function $" + V + r"(x,t)$. $" + V + r"(x,t)$ also induces a corresponding safe policy $" + PI + r"(x,t)$, as well as a BRT (referred to as the neural reachable tube from hereon)."),
    text("p0004-b006", [90.0, 443.0, 523.0, 567.0],
         r"However, the neural reachable tube will only be as accurate as $" + V + r"(x,t)$. To obtain a provably safe BRT, Lin and Bansal (2023) propose a uniform value correction bound which is defined, for the avoid case, as the maximum learned value of an unsafe state under the induced policy: $" + DELTA + r" := \max_{x\in X}\{" + V + r"(x,0): " + J + r"(x,0) \le 0\}$. The authors show that the super-$" + DELTA + r"$ level set of $" + V + r"(x,0)$ is provably safe under the policy $" + PI + r"(x,t)$. They also propose an iterative scenario-based probabilistic verification method for computing an approximation of $" + DELTA + r"$ from finite random samples that satisfies a desired confidence level and violation rate. However, the method is sensitive to outlier errors in the neural reachable tube and can result in very conservative safe sets. Specifically, it does not provide safety assurances for safe sets with nonzero empirical safety violations."),
    text("p0004-b007", [90.0, 570.0, 523.0, 608.0],
         "In this work, we propose probabilistic safety verification methods that allow nonzero empirical safety violations at the cost of the probabilistic strength of safety. This enables a direct trade-off between resilience to outlier errors and the strength of the safety guarantee."),
    text("p0004-b008", [90.0, 616.0, 523.0, 653.0],
         r"**Remark 1** Although we work with DeepReach solutions in particular for our problem setup, our proposed approaches can verify any general $" + V + r"(x,t)$ and $" + PI + r"(x,t)$, regardless of whether DeepReach, a numerical PDE solver, or some other tool is used to obtain them."),
    heading("p0004-b009", [90.0, 665.0, 432.0, 677.0],
            "## 4. Robust Scenario-Based Probabilistic Safety Verification Method"),
    text("p0004-b010", [90.0, 681.0, 523.0, 706.0],
         "Here, we propose a robust scenario-based probabilistic safety verification method for neural reachable tubes. The new method is a straightforward application of a scenario-based sampling-and-"),
    pageno(4, "p0004-b011", [303.0, 726.0, 309.0, 733.0]),
]

save(4, items, r"""
Compared the whole page with the 130 dpi render, with 200 dpi crops of the two mathematical regions (top of the page and
Section 3.2) and with sections/background.tex and sections/scenario-based_method.tex. The first item continues the inline
formula that ends page 3: the glyphs 'X, V(x,0) ≤ 0}' printed at the top of this page are transcribed at the end of page 3,
so this item starts with the full stop (join_previous 'none'). All inline mathematics was rewritten in LaTeX from the TeX
source with the macros expanded (\Tilde{\vfunc} -> \tilde{V}, \Tilde{\policy} -> \tilde{\pi}, \costFunction ->
J_{\tilde{\pi}}, \safetyMetric -> \delta_{\tilde{V},\tilde{\pi}}) and checked against the crops: the HJB-VI
min{D_t V + H, l - V} = 0 with terminal condition V(x,T) = l(x), the Hamiltonian with max over u, the optimal controller
with arg max over u, and the definition of the uniform value correction bound. Two notational substitutions that do not
change the printed symbols: the mathtools symbol \coloneqq (printed ':=') is written ':=', and the optimal-control star
u^* is written u^{\ast} (a bare '^*' can be read as Markdown emphasis). TeX and PDF agree. 'Remark 1' is printed in bold
without punctuation and its body in italics; the body is one sentence and ends with '... is used to obtain them.' (end
of the remark environment in the TeX source). Headings: 3.2 is level 3, Section 4 is level 2 (the extractor had levels 2
and 1). Line-wrap hyphens removed (func-tion, complex-ity, param-eterized, prov-ably, sam-ples, reach-able); real hyphens
kept (Hamilton-Jacobi-Bellman, higher-value, high-dimensional, self-supervision, scenario-based, trade-off, HJB-VI). The
last sentence breaks at the real hyphen of 'sampling-and-discarding': this item ends with 'sampling-and-' and the first
item of page 5 ('discarding approach ...') has join_previous 'none'. Omitted: running header and page number.
""")
