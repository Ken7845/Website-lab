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

## Transition 参数的归属

- 先读取当前项目的 `PROJECT.md`、`DECISIONS.md` 和已验收组件；已有项目动效契约时，复用该项目参数，而不是重新猜测一组数值。
- `Spring physics stiffness 250` 可以作为尚未建立项目契约时的起始提案；必须在项目内补全并记录 damping、mass、delay 等实际参数，再作为该项目的可复用依据。
- 不把某个项目的数值提升为所有网站的强制默认值。AURELIA 的 `spring-physics 250 30 1 0s` 是该项目的已批准证据，不是跨项目的唯一答案。
- 同一组件的 Default、Hover、Open、Closed 等相关状态默认使用同一套 transition；只有状态语义或真实 Preview 证明需要差异时才拆分。
- Press 反馈应克制、可感知即可；避免让整行或主操作在点击时产生明显缩小。
- Height reveal 只能插值连续的几何或视觉属性。`visible` 是二元开关：若 Drawer 在 Closed 状态被设为 `visible: false`，它会在 Open 时直接出现，不能被当作平滑进入动画。要做 Navbar 内展开，应让同一 Drawer 保留在两个状态中，再用外层高度与 `overflow: clip` 控制可见范围；要做浮层进入，则使用 Overlay 的 opacity / position enter transition。


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

## Gallery Lightbox 设计原则

Gallery 需要放大查看图片时，优先使用 Framer 原生 **Lightbox Effect**。

不要因为 Gallery 有很多图片，就默认创建：

- 多个 Fixed Overlay
- 每张图片一个 Overlay
- 每张图片一个 Component Variant
- 为简单放大效果引入 Custom Code

原生 Lightbox 已经包含打开、关闭、背景遮罩和响应式适配。对于只需要“点击图片后放大查看”的 Gallery，它比 Overlay 更轻、更容易维护，也更符合 Framer 模板的可编辑性要求。

### 推荐层级

简单 Gallery：

```text
Gallery Grid
├── Gallery Image 01 + Lightbox Effect
├── Gallery Image 02 + Lightbox Effect
└── Gallery Image 03 + Lightbox Effect
```

图片直接保持为 Grid / Stack 的子层。Desktop 可以使用跨列、跨行的编辑式排版；Tablet 简化为双列；Phone 通常改为单列。

### Lightbox 转场

Lightbox 不应点击后直接闪现。

必须设置明确的 `lightboxEffect.transition`，让缩略图到放大图之间形成连续、可感知但不过慢的转场。

推荐：

```text
spring-duration 0.55s 0.18 0s
```

可调范围：

- Duration：约 `0.45s–0.60s`
- Bounce：约 `0.12–0.22`
- Delay：通常 `0s`

目标感觉：

- 图片从原位置自然展开，而不是突然切换。
- 有轻微空间变化，但没有夸张弹跳。
- 关闭时同样保持连续感。
- 动画足够明显，用户能理解图片进入了放大查看状态。

如果使用 Spring Physics，继续遵循整体动效规则，以约 `stiffness 250` 为起点；如果 Lightbox 当前使用 Time Based Spring，则优先调整 Duration 与 Bounce，不要混用无效参数格式。

### Lightbox 尺寸

放大不等于铺满整个屏幕。

餐饮、品牌与 Editorial Gallery 应保留遮罩周围的空间，让用户仍能感知页面与图片之间的层级。

推荐起点：

```text
Desktop maxWidth: 820–900px
Desktop padding: 40–56px
Phone padding: 24–32px
Backdrop opacity: 0.78–0.84
```

Morrow & Grain 的有效参数：

```text
maxWidth: 860px
Desktop padding: 48px
Phone padding: 28px
backdrop: rgba(28, 23, 19, 0.82)
transition: spring-duration 0.55s 0.18 0s
```

不要默认使用接近 viewport 宽度的 Lightbox。图片过大会产生压迫感，也会削弱精品餐饮网站需要的留白与克制感。

### Component 与 Variant 的使用边界

不要为了给 Gallery 填入不同照片而创建 20 个图片 Variant。

如果图片卡片确实需要做成 Component，优先把图片做成可编辑的 Image / Fill 属性，让不同 Instance 直接替换照片：

```text
Gallery Photo Component
└── Image Layer
    └── Fill / Image Property
```

Variant 应用于真正的状态或结构差异，例如：

- Landscape / Portrait
- Default / Featured
- With Caption / Without Caption
- Hover / Pressed Gesture Variant

不同照片本身通常只是内容差异，不应该自动变成 20 个 Variant。

当前 Gallery 如果每张图片只是一个独立图片层，并且布局依赖不同的 grid span，直接在图片层使用 Lightbox Effect 往往最清晰。

### 什么时候才使用 Overlay

只有原生 Lightbox 无法满足内容和交互需求时，才使用 Fixed Overlay。

例如：

- 放大图旁边需要标题、说明、价格或项目资料。
- 需要自定义上一张 / 下一张导航。
- 每张图需要不同的 CTA 或交互控件。
- 需要视频、音频或混合媒体内容。
- 需要完全自定义打开和关闭动画。

