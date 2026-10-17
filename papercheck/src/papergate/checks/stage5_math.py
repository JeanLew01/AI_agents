"""Stage 5: math rigor. Deterministic: proofs exist, assumptions are referenced. LLM: per theorem,
with only its dependency context, check assumptions and statement/proof agreement."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

from ..llm.context import dependency_ranges, env_label, find_proof, is_restatement, provable_envs, render_range
from ..llm.structured import ask_json
from ..models import Severity
from ..registry import Check, SkipCheck, register
from .llm_common import LLMCheck


@register
class ProofPresence(Check):
    id = "math.proof_presence"
    stage = 5
    severity = Severity.WARN
    why = "Every theorem, lemma and proposition needs a proof or an explicit pointer to one."

    def run(self, ctx):
        proj = ctx.project
        out = []
        for env in provable_envs(proj):
            if is_restatement(proj, env):
                continue
            info = find_proof(proj, env)
            if info.kind is None:
                lab = env_label(proj, env)
                out.append(self.at(ctx, env.start, f"{env.name}{f' {lab}' if lab else ''} has no proof and no pointer to one",
                                   instructions="Add a proof, 'Proof in Appendix~\\ref{...}', or cite the source of the result."))
        return out


@register
class UnreferencedAssumptions(Check):
    id = "math.assumptions_unreferenced"
    stage = 5
    severity = Severity.WARN
    why = "An assumption that no result refers to is either unused or silently used."

    def run(self, ctx):
        proj = ctx.project
        refd = proj.referenced_keys
        out = []
        for env in proj.envs_named("assumption", "assumption*", "hypothesis", "condition"):
            lab = env_label(proj, env)
            if lab and lab not in refd:
                out.append(self.at(ctx, env.start, f"assumption '{lab}' is never referenced by any result or proof"))
        return out


class Dependency(BaseModel):
    kind: Literal["assumption", "definition", "lemma", "theorem", "equation", "other"]
    label: str
    used_in_proof: bool


class RigorIssue(BaseModel):
    category: Literal["unused_assumption", "unstated_assumption", "quantifier_mismatch",
                      "probability_level_mismatch", "constant_mismatch", "missing_step", "other"]
    severity: Literal["WARN", "INFO"]
    file: str
    line: int
    quote: str
    message: str
    why_it_matters: str = ""


class RigorAnswer(BaseModel):
    theorem: str
    dependencies: list[Dependency] = Field(default_factory=list)
    issues: list[RigorIssue] = Field(default_factory=list)


RIGOR_SCHEMA = {
    "type": "object",
    "properties": {
        "theorem": {"type": "string"},
        "dependencies": {"type": "array", "items": {
            "type": "object",
            "properties": {
                "kind": {"type": "string", "enum": ["assumption", "definition", "lemma", "theorem", "equation", "other"]},
                "label": {"type": "string"},
                "used_in_proof": {"type": "boolean"},
            },
            "required": ["kind", "label", "used_in_proof"], "additionalProperties": False}},
        "issues": {"type": "array", "items": {
            "type": "object",
            "properties": {
                "category": {"type": "string", "enum": ["unused_assumption", "unstated_assumption", "quantifier_mismatch",
                                                        "probability_level_mismatch", "constant_mismatch", "missing_step", "other"]},
                "severity": {"type": "string", "enum": ["WARN", "INFO"]},
                "file": {"type": "string"},
                "line": {"type": "integer"},
                "quote": {"type": "string"},
                "message": {"type": "string"},
                "why_it_matters": {"type": "string"},
            },
            "required": ["category", "severity", "file", "line", "quote", "message", "why_it_matters"],
            "additionalProperties": False}},
    },
    "required": ["theorem", "dependencies", "issues"],
    "additionalProperties": False,
}

RIGOR_TASK = """Check one result of a paper for rigor, using only the excerpts below (the statement, its proof,
and the definitions/assumptions/lemmas they reference).

1. List every assumption, definition and lemma the statement or proof depends on, and whether the proof uses it.
2. Report issues:
   - unused_assumption: an assumption listed in the statement that the proof never uses;
   - unstated_assumption: a property the proof uses that is not in the statement or its referenced assumptions;
   - quantifier_mismatch / probability_level_mismatch / constant_mismatch: the proof concludes something
     different from the statement (for all vs exists, 1-delta vs 1-2delta, a different constant or rate);
   - missing_step: a step that does not follow and is not justified;
   - other: any other concrete rigor problem.
Quote the exact text each issue is about (file and line from the excerpt headers). Do not report style issues.
If an excerpt is cut off, do not report problems caused by the cut.

{context}
"""


@register
class MathRigor(LLMCheck):
    id = "math.rigor"
    stage = 5
    severity = Severity.WARN
    why = "A theorem whose proof does not match its statement or assumptions undermines the paper's claims."

    def run(self, ctx):
        proj = ctx.project
        cap = ctx.config.llm.max_context_chars
        out = []
        n = 0
        for env in provable_envs(proj):
            if is_restatement(proj, env):
                continue
            info = find_proof(proj, env)
            if info.kind not in ("local", "referenced"):
                continue
            label = env_label(proj, env) or f"{env.name}@{proj.locate(env.start).file}:{proj.locate(env.start).line}"
            blocks = [render_range(proj, env.start, env.end, f"statement: {env.name} {label}"),
                      render_range(proj, info.start, info.end, "proof")]
            for key, dep in dependency_ranges(proj, [(env.start, env.end), (info.start, info.end)]):
                if dep.start == env.start:
                    continue
                blocks.append(render_range(proj, dep.start, dep.end, f"referenced: {dep.name} {key}"))
            context, used = [], 0
            for b in blocks:
                if used + len(b) > cap and context:
                    context.append("=== (further referenced excerpts omitted: context budget) ===")
                    break
                context.append(b)
                used += len(b)
            ans = ask_json(ctx, RigorAnswer, RIGOR_SCHEMA, task=self.id, item=label,
                           prompt=RIGOR_TASK.format(context="\n\n".join(context)))
            n += 1
            if ans is None:
                continue
            for iss in ans.issues:
                f = self.verified(ctx, quote=iss.quote, file=iss.file, line=iss.line,
                                  message=f"{label}: {iss.category.replace('_', ' ')}: {iss.message}",
                                  severity=iss.severity, why=iss.why_it_matters)
                if f:
                    out.append(f)
        if n == 0:
            raise SkipCheck("no theorem with a locatable proof")
        ctx.metrics.setdefault("llm_calls", {})[self.id] = n
        return out
