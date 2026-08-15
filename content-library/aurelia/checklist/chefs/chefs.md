# Chefs Page Checklist

Page: Chefs  
Path: `/chefs`  
Status: Demo structure and responsive Component built; Partial Pass; final content and QA Blocked  
Primary CTA: `Read their story` / `Close story` (native disclosure control; final labels require approval)

## Original request (verbatim)

> 你现在给我一个chefs页面的方案，我觉得主要讲的就是厨师的背景故事以及自己对于烹饪的态度或者独到的见解，我的想法这个页面进去是三个厨师的portrait，因为我们刚刚好有三张不同厨师的portait，从上往下排列，左边是portrait图片，右边是名字，和CTA的了解更多的按键，点击后这个向下展开，开始讲内容，你参考这个方案，然后写一个这个页面的checklist

## Scope lock and Definition of Ready

### Goal

Create a distinct editorial `Chefs` page that introduces three people through their portraits, then lets visitors open each person's background and cooking perspective without making the initial page dense. The page should add human authorship to AURELIA without replacing the existing `/about` culture page.

### Confirmed direction

- The opening is a concise page title followed by exactly three vertically sequenced chef portrait rows.
- On Desktop and Tablet, each row is a clear two-column relationship: portrait on the left; name, role (only if verified), and disclosure control on the right.
- The rows are intentionally unequal in portrait crop/vertical rhythm where source images allow; they are not three identical cards.
- Selecting `Read their story` expands the relevant row downward using a native Framer Variant. Expanded information must stay in the same row's reading and keyboard order.
- The expanded story covers a verified background and the chef's approved point of view on cooking. It does not become a résumé, award list, or generic chef biography.
- Phone changes to portrait → name/role → disclosure control → story as one strict vertical sequence per chef. It must not squeeze the desktop two-column composition.

### Required source material before factual content can be written

- Three approved portraits, chosen from `images/Chefs/portrait/` after the required image residency/contact-sheet process.
- Each chef's verified name, role, preferred pronouns if required, short background, approved first-person quote or viewpoint, and any claims that may appear.
- An explicit decision on whether these are real people, clearly labelled Demo profiles, or buyer-editable placeholders.
- Approved final page title, page metadata, and CTA wording. Chefs now appears in the shared primary navigation; final metadata and labels remain open.

### Blocked facts

Do not invent names, titles, restaurants, awards, years, nationalities, training, sourcing relationships, dietary claims, or team structures. Until approved material exists, build only clearly labelled Demo structure and editable placeholder fields.

## Page narrative

```text
Three people
→ first encounter through portrait
→ personal background
→ individual way of seeing cooking
→ return to the collective AURELIA culture
```

The page should feel intimate and observant, rather than like an agency team directory. `/about` continues to explain the restaurant's shared culture; `/chefs` explains the individual voices that shape it.

## Proposed content model

Each chef uses one reusable `ChefStoryRow` Component Instance with the current live Properties:

- `Portrait` responsive image.
- `Chef Name` string.
- Optional `Chef Role` string.
- One `Content` Rich Text value for the complete story; people are Page Instances, not content Variants.

The current component does not expose portrait Alt or the embedded `View the story` / `Back` labels as Properties. Those remain explicit Fix Required items before Marketplace handoff. Background and cooking perspective may remain distinct editorial ideas inside `Content`, but they are not separate current Properties.

The expanded content has two short editorial blocks, not a long CV:

1. `Background` — the relevant path into cooking or hospitality, only with supplied facts.
2. `At the stove` — a concrete, approved viewpoint about attention, flavour, time, service, memory, technique, or ingredients.

## Section build checklist

### 1. Opening

- [ ] Use one concise h1 and an optional short lead only when approved.
- [ ] Keep the first viewport calm; do not repeat Home's image-only Hero or About's portrait-led opening.
- [ ] State the page purpose without introducing fictional chef facts.
- [ ] Set a unique Page Title and Meta Description.

### 2. Chef story sequence

