# Framer 高级组件：可替换 Image Strip + Number Reel

## 适用场景

用于“缩略图或按钮切换大图，同时更新数字、标题和说明”的组件：菜品选择器、作品轮播、房型选择、产品系列或 gallery selector。

目标：

- 只用 Framer 原生 Component、Variants、Stacks、Properties 和 Transition。
- 买家能在组件外部替换每一道菜的图片。
- Desktop、Tablet、Phone 在外部 Preview 宽度变化时仍然对齐。
- 主图横向推送，数字纵向滚动；不依赖透明度 crossfade。
- 不使用 Code Component。

## 最终组件结构

    Image Selector Component
    ├── Variants
    │   ├── Item 01 / Desktop … Item 07 / Desktop
    │   ├── Item 01 / Tablet  … Item 07 / Tablet
    │   └── Item 01 / Phone   … Item 07 / Phone
    │
    └── Selector Content
        ├── Display Row
        │   ├── Meta Column
        │   │   ├── Number Window（fixed + clip）
        │   │   │   └── Number Reel（vertical stack）
        │   │   │       ├── 01 / 07
        │   │   │       ├── 02 / 07
        │   │   │       └── …
        │   │   ├── Item Name
        │   │   └── Item Description
        │   └── Image Viewport（fixed + clip）
        │       └── Image Strip（horizontal stack）
        │           ├── Main Image 01
        │           ├── Main Image 02
        │           └── …
        └── Preview Rail
            ├── Preview 01
            ├── Preview 02
            └── …

一个 selector 只能是一个 Component。不要把七个菜、七个缩略图或七张主图分别做成独立 component。

## 1. 先建立内容替换路径

### 图片 Properties

为每一项创建一个外部 Image Property：

    Item 01 Image
    Item 02 Image
    …
    Item 07 Image

同一项的主图和缩略图必须绑定同一个 Property。这样模板用户替换一次图片时，两处会自动同步。

不要把图片内容仅放进 Variant 的静态 Fill。Variant 管理状态和位置；Property 管理可替换内容。

### 文案

标题和说明必须是独立 Rich Text 层。若要让模板用户在组件实例外逐项替换，使用对应 String/Rich Text Property 或 CMS；若是固定 demo，可以放在各 Item Variant 内，但不能烘焙到图片。

### 触发器与缩略图

每一个 Preview 都使用原生 SET_VARIANT：

    Preview 01 → Item 01
    Preview 02 → Item 02
    …

未选中缩略图较暗；Desktop hover 变亮；当前项始终高亮。Phone 不依赖 hover，当前项也必须明显可辨认。

## 2. 关键原则：先固定裁切框，再移动内容

Image Viewport 是图片的裁切框和位移坐标系，不是普通响应式图片容器。

它必须：

- layout 为 null。
- overflow 为 clip。
- 在每个断点有 Fixed 的关键宽度。
- 有明确高度策略。
- 是 Image Strip 唯一的对齐参考。

AURELIA 的当前参考值：

| 断点 | Image Viewport 宽度 | 作用 |
|---|---:|---|
| Desktop | 585px | 外部实例变化时，主图步长仍是 585px |
| Tablet | 500px | Tablet 独立使用 500px 步长 |
| Phone | 单独测量 | 不复制 Desktop/Tablet 数值 |

如果 Viewport 使用 %、Fill 或参与父级的 1fr 分配，外部 Preview 宽度变化时，Viewport 会变宽或变窄；但 Variant 内的 left 仍是旧数值，Strip 就无法落在正确边框上。

### Fixed 与 Fill 的判断

| 使用 Fixed | 使用 Fill / % / 1fr |
|---|---|
| 会参与位移计算的裁切框 | 纯内容流和不参与位移的外层布局 |
| 每一张 Image Strip slide | Display Row 的剩余空间 |
| Number Window 高度 | 文案列的自然高度 |
| Strip 的 left 与 Reel 的 top | Section 的内容驱动高度 |

原则：只要数值会影响 left、top、slide pitch 或 reel pitch，就必须放进稳定的 Fixed 坐标系。

### 组件内部与外部 Instance 的尺寸契约

不要只设置 Component 内部的 Desktop / Tablet / Phone。外部页面 Instance 也必须选择同名断点 Variant，并提供与内部关键容器兼容的可用宽高。

