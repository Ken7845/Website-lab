# Workflow Observations

This directory records lightweight evidence from real website-construction work so later retrospectives can improve routing, Skills, references, and validation. **Do not preload** these files during ordinary project work.

## When to record

Write one compact entry after implementation and targeted QA for a meaningful Page, Section, reusable Component, Interaction, multi-breakpoint Part, or task that exposes a reusable workflow failure.

Do not record routine copy, link, naming, or isolated spacing fixes unless they reveal a broader failure. Do not interrupt implementation to maintain a diary. If a task is interrupted, use the project's `RECOVERY.md`; write an observation only after a meaningful outcome exists.

## Where to record

Use one append-only file per project, using the existing linked file or the lowercase kebab-case form of its `content-library/` project slug:

```text
history/workflow-observations/
├── aurelia.md
├── summit-roofing.md
└── <project-slug>.md
```

Do not create a file after every Prompt. Multiple Prompts, corrections, and follow-ups that belong to one meaningful construction task become one brief closing entry in that project's file. Later discoveries append to the same entry rather than creating a competing account. Cross-project workflow work may use `repository.md` only when no single project owns it. These files are retrospective evidence, not current project truth.

## Closeout

Before the final response for an eligible task, complete this closing step after implementation and targeted QA, including a meaningful `Partial` or `Blocked` outcome. A missing staging URL blocks runtime proof, not the repository record. Do not defer the observation until the whole website passes or the user reminds you.

1. Resolve the knowledge repository from the user's project and `PROJECT.md`, not the chat's working directory. Follow the project's History link; read only the relevant tail at closeout. Do not create a second log or a loose design note in another workspace.
2. Append the compact result to the existing project observation file. Reuse the same task's closing entry for follow-ups by appending a correction; preserve earlier facts. Follow an explicit user request for prompt-level history when present.
3. Replace stale Status / Recovery values and active contract decisions as needed. An appended observation alone does not synchronize current state; use dated evidence and `Needs refresh` when reconciling another chat without a new Canvas readback.
4. In the existing canonical Current Status owner, record `Closeout schema: 1` and `Observation: Recorded —` followed by a local Markdown link to the saved entry heading. For an ineligible routine fix use `Observation: N/A — <concrete scope reason>`; if the record could not be written use `Observation: Blocked — <actual write blocker>`. Do not add a new file just for this receipt.
5. Read back the written entry and receipt before claiming history is updated. The final response may link the record; do not expose internal node or session IDs. A promised future write or an output from a Canvas tool is not a history write.

This is a completion check, not a new startup approval gate or a reason to preload history. If interrupted before a meaningful outcome, save Recovery and close the observation when that outcome is available. The repository validator checks declared closeout receipts and their local entry targets; it cannot infer an omitted live task or prove Canvas behavior.

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
- During retrospective, read only the relevant project, date range, or failure class. Repository retrospective summaries belong in [history/repository](../repository/); ordinary construction still starts from `AGENTS.md` and current project state.
