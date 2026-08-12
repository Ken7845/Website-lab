# Morrow & Grain Bakehouse — Framer Marketplace Template 建设任务

现在开始创建一个新的 Framer Marketplace 模板项目。

项目名称：

Morrow & Grain Bakehouse

这是一个虚拟品牌，用于展示网站设计能力和作为 Marketplace Template 发布。

---

# 第一阶段：理解项目背景

在开始任何设计和搭建之前，请先阅读：

1. AGENTS.md
2. Taste Skill
3. inspiration 文件夹中相关的餐饮网站的案例，重点阅读dutch-treat-restaurant这个案例的study-case和HANDOFF.md
4. 当前项目中的品牌资料info.md
5. 当前项目的图片资料。图片处理遵循 `../../framer/basic/workflows/image-workflow.md`。本项目图片为 AI 生成的四场景/四产品拼图，搭建前使用一个可恢复的批处理脚本完成一分四裁切，不改变图片内容，再生成网页输出版本
6. 主要参考的设计是balkan-bakery
7. 明确本次任务的要求：首次搭建同时完成视觉、Styles、Components、交互、响应式、语义和链接。执行顺序阅读 `../../framer/basic/workflows/build-checklist.md`，动效要求阅读 `../../framer/basic/patterns/motion-design.md`

理解以下关系：

Taste Skill：
- 是整个 website-lab 的底层设计审美规范
- 定义最低质量标准
- 不应该限制设计风格

Inspiration：
- 是高级设计参考
- 用于学习视觉语言、布局节奏、故事表达方式
- 不应该直接复制

品牌资料：
- 决定 Morrow & Grain 是什么品牌

图片素材：
- 是真实视觉资产，需要围绕它们构建故事。

---

# 品牌定位

品牌名称：

Morrow & Grain Bakehouse

品牌口号：

Baked slowly. Shared daily.

品牌类型：

Neighborhood bakery & coffee shop

定位：

一家现代社区烘焙店，受到欧洲传统烘焙文化启发，强调手工制作、季节食材以及日常生活中的温暖仪式感。

品牌关键词：

warm
crafted
honest
tactile
modern
welcoming


不要设计成：

- 奢侈甜品品牌
- 高端酒店餐厅
- SaaS 产品网站
- 过度商业化的连锁品牌

目标感觉：

“一个存在很多年的社区面包店，被附近居民熟悉和喜爱。”

---

# 图片素材规则

已经准备好的图片素材是网站主要视觉来源。

包括：

- 店铺环境
- 店铺外观
- 面包产品
- 甜点
- 咖啡饮品
- 烘焙过程

规则：

- 不重新生成图片
- 不使用 placeholder
- 不创造虚假的品牌 Logo
- 不在图片里添加文字
- 保持所有图片属于同一家真实店铺的感觉

图片应该承担 storytelling 的作用，而不是简单装饰。

---

# 网站目标

创建一个完整、高质量、可复用的 Framer Marketplace Template。

它应该展示：

- 强视觉叙事能力
- 本地商业网站设计能力
- 食品品牌表达能力
- 清晰的信息架构
- 移动端体验

目标用户：

- Bakery
- Cafe
- Coffee Shop
- Local Restaurant
- Small Business Owner

---

# 网站结构

创建以下页面：

Home

Menu

About

Gallery

Visit

Contact


---

# Home 页面叙事结构

首页不是简单展示模块，而应该像一个品牌故事。

## 1. Hero

目标：

第一眼让用户理解：

“这是一家怎样的店？”

包含：

- 大尺寸环境图片
- 品牌标题
- 简短介绍
- CTA


方向：

Headline:

Fresh from the oven, made for the neighborhood.

CTA:

View Menu

Secondary CTA:

Visit the Bakehouse


---

## 2. Featured Bakes

展示招牌产品。

使用产品卡片。

每个产品包含：

- 图片
- 名称
- 简短描述
- 价格（如果合适）


示例：

Country Sourdough

Butter Croissant

Seasonal Fruit Danish

Cinnamon Morning Bun


---

## 3. Brand Story

讲述品牌。

使用：

图片 + 文字

表达：

- 手工制作
- 慢发酵
- 每日新鲜烘焙
- 社区关系


不要写空泛品牌故事。

---

## 4. Menu Preview

展示菜单入口。

分类：

Bread

Pastries

Savory Bakes

Cakes & Sweets

Coffee & Drinks


不要设计成传统 PDF 菜单。

应该像一个精心策划的品牌体验。


---

## 5. Gallery

展示：

- 店内环境
- 制作过程
- 产品细节
- 日常氛围


避免：

普通重复图片网格。


---

## 6. Values

设计三个或四个品牌价值：

Made by Hand

Slow Fermentation

Seasonal Ingredients

Local Rituals


---

## 7. Visit Section

这是本地商业网站非常重要的转化区域。

包含：

- 地址
- 营业时间
- 联系方式
- 地图入口


目标：

让访客产生：

“我想去这家店。”

---

## 8. Footer

包含：

- 品牌名称
- 导航
- 联系方式
- 社交媒体
- Copyright


---

# 视觉设计方向

整体：

Editorial + Hospitality Website

颜色：

Cream paper

Warm brown

Muted terracotta

Charcoal


字体：

标题：
具有编辑感、有品牌气质

正文：
清晰、高可读性


避免：

- 过度动画
- 炫技效果
- 黑金高级餐厅风
- AI 生成网站感


---

# Framer 组件结构

创建可复用组件：

Navbar

HeroSection

FeaturedProducts

ProductCard

BrandStory

MenuPreview

MenuCategory

GalleryGrid

ValueCards

VisitSection

Footer


命名保持语义化。

---

# 响应式要求

Desktop：

保持编辑型布局，大图和留白。

Tablet：

保持视觉节奏。

Phone：

重新设计布局，而不是简单缩小 Desktop。

优先：

- 阅读体验
- CTA 转化
- 图片展示


---

# 工作流程

不要直接开始大量修改。

按照阶段执行：

Phase 1:
分析素材和项目结构。

Phase 2:
提出 sitemap 和页面结构。

Phase 3:
先完成 Home 页面。

Phase 4:
完成其他页面。

Phase 5:
整体 review：

检查：

- 品牌一致性
- 图片使用
- 响应式
- 组件复用
- Marketplace 发布质量


开始前，请先告诉我：

1. 你理解的品牌方向
2. 你准备如何组织页面
3. 你计划如何使用现有图片素材

确认后再开始搭建。
