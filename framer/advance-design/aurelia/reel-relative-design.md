# Framer 高级组件：Reel Text 与 Button Arrow

> 状态：**Reference，mixed project-derived**。
> Provenance：AURELIA `Reel Text` native Component，live Canvas definition、shared Navigation / Footer instances 与一次组件截图回读，2026-08-16；Submit Roofing `Controls/Button` native Component，live structural readback，2026-10-02。
> 范围：短、单行文字的纵向 reel，以及 Button 内不改变外部尺寸的双箭头横向 reel。两者都是 pointer enhancement，不是长文案、自动换行文字或 Phone 必经信息路径的通用方案。

## Text Reel：何时使用 / 不使用

适合：一个短 Label 需要在不改变外部布局宽度的情况下，显示同一文字的纵向 reel；例如 AURELIA Footer 的品牌名、Navbar 的 `Menu / About / Reserve / Chefs` 和 Footer 的五个站点链接。

不适合：可能换成两行的正文、可变数量列表、需要逐项状态的 selector，或需在 Desktop / Tablet / Phone 之间改变文本换行策略的内容。遇到这些需求时，改用相应的独立文字窗口 / reel（例如 Dish Selector），不要强行复用本组件。

## Text Reel：已验证的责任划分

| 层级 | 责任 | 当前证据 |
|---|---|---|
| `Reel Text` Component | 文字重复、裁切窗口、Hover 位移、字体 geometry 与可编辑 Property | 原生 Component 定义 |
| `Label` Property | 一次编辑，绑定 Helper 与三行 Track 文字 | `AURELIA` 默认值；每个可见文字为同一变量 |
| `Link` Property | 绑定每一个 Track 文字的链接；实例可安全用于不同页面路由 | Navbar / Footer 实例各自拥有 `/`、`/menu`、`/about`、`/chefs`、`/reserve` |
| 父 Navigation / Footer Component | 放置、已有点击 / link 容器、Desktop / Tablet / Phone 组合 | 原有 shared components 保持负责外部响应与 Phone Open 状态 |
| 实例 | 文案、目标路由与字体 Variant | Desktop / Tablet Navbar 使用 `Button`；Desktop / Tablet Footer nav 使用 `Body`；Phone 保持普通 Rich Text；Footer brand 使用 `League Gothic` |

## Text Reel：当前组件树

```text
Reel Text
├── Properties: Variant, Label, Link
├── Font Variant (League Gothic / Button / Body)
│   ├── Helper Rich Text — normal flow, opacity 0, same Label + font
│   └── Text Reel Track — absolute vertical Stack, gap 0
│       ├── Label row 1 — Link Property
│       ├── Label row 2 — Link Property
│       └── Label row 3 — Link Property
└── Native Hover gesture Variant
    └── inherits the same tree; only Track position changes to `bottom: 0`
```

Helper 是组件可用宽度的唯一 in-flow 来源；Track 绝对定位，不能参与组件宽度计算。根节点裁切溢出，因而父 Stack 只需要放置 intrinsic-width 的 Component Instance，文字变长时边界会随 Helper 一起变宽。

## Text Reel：字体 Variant 与坐标合同

所有 Track 都是三行、`gap: 0px`。默认态显示第一行；Hover 态将 Track 移到 `bottom: 0px`，显示第三行。

| Variant | 字体来源 / 当前值 | 窗口与单行高度 | 默认 Track | Hover Track | 用途 |
|---|---|---:|---:|---:|---|
| `League Gothic` | League Gothic 400 / `100px` / `1.2em` | `80px` | `bottom: -160px` | `0px` | 品牌名 |
| `Button` | Inter 600 / `10px` / `1em` / `0.02em`（与当前 `Type/Button` 一致） | `10px` | `bottom: -20px` | `0px` | Navbar 与紧凑按钮标签 |
| `Body` | Inter 400 / `17px` / `1em` / `-0.012em` | `13px`; Track 当前总高 `53px` | `bottom: -40px` | `0px` | Footer 导航 |

`Body` 当前使用 inline font values，而不是 `Type/Body` preset：该 preset 的 line box 会使此固定高度 reel 留出过大的视觉间距。这个例外只适用于这条可裁切的单行轨道，不是放弃现有 Text Style 的通用许可。

## Text Reel：实现与替换顺序

1. 先确认内容是短单行文字，选择现有 `Reel Text`，不要创建新副本。
2. 选定 `League Gothic`、`Button` 或 `Body` font Variant；不要建立每条导航内容的 Variant。
3. 保持 Helper 与三行 Track 都绑定同一个 `Label` Property；Track 保持 absolute、`gap: 0px`，根保持 clip。
4. 若组件作为链接使用，先把 **所有** Variant / Hover state 的三行文字都绑定 `Link` Property；不得保留某一行的旧 hard-coded route。
5. 替换原标签时，把新 Instance 插回原 parent 和 index，保留 parent 的导航结构；写入正确的 `Label`、`Link` 和 font Variant 后再删除旧 Rich Text。
6. 对 Navigation Phone Open，显式复查触发文字的实例 override：AURELIA 默认 `Menu`，Open 状态为 `Close`。

