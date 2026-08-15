# AURELIA Shared Shell and Reservation Handoff Checklist

> **Current-state ownership after the 2026-08-15 knowledge migration:** project identity and sitemap live in `../PROJECT.md`; Build / QA in `../STATUS.md`; lasting rationale in `../DECISIONS.md`; the single latest continuation pointer in `../RECOVERY.md`. Older instructions below that name PROJECT as the combined owner are retained as historical request evidence.
>
> Within this request record, **Latest Part Result** owns the current outcome. Earlier Scope lock and Execution order sections preserve the approved pre-consolidation requirements and may name structures that were later replaced.

Status: Implemented; Fix Required final Phone rendering, regression, and visual sign-off  
Scope: One shared reservation-handoff section applied to Home, Menu, and Chefs, with page-specific editorial copy and one Reserve destination  
Primary CTA: `Reserve a seat` → existing `/reserve` information form

## Scope amendment — 2026-08-15

This was the approved implementation contract for the completed Canvas Part. It superseded only the earlier handoff-copy direction below; the current result and remaining QA are recorded under **Latest Part Result**.

### Required page-specific content

The section is a shared component/layout contract placed immediately before the shared Footer. It must use one CTA label and destination, while the headline and supporting copy respond to the page the visitor has just read.

| Page | Narrative role | Reservation heading | Supporting copy | CTA |
|---|---|---|---|---|
| Home `/` | Conclude the site’s belief-to-evidence story with an invitation. | `There is a place at the table.` | `When the evening feels right, begin with a date. The rest can be arranged around the table.` | `Reserve a seat` → `/reserve` |
| Menu `/menu` | Turn the changing-menu story into a concrete next step. | `A menu made for a particular night.` | `The dishes will keep changing. Choose a date, and we can begin with the table.` | `Reserve a seat` → `/reserve` |
| Chefs `/chefs` | Connect the people behind the meal to the guest’s decision to join them. | `The table begins with the people behind it.` | `Meet the hands shaping the evening, then choose a night to sit at the table.` | `Reserve a seat` → `/reserve` |

### Build and verification checklist

- [x] Re-read the live end-of-page structure for Home, Menu, and Chefs before inserting the handoff directly before the shared Footer.
- [x] Use one shared native Framer component/layout with editable Heading and Supporting Copy properties; do not duplicate three independent Frame trees.
- [x] Reuse the existing `Button` component with its existing white-on-dark treatment and bind its visible click boundary to `/reserve`.
- [x] Keep the existing `Reserve a seat` label identical on all three pages; no secondary booking route, provider, or invented operational claim.
- [x] Use the existing near-black inverse surface, white text, border tokens, Inter hierarchy, sharp edges, and existing page gutter rhythm.
- [x] Desktop: retain the spacious editorial conclusion with asymmetric copy ownership and approximately 220–300px vertical breathing room.
- [x] Tablet: reduce the composition deliberately using 28px gutters; do not passively shrink Desktop.
- [x] Phone structure uses a dedicated single-column Variant with 20px gutters and a single-line CTA label; static rendered confirmation remains open.
- [ ] Keep motion restrained: a single native entrance for editorial copy only; no new custom code, continuous motion, or layout-changing button hover.
- [ ] Verify focus visibility, colour contrast, semantic heading level, keyboard order, and Reduced Motion reading order.
- [x] Targeted structural readback verified one shared contract plus the three page-instance copy/property values and `/reserve` link at Desktop, Tablet, and Phone; Phone visual evidence remains open.
- [x] Update Latest Part Result and the current `STATUS.md` / `RECOVERY.md` owners with the evidence-qualified result.

### Explicit exclusions

- [ ] Do not modify the Reserve form or assert that a reservation is confirmed.
- [ ] Do not add address, hours, capacity, prices, dietary policy, booking-provider details, or any other unverified operational facts.
- [ ] Do not alter the shared Navbar, Footer, existing Menu dish-card system, Home DishSelector, or Chefs profile component outside the necessary page insertion point.

## Latest Part Result — 2026-08-15

Scope: Shared reservation handoff component and Home / Menu / Chefs instances  
Status: Fix Required

Pass:

- One native `Reservation Handoff` component now owns the deep inverse surface, Heading and Supporting Copy properties, plus an existing `Button` instance linking to `/reserve`.
- Home, Menu and Chefs use that component with their approved, page-specific Heading and Supporting Copy values.
- Desktop uses the primary component variant; Tablet uses the dedicated `Tablet` variant; Phone and Chefs Wide Phone use the dedicated `Phone` variant.
- Desktop and Tablet readback reports full-width instances with bounded rendered heights; one target-node screenshot was generated for the shared component.

Fix Required:

- Confirm the static Phone canvas result on Home, Menu and Chefs. Framer's measurement API returned its `200 × 200` editor placeholder for the Phone ground after the section was added, so it cannot establish the actual visual result.
- Resolve the pre-existing Menu root sibling-overlap warnings during its full-page QA; this Part did not change those earlier siblings.

