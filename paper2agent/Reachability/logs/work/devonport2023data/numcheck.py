#!/usr/bin/env python3
"""Explain number 'extra' diagnostics of pages with algorithm transcriptions / table notes:
tokens of the transcription items (same tokenizer as the verifier) are subtracted from 'extra';
Unicode-minus pairs are cancelled. What remains is printed."""
import json, re, html
from collections import Counter
from pathlib import Path
D = Path.home() / "AI_agents/paper2agent/Reachability/paper-review/devonport2023data-paper/documents/s001-devonport2023data"
def plain_markdown(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    text = re.sub(r"!\[[^\]]*\]\([^\n]+?\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^\n]+?\)", r"\1", text)
    text = re.sub(r"</?(?:sup|sub|b|i|strong|em)>|<br\s*/?>", " ", text)
    text = re.sub(r"^\s*(?:`{3,}|~{3,})[^\n]*$", "", text, flags=re.M)
    text = re.sub(r"\\([\\`*{}\[\]()#+.!_|<>-])", r"\1", text)
    return html.unescape(text)
def number_tokens(text):
    text = plain_markdown(text).replace("*", "").replace("_", "")
    return Counter(re.findall(r"[+−-]?(?:\d{1,3}(?:,\d{3})+(?!\d)|\d+)(?:\.\d+)*(?:[eE][+−-]?\d+)?%?", text))
v = json.loads((D / "verification.json").read_text())
for p in v["pages"]:
    n = p["page"]
    st = json.loads((D / f"pages/page-{n:04d}.json").read_text())
    hidden = Counter()
    for it in st["items"]:
        if it["id"].endswith("-text") and "alg" in it["id"]:
            hidden += number_tokens(it["markdown"])
    for key in ("number_differences", "independent_parser_number_differences"):
        d = p[key]
        miss, extra = Counter(d["missing"]), Counter(d["extra"])
        extra = extra - hidden if hidden else extra
        # cancel unicode minus vs ascii minus
        for k in list(miss):
            if k.startswith("−"):
                a = "-" + k[1:]
                c = min(miss[k], extra.get(a, 0))
                miss[k] -= c; extra[a] -= c
        miss = +miss; extra = +extra
        if miss or extra:
            print(f"p{n} {key[:11]}: hidden-alg-tokens={sum(hidden.values())} residual missing={dict(miss)} extra={dict(extra)}")