## Text Reel：响应式与状态合同

- `Reel Text` 本身没有 Desktop / Tablet / Phone Variant；字体 Variant 只决定字形和 fixed viewport geometry。
- 外部 shared Navigation 负责 Desktop、Tablet、Phone、Phone Open；Footer 负责 Desktop、Tablet、Phone。当前 AURELIA 仅在 Desktop / Tablet 使用 Reel Text；Phone 以普通 Rich Text 覆写，避免在紧凑触控导航中引入 hover reel。不要在 Reel Text 内复制这些外部断点。
- 一旦 Label 可能换行，停止：先缩短导航文案，或另建完整的多行 Component / Variant 并重测窗口、行高、轨道与所有状态。
- 组件没有独立 Press state；点击 / Focus 保留给外部 Navigation 或链接容器。检查键盘焦点、链接目的地和父级触发器没有被内层链接覆盖。

## Text Reel：当前实例映射（已验证示例）

| 位置 | Variant | Label | Link |
|---|---|---|---|
| Navbar links（Desktop / Tablet） | `Button` | Menu / About / Reserve / Chefs | `/menu` / `/about` / `/reserve` / `/chefs` |
| Navbar menu trigger（Desktop / Tablet） | `Button` | Menu | Parent button owns interaction |
| Navbar（Phone / Phone Open） | 普通 `Type/Button` Rich Text | Menu；Open 状态为 Close；Menu / About / Reserve / Chefs | 既有 parent links / trigger own interaction |
| Footer links（Desktop / Tablet） | `Body` | Home / Menu / About / Chefs / Reserve | `/` / `/menu` / `/about` / `/chefs` / `/reserve` |
| Footer links（Phone） | 普通 `Type/Body` Rich Text | Home / Menu / About / Chefs / Reserve | `/` / `/menu` / `/about` / `/chefs` / `/reserve` |
| Footer brand | `League Gothic` | AURELIA | `/#top` |

## Text Reel：验证清单

- [ ] Component controls 显示 `Variant`、`Label` 和 `Link`；三个 Track 文字均绑定 Label 与 Link。
- [ ] 默认与 Hover 都只显示一行；Track 的 default / hover `bottom` 符合所选字体 Variant。
- [ ] 改为较短与较长的**单行** Label 时，Helper 驱动实例宽度，父边界不产生固定宽度残留。
- [ ] Navbar Desktop / Tablet / Phone / Phone Open 保持现有排列；Phone Open 的 label 为 `Close`。
- [ ] Footer Desktop / Tablet / Phone 依次保留五条导航与正确路由。
- [ ] Pointer、键盘 Focus 和实际点击均到达正确页面；不要只看文字显示。
- [ ] 若 Framer linter 标记 clipped Track 或 text edge，先以实际截图检查 first / hover visible row；这是有意使用裁切窗口的模式，不要为了清除该类提示移除 clip。

## Text Reel：已知限制与修复路径

| 现象 | 原因 | 修复 |
|---|---|---|
| 文本改长后超出或换行 | 此模式只为单行和固定窗口设计 | 缩短 Label；若业务必须两行，另建多行 Variant 并重算全部 geometry |
| 新实例点击跳回旧页面 | 某个 Track row 未绑定 `Link` Property | 在每个字体 / Hover state 逐行回读 link binding，统一绑定 Link Property |
| Body 视觉间隔过大 | 继承 `Type/Body` 的 line box | 保持记录的 inline `1em` line-height 与 `13px` clipped viewport，并在 Canvas 截图复核 |
| Phone Open 显示 Menu 而非 Close | 只替换了 Primary 标签，未保留 replica override | 在 Phone Open 的触发器实例上覆写 `Label: Close` |

## Text Reel：精确验证证据

2026-08-16 live readback：`Reel Text` 的 `Label` 与新增 `Link` controls 已存在；其 League / Button / Body 与三个 native Hover state 的 Track 均使用同一 Label，所有 Track rows 都绑定 `Link`。Navigation 的四个链接实例为 Button font variant，保留 `/menu`、`/about`、`/reserve`、`/chefs`；Footer 的五个链接实例为 Body font variant，保留 `/`、`/menu`、`/about`、`/chefs`、`/reserve`。Footer brand 的 Link 为 `/#top`。该次 readback 同时确认 Phone Open 的 menu trigger Label override 为 `Close`。后续同日回读确认当前 `Type/Button` 是 `10px / 600 / 0.02em / 1em`，Button default / Hover 的 Helper 与全部三行 Track 已同步为该值；`10px` viewport、`30px` 三行 Track 与 `-20px → 0px` 位移不变。

## Button Arrow Reel：何时使用 / 不使用

