# Summit Roofing — PROJECT

## 1. Project Identity

- Project name: Summit Roofing
- Platform: Framer Marketplace
- Project type: Marketplace Template
- Overall status: Home is complete; Services remains in progress; Repair & Maintenance is structurally implemented but Visual status is Fix Required; not published
- Project / Canvas URL: `https://framer.com/projects/Submit-Roofing--tdaqnMK09J7IYROr3Ma0-2uiTa?node=augiA20Il` — Verified through the official Framer Agent on 2026-08-23.
- Demo URL: Missing
- Content status: Mixed — brand identity and supplied assets are available; all operational copy and contact facts are Demo or Missing.
- Last updated: 2026-09-16
- Last verified against current implementation: 2026-09-16 — official Framer Agent targeted live-tree readback confirms Repair & Maintenance structure and its Desktop, Tablet and Phone breakpoint owners; clean diagnostics were returned. The later user full-page visual review found sibling-page duplication and an asset-allocation mismatch, so structural evidence remains valid but the page Visual status is Fix Required. This repository migration did not perform a fresh Canvas readback.

## 2. Scope and Authority

- Current scope: The Summit Roofing Home page and its necessary shared systems are complete. The confirmed Marketplace expansion includes Services, four Service Detail pages, Projects and Project Detail, About, Insights and Insight Detail, and Contact. Services and Repair & Maintenance are structurally implemented; the remaining routes remain planned until their own confirmed page Checklists begin.
- Explicit non-goals: Publishing, adding paid dependencies, inventing real local-service details, copying Baker Roofing’s brand assets/copy, or promoting unapproved secondary pages into the buyer-facing template. The existing `ScrollRevealText.tsx` code component and `/reveal-text-test` page are development-only and need an explicit retain/remove decision before Marketplace delivery.
- Primary page / component: Home (`/`) is complete; Services (`/services`) is in progress pending its detail-route and visual-evidence limitations. Repair & Maintenance (`/services/repair-maintenance`) retains its verified structure but is Fix Required: its composition and colour-block rhythm are too close to Services, and its staged image set was not fulfilled.
- User-approved direction: Create an original Summit Roofing composition using Baker Roofing only as a reference for clean typography, hard-edged geometry, image-led storytelling, disciplined spacing and direct service/CTA hierarchy. Do not reproduce Baker's section order, structural proportions, grid ratios, logo, text, project facts or proprietary font files. Use an independent blue-grey visual identity.
- Current implementation differences: The approved Home is implemented. Unknown operational facts remain intentionally absent or Demo; Marketplace publication materials remain outside the completed Home scope. Live Canvas currently displays `SUBMIT ROOFING` in the shared Navbar and Footer while this project record names the template `Summit Roofing`; this is recorded as an unresolved brand-name mismatch, not an authorized direction change.
- Items requiring confirmation: Whether the live brand label should be `SUBMIT ROOFING` or `Summit Roofing`; whether to retain or remove the development-only Reveal Text code component and test page; final brand copy, demo contact details, service-area claims, supplied-image licensing, Marketplace listing assets and explicit publication approval. The multi-page Sitemap and staged image-use plan are confirmed.

## 3. Knowledge Map

| Responsibility | Current source | Status |
|---|---|---|
| Brand Voice | This PROJECT §6 and §9 | Draft |
| Style Guide | This PROJECT §6 and verified Framer shared Styles | Active |
| Formal Content | This PROJECT §9; all copy is proposed template copy | Draft / Demo |
| Assets | `/Users/Zhuanz/Desktop/Submit Roofing/` | Supplied; licence status Missing |
| Inspiration | Baker Roofing homepage: `https://bakerroofing.com/` | Approved layout/style reference, not a structural blueprint |
| Current Status | Inline §12 | Structurally verified 2026-08-26 |
| Decisions | Inline §13 | Active |
| Recovery | Inline §14 | Active |
| Checklist index | [Page Checklist index](./checklist/README.md); [approved site expansion plan](./checklist/site/2026-08-26-site-expansion-planning.md) | Home requests completed; site master plan approved; page contracts created one page at a time |
| History index | Not created | Not required |

