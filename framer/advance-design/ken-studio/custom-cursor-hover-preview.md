# Framer 动效制作：Custom Cursor 悬浮作品预览

> Status: **Reference; mixed provenance**.
> Provenance: Ken Studio Works cursor preview and later AURELIA fixed cursor-reel notes; dates are retained in their respective sections.
> Verification boundary: Read only the matched project section; pointer behavior is not a Phone interaction contract. Current capability and runtime must be revalidated. Repository classification added 2026-10-03; no fresh Canvas verification.

## 适用场景

这个方案适合做作品列表、菜单、目录、archive index 里的悬浮预览效果：

- 鼠标悬浮到某个选项时，鼠标指针变成一张作品预览图。
- 鼠标移开后，预览图自然消失。
- 鼠标从一个选项滑到另一个选项时，预览图可以顺滑切换，而不是突然闪一下。
- 页面默认状态保持干净，只显示文字列表，不额外放一个固定 preview stage。

这个效果优先使用 Framer 原生功能，不需要 custom code。

## 核心思路

不要把每个选项都做成单独的 hover overlay。

更顺滑的做法是：

1. 做一个统一的 Custom Cursor component。
2. 在这个 component 里创建多个 variants，每个 variant 对应一个作品预览图。
3. 每个作品选项都绑定同一个 custom cursor component。
4. 不同作品选项只切换 custom cursor 的 variant。
5. 给 component variant 设置 transition，让图片、尺寸、阴影等属性在切换时有过渡。

这样鼠标从 A 作品滑到 B 作品时，本质上是同一个 cursor component 在切换状态，而不是 Framer 硬替换两个不同组件。

## 推荐结构

```text
Cursor Preview / Works
├── Variant: Fighting the Chemistry
│   └── Frame: preview image
├── Variant: Campus
│   └── Frame: preview image
├── Variant: Golden Moment
│   └── Frame: preview image
└── Variant: Shadow
    └── Frame: preview image
```

页面中的作品列表：

```text
Project Index
├── Fighting the Chemistry row
├── Campus row
├── Golden Moment row
└── Shadow row
```

每一行都使用 Framer 的 `Custom Cursor` 设置，指向同一个 `Cursor Preview / Works` component，只是 variant 不同。

## 制作步骤

### 1. 创建统一 cursor component

在 Framer 里创建一个 component，例如：

```text
Cursor Preview / Works
```

它只负责 cursor 预览图，不承载页面布局。

### 2. 给 component 做多个 variants

每个作品一个 variant：

- Fighting the Chemistry
- Campus
- Golden Moment
- Shadow

每个 variant 里放一张图片 frame。

### 3. 给每个作品行绑定 custom cursor

在每个作品选项 row 上设置：

- Custom Cursor: `Cursor Preview / Works`
- Variant: 对应作品名

例如：

| Row | Custom Cursor Component | Variant |
|---|---|---|
| Fighting the Chemistry | Cursor Preview / Works | Fighting the Chemistry |
| Campus | Cursor Preview / Works | Campus |
| Golden Moment | Cursor Preview / Works | Golden Moment |
| Shadow | Cursor Preview / Works | Shadow |

### 4. 给 cursor preview component 加 transition

在 component variant 的根 frame 上加 transition。

推荐从比较轻的 spring 开始：

```text
spring-duration 0.45s ~ 0.55s
bounce 0.16 ~ 0.24
delay 0s
```

本次 Ken Studio Works 使用的感觉接近：

```text
spring-duration 0.52s 0.22 0s
```

用途：

- 图片切换更柔和。
- cursor preview 尺寸变化不突兀。
- 横图和竖图之间切换时不会硬跳。

### 5. 需要时再给 custom cursor binding 加轻微 transition

Framer 会提示 custom cursor transition 可能让鼠标变“慢”。所以不要默认加很重。

只有当目标就是“图片跟随鼠标时有一种柔软、滞后的质感”时，才加轻微 transition。

Ken Studio / AURELIA 的较轻跟随设置：

```text
spring-physics 400
```

如果仍然感觉拖沓，提高 physics 值，或移除 Custom Cursor transition，只保留 Reel / variant 的切换动画。

## 图片比例与内容完整度

不要为了统一视觉，把所有 cursor preview 都塞进同一个比例里。

