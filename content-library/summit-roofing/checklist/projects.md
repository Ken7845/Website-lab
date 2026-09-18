# Summit Roofing — Projects Page Checklist

## Status

- Page: Projects
- Path: `/projects`
- Current status: In progress — live at `/projects` with structural and bounded Desktop visual Pass on 2026-09-18; 320px / 1440px stress and Preview checks remain.
- Content status: The existing `Projects` CMS Collection has four editable Demo items. Project titles, locations, categories, scopes, captions, results, dates, before/after relationships and image licences remain Demo or Missing.
- Primary CTA: `Discuss a Project` → `/#contact` until a real Contact page exists.

## Scope lock / Definition of Ready

- **Add:** when explicitly approved for build, one CMS-backed Projects archive page using the existing `Projects` Collection and its native repeated-item pattern.
- **Reuse:** current `Site Shell`, shared Button, Big Shoulders / Inter, blue-grey Color Styles, zero-radius geometry, existing native `Project Card · CMS` repeated template, and the four current CMS fields: Title, Project Type, Location and Image.
- **Modify:** only the new `/projects` page when approved. The existing Home Projects CMS list remains unchanged. Do not modify Project Card, existing CMS items, collection variables, Navbar, Footer or the later Project Detail route in this page scope.
- **No-op:** service pages, Home, Insights, Contact, forms, Custom Code, new CMS collections, CMS taxonomy/filter fields, project-detail template, publishing and brand-name resolution.
- **Confirmed content:** an image-led, editable archive helps Marketplace buyers understand how the template can display work without presenting its four Demo CMS records as verified projects.
- **Blocked / Missing:** commercial image licences; verified project facts, categories, locations, scopes, captions, outcomes and dates; a Project Detail page; Contact route and contact facts. The existing `Project Type` is plain text, so category filters are out of scope until a suitable CMS taxonomy is explicitly approved.

## Visual Direction Contract

Contract status: Ready — preparation only. The user must explicitly approve Canvas construction after reviewing this contract.

| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |
|---|---|---|---|---|---|
| Design Read | Preserve-mode Marketplace archive: an editable work index should feel like an evidence field, not a service-detail journey or a generic portfolio card wall. | Page | `../PROJECT.md#8-sitemap-and-page-goals` | One H1, named Sections, current `Projects` Collection and native repeated-item readback. | One bounded Desktop archive-composition review after build. |
| Preserve | Keep the shared shell, Big Shoulders / Inter, blue-grey token roles, square geometry, dark Project Card treatment and concise CTA language. | Shared system | `../PROJECT.md#10-system-and-platform-plan` | Layout Template, styles and native Project Card / CMS binding readback. | Comparison with Home Projects and active service pages. |
| Transform | Turn the archive into a measured work ledger: restrained index opening, an explanatory record band, one lead CMS record and an intentionally uneven field of remaining records. | Page Sections | `projects.md#page-narrative-and-sections` | Named Section topology and two native Collection List owners. | Review of field rhythm, lead-to-list hierarchy and card density. |
| Avoid | Do not repeat the Services navigator / ledger, any service-page opening sequence, equal three-card marketing grids, fabricated project results, testimonial treatment, filter controls unsupported by CMS fields, or finished detail links before their page exists. | Page | `../PROJECT.md#9-narrative-and-conversion` | Section, Collection List, link and field comparison. | Desktop composition check against these exclusions. |
| Sibling-page delta | Projects is an archive field: evidence comes from editable CMS records and their relationship, rather than a problem-to-CTA service narrative. | Page | `../PROJECT.md#9-narrative-and-conversion` | CMS ownership, section order and card-layout comparison. | One bounded screenshot establishes a distinct archive memory point. |
| Section composition | Use a soft-white index opening; a slim deep-navy Demo-record band; a lead CMS record with a large image plane and editorial rail; an offset, native CMS record field; and a quiet slate-blue project-discussion handoff. | Page Sections | `projects.md#page-narrative-and-sections` | Five named semantic Sections with repeated-item and width owners. | Planned desktop colour and hierarchy review. |
| Colour rhythm | Soft white / deep navy / soft white / mist / slate blue. The archive rhythm remains calmer and more data-led than the existing service pages. | Page Sections | `../PROJECT.md#6-brand-direction` | Fill-token readback per Section. | Desktop colour-block review. |
| Asset map | Use only images already attached to the four current CMS items for the initial archive. The master-plan flat/commercial and exterior files remain future data-preparation candidates; do not silently replace item imagery or imply they are related projects. | CMS items | `../PROJECT.md#11-responsive-interaction-and-assets` | Collection item image URL and factual Alt readback. | One screenshot verifies that imagery remains record-specific. |
| Responsive transformation | Desktop establishes the lead record and offset archive field; Tablet stabilizes the field into an intentional two-column or stacked sequence; Phone presents one record at a time with image, type, title and Demo location in reading order. | Breakpoint owners | `projects.md#image-responsive-and-accessibility-contract` | Desktop 1200, Tablet 810, Phone 390 and 320 structural readback. | Representative Desktop review, then Phone only if visual risk requires it. |
| Completion evidence | Structural Pass requires live CMS, one H1, semantic Sections, image Alt, no dead detail links and responsive ownership. Visual Pass requires bounded proof of the archive-field hierarchy, sibling delta, colour rhythm and record density. Preview and Marketplace Page Done remain separate. | QA | `../../../framer/checklist.md#2-每个-part-的通用完成门槛` | Clean diagnostics plus targeted live-tree evidence. | Recorded Image Review Plan and non-repeated Canvas review. |

