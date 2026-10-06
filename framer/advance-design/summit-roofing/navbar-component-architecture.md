# Submit Roofing Navbar：分层组件与可配置导航

> 状态：**Reference，project-derived；结构已验证，精确复刻与 runtime 合同仍不完整**。  
> Provenance：Submit Roofing Canvas（仓库项目名 Summit Roofing），2026-10-06 本聊天官方 Framer Agent targeted readback；读取八个 Component Definitions、全部 Variants、Variables、Controls、内部实例与 CMS 字段，并核对 `/services` 的三端 Navbar 实例。  
> Evidence：以下 `Verified` 只表示该日期的结构与配置；无截图、pointer/touch/keyboard Preview 或内容替换压力测试。解释设计收益的文字标为 `Inference`。本轮仅整理知识，没有修改 Canvas；后来手改后必须重新 targeted readback。

通用设计规则由 [Navbar / Footer](../../basic/patterns/navbar-footer.md) 维护；本文件保存具体例子和精确参数，不将其自动升级为平台默认。较早建设合同见 [项目 Navbar 记录](../../../content-library/summit-roofing/checklist/site/2026-10-06-navbar-cms-overlays-and-expandable-drawer-rows.md)，当前项目入口见 [PROJECT](../../../content-library/summit-roofing/PROJECT.md)。该记录保留的是当时施工证据，不能覆盖后续用户手改。

## 1. 适用与边界

适合学习：包含 Desktop dropdown、Tablet/Phone drawer、独立 disclosure、静态服务导航与 CMS 内容导航的复杂共享 Navbar；重复 row 需要可编辑文字、链接、图标、padding 与反馈样式。

不适合直接照搬：只有少量普通链接的 Navbar、全屏 modal 菜单、不同信息架构或视觉系统。不要为复制本例而添加 CMS、付费依赖、Custom Code 或恢复项目已删除的 Layout Template。本例的黄/绿色反馈、90px 高度、300px overlay 和 390/810/1200px authored widths 都是项目值。

## 2. Verified：完整责任树

```text
Page breakpoint → Navbar instance（placement / width / page Current controls）
└── Navigation/Navbar（vertical Stack；nav）
    ├── Nav Row（horizontal Stack；space-between）
    │   ├── Brand（horizontal Stack；Home link）
    │   │   ├── Brand Mark（hidden Frame；保留的结构）
    │   │   ├── Logo（image-filled Frame；layout null）
    │   │   └── Brand text（RichText；Big Shoulders）
    │   ├── Controls/Menu Button instance
    │   ├── Links（horizontal Stack）
    │   │   ├── Services Menu Trigger（Stack；hover show/dismiss）
    │   │   │   ├── Controls/Text Link instance
    │   │   │   └── RelativeOverlay：Services Menu Overlay
    │   │   │       └── Controls/Text Row × 5（archive + four service links）
    │   │   ├── Projects Menu Trigger（Stack；hover show/dismiss）
    │   │   │   ├── Controls/Text Link instance
    │   │   │   └── RelativeOverlay：Projects Menu Overlay
    │   │   │       ├── Text Row：All Projects
    │   │   │       └── Projects CMS Menu List（Stack + collectionList）
    │   │   │           └── repeated Text Row instance（Title + Slug）
    │   │   ├── Text Link：Contact
    │   │   ├── Text Link：About
    │   │   └── Insights Menu Trigger（Stack；hover show/dismiss）
    │   │       ├── Controls/Text Link instance
    │   │       └── RelativeOverlay：Insights Menu Overlay
    │   │           ├── Text Row：All Insights
    │   │           └── Insights Overlay CMS List（Stack + collectionList）
    │   │               └── repeated Text Row instance（Title + Slug）
    │   └── Contact CTA（linked Stack → Controls/Button instance）
    └── Drawer（vertical Stack）
        ├── Navigation/Services Menu instance
        ├── Navigation/Projects Menu instance
        ├── Text Row：Contact
        ├── Text Row：About
        ├── Navigation/Insights Menu instance
        └── Drawer CTA（Stack → Controls/Button instance）

Each Navigation/* Menu（vertical Stack；own Closed/Open state）
├── Controls/Text Row instance（disclosure header）
└── Disclosure Items（vertical Stack；indentation / child visibility）
    ├── Text Row（All Services / Projects / Insights）
    └── Services：four static Text Rows
        Projects / Insights：CMS list → repeated Text Row

Controls/Text Row（horizontal Stack；space-between）
├── RichText（Content；Utility/Nav）
├── indicator Frame（layout null；Icon Visible）
│   └── IconNode（Icon property）
└── Filler（absolute Frame；feedback layer）

Controls/Text Link（horizontal Stack；link boundary）
└── inner vertical Stack（5px padding）→ RichText（Content）

Controls/Menu Button（Stack；emits Click）
└── Menu（padded horizontal Stack）→ Menu icon + X icon（visibility swap）

Controls/Button（horizontal Stack；auto / auto）
├── Filler（absolute）
├── RichText（Label；z-index 2）
└── clipped 18×18 Frame → absolute Arrow Stack → two Arrow Right icons
```