先看每张作品图的真实方向：

- 竖图用竖向 preview。
- 横图用横向 preview。
- 不要让横图被裁成竖图。
- 不要让主体、人物、建筑、空间关系被切掉。

本次 Ken Studio Works 的尺寸：

| Work | Source tendency | Cursor preview size |
|---|---:|---:|
| Fighting the Chemistry | portrait | 178 × 216 |
| Campus | portrait | 178 × 216 |
| Golden Moment | portrait | 178 × 216 |
| Shadow | landscape | 252 × 168 |

判断原则：

- 作品主体完整优先。
- 统一尺寸感次之。
- 如果统一比例会牺牲内容，宁可允许不同作品有不同 cursor preview 尺寸。

## 图片素材处理规则

如果图片来自 `content-library`：

1. 不要直接打开原尺寸图片做视觉查看。
2. 不要直接上传原图到 Framer。
3. 先生成 web-sized derivative。
4. 用 derivative 作为 Framer 资产。
5. 原图留在 `content-library`，不要覆盖。

本次 Campus / Shadow 使用的是压缩后的网页衍生图，再上传到 Framer。

## 常见错误

### 错误 1：每个 row 做一个独立 overlay

问题：

- 鼠标从一行滑到另一行时，overlay 会硬切。
- 容易出现旧 overlay 残留、引用断掉、hover leave 不稳定。
- 页面结构会越来越重。

更好的做法：

- 用 Custom Cursor。
- 用一个 component 的多个 variants。

### 错误 2：四个作品做四个独立 cursor component

问题：

- 切换时 Framer 是在替换 component。
- 动效容易生硬。

更好的做法：

- 一个 cursor component。
- 四个 variants。
- 行与行之间只切 variant。

### 错误 3：统一固定裁切比例

问题：

- 横图被裁成竖图。
- 作品主体不完整。

更好的做法：

- 按作品素材方向单独设 preview 尺寸。
- 允许 portrait / landscape 混合。

### 错误 4：保留一个固定 Preview Stage

问题：

- 列表不再纯粹。
- 视觉上像一个“右侧展示区”，不是“鼠标变成图片”的体验。

更好的做法：

- 默认只显示作品选项。
- 图片只在 hover cursor 中出现。

## QA 检查清单

完成后检查：

- 默认状态是否只显示作品列表。
- 鼠标进入 row 后，cursor preview 是否出现。
- 鼠标从 row A 移到 row B，图片是否顺滑切换。
- 鼠标离开列表后，preview 是否消失。
- 横图和竖图是否都保留了作品主体。
- 已确认路由的 row 是否仍可点击。
- 未确认路由的 row 是否没有误加链接。
- Framer review 是否没有 blocking errors。
- 手机端是否不依赖 hover 完成主要信息传达。

## Ken Studio Works 当前实现记录

项目：`Ken Studio`

页面：`/works`

区域：`Observation`

当前实现：

- 使用 Framer 原生 Custom Cursor。
- 使用一个统一 cursor preview component：`Cursor Preview / Works`。
- 四个 variants：
  - `Fighting the Chemistry`
  - `Campus`
  - `Golden Moment`
  - `Shadow`
- `Fighting the Chemistry` 和 `Golden Moment` 保留已确认点击路由。
- `Campus` 和 `Shadow` 保持待确认路由，不加链接。
- 没有使用固定 Preview Stage。
- 没有使用 custom code。

## 可复用一句话方案

在 Framer 里做作品列表悬浮预览时，优先用一个带多 variants 的 custom cursor component；每个列表项绑定同一个 cursor component 的不同 variant，再给 variant 加轻量 transition。图片 preview 的尺寸跟随作品素材比例，而不是统一硬裁。

## 组件化后 preview 丢失排查

作品行做成 component 后，custom cursor preview 很容易“看起来还在组件里，但页面预览没了”。

原因通常不是图片丢了，而是 cursor binding 没有落在实际页面实例上。

排查顺序：

1. Cursor preview component 是否还存在。
2. Cursor preview component 是否有每个作品对应的 variant。
3. 作品行 component variant 是否设置了 custom cursor。
4. 页面上的 row instance 是否也保留了 custom cursor。
5. 页面上的 row instance 是否选择了正确 row variant。
6. Desktop / Tablet / Phone 是否都检查过。

