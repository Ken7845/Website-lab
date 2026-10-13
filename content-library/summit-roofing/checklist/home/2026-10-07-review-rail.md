# Summit Roofing — Home Review Rail

- Contract schema: 1
- Component contract: Required
- Visual contract: Required
- Authorization: Authorized — user said “START” on 2026-10-07 after reviewing the horizontal review-section plan.

## User request

- “now I want to make a review section in the homepage. plan this section. it can switch horizontal”
- “START”

## Constraint lock

- **Goal:** Add one horizontally switchable review section to `/`, placed between Featured Work and Process.
- **Preserve:** Homepage shell, all existing Sections, Big Shoulders / Inter, square geometry, named token palette, and current Desktop / Tablet / Phone page structure.
- **Create:** One native `Review Rail` component with named responsive slide states and editable fields for three review records.
- **Content:** Reviews, reviewer identities, ratings, project results, locations and service outcomes are Missing. The initial visible content is complete, fictional `Demo` reference copy under the existing project authorization; it must not claim verified endorsement, a rating, outcome, location or service fact.
- **Do not modify:** Navbar, Footer, existing CMS collections, Form delivery, shared Button contract, colours, assets, page metadata, other routes, Custom Code, paid dependencies or publishing.
- **Verification:** Read the component definition, Home instances and all three breakpoint selections. Preview must test previous/next navigation, Desktop/Tablet hover and Phone tap/press; until then runtime remains Blocked.

## Follow-up constraint lock — Review Rail correction and layer naming

- **Still required:** Keep the Home-only proof-to-process section after Featured Work and before Process; preserve the deep-navy band, square blue-grey system, three editable Demo review records, cyclic previous/next behavior, and Desktop / Tablet / Phone coverage.
- **This correction:** Replace the current rigid, oversized Review Rail composition with a fluid, more balanced card and control layout; shorten the three record property groups to concise, understandable labels; audit page Sections and native Components for unnamed Frame layers and name them by their local role.
- **Do not change:** Brand naming, review facts or Demo content, other section order, non-Home page composition, shared styles/tokens, CMS, imagery, button contracts, code, paid dependencies, or publishing.
- **Verify:** Review Rail definition, Home Section and its three breakpoint instances; confirm property labels and routes remain intact; re-scan all page and native Component Frame layers, protect any enabled Scroll Target / `elementId`, and confirm no unnamed Frames remain. Runtime interaction remains subject to Preview evidence.

## Follow-up constraint lock — Review Rail reel principle

- **Still required:** Preserve the Home-only Client Perspective section, three editable Demo reviews, concise properties, responsive states, and cyclic Previous / Next behavior.
- **This correction:** Make the Review Rail follow the fixed-viewport, continuous-track principle from `framer/advance-design/aurelia/dish-selector-image-matrix.md`: each slide must match its viewport width, adjacent slide positions must use that exact pitch, and state changes move the same track by one pitch. Keep review copy in whole cards; the short-label vertical reel from `reel-relative-design.md` is not suitable for multi-line quotes.
- **Do not change:** Demo values, property names, section order, Home layout, colors, assets, shared button contracts, CMS, other routes, publishing, or code.
- **Verify:** Read all nine state offsets, Desktop/Tablet/Phone slide widths and pitch, bindings and cyclic routes; check the rendered Home rail and operate Previous / Next in Preview.

## Component Requirement Contract — correction

Contract status: Implemented — preserves the approved section and interaction direction while repairing the component’s internal layout and property labels.

