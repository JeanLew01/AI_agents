from pagelib import *
from refs import ref_items

items = ref_items(19, 11, 22) + [pageno(19, [300.0, 696.0, 311.0, 703.0])]

save(19, items, r"""
Compared with a 190-dpi render of the text block and with main2.bbl. Bibliography entries [11]-[22], one item per entry, generated from the authors' .bbl and compared automatically with the PDF text layer (letters and digits identical for all twelve entries) and read entry by entry on the render. Checked details: 'Joël Ouaknine' [11], 'Bjørner' [14], 'Donzé' [17], [18]; '14(04):583–604' [11]; page ranges 192–207, 208–219, 337–340, 165–168, 114–129, 167–170, 174–189, 144–161, 536–543, 1–10; 'vol. 3829 in LNCS' inside the italic venue of [19]; 'In *In the Proceedings of ...*' (doubled 'In') and 'volume 9206 of *LNCS*' in [21]; 'SysTems' [15] and 'smt solver' [14] as printed; [20] is a PhD thesis with italic title. Real hyphens at line ends kept ('counterexample-guided' [11], 'trajectory-based' [15]); line-wrap hyphens removed. Omitted: page number 19.
""")