## 4. Website Goal

- Website audience: Property owners and facilities managers evaluating a roofing contractor; Marketplace buyers evaluating a professional roofing template.
- User needs to understand: The company is competent, responsive and organised around clear roofing services, visible evidence and a direct next step.
- Most important result: A qualified estimate / inspection request.
- Primary CTA: Request an Inspection
- Secondary CTA: Explore Services
- Success evidence: Visitors can identify a relevant service, see proof-of-work and reach a short conversion path without searching for contact information.

## 5. Target User

- Primary audience: Residential and small-commercial property owners. The template should remain adaptable to regional roofing businesses.
- User intent: Verify fit, assess credibility, review services/projects, then request an inspection or estimate.
- Important questions: What work is offered? Can they handle my roof type/problem? Is their work credible? How do I start?
- Trust requirements: Authentic jobsite imagery, clear service labels, straightforward language, visible contact CTA, proof rather than unverified numerical claims.
- Device priority: Balanced, with phone optimised for urgent service enquiries.

## 6. Brand Direction

- Brand personality: Practical, steady, direct and capable — skilled trade without visual clutter.
- Core concept: “Clear roofline, clear next step.” The template uses large structural type and restrained image framing to make a consequential service feel simple to begin.
- Visual memory point: A wide work-in-progress roof image, oversized condensed headline, square slate-blue CTA, steel-grey information bands and an occasional angular roofline divider. The blue must own meaningful surfaces, not appear only in small controls.
- Typography direction: Reference Baker Roofing's strong hierarchy without copying its exact proportions: condensed, uppercase, tightly led display headlines with a neutral grotesk sans-serif for body and navigation. Implemented fonts are `Big Shoulders` for display type and `Inter` for body/navigation. Do not use Baker Roofing’s proprietary font files.
- Color direction: Independent blue-grey industrial palette. Approved colors: Slate Blue `#365F7A` as the primary brand color, Deep Navy `#172B3A` for high-contrast sections, Steel Grey `#6C767D` for secondary text and utility surfaces, Mist Grey `#E3E7E8` for section bands, Soft White `#F5F6F5` for the main canvas, and Pure White `#FFFFFF` for contrast. Target balance: Soft White / Mist Grey 45–55%, Slate Blue / Deep Navy 25–35%, Steel Grey 10–15%, with the remaining visual weight supplied by photography. Use at least one substantial blue section or band; do not use red as a brand UI color.
- Reference translation: Borrow the reference's typography hierarchy, crisp rules, strong image blocks and direct conversion rhythm. Design Summit's section order, widths, grid proportions, spacing rhythm and responsive transformations independently; it must not be Baker Roofing with substituted content.
- Geometry direction: `0px` corner radius everywhere — buttons, cards, images, inputs, menus, overlays, Navbar and Footer surfaces. Use straight edges, hard crops, 1px rules and optional angular roofline cuts for hierarchy.
- Image strategy: Use supplied high-resolution jobsite, roof-detail, completed-home and crew photos. Pair wide images with decision points; use portraits only as supporting human proof. Preserve native crop quality and add factual alt text at build time.
- Motion character: Near-still and purposeful — short reveal/fade only; never conceal required content behind hover.
- Avoid: Any rounded corners, pill-shaped controls, red brand UI, exact copying of Baker's section sequence or proportions, generic gradient/glass treatment, invented award counters, anonymous five-star testimonials, soft floating cards, or dramatic disasters as the default hero image.

## 7. Content Facts

| Fact | Value | Source | Status |
|---|---|---|---|
| Brand name | Summit Roofing | Supplied `Logo.png` | Approved for template identity |
| Address | Missing | — | Missing |
| Phone | Missing | — | Missing |
| Email | Missing | — | Missing |
| Opening hours | Missing | — | Missing |
| Social links | Missing | — | Missing |
| Prices | Missing | — | Missing |
| Service area | Missing | — | Missing |
| Legal / copyright | Image licence verification required before Marketplace submission | Supplied asset folder | Missing |

