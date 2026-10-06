# Framer Navbar 与 Footer 制作要求

本文档用于 Framer 多页面网站和 Marketplace Template。目标是让 Navbar 与 Footer 具备真实网站需要的导航能力、响应式表现和可维护结构。

## 1. 基本层级与 Shell 策略

多页面网站可采用以下两种等价的共享 Shell 策略；选择取决于页面共同结构是否稳定，而不是页面数量本身：

```text
Layout Template（稳定的全站 Shell）
├── Navbar Component
│   └── Desktop / Tablet / Phone / Interaction Variants
├── Page Content Placeholder
└── Footer Component
    └── Desktop / Tablet / Phone Variants
```

- **优先使用 Layout Template**：绝大多数页面都共享稳定的 Navbar、Content Placeholder 与 Footer，且集中修改 Shell 能降低维护成本时。
- **可使用页面级实例**：页面层级、入口体验或 Footer 组合需要独立变化；项目故意移除了 Layout Template；或共享 Shell 尚未稳定时。每个页面直接放置同一套 Navbar / Footer Component 实例即可。
- 无论采用哪种策略，页面结构仍应清晰区分 Navbar、Content 与 Footer；Navbar、Footer 和重复按钮优先复用 Component，不在每页复制裸 Frame。
- Component 使用 Variant 适配不同断点、背景和交互状态。
- 页面实例负责位置、可用宽度和当前路由状态；组件定义负责内部结构、Padding 和断点 Variant。

不要把 Layout Template 当作强制条件。判断依据是 Shell 的稳定性、页面差异、维护频率和项目当前决定；一旦选定策略，再在受影响页面保持一致并验证链接、宽度和断点。

## 2. Navbar 要求

### 布局与行为

- Desktop 导航保持清晰单行；高度由品牌、hit area、内容和 spacing 合同决定。80px 可作紧凑顶栏参考，不是硬上限；不得为符合参考值缩小已批准的 Logo 或触控目标。
- Navbar 应常驻顶部，使用 Sticky 或 Fixed、`top: 0`，并设置合理的 z-index。
- **层级归属分两层检查**：Navbar Component Variant 可拥有自己的表面层级；但 Fixed / Sticky 的页面实例也必须在每个断点显式拥有高于页面内容的 z-index。不要只因 Definition 已有 z-index 就假设页面实例会浮在内容之上。`10` 是 Summit Roofing 的已验证参考值，不是所有项目的固定数值。
- 滚动方向反馈可按项目需要加入：向下滚动时隐藏、向上滚动时出现。对于刻意极小、固定、持续可见的 Navbar，不要为满足通用模式而加入隐藏行为；在项目 Decisions 中记录该例外即可。
- 优先使用 Framer 原生 Scroll Variant Effect 和 Component Variant。
- 动画应短、平稳、克制。滚动隐藏与 row feedback 不改变布局尺寸；集成式 Drawer / disclosure 可有意改变自身高度，外部 Instance 必须允许该变化。
- 转场由目标反馈决定；配对 states 保持一致并经 Preview 验证。Spring Physics stiffness 250 是局部 filler 的调参参考，不是所有 Navbar 状态的默认值。

### 链接

- Logo 必须链接到首页 `/`。
- 每个导航项必须链接到已存在且非 Draft 的页面或有效页面锚点。
- CTA 按钮必须有明确链接，例如 Contact、Book、Visit 或 View Menu。
- 当前页面状态使用 Link Style 或 Text Link Component 的 `Current` Variant，不要复制多套 Navbar。
- 当共享导航由 Text Link Component 组成时，可通过 Control Reference 暴露其 Variant，或使用原生 current link styling；页面实例选择适用的当前目的地。逐一追踪到实际可见的 Desktop link、drawer header / row，不能把已设置属性等同于三端已显示 Current。普通样式按实际 fill/text 和所在表面选择，不仅看 White / Dark 名称。
- 详情页可高亮其父级归档，而不是创建一个不可导航的新链接：例如 Service Detail → Services、Project Detail → Projects、Insight Detail → Insights。当前路由状态属于页面实例，不属于共享组件 Definition。
- 链接 hover 以颜色、透明度或下划线变化为主，不使用 scale。

### 响应式 Variant

