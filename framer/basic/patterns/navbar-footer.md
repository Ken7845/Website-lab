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
- 推荐加入滚动方向反馈：向下滚动时隐藏，向上滚动时出现。
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
- 地址与地图链接。
- 营业时间。
- 电话和 Email，并使用 `tel:` 与 `mailto:` 链接。
- 社交媒体链接，外部链接按需在新标签页打开。
- 清晰 CTA，例如 Plan Your Visit、Get Directions 或 Contact。
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