适合：主 CTA 或次级 CTA 已有稳定 Button Component，并希望在 Desktop pointer Hover 时让箭头连续向右通过一个固定窗口。它可与独立的内部 filler 同时使用，但不能改变 Button 的外部尺寸、Label 基线、Link 责任或可点击边界。

不适合：Navbar、Footer 的密集链接、只有单一箭头但没有循环替身的图标、Phone 必须理解的行动提示，或会在 Hover 时改变 CTA 文字换行的 Button。Phone 可保留静态箭头；功能和目的不得依赖 Hover。

## Button Arrow Reel：Submit Roofing 已验证结构

```text
Controls/Button Component
├── Properties: Label (string), Destination (link)
├── Primary / Secondary
│   ├── Filler (absolute; independent surface effect)
│   ├── Label (relative, z-index 2)
│   └── Arrow Viewport (18×18, relative, overflow clip)
│       └── Arrow Track (absolute horizontal Stack)
│           ├── Arrow Right #1 (18×18)
│           └── Arrow Right #2 (18×18)
└── Primary Hover / Secondary Hover (native Hover gestures)
    └── inherit the same tree; only Filler and Arrow Track geometry change
```

| Owner | Responsibility | Verified Submit Roofing evidence, 2026-10-02 |
|---|---|---|
| `Controls/Button` Component | `Label` and `Destination` Properties; Button surface, link, padding, fixed hit-area logic and gesture states | `Label` is a string Property; `Destination` is a Link Property; Primary / Secondary and paired native Hover states exist. |
| Arrow Viewport | Stable 18×18 visible window in normal Button flow | Relative horizontal Stack, `overflow: clip`, width and height `18px`. |
| Arrow Track | Continuous horizontal movement, outside Button sizing | Absolute horizontal Stack with two `Arrow Right` icons, `30px` gap. |
| Base states | Starting reel position | Track `left: -48px`; both arrows remain 18×18. |
| Hover states | Complete the reel without reflow | Track `left: 0px`; native Hover state; current filler uses `spring-physics 250 30 1 0s`. |
| Page instance | Select Button Variant and supply content / route | Representative Navbar instance uses `Primary`, `Label: Get a Quote`, `Destination: /contact`; it does not own internal reel geometry. |

The two-arrow Track is essential. The first arrow leaves the 18px window as the second enters; a single icon would leave an empty frame and read as a translation rather than a reel.

## Button Arrow Reel：implementation and repair order

1. Reuse the existing Button Component and its paired Hover state. Do not create a page-local arrow animation or a second Button Component.
2. Add a relative, clipped 18×18 Arrow Viewport after the Label in the Button's normal horizontal Stack.
3. Add an absolute horizontal Track with two identical arrows. The Track must not participate in Button width or gap calculation.
4. In the base state, position the Track so one arrow is visible; in Hover, shift the same Track to reveal the duplicate. Preserve Button padding, root size, Label position, Link Property and Icon dimensions.
5. Use the same color as the visible Button state for both arrow copies. When the Button also uses a filler, keep the Label and arrows above it with an explicit z-index.
6. Read back Default and Hover geometry, then test one Primary and one Secondary instance in Desktop Preview. Test a longer single-line Label before accepting the pattern.

## Button Arrow Reel：responsive, accessibility and validation

- This is a pointer-only refinement. Touch users must still see a stable arrow and receive the same link destination without Hover.
- Keep the Button's native `button` semantics, accessible label and `Destination` Link Property on the outer Button surface. The Arrow Track must not become a separate link or intercept the primary action.
- Verify at Desktop and Tablet pointer widths that the Button's outer width and height do not change, and at Phone that the static Button remains legible and tappable.
- If a parent clips the Button itself, repair that parent’s sizing first. Do not solve it by making the Button or Arrow Viewport `overflow: visible`.

| Symptom | Cause | Repair |
|---|---|---|
| Arrow disappears or is cut in half | Viewport or Button root lost `overflow: clip`, or Track no longer has two copies | Restore the 18×18 clipped viewport and two-arrow Track. |
| Button jumps wider on Hover | Track is in normal flow or its width affects layout | Make the Track absolute; preserve the Viewport's fixed 18×18 size. |
| Arrow color conflicts with the filler | Arrow lacks explicit color / stacking order | Use state-appropriate arrow color and keep Label / Arrow above the filler. |
| Phone looks inert | Pointer-only effect was treated as essential feedback | Keep a visible static arrow and validate the tap route independently. |

## Button Arrow Reel：evidence limit

2026-10-02 live structural readback verified the native Component tree, Properties, paired Hover states, clip ownership, two `18px` Arrow Right icons, `30px` Track gap, default `left: -48px`, Hover `left: 0px`, and the representative Primary Navbar instance route. No pointer Preview was captured in this documentation pass; motion feel and long-label behavior remain Preview verification requirements rather than claimed visual proof.