Inference：普通 Stack 负责排列与尺寸，Component 负责重复结构和状态合同，CMS list 负责数据重复，absolute Frame 只承担局部装饰；Desktop overlay 不另建一个 disclosure Component。Navbar 与子菜单各自拥有状态，避免把三个子菜单的组合全部枚举成 Navbar Variants。未验证多个 disclosure 同时打开的 runtime 行为。

## 3. Verified：Definitions、Variants 与引用位置

| Definition / ID | Selectable variants | Ownership |
|---|---|---|
| `Navigation/Navbar` / `HYvK1XVjO` | Desktop / Tablet Closed / Phone Closed / Phone Open / Tablet Open | Header、Desktop overlays、整体 drawer、外层 open/close |
| `Navigation/Services Menu` / `RVoPX7J0j` | Phone Closed / Tablet Open / Tablet Closed / Phone Open | 静态 Services disclosure |
| `Navigation/Projects Menu` / `BYcoerjnz` | 同上 | Projects disclosure + CMS list |
| `Navigation/Insights Menu` / `vWbcWiC3K` | 同上 | Insights disclosure + CMS list |
| `Controls/Text Row` / `MQNSOUv63` | Style 1 / Style 2 | Row geometry、editable controls、Click、shared feedback |
| `Controls/Text Link` / `K6YRhcFA4` | White / Dark / Current | Compact link、content、surface/state presentation |
| `Controls/Menu Button` / `jfgxCcl1s` | Menu Open / Menu Close / Menu Open small / Menu Close small | Icon swap、size、Click output |
| `Controls/Button` / `H0Qzl5qmu` | Blue / White | Label、filler、arrow viewport、Hover |

Navbar Desktop 是 primary，其余四个是 replicas。三个 Menu 各以 Phone Closed 为 primary，其余三个为 replicas；继承结构不等于每个 state 的属性相同。Text Row 有 Style 1 hover/pressed 与 Style 2 hover gesture replicas；Text Link 有 White/Dark hover/pressed replicas；Menu Button 有 regular Open/Close hover replicas；Button 有 Primary Hover / Secondary Hover replicas。Gesture metadata 区分同名状态，不能把同名 frame 当作重复 selectable Variant 删除。

## 4. Verified：Properties 与实际 binding

| Scope | Property / type | Binding / use |
|---|---|---|
| Navbar | Services / Projects / Contact / About / Insights：ControlReferenceVariable | source 是 Text Link 的 `variant`，选择 White / Dark / Current；绑定到 Links 内对应 Text Link |
| Navbar | Desktop CTA / Tablet CTA / Phone CTA：boolean，default true | Desktop Button visibility；Tablet/Phone Open 的 Drawer CTA wrapper visibility |
| Text Row | Content：string，default All Services | RichText 内容 |
| Text Row | Link：LinkVariable | Row root link；CMS detail rows使用 title/slug binding |
| Text Row | Icon：IconVariable，default Chevron Down | native icon；set `Y7SpbVH16cWqMhj75z1M` |
| Text Row | Icon Visible：boolean，default true | indicator wrapper visibility |
| Text Row | Padding：padding，default `9px 12px 9px 12px` | Row root padding |
| Text Row | Click：EventHandlerVariable | root onTap emits event；instance可配置 `onClick` |
| Text Link | Content：string，default Services；Link：LinkVariable | RichText 内容与 root link |
| Menu Button | Click：EventHandlerVariable | root onTap emits event；Navbar instance `onClick` sets Navbar variant |
| Button | Label：string，default Request an Inspection | RichText；Navbar instances override 为 Get a Quote |

