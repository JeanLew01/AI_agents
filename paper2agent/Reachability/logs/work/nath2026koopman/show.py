#!/usr/bin/env python3
"""show.py N : print extractor items (id, kind, bbox, text head) of page N from the backup."""
import json,sys,pathlib
S=pathlib.Path(__file__).parent
n=int(sys.argv[1]); full=len(sys.argv)>2
p=json.load(open(S/f"orig_pages/page-{n:04d}.json"))
print("warnings:",p.get("warnings"))
for i in p["items"]:
    b=[round(x,1) for x in i["bbox"]]
    md=i.get("markdown","")
    extra={k:v for k,v in i.items() if k not in("id","kind","bbox","markdown","source_class","rows")}
    print(i["id"],i["kind"],b,extra if extra else "")
    print("    ",(md if full else md[:160]).replace("\n"," / "))
    if i.get("rows"): print("    rows:",i["rows"])
