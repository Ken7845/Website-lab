# Framer 网站基础规范

本文档定义所有 Framer 网站必须满足的最低完成标准，适用于 Section、Page 和完整 Website。

它不规定固定风格，也不替代项目的 Brand Voice、Style Guide 和 Inspiration。它负责确保一个视觉上成立的网站，同时具备系统、响应式、交互、语义、可访问性和维护能力。

## 使用关系

- 项目事实与范围：`content-library/<project>/PROJECT.md`
- 执行顺序：`framer/basic/workflows/build-checklist.md`
- 默认结构：`framer/basic/patterns/pattern-recipes.md`
- 完成前抓漏：`framer/basic/workflows/preflight-audit.md`
- Marketplace 附加要求：`framer/basic/standards/marketplace-guidelines.md`
- 专项细节：从 `README.md` 按任务读取

Baseline 必须在首次搭建阶段进入 Definition of Done，不能等到最终 Polish 才检查。

---

## 1. 第一性原理

一个成型的网站需要同时满足：

```text
视觉层：品牌、构图、排版、图片、内容叙事
系统层：Text Styles、Color Styles、Components、Variants、CMS 决策
交互层：Links、Hover、Sticky、Overlay、Lightbox、Forms
语义层：Metadata、Heading、Alt、按钮与链接语义
响应式层：Desktop、Tablet、Phone 的真实适配
交付层：命名、性能、QA、维护说明和发布准备
```

只完成视觉层不能称为完成。

开始前必须明确：

- 目标用户是谁。
- 网站帮助用户理解什么。
- 网站最重要的行动是什么。
- 每个页面存在的目的。
- 品牌事实、内容和素材是否足够。

缺少事实内容时标记 `Missing`，不得自行编造地址、价格、营业时间、人员和联系方式。

---

## 2. Brand 与视觉质量

网站需要明确 Brand Direction：

- Brand personality
- Core concept
- Visual memory point
- Typography direction
- Color direction
- Image strategy
- Motion character

避免：

- 标准 Hero + Cards + CTA 的机械模板结构。
- 只替换图片、颜色和文字。
- 平均化所有 Inspiration。
- 与项目无关的流行视觉语言。
- 用花哨动效掩盖内容和层级问题。

页面顺序应服务品牌叙事与转化，不因为“网站通常这样”而增加 Section。

---

## 3. Style System

最小 Text Styles：

- Display / H1
- H2
- H3（需要时）
- Body Large
- Body
- Caption
- Eyebrow / Label
- Button Label

最小 Color Styles / Variables：

- Background / Base
- Background / Inverse
- Surface
- Text / Primary
- Text / Secondary
- Accent / Primary
- Border / Divider
- State / Hover
- State / Focus

要求：

- Styles 在批量搭建页面前建立，不在最后统一补。
- 命名按用途，不按临时颜色值或页面名称。
- 同一种语义角色复用同一 Text Style。
- 页面背景、主要文字、品牌色、按钮、Navbar、Footer、Overlay 和 Link States 优先使用 Styles/Variables。
- 允许少量有理由的局部例外，不能让直接样式成为主要系统。
- 当项目已经有等值的命名 Color Style / token 时，必须引用该 token，不得再写等值 hex 或 RGB（例如 `#FFFFFF` 应使用项目的 `Pure White`，`#172B3A` 应使用 `Deep Navy`）。这样后续改色只需更新系统定义，现有实例会同步继承。
- 需要新增、替换或扩展项目颜色时，先说明用途、所影响的 surface/state 与现有 token 为什么不适用，并取得用户明确许可；未经许可不得为了局部效果创建新颜色。

Heading 语义与视觉 Style 是两件事：

- 页面主要标题在内容关系成立时使用 `h1`，但不强制绑定最大号 H1/Display Style。
- 主要 Section 标题在层级关系成立时使用 `h2`，视觉上可以使用更克制的现有 Style。
- 子级内容在真实从属关系成立时使用 `h3`，不能为了完成 Checklist 把普通标签或项目名升级为 Heading。
- Eyebrow、价格、标签不能因视觉醒目而误设为 Heading。

不要为了使用语义而使用语义，也不要让语义预设破坏页面：

