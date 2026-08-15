# About Culture Revision — 2026-08-13

Page: About  
Path: `/about`  
Status: Completed — Canvas revision read back  
Parent page contract: [About Page Checklist](./about.md)

## 原始要求（逐字记录）

1. 我看到每个section之间都有一条黑线，你看着怎么去掉
2. 在About Opening和Statement Section中间放一张那个exterior的照片
3. 你可以用一些chefs/details的图片比如handheld dish和food plating，来讲一下我们是怎么对待cooking这件事的，你Working Details那三张就不要了，排版也换一下
4. Working Method Section，Relationships Section这两个部分的desktop排版有问题，根据知识库的排版指示去审查并修改
5. About Handoff Section就不要了，因为这个是关于餐厅文化的，不用插入预定引导
6. 有一个图片处理要求和排版要求要补充到知识库的basic里面，就是在排版的前提下要尊重图片内容，如果一张图片的内容被裁切了很多内容变得不可读，那么这个图片就没有存在的意义，还有我发现你图片的引用总是重复，在做不同page的时候要检索内容库里的images，然后筛选符合叙事内容的图片，不要乱用图片，当然在检阅的时候要符合防止卡顿的图片处理要求
7. 在AGENTS.md新增一条要求，接收到很长的分很多点的prompt的时候要在content-library里的对应项目的文件夹的checklist里面做一条checklist，逐字写入，不可简化要求，但可以把prompt的分点优化的更加具体，做完checklist后再等待确认开始执行任务

## 执行细化与验收

### 1. 移除 Section 之间的黑线

- [x] 审查 About 页面所有 Section、外层内容 Stack、边框、背景色衔接与任何非预期 gap；定位黑线的真正来源，不能仅以覆盖色遮挡。
- [x] 移除非设计意图的黑线，同时保留明确需要的导航底部细线和内容层级。
- [x] 在 Desktop、Tablet、Phone 回读受影响节点，确认不存在新的重叠、裁切或边界断裂。

### 2. Opening 与 Statement 之间的 exterior 图片

- [x] 在 `About Opening` 与 `Statement Section` 的阅读顺序之间加入 `images/Interior/exterior.webp`。
- [x] 为该图片设置与其建筑内容匹配的容器比例、焦点与具体 Alt；不得因为版式而使建筑主体不可读。
- [x] 各断点重新判断高度与裁切，Phone 不直接继承 Desktop 的图片位。

### 3. 以 chefs/details 重新叙述 cooking，并替换现有 Working Details

- [x] 删除现有 `Working Details` 三张图片及其旧排版，不保留空 Section 或无效结构。
- [x] 检索 `images/Chefs/details/`，至少将 `handheld-dish.webp` 与 `food-plating.webp` 作为候选，基于“如何对待 cooking”这一叙事选择图片，而不是沿用当前重复图片。
- [x] 以烹饪中的手、摆盘、服务或专注作为具体证据，写入不虚构厨师、产地、奖项、团队或流程事实的 Demo 文案。
- [x] 新布局必须不同于原有三列高低图片组；先确定图片内容完整性，再决定比例、阅读顺序、文字宽度、留白与跨端转换。
- [x] 为每张使用图片给出明确 Alt，并验证裁切没有令手部动作、菜品或服务信息不可读。

### 4. 修正 Working Method 与 Relationships 的 Desktop 排版

- [x] 按 `framer/basic/standards/website-baseline.md`、`framer/basic/patterns/pattern-recipes.md` 与 `framer/basic/workflows/image-workflow.md` 审查两个 Section 的宽度所有权、Stack 方向、gap、padding、max-width、文本 measure、Section 节奏及内容增长行为。
- [x] 先修上游 Stack / Grid、width、max-width、gap、padding 等结构原因，不以局部绝对定位或随意缩小字体掩盖问题。
- [x] Working Method 与 Relationships 使用各自服务内容的构图，避免把不同内容平均成相同容器模板。
- [x] Desktop 修改后再检查 Tablet 与 Phone 继承或 override，避免修复 Desktop 时造成窄屏回归。

### 5. 删除 About Handoff Section

- [x] 删除 `About Handoff Section` 及其中的 Menu 链接和 `Reserve a seat` 引导，不以空白占位代替。
- [x] 检查页面顺序、Footer 衔接、语义结构与页面高度，确保 About 以餐厅文化和关系段落自然结束。
- [x] 不修改共享 Navbar、Footer 或其他页面的预约路径，除非后续要求明确提出。

### 6. 补充 basic 图片处理与排版规则

