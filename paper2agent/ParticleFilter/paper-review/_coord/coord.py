#!/usr/bin/env python3
"""Coordinator helpers for the ParticleFilter Paper2Skill builds (shared files only).

  status                      per-paper page state ([v2] marker) and adjudication notes
  meta PAPER META.json        write title/notes into plan.json and title/review notes/navigation into bundle.json
  bind PAPER                  bind reviewers' adjudication notes to the fingerprints in review-aid/review-queue.json
"""
import json, sys, glob
from pathlib import Path

ROOT = Path("/home/jixia/AI_agents/paper2agent/ParticleFilter/paper-review")
CHECKS = ("missing_lines", "number_differences", "independent_parser_number_differences")


def doc_dir(paper):
    docs = sorted((ROOT / paper / "documents").iterdir())
    assert len(docs) == 1, docs
    return docs[0]


def rj(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def wj(p, d):
    Path(p).write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def status():
    for paper in sorted(p.name for p in ROOT.iterdir() if (p / "bundle.json").exists()):
        d = doc_dir(paper)
        pages = sorted(d.glob("pages/page-*.json"))
        done = [rj(p)["page"] for p in pages if rj(p)["reviewed"] and rj(p).get("review_notes", "").lstrip().startswith("[v2]")]
        notes = sorted(int(p.stem.split("-")[1]) for p in d.glob("adjudication-notes/page-*.json"))
        todo = [rj(p)["page"] for p in pages if rj(p)["page"] not in done]
        print(f"{paper:34s} v2 {len(done):2d}/{len(pages):2d}  todo={todo}  adjudication-notes={notes}")


def meta(paper, meta_path):
    m = rj(meta_path)
    d = doc_dir(paper)
    plan = rj(d / "plan.json")
    plan["title"] = m["title"]
    plan["notes"] = m["notes"]
    if "reading_order" in m:
        plan["reading_order"] = m["reading_order"]
    wj(d / "plan.json", plan)
    b = rj(ROOT / paper / "bundle.json")
    b["title"] = m["title"]
    assert len(b["sources"]) == 1
    s = b["sources"][0]
    s["title"] = m["title"]
    s["reviewed"] = True
    s["review_notes"] = m["source_review_notes"]
    if m.get("navigation") is not None:
        b["navigation"] = m["navigation"]
    wj(ROOT / paper / "bundle.json", b)
    print("meta written for", paper)


def bind(paper):
    d = doc_dir(paper)
    queue = rj(ROOT / paper / "review-aid" / "review-queue.json")
    entries, problems = [], []
    for source in queue["sources"]:
        for item in source["items"]:
            entry = item.get("adjudication_entry")
            if not entry:
                continue
            page, check = entry["page"], entry["check"]
            note_file = d / "adjudication-notes" / f"page-{page:04d}.json"
            reason = rj(note_file).get(check, "").strip() if note_file.exists() else ""
            if not reason:
                problems.append((page, check))
                continue
            entries.append({"page": page, "check": check, "fingerprint": entry["fingerprint"], "reason": reason})
    wj(d / "adjudications.json", {"schema_version": 1, "entries": entries})
    print(f"{paper}: bound {len(entries)} adjudications; without reviewer note: {problems}")
    return problems


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "status":
        status()
    elif cmd == "meta":
        meta(sys.argv[2], sys.argv[3])
    elif cmd == "bind":
        sys.exit(1 if bind(sys.argv[2]) else 0)
