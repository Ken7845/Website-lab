# Summit Roofing — Services Page Checklist

Page: Services  
Path: `/services`  
Status: In progress — four distinct Sections, Desktop/Tablet/Phone structure and four distinct service paths created on 2026-08-26; final Page Done remains blocked by planned Service Detail destinations and the bounded visual-review budget  
Content status: Service labels approved; all explanatory copy is `Demo`; operational claims remain `Missing`  
Primary CTA: Request an Inspection → `/#contact` until `/contact` is built and verified

## Scope Lock and Definition of Ready

### Page job

Give a property owner one calm, visual place to identify why they are visiting, understand the four available service paths, and begin an inspection request. This is the service decision page, not a claim-heavy sales page or a duplicate of the Home Services Section.

### Confirmed content

- Four stable offers: Repair & Maintenance, Roof Replacement, New Construction and Storm Damage Repair.
- Original Summit Roofing system: slate-blue / deep-navy / steel-grey surfaces, `0px` radii, hard image crops, `Big Shoulders` display styles and `Inter` reading/interface styles.
- Baker Roofing informs only the service-to-proof-to-contact sequence and clear hierarchy; its copy, layout, claims, imagery and branded structures are excluded.
- One strong work-in-progress roof image, followed by service-specific decision rows; do not make a uniform card grid.
- A direct CTA that leads to the currently existing Home Contact anchor until the standalone Contact page exists.

### Known Missing / Blocked facts

- No verified location, telephone, email, service area, operating hours, emergency-response time, warranty, licence, credential, product, pricing or project-result claim.
- No approved form endpoint, privacy wording or standalone Contact page.
- Service Detail pages do not yet exist; their future paths must not be treated as verified live destinations.
- Commercial-use licences for supplied imagery remain Missing.

### Explicit exclusions

- No publishing, paid dependency, Custom Code, new CMS Collection, form backend, fabricated testimonials, awards, counters, project outcomes or emergency claims.
- Do not change the completed Home composition, global color/type system, zero-radius rule, `ScrollRevealText.tsx` or `/reveal-text-test`.
- Do not create a new shared Service component unless current `Service Row` is proven unable to fulfil the required role.

### Add / Reuse / Modify decision

| Object | Decision | Contract |
|---|---|---|
| Services Web Page `/services` | Add | New buyer-facing authored page using the existing `Site Shell` Layout Template and three breakpoints |
| Navbar and Footer | Reuse | Inherited from `Site Shell`; only add a global Services destination after the page exists and link readback passes |
| `Content/Service Row` | Reuse | Four editable instances; existing Default is a three-column article row and Phone is a one-column stack |
| `Controls/Button` | Reuse | Existing Primary / Secondary variants and hover states; no inline replacement button |
| `Content/Process Step` | No-op on Services | Preserve its existing Home responsibility; Services uses a page-owned Method Ledger so it does not repeat Home’s process pattern |
| Shared Styles and Colors | Reuse | Use only the Home-observed and PROJECT-approved visual system |
| Home navigation links | Modify later, only after `/services` exists | Do not convert a current valid Home anchor into a dead global route |
| Services CMS / new Component / Code | No-op | Stable authored offers do not need a CMS or code dependency |

## Page Narrative

```text
Image-led service context
→ choose a service path
→ understand the work logic as a concise ledger
→ request an inspection
```

The page must feel more like a service directory than a second Home page. It opens with one dark, image-led masthead, then uses the familiar Service Row format only where it solves the scanning job. A page-owned method ledger explains the work logic without repeating Home’s Process component; the ending is a single, quiet handoff.

## Section Build Checklist

### 1. Services Masthead

- [x] Use one full-width deep-navy masthead below the shared Navbar, with the H1 above a hard-cropped aerial roof image and the supporting copy / CTA below it. This deliberately replaces the Home-like two-column introduction.
- [ ] Use the label `Services` and one H1. Proposed Demo H1: “Roofing work, clearly scoped.”
- [ ] Use a short Demo supporting paragraph that says visitors can begin with the condition or project type they recognise; do not claim a response guarantee.
- [ ] Pair the primary Button, label `Request an Inspection`, with `/#contact` until `/contact` exists.
- [ ] Use no generic icon badge, numerical proof bar or extra CTA.
- [x] Make the opening distinguishable from Home’s “Roofing, Made Clear.” split Hero: it is an image-led service masthead with vertical narrative order rather than a split Hero.

### 2. Choose the Work

