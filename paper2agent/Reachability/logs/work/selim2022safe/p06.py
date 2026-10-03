from pagelib import *

P = 6
GITHUB = "https://github.com/Mahmoud-Selim/Safe-Reinforcement-Learning-for-Black-Box-Systems-Using-Reachability-Analysis"

items = furniture(P) + [
    text("p0006-b008", B(P, "b008"),
         r"unsafe plan with Algorithm 3, the zonotope collision check is guaranteed to always detect collisions [43, Prop. 2] to assess if $\hat{R}_j \cap X_{\text{obs}}$ is empty for each time step $j$ of the plan. Third, Algorithm 3 requires that, after $n_{\text{plan}}$ timesteps, the robot is stopped, so the new plan contains a failsafe manuever, and the robot can safely apply $\mathbf{u}_{\text{brk}}$ for all time $j \geq k+n_{\text{plan}}$. $\square$",
         join_previous="space"),
    text("p0006-b009", B(P, "b009"),
         "We note that the accuracy of the environment model, trained online, does not affect safety; Theorem 1 holds as long as the offline data are representative of the robot’s dynamics at runtime. We leave updating the data online for future work."),
    heading("p0006-b010", B(P, "b010"), "## IV. Evaluation"),
    text("p0006-b011", B(P, "b011"),
         "We evaluate BRSL on two types of environments: safe navigation to a goal (a Turtlebot in Gazebo and a quadrotor platform in Unreal Engine 4), and path following (a point mass based on [14], [24] and a hexarotor in wind in Unreal Engine 4). Figure 3 shows example environments. All code is run on a desktop computer with an Intel i5 11600 CPU and a RTX 3060 GPU. Our code is available [online](" + GITHUB + "). We aim to assess the following: (a) How does BRSL compare against other safe RL methods (RTS [28], SAILR [24], and SECAS [30])? (b) How conservative is BRSL? (c) Can BRSL run in real time?"),
    figure("p0006-fig3", [82.0, 56.0, 528.0, 158.0], "Figure 3", "figure-3"),
    caption("p0006-b007", B(P, "b007"),
            "Fig. 3: Evaluation Environments.\n\n"
            "Sub-captions printed under the panels: (a) Turtlebot3 Environment; (b) Quadrotor Environment; (c) Hexarotor Environment"),
    text("p0006-b012", B(P, "b012"),
         "**Setup.** We use TD3 [52] as our RL agent, after determining empirically that it outperforms SAC [53] and DDPG [54]. We randomly initialize the policy. Since the agent outputs continuous actions, to aid the exploration process, we inject zero-mean Gaussian noise with a variance of 0.5 that is dampened each time step. Note that this does not affect safety since our safety layer adjusts the output of the RL agent."),
    text("p0006-b013", B(P, "b013"),
         "For each robot, to perform reachability analysis with Algorithm 2, we collect 500 time steps of noisy state/input data (as per (4)) offline in an empty environment while applying random control inputs. We found this quantity of data sufficient to ensure safety empirically; we leave a formal analysis of the minimum amount of data for future work."),
    text("p0006-b014", B(P, "b014"),
         "We parameterize the environment model as an ensemble of neural networks, each modeling a Gaussian distribution over future states and observations. Each network has 4 layers, with hidden layers of size 200, and leaky ReLU activations with a negative slope of 0.01. We use a stochastic model wherein the ensemble predicts the parameters of a probability distribution, which is sampled to produce a state as in [55]."),
    text("p0006-b015", B(P, "b015"),
         r"*Goal-Based Environments.* The Turtlebot 3 and the quadrotor seek to navigate to a random circular goal region $X_{\text{goal}} \subset X$ while avoiding randomly-generated obstacles $X_{\text{obs}} \subset X$. Each robot starts in a safe location at the center of the map. Each task is episodic, ending if the robot reaches the goal, crashes, or exceeds a time limit. Both robots have uncertain, noisy dynamics as in (2). We discretize time at 10 Hz."),
    text("p0006-b017", B(P, "b017"),
         r"The Turtlebot’s control inputs are longitudinal velocity in $[0.00, 0.25]$ m/s and angular velocity in $[-0.5, 0.5]$ rad/s (these are the bounds of $U_k$). The robot has wheel encoders, plus a planar lidar that generates 18 range measurements evenly spaced in a $180^\circ$ arc in front of the robot. The robot requires $n_{\text{brk}} = 6$ time steps to stop, so we set $n_{\text{plan}} = 8$."),
    text("p0006-b018", B(P, "b018"),
         r"The quadrotor control inputs are commanded velocities up to 5 m/s in each spatial direction at each time step. We note that we also experimented with learning low-level rotor speeds versus high-level velocity commands, and found that the velocity commands created the fairest testing conditions across all agents. The robot is equipped with an IMU and a 16-channel lidar which receives range measurements around the robot in a $50^\circ$ vertical arc and a $360^\circ$ horizontal arc. The robot has $n_{\text{brk}} = 10$, so we set $n_{\text{plan}} = 11$."),
    text("p0006-b019", B(P, "b019"),
         "*Path Following Environments.* These experiments assess BRSL’s conservativeness is by placing the highest reward adjacent to obstacles."),
    text("p0006-b020", B(P, "b020"),
         r"The goal for the point robot is to follow a circular path of radius $r$ as quickly as possible while constrained to a region smaller than the target circle. The point robot is a 2-D double integrator with position and velocity as its state: $\mathbf{x}_k = (x_k,y_k,\dot{x}_k,\dot{y}_k)$. It has a maximum velocity of 2 m/s, and its control input is acceleration up to 1 m/s$^{2}$ in any direction. We use these dynamics as in [14], [24] to enable a fair test against other methods that require a robot model. We define a box-shaped safe set (the complement of the obstacle set) as $X_{\text{safe}} = \{\mathbf{x}_k \in X : |x_k| \le x_{\max}, |y_k| \le y_{\max}\}$, with $\lVert(x_{\max}, y_{\max})\rVert_2 < r$. We use a reward that encourages traveling quickly near the unsafe set: $\rho (\hat{\mathbf{x}}_k,\mathbf{u}_k) = \frac{(\dot{x}_k, \dot{y}_k) \cdot (-y_k, x_k)}{1 + \big| \lVert(x_k, y_k)\rVert_2 - r\big|}$."),
    text("p0006-b021", B(P, "b021"),
         "The hexarotor has the same setup as the quadrotor, but with the addition of wind as an external disturbance. The goal of the hexarotor is to pass through 10 checkpoints in a fixed order while subject to wind (constant speed and direction) and randomly-placed obstacles. Note, offline data collection was performed under wind conditions."),
    text("p0006-b022", B(P, "b022"),
         "**Results and Discussion.** The results are summarized in Tables I and II, and in Figure 4. BRSL outperforms the other methods in terms of reward and safety, is not overly conservative, and can operate in real time, despite lacking a model of the robot *a priori*. While SAILR and the baseline RL agent achieved higher speeds, both experienced collisions, unlike BRSL, RTS, and SECAS. In contrast to RTS, which chooses from a low-dimensional parameterized plans, BRSL outputs a more flexible sequence of actions. Furthermore RTS’ planning"),
]

