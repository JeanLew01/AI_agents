"""Stage 6: claims vs evidence, limitations, rebuttal commitments."""

from __future__ import annotations

import math
import re
from collections import Counter
from typing import Literal

from pydantic import BaseModel, Field

from ..llm.context import env_label, provable_envs, render_range
from ..llm.structured import ask_json
from ..models import Severity
from ..registry import Check, SkipCheck, register
from ..tex.source import latex_to_text, prose_mask
from .llm_common import LLMCheck
from .stage4_consistency import _region_ranges

STRONG_RX = re.compile(r"\b(guarantee[sd]?|provabl[ey]|optimal(?:ly|ity)?|always|never|first|"
                       r"state[- ]of[- ]the[- ]art|outperforms?\s+all)\b", re.I)


@register
class StrongWords(Check):
    id = "claims.strong_words"
    stage = 6
    severity = Severity.INFO
    why = "Strong words in the abstract/introduction/conclusion need a theorem or experiment behind them."

    def run(self, ctx):
        proj = ctx.project
        out = []
        for region, a, b in _region_ranges(proj):
            masked = prose_mask(proj.flat[a:b])
            for m in STRONG_RX.finditer(masked):
                out.append(self.at(ctx, a + m.start(), f"strong claim '{m.group(0)}' in the {region}: check that a "
                                                       f"theorem, experiment or citation backs it"))
        return out


@register
class Limitations(Check):
    id = "claims.limitations"
    stage = 6
    severity = Severity.WARN
    why = "A non-trivial limitations discussion is expected (and required by some venues)."

    def run(self, ctx):
        proj = ctx.project
        required = [s for s in ctx.config.sections_for("required", ctx.mode) if re.search("limitation", s.name + s.pattern, re.I)]
        min_words = max([s.min_words for s in required] + [int(self.opt(ctx, "min_words", 50))])
        sec = proj.find_section(r"limitation", max_level=5)
        if sec is None:
            if required:
                return []  # reported as structure.required_sections
            return [self.finding(ctx, "no Limitations section or paragraph", file=proj.main,
                                 instructions="Add a section discussing the assumptions and failure modes.")]
        a, b = proj.section_range(sec)
        if sec.level >= 4:  # \paragraph{Limitations}: until the next blank line
            nxt = re.search(r"\n\s*\n", proj.flat[sec.end:])
            b = sec.end + (nxt.start() if nxt else 2000)
        text = latex_to_text(proj.flat[sec.end:b])
        words = len(text.split())
        ctx.metrics["limitations_words"] = words
        out = []
        if words < min_words:
            out.append(self.at(ctx, sec.start, f"Limitations section is only {words} words (minimum {min_words})",
                               instructions="Discuss concrete assumptions, failure cases and scope."))
        elif re.fullmatch(r"(?is).{0,200}\b(future work|beyond the scope)\b.{0,200}", text) and words < 2 * min_words:
            out.append(self.at(ctx, sec.start, "Limitations section only defers to future work",
                               severity=Severity.INFO))
        return out


class ClaimItem(BaseModel):
    quote: str
    file: str
    line: int
    claim: str
    status: Literal["supported", "partially_supported", "unsupported"]
    evidence: list[str] = Field(default_factory=list)
    unbacked_strong_words: list[str] = Field(default_factory=list)
    message: str = ""


class ClaimsAnswer(BaseModel):
    claims: list[ClaimItem] = Field(default_factory=list)


CLAIMS_SCHEMA = {
    "type": "object",
    "properties": {"claims": {"type": "array", "items": {
        "type": "object",
        "properties": {
            "quote": {"type": "string"}, "file": {"type": "string"}, "line": {"type": "integer"},
            "claim": {"type": "string"},
            "status": {"type": "string", "enum": ["supported", "partially_supported", "unsupported"]},
            "evidence": {"type": "array", "items": {"type": "string"}},
            "unbacked_strong_words": {"type": "array", "items": {"type": "string"}},
            "message": {"type": "string"},
        },
        "required": ["quote", "file", "line", "claim", "status", "evidence", "unbacked_strong_words", "message"],
        "additionalProperties": False}}},
    "required": ["claims"], "additionalProperties": False,
}

