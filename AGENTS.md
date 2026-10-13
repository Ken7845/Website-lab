# AGENTS.md

## 仓库角色

Website-lab 是个人网站与独立站的设计实验室、项目事实库与 Framer 交付知识库。Agent 是长期设计合作伙伴，但只处理用户当前放入 Scope 的项目、页面、组件、内容和文件。

**Do not preload the entire knowledge base.** 先判断任务类型，再读取最小必要入口；不要默认通读 `content-library`、`inspiration`、`.agents/skills` 或 `framer`。

## 权威优先级

按问题选择权威，不把“现在存在什么”误当成“允许改变什么”：

| 问题 | 权威 |
|---|---|
| 允许修改什么 | 用户当前明确授权与仍有效 Scope |
| 应实现什么方向 | 用户明确意图、active Decisions 与 Approved sources |
| 当前存在什么 | targeted Canvas / current implementation evidence |
| 可使用什么事实 | PROJECT 链接的 Approved sources 与事实状态 |
| 平台能做什么 | 当前官方能力与 hard constraints |
| 如何执行 | 本轮 selected Skill 与 canonical workflow；Inspiration / History 仅为参考 |

实际 Canvas 只证明“现在存在什么”，不自动授权改变方向；与批准方案不一致时记录差异并在 Scope 内协调。历史不得覆盖 current evidence 或 active 意图。

## 永久硬边界

- **Scope**：只修改用户授权范围及其必要共享依赖。发现需要改品牌定位、页面目标、信息架构或无关页面时暂停确认。
- **Facts**：地址、价格、营业时间、联系人、人员、产品事实、授权和法律内容不得编造。缺失项标记 `Missing`；演示内容标记 `Demo`。
- **User-authorized demo reference content**：当用户明确要求填充 Template 的空白内容时，网站前台不得保留“发布前补充”“等待验证”“未编造”等指示性文案。应改为完整、连贯的虚构参考内容：联系信息使用明显虚构的 `.example` 邮箱和保留的虚构电话号码；文章和案例可使用虚构故事来完成版面。内部资料仍必须标记为 `Demo`，不得把这类内容写成已验证事实，也不得虚构法律、许可、认证、保修、奖项、价格、统计、真实人员或真实地址。
- **Content**：优先使用用户内容和素材；新文案服从 Approved Brand Voice；不随意替换核心视觉。
- **Authorization**：删除正式内容、发布网站、引入付费依赖或 Custom Code、改变主要体验前必须确认。
- **Platform**：使用当前平台原生能力；不得为了套用 Skill 示例更换技术栈。
- **History**：历史资料用于解释过去，不作为 current state。聊天记录也不是唯一状态来源。

读取、审计、targeted readback 和其他可逆验证可以直接进行。用户已明确授权的局部修复，以及不改变方向的 Responsive、SEO、Alt、Link、命名和结构完善，可以直接完成并验证。

## Live Framer Canvas Gate

任何需要读取、审计或修改真实 Framer Canvas 的任务，必须按以下状态机进入；不得跳步：

所有 `npx @framer/agent@latest ...` CLI 命令在 sandbox 中都必须从第一次尝试就申请 **required elevated permissions**（network + skill / session file access）；不得先在默认 sandbox 中运行。权限拒绝或网络失败是环境 blocker，不是 Framer 能力缺失。

1. **Installed**：运行 `npx @framer/agent@latest setup` 并等待进程退出。只有命令成功退出且没有 setup error 才算完成；界面显示“setup”、Agent 声称“已 setup”、超时或错误输出都不算。
2. **Loaded**：加载 official `$framer` Skill，不以网页搜索或仓库 Skill 替代。
3. **Connected**：使用已确认的 Project URL / ID 运行 `npx @framer/agent@latest session new "<url-or-id>"`，成功取得 session ID；本轮后续命令复用该 session，不重复建立。
4. **Routed**：`session new` 才会刷新 `projects/<safeProjectId>/index.md`。读取其 `Anything` 行、当前任务对应行及它们明确指向的少量文件，再选择一个 primary repository Skill。
5. **Verified**：修改前先通过 `npx @framer/agent@latest exec -s <sessionId>` 与 `framer.agent.*` 做一次 targeted live-tree readback；后续官方 CLI 命令必须复用同一 session。

上述任一状态报错、超时、无输出或缺少必需证据时，**Gate remains closed**：先诊断或报告准确 blocker，不得继续 Canvas 判断或自行改用 UI。仓库内的 `framer-layout-responsive`、`framer-components`、`framer-interactions` 与 `framer-qa` 只负责判断方法，不提供 Canvas 连接，也不能替代官方 `$framer` Skill。不得把搜索 Framer 官网、Browser / Playwright / Computer Use 或对编辑器 DOM 的观察表述为“已读取 Framer Skill”或“Framer Agent 已验证”。只有当官方 task map / docs 已证实精确能力缺口，且用户在获知 blocker 后明确授权，才可采用 UI fallback；Agent 不得自行授权。

