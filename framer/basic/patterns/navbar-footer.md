# Framer Navbar 与 Footer 制作要求

本文档用于 Framer 多页面网站和 Marketplace Template。目标是让 Navbar 与 Footer 具备真实网站需要的导航能力、响应式表现和可维护结构。

## 1. 基本层级

多页面网站统一使用以下层级：

```text
Layout Template
├── Navbar Component
│   └── Desktop / Tablet / Phone / Interaction Variants
├── Page Content Placeholder
└── Footer Component
    └── Desktop / Tablet / Phone Variants
```

- 页面结构统一拆分为 Navbar、Content、Footer。
- 跨页面共用的 Navbar 与 Footer 应放入同一个 Layout Template。
- Navbar、Footer 和重复按钮必须做成 Component，不要在每个页面复制 Frame。
- Component 使用 Variant 适配不同断点、背景和交互状态。
- 页面只保留自己的 Content，避免页面级重复结构。

## 2. Navbar 要求

### 布局与行为

- Desktop 导航保持单行，高度通常不超过 80px。
- Navbar 应常驻顶部，使用 Sticky，`top: 0`，并设置合理的 z-index。
- 滚动方向反馈可按项目需要加入：向下滚动时隐藏、向上滚动时出现。对于刻意极小、固定、持续可见的 Navbar，不要为满足通用模式而加入隐藏行为；在项目 Decisions 中记录该例外即可。
- 优先使用 Framer 原生 Scroll Variant Effect 和 Component Variant。
- 动画应短、平稳、克制，不改变页面布局高度。
- 转场可使用 Spring Physics，推荐 stiffness 250。

### 链接

- Logo 必须链接到首页 `/`。
- 每个导航项必须链接到已存在且非 Draft 的页面或有效页面锚点。
- CTA 按钮必须有明确链接，例如 Contact、Book、Visit 或 View Menu。
- 当前页面状态使用 Link Style 的 `current` 状态，不要复制多套 Navbar。
- 链接 hover 以颜色、透明度或下划线变化为主，不使用 scale。

### 响应式 Variant

- Desktop：Logo、主要导航、主要 CTA。
- Tablet：缩小间距与 padding，仍需保持清晰单行。
- Phone：只保留 Logo 与必要入口，完整导航可使用 Framer 原生 Overlay。
- 如果明确使用 Drawer Variant，应建立 Closed 与 Open Variants，保持 Logo 和菜单按钮位置稳定。

### Phone Drawer Variant（紧凑 Navbar 的推荐模式）

当 Phone 导航是紧凑固定顶栏时，可以优先使用同一个共享 `Navbar` Component 的 `Phone`（Closed）和 `Phone Open` Variants，而不是 Overlay：

- `Phone` 使用固定高度和 `overflow: clip`；抽屉内容仍存在，只由裁切隐藏。
- `Phone Open` 从 Closed 结构派生，只将外层高度改为 `auto`，显示同一组真实链接。
- Logo、Menu/Close 触发器和链接容器在两个 Variant 中保持相同位置、宽度和内容；不可在打开时重建另一套导航。
- Menu 与 Close 使用精确的 `SET_VARIANT` 目标切换；Phone 链接保留真实页面目标。
- Press 反馈采用原生 `tapEffect` 的短暂透明度变化，保持 `scale: 1`，不得改变高度、间距或造成 reflow。
- 此模式不要求 Overlay；只有确实需要覆盖全页、遮罩或独立 Modal 语义时才使用 Overlay。

#### Height-reveal ownership and failure checks

Before changing a shared Phone drawer, inspect the complete ownership chain instead of only the Component definition:

```text
Layout Template breakpoint Frame
└── fixed / sticky Navbar Component Instance  ← placement, available width, instance height
    └── Navbar Closed / Open Variant roots   ← state height, surface and clipping
        └── Drawer                            ← links, CTA, padding and internal rhythm
```

- The Layout Template instance must allow the Navbar to grow when the open state needs to grow: use `height: auto` unless a separately verified sizing contract owns that height. A fixed closed-height instance will clip an otherwise-correct Open Variant.
- For a height-reveal drawer, keep `overflow: clip` on both Closed and Open roots. `overflow: visible` lets drawer content spill out before the root has revealed it, which reads as a sudden pop rather than an expansion.
- Do not use `visible: false` on the Drawer as the mechanism for a smooth height reveal. Visibility is binary and is not interpolated. Keep the same Drawer structure in both variants; let the root's bounded height and clipping hide it while closed.
- Keep the root transition identical across the paired Closed/Open states unless a Preview proves a state-specific difference is necessary. Do not mix a fast physics spring on one state with a duration spring on the other by accident.
- If the intended interaction is an anchored floating panel rather than a reveal from the Navbar surface, choose the Relative Overlay pattern instead. Do not combine the two patterns in one state route.