这里的“对应”不是要求 Component 根层永远使用同一个固定像素尺寸；外部根层可以按 Section 使用 Fill、Fit 或 max-width。需要严格对应的是会参与坐标计算的内部容器：Image Viewport、slide、Number Window、各 Reel Window，以及它们的 left / top pitch。

```text
Page Instance 可用宽高
        ↓
Component Variant（Desktop / Tablet / Phone）
        ↓
Fixed Viewport / Window
        ↓
Slide size / Reel row size + gap
        ↓
State-specific left / top
```

若外部 Instance 变宽，而内部 Image Viewport 仍是旧值、slide 或 Strip left 没有一起切换，图片会在裁切框内偏移；反过来，内部改为新 pitch、外部却没有足够的可用空间，也会造成压缩、裁切或变形。

因此每个断点都要先写一张尺寸表，再开始复制 Variant：

| 断点 | 外部 Instance 的可用空间 | 内部固定坐标 | 必做复检 |
|---|---|---|---|
| Desktop | 能完整容纳 Desktop Viewport 与 Meta Column | Desktop Viewport / slide / reel pitch | 改变外部 Preview 宽度后检查 01、04、07 |
| Tablet | 能完整容纳 Tablet Viewport；不继承 Desktop 轨道 | Tablet Viewport / slide / reel pitch | 检查图片框与文字列不挤压 |
| Phone | 使用 Phone 专属列宽与图片高度 | Phone Viewport / slide / text reel pitch | 检查完整图片、触控缩略图与末项 |

## 3. 制作横向 Image Strip

### A. 建立 Image Viewport

创建 Image Viewport：

    layout: null
    overflow: clip
    width: Fixed per breakpoint
    height: Defined per breakpoint

它只负责裁切，不能替代横向 Stack。

### B. 建立 Image Strip

在 Viewport 内放 Image Strip：

    layout: stack
    direction: horizontal
    gap: 0px
    alignment: start
    distribution: start
    transition: native spring-duration

将七张主图连续放入 Strip。每一张 slide 的 Fixed 宽度必须等于当前断点的 Viewport 宽度：

    Desktop:
    Viewport = 585px
    Slide 01 = 585px
    Slide 02 = 585px

    Tablet:
    Viewport = 500px
    Slide 01 = 500px
    Slide 02 = 500px

不要使用 1fr 或百分比作为 slide 宽度。Canvas 里可能恰好正确，但外部 Preview 的父级空间变化后，实际宽度会重新计算。

### C. 用 Strip position 对齐每个状态

第 i 项（从 0 开始）的基础公式：

    strip left = -(i × slide pitch) + optical correction

AURELIA 的参考：

    Desktop:
    Item 01: 0px
    Item 02: about -585px
    Item 03: about -1170px

    Tablet:
    Item 01: 0px
    Item 02: -500px
    Item 03: -1000px

先用精确 pitch 对齐裁切框边缘。然后看图片内容：若图片本身的视觉重心或边缘存在一两像素误差，可为该状态做很小的 optical correction。以图片内容和边框同时正确为准，不要只看数学值。

每个 Variant 只改同一个 Image Strip 的 position；不要逐张图片做 visibility 或 opacity 动画。

### D. 动效

Transition 放在 Image Strip，不分别放在七张图片上：

    spring-duration: 0.45s–0.60s
    bounce: 0.12–0.22
    delay: 0s

效果是旧图向左离开，新图从右侧进入。不要加 opacity crossfade：它会削弱推送方向感，也容易在 Phone 出现叠图、残留或看不到图片。

## 4. 制作纵向 Number Reel

数字和图片使用同一个模型，只是横向 left 改成纵向 top。

### A. 正确结构

不要把所有数字写进同一个文本框：

    Number Window（fixed height + clip）
    └── Number Reel（vertical stack）
        ├── 01
        ├── 02
        ├── 03
        └── …

每一行都是独立文本层，统一由垂直 Stack 包住。只让 / 左边的两位当前数字滚动；/07 保持固定，可作为同级静态文本。

### B. 固定窗口与 pitch

Number Window 必须固定高度并裁切溢出。Number Reel 使用 Vertical Stack，gap 在每个断点独立测量。

| 断点 | 当前参考 gap | 要点 |
|---|---:|---|
| Desktop | 16px | 用实际 Rich Text 行高测量 pitch |
| Tablet | 12px | 不沿用 Desktop pitch |
| Phone | 单独测量 | 不能只缩小字体 |

