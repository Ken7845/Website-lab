# Insight Detail — Page Checklist

- Contract schema: 1
- Component contract: N/A — this recorded Part contains no component contract; lifecycle migration makes no construction change.
- Visual contract: Required
- Evidence migration: 2026-10-03; repository-only. Original contract assertions are preserved in project History; no fresh Canvas or runtime proof was produced.

- **Path:** `/insights/:Insights`
- **Current status:** In progress — Structural Pass at Desktop, Tablet and Phone; visual, stress and Preview evidence pending
- **Content status:** Existing Insight CMS values are Demo. Only Title, Category, Summary and Image are available; article body, author, date, expertise claims and service facts are Missing.
- **Primary CTA:** Explore Services → `/services`

## Scope Lock / Definition of Ready

Create one CMS-backed detail route for the existing `Insights` collection, then make the existing archive card route to its corresponding record. Reuse the Site Shell, Article Card and Button, existing type/color roles, straight-edge geometry, and the item image plus supplied Alt.

Do not add or alter CMS fields, CMS items, Custom Code, forms, contact facts, author/date metadata, articles, related-content claims, service-area claims, new visual assets, or publishing. The user’s 2026-09-19 `start` confirms this contract and its bounded build scope.

## Visual Direction Contract

Contract status: Blocked — recorded implementation exists; the full row-specific evidence matrix is not established by this repository-only repair.
Implementation status: Implemented — historical completion record; current live state not reverified.
Verification status: Blocked — retain bounded historical results; outstanding evidence requires the live Framer gate.

| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |
|---|---|---|---|---|---|
| Design Read | A concise, reading-first CMS record sheet for a template article whose body field is currently Missing. | Page structure | `../PROJECT.md#6-brand-direction` | Blocked — original record: Named semantic Sections and CMS bindings.; a row-specific completed result is not established here. | Blocked — original record: One bounded Desktop composition review.; a row-specific completed result is not established here. |
| Preserve | Site Shell, Big Shoulders/Inter hierarchy, blue-grey palette, zero-radius edges, direct CTA behavior, and existing CMS image/Alt. | Existing shared systems | Canvas `/insights` readback, 2026-09-19 | Blocked — original record: Shared-shell/card/button readback.; a row-specific completed result is not established here. | Blocked — original record: Consistent type, surfaces, hard edges, and image treatment.; a row-specific completed result is not established here. |
| Transform | Archive grid becomes a single-column editorial reading path with an image threshold and summary-led content record. | Detail page | `../PROJECT.md#9-narrative-and-conversion` | Blocked — original record: Independent CMS detail route and readable width chain.; a row-specific completed result is not established here. | Blocked — original record: Detail does not repeat the archive grid.; a row-specific completed result is not established here. |
| Avoid | Fabricated long-form body, author/date/chapter metadata, equal card grids, rounded UI, generic testimonials, and unverified claims. | Content and page structure | `../PROJECT.md#7-content-facts` | Blocked — original record: No new CMS data/fields; explicit Missing note.; a row-specific completed result is not established here. | Blocked — original record: Restrained record-sheet composition.; a row-specific completed result is not established here. |
| Sibling-page delta | Unlike `/insights` two-column archive, the detail page centers one article record; unlike Project Detail, it does not mimic a metadata case-study sheet. | Page composition | `../PROJECT.md#8-sitemap-and-page-goals` | Blocked — original record: Named Section sequence differs from both siblings.; a row-specific completed result is not established here. | Blocked — original record: Single editorial reading rail with image threshold.; a row-specific completed result is not established here. |
| Section composition | Threshold → Article Record → Editable Content Note → Service Handoff. | Page sections | `../PROJECT.md#9-narrative-and-conversion` | Blocked — original record: Four semantic Section nodes.; a row-specific completed result is not established here. | Blocked — original record: Deep-navy threshold, soft-white reading field, mist limitation note, slate handoff.; a row-specific completed result is not established here. |
| Colour rhythm | Deep Navy → Soft White → Mist Grey → Slate Blue. | Section fills | `../PROJECT.md#6-brand-direction` | Blocked — original record: Token-backed fills on the four Sections.; a row-specific completed result is not established here. | Blocked — original record: Clear but restrained progress through the record.; a row-specific completed result is not established here. |
| Asset map | Bind only the current item Image and its attached Alt; no static or generated image. | CMS image binding | Canvas `Insights` collection readback, 2026-09-19 | Blocked — original record: Responsive image source uses the current CMS Image variable.; a row-specific completed result is not established here. | Blocked — original record: Screenshot may check crop only after image workflow plan.; a row-specific completed result is not established here. |
| Responsive transformation | Desktop uses a readable text rail beside/under a bounded image threshold; Tablet preserves the reading order; Phone becomes one column with 20px gutters. | Breakpoint overrides | `insights.md#image-responsive-interaction-and-accessibility` | Blocked — original record: Desktop/Tablet/Phone owner readback.; a row-specific completed result is not established here. | Blocked — original record: Desktop and Phone review if image evidence is scoped.; a row-specific completed result is not established here. |
| Completion evidence | Structural proof covers CMS route, variable bindings, detail links, semantics and breakpoint owners; visual proof remains separately bounded. | QA | `../../../framer/checklist.md#2-每个-part-的通用完成门槛` | Blocked — original record: Targeted live readback.; a row-specific completed result is not established here. | Blocked — original record: One planned image review only.; a row-specific completed result is not established here. |

