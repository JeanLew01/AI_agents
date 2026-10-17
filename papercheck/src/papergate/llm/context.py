"""Build small, line-numbered source excerpts for LLM prompts (one theorem / one claim at a time)."""

from __future__ import annotations

import re
from dataclasses import dataclass

from ..tex.project import Env, TexProject

PROVABLE = {"theorem", "lemma", "proposition", "corollary", "claim", "conjecture"}
REF_RX = re.compile(r"\\(?:ref|cref|Cref|autoref|eqref|labelcref|nameref)\*?\{([^{}]+)\}")


def render_range(proj: TexProject, a: int, b: int, header: str) -> str:
    """Raw source lines covering flat range [a, b), prefixed 'N| ', grouped by file."""
    pieces = []
    for seg in proj.segments:
        lo, hi = max(a, seg.flat_start), min(b, seg.flat_end)
        if lo >= hi:
            continue
        f = proj.files[seg.rel]
        l1 = f.line_of(seg.file_offset + lo - seg.flat_start)
        l2 = f.line_of(seg.file_offset + hi - 1 - seg.flat_start)
        body = "\n".join(f"{n}| {f.line_text(n)}" for n in range(l1, l2 + 1))
        pieces.append(f"--- file {seg.rel}, lines {l1}-{l2} ---\n{body}")
    return f"=== {header} ===\n" + "\n".join(pieces)


def provable_envs(proj: TexProject) -> list[Env]:
    names = {n for n, printed in proj.theorem_envs.items()
             if n.rstrip("*") in PROVABLE or printed.lower() in PROVABLE}
    return [e for e in proj.envs if e.name in names or e.name.rstrip("*") in names]


def env_label(proj: TexProject, env: Env) -> str | None:
    m = re.search(r"\\label\{([^{}]+)\}", proj.flat[env.start:env.end])
    return m.group(1).strip() if m else None


def is_restatement(proj: TexProject, env: Env) -> bool:
    if not env.opt:
        return False
    keys = REF_RX.findall(env.opt)
    own = env_label(proj, env)
    return any(k.strip() != own for k in keys) or bool(re.search(r"restate|restatement|repeated", env.opt, re.I))


@dataclass
class ProofInfo:
    kind: str | None  # local | referenced | pointer | None
    start: int | None = None
    end: int | None = None
    note: str = ""


def find_proof(proj: TexProject, env: Env) -> ProofInfo:
    flat = proj.flat
    label = env_label(proj, env)
    proofs = proj.envs_named("proof", "proof*")
    nxt = next((p for p in proofs if p.start >= env.end), None)
    if nxt is not None:
        gap = flat[env.end:nxt.start]
        if len(gap.strip()) < 400 and not re.search(r"\\begin\{(?!equation|align)", gap):
            return ProofInfo("local", nxt.start, nxt.end)
    if label:
        lab_rx = re.escape(label)
        for p in proofs:
            if p.opt and re.search(r"\{" + lab_rx + r"\}", p.opt):
                return ProofInfo("referenced", p.start, p.end)
        m = re.search(r"proof\s+of\s+[^{}\n]{0,40}?\\(?:ref|cref|Cref|autoref)\{" + lab_rx + r"\}", flat, re.I)
        if m:
            end = len(flat)
            for pat in (r"\\(?:section|subsection)\*?\{", r"\\begin\{(?:theorem|lemma|proposition|corollary)\}",
                        r"\\paragraph\{proof", r"\\end\{document\}"):
                mm = re.search(pat, flat[m.end():], re.I)
                if mm:
                    end = min(end, m.end() + mm.start())
            return ProofInfo("referenced", m.start(), min(end, m.start() + 12000))
    near = (env.opt or "") + flat[env.body_end:env.end + 400]
    if re.search(r"\\cite", env.opt or "") or re.search(
            r"(?:proof|proved|shown|derivation)\b[^.]{0,80}?(?:appendix|section|supplement|\\ref|\\cref|\\cite)|"
            r"\bsee\s+(?:appendix|section|\\ref|\\cref)", near, re.I):
        return ProofInfo("pointer", note="proof is pointed to elsewhere or cited")
    return ProofInfo(None)


def dependency_ranges(proj: TexProject, text_ranges: list[tuple[int, int]], depth: int = 2) -> list[tuple[str, Env]]:
    """Environments (assumptions, definitions, lemmas, equations, ...) referenced from the ranges."""
    seen: dict[str, Env] = {}
    frontier = text_ranges
    for _ in range(depth):
        keys = set()
        for a, b in frontier:
            for k in REF_RX.findall(proj.flat[a:b]):
                keys.update(x.strip() for x in k.split(","))
        new = []
        for k in sorted(keys):
            if k in seen:
                continue
            lab = next((l for l in proj.labels if l.key == k), None)
            if lab is None or lab.env is None or lab.kind in ("figure", "table", "item", "section"):
                continue
            seen[k] = lab.env
            new.append((lab.env.start, lab.env.end))
        frontier = new
        if not new:
            break
    return list(seen.items())
