"""Stage 3 (submission), LLM-assisted: self-citations that reveal authorship."""

from __future__ import annotations

import re

from pydantic import BaseModel, Field

from ..llm.context import render_range
from ..llm.structured import ask_json
from ..models import Severity
from ..registry import SkipCheck, register
from .llm_common import LLMCheck


class SelfCiteItem(BaseModel):
    file: str
    line: int
    quote: str
    message: str


class SelfCiteAnswer(BaseModel):
    items: list[SelfCiteItem] = Field(default_factory=list)


SCHEMA = {
    "type": "object",
    "properties": {"items": {"type": "array", "items": {
        "type": "object",
        "properties": {"file": {"type": "string"}, "line": {"type": "integer"}, "quote": {"type": "string"},
                       "message": {"type": "string"}},
        "required": ["file", "line", "quote", "message"], "additionalProperties": False}}},
    "required": ["items"], "additionalProperties": False,
}
TASK = """This paper is under double-blind review. Below are the passages that contain citations.
Find sentences that reveal that the authors wrote a cited work (e.g. "our prior work [3]", "we previously showed [5]",
"as in our earlier paper", "building on our system [7]"). Neutral third-person citations ("Smith et al. [3] showed")
are fine. Quote each offending phrase exactly with its file and line.

{context}
"""


@register
class SelfCitationLLM(LLMCheck):
    id = "identity.self_citation_llm"
    stage = 3
    applies_to_modes = ("submission",)
    severity = Severity.WARN
    why = "First-person references to cited work reveal the authors in a double-blind review."

    def run(self, ctx):
        proj = ctx.project
        paras = []
        for m in re.finditer(r"[^\n]*\\cite[a-zA-Z]*\*?(?:\[[^\]]*\])*\{[^}]*\}[^\n]*", proj.flat[proj.body_start:proj.body_end]):
            a = proj.body_start + m.start()
            if re.search(r"\b(?:we|our|us)\b", m.group(0), re.I):
                paras.append((a, a + len(m.group(0)) + 1))
        if not paras:
            raise SkipCheck("no first-person sentences near citations")
        blocks = [render_range(proj, a, b, f"passage {i + 1}") for i, (a, b) in enumerate(paras[:60])]
        ans = ask_json(ctx, SelfCiteAnswer, SCHEMA, task=self.id, item="all",
                       prompt=TASK.format(context="\n\n".join(blocks)[: ctx.config.llm.max_context_chars]))
        if ans is None:
            return []
        return [f for it in ans.items
                if (f := self.verified(ctx, quote=it.quote, file=it.file, line=it.line,
                                       message=f"self-citation reveals authorship: {it.message}",
                                       instructions="Rephrase in the third person."))]
