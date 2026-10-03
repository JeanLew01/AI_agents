#!/usr/bin/env python3
"""Word-multiset comparison per page: pdftotext source (line-wrap hyphens joined) vs page JSON markdown incl. table
cells (LaTeX commands stripped). Adapted from hewing2019scenario/wordcheck.py. Omitted regions (banner, running
headers) show up as 'in source, not in output'."""
import json, re, subprocess, unicodedata
from collections import Counter
from pagelib import D
def words(t):
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    return Counter(w.lower() for w in re.findall(r"[A-Za-z]{4,}", t))
for n in range(1, 15):
    src = subprocess.run(['pdftotext', '-f', str(n), '-l', str(n), str(D / 'source.pdf'), '-'], capture_output=True, text=True).stdout
    src = re.sub(r'(\w)-\n(\w)', r'\1\2', src)
    src = re.sub(r'[¨´˜ˇ¸]\s?', '', src)                 # spacing accents of the text layer
    page = json.load(open(D / f'pages/page-{n:04d}.json'))
    md = '\n'.join(it.get('markdown', '') + ' ' + ' '.join(' '.join(r) for r in (it.get('rows') or [])) for it in page['items'] if it['kind'] != 'omit')
    md = re.sub(r'\\[A-Za-z]+', ' ', md).replace('&emsp;', ' ')
    a, b = words(src.replace('-', '')), words(md.replace('-', ''))
    print(f'page {n}: source words {sum(a.values())}, output words {sum(b.values())}')
    print('   in source, not in output:', dict(a - b))
    print('   in output, not in source:', dict(b - a))
