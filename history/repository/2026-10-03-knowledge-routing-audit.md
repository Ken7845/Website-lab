# Website_Lab knowledge routing and governance audit

Audit date: 2026-10-03, Asia/Shanghai. Declared repository version: Website_Lab_V2.1.1.

This is a repository audit snapshot and a reconstruction proposal. It does not establish live Canvas state, approve a website direction, or introduce new operating rules. Recommendations remain proposals until implemented.

## Conclusion

Keep the progressive-disclosure architecture. Its separation of projects, task Skills, platform references, inspiration, and historical evidence is appropriate for this laboratory. The main defect is that this separation is not consistently enforced at the joins: routing, authorization, current-state synchronization, contract lifecycle, and validation.

Reconstruct those joins before reorganizing large amounts of material. A wholesale rewrite would risk losing precise evidence without resolving the causes of conflicting instructions. No website copy, imagery, brand direction, business facts, or page composition needs revision as a consequence of this audit.

The most urgent work is to establish one task dispatcher, reconcile conflicting continuation pointers, and strengthen validation so a structural PASS cannot conceal an unusable knowledge route or unsupported completion claim.

## What the repository is used for

Website_Lab is both a design laboratory and an execution memory for a human working with an AI agent. It supports personal websites, local-business concepts, and Framer Marketplace templates. Its documents need to preserve approved intent, guide native implementation, support work across interrupted sessions, and retain reusable lessons without forcing the next agent to read everything.

The intended responsibilities are:

| Layer | Purpose | Intended owner |
|---|---|---|
| Repository policy | Scope, authority, authorization, safe platform entry, minimum reads | AGENTS.md |
| Human overview | Explain architecture and declared version | README.md |
| Project memory | Identity, approved intent, source map, current scope | Project PROJECT.md |
| Execution state | Build/QA state, active continuation, durable decisions | STATUS / RECOVERY / DECISIONS, or explicitly owned inline sections |
| Task reasoning | Select and apply a method | Repository Skills |
| Platform knowledge | Standards, implementation patterns, workflows | framer/basic |
| Project-derived patterns | Reusable mechanisms with exact provenance and limits | framer/advance-design |
| Work contracts | Long-lived page requirements and scoped requests | Project checklist directory |
| Inspiration | Design signals and reference interpretation | inspiration |
| Historical evidence | Retired directions, migrations, closed work, observations | Project history and repository history |

The intended execution path is: classify the task → read the project entry when applicable → enter the official platform gate for live Canvas work → select the primary method for the current Part → read targeted references and compile applicable contracts → implement → evaluate the affected scope → update the canonical current owners. Repository maintenance takes a separate path and does not connect to Canvas.

## Scope, method, and limits

The audit covered all repository entry routers, all six repository Skills and their metadata, all five existing project manifests, the sixth project's missing-entry condition, project checklist indexes, Basic and Advanced indexes, relevant procedural sections, validation policy, validator implementation, and the existing validator test suite. Repository-wide inventory, Markdown link checks, index checks, archive hashes, and contract scans supplemented targeted manual reading. Business and website content was inspected only where necessary to identify its owner or evidence status; it was not assessed or rewritten.

Baseline inventory before adding this report:

- 316 files outside .git; 117 Markdown documents.
- Six project directories; five PROJECT.md files.
- Six repository Skills; four contain a detailed live Framer gate in addition to the two root/router copies.
- 107 Markdown files participate in the validator's active-text checks; inactive status does not automatically exempt Markdown link checking.
- Five configured immutable archives.
- Four recognized Component contracts: three Pass, one Blocked.
- Eleven recognized Visual contracts: seven Ready, four Blocked.

The audit began against the current working tree, including ten pre-existing modified files. During the audit those changes became commit d708a0e, “Update: V2.1.1,” through work outside this audit. The final source snapshot is therefore identifiable by that commit; the audited changes were preserved. No live Framer connection, website inspection, platform API capability test, or external website research was performed. Statements about project implementation in this report describe disagreements between repository records, not independently verified Canvas facts.

