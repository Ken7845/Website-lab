# Home Page Checklist

Page: Home  
Path: `/`  
Status: Built; Fix Required full regression and shared-system sign-off
Primary CTA: `Reserve a seat`

## Scope lock

The current documented sequence is:

```text
Opening → Vision → Chef → Space → Craft → Experience → Signature → shared Reservation Handoff → Footer
```

- [x] Current narrative and Desktop visual rhythm were read from the live Canvas on 2026-08-11.
- [ ] Do not restore the retired arrival-to-reservation structure.
- [ ] Do not make the hidden Hero AURELIA text visible without explicit approval.
- [ ] Do not replace the fixed Evening Chapters or seven-state DishSelector with CMS during general cleanup.
- [ ] Preserve user-edited Phone DishSelector state layouts unless the current task explicitly targets them.

## Shared shell

- [x] Home is documented under the final shared Layout Template; final visual regression remains open.
- [x] The compact shared navigation and its Desktop / Tablet / Phone variants were preserved during consolidation.
- [x] Shared primary navigation now links Home, Menu, About, Chefs, and Reserve.
- [ ] Keep useful Home anchors available as contextual or Footer links.
- [x] Logo links to `/`; the shared Handoff CTA links to the existing `/reserve` request page.
- [x] Footer uses the shared component with five-page navigation and clearly fictional Demo email / telephone; it has no address, hours, social links, map, or separate CTA.
- [ ] Complete final shared Template / Navbar / Footer / Handoff visual and Phone sign-off through the [shared-shell Checklist](./shared-shell-and-reservation-handoff.md).

## Section checks

### Opening

- [ ] Preserve the centred architecture image, surrounding white field, and absence of visible copy or CTA.
- [ ] Verify 100vh and minimum-height behavior under mobile browser chrome.
- [ ] Recheck Hero image crop and focal point at 320, 390, 810, 1200, and 1440+.
- [ ] Verify the restrained parallax target and Reduced Motion fallback.
- [ ] Confirm hidden overlay and text layers remain non-visible and do not affect accessibility or layout.
- [ ] Add or verify the Hero image Alt decision.

### Vision

- [ ] Preserve the image-free typographic pause.
- [ ] Confirm exactly one semantic heading level appropriate to the page hierarchy.
- [ ] Verify Display line reveal and static Reduced Motion reading order.
- [ ] Check the narrow body column and heading wrap at all five widths.

### Chef

- [ ] Preserve the unequal portrait-and-copy relationship on Desktop.
- [ ] Recheck Tablet reflow and Phone reading order.
- [ ] Verify portrait crop, web output size, and specific Alt.
- [ ] Keep biography language visibly Demo until real chef facts are approved.
- [ ] Review the visible dash punctuation during the copy-polish Part without silently changing brand meaning.

### Space

- [ ] Preserve the asymmetric small exterior and larger dining-room composition.
- [ ] Verify each breakpoint owns its image size, focus, and sequence.
- [ ] Confirm both images have specific Alt and are not unnecessarily oversized.
- [ ] Preserve the long gap before the final narrow body copy.

### Craft

- [ ] Preserve the soft-grey surface as the first restrained background change.
- [ ] Verify text and process image retain readable contrast.
- [ ] Confirm the image enters once and does not replay excessively.
- [ ] Recheck text spacing in `Time is an ingredient.` and remove accidental whitespace only in an authorized copy/layout Part.

### Experience

- [ ] Keep four fixed chapters in the approved order.
- [ ] Verify all page instances use the correct EveningChapterRow device variant.
- [ ] Verify chapter title, description, image property, cursor target, and hover value for every row.
- [ ] Desktop and Tablet: test one representative hover plus first, middle, and last cursor transition.
- [ ] Phone: keep all chapter information visible without relying on hover.
- [ ] Recheck divider contrast, long-description stress, row height, and title wrapping.
- [ ] Verify the full-width plate image crop and Alt at each breakpoint.
- [ ] Preserve the closing line as a separate narrative beat.

### Signature

- [ ] Verify seven states at Desktop, Tablet, and Phone.
- [ ] Verify first, middle, and last dish states plus one arbitrary state change in Preview.
- [ ] Confirm image, title, long story, and Phone description controls map to the matching dish.
- [ ] Desktop/Tablet: confirm image strip, numeric reel, title reel, description reel, and thumbnail actions remain synchronized.
- [ ] Phone: test 320, 390, and a wider Phone breakpoint; confirm no overlap, overflow, empty grid columns, or accidental absolute offsets.
- [ ] Preserve the current fixed seven-item editing contract.
- [ ] Stress-test a longer title, longer story, portrait image, landscape image, and replaced image with a different focal point.
- [ ] Verify touch interaction does not depend on cursor behavior.