## 8. Sitemap and Page Goals

| Page | Path | User goal | Primary CTA | Content source | Current status |
|---|---|---|---|---|---|
| Home | `/` | Understand capability, evaluate credibility and begin an enquiry | Request an Inspection | Demo template copy and supplied imagery | Built and QA complete; not published |
| Services | `/services` | Compare the four core service paths and choose the relevant need | Explore a Service / Request an Inspection | Approved service labels; supporting copy remains Demo | Structurally implemented; Page Done blocked by unbuilt detail destinations and bounded visual evidence |
| Repair & Maintenance | `/services/repair-maintenance` | Understand assessment, maintenance and repair support | Request an Inspection | Demo service copy; operational details Missing | Structural status Pass; Visual status Fix Required; not published |
| Roof Replacement | `/services/roof-replacement` | Understand replacement triggers, process and material decisions | Request an Inspection | Demo service copy; product and warranty facts Missing | Planned and confirmed; not built |
| New Construction | `/services/new-construction` | Understand coordination and installation for new builds | Discuss a Project | Demo service copy; contractor credentials Missing | Planned and confirmed; not built |
| Storm Damage Repair | `/services/storm-damage-repair` | Understand the immediate response path after roof damage | Request an Inspection | Demo service copy; emergency response claims Missing | Planned and confirmed; not built |
| Projects | `/projects` | Review a filterable body of visual work and evaluate fit | View Project / Request an Inspection | Existing Projects CMS; project facts remain Demo | Planned and confirmed; not built |
| Project Detail | `/projects/:Projects` | Examine one project’s challenge, scope, solution and visual result | Request a Similar Inspection | Existing Projects CMS; verified case-study facts Missing | Planned and confirmed; not built |
| About | `/about` | Understand the team, working principles and process | Meet the Team / Request an Inspection | Demo template copy and supplied team imagery | Planned and confirmed; not built |
| Insights | `/insights` | Find practical roofing guidance and maintenance education | Read Article | Existing Insights CMS; article copy remains Demo | Planned and confirmed; not built |
| Insight Detail | `/insights/:Insights` | Read one useful article and continue to a relevant service | Explore Services / Request an Inspection | Existing Insights CMS | Planned and confirmed; not built |
| Contact | `/contact` | Submit a short inspection or estimate enquiry | Send Request | Contact and service-area facts Missing | Planned and confirmed; not built |
| Reveal Text test | `/reveal-text-test` | Development-only code-component inspection | `ScrollRevealText.tsx` test instance | No buyer-facing content source | Exists in Canvas; exclude from Marketplace scope until retain/remove decision |

The buyer-facing expansion above is confirmed. Four stable service offers use authored routes; Projects and Insights use CMS archive/detail pairs. Careers, Locations, National Accounts and other Baker-specific enterprise routes are intentionally excluded.

## 9. Narrative and Conversion

