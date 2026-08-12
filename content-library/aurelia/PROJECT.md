# AURELIA Project

## 1. Project Identity

- Project name: AURELIA
- Platform: Framer
- Project type: Marketplace template for a private dining restaurant
- Framer project URL: `https://framer.com/projects/6EYvZfFo1CleDR77cYUF`
- Framer project ID: `6EYvZfFo1CleDR77cYUF`
- Current live sitemap: Home `/` and Menu `/menu`
- Status: Home exists across Desktop, Tablet, and Phone; the requested Menu Opening, story, seven-dish card revision, and Desktop/Tablet expandable dish-card interaction are implemented, with full-page QA still open
- Content status: Fictional Demo and Draft
- Demo URL: Missing
- Last canvas audit: 2026-08-11
- Last document update: 2026-08-11

This file records the current Framer canvas as the source of truth. Earlier plans based on `The Evening`, `The Table`, and the former linear arrival-to-reservation story have been retired. Do not rebuild those structures from old chat history or older copies of this document.

All restaurant names, menu descriptions, reservation details, and operational information are fictional demo content for a Marketplace template. Buyers must replace or approve them before publication.

## 2. Current Design Read

AURELIA is a highly spacious, editorial Framer template for independent chefs, private dining rooms, supper clubs, and small reservation-led restaurants.

The current Home does not narrate one evening as a literal chronological journey. It moves from a broad belief into progressively more tangible evidence:

```text
Place
→ Belief
→ Person
→ Room
→ Craft
→ Rhythm
→ Dishes
→ Invitation
```

This is the narrative model that future pages must extend.

### Design dials observed on the live canvas

- `DESIGN_VARIANCE: 8` - asymmetric image scales, large open fields, deliberate edge alignment, and different layout families by section.
- `MOTION_INTENSITY: 4` - line reveals, short vertical image entrances, restrained parallax, native cursor and variant interactions.
- `VISUAL_DENSITY: 2` - one thought per section, long pauses, few simultaneous elements.

### Brand character

- Quiet, exact, intimate, contemporary, observant.
- Editorial rather than decorative luxury.
- Photographs act as evidence of place, authorship, process, and food.
- Copy is short, declarative, and specific enough to feel authored.
- White space is an active part of the composition, not unfinished space.
- The interface avoids repeated cards, badges, labels, numbered sections, fake awards, fake prices, review carousels, and generic fine-dining claims.

## 3. Website Goal

- Primary buyer: a design-conscious independent chef, supper club, or private dining venue.
- Primary visitor: a guest deciding whether the restaurant's point of view, room, food, and format are right for them.
- Primary conversion: begin a real reservation or private-dining enquiry.
- Primary CTA label: `Reserve a seat`.
- Trust requirements: clear demo status, legible information, believable content structure, easy asset replacement, mobile reliability, and a real booking destination before publication.

The Home creates desire and establishes the world. Supporting pages should answer practical or deeper questions without replaying the Home section sequence.

## 4. Live Framer Sitemap and Components

### Current sitemap

| Page | Path | Live status |
|---|---|---|
| Home | `/` | Built |
| Menu | `/menu` | Requested revision built; full-page QA in progress |

Private Dining, About, and Reserve do not yet exist in the Framer sitemap.

### Current reusable components

- `Navigation`: Desktop, Tablet, Phone, and Phone Open variants.
- `ButtonPrimary`.
- `DishSelector`: seven dish states for Desktop, Tablet, and Phone.
- `MenuDishCard`: reusable dish card with editable image/Alt, dish name, short description, and detailed Story. Desktop and Tablet add shared Hover plus click-to-expand states; collapsed uses Home's `Arrow Essentials / Arrow Right`, Expanded hides name and short description so only Story remains, and Phone stays static.
- `EveningChapterRow`: editable title, description, and chapter image properties.
- `ChapterCursorPreview`: four visual cursor-preview states.
- `AURELIA`: custom cursor component.
- `hero` and `Hero Loader`.
- External `Lenis` smooth-scroll instance.

### Current navigation behavior

