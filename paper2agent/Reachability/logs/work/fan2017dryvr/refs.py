"""Bibliography entries [1]..[56] generated from the authors' main2.bbl (de-TeXed); used by the page scripts p18-p23."""
import re, pathlib
BBL = pathlib.Path.home() / "AI_agents/paper2agent/Reachability/tex-source/fan2017dryvr/main2.bbl"
ACC = [(r"{\v{c}}", "č"), (r"{\'c}", "ć"), (r"{\=a}", "ā"), (r"{\v{C}}", "Č"), (r"{\'A}", "Á"), (r"{\'a}", "á"),
       (r'{\"e}', "ë"), (r"{\o}", "ø"), (r"{\'e}", "é"), (r"\v{c}", "č"), (r"\'{c}", "ć"), (r"\'A", "Á"), (r"\'a", "á")]

def entries():
    s = BBL.read_text()
    parts = re.split(r"\\bibitem\{[^}]*\}", s)[1:]
    out = []
    for n, p in enumerate(parts, 1):
        p = p.replace("\\end{thebibliography}", "")
        for a, b in ACC:
            p = p.replace(a, b)
        p = re.sub(r"\s+", " ", p.replace("\\newblock", " ")).strip()
        p = p.replace("~", " ").replace("--", "–").replace("\\&", "&")
        p = re.sub(r"\{\\em ([^{}]*)\}", r"*\1*", p)
        p = p.replace("{", "").replace("}", "")
        p = p.replace("'", "’")
        assert "\\" not in p.replace("$\\delta$", "").replace("$\\omega$", ""), p
        out.append(f"[{n}] {p}")
    assert len(out) == 56
    return out

if __name__ == "__main__":
    for e in entries():
        print(e); print()


def ref_items(page, first, last, bbox_override=None):
    """One text item per bibliography entry, with the bbox of the extractor item that starts with the same [n]."""
    import json
    from pagelib import text
    S = pathlib.Path(__file__).parent / "orig_pages" / f"page-{page:04d}.json"
    boxes = {}
    for i in json.loads(S.read_text())["items"]:
        m = re.match(r"\s*-?\s*\[(\d+)\]", i.get("markdown", ""))
        if m:
            boxes[int(m.group(1))] = i["bbox"]
    boxes.update(bbox_override or {})
    E = entries()
    return [text(f"p{page:04d}-ref{n:02d}", boxes[n], E[n - 1]) for n in range(first, last + 1)]
