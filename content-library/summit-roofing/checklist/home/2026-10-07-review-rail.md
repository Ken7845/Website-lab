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

Contract status: Blocked — implemented with structural readback; runtime Preview remains pending.

Implementation status: Implemented
Verification status: Blocked — structural contract passes; Preview evidence is pending.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Page-owned Deep Navy Review Section is inserted after Featured Work and before Process. | Home page | User request; live Home section order | Pass — [recorded evidence](#result); sibling order and section fill read back. | Blocked — bounded section rhythm pending. |
| Available width / placement | Page owns the available-width split; `Review Rail` fills the viewport column and owns only its internal track. | Home page + `Review Rail` | `.agents/skills/framer-components/SKILL.md#assign-responsibility` | Pass — [recorded evidence](#result); page instance fills the available column at all three breakpoints. | Blocked — no horizontal overflow Preview pending. |
| Visible boundary / border / surface | Rail uses Pure White default surface; controls use explicit token-backed surfaces. No new colours, shadows or radius. | `Review Rail` | `../../PROJECT.md#6-brand-direction`; user token rule | Pass — [recorded evidence](#result); named token fills, borders and square geometry read back. | Blocked — hover/press surfaces Preview pending. |
| Internal padding / hit area | Rail owns card padding and previous/next button hit areas; the page owns exterior Section padding. | `Review Rail` | `.agents/skills/framer-components/SKILL.md#assign-responsibility` | Pass — [recorded evidence](#result); component card padding and native button roots read back. | Blocked — usable pointer/touch controls pending. |
| Readable max-width | Page split and Review Rail card padding govern line length; no arbitrary card cap outside the rail viewport. | Home page + `Review Rail` | `../../../../framer/basic/standards/website-baseline.md#长条边框组件的宽度归属` | Pass — [recorded evidence](#result); Section split and rail padding govern the reading line. | Blocked — quote wrapping Preview pending. |
| Editable content / Properties | Expose three Demo quote/name/context property groups and a visible index; no CMS is added while real records are Missing. | `Review Rail` | `.agents/skills/framer-components/SKILL.md#assign-responsibility`; `../../PROJECT.md#7-content-facts` | Pass — [recorded evidence](#result); all nine content properties bind to the Home instance. | N/A — content properties are structural. |
| States / routes | Each breakpoint has Slide 1–3 states. Previous/next buttons route cyclically and move only the clipped horizontal track; arrow hover/press is visual feedback, not a content state. | `Review Rail` | User request; `../../../../framer/basic/patterns/pattern-recipes.md#6-repeated-content` | Pass — [recorded evidence](#result); all nine named states and representative cyclic routes read back. | Blocked — next/previous playback pending. |
| Breakpoint contract | Desktop/Tablet use hover feedback plus click; Phone uses tap and no-scale press feedback. | `Review Rail` | `../../PROJECT.md#11-responsive-interaction-and-assets`; user interaction convention | Pass — [recorded evidence](#result); matching starting state, hover effect and no-scale tap effect read back. | Blocked — Desktop/Tablet pointer and Phone tap pending. |
| Accessibility / touch / focus | Previous/next controls are native buttons with labels; visible index and no hover-only content path; reduced motion must keep state changes comprehensible. | `Review Rail` | `../../PROJECT.md#10-system-and-platform-plan` | Pass — [recorded evidence](#result); native buttons, text labels and visible index read back. | Blocked — keyboard/focus path pending. |
| Evidence sample | Verify component definition, Home instance, Desktop/Tablet/Phone state selections, token fills and routes. | Home page + `Review Rail` | `.agents/skills/framer-components/SKILL.md#implement-in-one-layer-at-a-time` | Pass — [recorded evidence](#result); targeted live readback completed. | Blocked — bounded Preview pending. |

## Result

- Structural status: Pass — Home now has one named Client Perspective section after Featured Work and before Process. It includes the scoped `Review Rail` component, a clipped horizontal track, three editable Demo reference records and nine named responsive Slide states.
- Runtime / visual status: Blocked — actual Desktop/Tablet hover, Phone tap/press, keyboard/focus and rendered composition still require Preview evidence.
- No CMS collection, review facts, rating, image, new colour, Custom Code, paid dependency, other route or publication was added.
