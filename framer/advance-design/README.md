# Framer Advanced Design 路由

本目录保存经过真实项目验证的高级原生组件与交互配方。它不是普通 Framer 工作的必读入口；先从 [`../README.md`](../README.md) 选择 `framer-interactions`、`framer-components` 或 `framer-layout-responsive` 中一个 primary Skill，再只读取命中的 Pattern。

## 使用边界

- `Canonical` 表示当前同类任务的首选知识入口，不表示其中项目尺寸是全局默认值。
- `Legacy` 表示为零损迁移与历史追溯保留；新任务先读对应 Canonical 文档。
- 文件中的项目名、日期、组件名、尺寸、位移和 Transition 都是 provenance。复用时保留底层合同，再按新项目的外部 Instance、断点和内容重测。
- 不批量通读本目录。固定坐标、轨道或裁切组件必须在外部 Page Instance 验证首项、中间项、末项和至少一次可用宽度变化。
- Advanced 不能绕过 Basic 已成立的 Link、Alt、Heading、Focus、Reduced Motion、Breakpoint 和内容替换路径；实施后仍回到 [`../checklist.md`](../checklist.md) 做 evaluator。
- 新增、迁移、重分类或去重 Pattern 时使用 [`knowledge-maintenance`](../../.agents/skills/knowledge-maintenance/SKILL.md)：保留 provenance 和精确证据，更新本索引，并在完成前运行 strict validator。

## Pattern Index

| Pattern | 状态 | Provenance | 何时读取 |
|---|---|---|---|
| [Filler 覆盖式 Button Hover](aurelia/button-filler-hover.md) | Canonical filler pattern；legacy component provenance | AURELIA `ButtonPrimary`，2026-08-12；早于当前 `Button` White / Dark Small 系统 | 只在需要内部 filler 自底向上覆盖且外部尺寸不能变化时读取；当前 Button 状态合同读 `basic/patterns/buttons.md` |
| [ChefStoryRow](aurelia/chef-story-row.md) | Canonical，project-specific | AURELIA `/chefs` 四 authored widths、八个配对状态 | 人物肖像、身份与长故事需要在同一行内按断点展开 / 返回时 |
| [Reel Text](aurelia/text-reel.md) | Reference，project-derived | AURELIA `Reel Text`，2026-08-16 live Canvas definition、Navbar / Footer instances | 短、单行、可编辑标签需要在 Hover 时纵向滚动，且外部宽度仍由内容驱动时 |
| [Dish Selector 图片矩阵与文字 Reel](aurelia/dish-selector-image-matrix.md) | **Canonical selector / reel** | AURELIA 固定 7 项，2026-08-10 精确实例 | 固定数量图片选择器、单一 Image Strip 与多条同步文字 Reel |
| [可展开 Editorial Card](aurelia/expandable-editorial-card.md) | Canonical，project-specific | AURELIA `MenuDishCard`，2026-08-11 验证 | Desktop / Tablet 展开长故事、Phone 保持独立静态阅读结构时 |
| [Image Strip + Number Reel](aurelia/image-strip-number-reel.md) | **Legacy，零损保留** | AURELIA 2026-08-06 较早实现与推导记录 | 追溯旧实现、光学校正与迁移来源；新 selector 先读上面的 Canonical 文档 |
| [Archive Folder Sticky Stack](ken-studio/archive-folder-sticky-stack.md) | Reference，project-specific；精确复刻合同不完整 | Ken Studio Works，2026-07-14 起的 Sticky Folder / Archive Row 经验 | Folder tab 分层、sticky overlap、scroll space 与 archive row 宽度链；实施前必须重读当前项目结构 |
| [Custom Cursor Hover Preview](ken-studio/custom-cursor-hover-preview.md) | Reference，mixed provenance | Ken Studio Works；后续包含 AURELIA Fixed Cursor Reel 扩展 | 明确需要 Desktop pointer cursor preview、统一 Cursor Component 或固定 Reel 时；只读命中的章节 |

## Canonical / Legacy 决策

```text
Image selector / number-title-description reel
├── 新建、修复或商品化 → dish-selector-image-matrix.md
└── 旧 AURELIA 实现追溯 → image-strip-number-reel.md（Legacy）
```

Legacy 文件不得删除、截断或静默改写；Canonical 文档无法解释的历史参数仍以 Legacy 原文为证据。
