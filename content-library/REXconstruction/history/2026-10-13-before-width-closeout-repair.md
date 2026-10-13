# REX records before width and closeout reconciliation

Retired source snapshot, preserved 2026-10-13. These exact records describe older states and include the conflicting 1120px contracts; they do not govern current work. Source-relative links are intentionally unchanged. Each fenced payload preserves the source bytes.

## PROJECT.md

SHA-256: `bb6da14537929443af8ceb1ce19fb56667d4afccd24faacbf474b84f66a3a77d`

````markdown
# REX Construction LLC — Project

- State schema: 1
- Current status owner: [Inline Status](#12-current-status)
- Recovery owner: [Inline Recovery](#14-recovery)

## 1. Project Identity

- Project name: REX Construction LLC website redesign
- Platform: Framer — confirmed by the user.
- Project type: Business website / roofing and exterior construction
- Overall status: Built — Home is review-ready in Framer; not published.
- Production website: https://rexconstructionllc.com/
- Project / Canvas URL: https://framer.com/projects/REX-Construction--sTWVLfrpuNKD6x8u6CXh-cSBqA
- Preview URL: Missing
- Content status: Source-backed homepage summaries implemented; conflicting or unverified facts remain omitted.
- Last updated: 2026-10-13
- Last verified against current implementation: navigation/buttons and six-state Review Selector read back; Counter code component registered; Desktop/Phone screenshots reviewed; preview readiness passed without warnings on 2026-10-13. Hero counter instances await exact metric values.

## 2. Scope and Authority

- Authorized request U1: “Now plan to design the homepage. make a checklist and start the project.md.”
- Authorized request U3: “start to build the homepage and I have created a project named REX Construction in the framer”
- Direction U2: “what color composition will you choose? I hope it will be a dark theme with bright highlight in the hover effect”
- Authorized request U4: “1.improve and revise the navbar and footer refer to the repository, especially the 'component' and 'response' issue 2. revise the Confidence part and turn it into a trust bar. use the images in the trust badges folder and apply a ticker effect. 3. input an image in the contact section to make this section better”
- Current scope: Maintain the responsive homepage in the user-created Framer project, including the U5 Navbar/Button refinements and the data-dependent Review Selector and Hero Counters.
- Primary page: Home, path `/`.
- Authority: User instruction → official REX website → [Info.md](Info.md#verbatim-website-copy). Maps and other listings are supplementary.
- Add / Reuse / Modify: Add PROJECT and homepage checklist because no equivalent owners exist; reuse the current Info file and categorized image library.
- Confirmed direction: Website redesign using REX's existing business information and saved imagery; dark theme with bright hover highlights, per U2.
- Proposed direction: A clear, local, approachable roofing homepage with charcoal surfaces, REX red actions and bright coral hover/focus highlights, focused on free inspection enquiries. Detailed direction lives in [the homepage contract](checklist/home.md#visual-direction-contract).
- Scope boundary: Homepage implementation and its necessary native styles/components are authorized. Other-page redesign, publication, custom code and paid dependencies are outside scope.
- Current implementation differences: Home now uses Barlow Condensed/Barlow, a charcoal/red/coral system, editorial service rows, three responsive breakpoints and direct official-site/protocol links. Other source-site pages remain outside scope.

## 3. Knowledge Map

| Responsibility | Current source | Status |
|---|---|---|
| Source copy and factual notes | [Info.md](Info.md#business-profile) and [verbatim copy](Info.md#verbatim-website-copy) | Approved source; unresolved claims flagged |
| Brand and visual direction | [Home visual contract](checklist/home.md#visual-direction-contract) | Pass |
| Homepage structure and acceptance criteria | [Home checklist](checklist/home.md) | Built; current revision recorded |
| Assets | [Branding](images/branding/), [project photos](images/project-photos/), [trust badges](images/trust-badges/), [review avatars](images/review-avatars/) | Available; usage candidates below |
| Current status / recovery | [Status](#12-current-status) / [Recovery](#14-recovery) | Current owners |
| Decisions | [Inline decisions](#13-decisions-and-exceptions) | Active decisions synchronized |
| Checklist index | [Checklist README](checklist/README.md) | Active |
| History | [Workflow observations](../../history/workflow-observations/rexconstruction.md) | Active |

## 4. Website Goal

Help a homeowner understand what REX does, where it works, how a roofing project is handled, and how to request a free inspection.

- Primary CTA: Free inspection enquiry, initially directed to the existing official Contact page.
- Secondary CTA: Call the office at (919) 946-8100.
- Success evidence for design: Visitors can identify the service, local coverage, next step and phone number without searching.
- Measurement proposal: Contact CTA clicks, phone clicks and completed enquiries; tracking and enquiry delivery remain to be configured and verified.

## 5. Target User

- Primary audience: Homeowners in Raleigh, Wake Forest, Clayton, Cary and Garner.
- Secondary audience: Townhome / HOA decision makers, supported by the official gallery copy.
- Main questions: Do you handle my roofing or exterior problem? Can you explain storm damage and the insurance process? What happens during the job? How do I contact you?
- Device priority: Balanced; prioritize simple mobile enquiry and call paths.
- Trust needs: Real work photos, clear process, accurate contact information and attributable reviews.

## 6. Brand Direction

User-directed theme: Dark throughout, with bright highlights on hover. Preserve the red, white and gray REX logo, the quality-work promise, local service focus and Rex's story. Use strong readable typography, generous spacing, straightforward service language and real project photography. Alternate charcoal canvas and slightly lighter surfaces to create section depth.

The homepage should move from offer to evidence to contact. Use different compositions for services, work, process and story rather than repeating the same card grid. Font family, spacing and final crops remain design tasks in [the checklist](checklist/home.md#visual-direction-contract).

### Color Palette

The following tokens are the proposed implementation palette, supporting the existing logo rather than representing a supplied brand standard.

| Role | Color | Use |
|---|---|---|
| Canvas | `#101214` | Hero, Work, footer and base page |
| Surface | `#1A1E23` | Services/process bands and contact panel |
| Raised surface | `#242A31` | Interactive service rows and secondary hover surfaces |
| Main text | `#F5F5F7` | Headings, body copy and normal primary-button labels |
| Muted text | `#B8BEC7` | Supporting text and captions |
| Primary action | `#D7263D` | Normal primary-button fill; logo-associated red emphasis |
| Hover / focus highlight | `#FF5A66` | Primary hover fill, links, arrows and focus outlines |
| Decorative divider | `#3B444F` | Quiet separators; not a required form/control boundary |
| Control boundary | `#707B88` | Form/control outlines where the boundary conveys necessary information |

Most area remains dark neutral; red highlights identify actions. Photographs keep their natural colors. Main text and muted text retain contrast against their actual surfaces.

### Hover Treatment

- Primary CTA: red fill with off-white text normally; coral fill with charcoal text on hover/focus, plus a restrained coral shadow.
- Navigation links: coral text/underline on hover and a visible keyboard-focus outline.
- Service rows: lighter charcoal surface and a coral arrow/leading rule; preserve readable body text.
- Timing proposal: 180 ms for color and shadow transitions. Reduced motion removes transitions. Essential actions remain visible on touch; a hover effect is never required to reveal information.
- Calculated solid-color contrast: main text/canvas 17.24:1; muted text/surface 8.95:1; normal CTA text/red 4.56:1; hover CTA charcoal/coral 6.17:1. These verify color pairs, not a completed page or all runtime states.

## 7. Content Facts

| Fact | Value / handling | Source | Status |
|---|---|---|---|
| Main phone | (919) 946-8100; use `tel:+19199468100` | [Info](Info.md#business-profile) | Approved source |
| Contact | Nick; (919) 946-8200; Nick@rexconstructionllc.com | [Info](Info.md#business-profile) | Approved source |
| Address | Official site: 1111 Consortium Drive, Unit 113, Raleigh, NC 27603; listing differs | [Conflict notes](Info.md#listing-cross-check-and-unresolved-address) | Draft — confirm before a map / location schema |
| Service area | Raleigh, Wake Forest, Clayton, Cary and Garner | [Info](Info.md#services-and-service-area) | Approved source |
| Inspection offer | Free roof inspection | [Info](Info.md#business-profile) | Approved source |
| Weekly hours | Site shows “Open today” 7 a.m.–7 p.m.; weekly schedule unconfirmed | [Info](Info.md#business-profile) | Missing |
| Experience figure | 18 combined years / thousands on Home; 10 years / hundreds on About | [Conflict notes](Info.md#brand-and-story-notes) | Missing — reconcile before use |
| License | Website claims #8744; current official registry status unverified | [Info](Info.md#business-profile) | Draft — source claim only |
| Reviews | Six attributable exact customer quotes saved and wired into the Home selector; aggregate rating/count unavailable | [reviews.md](reviews.md) | Quotes available; aggregate rating Missing |
| Affiliations / certifications | Five saved badge images are displayed in the Trust Bar at the user's explicit direction; no additional status or rating claim was added | [Info](Info.md#image-library), U4 | User-directed display; current status not independently reverified |
| Donation program | Site describes a yearly donation intention | [Info](Info.md#brand-and-story-notes) | Draft — confirm ongoing practice |
| Social links / warranties / pricing | No confirmed values supplied | [Info](Info.md#business-profile) | Missing |

## 8. Sitemap and Page Goals

Only Home is in the current design scope. Existing routes are recorded as destination references, not new page build tasks.

| Page | Existing path | Role | Current redesign status |
|---|---|---|---|
| Home | `/` | Introduce services and lead to a free inspection | Built — review-ready, not published |
| Services | `/services` | Explain services and project stages | Reference only |
| Our Work | `/gallery` | Show residential and townhome work | Reference only |
| About Us | `/about-us` | Company story | Reference only |
| Reviews | `/testimonials` | Customer feedback | Reference only; exact review text Missing |
| Contact Us | `/contact-us` | Inspection enquiry and contact information | Existing CTA destination; runtime verification needed |

## 9. Narrative and Conversion

| Home section | Purpose | Source / media | Next step |
|---|---|---|---|
| Navigation | Orient and provide immediate contact | Logo; existing page routes; office phone | Free inspection / phone |
| Hero | Explain the offer and local service | Existing quality-work heading; roofing crew image candidate | Contact page / call |
| Confidence statement | Explain communication, documentation and cleanup | Official service/process copy; badge use conditional | Continue to services |
| Services | Show roofing as the primary offer and exterior work as supporting services | Services and Contact copy; editorial service list | Services page |
| Selected work | Show actual roofs and homes | Townhomes and finished-home photo candidates; factual captions only | Our Work |
| Project process | Reduce uncertainty before, during and after the job | Pre-Construction → Construction → Post-Construction | Free inspection |
| Rex and cleanup | Give the business a recognizable human story | Official Rex story; Rex and Sophie image candidate | About Us |
| Customer reviews | Provide attributed evidence using the six saved exact reviews and selector | [reviews.md](reviews.md) | Reviews selector |
| Final contact prompt | Give one clear next action | Main phone, inspection offer and Contact route | Contact page / call |
| Footer | Business identity and useful destinations | Official contacts; subscription handling to confirm | Phone / email / pages / subscription |

Primary path: Understand services → see work and process → request an inspection or call.

Reviews are conditional on verified content. The existing subscription function is recorded for preservation; connection details are Missing. No enquiry form success state should be presented without a working submission destination.

### Page Visual Identity

| Page | Visual memory point | Composition | Color rhythm | Sibling difference | Status |
|---|---|---|---|---|---|
| Home | REX logo, real roofing work and Rex's story | Split hero, service rows, selected work, process sequence, story and contact close | Charcoal canvas and surfaces; off-white text; red actions; Yellow interactive fills | Homepage gives an overview; detailed source pages retain their separate purpose | Implemented |

## 10. System and Platform Plan

- Planning skill: repository [design-taste](../../.agents/skills/design-taste/SKILL.md).
- Implementation route: official Framer connection → generated task map → repository `framer-components` → `framer-qa`.
- Implemented shared elements: Inspection Button with Label/Link Properties, no shadow, and Yellow filler gesture states; Yellow-fill Desktop Navigation Button; White Button with Yellow filler; six-state Review Selector; reusable `Counter.tsx`; Site Navbar with Desktop, Tablet, Phone and Phone Open variants; Site Footer and Trust Bar.
- Component and visual contracts are recorded in [Home](checklist/home.md).
- CMS: Not required for the proposed static homepage; decide later if work/reviews need an editorial collection.
- Forms / newsletter: Connection and owner Missing. Keep existing working destinations until replacements are verified.
- Custom Code / paid dependencies: Not proposed.

## 11. Responsive, Interaction and Assets

| Area | Desktop | Tablet | Phone |
|---|---|---|---|
| Navigation | Logo, route links, office phone and contact CTA | Reduced spacing; office number hidden | Compact sticky bar with labeled 48px menu control and explicit Closed/Open drawer states |
| Hero | Copy and roofing photo side by side | Balanced columns if content fits | Copy, CTA, then image; independent crop |
| Services / process | Editorial rows / numbered sequence | Fewer columns | Vertical reading order |
| Selected work | Two images with differing emphasis | Two or one columns according to readable width | Stack with captions |
| Story / contact | Image-text story; Contact uses a project image beside copy/actions | Contact stacks the image, copy and actions | Vertical image, copy and large touch targets |

- Verification widths proposed: 320, 390, 810, 1200 and 1440+ px.
- Motion: Subtle optional entry feedback; meaningful focus/pressed states; reduced-motion alternative.
- Web assets: [images/](images/). Current inventory contains 34 named assets; the flyer is currently JPG. This planning task does not alter formats.
- Licensing: User-supplied source-site assets; confirm delivery/republication rights before launch.
- Full-page Desktop and Phone visual evidence: Pass. Tablet: structural Pass. Live runtime link/hover/focus checks: Blocked because preview readiness supplied no staging URL.

### Asset Usage Ledger

The approved homepage assets below are implemented in the redesigned Home.

| Asset | Narrative qualities | Approved role | Current use | Reuse decision / reason | Crop / focal notes | Status |
|---|---|---|---|---|---|---|
| [REX logo](images/branding/rex-logo.webp) | Existing identity | Existing brand asset | Header and Footer | Repeated for identity | Full logo remains readable | Used |
| [Roofing crew](images/project-photos/roofing-crew-at-work.webp) | Workers, materials, home and Rex | Hero | Hero principal image | One principal Home use | Roof work, people and Rex remain legible | Used |
| [Townhomes](images/project-photos/townhomes.webp) | Multi-family roofing scene | Selected Work | First work figure | Supports the source's townhome service story | Rooflines retained | Used |
| [Brick home and Rex](images/project-photos/brick-home-yard-sign-rex.webp) | House, roof, yard sign and Rex | Selected Work | Second work figure | Complements townhome image | Roof and Rex remain visible | Used |
| [Rex and Sophie](images/project-photos/rex-and-sophie.webp) | Named dogs in the source story | Rex Story | Story image | One supporting story use | Both dogs remain visible | Used |
| [Home with roof sign](images/project-photos/home-with-roof-sign.webp) | Finished home, REX sign and Rex | Contact | Contact project image | Distinct from Hero and supports the enquiry close | Home, sign and Rex remain visible | Used |
| [Trust badges](images/trust-badges/) | Five supplied platform/association marks | Trust Bar | Native ticker with one duplicate visual group | User explicitly requested these assets | Full marks remain legible; duplicate group has empty Alt | Used |

## 12. Current Status

- State revision: 2026-10-13-08
- Active request: [U5 — Navigation, Buttons, Reviews, and Counters revision](checklist/home/navigation-buttons-reviews-counters.md)
- Evidence basis: Framer component/variant readback, six review mappings, code-component catalog, component and full Desktop/Phone screenshots, and clean preview readiness.
- Current phase: Partial — Navbar, button variants, and Review Selector implemented; Counter definition exists; Hero metric instances await approved values.
- Active page: Home
- Open dependencies: Exact Years of Experience, Roofs Installed, and Client Rating values; favicon/Open Graph asset; runtime hover/focus/click evidence; separate 320 / 1440 visual evidence.
- Next approved step: User supplies exact metric values; place the three Hero counters and complete responsive QA. Publication remains a separate explicit request.
- Last verified: 2026-10-13 — components, selector mappings and links read back; Desktop/Phone visual review completed; preview readiness passed without errors or warnings; not published.

| Page | Plan | Content | Styles | Components | Links/runtime | SEO | Alt | Desktop | Tablet | Phone | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Home | Partial — Hero metric values needed | Source-backed summaries and six reviews; exact metrics Missing | Pass | Partial — Navbar/buttons/review selector Pass; counter instances pending | State routes structurally Pass; live runtime proof unavailable | Pass | Pass | Pass | Pass — structural | Pass for implemented scope | Definition/variant/code-catalog readback + component/full-page screenshots + clean preview readiness |

## 13. Decisions and Exceptions

| Decision | Reason | Scope | Status | Date |
|---|---|---|---|---|
| Official REX website is the source of truth | User instruction | Facts and source copy | Active | 2026-10-13 |
| Preserve exact extracted text in Info.md | User instruction | Source record | Active | 2026-10-13 |
| Create homepage plan/checklist and project entry | U1 | Repository planning | Active | 2026-10-13 |
| Build Home in the supplied REX Construction Framer project | U3 and supplied editor URL | Homepage implementation | Active | 2026-10-13 |
| Dark theme with bright hover highlights | U2 | Homepage visual direction | Active | 2026-10-13 |
| Convert Navbar/Footer to responsive components; add Trust Bar ticker and Contact image | U4 | Homepage shared shell, trust evidence and enquiry close | Implemented | 2026-10-13 |
| Refine Phone hover, add Yellow-fill navigation/buttons, review selector, and Hero counters from verified data | U5 | Navbar, buttons, Reviews and Hero metrics | Partial — only Hero metric values pending | 2026-10-13 |

Dark theme and bright hover highlights are user-directed. Exact palette tokens, final wording, crops and section composition remain proposals in the checklist.

## 14. Recovery

- State revision: 2026-10-13-08
- Active request: [U5 — Navigation, Buttons, Reviews, and Counters revision](checklist/home/navigation-buttons-reviews-counters.md)
- State reference: [Current Status](#12-current-status)
- Active connection: Official Framer Agent session 2 connected; generated task map and live revised Home readback complete.
- Current page: Home
- Last successful change: Removed Phone row hover; created Yellow-fill navigation, red and white buttons; applied white buttons to Services, Selected Work and About Rex; built a six-state review selector; retained Counter code component. Preview readiness clean.
- Last targeted readback: Button/nav/review states, CTA destinations, selector mappings and component catalog; Desktop/Phone visuals and preview readiness; 2026-10-13.
- Verified breakpoints / states: Desktop 1200 and Phone 390 visually reviewed; Tablet 810 structurally verified; Navbar Phone Closed/Open visually and structurally verified.
- Remaining approved work: Place three Hero counters after exact metric values are supplied, then finish responsive QA. Runtime interaction proof, favicon/Open Graph and publication remain separate limitations or follow-ups.
- Exact next action: Obtain the three exact metric values from the user.
- Important asset paths: [Asset ledger](#asset-usage-ledger)
- Visual review checkpoint: Phone Closed/Open, component fill variants, review selector, and full Desktop/Phone pages reviewed; implemented scope passed without layout regressions.
- Updated at: 2026-10-13

## 15. Checklist and Change Control

- Index: [Checklist README](checklist/README.md)
- Canonical page owner: [Home](checklist/home.md)
- Request checklist: [U5 Navigation, Buttons, Reviews, and Counters revision](checklist/home/navigation-buttons-reviews-counters.md) — implemented except Hero metric placement.
- Checklist status: Partial — implemented scope QA complete; Hero Counter instances await exact metric values.
- Last synchronized: 2026-10-13, revision 2026-10-13-08.

## 16. History

See [REX Construction workflow observations](../../history/workflow-observations/rexconstruction.md).

## 17. Definition of Ready

- [x] Authorized planning scope and source authority recorded.
- [x] Page goal, audience, CTA and narrative proposed.
- [x] Source content, asset candidates and missing facts recorded.
- [x] Canonical homepage checklist created.
- [x] Final copy and visual direction ready for implementation.
- [x] Platform and project target identified.
- [x] Current page/shared structures audited before creating or replacing them.
- [x] Relevant content gaps resolved or explicitly handled in the approved design.
````

## checklist/README.md

SHA-256: `b99af573170b9f4fe7f89743864dee5ea156ea54e100bf04cf46415e24662215`

````markdown
# REX Construction — Checklist Index

This directory owns page plans and acceptance criteria. The current request authorizes homepage implementation in the supplied Framer project. Publishing remains outside scope.

## Owners

- [Project](../PROJECT.md)
- [Current Status](../PROJECT.md#12-current-status)
- [Decisions](../PROJECT.md#13-decisions-and-exceptions)
- [Recovery](../PROJECT.md#14-recovery)
- [Platform workflow](../../../framer/README.md#1-先-inspect--reconcile)
- [Change control](../../../framer/basic/workflows/change-control.md#authorization-and-task-mode)

## Page Index

| Page | Path | Canonical checklist | Status |
|---|---|---|---|
| Home | `/` | [home.md](home.md) | Partial — Navbar, button variants, and six-review selector implemented; Hero counter instances await approved values |

Only Home has an active checklist. Existing supporting pages are reference destinations.

Latest request record: [Navigation, Buttons, Reviews, and Counters revision](home/navigation-buttons-reviews-counters.md) — implemented except Hero metric placement, which awaits approved values.

## Status Meaning

- **To do:** Authorized scope has not been implemented or verified.
- **In progress:** Work is underway on an explicit Part.
- **Fix Required:** A check failed and needs correction.
- **Blocked:** Required content, target, service or evidence is unavailable.
- **Pass:** The applicable structure, visual and runtime checks have passed.

A completed planning document does not mark the page as Pass.

## Shared Foundation Gate

Before implementation, inspect existing structures and decide Add / Reuse / Modify / No-op for the shell, navigation, footer, buttons and styles.

- [x] Confirm platform, project target and shared shell ownership.
- [x] Define text/color roles, readable logo sizing, buttons and responsive navigation.
- [x] Define keyboard focus, touch targets and reduced-motion behavior; live keyboard execution remains unavailable without staging.
- [ ] Assign favicon and social-sharing image.
- [ ] Confirm asset rights, form/newsletter connections and editing ownership.
- [x] Define component properties/variants before building reusable structures.

## Execution Loop

Read the page scope and contract → resolve the next Part's dependencies → implement that Part when authorized → targeted readback and Preview → record actual results → synchronize PROJECT status and its single Recovery owner.

Choose one primary implementation skill through the platform router. The local plan does not establish a Framer connection or prove current platform behavior.

## Part Result Format

Update the page's Latest Part Result with Part name, date, Pass / Fix Required / Blocked or Not run, verified widths, verified runtime paths, affected shared components and the canonical [Recovery reference](../PROJECT.md#14-recovery). Store the current checkpoint only in that Recovery owner.

## Latest Part Result

- Part: Navigation, Buttons, Reviews, and Counters revision
- Date: 2026-10-13
- Result: Partial — Phone hover removed; reusable Yellow-fill navigation, red, and white buttons implemented; white CTAs applied to three sections; six-review selector implemented. Hero Counter instances await approved metric values.
- Verified widths: 1200 and 390 visual; 810 structural.
- Verified paths/states: Phone Closed/Open with no row hover; Desktop nav and red/white button hover variants; section destinations; six review selections; Counter code-component registration; clean preview readiness.
- Canonical Recovery: [PROJECT §14](../PROJECT.md#14-recovery)
````

## checklist/home.md

SHA-256: `e2020eecc391cecaecf473a375192eaeeb0fca34ad8829648e939cd10ea65122`

````markdown
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
````

## checklist/home/navbar-trust-contact-revision.md

SHA-256: `27eaf3c2ffc8a4e200927c9db0950210f2cadee9e6de6fb7cfdb835296a4e868`

````markdown
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
````

## checklist/home/navigation-buttons-reviews-counters.md

SHA-256: `24ce4d44929cdabca81d792adb8cf5dd7242720851932041ae032171a771dd35`

````markdown
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
````
