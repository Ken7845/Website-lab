# Home Page Checklist

- Page: Home
- Path: `/`
- Status: Pass
- Content status: Mixed — Approved facts and assets; Demo marketing copy
- Primary CTA: View Menu

## Scope lock / Definition of Ready

- [x] Build the complete Home page only.
- [x] Keep future-page opportunities visible through meaningful buttons/links without broken routes.
- [x] Use only HK Place content-library facts and supplied images.
- [x] Do not publish, connect a domain, add paid dependencies or use Custom Code.
- [x] Missing: complete weekly hours, formal brand story, email, social links, logo artwork and public-use rights statement.
- [x] Active request checklist confirmed.

## Narrative order and Section contracts

### 1. Navigation

- Purpose: Identify HK Place and expose Menu, Reviews and Visit actions immediately.
- Composition: Compact signboard wordmark, restrained navigation, high-contrast Menu CTA.
- Responsive: Full row on Desktop; simplified on Tablet; essential routes and CTA remain reachable on Phone.
- Done: Semantic names, valid destinations, hit areas, focus, no overflow.

### 2. Hero

- Purpose: Explain “Hong Kong-style food in Brighton” within ten seconds.
- Content: One h1, location/value support, View Menu primary CTA and Get Directions secondary CTA.
- Image role: One appetizing signature dish or storefront-led image, not a random collage.
- Responsive: Split editorial Desktop; simplified Tablet; text-first single column Phone with independent crop.
- Done: Strong hierarchy, no tiny copy, no clipped dish, no overlay contrast failure.

### 3. Trust Strip

- Purpose: Make rating, review volume and typical spend scannable.
- Content: 4.8/5, 703 reviews, typical £10–20 spend; snapshot wording where needed.
- Done: Tabular numbers where supported; labels are not headings; contrast passes.

### 4. Restaurant Introduction

- Purpose: Describe authentic food, generous portions, friendly staff and quick service without inventing a brand history.
- Image role: Exterior/storefront or service context.
- CTA: “About HK Place” route visibly reserved; until a page exists it points to the current Home introduction anchor rather than a broken page.

### 5. Menu Highlights

- Purpose: Feature beef brisket, wonton noodles and roast duck as the three verified favourites.
- Structure: Repeated Dish Highlight component or a justified equivalent; content is property-driven, not content variants.
- CTA: View Full Menu links to the approved menu website.
- Done: Dish images retain their core food information; no invented price or description.

### 6. Food Gallery

- Purpose: Show variety through an asymmetric editorial rhythm rather than an equal AI card grid.
- Image role: 4–6 selected dish images with varied but intentional ratios.
- Interaction: Optional subtle inner-image hover; Phone cannot depend on hover; Lightbox only if native implementation remains simple.

### 7. Reviews

- Purpose: Prove flavour, value, warmth and service speed.
- Content: Only supplied representative quotations; no fake attribution or extra ratings.
- Structure: Review Quote component if repeated.
- CTA: Visit / Call.

### 8. Visit Us

- Purpose: Make the physical next step effortless.
- Content: Full address, phone, menu website; complete weekly hours remain Missing.
- Image role: Storefront.
- CTA: Get Directions, Call HK Place and View Menu.

### 9. Closing CTA

- Purpose: End with one clear action after evidence.
- Composition: Lacquer-red graphic field, concise line, one primary and one secondary action.

### 10. Footer

- Purpose: Repeat essential routes and contact details, expose future-page entries and state this is a concept Demo.
- Done: No dead internal link, semantic order, readable Phone stack.

## Styles, semantics and naming

- [x] Display/H1, H2, H3, Body Large, Body, Caption, Eyebrow and Button Label styles exist as needed.
- [x] Big Shoulders is used for display roles; Fira Sans for body/UI with valid weights.
- [x] Background, Surface, Text, Accent, Border, Hover and Focus semantic colors exist.
- [x] Exactly one h1; Sections use ordered h2/h3 semantics.
- [x] All Sections, rows, grids, text, image and buttons have semantic Layer names.
- [x] Body and labels are not undersized on Desktop or Phone.

## Components / properties / CMS

- [x] Add/Reuse/Modify/No-op decision recorded before creation.
- [x] Button, Dish Highlight and Review Quote use Properties for editable copy/image/alt/link where created.
- [x] Variants represent actual state or structure, not individual content records.
- [x] Page instances own available width and content; component roots own internal padding/layout.
- [x] CMS is No-op for this small one-page scope.
- [x] Definition, representative instances and breakpoint overrides are read back after implementation.

## Links, contact and conversion