- 先判断内容职责，再选择 tag；没有真实页面主标题时，不为凑一个 `h1` 把无关文字设为 `h1`。
- tag、字体角色、字号和行高分别判断。`h1` 不等于必须使用全站最大字号，`p` 也不等于只能使用最小正文样式。
- 如果套用 H1/H2/P 预设造成重叠、裁切、破坏性换行或与图像比例失衡，先换成符合页面的现有视觉 Style 或局部响应式值；不要机械保留不合适的预设。
- 不能通过把所有内容降为 `p` 来逃避层级。最终标准是内容关系正确、视觉成立、屏幕阅读器顺序可理解。

### 标题占位与视觉权重优先于预设字号

标题的 HTML 语义、Text Style 与最终视觉字号必须分开判断。`h1` 说明页面主标题的内容关系，并不要求它始终占用全站同样的视觉面积；Display 或 H1 Style 是可复用的起点，不是不可覆盖的版式答案。

- 在 Desktop 放置标题前，先同时判断：标题字数和单词长度、预期换行数、可用容器宽度、标题 Frame 在 Section 中的实际占位、相邻图片/正文的权重，以及该标题需要承担的是页面开场、Section 转场还是单一词语的视觉锚点。
- 一个短标题（尤其是单词标题）使用默认 H1 尺号时，可能因实际文字面积过小而失去开场权重；可以保留 `h1` tag，同时提高局部字号、调整宽度或字距，使它在画面中形成必要的占位。
- 一个较长标题使用同一 H1 尺号时，可能因多行和总文字面积而占满首屏、压迫图片或正文、破坏留白；应保留正确的 `h1` tag，但按当前容器和叙事角色降低局部字号、收窄 Frame、调整行高或设置合理 max-width，使它与页面其他元素重新取得平衡。
- 不要仅因两个标题同为 `h1` 就强制共用完全相同的字号，也不要仅因同一 Text Style 已存在就忽略标题长度差异。优先比较“标题在画面中实际占多少空间、比相邻元素重多少”，而非只比较 CSS/Framer 字号数值。
- 调整顺序应为：先确认文字职责与 tag → 检查当前断点的 Frame width/max-width 和预期行数 → 评估画面占位与相邻内容权重 → 再选择局部字号、tracking、line-height 或宽度 override。不得通过错误 tag、绝对定位、裁切文字或任意缩小正文来弥补标题失衡。
- 每个 Desktop 调整都必须在 Tablet 与 Phone 重新判断；标题长度、换行和可用宽度改变后，不机械继承 Desktop 的字号或占位比例。

示例：AURELIA 的 `/menu` 中单词 `menu` 为 `h1`，Desktop 以 200px 建立开场锚点；`/about` 中较长的 `A meal begins long before the table.` 同样保留 `h1` 语义，却以 96px、70% 宽度获得更平衡的首屏占位。两者的正确性来自各自在画面中的总权重，而非共享同一个 H1 视觉尺寸。

响应式字号必须有明确策略，不把 Desktop 字号逐页临时缩小成 Phone。

---

## 4. Components、Variants 与 Properties

优先组件化跨页面或高频重复结构：

- Navbar
- Footer
- Buttons
- Product / Menu / Project Cards
- Contact Info Rows
- Form Fields
- 其他实际重复结构

Variant 表达状态或结构：

- Desktop / Tablet / Phone
- Light / Dark
- Default / Hover / Active / Disabled
- Compact / Expanded

Property、Fill 或 CMS 表达内容差异。

同一行、卡片或项目模板中，标题、编号、Meta、状态、图片、基础 Fill、Hover Fill 和 Link 等可编辑内容，应优先暴露为 Component Properties / Variables，并在页面 Instance 上设置。不要把每个项目复制成一个内容 Variant。

推荐：

```text
ArchiveOptionRow
├── Desktop
├── Phone
└── Desktop Hover

Instance Properties
├── Number
├── Title
├── Meta
├── Surface
└── Hover Surface
```

`Desktop Hover` 是默认唯一的 pointer hover 状态；在没有项目级证据要求不同输入模型时，Desktop 与 Tablet 的 pointer feedback 默认使用 Hover，Phone 触摸路径默认使用 Press / Tap，且不机械复制 Hover Variant。若特定项目确实需要手机外接指针状态，必须先由真实 Preview 证明，再增加最小必要变体。

