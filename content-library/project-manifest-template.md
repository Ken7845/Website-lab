# Project Manifest Template

复制到 `content-library/<project-name>/PROJECT.md`，删除说明性占位内容后再开始搭建。

## 1. Project Identity

- Project name:
- Platform: Framer
- Project type: Brand Site / Portfolio / Landing Page / Marketplace Template / Other
- Status: Planning / Building / QA / Ready / Published
- Framer project URL:
- Demo URL:
- Content status: Approved / Draft / Mixed
- Last updated:

## 2. Website Goal

- 网站为谁服务？
- 用户进入网站后需要理解什么？
- 网站最重要的实际结果是什么？
- 主要 CTA：
- 次要 CTA：

## 3. Target User

- Primary audience:
- User intent:
- Important questions:
- Trust requirements:
- Device priority: Desktop / Phone / Balanced

## 4. Brand Direction

- Brand personality:
- Core concept:
- Visual memory point:
- Typography direction:
- Color direction:
- Image strategy:
- Motion character:
- Avoid:

资料链接：

- Brand Voice:
- Style Guide:
- Inspiration:

## 5. Content Facts

| Fact | Value / Source | Status |
|---|---|---|
| Address |  | Approved / Draft / Missing / Demo |
| Phone |  |  |
| Email |  |  |
| Opening hours |  |  |
| Social links |  |  |
| Prices |  |  |
| Legal / copyright |  |  |

不得根据视觉需要自行填写 `Missing` 的事实。

## 6. Sitemap and Page Goals

| Page | Path | User goal | Primary CTA | Content source | Status |
|---|---|---|---|---|---|
| Home | `/` |  |  |  | Planned |

每个页面必须有独立目的，不能只因为“网站通常有这个页面”而创建。

## 7. Section Plan

| Page | Section | Purpose | Content | Component / Pattern | Status |
|---|---|---|---|---|---|
| Home | Hero |  |  |  | Planned |

## 8. Conversion Paths

记录用户完成目标的最短路径：

```text
Landing
→ Understand offer
→ See proof/content
→ CTA
→ Contact / Visit / Buy / Book
```

- Phone:
- Email:
- Map:
- Social:
- Form / booking / purchase:

## 9. System Plan

### Text Styles

- Display:
- H1:
- H2:
- H3:
- Body Large:
- Body:
- Caption:
- Label:
- Button Label:

### Color Styles

- Background / Base:
- Background / Inverse:
- Surface:
- Text / Primary:
- Text / Secondary:
- Accent / Primary:
- Border / Divider:
- State / Hover:
- State / Focus:

### Shared Components

- Navbar:
- Footer:
- Primary Button:
- Secondary Button:
- Repeated content components:

### CMS Decision

- CMS required: Yes / No / Later
- Collections:
- Reason:

## 10. Responsive Plan

| Area | Desktop | Tablet | Phone |
|---|---|---|---|
| Navbar |  |  |  |
| Hero |  |  |  |
| Main grids |  |  |  |
| Footer |  |  |  |
| Special interactions |  |  |  |

Test widths: 320 / 390 / 810 / 1200 / 1440+

## 11. Motion and Interaction Plan

- Page/section enter:
- Navbar behavior:
- Button/link hover:
- Image hover:
- Gallery/Lightbox:
- Overlay/Menu:
- Reduced Motion decision:

优先从 `framer/basic/patterns/pattern-recipes.md` 选择已验证模式。

## 12. Assets

- Source folder:
- Contact sheet:
- Web output folder:
- Hero assets:
- Gallery assets:
- Missing assets:
- License status:

图片工作遵循 `framer/basic/workflows/image-workflow.md`。

## 13. Definition of Ready

- [ ] 网站目标和目标用户明确。
- [ ] Sitemap 和页面目的明确。
- [ ] 主要 CTA 与转化路径明确。
- [ ] 品牌方向和 Inspiration 明确。
- [ ] 正式事实已 Approved，缺失项已标记。
- [ ] 主要文案和素材足以开始。
- [ ] 必须使用与明确不使用的功能已记录。

未通过 Ready 时，可以做结构探索，但不能把猜测当成正式交付内容。

## 14. Build Status Matrix

| Page | Content | Styles | Components | Links | SEO | Alt | Desktop | Tablet | Phone | Preview |
|---|---|---|---|---|---|---|---|---|---|---|
| Home | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ |

## 15. Decisions and Exceptions

只记录会影响后续工作的决策：

| Decision | Reason | Scope | Date |
|---|---|---|---|

## 16. Recovery State

- Active Framer session:
- Current page/component:
- Last successful change:
- Verified breakpoints:
- Remaining work:
- Important local asset paths:

长任务每完成一个阶段更新这里，避免 reconnect 后从头读取和重做。
