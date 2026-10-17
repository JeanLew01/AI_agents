"""Data model of the findings ledger (findings.json)."""

from __future__ import annotations

import hashlib
import re
from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, Field

MODES = ("camera-ready", "submission")
Mode = Literal["camera-ready", "submission"]


class Severity(str, Enum):
    BLOCKER = "BLOCKER"
    WARN = "WARN"
    INFO = "INFO"

    @property
    def rank(self) -> int:
        return {"BLOCKER": 0, "WARN": 1, "INFO": 2}[self.value]


class Location(BaseModel):
    file: str | None = None
    line: int | None = None
    page: int | None = None

    def __str__(self) -> str:
        parts = []
        if self.file:
            parts.append(self.file + (f":{self.line}" if self.line else ""))
        if self.page:
            parts.append(f"p.{self.page}")
        return " ".join(parts) or "-"


class Fix(BaseModel):
    kind: Literal["patch", "manual"] = "manual"
    patch: str | None = None
    instructions: str = ""


class Finding(BaseModel):
    id: str = ""
    fingerprint: str = ""
    check_id: str
    stage: int
    severity: Severity
    mode: str = ""
    location: Location = Field(default_factory=Location)
    quote: str = ""
    message: str
    why_it_matters: str = ""
    fix: Fix = Field(default_factory=Fix)
    source: Literal["deterministic", "llm"] = "deterministic"

    def fingerprint_basis(self) -> str:
        # Line numbers are deliberately left out: edits above a finding shift its line,
        # and the fingerprint must survive that so `diff` can track it across runs.
        quote = re.sub(r"\s+", " ", self.quote).strip()
        anchor = quote or self.message
        page = "" if (quote or self.location.file) else str(self.location.page or "")
        return "\x1f".join([self.check_id, self.location.file or "", page, anchor])


def fingerprint(basis: str, occurrence: int) -> str:
    return hashlib.sha256(f"{basis}\x1f{occurrence}".encode()).hexdigest()[:16]


class SkippedCheck(BaseModel):
    check_id: str
    reason: str


class CrashedCheck(BaseModel):
    check_id: str
    error: str


class DiscardedFinding(BaseModel):
    check_id: str
    reason: str
    quote: str = ""
    file: str | None = None
    line: int | None = None


class ReadOnlyResult(BaseModel):
    verified: bool = False
    files_hashed: int = 0
    changes: list[str] = Field(default_factory=list)


class RunHeader(BaseModel):
    tool: str = "papergate"
    tool_version: str
    paper_dir: str
    main_file: str | None = None
    venue_name: str
    venue_config: str
    venue_config_hash: str
    mode: str
    source_tree_hash: str
    model: str | None = None
    started: str
    finished: str | None = None
    read_only: ReadOnlyResult = Field(default_factory=ReadOnlyResult)
    verdict: Literal["PASS", "FAIL", "ERROR"] = "ERROR"
    counts: dict[str, int] = Field(default_factory=dict)
    checks_run: list[str] = Field(default_factory=list)
    checks_skipped: list[SkippedCheck] = Field(default_factory=list)
    checks_crashed: list[CrashedCheck] = Field(default_factory=list)
    discarded_unverifiable: list[DiscardedFinding] = Field(default_factory=list)
    unconfirmed_config: dict[str, str] = Field(default_factory=dict)
    # Everything needed to re-run the same check (used by `papergate apply`).
    invocation: dict[str, Any] = Field(default_factory=dict)


class Ledger(BaseModel):
    header: RunHeader
    findings: list[Finding] = Field(default_factory=list)
    manual_checklist: list[str] = Field(default_factory=list)
    metrics: dict[str, Any] = Field(default_factory=dict)
