# Submit Roofing — Navbar CMS overlays and expandable drawer rows

- Contract schema: 1
- Component contract: Required
- Visual contract: N/A — this is a shared navigation behavior extension, not a visual-direction change.
- Authorization: Authorized by the user request on 2026-10-06.

## Original user requirements

1. “also add this overlay to the projects button and insight button but their overlay rows should be linked to the existing CMS list.”
2. “add unfolded rows to the services row, projects row and insights row in the tablet and phone navbar. In the tablet, hover→ unfold. In the phone, press→ unfold. also add a symbol on the right to indicate that it can be expanded. To make this I think you should turn the row into components.”

## Follow-up requirements — 2026-10-06

1. “change the folded rows in tablet to click→ open”
2. “add hover effects to the unfolded rows in the tablet and press effect in the phone”
3. “add the all projects and all services button to the corresponding overlays in the navbar.”
4. “add a knowledge to the Website_Lab: Usually established: phone→ press and tablet&desktop→ hover”
5. “when add hover to the rows or other stuff, you should fill the rows with the same color with background… Services All Row in the Services component… fill it with pure white.”

## Follow-up requirements — 2026-10-06 (Desktop overlay row reuse and Navbar naming)

1. “replace the rows with Text Row component in the overlays of desktop navbar. don't forget to link them”
2. “then audit all the navbar component and find out the stacks or frames which are not named and name them. follow the naming rule”

## Follow-up constraint lock — Desktop overlays and Navbar naming

- Reuse the existing `Text Row` Component, `Style 1`, for every Desktop overlay row. Preserve the existing Services routes and the Projects / Insights CMS title-and-slug detail links.
- The inspected Desktop Navbar has Services and Projects overlays, but no Insights overlay. Restore the missing Insights overlay using the existing Insights CMS collection; this continues the still-active user-approved Navbar overlay scope.
- Give all three Desktop overlay surfaces the Pure White token so their `Text Row` Default fill matches the immediate background and cannot flash after hover.
- Audit only `Navigation/Navbar` Frame / Stack layers. Name unnamed layers with short, role-based names from `framer/basic/standards/layer-naming.md`; do not rename Text, Icon, or existing named layers without need.
- Preserve all existing Navbar variants, Desktop trigger routes, drawer behavior, token system, CMS data, and publishing state.

## Component Requirement Contract update — Desktop overlay rows and Navbar naming

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
| --- | --- | --- | --- | --- | --- |
| Visible boundary / surface | Use Pure White token for the Desktop overlay surface and `Text Row` Default surface, avoiding hover reset flash. | `Navigation/Navbar` | User follow-up requirement 1; current `Text Row` Default fill | Planned — inspect all three overlay roots and one row per type. | Pending — runtime hover playback. |
| Editable content / Properties | Static Services and archive rows use `Text Row` content/link controls; Projects and Insights CMS repeated rows bind existing title and slug fields to current detail routes. | `Navigation/Navbar` | User follow-up requirement 1; existing CMS lists | Planned — inspect list templates and retained bindings. | Pending — CMS rendered rows. |
| States / routes | Preserve existing overlay triggers and drawer states; only replace child rows and restore the missing Insights Desktop overlay. | `Navigation/Navbar` | Current Canvas readback; prior Navbar contract | Planned — inspect overlay targets, routes and Tablet / Phone state inheritance. | Pending — pointer playback. |
| Layer naming | Name only unnamed Navbar Frames / Stacks with short role-based names. | `Navigation/Navbar` | User follow-up requirement 2; `framer/basic/standards/layer-naming.md#核心原则` | Planned — scan primary and replica Frame names. | N/A — naming is structural. |
| Evidence sample | Verify Services, Projects and Insights overlays, first CMS row templates, all retained routes, and the renamed Navbar Frames. | `Navigation/Navbar` | `framer-components` implementation sequence | Planned — targeted live tree readback. | Pending — Desktop hover playback. |

## Follow-up constraint lock

