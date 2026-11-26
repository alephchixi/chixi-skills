"""Regression checks for complete handoff, review status and installed resources."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "evals" / "run_evals.py"


def run(path, *args):
    return subprocess.run(
        [sys.executable, str(path), *map(str, args)], capture_output=True, text=True, check=False
    )


class EvalToolsTest(unittest.TestCase):
    def test_prepare_sends_degree_and_history_without_rubrics(self):
        result = run(RUNNER, "--case", "taypi-01", "--case", "soul-01", "--prepare")
        self.assertEqual(result.returncode, 0, result.stderr)
        taypi, soul = json.loads(result.stdout)
        self.assertEqual((taypi["skill"], taypi["grade"]), ("taypi", 3))
        self.assertEqual(soul["context"][0]["role"], "assistant")
        self.assertNotIn("expected_behavior", taypi)

    def test_all_skipped_review_does_not_pass(self):
        with tempfile.TemporaryDirectory() as scratch:
            archive = Path(scratch) / "answers.json"
            archive.write_text("{}")
            result = run(RUNNER, "--case", "image-01", "--review", archive)
            self.assertEqual(result.returncode, 2, result.stderr)
            self.assertIn("1 unevaluated", result.stdout)
            archive.write_text(json.dumps({"image-01": {
                "response": "The caption does not specify the angle.",
                "pass": True,
                "reason": "Separates the description from the unknown camera position."
            }}))
            self.assertEqual(run(RUNNER, "--case", "image-01", "--review", archive).returncode, 0)

    def test_adapter_gets_case_without_rubric_and_does_not_grade_empty_answer(self):
        spec = importlib.util.spec_from_file_location("chixi_evals", RUNNER)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        case = next(row for row in module.read_json(module.EVALS_PATH)["evals"] if row["id"] == "taypi-01")

        def subject(task):
            self.assertEqual(task["grade"], 3)
            self.assertNotIn("expected_behavior", task)
            return ""

        def judge(*args):
            self.fail("An empty response should not reach the judge")

        result = list(module.evaluate([case], subject, judge))
        self.assertIsNone(result[0]["pass"])

    def test_repeat_install_preserves_reference_and_local_changes(self):
        with tempfile.TemporaryDirectory() as scratch:
            target = Path(scratch) / ".claude" / "skills"
            installer = ROOT / "install_skills.py"
            for _ in range(2):
                result = run(installer, target)
                self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(len(list(target.glob("*/SKILL.md"))), 8)
            resource = target / "taypi" / "references" / "heteronyms.md"
            reference = ROOT / "skills" / "taypi" / "references" / "heteronyms.md"
            self.assertEqual(resource.read_bytes(), reference.read_bytes())
            resource.write_text("Local annotation")
            result = run(installer, target)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertEqual(resource.read_text(), "Local annotation")


if __name__ == "__main__":
    unittest.main()
