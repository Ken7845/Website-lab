# Framer 高级组件：ChefStoryRow

> **Current Canvas contract — verified 2026-08-16.** The `/chefs` page owns the available inline width: `Chef Profiles` and all three Page Instances are Fill (`1fr`) at Desktop, Tablet, Phone, and Wide Phone, with no `maxWidth` on the list. The portrait remains governed by its breakpoint-specific frame; the adjacent Story / identity region takes the responsive remainder. Treat this as the current source of truth over older revision notes.

## 适用范围

`ChefStoryRow` 用于 AURELIA `/chefs` 这类“先通过肖像相遇、再按需阅读一位人物长故事”的编辑型人物序列。它让首屏保持稀疏，同时让每位人物的姓名、角色和第一人称故事保留在同一个可展开的阅读单元中。

适合：三至少量人物、每人一张肖像、一条可编辑的长故事、Desktop / Tablet / Phone 都需要明确展开与返回的项目。

不适合：大量员工目录、可筛选团队网格、每人需要独立详情页的简历系统、并行多开 FAQ，或故事必须同时可见的长篇社论。此组件的展开状态是单个条目的阅读模式，不应被改作悬停预览或 Overlay。

## 交互目标与边界

- 折叠态呈现肖像、姓名、角色和 `View the story`；展开态在同一组件内显示长故事，并用 `Back` 返回对应断点的折叠态。
- 所有切换使用原生 Framer `SET_VARIANT`，不使用 Custom Code、Scroll Hijacking 或位置 scale。
- 组件本体拥有每个断点的水平 Padding；页面 Section 只负责垂直节奏和列表间距。
- 页面 Instance 只写人物内容与头像；不得为每位厨师新建 Component 或内容 Variant。
- Phone 不把 Desktop 的双列硬缩小：它改为肖像、身份与故事的纵向阅读关系；Wide Phone 保持可读的横向关系。

## Properties、Variants 与 Instance 的职责

### Component Properties

| Property | 类型 | 责任 |
|---|---|---|
| `Portrait` | Responsive image | 每个 Instance 的人物肖像。当前没有单独的 Alt Property；替换图片时必须另行完成可访问性检查。 |
| `Chef Name` | String | 人物姓名。 |
| `Chef Role` | String | 人物角色；可留空，但需在真实 Preview 复测空值节奏。 |
| `Content` | Rich text | 完整第一人称故事；可包含多个段落，不能靠内容 Variant 区分人物。 |

折叠 / 返回文案目前是内嵌 Button Instance 的 `View the story` 与 `Back`，并非 Component Property。若买家需要改 CTA 文案，应先将这两个值提升为明确 Property，再测试八个 Variant 的同步结果。

### Structural Variants

| Variant | 根尺寸与 Padding | 使用情境 |
|---|---|---|
| `Desktop Collapsed` | 1164px × auto；`0 32 0 64` | 1200px Desktop 的初始人物行。 |
| `Desktop Expanded` | 1164px × 580px；`40 32 50 64` | Desktop 长故事阅读态。 |
| `Tablet Collapsed` | 810px × 570px；`0 28 0 28` | 810px Tablet 初始态。 |
| `Tablet Expanded` | 810px × 570px；`36 28 50 28`，根 gap 28px | Tablet 故事阅读态。 |
| `Phone Collapsed` | 390px × auto；`0 20 50 20` | 390px 纵向初始态。 |
| `Phone Expanded` | 390px × auto；`20 20 30 20` | 390px 长故事阅读态。 |
| `Wide Phone Collapsed` | 599px × 400px；`0 28 0 28` | 599px authored Wide Phone 的横向紧凑态。 |
| `Wide Phone Expanded` | auto × auto；`36 28 36 28`，根 gap 28px | 599px authored Wide Phone 的横向故事阅读态。 |

所有八个 Variant 的 live transition 都是 `spring-physics 250 30 1 0s`（stiffness 250）。这些是结构 / 断点 / 阅读状态，不是人物内容的 Variant。

### Page Instance

`/chefs` 当前有三组 Instance：`Chef One Story`、`Chef Two Story`、`Chef Three Story`。它们在页面 Breakpoint 中选用：

- Desktop → `Desktop Collapsed`
- Tablet → `Tablet Collapsed`
- Phone → `Phone Collapsed`
- Wide Phone → `Wide Phone Collapsed`

Page 的 `Chef Profiles` 列表拥有可用宽度：Desktop、Tablet、Phone、Wide Phone 均为 `1fr` / Fill、高度 auto，且列表本身没有 `maxWidth`。三个 Page Instance 也均为 `1fr` / Fill、高度 auto。不要在外层 Section 额外加横向 Padding 或 `maxWidth` 来补组件边界，也不要将 Instance 改成 100% Relative 或固定宽度。

`599px` 是当前画布的 Wide Phone authored width，不是可凭空假设的浏览器范围。若要调整断点区间，先在 Page 的 Breakpoint 设置中读取实际最小 / 最大范围，再同步验证 Wide Phone 与相邻 Phone / Tablet 状态。

## 组件树与宽度所有权