公式：

    reel top = -(i × number pitch) + optical correction
    number pitch = actual rendered line height + stack gap

不要根据 font size 猜 pitch。必须看实际 Rich Text 的 line height 和 Stack gap。AURELIA 当前前几项约为：

    Desktop: 0px → -108px → -212px
    Tablet:  0px → -107px → -210px

这表示最终可有少量视觉校正，但主体仍应是固定步长。

Reel 使用与 Image Strip 接近的 native transition，让数字和主图同一时间启动、同一方向完成。

## 5. Variant 组织与状态职责

推荐名称：

    Item 01 / Desktop
    Item 02 / Desktop
    …
    Item 01 / Tablet
    …
    Item 01 / Phone
    …

每个状态只改：

1. Image Strip 的 left。
2. Number Reel 的 top。
3. 当前项标题与描述。
4. 预览图 selected 样式。
5. 该断点必须变化的尺寸或文字布局。

不要在每个 Variant 重建结构；也不要创建 42 个相邻状态的方向组合。每个 Item Variant 只定义自己的最终位置，Framer transition 自动完成两状态之间的过程。

## 6. 三端制作顺序

### Desktop

1. 固定 Viewport 宽度。
2. 将每张 slide 固定为同样宽度。
3. 对齐 Item 01、02、07，再检查中间项。
4. 测量 Number Window 与 reel pitch。
5. 先边框对齐，再进行少量内容视觉校正。

### Tablet

1. 重新选择 Viewport Fixed 宽度。
2. 重算 left = -index × tablet pitch。
3. 重测文字换行和数字 pitch。
4. 不复制 Desktop 的 position 数值。

### Phone

1. 先决定图片是完整显示还是裁切。
2. 建立 Phone 专属 Fixed Viewport 与 slide pitch。
3. 单独设置 Strip left、Reel top、缩略图尺寸和触控间距。
4. 在真实 Phone Preview 检查全套状态。
5. 不把 Desktop 仅缩小；Phone 是独立坐标系。

## AURELIA DishSelector：已验证的实际范例（2026-08-06）

此例是固定七项、内容可替换的 selector，不是通用默认尺寸。数值来自当前 AURELIA Component 的实时结构；以后复用时先保留结构与计算关系，再按新页面的外部 Instance 空间重新测量。

### 外部内容入口

组件有 21 个状态 Variant：7 道菜 × Desktop、Tablet、Phone。内容不是通过新增菜品 Variant 编辑，而是固定七组外部 Properties：

```text
Dish 01–07 Image
Dish 01–07 Title
Dish 01–07 Story                 # Desktop / Tablet
Dish 01–07 Phone Description
```

总数固定为七；主图和对应缩略图绑定同一 Image Property。这样替换内容不会改变缩略图数量、图片轨道长度、数字总数或状态映射。

### 外部 Instance 与内部尺寸表

| 断点 | 外部使用方式 | Image Viewport | Image Strip 当前尺寸 | 图片状态步长 |
|---|---|---:|---:|---:|
| Desktop | 选择 Desktop 状态；外部 Section 为内容驱动，最小高度 460px | 585px × 100% | 4091px × 410px | 以 585px 为基准，按实际边框与图片内容作光学校正 |
| Tablet | 选择 Tablet 状态；外部 Section 最小高度 520px | 500px × 100% | 4091px × 410px | 500px |
| Phone | 选择 Phone 状态；外部 Section 最小高度 560px | 350px × 250px | 2450px × 250px | 350px：`0, -350, -700, -1050, -1400, -1750, -2100` |

Desktop 与 Tablet 的 Viewport 是 Fixed 坐标框，即使外部预览宽度变化也不能被父级重新拉伸。Phone 用独立的 350px × 250px 框，不能把 Desktop 的 585px 轨道直接缩小。

### 已验证的数字 Reel

| 断点 | Number Window | Index Reel | 单行数字 | 实际第二项 top |
|---|---|---|---|---:|
| Desktop | `1fr × 94px`，clip | `auto` 宽，gap 16px | 90px / 1em | -108px |
| Tablet | `1fr × 84px`，clip | 250px 宽，gap 12px | 90px / 1em | -107px |
| Phone | `1fr × 58px`，clip | 170px 宽，gap 10px | 58px / 1em | -68px |