## Findings and recommended changes

P1 means the issue can lead to the wrong next action, an unnecessary stop, or an unsupported completion claim. P2 means it creates recurring ambiguity or maintenance debt. P3 means useful cleanup after the operational conflicts are resolved. These priorities apply to the knowledge system.

### F01 — P1: The primary routing decision has more than one entry path

Evidence: [AGENTS.md](../../AGENTS.md), lines 53–73, directly maps tasks to Skills and says to read framer/README.md when the task type is unclear. [Framer router](../../framer/README.md), lines 3 and 36–63, calls itself the unique entry and owns the important multi-domain precedence and Visual Direction stage. The Components Skill contains precedence in its description, but the root task table does not explain the same selection sequence.

Consequence: an agent can follow a valid-looking short route directly from AGENTS to Layout or Interactions and miss the dispatcher that requires Components to establish a reusable object's ownership first. A new Page can also reach implementation without encountering the intended design-stage handoff at the router.

Revise: make AGENTS the repository task-classification entry and framer/README the canonical Framer task-selection owner. Root task hints should point to that dispatcher rather than form a competing complete selection table. Explicit Skill invocation should still perform the same ownership scan.

Acceptance: a new responsive accordion routes first to Components; established-component transition changes route to Interactions; page composition without reusable ownership changes routes to Layout; new-page direction routes through Design Taste before implementation; repository-only audits route to Knowledge Maintenance without platform setup. Each scenario must have one defensible primary route.

### F02 — P1: Authorization and audit modes are not specified consistently

Evidence: [AGENTS.md](../../AGENTS.md), lines 91–97, includes confirmation and prior-request exceptions. [Change control](../../framer/basic/workflows/change-control.md), lines 17–24, requires explicit confirmation after recording a long request, while lines 39 and 48–50 permit already-authorized derived contracts to proceed. [Framer checklist](../../framer/checklist.md), lines 31–47, says to ask about a project Checklist “according to AGENTS,” although the current AGENTS no longer states that exact preliminary question. [Summit checklist index](../../content-library/summit-roofing/checklist/README.md), lines 33–45, adds a page-by-page confirmation gate. The [Framer router](../../framer/README.md), line 45, describes read-only audit work, while [QA](../../.agents/skills/framer-qa/SKILL.md), lines 58–65, instructs batch repairs for Fix Required findings.

Consequence: agents can ask repeatedly despite existing authorization, confuse approval of a record with approval of a design, or treat an audit request as authorization to repair the audited target. A genuinely approved project-specific planning gate may be valid, but its provenance and relationship to general authorization are unclear.

Revise: give change-control one authorization decision table covering audit-only, repair, new construction, prior authorization, new direction, destructive change, and publication. Distinguish permission to create the request record, approval of its scope, and permission to implement. Project-specific stricter gates should identify the approved decision that established them. A read-only audit reports repairs unless the user also authorizes them.

Acceptance: an audit-only request causes no target mutations; an authorized continuation does not ask again for unchanged scope; a genuine direction change or publication still stops at the applicable approval gate. All routers describe the same outcome.

### F03 — P1: Current-state fields already disagree within and between owners

Evidence: [Summit PROJECT](../../content-library/summit-roofing/PROJECT.md), lines 211–215, identifies the October 3 opening adaptation as active and specifies its next acceptance work. Lines 286–296 still identify Insight Detail QA and a September 19 checklist synchronization as the continuation. Lines 17 and 315 still say the remaining expansion routes are planned or have not begun, despite the current-status matrix and [page index](../../content-library/summit-roofing/checklist/README.md), lines 53–68, documenting many implemented routes.

