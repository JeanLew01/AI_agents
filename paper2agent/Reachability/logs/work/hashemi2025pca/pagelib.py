"""Helpers used by the per-page scripts (pNN.py) to write reviewed page JSON files (hashemi2025pca)."""
import json
import pathlib
import re

R = pathlib.Path.home() / "AI_agents/paper2agent/Reachability"
D = R / "paper-review/hashemi2025pca-paper/documents/s001-hashemi2025pca"
ORIG = R / "logs/work/hashemi2025pca/orig-pages"


def orig(page):
    """Extractor items of a page (backup made before the first edit), by id."""
    st = json.loads((ORIG / f"page-{page:04d}.json").read_text())
    return {i["id"]: i for i in st["items"]}


def text(id, bbox, md, **kw):
    return dict(id=id, kind="text", bbox=bbox, markdown=md.strip(), **kw)


def heading(id, bbox, md):
    return dict(id=id, kind="heading", bbox=bbox, markdown=md.strip())


def caption(id, bbox, md, **kw):
    return dict(id=id, kind="caption", bbox=bbox, markdown=md.strip(), **kw)


def omit(id, bbox, md, reason):
    return dict(id=id, kind="omit", bbox=bbox, markdown=md, reason=reason)


def figure(id, bbox, label, asset_name, **kw):
    return dict(id=id, kind="figure", bbox=bbox, markdown="", label=label, asset_name=asset_name, **kw)


def table(id, bbox, label, asset_name, rows):
    n = {len(r) for r in rows}
    assert len(n) == 1, "ragged table"
    assert all(isinstance(c, str) for r in rows for c in r)
    return dict(id=id, kind="table", bbox=bbox, markdown="", label=label, asset_name=asset_name, rows=rows)


def page_number(page):
    return omit(f"p{page:04d}-pageno", [296.0, 742.0, 316.0, 756.0], str(page),
                f"Printed page number {page} centred at the foot of the page; page furniture, checked on the 170 dpi render.")


def _balanced(md):
    depth = 0
    for ch in md.replace("\\{", "").replace("\\}", ""):
        if ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth < 0:
                return False
    return depth == 0


def save(page, items, notes):
    f = D / "pages" / f"page-{page:04d}.json"
    state = json.loads(f.read_text())
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
            assert _balanced(md), ("braces", i["id"])
            assert "~~" not in md, ("~~", i["id"])
            assert not re.search(r"\^\*", md), ("^* (use ^{\\ast})", i["id"])
        if i["kind"] == "omit":
            assert i.get("reason"), i["id"]
    state["items"] = items
    state["reviewed"] = True
    state["review_notes"] = " ".join(notes.split())
    f.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")
    print(f"page {page}: {len(items)} items written")


# ---- expansion of the authors' private macros (sections/macros.tex) into standard LaTeX ----
_NOARG = {
    "statee": "s", "Statee": "S", "states": r"\mathcal{S}", "horizon": r"\mathrm{K}", "timeid": "k",
    "init": r"\mathcal{I}", "distinit": r"\mathcal{W}", "traj": r"\sigma",
    "trajsim": r"\sigma^{\mathsf{sim}}", "trajreal": r"\sigma^{\mathsf{real}}",
    "dist": r"\mathcal{D}_{S,\mathrm{K}}^{\mathsf{real}}", "distzero": r"\mathcal{D}_{S,\mathrm{K}}^{\mathsf{sim}}",
    "distR": r"\mathcal{J}_{S,\mathrm{K}}^{\mathsf{real}}", "distzeroR": r"\mathcal{J}_{S,\mathrm{K}}^{\mathsf{sim}}",
    "overallf": r"\mathcal{F}", "ressim": r"\rho", "resreal": r"\rho",
    "PE": r"\mathsf{PE}", "PEreal": r"\mathsf{PE}", "PEsim": r"\mathsf{PE}", "tv": r"\mathsf{TV}",
    "traindataset": r"\mathcal{T}^{\mathsf{trn}}", "calibdataset": r"\mathcal{R}^{\mathsf{calib}}",
    "reals": r"\mathbb{R}", "relu": r"\mathrm{ReLU}", "gaussian": r"\mathcal{N}",
}
_ARG = {
    "errsim": "R^{%s}", "errreal": "R^{%s}", "PEsimseg": r"\mathsf{PE}^{%s}", "eigvecseg": r"\mathsf{V}^{%s}",
    "trajsimseg": r"\sigma^{\mathsf{sim} , %s}", "transpose": r"{%s}^{\top}",
    "navid": "%s", "navidd": "%s", "navidg": "%s",
}


def _arg(s, i):
    """s[i] == '{' -> (content, index after the closing brace)."""
    assert s[i] == "{", s[i:i + 20]
    depth, j = 0, i
    while True:
        if s[j] == "\\":
            j += 2
            continue
        if s[j] == "{":
            depth += 1
        elif s[j] == "}":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1


def X(s):
    """Expand the authors' macros; drop the negative thin spaces (\\!) used only for manual spacing."""
    for _ in range(6):
        out, i, changed = [], 0, False
        while i < len(s):
            m = re.match(r"\\([A-Za-z]+)", s[i:])
            if m:
                name = m.group(1)
                j = i + m.end()
                if name in _ARG:
                    a, j = _arg(s, j)
                    out.append(_ARG[name] % a)
                    i, changed = j, True
                    continue
                if name in _NOARG:
                    rep = _NOARG[name]
                    # keep a separating space only when the next char is a letter
                    out.append(rep)
                    if j < len(s) and s[j] == " " and j + 1 < len(s) and (s[j + 1].isalpha()) and rep[-1].isalpha():
                        out.append(" ")
                        j += 1
                    i, changed = j, True
                    continue
                out.append(m.group(0))
                i = j
                continue
            out.append(s[i])
            i += 1
        s = "".join(out)
        if not changed:
            break
    s = s.replace("\\!", "")
    s = s.replace("^*", "^{\\ast}")
    return s
