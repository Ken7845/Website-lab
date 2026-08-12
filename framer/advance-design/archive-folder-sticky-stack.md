# Framer archive folder sticky stack

Created for Ken Studio Works on 2026-07-14.

## Goal

Create a folder-stack scroll effect for the Works archive:

- The first archive folder reaches the sticky position and stays pinned.
- The second archive folder scrolls upward and overlaps the first folder body.
- Folder tabs remain visible and do not overlap.
- The later folder uses a higher layer and a slightly different neutral surface color.

## Framer-native structure

```text
Works Archive
├── Observation folder
│   ├── Observation tab
│   └── Observation sheet
├── Creation folder
│   ├── Creation tab
│   └── Creation sheet
└── Archive Stack Scroll Space
```

## Key settings

- Use `position: sticky` on each folder wrapper.
- Give the first folder the lower sticky top.
- Give the second folder a sticky top offset by roughly one tab height.
- Give the later folder the higher z-index.
- Add scroll space after the folders so the overlap has room to happen.
- Keep folder body colors close, but not identical.

For the Ken Studio Works desktop version:

```text
Observation sticky top: around navigation height + 24px
Creation sticky top: Observation sticky top + tab height
Observation z-index: lower
Creation z-index: higher
```

## Motion rule

The stack geometry should not be animated.

Do not animate:

- folder top
- folder height
- folder layout
- folder stack gap

Only animate preview content, such as:

- hover image opacity
- preview y-offset
- cursor-preview component transitions

## Row component rule

Archive rows should be native Framer components where possible.

For Ken Studio, the reusable row component is:

```text
Archive Option Row
├── Number
├── Title
├── Meta
└── Status
```

Use this for Creation records first, then optionally migrate Observation rows once the row system is finalized.

2026-07-14 update: Observation and Creation now use the same component.

The preferred maintenance model is:

- One component: `Archive Option Row`
- Structural variants only: Desktop and Phone, plus the minimum pointer-only Hover Gesture Variant; normally this is one shared `Desktop Hover`, not a duplicated `Phone Hover`
- Component Properties control number, title, meta, status, base fill, and hover fill
- Page instances control the real content, route/link, and custom cursor preview
- New work means duplicating an instance and changing its properties, not duplicating a record variant

This is cleaner than hand-building rows or creating a full variant set per record. A new work should not add Desktop + Phone + Hover copies inside the component.

The Ken Studio Campus row is the reference maintenance pattern:

```text
Archive Option Row / Desktop
└── Campus page instance
    ├── Number: 02
    ├── Title: Campus
    ├── Meta: PHOTOGRAPHY
    └── Cursor Variant: Campus
```

Content lives on the instance. The component remains a template.

Important hover-preview note:

When rows are placed as component instances, the custom cursor preview needs to be checked on the page instance as well as inside the component variant. If the preview disappears after componentizing rows, reselect each desktop/tablet row instance and apply the custom cursor component + matching preview variant there.

The row brightening state belongs to the shared component. Create one Hover Gesture Variant, expose hover fill as an instance property, and let every project row supply only its color/content values. Do not add per-record hover copies or a touch-only hover variant without a verified pointer requirement.

Phone should not reuse the exact desktop row layout. Use phone-specific row variants:

```text
Phone row
├── Number + Title
└── Status
```

Hide secondary metadata on phone unless the project specifically needs it. This prevents long titles from being squeezed into a vertical one-letter column.

## Tab offset rule

When stacking folders, offset tabs horizontally rather than relying only on vertical offset.

Recommended reading:

```text
Observation tab: left
Creation tab: shifted right
Folder bodies: same vertical layer during sticky overlap
```

On phone, reduce tab widths before increasing offsets. The tab should remain readable without pushing the second tab off canvas.

## Content rule

Do not link a row until its detail route is confirmed.

For Creation records, the row can exist as an archive item while showing:

```text
ROUTE TO CONFIRM
```

This avoids accidentally linking a website project to the category page.

## Row component checklist after componentizing

When archive rows are converted into a reusable component, do not assume the page still behaves the same. Componentizing can silently reset or hide instance-level settings.

After creating or replacing row components, check this matrix before moving on:

| Check | Why it matters |
|---|---|
| Component variants | Keep only structural/responsive and gesture variants; no record-specific copies. |
| Page instances | Each instance must contain the correct title, number, meta, fill, link and cursor values. |
| Custom cursor | Cursor preview often disappears after componentizing because the page instance no longer has the cursor binding. |
| Hover state | Hover should be a component hover variant or gesture state, not only a guessed outer effect. |
| Links | Only add links after the route exists and is confirmed. |
| Desktop / Tablet / Phone | Every breakpoint must select the correct row variant, especially phone-specific variants. |

For Ken Studio Works, the repeated bug pattern was:

```text
Row looked correct inside component
→ page instance still had old/default controls
→ preview or text appeared wrong in the actual page
```

The fix is to verify both layers:

```text
Archive Option Row component
└── Desktop / Phone / Hover structure + content/fill properties

Page folder
└── component instances / property values / custom cursor bindings
```

Never finish a component migration after checking only the component canvas.

## Responsive row rules

Phone rows should use one shared Phone structural variant, not a Phone variant per record and not a squeezed Desktop row.

Recommended phone row structure:

```text
Phone row
└── Title Group
    ├── Number: fixed width
    └── Title: 1fr
```

Keep the row stable:

- Give the number column enough fixed width, usually around `32–40px`.
- Give the title `1fr` so it owns the remaining space.
- Hide or reduce meta/status on phone unless it is essential.
- Increase vertical padding slightly if numbers visually collide with divider lines.
- Keep hover effects from changing size; use background/fill changes instead.

If text becomes one character per line, inspect in this order:

1. Is the parent too narrow?
2. Is the text node using `auto` where it should use `1fr`?
3. Is a horizontal stack squeezing multiple fixed-width children?
4. Is the phone instance still using a desktop variant?
5. Did a hidden status/meta column keep consuming width?

Do not fix this by randomly reducing font size first. The root cause is usually layout constraints.

## Width responsiveness rule

For archive folders and project rows, decide which layer owns the width:

```text
Folder sheet owns available width
└── Project Index fills sheet width
    └── Row instances fill index width
```

The component editing canvas may still show fixed visual widths such as `1044px` or `330px`; that is acceptable for component editing. What matters on the page is that the placed instances and their parent index containers fill the folder width.

Check page instances with targeted reads:

```text
Project Index: width 1fr / max 100%
Row instance: width 1fr / max 100%
```

If the folder width changes but rows do not respond, inspect the parent chain from the sheet down to the row instance. One fixed-width wrapper anywhere in the chain can break responsiveness.
