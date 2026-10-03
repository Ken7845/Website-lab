# Submit Roofing — Hover Readiness Audit

## Scope and evidence

- Date: 2026-10-03.
- Status: Audit complete; proposed implementation remains unstarted.
- Source: official Framer Agent session 7, live page trees, Component definitions, CMS variable ownership, Link Styles and root metadata.
- Coverage: all 12 buyer-facing routes, their Desktop / Tablet / Phone owners, eight native Components and shared Navbar/Footer. `/reveal-text-test` was inventoried but excluded from buyer-facing hover work.
- Evidence level: Verified structural settings and routes. Pointer timing, visual contrast during transitions, keyboard focus, touch behaviour and Reduced Motion execution remain Preview checks. No Canvas changes were made during this audit.
- Constraint lock: preserve the user's Method Ledger effect, approved imagery, page composition, content and existing Button reel/filler. Add feedback only where it communicates an action or helps scan repeated information.

## Existing hover systems

| System | Verified current implementation | Recommendation |
|---|---|---|
| Controls/Button | Primary / Secondary with paired native Hover gestures; absolute filler grows from 1px to 100%; arrow track moves from -48px to 0px inside an 18×18 clipped viewport; root uses `spring-duration 0.4s 0.2 0s`, hover filler `spring-physics 250 30 1 0s` | Reuse. Check representative light/dark surfaces and preserve link ownership. |
| Content/Project Card | Default / native Hover; image mask changes from transparent to `rgba(0, 0, 0, 0.32)`; three text nodes use 0.86 opacity on Hover; external geometry is stable; root transition `spring-duration 0.4s 0.2 0s` | Reuse; verify text contrast. Routes belong to the external CMS wrapper, not this Component. |
| Services Method Ledger | Three authored Method Blocks, each with `hoverEffect.backgroundColor: rgba(0, 0, 0, 0.3)` and `spring-duration 0.4s 0.2 0s`; scale 1, x/y 0, rotate/skew 0; inherited in Tablet and Phone. White text over the slate-blue section; no links or pointer cursor | Preserve as the user's informational-row reference. Do not convert it into a clickable control. |
| Navigation link style | Deep Navy → Slate Blue on Hover | Existing feedback is sufficient; no new reel required. |
| Footer link style | White → Mist Grey on Hover | Existing feedback is sufficient; keep external geometry stable. |
| Navbar menu trigger | Tablet outer Menu has 1.05 hover scale; other menu icon effects are present | Lower-priority consistency review: consider colour feedback instead of scale. Preserve drawer state routing. |
| Reduced Motion | Root metadata `reducedMotion: true` | Preserve and verify in Preview; the setting alone is not runtime evidence. |

## Candidate matrix

| Route / area | Current state | Proposed next action | Priority |
|---|---|---|---|
| Home Services + Services Service Navigator | Shared Service Row; Default and Phone layouts; four real service destinations; no hover variant or effect | Modify shared row with title/divider colour feedback. Preserve dimensions, padding and all content. Start without a sweeping filler or whole-row scale. | High |
| Home Featured Work | Shared Project Card already hovers, but CMS wrapper and children have no route on any breakpoint | Bind each Home wrapper to the matching Projects slug, reusing archive routing. Then reuse current Project Card feedback. | Prerequisite |
| Home Insights | Page-authored CMS card, not the shared Article Card; no route or hover on any breakpoint | Bind matching Insights slug; align with shared Article Card only after preserving Home geometry, bindings and editability. Avoid a second separate hover system. | Prerequisite / High |
| Home Process | Three shared Process Step instances; informational and unlinked | Optional subtle surface/divider emphasis inspired by Method Ledger; ordinary cursor and stable text. | Optional |
| Services Working Method | User-authored Method Ledger hover already exists | Preserve; review actual pointer and touch behaviour. | Reuse |
| Repair & Maintenance | Sequence 01–03 and three static FAQ entries are unlinked | Sequence may receive restrained informational emphasis. Leave static FAQ answers fully visible without hover affordances suggesting disclosure. | Optional / No-op |
| Roof Replacement | Handoff Stage 01–03 are unlinked; Decision Notes and three FAQ entries are static | Optional small background emphasis on Handoff stages. Keep opening, explanatory prose and FAQs static. | Optional / No-op |
| New Construction | Scope Rail 01–03 are discrete unlinked rows; Coordination Notes and FAQ entries are static | Optional subtle row tint/divider change on Scope Rails, keeping all details visible. | Optional |
| Storm Damage Repair | Review Notes, Documentation copy and FAQ are static; no distinct linked row/card set | Retain static content; existing CTAs provide actionable feedback. | No-op |
| Projects archive | Lead Project and Project Field wrappers have CMS-slug links and use Project Card | Reuse existing mask hover; verify both lead and repeated archive instances. | Reuse |
| Project Detail | Return to Projects is linked; metadata and project imagery are informational | Keep metadata/static images still. Review or apply existing Body Link Style to the return link. | Low |
| About | Three Working Principles blocks: Clear Assessment, Organised Work, Direct Next Step; unlinked | Optional restrained informational tint like Method Ledger; no pointer cursor, movement or hidden content. | Optional |
| Contact | Separate native Contact Submit Component has one state and no hover; inputs are functional, not cards | Add restrained submit background/label feedback while preserving the native form-submit contract. Do not replace with a navigation Button. Prioritise focus treatment on inputs. | High |
| Insights archive | Shared Article Card Default only; CMS wrapper already links to matching article | Add one shared native Hover gesture, using stable border/title contrast and a mild image treatment. Do not scale the whole card. | High |
| Insight Detail | Long-form article and images, no related-card list currently exists | Keep reading surface static; reuse CTA and link feedback. Do not add a new related-content section just to support hover. | No-op |
| Navbar / Footer | Shared Link Styles already have hover colours | Reuse. Optional text reel only if the user later chooses that direction. | Reuse |

