# REX Construction LLC — Project

- State schema: 1
- Current status owner: [Inline Status](#12-current-status)
- Recovery owner: [Inline Recovery](#14-recovery)

## 1. Project Identity

- Project name: REX Construction LLC website redesign
- Platform: Framer — confirmed by the user.
- Project type: Business website / roofing and exterior construction
- Overall status: Partial — Review Selector arrows and routes received a live readback on 2026-10-14; broader site proof remains incomplete; not published.
- Production website: https://rexconstructionllc.com/
- Project / Canvas URL: https://framer.com/projects/REX-Construction--sTWVLfrpuNKD6x8u6CXh-cSBqA
- Preview URL: Missing
- Content status: Source-backed homepage summaries implemented; displayed Hero metrics were later reported as unverified; see Current Status. Source copy is unchanged by this reconciliation.
- Last updated: 2026-10-14
- Last verified against current implementation: Live Framer readback on 2026-10-14 verified all six Review Selector routes, arrow instances and testimonials CTA URLs. First/middle/last and John screenshots confirmed icon order; a sample preview click advanced Alex Corbett to John Zare. Broader site, breakpoint and exhaustive runtime checks remain incomplete. The width result is dated; see [width correction](../../history/workflow-observations/rexconstruction.md#2026-10-13-home-parent-width-correction).

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
| Brand and visual direction | [Home visual contract](checklist/home.md#visual-direction-contract) | Dated evidence retained; later revisions need targeted QA |
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

Current U5 follow-ups supersede the initial coral/shadow proposal: Red and White Button appearances use Yellow left-to-right fillers, no shadow, square corners, hidden filler L:-1px and Hover Relative width 101%; Desktop navigation uses Yellow with no offset; Phone rows have no hover. White belongs to the existing Button definition; implementation consolidation Needs refresh. [Active request](checklist/home/navigation-buttons-reviews-counters.md#constraint-lock) owns the details.

The original palette contrast calculations below remain dated measurements, not proof of the current Yellow states.

- Primary CTA: preserve red normal state and apply the active Yellow filler contract; verify current label contrast against both surfaces.
- Navigation links: Desktop Yellow hover with no offset; Phone no hover; visible keyboard focus requires runtime verification.
- Service rows: lighter charcoal surface and a coral arrow/leading rule; preserve readable body text.
- Initial timing reference: 180 ms; current filler timing requires targeted readback. Reduced motion removes transitions. Essential actions remain visible on touch; a hover effect is never required to reveal information.
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
| Reviews | `/testimonials` | Customer feedback | Reference destination; six source reviews saved |
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
- Implemented shared elements: Inspection Button with Label/Link Properties, no shadow, and Yellow filler gesture states; Yellow-fill Desktop Navigation Button; White appearance requested as a variant of the existing Button; consolidation Needs refresh; six-state Review Selector; reusable `Counter.tsx`; Site Navbar with Desktop, Tablet, Phone and Phone Open variants; Site Footer and Trust Bar.
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

- Width policy: No max-width on structural parent containers. Follow [Max-width ownership](../../framer/basic/standards/website-baseline.md#max-width-ownership); generic lint recommendations cannot restore removed parent caps. No bounded-shell exception is approved for REX.
- Verification widths proposed: 320, 390, 810, 1200 and 1440+ px.
- Motion: Subtle optional entry feedback; meaningful focus/pressed states; reduced-motion alternative.
- Web assets: [images/](images/). Current inventory contains 34 named assets; the flyer is currently JPG. This planning task does not alter formats.
- Licensing: User-supplied source-site assets; confirm delivery/republication rights before launch.
- Dated visual evidence and its limits are recorded in [Current Status](#12-current-status); no fresh visual or runtime Pass is claimed by this repository repair.

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

- State revision: 2026-10-14-10
- Active request: [U5 and parent-width follow-up](checklist/home/navigation-buttons-reviews-counters.md), including Follow-up 8
- Evidence basis: live Framer readback dated 2026-10-14 for the Review Selector component; surrounding page and runtime state remain Needs refresh.
- Current phase: Partial — parent-width structural repair was recorded; later U5 implementation and unresolved proof are reconciled below.
- Active page: Home — only page found in the dated REX-2 project audit.
- Last recorded width result: 27 `1120px` caps cleared from content parents and shared structures; global remaining `maxWidth` count 0. Existing width/layout values were preserved. This is dated tool evidence, not a new live claim.
- Later U5 outcome: reported three-image Hero autoplay (4s), review avatars and 300px review cards. On 2026-10-14, the six-state selector readback confirmed cyclic previous/next routes, two visible Next Button instances per state, and Testimonials CTA links. Existing Button/White-variant consolidation remains unproven. See [U5 observations](../../history/workflow-observations/rexconstruction.md#2026-10-13-u56-autoplay-and-review-cardlink-follow-up) and [latest selector closeout](../../history/workflow-observations/rexconstruction.md#2026-10-14-review-selector-next-button-follow-up).
- Open dependencies: displayed `10+`, `100+`, `5.0/5` were reported without authoritative business verification; approved values remain Missing. Also unresolved: White-variant consolidation, exhaustive runtime route/focus/hover coverage, 320 / 1440+ stress-width evidence, favicon/Open Graph and launch checks. This reconciliation does not approve numeric claims or change site content.
- Next approved step: confirm counter facts from approved sources, resolve White Button consolidation, then verify runtime interactions and 320 / 1440+ widths; preserve the no-parent-max-width rule. Publishing remains outside scope.
- Last verified: live Review Selector readback dated 2026-10-14: all six previous/next routes, two visible Next Button instances per state, and six Testimonials CTA links. First/middle/last and John screenshots visually confirmed arrow order; one preview click advanced Alex Corbett to John Zare. A complete six-state cycle and focus behavior were not tested.
- Closeout schema: 1
- Observation: Recorded — [Review Selector Next Button closeout](../../history/workflow-observations/rexconstruction.md#2026-10-14-review-selector-next-button-follow-up)

| Page | Implementation | Structural evidence | Visual/runtime evidence | Current result |
|---|---|---|---|---|
| Home | U5 follow-ups and parent-cap removal reported; Review Selector arrow component/routes live-read on 2026-10-14 | Six-state route/CTA readback; dated zero-maxWidth scan | First/middle/last and John selector screenshots visually reviewed; 320 / 1440+ and exhaustive runtime proof incomplete | Partial; no publication |

## 13. Decisions and Exceptions

| Decision | Reason | Scope | Status | Date |
|---|---|---|---|---|
| Official REX website is the source of truth | User instruction | Facts and source copy | Active | 2026-10-13 |
| Preserve exact extracted text in Info.md | User instruction | Source record | Active | 2026-10-13 |
| Create homepage plan/checklist and project entry | U1 | Repository planning | Active | 2026-10-13 |
| Build Home in the supplied REX Construction Framer project | U3 and supplied editor URL | Homepage implementation | Active | 2026-10-13 |
| Dark theme with bright hover highlights | U2 | Homepage visual direction | Active | 2026-10-13 |
| Convert Navbar/Footer to responsive components; add Trust Bar ticker and Contact image | U4 | Homepage shared shell, trust evidence and enquiry close | Implemented | 2026-10-13 |
| Refine Phone hover, add Yellow-fill navigation/buttons, review selector, and Hero counters from verified data | U5 | Navbar, buttons, Reviews and Hero metrics | Partial — see Current Status for later implementation and proof gaps | 2026-10-13 |
| No max-width on REX structural parents | Explicit user correction in REX-2; generic linter guidance is not authorization | Home and shared component width chains | Active; dated repair recorded | 2026-10-13 |

Dark theme and bright hover highlights are user-directed. Exact palette tokens, final wording, crops and section composition remain proposals in the checklist.

## 14. Recovery

- State revision: 2026-10-14-10
- Active request: [U5 and parent-width follow-up](checklist/home/navigation-buttons-reviews-counters.md), including Follow-up 8
- State reference: [Current Status](#12-current-status)
- Active connection: Existing REX Construction Framer project session was used for the 2026-10-14 selector edit; revalidate the live tree before future writes.
- Current page: Home
- Last recorded operation: Replaced the six local previous-arrow frames with reusable Next Button instances and corrected the six previous and six next routes; preserved all six Testimonials CTA links.
- Exact next action: follow the [official re-entry route](../../framer/README.md#3-change-control-是写入前的条件路由) before further Canvas edits. Resolve counter facts, White Button ownership and remaining visual/runtime checks in [Status](#12-current-status).
- Important asset paths: [Asset ledger](#asset-usage-ledger)
- Updated at: 2026-10-14; repository status includes live Review Selector readback.

## 15. Checklist and Change Control

- Index: [Checklist README](checklist/README.md)
- Canonical page owner: [Home](checklist/home.md)
- Request checklist: [U5 Navigation, Buttons, Reviews, and Counters revision](checklist/home/navigation-buttons-reviews-counters.md) — reconciled through the width follow-up; existing metrics require fact verification.
- Checklist status: Partial — [Current Status](#12-current-status) owns later implementation and evidence gaps.
- Last synchronized: 2026-10-14, revision 2026-10-14-10.

## 16. History

See [REX Construction workflow observations](../../history/workflow-observations/rexconstruction.md) and the [exact pre-reconciliation records](history/2026-10-13-before-width-closeout-repair.md).

## 17. Definition of Ready

- [x] Authorized planning scope and source authority recorded.
- [x] Page goal, audience, CTA and narrative proposed.
- [x] Source content, asset candidates and missing facts recorded.
- [x] Canonical homepage checklist created.
- [x] Final copy and visual direction ready for implementation.
- [x] Platform and project target identified.
- [x] Current page/shared structures audited before creating or replacing them.
- [x] Relevant content gaps resolved or explicitly handled in the approved design.
