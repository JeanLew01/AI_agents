"""Helpers used by the per-page scripts (pNN.py) to write reviewed page JSON files for ganai2023iterative.

Bounding boxes are read by item id from the backup of the extractor output (orig_pages/), made
before the first edit, or given explicitly in PDF points.
"""
import json
import pathlib

R = pathlib.Path.home() / "AI_agents/paper2agent/Reachability"
D = R / "paper-review/ganai2023iterative-paper/documents/s001-ganai2023iterative"
S = R / "logs/work/ganai2023iterative"


def B(page, *ids):
    """Union of the bboxes of extractor items `ids` on `page`."""
    orig = json.loads((S / f"orig_pages/page-{page:04d}.json").read_text(encoding="utf-8"))
    boxes = {i["id"]: i["bbox"] for i in orig["items"]}
    bs = [boxes[k] for k in ids]
    return [min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs)]


def text(id, bbox, md, **kw):
    return dict(id=id, kind="text", bbox=bbox, markdown=md.strip(), **kw)


def display(id, bbox, tex):
    """A displayed formula as its own text item: one $$ ... $$ block."""
    return dict(id=id, kind="text", bbox=bbox, markdown="$$\n" + tex.strip() + "\n$$")


def heading(id, bbox, md):
    return dict(id=id, kind="heading", bbox=bbox, markdown=md.strip())


def caption(id, bbox, md):
    return dict(id=id, kind="caption", bbox=bbox, markdown=md.strip())


def omit(id, bbox, reason, md=""):
    return dict(id=id, kind="omit", bbox=bbox, markdown=md, reason=reason)


def figure(id, bbox, label, asset_name, **kw):
    return dict(id=id, kind="figure", bbox=bbox, markdown="", label=label, asset_name=asset_name, **kw)


def table(id, bbox, label, asset_name, rows):
    return dict(id=id, kind="table", bbox=bbox, markdown="", label=label, asset_name=asset_name, rows=rows)


def pageno(page):
    orig = json.loads((S / f"orig_pages/page-{page:04d}.json").read_text(encoding="utf-8"))
    it = orig["items"][-1]
    assert it["kind"] == "omit" and it["markdown"].strip() == str(page), it
    return omit(it["id"], it["bbox"], f"Printed page number '{page}' centred at the foot of the page; page furniture, checked on the page image.", str(page))


def save(page, items, notes):
    f = D / "pages" / f"page-{page:04d}.json"
    orig = json.loads((S / f"orig_pages/page-{page:04d}.json").read_text(encoding="utf-8"))
    ids = [i["id"] for i in items]
    assert len(ids) == len(set(ids)), "duplicate ids"
    for i in items:
        assert i["id"].startswith(f"p{page:04d}-"), i["id"]
        b = i["bbox"]
        assert len(b) == 4 and 0 <= b[0] < b[2] <= orig["width"] and 0 <= b[1] < b[3] <= orig["height"], (i["id"], b)
        if i["kind"] in ("text", "heading", "caption"):
            md = i["markdown"]
            assert md, i["id"]
            assert md.count("$$") % 2 == 0, ("$$", i["id"])
            assert md.replace("$$", "").count("$") % 2 == 0, ("odd $", i["id"])
            bare = md.replace("\\{", "").replace("\\}", "")
            assert bare.count("{") == bare.count("}"), ("braces", i["id"])
            assert "^*" not in md and "~~" not in md and "<sup>" not in md, ("forbidden pattern", i["id"])
            assert "\\left" not in md or md.count("\\left") == md.count("\\right"), ("left/right", i["id"])
    state = {k: orig[k] for k in ("page", "width", "height", "mode", "preview")}
    state["reviewed"] = True
    state["review_notes"] = " ".join(notes.split())
    state["warnings"] = orig.get("warnings", [])
    state["items"] = items
    f.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"page {page}: {len(items)} items written")


def O(page, id, *repl):
    """Extractor markdown of item `id` (verified against the page image as clean prose), with optional (old, new) replacements."""
    orig = json.loads((S / f"orig_pages/page-{page:04d}.json").read_text(encoding="utf-8"))
    md = {i["id"]: i["markdown"] for i in orig["items"]}[id]
    for a, b in repl:
        assert a in md, (id, a)
        md = md.replace(a, b)
    return md


def tidy(md):
    """Close the space the extractor leaves between a closing bold marker and following punctuation."""
    import re
    return re.sub(r"\*\* ([,.;:’)])", r"**\1", md)


def lead_italic(md):
    """Run-in italic paragraph title: the extractor writes '_Title._ rest'; return '*Title.* rest'."""
    import re
    m = re.match(r"_([^_]+)_ ", md)
    assert m, md[:40]
    return "*" + m.group(1) + "* " + md[m.end():]
