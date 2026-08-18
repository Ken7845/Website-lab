# AURELIA Marketplace Release Readiness Audit

Audit date: 2026-08-16  
Canvas source of truth: Framer project `AURELIA` (`6EYvZfFo1CleDR77cYUF`), session `9`  
Scope: all active pages, shared systems, Components, assets, semantics, responsive and interaction QA, buyer editability, Marketplace listing, launch distribution, and post-launch maintenance.  
Constraint: this is an execution plan only. No Canvas, publishing, pricing, payment, or external-service mutation was authorized in this audit.

This file supersedes its earlier canvas-only scope. It remains the single current Marketplace release checklist; do not create a parallel readiness file.

## Executive result

Status: **Fix Required — do not publish yet**

Provisional overall readiness: **55 / 100**. This is a structural and operational score, not a prediction of Marketplace rank. Visual quality, browser behavior, keyboard use, motion preferences, performance, licenses, Demo/Remix URLs, and listing media still require evidence.

| Dimension | Score | Current evidence | Main release gap |
|---|---:|---|---|
| Framer template standard | 61 / 100 | Six active pages including a custom 404; shared Template and reusable systems; authored Desktop/Tablet/Phone layouts | `/chefs` metadata, page semantics, responsive/interaction regression, Focus/Reduced Motion, performance and licensing |
| Buyer editability | 64 / 100 | Shared Styles; 14 local Components; useful text/image Properties; fixed seven-dish systems are intentionally bounded | Alt ownership is incomplete; generic Hero/Hero Loader variants and 13 meaningful unnamed/default layers remain; no buyer editing guide or recorded replacement stress test |
| Marketplace discovery readiness | 24 / 100 | Original, coherent restaurant/supper-club positioning exists | Demo URL, Remix URL, listing copy, categories/features, first-position video, screenshots, support statement, favicon and OG cover are not ready |

Weighted score: template standard 45%, buyer editability 35%, discovery readiness 20%. Re-score only after closing the evidence gates below; Framer does not publish exact ranking weights, so this score must never be presented as an algorithm forecast.

## Live structural baseline

Read back from the Canvas on 2026-08-16:

- Active pages: `/`, `/menu`, `/about`, `/chefs`, `/reserve`, `/404`.
- Metadata: all six pages have title/description; `/404` is no-indexed.
- Breakpoints: the five primary pages cover Desktop/Tablet/Phone; `/chefs` also has a 599–809px Wide Phone range.
- Local Components: 14. Site instances include 14 Buttons, 21 MenuDishCard replicas, 12 ChefStoryRow replicas, 12 EveningChapterRow replicas, 10 Reservation Handoff replicas, eight FAQ Row instances, shared Navigation/Footer, and the reservation submit system.
- Button hygiene is now **Pass**: only the eight descriptive diagonal states remain (`White/Dark`, standard/small, base/hover); the old horizontal-fill variants are absent.
- MenuDishCard now exposes `Image Alt`; the earlier claim that it lacked an Alt Property is retired. The seven current page instances inherit the component default and must still be tested after replacement.
- Home Hero now has descriptive Alt text; `ChefStoryRow`, `DishSelector`, and `EveningChapterRow` expose paired editable Alt Properties. `ChapterCursorPreview` still needs an explicit decorative-image decision.
- `hero` and `Hero Loader` now use descriptive state names. The remaining unnamed/default layer audit is limited to page-local or non-buyer-facing internals after the component subset was named.
- Shared style inventory contains intentional `Type/...` presets plus similarly named unprefixed presets that require usage readback before cleanup. Color tokens include `Color/red`, whose production ownership is not yet proven.
- No CMS Collection exists. This is acceptable for the approved fixed seven-dish concept only if buyer replacement testing and editing instructions prove the model is easy to maintain.
- Reserve contains native name, email, message, preferred date, party size, and booking type inputs. Production submission, privacy and service behavior remain blocked by missing product facts.

## Marketplace recommendation model — what the checklist can influence