The same failure appears in AURELIA: [RECOVERY](../../content-library/aurelia/RECOVERY.md), line 22, lists Chefs metadata, Hero Alt, editable Alt, and naming as current P0 gaps. [STATUS](../../content-library/aurelia/STATUS.md), lines 24 and 87, records Chefs metadata verification and completed Alt/naming work, with a different current gap list.

Consequence: a fresh chat can resume a superseded task or repeat completed work while technically following the project's current entry. Updating a file's top-level date is insufficient when its continuation sections remain stale.

Reconstruct: establish a single active request/Part pointer and one next action. Status owns completion and outstanding checks; Recovery references that state and carries only the continuation checkpoint. Identity and Scope summaries should not maintain independent detailed build inventories. Reconcile existing records using their dated evidence, marking uncertain live claims Needs refresh instead of guessing.

Acceptance: project overview, status, recovery, checklist index, and active request resolve to the same Part. Closed gaps no longer appear as current blockers. This reconciliation can correct documentary contradictions without asserting a new Canvas verification.

### F04 — P1: Contract readiness and implementation results share a state field

Evidence: [Design Taste](../../.agents/skills/design-taste/SKILL.md), lines 46–70, defines pre-write readiness; [Change control](../../framer/basic/workflows/change-control.md), lines 34–48, requires planned evidence to be replaced after implementation and the contract to become Pass or Blocked. Seven recognized Visual contracts remain Ready. Several simultaneously describe implementation results: [Repair build record](../../content-library/summit-roofing/checklist/repair-maintenance/2026-09-16-page-build.md), lines 27 and 61–62; [New Construction](../../content-library/summit-roofing/checklist/new-construction.md), lines 22 and 88–89. This does not prove their pages pass overall; it proves the same record mixes planning and outcome without closing its governing contract.

Consequence: Ready can mean “approved to start,” “already implemented,” or “implemented but incomplete.” A new agent cannot determine whether to build, verify, or resume a blocker from that field alone.

Reconstruct: separate scope authorization, contract readiness, implementation state, and verification result. Keep the contract's decisions stable while evidence fields identify their actual result. Define row-level Pass / Fix Required / Blocked / justified N/A, and explicitly authorized Deferred where the workflow permits it. Overall completion must be derived from the required evidence, not the approval field.

Acceptance: an implemented contract with pending visual evidence cannot look unstarted, and a Ready contract cannot imply completion. Planned proof remains clearly distinguishable from recorded proof. Existing records are reconciled without fabricating missing evidence.

### F05 — P1: The evidence workflow contains conflicting instructions

Evidence: [QA](../../.agents/skills/framer-qa/SKILL.md), lines 24–33, has a graduated evidence ladder. [Preflight](../../framer/basic/workflows/preflight-audit.md), lines 122–124, favors user confirmation for advanced effects and limits agent Preview to exceptions. [Checklist](../../framer/checklist.md), lines 154–164, requires one real interaction path, while lines 219 and 723 use a different Preview preference. [Motion patterns](../../framer/basic/patterns/motion-design.md), lines 224 and 487, require actual Preview, including a blanket three-breakpoint Hover check. Phone behavior should instead follow its touch/static contract.

For visual scope, [image workflow](../../framer/basic/workflows/image-workflow.md), line 26, correctly requires whole-page or compiled evidence for whole-page claims. Its older section at lines 156–173 favors one bounded region and delays another breakpoint. [Token-saving](../../framer/basic/workflows/token-saving.md), lines 307–309, still says to capture only the target container and read only the target node without the newer whole-page-claim exception.

Consequence: one route can stop for user confirmation, another insists on agent Preview, and a third spends a tightly limited screenshot on a crop that cannot prove the requested page-level claim. Structural fallback is appropriate for unavailable visuals, but cannot establish visual Pass.

Revise: use one evidence-selection matrix based on the claim: property, component state, interaction, breakpoint, or whole-page composition. Preserve image residency and retry protection, but define budget scope and what constitutes changed visual state. References should point to that matrix. Required unavailable evidence remains Blocked; successful structure does not waive it.

