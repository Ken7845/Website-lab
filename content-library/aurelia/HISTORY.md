# AURELIA History and Retired Directions

This file is not part of the normal task startup path. Read it only when investigating why a current decision exists, recovering an older implementation, or auditing a regression.

## Verbatim archive

The complete 538-line pre-migration `PROJECT.md` is preserved without summarization at:

- [project-pre-migration-2026-08-15.md](./history/project-pre-migration-2026-08-15.md)

That snapshot retains every earlier current/stale conflict, exact number, breakpoint root id, component parameter, Demo value, Canvas evidence note, QA caveat, decision row, and recovery entry. It is the lossless source for any detail not repeated in the new current documents.

## Retired and superseded directions

| Direction | Current disposition | Original evidence |
|---|---|---|
| `The Evening`, `The Table`, and a former four-page plan | Retired. Do not rebuild. | [Snapshot](./history/project-pre-migration-2026-08-15.md) |
| Home as a literal arrival-to-reservation chronology | Retired. Home is belief-to-evidence. | [Snapshot](./history/project-pre-migration-2026-08-15.md) |
| Oversized visible Science Gothic Hero wordmark | Retired. The current documented Hero text layer is hidden. | [Snapshot](./history/project-pre-migration-2026-08-15.md) |
| Full menu or equal dish grid on Home | Retired. Home uses the focused seven-state `DishSelector`. | [Snapshot](./history/project-pre-migration-2026-08-15.md) |
| `/private-dining` page and future navigation slot | Retired on 2026-08-15. Preserve the old plan for reference, but do not create or link it. | [Private Dining Checklist](./checklist/private-dining.md), [shared-shell decision](./checklist/shared-shell-and-reservation-handoff.md) |
| Anchor-only primary navigation | Superseded by five-page shared navigation. Home anchors may remain contextual only. | [Snapshot](./history/project-pre-migration-2026-08-15.md), [shared-shell Checklist](./checklist/shared-shell-and-reservation-handoff.md) |
| Separate page-specific Home/Menu/Chefs handoff Frame trees | Superseded by one shared `Reservation Handoff`. | [Snapshot](./history/project-pre-migration-2026-08-15.md), [shared-shell Checklist](./checklist/shared-shell-and-reservation-handoff.md) |
| About Menu / Reserve handoff | Retired. About now ends with Relationships. | [About culture revision](./checklist/about/2026-08-13-culture-revision.md) |
| About three-image Working Details group | Retired and replaced by the Cooking story sequence. | [About culture revision](./checklist/about/2026-08-13-culture-revision.md) |
| Earlier non-brand-aligned Reserve content | Removed and replaced by a compact native request scope. | [Snapshot](./history/project-pre-migration-2026-08-15.md), [Reserve Checklist](./checklist/reserve.md) |
| Six-state-only `ChefStoryRow` contract | Superseded by eight paired states including Wide Phone `599`. | [Chefs Checklist](./checklist/chefs/chefs.md) |
| Separate Chefs `Background` and `Cooking Perspective` property claim | Superseded in the later audit by the documented single `Content` Rich Text property. | [Chefs Checklist](./checklist/chefs/chefs.md) |

## Implementation chronology and evidence routes

### 2026-08-11: Home audit and Menu revision

- The Home belief-to-evidence sequence, visual system, fixed chapters, and DishSelector were read from the live Canvas.
- Menu Opening and Changing Menu Statement were rebuilt from approved reference compositions.
- One reusable `MenuDishCard` was created and applied to seven dishes across Desktop, Tablet, and Phone.
- Exact Menu root ids, variant paths, component evidence, image ownership, and initial build order remain in the [snapshot](./history/project-pre-migration-2026-08-15.md) and [Menu Checklist](./checklist/menu.md).

### 2026-08-12: Menu handoff, shared button work, and Reserve rebuild

- A Demo Menu reservation handoff and reusable `ButtonPrimary` were documented before the later shared-handoff consolidation.
- Reserve was rebuilt from an empty page as a compact Demo request scope, then expanded into a labelled native reservation-request form with `ReservationSubmit` states.
- Exact historical geometry, Demo contacts, copy, and state notes remain in the [snapshot](./history/project-pre-migration-2026-08-15.md) and [Reserve Checklist](./checklist/reserve.md).

The following page-specific Menu handoff checks are retained verbatim from that superseded contract. They are historical evidence, not current work items:

