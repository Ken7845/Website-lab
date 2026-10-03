# Summit Roofing — PROJECT

## 1. Project Identity

- Project name: Summit Roofing
- Platform: Framer Marketplace
- Project type: Marketplace Template
- Overall status: Home is complete; Services remains in progress; Repair & Maintenance is structurally and visually verified at Desktop and Phone, with final stress and Preview checks still pending; not published
- Project / Canvas URL: `https://framer.com/projects/Submit-Roofing--tdaqnMK09J7IYROr3Ma0-2uiTa?node=augiA20Il` — Verified through the official Framer Agent on 2026-08-23.
- Demo URL: Missing
- Content status: Mixed — brand identity and supplied assets are available; all operational copy and contact facts are Demo or Missing.
- Last updated: 2026-10-03
- Last verified against current implementation: 2026-09-18 — official Framer Agent targeted live-tree readback confirms `/projects/:Projects` has five CMS-bound record-sheet Sections and Desktop 1200 / Tablet 810 / Phone 390 owners. The `/projects` lead and field record wrappers resolve to matching `/projects/:slug` items; the CMS schema and shared Components remain unchanged.

## 2. Scope and Authority

- Current scope: The Summit Roofing Home page and its necessary shared systems are complete. The confirmed Marketplace expansion includes Services, four Service Detail pages, Projects and Project Detail, About, Insights and Insight Detail, and Contact. Services and Repair & Maintenance are structurally implemented; the remaining routes are planned until their own confirmed page Checklists begin.
- Explicit non-goals: Publishing, adding paid dependencies, inventing or implying real local-service details, copying Baker Roofing’s brand assets/copy, or promoting unapproved secondary pages into the buyer-facing template. User-authorized fictional reference copy is allowed for template blanks when it is internally retained as `Demo`; it must not be presented as verified business fact. The existing `ScrollRevealText.tsx` code component and `/reveal-text-test` page are development-only and need an explicit retain/remove decision before Marketplace delivery.
- Primary page / component: Home (`/`) is complete; Services (`/services`) is in progress pending its remaining detail-route and visual-evidence limitations. Repair & Maintenance (`/services/repair-maintenance`) is structurally complete and visually verified at Desktop and Phone; its stress and Preview checks remain pending.
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
| Current Status | Inline §12 | Live sitemap readback, 2026-09-16 |
| Decisions | Inline §13 | Active |
| Recovery | Inline §14 | Active |
| Hover readiness | [Site hover audit and implementation order](./checklist/site/hover-readiness-audit.md) | Verified pre-edit audit snapshot; implementation evidence lives in active request |
| Active hover request | [Shared hover implementation checklist](./checklist/site/2026-10-03-hover-implementation.md) | Implemented; Structural Pass / Visual and runtime Blocked, 2026-10-03 |
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
| Repair & Maintenance | `/services/repair-maintenance` | Understand assessment, maintenance and repair support | Request an Inspection | Demo service copy; operational details Missing | Structural Pass; Desktop and Phone visual evidence Pass; stress and Preview checks pending; not published |
| Roof Replacement | `/services/roof-replacement` | Understand replacement triggers, process and material decisions | Request an Inspection | Demo service copy; product and warranty facts Missing | Structural and Desktop visual Pass; stress and Preview checks pending; not published |
| New Construction | `/services/new-construction` | Understand coordination and installation for new builds | Discuss a Project | Demo service copy; contractor credentials Missing | Structural and bounded Desktop visual Pass; stress and Preview checks pending; not published |
| Storm Damage Repair | `/services/storm-damage-repair` | Understand the immediate response path after roof damage | Request an Inspection | Demo service copy; emergency response claims Missing | Structural and bounded Desktop visual Pass; stress and Preview checks pending; not published |
| Projects | `/projects` | Review an editable body of visual work and evaluate fit | Discuss a Project | Existing Projects CMS; project facts remain Demo | Structural and bounded Desktop visual Pass; stress and Preview checks pending; CMS record wrappers link to matching Project Detail items |
| Project Detail | `/projects/:Projects` | Examine one editable project record without fabricating a case study | Discuss a Project | Existing Projects CMS; all richer case-study facts remain Missing | Structural and bounded Desktop visual Pass; stress and Preview checks pending |
| About | `/about` | Understand editable working principles and crew imagery | Discuss a Project | Demo template copy and supplied crew imagery | Structural Pass at Desktop, Tablet and Phone; Visual Blocked; stress and Preview checks pending |
| Insights | `/insights` | Find practical roofing guidance and maintenance education | Explore Services | Existing Insights CMS; Title, Category, Summary and Image remain Demo | Structural Pass at Desktop, Tablet and Phone; visual review and detail route pending |
| Insight Detail | `/insights/:Insights` | Read one useful article and continue to a relevant service | Explore Services / Request an Inspection | Existing Insights CMS | Structural Pass at Desktop, Tablet and Phone; visual, stress and Preview evidence pending |
| Contact | `/contact` | Submit a short inspection or estimate enquiry | Send Request | Contact and service-area facts Missing | Structural Pass at Desktop, Tablet and Phone; delivery and visual evidence blocked |
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
| Projects | Index opening, Demo record band, lead record, uneven archive field and closing CTA | Show editable Demo work records without presenting them as verified project proof | Existing Projects CMS; project names/locations remain Demo | Images already bound to the four CMS records | Discuss a Project |
| Project Detail | Record threshold, metadata sheet, Demo-status strip, image record and closing CTA | Present one editable CMS record while visibly reserving unsupported case-study fields | Existing Projects CMS; verified facts Missing | The item’s own CMS Image only | Discuss a Project |
| About | Story, working principles, process, crew imagery and service CTA | Humanise the template while keeping the tone practical | Demo template copy; bios and credentials Missing | `team.webp` plus selected crew portraits | Request an Inspection |
| Insights | Intro, featured article, article archive and service CTA | Establish a useful education destination rather than filler | Existing Insights CMS | Roof detail, sample and aerial imagery | Read Article |
| Insight Detail | Article header, body, useful takeaway, related article/service and CTA | Support search and trust with readable editorial content | Existing Insights CMS | One relevant detail image per article | Explore Services |
| Contact | Direct contact options, short enquiry form, service-area note and expectation setting | Create the shortest conversion path | Contact facts, form endpoint and privacy text Missing | Optional restrained jobsite/detail image; no generic office stock required | Send Request |