- Modify the existing named disclosure components and desktop overlays; do not create replacements.
- Tablet folded rows must toggle by click/tap, not by pointer enter/leave. Phone remains press/tap-driven.
- Tablet unfolded child rows receive hover feedback; Phone unfolded child rows receive press feedback. Effects belong to row Frames and retain `scale: 1`.
- Add `All Services` and `All Projects` as normal linked rows to the corresponding desktop overlays, retaining the existing static Services source and Projects CMS rows.
- Extend the existing cross-project interaction baseline rather than creating a project-specific rule: Desktop and Tablet default to hover for pointer feedback; Phone defaults to press for touch feedback. Explicit project evidence may override this default.
- Before a row receives Hover or Press feedback, give its Default row Frame an explicit fill equal to the immediate surrounding surface. For the Services disclosure child rows, that Default fill is Pure White; Hover/Press may then change only the intended feedback surface.

## Authorization and constraint lock

- Modify the existing shared `Navigation/Navbar` component only; do not duplicate page-level navigation.
- Reuse the existing static Services overlay and the existing Projects and Insights CMS collections. Services must remain non-CMS.
- Add desktop hover overlays for Projects and Insights. Their rows must use the existing CMS records and route to their corresponding detail pages.
- Add reusable disclosure rows for Services, Projects, and Insights in the tablet and phone open-navigation states.
- Tablet disclosure toggles by click/tap; phone disclosure is press/tap-triggered. No scale animation is permitted.
- Add a right-aligned expansion indicator to each disclosure trigger. Apply row feedback to the row container, not to its label text.
- Do not alter page content, collection data, routes outside the navigation, the visual system, custom code, or publishing.

## Component Requirement Contract

