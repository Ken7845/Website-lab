# Ken Studio current visual system

Transferred from the previous PROJECT without changing approved values. Repository split: 2026-10-03. [Project entry](./PROJECT.md).

## 6. Typography System

全站字体选择以 2026-07-18 读取到的 `/works` 实际设置为准。

### 6.1 Font Roles

| Role | Font | Use | Rule |
|---|---|---|---|
| Display | Boldonse Regular 400 | 页面主标题、极少数全站级标题 | 每个页面通常只出现一次，不用于长标题、正文或按钮 |
| Structural Display | Inter Display Medium 500 | Section 标题、lead statement、作品名称、档案标签 | 负责秩序和清晰度，是全站主要结构字体 |
| Reading Voice | Libre Baskerville Regular / Italic 400 | 观察文字、短注释、反思性段落 | 只作为安静的第二声部，不装饰性滥用 |
| Functional Body | Inter Regular / Medium 400-500 | 正文、说明、导航、状态和交互信息 | 保持中性、直接、易读 |

BDO Grotesk 当前存在于项目字体列表，但不加入核心四角色。除非在现有组件中有明确品牌用途，否则后续不新增使用范围。

### 6.2 Canonical Type Scale

| Text Style | Desktop 1200+ | Tablet 810 | Phone 390 | Font / Treatment |
|---|---:|---:|---:|---|
| Display / Page Title | 103 px | 80 px | 68 px | Boldonse 400, line-height 1.1 / 1.1 / 1.3, tracking 0 |
| Heading / Section | 60 px | 48 px | 36 px | Inter Display 500, line-height 1.18, tracking -0.04em |
| Display / Archive Title | 58 px | 48 px | 38 px | Inter Display 500, line-height 1.05, tracking -0.04em |
| Body / Lead | 30 px | 26 px | 22 px | Inter Display 500, line-height 1.18, tracking -0.02em |
| Body / Reading | 20 px | 15 px | 14 px | Libre Baskerville 400, line-height 1.55 |
| Body / Functional | 16-18 px | 16-17 px | 15-16 px | Inter 500, line-height 1.35 |
| Archive / Row Title | 20 px target | 18-20 px target | 16-20 px by variant | Inter Display 500, line-height 1.18, tracking -0.02em |
| Meta / Primary | 12-13 px | 12-13 px | 11-13 px | Inter Display 500, line-height 1.2, tracking 0.06-0.14em |

The values above are canonical starting values, not permission to scale every page mechanically. Copy length, image proportion and viewport fit must be checked together.

### 6.3 Typography Rules

- Boldonse 建立页面身份，不承担密集信息。
- Inter Display 连接 Home、Works、作品详情页和全站导航结构。
- Libre Baskerville 只用于真实观察、注释和反思，不用于营销式副标题。
- 正文理想宽度为 55-65 characters；Phone 使用填充宽度并控制自然换行。
- 大标题保持左对齐，不通过居中制造默认 Hero。
- 同一语义层级在不同页面使用同一字体角色、字重和接近的 line-height。
- 小标签允许 uppercase，但必须具有真实档案意义；letter-spacing 保持在 0.06-0.14em。
- 数字、年份和状态保持固定列或稳定宽度，避免与标题碰撞。
- Serif italic 必须检查 descender 和行框，不能出现裁切。
- 新建 Framer Text Styles 时使用语义命名，不保留一次性字号作为系统默认。
- HTML 语义与视觉 Text Style 分开判断：只有内容关系确实是页面主标题、章节标题或正文时才使用 h1/h2/h3/p；不能为了通过语义检查机械套用标签。若预设字号造成重叠、裁切或不合理换行，保留正确内容层级，并改用合适的现有视觉 Style 或局部响应式数值。

Recommended Framer Text Styles:

```text
Display / Page Title
Display / Archive Title
Heading / Section
Body / Lead
Body / Reading
Body / Functional
Meta / Primary
Meta / Secondary
Archive / Row Title
Link / Editorial
```

## 7. Layout and Spacing System

### 7.1 Works-derived Page Rhythm

Current `/works` reference values:

| Area | Desktop | Tablet | Phone |
|---|---|---|---|
| Introduction horizontal padding | 44 px | 32 px | 18 px |
| Introduction top padding | 117 px | 128 px | 104 px |
| Introduction bottom padding | 159 px | 160 px | 129 px |
| Introduction internal gap | 56 px | 44 px | 36 px |
| Archive horizontal padding | 44 px | 32 px | 14 px |
| Archive top padding | 96 px | 72 px | 56 px |
| Folder body padding | 34 px | 28 px | 16 px |
| Folder body gap | 34 px | 28 px | 22 px |
| Folder tab height | 52 px | 52 px | 44 px |

### 7.2 Global Layout Rules

- 全站以左对齐和稳定内容边缘为主，标题、正文与图片边界需要建立可读的共同轴线。
- Desktop 和 Tablet 可以使用非对称双列；Phone 重组为清晰单列，不直接压缩 Desktop。
- 每个 Section 先确定目的，再决定布局。相邻 Section 不重复同一种模板构图。
- Section 的水平 padding 优先复用 Works 的 44 / 32 / 18 体系；特殊全宽图像可以突破，但必须有明确理由。
- 大段落与 heading 共用内容宽度；不使用悬空的右上角解释文字。
- 结构间距使用可复用节奏：14 / 18 / 22 / 28 / 34 / 44 / 56 / 72 / 96 / 128 / 160。
- 可见容器内文字必须有水平 padding；交互目标 Phone 最小高度 44 px。
- 使用 Stack、Grid、Components、Variants 和 Breakpoints；不依赖绝对定位修补正常文档流。
- 图片保持自身比例。仅在构图含义允许时使用 crop，并逐断点确认焦点。

## 8. Color and Surface System

Canonical colors derived from Works:

| Token | Value | Use |
|---|---|---|
| Background / Base | `#111111` | 全站主背景 |
| Surface / Observation | `#1D1D1D` | Observation 档案表面 |
| Surface / Creation | `#2B2926` | Creation 档案表面 |
| Text / Primary | `rgba(255,255,255,0.94-1)` | 标题和主要内容 |
| Text / Secondary | `rgba(255,255,255,0.78-0.90)` | lead、正文、交互文字 |
| Text / Muted | `rgba(255,255,255,0.48-0.60)` | 注释、元数据、状态 |
| Accent / Observation | `#BD2222` | Observation 标签和必要状态 |
| Accent / Creation | `#FCE351` | Creation 标签和必要状态 |
| Divider / Quiet | `rgba(255,255,255,0.12)` | 档案行和结构分隔 |

Rules:

- 页面保持一个深色主题，不在 Section 之间切换成浅色纸张主题。
- 红色和黄色是档案分类信号，不扩散成通用装饰色。
- 文字透明度必须通过实际背景上的 WCAG AA 检查。
- 表面层级依靠相邻深色差、边界和叠放表达，不使用厚重阴影。
- Radius 保持接近 sharp，默认 0-4 px；按钮若沿用现有组件，需遵循组件自身一致规则。
