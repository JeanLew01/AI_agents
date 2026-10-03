import json, os
D=os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/lew2021sampling-paper/documents/s001-lew2021sampling')
def load(n):
    return json.load(open(f'{D}/pages/page-{n:04d}.json'))
def save(n, items, notes):
    p=load(n)
    ids=[i['id'] for i in items]
    assert len(ids)==len(set(ids)), 'dup ids'
    for it in items:
        assert it['id'].startswith(f'p{n:04d}-'), it['id']
        b=it['bbox']; assert 0<=b[0]<b[2]<=612 and 0<=b[1]<b[3]<=792, it
        if it['kind'] in ('text','caption','heading'):
            md=it['markdown']; assert md.strip(), it['id']
            assert md.count('$')%2==0, ('odd $', it['id'])
    p['items']=items; p['reviewed']=True; p['review_notes']=notes
    json.dump(p, open(f'{D}/pages/page-{n:04d}.json','w'), indent=2, ensure_ascii=False)
    print('saved page',n,len(items),'items')
def T(id,bbox,md,**kw): return {'id':id,'kind':'text','bbox':bbox,'markdown':md,**kw}
def H(id,bbox,md): return {'id':id,'kind':'heading','bbox':bbox,'markdown':md}
def C(id,bbox,md,**kw): return {'id':id,'kind':'caption','bbox':bbox,'markdown':md,**kw}
def F(id,bbox,label,asset,**kw): return {'id':id,'kind':'figure','bbox':bbox,'markdown':'','label':label,'asset_name':asset,**kw}
def O(id,bbox,reason): return {'id':id,'kind':'omit','bbox':bbox,'markdown':'','reason':reason}
