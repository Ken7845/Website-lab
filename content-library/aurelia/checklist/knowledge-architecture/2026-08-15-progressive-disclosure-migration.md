# Website-lab Progressive Disclosure Migration

Status: Complete; explicit confirmation received; repository-wide validation passed
Scope: Repository knowledge architecture only; no Framer Canvas changes
Date: 2026-08-15

## User Prompt (verbatim)

这次任务是一次 website-lab 知识架构重构。请直接完成整个任务，但这是“无损迁移”，不是普通的删减或清理。

====================
一、为什么要做这次重构
====================

website-lab 是我长期积累的网站设计、Framer 实现、项目状态、踩坑经验、设计方法和高级组件知识库。

它在项目早期比较小的时候非常有帮助，但随着不断补充，现在出现了一个明显问题：

我每次开始 Framer 工作，通常都会要求 Agent：
- 从 AGENTS.md 开始阅读；
- 阅读当前项目 PROJECT.md；
- 阅读 framer/basic；
- 再按 Checklist 工作。

目前仅启动阶段就可能消耗约 58k context。

实际工作中我观察到：

1. 从 0 开始创建网站时，Agent 往往有比较好的自主设计判断。
2. 当一个网站已经完成大部分、知识库也越来越完善后，Agent反而容易表现得机械：
   - 用户说“改成左右布局”，就把 Phone 也机械做成左右布局；
   - 用户要求“结合网站已有风格”，却没有主动分析已有页面中的排版模式；
   - 新增 Section 前不会先确认页面是否已有同功能 Section；
   - 甚至同一页面重复创建 Reservation Handoff；
   - 用户指出一个问题后，只修字面问题，而不是重新思考该 Section 在整个页面、断点和设计系统中的合理方案。
3. 我做过一个对照实验：
   - 读取完整知识库后做 AURELIA 的 reservation-handoff，出现了大量上述问题；
   - 完全不读知识库，只要求“检查现有网站并给 Home/Menu/Chefs 最后加入 reservation-handoff，只修改这个 Section”，结果虽然设计不惊艳，但明显更正常、更少低级错误。

所以当前问题不是知识不够，而是：
“知识库正在变成过大的 working context，使规则、历史状态和当前任务互相争夺注意力。”

目标是：

KNOWLEDGE 可以继续越来越丰富，
但每次 TASK 的 working context 必须保持小而相关。

原则：

DELETE CONTEXT, NOT KNOWLEDGE.

====================
二、这次重构的核心目标
====================

把 website-lab 从：

“大量 Markdown + 每次要求 Agent 预读很多文件”

重构为：

“小型入口 / Router
→ 当前项目事实
→ 按任务触发 Skill
→ 必要时读取详细 Reference
→ 实施
→ 最后才调用 QA / Checklist”

需要建立真正的 progressive-disclosure 架构。

不要把所有资料变成 Skill。
需要明确区分以下概念：

1. AGENTS.md
   = repository-level routing + 少量永远有效的硬边界。

2. Skills
   = 可跨项目重复使用的“工作方法和能力”。
   例如：
   - 修改已有设计前如何 audit；
   - Framer responsive；
   - Framer component / variant；
   - design taste / anti-template；
   - Framer QA。

3. Project current state
   = 某个具体项目“现在是什么”。
   例如 AURELIA 当前页面、组件、视觉语言、现有 Section、breakpoints、active decisions。

4. References / Patterns
   = 需要时查询的详细技术知识、精确参数和经过验证的解决方案。

5. History / Decisions
   = 为什么以前这么做、哪些方案被废弃、历史设计方向。

6. Recovery / Working state
   = 最近工作的中断点和恢复信息。
   不能无限 append 成项目历史日志。

====================
三、最重要的安全要求：知识零损失
====================

我非常担心这次重构时，以前几周逐渐加入的精确经验被“简化”掉。

因此：

这不是内容删减任务。