正式实施前必须向用户显示一行 **Framer Agent gate receipt**：`setup OK / session connected / task-map <row> / live readback OK`。不展示 session ID 或内部节点 ID；任一项不是 OK 就不能声称已连接 Framer Agent。

纯仓库文档、规划或知识维护不连接 Canvas，也不运行 setup。未经可追踪的 Framer Agent targeted readback，不得把 Canvas 判断写成 Verified current state。

## 最小读取路径

1. 先读本文件。
2. 有具体项目时读 `content-library/<project>/PROJECT.md`；只跟随其中与当前 Scope 相关的链接。
3. 再按任务选择：

| 任务 | 追加读取 |
|---|---|
| 品牌、事实、文案、素材 | PROJECT 链接的 Approved sources |
| 平台无关的视觉方向 | [design-taste](.agents/skills/design-taste/SKILL.md) 与必要 Inspiration |
| Framer 规划、Canvas、Component、Layout、Interaction、QA | [唯一 Framer dispatcher](framer/README.md)；先按 mode 与 multi-domain precedence 路由，再读一个 primary Skill |
| 知识审计、修订、迁移、Router / Skill 修改 | [knowledge-maintenance](.agents/skills/knowledge-maintenance/SKILL.md)；不连接 Canvas |

Framer dispatcher 是 Skill 选择的唯一 owner，即使用户点名 Skill 也先扫描 Component / Layout / Interaction 责任。Skill 列表不是平行 dispatcher。图片、连续修改、高级模式与 evaluator 的 conditional references 由 dispatcher / selected Skill 路由。

旧项目没有 PROJECT 时从 [manifest template](content-library/project-manifest-template.md) 建立最小入口；未知实现标 Needs refresh。Context 压缩或 Session 恢复按 [Framer re-entry](framer/README.md#3-change-control-是写入前的条件路由) 重读 active 来源与合同；通过同一有效 session targeted readback 重建证据，旧 session 失效时遵守官方重连流程，不靠摘要续写。

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

建设类长篇 Prompt 的逐字记录、页面与请求 Checklist 分层、约束锁及确认规则由 [change-control](framer/basic/workflows/change-control.md#authorization-and-task-mode) 唯一维护。未经批准的建设合同先回读并等待确认；用户已经明确授权原 Scope 时不为记录或派生合同再次询问。新方向、破坏性变更和发布仍须相应授权。用户拒绝项目级 Checklist 时不擅自创建。知识审计、小修、诊断和已确认 Part 的连续执行不触发新的开工 Gate。

## 当前状态与交付

`PROJECT.md`、`STATUS.md` 和 `RECOVERY.md` 只保存覆盖式 current state；更新当前值时替换旧状态，不追加过程流水。持久决策进入 `DECISIONS.md`，关闭的 Prompt、handoff 和旧快照进入 `HISTORY.md` / `history/`。

Framer 的建设顺序、Responsive、Accessibility、交互、Part 验收和 Preflight 从 `framer/README.md` 路由到对应 Skill、Reference 与 `framer/checklist.md`，不在本文件重复。完成报告只说明最终改动、选择理由、验证范围和已知限制，不倾倒内部节点 ID 或完整工具输出。

## 轻量 Workflow Observation

完成有实际建设价值的 Page、Section、Component、Interaction 或跨断点 Part 后，在不影响实施和 QA 的前提下，按 [`history/workflow-observations/README.md`](history/workflow-observations/README.md) 追加一条简短 observation。记录用户要求、实际 route、完成内容、验证结果和后来发现的遗漏；只写可核对事实，不写逐步日记、完整聊天、内部推理、节点倾倒或原始工具输出。

- 小型文案、链接、命名、单点 spacing 等普通修复默认不记录；若它暴露了可复用的 workflow failure 才记录。
- Observation 以项目分类：每个项目只维护一个 append-only 文件；同一任务中的多条 Prompt 合并为一条简短 closing entry，不按 Prompt 建文件或逐条记录。
- Observation 在实施与 targeted QA 后写入，不是新的开工 Gate，不得暂停建设等待日志，也不得为了日志扩大读取范围。
- 最终回复前按 [closeout](history/workflow-observations/README.md#closeout) 写入并回读适用记录与 Current Status receipt；Partial / Blocked 的已实施结果同样适用，不等待用户提醒，不用其他 workspace 的笔记替代。
- 任务当下只写短记录；后来发现问题时追加 `Later-discovered issue` 与 correction，不改写原始事实。
- 普通建设不得预读 observations；只有 retrospective 或 knowledge-maintenance 才按项目、时间或失败类型 targeted read。
- 单条记录只是 evidence，不自动升级为规则。只有重复模式或高影响缺陷经复盘后，才修改 Router、Skill、Reference 或 validator。

## 文件管理

- 普通文件和文件夹使用 kebab-case；`README.md`、`AGENTS.md`、`PROJECT.md` 等正式入口保留约定大写。
- 规则放在最接近适用任务的位置；不要创建职责重复的规则文件。
- 整理回 `content-library` 时只保留 current 事实、最终内容、对应素材和清晰本地链接；过程记录按职责进入 Decisions 或 History。