Implementation status: Complete
Verification status: Structural Pass; final rendered and runtime Preview pending.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Preserve the existing Home-owned deep-navy band and position between Featured Work and Process. | Home Section | Original [Visual Direction Contract](#visual-direction-contract); follow-up constraint lock | Planned — verify existing sibling order and fill after replacement. | Planned — inspect the adjacent Home bands. |
| Available width / placement | Make the rail fluid in the Home split column; avoid the current fixed 640px root and track assumptions. | `Review Rail` | `.agents/skills/framer-components/SKILL.md#assign-responsibility`; live definition readback | Planned — verify root and Home instances at all breakpoints. | Planned — check horizontal overflow at Desktop and Phone. |
| Visible boundary / border / surface | Keep existing named white/navy tokens, square geometry and restrained 1px boundary; add no style token. | `Review Rail` | `../../PROJECT.md#6-brand-direction`; original component readback | Planned — verify token-backed fills/border and 0px geometry. | Planned — inspect contrast and rendered hierarchy. |
| Internal padding / hit area | Use balanced card padding and equal, compact previous/next controls; keep the page responsible for outer Section padding. | `Review Rail` | `.agents/skills/framer-components/SKILL.md#assign-responsibility`; `../../../../framer/basic/standards/layer-naming.md#0-简洁清楚有区分度` | Planned — verify card and button dimensions. | Planned — check readable quote wrapping and usable controls. |
| Readable max-width | Rail fills its page-owned viewport; quote line length is governed by card padding and responsive width. | Home Section + `Review Rail` | `../../../../framer/basic/standards/website-baseline.md#长条边框组件的宽度归属` | Planned — verify fluid viewport and slide widths. | Planned — inspect line length at Desktop and Phone. |
| Editable content / Properties | Keep nine editable fields, relabeled `Quote 1–3`, `Name 1–3`, and `Context 1–3`; keep existing Demo values. | `Review Rail` | `.agents/skills/framer-components/SKILL.md#preserve-behavior-and-editability`; `../../PROJECT.md#7-content-facts` | Planned — verify all bindings and Home values. | N/A — names/values are structural; no review facts are asserted. |
| States / routes | Preserve nine slide states and cyclic Previous/Next routing; use one continuous clipped track, with each slide equal to its viewport and each state moving exactly one slide pitch. | `Review Rail` | `../../../../framer/advance-design/aurelia/dish-selector-image-matrix.md#图片矩阵的核心固定裁切框移动单一轨道`; original [Component Requirement Contract](#component-requirement-contract) | Planned — verify every route target, slide width and exact track offset. | Planned — exercise Previous/Next at all breakpoints. |
| Breakpoint contract | Keep Desktop, Tablet and Phone states; make cards and controls adapt to available width while retaining tap-safe Phone behavior. | `Review Rail` | `../../PROJECT.md#11-responsive-interaction-and-assets` | Planned — inspect all nine states and three Home selections. | Planned — check Desktop/Tablet hover and Phone tap/press. |
| Accessibility / touch / focus | Keep native buttons and visible Previous/Next labels/index; retain a keyboard path and no hover-only content. | `Review Rail` | `../../PROJECT.md#10-system-and-platform-plan` | Planned — verify button tags, labels and index. | Planned — inspect focus and keyboard navigation. |
| Evidence sample | Read the component definition, Home Section, three instances, all unnamed Frame layers and Scroll Target attributes. | Home + all native Components | `.agents/skills/framer-components/SKILL.md#implement-in-one-layer-at-a-time`; `../../../../framer/basic/standards/layer-naming.md#ai-agent-操作-framer-时遵守` | Planned — audit all pages/components and confirm zero unnamed Frames. | Planned — bounded Desktop and Phone review. |

## Visual Direction Contract

Contract status: Blocked — implemented with structural readback; bounded visual and runtime Preview remain pending.

Implementation status: Implemented
Verification status: Blocked — structural contract passes; Preview evidence is pending.

| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |
|---|---|---|---|---|---|
| Design Read | A proof-to-process bridge: one focused review rail, not a ratings wall or generic card grid. | Home Review Section | User request; `../../PROJECT.md#4-website-goal` | Pass — [recorded evidence](#result); named Section and rail placed after Featured Work. | Blocked — bounded Desktop section review pending. |
| Preserve | Keep the existing blue-grey palette, Big Shoulders / Inter pairing, crisp square geometry and direct conversion rhythm. | Shared system | `../../PROJECT.md#6-brand-direction` | Pass — [recorded evidence](#result); existing named tokens and fonts read back. | Blocked — adjacent-band rhythm review pending. |
| Transform | Add a dark evidence band with a horizontal, single-active-review rail between project proof and process explanation. | Home Review Section | User-approved plan, 2026-10-07 | Pass — [recorded evidence](#result); section order, nine named Slide states and clipped viewport read back. | Blocked — directional motion Preview pending. |
| Avoid | No claimed testimonial, star rating, trust badge, metric, portrait, unrelated image, generic three-card grid, Custom Code or new colour. | Home Review Section | `../../PROJECT.md#2-scope-and-authority`; `../../PROJECT.md#7-content-facts` | Pass — [recorded evidence](#result); fictional Demo reference copy has no claimed outcome; no asset, CMS, code or token addition. | Blocked — rendered absence review pending. |
| Sibling-page delta | Home may carry a compact trust bridge after Featured Work; About remains standards/people-focused and Projects remains the evidence archive. | Home Review Section | `../../PROJECT.md#9-narrative-and-conversion` | Pass — [recorded evidence](#result); Home-only section and sibling preservation. | Blocked — Home flow review pending. |
| Section composition | Deep Navy section; display heading and visitor-facing copy at the leading edge; Pure White clipped review viewport; compact previous/next controls and index. | Home Review Section + Review Rail | User-approved plan, 2026-10-07 | Pass — [recorded evidence](#result); fills, containment and child hierarchy read back. | Blocked — one active card and controls Preview pending. |
| Colour rhythm | Featured Work → Deep Navy review rail → Soft White Process, using only existing named tokens. | Home Review Section | `../../PROJECT.md#6-brand-direction` | Pass — [recorded evidence](#result); order and named Deep Navy surface read back. | Blocked — adjacent-band rhythm pending. |
| Asset map | N/A — no image or avatar is needed for the reference review format. | Home Review Section | `../../PROJECT.md#7-content-facts` | Pass — [recorded evidence](#result); no image-node scan found an asset in this Section. | N/A — no image claim. |
| Responsive transformation | Desktop is a split heading/viewport field; Tablet narrows the split; Phone stacks heading, card and controls while keeping tap navigation. | Home Review Section + Review Rail | User request; `../../PROJECT.md#11-responsive-interaction-and-assets` | Pass — [recorded evidence](#result); matching Desktop, Tablet and Phone starting variants and page layouts read back. | Blocked — Desktop and Phone interaction review pending. |
| Completion evidence | Structural readback, one bounded Desktop composition check, and actual Desktop/Tablet/Phone navigation paths. | QA | `../../../../framer/checklist.md#section-done` | Pass — [recorded evidence](#result); tree, state-route and responsive-instance checks completed. | Blocked — Preview interaction path pending. |

## Component Requirement Contract

Contract status: Blocked — structural readback passes; final rendered and runtime Preview remain pending.

Implementation status: Partial — component geometry and routes are implemented; final visual/runtime verification remains.
Verification status: Blocked — final Phone visual and runtime Preview are pending.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Page-owned Deep Navy Review Section is inserted after Featured Work and before Process. | Home page | User request; live Home section order | Pass — [recorded evidence](#result); sibling order and section fill read back. | Blocked — bounded section rhythm pending. |
| Available width / placement | Page owns the available-width split; `Review Rail` fills the viewport column and owns a single continuous track whose three equal-width cards align to one viewport pitch. | Home page + `Review Rail` | `.agents/skills/framer-components/SKILL.md#assign-responsibility`; `../../../../framer/advance-design/aurelia/dish-selector-image-matrix.md#图片矩阵的核心固定裁切框移动单一轨道` | Pass — [recorded evidence](#follow-up-result-2026-10-09); all 9 states read back with Desktop 560px, Tablet 337px and Phone 350px slide pitch. | Blocked — final Phone Preview pending. |
| Visible boundary / border / surface | Rail uses Pure White default surface; controls use explicit token-backed surfaces. No new colours, shadows or radius. | `Review Rail` | `../../PROJECT.md#6-brand-direction`; user token rule | Pass — [recorded evidence](#result); named token fills, borders and square geometry read back. | Blocked — hover/press surfaces Preview pending. |
| Internal padding / hit area | Rail owns card padding and previous/next button hit areas; Phone uses compact 20px horizontal card padding and 16px card gap so wrapped quote, metadata and controls fit the existing viewport. | `Review Rail` | `.agents/skills/framer-components/SKILL.md#assign-responsibility`; user follow-up; `../../../../framer/advance-design/aurelia/dish-selector-image-matrix.md#文字改变后的对齐策略` | Pass — [recorded evidence](#follow-up-result-2026-10-09); responsive quote width, Phone quote window and card spacing read back. | Blocked — final Phone rendered composition and tap path pending. |
| Readable max-width | Page split and Review Rail card padding govern line length; no arbitrary card cap outside the rail viewport. | Home page + `Review Rail` | `../../../../framer/basic/standards/website-baseline.md#长条边框组件的宽度归属` | Pass — [recorded evidence](#result); Section split and rail padding govern the reading line. | Blocked — quote wrapping Preview pending. |
| Editable content / Properties | Expose three Demo quote/name/context property groups and a visible index; no CMS is added while real records are Missing. | `Review Rail` | `.agents/skills/framer-components/SKILL.md#assign-responsibility`; `../../PROJECT.md#7-content-facts` | Pass — [recorded evidence](#result); all nine content properties bind to the Home instance. | N/A — content properties are structural. |
| States / routes | Each breakpoint has Slide 1–3 states. Previous/Next moves the same clipped track by exactly one card pitch and wraps at both ends. | `Review Rail` | User follow-up; `../../../../framer/advance-design/aurelia/dish-selector-image-matrix.md#图片矩阵的核心固定裁切框移动单一轨道` | Pass — [recorded evidence](#follow-up-result-2026-10-09); all 9 track offsets and all 18 Previous/Next targets read back. | Blocked — playback in Preview pending. |
| Breakpoint contract | Desktop/Tablet use hover feedback plus click; Phone uses tap and no-scale press feedback. | `Review Rail` | `../../PROJECT.md#11-responsive-interaction-and-assets`; user interaction convention | Pass — [recorded evidence](#result); matching starting state, hover effect and no-scale tap effect read back. | Blocked — Desktop/Tablet pointer and Phone tap pending. |
| Accessibility / touch / focus | Previous/next controls are native buttons with labels; visible index and no hover-only content path; reduced motion must keep state changes comprehensible. | `Review Rail` | `../../PROJECT.md#10-system-and-platform-plan` | Pass — [recorded evidence](#result); native buttons, text labels and visible index read back. | Blocked — keyboard/focus path pending. |
| Evidence sample | Verify component definition, nine responsive states, all slide positions, quote widths, token fills and routes. | `Review Rail` | `.agents/skills/framer-components/SKILL.md#implement-in-one-layer-at-a-time` | Pass — [recorded evidence](#follow-up-result-2026-10-09); all state geometry, nine property names and cyclic routes read back. | Blocked — Desktop screenshot is readable; final Phone rendered composition and interactions remain pending. |

## Result

- Structural status: Pass — Home now has one named Client Perspective section after Featured Work and before Process. It includes the scoped `Review Rail` component, a clipped horizontal track, three editable Demo reference records and nine named responsive Slide states.
- Runtime / visual status: Blocked — actual Desktop/Tablet hover, Phone tap/press, keyboard/focus and rendered composition still require Preview evidence.
- No CMS collection, review facts, rating, image, new colour, Custom Code, paid dependency, other route or publication was added.

## Follow-up result — 2026-10-08

- Structural status: Pass — renamed the nine component controls to `Quote 1–3`, `Name 1–3`, and `Context 1–3`; reduced the Desktop / Tablet / Phone viewport heights to 240px / 220px / 200px; retained all nine responsive states and cyclic Previous / Next destinations. The Home instances remain bound to the same Demo values and breakpoints.
- Layer naming status: Pass — scanned 1,014 Frame layers across buyer-facing routes and native Component scopes; zero blank or default-named Frames remain. Existing Scroll Target / `elementId` values were not targeted by the naming changes.
- Rendered status: Blocked — the two planned captures predate the final viewport-height reduction. The Phone capture showed readable content but excessive whitespace; the Desktop capture was clipped in its screenshot frame. Final rendered composition needs a Preview re-check.
- Runtime status: Blocked — pointer, touch, keyboard/focus and motion playback were not exercised in Preview. Structural readback confirms cyclic routing for all nine states.
- Scope retained: No review facts, CMS, assets, shared styles, other routes, code, paid dependencies or publishing changes.

## Follow-up result — 2026-10-09

- Structural status: Pass — corrected the continuous track to use exact slide pitch, matched track/card heights to the clipped 240px / 220px / 200px viewports, and made the first quote fill its responsive text wrapper. Phone uses a 90px quote window with compact card padding and gap.
- Route status: Pass — read back all nine track positions and all 18 Previous/Next targets; both controls wrap cyclically for Desktop, Tablet and Phone.
- Rendered status: Partial — Desktop capture shows the full quote, author/context and controls. The initial Phone capture exposed a fixed-width quote; after the width repair, the quote aligned within the card. The last structural tightening was not captured, and the screenshot did not show metadata/controls clearly enough to claim final rendered acceptance.
- Runtime status: Blocked — no interaction playback or keyboard/focus path was exercised in Preview.
- Scope retained: Demo content, nine short property labels, section order, Home layout, existing colors/tokens, assets, shared button contracts and other routes remain unchanged; no CMS, code, paid dependency or publication change.