Framer states that Marketplace ranking can consider views, comments, likes, remixes, previews, purchases, account health, and other meaningful activity. No single signal guarantees rank, exact weights are private, and freshness changes over time. Therefore the executable strategy is:

1. Ship a useful, original, polished and accurately described product.
2. Make the first listing media asset strong; use video because visual media is required for Hype and video is generally the strongest format.
3. Use clear search language, accurate categories/styles/features, and a specific audience/problem statement.
4. Reduce Preview-to-Remix friction with a fast Demo, a valid Remix link, clear buyer instructions, and honest limitations.
5. Launch with a contextual Community post, invite genuine feedback, reply to comments, and keep the product maintained.
6. Never manufacture engagement or use misleading titles, screenshots, categories or claims.

## Release gate

Publish only when all P0 items are checked, every Blocked item has an explicit owner or honest listing limitation, the final regression matrix has evidence, and the listing package is complete. P1 may remain open only when it is documented as non-blocking and does not affect usability, licensing, accessibility, broken behavior or truthfulness.

## P0 — release blockers

### A. Page completeness, metadata and semantic structure

- [x] Add a unique Page Title and Meta Description to `/chefs`.
  - Verified 2026-08-16: `Chefs — AURELIA` / `Meet the fictional chefs behind AURELIA, a story-led restaurant Framer template.`
- [x] Verify one and only one semantic `h1` on every active content page and a logical `h2`/`h3` sequence below it.
  - Verified 2026-08-16: primary breakpoint readback found one `h1` on `/`, `/menu`, `/about`, `/chefs`, `/reserve`, and `/404`. Corrected the Menu seasonal statement from `h1` to `h2`, and the Reserve request heading from `h3` to `h2`; visual styles and component structure were unchanged.
- [x] Re-read the Home section order against the approved contract: `Opening → Vision → Chef → Space → Craft → Experience → Signature → Reservation Handoff → Footer`.
  - Verified 2026-08-16: Desktop structure readback places the shared Reservation Handoff immediately after Signature. Footer remains supplied by the shared Template.
- [x] Keep the custom `/404` with shared Template, one clear Return Home action, unique no-index metadata, and no invented operational claims.
- [x] Replace Framer's default site-level Settings metadata.
  - Verified 2026-08-16: global fallback Title is `AURELIA — Editorial Restaurant & Supper Club Framer Template`; the Description accurately states the responsive pages, editable components, and reservation-request flow. Existing favicon and social-image fields were retained pending final asset/licensing verification.
- [ ] Verify page names, paths and global navigation expose only Home, Menu, About, Chefs and Reserve; `/404` stays utility-only and `/private-dining` stays retired.
  - Acceptance: every Navbar/Footer route resolves, browser Back/Forward works, and there are no placeholder or dead destinations.

### B. Accessibility and replaceable-image ownership

- [x] Make an explicit Alt decision for the Home Hero image.
  - Verified 2026-08-16: it is a meaningful scene image with Alt `An intimate dining room at AURELIA, prepared for evening service.`
- [x] Add a buyer-editable Portrait Alt Property to `ChefStoryRow` and validate all three chef instances.
  - Verified 2026-08-16: `Portrait Alt` is bound to the existing portrait image; Mara Bellini, Elias Voss, and Noor Amani each have an instance-level editable value.
- [x] Add paired Alt Properties for all seven `DishSelector` image Properties.
  - Verified 2026-08-16: `Dish 01–07 Image Alt` controls are bound to the seven existing main image slots.
- [x] Add a Chapter Image Alt Property to `EveningChapterRow`.
  - Verified 2026-08-16: `Chapter Image Alt` is bound to the existing image and has instance-level values for Arrival, First Plates, From the Kitchen, and After.
- [ ] Decide whether all four `ChapterCursorPreview` images are decorative cursor enhancement.
  - Acceptance: decorative previews are ignored by assistive technology and do not duplicate chapter names.
