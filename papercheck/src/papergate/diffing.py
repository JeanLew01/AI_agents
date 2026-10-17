"""Compare two ledgers by fingerprint: resolved / new / persisting findings."""

from __future__ import annotations

from pydantic import BaseModel, Field

from .models import Finding, Ledger


class PersistingFinding(BaseModel):
    old_id: str
    new_id: str
    finding: Finding
    severity_changed: str | None = None


class LedgerDiff(BaseModel):
    old_report: str
    new_report: str
    resolved: list[Finding] = Field(default_factory=list)
    new: list[Finding] = Field(default_factory=list)
    persisting: list[PersistingFinding] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)


def diff_ledgers(old: Ledger, new: Ledger) -> LedgerDiff:
    d = LedgerDiff(old_report=old.header.started, new_report=new.header.started)
    if old.header.venue_config_hash != new.header.venue_config_hash:
        d.warnings.append("venue config changed between the runs")
    if old.header.mode != new.header.mode:
        d.warnings.append(f"mode changed ({old.header.mode} -> {new.header.mode})")
    if set(old.header.checks_run) != set(new.header.checks_run):
        d.warnings.append("the set of checks that ran differs (some 'resolved' findings may just not have been checked)")
    old_by = {f.fingerprint: f for f in old.findings}
    new_by = {f.fingerprint: f for f in new.findings}
    for fp, f in old_by.items():
        if fp in new_by:
            n = new_by[fp]
            sev = f"{f.severity.value} -> {n.severity.value}" if f.severity != n.severity else None
            d.persisting.append(PersistingFinding(old_id=f.id, new_id=n.id, finding=n, severity_changed=sev))
        else:
            d.resolved.append(f)
    d.new = [f for fp, f in new_by.items() if fp not in old_by]
    return d


def format_diff(d: LedgerDiff) -> str:
    def line(f: Finding, extra: str = "") -> str:
        return f"  {f.id:>4} {f.severity.value:<7} {f.check_id:<30} {str(f.location):<28} {f.message[:90]}{extra}"

    out = [f"resolved: {len(d.resolved)}   new: {len(d.new)}   persisting: {len(d.persisting)}"]
    for w in d.warnings:
        out.append(f"note: {w}")
    if d.resolved:
        out.append("\nRESOLVED (old ids)")
        out += [line(f) for f in d.resolved]
    if d.new:
        out.append("\nNEW")
        out += [line(f) for f in d.new]
    if d.persisting:
        out.append("\nPERSISTING (old id -> new id)")
        out += [line(p.finding, f"  [{p.old_id}->{p.new_id}{', ' + p.severity_changed if p.severity_changed else ''}]")
                for p in d.persisting]
    return "\n".join(out)
