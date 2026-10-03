# Summit Roofing — About Page Checklist

- Contract schema: 1
- Component contract: N/A — this recorded Part contains no component contract; lifecycle migration makes no construction change.
- Visual contract: Required
- Evidence migration: 2026-10-03; repository-only. Original contract assertions are preserved in project History; no fresh Canvas or runtime proof was produced.

## Status

- Page: About
- Path: `/about`
- Current status: In progress — Structural Pass at Desktop, Tablet and Phone; Visual Blocked after the single bounded Desktop review result became unavailable.
- Content status: Team names, biographies, tenure, credentials, awards, service area and image licences are Missing. Crew imagery is supplied but its people/place facts are unverified.
- Primary CTA: `Discuss a Project` → `/#contact`.

## Scope lock / Definition of Ready

- **Add:** after approval, one authored About page using supplied crew imagery and Demo working-principle copy.
- **Reuse:** Site Shell, Button, Big Shoulders / Inter, blue-grey tokens, square geometry and responsive system.
- **Modify:** `/about` only. **No-op:** CMS, shared components, Home, Projects, services, forms, Custom Code, publishing and brand-name resolution.
- **Blocked:** real company history, leadership bios, claims, credentials, licences and Contact details. Do not invent them.

## Visual Direction Contract

Contract status: Blocked — structural evidence is recorded; visual evidence is blocked for this Part.
Implementation status: Implemented — historical completion record; current live state not reverified.
Verification status: Blocked — retain bounded historical results; outstanding evidence requires the live Framer gate.

| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |
|---|---|---|---|---|---|
| Design Read | A people-and-principles working standard, not a corporate timeline. | Page | `../PROJECT.md#6-brand-direction` | Blocked — original record: One H1 and named Sections.; a row-specific completed result is not established here. | Blocked — original record: One bounded Desktop review.; a row-specific completed result is not established here. |
| Preserve | Shared shell, typography, tokens, square geometry and direct CTA. | Shared system | `../PROJECT.md#10-system-and-platform-plan` | Blocked — original record: Shell/style/Button readback.; a row-specific completed result is not established here. | Blocked — original record: Compare with live siblings.; a row-specific completed result is not established here. |
| Transform | Crew threshold, editorial standard, uneven principles field, editable people panel and quiet close. | Page | `about.md#page-narrative-and-sections` | Blocked — original record: Five Sections and image owners.; a row-specific completed result is not established here. | Blocked — original record: Human, practical composition review.; a row-specific completed result is not established here. |
| Avoid | No founder story, profile cards, metrics, awards, testimonials, timeline or credential badges. | Page | `../PROJECT.md#7-content-facts` | Blocked — original record: Text/link readback.; a row-specific completed result is not established here. | Blocked — original record: Desktop exclusion check.; a row-specific completed result is not established here. |
| Sibling-page delta | About is a standards-and-people field, unlike Projects’ archive or Project Detail’s record sheet. | Page | `../PROJECT.md#9-narrative-and-conversion` | Blocked — original record: Section/asset comparison.; a row-specific completed result is not established here. | Blocked — original record: One distinct memory point.; a row-specific completed result is not established here. |
| Section composition | Deep-navy image threshold; white standard; mist principles; slate editable people panel; white handoff. | Page | `about.md#page-narrative-and-sections` | Blocked — original record: Fill/width owner readback.; a row-specific completed result is not established here. | Blocked — original record: Colour and hierarchy review.; a row-specific completed result is not established here. |
| Colour rhythm | Deep navy/image / soft white / mist / slate blue / soft white. | Page | `../PROJECT.md#6-brand-direction` | Blocked — original record: Token readback.; a row-specific completed result is not established here. | Blocked — original record: Desktop review.; a row-specific completed result is not established here. |
| Asset map | Use only `team.webp`, `crew-lead.webp`, `roof-harness.webp`; no identity or credential claim. | Page assets | `../PROJECT.md#11-responsive-interaction-and-assets` | Blocked — original record: Image/Alt readback.; a row-specific completed result is not established here. | Blocked — original record: Non-decorative role review.; a row-specific completed result is not established here. |
| Responsive transformation | Desktop editorial field; Tablet stabilizes pairs; Phone is one reading column with 20px gutters. | Breakpoints | `about.md#image-responsive-interaction-and-accessibility` | Blocked — original record: 1200/810/390/320 checks.; a row-specific completed result is not established here. | Blocked — original record: Desktop review; Phone later only if needed.; a row-specific completed result is not established here. |
| Completion evidence | Structural: semantic Sections, H1, truthful Demo copy, Alt, CTA and responsive owners. Visual: bounded composition proof. | QA | `../../../framer/checklist.md#2-每个-part-的通用完成门槛` | Blocked — original record: Diagnostics/readback.; a row-specific completed result is not established here. | Blocked — original record: Recorded plan and one review.; a row-specific completed result is not established here. |

