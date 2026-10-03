from pagelib import *
from refs import ref_items

items = ref_items(21, 34, 45) + [pageno(21, [300.0, 696.0, 311.0, 703.0])]

save(21, items, r"""
Compared with a 190-dpi render of the text block and with main2.bbl. Bibliography entries [34]-[45], one item per entry, generated from the authors' .bbl and compared automatically with the PDF text layer (letters and digits identical for all twelve entries, except that the Greek letter of [44] is not alphanumeric in the PDF text) and read entry by entry on the render. Checked details: page ranges 272–286, 103–116, 265–293, 287–300, 253–262, 329–342, 430–445, 200–205; '55(1):116–126' [35]; '41(3):201–211' and the ampersand of 'Systems & control letters' [45]; 'Ivančić' [42]; [43] is the Kearns-Vazirani book with italic title ('MIT press, 1994'), the reference for the PAC argument of Section 3.1; [44] 'dreach: $\delta$-reachability' (Greek delta written as inline math, hyphen real); lower-case titles as printed ('cornell', 'simulink/stateflow', '17th international conference on Hybrid systems: computation and control'). Line-wrap hyphens removed. Omitted: page number 21.
""")