Required Phone Preview path at 390px: `Closed → Open → Close → Open → one real internal link`. Verify that the menu stays within the Navbar surface during expansion, the close control remains reachable, the linked page loads, and the state returns to Closed.

### Phone 菜单 Overlay

- Phone 宽度无法容纳完整导航时，将右侧 CTA 改为语义明确的 `Menu` 按钮。
- 紧凑导航菜单优先使用 Framer 原生 Relative Overlay，并直接挂在 Menu 触发器上；Fixed Overlay 留给需要遮罩整个页面的 Modal 或 Lightbox。
- Overlay 至少包含 Home、主要页面导航和 Contact 主 CTA，不能迫使用户滚动到 Footer 才能访问核心页面。
- Menu 触发器和 Overlay 应保留在共享 Navbar Component 内，由 Phone Variant 控制显示，Desktop 与 Tablet 不显示该触发器。
- 必须提供可见的 Close 按钮，并保留原生外部点击和键盘关闭行为。
- 打开动画使用透明度配合轻微位移或缩放，时长建议 280–420ms；禁止直接闪现或使用夸张弹跳。
- Overlay 宽度需要留出屏幕边距。390px 画布可使用约 340px 面板，并启用碰撞检测，避免贴边和横向溢出。
- 菜单项使用真实链接；Contact CTA 复用现有 Button Component，不为每个链接创建独立 Variant。
- 完成后必须在 Framer Preview 中真实点击测试打开、关闭与至少一个导航链接，不能只检查画布静态状态。

## 3. Footer 要求

Footer 不只是展示 Brand，还要帮助用户继续浏览、联系和行动。

### 必要内容

- 品牌名称或 Logo。
- 简短品牌说明或 tagline。
- 页面导航：Home、Menu、About、Gallery、Visit、Contact 等。
- 地址与地图链接、营业时间、电话、Email、社交和 CTA 仅在当前项目已确认需要且有事实/真实目标时加入。
- 电话和 Email 存在时必须使用 `tel:` 与 `mailto:` 链接。
- 用户明确指定极简 Footer 时，可只保留 Brand、tagline、页面导航、已确认的联系信息、版权和 Demo 说明；不要为满足通用清单添加社交或重复 CTA。
- Copyright 和必要的模板 Demo 说明。

### 排版

- Footer 顶部必须有充足留白，Desktop 建议约 64-96px。
- 内容不得贴顶部、贴边或全部挤在第一行。
- Desktop 可使用 3-4 列；Tablet 根据宽度改为 2 列；Phone 改为垂直 Stack。
- 内容组之间使用稳定的 gap，信息层级要清楚。
- 标题、正文、链接和辅助文字需要有明确的字号与颜色层级。
- Footer 链接 hover 禁止 scale，避免文字被 overflow 裁切或推开相邻内容。

## 4. Component 与 Variant 规则

- Component 使用 PascalCase，例如 `Navbar`、`Footer`、`PrimaryButton`。
- Layer 使用语义化名称，例如 `Navigation Links Row`、`Footer Visit Information`。
- 禁止保留 `Frame`、`Stack 1`、`Text 2` 等默认名称。
- 创建 Component 后必须回到页面实例检查 Variant、链接、hover、尺寸和响应式控制。
- 一个共享组件通过 Variant 适配状态，不要创建多个近似组件。
- Button Variant 应根据背景选择 Primary、Secondary、On Dark 或 Text Link。

## 5. 发布前检查

- Navbar Sticky 正常。
- 向下滚动隐藏、向上滚动出现正常。
- Logo、导航、CTA、Footer 导航、联系方式和社交链接均可点击。
- Desktop、Tablet、Phone 分别检查，没有横向溢出。
- Navbar Desktop 保持单行。
- Footer 顶部和四周留白合理。
- Phone Footer 为自然单列阅读顺序。
- 页面只保留一套共享 Navbar 与 Footer。
- Layer、Component、Variant 与 Layout Template 命名清晰。
- Framer Review 无本次修改产生的链接、尺寸、溢出或对比度错误。
