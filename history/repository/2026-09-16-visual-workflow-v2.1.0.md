# Website-lab Visual Workflow Improvement — v2.1.0

## Status

- Change type: repository knowledge-architecture improvement
- Base version: `v2.0.0` — user-confirmed last knowledge-base change
- Current version: `v2.1.0`
- Current status: Complete
- Scope: repository knowledge and project-state correction only; no Framer Canvas repair or publication
- Evidence sources:
  - User feedback in the current task, 2026-09-16
  - Referenced `Submit Roofing-2` task, read through Codex thread evidence
  - Referenced `重构 website-lab 知识架构` task, read through Codex thread evidence
  - Current Website-lab Router, Skills, Basic references, Checklist, validator, Summit Roofing manifest and page contracts

This file is the single request checklist and migration record for this change. It must not become a second Router, design handbook, or current project-status owner. After completion it remains under `history/repository/` as evidence of the v2.0.0 → v2.1.0 migration.

## User requirements — verbatim

### Design-workflow problem report

```text
in that context I thought the workflow is strange.Codex finished the work quickly and the layout is copied from another page. He also forgot some design rule, such as color 搭配, layout and so on. What's more, there is lots of photo materials in the content library but he didn't use or just use the photos which have been used in other page.When I asked him to 修改 a section and use different layout, what he made was terrible which was actually different but the layout rule and 审美 were ignored completely.read the problems ine by one and 结合what you have found and the problems I said ,plan to improve the knowledge base
```

### Repository-change and versioning request

```text
Our goal is improve the Website-lab and the work this time seems little heavy. So I think first you' better write down the plan in markdown file and follow the checklist to do the work. No long ago, I also made a big change of Website-lab\[@重构 website-lab 知识架构\]\(thread://01a0036d-0cbc-77e3-b1df-e246e220d46b?hostId=local\). More detailed things can be found in the conversation and I mean the change this time should follow and respect what we emphasize before, like the workflow and the route. One more thing, I want to record the version of the base in the README and the last change is v2.0.0
```

The backslashes above only prevent the embedded task mention from becoming an active repository link; the rendered wording remains unchanged.

## Prior v2 architecture invariants to preserve

The previous refactor established the following principles. This migration must strengthen them rather than reintroduce a large preloaded handbook.

- One canonical owner for each rule; summaries may link but must not duplicate detailed knowledge.
- Progressive disclosure for design and implementation knowledge.
- A small, mandatory control plane for routing, gates and observable receipts.
- Domain scan before selecting the primary repository Skill.
- Compile applicable knowledge into a low-ambiguity request contract before writing.
- Use the same contract for symmetric post-implementation verification.
- Router owns selection; Skill owns reasoning procedure; workflow owns persistence; QA owns evaluation; validator owns machine-checkable structure.
- Do not add a new Skill when an existing Skill already owns the responsibility.
- Do not move the full Checklist or Baseline into the pre-build path.
- Preserve exact evidence, current/history boundaries and unrelated dirty worktree changes.
- After Router or Skill changes, run strict validation and realistic forward regression tests.

## Verified failure model

The observed failure is a routing and enforcement gap, not an absence of all relevant design knowledge.

1. The build path optimized for rapid structural completion.
2. New-page work did not compile a page-specific visual direction before Canvas writing.
3. The Repair & Maintenance contract defined content order but not a distinct visual identity relative to Services.
4. `distinct` was interpreted as different text rather than different composition.
5. Existing palette tokens were reused without designing page-specific colour roles or colour rhythm.
6. Layout verification emphasized Stack/Grid, width ownership and breakpoints, but not proportion, focal hierarchy, balance or aesthetic coherence.
7. The project contains 38 WebP image files, but the Repair page reused the Services aerial image instead of its allocated `roofer-ledge.webp`, `roof-work.webp` and `roof-detail.webp` narrative set.
8. `image-workflow.md` already contains cross-page reuse control, but its routing can be bypassed when an Agent reuses an existing Canvas image without first reviewing local assets.
9. A request for a “different layout” had no compiled Preserve / Transform / Avoid contract, allowing arbitrary difference that broke the established visual language.
10. Clean Framer diagnostics and structural readback were reported as strong completion evidence without a full-page comparative visual review.
11. The visual budget was interpreted as permission to defer necessary composition review rather than to choose one efficient piece of visual evidence.
12. The strict repository validator passed because it checks knowledge structure, not whether a page-level visual contract exists or visual evidence supports `Pass`.

## Architectural decision

### Modify, do not create a new Skill

Create one new reusable contract type inside the existing design and Framer workflow:

`Visual Direction Contract`

Canonical responsibility remains distributed by owner:

| Responsibility | Canonical owner | Role in v2.1.0 |
|---|---|---|
| Visual interpretation and contract compilation | `.agents/skills/design-taste/SKILL.md` | Define Design Read, Preserve / Transform / Avoid, sibling differentiation, composition and aesthetic acceptance |
| Task selection and phase handoff | `framer/README.md` | Route new Page, major Section redesign and “different layout” work through visual-direction compilation before implementation |
| Contract persistence and confirmation | `framer/basic/workflows/change-control.md` | Store the contract in the active request Checklist and enforce confirmation when material design direction is newly derived |
| Page build sequence | `framer/basic/workflows/build-checklist.md` | Prevent Canvas writing until the visual contract and asset plan are Ready |
| Layout implementation | `.agents/skills/framer-layout-responsive/SKILL.md` | Consume the Ready visual contract while resolving width, Stack/Grid and breakpoint ownership |
| Asset selection, reuse and crop | `framer/basic/workflows/image-workflow.md` | Own inventory, narrative-role selection, cross-page reuse reason and responsive crop evidence |
| Page and request checklist schema | `framer/checklist.md` | Require page-specific composition, colour, imagery and evidence fields without duplicating design rules |
| Post-build evaluation | `.agents/skills/framer-qa/SKILL.md` and `framer/basic/workflows/preflight-audit.md` | Reverse-check the same visual contract and classify structural and visual status separately |
| Project-specific visual identity and asset usage | `content-library/<project>/PROJECT.md` via `content-library/project-manifest-template.md` | Record current page identity, asset allocation and reuse state |
| Machine-checkable contract integrity | `validate_repository.py` and narrow validation configuration | Reject incomplete persisted contracts and false `Pass`; do not attempt to score taste |
| Repository base version | Root `README.md` | Record base/current version and link this migration record; do not create a parallel changelog system |

## Visual Direction Contract — proposed schema

The contract applies to a new Page, a substantial Section redesign, multi-page differentiation, or a request whose main requirement is “use a different layout.” It does not apply to mechanical rename, link, copy-only, metadata or narrow breakpoint fixes.

Contract status: `Draft / Ready / Pass / Blocked`

| Concern | Required decision | Governing source | Implementation owner | Visual proof |
|---|---|---|---|---|
| Design Read | Page kind, audience, conversion goal and project-specific visual language | User / PROJECT / approved reference | Design direction | Planned before writing; final page review after writing |
| Preserve | Typography, palette tokens, geometry, spacing logic, image treatment and interaction character that must remain | PROJECT / current Canvas evidence | Shared system or page | Comparison against current approved language |
| Transform | Topology, proportion, alignment, density, media sequence or hierarchy intentionally changed | User / page purpose | Page / Section | Target Section or full-page screenshot |
| Avoid | Copied sibling pattern, generic default or arbitrary novelty prohibited in this scope | User / sibling audit | Page / Section | Comparative review |
| Sibling-page delta | Hero paradigm, section order, layout families, colour-block rhythm, repeated patterns and CTA composition | Current sibling pages | Page | Side-by-side or compiled comparison |
| Section composition | Purpose, layout family, focal point, content density and transition for each Section | Page narrative | Section | Full-page composition review |
| Colour rhythm | Background, text, accent, image relationship and transition per Section | PROJECT palette | Page / Section | Full-page composition review and contrast readback |
| Asset map | Selected image, existing use, narrative role, reuse decision, crop/focal plan and breakpoint behavior | PROJECT assets / image workflow | Page / image owner | Contact sheet or targeted image evidence plus Canvas readback |
| Responsive transformation | Content priority, order, crop, hierarchy and touch behavior by breakpoint | Page contract | Page / Component owner | Desktop, Tablet and Phone evidence |
| Completion evidence | Structural readback plus visual evidence that can actually prove the design claims | QA workflow | QA | `Pass` or reasoned `Blocked`; never command success alone |

## Implementation checklist

### Phase 0 — Protect and baseline

- [x] Re-read `AGENTS.md`, `knowledge-maintenance`, `skill-creator` and this confirmed checklist before editing.
- [x] Capture `git status` and the scoped diff; preserve the existing uncommitted `content-library/summit-roofing/PROJECT.md` changes.
- [x] Record the current relevant Router, Skill, workflow and validator owners.
- [x] Confirm no Framer Canvas connection or write is needed for this repository-only migration.
- [x] Treat `.knowledge-validation.json` `version` as validator/config schema unless evidence proves it is the knowledge-base release version; do not silently conflate it with `v2.0.0`.

### Phase 1 — Repository version and migration identity

- [x] Modify root `README.md` with a concise Knowledge Base Version section.
- [x] Record base version `v2.0.0` as the user-confirmed previous architecture release.
- [x] Record target/current version `v2.1.0` only after all v2.1.0 checks pass.
- [x] Link this migration record instead of copying a detailed changelog into README.
- [x] Keep ordinary file history in Git; do not create per-version directory snapshots.