CLAIMS_TASK = """Extract every contribution claim made in the abstract and introduction below, and map each to the
part of the paper that supports it, using the outline (theorems, sections, figures, tables) below.
For each claim give: the exact quote (file and line from the excerpt headers), a one-line paraphrase,
status (supported / partially_supported / unsupported), the evidence labels or section titles, and any strong
words ("guarantee", "optimal", "always", "first", "state of the art", ...) that the evidence does not back.

{front}

=== outline of the rest of the paper ===
{outline}
"""


@register
class ClaimsSupport(LLMCheck):
    id = "claims.support"
    stage = 6
    severity = Severity.WARN
    why = "Every contribution claim must be backed by a theorem, experiment or citation in the paper."

    def run(self, ctx):
        proj = ctx.project
        regions = [r for r in _region_ranges(proj) if r[0] in ("abstract", "introduction")]
        if not regions:
            raise SkipCheck("no abstract/introduction found")
        front = "\n\n".join(render_range(proj, a, b, name) for name, a, b in regions)
        outline = []
        for s in proj.sections:
            if s.level <= 2:
                outline.append(f"{'  ' * (s.level - 1)}section: {s.title}" + (f" [{s.label}]" if s.label else ""))
        for env in provable_envs(proj):
            lab = env_label(proj, env)
            outline.append(f"{env.name} [{lab or '-'}]: {latex_to_text(proj.flat[env.body_start:env.body_end])[:300]}")
        for e in proj.envs_named("figure", "figure*", "table", "table*"):
            cap = re.search(r"\\caption\{", proj.flat[e.start:e.end])
            lab = next((l.key for l in proj.labels if e.start <= l.start < e.end), "-")
            if cap:
                outline.append(f"{e.name} [{lab}]: {latex_to_text(proj.flat[e.start + cap.end():e.end])[:200]}")
        ans = ask_json(ctx, ClaimsAnswer, CLAIMS_SCHEMA, task=self.id, item="front",
                       prompt=CLAIMS_TASK.format(front=front, outline="\n".join(outline)[:ctx.config.llm.max_context_chars]))
        if ans is None:
            return []
        out = []
        ctx.metrics["claims"] = [{"claim": c.claim, "status": c.status, "evidence": c.evidence} for c in ans.claims]
        for c in ans.claims:
            if c.status == "supported" and not c.unbacked_strong_words:
                continue
            words = f" (unbacked: {', '.join(c.unbacked_strong_words)})" if c.unbacked_strong_words else ""
            sev = Severity.WARN if c.status == "unsupported" or c.unbacked_strong_words else Severity.INFO
            f = self.verified(ctx, quote=c.quote, file=c.file, line=c.line, severity=sev,
                              message=f"claim {c.status.replace('_', ' ')}: {c.claim}{words}. {c.message}".strip())
            if f:
                out.append(f)
        return out


# ---- rebuttal commitments -----------------------------------------------------------------

COMMIT_RX = re.compile(
    r"\bwe\s+(?:will|shall|'ll|plan to|are going to|have)\s+(?:also\s+|now\s+|further\s+)?"
    r"(?:add|added|include|included|clarify|clarified|revise|revised|discuss|discussed|move|moved|expand|expanded|"
    r"provide|provided|report|reported|update|updated|fix|fixed|correct|corrected|cite|cited|incorporate|"
    r"incorporated|release|released|rewrite|rewritten|elaborate|elaborated|explain|explained|state|stated|"
    r"highlight|highlighted|emphasize|emphasized|compare|compared|mention|mentioned|remove|removed|rename|renamed)\b|"
    r"\bwill be\s+(?:added|included|clarified|discussed|moved|expanded|provided|reported|updated|fixed|corrected|"
    r"cited|released|revised)\b|\b(?:in|to)\s+the\s+(?:final|camera[- ]ready|revised)\s+version\b", re.I)
