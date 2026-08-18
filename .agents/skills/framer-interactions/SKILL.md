---
name: framer-interactions
description: "Secondary repository reasoning for native Framer motion and interaction: Variants, Overlays, Lightbox, menus, cursor previews, scroll effects, transitions, and reduced motion. Use when the main risk is trigger/target routing, motion responsibility, pointer versus touch behavior, or advanced interaction fidelity. For live Canvas work, first complete official $framer setup, session, and project task-map routing; this Skill never replaces the platform connection. Do not use for static layout-only changes or final QA."
---

# Framer Interactions

Use the smallest native pattern that communicates hierarchy, story, feedback, or state change.

## Platform gate

For any live Canvas read or write, first complete the repository `Live Framer Canvas Gate`, using **required elevated permissions** for every Framer CLI command from the first attempt: successful `npx @framer/agent@latest setup`, official `$framer` Skill, successful `npx @framer/agent@latest session new "<url-or-id>"`, generated `projects/<safeProjectId>/index.md` task-map routing, then a targeted `npx @framer/agent@latest exec -s <sessionId>` live-tree readback. Any error means **Gate remains closed**. Before implementation, show the user a concise **Framer Agent gate receipt**. This Skill is secondary reasoning only; never substitute Browser / Playwright / Computer Use. Repo-only planning or documentation skips the Gate.

## Audit the existing behavior

1. Inspect the live trigger, target, current transition, variants, effects, and breakpoint-specific behavior.
2. Check whether the interaction or an equivalent component already exists before creating one.
3. Identify the interaction's purpose in one sentence. If it has no communicative purpose, omit it.
4. Preserve approved project motion language. Generic motion defaults never override the current Canvas or user direction.
5. On second or later revisions, apply [change-control.md](../../../framer/basic/workflows/change-control.md) before writing.

## Select the native model

- Disclosure or in-place expansion: paired `Closed / Open` or breakpoint-specific Variants.
- Anchored menu, dropdown, or popover: Relative Overlay when the anchor relationship matters.
- Simple image enlargement: Lightbox Effect.
- True page-level modal: Fixed Overlay outside ComponentNode scope.
- Hover feedback: Gesture Variant with identical external geometry.
- Cursor preview or fixed reel: use the verified advanced pattern only when desktop pointer behavior is explicitly valuable.

Use Custom Code only when native Framer cannot satisfy the approved interaction and the user authorizes the added maintenance/performance cost.

## Protect state and breakpoints

- Bind every trigger to the exact target state for the same breakpoint.
- Keep content differences in Properties and state differences in Variants.
- Do not let Phone inherit hover-only access to information. Transform or remove Desktop pointer behavior for touch.
- Preserve keyboard operation, visible focus, logical reading order, and a usable static/reduced-motion result.
- Motion may animate presentation, not change the only route to content.
- Keep fixed viewport/slide/window geometry stable when pixel offsets drive the animation; verify the external Page Instance at first, middle, last, and one width change.

## Verify after implementation

1. Read back trigger, target, route, transition, effect scope, and representative instances.
2. Test the actual interaction when live behavior cannot be proven structurally. Use one necessary Preview path or request focused user visual confirmation for advanced behavior.
3. Verify pointer, touch, keyboard, and Reduced Motion paths that apply.
4. Invoke `framer-qa` only after the interaction is implemented.

## Conditional references

- Native selection, motion, overlay, and Lightbox details: relevant headings in [motion-design.md](../../../framer/basic/patterns/motion-design.md)
- Fast pattern decision: [pattern-recipes.md](../../../framer/basic/patterns/pattern-recipes.md)
- Navbar drawer and relative menu: [navbar-footer.md](../../../framer/basic/patterns/navbar-footer.md)
- A specific advanced device: select one document through [advance-design/README.md](../../../framer/advance-design/README.md)
- Any screenshot, Gallery image, crop, or cursor-preview asset: read [image-workflow.md](../../../framer/basic/workflows/image-workflow.md) before viewing
- Marketplace interaction replacement stress: [marketplace-guidelines.md](../../../framer/basic/standards/marketplace-guidelines.md)
