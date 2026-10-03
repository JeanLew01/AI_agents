#!/usr/bin/env python3
"""Word-multiset comparison per page: pdftotext source (line-wrap hyphens joined) vs page JSON markdown (LaTeX commands stripped)."""
import json, os, re, subprocess, unicodedata
from collections import Counter
D = os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/sartipizadeh2019voronoi-paper/documents/s001-sartipizadeh2019voronoi')
def words(t):
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    return Counter(w.lower() for w in re.findall(r"[A-Za-z]{3,}", t))
for n in range(1, 16):
    src = subprocess.run(['pdftotext', '-f', str(n), '-l', str(n), f'{D}/source.pdf', '-'], capture_output=True, text=True).stdout
    src = re.sub(r'(\w)-\n(\w)', r'\1\2', src)
    page = json.load(open(f'{D}/pages/page-{n:04d}.json'))
    md = '\n'.join(it.get('markdown', '') + ' ' + ' '.join(' '.join(r) for r in (it.get('rows') or [])) for it in page['items'] if it['kind'] != 'omit')
    md = re.sub(r'\\(text|mathrm|operatorname)\{', ' {', md)
    md = re.sub(r'\\[A-Za-z]+', ' ', md)
    md = md.replace('&emsp;', ' ')
    a, b = words(src.replace('-', '')), words(md.replace('-', ''))
    miss = dict(a - b); extra = dict(b - a)
    print(f'page {n}: source words {sum(a.values())}, output words {sum(b.values())}')
    print('   in source, not in output:', miss)
    print('   in output, not in source:', extra)