如果选择 Overlay，应先判断能否使用一个可复用 Overlay 和动态内容，而不是为 20 张图片分别创建 20 个 Overlay。

### Gallery Hover 与 Lightbox 的关系

Lightbox 图片不需要依赖整块图片的 hover scale 来提示可点击。

优先使用：

- `cursor: zoom-in`
- 轻微透明度或色调变化
- 图片内容层的克制 scale

如果 Gallery Grid 使用 `overflow: clip`，外层图片整体 scale 容易被网格边缘裁切。遇到 Framer review 的 overflow clip 警告时：

- 直接取消外层 scale；或
- 使用“外框 + 内部图片层”结构，只放大内部图片。

不要为了保留 hover scale 而把整个 Gallery 容器改成不受控的 overflow visible。

### Lightbox 检查清单

交付前按 [evidence selection](../workflows/image-workflow.md#evidence-selection) 对适用路径实际点击检查；Preview 不可用时记录明确用户观测或 Blocked：

- 20 张图片是否都能打开。
- 打开和关闭是否都有连续转场，而不是闪现。
- 放大图是否过大或太靠近屏幕边缘。
- 图片主体是否完整，是否发生错误裁切。
- Backdrop 是否足够区分页面，但没有完全吞掉品牌氛围。
- Desktop、Tablet、Phone 是否分别有合理边距。
- 是否可以通过点击背景或关闭控制退出。
- 页面滚动、Navbar 和其他高层级元素是否会穿透 Lightbox。
- Transition 参数是否被 Framer 正确接受，而不是因为格式错误退回默认值。

本次 Morrow & Grain 的结论：

```text
20 个图片 Variant + 20 个 Overlay
→ 结构复杂，维护成本高，不适合简单 Gallery

普通图片层 + 原生 Lightbox Effect + 明确 Transition
→ 更轻、更稳定，也更适合 Marketplace Template
```

## Phone Navbar Menu Overlay：一次成型方法

### 本次耗时的根因

Morrow & Grain 的手机菜单之所以发生多轮修改，不是视觉方案复杂，而是一开始选错了 Framer 原生交互类型：

```text
手机导航菜单
→ 错误起点：页面级 Fixed Overlay + Component Event Variable
→ 结果：跨 Component / Layout Template 转发事件，Preview 只出现遮罩，内容没有稳定渲染

手机导航菜单
→ 正确默认：Menu Trigger 内的 Relative Overlay
→ 结果：触发器、菜单和关闭行为处于同一 Component Scope，结构更短，Preview 稳定
```

时间和 Token 主要浪费在：

- 没有先按交互类型选择 Relative Overlay / Fixed Overlay。
- 为跨组件触发建立了不必要的 EventHandler Variable 和实例事件映射。
- 完整搭建后才第一次真实点击，导致结构问题暴露太晚。
- 每次修改都输出过大的节点树和 Review，而不是只回读 Trigger、Overlay、Phone Variant。
- 已经确认的 Metadata、Alt、Link 等批量任务被混入交互调试，增加上下文切换。

### Overlay 类型决策

先判断交互是不是依附某个触发器：

| 需求 | 默认 Framer 方案 |
|---|---|
| Navbar menu、dropdown、popover、tooltip | Relative Overlay |
| 图片简单放大 | Lightbox Effect |
| 真正覆盖页面的 modal、复杂 lightbox | Fixed Overlay |
| 同一区块的展开/折叠状态 | Component Variant |

手机 Navbar 的默认方案是 Relative Overlay。只有明确需要全屏遮罩、锁定背景滚动、焦点管理和页面级居中 Modal 时，才使用 Fixed Overlay。

### 已验证的组件层级

```text
Navbar Component
├── Desktop Variant
├── Tablet Variant
└── Phone Variant
    └── Navbar Surface
        ├── Logo Link
        └── Menu Trigger
            ├── Menu Label
            └── Phone Navigation Overlay (Relative Overlay)
                ├── Menu Header
                │   ├── Brand
                │   └── Close Button
                ├── Navigation Links
                │   ├── Home
                │   ├── Menu
                │   ├── About
                │   ├── Gallery
                │   └── Visit
                ├── Divider
                └── Contact CTA (Button Instance)
```

Overlay 直接挂在 `Menu Trigger` 下，Trigger 使用 `SHOW_OVERLAY`，Close 使用 `DISMISS_OVERLAY`。不要为了这个结构创建 Component Event Variable，也不要把菜单拆到 Layout Template 再跨 Scope 连接。

### Morrow & Grain 已验证参数

```text
Trigger touch target: 不小于 44px 高
Overlay type: Relative Overlay
Placement: bottom
Alignment: end
Offset Y: 12px
Collision Detection: true
Panel width at 390px: 340px
Panel maxHeight: 82vh
Panel padding: 24px 22px 28px
Panel gap: 24px
Background: #29231F
Radius: 2px
Transition: spring-duration 0.36s 0.16 0s
Enter opacity: 0
Enter y: -14
Enter scale: 0.98
```

这个组合的目标是：菜单明显展开，但没有弹窗式压迫感；面板与触发按钮有清楚关系，同时在 390px Phone 保留约 25px 的左右安全空间。

### 一次写入顺序

同一次修改中完成：

1. Phone Variant 隐藏 Desktop Navigation Row 和旧 CTA。
2. 创建语义化 Menu Trigger，并保留 44px 触控高度。
3. 在 Trigger 内创建 Relative Overlay。
4. 一次写入 Header、Close、全部 Links、Divider、Contact Button Instance。
5. 同时设置真实页面链接、`SHOW_OVERLAY` 和 `DISMISS_OVERLAY`。
6. 设置 Placement、Collision、尺寸和动画。
7. 回读 Trigger、Overlay、Phone Variant 三个目标节点。
8. 在 390px Preview 中只做一次完整路径：Open → Close → 再 Open → 点击一个 Link。

不要先创建空 Overlay、再逐项补链接、再单独补动画。已验证的结构应一次写完，验证用于发现意外情况，不用于边看边设计。

### 最小验证矩阵

| 检查 | Desktop | Tablet | Phone 390 |
|---|---|---|---|
| 原导航 | 可见 | 可见 | 隐藏 |
| Menu Trigger | 隐藏 | 隐藏 | 可见 |
| Overlay 打开 | 不适用 | 不适用 | 正常 |
| Close | 不适用 | 不适用 | 正常 |
| 核心链接 | 原导航可用 | 原导航可用 | Overlay 可用 |
| 横向溢出 | 无 | 无 | 无 |

Phone 再补一次 320px 静态检查即可。除非发现问题，不重复打印完整页面树或进行多轮整页截图。

### Fixed Overlay 的使用边界

如果需求明确是全屏 Modal：

- Fixed Overlay 必须位于页面或 Layout Template Scope，不能放入 ComponentNode。
- Component 内触发器才需要暴露 EventHandler Variable，由页面实例连接 `SHOW_OVERLAY`。
- 面板是 Fixed Overlay 的绝对定位子层，必须明确位置或中心锚点。
- 第一次应先做最小可见面板并立即 Preview 验证，再填充复杂内容。

这条路径比 Relative Overlay 成本高，不应作为手机导航的默认方案。

### Token 与会话规则

- 全程复用一个 Framer Session，不因为等待变慢而 reconnect。
- 第一次读取后保存 Component、Variant、Trigger 和 Page IDs，不重复搜索。
- 回读深度控制在 2–4，只输出交互相关属性。
- 工具返回过长或超时后先读取当前状态，不重复提交同一写入。
- Overlay 完成后再批量做 SEO、Alt、Links；不要在交互调试中来回切换任务类型。

### 完成标准

- Phone 用户无需 Footer 即可访问全部核心页面。
- 菜单有连续进入动画，不闪现、不夸张弹跳。
- Close、外部点击和键盘关闭符合 Framer 原生行为。
- 面板不超出 320px / 390px 画布。
- Navbar Sticky 与滚动隐藏 Variant 不受影响。
- Desktop、Tablet 仍使用原导航。
- Preview 已真实点击，不仅检查画布。

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

当一整行列表项被做成 Framer component 后，先判断 Hover 是否真的需要共享状态 Variant：

- 所有实例使用完全相同的 Hover 样式：可以做一个共享 Hover Gesture Variant。
- 不同档案袋或记录需要不同 Hover Fill：使用页面 Instance 的 Hover Effect / Color Property。

不要为每条记录分别创建 Hover Gesture Variant。实例化后按 [evidence selection](../workflows/image-workflow.md#evidence-selection) 验证真实 pointer Hover；Phone 检查 touch/static 行为，不能只根据设置判断。

推荐做法：

```text
Archive Option Row
├── Desktop
└── Phone

Page Instances
├── Fighting the Chemistry: content + surface + hover properties
├── Campus: content + surface + hover properties
└── Morrow & Grain: content + surface + hover properties
```

若使用 Hover Variant，它只表达共享状态，不表达项目内容。不同项目或档案袋的基础色与 Hover 色通过 Instance 的 Fill / Color Properties 或 Hover Effect 设置。

Hover row 应该保持布局稳定：

- 改背景色 / fill。
- 可以轻微改文字透明度。
- 可以改 border/divider 对比度。
- 不要 scale 整行。
- 不要让 hover 后行高、宽度或相邻元素位置变化。

如果 Framer review 提示 hover scale 被 parent overflow clip，直接改成不 scale。

本次 Ken Studio Works 的参考模式：

```text
ArchiveOptionRow 只保留 Desktop / Phone
→ 每个页面 Instance 设置 content、base fill、hover fill、link、cursor preview
→ 新项目只复制 Instance，不增加 Variant
```

以后密集 archive/menu row 的 hover，默认先复用 Instance 模板；只有所有实例共享同一状态样式时才增加一个共享 Gesture Variant。


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