精确区别：Text Row 的 Click 是可用接口，但本例三个 disclosure 的 SET_VARIANT 位于 Menu **root onTap**，并非 child Text Row 的 `onClick` binding。不要把可配置能力写成已使用能力。Navbar 五个 Current controls 只绑定 Desktop Links；Drawer 的 Menu/Text Row 没有绑定这些 controls，不能声称移动端已显示相同 Current 状态。

发现但不推广的变量：Navbar `Link`（`lKlHQQfcV`）、Button `Destination`（`tKxGD_XbA`）、Services Menu `Fill`（`G2rK5nDQe`）在 Definition variables 中存在，但 controls lookup 未列出，所读子树也没有相应 variable binding。保留为待核对，不宣称它们提供有效编辑路径，也不据此自动删除。

## 5. Verified：Geometry 与三端 state routes

| Concern | Desktop | Tablet | Phone |
|---|---|---|---|
| Navbar definition | 1200px × 90px | 810px × auto | Closed 390px × 60px；Open auto height |
| Nav Row | fill width/height；padding `20px 40px` | fill width、auto height；`14px 28px` | Closed fill height / Open 60px；`14px 20px` |
| Logo | 48×23px | 44×21px | 40×19px |
| Links / Menu Button | Links visible；Button hidden | Links hidden；regular Button | Links hidden；small Button |
| Drawer | hidden | Open visible，child Menus start Tablet Closed | Open visible，child Menus start Phone Closed |
| Disclosure roots | N/A | 810px、auto height、clip | 390px、auto height、clip |
| Drawer rhythm | hidden structure gap 20px / padding `24px 20px 28px 20px` | Open gap 0、所读 Open 无 padding attribute | 同 Tablet |

Navbar root 是 white vertical Stack，Open roots `overflow: clip`、bottom padding 20px。Closed roots的所读属性没有显式 overflow，Drawer 用 `visible: false` 隐藏。因此这是 **visibility-toggle drawer** 的结构证据，不是已验证的连续 height-reveal 动画。全部 Navbar variants配置 `spring-duration 0.4s 0.2 0s`。

Navbar routes：Tablet Closed `LXeN9_vkZ` ↔ Tablet Open `Yttq5G7N6`；Phone Closed `PUpKBR9hN` ↔ Phone Open `z1aU6zBvY`。Menu Button instance 的 `onClick` 指向对应目标；Open 内 Brand onTap 也指向 Closed，Brand 仍链接 `/`。两种 action 与 navigation 的先后关系未经 Preview 验证。

| Menu | Phone Closed ↔ Open | Tablet Closed ↔ Open |
|---|---|---|
| Services | `fSnsEZslA` ↔ `M7dJawWBD` | `N1dfl7Dfj` ↔ `H_CCpRkjr` |
| Projects | `Xyh9H0Ubh` ↔ `fM8Mi0kck` | `Vh269iShW` ↔ `xEVJjza8k` |
| Insights | `bTayiqV1z` ↔ `Ivjekwi8S` | `djPnFpB_a` ↔ `tS8Q_y5my` |

所有 Menu root配置 paired onTap、white surface、clip、vertical Stack、gap 0、auto height与 `spring-duration 0.4s 0.2 0s`。Header padding `9px 20px 9px 32px`；Items padding `0px 20px 12px 50px`；child rows `9px 12px`。Tablet Closed header使用 Style 2，其余所读 header states使用 Style 1。Header Icon沿用 Chevron Down，没有已读出的 open-state icon/rotation override；不声称箭头会随展开转向。