save(P, items, r"""
Compared with the 170 dpi render of PDF page 6, a 200 dpi crop of Figure 3, 300-330 dpi crops of the end of the
proof, the Turtlebot paragraph and the point-robot paragraph, and the TeX source (end of Sections/5_solu.tex,
7_eval.tex). Running header and page number 6 omitted. Figure 3 is a full-width float at the top of the page that
interrupts the proof of Theorem 1: the first item is the continuation of the proof from page 5 ('Second, when
adjusting an | unsafe plan with Algorithm 3 ...'), join_previous 'space'; the printed end-of-proof box is written as
$\square$. Figure 3 and its caption are placed after the first paragraph of Section IV, which refers to it ('Figure
3 shows example environments'). The extractor had split the figure into five image fragments; they are replaced by
one crop with the three screenshots and their printed sub-captions (edges checked on the render; the caption line
'Fig. 3: Evaluation Environments.' is outside the crop). The three sub-captions are repeated in the caption item so
that they are searchable (they are inside the crop, hence not counted by the line check). The paragraph
'Goal-Based Environments. ... reaches the goal, | crashes, or exceeds a time limit ...' runs from the bottom of the
left column to the top of the right column and was merged. 'IV. EVALUATION' (small caps) is a level-2 heading in
title case. 'Setup.' and 'Results and Discussion.' are bold run-in labels; 'Goal-Based Environments.' and 'Path
Following Environments.' are italic run-in labels (kept as bold / italic text, not headings). The underlined word
'online' ('Our code is available online') is a hyperlink to the GitHub repository (PDF link annotation), given as a
Markdown link. Numbers that the authors typeset in math mode (4, 0.5, 500, 4, 0.01, 10, 18, 10) are written as plain
text so that they stay searchable; intervals '[0.00, 0.25] m/s' and '[-0.5, 0.5] rad/s', the degree values 180, 50,
360, n_brk = 6 / n_plan = 8 (Turtlebot) and n_brk = 10 / n_plan = 11 (quadrotor) were checked on the 300 dpi crop.
The inline reward fraction rho(x_hat_k, u_k) = ((x_dot_k, y_dot_k) . (-y_k, x_k)) / (1 + | ||(x_k, y_k)||_2 - r |)
is printed very small; it was taken from the TeX source and confirmed on a 330 dpi crop (the extractor output for it
was glyph soup). Line-end hyphens: 'Al-|gorithm', 'quadro-|tor', 'conser-|vative', 'travel-|ing' are line wraps;
'2-|D' is the compound '2-D'. Kept as printed, not conversion errors: 'manuever'; 'assess BRSL's conservativeness is
by placing'; 'a low-dimensional parameterized plans'; 'Furthermore RTS' planning' without comma; 'Turtlebot 3' in
the text versus 'Turtlebot3' in the sub-caption. The last paragraph ends mid-sentence ('Furthermore RTS' planning');
it continues on page 7 below the figure and tables and is joined there. Citation numbers checked against the image.
""")
