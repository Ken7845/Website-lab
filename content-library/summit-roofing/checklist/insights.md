# Summit Roofing — Insights Archive Checklist

## Status

- Page: Insights
- Path: `/insights`
- Current status: In progress — Structural Pass at Desktop, Tablet and Phone; visual review and Insight Detail remain pending.
- Content status: Existing Insights CMS titles, categories, summaries and image Alts are Demo. Article-body content, publishing cadence, authors, dates, legal/privacy information and image licences are Missing.
- Primary CTA: `Explore Services` → `/services`.

## Scope lock / Definition of Ready

- **Add:** one Insights archive bound only to the existing `Insights` CMS fields: Title, Category, Summary and Image.
- **Reuse:** Site Shell, Article Card, Button, Big Shoulders / Inter, blue-grey tokens, square geometry and responsive system.
- **Modify:** `/insights` only. **No-op:** CMS schema/items, Article Card definition, Navbar/Footer, contact page, Custom Code, publishing and the unbuilt Insight Detail route.
- **Blocked:** article-body content, detail route, actual editorial claims, author/date facts, licences and publication authorization. Cards must not link to the not-yet-existing detail route.

## Visual Direction Contract

Contract status: Blocked — structural evidence is recorded; visual evidence is pending for this Part.

| Concern | Decision / N/A reason | Owner | Governing source | Structural proof | Visual proof |
|---|---|---|---|---|---|
| Design Read | A practical roof-notes field, not a generic blog wall or a media publication. | Page | `../PROJECT.md#4-website-goal` | One H1, named Sections and CMS list. | One bounded Desktop review. |
| Preserve | Shared shell, condensed display type, blue-grey tokens, square geometry and restrained work imagery. | Shared system | `../PROJECT.md#6-brand-direction` | Shell/style/Card/Button readback. | Compare with live siblings. |
| Transform | Make the archive itself the evidence field: a dark editorial threshold followed by a contained CMS article grid. | Page | `insights.md#page-narrative-and-sections` | Four Sections and collection owner. | Distinct archive rhythm. |
| Avoid | No invented authors, dates, advice claims, search/filter system, tag cloud, newsletter, metrics or dead detail links. | Page | `../PROJECT.md#7-content-facts` | CMS/link readback. | Desktop exclusion check. |
| Sibling-page delta | Insights is an educational field, not Projects' work archive or Contact's request desk. | Page | `../PROJECT.md#9-narrative-and-conversion` | Section/CMS comparison. | One distinct memory point. |
| Section composition | Deep-navy notes threshold; mist editorial context; soft-white CMS field; slate-blue service handoff. | Page | `insights.md#page-narrative-and-sections` | Fill/width owner readback. | Colour and hierarchy review. |
| Colour rhythm | Deep navy / mist / soft white / slate blue. | Page | `../PROJECT.md#6-brand-direction` | Token readback. | Desktop review. |
| Asset map | Article Card receives only the existing CMS Image field and its current Alt. No static photo is allocated. | CMS | `../PROJECT.md#11-responsive-interaction-and-assets` | CMS binding readback. | Existing image-role review. |
| Responsive transformation | Desktop uses a two-column article field; Tablet stabilizes the same field; Phone becomes one readable article column with 20px gutters. | Breakpoints | `insights.md#image-responsive-interaction-and-accessibility` | 1200/810/390 readback. | Desktop review; Phone later only if needed. |
| Completion evidence | Structural: semantic Sections, CMS bindings, Article Card instances, truthful Demo state, links and breakpoint owners. Visual: bounded composition proof. | QA | `../../../framer/checklist.md#2-每个-part-的通用完成门槛` | Diagnostics/readback. | Recorded plan and one review. |

## Page narrative and Sections

1. **Practical Notes Threshold** — deep-navy H1 opening: `PRACTICAL ROOF NOTES, READY TO EDIT.` It presents the archive as editable Demo guidance, not published expertise.
2. **Editorial Context** — mist statement explaining that article titles and summaries are CMS-managed Demo content pending verified guidance.
3. **Current Articles Field** — soft-white collection list using Article Card instances bound only to current Title, Category, Summary and Image fields. No detail link appears until `/insights/:Insights` exists.
4. **Service Handoff** — slate-blue close with `Explore Services` → `/services`.

## Text, components, CMS and links

- Reuse display/body styles; one H1 and H2 section titles. Name layers by content responsibility.
- Reuse Article Card and Button; create no CMS field, CMS item, Component, Variant, form, filter or Custom Code.
- The collection list owns the `Insights` collection and repeats one article wrapper. Each Article Card binds `Title`, `Category`, `Summary`, and `Image` directly from the item variables.
- Cards remain non-linked while the Insight Detail route is unbuilt. Only the closing Button links to the existing `/services` route.

## Image, responsive, interaction and accessibility

- Use only the current CMS Image and its attached Alt. No static source image is added or reopened.
- Desktop 1200 owns a two-column article field; Tablet 810 retains two readable columns; Phone 390 becomes one article column with 20px outer gutters. Defer 320/1440 stress checks.
- Preserve reading order, visible focus, keyboard order and reduced motion. No hover-only content, overlay, Lightbox or motion is added.

## SEO, performance, Marketplace and Preview

- Metadata: `Insights | Summit Roofing`; `Editable roofing guidance archive for a contractor template. Update article content before publishing.`
- No third-party dependency is added. Marketplace stress: long titles/summaries, absent optional article detail, different CMS image ratios and empty future archive state must remain editable.
- Targeted Preview path: `/insights`. Publication and Insight Detail navigation are excluded.

## Page Done threshold

- `/insights` has metadata, shared shell/Card/Button, four semantic Sections, one H1, truthful Demo content, a CMS collection-list owner and independent breakpoint owners.
- No CMS facts are fabricated or changed; no card reaches an unbuilt detail route. Visual evidence, stress widths, Preview and the Insight Detail route remain explicit work.

## Latest Part Result

Scope: Insights archive build and structural QA
Status: Structural Pass / Visual Blocked

Pass:
- `/insights` is live with Site Shell metadata, four named semantic Sections, one H1 and three H2s, truthful Demo-state messaging and an `Explore Services` CTA to `/services`.
- The CMS collection list owns the existing `Insights` collection and repeats Article Card with its full Image, Category, Title and Summary controls bound to the current item variables. No CMS collection, field or item changed.
- Structural readback confirms Desktop 1200 and Tablet 810 use two article columns; Phone 390 uses one article column with 20px page gutters.
- Cards have no dead Insight Detail links while the detail route is unbuilt. No shared component, Custom Code, form, external dependency or publishing action changed.

Fix Required:
- None in the authorized `/insights` scope.

Blocked:
- Bounded visual review is not run in this build Part; it requires a separately scoped visual QA Part.
- Article-body fields, factual editorial content, the Insight Detail route, licences and publication authorization.

Verified widths:
- Structural: Desktop 1200, Tablet 810 and Phone 390.
- Deferred: 320 and 1440 stress widths, visual composition review, Preview and article-detail navigation.

Verified paths:
- `/insights`; closing CTA `/services`.

Shared components affected:
- Reused only: Site Shell, Article Card and Button; no shared-component modification.

Recovery:
- Canonical current pointer: `../PROJECT.md#14-recovery`
- This Part result date: 2026-09-18
