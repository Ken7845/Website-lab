---
name: framer-components
description: "Design, inspect, or repair native Framer Components, Variants, Component Properties, Instances, Styles, CMS bindings, Buttons, Navbar/Footer systems, and shared Layout Templates. Use when deciding Component versus Frame, content Properties versus state Variants, instance overrides, shared behavior, naming, or component-owned sizing. Do not use for a page-composition-only change, motion-only task, or final audit."
---

# Framer Components

Build reusable systems only where reuse or state actually exists.

## Inspect before creating

1. Read the current project manifest and inspect the live component list, target page instances, and relevant breakpoints.
2. Search for the same function, CTA intent, or shared shell before creating a component. Decide `Reuse`, `Extend`, `Repair`, `Create`, or `No-op`.
3. Inspect all three layers before diagnosing:

```text
Component Definition
→ Page Instance
→ Breakpoint Override
```

4. For repeated revisions, apply the short constraint lock in [change-control.md](../../../framer/basic/workflows/change-control.md).

## Assign responsibility

- Use a normal Frame for one-off structure.
- Use Component Properties for content and buyer-editable values: text, image, Alt, link, label, visibility, and controlled slots.
- Use Variants for real structural or behavioral states: breakpoint composition, open/closed, selected, loading, or error.
- Use CMS for genuinely repeating and independently managed collections, not merely because seven items exist.
- Keep page instances responsible for content and available width; keep the component root responsible for its internal layout contract.
- Do not create content Variants for each record.
- Do not componentize a one-off section merely to increase component count.

## Preserve behavior and editability

- Reuse existing Style, Button, icon, and navigation systems before adding near-duplicates.
- Keep Button visual padding and hit area inside the Button Component; keep the outer page Stack responsible for placement and available width.
- Bind trigger and target explicitly. Recheck every `SET_VARIANT`, Link Property, Overlay target, scroll target, and breakpoint route after renaming or duplicating.
- Preserve `scrollTargetEnabled` and real `elementId` contracts when names change.
- A Phone variant must not inherit Desktop hover/click behavior blindly.
- Prefer native Framer Components, Variants, Properties, Styles, Layout Templates, CMS, Effects, and Overlays. Obtain approval before Custom Code or paid dependencies.

## Implement in one layer at a time

1. Fix the canonical Component Definition first when the defect is shared.
2. Fix Page Instance content/width only when the definition is correct.
3. Fix a Breakpoint Override only when the difference is intentionally breakpoint-specific.
4. Batch the known changes, then read back the definition, representative first/middle/last instances, and affected breakpoints.
5. Invoke `framer-qa` after the system is implemented; do not preload the entire QA checklist.

## Conditional references

- Component/Property/Variant decision table: [pattern-recipes.md](../../../framer/basic/patterns/pattern-recipes.md)
- Button ownership and Small Variants: [buttons.md](../../../framer/basic/patterns/buttons.md)
- Shared shell and drawer/overlay patterns: [navbar-footer.md](../../../framer/basic/patterns/navbar-footer.md)
- Naming only when creating or renaming layers: [layer-naming.md](../../../framer/basic/standards/layer-naming.md)
- Targeted reads, instance overrides, and width chains: selected sections of [token-saving.md](../../../framer/basic/workflows/token-saving.md)
- A specific advanced component: choose exactly one entry from [advance-design/README.md](../../../framer/advance-design/README.md)
- Marketplace editability/replacement tests: [marketplace-guidelines.md](../../../framer/basic/standards/marketplace-guidelines.md)
