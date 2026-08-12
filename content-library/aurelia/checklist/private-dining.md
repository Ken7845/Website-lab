# Private Dining Page Checklist

Page: Private Dining  
Path: `/private-dining`  
Status: To do; operational facts partly Blocked  
Primary CTA: `Reserve a seat` or an approved private-dining enquiry label

## Definition of Ready

- [x] Page purpose and broad structure are approved in `PROJECT.md`.
- [ ] Approve the opening statement and private-dining value proposition.
- [ ] Identify which gathering formats are legitimate Demo examples.
- [ ] Supply or explicitly defer capacity, availability, accessibility, lead time, minimum spend, and included service facts.
- [ ] Decide whether the CTA opens Reserve with a preselected booking type.
- [ ] Select room imagery after the image-workflow residency and contact-sheet checks.

## Page narrative

```text
Room
→ why privacy changes the meal
→ kinds of gathering
→ relationship between table and space
→ verified practical facts
→ enquiry
```

This page should feel wider, more social, and more spatial than the introspective Home.

## Section build checklist

### 1. Room-led opening

- [ ] Exactly one h1 and one primary image role.
- [ ] Use a spatial composition that is not the Home image-only Hero.
- [ ] Keep the initial viewport concise and CTA visibility intentional.
- [ ] Do not invent location, capacity, or exclusivity claims.
- [ ] Verify image crop, focal point, output size, and Alt.

### 2. What private changes

- [ ] Explain pace, service, attention, and menu decisions in concrete language.
- [ ] Avoid generic event-sales or luxury copy.
- [ ] Use a layout family not repeated elsewhere on this page.
- [ ] Keep body width aligned with the chosen page grid.

### 3. Gathering formats

- [ ] Use editable editorial rows or uneven columns, not equal icon cards.
- [ ] Each format has a clear name, short description, optional image, and optional enquiry preset.
- [ ] Decide Component + Properties versus static content; use CMS only if buyers need frequent add/remove/reorder.
- [ ] Missing formats do not leave empty cells.
- [ ] Format hover or link behavior does not change layout size.

### 4. Room and table

- [ ] Create a new wide spatial relationship without copying Home Space's small-plus-large image pair.
- [ ] Images explain how guests occupy the room, not simply decorate the page.
- [ ] Desktop, Tablet, and Phone have independent crop and sequence decisions.
- [ ] Alt describes the useful spatial information.

### 5. Practical facts

- [ ] Fields are limited to verified capacity, availability, accessibility, lead time, minimum spend, and service inclusions.
- [ ] Every Missing field is hidden cleanly.
- [ ] Do not use placeholder numbers, fake ranges, or decorative progress bars.
- [ ] If facts exceed five items, group them into meaningful clusters rather than a long hairline table.
- [ ] Address, phone, email, and map become clickable only when real.

### 6. Enquiry handoff

- [ ] CTA wording describes the actual result.
- [ ] Link points to a real page or provider.
- [ ] If Reserve supports booking type, verify the preselected private-dining state.
- [ ] Provide a verified fallback contact path when submission is unavailable.

## Shared system and responsive

- [ ] Use shared Layout Template, Navbar, Footer, and Buttons.
- [ ] Add the page to navigation only after its path exists and the page is reviewable.
- [ ] Desktop uses wide horizontal relationships with controlled max-width.
- [ ] Tablet reduces span complexity and preserves room relationships.
- [ ] Phone follows a strict reading order: meaning before facts before enquiry.
- [ ] 320/390 practical facts and long format names do not overflow.
- [ ] Touch targets are approximately 44px or larger.
- [ ] Verify 320, 390, 810, 1200, and 1440+.

## SEO, accessibility, images, and motion

- [ ] Unique Page Title and Meta Description.
- [ ] Exactly one h1 with logical h2/h3 structure.
- [ ] All images have specific Alt or explicit empty Alt.
- [ ] Focus and keyboard order match the visual path.
- [ ] Information exposed on hover remains visible or accessible on touch and keyboard.
- [ ] Motion uses native effects, serves spatial hierarchy, and has a Reduced Motion fallback.
- [ ] Image sizes match containers and do not reuse oversized originals.
- [ ] No unapproved Custom Code or third-party dependency.

## Marketplace stress tests

- [ ] Remove one gathering format.
- [ ] Double one format description length.
- [ ] Replace a landscape room image with a portrait image.
- [ ] Hide every optional practical fact.
- [ ] Add all verified practical facts and confirm the page still breathes.
- [ ] Editing instructions identify format content, images, facts, CTA destination, and visibility controls.

## Targeted Preview

- [ ] Desktop: Navbar → opening → formats → room composition → enquiry → Footer.
- [ ] Phone: Menu open/close → formats → missing-facts case → enquiry.
- [ ] Test one real CTA destination and its return path.

## Private Dining Page Done

- [ ] Every Section passed its routed checklist.
- [ ] Missing facts are hidden or documented Blocked.
- [ ] Shared systems, semantics, Alt, links, responsiveness, Focus, and motion pass.
- [ ] Five widths and targeted Preview pass.
- [ ] Marketplace replacement stress tests pass.
- [ ] `PROJECT.md` Build Status Matrix and Recovery State are updated.

## Latest Part Result

Scope: Page plan  
Status: To do

Blocked:
- Capacity, availability, accessibility, lead time, minimum spend, service details, and booking destination are missing.
