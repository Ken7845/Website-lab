# Summit Roofing — Repair & Maintenance Page Build

## Status

- Page: Repair & Maintenance
- Path: `/services/repair-maintenance`
- Status: Fix Required — structural implementation was read back, but the 2026-09-16 user visual review found sibling-page duplication, weak page-specific composition and an unfulfilled asset allocation.
- Content status: All explanatory copy is Demo; operational facts remain Missing.
- Primary CTA: Request an Inspection → `/#contact` until the Contact route exists.

## User requirement — verbatim

> strat

## Scope and constraint lock

- **Add:** one authored buyer-facing service-detail page using the existing `Site Shell`, shared Navbar/Footer, shared Button and approved styles.
- **Reuse:** the existing slate-blue/deep-navy/steel-grey system, `Big Shoulders` display type, `Inter` body type, square geometry and zero-radius rule.
- **No-op:** Home, Services, shared Components, CMS Collections, Contact route, forms, publishing and custom code.
- No verified location, pricing, warranty, credential, service area, response time, licence, material-system or emergency claim may be introduced.
- Use Demo copy and the staged image roles: `roofer-ledge.webp`, `roof-work.webp`, and `roof-detail.webp`; factual Alt text is required for every information image.

## Visual Direction Contract

Contract status: Draft

| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |
|---|---|---|---|---|---|
| Design Read | Preserve-mode service-detail correction: practical industrial/editorial language, but a distinct repair-assessment journey rather than another Services overview. | Page | `../../PROJECT.md#6-brand-direction` | Planned page-tree comparison with Services. | Planned full-page Desktop and Phone comparison. |
| Preserve | Keep Big Shoulders and Inter, approved blue-grey tokens, zero-radius geometry, hard rules, shared Site Shell and direct inspection CTA. | Shared system | `../../PROJECT.md#6-brand-direction` | Planned Style, Component and Instance readback. | Planned comparison with approved Home language. |
| Transform | Redesign the masthead hierarchy, Section sequence, image cadence, assessment/work-scope composition and process treatment so the page expresses diagnosis and repair rather than service selection. | Page and Sections | `2026-09-16-page-build.md#page-contract` | Planned Section and breakpoint readback. | Planned full-page rhythm review. |
| Avoid | Do not copy the Services masthead-to-list-to-blue-ledger-to-pale-CTA rhythm, reuse its aerial image without reason, or introduce arbitrary novelty outside the approved system. | Page | `../../PROJECT.md#6-brand-direction` | Planned sibling topology and asset-use comparison. | Planned side-by-side Services and Repair review. |
| Sibling-page delta | Services remains an overview navigator; Repair must lead with condition assessment, use a different dominant composition and media sequence, and avoid the same blue ledger/process silhouette. | Page | `../../PROJECT.md#8-sitemap-and-page-goals` | Planned named-Section and layout-family comparison. | Planned compiled sibling-page comparison. |
| Section composition | Build a page-specific sequence around condition evidence, assessment, repair scope and maintenance decisions; final layout families require design review before Canvas repair. | Page Sections | `2026-09-16-page-build.md#page-contract` | Planned Section ownership map. | Planned composition review before implementation. |
| Colour rhythm | Keep approved token roles while changing their page sequence and visual weight; do not repeat the Services dark masthead, long white body, blue process band and pale CTA rhythm unchanged. | Page and Sections | `../../PROJECT.md#6-brand-direction` | Planned Fill and Color Style readback. | Planned full-page colour-block comparison. |
| Asset map | Use allocated `roofer-ledge.webp`, `roof-work.webp` and `roof-detail.webp` by narrative role; the Services aerial image is not approved for Repair reuse without a recorded reason. | Page image owners | `../../PROJECT.md#11-responsive-interaction-and-assets` | Planned Fill, Alt and breakpoint crop readback. | Planned approved-asset contact sheet plus Canvas review. |
| Responsive transformation | Desktop may use evidence-led asymmetry; Tablet must recompose image/copy pairs; Phone must keep assessment priority, deliberate crops and a clear CTA order rather than merely stacking Desktop. | Page breakpoint owners | `2026-09-16-page-build.md#responsive-and-acceptance-contract` | Planned Desktop 1200, Tablet 810, Phone 390 and stress 320 readback. | Planned representative Desktop, Tablet and Phone evidence. |
| Completion evidence | Overall Pass requires both structural readback and visual proof of composition, colour rhythm, image allocation and sibling differentiation; clean diagnostics alone are insufficient. | QA | `../../../../framer/basic/workflows/preflight-audit.md#2a-visual-composition-and-cross-page-differentiation` | Existing structural readback retained; correction readback planned. | Current user screenshots establish Fix Required; corrected full-page evidence remains planned. |

## Page contract

1. Image-led service masthead with one H1, concise fit statement and inspection CTA.
2. Assessment section explaining what a homeowner can clarify before work begins.
3. Practical work-scope section without promises, warranty terms or invented results.
4. A three-step process that is distinct from the Services-page Method Ledger.
5. A short Demo FAQ that does not imply availability, insurance handling or a guarantee.
6. A quiet final inspection handoff using the existing Button.

## Responsive and acceptance contract

- Desktop 1200: editorial two-column moments only where image and copy need them; bounded reading widths.
- Tablet 810: independently reflow image/copy pairs; no passive shrinking.
- Phone 390 and stress 320: one reading column, clear CTA order, deliberate image crops, no horizontal overflow.
- Verify one H1, purposeful H2/H3 order, semantic Sections, Alt, primary CTA, shared shell, zero radius, reduced-motion safety, and the affected routes.
- Page Done remains blocked until `/contact`, final service destinations, 1440 review and an appropriate Preview path are verified.

## Latest Part Result

- Structural status: Pass — the referenced build task recorded six semantic Sections, one H1, structured Demo FAQ, breakpoint ownership at Desktop 1200, Tablet 810 and Phone 390, factual masthead Alt and clean diagnostics.
- Visual status: Fix Required — the user-provided full-page screenshots show a composition and colour-block rhythm too close to Services; the Services aerial image was reused while the three allocated Repair assets were not fulfilled.
- Fix Required: Compile this Draft contract to Ready, assign the three Repair assets to named narrative roles, redesign the page-specific composition, and later verify it through the official Framer Agent and full-page comparative evidence.
- Blocked: No live Canvas correction or fresh readback is authorised in this repository migration. Contact, 1440 review, 320 visual stress review and final Preview also remain unresolved.

## Evidence required after correction

- Official Framer Agent targeted readback of the new route and Desktop/Tablet/Phone breakpoint structures.
- One efficient full-page or compiled Desktop/Phone comparison that can answer composition, colour rhythm, asset use and sibling differentiation; a target Section screenshot cannot prove the whole page.
- Record current-state and recovery changes in `PROJECT.md`; do not publish.