Blocked:

- Real booking-provider integration remains outside this handoff scope.

Verified widths:

- Desktop 1200: structural readback and rendered component rects.
- Tablet 810: structural readback and rendered component rects.
- Phone 390: component variant and content binding read back; visual canvas confirmation pending.

Verified paths:

- `Reserve a seat` is bound through the shared Button component to `/reserve`.

Shared components affected:

- `Reservation Handoff` (new)
- `Button` (reused; not modified)

## Scope lock

### Regression added 2026-08-14 — shared-shell application failure

Reported symptom: the updated Navbar and Footer render in the Layout Template, but the live page instances do not show or cannot apply the same changes. Phone `Chefs` also does not match the existing menu-link pattern.

Diagnosis: all three Layout Template breakpoint roots use fixed `height: 1000px` with `overflow: clip`. The Content Placeholder cannot expand the shared shell through page content, so later shared content is clipped. The new Phone Open `Chefs` link inherited Desktop `width: auto`/no-padding values instead of the existing Phone link-row contract.

- [ ] Mark Navbar and Footer as `Fix Required`; do not continue reservation-handoff work until the shared-shell regression is resolved.
- [ ] Inspect the Layout Template instance IDs, every page’s `$layoutTemplateId` / `layoutTemplate` assignment, and each page’s effective Navbar/Footer instances and variants.
- [ ] Compare the Phone Open `Chefs` link against the established Phone Open Menu/About/Reserve link structure: parent, width, padding, alignment, inherited variant status, link style, and press treatment.
- [ ] Determine whether the regression comes from component edits, replica inheritance, a stale/overridden Layout Template instance, or page-level layout-template assignment.
- [ ] Repair the smallest shared source of the defect; do not patch individual pages unless a page has an intentional documented override.
- [ ] Read back Template plus Home, Menu, About, Reserve, and Chefs effective Navbar/Footer instances after repair.
- [ ] Ask the user to visually confirm the repaired shared shell in Framer; do not use browser Preview by default.

Repair recorded: retained Framer-required fixed Template breakpoint heights, reset all three root containers from `overflow: clip` to the default visible overflow, and aligned Phone Open `Chefs` with the existing full-width/padded phone link row. All five pages remain assigned to the same `Template`; visual confirmation is pending.

Clarification recorded: Agent directly inspects static canvas/screenshot layout. The avoided behavior is repeated browser Preview mouse-clicking to prove an effect; advanced interactive behavior is instead structurally read back and then confirmed by the user.

Included:

- Add `Chefs` to the shared Navbar on Desktop, Tablet, Phone, and Phone Open, linking to the existing `/chefs` page.
- Preserve the intentionally compact Navbar. It remains fixed and **does not** receive a scroll-hide / scroll-show effect.
- Preserve the existing Phone Closed / Phone Open Variant drawer. Do not replace it with an Overlay.
- Add and verify the Phone press feedback for the Menu/Close trigger and navigation links; it must be native, restrained, non-scaling, and not shift layout.
- Record the verified Phone Variant-drawer structure in `framer/basic/patterns/navbar-footer.md` as a supported base pattern.
- Add a reservation handoff to `/chefs` by reusing the existing Menu `Menu Reservation Handoff` structure / component model. Its Reservation Heading is independently editable for Chefs.
- Rework Home `Invitation Section` to use that same reservation-handoff layout and interaction contract. Its Invitation Heading is independently editable for Home.
- Keep Menu, Home, and Chefs as three uses of one shared reservation-handoff component/layout; heading differs by page, function and destination remain identical.
- Complete the shared Footer navigation with Home, Menu, About, Chefs, and Reserve. Do not add a separate Footer CTA and do not add social links.
- Add the established fictional Demo email and phone from the Menu canvas as clickable `mailto:` and `tel:` links; retain the replace-before-publish Demo notice. Do not add address, hours, map, or other operational facts in this round.
- Adjust Footer composition only as needed to keep AURELIA’s quiet, sparse editorial voice across Desktop, Tablet, and Phone.
- Remove Private Dining from the approved plan and future navigation direction in the canonical AURELIA `PROJECT.md`; do not create, link, or reserve a `/private-dining` page.
- Update the review-policy documentation: prefer targeted structural readback and user visual approval for advanced motion/components. Do not use browser Preview as a default proof path when the user can directly judge the result. Keep Preview only for cases where the user specifically requests it or where behavior cannot be established through structural evidence and user confirmation.

Excluded:

- New Navbar `Reserve` CTA/button: the existing `/reserve` destination already serves this role.
- Navbar scroll-direction behavior.
- Phone Overlay implementation.
- Private Dining page, content, link, or information architecture.
- Social links, hours, address/map, and invented operational facts.
- Publishing, browser-driven visual QA, and unrelated page changes.

