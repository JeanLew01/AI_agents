from pg import *
B=r'\mathcal{B}'; x=r'\boldsymbol{x}'; mu=r'\boldsymbol{\mu}'; Q=r'\boldsymbol{Q}'; g=r'\boldsymbol{g}'; h=r'\boldsymbol{h}'; f=r'\boldsymbol{f}'
Qn=r'\boldsymbol{Q}_{\mathrm{nom},k}'; Qg=r'\boldsymbol{Q}_{\boldsymbol{g}_k}'
items=[
H('p0014-b000',[108,73,294,85],'## C Additional Experimental Details'),
H('p0014-b001',[108,98,354,108],'### C.1 Uncertainty Propagation using Lipschitz Continuity'),
T('p0014-b002',[108,118,505,139],'In this section, we detail our implementation of the Lipschitz-based uncertainty propagation method which we compare with in Section 6. For these experiments, consider the dynamical system'),
T('p0014-b003',[205,141,510,162],rf'''$$\boldsymbol{{x}}_{{k+1}} = {f}({x}_k) = {h}({x}_k) + {g}({x}_k), \quad {x}_k\in\mathbb{{R}}^n. \tag{{9}}$$'''),
T('p0014-b004',[108,164,504,196],rf'''Note that we drop the dependence on the control input $\boldsymbol{{u}}_k$ for conciseness, and since our comparisons concern a sequence of known open-loop controls. For simplicity, we assume ${h}$ is an affine map, and ${g}$ is Lipschitz continuous, such that for all ${x},{mu}\in\mathbb{{R}}^n$,'''),
T('p0014-b005',[203,198,509,220],rf'''$$|g_i({x})-g_i({mu})| \leq L_{{g_i}} \|{x}-{mu} \|_2, \quad i=1,\ldots,n. \tag{{10}}$$'''),
T('p0014-b006',[108,227,385,237],'The method presented in [13] consists of propagating ellipsoidal sets:'),
T('p0014-b007',[108,242,495,253],rf'''**Definition 2 (Ellipsoidal Set).** A set ${B}({mu}, {Q})$, ${mu}\in\mathbb{{R}}^n,{Q}\in\mathbb{{R}}^{{n\times n}}, {Q}\succ 0$, is an ellipsoidal set if'''),
T('p0014-b008',[204,255,509,278],rf'''$${B}({mu} , {Q}) := \left\{{ {x} \mid ({x}-{mu})^T {Q}^{{-1}} ({x}-{mu}) \leq 1 \right\}}. \tag{{11}}$$'''),
T('p0014-b009',[107,285,505,338],rf'''Assume that ${x}_k\in{B}({mu}_k,{Q}_k)$. The problem consists of computing ${mu}_{{k+1}}, {Q}_{{k+1}}$ such that ${x}_{{k+1}}\in{B}({mu}_{{k+1}},{Q}_{{k+1}})$. Generally, the reachable set of ${f}({x}_k)$ given that ${x}_k$ lies in an ellipsoidal set will not be an ellipsoidal set. However, an outer-approximation is sufficient for control applications where constraints satisfaction needs to be guaranteed. First, we compute the center of the ellipsoid as'''),
T('p0014-b010',[268,335,509,356],rf'''$${mu}_{{k+1}} = {f}({mu}_k). \tag{{12}}$$'''),
T('p0014-b011',[107,355,500,366],rf'''Since ${h}$ is affine, its Jacobian does not depend on ${x}$. Thus, we decompose the error to the mean as'''),
T('p0014-b012',[195,368,417,403],rf'''$$\begin{{aligned}} {x}_{{k+1}}-{mu}_{{k+1}} &= {h}({x}_k)-{h}({mu}_k)+{g}({x}_k)-{g}({mu}_k) \\ &= \nabla {h} \cdot ({x}_k-{mu}_k)+{g}({x}_k)-{g}({mu}_k). \end{{aligned}}$$'''),
T('p0014-b013',[108,411,496,424],rf'''First, given ${x}_k\in{B}({mu}_k,{Q}_k)$, we have $\nabla {h} \cdot ({x}_k-{mu}_k)\in{B}(\mathbf{{0}},{Qn})$, with ${Qn}={h}{Q}_k{h}^T$.'''),
T('p0014-n01',[108,427,496,439],rf'''Second, we use the Lipschitz property of ${g}$ to bound the approximation error component-wise as'''),
T('p0014-b014',[189,441,509,462],rf'''$$|g_i({x}_k)-g_i({mu}_k)|\leq L_{{g_i}} \|{x}_k-{mu}_k\|_2\leq L_{{g_i}} \lambda_{{\max}}({Q}_k), \tag{{13}}$$'''),
T('p0014-b015',[107,464,505,496],rf'''where $\lambda_{{\max}}({Q}_k)$ denotes the largest eigenvalue of ${Q}_k$, and since ${x}_k\in{B}({mu}_k,{Q}_k)$. This defines a rectangular set in which ${g}({x}_k)-{g}({mu}_k)$ is guaranteed to lie, which can be outer-approximated by an ellipsoid as'''),
T('p0014-b016',[107,502,504,520],rf'''$${g}({x}_k)-{g}({mu}_k)\in{B}(\mathbf{{0}},{Qg}), \quad \text{{where}} \ \ {Qg}=n\cdot\mathrm{{diag}}\big((L_{{g_i}}\lambda_{{\max}}({Q}_k)^2), \ i=1,\ldots,n \big), \tag{{14}}$$'''),
T('p0014-n02',[107,522,504,534],r'''where $\mathrm{diag}(\ldots)$ denotes the diagonal matrix with diagonal components $(\ldots)$.'''),
T('p0014-n03',[107,538,504,550],'Finally, the two terms can be combined as'),
T('p0014-b017',[180,552,509,573],rf'''$${x}_{{k+1}}-{mu}_{{k+1}} \in {B}(\mathbf{{0}},{Qn}) \oplus {B}(\mathbf{{0}},{Qg}) \subset {B}(\mathbf{{0}},{Q}_{{k+1}}), \tag{{15}}$$'''),
T('p0014-b018',[107,576,505,598],rf'''where ${Q}_{{k+1}}=\frac{{c+1}}{{c}}{Qn} + (1+c){Qg}$, with $c=\sqrt{{\mathrm{{Tr}}({Qn}/\mathrm{{Tr}}({Qg})}}$, and $\mathrm{{Tr}}(\cdot)$ denotes the trace operator. Finally, combining the terms above and by linearity,'''),
T('p0014-b019',[250,601,509,622],rf'''$${x}_{{k+1}} \in {B}({mu}_{{k+1}},{Q}_{{k+1}}). \tag{{16}}$$'''),
T('p0014-b020',[107,629,505,661],rf'''Starting from ${x}_0\in{B}({mu}_0,{Q}_0)$, and applying this recursion for all $k=0,\ldots, N-1$, this method enables the computation of sequence of sets which outer approximate the true reachable sets of the nonlinear system, given known upper-bounds for the Lipschitz constant of the dynamics.'''),
O('p0014-b021',[296,740,316,753],'Page number "14" in the footer.'),
]
for it in items:
    if it['kind']=='text': print(it['id'], it['markdown'][:400]); print()
