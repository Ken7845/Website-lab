# Ken Studio Personal Site

## 1. Project Identity

- Project name: Ken Studio Personal Site
- Platform: Framer
- Project type: Personal Portfolio / Visual Archive
- Status: Building
- Framer project URL: https://framer.com/projects/Ken-Studio--W2l0ZO8Ar0mErx3GOD0d-cr6l9
- Framer project ID: `W2l0ZO8Ar0mErx3GOD0d`
- Demo URL: Missing
- Content status: Mixed
- Last updated: 2026-07-30

## 2. Design Read

Reading this as: 一个面向视觉敏感型访客的个人视觉档案。摄影记录外部世界如何被观看；抽象曼陀罗记录注意力如何向内凝结为中心、节奏与结构；网站实践则把这种结构意识转化为可使用的空间。全站以安静、观察性、图像主导的编辑语言呈现，并以当前 `/works` 页的字体层级和排版节奏作为基准。

Design dials:

- `DESIGN_VARIANCE: 7` - 保留非对称构图和档案感，但不牺牲阅读顺序。
- `MOTION_INTENSITY: 5` - 动效用于层级、预览和状态变化，不成为页面主角。
- `VISUAL_DENSITY: 4` - 图像保有呼吸空间，元数据保持紧凑而清晰。

Project mode: targeted evolution。保留现有 Home、路由、品牌语言和已成立的 Works 结构，逐页统一排版与系统，不进行无授权的全站重设计。

## 3. Website Goal

- 网站为谁服务：对摄影、视觉叙事、网页设计和个人观察感兴趣的访客，以及希望理解 Ken 工作方式的潜在合作对象。
- 用户进入网站后需要理解什么：Observation 和 Creation 来自同一种注意力。摄影不是绘画的题材来源，而是训练观看的外部实践；抽象绘画把注意力向内转化为中心、节奏和结构；网站设计进一步把结构变成可以进入和使用的体验。
- 网站最重要的实际结果：让访客自然进入作品档案、完整观看独立作品，并在 Home、Works、Musings 与 About 之间形成连续体验。
- 主要 CTA：Browse Works
- 次要 CTA：Read Musings / About Ken

Home 负责建立氛围和提供入口，不承担完整作品归档。Works 是全部作品的总入口。

## 4. Target User

- Primary audience: 视觉文化、摄影、独立设计和个人创作领域的访客。
- User intent: 快速理解网站气质，浏览作品类别，进入某一作品并完整观看。
- Important questions:
  - Ken 在观察什么？
  - Observation 与 Creation 有什么关系？
  - 每个作品包含哪些真实图片、过程和文字？
  - 如何继续浏览同类作品？
- Trust requirements: 使用真实作品、真实项目状态和已确认路由，不编造客户、成果、奖项、日期或角色。
- Device priority: Balanced。Desktop 提供完整档案空间，Phone 必须拥有同等可访问的内容和独立交互方案。

## 5. Brand Direction

- Brand personality: Quiet, observant, personal, image-led.
- Core concept: A living visual archive. Observation records how Ken looks; Creation records how attention becomes core, rhythm, form and usable structure.
- Visual memory point: 深色背景上的大号安静标题、紧凑档案标签、两层 Works 文件夹，以及 Home 中 Core → DOC → DOMT 的生成式滚动段落。
- Typography direction: 以 `/works` 当前排版为全站基准，采用四个清晰字体角色，不增加第五种字体性格。
- Color direction: 近黑背景、柔和白色文字、深色中性表面，以及克制的红色和黄色档案标签。
- Image strategy: 真实作品优先；完整性重要时按原始比例展示，不为数学整齐强行裁切。
- Motion character: Smooth, restrained, spatial. 动效只服务层级、叙事、反馈或状态变化。
- Avoid:
  - 营销型作品集语气
  - 通用三卡片布局
  - 纸张纹理、胶带、图钉、邮戳等仿真实体档案道具
  - 每个 Section 都使用 eyebrow 或编号装饰
  - 过多字体、主题反转、发光渐变和无目的循环动效
  - 在未确认前创建新路由、事实或项目成果

资料链接：

- [Brand Voice](BRAND_VOICE.md)
- [Goal](GOAL.md)
- [Hero Content](hero-section.md)

当前没有独立 `STYLE-GUIDE.md` 或 Works Archive Implementation Plan。字体、颜色、布局和实现状态以本文件为准，不引用已删除的旧文件。

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

## 9. Content Facts and Boundaries

| Fact | Value / Source | Status |
|---|---|---|
| Site title | Ken's Gallery / Ken Studio, naming relationship to resolve | Mixed |
| Hero title | Ken's Gallery | Approved source |
| Hero subtitle | `hero-section.md` | Approved source |
| Works hierarchy | Works > Observation / Creation | Approved |
| Observation records | Fighting the Chemistry, Campus, Golden Moment, Shadow; Sanctuary pending cover source | Sanctuary1 asset not found locally or in the indexed project sources |
| Fighting the Chemistry route | `/fighting-the-chemistry` | Confirmed |
| Golden Moment route | `/golden-moment` | Confirmed |
| Campus route | Missing | Do not invent |
| Shadow route | Missing | Do not invent |
| Creation category route | `/creations` | Draft |
| Creation website covers | Dutch Treat Restaurant; Morrow & Grain Bakehouse | Confirmed on Home; detail routes still missing |
| Contact details | Missing | Do not invent |
| Social links | Missing | Do not invent |
| Copyright text | Missing | Do not invent |

