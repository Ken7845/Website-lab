# Home — Navbar, Trust Bar, and Contact Revision

> Reconciled 2026-10-13 from REX-2 and project observations; live Needs refresh. [Exact earlier contract](../../history/2026-10-13-before-width-closeout-repair.md) is preserved as history. Current owner: [Status](../../PROJECT.md#12-current-status). Dated Pass cells describe only their named historical checks.

- Page: Home
- Path: `/`
- Date: 2026-10-13
- Contract schema: 1
- Component contract: Required
- Component scope: shared Navbar, Footer, and Trust Bar ownership changes.
- Visual contract: N/A — scoped refinement under the existing passed Home visual direction; no new page or major narrative redesign.
- Authorization: Authorized — current user request explicitly asks to revise and implement these areas.
- Implementation status: Implemented
- Verification status: Blocked — dated evidence is retained; later U5 changes and width removal require scoped visual/runtime revalidation.

## User Request — Verbatim

1.improve and revise the navbar and footer refer to the repository, especially the 'component' and 'response' issue 2. revise the Confidence part and turn it into a trust bar. use the images in the trust badges folder and apply a ticker effect. 3. input an image in the contact section to make this section better

## Constraint Lock

- Preserve the existing dark theme, bright coral hover treatment, source-backed copy, verified links, and one-page scope.
- Replace page-owned Navbar and Footer frames with native shared Framer Components; use Desktop, Tablet, and Phone variants, plus explicit Phone Closed/Open navigation states.
- Replace Confidence with a native Trust Bar using the five supplied trust-badge images and one restrained continuous ticker.
- Add one existing REX project photo to the Contact section and keep the enquiry actions prominent.
- Do not change unrelated sections, add custom code or paid dependencies, publish the project, or introduce new factual trust claims in text.
- Verify the component definitions, representative page instances, 390 / 810 / 1200 responsive results, Phone navigation states, ticker structure, image crop, and preview readiness.

## Component Requirement Contract

- Contract status: Blocked — dated implementation evidence is partial; current proof limitations are explicit below.
- Implementation status: Partial — original work implemented; later corrections and unresolved dependencies are recorded in Current Status.
- Verification status: Blocked — no fresh Canvas verification in this repository reconciliation.
- Authorization: Authorized — user request above.
- Add / Reuse / Modify: Create shared Navbar, Footer, and Trust Bar definitions; reuse the Inspection Button, styles, tokens, logo, verified links, and supplied badge images; replace the three current page-owned frames.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Navbar/Footer keep Canvas surfaces and dividers; Trust Bar uses a compact Canvas band; Contact retains its existing section rhythm | Component definitions and Contact panel | `.agents/skills/framer-components/SKILL.md#assign-responsibility`; current Canvas evidence | Pass — fills, borders, heights and final page order read back; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. | Pass — Desktop and Phone section evidence, 2026-10-13; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. |
| Available width / placement | Structural parents distribute available width with Fill / existing responsive width; max-width None. Local Button intrinsic sizing is separate; no approved bounded-shell exception. | Page root, structural wrappers, shared definitions, instances and breakpoint overrides | framer/basic/standards/website-baseline.md#max-width-ownership | Pass — dated 2026-10-13 global readback found zero remaining maxWidth after 27 caps were cleared; [width correction](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-home-parent-width-correction). Current live state Needs refresh. | Blocked — three breakpoint captures do not prove 320 / 1440+ stress widths or all runtime states after cap removal. |
| Visible boundary / border / surface | Preserve charcoal surfaces, quiet dividers and coral interactive emphasis; badge tiles provide consistent light surfaces | Component definitions | User theme direction; `framer/basic/standards/website-baseline.md#3-style-system` | Pass — token, divider and native loop attributes read back; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. | Pass — Navbar, Trust Bar, Contact and Footer visual evidence, 2026-10-13; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. |
| Internal padding / hit area | Navbar controls are at least 48px on Phone; Footer groups and badge tiles keep readable padding | Component definitions | `framer/basic/patterns/navbar-footer.md#2-navbar-要求`; `framer/basic/patterns/buttons.md#component-内部结构` | Pass — 48px Phone menu controls and component padding read back; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. | Pass — Phone Closed/Open screenshots, 2026-10-13; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. |
| Readable max-width | Any future reading limit belongs to a specific text/local geometry owner; never restore a shared 1120px parent cap. No new local cap is approved by this reconciliation. | Local text or proven component geometry only | framer/basic/standards/website-baseline.md#max-width-ownership | Pass — dated scan recorded no remaining caps; [width correction](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-home-parent-width-correction). Future local limits require their own owner decision. | Blocked — local line lengths and wrapping need targeted narrow/wide visual evidence after the width repair. |
| Editable content / Properties | Static site identity and verified routes remain definition-owned; reuse Inspection Button Label/Link Properties; badge assets remain individually replaceable layers | Definitions and nested button instance | `.agents/skills/framer-components/SKILL.md#assign-responsibility`; current Button controls | Pass — four component definitions and exposed variant controls read back; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. | Pass — representative component instances reviewed, 2026-10-13; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. |
| States / routes | Navbar Desktop/Tablet/Phone/Phone Open variants; exact SET_VARIANT menu routes; all route, phone, email and inspection links preserved | Navbar definition and page instances | `framer/basic/patterns/navbar-footer.md#phone-drawer-variant紧凑-navbar-的推荐模式`; user requirement 1 | Pass — exact Open and Close actions plus hrefs read back; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. | Blocked — prior record: Pass — Closed/Open states reviewed; live click execution remains unavailable without staging; scope-specific completion evidence is incomplete or superseded. See [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). |
| Breakpoint contract | One instance per shared component in the primary page; instance variant matches Desktop/Tablet/Phone; Contact is horizontal on Desktop and vertical on Tablet/Phone | Page instance overrides and component variants | `.agents/skills/framer-components/SKILL.md#inspect-before-creating`; current breakpoints | Pass — 1200 / 810 / 390 instance variants and Contact overrides; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. | Pass — Desktop and Phone visual; Tablet structural evidence, 2026-10-13; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. |
| Accessibility / touch / focus | Native links, meaningful image Alt, labeled menu controls, 48px touch targets; duplicated ticker badges use empty Alt | Definitions and Contact image | `framer/basic/patterns/navbar-footer.md#5-发布前检查`; user requirement 2 | Pass — semantics, links, Alt and controls read back; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. | Pass — Phone states and readable no-motion content structure reviewed; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. |
| Evidence sample | Navbar definition + page instance + Phone states; Footer definition + instance; Trust Bar definition + page instance; Contact image at all breakpoints | QA | `.agents/skills/framer-components/SKILL.md#implement-in-one-layer-at-a-time` | Pass — targeted definition, instance and breakpoint readback, 2026-10-13; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. | Pass — bounded component/page screenshots and clean preview readiness, 2026-10-13; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-shared-shell-and-trust-revision). Dated result only; later changes are not covered. |

## Acceptance Checklist

- [x] Navbar and Footer are native shared Components with responsive variants.
- [x] Phone navigation opens and closes through explicit component state actions.
- [x] Confidence is replaced by a Trust Bar that uses all five supplied badge images.
- [x] The badge row has a restrained native ticker effect and no essential text depends on motion.
- [x] Contact includes one relevant project image with meaningful Alt and responsive crop.
- [x] Existing verified links and copy remain intact.
- [x] Definition, instance, breakpoint and preview evidence is recorded.
