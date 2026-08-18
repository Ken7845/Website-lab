# AURELIA Active Decisions

Updated: 2026-08-15

This file contains only decisions that are still active. Retired and superseded directions live in [HISTORY.md](./HISTORY.md). The actual Canvas and later explicit user decisions take precedence over this record.

## Information architecture

### D-01: Five-page current sitemap

The current site is Home `/`, Menu `/menu`, About `/about`, Chefs `/chefs`, and Reserve `/reserve`.

`/private-dining` is retired and must not be created, linked, or reserved. The five current pages already separate worldview, food, shared culture, individual voices, and reservation action without another parallel offer page.

### D-02: Home is belief-to-evidence

Home moves from Place to Belief to Person to Room to Craft to Rhythm to Dishes to Invitation. It is not a literal arrival-to-reservation chronology.

Supporting pages deepen one subject and must not replay Home's sections under new headings.

### D-03: One reservation intent

`Reserve a seat` is the single primary reservation label and routes to `/reserve` across the shared system.

Reserve collects a request. It must not imply live availability, successful submission, or a confirmed seat until a real service confirms those states.

## Page decisions

### D-04: Home Opening remains image-only

The centred architecture image, surrounding white field, restrained parallax, and absence of visible Hero copy or CTA remain active. The hidden AURELIA text layer stays hidden unless the user explicitly approves a new Hero direction.

### D-05: Home narrative systems remain fixed

- `EveningChapterRow` remains a fixed four-part Home system with cursor previews.
- `DishSelector` remains a fixed seven-dish Home component with its existing responsive and transition logic.
- Neither system is converted to CMS during unrelated cleanup.

### D-06: Menu uses one reusable fixed-source card system

The current seven dishes use one `MenuDishCard` Component with editable image/Alt, name, Description, and Story Properties. Content differences remain instance Properties, not dish-specific Variants.

- Desktop and Tablet: Collapsed, Hover, and Expanded behavior.
- Phone: static, with no arrow or inherited `onTap`.
- Collapsed uses Home's `Arrow Essentials / Arrow Right`; Expanded hides name and short Description, gives Story full text ownership, and uses `Arrow Up`.
- Page Instances remain Fill (`1fr`).
- Current motion contract: `spring-physics 250 30 1 0s`.

The exact tree, dimensions, routes, validation matrix, and replacement contract live in [Expandable editorial card](../../framer/advance-design/aurelia/expandable-editorial-card.md).

CMS remains deferred until a real buyer-editing requirement calls for frequent add/remove/reorder workflows.

### D-07: About ends with culture

About ends with Relationships and the shared Footer. It intentionally has no Menu or reservation handoff. The page explains collective culture and does not duplicate Home Chef or Chefs individual profiles.

### D-08: Chefs uses expandable individual stories

Chefs contains exactly three `ChefStoryRow` instances in a vertical editorial sequence. The live documented system has Desktop, Tablet, Phone, and Wide Phone `599` Collapsed/Expanded pairs, component-owned padding, same-breakpoint open/Back routes, and `spring-physics 250 30 1 0s` roots.

The exact component contract lives in [Chef story row](../../framer/advance-design/aurelia/chef-story-row.md). Current identities and stories remain Demo until approved.

### D-09: Reserve is a native request form

Reserve uses a native labelled reservation-request form rather than an external booking embed or a fake confirmed-booking flow.

Current request essentials are Name, Email, Preferred date, Party size, Booking type, and optional Message. `ReservationSubmit` owns Default, Incomplete, Pending, Success, and Error structures. Live behaviors remain blocked until the real destination and data-handling rules exist.

## Shared-system decisions

### D-10: One Layout Template, Navbar, and Footer

All five pages use one shared `Template`. Navbar and Footer are shared Components, not page copies.

The Template keeps its Framer-required fixed `1000px` authored root heights while allowing page content to remain visible through non-clipped root overflow. Do not patch individual pages for a shared-source defect unless an intentional page exception is documented.

### D-11: Compact native Navbar model