## Link readiness before motion

1. Home Project and Article CMS wrappers have no links at Desktop, Tablet or Phone. Projects and Insights archive wrappers already use their matching slug variables; the same Collections own Home data, so routing can be reused.
2. Seven primary CTA instances still use `/#contact`: Home Team, Services introduction, the four service-detail openings, and Projects opening. This is a valid Home Inspection Handoff anchor at all three breakpoints, but it adds a detour now that `/contact` exists. Recommend normalising enquiry CTAs to `/contact` in the implementation pass.
3. Preserve CMS wrapper link ownership; do not introduce nested links in a card's title/image/Component.

## Implementation order

1. Resolve Home CMS card destinations and the remaining enquiry detours.
2. Add Service Row shared hover and Article Card shared hover. Preserve Phone static usability; Tablet pointer users can receive the same feedback.
3. Give Contact Submit matching feedback through its native submit Component.
4. Test current Project Card and Button hover; keep successful existing states.
5. If desired, add a secondary pass for Process Steps, Repair Sequence, Roof Replacement Handoff Stages, New Construction Scope Rails and About Principles. Follow the Method Ledger's stable geometry and ordinary-cursor behaviour.

The next Canvas pass must compile a Component Requirement Contract before changing reusable state ownership. This audit is an implementation plan, not that contract and not a claim of finished interactions.

## Relevant Website-lab knowledge

- [Motion: buttons, links and component-row hover](../../../../framer/basic/patterns/motion-design.md#component-row-hover) — stable surfaces, shared Gesture Variant versus per-instance effects; no whole-row scaling.
- [Motion: menu/footer/category links](../../../../framer/basic/patterns/motion-design.md#menu-footer-category-link-hover) — colour, opacity, underline/divider feedback for dense links.
- [Buttons](../../../../framer/basic/patterns/buttons.md#hover-与-variant) — stable dimensions, Properties, Variant and link boundaries.
- [Image workflow](../../../../framer/basic/workflows/image-workflow.md#9-framer-中的图片结构) — clip the outer media frame; animate only the inner image if zoom is chosen. Existing direct image fills must be inspected before adding this structure.
- [Button filler hover](../../../../framer/advance-design/aurelia/button-filler-hover.md) — internal filler ownership; AURELIA's bottom-up red example is legacy project provenance, not Submit Roofing's colour/direction source.
- [Reel Text + Button Arrow](../../../../framer/advance-design/aurelia/reel-relative-design.md) — existing Button arrow geometry and optional short-label reel. Do not apply to paragraphs or multiline card titles.
- [Custom Cursor Hover Preview](../../../../framer/advance-design/ken-studio/custom-cursor-hover-preview.md) — reviewed for suitability; not recommended for this pass because project cards already expose their images and information.
- [Framer interactions Skill](../../../../.agents/skills/framer-interactions/SKILL.md) — state routing, touch and Reduced Motion requirements.

## Required verification for implementation

- Default/Hover external width, height, padding, grid/stack flow and neighbouring positions stay stable.
- Linked cards/rows retain one correct destination; test first and last CMS items.
- Informational blocks keep an ordinary cursor; all information is visible without Hover.
- Test one actual pointer path, focus/keyboard navigation, touch activation and Reduced Motion.
- Validate contrast during both default and hover states against their actual parent surfaces.
- Read back Desktop / Tablet / Phone overrides; check narrow 320px and wide 1440px fit where geometry changed.
- Contact Submit continues to submit the form rather than navigate.