### Interactive row default surface

任何会在 Hover 或 Press 时改变背景的可见 Row / Stack，必须先在 Default 状态的行容器上显式填写与其直接父级表面相同的命名 Color Style / token；不得依赖透明背景“看起来一样”。Hover / Press 只从这个明确的 Default surface 改变到反馈色，且必须保持现有几何。这样指针离开或按压结束时，Framer 会回到同一已定义表面，避免透明层重新露出造成闪烁。例：Pure White 菜单上的 `Services All Row` Default fill 应引用 `Pure White` token，Hover 才切换至 Slate Blue token。若父表面随后改色，必须同步更新该交互行的 Default fill。

### Card surface, padding and external colour controls

When a reusable card can sit on a background different from its own surface, the Component Definition owns the complete inner edge: apply one intentional padding value to the visible card surface so its image and text content share the same inset. Do not leave a text stack flush against a distinct card fill merely because the default surface happens to match the surrounding page.

- Expose the card's `Surface Color` and the independently meaningful text colours (for example Label, Title and Meta) as Component Properties / Variables when buyers or page Instances may need to adapt the card to a different background.
- Keep CMS responsible for record content and images; it should not be the workaround for a presentation-only surface or text-colour decision.
- If the image is intentionally full-bleed, make that a deliberate media-frame contract and give the text surface its own explicit padding. The image/text edge relationship must still be visually intentional.
- Keep Default, Hover and other visible variants on the same padding and colour-variable contract unless their state specifically requires a documented contrast change. Do not solve a hover mismatch by creating a content-specific Variant.

Failure mode: a card appears aligned only while its surface blends into the parent, then looks broken as soon as its fill changes. Repair the Definition rather than each CMS Instance: add the visible-surface padding, bind the root fill and relevant text nodes to exposed colour variables, then verify a Default sample, any visible state, and one page Instance with a contrasting surrounding background.

Verified project-derived example: Summit Roofing Project Card, 2026-10-04. Its unpadded dark root made the CMS text visually flush when placed on a different background; the repair added 20px root padding and external Surface / Label / Title / Meta colour controls while retaining CMS image and text bindings. This is evidence for the decision rule above, not a required universal 20px value.

Variant 只承担 Desktop / Phone、Default / Hover 等真实结构或状态差异。新增项目通常只增加一个 Instance 和对应内容，不增加一组内容 Variant。

禁止：

- `Variant 2`、`Copy` 等无语义命名。
- 为每张不同照片创建相同结构的 Variant。
- 为每条项目记录复制 Desktop、Phone 和 Hover 内容 Variant。
- 同时保留两个表达同一标题或状态的重复 Property。
- 为简单效果制造几十个状态。
- 为了组件数量而组件化一次性 Section。

组件化后必须回到实例检查：Variant、Properties、Link、Effect、Hover、Cursor 和各断点 override。

### 组件内部与外部实例的尺寸契约

### 长条边框组件的宽度归属

当 FAQ、可展开故事行、章节行等长条边框组件的边界应跟随页面可用宽度时，组件根层、外部 Instance 与承载它的 List 不应为了“看起来整齐”而加入任意 `max-width`。

- 宽度由父级 Section 的可用空间和 Instance 的 Fill 决定；组件自身负责横向 Padding、边框/分隔线、触控区与内部内容关系。
- `max-width` 只属于真正需要阅读行长控制的内部文字 Wrapper，或已经验证的固定几何契约；它不能承担整条边框的宽度。
- 发现边框在 Preview 加宽后不响应时，依次检查组件根层、页面 Instance、最近父级 List/Stack 与 Section 的宽度归属；不要通过拉伸图片、固定像素宽度或 Absolute 定位补偿。
- 至少在 Desktop、Tablet、Phone，以及窄屏和加宽 Preview 中检查收起与展开状态的边框连续性、文字可读性与图片比例。

这是一条尺寸归属原则，不要求所有组件使用同一内部结构。AURELIA 的 `EveningChapterRow` 与 `FAQ Row` 是当前项目中的对应证据。

### 组件文字的三端契约

