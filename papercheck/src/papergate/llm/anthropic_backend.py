"""Anthropic API backend (optional dependency: pip install 'papergate[llm]'). Network access happens
only here, and only when an LLM stage runs (never with --no-llm)."""

from __future__ import annotations

import os
from pathlib import Path

from .base import LLMBackend, LLMError


def credentials_present() -> bool:
    if os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("ANTHROPIC_AUTH_TOKEN") or os.environ.get("ANTHROPIC_PROFILE"):
        return True
    return (Path.home() / ".config" / "anthropic").is_dir()


class AnthropicBackend(LLMBackend):
    def __init__(self, model: str = "claude-opus-5-5", max_tokens: int = 16000, effort: str = "high",
                 client=None, fallbacks: bool = True):
        self.model_name = model
        self.max_tokens = max_tokens
        self.effort = effort
        self.fallbacks = fallbacks
        self._client = client
        self.available = client is not None or credentials_present()

    @property
    def client(self):
        if self._client is None:
            import anthropic

            self._client = anthropic.Anthropic()
        return self._client

    def complete(self, system: str, prompt: str, *, task: str, item: str = "", schema: dict | None = None) -> str:
        import anthropic

        output_config: dict = {"effort": self.effort}
        if schema is not None:
            output_config["format"] = {"type": "json_schema", "schema": schema}
        kwargs = dict(model=self.model_name, max_tokens=self.max_tokens, system=system,
                      messages=[{"role": "user", "content": prompt}], output_config=output_config)
        try:
            if self.fallbacks:
                # On a safety-classifier refusal the API re-runs the request on a fallback model.
                resp = self.client.beta.messages.create(betas=["server-side-fallback-2026-07-01"],
                                                        fallbacks="default", **kwargs)
            else:
                resp = self.client.messages.create(**kwargs)
        except anthropic.BadRequestError as e:
            raise LLMError(f"bad request: {e.message}") from e
        except anthropic.AuthenticationError as e:
            raise LLMError("authentication failed (set ANTHROPIC_API_KEY or run `ant auth login`)") from e
        except anthropic.RateLimitError as e:
            raise LLMError("rate limited (after SDK retries)") from e
        except anthropic.APIStatusError as e:
            raise LLMError(f"API error {e.status_code}: {e.message}") from e
        except anthropic.APIConnectionError as e:
            raise LLMError(f"connection error: {e}") from e
        if resp.stop_reason == "refusal":
            cat = getattr(getattr(resp, "stop_details", None), "category", None)
            raise LLMError(f"model refused (category {cat})")
        if resp.stop_reason == "max_tokens":
            raise LLMError("answer truncated at max_tokens")
        text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
        if not text.strip():
            raise LLMError("empty answer")
        return text
