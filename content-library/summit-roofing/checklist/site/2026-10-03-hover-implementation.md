# Submit Roofing — Shared Hover Implementation

## Original user requirements

1. “audit all the website and prepare for the next step: add hover effect. find cards or rows suitable for hover effect. Also look for the hover relative knowledge in the Website-lab. btw I have add one hover effect to the Method Ledger in the services page”
2. “start to add the effect”
3. “this is the new location and now resume the work. you should make a checklist before the complex work. Have you forgotten that?”

## Authorization and constraint lock

- Date: 2026-10-03. Status: Ready for implementation; no Canvas edits yet.
- User explicitly authorized implementation and resumption; no additional checklist-format approval is required by [change control](../../../../framer/basic/workflows/change-control.md#将知识规则编译进组件请求合同).
- Source plan: [verified hover audit](./hover-readiness-audit.md). New repository: `/Users/Zhuanz/Desktop/Business/Website_Lab/`.
- Modify existing Service Row, Article Card and Contact Submit definitions; reuse CMS collections, color/text styles, Project Card and Button.
- Fix Home Project/Article card destinations and normalize the seven audited enquiry CTA instances to `/contact`.
- Integrate Home's inline article rendering with the existing Article Card. Preserve Desktop/Tablet padding 20px and image height 240px; Home Phone keeps padding 18px and image height 220px. Archive Phone keeps its current Default geometry.
- Preserve Method Ledger effects, navbar/footer, imagery, CMS records/schema, copy, section composition and existing Button reel/filler. No publication, Custom Code, paid dependency, new page or invented fact.
- Optional Process, Repair Sequence, Replacement Handoff, Construction Scope and About Principle effects remain deferred. Static FAQs and reading surfaces remain static.

## Component Requirement Contract

Contract status: Ready.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Preserve page surfaces, gutters, section gap and reading order | Existing page sections | Current live Home/Services/Insights/Contact trees, 2026-10-03; [PROJECT brand](../../PROJECT.md#6-brand-direction) | Compare affected section ancestors and neighboring order against before snapshots | Bounded Home article render; no whole-page redesign claim |
| Available width / placement | Instances remain fill width / auto height; submit remains fit / fit | Page CMS wrapper, row instance and form | [Component responsibility](../../../../.agents/skills/framer-components/SKILL.md#assign-responsibility) | Definition plus first/middle/last row/card instances on Desktop/Tablet/Phone | Narrow Home card rendering and structural 320/1440 width-chain review |
| Visible boundary / border / surface | Service Hover: Slate Blue title and top rule. Article Hover: Slate Blue border/title and 8% Navy image mask. Submit Hover: Navy fill / white label. No external scaling | Shared component definitions | [Row hover](../../../../framer/basic/patterns/motion-design.md#component-row-hover); current tokens and existing Project Card mask | Default/Hover equal geometry; verify colors, mask and inherited content | Bounded Article Hover screenshot; calculated text contrast |
| Internal padding / hit area | Preserve row 28px vertical / Phone 22px; article 20px, Home Phone 18px; submit 14px 20px | Component roots; Home selects compact Phone article variant | Current live definitions and Home breakpoint overrides | Compare padding/gap/dimensions and native button tag | Submit state snapshot; keyboard/touch runtime remains separately reported if unavailable |
| Readable max-width | N/A — no typography/layout change; preserve flexible text widths and existing section caps | Existing page sections and component text | [PROJECT brand](../../PROJECT.md#6-brand-direction); current Canvas width chain | Same styles, text bindings, widths and order | Home Phone bounded card fit |
| Editable content / Properties | Preserve CMS variables and Service Row Properties; Article Card remains image/category/title/summary editable; no content variants | CMS and existing Component Properties | [Repeated content](../../../../framer/basic/patterns/pattern-recipes.md#6-repeated-content) | Same collection ids/schema/records; Home new instance binds same fields | Verify sample titles and images are visible; no fabricated demo edits |
| States / routes | Native Hover gestures, stable geometry; Service Phone stays static; Article Phone compact state stays static. One CMS-wrapper link per card. Submit has no navigation link and retains form-submit binding | Definitions own hover; wrappers own CMS route; form owns submit | [Native model](../../../../.agents/skills/framer-interactions/SKILL.md#select-the-native-model); official task-map Components/Forms/CMS/Links guidance | Gesture source/target, wrapper slug bindings, seven enquiry destinations and formSubmitButtonId | Official readiness preview; actual pointer/focus/touch execution pending if not supported by Agent |
| Breakpoint contract | Preserve all existing breakpoints. Home only selects compact Article Phone; archive Phone remains Default. No hover-only content | Existing page replicas and shared visual variants | [State protection](../../../../.agents/skills/framer-interactions/SKILL.md#protect-state-and-breakpoints) | All affected replica values and first/last destinations | Bounded Home Phone render; no claim of whole-site responsive QA |
| Accessibility / touch / focus | Native anchors and native submit button; complete default content; decorative mask ignores pointer; preserve Reduced Motion. Inspect input focus styles and apply missing native visible focus only in Contact | Native links/button/input and project metadata | [State protection](../../../../.agents/skills/framer-interactions/SKILL.md#protect-state-and-breakpoints) | Tags, links, no nested links, pointerEvents none, focused input borders, reducedMotion true | Pointer, focus, touch and Reduced Motion require actual runtime evidence; report Pending instead of inferring from settings |
| Evidence sample | Home/Services first-middle-last rows; Home Project and Article CMS templates; Insights archive; Contact submit; existing Button/ProjectCard/Method Ledger invariants | This request QA | [Implementation verification](../../../../.agents/skills/framer-components/SKILL.md#implement-in-one-layer-at-a-time) | Before/after snapshots and diagnostics; strict repository validator | Maximum three single bounded screenshots; readiness preview is not pointer testing |

## Execution checklist

- [x] Read relocated AGENTS, PROJECT relevant scope, verified audit and change-control rules.
- [x] Reuse connected official Framer Agent session; targeted live readback confirms no prior hover writes.
- [x] Record user requirements, preserve/exclusion lock and Ready component contract before Canvas writes.
- [ ] Bind Home Project/Article wrappers to matching CMS-slug routes on all breakpoints.
- [ ] Normalize only the seven audited enquiry CTA instances and their responsive copies to `/contact`.
- [ ] Add shared Service Row Default Hover with title/top-rule colors; preserve Phone layout/static usability.
- [ ] Add shared Article Default Hover; keep image treatment inside the fixed media frame.
- [ ] Integrate Home article instances, preserving responsive geometry and existing CMS bindings.
- [ ] Add Contact Submit Hover without altering its native form contract; check input focus.
- [ ] Read back all changed component states and representative instances across three breakpoints.
- [ ] Confirm Method Ledger, Button, Project Card, navbar/footer and unrelated content are preserved.
- [ ] Review bounded renders within budget and calculate contrast for changed text/control colors.
- [ ] Run official readiness Preview; distinguish diagnostics from runtime interaction testing.
- [ ] Synchronize PROJECT recovery/status and run strict knowledge validator.

## QA evidence and limits

- Structural evidence: Pending implementation.
- Visual evidence: Pending implementation.
- Actual pointer, keyboard focus, touch and Reduced Motion runtime: Pending; no UI fallback is authorized.
- Contact delivery/successful submission: Outside hover scope; existing recipient/delivery blocker remains.
- Whole-site launch QA and publishing: Not part of this request.