- [ ] Add an editorial service navigator with label `Choose Your Path` and H2. Proposed Demo H2: “Start with the work in front of you.”
- [ ] Reuse four `Content/Service Row` instances in this exact order:
  1. `01` Repair & Maintenance — targeted repairs and practical maintenance for roofs that need attention.
  2. `02` Roof Replacement — a structured path for roofs that have reached replacement decisions.
  3. `03` New Construction — coordination and roof installation for new-build work.
  4. `04` Storm Damage Repair — an assessment-first path after visible roof damage.
- [ ] Keep descriptions as `Demo` template copy; do not promise emergency availability, material systems, durability, insurance handling or warranty coverage.
- [ ] Maintain the existing row component’s 1px dividers, square geometry and article semantics.
- [x] Until each Service Detail page exists, all four row instances route to the verified `/#contact` inspection path rather than a dead detail page. Their intended destinations remain recorded below.
- [ ] Restore the four individual detail destinations only after their pages exist and link readback succeeds. The Services Page cannot reach `Pass` until then.
- [ ] Do not replace the rows with equal image cards or duplicate the Home’s Service Section copy.

### 3. Working Method Ledger

- [x] Add a restrained slate-blue method band whose content is a page-owned ledger: `01 — Inspect the condition`, `02 — Define the work`, `03 — Complete the scope`.
- [x] Use the ledger to explain the three decisions without implying a response time, crew size, warranty or credential.
- [x] Do not reuse the Home `Content/Process Step` composition here; it would reintroduce the repeated template rhythm. The page-owned ledger is a one-off Section structure, not a new shared Component.
- [ ] Use H2 for the Section and H3 for individual step titles where headings are used.
- [ ] No invented timing, crew size, inspection fee, licence or warranty details.

### 4. Closing Handoff

- [x] End with one contained mist-grey single-column CTA band, not a second generic marketing Hero or duplicated two-column close.
- [ ] H2 proposed Demo copy: “Start with an inspection.”
- [ ] Supporting copy stays factual and does not imply a response time.
- [ ] Reuse the Primary Button: `Request an Inspection` → `/#contact` until `/contact` is verified.
- [ ] Shared Footer remains the only footer; do not create a page-local contact block with invented details.

## Styles, Semantics and Naming

- [ ] Reuse Home-observed `Utility/Label`, `Display/Hero` or `Display/Section`, `Display/Card`, `Body/Large`, `Body/Default` and existing Button typography only when their roles match; do not add arbitrary type styles.
- [ ] Use exactly one H1 in Section 1; each major Section has a purposeful H2, and process-step titles use H3 only where appropriate.
- [ ] Use semantic `section` containers, `article` Service Row instances and a button/link only for actual actions.
- [x] Name layers by role, including `Services Introduction`, `Service Navigator`, `Working Method`, `Method Ledger` and `Inspection Handoff`; no unnamed or generic `Frame` layers.
- [ ] Preserve `0px` corner radius, existing 1px divider logic, no red brand UI, and no rounded/pill controls.
- [ ] Use only the approved slate blue `#365F7A`, deep navy `#172B3A`, steel grey `#6C767D`, mist grey `#E3E7E8`, soft white `#F5F6F5` and white `#FFFFFF` system roles as currently observed through shared Styles; do not introduce a new color.

## Components, CMS and Shared Systems

- [ ] Apply the existing `Site Shell` Layout Template. Live evidence from 2026-08-26 confirms it supplies Navbar and Footer with Desktop, Tablet and Phone ownership.
- [ ] Instantiate `Content/Service Row` rather than duplicating its source. Its current controls are Number, Title, Description and Destination; current variants are Default and Phone.
- [ ] Instantiate `Controls/Button` rather than hand-building a CTA. Its current controls are Label and Destination; current variants are Primary, Secondary and their Hover variants.
- [x] Keep `Content/Process Step` unmodified and unused on Services; the page-owned Method Ledger is the selected inline alternative and its outcome is recorded in Latest Part Result.
- [ ] No CMS is necessary for four stable authored services. Existing Projects and Insights CMS Collections are out of this page’s data scope.
- [ ] No Component Requirement Contract is needed unless the live implementation changes a reusable Component’s source, variants or Properties. If that becomes necessary, create the request-specific record and compile the contract before the change.

## Navigation and Conversion

- [ ] Navbar logo remains `/`; current global route additions are deferred until `/services` exists.
- [ ] Page primary CTA: `Request an Inspection` → `/#contact` while the Home Contact anchor is the only verified conversion destination.
- [x] Current Service Row destination: `/#contact` for all four rows, because it is the only verified inspection conversion path.
- [ ] Intended future Service Row destinations are `/services/repair-maintenance`, `/services/roof-replacement`, `/services/new-construction` and `/services/storm-damage-repair`; validate each only after its page is built.
- [ ] After `/contact` is built, update the Services Buttons to `/contact` in one scoped link change and revalidate Desktop, Tablet and Phone.
- [ ] No placeholder phone, email, map, social or form endpoint may be added.