- [ ] Validate MenuDishCard's existing `Image Alt` Property after replacing all seven dish images.
  - Acceptance: inherited defaults do not leave every distinct dish with the same generic Alt when the image is meaningful.
- [ ] Keyboard test every interactive system: Navigation, Phone menu, Button, EveningChapterRow, MenuDishCard, ChefStoryRow, DishSelector and Reserve form.
  - Acceptance: logical tab order, visible Focus, Enter/Space activation where appropriate, no keyboard trap, and focus returns sensibly after state changes.
- [ ] Verify Reduced Motion behavior for Hero Loader, Lenis, text reveal, cursor previews, scroll reveals and diagonal Button transitions.
  - Acceptance: essential content stays available; large/continuous motion is disabled or simplified when motion reduction is requested.
- [ ] Verify contrast for body text, muted text, focus treatment, inverse handoff, form states and Button states.

### C. Responsive, interaction and browser regression

- [ ] Run every active page at 320, 390, 599, 810, 1200 and 1440+ widths where applicable.
  - Acceptance: no horizontal overflow, clipping, collision, unreadable line length, accidental max-width constraint, or detached border/background.
- [ ] Stress-test the responsive fixes in `ChefStoryRow` and `EveningChapterRow`.
  - Acceptance: borders/story content fill available width; chef portrait retains its intended ratio and visual size contract while text grows; no image stretching.
- [ ] Test MenuDishCard collapsed/hover/expanded states on Desktop, Tablet and Phone.
- [ ] Test ChefStoryRow collapsed/expanded states on Desktop, Tablet, Wide Phone and Phone.
- [ ] Test DishSelector all seven choices on Desktop, Tablet and Phone; selection state, image crop and copy must remain synchronized.
- [ ] Test Navigation Desktop/Tablet/Phone/Phone Open, including scroll state, current page, close behavior and body scroll.
- [ ] Test all eight Button variants and every site instance; confirm diagonal filler, label legibility, link destination and hover connection.
- [ ] Test Reserve default, incomplete, pending, success and error states with keyboard and touch.
- [ ] Test latest Safari, Chrome and Firefox on Desktop plus iOS Safari and Android Chrome at minimum.

### D. Buyer editability and component hygiene

- [x] Replace old horizontal Button variants across the site with descriptive diagonal variants; preserve normal Variant-to-Variant hover connections.
- [x] Rename generic `hero` and `Hero Loader` variants to role/state names without changing timing or appearance.
  - Verified 2026-08-16: `Hero Base`, `Hero Alternate`, and `Loader Initial/Wordmark/Inverse/Hold/Exit`; original Variant-to-Variant connections remain ID-based.
- [ ] Name the 13 de-duplicated unnamed/default layers only where they own meaningful content, layout, image or state responsibility.
  - Acceptance: do not mass-rename generated breakpoint replicas; component internals remain scannable.
- [x] Confirm `Examples.tsx` is unused, then remove or replace it.
  - Verified 2026-08-16: no Canvas node used `withRandomColor`, `withHover` or `withRotate`; the unused test override file was removed after explicit authorization and the current code-file list is empty.
- [ ] Perform a controlled replacement test for Home Hero, About static imagery, MenuDishCard, ChefStoryRow, DishSelector and EveningChapterRow.
  - Acceptance record for each: replacement entry point, supported aspect ratios, crop/focal behavior, Alt owner, long-copy behavior, breakpoint result and fallback.
- [ ] Pressure-test content: 2× body copy, very long restaurant name, long navigation label, long dish/chef names, optional chef role removed, and mixed portrait/landscape images.
- [ ] Confirm buyers never need to edit generated breakpoint replicas to complete a normal content replacement.
- [ ] Keep the no-CMS model only if the seven-dish replacement test passes.
  - Escalation rule: propose CMS only if adding/removing/reordering items remains a repeated buyer task that cannot be documented safely with fixed Properties.

### E. Assets, code, performance and licensing

- [x] Build an asset register covering every shipped image, font, icon, external component and code dependency.
  - Current register: [asset-register.md](./asset-register.md). Unverified original source, redistribution permission, encoded weight and compatibility remain release blockers.
