#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pymupdf==1.28.2", "pymupdf4llm==1.28.2", "pypdf==6.18.1"]
# ///
"""Reviewer helpers for Paper2Skill page review (read-only with respect to review plans).

  overlay DOC PAGE OUT.png [--dpi 110]      page render with every item's bbox, id and kind drawn on it
  crop    DOC PAGE X0 Y0 X1 Y1 OUT.png [--dpi 200]   render one region given in PDF points
  lines   DOC PAGE [X0 Y0 X1 Y1]             native text lines (optionally only those centred in a region)
  check   DOC PAGE [PAGE ...]                run the verifier's per-page text/number checks on the current page plan

DOC is a document directory such as paper-review/<name>/documents/<source-id>.
The check reproduces pdf_to_skill.verify_work for single pages without building.
"""
import argparse, csv, io, json, re, sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / ".claude/skills/paper2agent/paper2skill/scripts"))
import pymupdf
import pdf_to_skill as eng

COLORS = {"text": (0, 0.45, 1), "heading": (0.6, 0, 0.8), "caption": (0, 0.6, 0.3), "figure": (1, 0, 0),
          "formula": (1, 0.5, 0), "table": (0.55, 0.35, 0), "omit": (0.5, 0.5, 0.5), "code": (0, 0.6, 0.6)}


def load(doc_dir, page):
    doc_dir = Path(doc_dir)
    state = json.loads((doc_dir / f"pages/page-{page:04d}.json").read_text(encoding="utf-8"))
    return doc_dir, state, pymupdf.open(doc_dir / "source.pdf")


def overlay(a):
    doc_dir, state, doc = load(a.doc, a.page)
    tmp = pymupdf.open(); tmp.insert_pdf(doc, from_page=a.page - 1, to_page=a.page - 1)
    page = tmp[0]
    for n, item in enumerate(state["items"]):
        r = pymupdf.Rect(item["bbox"]); c = COLORS.get(item["kind"], (0, 0, 0))
        page.draw_rect(r, color=c, width=0.8)
        tag = f"{n}:{item['id'].split('-')[-1]}:{item['kind'][:4]}"
        page.insert_text((r.x0 + 1, r.y0 + 6), tag, fontsize=5.5, color=c)
    page.get_pixmap(dpi=a.dpi, alpha=False).save(a.out)
    print(a.out, f"{len(state['items'])} items; tag = order:id-suffix:kind")


def crop(a):
    doc_dir = Path(a.doc); doc = pymupdf.open(doc_dir / "source.pdf")
    page = doc[a.page - 1]
    r = pymupdf.Rect(a.box) & page.rect
    page.get_pixmap(clip=r, dpi=a.dpi, alpha=False).save(a.out)
    print(a.out, "page size (pt):", page.rect.width, page.rect.height)


def lines(a):
    doc_dir = Path(a.doc); doc = pymupdf.open(doc_dir / "source.pdf")
    region = pymupdf.Rect(a.box) if a.box else None
    for line in eng.source_lines(doc[a.page - 1]):
        r = pymupdf.Rect(line["bbox"]); center = (r.tl + r.br) / 2
        if region is None or region.contains(center):
            print([round(v, 1) for v in line["bbox"]], repr(line["text"]))


def page_output_text(state):
    pieces = []
    for item in state["items"]:
        kind = item["kind"]
        if kind in {"omit", "figure", "formula"}:
            continue
        if kind == "table":
            if item.get("rows") is not None:
                pieces.append("\n".join(" ".join(row) for row in item["rows"]))
            continue
        text = item.get("markdown", "").strip()
        if text:
            pieces.append(text)
    return "\n\n".join(pieces)


