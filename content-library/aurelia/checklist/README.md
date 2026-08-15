# AURELIA Page Checklist Index

These files are page-level Framer execution contracts. Start with the small current manifest, then read only the Checklist for the page or shared system in scope.

## Status vocabulary

- `To do`: approved scope, no completed implementation claim.
- `In progress`: the current page is being built vertically by Section.
- `Fix Required`: a required check failed and must be repaired before continuing.
- `Blocked`: a real fact, asset, service, permission, or destination is missing.
- `Pass`: the current Part or Page passed the required readback and Preview.

## Mandatory workflow

For every Section, Component, interaction, breakpoint, CMS batch, Form state, Navbar/Footer change, or Page:

```text
Read PROJECT.md and only the relevant page checklist
→ declare current Part and exclusions
→ complete content, styles, structure, links, semantics, responsive, and interaction
→ reopen Website-lab/framer/checklist.md
→ route to every applicable checklist section
→ targeted readback and one necessary Preview path
→ mark Pass / Fix Required / Blocked
→ batch-fix the current class of problems
→ recheck only the affected scope
→ update the page record and the current owner: PROJECT / STATUS / DECISIONS / RECOVERY
→ start the next Part
```

Do not mark a Page complete because its Desktop layout looks finished. A Page reaches `Pass` only after the Page Done and Marketplace checks in its own file are complete.

## Project and shared references

- Current project manifest: [PROJECT.md](../PROJECT.md)
- Current Build / QA state: [STATUS.md](../STATUS.md)
- Active decisions: [DECISIONS.md](../DECISIONS.md)
- Current recovery pointer: [RECOVERY.md](../RECOVERY.md)
- Retired directions and implementation history: [HISTORY.md](../HISTORY.md), read only when needed
- Verbatim pre-migration snapshot: [project-pre-migration-2026-08-15.md](../history/project-pre-migration-2026-08-15.md)
- Repository rules: `../../../AGENTS.md`
- Framer routing: `../../../framer/README.md`
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
| Home | `/` | [home.md](./home.md) | Built; Fix Required full regression and shared-system sign-off |
| Menu | `/menu` | [menu.md](./menu.md) | Requested scope built; Partial Pass; full-page QA remains |
| About | `/about` | [about.md](./about/about.md) | Demo culture structure built; Partial Pass; verified biography blocked |
| Chefs | `/chefs` | [chefs.md](./chefs/chefs.md) | Demo profiles and responsive component built; Partial Pass; content and final QA blocked |
| Reserve | `/reserve` | [reserve.md](./reserve.md) | Native request form built; Partial Pass; live submission blocked |
| Shared shell & reservation handoff | Shared components + all five pages; Handoff on `/`, `/menu`, `/chefs` | [shared-shell-and-reservation-handoff.md](./shared-shell-and-reservation-handoff.md) | Implemented; Fix Required visual/Phone confirmation |

## Retired and repository-level records

| Record | File | Status |
|---|---|---|
| Private Dining page plan | [private-dining.md](./private-dining.md) | Retired; `/private-dining` is not current and must not be created or linked |
| Progressive-disclosure migration | [2026-08-15-progressive-disclosure-migration.md](./knowledge-architecture/2026-08-15-progressive-disclosure-migration.md) | Complete; repository validation passed; no Canvas changes |

## Shared foundation gate

Complete before the first supporting page is marked Done:

- [x] One shared Layout Template contains Navbar, Content Placeholder, and Footer; final visual regression remains open.
- [x] Navbar and Footer remain shared Components, not page copies.
- [x] Primary navigation links only the five existing current pages: Home, Menu, About, Chefs, and Reserve.
- [x] Desktop, Tablet, Phone, and Phone Open navigation structures are documented; final Phone interaction/visual sign-off remains open.
- [x] Logo links to `/`.
- [x] `Reserve a seat` uses one consistent intent and routes to `/reserve`; production form handling remains Blocked.
- [ ] Recheck live Body and Button text sizes before propagating them to new pages.
- [ ] Establish visible Focus treatment and Reduced Motion behavior.
- [x] Preserve the current color tokens and sharp shape system.
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

Recovery:
- Canonical current pointer: `../RECOVERY.md`
- This Part result date:
- Historical evidence link (only when needed):
```

Do not append a second current Session / Page / Next Part diary here. Replace the single checkpoint in `../RECOVERY.md`; completed implementation evidence can remain in the request-specific record or `../HISTORY.md`.
