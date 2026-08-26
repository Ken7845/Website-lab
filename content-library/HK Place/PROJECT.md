# HK Place — Project Manifest

## 1. Project Identity

- Project name: HK Place
- Platform: Framer
- Project type: Cold-outreach concept landing page
- Overall status: Ready for review — Home complete, unpublished
- Project / Canvas URL: https://framer.com/projects/Comfortable-Department--Aw0doKPVzcEKwIcp3vZl-fBmRA?duplicate=starter-template-empty-site&node=augiA20Il
- Demo URL: Missing — do not publish without approval
- Content status: Mixed — restaurant facts and supplied images are Approved sources; marketing copy is Demo
- Last updated: 2026-08-18
- Last verified against current implementation: 2026-08-18, complete Home across Desktop, Tablet and Phone

## 2. Scope and Authority

- Current scope: Design and build the complete Home page only, with reusable foundations and visible routes/CTAs for future pages.
- Explicit non-goals: Do not build other full pages, publish, connect a domain, add paid dependencies, or use Custom Code.
- Primary page / component: Home `/`; Button, Dish Highlight and Review Quote foundations only where repetition justifies them.
- User-approved direction: Confirmed on 2026-08-18; begin full Home implementation.
- Current implementation differences: None within the approved Home scope. Future pages remain intentionally unbuilt.
- Items requiring confirmation: Complete weekly opening hours, formal logo/favicon artwork and public-use rights before any public launch.

## 3. Knowledge Map

| Responsibility | Current source | Status |
|---|---|---|
| Brand Voice | Derived from authentic, friendly, good-value review language in `basic-info/basic-information.txt` | Draft |
| Style Guide | This manifest §6 and active Home checklist | Draft |
| Formal Content | `basic-info/basic-information.txt` and menu screenshots | Approved source / transcription pending |
| Assets | `dishes/`, `exterior/`, `menu/`, `basic-info/` | Approved source |
| Inspiration | `inspiration/restaurant/balkan-bakery/`, `june-on-cambie/`, `nirvana-on-vitoria/` | Principles only; no copying |
| Current Status | Inline §12 | Active |
| Decisions | Inline §13 | Active |
| Recovery | Inline §14 | Active |
| Checklist index | `checklist/README.md` | Active |
| History index | Missing | Not required yet |

## 4. Website Goal

- 网站为谁服务？ Brighton diners seeking approachable, authentic Hong Kong-style food, and the restaurant owner reviewing the cold-outreach concept.
- 用户进入后需要理解什么？ What HK Place serves, where it is, why diners trust it, and how to view the menu, call, or get directions.
- 最重要的实际结果： Move a visitor from appetite and trust to menu, phone, or visit action.
- Primary CTA: View Menu.
- Secondary CTA: Get Directions / Call HK Place.
- Success evidence: Clear first-screen comprehension, visible conversion actions, readable mobile layout, and no broken destination.

## 5. Target User

- Primary audience: Local diners, visitors to Brighton, students and value-conscious customers.
- User intent: Decide quickly whether the food, price and location fit; then view menu, call or visit.
- Important questions: What cuisine? Where? What are the signature dishes? Is it well reviewed? How much does it cost? How do I order or visit?
- Trust requirements: Real food imagery, authentic review excerpts, rating count, address, phone and clear Demo status.
- Device priority: Balanced, with Phone conversion paths treated as essential.

## 6. Brand Direction

- Brand personality: Direct, warm, lively, unpretentious and food-first.
- Core concept: “Brighton meets a Hong Kong neighbourhood café” — graphic signboard energy balanced with generous editorial spacing.
- Visual memory point: Condensed signboard typography, lacquer-red navigation/CTA, rice-paper cream surfaces and asymmetric food imagery.
- Typography direction: Big Shoulders for display headings; Fira Sans for body, navigation and UI.
- Color direction: Rice-paper cream base, ink charcoal text, lacquer red as dominant action color, restrained jade-green secondary tone, limited sharp yellow accent.
- Image strategy: One dominant dish/exterior image per narrative beat; varied editorial ratios; menu screenshots remain facts sources rather than primary website imagery.
- Motion character: Short native fades and image-scale hover only; restrained, readable and reduced-motion aware.
- Avoid: SaaS cards, generic dark gradients, glassmorphism, tiny text, fake awards, fabricated menu details, random equal image grids and decorative motion.

## 7. Content Facts

