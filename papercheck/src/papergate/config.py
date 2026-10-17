"""Venue configuration (YAML). No venue logic lives in code; everything venue-specific is here."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Literal

import yaml
from pydantic import BaseModel, ConfigDict, Field, field_validator

from .models import Severity

ANONYMIZATION_SERVICES = [
    "anonymous.4open.science",
    "anonymous.github",
    "anonymousfiles.io",
    "anonymous-url",
    "openreview.net/attachment",
]


class ConfigError(Exception):
    pass


class _Strict(BaseModel):
    model_config = ConfigDict(extra="forbid")


class TemplateSpec(_Strict):
    file: str | None = None  # official .sty/.cls name, e.g. corl_2026.sty
    sha256: str | None = None  # hash of the official version of that file
    official_path: str | None = None  # optional local copy of the official file (diffed against)
    # Expected layout of the official template in pt (as measured by `papergate measure-template`
    # or by a check run on the official example); used to detect layout hacks and margin ink.
    layout: dict[str, float] | None = None
    layout_tolerance_pt: float = 0.5


class PageLimit(_Strict):
    submission: int | None = None
    camera_ready: int | None = None
    # Sections that do not count towards the limit. They are assumed to follow the counted body.
    # Known names: references, appendix, acknowledgments, limitations, checklist, impact_statement
    excluded_sections: list[str] = Field(default_factory=lambda: ["references"])
    # Override the regex used to find a section heading in the PDF text (full-line match).
    heading_patterns: dict[str, str] = Field(default_factory=dict)

    def for_mode(self, mode: str) -> int | None:
        return self.camera_ready if mode == "camera-ready" else self.submission


class Marker(_Strict):
    kind: Literal["package_option", "class_option", "source_regex", "pdf_text", "line_numbers"]
    package: str | None = None  # package or class name for *_option kinds
    option: str | None = None
    pattern: str | None = None  # regex for source_regex / pdf_text
    description: str = ""

    def label(self) -> str:
        if self.description:
            return self.description
        if self.kind in ("package_option", "class_option"):
            return f"[{self.option}] option of {self.package}"
        if self.kind == "line_numbers":
            return "line numbers in the margin"
        return f"{self.kind} /{self.pattern}/"


class SectionSpec(_Strict):
    name: str
    pattern: str  # regex matched (case-insensitive) against a section title / PDF heading line
    min_words: int = 0


class Author(_Strict):
    name: str
    affiliations: list[str] = Field(default_factory=list)
    email: str | None = None


class Fonts(_Strict):
    require_embedded: bool = True
    forbid_type3: bool = True


class PdfVersion(_Strict):
    allowed: list[str] | None = None  # e.g. ["1.4", "1.5", "1.6", "1.7"]


class LLMSettings(_Strict):
    model: str = "claude-opus-5-5"
    effort: Literal["low", "medium", "high", "xhigh", "max"] = "high"
    max_tokens: int = 16000
    max_severity: Severity = Severity.WARN  # LLM findings are capped at this severity
    max_context_chars: int = 30000


class ComplianceNote(_Strict):
    text: str
    modes: list[str] = Field(default_factory=lambda: ["camera-ready", "submission"])


class VenueConfig(_Strict):
    name: str
    template: TemplateSpec = Field(default_factory=TemplateSpec)
    engine: Literal["pdflatex", "lualatex", "xelatex"] = "pdflatex"
    main_file: str | None = None
    texinputs: list[str] = Field(default_factory=list)
    page_limit: PageLimit = Field(default_factory=PageLimit)
    review_mode_markers: list[Marker] = Field(default_factory=list)
    final_mode_markers: list[Marker] = Field(default_factory=list)
    required_sections: dict[str, list[SectionSpec]] = Field(default_factory=dict)
    forbidden_sections: dict[str, list[SectionSpec]] = Field(default_factory=dict)
    fonts: Fonts = Field(default_factory=Fonts)
    max_file_size_mb: float | dict[str, float] | None = None
    pdf_version: PdfVersion = Field(default_factory=PdfVersion)
    abstract_max_words: int | dict[str, int] | None = None
    title: str | None = None
    authors: list[Author] = Field(default_factory=list)
    identity_terms: list[str] = Field(default_factory=list)
    anonymization_services: list[str] = Field(default_factory=lambda: list(ANONYMIZATION_SERVICES))
    compliance_notes: list[ComplianceNote] = Field(default_factory=list)
    checks: dict[str, dict[str, Any]] = Field(default_factory=dict)
    severity_overrides: dict[str, Severity] = Field(default_factory=dict)
    disabled_checks: list[str] = Field(default_factory=list)
    llm: LLMSettings = Field(default_factory=LLMSettings)
    # Values not yet confirmed against the official call for papers: dotted path -> note.
    todo: dict[str, str] = Field(default_factory=dict)

    # Filled by the loader, not by YAML.
    source_files: list[str] = Field(default_factory=list, exclude=True)
    config_hash: str = Field(default="", exclude=True)

    @field_validator("compliance_notes", mode="before")
    @classmethod
    def _notes(cls, v: Any) -> Any:
        return [{"text": n} if isinstance(n, str) else n for n in (v or [])]

    @field_validator("required_sections", "forbidden_sections", mode="before")
    @classmethod
    def _per_mode_sections(cls, v: Any) -> Any:
        if isinstance(v, list):  # same list for both modes
            return {"camera-ready": v, "submission": v}
        return {_mode_key(k): val for k, val in (v or {}).items()}

    # --- accessors -------------------------------------------------------------------
    def sections_for(self, which: str, mode: str) -> list[SectionSpec]:
        table = self.required_sections if which == "required" else self.forbidden_sections
        return table.get(mode, [])

    def max_size_mb(self, mode: str) -> float | None:
        v = self.max_file_size_mb
        if isinstance(v, dict):
            return {_mode_key(k): x for k, x in v.items()}.get(mode)
        return v

    def abstract_limit(self, mode: str) -> int | None:
        v = self.abstract_max_words
        if isinstance(v, dict):
            return {_mode_key(k): x for k, x in v.items()}.get(mode)
        return v

    def notes_for(self, mode: str) -> list[str]:
        return [n.text for n in self.compliance_notes if mode in [_mode_key(m) for m in n.modes]]

    def opt(self, check_id: str, key: str, default: Any = None) -> Any:
        """Per-check option: checks.<check_id>.<key>, falling back to checks.<group>.<key>."""
        for k in _id_prefixes(check_id):
            section = self.checks.get(k)
            if section and key in section:
                return section[key]
        return default

    def is_disabled(self, check_id: str) -> bool:
        return any(p in self.disabled_checks for p in _id_prefixes(check_id))


def _mode_key(k: str) -> str:
    return "camera-ready" if k.replace("_", "-") == "camera-ready" else k


def _id_prefixes(check_id: str) -> list[str]:
    parts = check_id.split(".")
    return [".".join(parts[:i]) for i in range(len(parts), 0, -1)]


_PATH_FIELDS = (("template", "official_path"),)


def _resolve_paths(raw: dict, base: Path) -> None:
    for outer, inner in _PATH_FIELDS:
        sec = raw.get(outer)
        if isinstance(sec, dict) and sec.get(inner):
            sec[inner] = str((base / Path(sec[inner]).expanduser()).resolve())
    if raw.get("texinputs"):
        raw["texinputs"] = [str((base / Path(p).expanduser()).resolve()) for p in raw["texinputs"]]


def _deep_merge(base: dict, over: dict) -> dict:
    out = dict(base)
    for k, v in over.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _deep_merge(out[k], v)
        else:
            out[k] = v
    return out


def _load_raw(path: Path, seen: tuple[Path, ...] = ()) -> tuple[dict, list[str]]:
    path = path.expanduser().resolve()
    if path in seen:
        raise ConfigError(f"circular 'extends' in {path}")
    if not path.is_file():
        raise ConfigError(f"venue config not found: {path}")
    try:
        raw = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        raise ConfigError(f"{path}: invalid YAML: {e}") from e
    if not isinstance(raw, dict):
        raise ConfigError(f"{path}: top level must be a mapping")
    _resolve_paths(raw, path.parent)
    files = [str(path)]
    parent = raw.pop("extends", None)
    if parent:
        base, base_files = _load_raw(path.parent / parent, seen + (path,))
        raw = _deep_merge(base, raw)
        files = base_files + files
    return raw, files


def load_config(path: str | Path) -> VenueConfig:
    raw, files = _load_raw(Path(path))
    try:
        cfg = VenueConfig.model_validate(raw)
    except Exception as e:  # pydantic.ValidationError, kept readable for the CLI
        raise ConfigError(f"{path}: {e}") from e
    cfg.source_files = files
    cfg.config_hash = hashlib.sha256(
        json.dumps(raw, sort_keys=True, default=str).encode()
    ).hexdigest()[:16]
    return cfg
