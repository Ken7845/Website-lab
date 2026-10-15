"""Behavioral regressions for routing, state ownership and completion evidence."""
from pathlib import Path
import hashlib
import tempfile
import unittest
from test_visual_contracts import MODULE

class KnowledgeRegressionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.config = {"inactive_text_globs": []}

    def write(self, name, text):
        p = self.root / name
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
        return p

    def check(self, *methods):
        v = MODULE.Validator(self.root, self.config, True)
        for name in methods:
            getattr(v, name)()
        return [x.code for x in v.findings]

    def contract(self, kind="Component", status="Pass", proof="Pass — observed; [record](#evidence)", level="##", implementation="Implemented"):
        headers = getattr(MODULE, kind.upper()+"_CONTRACT_HEADERS")
        concerns = getattr(MODULE, kind.upper()+"_CONTRACT_CONCERNS")
        title = "Component Requirement Contract" if kind == "Component" else "Visual Direction Contract"
        rows = ["| " + " | ".join([c, "Scoped decision", "Definition", "rules.md#ownership", proof, proof]) + " |" for c in concerns]
        text = "# Request\n- Contract schema: 1\n- Component contract: " + ("Required" if kind == "Component" else "N/A — visual-only work.") + "\n- Visual contract: " + ("Required" if kind == "Visual" else "N/A — ownership-only work.") + "\n\n" + level + " " + title + "\nContract status: " + status + "\nImplementation status: " + implementation + "\nVerification status: " + ("Not run" if status == "Ready" else status) + "\n| " + " | ".join(headers) + " |\n|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n\n## Evidence\nRecorded 2026-10-03 targeted readback of fixture ownership, all scoped states observed.\n"
        self.write("content-library/fixture/checklist/rules.md", "# Rules\n## Ownership\n")
        return text

    def request(self, text):
        return self.write("content-library/fixture/checklist/request.md", text)

    def test_inline_missing_rule_is_rejected(self):
        self.write("AGENTS.md", "Follow `framer/missing.md#scope`.\n")
        self.assertIn("route.inline.missing_source", self.check("check_inline_routes"))

    def test_inline_existing_rule_and_anchor_are_accepted(self):
        self.write("AGENTS.md", "Follow `framer/rules.md#scope`.\n")
        self.write("framer/rules.md", "## Scope\n")
        self.assertEqual(self.check("check_inline_routes"), [])

    def test_examples_do_not_become_rules_or_anchors(self):
        self.write("AGENTS.md", "```markdown\nFollow `framer/missing.md#scope`.\n## Fake heading\n```\n")
        v = MODULE.Validator(self.root, self.config, True)
        v.check_inline_routes()
        self.assertEqual(v.findings, [])
        self.assertNotIn("fake-heading", v.heading_anchors(self.root/"AGENTS.md"))

    def test_declared_required_contract_cannot_be_absent(self):
        self.request("# Request\n- Contract schema: 1\n- Component contract: Required\n- Visual contract: N/A — link repair.\n")
        self.assertIn("component_contract.required_missing", self.check("check_contract_applicability"))

    def test_reasoned_mechanical_nonapplicability_is_valid(self):
        self.request("# Request\n- Contract schema: 1\n- Component contract: N/A — existing label repair.\n- Visual contract: N/A — no visual change.\n")
        self.assertEqual(self.check("check_contract_applicability"), [])

    def test_fenced_contract_does_not_satisfy_required_declaration(self):
        self.request("- Contract schema: 1\n- Component contract: Required\n- Visual contract: N/A — no visual change.\n```markdown\n## Component Requirement Contract\n```\n")
        self.assertIn("component_contract.required_missing", self.check("check_contract_applicability"))

    def test_typo_in_required_flag_is_rejected(self):
        self.request("- Contract schema: 1\n- Component contract: Required-ish\n- Visual contract: N/A — no visual change.\n")
        self.assertIn("component_contract.applicability", self.check("check_contract_applicability"))

    def test_undated_legacy_exception_is_rejected(self):
        self.request("- Contract schema: 1\n- Component contract: Legacy — old build\n- Visual contract: N/A — no visual change.\n")
        self.assertIn("component_contract.applicability", self.check("check_contract_applicability"))

    def test_numbered_component_false_pass_is_rejected(self):
        self.request(self.contract(proof="Pass — not run; [record](#evidence)", level="### 3."))
        self.assertIn("component_contract.unproven_pass", self.check("check_component_contracts"))

    def test_numbered_visual_contract_is_validated(self):
        self.request(self.contract(kind="Visual", proof="Pass — planned review; [record](#evidence)", level="### 4."))
        self.assertIn("visual_contract.unproven_pass", self.check("check_visual_contracts"))

    def test_linked_completed_component_is_valid(self):
        self.request(self.contract())
        self.assertEqual(self.check("check_contract_applicability", "check_component_contracts"), [])

    def test_linked_completed_visual_is_valid(self):
        self.request(self.contract(kind="Visual"))
        self.assertEqual(self.check("check_contract_applicability", "check_visual_contracts"), [])

    def test_named_blocker_is_valid_and_never_a_pass(self):
        self.request(self.contract(status="Blocked", proof="Blocked — runtime unavailable."))
        self.assertEqual(self.check("check_component_contracts"), [])

    def test_success_word_without_evidence_record_is_rejected(self):
        self.request(self.contract(proof="Pass — looks good."))
        self.assertIn("component_contract.evidence_missing", self.check("check_component_contracts"))

    def test_missing_evidence_anchor_is_rejected(self):
        self.request(self.contract(proof="Pass — observed; [record](#missing)"))
        self.assertIn("component_contract.evidence.missing_anchor", self.check("check_component_contracts"))

    def test_pass_cannot_include_blocked_row(self):
        self.request(self.contract(proof="Blocked — runtime unavailable."))
        self.assertIn("component_contract.unproven_pass", self.check("check_component_contracts"))

    def test_implemented_contract_cannot_stay_ready(self):
        self.request(self.contract(status="Ready", proof="Planned readback."))
        self.assertIn("component_contract.stale_ready", self.check("check_component_contracts"))

    def test_not_started_ready_contract_is_valid(self):
        self.request(self.contract(status="Ready", proof="Planned readback.", implementation="Not started"))
        self.assertEqual(self.check("check_component_contracts"), [])

    def test_nonexistent_governing_heading_is_rejected(self):
        self.request(self.contract().replace("rules.md#ownership", "rules.md#fake"))
        self.assertIn("component_contract.missing_anchor", self.check("check_component_contracts"))

    def test_not_started_implementation_cannot_claim_pass(self):
        self.request(self.contract(implementation="Not started"))
        self.assertIn("component_contract.incomplete_pass", self.check("check_component_contracts"))

    def test_partial_implementation_cannot_claim_complete_pass(self):
        self.request(self.contract(implementation="Partial"))
        self.assertIn("component_contract.incomplete_pass", self.check("check_component_contracts"))

    def test_ready_status_cannot_claim_verified_result(self):
        self.request(self.contract(status="Ready", implementation="Not started").replace("Verification status: Not run", "Verification status: Pass"))
        self.assertIn("component_contract.preparation_verification", self.check("check_component_contracts"))

    def state(self, revision="2026-10-03", active="one.md", reference="STATUS.md", inline=False):
        self.write("content-library/fixture/one.md", "# One\n")
        self.write("content-library/fixture/two.md", "# Two\n")
        status = "- State revision: 2026-10-03\n- Active request: [Part](one.md)\n"
        recovery = "- State revision: " + revision + "\n- Active request: [Part]("+active+")\n- State reference: [State]("+reference+")\n"
        if inline:
            self.write("content-library/fixture/PROJECT.md", "- State schema: 1\n- Current status owner: [Status](#status)\n- Recovery owner: [Recovery](#recovery)\n## Status\n"+status+"## Recovery\n"+recovery)
        else:
            self.write("content-library/fixture/PROJECT.md", "- State schema: 1\n- Current status owner: [Status](STATUS.md)\n- Recovery owner: [Recovery](RECOVERY.md)\n")
            self.write("content-library/fixture/STATUS.md", status)
            self.write("content-library/fixture/RECOVERY.md", recovery)

    def test_consistent_split_state_is_valid(self):
        self.state()
        self.assertEqual(self.check("check_current_state"), [])

    def test_consistent_inline_state_is_valid(self):
        self.state(reference="#status", inline=True)
        self.assertEqual(self.check("check_current_state"), [])

    def test_older_recovery_revision_is_rejected(self):
        self.state(revision="2026-09-03")
        self.assertIn("state.stale_recovery", self.check("check_current_state"))

    def test_competing_active_requests_are_rejected(self):
        self.state(active="two.md")
        self.assertIn("state.active_request_conflict", self.check("check_current_state"))

    def test_recovery_cannot_point_to_a_second_truth(self):
        self.state(reference="one.md")
        self.assertIn("state.reference_conflict", self.check("check_current_state"))

    def test_new_broad_checklist_exclusion_is_rejected(self):
        self.request("# Active request\n")
        self.config["inactive_text_globs"] = ["content-library/*/checklist/**"]
        self.assertIn("policy.broad_exclusion", self.check("check_policy"))

    def test_local_only_project_files_are_not_repository_validation_input(self):
        project = self.write("content-library/fixture/PROJECT.md", "# Local project\n")
        guide = self.write("content-library/README.md", "# Tracked guide\n")
        self.config["local_only_path_globs"] = ["content-library/*/**"]
        v = MODULE.Validator(self.root, self.config, True)
        self.assertNotIn(project, v.markdown_files())
        self.assertIn(guide, v.markdown_files())
        self.assertEqual([x.code for x in v.findings], [])

    def test_local_only_scope_cannot_hide_tracked_content_entrypoints(self):
        self.config["local_only_path_globs"] = ["content-library/**"]
        self.assertIn("policy.local_only_scope", self.check("check_policy"))

    def test_missing_local_only_link_is_preserved_without_becoming_a_broken_repository_link(self):
        self.write("README.md", "[Local evidence](content-library/private/PROJECT.md)\n")
        self.config["local_only_path_globs"] = ["content-library/*/**"]
        v = MODULE.Validator(self.root, self.config, True)
        v.check_markdown_links()
        self.assertEqual(v.findings, [])

    def test_hash_protected_exact_archive_skip_is_valid(self):
        p = self.write("history/snapshot.md", "# Exact old record\n")
        self.config.update(skip_markdown_link_globs=["history/snapshot.md"], immutable_archives={"history/snapshot.md": hashlib.sha256(p.read_bytes()).hexdigest()})
        self.assertEqual(self.check("check_policy", "check_archives"), [])

    def test_changed_archive_cannot_hide_behind_skip(self):
        p = self.write("history/snapshot.md", "# Old\n")
        self.config.update(skip_markdown_link_globs=["history/snapshot.md"], immutable_archives={"history/snapshot.md": hashlib.sha256(p.read_bytes()).hexdigest()})
        p.write_text("# Changed\n")
        self.assertIn("archive.hash_mismatch", self.check("check_archives"))

    def test_route_traversal_does_not_read_binary_assets(self):
        self.write("AGENTS.md", "[router](framer/README.md)\n")
        self.write("framer/README.md", "[asset](sample.png)\n")
        (self.root/"framer/sample.png").write_bytes(b"\xff\xfe\x00")
        v = MODULE.Validator(self.root, self.config, True)
        self.assertEqual(v.reachable_markdown("AGENTS.md"), {"AGENTS.md", "framer/README.md"})
        self.assertEqual(v.findings, [])
