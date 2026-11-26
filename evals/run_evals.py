#!/usr/bin/env python3
"""Inspect Ch’ixi cases or review saved answers with explicitly supplied verdicts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVALS_PATH = HERE / "evals.json"
JUDGE_SYSTEM_PROMPT = (
    "Judge the answer using only the case-specific rubric, the public input and the response. "
    "Accept different conclusions when the evidence and task allow them. "
    "Record a decision with a reason tied to the response. Mark it undetermined if evidence is missing."
)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def public_case(case):
    """Pass the full task to an agent adapter while withholding its rubric."""
    return {key: value for key, value in case.items() if key != "expected_behavior"}


def evaluate(cases, agent, judge):
    """Adapter API. An empty answer does not reach the judge."""
    for case in cases:
        task = public_case(case)
        answer = agent(task)
        if isinstance(answer, str) and answer.strip():
            verdict = judge(task, answer, case["expected_behavior"])
        else:
            verdict = {"pass": None, "reason": "No response supplied"}
        yield {"id": case["id"], **verdict}


def review(case, archive):
    record = archive.get(case["id"], {})
    if not isinstance(record, dict):
        raise ValueError(f'{case["id"]}: expected an object')
    response = record.get("response")
    if not isinstance(response, str) or not response.strip():
        return {"pass": None, "reason": "No response supplied"}
    verdict = record.get("pass")
    if verdict is not None and type(verdict) is not bool:
        raise ValueError(f'{case["id"]}: pass must be true, false or null')
    reason = record.get("reason")
    if verdict is not None and (not isinstance(reason, str) or not reason.strip()):
        raise ValueError(f'{case["id"]}: an evaluated response requires a reason')
    return {"pass": verdict, "reason": reason or "Awaiting review"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", action="append", default=[], metavar="ID")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--prepare", action="store_true", help="Emit agent inputs as JSON")
    modes.add_argument("--review", type=Path, metavar="FILE", help="Read answers and supplied verdicts")
    args = parser.parse_args()
    cases = read_json(EVALS_PATH)["evals"]
    if args.case:
        selected = set(args.case)
        unknown = selected.difference(case["id"] for case in cases)
        if unknown:
            parser.error(f"Unknown case IDs: {', '.join(sorted(unknown))}")
        cases = [case for case in cases if case["id"] in selected]

    if args.prepare:
        print(json.dumps([public_case(case) for case in cases], ensure_ascii=False, indent=2))
        return 0
    if args.review is None:
        for case in cases:
            print(f'{case["id"]:<22} PREPARED   {case["skill"]}')
        print(f"{len(cases)} prepared, 0 evaluated")
        return 0

    try:
        archive = read_json(args.review)
        if not isinstance(archive, dict):
            raise ValueError("Expected an object keyed by case ID")
        reviewed = [(case, review(case, archive)) for case in cases]
    except (ValueError, OSError) as exc:
        parser.exit(2, f"{exc}\n")

    counts = dict(PASS=0, FAIL=0, SKIP=0)
    for case, result in reviewed:
        status = {True: "PASS", False: "FAIL", None: "SKIP"}[result["pass"]]
        counts[status] += 1
        print(f'{case["id"]:<22} {status:<4} {result["reason"]}')
    print(f'{counts["PASS"]} passed, {counts["FAIL"]} failed, {counts["SKIP"]} unevaluated')
    if counts["FAIL"]:
        return 1
    return 2 if counts["SKIP"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