| Page | Section / Part | Purpose | Content source | Image role | CTA / next step |
|---|---|---|---|---|---|
| Home | Utility bar + nav | Keep urgent contact and route choices obvious | Demo labels; contact values Missing | No image | Request an Inspection |
| Home | Hero | State the promise and make the inspection route immediate | Proposed copy: “Roofing built to hold up.” | `shingle-install.webp` or `modern-home.webp` with dark overlay | Request an Inspection / Explore Services |
| Home | Trust strip | Frame the business around workmanship, communication and care without inventing statistics | Draft value labels | Optional logo mark | Continue to services |
| Home | Services | Let visitors self-select the reason for visiting | Draft: Repair & Maintenance / Roof Replacement / New Construction / Storm Damage Repair | One wide roof/work image; no equal-card default | View Services |
| Home | Featured work | Replace claims with visual evidence | Four project titles and locations remain Demo until supplied | Supplied completed-roof, material and storm-damage-repair WebP images | View Projects |
| Home | Process | Lower friction by explaining the path from inspection to completed work | Draft 3-step labels | `roof-aerial.webp` or crew image | Start with an Inspection |
| Home | Team / local proof | Add a human note without fabricated bios | Demo labels only | `crew-lead.webp` or `roof-harness.webp` | Meet the Team / Contact |
| Home | Insights | Make education a modular content destination rather than filler | Titles remain Demo until supplied | Optional roof-detail image | Read Insights |
| Home | Closing CTA + footer | Repeat one clean next step and expose all needed navigation/contact fields | Contact values Missing | Detail or no image | Request an Inspection |
| Services | Intro + service navigator | Present the four approved service paths without forcing equal-card repetition | Approved labels; descriptions are Demo | One strong roof/work image plus service-specific supporting details | Choose a Service |
| Service Detail | Problem / fit, assessment, work scope, process, FAQs and closing CTA | Answer the decision questions for one stable service offer | Demo copy; facts, warranties and response times Missing | 2–4 relevant jobsite/detail images allocated in §11 | Request an Inspection |
| Projects | Intro, project filters or categories, visual archive and closing CTA | Turn supplied imagery into proof and route visitors toward comparable work | Existing Projects CMS; project names/locations remain Demo | Flat/commercial and exterior project image groups | View Project |
| Project Detail | Hero, project facts, challenge, solution, gallery/result and related CTA | Provide a reusable case-study structure without invented claims | Existing Projects CMS; verified facts Missing | Images from one verified project set when supplied | Request a Similar Inspection |
| About | Story, working principles, process, crew imagery and service CTA | Humanise the template while keeping the tone practical | Demo template copy; bios and credentials Missing | `team.webp` plus selected crew portraits | Request an Inspection |
| Insights | Intro, featured article, article archive and service CTA | Establish a useful education destination rather than filler | Existing Insights CMS | Roof detail, sample and aerial imagery | Read Article |
| Insight Detail | Article header, body, useful takeaway, related article/service and CTA | Support search and trust with readable editorial content | Existing Insights CMS | One relevant detail image per article | Explore Services |
| Contact | Direct contact options, short enquiry form, service-area note and expectation setting | Create the shortest conversion path | Contact facts, form endpoint and privacy text Missing | Optional restrained jobsite/detail image; no generic office stock required | Send Request |

Primary path:

```text
Landing → understand the offer → select a service → view proof / process → request an inspection
```

- Phone / email / map / social / form: Missing. Use visible template placeholders only after the Marketplace template’s demo-content policy is confirmed.
- Secondary paths: Services → relevant Service Detail → Contact; Projects → Project Detail → Contact; Insights → Insight Detail → relevant Service or Contact.

### Page Visual Identity

| Page | Visual memory point | Dominant composition | Colour rhythm | Sibling difference | Status |
|---|---|---|---|---|---|
| Services | A direct service navigator with four work paths | Image-led masthead, linear navigator, ruled method ledger | Deep-navy opening, white navigator, substantial slate-blue method band, pale handoff | Overview and route selection | In progress; bounded visual evidence remains limited |
| Repair & Maintenance | Condition evidence leading into assessment and repair decisions | Must be recomposed around diagnosis, evidence and scope rather than repeat the Services topology | Preserve approved tokens but change the Services section-colour sequence and weighting | Detail journey, not another overview ledger | Fix Required; active Visual Direction Contract is Draft |

## 10. System and Platform Plan

- Platform router: `framer/README.md`; the official Framer Agent gate and targeted live-tree readback passed on 2026-08-23.
- Selected Skills: Official `framer`, primary `framer-components`, supporting `framer-layout-responsive`, and final `framer-qa`.
- Text / Color Style source: Implemented as six shared Color Styles plus responsive display, body, utility and link styles based on §6.
- Geometry system: All visible radii fixed at `0px`; no rounded Component Variant or breakpoint exception is planned.
- Shared Components: Button, Service Row, Process Step, Project Card, Article Card, responsive Navbar and responsive Footer are implemented as native Framer Components.
- CMS decision: Existing Projects and Insights Collections own their archive/detail pairs. The four stable services use authored routes with one shared page contract; do not add a Services CMS unless later content scale requires it.
- Navbar / Footer: Implemented through a responsive `Site Shell` Layout Template with Desktop, Tablet and Phone ownership.
- Links and semantics: Semantic headings, visible focus and non-hover-only actions required.
- Accessibility / Focus: Maintain contrast; respect reduced motion; alt text must describe the actual supplied image.
- Third-party dependency: None proposed.
- Custom Code: Home has no code-component dependency. The project currently contains `ScrollRevealText.tsx` and its `/reveal-text-test` development page; its documented pattern is [Scroll Reveal Text](../../framer/advance-design/summit-roofing/scroll-reveal-text.md). Its Marketplace retention is unresolved.

