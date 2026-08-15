---
name: framer-layout-responsive
description: "Audit, create, or modify Framer page and section layouts across Desktop, Tablet, Phone, and project-specific breakpoints. Use for composition, spacing, stacking, responsive transformation, width ownership, full-bleed/max-width issues, overflow, breakpoint regressions, or adding/reworking a section in an existing Framer page. Do not use for isolated component-state architecture, interaction-only work, or final QA unless layout is the primary problem."
---

# Framer Layout and Responsive

Preserve the page's existing design logic while giving each breakpoint an intentional composition.

## Start from evidence

1. Read the repository router and the current project's `PROJECT.md`. Load `STATUS.md` or `RECOVERY.md` only when status or continuation matters.
2. Inspect the actual page, target section, adjacent sections, and Desktop/Tablet/Phone implementations before proposing a change.
3. Search for an existing section, CTA, or component with the same function. Decide `Add`, `Reuse`, `Modify`, or `No-op` before creating anything.
4. Reconcile live implementation, current docs, and the user's request. Live implementation and explicit user direction outrank historical plans.
5. Identify recurring page patterns: alignment edges, gutters, type relationships, image ratios, section transitions, full-bleed behavior, and intentional exceptions.

Do not load the full Checklist or all Framer references before designing.

## Build a constraint lock

For a second or later revision of the same Part, read [change-control.md](../../../framer/basic/workflows/change-control.md) and record the short constraint lock before writing. Treat new feedback as an addition or correction unless the user explicitly replaces the earlier direction.

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

- A full-bleed outer Section should not inherit an unrelated `max-width`; constrain an intentional inner wrapper.
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
2. Read back only the changed root, its parent width chain, and affected breakpoint instances.
3. Verify that adjacent sections, shared components, and untouched breakpoints remain unchanged.
4. Invoke `framer-qa` after implementation for targeted evaluation. Read only the applicable Checklist sections then.

## Conditional references

- Common layout choice: [pattern-recipes.md](../../../framer/basic/patterns/pattern-recipes.md)
- Current-scope completion contract: relevant headings only in [website-baseline.md](../../../framer/basic/standards/website-baseline.md)
- Image inspection, crop, screenshot, or visual QA: read [image-workflow.md](../../../framer/basic/workflows/image-workflow.md) before the first image view
- Marketplace replacement stress: [marketplace-guidelines.md](../../../framer/basic/standards/marketplace-guidelines.md)
- Advanced fixed-coordinate pattern: select one document through [advance-design/README.md](../../../framer/advance-design/README.md)
