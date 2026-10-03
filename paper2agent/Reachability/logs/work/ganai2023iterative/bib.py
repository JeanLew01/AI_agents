#!/usr/bin/env python3
"""Reference list from the thebibliography environment of main.tex as Markdown strings (BIB[n]), and a comparison with
the extractor's text of pages 11-13 (letters/digits only) when run as a script."""
import re, json, pathlib, unicodedata
S = pathlib.Path(__file__).parent
tex = (S / "main.resolved.tex").read_text(encoding="utf-8")
body = tex[tex.index(r"\begin{thebibliography}"):tex.index(r"\end{thebibliography}")]
ents = re.split(r"\\bibitem\{[^}]*\}", body)[1:]
def conv(e):
    e = " ".join(e.split())
    e = e.replace(r"\newblock ", "")
    e = e.replace(r"{\'i}", "í").replace(r"{\'a}", "á").replace(r"\'{e}", "é").replace(r"{\c{c}}", "ç")
    e = e.replace(r"\textquotesingle ", "'").replace(r"\&", "&")
    e = re.sub(r"\\url\{([^}]*)\}", r"`\1`", e)
    e = re.sub(r"\{\\em \{([^{}]*)\}\}", r"*\1*", e)
    e = re.sub(r"\{\\em ([^{}]*)\}", r"*\1*", e)
    e = e.replace("~", " ").replace("--", "–")
    e = re.sub(r"\{([^{}]*)\}", r"\1", e)
    assert "\\" not in e and "{" not in e and "}" not in e, e
    return e.strip()
BIB = {i + 1: f"[{i + 1}] " + conv(e) for i, e in enumerate(ents)}
def letters(t):
    t = unicodedata.normalize("NFKD", t)
    return "".join(c for c in t if c.isalnum()).lower()
if __name__ == "__main__":
    seen = {}
    for pg in (11, 12, 13):
        o = json.loads((S / f"orig_pages/page-{pg:04d}.json").read_text(encoding="utf-8"))
        for it in o["items"]:
            m = re.match(r"- \[(\d+)\] ", it["markdown"])
            if m:
                n = int(m.group(1)); seen[n] = (pg, it["id"])
                a = letters(it["markdown"][2:].replace("_", "")); b = letters(BIB[n].replace("*", "").replace("`", ""))
                if a != b:
                    k = next((j for j in range(min(len(a), len(b))) if a[j] != b[j]), min(len(a), len(b)))
                    print(f"DIFF [{n}] p{pg} {it['id']}: extractor ...{a[max(0,k-25):k+30]}... tex ...{b[max(0,k-25):k+30]}...")
    print("entries in TeX:", len(BIB), "matched extractor items:", len(seen), "missing:", [n for n in BIB if n not in seen])
    json.dump({n: list(v) for n, v in seen.items()}, open(S / "bibmap.json", "w"))
