#!/usr/bin/env python3
"""For every tool-'missing' line: strip LaTeX from the page markdown (taken from pages/*.json), reduce both sides to ASCII
letters and test that every word (>=3 letters) of the PDF line occurs, in order, in the page letter string (neighbouring
pages included for lines cut by page breaks). Lines that fail are printed. Also prints the number differences."""
import json, os, re, unicodedata, sys
D = os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/hashemi2025pca-paper/documents/s001-hashemi2025pca')
v = json.load(open(D + '/verification.json'))
pages = {}
for n in range(1, 17):
    st = json.load(open(f"{D}/pages/page-{n:04d}.json"))
    t = []
    for i in st["items"]:
        if i["kind"] == "omit": continue
        t.append(i.get("markdown", ""))
        if i.get("rows"): t.append(" ".join(" ".join(r) for r in i["rows"]))
    pages[n] = "\n".join(t)
KEEP = {'max', 'min', 'diag', 'Pr', 'text'}
MAP = {'mathsf': '', 'mathrm': '', 'mathcal': '', 'mathbf': '', 'mathbb': ''}
def strip(t):
    t = re.sub(r'\\tag\{[^}]*\}', ' ', t)
    t = re.sub(r'\\([A-Za-z]+)', lambda m: m.group(1) if m.group(1) in KEEP else ' ', t)
    return t
def letters(t):
    t = unicodedata.normalize('NFKD', t)
    return ''.join(c for c in t if c.isascii() and c.isalpha()).lower()
tot = bad = 0
for p in v['pages']:
    n = p['page']
    s = letters(strip(pages.get(n - 1, '')[-2500:])) + letters(strip(pages[n])) + letters(strip(pages.get(n + 1, '')[:1500]))
    for l in p['missing_lines']:
        tot += 1
        ws = [letters(w) for w in re.findall(r"[^\W\d_]{3,}", unicodedata.normalize('NFKD', l['text']))]
        ws = [w for w in ws if len(w) >= 3]
        ok = not ws
        if ws:
            for st_ in [m.start() for m in re.finditer(re.escape(ws[0]), s)]:
                pos, good = st_, True
                for w in ws:
                    j = s.find(w, pos, pos + 400)
                    if j < 0: good = False; break
                    pos = j + len(w)
                if good: ok = True; break
        if not ok:
            bad += 1; print(f"page {n} y={l['bbox'][1]:.0f}: {l['text']!r} words={ws}")
    if "-q" not in sys.argv:
        for key in ("number_differences", "independent_parser_number_differences"):
            d = p[key]
            if d["missing"] or d["extra"]:
                print(f"  p{n} {key[:11]}: missing={d['missing']} extra={d['extra']}")
    print(f"page {n}: lines checked {p['source_text_lines_checked']}, found {p['source_text_lines_found']}, missing {len(p['missing_lines'])}")
print('missing lines', tot, 'unmatched', bad)
