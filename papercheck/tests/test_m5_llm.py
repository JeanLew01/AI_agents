"""Milestone 5: LLM backend interface, stages 5-6 with a mocked backend, anti-hallucination rules."""

from __future__ import annotations

import json
import shutil
from types import SimpleNamespace

import pytest

from conftest import FIXTURES, VENUE, find, line_of, needs_tex, run_fixture
from papergate.config import load_config
from papergate.context import Options
from papergate.llm.anthropic_backend import AnthropicBackend
from papergate.llm.base import LLMError, MockBackend
from papergate.llm.verify import QuoteIndex
from papergate.pipeline import run_check

STMT = "Under Assumptions~\\ref{asm:lip} and~\\ref{asm:noise}, every plan accepted by the gate stays in"


def rigor_answer(quote=STMT, extra_hallucinated=True):
    issues = [{"category": "unused_assumption", "severity": "WARN", "file": "sec/method.tex", "line": 99,
               "quote": quote, "message": "Assumption asm:noise is listed but the proof never uses it.",
               "why_it_matters": "The theorem may hold under weaker assumptions, or the proof is incomplete."}]
    if extra_hallucinated:
        issues.append({"category": "missing_step", "severity": "WARN", "file": "sec/method.tex", "line": 12,
                       "quote": "By Assumption 3, the gate is convex", "message": "made up",
                       "why_it_matters": ""})
    return json.dumps({"theorem": "thm:main",
                       "dependencies": [{"kind": "assumption", "label": "asm:lip", "used_in_proof": True},
                                        {"kind": "assumption", "label": "asm:noise", "used_in_proof": False}],
                       "issues": issues})


def _run(fixture, llm, only, mode="camera-ready", rebuttal=None):
    return run_check(FIXTURES / fixture, load_config(VENUE), mode,
                     Options(only=only, rebuttal=FIXTURES / rebuttal if rebuttal else None), llm=llm,
                     venue_path=str(VENUE))


def test_quote_index_is_whitespace_insensitive_and_relocates():
    idx = QuoteIndex({"a.tex": "line one\nthe quick  brown\n  fox jumps\n", "b.tex": "other"})
    assert idx.find("quick brown fox", "a.tex", 50) == ("a.tex", 2)
    assert idx.find("quick brown fox", "b.tex", 1) == ("a.tex", 2)  # wrong file: found elsewhere
    assert idx.find("2| the quick brown", "a.tex", 2) == ("a.tex", 2)  # copied line prefix tolerated
    assert idx.find("slow brown fox", "a.tex", 2) is None


def test_unused_assumption_found_and_hallucination_discarded():
    llm = MockBackend({"math.rigor": rigor_answer()})
    led = _run("unused_assumption", llm, ["math"])
    f = find(led, "math.rigor")
    assert len(f) == 1 and f[0].source == "llm" and f[0].severity.value == "WARN"
    assert (f[0].location.file, f[0].location.line) == ("sec/method.tex", line_of("unused_assumption", "sec/method.tex", "Under Assumptions"))
    assert f[0].fix.kind == "manual" and f[0].fix.patch is None
    assert len(led.header.discarded_unverifiable) == 1
    assert "convex" in led.header.discarded_unverifiable[0].quote
    assert led.header.model == "mock-model"


def test_rigor_prompt_contains_only_dependency_context():
    llm = MockBackend({"math.rigor": rigor_answer(extra_hallucinated=False)})
    _run("unused_assumption", llm, ["math.rigor"])
    call = next(c for c in llm.calls if c["item"] == "thm:main")
    p = call["prompt"]
    assert "Assumption" in p and "asm:noise" in p and "The noise satisfies" in p  # referenced assumption text
    assert "proof" in p and "deviation of two trajectories" in p
    assert "Limitations" not in p and "Experiments" not in p and "hardware" not in p  # nothing else
    assert call["schema"]["required"] == ["theorem", "dependencies", "issues"]


