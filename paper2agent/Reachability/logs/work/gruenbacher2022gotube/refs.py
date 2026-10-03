"""Build the reference entries from the authors' .bbl, locate each entry on PDF pages 8-10 through the evidence lines,
and compare the normalised text of every entry with the PDF text layer. Importable: ENTRIES, place()."""
import json, os, re, unicodedata
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/gruenbacher2022gotube-paper/documents/s001-gruenbacher2022gotube"
bbl = open(f"{R}/tex-source/gruenbacher2022gotube/GoTube.bbl", encoding="utf-8").read()
ACC = {"'": "\u0301", '"': "\u0308", "v": "\u030c"}
def detex(s):
    s = re.sub(r"\\newblock\s*", "", s)
    s = re.sub(r"\{\\natexlab\{(\w)\}\}", r"\1", s)
    # accents: {\'{A}}, {\'e}, \'{e}, {\"a}, {\v{c}}
    def acc(m):
        return unicodedata.normalize("NFC", m.group(2) + ACC[m.group(1)])
    s = re.sub(r"\{\\(['\"v])\{(\w)\}\}", acc, s)
    s = re.sub(r"\{\\(['\"])(\w)\}", acc, s)
    s = re.sub(r"\\(['\"v])\{(\w)\}", acc, s)
    s = s.replace("'", "\u2019")
    s = re.sub(r"\\textquotesingle\s*", "'", s)
    s = s.replace("Flow*", "Flow\\*")
    s = re.sub(r"\\emph\{\{([^{}]*)\}\}", r"*\1*", s)
    s = re.sub(r"\\emph\{([^{}]*)\}", r"*\1*", s)
    s = s.replace("~", " ").replace("--", "–")
    s = re.sub(r"[{}]", "", s)
    s = re.sub(r"\s+", " ", s).strip()
    assert "\\" not in s.replace("Flow\\*", ""), s
    return s
body = bbl[bbl.index("\\bibitem"):bbl.index("\\end{thebibliography}")]
ENTRIES = []
for chunk in body.split("\\bibitem")[1:]:
    m = re.match(r"\[\{.*?\}\]\{[^}]*\}\s*\n", chunk, flags=re.S)
    ENTRIES.append(detex(chunk[m.end():]))
def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^0-9a-z]", "", s.lower())
def segments(page):
    ev = json.load(open(f"{D}/evidence/page-{page:04d}.json"))
    out = []
    for c in (0, 1):
        ls = sorted([l for l in ev["lines"] if (l["bbox"][0] >= 306) == bool(c)], key=lambda l: (round(l["bbox"][3]), l["bbox"][0]))
        cur = None; prev_y = None
        for l in ls:
            b = l["bbox"]
            if page == 8 and l["text"].strip() == "References":
                continue
            if prev_y is None or b[3] - prev_y > 12.4:
                cur = {"col": c, "bbox": list(b), "text": l["text"]}; out.append(cur)
            else:
                cur["text"] += " " + l["text"]
                cur["bbox"] = [min(cur["bbox"][0], b[0]), min(cur["bbox"][1], b[1]), max(cur["bbox"][2], b[2]), max(cur["bbox"][3], b[3])]
            if b[3] - (prev_y if prev_y is not None else -99) > 2:
                prev_y = b[3]
    return out
def place(verbose=False):
    """returns {page: [(entry_index, bbox, complete_here)]}"""
    res = {8: [], 9: [], 10: []}
    i = 0; rest = norm(ENTRIES[0]); first = True
    for p in (8, 9, 10):
        for sg in segments(p):
            n = norm(re.sub(r"(\w)- (\w)", r"\1\2", sg["text"]))
            n2 = norm(sg["text"])
            if rest.startswith(n): used = n
            elif rest.startswith(n2): used = n2
            else:
                # tolerate real hyphens at line ends: compare letter multiset prefix
                print("MISMATCH page", p, "entry", i, "\n  pdf:", sg["text"][:200], "\n  bbl:", ENTRIES[i][:200]); used = n
            if first:
                res[p].append((i, sg["bbox"], None))
            else:
                print(f"note: entry {i} continues on page {p} col {sg['col']}: {sg['text'][:60]}")
                res[p].append((i, sg["bbox"], "cont"))
            rest = rest[len(used):]
            if rest == "":
                i += 1; first = True
                if i < len(ENTRIES): rest = norm(ENTRIES[i])
            else:
                first = False
    print("entries matched:", i, "of", len(ENTRIES))
    return res
if __name__ == "__main__":
    res = place()
    for p in res:
        print(p, len(res[p]), [(i, c) for i, b, c in res[p] if c])
    for k, e in enumerate(ENTRIES):
        print(k, e)
