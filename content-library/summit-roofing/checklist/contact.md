# Summit Roofing — Contact Page Checklist

- Contract schema: 1
- Component contract: N/A — this recorded Part contains no component contract; lifecycle migration makes no construction change.
- Visual contract: Required
- Evidence migration: 2026-10-03; repository-only. Original contract assertions are preserved in project History; no fresh Canvas or runtime proof was produced.

## Status

- Page: Contact
- Path: `/contact`
- Current status: In progress — Structural Pass at Desktop, Tablet and Phone for the form and FAQ; form delivery and runtime/visual review remain Blocked.
- Content status: Phone, email, address, service area, business hours, privacy text, form recipient and image licences are Missing. All supplied operational details must remain editable Demo/Missing content.
- Primary CTA: `Send Request` — native Framer form submission structure only; delivery configuration is blocked until the buyer supplies a recipient and privacy terms.

## Scope lock / Definition of Ready

- **Add:** one Contact route with a native Framer form structure, truthful setup messaging and one link to the existing `/services` route.
- **Reuse:** Site Shell, the existing hover-enabled Button for the service handoff and Request Form submit control, Big Shoulders / Inter, blue-grey tokens, square geometry and the three responsive breakpoint roles.
- **Modify:** `/contact` and the existing Button’s native form-state variants only. **No-op:** CMS, Navbar/Footer, existing CTA destinations, real contact facts, Custom Code, third-party form services and publishing.
- **Blocked:** real contact and service-area facts, form recipient/delivery confirmation, privacy text, commercial image licence and publication authorization. Do not invent any of them.

## Native submit-state repair — 2026-10-06

- User request: “I have change the send request button into the one with hover effect. Now add the incomplete, error, pending and success conditions to the button.”
- Current Canvas evidence: the Request Form now registers the shared `Controls/Button` instance as its submit control. This explicit user change supersedes the earlier page-owned `Contact Submit` ownership for this one form.
- Scope: add native `Incomplete`, `Pending`, `Success`, and `Error` variants to the existing shared Button definition, then assign them only to the Request Form’s `Send Request` instance. Preserve its existing hover state and leave every other Button instance unwired to form states.
- Non-goals: form recipient/delivery, privacy, contact facts, Custom Code, external integrations, publishing, and changes to unrelated CTA behaviour.

## Contact FAQ disclosure — 2026-10-06

- User request: “add a FAQ section to the contact page. refer to the QA knowledge in the repository. it can fold and unfold with hover effect”
- Constraint lock: retain the Contact form, Missing operational facts, existing token palette, named-layer discipline and page-owned Navbar/Footer. Add the FAQ before the existing Inspection Handoff; do not add a CMS collection, custom code, delivery configuration, invented service guarantees, response-time claims or publishing.
- Reuse / create decision: no existing FAQ component is available in the live component catalog. Create one native `Contact FAQ Row` Component with editable Question and Answer properties, semantic button trigger, Closed/Open states, existing project tokens and a Chevron indicator.
- Responsive interaction: Desktop and Tablet use pointer hover to reveal/collapse; Phone uses tap to toggle and a press cue. Rows begin on an explicit Pure White surface, use no scale transform and clip their parent during the height reveal.
- Content status: concise Demo guidance only; it must not present unverified availability, pricing, inspection, warranty, insurance, scheduling, privacy or delivery facts as true.

## Component Requirement Contract — Contact FAQ disclosure

