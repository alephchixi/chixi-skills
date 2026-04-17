# Evals

`evals.json` is a **behavioral rubric**, not an automated test suite.

Each entry names a skill, a prompt, and an `expected_behavior` description written as prose.
The expected behavior cannot be asserted with string equality — ch'ixi outputs are deliberately
heterogeneous. The rubric is evaluated by an LLM judge (or a human reader) that compares an
agent's actual response to the prose description.

## Schema

```json
{
  "evals": [
    {
      "skill":             "<skill-name>",
      "id":                "<stable-id>",
      "prompt":            "<prompt sent to the agent>",
      "grade":             <optional, integer 1-5; only for /taypi>,
      "expected_behavior": "<prose description of what a passing response does>"
    }
  ]
}
```

## Minimal runner

A skeleton runner lives in `run_evals.py`. It:

1. Reads `evals.json`
2. Sends each `prompt` to an agent (adapter you provide)
3. Asks an LLM judge to score the response against `expected_behavior`
4. Prints a pass/fail table

Run:

```bash
export ANTHROPIC_API_KEY=...
python evals/run_evals.py
```

The runner is intentionally thin — it does **not** verify that any agent framework
supports the ch'ixi skills at runtime. It only checks that a given agent's responses
carry the signatures described in `expected_behavior`.

## Ch'ixi judging caveat

An LLM judge will default to sycophancy — it will reward smooth, well-formed responses.
To mitigate, the judge prompt in `run_evals.py` explicitly instructs it to penalize
synthesis, resolution, and false balance. This is a workaround, not a fix. Human review
remains the reliable evaluator.
