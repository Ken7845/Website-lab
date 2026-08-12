# Menu Page Checklist

Page: Menu  
Path: `/menu`  
Status: Requested revision implemented; full-page QA in progress  
Primary CTA: `Reserve a seat`  
Content status: Planned Demo

## Definition of Ready

- [x] Page purpose and approved information architecture are recorded in `PROJECT.md`.
- [x] Existing food assets and seven Demo dish stories are available as starting material.
- [x] Use one reusable long-form Dish Card component with externally editable Properties for the current seven dishes; do not create one content Variant per dish.
- [x] Approve the revised direction for a simple Opening, a full-screen Changing Menu Statement, and seven long-form dish cards based on the current Centre of the Meal card.
- [ ] Approve the exact short Opening title, short Changing Menu Statement heading, long story copy, movement names, and final CTA copy.
- [ ] Decide whether prices are intentionally omitted or supported as an optional field.
- [ ] Confirm dietary wording before presenting it as restaurant policy.
- [x] Declare this revision's included Sections and exclusions before Canvas work.

## Current revision scope and constraint lock

Included:

- Menu Opening composition and image ownership.
- Changing Menu Statement structure and long-form Demo story copy.
- One reusable long-form Dish Card component, applied to all seven dishes.
- Dish names, long descriptions, and images sourced from the existing `DishSelector` component and AURELIA content-library assets.
- Desktop, Tablet, and Phone behavior for every changed Section and component instance.

Excluded from this revision:

- Inventing prices, dietary policy, sourcing claims, booking details, or other operational facts.
- Changing the shared Navbar, Footer, Reserve destination, Home `DishSelector`, or other pages.
- CMS migration unless a later buyer-editing audit proves frequent add/remove/reorder is required.

User-approved direction:

- Opening must be simple and must not retain the current generic left-text/right-image split.
- Reference direction added on 2026-08-11: Opening uses a large upper field, an oversized full-width `menu` h1, one compact supporting line, and a left-owned image entering from below the title, following the supplied Paul Kalkbrenner music-page composition without copying its content.
- Reference direction added on 2026-08-11: Changing Menu Statement uses the soft-grey surface with an oversized left headline and a narrow right evidence column beginning with a small food image followed by dense long-form copy.
- The Opening image must be fully legible in its intended crop; the subject cannot be accidentally cut off by the container.
- Changing Menu Statement becomes a full-screen story section with one short large heading and substantially more small body copy.
- The story may discuss ingredient condition, dish character, seasonality, and kitchen decisions, but all text remains clearly Demo and cannot introduce unsupported sourcing or sustainability claims.
- The current Centre of the Meal card is the visual and structural reference for every dish card.
- All seven dishes use the same reusable long horizontal card system on Desktop: image, dish name, and long description.
- Tablet and Phone transform the shared card layout for their available width; they do not squeeze the Desktop horizontal composition.
- Desktop and Tablet dish cards add one shared click-to-expand interaction: the card becomes taller, the image enlarges, Dish Name and short Description both disappear, the text area becomes the editable long Story only, and Home's `Arrow Essentials / Arrow Right` changes to the same set's `Arrow Up`.
- Desktop and Tablet use one shared Hover treatment per breakpoint without scale or external size change. Phone remains a static card with no arrow, Hover, or expand event.
- Repetition is intentional for editability and consistency. Visual rhythm should come from spacing, image crop, sequencing, and movement grouping rather than seven separate card designs.

## Page narrative

```text
Simple Menu Opening
→ full-screen Changing Menu Statement
→ seven-dish long-form card sequence
→ movement pacing: opening / centre / close
→ practical note
→ reservation
```

The page must explain food more clearly than Home while avoiding another Evening Chapters table or embedding another `DishSelector`. The seven dish cards reuse content from `DishSelector`, not its reel interaction or state model.

## Section build checklist

### 1. Opening

- [x] Use exactly one h1.
- [x] Keep the composition simple and immediately legible.
- [x] Replace the current generic left-text/right-image split with a composition that gives the short title and image clear independent ownership.
- [x] Do not mechanically copy the Home image-only Hero.
- [x] Let the Opening image enter from below the title field as in the approved reference; do not force the entire image into the initial viewport.
- [x] Do not add an eyebrow, price, CTA stack, or metadata strip without a real need.
- [x] Use an image ratio and container model that shows the intended subject clearly instead of cropping it accidentally.
- [ ] Recheck focal point independently at Desktop, Tablet, and Phone; do not reuse one fixed crop when it hides the subject.
- [x] Image role and Alt are explicit.

### 2. Changing Menu Statement

- [x] Build this as a full-screen story section, not a short supporting paragraph.
- [x] Use one short large heading and a substantially longer small-text narrative.
- [x] Explain what changes and what remains consistent through ingredients, dish character, seasonality, texture, temperature, and kitchen judgment.
- [x] Keep every claim Demo; avoid unsupported locality, supplier, provenance, organic, sustainability, or health claims.
- [x] Organize the long copy into readable paragraphs or columns with a clear sequence, not one oversized unbroken text block.
- [ ] Keep line length, contrast, paragraph spacing, and reading order comfortable at all five verification widths.
- [x] Use a layout family clearly different from both the Opening and the dish-card sequence.
- [x] The Section remains visually calm despite the increased text volume; one small evidence image begins the right column, with no decorative labels or cards.