def test_malformed_output_retried_once_then_dropped():
    good = rigor_answer(extra_hallucinated=False)
    llm = MockBackend({"math.rigor": ["not json at all", good]})
    led = _run("unused_assumption", llm, ["math.rigor"])
    assert len(find(led, "math.rigor")) == 1 and not led.header.discarded_unverifiable
    llm2 = MockBackend({"math.rigor": ["{broken", '{"theorem": 3}']})
    led2 = _run("unused_assumption", llm2, ["math.rigor"])
    assert not find(led2, "math.rigor")
    assert any("malformed" in d.reason for d in led2.header.discarded_unverifiable)
    assert len([c for c in llm2.calls if c["task"] == "math.rigor"]) == 2


def test_llm_stages_skipped_offline():
    led = run_fixture("unused_assumption")  # NullBackend / --no-llm
    skipped = {s.check_id for s in led.header.checks_skipped}
    assert {"math.rigor", "claims.support"} <= skipped
    assert led.header.model is None


def test_proof_presence_and_unreferenced_assumption(tmp_path):
    paper = tmp_path / "p"
    shutil.copytree(FIXTURES / "clean", paper)
    m = paper / "sec" / "method.tex"
    m.write_text(m.read_text() + "\n\\begin{lemma}\\label{lem:orphan}\nEvery gate is monotone.\n\\end{lemma}\n\n"
                 "\\begin{assumption}\\label{asm:unused}\nThe map is smooth.\n\\end{assumption}\n")
    led = run_check(paper, load_config(VENUE), "camera-ready", Options(no_llm=True, only=["math"]))
    pp = find(led, "math.proof_presence", "WARN")
    assert len(pp) == 1 and "lem:orphan" in pp[0].message
    au = find(led, "math.assumptions_unreferenced", "WARN")
    assert len(au) == 1 and "asm:unused" in au[0].message


@needs_tex
def test_rebuttal_commitments_offline():
    led = run_fixture("rebuttal_unfulfilled", rebuttal="rebuttal_unfulfilled.rebuttal.md")
    f = find(led, "rebuttal.commitments", "WARN")
    assert len(f) == 1 and "runtime comparison" in f[0].message
    assert f[0].location.line == 3 and f[0].location.file.endswith("rebuttal_unfulfilled.rebuttal.md")
    table = led.metrics["rebuttal_commitments"]
    assert [r["status"] for r in table] == ["not found", "likely addressed"]


@needs_tex
def test_clean_rebuttal_has_no_missing_commitment():
    led = run_fixture("clean", rebuttal="clean.rebuttal.md")
    assert not find(led, "rebuttal.commitments")


def test_rebuttal_commitments_with_llm():
    ext = json.dumps({"commitments": [
        {"quote": "We will add a runtime comparison with the MPC baseline to Section 4.", "line": 3,
         "target": "Section 4", "what": "runtime comparison with the MPC baseline"},
        {"quote": "We will add a discussion of hardware limitations to the Limitations section.", "line": 5,
         "target": "Limitations section", "what": "discussion of hardware limitations"},
        {"quote": "We promise a user study.", "line": 9, "target": "", "what": "user study"}]})
    j_missing = json.dumps({"status": "missing", "evidence": [], "message": "No runtime numbers are reported."})
    j_ok = json.dumps({"status": "fulfilled", "evidence": [{"file": "main.tex", "line": 88,
                       "quote": "we have not yet tested\nthe planner on hardware"}], "message": ""})
    llm = MockBackend({"rebuttal.commitments_llm:extract": ext, "rebuttal.commitments_llm:judge0": j_missing,
                       "rebuttal.commitments_llm:judge1": j_ok})
    led = _run("rebuttal_unfulfilled", llm, ["rebuttal"], rebuttal="rebuttal_unfulfilled.rebuttal.md")
    f = find(led, "rebuttal.commitments_llm")
    assert len(f) == 1 and "runtime" in f[0].message and f[0].location.line == 3
    assert not find(led, "rebuttal.commitments")  # deterministic variant defers to the LLM one
    assert any("user study" in d.quote for d in led.header.discarded_unverifiable)  # hallucinated commitment
    assert [r["status"] for r in led.metrics["rebuttal_commitments"]] == ["missing", "fulfilled"]


