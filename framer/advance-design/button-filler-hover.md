# Framer 高级组件：Filler 覆盖式 Button Hover

## 适用范围

用于需要明确但克制的 Desktop pointer feedback 的主 CTA。默认态保留轻量的强调线；Hover 用同一个内部 `filler` 覆盖整颗按钮。它不是缩放、阴影或外部 overlay，因此不会改变按钮边界或推开相邻布局。

不用于密集导航链接、表格行或 Phone 必经信息路径；Phone 不应依赖 Hover 才能理解按钮用途。

## AURELIA 已验证实现（2026-08-12）

Component：`ButtonPrimary`

### 状态

| 状态 | 作用 | 外观 |
|---|---|---|
| `Default` | 组件默认与鼠标进入起点 | 白色按钮；底部 1px 红色 filler 线。 |
| `Hover` | Desktop pointer hover | 红色 filler 覆盖整个按钮；文字置于上层。 |
| `Pressed` | 原生 pressed gesture | 保持为独立手势态；不可用来代替 Hover。 |

旧的灰色 Hover 已移除。不要重新创建第二个 Hover Variant；一个组件只保留一条清晰的 pointer hover 路径。

## 推荐层级

```text
ButtonPrimary (Component)
├── Properties
│   ├── Label (string)
│   └── Link (link)
├── Default
│   ├── Label
│   └── filler (absolute)
├── Hover
│   ├── Label (z-index 2)
│   └── filler (absolute, full cover)
└── Pressed
    ├── Label
    └── filler
```

### 外层 Button

- `htmlTag="button"`，`cursor="pointer"`。
- 使用 Stack，`overflow="clip"`；这是 filler 在按钮边界内扩展的必要条件，不要改成 `visible`。
- 固定 Padding、Gap、Width/Height 所有权在 Default 与 Hover 间必须一致。Hover 不改变外层尺寸。
- `Default onMouseEnter` → `SET_VARIANT Hover`。
- `Hover onMouseLeave` → `SET_VARIANT Default`。
- 当前 AURELIA 实现中，Default 保持 `spring-duration 0.4s 0.2 0s`；红色 Hover 使用 `spring-physics 250 30 1 0s`。后者是 filler 覆盖进入时的关键运动参数。

### Default filler

`filler` 是 Button 的绝对定位内部 Frame，不是外层 Border：

- Fill：`rgb(252, 81, 81)`。
- `width="100%"`，`height="1px"`。
- 贴在按钮底边：`right="-0.75px"`、`bottom="-1px"`；不参与 Stack 排版。
- 保持可见，以形成细红线。

### Hover filler

Hover 从同一结构继承，只修改内部视觉层：

- 保持 `position="absolute"`。
- 覆盖按钮：`left="0px"`、`top="0px"`、`bottom="0px"`、`width="100%"`、`height="45px"`（等于该组件当前按钮高度）。
- Fill 与 Default 细线相同：`rgb(252, 81, 81)`。
- Label 设 `zIndex="2"`，保证文字始终位于红色 filler 上方。
- Hover 外层必须保持与 Default 相同的白色 Fill。红色只能来自内部 absolute filler；若外层同时变红，会出现整块背景先过渡、filler 动画失去“由下向上填充”读感的错误。

## 实施顺序

1. 先建立语义正确的 Default Button 与 Label/Link Properties。
2. 在 Default 内创建 absolute `filler`，先验证 1px 底线没有裁切。
3. 从 Default 创建一个普通 `Hover` Variant，复制结构。
4. 仅在 Hover 改 filler 的边界与 Label 的层级；不可修改 padding、外部宽高、gap 或按钮位置。
5. 设置 enter/leave 的 `SET_VARIANT`；Hover 使用 `spring-physics 250 30 1 0s`。如果项目要统一 Default 的退出感，须在真实实例中复检后再改，不要假设所有按钮都要同一 transition。
6. 删除被替代的旧 Hover Variant；检查组件画布中各 Variant 位置不重叠。
7. 回到至少一个实际 Page Instance 检查默认、hover、pressed、长 label 与窄容器。

## 验收

- Hover 过程中按钮外部尺寸、相邻元素位置、文字基线均不跳动。
- Default 的红线完整显示；若确认被父 Stack 裁切，先依照 `framer/basic` 检查尺寸与 Padding，再只在确认自然外溢的父级使用 `overflow="visible"`。
- Hover 时 filler 覆盖完整边界，Label 始终可读且层级高于 filler。
- 一个 Button Component 只有一条活动 Hover 路径；没有旧灰色或重复 Hover Variant。
- 组件画布没有 Ground node overlap、文本对比度或零尺寸可见层警告。
- Phone 不依赖 Hover；按钮在触摸状态下仍可辨认且可操作。

## 常见失效模式

| 症状 | 原因 | 修正 |
|---|---|---|
| 红线被裁掉 | filler 放在 clip 边界外，或父级尺寸错误 | 先检查尺寸与 padding；确认需要自然外溢时才按 basic 规则调整父级 overflow。 |
| Hover 时文字被红色遮住 | Label 没有明确高层级 | 在 Hover Label 设 `zIndex="2"`。 |
| Hover 改变按钮或布局尺寸 | filler 没有 absolute，或改了外层 padding/height | filler 必须 absolute；只改变 filler 边界。 |
| Framer 报对比度不足 | 检查器未采样 nested filler，误以为白色文字落在白色 Hover 外层 | 不要为消除静态提示把 Hover 外层改红；保持白色外层，确认真实 Preview 中 filler 覆盖后文字对比正确。 |
| 存在两个 Hover | 保留了旧的 gesture/普通 Hover 变体 | 删除被替代变体，只保留一条进入/离开路径。 |
| Component 画布重叠 | Variant 画布位置相叠 | 错开各 Variant 的画布位置；这不会影响页面实例。 |