- [ ] Render exactly three `ChefStoryRow` instances in a vertical editorial sequence.
- [ ] Choose three distinct portraits from `images/Chefs/portrait/` by narrative fit and source readability, not filename order.
- [ ] Desktop/Tablet: portrait stays left; identity and control stay right; expanded text opens downward within the selected row.
- [ ] Do not turn rows into equal bordered profile cards, avatars, or a three-column team grid.
- [ ] Preserve generous space between profiles without producing unexplained empty bands.
- [ ] Each portrait has specific Alt describing the person and useful visible context, or an explicit empty Alt only where the image is purely decorative.
- [ ] Name is a semantic heading appropriate to the page hierarchy; role is ordinary body/label text, not a heading.

### 3. Expanded story

- [ ] Use two clearly separated, short story blocks: approved background and approved cooking point of view.
- [ ] Expanded content has a readable, narrow measure and grows naturally for long copy.
- [ ] Expanded content does not shift another row into overlap, crop text, or create horizontal overflow.
- [ ] Exactly one row may be open at a time unless a deliberate multi-open requirement is approved.
- [ ] Opening a row changes the control's accessible name and visual state to `Close story` (or approved equivalent).
- [ ] The control exposes its expanded/collapsed state to keyboard and assistive-technology users.
- [ ] No story information is available only on hover.

### 4. Closing

- [x] End the three-profile sequence with the single shared `Reservation Handoff` before Footer; do not create a second Chefs CTA or copy of the handoff.
- [ ] Footer remains the shared Footer and retains existing site-wide routes.
- [ ] Add a contextual link to `/about` only if it clarifies the distinction between individual voices and shared culture.

## Component and interaction contract

- [x] Reuse and inspect the one existing native `ChefStoryRow`; choose `framer-components` as the primary Skill and load only the specific Button, motion, or shared-shell reference the current change actually needs.
- [x] Use the current Portrait, Chef Name, Chef Role, and Content Properties; never create one Variant per chef's content. Portrait Alt and CTA-label Properties remain Fix Required.
- [x] Use eight structural Variants only: Desktop, Tablet, Phone, and Wide Phone `599`, each with Collapsed and Expanded states.
- [ ] The disclosure trigger is a semantic button with an approximately 44px minimum target and a visible Focus state.
- [ ] Use restrained native Framer Variant transitions; no Custom Code, scroll hijacking, or layout-breaking scale effect.
- [ ] Reduced Motion preserves all expanded content and state feedback without dependent movement.
- [ ] After building the Component, return to all three Page Instances and verify their content, image, Alt, state, link, and breakpoint selection independently.

## Responsive and image requirements

- [ ] Verify 320, 390, 810, 1200, and 1440+ widths.
- [ ] Desktop uses deliberate left/right width ownership and controlled text measure.
- [ ] Tablet reduces span complexity while retaining the portrait-left relationship where readable.
- [ ] Phone uses the full reading order: portrait → name/role → button → expanded content.
- [ ] Long names, multi-line roles, long viewpoints, portrait and landscape replacement images, and a missing role do not break the layout.
- [ ] Inspect image source content before layout decisions; adjust crop, focal point, container ratio, or image choice if a person becomes unreadable.
- [ ] Do not repeat the same image elsewhere without a distinct narrative reason.

## Accessibility, SEO, and Marketplace checks

- [ ] One h1; chef names use a logical h2/h3 hierarchy; background/viewpoint labels are not fake headings.
- [ ] Focus order follows the visual reading order; expanded content enters after its own control.
- [ ] Test keyboard open/close for every chef and return focus predictably.
- [ ] Check text contrast, image Alt, visible Focus, and Reduced Motion.
- [ ] Page Title, Meta Description, Open Graph image responsibility, favicon strategy, and Demo status do not present fictional identities as real.
- [ ] Marketplace replacement test: change every name, double every story, remove one role, replace a portrait with portrait/landscape extremes, and ensure the third profile can be hidden without an empty gap.
- [ ] Provide buyer editing guidance for all Component Properties and image replacement.

## Targeted Preview

