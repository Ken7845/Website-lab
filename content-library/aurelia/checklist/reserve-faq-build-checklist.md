# AURELIA Reserve FAQ — Build and QA Checklist

Scope: FAQ section on `/reserve`, located after the native reservation request form and before the shared Footer.  
Reference direction: spacious editorial accordion on its own full-width soft-grey surface; fine horizontal separators, dark question at left and dark plus/minus trigger at right.  
Constraint: this record does not change the native form’s delivery destination. Its existing `Send To` setting remains project-owned.

## Build requirements

- [x] Create one reusable `FAQ Row` component with editable `Question` and `Answer` properties.
- [x] Provide `Closed` and `Open` variants connected with the existing Variant-to-Variant interaction pattern.
- [x] Closed is the default instance state; answers are hidden rather than clipped.
- [x] Use the existing Feather `Plus` and `Minus` icons; do not substitute text symbols.
- [x] Reuse existing AURELIA Text Styles and Color Tokens; do not create a duplicate type style merely for FAQ.
- [x] Add the `Reservation FAQ` section after the existing form/fallback content and before Footer.
- [x] Keep the FAQ surface separate from Reserve Detail/form; outer section, content wrapper and bordered-row list have no `max-width`.
- [x] Keep questions on the larger existing style and answers on the smaller existing Type/Body style.
- [x] Light-surface contrast is explicit: Text for primary questions/icons, Muted for answers, and the original light-grey divider system.
- [x] Add eight buyer-editable FAQ instances with complete fictional reference answers; visible answers do not contain instruction-style `Demo answer` placeholders.
- [x] Label the section and each layer/component with its content responsibility.

## Interaction and accessibility

- [x] Entire question row is clickable and uses a button semantic.
- [ ] Enter and Space toggle each FAQ row; no keyboard trap or accidental text selection.
- [ ] Visible focus treatment is present and remains legible on the white surface.
- [x] Plus/minus indicator changes with the current Open/Closed state.
- [ ] Answer content is available to assistive technology only when its row is open.
- [x] Question and answer use `userSelect: none` to prevent selection during toggling.
- [x] Hover treatment is present on pointer devices and does not become a mobile-only dependency.
- [x] Open/Closed/Hover states use `spring-physics 250 30 1 0s`; press feedback is a subtle `0.98` scale.
- [ ] Motion remains non-essential under Reduced Motion in Preview.

## Responsive and visual QA

- [x] Desktop, Tablet, and Phone section hierarchy is structurally read back with breakpoint-specific gutters and no FAQ parent/list `max-width`.
- [ ] Test 320, 390, 599, 810, 1200 and 1440+ widths for overflow, clipping, text collision and separator alignment.
- [ ] Question text wraps cleanly while the icon remains aligned at the row edge.
- [ ] Long question and 2× answer-copy test passes.
- [ ] Open answers preserve readable measure and spacing; rows do not jump or overlap.
- [ ] Horizontal rules fill the intended content width, including expanded state.
- [ ] Font, weight, line-height, color and spacing match the existing Reserve visual system.
- [ ] Check hover, open, closed, focus, keyboard, touch and reduced-motion states in Preview.

## Buyer-editing and release proof

- [ ] A buyer can change all eight questions/answers from instance Properties without entering component internals.
- [ ] Buyer guide explains where to change FAQ copy and confirms demo policy answers must be replaced before production use.
- [ ] Reserve checklist and Marketplace audit record the new FAQ and final QA result.
- [ ] Capture one bounded Desktop and one Phone screenshot of the FAQ open state for final regression evidence.