`content-library/ken-studio` is the source of truth. New visible copy must follow `BRAND_VOICE.md` and be reviewed before publishing.

## 10. Sitemap and Page Goals

| Page | Path | User goal | Primary action | Content source | Status |
|---|---|---|---|---|---|
| Home | `/` | 感受网站气质并进入主要内容 | Browse Works | Hero, Works, Musings, About content | Building |
| Works | `/works` | 理解 Observation 与 Creation 并选择作品 | Open a work | GOAL + Works plan | Building |
| Observation category | `/observations` | 浏览摄影类别 | Open a series | Observation content | Existing, role to confirm |
| Fighting the Chemistry | `/fighting-the-chemistry` | 完整观看独立摄影作品 | Next Observation | Content missing | Existing; page layers renamed and H1/Lead typography normalized, content/alt audit still incomplete |
| Golden Moment | `/golden-moment` | 完整观看独立摄影作品 | Next Observation | `works/golden-moment.md` | Existing |
| Campus | Missing | 完整观看独立摄影作品 | Next Observation | Images only | Blocked |
| Shadow | Missing | 完整观看独立摄影作品 | Next Observation | Images only | Blocked |
| Creation category | `/creations` | 浏览网站设计作品 | Open a project | Creation content | Draft |
| About | `/about` | 理解 Ken 的观察与创作背景 | Return to Works / contact if confirmed | Missing formal content | Existing, content audit needed |
| Musings | Missing or embedded | 阅读观察、实验和短文 | Open a musing | Missing content model | Planning |

不静默改名或删除任何现有 route。新增 Campus、Shadow、Creation detail 和 Musings 路由前必须确认。

## 11. Section Plan

| Page | Section | Purpose | Content | Component / Pattern | Status |
|---|---|---|---|---|---|
| Home | Hero | 建立安静的图像氛围 | Approved hero title, subtitle, background | Image-led Hero | Existing; semantic Styles applied and Phone navigation safe area verified |
| Home | Observation Sequence | 以摄影建立外部观看与注意力 | Selected real photography | Editorial image sequence | Existing user-built content; representative three-breakpoint screenshots verified |
| Home | Observation → Creation Bridge | 把摄影与抽象绘画连接在“注意力如何生成结构”上，而不是建立直接题材对应 | Current user-authored bridge copy | Quiet transition / scroll threshold | Existing user-built structure; representative three-breakpoint screenshots verified |
| Home | Creation Reveal | 从外部观察转向内部中心、象征和形式 | Current user-built reveal using real painting assets | User-authored sticky / scroll-target structure | Preserved; ordinary Frame/Stack names shortened, all Scroll Target names still exactly match `elementId`; Tablet base geometry fixed; interactive scroll QA pending |
| Home | Painting Continuum | 在 reveal 之后继续展示抽象曼陀罗创作 | Doctrine of the Mean Is the Truth, The Birth of the Sun, Depth | Alternating editorial artwork rows | Copy, semantic Styles, alt text and Desktop / Tablet / Phone compositions implemented and screenshot-verified |
| Home | Website Practice | 将绘画中的结构意识过渡到网站设计，并保留真实商业入口 | Dutch Treat Restaurant; Morrow & Grain Bakehouse | Quiet H2/P transition followed by alternating equal-size covers | Implemented on Desktop / Tablet / Phone; links and detail routes pending |
| Home | Works Entry | 在叙事成立之后进入完整档案 | Observation / Creation archive | Works Entry | Existing, reposition pending |
| Home | Musings | 引导进入文字和观察 | Real approved excerpts | Editorial list / selected entry | Content missing |
| Home | About | 提供简短背景和 About 入口 | Approved bio needed | Quiet text-image composition | Content missing |
| Works | Introduction | 解释两种实践的关系 | Current Works statement | Works canonical typography | Existing |
| Works | Observation Folder | 浏览摄影作品 | Fighting the Chemistry, Campus, Golden Moment, Shadow; Sanctuary pending `Sanctuary1` source | Sticky Archive Folder | Existing four rows use one `ArchiveOptionRow` template; Sanctuary is asset-blocked |
| Works | Creation Folder | 浏览绘画与网站实践 | Inner Form: Doctrine of the Mean Is the Truth, Ken, Pure, The Birth of the Sun, Depth; Digital Form: Morrow & Grain Demo | Sticky Archive Folder | Six template instances implemented; Ken and Pure rows exist, but their real cursor images remain upload-blocked |
| Observation Detail | Header | 建立作品标题、时间与开场注释 | Per-record content | Observation Header | Partial |
| Observation Detail | Image Sequence | 以图像节奏完整呈现作品 | Ordered real images | Responsive image sequence | Partial |
| Observation Detail | Next Record | 延续同类浏览 | Confirmed next route | Next Record | Planning |
| Creation Detail | Header / Context | 说明真实项目背景与角色 | Confirmed facts | Creation Header | Planning |
| Creation Detail | Decision / Gallery | 展示关键设计判断和真实页面 | Screenshots and writing | Authored case record | Planning |
| Creation Detail | Reflection / Next | 保留过程中的不确定性并继续浏览 | Approved reflection | Next Record | Planning |

