# Ken Studio Works Archive Implementation Plan

## Document purpose

This document is the durable design and implementation source for rebuilding the Works experience in Ken Studio.

It records:

- what was learned from [Mosby’s Files](https://www.mosbyfiles.com/)
- which ideas should be translated into Ken Studio
- which visual devices should not be copied
- how the Works index and project pages should be structured
- how the design should be implemented in Framer
- what content, CMS fields, components, motion states, responsive rules, and QA checks are required

Reference site reviewed on: 2026-07-14.

This is an implementation plan, not approved final copy. New visible copy must follow [BRAND_VOICE.md](BRAND_VOICE.md) and must be reviewed before publishing.

---

## 0. Current approved direction and implementation handoff

This section records the latest approved direction from Ken on 2026-07-14. If an older section in this document conflicts with Section 0, Section 0 is the source of truth and the older instruction must not be implemented.

### 0.1 Canonical content hierarchy

```text
Works
├── Observation
│   ├── Fighting the Chemistry
│   ├── Campus
│   ├── Golden Moment
│   └── Shadow
└── Creation
    └── One record for each website project
```

Definitions:

- Works is the top-level archive and route.
- Observation and Creation are categories inside Works. They are not individual projects.
- Fighting the Chemistry, Campus, Golden Moment, and Shadow are individual Observation records.
- Every website is an individual Creation record.
- Every individual record opens a dedicated detail page.
- `/fighting-the-chemistry` is the existing example of an individual detail page.
- A category folder must never link directly to one arbitrary child record as if the category and record were the same thing.

Known route status:

| Level | Content | Route status |
| --- | --- | --- |
| Works | Works archive | `/works` exists |
| Category | Observation | May keep `/observations` as a category landing page, but it is not a detail record |
| Observation record | Fighting the Chemistry | `/fighting-the-chemistry` exists |
| Observation record | Golden Moment | `/golden-moment` exists |
| Observation record | Campus | Route to confirm before publishing |
| Observation record | Shadow | Route to confirm before publishing |
| Category | Creation | `/creations` currently exists as a draft category page |
| Creation record | Each website | Route and content must be confirmed per real project |

Do not rename or delete an existing route silently. Confirm the missing Campus, Shadow, and Creation project routes, then create redirects if any published slug changes.

### 0.2 Approved Works page behavior

The Works page contains two archive folders:

1. Observation folder
2. Creation folder

The folders are vertically separated when first encountered. They become a sticky stack during scroll.

Each folder cover shows only:

- category title
- category tab
- one row per child work
- optional factual metadata such as year or medium when confirmed

The closed or resting folder cover must not permanently show:

- large project images
- project galleries
- long project descriptions
- a featured project that visually replaces the category index

The project content appears only as an interaction preview.

### 0.3 Desktop hover-preview model

Recommended desktop composition inside each folder:

```text
Archive Folder
├── Folder Tab
├── Folder Header
└── Folder Surface
    ├── Project Index
    │   ├── Project Row / Default
    │   ├── Project Row / Hover
    │   └── Project Row / Focus
    └── Preview Stage
        ├── Preview Empty
        ├── Preview Project A
        ├── Preview Project B
        └── Preview Project N
```

Default state:

- All project names are readable.
- No project preview is selected.
- Preview Stage is visually quiet and may be empty.
- No preview image should remain visible after the pointer leaves a project row.
- The folder still reads as an index without interaction.

Hover or keyboard focus state:

- The active row gains contrast through text color, weight, or one restrained divider change.
- Preview Stage reveals one cover image or primary work image.
- Preview Stage also reveals one short approved description, ideally 12-25 words.
- When the pointer leaves the active row, the preview image disappears and the folder returns to its Default state.
- The outer folder does not scale.
- Adjacent rows do not move.
- The preview uses opacity and a small y shift or clip reveal.
- Clicking the row opens that record's detail page.

The preview is supporting evidence. It must not become a permanent card grid or a second full project page inside the folder.

### 0.4 Mobile and touch behavior

Hover does not exist on touch devices. The mobile behavior must be explicit:

1. Project rows become a single-column disclosure list.
2. First tap opens that row's preview directly below the title.
3. The expanded preview contains the image, short description, and an explicit `Open project` link.
4. A second tap on another row closes the previous preview and opens the new one.
5. Keyboard focus and Enter must produce the same state on devices with keyboards.
6. Reduced motion uses an instant state change or a short opacity fade.

Do not make the first tap navigate immediately on mobile because that would make the preview impossible to access.

### 0.5 Sticky archive-stack geometry

The approved scroll behavior is a two-layer sticky stack inside `/works`. It is not automatic route navigation.

Desktop reference geometry:

```text
Nav height: use the real Main Template value
Observation sticky top: nav height + 16-24 px
Folder tab height: 44-52 px
Creation sticky top: Observation sticky top + folder tab height
Folder body height: approximately 68-82 dVh, based on real row count
Scroll spacer after Observation: enough for Creation to travel over it
```

Layer behavior:

- Observation reaches its sticky top and remains pinned.
- Creation continues scrolling upward.
- Creation settles above Observation's body but below Observation's exposed tab.
- Both category tabs remain visible at the final stacked state.
- Folder bodies overlap, but tabs never overlap.
- Creation receives the higher z-index because it arrives later.
- The stack ends naturally and releases before the footer.

Suggested z-index scale:

```text
Navigation: existing template layer
Observation folder: 2
Creation folder: 3
Preview content inside active folder: 1 relative to folder
```

Do not animate `top`, `height`, or layout dimensions during scroll. Use native sticky positioning for geometry and animate only preview opacity or transform.

### 0.6 Folder color rule

The two folders must use different neutral surfaces so the overlap remains legible, but both colors must remain inside the existing dark Ken Studio theme.

Recommended starting relationship, not locked final values:

```text
Observation body: darker charcoal
Observation tab: one step lighter
Creation body: lighter charcoal
Creation tab: one step lighter than its body
Page background: current Ken Studio near-black
```

Requirements:

- The difference must be visible without becoming a bright category palette.
- Text and interactive states must meet WCAG AA contrast.
- Do not introduce a light paper folder between dark sections.
- Do not use fake paper texture, tape, stamps, or decorative inventory marks.

### 0.7 Feasibility and implementation choice

Overall difficulty: medium-high.

Native Framer version is recommended for the current known content:

- Four known Observation records are a manageable fixed set.
- Each folder can be a component with one Default variant and one Active variant per project.
- Each row can trigger the parent folder variant on mouse enter, focus, and tap.
- Sticky folders can be built with native Framer sticky positioning, explicit top offsets, z-index, and scroll spacing.

The difficult boundary is CMS-driven dynamic preview state. Framer CMS can generate rows, but a dynamic CMS row does not automatically create a new parent component variant or shared preview state.

Use a Code Component only if all of these become requirements:

- new CMS items must appear without manually adding variants
- one shared Preview Stage must update from arbitrary CMS rows
- active preview state must be generated from collection data
- native component maintenance becomes error-prone

If custom code is proposed, explain the native limitation and obtain Ken's approval before implementation.

### 0.8 Implemented Creation archive row and sticky stack update

Updated in Framer on 2026-07-14.

Current implementation state:

- The Creation folder now uses a works-index structure instead of the previous large website contact-sheet preview.
- A native Framer component named `Archive Option Row` has been created for reusable archive rows.
- The component exposes editable fields for number, title, meta, and status.
- The first Creation record is `The Treat`.
- The route for `The Treat` is still marked `ROUTE TO CONFIRM`; do not link it to a category page as a substitute detail route.
- The old visible appear motion on the Observation and Creation folders has been neutralized by removing the opacity and y-offset change.
- Observation and Creation now use native sticky positioning to create the archive-stack effect.
- Observation uses the lower layer; Creation uses the higher layer so it can slide over the Observation body.
- Sticky offsets are separated by approximately one tab height so both folder tabs stay visible.
- The two folder surfaces now use different dark neutral colors so the overlap is readable.
- Additional scroll space has been added after the archive stack so the sticky overlap has room to resolve naturally.

Implementation notes:

- Keep this stack native in Framer: sticky position, z-index, tab offset, and neutral folder colors.
- Do not animate folder top, height, or layout dimensions during scroll.
- Use motion for previews only, not for the archive-stack geometry.
- Future Creation websites should be added by duplicating the `Archive Option Row` instance and editing its fields.
- Add confirmed detail routes before turning Creation rows into links.

Follow-up refinement on 2026-07-14:

- Observation rows and Creation rows now share the same native Framer component: `Archive Option Row`.
- The row component uses variants for the individual works:
  - `Fighting the Chemistry`
  - `Campus`
  - `Golden Moment`
  - `Shadow`
  - `The Treat`
- Each variant stores its own visible content, status, link state, and where relevant its custom cursor preview.
- Observation’s previous hand-built rows were replaced by component instances.
- `Fighting the Chemistry` links to `/fighting-the-chemistry`.
- `Golden Moment` links to `/golden-moment`.
- `Campus`, `Shadow`, and `The Treat` remain unlinked until their detail routes are confirmed.
- Observation and Creation sheets are now equal height with intentional empty room for future records.
- Folder tabs are horizontally offset, not vertically offset.
- Phone tabs are narrower to preserve the stacked-folder reading on small screens.
- Status text such as `OPEN` and `ROUTE TO CONFIRM` is right-aligned in a fixed status zone so it does not drift or visually collide with titles.

Responsive and hover fix on 2026-07-14:

- Phone uses dedicated `Archive Option Row` phone variants so titles do not get squeezed into one-letter or one-word columns.
- Phone row layout is vertical:
  - number + title on the first line
  - status on the second line
  - metadata hidden unless it becomes necessary for a specific record
- Desktop and tablet keep the horizontal row variants.
- Custom cursor preview must be applied to the row component instances on the page, not only inside the component variant.
- After converting hand-built rows into component instances, re-check each desktop/tablet instance for its `customCursor` effect.

### 0.8 Exact native Framer component plan

Create or refactor these components:

```text
ArchiveFolder / Observation
├── Default
├── FTC Active
├── Campus Active
├── Golden Moment Active
└── Shadow Active

ArchiveFolder / Creation
├── Default
└── One Active variant per confirmed website

ArchiveProjectRow
├── Default
├── Hover
├── Focus
└── Expanded Mobile
```

Recommended folder properties:

```text
Category Title
Folder Color
Tab Color
Project Title 1...N
Project Link 1...N
Preview Image 1...N
Preview Description 1...N
```

Do not create project facts in Framer. Titles, descriptions, routes, and image sources come from `content-library`.

### 0.9 Replacement layer tree for `/works`

```text
Works Page
├── Page Content
│   ├── Works Introduction
│   │   ├── Works Title
│   │   └── Works Statement
│   └── Sticky Archive Region
│       ├── Observation Scroll Space
│       │   └── Observation Folder
│       │       ├── Observation Tab
│       │       ├── Observation Header
│       │       └── Observation Folder Surface
│       │           ├── Observation Project Index
│       │           └── Observation Preview Stage
│       └── Creation Scroll Space
│           └── Creation Folder
│               ├── Creation Tab
│               ├── Creation Header
│               └── Creation Folder Surface
│                   ├── Creation Project Index
│                   └── Creation Preview Stage
└── Footer from Main Template
```

Semantic layer names are required. Do not leave new layers named Frame, Stack, Text, or Container.

### 0.10 Current live implementation and required migration

Current Framer project:

- Project: Ken Studio
- Project ID: `W2l0ZO8Ar0mErx3GOD0d`
- Works page route: `/works`
- Works page node: `fh4Zs4Ebl`
- Main Template: `Y5fLSaBQH`
- Existing responsive breakpoints: Desktop, Tablet, Phone
- Shared navigation Works link already points to `/works`
- The site has not been published as part of this implementation task

Current mismatch:

- The page already contains two visually separate archive folders.
- The folders currently show large project images and descriptions by default.
- This default content presentation is no longer approved.
- The current folder shells, typography, responsive setup, colors, navigation, and footer can be reused.
- Replace the internal folder content and scroll behavior. Do not rebuild the whole page or Home.

### 0.11 Implementation runbook for the next agent

The next agent should execute in this order:

1. Read `AGENTS.md`, `skills/taste-skill/SKILL.md`, `GOAL.md`, `BRAND_VOICE.md`, and this document.
2. Reconnect to the existing Ken Studio Framer project and inspect `/works`; do not create another Works page.
3. Capture Desktop, Tablet, and Phone screenshots before editing.
4. Preserve the page shell, Main Template, global navigation, footer, title typography, and route.
5. Convert the Observation folder body into the four-row project index.
6. Build the Observation preview variants using only confirmed content and images from the four existing image folders.
7. Link FTC to `/fighting-the-chemistry` and Golden Moment to `/golden-moment`.
8. Leave Campus and Shadow links unconnected or clearly marked in the editor until their routes are confirmed. Do not invent routes and publish them.
9. Test mouse hover, keyboard focus, and row click before touching Creation.
10. Convert Creation into the same folder system, but populate only confirmed website projects from `content-library`.
11. Implement sticky stacking with Observation first and Creation second. Keep both tabs visible in the final stack.
12. Tune folder colors inside the dark theme so the layers remain distinguishable.
13. Recompose Tablet geometry with smaller top offsets and preview width.
14. Build the Phone disclosure behavior. Do not depend on hover.
15. Add reduced-motion behavior.
16. Review Framer diagnostics and capture all three breakpoint screenshots.
17. Do not publish without Ken's explicit approval.

### 0.12 Acceptance checks for this revision

- Works clearly contains Observation and Creation.
- Observation clearly contains FTC, Campus, Golden Moment, and Shadow.
- Creation clearly contains individual website projects.
- Every listed item is treated as a future or existing detail-page record.
- No large project image is permanently visible on a resting folder cover.
- Hover or focus reveals only the active record preview.
- Clicking a confirmed row opens the correct detail page.
- Creation overlaps Observation during scroll.
- Both tabs remain visible and never collide.
- Folder colors remain distinct at the stacked state.
- Phone interaction works without hover.
- Reduced-motion mode preserves all content and links.
- Home layout remains unchanged.

---

## 1. Design read

Reading this as: a personal photography and web design portfolio for visually literate visitors, with a quiet, image-led, editorial language, using an archive as the information system rather than as surface decoration.

Recommended design dials:

- `DESIGN_VARIANCE: 7`
- `MOTION_INTENSITY: 5`
- `VISUAL_DENSITY: 4`

Reasoning:

- The layout should feel authored and asymmetric, but not chaotic.
- Motion should support reading, grouping, and state changes. It should not become the subject of the site.
- The photography needs space, while the archive metadata needs enough density to feel useful.

Project mode: targeted evolution.

The Home page and its current visual identity should be preserved. The new work is concentrated in a new Works page and its detail pages.

---

## 2. Non-negotiable project decisions

1. Keep the current Home composition and brand language.
2. The existing Home Works section remains a concise entry point, not the full archive.
3. Create a separate `/works` page.
4. Divide Works into two categories that contain individual records:
   - Observation: photography and visual studies
   - Creation: designed and built websites
5. Observation currently contains Fighting the Chemistry, Campus, Golden Moment, and Shadow.
6. Every photography series and every website opens its own detail page.
7. Do not copy Mosby’s Files literally.
8. Do not introduce paper textures, tape, paperclips, retro file props, or dense scrapbook collage unless Ken explicitly approves them later.
9. Build the archive feeling through taxonomy, sequence, metadata, typography, navigation, hover preview, and sticky layering.
10. Folder covers list project names. They do not permanently display project content.
11. Use Framer native Components, Variants, Layout, Stack, CMS, Breakpoints, and Animations first.
12. Use custom code only when a behavior cannot be maintained reliably with native Framer features.
13. Build and approve one page or component at a time.

---

## 3. What the reference site actually does

### 3.1 Homepage narrative

The reference homepage follows this sequence:

1. It opens with a research thesis: American Modernism.
2. It gives the visitor a concise point of view before showing any person or project.
3. It organizes architects into four schools of thought.
4. Each school is represented as a layer in one stacked archive object.
5. Individual architects appear as tabs inside those categories.
6. The navigation object is also the main visual object.

The important lesson is not the folder shape. The important lesson is that classification, navigation, and visual identity are the same system.

### 3.2 Case page narrative

The Frank Lloyd Wright case page follows this sequence:

1. Large person title
2. Biographical profile and dates
3. Short editorial interpretation
4. Representative works
5. Images, drawings, notes, and media arranged as evidence
6. A persistent next-case control
7. A page-end transition into the next architect

The page reads like a dossier instead of a normal portfolio case study.

### 3.3 Observed typography roles

The reference uses three clear typographic jobs:

- Condensed bold sans for major titles
- Editorial serif for interpretation and longer reading
- Monospaced or typewriter-like text for metadata, labels, and notes

The useful principle is role separation. The exact typefaces should not be copied.

### 3.4 Observed motion behavior

- Initial content reveal begins after a short dark hold.
- Case titles are split into individual characters for staged entry.
- Archive layers transition using position and height changes.
- The main transition duration observed on the archive stack is approximately 0.65 seconds.
- The main header is fixed.
- A smaller case header becomes visible after scrolling into the content.
- The next-case control changes state based on scroll position.
- At the bottom, the next case becomes part of the page rather than appearing as an unrelated footer card.

### 3.5 Mobile behavior

- The main title is recomposed into two lines.
- Archive layers remain visible instead of turning into generic cards.
- Layer heights and offsets are recalculated for the narrower viewport.
- The core metaphor survives, but the geometry becomes simpler.

### 3.6 What not to import

- Do not import the bright four-color category palette.
- Do not copy the physical office-file styling.
- Do not copy the exact title scale or condensed display face.
- Do not copy the scrapbook composition for every project.
- Do not copy the reference site's continued-scroll route navigation. The approved interaction is a sticky stack inside `/works`, with explicit clicks for opening detail pages.

These devices belong to the reference site’s subject and identity. Ken Studio needs a quieter translation.

---

## 4. Ken Studio narrative model

### 4.1 Central idea

Works should present Observation and Creation as two parts of one practice.

Internal narrative statement:

> Observation records how I look. Creation records what I make from that attention.

This is a direction, not approved final page copy.

### 4.2 Visitor journey

The intended path is:

1. Home establishes the mood of Ken Studio.
2. Home Works introduces Observation and Creation.
3. `/works` explains the relationship between them.
4. Visitors enter a photography series or a website project.
5. Each detail page presents material as an authored record.
6. The next record continues within the same category.
7. Selected cross-links can connect an Observation to a Creation when there is a real relationship.

### 4.3 Narrative difference between the two archives

Observation asks:

- What caught my attention?
- What changed between frames?
- What did the light, color, weather, distance, or film do?
- What remained unresolved?

Creation asks:

- What was the situation?
- What did the original material reveal?
- What design decision mattered?
- What changed through iteration?
- What was finally built?

The two categories use the same archive system but not the same case-study template.

---

## 5. Information architecture

### 5.1 Routes

Recommended route structure:

```text
/
/works
/observations                 optional category landing page
/fighting-the-chemistry       existing Observation detail
/golden-moment                existing Observation detail
/campus                       proposed, confirm before creating
/shadow                       proposed, confirm before creating
/creations                    existing draft category landing page
/creation/[slug]              proposed pattern for website details
```

Do not change existing published slugs silently. If current project pages already use different URLs, preserve them or create redirects before publishing.

### 5.2 Home Works section

Job: provide orientation and entry.

Required content:

- Works heading
- One short sentence explaining the two modes
- Observation entry with one real image
- Creation entry with one real project image
- One consistent Works CTA intent

Do not include:

- a full project grid
- long archive metadata
- two equal generic cards with identical structure
- multiple buttons that all mean “view work”

Recommended interaction:

- The entire Observation and Creation entries are links.
- Hover changes image treatment, text contrast, or divider color.
- Do not scale the outer card or move adjacent layout.

### 5.3 Works index page

The Works page has three narrative zones.

#### Zone A: Works introduction

Purpose: explain that Observation and Creation are connected practices.

Layout:

- Left-aligned title
- Short body directly below it
- No permanent project image in the introduction
- No scroll cue
- No section number label

#### Zone B: Observation folder

Purpose: make the photography category understandable as an index before the visitor opens a record.

Resting content:

- Observation title and tab
- Fighting the Chemistry row
- Campus row
- Golden Moment row
- Shadow row
- Confirmed metadata only

Interaction:

- Hover or focus on one row reveals that record in the shared Preview Stage.
- Click opens the dedicated detail page.
- Default state does not show a large cover image or description.

#### Zone C: Creation folder

Purpose: list each website as an individual Creation record.

Resting content:

- Creation title and tab
- One row per confirmed website project
- Confirmed project type, year, or role only when available

Interaction:

- Uses the same index and Preview Stage logic as Observation.
- Uses real website screenshots only.
- Does not invent clients, performance data, awards, or business results.
- Scrolls over the Observation body while leaving both category tabs visible.

Observation and Creation must not become two equal generic cards. They are two layers in one scrolling archive system.

### 5.4 Detail page sequence

Observation detail sequence:

1. Series title
2. Short opening note
3. Series metadata
4. First image with breathing room
5. Image sequence arranged by visual rhythm
6. Small text interruptions only when they add something the images cannot say
7. Closing note or unresolved observation
8. Next Observation record

Creation detail sequence:

1. Project title
2. Context and role
3. One-sentence project premise
4. Source material or original condition
5. Key design decision
6. Real page images and responsive views
7. System details only where they explain the outcome
8. Reflection on what changed or remained difficult
9. Next Creation record

---

## 6. CMS model

Use two CMS collections because the content structures are meaningfully different.

### 6.1 Observation Series collection

Required fields:

| Field | Type | Purpose |
| --- | --- | --- |
| Title | Plain text | Series title |
| Slug | Slug | Route |
| Year | Plain text or number | Real year |
| Date Range | Plain text | Optional real range |
| Place | Plain text | Optional location |
| Medium | Plain text | Film, digital, instant film, or other real medium |
| Opening Note | Formatted text | Short brand-voice introduction |
| Cover Image | Image | Works index image |
| Cover Alt | Plain text | Accessible description |
| Gallery | Gallery or repeated image fields | Main sequence |
| Image Notes | Formatted text | Optional notes tied to selected images |
| Closing Note | Formatted text | Optional ending |
| Featured | Boolean | Home or Works feature state |
| Sort Order | Number | Manual archive order |
| Next Record URL | Link | Explicit next item if CMS relation is unavailable |

### 6.2 Creation Projects collection

Required fields:

| Field | Type | Purpose |
| --- | --- | --- |
| Title | Plain text | Project name |
| Slug | Slug | Route |
| Year | Plain text or number | Real year |
| Project Type | Plain text | Portfolio, restaurant, editorial, or other real type |
| Role | Plain text | Real contribution only |
| Status | Plain text | Live, concept, redesign, or archived |
| Project URL | Link | Optional live site |
| Premise | Plain text | One concrete sentence |
| Context | Formatted text | Starting condition |
| Key Decision | Formatted text | Main design judgment |
| Reflection | Formatted text | What changed or remained difficult |
| Cover Image | Image | Works index image |
| Cover Alt | Plain text | Accessible description |
| Gallery | Gallery or repeated image fields | Real desktop, tablet, and mobile images |
| Featured | Boolean | Home or Works feature state |
| Sort Order | Number | Manual archive order |
| Next Record URL | Link | Explicit next item if CMS relation is unavailable |

### 6.3 Content rules

- `content-library` remains the source of truth.
- Do not publish generated facts.
- Empty optional fields should collapse cleanly.
- No placeholder copy should remain in published CMS items.
- Alt text describes content, not visual style alone.
- Observation entries should be series-based.
- Creation entries must use real screenshots or real project media.

---

## 7. Typography system

### 7.1 Principle

Typography should create archive hierarchy without turning the site into a retro document.

Use a maximum of three roles:

1. Display role
2. Reading role
3. Metadata role

### 7.2 Display role

Use the existing Ken Studio Home display typeface if it remains legible at large and small sizes.

Use for:

- Works
- Observation
- Creation
- Series and project titles
- Next record title

Rules:

- Desktop Works title: target 72-112 px depending on the existing Home scale
- Mobile Works title: target 44-64 px
- Maximum two lines in the first viewport
- Tight tracking is acceptable, but letter collisions are not
- Do not add a different serif word for emphasis
- If italics are used, use the same family and protect descenders

### 7.3 Reading role

A restrained editorial serif is justified for longer observation notes because the site is explicitly image-led, reflective, and notebook-like.

Before selecting a new family:

1. Audit the current project text styles.
2. Reuse the current body family if it already supports the voice.
3. Add a serif only if it produces a clear reading benefit and does not disconnect Works from Home.

Use for:

- Opening notes
- Photography observations
- Project reflections

Rules:

- Desktop body: 18-22 px
- Mobile body: 17-19 px
- Line height: 1.45-1.65
- Maximum text width: 55-65 characters
- Avoid centered long paragraphs
- Avoid long marketing explanations

### 7.4 Metadata role

Use the existing neutral sans or one restrained mono family.

Use for:

- Year
- Medium
- Place
- Role
- Status
- Archive controls

Rules:

- Desktop: 12-14 px
- Mobile: 12-13 px
- Do not use all caps everywhere
- Do not add fake version numbers or decorative status dots
- Use no more than one middle dot per line
- Prefer columns, line breaks, or spacing to repeated separators

### 7.5 Text hierarchy tokens

Create or reuse Framer Text Styles with semantic names:

```text
Display / Page Title
Display / Record Title
Heading / Section
Body / Lead
Body / Reading
Meta / Primary
Meta / Secondary
Caption / Image
Link / Editorial
```

Do not leave one-off text sizes without a named style unless the composition genuinely requires an exception.

---

## 8. Visual system

### 8.1 Archive feeling without props

Use:

- sequence
- category
- metadata
- index behavior
- controlled dividers
- repeated title positions
- persistent navigation state
- next-record continuity

Do not rely on:

- paper textures
- tape
- fake handwriting
- paperclips
- stamps
- fake inventory numbers
- decorative document UI

### 8.2 Color

- Preserve the current Ken Studio page theme and accent color.
- Observation and Creation require different neutral folder colors so their overlap remains readable.
- Keep both folder colors inside the existing dark charcoal family.
- Prefer one accent used consistently across Works.
- Active project rows can use text contrast, weight, or a restrained divider change.
- Do not invert the page theme repeatedly between sections.

### 8.3 Images

Observation:

- Preserve each photograph’s meaning when cropping.
- Mix portrait, landscape, and full-width moments based on the actual series.
- Do not overlay decorative pills on images.
- Use captions only when they communicate real context.

Creation:

- Use real project screenshots.
- Show desktop, tablet, and mobile only when those views exist.
- Do not build fake website screenshots from empty Framer frames.
- Keep browser chrome only if it helps explain the artifact.

### 8.4 Shape system

Adopt one radius rule for Works based on the current Home system.

Preferred default if Home is mostly sharp:

- Images and records: 0-4 px
- Interactive tabs: same system, not unrelated pills
- Buttons: use existing Ken Studio component variants

Do not mix soft cards, pill buttons, and sharp archive rows without an explicit rule.

---

## 9. Motion specification

### 9.1 Motion jobs

Every animation must do one of four jobs:

- establish hierarchy
- reveal a narrative sequence
- confirm interaction
- communicate a state change

If it does none of these, remove it.

### 9.2 Global motion language

- Smooth
- Restrained
- Spatial
- No bounce-heavy motion
- No constant movement
- No custom cursor
- No scroll cue

Default Framer spring:

```text
Type: Spring
Stiffness: 250
Damping: 28-34
Mass: 1
```

Use approximately 0.55-0.70 seconds only where a duration-based transition is more appropriate than a spring. The reference archive uses about 0.65 seconds, but Ken Studio should not copy that timing mechanically.

### 9.3 Page entrance

Sequence:

1. Navigation or page shell is already stable.
2. Page title enters.
3. Opening statement enters 60-100 ms later.
4. First image reveals 80-140 ms after the statement.

Motion:

- Text: opacity 0 to 1, y 12-20 px to 0
- Image: mask or clip reveal with minimal scale
- Run once per page visit

Do not hold the page on black. That behavior belongs to the reference site and would interrupt Ken Studio’s quieter flow.

### 9.4 Folder preview state

State change:

- Active project row gains contrast through text color, weight, or one divider.
- Shared Preview Stage changes image and short description.
- Preview Stage size remains stable between records.
- Adjacent rows do not move on hover or focus.
- Returning the pointer to the empty folder area returns to the Default state, with no preview image left visible.

Native Framer implementation:

- One ArchiveFolder component per category.
- One Default variant and one Active variant per confirmed record.
- Row hover and focus trigger the matching folder variant.
- Variant transitions use opacity and a small y shift, not outer scale.

### 9.5 Project-row hover and focus

```text
Project Row
├── Project Title
├── Optional Confirmed Metadata
└── Interaction Target

Preview Stage
├── Stable Image Frame
└── Short Description
```

- Row height remains stable.
- Image frame keeps size, overflow, border, and radius stable.
- Preview image may scale between 1.0 and 1.02 inside the stable frame.
- Text can change opacity, color, or weight.
- Divider can change opacity.
- Do not scale the full row or folder.
- Focus state must provide the same information as hover.

### 9.6 Scroll reveal

- Reveal only key records and section transitions.
- Do not animate every caption and metadata item separately.
- Observation image sequences should feel calm.
- Creation screenshots can use a slightly clearer mask reveal.
- Use viewport animation once, with threshold around 20-30 percent.

### 9.7 Sticky folder stack

Version 1:

- Observation uses sticky positioning at the first approved top offset.
- Creation uses sticky positioning one tab height lower.
- Creation has the higher folder z-index.
- Creation covers the Observation body, not its tab.
- Both tabs remain visible until the sticky region releases.
- The footer remains outside the sticky region.

Do not use a page-level scroll listener. Native sticky positioning is the first implementation choice.

### 9.8 Next record

Version 1:

- Use an explicit accessible link.
- The next title and image enter near the end of the current record.
- The visitor clicks to continue.

Optional version 2:

- Build a shared transition or continued-scroll navigation as a Code Component.
- Must provide reduced-motion and keyboard fallbacks.
- Must never trap the user or trigger accidental navigation.

### 9.9 Reduced motion

When reduced motion is requested:

- Remove parallax
- Remove image scale
- Replace mask reveals with simple opacity or static content
- Make archive state changes immediate or near-immediate
- Keep all content and links available

---

## 10. Framer implementation architecture

### 10.1 Native-first component list

Create or audit these components:

```text
NavigationBar
WorksEntry
ArchiveFolderObservation
ArchiveFolderCreation
ArchiveProjectRow
ArchivePreviewStage
RecordMetadata
NextRecord
FooterSection
```

Component variants:

```text
WorksEntry / Observation
WorksEntry / Creation

ArchiveFolderObservation / Default
ArchiveFolderObservation / FTC Active
ArchiveFolderObservation / Campus Active
ArchiveFolderObservation / Golden Moment Active
ArchiveFolderObservation / Shadow Active

ArchiveFolderCreation / Default
ArchiveFolderCreation / One Active variant per confirmed website

ArchiveProjectRow / Default
ArchiveProjectRow / Hover
ArchiveProjectRow / Focus
ArchiveProjectRow / Expanded Mobile

NextRecord / Observation
NextRecord / Creation
```

Use separate ObservationRecord and CreationRecord components if forcing them into one component creates too many conditional layers.

### 10.2 Page layer tree

Recommended Works page tree:

```text
Works Page
├── Page Content
│   ├── Works Introduction
│   │   ├── Works Title
│   │   └── Works Statement
│   └── Sticky Archive Region
│       ├── Observation Scroll Space
│       │   └── Observation Folder
│       │       ├── Observation Tab
│       │       ├── Observation Project Index
│       │       └── Observation Preview Stage
│       └── Creation Scroll Space
│           └── Creation Folder
│               ├── Creation Tab
│               ├── Creation Project Index
│               └── Creation Preview Stage
└── Footer from Main Template
```

Recommended Observation detail tree:

```text
Observation Detail Page
├── Navigation Bar
├── Observation Header Section
│   └── Observation Header Container
│       ├── Observation Title
│       ├── Observation Opening Note
│       └── Observation Metadata
├── Observation Gallery Section
│   └── Observation Image Sequence
├── Observation Closing Section
└── Next Observation Record
```

Recommended Creation detail tree:

```text
Creation Detail Page
├── Navigation Bar
├── Creation Header Section
│   └── Creation Header Container
│       ├── Creation Title
│       ├── Creation Premise
│       └── Creation Metadata
├── Creation Context Section
├── Creation Decision Section
├── Creation Gallery Section
├── Creation Reflection Section
└── Next Creation Record
```

Do not leave layers named Stack, Frame, Text, Rectangle, or Container.

### 10.3 When custom code is justified

Custom code is not required for version 1 while the project lists remain fixed and manually authored.

Consider a Code Component only for:

- CMS-driven project rows that must update one shared Preview Stage automatically
- arbitrary record counts that should not require new component variants
- active preview state generated from collection data
- complex sticky geometry that proves unreliable after native Framer testing

Before adding code:

1. Explain the exact limitation of native Framer.
2. Confirm the behavior is important enough to maintain.
3. Isolate the code to one component.
4. Provide a static and reduced-motion fallback.

---

## 11. Responsive specification

### 11.1 Desktop

- Use asymmetric composition and generous image scale.
- Keep reading text within 55-65 characters.
- Allow selected images to cross grid columns.
- Keep metadata aligned but not boxed into generic cards.
- Navigation remains one line and no taller than 80 px.

### 11.2 Tablet

- Reduce archive asymmetry.
- Avoid narrow three-column metadata structures.
- Move metadata below titles when necessary.
- Reduce overlapping images before reducing image legibility.
- Test both portrait and landscape tablet widths.

### 11.3 Mobile

- Collapse complex layouts to one clear column.
- Preserve the narrative order.
- Use 16-20 px horizontal padding based on the current Home system.
- Keep body text at least 17 px where possible.
- Make archive controls at least 44 px tall.
- Keep the two-folder order, but reduce the sticky offsets and overlap depth.
- Replace hover preview with a one-open-at-a-time disclosure interaction.
- First tap expands preview; a separate link opens the detail page.
- If sticky layering causes clipping or traps scroll, keep the visible tabs but release the folders into normal document flow.
- Re-crop images intentionally per series.
- Keep Observation and Creation recognizable as the same system.

### 11.4 Breakpoint verification

Minimum checks:

- 1440 px desktop
- 1280 px desktop
- 1024 px tablet landscape
- 768 px tablet portrait
- 390 px mobile
- 375 px mobile

Check:

- title line breaks
- image focal points
- archive control wrapping
- metadata overflow
- next-record visibility
- sticky element collisions
- horizontal overflow

---

## 12. Content requirements before build

### 12.1 Observation

For each photography series, prepare:

- final title
- year or real date range
- place if relevant
- medium if relevant
- 1 cover image
- 4-12 ordered images
- opening note
- optional notes tied to selected frames
- closing note if there is a genuine ending
- alt text for each published image

Existing content:

- `Golden Moment` contains a usable title, subtitle, two sections, and two image references.
- `Fighting the Chemistry` has four image assets, but its markdown content is currently empty and requires approved copy.
- `Campus` has four image assets but no content markdown or confirmed route.
- `Shadow` has eight image assets but no content markdown or confirmed route.
- The Observation folder can list all four approved titles, but only confirmed routes should be clickable before publishing.

### 12.2 Creation

For each website project, prepare:

- project title
- year
- project type
- role
- live or concept status
- project URL if applicable
- one-sentence premise
- context
- key design decision
- reflection
- real desktop images
- real mobile images
- alt text

Do not begin bulk CMS population until at least one complete Observation and one complete Creation record are approved.

---

## 13. Build phases

### Phase 0: Audit and preservation record

Goal: understand the current Ken Studio project before editing.

Actions:

1. Read the live Framer project.
2. Record current page tree, published routes, text styles, color styles, components, breakpoints, and Works structure.
3. Identify what must be preserved.
4. Check whether current Home links already point to project pages.
5. Record current SEO titles and descriptions.

Deliverable:

- short audit added to this document or a linked handoff file

No design changes in this phase.

### Phase 1: Content model

Goal: make the archive maintainable.

Actions:

1. Confirm final routes.
2. Create or map Observation Series CMS.
3. Create or map Creation Projects CMS.
4. Populate one complete item in each collection.
5. Validate optional field behavior.

Approval gate:

- Ken approves the CMS structure and two sample records.

### Phase 2: Works index desktop

Goal: replace the existing folder contents with the approved project index and preview system.

Actions:

1. Preserve the existing Works introduction and page shell.
2. Build ArchiveFolderObservation with Default and four Active variants.
3. Build the four project rows and the shared Preview Stage.
4. Connect only confirmed detail routes.
5. Test hover, focus, click, and Default return behavior.
6. Review before rebuilding ArchiveFolderCreation.
7. Populate Creation only with confirmed website projects.

Approval gate:

- Ken approves the Observation folder interaction before Creation or sticky-scroll geometry is added.

### Phase 3: Detail page templates

Goal: prove that Observation and Creation can share a system without sharing the same layout.

Actions:

1. Build Observation detail template.
2. Build Creation detail template.
3. Add NextRecord.
4. Verify content order and image rhythm.
5. Test missing optional fields.

Approval gate:

- Ken approves both detail structures.

### Phase 4: Home integration

Goal: connect the existing Home to the new archive without redesigning Home.

Actions:

1. Update only the Works entry links and necessary preview states.
2. Preserve current Home composition.
3. Confirm one CTA intent.
4. Verify browser back behavior.

### Phase 5: Responsive build

Goal: adapt composition rather than shrink it.

Actions:

1. Tablet Works index.
2. Mobile Works index.
3. Mobile one-open-at-a-time project disclosure behavior.
4. Tablet Observation detail.
5. Mobile Observation detail.
6. Tablet Creation detail.
7. Mobile Creation detail.
8. Re-crop images and correct focal points per breakpoint.

### Phase 6: Motion and transition polish

Goal: add only motion that improves hierarchy and continuity.

Actions:

1. Page entrance.
2. Folder preview state transition.
3. Project-row hover and focus.
4. Sticky Observation and Creation overlap.
5. Next-record entrance on detail pages.
6. Reduced-motion fallback.

Sticky overlap is added only after both folder heights are stable at all three breakpoints.

### Phase 7: Final QA and publish preparation

Actions:

1. Verify all routes and links.
2. Check Desktop, Tablet, and Mobile.
3. Check focus states and keyboard access.
4. Check text and background contrast.
5. Check image alt text.
6. Check image sizes and loading behavior.
7. Check title hierarchy and metadata wrapping.
8. Check reduced motion.
9. Check SEO title, description, and OG image.
10. Read every visible string for brand voice and factual accuracy.

---

## 14. Acceptance criteria

The Works redesign is complete only when all of the following are true.

### Narrative

- A visitor understands why Observation and Creation belong together.
- Works does not read as two unrelated portfolios.
- Each detail page feels like a record, not a marketing case-study template.
- Photography leads Observation pages.
- Real design decisions lead Creation pages.

### Visual quality

- The page feels continuous with the existing Home.
- The archive is recognizable without literal file props.
- No generic three-equal-card section is used.
- Repeated sections do not all use the same layout family.
- Images are real, relevant, and correctly cropped.
- Typography roles are consistent.

### Motion

- Every animation has a documented purpose.
- Motion does not shift surrounding layout on hover.
- Image scaling happens inside a stable image frame.
- Reduced-motion mode remains complete and usable.
- No accidental page navigation occurs from scroll.

### Structure

- CMS fields are semantic and maintainable.
- Framer layers are semantically named.
- Repeated UI is componentized.
- Optional fields collapse without empty gaps.
- Custom code, if any, is isolated and documented.

### Responsive and accessibility

- No horizontal overflow at the listed breakpoints.
- Text remains readable.
- Controls are large enough for touch.
- Focus states are visible.
- Contrast meets WCAG AA.
- Images have meaningful alt text.

### Performance

- Large images have web-sized derivatives.
- Above-the-fold media is prioritized.
- Below-the-fold galleries are lazy-loaded where supported.
- Layout space is reserved to prevent shifting.
- Fixed grain or texture effects are not applied to scrolling containers.

---

## 15. Risks and responses

### Risk: The archive becomes a visual costume

Response: remove props and check whether taxonomy, metadata, and sequence still communicate the concept.

### Risk: Observation and Creation become two equal cards

Response: give each archive its own content rhythm and detail structure while preserving shared typography and navigation.

### Risk: CMS makes every project look identical

Response: define a small set of flexible layout patterns and allow controlled per-project composition. Do not create one universal image grid.

### Risk: The new Works page feels disconnected from Home

Response: reuse current brand tokens, navigation, footer, text styles, spacing logic, and motion character before introducing new styles.

### Risk: Motion becomes the main attraction

Response: remove any animation that cannot be explained as hierarchy, narrative, feedback, or state change.

### Risk: Photography loads slowly

Response: create web derivatives based on actual container sizes, reserve dimensions, and avoid loading full-resolution originals into the page.

### Risk: Sticky folders trap scroll or hide content

Response: use native sticky positioning, keep the footer outside the sticky region, test all listed viewport sizes, and provide normal-flow or reduced-motion fallbacks when the overlap is not reliable.

---

## 16. Immediate next action

The Works page shell, route, navigation connection, and three responsive breakpoints already exist.

The next approved implementation task should be:

1. Reopen and audit the existing `/works` page. Do not create a second Works page.
2. Preserve the introduction, template, navigation, footer, and responsive breakpoint structure.
3. Replace only the Observation folder interior with the four-row index and inline hover preview overlays. Do not add a persistent Preview Stage.
4. Test Default, Hover, Focus, Click, Phone Expanded, and reduced-motion states.
5. Review Desktop, Tablet, and Phone before modifying Creation.
6. After Observation is approved, rebuild the Creation folder with confirmed website content.
7. Implement the sticky two-folder overlap last, after both folder components have stable heights.

This keeps the next change limited to one component system and prevents scroll geometry from being tuned against temporary content.

---

## 17. Implementation handoff log

### 2026-07-14 Hover preview interaction pass

Project state:

- Framer project: `Ken Studio`, project id `W2l0ZO8Ar0mErx3GOD0d`.
- Active Framer session used for this pass: `3`.
- Page path: `/works`.
- Current edited section: Observation folder interior.

Completed in Framer:

- Confirmed that the requested interaction is feasible as a Framer relative hover preview: when a desktop visitor hovers an Observation row, a preview image appears; when the pointer leaves, the preview should not remain visible as a persistent default image.
- Removed the always-visible default Preview Stage image from Desktop, Tablet, and Phone states.
- Added desktop hover previews for the two Observation rows that already have confirmed routes and Framer image URLs:
  - `Fighting the Chemistry`
  - `Golden Moment`
- Preserved the confirmed click routes:
  - `Fighting the Chemistry` → `/fighting-the-chemistry`
  - `Golden Moment` → `/golden-moment`
- Preserved `Campus` and `Shadow` as unlinked / route-to-confirm records.

Image handling state:

- No original source image was opened in visual context.
- No original source image was uploaded directly.
- Web-sized hover preview derivatives were generated for the unconfirmed rows and stored outside `content-library`:
  - `/private/var/folders/q8/mg9d8_gd3qjglngrd_2x8gzh0000gp/T/ken-studio-hover-previews/campus-hover-preview.jpg`
  - `/private/var/folders/q8/mg9d8_gd3qjglngrd_2x8gzh0000gp/T/ken-studio-hover-previews/shadow-hover-preview.jpg`
- Each derivative is roughly 100 KB and can be uploaded to Framer as the safe web asset for future Campus / Shadow hover previews.

Not completed yet:

- Full interactive browser hover QA is still pending.
- Publishing is still pending.

### 2026-07-14 Video-reference correction pass

Reference read:

- User-provided screen recording shows the intended interaction as a Framer native custom-cursor image treatment: the pointer becomes / carries a preview image while hovering an active option row, not as a separate persistent preview panel.
- The Observation UI should read as a list of work options first; no dedicated `Preview Stage` should be visible in the default state.

Completed in Framer:

- Removed the persistent `Preview Stage` from the Observation folder.
- Rebuilt the desktop Observation interior as a single four-row Project Index.
- Added inline hover preview overlays for all four Observation options:
  - `Fighting the Chemistry`
  - `Campus`
  - `Golden Moment`
  - `Shadow`
- Added mouse-leave dismissal so the preview image disappears after leaving the active option.
- Preserved confirmed links only:
  - `Fighting the Chemistry` → `/fighting-the-chemistry`
  - `Golden Moment` → `/golden-moment`
- Kept `Campus` and `Shadow` unlinked / route-to-confirm.

Image handling state:

- The existing Framer-hosted images were reused for `Fighting the Chemistry` and `Golden Moment`.
- Campus and Shadow used the web-sized derivative files generated in the previous pass, not the original source images.
- Uploaded derivative asset URLs now used in Framer:
  - `Campus` → `https://framerusercontent.com/images/ryOkK5AD7sm6rKR7cZ4PiBv85UU.jpg`
  - `Shadow` → `https://framerusercontent.com/images/WUZ46CLVnqtEArc9nmcLxw4org.jpg`

Verification:

- Framer review reports no blocking errors after the correction pass.
- Static default screenshot confirms the Observation folder now shows only the four work options and no Preview Stage.
- Full live pointer-hover QA in browser is still pending.
- Publishing is still pending.

### 2026-07-14 Custom cursor correction

Implementation correction:

- Replaced the hover overlay approach with Framer native Custom Cursor.
- Removed the four temporary hover overlay nodes from the Observation rows.
- Created four reusable native Framer cursor preview components:
  - `Cursor Preview / Fighting the Chemistry`
  - `Cursor Preview / Campus`
  - `Cursor Preview / Golden Moment`
  - `Cursor Preview / Shadow`
- Bound each Observation row to its matching cursor preview component through Framer's custom cursor setting.
- Kept the default Observation state as only the four work rows; no Preview Stage and no inline preview image is visible until hover.

Verification:

- Framer review reports no blocking errors after the custom cursor correction.
- Static default screenshot remains clean: four work options only, no preview residue.
- Full live pointer-hover QA in browser is still pending.
- Publishing is still pending.

### 2026-07-14 Cursor preview image completeness pass

Issue:

- Custom cursor previews should preserve each work image's content integrity. The preview component must not use one fixed crop ratio when source works have different orientations.

Completed in Framer:

- Adjusted cursor preview component dimensions to match source image proportions more closely:
  - `Fighting the Chemistry`: `178 × 216`
  - `Campus`: `178 × 216`
  - `Golden Moment`: `178 × 216`
  - `Shadow`: `252 × 168`
- This keeps the three portrait works in a portrait cursor and gives the Shadow landscape work a landscape cursor, reducing unwanted crop and preserving the intended image content.

Notes:

- Source dimensions were checked from file metadata / web derivatives only; original images were not opened in visual context.
- Publishing is still pending.

### 2026-07-14 Cursor preview transition pass

Issue:

- Switching between separate custom cursor components made the image preview change feel abrupt.

Completed in Framer:

- Replaced the four separate cursor preview components with one unified native Framer component:
  - `Cursor Preview / Works`
- Added four variants inside that component:
  - `Fighting the Chemistry`
  - `Campus`
  - `Golden Moment`
  - `Shadow`
- Rebound all four Observation rows to the same custom cursor component, changing only the active variant per row.
- Added a spring-duration transition to the cursor preview variants and custom cursor binding, so moving between rows transitions the preview instead of hard-swapping separate components.
- Kept the content-complete dimensions from the previous pass:
  - portrait works: `178 × 216`
  - Shadow: `252 × 168`

Verification:

- Framer review reports no warnings or errors for the unified cursor component after arranging variants on the component canvas.
- Publishing is still pending.
