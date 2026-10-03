# Framer Build Checklist

这是 Framer 网站的执行顺序。Baseline 定义质量，本文件负责把质量要求放进首次搭建流程。

适用于一个 Section、一个 Page 或完整网站。选择当前范围，但不能跳过该范围需要的质量层。

## 0. Scope 与 Ready

- [ ] 明确本轮范围：Section / Page / Website / Audit。
- [ ] 读取当前项目 `PROJECT.md`。
- [ ] 确认目标用户、页面目的和 CTA。
- [ ] 确认内容状态：Approved / Draft / Missing / Demo。
- [ ] 从 `framer/basic/README.md` 加载本轮专项规则。
- [ ] 列出本轮不会做的内容，避免范围漂移。

如果关键事实是 `Missing`，停止正式内容写入；可以继续完成不依赖该事实的结构工作。

## 0A. Visual Direction Gate

新 Page、重大 Section 重构、多页面差异化，或主要要求为“不同布局”时，批量创建节点前必须完成 active request Checklist 中的 `Visual Direction Contract`：

- [ ] 一行 Design Read 明确页面种类、用户、转化目标与项目视觉语言。
- [ ] Preserve / Transform / Avoid 区分共享系统、允许变化与禁止默认模式。
- [ ] Existing multi-page site 已完成 Sibling-page delta 与全站 layout-family distribution：允许有功能理由的 Contact / CTA / Form / shared-system 布局复用，但不得让所有 sibling pages 使用同一 Hero 或整套 Section/layout-family sequence，形成 site-wide layout monoculture；不设置“每段必须不同”的数量配额。
- [ ] 每个 Section 已明确叙事目的、layout family、focal point、内容密度与过渡关系；复用 family 时能说明相同职责，变化时能说明内容需要。
- [ ] Colour rhythm 已说明每段的 background、text、accent、image relationship 与下一段 transition；仅有 palette token 清单不算完成。
- [ ] Asset map 已记录候选素材、现有使用位置、content-relative image role、复用理由、裁切焦点和三端计划；图片不是只为配合布局或替换标题而互换的装饰物。
- [ ] Structural proof 与 Visual proof 均已规划。
- [ ] `Contract status: Ready`，并已显示 `Visual contract receipt`。

合同暴露真实设计分歧时先向用户确认。若方向已批准，Agent 可以继续执行，不为合同格式重复暂停。纯 Copy、Link、Metadata、命名或窄范围 breakpoint 修复跳过本 Gate。

## 1. 最小系统先行

在批量创建页面内容前完成：

### Text Styles

- [ ] Display / H1
- [ ] H2
- [ ] H3（项目需要时）
- [ ] Body Large
- [ ] Body
- [ ] Caption
- [ ] Eyebrow / Label
- [ ] Button Label

### Color Styles / Variables

- [ ] Background / Base
- [ ] Background / Inverse
- [ ] Surface
- [ ] Text / Primary
- [ ] Text / Secondary
- [ ] Accent / Primary
- [ ] Border / Divider
- [ ] State / Hover
- [ ] State / Focus

### Shared Components

- [ ] Primary / Secondary / On Dark Button Variants
- [ ] Navbar Desktop / Tablet / Phone
- [ ] Footer Desktop / Tablet / Phone
- [ ] Layout Template：Navbar / Content Placeholder / Footer
- [ ] 可复用组件在自身 Variant 中拥有真实的横向 Padding；不依赖页面 Section 的统一横向 Padding 才能正确预览。
- [ ] 混合 Section 将组件与普通文字/图片拆到各自的 Padding Wrapper；外层 Section 只保留背景和垂直节奏。

只建立实际会复用的系统，不为了数量创建 Styles 或 Components。

## 2. 页面骨架

- [ ] Sitemap 与正式路径一致。
- [ ] 每页有明确目的和主要 CTA。
- [ ] 页面使用共享 Layout Template。
- [ ] Section 顺序服务内容叙事，不机械复制模板结构。
- [ ] Desktop、Tablet、Phone 骨架同时存在。
- [ ] Content Placeholder、Navbar、Footer 没有重复副本。
- [ ] 第一段代表性视觉 Section 已在目标画布或截图中检查，确认视觉语言成立后再传播到整页；不能用命令成功替代此检查。

## 3. Section 纵向完成循环

每个 Section 按以下顺序一次完成：

1. [ ] 写入 Approved/Draft 内容。
2. [ ] 应用 Text Styles 与 Color Styles。
3. [ ] 使用 Stack/Grid 建立宽度和间距逻辑。
4. [ ] 重复结构复用 Component / Property / CMS。
5. [ ] 图片完成网页输出、裁切、焦点和 Alt 判断。
6. [ ] CTA、电话、邮箱、地图、社交和内部链接有真实目标。
7. [ ] Heading 使用正确 h1/h2/h3，而不是只靠视觉字号。
8. [ ] 完成 Desktop、Tablet、Phone。
9. [ ] 添加必要且克制的 Motion / Hover。
10. [ ] Targeted readback，确认本 Section 没有结构性遗漏。

完成一个 Section 后再进入下一个，避免全站结束后重新补 Styles、Links 和 Phone。

