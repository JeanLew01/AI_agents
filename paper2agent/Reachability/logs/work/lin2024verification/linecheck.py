#!/usr/bin/env python3
"""For every tool-'missing' line: strip LaTeX from the built page text (formatting/relation/Greek commands deleted,
function names such as max/min/tanh/diag/det kept), reduce both sides to ASCII letters, and test that every word of the
PDF line with >=3 letters occurs as a substring of the page letter string, in order. Lines that fail are printed."""
import json, os, re, unicodedata
D=os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/lin2024verification-paper/documents/s001-lin2024verification')
v=json.load(open(D+'/verification.json')); b=json.load(open(D+'/build.json'))
md=open(os.path.join(b['output'],b['paper']),encoding='utf-8').read()
ch=re.split(r'<!-- PDF page (\d+) -->',md); pages={int(ch[i]):ch[i+1] for i in range(1,len(ch),2)}
KEEP={'max','min','tanh','det','diag','Gamma'}
def strip(t):
    t=re.sub(r'\\tag\{[^}]*\}',' ',t)
    t=re.sub(r'\\([A-Za-z]+)',lambda m: m.group(1) if m.group(1) in KEEP else ' ',t)
    t=t.replace('&emsp;',' ')
    return t
def letters(t):
    t=unicodedata.normalize('NFKD',t)
    return ''.join(c for c in t if c.isascii() and c.isalpha()).lower()
tot=bad=0
for p in v['pages']:
    n=p['page']
    s=letters(strip(pages.get(n-1,'')[-1500:]))+letters(strip(pages[n]))+letters(strip(pages.get(n+1,'')[:600]))
    for l in p['missing_lines']:
        tot+=1
        ws=[letters(w) for w in re.findall(r"[^\W\d_]{3,}",unicodedata.normalize('NFKD',l['text']))]
        ws=[w for w in ws if len(w)>=3]
        # find in order (allowing any start)
        ok=False
        if not ws: ok=True
        else:
            for st in [m.start() for m in re.finditer(re.escape(ws[0]),s)]:
                pos=st; good=True
                for w in ws:
                    j=s.find(w,pos, pos+400)
                    if j<0: good=False; break
                    pos=j+len(w)
                if good: ok=True; break
        if not ok:
            bad+=1; print(f"page {n} y={l['bbox'][1]:.0f}: {l['text']!r} words={ws}")
print('missing lines',tot,'unmatched',bad)