Primary path:

```text
Landing → understand the offer → select a service → view proof / process → request an inspection
```

- Phone / email / map / social / form: Missing as real operational facts. The front end uses clearly fictional Demo contact references (`.example` email and a reserved fictional phone number); they are not an active service route.
- Secondary paths: Services → relevant Service Detail → Contact; Projects → Project Detail → Contact; Insights → Insight Detail → relevant Service or Contact.

### Page Visual Identity

| Page | Visual memory point | Dominant composition | Colour rhythm | Sibling difference | Status |
|---|---|---|---|---|---|
| Services | A direct service navigator with four work paths | Image-led masthead, linear navigator, ruled method ledger | Deep-navy opening, white navigator, substantial slate-blue method band, pale handoff | Overview and route selection | In progress; bounded visual evidence remains limited |
| Repair & Maintenance | Condition evidence leading into assessment and repair decisions | Composed around diagnosis, evidence and scope rather than repeat the Services topology | Soft-white masthead, mist assessment, deep-navy work scope, white sequence, mist FAQ and soft-white handoff | Detail journey, not another overview ledger | Structural Pass; bounded Desktop and Phone visual evidence Pass; stress and Preview remain |
| Roof Replacement | A considered decision about a complete roof rather than a repair scope | Broad roof-plane opening, text-first decision band, offset exterior-planning spread and horizontal handoff | Soft-white copy rail, mist decision band, soft-white spread, slate-blue sequence and deep-navy close | Whole-roof planning; does not repeat Services overview or Repair assessment/process topology | Structural and bounded Desktop visual Pass; stress and Preview remain |
| New Construction | A structure-taking-shape journey about project coordination and installation planning | Framing-image threshold, nested coordination brief, tall working field, continuous scope rail and detail band | Image/deep-navy opening, mist brief, slate-blue field, soft-white rail and deep-navy close | Emerging structure; does not repeat assessment, replacement decision or Services navigation topology | Structural and bounded Desktop visual Pass; stress and Preview remain |
| Storm Damage Repair | A calm response board that moves from damage context to an inspection conversation | Deep-navy response rail, condition field, documentation panel and narrow evidence band | Deep navy/mist opening, mist review, slate documentation, soft-white evidence, mist FAQ and deep-navy close | Response and documentation; does not repeat condition diagnosis, whole-roof planning or construction sequence | Structural and bounded Desktop visual Pass; stress and Preview remain |
| Projects | An editable work-record archive rather than a service journey | Restrained index opening, Demo record band, lead CMS record and uneven record field | Soft white, deep navy, soft white, mist and slate blue | Archive evidence; does not repeat Services navigation or any service-detail narrative | Structural and bounded Desktop visual Pass; stress and Preview remain |
| Project Detail | One editable record sheet rather than a finished case study | Image/deep-navy threshold, offset metadata sheet, Demo status strip, single image record and quiet close | Deep navy/image, soft white, mist, slate blue and soft white | Individual evidence record; does not repeat the archive field or service-detail sequence | Structural and bounded Desktop visual Pass; stress and Preview remain |
| About | A practical working-standard page, not a corporate story | Crew-image threshold, editorial standard, uneven principles field, editable people panel and quiet close | Deep navy/image, soft white, mist, slate blue and soft white | People and principles; distinct from archive and record-sheet composition | Structural Pass at Desktop, Tablet and Phone; Visual Blocked; stress and Preview remain |

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
| Services aerial masthead image | Top-down roof-condition overview | Services overview masthead | Services only in the current Canvas | Repair reuse is not approved without a recorded narrative reason | Existing broad aerial crop; no page-specific focal plan recorded | Retain on Services pending later review |
| `roofer on roof/roofer-ledge.webp` | Human inspection context and roof-edge condition | Repair assessment / inspection evidence | Repair & Maintenance masthead | Used as the page’s inspection-evidence masthead; not reused from Services | Centered portrait crop; Phone height structurally set to 420px | Used |
| `roofer on roof/roof-work.webp` | Active repair work and material handling | Repair work-scope evidence | Repair & Maintenance work scope | Used only for the deep-navy work-scope section | Centered portrait crop; Phone height structurally set to 360px | Used |
| `exterior/roof-detail.webp` | Material and condition detail | Repair maintenance / decision detail | Repair & Maintenance assessment | Used for the mist-grey condition-assessment section; future Insights reuse requires a distinct role | Centered landscape crop; Phone height structurally set to 280px | Used |
| `exterior/red-roof.webp` | Broad roof plane and complete-roof context | Roof Replacement opening | Roof Replacement image-plane masthead | Used for the page’s wide opening, not reused from Services or Repair | Centered broad crop; Phone keeps the image behind a semi-opaque copy rail | Used |
| `exterior/modern-home.webp` | Complete exterior context | Roof Replacement planning spread | Roof Replacement planning section | Used as a non-project-specific completed-exterior context; not a verified case study | Centered landscape crop; Phone follows decision copy | Used |
| `roofer on roof/shingle-install.webp` | Installation context | Roof Replacement handoff inset | Roof Replacement slate-blue handoff | Used only as an inset alongside Demo decision stages | Centered crop; Phone expands to a 340px contextual image | Used |
| `exterior/house-frame.webp` | Framed building context | New Construction opening | New Construction image threshold | Used only as the page’s structural opening, not as a completed project claim | Centered broad crop behind a deep-navy title band | Used |
| `roofer on roof/frame-ladder.webp` | Work alongside a roof frame | New Construction tall working field | New Construction slate-blue installation context | Used only for the structure-working section | Centered portrait crop; Phone places copy before a 420px contextual image | Used |
| `roofer on roof/roof-framing.webp` | Build-detail context | New Construction framing-detail band | New Construction narrow media punctuation | Used only as a full-width detail band; not a verified project result | Centered vertical crop; Phone height structurally set to 260px | Used |
| `storm damage roof/fire-damage.webp` | Damaged roof condition context | Storm Damage Repair opening | Storm Damage Repair response opening | Used only for the calm response-board opening; not a verified property or hazard claim | Centered image fill alongside the deep-navy response rail | Used |
| `storm damage roof/roof-damage.webp` | Damaged roof condition context | Storm Damage Repair documentation field | Storm Damage Repair documentation context | Approved alternate because the documented duplicate-role `storm-repair.webp` source is Missing | Centered portrait crop; Phone follows readable documentation copy | Used |
| `storm damage roof/storm-roof.webp` | Roof beneath changing weather | Storm Damage Repair evidence band | Storm Damage Repair condition-evidence band | Used as contextual evidence only, not proof of a visitor property or a verified project | Centered landscape fill; Phone retains the evidence after its copy | Used |

