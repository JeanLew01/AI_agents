"""Pluggable LLM backend interface."""

from __future__ import annotations

from abc import ABC, abstractmethod


class LLMError(Exception):
    pass


class LLMBackend(ABC):
    model_name: str | None = None
    available: bool = True

    @abstractmethod
    def complete(self, system: str, prompt: str, *, task: str, item: str = "", schema: dict | None = None) -> str:
        """Return the model's raw text answer (expected to be one JSON object).
        `task`/`item` identify the request (e.g. task="math.rigor", item="thm:main") so test doubles
        can replay canned answers; `schema` is the JSON schema the answer must follow."""


class NullBackend(LLMBackend):
    """No model: LLM-assisted checks are skipped and listed as such in the report."""

    model_name = None
    available = False

    def complete(self, system: str, prompt: str, *, task: str, item: str = "", schema: dict | None = None) -> str:
        raise LLMError("NullBackend has no model")


class MockBackend(LLMBackend):
    """Replays canned answers. responses maps "task" or "task:item" to a string, a list of strings
    (consumed one per call, e.g. malformed then valid) or a callable(prompt) -> str."""

    def __init__(self, responses: dict, model_name: str = "mock-model"):
        self.responses = {k: (list(v) if isinstance(v, list) else v) for k, v in responses.items()}
        self.model_name = model_name
        self.calls: list[dict] = []

    def complete(self, system: str, prompt: str, *, task: str, item: str = "", schema: dict | None = None) -> str:
        self.calls.append({"task": task, "item": item, "system": system, "prompt": prompt, "schema": schema})
        for key in (f"{task}:{item}", task):
            if key in self.responses:
                v = self.responses[key]
                if isinstance(v, list):
                    if not v:
                        raise LLMError(f"mock has no more answers for {key}")
                    return v.pop(0) if len(v) > 1 else v[0]
                return v(prompt) if callable(v) else v
        raise LLMError(f"mock has no answer for {task}:{item}")
