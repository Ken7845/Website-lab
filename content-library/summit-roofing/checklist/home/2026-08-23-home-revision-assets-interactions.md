# Home — 2026-08-23 Revision: Assets, Responsive, Interactions

## Status

Complete. Confirmed by the user (“开始” / “直接完成”); implementation and targeted QA readback are complete. No publishing was authorized or performed.

## User requirements — verbatim

1. 有几个问题要修改，1，navbar在home page上面看没有更新，但是点进去是有的，我不知道这个是不是没有加载出来，还是哪里出问题了，

2. 这个tablet的04 Featured Work有空缺，需要再来一个案例补充一下，

3. 我看到你里面有一个storm response，我里面弄了一些storm damage的图片，其实是要做那种storm damage后修复的，

4. 里面的arrow right为什么是一个圆圈，

5. 做一下04 Featured Work那一部分的图片hover效果，就是图片出现一个图片变暗的hover和文字变色效果，实际上是一个遮罩，把这个卡片做成一个component，然后通过hover vibrant去实现，整个网站的图片hover就这种效果，

6. 03 Services的响应没做好，导致箭头飞到下面去了，见上图，

7. 06 Team这个部分的图片要换一下，我找了一张team的图片放在库里，记得转化格式再用，注意排版，不要过度裁切把人切没了，

8. 你的section命名有问题，不要加01，02，03这些在前面。注意长prompt工作要求

## Follow-up requirements — verbatim

1，project card的hover效果，图片变黑实际上是加一个低透明度的黑色cover在上面，然后我觉得文字可以直接降低透明度但是不要太多，

2，logo的图片裁切一下，就是只保留图案，不要有下面的文字，然后在logo右边补上SUBMIT ROOFING，还有footer也是一样处理，

3，这个lucide里面的icon怎么都变成这样了，是出什么bug了吗，导致arrow right就是一坨圆圈，

4，你这个service row右边也放了箭头，是后面要做什么页面引导澳吗

## Evidence supplied with the request

- `Screenshot 2026-08-23 at 17.34.08.png`: Home Canvas shows a text Navbar rather than the expected image Logo.
- `Screenshot 2026-08-23 at 17.34.02.png`: Tablet Featured Work has an incomplete two-column grid after the third project.
- `Screenshot 2026-08-23 at 17.43.44.png`: Services arrows appear below their intended row alignment.

## Constraint lock and planned verification

- Existing direction remains active: original Summit blue-grey system, no red UI, zero visible radius, no invented operational facts, and no publication.
- The new Team image must be located, converted to WebP under the user-specified asset policy, uploaded, assigned factual Alt text, and checked for person-preserving crop behavior.
- Reusable ownership will be inspected before writing: Project Card must be reconciled with the existing CMS limitation; hover mask, text-color state and arrow treatment require a revised Component Requirement Contract.
- The scope includes Home static/CMS content, Navbar, Services, Featured Work, Team, shared image-hover behavior and section layer names only. It excludes unrelated pages, final business facts, licensing decisions and publishing.
- Required validation after implementation: Navbar across Desktop/Tablet/Phone; Featured Work at Tablet and Phone; Services at Desktop/Tablet/Phone; Project Card default/hover/touch behavior; Team image crop at Desktop/Tablet/Phone; all affected section names; WebP size/decode/reference checks; targeted QA.

## Component Requirement Contract

- Contract status: Pass

| Requirement | Contract |
|---|---|
| Component | Modify the existing `Project Card`; do not create a duplicate card system. |
| Purpose | Provide the reusable visual contract for Featured Work cards, including the hover state. |
| Reuse scope | Featured Work and any future Home image card that uses the same card treatment. CMS data stays in the existing Projects collection. |
| Variants | Default and Hover gesture variant. |
| Properties | Existing CMS-facing content controls stay intact; no new business facts are introduced. |
| States | Default: image and original text color. Hover: dark image overlay and blue text emphasis. Touch devices retain a stable default state. |
| Responsive contract | Desktop and Tablet retain a two-column Featured Work grid; Phone is single-column. The card owns media crop and content rhythm. |
| Accessibility | Card imagery uses factual Alt text; card remains readable without hover; no hover-only essential content. |
| Ownership | `Project Card` owns the image-mask interaction. `Featured Work` owns CMS listing/grid density. `Service Row` owns arrow alignment. `Navbar` remains the shared layout-template component. |
| Verification | Read back Navbar/template, CMS item count and fields, Desktop/Tablet/Phone grids, Project Card default/hover, and Team crop. |

### Follow-up refinement contract — Ready

