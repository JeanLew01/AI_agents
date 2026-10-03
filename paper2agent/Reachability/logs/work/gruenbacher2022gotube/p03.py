from pt import *
rows = [
 ["Technique", "Determ.", "Parallel", "wrapping effect", "Arbitrary Time-horizon"],
 ["LRT (Cyranka et al. 2017) with Infinitesimal strain theory", "yes", "no", "yes", "no"],
 ["CAPD (Kapela et al. 2020) implements Lohner algorithm", "yes", "no", "yes", "no"],
 ["Flow-star (Chen, Ábrahám, and Sankaranarayanan 2013) with Taylor models", "yes", "no", "yes", "no"],
 ["δ-reachability (Gao, Kong, and Clarke 2013) with approximate satisfiability", "yes", "no", "yes", "no"],
 ["C2E2 (Duggirala et al. 2015) with discrepancy functions", "yes", "no", "yes", "no"],
 ["LDFM (Fan et al. 2017) by simulation, matrix measures", "yes", "yes", "no", "no"],
 ["TIRA (Meyer, Devonport, and Arcak 2019) with second-order sensitivity", "yes", "yes", "no", "no"],
 ["Isabelle/HOL (Immler 2015) with proof-assistant", "yes", "no", "yes", "no"],
 ["Breach (Donzé 2010; Donzé and Maler 2007) by simulation", "yes", "yes", "no", "no"],
 ["PIRK (Devonport et al. 2020) with contraction bounds", "yes", "yes", "no", "no"],
 ["HR (Li, Bak, and Bogomolov 2020) with hybridization", "yes", "no", "yes", "no"],
 ["ProbReach (Shmarov and Zuliani 2015a) with δ-reachability,", "no", "no", "yes", "no"],
 ["VSPODE (Enszer and Stadtherr 2011) using p-boxes", "no", "no", "yes", "no"],
 ["Gaussian process (GP) (Bortolussi and Sanguinetti 2014)", "no", "no", "no", "no"],
 ["Stochastic Lagrangian reachability SLR (Gruenbacher et al. 2021)", "no", "yes", "no", "no"],
 ["GoTube (Ours)", "no", "yes", "no", "yes"],
]
items = [
 T("knowledge about the values, such that we are able to correspondingly estimate the stochastic global optimum with high confidence. (Zhigljavsky and Zilinskas 2008).", L, 296, 328, join="space"),
 T("**Verification of Neural Networks.** A large body of work tried to enhance the robustness of neural networks against adversarial examples (Goodfellow, Shlens, and Szegedy 2014). There are efforts that show how to break the many defense mechanisms proposed (Athalye, Carlini, and Wagner 2018; Lechner et al. 2021), until the arrival of methods for formally verifying robustness to adversarial attacks around neighborhoods of data (Henzinger, Lechner, and Zikelic 2021). The majority of these complete verification algorithms for neural networks work on piece-wise linear structures of small-to-medium-size feedforward networks (Salman et al. 2019). For instance, (Bunel et al. 2020b) has recently introduced a BaB method that outperforms state-of-the-art verification methods (Katz et al. 2017; Tjandraatmadja et al. 2020). A more scalable approach for rectified linear unit (ReLU) networks (Nair and Hinton 2010) was recently proposed based on Lagrangian decomposition; this approach significantly improves the speed and tightness of the bounds (De Palma et al. 2021). The proposed approach not only improves the tightness of the bounds but also performs a novel branching that matches the performance of the learning-based methods (Lu and Mudigonda 2020) and outperforms state-of-the-art methods (Zhang et al. 2018; Singh et al. 2020; Bak et al. 2020; Henriksen and Lomuscio 2020). While these verification approaches work well for feedforward networks with growing complexity, they are not suitable for recurrent and continuous neural network instances, which we address in this work.", L, 331, 637),
 T("**Verification of Continuous-time Systems.** Reachability analysis is a verification approach that provides safety guarantees for a given continuous dynamical system (Gurung et al. 2019; Vinod and Oishi 2021). Most dynamical systems in safety-critical applications are highly nonlinear and uncertain in nature (Lechner et al. 2020). The uncertainty can be in the system’s parameters (Wang et al. 2015; Shmarov and Zuliani 2015b; Enszer and Stadtherr 2011), or their initial state (Enszer and Stadtherr 2011; Huang et al. 2017). This is often handled by considering balls of a certain radius around them. Nonlinearity might be inherent in the system dynamics or due to discrete mode-jumps (Fränzle et al. 2011). We provide a summary of methods developed for the reachability analysis of continuous-time ODEs in Table 1.", L, 640, 705),
 C("Table 1: Related work on the reachability analysis of continuous-time systems. Determ.= Deterministic. ”No” indicates a stochastic method. Table content is partially reproduced from (Gruenbacher et al. 2021).", (54, 558), 54, 76),
 TAB("Table 1", "table-1", [67, 85, 543, 275], rows),
 T("A fundamental shortcoming of the majority of the methods described in Table 1 is their lack of scalability while providing conservative bounds. In this paper, we show that GoTube establishes the state-of-the-art for the verification of ODE-based systems in terms of speed, time-horizon, task completion, and scalability on a large set of experiments.", R, 384, 449.5),
 H("## Setup", (424, 454), 463, 474.5),
 T("In this section, we introduce our notation, preliminary concepts, and definitions required to state and prove the stochastic bounds that GoTube guarantees for time-continuous process models.", R, 480, 523),
 T(r"*Continuous-depth models.* These are a special case of nonlinear ordinary differential equations (ODEs), where the model is defined by the derivative of the unknown states $x$ computed by a vector-valued function $f : \mathbb{R}^n \rightarrow \mathbb{R}^n$, which is assumed to be Lipschitz-continuous and forward-complete:", R, 524.5, 578.5),
 T(r"$$\partial_t x = f(x),\quad x(t_0) \in \mathcal{B}_0 = B(x_0, \delta_0), \tag{1}$$", R, 583, 603),
 T(r"$\mathcal{B}_0$ defines the initial ball (a region of initial states, whose radius quantifies the magnitude $\delta_0$ of a perturbation of its center $x_0$). Time dependence can be incorporated by an additional variable $x$ with $\delta_t x = 1$. Thus this definition naturally extends to time-varying ODEs. Nonlinear ODEs do not have in general closed-form solutions, and therefore one can not compute symbolically the solution $\chi(t_j, x)$ for all $x \in \mathcal{B}_0$. For a sequence of $k$ timesteps from time $t_0$ until time horizon $T$: $t_0 < \ldots < t_k = T$, we use numerical ODE solvers", R, 606.5, 705.5),
]
notes = r"""
Compared with a 170 dpi render of PDF page 3 and with the authors' TeX source; mathematics taken from the TeX source (macros \R -> \mathbb{R}, \calB -> \mathcal{B}, \rd -> \delta; spacing-only
'\,{:}\,', '\,{=}\,', '\,{\in}\,', '\,{<}' written plainly) and checked against the page. The first item continues the last sentence of page 2 ('... where we have probabilistic | knowledge about the values'),
join_previous=space. Table 1 is printed across both columns at the top of the page, above that continuing sentence; here its caption (printed above the table) and the table follow the paragraph
'Verification of Continuous-time Systems.', which ends with the reference to Table 1. That paragraph runs from the left column into the right column ('The uncertainty can | be in the system's parameters') and is one item.
Table 1: 5 columns, header row plus 16 technique rows, every cell read on the render and compared with the TeX tabular; the two-line headers 'wrapping / effect' and 'Arbitrary / Time-horizon' are joined
with a space; the header row and the cells 'GoTube (Ours)' and the final 'yes' are printed in bold (not marked in the cells); the delta of 'δ-reachability' (rows 4 and 12) is a Unicode character in the cells;
the trailing comma of 'ProbReach (Shmarov and Zuliani 2015a) with δ-reachability,' is as printed. The extractor's table had the same cells with bold markers and <br> tags.
Caption: the PDF prints the quotation marks around No as two closing marks (”No”), kept; 'Determ.= Deterministic.' as printed.
Display (1) is the only display and carries the printed number (1); the extractor's formula image was replaced by a LaTeX block. 'Setup' is a real unnumbered heading (extractor: level 1).
'Verification of Neural Networks.' and 'Verification of Continuous-time Systems.' are bold run-in paragraph labels; 'Continuous-depth models.' is an italic run-in label; none is a heading.
Kept as printed (authors' wording): 'high confidence. (Zhigljavsky and Zilinskas 2008).' with a period before the citation; 'For instance, (Bunel et al. 2020b) has recently introduced'; 'Zikelic' without diacritics;
'$\delta_t x = 1$' with a delta (the TeX source has \delta_t here, while display (1) has \partial_t); 'an additional variable $x$'; 'one can not'. The dots in '$t_0 < \ldots < t_k = T$' are printed on the baseline
(TeX source: \dots between braced relation signs), hence \ldots. Line-wrap hyphens removed (cor-respondingly, Wag-ner, meth-ods, Tjandraat-madja, per-forms, out-performs, feedfor-ward, suit-able, guar-antees,
un-certain, ini-tial, ra-dius, sys-tem, con-cepts, stochas-tic, pro-cess, addi-tional, hori-zon); real compounds kept (state-of-the-art, piece-wise, small-to-medium-size, learning-based, safety-critical,
mode-jumps, continuous-time, ODE-based, time-horizon, time-continuous, vector-valued, Lipschitz-continuous, forward-complete, time-varying, closed-form, Continuous-depth, second-order, proof-assistant, p-boxes).
The last paragraph ends mid-sentence ('... we use numerical ODE solvers') and continues on page 4 (joined there). No page number or running head.
"""
write(3, items, notes)