任何：
- 精确数值；
- Breakpoint 参数；
- 已验证 Component 结构；
- Framer Pattern；
- Bug 原因；
- 修复路径；
- Tool / Session 经验；
- 响应式经验；
- Marketplace 要求；
- 图片 workflow；
- Advanced Design 实现；
- 历史设计决定；
- Retired direction；
- QA caveat；
- Recovery information；

都不得仅仅因为“看起来太细”“似乎重复”“可以概括”为由消失。

必须遵循：

MOVE BEFORE DELETE.

在删除旧位置的内容之前，必须确认：
1. 它已经完整存在于新的合理位置；
2. 唯一细节没有被摘要掉；
3. Git diff 可以追踪它去了哪里。

如果某段信息是否仍然有价值无法确定：
保留，移动到 Reference / History / Archive；
不要自行删除。

禁止：
- git reset --hard
- 丢弃用户已有未提交修改
- 为了“清爽”删除无法确认价值的经验
- 用一句通用原则替代唯一存在的精确实践

修改前先检查 git status。

如果当前已有未提交修改：
保护它们，不 reset、不覆盖。

在整个迁移结束前保持所有原始信息可恢复。

====================
四、首先重构 AGENTS.md
====================

当前 AGENTS.md 已经不只是 router，而包含大量：

- Framer workflow
- Advanced / Basic 建设方法
- Checklist 流程
- responsive
- communication workflow
- image workflow routing
- verification
- implementation details

这会使它成为长期 always-on context。

目标：

将 AGENTS.md 缩成真正的入口地图。

建议目标大约 50–100 行，但以职责清晰为优先，不要为了达到数字强删信息。

AGENTS.md 只应该主要保留：

- website-lab 是什么；
- 当前实际 project / Canvas 是 source of truth；
- 用户明确要求优先；
- 不得编造事实；
- 不得擅自扩大 scope；
- repository 的知识地图；
- PROJECT current state 在哪里；
- Skills 在哪里；
- Reference / Pattern 在哪里；
- 如何按任务选择最少必要上下文；
- 一个核心规则：
  “Do not preload the entire knowledge base.”

将 Framer 专项执行细节移到对应 Skill / Reference。

AGENTS 的职责是：
告诉 Agent 去哪里找知识，
而不是自己承载知识。

====================
五、重构 AURELIA PROJECT
====================

当前 AURELIA PROJECT.md 已经同时承担：

- Current project identity
- Current Canvas description
- Visual system
- 页面设计说明
- Supporting-page planning
- Active decisions
- Retired decisions
- Build Status Matrix
- QA backlog
- Recovery State
- 多天累计 implementation log
- 精确 component 参数

目前已经存在新旧状态混杂现象。

例如：
PROJECT 不同位置可能同时出现旧 sitemap / 新 sitemap、
旧 To-do 状态 / 已 Built 状态、
旧 handoff 规划 / 后来明确删除 handoff 的 active decision。

因此将 AURELIA 拆成职责明确的结构。

可以根据现有 repository 风格调整文件名，但建议接近：

content-library/AURELIA/
├── PROJECT.md or CURRENT.md
├── STATUS.md
├── DECISIONS.md
├── HISTORY.md
├── RECOVERY.md
└── checklist/

要求：

CURRENT / PROJECT：
只回答“现在是什么”。

包含：
- project identity
- current sitemap
- 当前页面责任
- 当前 visual language
- 当前 typography / color / layout rhythm
- 当前 reusable components
- 当前 cross-page design language
- current responsive direction
- 当前仍有效的重要 constraints

不保留旧状态。

STATUS：
只保存当前 Build / QA 状态。
更新时覆盖旧状态，而不是不断追加日志。

DECISIONS：
保存仍然有效且需要解释“为什么”的设计决定。

HISTORY：
保存 retired direction、过去方案和旧实现历史。
默认任务不读取。

