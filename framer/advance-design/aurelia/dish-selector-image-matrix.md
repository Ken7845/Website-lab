
# Framer 高级组件：Dish Selector 图片矩阵与文字 Reel

> Status: **Canonical selector / reel; project-specific**.
> Provenance: AURELIA fixed seven-item selector, exact recorded instance 2026-08-10.
> Verification boundary: Parameters belong to this example; content count, width and breakpoint changes need fresh validation. Repository classification added 2026-10-03; no fresh Canvas verification.

## 适用范围

用于固定数量的菜品、作品或产品选择器：点击缩略图后，当前主图横向推入，其他缩略图保持较暗和较小；数字、标题与说明在各自裁切窗口内同步滚动。

此模式适合“图片是叙事主体、文字是随选择状态更新的辅助信息”的场景。它不是普通 gallery grid，也不应用于条目数量会频繁增减的 CMS 列表。

## 交互目标

- 点击任一缩略图，切换到对应 Item Variant。
- 当前缩略图放大并提高亮度；其余项缩小、降低亮度，但仍可点击。
- 一个连续的 Image Strip 横向移动，令新图从右侧进入；不采用逐张显示/隐藏或 opacity crossfade。
- Number、Title、Description 是三个独立的 vertical reel：同一状态一次只显示各自的一行。
- 每个断点各有独立坐标系。Phone 不是 Desktop 的缩小副本。

## 推荐组件模型

```text
DishSelector Component
├── Content Properties
│   ├── Dish 01–07 Image       # 同一属性绑定主图和缩略图
│   ├── Dish 01–07 Title
│   ├── Dish 01–07 Story       # Desktop / Tablet
│   └── Dish 01–07 Phone Description
├── Variants
│   ├── Item 01–07 / Desktop
│   ├── Item 01–07 / Tablet
│   └── Item 01–07 / Phone
└── Selector Layout
    ├── Meta Column
    │   ├── Number Window (fixed, clip) → Number Reel
    │   ├── Title Window (fixed, clip) → Title Reel
    │   ├── Long Description Window (Desktop/Tablet only) → Long Reel
    │   └── Short Description Window (Phone only) → Short Reel
    ├── Image Viewport (fixed, clip) → Image Strip
    │   ├── Slide 01
    │   ├── …
    │   └── Slide 07
    └── Preview Rail
        ├── Preview 01 → SET_VARIANT Item 01
        ├── …
        └── Preview 07 → SET_VARIANT Item 07
```

## 内容、状态与可替换路径

Variant 只负责“当前选中项 + 断点”的状态，不负责储存不同图片或菜品文案。每一项内容应由 Component Property 提供：主图和对应缩略图必须引用同一 Image Property，避免模板用户换图时只改到其中一处。

7 个固定内容项可使用 21 个状态（7 项 × 3 断点）；若数量会动态变化，应改用 CMS / Carousel，而不是继续堆叠 Variant。

## 图片矩阵的核心：固定裁切框，移动单一轨道

`Image Viewport` 是裁切框和位移坐标系，必须 `layout: null`、`overflow: clip`，并在每个断点使用固定宽高。每张 slide 的固定宽高必须等于该断点的 Viewport。

```text
Image Strip left = -(itemIndex × slidePitch) + opticalCorrection
```

`slidePitch` 不是父容器剩余宽度，也不能用 `1fr` 或百分比推导。父级宽度变化时，只有 Viewport、slide 与 left 同属稳定坐标系，边框才不会露出上一张/下一张图或出现空隙。

### 底层实现逻辑：两个独立的尺寸系统

这个组件同时有两个系统，不能混为一谈：

```text
外部响应式系统
Page Section → Component Instance → 可用空间 / breakpoint
        │
        └── 选择对应的 Desktop / Tablet / Phone Variant

内部动画坐标系统
Fixed Viewport / Window → Fixed Slide / Reel Row → state left / top
```

外部 Instance 可以随着页面收缩、换列或拥有 `max-width`；它的职责是提供足够的空间并切到正确的 Variant。内部 Viewport、slide、文字窗口和 reel row 的职责则是维持不变的像素坐标。不要让一个节点同时承担这两种职责。

对于图片：`Viewport.width === Slide.width === slidePitch`。对于文字：`Window.height === row.height`，而 `reelPitch === row.height + gap`。因此切换状态只是在同一条连续轨道上移动一个确定距离，而不是重新计算或缩放图片/文字。

