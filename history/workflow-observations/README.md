# Workflow Observations

This directory records lightweight evidence from real website-construction work so later retrospectives can improve routing, Skills, references, and validation. **Do not preload** these files during ordinary project work.

## When to record

Write one compact entry after implementation and targeted QA for a meaningful Page, Section, reusable Component, Interaction, multi-breakpoint Part, or task that exposes a reusable workflow failure.

Do not record routine copy, link, naming, or isolated spacing fixes unless they reveal a broader failure. Do not interrupt implementation to maintain a diary. If a task is interrupted, use the project's `RECOVERY.md`; write an observation only after a meaningful outcome exists.

## Where to record

Use one append-only file per project, named with the same project slug used in `content-library/`:

```text
history/workflow-observations/
├── aurelia.md
├── summit-roofing.md
└── <project-slug>.md
```

Do not create a file after every Prompt. Multiple Prompts, corrections, and follow-ups that belong to one meaningful construction task become one brief closing entry in that project's file. Later discoveries append to the same entry rather than creating a competing account. Cross-project workflow work may use `repository.md` only when no single project owns it. These files are retrospective evidence, not current project truth.

## Entry format

```markdown
## YYYY-MM-DD — Part

- Task reference: task, request Checklist, or Git commit when available
- Request: one or two factual sentences describing what the user asked for
- Route selected: project entry → live implementation → primary Skill → targeted references → QA
- Actions: compact summary of what was actually changed
- Verification: targeted readback / Preview / breakpoints / states actually checked
- Outcome: Pass / Partial / Blocked
- Later-discovered issue: None, or evidence found in a later task
- Correction: None, pending, or what repaired the issue
- Workflow candidate: None, or a possible Router / Skill / Reference / validator improvement
```

## Evidence rules

- Keep `Request`, `Actions`, and `Verification` distinct. An Agent statement that work completed is not verification.
- Record observable facts and durable references; do not store internal reasoning, full chats, raw tool output, session IDs, node dumps, or repeated progress narration.
- Keep the entry short enough that writing it is a natural closing action, not a second deliverable.
- A `Workflow candidate` is not automatically a new rule. Promote it only after a repeated pattern or a reviewed high-impact failure.
- During retrospective, read only the relevant project, date range, or failure class. Summaries belong in `reviews/`; ordinary construction still starts from `AGENTS.md` and current project state.