RECOVERY：
只保存最近真正需要恢复工作的 active state。
旧的实施日志移入 history/reference，不无限累积。

特别注意：
当前 AURELIA 的 Framer Canvas 是最终 current-state source of truth。

PROJECT 文档不得因为历史记录与 Canvas 冲突而覆盖真实 Canvas。

====================
六、重构 design-taste SKILL
====================

当前根 SKILL.md / design-taste 来自 GitHub，是一个很长的 frontend design skill。

它里面有很多有价值的东西：
- brief inference
- anti-default / anti-slop
- design dials
- layout diversity
- motion motivation
- redesign audit
- responsiveness
- preflight
等等。

这些知识必须保留。

但是它也包含大量：
- React
- Next.js
- Tailwind
- Motion / GSAP
- Web-specific breakpoints
- dark mode defaults
- icon libraries
- frontend implementation
- 与 Framer 项目不一定相关的技术规则

其中一些通用默认甚至会与已经成立的项目设计冲突。

例如已有 AURELIA 可以合法拥有：
- Inter；
- custom cursor；
- 固定 light editorial system；
- 有意设计的 dark Invitation transition；

通用 Skill 不能因为自己的默认偏好去推翻已经存在并经用户确认的项目设计。

因此将 design-taste 改造成真正的 Skill：

建议结构：

.agents/skills/design-taste/
├── SKILL.md
└── references/
    ├── original-design-taste.md
    ├── anti-slop-rules.md
    ├── frontend-implementation.md
    ├── motion-reference.md
    └── 其他确有必要的 reference

要求：

1. 当前 GitHub 原始 SKILL.md 必须完整保留一份 verbatim archive/reference。
2. 主 SKILL.md 只保留真正的设计判断框架和调用规则。
3. Skill 必须明确：
   - 先 read the room；
   - existing project = audit first；
   - current Canvas / approved project language > generic Skill defaults；
   - 用户明确方向 > Skill aesthetic defaults；
   - 通用规则是 guidance，除非明确标记 universal safety/accessibility requirement；
   - 只在需要时读取 references。
4. 不允许主 design Skill 每次自动把所有 frontend implementation reference 载入 context。

====================
七、重构 Framer Basic
====================

不要删除 framer/basic 中经过真实项目踩坑后形成的知识。

尤其需要保护：
- targeted read；
- component / instance / breakpoint 分层；
- width ownership；
- responsive；
- button structure；
- image workflow；
- token-saving；
- Pattern recipes；
- Navbar/Footer；
- Marketplace；
- motion；
- QA；
- layer naming。

问题不是这些知识“存在”，
而是 Agent 不应该每次都全部读取。

检查现有 framer/basic，并将“重复工作方法”抽象成少量清晰 Skill。

例如可以考虑：

.agents/skills/
├── design-taste/
├── framer-layout-responsive/
├── framer-components/
├── framer-interaction/
└── framer-qa/

不要为了 Skill 数量而过度拆分。

每个 Skill 的 description 必须让 Codex能够判断：
“什么时候应该调用我”。

详细实现、参数、Pattern、长篇踩坑经验继续留在 references / framer/basic，
Skill 只负责：
WHEN + HOW TO REASON + WHAT TO LOAD。

例如：

framer-layout-responsive Skill：
不是把所有 responsive 文档复制进去，
而是告诉 Agent：

修改布局时：
1. inspect existing Desktop / Tablet / Phone；
2. 找真实已有 pattern；
3. 判断 width ownership；
4. Desktop composition 在窄屏是 transform，不是 mechanically shrink；
5. 按需读取对应 reference；
6. 实施后验证三个 breakpoint。

====================
八、改变设计任务 workflow
====================

这是这次重构最重要的行为变化。

旧思路容易变成：

READ RULES
→ READ MORE RULES
→ CHECKLIST
→ DESIGN
→ QA

我要改成：

