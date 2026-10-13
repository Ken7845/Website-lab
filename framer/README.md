# Framer 工作路由

本目录是仓库内 Framer 工作的唯一入口。先检查并协调当前状态，再选择一个主要仓库 Skill；不要把全部 Skills、Checklist 和 references 同时预读。

## 0. Live Canvas Hard Gate

完整连接协议只由 [AGENTS — Live Framer Canvas Gate](../AGENTS.md#live-framer-canvas-gate) 维护。本 router 和仓库 Skills 不复制平台命令。

真实 Canvas 读取、审计或写入必须先完成该 Gate；official `$framer` Skill 和动态 task map 提供当前能力。**Gate remains closed** 时停止 Canvas 判断；Browser / Playwright / Computer Use fallback 仍须符合 canonical Gate 的明确授权条件。正式实施前显示 **Framer Agent gate receipt**。纯仓库文档、规划和知识维护跳过连接。

## 1. 先 Inspect / Reconcile

任何写入前先确认：

1. 当前任务的项目、页面、Part、授权范围和 task mode：Audit only / Repair / Build / Publish。按 [authorization table](basic/workflows/change-control.md#authorization-and-task-mode) 判定；Audit only 不写 Canvas，发现修复项只报告。
2. 当前项目 `content-library/<project>/PROJECT.md`。只有任务正在恢复中断状态时再读 `RECOVERY.md`；通过 PROJECT 的 active pointer 读取当前页面 / 请求合同，不猜测最新日期文件。
3. 用户本轮要求是新增、校正还是明确覆盖旧要求；连续修改按 [`basic/workflows/change-control.md`](basic/workflows/change-control.md) 建立约束锁。
4. 当前真实结构与最后成功状态；中断任务先恢复，不根据聊天记忆重做。
5. 当前结论的证据来源是 Framer Agent targeted readback、明确标注的 UI fallback，还是尚未验证；只有第一种可直接写为 Verified Canvas current state。

官方 `$framer` Skill 负责平台连接与能力入口，不计入下面的“一个主要仓库 Skill”。仓库不再维护平行的 `agent-connection.md`。

## 2. 只选一个 Primary Repo Skill

按本轮主要判断选择一个；其他领域通过 [`basic/README.md`](basic/README.md) 按需读取 reference，不再同时加载第二个建设 Skill。

| 主要任务 | Primary repo Skill | 典型范围 |
|---|---|---|
| 品牌方向、叙事、参考转译、视觉审阅 | [`design-taste`](../.agents/skills/design-taste/SKILL.md) | Design Read、艺术方向、反模板化、内容与视觉关系 |
| Page / Section 构图、Stack / Grid、宽度所有权、三端适配 | [`framer-layout-responsive`](../.agents/skills/framer-layout-responsive/SKILL.md) | Layout、Responsive、图片位置与裁切容器 |
| Styles、Component、Variant、Property、CMS、共享结构 | [`framer-components`](../.agents/skills/framer-components/SKILL.md) | Button、Navbar、Footer、卡片、可编辑内容系统 |
| Motion、Hover、Overlay、Lightbox、Cursor、Sticky 与高级装置 | [`framer-interactions`](../.agents/skills/framer-interactions/SKILL.md) | 原生交互选择、状态路由、Advanced Pattern |
| 只读审查、诊断、Preflight 或交付验收 | [`framer-qa`](../.agents/skills/framer-qa/SKILL.md) | Audit、回归、Pass / Fix Required / Blocked |

Link / Copy / Metadata / Naming 小修按被改对象的责任选 primary；复用现有合同，不因改 Property 值重建 Component 合同。纯 layout 诊断用 Layout；跨域只读验收用 QA。

完整网站任务也只选择当前实施 Part 的主要 Skill；Part 改变时重新 inspect / reconcile，再决定是否切换 primary Skill。

### Multi-domain primary-skill precedence

不要根据最显眼的表面特征过早路由。写入前先对当前可交付 Part 扫描：Page / Section composition、reusable Component contract、interaction state、breakpoint transformation、final QA。

- 新建、复制或重构可复用 Component 时，`framer-components` 优先；即使它同时是 Accordion、Hover Row 或 Responsive Card，也先确立 Definition / Instance / Breakpoint 责任。
- 已成立 Component 的合同不变，只修改 trigger、target、transition、Overlay 或 motion 时，才以 `framer-interactions` 为 primary。
- 不涉及可复用 Component 责任的 Page / Section 构图、Stack / Grid 或断点变换，以 `framer-layout-responsive` 为 primary。
- 其他命中域记为 secondary concerns，只读 task map 指向的小节或 Reference；不为一个组件人为切成四个并行 Skills。

新 Page、重大 Section 重构、多页面差异化，或以“换一种 / different layout”为主要目标时，先用 `design-taste` 编译 **Visual Direction Contract**，再切换到负责 Canvas 结构的一个 primary implementation Skill。这个前置方向阶段不等于同时加载两个建设 Skills；`design-taste` 决定 Preserve / Transform / Avoid、Sibling-page delta、Colour rhythm 与 Asset map，`framer-layout-responsive` 或其他 primary Skill 只实现已 Ready 的合同。

纯 Copy、Link、Metadata、命名或窄范围 breakpoint 修复不触发 Visual Direction Contract。已有多页项目的新页面若没有 sibling comparison，或“不同布局”只描述结构变化而没有保留的视觉系统，合同保持 `Draft`，不得开始 Canvas 写入。

当 primary 为 `framer-components` 且会建立或改写组件责任时，必须先通过其 **Component Requirement Contract**；当任务命中上述视觉方向范围时，必须先通过 **Visual Direction Contract**。读过 Baseline 不等于已将规则应用到当前对象。

无论选择哪个 primary，只要创建、保留或修改宽度约束，就读取 [Max-width ownership](basic/standards/website-baseline.md#max-width-ownership)，把父层是否封顶及批准来源写进现有合同；Component 路线不能跳过该规则。

## 3. Change Control 是写入前的条件路由

仅在以下情况读取 [`basic/workflows/change-control.md`](basic/workflows/change-control.md)：

- 用户提交会指导后续建设的长篇、多分点 Prompt。
- 同一个 Part、Component、Section 或交互进入第二轮及后续修改。
- 新反馈可能与先前要求、现有 Checklist 或已验证状态冲突。

长篇 Prompt 的逐字 Checklist 与确认 Gate 是实施前例外；普通小修、审阅、诊断或已确认 Part 不因此暂停。

Context Compaction 或 Session 恢复后，重新读取 official `$framer` Skill 及 task-map 行、当前 `PROJECT.md`、请求 Checklist、primary repo Skill，以及 active Component Requirement Contract / Visual Direction Contract；通过同一 session 的 targeted readback 确认后再续写，不从压缩摘要重建责任。

## 4. Implement 后再进入 Checklist / QA

Checklist 不是开工前的全量教材。完成一个明确 Part 后：

```text
完成实施
→ 打开 checklist.md 路由表
→ 只读当前 Part 对应章节
→ Targeted readback / 必要 Preview
→ Pass / Fix Required / Blocked
→ 批量修补并只复检受影响范围
→ 同步当前状态并完成 Workflow Observation closeout
```

- 实施后的 evaluator：[`checklist.md`](checklist.md) 与 `framer-qa`。
- 有实际建设结果或可复用失败的 Part，在最终回复前执行 [observation closeout](../history/workflow-observations/README.md#closeout)，包括 Partial / Blocked 的已实施结果；不等待用户提醒。
- Page / Website 报告完成前：读取 [`basic/workflows/preflight-audit.md`](basic/workflows/preflight-audit.md)。
- Marketplace 项目：在普通 Baseline 通过后追加 [`basic/standards/marketplace-guidelines.md`](basic/standards/marketplace-guidelines.md)。
- 图片或截图开始前：先读取 [`basic/workflows/image-workflow.md`](basic/workflows/image-workflow.md) 的视觉预算、驻留检查和失败降级。

## 5. Advanced Design

只有当前交互或组件确实命中高级装置时，才进入 [`advance-design/README.md`](advance-design/README.md) 选择一个 Pattern。项目精确参数是 provenance，不是全站默认值；Legacy 文档为零损保留，不作为新任务首选入口。