组件内部不要直接引用已经成型的 `Text Style`。页面 Breakpoint 与 Component Variant 是两套独立系统；直接引用 Style 不会可靠地随着组件的 Desktop / Tablet / Phone Variant 自动切换，容易造成组件画布、实例和实际排版不一致。

- 在组件内以当前项目 Text Style 为视觉基准，手动写入相同的字体、字重/轴、字号、字距、行高、段落间距、颜色与文字宽度；不要临时换字体或另造一套排版语言。
- 每个包含响应式文字的组件必须有语义化 `Desktop`、`Tablet`、`Phone` Variant，并在每个 Variant 内明确覆盖文字的三端数值与可用宽度。
- Page Instance 必须选择与页面断点一致的 Component Variant；不得让 Phone 继续继承 Desktop 文字尺寸。
- Text Style 仍是页面普通文字与系统参考的唯一来源；组件的手动值必须在对应项目的 current manifest、active decision 或组件记录中可追溯到该 Style 的 L / M / S 参数。
- 文字视觉大小与 HTML 语义分开处理：页面只能有一个 `h1`；组件可采用 H1 的视觉比例，但在非页面主标题的场景保留正确的 `h2` / `h3` 语义。

组件不是脱离页面存在的画板。凡是内部含有固定坐标、裁切窗口、横竖轨道、Absolute 内容或基于像素的动效，必须先定义并保持“组件内部尺寸 ↔ 页面实例可用尺寸”的对应关系。

- Desktop、Tablet、Phone 的 Component Variant 必须与外部 Instance 所选断点一一对应；不要在 Phone 页面继续使用 Desktop Variant，或让 Tablet Instance 继承不兼容的固定尺寸。
- 外部 Instance 的 `width`、`height`、`max-width`、父级 Stack 分配方式，必须能容纳组件内部的关键 Fixed 容器。内部尺寸可以是固定值，外部根尺寸则可按内容使用 Fill / Fit / 明确 max-width；重点是两者必须属于同一套尺寸模型。
- 当内部有 Image Viewport、slide、number reel 或文字 reel 等像素坐标时，外部可用宽高一变，内部的 Fixed 值、pitch、裁切窗口与状态位移必须同时重新计算或切换到对应 Variant。
- 不要只在 Component Canvas 中看起来正确。必须把实例放回真实 Section，在 Desktop、Tablet、Phone 外部 Preview 中检查首项、中间项、末项，以及父级宽度变化后的对齐。

### 组件自身的 Padding 归属

- 可复用组件的横向 Padding 属于组件自身：只要它决定了组件的可见边界、hover/pressed 表面、分隔线、图片裁切、触控区，或内部 Fixed 容器的可用宽度，就必须写在该组件的 Desktop / Tablet / Phone Variant 根层或其可见内部 Stack，不能依赖某一个页面 Section 的横向 Padding 才成立。
- 页面外层 Section 负责背景与垂直节奏；组件外层 List / Stack 只负责排序、间距、对齐和可用宽度。不要让它同时承担所有组件的左右留白，否则 Component Canvas 无法预览真实效果，组件被复用到另一页时也会失去尺寸契约。
- 一个 Section 同时含组件与普通标题、正文或图片时，去掉 Section 的统一横向 Padding：组件自行处理自己的 Padding；标题/正文使用独立的 Text / Introduction Stack；普通图片和收尾文字使用独立的 Media / Closing Wrapper。这样非组件内容仍能保留同一视觉对齐，组件也能独立预览。
- 例外：一次性、完全不包含可复用组件的普通内容 Section，可以继续在 Section 外层统一设置横向 Padding。

示例：外部实例在 Desktop 给图片裁切区 585px 的稳定可用宽度时，组件内部的 Image Viewport、每张 slide 和横向位移 pitch 都必须以 585px 为坐标基准；Tablet 若改为 500px，则必须使用 Tablet 专属的 500px 轨道与位移值。只改外部 Instance 或只改内部组件，都会让切换后的图片偏离裁切框。

创建后强制回到页面实例检查时，追加：

