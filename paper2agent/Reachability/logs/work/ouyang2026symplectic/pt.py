"""Helper for writing reviewed page JSON files (ouyang2026symplectic)."""
import json, os, re
D = os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/ouyang2026symplectic-paper/documents/s001-ouyang2026symplectic")
L = (54.0, 299.0)   # left column x-range
R = (313.0, 559.0)  # right column x-range
PW, PH = 612.0, 792.0

def _bb(col, y0, y1):
    return [float(col[0]), float(y0), float(col[1]), float(y1)]

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

def _check(it):
    md = it.get("markdown", "")
    pid = it["id"]
    if md.replace("\\$", "").count("$") % 2:
        print("WARNING unbalanced $ in", pid)
    if md.count("{") != md.count("}"):
        print("WARNING unbalanced braces in", pid, md.count("{"), md.count("}"))
    if md.count("\\left") != md.count("\\right"):
        print("WARNING left/right mismatch in", pid)
    if "~~" in md or "<sup>" in md or "�" in md:
        print("WARNING damage marker in", pid)
    if re.search(r"\^\*", md):
        print("WARNING ^* in", pid)
    b = it["bbox"]
    if not (0 <= b[0] < b[2] <= PW and 0 <= b[1] < b[3] <= PH):
        print("WARNING bbox", pid, b)

def write(page, items, notes):
    path = f"{D}/pages/page-{page:04d}.json"
    s = json.load(open(path))
    out = []
    for k, it in enumerate(items):
        it = {"id": f"p{page:04d}-r{k:03d}", **dict(it)}
        _check(it)
        out.append(it)
    s["items"] = out
    s["reviewed"] = True
    s["review_notes"] = " ".join(notes.split())
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(s, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    os.replace(tmp, path)
    print("wrote", path, len(out), "items")
