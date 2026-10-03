# Summit Roofing — Contact Page Checklist

- Contract schema: 1
- Component contract: N/A — this recorded Part contains no component contract; lifecycle migration makes no construction change.
- Visual contract: Required
- Evidence migration: 2026-10-03; repository-only. Original contract assertions are preserved in project History; no fresh Canvas or runtime proof was produced.

## Status

- Page: Contact
- Path: `/contact`
- Current status: In progress — Structural Pass at Desktop, Tablet and Phone; form delivery and visual review remain Blocked.
- Content status: Phone, email, address, service area, business hours, privacy text, form recipient and image licences are Missing. All supplied operational details must remain editable Demo/Missing content.
- Primary CTA: `Send Request` — native Framer form submission structure only; delivery configuration is blocked until the buyer supplies a recipient and privacy terms.

## Scope lock / Definition of Ready

- **Add:** one Contact route with a page-owned native Framer form structure, a page-specific semantic `Contact Submit` control, truthful setup messaging and one link to the existing `/services` route.
- **Reuse:** Site Shell, existing Button for the service handoff, Big Shoulders / Inter, blue-grey tokens, square geometry and the three responsive breakpoint roles.
- **Modify:** `/contact` only. **No-op:** shared components, CMS, Navbar/Footer, existing CTA destinations, real contact facts, Custom Code, third-party form services and publishing.
- **Blocked:** real contact and service-area facts, form recipient/delivery confirmation, privacy text, commercial image licence and publication authorization. Do not invent any of them.

## Visual Direction Contract

Contract status: Blocked — structural evidence is recorded; visual evidence and form delivery are blocked for this Part.
Implementation status: Implemented — historical completion record; current live state not reverified.
Verification status: Blocked — retain bounded historical results; outstanding evidence requires the live Framer gate.

| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |
|---|---|---|---|---|---|
| Design Read | A practical enquiry threshold, not a local-office profile or a generic card wall. | Page | `../PROJECT.md#4-website-goal` | Blocked — original record: One H1, page-owned form and named Sections.; a row-specific completed result is not established here. | Blocked — original record: One bounded Desktop review.; a row-specific completed result is not established here. |
| Preserve | Shared shell, condensed display type, blue-grey tokens, square geometry and direct CTA language. | Shared system | `../PROJECT.md#6-brand-direction` | Blocked — original record: Shell/style/Button readback.; a row-specific completed result is not established here. | Blocked — original record: Compare with live siblings.; a row-specific completed result is not established here. |
| Transform | Build a text-and-form conversion sequence with no unverified location image or credential content. | Page | `contact.md#page-narrative-and-sections` | Blocked — original record: Four Sections and field ownership.; a row-specific completed result is not established here. | Blocked — original record: Functional, non-card-wall composition.; a row-specific completed result is not established here. |
| Avoid | No phone/email/address placeholders presented as real, map, office-hours claims, testimonials, metrics, external form service or third-party embed. | Page | `../PROJECT.md#7-content-facts` | Blocked — original record: Text/link/form readback.; a row-specific completed result is not established here. | Blocked — original record: Desktop exclusion check.; a row-specific completed result is not established here. |
| Sibling-page delta | Contact is an operational request desk, unlike About's people field or Projects' evidence record. | Page | `../PROJECT.md#9-narrative-and-conversion` | Blocked — original record: Section sequence comparison.; a row-specific completed result is not established here. | Blocked — original record: One distinct memory point.; a row-specific completed result is not established here. |
| Section composition | Deep-navy request threshold; soft-white form workspace; mist editable-contact notice; slate-blue service handoff. | Page | `contact.md#page-narrative-and-sections` | Blocked — original record: Fill/width owner readback.; a row-specific completed result is not established here. | Blocked — original record: Colour and hierarchy review.; a row-specific completed result is not established here. |
| Colour rhythm | Deep navy / soft white / mist / slate blue. | Page | `../PROJECT.md#6-brand-direction` | Blocked — original record: Token readback.; a row-specific completed result is not established here. | Blocked — original record: Desktop review.; a row-specific completed result is not established here. |
| Asset map | No image is used: a verified office/contact scene is Missing and photography would not improve an editable form flow. | Page | `../PROJECT.md#11-responsive-interaction-and-assets` | Blocked — original record: No page-owned image node.; a row-specific completed result is not established here. | Blocked — original record: N/A.; a row-specific completed result is not established here. |
| Responsive transformation | Desktop uses a wide request workspace; Tablet stabilizes the text/form pair; Phone becomes a single reading and input column with 20px gutters. | Breakpoints | `contact.md#image-responsive-interaction-and-accessibility` | Blocked — original record: 1200/810/390 readback.; a row-specific completed result is not established here. | Blocked — original record: Desktop review; Phone later only if needed.; a row-specific completed result is not established here. |
| Completion evidence | Structural: semantic Sections, heading order, field labels/types, honest delivery state, CTA and responsive owners. Visual: one bounded composition review. | QA | `../../../framer/checklist.md#2-每个-part-的通用完成门槛` | Blocked — original record: Diagnostics/readback.; a row-specific completed result is not established here. | Blocked — original record: Recorded plan and one review.; a row-specific completed result is not established here. |

