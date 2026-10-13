import { addPropertyControls, ControlType, useIsStaticRenderer } from "framer"
import {
    useEffect,
    useRef,
    useState,
    startTransition,
    type CSSProperties,
} from "react"
import { useInView } from "framer-motion"

interface CounterProps {
    value: number
    decimals: number
    prefix: string
    suffix: string
    duration: number
    color: string
    fontFamily: string
    fontSize: number
    fontWeight: number
    letterSpacing: string
    lineHeight: string
    style?: CSSProperties
}

/**
 * Counter
 *
 * Counts up to a value the first time it scrolls into view.
 *
 * @framerIntrinsicWidth 120
 * @framerIntrinsicHeight 58
 *
 * @framerSupportedLayoutWidth auto
 * @framerSupportedLayoutHeight auto
 */
export default function Counter(props: CounterProps) {
    const {
        value = 100,
        decimals = 0,
        prefix = "",
        suffix = "",
        duration = 2,
        color = "#0A0A0A",
        fontFamily = "Switzer",
        fontSize = 48,
        fontWeight = 500,
        letterSpacing = "-0.04em",
        lineHeight = "1.2em",
    } = props

    const ref = useRef<HTMLSpanElement>(null)
    const isInView = useInView(ref, { once: true, amount: 0.4 })
    const isStatic = useIsStaticRenderer()
    const [progress, setProgress] = useState(0)

    useEffect(() => {
        if (isStatic || !isInView) return
        let frame = 0
        let startTime: number | null = null
        const safeDuration = Math.max(0.1, duration) * 1000
        const step = (now: number) => {
            if (startTime === null) startTime = now
            const t = Math.min(1, (now - startTime) / safeDuration)
            const eased = 1 - Math.pow(1 - t, 3)
            startTransition(() => setProgress(eased))
            if (t < 1) frame = requestAnimationFrame(step)
        }
        frame = requestAnimationFrame(step)
        return () => cancelAnimationFrame(frame)
    }, [isInView, isStatic, duration])

    const shown = isStatic ? value : value * progress

    return (
        <span
            ref={ref}
            style={{
                position: "relative",
                display: "inline-block",
                minWidth: "max-content",
                whiteSpace: "nowrap",
                fontVariantNumeric: "tabular-nums",
                fontFamily,
                fontSize,
                fontWeight,
                letterSpacing,
                lineHeight,
                color,
            }}
        >
            {prefix}
            {shown.toFixed(decimals)}
            {suffix}
        </span>
    )
}

addPropertyControls(Counter, {
    value: {
        type: ControlType.Number,
        title: "Value",
        defaultValue: 100,
        min: 0,
        max: 1000000,
        step: 1,
    },
    decimals: {
        type: ControlType.Number,
        title: "Decimals",
        defaultValue: 0,
        min: 0,
        max: 3,
        step: 1,
        displayStepper: true,
    },
    prefix: { type: ControlType.String, title: "Prefix", defaultValue: "" },
    suffix: { type: ControlType.String, title: "Suffix", defaultValue: "+" },
    duration: {
        type: ControlType.Number,
        title: "Duration",
        defaultValue: 2,
        min: 0.2,
        max: 6,
        step: 0.1,
        unit: "s",
    },
    color: { type: ControlType.Color, title: "Color", defaultValue: "#0A0A0A" },
    fontFamily: {
        type: ControlType.String,
        title: "Font",
        defaultValue: "Switzer",
    },
    fontSize: {
        type: ControlType.Number,
        title: "Size",
        defaultValue: 48,
        min: 8,
        max: 160,
        step: 1,
        unit: "px",
    },
    fontWeight: {
        type: ControlType.Number,
        title: "Weight",
        defaultValue: 500,
        min: 100,
        max: 900,
        step: 100,
        displayStepper: true,
    },
    letterSpacing: {
        type: ControlType.String,
        title: "Tracking",
        defaultValue: "-0.04em",
    },
    lineHeight: {
        type: ControlType.String,
        title: "Line Height",
        defaultValue: "1.2em",
    },
})

Counter.displayName = "Counter"