def test_claims_support_with_llm():
    ans = json.dumps({"claims": [
        {"quote": "a gate that certifies sampled plans with high probability", "file": "main.tex", "line": 41,
         "claim": "certification gate", "status": "supported", "evidence": ["thm:main"],
         "unbacked_strong_words": [], "message": ""},
        {"quote": "an evaluation on a cluttered navigation benchmark", "file": "main.tex", "line": 42,
         "claim": "evaluation", "status": "partially_supported", "evidence": ["tab:main"],
         "unbacked_strong_words": [], "message": "single benchmark"},
        {"quote": "GDP is the first certified diffusion planner", "file": "main.tex", "line": 1,
         "claim": "first", "status": "unsupported", "evidence": [], "unbacked_strong_words": ["first"],
         "message": ""}]})
    led = _run("clean", MockBackend({"claims.support": ans}), ["claims.support"])
    f = find(led, "claims.support")
    assert [x.severity.value for x in f] == ["INFO"] and "partially supported" in f[0].message
    assert len(led.header.discarded_unverifiable) == 1


def test_self_citation_llm_submission():
    ans = json.dumps({"items": [{"file": "sec/method.tex", "line": 3, "quote": "In our prior work~\\cite{campi2008exact}",
                                 "message": "first person"}]})
    led = _run("submission_leak", MockBackend({"identity.self_citation_llm": ans}), ["identity.self_citation_llm"],
               mode="submission")
    f = find(led, "identity.self_citation_llm")
    assert len(f) == 1 and f[0].location.line == line_of("submission_leak", "sec/method.tex", "In our prior work")


def test_llm_severity_is_capped(tmp_path):
    cfg_path = tmp_path / "v.yaml"
    cfg_path.write_text(f"extends: {VENUE}\nllm: {{max_severity: INFO}}\n")
    led = run_check(FIXTURES / "unused_assumption", load_config(cfg_path), "camera-ready", Options(only=["math.rigor"]),
                    llm=MockBackend({"math.rigor": rigor_answer(extra_hallucinated=False)}))
    assert find(led, "math.rigor")[0].severity.value == "INFO"


class _FakeMessages:
    def __init__(self, resp):
        self.resp, self.kwargs = resp, None

    def create(self, **kw):
        self.kwargs = kw
        return self.resp


def _fake_client(text="{}", stop="end_turn"):
    resp = SimpleNamespace(stop_reason=stop, stop_details=SimpleNamespace(category="cyber"),
                           content=[SimpleNamespace(type="thinking", thinking=""), SimpleNamespace(type="text", text=text)])
    msgs = _FakeMessages(resp)
    return SimpleNamespace(beta=SimpleNamespace(messages=msgs), messages=msgs), msgs


def test_anthropic_backend_request_shape_and_refusal():
    client, msgs = _fake_client('{"ok": true}')
    b = AnthropicBackend(model="claude-opus-5-5", client=client)
    schema = {"type": "object", "properties": {}, "additionalProperties": False}
    assert b.complete("sys", "prompt", task="t", schema=schema) == '{"ok": true}'
    kw = msgs.kwargs
    assert kw["model"] == "claude-opus-5-5" and kw["system"] == "sys"
    assert kw["output_config"] == {"effort": "high", "format": {"type": "json_schema", "schema": schema}}
    assert kw["fallbacks"] == "default" and kw["betas"] == ["server-side-fallback-2026-07-01"]
    refused, _ = _fake_client(stop="refusal")
    with pytest.raises(LLMError, match="refused"):
        AnthropicBackend(client=refused).complete("s", "p", task="t")
    trunc, _ = _fake_client(stop="max_tokens")
    with pytest.raises(LLMError, match="truncated"):
        AnthropicBackend(client=trunc).complete("s", "p", task="t")