```text
Selected index i (0-based)
imageStrip.left = -(i × imagePitch)
numberReel.top  = -(i × numberPitch)
titleReel.top   = -(i × titlePitch)
bodyReel.top    = -(i × bodyPitch)
```

先使用数学基准对齐边框，再允许每个状态做极小的 `opticalCorrection`。光学校正只能在截图证明边框准确后加入，不能用来掩盖错误 pitch。

### 为什么图片不会被过度拉伸

外层 Section 可以响应；主图轨道不能响应式拉伸。正确关系如下：

```text
Responsive outer section
└── Component Instance (为当前 Variant 留出稳定可用空间)
    └── Image Viewport — Fixed width + Fixed height + overflow clip
        └── Image Strip — Fixed total width, horizontal Stack, gap 0
            └── Each Slide — exactly Viewport width × Viewport height
                └── Image Fill — 在自身 slide 内按既定 crop / focus 展示
```

- Viewport 是唯一的可见边界；它不使用 `Fill`、`%` 或 `1fr` 参与轨道计算。
- 每张 slide 必须与 Viewport 同尺寸。`fit` / `cover` 只决定图像在 slide 内的裁切方式，不能改变 slide 尺寸。
- Instance 若变窄到不能容纳该 Variant 的固定 Viewport，应由页面切到 Phone Variant、改外层排版或限制 Instance 最大宽度；绝不能让 Desktop slide 被压缩。
- Preview 要测试“可用空间变化”而不只是设备名：调整页面实例所在父容器/Preview 宽度后，Viewport 边界、01/04/07 的 strip left、图片焦点与相邻 slide 残留都必须保持正确。

缩略图 rail 不移动图片轨道；它只触发 `SET_VARIANT` 并显示 selected 状态。推荐将当前项的 scale / brightness 放在 Preview 本身，而非外层 rail，以免 hover 或 selected 状态推开相邻项。

## Reel 的核心：窗口高度 + 实际 pitch

每段会滚动的文字都需要独立结构：固定高度、裁切溢出的 Window 包裹一个 vertical Stack Reel，Reel 中每项为独立 Rich Text。不要把所有数字或所有文案写进一个文本框。

```text
reel top = -(itemIndex × rowPitch) + opticalCorrection
rowPitch = actual rendered row height + stack gap
```

必须按实际 Rich Text 的 line-height 和 Stack gap 测量 `rowPitch`，不能仅按 font-size 猜算。长说明与 Phone 短说明必须是两条不同轨道：两者行高、窗口高度和 pitch 不同。`/07` 等恒定部分放在 Number Reel 外，避免它随当前号码滚动。

所有轨道采用相近的原生 spring transition，使图片、数字、标题和说明在同一方向、相近时序完成；避免 opacity crossfade 造成图像残影或方向感消失。

### 文字改变后的对齐策略

文字变更不是只改内容：先判断它会不会改变 row 的实际高度。若 Phone Description 是一行模式，就必须同时满足：

1. 每项文字可在 Short Description Window 内单行显示。
2. 每个 Rich Text row 使用相同的固定 height；不要让某一条以 `auto` 高度换行。
3. 文字 reel 的 `top` 按 `row.height + gap` 重算，所有 7 个 Phone 状态都使用同一 pitch。
4. 只有上述三项成立时，才可以只改 Phone Description Property；不要顺手改图片轨道、数字轨道或 Desktop/Tablet 长说明。

若一条文本无法单行容纳，优先缩短文案，而不是改小字号、减小 gap 或让单行轨道变成两行。若业务明确要求两行，应新建 Phone 两行说明 Variant / 独立 Reel，并完整重算 window、row height、pitch 与 7 个 state top；这不是一个“文案小改”。

## AURELIA 已验证尺寸（固定 7 项）

| 断点 | Image Viewport / Slide | Image Strip | 图片 left pitch | Number pitch | Title pitch | Description pitch |
|---|---:|---:|---:|---:|---:|---:|
| Desktop | 585px × 410px | 4091px × 410px | 585px（再做微小光学校正） | 约 108px | 52px | 94px |
| Tablet | 500px × 410px | 4091px × 410px | 500px | 约 107px | 52px | 94px |
| Phone | 350px × 250px | 2450px × 250px | 350px | 68px | 48px | 30px（短说明） |

Phone 的完整状态位置：

```text
Image Strip left: 0, -350, -700, -1050, -1400, -1750, -2100
Number Reel top:  0,  -68, -136,  -204,  -272,  -340,  -408
Title Reel top:   0,  -48,  -96,  -144,  -192,  -240,  -288
Short Reel top:   0,  -30,  -60,   -90,  -120,  -150,  -180
```

