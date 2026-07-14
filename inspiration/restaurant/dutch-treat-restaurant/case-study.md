# Dutch Treat Restaurant Case Study

## Reference

项目类型：本地社区餐厅的非官方概念重设计 Demo，使用 Framer 构建 Desktop、Tablet 和 Phone 网站体验。

项目的核心不是把一家社区 diner 包装成高端餐饮品牌，而是把真实、熟悉、方便到访的餐厅体验转化为清晰的网站叙事。所有事实内容来自 content-library 中的餐厅截图、菜单、地址、营业时间和公开评价，不补写无法核验的品牌历史、电话、预订功能或奖项。

## Brand Direction

品牌方向是 “warm, honest neighborhood diner”：温暖、直接、有社区感，但不怀旧到像主题餐厅，也不精致到失去真实感。

视觉系统使用奶油纸色作为主要背景、深咖色作为结构和文字颜色、餐厅红作为动作色。奶油色带来旧式纸质菜单和早餐店的触感；深咖比纯黑更柔和；红色既呼应传统 diner 视觉，也能明确标记 CTA。标题使用 Vollkorn，正文使用 Alegreya Sans，使网站同时具有编辑感和亲切的日常可读性。

## Design Principles Learned

1. 餐厅 Hero 应先回答“这是什么地方”，再表达气氛。外观图比泛化的食物照片更适合 Dutch Treat，因为它立即建立真实地点、店面辨识度和到店预期。
2. 真实不等于直接使用未经处理的地图截图。发布者信息、按钮和 Google Maps UI 会破坏品牌感，必须修复画面，而不是用裁剪牺牲建筑主体。
3. 首页负责建立兴趣和提供入口，完整信息应放到独立页面。完整菜单不应该被塞进 Home；Gallery 也需要成为可浏览的独立内容空间。
4. CTA 必须与用户当前意图一致。Hero 提供 Get Directions 和 View Menu；Menu 入口明确指向完整菜单；Gallery 末尾使用 Plan Your Visit，把浏览图片后的兴趣转化为到店行动。
5. Hover 是反馈，不是装饰。按钮可以轻微变色或有限缩放，但 Footer 链接位于裁切容器中时不应缩放，否则文字会被截断。Footer 更适合透明度或颜色变化。
6. 响应式设计不是 Desktop 的等比缩小。Tablet 可保留双栏菜单和图片网格；Phone 应把菜单、Gallery、Contact 和 Footer 改成真正的单列阅读顺序。

## Layout Structure

### Home

1. Navigation：Menu、Gallery、Contact 与 Get Directions。
2. Hero：真实餐厅外观、品牌主张、简短说明、方向和菜单 CTA。
3. Full Menu Entry：不重复完整菜单，只解释菜单内容并提供入口。
4. Food and Atmosphere Preview：用少量食物和环境图片建立期待，并引导到完整 Gallery。
5. Reviews：用公开评价片段提供社会证明。
6. Visit：地址、营业时间、外观和 Google Maps 行动。
7. Final CTA：再次提供 Get Directions。
8. Detailed Footer：餐厅简介、地址、营业时间和站点导航。

Restaurant Introduction 最终被移除，因为 Hero 已经用外观和文字完成地点与品牌介绍；保留独立 Introduction 会重复信息并拖慢首页节奏。

### Menu

菜单从两张截图中提取菜名、分类和价格，重新组织为可读文本卡片。Desktop 和 Tablet 使用双栏分类，Phone 使用单栏。这样比直接展示图片更容易阅读、更适合辅助技术，也能在不同屏幕上保持真实字号。

### Gallery

Gallery 以 Food 与 Atmosphere 混合的图片网格呈现真实体验。Desktop 使用三栏节奏，Tablet 使用两栏，Phone 使用单列固定高度图片。图片墙之后放置红色 CTA 区域，文案 “Ready for breakfast?” 和按钮 “Plan Your Visit”，位置在 Footer 之前。

### Contact

Desktop 和 Tablet 使用外观图与联系信息双栏；Phone 改为外观图在上、地址和营业时间在下。地图按钮是主要行动，但不虚构电话号码或预订能力。

## Typography

