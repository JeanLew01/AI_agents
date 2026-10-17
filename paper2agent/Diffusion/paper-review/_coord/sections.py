#!/usr/bin/env python3
"""sections.py PAPER.md : for every heading list the equation tags, figure/table/algorithm links and theorem-like labels inside it (up to the next heading)."""
import re,sys
text=open(sys.argv[1],encoding='utf-8').read().split('\n')
cur=None; out=[]
def flush():
    if cur: out.append(cur)
for line in text:
    m=re.match(r'^(#{1,4}) (.+)$',line)
    if m:
        flush(); cur={'h':m.group(2),'lvl':len(m.group(1)),'tags':[],'assets':[],'thm':[]}
        continue
    if cur is None: continue
    cur['tags']+=re.findall(r'\\tag\{([^}]+)\}',line)
    cur['assets']+=re.findall(r'\]\(\.\./assets/[a-z_]+/([a-z0-9-]+)\.(?:jpg|csv)\)',line)
    cur['thm']+=re.findall(r'\*\*((?:Definition|Assumption|Lemma|Theorem|Proposition|Corollary|Problem|Remark)[^*]{0,40}?)[.:]?\*\*',line)
flush()
for c in out:
    def rng(t):
        return (t[0]+'..'+t[-1]+f' ({len(t)})') if len(t)>2 else ', '.join(t)
    print('  '*(c['lvl']-1)+c['h'][:70],'| eq:',rng(c['tags']) or '-','| assets:',' '.join(c['assets']) or '-','| thm:','; '.join(c['thm']) or '-')
