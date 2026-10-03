#!/usr/bin/env python3
"""Helpers to regenerate the reviewed page JSON files for dietrich2024nonconvex.

Every run reads the untouched extractor output from SCRATCH/orig-pages/ (backup made before the
first edit) and rewrites D/pages/page-NNNN.json.  Items are dicts made with T/H/C/O/F/TB below.
bbox: explicit list, or `box=` one original item id / tuple of original ids (union), or the
original bbox of the item's own id.
"""
import json
from pathlib import Path

R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/dietrich2024nonconvex-paper"
D = W / "documents/s001-dietrich2024nonconvex"
S = R / "logs/work/dietrich2024nonconvex"

RUNHEAD = ("Running header of the proceedings layout (author names on even pages, short title on odd pages); "
           "page furniture, not part of the text.")
PAGENO = "Printed page number in the footer; page furniture."


def T(i, md, **kw):
    return dict(id=i, kind="text", markdown=md, **kw)


def H(i, md, **kw):
    return dict(id=i, kind="heading", markdown=md, **kw)


def C(i, md, **kw):
    return dict(id=i, kind="caption", markdown=md, **kw)


def O(i, reason, **kw):
    return dict(id=i, kind="omit", markdown="", reason=reason, **kw)


def F(i, label, asset, bbox, **kw):
    return dict(id=i, kind="figure", markdown="", label=label, asset_name=asset, bbox=bbox, **kw)


def TB(i, label, asset, rows, **kw):
    return dict(id=i, kind="table", markdown="", label=label, asset_name=asset, rows=rows, **kw)


def write_pages(pages, notes):
    seen = set()
    for pn, items in sorted(pages.items()):
        orig = json.loads((S / f"orig-pages/page-{pn:04d}.json").read_text(encoding="utf-8"))
        boxes = {i["id"]: i["bbox"] for i in orig["items"]}
        out = []
        used = set()
        for spec in items:
            spec = dict(spec)
            iid = spec["id"]
            assert iid not in seen, ("duplicate id", iid)
            seen.add(iid)
            box = spec.pop("box", None)
            if "bbox" in spec:
                bbox = spec.pop("bbox")
            else:
                ids = (box,) if isinstance(box, str) else tuple(box) if box else (iid,)
                used.update(ids)
                bs = [boxes[k] for k in ids]
                bbox = [min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs)]
            used.add(iid)
            assert 0 <= bbox[0] < bbox[2] <= orig["width"] and 0 <= bbox[1] < bbox[3] <= orig["height"], (iid, bbox)
            md = spec.get("markdown", "")
            if spec["kind"] in ("text", "caption", "heading"):
                assert md.strip(), ("empty text", iid)
                assert md.count("$") % 2 == 0, ("odd number of $", iid)
                assert md.count("{") == md.count("}"), ("brace imbalance", iid)
                assert "~~" not in md and "<sup>" not in md and "�" not in md, ("damage", iid)
            if spec["kind"] == "table":
                rows = spec["rows"]
                assert all(len(r) == len(rows[0]) and all(isinstance(c, str) for c in r) for r in rows), iid
            item = {"id": iid, "kind": spec.pop("kind"), "bbox": bbox, "markdown": md}
            spec.pop("id"); spec.pop("markdown", None)
            item.update(spec)
            out.append(item)
        state = {k: orig[k] for k in ("page", "width", "height", "mode", "preview")}
        state["reviewed"] = True
        state["review_notes"] = " ".join(notes[pn].split())
        state["warnings"] = orig.get("warnings", [])
        state["items"] = out
        (D / f"pages/page-{pn:04d}.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        unused = [k for k in boxes if k not in used]
        print(f"page {pn}: {len(out)} items written; extractor items not referenced: {unused}")
