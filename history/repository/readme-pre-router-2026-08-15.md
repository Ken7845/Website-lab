# Website-lab

Website-lab 是面向 AI Agent 的网站设计与交付系统，不只是灵感和文件仓库。

目标是让 Agent 在读取明确输入后，按照同一条质量链完成 Section、Page 或完整网站，使第一次交付已经符合 Baseline，最终 Polish 只处理细节。

## 系统结构

```text
AGENTS.md
├── 仓库级协作、授权与读取路由
├── content-library/
│   ├── 项目事实、品牌、内容、素材与 PROJECT.md
│   └── project-manifest-template.md
├── inspiration/
│   └── 按网站类型整理的创意参考
├── skills/taste-skill/
│   └── 基础设计质量与反模板化标准
└── framer/basic/
    ├── standards/
    ├── patterns/
    └── workflows/
```

## Agent 入口

1. 阅读 `AGENTS.md`。
2. 读取当前项目的 `content-library/<project>/PROJECT.md`。
3. 按 `PROJECT.md` 指向读取品牌、内容、素材和 Inspiration。
4. Framer 任务读取 `framer/basic/README.md`，按任务加载最少必要规则。
5. 使用 `framer/basic/workflows/build-checklist.md` 执行，不把基础能力留给最终 Polish。
6. 使用 `framer/basic/workflows/preflight-audit.md` 验收后再报告完成。

## 开始一个新网站：你需要做什么

### 1. 创建项目资料夹

```text
content-library/<project-name>/
```

复制 `content-library/project-manifest-template.md` 为项目的 `PROJECT.md`。

### 2. 提供必须由你决定的输入

- 网站目标和目标用户。
- 页面列表或业务上必须表达的内容。
- 主要 CTA：购买、预约、到店、联系、询价等。
- 品牌方向、喜欢和不喜欢的感觉。
- 正式事实：地址、价格、营业时间、联系方式、人员和授权。
- 正式文案、图片和可用素材。
- Inspiration 及你对参考的具体感受。
- 明确必须使用和明确不要使用的功能。

不完整的事实标记为 `Missing`，不要为了让资料看起来完整而猜测。

### 3. 只确认真正影响方向的选择

Agent 会先汇总：

- 对项目目标的理解。
- Sitemap 与页面目的。
- 视觉和系统方向。
- 关键 Framer Patterns。
- Missing / Blocked 内容。

你只需要确认会改变品牌、信息架构或主要交互的选择。已经授权的搭建、响应式、SEO、Alt、链接和 QA 不需要逐项确认。

## Agent 会自动做什么

### 开工前

- 检查 `PROJECT.md` 是否达到 Definition of Ready。
- 读取 Brand Voice、Style Guide、内容、素材和相关 Inspiration。
- 从 Framer Basic 选择最少必要标准、Pattern 和 Workflow。
- 列出当前 Scope 和明确不做的内容。

### 搭建时

- 先建立最小 Text Styles、Color Styles、Buttons、Navbar、Footer 和 Layout Template。
- 按 Section/Page 纵向完成视觉、Styles、Components、Links、Heading、Alt、Responsive 和 Motion。
- 对常见需求直接使用 Pattern Recipes，不临场试错。
- 同类修改批量完成，不拆成大量重复调用。
- 更新 `PROJECT.md` 的 Build Status Matrix 和 Recovery State。

### 完成前

- 对当前 Scope 执行 Preflight Audit。
- 检查 320、390、810、1200、1440+ 的必要行为。
- 在 Preview 中真实测试关键路径。
- 批量修复具体问题，只复测受影响路径。
- 报告 Pass、Fix Required 或 Blocked，不用“差不多完成”。

## 协作流程

```text
你提供目标、事实、素材与审美方向
→ Agent 检查 Ready 并整理方案
→ 你确认重大方向
→ Agent 按 Baseline 纵向搭建
→ Agent 执行 Preflight 与 Preview
→ 你进行最终主观审美检查
→ 你确认后发布
```

## 不同 Scope 使用同一条质量链

- 做一个 Section：该 Section 必须同时完成 Styles、Links、Alt、Responsive 和 Motion。
- 做一个 Page：该 Page 还必须完成 Metadata、H1/H2、Navbar/Footer 路径和 Preview。
- 做完整 Website：再完成全局系统、全部页面矩阵、性能、可访问性和交付要求。

Scope 可以不同，Baseline 不会因为任务较小而被遗忘。

## 你不需要提前解决的技术问题

以下默认由 Agent 根据 Website-lab 规则处理：

- Text/Color Style 结构。
- Component、Variant、Property 和 CMS 决策。
- Desktop、Tablet、Phone 转换。
- Metadata、Heading、Alt 和链接协议。
- Navbar、Overlay、Lightbox、Hover 的原生模式。
- Preflight、状态记录和 reconnect 恢复。

只有这些选择会改变品牌、内容事实、成本或主要体验时，Agent 才需要再次询问。

## 完成的定义

网站完成不是“截图看起来不错”，而是同时满足：

- 视觉与品牌方向成立。
- 内容真实且转化路径清楚。
- Text/Color Styles、Components 和 Variants 可维护。
- Desktop、Tablet、Phone 均成立。
- 动效和交互使用合适的原生模式。
- Metadata、Heading、Alt、Links 和 Accessibility 完整。
- 关键交互在 Preview 中真实验证。

详细标准见 `framer/basic/standards/website-baseline.md`。

## 核心原则

```text
完整输入
→ 固定建设顺序
→ 已验证默认模式
→ Section / Page / Website 三层验收
→ 自动化或结构化 Preflight
→ 一次 Preview 路径
→ 交付
```

规则的价值不是让 Agent 读更多，而是减少临场猜测、重复检查和返工。

## 技术与工具

- Framer
- Codex
- GitHub
- ChatGPT