## Page narrative and Sections

1. **Working Standard Threshold** — crew image, H1 and editable-template label; no history or credentials.
2. **Why the Standard Exists** — soft-white Demo statement about practical communication.
3. **Working Principles Field** — uneven field for clear assessment, organised work and a direct next step.
4. **Editable People Panel** — crew imagery plus replacement instruction for names and verified details.
5. **Service Handoff** — `Discuss a Project` CTA to `/#contact`.

## Text, components, navigation and conversion

- Reuse styles; one H1, H2 section titles and descriptive layer names.
- Reuse Site Shell and Button; no new components, CMS, variants, motion, overlays, Lightbox, Forms or Custom Code.
- Navbar/Footer remain shared. Links may use existing `/services` or `/projects`; CTA stays `/#contact`.

## Image, responsive, interaction and accessibility

- Follow [`image-workflow.md`](../../../framer/basic/workflows/image-workflow.md); write one Desktop Image Review Plan before review.
- Use only the documented About assets; factual Alt describes scene, not identity or location.
- Own Desktop 1200, Tablet 810 and Phone 390 independently; defer 320/1440 stress. Preserve keyboard order, visible focus, contrast and reduced motion.

## SEO, performance, Marketplace and Preview

- Proposed metadata: `About | Summit Roofing`; `Editable working-principles and team-imagery page for a roofing contractor template.`
- Verify heading order, Alt, CTA/path, long labels, alternate crops and missing optional people details. No third-party dependency. Preview and publication are excluded.

## Page Done threshold

- `/about` has metadata, shared shell/Button, five semantic Sections, one H1, truthful Demo copy, supplied-image Alt and responsive ownership.
- No real company record is implied; bounded visual evidence is recorded. Stress widths, Preview, facts, licences and publishing remain explicit.

## Latest Part Result

Scope: About route build and QA
Status: Structural Pass / Visual Blocked

Pass:
- `/about` is live with the shared Site Shell, metadata, five named semantic Sections, one H1, H2/H3 hierarchy, truthful Demo copy and the shared Button CTA to `/#contact`.
- Structural readback confirms intentional responsive ownership at Desktop 1200, Tablet 810 and Phone 390: the hero and people panel move from two columns to one; the principles field remains three columns on Tablet and becomes one column on Phone.
- No CMS schema, shared component, form, Custom Code, publishing action or factual company claim was added.

Fix Required:
- None in the authorized `/about` scope.

Blocked:
- The one planned Desktop screenshot was generated, but its locally reduced review output became unavailable during context interruption. No visual inference is recorded and this Part's one-image budget is exhausted; later visual QA requires a separately scoped Part.
- Real company/team facts, image licences, Contact details and publication authorization.

Verified widths:
- Structural: Desktop 1200, Tablet 810 and Phone 390.
- Deferred: 320 and 1440 stress widths, live Preview, keyboard/focus and rendered Alt checks.

Verified paths:
- `/about`; CTA fallback `/#contact`.

Shared components affected:
- Reused only: Site Shell and Button; no shared-component modification.

Recovery:
- Canonical current pointer: `../PROJECT.md#14-recovery`
- This Part result date: 2026-09-18
