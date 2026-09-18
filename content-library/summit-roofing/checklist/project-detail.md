# Summit Roofing — Project Detail Page Checklist

## Status

- Page: Project Detail
- Path: `/projects/:Projects`
- Current status: In progress — live at `/projects/:Projects` with Structural and bounded Desktop visual Pass. Archive record destinations are live; 320px / 1440px stress and Preview checks remain.
- Content status: The live `Projects` Collection has four editable Demo items and only Title, Slug, Project Type, Location and Image fields. Verified project scope, challenge, solution, results, gallery images, dates, captions and licences are Missing.
- Primary CTA: `Discuss a Project` → `/#contact` until a real Contact page exists.

## Scope lock / Definition of Ready

- **Add:** when explicitly approved for build, one CMS detail page at `/projects/:Projects` using only the existing `Projects` Collection and its five current fields.
- **Reuse:** current `Site Shell`, shared Button, Big Shoulders / Inter, blue-grey Color Styles, zero-radius geometry, and the existing CMS Image / Title / Project Type / Location variables.
- **Modify:** only the new detail route and, after its route is live, the existing `/projects` card instances as necessary to provide native CMS detail destinations. Do not change the Collection schema, CMS items, Project Card definition, Home archive, Navbar or Footer.
- **No-op:** service pages, Home, Insights, Contact, forms, Custom Code, new CMS fields, galleries, related-project logic, filters, publishing and brand-name resolution.
- **Confirmed content:** every visible project field stays CMS-bound and visibly Demo until the buyer supplies verified facts. A transparent template note replaces unsupported challenge, solution and result claims.
- **Blocked / Missing:** verified project scope, challenge, solution, result, date, gallery, licence and contact facts. Do not create fields to simulate these facts in this page scope.

## Visual Direction Contract

Contract status: Ready — preparation only. The user must explicitly approve Canvas construction after reviewing this contract.

| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |
|---|---|---|---|---|---|
| Design Read | Preserve-mode CMS detail: one editable record should read as a field sheet with an image evidence plane, rather than a completed case study. | Page | `../PROJECT.md#7-content-facts` | CMS detail route and only current field bindings read back. | One bounded Desktop review after build. |
| Preserve | Keep Site Shell, Big Shoulders / Inter, blue-grey roles, square geometry, restrained labels and direct CTA language. | Shared system | `../PROJECT.md#10-system-and-platform-plan` | Layout Template and style/CTA reuse readback. | Compare with Projects archive and service siblings. |
| Transform | Turn the archive’s index logic into one focused record: a dark image threshold, an offset metadata sheet, an explicit Demo-status strip, a single image record and a compact CTA close. | Page Sections | `project-detail.md#page-narrative-and-sections` | Named Sections and CMS variable bindings. | Review hierarchy from image threshold through field sheet. |
| Avoid | Do not invent challenge, solution, result, timeline, project value, customer quote, gallery, before/after pairing, or a generic service-detail sequence. | Page | `../PROJECT.md#7-content-facts` | CMS schema and text/link readback. | Desktop check for truthful, non-case-study treatment. |
| Sibling-page delta | Projects is the archive field; Project Detail is the individual record sheet. It cannot repeat the archive’s five-band sequence or any service-page problem-to-process narrative. | Page | `../PROJECT.md#9-narrative-and-conversion` | Section order and CMS ownership comparison. | One bounded screenshot establishes individual-record focus. |
| Section composition | Use an image/deep-navy title threshold; an offset soft-white metadata sheet; a slim mist Demo-status strip; a slate-blue record-use panel with the current CMS image; and a quiet soft-white discussion handoff. | Page Sections | `project-detail.md#page-narrative-and-sections` | Five named semantic Sections with width owners. | Desktop colour, hierarchy and detail-page distinction review. |
| Colour rhythm | Deep navy/image / soft white / mist / slate blue / soft white. This reverses the archive’s opening and keeps the record-sheet role distinct. | Page Sections | `../PROJECT.md#6-brand-direction` | Fill-token readback per Section. | Desktop colour-block review. |
| Asset map | Bind the single current CMS Image as the title threshold and record image. Do not add a gallery or borrow reserve assets, because no verified same-project set exists. | CMS item | `../PROJECT.md#11-responsive-interaction-and-assets` | Existing Image variable binding and Alt readback. | One screenshot verifies the one-image evidence treatment. |
| Responsive transformation | Desktop establishes image threshold plus offset field sheet; Tablet makes the sheet stable and legible; Phone puts title, type, location, Demo note, image and CTA in one reading order with at least 20px gutters. | Breakpoint owners | `project-detail.md#image-responsive-interaction-and-accessibility` | Desktop 1200, Tablet 810, Phone 390 and 320 structural readback. | Representative Desktop review; Phone only in a separately scoped QA Part if risk requires it. |
| Completion evidence | Structural Pass requires the CMS detail route, one H1, semantic Sections, only current field bindings, image Alt, working archive-to-detail destinations and responsive ownership. Visual Pass requires bounded proof of record-sheet hierarchy and sibling delta. Preview and Marketplace Page Done remain separate. | QA | `../../../framer/checklist.md#2-每个-part-的通用完成门槛` | Clean diagnostics plus targeted live-tree evidence. | Recorded Image Review Plan and one non-repeated Canvas review. |