Services Closed 中隐藏的五个 children 保留默认 All Services / icon visible；两个 Open states分别 override 成实际 labels、links、icon hidden。Navbar Closed 中 Drawer隐藏，Contact/About 默认值也不代表 Open state内容。复用/替换时核对 replicas，不能只读 primary 后统一写回。

`/services` page instances已验证：Desktop width 1200px；Tablet/Phone width 100%；均 fixed、left/right/top 0、height auto、z-index 10；Services = Current，其余 = White。只核对这个页面的三端使用，不据此证明全站所有实例或宽屏流式行为。

## 6. Verified：Desktop overlays、静态与 CMS repetition

三个 trigger roots配置 onMouseEnter SHOW_OVERLAY、onMouseLeave DISMISS_OVERLAY。每个 overlay直接挂在自己的 trigger wrapper下：300px width、auto height、vertical Stack、gap 0、padding 10px、clip、Pure White surface、1px Mist Grey border、shadow `0px 10px 20px 0px rgba(0,0,0,0.05)`、z-index 10。

Floating：bottom/start、offset X 0 / Y 12px、collision detection true、collision padding 20px。Enter：onMount、opacity 0、x/y 0、scale 1、stagger 0s、`spring-duration 0.4s 0.2 0s`。从 trigger 穿过 12px间隔到 overlay 时能否保持打开仍未验证。

全部 Desktop rows使用 Text Row Style 1、fill width、auto height、icon hidden、padding `12px 14px`：

- Services：All Services `/services`；Repair & Maintenance `/services/repair-maintenance`；Roof Replacement `/services/roof-replacement`；New Construction `/services/new-construction`；Storm Damage Repair `/services/storm-damage-repair`。
- Projects：静态 All Projects `/projects` + Projects CMS list；Title `fiWjBoWXS` → Content；Slug `QPQFHlHk0` → link `{href: /projects/:slug, collectionItem: Slug variable}`。
- Insights：静态 All Insights `/insights` + Insights CMS list；Title `lMCktHoht` → Content；Slug `ao1A7abZQ` → link `{href: /insights/:slug, collectionItem: Slug variable}`。

Repeated instance IDs：Desktop Projects `HeOYHGHeW`、Insights `QMbic_NvX`；disclosure Projects `yOj6hezwA`、Insights `VOB9IwBYP`。每个 list指向其 repeatedDescendantId；只维护 template，不为每条 CMS record建 Variant或组件。未验证 first/last rendered records、最长标题换行、empty或大量记录。

## 7. Verified：内部反馈机制与 token provenance

Text Row root为水平 space-between Stack、auto/auto、clip；Text使用 `Utility/Nav`：Inter 600、14px、uppercase、0.04em letter spacing、120% line height。Indicator wrapper 16×17px，icon 16×16px、stroke width 2。

- Style 1：Pure White default、Mist Grey hover、Bright Yellow pressed；Filler隐藏，布局尺寸不变。
- Style 2：default白底，absolute Filler left -1px、top/bottom 0、width 1px、height 35px；hover width 101%、`spring-physics 250 30 1 0s`，Filler排到文字之前；indicator背景 Deep Navy、icon Pure White。Style 2没有独立 pressed gesture。
- Text Link：White / Dark normal与hover交换white/navy surface；pressed与Current使用Bright Yellow。内部文字同时有 `Utility/Nav` 与 `Links/Navigation` preset；后者默认 Deep Navy、hover Slate Blue。最终字色对比受 preset precedence影响，结构属性不能证明 rendered contrast。
- Menu Button：regular wrapper padding 10px、small 8px；normal Deep Navy、regular hover Bright Yellow；regular Menu icon所读 height仅 `0.4583333333333333px`，width 22px，X 22×22px；small visible icon 18×19px。该regular尺寸异常保留为待视觉核查，不自动修复或当作规范。
- Button：padding `16px 22px`、gap 14px、clip；Filler absolute left -1px、top/bottom 0、height 50px，normal width 1px，Blue hover 101% / White hover 100%，同 physics spring。18×18 clipped viewport里，Arrow Stack含两个18×18 Arrow Right、gap 30px，left -48px → 0px。Navbar desktop Contact CTA wrapper链接 `/contact`；Drawer CTA Button没有在所读结构中发现 destination binding，不能声称其导航已验证。