## 11. Responsive, Interaction and Assets

| Area | Desktop | Tablet | Phone |
|---|---|---|---|
| Navbar | Utility strip + full nav + CTA | Condensed links + CTA | Logo, menu trigger and persistent CTA; phone values only when supplied |
| Hero | Wide 55–65vh image plane; copy aligned left | Preserve type hierarchy, reduce image height | Image remains contextual; text and primary CTA lead before scrolling |
| Main layout | Alternating full-bleed image / contained editorial blocks | Shift asymmetrical pairs to stable two-column or stack | One clear reading column; services become rows rather than cramped cards |
| Footer | Multi-column utility grid | Two-column groups | Stacked contact and legal groups |
| Special interaction | Project Card uses a dark image mask plus slate-blue text Hover variant | Same behaviour | Tap-safe default state; no hover-only information |

- Required test widths: Verified at 1200px, 810px and 390px, with a structural 320px narrow-width stress check and a capped/centred wide-layout review.
- Reduced Motion: No essential movement; transition effects disabled or simplified.
- Source asset folder: `/Users/Zhuanz/Desktop/Submit Roofing/` — verified 2026-08-23: 27 supplied assets are WebP, each ≤500KB; prior JPG/PNG sources were removed on user instruction.
- Project asset library: `images/` — verified 2026-08-23: 38 project assets are WebP, each ≤500KB; `images/home/` contains the 11 uploaded Home assets plus the cropped Navbar Logo asset.
- Hero candidates: `roofer on roof/shingle-install.webp`, `exterior/modern-home.webp`, `flat roof/modern-deck.webp`.
- Confirmed staged allocation for Repair & Maintenance: `roofer on roof/roofer-ledge.webp`, `roofer on roof/roof-work.webp`, `exterior/roof-detail.webp`.
- Confirmed staged allocation for Roof Replacement: `exterior/red-roof.webp`, `roofer on roof/shingle-install.webp`, `exterior/modern-home.webp`; reserve `exterior/tile-house.webp` for Projects.
- Confirmed staged allocation for New Construction: `exterior/house-frame.webp`, `roofer on roof/frame-ladder.webp`, `roofer on roof/roof-framing.webp`; reserve `roofer on roof/roof-build.webp`.
- Confirmed staged allocation for Storm Damage Repair: `storm damage roof/fire-damage.webp`, one of the visually duplicated `roof-damage.webp` / `storm-repair.webp`, and `storm-roof.webp`; `roof-crane.webp` is optional.
- Confirmed staged allocation for Projects: flat/commercial work uses `flat-roof.webp`, `roof-aerial.webp`, `facade-roof.webp` and `modern-deck.webp`; exterior work uses `brick-roof.webp`, `tile-house.webp`, `modern-home.webp` and `red-roof.webp`.
- Confirmed staged allocation for About: `team.webp`, `roofer portait/crew-lead.webp`, `roofer portait/roof-harness.webp`; reserve `crew-beanie.webp` and `crew-smile.webp`.
- Confirmed staged allocation for Insights: `exterior/roof-detail.webp`, `exterior/roof-samples.webp`, `flat roof/roof-aerial.webp` and unused jobsite details.
- Missing assets / evidence: Commercial-use licences, verified same-project before/after pairs, verified project facts/locations/captions and a real office/contact scene. Contact/service-area facts, form endpoint and privacy text are also Missing.
- License status: Missing — confirm all supplied files are licensed for a Framer Marketplace template before publication.

### Asset Usage Ledger

