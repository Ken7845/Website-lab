# Framer Preflight Audit

在报告 Section、Page 或 Website 完成前执行。目标是抓取结构性遗漏，不重新设计已经成立的页面。

## 审查原则

- 先自动或结构化检查，再直接审阅当前画布或目标截图的静态平面结果；不要把浏览器 Preview 当作默认审查步骤。
- 只检查当前范围及其共享依赖。
- 发现问题按同类批量修复，不逐项来回调用。
- Warning 需要判断设计意图；Error 和本轮新增问题必须解决。
- 审查输出使用 Pass / Fix / Blocked，不使用模糊的“差不多”。
- 审查按风险分级。Rename、文案、Link 和 Property 修改以结构回读为主；静态视觉、布局和断点由 Agent 直接审阅目标画布/截图并结合目标节点读回；高级动效、Cursor、Hover、Variant 组件先验证事件图、目标、状态与尺寸，再按 [Evidence selection](image-workflow.md#evidence-selection) 检查必要 runtime 路径；路径不可用时可请求 focused user confirmation，未验证部分保持 Blocked。
- 不为同一结论重复使用全页截图、节点截图、浏览器截图和原图查看。一条权威证据足够时立即停止。
- Component / Section 范围不升级为全站审查；共享依赖只查受影响实例。

## 1. Content and Facts

- [ ] 无 Lorem Ipsum 和未说明占位文案。
- [ ] 地址、价格、营业时间、联系方式与 `PROJECT.md` 一致。
- [ ] Draft、Demo 和 Missing 状态没有被误当成 Approved。
- [ ] 虚构品牌保留 Demo 声明。

## 2. Page Semantics

逐页检查：

- [ ] Page Title 唯一。
- [ ] Meta Description 独立。
- [ ] 只有一个主要 h1。
- [ ] h2/h3 层级与内容关系一致。
- [ ] favicon 与 Open Graph 已设置。
- [ ] 页面路径清晰，无 Draft 页面被正式导航引用。

## 2A. Visual Composition and Cross-page Differentiation

当 scope 命中 Visual Direction Contract 时：

- [ ] Design Read 与当前品牌、页面目的和用户行动一致。
- [ ] Preserve 项没有被“为了不同”而破坏；Transform 项确实改变了内容需要的构图责任。
- [ ] 全站 layout-family distribution 有可解释的重复与变化：Contact / CTA / Form 等同职责区域可以一致，但所有 sibling pages 没有机械复用同一 Hero 或完整 Section/layout-family sequence 而形成 site-wide layout monoculture；未用“每个 Section 必须不同”的数量配额制造无意义变化。
- [ ] 每个 Section 有明确 focal point、比例、密度、留白与进入下一段的过渡，不是平均化容器。
- [ ] Colour rhythm 使用批准的 palette roles，但页面之间不是同一 dark / light / accent 序列的机械复刻。
- [ ] Asset map 与实际 Fill、Alt、crop、breakpoint 使用一致；每张图片支持分配给它的 content-relative image role，复用和遗漏均有理由，不能只因尺寸或色调方便而替换叙事不相关的素材。
- [ ] 一张高效 full-page 或 compiled Desktop/Phone evidence 足以证明整体节奏；Section screenshot 不冒充整页证据。

输出分别记录 `Structural status` 与 `Visual status`。命令成功、clean diagnostics 或结构 readback 不能单独让 Visual status 通过。

## 3. Images

- [ ] 所有信息性图片有 Alt。
- [ ] 所有装饰图片显式空 Alt。
- [ ] 不存在 Alt 未定义。
- [ ] 没有直接上传不必要的超大原图。
- [ ] Desktop/Tablet/Phone 裁切保留核心信息。
- [ ] 没有地图 UI、黑块、控件或截图痕迹。

## 4. Links and Conversion

- [ ] Logo → `/`。
- [ ] Navbar 与 Footer 所有项目有真实链接。
- [ ] Primary/Secondary CTA 有真实目标。
- [ ] Phone 使用 `tel:`。
- [ ] Email 使用 `mailto:`。
- [ ] Address 使用地图链接。
- [ ] Social 使用真实外部链接。
- [ ] 无空链接、无无关锚点、无未存在页面目标。

## 5. System

- [ ] 核心排版使用 Text Styles。
- [ ] 核心颜色使用 Color Styles/Variables。
- [ ] Navbar、Footer、Buttons 使用共享 Components。
- [ ] Variants 表达状态/结构，不表达不同内容。
- [ ] 项目行和卡片使用单一模板组件；内容、Fill、Link 与 Cursor 在 Instance 层设置。
- [ ] 无 `Variant 2`、`Frame 23`、`Stack 1` 等默认命名。
- [ ] Component instances 的 Variant、Properties、Links 和 Effects 正确。

## 6. Responsive Matrix

最低宽度：320 / 390 / 810 / 1200 / 1440+

- [ ] Navbar 完整且不拥挤。
- [ ] Heading 换行自然。
- [ ] 邮箱、价格、日期、metadata 不破坏布局。
- [ ] Grid/Row 在 Phone 转换合理。
- [ ] CTA 易于点击。
- [ ] 无横向溢出。
- [ ] Page root、full-bleed Section 与 senior structural parent 保持 Fill / `1fr`；`max-width` 位于 deepest valid max-width owner。若存在 bounded-canvas exception，能证明它已获批准、外层背景仍覆盖视口且窄屏/宽屏均成立。
- [ ] 图片焦点与内容顺序合理。
- [ ] Footer 留白、列数与阅读顺序合理。

## 7. Motion and Interaction

- [ ] Sticky Navbar 工作。
- [ ] Scroll direction behavior 工作（项目使用时）。
- [ ] Phone Menu 可打开、关闭并导航。
- [ ] Lightbox 可打开、关闭且尺寸克制。
- [ ] Hover 不推开布局或被 clip。
- [ ] Overlay/Lightbox 不出现生硬闪现。
- [ ] Focus 与触控路径可用。
- [ ] Reduced Motion 不破坏内容与导航。

## 8. Performance and Delivery

- [ ] 图片尺寸与容器匹配。
- [ ] 没有无意义 Custom Code、动画或重复 Components。
- [ ] 没有私人信息、测试链接和未授权素材。
- [ ] Marketplace 项目的 Demo、Remix、Preview 和授权材料完整。

## 9. Targeted Preview Paths

只执行与项目相关的路径：

- Desktop：Home → Navbar → Primary CTA → Contact/Visit。
- Phone：Menu Open → Close → Open → Core Link。
- Gallery：Thumbnail → Lightbox → Close。
- Contact：Phone / Email / Map / Social。
- Footer：Page Link / CTA / External Link。

每条路径成功一次即可。发现具体错误后修复并只复测受影响路径。

验证工具由 [evidence selection](image-workflow.md#evidence-selection) 决定。nonvisual 修复以 readback 为主；static scope 用适当截图；runtime claim 要一次必要 Preview 或已完成的 focused user confirmation。不可用的 required path 保持 Blocked，不能靠设置或请求确认宣称 Pass。

## 10. Audit Output

```markdown
# Preflight Result

Scope: Section / Page / Website
Status: Pass / Fix Required / Blocked
Structural status: Pass / Fix Required / Blocked
Visual status: Pass / Fix Required / Blocked / N/A — reason

## Pass
- ...

## Fix Required
- [Category] Issue → planned batch fix

## Blocked
- Missing fact/content/permission

## Verified
- Widths:
- Preview paths:
- Shared components:
```

不得以高视觉分抵消缺失链接、语义、Phone 导航或未完成页面。
