# Frontend implementation reference map

Load this reference only for code-based web implementation. It is not part of ordinary Framer work.

The complete upstream content is preserved verbatim in [original-design-taste.md](original-design-taste.md). Locate its headings first and read only the selected range:

```bash
rg -n '^## |^### |^# APPENDICES' .agents/skills/design-taste/references/original-design-taste.md
```

## Topic routing

| Need | Archive section |
|---|---|
| React, Next.js, Tailwind, state, fonts, icons, dependencies | `3. DEFAULT ARCHITECTURE & CONVENTIONS` |
| Official design-system selection | `2. BRIEF → DESIGN SYSTEM MAP` |
| Web performance and accessibility implementation | `6. PERFORMANCE & ACCESSIBILITY GUARDRAILS` |
| Dial-to-technical behavior | `7. DIAL DEFINITIONS` |
| CSS-variable or Tailwind dark mode | `8. DARK MODE PROTOCOL` |
| Reusable code-block schema | `12. THE BLOCK LIBRARY` |
| Package installation and official source links | `Appendix A`, `Appendix B` |
| Liquid Glass web approximation | `Appendix C` |

## Platform boundary

- Inspect the existing repository and dependencies before selecting a framework or package.
- Do not import React/Next/Tailwind defaults into a Framer-native project.
- Existing project architecture and user direction outrank the archived default stack.
- Official packages, paid dependencies, and Custom Code still require the repository's authorization rules.
- Treat version-sensitive package commands and external links as historical source material until verified for the current task.