| Asset | Narrative qualities | Approved role | Current use | Reuse decision / reason | Crop / focal notes | Status |
|---|---|---|---|---|---|---|
| Services aerial masthead image | Top-down roof-condition overview | Services overview masthead | Services and Repair & Maintenance mastheads in the reviewed Canvas | Repair reuse is not approved: it duplicates the sibling page and bypasses the allocated Repair narrative set | Existing broad aerial crop; no page-specific focal plan recorded | Reassigned from Repair; retain on Services pending later review |
| `roofer on roof/roofer-ledge.webp` | Human inspection context and roof-edge condition | Repair assessment / inspection evidence | Not evidenced on the reviewed Repair page | Use on Repair after the Visual Direction Contract assigns its exact Section and breakpoint crop | Focal plan Missing until contract becomes Ready | Allocated; not yet fulfilled |
| `roofer on roof/roof-work.webp` | Active repair work and material handling | Repair work-scope evidence | Not evidenced on the reviewed Repair page | Use on Repair or deliberately reassign with a recorded narrative reason | Focal plan Missing until contract becomes Ready | Allocated; not yet fulfilled |
| `exterior/roof-detail.webp` | Material and condition detail | Repair maintenance / decision detail | Not evidenced on the reviewed Repair page; also staged for Insights | Cross-page reuse requires separate narrative roles and crop decisions; do not silently reuse | Focal plan Missing until contract becomes Ready | Allocated to Repair; shared future allocation requires review |

## 12. Current Status

- Current phase: Home is complete and Services remains in progress. Repair & Maintenance retains a structurally verified first build, but the 2026-09-16 user visual review sets the page to Fix Required for sibling-page duplication, weak page-specific composition and unfulfilled Repair image allocation.
- Active page / component: Repair & Maintenance (`/services/repair-maintenance`) is the active correction scope. Its new Visual Direction Contract is Draft; no Canvas repair occurred in this repository migration. Development-only `ScrollRevealText.tsx` / `/reveal-text-test` remain outside the buyer-facing expansion.
- Current blockers: The Repair visual contract is not Ready, its three allocated images lack implemented narrative roles and corrected full-page visual evidence does not exist. Supplied-image commercial licensing, contact, address, service-area and legal facts are Missing; Marketplace Demo/Remix URLs and listing assets do not yet exist. The `Summit Roofing` / `SUBMIT ROOFING` mismatch and Reveal Text retain/remove decision remain unresolved.
- Next approved step: Compile the Repair & Maintenance Visual Direction Contract to Ready, then in a separately authorised live Canvas task correct and verify that page before advancing to Roof Replacement. Missing operational facts must remain visibly Demo or Missing; image licensing and explicit approval still block Marketplace publication.
- Last verified: 2026-09-16 — official Framer Agent targeted live readback confirms Home’s eight named Sections and its one H1 / seven H2 structure at Desktop, Tablet and Phone; `Site Shell` owns shared Navbar and Footer at all three breakpoints; Projects has four Demo items and Insights has two Demo items; Home CTAs and navigation point to existing Home anchors; metadata and inspected image Alt text are present. Services has four named Sections in one page-owned vertical content container: an image-led deep-navy masthead, Service Navigator, page-owned Method Ledger and Inspection Handoff. The Method Ledger now contains three named process blocks, each with an H3 and `Body/Default` Demo description. Repair & Maintenance has one vertical page-content container and six named semantic Sections: image-led masthead, Assessment, Work Scope, Repair Process, Repair FAQ and Inspection Handoff. Desktop uses a bounded two-column scope, ruled three-step process and four structured Demo FAQ items; Tablet reduces section padding; Phone changes scope and process to single-column stacks with 24px gutters. The masthead image has factual Alt text and both page CTAs point to verified `/#contact`. Clean diagnostics support these structural facts only. The later user full-page review establishes Visual Fix Required because the page closely repeats Services and reuses its aerial image instead of fulfilling the allocated Repair set. No fresh Canvas readback or publication occurred during this repository migration.