- Fixed, white, 35px-high navigation with a bottom hairline.
- Desktop and Tablet links currently point to Home anchors: `Vision`, `Chef`, and `Reserve`.
- Phone uses closed and open variants with the same anchor destinations.
- AURELIA uses League Gothic in the navigation.
- The navigation is not yet a cross-page information architecture.

Before supporting pages are built, convert the shared shell to a Layout Template or another verified shared structure so Navbar and Footer are not copied page by page.

## 5. Current Home Narrative

The following sequence was read directly from the live Framer Canvas on 2026-08-11.

### 1. Opening

Purpose: establish place and restraint before any explanation.

Current content and layout:

- Image-only opening with no visible headline, paragraph, or CTA.
- Desktop section is 100vh with a 760px minimum height.
- The architecture image is centred within the white page field at roughly 80% width and 540px height on the 1200px Desktop canvas.
- The image uses restrained parallax and custom cursor behavior.
- A hidden AURELIA text layer exists inside the Hero, but it is not visible and is not part of the current composition.
- Do not restore the former oversized Hero wordmark unless the user explicitly requests it.

Narrative effect: the site begins with observation, not branding or conversion.

### 2. Vision

Purpose: state the belief that controls the rest of the site.

- Heading: `An evening made for attention.`
- Body: `AURELIA is built around the belief that a meal can alter the pace of a night. Fewer distractions. More time for what is already in front of you.`
- Anchor: `#vision`.
- Desktop uses approximately 300px top and 280px bottom padding.
- The large headline occupies most of the available width; the body remains a narrow 520px column.
- There is no image in this section.

Narrative effect: a long typographic pause turns the opening image into a point of view.

### 3. Chef

Purpose: give the belief a human source without becoming a biography or résumé.

- Heading: `The table begins with someone noticing.`
- Body: `Before a plate reaches the room, someone has considered the season, the room, and the people who will sit together. This is the space for the chef’s real voice—not a résumé, but a point of view.`
- Anchor: `#chef`.
- Desktop pairs a tall portrait with a narrower text column aligned toward the bottom.
- The portrait and copy are unequal in scale, with a wide 112px gap.

Narrative effect: authorship appears through attention and observation, not credentials.

### 4. Space

Purpose: show architecture as an active ingredient in the experience.

- Heading: `The room is part of the menu.`
- Body: `Light changes the table. Sound travels differently after the room fills. The architecture is not a backdrop; it gives the evening its rhythm.`
- Anchor: `#space`.
- One smaller vertical exterior image and one larger square dining-room image form an asymmetric pair.
- The heading appears before the images; the narrow body copy appears after them.
- Desktop is approximately 1812px tall with very large internal gaps and section padding.

Narrative effect: the page expands spatially after the intimate Chef section.

### 5. Craft

Purpose: connect the restaurant's point of view to physical work.

- Heading: `Time is an ingredient.`
- Body: `The work happens close to the hands: a stock held back for another hour, a sauce adjusted once, a texture left imperfect on purpose. Precision is felt before it is explained.`
- Anchor: `#craft`.
- Soft grey surface creates the first restrained background change.
- Desktop uses a two-column layout with text at left and a tall working image at right.

Narrative effect: the page becomes more material and close to the hands without increasing visual density.

### 6. Experience

Purpose: describe the rhythm of the evening without presenting a priced menu.

- Heading: `A table has its own tempo.`
- Body: `There is no performance to follow. The night opens slowly, gathers around the table, then leaves room for what happens after dinner.`
- Anchor: `#experience`.
- Four fixed chapter rows: `Arrival`, `First plates`, `From the kitchen`, and `After`.
- Desktop and Tablet use title-and-description rows with fine dividers.
- Phone changes the row composition rather than squeezing the Desktop layout.
- Each row has a corresponding native cursor image preview.
- A full-width image of prepared dinner plates follows the chapter sequence.
- Closing line: `A first pour. A long pause. One last cup.`
- This is the longest Home section and the main narrative body.

Narrative effect: time enters after belief, person, room, and craft have already been established.

### 7. Signature

Purpose: turn the abstract idea of a changing menu into an explorable set of dishes.

- The section contains the `DishSelector` component rather than a fixed image-and-copy block.
- Seven dishes have editable image, title, long story, and Phone description controls.
- Desktop and Tablet use a selected dish, text reels, numeric reel, and thumbnail navigation.
- Phone uses its own responsive six-column image exchange grid and device-specific variants.
- State changes use native Framer variant transitions.
- The section is a concentrated dark editorial object between the long white Experience section and the final invitation.