## Image Plan and Alt Contract

- [ ] Use one Services-wide proof image only; avoid repeating Home’s `shingle-install.webp` Hero asset.
- [x] Selected Canvas source: `https://framerusercontent.com/images/U5yFdwnN3bmApukAx6T9CSlTALk.webp`; role: Services masthead, 440px Desktop / 360px Tablet / 240px Phone; focus: centred aerial roof inspection.
- [x] Final Canvas Alt: `Aerial view of a flat roof inspection`.
- [ ] Desktop image can be a wide horizontal plane; Tablet preserves the roof/worker focal point; Phone must use a shorter crop or natural stack rather than shrinking the subject beyond recognition.
- [ ] Final Alt example format: `Roofer working on a framed roof structure` — use only if it matches the final selected image.
- [ ] Licence status remains Missing and blocks Marketplace publication, not layout work.

## Responsive Contract

| Breakpoint | Required composition | Ownership / risk |
|---|---|---|
| Desktop ≥1200 | Dark vertical masthead sequence: H1 → aerial image → copy / CTA; navigator uses the current Service Row Default three-column grid; method stays a three-column ledger | Page Section owns widths and spacing; Service Row instance owns row internals |
| Tablet 810–1199 | Same masthead order with a 360px aerial plane; service rows remain legible; method ledger remains three columns | Do not invent a Tablet Service Row Variant without inspecting need and Component ownership |
| Phone ≤809 | Masthead remains one reading column with a 240px image; Service Row Phone variant is a one-column stack; method ledger becomes a vertical list; CTA stays visible without fixed-position overlap | Page owns Section stack and image height; Service Row Phone variant owns its row stacking |
| Narrow stress 320 | No horizontal overflow, clipped Button label, single-character heading wrap or inaccessible service row | Structural stress only; repair the responsible Page or Component owner |
| Wide 1440+ | Content remains deliberately capped/contained while selected proof imagery may be full-width | Avoid a stretched text measure or arbitrarily wider rows |

## Motion, Focus and Accessibility

- [ ] Use existing Button Hover states only; no hover-only service information.
- [ ] Service Row behaviour must remain equally understandable through keyboard and touch; if a future link is inactive, do not present it as a completed interactive path.
- [ ] Preserve visible focus, natural reading order and meaningful aria/semantic behaviour from shared systems.
- [ ] Reduced Motion retains all content; any entrance treatment is short, nonessential and removable.
- [ ] Do not add overlays, lightboxes, scroll-jacking or code-driven animation to this page.

## Metadata, Performance and Maintainability

- [ ] Proposed Demo Page Title: `Roofing Services | Summit Roofing`.
- [ ] Proposed Demo Meta Description: `Explore repair, replacement, new construction, and storm damage roofing services in a clear, adaptable contractor template.`
- [ ] Page-specific Open Graph image may use the final proof image only after licence and crop review; otherwise inherit the verified site image.
- [ ] Keep page media to the one planned proof image plus shared shell assets; use the image workflow to avoid oversized output.
- [ ] No third-party dependency, custom code, external form provider or unnecessary Component source edit.
- [ ] Buyer editing guidance must identify editable labels, service descriptions, row destinations, proof image, metadata and Demo/Missing boundaries.

## Marketplace Replacement Stress Tests

- [ ] Replace every service name with a longer title and confirm Row wrapping and phone order remain sound.
- [ ] Double each service description; confirm Default and Phone rows do not overlap or truncate meaningfully.
- [ ] Remove a service description; confirm the missing content has an intentional fallback rather than an empty visual gap.
- [ ] Replace the proof image with portrait and landscape alternatives; confirm focal point and Section height remain readable.
- [ ] Change inspection CTA wording to a longer buyer-provided label.
- [ ] Confirm the page does not imply unverified service areas, warranties, pricing, emergency response or credentials when a buyer replaces Demo content.

## Targeted Preview and Page Done

### Targeted Preview paths

- [ ] Desktop: Navbar → Services Masthead → four Service Rows → Method Ledger → Inspection Handoff → Footer.
- [ ] Tablet: confirm the 360px masthead image and scan all four Default rows for usable reading width.
- [ ] Phone: open/close shared Navbar → masthead → four Phone Service Rows → vertical Method Ledger → CTA → Footer.
- [ ] Keyboard: tab through Navbar, primary CTA, every completed service destination and Footer links; focus stays visible.

### Services Page Done

