#!/usr/bin/env python3
"""Scan the reviewed page JSON files (or a built paper.md given as argument) for leftover extraction damage."""
import json, glob, re, sys, os
D = os.path.expanduser("~/AI_agents/paper2agent/Reachability/paper-review/nath2026koopman-paper/documents/s001-nath2026koopman")
PAT = ["](", "<u>", "<sup>", "~~", "^*", "�", " ˆ", "_ _", "** **", "´", "  "]
def scan(name, md):
    for x in PAT:
        if x in md:
            print(name, repr(x), md[max(0, md.index(x) - 40): md.index(x) + 40].replace("\n", " "))
    nm = re.sub(r"\$\$.*?\$\$", "", md, flags=re.S)
    nm = re.sub(r"\$[^$]*\$", "", nm)
    nm = re.sub(r"`[^`]*`", "", nm)
    if "_" in nm:
        k = nm.index("_"); print(name, "underscore outside math:", nm[max(0, k - 40): k + 40].replace("\n", " "))
    if nm.count("*") % 2:
        print(name, "odd number of *")
if len(sys.argv) > 1:
    scan(sys.argv[1], open(sys.argv[1], encoding="utf-8").read())
else:
    for f in sorted(glob.glob(f"{D}/pages/*.json")):
        for i in json.load(open(f))["items"]:
            if i["kind"] in ("text", "caption", "heading"):
                scan(i["id"], i["markdown"])
print("scan done")
