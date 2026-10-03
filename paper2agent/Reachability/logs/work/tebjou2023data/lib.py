#!/usr/bin/env python3
"""Helpers to (re)write reviewed page JSONs for tebjou2023data from the backed-up extractor output.

Idempotent: page(n, notes, items) reads SCRATCH/orig-pages/page-NNNN.json and rewrites D/pages/page-NNNN.json
immediately. Each item is (id, kind, bbox_spec, markdown, extras); bbox_spec is a list of four numbers
(PDF points, top-left origin) or a tuple of original item ids whose bboxes are unioned.
"""
import json
from pathlib import Path

R = Path.home() / "AI_agents/paper2agent/Reachability"
W = R / "paper-review/tebjou2023data-paper"
D = W / "documents/s001-tebjou2023data"
S = R / "logs/work/tebjou2023data"
SEEN = {}


def page(n, notes, items):
    orig = json.loads((S / f"orig-pages/page-{n:04d}.json").read_text(encoding="utf-8"))
    boxes = {i["id"]: i["bbox"] for i in orig["items"]}
    out_items = []
    for iid, kind, spec, md, extra in items:
        assert iid not in SEEN, ("duplicate id", iid)
        SEEN[iid] = n
        assert iid.startswith(f"p{n:04d}-"), iid
        if isinstance(spec, tuple):
            bs = [boxes[k] for k in spec]
            bbox = [min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs)]
        else:
            bbox = [float(v) for v in spec]
        assert bbox[0] < bbox[2] and bbox[1] < bbox[3] and bbox[0] >= 0 and bbox[1] >= 0 \
            and bbox[2] <= orig["width"] and bbox[3] <= orig["height"], (iid, bbox)
        if kind not in ("figure", "omit", "table"):
            assert md.strip(), ("empty markdown", iid)
            assert md.count("$") % 2 == 0, ("odd number of $", iid)
            assert md.count("{") == md.count("}"), ("brace imbalance", iid)
            assert md.count("(") == md.count(")") or extra.get("paren_ok"), ("paren imbalance", iid)
            for bad in ("<sup>", "�", "~~", "\\Vec", "\\set{", "\\ref", "\\cite", "\\sfrac", "\\eqref", "\\label"):
                assert bad not in md, (bad, iid)
        if kind == "omit":
            assert extra.get("reason"), iid
        if kind in ("figure", "table"):
            assert extra.get("asset_name") and extra.get("label"), iid
        item = {"id": iid, "kind": kind, "bbox": bbox, "markdown": md}
        item.update({k: v for k, v in extra.items() if k != "paren_ok"})
        out_items.append(item)
    state = {k: orig[k] for k in ("page", "width", "height", "mode", "preview")}
    state["reviewed"] = True
    state["review_notes"] = " ".join(notes.split())
    state["warnings"] = orig.get("warnings", [])
    state["items"] = out_items
    (D / f"pages/page-{n:04d}.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"page {n}: {len(out_items)} items written")


HDR_ODD = "Running header 'Data-driven Reachability using Christoffel Functions' (short title, small caps); page furniture repeated on odd pages."
HDR_EVEN = "Running header 'Tebjou Frehse Chamroukhi' (author surnames, small caps); page furniture repeated on even pages."


def pageno(n):
    return f"Printed page number '{n}' in the footer (the PDF numbers its pages 1-20, equal to the PDF page index; the proceedings pagination 194-213 is not printed)."
