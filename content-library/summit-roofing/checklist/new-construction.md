# Summit Roofing — New Construction Page Checklist

## Status

- Page: New Construction
- Path: `/services/new-construction`
- Current status: In progress — the route, seven Sections and Desktop / Tablet / Phone owners are live; Structural and bounded Desktop Visual Pass are complete, while stress and Preview checks remain outstanding.
- Content status: Demo explanatory copy. Contractor credentials, material systems, builder partners, coverage, timelines, pricing, contact facts and service area remain Missing.
- Primary CTA: `Discuss a Project` → `/#contact` until a real Contact page exists.

## Scope lock / Definition of Ready

- **Add:** when explicitly approved for build, one authored service-detail page using the current `Site Shell`, shared Button and established styles.
- **Reuse:** Big Shoulders display type, Inter body type, blue-grey Color Styles, zero-radius geometry, shared Navbar/Footer and honest Demo / Missing content treatment.
- **Modify:** only after the route exists, the existing Services `New Construction` row and its responsive replicas may be linked to `/services/new-construction`.
- **No-op:** Home, Services structure, Repair & Maintenance, Roof Replacement, Storm Damage Repair, shared Components, CMS, Contact, forms, Custom Code, publishing and brand-name resolution.
- **Confirmed content:** the page helps a visitor understand coordination and installation for a new build. Its staged assets are `exterior/house-frame.webp`, `roofer on roof/frame-ladder.webp`, and `roofer on roof/roof-framing.webp`.
- **Blocked / Missing:** commercial image licence, real contact destination, verified contractor credentials, actual builder coordination model, materials, warranties, project facts, cost and timeframes.

## Visual Direction Contract

Contract status: Ready — approved by the user on 2026-09-17 and implemented as the governing Canvas contract.

| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |
|---|---|---|---|---|---|
| Design Read | Preserve-mode service detail: the visual story is structure taking shape, with planning and build coordination expressed as a sequence of framing conditions rather than repair diagnosis or finished-roof decision-making. | Page | `../PROJECT.md#8-sitemap-and-page-goals` | Named Section tree, one H1 and shared-shell readback. | One bounded Desktop page-composition review after build. |
| Preserve | Keep Big Shoulders / Inter, blue-grey token roles, square geometry, restrained industrial/editorial language, shared shell, shared Button and direct contact fallback. | Shared system | `../PROJECT.md#6-brand-direction` | Style, Layout Template and Button-instance readback. | Comparison with the active Services, Repair and Roof Replacement language. |
| Transform | Give New Construction a build-sequence topology: image-led structural opening, a nested coordination brief, a tall ladder/framing moment, a long linear scope rail and a measured handoff. | Page Sections | `new-construction.md#page-narrative-and-sections` | Section topology and breakpoint ownership. | Review of hierarchy, section cadence and media roles. |
| Avoid | Do not repeat the Services navigator/ledger, Repair’s assessment-first split / dark work-scope / vertical sequence, Roof Replacement’s roof-plane copy rail / decision band / slate handoff, equal card grids, fabricated credentials or decorative blueprint effects. | Page | `../PROJECT.md#9-page-visual-identity` | Sibling Section / Fill / asset comparison. | Desktop composition check against the stated exclusions. |
| Sibling-page delta | New Construction is an emerging-structure journey: a framed opening, coordination brief, installation-field moment and continuous scope rail. It is neither condition-led nor completed-exterior-led. | Page | `../PROJECT.md#9-page-visual-identity` | Named Sections, fills and layout-family comparison. | One bounded screenshot demonstrates a separate visual memory point. |
| Section composition | Use a full-width framing opening with a dark title band; a mist coordination brief; a slate-blue, tall ladder/framing section; a soft-white continuous scope rail; a narrow roof-framing media band; Demo FAQ; and a deep-navy project-discussion close. | Page Sections | `new-construction.md#page-narrative-and-sections` | Six or seven named semantic Sections with explicit nested owners. | Planned page rhythm review. |
| Colour rhythm | Begin with a strong image / deep-navy title threshold, move through mist and slate-blue working fields, reset in soft white for the scope rail, and finish in deep navy. Do not reuse Roof Replacement’s soft-white/mist/soft-white/slate/deep-navy order. | Page Sections | `../PROJECT.md#6-brand-direction` | Fill-token readback per Section. | Desktop colour-block review. |
| Asset map | `house-frame.webp` supplies the opening framing context, `frame-ladder.webp` is the tall coordination / installation field, and `roof-framing.webp` is the narrow build-detail band. All use factual Alt and purpose-specific crops. | Page image owners | `../PROJECT.md#11-responsive-interaction-and-assets` | Fill URL, Alt and breakpoint crop readback. | One screenshot verifies the asset roles in their final composition. |
| Responsive transformation | Desktop uses stacked full-width thresholds and a continuous horizontal scope rail; Tablet stabilizes the working field; Phone keeps the project-discussion CTA and coordination copy before contextual media, and turns the scope rail into ordered rows. | Breakpoint owners | `new-construction.md#responsive-and-acceptance-contract` | Desktop 1200, Tablet 810, Phone 390 and 320 structural readback. | Representative Desktop review, then Phone only if visual risk requires it. |
| Completion evidence | Structural Pass requires live semantics, labels, links, alts and responsive ownership. Visual Pass requires bounded proof of the emerging-structure narrative, sibling delta, colour rhythm and asset roles. Preview and Marketplace Page Done remain separate. | QA | `../../../framer/checklist.md#2-每个-part-的通用完成门槛` | Clean diagnostics plus targeted live-tree evidence. | Recorded Image Review Plan and non-repeated Canvas review. |

