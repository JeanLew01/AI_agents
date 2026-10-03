"""Helpers used by the per-page scripts (pNN.py) to write reviewed page JSON files for lin2024verification."""
import json
import pathlib

R = pathlib.Path.home() / "AI_agents/paper2agent/Reachability"
D = R / "paper-review/lin2024verification-paper/documents/s001-lin2024verification"
S = R / "logs/work/lin2024verification"

# Frequently used LaTeX fragments (authors' macros expanded, see notation.tex)
V = r"\tilde{V}"                       # \Tilde{\vfunc}
PI = r"\tilde{\pi}"                    # \Tilde{\policy}
J = r"J_{\tilde{\pi}}"                 # \costFunction
JT = r"\tilde{J}_{\tilde{\pi}}"        # \learnedCostFunction
DELTA = r"\delta_{\tilde{V},\tilde{\pi}}"   # \safetyMetric
PS = r"\underset{x \in \mathcal{S}}{\mathbb{P}}"
PJ = r"\underset{ \left( x_{1:N},x \right) \in \mathcal{S} }{\mathbb{P}}"
BINOM = r"\sum^k_{i=0} \binom{N}{i} \epsilon^i (1-\epsilon)^{N-i} \le \beta"
FN = " $^{1}$"                         # footnote mark, written with a space before it


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


def display(body, tag=None):
    return "$$\n" + body.strip() + (f" \\tag{{{tag}}}" if tag else "") + "\n$$"


def header(page):
    if page % 2 == 0:
        return omit(f"p{page:04d}-b000", [277.0, 41.0, 332.0, 49.0], "LIN BANSAL",
                    "Running header of an even page (author names 'LIN BANSAL' in small capitals); page furniture, checked on the page image.")
    return omit(f"p{page:04d}-b000", [204.0, 41.0, 406.0, 49.0], "VERIFICATION OF NEURAL REACHABLE TUBES",
                "Running header of an odd page (short title 'VERIFICATION OF NEURAL REACHABLE TUBES' in small capitals); page furniture, checked on the page image.")


def pageno(page, id, bbox):
    return omit(id, bbox, str(page), f"Page number {page} at the foot of the page; page furniture.")


def save(page, items, notes):
    f = D / "pages" / f"page-{page:04d}.json"
    orig = json.loads((S / "orig-pages" / f"page-{page:04d}.json").read_text(encoding="utf-8"))
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
            assert md.replace("$$", "").replace("\\$", "").count("$") % 2 == 0, ("$", i["id"])
            assert md.count("{") == md.count("}"), ("brace imbalance", i["id"])
            assert "^*" not in md and "~" not in md and "<sup>" not in md, ("forbidden token", i["id"])
        if i["kind"] == "omit":
            assert i["reason"].strip()
    state = {k: orig[k] for k in ("page", "width", "height", "mode", "preview")}
    state["reviewed"] = True
    state["review_notes"] = " ".join(notes.split())
    state["warnings"] = orig.get("warnings", [])
    state["items"] = items
    f.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"page {page}: {len(items)} items written")
