#!/usr/bin/env python3
"""Word-multiset comparison per page: pdftotext source (line-wrap hyphens joined) vs page JSON markdown (LaTeX commands stripped)."""
import json, os, re, subprocess, unicodedata, sys
from collections import Counter
D = os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/fan2017dryvr-paper/documents/s001-fan2017dryvr')
def words(t):
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    return Counter(w.lower() for w in re.findall(r"[A-Za-z]{3,}", t))
tm = te = 0
for n in range(1, 26):
    src = subprocess.run(['pdftotext', '-f', str(n), '-l', str(n), f'{D}/source.pdf', '-'], capture_output=True, text=True).stdout
    src = re.sub(r'(\w)-\n(\w)', r'\1\2', src)
    page = json.load(open(f'{D}/pages/page-{n:04d}.json'))
    md = '\n'.join(it.get('markdown', '') + ' ' + ' '.join(' '.join(r) for r in (it.get('rows') or [])) for it in page['items'] if it['kind'] != 'omit' and 'tnote' not in it['id'])
    md = re.sub(r'\\(text|mathcal|mathbb|mathsf|mathit|mathrm|frac|left|right|quad|qquad|ldots|tag|in|leq|geq|to|subseteq|subset|forall|exists|setminus|sum|ln|cup|cap|circ|times|rangle|langle|rightarrow|gets|preceq|emptyset|neq|notin|wedge|cdot|ell|tau|alpha|beta|gamma|delta|epsilon|lambda|pi|sigma|Theta|Gamma|omega|square|xrightarrow|ast)(?![a-zA-Z])', ' ', md)
    md = md.replace('&emsp;', ' ').replace('\\_', '_')
    a, b = words(src.replace('-', '')), words(md.replace('-', ''))
    miss = dict(a - b); extra = dict(b - a)
    tm += sum(miss.values()); te += sum(extra.values())
    print(f'page {n}: src {sum(a.values())}, out {sum(b.values())}  missing: {miss}  extra: {extra}')
print('total missing', tm, 'extra', te)
