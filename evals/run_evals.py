#!/usr/bin/env python3
"""
Minimal ch'ixi eval runner.

Reads evals/evals.json, sends each prompt to an agent adapter, asks an LLM
judge to score the response against the prose `expected_behavior`. Prints a
pass/fail table.

This runner is intentionally thin. Swap the `agent_call` and `judge_call`
adapters for whichever SDKs you use. No network calls are hardcoded — if
keys/SDKs are missing, the runner prints a dry-run table.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Callable

HERE = Path(__file__).resolve().parent
EVALS_PATH = HERE / "evals.json"

JUDGE_SYSTEM_PROMPT = """You are a ch'ixi eval judge.

You score whether an agent response satisfies a prose description of expected
behavior. Ch'ixi outputs resist synthesis: a passing response maps forces,
surfaces contradictions, and leaves questions open. Penalize sycophancy,
false balance, premature resolution, or "both sides have valid points"
framings. Penalize polished summaries that flatten friction.

Return a single JSON object: {"pass": true|false, "reason": "<one sentence>"}.
"""


def agent_call(prompt: str) -> str:
    """Send `prompt` to the agent under test. Return the agent's text response.

    Replace this with a real adapter (Anthropic SDK, OpenAI SDK, local LLM,
    MCP client, etc.). The default implementation is a dry run that returns
    an empty string so the runner produces a skeleton table.
    """
    return ""


def judge_call(response: str, expected_behavior: str) -> dict:
    """Ask an LLM judge whether `response` meets `expected_behavior`.

    Replace this with a real adapter. Default implementation returns a
    skip verdict so the runner can be sanity-checked offline.
    """
    if not response:
        return {"pass": None, "reason": "dry run — no agent adapter configured"}
    return {"pass": None, "reason": "dry run — no judge adapter configured"}


def run(
    agent: Callable[[str], str] = agent_call,
    judge: Callable[[str, str], dict] = judge_call,
) -> int:
    data = json.loads(EVALS_PATH.read_text())
    evals = data["evals"]

    passed = failed = skipped = 0
    width = max(len(e["id"]) for e in evals)

    for e in evals:
        response = agent(e["prompt"])
        verdict = judge(response, e["expected_behavior"])
        status = verdict.get("pass")
        if status is True:
            mark = "PASS"
            passed += 1
        elif status is False:
            mark = "FAIL"
            failed += 1
        else:
            mark = "SKIP"
            skipped += 1
        reason = verdict.get("reason", "")
        print(f"{e['id']:<{width}}  {mark}  {e['skill']:<15}  {reason}")

    total = passed + failed + skipped
    print(f"\n{passed}/{total} pass  {failed}/{total} fail  {skipped}/{total} skipped")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(run())