尤其注意：

```text
Component variant 有 cursor
≠
Page instance 一定会显示 cursor
```

在 Framer 里，component instance 可能有自己的 override。组件化之后，必须回到页面层检查实际 instance。

## Cursor preview 扩展新作品

新增作品时，不要重新做一套 cursor system。

最省事的方式：

1. 在 `Cursor Preview / Works` 里复制一个相近的 variant。
2. 改名为新作品名。
3. 替换 preview image。
4. 根据素材方向调整 preview 尺寸。
5. 回到页面复制一个 `Archive Option Row` instance。
6. 在 Instance 修改 Number、Title、Meta、Fill 和 Link。
7. 在页面实例确认 custom cursor 指向新 preview variant。

每新增一个作品，用同一张检查表走完，而不是边看边修。

## 列表组件化：Cursor binding 放在哪里

当列表的每一行需要同时具备可编辑文案、浅灰 hover 与悬浮图片预览时，把**行本身**做成原生 Component，而不是把整组列表连同 preview 一起做进一个大组件。

推荐分层：

```text
Page section
└── Index/List container
    ├── Chapter / Archive Row instance 01
    ├── Chapter / Archive Row instance 02
    └── ...

Chapter / Archive Row component
├── Variant: Desktop
├── Variant: Tablet
├── Variant: Phone
├── Gesture variant: Desktop Hover
└── Gesture variant: Tablet Hover

Cursor Preview component
├── Variant: item 01 image
├── Variant: item 02 image
└── ...
```

### 组件职责

`Chapter / Archive Row` component 只管理：

- 标题与描述的 string properties；
- Desktop / Tablet / Phone 的行内排版；
- divider、内边距与 `height="auto"`；
- 原生 Hover gesture variant 的浅灰背景与短 transition。

`Cursor Preview` component 只管理：

- 每个条目的图片；
- 每张图片自己的预览宽高；
- variant 切换 transition。

页面里的**每个 Row instance**管理：

- 它自己的标题和描述值；
- Custom Cursor 指向同一个 `Cursor Preview` component；
- Custom Cursor 的正确图片 variant。

不要只在 Row component 定义里设置 custom cursor。组件化后，页面实例可能有自己的 override；最终必须在页面层逐项检查 instance 的 cursor binding。

### Ken Studio 的已验证范例

`Ken Studio / Works / Observation Index Area` 采用的是 `ArchiveOptionRow`：

- Row 有 `Desktop`、`Phone` 和对应 Hover gesture variants；
- `Project Title`、`Meta`、`Number`、`Project Link`、`Base Fill`、`Hover Fill` 都是 instance properties；
- 页面里每一个作品 instance 自己绑定 `Cursor Preview / Works` 的对应 variant；
- Hover 使用组件内部状态，Cursor Preview 保持为独立组件。

这避免了“组件化后预览消失”的问题，也让单行内容、手机排版与 hover 外观可复用。

### Preview 图片：先选定“完整内容”还是“统一滚动窗口”

这两个要求在素材比例不一致时不能同时由一个普通 Frame fill 自动完成，必须先选策略：

| 目标 | Preview Frame | 图片处理 | 适合 |
|---|---|---|---|
| 每张图完整显示 | 宽度固定、高度 `fit-image` | 保留真实图片比例 | 静态 cursor preview / 不同尺寸的 variant |
| 所有状态以固定步长滚动 | 所有 slide 锁定同一宽高 | 素材同一比例，或先做 letterbox 衍生图 | 垂直 / 横向 reel |

固定 Reel 不能让一张横图与一张竖图都“原尺寸完整覆盖”同一个窗口；否则其中一张必然被裁切。若内容完整比满框更重要，先把非同一比例的图片制作成带背景留白的统一比例 web derivative，再上传到 Framer。不要拉伸原图。

`overflow: clip` 与小圆角用于显示窗口边缘；它们不是图片内容的排版方案。

## 完整制作配方：固定尺寸 Cursor Preview Reel

下面是可以直接复用的原生 Framer 方案。适用于固定数量的目录、菜品、作品或章节，并且需要“图片滚动 + 鼠标粘滞”而不是淡入淡出。

### 0. 先固定内容数量与素材策略

在开始前确认三件事：

