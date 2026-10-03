"""Bibliography entries from the authors' .bbl, in printed order, as Markdown strings."""
import re, pathlib, json
bbl = (pathlib.Path.home() / "AI_agents/paper2agent/Reachability/tex-source/hashemi2025pca/neus2025-arxiv.bbl").read_text()
body = bbl.split("\\bibitem", 1)[1]
entries = []
for chunk in ("\\bibitem" + body).split("\\bibitem")[1:]:
    chunk = chunk.split("\\end{thebibliography}")[0]
    m = re.match(r"\[.*?\]\{([^}]*)\}\s*", chunk, flags=re.S)
    # the optional argument may contain nested braces/brackets: find the key as the first {...} after the closing ']' at depth 0
    depth, i = 0, 0
    assert chunk[0] == "["
    while True:
        c = chunk[i]
        if c == "{": depth += 1
        elif c == "}": depth -= 1
        elif c == "]" and depth == 0: break
        i += 1
    rest = chunk[i + 1:]
    key, rest = re.match(r"\{([^}]*)\}(.*)", rest, flags=re.S).groups()
    t = rest.replace("\\newblock", " ")
    t = re.sub(r"\\penalty0\s*", "", t)
    t = re.sub(r"\{\\natexlab\{(\w)\}\}", r"\1", t)
    t = t.replace("{\\'a}", "á").replace("\\&", "&").replace("~", " ")
    t = re.sub(r"\\emph\{([^{}]*)\}", r"*\1*", t)
    t = t.replace("--", "–")
    t = " ".join(t.split())
    assert "\\" not in t and "{" not in t, t
    entries.append((key, t))
if __name__ == "__main__":
    import unicodedata
    def canon(s): return "".join(c for c in unicodedata.normalize("NFKD", s) if c.isalnum()).casefold()
    ex = []
    for p in (12, 13, 14):
        st = json.load(open(f"orig-pages/page-{p:04d}.json"))
        ex += [i for i in st["items"] if i["markdown"].startswith("- ")]
    print(len(entries), len(ex))
    for (k, t), i in zip(entries, ex):
        ok = canon(t) == canon(i["markdown"][2:])
        print("OK " if ok else "DIFF", i["id"], k)
        if not ok: print("   bbl:", t); print("   pdf:", i["markdown"])
    for k, t in entries: print(t)
