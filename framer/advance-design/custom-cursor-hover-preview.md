# Framer 动效制作：Custom Cursor 悬浮作品预览

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

本次使用过：

```text
spring-duration 0.42s 0.18 0s
```

如果感觉拖沓，优先减小 duration，或者只保留 variant transition，不给 custom cursor 本身加 transition。

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
5. 回到 archive row component，创建/复制对应 row variant。
6. 在页面实例选择新 row variant。
7. 在页面实例确认 custom cursor 指向新 preview variant。

每新增一个作品，用同一张检查表走完，而不是边看边修。

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
