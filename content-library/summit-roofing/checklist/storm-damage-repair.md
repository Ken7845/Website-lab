# Summit Roofing — Storm Damage Repair Page Checklist

## Status

- Page: Storm Damage Repair
- Path: `/services/storm-damage-repair`
- Current status: In progress — live route and page content were created on 2026-09-17. Structural readback and the separately scoped bounded Desktop visual QA pass.
- Content status: Demo explanatory copy. Emergency availability, response times, insurance support, restoration scope, credentials, pricing, contact facts and service area remain Missing.
- Primary CTA: `Request an Inspection` → `/#contact` until a real Contact page exists.

## Scope lock / Definition of Ready

- **Add:** when explicitly approved for build, one authored service-detail page using the current `Site Shell`, shared Button and established styles.
- **Reuse:** Big Shoulders display type, Inter body type, approved blue-grey Color Styles, zero-radius geometry, shared Navbar/Footer and honest Demo / Missing content treatment.
- **Modify:** only after the route exists, the existing Services `Storm Damage Repair` row and responsive replicas may be linked to `/services/storm-damage-repair`.
- **No-op:** Home, Services structure, Repair & Maintenance, Roof Replacement, New Construction, shared Components, CMS, Contact, forms, Custom Code, publishing and brand-name resolution.
- **Confirmed content:** the page helps a visitor understand a calm, inspection-led response path after roof damage. Its staged assets are `storm damage roof/fire-damage.webp`, one of the duplicate-role `storm-repair.webp` / `roof-damage.webp`, and `storm-roof.webp`. The documented `storm-repair.webp` file is Missing at the source path on 2026-09-17, so this contract uses the approved `roof-damage.webp` alternate and does not substitute another image.
- **Blocked / Missing:** commercial image licence, real contact destination, availability, response-time, insurance, emergency, scope, credential, price and restoration facts.

## Visual Direction Contract

Contract status: Ready — preparation only. The user must explicitly approve Canvas construction after reviewing this contract.

| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |
|---|---|---|---|---|---|
| Design Read | Preserve-mode service detail: damage context should feel calm and legible, moving from visual condition evidence to a clear inspection conversation without implying emergency availability or a guaranteed outcome. | Page | `../PROJECT.md#8-sitemap-and-page-goals` | Named Section tree, one H1 and shared-shell readback. | One bounded Desktop page-composition review after build. |
| Preserve | Keep Big Shoulders / Inter, blue-grey tokens, square geometry, shared shell/Button, direct CTA and factual Alt treatment. | Shared system | `../PROJECT.md#6-brand-direction` | Style, Layout Template and Button-instance readback. | Comparison against all active service pages. |
| Transform | Use a persistent deep-navy response rail alongside damage imagery, then progress through calm review fields, documentation guidance and a quiet inspection handoff. | Page Sections | `storm-damage-repair.md#page-narrative-and-sections` | Section topology and breakpoint ownership. | Review of hierarchy, evidence cadence and colour rhythm. |
| Avoid | Do not repeat Services’ navigator/ledger, Repair’s diagnosis split / dark scope / vertical sequence, Roof Replacement’s roof-plane decision journey, New Construction’s framing threshold / scope rail, alarmist visual language, false urgency or decorative damage effects. | Page | `../PROJECT.md#9-page-visual-identity` | Sibling Section / Fill / asset comparison. | Desktop composition check against the stated exclusions. |
| Sibling-page delta | Storm Damage Repair is a contained response board: narrow persistent signal rail, large condition field, calm evidence panels and document-style guidance. It is not another repair diagnostic or replacement decision page. | Page | `../PROJECT.md#9-page-visual-identity` | Named Section and layout-family comparison. | One bounded screenshot establishes a separate visual memory point. |
| Section composition | Use a deep-navy response rail beside `fire-damage.webp`; a mist review field; a slate-blue documentation section paired with `storm-repair.webp`; a soft-white `storm-roof.webp` evidence band; Demo FAQ; and a deep-navy inspection handoff. | Page Sections | `storm-damage-repair.md#page-narrative-and-sections` | Six named semantic Sections with nested layout owners. | Planned page rhythm review. |
| Colour rhythm | Start at deep navy against a mist/image condition field, move into mist review, slate-blue documentation, soft-white evidence, mist FAQ and quiet deep-navy close. This avoids the preceding page sequences. | Page Sections | `../PROJECT.md#6-brand-direction` | Fill-token readback per Section. | Desktop colour-block review. |
| Asset map | `fire-damage.webp` provides opening condition context, the approved `roof-damage.webp` alternate provides documentation / work context because `storm-repair.webp` is Missing, and `storm-roof.webp` is a narrow condition-evidence band. Verify exact factual Alt after residency check before upload. | Page image owners | `../PROJECT.md#11-responsive-interaction-and-assets` | Fill URL, Alt and breakpoint crop readback. | One screenshot verifies unique asset roles. |
| Responsive transformation | Desktop retains the narrow response rail and large condition field; Tablet stabilizes pairs; Phone orders inspection copy before supporting evidence, turns documentation into a readable single flow and retains a visible CTA. | Breakpoint owners | `storm-damage-repair.md#responsive-and-acceptance-contract` | Desktop 1200, Tablet 810, Phone 390 and 320 structural readback. | Representative Desktop review, then Phone only if visual risk requires it. |
| Completion evidence | Structural Pass requires live semantics, labels, links, Alt and responsive ownership. Visual Pass requires bounded proof of the response-board narrative, sibling delta, colour rhythm and asset roles. Preview and Marketplace Page Done remain separate. | QA | `../../../framer/checklist.md#2-每个-part-的通用完成门槛` | Clean diagnostics plus targeted live-tree evidence. | Recorded Image Review Plan and non-repeated Canvas review. |