### 3. Opening dishes

- [x] Use a semantic h2 and accessible item hierarchy.
- [x] Establish the reusable long-form Dish Card component before duplicating content.
- [x] Use the current Centre of the Meal card as the structural reference: a long horizontal Desktop composition with image, dish name, and long description.
- [x] Add intentional Tablet and Phone component Variants that preserve the same content model while changing the layout for narrow widths.
- [x] Expose dish name, short description, detailed Story, image, and image Alt as buyer-editable instance content; optional dietary note, optional price, order, and visibility remain future requirements where applicable.
- [x] Source names and long descriptions from the seven existing `DishSelector` dishes; do not write a second conflicting dish-content set.
- [ ] Hidden optional fields leave no empty gap or separator.
- [x] Do not create content-specific Variants for individual dishes.
- [x] Desktop and Tablet collapsed cards use the exact Home `Arrow Essentials / Arrow Right` treatment (24×24, `#1A1A1A`, stroke 1.6) inside a 44×44px affordance, a shared Gesture Hover Variant, and exact click paths to their matching Expanded Variant.
- [x] Expanded cards increase image and card height, hide Dish Name and Description, show only Story in the text column, and use `Arrow Essentials / Arrow Up`; Phone explicitly clears the inherited click action and hides the arrow.
- [x] All normal, Expanded, and Gesture states use `spring-physics 250 30 1 0s`; stiffness is fixed at 250.

### 4. Image interruption

- [ ] Reassess whether a separate major food image is still needed after the full-screen story and seven image-led dish cards are in place.
- [ ] Keep it only if it creates a necessary pacing break rather than duplicating imagery already carried by the dish cards.
- [ ] Choose a crop and scale not already used by Home Signature.
- [ ] Verify output size, focal point, and Alt across all breakpoints.
- [ ] Motion is limited to one native appear or restrained inner-image behavior.

### 5. Centre of the meal

- [x] Preserve the current Centre of the Meal card's successful image/name/description relationship as the canonical Dish Card pattern.
- [x] Apply that reusable pattern consistently across the relevant movement without rebuilding the card as unrelated Frames.
- [x] Increase typographic density without turning the page into a long bordered specification table.
- [x] Stress-test the seven source dish titles and multi-line descriptions at the three authored breakpoints.
- [x] Verify image ratios and long descriptions do not change the component's external width or break movement rhythm.

### 6. Close of the meal

- [ ] Reduce density and reopen white space.
- [ ] Keep dessert and closing content structurally editable through the same Dish Card Properties.
- [ ] Preserve the shared card structure while varying surrounding spacing and sequence so the closing movement feels more open.

### 6A. Seven-dish coverage

- [x] Exactly seven dish-card instances are present unless the source `DishSelector` count changes with explicit approval.
- [x] Every instance has an image, dish name, and long description sourced from the existing `DishSelector` content.
- [x] Every image maps to the intended AURELIA dish asset and has a specific per-instance Image Alt decision.
- [x] No dish is omitted, duplicated, or assigned another dish's description.
- [x] Changing one instance's name, description, or image from the page does not alter the other six instances.
- [x] Updating the shared component's layout propagates consistently to all seven instances.

### 7. Practical note

- [ ] Show menu format, dietary accommodation, and price only when verified.
- [ ] Missing fields are hidden, not replaced with invented values.
- [ ] If a dietary-contact link exists, it uses a real destination.

### 8. Reservation handoff

- [x] Use `Reserve a seat` consistently.
- [x] Reuse the shared `ButtonPrimary` component.
- [ ] Link to a real Reserve page or booking destination.
- [x] Use clearly marked fictional Demo contact values until verified production details exist: `reservations@aurelia.example`, `+1 212 555 0148`, and `18 Aurelia Lane, New York, NY 10013`.
- [x] Make the Demo email and telephone directly clickable while retaining an explicit replace-before-publish notice.
- [x] Preserve the dark conclusion without mechanically duplicating Home Invitation: Desktop uses an asymmetric lead and three-column contact band, Tablet tightens the split, and Phone changes to a single-column contact sequence.
- [x] Verify the optimized Handoff visually at Desktop, Tablet, and Phone component screenshots.

## CMS or component gate

- [x] Document the reusable Dish Card component choice in `PROJECT.md` Decisions before Canvas implementation is marked complete.
- [x] Use a reusable Component + Properties for the current seven dishes.
- [x] CMS is introduced only if a later buyer-editing audit proves frequent add/remove/reorder is required.
- [ ] If CMS is introduced later, its fields have buyer-facing names and complete Demo defaults.
- [x] No test fields or duplicate content Properties.
- [ ] Added items do not require new Variants.
- [ ] Stress-test long title, long description, missing image, portrait image, landscape image, missing price, and missing dietary note.
- [x] Provide a short editing note explaining how buyers edit each page instance's image, dish name, description, and order.

## Shared system and links