Contract status: Blocked — structural implementation is complete; browser pointer/touch playback remains required for final runtime acceptance.
Implementation status: Implemented — applied Pure White to the five existing Services child-row Frames without changing labels, links, geometry or effects.
Verification status: Blocked — targeted live readback confirms all five Default fills and preserved links/effects; browser pointer playback remains pending.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
| --- | --- | --- | --- | --- | --- |
| Section background / vertical rhythm | N/A — shared navigation only; retain the existing Navbar surface and drawer rhythm. | `Navigation/Navbar` | Current Canvas: `Navigation/Navbar` variants; user requirement 2 | Pass — [recorded evidence](#qa-evidence-and-limits) retains the existing Navbar and drawer stack ownership. | Blocked — no browser breakpoint preview in this Part. |
| Available width / placement | Desktop overlays anchor below their existing link trigger at the Services panel width; drawer disclosures fill their current row width with a fixed right indicator. | `Navigation/Navbar` and `Navbar Disclosure Row` | Current Canvas: Services overlay is 300px; user requirements 1–2 | Pass — [recorded evidence](#qa-evidence-and-limits) preserves overlay/drawer width ownership. | Blocked — rendered panel alignment and wrapping need Preview. |
| Visible boundary / border / surface | Projects and Insights match the existing light Services panel: light surface, 1px border, no rounded-card treatment. Expanded drawer children remain visibly nested rather than carded. | `Navigation/Navbar` | Current Canvas: `Services Menu Overlay`; user requirement 1 | Pass — [recorded evidence](#qa-evidence-and-limits) records the named light overlay and nested row structures. | Blocked — rendered opened groups need Preview. |
| Internal padding / hit area | Preserve existing Services panel row padding; preserve existing drawer trigger height and extend the indicator’s tap/hover target across the whole trigger row. | `Navbar Disclosure Row` | Current Canvas: Services menu rows and drawer rows; user requirement 2 | Pass — [recorded evidence](#qa-evidence-and-limits) confirms row-owned effects and unchanged geometry. | Blocked — practical target size requires touch/pointer Preview. |
| Readable max-width | N/A — menu labels are short and the existing 300px desktop panel / full-width drawer is the governing readable width. | `Navigation/Navbar` | Current Canvas: existing menu and drawer widths | Pass — [recorded evidence](#qa-evidence-and-limits) records no menu-width or text-width write. | Blocked — longest CMS-label wrapping needs Preview. |
| Editable content / Properties | Projects and Insights read title and slug from existing CMS collections; Services remains static. The reusable row owns indicator/state only, while each Navbar placement owns its label and child destinations. | `Navbar Disclosure Row` plus `Navigation/Navbar` | User requirement 1; current Canvas CMS collections `on7KEF_vG` and `iYJZDQgKb` | Pass — [recorded evidence](#qa-evidence-and-limits) confirms title/slug bindings and static Services ownership. | Blocked — CMS row rendering needs Preview. |
| States / routes | Desktop Projects and Insights use hover show/dismiss overlays. Tablet disclosure toggles by click/tap; Phone disclosure uses press/tap. Revealed rows retain their existing service routes or bind CMS detail routes. No scale effect. | `Navigation/Navbar` and `Navbar Disclosure Row` | Follow-up requirements 1–3 | Pass — [recorded evidence](#qa-evidence-and-limits) covers paired Tablet routes, Phone routes, overlay links and `scale: 1` effects. | Blocked — browser event precedence and route playback need Preview. |
| Breakpoint contract | Desktop uses hover overlays. Tablet uses click/tap disclosure and hover feedback on opened child rows. Phone uses press disclosure and press feedback on opened child rows. | `Navigation/Navbar` variants | Follow-up requirements 1–2; current Canvas variants Desktop / Tablet Open / Phone Open | Pass — [recorded evidence](#qa-evidence-and-limits) confirms named variants and representative row effects. | Blocked — rendered breakpoint transitions need Preview. |
| Accessibility / touch / focus | Use a native `Chevron Down` icon as the non-text expansion affordance; preserve readable text labels and direct child links. Tablet triggers must work by click/tap; Phone triggers and opened rows use press feedback. | `Navbar Disclosure Row` | Follow-up requirements 1–2; Lucide icon-set inspection | Pass — [recorded evidence](#qa-evidence-and-limits) confirms chevrons, direct links and row-owned effects. | Blocked — keyboard, touch and focus execution need Preview. |
| Evidence sample | Verify representative Services, Projects, and Insights rows plus the first and last Projects/Insights CMS items, their child links, and the Desktop / Tablet Open / Phone Open variants. | `Navigation/Navbar` | [Component implementation verification](../../../../.agents/skills/framer-components/SKILL.md#implement-in-one-layer-at-a-time) | Pass — [recorded evidence](#qa-evidence-and-limits) covers representative targets and new all-index rows. | Blocked — browser samples were not authorized or available. |

Actual proof: Framer Agent readback confirms the three named Desktop overlays, all as named `Text Row` instances: Services retains its five static route rows; Projects and Insights retain archive rows plus CMS title/slug detail-link templates. Each overlay surface uses the Pure White token and Mist Grey token border, so its `Text Row` Default fill matches the immediate background. Projects and Insights also match the Services menu’s disclosure ownership: their trigger and child rows are named user-created `Text Row` Component instances; their Tablet Closed triggers use `Style 2`, while Phone Closed/Open and Tablet Open use `Style 1`. Each parent state has the Pure White token fill, `overflow: clip`, and Services-matching `810px` Tablet or `390px` Phone width. Live tree audit found no unnamed Frame or Stack in `Navigation/Navbar`. Runtime browser playback remains pending.

## QA evidence and limits

- Structural result: Pass — live readback confirms the paired Tablet and Phone parent-root routes, three light Desktop overlays, CMS/static links, all-index routes, native chevrons and `overflow: clip` on every folded/unfolded disclosure root. Every Desktop overlay row is a named `Text Row` instance. Projects and Insights match Services with named `Text Row` trigger instances and four named child-row instances each: static archive rows plus CMS title/detail-link rows, including Tablet and Phone replicas. The Navbar Frame / Stack naming audit has no unnamed layers.
- Runtime result: Blocked — the official task-map route does not provide browser pointer, touch or keyboard playback. No UI fallback was authorized.

## Execution checklist

- [x] Inspect the current shared Navbar variants, list patterns, and icon controls before writing.
- [x] Create the reusable disclosure-row components and name their states and instances clearly.
- [x] Add Projects and Insights desktop overlays using the existing CMS collections and their existing detail routes.
- [x] Add Services, Projects, and Insights expandable rows in Tablet Open and Phone Open.
- [x] Verify CMS bindings, routes, interaction triggers, visible indicators, and affected breakpoints.
- [x] Record the final shared-navigation change in the project’s workflow observations and current-state documentation.
