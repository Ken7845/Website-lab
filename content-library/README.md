# Content Library

`content-library` 保存每个网站项目的 current 事实、品牌、正式内容、素材、执行合同和恢复状态。聊天记录、Inspiration 和历史 handoff 都不能代替项目入口。

## Git tracking boundary

Only this guide and `project-manifest-template.md` are tracked in the main Website_Lab Git repository. Every `content-library/<project>/` directory is a local-only working area containing project facts, current state, contracts, history, and assets; those directories are intentionally excluded from GitHub.

This boundary changes distribution, not routing. Local project work still begins at `content-library/<project>/PROJECT.md`. A missing project directory in a fresh clone does not mean that the project never existed and must never be filled by inference: restore it from the separate local backup or ask the user for the authoritative project sources.

Git is not the backup for local-only project data. Before deleting, moving, replacing, or migrating a project directory, verify that a separate recoverable backup exists. A new computer or clean clone must restore project directories separately before project work begins.

## 唯一入口

每个项目必须有：

```text
content-library/<project-name>/PROJECT.md
```

新项目从 `project-manifest-template.md` 创建。`PROJECT.md` 是项目的 current manifest 与资料索引，不是把所有内容复制到一个文件的笔记本。

## 推荐结构

```text
<project-name>/
├── PROJECT.md
├── STATUS.md
├── DECISIONS.md
├── RECOVERY.md
├── HISTORY.md
├── BRAND_VOICE.md
├── STYLE_GUIDE.md
├── CONTENT.md
├── checklist/
├── history/
├── images/
└── references/
```

小项目可以把 STATUS、DECISIONS 和 RECOVERY 作为 `PROJECT.md` 内的明确章节；一旦拆成独立文件，PROJECT 只保留 current 摘要和链接，不再维护第二份明细。

## 文件职责

| 文件或目录 | 负责 | 更新方式 |
|---|---|---|
| `PROJECT.md` | 当前目标、Scope、页面、事实摘要、权威资料地图 | 覆盖式更新 current 值 |
| `STATUS.md` | 当前 Build Status Matrix、阻塞、当前阶段与下一步 | 旧状态被新状态替换 |
| `DECISIONS.md` | 会持续影响未来工作的批准决定和真实例外 | 保留决定；被替代时标 `Superseded` |
| `RECOVERY.md` | 当前 Session、目标 Part、最后成功动作、已验证范围、下一动作 | 永远只保留最新 checkpoint |
| `HISTORY.md` | 历史索引和必要背景 | 只链接已关闭记录，不声明 current truth |
| `history/` | 已关闭 Prompt、handoff、旧计划和有复用价值的快照 | 使用日期与语义名称，默认不预读 |
| `checklist/` | 已批准的页面长期合同与请求级工作合同 | 状态必须与 STATUS / PROJECT 同步 |
| `BRAND_VOICE.md` | 语气、词汇、禁用表达和示例 | Approved 内容优先 |
| `STYLE_GUIDE.md` | 项目视觉方向 | 不替代平台 Baseline |
| `CONTENT.md` | 已审核文案与结构化事实 | 每项标明事实状态 |
| `images/` | 原始素材和明确命名的网页输出 | 原图与输出分开，不静默覆盖 |
| `references/` | 当前项目特定参考 | 不替代类型级 `inspiration` |

## Current 状态必须覆盖更新

- PROJECT、STATUS 和 RECOVERY 只回答当前状态。更新时修改原字段，不在文件尾部累积每日过程。
- 当前值变化前，只有仍会影响未来工作的理由进入 DECISIONS。
- 已结束的原始 Prompt、handoff 或旧快照只有具备追溯价值时才进入 HISTORY；普通版本变化由 Git 保存。
- HISTORY 不参与默认读取，也不得覆盖 Approved source、Canvas readback 或 current PROJECT。
- Checklist 中的页面/Part 状态与 STATUS / PROJECT 不一致时，先通过 targeted readback 查明实际状态，再同步 current 文件。

## Checklist 边界

- 页面长期 Checklist 与某次长篇 Prompt 的请求 Checklist 必须分开。
- Checklist 只保存已批准的执行合同，不保存聊天转录。
- 长篇 Prompt 的逐字记录、确认 Gate、连续修改约束锁和目录规则见 `../framer/basic/workflows/change-control.md`。
- 项目没有触发 Checklist 时，在 PROJECT 中写 `Not created / Not required`，不创建空目录。

## 事实状态

- `Approved`：可以直接用于正式交付。
- `Draft`：可用于设计，发布前仍需审核。
- `Missing`：不得猜测，需要用户提供。
- `Demo`：虚构演示内容，必须保留声明。
- `Superseded`：曾经有效、已被新决定替代，不再控制 current work。

地址、价格、营业时间、人员、联系方式、产品事实、版权和授权必须有来源与状态。

## 旧项目兼容

旧项目没有 `PROJECT.md` 时：

1. 只读取现有 brief、prompt、info、品牌和 TODO 中与当前 Scope 相关的部分。
2. 用模板建立 PROJECT，并把不确定内容标为 `Missing`。
3. 通过实际 Canvas / current implementation 回读当前建设状态。
4. 把仍有效资料链接到 PROJECT；已关闭材料归入 History。
5. 后续任务统一从 PROJECT 进入，不再每次重新拼接旧文件。

## Current state contract

Every current PROJECT declares `State schema: 1`, a linked `Current status owner` and `Recovery owner`. Owners may be inline headings or split files. This metadata points to existing current knowledge; it is not a second state store.

Status and Recovery contain the same `State revision` and compact `Active request` pointer (a valid link, or `None — reason`). Status owns results, blockers and the next approved step. Recovery owns connection re-entry and links to Status through `State reference`; it does not copy blocker inventories or earlier image plans. Bump the revision and synchronize pointers whenever a Part changes; dates of old live evidence remain unchanged.

New projects use the manifest template. Repo-only reconciliation writes `Evidence basis: repository records; live Needs refresh` rather than inventing current verification. Session IDs in old records are historical until a real connection establishes validity.

## Local project discovery

The tracked guide intentionally does not enumerate private local projects. Discover the exact local project directory requested by the user, open its `PROJECT.md`, and follow only the sources relevant to the current Scope. If the directory or manifest is absent, stop project-state inference and restore the local source set first.