- [ ] Replace, license or remove every asset without proven Marketplace redistribution rights.
- [ ] Confirm font licensing and whether buyers need any external font account or manual setup.
- [ ] Review Lenis and Text Reveal on Scroll for license, current compatibility, buyer visibility, graceful failure and Reduced Motion behavior.
- [ ] Run Framer performance checks and a real published-preview audit.
  - Acceptance: optimize oversized originals, remove unused assets/effects/code, avoid blocking loaders, and record mobile load/interaction findings.
- [ ] Confirm favicon and Open Graph cover exist, are licensed, and remain legible at their actual display sizes.
- [ ] Verify no private data, API key, personal destination, unpublished client material or accidental test content ships in the Remix project.

### F. Reservation and product truth

- [ ] Choose and configure the real reservation/form destination, or deliberately ship the form as a clearly labelled demo.
- [ ] Add the required privacy/consent treatment, response expectation, cancellation language and success/error copy once the service is known.
- [ ] Verify every fictional chef, address, menu fact and operational claim is clearly demo content and easy to replace.
- [ ] Do not invent pricing, hours, policies, booking promises or biographies to close this checklist.

### G. Marketplace listing package

- [ ] Create and verify a public Demo/Preview URL.
  - Acceptance: no editor chrome, no password, all routes resolve, performance is acceptable, and the preview matches the listing media.
- [ ] Create and verify the Remix URL from a clean buyer account/path.
  - Acceptance: duplication succeeds; assets, styles, Components, links and instructions arrive intact.
- [ ] Finalize listing name and one-line byline.
  - Working search intent: `AURELIA — Editorial Restaurant & Supper Club Framer Template`.
  - Do not keyword-stuff or imply functionality the template does not include.
- [ ] Write a concise description answering: who it is for, what problem it solves, included pages/systems, editing model, form limitation, CMS status, and support scope.
- [ ] Select only accurate categories, styles and features.
  - Candidate language to validate in the current Marketplace UI: restaurant, hospitality, supper club, editorial, minimal, dark, reservation, storytelling, responsive.
- [ ] Produce listing media in this order:
  1. A short first-position video showing Home, Menu interaction, Chef expansion, responsive transition and editing controls.
  2. Desktop hero/overview screenshot.
  3. Menu interaction screenshot.
  4. Chef story screenshot.
  5. Phone/responsive screenshot.
  6. Editing/Styles/Properties screenshot.
  - Acceptance: no misleading mockups, browser clutter, illegible text or unlicensed imagery; first media reads well as a thumbnail.
- [ ] Add a support/contact statement, response expectation, version/update policy and honest limitations.
- [ ] Decide free/paid positioning and checkout only after the product package is complete; price is not a substitute for missing proof.

## P1 — quality and conversion improvements

### Styles and design-system cleanup

- [ ] Read usage before consolidating similarly named Text Styles (`Type/Display` vs `Display`, `Type/Heading 2` vs `Heading 2`, and equivalent Body/Story groups).
- [ ] Keep responsive/style variants that serve a real contract; remove only unreferenced legacy presets.
- [ ] Read token usage for `Color/red`, `Color/On Accent` and every Color Token; remove only proven test tokens.
- [ ] Normalize component capitalization (`hero` → `Hero`) if no external reference depends on the current name.
- [ ] Confirm all buyer-facing type uses shared Text Styles except documented one-off display treatments.

### Buyer onboarding

- [x] Write a concise Start Here editing guide outside the public sitemap unless a new page is separately authorized.
  - Draft: [buyer-editing-guide.md](./buyer-editing-guide.md). It remains contingent on the P0 image-Alt and replacement-proof items.