## 12. Conversion Paths

Primary archive path:

```text
Home
-> Works entry
-> /works
-> Observation or Creation record
-> Detail page
-> Next record
```

Secondary reading path:

```text
Home
-> Musings
-> Individual musing
-> Related work when a real relationship exists
```

Contact path remains blocked until real contact details and intended CTA are confirmed.

## 13. System Plan

### Shared Components

- Navbar: preserve current navigation labels and routes; align typography to Meta / Primary or Body / Functional.
- Footer: shared native component. All three variants use the same left-wordmark / right-navigation composition; links are Home, Browse Works, About and Observations.
- SectionTitle: shared native component for the repeated Eyebrow + H2 + Reading description group. Content differences use Image/Text-style component properties, not visual variants.
- ArtworkEntry: currently blocked as a shared component while the painting image and copy retain separate page-scoped `onScrollTarget` targets. Do not replace the live rows until Framer can preserve those two targets per instance.
- CTA Button: keep one label per intent; no duplicate contact or portfolio CTA wording.
- Works Entry: Observation and Creation variants.
- Archive Folder: Observation and Creation variants with shared structural logic.
- ArchiveOptionRow: one shared template with only Desktop and Phone structural variants. Project Title, Meta, Number, Project Link and Base Fill are instance properties; per-record Hover Effect and Cursor Preview are set on the page instance.
- Observation Header / Creation Header: separate when content structures differ.
- Next Record: Observation and Creation variants.
- Image Caption: optional and factual only.

### CMS Decision

- CMS required: Later, after content readiness.
- Proposed collections: Observation Series and Creation Projects.
- Reason: 两类记录拥有不同字段和叙事结构，不应强制套用一个万能模板。
- Current rule: 固定内容数量可以继续使用 native components and variants。只有在新增 CMS 项目必须自动驱动共享预览时，才评估 Code Component。

## 14. Responsive Plan

| Area | Desktop | Tablet | Phone |
|---|---|---|---|
| Navbar | Single line, max 80 px height | Condensed but readable | Menu or compact native pattern, core navigation always reachable |
| Page title | Boldonse 103 px reference | 80 px | 68 px, verify no collision or clipping |
| Lead statement | 64% width, 30 px | 62% width, 26 px | Full width, 22 px |
| Intro composition | Horizontal statement row | Horizontal with reduced widths | Vertical stack, 24 px internal gap |
| Page horizontal padding | 44 px | 32 px | 18 px baseline; archive may use 14 px |
| Archive folder | Two sticky dark layers | Reduced offsets and body size | One-column disclosure; release sticky if it clips or traps scroll |
| Folder tab | 300 x 52 px | 260 x 52 px | 170 x 44 px reference |
| Project rows | Horizontal title / meta / status | Horizontal, allow metadata reflow | Number + title first line, status second line, min 44 px target |
| Image sequences | Asymmetric, preserve ratios | Reduced asymmetry | Single column with intentional crop decisions |
| Creation reveal | Preserve user-authored Desktop geometry | 810 px base image and clipped 760 px stage; keep existing targets | Preserve current full-bleed reveal; verify interactive scale and release independently |
| Painting Continuum | Alternating image / copy rows, 44 px page padding | Alternating image / copy rows, 32 px page padding | Single-column image → title → reflection, 18 px page padding |
| Website Practice | H2/P transition; 46.217% × 360 px covers, left/right alternating | H2/P transition; 54% × 282 px covers, left/right alternating | H2/P transition; 100% × 248 px covers, vertical sequence |
| Footer | Left wordmark / right navigation | Same paired layout with reduced padding | Same paired layout; verify no collision at 320-390 px |

Test widths: 320 / 375 / 390 / 768 / 810 / 1024 / 1200 / 1280 / 1440+.

## 15. Motion and Interaction Plan

