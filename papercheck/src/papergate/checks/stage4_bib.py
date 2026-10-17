"""Stage 4: bibliography hygiene (unused, duplicates, arXiv entries, venue name formatting)."""

from __future__ import annotations

import re

from ..models import Severity
from ..registry import Check, SkipCheck, register
from ..tex.source import latex_to_text
from .stage3_identity import bib_entries


def _cited(ctx) -> set[str]:
    return ctx.project.cited_keys


def _norm_title(t: str) -> str:
    return re.sub(r"[^a-z0-9]", "", latex_to_text(t).lower())


def _doi(e: dict) -> str | None:
    d = e.get("doi", "").strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    return d or None


def arxiv_id(e: dict) -> str | None:
    for f in ("eprint", "url", "journal", "note", "howpublished", "booktitle", "volume"):
        v = e.get(f, "")
        m = re.search(r"(?:arxiv(?:\.org/(?:abs|pdf)/|:|\s*preprint\s*arxiv:?\s*)\s*)(\d{4}\.\d{4,5}|[a-z\-]+/\d{7})", v, re.I)
        if m:
            return m.group(1)
        if f == "eprint" and re.fullmatch(r"\d{4}\.\d{4,5}(v\d+)?", v.strip()):
            return v.strip()
    return None


def is_arxiv(e: dict) -> bool:
    venue = " ".join(e.get(f, "") for f in ("journal", "booktitle", "publisher", "howpublished", "note", "archiveprefix", "eprinttype"))
    real_venue = e.get("booktitle", "") or (e.get("journal", "") if "arxiv" not in e.get("journal", "").lower() else "")
    return ("arxiv" in venue.lower() or "arxiv.org" in e.get("url", "").lower()) and not (
        real_venue and "arxiv" not in real_venue.lower())


@register
class UnusedEntries(Check):
    id = "bib.unused_entries"
    stage = 4
    severity = Severity.INFO
    why = "Unused entries are harmless for BibTeX but clutter shared .bib files."

    def run(self, ctx):
        cited = _cited(ctx)
        if "*" in cited:
            raise SkipCheck("\\nocite{*} cites every entry")
        per_file: dict[str, list[dict]] = {}
        for e in bib_entries(ctx):
            if e["ID"] not in cited:
                per_file.setdefault(e["_file"], []).append(e)
        out = []
        for rel, es in per_file.items():
            keys = ", ".join(e["ID"] for e in es[:12]) + (f" (+{len(es) - 12} more)" if len(es) > 12 else "")
            msg = (f"bibliography entry '{es[0]['ID']}' is never cited" if len(es) == 1
                   else f"{len(es)} entries in {rel} are never cited: {keys}")
            out.append(self.finding(ctx, msg, file=rel, line=es[0]["_line"], quote=rel if len(es) > 1 else es[0]["_quote"]))
        return out


@register
class DuplicateEntries(Check):
    id = "bib.duplicates"
    stage = 4
    severity = Severity.WARN
    why = "The same work under two keys appears twice in the reference list."

    def run(self, ctx):
        groups: dict[str, list[dict]] = {}
        for e in bib_entries(ctx):
            keys = [("title", _norm_title(e.get("title", "")))] if e.get("title") else []
            if _doi(e):
                keys.append(("doi", _doi(e)))
            if arxiv_id(e):
                keys.append(("arxiv", arxiv_id(e).split("v")[0]))
            for k in keys:
                if k[1]:
                    groups.setdefault(f"{k[0]}:{k[1]}", []).append(e)
        out, reported = [], set()
        cited = _cited(ctx)
        for gk, es in groups.items():
            ids = tuple(sorted({e["ID"] for e in es}))
            if len(ids) < 2 or ids in reported:
                continue
            reported.add(ids)
            both = [i for i in ids if i in cited]
            e0 = es[0]
            sev = Severity.WARN if len(both) >= 2 else Severity.INFO
            out.append(self.finding(ctx, f"duplicate bibliography entries {', '.join(ids)} (same {gk.split(':')[0]}); "
                                         f"cited: {', '.join(both) or 'none'}", severity=sev,
                                    file=e0["_file"], line=e0["_line"], quote=e0["_quote"],
                                    instructions="Keep one key and replace the others in the text."))
        return out


