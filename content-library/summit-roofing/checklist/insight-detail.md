# Insight Detail — Page Checklist

- Contract schema: 1
- Component contract: N/A — this Part creates a page-local repeated Frame and CMS List, not a reusable Component.
- Visual contract: Legacy — the established page direction remains; the 2026-10-04 row repair is a scoped CMS/rendering correction, not a new visual-direction decision.
- Evidence migration: 2026-10-04 live update. Original page-direction assertions remain preserved in project History; current row structure has targeted Canvas and bounded Desktop visual proof, while runtime Hover remains unverified.

- **Path:** `/insights/:Insights`
- **Current status:** Article Body content Pass — both CMS items now have detailed image-relevant Demo articles and the existing body binding reads on Desktop, Tablet and Phone. The Field Checklist retains its bounded Desktop visual Pass; page-wide stress, runtime Hover and full Preview evidence remain pending.
- **Content status:** Existing Insight CMS values are Demo. Title, Category, Summary, Image, Article Body and a required ten-item `Checklist Steps` CMS List are editable. The original Field Checklist rich-text field is preserved as legacy content; author, date, expertise claims and service facts remain Missing.
- **Primary CTA:** Explore Services → `/services`

## Scope Lock / Definition of Ready

Create one CMS-backed detail route for the existing `Insights` collection, then make the existing archive card route to its corresponding record. Reuse the Site Shell, Article Card and Button, existing type/color roles, straight-edge geometry, and the item image plus supplied Alt.

The 2026-10-03 [CMS-editable Detail Content request](./detail-pages/2026-10-03-cms-editable-detail-content.md) authorizes Article Body and Field Checklist content plus their Demo reference content. The 2026-10-04 user correction authorizes the Field Checklist's page display to use a required ten-item `Checklist Steps` CMS List, repeated page-local Frame rows, and a row Hover effect. It does not authorize Custom Code, forms, contact facts, author/date metadata, related-content claims, service-area claims, new visual assets, or publishing.

## Visual Direction Contract

Contract status: Blocked — existing page direction retained; the row repair has bounded visual evidence, but runtime Hover and broader Preview remain unverified.
Implementation status: Implemented — current live Field Checklist structure was updated on 2026-10-04.
Verification status: Blocked — CMS, Desktop/Tablet/Phone inheritance and one bounded Desktop visual sample pass; runtime Hover and broader Preview remain unverified.

The dated restriction against CMS fields and long-form article content is superseded only by the 2026-10-03 CMS-editable Detail Content request; the existing visual system and fact boundaries remain active.

| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |
|---|---|---|---|---|---|
| Design Read | A reading-first CMS detail page with a substantial image-relevant article body and useful field checklist. | Page structure | `../PROJECT.md#6-brand-direction`; 2026-10-03 Detail Content request | Pass — [recorded evidence](#part-result-cms-checklist-rows-2026-10-04); named semantic Sections and CMS bindings are established. | Blocked — page-wide rendered review remains outstanding. |
| Preserve | Site Shell, Big Shoulders/Inter hierarchy, blue-grey palette, zero-radius edges, direct CTA behavior, and existing CMS image/Alt. | Existing shared systems | Canvas `/insights` readback, 2026-09-19 | Blocked — original record: Shared-shell/card/button readback.; a row-specific completed result is not established here. | Blocked — original record: Consistent type, surfaces, hard edges, and image treatment.; a row-specific completed result is not established here. |
| Transform | Archive grid becomes a single-column editorial reading path with an image threshold and summary-led content record. | Detail page | `../PROJECT.md#9-narrative-and-conversion` | Blocked — original record: Independent CMS detail route and readable width chain.; a row-specific completed result is not established here. | Blocked — original record: Detail does not repeat the archive grid.; a row-specific completed result is not established here. |
| Avoid | Unsupported business claims, invented author/date/credentials, unsupported roof diagnoses, equal card grids, and rounded UI. Detailed, source-grounded Demo articles are authorized. | Content and page structure | `../PROJECT.md#7-content-facts`; 2026-10-03 Detail Content request; 2026-10-09 Article Body depth correction | Pass — [recorded evidence](#latest-part-result-article-body-expansion-2026-10-09); articles remain general and qualified, with no pictured-property or Summit capability claim. | N/A — text-only CMS value change. |
| Sibling-page delta | Unlike `/insights` two-column archive, the detail page centers one article record; unlike Project Detail, it does not mimic a metadata case-study sheet. | Page composition | `../PROJECT.md#8-sitemap-and-page-goals` | Blocked — original record: Named Section sequence differs from both siblings.; a row-specific completed result is not established here. | Blocked — original record: Single editorial reading rail with image threshold.; a row-specific completed result is not established here. |
| Section composition | Threshold → Article Record → Editable Content Note → Service Handoff. | Page sections | `../PROJECT.md#9-narrative-and-conversion` | Blocked — original record: Four semantic Section nodes.; a row-specific completed result is not established here. | Blocked — original record: Deep-navy threshold, soft-white reading field, mist limitation note, slate handoff.; a row-specific completed result is not established here. |
| Colour rhythm | Deep Navy → Soft White → Mist Grey → Slate Blue. | Section fills | `../PROJECT.md#6-brand-direction` | Blocked — original record: Token-backed fills on the four Sections.; a row-specific completed result is not established here. | Blocked — original record: Clear but restrained progress through the record.; a row-specific completed result is not established here. |
| Asset map | Bind only the current item Image and its attached Alt; no static or generated image. | CMS image binding | Canvas `Insights` collection readback, 2026-09-19 | Blocked — original record: Responsive image source uses the current CMS Image variable.; a row-specific completed result is not established here. | Blocked — original record: Screenshot may check crop only after image workflow plan.; a row-specific completed result is not established here. |
| Responsive transformation | Desktop uses a readable text rail beside/under a bounded image threshold; Tablet preserves the reading order; Phone becomes one column with 20px gutters. | Breakpoint overrides | `insights.md#image-responsive-interaction-and-accessibility` | Blocked — original record: Desktop/Tablet/Phone owner readback.; a row-specific completed result is not established here. | Blocked — original record: Desktop and Phone review if image evidence is scoped.; a row-specific completed result is not established here. |
| Completion evidence | Structural proof covers CMS route, variable bindings, detail links, semantics and breakpoint owners; visual proof remains separately bounded. | QA | `../../../framer/checklist.md#2-每个-part-的通用完成门槛` | Blocked — original record: Targeted live readback.; a row-specific completed result is not established here. | Blocked — original record: One planned image review only.; a row-specific completed result is not established here. |

## Page Narrative and Sections

1. **Article Threshold** — deep-navy opening with CMS Category, Title, Summary and bound item Image. It establishes an editable article record rather than a fabricated authority claim.
2. **Article Reading** — soft-white reading section with the CMS Summary and Article Body. Each record can now carry an image-relevant editorial story without changing the page structure.
3. **Field Checklist** — mist-grey reading section with a `Checklist Steps` CMS List. One repeated, padded Frame row renders each of the ten editable Demo items; a restrained Hover shifts the row 6px and changes its surface without changing content or route.
4. **Service Handoff** — slate-blue close with `Explore Services` → `/services` and an optional route back to `/insights` if it remains a real destination.

## Text, Styles, Semantics and Naming

- Reuse existing display/body styles, Color Styles and zero-radius geometry. No new shared Style or Component is required.
- Use exactly one CMS-bound `h1` for Title. Article Record, Editable Content Note and Service Handoff use logical `h2` headings.
- Name frames for their content responsibility; no generic Section/Frame names.
- Keep the summary in its actual CMS form rather than presenting it as a complete article body.

## Components, CMS, Links and Conversion

- **Reuse:** Site Shell, Article Card and Button. **Add:** one `Checklist Steps` List field and page-local repeated Frame row. **Modify:** the Field Checklist display source. **No-op:** shared component definitions, Navbar/Footer, image/Alt, archive routes and the legacy Field Checklist rich-text data.
- Bind Title, Category, Summary, Image and Article Body directly to the `Insights` variables. Bind each repeated row to the `Checklist Steps → Step` item field. Bind metadata title/description safely to the available CMS data.
- Each card link targets `/insights/:Insights` with the current item slug as its collection item. Its previously absent link becomes valid only after the detail route exists.
- `Explore Services` points to existing `/services`; any archive-return link points to existing `/insights`.

## Image, Responsive, Interaction and Accessibility

- Use only the CMS image and its existing attached Alt. No image review or crop adjustment is authorized until the Image Review Plan is recorded in `../PROJECT.md#14-recovery` and `image-workflow.md` is read.
- Desktop 1200: image threshold and reading rail use one max-width owner. Tablet 810 preserves legible text width and reading order. Phone 390 uses a single column with 20px outer gutters. Stress widths 320 and 1440+ remain deferred.
- The checklist row uses a native Hover effect only: a 6px horizontal shift and surface-colour change with no scale, no hover-only information, no cursor change and no route. Phone preserves the static row; keyboard order, visible focus and reduced-motion behavior remain owned by the shared shell. Runtime pointer playback remains a Preview check.

## SEO, Performance, Marketplace and Preview

- Metadata: `{{Title}} | Summit Roofing`; description: `Editable roofing guidance for a contractor template. Add verified article content before publishing.`
- No dependency, Custom Code or external embed. The template must tolerate long titles, long article/checklist content, different image ratios, item reordering and future items.
- Targeted Preview path: one existing item under `/insights/:Insights`. Publication remains excluded.

## Page Done Threshold

- The route exists as one CMS detail page with shared shell, editable CMS content, four named semantic Sections, one H1, item image/Alt binding, valid archive-to-detail routes and valid service handoff.
- Desktop, Tablet and Phone breakpoint owners are structurally verified. Visual evidence, 320/1440 stress, Preview, image licensing and publishing remain explicit work when unavailable.

## Part Result — CMS checklist rows (2026-10-04)

Scope: CMS checklist rows
Status: Structural Pass / bounded Desktop visual Pass

Pass:
- Added a required, ten-item `Checklist Steps` CMS List to both Insight records and migrated the existing ten Demo steps for each. The original Field Checklist rich-text data remains preserved but is no longer the page display source.
- Replaced the plain rich-text display with a named parent Stack and one repeated, padded/bordered page-local Frame row. The Row binds its text to `Checklist Steps → Step` and carries a non-scaling 6px Hover surface change.
- Targeted readback confirms the CMS item count, repeat binding, row styling and Hover configuration on Desktop, Tablet and Phone. A bounded Desktop screenshot confirms all ten individual rows are visible.

Blocked:
- Runtime pointer Hover playback, 320px / 1440px stress, Preview, author/date facts, commercial image licences and publication authorization remain outside this Part.

Verified widths:
- Structural: Desktop 1200, Tablet 810 and Phone 390.
- Visual: bounded Desktop composition only.

Verified paths:
- `/insights/:Insights`, with existing archive and service destinations retained.

Shared components affected:
- Reused only: Site Shell, Article Card and Button; no shared Component definition changed.

Recovery:
- Canonical current pointer: `../PROJECT.md#14-recovery`
- This Part result date: 2026-10-04

## Latest Part Result — Article Body expansion (2026-10-09)

Scope: Expand both existing Insight CMS Article Body values.

Status: Structural content Pass; page-level visual/runtime acceptance not changed.

Pass:
- `roof-inspection` now contains 830 words across 22 semantic rich-text blocks, covering inspection scope, roof-system details, interior clues, evidence, useful reporting, questions, and records.
- `replacement-signs` now contains 913 words across 23 semantic rich-text blocks, covering repair options, broader replacement considerations, recover vs. replacement, comparing proposals, uncertainty, and practical next steps.
- Official Framer Agent readback confirms the Article Body field remains bound on Desktop, Tablet, and Phone. Titles, summaries, images/Alt, ten-item checklists, the two-item collection, and detail route remain intact.
- Roofing guidance is qualified and grounded in ARMA / NRCA sources; article copy does not assert a diagnosis for either pictured property or a Summit-specific service fact.

Limits:
- No page screenshot or runtime Preview was needed for this copy-only CMS update. Existing page visual, stress, and runtime checks remain as previously recorded.

Verified widths: CMS binding readback covers Desktop, Tablet, and Phone; no new width claim.

Sources: [ARMA repair guidance](https://www.asphaltroofing.org/asphalt-shingle-roofs-are-repairable-what-you-need-to-know/); [ARMA replacement vs. recover guidance](https://www.asphaltroofing.org/reroofing-replacement-vs-recover/); [NRCA homeowner inspection and maintenance guide](https://www.nrca.net/roofingguidelines/pdf?id=177659&k=3224943).

Recovery: PROJECT §14 — Insight Article Body expansion; result date 2026-10-09.
