from pagelib import *
from refs import ref_items

items = [heading("p0018-b000", [133.0, 124.0, 210.0, 135.0], "## References")] + ref_items(18, 1, 10) + [pageno(18, [300.0, 696.0, 311.0, 703.0])]

save(18, items, r"""
Compared with a 190-dpi render of the text block and with main2.bbl. 'References' is an unnumbered section heading (##). Entries [1]-[10], one item per entry, in the printed plain-style format '[n] Authors. Title. In *Venue*, pages. Publisher, year.'; the text was generated from the authors' .bbl (accent macros converted to Unicode, en dashes for page ranges, italics of the venue/journal/book title kept with * markers) and compared (a) automatically, entry by entry, with the PDF text layer after reducing both to letters and digits - all ten agree apart from the accent glyphs of [8] and [9] - and (b) by reading all ten entries on the render. Checked details: diacritics 'Ivančić' [1], 'Kārlis Čerāns' [8], 'Ábrahám' [9] (the extractor had split accents such as 'Ivanˇci´c', 'K¯arlis'); page ranges 208–223, 365–370, 116–131, 73–88, 302–315, 258–263, 76–90; 'Flow*:' in [9] has a literal asterisk; in [4] the period is inside the italic title and 'Syposium' is the printed spelling; [10] has lower-case 'International workshop on hybrid systems: computation and control' as printed. Extractor damage fixed: 'Assumeguarantee' -> 'Assume-guarantee' [6] and 'polyhedralinvariant' -> 'polyhedral-invariant' [10] (real hyphens at line ends per the .bbl); 'pages 73– 88' -> '73–88' [7]; line-wrap hyphens removed. Omitted: page number 18.
""")
