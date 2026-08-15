---
name: framer-qa
description: "Evaluate a completed Framer Section, Component, interaction, breakpoint, Page, or Website through targeted readback, visual evidence, responsive/accessibility checks, Marketplace stress, preflight, and recovery/status updates. Use after implementation, for explicit audits or diagnoses, or before delivery/publishing. This is an evaluator and verifier, not a design generator; do not preload it before ordinary creative work."
---

# Framer QA

Evaluate the implemented scope against evidence. Do not redesign from a memorized checklist.

## Define the audit

1. Name the exact scope: Section, Component, interaction, breakpoint, Page, or Website.
2. Record exclusions and the user's active constraint lock.
3. Inspect the current implementation before reading detailed QA material.
4. Locate applicable headings with `rg -n '^##|^###'` and load only those sections from [framer/checklist.md](../../../framer/checklist.md).
5. Add Marketplace checks only for Marketplace work.

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
- Content and facts: Approved/Draft/Demo/Missing states remain honest; links and labels lead to real destinations.
- Breakpoints: actual Desktop, Tablet, Phone, and any project-specific widths are inspected; narrow layouts transform rather than mechanically shrink.
- Components/interactions: Properties, state routes, trigger targets, shared behavior, touch behavior, and Reduced Motion remain intact.
- Accessibility: semantic headings, Alt, contrast, visible focus, keyboard path, touch targets, and reading order.
- Delivery: SEO, performance, licensing, editing path, error/loading/empty states, and Marketplace replacement pressure when in scope.

Use relevant headings only from:

- [website-baseline.md](../../../framer/basic/standards/website-baseline.md)
- [preflight-audit.md](../../../framer/basic/workflows/preflight-audit.md)
- [marketplace-guidelines.md](../../../framer/basic/standards/marketplace-guidelines.md), only when applicable

## Close the loop

Classify the result:

- `Pass`: evidence proves the scoped contract.
- `Fix Required`: an in-scope issue can be repaired now; batch-fix the class and recheck only affected evidence.
- `Blocked`: a real fact, asset, permission, service, or unavailable evidence prevents completion.

Update project state by responsibility:

- Current build/QA truth → `STATUS.md` (replace stale status; do not append a diary).
- Active continuation pointer only → `RECOVERY.md`.
- A genuinely new why-decision → `DECISIONS.md`.
- Completed or retired implementation narrative → `HISTORY.md` or request-specific Checklist.

Report only the outcome, verified widths/paths, fixes, blockers, and known limits. Never mark a scope complete because Desktop merely looks finished.