Narrative effect: this is the Home's interactive and visual climax. It must not be duplicated as a generic grid on another page.

### 8. Invitation

Purpose: turn the accumulated atmosphere into a single action.

- Heading: `There is a place at the table.`
- Body: `When the evening feels right, begin with a date. The rest can be arranged around the table.`
- CTA: `Reserve a seat`.
- Anchor: `#reserve`.
- Near-black background, white type, and a compact button create the only major full-section inversion.

Narrative effect: the dark transition reads as a conclusion, not a promotional CTA block.

### 9. Footer

- AURELIA wordmark.
- Description: `A story-led Framer template for private dining rooms and independent chefs.`
- Current links: `Vision`, `Chef`, `Space`, `Reserve`.
- Demo notice and template copyright.
- White background returns after the dark invitation.

## 6. Current Visual System

### Typography read from live styles

- Hero/navigation brand type: League Gothic. The former visible Science Gothic Hero plan is retired.
- Display: Inter Medium, width axis 92, 138px Desktop, 96px Tablet, 54px Phone, very tight tracking and sub-1 line height.
- Heading 2: Inter Medium, 82px Desktop, 62px Tablet, 40px Phone.
- Heading 3: Inter Medium, 38px Desktop, 31px Tablet, 27px Phone.
- Body Large: Inter Regular, 26px Desktop, 22px Tablet, 19px Phone.
- Body: Inter Regular, 17px Desktop, 12px Tablet, 11px Phone in the current live preset.
- Button: Inter Semibold, 10px in the current live preset.
- Display headings reveal by line with opacity, short vertical movement, and blur.

The small Tablet and Phone Body values and the 10px Button value are current canvas facts, not an automatic recommendation for new pages. Recheck their accessibility and readability during the shared-system pass before reusing them broadly.

### Color tokens read from live styles

- `Color/Background`: `#FFFFFF`.
- `Color/Inverse`: `#151515`.
- `Color/Surface`: `#EEEEEC`.
- `Color/Text`: `#151515`.
- `Color/Muted`: `#6F6F6F`.
- `Color/Border`: `#C9C9C7`.

The site uses one locked light editorial system. The Craft section uses the soft-grey surface, and the Invitation section uses the near-black inverse color as a deliberate final transition.

### Layout and rhythm

- Desktop content uses 32px page gutters and internal widths up to 1440px.
- Tablet uses 28px gutters.
- Phone uses 20px gutters.
- Desktop section padding generally sits between 220px and 300px for major narrative sections.
- Body columns stay narrow even when headlines and images are wide.
- Image compositions alternate between isolated media, portrait-and-copy, asymmetric pairs, tall process photography, and one full-width narrative image.
- Section layouts are not interchangeable templates.

### Motion and interaction

- Native Framer effects and variants are preferred.
- Images generally enter once with opacity, a short vertical movement, and slight scale adjustment.
- Display headings reveal line by line.
- Hero uses restrained native parallax.
- Evening Chapters use cursor previews.
- DishSelector uses native state transitions and editable controls.
- Avoid adding continuous marquees, scroll hijacking, heavy parallax stacks, custom code, or decorative motion.
- Reduced-motion behavior remains a required final QA item.

## 7. Content Facts and Blockers

| Fact | Current value | Status |
|---|---|---|
| Brand name | AURELIA | Demo |
| Restaurant type | Private dining restaurant template | Demo |
| Address | Not provided | Missing |
| Opening hours | Not provided | Missing |
| Phone | Not provided | Missing |
| Email | Not provided | Missing |
| Capacity | Not provided | Missing |
| Menu price | Not provided | Missing |
| Chef name and verified biography | Not provided | Missing |
| Dietary policy | Not provided | Missing |
| Private-dining formats | Not provided | Missing |
| Booking provider or form endpoint | Not provided | Missing |
| Response time | Not provided | Missing |
| Social links | Not provided | Missing |
| Image licensing | Pexels source filenames retained; Marketplace redistribution must be verified | Draft |
| Favicon and Open Graph cover | Not provided | Missing |

