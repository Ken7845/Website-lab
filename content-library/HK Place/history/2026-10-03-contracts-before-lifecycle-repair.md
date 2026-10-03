# Contract records before lifecycle repair — 2026-10-03

Status: Immutable historical evidence. No new Canvas verification. Each fenced section is the exact original section from the named source.

## Source: content-library/HK Place/checklist/home/2026-08-18-homepage-cold-outreach-build.md

````markdown
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

````