- Page / section enter: title first, lead 60-100 ms later, first image 80-140 ms after lead when present.
- Motion properties: animate opacity and transform only; do not animate sticky top, height or layout dimensions.
- Navbar behavior: preserve current behavior until audited; no new scroll listener or decorative movement.
- Links and rows: contrast, text weight or one restrained divider change. No outer-card scaling.
- Works sticky archive: native sticky geometry. Creation sits above Observation body while both tabs remain legible.
- Works pointer preview: current project uses one native Framer custom cursor component for Observation and Creation rows. Each artwork/project preview is a cursor-content variant, while the archive row itself remains a two-variant structural template. Preserve this as a Works-specific pointer-device signature; do not make it the global site cursor.
- Touch fallback: first tap expands inline preview, explicit `Open project` link navigates, one row open at a time.
- Keyboard: focus must reveal the same useful information as hover; Enter activates the confirmed route.
- Reduced Motion: remove image scale and spatial reveal; use static content or short opacity changes.
- No automatic continued-scroll navigation between routes.
- Website Practice adds no Scroll Target or entrance effect. Its Background / Base
  fill and foreground stacking isolate the new chapter from the preceding enlarged
  painting without changing the reveal's targets, timing or geometry.
- Painting Continuum currently keeps each Image and Copy node in the Home page scope.
  Their independent `onScrollTarget` targets cannot be moved into a shared canvas
  component without Framer rejecting the external target references. Preserve the
  page-scoped rows until an instance-safe target control exists.

### 15.1 Home Creation Reveal — Current User-Built Structure

The previous agent-authored Core → DOC → DOMT implementation was rejected and fully withdrawn. The current reveal visible on the Home canvas was built manually by the user and must be preserved as the implementation source.

Narrative role:

```text
External observation
→ attention turns inward
→ a centre appears
→ opposites gather around it
→ language follows the image
→ the wider painting practice opens
```

Current structural read:

```text
Creation Reveal Stage
├── Doctrine Base Layer
├── Core Focus Layer
├── Core Mask / Anchor
└── Effect-linked Scroll Targets and Release Track
```

Rules:

- Do not recreate the rejected agent sequence or reapply its old timing table.
- Preserve the current user-built Desktop composition and its scroll relationships.
- Every Frame with Scroll Target enabled must use its exact `elementId` as its
  layer name, including case and numbering (for example `core-fade-in`,
  `painting-fade-in2` and `doC`). Do not replace these names with longer semantic
  labels; nearby non-target wrapper frames may carry the descriptive hierarchy.
- Tablet and Phone require independent geometry. Desktop widths and offsets cannot be copied directly.
- Motion remains restrained and symbolic. It should feel like an inward encounter, not a product animation.
- Reduced Motion should retain the final image and real text without depending on scale or scroll timing.
- The relationship between photography and painting is attention, not literal subject translation.

## 16. Assets

- Source folder: `content-library/ken-studio/images`
- Hero asset: `images/herosection-background.jpg`
- Observation assets:
  - `images/works/fighting-the-chemistry`
  - `images/works/campus`
  - `images/works/golden-moment`
  - `images/works/shadow`
- Creation painting assets: `images/Paintings/Webp`
  - `Core.webp` — 1778 × 1844, transparent, approximately 179 KB.
  - `Doctrine of the mean.webp` — 4644 × 3253, transparent, approximately 494 KB. Internal shorthand: DOC.
  - `Doctrine of the mean is the truth.webp` — 4644 × 3253, opaque, approximately 587 KB. Internal shorthand: DOMT.
  - Additional confirmed painting files currently include `Depth.webp`, `E.webp`, `Pure.webp`, and `the birth of the sun.webp`.
- Creation website cover assets:
  - Dutch Treat Restaurant — uploaded Framer cover reused across all breakpoints.
  - Morrow & Grain Bakehouse — uploaded Framer cover reused across all breakpoints.
  - Canonical case-study copy, links and detail routes remain missing.
- Contact sheet: A temporary review sheet exists at `Framer 2/contact-sheets/ken-studio-paintings-review.jpg`; it is a working artifact, not a source asset.
- Web derivatives: Create from source according to real Framer container sizes; do not overwrite originals.
- Alt text: Added for the two reveal images and the three Painting Continuum artworks; most remaining site assets still require audit.
- License status: User-provided personal work assumed, but publication rights should be confirmed for any third-party website screenshots or external media.

### 16.1 Creation Image Performance Rules

- Use existing WebP outputs; never overwrite the source paintings.
- Upload each artwork once and reuse its uploaded asset across breakpoints.
- Use `fit-image` / contain behavior when completeness matters.
- Do not copy Desktop fixed pixel widths into Tablet or Phone.
- Avoid blur, filter stacks, blend modes and large animated masks on high-resolution layers.
- The seven Painting WebPs total roughly 70MP when decoded. Visual review must use the generated compressed contact sheet rather than opening every original in one turn.
- If Phone Preview shows memory pressure, create non-destructive responsive derivatives in a separate work directory and record the mapping here.

## 17. Definition of Ready

- [x] Website goal and core audience are defined.
- [x] Works hierarchy is approved.
- [x] Works-based typography direction is defined.
- [x] Responsive foundation is defined.
- [x] Brand voice and image-led direction are documented.
- [ ] Site naming relationship between Ken Studio and Ken's Gallery is resolved.
- [ ] Primary and secondary CTA wording is approved.
- [ ] Campus and Shadow routes are confirmed.
- [ ] Fighting the Chemistry copy is approved.
- [ ] Creation project inventory and routes are confirmed.
- [ ] Musings content model and route are confirmed.
- [ ] About copy, contact details, social links and copyright facts are approved.
- [ ] Most image alt text is prepared.