- [x] Page continues to use the shared Layout Template; Navbar and Footer were not duplicated or modified in this revision.
- [ ] Navigation current state works without duplicating Navbar variants.
- [ ] Logo links to `/`.
- [ ] Main CTA is available in the body, not only Footer.
- [ ] No link targets Draft or missing pages.
- [x] Dish-card Hover does not scale or change the row's external dimensions; it uses shared Surface, Border, and arrow emphasis only.

## Responsive ownership

- [x] Desktop max-width, gutters, image scale, and density change are intentional.
- [x] Tablet rebalances menu columns and gaps rather than shrinking Desktop.
- [x] Phone uses a natural single-column order and no horizontal menu table.
- [ ] 320/390: long titles, optional prices, dietary notes, and CTA do not overflow.
- [x] The Desktop/Tablet arrow affordance is 44×44px and the full card is clickable; Phone remains a non-interactive content card.
- [x] All 21 responsive dish-card Page Instances use Fill (`1fr`) width inside the `Centre of the Meal` Stack, so Preview width follows the surrounding container/border rather than a relative fixed length.
- [ ] Verify 320, 390, 810, 1200, and 1440+.

## SEO, accessibility, and performance

- [x] Unique Page Title and Meta Description.
- [x] Exactly one h1; movement titles use h2; dish titles use h3 only when their relationship warrants it.
- [x] All seven dish-card images have specific Alt through the existing Dish Image instance control.
- [ ] Focus is visible on navigation, items with links, and CTA.
- [ ] Keyboard order follows menu reading order.
- [ ] Reduced Motion keeps all content and feedback available.
- [x] Images are sized for their containers.
- [x] No unnecessary Custom Code, repeated components, or content-specific variant sets.

## Targeted Preview

- [ ] Desktop: Opening image crop → full-screen story readability → all seven dish cards → CTA.
- [ ] Tablet: Opening transformation → story column/read order → representative first, middle, and final dish cards.
- [ ] Phone: Opening crop → long story reading order → long dish title → missing optional field case → final card.
- [ ] Component replacement: change one instance's name, long description, and image, then confirm the other six remain unchanged and the shared layout stays stable.

## Menu Page Done

- [ ] Every Section passed its routed Part checklist before the next began.
- [ ] Content, CMS/component model, styles, links, semantics, images, Alt, and interactions are complete.
- [ ] Five widths and targeted Preview pass.
- [ ] Marketplace editing and replacement stress tests pass.
- [ ] Page Status and recovery state are updated in `PROJECT.md`.

## Latest Part Result

Scope: `MenuDishCard` Desktop/Tablet expandable interaction and seven-instance Story content  
Status: Component interaction implemented; full-page QA remains

Pass:
- `MenuDishCard` remains one reusable native Framer Component; content differences are Properties, not dish-specific Variants or Custom Code.
- Added editable `Story` content plus `Desktop Expanded`, `Tablet Expanded`, `Desktop Hover`, and `Tablet Hover` states.
- Desktop path is exact `Desktop → Desktop Expanded → Desktop`; Tablet uses its own exact path. Phone explicitly clears the inherited `onTap`, hides Story Arrow, and stays static.
- Collapsed states retain image, h3 dish name, short Description, and the far-right Home `Arrow Essentials / Arrow Right`; Expanded states enlarge the image, hide both Dish Name and Description, reveal Story as the only text content, and switch to the same set's `Arrow Up`.
- Hover keeps width, height model, padding, gap, and image dimensions identical to the collapsed state; only Surface, Border, and arrow emphasis change.
- Desktop, Tablet, and Phone replicas for all seven dishes now use Fill (`1fr`) Page Instance width. The Framer Style panel and structural readback both confirm container-owned responsive width.
- All five normal Variants plus both Hover Gesture Variants use `spring-physics 250 30 1 0s`; stiffness is fixed at 250.
- Seven distinct Demo-safe Story values and seven specific Image Alt values were written at Page Instance level and inherited correctly by Tablet and Phone replicas.
- First, middle, and final instances were read back across Desktop, Tablet, and Phone; image, name, Description, Story, and breakpoint Variant remained independent and correct.
- New on-demand screenshots passed for Desktop collapsed/expanded, Tablet expanded, and the full Menu page after the Arrow/Story/Fill correction. Framer Preview preflight returned `ready` with zero errors and zero warnings; no publish was performed.
- Reusable implementation guidance is recorded in `framer/advance-design/expandable-editorial-card.md`.

Fix Required:
- Run the full `/menu` Preview at 320, 390, 810, 1200, and 1440+; this component pass does not claim whole-page five-width completion.
- In a live external Page Preview, operate one Desktop and one Tablet card through Hover → Expand → Collapse and confirm keyboard focus presentation. The native event graph and visual steady states passed readback, but the editor canvas did not provide a reliable real-click interaction surface without publishing.
- Reassess the unchanged Kitchen Interruption and complete the untouched practical-note/reservation-link checks during full Menu QA.
- Complete instance replacement stress tests for missing image, portrait/landscape extremes, missing optional fields, and buyer reorder instructions.

Blocked:
- Price and dietary policy are not verified.
- Final booking destination is missing.