@register
class ArxivEntries(Check):
    id = "bib.arxiv_published"
    stage = 4
    severity = Severity.INFO
    why = "Cite the peer-reviewed version when an arXiv preprint has been published."

    def run(self, ctx):
        cited = _cited(ctx)
        out = []
        for e in bib_entries(ctx):
            if e["ID"] not in cited or not is_arxiv(e):
                continue
            aid = arxiv_id(e)
            if not ctx.options.online:
                out.append(self.finding(ctx, f"'{e['ID']}' cites an arXiv preprint{f' ({aid})' if aid else ''}; "
                                             f"check for a published version (run with --online to look it up)",
                                        file=e["_file"], line=e["_line"], quote=e["_quote"]))
                continue
            out.append(self._lookup(ctx, e, aid))
        return [f for f in out if f]

    def _lookup(self, ctx, e, aid):
        from .. import online

        found = None
        try:
            if aid:
                meta = online.arxiv_metadata(aid)
                if meta:
                    found = ", ".join(f"{k}: {v}" for k, v in meta.items())
            if not found and e.get("title"):
                d = online.dblp_published(e["title"])
                if d:
                    found = f"{d['venue']} {d.get('year') or ''}".strip() + (f", doi {d['doi']}" if d.get("doi") else "")
        except Exception as ex:
            return self.finding(ctx, f"'{e['ID']}': online lookup failed ({type(ex).__name__}); check manually",
                                file=e["_file"], line=e["_line"], quote=e["_quote"])
        if found:
            return self.finding(ctx, f"'{e['ID']}' cites arXiv but a published version exists: {found}",
                                severity=Severity.WARN, file=e["_file"], line=e["_line"], quote=e["_quote"],
                                instructions="Update the entry to the published version (verify it is the same work).")
        return self.finding(ctx, f"'{e['ID']}' cites arXiv; no published version found online",
                            file=e["_file"], line=e["_line"], quote=e["_quote"])


VENUES = {
    "ICRA": r"\bICRA\b|international conference on robotics (?:and|&) automation|int\.? conf\.? (?:on )?robot(?:ics|\.)? (?:and |& )?autom",
    "IROS": r"\bIROS\b|intelligent robots and systems|intell\.? robots? (?:and )?syst",
    "CoRL": r"\bCoRL\b|conference on robot learning|conf\.? robot\.? learn",
    "RSS": r"\bRSS\b|robotics:? science and systems",
    "NeurIPS": r"neurips|\bnips\b|neural information processing systems|neural inf\.? process\.? syst",
    "ICML": r"\bICML\b|international conference on machine learning",
    "ICLR": r"\bICLR\b|international conference on learning representations",
    "CDC": r"\bCDC\b|conference on decision and control|conf\.? decis(?:ion)?\.? (?:and )?control",
    "ACC": r"\bACC\b|american control conference",
    "L4DC": r"\bL4DC\b|learning for dynamics and control",
    "CVPR": r"\bCVPR\b|computer vision and pattern recognition",
    "AAAI": r"\bAAAI\b|aaai conference on artificial intelligence",
    "T-RO": r"transactions on robotics|trans\.? robot(?:ics)?\b|\bT-?RO\b",
    "RA-L": r"robotics and automation letters|robot\.? autom\.? lett|\bRA-?L\b",
    "TAC": r"transactions on automatic control|trans\.? autom(?:atic)?\.? control|\bTAC\b",
    "IJRR": r"international journal of robotics research|int\.? j\.? robot\.? res|\bIJRR\b",
    "JMLR": r"journal of machine learning research|\bJMLR\b",
    "Science Robotics": r"science robotics|sci\.? robot",
}


def _style_key(s: str) -> str:
    s = latex_to_text(s).lower()
    s = re.sub(r"\b(?:19|20)\d{2}\b|\b\d+(?:st|nd|rd|th)\b|\b(?:first|second|third|[a-z]+th)\b", " ", s)
    s = re.sub(r"\(.*?\)", " ", s)
    s = re.sub(r"[^a-z]+", " ", s)
    s = re.sub(r"\b(?:proceedings|proc|of|the|in)\b", " ", s)
    return re.sub(r"\s+", " ", s).strip()


@register
class VenueFormat(Check):
    id = "bib.venue_format"
    stage = 4
    severity = Severity.WARN
    why = "The same venue written in different forms looks careless in the reference list."

    def run(self, ctx):
        cited = _cited(ctx)
        groups: dict[str, dict[str, list[dict]]] = {}
        for e in bib_entries(ctx):
            if e["ID"] not in cited and "*" not in cited:
                continue
            v = e.get("booktitle") or e.get("journal") or ""
            if not v or "arxiv" in v.lower():
                continue
            canon = next((k for k, rx in VENUES.items() if re.search(rx, latex_to_text(v), re.I)), None)
            if canon is None:
                continue
            groups.setdefault(canon, {}).setdefault(_style_key(v), []).append(e)
        out = []
        for canon, styles in groups.items():
            if len(styles) < 2:
                continue
            forms = [f"'{latex_to_text(es[0].get('booktitle') or es[0].get('journal'))}' ({', '.join(x['ID'] for x in es)})"
                     for es in styles.values()]
            e0 = next(iter(styles.values()))[0]
            out.append(self.finding(ctx, f"{canon} is written in {len(styles)} different forms: " + "; ".join(forms),
                                    file=e0["_file"], line=e0["_line"], quote=e0["_quote"],
                                    instructions="Use one form (full name or one abbreviation style) for every entry."))
        return out