Until these missing items are resolved, structural and visual work may continue, but placeholders and guesses cannot be treated as publish-ready content.

## 18. Build Status Matrix

Legend: `✓` verified or sourced, `◐` existing but requires audit, `□` not complete, `B` blocked by missing content or decision.

| Page | Content | Styles | Components | Links | SEO | Alt | Desktop | Tablet | Phone | Preview |
|---|---|---|---|---|---|---|---|---|---|---|
| Home | ◐ | ✓ current scope | ◐ | ◐ | □ | ◐ | ✓ screenshot | ✓ screenshot | ✓ screenshot | ◐ interactive |
| Works | ◐ | ✓ baseline | ✓ row template | ◐ confirmed routes only | □ | B | ✓ targeted | ✓ targeted | ✓ screenshot | ◐ cursor runtime |
| Fighting the Chemistry | B | ✓ header scope | ◐ | ◐ | □ | B | ✓ screenshot | ✓ screenshot | ✓ structure + prior screenshot | ◐ interaction |
| Golden Moment | ✓ source | ◐ | ◐ | ◐ | □ | B | ◐ | ◐ | ◐ | □ |
| Campus | B | □ | □ | B | □ | B | □ | □ | □ | □ |
| Shadow | B | □ | □ | B | □ | B | □ | □ | □ | □ |
| Creation category | B | ◐ | ◐ | B | □ | B | ◐ | ◐ | ◐ | □ |
| Creation details | B | □ | □ | B | □ | B | □ | □ | □ | □ |
| About | B | ◐ | ◐ | ◐ | □ | B | ◐ | ◐ | ◐ | □ |
| Musings | B | □ | □ | B | □ | B | □ | □ | □ | □ |

This matrix is a planning baseline, not a claim that live Preview QA has passed.

## 19. Decisions and Exceptions

