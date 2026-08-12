# Morrow & Grain Bakehouse — Project Manifest

## 1. Project Identity

- Project name: Morrow & Grain Bakehouse
- Platform: Framer
- Project type: Marketplace Template / Local Business Brand Site
- Status: QA / Marketplace Preparation
- Framer project: https://framer.com/projects/Morrow-Grain--oZuhc47PHCrmoGiOkVKy-3hDsu
- Content status: Demo
- Brand status: Fictional demonstration brand

正式发布时必须保留：

> Morrow & Grain is a fictional brand created for demonstration purposes.

## 2. Source Index

- Brand facts and approved demo content: `info.md`
- Original build brief: `prompt.md`
- Remaining work: `TODO.md`
- Images: `images/`
- Framer baseline: `../../framer/basic/standards/website-baseline.md`
- Build checklist: `../../framer/basic/workflows/build-checklist.md`

## 3. Website Goal

为独立 Bakery、Cafe、Coffee Shop、Local Restaurant 和 Small Business Owner 提供一个可复用的高质量 Framer 网站模板。

访客需要快速理解：

- 这是一家温暖、手工制作、重视慢发酵与季节食材的社区烘焙店。
- 可以查看菜单、了解品牌、浏览图片并获得到店信息。

主要转化：Visit the Bakehouse。

次要转化：View Menu、Call、Email、Map、Instagram。

## 4. Target User

- Template buyer: 独立烘焙店、咖啡店、本地餐饮和小型商业所有者。
- Website visitor: 附近居民、早餐/咖啡顾客、首次到店访客。
- Device priority: Balanced；Phone 的导航、地址、营业时间和联系方式尤其重要。

## 5. Brand Direction

- Personality: Warm, crafted, honest, tactile, modern, welcoming
- Positioning: Modern neighborhood bakehouse inspired by European baking traditions, seasonal ingredients and everyday rituals
- Tagline: Baked slowly. Shared daily.
- Visual direction: Cream paper, toasted brown, muted terracotta, charcoal, natural oak, linen and flour texture
- Photography: Editorial natural light, realistic texture, slight film grain, 35mm feeling
- Motion: Subtle, natural, premium; no SaaS-like motion or exaggerated bounce
- Memory point: Editorial bakery imagery combined with tactile typography and morning ritual storytelling

Avoid:

- Luxury dessert branding
- Hotel restaurant aesthetics
- SaaS landing-page structure
- Highly commercial chain-store feeling
- Plastic or over-polished photography

## 6. Content Facts

All facts below are Demo content.

| Fact | Value | Status |
|---|---|---|
| Address | 18 Market Row, Northfield, Oregon | Demo |
| Phone | (503) 555-0148 | Demo |
| Email | hello@morrowandgrain.com | Demo |
| Instagram | @morrowandgrain | Demo |
| Tue–Fri | 7:30 AM–4:00 PM | Demo |
| Sat–Sun | 8:00 AM–3:00 PM | Demo |
| Monday | Closed | Demo |
| Menu and prices | See `info.md` | Demo |

## 7. Sitemap

| Page | Path | Purpose | Primary action |
|---|---|---|---|
| Home | `/` | Introduce brand and route visitors | View Menu / Visit |
| Menu | `/menu` | Show breads, pastries, savory bakes, sweets and drinks | Visit / Contact |
| About | `/about` | Build trust through process and values | Visit |
| Gallery | `/gallery` | Show products, space, work and rituals | Visit |
| Visit | `/visit` | Provide address, hours and directions | Map / Call |
| Contact | `/contact` | Provide direct contact paths | Phone / Email |

## 8. Home Story

```text
Hero
→ Featured Bakes
→ Brand Story
→ Menu Preview
→ Gallery
→ Values
→ Visit
→ Footer
```

页面顺序服务“认识社区烘焙店 → 看产品与过程 → 形成到店行动”的路径。

## 9. Conversion Paths

```text
Home / Menu / Gallery
→ Understand brand and offering
→ Visit CTA
→ Address / Hours / Map / Phone
```

主体和 Footer 均提供：

- `tel:+15035550148`
- `mailto:hello@morrowandgrain.com`
- Map link
- Instagram link

## 10. System Status

### Shared structure