Do not invent operational facts to make the new pages look complete. Structure and visibly marked Demo content may be built while those facts remain blocked.

## 8. Revised Supporting-Page Architecture

The retired `The Evening` and `The Table` page plan must not be restored. The revised site should use direct, buyer-editable page names and give each page a different narrative responsibility.

Plan status: approved for phased, page-by-page implementation on 2026-08-11. Every supporting page remains `To do` until it passes its page checklist and the required Framer Preflight.

| Page | Path | Main question | Status |
|---|---|---|---|
| Home | `/` | What kind of place is AURELIA? | Built |
| Menu | `/menu` | What is served, and how does it change? | To do |
| Private Dining | `/private-dining` | What kind of gathering can happen here? | To do; facts partly blocked |
| About | `/about` | Who is behind the point of view? | To do; biography blocked |
| Reserve | `/reserve` | How do I request or confirm a seat? | To do; integration blocked |

Optional Journal or Gallery content may be added after the core conversion path is complete. Neither belongs in the first build or primary navigation yet.

### Page 1: Menu

Role: expand the food language introduced by Experience and DishSelector without copying either Home interaction.

Recommended structure:

1. A reference-directed typographic opening with a large upper field, oversized full-width `menu` h1, compact supporting line, and a left-owned food image entering beneath the title.
2. A full-screen soft-grey story statement with oversized `The menu listens.` at left and a narrow right column beginning with a small food image followed by dense long-form copy.
3. A seven-dish editorial sequence using one shared card pattern: image, dish name, short description, and Home Arrow Right when collapsed; a larger image with Story-only text and Arrow Up when expanded on Desktop/Tablet; static content on Phone. Page Instances use Fill width so the sequence follows its container in Preview.
4. One controlled image interruption between movements, using a different crop and scale from Home.
5. A compact practical note for dietary accommodation, menu format, and pricing only when verified values exist.
6. A final `Reserve a seat` handoff.

Content system:

- Current implementation uses the reusable `MenuDishCard` Component because the source count is a fixed seven dishes. Use a CMS collection later only if buyers need frequent add/remove/reorder workflows.
- Current editable fields: Dish Image with per-instance Alt, Dish Name, Description, and Story. Recommended future fields: movement, optional dietary note, order, and visibility.
- Price must remain optional and hidden when empty.
- Do not repeat the fixed Home Evening Chapters or embed another DishSelector.

Buyer editing note:

- Select any card instance on `/menu` and edit its `Dish Image` (including Alt), `Dish Name`, `Description`, or `Story` Property; these values affect only that instance.
- Reorder dishes by moving the seven card instances within the `Centre of the Meal` stack. Edit the shared `MenuDishCard` Component only when the layout should change for all seven cards.
- Optional dietary note, optional price, visibility, and order controls remain follow-up work; do not invent values for them.

Distinct visual device:

- Let density change across the page. Opening content is sparse, the centre becomes typographically denser, and the final movement opens back into white space.
- Food images appear as interruptions, not thumbnails beside every menu item.

### Page 2: Private Dining

Role: explain the offer for people planning a gathering, without turning the site into an events brochure.

Recommended structure:

1. A room-led opening using one architectural image and a compact statement.
2. A section explaining what private dining changes about pace, service, and menu decisions.
3. A flexible event-format area for dinner, celebration, or hosted gathering. Use replaceable editorial rows or columns, not icon cards.
4. A room-and-table composition showing how guests relate to the space.
5. A practical facts block for capacity, availability, accessibility, lead time, and minimum spend only after real values are supplied.
6. A focused enquiry handoff leading to Reserve with a preselected private-dining intent when the form system supports it.

Content system:

- Keep formats as ordinary editable content unless buyers truly need a variable-length list.
- Do not invent capacities, prices, days, or service inclusions.
- Empty practical facts must disappear cleanly rather than display placeholder numbers.

Distinct visual device:

- Use wider horizontal relationships than Home, with room images spanning across text boundaries.
- The page should feel social and spatial, while Home remains introspective.

### Page 3: About

Role: deepen authorship. It must not repeat the Home Chef section or become a CV.

Recommended structure:

1. A portrait-led opening with the chef or host's verified name when available.
2. One approved first-person statement explaining why the project exists.
3. A process section connecting sourcing, repetition, adjustment, and service.
4. A small sequence of working details rather than a conventional biography timeline.
5. A relationship section connecting the chef, team, room, and guests.
6. A quiet link to Menu and the final reservation action.

Content system:

- Chef name, biography, awards, past restaurants, sourcing claims, and team facts remain blocked until verified.
- Avoid fabricated milestones, press logos, testimonials, and awards.
- If no real biography is supplied, keep this page in a clearly marked Demo state rather than presenting fiction as fact.

Distinct visual device:

- Narrower text columns, closer image crops, and fewer total sections than Home.
- Use material and working images instead of repeating the Home portrait-and-copy layout.

### Page 4: Reserve

Role: provide the most direct and operationally clear page in the site while retaining AURELIA's calm visual language.

Recommended structure:

1. Compact opening: `Choose a night.` or another approved direct title.
2. One sentence explaining whether the action is an enquiry or a confirmed booking.
3. Real booking embed, external booking handoff, or native enquiry form.
4. Form fields only when needed: name, email, preferred date, party size, booking type, and message.
5. Complete states: default, focus, filled, error, disabled, submitting, success, and service failure.
6. Verified fallback contact method.
7. Practical information such as address, arrival time, cancellation policy, accessibility, and response time only when supplied.

Content system:

- Current booking provider and form endpoint are missing, so integration is blocked.
- A Demo form may be designed, but it must not imply that a reservation was confirmed or that data was submitted.
- `Reserve a seat` remains the single label for the primary reservation intent across the site.

Distinct visual device:

- Reduce the extreme section length used on Home.
- Use a quiet two-zone composition on Desktop and a strict single-column sequence on Phone.
- The form should feel like the final clear decision after the site's expansive storytelling.

## 9. Cross-Page Narrative Rules

- Home establishes the complete worldview; supporting pages deepen one subject each.
- Do not copy Home sections into new pages with different headings.
- Each page gets one dominant composition and one visual climax.
- Do not repeat the Home DishSelector, cursor-preview table, portrait-and-copy layout, or Space image pair as generic modules.
- Keep large Display type, narrow body columns, sharp image edges, and long pauses as the shared language.
- Use photography selectively. A new page does not need an image beside every paragraph.
- Maintain the white, near-black, and grey token system.
- Continue the same copy register: short, observant, and concrete.
- Avoid generic luxury terms, fake scarcity, awards, ratings, invented numbers, and sales-heavy CTA blocks.
- Primary navigation should eventually become `Menu`, `Private Dining`, `About`, and `Reserve` once those pages exist.
- Home anchors may remain useful in the Footer or as contextual links, but they should not substitute for the final cross-page navigation.

## 10. Responsive Direction

- Breakpoints: Desktop 1200, Tablet 810, Phone 390, with additional stress checks at 320 and wider desktop widths.
- Preserve the current gutter rhythm: 32px Desktop, 28px Tablet, 20px Phone unless a verified shared system changes it.
- Large Desktop compositions must transform, not merely shrink.
- Phone should use a strict reading order, full-width text ownership, stable image ratios, and at least 44px interactive targets.
- Long Display headings require independent wrap checks at all breakpoints.
- Menu CMS entries must tolerate long dish names, missing images, missing prices, and longer descriptions.
- Private Dining practical facts must collapse cleanly when fields are absent.
- Reserve must remain fully usable at 320px and under mobile browser chrome.

## 11. Recommended Build Order

```text
1. Confirm revised information architecture and page purposes - complete
2. Audit and establish shared Layout Template, Navbar, Footer, and link strategy
3. Build Menu as the first supporting page
4. Complete Menu Desktop, Tablet, Phone, CMS decision, links, SEO, and targeted Preview
5. Build Private Dining with missing facts visibly blocked
6. Build About after approved chef or host content is available
7. Build Reserve structure and states
8. Connect a real booking provider or form endpoint
9. Run Home regression, Website Preflight, Marketplace stress tests, and Basic Polish Gate
```

Menu should be the first new page because it can use the current Demo food content and existing assets without inventing operational facts. Reserve is the last core build because its real integration is currently blocked.