- [ ] Include: global colors/type, logo/navigation/footer, Button variants, Home dishes, Menu cards, Chef stories, reservation handoff, form destination, image/Alt replacement, favicon/OG, Demo content and publish steps.
- [ ] Add a five-minute buyer task test: change brand name/colors, replace one dish, replace one chef portrait/Alt, update reservation destination, publish Preview.
- [ ] Observe one unfamiliar tester. Record hesitation points and improve names/Properties/instructions rather than explaining them verbally.

### Listing conversion and launch distribution

- [x] Draft title, byline, description, category/style/feature selections and media captions as one coherent search package.
  - Draft: [listing-package-draft.md](./listing-package-draft.md). Verify exact Marketplace field labels and final media before publishing.
- [ ] Prepare one Community launch post with the video first, a contextual personal message, the buyer problem, and an invitation for real feedback.
- [ ] Reply to substantive comments and questions; turn repeated questions into listing or guide improvements.
- [ ] Prepare two non-spam distribution assets for relevant owned channels; link to the Marketplace listing, not an unverifiable checkout path.
- [ ] Schedule a 7-day and 30-day maintenance review for bugs, broken links, compatibility, comments and listing accuracy.

## P2 — post-launch learning

- [ ] Track views, preview opens where available, remixes, purchases, support requests and refunds separately.
- [ ] Do not treat Remix count as sales; remixes include template duplications.
- [ ] Diagnose the funnel by stage: listing thumbnail/title → detail page → Demo → Remix/purchase → successful edit/publish.
- [ ] Update media/copy only from observed confusion or weak conversion; preserve accurate positioning.
- [ ] Ship meaningful fixes and refreshes. Framer ranking is freshness-sensitive, but updates must improve the product rather than simulate activity.
- [ ] Maintain an issue log with severity, affected Framer version, workaround, fix date and buyer communication.

## Final regression matrix

Complete this table immediately before publication. `Pass` requires evidence; use `Blocked` when an external fact is missing.

| Scope | Structure | 320/390 | 599/810 | 1200/1440+ | Keyboard/Focus | Reduced Motion | Links/forms | Replacement | Result |
|---|---|---|---|---|---|---|---|---|---|
| Home | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | — |
| Menu | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | — |
| About | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | — |
| Chefs | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | — |
| Reserve | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | — |
| 404 | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | N/A | — |
| Shared Template/Nav/Footer/Button | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | [ ] | — |

## Evidence package required for release

- [ ] Final structural readback: pages, metadata, paths, Components, Properties, variants, links, forms, Styles, unused overrides and removal checks.
- [ ] Targeted screenshots for every material visual fix; do not substitute one full-page long capture for bounded evidence.
- [ ] Preview evidence for the regression matrix and all interaction states.
- [ ] Asset/license register and performance report.
- [ ] Clean-account Demo and Remix verification.
- [ ] Final listing copy/media package and support statement.
- [ ] Update `../STATUS.md` with current build truth and keep one current pointer in `../RECOVERY.md` after remediation begins.
- [ ] Re-run repository knowledge validation after checklist/status updates.

## Official Framer basis

- [Template best practices](https://www.framer.com/help/articles/template-best-practices/): originality, cohesive/shared styles, custom 404, auto layout, responsive behavior, clear links, appropriate CMS use, minimal code, purposeful motion, organized assets, semantics/Alt/accessibility, metadata, performance, copyright, listing and support.
- [How Marketplace ranking works](https://www.framer.com/help/articles/marketplace-ranking/): multiple meaningful activity and account-quality signals; no single signal or public fixed weighting; rankings and freshness change over time.
- [Get visibility in the Community](https://www.framer.com/help/articles/get-visibility-in-the-community/): For You, Hype, Marketplace Popular/Newest, Following and Search; visual media and especially first-position video improve discovery opportunities.
- [How to publish a template](https://www.framer.com/help/articles/how-to-publish-a-template/): pre-publish browser/screen/link/performance testing; listing name/byline/description/media/categories/styles/features plus Preview and Remix URLs.
- [Why remix count can exceed sales](https://www.framer.com/help/articles/why-is-a-template-s-remix-count-higher-than-its-sales/): remixes measure duplications, not purchases.
