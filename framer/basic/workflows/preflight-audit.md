# Framer Preflight Audit

在报告 Section、Page 或 Website 完成前执行。目标是抓取结构性遗漏，不重新设计已经成立的页面。

## 审查原则

- 先自动或结构化检查，再进行少量视觉 Preview。
- 只检查当前范围及其共享依赖。
- 发现问题按同类批量修复，不逐项来回调用。
- Warning 需要判断设计意图；Error 和本轮新增问题必须解决。
- 审查输出使用 Pass / Fix / Blocked，不使用模糊的“差不多”。
- 审查按风险分级。Rename、文案、Link 和 Property 修改以结构回读为主；视觉、布局和断点修改追加一次目标截图；交互修改追加一次关键 Preview 路径。
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

可以省略 Preview 的情况：纯命名、无视觉变化的文案替换、已结构确认的 Link/Property 修正。不能省略 Preview 的情况：本轮新增或修改 Hover、Cursor、Overlay、Scroll、Lightbox、Form 状态或真实导航行为。

## 10. Audit Output

```markdown
# Preflight Result

Scope: Section / Page / Website
Status: Pass / Fix Required / Blocked

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
