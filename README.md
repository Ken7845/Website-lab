# Website-lab

Website-lab is a knowledge base for website design, project facts, and Framer delivery, built for humans and AI Agents. Its goal is not to make Agents read more, but to give each type of information one authoritative location so website work can be resumed accurately after interruptions, across new Sessions, or through multiple rounds of revision.

## Knowledge Base Version

- Repository version: `Website_Lab_V2.2.3`
- Current release: `V2.2.3`
- Release source: `main`; project-specific Content Library data remains outside Git tracking
- Previous release: `V2.2.2` (source `543afa3`)
- Architecture base: `v2.0.0`
- Released: 2026-10-15
- Updated: 2026-10-15
- Scope: knowledge routing, authorization, current-state ownership, contract lifecycle, evidence requirements and maintenance validation; preserves the existing design system and website content.
- Current revision: retains the V2.2.2 architecture; adds a forward-only English repository-writing policy with preservation exceptions, translates only `README.md` into English without authorizing a bulk repository translation, and makes project-specific Content Library workspaces local-only while keeping reusable knowledge and Skills in Git.
- Previous release notes: [Website_Lab V2.2.2](history/repository/2026-10-13-knowledge-base-v2.2.2.md)
- Architecture migration record (v2.1.0 base): [Website-lab Visual Workflow Improvement — v2.1.0](history/repository/2026-09-16-visual-workflow-v2.1.0.md)

## Architecture

```text
AGENTS.md
├── Repository-level priorities, minimal-read routing, and permanent hard boundaries
├── .knowledge-validation.json    Immutable archives, migrations, and validation policy
├── .agents/skills/
│   ├── design-taste/             Platform-independent design judgment
│   ├── framer-*/                 Task-selected Framer Skills
│   └── knowledge-maintenance/    Triggered for knowledge audits, writes, migrations, and validation
├── content-library/
│   ├── README.md                 Tracked project-knowledge responsibilities
│   ├── project-manifest-template.md  Tracked reusable manifest template
│   └── <project>/                Local-only project facts, state, contracts, and assets
├── inspiration/
│   └── Creative references organized by website type; never current project state
├── history/                       Retired manuals, migration evidence, and workflow observations; not read by default
└── framer/
    ├── README.md                 The single Framer task router
    ├── basic/                    Stable platform standards, Patterns, and Workflows
    ├── checklist.md              Part / Page / Website acceptance criteria
    └── advance-design/           Verified project-level advanced patterns
```

## Information Ownership

| Information | Authoritative location | Not responsible for |
|---|---|---|
| Repository routing, authorization, and fact boundaries | `AGENTS.md` | Does not duplicate the Framer implementation manual |
| Project goals, Scope, facts, and source index | Local-only `content-library/<project>/PROJECT.md` | Does not store long process logs or enter the public Git repository |
| Current build state | Project `STATUS.md` or PROJECT Current Status | Does not preserve an old-state timeline |
| Durable design decisions and genuine exceptions | Project `DECISIONS.md` or PROJECT Decisions | Does not record every small operation |
| Current recovery point | Project `RECOVERY.md` or PROJECT Recovery | Keeps only one latest checkpoint |
| Closed Prompts, handoffs, and old snapshots | Project `HISTORY.md` / `history/` | Does not override current state |
| Approved page-level and request contracts | Project `checklist/` | Does not replace PROJECT or platform acceptance checks |
| Brand facts, approved copy, and assets | Approved sources linked from PROJECT | Does not infer facts from Inspiration |
| Foundational design judgment | `.agents/skills/design-taste/SKILL.md` | Does not replace brand or platform constraints |
| Framer implementation and acceptance | `framer/basic/`, `framer/checklist.md`, and the selected Framer Skill | Does not decide brand facts |
| Creative references | `inspiration/` | Does not store project current status |
| Retired repository-level manuals | `history/` | Does not participate in current routing or override active rules |
| Lightweight observations from real construction work | `history/workflow-observations/` | Not current state, Recovery, or normal task-start context |
| Knowledge additions, migrations, and structural validation | `.agents/skills/knowledge-maintenance/`, `.knowledge-validation.json` | Does not participate in ordinary website tasks |