### Shared Reservation Handoff

- [ ] Preserve the near-black conclusion and white text contrast.
- [ ] Verify the CTA uses the shared button structure with Fit content and a click boundary matching its visible bounds.
- [ ] Button hover must not scale or change layout size.
- [ ] Keep `Reserve a seat` on one line.
- [x] Reuse the one shared `Reservation Handoff`; do not recreate the former page-specific Invitation tree.
- [x] `Reserve a seat` links to the existing `/reserve` request page. Production form/provider behavior remains Blocked and does not require a second destination.

### Footer

- [ ] Verify the white return after the dark ending remains intentional.
- [x] Shared Footer navigation links the five current pages; final regression and visual sign-off remain open.
- [ ] Preserve Demo notice and copyright.
- [ ] Phone Footer follows a natural vertical order.

## Styles, semantics, and accessibility

- [ ] Apply the standard line-by-line `onInView` text appearance effect to editorial headings only. Use About Phone → Opening Content → Opening Heading as the visual and timing reference; keep long-form Story/body copy static to avoid scroll lag, and exclude navigation, buttons, controls, form labels, and other functional UI text.
- [ ] Consolidate duplicate text styles only after targeted instance readback.
- [ ] Recheck current 12px Tablet Body, 11px Phone Body, and 10px Button preset before reuse; fix if readability or touch labeling fails.
- [ ] Confirm one page h1 and logical h2/h3 hierarchy.
- [ ] Set a unique Home title and Meta Description.
- [ ] Confirm visible Focus for navigation, buttons, chapter rows where interactive, and DishSelector controls.
- [ ] Confirm keyboard order matches the visual sequence.
- [ ] Confirm all hover-only imagery has equivalent persistent text.
- [ ] Verify Reduced Motion removes parallax and large spatial movement without hiding content.

## Performance

- [ ] Verify Lenis behavior and its known editor-replica sizing caveat without resizing it blindly.
- [ ] Resolve current-scope overflow or zero-size visible-layer diagnostics.
- [ ] Confirm images match container needs and avoid unnecessary original dimensions.

## Marketplace regression

- [ ] A buyer can find and replace Home images, fixed chapter content, chapter cursor images, and all seven DishSelector content groups.
- [ ] Long headings, long chapter descriptions, different image ratios, and missing optional content do not break the page.
- [ ] No test Component, unused Variant, duplicate Style, private data, or unlicensed asset remains in the delivery scope.
- [ ] Home editing instructions explain Styles, Navigation, Footer, Button, EveningChapterRow, ChapterCursorPreview, DishSelector, image focal points, and reservation link ownership.
- [ ] Desktop and Phone template screenshots match the final Canvas.

## Targeted Preview

- [ ] Preview Desktop: Opening → Navigation → one chapter hover → DishSelector → Reserve CTA → Footer.
- [ ] Preview Phone: Menu open → close → core link → chapter reading → DishSelector state → CTA.
- [ ] Verify widths: 320, 390, 810, 1200, 1440+.

## Home Page Done

- [ ] All Section checks above are Pass or documented Blocked.
- [ ] Shared Navbar, Footer, Button, and Layout Template are verified on Home.
- [ ] Metadata, one h1, headings, Alt, links, Focus, and Reduced Motion pass.
- [ ] Targeted Desktop and Phone Preview paths pass.
- [ ] Marketplace replacement and editing-path regression passes.
- [ ] Home row in `STATUS.md` is current; only lasting rationale goes to `DECISIONS.md`, and only the latest continuation pointer goes to `RECOVERY.md`.
- [ ] Latest exceptions and recovery state are recorded.

## Latest Part Result

Scope: Page audit  
Status: Fix Required

Pass:
- Live narrative, Desktop composition, existing components, styles, and content roles were read on 2026-08-11.
- Shared Template, five-page navigation, Footer, and one shared Reservation Handoff linking to `/reserve` are documented as integrated.

Fix Required:
- Complete the remaining page checklist, five-width regression, and shared-shell visual / Phone sign-off.

Blocked:
- Real reservation submission/provider behavior, operational facts, licensing, favicon, and Open Graph cover.

Verified widths:
- Desktop 1200 structurally and visually.
- Tablet 810 structurally.
- Phone 390 structurally; use real Preview for visual conclusions.

Verified paths:
- Shared logo → `/`; shared Handoff `Reserve a seat` → `/reserve` are documented. Live click-path regression remains open.

Shared components affected:
- None. Canvas writes were not made.