- [x] Use `Reserve a seat` consistently.
- [x] Reuse the shared `ButtonPrimary` component.
- [ ] Link to a real Reserve page or booking destination.
- [x] Use clearly marked fictional Demo contact values until verified production details exist: `reservations@aurelia.example`, `+1 212 555 0148`, and `18 Aurelia Lane, New York, NY 10013`.
- [x] Make the Demo email and telephone directly clickable while retaining an explicit replace-before-publish notice.
- [x] Preserve the dark conclusion without mechanically duplicating Home Invitation: Desktop uses an asymmetric lead and three-column contact band, Tablet tightens the split, and Phone changes to a single-column contact sequence.
- [x] Verify the optimized Handoff visually at Desktop, Tablet, and Phone component screenshots.

### 2026-08-13: About and Chefs revisions

- About's outer `5px` gap was corrected to `0px`; Exterior was inserted; Working Details was replaced by Cooking; About Handoff was removed.
- `Type/Story` was created and used for Working Method, Cooking, and Relationships. Relationships and Cooking became long vertical story/image sequences.
- Chefs responsive width ownership was corrected: full-width outer surfaces, bounded inner wrappers, preserved Phone portrait `350 x 440px`, and component-owned `32 / 28 / 20px` padding.
- Exact node ids, image frames, Story nodes, source ratios, and visual evidence are preserved in the two [About request Checklists](./checklist/about/) and the [Chefs responsive Checklist](./checklist/chefs/2026-08-13-responsive-and-outer-width.md).

The following About Preview routes were superseded when the page's in-page Menu / Reserve ending was retired. They are retained verbatim as historical evidence:

- [ ] Desktop: Navbar → opening → statement → working details → Menu link → Reserve CTA → Footer.
- [ ] Phone: Menu open/close → long-name case → image sequence or Lightbox → CTA.

#### Superseded Chefs planning assertions

These original checklist lines predate the later live audit. They are retained verbatim, but the current `ChefStoryRow` contract has eight states, one `Content` Rich Text Property, an established primary-navigation route, and a shared Reservation Handoff:

- [ ] End quietly after the third chef; do not duplicate Home Invitation or force another reservation CTA.
- [ ] Use Component Properties for portrait, Alt, name, role, background, viewpoint, and labels; never create one Variant per chef's content.
- [ ] Use compact structural Variants only: Desktop Collapsed, Desktop Expanded, Tablet Collapsed, Tablet Expanded, Phone Collapsed, Phone Expanded.
- [ ] Navigation decision, `STATUS.md`, `DECISIONS.md`, and the single latest `RECOVERY.md` checkpoint are synchronized.

#### Superseded Chefs build checkpoint (verbatim)

Scope: Chefs page structure, `ChefStoryRow` component, three portrait instances, Desktop / Tablet / Phone layouts  
Status: Partial Pass — factual profile content and final QA Blocked

Pass:

- Created `/chefs` using the existing shared Layout Template; Navbar and Footer were not copied into the page.
- Created one native `ChefStoryRow` component with editable Portrait, Chef Name, Chef Role, Background, and Cooking Perspective Properties.
- Added Desktop, Tablet, and Phone collapsed/expanded component structures; Page Instances select the matching collapsed variant at each authored breakpoint.
- Built exactly three vertically sequenced instances with left portrait / right identity on Desktop and Tablet, and portrait → name → button → story order on Phone.
- Uploaded and assigned the three approved portrait assets: `chef-portrait.webp`, `chef-bar.webp`, and `chef-plate.webp`.
- Kept visible profile text intentionally Demo-only; no names, biographies, awards, dates, or claims were invented.
- Targeted structural readback confirms the page and content scope exist at Desktop 1200, Tablet 810, and Phone 390, with the expected shared-template relationship and independent instance properties.

Fix Required:

- Replace `Chef One`, `Chef Two`, and `Chef Three`, their roles, Background, and Cooking Perspective with approved profile material.
- Write specific per-portrait Alt text through the final image-editing path; current upload endpoints did not preserve authored image alt metadata.
- Set Page Title, Meta Description, Open Graph responsibility, final CTA labels, and the primary-navigation decision.
- Run Preview keyboard open/close, Focus, Reduced Motion, 320 / 390 / 810 / 1200 / 1440+, long name, long story, missing role, and image-replacement stress tests.

Blocked:

