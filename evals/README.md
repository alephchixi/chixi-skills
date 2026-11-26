# Evaluating the Ch’ixi Skills

```sh
python3 evals/run_evals.py
python3 evals/run_evals.py --case taypi-01 --case soul-01 --prepare
python3 evals/run_evals.py --case image-01 --review answers.json
```

Inspection lists prepared cases. Preparation emits agent inputs, including case ID, skill, degree when specified, language, modality, the selection intent and earlier turns when available. The evaluator can read the rubric in `evals.json`. The agent should receive the task only. The route cases measure whether the agent honors a nearby request that needs a different operation. The imported `evaluate(cases, agent, judge)` function supports a host adapter and any reviewer that implements the documented result fields.

To review an existing response without a provider, save a JSON object keyed by case ID. Use a boolean for a reviewed answer and add an evidence-linked reason. A null judgment or missing response is unevaluated.

```json
{
  "image-01": {
    "response": "The description establishes where the vendors sit in the frame. I cannot determine the camera angle.",
    "pass": true,
    "reason": "The response locates its observation in the description and leaves the angle open."
  }
}
```

Review exits 0 when all selected records pass, 1 if any fail, and 2 if any remain unevaluated or the supplied file cannot be read. Inspection and preparation exit 0 on a valid selection.

## Running a comparison

In a scratch project, record the host, version, model, exact instructions and any source files. Check discovery by the skill’s name, reading the whole `taypi` reference, repeating installation, and exiting the sustained mode. For a blind comparison, give the same task to a baseline and an installed skill, hide which is which, alternate their order and have a reviewer record a reason or dissent against the case rubric. Pair `ct-01` with `ct-03` for an order-and-preference check. An image comparison should start with an image the project has permission to use and then repeat the case with its caption alone.

## Verified host sample

On 26 November 2026, a scratch project loaded the collection in Claude Code 2.1.332 with Claude Haiku 5.5. Repeating installation preserved eight folders and the `taypi` resource. The installed skill returned the documented pair and the locator on p. 247. A resumed session turned off `agentic-tension` and answered the subsequent calculation directly. The result speaks to this host and version. The remaining paths in the main README come from host documentation.
