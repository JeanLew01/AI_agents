"""Compare generated reference entries with the extractor's PDF text for a page: alphanumeric-normalised."""
import json, re, sys, unicodedata
from refs import entries
S='/home/jixia/AI_agents/paper2agent/Reachability/logs/work/fan2017dryvr/orig_pages'
def norm(t):
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = t.replace('ø','o')
    return re.sub(r'[^A-Za-z0-9]', '', t).lower()
E_ = {int(e[1:e.index(']')]): e for e in entries()}
for n in sys.argv[1:]:
    p = json.load(open(f'{S}/page-{int(n):04d}.json'))
    for i in p['items']:
        md = i.get('markdown','')
        m = re.match(r'\s*-?\s*\[(\d+)\]', md)
        if not m: 
            print('  (non-ref item)', i['id'], i['kind'], md[:60].replace('\n',' '))
            continue
        k = int(m.group(1))
        a, b = norm(md), norm(E_[k])
        print(k, 'OK' if a == b else f'DIFF\n   pdf: {a}\n   bbl: {b}', i['id'], [round(x) for x in i['bbox']])
