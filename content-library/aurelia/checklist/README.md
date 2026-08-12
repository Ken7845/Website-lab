# AURELIA Page Checklist Index

These files turn the approved page plan in `../PROJECT.md` into page-level Framer execution contracts.

## Status vocabulary

- `To do`: approved scope, no completed implementation claim.
- `In progress`: the current page is being built vertically by Section.
- `Fix Required`: a required check failed and must be repaired before continuing.
- `Blocked`: a real fact, asset, service, permission, or destination is missing.
- `Pass`: the current Part or Page passed the required readback and Preview.

## Mandatory workflow

For every Section, Component, interaction, breakpoint, CMS batch, Form state, Navbar/Footer change, or Page:

```text
Read PROJECT.md and this page checklist
→ declare current Part and exclusions
→ complete content, styles, structure, links, semantics, responsive, and interaction
→ reopen Website-lab/framer/checklist.md
→ route to every applicable checklist section
→ targeted readback and one necessary Preview path
→ mark Pass / Fix Required / Blocked
→ batch-fix the current class of problems
→ recheck only the affected scope
→ update this file and PROJECT.md
→ start the next Part
```

Do not mark a Page complete because its Desktop layout looks finished. A Page reaches `Pass` only after the Page Done and Marketplace checks in its own file are complete.

## Shared references

- Project truth and approved plan: `../PROJECT.md`
- Repository rules: `../../../AGENTS.md`
- Framer routing: `../../../framer/basic/README.md`
- Website baseline: `../../../framer/basic/standards/website-baseline.md`
- Marketplace requirements: `../../../framer/basic/standards/marketplace-guidelines.md`
- Layer naming: `../../../framer/basic/standards/layer-naming.md`
- Build order: `../../../framer/basic/workflows/build-checklist.md`
- Preflight: `../../../framer/basic/workflows/preflight-audit.md`
- Image workflow: `../../../framer/basic/workflows/image-workflow.md`
- Pattern decisions: `../../../framer/basic/patterns/pattern-recipes.md`
- Navbar/Footer: `../../../framer/basic/patterns/navbar-footer.md`
- Buttons: `../../../framer/basic/patterns/buttons.md`
- Mandatory Part checklist: `../../../framer/checklist.md`

## Page files

| Page | Path | File | Current status |
|---|---|---|---|
| Home | `/` | [home.md](./home.md) | Built; QA incomplete |
| Menu | `/menu` | [menu.md](./menu.md) | To do |
| Private Dining | `/private-dining` | [private-dining.md](./private-dining.md) | To do; facts partly blocked |
| About | `/about` | [about.md](./about.md) | To do; biography blocked |
| Reserve | `/reserve` | [reserve.md](./reserve.md) | To do; integration blocked |

## Shared foundation gate

Complete before the first supporting page is marked Done:

- [ ] Build or verify one shared Layout Template containing Navbar, Content Placeholder, and Footer.
- [ ] Keep Navbar and Footer as shared Components, not page copies.
- [ ] Change primary navigation to existing pages only; do not link to a page before its structure and destination are real.
- [ ] Preserve Desktop, Tablet, Phone, and Phone Open navigation behavior.
- [ ] Logo links to `/`.
- [ ] `Reserve a seat` uses one consistent intent and a real destination when available.
- [ ] Recheck live Body and Button text sizes before propagating them to new pages.
- [ ] Establish visible Focus treatment and Reduced Motion behavior.
- [ ] Preserve the current color tokens and sharp shape system.
- [ ] Confirm favicon, Open Graph strategy, Demo statement, licensing, and editing-instruction ownership.

## Page completion record format

Append or update the following block at the end of the active page file after each completed Part:

```markdown
## Latest Part Result

Scope: Section / Component / Page
Status: Pass / Fix Required / Blocked

Pass:
- ...

Fix Required:
- ...

Blocked:
- ...

Verified widths:
- ...

Verified paths:
- ...

Shared components affected:
- ...

Recovery state:
- Session:
- Page:
- Last successful change:
- Next Part:
```
