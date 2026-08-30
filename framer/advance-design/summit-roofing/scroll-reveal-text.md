# Framer 高级组件：Scroll Reveal Text

> 状态：**Reference，project-derived**。  
> Provenance：Submit Roofing 的 `ScrollRevealText.tsx`、`/reveal-text-test` Desktop 实例、官方 Framer Agent live source / instance readback 与 strict typecheck，2026-08-26。  
> 验证范围：源码和单一 Desktop 测试实例已验证；Tablet、Phone、实际滚动视觉效果和键盘/屏幕阅读器体验**尚未验证**。不要把这里的参数当作跨项目默认值。

## 何时使用 / 不使用

适合：一段本身可完整阅读的展示文案，滚动时从低对比色逐字符过渡到完成色。例如品牌宣言、章节开场或一段短的解释性文字。

不适合：关键行动文案、导航、表单标签、需要可预测逐词阅读的长文章、频繁更新的 CMS 正文，或必须不引入 Custom Code 的 Marketplace 成品。该效果只是增强；文字在静态渲染与 reduced motion 下必须直接呈现完成色。

## 已验证的组件责任

| 层级 | 责任 | 证据 |
|---|---|---|
| `ScrollRevealText.tsx` code component | 文字拆分、滚动进度、逐字符颜色插值、静态 / reduced-motion fallback 与编辑控制项 | 2026-08-26 live source readback；strict typecheck 0 diagnostics |
| Root `<p>` | 滚动 target、可访问名称、整段宽度、换行与对齐 | 源码：`ref`、`aria-label`、`width: 100%`、flex-wrap |
| `Character` motion span | 每个字符的颜色插值；以 `aria-hidden` 避免逐字重复朗读 | 源码 readback |
| Page instance | 文案、字族、字重、字号、色彩、滚动区间与可用宽度 | `/reveal-text-test` Desktop instance |
| Test page | 隔离验证，不属于 Home 或 Marketplace buyer-facing scope | live page-tree readback |

## 精确实现合同

```text
ScrollRevealText
├── Root p (width 100%, display flex, flex-wrap)
│   └── Character × text.length
│       └── motion.span (color: inactive → active)
├── useScroll target: Root p
├── useTransform per character
└── static renderer / reduced motion → activeColor
```

代码组件声明：`@framerSupportedLayoutWidth any-prefer-fixed`、`@framerSupportedLayoutHeight auto`。它以 `Array.from(text)` 拆分字符；设字符数量为 `N`（至少为 1），第 `i` 个字符的颜色区间为 `i / N → (i + 1) / N`。因此字符按阅读顺序依次完成，而不是整段同时淡入。

滚动 offset 直接由两个百分比控制项计算：

```text
["start " + startOffset / 100, "start " + endOffset / 100]
```

这是当前 Submit Roofing 的精确实现，不是对 Framer Motion offset 语法的通用建议；复用前必须在新页面实际滚动验证。

## 已验证源码

以下为 2026-08-26 从 Submit Roofing `ScrollRevealText.tsx` 读取、并以 strict typecheck 获得 0 diagnostics 的完整源文件。新项目可从该文件开始，但必须先完成本文的响应式、Preview、性能和无障碍验证；不要将它直接视为 Marketplace 成品。

