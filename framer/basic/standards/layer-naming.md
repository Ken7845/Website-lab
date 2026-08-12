# Framer Layer 命名规范

本规范用于 Framer 项目的 Layer Tree 命名。

目标：

- 保持 Framer 页面结构清晰
- 方便后续维护和修改
- 让 AI Agent 能理解页面结构
- 避免出现大量 Stack、Frame、Text 导致无法定位


---

# 核心原则

## 0. 简洁、清楚、有区分度

Layer 名称应使用“在当前父级语境中仍能准确定位”的最短表达。

- 优先 1–3 个清楚单词；只有真实职责需要时才增加 `Section`、`Row`、`Grid`、`Image` 等类型。
- 父级已经提供语境时，不重复祖先前缀。
- 同级 Layer 必须有区分度；不同父级允许复用 `Image`、`Copy`、`Content` 等短名称。
- 不把整条层级路径塞进一个名称，也不连续重复项目名、Section 名或内容类别。
- Scroll Target 是例外：名称必须与真实 `elementId` 完全一致，即使它不符合普通语义命名格式。

推荐：

```text
Creation
├── Painting Continuum
│   ├── Doctrine of the Mean
│   │   ├── Image
│   │   └── Copy
│   └── Depth
│       ├── Image
│       └── Copy
└── Digital Form
    └── Website Covers
```

避免：

```text
Creation Section
└── Creation Painting Continuum Section
    └── Creation Painting Continuum Doctrine of the Mean Artwork Row
        ├── Creation Painting Continuum Doctrine of the Mean Artwork Image Frame
        └── Creation Painting Continuum Doctrine of the Mean Artwork Copy Stack
```

判断顺序：

1. 在同级中能否唯一识别。
2. 父级是否已经说明语境。
3. 删除重复前缀后是否仍然清楚。
4. 类型后缀是否真的帮助定位。

## 1. 禁止使用 Framer 默认名称

不要保留：

```
Stack
Stack 1
Stack 2

Frame
Frame 1

Text
Text 1

Rectangle
Group
Container
```

这些名称无法表达功能。


应该改成：

```
Hero Section

Product Grid

Footer Content

Navigation Bar
```


---

# 2. 命名原则

缺少父级语境时使用：

```
功能 + 类型
```

例如：

```
Hero Section

About Section

Product Card

Gallery Grid

Footer Section
```


不要使用：

```
Big Area

Top Part

Middle Content

Image Block
```


---

# 页面整体结构命名

每个页面建议保持：

```
Page

├── Navigation Bar

├── Hero Section

├── Content Sections

├── CTA Section

└── Footer Section
```


示例：

```
Home Page

├── Navigation Bar

├── Hero Section

├── Featured Works Section

├── About Section

├── Contact Section

└── Footer Section
```


---

# Section 命名规则

Section 是页面主要内容区域。

格式：

```
内容主题 + Section
```


Examples:

```
Hero Section

About Section

Featured Products Section

Gallery Section

Testimonials Section

Visit Section

Contact Section

Footer Section
```


避免：

```
Section 1

Section 2

Content Section

New Section
```


---

# Stack 命名规则

Stack 表示布局结构。

不要：

```
Stack

Stack 1

Stack 2
```


根据用途命名。父级已说明主题时只保留当前层职责，不重复父级名称。


## 垂直布局 Stack

Examples:

```
Hero Content Stack

Text Content Stack

Product Information Stack

Footer Content Stack

Navigation Links Stack
```

在明确父级内可以简化：

```text
Hero
├── Content
└── Image

Footer
├── Navigation
└── Legal
```


## 水平布局 Stack

Examples:

```
Navigation Links Row

Social Links Row

Product Cards Row

Footer Columns Row
```


---

# Container 命名规则

Container 用于控制内容宽度。


不要：

```
Container
Container 1
```


使用：

```
Page Container

Hero Container

Content Container

Section Container

Footer Container
```


