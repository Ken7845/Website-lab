# Goal

在这个网站我希望用一种静谧、艺术性、简约的语言展示个人摄影作品、网站设计作品以及 musings。

首页由 Hero、Works、Musings、About 组成。首页负责建立气氛和提供入口，不承担完整作品归档。

## Canonical Works hierarchy

Works 是全部作品的总入口，分为两个一级类别：

```text
Works
├── Observation
│   ├── Fighting the Chemistry
│   ├── Campus
│   ├── Golden Moment
│   └── Shadow
└── Creation
    └── 每一个独立的网站项目
```

层级含义：

- `Works` 是作品总索引页，不是单个作品。
- `Observation` 是摄影作品集类别。
- `Creation` 是网站设计作品集类别。
- `Fighting the Chemistry`、`Campus`、`Golden Moment`、`Shadow` 都是独立的 Observation 作品。
- Creation 下的每一个网站也都是独立作品。
- 每一个独立作品都需要自己的详情页，展示完整内容、图片顺序、文字和下一作品入口。
- `/fighting-the-chemistry` 是单个作品详情页的现有例子，不是 Observation 分类页。

Works 页面采用两个可滚动叠放的档案袋来表达 Observation 和 Creation。档案袋默认只列作品名称，不在封面直接铺开具体作品内容。桌面端悬浮作品名称时显示封面图或主要作品与简短介绍；移动端用点击展开代替 hover。
