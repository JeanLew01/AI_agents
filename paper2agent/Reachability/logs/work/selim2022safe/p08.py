from pagelib import *
from refs import entries

P = 8
E = entries()
# [17] is extractor item b002, ..., [55] is b040
items = furniture(P) + [text(f"p0008-ref{n:02d}", B(P, f"b{n - 15:03d}"), E[n]) for n in range(17, 56)]

save(P, items, r"""
Compared with the 170 dpi render of PDF page 8 and with the authors' main.bbl. Running header and page number 8
omitted. The page contains only bibliography entries [17]-[55] in two columns (left column [17]-[36], right column
[37]-[55]); one text item per entry, in printed order. The entries were generated from main.bbl (IEEEtran.bst
output: ties, \emph, quotes, dashes and accents converted) and each was compared with the PDF text layer of the
corresponding extractor item (identical alphanumeric content for all 39 entries) and read against the page image.
The extractor's list markers ('- [17] ...') were removed. Compound hyphens broken at line ends were restored from
the .bbl: '[32] receding-horizon', '[34] non-communicating' (extractor: 'noncommunicating'), '[53] Off-policy' (extractor:
'Offpolicy'); page ranges broken across lines were closed up ('[17] pp. 145–|152', '[33] pp. 1326–|1345');
line-wrap hyphens removed ('learn-|ing', 'stabiliza-|tion', 'Inter-|national', 'rein-|forcement', 'as-|sessment',
'Va-|sudevan', 'Con-|strained', 'reinforce-|ment'). Accents: '[40] Technische Universität München', '[42] F.
Allgöwer' (extractor had 'Allg¨ower'). Kept as printed: lower-case title words produced by the bibliography style
('lyapunov-based', 'rts', 'gnss-based uas', 'ddpg', 'Optnet'), '[25] ... 10 2018' and '[40] ... 07 2010' (month
numbers before the year), '[33] ... no. 10-11, pp. 1326–1345' with an en dash in 'human–robot', '[29] ... 2022, in
Press', '[22] ... no. 01'. URLs in [23] and [26] are plain text as printed. Bounding boxes are those of the
extractor items b002-b040, which correspond one to one to entries [17]-[55].
""")
