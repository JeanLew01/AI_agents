import json,sys,os
D=os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/lew2022simple-paper/documents/s001-lew2022simple')
for n in sys.argv[1:]:
    p=json.load(open(f'{D}/pages/page-{int(n):04d}.json'))
    print('PAGE',n,p.get('reviewed'))
    for it in p['items']:
        print(it['id'],it['kind'],[round(x) for x in it['bbox']],it.get('label',''),it.get('asset_name',''),'|',it.get('markdown','')[:110].replace('\n',' '), '|', it.get('reason',''))
