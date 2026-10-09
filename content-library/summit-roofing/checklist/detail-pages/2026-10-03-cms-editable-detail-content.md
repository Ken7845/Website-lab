# CMS-editable Detail Content — Request Checklist

- Contract schema: 1
- Component contract: N/A — this request changes page-local CMS fields and bindings, not a reusable Component definition.
- Visual contract: N/A — the request repairs existing detail sections within the established visual system; it does not introduce a new page composition or visual direction.
- Authorization: Authorized — user request, 2026-10-03.

## User request (verbatim)

> yes. what I mean is making the CMS detail page content-editable. There content should fit the image. What should be fixed includes the project pages and insight pages. btw the Record Metadata Sheet and Demo Detail Status in the project detail page is bad and revise it.  Also the Article Record and Editable Content Note section in the insight detail page. If you can't find a suitable image to match the section, you can use the text-rich article to fill the room. For example, in the Editable Content Note you can write a detail plan with maybe ten rows. This will make the website more rich in content.

## Scope lock

- **Modify:** the `Projects` and `Insights` CMS schemas; the `/projects/:Projects` and `/insights/:Insights` detail-page bindings and named content sections, across their existing Desktop, Tablet and Phone breakpoints.
- **Reuse:** Site Shell, Button, shared styles, typography, colour palette, square geometry, existing CMS image fields and their factual Alt text, archive-to-detail links, and established CTA destinations.
- **Add:** editable rich-text body fields for both collections, plus only page-local CMS-bound presentation needed to make the body responsive and readable alongside the item image.
- **Content:** populate the new editable body fields with coherent **Demo** reference content. Do not add verified business claims, pricing, licensing, awards, warranties, real addresses, customer quotes, or unsupported project outcomes.
- **No-op:** archive structure, shared component definitions, Navbar, Footer, service pages, Home, Contact, forms, Custom Code, image uploads/reassignment, publishing, and brand-name resolution.

## Constraint lock

- Project Detail remains an individual record, not a fabricated case study. Its revised metadata/status sections should become useful CMS-driven editorial content rather than template-status filler.
- Insight Detail remains reading-first. Its Article Record and Editable Content Note should become a coherent CMS-backed article body; the content may use a detailed ten-row plan when an additional suitable image is not available.
- The same item Image should remain the image source; content should be sized and sequenced to complement, not compete with, that image.
- The user’s new CMS-editability request overrides the older page-contract restrictions against CMS fields and long-form content, but not the project’s Demo/fact boundaries.

## Follow-up constraint lock — Insight Article Body depth

- **Modify:** Expand the `Article Body` rich-text content for both existing `Insights` CMS items: `roof-inspection` and `replacement-signs`.
- **Preserve:** Current titles, slugs, categories, summaries, images/Alt text, ten-item Checklist Steps, CMS schema, detail-page bindings, section order, layout, archive routes, and CTA.
- **Content direction:** Replace placeholder copy with substantial, distinct homeowner education that matches each item’s image and topic. Ground technical statements in authoritative roofing sources; retain generic Demo/template status internally.
- **Do not add:** New CMS items/fields, author/date/credential claims, prices, warranties, service-area claims, company capabilities, diagnosis of the pictured property, or instructions for homeowners to access a roof.
- **Verify:** Read back both complete rich-text bodies and word counts; confirm the CMS item count, checklist values, image/Alt, and existing Article Body binding remain unchanged. Runtime/visual acceptance is separate from the content readback.

## Verification plan

- Read back both collection schemas and the first/middle/last available collection items after the update.
- Confirm every new body field is bound on each corresponding detail page at Desktop, Tablet and Phone, with one CMS-bound H1 and valid existing routes/CTAs.
- Inspect the four revised named sections for responsive reading order and preservation of the existing image binding/Alt.
- Run targeted Framer QA and record the scoped result in the two canonical page checklists and current project status.

## Result

- Structural status: Pass — new fields are populated and bound to each corresponding detail page at Desktop, Tablet and Phone; existing CMS image/Alt and route bindings remain intact.
- Visual status: Pass — one bounded Desktop screenshot per page confirms the image-led reading sequence and the revised named sections.
- Known limits: 320px / 1440px stress and Preview are not part of this request; inherited placeholder-Rect linter warnings are not treated as rendered overlap because the bounded screenshots show the scoped sections in a continuous reading order.

## Follow-up result — Insight Article Body depth (2026-10-09)

- Structural status: Pass — `roof-inspection` now has 830 words across 22 rich-text blocks; `replacement-signs` has 913 words across 23 blocks. Both bodies use semantic H2 and paragraph blocks and remain in the existing `Article Body` field.
- Content direction: The inspection article covers scope, connected roof details, interior clues, observed evidence, useful reporting, questions, and records. The repair/replacement article covers localized repair considerations, broader replacement factors, recover vs. replacement, proposal scope, uncertainty, and next steps. Technical statements are qualified and grounded in ARMA/NRCA guidance; no pictured home is diagnosed.
- Preservation: The two-item collection, titles, slugs, categories, summaries, CMS images/Alt, `Checklist Steps` arrays, CMS schema, page structure, detail routes, and CTA remain unchanged. The Article Body variable remains bound on Desktop, Tablet, and Phone.
- Visual/runtime status: N/A for this text-only CMS edit; no image, layout, or interaction changed. This is not a new page-level visual or runtime acceptance claim.
- Scope retained: No author/date/credential claims, prices, warranties, service-area claims, additional CMS items/fields, or publishing.
