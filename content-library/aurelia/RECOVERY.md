# AURELIA Current Recovery

- Updated: 2026-08-15
- Status: **Needs refresh**

This file is intentionally short. It records only the latest useful re-entry state; older implementation logs live in [HISTORY.md](./HISTORY.md).

## Connection state

- Framer project: `6EYvZfFo1CleDR77cYUF`
- Current live page: **Needs refresh**
- Current Framer session: **Needs refresh**
- Canvas connection during this knowledge migration: none
- Publish performed: no

The older About session `2` and Chefs session `3` are historical evidence, not a safe current connection pointer.

## Last documented multi-page Part

- Scope: shared Layout Template, Navbar, Footer, and `Reservation Handoff` across the current five-page site
- Latest dated record: 2026-08-15
- Part status: Fix Required

Last documented successful changes:

- All five pages remained assigned to one shared `Template`.
- Template root overflow was changed from clipped to visible while Framer-required fixed `1000px` authored heights were retained.
- Shared Navbar navigation became Home, Menu, About, Chefs, and Reserve.
- Shared Footer received the same page navigation plus Demo email and telephone.
- One shared `Reservation Handoff` was applied to Home, Menu, and Chefs with page-specific Heading / Supporting Copy and one `Reserve a seat` link to `/reserve`.
- Private Dining was removed from the active plan.

## Open recovery checks

1. Before any future Canvas write, establish a new current session and inspect the actual target page/component. Do not resume from session `2` or `3` by assumption.
2. Confirm the effective shared Template, Navbar, Footer, and Handoff instances on all five current pages.
3. Confirm the static Phone Handoff result on Home, Menu, and Chefs. Existing measurement evidence returned a `200 x 200` editor placeholder and is not a visual pass.
4. Obtain the user's visual confirmation for the repaired shared shell and compact Phone navigation behavior.
5. Leave the unidentified canvas-only white area untouched until its exact selectable object or node is known.
6. Resolve the pre-existing Menu root sibling-overlap warnings only during authorized full Menu QA.
7. Keep Reserve live submission blocked until a real destination, privacy handling, policies, and result behavior are supplied.

## Re-entry constraints

- Current sitemap: `/`, `/menu`, `/about`, `/chefs`, `/reserve`.
- Do not restore `/private-dining`.
- Do not create a second reservation handoff on Home, Menu, or Chefs.
- Do not change About's no-handoff ending.
- Do not modify or publish the Canvas from a knowledge-architecture task.
- Inspect current implementation before loading historical details.

## Recovery routes

- [Current manifest](./PROJECT.md)
- [Current status](./STATUS.md)
- [Shared-shell Checklist](./checklist/shared-shell-and-reservation-handoff.md)
- [History and exact evidence routes](./HISTORY.md)
- [Verbatim pre-migration snapshot](./history/project-pre-migration-2026-08-15.md)
