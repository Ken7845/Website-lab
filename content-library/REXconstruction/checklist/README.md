# REX Construction — Checklist Index

This directory owns page plans and acceptance criteria. The current request authorizes homepage implementation in the supplied Framer project. Publishing remains outside scope.

## Owners

- [Project](../PROJECT.md)
- [Current Status](../PROJECT.md#12-current-status)
- [Decisions](../PROJECT.md#13-decisions-and-exceptions)
- [Recovery](../PROJECT.md#14-recovery)
- [Platform workflow](../../../framer/README.md#1-先-inspect--reconcile)
- [Change control](../../../framer/basic/workflows/change-control.md#authorization-and-task-mode)

## Page Index

| Page | Path | Canonical checklist | Status |
|---|---|---|---|
| Home | `/` | [home.md](home.md) | Partial — Navbar, button variants, and six-review selector implemented; Hero counter instances await approved values |

Only Home has an active checklist. Existing supporting pages are reference destinations.

Latest request record: [Navigation, Buttons, Reviews, and Counters revision](home/navigation-buttons-reviews-counters.md) — implemented except Hero metric placement, which awaits approved values.

## Status Meaning

- **To do:** Authorized scope has not been implemented or verified.
- **In progress:** Work is underway on an explicit Part.
- **Fix Required:** A check failed and needs correction.
- **Blocked:** Required content, target, service or evidence is unavailable.
- **Pass:** The applicable structure, visual and runtime checks have passed.

A completed planning document does not mark the page as Pass.

## Shared Foundation Gate

Before implementation, inspect existing structures and decide Add / Reuse / Modify / No-op for the shell, navigation, footer, buttons and styles.

- [x] Confirm platform, project target and shared shell ownership.
- [x] Define text/color roles, readable logo sizing, buttons and responsive navigation.
- [x] Define keyboard focus, touch targets and reduced-motion behavior; live keyboard execution remains unavailable without staging.
- [ ] Assign favicon and social-sharing image.
- [ ] Confirm asset rights, form/newsletter connections and editing ownership.
- [x] Define component properties/variants before building reusable structures.

## Execution Loop

Read the page scope and contract → resolve the next Part's dependencies → implement that Part when authorized → targeted readback and Preview → record actual results → synchronize PROJECT status and its single Recovery owner.

Choose one primary implementation skill through the platform router. The local plan does not establish a Framer connection or prove current platform behavior.

## Part Result Format

Update the page's Latest Part Result with Part name, date, Pass / Fix Required / Blocked or Not run, verified widths, verified runtime paths, affected shared components and the canonical [Recovery reference](../PROJECT.md#14-recovery). Store the current checkpoint only in that Recovery owner.

## Latest Part Result

- Part: Navigation, Buttons, Reviews, and Counters revision
- Date: 2026-10-13
- Result: Partial — Phone hover removed; reusable Yellow-fill navigation, red, and white buttons implemented; white CTAs applied to three sections; six-review selector implemented. Hero Counter instances await approved metric values.
- Verified widths: 1200 and 390 visual; 810 structural.
- Verified paths/states: Phone Closed/Open with no row hover; Desktop nav and red/white button hover variants; section destinations; six review selections; Counter code-component registration; clean preview readiness.
- Canonical Recovery: [PROJECT §14](../PROJECT.md#14-recovery)