| Fact | Value | Source | Status |
|---|---|---|---|
| Address | 37 Preston St, Brighton and Hove, Brighton BN1 2HP, United Kingdom | `basic-info/basic-information.txt` | Approved |
| Phone | +44 7577 196494 | `basic-info/basic-information.txt` | Approved |
| Email | Missing | — | Missing |
| Opening hours | Opens at 11:30 AM; complete weekly hours not supplied | `basic-info/basic-information.txt` | Partial / do not invent |
| Menu website | hkplace.co.uk | `basic-info/basic-information.txt` | Approved |
| Google rating | 4.8 / 5 from 703 reviews | `basic-info/basic-information.txt` | Approved snapshot |
| Typical spend | £10–20, based on 344 responses | `basic-info/basic-information.txt` | Approved snapshot |
| Highlight dishes | Beef brisket, wonton noodles, roast duck | `basic-info/basic-information.txt` | Approved mention |
| Legal / copyright | Missing | — | Missing; concept must not imply commission or endorsement |

## 8. Sitemap and Page Goals

| Page | Path | User goal | Primary CTA | Content source | Current status |
|---|---|---|---|---|---|
| Home | `/` | Understand, trust and act | View Menu | HK Place content library | Pass — unpublished |
| Menu | Future / external handoff | Browse complete menu | View Menu | hkplace.co.uk / screenshots | Reserved only |
| About | Future | Learn more about HK Place | About HK Place | Missing story facts | Reserved only |
| Reviews | Future or Home anchor | Validate quality and value | Read Reviews | Approved review source | Reserved only |
| Visit | Future or Home anchor | Call or navigate | Get Directions | Approved address/phone | Reserved only |

## 9. Narrative and Conversion

| Page | Section / Part | Purpose | Content source | Image role | CTA / next step |
|---|---|---|---|---|---|
| Home | Navigation | Orient and expose conversion path | Approved facts | Wordmark/signboard treatment | Menu / Reviews / Visit |
| Home | Hero | Explain cuisine, location and next action in ten seconds | Approved facts + Demo copy | Dominant signature dish or storefront | View Menu / Get Directions |
| Home | Trust Strip | Establish rating, value and speed | Approved facts/reviews | Minimal | Continue to food |
| Home | Restaurant Introduction | Frame HK Place as authentic and welcoming | Review summary + address | Exterior or counter/service image | About HK Place reserved route |
| Home | Menu Highlights | Showcase three verified signature dish categories | Approved review summary | Three distinct food images | Full Menu |
| Home | Food Gallery | Build appetite and variety without a templated grid | Supplied dishes | Asymmetric editorial sequence | Explore Menu |
| Home | Reviews | Prove friendliness, speed, flavour and value | Supplied quotations | Optional small supporting dish | Visit / Call |
| Home | Visit Us | Make location and contact effortless | Address, phone, menu URL | Storefront | Directions / Call |
| Home | Closing CTA | Resolve final action | Approved destinations | Graphic color field | View Menu |
| Home | Footer | Provide routes, contact and Demo disclosure | Approved facts | None | Future routes reserved |

Primary path:

```text
Land → Understand cuisine and location → See signature dishes → Trust reviews → View menu / call / visit
```

## 10. System and Platform Plan

- Platform router: `framer/README.md` and official Framer task map.
- Selected Skills: Design Taste for art direction; Framer Components for reusable foundations; Framer Layout and Responsive for page composition; Framer QA for final audit.
- Text / Color Style source: Semantic Framer Styles created from §6.
- Shared Components: Button, Dish Highlight, Review Quote; Navbar/Footer remain page-local unless future-page reuse is introduced now without duplication.
- CMS decision: No CMS for the current one-page Demo; content volume is small and facts are not independently managed.
- Navbar / Footer: Simple, recognizable, semantic layers; future page routes remain visible but no broken internal links.
- Links and semantics: Existing external menu, `tel:` and map destination; Home anchors for sections until future pages exist.
- Accessibility / Focus: One h1, ordered h2/h3, visible focus, adequate hit areas, truthful alt text, keyboard-safe links.
- Third-party dependency: None.
- Custom Code: No.

## 11. Responsive, Interaction and Assets

| Area | Desktop | Tablet | Phone |
|---|---|---|---|
| Navbar | Full routes + CTA | Reduced routes + CTA | Compact bar; essential actions visible |
| Hero | Split editorial composition | Reduced split / controlled crop | Single-column, text first, image second |
| Main layout | Asymmetric image rhythm | Simplified two/one-column flow | Single-column reading order |
| Footer | Multi-column | Two-column | Stacked with phone/menu actions first |
| Special interaction | Subtle hover and reveal | Touch-safe | No hover dependency |

