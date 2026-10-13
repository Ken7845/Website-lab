# Home — Design Plan and Checklist

- Page: Home
- Path: `/`
- Page status: Built — responsive Home is review-ready in Framer; publication is outside the authorized scope.
- Content status: Source-backed homepage summaries implemented; conflicting or unverified trust claims remain omitted.
- Primary CTA: Request a free roof inspection.
- Secondary CTA: Call (919) 946-8100.
- Contract schema: 1
- Component contract: Required — native Inspection Button, Site Navbar, Site Footer and Trust Bar definitions.
- Visual contract: Required — homepage redesign direction.
- Authorization: Authorized for planning — U1; dark theme and bright hover highlights directed by U2. Homepage implementation authorized by U3.
- Implementation status: Complete for the authorized homepage scope
- Verification status: Structural and visual Pass at 390 / 810 / 1200 for the revised shell, Trust Bar and Contact; live runtime click/focus and separate 320 / 1440 checks remain unavailable without staging.
- Source: [Project](../PROJECT.md#2-scope-and-authority), [source copy](../Info.md#verbatim-website-copy).

## Scope Lock

U1, user request: “Now plan to design the homepage. make a checklist and start the project.md.”

U3, user request: “start to build the homepage and I have created a project named REX Construction in the framer”

U2, user direction: “what color composition will you choose? I hope it will be a dark theme with bright highlight in the hover effect”

Plan the homepage using the official REX website and existing images. Preserve Info.md as the source transcription. The dark theme and bright hover effect are user-directed. New wording, exact palette values, final crops and layouts remain Draft proposals. U3 authorizes the responsive homepage and its necessary native dependencies. Publishing, other-page redesign, paid dependencies and custom code remain outside scope.

### Definition of Ready

- [x] Page goal, proposed narrative, conversion path and asset candidates documented.
- [x] Content conflicts and missing proof recorded in [PROJECT facts](../PROJECT.md#7-content-facts).
- [x] Confirm platform/project target and audit the existing page, shell and relevant components.
- [x] Complete one bounded review of candidate images and establish final crops.
- [x] Finalize copy and direction for the implementation scope.
- [x] Decide verified reviews, trust claims, address and subscription handling.

## Proposed Homepage Narrative

### 1. Navigation — Identity and immediate contact

Purpose: Recognize REX and find services, work, company information or contact quickly.

- Content: REX logo; existing Services, Our Work, About Us, Reviews and Contact destinations; office phone and inspection CTA.
- Composition: Compact header with an accessible menu when links no longer fit.
- [ ] Establish shared navigation ownership and Add / Reuse / Modify decision.
- [ ] Verify every route and `tel:+19199468100`; confirm responsive menu focus, close behavior and keyboard operation.
- [ ] Keep the logo readable and the inspection action prominent.

### 2. Hero — What REX offers and how to begin

Purpose: Connect the existing “Building Trust with Quality Work” promise to roofing/exterior services and the local area.

- Copy proposal: Preserve the original heading. Supporting copy may summarize roofing, exterior work and insurance restoration; mark it Draft until finalized.
- Image candidate: [Roofing crew at work](../images/project-photos/roofing-crew-at-work.webp).
- Composition: Text and CTA on the left, a large work photo on the right; copy/CTA precede the image on phone.
- Primary CTA: Free inspection → existing Contact route. Secondary CTA: Call office.
- [ ] Show one main h1, concise support copy, service location and clear next action.
- [ ] Keep workers, roofing activity and the house understandable at every crop.
- [ ] Avoid making payment, insurance coverage or project-time guarantees.

### 3. Trust Bar — Show supplied trust badges

Purpose: Give source-backed reasons to continue.

- Content: The five user-supplied trust badges with a restrained “Trusted connections” introduction.
- Composition: One native looping ticker with duplicated visual groups for continuity; duplicated images use empty Alt.
- [x] Use the supplied HomeAdvisor, GAF, Google Reviews, Wake Forest Chamber and NRCA badge assets.
- [x] Keep the badge bar compact and readable at Desktop, Tablet and Phone widths.
- [x] Avoid adding rating counts, metrics or new certification text beyond the supplied imagery.

### 4. Services — Make the offer clear

Purpose: Lead with roofing and show the scope of exterior work.

- Proposed hierarchy: Roof replacement, repairs and inspections → storm damage / insurance restoration → gutters and siding → windows and interior painting as supporting services.
- Composition: Editorial service rows with one-sentence summaries and clear links, rather than an automatic equal card grid.
- Next step: Existing Services page; inspection CTA beside roofing where useful.
- [ ] Confirm the service labels against official source wording.
- [ ] Distinguish assistance with an insurance process from any promise that a claim will be covered.
- [ ] Keep supporting services subordinate to the primary roofing offer.

### 5. Selected Work — Let real projects provide evidence

Purpose: Show residential and townhome roofing with the saved site imagery.

- Image candidates: [Townhomes](../images/project-photos/townhomes.webp) and [brick home with Rex](../images/project-photos/brick-home-yard-sign-rex.webp).
- Composition: A prominent work image with a second supporting image; captions below, stacked on phone.
- Next step: Existing Our Work route.
- [ ] Use neutral factual captions; do not invent project names, customer names, locations, dates, budgets or before/after results.
- [ ] Preserve rooflines and the meaningful subjects when cropping.
- [ ] Give each informative image context-specific alt text.
- [ ] Decide whether a lightbox adds value; a functioning gallery link is sufficient if enlargement is unnecessary.

### 6. Project Process — Reduce uncertainty

Purpose: Explain what happens before, during and after a job.

- Source stages: Pre-Construction, Construction, Post-Construction.
- Content: Documentation/scheduling → subcontractor coordination/quality control → cleanup/inspection/final walkthrough.
- Composition: A clear numbered sequence; vertical sequence on phone.
- [ ] Keep each stage brief and consistent with [the source process](../Info.md#services-and-service-area).
- [ ] Make reading order understandable without motion or hover.
- [ ] Add an inspection link after the process where it advances the enquiry.

### 7. Rex and Cleanup — Make the brand memorable

Purpose: Connect Rex's origin story to the emphasis on children, pets and yard cleanup.

- Image candidate: [Rex and Sophie](../images/project-photos/rex-and-sophie.webp).
- Composition: Smaller story image paired with a short text block, visually quieter than Hero and Work.
- Next step: Existing About Us route.
- [ ] Preserve the sourced Plott hound/Hurricane Florence story.
- [ ] Exclude the conflicting experience figure until reconciled.
- [ ] Confirm any current donation-program claim before using it.
- [ ] Retain both dogs in the image crop.

### 8. Reviews — Conditional evidence

Purpose: Present genuine, attributable customer feedback.

- Exact review text is Missing; review avatars and a Google badge do not establish a testimonial.
- [ ] Obtain exact source-linked review text and attribution before filling this section.
- [ ] Verify any rating/count close to publication.
- [ ] If content remains unavailable, agree how this slot and existing Reviews link will be handled in the final design.
- [ ] Prefer readable quotes to an auto-advancing carousel; keep review text accessible on touch and keyboard.

### 9. Final Contact Prompt — Complete the enquiry path

Purpose: End with a specific next action.

- Content: Free inspection offer, office phone, Nick's contact details if useful, and a link to Contact.
- Composition: A slightly lighter charcoal contact panel with a real REX project photo, prominent red inspection action and clear phone alternative.
- [x] Add a distinct project image with meaningful Alt and responsive crop.
- [ ] Verify Contact navigation, phone and email actions.
- [ ] Verify enquiry delivery and success/error behavior before introducing an inline form.
- [ ] Publish only confirmed address/hours; do not introduce a map or location schema using unresolved listing data.

### 10. Footer — Practical details and existing subscription

- Content: Logo, source-backed business contacts, useful page links, copyright owner/year once confirmed, existing subscription intent.
- [ ] Confirm subscription provider, delivery, consent text and error/success states before reproducing the sign-up UI.
- [ ] Keep the original subscription function as an explicit decision; do not silently remove it during the redesign.
- [ ] Check footer links, email and phone; ensure the small logo and text remain legible.

## Visual Direction Contract

- Contract status: Pass — implemented page matches the approved direction and bounded Desktop/Phone visual evidence.
- Authorization: Homepage build authorized by U3, using the U1 plan and U2 theme.
- Implementation status: Complete
- Verification status: Structural Pass; Visual Pass; runtime interaction proof Blocked because preview readiness returned no staging URL.

| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |
|---|---|---|---|---|---|
| Design Read | Local, approachable roofing business; explain work and lead to a free inspection | Home | [PROJECT goal](../PROJECT.md#4-website-goal), U1 | Pass — one ordered section tree and real CTA destinations | Pass — full Desktop/Phone review |
| Preserve | Existing REX logo, quality-work promise, real photography, free inspection/call intent and Rex story | Header / Hero / Story | [Info](../Info.md#business-profile), [brand story](../Info.md#brand-and-story-notes) | Pass — source copy/assets mapped to live nodes | Pass — identity and image subjects remain clear |
| Transform | Build a clear service → work → process → contact narrative; concise source-backed summaries used for the build; exact transcription remains in Info.md | Home | [Narrative](../PROJECT.md#9-narrative-and-conversion) | Planned: one canonical section tree | Planned: hierarchy and section rhythm |
| Avoid | Unverified badges, fabricated reviews/statistics, insurance guarantees, repeated card grids and decorative motion | Home | [Facts](../PROJECT.md#7-content-facts), U1 | Planned: claim and component audit | Planned: content-led layout review |
| Sibling-page delta | Home summarizes; Services, Work and About remain detail destinations; shared utilities repeat intentionally | Home / shell | [Sitemap](../PROJECT.md#8-sitemap-and-page-goals) | Planned: destination map; no sibling redesign | Planned: role distinction after current-site audit |
| Section composition | Split Hero; service rows; selected-work pair; numbered process; quieter story; contact close | Home sections | [Narrative](#proposed-homepage-narrative) | Pass — targeted section/read-order readback | Pass — full-page rhythm and crops reviewed |
| Colour rhythm | Charcoal canvas/surfaces, off-white text, red actions and coral hover/focus; natural-color photography | Page styles | U2, [palette](../PROJECT.md#color-palette), [hover treatment](../PROJECT.md#hover-treatment) | Pass — eight semantic color tokens and gesture variants | Pass — dark/light-surface rhythm reviewed; runtime focus Blocked |
| Asset map | Five reviewed assets: logo → Header/Footer; crew → Hero; townhomes + brick home → Work; Rex and Sophie → Story | Section media | [Asset ledger](../PROJECT.md#asset-usage-ledger) | Pass — all five uploaded with Alt and assigned | Pass — candidate sheet and rendered crops reviewed |
| Responsive transformation | Desktop 1200, Tablet 810, Phone 390; split layouts become vertical and Phone retains visible core navigation | Page breakpoints | [Responsive plan](../PROJECT.md#11-responsive-interaction-and-assets) | Pass — three breakpoints and overrides read back | Pass at 390 / 1200; 810 structural Pass; 320 / 1440 separate visual evidence Blocked |
| Completion evidence | Source-correct content, functioning enquiry paths, readable responsive page and maintainable editing | Home | [Page Done](#page-done) | Pass — metadata, headings, targets, protocol links and button Properties read back | Pass — bounded full Desktop/Phone review; runtime interaction proof Blocked |


## Component Requirement Contract

- Contract status: Pass — Inspection Button, Site Navbar, Site Footer and Trust Bar are native components.
- Authorization: U3
- Add / Reuse / Modify: Add definitions and styles because live reusable-system list is empty; Modify blank Desktop; Reuse Home.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Canvas and alternating Surface; section padding 88px desktop / 56px phone | Page sections | U2; PROJECT.md#color-palette | Section fill/padding readback | Desktop/Phone screenshots |
| Available width / placement | Centered maxWidth 1120px; full-bleed bands; Button intrinsic width | Page wrapper and instances | prompt/core-principles.md#Core-Principles | Width chain and instance readback | Desktop/Phone screenshots |
| Visible boundary / border / surface | Button red normal, coral hover/pressed; Nav charcoal; 4px radius | Definitions | U2; PROJECT.md#hover-treatment | Normal/gesture variant attributes | Button states and header preview |
| Internal padding / hit area | Button 16px 24px; minimum 48px; menu trigger 48px | Definitions | framer/basic/patterns/buttons.md | Definition and instance rect | Phone touch controls |
| Readable max-width | 1120px sections; Hero text half column; body readable 18px | Page | prompt/how-projects-work.md#Width-Rules | Text widths and style presets | Responsive wraps |
| Editable content / Properties | Button Label string and Link; navigation native text/logo; static sections | Definitions and native page nodes | prompt/how-projects-work.md#Components | Controls lookup / text nodes | Representative instances |
| States / routes | Button Default / Hover / Pressed; visible Header links at all breakpoints; official Contact, `tel:` and `mailto:` targets | Definition and page targets | prompt/how-projects-work.md#Links | Pass — variants and href targets read back | Desktop/Phone rendering Pass; runtime hover/focus Blocked |
| Breakpoint contract | Shared primary page tree with Tablet and Phone replicas; Header reflows to stacked visible navigation on Phone | Page overrides | prompt/how-projects-work.md#Replicas | Pass — breakpoint and compound override readback | Pass — Desktop/Phone rendering |
| Accessibility / touch / focus | Meaningful headings, image alt, minimum 48px targets; native link focus; no entrance motion; focus runtime proof pending | Definitions and page | U2; prompt/design-rules.md#Typography | Tags/alt/rect and links | Keyboard runtime where available |
| Evidence sample | Button first Header, middle Hero, last Contact; Nav normal and Phone Open | QA | Current blank Canvas; framer-components skill#Implement-in-one-layer-at-a-time | Definition / instances / overrides | Bounded canvas and runtime preview |

## Styles, Components and Semantics

- [x] Propose dark color roles and contrast-checked CTA states in [PROJECT](../PROJECT.md#color-palette).
- [x] Implement text/color styles and interaction states using those roles after the current-site audit.
- [x] Use one h1, meaningful h2 section headings and h3 only for subordinate service/process content.
- [x] Name sections/layers by purpose: Home / Hero / Services / Work / Process / RexStory / Contact.
- [x] Use shared Site Navbar and Site Footer components; preserve the Inspection Button Properties and gesture Variants.
- [x] Check page instances after editing component definitions.
- [x] Use static content for this first homepage unless actual editing needs justify CMS.
- [x] Keep exact source transcription in Info.md; use concise source-backed summaries on Home.

## Images, Responsive Behavior and Accessibility

Image Review Plan for the next design step: one contact sheet with exactly five candidates from the PROJECT ledger. Questions: Is the logo readable? Does the crew image clearly show roofing work? Do the townhome rooflines remain useful? Does the brick-home image communicate residential work? Does the dog photo support the Rex story? Maximum two attempts; if unavailable, record visual allocation as Blocked and continue independent structure/copy planning.

- [x] Confirm residency, dimensions and decoding before visual review; record the checkpoint in [Recovery](../PROJECT.md#14-recovery).
- [x] Confirm all crops at their actual containers and review the rendered Desktop/Phone result.
- [x] Define informative Alt for every uploaded image.
- [ ] Assign width ownership; avoid horizontal overflow at 320/390/810/1200/1440+ px.
- [x] Keep headings, body text, buttons, logo and key image subjects readable.
- [ ] Use keyboard access, visible focus, adequate contrast and touch targets.
- [x] Verify menu Closed/Open structure, exact state actions and 48px controls; live keyboard execution remains unavailable without staging.
- [x] Respect reduced motion; essential information and links remain usable without animations.
- [x] Apply bright coral hover highlights to navigation, primary CTA and service-row accents; primary CTA label becomes charcoal on coral.
- [ ] Keep decorative dividers distinct from required control boundaries; verify contrast on actual normal/hover/focus backgrounds.
- [ ] Verify the highlight on keyboard focus and useful pressed feedback on touch; do not make touch access depend on hover.

## Metadata, Performance and Editing

- [x] Draft and apply Page Title and Meta Description using confirmed service/location facts.
- [ ] Assign favicon and Open Graph image; verify social preview crop.
- [ ] Confirm canonical URL and structured business facts when the publishing target is known.
- [ ] Optimize Hero delivery and lower-page image loading; avoid unnecessary scripts/dependencies.
- [x] Resolve implementation diagnostics and run Framer preview readiness; result `ready` with no errors or warnings.
- [ ] Document how to edit copy, images, links and any connected form/subscription.
- [ ] Check long copy and alternate image proportions for maintainability.
- Marketplace buyer-replacement tests: N/A — a client business redesign, not a marketplace template.

## Targeted Preview Paths

When implementation is authorized:

- [ ] 320 / 390 px: Menu → Services → Work → inspection CTA; no overflow or unreadable crop.
- [ ] 810 px: Header fit, Hero reflow and service/process reading order.
- [ ] 1200 / 1440+ px: Whole-page hierarchy, image balance, line length and section rhythm.
- [ ] Keyboard: Header navigation → primary CTA → content links → footer; visible focus and sensible order.
- [ ] Real enquiry/call/email path; verify submission delivery if a new form is introduced.
- [ ] Subscription success/error path if enabled; reduced-motion behavior; optional lightbox.

## Page Done

- [ ] Final direction and content ready within the authorized build scope.
- [ ] Applicable contracts and shared component responsibilities complete.
- [ ] Every included section serves the enquiry path and uses source-backed facts.
- [ ] Applicable structure, visual and runtime checks pass at the recorded widths/states.
- [ ] Relevant page evaluator/preflight completed through the implementation router.
- [ ] PROJECT status and this page's result synchronized; Recovery updated in its canonical owner.
- [ ] Remaining limitations explicitly recorded; no unverified slot presented as completed.

## Latest Part Result

- Part: Navigation, Buttons, Reviews, and Counters revision
- Date: 2026-10-13
- Result: Partial — Phone row hover removed; Yellow-fill nav/red/white button variants and three section CTAs implemented; six-review selector built; reusable Counter definition exists; Hero instances await exact metric values.
- Structural status: Pass for implemented scope — nav/button states, links and six review mappings read back; only counter instances are blocked pending values.
- Visual status: Pass for implemented scope — nav, button and review-selector states plus full Home reviewed at Desktop/Phone; Tablet structurally retained. Separate 320 / 1440 evidence is Blocked.
- Verified widths: 390 visual; 810 structural; 1200 structural and visual. Phone breakpoint covers widths below 810; Desktop covers widths at and above 1200.
- Verified runtime paths: Framer preview readiness Pass; live hover/focus/click execution Blocked because staging is disabled and no preview URL was returned.
- Shared components changed: Site Navbar Phone row effects and Desktop Navigation Button; red Inspection Button and White Button with Yellow fillers; Review Selector; reusable Counter code component added but not instantiated.
- Canonical Recovery: [PROJECT §14](../PROJECT.md#14-recovery)

## Build Decisions

- Hero: preserve original heading; summarize roofing/exterior work and five sourced service areas.
- Reviews: use existing official testimonials link; no fabricated quote or rating.
- Subscription: link to existing official subscription on source homepage; no disconnected signup field.
- No inline form: inspection goes to original Contact page; phone/email routes remain direct.
- Trust badges are displayed because the user explicitly requested the supplied assets; no new rating, metric or certification wording was added. Experience metric, weekly hours and map remain omitted while conflicts remain.
- Fonts: Barlow Condensed 700 headings and Barlow 400/600 body/labels, resolved through exact font search. Style-driven search returned Framer AI credit exhaustion; exact font results remain usable.
- Image review: one five-image contact sheet decoded successfully; full crew frame preserves workers and Rex; both dogs retained in story.