Phone 短说明窗口为 230px × 20px；每一行说明必须在这一宽度内保持一行，避免换行改变 30px pitch 并破坏同步。AURELIA 当前 transition：文字/数字为 `spring-duration 0.42s 0.16 0s`，Phone 图片轨道为 `spring-duration 0.52s 0.18 0s`。

## 实施顺序

1. 在页面实例中先确定每个断点可提供的空间。
2. 在组件内建立独立的 Desktop、Tablet、Phone Variant；先固定 Viewport，再固定全部 slide。
3. 绑定 Image / Title / Story / Phone Description Properties；同项主图和缩略图复用一个 Image Property。
4. 建立 Number、Title、Long Description、Short Description 四条独立 Reel；仅在相应断点显示。
5. 根据实际 row height + gap 计算每条 Reel 的 top；根据 slide 宽度计算 Image Strip left。
6. 将每个 Preview 接到原生 `SET_VARIANT`；为 selected 状态设置清晰的亮度/缩放差异，Phone 不依赖 hover。
7. 先在外部实例验证 Item 01、04、07，再检查中间项与不同可用宽度。

## 外部 Preview：响应式验证方法

预览不以 Component Canvas 为准，按以下顺序在实际页面 Instance 验证：

1. 记录目标 breakpoint 的 Instance 可用宽度、Image Viewport 尺寸、slide 尺寸、各 reel window 尺寸与 state pitch。
2. 在 Desktop / Tablet / Phone 分别选中 01、04、07；首项检查起点，中项检查同步，末项检查轨道尾部。
3. 对每个断点只改变外层的可用空间一次：Desktop/Tablet 检查固定 Viewport 没有被父级拉伸；Phone 在 320px 与 390px 检查主图没有溢出、文本不换行、Preview 仍可触控。
4. 触发一次缩略图切换，确认图片只由 Image Strip `left` 移动，数字/标题/文字只由各自 Reel `top` 移动；不能以 opacity 或 visibility 替代移动。
5. 若问题出现，先沿着 `Section → Instance → Variant → Viewport/Window → Strip/Reel` 找第一个尺寸或状态不一致的节点。不要先缩字号或逐张移动图片。

### 一次性验收矩阵

| 检查项 | 01 | 04 | 07 | 宽度变化 | 通过标准 |
|---|---:|---:|---:|---:|---|
| 图片窗口 | 必测 | 必测 | 必测 | 必测 | 无露白、无相邻 slide、无非预期拉伸 |
| 数字 Reel | 必测 | 必测 | 必测 | — | 当前数字完整，`/07` 不移动 |
| 标题 Reel | 必测 | 必测 | 必测 | — | 仅当前标题处于窗口内 |
| Phone 短说明 | 必测 | 必测 | 必测 | 320 / 390 | 单行、无裁切、top 为统一 pitch |
| Preview rail | 必测 | 必测 | 必测 | 390 | 当前项显著且所有缩略图可点击 |
| Desktop / Tablet 回归 | — | — | — | 各一次 | Phone 编辑未改变其文案、轨道或图片 |

## 验收与回归检查

- Item 01：主图左边框、数字、标题与短说明同时落在窗口起点。
- Item 04：图片没有相邻 slide 残留；三个文字 reel 都显示第 4 行。
- Item 07：轨道末端不露白、不超出、不跳位。
- Phone 320px 与 390px：短说明不换行，无横向溢出，Preview 仍可触控。
- Desktop / Tablet：各自轨道位置不因 Phone 编辑被重算或覆盖。
- 更换某项 Image Property：主图和缩略图同步变化，状态映射、轨道长度和数字总数不变。
- Reduced Motion：最终选中项、数字与文字仍明确；动效不是理解状态的唯一手段。

## 常见失效模式

| 症状 | 常见原因 | 修正 |
|---|---|---|
| 切换后露白或看到相邻图片 | Viewport/slide 使用 Fill、百分比或 `1fr` | 改为每断点 Fixed，并按真实 pitch 重算 left |
| 数字或文字滚动后上下残留 | Window 未 clip，或每行不独立 | 固定 Window 高度 + `overflow: clip` + 独立 Rich Text 行 |
| Phone 文案滚动错位 | 短说明换行，或复用了长说明 pitch | 保持单行；短说明单独 Window / Reel / 30px pitch |
| 替换图片时主图和缩略图不一致 | 使用两份 Fill 而非同一个 Property | 两处绑定同一个 Image Property |
| 选中缩略图推开其他项 | 对外层 rail 或布局容器做 scale | 只对 Preview 内部视觉层做 selected/hover 效果 |
| Desktop / Tablet 被 Phone 改动污染 | 在主 Variant 改值，而非 Phone override | 只编辑对应 Phone Variant；回读其他两端关键值 |

