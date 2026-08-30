# Summit Roofing Page Checklist Index

This directory turns the approved Summit Roofing site plan into page-by-page Framer execution contracts. A fresh chat must start from the small current manifest and this index, then load only the active page Checklist and its directly routed sources.

## Status Vocabulary

- `To do`: The page scope is approved, but its page Checklist or implementation is not complete.
- `In progress`: The page is being built vertically by Section or Part.
- `Fix Required`: A required check failed and must be repaired before the next Part.
- `Blocked`: A real fact, asset, service, permission or destination is missing.
- `Pass`: The page passed its required readback, Preview and Page Done checks.

## Fresh-Session Re-entry

For a new chat with no prior conversation context:

```text
Read Website-lab/AGENTS.md
→ read ../PROJECT.md as current project truth
→ read this index
→ read the approved site overview only when page scope or build order is needed
→ read only the active page Checklist and its linked request record
→ if live Canvas work is authorized, complete the official Framer Agent gate
→ targeted live readback of the active page and shared dependencies
→ declare current Part, Add / Reuse / Modify / No-op choice, exclusions and required verification
→ implement one Part
→ route to the applicable sections of ../../../framer/checklist.md
→ readback + Preview + repair + status synchronization
```

Do not use chat memory, the reference website or historical records as current implementation truth. Current live Canvas evidence outranks an older Checklist state, while the user-approved direction in `PROJECT.md` continues to control what may be changed.

## Mandatory Page-Planning Gate

Before building any new buyer-facing page:

1. Inspect the current Canvas and shared systems after completing the official Framer Agent gate.
2. Create or update exactly one long-lived page contract at `checklist/<page-slug>.md`.
3. Keep any later multi-point request verbatim in `checklist/<page-slug>/<date>-<request-name>.md`; do not merge it into the page contract.
4. Make the page contract self-contained enough for a fresh chat to identify the page role, narrative, Sections, images, reusable systems, responsive transformation, interaction, SEO, validation path and blockers.
5. Show the planned page Checklist to the user and wait for explicit confirmation before the first Canvas write for that page.
6. After confirmation, keep the unstarted page `To do`; change it to `In progress` only when the first declared Canvas Part begins.
7. Do not create all remaining page contracts in advance. Plan the next page only when it becomes the active page, so its contract can incorporate the latest verified shared system and completed-page lessons.

Every page contract must include all 16 required categories defined in [Framer Part Completion Checklist — project folder standard](../../../framer/checklist.md#项目级-checklist-文件夹规范). It must be page-specific rather than a copy of the generic evaluator.

## Approved Master Plan

- [Site expansion planning record](./site/2026-08-26-site-expansion-planning.md) — approved Sitemap, page roles, build order, image allocation, Missing facts and project-wide boundaries.
- This master record does not authorize skipping a page-specific Checklist.
- Baker Roofing is a reference for information hierarchy and page roles only; it is not current-state evidence or a structural blueprint.

## Page Index

| Build order | Page | Path | Page contract | Current status |
|---:|---|---|---|---|
| Existing | Home | `/` | Existing Home request records in [`home/`](./home/) | Pass for completed Home scope; final Marketplace publication remains blocked |
| 1 | Services | `/services` | [services.md](./services.md) — implemented and structurally QA-checked; final destinations and bounded visual evidence remain recorded | In progress |
| 2 | Repair & Maintenance | `/services/repair-maintenance` | `repair-maintenance.md` — create and confirm before Canvas work | To do |
| 3 | Roof Replacement | `/services/roof-replacement` | `roof-replacement.md` — create and confirm before Canvas work | To do |
| 4 | New Construction | `/services/new-construction` | `new-construction.md` — create and confirm before Canvas work | To do |
| 5 | Storm Damage Repair | `/services/storm-damage-repair` | `storm-damage-repair.md` — create and confirm before Canvas work | To do |
| 6 | Projects | `/projects` | `projects.md` — create and confirm before Canvas work | To do |
| 7 | Project Detail | `/projects/:Projects` | `project-detail.md` — create and confirm before Canvas work | To do |
| 8 | About | `/about` | `about.md` — create and confirm before Canvas work | To do |
| 9 | Contact | `/contact` | `contact.md` — create and confirm before Canvas work | To do |
| 10 | Insights | `/insights` | `insights.md` — create and confirm before Canvas work | To do |
| 11 | Insight Detail | `/insights/:Insights` | `insight-detail.md` — create and confirm before Canvas work | To do |

`/reveal-text-test` is development-only and remains outside this buyer-facing build order pending its separate retain/remove decision.

## Shared Foundation Gate

Recheck these shared responsibilities before presenting a page Checklist for confirmation, and again before the page reaches `Pass`:

- [ ] Reuse the current shared `Site Shell`, Navbar and Footer; do not create page copies.
- [ ] Reuse existing Button, Service Row, Process Step, Project Card and Article Card contracts where their responsibilities match.
- [ ] Preserve current shared Color and Text Styles, zero-radius geometry and established focus/motion direction.
- [ ] Confirm navigation destinations against pages that actually exist; do not publish dead routes as finished links.
- [ ] Preserve one clear H1, logical H2/H3 order, visible focus, keyboard order and non-hover-only information.
- [ ] Verify Reduced Motion and touch-safe states.
- [ ] Keep contact facts, project claims, credentials, warranties, response times and service areas visibly `Demo` or `Missing` until approved.
- [ ] Verify favicon, Open Graph, image licensing and buyer editing instructions before Marketplace submission.

## Mandatory Part Closure

For every Section, Component, interaction, breakpoint, CMS batch, Form state or Page:

```text
Build one declared Part
→ open the applicable evaluator sections in ../../../framer/checklist.md
→ targeted readback and necessary Preview path
→ mark Pass / Fix Required / Blocked
→ repair the current class of failures
→ recheck the affected scope
→ update the page Latest Part Result
→ update the single current Recovery owner in ../PROJECT.md#14-recovery
→ only then begin the next Part
```

## Latest Part Result Format

Each active page contract ends with one replaceable block:

```markdown
## Latest Part Result

Scope: Section / Component / Page
Status: Pass / Fix Required / Blocked

Pass:
- ...

Fix Required:
- ...

Blocked:
- ...

Verified widths:
- ...

Verified paths:
- ...

Shared components affected:
- ...

Recovery:
- Canonical current pointer: `../PROJECT.md#14-recovery`
- This Part result date:
```

Do not append a second current-session diary. Completed historical evidence stays in the request-specific record or future History owner.

## Canonical References

- Current project manifest: [PROJECT.md](../PROJECT.md)
- Current Build / QA: [PROJECT.md §12](../PROJECT.md#12-current-status)
- Active decisions: [PROJECT.md §13](../PROJECT.md#13-decisions-and-exceptions)
- Current recovery pointer: [PROJECT.md §14](../PROJECT.md#14-recovery)
- Active Checklist pointer: [PROJECT.md §15](../PROJECT.md#15-checklist-and-change-control)
- Repository rules: [`AGENTS.md`](../../../AGENTS.md)
- Framer task router: [`framer/README.md`](../../../framer/README.md)
- Mandatory Part evaluator and page-file contract: [`framer/checklist.md`](../../../framer/checklist.md)
- Change control: [`change-control.md`](../../../framer/basic/workflows/change-control.md)
- Image workflow: [`image-workflow.md`](../../../framer/basic/workflows/image-workflow.md)
- Preflight: [`preflight-audit.md`](../../../framer/basic/workflows/preflight-audit.md)
