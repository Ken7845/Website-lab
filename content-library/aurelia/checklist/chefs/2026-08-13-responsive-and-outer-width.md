# Chefs Responsive and Outer Width Revision — 2026-08-13

Page: Chefs  
Path: `/chefs`  
Status: Partial pass — live wide-Preview and interaction QA still required

## Original request (verbatim)

> 你没有做响应式，做一下响应式，然后用checklist审查一下，汇报一下checklist进程，preview两边拉开后两侧是黑色，我发现你很喜欢加Max width，这个给一些组件可以，但是不要给最外层加这个max，这一点要写进basic里面的文件，然后注意你做响应式的话手机的portrait不要变

## Scope

- [x] Inspect existing Desktop, Tablet, and Phone Chefs page width ownership and instance selection.
- [x] Remove outer page/content `max-width` that caused black side bands when the Preview viewport was wider than the authored Desktop canvas.
- [x] Keep `max-width` only on genuinely bounded inner content needed for readable text or a component contract.
- [x] Make the authored Tablet and Phone layouts responsive without changing Phone portrait dimensions, aspect ratio, image fill, or focal treatment.
- [x] Run the Chefs page routed Checklist and record Pass / Fix Required / Blocked evidence.
- [x] Add the outer-page-width rule to Framer Basic guidance.

## Constraint lock

- Do not modify chef names, Demo story copy, portrait assets, shared Navbar, Footer, or global navigation.
- Do not change Phone portrait size or crop as part of responsive work.
- Do not mistake structural readback for Preview evidence.

## Latest Part Result

Scope: Chefs responsive revision and outer-width correction
Status: Partial pass — production content and real Preview interaction QA remain open

### Pass

- All three authored page breakpoints use natural height: Desktop 1200, Tablet 810, and Phone 390.
- The outer Chefs Content and both full-bleed sections are 100% width with no `max-width`; their white fills now own the full page width.
- A 1200px on-demand desktop screenshot was visually reviewed after the correction. The canvas is white edge-to-edge; no black side bands appear within that capture.
- Width limiting now belongs only to inner layers: the Opening Inner wrapper (1440px), Desktop profile list (1440px), Tablet profile list (754px), and Phone profile list (350px).
- Tablet profile instances now fill the 754px inner list and use their dedicated Tablet collapsed component variant.
- Phone retains its dedicated Phone collapsed component variant and 350px instance width. The collapsed and expanded Phone portrait frames remain 350 × 440px with the same image fills and clipped image treatment; this revision did not alter them.
- Basic guidance and its build checklist now explicitly prohibit `max-width` on the outer Page Content and full-bleed Sections; only inner wrappers/components may be bounded.

### Fix required

- Test the actual external Preview at 1440px+ and 320px. The desktop on-demand screenshot is evidence at 1200px only, not a substitute for a wide interactive Preview.
- Perform live keyboard, focus, open/close, Reduced Motion, long-name, long-story, missing-role, and replacement-image tests.
- Replace visible Demo identities, roles, stories, image alt text, and page metadata with approved production material before publishing.

### Blocked / evidence limits

- A requested Phone visual capture did not finish downloading within the permitted single attempt. Phone portrait preservation is therefore confirmed by structural readback, not by a new rendered screenshot.
- Existing Framer layout lint still reports a generic full-bleed-content width warning. It is intentionally not followed here because the user explicitly requires the outer page layer to remain unbounded; the inner content layers now provide the required width control.