META = set("""a an the and or of to in on for with by from at as is are be this that these those we our us it its
will shall also add added include included clarify clarified revise revised discuss discussed discussion move moved
expand expanded provide provided report reported update updated fix fixed correct corrected cite cited incorporate
release released rewrite elaborate explain explained state stated highlight emphasize compare compared comparison
mention mentioned remove removed rename section sec appendix table figure fig paper version final camera ready
revised text paragraph sentence detail details more new additional brief short thank thanks reviewer reviewers
response comment comments point suggestion suggestions agree indeed now further analysis result results experiment
experiments""".split())


def _stem(w: str) -> str:
    w = w.lower()
    for suf in ("ations", "ation", "ings", "ing", "ies", "es", "ed", "s"):
        if len(w) > len(suf) + 3 and w.endswith(suf):
            return w[: -len(suf)]
    return w


def _keywords(sentence: str) -> list[str]:
    s = re.sub(r"\b(?:sec(?:tion|\.)?|appendix|table|fig(?:ure|\.)?)\s*~?[A-Z0-9IVX.]+", " ", sentence, flags=re.I)
    words = re.findall(r"[A-Za-z][A-Za-z-]{2,}", s)
    return sorted({_stem(w) for w in words if w.lower() not in META})


def _sentences(text: str) -> list[tuple[int, str]]:
    """(line, sentence) pairs from a markdown/plain rebuttal."""
    out = []
    for ln_no, ln in enumerate(text.splitlines(), 1):
        for s in re.split(r"(?<=[.!?])\s+", re.sub(r"\*\*[^*]+\*\*", " ", ln)):
            if s.strip():
                out.append((ln_no, s.strip()))
    return out


def _target_range(proj, sentence: str):
    m = re.search(r"\bsec(?:tion|\.)?\s*~?(\d+|[IVX]+)", sentence, re.I)
    main_secs = [s for s in proj.sections if s.level == 1 and not s.starred and not proj.in_appendix(s.start)]
    if m:
        tok = m.group(1)
        idx = int(tok) if tok.isdigit() else {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8}.get(tok.upper(), 0)
        if 1 <= idx <= len(main_secs):
            return main_secs[idx - 1]
    m = re.search(r"\b(?:the\s+)?([A-Z][a-z]+(?:\s+[A-Z]?[a-z]+)?)\s+section\b", sentence)
    if m:
        sec = proj.find_section(re.escape(m.group(1).split()[-1]), max_level=3)
        if sec:
            return sec
    m = re.search(r"\bappendix\s*~?([A-Z])\b", sentence, re.I)
    if m and proj.appendix_start is not None:
        app = [s for s in proj.sections if s.level == 1 and proj.in_appendix(s.start)]
        k = ord(m.group(1).upper()) - ord("A")
        if 0 <= k < len(app):
            return app[k]
    return None


def _paragraphs(proj) -> list[tuple[int, int]]:
    body = proj.flat[: proj.body_end]
    out, pos = [], proj.body_start
    for m in re.finditer(r"\n\s*\n", body[proj.body_start:]):
        end = proj.body_start + m.start()
        if end > pos:
            out.append((pos, end))
        pos = proj.body_start + m.end()
    out.append((pos, proj.body_end))
    return out


def commitments(ctx) -> list[tuple[int, str]]:
    return [(ln, s) for ln, s in _sentences(ctx.rebuttal_text or "") if COMMIT_RX.search(s)]


