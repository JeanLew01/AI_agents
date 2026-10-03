from pt import *
import json, os
refs = json.load(open(os.path.dirname(os.path.abspath(__file__)) + '/refs.json'))
keys = [k for k, _ in refs]
def block(a, b):
    i, j = keys.index(a), keys.index(b)
    return "\n\n".join(t for _, t in refs[i:j+1]), j - i + 1

b11, n11 = block('AamariPhD2017', 'Devroye1980')
b12, n12 = block('Dumbgen1996', 'Liu2021')
b13, n13 = block('Matheron1975', 'ThorpeL4DC2021')
b14, n14 = block('Tran2019', 'Wittig2015')
assert n11 + n12 + n13 + n14 == 50 == len(refs)
common = "Reference entries were generated from the authors' main.bbl (LaTeX accents, \\emph, \\penalty and url macros converted; journal/booktitle italics kept as *...*; en dashes in page ranges) and then every entry on this page was compared with the 150-dpi render: authors, title, venue, volume(issue):pages and year agree. The bibliography is unnumbered (author-year style, sorted alphabetically); entries are separated by blank lines in one text item."

page(11, [
 HDR(),
 H(r"## Acknowledgments", [90, 93, 184, 105]),
 T(r"""The authors thank Robin Brown for her helpful feedback and insightful discussions about neural network verification, Edward Schmerling for his helpful comments and suggestions, and Adam Thorpe for helpful discussions about kernel methods. The NASA University Leadership Initiative (grant #80NSSC20M0163) provided funds to assist the authors with their research, but this article solely reflects the opinions and conclusions of its authors and not any NASA entity. NVIDIA provided funds to assist the authors with their research. L.J. was supported by the National Science Foundation via grant CBET-2112085.""", [90, 115, 523, 207]),
 H(r"## References", [90, 226, 146, 236]),
 T(b11, [90, 248, 523, 683]),
 PNUM(11),
], f"Acknowledgments paragraph compared word by word with the render and the TeX (\\acks block): grant numbers '#80NSSC20M0163' and 'CBET-2112085' checked. Headings fixed to '## Acknowledgments' and '## References' (both unnumbered in print). {common} This page holds {n11} entries (Aamari 2017 ... Devroye and Wise 1980). Accents repaired ('Université', 'Clément'); 'Flow*' written with an escaped asterisk. Lower-case 'delaunay' in two titles is as printed. Running header and page number 11 omitted.")

page(12, [
 HDR(),
 T(b12, [90, 94, 523, 700]),
 PNUM(12),
], f"{common} This page holds {n12} entries (Dumbgen and Walther 1996 ... Liu et al. 2021). Checked in particular: the arXiv URL of Everett et al. (https://arxiv.org/abs/2101.01815), Federer '(93):418–491' (no volume printed), 'R. Harman and V Lacko' (no period after V, as printed), 'dreach: $\\delta$-reachability', Lew et al. 2022 'In Press.', Liu et al. '4(3-4):244–404'. A stray space printed before the comma after the italic booktitle of Kong et al. was not reproduced. Running header and page number 12 omitted.")

page(13, [
 HDR(),
 T(b13, [90, 94, 523, 706]),
 PNUM(13),
], f"{common} This page holds {n13} entries (Matheron 1975 ... Thorpe et al. 2021). Checked in particular: the two URLs (https://math.stackexchange.com/q/162873 and https://arxiv.org/abs/1907.08627), the two Rodriguez-Casal and Saavedra-Nieves entries (2016 and 2019; 'data-driven' is a real compound that is printed across a line break in the second), the two Schneider entries (1988, 2014), 'Schürmann' umlaut repaired, 'O'Kelly' apostrophe, and the author string 'Oishi M. M. K.' printed in that order. Running header and page number 13 omitted.")

page(14, [
 HDR(),
 T(b14, [90, 94, 523, 276]),
 PNUM(14),
], f"{common} This page holds the last {n14} entries (Tran et al. 2019 ... Wittig et al. 2015); the rest of the page is blank. Checked in particular: Walther page range printed with spaces around the dash ('2273 – 2299'), 'Y.W. Teh' without space, and the author string 'Bernelli-Zazzera F.' printed in that order. Line-wrap hyphen in 'algo-rithm' removed. Running header and page number 14 omitted.")
