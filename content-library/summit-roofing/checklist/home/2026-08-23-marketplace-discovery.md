# Home — 2026-08-23 Marketplace Discovery Request

## Status

Completed — Home built and QA complete on 2026-08-23. The implementation scope covered the complete Home page and its necessary shared systems; publishing remains outside scope until separately approved.

## User requirements — verbatim

1. 我现在要做一个关于Roofing的template发布framer的marketplace，1，先阅读工作文件夹，了解相关要求，2，然后图片素材在电脑的submit roofing文件夹里，对图片文件进行命名，要求命名简短不超过两个词但是要一看就知道图片相关内容，3，学习成熟roofing网站[https://bakerroofing.com，](https://bakerroofing.com，)学习一下他是怎么划分结构的，以及他的排版，他的配色，他的字体，以及干净利落的风格

2. 你有没有阅读website-lab，从AGENTS.md开始阅读，因为我没有看到你的阅读记录，阅读后我们开始规划网站搭建结构，我需要你详细的给我讲一下搭建计划，然后按照website-lab要求，要一次性完成home界面，包括各种组件应用，footer和navbar等等等等，先别开始做，先确定搭建思路

3. 这些你有记录在project.md里面吗，然后主题色是什么，不能只有灰白吧，还有不要有圆角，你可以直接模仿那个baker roofing的风格

4. 不是说直接模仿就是结构比例一模一样就换个内容，而是参考他的排版，他的风格，然后我希望不要以红色为主题色，我觉得用灰和蓝吧，

## Derived acceptance notes

- The asset task is limited to filename changes. Folder structure, image pixels and the supplied `Logo.png` remain intact.
- The reference informs information hierarchy and visual restraint only; no Baker Roofing copy, identity or factual claims will be reused.
- The planned template must mark unknown contact, service-area, pricing and licensing facts as Missing or Demo instead of inventing them.
- Formal Canvas work requires a Framer project URL plus the repository Live Framer Canvas Gate.
- The Home implementation is one continuous approved scope, but it is executed in ownership order: Component Definition → Page Instance → Breakpoint Override → Preview/QA.
- Planned primary repository Skill: `framer-components`, because the delivery establishes reusable Navbar, Footer, Button and repeated-content contracts.
- No Canvas implementation begins until the user confirms the recorded scope and build approach.
- Superseded by requirement 4: Baker Roofing is not a structural blueprint or a content-swap target. It remains a reference for typography, spacing discipline, hard-edged geometry, image treatment and direct conversion rhythm.
- Superseded by requirement 4: the earlier safety-red palette is retired. The active palette is Slate Blue `#365F7A`, Deep Navy `#172B3A`, Steel Grey `#6C767D`, Mist Grey `#E3E7E8`, Soft White `#F5F6F5` and Pure White `#FFFFFF`.
- Summit's section order, widths, grid ratios, spacing and responsive transformations must be designed independently from Baker Roofing.
- All visible Component and content surfaces use `0px` radius across Desktop, Tablet and Phone.

## Current completion evidence

- Workspace routing and project-manifest requirements were read.
- All supplied image files were visually reviewed and renamed with one or two descriptive words.
- Baker Roofing’s homepage structure and visible design system were reviewed.
- `PROJECT.md` establishes the current source of truth and a proposed Home-page narrative.
- The repository was re-read from `AGENTS.md`, followed by the current `PROJECT.md`, active request checklist, `framer/README.md`, `framer-components`, and its targeted Navbar/Footer, Button, Marketplace and layer-naming references.
- The official Framer Agent gate passed, and the existing blank Home was modified rather than duplicated.
- Shared Color/Text/Link Styles, reusable Button/Service/Process/Card/Navbar/Footer Components, the responsive `Site Shell`, Projects CMS and Insights CMS were implemented.
- The eight-section Home contains Hero, Trust Band, Services, Featured Work, Process, Team, Insights and Closing CTA, with shared Navbar and Footer.
- Desktop 1200px, Tablet 810px and Phone 390px were verified; Phone also passed a 320px structural width stress scan. The bounded Phone preview showed the full runtime page.
- Links, anchors, page/root metadata, reduced motion, image alt text and zero-radius geometry passed targeted readback.
- The non-publishing Framer readiness preview returned zero errors and zero warnings. No publish confirmation was executed.
- Follow-up asset optimisation verified 27 Desktop-source and 38 project-library WebP assets, each ≤500KB; old JPG/PNG files were removed on user instruction. The Home's four static image fills, five CMS image fields, page/root social images and site icon images now use WebP. The shared Navbar uses a cropped supplied WebP Logo at Desktop, Tablet and Phone sizes; Framer retains one Phone Open static spacing lint warning despite the read-back 604px expanded container, so no fresh visual preview was taken beyond this Part's one-logo visual budget.

## Confirmation gate

Confirmed by the user on 2026-08-23 with “现在开始做”. Changes to scope, brand facts, image licensing or the project URL will be recorded before implementation.

## Component Requirement Contract

Contract status: Pass. The initial live readback found one blank Home Desktop breakpoint and no existing Components, Layout Templates, CMS Collections or shared Styles. The implementation used **Modify** for the existing Home page and **Add** for the missing shared systems; no parallel page or duplicate component set was created.

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | Page Sections own full-width fills, order and vertical spacing; Component roots own internal layout; the Layout Template owns the shared shell | Page Section / Layout Template | User requirements 2–4; `framer-components` responsibility rules | Eight ordered Sections and `Site Shell` read back | Full 390px runtime page preview |
| Available width / placement | Sections provide width; inner wrappers fill with a Desktop cap; Components do not impose page gutters | Page Instance | Framer width rules; `framer-components` Assign Responsibility | Desktop, Tablet and Phone ownership chain read back | 1200px, 810px and 390px checks |
| Visible boundary / border / surface | All visible surfaces use 0px radius; fills, hard crops and 1px rules create hierarchy | Component Definition / Page Section | User requirements 3–4; [`framer-components` — Assign responsibility](../../../../.agents/skills/framer-components/SKILL.md#assign-responsibility) | Home audit found no non-zero radii | Phone preview confirmed square geometry |
| Internal padding / hit area | Button, Navbar, Footer, Service Row, Project Card, Article Card and Process Step Definitions own internal padding and usable touch areas | Component Definition | Framer Button and Navbar/Footer guidance | Definition attributes and representative Instances read back | Phone Navbar and CTA sample |
| Readable max-width | Page wrappers cap long prose; display headings may use the wider grid; Components add no duplicate editorial cap | Page Section / deepest content owner | Framer width and typography rules | Parent/child width chain read back | Desktop and Phone wrapping check |
| Editable content / Properties | Buttons, rows, steps and standalone cards expose relevant labels, destinations and content; CMS owns project/article records | Component Properties / CMS | `framer-components` Properties contract; Framer CMS guidance | Definitions, controls, Collections and first/middle/last records read back | Dynamic project/article samples in Phone preview |
| States / routes | Buttons include default/hover states; Navbar has Desktop, Tablet, Phone Closed and Phone Open; actions target explicit page anchors | Component Definition + Instance link | Home scope; [`framer-components` — Preserve behavior and editability](../../../../.agents/skills/framer-components/SKILL.md#preserve-behavior-and-editability) | Variants and all navigation/CTA destinations read back | Phone navigation shell sample |
| Breakpoint contract | Definitions precede Instances; page composition changes at Desktop, Tablet and Phone without changing ownership | Component Definition + Page Breakpoint | `framer-components` definition-first rule; responsive guidance | 1200px, 810px and 390px structures read back; 320px scan found no wide fixed descendant | Full bounded Phone preview |
| Accessibility / touch / focus | Semantic structure, meaningful alt, reduced motion and touch-safe actions are required; no hover-only content | Definition + Instance content | Website-lab accessibility requirements; image workflow | Root/page metadata, reduced motion, image alt and destinations read back | Phone content remained visible without hover |
| Evidence sample | Navbar/Footer, Button states, all Service rows, first/middle/last CMS projects and both Insights records | QA | `framer-components` Evidence Sample; visual-budget rules | Targeted serialization and final readiness preview with 0 errors / 0 warnings | One bounded Phone preview only |

### Contract result

| Contract area | Result | Evidence / retained limit |
|---|---|---|
| Page and shell ownership | Pass | Eight Home sections plus one responsive `Site Shell` Layout Template; Navbar/Footer remain shared. |
| Shared styles and geometry | Pass | Six shared colors, responsive type/link styles, and no non-zero visible radii found on Home. |
| Reusable Components | Pass | Button, Service Row, Process Step, Project Card, Article Card, Navbar and Footer Definitions exist and are used where their ownership fits. |
| CMS | Pass with platform exception | Projects and Insights Collections render dynamic native repeated card templates. Direct CMS responsive-image binding through Component Instances was rejected by Framer, so reusable standalone Card Definitions were retained while the CMS lists use native repeated templates for correct per-item images. |
| Navigation and actions | Pass | Brand, Services, Work, Process, Team, Insights and Contact targets were read back; no invented phone, address or service-area destination was added. |
| Responsive behavior | Pass | 1200px, 810px and 390px layouts verified; 320px scan found no visible fixed-width descendant wider than 350px. |
| Accessibility and metadata | Pass | Meaningful alt text, semantic structure, reduced motion and page/root metadata are present. Full manual keyboard/screen-reader testing remains a Marketplace preflight activity. |
| Publication readiness | Blocked outside Home scope | Image licences, final contact/legal facts, Demo/Remix URLs and Marketplace listing assets are Missing. Publishing was not authorised or performed. |
