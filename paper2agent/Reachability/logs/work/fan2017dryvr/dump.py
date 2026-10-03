import json,sys
S='/home/jixia/AI_agents/paper2agent/Reachability/logs/work/fan2017dryvr/orig_pages'
full = len(sys.argv)>2
for n in sys.argv[1].split(','):
    n=int(n)
    p=json.load(open(f'{S}/page-{n:04d}.json'))
    print(f'=== page {n} {p["width"]}x{p["height"]} warnings={p.get("warnings")}')
    for i in p['items']:
        md=i.get('markdown','')
        extra={k:v for k,v in i.items() if k not in('id','kind','bbox','markdown','source_class')}
        print(i['id'],i['kind'],[round(x,1) for x in i['bbox']],extra if extra else '')
        print('   ', md if full else (md[:150]+' ... '+md[-80:] if len(md)>240 else md))