## Page narrative and Sections

1. **Projects Index Opening** — A soft-white index opening introduces the archive with one H1, a concise Demo explanation and the only page-level CTA, `Discuss a Project`. It frames editable project records rather than making capability or outcome claims.
2. **Demo Record Band** — A slim deep-navy band states that the archive’s titles, locations, types and images are editable Demo content until the buyer replaces them. It contains no statistics, testimonials, filters or project claims.
3. **Lead Project Record** — A native `Projects` Collection List limited to one item gives the first current record a large image plane and editorial text rail. It uses the live collection’s Image, Project Type, Title and Location fields, without asserting that the first item is a verified featured project.
4. **Projects Field** — A second native `Projects` Collection List, offset after the lead record, displays remaining records using the current native repeated-item / Project Card pattern in an intentionally uneven Desktop field. Cards are non-interactive until the Project Detail route exists; no unbuilt detail destination is presented as finished.
5. **Project Discussion Handoff** — A restrained slate-blue close offers `Discuss a Project` to `/#contact`, explicitly as an editable template CTA until a real Contact route and details exist.

## Text, semantic and layer contract

- Reuse existing Text / Color Styles; add no global style for this page.
- One H1 appears in the index opening. Section titles use H2; record type and location stay as labels/body text, not artificial headings.
- Each new visible layer has a descriptive responsibility-based name. Collection list owners, repeated items, media, rails, empty state and CTA wrappers must never retain generic names.
- All archive explanation and CTA-supporting copy is Demo. Titles, project types, locations and image Alt are sourced from the existing CMS and retain their current Demo / factual status.

## Components, CMS, navigation and conversion

- Reuse the default `Site Shell`, shared Button, existing `Projects` Collection and the current native `Project Card · CMS` repeated-item pattern. Do not duplicate a Project Card or create a new collection.
- The live `Projects` Collection currently has four items and Title, Slug, Project Type, Location and Image fields. Retain that schema in the archive build; do not add filters, taxonomy, rich text, dates or case-study facts in this page scope.
- Use two Collection Lists bound to `Projects`: lead record `limit=1`; record field starts after that lead item. Implement an explicit empty state for the archive, although the current collection has four items.
- Project Detail does not yet exist. Do not give cards a finished `/projects/:Projects` destination until that route and its CMS detail contract are built and verified.
- The page CTA remains `/#contact`. It may invite a project discussion but cannot imply live contact information, scheduling or a delivered project service.

