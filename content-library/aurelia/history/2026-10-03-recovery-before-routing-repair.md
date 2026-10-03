# AURELIA Current Recovery

- Updated: 2026-08-16
- Status: **Custom 404 page built; remaining visual and behavior QA remains open**

This file is intentionally short. It records only the latest useful re-entry state; older implementation logs live in [HISTORY.md](./HISTORY.md).

## Connection state

- Framer project: `6EYvZfFo1CleDR77cYUF`
- Current live page: `/chefs` (latest page write context)
- Current Framer session: `9` (used for the latest authorized Chefs responsive-width and Tablet Expanded portrait write; inspect live Canvas before future writes)
- Canvas connection during this knowledge migration: authorized Chefs responsive-width and portrait work with targeted readback completed on 2026-08-16
- Publish performed: no

The older About session `2` and Chefs session `3` are historical evidence, not a safe current connection pointer.

## Current audit checkpoint

- Scope: Marketplace canvas readiness, excluding listing/publishing/payment settings.
- Result: Fix Required. Five active navigation pages, the shared Template, and a custom `/404` page were structurally verified; `/private-dining` is absent.
- Current P0 gaps: `/chefs` metadata, Home Hero Alt decision, editable Alt paths for buyer-replaceable component images, and component/layer naming cleanup. The custom `/404` page has unique no-index metadata, one semantic `h1`, Desktop/Tablet/Phone breakpoints, and a `Return home` Button route to `/`; its cross-browser, keyboard/Focus, `320/1440+`, and user visual checks remain open.
- Canonical remediation checklist: [Marketplace canvas readiness audit](./checklist/marketplace/2026-08-15-canvas-readiness-audit.md).

## Last documented multi-page Part

- Scope: shared Layout Template, Navbar, Footer, and `Reservation Handoff` across the current five-page site
- Latest dated record: 2026-08-15
- Part status: Fix Required

Last documented successful changes:

- All five pages remained assigned to one shared `Template`.
- Template root overflow was changed from clipped to visible while Framer-required fixed `1000px` authored heights were retained.
- Shared Navbar navigation became Home, Menu, About, Chefs, and Reserve.
- Shared Footer received the same page navigation plus Demo email and telephone.
- One native shared Reservation Handoff Component now serves Home, Menu, and Chefs with page-specific Heading / Supporting Copy properties and one existing Button route to `/reserve`. Desktop/Tablet use horizontal variants; Phone and Chefs Wide Phone use the vertical Phone variant.
- A custom `/404` Not Found page was added with the shared Template and existing Button component. Its dark editorial surface contains one `h1`, supporting copy, and one clear route back to `/`.
- Private Dining was removed from the active plan.

## Open recovery checks

1. Before any future Canvas write, establish a new current session and inspect the actual target page/component. Do not resume from session `2` or `3` by assumption.
2. Confirm the effective shared Template, Navbar, Footer, and Handoff instances on all five current pages.
3. The Handoff component and its Desktop/Tablet/Phone instance variants have structural evidence. User visual confirmation remains the final composition check; do not recreate page-local Handoff Frames.
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
