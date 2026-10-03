# Framer Change Control

本文件只管理写入前的需求协调，不代替实施 Skill、Part Checklist 或 Preflight。触发时先 inspect / reconcile 用户要求、项目状态与最后成功状态，再选择一个 primary repo Skill。

## Authorization and task mode

在写入前声明 mode。用户当前要求与已有明确授权持续有效；不为同一 Scope 的记录、回读或派生合同重复请求批准。

| Mode / 情形 | 可以直接做什么 | 何时等待用户 |
|---|---|---|
| Audit only | 只读检查、形成报告；缺陷标 Fix Required | 审计不自动授权修复目标 |
| Repair | 完成已授权局部修复与必要依赖、targeted QA | 新范围、破坏性变更或真实方向分歧 |
| Build，Scope 已明确授权 | 记录原始要求、编译 Ready 合同、回读后实施 | 超出原授权或批准方向变化 |
| Build，只有方案/准备授权 | 完成具体可审阅方案与请求合同 | 正式建设前确认该方案 |
| 用户明确要求创建 Checklist | 创建或更新原 owner | 创建记录本身不扩大建设授权 |
| 用户拒绝项目级 Checklist | 不创建项目目录；在 working state 保留合同 | 若必要信息仍缺失，仅问影响实施的事实 |
| Publish / destructive / paid / Custom Code | 先完成具体可审阅结果 | 相应动作没有既有明确授权时 |

项目额外 planning gate 必须链接建立它的 user-approved decision；没有批准来源时按本表，不把模板里的确认框当作未取得授权的证据。Repo-only knowledge repair 不连接 Canvas，也不触发建设类长篇 Prompt Gate。

## Inspect / Reconcile

任何正式写入前先确认：

- 当前项目、页面、Part、Component、Section 或交互的真实范围。
- 当前 `PROJECT.md`、页面长期 Checklist、请求级 Checklist、Recovery State 与最后成功验证。
- 用户新反馈是追加、校正还是明确覆盖；未明确撤销的既有要求继续有效。
- 本轮允许修改和明确不得修改的页面、断点、组件、素材与内容入口。
- 实施后必须验证的断点、状态和真实路径。

若 inspect 发现结构或聊天记录与当前真实状态不一致，以用户已确认意图和当前可验证状态为准；不要靠重做覆盖差异。

## 长篇分点 Prompt 的 Checklist 前置规则

当用户一次提交包含多个明确分点、会影响同一项目后续 Canvas、页面、组件、素材、排版或交互工作的长篇 Prompt 时，必须在任何正式建设操作前执行：

1. 页面长期 Checklist 与某次具体 Prompt 的工作 Checklist 必须分开。先在 `content-library/<project>/checklist/` 中找到当前页面的长期 Checklist；再在 `checklist/<page-slug>/` 建立该次工作的语义明确文件。没有该页面子文件夹时先创建，不能把请求级 Checklist 混入页面长期 Checklist，也不建立平行聊天日志。
2. 将用户 Prompt 的每一个要求逐字写入该 Checklist；不得省略、合并、摘要或以“同上”等方式简化原始要求。
3. 可以在每一条原始要求下补充更具体的执行判定、风险、依赖、验收项和建议顺序，但不得改变、削弱或替代用户原话。
4. 完成写入和回读，按上表判断建设授权。已明确授权原 Scope 时继续；只有方案/准备授权时展示具体合同并等待确认，确认前不开始正式建设。

这一规则只约束长篇、多分点且将指导后续建设的 Prompt；小范围修复、单一修改、审阅、诊断和已确认 Checklist Part 的连续执行不需要额外暂停。

