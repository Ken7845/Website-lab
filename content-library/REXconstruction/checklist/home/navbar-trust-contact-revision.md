# Home — Navbar, Trust Bar, and Contact Revision

- Page: Home
- Path: `/`
- Date: 2026-10-13
- Contract schema: 1
- Component contract: Required — shared Navbar, Footer, and Trust Bar ownership changes.
- Visual contract: N/A — scoped refinement under the existing passed Home visual direction; no new page or major narrative redesign.
- Authorization: Authorized — current user request explicitly asks to revise and implement these areas.
- Implementation status: Implemented
- Verification status: Pass — definition, instance, responsive and bounded visual evidence recorded; preview readiness is clean.

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

- Contract status: Pass
- Authorization: Authorized — user request above.
- Add / Reuse / Modify: Create shared Navbar, Footer, and Trust Bar definitions; reuse the Inspection Button, styles, tokens, logo, verified links, and supplied badge images; replace the three current page-owned frames.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Navbar/Footer keep Canvas surfaces and dividers; Trust Bar uses a compact Canvas band; Contact retains its existing section rhythm | Component definitions and Contact panel | `prompt/design-rules.md#Spacing`; current Canvas evidence | Pass — fills, borders, heights and final page order read back | Pass — Desktop and Phone section evidence, 2026-10-13 |
| Available width / placement | Page instances fill available width; internal wrappers stay centered at 1120px; Contact image and copy share the existing panel | Page instances and component roots | `prompt/core-principles.md#Core-Principles`; current Canvas evidence | Pass — definition → instance → breakpoint width chain at 1200 / 810 / 390 | Pass — Desktop, Tablet structural and Phone visual evidence, 2026-10-13 |
| Visible boundary / border / surface | Preserve charcoal surfaces, quiet dividers and coral interactive emphasis; badge tiles provide consistent light surfaces | Component definitions | User theme direction; `prompt/design-rules.md#Colors` | Pass — token, divider and native loop attributes read back | Pass — Navbar, Trust Bar, Contact and Footer visual evidence, 2026-10-13 |
| Internal padding / hit area | Navbar controls are at least 48px on Phone; Footer groups and badge tiles keep readable padding | Component definitions | `framer/basic/patterns/navbar-footer.md#2-navbar-要求`; `prompt/design-rules.md#Components` | Pass — 48px Phone menu controls and component padding read back | Pass — Phone Closed/Open screenshots, 2026-10-13 |
| Readable max-width | Navigation/Footer content max 1120px; Trust label remains concise; Contact copy stays in a bounded column | Component roots and Contact panel | `prompt/how-projects-work.md#Width-Rules` | Pass — max-width and text-width readback | Pass — Desktop/Phone wraps reviewed, 2026-10-13 |
| Editable content / Properties | Static site identity and verified routes remain definition-owned; reuse Inspection Button Label/Link Properties; badge assets remain individually replaceable layers | Definitions and nested button instance | `prompt/how-projects-work.md#Components`; current Button controls | Pass — four component definitions and exposed variant controls read back | Pass — representative component instances reviewed, 2026-10-13 |
| States / routes | Navbar Desktop/Tablet/Phone/Phone Open variants; exact SET_VARIANT menu routes; all route, phone, email and inspection links preserved | Navbar definition and page instances | `prompt/how-projects-work.md#Navigation-with-Drawer`; user requirement 1 | Pass — exact Open and Close actions plus hrefs read back | Pass — Closed/Open states reviewed; live click execution remains unavailable without staging |
| Breakpoint contract | One instance per shared component in the primary page; instance variant matches Desktop/Tablet/Phone; Contact is horizontal on Desktop and vertical on Tablet/Phone | Page instance overrides and component variants | `prompt/how-projects-work.md#Working-with-Existing-Components`; current breakpoints | Pass — 1200 / 810 / 390 instance variants and Contact overrides | Pass — Desktop and Phone visual; Tablet structural evidence, 2026-10-13 |
| Accessibility / touch / focus | Native links, meaningful image Alt, labeled menu controls, 48px touch targets; duplicated ticker badges use empty Alt | Definitions and Contact image | `framer/basic/patterns/navbar-footer.md#5-发布前检查`; user requirement 2 | Pass — semantics, links, Alt and controls read back | Pass — Phone states and readable no-motion content structure reviewed |
| Evidence sample | Navbar definition + page instance + Phone states; Footer definition + instance; Trust Bar definition + page instance; Contact image at all breakpoints | QA | `framer-components/SKILL.md#Implement-in-one-layer-at-a-time` | Pass — targeted definition, instance and breakpoint readback, 2026-10-13 | Pass — bounded component/page screenshots and clean preview readiness, 2026-10-13 |

## Acceptance Checklist

- [x] Navbar and Footer are native shared Components with responsive variants.
- [x] Phone navigation opens and closes through explicit component state actions.
- [x] Confidence is replaced by a Trust Bar that uses all five supplied badge images.
- [x] The badge row has a restrained native ticker effect and no essential text depends on motion.
- [x] Contact includes one relevant project image with meaningful Alt and responsive crop.
- [x] Existing verified links and copy remain intact.
- [x] Definition, instance, breakpoint and preview evidence is recorded.
