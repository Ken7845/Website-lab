# Ken Studio Personal Site

- State schema: 1
- Current status owner: [STATUS.md](./STATUS.md)
- Recovery owner: [RECOVERY.md](./RECOVERY.md)

## 1. Project Identity

- Project name: Ken Studio Personal Site
- Platform: Framer
- Project type: Personal Portfolio / Visual Archive
- Status: Building
- Framer project URL: https://framer.com/projects/Ken-Studio--W2l0ZO8Ar0mErx3GOD0d-cr6l9
- Framer project ID: `W2l0ZO8Ar0mErx3GOD0d`
- Demo URL: Missing
- Content status: Mixed
- Last updated: 2026-10-03 — repository owner split; last recorded live evidence 2026-07-30

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

当前视觉系统由 [STYLE_GUIDE.md](./STYLE_GUIDE.md) 维护，实施与 QA 由 [STATUS.md](./STATUS.md) 维护；没有独立 Works Archive Implementation Plan。旧 `STYLE-GUIDE.md` 不再作为入口。

## 6. Typography System

See [STYLE_GUIDE](./STYLE_GUIDE.md) for this unchanged system.

## 7. Layout and Spacing System

See [STYLE_GUIDE](./STYLE_GUIDE.md) for this unchanged system.

## 8. Color and Surface System

See [STYLE_GUIDE](./STYLE_GUIDE.md) for this unchanged system.

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
- Contact sheet: the former `Framer 2/contact-sheets/ken-studio-paintings-review.jpg` is a historical temporary artifact, not currently present at that repository-relative path. Regenerate from resident authorized source files only if the active task needs it.
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

See [STATUS](./STATUS.md) for current results and gaps.

## 19. Decisions and Exceptions

See [DECISIONS](./DECISIONS.md) for active approved decisions.

## 20. Recovery State

See [RECOVERY](./RECOVERY.md) for the one current continuation pointer; exact earlier evidence is indexed in [HISTORY](./HISTORY.md).

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