Contract status: Blocked — implementation and structural readback pass; runtime Preview remains pending.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
| --- | --- | --- | --- | --- | --- |
| Section background / vertical rhythm | One Mist Grey FAQ Section now sits before Inspection Handoff in the existing full-width Contact stack. | Contact page | User request; current Contact page order | Pass — targeted live readback confirms section and sibling order at all breakpoints. | Pending — rendered rhythm. |
| Available width / placement | FAQ List and all row instances fill their Section’s available width; no arbitrary row `max-width`. | Contact FAQ Section + instances | `../../../framer/basic/standards/website-baseline.md#长条边框组件的宽度归属` | Pass — Desktop/Tablet/Phone width chain uses available width. | Pending — narrow/wide continuity. |
| Visible boundary / border / surface | Pure White Default row surface, Mist Grey border and Mist Grey Phone press surface; no new colours. | `Contact FAQ Row` | User request; project token rule | Pass — variant fills and borders use existing named tokens. | Pending — hover/press playback. |
| Internal padding / hit area | Row component owns 24px horizontal padding and a full-width semantic trigger. | `Contact FAQ Row` | `framer-components/SKILL.md#Assign responsibility` | Pass — component root and trigger read back. | Pending — pointer/touch target. |
| Readable max-width | N/A — FAQ answer line length is governed by the full row’s available width and Section padding. | Contact FAQ Section | `../../../framer/basic/standards/website-baseline.md#长条边框组件的宽度归属` | Pass — no row cap; Section padding governs line length. | Pending — answer wrapping. |
| Editable content / Properties | Question and Answer string properties are exposed; four Contact instances own their Demo guidance. | `Contact FAQ Row` + instances | `framer-components/SKILL.md#Assign responsibility` | Pass — variable bindings and four instances read back. | N/A — property-panel editability is structural. |
| States / routes | Closed/Open variants reveal the answer and swap Chevron Down/Up; no links or overlay required. | `Contact FAQ Row` | `framer` core FAQ pattern; user request | Pass — paired state routes read back. | Pending — open/close playback. |
| Breakpoint contract | Desktop/Tablet hover reveal; Phone tap reveal with press cue; all roots use Clip. | `Contact FAQ Row` | repository interaction convention; user request | Pass — seven states and three instance selections read back. | Pending — device input playback. |
| Accessibility / touch / focus | Native button trigger, readable question/answer copy and non-colour indicator change; no hover-only path on Phone. | `Contact FAQ Row` | `../PROJECT.md#10-system-and-platform-plan` | Pass — semantics, indicators and Phone tap path read back. | Pending — keyboard/focus playback. |
| Evidence sample | Verify definition, all four instances, section order and three breakpoint contracts. | Contact page + Component | `framer-components/SKILL.md#Implement in one layer at a time` | Pass — targeted live readback completed. | Pending — targeted Preview. |

## Component Requirement Contract — Native submit states

Contract status: Ready

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
| --- | --- | --- | --- | --- | --- |
| Visible boundary / surface | Retain the hover-enabled Blue Button; states use only existing Slate Blue, Deep Navy, Mist Grey and Pure White tokens. | `Controls/Button` | User request; `../PROJECT.md#6-brand-direction` | Pass — four variant surfaces and label colours read back. | Pending — native form-state playback. |
| Editable content / Properties | The normal label remains the Button label property; state labels are fixed feedback copy. | `Controls/Button` | Current shared Button controls; user request | Pass — all state labels and Button typography read back. | Pending — form playback. |
| States / routes | Add `Incomplete`, `Pending`, `Success`, and `Error` Blue-derived variants; map them only on the Request Form submit instance. | `Controls/Button` + Request Form | User request; Framer Forms guidance | Pass — all four mappings read back on the desktop, tablet and phone instances. | Pending — validation/submission playback. |
| Breakpoint contract | Create states from the Button’s shared Blue definition so the existing Contact Desktop, Tablet and Phone replicas inherit them. | `Controls/Button` | Current Canvas primary/replica structure | Pass — primary plus responsive replicas use the same mappings. | Pending — native form playback. |
| Accessibility / touch / focus | Pending uses a progress cursor; incomplete lowers opacity; feedback labels make state changes understandable without relying on colour only. | `Controls/Button` | Framer Forms guidance; user request | Pass — state labels, opacity and cursors read back. | Pending — keyboard/focus playback. |
| Evidence sample | Verify Button variants, Request Form submit registration, four native mappings, label correction, and unaffected hover variant. | `Controls/Button` + Request Form | `framer-components` implementation sequence | Pass — targeted live readback completed. | Pending — runtime. |

## Current native submit-state result — 2026-10-06

Status: Structural Pass / native runtime playback and delivery remain Blocked.

