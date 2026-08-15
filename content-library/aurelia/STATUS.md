# AURELIA Current Build and QA Status

- Reconciled: 2026-08-15
- Evidence basis: latest dated project Checklists and the preserved pre-migration snapshot
- Canvas verification in this migration: **not performed**

This file contains current status only. Replace stale status here when work advances; move implementation chronology to [HISTORY.md](./HISTORY.md).

## Status vocabulary

- `Built`: the documented structure exists.
- `Partial Pass`: the documented structure or component passed targeted checks, but Page Done is not established.
- `Fix Required`: a required current check remains open.
- `Blocked`: completion depends on missing facts, services, assets, permission, or reliable evidence.
- `Needs refresh`: the repository cannot safely establish the current live value without a future authorized inspection.

## Page status matrix

| Page | Structure and current system | Content | Current QA state | Current status |
|---|---|---|---|---|
| Home `/` | Built across Desktop, Tablet, and Phone; shared `Reservation Handoff`, Navbar, and Footer documented. | Demo. | Full regression, five widths, Hero crop/Alt, chapter and DishSelector interactions, Focus, Reduced Motion, Lenis, overflow, metadata, and replacement stress remain open. | Fix Required |
| Menu `/menu` | Requested Opening, Changing Menu Statement, seven `MenuDishCard` instances, responsive variants, and shared handoff documented as built. | Demo; price and dietary policy missing. | Full `320/390/810/1200/1440+` Page QA, live Hover/Expand/Collapse, Focus, Kitchen Interruption decision, optional-field stress, replacement images, and buyer reorder path remain open. | Partial Pass |
| About `/about` | Culture structure built: Opening, Exterior, Statement, Working Method, Cooking, Relationships; no in-page handoff. | Clearly marked Demo; verified identity and claims missing. | Desktop targeted evidence exists; Phone visual evidence, five widths, Focus, Reduced Motion, metadata, and replacement stress remain open. | Partial Pass / Blocked content |
| Chefs `/chefs` | Shared Template, three `ChefStoryRow` instances, eight responsive component states, and shared handoff documented as built. | Visible Demo profiles; verified names, roles, stories, and claims missing. | `320`, `1440+`, Phone render, keyboard, state semantics, Focus, Reduced Motion, metadata, Alt/property path, long-content, and image replacement remain open. | Partial Pass / Blocked content |
| Reserve `/reserve` | Compact request page, native labelled form, `ReservationSubmit` state component, Demo fallbacks, Navbar/Footer routes documented as built. | Demo contacts; production policies missing. | Real submission, validation/error behavior, privacy, keyboard, Focus, screen-reader names, Reduced Motion, `320/1440+`, live click path, and replacement setup remain open. | Partial Pass / Blocked service |

## Shared system status

### Shared Layout Template

Status: **Fix Required / user visual confirmation pending**

- All five current pages are documented as assigned to one `Template`.
- Framer-required `height: 1000px` breakpoint roots were retained.
- The clipping regression was repaired by resetting the three Template roots from `overflow: clip` to visible overflow.
- The effective Navbar/Footer instances on all five pages still require current visual confirmation before Page Done claims.
- A visually white canvas-only area has no selectable or serialized node in the existing evidence. It must remain untouched until its exact object can be identified safely.

### Shared Navbar

Status: **Built; final visual/interaction sign-off open**

- Current links: Home `/`, Menu `/menu`, About `/about`, Chefs `/chefs`, Reserve `/reserve`.
- Desktop, Tablet, Phone Closed, and Phone Open variants remain the active model.
- The Navbar remains fixed and compact at `35px`; no scroll-hide/show effect and no extra Reserve CTA.
- Phone Open Chefs was aligned to the existing full-width padded link-row contract.
- Phone press feedback and effective page-instance rendering still need user confirmation or targeted behavior evidence.

### Shared Footer

Status: **Built; final visual sign-off open**

- Current navigation covers all five pages.
- Demo email and phone use clickable `mailto:` and `tel:` destinations.
- No Footer CTA, social links, address, map, or hours are part of the active Footer scope.
- Final inherited breakpoint composition and links require current confirmation.

### Shared Reservation Handoff

Status: **Fix Required**

- One native `Reservation Handoff` owns the deep inverse surface, Heading, Supporting Copy, and an existing `Button` linked to `/reserve`.
- Home, Menu, and Chefs use page-specific copy through the shared contract.
- Desktop uses the primary variant, Tablet uses `Tablet`, and Phone plus Chefs Wide Phone use `Phone`.
- Desktop `1200` and Tablet `810` have structural/rendered evidence.
- Phone `390` content and variant bindings were read back, but the measurement path returned a `200 x 200` editor placeholder. Static Phone visual confirmation is still required on Home, Menu, and Chefs.
- Pre-existing Menu root sibling-overlap warnings remain for full Menu QA.

## Current global blockers

- Real reservation/form data destination and data handling
- Privacy language, response time, cancellation and arrival policies
- Verified address, phone, email, opening hours, capacity, pricing, dietary policy, accessibility, and other operational facts
- Verified chef identities, roles, biographies, viewpoints, team information, and claims
- Image/font licensing and Marketplace redistribution confirmation
- Demo URL, Remix URL, favicon, Open Graph cover, and complete Marketplace editing instructions
- Reliable current Framer session and active page recovery pointer

## Current QA priorities

1. On the next authorized Canvas task, inspect the actual target before writing and reconcile this status with the live implementation.
2. Confirm the shared Template, Navbar, Footer, and Handoff on their effective page instances before page-specific cleanup.
3. Obtain the missing Phone visual evidence for the shared Handoff without treating the `200 x 200` editor placeholder as a responsive conclusion.
4. Complete page-specific five-width, keyboard, Focus, Reduced Motion, content replacement, and Marketplace stress checks only for the page currently in scope.
5. Connect and verify the Reserve submission path only after the user supplies or approves the real service and privacy handling.

## Page contracts

- [Home](./checklist/home.md)
- [Menu](./checklist/menu.md)
- [About](./checklist/about/about.md)
- [Chefs](./checklist/chefs/chefs.md)
- [Reserve](./checklist/reserve.md)
- [Shared shell and reservation handoff](./checklist/shared-shell-and-reservation-handoff.md)
