# Ken Studio active decisions

Preserved from the former PROJECT; dated decisions are not new Canvas evidence. [Project entry](./PROJECT.md).

## 19. Decisions and Exceptions

| Decision | Reason | Scope | Date |
|---|---|---|---|
| `/works` typography and spacing become the full-site baseline | It currently expresses the intended quiet archive language most clearly | Website | 2026-07-18 |
| Boldonse is reserved for page-level display titles | Its weight is distinctive but becomes loud and difficult when repeated densely | Website | 2026-07-18 |
| Inter Display carries structural hierarchy | It connects large archive titles, lead statements, rows and metadata without adding another font | Website | 2026-07-18 |
| Libre Baskerville is a restrained reading voice | It supports observation and reflection while remaining secondary to images | Website | 2026-07-18 |
| BDO Grotesk is not part of the core type system yet | No required role is currently established by Works | Website | 2026-07-18 |
| The site remains dark-theme locked | Works and Brand Voice rely on soft white type over near-black surfaces | Website | 2026-07-18 |
| Red and yellow remain category signals | They distinguish Observation and Creation without creating a broad decorative palette | Works and related navigation | 2026-07-18 |
| Current custom cursor is a Works-only exception | It is already the latest project-specific interaction, but must not become a global cursor and requires keyboard, touch and reduced-motion fallbacks | Works, pointer devices only | 2026-07-18 |
| Native Framer patterns remain the default | Components, Variants, Styles, Stacks, Breakpoints and native Effects are more maintainable for the known fixed content | Website | 2026-07-18 |
| No publishing without explicit approval | Routes and formal content remain incomplete | Website | 2026-07-18 |
| Home narrative does not move directly from a generic Hero to a project grid | The site needs to establish how external observation becomes internal form before presenting an archive or service | Home | 2026-07-18 |
| Photography and mandala painting are connected through attention, rhythm and structure | The abstract paintings are not literal depictions of photographed subjects | Home / Observation → Creation bridge | 2026-07-18 |
| Preserve the current user-built Creation reveal | The previous agent implementation was rejected; current canvas geometry and scroll relationships are the implementation source | Home / Creation Reveal | 2026-07-26 |
| DOMT's white field is treated as artwork content | It is an intentional local visual event, not permission to introduce a general paper-themed site skin | Home / Creation Reveal | 2026-07-18 |
| Home Creation no longer opens with the old four-cover website grid | Painting is the primary Creation narrative; website practice should appear later as structure made usable, not as a generic product display | Home / Creation | 2026-07-18 |
| Creation writing may draw from Jung's *The Red Book* as a reference | The paintings were made in dialogue with its mandalas and inner-symbolic language; copy may use restrained mythic and theological imagery without imitation or false quotation | Home / Painting Continuum | 2026-07-26 |
| Creation receives an opaque Background / Base surface | The preceding sticky reveal must not remain visible beneath the introduction and first artwork; the fill establishes a readable content plane without changing the reveal targets | Home / Painting Continuum | 2026-07-26 |
| Creation and Digital Form headings reuse the existing `Heading/Section` H2 preset | The project already has canonical H1, H2 and paragraph roles; section copy must not introduce a parallel display style | Home / Creation | 2026-07-27 |
| Website Practice begins only after the third painting | It preserves the inward-form narrative before translating structure into usable digital space | Home / Website Practice | 2026-07-27 |
| Website covers have no new scroll animation | Appending content must not add or rename reveal targets; a foreground Background / Base surface provides visual separation instead | Home / Website Practice | 2026-07-27 |
| Repeated Creation and Digital Form title groups use the native `SectionTitle` component | Their structure and typography are identical; Eyebrow, Heading and Description are exposed as content properties while existing Meta/H2/P presets remain authoritative | Home / Creation | 2026-07-27 |
| Painting rows remain page-scoped despite the maintenance goal | A hidden component test proved Framer rejects page Scroll Section targets from inside a component and exposes no instance-descendant override path; replacing the rows would remove the independent Image/Copy entrance sequence | Home / Painting Continuum | 2026-07-27 |
| Footer variants share the phone-derived paired layout | One shared Footer now provides a stable left wordmark and right navigation at Desktop, Tablet and Phone; only confirmed non-draft routes are linked | Shared Footer | 2026-07-27 |
| Layer names use the shortest clear expression inside their parent context | Repeating ancestor or Section prefixes makes the tree slower to scan without adding meaning; Scroll Target names remain the exact `elementId` exception | Website | 2026-07-29 |
| `ArchiveOptionRow` is a record-agnostic template | Record content, link, base fill, hover fill and cursor selection belong to page instances; only Desktop and Phone express structural differences | Works | 2026-07-29 |
| Creation keeps Inner Form and Digital Form inside the same folder | Home establishes painting and website practice as two expressions of Creation; five painting rows and one Morrow & Grain Demo row preserve that hierarchy | Works / Creation Folder | 2026-07-29 |
| Fighting the Chemistry keeps its two responsive intro orders | Desktop/Phone remain Title First while Tablet remains Lead First; typography and semantics were normalized without changing the photo sequence or scroll timing | Fighting the Chemistry | 2026-07-29 |
| Tablet intro uses canonical values as a local exception | The inherited Tablet RichText continued rendering the removed `auto-fit` override while reporting a preset binding; direct Boldonse 80 and Inter Display 26 values match the canonical style and prevent runtime clipping | Fighting the Chemistry / Tablet | 2026-07-29 |
| Visual review uses a fixed evidence budget and stop condition | Repeated original-image decoding, CDN download and screenshot retries have repeatedly become a single point of failure; one authoritative evidence chain is enough and visual failure cannot block independent structural work | Website workflow | 2026-07-30 |
| Review depth follows change risk | Naming, copy and property changes use structural readback; layout uses one targeted screenshot; hover/cursor/scroll uses one key interaction; full-page review is reserved for page-level work | Website workflow | 2026-07-30 |
| Semantic tags do not dictate visual size | Correct content hierarchy must be preserved, but a mechanically applied H1/H2/P preset may be replaced by a suitable existing visual style or responsive values when it overlaps, clips or damages the composition | Website | 2026-07-30 |
| `ArchiveOptionRow` uses breakpoint-matched pointer hover states | Desktop and Phone remain structural variants. `Desktop Hover` and the explicitly requested `Phone Hover` both consume the same per-instance Hover Fill; Phone hover serves narrow-screen pointer environments, while touch-only devices still have no hover event | Works | 2026-07-30 |
| Phone Footer separates full-width surface from bounded content | The footer background may fill the Phone breakpoint up to 809 px, but the paired wordmark/navigation layout is capped at 480 px and centered so auto-fit text cannot grow beyond the fixed visual composition | Shared Footer / Phone | 2026-07-30 |
| CTA buttons use padding-driven Fit Content structure | The visible Button Stack owns Border and Padding around Fit Content text; page-level CTA Stacks own Fill width, alignment and Fit height so changed labels resize the boundary without clipping | Home / Observation / Shared CTA | 2026-07-31 |