1. 条目数是否固定。例如 AURELIA 是固定 4 个章节；新增条目会同时改变 row instances、cursor variants 与 Reel slide 数，不能交给可无限增加的 CMS list。
2. Reel 是否必须每格相同大小。若必须，先统一所有 image derivative 的画布比例；若不必须，改用每张图自己的 `fit-image` variant，放弃固定步长 Reel。
3. Phone 是否需要 hover。Phone 不依赖 cursor preview 传达主要信息，但应保留完整标题和描述；桌面指针设备才是该动效的核心场景。

### 1. 建立三个独立层级

```text
Section / List container
├── Row instance 01 → cursor variant 01
├── Row instance 02 → cursor variant 02
└── Row instance 03 …

Row component
├── Desktop / Tablet / Phone variants
├── Desktop Hover / Tablet Hover gesture variants
└── editable title + description properties

Cursor Preview Reel component
├── State variant 01
├── State variant 02
└── …
    └── one shared clipped viewport + one shared image stack
```

不要把 row、整组列表和 cursor preview 合并成一个大 component。它们的复用粒度、外部编辑方式和响应式职责都不同。

### 2. Row component 必须这样建立

1. 从一条已经正确排版的原始 row 创建 component，或以同一结构新建 component。
2. 组件内部建立 `Desktop`、`Tablet`、`Phone` 三个普通 variants；不要把 breakpoint 写在页面实例内硬撑。
3. 标题与描述使用独立 string properties，例如 `Chapter Title` 和 `Chapter Description`。
4. Hover 只做 Gesture variants：背景变浅灰、`scale = 1`、短 tween/spring；不要给 row 再加放大。
   - 为 Desktop、Tablet、Phone 都建立对应的 Hover gesture variant，使窄屏但带鼠标的预览也一致。
   - 真实触摸设备没有 hover 或 cursor；Phone 的文字内容必须独立完整，不能依赖预览图片传达信息。
5. 每个内部 variant 的参考尺寸必须与页面外部实例在相应设备上的参考尺寸相同，且都使用 `height="auto"`。AURELIA 示例为 Desktop `1136px`、Tablet `754px`、Phone `350px`，页面 instance 均为 `width="1fr" height="auto"`。
6. 页面中的每一条都使用同一个 Row component instance；Desktop / Tablet / Phone breakpoint 分别选择对应内部 variant。

这是防止组件在外部套用后比例、文字换行和 divider 宽度变形的尺寸契约。

### 3. Cursor Preview Reel component 的精确结构

以 4 项、每项 `300 × 200px` 为例：

```text
ChapterCursorPreview
├── Arrival variant
│   └── Preview Viewport — 300 × 200, overflow: clip
│       └── Preview Reel — vertical Stack, 300 × auto
│           ├── Slide 01 — 300 × 200
│           ├── Slide 02 — 300 × 200
│           ├── Slide 03 — 300 × 200
│           └── Slide 04 — 300 × 200
├── First Plates variant  → Reel top: -200px
├── From the Kitchen      → Reel top: -400px
└── After                 → Reel top: -600px
```

制作规则：

- Viewport 必须是固定宽高、`overflow: clip`、小圆角；它是唯一可见窗口。
- Reel 必须是一个纵向 Stack，`gap: 0px`，宽度与 Viewport 一致，高度 `auto`。
- 每张 slide 的宽高必须相同；第 `n` 状态的位移 = `-(n - 1) × slide height`。
- 所有图片只在 Primary Variant 的 Stack 内创建一次；其他状态 variants 只覆盖 Reel 的 `top`。不要每个 Variant 再复制一套图片。
- 给 Reel 本身设置 `spring-duration 0.52s 0.22 0s` 左右的 transition。根 variant 的同类 transition 用于尺寸 / 外框状态同步。
- 后续替换图片时，只替换 Primary Stack 中对应 slide 的 fill；所有状态会自动继承。

### 4. Custom Cursor binding 必须设置在页面实例

对每个实际 Row instance 设置：

```text
Custom Cursor type: ComponentNode
Component: ChapterCursorPreview
Variant: 与该 row 对应的状态
Follow: false
Transition: spring-physics 400
```

两层 transition 的职责不同：