## Page Narrative and Sections

1. **Article Threshold** — deep-navy opening with CMS Category, Title, Summary and bound item Image. It establishes an editable article record rather than a fabricated authority claim.
2. **Article Record** — soft-white reading section with the Summary and a clear content-availability statement. The Summary is the only current article text field and must remain visibly truthful.
3. **Editable Content Note** — mist-grey plain-language note: add verified article copy in the CMS before publishing. This makes the Missing long-form body an editing requirement, not false content.
4. **Service Handoff** — slate-blue close with `Explore Services` → `/services` and an optional route back to `/insights` if it remains a real destination.

## Text, Styles, Semantics and Naming

- Reuse existing display/body styles, Color Styles and zero-radius geometry. No new shared Style or Component is required.
- Use exactly one CMS-bound `h1` for Title. Article Record, Editable Content Note and Service Handoff use logical `h2` headings.
- Name frames for their content responsibility; no generic Section/Frame names.
- Keep the summary in its actual CMS form rather than presenting it as a complete article body.

## Components, CMS, Links and Conversion

- **Reuse:** Site Shell, Article Card and Button. **Add:** one WebPage CMS detail route and page-local Frames/RichText nodes. **Modify:** the archive's repeating page-local Article Card wrapper to point to the matching new detail record. **No-op:** CMS schema/items, shared component definitions and Navbar/Footer.
- Bind Title, Category, Summary and Image directly to the `Insights` variables. Bind metadata title/description safely to the available CMS data.
- Each card link targets `/insights/:Insights` with the current item slug as its collection item. Its previously absent link becomes valid only after the detail route exists.
- `Explore Services` points to existing `/services`; any archive-return link points to existing `/insights`.

## Image, Responsive, Interaction and Accessibility

- Use only the CMS image and its existing attached Alt. No image review or crop adjustment is authorized until the Image Review Plan is recorded in `../PROJECT.md#14-recovery` and `image-workflow.md` is read.
- Desktop 1200: image threshold and reading rail use one max-width owner. Tablet 810 preserves legible text width and reading order. Phone 390 uses a single column with 20px outer gutters. Stress widths 320 and 1440+ remain deferred.
- No motion, hover-only information, overlay, Lightbox, cursor effect or new interaction. Preserve keyboard order, visible focus and reduced-motion behavior from the shared shell.

## SEO, Performance, Marketplace and Preview

- Metadata: `{{Title}} | Summit Roofing`; description: `Editable roofing guidance for a contractor template. Add verified article content before publishing.`
- No dependency, Custom Code, external embed or CMS schema change. The template must tolerate long titles/summaries, different image ratios, missing article body, item reordering and future items.
- Targeted Preview path: one existing item under `/insights/:Insights`. Publication remains excluded.

## Page Done Threshold

- The route exists as one CMS detail page with shared shell, truthful CMS-only content, four named semantic Sections, one H1, item image/Alt binding, valid archive-to-detail routes and valid service handoff.
- Desktop, Tablet and Phone breakpoint owners are structurally verified. Visual evidence, 320/1440 stress, Preview, article body content, image licensing and publishing remain explicit work when unavailable.

## Latest Part Result

Scope: Insight Detail CMS route, archive linking and structural QA
Status: Structural Pass / Visual Blocked

Pass:
- `/insights/:Insights` is associated with the existing Insights CMS collection, uses Site Shell metadata and has independent Desktop 1200, Tablet 810 and Phone 390 breakpoint owners.
- Four named semantic Sections follow the contracted Deep Navy → Soft White → Mist Grey → Slate Blue sequence. Category, Title, Summary and Image are CMS-bound; no collection, item, field, Component definition, Custom Code or dependency changed.
- The existing Insights collection-list wrapper now links each record to `/insights/:slug` with the active CMS slug. Article Card remains unmodified; the service CTA reaches the existing `/services` route.

Fix Required:
- None in the authorized structural scope.

Blocked:
- Long-form article body, factual editorial content, author/date data, image licensing, visual review, 320/1440 stress widths, Preview and publishing remain unavailable or outside this Part.

Verified widths:
- Structural: Desktop 1200, Tablet 810 and Phone 390. Deferred: 320 and 1440+ stress widths.

Verified paths:
- `/insights`, `/insights/:slug` and `/services`.

Shared components affected:
- Reused only: Site Shell, Article Card and Button. The archive's page-local repeat wrapper gained the valid dynamic destination; no shared component changed.

Recovery:
- Canonical current pointer: `../PROJECT.md#14-recovery`
- This Part result date: 2026-09-19
