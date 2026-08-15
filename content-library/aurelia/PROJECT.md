# AURELIA Current Project

- Updated: 2026-08-15
- Platform: Framer
- Project ID: `6EYvZfFo1CleDR77cYUF`
- Project URL: `https://framer.com/projects/6EYvZfFo1CleDR77cYUF`

This manifest answers only: **what is AURELIA now?** It was reconciled from the latest dated project records during a repository-only migration. The actual Framer Canvas remains the final source of truth whenever a future authorized Canvas inspection finds a difference.

Do not preload the project history for ordinary work. Read this file, inspect the actual target when Canvas work is authorized, then load only the relevant page Checklist or implementation reference.

## Knowledge routes

- [Current build and QA status](./STATUS.md)
- [Active decisions](./DECISIONS.md)
- [Current recovery pointer](./RECOVERY.md)
- [Retired directions and implementation history](./HISTORY.md)
- [Page Checklist index](./checklist/README.md)
- [Verbatim pre-migration PROJECT snapshot](./history/project-pre-migration-2026-08-15.md)

## Project identity

- Name: AURELIA
- Product: Marketplace template for an independent, reservation-led restaurant, chef, supper club, or intimate dining concept
- Content status: Fictional Demo and Draft
- Primary visitor action: begin a reservation request
- Primary CTA label: `Reserve a seat`
- Primary CTA destination: `/reserve`
- Demo URL, Remix URL, favicon, Open Graph cover, final asset licensing, and production operations remain incomplete.

All names, menu descriptions, contact details, reservation details, and operational information remain Demo unless separately verified. A buyer must replace or approve them before publication.

## Current sitemap

| Page | Path | Current responsibility |
|---|---|---|
| Home | `/` | Establish AURELIA's worldview through place, belief, people, room, craft, rhythm, dishes, and invitation. |
| Menu | `/menu` | Explain what is served and how the menu changes through a fixed seven-dish editorial system. |
| About | `/about` | Explain the restaurant's shared culture, working method, cooking, and relationships. |
| Chefs | `/chefs` | Introduce three individual Demo voices through expandable portrait stories. |
| Reserve | `/reserve` | Collect a reservation request without implying live availability or confirmation. |

`/private-dining` is retired. Do not create, link, reserve, or restore that page from the archived plan.

## Existing page composition

### Home

```text
Opening
-> Vision
-> Chef
-> Space
-> Craft
-> Experience
-> Signature
-> shared Reservation Handoff
-> shared Footer
```

- Opening remains a centred image-only field. The hidden AURELIA Hero text must stay hidden unless the user explicitly approves a new Hero direction.
- Experience retains four fixed `EveningChapterRow` entries and cursor previews.
- Signature retains the fixed seven-state `DishSelector`; do not replace it with CMS during general cleanup.

### Menu

```text
Opening
-> Changing Menu Statement
-> fixed seven-dish MenuDishCard sequence
-> existing interruption / practical-note scope
-> shared Reservation Handoff
-> shared Footer
```

- `MenuDishCard` is the current content system; CMS remains deferred unless a later buyer-editing audit proves frequent add/remove/reorder is required.
- Desktop and Tablet may expand; Phone remains a static reading experience.

### About

```text
Opening
-> Exterior image
-> Statement
-> Working Method
-> Cooking
-> Relationships
-> shared Footer
```

- About ends with Relationships. It intentionally has no Menu or reservation handoff.
- Identity, biography, team, sourcing, award, and process claims remain Demo or blocked until verified.

### Chefs

```text
Opening
-> three ChefStoryRow instances
-> shared Reservation Handoff
-> shared Footer
```

- Exactly three portrait stories exist in the current Demo structure.
- `/about` owns collective culture; `/chefs` owns individual voices.

### Reserve

```text
Compact opening
-> native reservation-request form
-> Demo result / fallback information
-> shared Footer
```

- Reserve is a request flow, not a confirmed-booking flow.
- No external booking embed or handoff is part of the active direction.
- Live submission remains blocked until a real data destination, privacy handling, policies, and result behavior are supplied.

## Current design language

- Quiet, exact, intimate, contemporary, and observant.
- Editorial rather than decorative luxury.
- Photographs act as evidence of place, authorship, process, and food.
- Copy is short, declarative, concrete, and visibly Demo where facts are unverified.
- White space is an active compositional element.
- Avoid repeated generic cards, decorative badges, numbered sections, fake awards, fake prices, invented facts, review carousels, and sales-heavy luxury language.

Current design dials:

- `DESIGN_VARIANCE: 8`
- `MOTION_INTENSITY: 4`
- `VISUAL_DENSITY: 2`

## Current visual system

### Typography

- Brand / navigation: League Gothic.
- Display and body system: Inter.
- Display: Inter Medium, width axis `92`; Desktop `138px`, Tablet `96px`, Phone `54px`.
- Heading 2: `82 / 62 / 40px` at Desktop / Tablet / Phone.
- Heading 3: `38 / 31 / 27px`.
- Body Large: `26 / 22 / 19px`.
- `Type/Body`: `17 / 12 / 11px` in the documented live preset. The small Tablet and Phone values require accessibility review before broad reuse.
- `Type/Story`: Inter 600. Latest dated evidence records Desktop `14px`, Medium / Tablet `12px`, and Phone `13px`; inspect the live Style before changing or propagating it.
- Compact Button labels: `10px`; verify readability and target size in context.
- Editorial display headings may use the established line-by-line native entrance. Long-form Story/body copy stays static.

### Color