## Page narrative and Sections

1. **Project Record Threshold** — A deep-navy, image-led opening binds the current CMS Image, Project Type, Title and Location into one record introduction. The H1 is the CMS Title; the surrounding language states that it is editable Demo content.
2. **Record Metadata Sheet** — A soft-white offset sheet repeats the CMS Project Type and Location with a factual “current fields” explanation. It displays no dates, scope, result or location claim beyond the field itself.
3. **Demo Detail Status** — A narrow mist-grey band explains that challenge, scope, result, gallery and licensing fields are not yet part of this template’s current CMS record. It is a truthful template status, not empty editorial filler.
4. **Record Image and Editing Note** — A slate-blue field uses the same CMS Image as a single image record alongside an editorial note describing what the buyer can replace: image, title, type and location. It deliberately does not masquerade as a gallery or case-study result.
5. **Project Discussion Handoff** — A restrained soft-white close offers `Discuss a Project` to `/#contact`, marked as a Demo CTA until a dedicated Contact route and real details exist.

## Text, semantic and layer contract

- Reuse existing Text / Color Styles; add no global style for this page.
- The CMS Title is the single H1 in Project Record Threshold. Section titles use H2. Project Type and Location remain label/body text, not artificial headings.
- Each visible layer has a descriptive responsibility-based name. CMS-detail owners, metadata items, image record, status strip and CTA wrappers must never retain generic names.
- All fixed explanation and CTA-supporting copy is Demo. The CMS Title, Project Type, Location and Image preserve their current Demo / factual status and do not become verified claims through presentation.

## Components, CMS, navigation and conversion

- Create one native `WebPageNode` detail route at `/projects/:Projects`; bind only `var(--variable-fiWjBoWXS)`, `var(--variable-qtKu0ioQh)`, `var(--variable-Y8uniNhkU)` and `var(--variable-C9w9owXSC)`.
- Reuse the current `Projects` Collection exactly as read: Title, Slug, Project Type, Location and Image. Do not create scope, description, date, gallery, result, related-project or taxonomy fields.
- After route verification, set the two existing `/projects` native CMS record patterns to their matching CMS detail destination. Do not alter the Project Card component definition or Home archive; cards must remain usable without hover.
- Reuse the shared Button for the CTA to `/#contact`. Do not create a contact form, external destination or a false scheduling promise.

## Navbar, Footer and conversion

- Reuse the default Site Shell. Navbar and Footer remain the shared instances; no duplicate page-local navigation or footer is allowed.
- The breadcrumb/return affordance, if added, must lead to the existing `/projects` route and be keyboard-accessible. It must not invent a project category, location or sequence.
- The primary page CTA is `Discuss a Project` → `/#contact`; its copy may explain the Demo state but cannot imply that contact details, availability or a real project service are confirmed.

