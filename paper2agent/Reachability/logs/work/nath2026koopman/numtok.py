#!/usr/bin/env python3
"""numtok.py PAGE ITEM_ID... : number-token multiset (verifier tokenizer) of the given items of a reviewed page."""
import json, sys, re, html, os
from collections import Counter
D = os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/nath2026koopman-paper/documents/s001-nath2026koopman")
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
p = json.load(open(f"{D}/pages/page-{int(sys.argv[1]):04d}.json"))
c = Counter()
for i in p["items"]:
    if i["id"] in sys.argv[2:]:
        c += number_tokens(i["markdown"])
print(dict(c))