- [ ] 外部 Instance 与当前 Desktop / Tablet / Phone Variant 对应。
- [ ] Instance 的外部宽高模型能容纳内部的 Fixed Viewport、轨道和裁切窗口。
- [ ] 固定坐标组件已在外部 Preview 改变可用宽度后复查，没有变形、露白或偏移。
- [ ] 改变或单独预览组件时，组件自身已包含其真实横向 Padding；没有依赖某一页面 Section 的 Padding 才看起来正确。
- [ ] 混合 Section 已将组件、标题/正文、图片/收尾内容拆到各自的 Padding 所有者；外层只保留背景与垂直节奏。

---

## 5. Layout 与共享结构

多页面网站默认：

```text
Layout Template
├── Navbar Component
├── Content Placeholder
└── Footer Component
```

要求：

- 页面只维护自己的 Content。
- Navbar/Footer 不在每页复制。
- 优先使用 Stack 和 Grid，明确谁拥有宽度。
- **Max-width ownership rule**：默认不在 Page breakpoint root、最外层 Page Content、full-bleed Section 或负责分配可用宽度的 senior structural parent 上设置 `max-width`。这些层使用 Fill / `1fr` 跟随视口，负责背景、外部构图和可用宽度分配，不能同时承担局部内容封顶。
- 紧邻 Section 的第一层或前几层结构 Stack 通常仍属于流式页面骨架，不得因为“统一内容宽度”就默认加 `max-width`。过早约束会让 Hero、Grid、Navbar、Footer 或整组 Page Content 像一个固定画板，在宽屏停止扩展、在窄屏过早换行或留下不受控边带。
- `max-width` 只放在真正需要控制阅读行长或组件尺寸契约的 **deepest valid max-width owner**，例如局部 Content Wrapper、文本列、特定 Grid、列表或组件。判断时沿 `Breakpoint → Section → structural Stack → local content owner` 逐层追踪；先区分“铺背景/分配可用宽度的骨架”与“约束具体内容的内层”，不要把两者合并。
- 若设计明确需要 bounded canvas / centered shell，只有在项目语言或用户要求批准、外层仍有独立的全视口背景 Owner、且 320 / 390 / 810 / 1200 / 1440+ 均验证成立时，senior parent 才可例外拥有 `max-width`；不得把这个例外当成普通响应式默认值。
- 验证时至少比较 Desktop 1200 与 1440+：外层和 senior structural parents 应继续 Fill / `1fr` 扩展，只有被明确选定的局部 Owner 保持最大宽度。若移除约束后行长过长，应约束文字列或局部 Grid，而不是把 `max-width` 重新加回靠外层的公共 Stack。
- 修复顺序：先从 Page root 沿 width chain 向下定位第一个不应封顶的 Owner → 移除或下移该 `max-width` → 保持外层 Fill / `1fr` → 在最深有效 Owner 恢复必要的阅读宽度或几何上限 → 复检相邻 Section 与全部相关断点。不要先缩小字号、固定子层宽度或添加额外 Padding 来补偿。

已观察到的 failure signature（Summit Roofing，2026-10-03 用户截图）：图片、标题与正文被 senior parent 一起封装成窄的居中画板；视口变化时整组内容不按可用宽度重排，只改变外部空白、过早换行或裁切。该现象证明需要检查 width ownership，但截图本身不授权假设具体节点或数值；仍须通过 live-tree readback 定位真实 Owner。

- 间距来自稳定系统，不逐个 Section 随机设置。
- Targeted Preview 或截图如确认文字被父级 Stack 裁切，先排查该父级的固定尺寸、Padding 和宽度所有权；确认文字本应自然外溢且不存在横向溢出后，把该父级 Stack 的 `overflow` 改为 `visible`，再复检相关断点。不要把 `visible` 设为默认值，也不要用它掩盖错误尺寸或布局溢出。
- 允许不同 Section 使用不同构图，不把全站变成同一种容器模板。
- 图片容器的比例、裁切与焦点必须保留该图承担的主要内容；如果人物、菜品主体、动作、空间关系或必要文字因裁切而变得不可读，应先调整图片位或更换素材，而不是为了版式整齐保留无效图片。完整判断与跨页面素材选取规则见 `framer/basic/workflows/image-workflow.md` §5.1–§5.2。

### 用嵌套 Stack 建立叙事层级，而不是统一 gap

大型 Section 不是一串同级的文字和图片。先按叙事关系切成若干“段”，再把每一段拆成更小的相关元素组；每一级 Stack 只负责它自己的关系与间距。这样图片、文字、转场与留白都有明确的主次，而不是所有内容以一个统一 gap 平铺。

