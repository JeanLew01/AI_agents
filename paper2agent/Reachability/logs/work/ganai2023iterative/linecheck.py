#!/usr/bin/env python3
"""For every tool-'missing' line: strip LaTeX from the page markdown (command names deleted except function names),
reduce both sides to ASCII letters, and test that every word of the PDF line with >=3 letters occurs in order in the
letter string of the page (plus the neighbouring pages). Lines that fail are printed."""
import json, os, re, unicodedata
D=os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/ganai2023iterative-paper/documents/s001-ganai2023iterative')
v=json.load(open(D+'/verification.json'))
KEEP={'max','min','arg','sup','lim','log'}
def strip(t):
    t=re.sub(r'\\tag\{[^}]*\}',' ',t)
    t=re.sub(r'\\([A-Za-z]+)',lambda m: m.group(1) if m.group(1) in KEEP else ' ',t)
    return t.replace('&emsp;',' ')
def letters(t):
    t=unicodedata.normalize('NFKD',t)
    return ''.join(c for c in t if c.isascii() and c.isalpha()).lower()
def pagetext(n):
    try: p=json.load(open(f'{D}/pages/page-{n:04d}.json'))
    except FileNotFoundError: return ''
    return '\n'.join(i.get('markdown','') for i in p['items'] if i['kind'] in ('text','caption','heading'))
tot=bad=0
for p in v['pages']:
    n=p['page']
    s=letters(strip(pagetext(n-1)[-1500:]))+letters(strip(pagetext(n)))+letters(strip(pagetext(n+1)[:600]))
    for l in p['missing_lines']:
        tot+=1
        ws=[letters(w) for w in re.findall(r"[^\W\d_]{3,}",unicodedata.normalize('NFKD',l['text']))]
        ws=[w for w in ws if len(w)>=3]
        ok=not ws
        if ws:
            for st in [m.start() for m in re.finditer(re.escape(ws[0]),s)]:
                pos=st; good=True
                for w in ws:
                    j=s.find(w,pos,pos+500)
                    if j<0: good=False; break
                    pos=j+len(w)
                if good: ok=True; break
        if not ok:
            bad+=1; print(f"page {n} y={l['bbox'][1]:.0f}: {l['text']!r}")
print('missing lines',tot,'unmatched',bad)
