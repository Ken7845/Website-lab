# Morrow & Grain Bakehouse — 精简完善 TODO

目标：用最少的修改，把当前模板推进到可以放心展示和准备 Marketplace 发布的状态。

当前判断：

- 设计已经成熟，不需要重新设计页面。
- 优先修复影响导航、SEO、可操作性和模板交付的问题。
- 不为了追求理论上的满分，增加 CMS、表单、复杂代码或大量新组件。
- 每次只完成一个小阶段，完成后检查，再进入下一项。

---

# A. 下一步必须做

## 1. Phone Navbar 菜单 Overlay

本轮状态：已完成，并通过 390px Framer 交互预览检查。

- [x] 将 Phone Navbar 的 `Contact` 按钮改成 Menu 触发按钮。
- [x] 使用 Framer 原生 Relative Overlay 展开完整导航。
- [x] 导航包含 Home、Menu、About、Gallery、Visit、Contact。
- [x] Overlay 中保留 Contact 主 CTA。
- [x] 增加关闭按钮，并保留原生外部点击与键盘关闭行为。
- [x] 菜单面板使用轻微位移、缩放和透明度进入，不能直接闪现。
- [x] 动画保持简短自然，约 360ms。
- [x] 检查 390px Phone，不影响 Desktop 和 Tablet Navbar。

完成标准：Phone 用户无需滚动到 Footer，就能访问全部核心页面；菜单打开与关闭没有闪现、溢出或背景跳动。

## 2. 基础 SEO 与页面语义

不进行关键词研究，只补齐模板发布的基本结构。

- [x] 为 Menu、About、Gallery、Visit、Contact 添加独立 title 和 description。
- [x] 每个页面设置一个正确的 `h1`。
- [x] 主要 Section 标题按需要设置为 `h2`。
- [x] 设置 favicon 和一张全站 Open Graph 图片。

完成标准：六个页面都有独立 Metadata，每页只有一个主要 `h1`。

## 3. 图片 Alt Text

Gallery 的 20 张图片已经完成，不重复修改。

- [x] Home：补齐 7 张。
- [x] Menu：补齐 1 张。
- [x] About：补齐 4 张。
- [x] Visit：补齐 1 张。
- [x] Contact：补齐 1 张。

完成标准：信息性图片有简短描述；纯装饰图片明确使用空 Alt，不保留未定义状态。

## 4. Visit 与 Contact 链接

- [x] 电话设置 `tel:`。
- [x] 邮箱设置 `mailto:`。
- [x] Instagram 设置外部链接。
- [x] 地址设置地图链接。
- [x] 修正 Contact 页 Phone 邮箱的不自然断行。

完成标准：Visit、Contact 主体中的联系方式都可以直接操作，不只依赖 Footer。

---

# B. Marketplace 上架前值得做

这些任务有明显收益，但不要和 A 组同时开始。

## 5. 最小 Style System

- [ ] 只建立实际重复使用的 Text Styles：Display、Section Heading、Body、Caption、Label。
- [ ] 只建立核心颜色：Cream、Charcoal、Terracotta、Brown、Muted Text、Divider。
- [ ] 优先替换跨页面重复样式，不处理没有复用价值的个别例外。

## 6. 最小组件整理

- [ ] 将按钮中的 `Variant 2` 改成有意义的名称。
- [ ] 检查 Navbar、Footer 和 Button 的组件属性是否容易理解。
- [ ] Menu Item 只有在实际修改明显费时时，再做成组件。
- [ ] Gallery 保持当前原生 Lightbox，不创建 20 个图片 Variant。

## 7. 最终 QA

- [ ] 检查六页的 Desktop、Tablet、Phone。
- [ ] 点击测试 Navbar、Footer、CTA、地图、电话、邮箱和社交链接。
- [ ] 检查 sticky Navbar 的隐藏与出现。
- [ ] 抽查 Gallery Lightbox 的打开、关闭和过渡。
- [ ] 检查 Phone 是否有横向溢出或难看的文字断行。

## 8. 发布材料

- [ ] Preview 封面图。
- [ ] Desktop 和 Phone 预览图。
- [ ] Demo URL。
- [ ] Remix URL。
- [ ] 简短模板介绍和编辑说明。
- [ ] 保留虚构品牌声明。

---

# C. 暂不做

以下内容不是当前模板发布质量的主要瓶颈。除非后续真实需求证明有必要，否则不投入时间和 Token。

- [ ] 不创建复杂 CMS 系统。
- [ ] 不增加 Contact 表单。
- [ ] 不增加 Privacy 页面。
- [ ] 不为 Gallery 创建图片 Variant 或独立 Overlay。
- [ ] 不为 Reduced Motion 编写 Custom Code。
- [ ] 不重做已经稳定的 Desktop 页面设计。
- [ ] 不为了组件数量而组件化一次性 Section。

CMS 仅在以下情况再考虑：菜单需要频繁增删、排序，或模板测试者明确反馈静态菜单难以编辑。

Contact 表单仅在 Marketplace 审核或目标用户明确需要在线询价时再增加；目前可点击的电话和邮箱已经能形成有效联系路径。

---

# 推荐执行顺序

一次只做一项：

1. Phone Navbar Overlay
2. Metadata 与 Heading
3. Alt Text
4. Contact / Visit 链接
5. 最终 QA
6. 发布材料

完成前四项后先重新审查。只有审查结果表明 Styles 或组件编辑体验仍明显影响发布，再进入 B5、B6。