## Image, responsive, interaction and accessibility contract

- Follow [`image-workflow.md`](../../../framer/basic/workflows/image-workflow.md). Before any visual review, record an Image Review Plan in `../PROJECT.md#14-recovery`; cap the initial build Part at one bounded Desktop screenshot and use structural fallback after that.
- Do not open or upload master-plan reserve images during archive construction. Reuse only the Images already bound to the four current CMS items, retain their factual existing Alt, and verify field binding after construction.
- Desktop 1200 owns the index hierarchy, lead record and uneven record field; Tablet 810 independently stabilizes the archive; Phone 390 uses a one-record reading order with at least 20px gutters. Check 320px for overflow and 1440px for capped, centred composition.
- Preserve keyboard order, visible focus and text contrast. The existing Project Card Hover state is supplementary only: its type, title and location remain visible and legible without hover, and Phone uses its stable default treatment.
- No new motion, Overlay, Lightbox, slider or Custom Code is required.

## SEO, performance, Marketplace and Preview

- Proposed metadata title: `Projects | Summit Roofing`; proposed description: `Browse editable project-record examples in this adaptable roofing contractor template.` Both remain template copy pending brand-name resolution.
- Confirm one H1, logical heading order, CMS image Alt, correct archive path and no dead project-detail links. Favicon and Open Graph remain shared final-preflight responsibilities.
- Use the existing CMS image fields and native Collection Lists only. Add no third-party dependency or Custom Code. Keep long titles, alternate image proportions, missing optional fields, zero-item state, item ordering and buyer editing paths testable during Page Done.
- Targeted Preview is deferred until explicit authorization. Publication is excluded.

## Page Done threshold

- The live `/projects` route has metadata, named semantic Sections, the shared shell/Button, one H1, two native Collection Lists, CMS image Alt, a deliberate empty state and Desktop/Tablet/Phone ownership read back.
- The archive does not claim verified project facts or contain dead detail links. The Visual Direction Contract has Structural and Visual Pass evidence, including its bounded image review.
- 320px, 1440px, Preview, Project Detail, real Contact route, licence verification and Marketplace publication remain explicitly classified rather than silently marked complete.

## Latest Part Result

Scope: Projects page build
Status: In progress — Structural and bounded Desktop visual Pass

Pass:
- Live `/projects` has metadata, one H1 and five named semantic Sections: Projects Index Opening, Demo Record Band, Lead Project Record, Projects Field and Project Discussion Handoff.
- Two native Collection Lists reuse the existing four-item Demo `Projects` Collection: lead record `limit=1`; remaining record field `limit=3`, `offset=1`. Image, project type, title and location remain CMS-bound, and the existing Project Card pattern is reused without a shared Component or CMS schema change.
- Targeted readback verifies the shared Site Shell, Button CTA destinations to `/#contact`, no finished Project Detail links, and independently owned Desktop 1200 / Tablet 810 / Phone 390 structures.
- One bounded Desktop review passes the archive hierarchy, colour rhythm, record density and sibling-page delta. The review budget is exhausted for this Part.

Fix Required:
- None in the approved build scope.

Blocked:
- 320px / 1440px stress checks and Preview remain deferred. Verified project facts, commercial image licences, Project Detail, a real Contact route/details and publication authorization remain unavailable.

Verified widths:
- Structural: Desktop 1200, Tablet 810 and Phone 390.
- Visual: bounded Desktop composition.

Verified paths:
- `/projects`; existing Home Projects CMS list remains unchanged.

Shared components affected:
- Reused only: Site Shell, Button and Project Card. No shared Component change occurred.

Recovery:
- Canonical current pointer: `../PROJECT.md#14-recovery`
- This Part result date: 2026-09-18
