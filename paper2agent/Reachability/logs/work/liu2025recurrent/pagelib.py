#!/usr/bin/env python3
"""Helper for the per-page generator scripts pgN.py of liu2025recurrent.

Each pgN.py calls write_page(n, notes, items); items are tuples
(id, kind, bbox_spec, markdown, extras). bbox_spec is a list of four numbers (PDF points) or a tuple
of original extractor item ids (read from SCRATCH/orig-pages, the backup made before the first edit)
whose bboxes are unioned. The page JSON is written immediately (idempotent)."""
import json
import re
from pathlib import Path

R = Path.home() / "AI_agents/paper2agent/Reachability"
D = R / "paper-review/liu2025recurrent-paper/documents/s001-liu2025recurrent"
S = R / "logs/work/liu2025recurrent"


def write_page(n, notes, items):
    orig = json.loads((S / f"orig-pages/page-{n:04d}.json").read_text(encoding="utf-8"))
    boxes = {i["id"]: i["bbox"] for i in orig["items"]}
    seen, out = set(), []
    for iid, kind, spec, md, extra in items:
        assert iid not in seen and iid.startswith(f"p{n:04d}-"), iid
        seen.add(iid)
        if isinstance(spec, tuple):
            bs = [boxes[k] for k in spec]
            bbox = [min(b[0] for b in bs), min(b[1] for b in bs), max(b[2] for b in bs), max(b[3] for b in bs)]
        else:
            bbox = [float(v) for v in spec]
        assert 0 <= bbox[0] < bbox[2] <= orig["width"] and 0 <= bbox[1] < bbox[3] <= orig["height"], (iid, bbox)
        if kind in ("text", "caption", "heading"):
            assert md.strip(), ("empty", iid)
            assert md.count("$") % 2 == 0, ("odd number of $", iid)
            assert md.count("{") == md.count("}"), ("brace imbalance", iid)
            assert "](" not in md, ("markdown-link-like sequence", iid)
            assert "^*" not in md and "~~" not in md and "<sup>" not in md, ("^* / ~~ / <sup>", iid)
            assert not re.search(r"<[A-Za-z/]", md), ("html-like <", iid)
            for m in re.findall(r"\$\$(.+?)\$\$", md, flags=re.S):
                assert "\\begin{align" not in m.replace("\\begin{aligned}", ""), ("align in $$", iid)
        item = {"id": iid, "kind": kind, "bbox": bbox, "markdown": md}
        item.update(extra)
        if kind == "omit":
            assert item.get("reason")
        if kind in ("figure", "table"):
            assert item.get("asset_name") and item.get("label")
        out.append(item)
    state = {k: orig[k] for k in ("page", "width", "height", "mode", "preview")}
    state["reviewed"] = True
    state["review_notes"] = " ".join(notes.split())
    state["warnings"] = orig.get("warnings", [])
    state["items"] = out
    (D / f"pages/page-{n:04d}.json").write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"page {n}: {len(out)} items written, reviewed=true")
