# Website-lab

Website-lab 是面向人类与 AI Agent 的网站设计、项目事实和 Framer 交付知识库。它的目标不是让 Agent 阅读更多，而是让每类信息只有一个权威位置，使网站在中断、换 Session 或多轮修改后仍能被准确接续。

## Knowledge Base Version

- Repository version: `Website_Lab_V2.1.0`
- Current release: `v2.1.0`
- Architecture base: `v2.0.0`
- Released: 2026-09-16
- Updated: 2026-10-03
- Scope: adds the Visual Direction Contract, page/asset identity persistence, symmetric structural/visual QA and machine-checkable contract integrity while preserving the v2 routing and progressive-disclosure architecture.
- Current revision: adds lightweight workflow observations for later retrospective improvement without adding them to normal task context.
- Migration record: [Website-lab Visual Workflow Improvement — v2.1.0](history/repository/2026-09-16-visual-workflow-v2.1.0.md)

## 架构

```text
AGENTS.md
├── 仓库级优先级、最小读取路由与永久硬边界
├── .knowledge-validation.json    不可变归档、迁移与验证策略
├── .agents/skills/
│   ├── design-taste/             平台无关的设计判断
│   ├── framer-*/                 按任务选择的 Framer Skills
│   └── knowledge-maintenance/    仅在知识写入、迁移与验证时触发
├── content-library/
│   ├── README.md                 项目知识职责
│   ├── project-manifest-template.md
│   └── <project>/PROJECT.md      每个项目的唯一入口
├── inspiration/
│   └── 按网站类型保存创意参考，不保存 current 项目状态
├── history/                       退役手册、迁移证据与 workflow observations；默认不读
└── framer/
    ├── README.md                唯一 Framer task router
    ├── basic/                    稳定的平台标准、Patterns 与 Workflows
    ├── checklist.md              Part / Page / Website 验收
    └── advance-design/           已验证的项目级高级模式
```

## 信息所有权

| 信息 | 权威位置 | 不承担的职责 |
|---|---|---|
| 仓库路由、授权、事实边界 | `AGENTS.md` | 不复制 Framer 实施手册 |
| 项目目标、Scope、事实与资料索引 | `content-library/<project>/PROJECT.md` | 不保存长篇过程流水 |
| 当前建设状态 | 项目 `STATUS.md` 或 PROJECT 的 Current Status | 不保存旧状态时间线 |
| 持久设计决定与真实例外 | 项目 `DECISIONS.md` 或 PROJECT 的 Decisions | 不记录每次小操作 |
| 当前恢复点 | 项目 `RECOVERY.md` 或 PROJECT 的 Recovery | 只保留一个最新 checkpoint |
| 已关闭的 Prompt、handoff、旧快照 | 项目 `HISTORY.md` / `history/` | 不覆盖 current state |
| 已批准的逐页与请求合同 | 项目 `checklist/` | 不替代 PROJECT 或平台验收 |
| 品牌事实、正式文案与素材 | PROJECT 链接的 Approved sources | 不从 Inspiration 推断事实 |
| 基础设计判断 | `.agents/skills/design-taste/SKILL.md` | 不替代品牌或平台约束 |
| Framer 实施与验收 | `framer/basic/`、`framer/checklist.md`、选中的 Framer Skill | 不决定品牌事实 |
| 创意参考 | `inspiration/` | 不保存项目 current status |
| 退役的仓库级手册 | `history/` | 不参与 current 路由或覆盖现行规则 |
| 真实建设过程的轻量观测 | `history/workflow-observations/` | 不作为 current state、Recovery 或普通任务启动上下文 |
| 知识新增、迁移与结构验证 | `.agents/skills/knowledge-maintenance/`、`.knowledge-validation.json` | 不参与普通网站任务 |

若信息冲突，以 `AGENTS.md` 的权威优先级为准。

## 开始或更新一个项目

1. 在 `content-library/<project-name>/` 创建或更新 `PROJECT.md`。
2. 新项目从 `content-library/project-manifest-template.md` 开始。
3. 提供网站目标、目标用户、页面与 CTA、品牌方向、事实、文案、素材和参考。
4. 将未知事实标为 `Missing`，演示事实标为 `Demo`；不要为了资料完整而猜测。
5. 大项目总览或长篇多分点建设要求按 `framer/basic/workflows/change-control.md` 决定 PROJECT、Checklist 和请求记录。
6. 当前状态持续覆盖更新；旧 Prompt、handoff 和有长期价值的快照再进入 History。

## Current 与 History

`PROJECT.md`、`STATUS.md` 和 `RECOVERY.md` 回答“现在是什么、做到哪里、下一步是什么”。更新时替换旧值，不向文件尾部追加聊天式日志。

`DECISIONS.md` 保存仍会影响未来工作的决定，并把被替代项标记为 `Superseded`。`HISTORY.md` 与 `history/` 保存已经结束且值得追溯的材料。普通版本变化由 Git 负责，不需要为每个旧版本建立副本。

## Workflow Observations

有实际建设价值的 Framer / 网站任务在实施与 targeted QA 完成后，可以自然地写入一条简短 workflow observation：记录用户要求、Agent 选择的 route、实际完成内容、验证结果，以及后来发现的遗漏。它用于阶段性复盘和改进 Router / Skill / Reference，不用于证明 current state。

这不是工作日志压力：小型文案、链接、命名或单点 spacing 修复默认不记录；建设中不维护逐步日记；单次记录不复制聊天、工具输出或内部推理。每个项目只维护一个简短的 append-only observation 文件，同一任务的多条 Prompt 合并为一条 closing entry。Observations 位于 [`history/workflow-observations/`](history/workflow-observations/README.md)，普通任务不得预读，只有 retrospective 或 knowledge-maintenance 才按需读取。

## Agent 如何使用本仓库

Agent 从 `AGENTS.md` 开始，只读取当前 Scope 必要的 PROJECT、Approved sources、平台规则和 selected Skill。README 只解释架构，不是另一份执行手册。

Framer 的完成标准与执行细节由以下入口管理：

- `framer/README.md`
- `.agents/skills/framer-*/SKILL.md`
- `framer/basic/README.md`
- `framer/checklist.md`
- `framer/basic/workflows/change-control.md`
- `framer/basic/workflows/preflight-audit.md`

## 知识写入验证

新增、移动、去重或重构 Basic、Advanced Design、项目状态、Router 或 Skill 时，使用 `knowledge-maintenance`，并在完成前运行：

```bash
python3 .agents/skills/knowledge-maintenance/scripts/validate_repository.py --strict
```

验证器检查 active links / anchors、Skill metadata、旧路由、索引覆盖、不可变归档、全库关键词与 canonical 文件中的精确知识契约、current/history 卫生、Markdown 删除迁移目标和 `git diff HEAD --check`。普通网站建设不预读这套维护上下文。

## 核心目标

交付必须同时满足品牌与真实内容、可维护结构、Desktop / Tablet / Phone、必要交互、语义与可访问性。知识库本身也必须可维护：当前状态清楚、历史不冒充事实、下一位 Agent 不需要重新拼接聊天记录。
