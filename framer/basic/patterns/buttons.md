# Framer Button Pattern

本文件记录 Framer 原生 Button 的默认结构。核心目标是让按钮边框随文字内容自然变化，同时让页面容器负责对齐和可用宽度。

## 第一性原理

Button 的内容响应不是靠 Relative、百分比宽度或手动计算边界实现。

正确关系是：

```text
文字的真实尺寸
→ 拥有边框的 Stack 用 Padding 包住文字
→ Stack 使用 Fit Content
→ 文字变化时，边框自然跟随变化
```

文字节点不能拥有 Padding。Padding 必须设置在真正拥有 Fill、Border、Radius 或可点击边界的父级 Stack 上。

## Component 内部结构

```text
CTA Button Component
├── Desktop
│   └── Button Stack (Fit / Fit + Border + Padding)
│       └── Content (Fit / Fit + String Property)
├── Tablet
│   └── Button Stack (Fit / Fit + Border + Padding)
│       └── Content (Fit / Fit + String Property)
└── Phone
    └── Button Stack (Fit / Fit + Border + Padding)
        └── Content (Fit / Fit + String Property)
```

默认设置：

- Component Variant 根层使用 Stack，`width: Fit Content`、`height: Fit Content`。
- 拥有可见边框的 Button Stack 使用 `width: Fit Content`、`height: Fit Content`。
- Content 文字使用 `width: Fit Content`、`height: Fit Content`。
- Button Stack 通过水平和垂直 Padding 决定文字与边框的距离。
- Content 使用 String Property；不同页面实例只修改 Content，不复制内容 Variant。
- Link 使用 Link Property，并绑定在可点击的 Button Stack，而不是文字节点。
- Desktop、Tablet、Phone Variant 只处理真实的字号、Padding 或结构差异，不为不同文案复制 Variant。

## 页面中的放置结构

组件负责自身边框和内容尺寸，页面外层 Stack 负责位置、对齐和可用宽度。

```text
Section / Card Content
└── CTA Stack (Fill width + Fit height)
    └── CTA Button Instance (Fit / Fit)
```

CTA Stack 的默认职责：

- `width: Fill`，取得所在 Section、Row 或 Card 的可用宽度。
- `height: Fit Content`，让按钮的完整边框进入正常文档流。
- 使用水平 Stack。
- Desktop / Tablet 通常通过 Distribution 控制左对齐或右对齐。
- Phone 可根据构图改为居中，但仍保持 Fit 高度。
- Button Instance 保持 `width: Fit Content`、`height: Fit Content`。

外层 Stack 不能用过小的固定高度。固定高度低于按钮真实高度时，即使组件内部正确，Border、Hover Fill 或文字行框仍会被父级裁切。

## Link 边界

优先在 Button Component 内建立 Link Property，并把链接绑定到拥有可见边界的 Button Stack。

如果现有 Component 暂时没有 Link Property，可以使用：

```text
CTA Stack (Fill / Fit, only placement)
└── Link Stack (Fit / Fit, owns Link)
    └── CTA Button Instance (Fit / Fit)
```

不要把 Link 绑定到 Fill 宽度的外层 CTA Stack，否则按钮之外的空白区域也会变成可点击区域。

## Hover 与 Variant

- Hover 使用共享 Gesture Variant。
- Hover 可以改变 Fill、Border、文字颜色或透明度。
- Hover 前后必须保持相同 Padding 和布局尺寸。
- 不默认使用 scale，避免推动邻近内容或被父级裁切。
- 每个断点只有在字号或 Padding 确实不同的时候才保留独立结构 Variant。
- 不为每种按钮文案建立新的 Hover Variant。

## Small Variant（Phone 可用）

以后每一个可复用 Button Component 都必须同时提供 Small Variant，供 Phone 的紧凑版面、卡片或次级 CTA 使用。Small 不是复制一份新的组件：它必须复用同一组 Content、Link 与 Click Property，并且拥有与常规按钮一致的状态逻辑。

- 默认同时建立对应的 Small Hover 状态；有指针设备进入 / 离开时的效果必须与常规尺寸同一逻辑，Phone 不因没有 hover 而失效。
- Small 的字号、Padding 与常规尺寸分开管理，但仍保持 Fit / Fit、文字由拥有可见边界的 Button Stack 的 Padding 包住。
- AURELIA 当前 `White Small` 的基准是 `12px 18px` Padding、`10px` Label；新的 Small 表面或配色以此为尺寸参考，除非页面已有明确的系统尺寸。
- 若 Small 用于独立的主要操作，需另外确认实际点击目标是否足够；Small 适合紧凑语境，不应被固定高度的外层容器裁切。

## 常见错误

### 1. 给文字设置 Relative 或百分比宽度

结果：边框不会真正由内容驱动，文案变化后出现多余空白、换行或裁切。

修复：文字和可见 Button Stack 都改为 Fit Content，由父 Stack 的 Padding 建立边界。

### 2. Button Instance 是 Fit，但外层 Stack 使用固定高度

结果：组件自身尺寸正确，放到页面后 Border 或 Hover Fill 仍被裁切。

修复：外层 CTA Stack 使用 Fit height。需要触控目标时使用合理 Padding 或 min-height，不用更小的固定高度压住组件。

### 3. 把页面对齐职责放进 Button Component

结果：同一个按钮无法自然适配左对齐、右对齐和 Phone 居中场景。

修复：Component 只负责按钮本体；页面外层 CTA Stack 负责 Fill width 和对齐。

### 4. 为不同文字复制 Button Component 或 Variant

结果：Hover、Padding 和断点修改需要多处同步。

修复：只保留一个 Content Property。Variant 只表达断点、状态或真实结构差异。

### 5. Link 放在文字节点或整条 Fill Stack

结果：点击范围过小，或按钮之外的大块空白也能点击。

修复：Link 绑定在按钮可见边界 Stack；若需额外包装，Link Stack 也必须是 Fit / Fit。

## 完成检查

- [ ] 改长和改短 Content 后，Border 都随文字自然变化。
- [ ] Button Stack 的 Padding 是文字与边框间距的唯一所有者。
- [ ] Component Variant、Button Stack、Content 和 Instance 均无多余固定宽度。
- [ ] 页面外层 CTA Stack 是 Fill width + Fit height。
- [ ] Desktop、Tablet、Phone 选择正确 Variant。
- [ ] 320 / 390 / 810 / 1200 / 1440+ 无裁切、零尺寸或横向溢出。
- [ ] Hover 前后尺寸不变化，文字对比度有效。
- [ ] 每个可复用按钮同时具备 Small Variant，且 Small Hover 与常规状态逻辑一致。
- [ ] Link 的点击区域与可见按钮边界一致。
- [ ] 修改共享 Component 后，抽查全部受影响实例。

## Ken Studio 已验证模式

Ken Studio Home 的 `CTA Button` 使用以下结构：

- Component 内部的 Border Stack 通过 Padding 包住 Content。
- Desktop / Tablet 使用 15 px Padding，Phone 使用 12 px Padding。
- Content、Button Stack、Component Variant 和页面 Instance 均使用 Fit Content。
- Home 的外层 `CTA` Stack 使用 Fill width + Fit height，并按断点控制右对齐或居中。
- Observation 的 Polaroid Card 使用相同组件；外层 `CTA` Stack 负责 Fill / Fit，内部 Fit Link Stack 保留每张卡片自己的 Link。

这是后续 Framer Button 的默认参考。除非项目有明确的等宽按钮、全宽 CTA 或固定触控尺寸需求，不使用固定宽度替代内容驱动结构。