- [x] View Menu uses the approved menu destination.
- [x] Call uses `tel:+447577196494`.
- [x] Get Directions uses the approved address in a maps destination.
- [x] Home anchors are enabled before same-page links target them.
- [x] Future routes are visibly reserved without creating broken unpublished pages.
- [x] Navigation order matches Section order.

## Images and Alt

- [x] One contact sheet reviewed; 27 supplied images are locally available.
- [x] Selected source files and narrative role are recorded after implementation.
- [x] Menu and Google UI screenshots are used as facts sources, not placed as primary content without cleanup.
- [x] Crop/focal point is checked separately for Desktop, Tablet and Phone.
- [x] Informational images have concise specific Alt; decorative images have explicit empty Alt.
- [x] No source image is overwritten.

## Responsive width ownership

- [x] Page breakpoints use Stack and content-driven height.
- [x] Desktop, Tablet and Phone are authored intentionally.
- [x] Exactly one layer owns horizontal gutters; content sections share a coherent max-width.
- [x] 320 / 390 / 810 / 1200 / 1440+ stress widths are verified.
- [x] No horizontal overflow, one-character wrapping, clipped CTA or accidental full-width band.
- [x] Desktop asymmetry simplifies on narrow screens without changing semantic order.

## Motion and accessibility

- [x] Motion supports hierarchy and feedback only.
- [x] Hover has an equivalent non-hover path.
- [x] Focus is visible against every surface.
- [x] Interactive targets meet comfortable touch sizing.
- [x] Reduced Motion removes non-essential transforms/reveals.
- [x] Keyboard order follows visual and semantic order.

## SEO and metadata

- [x] Page Title and Meta Description describe HK Place, Hong Kong-style food and Brighton truthfully.
- [x] One primary h1 exists.
- [x] Favicon is evidence-backed Blocked because formal logo artwork was not supplied; no substitute brand mark was invented.
- [x] Open Graph image is selected from an approved, clean source or marked Blocked.
- [x] Concept Demo does not imply commission, endorsement or official operation.

## Performance and maintainability

- [x] No unnecessary Custom Code, large embed or third-party dependency.
- [x] Images are not uploaded far beyond container needs.
- [x] Repeated systems remain editable in Framer.
- [x] Effects and components remain reviewable in native Framer.

## Targeted Preview path

1. Navigation → Hero CTAs.
2. Menu Highlight → approved menu destination.
3. Reviews → Visit Us.
4. Address → directions; phone → call.
5. Desktop 1200/1440+, Tablet 810, Phone 390/320.

## Page Done gate

- [x] All scoped Sections are present and narratively coherent.
- [x] Content, styles, components, links, SEO, Alt and all three breakpoints are Pass or evidence-backed Blocked.
- [x] Targeted readback is clean; diagnostics are resolved.
- [x] Representative visual checks answer the planned composition questions within the image budget.
- [x] Preflight is complete.
- [x] Site remains unpublished.

## Latest Part Result

- Status: Pass
- Verified widths: Desktop 1200/1440+, Tablet 810, Phone 390/320. Representative screenshots confirm the responsive composition; structural readback covers all sections.
- Verified paths: Menu website, maps directions, telephone, `/`, and the Restaurant/Menu/Reviews/Visit Home anchors.
- Shared components: Button, Dish Highlight and Review Quote. Controls, instances and responsive ownership were read back.
- Visual evidence: Desktop Hero, Phone Hero and Phone Menu Highlight crops reviewed; images remain readable and CTAs remain visible.
- Accepted diagnostic: Eight Phone stack-proximity warnings are a Framer replica-measurement false positive. The affected replica roots return placeholder geometry while targeted screenshots show correct content-driven spacing and no overlap.
- Accessibility note: Dish Highlight uses a truthful shared image Alt fallback because Framer rejected per-instance Alt binding; all page-owned images retain specific Alt.
- Detail revision: Closing CTA Call Us now has a Warm White 1px outline across Desktop, Tablet and Phone; the `tel:` path is unchanged.
- Tablet Menu evidence: four Dish Highlight instances form a complete flexible 2×2 grid; Wonton Lo Mein uses a distinct supplied noodle image.
- Tablet Review evidence: all three Review Quote instances are 212px high with 16px row spacing; the targeted screenshot shows complete quote and source text.
- Width ownership evidence: page-wide targeted readback returns zero `maxWidth` attributes; outer and near-outer layout Stacks remain fluid.
- Visual evidence for this revision: one bounded Closing CTA screenshot, one Tablet Menu Highlights screenshot and one Tablet Reviews screenshot, each reviewed once within the image budget.
- Canonical Recovery reference: `../PROJECT.md#14-recovery`