- Display / Hero：Vollkorn，Desktop 约 58–72px；Tablet 约 44–52px；Phone 约 36–44px。
- Section Heading：Vollkorn，Desktop 约 48–62px；窄屏逐级缩小。
- Body：Alegreya Sans，约 17–20px，行高 1.45–1.65。
- Labels：Alegreya Sans，13–14px、粗体、大写、增加字距，使用红色或浅橙色。
- Menu Items：分类标题使用衬线，项目与价格使用无衬线；价格使用 tabular numbers。

标题与正文的比例需要明显，但正文不能过小。Hero Content 应保持紧凑，避免在 Phone 上遮挡建筑；Phone 可隐藏次要说明，把主标题和 CTA 作为最低必要信息。

留白采用分级策略：Section 外部使用较大的 72–112px 垂直空间，内容组使用 18–40px gap，按钮和标签使用更紧凑的 12–20px。留白用于建立叙事节奏，不是把所有区块平均拉开。

## Image Strategy

1. 先把素材按 Exterior、Food、Atmosphere、Menu、Contact、Reviews 分类。
2. 使用最长边不超过 1200px、JPEG 质量约 50–60%、小于 1 MB 的联系表做筛选，每轮只查看一张联系表。
3. Hero 使用经过 AI 修复的餐厅外观图，保留建筑、招牌、透视和光线，只移除地图 UI 并补全被遮挡区域。
4. Gallery 尽量使用真实食物和空间图片，但避免重复、模糊和带截图 UI 的素材。
5. 网页上传前生成合适尺寸的压缩版本，原图保存在 content-library，不覆盖。
6. 菜单图片只作为事实来源；最终界面用真实文本排版。

## Components Worth Reusing

- 深色 Navigation + 独立红色主 CTA。
- 半透明深咖 Hero Content 面板，但必须控制宽度、透明度和移动端占用面积。
- Full Menu Entry：标题、简短说明和单一 CTA，可用于把首页摘要连接到完整菜单页。
- Typeset Menu Category Card：衬线分类标题、无衬线条目、tabular 价格。
- Gallery Grid：Desktop 三栏、Tablet 两栏、Phone 单列。
- Gallery-to-Visit CTA：浏览内容之后的情境化转化区。
- Detailed Footer：品牌摘要、地址与营业时间、页面导航三组信息。
- Hover 规则：主按钮变色，可选极轻微缩放；Footer 与小型文字链接仅变色或透明度，不缩放。

## Mistakes To Avoid

1. 不要用食物图代替最能说明地点身份的 Hero 外观图。
2. 不要让 Hero Content 在 Phone 上覆盖大部分主体图片。
3. 不要为了隐藏地图 UI 而裁掉建筑、招牌或关键食物。
4. 不要把完整菜单和完整 Gallery 全部塞进 Home。
5. 不要把菜单照片直接当作最终菜单页面。
6. 不要创建 CTA 后只验证节点存在；必须确认它位于正确页面、正确顺序，并继承到 Tablet 和 Phone。
7. 不要只做 Desktop 后假设 Framer 会自动产生可用的 Tablet/Phone。
8. 不要在 Footer 链接使用放大 Hover；裁切容器会截断超出的文字。
9. 不要把无法核验的电话号码、预订、品牌故事或最新价格写入网站。
10. 不要一次把多张原图或大尺寸截图写入上下文，这会显著增加 reconnect 风险。
11. 不要在批量 Framer 操作没有输出时假设成功；必须回读页面树、sitemap、断点和浏览器 DOM。
12. 不要重复创建页面来绕过回读异常；先确认正式路由是否已经存在。

## Future Improvements

- 由餐厅人工核验菜单价格、地址和营业时间，再更新正式内容。
- 如果获得可核验电话，可在 Contact 和 Footer 添加 Call 按钮。
- 为 Menu 建立结构化 CMS，使分类和价格更易维护。
- 为 Gallery 添加分类筛选或轻量 Lightbox，但保持操作简单。
- 把 Navigation 与 Footer 提取成共享 Layout Template，减少跨页面重复维护。
- 建立项目级断点检查表，要求每个新增页面在交付前验证 Desktop、Tablet 和 Phone。
- 为长图片任务保存明确的 checkpoint，包括 Framer URL、正式页面、素材路径、已处理图片和下一步，降低 reconnect 后的恢复成本。
