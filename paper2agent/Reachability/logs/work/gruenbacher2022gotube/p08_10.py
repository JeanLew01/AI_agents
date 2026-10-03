from pt import *
import refs
res = refs.place()
E = refs.ENTRIES
def ref_items(p):
    out = []
    for i, b, c in res[p]:
        assert c is None
        out.append({"kind": "text", "bbox": [b[0] - 0.5, b[1] - 0.5, b[2] + 0.5, b[3] + 0.5], "markdown": E[i]})
    return out
COMMON = r"""
The reference list is unnumbered (author-year style, AAAI format), one entry per text item, in the printed alphabetical order. The entry texts were generated from the authors' GoTube.bbl
(accent macros converted to Unicode letters, \emph{...} to Markdown italics, '--' to an en dash, ties to spaces, the year suffixes 2020a/2020b and 2015a/2015b from \natexlab) and each entry was matched against the
PDF text layer of this page by a script (refs.py in the scratch directory: the alphanumeric string of every one of the 64 entries equals that of the corresponding block of PDF lines, entry boundaries found from the
vertical gaps; the single reported difference, Goodfellow et al. 2014, is only the order in which the text layer lists two fragments of one printed line). Every entry of the page was then read on a 170 dpi render
(page 10: 90 dpi, two entries) for punctuation, diacritics and italics. No entry is split across columns or pages. Line-wrap hyphens are not present in the bbl text; real hyphens kept.
"""
n8 = COMMON + r"""
Page 8: heading 'References' (real unnumbered heading; extractor: level 1) and entries 1-29, Abdar et al. 2021 to Gurung et al. 2019 (left column 14 entries, right column 15; the extractor had merged
Athalye/Bak and Chen/Chen into single items). Checked on the render: 'D’Souza' with a typographic apostrophe; 'd'Alché-Buc' with a straight apostrophe (source: \textquotesingle) in Fazlyab et al. 2019;
'Ábrahám', 'Kunčak', 'Donzé', 'Fränzle' with their diacritics (split in the extractor text); 'Flow*' written with an escaped asterisk; 'Arandjelovic' without diacritics as printed.
Kept as printed (source slips): 'Lagrangian Reachabililty' (Cyranka et al. 2017); 'JMLR, 21(2020)'; 'NeurIPS 31' vs 'NeurIPS, volume 31'; 'University of Cambridge, 1(3): 4' (Gal 2016); 'in xspeed'.
The two references used only in the appendix (Dvoretzky, Kiefer, and Wolfowitz 1956 here; Massart 1990 on page 9) are part of this list. No page number or running head.
"""
n9 = COMMON + r"""
Page 9: entries 30-62, Hansen and Walster 2003 to Xu et al. 2021 (left column 17 entries, right column 16). Checked on the render: 'ICML’17' and 'HSCC ’19' with typographic apostrophes;
'd'Alché-Buc' with a straight apostrophe (Salman et al. 2019); 'Müller', 'Püschel' with umlauts; the en dashes of 'Dvoretzky–Kiefer–Wolfowitz' (Massart 1990); page ranges with en dashes.
Kept as printed (source slips): 'Nueral network branching for nueral network verification' (Lu and Mudigonda 2020); 'PATEL, K. K.' in capitals (Tjandraatmadja et al. 2020); 'CAPD:: DynSys' and
'Pre-Print - ww2.ii.uj.edu.pl' (Kapela et al. 2020); 'URL https://github. com/eth-sri/eran' in italics with a space after 'github.' (Singh et al. 2020); 'Zikelic', 'Zgliczynski' without diacritics;
'restricted boltzmann machines'; 'Nature MI'; 'AAAI, 35(9)'; '16(5s)'. No page number or running head.
"""
n10 = COMMON + r"""
Page 10: the last two entries, Zhang et al. 2018 and Zhigljavsky and Zilinskas 2008, at the top of the left column; the rest of the page is blank (the appendix starts on a new page, page 11).
Nothing omitted; no page number or running head.
"""
write(8, [H("## References", (145, 201.5), 55, 67)] + ref_items(8), n8)
write(9, ref_items(9), n9)
write(10, ref_items(10), n10)