本次live读出的tokens含 Slate Blue `#365F7A`、Deep Navy `#172B3A`、Mist Grey `#E3E7E8`、Soft White `#F5F6F5`、Pure White `#FFFFFF`、Medium Dark Blue `#243747`、Bright Yellow `#E6F748`、Light Green `#C5F57D`。后两者出现在用户手改反馈中；PROJECT批准的blue-grey品牌方向仍是方向权威，本研究不批准全站新增黄/绿色品牌面。

## 8. 适配顺序、失败修复与验证矩阵

以下是 **Inference / adaptation procedure**，不是本轮执行过的 Canvas写入：

1. 重读目标项目意图与live tree；Reuse现有Navbar/Row/Menu，不从本例复制新Navbar绕过未知状态。
2. 确定Shell/page instance、Navbar、Menu、Row四层owner；决定visibility toggle还是连续height reveal。
3. 先确立Row Properties、gesture styles与event interface，再替换重复rows；保留state-specific overrides、真实routes和CMS bindings。
4. 分开建立整体drawer与子disclosure routes；新建结构先primary后replicas，按device/state设置差异，不枚举内容组合。
5. 为CMS list保留一个repeated Row template；Archive row独立；需要当前路由反馈的所有可见分支逐一binding。
6. 核对外部instance高度、可用宽度、层级、hit target、drawer scroll/viewport合同；批量readback后执行下表runtime paths。

| Risk / failure | Repair owner / path | This example evidence |
|---|---|---|
| Drawer被实例固定高度裁切 | page instance height → Navbar root height/clip；按所选模型修复 | `/services` instance auto；rendered未验证 |
| 平移/hover后row flash或reflow | Row default surface匹配parent；只改变feedback层，检查Filler clip/height | Style 1 parent/rowwhite已读；运行未验证 |
| Nested tap同时collapse/navigation | Menu root与Row event/link边界；若Preview证实冲突，将state action收窄到header | root tap配置已读；传播未验证 |
| Desktop dropdown越过间隔即dismiss | trigger/overlay pointer boundary、offset、dismiss route | 12px offset与leave dismiss已读；连续性未验证 |
| Current只在隐藏desktop链接上配置 | Navbar control向drawer header/row的binding或native current样式 | 本例drawer未binding，不能推广为已完成 |
| CMS title过长、空/大量记录 | Row label sizing、list限制、panel scroll与empty合同 | bindings已读；内容压力未验证 |
| 替换Row丢失可见state内容 | 逐state检查Properties/links，不用primary默认值覆盖replicas | Services open overrides已读 |
| Button看起来可点击但没有目标 | 实际link owner / Link Property，逐可见CTA检查 | Desktop wrapper有link；Drawer待核对 |
| 存在variable但没有有效binding | 对比variables、controls lookup、实际引用；未经批准不改type或删除 | 三个疑似未使用变量保留 |

后续验证最小矩阵：Desktop Services和CMS overlay各一次 hover enter → panel row → real route → dismiss，含最长/首末CMS label；Tablet Navbar Closed → Open → disclosure Open → Closed → Open → real child link；Phone同一路径并实际press。补keyboard/focus/close、触控hit targets、reduced motion、320/1440px、viewport高度/长drawer滚动与多disclosure同时打开。结构readback不能替代这些证据。

## 9. 维护结论

保留为Reference的原因：拥有完整结构与精确配置证据，但缺少rendered、事件传播、触控/keyboard、压力宽度与内容替换结果，并存在未绑定Current、疑似未使用Properties、Drawer CTA link与regular Menu icon尺寸等待核对项。Basic推广的是责任划分和选择逻辑，不是宣称本例已全部通过或应无条件照搬。