## 12. Current Status

- Current phase: Home is complete and Services remains in progress. Repair & Maintenance has bounded Desktop and Phone visual evidence; Roof Replacement, New Construction, Storm Damage Repair, Projects and Project Detail have Structural and bounded Desktop visual Pass. About, Contact, Insights and Insight Detail have Structural Pass with explicit visual/delivery limitations. All retain stress and Preview work.
- Active page / component: Shared Service Row, Article Card and Contact Submit hover implementation. Scoped Structural Pass at Desktop 1200 / Tablet 810 / Phone 390; visual and runtime acceptance are Blocked. Home uses shared Article Card with Compact on Phone; Home CMS card destinations and the seven enquiry CTA families are normalized. The [active request checklist](./checklist/site/2026-10-03-hover-implementation.md) owns the detailed Component contract and evidence. Existing page-wide stress/visual/delivery limitations remain; development-only `ScrollRevealText.tsx` / `/reveal-text-test` are excluded.
- Current blockers: Insights has no article-body field; its titles, categories, summaries and images remain Demo. The detail page’s fictional reference story is not CMS-specific editorial content; its visual review, 320px / 1440px stress widths and Preview remain pending. Contact's form recipient, delivery configuration, privacy terms, successful-submission Preview and visual review remain Blocked; clearly fictional Demo email and phone references are visible, but no real phone, email, address, service area or hours are claimed. About's sole Desktop visual-review result became unavailable during context interruption, so its visual status remains Blocked. Commercial image licensing, Marketplace Demo/Remix URLs and listing assets do not yet exist. The `Summit Roofing` / `SUBMIT ROOFING` mismatch and Reveal Text retain/remove decision remain unresolved.
- Next approved step: Focused live Preview acceptance for Hover → Leave, card/enquiry routing, Tab focus, Phone static/tap behavior and Reduced Motion. Native Hover screenshots are unsupported and the bounded Phone screenshot download failed; no UI fallback is authorized. Optional informational hovers remain deferred. After this Part, resume outstanding page visual/stress/delivery audits; image licensing and explicit approval still block publication.
- Last verified: 2026-10-03 — official Framer Agent targeted before/after readback verifies the active shared-hover scope, all 21 enquiry destinations, Home CMS-slug links, archive Default selection and preserved form binding/input focus. Button, Project Card, Navbar/Footer and Method Ledger effects are preserved. Non-publishing readiness Preview returned ready, zero errors and zero warnings; this is not runtime or launch acceptance.

