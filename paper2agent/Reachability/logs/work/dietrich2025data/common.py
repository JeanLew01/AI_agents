"""Helper for writing reviewed page JSON files (dietrich2025data)."""
import json, os

D = os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/dietrich2025data-paper/documents/s001-dietrich2025data')

LEFT = (54.0, 299.0)
RIGHT = (313.0, 559.0)


class Page:
    def __init__(self, n):
        self.n = n
        self.path = f'{D}/pages/page-{n:04d}.json'
        self.state = json.load(open(self.path))
        self.items = []
        self.k = 0

    def _id(self):
        self.k += 1
        return f'p{self.n:04d}-r{self.k:03d}'

    def add(self, kind, markdown, bbox, **extra):
        item = {'id': self._id(), 'kind': kind, 'bbox': [float(v) for v in bbox], 'markdown': markdown}
        item.update(extra)
        self.items.append(item)
        return item

    def text(self, md, bbox, **extra):
        return self.add('text', md, bbox, **extra)

    def heading(self, md, bbox):
        return self.add('heading', md, bbox)

    def caption(self, md, bbox, **extra):
        return self.add('caption', md, bbox, **extra)

    def math(self, md, bbox):
        return self.add('text', '$$\n' + md.strip('\n') + '\n$$', bbox)

    def omit(self, bbox, reason):
        return self.add('omit', '', bbox, reason=reason)

    def figure(self, bbox, label, asset_name, **extra):
        return self.add('figure', '', bbox, label=label, asset_name=asset_name, **extra)

    def table(self, bbox, label, asset_name, rows):
        return self.add('table', '', bbox, label=label, asset_name=asset_name, rows=rows)

    def write(self, notes):
        self.state['items'] = self.items
        self.state['reviewed'] = True
        self.state['review_notes'] = notes
        with open(self.path, 'w', encoding='utf-8') as f:
            json.dump(self.state, f, ensure_ascii=False, indent=2)
            f.write('\n')
        print('wrote', self.path, len(self.items), 'items')