## Page narrative and Sections

1. **Framing Opening** — A wide `house-frame.webp` image threshold with a contained deep-navy title band, one H1, a concise Demo fit statement and `Discuss a Project` CTA. It must express a new-build context without claiming a particular project or capability.
2. **Coordinate the whole build** — A mist-grey coordination brief that identifies editable areas of discussion: roof design context, sequencing and information a project team may need. No builder relationship, timeline or scope promise.
3. **Work alongside the structure** — A tall slate-blue installation field using `frame-ladder.webp`, paired with concise Demo copy about the questions that can be aligned before work starts.
4. **A continuous scope rail** — A soft-white, ruled Desktop progression for three editable project stages. It is a linear document-like rail, not a three-card or Repair-style vertical-step pattern.
5. **Framing detail band** — A narrow, full-width `roof-framing.webp` media band that punctuates the scope sequence; it does not represent a verified completed project.
6. **Questions for a new build** — A static Demo FAQ that avoids credentials, capacity, warranty, code, price, schedule and permit claims.
7. **Project discussion handoff** — A deep-navy close with one clear `Discuss a Project` CTA to `/#contact` until a real destination exists.

## Text, semantic and layer contract

- Reuse existing Text / Color Styles; add no global style for this one page.
- One H1 appears in the opening title band. Major Section titles use H2; scope stages and FAQ prompts use H3 or regular text according to their role.
- All new visible layers receive descriptive, responsibility-based names; no default Frame, Stack, Text or Image names.
- All explanatory copy is Demo. Do not add unverified credentials, code/permit, timeline, price, materials, warranty, installation, safety, partnership or performance claims.

## Components, navigation and conversion

- Reuse the default `Site Shell` and existing shared Button. Do not copy Navbar/Footer or introduce a new Component, Variant, CMS collection, Overlay, form or Custom Code.
- Use ordinary authored Frames for the static scope rail and FAQ rows; no accordion is required.
- After creation, update only the existing Services `New Construction` row and its Desktop / Tablet / Phone replicas to `/services/new-construction`, then read back all destinations.
- The CTA remains `/#contact`; it may invite discussion but cannot imply live contact information exists.

## Image, responsive, interaction and accessibility contract

- Follow [`image-workflow.md`](../../../framer/basic/workflows/image-workflow.md). Before any visual review, record an Image Review Plan in `../PROJECT.md#14-recovery`; cap the initial build part at one bounded Desktop screenshot and use structural fallback after that.
- Verify exact local-file residency and dimensions before upload. Upload only the three staged WebP files with factual Alt text: “Partially framed house exterior”, “Roofer climbing a ladder beside a roof frame”, and “Wood roof framing under construction”.
- Desktop 1200 owns the title band and continuous scope rail; Tablet 810 independently recomposes the tall field; Phone 390 uses a clear one-column reading order with at least 20px gutters, CTA before supporting media, and ordered scope rows. Check 320px for overflow and 1440px for capped/centred composition.
- No motion, hover-only information, Overlay or Lightbox is required. Preserve keyboard order, visible focus, contrast and reduced-motion safety through the shared system.

## SEO, performance, Marketplace and Preview

- Proposed metadata title: `New Construction | Summit Roofing`; proposed description: `Explore a clear, coordination-first approach to new construction roofing in this adaptable contractor template.` Both remain template copy pending brand-name resolution.
- Confirm one H1, logical H2/H3 order, factual Alt text and correct route. Favicon and Open Graph remain shared/final-preflight responsibilities.
- Use only supplied WebP assets, no third-party dependency and no Custom Code. Keep all Demo content easy for Marketplace buyers to replace; test long copy and alternate image proportions during Page Done.
- Targeted Preview is deferred until explicit authorization. Publication is excluded.

## Page Done threshold

- The live route has its metadata, named semantic Sections, shared shell/Button, one H1, factual image Alt, Desktop/Tablet/Phone ownership and Services link replicas read back.
- The Visual Direction Contract has Structural and Visual Pass evidence, including its bounded image review.
- 320px, 1440px, Preview, real Contact route, licence verification and Marketplace publication remain explicitly classified rather than silently marked complete.

## Latest Part Result

Scope: Page build
Status: In progress

Pass:
- The approved route, goal, CTA, three allocated assets, exclusions and Ready Visual Direction Contract are recorded.
- Structural status: Pass — `/services/new-construction` uses the existing `Site Shell`, metadata, seven named semantic Sections, one H1, shared Button instances, all three allocated image fills with factual Alt text, and Desktop 1200 / Tablet 810 / Phone 390 breakpoint owners.
- Visual status: Pass for the bounded Desktop review — the framed opening, tall ladder field, continuous scope rail and narrow roof-framing detail band establish the approved emerging-structure narrative without repeating the previous service-page sequences.
- The Services `New Construction` row and its Tablet / Phone replicas all route to `/services/new-construction`.

Fix Required:
- None in the bounded build scope.

Blocked:
- Real contact details, contact route, credentials, project facts, materials/warranty facts, image licences and publication authorization remain unavailable. Preview, 320px and 1440px checks are deferred.

Verified widths:
- Structural ownership: Desktop 1200, Tablet 810 and Phone 390.

Verified paths:
- `/services/new-construction`; `/services` (all three New Construction row replicas).

Shared components affected:
- Reused only: `Site Shell` and Button. No shared Component was changed.

Recovery:
- Canonical current pointer: `../PROJECT.md#14-recovery`
- This Part result date: 2026-09-17