```text
ChefStoryRow (Component)
├── Properties: Portrait / Chef Name / Chef Role / Content
├── Desktop Collapsed / Tablet Collapsed / Phone Collapsed / Wide Phone Collapsed
│   └── Chef Identity Row
│       ├── Portrait Column
│       │   └── Chef Portrait (image Fill 由 Portrait Property 提供)
│       └── Chef Identity
│           ├── Chef Role
│           └── Story Content
│               ├── Identity Copy (Chef Name 与 Content 的断点顺序)
│               └── Story Toggle Button → matching Expanded Variant
└── Desktop Expanded / Tablet Expanded / Phone Expanded / Wide Phone Expanded
    └── Same semantic tree, with matching Back Button → matching Collapsed Variant
```

根 Variant 是拥有白色 Surface、裁切和左右空间的可见边界，因此 Padding 必须停留在根。`Chef Identity Row` 使用 Stack 建立 Desktop / Tablet / Wide Phone 的左右关系，Phone 则改为纵向。`Chef Portrait` 自己拥有裁切与图片 Fill；不可将画布外 Instance 的 Width 当作头像比例的来源。

## 精确尺寸契约

| 状态 | Portrait | Identity / story area | 关键关系 |
|---|---|---|---|
| Desktop Collapsed | 386.5 × 580px | `1fr`，Identity 高 580px，底部 Padding 50px | Row gap 50px。 |
| Desktop Expanded | 326.5px × `1fr` | 604px × `1fr` | 根高 580px；Row gap 50px。 |
| Tablet Collapsed | 380px × `1fr` | `1fr` × `1fr` | 根高 570px；Row gap 48px；Identity gap 20px。 |
| Tablet Expanded | 固定 `289.33 × 434px`（约 2:3；Portrait Column 与 Chef Portrait 一致） | `1fr` × `1fr` | Row gap 30px；肖像不随可用宽度拉伸，Story / identity 吸收边框变宽后的剩余空间。 |
| Phone Collapsed | `1fr` × 440px | `1fr` × auto | 先肖像、后身份；Identity gap 20px。 |
| Phone Expanded | `fit-image` × `1fr`（Portrait Column 220px 高） | `1fr` × `1fr` | Identity gap 100px；Story wrapper gap 54px。 |
| Wide Phone Collapsed | 279px × `1fr` | `1fr` × `1fr` | 根高 400px；Row gap 25px。 |
| Wide Phone Expanded | 166 × 245px | `1fr` × `1fr` | 外 Row 543 × 620px；Row gap 30px；Identity gap 70px。 |

替换头像时，先保持这些容器契约，再检查 focal point 和可读性。不能用 `Fill`、百分比或外部 Section Padding 改写参与上述尺寸关系的 Portrait Column / Chef Portrait；响应宽度应由 Page list → Instance → Story / identity 的 `1fr` 链承接，而不是由人物图承担。

## 状态路由

| 断点 | 展开 | 返回 |
|---|---|---|
| Desktop | `Desktop Collapsed` → `Desktop Expanded` | `Desktop Expanded` → `Desktop Collapsed` |
| Tablet | `Tablet Collapsed` → `Tablet Expanded` | `Tablet Expanded` → `Tablet Collapsed` |
| Phone | `Phone Collapsed` → `Phone Expanded` | `Phone Expanded` → `Phone Collapsed` |
| Wide Phone | `Wide Phone Collapsed` → `Wide Phone Expanded` | `Wide Phone Expanded` → `Wide Phone Collapsed` |

折叠 Button 的视觉 Variant 分别为 Desktop `Dark`、其余断点 `Dark Small`；展开 Button 分别为 Desktop `White`、其余断点 `White Small`。每个 Button 都是 Fit / Fit，并由自身的 Label、Link、Click Property 控制，不把点击边界放在外层 Story Stack。

## 实施与恢复顺序

1. 建立一个 Primary `Desktop Collapsed`，先确认 Portrait / Name / Role / Content 是 Properties，而非人物 Variant。
2. 用 `CREATE_VARIANT` 建立同断点 Expanded，并从折叠态只改阅读状态、头像比例、copy 顺序 / 可见性与 Button 路由。
3. 建立 Tablet、Phone、Wide Phone 的折叠 / 展开成对 Variant；每一对只回到自身断点的折叠态，绝不跨断点跳转。
4. 把根 Padding 写在 Component root，Page 的 `Chef Profiles` 只保留垂直 gap 与 Section bottom spacing。
5. 在 `/chefs` 放入三个 `1fr` Instance；仅在 Instance 编辑 Portrait、姓名、角色、Content。
6. 先做一次结构回读，再在外部 Preview 测试首项、中间项、末项、宽度变化和长内容；最后记录例外。

## 验收矩阵

