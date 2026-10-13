"""Closeout receipts must point to a real project observation, not a promise."""
from pathlib import Path
import tempfile
import unittest
from test_visual_contracts import MODULE


class CloseoutTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.project = self.write('content-library/REXconstruction/PROJECT.md', '# Project\n')
        self.log = 'history/workflow-observations/rexconstruction.md'
        self.entry = '## 2026-10-13 — Width correction\n\n- Task reference: fixture repair\n- Actions: Removed parent cap\n- Verification: Width readback; runtime unavailable\n- Outcome: Partial\n'
        self.write(self.log, self.entry)
        self.receipt = 'Recorded — [entry](../../' + self.log + '#2026-10-13-width-correction)'

    def write(self, rel, text):
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return p

    def check(self, receipt, schema='1', source=None):
        status = ('- Closeout schema: ' + schema + '\n' if schema else '')
        if receipt is not None:
            status += '- Observation: ' + receipt + '\n'
        v = MODULE.Validator(self.root, {}, True)
        v.check_closeout(self.project, source or self.project, status)
        return [f.code for f in v.findings]

    def test_recorded_partial_result_is_valid(self):
        self.assertEqual(self.check(self.receipt), [])

    def test_missing_receipt_is_rejected(self):
        self.assertIn('closeout.receipt_missing', self.check(None))

    def test_promise_is_not_a_record(self):
        self.assertIn('closeout.receipt_missing', self.check('Will update later'))

    def test_missing_file_or_heading_is_rejected(self):
        for receipt in [self.receipt.replace('rexconstruction.md', 'missing.md'), self.receipt.replace('width-correction', 'missing')]:
            with self.subTest(receipt=receipt):
                self.assertIn('closeout.entry_missing', self.check(receipt))

    def test_whole_file_is_not_entry_evidence(self):
        self.assertIn('closeout.entry_missing', self.check(self.receipt.split('#')[0] + ')'))

    def test_other_project_is_rejected(self):
        self.write('history/workflow-observations/other.md', self.entry)
        self.assertIn('closeout.wrong_project', self.check(self.receipt.replace('rexconstruction.md', 'other.md')))

    def test_other_workspace_is_rejected(self):
        self.write('other-workspace/rexconstruction.md', self.entry)
        self.assertIn('closeout.wrong_project', self.check(self.receipt.replace(self.log, 'other-workspace/rexconstruction.md')))

    def test_empty_or_planned_entry_is_rejected(self):
        self.write(self.log, self.entry.replace('- Actions: Removed parent cap', '- Actions: TODO'))
        self.assertIn('closeout.entry_incomplete', self.check(self.receipt))

    def test_reasoned_na_and_actual_blocker_are_valid(self):
        for receipt in ['N/A — routine label typo correction', 'Blocked — repository write denied']:
            self.assertEqual(self.check(receipt), [])

    def test_unreasoned_na_is_rejected(self):
        self.assertIn('closeout.receipt_missing', self.check('N/A'))

    def test_schema_required_for_declared_receipt(self):
        self.assertIn('closeout.schema', self.check(self.receipt, schema=None))
        self.assertEqual(self.check(None, schema=None), [])

    def test_split_status_resolves_relative_to_actual_owner(self):
        status = self.write('content-library/REXconstruction/state/STATUS.md', '# Status\n')
        self.assertEqual(self.check(self.receipt.replace('../../', '../../../'), source=status), [])
