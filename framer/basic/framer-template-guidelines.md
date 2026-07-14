# Framer Template 制作规范

本文档定义 Framer Marketplace 模板的设计、结构和发布标准。

目标：

创建的模板必须满足：

- 高质量视觉表现
- 明确的品牌定位
- 良好的可编辑性
- 清晰的结构
- 优秀的响应式体验
- 可以被真实用户直接使用

一个 Marketplace Template 不只是一个漂亮的网站。

它应该是一个：

> 可复用、可修改、可交付的设计产品。


---

# 1. 模板核心理念

每一个模板都应该服务于明确的用户和场景。

开始制作前必须明确：

- 目标用户是谁
- 适合什么行业
- 解决什么问题
- 用户访问网站后的目标行为是什么


避免制作：

❌ 泛化的网站模板

例如：

"Modern Business Website"


应该变成：

✅

"为独立咖啡店展示品牌故事、菜单和到店信息的网站模板"

"为摄影师展示作品和获取客户的网站模板"


---

# 2. 创意方向要求（避免模板感）

模板不能只是：

更换图片 + 修改颜色 + 替换文字。


每个模板开始制作前，需要明确：

## Brand Direction

包括：

- 品牌人格
- 核心概念
- 故事方向
- 视觉隐喻
- 排版方向
- 图片策略
- 动效语言


模板必须拥有至少一个令人记住的设计特点。

例如：

- 独特的 Hero 构图
- 特殊的滚动体验
- 编辑杂志式布局
- 沉浸式图片展示
- 独特的信息叙事方式


避免：

- 标准 Hero + Card + Story + CTA 模板结构
- 复制已有模板布局
- 只改变颜色和字体


---

# 3. 网站结构规范

每个页面必须有明确目的。

## 首页 Home

目标：

介绍品牌，引导用户行动。


常见结构：

```
Navigation

Hero

Brand Introduction

Featured Content

Products / Services

Story Section

Gallery

Testimonials / Social Proof

Contact / Visit

Footer
```


注意：

不要机械使用固定结构。

页面顺序应该根据品牌故事决定。


---

## About 页面

目标：

建立信任。


可以包含：

- 品牌故事
- 创始人
- 制作过程
- 品牌理念
- 团队介绍


---

## Products / Services / Menu 页面

目标：

清晰展示内容。


要求：

- 使用可复用 Card
- 使用 CMS（如果适合）
- 保持统一结构


例如：

餐厅：

```
Menu Items

Categories

Reviews
```


作品集：

```
Projects

Categories

Case Studies
```


---

## Contact / Visit 页面

目标：

促进用户行动。


应该包含：

- 联系方式
- 地址
- 营业时间
- 地图
- CTA


---

# 4. Component 组件规范

模板必须具有良好的组件结构。


应该创建：

```
NavigationBar

HeroSection

ProductCard

ProjectCard

GalleryGrid

FooterSection
```


组件应该：

- 可复用
- 易修改
- 保持一致


避免：

- 重复复制相同结构
- 每个页面单独制作相同组件
- 难以修改的布局


---

# 5. Framer Layer 命名规范

禁止保留默认名称：

```
Stack

Stack 1

Frame

Frame 1

Text

Container
```


所有 Layer 必须语义化。


正确：

```
Hero Section

Hero Container

Hero Content Stack

Hero Heading

Primary CTA Button
```


错误：

```
Stack

Frame 23

Text Copy
```


详细规则参考：

framer-layer-naming.md

---

# 6. Typography 字体规范

模板必须具有清晰的视觉层级。


定义：

- 大标题
- Section 标题
- 正文
- Caption
- Label


要求：

- 字体搭配统一
- 标题层级明确
- 行距合理
- 阅读舒适
- 如果是延续已有页面风格，必须先读取参考节点的真实字体属性，再同步到新页面


避免：

- 随意改变字体大小
- 过多字体组合
- 不一致的文本样式
- 凭截图感觉替换字体，导致同一网站的大标题系统断裂


---

