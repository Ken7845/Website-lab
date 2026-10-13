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
VISUAL_CONTRACT_HEADING = "## Visual Direction Contract"
VISUAL_CONTRACT_HEADERS = (
    "Concern",
    "Decision / N/A reason",
    "Owner",
    "Governing source",
    "Structural proof",
    "Visual proof",
)
VISUAL_CONTRACT_CONCERNS = (
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
        for key in ("inactive_text_globs", "skip_markdown_link_globs"):
            patterns = self.config.get(key, [])
            if not isinstance(patterns, list):
                self.error("policy.invalid_globs", ".knowledge-validation.json", f"{key} must be a list.")
                continue
            for pattern in patterns:
                if not isinstance(pattern, str):
                    self.error("policy.invalid_globs", ".knowledge-validation.json", f"Non-string {key} pattern.")
                    continue
                if key == "skip_markdown_link_globs":
                    permitted = pattern in self.config.get("immutable_archives", {}) and not any(c in pattern for c in "*?[")
                else:
                    permitted = pattern in {"history/**", "content-library/**/history/**"} or (
                        not any(c in pattern for c in "*?[") and (
                            pattern in self.config.get("immutable_archives", {}) or
                            len(self.config.get("inactive_document_reasons", {}).get(pattern, "")) >= 20
                        )
                    )
                if not permitted:
                    self.error("policy.broad_exclusion", ".knowledge-validation.json", f"Unbounded or unreviewed {key} scope: {pattern}")
                if not any(fnmatch.fnmatchcase(self.rel(p), pattern) for p in self.markdown_files()):
                    self.error("policy.empty_exclusion", ".knowledge-validation.json", f"Exclusion matches no preserved document: {pattern}")

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
            if route not in self.reachable_markdown("AGENTS.md"):
                self.error(
                    "skill.unrouted",
                    skill_file,
                    f"Skill is not reachable through the canonical AGENTS dispatcher: {route}.",
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

    @staticmethod
    def prose_lines(text: str) -> list[str]:
        """Preserve line numbers while hiding fenced examples from executable checks."""
        lines = []
        fence = None
        for line in text.splitlines():
            match = re.match(r"^\s*(`{3,}|~{3,})", line)
            if match:
                token = match.group(1)
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence):
                    fence = None
                lines.append("")
            else:
                lines.append(line if fence is None else "")
        return lines

    def reachable_markdown(self, start: str) -> set[str]:
        visited = set()
        pending = [start]
        while pending:
            item = pending.pop()
            if item in visited or not (self.root / item).is_file():
                continue
            visited.add(item)
            pending.extend(p for p in self.local_linked_files(self.root / item) - visited if Path(p).suffix.casefold() == ".md")
        return visited

    def check_required_routes(self) -> None:
        for source, targets in self.config.get("required_routes", {}).items():
            p = self.root / source
            if not p.is_file():
                self.error("route.owner_missing", source, "Canonical route owner is missing.")
                continue
            actual = set()
            for raw in LINK_RE.findall("\n".join(self.prose_lines(self.read_text(p)))):
                candidate, fragment = self.resolve_link(p, self.extract_target(raw))
                if candidate:
                    actual.add((str(candidate), fragment.casefold()))
            for target in targets:
                candidate, fragment = self.resolve_link(self.root / "README.md", target)
                if (str(candidate), fragment.casefold()) not in actual:
                    self.error("route.required_missing", source, f"Required canonical link is missing: {target}")

    def rule_target(self, source: Path, target: str) -> tuple[Path | None, str]:
        """Top-level repository paths are root-relative; ./, ../ and basenames are local."""
        top = target.split("/", 1)[0]
        if top in {".agents", "framer", "content-library", "history", "inspiration"}:
            return self.resolve_link(self.root / "README.md", target)
        return self.resolve_link(source, target)

    def check_rule_target(self, source: Path, target: str, code: str, location: str) -> None:
        candidate, fragment = self.rule_target(source, target)
        if candidate is None or not candidate.is_file():
            self.error(code + ".missing_source", location, f"Rule source does not exist: {target}")
        elif fragment and fragment.casefold() not in self.heading_anchors(candidate):
            self.error(code + ".missing_anchor", location, f"Rule heading does not exist: {target}")

    def check_inline_routes(self) -> None:
        for path in self.active_markdown():
            for number, line in enumerate(self.prose_lines(self.read_text(path)), 1):
                for token in re.findall(r"`([^`]+)`", line):
                    if any(x in token for x in ("<", ">", "{{", "}}")) or token == "path.md#heading":
                        continue
                    anchored = re.fullmatch(r"[^\s]+\.md#[^\s]+", token)
                    directed = re.search(r"(?:read|follow|load|读取|遵循)\s*`" + re.escape(token), line, re.I)
                    if anchored or (directed and token.endswith(".md")):
                        self.check_rule_target(path, token, "route.inline", f"{self.rel(path)}:{number}")

    def heading_anchors(self, path: Path) -> set[str]:
        if path in self._heading_cache:
            return self._heading_cache[path]
        counts: dict[str, int] = {}
        anchors: set[str] = set()
        for line in self.prose_lines(self.read_text(path)):
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

    def check_discovery(self) -> None:
        index = self.root / "content-library/README.md"
        linked = self.local_linked_files(index)
        for p in (self.root / "content-library").glob("*/PROJECT.md"):
            if self.rel(p) not in linked:
                self.error("index.project_unlisted", p, "Project is not directly linked from Content Library index.")
        inspiration = self.root / "inspiration/README.md"
        if inspiration.is_file():
            linked = self.local_linked_files(inspiration)
            for p in (self.root / "inspiration").rglob("*.md"):
                if p != inspiration and self.rel(p) not in linked:
                    self.error("index.inspiration_unlisted", p, "Reference classification is missing from Inspiration index.")
        for index in (self.root / "content-library").glob("*/checklist/README.md"):
            text = self.read_text(index)
            p = index.parent.parent / "PROJECT.md"
            if self.rel(p) not in self.local_linked_files(index):
                self.error("index.project_backlink", index, "Checklist index must link its PROJECT owner.")
            for line in self.prose_lines(text):
                if not line.lstrip().startswith("|"):
                    continue
                for raw in LINK_RE.findall(line):
                    target, _ = self.resolve_link(index, self.extract_target(raw))
                    if target and target.is_dir():
                        self.error("index.ambiguous_page_owner", index, "Page table must link an exact canonical page file, not a directory.")

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

    def owner_section(self, path: Path, fragment: str) -> str:
        lines = self.prose_lines(self.read_text(path))
        if not fragment:
            return "\n".join(lines)
        counts = {}
        for index, line in enumerate(lines):
            m = HEADING_RE.match(line)
            if not m:
                continue
            base = self.slug_base(m.group(2))
            count = counts.get(base, 0)
            counts[base] = count + 1
            anchor = base if count == 0 else f"{base}-{count}"
            if anchor == fragment.casefold():
                level = len(m.group(1))
                end = next((i for i in range(index + 1, len(lines)) if (h := HEADING_RE.match(lines[i])) and len(h.group(1)) <= level), len(lines))
                return "\n".join(lines[index:end])
        return ""

    def pointer(self, source: Path, value: str) -> tuple[str, str] | None:
        if re.match(r"None\s+—\s+\S", value, re.I):
            return ("none", "")
        match = LINK_RE.search(value)
        if not match:
            return None
        target = self.extract_target(match.group(1))
        candidate, fragment = self.resolve_link(source, target)
        if not candidate or not candidate.is_file() or (fragment and fragment.casefold() not in self.heading_anchors(candidate)):
            return None
        return (str(candidate), fragment.casefold())

    def check_current_state(self) -> None:
        for project in sorted((self.root / "content-library").glob("*/PROJECT.md")):
            text = "\n".join(self.prose_lines(self.read_text(project)))
            if self.field(text, "State schema") != "1":
                self.error("state.schema_missing", project, "Current PROJECT must declare State schema: 1.")
                continue
            owners = {}
            for role in ("Current status owner", "Recovery owner"):
                value = self.field(text, role) or ""
                point = self.pointer(project, value)
                if not point or point[0] == "none":
                    self.error("state.owner_missing", project, f"Missing valid owner link: {role}")
                    continue
                path, fragment = Path(point[0]), point[1]
                owners[role] = (path, fragment, self.owner_section(path, fragment))
            if len(owners) != 2:
                continue
            status_path, status_fragment, status = owners["Current status owner"]
            recovery_path, _, recovery = owners["Recovery owner"]
            self.check_closeout(project, status_path, status)
            revisions = [self.field(t, "State revision") for t in (status, recovery)]
            if any(not v or not re.fullmatch(r"\d{4}-\d{2}-\d{2}(?:[a-z0-9.-]*)?", v) for v in revisions):
                self.error("state.revision_missing", project, "Both current owners require an explicit state revision.")
            elif revisions[0] != revisions[1]:
                self.error("state.stale_recovery", project, "Recovery revision differs from Status.")
            points = []
            for owner_path, t in ((status_path, status), (recovery_path, recovery)):
                value = self.field(t, "Active request") or ""
                points.append(self.pointer(owner_path, value))
            if any(point is None for point in points):
                self.error("state.active_request_missing", project, "Both owners require a valid Active request or None — reason.")
            elif points[0] != points[1]:
                self.error("state.active_request_conflict", project, "Status and Recovery point to different active requests.")
            reference = self.pointer(recovery_path, self.field(recovery, "State reference") or "")
            if reference != (str(status_path), status_fragment):
                self.error("state.reference_conflict", project, "Recovery must reference its declared Status owner.")
            if len(recovery.splitlines()) > 120:
                self.error("state.recovery_overloaded", project, "Inline or split Recovery exceeds 120 lines; move chronology to History.")

    def check_closeout(self, project: Path, status_path: Path, status: str) -> None:
        """Validate a declared receipt; do not infer unrecorded external work."""
        schema = self.field(status, "Closeout schema")
        receipt = self.field(status, "Observation")
        if schema is None and receipt is None:
            return  # Older untouched state has no declared closeout schema.
        if schema != "1":
            self.error("closeout.schema", status_path, "Observation receipts require Closeout schema: 1.")
            return
        if receipt and re.fullmatch(r"(?:N/A|Blocked)\s+—\s+\S.*", receipt, re.I):
            return
        if not receipt or not re.match(r"Recorded\s+—\s+", receipt, re.I):
            self.error("closeout.receipt_missing", status_path, "Declare Recorded — linked entry, N/A — scope reason, or Blocked — write blocker.")
            return
        point = self.pointer(status_path, receipt)
        if not point or point[0] == "none" or not point[1]:
            self.error("closeout.entry_missing", status_path, "Recorded needs an existing local observation entry heading.")
            return
        path, fragment = Path(point[0]).resolve(), point[1]
        observation_dir = (self.root / "history/workflow-observations").resolve()
        slug = re.sub(r"[^a-z0-9]+", "-", project.parent.name.casefold()).strip("-")
        if path.parent != observation_dir or path.name != slug + ".md":
            self.error("closeout.wrong_project", status_path, "Observation must use this project's canonical repository log, not another project or workspace.")
            return
        entry = self.owner_section(path, fragment)
        for field in ("Task reference", "Actions", "Verification", "Outcome"):
            value = self.field(entry, field)
            if not value or re.fullmatch(r"(?:TODO|TBD|Pending)", value, re.I):
                self.error("closeout.entry_incomplete", status_path, f"Recorded entry lacks factual {field}.")

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

    @staticmethod
    def field(text: str, name: str) -> str | None:
        match = re.search(r"^\s*(?:-\s*)?" + re.escape(name) + r":\s*(.+)$", text, re.M | re.I)
        return match.group(1).strip() if match else None

    def checklist_documents(self) -> list[Path]:
        return [p for p in self.active_markdown() if self.rel(p).startswith("content-library/") and "/checklist/" in self.rel(p)]

    def contract_sections(self, text: str, title: str) -> list[list[str]]:
        lines = self.prose_lines(text)
        starts = []
        for index, line in enumerate(lines):
            match = HEADING_RE.match(line)
            if match and re.sub(r"^\d+[.)]\s*", "", match.group(2)).strip().casefold() == title.casefold():
                starts.append((index, len(match.group(1))))
        result = []
        for start, level in starts:
            end = next((i for i in range(start + 1, len(lines)) if (m := HEADING_RE.match(lines[i])) and len(m.group(1)) <= level), len(lines))
            result.append(lines[start:end])
        return result

    def check_contract_applicability(self) -> None:
        for path in self.checklist_documents():
            text = "\n".join(self.prose_lines(self.read_text(path)))
            if self.field(text, "Contract schema") != "1":
                continue
            for kind, title in (("Component", "Component Requirement Contract"), ("Visual", "Visual Direction Contract")):
                value = self.field(text, kind + " contract")
                sections = self.contract_sections(text, title)
                code = kind.casefold() + "_contract"
                if not value or not re.fullmatch(r"Required|N/A\s+—\s+\S.*|Legacy\s+—\s+.*\d{4}-\d{2}-\d{2}.*", value, re.I):
                    self.error(code + ".applicability", path, "Declare Required, N/A — reason, or Legacy — dated source.")
                elif value.casefold() == "required" and not sections:
                    self.error(code + ".required_missing", path, "Required contract is absent.")
                elif value.casefold().startswith("n/a") and sections:
                    self.error(code + ".applicability_conflict", path, "N/A request contains an active contract.")

    def check_component_contracts(self) -> None:
        self.check_contracts("Component Requirement Contract", COMPONENT_CONTRACT_HEADERS, COMPONENT_CONTRACT_CONCERNS, "component_contract")

    def check_visual_contracts(self) -> None:
        self.check_contracts("Visual Direction Contract", VISUAL_CONTRACT_HEADERS, VISUAL_CONTRACT_CONCERNS, "visual_contract")

    def check_contracts(self, title: str, headers: tuple, concerns: tuple, code: str) -> None:
        expected = {c.casefold(): c for c in concerns}
        unfinished = re.compile(r"\b(?:tbd|todo|pending|planned|unperformed|unchecked|not run|not reviewed|not tested)\b|\[ \]", re.I)
        for path in self.checklist_documents():
            text = self.read_text(path)
            sections = self.contract_sections(text, title)
            if len(sections) > 1:
                self.error(code + ".duplicate", path, "A document must have one active contract of each kind.")
            schema = self.field("\n".join(self.prose_lines(text)), "Contract schema") == "1"
            for lines in sections:
                section = "\n".join(lines)
                status = self.field(section, "Contract status") or ""
                status_match = re.match(r"(?:\*\*)?(Draft|Ready|Pass|Fix Required|Blocked)\b", status, re.I)
                status = status_match.group(1).casefold() if status_match else ""
                if not status:
                    self.error(code + ".status", path, "Missing valid Contract status.")
                implementation = self.field(section, "Implementation status") or ""
                verification = self.field(section, "Verification status") or ""
                if schema:
                    if not re.match(r"^(Implemented|Partial|Not started)\b", implementation, re.I):
                        self.error(code + ".implementation", path, "Declare implementation stage separately.")
                    if not re.match(r"^(Pass|Fix Required|Blocked|Not run)\b", verification, re.I):
                        self.error(code + ".verification", path, "Declare verification result separately.")
                    if status == "ready" and implementation.casefold().startswith(("implemented", "partial")):
                        self.error(code + ".stale_ready", path, "Implemented work cannot retain a preparation-only Ready state.")
                    if status == "pass" and not implementation.casefold().startswith("implemented"):
                        self.error(code + ".incomplete_pass", path, "Pass requires completed applicable implementation.")
                    if status in {"draft", "ready"} and not verification.casefold().startswith("not run"):
                        self.error(code + ".preparation_verification", path, "Preparation status cannot claim a post-implementation verification result.")
                    if status in {"pass", "blocked", "fix required"} and not verification.casefold().startswith(status):
                        self.error(code + ".result_conflict", path, "Contract and verification outcomes disagree.")
                header_index = next((i for i, l in enumerate(lines) if l.lstrip().startswith("|") and [c.casefold() for c in self.markdown_table_cells(l)] == [h.casefold() for h in headers]), None)
                if header_index is None:
                    self.error(code + ".headers", path, "Missing canonical six-column contract table.")
                    continue
                rows = {}
                for line in lines[header_index + 1:]:
                    if not line.lstrip().startswith("|"):
                        if rows:
                            break
                        continue
                    cells = self.markdown_table_cells(line)
                    if all(re.fullmatch(r":?-{3,}:?", c) for c in cells):
                        continue
                    if len(cells) != len(headers):
                        self.error(code + ".columns", path, "Contract row has the wrong number of cells.")
                        continue
                    key = cells[0].casefold()
                    if key in rows:
                        self.error(code + ".duplicate_concern", path, f"Duplicate concern: {cells[0]}")
                    rows[key] = cells
                for key, label in expected.items():
                    if key not in rows:
                        self.error(code + ".concern_missing", path, f"Missing concern: {label}")
                for key, cells in rows.items():
                    if key not in expected:
                        self.warning(code + ".unknown_concern", path, f"Unknown concern: {cells[0]}")
                    if any(not c.strip() for c in cells) and status != "draft":
                        self.error(code + ".empty_cell", path, f"Blank cell: {cells[0]}")
                    if cells[1].casefold().startswith("n/a") and not re.match(r"N/A\s*(?:—|-)\s*\S", cells[1], re.I):
                        self.error(code + ".unreasoned_na", path, f"N/A needs a reason: {cells[0]}")
                    source = cells[3]
                    if source.casefold() == "baseline" or (".md" in source.casefold() and "#" not in source):
                        self.error(code + ".unscoped_source", path, f"Source must identify a rule heading: {cells[0]}")
                    for target in re.findall(r"[^\s`<>()|;,]+\.md#[^\s`<>()|;,]+", source):
                        self.check_rule_target(path, target, code, self.rel(path))
                    for proof in cells[4:]:
                        if status == "pass" and unfinished.search(proof):
                            self.error(code + ".unproven_pass", path, f"Pass has unfinished proof: {cells[0]}")
                        if schema and status not in {"draft", "ready"}:
                            if not re.match(r"^(Pass|Fix Required|Blocked|N/A)\s+—\s+\S", proof, re.I):
                                self.error(code + ".proof_state", path, f"Proof needs a result and evidence/reason: {cells[0]}")
                            elif status == "pass" and not proof.casefold().startswith(("pass —", "n/a —")):
                                self.error(code + ".unproven_pass", path, f"Pass has a failing or blocked proof: {cells[0]}")
                            if proof.casefold().startswith("pass —"):
                                evidence = LINK_RE.findall(proof)
                                if not evidence:
                                    self.error(code + ".evidence_missing", path, f"Pass requires a scoped evidence-record link: {cells[0]}")
                                for raw in evidence:
                                    target = self.extract_target(raw)
                                    if not target.casefold().startswith(("https://", "http://")):
                                        self.check_rule_target(path, target, code + ".evidence", self.rel(path))

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
        self.check_required_routes()
        self.check_inline_routes()
        self.check_index_coverage()
        self.check_project_hygiene()
        self.check_discovery()
        self.check_current_state()
        self.check_archives()
        self.check_required_terms()
        self.check_contract_applicability()
        self.check_component_contracts()
        self.check_visual_contracts()
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
