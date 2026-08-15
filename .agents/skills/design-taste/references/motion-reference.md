# Web motion reference map

Use this map only when implementing motion in a code-based website or when studying the upstream rationale. For Framer-native interactions, use the `framer-interactions` Skill and the Framer references instead.

The untouched source is [original-design-taste.md](original-design-taste.md). Locate headings, then load only the required section:

```bash
rg -n '^## 5|^### 5\.|^## 6|^### 6\.' .agents/skills/design-taste/references/original-design-taste.md
```

## Topic routing

| Need | Archive section |
|---|---|
| Motion motivation and intensity | `5. CONTEXT-AWARE PROACTIVITY` |
| GSAP sticky stack | `5.A Sticky-Stack` |
| GSAP horizontal pan | `5.B Horizontal-Pan` |
| Motion reveal stagger | `5.C Scroll-Reveal Stagger` |
| Forbidden scroll/state patterns | `5.D Forbidden Animation Patterns` |
| Transform/opacity, Reduced Motion, DOM/GPU cost | `6. PERFORMANCE & ACCESSIBILITY GUARDRAILS` |

## Interpretation rule

- Every animation needs a hierarchy, storytelling, feedback, or state-change purpose.
- Honor Reduced Motion and keep content usable without animation.
- Treat code skeletons, library choices, and numeric springs as implementation references, not universal brand defaults.
- Preserve the existing project's motion language before adding intensity or a new library.