Desktop 与 Tablet 的数字 Reel 保留用户调好的视觉校正，因此不能根据字号直接假设整数 pitch；必须读取实际第二个状态的 top。Phone 当前为稳定 68px 步长：`0, -68, -136, -204, -272, -340, -408`，并使用 `spring-duration 0.42s 0.16 0s`。`/07` 保持在 Reel 外部，不随左侧两位数字滚动。

### 已验证的文字轨道

| 断点 | 标题窗口 / pitch | 长说明窗口 / pitch | Phone 短说明窗口 / pitch | Transition |
|---|---|---|---|---|
| Desktop | 230px × 40px / 52px | 230px × 82px / 94px | 隐藏 | `spring-duration 0.42s 0.16 0s` |
| Tablet | 230px × 40px / 52px | 230px × 82px / 94px | 隐藏 | `spring-duration 0.42s 0.16 0s` |
| Phone | 230px × 38px / 48px | 隐藏 | 230px × 20px / 30px | `spring-duration 0.42s 0.16 0s` |

对应状态位移必须由真实 row height 加 stack gap 得出：Desktop/Tablet 标题为 `0, -52, -104, …, -312`，长说明为 `0, -94, -188, …, -564`；Phone 标题为 `0, -48, -96, …, -288`，短说明为 `0, -30, -60, …, -180`。

### 用此例重新制作时的顺序

1. 在页面中先确定外部 Instance 的 Desktop、Tablet、Phone 可用宽高。
2. 为每个断点建立匹配的 Component Variant，再固定 Image Viewport 与每张 slide。
3. 依据真实窗口宽度生成 Strip 的 left；只在边框已对齐后加入少量视觉校正。
4. 用独立的标题、长说明、短说明与数字 Reel 计算各自的 pitch；不要将不同文字轨道合并。
5. 最后在外部 Preview 依次验证 01、04、07 及外部宽度变化。通过后才允许替换图片或文案作为模板交付。

## 7. 验收顺序

每个断点至少检查：

1. Item 01：图片左边框、内容和数字 01 对齐。
2. Item 02：推送后没有前一张或下一张图片残留。
3. Item 07：不露白、不超出、不跳位。
4. 中间项：标题、描述和缩略图 selected 状态同步。
5. 外部 Preview：改变可用宽度后，固定裁切框和 Strip 仍对齐。
6. Desktop：hover 变亮；Phone：当前项仍可辨认并可点击。
7. Reduced Motion：最终状态和选中反馈仍明确。

## 常见错误

### Viewport 使用 Fill 或百分比

外部 Preview 宽度一变，图片框宽度变化，固定 left 不再等于一张图宽。

修正：Viewport 与 slide 在每个断点使用 Fixed，并按该尺寸重算 pitch。

### Slide 使用 1fr

Stack 的实际可用空间会随父级变化，七等分不一定等于图片框宽。

修正：每张 slide 设为与 Viewport 相同的 Fixed 宽度。

### 用 opacity 切图

失去推送方向感，Phone 易出现不可见、叠图或残留。

修正：只移动一个 Image Strip。

### 数字在同一文本框里换行

无法控制每行距离，滚动时上下数字会残留。

修正：独立数字层 + 垂直 Reel Stack + 固定裁切窗口。

### 只在 Canvas 对齐

Canvas 的宽度稳定不代表外部实例稳定。

修正：必须在外部 Preview 改变宽度，再检查首项、中间项和末项。

### 主图和缩略图用两份图片

模板用户换图时容易漏改。

修正：同一项主图和 Preview 绑定同一个 Image Property。

## 交付清单

- [ ] 一个可复用 Component，不是七个独立组件
- [ ] 每项图片都有外部 Image Property
- [ ] 同一 Property 同时绑定主图与缩略图
- [ ] Image Viewport 在每个断点有稳定 Fixed 坐标
- [ ] 每张 slide 宽度等于对应 Viewport 宽度
- [ ] 每个 Variant 有正确的 Image Strip left
- [ ] 每个 Variant 有正确的 Number Reel top
- [ ] Number Window 与 Image Viewport 都裁切溢出内容
- [ ] Desktop、Tablet、Phone 分别测量 pitch
- [ ] 缩略图有 hover、selected 与触控可辨认状态
- [ ] 外部 Preview 通过首项、中间项、末项和宽度变化检查