def locate_commitment(ctx, sentence: str) -> tuple[float, int | None, str | None]:
    """Keyword (IDF-weighted) match of a commitment against its target section or the whole paper.
    Returns (score in [0,1], flat offset of the best paragraph, target section title)."""
    proj = ctx.project
    kws = _keywords(sentence)
    if not kws:
        return 0.0, None, None
    paras = _paragraphs(proj)
    texts = [{_stem(w) for w in re.findall(r"[A-Za-z][A-Za-z-]{2,}", latex_to_text(proj.flat[a:b]))} for a, b in paras]
    df = Counter(w for t in texts for w in set(t))
    idf = {k: math.log((len(texts) + 1) / (df.get(k, 0) + 1)) + 1 for k in kws}
    target = _target_range(proj, sentence)
    cands = list(range(len(paras)))
    if target is not None:
        ta, tb = proj.section_range(target)
        cands = [i for i, (a, b) in enumerate(paras) if a < tb and b > ta]
        title_words = {_stem(w) for w in re.findall(r"[A-Za-z]{3,}", target.title)}
        for i in cands:
            texts[i] = texts[i] | title_words
    best, best_i = 0.0, None
    for i in cands:
        score = sum(idf[k] for k in kws if k in texts[i]) / sum(idf.values())
        if score > best:
            best, best_i = score, i
    return best, (paras[best_i][0] if best_i is not None else None), (target.title if target else None)


@register
class RebuttalCommitments(Check):
    id = "rebuttal.commitments"
    stage = 6
    requires = frozenset({"rebuttal"})
    severity = Severity.WARN
    why = "Promises made in the rebuttal are part of the acceptance; reviewers and chairs check them."

    def run(self, ctx):
        if ctx.llm.available and not ctx.options.no_llm:
            raise SkipCheck("handled by rebuttal.commitments_llm")
        thr = float(self.opt(ctx, "min_score", 0.6))
        items = commitments(ctx)
        if not items:
            raise SkipCheck("no commitments found in the rebuttal")
        out, table = [], []
        for ln, s in items:
            score, off, target = locate_commitment(ctx, s)
            where = None
            if off is not None:
                loc = ctx.project.locate(off)
                where = f"{loc.file}:{loc.line}"
            ok = score >= thr
            table.append({"line": ln, "commitment": s, "status": "likely addressed" if ok else "not found",
                          "score": round(score, 2), "target": target, "best_match": where})
            if not ok:
                out.append(self.finding(ctx, f"rebuttal commitment not found in the paper"
                                             f"{f' (target: {target})' if target else ''}: {s}",
                                        file=str(ctx.options.rebuttal), line=ln, quote=s,
                                        instructions="Make the promised change, or explain to the chairs why not."))
        ctx.metrics["rebuttal_commitments"] = table
        return out


class Commitment(BaseModel):
    quote: str
    line: int
    target: str = ""
    what: str


class CommitmentList(BaseModel):
    commitments: list[Commitment] = Field(default_factory=list)


class Evidence(BaseModel):
    file: str
    line: int
    quote: str


class Judgement(BaseModel):
    status: Literal["fulfilled", "partially_fulfilled", "missing"]
    evidence: list[Evidence] = Field(default_factory=list)
    message: str = ""


EXTRACT_SCHEMA = {
    "type": "object",
    "properties": {"commitments": {"type": "array", "items": {
        "type": "object",
        "properties": {"quote": {"type": "string"}, "line": {"type": "integer"}, "target": {"type": "string"},
                       "what": {"type": "string"}},
        "required": ["quote", "line", "target", "what"], "additionalProperties": False}}},
    "required": ["commitments"], "additionalProperties": False,
}
JUDGE_SCHEMA = {
    "type": "object",
    "properties": {
        "status": {"type": "string", "enum": ["fulfilled", "partially_fulfilled", "missing"]},
        "evidence": {"type": "array", "items": {
            "type": "object",
            "properties": {"file": {"type": "string"}, "line": {"type": "integer"}, "quote": {"type": "string"}},
            "required": ["file", "line", "quote"], "additionalProperties": False}},
        "message": {"type": "string"},
    },
    "required": ["status", "evidence", "message"], "additionalProperties": False,
}
EXTRACT_TASK = """List every concrete commitment the authors make in this rebuttal (things they promise to add,
change, clarify or release in the final version). Quote each one exactly (file "rebuttal"), give its line,
the target location if stated (e.g. "Section 4"), and what must change.

=== rebuttal ===
{text}
"""
JUDGE_TASK = """A rebuttal promised: "{what}" (quote: "{quote}"; target: {target}).
Decide from the excerpts of the final paper below whether the promise is fulfilled. Quote the exact evidence
(file and line from the excerpt headers). If it is missing, say what is missing.

{context}
"""


