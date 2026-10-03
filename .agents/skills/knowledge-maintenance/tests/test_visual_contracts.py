#!/usr/bin/env python3
"""Regression tests for the persisted Visual Direction Contract validator."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


VALIDATOR_PATH = Path(__file__).parents[1] / "scripts" / "validate_repository.py"
SPEC = importlib.util.spec_from_file_location("website_lab_validator", VALIDATOR_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load validator from {VALIDATOR_PATH}")
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


CONCERNS = (
    "Design Read",
    "Preserve",
    "Transform",
    "Avoid",
    "Sibling-page delta",
    "Section composition",
    "Colour rhythm",
    "Asset map",
    "Responsive transformation",
    "Completion evidence",
)


def contract_text(
    status: str = "Ready",
    *,
    drop: str | None = None,
    overrides: dict[str, list[str]] | None = None,
) -> str:
    rows: list[str] = []
    overrides = overrides or {}
    for concern in CONCERNS:
        if concern == drop:
            continue
        cells = overrides.get(
            concern,
            [
                concern,
                f"Specific decision for {concern}.",
                "Page owner",
                "PROJECT.md#visual-direction",
                "Named readback evidence.",
                "Named visual evidence.",
            ],
        )
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join(
        [
            "# Request",
            "",
            "## Visual Direction Contract",
            "",
            f"Contract status: {status}",
            "",
            "| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |",
            "|---|---|---|---|---|---|",
            *rows,
            "",
        ]
    )


class VisualContractValidationTests(unittest.TestCase):
    def validate_contract(self, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            checklist = root / "content-library" / "fixture" / "checklist"
            checklist.mkdir(parents=True)
            (checklist / "request.md").write_text(text, encoding="utf-8")
            (checklist / "PROJECT.md").write_text("# Fixture\n## Visual direction\n## Asset usage ledger\n", encoding="utf-8")
            (checklist / "preflight-audit.md").write_text("# QA\n## Visual composition\n", encoding="utf-8")
            validator = MODULE.Validator(root, {"inactive_text_globs": []}, strict=True)
            validator.check_visual_contracts()
            return [finding.code for finding in validator.findings]

    def test_valid_ready_contract_passes(self) -> None:
        self.assertEqual(self.validate_contract(contract_text()), [])

    def test_missing_sibling_delta_fails(self) -> None:
        codes = self.validate_contract(contract_text(drop="Sibling-page delta"))
        self.assertIn("visual_contract.concern_missing", codes)

    def test_missing_asset_reuse_decision_fails(self) -> None:
        cells = [
            "Asset map",
            "",
            "Page image owner",
            "PROJECT.md#asset-usage-ledger",
            "Named readback evidence.",
            "Named visual evidence.",
        ]
        codes = self.validate_contract(contract_text(overrides={"Asset map": cells}))
        self.assertIn("visual_contract.empty_cell", codes)

    def test_false_visual_pass_fails(self) -> None:
        cells = [
            "Completion evidence",
            "Require structural and visual evidence.",
            "QA",
            "preflight-audit.md#visual-composition",
            "Structural proof complete.",
            "Planned full-page review.",
        ]
        codes = self.validate_contract(contract_text("Pass", overrides={"Completion evidence": cells}))
        self.assertIn("visual_contract.unproven_pass", codes)


if __name__ == "__main__":
    unittest.main()