- [ ] All four Sections match the approved narrative and image plan.
- [ ] All service destinations exist and their links pass targeted readback; otherwise Page status cannot be `Pass`.
- [ ] Shared shell, styles, components, semantics, Alt, focus, reduced motion and Button states pass.
- [ ] 320, 390, 810, 1200 and 1440+ checks pass.
- [ ] Metadata, image performance, Marketplace replacement tests and targeted Preview paths pass.
- [ ] `PROJECT.md` Current Status and Recovery are updated with final evidence; this page does not duplicate the current checkpoint.

## Latest Part Result

Scope: Services page redesign — break the repeated Home composition while retaining the confirmed service content and shared system
Status: In progress

### Revision Constraint Lock — 2026-08-26

- Still active: four approved service labels; all supporting copy remains `Demo`; `/#contact` remains the only verified conversion destination; `Site Shell`, zero-radius blue-grey system, shared Button and Service Row remain the required shared dependencies.
- User correction: “你这个排版和home太重复了，你完全可以直接参照[https://bakerroofing.com](https://bakerroofing.com)的service是怎么做的，不要总是套用差不多的模版”.
- New page direction: replace the repeated Home-like two-column introduction / process-band rhythm with a service-directory composition informed by Baker’s service hierarchy: an image-led service masthead, a dense navigable service index, then one editorial proof / method band and a restrained conversion close. This is a translation of hierarchy only, not a copy of Baker’s layout, copy, imagery, facts, figures or enterprise claims.
- Add / Reuse / Modify: **Modify** the existing Services page-owned Sections and their Desktop / Tablet / Phone overrides; **Reuse** Site Shell, Button, Service Row and the existing aerial-inspection asset; **No-op** for Home, shared Component source, CMS, Custom Code, detail-route destinations and publication. The existing Process Step source is preserved but no longer used on Services.
- Required verification after the batch: affected Desktop / Tablet / Phone structure, service-row reading order and `/#contact` controls. Image Review Plan: reuse the existing Canvas aerial-inspection asset only; answer whether its masthead crop has a readable roof subject; one bounded Services masthead screenshot at Desktop maximum, then structural fallback if unavailable.

Pass:
- Live targeted readback on 2026-08-26 confirms the completed Home uses `Site Shell` with Desktop, Tablet and Phone ownership.
- Existing `Content/Service Row` has Number, Title, Description and Destination controls; Default is a three-column article row and Phone is a one-column stack.
- Existing `Controls/Button` has Label and Destination controls with Primary / Secondary and Hover variants.
- `/services` now uses `Site Shell` with Services Introduction, Service Navigator, Working Method and Inspection Handoff; the standalone Jobsite Proof Section was removed after its image was promoted to the masthead.
- `Content/Process Step` remains unchanged for Home but is no longer instantiated on Services; a page-owned Method Ledger now carries the three work decisions.
- Tablet readback confirms a 360px masthead image, the four-row Service directory and the three-column Method Ledger at 810px.
- Phone readback confirms a 240px masthead image, single-column Service Row variants, a vertical Method Ledger and single-column Handoff structure.
- One bounded Desktop masthead screenshot was visually checked; it confirms a readable aerial roof subject, deep-navy service entry and a composition distinct from Home’s split Hero.
- Live QA found three duplicated Desktop Service Row instances; the in-scope repair restored `02 Roof Replacement`, `03 New Construction` and `04 Storm Damage Repair`. Desktop and Phone control readback now confirms all four distinct rows and the shared `/#contact` destination.
- Metadata is present: `Roofing Services | Summit Roofing` and the page-specific Demo description recorded above.
- The final proof image has a specific Canvas Alt and no unlabelled image was introduced in this page scope.

Fix Required:
- No remaining in-scope structural or content defect found in targeted live QA.

Blocked:
- Standalone Service Detail destinations and Contact page do not yet exist. Service Rows therefore intentionally use `/#contact` until their pages are built.
- Operational facts, form handling and supplied-image licensing are not yet verified.
- Full-page visual/Preview, 320px narrow stress and 1440px wide review were not run in this Part: the one permitted screenshot was already used for the opening-section composition, so repeated visual inspection is intentionally deferred rather than represented as verified.

Verified widths:
- Existing shared-system readback: Desktop 1200, Tablet 810 and Phone 390 breakpoint contracts.
- Services targeted structure: Desktop 1200 source structure, Tablet 810 measured Section flow, Phone 390 single-column variant structure.

Verified paths:
- Existing conversion destination `/#contact` is used by the two Services Buttons and all four Service Rows.
- Service Detail paths are planned only and not yet verified.

Shared components affected:
- Reused without source edits: `Site Shell`, Navbar, Footer, `Content/Service Row`, `Controls/Button`. `Content/Process Step` remains unchanged but is no longer instantiated on Services.

Recovery:
- Canonical current pointer: `../PROJECT.md#14-recovery`
- This Part result date: 2026-08-26