```tsx
import { addPropertyControls, ControlType, useIsStaticRenderer } from "framer"
import {
    motion,
    useReducedMotion,
    useScroll,
    useTransform,
    type MotionValue,
} from "framer-motion"
import { useRef, type CSSProperties } from "react"

interface ScrollRevealTextProps {
    text: string
    inactiveColor: string
    activeColor: string
    fontFamily: "Inter" | "Big Shoulders"
    fontSize: number
    fontWeight: "400" | "500" | "600" | "700" | "800"
    lineHeight: number
    letterSpacing: number
    align: "left" | "center" | "right"
    startOffset: number
    endOffset: number
    style?: CSSProperties
}

interface CharacterProps {
    char: string
    progress: MotionValue<number>
    start: number
    end: number
    inactiveColor: string
    activeColor: string
    staticRenderer: boolean
    reducedMotion: boolean | null
}

function Character({
    char,
    progress,
    start,
    end,
    inactiveColor,
    activeColor,
    staticRenderer,
    reducedMotion,
}: CharacterProps) {
    const color = useTransform(
        progress,
        [start, end],
        [inactiveColor, activeColor]
    )
    return (
        <motion.span
            aria-hidden="true"
            style={{
                color: staticRenderer || reducedMotion ? activeColor : color,
            }}
        >
            {char}
        </motion.span>
    )
}

/**
 * @framerSupportedLayoutWidth any-prefer-fixed
 * @framerSupportedLayoutHeight auto
 */
export default function ScrollRevealText(props: ScrollRevealTextProps) {
    const {
        text = "Clear communication starts with every detail.",
        inactiveColor = "#6C767D",
        activeColor = "#F5F6F5",
        fontFamily = "Inter",
        fontSize = 48,
        fontWeight = "600",
        lineHeight = 1.12,
        letterSpacing = -0.02,
        align = "left",
        startOffset = 72,
        endOffset = 22,
        style,
    } = props
    const ref = useRef<HTMLParagraphElement>(null)
    const staticRenderer = useIsStaticRenderer()
    const reducedMotion = useReducedMotion()
    const offset: any = [
        "start " + startOffset / 100,
        "start " + endOffset / 100,
    ]
    const { scrollYProgress } = useScroll({ target: ref, offset })
    const characters = Array.from(text)
    const denominator = Math.max(characters.length, 1)
    const justifyContent =
        align === "left"
            ? "flex-start"
            : align === "right"
              ? "flex-end"
              : "center"

    return (
        <p
            ref={ref}
            aria-label={text}
            style={{
                margin: 0,
                width: "100%",
                display: "flex",
                flexWrap: "wrap",
                justifyContent,
                fontFamily,
                fontSize: fontSize + "px",
                fontWeight,
                lineHeight,
                letterSpacing: letterSpacing + "em",
                ...style,
            }}
        >
            {characters.map((char, index) => (
                <Character
                    key={index}
                    char={char === " " ? "\u00A0" : char}
                    progress={scrollYProgress}
                    start={index / denominator}
                    end={(index + 1) / denominator}
                    inactiveColor={inactiveColor}
                    activeColor={activeColor}
                    staticRenderer={staticRenderer}
                    reducedMotion={reducedMotion}
                />
            ))}
        </p>
    )
}

addPropertyControls(ScrollRevealText, {
    text: {
        type: ControlType.String,
        title: "Text",
        defaultValue: "Clear communication starts with every detail.",
        displayTextArea: true,
    },
    fontFamily: {
        type: ControlType.Enum,
        title: "Font",
        options: ["Inter", "Big Shoulders"],
        defaultValue: "Inter",
    },
    fontSize: {
        type: ControlType.Number,
        title: "Size",
        defaultValue: 48,
        min: 12,
        max: 144,
        unit: "px",
    },
    fontWeight: {
        type: ControlType.Enum,
        title: "Weight",
        options: ["400", "500", "600", "700", "800"],
        defaultValue: "600",
    },
    lineHeight: {
        type: ControlType.Number,
        title: "Line Height",
        defaultValue: 1.12,
        min: 0.8,
        max: 2,
        step: 0.01,
    },
    letterSpacing: {
        type: ControlType.Number,
        title: "Tracking",
        defaultValue: -0.02,
        min: -0.1,
        max: 0.2,
        step: 0.01,
        unit: "em",
    },
    align: {
        type: ControlType.Enum,
        title: "Align",
        options: ["left", "center", "right"],
        optionTitles: ["Left", "Center", "Right"],
        defaultValue: "left",
        displaySegmentedControl: true,
    },
    inactiveColor: {
        type: ControlType.Color,
        title: "Before",
        defaultValue: "#6C767D",
    },
    activeColor: {
        type: ControlType.Color,
        title: "After",
        defaultValue: "#F5F6F5",
    },
    startOffset: {
        type: ControlType.Number,
        title: "Start",
        defaultValue: 72,
        min: 0,
        max: 100,
        unit: "%",
    },
    endOffset: {
        type: ControlType.Number,
        title: "Finish",
        defaultValue: 22,
        min: 0,
        max: 100,
        unit: "%",
    },
})
```

## 可编辑 Properties

| Property | 当前默认值 | 范围 / 作用 |
|---|---:|---|
| Text | `Clear communication starts with every detail.` | 多行 String；实际输出按字符处理 |
| Font | `Inter` | `Inter` 或 `Big Shoulders` |
| Size | `48px` | 12–144px |
| Weight | `600` | 400 / 500 / 600 / 700 / 800 |
| Line Height | `1.12` | 0.8–2 |
| Tracking | `-0.02em` | -0.1–0.2em |
| Align | Left | Left / Center / Right，控制 flex 对齐 |
| Before | `#6C767D` | 未完成字符颜色 |
| After | `#F5F6F5` | 已完成字符颜色，同时用于静态和 reduced-motion fallback |
| Start | `72%` | Scroll target 起始位置 |
| Finish | `22%` | Scroll target 结束位置 |

### 已验证实例

