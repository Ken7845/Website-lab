# AGENTS.md

## 项目定位

这是个人网站与独立站设计实验室，也是设计知识库。Agent 的角色是长期设计合作伙伴：理解品牌、保持设计语言一致，并把网站做成可操作、可维护和可交付的真实产品。

不要把仓库当成需要全部读取的资料库。按任务路由，只读取当前工作需要的内容。

## 开始任务前

### 设计与网站任务读取顺序

1. 阅读本文件，确认仓库级协作和内容边界。
2. 阅读根目录的 `SKILL.md`，获得基础设计质量、反模板化和交付检查标准。
3. 阅读当前项目的 `content-library/<project>/PROJECT.md`，再按其中链接读取 Brand Voice、Style Guide、内容和素材。
4. 如果旧项目没有 `PROJECT.md`，先用 `content-library/project-manifest-template.md` 整理入口；不要每次重新拼接多个旧文件。
5. 按项目类型读取相关 `inspiration`，理解创意方向，而不是平均化所有参考。
6. 如果任务涉及 Framer，先读 `framer/basic/README.md`，再按索引读取最少必要文件。
7. Framer 工作开始前阅读 `framer/checklist.md` 的“强制使用方法”和路由表；每完成一个 Part，必须重新打开对应 Checklist，检查、自我修补并复检后才能继续。

### 项目级 Checklist 的询问触发规则

当用户给出以下任一类型的具体项目 Prompt 时，在执行 Canvas、页面、组件、素材或其他正式建设操作前，必须先询问用户是否需要在知识库项目文件夹中创建或更新项目级 Checklist：

- 大项目总览、完整网站规划或多页面工作说明。
- 开工准备、实施顺序、阶段拆分或交付计划。
- 页面架构、叙事方向、创意构建或想法定稿。
- 会指导后续多轮、逐页或逐 Part 执行的整体方案。

询问保持简短，目的不是重新确认已经明确的设计方向，而是确认是否需要把方案沉淀为可逐项执行的文件。例如：`是否需要我先在 content-library/<project>/checklist/ 建立逐页 Checklist，再开始后续建设？`

- 用户确认需要时，先把已批准的总体方案写入 `content-library/<project>/PROJECT.md`，再按 `framer/checklist.md` 的“项目级 Checklist 文件夹规范”创建或更新 `content-library/<project>/checklist/`，完成后才进入正式建设。
- 用户明确不需要时，继续原任务，不擅自创建目录。
- 用户已经明确要求创建 Checklist 时无需重复询问，直接按规范执行。
- 项目已有 Checklist 时，询问应改为是否需要依据本次新总览更新现有 Checklist，不创建第二套平行目录。
- 小范围修改、单一修复、诊断、审阅和已经处于某一现有 Checklist Part 内的续接任务，不触发这次总览询问。
- Checklist 必须保存在知识库的项目目录，不放在临时工作区、Framer 项目旁的任意文件夹或聊天记录中。

图片与视觉审阅属于高风险步骤，优先级高于一般执行习惯。任何本地素材查看、Framer 截图或 Preview 截图开始前，必须先执行 `framer/basic/workflows/image-workflow.md` 的视觉预算、驻留检查和失败降级规则。图片审阅不得成为结构、文案、Styles、命名或 Breakpoint 工作的单点阻塞。

`taste-skill` 负责基础设计质量，`inspiration` 负责项目独特性。不要把 Skill 示例中的字体、框架、布局、色彩或动效当成所有项目的固定风格。

平台实现应使用当前平台原生能力。处理 Framer、Shopify 或其他平台时，保留设计判断，但不得为了套用上游示例更换技术栈。

## 内容边界

`content-library` 是品牌事实、正式文案和素材的主要来源。

- 优先使用用户提供的标题、文案、图片和页面结构。
- 新文案必须符合 `BRAND_VOICE.md`。
- 地址、价格、营业时间、联系人、产品事实等不可自行编造。
- 缺少事实信息时先询问；允许生成的展示性文案也要明确标记并等待审核。
- 不随意替换核心视觉素材。

编辑完成后，如需整理回 `content-library`，只保留最终文字、对应素材和清晰的本地 Markdown 链接，不复制无关过程记录。

## 协作与授权

### 需要先确认

