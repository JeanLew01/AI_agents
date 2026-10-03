"""Helper for writing reviewed page JSON files (liebenwein2018sampling)."""
import json, os
D = os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/liebenwein2018sampling-paper/documents/s001-liebenwein2018sampling")
L = (48.0, 301.0)   # left column x-range
R = (311.0, 564.0)  # right column x-range

def _bb(col, y0, y1):
    if isinstance(col, (list, tuple)) and len(col) == 2:
        return [float(col[0]), float(y0), float(col[1]), float(y1)]
    raise ValueError(col)

def H(md, col, y0, y1):
    return {"kind": "heading", "bbox": _bb(col, y0, y1), "markdown": md}

def T(md, col, y0, y1, join=None):
    it = {"kind": "text", "bbox": _bb(col, y0, y1), "markdown": md}
    if join:
        it["join_previous"] = join
    return it

def C(md, col, y0, y1):
    return {"kind": "caption", "bbox": _bb(col, y0, y1), "markdown": md}

def FIG(label, asset, bbox, kind="figure"):
    return {"kind": kind, "bbox": [float(v) for v in bbox], "markdown": "", "label": label, "asset_name": asset}

def OMIT(bbox, reason):
    return {"kind": "omit", "bbox": [float(v) for v in bbox], "markdown": "", "reason": reason}

def write(page, items, notes):
    path = f"{D}/pages/page-{page:04d}.json"
    s = json.load(open(path))
    out = []
    for k, it in enumerate(items):
        it = dict(it)
        it = {"id": f"p{page:04d}-r{k:03d}", **it}
        out.append(it)
    s["items"] = out
    s["reviewed"] = True
    s["review_notes"] = notes
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(s, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    os.replace(tmp, path)
    # sanity: balanced $ per item
    for it in out:
        md = it.get("markdown", "")
        if md.replace("\\$", "").count("$") % 2:
            print("WARNING unbalanced $ in", it["id"])
    print("wrote", path, len(out), "items")