`/reveal-text-test` 当前仅有一个 Desktop 实例：可用宽度为 Fill，文字尺寸 `64px`、字重 `700`、行高 `1.08`、Tracking `-0.04em`、Left 对齐、Before `#6C767D`、After `#F5F6F5`、Start `78%`、Finish `22%`。测试页采用深蓝表面，内容容器最大宽度 `900px`、内边距 `96px 64px`、高度 `1628px`。

Framer 实例读回使用 `$control__font`、`$control__size`、`$control__weight`、`$control__tracking`、`$control__before`、`$control__after`、`$control__start` 和 `$control__finish` 等键；这些键与源码 Props 的命名并不完全一致。复用或改名控制项前先 readback 控制面板，不能依据源码自行推断 Instance 属性键。

## 响应式与可访问性边界

- 组件根可换行且宽度 Fill；这不等于其大字号文本已在窄屏通过验证。
- 当前没有 Tablet 或 Phone 实例，也没有字长、宽度或不同语言的替换压力测试。新项目必须独立确定字号、行高、字距、换行、Start / Finish，并在 320 / 390 / 810 / 1200 / 1440+ 复测。
- Root `<p>` 提供整段 `aria-label`；字符 spans 全部 `aria-hidden`。保留这一组合，避免辅助技术逐字朗读。
- 静态 renderer 和 `useReducedMotion()` 都输出 After 色；不要把可见内容、CTA 或唯一信息只放在滚动前的 Before 色。
- Before / After 与其背景的对比度必须在新表面单独审查；本组件不保证任何配色组合合规。

## 实施与替换顺序

1. 确认该文案不是唯一关键内容，也不违反项目的 Custom Code / Marketplace scope。
2. 在 Framer Code Components 中复用或复制此实现；保留默认导出、布局注释、typed props 和 `framer-motion` imports。
3. 先在独立测试 Section 放置单个实例，设置文案、字体、颜色、Start / Finish 和 Fill 宽度。
4. 分别检查静态画布、reduced motion 与真实滚动；再放入目标页面，不要先替换正式 Home 标题。
5. 分别设定 Desktop、Tablet、Phone 实例的排版与滚动区间。若正文变成很长或多语言内容，放弃此模式，改用普通 Rich Text 或更粗粒度的分段 reveal。
6. 若将测试页纳入 Marketplace，补齐它的 Metadata、导航可达性和编辑说明；否则在发布前经确认移除测试页和不再使用的代码文件。

## 验证矩阵

| 检查 | 已有证据 | 新项目必须补充 |
|---|---|---|
| Source / export / typecheck | Default export `ScrollRevealText`；0 diagnostics | 改码后重新 typecheck |
| Static / reduced motion | 源码明确输出 After 色 | Canvas 和真实 reduced-motion 环境各确认一次 |
| Desktop geometry | 单一 1200px 测试页实例 | 目标页面文本与容器宽度 |
| Tablet / Phone | 无 | 810 / 390 / 320px 的换行、文字大小和滚动节奏 |
| Scroll behavior | 结构已读回；视觉未验证 | 一次真实从 Start 到 Finish 的滚动路径 |
| Accessibility | 语义和 `aria` 结构已读回 | 对比度、键盘阅读与屏幕阅读器抽查 |

## 失败模式与修复

| 现象 | 原因 | 修复 |
|---|---|---|
| 长文滚动卡顿 | 每个字符都会创建一个 motion span 和 transform | 缩短文案；改为逐词或分段 reveal；不要用于 CMS 长文 |
| Emoji / 组合字符显示不自然 | `Array.from` 处理 code point，不等同于用户感知的 grapheme cluster | 避免 emoji / 复杂组合文字；需要支持时改用 grapheme 分词并重新测试 |
| 窄屏出现糟糕断行 | Root 允许 wrap，但字号和 Tracking 仍由实例决定 | 为 Phone 独立降低字号 / 调整 Tracking，或使用普通文本 |
| 静态画布看起来已完成 | static renderer 有意直接使用 After 色 | 在 Preview 才判断滚动动画，不把静态状态当作交互证据 |
| 颜色过渡不可读 | Before 色与背景对比不足 | 提高 Before 对比度，或让该效果只用于非关键信息 |
| 实例控制项写入无效 | Framer 控制键与源码 Props 名不同 | 每次先 readback 当前 controls / instance，不猜 `$control__*` 名称 |

## 保留的不确定性

这是 Submit Roofing 的开发测试，不是已批准的 Home 体验，也未完成视觉或交互 Preview。它保留为 Advanced Design **Reference**，供需要逐字符滚动显色的项目有选择地读取；在其经过多端、性能、无障碍和真实页面验证前，不应升级为 Canonical。