| 层级 | 控制对象 | 效果 |
|---|---|---|
| Reel transition | 图片 Stack 的 `top` | 状态之间的纵向滚动 |
| Custom Cursor transition | preview 跟随鼠标的位置 | Ken Studio 式轻微粘滞 / 回弹 |

只设置 Reel transition 不会让鼠标运动本身变粘；只设置 Custom Cursor transition 则会有粘滞但图像会硬切。两者都要有。

组件定义里有 Cursor 设置不代表页面 instance 已生效。完成组件化后必须在页面的 Desktop、Tablet、Phone 三端分别读取 / 检查每个实例的 `customCursor.componentNodeId`、`variant` 和 `transition`。

### 5. 模板交付：让预览图片可以一处替换

不要让买家在四个 Variant 中逐张替换图片；这会留下错误的副本 override，令 Reel 在滚动时出现旧图。

正确做法是在 `Cursor Preview Reel component` 本身建立固定数量的 **image properties**：

```text
Arrival Preview Image
First Plates Preview Image
From The Kitchen Preview Image
After Preview Image
```

每个 property 只绑定 Primary Variant 的 Reel 中对应 slide 的 `fill`。其他 cursor state variants 必须继承同一个 Reel 和这些 fill bindings，不能在任何 Replica Variant 单独替换图片。

模板使用者的操作路径：

1. 在 Components 面板打开 `ChapterCursorPreview`；
2. 在右侧属性中替换四个 `… Preview Image`；
3. 不改 Slide 顺序、不添加或删除 slide；
4. 回到 Desktop 和 Tablet Preview 横移四行，确认每个 Row 的 Cursor variant 仍对应正确图片。

这是全局预览组件，因此图片属性显示在 `ChapterCursorPreview` 的组件定义中，而不在每个 `EveningChapterRow` instance 内。替换一次会同步四个列表行和全部响应式 breakpoint。

### 6. AURELIA 已验证示例

`ChapterCursorPreview`：

- 4 个状态：Arrival、First Plates、From the Kitchen、After；
- 固定 Viewport：`300 × 200px`；
- 4 个 Slide：均 `300 × 200px`；
- Reel 位移：`0 / -200 / -400 / -600px`；
- Reel transition：`spring-duration 0.52s 0.22 0s`；
- Row Custom Cursor transition：`spring-physics 400`。
- 图片属性：Arrival / First Plates / From The Kitchen / After，各一项，均绑定到共享 Reel 的 Primary slide。

### 7. 最终 QA 清单

- 默认页面没有固定 preview stage。
- 每个 row 的标题和描述仍可在外部 instance 编辑。
- Desktop、Tablet、Phone 的 Row instance 都使用匹配的内部 variant。
- 所有 row 的 Cursor component id 相同，但 Cursor variant 各自匹配。
- 每个 Cursor binding 都有同一个轻量 transition；没有意外放大。
- Phone Row 有对应 Hover gesture variant；同时确认触摸内容不依赖 hover。
- 四个 `… Preview Image` 属性各自绑定一个 Primary Reel slide，且所有 cursor variants 没有图片 fill override。
- Preview Reel 的 slide 数与 row 数相同，顺序一致。
- 第 `n` 个 variant 的位移等于 `-(n - 1) × slide height`。
- Viewport 之外不出现相邻图片残留。
- 连续从 row A 横移到 row B 时，图片滚动不硬切，鼠标框有轻微粘滞。
- 图片比例不一致时，已明确选择裁切或 letterbox derivative，未拉伸。
- Phone 不依赖 hover 才能阅读或操作。
- Framer change diagnostics 没有 blocking error；用一次真实 Desktop / Tablet Preview 检查跟随手感。

不要在 archive row component 内为新作品复制 Desktop、Phone 和 Hover 内容 Variant。Row component 只维护结构与状态；作品内容留在页面 Instance。

## Transition 使用边界

Cursor preview 的顺滑感主要来自 preview component variant 的 transition。

不要默认把很重的 transition 放在 custom cursor binding 上。Framer 可能会让鼠标跟随变慢。

推荐优先级：

1. 先给 cursor preview component variant 设置 transition。
2. 如果切换仍然太硬，再给 custom cursor binding 加很轻的 transition。
3. 如果鼠标跟随拖沓，先移除 binding transition，不要移除 preview variant transition。

一句话：

```text
图片切换要柔，鼠标跟随要轻。
```