| Page | Content | Styles | Components | Links | SEO | Alt | Desktop | Tablet | Phone | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| Home | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Targeted readback, 390px bounded preview, 320px stress scan, readiness preview: 0 errors / 0 warnings |
| Services | Demo | ✓ | ✓ | Partial | ✓ | ✓ | ✓ | ✓ | ✓ | Four distinct Sections; unique Desktop/Phone Service Rows, 810px Tablet flow, specific masthead Alt and one bounded Desktop masthead screenshot; final detail links, 320/1440 review and full-page Preview remain blocked/deferred |
| Repair & Maintenance | Demo | ✓ | Reused | Partial | ✓ | ✓ | ✓ | ✓ | Structural Pass; Desktop and Phone visual evidence Pass. Stress widths and final Preview remain pending; Services repair-row link is live. |
| Roof Replacement | Demo | ✓ | Reused | Partial | ✓ | ✓ | ✓ | ✓ | Structural and bounded Desktop visual Pass; stress widths and Preview remain pending; Services roof-replacement row is live. |
| New Construction | Demo | ✓ | Reused | Partial | ✓ | ✓ | ✓ | ✓ | Structural and bounded Desktop visual Pass; stress widths and Preview remain pending; Services new-construction row is live. |
| Storm Damage Repair | Demo | ✓ | Reused | Partial | ✓ | ✓ | ✓ | ✓ | Structural and bounded Desktop visual Pass; stress widths and Preview remain pending; Services storm-damage row is live. |
| Projects | Demo | ✓ | Reused | ✓ | ✓ | ✓ | ✓ | ✓ | Structural and bounded Desktop visual Pass; stress widths and Preview remain pending; CMS record wrappers link to matching Project Detail items. |
| About | Demo | ✓ | Reused | ✓ | ✓ | Partial | ✓ | ✓ | Structural Pass; Visual Blocked after the sole Desktop image result became unavailable; 320/1440 stress, Preview and rendered Alt checks remain. |
| Contact | Missing / Demo | ✓ | Reused + page-owned submit | ✓ | ✓ | N/A | ✓ | ✓ | Structural Pass; form recipient/delivery, privacy, successful-submission Preview, visual review and 320/1440 stress remain Blocked. |
| Insights | Demo | ✓ | Reused | ✓ | ✓ | CMS-owned | ✓ | ✓ | Structural Pass; CMS image/category/title/summary bindings are live and each item reaches the matching Insight Detail route. Visual review, 320/1440 stress and Preview remain pending. |
| Insight Detail | Demo / Missing | ✓ | Reused | ✓ | ✓ | CMS-owned | ✓ | ✓ | Structural Pass; CMS Category/Title/Summary/Image bindings, article-body limitation note and Services CTA are live. Visual review, 320/1440 stress and Preview remain pending. |
| Project Detail | Demo | ✓ | Reused | ✓ | ✓ | ✓ | ✓ | ✓ | Structural and bounded Desktop visual Pass; stress widths and Preview remain pending; Projects CMS record wrappers link to matching detail items. |

