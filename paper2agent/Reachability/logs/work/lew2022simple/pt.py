"""Helper to write reviewed page JSON files for lew2022simple (review inputs only)."""
import json, os

D = os.path.expanduser('~/AI_agents/paper2agent/Reachability/paper-review/lew2022simple-paper/documents/s001-lew2022simple')

HEADER_REASON = "Running header 'SAMPLING-BASED REACHABILITY ANALYSIS' (page furniture repeated on every page after the first); checked on the page image."


def T(md, bbox, **kw):
    d = {"kind": "text", "bbox": [float(x) for x in bbox], "markdown": md.strip()}
    d.update(kw)
    return d


def H(md, bbox):
    return {"kind": "heading", "bbox": [float(x) for x in bbox], "markdown": md.strip()}


def C(md, bbox, **kw):
    d = {"kind": "caption", "bbox": [float(x) for x in bbox], "markdown": md.strip()}
    d.update(kw)
    return d


def F(label, asset, bbox, cat=None):
    d = {"kind": "figure", "bbox": [float(x) for x in bbox], "markdown": "", "label": label, "asset_name": asset}
    if cat:
        d["asset_category"] = cat
    return d


def O(bbox, reason, md=""):
    return {"kind": "omit", "bbox": [float(x) for x in bbox], "markdown": md, "reason": reason}


def HDR():
    return O([200, 36, 412, 54], HEADER_REASON, "SAMPLING-BASED REACHABILITY ANALYSIS")


def PNUM(n):
    return O([295, 722, 317, 737], f"Printed page number {n} at the bottom centre (page furniture); checked on the page image.", str(n))


def page(n, items, notes):
    path = f'{D}/pages/page-{n:04d}.json'
    p = json.load(open(path))
    out = []
    for k, it in enumerate(items):
        it = dict(it)
        it["id"] = f"p{n:04d}-r{k:03d}"
        # stable key order
        out.append({"id": it.pop("id"), **it})
    p["items"] = out
    p["reviewed"] = True
    p["review_notes"] = notes.strip()
    for it in out:
        b = it["bbox"]
        assert 0 <= b[0] < b[2] <= p["width"] and 0 <= b[1] < b[3] <= p["height"], (it["id"], b)
        if it["kind"] in ("text", "heading", "caption"):
            md = it["markdown"]
            assert md, it["id"]
            # crude balance check for inline math
            stripped = md.replace("\\$", "")
            assert stripped.count("$") % 2 == 0, ("unbalanced $", it["id"], md[:80])
            assert stripped.count("{") == stripped.count("}"), ("unbalanced braces", it["id"], md[:80])
            if not md.startswith("$$"):
                assert "$$" not in md, ("stray $$ in prose item", it["id"], md[:80])
            assert "\t" not in md and "\x08" not in md and "\x0c" not in md, ("control char", it["id"])
    tmp = path + '.tmp'
    json.dump(p, open(tmp, 'w'), indent=1, ensure_ascii=False)
    os.replace(tmp, path)
    print(f"page {n}: {len(out)} items written")