- [ ] Desktop: Navbar → h1 → first closed profile → first expanded profile → second expanded profile → third profile → shared Reservation Handoff → Footer.
- [ ] Phone: Menu open/close → each profile's long-name case → open/close interaction → long story → shared Reservation Handoff → Footer.
- [ ] Keyboard: Tab through the three disclosure controls, open/close each one, and confirm state/Focus visibility.
- [ ] Test one portrait replacement and one long-copy replacement in a Page Instance.

## Page Done

- [ ] All three chef profiles use verified content or visible Demo placeholders.
- [ ] Component, all Page Instances, links, semantics, image Alt, Focus, Reduced Motion, and responsive behavior pass.
- [ ] Five-width review and targeted Preview pass.
- [ ] Marketplace replacement tests pass.
- [ ] Shared primary navigation is established; synchronize any new build/QA truth only through `STATUS.md`, lasting rationale through `DECISIONS.md`, and the single latest pointer through `RECOVERY.md`.

## 2026-08-14 — Completion audit, component record, and naming

Scope: the existing `/chefs` page and native `ChefStoryRow` component only. This Part does not redesign the page, replace content, move layout, or publish.

### A. Live structure audit and checklist delta

- [x] Read the live page tree, authored Desktop / Tablet / Phone / Wide Phone breakpoints, and all three `ChefStoryRow` instances.
- [x] Read the full `ChefStoryRow` variant tree, Properties, trigger routes, width / padding ownership, image contracts, and direct children outside variants.
- [x] Compare the live result to every relevant existing Chefs checklist item; report `Pass`, `Fix Required`, or `Blocked` with evidence.
- [x] Separate work genuinely completed by the user from items that cannot be asserted without a real Preview, keyboard, content-replacement, or metadata check.

### B. Advanced Design component documentation

- [x] Create `framer/advance-design/aurelia/chef-story-row.md` using the required Advanced Design format.
- [x] Record appropriate / inappropriate use, interaction purpose, full component tree, Properties / Variant / Instance responsibilities, all state routes, and content replacement path.
- [x] Record the exact live Desktop / Tablet / Phone / Wide Phone geometry, root padding, portrait contracts, open-state width ownership, transitions, and any known component-scope exceptions.
- [x] Include exact implementation sequence, validation matrix, failure modes, immutable constraints, and recovery steps.
- [x] End with an exact `ChefStoryRow` Example that can be reproduced from the live component without guessing values.

### C. Layer naming

- [x] Read `framer/basic/standards/layer-naming.md` before canvas changes.
- [x] Rename only unnamed / default / semantically vague Stack or Frame layers in `/chefs` and `ChefStoryRow`; preserve the existing hierarchy, effects, geometry, and authored content.
- [x] Names use the nearest parent context, state the content and layout responsibility, and do not repeat the entire ancestor path.
- [x] Re-read the modified layer tree and confirm no generic `Stack`, `Frame`, `Copy`, or numbered default names remain in the audited scope.

### Part done

- [x] Report checklist deltas and remaining blocked QA to the user.
- [x] Update `PROJECT.md` with the audit result, documentation path, naming result, and any unmodified exceptions.

## Latest Part Result — 2026-08-14

Status: **Partial Pass** — live structure and component system pass; the original checklist still contains content-status, accessibility, metadata, and real-Preview requirements that have not been evidenced in this audit.

Pass:

- `/chefs` has a shared-template page structure, one opening and one profile Section, and exactly three Fill / auto `ChefStoryRow` instances.
- The page now has Desktop 1200px, Tablet 810px, Phone 390px, and Wide Phone 599px breakpoints. Instances select the matching collapsed Variant at each one.
- `ChefStoryRow` now has eight correctly paired structural states: Desktop / Tablet / Phone / Wide Phone, each with Collapsed and Expanded. Every root uses `spring-physics 250 30 1 0s`.
- All live Button routes return to the matching breakpoint pair: `View the story` opens and `Back` returns. Desktop uses Dark / White; the three smaller ranges use Dark Small / White Small.
- Root padding remains component-owned. The audited component has no unnamed/default Frame or Stack layers after renaming `Portrait Column`, `Story Content`, and `Identity Copy`.
- `framer/advance-design/aurelia/chef-story-row.md` now records the exact implementation and recovery contract.
- The previously recorded out-of-variant ids `aCo9KmwGV` and `MLLUuNh30` no longer resolve in the live component read. They were not moved or deleted by this audit.