Acceptance: the same Hover task has one pointer/touch/keyboard verification plan; page-rhythm work plans suitable bounded aggregate evidence before using its visual budget; small nonvisual fixes do not acquire unrelated Preview work.

### F06 — P1: Validator PASS does not cover several declared contracts

Evidence: [Validator](../../.agents/skills/knowledge-maintenance/scripts/validate_repository.py), lines 416–447, checks Markdown links, not executable paths written as inline code. Lines 482–505 enforce discovery coverage only for Basic and Advanced. Lines 506–555 check project existence, line count, owner-name mentions, and split Recovery size rather than state consistency. Lines 599–894 validate recognized contract tables only when an exact heading already exists. Pass checking searches a small list of unfinished words rather than requiring an identifiable evidence result.

Isolated temporary-fixture probes confirmed these limits:

| Probe | Result from the relevant validator methods |
|---|---|
| Nonexistent rule written as an inline path | No finding |
| Same nonexistent rule written as a Markdown link | markdown.broken_link; positive control |
| Reusable-component request without a Component contract | No finding |
| Component Pass with both proof cells saying “not run” and an inline nonexistent governing source | No finding |
| Visual contract under a numbered heading rather than the exact recognized heading | No finding |
| Broad checklist inactivation pattern differing from the exact blacklist strings | No policy finding; the fixture's stale-route text was skipped |

These were method-level tests in temporary directories, not claims that every fixture passed a full repository validation. No exclusion was added to this repository.

Reconstruct: validate declared applicability and canonical owner paths, parsed links/anchors, explicit evidence states and references, contract lifecycle, and active-pointer consistency. Require structured applicability so the validator does not guess construction intent from arbitrary prose. Validate scope exclusions by what they match, rather than only a few exact strings. Share Component/Visual schema logic where appropriate instead of maintaining near-duplicate validation loops.

Acceptance: add positive and negative tests for each demonstrated gap. The validator must continue to distinguish repository evidence from live Canvas proof; it should validate whether evidence is identified, never invent or judge the visual result.

### F07 — P2: Detailed policies have multiple owners, and validation requires duplication

Evidence: the detailed live gate appears in [AGENTS](../../AGENTS.md), [Framer router](../../framer/README.md), and all four Framer Skills. [.knowledge-validation.json](../../.knowledge-validation.json), beginning at line 93, requires many of the same literal instructions in each owner. Layout, image-role, and visual-direction requirements are likewise repeated across Skills, Baseline, Build, Checklist, and Preflight.

Consequence: an improvement must be propagated to several detailed copies. Literal term preservation protects against accidental deletion, but can also make safe deduplication fail while contradictory copies still pass.

Revise: retain one full canonical definition per policy. Other documents retain a short applicable guard and a validated link, or turn the policy into an evaluator question. Update precision contracts to verify the canonical rule and its required routes. Do not remove the live gate or its safety receipt as part of deduplication.

Acceptance: one deliberate policy revision has one normative edit location; routed evaluators still test its consequences. Unique values and historical evidence are preserved before any detailed duplicate is removed.

### F08 — P2: Long-lived page contracts and request records are not consistently owned

Evidence: [Checklist](../../framer/checklist.md), lines 49–72, specifies one formal page Markdown and a fixed page-file layout. [Summit index](../../content-library/summit-roofing/checklist/README.md), lines 57–59, uses request folders/records for Home and Repair instead of existing home.md and repair-maintenance.md page owners; neither file exists. AURELIA deliberately uses nested About and Chefs page owners, documented in its index and migration policy. [Build workflow](../../framer/basic/workflows/build-checklist.md), line 20, requires the Visual contract in an active request Checklist, while Design Taste permits a working-response contract when no request Checklist exists.

