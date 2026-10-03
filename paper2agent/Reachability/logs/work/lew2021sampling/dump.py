import json,sys,os
D=os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/lew2021sampling-paper/documents/s001-lew2021sampling')
n=int(sys.argv[1])
p=json.load(open(f'{D}/pages/page-{n:04d}.json'))
print({k:v for k,v in p.items() if k!='items'})
for it in p['items']:
    extra={k:v for k,v in it.items() if k not in('id','kind','bbox','markdown')}
    print('---',it['id'],it['kind'],[round(x,1) for x in it.get('bbox',[])],extra if extra else '')
    print(it.get('markdown',''))
