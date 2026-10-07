#!/usr/bin/env python3
"""fixlinks.py PAPER : interval notation such as $p([x])([z])$ contains "](" which markdown (and the package's
link check) reads as a link. Insert an empty LaTeX group, "]{}(", which renders identically."""
import json, re, sys
from pathlib import Path
doc = next((Path('/home/jixia/AI_agents/paper2agent/ParticleFilter/paper-review') / sys.argv[1] / 'documents').iterdir())
total = 0
for f in sorted(doc.glob('pages/page-*.json')):
    p = json.loads(f.read_text(encoding='utf-8')); n = 0
    for it in p['items']:
        md = it.get('markdown') or ''
        new = re.sub(r'\]\((?!https?://|\.\./|mailto:)', ']{}(', md)
        if new != md: n += len(re.findall(r'\]\{\}\(', new)) - len(re.findall(r'\]\{\}\(', md)); it['markdown'] = new
    if n:
        p['review_notes'] += f' [coordinator] {n} occurrence(s) of "](" inside mathematics written as "]{{}}(" (empty LaTeX group, same rendering) so that interval notation is not parsed as a markdown link.'
        f.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding='utf-8'); total += n
print(sys.argv[1], 'fixed', total)
