# Reserve FAQ Surface, Motion, and Responsive Revision — 2026-08-16

Status: Implemented; Canvas structural readback complete, Preview behavior sign-off pending.  
Scope: `/reserve` FAQ section, reusable `FAQ Row`, project-specific motion record, and the closest existing cross-project responsive guidance.  
Out of scope: native form delivery/recipient configuration, FAQ question/answer content, other pages except the documented `EveningChapterRow` responsive rule.

Latest visual override: the user briefly requested a deep-inverse FAQ treatment, then explicitly reverted it. The final current state returns to the original soft-grey surface with dark Text questions/icons, Muted answers, light dividers and a restrained light-grey Hover. The verbatim original requirement below remains preserved.

## User requirements — verbatim

1. `FAQ部分的背景做成灰色，不要和Reserve Detail放在同一个背景部分`
2. `展开内容应该和展开前的问题有层级关系，不要用同一套字体，内容用比较小的字体`
3. `展开的时候用的transition用Spring physics stiffness250`
4. `不要给FAQ的父级stack设置Max width，这个Max width是之前用于request detail部分的，因为表格不用响应，但是你们两个部分不要放在一起`
5. `点击时的press效果的scale不要太大，有一点点就行`
6. `查询知识库，有没有关于动画transition的相关要求，就比如默认使用Spring physics stiffness250，没有的话补充一下，还有一个要补充的就是响应式，像EveningChapterRow和你刚刚做的这种FAQ类似的这种长条形有边框的组件通常不用加Max width，防止影响响应效果，补充的时候要注意知识库的维护规则，EveningChapterRow`

## Evidence and implementation record

### Pre-change Canvas evidence — 2026-08-16

- `Reservation FAQ` is currently a child of `Reserve Request Content`, whose `maxWidth: 1120px` belongs to the reservation-detail/form composition.
- `FAQ Row` currently uses the same `Type/Body Large` style for its question and answer, a `tween 0.44,0,0.56,1 0.18s 0s` root transition, and a press scale of `0.9`.
- `FAQ Row` has native Closed/Open plus Closed Hover/Open Hover states, with eight page instances.

### Implemented Canvas changes

- Moved the FAQ out of `Reserve Request Content` into `Reservation FAQ Section`, a separate full-width soft-grey surface after the white reserve-request section. Its outer section, content wrapper and FAQ list have no `maxWidth`.
- Preserved a deliberately bounded inner text wrapper only for the FAQ introduction’s readable measure; it is not the FAQ parent/list width owner.
- Moved the FAQ rows’ horizontal `32px` padding from the external `Reservation FAQ Content` wrapper to each `FAQ Row` state root. The bordered row can now Fill its parent while its question, icon, answer and touch area retain component-owned internal spacing.
- Kept the non-component FAQ introduction locally padded at `32px` / `28px` / `20px` across Desktop, Tablet and Phone, so its text measure and alignment remain independent of the reusable row.
- Changed FAQ answers to the existing smaller `Type/Body` style, while questions retain the existing larger question style.
- Set all FAQ Open/Closed/Hover root transitions to the AURELIA native spring contract: `spring-physics 250 30 1 0s`.
- Reduced press feedback to `0.98`, preserving the existing Variant-to-Variant interaction route and touch behavior.
- After a temporary dark-palette test, restored the established light FAQ palette across the Section and current states: Surface background, Text questions/icons, Muted answers, original light dividers, and a restrained `rgb(229, 229, 226)` Hover surface.
- Read back the Desktop, Tablet and Phone hierarchy plus the four FAQ states after implementation. Preview behavior, reduced-motion, focus, keyboard, and stress widths remain separate QA gates.

### Knowledge maintenance result

- Existing evidence: AURELIA already records `spring-physics 250 30 1 0s` as its current motion contract in `DECISIONS.md` for MenuDishCard, ChefStoryRow, and Buttons; it must not be promoted to an unqualified cross-project numeric default.
- Updated the existing cross-project motion reference with the decision boundary: use project-approved transition values first; `stiffness 250` is an AURELIA-specific example, not a universal default.
- Updated the closest existing cross-project responsive-width owner with a bounded rule: long bordered disclosure/story rows whose border is expected to span available page width should not receive an arbitrary root or list `max-width`; constrain only a genuine inner reading measure or fixed-geometry contract. `EveningChapterRow` and `FAQ Row` remain AURELIA evidence, not universal component templates.
- Preserved the existing outer-section rule, documented the project decision in `DECISIONS.md`, and avoided duplicating a new canonical rule elsewhere.

## Acceptance criteria

- FAQ soft-grey surface is visually separate from the white Reserve Detail/form area and fills the available page width.
- FAQ outer parent/list has no `maxWidth`; Desktop, Tablet and Phone instances remain Fill.
- Question and answer have visibly distinct hierarchy using existing styles.
- Open/close uses `spring-physics 250 30 1 0s`; press feedback is perceptible but does not noticeably shrink the row.
- No existing form, FAQ content Property, navigation, Footer, or external-component behavior changes.
- Knowledge updates retain canonical ownership, label project-specific evidence, and pass strict validation.