| Decision | Reason | Scope | Date |
|---|---|---|---|
| `/works` typography and spacing become the full-site baseline | It currently expresses the intended quiet archive language most clearly | Website | 2026-07-18 |
| Boldonse is reserved for page-level display titles | Its weight is distinctive but becomes loud and difficult when repeated densely | Website | 2026-07-18 |
| Inter Display carries structural hierarchy | It connects large archive titles, lead statements, rows and metadata without adding another font | Website | 2026-07-18 |
| Libre Baskerville is a restrained reading voice | It supports observation and reflection while remaining secondary to images | Website | 2026-07-18 |
| BDO Grotesk is not part of the core type system yet | No required role is currently established by Works | Website | 2026-07-18 |
| The site remains dark-theme locked | Works and Brand Voice rely on soft white type over near-black surfaces | Website | 2026-07-18 |
| Red and yellow remain category signals | They distinguish Observation and Creation without creating a broad decorative palette | Works and related navigation | 2026-07-18 |
| Current custom cursor is a Works-only exception | It is already the latest project-specific interaction, but must not become a global cursor and requires keyboard, touch and reduced-motion fallbacks | Works, pointer devices only | 2026-07-18 |
| Native Framer patterns remain the default | Components, Variants, Styles, Stacks, Breakpoints and native Effects are more maintainable for the known fixed content | Website | 2026-07-18 |
| No publishing without explicit approval | Routes and formal content remain incomplete | Website | 2026-07-18 |
| Home narrative does not move directly from a generic Hero to a project grid | The site needs to establish how external observation becomes internal form before presenting an archive or service | Home | 2026-07-18 |
| Photography and mandala painting are connected through attention, rhythm and structure | The abstract paintings are not literal depictions of photographed subjects | Home / Observation → Creation bridge | 2026-07-18 |
| Preserve the current user-built Creation reveal | The previous agent implementation was rejected; current canvas geometry and scroll relationships are the implementation source | Home / Creation Reveal | 2026-07-26 |
| DOMT's white field is treated as artwork content | It is an intentional local visual event, not permission to introduce a general paper-themed site skin | Home / Creation Reveal | 2026-07-18 |
| Home Creation no longer opens with the old four-cover website grid | Painting is the primary Creation narrative; website practice should appear later as structure made usable, not as a generic product display | Home / Creation | 2026-07-18 |
| Creation writing may draw from Jung's *The Red Book* as a reference | The paintings were made in dialogue with its mandalas and inner-symbolic language; copy may use restrained mythic and theological imagery without imitation or false quotation | Home / Painting Continuum | 2026-07-26 |
| Creation receives an opaque Background / Base surface | The preceding sticky reveal must not remain visible beneath the introduction and first artwork; the fill establishes a readable content plane without changing the reveal targets | Home / Painting Continuum | 2026-07-26 |
| Creation and Digital Form headings reuse the existing `Heading/Section` H2 preset | The project already has canonical H1, H2 and paragraph roles; section copy must not introduce a parallel display style | Home / Creation | 2026-07-27 |
| Website Practice begins only after the third painting | It preserves the inward-form narrative before translating structure into usable digital space | Home / Website Practice | 2026-07-27 |
| Website covers have no new scroll animation | Appending content must not add or rename reveal targets; a foreground Background / Base surface provides visual separation instead | Home / Website Practice | 2026-07-27 |
| Repeated Creation and Digital Form title groups use the native `SectionTitle` component | Their structure and typography are identical; Eyebrow, Heading and Description are exposed as content properties while existing Meta/H2/P presets remain authoritative | Home / Creation | 2026-07-27 |
| Painting rows remain page-scoped despite the maintenance goal | A hidden component test proved Framer rejects page Scroll Section targets from inside a component and exposes no instance-descendant override path; replacing the rows would remove the independent Image/Copy entrance sequence | Home / Painting Continuum | 2026-07-27 |
| Footer variants share the phone-derived paired layout | One shared Footer now provides a stable left wordmark and right navigation at Desktop, Tablet and Phone; only confirmed non-draft routes are linked | Shared Footer | 2026-07-27 |
| Layer names use the shortest clear expression inside their parent context | Repeating ancestor or Section prefixes makes the tree slower to scan without adding meaning; Scroll Target names remain the exact `elementId` exception | Website | 2026-07-29 |
| `ArchiveOptionRow` is a record-agnostic template | Record content, link, base fill, hover fill and cursor selection belong to page instances; only Desktop and Phone express structural differences | Works | 2026-07-29 |
| Creation keeps Inner Form and Digital Form inside the same folder | Home establishes painting and website practice as two expressions of Creation; five painting rows and one Morrow & Grain Demo row preserve that hierarchy | Works / Creation Folder | 2026-07-29 |
| Fighting the Chemistry keeps its two responsive intro orders | Desktop/Phone remain Title First while Tablet remains Lead First; typography and semantics were normalized without changing the photo sequence or scroll timing | Fighting the Chemistry | 2026-07-29 |
| Tablet intro uses canonical values as a local exception | The inherited Tablet RichText continued rendering the removed `auto-fit` override while reporting a preset binding; direct Boldonse 80 and Inter Display 26 values match the canonical style and prevent runtime clipping | Fighting the Chemistry / Tablet | 2026-07-29 |
| Visual review uses a fixed evidence budget and stop condition | Repeated original-image decoding, CDN download and screenshot retries have repeatedly become a single point of failure; one authoritative evidence chain is enough and visual failure cannot block independent structural work | Website workflow | 2026-07-30 |
| Review depth follows change risk | Naming, copy and property changes use structural readback; layout uses one targeted screenshot; hover/cursor/scroll uses one key interaction; full-page review is reserved for page-level work | Website workflow | 2026-07-30 |
| Semantic tags do not dictate visual size | Correct content hierarchy must be preserved, but a mechanically applied H1/H2/P preset may be replaced by a suitable existing visual style or responsive values when it overlaps, clips or damages the composition | Website | 2026-07-30 |
| `ArchiveOptionRow` uses breakpoint-matched pointer hover states | Desktop and Phone remain structural variants. `Desktop Hover` and the explicitly requested `Phone Hover` both consume the same per-instance Hover Fill; Phone hover serves narrow-screen pointer environments, while touch-only devices still have no hover event | Works | 2026-07-30 |
| Phone Footer separates full-width surface from bounded content | The footer background may fill the Phone breakpoint up to 809 px, but the paired wordmark/navigation layout is capped at 480 px and centered so auto-fit text cannot grow beyond the fixed visual composition | Shared Footer / Phone | 2026-07-30 |
| CTA buttons use padding-driven Fit Content structure | The visible Button Stack owns Border and Padding around Fit Content text; page-level CTA Stacks own Fill width, alignment and Fit height so changed labels resize the boundary without clipping | Home / Observation / Shared CTA | 2026-07-31 |

## 20. Recovery State

- Active Framer session: `1`, connected through the official `@framer/agent` workflow.
- Current project: Ken Studio
- Current pages changed: Home `/`, Works `/works`, and Fighting the Chemistry
  `/fighting-the-chemistry`.
- Last successful action: Replaced the Observation Polaroid Card's old fixed-size
  CTA Button 2 with the user-built padding-driven CTA Button. The card now uses a
  Fill-width / Fit-height CTA Stack, a Fit Link boundary and breakpoint-matched
  Desktop, Tablet and Phone button variants.
- Verified breakpoints from live structure: Desktop 1200, Tablet 810, Phone 390.
- Official visual QA in this task:
  - Framer-generated full-page screenshots completed for Desktop, Tablet and Phone.
  - Creation section screenshots completed independently for all three breakpoints.
  - Tablet reveal screenshot verified after reducing the inherited Desktop image geometry and clipping the 760 px stage.
  - Phone Hero screenshot verified after adding the 64 px top safe area.
  - Interactive Preview scrolling still requires a final hands-on pass.
