# Home — Navigation, Buttons, Reviews, and Counters Revision

> Reconciled 2026-10-13 from REX-2 and project observations; live Needs refresh. [Exact earlier contract](../../history/2026-10-13-before-width-closeout-repair.md) is preserved as history. Current owner: [Status](../../PROJECT.md#12-current-status). Dated Pass cells describe only their named historical checks.

- Page: Home
- Path: `/`
- Date: 2026-10-13
- Contract schema: 1
- Component contract: Required
- Component scope: Navbar, Inspection Button, Review Selector, and Counter responsibilities are in scope.
- Visual contract: N/A — targeted refinement under the existing passed Home visual direction.
- Authorization: Authorized — the current user request explicitly asks to implement all four items.
- Implementation status: Partial — later U5 follow-ups and width repair recorded; see PROJECT Current Status for remaining gaps.
- Verification status: Blocked — dated evidence is retained; later U5 changes and width removal require scoped visual/runtime revalidation.

## User Request — Verbatim

1.you can refer to the nabber in Submit Roofing, like the hover effect and the organization of the stacks, especially the Phone Drawer. 
2.Use a filling hover effect in the button component. You can also refer to the button in the submit roofing. The button is the current red and the filler is the brighter red.
3.The review section is so simple. Make a card selector for this section. The review details are in the reviews.md
4.	Make a counter component and put them in the hero section. The method is in the advanced-design. Three counters: Years of Experience, Roofs Installed and Client Rating

## User Request — Verbatim, Follow-up

1. remove the hover effect in the phone navbar. first, no hover in Phone. second, no offset in hover. 2.I forget to save the reviews.md and now it exist. 3. no shadow in the button component. the button has radius and the filler should also have it. I effect I want is the filler fill the button from the left to the right. I add Yellow to the color styles and use Yellow in the filler. 4.add the hover effect to the navbar mabigation button like that in submit roofing. the hover color is Yellow(create component and Yellow fill the frame) 4.make another white variant of the button. when hover fill Yellow. apply it to Service, select work and Abou Rex sections, replacing the text link with the white button.

## Later User Corrections — Verbatim

### Follow-up 3

1.update the project: no radius of all the cards and buttons. 2. I mean add a variant in the button component, not create another white button component.

### Follow-up 4

1.About the review section: I mean add a selector. but not the name list below. I mean there are two arrow beside the card and choose next. if the text of the review is too long, you should use '...' to 省略 some content and the complete content will be shown in the review seciton 2.add to the button filler design: the position of the initial filler should be L:-1 to hide the filler. and the width of the filler in the hover variant should be relative 101%. 3.make a text row component like submit roofing and apply it to the navbar in Phone

### Follow-up 5

1.remove all the radius in all images and frames in the page. 2.'Set the button’s hidden filler to `L: -1px` and the hover filler width to `101%`' add this to the repository 3.I want to make a image automatic switching effect and tell me how to use Framer native function to make this effect first.

### Follow-up 6

1.add the effect to the hero image and use autoplay. 2.about the review section: add the avatar and the 'read full review button should link to the review page but not unfold all the content. you should arrange the width of the card in the component because they overlay although they align well outside. Remove the read testimonials text link and replace with the read full review white button

### Follow-up 7 — Parent width

Do you forget the rule: Don't add max width to parent container? fix them in the whole website

## Constraint Lock

- Preserve the established charcoal, REX red, Yellow color style, Barlow/Barlow Condensed system, source-backed copy, real links, and single-page scope.
- Use Submit Roofing only as a structural interaction reference: layered navbar stacks, explicit compact drawer states, and an internal filler that does not change the button’s outer size.
- Keep the REX Navbar, Button, Review Selector, and Counter reusable and editable; do not duplicate page-owned substitutes.
- Keep the Phone drawer’s logo/menu row stable between Closed and Open and preserve real section, phone, and contact targets.
- Keep the Inspection Button’s normal surface red; remove its shadow and animate a square Yellow internal filler from left to right; preserve label/link Properties and the pressed state.
- Remove all hover effects from Phone drawer rows. Desktop navigation buttons use a reusable component with a Yellow filled hover state and no positional offset.
- Use a White variant inside the existing Button definition with a Yellow filler hover and apply it to Services, Selected Work, and About Rex, preserving each section’s destination.
- Use the six saved reviews with avatars, arrow controls and truncated excerpts; Read full review links to `/testimonials` instead of expanding the card. The dated implementation used 300px cards; revalidate component and page width together.
- Reuse the existing Counter definition and read back its existing instances; do not create duplicates from the stale placement plan. The reported numeric claims remain unverified and need approved facts.
- No max-width on structural parents; no bounded-shell exception is approved. Preserve existing responsive widths; any local reading cap requires its own justified owner.
- Later corrections: no radius on cards, buttons, images or frames; filler hidden at L:-1px and Hover width Relative 101%; Hero native slideshow autoplay requested.
- Do not publish, change unrelated sections, introduce new claims, or modify Submit Roofing.
- Verify component definitions, first/middle/last representative instances, Desktop/Tablet/Phone page variants, Phone Closed/Open states, hover/pressed states, selector states, counter static rendering, and preview readiness.

## Component Requirement Contract

- Contract status: Blocked — dated implementation evidence is partial; current proof limitations are explicit below.
- Implementation status: Partial — original work implemented; later corrections and unresolved dependencies are recorded in Current Status.
- Verification status: Blocked — no fresh Canvas verification in this repository reconciliation.
- Authorization: Authorized — user request above.
- Add / Reuse / Modify: Modify Site Navbar and red Inspection Button; reuse Desktop Navigation Button and Review Selector; consolidate White as a variant of the existing Button only after targeted readback; reuse existing section wrappers and destinations; do not alter Submit Roofing.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Preserve current Hero and Reviews section fills and page rhythm; components remain transparent or use existing charcoal surfaces | Page sections and component definitions | User requirements 1–4; current Canvas evidence | Blocked — prior record: Pass — Hero and Reviews retain their original section fills/padding; no blocked content was inserted; scope-specific completion evidence is incomplete or superseded. See [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). | Pass — full Desktop and Phone screenshots preserve page rhythm; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). Dated result only; later changes are not covered. |
| Available width / placement | Structural parents distribute available width with Fill / existing responsive width; max-width None. Local Button intrinsic sizing is separate; no approved bounded-shell exception. | Page root, structural wrappers, shared definitions, instances and breakpoint overrides | framer/basic/standards/website-baseline.md#max-width-ownership | Pass — dated 2026-10-13 global readback found zero remaining maxWidth after 27 caps were cleared; [width correction](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-home-parent-width-correction). Current live state Needs refresh. | Blocked — three breakpoint captures do not prove 320 / 1440+ stress widths or all runtime states after cap removal. |
| Visible boundary / border / surface | Red and White appearances must use square Yellow internal fillers in the same Button definition; review selector uses existing charcoal/border tokens; counters add no unsupported surface | Definitions | User follow-up; `framer/advance-design/aurelia/button-filler-hover.md#适用范围` | Pass — red root has no shadow; red and white fillers start at 1px and fill left-to-right in Hover/Pressed; matching radius; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). Dated result only; later changes are not covered. | Pass — selector screenshot and static Hover screenshots reviewed; runtime animation remains structurally evidenced only; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). Dated result only; later changes are not covered. |
| Internal padding / hit area | Preserve 48px minimum Button and menu targets; review selector triggers are at least 44–48px; counter values do not become controls | Definitions | `framer/basic/patterns/buttons.md#Hover-与-Variant`; `framer/basic/patterns/navbar-footer.md#2-navbar-要求` | Blocked — prior record: Pass for implemented scope — Button min-height 48px; menu controls remain 48px; Drawer rows use 14px × 16px padding; scope-specific completion evidence is incomplete or superseded. See [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). | Pass — Phone Closed/Open screenshots reviewed; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). Dated result only; later changes are not covered. |
| Readable max-width | Any future reading limit belongs to a specific text/local geometry owner; never restore a shared 1120px parent cap. No new local cap is approved by this reconciliation. | Local text or proven component geometry only | framer/basic/standards/website-baseline.md#max-width-ownership | Pass — dated scan recorded no remaining caps; [width correction](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-home-parent-width-correction). Future local limits require their own owner decision. | Blocked — local line lengths and wrapping need targeted narrow/wide visual evidence after the width repair. |
| Editable content / Properties | Preserve Button Label/Link; Counter exposes value/decimals/prefix/suffix/duration/type controls; Review Selector presents source-backed content | Definitions and instances | User requirements; `.agents/skills/framer-components/SKILL.md#assign-responsibility` | Pass — button properties preserved; six source reviews in six selector states; Counter registered as reusable code component; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). Dated result only; later changes are not covered. | Blocked — prior record: Pass for static selector view; metric instance preview awaits values; scope-specific completion evidence is incomplete or superseded. See [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). |
| States / routes | Navbar Desktop/Tablet/Phone Closed/Phone Open; Button Default/Hover/Pressed; six Review states; exact links; counter static final values | Definitions and page instances | User requirements; official Buttons and Navigations guides; `framer/advance-design/counter.tsx` | Pass — Phone rows have no hover effect; Desktop nav Yellow fill has no offset; six dated tab actions mapped to matching review state before the later arrow-selector correction; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). Dated result only; later changes are not covered. | Blocked — prior record: Pass for static page/variant screenshots and clean preview; runtime interaction not claimed; scope-specific completion evidence is incomplete or superseded. See [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). |
| Breakpoint contract | One Navbar/Button/Review Selector/Counter instance tree in Desktop primary; Tablet/Phone use replica overrides and component variants, not duplicated page trees | Page replicas and component variants | `.agents/skills/framer-layout-responsive/SKILL.md#transform-each-breakpoint`; current Canvas evidence | Blocked — prior record: Pass for Navbar/buttons/Review Selector; Hero Counter instances await values; scope-specific completion evidence is incomplete or superseded. See [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). | Blocked — prior record: Pass for existing 1200/810/390 structure; Desktop and Phone visually reviewed; scope-specific completion evidence is incomplete or superseded. See [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). |
| Accessibility / touch / focus | Native nav/button semantics, labeled menu controls, touch-safe selector controls, tabular numeric values, and static final counter values | Definitions and page | official guides; `framer/basic/standards/website-baseline.md#3-style-system`; user requirements | Blocked — prior record: Pass for controls: real links, 48px buttons, touch-friendly selector cells; focus/runtime requires staging; scope-specific completion evidence is incomplete or superseded. See [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). | Blocked — prior record: Phone controls visually pass; live keyboard/focus/runtime evidence remains unavailable because staging is disabled; scope-specific completion evidence is incomplete or superseded. See [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). |
| Evidence sample | Navbar Closed/Open; Button Default/Hover/Pressed; Review first/middle/last; Counter static render | QA | `.agents/skills/framer-components/SKILL.md#implement-in-one-layer-at-a-time` | Blocked — prior record: Pass for implemented components: definitions, routes, mappings, code component catalog read back; metric instances blocked; scope-specific completion evidence is incomplete or superseded. See [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). | Pass — Desktop/Phone and selector screenshots reviewed; preview ready with no errors/warnings; [dated record](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u52-phone-navigation-yellow-filler-and-review-source-follow-up). Dated result only; later changes are not covered. |

