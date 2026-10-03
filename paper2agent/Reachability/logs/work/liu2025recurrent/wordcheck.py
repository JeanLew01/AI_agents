#!/usr/bin/env python3
"""Word-multiset comparison per page: pdftotext source (line-wrap hyphens joined) vs page JSON markdown (LaTeX commands stripped)."""
import json, os, re, subprocess, unicodedata
from collections import Counter
D = os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/liu2025recurrent-paper/documents/s001-liu2025recurrent')
def words(t):
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    return Counter(w.lower() for w in re.findall(r"[A-Za-z]{4,}", t))
for n in range(1, 9):
    src = subprocess.run(['pdftotext', '-f', str(n), '-l', str(n), f'{D}/source.pdf', '-'], capture_output=True, text=True).stdout
    src = re.sub(r'(\w)-\n(\w)', r'\1\2', src)          # join line-wrap hyphens (also joins real compounds; handled below)
    page = json.load(open(f'{D}/pages/page-{n:04d}.json'))
    md = '\n'.join(it.get('markdown', '') + ' ' + ' '.join(' '.join(r) for r in (it.get('rows') or [])) for it in page['items'] if it['kind'] != 'omit')
    md = re.sub(r'\\(text|mathcal|mathbb|mathsf|mathbf|bar|tilde|dot|ddot|frac|left|right|begin|end|quad|ldots|tag|in|le|ge|to|sim|mid|subseteq|subset|ominus|bigcap|forall|Rightarrow|infty|setminus|sum|binom|sqrt|ln|min|max|Pr|log|det|exp|cos|sin|theta|alpha|beta|delta|lambda|pi|Sigma|pm|approx|square|ll|Big|times|cases|bmatrix|aligned)\b', ' ', md)
    md2 = md.replace('-', '')                            # compare compounds joined, like the source join above
    a, b = words(src.replace('-', '')), words(md2)
    miss = {w: c for w, c in (a - b).items()}
    extra = {w: c for w, c in (b - a).items()}
    print(f'page {n}: source words {sum(a.values())}, output words {sum(b.values())}')
    print('   in source, not in output:', miss)
    print('   in output, not in source:', extra)
