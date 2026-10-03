#!/usr/bin/env python3
"""Rebuild the reviewed page JSONs for sartipizadeh2019voronoi from the backed-up extractor output.

Idempotent: reads SCRATCH/orig-pages/page-NNNN.json and rewrites D/pages/page-NNNN.json for every
page defined in the part files (pages_01_05.py, pages_06_10.py, pages_11_15.py) that exist.
Each page is a list of (id, kind, bbox_spec, markdown, extras). bbox_spec is either a list of four
numbers or a tuple of original item ids whose bboxes are unioned.
usage: make_pages.py [page numbers ...]   (no argument = all defined pages)
"""
import json
import re
import sys
from pathlib import Path

R = Path.home() / "AI_agents/paper2agent/Reachability"
D = R / "paper-review/sartipizadeh2019voronoi-paper/documents/s001-sartipizadeh2019voronoi"
S = R / "logs/work/sartipizadeh2019voronoi"

PAGES = {}
NOTES = {}


def page(n, notes, items):
    PAGES[n] = items
    NOTES[n] = " ".join(notes.split())


def dd(body, tag=None):
    """A display-math markdown block; tag is the printed equation number."""
    body = body.strip()
    if tag:
        body += r" \tag{" + tag + "}"
    return "$$\n" + body + "\n$$"


for part in ("pages_01_05.py", "pages_06_10.py", "pages_11_15.py"):
    f = S / part
    if f.exists():
        exec(compile(f.read_text(encoding="utf-8"), str(f), "exec"))


def main():
    only = {int(a) for a in sys.argv[1:]}
    seen = set()
    for n, items in sorted(PAGES.items()):
        orig = json.loads((S / f"orig-pages/page-{n:04d}.json").read_text(encoding="utf-8"))
        boxes = {i["id"]: i["bbox"] for i in orig["items"]}
        out_items = []
        assets = set()
        for iid, kind, spec, md, extra in items:
            assert iid not in seen, iid
            seen.add(iid)
            assert iid.startswith(f"p{n:04d}-"), iid
            if isinstance(spec, tuple):
                bs = [boxes[k] for k in spec]
                bbox = [min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs)]
            else:
                bbox = spec
            assert bbox[0] < bbox[2] and bbox[1] < bbox[3] and bbox[0] >= 0 and bbox[1] >= 0 \
                and bbox[2] <= orig["width"] and bbox[3] <= orig["height"], (iid, bbox)
            assert kind in ("heading", "text", "caption", "figure", "table", "omit"), (iid, kind)
            if kind in ("heading", "text", "caption"):
                assert md.strip(), ("empty markdown", iid)
                assert md.count("$") % 2 == 0, ("odd number of $", iid)
                assert md.count("{") == md.count("}"), ("brace imbalance", iid)
                assert md.count("(") == md.count(")") or extra.get("paren_ok"), ("paren imbalance", iid)
                assert len(re.findall(r"\\left(?![A-Za-z])", md)) == len(re.findall(r"\\right(?![A-Za-z])", md)), ("left/right imbalance", iid)
                for bad in ("~~", "<sup>", "�", "\\R", "\\N_", "\\mcS", "\\mcT", "\\mcR", "\\mcP", "\\mcV", "\\mcC",
                            "\\Prob", "\\Exp", "\\Costpi", "\\U^", "\\W_", "\\X^", "\\ref", "\\cite", "\\eqref", "\\label", "^{*}", "^*"):
                    assert bad not in md, (bad, iid)
            if kind == "omit":
                assert extra.get("reason"), iid
            if kind in ("figure", "table"):
                assert extra.get("asset_name") and extra["asset_name"] not in assets, iid
                assets.add(extra["asset_name"])
            item = {"id": iid, "kind": kind, "bbox": bbox, "markdown": md}
            item.update({k: v for k, v in extra.items() if k != "paren_ok"})
            out_items.append(item)
        if only and n not in only:
            continue
        state = {k: orig[k] for k in ("page", "width", "height", "mode", "preview")}
        state["reviewed"] = True
        state["review_notes"] = NOTES[n]
        state["warnings"] = orig.get("warnings", [])
        state["items"] = out_items
        (D / f"pages/page-{n:04d}.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"page {n}: {len(out_items)} items written")


if __name__ == "__main__":
    main()
