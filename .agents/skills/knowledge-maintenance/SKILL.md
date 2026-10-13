---
name: knowledge-maintenance
description: "Audit conflicts and routes; classify, update, move, archive, or validate knowledge in the Website-lab repository without damaging progressive disclosure or losing precise evidence. Use when changing AGENTS/README routers, project current-state documents, Framer Basic or Advanced Design references, repository Skills, history/recovery ownership, or when deduplicating and migrating knowledge. Do not use for an ordinary website or Canvas edit unless the task also asks to preserve a reusable lesson in the knowledge base."
---

# Knowledge Maintenance

Keep the repository's read path small while preserving the full value of its knowledge.

## Start safely

1. Read [AGENTS.md](../../../AGENTS.md) and inspect `git status` before editing.
2. Name the exact knowledge being added or changed and its evidence source.
3. Do not connect to or modify a Framer Canvas for a repository-only knowledge task.
4. Protect pre-existing worktree changes. Never reset or overwrite them.
5. Apply `MOVE BEFORE DELETE`: preserve exact content before removing an old owner.
6. Declare Audit only or Repair. Audit-only work does not repair targets; already-authorized knowledge repairs proceed without a new construction Checklist gate.

## Classify the owner

| Knowledge | Canonical owner |
|---|---|
| Current project identity, sitemap, visual system, components, constraints | `content-library/<project>/PROJECT.md` |
| Current Build / QA truth | `STATUS.md` or the small project's current-status section |
| Page scope and active request contract | Project checklist index → one page owner / one active request |
| A lasting approved why-decision | `DECISIONS.md` |
| One latest continuation checkpoint | `RECOVERY.md` |
| Retired direction, closed Prompt, old Session, superseded implementation | `HISTORY.md` / `history/` |
| Cross-project, platform-general Framer standard, pattern, or workflow | `framer/basic/` |
| Fully evidenced project-derived advanced component or interaction | `framer/advance-design/<project>/` |
| Reusable task-selection and reasoning method | `.agents/skills/` |

Do not place one fact in two current owners. A link or short summary may point to the owner; it must not become a second detailed copy.

## Search before creating

1. Use `rg` to find the concept, component name, bug symptom, exact parameter, and likely synonyms.
2. Inspect the nearest Router and the existing canonical document.
3. Choose `Update`, `Extend`, `Move`, `Archive`, or `No-op` before `Create`.
4. Create a new document only when the existing owner has a genuinely different responsibility.

## Review conflicts and routes

For a router, migration, current-state repair, or repository audit, use [maintenance-review.md](references/maintenance-review.md). Compare authority, trigger, mode, owner, required reads, write permission, completion evidence, and recovery for the affected routes. A strict validator PASS is a structural check, not proof of semantic agreement.

## Preserve evidence

- Keep exact values, ids, state names, breakpoints, dimensions, formulas, transition parameters, failure causes, repair order, tool/session caveats, and validation limits.
- Record provenance: project, date or version, implementation scope, and evidence type.
- Label claims as `Verified`, `Inference`, `Unverified`, `Legacy`, or `Retired` where ambiguity matters.
- Never turn one project's exact parameter into a universal default.
- Preserve uncertain but unique material in Reference or History instead of deleting it.

## Write Basic and Advanced knowledge

For Framer Basic, keep the rule platform-general and state its boundary, decision logic, failure mode, repair path, and verification method. Put the detail in the existing standards/patterns/workflows file and update only `framer/basic/README.md` when discovery changes.

For Advanced Design, include enough evidence for another Agent to reproduce or safely adapt the pattern:

- appropriate and inappropriate use;
- interaction or narrative goal;
- exact component tree and Property / Variant / Instance responsibilities;
- geometry, coordinate system, clipping, width/height ownership, and state routes;
- independent Desktop, Tablet, Phone, and project-specific breakpoint contracts;
- ordered implementation, replacement path, validation matrix, failure modes, and repair path;
- one exact verified Example.

If any part is missing, mark the document `Reference` or `Incomplete`; do not claim exact reproducibility. Register it in `framer/advance-design/README.md` as Canonical, Reference, or Legacy.

## Change a Skill or Router

- Keep Skill descriptions explicit about both triggers and non-triggers.
- Keep `SKILL.md` procedural and concise; detailed knowledge belongs in conditional references.
- Keep `agents/openai.yaml` synchronized and free of placeholders.
- Do not add a Skill merely for one component or one parameter.
- After a Router or Skill change, run the validator and forward-test a realistic request without giving the evaluator the intended answer. Use an independent subagent in an isolated temporary workspace for substantial routing repairs when delegation is available; restrict it to read-only repository sources and temporary artifacts. Record its actual choice, evidence and any resulting repair.

## Validate before completion

Run from the repository root:

```bash
python3 .agents/skills/knowledge-maintenance/scripts/validate_repository.py --strict
```

The validator checks structural routes, declared state/contract schemas, proof-state consistency, declared observation closeout receipts, link targets, metadata, discovery, immutable archives, preservation terms, migrations and whitespace. It cannot prove arbitrary prose agreement, user intent, historical migration fidelity or live Canvas truth; complete the manual conflict and preservation review too.

- Fix every Error.
- In strict mode, resolve every new Warning or document a narrow baseline exception in `.knowledge-validation.json` with a reason.
- Do not weaken a rule or add a broad exclusion merely to obtain a pass.
- Review large deletions manually even when a byte-identical destination exists.

Before closing, run the meaningful regression suite when validator behavior changed: `python3 -B -m unittest discover -s .agents/skills/knowledge-maintenance/tests -v`.

Close with a short migration map: source responsibility, destination, preservation evidence, updated Router, validator result, and any retained uncertainty.