- 新网站或大范围重设计的视觉方向。
- 会改变品牌定位、页面目标或信息架构的选择。
- 删除正式内容、发布网站、引入付费依赖或 Custom Code。
- 用户没有授权、且不同选择会明显改变结果的事项。

### 可以直接执行

- 用户已经明确要求的局部修改、修复和 Polish。
- 不改变设计方向的响应式、SEO、Alt、链接、命名和结构完善。
- 读取、审查、截图和其他可逆验证。

执行前给出简短目标和方案即可，不要把每个小步骤都变成一次等待确认。发现风险或需要扩大范围时再暂停询问。

## 一次成型工作流

先判断任务属于哪一层：

```text
内容与品牌
设计与布局
Component / Variant / Styles
交互与链接
Responsive
SEO / Accessibility
发布与交付
```

修改时按页面或 Section 纵向完成，不要先画完整站点、最后统一补基础能力：

```text
设计
→ 应用 Styles
→ 组件化重复结构
→ 设置真实内容、链接和语义
→ 完成各断点
→ 目标化 Preview 检查
→ 标记完成
```

“看起来完成”不等于完成。基础功能被留到最终 Polish，通常会造成最大时间和 Token 浪费。

## 高级模板的两阶段建设法

高级 Marketplace Template 默认使用以下工作流。这里的“高级”指需要明确艺术指导、参考站转译和差异化视觉装置的模板，不是把基础质量留到最后补的普通草稿。

### 0. 叙事与参考先定稿

进入 Framer Canvas 前先完成：

1. 明确页面叙事顺序、每个 Section 的作用、主要文字、图片角色和 CTA 路径。
2. 拆解参考站真正有价值的构图、排版、图片节奏和交互逻辑，区分“可转译的设计语言”和“不可照搬的行业内容”。
3. 先与用户完成文字版结构审阅和 Polish；叙事、页面目的或主要视觉方向仍在变化时，不开始批量搭建。
4. 将确认结果写入当前项目 `PROJECT.md`，使聊天记录不成为唯一设计依据。

### 1. Basic：基础层必须完整可交付

Basic 不是低保真线框，也不是只做静态排版。它是所有后续差异化设计的稳定底座，每个 Section 都必须纵向完成：

```text
基础构图与真实内容
→ Text / Color Styles
→ Components / Variants / Properties / CMS 决策
→ Navbar、Footer、Button、Form、Gallery 等必要共享结构
→ Links、Heading、Alt、SEO 和真实内容入口
→ Desktop、Tablet、Phone
→ 必要的原生 Motion、Hover、Overlay、Lightbox 和状态反馈
→ Reduced Motion、Focus、Loading、Empty、Error 等基础状态
→ Targeted readback / Preview
→ 对应 Part Checklist 闭环
```

要求：

- 动效、交互组件、响应式、可访问性、可编辑性和性能都属于 Basic，不得推迟到 Advanced 或最终 Polish。
- 优先使用 Framer 原生 Styles、Components、Variants、Properties、CMS、Effects、Overlays、Lightbox 和 Breakpoints。
- Marketplace 模板的替换路径、长文案压力、不同图片比例、缺失可选字段和买家编辑入口必须在 Basic 阶段成立。
- 一个 Part 未通过 `framer/checklist.md` 时，不进入该 Part 的 Advanced 设计。

### 2. Basic Polish Gate

完成基础层后先进行一次独立 Polish 和验收，不立即叠加高级效果：

- 检查叙事节奏、构图比例、文字换行、图片焦点、Section 过渡和全站一致性。
- 执行当前范围 Checklist 与 Preflight，修复基础错误并更新 `PROJECT.md`。
- 由用户确认基础叙事和整体方向。若方向仍需调整，优先在结构简单的 Basic 层修改。
- 只有 Basic 达到可交付状态并通过确认后，才进入 Advanced。

### 3. Advanced：参考驱动的差异化设计

Advanced 的目标是增加项目独特性，而不是重复修补 Basic。创意判断主要来自当前项目参考站、品牌内容和用户审美反馈。

Advanced 可以偏离根 `SKILL.md` 中的通用审美默认值、推荐风格、Dial 建议和常见 Pattern，但必须遵守以下边界：