Consequence: there is no uniform way to locate the current page contract, determine whether a dated request is the durable page owner, or decide where a required contract should live. The problem is ambiguity, not the nested layout itself.

Reconstruct: explicitly map each page to one long-lived contract and each active Part to one request record where applicable. Decide whether paths are fixed or index-declared; avoid claiming both. Put the pre-write Checklist schema in change-control and let the post-implementation evaluator link to it, so agents do not have to load an evaluator to discover construction prerequisites.

Acceptance: a fresh chat can find any page's current contract through PROJECT and its index, without browsing a folder or inferring from dates. Multiple requests preserve original requirements without becoming competing current page owners.

### F09 — P2: Legacy entry and recovery debt is acknowledged but can grow indefinitely

Evidence: [Validation policy](../../.knowledge-validation.json), lines 29–34, baselines Dutch Treat's absent manifest and Ken Studio's overloaded manifest. [Ken PROJECT](../../content-library/ken-studio/PROJECT.md) has 656 lines; its Recovery begins at line 482 and continues through extensive implementation narratives. The validator limits only standalone RECOVERY.md size, not inline recovery. It accepts the overloaded-project exception at any later line count. Morrow's project entry, TODO, and original prompt also lack explicit current/closed ownership metadata and manifest-wide verification dates.

Consequence: “temporary migration debt” can remain accepted while more history accumulates in current startup context. The affected project becomes expensive to resume and may inherit stale session assumptions.

Revise: schedule a bounded migration. Create Dutch Treat's minimal manifest from existing records without claiming live verification. Split Ken's status, durable decisions, latest Recovery, and history while preserving the exact historical record. Clarify Morrow's remaining-work owner and the status of its original request. Add baseline scope, growth limits, and review conditions so exceptions do not silently expand.

Acceptance: one latest checkpoint per project; session identifiers treated as prior-session references until connection is re-established; no implementation diary in current Recovery; baselines cease to suppress new drift. File length alone is not a reason to split useful targeted references.

### F10 — P2: Project examples sometimes become cross-project defaults

Evidence: [Knowledge Maintenance](../../.agents/skills/knowledge-maintenance/SKILL.md) prohibits elevating one project's exact parameter into a universal default. [Button pattern](../../framer/basic/patterns/buttons.md), lines 90–96, requires every reusable Button to have a Small Variant and uses AURELIA's 10px label and 12px/18px padding as the reference for new Small surfaces unless another system already exists. [Motion guidance](../../framer/basic/patterns/motion-design.md), lines 21–26, more carefully distinguishes a starting proposal from a project-approved parameter.

[Navbar/Footer](../../framer/basic/patterns/navbar-footer.md), lines 50–83, describes both a compact height-reveal drawer and a compact Relative Overlay preference. The drawer section contains a useful distinction for an anchored floating panel, but [Pattern Recipes](../../framer/basic/patterns/pattern-recipes.md) still reduces Phone menus to a general Relative Overlay default.

Consequence: a general rule can import a project's sizing or create unnecessary states; a simplified recipe can erase an important interaction choice.

Revise: separate hard platform constraints, general ownership principles, recommended decisions, and dated project examples. Require Small states when the component's usage contract calls for them. Keep AURELIA's exact measurements as examples. Route Phone menu selection by intended behavior: integrated height reveal, anchored floating panel, or full-page modal; preserve an approved existing mechanism.

Acceptance: a new project inherits responsibility rules and selection criteria rather than AURELIA's dimensions or a universal menu mechanism. This is an instruction change, not a proposal to change existing Button or Navbar designs.

### F11 — P2: Inspiration and historical material can re-enter as operating instructions