def check(a):
    from pypdf import PdfReader
    bad = 0
    for pn in a.pages:
        doc_dir, state, doc = load(a.doc, pn)
        page = doc[pn - 1]
        problems = []
        ids = [i.get("id") for i in state["items"]]
        if len(ids) != len(set(ids)):
            problems.append("duplicate item ids on page")
        for i in state["items"]:
            try:
                eng.rectangle(i["bbox"], page)
            except Exception as exc:
                problems.append(f"{i.get('id')}: {exc}")
            if i["kind"] not in eng.KINDS:
                problems.append(f"{i.get('id')}: invalid kind {i['kind']}")
            if i["kind"] == "omit" and not str(i.get("reason", "")).strip():
                problems.append(f"{i.get('id')}: omit needs a reason")
            if i["kind"] in {"figure", "formula", "table"} and not eng.valid_name(i.get("asset_name", i["id"])):
                problems.append(f"{i.get('id')}: invalid asset_name {i.get('asset_name')}")
            if i["kind"] == "table" and i.get("rows") is not None:
                rows = i["rows"]
                if not rows or any(len(r) != len(rows[0]) or any(not isinstance(c, str) for c in r) for r in rows):
                    problems.append(f"{i.get('id')}: rows must be rectangular arrays of strings")
        exclusions = [i["bbox"] for i in state["items"] if i["kind"] in {"figure", "formula", "omit"} or
                      (i["kind"] == "table" and i.get("rows") is None)]
        src = [l for l in eng.source_lines(page) if not eng.covered(l, exclusions)]
        text = page_output_text(state)
        compact = eng.canonical(text)
        eligible = [l for l in src if len(eng.canonical(l["text"])) >= 4]
        missing = [l for l in eligible if eng.canonical(l["text"]) not in compact]
        raw = "\n".join(l["text"] for l in src)
        numbers = eng.counter_difference(eng.number_tokens(raw), eng.number_tokens(text))
        clone = pymupdf.open(); clone.insert_pdf(doc, from_page=pn - 1, to_page=pn - 1)
        for box in exclusions:
            clone[0].add_redact_annot(pymupdf.Rect(box), fill=False)
        if exclusions:
            clone[0].apply_redactions(images=0, graphics=0, text=0)
        ip = PdfReader(io.BytesIO(clone.tobytes())).pages[0]
        chunks = []; bottom, top = float(ip.cropbox.bottom), float(ip.cropbox.top)
        def visible(t, cm, tm, font, size):
            y = tm[4] * cm[1] + tm[5] * cm[3] + cm[5]
            extent = abs(size) * max(abs(cm[0]), abs(cm[1]), abs(cm[2]), abs(cm[3]), 1)
            if not (y + extent < bottom or y - extent > top):
                chunks.append(t)
        try:
            ip.extract_text(visitor_text=visible)
        except Exception as exc:
            problems.append(f"independent parser failed: {exc}")
        indep = eng.counter_difference(eng.number_tokens("".join(chunks)), eng.number_tokens(text))
        ok = not problems and not missing and not any(numbers.values())
        bad += not ok
        print(f"== page {pn}: {'OK' if ok else 'ATTENTION'} | reviewed={state['reviewed']} | lines found {len(eligible) - len(missing)}/{len(eligible)}")
        for p in problems:
            print("   structural:", p)
        for l in missing:
            print("   missing line:", [round(v) for v in l["bbox"]], repr(l["text"]))
        if any(numbers.values()):
            print("   number differences (missing = in source, absent from output; extra = only in output):", json.dumps(numbers, ensure_ascii=False))
        if any(indep.values()):
            print("   second-parser number differences (report to coordinator, do not chase blindly):", json.dumps(indep, ensure_ascii=False))
    sys.exit(1 if bad else 0)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = p.add_subparsers(dest="cmd", required=True)
    o = s.add_parser("overlay"); o.add_argument("doc"); o.add_argument("page", type=int); o.add_argument("out"); o.add_argument("--dpi", type=int, default=130); o.set_defaults(f=overlay)
    c = s.add_parser("crop"); c.add_argument("doc"); c.add_argument("page", type=int); c.add_argument("box", type=float, nargs=4); c.add_argument("out"); c.add_argument("--dpi", type=int, default=220); c.set_defaults(f=crop)
    l = s.add_parser("lines"); l.add_argument("doc"); l.add_argument("page", type=int); l.add_argument("box", type=float, nargs="*"); l.set_defaults(f=lines)
    k = s.add_parser("check"); k.add_argument("doc"); k.add_argument("pages", type=int, nargs="+"); k.set_defaults(f=check)
    a = p.parse_args(); a.f(a)


if __name__ == "__main__":
    main()