## 13. Decisions and Exceptions

| Decision | Reason | Scope | Status | Date | Supersedes |
|---|---|---|---|---|---|
| Use Baker Roofing as the close visual benchmark | Earlier interpretation treated the reference too literally and included its color direction | Home visual system | Superseded | 2026-08-23 | Earlier loose “informed by” direction |
| Use safety red as a primary brand surface | Earlier color proposal; user explicitly replaced it with a blue-grey direction | Home color system | Superseded | 2026-08-23 | Earlier “red accent” wording |
| Use Baker Roofing as a style and layout reference, not a structural blueprint | Preserve the reference's clean hierarchy and trade-industry confidence while keeping Summit's section order, proportions, grids and spacing original | Home visual system | Active | 2026-08-23 | Close visual benchmark decision |
| Use an independent blue-grey palette | User explicitly rejected red and selected grey and blue; slate blue provides roofing/material character without reading as generic tech branding | Home color system | Active | 2026-08-23 | Safety-red primary decision |
| Use zero-radius geometry | User explicitly rejected rounded corners; square edges better match the approved industrial reference | All Home Components and surfaces | Active | 2026-08-23 | Earlier allowance for restrained rounding |
| Fill empty template slots with fictional reference content when explicitly authorized | User directed the template to use complete, coherent reference content instead of visible publishing / verification instructions. Emails use `.example`; phone numbers use reserved fictional formats; stories remain internally `Demo` and never imply verified operations, credentials, legal terms, pricing or real locations. | All buyer-facing template content | Active | 2026-10-02 | Treat service facts and contact details as Missing |
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