TASK
→ READ SMALL ROUTER
→ READ CURRENT PROJECT STATE
→ INSPECT ACTUAL CANVAS / CURRENT IMPLEMENTATION
→ RECONCILE EXISTING STATE
→ IDENTIFY EXISTING DESIGN PATTERNS
→ LOAD ONLY RELEVANT SKILL / REFERENCE
→ PLAN
→ IMPLEMENT
→ TARGETED QA

特别加入一个非常重要的步骤：

BEFORE CREATE → CHECK WHETHER IT ALREADY EXISTS.

用户要求：
“给页面添加 reservation handoff”

不能直接解释为：
CREATE RESERVATION HANDOFF。

Agent 应先检查：
- 页面是否已经存在同功能 Section；
- 是否已经有 CTA / Invitation / reservation handoff；
- 是 Add、Reuse、Modify 还是 No-op；
- 是否会产生重复内容。

设计任务也不能机械把用户局部反馈变成跨断点硬约束。

例如：
用户说 Desktop 使用左右布局，

Agent 应理解：
这是 desktop composition intent，

然后独立判断：
Desktop
Tablet
Phone

而不是把 Phone 机械设成左右布局。

====================
九、Checklist 与 QA 的地位
====================

不要让大型 Checklist 在“创造设计之前”占据大量 context。

将它们更多作为 evaluator / verifier，而不是 generator。

正确思路：

inspect
→ reason
→ design
→ implement
→ targeted verification

而不是：

memorize every possible rule
→ attempt to design inside them

Hard constraints 与 Design Guidance 必须明确区分。

Hard constraints 例如：
- 不修改用户 scope 之外区域；
- 不编造真实事实；
- 不重复已有 Section；
- 必须检查实际 breakpoint；
- 不破坏已存在 component behavior。

Design guidance 例如：
- editorial
- restrained
- asymmetric
- cinematic motion

Design guidance 是帮助 Agent判断，不应该被机械解释成固定布局模板。

====================
十、此次任务禁止修改 Framer Canvas
====================

本次任务只重构 website-lab repository。

不要：
- 修改 AURELIA Framer Canvas；
- 修改任何真实网页设计；
- 发布网站；
- 重做任何 Component。

这里只改：
知识组织、文件职责、routing、Skill architecture 和相关 documentation。

====================
十一、执行方式
====================

不要停留在建议层。

请实际完成重构。

执行顺序：

Phase 1 — Audit
- 查看 git status；
- 审计当前 repository；
- 建立内部 Migration Map；
- 标记每类信息：
  current / skill / reference / decision / history / recovery / obsolete duplicate。

Phase 2 — Preservation
- 在移动任何唯一知识前确定 destination；
- 原始 design-taste 完整保存；
- 确认没有唯一内容只有一个即将删除的来源。

Phase 3 — Architecture
- 重构 AGENTS；
- 建立 Skills；
- 重构 AURELIA project docs；
- 重构 Framer Basic routing；
- 更新 README / indexes。

Phase 4 — Deduplication
只有确认内容已经完整迁移后，
才删除旧位置的重复文本。

Phase 5 — Validation
最后必须做 repository-wide audit。

====================
十二、最终验收
====================

完成后验证：

1. 一个普通 AURELIA 小范围 Section 修改，
   理论上启动只需要：
   - AGENTS
   - AURELIA current state
   - 1 个相关 Skill / reference
   而不需要通读整个 website-lab。

2. AGENTS 本身不再承担 Framer 操作手册职责。

3. AURELIA current-state 文件内部不存在明显 stale state 与 current state 冲突。

4. 历史信息仍然可查。

5. design-taste GitHub 原始规则仍有完整备份。

6. 所有重要 Framer 经验仍存在。

7. Skill 与 Project knowledge 职责明确。

8. 搜索原有的重要关键词和精确参数，仍可以在 repository 中找到对应知识。

9. 检查 git diff：
   对每一类大量删除内容，都能够说明它迁移到了哪里。
   如果无法解释某段删除内容的 destination，恢复它。

