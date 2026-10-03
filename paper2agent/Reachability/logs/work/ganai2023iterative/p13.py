from pagelib import *
from bib import BIB
import json
P = 13
bm = {int(n): v for n, v in json.load(open(S / "bibmap.json")).items()}
items = []
for n in sorted(bm):
    pg, iid = bm[n]
    if pg == P:
        items.append(text(iid, B(P, iid), BIB[n]))
assert len(items) == 21 and items[0]["markdown"].startswith("[40]") and items[-1]["markdown"].startswith("[60]")
items.append(pageno(P))
save(P, items, r"""
Compared with a 170 dpi render of PDF page 13 and with the thebibliography environment in main.tex. Entries [40]-[60]
(end of the reference list; 60 entries in total), one text item per entry, generated from the TeX entries (same
conversion as on page 11) and checked by a script comparison of letters and digits with the PDF text layer (identical
for all 21) and by reading every entry on the render. As printed: '[50] Sven Gronauer. Bullet-safety-gym: ... 2022.'
has no venue; '[58]' has no venue ('..., 2022.'); '[59] Ppo lagrangian pytorch.' is a URL entry, the URL is printed in
typewriter type and given as a code span (underscores kept); '48(3):334–334' in [54]; 'H.K. Khalil' and 'Pearson
Education. Prentice Hall' in [55]; an en dash in 'barrier–value' in [57]; lower-case 'Mujoco:', 'Deepreach:',
'Omnisafe:', 'neural lyapunov'. The page range '2724–2734' in [45] is broken across lines after the dash and is closed
up; the journal name 'IEEE Transactions on Automatic Control' in [49] is hyphenated at a line end ('Transac-/tions').
The appendix starts on the next page. Omitted: printed page number 13.
""")