### Phase 2 — Compile visual direction before implementation

- [x] Extend `design-taste/SKILL.md` with the canonical Visual Direction Contract procedure.
- [x] Define precise triggers and non-triggers so ordinary mechanical fixes do not load design planning.
- [x] Add the coherent-difference rule: preserve the approved visual language while transforming composition intentionally.
- [x] Require a one-line Design Read and explicit Preserve / Transform / Avoid decisions.
- [x] Require sibling-page comparison for new pages in an existing multi-page site.
- [x] Keep detailed schemas in the existing relevant reference or workflow when they would make `SKILL.md` too large.
- [x] Keep `agents/openai.yaml` synchronized only if the Skill description or invocation metadata changes.

### Phase 3 — Route and persist the contract

- [x] Update `framer/README.md` Domain Scan so new Page composition, major Section redesign, multi-page differentiation and “different layout” requests compile visual direction before the implementation Skill is selected.
- [x] Preserve the rule that only one primary Framer implementation Skill owns Canvas structure at a time.
- [x] Update `change-control.md` so a request Checklist stores the Visual Direction Contract without creating a second design log.
- [x] Clarify confirmation behavior: explicit authorization to build does not require redundant approval, but material Agent-derived visual choices must be surfaced before writing; genuine design divergence pauses for confirmation.
- [x] Add a concise visible visual-contract receipt before implementation.

### Phase 4 — Build workflow and page-contract schema

- [x] Add a pre-writing Design Preflight Gate to `build-checklist.md`.
- [x] Require page purpose, visual memory point, composition map, colour rhythm and asset map before bulk Section creation.
- [x] Require one representative visual Section to be checked before propagating the same language through a whole page; this may remain internal when it does not change approved direction.
- [x] Update `framer/checklist.md` page-file requirements with a Section composition table.
- [x] Require a sibling-page delta for existing multi-page projects.
- [x] Prohibit generic page contracts that describe only `Hero → content → process → CTA` without page-specific composition responsibility.
- [x] Keep detailed design judgment out of the Checklist; link to the canonical contract owner.

### Phase 5 — Asset discovery, allocation and reuse

- [x] Extend `image-workflow.md` trigger from “before viewing” to before selecting, reusing, uploading, placing, cropping or visually reviewing an image.
- [x] Preserve the visual-budget and stop rules.
- [x] Clarify that the budget controls capture count, not whether visual QA occurs.
- [x] Add a project asset-usage ledger contract: asset, narrative qualities, approved role, current use, reuse reason, crop/focal notes and status.
- [x] Require an explicit reason when an existing sibling-page image is reused.
- [x] Require every allocated image to be implemented, deliberately reassigned or marked `Blocked`; silent omission fails the contract.
- [x] Add the minimum project-facing fields to `project-manifest-template.md` without turning PROJECT into a duplicated image manual.

### Phase 6 — Layout, colour and aesthetic preservation

- [x] Update `framer-layout-responsive/SKILL.md` to consume, not reinvent, a Ready Visual Direction Contract.
- [x] For “different layout,” require preserved system invariants and named transformation dimensions.
- [x] Require comparison with adjacent Sections and relevant sibling pages before changing composition.
- [x] Add page-level colour rhythm as an implementation input while leaving token definitions in the project Style System.
- [x] Ensure Tablet and Phone transform the approved hierarchy rather than mechanically collapse Desktop.
- [x] Do not turn optional anti-template heuristics into universal aesthetic bans.

### Phase 7 — Symmetric visual QA and status

- [x] Extend `framer-qa/SKILL.md` to reverse-check the same Visual Direction Contract.
- [x] Add comparative checks for masthead paradigm, layout-family sequence, colour-block rhythm, image reuse, heading/body proportion, whitespace, repeated process treatment and CTA composition.
- [x] Extend `preflight-audit.md` with a focused visual-composition and cross-page differentiation section.
- [x] Require one efficient full-page or compiled Desktop/Phone visual review for Page-level aesthetic claims.
- [x] State that a target Section screenshot cannot prove whole-page rhythm.
- [x] Separate `Structural status` and `Visual status`; overall `Pass` requires both.
- [x] Treat unavailable required visual evidence as `Blocked` or `Fix Required`, not implicit success.
- [x] Preserve the evidence ladder and avoid repeated screenshots of the same state.

### Phase 8 — Summit Roofing regression correction

- [x] Use the observed Summit Roofing failure as project evidence, not as a universal style template.
- [x] Carefully merge the current dirty `PROJECT.md`; do not overwrite unrelated prior work.
- [x] Correct Repair & Maintenance to `Fix Required` for visual duplication and asset-contract mismatch while preserving structurally verified facts.
- [x] Record that the Services aerial image was reused and the allocated Repair image set was not fulfilled.
- [x] Do not repair the live Canvas in this migration.
- [x] Do not advance to Roof Replacement in the project record until the Repair visual contract is corrected and later verified.