| Concern | Decision / N/A reason | Owner | Governing source | Readback proof | Preview proof |
|---|---|---|---|---|---|
| Section background / vertical rhythm | N/A — no section rhythm change. | Home | Follow-up 1–4 | Existing section tree remains unchanged. | N/A |
| Available width / placement | Logo mark and `SUBMIT ROOFING` form one horizontal Brand stack; Footer mirrors it. | Navbar / Footer | Follow-up 2 | Brand child sizes and gaps across variants. | Navbar and Footer at Desktop/Phone |
| Visible boundary / border / surface | Hover image receives a black low-opacity cover; text does not recolor. | Project Card | Follow-up 1 | Hover mask fill and text opacity values. | Project Card hover |
| Internal padding / hit area | Preserve current Card and Brand padding / link hit area. | Existing Components | Current Canvas evidence | Component attributes unchanged except required children. | N/A |
| Readable max-width | N/A — existing shared shell width preserved. | Site Shell | Current Canvas | Navbar/Footer outer widths unchanged. | N/A |
| Editable content / Properties | Keep existing Project Card and service properties; add no business facts. | Existing Components | Follow-up 1, 4 | Controls and CMS bindings remain. | N/A |
| States / routes | Hover retains identical geometry; text lowers to 86% opacity. Service Row removes inactive arrow and its invalid implied route. | Project Card / Service Row | Follow-up 1, 4 | Hover replica + Service Row children. | Hover and touch default |
| Breakpoint contract | Navbar/Footer brand treatment applies Desktop, Tablet and Phone. | Navbar / Footer | Follow-up 2 | Variant replica readback. | Desktop and Phone |
| Accessibility / touch / focus | Mark has factual Alt; textual brand remains visible; no information depends on hover. | Navbar / Footer / Project Card | [PROJECT.md §10](../../PROJECT.md#10-system-and-platform-plan) | Alt, text visibility, touch default. | Phone default |
| Evidence sample | One targeted crop check, live definition/instance/replica readback, then targeted QA. | Agent | [image-workflow.md §0](../../../../framer/basic/workflows/image-workflow.md#0-最高优先级视觉预算与停止条件); [framer-components](../../../../.agents/skills/framer-components/SKILL.md#compile-a-component-requirement-contract) | Recorded in Completion evidence. | One per affected visual state |

## Confirmation record

User confirmed the scope on 2026-08-23. Work follows the Framer Agent gate and the contract above.

## Completion evidence

- The Home page retains the shared `Site Shell`; its Navbar Desktop, Tablet and Phone variants all use the supplied WebP Logo. The earlier text-mark screenshot was not the current shared component state.
- Projects now contains four Demo items. `Storm Damage Repair` uses the supplied WebP image and factual Alt text; Featured Work is a two-column four-item grid on Desktop/Tablet and a four-item stack on Phone.
- Featured Work's CMS template now instantiates the existing `Project Card`. The reusable component has Default and Hover gesture variants; Hover applies a 58% deep-navy image mask and slate-blue text. Touch retains the readable default state.
- Services uses the plain Lucide `Arrow Right`; its Desktop/Tablet component grid has four columns and its Phone variant has one column, preventing the arrow from dropping below the row.
- Team uses supplied `team.webp` at Desktop 450px, Tablet 390px and Phone 292px heights, preserving the 4:3 source proportion. The staged `team.jpg` was removed.
- Home section names are semantic on Desktop, Tablet and Phone: Hero, Trust Band, Services, Featured Work, Process, Team, Insights and Closing CTA.
- Local asset checks found no non-WebP image sources other than Finder `.DS_Store` files, and no WebP over 500KB in either the supplied source folder or the project image library.

## Follow-up completion evidence

- `roof-mark.webp` is a 640×300, 14KB transparent WebP cropped from the supplied Logo to retain only the roof graphic. Navbar and Footer use its uploaded Framer asset beside visible `SUBMIT ROOFING` text at Desktop, Tablet and Phone.
- Project Card’s Hover gesture variant now uses `rgba(0, 0, 0, 0.32)` as an image-only cover. Its existing text colours are retained at 86% opacity.
- The Lucide issue was a configuration error, not an icon-library failure: `$control__width` sets stroke thickness, and the prior `16`px stroke filled the icon shapes. Every remaining live Lucide IconNode now uses the normal `2`px stroke while retaining its explicit visual box size.
- Service Row’s arrow was an unused signal for an absent service-detail route. It has been removed from Desktop/Tablet and Phone component variants; the layout now contains only number, title and description.