## Image, responsive, interaction and accessibility

- Follow [`image-workflow.md`](../../../framer/basic/workflows/image-workflow.md). Before visual review, write an Image Review Plan in `../PROJECT.md#14-recovery`; cap this build Part at one bounded Desktop screenshot and use structural fallback after that.
- Use only the CMS-bound Image on the detail page. Preserve its existing factual Alt; do not inspect, upload or reassign reserve images or create a gallery.
- Desktop 1200 owns the image threshold and offset metadata sheet; Tablet 810 independently stabilizes the composition; Phone 390 uses a linear reading order and at least 20px gutters. Check 320px for overflow and 1440px for capped, centred composition.
- No new motion, Overlay, Lightbox, slider or Custom Code is required. Hover never owns essential field information. Preserve keyboard order, visible focus, contrast and reduced-motion safety.

## SEO, performance, Marketplace and Preview

- Proposed metadata title: `{{Title}} | Summit Roofing`; proposed description: `Editable Demo project record with image, type and location fields for a roofing contractor template.` Both remain template copy pending brand-name resolution.
- Confirm one H1, logical heading order, CMS image Alt, correct detail route, `/projects` return destination and no dead CMS detail links. Favicon and Open Graph remain shared final-preflight responsibilities.
- Use native CMS bindings and existing image delivery only. Add no third-party dependency or Custom Code. Test long titles, absent optional text, alternate image proportions, item order and buyer editing paths during Page Done.
- Targeted Preview is deferred until explicit authorization. Publication is excluded.

## Page Done threshold

- The live `/projects/:Projects` route has metadata, the shared shell/Button, one CMS-bound H1, five named semantic Sections, the current four field bindings, truthful Demo status and Desktop/Tablet/Phone ownership read back.
- Archive record patterns lead to the matching CMS detail item; Home and the CMS schema are unchanged. The route contains no fabricated project narrative, gallery, result or unsupported fact.
- The Visual Direction Contract has Structural and Visual Pass evidence, including one bounded image review. 320px, 1440px, Preview, verified project facts, licensing, real Contact route and Marketplace publication remain explicitly classified.

## Latest Part Result

Scope: Project Detail route, archive destinations and responsive page structure
Status: In progress — Structural and bounded Desktop visual Pass

Pass:
- Live `/projects/:Projects` now has the default Site Shell, metadata, five named semantic Sections and only the current CMS Image, Title, Project Type and Location bindings.
- Targeted readback confirms Desktop 1200, Tablet 810 and Phone 390 breakpoint ownership. The negative Canvas-editor coordinates reported for both detail and the already working Projects Phone replicas are not page collapse evidence; the Phone replica’s serialized one-column hierarchy, gutters and content are intact.
- The two `/projects` CMS record wrappers now resolve to `/projects/:slug` with their current CMS Slug binding. No CMS schema, CMS item, Project Card definition, Home archive or shared Component was changed.
- One bounded Desktop review passes the image threshold, metadata sheet, Demo-status strip, single-image editing note and quiet close as an individual editable record sheet, distinct from Projects and service-detail narratives. The review budget is exhausted for this Part.

Fix Required:
- None in the approved build scope.

Blocked:
- Verified project facts, commercial image licences, richer CMS fields, real Contact route/details and publication authorization remain unavailable.

Verified widths:
- Structural: Desktop 1200, Tablet 810 and Phone 390.
- Visual: bounded Desktop composition. 320px / 1440px and Preview are not checked.

Verified paths:
- `/projects/:Projects` has the five-section structure; `/projects` lead and field CMS record wrappers resolve to matching `/projects/:slug` items.

Shared components affected:
- Reused only: Site Shell and Button. The existing Projects archive record wrappers gained native destinations; no shared Component change occurred.

Recovery:
- Canonical current pointer: `../PROJECT.md#14-recovery`
- This Part result date: 2026-09-18
