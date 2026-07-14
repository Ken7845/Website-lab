# 动效与交互要求

网站不能只是静态内容堆叠，需要加入克制、高级的交互动效。

动效方向：

整体感觉：
像高质量 Framer Showcase / Awwwards / 精品餐饮品牌网站。

不要使用大量花哨动画。
不要让页面像 SaaS landing page。

为了让动效看起来更加舒缓流畅，transition应该选择Spring physics stiffness250

动画应该增强：
- 品牌氛围
- 阅读节奏
- 空间感
- 高级感


## 页面进入动画

每个 section 在进入 viewport 时应该有自然出现效果：

例如：

- 内容从轻微下方移动并淡入
- 图片缓慢 reveal
- 标题和正文有轻微 stagger 延迟出现
- 卡片依次出现

避免：
- 突然出现
- 所有元素同时弹出
- 过度 bounce


## Hero 动效

Hero 应该有开场体验：

建议：

- 背景图片缓慢 zoom out / scale animation
- 标题和 CTA 分层出现
- 小标签先出现
- 主标题随后出现
- 描述和按钮最后出现


## 图片交互

图片不要只是静态展示。

加入：

- hover 时轻微 scale
- gallery 图片 reveal
- 图片进入时 mask reveal effect

保持自然。

图片 hover 的 scale 必须发生在“图片内容层”，不要让外层边框、卡片边界或布局容器一起 scale。

推荐结构：

```
Product Image Frame
└── Product Image
```

- `Product Image Frame` 负责固定尺寸、圆角、overflow clip、边框或卡片结构
- `Product Image` 负责 hover scale
- hover 时只放大框内图片内容，外框尺寸和边界保持稳定

这样图片会有精致的“镜头推进”感，而不是廉价的整块卡片弹动。

## Navbar

Navbar要有stick的效果，最好也要有向下滚动时隐藏，向上滚动时出现的效果

## 产品卡片

Menu/Product card:

Hover:

- 图片轻微放大
- 卡片有细微 elevation
- 信息保持稳定


不要：

- 大幅移动
- 夸张旋转
- 让整个卡片或边框一起 scale


## 按钮与链接动效

按钮 hover 应该以颜色、对比度、边框和文字颜色变化为主，尽量避免使用 scale。

尤其避免：

- CTA 按钮 hover 后整体放大
- 一组排列在一起的 menu/category/link 按钮使用 scale
- footer/nav/menu preview 这类密集链接在 hover 时发生位移或尺寸变化

这些区域的 hover 应该保持布局稳定。更好的处理方式：

- 背景颜色轻微变深或变浅
- 文本颜色轻微变淡
- border/text/fill 做克制的颜色反转
- underline / divider 的颜色或透明度变化

按钮 hover 后的颜色必须和当前 section 背景保持足够对比，不要让按钮 hover 色和背景混在一起。

例如：

- 主按钮在浅色背景上 hover 可以变为深色底、浅色字
- 次级按钮在浅色背景上 hover 可以保持边框感，只做浅色填充或文字变化
- 如果按钮所在 section 的背景和默认按钮颜色接近，必须使用另一个 button variant

不要为了统一所有按钮而牺牲对比度。Button component 的意义是方便创建不同 variant，并根据背景选择正确 variant。


## Button Component / Variant 使用原则

Framer 项目中重复出现的按钮必须优先做成 Component，而不是每个页面手动堆 Frame。

Button component 至少应考虑：

- Primary variant
- Secondary variant
- Dark / On Dark variant（用于深色或高对比背景）
- Text Link variant（用于 editorial link，例如 Read Our Story）

选择 variant 时先看按钮所在 section 的背景：

- 默认态要清楚可见
- hover 态也要清楚可见
- hover 不应突然从浅灰边框跳成黑色边框，除非这是明确设计意图
- 同一个按钮 component 可以有不同 variant，但每个 variant 的 hover 逻辑要稳定、可预测

创建 component 的目的不是“所有按钮长一样”，而是让按钮在不同背景下可维护、可复用、可快速换 variant。


## Menu / Footer / Category Link Hover

菜单预览、footer explore、导航链接、分类列表这类密集排列的交互项，hover 不要使用 scale。

推荐：

- 背景色微微变深
- 文字透明度轻微变化
- divider / underline 变深
- cursor pointer

禁止：

- hover scale
- hover 后推开相邻元素
- hover 后改变 stack/grid 的视觉尺寸

这些链接应该拆成独立 layer，并放进 Stack 中，而不是写成一段 multiline text。这样才能单独设置 link、hover、间距和 variant。

## Component row hover

当一整行列表项被做成 Framer component 后，hover 效果优先做成组件内部的 Hover Gesture Variant。

不要只给页面上的 component instance 加一个外层 hover effect，然后以为组件本身已经有 hover 状态。这样很容易在组件化、复制实例或切换 breakpoint 后丢失。

推荐做法：

```text
Archive Option Row
├── Fighting the Chemistry
│   └── Hover gesture variant: darker fill
├── Campus
│   └── Hover gesture variant: darker fill
└── Dutch Treat Restaurant
    └── Hover gesture variant: warmer darker fill
```

Hover row 应该保持布局稳定：

- 改背景色 / fill。
- 可以轻微改文字透明度。
- 可以改 border/divider 对比度。
- 不要 scale 整行。
- 不要让 hover 后行高、宽度或相邻元素位置变化。

如果 Framer review 提示 hover scale 被 parent overflow clip，直接改成不 scale。

本次 Ken Studio Works 的教训：

```text
外层 instance hoverEffect
→ preview 里看不到稳定变亮
→ 改为 component Hover Gesture Variant 后才符合 Framer 原生逻辑
```

以后密集 archive/menu row 的 hover，默认走 Gesture Variant。


## 页面滚动体验

整体滚动应该有节奏：

用户向下浏览时：

- 内容逐渐展开
- section 之间有呼吸感
- 图片和文字形成视觉关系


参考感觉：

不是动画网站，
而是一个真实高级品牌网站。


## 动效原则

优先级：

1. 页面进入 transition
2. 图片 reveal
3. Typography animation
4. Hover interaction

保持：
smooth
subtle
premium
natural
