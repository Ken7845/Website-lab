# AGENTS.md

## 仓库角色

Website-lab 是个人网站与独立站的设计实验室、项目事实库与 Framer 交付知识库。Agent 是长期设计合作伙伴，但只处理用户当前放入 Scope 的项目、页面、组件、内容和文件。

**Do not preload the entire knowledge base.** 先判断任务类型，再读取最小必要入口；不要默认通读 `content-library`、`inspiration`、`.agents/skills` 或 `framer`。

## 权威优先级

信息冲突时按以下顺序判断：

1. 用户当前明确要求
2. 实际 Canvas / current implementation
3. 当前 `PROJECT.md` 与其链接的 Approved sources
4. 当前平台的 hard constraints
5. 本轮 selected Skill
6. 相关 `inspiration`
7. `HISTORY.md`、`history/` 和其他历史记录

实际 Canvas 只证明“现在存在什么”，不自动授权改变方向；若它与批准方案不一致，先记录差异，再按 Scope 修复或向用户确认。低优先级资料不得静默覆盖高优先级事实和决定。

## 永久硬边界

- **Scope**：只修改用户授权范围及其必要共享依赖。发现需要改品牌定位、页面目标、信息架构或无关页面时暂停确认。
- **Facts**：地址、价格、营业时间、联系人、人员、产品事实、授权和法律内容不得编造。缺失项标记 `Missing`；演示内容标记 `Demo`。
- **Content**：优先使用用户内容和素材；新文案服从 Approved Brand Voice；不随意替换核心视觉。
- **Authorization**：删除正式内容、发布网站、引入付费依赖或 Custom Code、改变主要体验前必须确认。
- **Platform**：使用当前平台原生能力；不得为了套用 Skill 示例更换技术栈。
- **History**：历史资料用于解释过去，不作为 current state。聊天记录也不是唯一状态来源。

读取、审计、targeted readback 和其他可逆验证可以直接进行。用户已明确授权的局部修复，以及不改变方向的 Responsive、SEO、Alt、Link、命名和结构完善，可以直接完成并验证。

## 最小读取路径

1. 先读本文件。
2. 有具体项目时读 `content-library/<project>/PROJECT.md`；只跟随其中与当前 Scope 相关的链接。
3. 再按任务选择：

| 任务 | 追加读取 |
|---|---|
| 品牌、事实、文案、素材 | `PROJECT.md` 链接的 Approved sources |
| 设计方向与反模板化 | 本轮明确相关的 `.agents/skills/design-taste/SKILL.md` 与少量 Inspiration |
| Framer Section / Page 布局与断点 | `.agents/skills/framer-layout-responsive/SKILL.md` |
| Framer Component / Variant / Property / shared system | `.agents/skills/framer-components/SKILL.md` |
| Framer motion / Overlay / Lightbox / Hover | `.agents/skills/framer-interactions/SKILL.md` |
| 已完成范围的 QA / Preflight | `.agents/skills/framer-qa/SKILL.md`，再按其路由读取当前 Part Checklist |
| 图片或视觉审阅 | `framer/basic/workflows/image-workflow.md` |
| 连续修改、长 Prompt、需求锁 | `framer/basic/workflows/change-control.md` |
| 高级组件模式 | `framer/advance-design/` 中与当前项目或模式直接相关的文件 |
| 知识新增、迁移、去重、Skill / Router 修改 | `.agents/skills/knowledge-maintenance/SKILL.md` |

普通小范围 Framer 任务通常只需本文件、当前 `PROJECT.md` 和一个 primary Skill；只有 Skill 明确路由时才追加详细 Reference。任务类型不清楚时再读 `framer/README.md`。旧项目没有 `PROJECT.md` 时，先用 `content-library/project-manifest-template.md` 建立入口并标记未知事实。Context 压缩或 Session 恢复后，重新读取当前 Part 的 PROJECT、变更控制和 Checklist 路由，不靠记忆续写。

知识维护任务完成前运行 `knowledge-maintenance` 的 strict validator；不得用扩大排除范围或删除精确证据换取通过。

## 写入前：Add / Reuse / Modify / No-op

创建任何页面、Section、Component、Variant、Style、文件或规则前，先检查目标是否已经存在，并明确选择：

- **Add**：不存在等价项，且当前 Scope 确实需要新增。
- **Reuse**：已有结构可以原样复用。
- **Modify**：已有结构职责正确，只需在原处调整。
- **No-op**：当前状态已满足要求，不做重复写入。

不得用新副本绕过不确定状态。工具超时或无输出时先 read back；同类修改批量完成，随后只验证受影响范围。

同一 Part 的第二轮及后续修改，先回顾该 Part 自开始以来的用户要求，锁定仍有效目标、追加要求、本轮变化、禁止改动范围和必须验证的断点/状态。新反馈默认是补充或校正，除非用户明确要求覆盖旧方向。

## 长篇 Prompt Gate

长篇、多分点 Prompt 若会指导后续 Canvas、页面、组件、素材、排版、交互或多轮建设，在任何正式建设写入前必须执行 [change-control.md](framer/basic/workflows/change-control.md)：

- 页面长期 Checklist 与本次请求 Checklist 分开；不建立平行聊天日志或 `checklist-2`。
- 将用户每一条原始要求逐字写入语义明确的请求文件；可追加验收项，但不得省略、合并或削弱原话。
- 写入后回读，向用户说明已记录范围并等待明确确认；确认前不开始正式建设。
- 用户已明确要求创建时不重复询问；用户明确拒绝项目级 Checklist 时不擅自创建。小修、诊断、审阅和现有 Checklist Part 的连续执行不触发新建。

## 当前状态与交付

`PROJECT.md`、`STATUS.md` 和 `RECOVERY.md` 只保存覆盖式 current state；更新当前值时替换旧状态，不追加过程流水。持久决策进入 `DECISIONS.md`，关闭的 Prompt、handoff 和旧快照进入 `HISTORY.md` / `history/`。

Framer 的建设顺序、Responsive、Accessibility、交互、Part 验收和 Preflight 从 `framer/README.md` 路由到对应 Skill、Reference 与 `framer/checklist.md`，不在本文件重复。完成报告只说明最终改动、选择理由、验证范围和已知限制，不倾倒内部节点 ID 或完整工具输出。

## 文件管理

- 普通文件和文件夹使用 kebab-case；`README.md`、`AGENTS.md`、`PROJECT.md` 等正式入口保留约定大写。
- 规则放在最接近适用任务的位置；不要创建职责重复的规则文件。
- 整理回 `content-library` 时只保留 current 事实、最终内容、对应素材和清晰本地链接；过程记录按职责进入 Decisions 或 History。