## 修改约束

若任务只要求缩短 Phone 文案：仅编辑 `Dish 01–07 Phone Description` Properties，并确认其一行长度。不得修改图片 Property、Image Strip、Image Viewport、slide 尺寸、数字/标题/短说明 Reel 的 top 或 gap，也不得改 Desktop / Tablet Variant。

## 1:1 Example — AURELIA DishSelector（2026-08-10）

以下是当前 AURELIA 的固定七项实现。它可按相同结构、数值、绑定与状态复刻；图片源可替换，但数量必须仍为 7。

### Component、Properties 与状态

```text
Component: DishSelector

Image properties:
Dish 01 Image … Dish 07 Image
  └── 每项同时绑定 Main Image NN 与 Preview NN

Text properties:
Dish 01 Title … Dish 07 Title
Dish 01 Story … Dish 07 Story                 # Desktop / Tablet
Dish 01 Phone Description … Dish 07 Phone Description # Phone only

Variants (21):
Pasta, Bread, Dark course, Blue plate, Shellfish, Avocado, Salad
Pasta Tablet, Bread Tablet, Dark course Tablet, Blue plate Tablet,
Shellfish Tablet, Avocado Tablet, Salad Tablet
Pasta Phone, Bread Phone, Dark course Phone, Blue plate Phone,
Shellfish Phone, Avocado Phone, Salad Phone
```

每个 `Preview NN` 使用原生 `SET_VARIANT` 指向同 index 的状态。当前项 Preview 亮、较大；未选中项保留可点击面积。Phone 不以 hover 作为当前项识别的唯一线索。

### AURELIA Phone 精确层级与值

```text
Pasta Phone … Salad Phone
└── Dish Display
    ├── Dish Meta
    │   ├── Dish Number Window: height 58px, overflow clip
    │   │   └── Dish Index Reel: vertical stack, row 58px, gap 10px
    │   ├── Dish Title Window: 230px × 38px, overflow clip
    │   │   └── Dish Title Reel: vertical stack, row 38px, gap 10px
    │   ├── Long Description Window: visible false
    │   └── Short Description Window: 230px × 20px, overflow clip
    │       └── Short Description Reel: 230px × auto, vertical stack,
    │           each row 230px × 20px, font Inter 12px / 1.25em,
    │           gap 10px, transition spring-duration 0.42s 0.16 0s
    └── Dish Image Viewport: 350px × 250px, layout null, overflow clip
        └── Dish Image Strip: 2450px × 250px, horizontal stack, gap 0px,
            transition spring-duration 0.52s 0.18 0s
            └── Dish 01–07 Main Image: each 350px × 250px
```

```text
Phone state      Image Strip left   Number top   Title top   Short Description top
Pasta Phone       0px                 0px          0px         0px
Bread Phone      -350px              -68px        -48px       -30px
Dark course      -700px             -136px        -96px       -60px
Blue plate      -1050px             -204px       -144px       -90px
Shellfish       -1400px             -272px       -192px      -120px
Avocado         -1750px             -340px       -240px      -150px
Salad           -2100px             -408px       -288px      -180px
```

Phone Description Properties (the only Phone text edited in this pass):

```text
01  Peas and brown butter in broth.
02  Warm milk bread with butter.
03  Roasted allium, smoke, acidity.
04  Day’s catch with herbs and sauce.
05  Shellfish with citrus and fennel.
06  Avocado with lime and chilli.
07  Little Gem, herbs, vinaigrette.
```

### AURELIA 复刻时的不可变约束

- Phone 的 7 张 Main Image 必须固定为 350px × 250px，Strip 总宽 2450px，gap 0px。
- Phone Short Description 的每行必须是 20px 高，gap 10px；故 pitch 恒为 30px。不可因某一句更长而改单行高度。
- Desktop/Tablet 使用各自的 `Story` 长说明与独立轨道；Phone 使用 `Phone Description`。三个断点不共用图像/文字的 state position。
- 在外部页面预览 320px、390px 的 01/04/07，且 Desktop/Tablet 各抽查一次后，才可判为复制成功。