## Page narrative and Sections

1. **Damage Response Opening** — `fire-damage.webp` provides condition context alongside a deep-navy response rail with one H1, concise Demo fit statement and `Request an Inspection` CTA. It must not claim availability, safety clearance or an emergency response.
2. **Start with a calmer review** — A mist-grey explanation of what an inspection conversation can clarify. The copy stays general and Demo, with no diagnosis or insurance outcome.
3. **Keep the right context together** — A slate-blue documentation field paired with the approved `roof-damage.webp` alternate, offering editable prompts for what a homeowner may want to note or photograph. It does not advise on safety or create legal/insurance guidance.
4. **Condition evidence band** — A narrow, soft-white `storm-roof.webp` media band to punctuate the page without claiming that it depicts the visitor’s property or a verified project.
5. **Storm damage questions, answered carefully** — A static Demo FAQ that avoids emergency service, response time, insurance, coverage, warranty, price, scheduling and restoration claims.
6. **Inspection handoff** — A quiet deep-navy close with one `Request an Inspection` CTA to `/#contact` until a real destination exists.

## Text, semantic and layer contract

- Reuse existing Text / Color Styles; add no global style for this one page.
- One H1 appears in the response rail. Major Section titles use H2; documentation prompts and FAQ questions use H3 or regular text according to their role.
- All new visible layers receive descriptive, responsibility-based names; no default Frame, Stack, Text or Image names.
- All explanatory copy is Demo. Do not add claims about emergency availability, hazard status, insurance, response time, credentials, scope, warranty, price, safety, local coverage or performance.

## Components, navigation and conversion

- Reuse the default `Site Shell` and current shared Button. Do not copy Navbar/Footer or introduce a Component, Variant, CMS collection, Overlay, form or Custom Code.
- Use ordinary authored Frames for static documentation prompts and FAQ rows; no accordion is required.
- After creation, update only the existing Services `Storm Damage Repair` row and its Desktop / Tablet / Phone replicas to `/services/storm-damage-repair`, then read back all destinations.
- The CTA remains `/#contact`; it may invite an inspection conversation but cannot imply live contact or urgent-response service exists.

## Image, responsive, interaction and accessibility contract

- Follow [`image-workflow.md`](../../../framer/basic/workflows/image-workflow.md). Before any visual review, record an Image Review Plan in `../PROJECT.md#14-recovery`; cap the build Part at one bounded Desktop screenshot and use structural fallback after that.
- Verify exact local-file residency and inspect source content before finalising factual Alt. Upload only `fire-damage.webp`, `roof-damage.webp` and `storm-roof.webp`; `storm-repair.webp` is Missing at its documented source path.
- Desktop 1200 owns the response rail and evidence field; Tablet 810 independently recomposes image/copy pairs; Phone 390 keeps a clear single-column reading order, 20px gutters and CTA before supporting evidence. Check 320px for overflow and 1440px for capped/centred composition.
- No motion, hover-only information, Overlay or Lightbox is required. Preserve keyboard order, visible focus, contrast and reduced-motion safety through the shared system.

## SEO, performance, Marketplace and Preview

- Proposed metadata title: `Storm Damage Repair | Summit Roofing`; proposed description: `Explore a calm, inspection-led approach to storm damage repair in this adaptable contractor template.` Both remain template copy pending brand-name resolution.
- Confirm one H1, logical H2/H3 order, factual Alt text and correct route. Favicon and Open Graph remain shared/final-preflight responsibilities.
- Use only supplied WebP assets, no third-party dependency and no Custom Code. Keep all Demo content easy for Marketplace buyers to replace; test long copy and alternate image proportions during Page Done.
- Targeted Preview is deferred until explicit authorization. Publication is excluded.

## Page Done threshold

- The live route has metadata, named semantic Sections, shared shell/Button, one H1, factual image Alt, Desktop/Tablet/Phone ownership and Services link replicas read back.
- The Visual Direction Contract has Structural and Visual Pass evidence, including its bounded image review.
- 320px, 1440px, Preview, real Contact route, licence verification and Marketplace publication remain explicitly classified rather than silently marked complete.

## Latest Part Result

Scope: Visual QA
Status: In progress — Structural and bounded Desktop visual Pass

Pass:
- The live `/services/storm-damage-repair` route has the recorded metadata, one H1, six named semantic Sections, the shared Button with `/#contact` CTA destinations, and the approved supplied-image roles with factual Alt text.
- Desktop 1200, Tablet 810 and Phone 390 own the authored page structures. The existing Services `Storm Damage Repair` row routes to this page on Desktop, Tablet and Phone.
- The documented `storm-repair.webp` source remains Missing; only the approved `roof-damage.webp` alternate was uploaded for the documentation field.
- One separately scoped Desktop QA screenshot confirms the calm response-board composition: the deep-navy response rail, large condition image, restrained slate documentation field, narrow condition-evidence band and quiet handoff establish the approved page rhythm without alarmist treatment or duplication of the other service pages.

Fix Required:
- None found by the targeted live structural readback.

Blocked:
- 320px, 1440px, Preview, real contact details/route, emergency and insurance facts, credentials, project facts, image licences and publication authorization remain unavailable or deferred.

Verified widths:
- Desktop 1200px: structural and bounded visual QA pass. Tablet 810px and Phone 390px: structural readback only.

Verified paths:
- `/services/storm-damage-repair` and Services-row destinations on `/services`.

Shared components affected:
- Reused Site Shell and Button; no shared Component was changed.

Recovery:
- Canonical current pointer: `../PROJECT.md#14-recovery`
- This Part result date: 2026-09-17
