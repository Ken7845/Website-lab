# Summit Roofing — Site Expansion Planning Checklist

## Status

- Document role: Approved project-wide master plan and verbatim request record; not a page execution Checklist
- Status: Approved
- Confirmed by user: 2026-08-26, `确认`
- Scope type: Buyer-facing multi-page expansion planning
- Canvas implementation: Not started
- Publishing: Excluded; requires separate explicit approval

## Context-Free Handoff

If this file is opened in a fresh chat with no prior conversation, use the following facts and sequence:

- Project: Summit Roofing, a Framer Marketplace roofing template.
- Current implementation truth: Home and its shared `Site Shell` are complete; the expansion pages in this file are approved but have not been built. Verify this again through the official Framer Agent before Canvas work.
- Direction: Independent slate-blue / deep-navy / steel-grey industrial system, `0px` radius, `Big Shoulders` display type, `Inter` body type, hard crops and restrained motion.
- Reference boundary: Baker Roofing informs page roles, hierarchy and service-to-proof-to-contact flow only. Do not copy its brand, exact page structures, proprietary content or enterprise claims.
- Current unresolved facts: Contact details, service area, credentials, warranties, response claims, project facts, image licences, form destination and privacy text remain `Missing`; sample copy remains `Demo`.
- Development exclusion: `/reveal-text-test` and `ScrollRevealText.tsx` are not buyer-facing pages and require a separate retain/remove decision.
- Immediate next action: Create and present `../services.md` as the first page-specific Checklist. Do not write to the Services Canvas until the user confirms that Checklist.

Required re-entry order:

```text
Website-lab/AGENTS.md
→ ../../PROJECT.md
→ ../README.md
→ this approved master plan
→ the one active page Checklist
→ official Framer Agent gate and targeted current-state readback
→ one declared Page Part at a time
```

The canonical current-state and recovery owners remain `../../PROJECT.md`; this record preserves the approved plan and source request without becoming a second current-status diary.

## User Requirements — Verbatim

