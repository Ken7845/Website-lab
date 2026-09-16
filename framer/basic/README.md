# Framer Basic Reference 路由

`basic` 保存详细标准、原生 Pattern 与执行经验。它不是开工前必须通读的规则包；先从 [`../README.md`](../README.md) inspect / reconcile 并选择一个 primary repo Skill，再按当前判断读取最少必要 reference。

新增、迁移或去重 Basic 知识时不要沿用网站建设路由；改用 [`knowledge-maintenance`](../../.agents/skills/knowledge-maintenance/SKILL.md)，先搜索现有 Canonical，完成后运行 strict validator。

Checklist 与 `framer-qa` 是实施后的 evaluator。除纯 Audit 任务外，不在开工前完整读取 [`../checklist.md`](../checklist.md) 或 `preflight-audit.md`。

```text
framer/basic/
├── README.md
├── standards/   完成标准、Marketplace 与命名
├── patterns/    Framer 原生结构与交互配方
└── workflows/   建设、变更控制、视觉安全、验证与恢复
```

## Standards：按完成责任读取

| Reference | 何时读取 |
|---|---|
| [`standards/website-baseline.md`](standards/website-baseline.md) | 新 Page / Website、范围 DoD、SEO / A11y / CMS / Delivery；小修只读相关章节 |
| [`standards/marketplace-guidelines.md`](standards/marketplace-guidelines.md) | 仅 Marketplace 商品化、买家替换压力、Demo / Remix / 授权交付 |
| [`standards/layer-naming.md`](standards/layer-naming.md) | 新建或批量重命名 Layer / Component / Variant；先保护 Scroll Target / `elementId` |

## Patterns：先选结构，再读参数

| Reference | 何时读取 |
|---|---|
| [`patterns/pattern-recipes.md`](patterns/pattern-recipes.md) | 不确定 Relative Overlay、Lightbox、Fixed Overlay、Variant、Property 或 CMS 的原生归属时 |
| [`patterns/buttons.md`](patterns/buttons.md) | Button Fit / Fit、Padding 所有权、Link 边界、Small / Hover Variant |
| [`patterns/navbar-footer.md`](patterns/navbar-footer.md) | Layout Template、共享 Navbar / Footer、Phone Drawer / Menu |
| [`patterns/motion-design.md`](patterns/motion-design.md) | Motion、Hover、Overlay、Lightbox 与 Row 状态；只读当前 Pattern 章节 |
| [`../advance-design/README.md`](../advance-design/README.md) | 当前任务明确命中高级原生组件或交互装置时，选择一个 Canonical Pattern |

## Workflows：按风险读取

| Reference | 何时读取 |
|---|---|
| [`workflows/change-control.md`](workflows/change-control.md) | 长篇多分点 Prompt、第二轮及后续连续修改、要求可能冲突时；属于写入前条件路由 |
| [`workflows/build-checklist.md`](workflows/build-checklist.md) | 新建 Section / Page / Website 或多 Part 实施顺序；不作为纯 Rename / Link 修复的前置全文 |
| [`workflows/token-saving.md`](workflows/token-saving.md) | Targeted read、Definition / Instance / Breakpoint 分层、批量写入、宽度所有权、Session / Recovery |
| [`workflows/image-workflow.md`](workflows/image-workflow.md) | **任何素材选择、复用、上传、放置、裁切，本地查看、Framer 截图或 Preview 截图之前**；叙事角色、重复控制、视觉预算、驻留、联系表、失败降级 |
| [`workflows/preflight-audit.md`](workflows/preflight-audit.md) | 实施完成后的 Page / Website Preflight 与交付报告，不是开工教材 |

仓库不再维护平行的 Agent connection 文档。需要真实 Framer 连接时，先运行 `npx @framer/agent@latest setup`，完成后加载已安装的官方 `framer` Skill。

## Primary Skill 与 Reference 路由

| 当前主要判断 | Primary repo Skill | 最小 references |
|---|---|---|
| 品牌、叙事、视觉方向、参考站转译 | `design-taste` | 当前项目 PROJECT / Brand / Inspiration；按需 Baseline 相关章节 |
| Page / Section Layout、Stack / Grid、Responsive、宽度所有权 | `framer-layout-responsive` | Baseline Layout / Responsive；`token-saving` 的宽度链；涉及图片时先 `image-workflow` |
| Styles、Component、Variant、Property、CMS、共享 Shell | `framer-components` | Pattern Recipes；对应 Button / Navbar reference；Naming；Baseline Components |
| Motion、Hover、Overlay、Lightbox、Cursor、Sticky | `framer-interactions` | Pattern Recipes → Motion 目标章节；命中高级装置时再进 Advanced Index |
| Audit、诊断、Preflight、交付验收 | `framer-qa` | 当前范围 Checklist 章节；Preflight；Marketplace 时追加 Marketplace reference |

图片任务按主要目标选择 primary Skill：素材叙事与选择使用 `design-taste`；容器、裁切和三端放置使用 `framer-layout-responsive`。两者都必须先遵守 `image-workflow`，但不因此同时加载两个 primary Skills。

新 Page、重大 Section 重构、多页面差异化或“不同布局”先由 `design-taste` 编译 Visual Direction Contract；方向 Ready 后再切换到一个 Framer implementation Skill。纯机械修复不进入这条较重路径。

## 实施后 Evaluator

完成一个 Section、Component、Variant、图片批次、交互、Breakpoint、Navbar、Footer、Page 或其他明确 Part 后：

```text
打开 ../checklist.md 路由表
→ 只读当前 Part 对应章节
→ Targeted readback / 必要 Preview
→ Pass / Fix Required / Blocked
→ 同类问题批量修补
→ 只复检受影响范围
```

Page / Website 报告至少说明 Scope、通过的断点、验证路径、Missing / Blocked 与经过说明的例外。不要为了“更确定”读取未命中的全部 references。
