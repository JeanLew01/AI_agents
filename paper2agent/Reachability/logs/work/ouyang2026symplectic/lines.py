import json,sys,os
D=os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/ouyang2026symplectic-paper/documents/s001-ouyang2026symplectic")
n=int(sys.argv[1])
d=json.load(open(f"{D}/evidence/page-{n:04d}.json"))
L=[l for l in d['lines']]
def col(l): return 0 if l['bbox'][0]<306 else 1
for c in (0,1):
    print('--- col',c)
    for l in sorted([l for l in L if col(l)==c], key=lambda l:(l['bbox'][1],l['bbox'][0])):
        b=l['bbox']; print(f"{b[0]:6.1f} {b[1]:6.1f} {b[2]:6.1f} {b[3]:6.1f}  {l['text'][:70]}")