- 不得跳过 Framer 平台约束、Checklist、响应式、可访问性、Reduced Motion、性能、可编辑性、事实边界和 Marketplace 交付要求。
- 用户明确要求的参考语言优先于 Skill 示例；偏离默认 Pattern 时在 `PROJECT.md` Decisions / Exceptions 记录设计目的和影响范围。
- 每个高级装置先说明它从参考站转译了什么、服务哪个叙事目的，再选择最小可行实现。
- 原生能力能完成时不引入 Custom Code；确需 Custom Code、付费依赖或高性能成本时先取得用户确认。
- 差异化设计不得破坏 Basic 已通过的 Component、Link、Alt、Heading、CMS、Breakpoint 和编辑路径。
- 每完成一个 Advanced Part，重新执行该 Part 的全部 Checklist，并针对性能、Reduced Motion、内容替换和断点做额外复检。

### Advanced Design 知识沉淀

任何新增或回读的高级组件模式，都必须在 `framer/advance-design/` 留下一份能让下一位 Agent 一次完成的 Markdown；不能只记录视觉意图或几个局部数值。文档至少包括：

- 适用边界、交互目标与不适用的场景。
- 组件树、Property / Variant / Instance 的职责分层，以及每个触发器的目标。
- 底层实现逻辑：坐标系、裁切窗口、宽度/高度所有权、状态位移公式、动效责任层与内容替换路径。
- Desktop、Tablet、Phone 的独立尺寸契约；说明外部 Instance 在 Preview 改变可用宽度时如何避免图片拉伸、露白、错位或文字跳位。
- 按真实顺序的实施步骤、一次性验收矩阵、常见错误、不可改动的约束和修复路径。
- 文档最后放一个精确 Example：以一个实际已验证组件为例，给出可 1:1 复刻的层级、状态名、尺寸、gap、position、transition、Property 绑定和 Preview 验证项。没有精确数据时不得宣称可复刻。

高级组件先在外部 Page Instance 的真实 Preview 验证首项、中间项、末项与至少一个可用宽度变化，再视为可复用。图片轨道、文字 reel 等像素位移结构必须用 Fixed viewport/slide/window 建立稳定坐标；页面可响应，但不得让参与位移计算的内容被 `Fill`、百分比或 `1fr` 重新拉伸。

### 4. 最终整合

```text
Basic 完整
→ Basic Polish Gate
→ Advanced 差异化 Part
→ 每 Part Checklist 与回归检查
→ Website Preflight
→ Marketplace 商品化与发布材料
```

如果 Advanced 造成基础功能回归，先恢复 Basic 的可交付状态，再重新评估高级装置；不能用视觉独特性抵消低可用性、低性能或低可编辑性。

Framer 搭建任务必须使用 `framer/basic/workflows/build-checklist.md`。报告完成前必须使用 `framer/basic/workflows/preflight-audit.md` 检查当前范围。

### 每个 Part 后的强制 Checklist 闭环

Framer 任务不得只在开头阅读规范、最后统一检查。每完成一个 Section、Component、Variant、图片批次、交互、Breakpoint、Navbar、Footer、Page 或其他明确 Part，必须：

1. 打开 `framer/checklist.md`。
2. 从路由表找到当前 Part 对应的全部检查部分。
3. 对页面实例、共享组件和相关断点进行 Targeted readback / Preview。
4. 将结果判定为 `Pass`、`Fix Required` 或 `Blocked`。
5. 对 `Fix Required` 的同类问题立即批量自修补，不把基础缺陷留给用户或最终 Polish。
6. 只复检受影响范围；通过后才能开始下一个 Part。
7. 把真实例外、阻塞和恢复状态写回当前项目 `PROJECT.md`。

Context 压缩、Session 恢复或长任务续接后，不得依靠先前记忆继续工作；必须重新读取 `framer/checklist.md` 的强制使用方法、路由表和当前 Part 对应部分。

完成后更新当前项目 `PROJECT.md` 的 Build Status Matrix、Decisions/Exceptions 和 Recovery State。不要让聊天记录成为唯一状态来源。

## Framer 路由

Framer 的详细规则不在本文件重复维护。进入 `framer/basic/README.md` 按任务读取：

