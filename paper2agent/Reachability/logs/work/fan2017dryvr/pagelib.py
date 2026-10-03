"""Helpers used by the per-page scripts (pNN.py) to write reviewed page JSON files."""
import json
import pathlib

D = pathlib.Path.home() / "AI_agents/paper2agent/Reachability/paper-review/fan2017dryvr-paper/documents/s001-fan2017dryvr"


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
    return dict(id=id, kind="table", bbox=bbox, markdown="", label=label, asset_name=asset_name, rows=rows)


def algfmt(md):
    """Algorithm transcription: one paragraph per printed line; every 4 leading spaces = one nesting level, shown as '&emsp;&emsp;'."""
    out = []
    for line in md.strip("\n").splitlines():
        if not line.strip():
            continue
        n = len(line) - len(line.lstrip(" "))
        assert n % 4 == 0, line
        out.append("&emsp;&emsp;" * (n // 4) + line.strip())
    return "\n\n".join(out)


def pageno(page, bbox):
    return omit(f"p{page:04d}-pageno", bbox, str(page), f"Printed page number {page} centred at the foot of the page; page furniture, checked on the page render.")


def save(page, items, notes):
    f = D / "pages" / f"page-{page:04d}.json"
    state = json.loads(f.read_text())
    ids = [i["id"] for i in items]
    assert len(ids) == len(set(ids)), "duplicate ids"
    for i in items:
        if i["id"].endswith("-text") and "-alg" in i["id"]:
            i["markdown"] = algfmt(i["markdown"])
        assert i["id"].startswith(f"p{page:04d}-"), i["id"]
        b = i["bbox"]
        assert len(b) == 4 and 0 <= b[0] < b[2] <= state["width"] and 0 <= b[1] < b[3] <= state["height"], (i["id"], b)
        if i["kind"] in ("text", "heading", "caption"):
            md = i["markdown"]
            assert md, i["id"]
            # crude balance checks for math delimiters and braces
            assert md.count("$$") % 2 == 0, ("$$", i["id"])
            assert md.replace("$$", "").replace("\\$", "").count("$") % 2 == 0, ("$", i["id"])
    state["items"] = items
    state["reviewed"] = True
    state["review_notes"] = notes.strip()
    f.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")
    print(f"page {page}: {len(items)} items written")
