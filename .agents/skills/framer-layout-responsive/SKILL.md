---
name: framer-layout-responsive
description: "Secondary repository reasoning for auditing, creating, or modifying Framer layouts across breakpoints. Use for composition, spacing, stacking, responsive transformation, width ownership, overflow, regressions, or reworking a section. For live Canvas work, first complete official $framer setup, session, and project task-map routing; this Skill never replaces the platform connection. Do not use for isolated component-state architecture, interaction-only work, or final QA unless layout is primary."
---

# Framer Layout and Responsive

Preserve the page's existing design logic while giving each breakpoint an intentional composition.

## Platform gate

First use the [Framer dispatcher](../../../framer/README.md#2-只选一个-primary-repo-skill), including its ownership precedence and task mode. For live reads or writes, complete the canonical [Live Framer Canvas Gate](../../../AGENTS.md#live-framer-canvas-gate); **Gate remains closed** until its evidence is complete. Show the **Framer Agent gate receipt** before implementation. This Skill supplies reasoning, not a platform connection. Repository-only work skips connection.

## Start from evidence

1. Read the repository router and the current project's `PROJECT.md`. Load the manifest-declared current-status owner or `RECOVERY.md` only when status or continuation matters.
2. Inspect the actual page, target section, adjacent sections, and Desktop/Tablet/Phone implementations before proposing a change.
3. Search for an existing section, CTA, or component with the same function. Decide `Add`, `Reuse`, `Modify`, or `No-op` before creating anything.
4. Reconcile live implementation, current docs, and the user's request. Live implementation and explicit user direction outrank historical plans.
5. Identify recurring page patterns: alignment edges, gutters, type relationships, image ratios, section transitions, full-bleed behavior, and intentional exceptions.

Do not load the full Checklist or all Framer references before designing.

## Build a constraint lock

For a second or later revision of the same Part, read [change-control.md](../../../framer/basic/workflows/change-control.md) and record the short constraint lock before writing. Treat new feedback as an addition or correction unless the user explicitly replaces the earlier direction.

For a new Page, substantial Section redesign, multi-page differentiation, or a request centered on a “different layout,” require a `Ready` [Visual Direction Contract](../design-taste/SKILL.md#compile-a-visual-direction-contract) before writing. This Skill consumes that direction; it does not invent a new aesthetic from Stack/Grid mechanics.

Before changing composition, compare the target with adjacent Sections and relevant sibling pages. Preserve the named typography, palette roles, geometry, spacing logic and image behavior; transform only the contract’s named topology, proportion, alignment, density, media sequence or hierarchy. A structurally different layout that breaks the approved visual language is `Fix Required`.

## Resolve width ownership

Trace the full chain:

```text
Page breakpoint root
→ Section
→ inner wrapper
→ component instance
→ component root
→ media/text child
```

- Keep the Page breakpoint root, outer Page Content, full-bleed Section, and any senior structural parent whose job is distributing available width fluid with Fill / `1fr`. Do not place `max-width` on them by default or automatically cap the first inner wrapper; trace to the **deepest valid max-width owner**—a local Content Wrapper, reading column, specific Grid, list, or component that genuinely needs the constraint. A deliberately bounded canvas is an exception only when approved by the project/user, wrapped by a separate full-viewport background owner, and verified across the relevant narrow and wide widths. See `framer/basic/standards/website-baseline.md#5-layout-与共享结构`.
- Let exactly one layer own horizontal gutters. Do not repair child alignment by stacking padding at multiple levels.
- Prefer `Fill / 1fr` for page instances when the parent owns available width. Do not use `100% Relative` to hide an unclear ownership chain.
- Fixed-coordinate tracks, reels, viewports, slides, and windows keep their internal fixed geometry; make the surrounding page responsive instead.

Read [token-saving.md](../../../framer/basic/workflows/token-saving.md) only for the targeted-read, three-layer diagnosis, width-chain, batching, or recovery section needed by the task.

## Transform each breakpoint

- Desktop composition intent is not a cross-breakpoint command.
- Inspect the actual authored breakpoints; do not assume only three exist.
- For Tablet and Phone, independently choose order, stack direction, visibility, crop, focal point, gap, type wrap, and touch affordance.
- Preserve semantic reading order and essential navigation.
- Test narrow and wide stress widths relevant to the project, commonly `320 / 390 / 810 / 1200 / 1440+`, without treating those values as universal authored breakpoints.
- Avoid horizontal overflow and accidental black/white bands caused by mismatched full-bleed ownership.

## Implement and verify

1. Make the smallest coherent batch inside the authorized Section/Page.
2. Read back only the changed root, its parent width chain, and affected breakpoint instances. For a `max-width` fix, prove which node is the deepest valid owner and that every senior structural parent remains fluid.
3. Verify that adjacent sections, shared components, and untouched breakpoints remain unchanged.
4. Invoke `framer-qa` after implementation for targeted evaluation. Read only the applicable Checklist sections then.

## Conditional references

- Common layout choice: [pattern-recipes.md](../../../framer/basic/patterns/pattern-recipes.md)
- Current-scope completion contract: relevant headings only in [website-baseline.md](../../../framer/basic/standards/website-baseline.md)
- Image inspection, crop, screenshot, or visual QA: read [image-workflow.md](../../../framer/basic/workflows/image-workflow.md) before the first image view
- Marketplace replacement stress: [marketplace-guidelines.md](../../../framer/basic/standards/marketplace-guidelines.md)
- Advanced fixed-coordinate pattern: select one document through [advance-design/README.md](../../../framer/advance-design/README.md)
