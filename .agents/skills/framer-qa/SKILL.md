---
name: framer-qa
description: "Secondary repository evaluation for a completed Framer Section, Component contract, interaction, breakpoint, Page, or Website through targeted evidence, ownership symmetry, responsive/accessibility checks, Marketplace stress, preflight, and status updates. Use after implementation, for audits or diagnoses, or before delivery. For live Canvas work, first complete official $framer setup, session, and task-map routing. It is a verifier, not a design generator."
---

# Framer QA

Evaluate the implemented scope against evidence. Do not redesign from a memorized checklist.

## Platform gate

For any live Canvas read or write, first complete the repository `Live Framer Canvas Gate`, using **required elevated permissions** for every Framer CLI command from the first attempt: successful `npx @framer/agent@latest setup`, official `$framer` Skill, successful `npx @framer/agent@latest session new "<url-or-id>"`, generated `projects/<safeProjectId>/index.md` task-map routing, then a targeted `npx @framer/agent@latest exec -s <sessionId>` live-tree readback. Any error means **Gate remains closed**. Before implementation, show the user a concise **Framer Agent gate receipt**. This Skill is secondary reasoning only; never substitute Browser / Playwright / Computer Use. Repo-only planning or documentation skips the Gate.

## Define the audit

1. Name the exact scope: Section, Component, interaction, breakpoint, Page, or Website.
2. Record exclusions and the user's active constraint lock.
3. Inspect the current implementation before reading detailed QA material.
4. If the scope created, duplicated, or reassigned a reusable Component, locate its active `Component Requirement Contract`; absence of the contract is `Fix Required`, not permission to reconstruct ownership from memory.
5. If the scope created a Page, substantially redesigned a Section, differentiated sibling pages, or promised a “different layout,” locate its active `Visual Direction Contract`; missing or `Draft` direction is `Fix Required`.
6. Locate applicable headings with `rg -n '^##|^###'` and load only those sections from [framer/checklist.md](../../../framer/checklist.md).
7. Add Marketplace checks only for Marketplace work.

## Evidence ladder

Use the least expensive evidence that proves the claim:

1. Targeted structural readback for names, styles, properties, links, variants, dimensions, and ownership.
2. Targeted Canvas screenshot for static composition when needed.
3. One necessary live Preview path for behavior, routing, responsive layout, keyboard, or focus that structure cannot prove.
4. Focused user visual confirmation for advanced motion/cursor/hover when direct evidence remains unavailable.

Do not repeatedly capture the same state. Do not treat a successful write command as proof.

For any local image, screenshot, Preview capture, Gallery, crop, upload, or Alt audit, read [image-workflow.md](../../../framer/basic/workflows/image-workflow.md) before the first visual operation. Its visual budget, local-residency checks, two-attempt limit, and structural fallback are hard safety rules.

## Targeted matrix

Check only what the scope can affect:

- Existence and duplication: the requested function appears once where intended; no redundant Section or CTA intent was added.
- Structure and ownership: Definition → Instance → Breakpoint Override; full-bleed, wrapper, gutter, and component boundaries are coherent.
- Contract symmetry: for every Component concern, compare planned Decision / Owner with the actual Canvas owner, then replace planned readback/Preview proof with evidence or an explicit Blocked reason.
- Content and facts: Approved/Draft/Demo/Missing states remain honest; links and labels lead to real destinations.
- Breakpoints: actual Desktop, Tablet, Phone, and any project-specific widths are inspected; narrow layouts transform rather than mechanically shrink.
- Components/interactions: Properties, state routes, trigger targets, shared behavior, touch behavior, and Reduced Motion remain intact.
- Accessibility: semantic headings, Alt, contrast, visible focus, keyboard path, touch targets, and reading order.
- Delivery: SEO, performance, licensing, editing path, error/loading/empty states, and Marketplace replacement pressure when in scope.
- Visual-contract symmetry: compare Design Read, Preserve / Transform / Avoid, sibling delta, Section composition, colour rhythm, asset map and responsive transformation against actual evidence. A different structure is not a visual Pass if it abandons the approved project language.
- Cross-page differentiation: for a new Page, compare masthead paradigm, layout-family sequence, colour-block rhythm, image reuse, heading/body proportion, whitespace, repeated process treatment and CTA composition with the relevant siblings.

Use relevant headings only from:

- [website-baseline.md](../../../framer/basic/standards/website-baseline.md)
- [preflight-audit.md](../../../framer/basic/workflows/preflight-audit.md)
- [marketplace-guidelines.md](../../../framer/basic/standards/marketplace-guidelines.md), only when applicable

## Close the loop

Classify the result:

- `Pass`: evidence proves the scoped contract.
- `Fix Required`: an in-scope issue can be repaired now; batch-fix the class and recheck only affected evidence.
- `Blocked`: a real fact, asset, permission, service, or unavailable evidence prevents completion.

For Page-level visual work, report `Structural status` and `Visual status` separately; overall `Pass` requires both. Clean diagnostics, successful writes and targeted structure cannot prove aesthetic composition. Use one efficient full-page or compiled Desktop/Phone view when the claim concerns whole-page rhythm; a target Section screenshot cannot prove it. If required visual evidence is unavailable, mark visual status `Blocked` or `Fix Required` rather than implying completion.

For an active Component Requirement Contract, every row must end as evidenced `Pass` or reasoned `Blocked`; an unchecked or planned-only row is not completion. When the user asks to finish the current Part or complete it in one pass, do not stop after implementation while an authorized, executable checklist item remains unclassified.

Update project state by responsibility:

- Current build/QA truth → `STATUS.md` (replace stale status; do not append a diary).
- Active continuation pointer only → `RECOVERY.md`.
- A genuinely new why-decision → `DECISIONS.md`.
- Completed or retired implementation narrative → `HISTORY.md` or request-specific Checklist.

Report only the outcome, verified widths/paths, fixes, blockers, and known limits. Never mark a scope complete because Desktop merely looks finished.
