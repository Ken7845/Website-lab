# Framer Part Completion Checklist

本文件是实施后的 evaluator：把 `framer/basic` 的规则转换为每个工作部分完成后的强制自审与自修补清单。

它不是开工前必须全读的建设手册，也不是只在最终交付时才使用的总检查表。先从 `framer/README.md` inspect / reconcile、选择一个 primary repo Skill 并完成当前 Part；随后只读取本文件路由表和对应章节。发现问题先修补并复检，再进入下一个部分。

纯 Audit / Preflight 任务可以把 `framer-qa` 作为 primary Skill 并直接进入本文件。长篇多分点 Prompt 与连续修改的写入前规则见 `framer/basic/workflows/change-control.md`；这是实施前的条件 Gate，不要求预读本文件全部 evaluator。

规则来源：

- `framer/basic/standards/website-baseline.md`
- `framer/basic/standards/layer-naming.md`
- `framer/basic/standards/marketplace-guidelines.md`
- `framer/basic/patterns/pattern-recipes.md`
- `framer/basic/patterns/navbar-footer.md`
- `framer/basic/patterns/motion-design.md`
- `framer/basic/workflows/build-checklist.md`
- `framer/basic/workflows/preflight-audit.md`
- `framer/basic/workflows/image-workflow.md`
- `framer/basic/workflows/token-saving.md`
- `framer/basic/workflows/change-control.md`

---

## 项目级 Checklist 文件夹规范