- `Color/Background`: `#FFFFFF`
- `Color/Inverse`: `#151515`
- `Color/Surface`: `#EEEEEC`
- `Color/Text`: `#151515`
- `Color/Muted`: `#6F6F6F`
- `Color/Border`: `#C9C9C7`

The page language is a locked light editorial system with controlled near-black narrative objects and reservation handoffs. Do not introduce an unrelated palette or arbitrary section theme.

### Layout and responsive ownership

- Authored breakpoints: Desktop `1200`, Tablet `810`, Phone `390`.
- Required stress widths: `320` and `1440+`.
- Chefs also has a Wide Phone `599` breakpoint.
- Project gutters: Desktop `32px`, Tablet `28px`, Phone `20px`.
- Major Desktop narrative sections commonly use `220-300px` vertical breathing room.
- Outer Page Content and full-bleed Sections remain full width. Width limits belong to intentional inner wrappers or component contracts.
- Desktop composition transforms for Tablet and Phone; it is not mechanically shrunk.
- Phone uses a strict reading order, stable image ratios, and approximately `44px` interactive targets.
- Component roots own component horizontal padding. Parent Sections own page-level vertical rhythm.

## Current reusable system

| System | Current contract | Detailed route |
|---|---|---|
| Shared `Template` | All five pages use the same Layout Template with shared Navbar, Content Placeholder, and Footer. | [Shared-shell Checklist](./checklist/shared-shell-and-reservation-handoff.md) |
| `Navigation` | Desktop, Tablet, Phone Closed, and Phone Open; compact fixed `35px` system; links to Home, Menu, About, Chefs, and Reserve. | [Navbar/Footer pattern](../../framer/basic/patterns/navbar-footer.md) |
| `Footer` | Shared navigation for the five current pages plus clickable Demo email and telephone; no separate Footer CTA, social links, address, map, or hours. | [Shared-shell Checklist](./checklist/shared-shell-and-reservation-handoff.md) |
| `Reservation Handoff` | One deep-inverse shared component with editable Heading and Supporting Copy; used by Home, Menu, and Chefs; one `Button` links to `/reserve`. | [Shared-shell Checklist](./checklist/shared-shell-and-reservation-handoff.md) |
| `Button` | Shared White / Dark and Small state system with Label, Link, and Click ownership. Small states use `12px x 18px` padding, `10px` labels, and `spring-physics 250 30 1 0s`. | [Current Button pattern](../../framer/basic/patterns/buttons.md), [exact project evidence](./history/project-pre-migration-2026-08-15.md) |
| `EveningChapterRow` | Fixed Home chapter row with component-owned breakpoint padding. | [Pre-migration snapshot](./history/project-pre-migration-2026-08-15.md) |
| `ChapterCursorPreview` | Four visual cursor-preview states for Home Experience. | [Pre-migration snapshot](./history/project-pre-migration-2026-08-15.md) |
| `DishSelector` | Fixed seven-dish Home interaction with dedicated responsive state logic. | [Image matrix](../../framer/advance-design/aurelia/dish-selector-image-matrix.md), [reel pattern](../../framer/advance-design/aurelia/image-strip-number-reel.md) |
| `MenuDishCard` | One reusable editable component. Desktop/Tablet expand; Phone static; Page Instances are Fill. | [Expandable editorial card](../../framer/advance-design/aurelia/expandable-editorial-card.md) |
| `ChefStoryRow` | One editable component with Desktop, Tablet, Phone, and Wide Phone Collapsed/Expanded pairs. | [Chef story row](../../framer/advance-design/aurelia/chef-story-row.md) |
| Reservation field system | Labelled native request fields plus `ReservationSubmit` states for Default, Incomplete, Pending, Success, and Error. | [Reserve Checklist](./checklist/reserve.md) |
| Hero / cursor / scroll | `hero`, `Hero Loader`, custom `AURELIA` cursor, and external `Lenis` remain existing systems. | [Home Checklist](./checklist/home.md) |

## Current cross-page constraints

- Inspect before creating. A request to add a Section may mean reuse, modify, or no-op if the function already exists.
- Home owns the complete worldview; supporting pages deepen one subject and do not replay Home modules.
- Do not duplicate Home `DishSelector`, Home cursor-preview chapters, the Home Space image pair, or another reservation handoff.
- Navbar and Footer remain shared Components, not page copies.
- `Reserve a seat` remains one label and one route across the site.
- About remains handoff-free by design.
- Keep real page paths and shared-component behavior stable unless the user explicitly changes information architecture.
- Prefer native Framer Styles, Components, Variants, Properties, Layout, Effects, and forms. Do not add Custom Code or a paid dependency without approval.
- Preserve Focus, keyboard order, Reduced Motion, content replacement, and all authored breakpoints when modifying a current system.
- No publish is authorized by this documentation.

## Current Demo facts and blockers

| Fact | Current value |
|---|---|
| Brand | `AURELIA` - Demo |
| Address | `18 Aurelia Lane, New York, NY 10013` - Fictional Demo |
| Phone | `+1 212 555 0148` - Fictional Demo |
| Email | `reservations@aurelia.example` - Fictional Demo on reserved `.example` domain |
| Opening hours | Missing |
| Capacity | Missing |
| Menu price | Missing |
| Verified chef identities and biographies | Missing |
| Dietary policy | Missing |
| Booking/form destination and privacy handling | Missing |
| Response time and operating policies | Missing |
| Social links | Missing and intentionally absent from the current Footer |

See [STATUS.md](./STATUS.md) for the current implementation and QA consequences of these blockers.
