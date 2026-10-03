#!/usr/bin/env python3
"""Compare every inline/display formula of the built paper.md with the authors' TeX source after
normalisation (whitespace removed, a fixed list of equivalent spellings mapped). Formulas that do
not occur in the normalised TeX are printed for manual review."""
import re, sys
from pathlib import Path
R = Path.home() / 'AI_agents/paper2agent/Reachability'
tex = (R / 'tex-source/dietrich2025data/root.tex').read_text() + (R / 'tex-source/dietrich2025data/reachable_fig.tex').read_text()
tex = '\n'.join(l for l in tex.splitlines() if not l.lstrip().startswith('%'))
tex = re.sub(r'(?<!\\)%.*', '', tex)
md = Path(sys.argv[1]).read_text()
MAP = [(r'\dotsc', r'\dots'), (r'\not\in', r'\notin'), (r'\rm{Vol}', r'\mathrm{Vol}'), (r'{\rmVol}', r'\mathrm{Vol}'), (r'{\rm Vol}', r'\mathrm{Vol}'),
       (r'\mathds{1}', r'\mathbb{1}'), (r'\theta^*', r'\theta^{\ast}'), (r'\label{eq:h_prob_guarantee}', ''),
       (r'\sum^m_{i=1}', r'\sum_{i=1}^{m}'), (r'\sum_{i=1}^m', r'\sum_{i=1}^{m}'), (r'\sum^{M}_{i=1}', r'\sum_{i=1}^{M}'), (r'\sum^t_{\tau=0}', r'\sum_{\tau=0}^{t}'),
       (r'n_{\theta}', r'n_\theta'), (r'\binomMj', r'\binom{M}{j}'), (r'\mu_{D}', r'\mu_D'), (r'\le0', r'\leq0'), (r'&', ''), (r'\\', ''), ('\\,', ''), (r'\quad', ''), (r'\;', ''),
       (r'\notag', ''), (r'\ge1', r'\geq1')]
def norm(s):
    s = re.sub(r'\\label\{[^}]*\}', '', s)
    s = re.sub(r'\\tag\{[^}]*\}', '', s)
    s = re.sub(r'\s+', '', s)
    for a, b in MAP:
        s = s.replace(re.sub(r'\s+', '', a), b)
    s = s.replace(r'\le', r'\leq').replace(r'\leqq', r'\leq').replace(r'\leqft', r'\left').replace(r'\ge', r'\geq').replace(r'\geqq', r'\geq')
    return s
T = norm(tex)
displays = re.findall(r'\$\$(.+?)\$\$', md, flags=re.S)
rest = re.sub(r'\$\$(.+?)\$\$', ' ', md, flags=re.S)
inl = list(dict.fromkeys(re.findall(r'\$([^$\n]+?)\$', rest)))
bad = 0
for kind, items in (('display', displays), ('inline', inl)):
    for m in items:
        n = norm(m)
        # displays: compare line by line (alignment structure differs)
        parts = [norm(x) for x in re.split(r'\\\\|\\begin\{[a-z]+\}(?:\{[a-z]+\})?|\\end\{[a-z]+\}', m)] if kind == 'display' else [n]
        for part in parts:
            if part and part not in T:
                bad += 1
                print(f'[{kind}] NOT IN TEX: {part}')
print('formulas:', len(displays), 'displays,', len(inl), 'unique inline; not found:', bad)
