from pt import *
E2 = "&emsp;&emsp;"
E4 = E2 + E2
alg = "\n\n".join([
 r"**Algorithm 1: GoTube**",
 r"**Require:** initial ball $\mathcal{B}_0 = B(x_0, \delta_0)$, time horizon T, sequence of timesteps $t_j$ ($t_0 < \cdots < t_k = T$), error tolerance $\mu > 1$, confidence level $\gamma \in (0,1)$, batch size $b$, distance function $d$",
 r"1: $\mathcal{V} \leftarrow \{\}$ $\quad$ (list of visited random points)",
 r"2: **sample batch** $x^B \in \mathcal{B}_0^S$",
 r"3: **for** $(j=1; j\le k; j=j+1)$ **do**",
 r"4: " + E2 + r"$\bar{p} \leftarrow 0$",
 r"5: " + E2 + r"**while** $\bar{p} < 1 - \gamma$ **do**",
 r"6: " + E4 + r"$\mathcal{V} \leftarrow \mathcal{V} \cup \{x^B\}$",
 r"7: " + E4 + r"$x_j \leftarrow \chi(t_j, x_0)$ $\quad$ (integrate initial center point)",
 r"8: " + E4 + r"$\bar{m}_{j,\mathcal{V}} \leftarrow \max_{x\in\mathcal{V}} d(t_j, x)$",
 r"9: " + E4 + r"**compute** local Lipschitz constants $\lambda_x$ for $x\in\mathcal{V}$",
 r"10: " + E4 + r"**compute** expected local difference quotient $\Delta\lambda_{x,\mathcal{V}}$ for $x\in\mathcal{V}$",
 r"11: " + E4 + r"**compute** cap radii $r_x(\lambda_x, \Delta\lambda_{x,\mathcal{V}})$ (Thm. 1) for $x\in\mathcal{V}$",
 r"12: " + E4 + r"$\mathcal{S} \leftarrow \bigcup_{x\in\mathcal{V}} B(x,r_x)^S$ $\quad$ (total covered area)",
 r"13: " + E4 + r"$\bar{p} \leftarrow \Pr(\mu \cdot \bar{m}_{j,\mathcal{V}} \ge m^\star)$",
 r"14: " + E4 + r"**sample batch** $x^B \in \mathcal{B}_0$",
 r"15: " + E2 + r"**end while**",
 r"16: " + E2 + r"$\delta_j \leftarrow \mu\cdot\bar{m}_{j,\mathcal{V}}$",
 r"17: " + E2 + r"$\mathcal{B}_j \leftarrow B(x_j, \delta_j)$",
 r"18: **end for**",
 r"19: **return** $(\mathcal{B}_1,\dots,\mathcal{B}_k)$",
])
items = [
 T(r"to compute $\chi(t_j, x)$ of the initial value problem (IVP) in Eq. (1) at time $t_j$ starting at different points $x(t_0) = x$.", L, 56, 78.8, join="space"),
 T(r"We extend this computation to the entire ball by numerically integrating the center $x_0$ and a set of points $x \in \mathcal{V}$, uniformly sampled from the surface of the ball, and using this information to compute stochastic upper bounds for the possible evolutions of the system. We define the bounding ball and bounding tube as follows:", L, 79.2, 144),
 T(r"**Definition 1 (Bounding Ball)** Given an initial ball $\mathcal{B}_0 = B(x_0, \delta_0)$, we call $\mathcal{B}_j = B(\chi(t_j, x_0), \delta_{j}(\mathcal{B}_0))$ a *bounding ball* at time $t_j$, if it stochastically bounds the reachable states $x$ at time $t_j$ for all initial points around $x_0$ having the maximal initial perturbation $\delta_0$.", L, 149, 204),
 T("As we do not only want to bound the perturbation at one specific time, but on a time series, we define:", L, 208.5, 229.5),
 T(r"**Definition 2 (Bounding Tube)** Given an initial ball $\mathcal{B}_0 = B(x_0, \delta_0)$ and bounding balls for $t_0 < \ldots < t_k = T$, we call the series of bounding balls $\mathcal{B}_1, \mathcal{B}_2, \dots, \mathcal{B}_k$ a *bounding tube*.", L, 234.5, 268),
 T(r"*Maximum perturbation at time $t_j$*. To compute a bounding tube, we have to compute at every timestep $t_j$ the maximum perturbation $\delta_j$, which is defined as a solution of the optimization problem:", L, 272.5, 315.5),
 T(r"$$\delta_j \ge \max_{x\in\mathcal{B}_0}\|\chi(t_j, x) - \chi(t_j, x_0)\| = \max_{x\in\mathcal{B}_0} d(t_j, x), \tag{2}$$", L, 319, 344),
 T(r"where $d_j(x)=d(t_j,x)$ denotes the *distance* at time $t_j$, if the initial center $x_0$ is known from the context. As stated in (Gruenbacher et al. 2021), the radius at time $t_j$ can be over-approximated by solving a global optimization problem on the surface of the initial ball $\mathcal{B}_0$: as we require Lipschitz-continuity and forward-completeness of the ODE in Eq. (1), the map $x \mapsto \chi(t_j,x)$ is a homeomorphism and commutes with closure and interior operators. In particular, the image of the boundary of the set $\mathcal{B}_0$ is equal to the boundary of the image $\chi(t_j,\mathcal{B}_0)$. Thus, Eq. (2) has its optimum on the surface of the initial ball $\mathcal{B}_0^S = \textrm{surface}(\mathcal{B}_0)$, and we will only consider points on the surface.", L, 347.5, 480),
 H("## Main Results", (139, 207), 492, 503.5),
 T("Our GoTube algorithm and its theory solve fundamental scalability problems of related works (see Table 1) by replacing interval arithmetic used to compute deterministic caps with stochastic Lipschitz caps. This enables us to verify continuous-depth models up to an arbitrary time-horizon, a capability beyond what was achievable before.", L, 508, 573.5),
 T(r"To be able to do that, we formulated Theorems on: 1) How to choose the radius of a Lipschitz cap using stochastic bounds of local Lipschitz constants of the samples together with the expected difference quotients. 2) Convergence guarantees using these new stochastic caps, as they are used by GoTube to compute the probability of $\delta_j$ being an upper bound of the biggest perturbation. In addition, we implemented tensorization and substantially increased the number of random samples, thus being able to remove the dependence on the propagation-horizon of the gradient descent and increasing the computation speed to be able to deal with continuous-depth models.", L, 574.2, 705),
 FIG("Algorithm 1", "algorithm-1", [316, 52, 562, 359.5]),
 T(alg, R, 360, 372),
 T(r"We start by describing the GoTube Algorithm. This facilitates the comprehension of the different computation and theory steps. Given a continuous-depth model as in Eq. (1), an initial ball $\mathcal{B}_0$ defined by a center point $x_0$ and the maximum initial perturbation $\delta_0$, a time horizon $T$ with a sequence of timesteps $t_j\ (t_0 < \ldots < t_k = T)$, a confidence level $\gamma \in (0,1)$, a tightness factor $\mu > 1$, a batch size $b$, and a distance function $d$. The output of the GoTube algorithm is a bounding tube that stochastically over-approximates at most by $\mu$ the propagated initial perturbation from the center $x_0$ with a probability higher than $1 - \gamma$.", R, 385, 505),
 T(r"GoTube starts by sampling a batch (tensor) $x^B\in\mathcal{B}_0^S$. It then iterates for the $k$ steps of the time horizon $T$ the following. After initializing the probability ensured to zero, and the visited states to the empty set, it loops until it reaches the desired confidence (probability) $1 - \gamma$, by increasingly taking additional batches. In each iteration, it integrates the center and the already available samples from their previous time step and the possibly new batches from their initial state (for simplicity, the pseudocode does not make this distinction explicit). GoTube then computes the maximum distance from the integrated samples to the integrated center, their local Lipschitz constant according to the variational equation of Eq. (1). Based on this information GoTube then computes the mean Lipschitz statistics and the cap radii accordingly. The total surface of the caps is then employed to compute and update the achieved confidence (probability). Once the desired confidence is achieved, GoTube exits the inner loop and computes the bounding ball in terms of its center and", R, 505.5, 705),
]
notes = r"""
Compared with a 170 dpi render of PDF page 4, 260 dpi crops of the Algorithm 1 box and of the Definition 1 / Definition 2 / display (2) region, and with the authors' TeX source; all mathematics taken from the
TeX source (macros \calB, \calV, \calS -> \mathcal{B}, \mathcal{V}, \mathcal{S}; \rd -> \delta; \calP -> \bar{p}; spacing-only '\,{=}\,' etc. written plainly) and checked against the crops; TeX and PDF agree.
The first item continues the last sentence of page 3 ('... we use numerical ODE solvers | to compute $\chi(t_j,x)$ ...'), join_previous=space.
Definitions: the PDF prints 'Definition 1 (Bounding Ball)' and 'Definition 2 (Bounding Tube)' entirely in bold with no period; kept so. The bodies are printed in italics (not reproduced); each definition
is one paragraph and ends where its TeX environment ends ('... perturbation $\delta_0$.' and '... a bounding tube.'). The emphasised terms 'bounding ball' and 'bounding tube', printed upright inside the italic
bodies, are written in italics. '*Maximum perturbation at time $t_j$*.' is an italic run-in label (the period is upright in print), not a heading. 'Main Results' is a real unnumbered heading (extractor: level 1).
Display (2) carries the printed number (2); the extractor's formula image was replaced by a LaTeX block. Low dots in '$t_0 < \ldots < t_k = T$' (Definition 2 and the paragraph after the algorithm) are as printed
(\ldots); the Require line of Algorithm 1 prints centred dots (\cdots) and '$\mathcal{B}_1, \ldots, \mathcal{B}_k$' low dots.
Algorithm 1 (printed at the top of the right column, between the end of the left column and the paragraph 'We start by describing the GoTube Algorithm.') is kept as an image crop (asset algorithm-1; the
extractor had mis-classified the box as a 21-row table) followed by a line-by-line transcription: title line in bold, Require line, printed line numbers '1:' to '19:', one paragraph per printed line,
two em-spaces per nesting level; lines 10 and 11 wrap in print ('for $x \in \mathcal{V}$' / '$\mathcal{V}$' on the continuation line) and are one line each here. As printed in the pseudocode (not conversion errors):
'time horizon T' with an upright text T in the Require line; line 2 samples from the surface $\mathcal{B}_0^S$ but line 14 from $\mathcal{B}_0$; line 13 has $m^\star$ without the index $j$;
line 1 initialises $\mathcal{V}$ before the for loop although the prose says the visited states are initialised inside it; $\mathcal{S}$ of line 12 is not used again; the Require line calls $\mu$ 'error tolerance'
and $\gamma$ 'confidence level'. The parenthesised remarks in lines 1, 7 and 12 are printed after a quad space (written as a separate $\quad$).
Kept as printed: 'formulated Theorems on: 1) How ... 2) Convergence ...', 'the probability ensured', 'iterates for the $k$ steps of the time horizon $T$ the following'.
Line-wrap hyphens removed (numer-ically, opti-mization, prob-lem, bound-ary, re-placing, stochas-tic, to-gether, Conver-gence, de-scent, facil-itates, max-imum, se-quence, follow-ing, de-sired, ex-plicit);
real compounds kept (over-approximated, Lipschitz-continuity, forward-completeness, continuous-depth, time-horizon, propagation-horizon, over-approximates).
The last paragraph ends mid-sentence ('... in terms of its center and') and continues on page 5 (joined there). No page number or running head.
"""
write(4, items, notes)