@register
class RebuttalCommitmentsLLM(LLMCheck):
    id = "rebuttal.commitments_llm"
    stage = 6
    requires = frozenset({"llm", "rebuttal"})
    severity = Severity.WARN
    why = "Promises made in the rebuttal are part of the acceptance; reviewers and chairs check them."

    def run(self, ctx):
        from ..llm.verify import project_index

        text = ctx.rebuttal_text or ""
        numbered = "\n".join(f"{i}| {ln}" for i, ln in enumerate(text.splitlines(), 1))
        lst = ask_json(ctx, CommitmentList, EXTRACT_SCHEMA, task=self.id, item="extract",
                       prompt=EXTRACT_TASK.format(text=numbered))
        if lst is None:
            return []
        idx = project_index(ctx)
        proj = ctx.project
        out, table = [], []
        for i, c in enumerate(lst.commitments):
            hit = idx.find(c.quote, "rebuttal", c.line)
            if hit is None or hit[0] != "rebuttal":
                from ..models import DiscardedFinding

                ctx.discarded.append(DiscardedFinding(check_id=self.id, reason="commitment quote not in the rebuttal",
                                                      quote=c.quote[:300]))
                continue
            line = hit[1]
            _score, off, target = locate_commitment(ctx, c.quote + " " + c.what + " " + c.target)
            sec = _target_range(proj, c.target + " " + c.quote)
            blocks = []
            if sec is not None:
                a, b = proj.section_range(sec)
                blocks.append(render_range(proj, a, b, f"section {sec.title}"))
            if off is not None:
                para = next(((a, b) for a, b in _paragraphs(proj) if a <= off < b), None)
                if para and (sec is None or not (proj.section_range(sec)[0] <= para[0] < proj.section_range(sec)[1])):
                    blocks.append(render_range(proj, para[0], para[1], "best keyword match"))
            context = "\n\n".join(blocks)[: ctx.config.llm.max_context_chars] or "(no candidate text found)"
            j = ask_json(ctx, Judgement, JUDGE_SCHEMA, task=self.id, item=f"judge{i}",
                         prompt=JUDGE_TASK.format(what=c.what, quote=c.quote, target=c.target or "not stated",
                                                  context=context))
            if j is None:
                continue
            verified_ev = [e for e in j.evidence if idx.find(e.quote, e.file, e.line)]
            from ..models import DiscardedFinding

            for e in j.evidence:
                if e not in verified_ev:
                    ctx.discarded.append(DiscardedFinding(check_id=self.id, reason="evidence quote not in the paper",
                                                          quote=e.quote[:300], file=e.file, line=e.line))
            status = j.status
            if status != "missing" and not verified_ev:
                status = "unverified"
            table.append({"line": line, "commitment": c.quote, "status": status,
                          "evidence": [f"{e.file}:{e.line}" for e in verified_ev]})
            if status in ("missing", "partially_fulfilled", "unverified"):
                sev = Severity.WARN
                msg = {"missing": "rebuttal commitment not fulfilled",
                       "partially_fulfilled": "rebuttal commitment only partly fulfilled",
                       "unverified": "rebuttal commitment: the model's evidence could not be verified in the paper"}[status]
                f = self.verified(ctx, quote=c.quote, file="rebuttal", line=line, severity=sev,
                                  message=f"{msg}: {c.what}. {j.message}".strip())
                if f:
                    out.append(f)
        ctx.metrics["rebuttal_commitments"] = table
        return out