# 7. Layout 布局规范

布局应该具有设计逻辑。


要求：

- 清晰视觉层级
- 统一间距系统
- 平衡留白
- 合理使用 Grid 和 Stack


避免：

- 随机 padding
- 过度规则化布局
- 所有 Section 都使用同一种结构


优秀模板应该：

简单修改内容后仍然保持高级感。


---

# 8. Responsive 响应式规范

模板必须支持：

- Desktop
- Tablet
- Mobile


不能只是缩小桌面版本。


## Desktop

关注：

- 大图表现
- 空间感
- 排版比例


## Tablet

检查：

- 布局是否自然变化
- 内容是否拥挤


## Mobile

检查：

- 字体可读性
- 按钮大小
- 图片比例
- 内容顺序
- 数字、标题、metadata 是否互相重叠
- 桌面端的 row/grid 是否在手机端改成合适的 stack 或隐藏次要信息


禁止：

- 横向溢出
- 过小文字
- 拥挤布局


---

# 9. Motion 动效规范

详细规则参考：

motion-design.md


---

# 10. 图片和素材规范

图片是模板质量的重要组成。


要求：

- 高质量
- 风格统一
- 符合品牌
- 适合网页加载


避免：

- 随机 Stock 图片
- 风格不一致图片
- 未压缩的大文件


图片应该：

服务品牌故事，而不是简单填充空间。

## 图片比例与外框规则

如果图片内容完整度比统一格子更重要：

- 让图片按原始比例响应宽度。
- 让外框、边框、阴影跟随图片一起等比例变化。
- 使用 `height: fit-image` 或等效的原比例策略。
- 不要把图片 `cover` 到固定 holder 中再用外框遮裁。

如果是作品集、摄影、案例封面，优先保护内容完整度。

如果是装饰图、背景图、统一卡片矩阵，才考虑固定比例裁切。


---

# 11. CMS 内容规范

适合重复内容时应该使用 CMS。


例如：

餐厅：

```
Menu Items

Gallery

Reviews
```


作品集：

```
Projects

Articles

Categories
```


CMS 要求：

- 字段命名清晰
- 删除无用数据
- 默认内容完整
- 用户容易替换


---

# 12. SEO 和可访问性规范

模板需要考虑真实商业使用。


SEO：

检查：

- 页面标题
- Description
- Heading 层级
- 图片 Alt Text


Accessibility：

检查：

- 颜色对比度
- 按钮明确
- 字体大小合理
- 表单标签完整


---

# 13. 性能规范

发布前检查：

- 图片大小
- 页面加载速度
- 动画数量
- 不必要组件


避免：

- 超大图片
- 过多动画
- 无意义代码


---

# 14. 用户编辑体验

Marketplace 用户购买模板后，需要能够快速修改。


要求：

- Layer 命名清晰
- 内容位置明确
- Component 结构合理
- 样式统一


目标：

用户应该感觉：

> "我购买后可以快速改成自己的品牌。"


而不是：

> "我需要重新设计整个网站。"


---

# 15. 发布前检查清单

## 设计

□ 有明确设计概念

□ 不像普通模板

□ 有独特视觉记忆点

□ 排版统一

□ 图片质量高


## 结构

□ Layer 命名规范

□ Component 可复用

□ 页面结构清晰

□ CMS 设置正确


## 响应式

□ Desktop 检查

□ Tablet 检查

□ Mobile 检查


## 内容

□ 无 Lorem Ipsum

□ 无占位文字

□ 无未完成区域


## 发布准备

准备：

- 模板名称
- 模板介绍
- 分类
- Preview 图片
- Demo 链接
- Remix 链接


---

# 最终目标

一个优秀的 Framer Marketplace Template 应该同时满足：

视觉上：

> 像一个真实品牌网站。


结构上：

> 像一个专业设计系统。


使用上：

> 买家可以快速修改并投入使用。


不要制作一个"展示 AI 能力的网站"。

要制作一个：

> 可以被真实用户购买和使用的设计产品。