- Desktop：Logo、主要导航、主要 CTA。
- Tablet：空间足够时收紧间距并保持单行；链接或 hit area 已拥挤时可切换为 Tablet Closed / Open Drawer，不能强制缩成 Desktop 小号版。
- Phone：保留 Logo 与必要入口；集成式展开选 Drawer Variants，锚定浮动 panel 选 Relative Overlay。选择由行为与表面所有权决定。
- 如果明确使用 Drawer Variant，应建立 Closed 与 Open Variants，保持 Logo 和菜单按钮位置稳定。

### Phone Drawer Variant（紧凑 Navbar 的推荐模式）

当导航从紧凑固定顶栏的同一表面展开时，可使用共享 `Navbar` Component 的 Closed / Open Variants；Tablet可使用对应配对状态。下面是 **continuous height-reveal** 配方；visibility-toggle 的适用边界见下一小节：

- `Phone` 使用固定高度和 `overflow: clip`；抽屉内容仍存在，只由裁切隐藏。
- `Phone Open` 从 Closed 结构派生，只将外层高度改为 `auto`，显示同一组真实链接。
- Logo、Menu/Close 触发器和链接容器在两个 Variant 中保持相同位置、宽度和内容；不可在打开时重建另一套导航。
- Menu 与 Close 使用精确的 `SET_VARIANT` 目标切换；Phone 链接保留真实页面目标。
- 密集导航 row 的 Press 反馈可采用共享 pressed Gesture Variant 或原生 tapEffect，改变颜色/透明度并保持 `scale: 1`；不改变 row 高度或间距。独立 Menu Button 的反馈另按其 hit-area 合同验证。
- 此模式不要求 Overlay；只有确实需要覆盖全页、遮罩或独立 Modal 语义时才使用 Overlay。

#### Visibility toggle 与连续 height reveal

Closed/Open Variants 不自动证明连续高度动画。先在合同里选择一种机制：

- **Visibility toggle**：Drawer / Items 用 visibility 隐藏或显示，Open 使用 auto height；可用于直接展开，但 visibility 是离散变化，不宣称持续 height reveal。
- **Continuous height reveal**：保留同一组可见内容，以 Closed root 的固定高度与两端 clip 裁切，Open root auto height；按下面的完整高度链验证。
- 两者共享语义结构与 routes，但不能对 visibility-toggle 的现存组件机械套用 continuous reveal 要求；更换主要体验须符合项目授权。Tablet 可采用同样的两种模型。

#### Height-reveal ownership and failure checks

Before changing a shared Phone drawer, inspect the complete ownership chain instead of only the Component definition:

```text
Layout Template or Page breakpoint Frame
└── fixed / sticky Navbar Component Instance  ← placement, available width, instance height
    └── Navbar Closed / Open Variant roots   ← state height, surface and clipping
        └── Drawer                            ← links, CTA, padding and internal rhythm
```

- The Layout Template or page-level instance must allow the Navbar to grow when the open state needs to grow: use `height: auto` unless a separately verified sizing contract owns that height. A fixed closed-height instance will clip an otherwise-correct Open Variant.
- For a height-reveal drawer, keep `overflow: clip` on both Closed and Open roots. `overflow: visible` lets drawer content spill out before the root has revealed it, which reads as a sudden pop rather than an expansion.
- Do not use `visible: false` on the Drawer as the mechanism for a smooth height reveal. Visibility is binary and is not interpolated. Keep the same Drawer structure in both variants; let the root's bounded height and clipping hide it while closed.
- Keep the root transition identical across the paired Closed/Open states unless a Preview proves a state-specific difference is necessary. Do not mix a fast physics spring on one state with a duration spring on the other by accident.
- If the intended interaction is an anchored floating panel rather than a reveal from the Navbar surface, choose the Relative Overlay pattern instead. Do not combine the two patterns in one state route.

Required Phone Preview path at 390px: `Closed → Open → Close → Open → one real internal link`. Verify that the menu stays within the Navbar surface during expansion, the close control remains reachable, the linked page loads, and the state returns to Closed.

### Phone 菜单 Overlay

