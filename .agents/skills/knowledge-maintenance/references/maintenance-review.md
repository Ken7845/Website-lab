# Maintenance conflict review

Read this only for an audit, router/Skill revision, migration, or current-state repair. Ordinary content entry needs only the main Skill.

## Review the affected routes

Record the task mode and source evidence. Search existing owners before creating files. For each realistic request trace entry → dispatcher → project owner → selected method → conditional references → authorization → evidence → current-state update.

| Concern | Check | Failure response |
|---|---|---|
| Authority | Separate observed implementation, intended direction, facts and permission | Retain the approved direction; record differences |
| Trigger | The same task has one primary dispatch outcome | Fix the nearest canonical dispatcher, then its callers |
| Authorization | Existing permission and audit-only boundaries agree | Do not add approvals or repair targets beyond authorized mode |
| Ownership | One detailed owner; summaries link to it | Move unique detail first; update callers before retiring duplicates |
| Continuation | Status / Recovery share revision and active request | Reconcile dated records; mark live uncertainty Needs refresh |
| Evidence | Ready is preparation; Pass names recorded proof | Mark missing proof Blocked, never synthesize verification |
| Discovery | Concrete source routes resolve; archive classifications survive direct reads | Repair links or register external/Legacy boundaries |
| Preservation | Exact unique parameters and old evidence survive migration | Compare source and destination manually plus hashes |

Use [Content Library state contract](../../../../content-library/README.md#current-state-contract) and [construction contract lifecycle](../../../../framer/basic/workflows/change-control.md#contract-lifecycle) for their schemas. Rule bodies remain in their canonical owner; callers link instead of copying them.

## Forward-test and close

Give a fresh evaluator the revised Skill, a realistic request, and the minimum raw artifacts. Do not give suspected failures or expected route labels. For a substantial routing repair use an independent subagent with no inherited audit conclusions, no Canvas connection, no repository writes, and a temporary output directory. Review its actual route, authorization decision, evidence requirements and outcome. Repair demonstrated issues; rerun only affected tests.

A regression test must prove a behavior: missing source rejection, false Pass rejection, absent required contract, stale state pointer, forbidden exclusion, archive corruption or a valid migration. Matching a particular sentence is not sufficient.

Report: mode and scope, source → destination map, preserved unique evidence, corrected routes, automated results, independent-test result and any unresolved semantic or live-state uncertainty. An automated PASS never waives the manual review above.
