# Framer 高级组件：AURELIA Reel Text

> 状态：**Reference，project-derived**。  
> Provenance：AURELIA `Reel Text` native Component，live Canvas definition、shared Navigation / Footer instances 与一次组件截图回读，2026-08-16。  
> 范围：短、单行、可编辑的品牌名或导航标签在 Hover 时向上滚动；不是长文案、自动换行文字或多项内容列表的通用方案。

## 何时使用 / 不使用

适合：一个短 Label 需要在不改变外部布局宽度的情况下，显示同一文字的纵向 reel；例如 AURELIA Footer 的品牌名、Navbar 的 `Menu / About / Reserve / Chefs` 和 Footer 的五个站点链接。

不适合：可能换成两行的正文、可变数量列表、需要逐项状态的 selector，或需在 Desktop / Tablet / Phone 之间改变文本换行策略的内容。遇到这些需求时，改用相应的独立文字窗口 / reel（例如 Dish Selector），不要强行复用本组件。

## 已验证的责任划分

| 层级 | 责任 | 当前证据 |
|---|---|---|
| `Reel Text` Component | 文字重复、裁切窗口、Hover 位移、字体 geometry 与可编辑 Property | 原生 Component 定义 |
| `Label` Property | 一次编辑，绑定 Helper 与三行 Track 文字 | `AURELIA` 默认值；每个可见文字为同一变量 |
| `Link` Property | 绑定每一个 Track 文字的链接；实例可安全用于不同页面路由 | Navbar / Footer 实例各自拥有 `/`、`/menu`、`/about`、`/chefs`、`/reserve` |
| 父 Navigation / Footer Component | 放置、已有点击 / link 容器、Desktop / Tablet / Phone 组合 | 原有 shared components 保持负责外部响应与 Phone Open 状态 |
| 实例 | 文案、目标路由与字体 Variant | Desktop / Tablet Navbar 使用 `Button`；Desktop / Tablet Footer nav 使用 `Body`；Phone 保持普通 Rich Text；Footer brand 使用 `League Gothic` |

## 当前组件树

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

## 字体 Variant 与坐标合同

所有 Track 都是三行、`gap: 0px`。默认态显示第一行；Hover 态将 Track 移到 `bottom: 0px`，显示第三行。

| Variant | 字体来源 / 当前值 | 窗口与单行高度 | 默认 Track | Hover Track | 用途 |
|---|---|---:|---:|---:|---|
| `League Gothic` | League Gothic 400 / `100px` / `1.2em` | `80px` | `bottom: -160px` | `0px` | 品牌名 |
| `Button` | Inter 600 / `10px` / `1em` / `0.02em`（与当前 `Type/Button` 一致） | `10px` | `bottom: -20px` | `0px` | Navbar 与紧凑按钮标签 |
| `Body` | Inter 400 / `17px` / `1em` / `-0.012em` | `13px`; Track 当前总高 `53px` | `bottom: -40px` | `0px` | Footer 导航 |

`Body` 当前使用 inline font values，而不是 `Type/Body` preset：该 preset 的 line box 会使此固定高度 reel 留出过大的视觉间距。这个例外只适用于这条可裁切的单行轨道，不是放弃现有 Text Style 的通用许可。

## 实现与替换顺序

1. 先确认内容是短单行文字，选择现有 `Reel Text`，不要创建新副本。
2. 选定 `League Gothic`、`Button` 或 `Body` font Variant；不要建立每条导航内容的 Variant。
3. 保持 Helper 与三行 Track 都绑定同一个 `Label` Property；Track 保持 absolute、`gap: 0px`，根保持 clip。
4. 若组件作为链接使用，先把 **所有** Variant / Hover state 的三行文字都绑定 `Link` Property；不得保留某一行的旧 hard-coded route。
5. 替换原标签时，把新 Instance 插回原 parent 和 index，保留 parent 的导航结构；写入正确的 `Label`、`Link` 和 font Variant 后再删除旧 Rich Text。
6. 对 Navigation Phone Open，显式复查触发文字的实例 override：AURELIA 默认 `Menu`，Open 状态为 `Close`。

## Responsive 与状态合同