### Page checklist files

- [Home checklist](./checklist/home.md): existing page regression, unresolved QA, and Website foundation dependencies.
- [Menu checklist](./checklist/menu.md): first new page and recommended next build.
- [Private Dining checklist](./checklist/private-dining.md): room-led offer page with fact-dependent practical information.
- [About checklist](./checklist/about.md): authorship page with biography and claim controls.
- [Reserve checklist](./checklist/reserve.md): booking or enquiry page with full form and service states.
- [Checklist index and workflow](./checklist/README.md).

## 12. Build Status Matrix

| Page | Content | Structure | Components | Links | SEO | Desktop | Tablet | Phone | Preview |
|---|---|---|---|---|---|---|---|---|---|
| Home | Demo | Built | Built | Home anchors only | Existing title and description | Built | Built | Built; targeted QA caveat | Partial targeted QA |
| Menu | Demo | Requested scope built | `MenuDishCard` expandable interaction built; CMS deferred | Existing handoff; destination blocked | Existing title and description | Collapsed/expanded states visually checked | Collapsed/expanded states visually checked | Static card visually checked | Component steady states checked; live click path and full-page five-width QA remain |
| Private Dining | Planned; facts partly blocked | To do | To do | To do | To do | To do | To do | To do | To do |
| About | Planned; biography blocked | To do | To do | To do | To do | To do | To do | To do | To do |
| Reserve | Planned; integration blocked | To do | Form system pending | To do | To do | To do | To do | To do | To do |

## 13. Known QA and Delivery Work

- Home's current page-level narrative has been visually reviewed once at low resolution on Desktop and structurally read across all three breakpoints.
- Framer's on-demand Phone breakpoint screenshot may resolve to a 200px editor replica instead of the real responsive page. Use real Preview for Phone visual conclusions.
- Hero contains hidden text and overlay layers. Preserve their current hidden state unless a new Hero direction is explicitly approved.
- Live text includes some em-dash characters in Demo copy. They remain canvas facts and should be reviewed during the copy-polish pass; this document does not authorize changing them now.
- Verify the Lenis instance, reduced motion, focus states, link destinations, and any remaining overflow diagnostics during Preflight.
- Recheck live `Type/Body` Tablet/Phone sizes and the 10px Button preset for accessibility before reusing them across new pages.
- Image and font licensing, favicon, Open Graph cover, demo URL, Remix URL, and Marketplace editing instructions remain incomplete.

## 14. Decisions and Retired Directions

| Decision | Status | Reason | Date |
|---|---|---|---|
| Home is belief-to-evidence, not a literal chronological evening | Active | Matches the live Canvas sequence | 2026-08-11 |
| Centred image-only Hero with no visible wordmark or CTA | Active and user-edited | Matches the live Canvas | 2026-08-11 |
| Large Inter editorial type, League Gothic brand details | Active | Matches live styles | 2026-08-11 |
| White, near-black, and soft-grey palette | Active | Matches live tokens | 2026-08-11 |
| One dark Invitation transition | Active | Provides a controlled conclusion | 2026-08-11 |
| Evening Chapters remain fixed Home components | Active | Protects the four-part composition and cursor states | 2026-08-11 |
| DishSelector remains a fixed seven-dish component | Active | Protects its responsive and transition logic | 2026-08-11 |
| Menu uses one reusable `MenuDishCard` Component with editable image/Alt, name, Description, and Story Properties | Active | Keeps the fixed seven-dish source consistent and buyer-editable without seven content Variants or premature CMS | 2026-08-11 |
| `MenuDishCard` expands only on Desktop and Tablet; Phone remains static | Active | Desktop/Tablet can reveal editorial depth with native state Variants and shared Hover, while Phone avoids hover-only affordances and extra interaction weight | 2026-08-11 |
| `MenuDishCard` reuses Home `Arrow Essentials / Arrow Right`, hides name and short Description in Expanded, uses Fill Page Instance width, and fixes motion at `spring-physics` stiffness 250 | Active | Keeps the affordance consistent with Home, gives Story full ownership of the expanded text area, prevents fixed-length Preview behavior, and standardizes motion across states | 2026-08-11 |
| Menu Opening and Changing Menu Statement use the supplied Paul Kalkbrenner page compositions as layout references | Active | Establishes a stronger typographic opening and a high-density asymmetric story section while preserving AURELIA content, Inter typography, and the existing color tokens | 2026-08-11 |
| `The Evening`, `The Table`, `Reserve` four-page plan | Retired | Came from an earlier direction that was overturned | 2026-08-11 |
| Oversized visible Science Gothic Hero wordmark | Retired | The text layer is hidden in the current Hero | 2026-08-11 |
| Home as arrival-to-reservation chronology | Retired | Does not describe the live Canvas | 2026-08-11 |
| Full menu or equal dish grid on Home | Retired | DishSelector is the current focused food experience | 2026-08-11 |