- 全站基础质量：`standards/website-baseline.md`
- Marketplace 附加要求：`standards/marketplace-guidelines.md`
- Layer 命名：`standards/layer-naming.md`
- 已验证默认模式：`patterns/pattern-recipes.md`
- Navbar / Footer：`patterns/navbar-footer.md`
- Motion / Overlay / Lightbox：`patterns/motion-design.md`
- 固定建设顺序：`workflows/build-checklist.md`
- 完成前审查：`workflows/preflight-audit.md`
- Token、Session、批量写入与验证：`workflows/token-saving.md`
- 图片处理与 reconnect：`workflows/image-workflow.md`
- Agent 连接：`workflows/agent-connection.md`
- 每个 Part 后的检查与自修补：`framer/checklist.md`

Framer 默认原则：

- 优先使用 Components、Variants、Styles、Layout、Stack、Breakpoints 和原生 Effects。
- 简单效果不引入 Custom Code。
- 新任务复用一个明确 Session；等待变慢时先回读状态，不主动 reconnect。
- 读取目标节点，不默认打印整页节点树。
- 已知结构一次批量写入，再做最小必要验证。
- 默认从 Pattern Recipes 选择结构；偏离默认模式时在项目 Decisions 中记录原因。

## 响应式

任何网站任务都必须考虑 Desktop、Tablet 和 Phone。不能只缩小 Desktop：

- 检查内容顺序、宽度所有权、文字换行和触控目标。
- Grid / Row 在窄屏需要转换为合理 Stack 或减少次要信息。
- 图片在各断点重新判断比例、裁切和焦点。
- 不允许横向溢出、极小文字和依赖 Footer 才能访问的核心导航。

更具体的 Framer 验收矩阵见 `framer/basic/standards/website-baseline.md`。

## 文案原则

文案保持自然、真实、有品牌个性。避免空洞营销、过度夸张和常见 AI 模板句。

除非有事实依据和明确理由，避免使用：

- Best
- Professional
- Innovative
- Passionate

## 修改原则

- 优先小范围、可验证的修改，但同一个明确任务应一次完成完整质量链。
- 不把可以一次批量完成的 20 个同类改动拆成 20 次调用。
- 不为了组件数量而组件化一次性内容。
- 不为了消除所有警告破坏明确设计意图；本次新增的真实错误必须解决。
- 修改后回读目标节点或目标容器，不重复读取无关页面。
- Section、Page 或 Website 只有通过对应 Definition of Done 才能标记完成。

## 代码原则

如果涉及代码：

- 保持简洁、易维护和可理解。
- 优先复用现有脚本和平台原生能力。
- 临时脚本使用明确名称，确保任务中断后可以恢复。
- 删除不必要架构，不为简单视觉效果引入复杂状态系统。

## 沟通方式

### 连续修改前的需求回顾

同一个 Part、Component、Section 或交互进入第二轮及后续修改时，不得只根据用户最新一条消息继续。每次新的写入前必须回顾从该 Part 开始以来用户给出的相关提示与修正，并整理一份短约束锁：

- 当前仍有效的设计目标与交互行为。
- 用户后续补充但没有明确撤销的既有要求。
- 本轮新增或改变的内容。
- 明确不得修改的页面、断点、组件或内容入口。
- 完成后必须验证的断点、状态与真实交互路径。

用户的新反馈默认是在既有要求上追加或校正，不得自动视为替换全部前文。只有用户明确表示放弃、重做或覆盖旧方向时，才移除对应约束。

执行顺序：

```text
回顾当前 Part 的用户提示
→ 写出短约束锁
→ 将拟修改结构逐项对照约束
→ 批量写入
→ 按约束锁和 Framer Checklist 双重复检
```

若实现方案会满足最新反馈却破坏前文要求，必须在写入前调整方案；不能等用户再次指出后才恢复。

说明：

- 最终改了什么。
- 为什么选择该方案。
- 检查了哪些端侧或交互。
- 是否存在已知限制。

不要向用户倾倒内部节点 ID、完整工具输出或重复过程。发现用户方案有结构性问题时，应给出证据和更低成本的替代方案。

## 文件管理

- 文件夹和普通文件使用 kebab-case。
- 特殊入口文件保持大写，例如 `README.md`、`TODO.md`、`AGENTS.md`。
- 修改前确认文件用途。
- 不创建职责重复的规则文件。
- 规则放在最接近其适用平台或任务的位置；Framer 专项规则放入 `framer/basic`，不要堆在仓库级 AGENTS 中。

## 最终目标

建造符合项目审美、品牌事实和真实使用目标的网站，同时让后续修改比首次搭建更简单，而不是把结构债务留给最终 Polish。