## Page narrative and Sections

1. **Request Threshold** — deep-navy, no-photo opening with one H1: `START WITH A CLEAR REQUEST.` It explains that the buyer should add verified contact and service-area information before publishing.
2. **Request Workspace** — soft-white two-column field: a practical H2 and a native Framer form with visible labels for name, email, phone (optional) and project note. The button is `Send Request`; no delivery success claim is made.
3. **Contact Details Setup** — mist editable notice that phone, email, address, hours, privacy terms and form recipient are Missing. It must not resemble published local business details.
4. **Service Handoff** — slate-blue close with `Explore Services` → `/services`, retaining a clear path if the visitor is still deciding what they need.

## Text, styles, components and CMS

- Reuse the existing display/body styles; one H1, H2 Section titles, and purposeful layer names.
- Reuse Site Shell and Button only for the service handoff. The form and semantic `Contact Submit` component remain page-owned; create no shared form Component, CMS collection, Custom Code or external integration.
- Use native controls with visible labels. Email must use the email input type; phone remains optional and must use the phone input type.

## Navigation, conversion and form delivery

- Navbar/Footer stay shared and unchanged. `Explore Services` links to the existing `/services` route.
- Existing `/#contact` fallbacks are outside this scope; do not silently rewrite shared CTA destinations.
- Use native Framer form structure only. The form recipient, privacy statement, successful delivery verification and error-state Preview are Blocked until factual details and buyer configuration exist.

## Image, responsive, interaction and accessibility

- No page-owned images: therefore no image crop or Alt claim is needed for this route.
- Desktop 1200 owns the two-column request workspace. Tablet 810 preserves readable field widths; Phone 390 stacks into one reading/input column with 20px gutters. Defer 320/1440 stress checks.
- Preserve semantic reading order, visible labels, keyboard order, focus, touch-safe inputs and reduced motion. No hover-only information, overlay or motion is added.

## SEO, performance, Marketplace and Preview

- Metadata: `Contact | Summit Roofing`; `Editable enquiry page for a roofing contractor template. Replace contact and privacy details before publishing.`
- No third-party dependency or image payload is added. Marketplace replacement pressure: long headings, empty optional phone, missing recipient/privacy details and editable form labels must remain clear.
- Targeted Preview path: `/contact`. A real submission is excluded until a legitimate recipient and privacy basis are supplied.

## Page Done threshold

- `/contact` has metadata, shared shell/Button, four semantic Sections, one H1, labelled fields, an explicit delivery limitation, truthful Missing messaging and independent breakpoint owners.
- Structural and bounded visual evidence are recorded. Form delivery, legal/privacy facts, stress widths, Preview submission and publication remain explicit blockers.

## Latest Part Result

Scope: Contact route build and structural QA
Status: Structural Pass / Delivery and Visual Blocked

Pass:
- `/contact` is live with Site Shell metadata, four named semantic Sections, one H1 and three H2s, truthful Missing-state messaging, and an `Explore Services` CTA to `/services`.
- The native form has linked visible labels and Name (required text), Email (required email), Phone (optional tel), and Project Note (required textarea) inputs. Its final page-specific `Contact Submit` instance is semantic `button` and is registered as the form submit control.
- Structural readback confirms Desktop 1200 uses two columns in the request workspace and details notice; Tablet 810 and Phone 390 transform both to one readable column with reduced gutters.
- Responsive repair: the workspace now owns a nested Desktop two-column sequence, while Tablet uses a 48px vertical sequence and Phone a 36px vertical sequence. This removes the one-column grid track that created the reported blank space before the form.
- No CMS schema, shared component, Custom Code, external form service, factual contact record or publication changed.

Fix Required:
- None in the authorized `/contact` scope.

Blocked:
- Real contact facts, form recipient/delivery configuration, privacy terms, a successful-submission Preview and publication authorization.
- The one bounded Phone workspace screenshot for the responsive repair was generated but could not be inspected in this workspace. No visual inference is recorded; another visual review requires a separately scoped QA Part.

Verified widths:
- Structural: Desktop 1200, Tablet 810 and Phone 390.
- Deferred: 320 and 1440 stress widths, visual composition review, keyboard/focus Preview and successful form submission.

Verified paths:
- `/contact`; handoff target `/services`.

Shared components affected:
- Reused only: Site Shell and existing Button for the service handoff. `Contact Submit` is page-owned and does not alter shared Button behaviour.

Recovery:
- Canonical current pointer: `../PROJECT.md#14-recovery`
- This Part result date: 2026-09-18