推荐关系树：

```text
Section（Surface / 外部 Padding）
└── Content Stack（内容最大宽度 / 主段之间的节奏）
    ├── Heading Group（标题与开场留白）
    └── Narrative Stack（多个叙事段之间的大停顿）
        ├── Story-Image Group（故事与其直接承接图片之间的小 gap）
        │   ├── Story Copy Group（段落与局部说明）
        │   └── Image Row
        ├── Text-Image Composition（文字组与图片组的中等 gap）
        │   ├── Story Copy Stack
        │   └── Image Row
        └── Closing Story Group
```

- `Section` 的 padding 负责内容与背景边缘的距离；不要用子元素 gap 假装成 Section 留白。
- `Content Stack` 只负责标题、叙事大组或明显篇章之间的一级节奏。它的 gap 可以较小或较大，但必须表达篇章关系，不能成为页面所有距离的默认值。
- `Narrative Stack` 用较大的 gap 分隔真正的故事转场，例如一段经历结束、图片作为证据出现、叙事进入下一阶段；它让读者感到“进入了下一部分”。
- `Story-Image Group` 用较小 gap 把有直接因果或说明关系的文字和图片绑在一起。读者应一眼知道这张图属于哪段故事，而不是把它读成独立图库。
- `Text-Image Composition` 可以使用水平 Stack，在 Desktop 让一组故事与另一张图片形成对话；其中的文字 Stack 仍应有自己的更小 gap。到 Phone 时改为垂直 Stack，保持“文字 → 图片 → 文字”的自然阅读顺序，不仅是把 Desktop 压窄。
- gap 的数值不需要全站相同，也不应随机。它们应形成有限、可解释的层级，例如：元素内部 < 文字与直接图片 < 同一叙事段 < 篇章转场 < Section padding。先定义关系，再为每层选择数值。
- 不要只把所有子项放入一个大 Stack 后设置一个统一 gap；这会消除标题、故事、图片与收束之间的语义距离，使页面缺少主次和叙事节奏。
- 创建或重构时，先画出父子关系和每个 gap 服务的对象，再写入 Stack。不要用绝对定位或空白 Spacer 代替这些真实关系。

案例：AURELIA `/about` 的手动调优将 Cooking 与 Relationships 拆成标题层、多个 Narrative Stack、故事—图片小组和文字—图片对话组。外层/内容层/段落层/局部组分别使用不同 gap，使长故事、两张图片和收束文字既连续又有转场；这一结构优先于把所有节点塞进同一个等距 Stack。

Layer、Component 和 Variant 使用语义名称。详细规则见 `framer/basic/standards/layer-naming.md`。

---

## 6. 页面结构与内容目标

每个页面必须有明确目的和主要行动。

常见页面职责：

- Home：解释品牌、建立兴趣并引导核心行动。
- About：建立信任，说明故事、过程、团队或价值。
- Product / Service / Menu：清楚展示可选择内容。
- Gallery / Work：展示证据、作品、空间或过程。
- Contact / Visit：完成联系、到店、预约或询价。

不要机械创建全部页面。页面和 Section 以 `PROJECT.md` 为准。

正式页面不得存在：

- Lorem Ipsum。
- 无说明占位内容。
- 无来源的品牌事实。
- 无目标 CTA。
- 只能通过 Footer 才能找到的核心行动。

### 强制规则：访客文案不得含模板或编辑操作说明

面向访客的网页文案必须服务访客的决策、理解或行动，不得指导编辑者、模板买家或 Agent 操作网站。例如“Add…”，“Replace…”，“Use this…”，“Update before publishing”，“Placeholder”，或“在此填写”只能出现在仓库文档、Component / Layer / Property 名称、注释或编辑器说明中，不能作为公开页面的标题、正文、CTA、卡片、表单提示或状态文案。

这不禁止真正帮助访客的引导，例如安全准备、检查前须知或下一步说明；判断标准是它是否面向访客目标，而不是是否含有祈使动词。当正式事实或已批准的 Demo 内容缺失时，优先省略该内容、使用完整且连贯的授权 Demo 参考内容，或用中性、面向访客的方式表达真实限制；不得用前台操作说明填补空白。实施与 QA 必须检查所有新增或修改的可见文本，发现模板或编辑操作说明即为 `Fix Required`。

