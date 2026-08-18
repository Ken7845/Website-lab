#!/usr/bin/env python3
"""Validate Website-lab's progressive-disclosure knowledge architecture.

Uses only the Python standard library so it can run in a fresh local workspace.
"""

from __future__ import annotations

import argparse
import dataclasses
import fnmatch
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote


LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_ROOT_FILES = (
    "AGENTS.md",
    "README.md",
    "content-library/README.md",
    "content-library/project-manifest-template.md",
    "framer/README.md",
    "framer/basic/README.md",
    "framer/advance-design/README.md",
    "framer/checklist.md",
)
COMPONENT_CONTRACT_HEADING = "## Component Requirement Contract"
COMPONENT_CONTRACT_HEADERS = (
    "Concern",
    "Decision / N/A reason",
    "Owner",
    "Governing source",
    "Readback proof",
    "Preview proof",
)
COMPONENT_CONTRACT_CONCERNS = (
    "Section background / vertical rhythm",
    "Available width / placement",
    "Visible boundary / border / surface",
    "Internal padding / hit area",
    "Readable max-width",
    "Editable content / Properties",
    "States / routes",
    "Breakpoint contract",
    "Accessibility / touch / focus",
    "Evidence sample",
)


@dataclasses.dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str


class Validator:
    def __init__(self, root: Path, config: dict, strict: bool) -> None:
        self.root = root
        self.config = config
        self.strict = strict
        self.findings: list[Finding] = []
        self._markdown_files: list[Path] | None = None
        self._heading_cache: dict[Path, set[str]] = {}

    def add(self, severity: str, code: str, path: str | Path, message: str) -> None:
        if isinstance(path, Path):
            try:
                path = path.resolve().relative_to(self.root).as_posix()
            except ValueError:
                path = path.as_posix()
        self.findings.append(Finding(severity, code, str(path), message))

    def error(self, code: str, path: str | Path, message: str) -> None:
        self.add("error", code, path, message)

    def warning(self, code: str, path: str | Path, message: str) -> None:
        self.add("warning", code, path, message)

    def note(self, code: str, path: str | Path, message: str) -> None:
        self.add("note", code, path, message)

    def rel(self, path: Path) -> str:
        return path.resolve().relative_to(self.root).as_posix()

    def matches(self, rel_path: str, config_key: str) -> bool:
        return any(
            fnmatch.fnmatchcase(rel_path, pattern)
            for pattern in self.config.get(config_key, [])
        )

    def markdown_files(self) -> list[Path]:
        if self._markdown_files is None:
            self._markdown_files = sorted(
                path
                for path in self.root.rglob("*.md")
                if ".git" not in path.parts
            )
        return self._markdown_files

    def read_text(self, path: Path) -> str:
        try:
            return path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            self.error("file.read", path, f"Cannot read UTF-8 text: {exc}")
            return ""

    def run_git(self, *args: str) -> subprocess.CompletedProcess[bytes]:
        return subprocess.run(
            ["git", *args],
            cwd=self.root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def check_entrypoints(self) -> None:
        for rel_path in REQUIRED_ROOT_FILES:
            path = self.root / rel_path
            if not path.is_file():
                self.error("entrypoint.missing", rel_path, "Required repository entry point is missing.")

        if (self.root / "SKILL.md").exists():
            self.error(
                "entrypoint.duplicate_root_skill",
                "SKILL.md",
                "Root SKILL.md would recreate a parallel always-on design system.",
            )
        if (self.root / "skills" / "taste-skill").exists():
            self.error(
                "entrypoint.legacy_taste_skill",
                "skills/taste-skill",
                "Legacy taste-skill directory must not return as an active system.",
            )

        agents = self.root / "AGENTS.md"
        if agents.is_file():
            line_count = len(self.read_text(agents).splitlines())
            if line_count > 120:
                self.warning(
                    "entrypoint.agents_size",
                    agents,
                    f"AGENTS.md has {line_count} lines; inspect whether implementation detail leaked into the router.",
                )

    def check_policy(self) -> None:
        broad_patterns = {"*", "**", "*.md", "**/*.md", "content-library/**"}
        for key in ("inactive_text_globs", "skip_markdown_link_globs"):
            patterns = self.config.get(key, [])
            if not isinstance(patterns, list):
                self.error("policy.invalid_globs", ".knowledge-validation.json", f"{key} must be a list.")
                continue
            for pattern in patterns:
                if pattern in broad_patterns:
                    self.error(
                        "policy.broad_exclusion",
                        ".knowledge-validation.json",
                        f"{key} contains an unsafe broad exclusion: {pattern}",
                    )

        for key in ("known_project_manifest_exceptions", "known_overloaded_projects"):
            entries = self.config.get(key, {})
            if not isinstance(entries, dict):
                self.error("policy.unreasoned_baseline", ".knowledge-validation.json", f"{key} must map paths to reasons.")
                continue
            for path, reason in entries.items():
                if not isinstance(path, str) or not isinstance(reason, str) or len(reason.strip()) < 20:
                    self.error(
                        "policy.unreasoned_baseline",
                        ".knowledge-validation.json",
                        f"{key} contains a path without a specific reason: {path}",
                    )

        migrations = self.config.get("semantic_markdown_migrations", {})
        if not isinstance(migrations, dict):
            self.error("policy.invalid_migrations", ".knowledge-validation.json", "semantic_markdown_migrations must be an object.")
        else:
            for source, record in migrations.items():
                if not isinstance(record, dict):
                    self.error(
                        "policy.unreviewed_migration",
                        ".knowledge-validation.json",
                        f"Semantic migration must include destination and reason: {source}",
                    )
                    continue
                destination = record.get("destination")
                reason = record.get("reason")
                if not isinstance(destination, str) or not isinstance(reason, str) or len(reason.strip()) < 20:
                    self.error(
                        "policy.unreviewed_migration",
                        ".knowledge-validation.json",
                        f"Semantic migration must include destination and a specific reason: {source}",
                    )

        required_path_terms = self.config.get("required_path_terms", {})
        if not isinstance(required_path_terms, dict):
            self.error(
                "policy.invalid_path_terms",
                ".knowledge-validation.json",
                "required_path_terms must map canonical files to non-empty term lists.",
            )
        else:
            for path, terms in required_path_terms.items():
                if not isinstance(path, str) or not isinstance(terms, list) or not terms:
                    self.error(
                        "policy.invalid_path_terms",
                        ".knowledge-validation.json",
                        f"Invalid canonical precision contract: {path}",
                    )
                    continue
                if any(not isinstance(term, str) or not term.strip() for term in terms):
                    self.error(
                        "policy.invalid_path_terms",
                        ".knowledge-validation.json",
                        f"Canonical precision contract contains an empty or non-string term: {path}",
                    )

    @staticmethod
    def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
        lines = text.splitlines()
        if not lines or lines[0].strip() != "---":
            return {}, "Missing opening YAML delimiter."
        try:
            end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
        except StopIteration:
            return {}, "Missing closing YAML delimiter."

        values: dict[str, str] = {}
        for line in lines[1:end]:
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
            if not match:
                return {}, f"Unsupported frontmatter line: {line}"
            key, raw = match.groups()
            raw = raw.strip()
            if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in {'"', "'"}:
                raw = raw[1:-1]
            values[key] = raw
        return values, None

    @staticmethod
    def parse_quoted_yaml_value(text: str, key: str) -> str | None:
        match = re.search(rf"^\s+{re.escape(key)}:\s*(.+?)\s*$", text, re.MULTILINE)
        if not match:
            return None
        raw = match.group(1)
        try:
            value = json.loads(raw)
        except json.JSONDecodeError:
            return None
        return value if isinstance(value, str) else None

    def check_skills(self) -> None:
        skills_root = self.root / ".agents" / "skills"
        if not skills_root.is_dir():
            self.error("skill.root_missing", skills_root, "Repository Skill directory is missing.")
            return

        agents_text = self.read_text(self.root / "AGENTS.md")
        for skill_dir in sorted(path for path in skills_root.iterdir() if path.is_dir()):
            skill_file = skill_dir / "SKILL.md"
            metadata_file = skill_dir / "agents" / "openai.yaml"
            name = skill_dir.name

            if not skill_file.is_file():
                self.error("skill.file_missing", skill_dir, "Skill directory has no SKILL.md.")
                continue

            text = self.read_text(skill_file)
            frontmatter, problem = self.parse_frontmatter(text)
            if problem:
                self.error("skill.frontmatter", skill_file, problem)
                continue

            extra = sorted(set(frontmatter) - {"name", "description"})
            if extra:
                self.error(
                    "skill.frontmatter_extra",
                    skill_file,
                    f"Only name and description are allowed; found: {', '.join(extra)}.",
                )
            if frontmatter.get("name") != name:
                self.error(
                    "skill.name_mismatch",
                    skill_file,
                    f"Frontmatter name {frontmatter.get('name')!r} does not match folder {name!r}.",
                )
            if not SKILL_NAME_RE.fullmatch(name) or len(name) > 64:
                self.error("skill.invalid_name", skill_file, "Skill name must be kebab-case and at most 64 characters.")

            description = frontmatter.get("description", "").strip()
            if len(description) < 80:
                self.error(
                    "skill.description_short",
                    skill_file,
                    "Description must explain capability plus concrete trigger/non-trigger conditions.",
                )
            if "todo" in description.casefold() or "placeholder" in description.casefold():
                self.error("skill.description_placeholder", skill_file, "Skill description still contains a placeholder.")

            route = f".agents/skills/{name}/SKILL.md"
            if route not in agents_text:
                self.error(
                    "skill.unrouted",
                    skill_file,
                    f"AGENTS.md does not route knowledge tasks to {route}.",
                )

            if not metadata_file.is_file():
                self.error("skill.metadata_missing", metadata_file, "agents/openai.yaml is required for repository Skills.")
                continue

            metadata = self.read_text(metadata_file)
            if "todo" in metadata.casefold() or "placeholder" in metadata.casefold():
                self.error("skill.metadata_placeholder", metadata_file, "Skill UI metadata contains a placeholder.")

            display_name = self.parse_quoted_yaml_value(metadata, "display_name")
            short_description = self.parse_quoted_yaml_value(metadata, "short_description")
            default_prompt = self.parse_quoted_yaml_value(metadata, "default_prompt")
            if not display_name:
                self.error("skill.metadata_display", metadata_file, "Missing quoted interface.display_name.")
            if not short_description or not 25 <= len(short_description) <= 64:
                self.error(
                    "skill.metadata_short_description",
                    metadata_file,
                    "short_description must be quoted and 25-64 characters.",
                )
            if not default_prompt or f"${name}" not in default_prompt:
                self.error(
                    "skill.metadata_default_prompt",
                    metadata_file,
                    f"default_prompt must be quoted and mention ${name}.",
                )

    @staticmethod
    def extract_target(raw_target: str) -> str:
        target = raw_target.strip()
        if target.startswith("<") and ">" in target:
            return target[1 : target.index(">")]
        return target.split(maxsplit=1)[0] if target else ""

    @staticmethod
    def slug_base(heading: str) -> str:
        heading = re.sub(r"<[^>]+>", "", heading)
        heading = re.sub(r"!?\[([^\]]+)\]\([^)]+\)", r"\1", heading)
        heading = heading.replace("`", "").strip().casefold()
        kept: list[str] = []
        for char in heading:
            category = unicodedata.category(char)
            if char.isspace() or char == "-" or category[0] in {"L", "N"}:
                kept.append(char)
        slug = "".join(kept)
        slug = re.sub(r"\s+", "-", slug)
        slug = re.sub(r"-+", "-", slug).strip("-")
        return slug

    def heading_anchors(self, path: Path) -> set[str]:
        if path in self._heading_cache:
            return self._heading_cache[path]
        counts: dict[str, int] = {}
        anchors: set[str] = set()
        for line in self.read_text(path).splitlines():
            match = HEADING_RE.match(line)
            if not match:
                continue
            base = self.slug_base(match.group(2))
            if not base:
                continue
            count = counts.get(base, 0)
            anchors.add(base if count == 0 else f"{base}-{count}")
            counts[base] = count + 1
        self._heading_cache[path] = anchors
        return anchors

    def resolve_link(self, source: Path, target: str) -> tuple[Path | None, str]:
        path_part, _, fragment = target.partition("#")
        path_part = unquote(path_part.split("?", 1)[0])
        if not path_part:
            return source, unquote(fragment)
        candidate = Path(path_part)
        if not candidate.is_absolute():
            candidate = source.parent / candidate
        return candidate.resolve(), unquote(fragment)

    def check_markdown_links(self) -> None:
        for path in self.markdown_files():
            rel_path = self.rel(path)
            if self.matches(rel_path, "skip_markdown_link_globs"):
                self.note("markdown.links_skipped", rel_path, "Immutable archive link targets are intentionally not normalized.")
                continue

            for line_number, line in enumerate(self.read_text(path).splitlines(), start=1):
                for raw_target in LINK_RE.findall(line):
                    target = self.extract_target(raw_target)
                    if not target:
                        continue
                    lowered = target.casefold()
                    if lowered.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                        continue
                    if any(token in target for token in ("<project>", "<project-name>", "{{", "}}")):
                        continue

                    candidate, fragment = self.resolve_link(path, target)
                    location = f"{rel_path}:{line_number}"
                    if candidate is None or not candidate.exists():
                        self.error("markdown.broken_link", location, f"Local target does not exist: {target}")
                        continue
                    if fragment and candidate.is_file() and candidate.suffix.casefold() == ".md":
                        normalized = fragment.casefold()
                        if normalized not in self.heading_anchors(candidate):
                            self.warning(
                                "markdown.broken_anchor",
                                location,
                                f"Heading anchor was not found in {self.rel(candidate)}: #{fragment}",
                            )

    def active_markdown(self) -> list[Path]:
        return [
            path
            for path in self.markdown_files()
            if not self.matches(self.rel(path), "inactive_text_globs")
        ]

    def check_stale_routes(self) -> None:
        for path in self.active_markdown():
            text = self.read_text(path)
            for term in self.config.get("stale_active_terms", []):
                if term in text:
                    self.error(
                        "route.stale_active_term",
                        path,
                        f"Active document still contains retired route: {term}",
                    )

    def local_linked_files(self, index_path: Path) -> set[str]:
        linked: set[str] = set()
        for raw_target in LINK_RE.findall(self.read_text(index_path)):
            target = self.extract_target(raw_target)
            if not target or target.startswith("#"):
                continue
            if target.casefold().startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            candidate, _ = self.resolve_link(index_path, target)
            if candidate and candidate.is_file():
                try:
                    linked.add(self.rel(candidate))
                except ValueError:
                    pass
        return linked

    def check_index_coverage(self) -> None:
        index_specs = (
            (
                self.root / "framer" / "basic" / "README.md",
                self.root / "framer" / "basic",
                "index.basic_unlisted",
            ),
            (
                self.root / "framer" / "advance-design" / "README.md",
                self.root / "framer" / "advance-design",
                "index.advanced_unlisted",
            ),
        )
        for index_path, knowledge_root, code in index_specs:
            if not index_path.is_file() or not knowledge_root.is_dir():
                continue
            linked = self.local_linked_files(index_path)
            for path in sorted(knowledge_root.rglob("*.md")):
                if path == index_path:
                    continue
                rel_path = self.rel(path)
                if rel_path not in linked:
                    self.error(code, path, f"Knowledge file is not linked directly from {self.rel(index_path)}.")

    def check_project_hygiene(self) -> None:
        content_root = self.root / "content-library"
        manifest_exceptions = self.config.get("known_project_manifest_exceptions", {})
        overloaded = self.config.get("known_overloaded_projects", {})

        for project_dir in sorted(path for path in content_root.iterdir() if path.is_dir() and not path.name.startswith(".")):
            rel_dir = self.rel(project_dir)
            manifest = project_dir / "PROJECT.md"
            if not manifest.is_file():
                if rel_dir in manifest_exceptions:
                    self.note("project.manifest_baseline", rel_dir, manifest_exceptions[rel_dir])
                else:
                    self.warning("project.manifest_missing", rel_dir, "Project directory has no PROJECT.md entry point.")
                continue

            manifest_text = self.read_text(manifest)
            line_count = len(manifest_text.splitlines())
            rel_manifest = self.rel(manifest)
            if line_count > 400:
                if rel_manifest in overloaded:
                    self.note(
                        "project.overloaded_baseline",
                        rel_manifest,
                        f"{overloaded[rel_manifest]} Current line count: {line_count}.",
                    )
                else:
                    self.warning(
                        "project.overloaded_manifest",
                        rel_manifest,
                        f"PROJECT.md has {line_count} lines; inspect current/history/status/recovery ownership.",
                    )

            for owner_name in ("STATUS.md", "DECISIONS.md", "RECOVERY.md", "HISTORY.md"):
                owner = project_dir / owner_name
                if owner.is_file() and owner_name not in manifest_text:
                    self.warning(
                        "project.unlinked_owner",
                        owner,
                        f"Split current/history owner is not linked from {rel_manifest}.",
                    )

            recovery = project_dir / "RECOVERY.md"
            if recovery.is_file():
                recovery_lines = len(self.read_text(recovery).splitlines())
                if recovery_lines > 120:
                    self.warning(
                        "project.recovery_size",
                        recovery,
                        f"RECOVERY.md has {recovery_lines} lines; it may be accumulating history.",
                    )

    def check_archives(self) -> None:
        for rel_path, expected in sorted(self.config.get("immutable_archives", {}).items()):
            path = self.root / rel_path
            if not path.is_file():
                self.error("archive.missing", rel_path, "Configured immutable archive is missing.")
                continue
            actual = hashlib.sha256(path.read_bytes()).hexdigest()
            if actual != expected:
                self.error(
                    "archive.hash_mismatch",
                    rel_path,
                    f"SHA-256 changed: expected {expected}, got {actual}.",
                )

    def check_required_terms(self) -> None:
        corpus = "\n".join(self.read_text(path) for path in self.markdown_files()).casefold()
        for term in self.config.get("required_terms", []):
            if term.casefold() not in corpus:
                self.error("preservation.term_missing", ".knowledge-validation.json", f"Required exact knowledge term is missing: {term}")

        for rel_path, terms in self.config.get("required_path_terms", {}).items():
            path = self.root / rel_path
            if not path.is_file():
                self.error(
                    "preservation.canonical_file_missing",
                    rel_path,
                    "Canonical precision contract points to a missing file.",
                )
                continue
            text = self.read_text(path).casefold()
            for term in terms:
                if term.casefold() not in text:
                    self.error(
                        "preservation.canonical_term_missing",
                        rel_path,
                        f"Required exact knowledge term is missing from its canonical owner: {term}",
                    )

    @staticmethod
    def markdown_table_cells(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip().strip("|").split("|")]

    def check_component_contracts(self) -> None:
        """Validate persisted component contracts without inferring Canvas truth."""

        expected_headers = [value.casefold() for value in COMPONENT_CONTRACT_HEADERS]
        expected_concerns = {value.casefold(): value for value in COMPONENT_CONTRACT_CONCERNS}
        unfinished_tokens = ("tbd", "todo", "pending", "[ ]")

        for path in self.active_markdown():
            rel_path = self.rel(path)
            if not rel_path.startswith("content-library/") or "/checklist/" not in rel_path:
                continue

            text = self.read_text(path)
            lines = text.splitlines()
            starts = [i for i, line in enumerate(lines) if line.strip() == COMPONENT_CONTRACT_HEADING]
            if not starts:
                continue
            if len(starts) > 1:
                self.error(
                    "component_contract.duplicate",
                    path,
                    "A request Checklist must not contain multiple active Component Requirement Contracts.",
                )

            for start in starts:
                end = next(
                    (i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")),
                    len(lines),
                )
                section_lines = lines[start:end]
                section = "\n".join(section_lines)
                status_match = re.search(
                    r"Contract status:\s*(?:\*\*)?(Draft|Ready|Pass|Blocked)(?:\*\*)?",
                    section,
                    flags=re.IGNORECASE,
                )
                if not status_match:
                    self.error(
                        "component_contract.status",
                        path,
                        "Component Requirement Contract must declare Contract status: Draft, Ready, Pass, or Blocked.",
                    )
                    status = ""
                else:
                    status = status_match.group(1).casefold()

                header_index = None
                for index, line in enumerate(section_lines):
                    if not line.lstrip().startswith("|"):
                        continue
                    cells = [cell.casefold() for cell in self.markdown_table_cells(line)]
                    if cells == expected_headers:
                        header_index = index
                        break
                if header_index is None:
                    self.error(
                        "component_contract.headers",
                        path,
                        "Component contract table is missing the canonical six columns or their order changed.",
                    )
                    continue

                data_start = header_index + 1
                if data_start < len(section_lines):
                    separator = self.markdown_table_cells(section_lines[data_start])
                    if len(separator) == len(COMPONENT_CONTRACT_HEADERS) and all(
                        re.fullmatch(r":?-{3,}:?", cell) for cell in separator
                    ):
                        data_start += 1

                rows: dict[str, list[str]] = {}
                for line in section_lines[data_start:]:
                    if not line.lstrip().startswith("|"):
                        if rows:
                            break
                        continue
                    cells = self.markdown_table_cells(line)
                    if len(cells) != len(COMPONENT_CONTRACT_HEADERS):
                        self.error(
                            "component_contract.columns",
                            path,
                            f"Component contract row must have {len(COMPONENT_CONTRACT_HEADERS)} cells: {line.strip()}",
                        )
                        continue
                    concern_key = cells[0].casefold()
                    if concern_key in rows:
                        self.error(
                            "component_contract.duplicate_concern",
                            path,
                            f"Duplicate Component contract concern: {cells[0]}",
                        )
                    rows[concern_key] = cells

                for concern_key, display in expected_concerns.items():
                    if concern_key not in rows:
                        self.error(
                            "component_contract.concern_missing",
                            path,
                            f"Component contract is missing required concern: {display}",
                        )

                for concern_key, cells in rows.items():
                    if concern_key not in expected_concerns:
                        self.warning(
                            "component_contract.unknown_concern",
                            path,
                            f"Non-canonical concern should be folded into the fixed contract or justified separately: {cells[0]}",
                        )
                    if any(not cell.strip() for cell in cells):
                        self.error(
                            "component_contract.empty_cell",
                            path,
                            f"Component contract row contains a blank cell: {cells[0] or '<unnamed>'}",
                        )
                        continue

                    decision = cells[1].strip()
                    if decision.casefold() == "n/a" or (
                        decision.casefold().startswith("n/a")
                        and "—" not in decision
                        and " - " not in decision
                    ):
                        self.error(
                            "component_contract.unreasoned_na",
                            path,
                            f"N/A must include a reason: {cells[0]}",
                        )

                    governing_source = cells[3].strip()
                    if ".md" in governing_source.casefold() and "#" not in governing_source:
                        self.error(
                            "component_contract.unscoped_source",
                            path,
                            f"Markdown governing source must target path.md#heading: {cells[0]}",
                        )
                    if governing_source.casefold() == "baseline":
                        self.error(
                            "component_contract.unscoped_source",
                            path,
                            f"Bare Baseline is not a targeted governing source: {cells[0]}",
                        )

                    if status == "pass":
                        proof = " ".join(cells[4:]).casefold()
                        if any(token in proof for token in unfinished_tokens) or "planned" in proof:
                            self.error(
                                "component_contract.unproven_pass",
                                path,
                                f"Pass contract still contains planned or unfinished proof: {cells[0]}",
                            )

    def current_markdown_hashes(self) -> dict[str, list[str]]:
        hashes: dict[str, list[str]] = {}
        for path in self.markdown_files():
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            hashes.setdefault(digest, []).append(self.rel(path))
        return hashes

    def check_deleted_markdown(self) -> None:
        result = self.run_git("diff", "HEAD", "--name-status", "--diff-filter=D")
        if result.returncode != 0:
            self.warning("git.deleted_scan", ".git", result.stderr.decode("utf-8", errors="replace").strip())
            return

        current_hashes = self.current_markdown_hashes()
        semantic = self.config.get("semantic_markdown_migrations", {})
        for raw_line in result.stdout.decode("utf-8", errors="replace").splitlines():
            parts = raw_line.split("\t", 1)
            if len(parts) != 2:
                continue
            source = parts[1]
            if not source.casefold().endswith(".md"):
                continue

            old = self.run_git("show", f"HEAD:{source}")
            if old.returncode != 0:
                self.warning("migration.source_unreadable", source, "Deleted Markdown cannot be read from HEAD for preservation audit.")
                continue
            digest = hashlib.sha256(old.stdout).hexdigest()
            exact_destinations = [path for path in current_hashes.get(digest, []) if path != source]
            if exact_destinations:
                self.note(
                    "migration.exact_destination",
                    source,
                    f"Byte-identical destination: {', '.join(exact_destinations)}.",
                )
                continue

            record = semantic.get(source, {})
            destination = record.get("destination") if isinstance(record, dict) else None
            reason = record.get("reason") if isinstance(record, dict) else None
            if destination and (self.root / destination).is_file():
                self.note(
                    "migration.semantic_destination",
                    source,
                    f"Configured reviewed destination: {destination}. {reason}",
                )
                continue

            self.error(
                "migration.unmapped_delete",
                source,
                "Deleted Markdown has no byte-identical or configured reviewed destination.",
            )

    def check_git_diff(self) -> None:
        result = self.run_git("diff", "HEAD", "--check")
        if result.returncode != 0:
            output = (result.stdout + result.stderr).decode("utf-8", errors="replace").strip()
            self.error("git.diff_check", "git diff --check", output or "git diff --check failed.")

    def validate(self) -> None:
        self.check_policy()
        self.check_entrypoints()
        self.check_skills()
        self.check_markdown_links()
        self.check_stale_routes()
        self.check_index_coverage()
        self.check_project_hygiene()
        self.check_archives()
        self.check_required_terms()
        self.check_component_contracts()
        self.check_deleted_markdown()
        self.check_git_diff()

    def result(self) -> dict:
        order = {"error": 0, "warning": 1, "note": 2}
        findings = sorted(
            self.findings,
            key=lambda item: (order[item.severity], item.path, item.code, item.message),
        )
        errors = sum(item.severity == "error" for item in findings)
        warnings = sum(item.severity == "warning" for item in findings)
        notes = sum(item.severity == "note" for item in findings)
        passed = errors == 0 and (warnings == 0 or not self.strict)
        return {
            "status": "PASS" if passed else "FAIL",
            "strict": self.strict,
            "errors": errors,
            "warnings": warnings,
            "notes": notes,
            "findings": [dataclasses.asdict(item) for item in findings],
        }


def discover_root(start: Path) -> Path:
    start = start.resolve()
    candidates = (start, *start.parents)
    for candidate in candidates:
        if (candidate / "AGENTS.md").is_file() and (candidate / ".knowledge-validation.json").is_file():
            return candidate
    raise FileNotFoundError("Could not find AGENTS.md plus .knowledge-validation.json in this directory or its parents.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, help="Repository root; defaults to discovery from the current directory.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as validation failures.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        root = args.root.resolve() if args.root else discover_root(Path.cwd())
        config_path = root / ".knowledge-validation.json"
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, FileNotFoundError) as exc:
        print(f"Knowledge architecture validation: FAIL\n[ERROR] config: {exc}", file=sys.stderr)
        return 2

    if config.get("version") != 1:
        print("Knowledge architecture validation: FAIL\n[ERROR] config: unsupported policy version.", file=sys.stderr)
        return 2

    validator = Validator(root, config, args.strict)
    validator.validate()
    result = validator.result()

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Knowledge architecture validation: {result['status']}")
        for finding in result["findings"]:
            print(
                f"[{finding['severity'].upper()}] {finding['code']} "
                f"{finding['path']}: {finding['message']}"
            )
        print(
            f"Summary: {result['errors']} error(s), "
            f"{result['warnings']} warning(s), {result['notes']} note(s)."
        )

    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