结构示例：

```
Hero Section

└── Hero Container

    ├── Hero Content Stack

    └── Hero Image Frame
```


---

# Frame 命名规则

Frame 通常用于：

- 图片区域
- 卡片区域
- 背景区域
- UI 容器


格式：

```
用途 + Frame
```


Examples:


图片：

```
Hero Image Frame

Product Image Frame

Gallery Image Frame

Background Image Frame
```


卡片：

```
Product Card Frame

Review Card Frame
```


按钮：

```
CTA Button Frame

Primary Button Frame
```


---

# Text 命名规则

不要：

```
Text

Text 1

Heading

Paragraph
```


根据用途命名。


## 标题

```
Hero Heading

Section Heading

Card Heading

Footer Heading
```


## 正文

```
Hero Description

Section Description

Product Description

Body Text
```


## 小文字

```
Eyebrow Text

Caption Text

Label Text
```


---

# Button 命名规则

不要：

```
Button

Button 1
```


使用：

```
Primary CTA Button

Secondary CTA Button

Explore Button

View Project Button

Contact Button

Book Now Button
```


---

# Image 命名规则

不要：

```
Image

Image 1
```


使用：

```
Hero Background Image

Product Image

Gallery Image

Portrait Image

Logo Image
```


---

# Card 命名规则

格式：

```
内容 + Card
```


Examples:

```
Product Card

Project Card

Review Card

Service Card

Blog Card
```


Card 内部结构：

```
Product Card

├── Product Image Frame

├── Product Content Stack

│   ├── Product Name

│   └── Product Description

└── CTA Button
```


---

# Grid 命名规则

Grid 用于重复内容。


Examples:

```
Product Grid

Project Grid

Gallery Grid

Review Grid

Card Grid
```


不要：

```
Grid 1

Grid 2
```


---

# Component 命名规则

Component 使用 PascalCase。


Examples:

```
NavigationBar

HeroSection

ProductCard

GalleryGrid

FooterSection
```


Variants：

```
Button / Primary

Button / Secondary

Hero / Desktop

Hero / Mobile
```


---

# 推荐完整 Layer Tree 示例


```
Home Page


├── Navigation Bar


├── Hero Section
│
│   ├── Hero Container
│   │
│   ├── Hero Content Stack
│   │
│   │   ├── Eyebrow Text
│   │   ├── Hero Heading
│   │   ├── Hero Description
│   │   └── Primary CTA Button
│   │
│   └── Hero Image Frame


├── Featured Products Section
│
│   ├── Section Heading
│   │
│   └── Product Grid
│
│       ├── Product Card
│       │
│       ├── Product Card
│       │
│       └── Product Card


├── Gallery Section


├── Visit Section


└── Footer Section

    ├── Footer Content Stack

    ├── Social Links Row

    └── Copyright Text
```


---

# AI Agent 操作 Framer 时遵守

1. 创建新的 Layer 后立即命名。

2. 不允许留下默认名称：
```
Stack
Frame
Text
Container
```

3. 修改已有页面时保持已有命名结构。

4. 新增 Section 必须使用语义化名称。

5. 优先通过 Layer 名称理解页面结构，而不是通过视觉猜测。

6. 保持 Layer Tree 能同时被设计师和 AI Agent 理解。

7. 命名使用最短可区分表达，不重复祖先前缀。

8. 批量重命名前先保护 Scroll Target：启用 `scrollTargetEnabled` 的 Frame 名称必须与 `elementId` 完全一致。


---

# 命名目标

优秀的 Framer Layer Tree 应该像网页结构说明：

```
Hero Section

└── Hero Content Stack

    ├── Hero Heading

    ├── Hero Description

    └── Primary CTA Button
```


而不是：

```
Stack

└── Stack

    ├── Text

    ├── Text

    └── Button
```


好的命名能够让未来的 AI Agent 更准确地定位、修改和扩展网站。