10. 不存在两套并行、职责重叠的新旧体系。

11. README 更新为新的知识架构说明。

====================
十三、完成后的报告
====================

最后不要给我长篇工作日志。

只报告：

- 新的 repository architecture；
- 创建 / 拆分 / 重构了哪些核心文件；
- AGENTS 大约从什么规模降到什么规模；
- AURELIA current / history / recovery 如何分离；
- 创建了哪些 Skills，以及分别什么时候触发；
- 原 design-taste 放在哪里；
- 有无任何无法安全迁移、所以暂时保留的内容；
- 是否确认没有主动丢弃唯一知识；
- 以后一个普通 Framer Section task 推荐的最小读取路径；
- git diff / validation 的最终结论。

如果在迁移过程中发现我现有架构里还有比上述更严重的 context-routing 问题，可以修正架构，但必须继续遵守：
“知识零损失、current state 与 history 分离、按需读取优先”的总目标。

## Execution gates

- [x] Git status checked before migration.
- [x] Verbatim request captured and read back.
- [x] User explicitly confirms this captured scope.
- [x] Audit and migration map completed.
- [x] Unique knowledge preserved before removal.
- [x] Architecture refactor completed.
- [x] Deduplication destination audit completed.
- [x] Repository-wide validation completed.
- [x] No Framer Canvas, website, publishing, or component changes made.

## Migration map

| Source responsibility | Canonical destination | Preservation rule |
|---|---|---|
| Repository routing and always-on boundaries in `AGENTS.md` | Lean `AGENTS.md`; detailed Framer change control in `framer/basic/workflows/change-control.md` | Committed pre-router manual preserved byte-for-byte in `history/repository/agents-pre-router-2026-08-15.md` |
| Root `SKILL.md` | `.agents/skills/design-taste/SKILL.md` plus conditional references | Untouched original archived at `.agents/skills/design-taste/references/original-design-taste.md` |
| Framer layout/responsive method | `.agents/skills/framer-layout-responsive/SKILL.md` | Detailed parameters remain in `framer/basic` and project-specific advanced references |
| Framer component/variant method | `.agents/skills/framer-components/SKILL.md` | Existing Button, Navbar/Footer, naming, width-ownership, and advanced pattern files remain canonical references |
| Framer motion/interaction method | `.agents/skills/framer-interactions/SKILL.md` | Existing motion and advanced implementation documents remain available by pattern |
| Checklist, preflight, image evidence, delivery QA | `.agents/skills/framer-qa/SKILL.md` | QA loads only after implementation and only by applicable headings |
| AURELIA mixed `PROJECT.md` | New `PROJECT.md`, `STATUS.md`, `DECISIONS.md`, `HISTORY.md`, `RECOVERY.md` | Pre-migration working copy preserved verbatim under `history/` |
| AURELIA retired IA and implementation logs | `HISTORY.md`, request-specific Checklists, and immutable pre-migration snapshot | Never treated as current-state input |
| Framer Basic and Advanced discoverability | `framer/README.md`, lean `framer/basic/README.md`, `framer/advance-design/README.md` | No detailed reference deleted merely to reduce startup context |
| Human-facing architecture | Root `README.md` and `content-library/README.md` | Explain ownership without duplicating operating manuals |
| Retired repository overview and single-file project schema | `history/repository/` | Former README and manifest template preserved byte-for-byte; archive never participates in startup routing |

## Preservation checksums

- Original design-taste before migration and archived reference: `aa194351b246b8b4799099d4ed7b033d29eab6e6e3d58d8d2172978be7b3ec89`.
- Dirty AURELIA `PROJECT.md` before migration and archived snapshot: `462b699f6ef9fbf4af28528252faefc4dc924192a303adddf50c88e9582f52c8`.
- Old committed `AGENTS.md`, `README.md`, project-manifest template, and root `SKILL.md` archives match their original Git blob ids exactly.
