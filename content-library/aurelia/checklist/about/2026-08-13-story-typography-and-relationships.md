# About Story Typography and Relationships — 2026-08-13

Page: About  
Path: `/about`  
Status: Completed — Canvas revision read back  
Parent page contract: [About Page Checklist](./about.md)

## 原始要求（逐字记录）

1，算了，我觉得应该明确一下字体的分配，这个小字负责长篇内容，而不是副标题引导，修改一下，把引导换成原来的小字，然后故事内容就用这个小小字，还有把这个小小字做成可以直接引用的style，2，Working Method Section，Relationships Section的小字故事太短，长一些，要讲故事，3，Relationships Section部分的故事讲述要详细，把两张图片上下分开，用文字和故事来承接，故事要具体要长。修完checklist直接开始执行

## 执行细化与验收

### 1. 明确字体职责并建立可引用 Style

- [x] 将当前用于长篇故事的 Inter 600 / 14px / -0.015em / 1.2em 小小字建立为语义化、可直接引用的 Text Style；不得只保留在单个节点的直接样式中。
- [x] 将现有 Opening 与 Statement 的引导文字换回本轮改动之前的原有小字角色与样式；该角色不再承担长篇故事。
- [x] 将 Working Method、Cooking 与 Relationships 的故事正文改为引用新的故事小字 Style，并在 Desktop、Tablet、Phone 回读其继承或 override。

### 2. 扩写 Working Method 与 Relationships 的故事

- [x] 在不编造厨师、产地、奖项、团队、服务流程或运营事实的前提下，将 Working Method 的 Demo 故事扩展为具体、连续的叙事，而非副标题式引导。
- [x] 在不编造事实的前提下，将 Relationships 的 Demo 故事扩展为具体、较长的文化叙事，清晰写出厨房、房间与客人如何共同形成一晚的节奏。
- [x] 保持 Heading、故事文本的阅读层级与可读 measure；长文不得靠缩小字体或绝对定位塞入。

### 3. Relationships 的双图与故事承接

- [x] 检索当前 About 与内容库图片使用位置，选择两张叙事角色不同且不造成无意义重复的现有图片。
- [x] 将 Relationships 的两张图片上下分开，使用文字与长故事在阅读顺序中承接，不做并列图库或无说明装饰。
- [x] 每张图保留明确 Alt、内容完整性与跨断点比例；图片和文字的顺序在 Phone 保持自然阅读流。

## Latest Part Result

Scope: typography-role reset, reusable story Style, Working Method and Relationships narrative expansion, Relationships image/story sequence  
Status: Completed — all requested typography, narrative and Relationships sequence work read back

Image Review Plan:

- Exact target: one Framer screenshot of Desktop `Relationships Middle Copy`.
- Question: whether the new reusable Story type remains legible as a continuous two-paragraph narrative at its intended Desktop measure.
- Evidence chain: one targeted node screenshot only. The two new interior images are verified through resident source files, 3:2 source dimensions, explicit Alt, Framer Fill URLs and frame ratios; no original-image preview is needed in this Part.
- Budget: one screenshot request. If it fails, do not retry through another visual path; keep the structural readback as the verification record.

Pass:

- 用户明确要求本清单完成后直接开始执行，故未额外等待确认。

Historical execution evidence — not the current recovery pointer; use [`../../RECOVERY.md`](../../RECOVERY.md) for re-entry:

- Framer session: `2`
- Text Style: `Type/Story` (`CAbFL0Tw6`), Inter 600; Desktop/Tablet 14px, Phone 13px; separate responsive line-height and paragraph-spacing slots.
- Story nodes: Method `cBeqUGmlS`, Cooking `UE3f6RSpP`, Relationships opening `FUa7UYncZ`, middle `Sx2cZiWpG`, and closing `gAdVNJu1y` all reference `Type/Story`.
- Relationships media: private table `F4I8Ranoc` (720×480 Desktop) and table setting `XP_TaWjmI` (600×400 Desktop); both are 3:2 sources, have specific Alt, and become 1fr × 233px on Phone.
- Visual evidence: one Desktop `Relationships Middle Copy` screenshot passed for Story type legibility and paragraph rhythm. No full-page screenshot or publish was performed.

## Follow-up — Cooking story sequence

Status: Completed

- [x] Convert Cooking from an opening plus a parallel image pair to a long vertical story sequence matching the Relationships approach.
- [x] Keep the existing food-plating and handheld-dish images, place them separately between story movements, and preserve their content-respecting ratios.
- [x] Keep all Cooking stories on `Type/Story`, with Tablet and Phone changing to a natural single-column reading order.

Image Review Plan:

- Exact target: one Framer screenshot of Desktop `Cooking Middle Copy`.
- Question: whether the Story text is legible at its intended reading measure after the image pair was separated.
- Budget and fallback: one targeted screenshot only; if unavailable, retain the targeted node-tree, Style, Alt and responsive-dimension readback.

Visual result:

- One Desktop `Cooking Middle Copy` screenshot passed. The two paragraphs retain legible line length and paragraph rhythm in `Type/Story`; no full-page screenshot or publish was performed.

Historical follow-up evidence — not the current recovery pointer; use [`../../RECOVERY.md`](../../RECOVERY.md) for re-entry:

- Cooking order: heading and opening story → food-plating image → middle story → handheld-dish image → closing story.
- Desktop: food plating is 720×480; handheld dish is 400×599. Tablet preserves 600×400 and 340×509 respectively. Phone uses single-column story flow with 1fr × 233px food plating and 280×419 handheld dish.