- Phone 宽度无法容纳完整导航时，将右侧 CTA 改为语义明确的 `Menu` 按钮。
- 当意图是相对触发器浮动的 anchored panel 时使用 Relative Overlay；集成式 height-reveal 使用上方 Drawer Variant。Fixed Overlay 仅用于需要页面遮罩 / modal scope 的体验。
- Overlay 至少包含 Home、主要页面导航和 Contact 主 CTA，不能迫使用户滚动到 Footer 才能访问核心页面。
- Menu 触发器和 Overlay 应保留在共享 Navbar Component 内，由使用该菜单模型的断点控制显示；Tablet 若也采用折叠菜单，应有对应 Variant，不机械隐藏全部 Tablet triggers。
- 必须提供可见的 Close 按钮，并保留原生外部点击和键盘关闭行为。
- 打开动画使用透明度配合轻微位移或缩放，时长建议 280–420ms；禁止直接闪现或使用夸张弹跳。
- Overlay 宽度需要留出屏幕边距。390px 画布可使用约 340px 面板，并启用碰撞检测，避免贴边和横向溢出。
- 菜单项使用真实链接；Contact CTA 复用现有 Button Component，不为每个链接创建独立 Variant。
- 按 [evidence selection](../workflows/image-workflow.md#evidence-selection) 建立打开、关闭和一个真实链接的 runtime evidence；不可用时保持 Blocked，静态画布不足以证明行为。

### 复杂 Navbar：先划分 Component 与 state ownership

```text
Page / Layout Template → Navbar instance（placement、width、route configuration）
└── Navbar definition（header、整体 drawer、desktop overlay triggers）
    ├── Desktop trigger Stack → Text Link + Relative Overlay → Text Row instances
    └── Drawer Stack
        ├── Disclosure Menu component（自身 Closed/Open）
        │   ├── Text Row header
        │   └── Items Stack → static Text Rows / CMS list → repeated Text Row
        └── Direct Text Rows + shared CTA
```

- 普通 Frame / Stack 用于一次性组合与尺寸；重复 row 的结构、hit area、Property 和共享反馈由一个 Row Component 维护；需要独立展开的组由 Menu Component 维护状态。并非每个 wrapper 都应组件化，也不把所有行为堆入 Navbar。
- Navbar 控制整体 Drawer，Menu 控制该组 disclosure，Row 控制自身 presentation/feedback。除非确有互斥行为合同，不把每个子菜单组合复制为 Navbar Variant；不要为不同内容创建 Variants。
- Variants表达设备/结构/状态/样式；Content用 string，Destination用 Link，Icon用 Icon，Visibility用 boolean，Spacing按需要暴露 Padding；Control Reference用于把nested Component的既有variant接口传到外部。
- Shared Row可用于无icon link、带indicator header、indented child与CMS template。先确认这些角色的布局合同相容；instance选择内容、链接、icon visibility和padding，definition负责共同结构和Gesture Variant。
- **配置不是使用证据**：对比 Definition variables、controls lookup、真实binding与可见state。存在Event/Link/Fill variable，不代表父级已连接它；不可把未绑定属性描述成可用功能。
- 原生Frame trigger可直接拥有show/dismiss或state action。触发器是nested Component instance且需由父级响应时，使用其已暴露Event；没有适用Event才在child definition补事件接口。不要一律禁止Event Variable，也不为已有Frame trigger额外建立跨Scope事件链。
- Gesture Variants属于对应base style；同名hover/pressed不是重复普通Variants。不同记录共享同一反馈才共用Gesture；默认Row surface应匹配其直接parent，避免反馈结束时flash；密集row反馈不scale。
- Closed/Open继承结构不意味着属性完全相同。读取primary与全部受影响replicas，保护state-specific文字/Link/visibility/CMS绑定；隐藏内容的default值不得覆盖已完成的Open内容。

### Desktop dropdown 与数据重复

- Dropdown用trigger-owned Relative Overlay；结构属于Navbar，内部重复rows复用Row definition。与Tablet/Phone disclosure分开验证，不能把hover打开作为触控设备的唯一访问路径。
- 少量稳定站点导航可用static row instances；来自现有CMS的Project/Article detail导航用CMS list + 一个repeated Row template，文字和detail destination绑定collection字段。Archive link独立于CMS重复template；不为每条record建Variant。
- Overlay placement、offset、collision、可用宽度和最长标题依据项目确定；绑定后抽查首末记录、长标题与真实detail route，按需要核对empty/大量records与panel滚动。
- Desktop可用hover打开与row反馈；Tablet支持pointer feedback但disclosure默认应有click/tap路径；Phone用tap打开与press反馈。**反馈trigger与持久state trigger分别设计**，项目明确要求优先。
- Root-wide disclosure tap容易和child link/Row Event交互；Preview检查event传播、nested group与真实导航，若发生冲突把toggle收窄到header。Pointer dropdown检查trigger→panel的间隔是否导致提前dismiss；不能仅凭show/dismiss配置报runtime Pass。

结构学习的精确实例见 [Submit Roofing Navbar architecture](../../advance-design/summit-roofing/navbar-component-architecture.md)（Reference；结构已验证，runtime未验证）。它展示层级与Properties，精确尺寸、色彩和待核对项留在例子中，不作为本指南默认。

## 3. Footer 要求

Footer 不只是展示 Brand，还要帮助用户继续浏览、联系和行动。

### 必要内容

- 品牌名称或 Logo。
- 简短品牌说明或 tagline。
- 页面导航：Home、Menu、About、Gallery、Visit、Contact 等。
- 地址与地图链接、营业时间、电话、Email、社交和 CTA 仅在当前项目已确认需要且有事实/真实目标时加入。
- 电话和 Email 存在时必须使用 `tel:` 与 `mailto:` 链接。
- 用户明确指定极简 Footer 时，可只保留 Brand、tagline、页面导航、已确认的联系信息、版权和 Demo 说明；不要为满足通用清单添加社交或重复 CTA。
- Copyright 和必要的模板 Demo 说明。

### 排版

- Footer 顶部必须有充足留白，Desktop 建议约 64-96px。
- 内容不得贴顶部、贴边或全部挤在第一行。
- Desktop 可使用 3-4 列；Tablet 根据宽度改为 2 列；Phone 改为垂直 Stack。
- 内容组之间使用稳定的 gap，信息层级要清楚。
- 标题、正文、链接和辅助文字需要有明确的字号与颜色层级。
- Footer 链接 hover 禁止 scale，避免文字被 overflow 裁切或推开相邻内容。

## 4. Component 与 Variant 规则

- Component 使用 PascalCase，例如 `Navbar`、`Footer`、`PrimaryButton`。
- Layer 使用语义化名称，例如 `Navigation Links Row`、`Footer Visit Information`。
- 禁止保留 `Frame`、`Stack 1`、`Text 2` 等默认名称。
- 创建 Component 后必须回到页面实例检查 Variant、链接、hover、尺寸和响应式控制。
- 同一重复职责通过一个共享组件和Properties/Variants适配；Navbar、Menu、Row等不同职责可分别定义，并通过Instances组合。不要把职责分层误判为近似重复组件。
- Button Variant 应根据背景选择 Primary、Secondary、On Dark 或 Text Link。

## 5. 发布前检查

- 所选 Fixed / Sticky placement、top与内容避让正常。
- Fixed / Sticky Navbar 在 Desktop、Tablet、Phone 页面实例都有高于内容的 z-index；Definition 的值不作为实例层级的替代证明。
- 若启用滚动隐藏，向下隐藏、向上出现正常；未启用时不强制添加。
- Logo、导航、CTA、Footer 导航、联系方式和社交链接均可点击。
- 有适用导航目的地的页面呈现正确 `Current`；详情页高亮父级。核对各断点实际可见branch；Home没有对应菜单项时允许无Current，不为凑数高亮无关项。
- Desktop、Tablet、Phone 分别检查，没有横向溢出。
- Navbar Desktop 保持单行；Tablet按其合同使用单行或Drawer。
- Dropdown与disclosure分别完成open → close → reopen → real link；核对nested事件、Current、hit area、focus、keyboard、reduced motion与长内容/viewport滚动。
- 对Drawer按visibility toggle或continuous reveal合同验证；结构readback与runtime/visual结果分开，不把未执行Preview报为Pass。
- Footer 顶部和四周留白合理。
- Phone Footer 为自然单列阅读顺序。
- 页面只保留一套共享 Navbar 与 Footer。
- Layer、Component、Variant，以及所选 Shell 策略的命名清晰。
- Framer Review 无本次修改产生的链接、尺寸、溢出或对比度错误。
