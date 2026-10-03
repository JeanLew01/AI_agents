from pt import *
items = [
 O([14, 195, 40, 580], "Vertical arXiv stamp in the left margin ('arXiv:2112.05745v3 [eess.SY] 13 Apr 2022'); page furniture, recorded in the conversion notes as the source version.", "arXiv:2112.05745v3 [eess.SY] 13 Apr 2022"),
 H(r"# A Simple and Efficient Sampling-based Algorithm for General Reachability Analysis", [152, 102, 460, 134]),
 T(r"""**Thomas Lew**$^1$ (thomas.lew@stanford.edu)

**Lucas Janson**$^2$ (ljanson@fas.harvard.edu)

**Riccardo Bonalli**$^3$ (riccardo.bonalli@l2s.centralesupelec.fr)

**Marco Pavone**$^1$ (pavone@stanford.edu)

$^1$ Department of Aeronautics and Astronautics, Stanford University

$^2$ Department of Statistics, Harvard University

$^3$ Laboratory of Signals and Systems, University of Paris-Saclay, CNRS, CentraleSupélec""", [89, 152, 523, 268]),
 H(r"## Abstract", [283, 307, 329, 316]),
 T(r"""In this work, we analyze an efficient sampling-based algorithm for general-purpose reachability analysis, which remains a notoriously challenging problem with applications ranging from neural network verification to safety analysis of dynamical systems. By sampling inputs, evaluating their images in the true reachable set, and taking their $\epsilon$-padded convex hull as a set estimator, this algorithm applies to general problem settings and is simple to implement. Our main contribution is the derivation of asymptotic and finite-sample accuracy guarantees using random set theory. This analysis informs algorithmic design to obtain an $\epsilon$-close reachable set approximation with high probability, provides insights into which reachability problems are most challenging, and motivates safety-critical applications of the technique. On a neural network verification task, we show that this approach is more accurate and significantly faster than prior work. Informed by our analysis, we also design a robust model predictive controller that we demonstrate in hardware experiments.""", [109, 324, 503, 454]),
 T(r"""**Keywords:** reachability analysis, random set theory, robust control, neural network verification.""", [109, 454, 503, 466]),
 H(r"## 1. Introduction", [90, 486, 170, 495]),
 F("Figure 1", "figure-1", [326, 480, 518, 572]),
 C(r"""Figure 1: $\epsilon$-RandUP consists of three simple steps: 1) sampling $M$ inputs $x_i$ in $\mathcal{X}$, 2) propagating these inputs through the reachability map $f$, and 3) taking the $\epsilon$-padded convex hull $\hat{\mathcal{Y}}_\epsilon^M$ to approximate the reachable set $\mathcal{Y}$.""", [331, 577, 513, 635]),
 T(r"""Forward reachability analysis entails characterizing the reachable set of outputs of a given function corresponding to a set of inputs. This type of analysis underpins a plethora of applications in model predictive control, neural network verification, and safety analysis of dynamical systems. Sampling-based reachability analysis techniques are a particularly simple class of methods to implement; however, conventional wisdom suggests that if insufficient representative samples are considered, these methods may not be robust in that they cannot rule out edge cases missed by the sampling procedure. Alternatively, by leveraging structure in specific problem formulations or computational methods designed for exhaustivity (e.g., branch and bound), a large range of algorithms with deterministic accuracy and performance""", [90, 508, 523, 681]),
]
page(1, items, r"""Compared the whole page with the 150-dpi render and with the authors' TeX (main.tex lines 6-95). Title merged into a single '#' heading (printed on two lines). Author block rebuilt: the extractor had promoted 'Marco Pavone' to a heading and left <sup> affiliation marks; names, affiliation superscripts and e-mails now in one text item (e-mails are printed in small caps, written here in lower case as in the TeX source; 'CentraleSupélec' accent repaired from 'CentraleSup´elec'). Abstract and Keywords checked word by word; inline math ($\epsilon$) rewritten in LaTeX. The wrapped Figure 1 sits to the right of the first Introduction paragraph and splits it in the extraction; the two halves ('...may not be robust' / 'in that they cannot rule out...') were merged into one paragraph and the figure with its caption placed directly after the section heading so that the sentence, which continues on page 2, is not interrupted. Figure 1 crop [326,480,518,572] checked on a high-resolution crop: contains the sets X, Y, the map f, x_i, y_i, the epsilon arrow and the red label \hat{Y}^M_epsilon; caption excluded. Caption transcribed with LaTeX math from TeX (macro \randup expanded; small-caps 'RANDUP' written 'RandUP'; \X,\Y -> \mathcal{X},\mathcal{Y}). The vertical arXiv stamp is omitted as page furniture. No page number is printed on page 1.""")
