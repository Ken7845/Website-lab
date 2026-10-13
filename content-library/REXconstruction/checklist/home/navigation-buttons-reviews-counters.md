# Home — Navigation, Buttons, Reviews, and Counters Revision

- Page: Home
- Path: `/`
- Date: 2026-10-13
- Contract schema: 1
- Component contract: Required — Navbar, Inspection Button, Review Selector, and Counter responsibilities are in scope.
- Visual contract: N/A — targeted refinement under the existing passed Home visual direction.
- Authorization: Authorized — the current user request explicitly asks to implement all four items.
- Implementation status: Partial — Navbar, both button components, and Review Selector are implemented; Counter definition exists, but Hero instances await approved metric values.
- Verification status: Pass for implemented scope — structural readback, screenshots, six selector mappings, and preview readiness are verified; runtime interactions and metric placement remain unverified/blocked.

## User Request — Verbatim

1.you can refer to the nabber in Submit Roofing, like the hover effect and the organization of the stacks, especially the Phone Drawer. 
2.Use a filling hover effect in the button component. You can also refer to the button in the submit roofing. The button is the current red and the filler is the brighter red.
3.The review section is so simple. Make a card selector for this section. The review details are in the reviews.md
4.	Make a counter component and put them in the hero section. The method is in the advanced-design. Three counters: Years of Experience, Roofs Installed and Client Rating

## User Request — Verbatim, Follow-up

1. remove the hover effect in the phone navbar. first, no hover in Phone. second, no offset in hover. 2.I forget to save the reviews.md and now it exist. 3. no shadow in the button component. the button has radius and the filler should also have it. I effect I want is the filler fill the button from the left to the right. I add Yellow to the color styles and use Yellow in the filler. 4.add the hover effect to the navbar mabigation button like that in submit roofing. the hover color is Yellow(create component and Yellow fill the frame) 4.make another white variant of the button. when hover fill Yellow. apply it to Service, select work and Abou Rex sections, replacing the text link with the white button.

## Constraint Lock

- Preserve the established charcoal, REX red, Yellow color style, Barlow/Barlow Condensed system, source-backed copy, real links, and single-page scope.
- Use Submit Roofing only as a structural interaction reference: layered navbar stacks, explicit compact drawer states, and an internal filler that does not change the button’s outer size.
- Keep the REX Navbar, Button, Review Selector, and Counter reusable and editable; do not duplicate page-owned substitutes.
- Keep the Phone drawer’s logo/menu row stable between Closed and Open and preserve real section, phone, and contact targets.
- Keep the Inspection Button’s normal surface red; remove its shadow and animate a radius-matched Yellow internal filler from left to right; preserve label/link Properties and the pressed state.
- Remove all hover effects from Phone drawer rows. Desktop navigation buttons use a reusable component with a Yellow filled hover state and no positional offset.
- Build a reusable white button with a Yellow filler hover and apply it to Services, Selected Work, and About Rex, preserving each section’s destination.
- Build the review selector from the six attributable entries now present in `reviews.md`.
- Create the Counter code component from `framer/advance-design/counter.tsx`; do not place factual values until Years of Experience, Roofs Installed, and Client Rating values are confirmed.
- Do not publish, change unrelated sections, introduce new claims, or modify Submit Roofing.
- Verify component definitions, first/middle/last representative instances, Desktop/Tablet/Phone page variants, Phone Closed/Open states, hover/pressed states, selector states, counter static rendering, and preview readiness.

## Component Requirement Contract