- Verified chef names, roles, biographies, viewpoints, and any factual claims are missing.
- A single bounded Framer screenshot request returned no result in this build pass; do not treat structural readback as a visual screenshot pass.

Recovery state:

- Framer session: 3
- Page: `/chefs`
- Page id: `zz0sK4qC1`
- Component: `ChefStoryRow` (`w84t84ST7`)
- Page content root: `O0dtSoRtO`
- Last successful change: three profile instances and Desktop / Tablet / Phone configuration added.
- Next Part: obtain approved profile content, then run the blocked visual and interaction QA without restructuring the page first.

### 2026-08-14: Component audits, button states, and shared-shell repair

- The Button system gained White/Dark Small and Hover pairs using `12px x 18px` padding, `10px` labels, and `spring-physics 250 30 1 0s`.
- `ChefStoryRow` was audited as eight paired states across Desktop, Tablet, Phone, and Wide Phone `599`; layer naming and exact implementation were documented.
- Tablet Expanded adopted the white `Back` close affordance and the latest documented Medium `Type/Story` value of `12px`.
- The Layout Template clipping failure was traced to fixed `1000px` roots using `overflow: clip`; fixed heights were retained and root overflow was returned to visible.
- Exact current component contracts are routed below under Precision and implementation references.

### 2026-08-15: Shared navigation, Footer, and Reservation Handoff

- Chefs was added to the shared Navbar.
- Footer navigation was completed for Home, Menu, About, Chefs, and Reserve with Demo email and telephone.
- Private Dining was retired from the current plan.
- One shared `Reservation Handoff` was applied to Home, Menu, and Chefs with page-specific copy and one `/reserve` action.
- Desktop and Tablet evidence passed targeted readback; Phone static visual confirmation remains open because the measurement path returned a `200 x 200` editor placeholder.
- Complete scope, copy, regression notes, and current open checks remain in the [shared-shell Checklist](./checklist/shared-shell-and-reservation-handoff.md).

The earlier Home checklist line “Replace the blocked destination only when the real Reserve page or provider exists” is retired: `/reserve` now exists as the internal request destination, while production form/provider behavior remains blocked.

## Precision and implementation references

| Subject | Authoritative detailed route |
|---|---|
| Original exact project parameters, ids, content, and evidence | [Pre-migration snapshot](./history/project-pre-migration-2026-08-15.md) |
| Menu expandable card tree, dimensions, variants, properties, motion, and Preview matrix | [Expandable editorial card](../../framer/advance-design/aurelia/expandable-editorial-card.md) |
| Chef story row tree, eight states, dimensions, padding, routes, and recovery | [Chef story row](../../framer/advance-design/aurelia/chef-story-row.md) |
| DishSelector responsive image matrix | [Dish selector image matrix](../../framer/advance-design/aurelia/dish-selector-image-matrix.md) |
| DishSelector image-strip and number-reel mechanics | [Image strip number reel](../../framer/advance-design/aurelia/image-strip-number-reel.md) |
| Current `Button` White / Dark Small states and exact 2026-08-14 evidence | [Reusable Button pattern](../../framer/basic/patterns/buttons.md), [pre-migration snapshot](./history/project-pre-migration-2026-08-15.md) |
| Legacy `ButtonPrimary` internal filler technique | [Button filler hover](../../framer/advance-design/aurelia/button-filler-hover.md) |
| About node ids, exact frame dimensions, `Type/Story` history, and image order | [About request Checklists](./checklist/about/) |
| Chefs page/component ids, old exception ids, responsive widths, and audit deltas | [Chefs Checklist](./checklist/chefs/chefs.md) |
| Shared Template failure, repair path, Navbar/Footer/Handoff evidence | [Shared-shell Checklist](./checklist/shared-shell-and-reservation-handoff.md) |

## Request-level history

- [About culture revision, 2026-08-13](./checklist/about/2026-08-13-culture-revision.md)
- [About Story typography and Relationships, 2026-08-13](./checklist/about/2026-08-13-story-typography-and-relationships.md)
- [Chefs responsive and outer-width revision, 2026-08-13](./checklist/chefs/2026-08-13-responsive-and-outer-width.md)
- [Chefs page contract and completion audits](./checklist/chefs/chefs.md)
- [Shared shell and reservation handoff](./checklist/shared-shell-and-reservation-handoff.md)
- [Progressive-disclosure migration request](./checklist/knowledge-architecture/2026-08-15-progressive-disclosure-migration.md)