save(14, items, 'Compared with a 130 dpi render, two 230 dpi zooms covering the whole text block, and the TeX source. Headings "## C Additional Experimental Details" and "### C.1 Uncertainty Propagation using Lipschitz Continuity". All eight extractor formula images are replaced by LaTeX display items with the printed tags (9)-(16) plus the unnumbered two-line decomposition of the error to the mean; macros expanded (\\h -> \\boldsymbol{h}, \\g -> \\boldsymbol{g}, \\bmu -> \\boldsymbol{\\mu}, \\bQ -> \\boldsymbol{Q}, \\B -> \\mathcal{B}). Definition 2 (bold label with the printed title) consists of its sentence and equation (11) (end of the definition taken from the TeX environment). Paragraph structure restored ("First, given ...", "Second, we use ...", "where diag(...) ...", "Finally, the two terms ..." are separate lines in print). Printed formulas kept exactly, including the authors\' apparent slips, which are NOT corrected: $\\boldsymbol{Q}_{nom,k}=\\boldsymbol{h}\\boldsymbol{Q}_k\\boldsymbol{h}^T$ (written with $\\boldsymbol{h}$, not $\\nabla\\boldsymbol{h}$); bound (13) $\\leq L_{g_i}\\lambda_{\\max}(\\boldsymbol{Q}_k)$; in (14) the square sits inside the inner parenthesis as $(L_{g_i}\\lambda_{\\max}(\\boldsymbol{Q}_k)^2)$; and $c=\\sqrt{\\mathrm{Tr}(\\boldsymbol{Q}_{nom,k}/\\mathrm{Tr}(\\boldsymbol{Q}_{g_k})}$ has an unmatched opening parenthesis under the root, exactly as printed and as in the TeX.')
