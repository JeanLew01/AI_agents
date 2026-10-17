"""Findings ledger: severity overrides, de-duplication, fingerprints, IDs, verdict, JSON I/O."""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from .config import VenueConfig
from .models import Finding, Ledger, Severity, fingerprint
from .registry import matches


def _override(f: Finding, config: VenueConfig) -> None:
    best = None
    for sel, sev in config.severity_overrides.items():
        if matches(f.check_id, [sel]) and (best is None or len(sel) > len(best[0])):
            best = (sel, sev)
    if best:
        f.severity = Severity(best[1])


def finalize(ledger: Ledger, config: VenueConfig) -> Ledger:
    seen = set()
    out: list[Finding] = []
    for f in ledger.findings:
        _override(f, config)
        f.mode = f.mode or ledger.header.mode
        key = (f.check_id, f.location.file, f.location.line, f.location.page, f.quote, f.message)
        if key in seen:
            continue
        seen.add(key)
        out.append(f)
    out.sort(key=lambda f: (f.severity.rank, f.stage, f.check_id, f.location.file or "",
                            f.location.line or 0, f.location.page or 0))
    occ: Counter[str] = Counter()
    for i, f in enumerate(out, 1):
        basis = f.fingerprint_basis()
        f.fingerprint = fingerprint(basis, occ[basis])
        occ[basis] += 1
        f.id = f"F{i}"
    ledger.findings = out
    counts = Counter(f.severity.value for f in out)
    ledger.header.counts = {s.value: counts.get(s.value, 0) for s in Severity}
    if not ledger.header.read_only.verified:
        ledger.header.verdict = "ERROR"
    elif counts.get("BLOCKER"):
        ledger.header.verdict = "FAIL"
    else:
        ledger.header.verdict = "PASS"
    return ledger


def write_ledger(ledger: Ledger, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    p = out_dir / "findings.json"
    p.write_text(ledger.model_dump_json(indent=2), encoding="utf-8")
    return p


def read_ledger(path: Path) -> Ledger:
    path = Path(path)
    if path.is_dir():
        path = path / "findings.json"
    if not path.is_file():
        raise FileNotFoundError(f"no findings.json at {path}")
    return Ledger.model_validate(json.loads(path.read_text(encoding="utf-8")))