| Page | Content | Styles | Components | Links | SEO | Alt | Desktop | Tablet | Phone | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| Home | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Targeted readback, 390px bounded preview, 320px stress scan, readiness preview: 0 errors / 0 warnings |
| Services | Demo | ✓ | ✓ | Partial | ✓ | ✓ | ✓ | ✓ | ✓ | Four distinct Sections; unique Desktop/Phone Service Rows, 810px Tablet flow, specific masthead Alt and one bounded Desktop masthead screenshot; final detail links, 320/1440 review and full-page Preview remain blocked/deferred |
| Repair & Maintenance | Demo | ✓ | Reused | Partial | Inherited | ✓ | ✓ | ✓ | ✓ | Structural Pass: six semantic Sections, one H1, structured Demo FAQ and Desktop/Tablet/Phone live readback. Visual Fix Required: composition and colour rhythm closely repeat Services, its aerial image was reused, and the allocated Repair set was not fulfilled. |

## 13. Decisions and Exceptions

| Decision | Reason | Scope | Status | Date | Supersedes |
|---|---|---|---|---|---|
| Use Baker Roofing as the close visual benchmark | Earlier interpretation treated the reference too literally and included its color direction | Home visual system | Superseded | 2026-08-23 | Earlier loose “informed by” direction |
| Use safety red as a primary brand surface | Earlier color proposal; user explicitly replaced it with a blue-grey direction | Home color system | Superseded | 2026-08-23 | Earlier “red accent” wording |
| Use Baker Roofing as a style and layout reference, not a structural blueprint | Preserve the reference's clean hierarchy and trade-industry confidence while keeping Summit's section order, proportions, grids and spacing original | Home visual system | Active | 2026-08-23 | Close visual benchmark decision |
| Use an independent blue-grey palette | User explicitly rejected red and selected grey and blue; slate blue provides roofing/material character without reading as generic tech branding | Home color system | Active | 2026-08-23 | Safety-red primary decision |
| Use zero-radius geometry | User explicitly rejected rounded corners; square edges better match the approved industrial reference | All Home Components and surfaces | Active | 2026-08-23 | Earlier allowance for restrained rounding |
| Treat service facts and contact details as Missing | Marketplace design must not disguise invented business facts as real | All template content | Active | 2026-08-23 | — |
| Retain original asset folder and rename files only | Initial asset-management direction before the user required format conversion and source removal | Supplied assets | Superseded | 2026-08-23 | — |
| Convert supplied assets to WebP at ≤500KB and remove old formats | User explicitly required WebP delivery and removal of prior formats; converted outputs were decoded and size-checked before source deletion | Desktop source folder and project asset library | Active | 2026-08-23 | Retain-original asset decision |
| Use a cropped supplied Logo in the shared Navbar | The square white-background Logo was cropped to its roof-mark and wordmark bounds before use so the shared navigation remains compact; Footer retains editable text branding for contrast on its dark surface | Navbar Component, Desktop/Tablet/Phone | Active | 2026-08-23 | Text-only Navbar brand |
| Use native CMS repeated card templates for dynamic project/article images | Framer rejected direct CMS responsive-image binding through Component Instances; native repeated templates preserve correct per-item images while standalone reusable Card Definitions remain available | Home Projects and Insights lists | Active platform exception | 2026-08-23 | Planned all-instance CMS card binding |
| Bind Featured Work’s native CMS template to the existing Project Card | The current Framer binding accepts CMS responsive-image and text variables through the Card Instance; this makes the requested Hover variant active for every Featured Work item while preserving the Projects collection | Home Featured Work only | Active | 2026-08-23 | Native Projects-card exception |
| Use a transparent cropped roof mark alongside requested text branding | The supplied square logo includes a roof mark plus stacked wording. Navbar and Footer now use a factual cropped roof-only WebP with editable `SUBMIT ROOFING` text beside it, avoiding duplicate wording inside the image | Navbar and Footer, all breakpoints | Active | 2026-08-23 | Cropped full-logo Navbar decision |
| Keep Lucide stroke width at 2px | The previous value `16` controlled stroke thickness rather than icon box size, producing blob-like icon rendering. Visual size remains owned by each IconNode’s width and height. | Shared Button and Navbar icons | Active repair | 2026-08-23 | — |
| Expand the template through nine buyer-facing page types | User confirmed a service-led Sitemap informed by Baker Roofing’s page roles while excluding its enterprise-specific Careers, Locations, National Accounts and unsupported company claims | Services, four Service Details, Projects and Project Detail, About, Insights and Insight Detail, Contact | Active | 2026-08-26 | Earlier Home-only scope |
| Allocate supplied imagery by page role and preserve reserves | The full supplied image set was reviewed; staged use prevents omission without forcing every image into the first implementation pass or repeating visually duplicate storm images | Multi-page expansion assets | Active | 2026-08-26 | — |