| 检查 | 必须通过的证据 |
|---|---|
| 路由 | 四个断点均能 `Collapsed → Expanded → Collapsed`，且没有跳到其他断点。 |
| 宽度 | `Chef Profiles` 在 Desktop / Tablet / Phone / Wide Phone 都为 `1fr` 且无 `maxWidth`；三个 Page Instance 同样为 `1fr`，根 Padding 由组件拥有。 |
| 替换 | 首、中、末 Instance 分别替换 Portrait、长 Name / Role、双倍 Content、空 Role；无横向溢出、裁切或空白断层。 |
| 图片 | 纵向和横向替换图都保留人物可读焦点；Tablet Expanded 固定为 `289.33 × 434px`（约 2:3），Phone Collapsed 仍为 440px 高。 |
| 动效 | `spring-physics 250 30 1 0s` 不改变页面的阅读顺序；Reduced Motion 下最终状态和 Back 操作仍清楚。 |
| 可访问性 | Button 可键盘进入、Focus 可见、展开内容紧随对应 Trigger；每张 Portrait 有准确 Alt。 |
| Preview | 至少实测 320 / 390 / 599 / 810 / 1200 / 1440+，并检查首项、中间项、末项。 |

## 常见失效与修复

| 症状 | 原因 | 修复 |
|---|---|---|
| 预览拉宽后右侧留白或背景露黑 | 把 root / Section 锁为过小 max-width，或让外层拥有组件的横向 Padding | 保持 Page / Section full bleed；只在必要的内层限制宽度，根 Padding 留在组件。 |
| 边框变宽时人物图被拉伸，或 Story 没有跟随边框 | `Chef Profiles` / Instance 链中仍有 `maxWidth` 或固定宽度；或 Tablet Expanded 的 Portrait / Story 同时使用 `1fr` | 依次检查 `Chef Profiles → Page Instance → Chef Identity Row`：列表与 Instance 都恢复为 `1fr`、移除列表 `maxWidth`；Tablet Expanded 将 Portrait Column 与 Chef Portrait 保持 `289.33 × 434px` / 约 2:3，Chef Identity 保持 `1fr`。 |
| Phone 头像变形或故事不随宽度变化 | 改写了 Portrait Container 的 350 / 440 或 `fit-image` 合同，或 Story 父级不是 Fill | 恢复对应 Variant 的 Portrait 与 `1fr` Story 链；不要在 Text 上加 Padding。 |
| 展开后跳到 Desktop 或无法返回 | 继承了错误断点的 `SET_VARIANT` 目标 | 回读 Button Click Property，按上表设为同断点配对 Variant。 |
| 新厨师需要新 Variant | 将内容当成状态 | 复制一个 Page Instance，写入四个 Properties；不增加 Component Variant。 |
| 长故事裁切 | root / Row 使用与故事不匹配的固定高度 | 先检查对应状态是否应为 auto；若已有刻意固定高度，先在真实长文案 Preview 验证后才改。 |
| 画布正常，Preview 无法理解文案 | CTA 标签不是组件 Property | 提升为明确的打开 / 关闭 String Properties，随后复测八个状态。 |

## 不可改动的约束

- 不把外层 Page 的统一 Padding 重新作为组件横向边界；此组件根层已经拥有各断点 Padding。
- Phone Collapsed 的人物肖像保持 350px 可用宽度内的 440px 高合同；不要为了“响应”把 Portrait 拉成任意比例。
- 不删除或移动 Variant root 来处理画布位置；组件的 Variant 坐标不参与页面实例布局。
- 不将故事只放入 Hover、Cursor 或绝对定位 Overlay。

## 精确 Example：AURELIA `/chefs` 的 ChefStoryRow

这是当前 live Component 的可复刻例子，而不是抽象示意。

```text
Component: ChefStoryRow
Page: /chefs
Page list: Chef Profiles (vertical Stack; Desktop gap 160px / Tablet 112px / Phone 88px)

Instance Properties:
Portrait: responsive image
Chef Name: string
Chef Role: string
Content: rich text

Desktop Collapsed:
1164px × auto; white root; overflow clip; padding 0 / 32 / 0 / 64
Chef Identity Row: horizontal, gap 50px
Portrait: 386.5 × 580px
Open button: Button Dark, label “View the story” → Desktop Expanded

Desktop Expanded:
1164px × 580px; padding 40 / 32 / 50 / 64
Portrait: 326.5px × 1fr; identity: 604px × 1fr
Back button: Button White, label “Back” → Desktop Collapsed

Tablet pair:
810px × 570px; collapsed padding 0 / 28 / 0 / 28; expanded padding 36 / 28 / 50 / 28
Expanded portrait: fixed 289.33 × 434px (about 2:3); Story / identity: Fill (`1fr`)
Open: Dark Small → Tablet Expanded; Back: White Small → Tablet Collapsed

Phone pair:
390px wide; collapsed padding 0 / 20 / 50 / 20 with 1fr × 440px portrait
expanded padding 20 / 20 / 30 / 20 with 220px portrait row
Open: Dark Small → Phone Expanded; Back: White Small → Phone Collapsed

Wide Phone pair:
599px; collapsed 400px high with 279px portrait; expanded has 166 × 245px portrait
Open: Dark Small → Wide Phone Expanded; Back: White Small → Wide Phone Collapsed

Every route and root transition: spring-physics 250 30 1 0s.
```

复刻后必须在真实 Preview 中检查首、中、末三个 Instance 及一次可用宽度变化；没有通过这一步，不能把画布结构当作可交付的高级组件。
