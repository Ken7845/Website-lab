# Framer Pattern Recipes

这是常见需求的默认方案索引。先选模式，再搭建；不要在实现过程中临时发明结构。

详细参数由对应专项文件维护，本文件不复制全部细节。

## 决策表

| 需求 | 默认方案 | 不要默认使用 | 详细规则 |
|---|---|---|---|
| 稳定的多页面共享 Shell | Layout Template + Navbar/Footer Components；Shell 不稳定或有意移除模板时使用页面级 Component Instances | 每页复制裸 Navbar/Footer Frame | `framer/basic/patterns/navbar-footer.md` |
| Sticky 且滚动隐藏 Navbar | Scroll Direction Variant Effect | Custom Code scroll listener | `framer/basic/patterns/navbar-footer.md` |
| Phone Navbar Menu | integrated drawer → Closed/Open Variants；anchored floating panel → Relative Overlay | 把两种机制混成一条 state route | [Navbar models](navbar-footer.md#phone-drawer-variant紧凑-navbar-的推荐模式) |
| 简单 Gallery 放大 | Lightbox Effect | 每图一个 Overlay/Variant | `framer/basic/patterns/motion-design.md` |
| 复杂页面级 Modal | Fixed Overlay | Component 内 Fixed Overlay | `framer/basic/patterns/motion-design.md` |
| Accordion / Disclosure | Open/Closed Component Variants | 多个重叠 Frames | Baseline / Framer 原生 Variant |
| 相同结构不同图片 | Image/Fill Property 或直接替换 Fill | 每图一个 Variant | `framer/basic/workflows/image-workflow.md` |
| 相同结构不同项目行 | 单一 Row Component + 内容/Fill Properties | 每个项目一组 Desktop/Phone/Hover Variants | Baseline / Component Properties |
| 重复内容且需增删排序 | CMS | 大量静态复制 | `framer/basic/standards/website-baseline.md` |
| Button 内容与边框响应 | Fit Content Button Stack + Padding + 外层 CTA Stack | Relative/百分比宽度或固定高度 Holder | `framer/basic/patterns/buttons.md` |
| Button 状态与背景适配 | Button Component Gesture Variants | 每页手工按钮 | `framer/basic/patterns/buttons.md`、`framer/basic/patterns/motion-design.md` |
| 密集 Row Hover | Gesture Variant + color/opacity | 整行 scale | `framer/basic/patterns/motion-design.md` |
| 图片 Hover | Outer Frame + Inner Image scale | 整卡 scale | `framer/basic/workflows/image-workflow.md` |
| Contact / Visit 信息 | 可点击文本 +真实协议链接 | 纯展示文字 | Baseline |
| Desktop Grid 到 Phone | Phone Stack / 简化结构 | 一列 Grid 硬撑 | Baseline |

## 1. Shared Shell Strategy

```text
Layout Template
├── Navbar Component Instance
├── Content Placeholder
└── Footer Component Instance
```

适用：大多数页面共用稳定 Navbar、Content Placeholder 与 Footer 的网站。

如果页面结构需要独立变化、项目已故意移除模板，或共享 Shell 尚未稳定，则改用页面级 Navbar/Footer Component Instances；不为满足模式而恢复模板。两种策略都复用同一个组件定义，而不是复制 Frame。

完成条件：

- Navbar/Footer 只有一套共享定义。
- Desktop/Tablet/Phone 使用清晰 Variants。
- Template 策略下页面只维护自己的 Content；页面级策略下页面负责实例位置和当前路由 Variant。
- Navbar Sticky 和 Footer 高度不破坏内容流。

## 2. Phone Navbar Menu

```text
Phone Navbar Variant
└── Menu Trigger
    └── Relative Overlay
        ├── Close
        ├── Core Navigation
        └── Primary CTA
```

适用：锚定 Navbar Trigger 的浮动 panel；集成式高度展开读 [Drawer model](navbar-footer.md#phone-drawer-variant紧凑-navbar-的推荐模式)。

默认：bottom/end、collision detection、340px at 390px、约 360ms opacity + slight y/scale。

禁止：为了普通锚定菜单创建 page-level Fixed Overlay 或不必要的跨 Scope 映射。Frame Trigger无需额外Event Variable；nested Component Trigger按其已暴露Event接口连接父级。复杂Navbar的Row/Menu责任读 [Component ownership](navbar-footer.md#复杂-navbar先划分-component-与-state-ownership)。

## 3. Gallery Lightbox

```text
Gallery Grid
├── Image + Lightbox Effect
├── Image + Lightbox Effect
└── Image + Lightbox Effect
```

适用：只需点击放大图片。

只有需要 Caption、CTA、混合媒体或自定义前后导航时，才升级为可复用 Fixed Overlay。

## 4. Reusable Button

```text
Page CTA Stack (Fill / Fit)
└── Button Instance (Fit / Fit)
    └── Button Stack (Fit / Fit + Padding + visible boundary)
        └── Content (Fit / Fit + Property)
```

文字变化由 Button Stack 的 Padding 和 Fit Content 驱动边框变化，不用 Relative 或百分比宽度。页面外层 CTA Stack 负责对齐和可用宽度，并必须使用 Fit height，避免裁切 Border 或 Hover Fill。

状态差异进入 Variant；Content 和 Link 属于 Properties。Hover 使用颜色、边框、文字或轻微 elevation，不用整体 scale。完整规则见 `framer/basic/patterns/buttons.md`。

## 5. Image Hover

```text
Image Frame
└── Image Content
```

外框保持尺寸、边框、圆角和 clip；内部图片轻微 scale。Gallery 已有 Lightbox 时，`cursor: zoom-in` 可以承担主要可点击提示。

## 6. Repeated Content

选择顺序：

```text
是否重复？
├── 否 → 普通 Section
└── 是
    ├── 只需复用视觉结构 → Component + Properties
    ├── 需要经常增删排序 → CMS
    └── 真正状态/结构差异 → Variants
```

内容差异不是 Variant 的理由。

项目列表默认维护模型：

```text
一个结构 Component
├── Desktop
├── Phone
└── Gesture Variants

多个 Page Instances
└── 各自设置 Number / Title / Meta / Fill / Link / Cursor
```

新增内容时复制 Instance 并修改 Properties。只有布局、状态或交互结构真正不同，才创建 Variant。

## 7. Contact and Visit

- Phone → `tel:`
- Email → `mailto:`
- Address → Map URL
- Social → Real external URL
- Main action → Clear CTA

主体与 Footer 都应提供操作路径。不要让 Contact 页面只展示不可点击文字。

## 8. Pattern 例外

只有以下情况允许偏离默认方案：

- 用户明确要求不同交互。
- 原生模式无法承载必要内容。
- Preview 证明默认模式在当前结构中不可用。
- Accessibility 或平台限制要求调整。

偏离时记录：选择、原因、影响范围和验证结果。不要把一次临时 workaround 升级为全局默认。
