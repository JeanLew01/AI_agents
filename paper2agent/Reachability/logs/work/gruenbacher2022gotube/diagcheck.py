#!/usr/bin/env python3
"""(1) every tool-'missing' line: its words (>=3 letters) must occur in order in the page markdown with LaTeX commands stripped;
(2) number differences: tokens of algorithm-transcription and conversion-note items are subtracted from 'extra', Unicode-minus pairs cancelled; residual printed."""
import json, re, html, unicodedata, os
from collections import Counter
D = os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/gruenbacher2022gotube-paper/documents/s001-gruenbacher2022gotube")
KEEP = {"max", "min", "sup", "Pr", "ln", "operatorname"}
def strip(t):
    t = re.sub(r"\\tag\{[^}]*\}", " ", t)
    t = re.sub(r"\\(?:textrm|text|operatorname)\{([^}]*)\}", r" \1 ", t)
    t = re.sub(r"\\([A-Za-z]+)", lambda m: m.group(1) if m.group(1) in KEEP else " ", t)
    return t.replace("&emsp;", " ")
def letters(t):
    t = unicodedata.normalize("NFKD", t)
    return "".join(c for c in t if c.isascii() and c.isalpha()).lower()
def page_md(n):
    try:
        pg = json.load(open(f"{D}/pages/page-{n:04d}.json"))
    except FileNotFoundError:
        return ""
    return "\n".join(i.get("markdown", "") + " " + " ".join(" ".join(r) for r in (i.get("rows") or [])) for i in pg["items"] if i["kind"] != "omit")
def plain_markdown(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"!\[[^\]]*\]\([^\n]+?\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^\n]+?\)", r"\1", text)
    text = re.sub(r"</?(?:sup|sub|b|i|strong|em)>|<br\s*/?>", " ", text)
    text = re.sub(r"\\([\\`*{}\[\]()#+.!_|<>-])", r"\1", text)
    return html.unescape(text)
def number_tokens(text):
    text = plain_markdown(text).replace("*", "").replace("_", "")
    return Counter(re.findall(r"[+−-]?(?:\d{1,3}(?:,\d{3})+(?!\d)|\d+)(?:\.\d+)*(?:[eE][+−-]?\d+)?%?", text))
v = json.load(open(f"{D}/verification.json"))
tot = bad = 0
for p in v["pages"]:
    n = p["page"]
    s = letters(strip(page_md(n - 1)[-1500:])) + letters(strip(page_md(n))) + letters(strip(page_md(n + 1)[:600]))
    for l in p["missing_lines"]:
        tot += 1
        txt = l["text"] if isinstance(l, dict) else l
        ws = [letters(w) for w in re.findall(r"[^\W\d_]{3,}", unicodedata.normalize("NFKD", txt))]
        ws = [w for w in ws if len(w) >= 3 and w not in ("maxx", "maxm")]
        ok = not ws
        if ws:
            for st in [m.start() for m in re.finditer(re.escape(ws[0]), s)]:
                pos = st; good = True
                for w in ws:
                    j = s.find(w, pos, pos + 500)
                    if j < 0: good = False; break
                    pos = j + len(w)
                if good: ok = True; break
        if not ok:
            bad += 1; print(f"page {n}: UNMATCHED {txt!r} words={ws}")
    pg = json.load(open(f"{D}/pages/page-{n:04d}.json"))
    hidden = Counter()
    for it in pg["items"]:
        md = it.get("markdown", "")
        if md.startswith("**Algorithm 1: GoTube**") or md.startswith("*Conversion note"):
            hidden += number_tokens(md)
    for key in ("number_differences", "independent_parser_number_differences"):
        d = p[key]
        miss, extra = Counter(d["missing"]), Counter(d["extra"])
        extra0 = Counter(extra)
        extra = extra - hidden
        for k in list(miss):
            if k.startswith("−"):
                a = "-" + k[1:]
                c = min(miss[k], extra.get(a, 0))
                miss[k] -= c; extra[a] -= c
        miss = +miss; extra = +extra
        if d["missing"] or d["extra"]:
            print(f"p{n} {key[:11]}: hidden tokens={sum(hidden.values())} unused hidden={dict(hidden - extra0)} residual missing={dict(miss)} extra={dict(extra)}")
print("missing lines", tot, "unmatched", bad)