Evidence: [Inspiration README](../../inspiration/README.md) has no typed index distinguishing source-site studies from project records. [Dutch Treat HANDOFF](../../inspiration/restaurant/dutch-treat-restaurant/HANDOFF.md) contains project scope, intended page routes, operational lessons, and next-work guidance inside the inspiration tree. [AURELIA PROJECT](../../content-library/aurelia/PROJECT.md), lines 183–184, routes current component detail to a pre-migration snapshot. This is a legitimate evidence fallback, but its limitation should be explicit. Advanced correctly labels several entries Reference or Legacy, while some documents rely on the index rather than carrying that classification locally.

Consequence: category-based inspiration reading can bring in stale project instructions. Reading a pattern or archive directly can lose its index-level provenance and applicability limits.

Revise: keep source-site design studies in Inspiration; put closed project handoffs in project History and point to current PROJECT. Preserve retrospective lessons as evidence, not fresh commands. Add local status, provenance, verification scope, and canonical-successor information where direct reads are likely. Where an archive is the only exact evidence, label the route historical and require current readback before reuse.

Acceptance: inspiration cannot select the next project action; direct pattern reads expose their Reference/Legacy limits; archives remain immutable. Do not move or normalize the five hash-protected archives casually.

### F12 — P2/P3: Discovery and path hygiene are weaker outside the Framer indexes

Evidence: Markdown file-link analysis found 25 nonhistorical, non-Skill-entry documents with no incoming file link. This is a discovery signal, not proof they are unused: several are intentionally referenced as plain paths. Project discovery, checklist coverage, and Inspiration coverage are not part of the validator's index coverage checks.

Concrete discrepancies include the physical folder `inspiration/restaurant/ nirvana-on-vitoria` with a leading space versus the no-space reference in [Dutch Treat prompt](../../content-library/dutch-treat-restaurant/prompt.md), line 22; `insipiration.md` in the Masayoshi folder; and shorthand Inspiration paths in [HK Place PROJECT](../../content-library/HK%20Place/PROJECT.md), line 32. [Ken PROJECT](../../content-library/ken-studio/PROJECT.md), line 391, refers to a temporary contact sheet not present at that repository-relative path. Root payment-SOP.md has no declared route/owner in the knowledge overview, and root TODO.md is empty. The observation guide mentions a reviews directory whose location is undefined and which does not currently exist.

Revise: make executable source paths validated links or declared route fields; keep examples and placeholders distinguishable. Add lightweight project and Inspiration discovery tables to their existing READMEs. Register legitimate external/temporary dependencies with a boundary and fallback. Normalize spelling/space issues with preserved references. Decide whether the payment SOP belongs to the laboratory's operating knowledge and register it accordingly; defer empty-file cleanup until after routing repair.

Acceptance: every active project, page contract, and reusable reference has a discoverable owner; concrete execution links resolve; required external assets are not falsely treated as repository files. Do not treat every unlinked example as an orphan or require a folder rename without updating all references.

## Authority and version rules that should be made explicit

The root policy already makes an important distinction: current Canvas proves what exists and does not automatically authorize a change in direction. Preserve it. Lower-level phrases such as “Canvas remains the final source of truth” or “Canvas takes precedence over this decision” are too broad when separated from that distinction. A flat priority list should be interpreted by question:

| Question | Governing authority |
|---|---|
| What may change? | Current user authorization and active scope |
| What should the design do? | Explicit user direction and active approved decisions |
| What currently exists? | Targeted current implementation evidence |
| What facts may be used? | Approved sources and their fact status |
| What can the platform support? | Current official platform capability and hard constraints |
| How should the task be executed? | Applicable canonical workflow and selected Skill |

Also define when newly introduced contract requirements apply. QA currently treats absence as Fix Required, while older builds predate the contract rules and the validator checks only contracts that exist. Versioned applicability should distinguish new work, a current modification, a legacy audit, and a retrospective migration. Never synthesize evidence to make an old record appear compliant. Documented old API recipes should be treated as dated mechanisms to resolve through the current official task map, not as independently verified current capability.