- Layout Template: Navbar / Content / Footer
- Navbar Component: Desktop / Tablet / Phone and scroll behavior
- Footer Component: Desktop / Tablet / Phone
- Buttons: Primary and Secondary exist; Variant naming still needs cleanup
- Gallery: Native Lightbox Effect, no image-content Variants

### Style System target

Text Styles:

- Display / H1
- Section Heading / H2
- Body
- Caption
- Label
- Button Label

Color Styles:

- Cream
- Charcoal
- Terracotta
- Brown
- Muted Text
- Divider

Current status: visual system is established, global Style migration remains pending per `TODO.md`.

### CMS decision

Current decision: No CMS in this release.

Reconsider only if template testing shows buyers need frequent menu/gallery additions, deletion or sorting.

## 11. Responsive Plan

| Area | Desktop | Tablet | Phone |
|---|---|---|---|
| Navbar | Full nav + CTA | Compact full nav | Logo + Menu Relative Overlay |
| Content | Editorial grid and wide imagery | Reduced grid complexity | Natural vertical stack |
| Gallery | Mixed spans | Simplified columns | Single-column rhythm |
| Footer | Multi-column | Reduced columns | Vertical reading order |

Test widths: 320 / 390 / 810 / 1200 / 1440+

## 12. Motion and Interaction

- Navbar: Sticky; scroll down hides, scroll up reveals.
- Phone Menu: Trigger-contained Relative Overlay, about 360ms opacity + slight y/scale.
- Gallery: Native Lightbox with continuous transition and restrained size.
- Hover: Color/opacity and inner-image scale; no dense-link or full-card scale.
- Custom Code: Not required for current release.

## 13. Assets

- Original images are AI-generated four-scene composites.
- Each composite must be sliced into four images without changing content.
- Gallery uses 20 final images.
- Do not regenerate core images or introduce unrelated stock assets.
- Image processing follows `../../framer/basic/workflows/image-workflow.md`.

## 14. Build Status Matrix

Legend: ✓ Complete / △ Needs final audit or cleanup / ☐ Not started

| Page | Content | Styles | Components | Links | SEO | Alt | Desktop | Tablet | Phone | Preview |
|---|---|---|---|---|---|---|---|---|---|---|
| Home | ✓ | △ | ✓ | ✓ | ✓ | ✓ | ✓ | △ | △ | △ |
| Menu | ✓ | △ | ✓ | ✓ | ✓ | ✓ | ✓ | △ | △ | △ |
| About | ✓ | △ | ✓ | ✓ | ✓ | ✓ | ✓ | △ | △ | △ |
| Gallery | ✓ | △ | ✓ | ✓ | ✓ | ✓ | ✓ | △ | △ | △ |
| Visit | ✓ | △ | ✓ | ✓ | ✓ | ✓ | ✓ | △ | △ | △ |
| Contact | ✓ | △ | ✓ | ✓ | ✓ | ✓ | ✓ | △ | ✓ | △ |

## 15. Completed Polish

- Phone Navbar Menu Overlay and real Preview open/close test.
- Independent Metadata for inner pages.
- H1 and main H2 semantics.
- favicon and Open Graph image.
- Alt Text for Home, Menu, About, Visit and Contact; Gallery already complete.
- Phone, Email, Instagram and Map links.
- Contact Phone email wrapping fix.

## 16. Remaining Work

See `TODO.md`. Current priorities:

1. Minimal Text/Color Style migration.
2. Semantic Button Variant names and component-control cleanup.
3. Six-page responsive and interaction Preflight.
4. Marketplace Preview, Demo, Remix and editing instructions.

## 17. Explicit Non-goals

- No complex CMS in current release.
- No Contact form unless Marketplace or target-user evidence requires it.
- No Privacy page in current scope.
- No per-image Gallery Variants or custom Overlays.
- No Reduced Motion Custom Code.
- No Desktop redesign solely to increase component count.

## 18. Recovery State

- Current Framer project: Morrow & Grain
- Current phase: QA / Marketplace preparation
- Last verified interaction: 390px Phone Navbar Menu opens and closes correctly
- Next source of truth: `TODO.md`
- Before reporting Ready: execute `../../framer/basic/workflows/preflight-audit.md`