> [https://bakerroofing.com](https://bakerroofing.com)这是本次搭建任务的参考网站，然后现在需要进行搭建规划，先参考网站，规划一下要搭建哪些页面，这些页面要做哪些内容，要特别注意不要遗漏图片素材，但也不用一次性全都用上，就是要读一下图片素材去适配内容

> 确认

> 在建设每个页面之前要先规划checklist，然后我看你这个建设清单应该是总览，要符合就是无上下文的聊天框读了也知道要怎么做的要求，所以优化一下建设清单，然后我们一个页面一个页面来。对了知识库有这个要求吗，找一下

## Confirmed Scope

- Preserve the completed Home and its shared `Site Shell`, Styles, Components and CMS Collections as the current base.
- Add nine buyer-facing page types across approximately twelve routes: Services, four authored Service Detail pages, Projects and CMS Project Detail, About, Insights and CMS Insight Detail, and Contact.
- Use Baker Roofing as an information-architecture and hierarchy reference only. Do not copy its brand, wording, exact layout, enterprise scale or unsupported claims.
- Exclude Baker-specific Careers, Locations, National Accounts, employee-ownership claims, century-scale history and other unverified enterprise routes.
- Use the supplied image library in stages. Every image has been reviewed for possible placement, but not every image must appear in the first build.
- Keep unknown operational facts as `Missing` and sample/template content as `Demo`.
- Keep `/reveal-text-test` and `ScrollRevealText.tsx` outside buyer-facing scope until the separate retain/remove decision is made.

## Confirmed Sitemap and Build Order

1. Services `/services`
2. Repair & Maintenance `/services/repair-maintenance`
3. Roof Replacement `/services/roof-replacement`
4. New Construction `/services/new-construction`
5. Storm Damage Repair `/services/storm-damage-repair`
6. Projects `/projects`
7. CMS Project Detail `/projects/:Projects`
8. About `/about`
9. Contact `/contact`
10. Insights `/insights`
11. CMS Insight Detail `/insights/:Insights`

Implementation order:

1. Services plus the four Service Detail routes.
2. Projects archive and CMS Project Detail.
3. About.
4. Contact.
5. Insights archive and CMS Insight Detail.

The order is sequential. Before each numbered page begins, create its long-lived page contract at `checklist/<page-slug>.md`, show it to the user and wait for explicit confirmation. Do not generate every page contract in advance; later page plans must incorporate verified lessons from the pages already completed.

## Page Content Contract

### Services

- Intro that explains the four service paths.
- A service navigator that reuses the established Service Row language where appropriate.
- Service-specific image moments rather than a uniform grid of generic cards.
- A direct inspection CTA and route to Contact.

### Four Service Detail Pages

- Problem / fit statement.
- What the assessment covers.
- Typical work scope without invented guarantees or response times.
- Clear process.
- Relevant image sequence.
- FAQs using Demo content until approved facts exist.
- Closing inspection CTA.
- Use one shared authored-page contract; do not create a Services CMS unless later scale requires it.

### Projects and Project Detail

- Projects intro and useful categories or filters only when supported by CMS fields.
- Image-led archive using the existing Projects Collection.
- Project Detail structure: hero, verified facts, challenge, solution, gallery/result and related CTA.
- Until verified project sets are supplied, titles, locations, scope and results remain Demo.

### About

- Short brand story written as Demo template copy.
- Working principles and process rather than unsupported awards or numerical claims.
- Supplied team and crew imagery.
- Service and Contact routes.

### Contact

- Direct contact options with values marked Missing until supplied.
- Short inspection / estimate enquiry form.
- Service-area note, response expectation and privacy wording only when approved.
- One restrained visual at most; conversion clarity takes priority.

### Insights and Insight Detail

- Featured article plus an article archive using the existing Insights Collection.
- Detail template with readable article body, useful takeaway, related content/service and CTA.
- Article copy and author/date facts remain Demo unless supplied.

## Approved Staged Image Allocation

| Destination | Use now | Reserve / rule |
|---|---|---|
| Repair & Maintenance | `roofer on roof/roofer-ledge.webp`; `roofer on roof/roof-work.webp`; `exterior/roof-detail.webp` | Prefer active inspection and detail views |
| Roof Replacement | `exterior/red-roof.webp`; `roofer on roof/shingle-install.webp`; `exterior/modern-home.webp` | Reserve `exterior/tile-house.webp` for Projects |
| New Construction | `exterior/house-frame.webp`; `roofer on roof/frame-ladder.webp`; `roofer on roof/roof-framing.webp` | Reserve `roofer on roof/roof-build.webp` |
| Storm Damage Repair | `storm damage roof/fire-damage.webp`; one of `roof-damage.webp` / `storm-repair.webp`; `storm-roof.webp` | The two damage images are visually duplicate; do not use both by default. `roof-crane.webp` is optional |
| Projects — flat/commercial | `flat roof/flat-roof.webp`; `flat roof/roof-aerial.webp`; `flat roof/facade-roof.webp`; `flat roof/modern-deck.webp` | Group only when project facts support the category |
| Projects — exterior | `exterior/brick-roof.webp`; `exterior/tile-house.webp`; `exterior/modern-home.webp`; `exterior/red-roof.webp` | Avoid implying these are one project without evidence |
| About | `team.webp`; `roofer portait/crew-lead.webp`; `roofer portait/roof-harness.webp` | Reserve `crew-beanie.webp` and `crew-smile.webp` |
| Insights | `exterior/roof-detail.webp`; `exterior/roof-samples.webp`; `flat roof/roof-aerial.webp`; unused jobsite details | Match each image to article subject; do not use as decoration only |

## Missing or Blocked Inputs

- Commercial-use licences for supplied imagery.
- Verified same-project before/after pairs.
- Verified project titles, locations, scopes, captions and results.
- Real address, phone, email, opening hours, social links and service area.
- Form destination, privacy wording and expected response time.
- Verified credentials, warranties, emergency-response claims and team biographies.
- Final decision between the `SUBMIT ROOFING` live label and `Summit Roofing` project identity.
- Final Marketplace decision for the Reveal Text development component and test page.

These inputs block factual completion or Marketplace publication, but they do not block structural page implementation when all placeholders remain visibly Demo or Missing.

## Implementation and Validation Gate

- Project-wide approval does not authorize an individual page build. The page remains `To do` after its 16-category page contract is confirmed and becomes `In progress` only when its first declared Canvas Part begins.
- Before each live Canvas implementation turn, complete the repository-required Framer Agent gate and show the gate receipt.
- Before creating each page, Section, Component, Variant or CMS field, classify the action as Add, Reuse, Modify or No-op.
- Reuse the approved `Site Shell`, zero-radius geometry, shared Styles and existing Components before adding equivalents.
- Preserve one clear H1 per page, semantic heading order, visible focus, meaningful Alt text and non-hover-only actions.
- Verify relevant Desktop, Tablet and Phone states, including 1200px, 810px, 390px, 320px narrow stress and a 1440px+ capped-layout review.
- Follow the repository image workflow for crop, focal point, compression, Alt and licensing evidence.
- Verify metadata, links, forms, CMS bindings, empty states and Preview behaviour for every completed Part.
- Publication and Marketplace submission remain separate, explicitly authorised actions.

## Confirmation Record

- The user confirmed this planned Sitemap, content scope, image strategy and build order on 2026-08-26 with `确认`.
- On 2026-08-26 the user further required a page-specific Checklist before every page and page-by-page construction. This master plan therefore governs scope and order but cannot replace the active page contract.
- The next planning Part is Services `/services`; its page-specific Checklist does not yet exist and no Canvas work is authorized until it is presented and confirmed.
