"""Network lookups, used only when `papergate check --online` is given (stdlib urllib, no new deps)."""

from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = "papergate/0.1 (pre-submission checker)"
_last_arxiv = 0.0


def _get(url: str, timeout: float = 15.0) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310 (https URLs built below)
        return r.read()


def arxiv_metadata(arxiv_id: str) -> dict:
    """journal_ref / doi that the authors registered on arXiv (empty dict if none)."""
    global _last_arxiv
    wait = 3.0 - (time.time() - _last_arxiv)  # arXiv API etiquette: one request per 3 s
    if wait > 0:
        time.sleep(wait)
    _last_arxiv = time.time()
    data = _get("https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(arxiv_id))
    ns = {"a": "http://www.w3.org/2005/Atom", "x": "http://arxiv.org/schemas/atom"}
    root = ET.fromstring(data)
    entry = root.find("a:entry", ns)
    if entry is None:
        return {}
    out = {}
    for tag in ("journal_ref", "doi"):
        el = entry.find(f"x:{tag}", ns)
        if el is not None and el.text:
            out[tag] = el.text.strip()
    return out


def dblp_published(title: str) -> dict | None:
    """A non-CoRR DBLP record whose title matches, if any."""
    q = urllib.parse.quote(re.sub(r"[{}\\]", "", title))
    data = json.loads(_get(f"https://dblp.org/search/publ/api?q={q}&format=json&h=10"))
    hits = ((data.get("result") or {}).get("hits") or {}).get("hit") or []
    want = _norm_title(title)
    for h in hits:
        info = h.get("info", {})
        if _norm_title(info.get("title", "")) != want:
            continue
        venue = info.get("venue", "")
        if isinstance(venue, list):
            venue = ", ".join(venue)
        if venue and venue != "CoRR":
            return {"venue": venue, "year": info.get("year"), "doi": info.get("doi"), "url": info.get("ee") or info.get("url")}
    return None


def _norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]", "", re.sub(r"\\[a-zA-Z]+|[{}]", "", t.lower()))
