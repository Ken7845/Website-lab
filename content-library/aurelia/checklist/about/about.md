# About Page Checklist

Page: About  
Path: `/about`  
Status: Demo culture structure built; Partial Pass; verified identity and biography Blocked  
Primary CTA: None — this Demo culture page ends with Relationships rather than a reservation handoff.

## Definition of Ready

- [x] Page role is approved in `PROJECT.md`.
- [ ] Supply or approve the chef/host name, portrait, biography, first-person statement, and role.
- [ ] Verify every past restaurant, award, sourcing, team, and process claim before use.
- [ ] Decide whether the page remains visible Demo content until real material exists.
- [ ] Select working-detail imagery through the image workflow.
- [x] About intentionally has no in-page Menu / Reserve handoff; shared Navbar and Footer retain site-wide routes.

## Page narrative

```text
Person
→ reason for AURELIA
→ way of working
→ material details
→ relationship with team, room, and guests
```

The page deepens authorship. It must not repeat the Home Chef section or become a résumé timeline.

## Section build checklist

### 1. Portrait-led opening

- [ ] Exactly one h1.
- [ ] Show verified name and role only when supplied.
- [ ] Use a composition different from Home's tall portrait plus bottom-aligned copy.
- [ ] Keep portrait crop, focal point, output size, and Alt specific.
- [ ] If facts are still Demo, make that status clear in editing guidance and metadata decisions.

### 2. First-person statement

- [ ] Use approved first-person copy with one clear idea.
- [ ] Avoid generic passion, innovation, excellence, and luxury claims.
- [ ] Keep a narrow editorial measure and deliberate pause.
- [ ] Preserve smart apostrophes and quotes in visible copy.

### 3. Working method

- [x] Connect sourcing, repetition, adjustment, and service without unsupported claims.
- [ ] Use a layout family not used by the opening.
- [ ] Decide which content is static and which becomes reusable Properties.
- [ ] Do not create a four-card values grid.

### 4. Working details

- [x] Use a small sequence of hands, materials, preparation, or tools.
- [ ] Avoid another large portrait or generic Gallery.
- [x] Each image has an information role and explicit Alt decision.
- [ ] If a Lightbox is genuinely needed, use the native Lightbox pattern and test open/close at all breakpoints.

### 5. Relationships

- [x] Explain the connection among chef, team, room, and guests.
- [x] Use a vertical story sequence with two source-respecting images, rather than a parallel gallery.
- [ ] Team names and roles appear only when verified.
- [ ] Keep the Section shorter than the corresponding Home narrative body.
- [ ] Avoid testimonials, press logos, awards, or career dates without sources.

### 6. Cultural ending

- [x] End the Demo page with the Relationships Section; do not add a Menu or reservation handoff.
- [x] Keep the shared Navbar and Footer unchanged so their existing paths remain available outside this page narrative.

## Shared system and responsive

- [x] Use the documented shared Layout Template, Navbar, and Footer; About adds no page-specific Button or handoff.
- [x] Shared navigation includes Home, Menu, About, Chefs, and Reserve; live regression remains part of final QA.
- [ ] Desktop uses narrower text columns and closer detail crops than Home.
- [ ] Tablet rebalances text and images without passive scaling.
- [x] Phone keeps identity, statement, process, details, and relationship in natural order without a CTA section.
- [ ] Long name, long role, long quote, and absent optional details do not break layout.
- [ ] Verify 320, 390, 810, 1200, and 1440+.

## SEO, accessibility, and performance

- [ ] Unique Page Title and Meta Description do not present fictional biography as fact.
- [ ] Exactly one h1 and logical h2/h3 hierarchy.
- [x] Images used in this revision have specific Alt.
- [ ] Focus is visible and keyboard order follows reading order.
- [ ] Hover information remains available on touch and keyboard.
- [ ] Reduced Motion preserves all content.
- [x] Revision images use container proportions chosen to keep their visual subject readable.
- [ ] No duplicate Components, content Variants, or unnecessary Custom Code.

## Marketplace stress tests

- [ ] Replace chef name with a much longer name.
- [ ] Replace portrait with landscape and portrait alternatives.
- [ ] Remove team content and confirm no empty Section remains.
- [ ] Double the first-person statement length.
- [ ] Hide awards, press, dates, and claims when absent.
- [ ] Editing instructions identify identity, portrait, story, process images, links, and Demo boundaries.

## Targeted Preview

- [ ] Desktop: Navbar → Opening → Exterior → Statement → Working Method → Cooking → Relationships → Footer.
- [ ] Phone: Menu open/close → the same natural content order → Relationships → Footer; no CTA Section.
- [ ] Keyboard-test links and any image interaction.

## About Page Done

- [ ] All visible identity and biography facts are verified or visibly Demo.
- [ ] Every Section passed its routed checklist.
- [ ] Shared systems, semantics, Alt, links, responsive, Focus, and Reduced Motion pass.
- [ ] Five widths and targeted Preview pass.
- [ ] Marketplace replacement stress tests pass.
- [ ] Current build/QA is updated in `STATUS.md`; the latest continuation pointer is updated in `RECOVERY.md`.

## Latest Part Result

Scope: Culture-page revision  
Status: Structure, story typography, and approved image revision built; factual biography remains Blocked

Pass:
- About ends with Relationships and the shared Footer; no Menu or Reservation Handoff exists in the page narrative.
- Shared site navigation remains available through Navbar and Footer.

Blocked:
- Verified chef/host name, role, biography, first-person story, team information, and claims are missing.
- Framer's targeted screenshot request returned a parameter error; do not treat this as visual confirmation. Desktop and Tablet Section rects, image source ratios, Fill URLs, Alt text and responsive node structure were re-read instead.
- Verified chef/host name, role, biography, first-person story, team information, and claims are still missing; the expanded Method and Relationships copy remains explicitly Demo and must be replaced with approved facts before publication.

## Request-specific work

The current multi-point request is maintained separately from this page contract: [2026-08-13 about culture revision](./2026-08-13-culture-revision.md). Do not merge request-specific execution checklists into this document.
