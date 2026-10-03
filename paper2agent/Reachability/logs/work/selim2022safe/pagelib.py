"""Helpers used by the per-page scripts (pNN.py) to write reviewed page JSON files for selim2022safe.

Bounding boxes are read by item id from the backup of the extractor output (orig-pages/), made before the
first edit, or given explicitly in PDF points (top-left origin)."""
import json
import pathlib

R = pathlib.Path.home() / "AI_agents/paper2agent/Reachability"
D = R / "paper-review/selim2022safe-paper/documents/s001-selim2022safe"
S = R / "logs/work/selim2022safe"

_ORIG = {}


def B(page, *ids):
    """Union of the extractor bboxes of the given original item ids (short form 'b007')."""
    if page not in _ORIG:
        st = json.loads((S / f"orig-pages/page-{page:04d}.json").read_text(encoding="utf-8"))
        _ORIG[page] = {i["id"]: i["bbox"] for i in st["items"]}
    bs = [_ORIG[page][f"p{page:04d}-{k}"] for k in ids]
    return [min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs)]


def text(id, bbox, md, **kw):
    return dict(id=id, kind="text", bbox=bbox, markdown=md.strip(), **kw)


def heading(id, bbox, md):
    return dict(id=id, kind="heading", bbox=bbox, markdown=md.strip())


def caption(id, bbox, md):
    return dict(id=id, kind="caption", bbox=bbox, markdown=md.strip())


def omit(id, bbox, md, reason):
    return dict(id=id, kind="omit", bbox=bbox, markdown=md, reason=reason)


def figure(id, bbox, label, asset_name, **kw):
    return dict(id=id, kind="figure", bbox=bbox, markdown="", label=label, asset_name=asset_name, **kw)


def table(id, bbox, label, asset_name, rows):
    n = len(rows[0])
    assert all(len(r) == n for r in rows), "ragged table"
    assert all(isinstance(c, str) for r in rows for c in r)
    return dict(id=id, kind="table", bbox=bbox, markdown="", label=label, asset_name=asset_name, rows=rows)


def alg(md):
    """Algorithm transcription: one paragraph per printed line; each leading '>' is one nesting level."""
    out = []
    for line in md.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        depth = 0
        while line.startswith(">"):
            depth += 1
            line = line[1:].lstrip()
        out.append("&emsp;&emsp;" * depth + line)
    return "\n\n".join(out)


HEAD_EVEN = "IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. ACCEPTED JUNE, 2022"
HEAD_ODD = "SELIM et al.: BLACK-BOX REACHABILITY-BASED SAFETY"


def furniture(page):
    """Running header and page number (both in the top margin, y = 26-33 pt)."""
    if page == 1 or page % 2 == 0:
        head, hb = HEAD_EVEN, ([48.0, 24.0, 348.0, 35.0] if page == 1 else [264.0, 24.0, 565.0, 35.0])
    else:
        head, hb = HEAD_ODD, [48.0, 24.0, 240.0, 35.0]
    nb = [46.0, 24.0, 55.0, 35.0] if (page % 2 == 0) else [557.0, 24.0, 566.0, 35.0]
    return [
        omit(f"p{page:04d}-runhead", hb, head,
             f"Running header of page {page} ('{head}'); page furniture repeated on every "
             f"{'even page and on page 1' if head == HEAD_EVEN else 'odd page from 3 on'}, checked on the page image."),
        omit(f"p{page:04d}-pageno", nb, str(page), f"Printed page number {page} in the top margin; page furniture."),
    ]


def save(page, items, notes):
    f = D / "pages" / f"page-{page:04d}.json"
    state = json.loads(f.read_text(encoding="utf-8"))
    ids = [i["id"] for i in items]
    assert len(ids) == len(set(ids)), "duplicate ids"
    for i in items:
        assert i["id"].startswith(f"p{page:04d}-"), i["id"]
        b = i["bbox"]
        assert len(b) == 4 and 0 <= b[0] < b[2] <= state["width"] and 0 <= b[1] < b[3] <= state["height"], (i["id"], b)
        if i["kind"] in ("text", "heading", "caption"):
            md = i["markdown"]
            assert md, i["id"]
            assert md.count("$$") % 2 == 0, ("$$", i["id"])
            assert md.replace("$$", "").replace("\\$", "").count("$") % 2 == 0, ("$", i["id"])
            assert md.count("{") == md.count("}"), ("braces", i["id"])
            assert "~~" not in md and "^*" not in md and "<sup>" not in md, ("markup", i["id"])
        if i["kind"] in ("figure", "table"):
            assert i["asset_name"] == i["asset_name"].lower()
    state["items"] = items
    state["reviewed"] = True
    state["review_notes"] = " ".join(notes.split())
    f.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"page {page}: {len(items)} items written")