页面 / request 合同的创建、目录、必需职责和确认条件由 [change-control — 项目级 Checklist 文件夹规范](basic/workflows/change-control.md#项目级-checklist-文件夹规范) 维护。先按该合同建设，再由本文件按 Part 路由评估；不要用 evaluator 重新决定是否开工。

页面与当前状态同步遵守 [Content Library — Current state contract](../content-library/README.md#current-state-contract)。

---

## 0. 实施后使用方法

当前 Part 实施完成后使用以下闭环：

```text
完成一个 Part
→ 在“路由表”找到对应 Checklist
→ Targeted readback / Preview
→ 标记 Pass / Fix / Blocked
→ 同类问题批量自修补
→ 只复检受影响范围
→ 更新 STATUS / RECOVERY 的当前 owner
→ 才能进入下一个 Part
```

强制要求：

- [ ] 不凭记忆检查；每次实际打开并读取本文件的对应部分。
- [ ] 一个 Part 可以触发多个 Checklist，例如 Component + Responsive + Image。
- [ ] 任一必查项失败时，当前 Part 状态为 `Fix Required`，不得报告完成。
- [ ] 能在当前授权范围内修复的问题必须直接自修补，不把基础缺陷留给用户。
- [ ] 缺少事实、权限或素材时标记 `Blocked`，继续完成不依赖阻塞项的工作。
- [ ] 用户要求“完成”、“一次性完成”或完成当前 Part 时，Scope 内每个项目必须为 `Pass`、有证据的 `Blocked` 或用户明确授权的 `Deferred`；不得带未分类的 `[ ]` 结束。
- [ ] 新建、复制或改写可复用 Component 责任时，实施前的 `Component Requirement Contract` 已为 `Ready`；实施后按同一合同记录 Implementation status、Verification status 与 `Pass / Fix Required / Blocked` 证据。
- [ ] 新 Page、主要 Section 重设计、跨页面差异化或“different layout”范围在实施前已有 `Ready` 的 `Visual Direction Contract`；实施后按同一合同反向验证，并分别记录 Structural status 与 Visual status。
- [ ] 跨页面差异以全站 layout-family distribution 判断，不要求每个 Section 独一无二：同职责 Contact / CTA / Form 与共享系统可有理由复用；所有 sibling pages 使用同一 Hero 或完整页面构图的 site-wide layout monoculture 不通过；示例数量不是硬配额。
- [ ] 用户明确设计意图与通用规则冲突时保留用户意图，并在 `DECISIONS.md` 或 PROJECT 的 Decisions / Exceptions 章节记录。
- [ ] 只复检当前 Part 及受影响的共享依赖，不无目的重读整页或整站。

### 高效率审查分级

所有修改都要验证，但不是所有修改都需要截图或完整 Preview：

| 风险 | 必要审查 | 可以省略 |
|---|---|---|
| Rename、文案、Link、Property、非视觉结构 | Targeted readback、数量和真实值 | Screenshot、全断点 Preview |
| Fill、Border、Typography、Layout、Breakpoint | Targeted readback + 受影响断点的一次目标节点截图 | 全页截图、重复查看相邻未受影响状态 |
| Hover、Cursor、Overlay、Scroll、Lightbox | 结构回读 + 一次真实关键交互路径 | 每个实例重复操作、同状态重复截图 |
| Page / Website 完成 | 当前范围 Preflight + 代表性宽度和路径 | 与本轮无关的全站重审 |

- [ ] 共享组件修改后检查所有受影响实例的结构值，但视觉抽查只选每类状态的代表实例。
- [ ] 继承关系明确且尺寸未改变时，检查主断点和发生 override 的断点；不机械重截全部断点。
- [ ] 一条权威证据已回答问题后停止，不再用第二、第三种工具重复证明。

### Part 路由表

| 本轮完成的 Part | 必查部分 |
|---|---|
| 任何修改 | 1、2、18 |
| 新建或修改 Section | 1、3、4、4A、6、8；按需追加 5、7、9 |
| Layout Template / 页面骨架 / 共享结构 | 4A、5、8 |
| Text / Color Styles | 3 |
| Layer Tree / 命名 | 4 |
| Component / Variant / Property | 5、8 |
| CTA / Link / Contact | 6 |
| 图片、Gallery、封面、Cursor Preview | 7、8；有交互再查 9 |
| Desktop / Tablet / Phone | 8 |
| Motion / Hover / Overlay / Lightbox | 9 |
| Navbar | 5、6、8、9、10 |
| Footer | 5、6、8、11 |
| Page 完成 | 12、17 |
| CMS | 13 |
| Form / Input / Submit | 6、8、13A、14 |
| Accessibility | 14 |
| Performance / Framer Review | 15 |
| Marketplace Template | 16、17 |
| Session、长任务、图片查看中断 | 18 |

---

## 1. Scope、内容与事实

- [ ] 当前范围明确为 Section / Component / Page / Website / Audit。
- [ ] 已读取当前项目 `PROJECT.md` 及其链接的 Brand Voice、内容和素材。
- [ ] 已确认当前 Part 的目标用户、内容目的和主要行动。
- [ ] 内容状态已区分 Approved / Draft / Missing / Demo。
- [ ] 未编造地址、价格、营业时间、人员、联系方式或其他品牌事实。
- [ ] 未删除或替换用户核心素材，除非用户明确授权。
- [ ] 本轮不做的内容已明确，未发生范围漂移。

自修补：

- 事实缺失：停止正式内容写入，标记 `Missing`，先完成结构或样式工作。
- 文案偏离：回读 `BRAND_VOICE.md`，批量修正当前 Part 的文字。
- 范围扩大：暂停新增范围，先报告影响并取得确认。

---

## 2. 每个 Part 的通用完成门槛

- [ ] 当前 Part 使用真实内容或已标明状态的 Draft / Demo 内容。
- [ ] 使用正确的 Styles、语义、链接和内容入口。
- [ ] 重复结构已判断普通 Frame / Component / Property / CMS 的正确归属。
- [ ] Desktop、Tablet、Phone 均已处理，而不是只完成 Desktop。
- [ ] 静态平面设计已由 Agent 直接通过目标画布/截图审阅；必要交互已完成目标化结构读回。交互的实际效果按 [evidence selection](basic/workflows/image-workflow.md#evidence-selection) 通过必要 Preview 或具有明确范围的用户确认建立；不可把结构设置当作 runtime 证据。
- [ ] 新增 Layer、Component、Variant 没有默认名称。
- [ ] Targeted readback 确认实际值，而不是根据命令成功推测完成。
- [ ] 本轮新增 Error 已解决；Warning 已判断是问题还是明确设计意图。
- [ ] 当前 Part 已达到 Pass，或真实 Blocked 已记录。

自修补：

- 同类问题一次批量修复，例如一批 Alt、一批 Link、一批命名。
- 只重测受影响的断点、实例或交互路径。
- 如果修复触及共享 Component，重新检查所有受影响 Page Instances。

---

## 3. Style System 与 Typography

### Text Styles

- [ ] Display / H1、H2、H3（需要时）、Body Large、Body、Caption、Eyebrow / Label、Button Label 已按项目需要建立。
- [ ] 同一语义角色复用同一 Text Style。
- [ ] Heading 的 HTML 语义与视觉 Style 分开判断。
- [ ] 页面主标题为 `h1`，主要 Section 为 `h2`，子级内容为 `h3`。
- [ ] Eyebrow、价格、标签未因视觉醒目被误设为 Heading。
- [ ] 字体沿用参考时读取真实节点属性，没有凭截图或印象猜测。
- [ ] Desktop、Tablet、Phone 字号和换行分别检查。

### Color Styles / Variables

- [ ] Background、Surface、Text、Accent、Border、Hover、Focus 等核心颜色使用 Styles / Variables。
- [ ] 命名按语义用途，不按临时色值或单个页面命名。
- [ ] Navbar、Footer、Button、Overlay 和 Link State 使用正确语义颜色。
- [ ] Hover 与 Focus 在所在背景上保持足够对比。
- [ ] 局部直接样式只有少量、有理由的例外。
- [ ] 页面间沿用批准的颜色角色，但 Section 明暗顺序、强调色密度和图片色调形成合同中批准的 Colour rhythm，而非复制 sibling page 的整页色块节奏。

自修补：

- 出现同角色多个直接样式：建立或复用 Style 后批量替换。
- Phone 文字挤压：先检查宽度链和父级布局，再调整响应式 Style。
- 字体不一致：回读正确参考节点的 font、weight、size、line-height、letter-spacing、color 后同步。

---

## 4. Layer Tree 与命名

- [ ] Page、Section、Container、Stack、Row、Grid、Frame、Text、Image 和 Button 均按用途命名。
- [ ] 名称使用当前父级语境中最短且可区分的表达，没有重复祖先或 Section 前缀。
- [ ] 不存在 `Frame`、`Stack 1`、`Text 2`、`Variant 2`、`Copy` 等默认或无语义名称。
- [ ] Section 使用“内容主题 + Section”。
- [ ] Stack / Row / Grid 名称说明内容与布局职责。
- [ ] Text 名称说明 Heading、Description、Label、Caption 等语义。
- [ ] Button 名称说明行动结果，例如 `View Project Button`。
- [ ] Component 使用 PascalCase。
- [ ] Variant 名称描述状态、结构、背景或断点。
- [ ] Scroll Section / Trigger 名称与实际 Effect 目标对应。
- [ ] 修改已有页面时延续现有命名体系，没有另起一套近似语言。

自修补：

- Targeted 读取当前 Part 的 Layer Tree。
- 按同一命名模式批量重命名默认层。
- 不为修名改变层级、位置、Effect target 或布局属性。

---

## 4A. Layout、Section 与共享结构

- [ ] Section 顺序服务品牌叙事、页面目的和主要行动，不机械复制 Hero + Cards + CTA 模板。
- [ ] 当前 Part 有明确的视觉层级、阅读顺序和一个主要重点。
- [ ] 使用 Stack / Grid 建立稳定布局，Absolute 只用于明确重叠、动效或特殊构图。
- [ ] 已明确 Section、Container、Row/Grid、Component 和内容层之间的宽度所有权。
- [ ] `max-width` 只位于需要阅读行长或几何上限的 deepest valid max-width owner；Page root、full-bleed Section 与负责分配宽度的 senior structural parent 保持 Fill / `1fr`。Approved bounded-canvas exception 有独立全视口背景 Owner 和全断点证据。
- [ ] Gap、Padding 和 Section rhythm 来自稳定系统，不逐层随机补值。
- [ ] Text 不贴可见容器边缘；外层可见容器拥有必要 padding。
- [ ] 内容增长、标题变长和图片比例变化时布局仍能自然扩展。
- [ ] 多页面网站使用 `Layout Template → Navbar → Content Placeholder → Footer`。
- [ ] Page 只维护自己的 Content，没有复制 Navbar / Footer。
- [ ] 共享结构修改后已检查所有受影响页面。
- [ ] Section 没有因为动效 Trigger、Absolute Layer 或隐藏层产生意外高度、裁切或 overlap。
- [ ] 页面视觉保留项目独特性，没有把不同 Section 平均化成同一种容器模板。

自修补：

- 结构不稳定：先修最上游 Stack/Grid、width、max-width、gap 和 padding，再修子层。
- 内容增长破坏布局：去除不必要固定高度，改为内容驱动高度或合理最小值。
- 共享结构出现副本：合并为 Component / Layout Template，并重新检查实例。
- Absolute / Scroll Section 已由用户调试：先记录 Rect、位置和 Effect target；未经明确必要不移动。

---

## 5. Component、Variant、Property 与 Instance

### 创建前

- [ ] 该结构确实跨页面或高频重复，不是一次性内容。
- [ ] 内容差异使用 Property、Fill 或 CMS。
- [ ] Variant 只表达状态或结构，例如断点、排列、Light/Dark、Open/Closed。
- [ ] 没有为每张不同图片或每段不同文字创建 Variant。
- [ ] 项目行或卡片没有按记录复制 Desktop / Phone / Hover Variant；内容与 Fill 从 Instance Properties 设置。
- [ ] 没有两个表达同一内容职责的重复 Property。
- [ ] 已判断问题属于 Component Definition、Page Instance 还是 Breakpoint Override。

### 创建后强制回到页面实例

- [ ] 每个 Instance 选择了正确 Variant。
- [ ] 每个 Instance 的文字已替换，不保留默认值。
- [ ] 每个 Instance 的图片与 Alt 已替换，不保留默认值。
- [ ] Link 已保留或设置为正确真实目标。
- [ ] Effect 对应的 Scroll Target 仍然有效，Scroll Section不会因为被纳入component里面而失效，Scroll Section就在外部并在component内部进行引用。
- [ ] Hover Effect 或共享 Gesture Variant 在 Preview 中仍然有效。
- [ ] Cursor / Custom Cursor 仍然存在且指向正确 Variant。
- [ ] Tablet / Phone 选择了对应 Variant。
- [ ] Phone 不需要的 metadata、status、cursor 已隐藏或禁用。
- [ ] Instance 的 width、height、max-width 和父级 Stack 关系正确。
- [ ] 所有受共享组件影响的页面实例均已抽查。
- [ ] 未使用的变量、测试 Variant 和空 Component 已删除。

自修补：

- 默认内容残留：按实例批量写入真实 Properties。
- 动效目标丢失：优先把触发器放在可复用的同一 Scope；不得静默改成不同动效。
- Hover 丢失：先检查当前模式是 Instance Effect 还是共享 Gesture Variant，再修对应层；不要为记录内容补建专属 Gesture Variant。
- 断点错误：修对应 breakpoint override，不为了 Phone 破坏 Component 主 Variant。
- 无法在不改变行为的情况下组件化：停止替换，恢复页面状态并报告结构限制。

---

## 6. Links、CTA 与 Conversion

- [ ] Logo 链接到 `/`。
- [ ] Navbar、Footer 和主要 CTA 均有真实目标。
- [ ] 不链接到不存在、Draft 或无关页面。
- [ ] Phone 使用 `tel:`，Email 使用 `mailto:`，地址使用地图链接。
- [ ] Social 使用真实外部 URL，按需新标签页打开。
- [ ] Button / Link 文案描述行动结果。
- [ ] 主体内容也提供核心行动，不让用户只能去 Footer 操作。
- [ ] 无空链接、无无关锚点、无测试链接。
- [ ] Current 状态使用 Link Style / 原生状态，不复制多套导航。
- [ ] Hover 不使用 scale，不推开相邻内容。

自修补：

- 缺少真实事实：不编造目标，标记 `Blocked`。
- 链接散落：按 Navbar、主体 CTA、Footer 分组批量修复。
- 修复后真实点击一条内部路径、一条主要 CTA 和相关外部/协议链接。

---

## 7. 图片、Gallery 与视觉素材

### 本地素材查看前

- [ ] 未直接对未知目录或多张原尺寸图片调用视觉查看工具。
- [ ] 已检查文件名、逻辑大小、`ls -lO@` flags 和单图像素尺寸。
- [ ] dataless / offline / cloud-only 文件已停止读取、下载或标记 Blocked。
- [ ] 已估算总像素和解码内存，而不是只看压缩文件大小。
- [ ] 已生成最长边不超过 1200px、约 50–60% JPEG、尽量小于 1MB 的联系表。
- [ ] 本轮最多查看一张已验证联系表。
- [ ] 已写 Image Review Plan；单个 Part 未超过“一张联系表或三张单图”的视觉预算。
- [ ] 同一素材或 screenshot URL 未被重复查看；跨工具总尝试不超过两次。
- [ ] 原始素材未被覆盖，输出写入独立目录并保留版本。

### Framer 画布检查

- [ ] 优先使用目标节点或 Variant 的 Framer on-demand screenshot。
- [ ] 每次只检查一个必要节点或一个 Variant。
- [ ] 未打印原始截图 Buffer。
- [ ] 截图失败后转为 Rect、Fill、Style、Link、Effect target 的结构审计，没有无限重试。

### 网页使用

- [ ] 网页输出尺寸与容器匹配，不直接使用不必要的超大原图。
- [ ] 裁切保留核心视觉信息，不机械统一格子。
- [ ] 作品集、摄影和案例封面优先原比例 / `fit-image`。
- [ ] 只有明确统一卡片矩阵时才使用固定比例 cover。
- [ ] Desktop、Tablet、Phone 分别检查比例、焦点和高度。
- [ ] 信息性图片有简短具体 Alt。
- [ ] 装饰图片显式空 Alt。
- [ ] 不存在 Alt 未定义。
- [ ] 没有地图 UI、黑块、角落控件或截图痕迹。
- [ ] `Asset usage ledger` 已记录候选素材的 narrative qualities、Approved role、Current use、Reuse decision / reason、裁切焦点和 allocated / used / reassigned / blocked 状态。
- [ ] 用户内容库中适合当前叙事且已获批准的素材已被使用、明确重新分配或有证据地标记 Blocked；没有因邻页已方便使用某图就无理由复用。
- [ ] 每张图片承担明确的 content-relative image role；替换标题、颜色或布局不构成使用叙事不相关图片的理由。

### Gallery / Hover

- [ ] 图片 Hover 使用“Outer Frame + Inner Image”，只缩放图片内容层。
- [ ] 简单放大使用 Lightbox Effect。
- [ ] 没有为每张图片创建 Overlay 或内容 Variant。
- [ ] Lightbox 有连续 transition、合理 max-width、边距、Backdrop 和关闭路径。
- [ ] Desktop、Tablet、Phone 均真实打开和关闭一次。

自修补：

- 图片查看无输出：立即停止；检查 flags；只重试一次更小联系表；仍失败则降级为结构审计并标记视觉判断 Blocked。
- 裁切错误：先调焦点或容器比例，再考虑换图。
- Hover 被 clip：取消外框 scale，改为内部图片层。
- 图片内容串用：回到每个 Component Instance 重新设置 Image Property 和 Alt。

---

## 8. Responsive 与 Width Ownership

最低检查：320 / 390 / 810 / 1200 / 1440+。

### 共通

- [ ] 已画清 Section → Container → Row/Grid → Component → Text/Image 的宽度链。
- [ ] 明确固定宽度、`1fr`、`100%`、max-width 和隐藏规则分别由哪一层拥有。
- [ ] 没有把 `max-width` 放在 Page root、full-bleed Section 或 senior structural parent 上来统一封顶整组内容；需要封顶时已下移到 deepest valid max-width owner。
- [ ] 没有先用缩小字体掩盖父级宽度错误。
- [ ] 无横向溢出、负宽度、零尺寸可见层或意外裁切。

### Desktop

- [ ] 外层骨架在宽屏继续响应；只有局部 deepest valid max-width owner 保持合理上限，阅读内容不会无限拉伸。
- [ ] 构图、留白、大图比例和 Section 节奏成立。
- [ ] Navbar 单行且 Sticky 正常。
- [ ] Preserve 的品牌系统与 Transform 的页面构图同时成立；与 sibling page 的 masthead、Section 顺序、图文比例和主要视觉记忆点存在合同中定义的 coherent difference。

### Tablet

- [ ] 不是被动缩放 Desktop。
- [ ] Grid、Row、间距、字体和图片焦点已重新判断。
- [ ] Navbar、Footer 和 CTA 不拥挤。

### Phone 320 / 390

- [ ] Row/Grid 转为自然 Stack 或合理减少次要信息。
- [ ] 内容顺序符合阅读和行动优先级。
- [ ] Heading、邮箱、价格、日期和 metadata 无破坏性断行。
- [ ] 触控目标约 44×44px 或更大。
- [ ] 核心导航不依赖 Footer。
- [ ] 图片比例、焦点和高度已重新设置。
- [ ] 不存在极小文字和横向溢出。

自修补：

- 先修最上游宽度所有者，再修子级。
- 用 breakpoint override 修端侧差异，不污染其他断点。
- 修复后只复检受影响宽度及相邻一个宽度。

---

## 9. Motion、Hover、Overlay 与 Lightbox

- [ ] Motion 服务品牌氛围、阅读节奏、状态反馈或空间层级。
- [ ] 优先使用 Framer 原生 Effects、Variants、Overlays 和 Lightbox。
- [ ] 不为简单效果引入 Custom Code。
- [ ] 默认 Spring Physics 以 stiffness 250 为起点，动画克制、平稳、无夸张 bounce。
- [ ] Scroll / Appear Effect 的 target、viewport、transition 和 section 值均已回读。
- [ ] 修改动效前保存目标值，修改后逐项对比。
- [ ] Hover 不改变密集 Row、Navbar、Footer、Menu、Button 或 Card 的布局尺寸。
- [ ] Dense Row Hover 只在所有实例共享同一状态样式时使用 Component Gesture Variant；记录专属 Hover Fill 使用 Instance Property / Effect，不为每条记录复制 Gesture Variant。
- [ ] Button Hover 保持对比度，不默认 scale。
- [ ] Overlay / Lightbox 不闪现，有明确关闭路径。
- [ ] Reduced Motion 下不依赖大位移、强缩放、视差或持续运动传递信息。

模式选择：

- [ ] Phone Navbar Menu → Relative Overlay。
- [ ] 简单图片放大 → Lightbox Effect。
- [ ] 页面级复杂 Modal → Fixed Overlay。
- [ ] Disclosure → Open / Closed Component Variants。
- [ ] 相同结构不同内容 → Property / Fill / CMS。

自修补：

- 交互结构选错：停止叠加事件链，按 Pattern Recipe 重建最小原生结构。
- Effect target 串联：恢复原 target，或把 target 与动画元素放在同一可复用 Scope。
- Preview 无 Hover：检查当前组件约定的 Instance Effect 或共享 Gesture Variant；不要混用两套模式，也不要按记录复制 Hover Variant。
- 修改后真实走一次 Open → Close / Hover → Leave / Scroll enter 路径。

---

## 10. Navbar

- [ ] Navbar、Footer 与 Content 使用共享 Layout Template。
- [ ] Navbar 是共享 Component，不在每页复制。
- [ ] Desktop 单行，通常不超过 80px。
- [ ] Sticky、top 0 和 z-index 正常。
- [ ] 使用滚动隐藏时，向下隐藏、向上出现且不改变页面布局高度。
- [ ] Logo、所有导航和 CTA 使用真实链接。
- [ ] Desktop / Tablet / Phone Variant 清楚且已应用到页面实例。
- [ ] Tablet 间距和 padding 已收紧但仍清晰。
- [ ] Phone 只保留 Logo 与必要入口，核心导航不依赖 Footer。

### Phone Menu

- [ ] Menu Trigger 在共享 Navbar Component 内，触控高度至少约 44px。
- [ ] Relative Overlay 直接挂在 Trigger 下。
- [ ] Overlay 有 Home、核心页面、主要 CTA 和可见 Close。
- [ ] 390px 面板保留屏幕边距；320px 无溢出。
- [ ] Collision detection、外部点击和键盘关闭正常。
- [ ] Desktop / Tablet 不显示 Phone Trigger。
- [ ] Preview 完成 Open → Close → Open → Core Link。

自修补：

- 普通手机菜单误用 Fixed Overlay：改回 Trigger 内 Relative Overlay。
- 组件化后链接或滚动行为丢失：逐个页面实例复查 Variant、Link、Effect。

---

## 11. Footer

- [ ] Footer 是共享 Component，并通过 Layout Template 服务所有页面。
- [ ] 包含项目已确认存在的 Brand、tagline、导航、CTA 和必要辅助信息。
- [ ] 地址、时间、电话、Email、Social 只在有真实事实时加入。
- [ ] 电话、Email、地图和外部链接均使用真实协议/目标。
- [ ] Copyright 和 Demo 声明与项目状态一致。
- [ ] 顶部和四周有合理留白，内容不贴边、不挤在首行。
- [ ] Desktop / Tablet / Phone 的列数或阅读结构适应实际内容。
- [ ] 用户明确指定特殊 Phone 风格时已在 Decisions 记录，并确保不溢出。
- [ ] 链接拆成独立 Layer，可分别设置 Link、Hover 和间距。
- [ ] Footer Hover 不 scale、不被 clip、不推开相邻内容。
- [ ] 所有页面实例使用正确 Footer Variant、颜色和链接。
- [ ] Preview 至少点击一个页面链接、一个 CTA 和一个外部/协议链接。

自修补：

- 缺少事实：不填虚构联系信息，只保留已确认导航和 CTA。
- 多页副本：合并为共享 Footer Component + Layout Template。
- Phone 拥挤：重排内容顺序、列数和 gap，不只缩小字号。

---

## 12. Page、SEO 与语义

- [ ] Page 有明确目的和主要 CTA。
- [ ] Page Title 唯一。
- [ ] Meta Description 独立。
- [ ] 恰好一个主要 `h1`。
- [ ] 主要 Section 使用合理 `h2`，子级使用 `h3`。
- [ ] 页面路径清晰，正式导航不引用 Draft 页面。
- [ ] favicon、Open Graph 和必要分享信息已设置。
- [ ] 无 Lorem Ipsum、未说明占位内容或无来源事实。
- [ ] Navbar、Footer、CTA、Contact / Visit 信息可操作。
- [ ] 所有图片已完成 Alt 判断。
- [ ] 320 / 390 / 810 / 1200 / 1440+ 已检查。
- [ ] 已完成至少一次目标化 Preview。

自修补：

- Metadata、Heading、Alt、Links 按类别批量修复。
- 不用视觉字号替代 HTML Heading 语义。
- Page 未通过本节时不能进入 Done。

---

## 13. CMS

- [ ] 只有需要频繁增删排序、字段化、分类或详情页时使用 CMS。
- [ ] 少量静态内容没有为了“专业感”被强行 CMS 化。
- [ ] 字段命名清楚，默认内容完整，无测试字段和条目。
- [ ] 分类、排序和编辑入口可理解。
- [ ] 长标题、不同图片比例、可选字段缺失不会破坏布局。
- [ ] 内容与品牌事实一致。
- [ ] Marketplace 项目包含简短编辑说明。

自修补：

- 结构重复但无需增删：改为 Component + Properties。
- CMS 负担大于维护价值：保留静态结构并记录决定。

---

## 13A. Forms

- [ ] Form 只收集完成用户目标所需的信息，没有无意义字段。
- [ ] 每个输入有可见、明确且与控件关联的 Label。
- [ ] Placeholder 不替代 Label。
- [ ] Email、Phone、URL 等使用正确输入类型。
- [ ] 必填、可选、错误、提交中、成功和失败状态清楚。
- [ ] Submit Button 使用可维护的共享 Button Component / 对应状态 Variant。
- [ ] 键盘顺序、Focus、Enter 提交和错误返回路径可用。
- [ ] Phone 输入与 Submit 触控尺寸合理，无横向溢出。
- [ ] 隐私、数据去向和第三方依赖与项目事实一致。
- [ ] Preview 真实完成一次成功提交；无法真实提交时明确标记 Blocked，不能假装通过。

自修补：

- 缺 Label 或错误语义：按字段批量补齐，不只调整视觉。
- Submit 状态不完整：补 Pending / Success / Error / Incomplete Variant 或明确反馈。
- 外部服务未授权：保留可审查结构，记录 Blocked，不连接虚构 endpoint。

---

## 14. Accessibility 与 Focus

- [ ] 正文尺寸和颜色对比满足阅读需要。
- [ ] Focus 状态可见。
- [ ] 键盘顺序符合视觉顺序。
- [ ] Hover 信息在触控和键盘下仍可获得。
- [ ] Button / Link 名称说明操作结果。
- [ ] Overlay、Lightbox 和 Form 不造成焦点丢失。
- [ ] Overlay / Lightbox 有明确 Close 和原生退出路径。
- [ ] Reduced Motion 不破坏内容、导航或反馈。
- [ ] 装饰图片空 Alt，信息图片有有效 Alt。

自修补：

- 对比不足：使用语义 Color Style 修复，不逐节点临时调色。
- 只有 Hover 可见的信息：增加可点击、Focus 或常驻表达。

---

## 15. Performance、维护与 Framer Review

- [ ] 图片尺寸与实际容器匹配。
- [ ] 动画数量克制，没有无意义持续运动。
- [ ] 没有无用 Code、重复 Components、重复 Variants 或测试 CMS 字段。
- [ ] 新增一条内容只需复制 Instance 并修改 Properties，不需要扩张组件 Variant 集。
- [ ] 核心视觉可通过 Styles 修改。
- [ ] 核心内容可通过 Properties / CMS / Fill 修改。
- [ ] 核心结构可通过共享 Components 修改。
- [ ] 第三方依赖和授权清楚。
- [ ] 本轮新增 invalid / rejected attributes、零尺寸可见层、意外 overlap、hover clip 已解决。
- [ ] Intentional sticky overlap 等 Warning 已判断并记录，而不是机械清零。

自修补：

- 新增错误优先修复；旧 Warning 只在当前范围受影响时处理。
- 删除临时组件、空变量和测试内容。
- 不为消除 Warning 破坏明确设计意图。

---

## 16. Marketplace Template

- [ ] 普通 Website Baseline 已通过。
- [ ] 定位明确到行业、目标买家和使用场景。
- [ ] 默认内容像真实品牌，不是组件展示页。
- [ ] 至少一个明确视觉记忆点。
- [ ] 买家可快速找到 Styles、Navbar、Footer、Buttons、CMS 和内容入口。
- [ ] 字体、颜色、图片和内容可直接替换，不需要理解 Variant 迷宫。
- [ ] Components、Properties 和 CMS 已做内容替换压力测试。
- [ ] 长内容、不同图片比例和可选字段缺失不会破坏布局。
- [ ] 已删除测试组件、无用字段、默认 Layer 名和未使用 Styles。
- [ ] Preview、Demo、Remix、Desktop/Phone 截图和编辑说明完整。
- [ ] 授权、第三方依赖和 Fictional / Demo 声明完整。
- [ ] 无私人信息、测试链接和未授权素材。

自修补：

- 高视觉分不能抵消低可编辑性、低可访问性或缺失交付材料。
- Productization 问题按 Styles、Components、CMS、Instructions 分批修复。

---

## 17. Part / Page / Website Preflight

### Section Done

- [ ] Styles、Component 决策、图片、Alt、Links、Heading 完成。
- [ ] Desktop、Tablet、Phone 成立。
- [ ] 必要 Motion / Interaction 完成。
- [ ] Targeted readback 无结构性遗漏。

### Page Done

- [ ] 内容和主要行动完整。
- [ ] Metadata、一个 h1、主要 h2/h3 完成。
- [ ] Navbar、Footer、CTA、Contact / Visit 可操作。
- [ ] 图片 Alt 完整。
- [ ] 320 / 390 / 810 / 1200 / 1440+ 合理。
- [ ] 目标化 Preview 已通过。
- [ ] 适用时 `Visual Direction Contract` 已从 `Ready` 反向验证为 `Pass`；Structural status 与 Visual status 分别为 `Pass`。
- [ ] Page 范围已有代表性 Desktop / Tablet / Phone 静态全页视觉证据，可判断构图、颜色节奏、素材分配与 sibling-page differentiation，而不只验证结构值。

### Website Done

- [ ] Layout Template、Navbar、Footer、Buttons 和核心 Styles 成立。
- [ ] 全部正式页面进入项目 current status owner 的 Build Status Matrix。
- [ ] favicon、Open Graph、Links、Accessibility、Performance 完成。
- [ ] Sticky、Overlay、Lightbox、Form 等关键交互真实验证。
- [ ] 已执行 `framer/basic/workflows/preflight-audit.md`。
- [ ] Exceptions 和 Missing 已记录。

审查输出必须为：

```text
Scope: Section / Component / Page / Website
Status: Pass / Fix Required / Blocked
Structural status: Pass / Fix Required / Blocked
Visual status: Pass / Fix Required / Blocked / N/A — reason
Pass:
Fix Required:
Blocked:
Verified widths:
Verified paths:
Shared components:
```

---

## 18. Token、Session、截图与恢复

- [ ] 全程复用一个明确 Framer Session，不因等待变慢主动 reconnect。
- [ ] 第一次读取后保存 Page、Component、Variant、Instance 和 target IDs。
- [ ] 使用 targeted read，深度和属性只覆盖当前判断。
- [ ] 输出开始截断时立即缩小范围，不继续打印整页树。
- [ ] 已知结构一次批量写入，不把同类修改拆成大量调用。
- [ ] 修改后只回读目标节点、实例和断点。
- [ ] 按 [evidence selection](basic/workflows/image-workflow.md#evidence-selection) 选择结构、静态视觉或真实交互证据；不反复验证未改变的状态。
- [ ] API 超时或工具无输出时先读当前状态，不重复提交同一写入。
- [ ] 图片查看是可降级子步骤，不让整个 Framer 任务因视觉工具阻塞。
- [ ] 第一次视觉查看前已在 canonical Recovery owner 写入一个当前 Checkpoint。
- [ ] 每完成一个 Part 已覆盖更新 canonical Recovery owner 中的项目、页面、Session、组件、Variant、实例、断点、完成项和剩余项；没有在多个文件追加第二份 current diary。
- [ ] `PROJECT.md` current manifest、`STATUS.md` / Current Status、`DECISIONS.md` / Decisions、`RECOVERY.md` / Recovery 已按项目实际拆分更新，且没有维护两份 current 明细。

推荐单元：

```text
1 次 targeted read
→ 1 次批量 apply
→ 1 次 targeted review
→ 用户视觉确认或 1 次必要的关键 Preview
→ 本文件对应 Part 自审与修补
```

---

## 最终原则

Checklist 的目标不是增加报告长度，而是防止长 Context 中逐渐丢失基础要求。

Agent 不应只告诉用户“还有哪些问题”，而应在当前授权范围内完成以下闭环：

```text
发现
→ 定位所属层
→ 批量修补
→ 目标化复检
→ 记录结果
```

只有通过当前 Part 对应 Checklist，才可以继续下一个 Part 或向用户报告完成。
