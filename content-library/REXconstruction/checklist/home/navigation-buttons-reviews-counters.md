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
- Verification status: Partial — Follow-up 8 now has live route and representative visual evidence; the broader Home scope still needs scoped runtime and breakpoint revalidation.

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

### Follow-up 8 — Review Selector Next Button

read the Review Selector and sync the statue to the repository.I make the Next button for the Review Selector. now replace all the button with this component and fix the links in the component

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

- Contract status: Partial — live structure, cyclic routes, and representative icon rendering pass; exhaustive runtime interaction remains unverified.
- Implementation status: Implemented — reused Next Button instances for all twelve arrow positions and removed the six local Previous Review frames.
- Verification status: Partial — all six state routes and CTA URLs read back correctly; representative previews confirm the left/right icon order, and a sample preview click advanced the first review. Exhaustive click/focus behavior across all states remains unverified.
- Authorization: Authorized — current user request.
- Add / Reuse / Modify: Reuse the existing Next Button; replace the six local Previous Review arrow frames with instances; repair all twelve arrow event targets; preserve the existing testimonial CTA link and all review content; do not change page sections, width owners, or unrelated components.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Preserve Review Selector card, attribution, and CTA; only replace arrow controls | Review Selector definition | Current Canvas readback; Follow-up 8 | Pass — old local Previous Review frames are absent; card and CTA structure remain | Pass — first, middle, last, and John variant screenshots show the preserved card and CTA |
| Available width / placement | Keep both arrow instances 44×44 in existing Review Arrows slots; do not change parent widths or max-width | Review Arrows and Next Button | Current Canvas readback; [Max-width ownership](../../../../framer/basic/standards/website-baseline.md#max-width-ownership) | Pass — arrow instances retain 44×44; this edit did not change parent widths | Partial — component screenshots reviewed; full page breakpoint review not performed |
| Visible boundary / border / surface | Reuse the existing Next Button’s normal and hover appearance; set Chevron Left for previous and retain Chevron Right for next | Next Button definition and instances | Current Canvas readback; Framer Buttons guide | Pass — left and right icons confirmed visually in first, middle, last, and John variant screenshots | Pass — the existing charcoal surfaces and square arrow boundaries remain intact |
| Internal padding / hit area | Preserve the component’s 44×44 button hit area | Next Button instances | Current Canvas readback; `framer/basic/patterns/buttons.md#Hover-与-Variant` | Pass — all six visible arrow pairs use 44×44 Next Button instances | Partial — component screenshots reviewed; full breakpoint review not performed |
| Readable max-width | N/A — no text or content width changes | None | Follow-up 8; current Canvas readback | N/A — no width constraint was introduced | N/A |
| Editable content / Properties | Use the exposed Icon property and `onClick` EventHandler; preserve the existing Read full review link | Next Button instances and CTA frames | Current Canvas readback; Framer Buttons guide; `framer/basic/patterns/buttons.md#Link-边界` | Pass — each review CTA still links to `https://rexconstructionllc.com/testimonials`; arrow EventHandlers remain present | Partial — preview captures generated; runtime destinations not exercised |
| States / routes | Previous/Next traverse the six reviews cyclically; preserve the Testimonials CTA destination | Next Button instances and Review Selector variants | Follow-up 8; current Canvas readback; `../../PROJECT.md#7-content-facts` | Pass — all six previous and six next targets form the expected cyclic sequence | Partial — first-to-second preview click worked; a complete six-state runtime cycle was not exercised |
| Breakpoint contract | Reuse the shared Review Selector definition in its existing page instances; do not add per-breakpoint copies | Review Selector definition and instances | Current Canvas readback; `framer/README.md#2-只选一个-primary-repo-skill` | Partial — the shared definition’s six variants were read back; page-instance breakpoints were not re-audited | Partial — representative variant captures generated; Desktop/Tablet/Phone captures not reviewed |
| Accessibility / touch / focus | Retain semantic button controls and 44×44 targets; keyboard/focus behavior is not assumed from structural readback | Next Button definition | Current Canvas readback; Framer Buttons guide | Partial — 44×44 button instances confirmed; focus behavior not tested | Partial — screenshots generated; pointer and keyboard paths not exercised |
| Evidence sample | Check first, middle, and last review states, with both arrow directions; keep the separate CTA | Review Selector and Next Button | Follow-up 8; current Canvas readback | Pass — all six state mappings and CTA URLs were read back | Pass — first, middle, and last plus John screenshots visually confirm icon direction; sample click confirmed state change |

## Acceptance Checklist

- [x] REX Navbar uses the stronger nested stack organization and explicit Phone drawer behavior without copying Submit Roofing’s project-specific dimensions.
- [ ] Inspection Button retains its outer size, no shadow and square corners; L:-1px hidden filler and 101% Relative Hover width need current targeted confirmation.
- [x] Reviews becomes a selector with six attributable entries from `reviews.md`.
- [x] Review Selector arrows reuse Next Button in both directions; all six previous/next routes and Testimonials CTA links were read back.
- [x] Desktop navigation uses a reusable Yellow-fill button without hover offset; Phone drawer rows have no hover effects.
- [ ] White appearance replaces section links, but consolidation inside the existing Button definition still lacks completion evidence.
- [ ] Existing Counter instances need approved numeric facts; their later reported values are unverified. Do not repeat the earlier instance-creation plan.
- [x] Existing links, source-backed copy, typography, colors, and unrelated sections remain intact.
- [ ] Close the remaining fact, component-consolidation and visual/runtime evidence gaps listed in [Current Status](../../PROJECT.md#12-current-status).

## QA Outcome

Current outcome: Partial for the broader Home revision. The 2026-10-14 live readback verifies the Review Selector’s six cyclic arrow routes, two visible shared Next Button instances per state, and six Testimonials CTA URLs. First, middle, last, and John screenshots confirm left/right icon order; a sample click advanced Alex Corbett to John Zare. Exhaustive six-state runtime/focus checks remain open. Other open items remain: unverified counter facts, White Button consolidation, stress-width evidence, and launch metadata. Earlier implementation and width results remain in the [dated U5 observations](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-u56-autoplay-and-review-cardlink-follow-up) and [width observation](../../../../history/workflow-observations/rexconstruction.md#2026-10-13-home-parent-width-correction).

The single [Current Status](../../PROJECT.md#12-current-status) owns blockers and the next approved action; [Recovery](../../PROJECT.md#14-recovery) owns re-entry. Original U5 evidence and wording remain in the [preserved snapshot](../../history/2026-10-13-before-width-closeout-repair.md).