## 4. Page 完成门槛

- [ ] 唯一 Page Title。
- [ ] 独立 Meta Description。
- [ ] 恰好一个主要 `h1`。
- [ ] 主要 Section 使用合理 `h2`，子级使用 `h3`。
- [ ] 信息性图片有 Alt，装饰图片显式空 Alt。
- [ ] Navbar、Footer 和主要 CTA 可点击。
- [ ] 主体中的 Contact/Visit 信息也可操作。
- [ ] 无 Lorem Ipsum、无未说明占位内容。
- [ ] 320 / 390 / 810 / 1200 / 1440+ 宽度行为合理。
- [ ] 页面已完成一次 Preview 检查。
- [ ] Visual Direction Contract 已从 `Ready` 反向验证为 `Pass` 或有证据的 `Blocked`。
- [ ] Structural status 与 Visual status 分别记录；两者都 Pass 才能报告 Page Pass。

Page 未通过以上条件时，不得标记 Done。

## 5. Interaction Pattern Gate

创建复杂交互前先从 `framer/basic/patterns/pattern-recipes.md` 选择模式：

- [ ] Phone Navbar Menu：Relative Overlay。
- [ ] 简单 Gallery 放大：Lightbox Effect。
- [ ] 页面级 Modal：Fixed Overlay。
- [ ] 展开/折叠：Component Variant。
- [ ] 密集 Row Hover：Gesture Variant / color change。
- [ ] 相同结构不同内容：Property、Fill 或 CMS，不是大量 Variants。
- [ ] 项目行、卡片和列表没有按内容复制 Desktop / Phone / Hover Variant；内容从 Instance Properties 设置。

偏离默认模式且会持续影响后续工作时，在 `DECISIONS.md` 或 PROJECT 的 Decisions 章节记录原因。

## 6. Responsive Gate

### Desktop

- [ ] Page root、外层 Page Content、full-bleed Section 与负责宽度分配的 senior structural parent 使用 Fill / `1fr`，默认不设 `max-width`；约束落在 deepest valid max-width owner，并对比 1200 / 1440+ 确认外层仍会扩展。若采用 approved bounded-canvas exception，已有独立全视口背景 Owner 和全断点证据。
- [ ] Navbar 单行且 Sticky 正常。
- [ ] 图片构图、留白和大屏节奏成立。

### Tablet

- [ ] 不是被动缩放的 Desktop。
- [ ] Grid、间距和字体根据宽度调整。
- [ ] 导航和 Footer 没有拥挤。

### Phone 320 / 390

- [ ] 核心导航无需依赖 Footer。
- [ ] Row/Grid 转为自然 Stack 或隐藏次要信息。
- [ ] Heading、邮箱、价格和 metadata 不出现破坏性断行。
- [ ] 触控目标约 44×44px 或更大。
- [ ] 没有横向溢出。
- [ ] 图片焦点重新检查。

## 7. Motion 与 Accessibility Gate

- [ ] Motion 增强层级和阅读节奏，不只是增加动画数量。
- [ ] Navbar、Button、Gallery、Overlay 使用对应原生模式。
- [ ] Hover 不改变密集布局尺寸。
- [ ] Focus 可见，按钮与链接名称描述操作结果。
- [ ] Overlay / Lightbox 有明确关闭路径。
- [ ] Reduced Motion 下不依赖大位移、强缩放或持续运动传递信息。
- [ ] 颜色对比和正文尺寸满足阅读需要。

## 8. Website Gate

- [ ] favicon 与 Open Graph 图片完成。
- [ ] 全站核心颜色由 Styles/Variables 控制。
- [ ] 全站核心文字由 Text Styles 控制。
- [ ] Navbar、Footer、Buttons 使用共享 Components。
- [ ] Layer、Component、Variant 命名语义化。
- [ ] 所有正式页面进入 `STATUS.md` 或 PROJECT Current Status 的 Build Status Matrix。
- [ ] 执行 `framer/basic/workflows/preflight-audit.md`。
- [ ] 关键 Preview 路径通过。
- [ ] 会持续影响后续工作的已知例外记录在 `DECISIONS.md` 或 PROJECT Decisions；当前缺口记录在 Status。

Marketplace 项目再执行 `framer/basic/standards/marketplace-guidelines.md`。

## 9. 关键 Preview 路径

不要无目的重复截图。最低真实路径：

```text
Home
→ Navbar navigation
→ Primary CTA
→ Contact / Visit action
→ Phone Menu open / close / link
→ Gallery Lightbox open / close（存在时）
→ Footer links
```

每种关键交互验证一次成功路径和一次关闭/返回路径。

## 10. 交付报告

报告前：

- [ ] 更新项目 `STATUS.md` 或 PROJECT Current Status 的 Build Status Matrix。
- [ ] 更新 `DECISIONS.md` 或 PROJECT Decisions / Exceptions。
- [ ] 长任务只更新 `RECOVERY.md` 或 PROJECT 的单一最新 Recovery checkpoint。

只报告：

- 完成范围。
- 通过的断点和关键交互。
- Preflight 结果。
- 仍存在的真实限制或 Missing 内容。

不要用长篇内部节点 ID 或工具过程替代验收结果。
