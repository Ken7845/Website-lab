---
name: design-taste
description: "Infer, critique, or establish the visual direction of marketing sites, portfolios, editorial sites, and design-led pages without falling into generic template patterns. Use for greenfield art direction, redesign audits, visual-language decisions, layout diversity, design critique, or anti-slop review. Do not trigger for a purely mechanical Framer breakpoint, component, link, or QA fix whose approved project language is already clear."
---

# Design Taste

Use design judgment as a context-sensitive lens, not as a replacement design system.

## Authority order

Apply this order whenever sources disagree:

1. The user's current explicit direction.
2. The actual current implementation and approved project language.
3. Approved project facts, content, and active decisions.
4. Universal safety and accessibility requirements.
5. This Skill's general guidance.
6. Inspiration and archived history.

Existing approved choices may legitimately include Inter, a custom cursor, a fixed light editorial system, or a deliberate dark transition. Never overturn them merely because a generic preference in the archived source says otherwise.

## Design read

Before proposing a direction:

1. Identify page kind, audience, conversion goal, brand assets, reference signals, and quiet constraints.
2. Classify the task as greenfield, preserve-mode redesign, or approved overhaul.
3. For an existing project, audit the actual implementation before choosing any aesthetic move. Extract its typography, palette, spacing rhythm, image behavior, recurring compositions, interaction language, and intentional exceptions.
4. State one short design read. Do not force numeric dials when the existing project already provides a clearer language; use dials only as a discussion aid.
5. Separate hard constraints from design guidance. Accessibility, truthful content, valid interaction, and explicit scope are hard constraints. Editorial, restrained, asymmetric, cinematic, playful, or minimal are guidance that must be interpreted in context.

If a request changes only one Desktop composition, treat it as Desktop intent. Independently design Tablet and Phone behavior from content priority, available width, touch use, and the project's existing patterns.

## Existing-project audit

Before creating or replacing a section:

- Inspect the page and shared components for the same function or CTA intent.
- Decide explicitly: `Add`, `Reuse`, `Modify`, or `No-op`.
- Reconcile documentation against the implementation; the current implementation wins when historical notes disagree.
- Preserve signature patterns unless the user approves a new direction.
- Prefer the smallest coherent change that improves the page as a whole, not a literal patch to one symptom.

## Anti-default judgment

- Avoid automatic AI-purple gradients, generic glass panels, centered dark-mesh heroes, equal three-card rows, decorative micro-labels, fake metrics, filler testimonials, and motion with no communicative purpose.
- Do not convert these cautions into universal bans. A pattern is valid when brand context, content, and the existing system justify it.
- Vary section composition through narrative needs, not novelty quotas.
- Let real content and images determine density and hierarchy; never invent operational facts or fake precision to make a layout feel complete.
- Motivate motion through hierarchy, storytelling, feedback, or state change.

## Universal requirements

These do not yield to taste:

- Maintain readable contrast, keyboard access, visible focus, semantic order, truthful content, and reduced-motion alternatives.
- Do not hide required information behind hover-only behavior on touch devices.
- Do not introduce paid dependencies, Custom Code, destructive content changes, or scope expansion without approval.

## Load references only when needed

- For anti-template patterns and copy/visual tells, read [references/anti-slop-rules.md](references/anti-slop-rules.md), then only the named sections of the archive.
- For React, Next.js, Tailwind, design-system packages, dark-mode implementation, or browser performance, read [references/frontend-implementation.md](references/frontend-implementation.md).
- For Motion, GSAP, scroll choreography, and web animation code, read [references/motion-reference.md](references/motion-reference.md).
- The untouched upstream source is [references/original-design-taste.md](references/original-design-taste.md). It is provenance, not an always-loaded rulebook. Never preload it in full for ordinary Framer work.

For Framer implementation, switch to the one primary Framer Skill matching the work. Return to design-taste only when visual judgment or direction is actually at issue.