## 15. Recovery State

- Current Framer project: `6EYvZfFo1CleDR77cYUF`.
- Current page: Menu `/menu`.
- Current conversation session: `5`.
- Canvas writes in the 2026-08-11 Menu revision: Opening and Changing Menu Statement rebuilt; `MenuDishCard` created; seven dish instances added; old three inconsistent cards removed; Tablet and Phone page breakpoints added. A later reference pass rebuilt only Opening and Changing Menu Statement around the supplied music/impact compositions.
- Knowledge-base page checklists: `./checklist/`.
- Live Menu breakpoint roots: Desktop 1200 `CuPy0iH7F`, Tablet 810 `z5tC4bH2D`, Phone 390 `AyfdERUsu`.
- Reusable Menu component: `MenuDishCard` with Desktop, Tablet, Phone, Desktop Expanded, and Tablet Expanded normal Variants; Desktop/Tablet Hover Gesture Variants; editable Dish Image/Alt, Dish Name, Description, and Story content. Collapsed arrows use `Arrow Essentials / Arrow Right` matching Home; Expanded hides Dish Name and Description, shows Story only, and uses `Arrow Up`.
- Component behavior: Desktop and Tablet collapsed cards use Home's `Arrow Essentials / Arrow Right` and exact `SET_VARIANT` paths to their matching Expanded state; Expanded cards enlarge the image, hide Dish Name and Description, show Story only, use the same set's `Arrow Up`, and return to the matching collapsed state. Phone explicitly has no arrow or `onTap`.
- Component visual evidence: on-demand screenshots passed for Desktop collapsed/expanded, Tablet expanded, Phone static, and the full Menu page. All 21 Page Instances read back as Fill (`1fr`), all seven component states use `spring-physics 250 30 1 0s`, and Preview preflight returned ready with zero errors/warnings; no publish was performed.
- Page-instance evidence: all seven cards retain independent Image, Name, Description, Story, and Image Alt values; first, middle, and final instances were checked across all three page breakpoints.
- Opening evidence: Desktop uses a large upper field, a full-width oversized `menu` h1, 15px compact supporting line, and a 58%-width left-owned image; Tablet uses a 72%-width image; Phone uses a full-width 350×280 image.
- Story evidence: Desktop uses a 58% oversized headline and narrow right story column; the complete story is one Rich Text node containing six paragraph blocks rather than six separate layers. Tablet preserves the asymmetric two-column layout; Phone changes to a vertical headline → story sequence with 14px body copy.
- Reference visual evidence: one final Desktop screenshot was viewed for each revised Section and compared against the two supplied reference screenshots.
- Known diagnostic exception: page-stack spacing lint can report false negative spacing on layout-template-backed breakpoint replicas; targeted serialized section rects on Desktop/Tablet were sequential. Framer publish preflight after the interaction work returned `ready` with zero errors and zero warnings; no publish was performed.
- Reusable pattern documentation: `framer/advance-design/expandable-editorial-card.md`.
- Remaining Menu QA: operate Desktop and Tablet Hover → Expand → Collapse in a live external Page Preview, verify focus presentation, run 320/390/810/1200/1440+ full-page QA, reassess Kitchen Interruption, stress-test optional/missing fields and extreme image ratios, verify the shared handoff/link, and complete overflow/accessibility review.
- Next safe action: re-read the Menu checklist, then complete the remaining full-page Preview and blocker-dependent checks without changing Navbar, Footer, Home `DishSelector`, or other pages.
