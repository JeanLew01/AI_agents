from pagelib import *
P = 11
items = [
    text("p0011-b001", B(P, "p0011-b001"),
         r"**3D Quadcopter** We evaluate an analytical 12-state quadcopter (14) (Sabatino, 2015) navigating around a $1\,\mathrm{m}$ radius obstacle for $T=200$. Here, $\phi$ and $\psi$ have 3 hidden layers with 128 neurons each, and $z \in \mathbb{R}^{24}$. The computed CKRS (Fig. 4) verifies safety and goal reaching; metrics are in Table 1. To show that the offline CP inflation generalizes across controllers, we compute the CKRS for two references (Fig. 4, one orange, one blue) using the same offline-calibrated bounds; we visualize additional CKRSs in Fig. 9. An NNV-only baseline (Nath et al., 2025) is much slower and more conservative, requiring $2153.45\,\mathrm{s}$ with an average log-volume of $-30.32$. Overall, these results show our method’s efficiency, tightness, and offline CP generalization for high-dimensional systems."),
    figure("p0011-b002", [86.0, 206.0, 526.0, 358.0], "Figure 4", "figure-4"),
    caption("p0011-b003", B(P, "p0011-b003"), O(P, "p0011-b003")),
    text("p0011-b004", B(P, "p0011-b004"),
         r"**MuJoCo: Hopper** We evaluate on MuJoCo’s Hopper-v5 (Todorov et al., 2012), a nonlinear, underactuated system with black-box dynamics. A PPO agent (Stable-Baselines3, default hyperparameters) trained for $2\times 10^6$ steps is used as the planner $P$ that generates trajectories for the training dataset. Here, $\phi$ and $\psi$ have 3 hidden layers with 128 neurons each, and $z \in \mathbb{R}^{24}$. Numerical results are in Table 1 and RSOA slices for a few state dimensions are shown in Fig. 1 (see Fig. 11 for all 11 dimensions). This experiment highlights that our approach scales to black-box, high-dimensional contact-rich dynamics while maintaining low runtimes and probabilistic coverage guarantees."),
    text("p0011-b005", B(P, "p0011-b005"),
         r"**MuJoCo: Customized Swimmer** We further assess scalability on a customized MuJoCo Swimmer-v5 (Todorov et al., 2012) with extended links, yielding a 28-dimensional state. The planner $P$ is a PPO agent (Stable-Baselines3 MLP) trained for $1\times10^{7}$ steps with modified hyperparameters (LR $1\times10^{-3}$, $\gamma=0.9999$, batch size $512$; others default). Here, $\phi$ and $\psi$ have 3 hidden layers with 128 neurons each, and $z \in \mathbb{R}^{38}$. Numerical results are in Table 1 and RSOA slices for a few state dimensions are shown in Fig. 1 (see Fig. 12 for all 28 dimensions). This experiment indicates that our approach maintains certified probabilistic safety while tractably computed RSOAs for high-dimensional systems over long horizons for black-box dynamical systems in MuJoCo."),
    heading("p0011-b006", B(P, "p0011-b006"), "## 7. Conclusion"),
    text("p0011-b007", B(P, "p0011-b007"), O(P, "p0011-b007")),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 11, a 200 dpi crop of Figure 4, and with experiments.tex/conclusion.tex.
Run-in bold titles '3D Quadcopter', 'MuJoCo: Hopper', 'MuJoCo: Customized Swimmer' kept inside their text items.
Mathematics rewritten from the TeX (the extractor had <sup> and split decimals such as '2153 _._ 45'): $1\,\mathrm{m}$,
$T=200$, $\phi$, $\psi$, $z \in \mathbb{R}^{24}$ / $\mathbb{R}^{38}$, $2153.45\,\mathrm{s}$, $-30.32$, $2\times 10^6$,
$1\times10^{7}$, LR $1\times10^{-3}$, $\gamma=0.9999$, batch size $512$; the planner $P$ is math. Line-wrap hyphens:
'Ta-ble', 'con-servative', 'hyperpa-rameters', 'indi-cates' closed up; 'Swimmer-/v5' is the environment name
'Swimmer-v5' (hyphen kept; extractor had 'Swimmerv5'). Source wording kept: 'while tractably computed RSOAs'.
References as printed: (14), Fig. 4 (twice), Fig. 9, Fig. 1 (twice), Fig. 11, Fig. 12, Table 1; citations (Sabatino,
2015), (Nath et al., 2025), (Todorov et al., 2012) twice. Figure 4: 4 x 3 grid of time plots (columns 'Position (m)',
'Angles (rad)', 'Velocity (m/s)', 'Angular Velocity (rad/s)'; rows p_x/p_y/p_z, psi/theta/phi, v_x/v_y/v_z, p/q/r;
x-axes 'Time Step (t)'; legend 'KRS', 'CKRS', 'GT Rollouts', 'Reference'); one crop 'figure-4' with all labels inside
(edges checked at 200 dpi); the extractor's scattered picture text was deleted after checking it lies inside the
crop. Caption verbatim. Heading '7. Conclusion' level 2 (extractor had level 1). Conclusion paragraph: extractor text
checked on the render (curly quotes around 'conformalize' as printed; 'represen-tation' closed up); it continues on
page 12 ('set with a specified probability ...'), joined there with join_previous 'space'. Omitted: running header
(short title) and page number 11.
""")