- `Send Request Submit` is the Request Form’s registered shared Button instance at all three responsive breakpoints; its normal label is `Send Request` and its existing Blue hover remains intact.
- `Incomplete`: muted Slate Blue, `Complete Required Fields`, default cursor and no arrow.
- `Pending`: Slate Blue, `Sending Request…`, progress cursor and no arrow.
- `Success`: Deep Navy, `Request Sent`, Pure White label, default cursor and no arrow.
- `Error`: Mist Grey, `Try Again`, Deep Navy label and retry affordance.
- No recipient, privacy configuration or real submission was added; this work only supplies native Framer feedback states.

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
4. **Frequently Asked Questions** — mist-grey disclosure section before the handoff, with four editable Contact FAQ rows. Desktop and Tablet reveal on hover; Phone uses tap with a press cue. Each row uses a Pure White default surface, a Mist Grey border and a Chevron state indicator.
5. **Service Handoff** — slate-blue close with `Explore Services` → `/services`, retaining a clear path if the visitor is still deciding what they need.

## Text, styles, components and CMS

- Reuse the existing display/body styles; one H1, H2 Section titles, and purposeful layer names.
- Reuse Site Shell and the existing Button for the service handoff and the Request Form submit control. The submit states belong to Button, but are mapped only on the Request Form instance; create no CMS collection, Custom Code or external integration.
- `Contact FAQ Row` owns its Question and Answer properties, semantic button trigger, Chevron state, surface, padding and Closed/Open variants. The Contact page owns its four Demo guidance entries and available-width placement.
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

- `/contact` has metadata, shared shell/Button, five semantic Sections, one H1, labelled fields, an explicit delivery limitation, truthful Missing messaging, a reusable FAQ disclosure and independent breakpoint owners.
- Structural and bounded visual evidence are recorded. Form delivery, legal/privacy facts, stress widths, Preview submission and publication remain explicit blockers.

## Latest Part Result

Scope: Contact route build and structural QA
Status: Structural Pass / Delivery, runtime interaction and visual review Blocked

Pass:
- `/contact` is live with Site Shell metadata, five named semantic Sections, one H1 and four H2s, truthful Missing-state messaging, and an `Explore Services` CTA to `/services`.
- The new Mist Grey FAQ Section sits before Inspection Handoff and contains four named `Contact FAQ Row` instances. Their editable Question/Answer properties use Pure White defaults, Mist Grey borders and no scale transform; all disclosure roots clip their height reveal.
- Structural readback confirms Desktop and Tablet Closed/Open hover routes, Phone Closed/Open tap routes plus a no-scale Phone Press state, Chevron Down/Up indicators, semantic button triggers and correct instance selection at all three breakpoints.
- The native form has linked visible labels and Name (required text), Email (required email), Phone (optional tel), and Project Note (required textarea) inputs. Its final `Send Request Submit` shared Button instance is semantic `button`, registered as the form submit control, and maps all four native feedback states.
- Structural readback confirms Desktop 1200 uses two columns in the request workspace and details notice; Tablet 810 and Phone 390 transform both to one readable column with reduced gutters.
- Responsive repair: the workspace now owns a nested Desktop two-column sequence, while Tablet uses a 48px vertical sequence and Phone a 36px vertical sequence. This removes the one-column grid track that created the reported blank space before the form.
- No CMS schema, shared component, Custom Code, external form service, factual contact record or publication changed.

Fix Required:
- None in the authorized `/contact` scope.

Blocked:
- Real contact facts, form recipient/delivery configuration, privacy terms, a successful-submission Preview, FAQ pointer/tap/keyboard playback and publication authorization.
- The one bounded Phone workspace screenshot for the responsive repair was generated but could not be inspected in this workspace. No visual inference is recorded; another visual review requires a separately scoped QA Part.

Verified widths:
- Structural: Desktop 1200, Tablet 810 and Phone 390, including the FAQ disclosure contract.
- Deferred: 320 and 1440 stress widths, visual composition review, keyboard/focus Preview and successful form submission.

Verified paths:
- `/contact`; handoff target `/services`.

Shared components affected:
- Site Shell is unchanged. The existing Button gained four native feedback variants; only the Request Form’s `Send Request Submit` instance maps to them, so other CTA instances retain their normal behaviour. `Contact FAQ Row` is new and scoped to Contact.

Recovery:
- Canonical current pointer: `../PROJECT.md#14-recovery`
- This Part result date: 2026-09-18