目录和 page contract 的必需职责由本文件下方的 [项目级 Checklist 文件夹规范](#项目级-checklist-文件夹规范) 维护；实施后验收回到 [Part evaluator](../../checklist.md)。

## 将知识规则编译进组件请求合同

当一次请求会新建、复制或改写可复用 Component 责任，且本轮已存在请求 Checklist 时，在用户原话之后另建 `## Component Requirement Contract`：

1. 用户原话保持逐字、不改写；Component Contract 是派生实施合同，不能取代原始要求。
2. 先完成 `framer/README.md` 的 multi-domain 扫描与 primary-skill 选择，再使用 [`framer-components`](../../../.agents/skills/framer-components/SKILL.md#compile-a-component-requirement-contract) 的唯一标准表格。
3. 只编译当前组件命中的规则；每行记录具体 Decision / N/A reason、Owner、Governing source、Readback proof 和 Preview proof，不把 Baseline 整篇复制进 Checklist。Markdown 来源写为 `path.md#heading`；也可引用编号用户原话或 current Canvas evidence，不能只写裸文件名或“Baseline”。
4. `Contract status: Ready` 是组件写入前提；实施后用同一张表替换计划证据，再按 [Contract lifecycle](#contract-lifecycle) 记录结果。

用户已明确要求开始执行，且派生合同没有扩大 Scope 或改变用户方向时，完成 `Ready` 后直接继续，不为合同格式再次询问。合同暴露新范围、破坏性变更或真实设计分歧时才暂停确认。

## 将视觉规则编译进页面或 Section 请求合同

当请求会创建新 Page、重大重构 Section、区分多页面构图，或主要要求是“使用不同布局”时，在用户原话之后建立一个 `## Visual Direction Contract`：

1. 由 [`design-taste`](../../../.agents/skills/design-taste/SKILL.md#compile-a-visual-direction-contract) 编译唯一标准表格；本文件只管理持久化和确认，不复制其设计规则。
2. 合同必须明确 Design Read、Preserve / Transform / Avoid、Sibling-page delta、Section composition、Colour rhythm、Asset map、Responsive transformation 与 Completion evidence。
3. 只有 `Contract status: Ready` 才允许进入 Canvas 实施；实施后由同一合同替换 planned proof，并按 [Contract lifecycle](#contract-lifecycle) 分类结果。
4. 用户已明确授权建设时，不为合同格式重复询问；但 Agent 新推导出的核心构图、素材复用、跨页面相似性或颜色方向若构成真实设计分歧，必须先展示并等待确认。
5. 写入前显示 `Visual contract receipt`；该 receipt 只证明合同完整，不证明 Canvas 已实现。

Component 与 Visual 合同命中同一请求时，写入同一个 request Checklist，各自保持唯一 heading；不得建立第二份平行设计日志。

## 连续修改前的需求回顾

同一个 Part、Component、Section 或交互进入第二轮及后续修改时，不得只根据用户最新一条消息继续。每次新的写入前必须回顾从该 Part 开始以来用户给出的相关提示与修正，并整理一份短约束锁：

- 当前仍有效的设计目标与交互行为。
- 用户后续补充但没有明确撤销的既有要求。
- 本轮新增或改变的内容。
- 明确不得修改的页面、断点、组件或内容入口。
- 完成后必须验证的断点、状态与真实交互路径。

用户的新反馈默认是在既有要求上追加或校正，不得自动视为替换全部前文。只有用户明确表示放弃、重做或覆盖旧方向时，才移除对应约束。

执行顺序：

```text
回顾当前 Part 的用户提示
→ 写出短约束锁
→ 将拟修改结构逐项对照约束
→ 批量写入
→ 按约束锁和 Framer Checklist 双重复检
```

若实现方案会满足最新反馈却破坏前文要求，必须在写入前调整方案；不能等用户再次指出后才恢复。

说明：

- 最终改了什么。
- 为什么选择该方案。
- 检查了哪些端侧或交互。
- 是否存在已知限制。

不要向用户倾倒内部节点 ID、完整工具输出或重复过程。发现用户方案有结构性问题时，应给出证据和更低成本的替代方案。

## Contract lifecycle

新 request / page owner 声明下面的 applicability，避免根据自然语言猜测是否缺合同；机械修复给出 N/A 理由。

```markdown
- Contract schema: 1
- Component contract: Required / N/A — reason / Legacy — dated source
- Visual contract: Required / N/A — reason / Legacy — dated source
```

每个适用合同仍使用其 Skill 的唯一六列表格。编译期 `Contract status: Draft / Ready`；Ready 证明决定和计划完整，不证明已实施。用户授权单独记录为 `Authorization: Authorized — source` 或 `Pending — reason`。

实施后写 `Implementation status: Implemented / Partial / Not started` 和 `Verification status: Pass / Fix Required / Blocked / Not run`。Implemented / Partial 的合同不能继续标 Ready；以实际整体结果更新 Contract status 为 Pass / Fix Required / Blocked。每个实际 proof cell 写 `Pass — evidence`（链接可核对的 scoped evidence record；记录日期与范围，不能只写 complete）、`Fix Required — issue`、`Blocked — missing evidence` 或 `N/A — reason`。未实施的 Ready 合同可保留明确 Planned proof。

Pass 只能由全部适用 proof 的 Pass / reasoned N/A 得到。用户授权的 Deferred 进入 scope 限制，不能冒充证据。验收字段和 evidence source 可核对，但 validator 不判定截图审美或证明 live 状态。

旧合同先按 dated evidence 标 Legacy，再在下一次相关改写时升级；只读 legacy audit 不因缺少后来新增的表格而要求重建网站。不能为升级 schema 编造历史验证；已有实施而缺 proof 的记录改 Blocked，保留原要求和原结果出处。

## 项目级 Checklist 文件夹规范

本节是项目 Checklist 创建和维护的 canonical schema。项目级 Checklist 负责把已经批准的总览和页面方案转成后续可以逐页、逐 Part 执行的合同；[Part evaluator](../../checklist.md) 负责实施后的验收。

长篇多分点 Prompt 的逐字记录、确认 Gate 与连续修改约束锁由 `framer/basic/workflows/change-control.md` 维护；本节只维护项目 Checklist 的目录、页面文件、状态和同步合同。

### 触发与执行顺序

建设类总览与长篇请求按 [Authorization and task mode](#authorization-and-task-mode) 决定是否需要确认。用户已批准执行时记录和回读后直接继续；未知范围、真实方向分歧或批准后 scope 变化才暂停。用户明确拒绝项目级 Checklist 时不创建目录，保留当前工作合同并继续获授权范围。普通小修、诊断、审阅和已有 Part 的连续执行不触发新建。

### 固定位置与目录结构

Checklist 只能位于当前知识库项目目录：

```text
content-library/<project>/
├── PROJECT.md
├── STATUS.md            # complex projects; current Build / QA
├── DECISIONS.md         # complex projects; active why-decisions
├── RECOVERY.md          # complex projects; one latest checkpoint
└── checklist/
    ├── README.md
    ├── home.md
    ├── about.md
    ├── menu.md
    ├── contact.md
    └── <other-page-slug>.md
```

- 一个正式页面对应一个 canonical page contract；索引声明其精确路径。推荐平铺 page-slug.md，已有嵌套路径可以原处保留。
- 文件名使用页面 slug 的 kebab-case，例如 `private-dining.md`。
- `README.md` 是索引和共享工作流，不代替页面文件。
- 不把 Checklist 放在临时工作区、发布目录、图片目录、聊天导出目录或项目目录之外。
- PROJECT 链接 Checklist 索引；索引逐页链接唯一 page contract 并回链 PROJECT 与实际 Status / Decisions / Recovery owner。request 文件放 page-slug 子目录，不能代替长期页面 owner。

### README.md 必须包含

- 项目级 Checklist 的用途和状态词定义。
- 强制执行闭环和 Part 路由提醒。
- 当前页面、路径、文件和状态索引。
- Shared Foundation Gate：Layout Template、Navbar、Footer、Button、Styles、Focus、Reduced Motion、favicon、Open Graph、授权和编辑说明。
- Latest Part Result 与 canonical Recovery reference 的统一记录格式。
- 对 `PROJECT.md`、当前 Status / Decisions / Recovery owner、`framer/basic/` 和本文件的有效相对链接。

### 每个页面 Markdown 必须包含

1. Page 名称、path、当前状态、内容状态和 Primary CTA。
2. Scope lock / Definition of Ready：目标、已确认内容、Missing、Blocked 和本轮明确不做的范围。
3. 页面专属叙事顺序；不能只写通用 Hero、Cards、CTA。
4. 每个 Section 的目的、内容、图片角色、构图职责、CTA 和完成项目。
5. Text / Color Styles、Heading 语义和 Layer 命名要求。
6. Component / Variant / Property / CMS 决策，以及创建后回到 Page Instance 的检查。
7. Navbar、Footer、Button、Link、Contact / Visit 和 Conversion 路径。
8. 图片驻留、视觉预算、网页输出、裁切、焦点和 Alt。
9. Desktop、Tablet、Phone 的宽度所有权，以及 320 / 390 / 810 / 1200 / 1440+ 验证。
10. Motion、Hover、Overlay、Lightbox、Focus、Keyboard 和 Reduced Motion。
11. Page Title、Meta Description、一个主要 h1、h2/h3、favicon 和 Open Graph 责任。
12. Performance、第三方依赖、Framer Review 和可维护性。
13. Marketplace 替换压力测试：长文案、不同图片比例、缺失可选字段、增删排序和买家编辑入口。
14. Targeted Preview 路径。
15. Page Done 门槛。
16. Latest Part Result：Pass、Fix Required、Blocked、Verified widths、Verified paths、Shared components 和 canonical Recovery reference；不在页面 Checklist 复制第二份 current checkpoint。
17. 当范围是新 Page、主要 Section 重设计、跨页面差异化或用户要求“different layout”时，包含由 `design-taste` 编译的 `Visual Direction Contract`：明确 sibling-page delta、Section composition、Colour rhythm、Asset map、Responsive transformation，以及 Structural proof / Visual proof；轻量文案或机械修复不强制创建。

页面文件必须针对当前页面写具体检查项。迁移既有页面时可按上述类别链接仍有效的精确 source headings，保留一个稳定 page owner；缺少的 legacy 合同或证据标明 Legacy / Blocked，不为补 schema 虚构历史建设。新建设或相关改写仍编译完整适用合同。禁止把本文件的 18 个通用章节原样复制五次，也禁止只写视觉 Section 而遗漏 Styles、Links、语义、响应式、Focus、状态和交付。

### 状态与同步

项目级状态统一使用：

- `To do`：范围已批准，尚未宣称完成。
- `In progress`：正在按 Section 或 Part 纵向建设。
- `Fix Required`：当前必查项失败，修复前不得进入下一 Part。
- `Blocked`：缺少事实、素材、权限、服务或真实目标。
- `Pass`：当前 Part 或 Page 通过对应 readback、Preview 和 Preflight；适用 `Visual Direction Contract` 的范围必须同时达到 Structural status 与 Visual status 的 `Pass`。

强制同步：

- Checklist 页面状态与项目 current status owner 必须一致：复杂项目使用 `STATUS.md`，小项目使用 `PROJECT.md` 的 Current Status。
- 每完成一个 Part，更新页面文件的 Latest Part Result；当前恢复指针写入 `RECOVERY.md` 或 PROJECT 的单一 Recovery 章节，不在页面文件和多个入口重复维护 current checkpoint。
- 每完成一个 Page，执行 [Part evaluator](../../checklist.md) 的 Page 路由和 [preflight](preflight-audit.md)，再把状态改为 `Pass`。
- 叙事、页面目的或信息架构变化时，先更新 `PROJECT.md`；需要持续解释原因时再更新 `DECISIONS.md` 或 PROJECT 的 Decisions 章节，然后同步受影响 Checklist，不能只改 Canvas。
- Missing 和 Blocked 不用虚构内容填满；保留真实状态并继续完成不依赖阻塞项的工作。
