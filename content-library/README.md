# Content Library

`content-library` 保存每个网站项目的事实、品牌、正式内容、素材和实施状态。Agent 不应依靠聊天记录重新推断这些信息。

## 每个项目的入口

新项目必须创建：

```text
content-library/<project-name>/PROJECT.md
```

使用同目录的 `project-manifest-template.md` 创建。`PROJECT.md` 是项目唯一入口，负责链接到其他资料，而不是复制所有内容。

## 推荐结构

```text
<project-name>/
├── PROJECT.md
├── BRAND_VOICE.md
├── STYLE_GUIDE.md
├── CONTENT.md
├── TODO.md
├── images/
└── references/
```

文件可以按项目需要减少，但 `PROJECT.md` 必须存在。

## 信息职责

- `PROJECT.md`：目标用户、页面、转化、状态、决策和资料索引。
- `BRAND_VOICE.md`：语气、词汇、禁用表达和文案示例。
- `STYLE_GUIDE.md`：项目视觉方向，不替代 Framer 全局 Baseline。
- `CONTENT.md`：已审核正式文案和结构化事实。
- `TODO.md`：尚未完成的项目工作，不重复全局 Checklist。
- `images/`：原始素材和明确命名的网页输出。
- `references/`：项目特定参考，不替代 `inspiration` 的类型级知识。

## 事实状态

重要内容应标记状态：

- `Approved`：可直接发布。
- `Draft`：可用于设计，但发布前需要审核。
- `Missing`：不能猜测，需要用户提供。
- `Demo`：虚构演示内容，必须保留声明。

地址、价格、营业时间、人员、联系方式和授权信息必须明确状态。

## 旧项目兼容

如果旧项目暂时没有 `PROJECT.md`：

1. 读取现有 brief、prompt、info、品牌和 TODO。
2. 先根据模板整理一个 `PROJECT.md`。
3. 标出无法确认的内容，不自行补全事实。
4. 后续任务统一从 `PROJECT.md` 进入。

不要长期让 Agent 每次从多个旧文件重新拼接项目状态。
