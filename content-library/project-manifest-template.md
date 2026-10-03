# Project Manifest Template

复制到 `content-library/<project-name>/PROJECT.md` 后填写。删除说明性占位内容；未知事实标为 `Missing`，不要为了完整而猜测。

PROJECT 是 current manifest 与资料地图。默认可内嵌 Current Status、Decisions 和 Recovery；项目变复杂后可拆到 `STATUS.md`、`DECISIONS.md`、`RECOVERY.md`，但不得同时维护两份明细。

## Current ownership metadata

- State schema: 1
- Current status owner: [Inline Status](#12-current-status)
- Recovery owner: [Inline Recovery](#14-recovery)

## 1. Project Identity

- Project name:
- Platform:
- Project type: Brand Site / Portfolio / Landing Page / Marketplace Template / Other
- Overall status: Planning / Building / QA / Ready / Published
- Project / Canvas URL:
- Demo URL:
- Content status: Approved / Draft / Mixed / Demo
- Last updated:
- Last verified against current implementation:

## 2. Scope and Authority

- Current scope:
- Explicit non-goals:
- Primary page / component:
- User-approved direction:
- Current implementation differences:
- Items requiring confirmation:

冲突时使用仓库 `AGENTS.md` 的优先级。实际 Canvas / current implementation 记录“当前存在什么”；Approved sources 记录事实与批准方向。

## 3. Knowledge Map

| Responsibility | Current source | Status |
|---|---|---|
| Brand Voice |  | Approved / Draft / Missing |
| Style Guide |  |  |
| Formal Content |  |  |
| Assets |  |  |
| Inspiration |  |  |
| Current Status | Inline §12 / `STATUS.md` |  |
| Decisions | Inline §13 / `DECISIONS.md` |  |
| Recovery | Inline §14 / `RECOVERY.md` |  |
| Checklist index |  | Not created / Active / Complete |
| History index | `HISTORY.md` / `history/` |  |

如果职责已拆到独立文件，本文件只保留摘要和链接。

## 4. Website Goal

- 网站为谁服务？
- 用户进入后需要理解什么？
- 最重要的实际结果：
- Primary CTA:
- Secondary CTA:
- Success evidence:

## 5. Target User

- Primary audience:
- User intent:
- Important questions:
- Trust requirements:
- Device priority: Desktop / Phone / Balanced

## 6. Brand Direction

- Brand personality:
- Core concept:
- Visual memory point:
- Typography direction:
- Color direction:
- Image strategy:
- Motion character:
- Avoid:

具体规范链接到 Brand Voice / Style Guide，不在这里复制全文。

## 7. Content Facts

| Fact | Value | Source | Status |
|---|---|---|---|
| Address |  |  | Approved / Draft / Missing / Demo |
| Phone |  |  |  |
| Email |  |  |  |
| Opening hours |  |  |  |
| Social links |  |  |  |
| Prices |  |  |  |
| Legal / copyright |  |  |  |

Missing 事实不得根据视觉需要补写；Demo 事实必须在最终展示中保留声明。

## 8. Sitemap and Page Goals

| Page | Path | User goal | Primary CTA | Content source | Current status |
|---|---|---|---|---|---|
| Home | `/` |  |  |  | Planned |

每个页面必须有独立目的；不因“网站通常有这个页面”而新增。

## 9. Narrative and Conversion

| Page | Section / Part | Purpose | Content source | Image role | CTA / next step |
|---|---|---|---|---|---|
| Home | Hero |  |  |  |  |

Primary path:

```text
Landing
→ Understand
→ Evidence / content
→ CTA
→ Contact / Visit / Buy / Book
```

- Phone:
- Email:
- Map:
- Social:
- Form / booking / purchase:

### Page Visual Identity

本表只保存当前批准的页面身份与页面间差异；完整合同与判断方法由 `.agents/skills/design-taste/SKILL.md` 和页面 Checklist 中的 `Visual Direction Contract` 负责。

| Page | Visual memory point | Dominant composition | Colour rhythm | Sibling difference | Status |
|---|---|---|---|---|---|
| Home |  |  |  |  | Draft / Approved / Fix Required |

## 10. System and Platform Plan

- Platform router:
- Selected Skills:
- Text / Color Style source:
- Shared Components:
- CMS decision:
- Navbar / Footer:
- Links and semantics:
- Accessibility / Focus:
- Third-party dependency:
- Custom Code: No / Proposed / Approved

Framer 项目从 `../../framer/basic/README.md` 路由；不要在 PROJECT 复制平台 Baseline。

## 11. Responsive, Interaction and Assets

| Area | Desktop | Tablet | Phone |
|---|---|---|---|
| Navbar |  |  |  |
| Hero |  |  |  |
| Main layout |  |  |  |
| Footer |  |  |  |
| Special interaction |  |  |  |

- Required test widths:
- Page / section enter:
- Hover / pressed:
- Overlay / Lightbox:
- Reduced Motion:
- Source asset folder:
- Web output folder:
- Hero / gallery assets:
- Missing assets:
- License status:

### Asset Usage Ledger

本表只保存当前素材分配与使用事实；选图、复用理由、裁切和视觉预算规则由 [image-workflow.md](../framer/basic/workflows/image-workflow.md) 负责。

| Asset | Narrative qualities | Approved role | Current use | Reuse decision / reason | Crop / focal notes | Status |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  | Candidate / Allocated / Used / Reassigned / Blocked |

图片工作遵循 [image-workflow.md](../framer/basic/workflows/image-workflow.md)。

## 12. Current Status

- State revision: YYYY-MM-DD
- Active request: None — replace with the authorized request link when one exists.

本节为覆盖式 current state。若使用 `STATUS.md`，这里只写摘要、最后验证时间和链接。

- Current phase:
- Active page / component:
- Current blockers:
- Next approved step:
- Last verified:

| Page | Content | Styles | Components | Links | SEO | Alt | Desktop | Tablet | Phone | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| Home | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |

旧状态被新状态替换，不在本节追加日期流水。

## 13. Decisions and Exceptions

只记录会持续影响未来工作的批准决定。若使用 `DECISIONS.md`，本节只保留 active 摘要和链接。

| Decision | Reason | Scope | Status | Date | Supersedes |
|---|---|---|---|---|---|
|  |  |  | Active / Superseded |  |  |

普通微调和工具调用不进入 Decisions。

## 14. Recovery

- State revision: YYYY-MM-DD
- Active request: None — must match the Status pointer.
- State reference: [Current Status](#12-current-status)

本节永远只保留一个最新 checkpoint。若使用 `RECOVERY.md`，这里只保留链接和更新时间。

- Active session / connection:
- Current page / component:
- Last successful change:
- Last targeted readback:
- Verified breakpoints / states:
- Remaining approved work:
- Exact next action:
- Important local asset paths:
- Updated at:

新 checkpoint 覆盖旧 checkpoint。需要长期追溯的旧 handoff 才移入 History。

## 15. Checklist and Change Control

- Project checklist index:
- Active page checklist:
- Active request checklist:
- Checklist status: Not created / In progress / Pass / Blocked
- Last synchronization with Current Status:

长篇、多分点 Prompt 的逐字记录、确认 Gate、页面长期/请求 Checklist 分层，以及连续修改约束锁，遵循 [change-control.md](../framer/basic/workflows/change-control.md)。Checklist 状态必须与 §12 或 `STATUS.md` 同步。

## 16. History

- History index:
- Closed prompt / handoff records:
- Superseded plans worth retaining:

History 只解释过去，不控制 current work。普通版本变化由 Git 保存，不为每次编辑复制快照。

## 17. Definition of Ready

- [ ] 当前 Scope 与 non-goals 明确。
- [ ] 网站目标、目标用户和页面目的明确。
- [ ] Primary CTA 与转化路径明确。
- [ ] 品牌方向和必要 Inspiration 明确。
- [ ] 正式事实有来源与状态；Missing 未被猜测填充。
- [ ] 主要内容和素材足以开始，或阻塞已明确。
- [ ] 当前实现差异与需要确认的选择已记录。
- [ ] Checklist / change-control 需求已判定。

未通过 Ready 时可以做只读审计与结构探索，但不能把猜测写成正式事实或完成状态。