## Acceptance Checklist

- [x] REX Navbar uses the stronger nested stack organization and explicit Phone drawer behavior without copying Submit Roofing’s project-specific dimensions.
- [ ] Inspection Button retains its outer size, no shadow and square corners; L:-1px hidden filler and 101% Relative Hover width need current targeted confirmation.
- [x] Reviews becomes a selector with six attributable entries from `reviews.md`.
- [x] Desktop navigation uses a reusable Yellow-fill button without hover offset; Phone drawer rows have no hover effects.
- [ ] White appearance replaces section links, but consolidation inside the existing Button definition still lacks completion evidence.
- [ ] Existing Counter instances need approved numeric facts; their later reported values are unverified. Do not repeat the earlier instance-creation plan.
- [x] Existing links, source-backed copy, typography, colors, and unrelated sections remain intact.
- [ ] Close the remaining fact, component-consolidation and visual/runtime evidence gaps listed in [Current Status](../../PROJECT.md#12-current-status).

## QA Outcome

Current outcome: Partial. The [dated U5 observations](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u56-autoplay-and-review-cardlink-follow-up) record later autoplay, avatars, arrow controls, review links and card-width repairs. The [width observation](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-home-parent-width-correction) records 27 parent-cap removals and a global zero-remaining scan. Neither proves current Canvas truth, verified business metrics or all runtime states in this repository-only task.

The single [Current Status](../../PROJECT.md#12-current-status) owns blockers and the next approved action; [Recovery](../../PROJECT.md#14-recovery) owns re-entry. Original U5 evidence and wording remain in the [preserved snapshot](../../history/2026-10-13-before-width-closeout-repair.md).
