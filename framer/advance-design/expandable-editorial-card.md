# Framer 高级组件：可展开 Editorial Card

## 适用范围

用于菜单、作品、产品或案例列表中的长条卡片：Desktop / Tablet 默认显示图片、标题和短说明；点击后卡片变高、图片放大、短说明切换为较长故事；Phone 保持静态，避免把桌面 Hover 和展开逻辑强加给触控阅读。

## 核心决策

- 一个共享 Component 服务全部条目；每条内容通过 Instance Properties 写入。
- 普通 Variant 只表达断点与展开状态：`Desktop`、`Tablet`、`Phone`、`Desktop Expanded`、`Tablet Expanded`。
- Hover 使用从对应折叠 Variant 创建的 Gesture Variant，不为每条记录复制 Hover。
- `Story` 是一个多行 String Property；展开态同时隐藏 `Title` 与 `Description`，让文字区域只显示 `Story`，不创建内容 Variant。
- 折叠态复用 Home 已存在的 `Arrow Essentials / Arrow Right`（24×24、`#1A1A1A`、Stroke Width 1.6），展开态使用同一 Icon Set 的 `Arrow Up`。
- Phone 不继承点击事件，不显示箭头，也不依赖 Hover 才能获得信息。
- Page Instance 的宽度由外层列表 Stack 拥有，使用 Fill（`1fr`）；不要用 `100%` Relative 或组件画布 Variant 的固定宽度代替页面响应式所有权。
- 状态切换统一使用 `spring-physics 250 30 1 0s`；其中 stiffness 固定为 250。

## 推荐层级

```text
Expandable Editorial Card Component
├── Properties
│   ├── Image
│   ├── Title
│   ├── Description
│   └── Story (multiline)
├── Desktop / Tablet / Phone
│   ├── Image
│   ├── Copy
│   │   ├── Title
│   │   ├── Description (visible)
│   │   └── Story (hidden)
│   └── Story Arrow → Arrow Essentials / Arrow Right
├── Desktop Expanded / Tablet Expanded
│   ├── Larger Image
│   ├── Copy
│   │   ├── Title (hidden)
│   │   ├── Description (hidden)
│   │   └── Story (visible)
│   └── Story Arrow → Arrow Up
└── Desktop Hover / Tablet Hover
    └── Same external dimensions; surface, border, or arrow emphasis only
```

## 原生交互模型

1. 从 Desktop / Tablet 折叠 Variant 各复制一个普通 Expanded Variant。
2. 折叠卡片用原生 `SET_VARIANT` 精确指向同断点 Expanded；Expanded 精确返回同断点折叠态。
3. 从两个折叠 Variant 各创建一个 `gesture="hover"` Variant。Hover 保持 width、height、padding、gap 和图片尺寸不变，只改变 Surface / Border / icon emphasis。
4. Phone Replica 必须显式清除从主 Variant 继承的 `onTap`，并隐藏箭头。
5. 使用 `auto` 高度与连续 transition，让父级 Stack 接受展开后的真实高度；不要用 Overlay 模拟卡片展开。

## AURELIA 已验证实现（2026-08-11）

```text
Component: MenuDishCard

Properties:
Dish Image
Dish Name
Description
Story

Desktop collapsed: 1056px wide, 20px padding, 32px gap, image 240×180
Desktop expanded:  1056px wide, 28px padding, 40px gap, image 380×285

Tablet collapsed: 730px wide, 18px padding, 28px gap, image 220×165
Tablet expanded:  730px wide, 20px padding, 28px gap, image 300×225

Phone: 350px wide, vertical static layout, no arrow, no click-to-expand
Page Instance width: 1fr / Fill inside the movement Stack at all three breakpoints
Arrow affordance: 44×44 wrapper, Arrow Essentials Arrow Right / Arrow Up, icon 24×24, #1A1A1A, stroke 1.6
Transition: spring-physics 250 30 1 0s
```

七个 `/menu` Page Instances 各自写入独立 Image、Dish Name、Description、Story 和 Image Alt。增加第八条时，只复制一个 Page Instance 并修改 Properties；不得增加新的内容 Variant。

## 验收

- 折叠态、Hover 态外部尺寸一致；Hover 不推开相邻卡片。
- Desktop 与 Tablet 点击路径为 `Collapsed → Expanded → Collapsed`，且不会跨断点跳 Variant。
- Expanded 图片明显增大，Title 与 Description 完全隐藏，文字列只显示完整 Story，箭头向上。
- 在页面 Preview 中缩放父容器时，卡片宽度持续贴合外层边框；七个 Desktop、Tablet、Phone 实例都必须是 Fill（`1fr`）。
- Phone 无箭头、无 Hover、无展开事件，阅读顺序保持图片 → 标题 →短说明。
- 第一、中间、最后实例的 Story 与图片 Alt 均不同，Replica 正确继承 Page Instance 数据。
- 长标题、最长 Story、横竖图片替换和缺失可选字段不造成横向溢出或空白分隔。
- Reduced Motion 下最终折叠/展开状态仍清楚，信息不依赖动画本身。

## 常见失效模式

| 症状 | 原因 | 修正 |
|---|---|---|
| Phone 点击后跳到 Desktop Expanded | 主 Variant 事件被 Replica 继承 | 在 Phone Variant 上显式清除对应 `onTap` action |
| Hover 时列表跳动 | Hover 改了图片、padding、gap 或外部 height | 恢复与折叠态相同尺寸，只改颜色、边框或图标强调 |
| 七道菜需要七组 Variants | 把内容当成状态 | 保留一组结构 Variants，把内容移到 Properties / CMS |
| 展开后仍显示短说明 | Description / Story visibility 未在 Expanded override | Expanded 明确设 Description hidden、Story visible |
| 展开后仍显示菜名 | 只切换了 Description / Story | Expanded 同时设 Title hidden，文字区域只保留 Story |
| 画布上正常、Preview 中卡片长度不跟随边框 | Page Instance 使用 `100%` Relative，宽度所有权不清楚 | 在父 Stack 中把每个 Page Instance 设为 Fill（`1fr`），组件内部 Copy 保持 `1fr` |
| 箭头与 Home 风格不一致 | 只找了相似的 Phosphor 图标 | 读取 Home 参考节点，复用同一 `Arrow Essentials` 图标集、颜色、尺寸与 Stroke Width |
| 修改一张图影响全部卡片 | 在 Component Definition 写入内容 | 回到 Page Instance 修改 Image Property 与 Alt |
| Gesture Variant 截图失败 | Gesture Variant 不是普通 top-level Variant | 用结构回读验证尺寸与 token，并截图对应普通折叠 / 展开 Variant |