- Current copy-repair checkpoint: 2026-10-03 — repository `/Users/Zhuanz/Desktop/Business/Website_Lab/`; official Framer Agent session 7 reused. Corrective [instructional-copy checklist](./checklist/site/2026-10-03-instructional-copy-repair.md) saved before writes. Live audit and replacement mapping cover 103 authored blocks / 309 responsive copies; no bound-CMS text targets or differing replica copy. Next: in-place replacements, fresh re-scan and non-copy preservation checks. Prior [hover acceptance](./checklist/site/2026-10-03-hover-implementation.md) remains visual/runtime Blocked; no publication.
- Image Review Plan: 2026-10-03 shared-hover implementation — maximum three bounded single-node screenshots, one view each: Article Hover (border/title/mask legibility), Home Phone Article wrapper (18px padding / 220px image preserved after shared-instance migration), Contact Submit Hover (white label legible on navy without size change). No asset reopening or whole-page screenshots. On failure stop that visual chain and record structural evidence only; actual pointer/focus/touch/Reduced Motion need runtime evidence and are not proven by static screenshots.
- Image Review Result: 2026-10-03 shared-hover implementation — Article native Hover screenshot was rejected with `Variant node must be a top-level variant`. Home Phone article screenshot was generated (`https://framerusercontent.com/screenshots/on-demand/5babae7c-b9e2-4e5e-9b82-ddaa26e5b1f7.jpg`), but its bounded download failed with `LibreSSL SSL_ERROR_SYSCALL`; no image was viewed and no visual Pass is inferred. The failed visual chain is stopped; Contact Hover capture is omitted because it uses the same unsupported gesture-state capture. Structural checks and contrast calculation continue; live Preview confirmation remains required.
- Current opening adaptation checkpoint: Complete, 2026-10-03 — official Framer Agent session 7. Roof Replacement Desktop/Tablet opening now uses the user-approved Phone full-image / 70% Soft White overlay composition; height 740px, heading/body gap 10px, Desktop gutters 64px with 880px copy-group cap, Tablet gutters 32px. Three bounded Section screenshots were each reviewed once: Phone reference (`a0d48586-b3c4-4a53-937f-64efc7b856f3.jpg`), Desktop result (`64368658-5389-4287-a9d5-56055aed6557.jpg`) and Tablet result (`127e7cf0-e76e-494e-8919-7168178dcfc8.jpg`). Targeted structural and visual Pass at 1200/810; Phone design/content values, imagery, CTA destination and adjacent decision-band layout/content are preserved. Framer normalized relative-position metadata during rendering. `getRect` returned placeholder-like 200px widths and was not used as rendered-fit evidence. Whole-page stress/Preview remain pending; see [Roof Replacement Checklist](./checklist/roof-replacement.md).
- Active session / connection: Official Framer Agent session connected on 2026-09-18 for Project Detail build, archive destinations and targeted readback. No publication action is authorized or claimed.
- Image Review Plan: 2026-09-16 Roof Replacement build — inspect one bounded Desktop Canvas screenshot after all Sections and Desktop/Table/Phone structures are written. The sole question is whether the page’s roof-plane opening, planning spread, slate-blue horizontal handoff and allocated image roles establish the approved sibling-page delta. Maximum visual attempts: one screenshot. If unavailable or insufficient, stop visual review and record Structural Pass / Visual Blocked from Fill, Alt, Rect, Section and breakpoint evidence. No original asset image will be visually reopened; user-allocated files were already resident and dimension-verified before upload.
- Image Review Plan: 2026-09-17 Roof Replacement visual QA — inspect one newly generated, bounded Desktop Canvas screenshot after the opening headline shortening. The sole question is whether the corrected copy rail now keeps the H1 fully legible while preserving the distinct roof-plane / planning-spread / slate-blue-handoff narrative. Maximum visual attempts: one screenshot. If the screenshot is unavailable or cannot answer that question, stop and retain Visual Blocked; do not repeat the 2026-09-16 screenshot or reopen supplied assets.
- Image Review Result: 2026-09-16 Repair build — reviewed one Services Desktop screenshot and one Repair Desktop screenshot. Repair passes Desktop sibling differentiation: light split masthead with `roofer-ledge.webp`, mist assessment with `roof-detail.webp`, deep-navy work scope with `roof-work.webp`, vertical sequence and ruled FAQ do not repeat the Services dark masthead / service index / blue ledger sequence. The two-image budget is exhausted; Phone visual evidence is pending and must not be inferred from structural readback.
- Image Review Result: 2026-09-16 Repair QA continuation — one Phone screenshot passed: reading order is single-column, the three image crops remain legible, the primary CTA is visible, and the page does not regress into the Services overview/ledger composition. The one-image QA budget is exhausted.
- Image Review Result: 2026-09-16 Roof Replacement build — one Desktop screenshot (`https://framerusercontent.com/screenshots/on-demand/27cd874f-0d78-453c-a549-1ef2c5c38bc7.jpg`, stored temporarily as `roof-replacement-desktop-review.jpg`) established distinct roof-plane, decision-band, planning-spread and slate-blue-handoff composition with the three allocated images. It also exposed a clipped opening headline. The headline was shortened in the live Canvas; do not infer final visual Pass without a separately budgeted follow-up screenshot. The Roof Replacement visual budget is exhausted for this Part.
- Image Review Result: 2026-09-17 Roof Replacement visual QA — one new Desktop screenshot (`https://framerusercontent.com/screenshots/on-demand/cbd815c4-bb72-4e5c-85f6-358d6cd06810.jpg`, stored temporarily as `roof-replacement-qa-desktop-review.jpg`) passes the corrected opening: the shortened H1 is fully legible in the copy rail, all three allocated image roles remain clear, and the roof-plane / planning-spread / slate-blue-handoff rhythm remains distinct from Services and Repair. The one-image QA budget is exhausted.
- Image Review Plan: 2026-09-17 New Construction build — after structural writing, inspect one bounded Desktop Canvas screenshot. The sole question is whether the framed opening, tall ladder field, continuous scope rail and narrow framing-detail band form the approved emerging-structure narrative without repeating the preceding service pages. Maximum visual attempts: one screenshot. If it is unavailable or insufficient, stop visual review and retain Structural Pass / Visual Blocked from Fill, Alt, Rect, Section and breakpoint evidence. Do not reopen the three supplied source assets; they were resident and dimension-verified before upload.
- Image Review Plan: 2026-09-17 Storm Damage Repair build — after structural writing, inspect one bounded Desktop Canvas screenshot. The sole question is whether the deep-navy response rail, condition field, slate documentation field and narrow evidence band establish the approved calm response-board narrative without alarmist or duplicate sibling composition. Maximum visual attempts: one screenshot. If it is unavailable or insufficient, stop visual review and retain Structural Pass / Visual Blocked from Fill, Alt, Rect, Section and breakpoint evidence. Do not reopen supplied source assets; `storm-repair.webp` is Missing at its documented path, so only the approved `roof-damage.webp` alternate may be used.
- Image Review Result: 2026-09-17 New Construction build — one Desktop screenshot (`https://framerusercontent.com/screenshots/on-demand/6646051d-b5e7-48da-8818-3bea0e9c3964.jpg`, stored temporarily as `new-construction-desktop-review.jpg`) passes the approved composition: the deep-navy title threshold over `house-frame.webp`, mist coordination brief, slate-blue ladder field, continuous soft-white scope rail and narrow `roof-framing.webp` band establish a distinct emerging-structure journey. The one-image visual budget is exhausted for this Part.
- Image Review Result: 2026-09-17 Storm Damage Repair build — one Desktop screenshot (`https://framerusercontent.com/screenshots/on-demand/281c388f-df0e-4bfa-9d10-89dcb8ea06ca.jpg`, stored temporarily as `storm-damage-desktop-review.jpg`) was generated and reduced for the planned review, but the visual result became unavailable during context interruption. No visual inference is recorded and the one-image build budget is exhausted; a later visual check needs a separately scoped QA Part.
- Image Review Plan: 2026-09-17 Storm Damage Repair visual QA — inspect one newly generated, bounded Desktop screenshot. The sole question is whether the response rail, condition field, documentation field and evidence band form the approved calm response-board rhythm without alarmist treatment or duplicating the other service pages. Maximum visual attempts: one screenshot. If unavailable or insufficient, retain Structural Pass / Visual Blocked; do not repeat the build-Part screenshot or reopen supplied source assets.
- Image Review Result: 2026-09-17 Storm Damage Repair visual QA — one Desktop screenshot (`https://framerusercontent.com/screenshots/on-demand/69ea22d0-4b52-41a8-a98d-9bc36803f7e6.jpg`, stored temporarily as `storm-damage-qa-desktop-review.jpg`) passes: the deep-navy response rail, large condition field, slate documentation field, soft-white evidence band and quiet close form the approved calm response-board rhythm. The composition is distinct from the other service pages and does not introduce alarmist treatment. The one-image QA budget is exhausted.
- Image Review Plan: 2026-09-18 Projects build — inspect one bounded Desktop Canvas screenshot after structural writing. The sole question is whether the index opening, Demo-record band, lead CMS record and uneven remaining-record field read as the approved editable archive rather than a service journey or generic card wall. Maximum visual attempts: one screenshot. If unavailable or insufficient, retain Structural Pass / Visual Blocked; do not reopen CMS item images or capture another state in this Part.
- Image Review Result: 2026-09-18 Projects build — one Desktop screenshot (`https://framerusercontent.com/screenshots/on-demand/3a44a1ed-3134-4072-954d-c86161aaebe9.jpg`, stored temporarily as `submit-roofing-projects-desktop-review.jpg`) passes: the strong soft-white index opening, explicit deep-navy Demo record band, single lead CMS record and uneven remaining-record field read as an editable archive rather than a service journey or generic card wall. The one-image visual budget is exhausted for this Part.
- Image Review Plan: 2026-09-18 Project Detail build — inspect one bounded Desktop Canvas screenshot after structural writing. The sole question is whether the image/deep-navy record threshold, offset metadata sheet, explicit Demo-status strip, single-image editing note and quiet close read as an individual editable record sheet rather than a finished case study, archive field or service journey. Maximum visual attempts: one screenshot. If unavailable or insufficient, retain Structural Pass / Visual Blocked; do not reopen CMS item images or capture another state in this Part.
- Image Review Result: 2026-09-18 Project Detail build — one Desktop screenshot (`https://framerusercontent.com/screenshots/on-demand/e2abcf03-edcb-4027-aee9-39b8029ee84e.jpg`, stored temporarily as `submit-roofing-project-detail-desktop-review.jpg`) passes: the image/deep-navy record threshold, offset metadata sheet, explicit Demo-status strip, single-image editing note and quiet close read as a focused editable record sheet. The composition is distinct from the Projects archive and service-detail narratives, and it does not imply a completed case study. The one-image visual budget is exhausted for this Part.
- Image Review Plan: 2026-09-18 About build — inspect one bounded Desktop Canvas screenshot after structural writing. The sole question is whether the crew-work threshold, working-standard statement, principles field, editable people panel and quiet close read as a practical people-and-principles page rather than a corporate timeline or claims page. Maximum visual attempts: one screenshot; if unavailable, retain Structural Pass / Visual Blocked.
- Image Review Plan: 2026-09-18 Contact responsive gap repair — inspect one bounded Phone Request Workspace screenshot after converting the one-column grid to a vertical Stack. The sole question is whether the form follows the explanatory copy after the intended 36px gap, with no empty grid track. Maximum visual attempts: one screenshot; if unavailable, retain structural verification only and record Visual Blocked.
- Image Review Result: 2026-09-18 Contact responsive gap repair — one Phone workspace screenshot (`https://framerusercontent.com/screenshots/on-demand/2a7d3f06-f0eb-400e-851b-d82d770cfb96.jpg`) was generated but could not be inspected in this workspace. No visual inference is recorded. Targeted readback confirms the final implementation uses a nested Desktop two-column sequence, a 48px Tablet vertical sequence and a 36px Phone vertical sequence; the prior one-column grid track no longer owns the responsive layout.
- Image Review Result: 2026-09-18 About build — one Desktop screenshot (`https://framerusercontent.com/screenshots/on-demand/ddde18b7-a31d-4d40-9603-3db78922926d.jpg`, reduced temporarily as `about-review.jpg`) was captured, but its review output became unavailable when the image view was truncated during context interruption. No visual inference is recorded. The one-image Part budget is exhausted; later visual QA needs a separately scoped Part.
- Image Review Plan: 2026-09-19 Insight Detail build — inspect one bounded Desktop Canvas screenshot only in a separately scoped visual-QA Part. The sole question is whether the deep-navy article threshold, soft-white summary rail, mist explicit body-limit note and slate-blue service handoff read as a distinct editable article record rather than a duplicated archive or Project Detail case-study sheet. Maximum visual attempts: one screenshot. If unavailable or insufficient, retain Structural Pass / Visual Blocked; do not reopen CMS item images or create new article content.
- Current page / component: Insight Detail is live at `/insights/:slug`, with a deep-navy article threshold, soft-white reading record, mist editable-content note and slate-blue service handoff. It binds only the current Insights Category, Title, Summary and Image values and makes the missing body explicit; the `/insights` repeat wrapper links each card to its matched detail record.
- Last successful change: 2026-09-19 — created the CMS-owned Insight Detail route, added its Tablet and Phone breakpoint replicas, and connected the existing archive wrapper to the valid dynamic destination. No CMS schema/item, Article Card definition, Custom Code or publication changed.
- Last targeted readback: `/insights/:slug` is associated with the Insights collection and has one H1, three H2s, four semantic Sections, Site Shell metadata, bound Category/Title/Summary/Image values, `/services` CTA and independent Desktop 1200 / Tablet 810 / Phone 390 owners. `/insights` wrapper has `/insights/:slug` plus the active CMS slug.
- Verified breakpoints / states: Insight Detail Desktop 1200, Tablet 810 and Phone 390 structural Pass; Visual Blocked. 320px / 1440px and Preview remain deferred. Insights archive navigation structural Pass; its visual/stress/Preview status remains unchanged.
- Remaining approved work: Complete separately scoped visual/stress QA across Insights archive/detail, Contact and About. All prior completed pages retain stress/Preview checks.
- Exact next action: Run bounded visual/stress QA for the Insights archive/detail pair without changing CMS schema or shared systems.
- Important local asset paths: `/Users/Zhuanz/Desktop/Submit Roofing/`
- Updated at: 2026-09-19

## 15. Checklist and Change Control

- Project checklist index: [checklist/README.md](./checklist/README.md)
- Active page checklist: [Insight Detail Checklist](./checklist/insight-detail.md) — Structural Pass / Visual Blocked; archive navigation is structurally complete.
- Active request checklist: [approved site expansion plan](./checklist/site/2026-08-26-site-expansion-planning.md)
- Checklist status: Project-wide plan Approved; Services remains in progress; all completed pages retain outstanding stress/Preview checks; About is Structural Pass / Visual Blocked; Contact is Structural Pass / delivery and visual Blocked; Insights archive and Insight Detail are Structural Pass / Visual Blocked; publishing excluded.
- Last synchronization with Current Status: 2026-09-19

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
