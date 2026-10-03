import re, os, json
T=os.path.expanduser('~/AI_agents/paper2agent/Reachability/tex-source/lew2022simple/main.bbl')
src=open(T).read()
body=src.split('\\begin{thebibliography}{50}')[1].split('\\end{thebibliography}')[0]
ents=re.split(r'\\bibitem\[', body)[1:]
out=[]
for e in ents:
    # drop the label [..]{key}
    m=re.match(r'(.*?)\]\{([^}]*)\}\n', e, flags=re.S)
    key=m.group(2); t=re.sub(r'\\penalty0\s*','',e[m.end():])
    t=t.replace('\\newblock','').replace('\\penalty0','')
    t=re.sub(r'\s+',' ',t).strip()
    t=t.replace("Universit\\'e","Université").replace("Cl{\\'{e}}ment","Clément").replace('Sch\\"urmann','Schürmann')
    t=t.replace('{\\&}','&').replace('.\\ ','. ').replace('~',' ')
    t=re.sub(r'\\url\{([^}]*)\}', r'\1', t)
    t=re.sub(r'\\emph\{((?:[^{}]|\{[^{}]*\})*)\}', lambda mm: '*'+mm.group(1).strip()+'*', t)
    t=t.replace('{','').replace('}','')
    t=t.replace('--','–')
    t=t.replace('Flow*:','Flow\\*:')
    t=re.sub(r' +',' ',t)
    t=t.replace(' *,','*,')
    assert '\\' not in t.replace('\\*','').replace('$\\delta$',''), t
    out.append((key,t))
json.dump(out, open(os.path.dirname(os.path.abspath(__file__))+'/refs.json','w'), indent=1, ensure_ascii=False)
for k,t in out: print(t); print()
print(len(out))