---

## 7. Links 与 Conversion

以下信息在主要出现位置必须可操作：

- Logo → `/`
- 电话 → `tel:`
- 邮箱 → `mailto:`
- 地址 → Map URL
- 社交账号 → Real external URL
- 预约、购买、询价、到店 → Clear CTA

要求：

- 主体与 Footer 的关键信息一致。
- Navbar、Footer、CTA 不使用空链接。
- 不连接到不存在、Draft 或无关页面。
- 外部链接按需要在新标签页打开。
- Contact 页面没有表单时，必须有清楚的替代联系路径。

---

## 8. SEO 与页面语义

每个正式页面必须有：

- 唯一 Page Title。
- 独立 Meta Description。
- 一个主要 `h1`。
- 按关系组织的 `h2/h3`。
- 清晰页面路径。

全站必须有：

- favicon。
- Open Graph 图片。
- 必要社交分享信息。

不能只在首页设置 Metadata，也不能用字号模拟 Heading。

---

## 9. 图片与 Alt

图片必须：

- 符合品牌和内容目标。
- 使用适合容器的网页输出尺寸。
- 在各断点保留核心视觉信息。
- 不含不应出现的截图 UI、黑块或控件。

Alt 判断：

- 信息性图片：简短、具体、与上下文相关的 Alt。
- 装饰性图片：显式空 Alt。
- 不允许 Alt 未定义。

裁切、联系表、批处理和 reconnect 规则见 `framer/basic/workflows/image-workflow.md`。

---

## 10. Responsive

最低检查宽度：

- 320px Phone
- 390px Phone
- 810px Tablet
- 1200px Desktop
- 1440px+ Wide Desktop

Desktop 关注构图、空间感、大图和 max-width。

Tablet 需要真实布局调整，不能只是缩小 Desktop。

Phone 检查：

- 核心导航完整。
- 内容顺序自然。
- Row/Grid 转为合适 Stack 或减少次要信息。
- Heading、邮箱、价格、日期和 metadata 不破坏性断行。
- 触控目标约 44×44px 或更大。
- 图片重新设置比例和焦点。
- 无横向溢出和极小文字。

Footer 在 Phone 使用自然垂直阅读顺序。

---

## 11. Motion 与交互

Motion 服务：

- 品牌氛围。
- 阅读节奏。
- 状态反馈。
- 空间层级。

优先使用 Framer 原生 Effects、Variants 和 Overlays。

默认模式：