Navigation remains a fixed `35px` shared component with Desktop, Tablet, Phone Closed, and Phone Open Variants.

- Links: Home, Menu, About, Chefs, Reserve.
- No additional Navbar CTA.
- No scroll-hide/show behavior.
- Phone remains a native Closed/Open Variant drawer, not an Overlay.
- Press feedback is native, restrained, non-scaling, and must not reflow the link row.

### D-12: One shared Reservation Handoff

Home, Menu, and Chefs use one native `Reservation Handoff` component immediately before the shared Footer. Heading and Supporting Copy are page-editable; the CTA label and `/reserve` destination are shared.

Do not create another Invitation, CTA block, or reservation section on those pages before checking the existing shared instance.

### D-13: Shared Footer remains informational

The Footer contains navigation for the five current pages plus clickable fictional Demo email and telephone. It has no separate CTA, social links, address, map, or hours in the active scope.

### D-14: Button systems own their interaction geometry

Reusable Buttons own Label, Link, Click boundary, padding, visible state, and state transitions. Page Frames do not redraw or artificially stretch them.

The active Small variants use `12px x 18px` padding, `10px` labels, and `spring-physics 250 30 1 0s`. The current contract is routed to [Buttons](../../framer/basic/patterns/buttons.md) and the [exact project snapshot](./history/project-pre-migration-2026-08-15.md). [Button filler hover](../../framer/advance-design/aurelia/button-filler-hover.md) preserves the earlier `ButtonPrimary` filler technique; it is not evidence for the current White / Dark Small state set.

## Visual and responsive decisions

### D-15: Preserve the established editorial system

Large Inter editorial type, League Gothic brand details, white / near-black / soft-grey tokens, sharp image edges, narrow body measures, asymmetric image relationships, and long pauses remain the shared visual language.

The controlled near-black Handoff is an approved narrative conclusion inside the established system, not permission to introduce unrelated section themes.

### D-16: Width ownership belongs at the correct layer

Outer Page Content and full-bleed Sections remain full width. `max-width` belongs only to intentional inner wrappers or component contracts.

Reusable component roots own their horizontal padding. Parent Sections own page-level vertical rhythm. Responsive work must preserve this ownership instead of compensating with arbitrary fixed widths or absolute positioning.

Long bordered rows such as `EveningChapterRow` and `FAQ Row` keep their root/list and external instances Fill. Their border should respond to available page width; only a true inner reading measure or fixed-geometry contract may be bounded.

### D-17: Breakpoints transform independently

Desktop `1200`, Tablet `810`, and Phone `390` are authored compositions; Chefs also has Wide Phone `599`. Stress checks include `320` and `1440+`.

A Desktop left/right composition is a Desktop intent, not a command to squeeze Phone into the same relationship. Phone gets its own reading order, image contract, and touch behavior.

## Content and verification decisions

### D-18: Unverified content remains visibly Demo

Do not invent chef identities, biographies, operations, hours, capacity, price, dietary policy, sourcing, awards, service details, response time, or booking behavior. Missing optional facts disappear cleanly.

The current `.example` email, `555` phone number, and Aurelia Lane address are presentation-only Demo values and must never be described as verified operations.

### D-19: Inspect before creating or changing

Before adding a Section, component, CTA, or handoff, inspect the current page and shared system. Decide whether the correct action is Add, Reuse, Modify, or No-op.

For existing design work, current Canvas patterns and approved project language take precedence over generic aesthetic defaults.

### D-20: Verification is targeted and evidence-labelled

Structural readback remains mandatory. Advanced visual and interaction conclusions use the smallest reliable evidence path plus user visual approval. Browser Preview is not a default substitute for user judgment; use it when the user requests it or when real behavior cannot be established through structure and targeted evidence.

Never promote a structural readback, editor replica, or `200 x 200` placeholder to a rendered Phone pass.

### D-21: No implicit publication

No knowledge-base update, structural audit, screenshot, or preflight authorizes publishing the Framer project.