### Phase 9 — Validator and regression tests

- [x] Extend the validator only for machine-checkable contract integrity.
- [x] Check required Visual Direction Contract columns, valid status and non-empty owners/sources where a persisted contract is present.
- [x] Reject `Pass` when visual proof remains `Planned`, absent or explicitly unperformed.
- [x] Do not attempt to machine-score beauty, originality or colour taste.
- [x] Preserve existing Component Requirement Contract checks and canonical-owner validations.
- [x] Add a valid `Ready` fixture that passes.
- [x] Add invalid fixtures for missing sibling delta, missing asset reuse decision and false visual `Pass`.
- [x] Run repository strict validation.
- [x] Run `git diff --check`.
- [x] Run Skill validation available in the current environment without installing unapproved dependencies.
- [x] Forward-test at least two fresh realistic prompts without leaking the expected answer:
  - Build a new service-detail page in an existing multi-page project.
  - Make an existing Section use a different layout while preserving the project language.
- [x] Confirm small copy/link/rename fixes do not trigger the heavy visual contract.

### Phase 10 — Final preservation and migration report

- [x] Review the scoped diff for duplicated rules and accidental expansion.
- [x] Confirm each detailed rule has one canonical owner and every other location only routes, persists, consumes or verifies it.
- [x] Confirm README version reports `v2.1.0` only after successful validation.
- [x] Update this file from `Awaiting user confirmation` to `Complete` and record final validation evidence.
- [x] Provide a migration map: source responsibility, destination, preservation evidence, Router updates, validator results and retained uncertainty.
- [x] Report that no Framer Canvas was modified.

## Forward regression results

These fresh prompts were traced through the active Router and canonical owners after implementation:

| Prompt | Observed route | Result |
|---|---|---|
| “Build a roof-repair service-detail page for this existing multi-page Framer project, using the project photo library.” | `framer/README.md` → `design-taste` Visual Direction Contract → asset ledger / `image-workflow.md` → one primary implementation Skill after `Ready` → symmetric QA | Pass: sibling comparison, colour rhythm, asset roles and structural/visual proof are mandatory before Page Pass. |
| “Change this assessment Section to a different layout, but keep the site’s existing visual language.” | existing-project audit → Preserve / Transform / Avoid contract → `change-control.md` constraint lock for a later revision → `framer-layout-responsive` consumes the Ready contract | Pass: structural difference alone cannot satisfy the request; preserved system and named transformation dimensions are required. |
| “Change the CTA label and fix its link.” | mechanical-fix non-trigger → targeted primary Skill/readback only | Pass: the Visual Direction Contract is explicitly skipped, preserving the lightweight path. |

Validator regression fixtures also pass for one valid `Ready` contract and fail as expected for a missing sibling delta, a blank asset reuse decision and a false visual `Pass` with planned-only evidence.

## Final validation evidence

- Strict knowledge validator: Pass with 0 errors and 0 warnings; three documented baseline notes remain.
- Visual contract regression tests: four tests passed.
- `git diff --check`: Pass.
- Repository Skill/frontmatter/metadata validation: Pass through the strict validator. The optional system `quick_validate.py` was attempted but could not run because PyYAML is not installed; no dependency was installed or introduced.
- Preservation review: no Markdown deletion, no immutable archive change, no new Skill and no Framer Canvas modification.

## Out of scope

- Repairing or redesigning the live Summit Roofing Canvas.
- Publishing any Framer site.
- Creating a new design Skill or a parallel all-purpose design handbook.
- Moving the entire Baseline or Checklist into pre-build context.
- Rewriting unrelated project knowledge.
- Converting project-specific visual preferences into universal rules.
- Committing or pushing repository changes unless separately requested.

## Acceptance criteria

This migration is complete only when:

1. The v2.0.0 ownership and progressive-disclosure architecture remains intact.
2. New Page and major visual redesign tasks cannot reach Canvas writing without a compiled visual direction and asset plan.
3. “Different layout” produces a Preserve / Transform / Avoid contract rather than arbitrary novelty.
4. Cross-page image reuse and ignored allocated assets become explicit decisions.
5. Structural diagnostics cannot substitute for visual proof.
6. A page cannot reach overall `Pass` while its required visual evidence is missing.
7. Small mechanical changes remain lightweight.
8. Strict validation and all scoped regression tests pass.
9. Root README records the successful knowledge-base release as `v2.1.0`, with `v2.0.0` identified as its base.
10. Existing uncommitted project work remains preserved.

## Confirmation gate

Confirmation received: the user replied `start` on 2026-09-16. That confirmation authorised the repository-only migration described above; it did not authorise live Framer Canvas repair, publishing, commit or push.
