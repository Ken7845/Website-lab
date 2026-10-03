# Submit Roofing — Shared Hover Implementation

- Contract schema: 1
- Component contract: Required
- Visual contract: N/A — this recorded Part contains no visual contract; lifecycle migration makes no construction change.
- Evidence migration: 2026-10-03; repository-only. Original contract assertions are preserved in project History; no fresh Canvas or runtime proof was produced.

## Original user requirements

1. “audit all the website and prepare for the next step: add hover effect. find cards or rows suitable for hover effect. Also look for the hover relative knowledge in the Website-lab. btw I have add one hover effect to the Method Ledger in the services page”
2. “start to add the effect”
3. “this is the new location and now resume the work. you should make a checklist before the complex work. Have you forgotten that?”

## Authorization and constraint lock

- Date: 2026-10-03. Status: Implemented; Structural Pass / Visual and runtime Blocked. Checklist and Ready contract were saved before the first Canvas write.
- User explicitly authorized implementation and resumption; no additional checklist-format approval is required by [change control](../../../../framer/basic/workflows/change-control.md#将知识规则编译进组件请求合同).
- Source plan: [verified hover audit](./hover-readiness-audit.md). New repository: `/Users/Zhuanz/Desktop/Business/Website_Lab/`.
- Modify existing Service Row, Article Card and Contact Submit definitions; reuse CMS collections, color/text styles, Project Card and Button.
- Fix Home Project/Article card destinations and normalize the seven audited enquiry CTA instances to `/contact`.
- Integrate Home's inline article rendering with the existing Article Card. Preserve Desktop/Tablet padding 20px and image height 240px; Home Phone keeps padding 18px and image height 220px. Archive Phone keeps its current Default geometry.
- Preserve Method Ledger effects, navbar/footer, imagery, CMS records/schema, copy, section composition and existing Button reel/filler. No publication, Custom Code, paid dependency, new page or invented fact.
- Optional Process, Repair Sequence, Replacement Handoff, Construction Scope and About Principle effects remain deferred. Static FAQs and reading surfaces remain static.

## Component Requirement Contract

Contract status: Blocked — structural ownership and settings pass; visual and actual interaction evidence are unavailable. See [QA evidence and limits](#qa-evidence-and-limits). This is not a completed runtime acceptance.
Implementation status: Implemented — historical completion record; current live state not reverified.
Verification status: Blocked — retain bounded historical results; outstanding evidence requires the live Framer gate.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Preserve page surfaces, gutters, section gap and reading order | Existing page sections | Current live Home/Services/Insights/Contact trees, 2026-10-03; [PROJECT brand](../../PROJECT.md#6-brand-direction) | Pass — before/after page comparison: only approved card wrappers, enquiry destinations and archive explicit Default selection changed; section settings/order preserved; [recorded evidence](#qa-evidence-and-limits) | Blocked — Phone render download failed; no whole-page visual claim |
| Available width / placement | Instances remain fill width / auto height; submit remains fit / fit | Page CMS wrapper, row instance and form | [Component responsibility](../../../../.agents/skills/framer-components/SKILL.md#assign-responsibility) | Pass — all 24 Service Row copies, six Article templates and three submit copies inspected at 1200/810/390; fill/auto and fit/fit contracts retained; [recorded evidence](#qa-evidence-and-limits) | Blocked — narrow rendered fit and 320/1440 runtime stress not proven |
| Visible boundary / border / surface | Service Hover: Slate Blue title and top rule. Article Hover: Slate Blue border/title and 8% Navy image mask. Submit Hover: Navy fill / white label. No external scaling | Shared component definitions | [Row hover](../../../../framer/basic/patterns/motion-design.md#component-row-hover); current tokens and existing Project Card mask | Pass — three native Hover sources match their Default geometry; exact tokens/mask alpha read back; contrast 6.83:1 Slate/White, 14.55:1 Navy/White; [recorded evidence](#qa-evidence-and-limits) | Blocked — Agent rejects native gesture-state screenshots; transition appearance needs actual Preview |
| Internal padding / hit area | Preserve row 28px vertical / Phone 22px; article 20px, Home Phone 18px; submit 14px 20px | Component roots; Home selects Compact article variant | Current live definitions and Home breakpoint overrides | Pass — padding/gap unchanged; Compact image 220px, Default image 240px; submit native button measured 166×58 with matching Hover geometry; [recorded evidence](#qa-evidence-and-limits) | Blocked — pointer and touch operation not executed |
| Readable max-width | N/A — no typography redesign; preserve flexible text widths and existing section caps | Existing page sections and component text | [PROJECT brand](../../PROJECT.md#6-brand-direction); current Canvas width chain | Pass — migrated image/category/title/summary match original bindings/styles; section caps and text fill widths retained; [recorded evidence](#qa-evidence-and-limits) | Blocked — Home Phone screenshot unavailable; no claim of rendered wrapping |
| Editable content / Properties | Preserve CMS variables and Service Row Properties; Article Card remains image/category/title/summary editable; no content variants | CMS and existing Component Properties | [Repeated content](../../../../framer/basic/patterns/pattern-recipes.md#6-repeated-content) | Pass — existing controls and bindings retained; current Projects four / Insights two records and slug variables match audit; no collection/item writes; [recorded evidence](#qa-evidence-and-limits) | Blocked — CMS-backed card image/title visual fit not inspected |
| States / routes | Native Hover gestures, stable geometry; Service Phone and Home Compact Article stay static. One CMS-wrapper link per card. Submit has no navigation link and retains form-submit binding | Definitions own hover; wrappers own CMS route; form owns submit | [Native model](../../../../.agents/skills/framer-interactions/SKILL.md#select-the-native-model); official task-map Components/Forms/CMS/Links guidance | Pass — Home CMS wrappers bind matching slugs on all breakpoints; all 21 enquiry copies point to /contact with unchanged labels; native submit binding retained; [recorded evidence](#qa-evidence-and-limits) | Blocked — readiness Preview ready with zero errors/warnings, but no runtime pointer, route-click or submission evidence |
| Breakpoint contract | Preserve existing breakpoints. Home Phone selects Compact; archive Phone remains Default. No hover-only content | Existing page replicas and shared visual variants | [State protection](../../../../.agents/skills/framer-interactions/SKILL.md#protect-state-and-breakpoints) | Pass — Desktop/Tablet Default and Home Phone Compact confirmed; archive all Default; Service Phone preserved; new breakpoint-name mismatch warning resolved; [recorded evidence](#qa-evidence-and-limits) | Blocked — static and touch usability require actual Phone Preview |
| Accessibility / touch / focus | Native anchors and native submit button; complete default content; decorative mask ignores pointer; preserve Reduced Motion. Preserve existing Contact focus styling | Native links/button/input and project metadata | [State protection](../../../../.agents/skills/framer-interactions/SKILL.md#protect-state-and-breakpoints) | Pass — no nested Article links; mask pointerEvents none; all 12 inputs retain 2px Slate focus borders and 16px text; root reducedMotion true; no hover-only information; [recorded evidence](#qa-evidence-and-limits) | Blocked — keyboard focus visibility, touch and Reduced Motion execution untested; settings are not runtime evidence |
| Evidence sample | Home/Services all rows; Home CMS templates; Insights archive; Contact submit; protected Button/Project Card/navbar/footer/Method Ledger | This request QA | [Implementation verification](../../../../.agents/skills/framer-components/SKILL.md#implement-in-one-layer-at-a-time) | Pass — targeted snapshots compared; protected component attributes/content equal; Method Ledger effects preserved (placement serialization differs); repository validator result below; [recorded evidence](#qa-evidence-and-limits) | Blocked — screenshot failure recorded once; readiness check does not test interactions |

## Execution checklist

- [x] Read relocated AGENTS, PROJECT relevant scope, verified audit and change-control rules.
- [x] Reuse connected official Framer Agent session; targeted live readback confirms no prior hover writes.
- [x] Record user requirements, preserve/exclusion lock and Ready component contract before Canvas writes.
- [x] Bind Home Project/Article wrappers to matching CMS-slug routes on all breakpoints.
- [x] Normalize only the seven audited enquiry CTA instances and their responsive copies to `/contact`.
- [x] Add shared Service Row Default Hover with title/top-rule colors; preserve Phone layout/static usability.
- [x] Add shared Article Default Hover; keep image treatment inside the fixed media frame.
- [x] Integrate Home article instances, preserving responsive geometry and existing CMS bindings.
- [x] Add Contact Submit Hover without altering its native form contract; check input focus.
- [x] Read back all changed component states and representative instances across three breakpoints.
- [x] Confirm Method Ledger, Button, Project Card, navbar/footer and unrelated content are preserved.
- [x] Calculate changed-color contrast and classify bounded visual review as Blocked; see evidence below.
- [x] Run official readiness Preview; distinguish diagnostics from runtime interaction testing.
- [x] Synchronize PROJECT recovery/status and run strict knowledge validator.

## QA evidence and limits

- Structural evidence: Pass, official Framer Agent session 7 targeted readback, 2026-10-03. All three native Hover variants inherit the correct source and retain equal external geometry; their existing `spring-duration 0.4s 0.2 0s` transition is retained. Service Row Phone has no new hover; Home Article Compact is explicitly selected only on Home Phone. Archive retains Default at every breakpoint.
- Links: Home Projects uses `/projects/:slug` with its Projects Slug variable; Home/Archive Insights uses `/insights/:slug` with its Insights Slug variable. Links belong to CMS wrappers, not Article children. All seven enquiry CTA primary instances plus their 14 responsive copies use `/contact`; labels are unchanged. Route clicks remain untested.
- Preservation: Button, Project Card, Navbar and Footer content/attributes compare equal with pre-edit snapshots. All three Method Ledger effects retain `rgba(0, 0, 0, 0.3)`, scale 1, x/y 0 and `spring-duration 0.4s 0.2 0s`. Their isolated-node snapshots differ only in position/pin serialization; whole Services before/after comparison shows only the three authorized CTA destinations changed. Contact page values and form binding compare unchanged.
- Diagnostics: Native component edits applied cleanly. Page edits reported existing section-spacing/max-width warnings; implicated ancestor settings are unchanged versus baseline and rendered overlap is not inferred from those diagnostics. A newly introduced Article Phone-name mismatch was resolved by naming the compact visual variant `Compact`, keeping Home's explicit selection and archive Default. Readiness Preview returns `ready`, zero errors and zero warnings; it neither publishes nor proves interaction execution.
- Contrast: Slate Blue `#365F7A` / White `#FFFFFF` = 6.83:1; Navy `#172B3A` / White = 14.55:1, calculated from sRGB relative luminance.
- Visual evidence: Blocked. Article native Hover capture returned `Variant node must be a top-level variant`. Home Phone bounded capture generated [screenshot](https://framerusercontent.com/screenshots/on-demand/5babae7c-b9e2-4e5e-9b82-ddaa26e5b1f7.jpg), but its single timed download failed with `LibreSSL SSL_ERROR_SYSCALL`; no image was viewed. Contact Hover capture is omitted because it uses the same unsupported gesture-state screenshot path. No visual Pass is claimed.
- Actual pointer, keyboard focus, touch and Reduced Motion runtime: Blocked — official task-map tools provide no documented pointer/keyboard execution control; no UI fallback is authorized. Next focused check: Hover → Leave on Home/Services rows and Home/Insights cards, submit Hover without submitting, Tab focus on card links/submit, then Phone static/tap behavior and Reduced Motion.
- 320px / 1440px stress: Not executed; existing page stress limitations remain. The structural 1200/810/390 review is not evidence of stress-width rendering.
- Contact delivery/successful submission: Outside hover scope; existing recipient/delivery blocker remains.
- Whole-site launch QA and publishing: Not part of this request.
- Repository validation: `validate_repository.py --strict` Pass, zero errors / zero warnings / three pre-existing notes. PROJECT links the active request and records the continuation point; the pre-edit audit is explicitly a snapshot, not current implementation truth.