When information conflicts, follow the authority order in `AGENTS.md`.

## Starting or Updating a Project

1. Create or update `PROJECT.md` inside `content-library/<project-name>/`.
2. Start a new project from `content-library/project-manifest-template.md`.
3. Provide the website goal, target users, pages and CTA, brand direction, facts, copy, assets, and references.
4. Mark unknown facts as `Missing` and demo facts as `Demo`; do not guess merely to make the source set appear complete.
5. For a large project overview or a long, multi-part construction request, use `framer/basic/workflows/change-control.md` to determine the PROJECT, Checklist, and request records.
6. Keep current state up to date by replacing old values; move old Prompts, handoffs, and snapshots with long-term value into History.

## Current and History

`PROJECT.md`, `STATUS.md`, and `RECOVERY.md` answer “What exists now?”, “How far has the work progressed?”, and “What comes next?”. Replace old values when updating them; do not append chat-style logs to the end of these files.

`DECISIONS.md` stores decisions that still affect future work and marks replaced items as `Superseded`. `HISTORY.md` and `history/` preserve completed material worth tracing. Git tracks ordinary version changes, so a separate copy is not required for every earlier version.

## Workflow Observations

After implementation and targeted QA, a Framer or website task with meaningful construction value may naturally produce one short workflow observation. It records the user request, the route selected by the Agent, what was actually completed, the validation result, and any omissions discovered later. It supports periodic retrospectives and improvements to Routers, Skills, and References; it does not prove current state.

This is not a work-log burden: small copy, link, naming, or single-point spacing fixes are not recorded by default; construction work does not maintain a step-by-step diary; and an observation does not copy the chat, tool output, or internal reasoning. Each project maintains only one short append-only observation file, and multiple Prompts from the same task are combined into one closing entry. Observations live in [`history/workflow-observations/`](history/workflow-observations/README.md). Ordinary tasks must not preload them; only retrospective or knowledge-maintenance work reads them as needed.

## How Agents Use This Repository

Agents start with `AGENTS.md` and read only the local PROJECT, Approved sources, platform rules, and selected Skill required by the current Scope. This README explains the architecture; it is not a second implementation manual. Repository maintenance routes through [knowledge-maintenance](.agents/skills/knowledge-maintenance/SKILL.md); all Framer work routes through the [dispatcher](framer/README.md); local projects follow the [Content Library guide](content-library/README.md); and reference sites begin at the [Inspiration index](inspiration/README.md).

Framer completion criteria and implementation details are managed through these entry points:

- `framer/README.md`
- `.agents/skills/framer-*/SKILL.md`
- `framer/basic/README.md`
- `framer/checklist.md`
- `framer/basic/workflows/change-control.md`
- `framer/basic/workflows/preflight-audit.md`

## Knowledge Write Validation

When adding, moving, deduplicating, or restructuring Basic knowledge, Advanced Design knowledge, project state, a Router, or a Skill, use `knowledge-maintenance` and run the following command before completion:

```bash
python3 .agents/skills/knowledge-maintenance/scripts/validate_repository.py --strict
```

The validator checks active links and anchors, Skill metadata, stale routes, index coverage, immutable archives, repository-wide keywords and precise knowledge contracts in canonical files, current/history hygiene, migration destinations for deleted Markdown, and `git diff HEAD --check`. Ordinary website construction does not preload this maintenance context.

## Laboratory operating reference

[Payment SOP](payment-SOP.md) preserves the personal client-payment reference. It does not authorize transactions or override project facts. Root TODO.md is an empty legacy placeholder, not a current work queue.

## Core Objective

Every delivery must align with the brand and factual content while providing a maintainable structure, correct Desktop / Tablet / Phone behavior, necessary interactions, semantics, and accessibility. The knowledge base itself must also remain maintainable: current state is clear, history does not masquerade as fact, and the next Agent does not need to reconstruct context from chat records.
