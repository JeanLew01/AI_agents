#!/usr/bin/env python3
"""Explain the tool's number diagnostics item by item, using the tool's own tokenizer.
For each page with a number difference, list every markdown item and every PDF line whose tokens
differ, so that each missing/extra token can be attributed to a specific place."""
import json, os, re, sys, collections
sys.path.insert(0, os.path.expanduser("~/.claude/skills/paper2agent/paper2skill/scripts"))
R = os.path.expanduser("~/AI_agents/paper2agent/Reachability")
D = f"{R}/paper-review/devonport2020estimating-paper/documents/s001-devonport2020estimating"
TOK = re.compile(r"[+−-]?(?:\d{1,3}(?:,\d{3})+(?!\d)|\d+)(?:\.\d+)*(?:[eE][+−-]?\d+)?%?")
def toks(t):
    return collections.Counter(TOK.findall(t.replace("*", "").replace("_", "")))
ver = json.load(open(f"{D}/verification.json"))
for p in ver["pages"]:
    nd = p["number_differences"]
    if not (nd["missing"] or nd["extra"]):
        continue
    pn = p["page"]
    print(f"=== page {pn}: tool says missing={nd['missing']} extra={nd['extra']}")
    page = json.load(open(f"{D}/pages/page-{pn:04d}.json"))
    ev = json.load(open(f"{D}/evidence/page-{pn:04d}.json"))
    excl = [i["bbox"] for i in page["items"] if i["kind"] in ("figure", "formula", "omit")]
    def inside(b):
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        return any(e[0] <= cx <= e[2] and e[1] <= cy <= e[3] for e in excl)
    for l in ev["lines"]:
        if inside(l["bbox"]):
            continue
        t = toks(l["text"])
        odd = {k: v for k, v in t.items() if k[0] in "+−-" or "," in k}
        if odd:
            print(f"   PDF line y={l['bbox'][1]:.0f}: {l['text']!r} -> signed/grouped tokens {odd}")
    for i in page["items"]:
        if i["kind"] not in ("text", "caption", "heading"):
            continue
        t = toks(i["markdown"])
        odd = {k: v for k, v in t.items() if k[0] in "+−-" or "," in k}
        tag = " [whole item is outside the line check: transcription of an image-cropped region]" if i["id"].endswith("algorithm1-text") else ""
        if odd or tag:
            print(f"   MD item {i['id']}: signed/grouped tokens {odd}; all tokens {dict(t) if tag else ''}{tag}")