At audit startup the README declared v2.1.1 released while related changes were uncommitted. During the audit those changes became commit d708a0e. No Git tags exist; tags are optional, and their absence is not a release defect. Future release records should identify their source commit or explicitly say working-tree revision so the version label resolves to a reproducible snapshot.

## Reconstruction plan

| Order | Work package | Existing owners to revise | Completion criterion |
|---|---|---|---|
| 1 | Reconcile current pointers | Summit PROJECT/checklist pointers; AURELIA STATUS/RECOVERY | One active Part, coherent next action, no contradictory gap lists |
| 2 | Unify dispatch and authorization | AGENTS; framer/README; change-control; project planning gates | Deterministic route and confirmation behavior for each scenario |
| 3 | Define contract lifecycle and page ownership | change-control; Component/Design Skills; page indexes; manifest template | Readiness, authorization, implementation, and QA cannot be confused |
| 4 | Unify evidence policy | image workflow; QA; Preflight; Checklist; token-saving; motion references | One claim-specific verification plan, explicit blockers, preserved visual limits |
| 5 | Strengthen validator and tests | Existing validator, tests, validation policy | Demonstrated false negatives fail; valid fixtures and immutable archives still pass |
| 6 | Migrate bounded legacy debt | Dutch Treat entry; Ken current/history split; Morrow ownership | Minimal startup context and precise preservation map |
| 7 | Clean discovery and local classifications | content-library/README; inspiration/README; direct-read pattern metadata | Typed routes, validated paths, historical records cannot act as current instructions |

Avoid creating a new parallel rulebook, all-purpose super-Skill, duplicate Checklist system, or database merely to manage these changes. Most reconstruction fits in the current files and directory responsibilities.

Before moving or removing knowledge, identify its existing owner, destination, evidence status, and references. Preserve unique parameters and historical examples exactly. Update active routes before removing their old owner. Keep unknown live state explicitly unverified.

## Forward-test scenarios for revised routing

These are static audit scenarios, not live Canvas runs or independent-agent tests. Their acceptance outcomes should become regression cases after routing revision.

| Scenario | Required behavior |
|---|---|
| Audit knowledge routing only | Knowledge Maintenance; no Framer setup; report findings |
| Audit an existing page without repairs | Platform gate + QA; report defects; no Canvas mutations |
| Fix one existing link | Existing-object repair; targeted readback; no visual-direction contract |
| Create a reusable responsive accordion | Establish Component ownership before interaction/layout; applicable contract |
| Change only an established Hover transition | Interactions primary; preserve existing Component contract |
| Build a new page from an approved direction | Design contract → implementation primary → scoped QA; no redundant approval |
| Continue the same Part with added feedback | Reconcile original requirements and current request; keep constraints not withdrawn |
| Resume after compaction | Re-read required active sources; verify connection and target; never infer live session from an old number |
| Audit a legacy page lacking a newer contract | Apply documented legacy policy; report evidence limits; no invented historical proof |
| Required visual evidence fails twice | Stop the failing chain; continue independent work; Visual remains Blocked |
| Publish a finished site | Separate publication authorization; construction completion does not imply it |

## Verification and delivered changes

The baseline strict validator completed with 0 errors, 0 warnings, and 3 notes: the intentionally unnormalized immutable archive, Dutch Treat's missing manifest baseline, and Ken's overloaded-manifest baseline. The four existing Visual-contract regression tests passed. The isolated fixture probes above exposed five unreported defects/coverage gaps plus a working broken-link control.

The audit added this report only. Add/Reuse/Modify decision: Add, because no equivalent repository routing audit existed; existing project audits have a different Canvas scope. No current router, Skill, validation exception, project content, or historical archive was changed. No knowledge migration was performed. All reconstruction items remain proposed.

After adding the report, the strict validator again passed with 0 errors, 0 warnings, and the same 3 notes. The existing four tests again passed. Whitespace validation and a final working-tree review confirmed that this audit added only the report; the ten pre-existing changed files are now part of commit d708a0e.
