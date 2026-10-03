import json,sys
n=int(sys.argv[1])
d=json.load(open(f"orig_pages/page-{n:04d}.json"))
print({k:v for k,v in d.items() if k!='items'})
for it in d['items']:
    b=[round(x,1) for x in it['bbox']]
    print(it['id'],it['kind'],b,it.get('label',''),it.get('asset_name',''),repr(it.get('markdown','')[:90]), ('rows=%d'%len(it['rows']) if it.get('rows') else ''))
