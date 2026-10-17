from pagelib import *
P = 6
items = [
    text("p0006-b001", [89.0, 90.0, 524.0, 202.0],
         r"where $K_{B}^{\dagger}$ is the pseudo-inverse of $K_{B}$. The error states $\delta z_{t} = z_{t} - z^{\text{ref}}_{t}$ and controls $\delta u_{t} = u_{t} - u^{\text{ref}}_{t}$ follow linear error dynamics $\delta z_{t+1} = K_{A} \delta z_{t} + K_{B} \delta u_{t}$, starting from an initial error $\delta z_0 = \phi(x_0) - z^{\text{ref}}_0$, where $x_0 \in \mathcal{B}_{\epsilon}(x_{0}^{\text{ref}})$. We solve an LQR problem, finding the feedback controls $\delta u_{0:T-1}$ that minimize the finite-horizon quadratic cost $\delta z_T^\top Q_T \delta z_T + \sum_{t=0}^{T-1} (\delta z_t^\top Q \delta z_t + \delta u_t^\top R \delta u_t)$, subject to the linear dynamics $\delta z_{t+1} = K_{A} \delta z_t + K_{B} \delta u_t$, where $Q \succ 0$, $R \succ 0$, and $Q_T \succ 0$. In particular, we solve a backward Riccati recursion to obtain the optimal feedback gains $G_{0:T-1}$. This yields the tracking control law in the lifted state space (3), which can be applied on the nonlinear system (1a) as (4) by measuring and encoding the state $x_t$:"),
    text("p0006-eq34", [89.0, 202.0, 524.0, 218.0],
         "$$\nu_t = u^{\\text{ref}}_t - G_t (z_t - z^{\\text{ref}}_t), \\tag{3}\n$$\n\n$$\nu_t = u^{\\text{ref}}_t - G_t (\\phi(x_t) - z^{\\text{ref}}_t). \\tag{4}\n$$"),
    heading("p0006-b002", B(P, "p0006-b002"), "### 5.3. Reachability Analysis for Closed-Loop Koopman Dynamics"),
    text("p0006-b003", B(P, "p0006-b003"),
         r"The high computational cost of nonlinear reachability motivates our use of Koopman operators. Standard RSOA computation repeatedly overapproximates nonlinearities at each timestep in both $f$ and $\pi$ (which typically must be nonlinear to stabilize $f$), leading to high conservativeness. A $T$-step RSOA requires $2T$ nonlinear function evaluations, causing reachable sets to become vacuously loose as $T$ increases. To reduce conservativeness, partition-based methods split the input set $\overline{\mathcal{X}}_t$, propagate each partition element, and union the result; however, this incurs computational and memory costs that increases with the cardinality of the partition. In contrast, Koopman-based reachability improves scalability and reduces conservativeness without partitioning overhead by reducing the number of nonlinearities. Mapping to the lifted space $\mathcal{Z}$ creates linear dynamics, eliminating the need to bound nonlinearities during propagation. The linear dynamics also permit a linear tracking controller. Consequently, computing an RSOA $\overline{\mathcal{X}}_t$ for any timestep $t$ requires bounding only a single application of the nonlinear encoder ($\phi$) and decoder ($\psi$), reducing the number of nonlinear bounding operations from $2T$ to just $2$. To apply this insight formally for RSOA computation, we define the Tracking Koopman Feedback Loop (TKFL), denoted $\Gamma$, as a CG the describes the closed-loop dynamics for tracking $z_{0:T}^{\text{ref}} \doteq \{\phi(x_t^{\text{ref}})\}_{t=0}^T$ in the lifted state space using the feedback control law (4). Specifically, the TKFL $\Gamma : \mathcal{X}_0 \times \mathcal{U}^T \times \mathcal{Z}^{T+1} \rightarrow \hat{\mathcal{X}}^{T+1}$ maps the initial state $x_0 \in \mathcal{B}_{\epsilon}(x_{0}^{\text{ref}})$, the feedforward control trajectory $u_{0:T-1}^{\text{ref}}$ (2), and the lifted reference $z_{0:T}^{\text{ref}}$ to the decoded trajectory $\hat{x}_{0:T} \doteq \{\psi(z_{t})\}_{t=0}^T$ representing the predicted closed-loop trajectory (5) in the original state space, where the lifted states $z_t$ are updated via the closed-loop lifted dynamics (6):"),
    text("p0006-eq56", B(P, "p0006-b004"),
         "$$\n\\hat{x}_{0:T} = \\{x_0, \\{\\psi (\\tilde f_z(z_t))\\}_{t=0}^{T-1}\\}, \\tag{5}\n$$\n\n$$\nz_{t+1} = K_{A} z_t + K_{B} (u_t^\\textrm{ref} - G_t(z_t - z_t^\\textrm{ref})) \\doteq \\tilde f_z(z_t). \\tag{6}\n$$"),
    text("p0006-b005", B(P, "p0006-b005"),
         r"To summarize, the CG is constructed as follows (see Fig. 2 for visualization). First, we map the initial state via $\phi$ into the latent space, computing $z_0 = \phi(x_0)$. Second, we unroll the $T$-fold recursive application of the single-step latent dynamics, $z_{t+1} = K_{A} z_t + K_{B} u_t$, where $u_t$ is the closed-loop tracking control computed using (3), to obtain the latent trajectory $z_{0:T} = \{z_0, z_2, \cdots, z_T\}$. Third, $z_{0:T}$ is mapped back to the original state space via the decoder $\psi$ to obtain $\hat{x}_{0:T}$. The CG $\Gamma$ is passed to the `auto_LiRPA` library (Xu et al., 2020), which enables set-based bound propagation through $\Gamma$ using CROWN (Zhang et al., 2018). `auto_LiRPA` computes vector-valued affine bounding functions, $\underline{\Gamma}$ and $\overline{\Gamma}$, which enables us to compute an RSOA $\hat{\overline{\mathcal{X}}}_{0:T}$ for the decoded closed-loop lifted dynamics (5) by considering specific components of $\Gamma$, $\underline{\Gamma}_t$ and $\overline{\Gamma}_t$, that bound the states"),
    run_header(P),
    page_number(P),
]
save(P, items, r"""
Compared with a 170 dpi render of PDF page 6, 230 dpi crops of the first paragraph and of displays (5)-(6), and with
methodology.tex (macros expanded: \delfz = \delta z, \delfu = \delta u, \zref = z^{\text{ref}}, \uref =
u^{\text{ref}}, \lqrmat = G, \tnfl = \Gamma, \enc = \phi, \dec = \psi, \ka = K_{A}, \kb = K_{B}). The extractor text
was glyph soup with <sup>; all mathematics rewritten from the TeX and checked on the renders. First paragraph: the
sentence after display (2) on page 5 ('where K_B^dagger is the pseudo-inverse of K_B. ...'), new paragraph item
(page 5 ends with a display). Displays (3) and (4) are printed side by side on one line (two minipages): one text
item with one $$ block per printed number, \tag{3} and \tag{4}, kept together. Heading '5.3. Reachability Analysis for
Closed-Loop Koopman Dynamics' level 3 (extractor had level 1). 5.3 paragraph from the TeX: source wording kept as
printed, including 'memory costs that increases' and 'as a CG the describes the closed-loop dynamics' (typo for
'that'); 'vacu-ously', 'reach-ability', 'track-ing' closed up; 'closed-loop' compounds kept. Displays (5) and (6):
one text item with two $$ blocks, \tag{5}, \tag{6}; the negative \hspace of the TeX dropped (layout only). Last
paragraph ('To summarize, ...'): source slip kept as printed, the latent trajectory is written
$z_{0:T} = \{z_0, z_2, \cdots, z_T\}$ (z_1 missing, checked at 230 dpi); 'auto_LiRPA' in typewriter written as a code
span; the underline/overline on Gamma for the lower/upper bounding functions; 'recur-sive', 'propaga-tion' closed up.
The paragraph and its sentence continue on page 7 ('reached under (5) at timestep t, ...'), joined there with
join_previous 'space'; Figure 2 (cited here as 'Fig. 2') is printed on page 7 and placed there after that
paragraph. Citations: (Xu et al., 2020), (Zhang et al., 2018). Omitted: running header 'NATH YIN CHOU' and page
number 6.
""")