- `Reel Text` 本身没有 Desktop / Tablet / Phone Variant；字体 Variant 只决定字形和 fixed viewport geometry。
- 外部 shared Navigation 负责 Desktop、Tablet、Phone、Phone Open；Footer 负责 Desktop、Tablet、Phone。当前 AURELIA 仅在 Desktop / Tablet 使用 Reel Text；Phone 以普通 Rich Text 覆写，避免在紧凑触控导航中引入 hover reel。不要在 Reel Text 内复制这些外部断点。
- 一旦 Label 可能换行，停止：先缩短导航文案，或另建完整的多行 Component / Variant 并重测窗口、行高、轨道与所有状态。
- 组件没有独立 Press state；点击 / Focus 保留给外部 Navigation 或链接容器。检查键盘焦点、链接目的地和父级触发器没有被内层链接覆盖。

## 当前实例映射（已验证示例）

| 位置 | Variant | Label | Link |
|---|---|---|---|
| Navbar links（Desktop / Tablet） | `Button` | Menu / About / Reserve / Chefs | `/menu` / `/about` / `/reserve` / `/chefs` |
| Navbar menu trigger（Desktop / Tablet） | `Button` | Menu | Parent button owns interaction |
| Navbar（Phone / Phone Open） | 普通 `Type/Button` Rich Text | Menu；Open 状态为 Close；Menu / About / Reserve / Chefs | 既有 parent links / trigger own interaction |
| Footer links（Desktop / Tablet） | `Body` | Home / Menu / About / Chefs / Reserve | `/` / `/menu` / `/about` / `/chefs` / `/reserve` |
| Footer links（Phone） | 普通 `Type/Body` Rich Text | Home / Menu / About / Chefs / Reserve | `/` / `/menu` / `/about` / `/chefs` / `/reserve` |
| Footer brand | `League Gothic` | AURELIA | `/#top` |

## 验证清单

- [ ] Component controls 显示 `Variant`、`Label` 和 `Link`；三个 Track 文字均绑定 Label 与 Link。
- [ ] 默认与 Hover 都只显示一行；Track 的 default / hover `bottom` 符合所选字体 Variant。
- [ ] 改为较短与较长的**单行** Label 时，Helper 驱动实例宽度，父边界不产生固定宽度残留。
- [ ] Navbar Desktop / Tablet / Phone / Phone Open 保持现有排列；Phone Open 的 label 为 `Close`。
- [ ] Footer Desktop / Tablet / Phone 依次保留五条导航与正确路由。
- [ ] Pointer、键盘 Focus 和实际点击均到达正确页面；不要只看文字显示。
- [ ] 若 Framer linter 标记 clipped Track 或 text edge，先以实际截图检查 first / hover visible row；这是有意使用裁切窗口的模式，不要为了清除该类提示移除 clip。

## 已知限制与修复路径

| 现象 | 原因 | 修复 |
|---|---|---|
| 文本改长后超出或换行 | 此模式只为单行和固定窗口设计 | 缩短 Label；若业务必须两行，另建多行 Variant 并重算全部 geometry |
| 新实例点击跳回旧页面 | 某个 Track row 未绑定 `Link` Property | 在每个字体 / Hover state 逐行回读 link binding，统一绑定 Link Property |
| Body 视觉间隔过大 | 继承 `Type/Body` 的 line box | 保持记录的 inline `1em` line-height 与 `13px` clipped viewport，并在 Canvas 截图复核 |
| Phone Open 显示 Menu 而非 Close | 只替换了 Primary 标签，未保留 replica override | 在 Phone Open 的触发器实例上覆写 `Label: Close` |

## 精确验证证据

2026-08-16 live readback：`Reel Text` 的 `Label` 与新增 `Link` controls 已存在；其 League / Button / Body 与三个 native Hover state 的 Track 均使用同一 Label，所有 Track rows 都绑定 `Link`。Navigation 的四个链接实例为 Button font variant，保留 `/menu`、`/about`、`/reserve`、`/chefs`；Footer 的五个链接实例为 Body font variant，保留 `/`、`/menu`、`/about`、`/chefs`、`/reserve`。Footer brand 的 Link 为 `/#top`。该次 readback 同时确认 Phone Open 的 menu trigger Label override 为 `Close`。后续同日回读确认当前 `Type/Button` 是 `10px / 600 / 0.02em / 1em`，Button default / Hover 的 Helper 与全部三行 Track 已同步为该值；`10px` viewport、`30px` 三行 Track 与 `-20px → 0px` 位移不变。