## Execution order

### Part 1 — Shared Navbar

- [x] Read the current `Navigation` component and its Desktop, Tablet, Phone, and Phone Open variants immediately before changes.
- [x] Add `Chefs` once to the shared link model, with `/chefs` as its real destination, and retain Menu, About, and Reserve.
- [x] Preserve 35px compact fixed Desktop/Tablet navigation and its existing visual language; do not add a second CTA or scroll behavior.
- [x] Preserve the Phone Variant drawer. Closed remains clipped; Phone Open reveals the same link structure with stable brand/menu placement.
- [x] Add native press states to relevant Phone controls without scale, reflow, or overflow.
- [x] Read back all four variants and confirm the new link, variants, and link destination; user visual confirmation remains required for the press treatment.

### Part 2 — Document the Phone Navbar base pattern

- [x] Update `framer/basic/patterns/navbar-footer.md` to state that a shared Navbar Component may use Closed / Phone Open Variants as the preferred compact phone drawer pattern.
- [x] Document: one shared component; identical logo/menu row placement; Closed variant clips the existing menu; Open variant reveals it; links remain real destinations; press feedback is native and restrained; Overlay is unnecessary for this pattern.
- [x] Keep the documentation general and reusable; do not embed AURELIA-specific content or chat history.

### Part 3 — Shared reservation handoff

- [x] Read the Menu `Menu Reservation Handoff` structure and its responsive instances.
- [x] Determine whether it is already a reusable component: it is currently a page Frame with separate Desktop, Tablet, and Phone structures.
- [x] Create one shared editable component/layout without changing the Menu visual result.
- [x] Apply it to Chefs and Home. Do not copy independent Frame trees.
- [x] Bind page-specific Reservation Heading content for Menu, Chefs, and Home while preserving a single `Reserve a seat` destination and interaction model.
- [x] Preserve Menu's existing Demo contact handling and apply the same factual status to any reused contact presentation.
- [x] Read back all three page instances at Desktop, Tablet, and Phone after the shared structure is in place.

### Part 4 — Footer

- [x] Read the current shared `Footer` component and all breakpoint variants.
- [x] Add navigation to Home `/`, Menu `/menu`, About `/about`, Chefs `/chefs`, and Reserve `/reserve`.
- [x] Add `reservations@aurelia.example` as `mailto:` and `+1 212 555 0148` as `tel:`; retain their clearly fictional Demo status.
- [x] Do not add a separate CTA, social link, address, map, or hours.
- [x] Maintain a sparse Desktop layout, a legible Tablet reflow, and a natural Phone reading stack; ensure links do not scale on hover/press or cause clipping.
- [x] Read back Footer links, contact destinations, hierarchy, and inherited breakpoint variants; user visual confirmation remains required for final composition.

### Part 5 — Project and review-policy records

- [x] Update the canonical AURELIA `PROJECT.md`: remove Private Dining from sitemap/architecture/build order/navigation references, and record this scope’s decisions and recovery state.
- [x] Update the knowledge-base audit/checklist guidance with the user-approval-first policy for advanced motion/components.
- [x] Keep structural readback mandatory. Browser Preview becomes exceptional rather than default, and cannot be used as a substitute for a user’s visual approval.
- [ ] Update the applicable checklist index and latest-part records with actual status only after execution.

## Acceptance criteria

- [ ] Navbar: Chefs is reachable across all variants; `/reserve` remains the only reservation route; no extra navbar CTA or scroll-hide behavior exists.
- [ ] Phone Navbar: Closed/Open Variant drawer and press feedback are stable and preserve the compact visual system.
- [x] Reservation handoff: Menu, Home, and Chefs share one layout/component contract with page-specific headings and the same Reserve action.
- [ ] Footer: complete page navigation plus clickable Demo email and telephone; no social/CTA/address/hours additions.
- [x] Documentation: Private Dining is removed from the project plan; the reusable Variant-drawer pattern and approval-first review policy are recorded in the correct knowledge-base documents.
- [ ] Validation: targeted live-node readback is complete; advanced visual/interactive sign-off is requested from the user instead of automatically opening a browser Preview.

## Canvas-only white area (2026-08-14)

- [x] Inspect the Layout Template tree before removing anything: no additional top-level content frame exists beyond the expected breakpoint roots and shared instances.
- [ ] Locate the large white block above Desktop/Tablet/Phone through the canvas layer selection. It is not exposed as a separable node in the current structural readback, so it must not be classified as editor chrome or deleted blindly.
- [ ] Delete the exact identified white canvas object, then read back the Template structure and report the result. Current blocker: the visually white area cannot be selected in Canvas and has no corresponding Layer/Framer node; deleting now could remove an unrelated selected layer.

## Confirmation gate

Do not begin Canvas edits, Project-plan edits, or standards edits until the user confirms this checklist.
