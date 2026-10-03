# Anti-slop reference map

Use this map when a design critique, greenfield direction, or copy/visual audit needs the detailed upstream rules. The complete source remains unchanged in [original-design-taste.md](original-design-taste.md).

Do not read the archive from top to bottom. First locate headings:

```bash
rg -n '^## |^### ' .agents/skills/design-taste/references/original-design-taste.md
```

Then read only the relevant section.

## Topic routing

| Need | Archive section |
|---|---|
| Brief inference and design dials | `0. BRIEF INFERENCE`, `1. THE THREE DIALS` |
| Typography, palette, layout, imagery, content density | `4. DESIGN ENGINEERING DIRECTIVES` |
| Contextual creative devices | `5. CONTEXT-AWARE PROACTIVITY` |
| Pattern names and design vocabulary | `10. REFERENCE VOCABULARY` |
| Preserve-mode redesign audit | `11. REDESIGN PROTOCOL` |
| Detailed AI-tell catalog | `9. AI TELLS` |
| Original all-purpose preflight | `14. FINAL PRE-FLIGHT CHECK` |

## Interpretation rule

The archive mixes three classes of statement:

1. Universal integrity: truthful facts, readable contrast, keyboard/focus access, reduced-motion support, and functional responsive behavior.
2. Strong bias correction: common AI-template patterns worth challenging.
3. Upstream aesthetic or implementation defaults: fonts, themes, stacks, breakpoints, icon libraries, and absolute style bans.

Apply class 1. Treat class 2 as an audit prompt. Apply class 3 only when the current project, platform, and user direction support it.

An approved project's typography, cursor, theme transitions, copy punctuation, or component language is not invalid merely because it conflicts with an upstream anti-default preference.

The archive's `Section-Layout-Repetition Ban` and its “at least 4 different families across 8 sections” check are class 2 bias-correction heuristics, not active hard requirements or numeric quotas. The active Skill permits functionally justified reuse—including repeated Contact, CTA, form and shared-system layouts—and rejects site-wide layout monoculture or unreasoned mechanical copying. Judge the distribution across the page and website; do not require every Section to be unique.
