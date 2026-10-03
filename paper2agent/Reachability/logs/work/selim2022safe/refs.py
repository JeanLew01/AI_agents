"""Bibliography entries [1]-[55] as Markdown, generated from the authors' main.bbl (IEEEtran.bst output) and
compared (alphanumeric skeleton) with the extractor's text of PDF pages 7-8. The PDF is the reference."""
import json, re, pathlib, unicodedata
R = pathlib.Path.home() / "AI_agents/paper2agent/Reachability"
S = R / "logs/work/selim2022safe"
bbl = (R / "tex-source/selim2022safe/main.bbl").read_text(encoding="utf-8")


def conv(t):
    t = t.replace("\\BIBentryALTinterwordspacing", "").replace("\\BIBentrySTDinterwordspacing", "")
    t = " ".join(t.split())
    t = t.replace("\\hskip 1em plus 0.5em minus 0.4em\\relax", "")
    t = t.replace("{\\i}", "ı").replace("{\\'a}", "á").replace('{\\"a}', "ä").replace('{\\"u}', "ü").replace('{\\"o}', "ö")
    t = re.sub(r"\\url\{([^}]*)\}", r"\1", t)
    t = re.sub(r"\\emph\{([^{}]*)\}", r"*\1*", t)
    t = t.replace("``", "“").replace("''", "”").replace("--", "–").replace("~", " ").replace("\\&", "&")
    t = re.sub(r"\s+", " ", t).strip()
    assert "\\" not in t and "{" not in t, t
    return t


def entries():
    parts = re.split(r"\\bibitem\{[^}]*\}", bbl)[1:]
    parts[-1] = parts[-1].split("\\end{thebibliography}")[0]
    out = {}
    for n, p in enumerate(parts, 1):
        out[n] = f"[{n}] " + conv(p)
    return out


def canon(s):
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if c.isalnum() and not unicodedata.combining(c)).casefold()


if __name__ == "__main__":
    E = entries()
    print(len(E), "entries")
    src = {}
    for pn in (7, 8):
        st = json.loads((S / f"orig-pages/page-{pn:04d}.json").read_text(encoding="utf-8"))
        cur = None
        for it in st["items"]:
            m = re.match(r"- \[(\d+)\] ", it["markdown"])
            if m:
                cur = int(m.group(1)); src[cur] = it["markdown"][2:]
            elif cur == 3 and it["markdown"].startswith("- ment learning"):
                src[3] += it["markdown"][2:]
    bad = 0
    for n in sorted(E):
        a, b = canon(E[n]), canon(src[n].replace("´", "").replace("¨", ""))
        if a != b:
            bad += 1
            print("DIFF", n, "\n  bbl:", E[n], "\n  pdf:", src[n])
    print("entries differing from the extractor text (alphanumeric skeleton):", bad)
    for n in (1, 3, 6, 8, 12, 33, 40, 42):
        print(E[n])