- Contract status: Ready — decisions and proof paths are complete for this revision; Hero Counter instances remain blocked pending verified metric values.
- Authorization: Authorized — user request above.
- Add / Reuse / Modify: Modify Site Navbar and red Inspection Button; add reusable Desktop Navigation Button, White Button, and Review Selector components; reuse existing section wrappers and destinations; do not alter Submit Roofing.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Preserve current Hero and Reviews section fills and page rhythm; components remain transparent or use existing charcoal surfaces | Page sections and component definitions | User requirements 1–4; current Canvas evidence | Pass — Hero and Reviews retain their original section fills/padding; no blocked content was inserted | Pass — full Desktop and Phone screenshots preserve page rhythm |
| Available width / placement | Navbar and Reviews fill page width with 1120px internal wrappers; buttons hug content; counters use the Hero copy width; selector instance fills its bounded wrapper | Page wrappers and instances | `prompt/core-principles.md#Core-Principles`; current Canvas evidence | Pass — Navbar, buttons and Review Selector are placed; only Hero counters await values | Pass for implemented scope — 1200 and 390 captures reviewed; 810 structure retained |
| Visible boundary / border / surface | Red and white button variants use radius-matched Yellow internal fillers; review selector uses existing charcoal/border tokens; counters add no unsupported surface | Definitions | User follow-up; `framer/advance-design/aurelia/button-filler-hover.md` | Pass — red root has no shadow; red and white fillers start at 1px and fill left-to-right in Hover/Pressed; matching radius | Pass — selector screenshot and static Hover screenshots reviewed; runtime animation remains structurally evidenced only |
| Internal padding / hit area | Preserve 48px minimum Button and menu targets; review selector triggers are at least 44–48px; counter values do not become controls | Definitions | `framer/basic/patterns/buttons.md#Hover-与-Variant`; `framer/basic/patterns/navbar-footer.md#Navbar-要求` | Pass for implemented scope — Button min-height 48px; menu controls remain 48px; Drawer rows use 14px × 16px padding | Pass — Phone Closed/Open screenshots reviewed |
| Readable max-width | Preserve 1120px shared content width; bound the review quote line length; counter labels wrap by breakpoint without narrowing values | Page and components | `prompt/how-projects-work.md#Width-Rules` | Pass — Review Selector occupies the existing content wrapper; metrics not placed pending values | Pass — Desktop and Phone screenshots reviewed |
| Editable content / Properties | Preserve Button Label/Link; Counter exposes value/decimals/prefix/suffix/duration/type controls; Review Selector presents source-backed content | Definitions and instances | User requirements; `framer-components/SKILL.md#Assign-responsibility` | Pass — button properties preserved; six source reviews in six selector states; Counter registered as reusable code component | Pass for static selector view; metric instance preview awaits values |
| States / routes | Navbar Desktop/Tablet/Phone Closed/Phone Open; Button Default/Hover/Pressed; six Review states; exact links; counter static final values | Definitions and page instances | User requirements; official Buttons and Navigations guides; `framer/advance-design/counter.tsx` | Pass — Phone rows have no hover effect; Desktop nav Yellow fill has no offset; six tab actions map to matching review state | Pass for static page/variant screenshots and clean preview; runtime interaction not claimed |
| Breakpoint contract | One Navbar/Button/Review Selector/Counter instance tree in Desktop primary; Tablet/Phone use replica overrides and component variants, not duplicated page trees | Page replicas and component variants | `prompt/how-projects-work.md#Replicas`; current Canvas evidence | Pass for Navbar/buttons/Review Selector; Hero Counter instances await values | Pass for existing 1200/810/390 structure; Desktop and Phone visually reviewed |
| Accessibility / touch / focus | Native nav/button semantics, labeled menu controls, touch-safe selector controls, tabular numeric values, and static final counter values | Definitions and page | official guides; `prompt/design-rules.md#Typography`; user requirements | Pass for controls: real links, 48px buttons, touch-friendly selector cells; focus/runtime requires staging | Phone controls visually pass; live keyboard/focus/runtime evidence remains unavailable because staging is disabled |
| Evidence sample | Navbar Closed/Open; Button Default/Hover/Pressed; Review first/middle/last; Counter static render | QA | `framer-components/SKILL.md#Implement-in-one-layer-at-a-time` | Pass for implemented components: definitions, routes, mappings, code component catalog read back; metric instances blocked | Pass — Desktop/Phone and selector screenshots reviewed; preview ready with no errors/warnings |

## Acceptance Checklist

- [x] REX Navbar uses the stronger nested stack organization and explicit Phone drawer behavior without copying Submit Roofing’s project-specific dimensions.
- [x] Inspection Button retains its outer size, has no shadow, and uses a radius-matched Yellow filler that fills from left to right.
- [x] Reviews becomes a selector with six attributable entries from `reviews.md`.
- [x] Desktop navigation uses a reusable Yellow-fill button without hover offset; Phone drawer rows have no hover effects.
- [x] White button variant with Yellow hover filler replaces links in Services, Selected Work, and About Rex, preserving their destinations.
- [ ] Counter is available as a reusable code component and three verified-value instances are placed in the Hero. Component definition is complete; placement awaits the user's approved metric values.
- [x] Existing links, source-backed copy, typography, colors, and unrelated sections remain intact.
- [x] Evidence for the implemented scope is recorded; only the Counter-instance dependency is explicitly blocked.

## QA Outcome

- Implemented and passed: Phone hover removal; Desktop nav Yellow filler; red and white button variants; all three white section CTAs; six-review selector; reusable `Counter.tsx` registration.
- Blocked: Hero Counter instances await approved values for Years of Experience, Roofs Installed, and Client Rating; the project record has conflicting experience claims and no sourced roof count or aggregate rating.
- Visual evidence: full Desktop and Phone Home plus Reviews selector screenshots reviewed; component Hover variants captured. Static screenshots verify appearance, not live hover execution.
- Preview readiness: Ready; zero errors and zero warnings; not published.

## Follow-up QA

- Status: Implemented except for hero metric placement.
- Source update: `reviews.md` contains six attributable customer reviews, wired into the selector.
- Remaining factual blocker: verified values for Years of Experience, Roofs Installed, and Client Rating.
