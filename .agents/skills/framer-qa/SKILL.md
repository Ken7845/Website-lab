---
name: framer-qa
description: "Secondary repository evaluation for a completed Framer Section, Component contract, interaction, breakpoint, Page, or Website through targeted evidence, ownership symmetry, responsive/accessibility checks, Marketplace stress, preflight, and status updates. Use after implementation, for audits or diagnoses, or before delivery. For live Canvas work, first complete official $framer setup, session, and task-map routing. It is a verifier, not a design generator."
---

# Framer QA

Evaluate the implemented scope against evidence. Do not redesign from a memorized checklist.

## Platform gate

First use the [Framer dispatcher](../../../framer/README.md#2-只选一个-primary-repo-skill), including its ownership precedence and task mode. For live reads or writes, complete the canonical [Live Framer Canvas Gate](../../../AGENTS.md#live-framer-canvas-gate); **Gate remains closed** until its evidence is complete. Show the **Framer Agent gate receipt** before implementation. This Skill supplies reasoning, not a platform connection. Repository-only work skips connection.

## Define the audit

1. Name the exact scope: Section, Component, interaction, breakpoint, Page, or Website.
2. Declare Audit only or Repair, exclusions and the active constraint lock. Audit only reports issues; it does not mutate the target.
3. Inspect the current implementation before reading detailed QA material.
4. If the scope created, duplicated, or reassigned a reusable Component, locate its active `Component Requirement Contract`; apply the [contract lifecycle and legacy policy](../../../framer/basic/workflows/change-control.md#contract-lifecycle). Missing Required contracts in schema 1 are Fix Required; missing later-introduced contracts in a legacy audit are an evidence limitation, not a redesign instruction.
5. If the scope created a Page, substantially redesigned a Section, differentiated sibling pages, or promised a “different layout,” locate its active `Visual Direction Contract`; apply the same lifecycle policy. New work needs Ready direction; a legacy audit preserves dated evidence and labels uncertainty.
6. Locate applicable headings with `rg -n '^##|^###'` and load only those sections from [framer/checklist.md](../../../framer/checklist.md).
7. Add Marketplace checks only for Marketplace work.

## Evidence ladder

Use the canonical [evidence selection](../../../framer/basic/workflows/image-workflow.md#evidence-selection) for property, composition and runtime claims. User confirmation counts only for the explicitly observed scope. Structure, diagnostics and successful writes do not prove visual or runtime Pass. Observe the workflow's residency, budget and two-attempt stopping limits before visual operations.

## Targeted matrix

Check only what the scope can affect:

- Existence and duplication: the requested function appears once where intended; no redundant Section or CTA intent was added.
- Structure and ownership: Definition → Instance → Breakpoint Override; full-bleed, wrapper, gutter, and component boundaries are coherent. Page root, full-bleed Section, and senior structural parents remain fluid; `max-width` belongs to the deepest valid max-width owner. A bounded-canvas exception passes only with approved intent, a separate full-viewport background owner, and narrow/wide evidence.
- Width-policy validity: check [Max-width ownership](../../../framer/basic/standards/website-baseline.md#max-width-ownership) and active user direction before accepting the planned contract. Matching an incorrectly capped contract is still Fix Required; generic lint suggestions do not authorize restoring caps.
- Contract symmetry: for every Component concern, compare planned Decision / Owner with the actual Canvas owner, then replace planned readback/Preview proof with evidence or an explicit Blocked reason.
- Content and facts: Approved/Draft/Demo/Missing states remain honest; links and labels lead to real destinations.
- Breakpoints: actual Desktop, Tablet, Phone, and any project-specific widths are inspected; narrow layouts transform rather than mechanically shrink.
- Components/interactions: Properties, state routes, trigger targets, shared behavior, touch behavior, and Reduced Motion remain intact.
- Accessibility: semantic headings, Alt, contrast, visible focus, keyboard path, touch targets, and reading order.
- Delivery: SEO, performance, licensing, editing path, error/loading/empty states, and Marketplace replacement pressure when in scope.
- Visual-contract symmetry: compare Design Read, Preserve / Transform / Avoid, sibling delta, Section composition, colour rhythm, asset map and responsive transformation against actual evidence. A different structure is not a visual Pass if it abandons the approved project language.
- Cross-page differentiation: evaluate the site's layout-family distribution rather than requiring every Section to be unique. Functionally justified reuse of Contact, CTA, form and shared-system layouts may Pass; using the same Hero or complete page composition across every sibling page is site-wide layout monoculture and must fail. Treat numeric diversity examples as heuristics, not quotas. Verify that each image still performs its content-relative image role instead of acting as an interchangeable skin.

Use relevant headings only from:

- [website-baseline.md](../../../framer/basic/standards/website-baseline.md)
- [preflight-audit.md](../../../framer/basic/workflows/preflight-audit.md)
- [marketplace-guidelines.md](../../../framer/basic/standards/marketplace-guidelines.md), only when applicable

## Close the loop

Classify the result:

- `Pass`: evidence proves the scoped contract.
- `Fix Required`: an in-scope issue needs repair. In Repair mode batch-fix and recheck; in Audit only mode report the concrete repair without writing.
- `Blocked`: a real fact, asset, permission, service, or unavailable evidence prevents completion.

For Page-level visual work, report `Structural status` and `Visual status` separately; overall `Pass` requires both. Clean diagnostics, successful writes and targeted structure cannot prove aesthetic composition. Use one efficient full-page or compiled Desktop/Phone view when the claim concerns whole-page rhythm; a target Section screenshot cannot prove it. If required visual evidence is unavailable, mark visual status `Blocked` or `Fix Required` rather than implying completion.

For an active Component Requirement Contract, every applicable proof cell must end as evidenced `Pass`, explicit `Fix Required`, reasoned `Blocked` or `N/A — reason`; an unchecked or planned-only row is not completion. When the user asks to finish the current Part or complete it in one pass, do not stop after implementation while an authorized, executable checklist item remains unclassified.

Update project state by responsibility:

- Current build/QA truth → `STATUS.md` (replace stale status; do not append a diary).
- Active continuation pointer only → `RECOVERY.md`.
- A genuinely new why-decision → `DECISIONS.md`.
- Completed or retired implementation narrative → `HISTORY.md` or request-specific Checklist.

Before the final response, complete [observation closeout](../../../history/workflow-observations/README.md#closeout) for eligible outcomes. Read back the saved entry and Current Status receipt in the actual knowledge repository; a Partial/Blocked implementation still needs its record.

Report only the outcome, verified widths/paths, fixes, blockers, and known limits. Never mark a scope complete because Desktop merely looks finished.