- Required test widths: 320, 390, 810, 1200 and 1440+.
- Page / section enter: Subtle native opacity/y shift, no essential content delay.
- Hover / pressed: Button fill/contrast change; inner image scales slightly inside clipped frame.
- Overlay / Lightbox: Deferred unless a gallery interaction is justified after layout proof.
- Reduced Motion: Remove transforms and shorten/disable non-essential reveals.
- Source asset folder: `content-library/HK Place/`.
- Web output folder: Missing; create only if asset optimization is required.
- Hero / gallery assets: Selection recorded in the active Home checklist after implementation.
- Missing assets: Logo artwork, complete opening hours, formal story, social links and rights statement.
- License status: User-supplied for private concept work; public-use rights not verified.

## 12. Current Status

- Current phase: Ready for client review; requested detail revision passed targeted QA.
- Active page / component: Home `/`.
- Current blockers: Favicon/logo artwork and complete weekly hours are not supplied; neither was fabricated. Public-use rights remain unverified.
- Next approved step: Client review. Publishing remains outside scope until explicitly approved.
- Last verified: 2026-08-18 — detail readback confirms no remaining `maxWidth` attributes on page layout nodes, a filled Tablet 2×2 dish grid, 212px Tablet review instances and working three-breakpoint Call Us treatments.

| Page | Content | Styles | Components | Links | SEO | Alt | Desktop | Tablet | Phone | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| Home | ✓ | ✓ | ✓ | ✓ | ✓* | ✓ | ✓ | ✓ | ✓ | Live tree readback + Desktop/Phone visual QA |

\* Page title, description, Open Graph image and no-index Demo protection pass. Favicon is evidence-backed Blocked because logo artwork was not supplied.

## 13. Decisions and Exceptions

| Decision | Reason | Scope | Status | Date | Supersedes |
|---|---|---|---|---|---|
| Build Home only; reserve future routes without broken links | Minimize cold-outreach production cost | Project | Active | 2026-08-18 | — |
| Use content-library facts only | Prevent fabricated restaurant claims | Project | Active | 2026-08-18 | — |
| Treat menu screenshots as facts sources, not hero visuals | Preserve readability and visual quality | Home | Active | 2026-08-18 | — |
| Keep the concept unpublished and no-indexed | Publishing was not authorized and the concept is unofficial | Project | Active | 2026-08-18 | — |
| Accept Phone stack diagnostics as a Framer replica-measurement false positive | Targeted screenshots show correct spacing; the replica API returns placeholder geometry for the affected roots | Home | Accepted exception | 2026-08-18 | — |
| Keep outer and near-outer layout Stacks fluid | A broad `max-width` on the first inner Stack restricted Desktop response; constrain only the deepest content owner that truly needs it | Home / cross-project lesson | Active | 2026-08-18 | — |

## 14. Recovery

- Active session / connection: Connected Framer session for HK Place project.
- Current page / component: Home `/`; Button, Dish Highlight and Review Quote components.
- Last successful change: Added Closing CTA light-border treatment, filled the Tablet Menu grid with a verified Wonton Lo Mein instance, reduced Tablet Review Quote height, and removed outer/near-outer Stack max-width constraints.
- Last targeted readback: Affected CTA, Menu and Review nodes across Desktop/Tablet/Phone; page-wide `maxWidth` inventory is empty.
- Verified breakpoints / states: Desktop 1200+, Tablet 810–1199.98, Phone through 809.98; Button primary/secondary and hover states.
- Remaining approved work: None. Keep unpublished pending explicit approval.
- Exact next action: Client review; optionally supply logo/favicon and complete weekly opening hours.
- Important local asset paths: `content-library/HK Place/basic-info`, `dishes`, `exterior`, `menu`.
- Updated at: 2026-08-18.

## 15. Checklist and Change Control

- Project checklist index: `checklist/README.md`
- Active page checklist: `checklist/home.md`
- Active request checklist: `checklist/home/2026-08-18-homepage-cold-outreach-build.md`
- Checklist status: Pass
- Last synchronization with Current Status: 2026-08-18

## 16. History

- History index: Not created.
- Closed prompt / handoff records: None.
- Superseded plans worth retaining: None.

## 17. Definition of Ready

- [x] Current Scope and non-goals are explicit.
- [x] Website goal, target user and Home purpose are explicit.
- [x] Primary CTA and conversion path are explicit.
- [x] Brand direction and minimal Inspiration sources are explicit.
- [x] Formal facts have sources and Missing facts remain Missing.
- [x] Supplied content and assets are sufficient for a Home concept.
- [x] Current implementation differences are recorded.
- [x] Active request checklist is confirmed by the user.