- [x] 在 `framer/basic/workflows/image-workflow.md` 写入：排版必须尊重图片内容；若裁切使内容大量缺失且不可读，应调整焦点、比例、布局或换图，不得保留无意义图片。
- [x] 在 `framer/basic/workflows/image-workflow.md` 写入：新页面应先检索项目 `content-library/<project>/images/`，依据当前叙事筛选素材、控制无意义重复，并继续遵守驻留检查、视觉预算和联系表流程。
- [x] 在 `framer/basic/standards/website-baseline.md` 的 Layout 要求中加入图片内容完整性规则与对应工作流引用。

### 7. 补充 AGENTS.md 长篇 Prompt Checklist 规则

- [x] 在 `AGENTS.md` 写入：收到很长且分很多点的 Prompt 时，先在 `content-library/<project>/checklist/` 的对应项目 Checklist 中逐字记录，不得简化；可添加更具体的执行要求；完成后等待确认，再开始正式建设。
- [x] 本轮 Checklist 已在 `content-library/aurelia/checklist/about/2026-08-13-culture-revision.md` 中逐字写入七项要求，并在 Canvas 修改前暂停。

## Latest Part Result

Scope: About page structure, approved image upload, cooking revision, Desktop layout pass, and Menu typography alignment
Status: Completed — Menu-referenced typography and About layout polish read back

Image Review Plan — typography/layout polish:

- Exact target: one Framer screenshot of Desktop `Working Method Section`.
- Question: whether the Menu-referenced large-heading / compact-story-column relationship is legible and balanced in About.
- Evidence chain: one targeted Framer screenshot requested with its required `id` parameter. No full-page or source-image review.
- Budget: one screenshot request. If unavailable, record the failure and use the saved Typography attributes and stack ownership readback only.

Visual result:

- One Desktop `Working Method Section` screenshot passed. The 58% large heading and narrow right-hand story column are legible, retain generous editorial white space, and match the intended Menu Story Columns text treatment without duplicating the Relationships composition.

Image Review Plan:

- Exact target: one Framer screenshot of the Desktop `Cooking Section`.
- Question: whether the two selected images and their unequal, source-respecting proportions keep the hands, dish and plating action readable while supporting the cooking copy.
- Evidence chain: targeted Framer node screenshot only; no local original image preview is needed because the three approved source files were already verified in the earlier contact-sheet review and their current residency plus pixel dimensions were rechecked.
- Budget: one screenshot attempt in this Part. If it cannot be retrieved, fall back to the recorded source ratios, Fill URLs, Alt text, Frame dimensions and Section rect audit; do not retry through another visual path.

Pass:
- 黑线来源已确认是 `About Content` 外层 Stack 的 5px gap；已设为 0px，而非用背景覆盖。
- 已在 Opening 与 Statement 之间插入已指定的 exterior，且以源图 16:9 比例在三种断点分别设定可读高度。
- 已删除 Working Details 的原三张图片与旧三列构图；已上传并使用 `food-plating.webp` 与 `handheld-dish.webp`，写入不虚构事实的 cooking Demo 文案、明确 Alt 与新的两图编辑式构图。
- 已将 Working Method 修为明确的 Desktop 双栏宽度所有权和固定 gap；Relationships 改为宽标题加右对齐窄正文的独立构图，未使用绝对定位。
- 已删除 About Handoff Section 及其 Menu / Reserve 引导，未触及共享 Navbar 或 Footer。

Blocked:
- Targeted Framer screenshot could not be generated because the request was rejected for using `nodeId` rather than the required `id`; the one-screenshot visual budget was not retried. Structural evidence is complete, but this is not a visual screenshot pass.

Historical execution evidence — not the current recovery pointer; use [`../../RECOVERY.md`](../../RECOVERY.md) for re-entry:
- Project: AURELIA
- Page: `/about`
- Framer session: `2`
- New image nodes: Exterior `v0qZgOE0o`; Cooking heading `Xy6oXk5Oe`; cooking copy `UE3f6RSpP`; food plating `QgFfDTzGN`; handheld dish `xjuK86y8N`.
- Final readback: direct Section order is Opening → Exterior → Statement → Working Method → Cooking → Relationships; outer gap is `0px`; no About Handoff node remains. Desktop and Tablet Section rects are sequential with no gaps or overlaps. Phone explicitly uses 219px exterior, 233px food-plating, and 280×419px handheld-dish frames.
- Typography polish: Opening notice, Method description, Cooking description and Relationships description now use the same Inter 600 / 14px / -0.015em / 1.2em treatment as Menu `Changing Menu Story Columns`. Method and Cooking now use a 58%-width headline plus compact story column; Relationships keeps its separate wide-heading / right-aligned narrative ending.
- Next safe action: if a visual screenshot pass is required later, begin a new Image Review Plan and request the single target with the Framer screenshot `id` parameter; do not alter the completed structure first.