- Sticky/scroll Navbar → Navbar Variants。
- Phone Navbar Menu → integrated drawer用Closed/Open Variants；anchored floating panel用Relative Overlay；选择与验证读 [Navbar models](../patterns/navbar-footer.md#响应式-variant)。
- 简单图片放大 → Lightbox Effect。
- 页面级 Modal → Fixed Overlay。
- Dense Row Hover → Gesture Variant + color/opacity。
- Image Hover → Outer Frame + Inner Image scale。
- Image-and-text Card Highlight → keep the card geometry stable and apply a brightness filter to the image layer only; use `120%` as a tuning reference when a lighter, not darker, photo response is desired.

### Image-card brightness highlight

For a card that combines an image and adjacent text, a hovered image can signal focus by increasing the image layer's `brightness` (for example, `120%`) instead of placing a low-opacity dark fill over the image. Apply the filter to the image/content layer inside its clipping frame—not to the card root—so the text, card surface, padding and external colour controls do not brighten with the photograph.

- Keep the card's outer geometry, image crop, text placement and row/grid position unchanged. Brightness is a visual highlight, not a layout animation.
- Treat `120%` as a starting point, not a universal number. Tune only enough to preserve photo detail and text/surface contrast; retain a documented project-specific value when current Canvas evidence differs.
- Do not use a dark mask merely to simulate this highlight. A separate overlay remains appropriate only when it is needed for readable over-image text or an intentionally darker art direction.
- Keep the Pointer Hover state separate from the Phone static/touch path, and verify one actual pointer interaction before calling runtime behavior passed.

Verified project-derived example: Summit Roofing Project Card, 2026-10-04. The Hover image layer has no dark-mask override and uses `brightness: 130%`; the user identified `120%` as the reusable tuning reference. The nine CMS-bound instances inherit the same image-only state while their CMS content and card colour controls remain independent. This is project evidence, not a universal requirement.

禁止：

- 密集链接、整行或整个卡片 hover scale。
- 直接闪现的 Overlay/Lightbox。
- 过度 bounce、旋转和无目的动画。
- 为简单原生效果引入 Custom Code。

详细规则见 `framer/basic/patterns/motion-design.md` 和 `framer/basic/patterns/pattern-recipes.md`。

---

## 12. Accessibility 与 Reduced Motion

检查：

- 颜色对比度和正文尺寸。
- 可见 Focus 状态。
- 键盘顺序符合视觉顺序。
- Hover 信息在触控/键盘下可获得。
- 按钮和链接名称描述操作结果。
- Overlay、Lightbox、Form 不造成焦点丢失。

Reduced Motion 下：

- 取消大位移、强缩放、视差和持续自动运动。
- 可以保留短透明度变化。
- 不得破坏内容、导航和反馈。

不为简单项目强制增加 Custom Code；优先使用 Framer 和系统原生行为。

---

## 13. CMS 决策

优先评估 CMS 的条件：

- 同一结构大量重复。
- 用户需要经常增删排序。
- 内容有明确字段。
- 需要筛选、分类或详情页。

不为了“看起来专业”而 CMS 化少量静态内容。

CMS 必须字段清楚、默认内容完整、无测试数据，并能承受长标题、不同图片比例和可选字段缺失。

---

## 14. Performance 与维护

- 图片尺寸匹配容器。
- 动画数量克制。
- 不保留无意义 Code、Components、Variants 和 CMS 字段。
- 核心视觉可通过 Styles 修改。
- 核心结构可通过 Components/Properties 修改。
- Layer 和内容入口清楚。
- 第三方依赖和授权明确。

目标是后续修改比首次搭建更简单。

---

## 15. Definition of Done

### Section Done

- 使用正确 Text/Color Styles。
- 重复结构使用合适 Component/Property/CMS。
- 图片、Alt、Links 和 Heading 完成。
- Desktop、Tablet、Phone 成立。
- 必要 Motion 和 Interaction 完成。
- Targeted readback 无结构性遗漏。

### Page Done

- 内容与页面目的完整。
- Metadata、一个 h1 和主要 h2/h3 完成。
- Navbar、Footer、CTA 和 Contact/Visit 信息可操作。
- 所有图片有明确 Alt 判断。
- 320/390/810/1200/1440+ 行为合理。
- 完成一次目标化 Preview 检查。

### Website Done

- Layout Template、Navbar、Footer、Buttons 和核心 Styles 成立。
- 全部正式页面进入 `STATUS.md` 或 PROJECT Current Status 的 Build Status Matrix。
- favicon、Open Graph、Links、Accessibility 和 Performance 完成。
- Sticky、Overlay、Lightbox、Form 等关键交互真实验证。
- 通过 `framer/basic/workflows/preflight-audit.md`。
- 持久例外记录在 `DECISIONS.md` 或 PROJECT Decisions；当前 Missing / Blocked 记录在 Status 与 current facts source。

---

## 16. 避免集中 Polish

不要采用：

```text
先完成所有视觉页面
→ 最后统一补 Styles、Phone、SEO、Alt、Links、Components 和 QA
```

应该按 Section/Page 纵向完成：

```text
内容
→ 视觉
→ Styles
→ Components
→ Links 与语义
→ Responsive
→ Motion
→ Targeted Preview
→ Done
```

如果最终 Polish 仍需要新增 Metadata、Heading、Alt、Phone Navigation、共享 Components 或核心 Styles，说明首次搭建没有执行 Baseline。

真正的最终 Polish 主要处理：

- 小范围间距与换行。
- 图片焦点。
- Hover 对比度。
- 动画节奏。
- 少量文案修正。
- 发布前点击抽查。

---

## 最终标准

视觉上：像一个真实且有辨识度的品牌。

结构上：像一个可理解、可维护的系统。

使用上：用户能够理解内容并完成行动。

交付上：不把基础能力和结构债务留给最终 Polish。
