# Framer 节省额度工作流

这个文件给以后接手 Framer 项目的 agent 读。目标不是多写规则，而是减少反复试错、重复读取和“改好一个地方又弄坏另一个地方”的额度浪费。

## 第一性原理

Framer 页面问题通常分三层：

```text
Component definition
└── Page instance
    └── Breakpoint / responsive override
```

不要把三层混在一起修。

先判断问题发生在哪一层：

- 组件内部错：改 component variant。
- 页面实例错：改 instance controls / cursor / link / selected variant。
- 端侧错：改对应 breakpoint 或 phone-specific variant。

如果没有先分层，后面就会出现：

- 组件里看起来对，页面实例还是错。
- Desktop 对了，Phone 文字挤成一列。
- hover 在编辑器里有，preview 里没有。
- custom cursor 在某些实例上消失。

## 开工前的小矩阵

涉及 component、hover、cursor、responsive 的任务，先列一个小矩阵。

例：

| Area | Desktop | Tablet | Phone |
|---|---|---|---|
| Observation rows | text / hover / cursor | text / hover / cursor | text / layout |
| Creation rows | text / hover / cursor | text / hover / cursor | text / layout |

这个矩阵比边改边想省 token。

它能提前暴露：

- 哪些实例需要同步。
- 哪些端侧需要独立 variant。
- 哪些交互在 phone 端不需要。
- 哪些字段应该隐藏。

## Typography 不能凭感觉匹配

如果用户说“沿用某个页面/某个参考站的字体排版”，不要根据截图或印象猜字体。

最省 token、最少返工的做法：

1. 先读取参考页面里已经做对的真实节点属性。
2. 记录 `fontName / fontSize / fontWeight / lineHeight / letterSpacing / textColor`。
3. 再把这些属性同步到目标页面的同类标题。
4. Desktop / Tablet / Phone 分别读对应 breakpoint，不要用桌面字号硬缩到手机。

Ken Studio 例子：

```text
Works title = Boldonse
Desktop: 103px / 400 / 1.2em / 0em
Tablet: 80px / 400 / 1.2em / 0em
Phone: 68px 左右，根据标题长度可小幅调整
```

错误路径：

- 看起来像 display sans，于是换成 Inter Display。
- 只改 desktop，tablet/phone 没同步。
- 看到 phone 挤压先盲目缩字号，而不是先检查宽度链。

正确路径：

- 参考谁，就读谁的真实 Framer 节点。
- 字体是品牌系统的一部分，不是“差不多”的装饰选项。
- 如果参考来自外部网站，先用现有 Framer 中已复刻成功的节点作为本项目基准。

## Targeted read, not full-page read

不要一上来读取整页大树。

优先读取：

- 当前 component id。
- 当前 folder/container id。
- 相关 page instances。
- 相关 breakpoint replicas。

读取时限制：

- `depth` 控制在 1–4。
- `attributeFilter` 只包含当前要判断的属性。
- 输出做 summary，不要把整棵树全部打印。

推荐读取内容：

```text
name
$variants
$rect
width / height / minWidth / maxWidth
layout / stackDirection / gap / padding
text / textColor / fontSize / lineHeight
$control__variant / title / number / meta / status
customCursor
hoverEffect
```

如果输出开始被截断，停止继续读大树，改写更小的 targeted script。

## 修改前先确定“谁拥有宽度”

响应式问题大多不是字体问题，而是 width ownership 不清楚。

先画出宽度链：

```text
Section
└── Folder sheet
    └── Project Index
        └── Row instance
            └── Title Group
                ├── Number
                └── Title
```

再决定：

- 哪一层固定宽度。
- 哪一层 `1fr`。
- 哪一层 `maxWidth: 100%`。
- 哪一层隐藏 meta/status。

不要看到文字重叠就先调字号。先查父容器宽度、子元素宽度和 stack 方向。

## 图片完整度优先于统一格子

作品图片、封面图、cursor preview 这类内容，如果用户强调“内容完整度”，不要把图片强行塞进一个统一比例的 holder。

第一性原理：

```text
图片内容有自己的原始比例
→ 边框/外框应该跟随图片比例等比缩放
→ 不是让图片 cover 一个同宽同高的框
```

推荐结构：

```text
Outer visible frame / card
  layout: stack
  width: 1fr 或 100%
  height: auto
  overflow: clip
  border / radius 在这里
  └── Image layer
      width: 100%
      height: fit-image
```

这样用户改变可用宽度时：

- 图片按原比例缩放。
- 外框跟着图片自然变高/变矮。
- 不会因为 holder 固定高度导致作品内容被裁掉。

只有当目标明确是统一卡片矩阵、且裁切本身是设计语言时，才使用固定 aspect ratio / cover。

## Component 创建后的必查项

每次把页面元素做成 component 后，必须回到页面实例检查：

1. Instance 是否选择了正确 variant。
2. Instance controls 是否还是默认值。
3. Custom cursor 是否保留。
4. Link 是否保留或是否应该暂时为空。
5. Hover 是否仍然有效。
6. Tablet / Phone 是否选择了对应 variant。
7. Phone 是否需要隐藏 meta/status。

特别注意：组件化后最容易丢的是 effect、cursor、link、instance controls。

## Hover 的默认策略

密集列表、archive row、menu row 默认不要 scale。

优先：

- component Hover Gesture Variant；
- 背景色变亮/变深；
- 文字透明度变化；
- border/divider 变化。

避免：

- 给每个页面实例随手加 hoverEffect；
- hover scale；
- hover 后改变布局尺寸；
- 用 overlay 伪装 row hover。

如果 hover 是 component 行的一部分，优先在 component 内部建 Hover Gesture Variant。

## Custom cursor preview 的默认策略

作品 hover preview 默认用一个 cursor component + 多个 variants。

不要：

- 每个 row 一个 overlay；
- 每个作品一个 cursor component；
- 做固定 preview stage，除非用户明确要。

新增或组件化后检查：

```text
Cursor Preview component variant exists
→ Row component variant points to it
→ Page instance also points to it
→ Desktop / Tablet instance checked
```

Phone 通常不需要 cursor preview，但仍要确认 phone variant 没有因此挤压布局。

## Framer review 的判断

Review warning 不要机械清零，要判断它是不是设计意图。

必须处理：

- text contrast too low；
- element zero width/height 且仍 visible；
- ground nodes overlap each other；
- hover scale clipped；
- invalid/rejected attributes。

可以接受或单独说明的：

- sticky folder stack 的 intentional overlap；
- component editing canvas 中用于编辑的固定 width；
- phone 不使用 hover/cursor 的提示。

但如果 review 报错来自刚刚新增的 variant，先修掉，不要留给用户发现。

## 每阶段恢复记录

长任务容易 reconnect。每完成一个阶段，至少在工作笔记或最终回复里留下：

- Framer project / page path。
- 主要 component 名。
- 新增/修改的 variant。
- 已同步的 page instances。
- 已检查的 breakpoint。
- 还没做或故意不做的内容。

这样下一个 agent 不需要从头读，也不会覆盖已经做好的东西。

## 最省 token 的交付方式

完成后不要长篇解释内部节点 ID。

简洁说明：

- 改了什么。
- 哪些端侧检查过。
- 哪些交互已恢复。
- 是否还有已知限制。

如果需要截图，只截目标容器，不截整页。

如果需要回读，只回读目标节点，不读整页。
