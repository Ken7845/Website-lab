# 2026-08-18 — Homepage Cold-Outreach Build

- Page: Home `/`
- Request status: Pass
- Canvas write status: Complete; unpublished

## User request — verbatim

> 现在要搭建一个framer项目HK Place，给一家香港菜餐厅做一个网站，用于cold outreach，为了降低每次outreach的成本，所以这次网站只先做home page，但是每个关联到其他page的section要预留跳转按键，我已经在framer里面创建了画布，再开始搭建之前要阅读website-lab知识库了解搭建要求，然后先把整体的方案和风格基调给我，在生成checklist后再开始搭建，要求一次性完成整个page，细节和各种要求都必须完善，图片和餐厅基本信息在website-lab的content-library里

## Derived execution checklist

- [x] Read Website Lab router, change control, image workflow, project manifest template and relevant design/layout/component guidance.
- [x] Locate and read HK Place basic facts.
- [x] Inspect one safe contact sheet covering all supplied HK Place images.
- [x] Inspect the live Home canvas without writing.
- [x] Establish the overall plan and visual tone in `PROJECT.md`.
- [x] Create the project checklist index and page-specific Home checklist.
- [x] Receive explicit user confirmation of this checklist.
- [x] Show the Framer Agent gate receipt before implementation.
- [x] Show the Component contract receipt before reusable-component writes.
- [x] Build the shared design foundation.
- [x] Build the complete Desktop Home page.
- [x] Author Tablet and Phone compositions rather than scaling Desktop.
- [x] Add valid links/anchors and reserve future-page CTAs without broken destinations.
- [x] Add SEO, semantic headings, Alt, focus and Reduced Motion treatment.
- [x] Run targeted readback, representative previews and preflight.
- [x] Resolve every in-scope diagnostic or mark a fact-based Blocked item.
- [x] Keep the project unpublished.

## Component Requirement Contract

Contract status: Pass. Ownership, controls, representative instances and responsive behavior were read back after implementation.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Components stay surface-local; Sections own background and vertical rhythm | Page Section | `framer-components/SKILL.md#Assign-responsibility`; Home checklist | Read Section and representative instance parents | One representative Section crop |
| Available width / placement | Page instances own available width; components fill or hug according to role | Page Instance | `framer-components/SKILL.md#Assign-responsibility` | Definition → Instance → Breakpoint chain | Desktop and Phone representative instances |
| Visible boundary / border / surface | Button owns its visible fill/border; cards own only intentional local surface | Component Definition | `framer/basic/patterns/buttons.md#component-内部结构`; `framer/basic/standards/website-baseline.md#4-componentsvariants-与-properties` | Definition styles | Default/hover representative state |
| Internal padding / hit area | Button and card definitions own internal padding; minimum touch target respected | Component Definition | `framer-components/SKILL.md#Preserve-behavior-and-editability` | Definition attributes | Phone tap target inspection |
| Readable max-width | N/A — compact Button has no readable-line-length contract; card text fills its bounded internal column and prose width belongs to the deepest Page content owner | Page / Definition as noted | `framer-layout-responsive/SKILL.md#Resolve-width-ownership` | Text and parent width chain | Desktop and Phone wrap check |
| Editable content / Properties | Button label/link; Dish title/image/alt; Review quote/source fields where source exists | Component Properties | `framer-components/SKILL.md#Assign-responsibility` | Controls/instances readback | First/middle/last instance sample |
| States / routes | Button default/hover/pressed/focus where native; content records are not Variants | Component Definition + Instance link | `framer-components/SKILL.md#Preserve-behavior-and-editability` | Variant/link readback | One real menu and one phone route |
| Breakpoint contract | Compact components remain content-driven; Page rearranges composition; no hover dependency on Phone | Component Definition + Page Breakpoint | `framer-layout-responsive/SKILL.md#Transform-each-breakpoint` | Desktop/Tablet/Phone values | Representative 810/390 checks |
| Accessibility / touch / focus | Visible focus, readable contrast, semantic label, comfortable touch area, truthful Alt | Definition + Instance content | `design-taste/SKILL.md#Universal-requirements`; Home checklist | Focus/link/Alt properties | Keyboard/focus and Phone sample |
| Evidence sample | Button: primary/secondary; Dish: first/middle/last; Review: first/last | QA | `framer-components/SKILL.md#Implement-in-one-layer-at-a-time` | Targeted serialization | Targeted preview only |

## Confirmation Gate

- [x] User confirms the plan, visual direction and recorded checklist.
- [x] Only after confirmation may the first Canvas write begin.

## Completion Evidence

- Complete section order: Navigation, Hero, Trust, Restaurant Introduction, Menu Highlights, Food Gallery, Reviews, Visit Us, Closing CTA and Footer.
- Responsive breakpoints: Desktop, Tablet and Phone with intentional rearrangement rather than uniform scaling.
- Shared foundations: seven semantic colors, seven text styles, three link styles and three reusable components.
- Conversion paths: menu, directions, telephone and same-page anchors all resolve to real destinations.
- Metadata: truthful title/description, approved Open Graph image and no-index Demo protection.
- QA: one h1 per breakpoint replica, ordered section headings, semantic layer names, image Alt coverage and no dead link inventory.
- Accepted exception: Phone stack diagnostics are a Framer replica-measurement false positive; representative screenshots show no visible overlap.
- Blocked facts: complete weekly hours, formal logo/favicon and public-use rights were not supplied and were not fabricated.
- Publishing: not performed.

## 2026-08-18 Detail Revision

- [x] Add a shallow light outline so the Closing CTA Call Us button separates from the lacquer-red background.
- [x] Fill the Tablet Menu Highlights 2×2 grid with a fourth Dish Highlight using verified Wonton Lo Mein content and a supplied distinct noodle image.
- [x] Reduce excessive Tablet Review Quote whitespace while preserving all quote and source text.
- [x] Remove `maxWidth` from outer and near-outer page Stacks across all breakpoints; final page-wide readback count is zero.
- [x] Preserve all existing content, routes, three-breakpoint structure and unpublished status.
- QA result: Pass. Closing CTA, Tablet Menu and Tablet Reviews received one bounded visual check each; affected nodes received final structural readback.
