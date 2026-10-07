#!/usr/bin/env python3
"""automet.py PAPER SPEC.json : build a draft, derive navigation (one entry per heading, purpose = contents summary)
and write _coord/meta/PAPER.json from SPEC {title, notes[], source_review_notes, reading_order_moves?[{ids,after|before}], purposes?{heading: text}}."""
import json, re, subprocess, sys, shutil
from pathlib import Path
ROOT = Path('/home/jixia/AI_agents/paper2agent/ParticleFilter'); PR = ROOT / 'paper-review'
paper, spec = sys.argv[1], json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
doc = next((PR / paper / 'documents').iterdir())
order = None
if spec.get('reading_order_moves'):
    ids = [it['id'] for f in sorted(doc.glob('pages/page-*.json')) for it in json.loads(f.read_text())['items'] if it['kind'] != 'omit']
    n = len(ids)
    for mv in spec['reading_order_moves']:
        ids = [i for i in ids if i not in mv['ids']]
        k = ids.index(mv['before']) if 'before' in mv else ids.index(mv['after']) + 1
        ids = ids[:k] + mv['ids'] + ids[k:]
    assert len(ids) == n == len(set(ids)); order = ids
    plan = json.loads((doc / 'plan.json').read_text()); plan['reading_order'] = order
    (doc / 'plan.json').write_text(json.dumps(plan, ensure_ascii=False, indent=2))
tmp = ROOT / 'staging' / f'.draft-{paper}'; shutil.rmtree(tmp, ignore_errors=True)
subprocess.run(['/home/jixia/.local/bin/uv', 'run', '/home/jixia/.claude/skills/paper2agent/paper2skill/scripts/paper_bundle.py', 'build',
                '--work', str(PR / paper), '--output', str(tmp), '--draft'], capture_output=True)
lines = (tmp / 'references' / 'paper.md').read_text(encoding='utf-8').split('\n')
secs, cur, seen = [], None, set()
for line in lines:
    m = re.match(r'^(#{2,4}) (.+)$', line)
    if m:
        cur = {'h': m.group(2), 'tags': [], 'assets': [], 'thm': []}; secs.append(cur); continue
    if cur is None: continue
    cur['tags'] += re.findall(r'\\tag\{([^}]+)\}', line)
    cur['assets'] += re.findall(r'\]\(\.\./assets/[a-z_]+/([a-z0-9-]+)\.(?:jpg|csv)\)', line)
    cur['thm'] += re.findall(r'\*\*((?:Definition|Assumption|Lemma|Theorem|Proposition|Corollary|Problem|Remark|Example|Algorithm)[^*]{0,40}?)[.:]?\*\*', line)
nav = []
for c in secs:
    if c['h'] in seen or c['h'].startswith('Conversion'): continue   # duplicate heading text cannot be addressed twice
    seen.add(c['h'])
    parts = []
    if c['tags']: parts.append('equations (' + (c['tags'][0] + ')-(' + c['tags'][-1] if len(c['tags']) > 1 else c['tags'][0]) + ')')
    if c['thm']: parts.append('; '.join(dict.fromkeys(c['thm'])))
    if c['assets']: parts.append(', '.join(dict.fromkeys(c['assets'])))
    auto = '; '.join(parts)
    p = spec.get('purposes', {}).get(c['h'])
    nav.append({'file': 'references/paper.md', 'heading': c['h'], 'purpose': (p + (' [' + auto + ']' if auto else '')) if p else (auto or 'Section text')})
meta = {'title': spec['title'], 'notes': spec['notes'], 'source_review_notes': spec['source_review_notes'], 'navigation': nav}
if order: meta['reading_order'] = order
(PR / '_coord' / 'meta' / f'{paper}.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')
shutil.rmtree(tmp, ignore_errors=True)
for e in nav: print(e['heading'][:60], '|', e['purpose'][:110])
