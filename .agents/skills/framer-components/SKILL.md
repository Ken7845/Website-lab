---
name: framer-components
description: "Compile, design, inspect, or repair native Framer Component contracts: Definitions, Variants, Properties, Instances, Styles, CMS, shared systems, and component-owned sizing. Use whenever creating, duplicating, or restructuring a reusable Component, including an interactive or responsive row/card; this is primary over layout or interaction Skills while ownership is being established. For live Canvas work, first complete official $framer setup, session, and task-map routing. Do not use for page-composition-only, established-component motion-only, or final-audit work."
---

# Framer Components

Build reusable systems only where reuse or state actually exists.

## Platform gate

First use the [Framer dispatcher](../../../framer/README.md#2-只选一个-primary-repo-skill), including its ownership precedence and task mode. For live reads or writes, complete the canonical [Live Framer Canvas Gate](../../../AGENTS.md#live-framer-canvas-gate); **Gate remains closed** until its evidence is complete. Show the **Framer Agent gate receipt** before implementation. This Skill supplies reasoning, not a platform connection. Repository-only work skips connection.

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

## Compile a Component Requirement Contract

Before the first Canvas write that creates, duplicates, or changes a reusable Component's ownership, compile this contract from current Canvas evidence plus only the relevant routed rules. Reading a long Baseline is not proof that a rule was applied.

Use `rg -n` to locate the applicable headings rather than loading whole references. Fill every row with a concrete decision or `N/A — <reason>`; no blank cell is allowed. `Governing source` must identify a targeted `path.md#heading`, a numbered user requirement, current Canvas evidence, or a reasoned `N/A`; a bare filename or the word “Baseline” is not a usable rule link.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm |  |  |  |  |  |
| Available width / placement |  |  |  |  |  |
| Visible boundary / border / surface |  |  |  |  |  |
| Internal padding / hit area |  |  |  |  |  |
| Readable max-width |  |  |  |  |  |
| Editable content / Properties |  |  |  |  |  |
| States / routes |  |  |  |  |  |
| Breakpoint contract |  |  |  |  |  |
| Accessibility / touch / focus |  |  |  |  |  |
| Evidence sample |  |  |  |  |  |

Use [Contract lifecycle](../../../framer/basic/workflows/change-control.md#contract-lifecycle) for applicability, separate authorization, implementation and verification states, and scoped evidence links.

Set `Contract status: Ready` only after all owner decisions and planned proof paths are complete. If a request Checklist exists, persist the table there under `## Component Requirement Contract`; otherwise keep the compact contract in working state. Do not create another repository file merely for the contract.

Before implementation, show one concise **Component contract receipt**: `owners complete / N/A reasoned / readback planned / preview planned`. Any missing field keeps the write gate closed; do not substitute a generic claim that the Baseline was read.

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

1. Implement the `Ready` contract in ownership order; do not invent a second layout model while writing.
2. Fix the canonical Component Definition first when the defect is shared.
3. Fix Page Instance content/width only when the definition is correct.
4. Fix a Breakpoint Override only when the difference is intentionally breakpoint-specific.
5. Batch the known changes, then read back each contract row through Definition, representative first/middle/last Instances, affected Breakpoint Overrides, standalone Component, and real Page Preview as applicable.
6. Replace planned proof with actual evidence and set the contract to `Pass` or `Blocked`; never mark it `Pass` from a successful write command.
7. Invoke `framer-qa` after the system is implemented; do not preload the entire QA checklist.

## Conditional references

- Component/Property/Variant decision table: [pattern-recipes.md](../../../framer/basic/patterns/pattern-recipes.md)
- Button ownership and Small Variants: [buttons.md](../../../framer/basic/patterns/buttons.md)
- Shared shell and drawer/overlay patterns: [navbar-footer.md](../../../framer/basic/patterns/navbar-footer.md)
- Naming only when creating or renaming layers: [layer-naming.md](../../../framer/basic/standards/layer-naming.md)
- Targeted reads, instance overrides, and width chains: selected sections of [token-saving.md](../../../framer/basic/workflows/token-saving.md)
- A specific advanced component: choose exactly one entry from [advance-design/README.md](../../../framer/advance-design/README.md)
- Marketplace editability/replacement tests: [marketplace-guidelines.md](../../../framer/basic/standards/marketplace-guidelines.md)
