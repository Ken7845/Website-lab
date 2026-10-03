# AURELIA Current Build and QA Status

- Reconciled: 2026-10-03 — repository only; last recorded live evidence remains 2026-08-16
- State revision: 2026-10-03-repository
- Active request: [Marketplace readiness audit](./checklist/marketplace/2026-08-15-canvas-readiness-audit.md)
- Evidence basis: latest dated project Checklists, the preserved pre-migration snapshot, and a read-only live Canvas structure and Marketplace release audit on 2026-08-16
- Canvas verification: page tree, metadata, shared systems, component controls, image Alt ownership, style/token inventory, and CMS presence inspected. The recorded project workflow leaves responsive, interaction, Focus, Reduced Motion, navigation, CTA-route and Reserve-state visual review with the user. Pending reviews remain unverified; actual scoped user observations may be recorded as evidence under [Evidence selection](../../framer/basic/workflows/image-workflow.md#evidence-selection).

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
| Home `/` | Built across Desktop, Tablet, and Phone; shared `Reservation Handoff`, Navbar, and Footer documented. Desktop structure readback on 2026-08-16 confirms the approved sequence, with Reservation Handoff immediately after Signature. | Demo. | Full regression, five widths, Hero crop/Alt, chapter and DishSelector interactions, Focus, Reduced Motion, Lenis, overflow, metadata, and replacement stress remain open. | Fix Required |
| Menu `/menu` | Requested Opening, Changing Menu Statement, seven `MenuDishCard` instances, responsive variants, and shared handoff documented as built. | Demo; price and dietary policy missing. | Full `320/390/810/1200/1440+` Page QA, live Hover/Expand/Collapse, Focus, Kitchen Interruption decision, optional-field stress, replacement images, and buyer reorder path remain open. | Partial Pass |
| About `/about` | Culture structure built: Opening, Exterior, Statement, Working Method, Cooking, Relationships; no in-page handoff. | Clearly marked Demo; verified identity and claims missing. | Desktop targeted evidence exists; Phone visual evidence, five widths, Focus, Reduced Motion, metadata, and replacement stress remain open. | Partial Pass / Blocked content |
| Chefs `/chefs` | Shared Template, three `ChefStoryRow` instances, eight responsive component states, and shared handoff documented as built. The `Chef Profiles` list now has no breakpoint max-width; every instance is Fill. Tablet Expanded keeps its portrait at a fixed 2:3 frame while Story remains the responsive Fill region. | Visible Demo profiles; verified names, roles, stories, and claims missing. | `320`, `1440+`, Phone render, keyboard, state semantics, Focus, Reduced Motion, Alt/property path, long-content, and image replacement remain open. Page Title and Meta Description were verified in the live Canvas on 2026-08-16. | Partial Pass / Blocked content |
| Reserve `/reserve` | Compact white request area, native labelled form, `ReservationSubmit` state component, and a separate full-width soft-grey FAQ surface with eight `FAQ Row` instances. Questions retain the larger dark style; answers use smaller Muted typography and complete fictional reference policies rather than instruction-style Demo placeholders. | Fictional contacts and reference policies; production facts and policies missing. | Real submission, validation/error behavior, privacy, keyboard, Focus, FAQ interaction, screen-reader names, Reduced Motion, `320/1440+`, live click path, and replacement setup remain open. | Partial Pass / Blocked service |
| Not Found `/404` | Custom error page built with the shared Template, a dark editorial surface, one semantic `h1`, and the existing Button component returning to `/`. Desktop, Tablet, and Phone breakpoints are authored. | No operational claims added. | Structural readback, metadata, route, button link, semantic `h1`, breakpoint values, and one Desktop screenshot verified on 2026-08-16. Cross-browser, keyboard/Focus, `320/1440+`, and user visual confirmation remain open. | Partial Pass |

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
- Desktop and Tablet Menu, About, Reserve, and Chefs labels are editable `Reel Text` Button instances; Phone and Phone Open use ordinary `Type/Button` labels, with Phone Open retaining `Close`.
- Phone press feedback and effective page-instance rendering still need user confirmation or targeted behavior evidence.

### Shared Footer

Status: **Built; final visual sign-off open**

- Current navigation covers all five pages.
- Desktop and Tablet Home, Menu, About, Chefs, and Reserve are editable `Reel Text` Body instances with their existing routes; Phone uses ordinary `Type/Body` links. The AURELIA brand Reel retains `/#top`.
- Demo email and phone use clickable `mailto:` and `tel:` destinations.
- No Footer CTA, social links, address, map, or hours are part of the active Footer scope.
- Final inherited breakpoint composition and links require current confirmation.

### Shared Reservation Handoff

Status: **Built; user visual sign-off open**

- One native `Reservation Handoff` component now owns the inverse surface, the Heading and Supporting Copy properties, and the existing white `Button` linking to `/reserve`.
- Home, Menu, and Chefs each use one instance with page-specific copy. Their authored breakpoints use `Desktop`, `Tablet`, and `Phone` variants; Chefs Wide Phone uses the `Phone` variant.
- Desktop and Tablet use the horizontal reading/action arrangement; Phone uses the vertical reading order. Existing 32px, 28px, and 20px gutters are retained through the component variants.
- Targeted structural readback confirms the component, all three page instances, their content overrides, all authored Handoff variants, and the existing `/reserve` Button route. Final static composition remains user-judged in Framer, as requested.
- Pre-existing Menu root sibling-overlap warnings remain for full Menu QA and were not changed by this component work.

## Current global blockers

- Real reservation/form data destination and data handling
- Privacy language, response time, cancellation and arrival policies
- Verified address, phone, email, opening hours, capacity, pricing, dietary policy, accessibility, and other operational facts
- Verified chef identities, roles, biographies, viewpoints, team information, and claims
- Image/font licensing and Marketplace redistribution confirmation
- Demo URL, Remix URL, favicon, Open Graph cover, and complete Marketplace editing instructions
- Reliable current Framer session and active page recovery pointer

## Marketplace release readiness

Status: **Fix Required — 55/100 provisional overall readiness**

- A read-only audit confirmed six active pages including `/404`, one shared Template, 14 local Components, no active `/private-dining`, and no CMS collections. Primary breakpoint readback now confirms exactly one semantic `h1` on each active page; Menu's seasonal statement and Reserve's request heading were corrected to `h2` without visual or structural change.
- Button hygiene now passes: the old horizontal variants are absent and 14 site instances use descriptive diagonal variants. MenuDishCard now exposes `Image Alt`; the older missing-Property claim is retired.
- Home Hero, `ChefStoryRow`, `DishSelector`, and `EveningChapterRow` now have explicit Alt handling; `hero` and `Hero Loader` variants use descriptive state names. The unused `Examples.tsx` test override was removed after a zero-reference readback. Current P0 gaps include the ChapterCursorPreview decorative decision; replacement pressure; licensing/performance; Demo/Remix URLs; listing media/copy/support; and full regression evidence.
- Responsive, interaction, keyboard/Focus, Reduced Motion, Phone navigation, Footer/CTA routing, Reserve states and cross-browser behavior require Preview/user evidence and are not considered structurally proven by this audit.
- The executable Canvas, buyer-editability, listing, launch and post-launch plan is maintained in [Marketplace release readiness audit](./checklist/marketplace/2026-08-15-canvas-readiness-audit.md). This does not authorize a Canvas change or publication.

## Current QA priorities

1. On the next authorized Canvas task, inspect the actual target before writing and reconcile this status with the live implementation.
2. Confirm the shared Template, Navbar, Footer, and Handoff on their effective page instances before page-specific cleanup.
3. The Reservation Handoff is already consolidated into one native Component; future edits should change its component definition and page-instance text properties rather than recreating page Frames.
4. Complete page-specific five-width, keyboard, Focus, Reduced Motion, content replacement, and Marketplace stress checks only for the page currently in scope.
5. Connect and verify the Reserve submission path only after the user supplies or approves the real service and privacy handling.

## Page contracts

- [Home](./checklist/home.md)
- [Menu](./checklist/menu.md)
- [About](./checklist/about/about.md)
- [Chefs](./checklist/chefs/chefs.md)
- [Reserve](./checklist/reserve.md)
- [Shared shell and reservation handoff](./checklist/shared-shell-and-reservation-handoff.md)
