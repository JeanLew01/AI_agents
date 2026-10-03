#!/usr/bin/env python3
"""Word-multiset comparison per page: pdftotext source (line-wrap hyphens joined) vs page JSON markdown (LaTeX commands stripped)."""
import json, os, re, subprocess, unicodedata
from collections import Counter
D = os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/lew2022simple-paper/documents/s001-lew2022simple')
def words(t):
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    return Counter(w.lower() for w in re.findall(r"[A-Za-z]{4,}", t))
for n in range(1, 26):
    page = json.load(open(f'{D}/pages/page-{n:04d}.json'))
    src = ''
    # text outside figure crops only: use the evidence lines (same text layer) to drop figure text
    ev = json.load(open(f'{D}/evidence/page-{n:04d}.json'))
    excl = [i['bbox'] for i in page['items'] if i['kind'] == 'figure']
    def inside(l):
        b = l['bbox']; cx, cy = (b[0]+b[2])/2, (b[1]+b[3])/2
        return any(e[0] <= cx <= e[2] and e[1] <= cy <= e[3] for e in excl)
    src = '\n'.join(l['text'] for l in ev['lines'] if not inside(l))
    src = re.sub(r'(\w)-\n(\w)', r'\1\2', src)
    md = '\n'.join(it.get('markdown', '') for it in page['items'])
    md = re.sub(r'\\[A-Za-z]+', ' ', md)
    a, b = words(src.replace('-', '')), words(md.replace('-', ''))
    miss = dict(a - b); extra = dict(b - a)
    print(f'page {n}: source words {sum(a.values())}, output words {sum(b.values())}')
    if miss: print('   in source, not in output:', miss)
    if extra: print('   in output, not in source:', extra)
