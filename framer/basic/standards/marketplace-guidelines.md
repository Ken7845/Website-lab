# Framer Marketplace 附加规范

先满足 `framer/basic/standards/website-baseline.md`。本文档只包含 Marketplace Template 比普通网站额外需要的商品化和交付要求。

## 1. Template 定位

- 明确目标行业、目标买家和使用场景。
- 避免 “Modern Business Website” 这类泛化定位。
- 默认内容应该像真实品牌，而不是组件展示页。
- 至少有一个清楚的视觉记忆点。

## 2. 买家价值

买家应该能够：

- 快速找到品牌、Styles、Navbar、Footer、Buttons 和内容入口。
- 不重新设计即可替换字体、颜色、图片和正式内容。
- 通过 Properties、CMS 或 Fill 替换内容，而不是理解复杂 Variant 迷宫。
- 在内容变长、图片比例变化后仍保持稳定布局。

## 3. Productization

- Components、Variants、Properties 和 CMS 降低修改成本，而不是增加层级。
- Variant 名称描述状态和结构。
- 删除测试组件、无用字段、默认 Layer 名和未使用 Styles。
- 记录少量必要例外。
- 提供简短编辑说明。

## 4. CMS

当买家需要经常增删排序时优先 CMS，例如：Menu Items、Projects、Gallery、Reviews、Team 和 Articles。

验收：

- 字段命名清楚。
- 默认内容完整。
- 分类与排序可理解。
- 无测试字段和无用条目。
- 长标题、不同图片比例和缺失可选字段不会破坏布局。
- 编辑说明告诉买家从哪里修改。

## 5. 发布材料

- Template name
- One-sentence positioning
- Full description
- Category and target user
- Preview cover
- Desktop and Phone screenshots
- Demo URL
- Remix URL
- Editing instructions
- Image, font, icon and third-party licenses
- Fictional/demo content statement

检查：

- Demo 和 Remix 指向正确版本。
- Preview 与最终模板一致。
- 无私人信息、测试链接和未授权素材。
- 第三方组件没有不透明的账号或付费依赖。

## 6. Marketplace 评分

### Design Index

- Brand recognition
- Composition and hierarchy
- Typography and color
- Image strategy
- Content storytelling
- Motion quality

### Template Completeness

- Page/content completeness
- Responsive stability
- Components/Variants/Styles
- CMS/content expansion
- SEO and semantics
- Accessibility
- Conversion links
- Performance
- Delivery materials

判断：

- 90–100：成熟商品，可发布。
- 80–89：高质量，仍有少量发布前工作。
- 70–79：视觉或结构较好，商品化不完整。
- 60–69：可展示，不能作为成熟模板交付。
- 60 以下：核心结构或设计方向需要重做。

不能用高设计分掩盖低可编辑性、低可访问性或缺失发布材料。

## 7. Marketplace Done

- [ ] 普通 Website Baseline 已通过。
- [ ] 买家编辑路径清楚。
- [ ] Components/Variants/Styles/CMS 经过替换压力测试。
- [ ] Preview、Demo、Remix 与编辑说明完整。
- [ ] 授权和 Demo 声明完整。
- [ ] Template Completeness 达到发布目标。