## 14. Recovery

- Active session / connection: No active session is claimed for this repository migration. The latest retained official Framer Agent evidence is the 2026-09-16 structural readback; no publication action was taken.
- Current page / component: Repair & Maintenance route and shared `Site Shell`; `ScrollRevealText.tsx` and `/reveal-text-test` remain development-only pending a retain/remove decision.
- Last successful change: On 2026-09-16, the first structural build of Repair & Maintenance was completed without changing shared Components. It includes an image-led masthead, assessment, practical scope, three-step process, a four-item structured Demo FAQ and closing inspection handoff. This does not constitute visual completion; the later user review sets Visual status to Fix Required.
- Last targeted readback: Repair & Maintenance content container, all six semantic Sections, masthead Alt and CTA, Desktop two-column scope, structured four-item FAQ, and the Desktop 1200px / Tablet 810px / Phone 390px breakpoint owners were verified through official Framer Agent readback on 2026-09-16. The final build returned clean Framer diagnostics. No Preview or publication occurred.
- Verified breakpoints / states: Repair & Maintenance Desktop 1200px, Tablet 810px and Phone 390px own revised structures. Phone uses 24px section gutters, a stacked scope, and a stacked process sequence. These are structural facts; corrected cross-page composition, Repair 320px / 1440px visual review and full-page evidence remain unverified.
- Remaining approved work: First compile the Repair visual contract to Ready and complete a separately authorised Canvas correction with structural and full-page comparative visual proof. Only after Repair passes may Roof Replacement proceed. Later expansion order, link restoration, brand-name and Reveal Text decisions remain unchanged.
- Exact next action: Review and approve the Repair Visual Direction Contract decisions before any live Canvas correction; do not start Roof Replacement first.
- Important local asset paths: `/Users/Zhuanz/Desktop/Submit Roofing/`
- Updated at: 2026-09-16

## 15. Checklist and Change Control

- Project checklist index: [checklist/README.md](./checklist/README.md)
- Active page checklist: [Repair & Maintenance page Checklist](./checklist/repair-maintenance/2026-09-16-page-build.md) — Structural status Pass; Visual status Fix Required; active Visual Direction Contract Draft.
- Active request checklist: [approved site expansion plan](./checklist/site/2026-08-26-site-expansion-planning.md)
- Checklist status: Project-wide plan Approved; Services remains in progress; Repair & Maintenance Fix Required pending a Ready visual contract and later Canvas correction; publishing excluded.
- Last synchronization with Current Status: 2026-09-16

## 16. History

- History index: Not created.
- Closed prompt / handoff records: None.
- Superseded plans worth retaining: None.

## 17. Definition of Ready

- [x] Current Scope and non-goals documented.
- [x] Website goal, target user and Home-page purpose established.
- [x] Primary CTA and conversion path proposed.
- [x] Brand direction and relevant inspiration documented.
- [x] Facts separated into Approved, Demo and Missing.
- [x] Supplied assets inventoried and renamed; license status retained as Missing.
- [x] Current implementation verified against the live Canvas.
- [x] Change-control requirement identified and request checklist created.

Home is built and QA complete. Services is structurally implemented but has recorded conversion and visual-evidence limitations; the remaining confirmed expansion routes have not begun. The project is not ready for Marketplace submission until the approved pages are built and verified, commercial-use image licences, final business facts and Marketplace delivery assets are resolved, and publishing is separately authorised.
