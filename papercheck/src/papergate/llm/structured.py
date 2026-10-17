"""Ask for JSON, validate it against a schema, retry once, otherwise drop (and count) the answer."""

from __future__ import annotations

import json
import re

from pydantic import BaseModel, ValidationError

from ..models import DiscardedFinding
from .base import LLMError

SYSTEM_RULES = (
    "You are a meticulous reviewer checking an academic LaTeX paper before publication. "
    "Answer only with one JSON object that follows the given JSON schema. "
    "Every quote you give must be copied character for character from the source text shown to you "
    "(without the 'NN| ' line-number prefix); quotes that do not occur verbatim in the source are discarded. "
    "Report only problems you can point to in the text; if there are none, return empty lists."
)


def _extract_json(raw: str) -> str:
    s = raw.strip()
    m = re.search(r"```(?:json)?\s*(.*?)```", s, re.S)
    if m:
        s = m.group(1).strip()
    if not s.startswith("{"):
        a, b = s.find("{"), s.rfind("}")
        if a >= 0 and b > a:
            s = s[a:b + 1]
    return s


def ask_json(ctx, model_cls: type[BaseModel], schema: dict, *, task: str, item: str, prompt: str,
             system: str = SYSTEM_RULES) -> BaseModel | None:
    last = ""
    p = prompt
    for attempt in range(2):
        try:
            raw = ctx.llm.complete(system, p, task=task, item=item, schema=schema)
        except LLMError as e:
            last = f"LLM error: {e}"
            continue
        try:
            return model_cls.model_validate(json.loads(_extract_json(raw)))
        except (json.JSONDecodeError, ValidationError) as e:
            last = f"{type(e).__name__}: {str(e)[:300]}"
            p = (prompt + "\n\nYour previous answer was not valid JSON for the schema (" + last +
                 "). Return only the corrected JSON object.")
    ctx.discarded.append(DiscardedFinding(check_id=task, reason=f"malformed or failed LLM answer for {item or task} "
                                                                 f"after one retry ({last[:200]})"))
    return None