- Framer canvas changes in this task:
  - Learned the user-built `CTA Button` from its live Home instances: Border and
    Padding belong to a Fit Content Stack around the Content property; page CTA
    Stacks use Fill width and Fit height so the button is not clipped.
  - Replaced the old `CTA Button 2` inside `Polaroid Card` with the shared
    `CTA Button`, preserving `View Collection` and the card's Link variable.
  - Added a Fit Link Stack inside the Fill-width CTA placement Stack so only the
    visible button boundary is clickable, not the surrounding empty row.
  - Applied Desktop, Tablet and Phone button variants to the corresponding
    Polaroid variants; Phone keeps centered placement while larger variants remain
    left aligned.
  - Preserved the current user-built Creation reveal and its existing effect targets.
  - Kept semantic names on ordinary structure and synchronized all 22
    effect-linked Scroll Target Frames to their exact `elementId` values.
  - Created `Display/Page Title`, `Heading/Section`, `Body/Lead`, `Body/Reading`,
    `Body/Reading Italic`, `Meta/Primary` and `Artwork/Title` Text Styles with
    Desktop / Tablet / Phone slots.
  - Set `Artwork/Title` to 30 / 26 / 22 px so artwork names remain clearly above
    their reading copy at all three breakpoints.
  - Added approved Jung / *The Red Book*-influenced titles and reflections for
    Doctrine of the Mean Is the Truth, The Birth of the Sun and Depth.
  - Converted Painting Continuum to alternating Desktop / Tablet rows and
    single-column Phone rows while preserving the original reveal-target frames.
  - Added alt text to the two reveal images and three continuum artworks.
  - Added an opaque Background / Base fill to Creation so the sticky reveal does not
    bleed through the introduction.
  - Fixed Tablet reveal composition by using an 810 × 543 base image, a clipped
    760 px stage and a 560 × 400 document layer.
  - Updated the Creation entry to `CREATION / INNER FORM`, “A centre forms
    within.” and its revised inward-attention subtitle while retaining the existing
    `Heading/Section`, `Meta/Primary` and `Body/Reading` presets.
  - Added `CREATION / DIGITAL FORM`, “The structure leaves the page.” and a
    transitional paragraph after the Painting Continuum.
  - Added Dutch Treat Restaurant and Morrow & Grain Bakehouse covers at matching
    sizes: Desktop 46.217% × 360 px, Tablet 54% × 282 px and Phone 100% × 248 px.
  - Added no Scroll Targets or effects to Website Practice.
  - Renamed the painting container to `Creation / Painting Continuum` and its
    three content rows to `Artwork 01 / Content Row` through `Artwork 03 / Content Row`.
  - Created native `SectionTitle` with Eyebrow, Heading and Description controls;
    replaced the Creation and Digital Form title groups and restored their original
    Desktop / Tablet / Phone widths.
  - Kept the `Meta/Primary`, `Heading/Section` and `Body/Reading` presets inside
    `SectionTitle`; no parallel font styling was introduced.
  - Tested `ArtworkEntry` as a hidden component before replacement. Framer rejected
    both page-scoped Scroll Section targets inside the component, so the test
    instance and component were removed and all three live rows were left unchanged.
  - Re-audited all six painting Image/Copy effect targets and all six Scroll Target
    frames after cleanup; target IDs, transitions, elementIds, widths and heights
    remain unchanged.
  - Updated the existing shared Footer component instead of duplicating it. Desktop,
    Tablet and Phone now use the phone-derived left wordmark / right navigation
    layout with `/`, `/works`, `/about` and `/observations` links.
  - Matched the Phone Footer Variant to the Layout Template instance's real 160 px
    height and reduced only its wordmark/navigation sizing; the final instance
    screenshot shows no top clipping or right-column overflow.
  - Visually checked the three Footer variants and Home Creation node using Framer
    on-demand screenshots and `node_repl.emitImage`, without reading Painting originals.
  - Verified in the live Framer editor that the three breakpoint canvases contain
    the new section after the third painting and that protected layers remain locked.
  - Home naming readback found no unnamed page-local Frame/RichText nodes and no
    Scroll Target whose layer name differs from its `elementId`.
  - Removed 19 record-specific Desktop/Phone/Hover variants and the duplicate
    Status/Title properties from `ArchiveOptionRow`; retained only Desktop and Phone.
  - Added Project Link and Base Fill instance properties to the row template and
    preserved the confirmed Fighting the Chemistry and Golden Moment routes.
  - Added Works Creation groups `Inner Form` and `Digital Form`; their six instances
    use real titles, numbered rows, Creation surface colors, non-scaling Hover Effects
    and matching Cursor Preview variants.
  - Targeted readback verified 18 Creation instances across Desktop, Tablet and Phone,
    with Phone selecting the Phone variant and no missing content/cursor fields.
  - Desktop interaction view and Framer on-demand Phone screenshot show stable rows
    with no horizontal overflow. Sticky-folder overlap warnings remain intentional
    user-authored geometry.
  - Fighting the Chemistry now uses `Content → Introduction → Title First / Lead
    First` and `Photo Sequence`; the four effect targets still retain exact
    `content-appear1` through `content-appear4` names.
  - Desktop and Phone use the canonical `Display/Page Title` and `Body/Lead`
    presets. Tablet retains its Lead First composition with canonical 80 px
    Boldonse and 26 px Inter Display values after clearing a stale `auto-fit`
    breakpoint override.
  - Tablet screenshots were iterated until the H1 and Lead no longer clipped or
    split a word. Phone uses new clean single-block title/lead nodes; old multi-h1
    and clipped Lead replicas are hidden.
  - The final Phone on-demand screenshot was generated by Framer, but its image URL
    failed twice during temporary download. Per image-workflow rules, visual
    retries stopped and the pass was completed with RichText/tag/visibility/width
    readback; a later runtime screenshot remains desirable.
  - Added one shared `Desktop Hover` Gesture Variant to `ArchiveOptionRow`; its fill
    comes from a per-instance Hover Fill property. Removed page-instance hover
    effects and disabled custom cursor on the Phone structural variant.
  - Restored the quiet 1 px bottom divider on the shared Desktop, Phone and hover
    states so Creation rows match Observation rows.
  - Removed the redundant Core and Doctrine of the Mean Creation records. Inner
    Form is now ordered Doctrine of the Mean Is the Truth, Ken, Pure, The Birth of
    the Sun and Depth; Digital Form retains Morrow & Grain Demo.
  - Corrected Morrow & Grain's cursor preview binding away from the unrelated Dutch
    Treat image.
  - The supplied optimized painting files are under
    `/Users/Zhuanz/Desktop/Worls/Paintings/Webp`. Filename authority changes `E`
    to `Ken`. The user uploaded Ken and Pure manually; live cursor readback now shows
    distinct Framer image URLs for both variants.
  - Phone readback confirms all ten archive instances select the Phone variant,
    use `1fr` width, and bind to their matching custom cursor preview. The shared
    Phone title owns
    248 px inside its 330 px row; the 390 px screenshot shows normal horizontal
    titles, with the longest title wrapping to two lines instead of vertically.
  - Added `Phone Hover` from the Phone structural variant. It preserves the 330 px
    row, divider and title geometry, and changes only to each instance's Hover Fill.
    Desktop and Phone hover variants remain shared gesture states rather than
    record-specific copies.
  - Phone Footer keeps its full-width surface while `Paired Layout` uses `1fr` with
    `maxWidth: 480px`. The wordmark column uses `1fr`, `minWidth: 0` and
    `maxWidth: 336px`; Navigation uses a stable 104 px width within 96–120 px.
  - The Main Template Phone Footer instance now uses `height: auto` with a 220 px
    minimum. A 760 px Phone Preview remained inside the viewport with no horizontal
    overflow; Preview width was restored to 390 px afterward.
  - `Sanctuary1` was not found under the project image folders, repository history,
    Spotlight index or available Framer asset readback. Sanctuary was not invented
    or added with a wrong cover.
