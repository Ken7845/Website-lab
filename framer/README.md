# Framer 工作路由

本目录是仓库内 Framer 工作的唯一入口。先检查并协调当前状态，再选择一个主要仓库 Skill；不要把全部 Skills、Checklist 和 references 同时预读。

## 1. 先 Inspect / Reconcile

任何写入前先确认：

1. 当前任务的项目、页面、Part、授权范围和明确不做的内容。
2. 当前项目 `content-library/<project>/PROJECT.md`。只有任务正在恢复中断状态时再读 `RECOVERY.md`；只有用户指定了现有 Part 合同时再读对应页面 / 请求 Checklist。
3. 用户本轮要求是新增、校正还是明确覆盖旧要求；连续修改按 [`basic/workflows/change-control.md`](basic/workflows/change-control.md) 建立约束锁。
4. 当前真实结构与最后成功状态；中断任务先恢复，不根据聊天记忆重做。
5. 任务是否需要连接 Framer Canvas。只在需要真实 Framer 连接时，先运行官方要求的 `npx @framer/agent@latest setup`，完成后再加载已安装的官方 `framer` Skill。仓库不再维护平行的 `agent-connection.md`。

官方 `framer` Skill 负责平台连接与能力入口，不计入下面的“一个主要仓库 Skill”。

## 2. 只选一个 Primary Repo Skill

按本轮主要判断选择一个；其他领域通过 [`basic/README.md`](basic/README.md) 按需读取 reference，不再同时加载第二个建设 Skill。

| 主要任务 | Primary repo Skill | 典型范围 |
|---|---|---|
| 品牌方向、叙事、参考转译、视觉审阅 | [`design-taste`](../.agents/skills/design-taste/SKILL.md) | Design Read、艺术方向、反模板化、内容与视觉关系 |
| Page / Section 构图、Stack / Grid、宽度所有权、三端适配 | [`framer-layout-responsive`](../.agents/skills/framer-layout-responsive/SKILL.md) | Layout、Responsive、图片位置与裁切容器 |
| Styles、Component、Variant、Property、CMS、共享结构 | [`framer-components`](../.agents/skills/framer-components/SKILL.md) | Button、Navbar、Footer、卡片、可编辑内容系统 |
| Motion、Hover、Overlay、Lightbox、Cursor、Sticky 与高级装置 | [`framer-interactions`](../.agents/skills/framer-interactions/SKILL.md) | 原生交互选择、状态路由、Advanced Pattern |
| 只读审查、诊断、Preflight 或交付验收 | [`framer-qa`](../.agents/skills/framer-qa/SKILL.md) | Audit、回归、Pass / Fix Required / Blocked |

完整网站任务也只选择当前实施 Part 的主要 Skill；Part 改变时重新 inspect / reconcile，再决定是否切换 primary Skill。

## 3. Change Control 是写入前的条件路由

仅在以下情况读取 [`basic/workflows/change-control.md`](basic/workflows/change-control.md)：

- 用户提交会指导后续建设的长篇、多分点 Prompt。
- 同一个 Part、Component、Section 或交互进入第二轮及后续修改。
- 新反馈可能与先前要求、现有 Checklist 或已验证状态冲突。

长篇 Prompt 的逐字 Checklist 与确认 Gate 是实施前例外；普通小修、审阅、诊断或已确认 Part 不因此暂停。

## 4. Implement 后再进入 Checklist / QA

Checklist 不是开工前的全量教材。完成一个明确 Part 后：

```text
完成实施
→ 打开 checklist.md 路由表
→ 只读当前 Part 对应章节
→ Targeted readback / 必要 Preview
→ Pass / Fix Required / Blocked
→ 批量修补并只复检受影响范围
```

- 实施后的 evaluator：[`checklist.md`](checklist.md) 与 `framer-qa`。
- Page / Website 报告完成前：读取 [`basic/workflows/preflight-audit.md`](basic/workflows/preflight-audit.md)。
- Marketplace 项目：在普通 Baseline 通过后追加 [`basic/standards/marketplace-guidelines.md`](basic/standards/marketplace-guidelines.md)。
- 图片或截图开始前：先读取 [`basic/workflows/image-workflow.md`](basic/workflows/image-workflow.md) 的视觉预算、驻留检查和失败降级。

## 5. Advanced Design

只有当前交互或组件确实命中高级装置时，才进入 [`advance-design/README.md`](advance-design/README.md) 选择一个 Pattern。项目精确参数是 provenance，不是全站默认值；Legacy 文档为零损保留，不作为新任务首选入口。
