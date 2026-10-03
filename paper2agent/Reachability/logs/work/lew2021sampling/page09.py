from pg import *
from refs import REFS
old={i['id']:i for i in load(9)['items']}
items=[
T('p0009-b000',[108,75,505,128],'**Acknowledgments** The authors were partially supported by the Office of Naval Research, ONR YIP Program, under Contract N00014-17-1-2433. The authors thank the anynomous reviewers for their helpful comments, Spencer Richards for his feedback and suggestions, Robert Dyro for his implementation of (S-ADMM), Riccardo Bonalli for his feedback on theoretical results, James Harrison and Apoorva Sharma for helpful discussions on learning-based control, and Paul-Edouard Sarlin for suggesting related work on shape reconstruction.'),
H('p0009-b001',[108,154,164,163],'## References'),
]
for n in range(1,22):
    i=f'p0009-b{n+1:03d}'
    items.append(T(i,old[i]['bbox'],REFS[n]))
items.append(O('p0009-b023',[296,740,316,753],'Page number "9" in the footer.'))
save(9, items, 'Compared with a 130 dpi render and the authors\' .bbl. Acknowledgments kept verbatim including the funding contract number N00014-17-1-2433 and the authors\' spelling "anynomous". References [1]-[21]: one entry per item in the printed [n] style; all 21 entries read against the page. Corrections of extraction damage: accents restored in [1] (Pál, Szepesvári), line-wrap hyphens restored in [9] (Olivares-Mendez) and [12] (Springer-Verlag), the URL in [19] rejoined (https://arxiv.org/abs/2008.11700), list-bullet prefixes removed. Printed oddities kept: "H.and Chen" in [20], "60 (1)" in [6], "3620 – 3625" in [9], lower-case "lipschitz" and "bayesian" in [15] and [18].')