- Current document task: Keep `content-library/ken-studio/PROJECT.md` as the durable design and recovery source.
- Remaining work:
  - Run a hands-on Preview pass for the exact Core growth, document crossfade, final arrival and sticky release timing on all three devices.
  - Verify reduced-motion behavior and real-device memory use; current screenshots validate static composition, not scroll runtime.
  - Add confirmed links and case-study routes to the two Website Practice covers
    when those destinations are ready.
  - Audit Home, About and detail pages against the new type system.
  - Complete a final published/runtime pointer test for every Works custom cursor;
    the editor interaction pass verified row hover stability and cursor bindings,
    but the OS pointer image is not represented in captured screenshots.
  - Run one later narrow-screen pointer Preview when Framer's embedded preview
    viewport renders normally; the current embedded canvas loaded the full Works DOM
    but produced a blank visual frame, so runtime evidence is structural for now.
  - Provide or identify the exact `Sanctuary1` asset, then add Sanctuary as the next
    Observation row and bind its cursor preview.
  - Re-open the final Fighting the Chemistry Phone screenshot or Preview when the
    Framer screenshot CDN is stable; current structural audit confirms one visible
    h1 and one visible Lead, with the legacy text nodes hidden.
  - Apply or normalize the new semantic Text Styles outside the current Home scope.
  - Resolve missing content and routes.
  - Complete SEO, remaining alt text and interactive Preview checks before publishing.
- Important local asset path: `content-library/ken-studio/images`

## 21. Definition of Done

A page is complete only when:

- Its purpose and content source are documented.
- Typography follows the four established font roles.
- Desktop, Tablet and Phone are intentionally composed.
- All real links, focus states and touch targets work.
- Images have meaningful alt text and appropriate web derivatives.
- Motion has a stated purpose and a reduced-motion fallback.
- No invented facts or placeholder copy remain visible.
- SEO title, description and OG image are set.
- Targeted Preview QA has passed.
- Any exception is recorded in this file.

The website is complete only when every published page satisfies this definition and the Build Status Matrix is updated to reflect verified reality.