Fix Required / not yet evidenced:

- The visible opening still says `CHEFS / DEMO` and asks buyers to replace every name and story before publishing. Therefore the Page Done requirement for approved content cannot be marked complete from the live page alone.
- The Component currently exposes one `Content` rich-text Property, not the checklist's separately editable `Background` and `Cooking Perspective`; it also does not expose portrait Alt or open/close CTA labels as Component Properties.
- Framer reports that the variable-bound `Content` Rich Text is missing a `Heading 1` style preset. Current stories are paragraph-only, so this does not change the audited visual result; it must be resolved before buyers are invited to add headings in replacement content.
- The pre-audit planning checklist named only six variants and omitted the live `Wide Phone Collapsed` / `Wide Phone Expanded` pair. That wording is now archived; all current QA and documentation include 599px Wide Phone.
- No evidence was produced in this Part for 320px / 1440px+ external Preview, keyboard Focus order, screen-reader state, Reduced Motion, Page Title / Meta Description / OG, individual portrait Alt, long-name / missing-role / replacement-image stress, or Marketplace replacement tests.

Blocked:

- Approval status for the current identities, roles and long stories cannot be determined from the live canvas. The current on-page Demo notice explicitly preserves them as buyer-editable demonstration material.

## Historical implementation notes

The dated revisions below preserve implementation evidence. They do not create a second current Result or Recovery checkpoint; use the Latest Part Result above and [`../../RECOVERY.md`](../../RECOVERY.md) for re-entry. The superseded earlier build checkpoint, including session `3`, remains verbatim in [`../../HISTORY.md`](../../HISTORY.md#superseded-chefs-build-checkpoint-verbatim).

### Responsive revision — 2026-08-13

Partial Pass:

- Desktop, Tablet, and Phone page roots now use natural height; the outer Chefs Content and its full-bleed white sections use 100% width without `max-width`.
- The page-wide black side bands reported in wide Preview were addressed by moving width limits into inner opening/profile wrappers only.
- Tablet now uses its dedicated component variant with instances filling the 754px inner list; Phone keeps its dedicated variant and the original 350px instance contract.
- Phone portrait frames remain 350 × 440px in both collapsed and expanded states with unchanged image fill and clipping.

Still required:

- Real external Preview at 320px and 1440px+, plus live keyboard, focus, motion, long-content, and image-replacement checks.

### Component padding revision — 2026-08-13

Pass:

- `ChefStoryRow` now owns its breakpoint-specific horizontal padding at the component root: 32px Desktop, 28px Tablet, and 20px Phone, in both collapsed and expanded states.
- `Chef Profiles Section` now provides only vertical spacing. Its list widths and Page Instances were expanded to the full component contract (1164px Desktop, 810px Tablet, 390px Phone), while the Phone portrait itself remains the original 350 × 440px child inside the component.

Still required:

- Inspect the open/close state in real Preview after editing a component property, especially with long names and long stories.

### Tablet expanded-story refinement — 2026-08-14

Pass:

- Desktop and Phone variants were read only and left unchanged.
- Tablet Expanded now mirrors Desktop’s close affordance: the existing action returns to Tablet Collapsed, while its shared button uses the white `Back` presentation.
- The Tablet story content remains bound at the Paragraph level to `Type/Story`. That shared style’s Medium breakpoint is 12px (Desktop 14px; Phone 13px), so no separate `M` style is required.
- One targeted Tablet Expanded component screenshot was visually reviewed: the portrait, name, 12px story text, and Back button are readable with no observed clipping.

Known exception / Fix Required outside this refinement:

- During this Tablet refinement, Framer reported two overlapping direct children of the `ChefStoryRow` component scope (`aCo9KmwGV` and `MLLUuNh30`). They were not inside the Desktop, Tablet, or Phone variants and were not moved or deleted because this Tablet-only request explicitly locked Desktop and Phone. The later completion audit above records that both ids no longer resolved; do not restore or remove anything from this historical note.
